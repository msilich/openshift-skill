"""ACM offline integrity and update checks; not a model or cluster evaluation."""
import copy
import hashlib
import importlib.util
import json
from pathlib import Path
import shutil
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
TOOLS = ROOT / "tools/docs"
SNAPSHOT = ROOT / ".agents/skills/openshift-docs/references/acm-2.17"
LOCK = json.loads((TOOLS / "acm.lock.json").read_text())
sys.path.insert(0, str(TOOLS))


class AcmIntegrityTest(unittest.TestCase):
    def test_inventory_provenance_licenses_and_checksums(self):
        source = json.loads((SNAPSHOT / "SOURCE.json").read_text())
        actual = {p.relative_to(SNAPSHOT).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
                  for p in SNAPSHOT.rglob("*") if p.is_file() and p.name != "SOURCE.json"}
        self.assertEqual(actual, source["integrity"]["files"])
        self.assertEqual(source["sources"], LOCK["sources"])
        self.assertFalse(source["runtime_network_required"])
        self.assertEqual(source["artifact"]["converted_topics"], 22)
        self.assertEqual(len(source["inventory"]), 22)
        self.assertEqual({Path(path).parts[0] + ".md" for path in source["inventory"]},
                         set(json.loads((SNAPSHOT / "CONVERSION.json").read_text())["handbooks"]))
        markdown = {name: value for name, value in actual.items() if name.endswith(".md")}
        manifest = "".join(f"{value}  {name}\n" for name, value in sorted(markdown.items()))
        self.assertEqual(hashlib.sha256(manifest.encode()).hexdigest(), LOCK["expected_output"]["markdown_manifest_sha256"])
        self.assertEqual(len(markdown), LOCK["expected_output"]["markdown_files"])
        self.assertGreater(source["artifact"]["assets"], 0)
        self.assertIn("Section 4d", (SNAPSHOT / "LEGAL-NOTICE.md").read_text())
        self.assertIn("Attribution-ShareAlike 3.0", (SNAPSHOT / "LICENSE.md").read_text())
        self.assertIn("Apache License", (SNAPSHOT / "LICENSE.api-documentation").read_text())
        for row in LOCK["legal_notices"]:
            self.assertEqual(hashlib.sha256((TOOLS / row["path"]).read_bytes()).hexdigest(), row["sha256"])
        for name, digest in LOCK["local_build_helpers"].items():
            self.assertEqual(hashlib.sha256((TOOLS / name).read_bytes()).hexdigest(), digest)

    def test_source_gaps_are_visible_and_release_pins_consistent(self):
        source = json.loads((SNAPSHOT / "SOURCE.json").read_text())
        self.assertEqual(source["source_issues"][0]["kind"], "missing-generated-api-reference")
        self.assertIn("No core API field reference", (SNAPSHOT / "api-reference.md").read_text())
        pins = json.loads((ROOT / "sources.lock.json").read_text())["sources"]["acm_docs"]
        self.assertEqual(pins["commit"], LOCK["sources"]["rhacm_docs"]["commit"])
        self.assertEqual(pins["api_commit"], LOCK["sources"]["api_docs"]["commit"])
        for name in ("README.md", "THIRD_PARTY_NOTICES.md"):
            text = (ROOT / name).read_text()
            self.assertIn(pins["commit"], text)
            self.assertIn(pins["api_commit"], text)
        self.assertEqual(LOCK["sources"]["rhacm_docs"]["branch"], "2.17_prod")
        self.assertEqual(LOCK["sources"]["api_docs"]["branch"], "release-2.17")


@unittest.skipUnless(importlib.util.find_spec("yaml") and importlib.util.find_spec("bs4") and shutil.which("pandoc"),
                     "requires pinned documentation build dependencies")
class AcmConversionTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        import import_acm
        cls.importer = import_acm

    def test_local_links_images_and_final_code_table_signatures(self):
        module = self.importer
        generated = {p.relative_to(SNAPSHOT).as_posix(): p.read_bytes() for p in SNAPSHOT.rglob("*") if p.is_file()}
        self.assertGreater(module.verify_generated(generated), 100)
        quality = json.loads((SNAPSHOT / "CONVERSION.json").read_text())
        for name, row in quality["handbooks"].items():
            with self.subTest(handbook=name):
                text = (SNAPSHOT / name).read_text()
                self.assertIn("Copyright Red Hat", text)
                tree = json.loads(module.pandoc(module.pandoc(text, "gfm", "html"), "html", "json"))
                codes, tables = module.signature(tree)
                self.assertEqual(hashlib.sha256(json.dumps(codes).encode()).hexdigest(), row["code_sha256"])
                self.assertEqual(hashlib.sha256(json.dumps(tables).encode()).hexdigest(), row["table_text_sha256"])
        for path, digest in quality["image_sha256"].items():
            self.assertEqual(hashlib.sha256(generated[path]).hexdigest(), digest)

    def test_adjacent_code_blocks_keep_their_boundaries(self):
        module = self.importer
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            xml, md = root / "test.xml", root / "test.md"
            xml.write_text('<article xmlns="http://docbook.org/ns/docbook"><title>Test</title>'
                           '<screen>oc get managedclusters</screen><screen>oc get managedclustersets</screen></article>')
            module.render_topic(xml, md, "", root)
            quality = json.loads(md.with_suffix(".quality.json").read_text())
            self.assertEqual(quality["code_blocks"], 2)
            self.assertIn("Separate adjacent source examples", md.read_text())

    def test_unversioned_source_and_network_include_are_rejected(self):
        for name, field, value in (("rhacm_docs", "branch", "main"),
                                   ("api_docs", "url", "https://example.invalid/docs"),
                                   ("api_docs", "commit", "latest")):
            changed = copy.deepcopy(LOCK)
            changed["sources"][name][field] = value
            with self.assertRaises(ValueError):
                self.importer.definition(changed)
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            with self.assertRaisesRegex(ValueError, "empty"):
                self.importer.inventory(root)
            book = root / "guide"
            book.mkdir()
            (book / "master.adoc").write_text("include::https://example.invalid/part.adoc[]")
            with self.assertRaisesRegex(ValueError, "Network include"):
                self.importer.inventory(root)
            (book / "master.adoc").write_text("= Guide\n")
            (book / "outside").symlink_to(root.parent)
            with self.assertRaisesRegex(ValueError, "symlink escapes"):
                self.importer.inventory(root)

    def test_missing_include_is_not_published(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            book = root / "guide"
            book.mkdir()
            master = book / "master.adoc"
            master.write_text("= Guide\n\ninclude::missing.adoc[]\n")
            output = root / "output"
            output.mkdir()
            from subprocess import CompletedProcess
            with patch.object(self.importer.subprocess, "run", return_value=CompletedProcess([], 0, "", "asciidoctor: ERROR: include file not found")):
                with self.assertRaisesRegex(ValueError, "include file not found"):
                    self.importer.render_book(master, output, root)
            self.assertFalse(list(output.iterdir()))

    def test_missing_images_fail_and_missing_fragments_are_recorded(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / "guide").mkdir()
            md = root / "guide.md"
            quality = {"guide.md": {"anchors": ["existing"]}}
            md.write_text("![Missing](../images/missing.png)")
            with self.assertRaisesRegex(ValueError, "Missing or escaping"):
                self.importer.rewrite_references(root, root, LOCK, quality)
            md.write_text("[Section](#absent)")
            assets, issues, external = self.importer.rewrite_references(root, root, LOCK, quality)
            self.assertFalse(assets)
            self.assertEqual(len(issues), 1)
            self.assertIn("[Section](guide.md)", md.read_text())

    def test_output_guard_preserves_sources_and_user_home(self):
        for output in (Path.home(), ROOT, ROOT / "source/child"):
            with patch.object(sys, "argv", ["import_acm.py", "--source-dir", str(ROOT / "source"),
                    "--api-source-dir", str(ROOT / "api"), "--output-dir", str(output)]), \
                    patch.object(self.importer, "build") as build:
                with self.assertRaisesRegex(ValueError, "Unsafe"):
                    self.importer.main()
                build.assert_not_called()

    def test_new_api_reference_or_corrupt_legal_input_stops_before_output(self):
        module = self.importer
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            source, api = root / "source", root / "api"
            (source / "modules").mkdir(parents=True)
            (source / "modules/common-attributes.adoc").write_text(":product-version: 2.17\n")
            (source / "guide").mkdir()
            (source / "guide/master.adoc").write_text("= Guide\n")
            (api / "api-docs").mkdir(parents=True)
            reference = api / "api-docs/README.adoc"
            reference.write_text("= Newly published API reference\n")
            output = root / "output"
            with patch.object(module.common, "verify_tool_versions"), \
                 patch.object(module.common, "verify_converter"), \
                 patch.object(module, "check_dependencies"), \
                 patch.object(module, "verify_checkout", return_value="pinned-time"):
                with self.assertRaisesRegex(ValueError, "now available"):
                    module.build(LOCK, source, api, output)
                reference.unlink()
                changed = copy.deepcopy(LOCK)
                changed["legal_notices"][0]["sha256"] = "0" * 64
                with self.assertRaisesRegex(ValueError, "Legal source checksum"):
                    module.build(changed, source, api, output)
            self.assertFalse(output.exists())

    def test_acm_updates_pin_both_sources_and_build_twice(self):
        import update
        builds, fetched = [], []
        def run(*command):
            if command[1] == "ls-remote":
                return ("a" if "rhacm-docs" in command[3] else "b") * 40 + "\tref\n"
            if command[0] == sys.executable:
                builds.append(command)
                candidate = update.read_json(Path(command[command.index("--lock") + 1]))
                self.assertEqual(candidate["sources"]["rhacm_docs"]["commit"], "a" * 40)
                self.assertEqual(candidate["sources"]["api_docs"]["commit"], "b" * 40)
                self.assertEqual(candidate["document"], LOCK["document"])
                target = Path(command[command.index("--output-dir") + 1])
                target.mkdir()
                (target / "chapter.md").write_text("deterministic")
            elif "fetch" in command:
                fetched.append(command[-1])
            return ""
        with tempfile.TemporaryDirectory() as temp, patch.object(update, "run", side_effect=run):
            update.prepare_acm(LOCK, Path(temp))
        self.assertEqual(fetched, ["a" * 40, "b" * 40])
        self.assertEqual(len(builds), 2)
        self.assertIn("--refresh-lock", builds[0])
        self.assertNotIn("--refresh-lock", builds[1])

    def test_acm_noop_checks_both_release_heads_without_building(self):
        import update
        values = [LOCK["sources"][name]["commit"] + "\tref\n" for name in ("rhacm_docs", "api_docs")]
        with patch.object(update, "run", side_effect=values) as run:
            self.assertIsNone(update.prepare_acm(LOCK, Path("unused")))
            self.assertEqual(run.call_count, 2)


if __name__ == "__main__":
    unittest.main()
