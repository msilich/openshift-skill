"""Offline coverage for the NetObserv references moved out of openshift-docs."""
import hashlib
from argparse import Namespace
import importlib.util
import json
from pathlib import Path
import shutil
import sys
from subprocess import CompletedProcess
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
TOOLS = ROOT / "tools/docs"
LOCK = json.loads((TOOLS / "build.lock.json").read_text())
SNAPSHOT = ROOT / ".agents/skills/openshift-docs/references" / ("ocp-" + LOCK["document"]["version"])


@unittest.skipUnless(importlib.util.find_spec("yaml"), "requires pinned PyYAML")
class OfflineReferenceTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        sys.path.insert(0, str(TOOLS))
        import netobserv
        cls.module = netobserv
        cls.expected = LOCK["offline_references"]["netobserv_manifest_sha256"]
        cls.manifest = netobserv.load_sources(cls.expected)

    def fixture(self, path):
        path.mkdir()
        for name in ("index.md", "AGENTS.md"):
            (path / name).write_text("# Fixture\n")
        catalog = path / self.module.CATALOG
        catalog.parent.mkdir(parents=True)
        catalog.write_text("\n".join(f"[Reference]({url})" for url in self.manifest["documents"]))

    def test_all_nine_references_are_local_versioned_and_checksummed(self):
        import build
        build.verify_converter(LOCK)
        self.assertEqual(len(self.manifest["documents"]), 9)
        bundle = SNAPSHOT / self.module.PREFIX
        report = json.loads((bundle / "SOURCE.json").read_text())
        self.assertEqual(report["manifest_sha256"], self.expected)
        self.assertEqual(report["sources"], self.manifest["sources"])
        for source in report["sources"].values():
            self.assertRegex(source["commit"], r"^[0-9a-f]{40}$")
            self.assertEqual(source["license"], "Apache-2.0")
        actual = {p.relative_to(bundle).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
                  for p in bundle.rglob("*") if p.is_file() and p.name != "SOURCE.json"}
        self.assertEqual(actual, report["files"])
        catalog = SNAPSHOT / self.module.CATALOG
        text = catalog.read_text()
        for url, document in self.manifest["documents"].items():
            self.assertNotIn(url, text)
            relative = self.module.os.path.relpath(bundle / document["output"], catalog.parent).replace(self.module.os.sep, "/")
            self.assertIn(f"]({relative})", text)
            self.assertIn(document["output"], (SNAPSHOT / "AGENTS.md").read_text())
        for version in ("1.12", "2.0", "cli"):
            self.assertIn("Apache License", (bundle / version / "LICENSE").read_text())
        self.assertEqual(json.loads((SNAPSHOT / "SOURCE.json").read_text())["offline_references"], LOCK["offline_references"])
        self.assertEqual(build.markdown_manifest(SNAPSHOT), (LOCK["expected_output"]["markdown_files"], LOCK["expected_output"]["markdown_manifest_sha256"]))
        self.assertGreater(build.verify_local_links(SNAPSHOT), 10000)

    @unittest.skipUnless(shutil.which("pandoc"), "requires pinned Pandoc")
    def test_installed_tables_and_code_match_conversion_report(self):
        from acs import pandoc, signature
        from html.parser import HTMLParser
        from urllib.parse import unquote
        class Links(HTMLParser):
            def __init__(self):
                super().__init__()
                self.ids, self.fragments = set(), []
            def handle_starttag(self, tag, attrs):
                attrs = dict(attrs)
                if "id" in attrs:
                    self.ids.add(attrs["id"])
                href = attrs.get("href", "")
                if href.startswith("#"):
                    self.fragments.append(unquote(href[1:]))
        bundle = SNAPSHOT / self.module.PREFIX
        report = json.loads((bundle / "SOURCE.json").read_text())
        for name, recorded in report["conversion"].items():
            html = pandoc((bundle / name).read_text(), "gfm", "html")
            codes, tables = signature(json.loads(pandoc(html, "html", "json")))
            self.assertEqual(hashlib.sha256(json.dumps(codes).encode()).hexdigest(), recorded["code_sha256"], name)
            self.assertEqual(hashlib.sha256(json.dumps(tables).encode()).hexdigest(), recorded["table_text_sha256"], name)
            links = Links()
            links.feed(html)
            self.assertTrue(all(fragment in links.ids for fragment in links.fragments), (name, set(links.fragments) - links.ids))
        self.assertEqual(len(report["conversion"]["cli/netobserv_cli.md"]["source_adjustments"]), 1)

    @unittest.skipUnless(shutil.which("asciidoctor") and shutil.which("pandoc"), "requires pinned conversion tools")
    def test_rebuild_is_offline_repeatable_and_matches_installed_bundle(self):
        import update
        with tempfile.TemporaryDirectory() as temp:
            roots = [Path(temp) / name for name in ("first", "second")]
            for root in roots:
                self.fixture(root)
                # Any accidental downloader introduced here must fail the test.
                with patch("urllib.request.urlopen", side_effect=AssertionError("network forbidden")):
                    self.assertEqual(self.module.finish_snapshot(root, self.expected), 9)
            update.require_identical(*roots)
            update.require_identical(roots[0] / self.module.PREFIX, SNAPSHOT / self.module.PREFIX)

    def test_unknown_reference_or_missing_catalog_stops_the_build(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp) / "snapshot"
            self.fixture(root)
            catalog = root / self.module.CATALOG
            catalog.write_text(catalog.read_text() + "\n[New](https://github.com/openshift/network-observability-operator/blob/release-2.1/docs/new.adoc)\n")
            with self.assertRaisesRegex(RuntimeError, "unbundled"):
                self.module.finish_snapshot(root, self.expected)
            self.assertFalse((root / self.module.PREFIX).exists())
            catalog.unlink()
            with self.assertRaisesRegex(RuntimeError, "catalog missing"):
                self.module.finish_snapshot(root, self.expected)

    def test_tampered_manifest_source_and_escaping_paths_are_rejected(self):
        with self.assertRaisesRegex(RuntimeError, "manifest checksum"):
            self.module.load_sources("0" * 64)
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp) / "sources"
            shutil.copytree(self.module.SOURCES, root)
            name = next(iter(self.manifest["files"]))
            (root / name).write_text("tampered")
            with patch.object(self.module, "SOURCES", root):
                with self.assertRaisesRegex(RuntimeError, "reference checksum"):
                    self.module.load_sources(self.expected)
            for name in ("../outside.md", "/etc/passwd"):
                with self.assertRaisesRegex(RuntimeError, "escaping"):
                    self.module.safe_path(root, name)

    def test_ocp_builder_keeps_supplement_and_counts_it_during_refresh(self):
        import build
        from test_docs_updates import updater
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            source = root / "source"
            source.mkdir()
            (source / "LICENSE").write_text("source license")
            lockfile = root / "lock.json"
            lockfile.write_text(json.dumps(LOCK))
            output = root / "output"
            args = Namespace(lock=lockfile, source_dir=source, output_dir=output, workers=1, refresh_lock=True)
            def convert(command, **kwargs):
                target = Path(command[command.index("--output-dir") + 1])
                self.fixture(target)
                (target / "index.md").write_text("> Designed for AI agent consumption. Updated weekly.\n")
                return CompletedProcess(command, 0, "Conversion complete: 1 succeeded, 0 failed\n")
            def supplement(target, expected):
                self.assertEqual(expected, self.expected)
                (target / "supplement.md").write_text("offline content\n")
                return 1
            with patch.object(build, "parse_args", return_value=args), \
                 patch.object(build, "verify_source", return_value="2026-10-26T00:00:00Z"), \
                 patch.object(build, "verify_tool_versions", return_value={}), \
                 patch.object(build, "parse_distro_map", return_value={}), \
                 patch.object(build, "get_distro_attributes", return_value={"product-version": LOCK["document"]["version"], "product-title": LOCK["document"]["product"]}), \
                 patch.object(build, "source_topic_count", return_value=1), \
                 patch.object(build, "run", side_effect=convert), \
                 patch.object(self.module, "finish_snapshot", side_effect=supplement) as finish:
                self.assertEqual(build.main(), 0)
            finish.assert_called_once()
            self.assertTrue((output / "supplement.md").is_file())
            self.assertEqual(updater.read_json(lockfile)["expected_output"]["markdown_files"], 4)


if __name__ == "__main__":
    unittest.main()
