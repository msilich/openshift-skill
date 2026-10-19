"""Exercise update failures and provenance without downloading vendor sources."""
import copy
import importlib.util
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch
from argparse import Namespace
from subprocess import CompletedProcess

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools/docs"))
import update as updater


class DocumentationUpdateTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.tools = self.root / "tools/docs"
        self.tools.mkdir(parents=True)
        self.snapshots = self.root / ".agents/skills/openshift-docs/references"
        self.snapshots.mkdir(parents=True)
        for product, (filename, _) in updater.PRODUCTS.items():
            lock = updater.read_json(ROOT / "tools/docs" / filename)
            updater.write_json(self.tools / filename, lock)
            snapshot = self.snapshots / f"{product}-{lock['document']['version']}"
            snapshot.mkdir()
            (snapshot / "SOURCE.json").write_text('{"old": true}\n')
        sources = updater.read_json(ROOT / "sources.lock.json")
        updater.write_json(self.root / "sources.lock.json", sources)
        self.old = sources["sources"]["openshift_docs"]["commit"]
        self.new = "a" * 40
        (self.root / "README.md").write_text(self.old + "\n")
        (self.root / "THIRD_PARTY_NOTICES.md").write_text(self.old + "\n")
        source_map = self.root / ".agents/skills/openshift-upgrade/references/sources.md"
        source_map.parent.mkdir(parents=True)
        source_map.write_text(self.old + "\n")
        for key, value in (("ROOT", self.root), ("TOOLS", self.tools), ("SNAPSHOTS", self.snapshots)):
            p = patch.object(updater, key, value)
            p.start()
            self.addCleanup(p.stop)

    def candidate(self, product, lock, work):
        candidate = copy.deepcopy(lock)
        candidate["sources"]["openshift_docs"]["commit"] = self.new
        output = work / "first"
        output.mkdir()
        updater.write_json(output / "SOURCE.json", {"artifact": {"converted_topics": 3}})
        (output / "chapter.md").write_text("new content\n")
        return candidate, output, None

    def test_noop_changes_no_checkout_files(self):
        before = updater.file_hashes(self.root)
        with patch.object(updater, "prepare_git", return_value=None):
            updater.update(["ocp"], None)
        self.assertEqual(updater.file_hashes(self.root), before)

    def test_cli_refuses_to_overwrite_a_dirty_checkout(self):
        with patch.object(sys, "argv", ["update.py"]), \
             patch.object(updater, "run", return_value=" M local-document.md\n"), \
             patch.object(updater, "update") as update:
            with self.assertRaisesRegex(RuntimeError, "clean checkout"):
                updater.main()
            update.assert_not_called()

    def test_one_failed_product_leaves_all_sources_and_snapshots_untouched(self):
        before = updater.file_hashes(self.root)
        def prepare(product, lock, work):
            if product == "gitops":
                raise RuntimeError("upstream conversion failed")
            return self.candidate(product, lock, work)
        with patch.object(updater, "prepare_git", side_effect=prepare):
            with self.assertRaisesRegex(RuntimeError, "conversion failed"):
                updater.update(["ocp", "gitops"], None)
        self.assertEqual(updater.file_hashes(self.root), before)

    def test_success_updates_snapshot_locks_and_source_maps_together(self):
        before = updater.read_json(self.root / "sources.lock.json")
        report = self.root / "report.md"
        with patch.object(updater, "prepare_git", side_effect=self.candidate):
            updater.update(["ocp"], report)
        after = updater.read_json(self.root / "sources.lock.json")
        self.assertEqual(after["sources"]["openshift_docs"]["commit"], self.new)
        for key in before["sources"]:
            if key != "openshift_docs":
                self.assertEqual(before["sources"][key], after["sources"][key])
        self.assertEqual(after["documentation_version"], before["documentation_version"])
        self.assertEqual((self.root / "README.md").read_text().strip(), self.new)
        source_map = self.root / ".agents/skills/openshift-upgrade/references/sources.md"
        self.assertEqual(source_map.read_text().strip(), self.new)
        self.assertIn(self.new, report.read_text())
        snapshot = self.snapshots / f"ocp-{after['documentation_version']}"
        self.assertEqual((snapshot / "chapter.md").read_text(), "new content\n")
        self.assertNotIn('"old"', (snapshot / "SOURCE.json").read_text())

    def test_repeated_build_checks_include_assets_and_provenance(self):
        first, second = self.root / "first", self.root / "second"
        first.mkdir()
        second.mkdir()
        for name in ("chapter.md", "SOURCE.json", "illustration.png"):
            (first / name).write_bytes(b"same")
            (second / name).write_bytes(b"same")
        updater.require_identical(first, second)
        for name in ("SOURCE.json", "illustration.png"):
            (second / name).write_bytes(b"different")
            with self.assertRaisesRegex(RuntimeError, "builds differ"):
                updater.require_identical(first, second)
            (second / name).write_bytes(b"same")

    def test_git_noop_does_not_build_and_invalid_sources_are_rejected(self):
        lock = updater.read_json(self.tools / "build.lock.json")
        with patch.object(updater, "run", return_value=self.old + "\trefs/heads/enterprise-4.20\n") as run:
            self.assertIsNone(updater.prepare_git("ocp", lock, self.root))
            self.assertEqual(run.call_count, 1)
        for field, value in (("url", "https://example.invalid/repo"), ("branch_hint", "main")):
            changed = copy.deepcopy(lock)
            changed["sources"]["openshift_docs"][field] = value
            with patch.object(updater, "run") as run:
                with self.assertRaises(ValueError):
                    updater.prepare_git("ocp", changed, self.root)
                run.assert_not_called()

    def test_git_candidate_gets_strict_second_build(self):
        lock = updater.read_json(self.tools / "build.lock.json")
        builds = []
        def run(*command):
            if command[1] == "ls-remote":
                return self.new + "\trefs/heads/enterprise-4.20\n"
            if command[0] == sys.executable:
                builds.append(command)
                output = Path(command[command.index("--output-dir") + 1])
                output.mkdir()
                (output / "chapter.md").write_text("same content")
                candidate_path = Path(command[command.index("--lock") + 1])
                candidate = updater.read_json(candidate_path)
                self.assertEqual(candidate["document"], lock["document"])
                self.assertEqual(candidate["sources"]["openshift_docs"]["commit"], self.new)
            return ""
        with patch.object(updater, "run", side_effect=run):
            updater.prepare_git("ocp", lock, self.root)
        self.assertEqual(len(builds), 2)
        self.assertIn("--refresh-lock", builds[0])
        self.assertNotIn("--refresh-lock", builds[1])

    @unittest.skipUnless(importlib.util.find_spec("bs4"), "requires importer dependency")
    def test_devspaces_timestamp_only_refresh_preserves_old_archive(self):
        import import_devspaces as importer
        lock = updater.read_json(self.tools / "devspaces.lock.json")
        def fetch(lock, cache, archive):
            archive.write_bytes(b"same documents, new retrieval metadata")
        def build(candidate, archive, output):
            output.mkdir()
            updater.write_json(output / "SOURCE.json", {
                "artifact": {"converted_topics": lock["expected_output"]["topics"]},
                "integrity": {"content_manifest_sha256": lock["expected_output"]["content_manifest_sha256"]},
            })
        with patch.object(importer, "fetch", side_effect=fetch), patch.object(importer, "build", side_effect=build):
            self.assertIsNone(updater.prepare_devspaces(lock, self.root))


@unittest.skipUnless(importlib.util.find_spec("yaml"), "requires build dependency")
class BuildInventoryTest(unittest.TestCase):
    def test_source_inventory_is_filtered_by_product_and_must_be_nonempty(self):
        import build
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / "_topic_maps").mkdir()
            (root / "_topic_maps/_topic_map.yml").write_text(
                "Name: Included\nDir: guide\nDistros: openshift-gitops\nTopics:\n"
                "- Name: First\n  File: first\n- Name: Nested\n  Dir: nested\n  Topics:\n"
                "  - Name: Second\n    File: second\n"
                "---\nName: Other\nDir: other\nDistros: openshift-acs\nTopics:\n- File: third\n")
            self.assertEqual(build.source_topic_count(root, "openshift-gitops"), 2)
            with self.assertRaisesRegex(RuntimeError, "empty"):
                build.source_topic_count(root, "openshift-enterprise")

    def test_refresh_does_not_pin_a_partial_conversion(self):
        import build
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            lock_path = root / "candidate.json"
            original = (ROOT / "tools/docs/build.lock.json").read_bytes()
            lock_path.write_bytes(original)
            lock = json.loads(original)
            doc = lock["document"]
            args = Namespace(lock=lock_path, source_dir=root / "source", output_dir=root / "output",
                             workers=1, refresh_lock=True)
            with patch.object(build, "parse_args", return_value=args), \
                 patch.object(build, "verify_source", return_value="2026-01-01T00:00:00+00:00"), \
                 patch.object(build, "verify_converter"), patch.object(build, "verify_tool_versions", return_value={}), \
                 patch.object(build, "parse_distro_map", return_value={}), \
                 patch.object(build, "get_distro_attributes", return_value={"product-version": doc["version"], "product-title": doc["product"]}), \
                 patch.object(build, "source_topic_count", return_value=2), \
                 patch.object(build, "run", return_value=CompletedProcess([], 0, "Conversion complete: 1 succeeded, 0 failed\n")):
                with self.assertRaisesRegex(RuntimeError, "unexpected conversion result"):
                    build.main()
            self.assertEqual(lock_path.read_bytes(), original)
            self.assertFalse(args.output_dir.exists())


if __name__ == "__main__":
    unittest.main()
