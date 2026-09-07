"""Offline source/format checks; these do not evaluate a model or real MCP."""
import hashlib
import importlib.util
import json
from pathlib import Path
import re
import shutil
import sys
import tempfile
import unittest
from unittest.mock import patch
from urllib.parse import urljoin
import zipfile

ROOT = Path(__file__).resolve().parents[1]
SNAPSHOT = ROOT / ".agents/skills/openshift-docs/references/devspaces-3.29"
LOCK = json.loads((ROOT / "tools/docs/devspaces.lock.json").read_text())
ARCHIVE = ROOT / "tools/docs" / LOCK["archive"]


class DevSpacesIntegrityTest(unittest.TestCase):
    def test_all_installed_files_match_manifest(self):
        source = json.loads((SNAPSHOT / "SOURCE.json").read_text())
        hashes = source["integrity"]["files"]
        actual = {p.relative_to(SNAPSHOT).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
                  for p in SNAPSHOT.rglob("*") if p.is_file() and p.name != "SOURCE.json"}
        self.assertEqual(actual, hashes)
        manifest = "".join(f"{value}  {path}\n" for path, value in sorted(actual.items()))
        self.assertEqual(hashlib.sha256(manifest.encode()).hexdigest(), LOCK["expected_output"]["content_manifest_sha256"])
        self.assertEqual(source["artifact"]["converted_topics"], 302)
        self.assertEqual(source["artifact"]["assets"], 46)
        self.assertEqual(source["archive_sha256"], LOCK["archive_sha256"])

    def test_source_archive_and_portable_inventory(self):
        self.assertEqual(hashlib.sha256(ARCHIVE.read_bytes()).hexdigest(), LOCK["archive_sha256"])
        with zipfile.ZipFile(ARCHIVE) as z:
            manifest = json.loads(z.read("MANIFEST.json"))
            for row in manifest["files"]:
                self.assertEqual(hashlib.sha256(z.read(row["path"])).hexdigest(), row["sha256"])
                self.assertRegex(row["response_sha256"], r"^[0-9a-f]{64}$")
                self.assertTrue(row["retrieved_at"].startswith("2026-09-07"))
            self.assertEqual(len(manifest["inventory"]), 302)
            index = json.loads((SNAPSHOT / "search-index.json").read_text())
            self.assertEqual({row["path"] for row in index}, {slug + ".md" for slug in manifest["topics"]})
            self.assertEqual(len(index), 302)
            self.assertTrue(manifest["external_references"])
            self.assertTrue(manifest["exclusions"])

    def test_attribution_and_nonempty_license(self):
        legal = (SNAPSHOT / "LEGAL-NOTICE.md").read_text()
        self.assertIn("Section 4d", legal)
        self.assertIn("Copyright", legal)
        license_text = (SNAPSHOT / "LICENSE.md").read_text()
        self.assertIn("Attribution-ShareAlike 3.0", license_text)
        self.assertGreater(len(license_text), 18000)
        for row in json.loads((SNAPSHOT / "search-index.json").read_text()):
            text = (SNAPSHOT / row["path"]).read_text()
            self.assertIn(LOCK["document"]["base_url"] + Path(row["path"]).stem, text)
            self.assertIn("Copyright Red Hat", text)


@unittest.skipUnless(importlib.util.find_spec("bs4") and shutil.which("pandoc"),
                     "requires optional pinned Dev Spaces importer dependencies")
class DevSpacesConversionTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        spec = importlib.util.spec_from_file_location("devspaces_import", ROOT / "tools/docs/import_devspaces.py")
        cls.importer = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(cls.importer)

    def test_all_document_text_tables_code_images_survive(self):
        module = self.importer
        with zipfile.ZipFile(ARCHIVE) as z:
            for path in z.namelist():
                if not path.startswith("topics/"):
                    continue
                with self.subTest(topic=path):
                    original = module.prepare_html(module.soup(z.read(path)))
                    module.verify_conversion(original, (SNAPSHOT / (Path(path).stem + ".md")).read_text())

    def test_all_local_markdown_and_html_links_and_images_resolve(self):
        generated = {path.relative_to(SNAPSHOT).as_posix(): path.read_bytes()
                     for path in SNAPSHOT.rglob("*") if path.is_file()}
        self.assertGreater(self.importer.verify_generated(generated), 1000)
        for path, data in generated.items():
            if path.endswith(".svg"):
                self.assertNotRegex(data.decode(), r"<script|(?:href|src)=[\"']https?://")

    def test_source_inventory_is_complete_and_version_scoped(self):
        module = self.importer
        manifest, files = module.load_archive(LOCK, ARCHIVE)
        toc = module.soup(files["inventory.html"])
        urls = {urljoin(LOCK["document"]["toc_url"], a["href"]) for a in toc.select("a[href]")}
        self.assertEqual(urls, set(manifest["inventory"]))
        for url in urls:
            self.assertIn("topics/" + module.local_topic(url, LOCK["document"]) + ".html", files)

    def test_fail_closed_on_corruption_or_unversioned_source(self):
        module = self.importer
        changed = json.loads(json.dumps(LOCK))
        changed["document"]["version"] = "latest"
        with self.assertRaises(ValueError):
            module.definition(changed)
        changed = json.loads(json.dumps(LOCK))
        changed["archive_sha256"] = "0" * 64
        with self.assertRaises(ValueError):
            module.load_archive(changed, ARCHIVE)
        with tempfile.TemporaryDirectory() as temp:
            with self.assertRaises(ValueError):
                module.build(LOCK, ARCHIVE, Path(temp))

    def test_conversion_rejects_missing_rows_code_and_images(self):
        module = self.importer
        for fragment, incomplete in (
            ("<table><tr><th>A</th></tr><tr><td>B</td></tr></table>", "| A |\n|---|\n"),
            ("<pre>oc get pods\noc get events</pre>", "```\noc get pods\n```"),
            ('<img src="assets/a.png" alt="Diagram"/>', "Diagram"),
            ("<p>A required prerequisite.</p>", "Different prose."),
        ):
            with self.assertRaises(ValueError):
                module.verify_conversion(module.soup(fragment), incomplete)

    def test_table_anchors_code_pipes_tabs_and_adjacent_blocks(self):
        module = self.importer
        source = module.prepare_html(module.soup('''
            <h1 id="title">Fixture</h1>
            <table><tr><th id="column">Mode</th></tr>
            <tr><td><code>basic|cluster</code></td></tr></table>
            <pre><code>oc get pods</code></pre><pre><code>spec:\n\tvalue: test</code></pre>
            <p><code>custom</code><code>configMap</code></p>
            <p>Required warning after the table.</p>
        '''))
        body = module.convert_html(str(source))
        rendered = module.verify_conversion(source, body)
        self.assertIsNotNone(rendered.find(id="column"))
        self.assertEqual(len(rendered.find_all("pre")), 2)
        self.assertEqual(rendered.find("td").get_text(), "basic|cluster")

    def test_local_links_fail_closed_and_legacy_resolution_is_unique(self):
        module = self.importer
        for target in ("missing.md", "../outside.md", "chapter.md#absent"):
            with self.assertRaises(ValueError):
                module.verify_generated({"chapter.md": f"[link]({target})".encode()})
        doc = LOCK["document"]
        topics = {doc["base_url"] + "install-proc_test": "install-proc_test.md"}
        old = "https://access.redhat.com/documentation/en-us/red_hat_openshift_dev_spaces/3.29/html-single/install/index"
        self.assertEqual(module.legacy_topic(old, "proc_test_install", topics, doc), next(iter(topics)))
        self.assertIsNone(module.legacy_topic(old.replace("3.29", "3.28"), "proc_test_install", topics, doc))
        topics[doc["base_url"] + "configure-proc_test"] = "configure-proc_test.md"
        self.assertIsNone(module.legacy_topic(old, "proc_test_install", topics, doc))
