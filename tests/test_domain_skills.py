"""Static contracts and synthetic transports; NOT an OpenCode/Qwen evaluation."""
from __future__ import annotations

import fnmatch
import importlib.util
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

from fake_cluster import mcp_response, oc_response, tools_for
from test_bundle import EXAMPLES, ROOT, SKILLS_ROOT, SKILL_NAMES, load_jsonc

CASES = json.loads((ROOT / "tests/fixtures/domain_scenarios.json").read_text())
DOMAINS = SKILL_NAMES[3:]


def permission(rules: dict, command: str) -> str:
    result = "deny"
    for pattern, value in rules.items():
        if fnmatch.fnmatchcase(command, pattern):
            result = value
    return result


class DomainBundleTest(unittest.TestCase):
    def test_relocated_links_and_search_from_unrelated_directory(self):
        with tempfile.TemporaryDirectory() as temp:
            installed = Path(temp) / "custom-install" / "skills"
            shutil.copytree(SKILLS_ROOT, installed)
            unrelated = Path(temp) / "unrelated"
            unrelated.mkdir()
            for name in SKILL_NAMES:
                for path in (installed / name).rglob("*.md"):
                    if any(part in str(path) for part in ("/references/ocp-", "/references/gitops-1.21/", "/references/devspaces-3.29/")):
                        continue  # Generated snapshots have their own manifest/link test.
                    for target in re.findall(r"\[[^]]*\]\(([^)]+)\)", path.read_text()):
                        local = target.split("#")[0]
                        if not local or "://" in local:
                            continue
                        resolved = (path.parent / local).resolve()
                        self.assertTrue(resolved.is_relative_to(installed.resolve()), (path, target))
                        self.assertTrue(resolved.exists(), (path, target))
            script = installed / "openshift-docs/scripts/search_docs.py"
            for product, query in (("ocp", "ingress"), ("gitops", "ApplicationSet"), ("devspaces", "CheCluster")):
                result = subprocess.run([sys.executable, str(script), query, "--product", product,
                                         "--max-results", "2"], cwd=unrelated, capture_output=True, text=True)
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertRegex(result.stdout, r"\.md:\d+:")
            shutil.rmtree(installed / "openshift-docs/references/gitops-1.21")
            result = subprocess.run([sys.executable, str(script), "test", "--product", "gitops"],
                                    cwd=unrelated, capture_output=True, text=True)
            self.assertEqual(result.returncode, 2)
            self.assertIn("directory not found", result.stderr)

    def test_source_maps_pin_revision_and_product(self):
        lock = json.loads((ROOT / "sources.lock.json").read_text())
        self.assertEqual(lock["sources"]["openshift_gitops_docs"]["commit"], "ca5db8539a097b38e2975980963e0959782d105f")
        self.assertEqual(lock["sources"]["agentic_skills_workflows"]["commit"], "7aca4bee317cd70a4204795db6b1d7b9eb78f48c")
        for name in DOMAINS:
            text = (SKILLS_ROOT / name / "references/sources.md").read_text()
            if name == "openshift-devspaces":
                self.assertIn(lock["sources"]["devspaces_docs"]["archive_sha256"], text)
            else:
                source = "openshift_gitops_docs" if name == "openshift-gitops" else "openshift_docs"
                self.assertIn(lock["sources"][source]["commit"], text)
            self.assertIn("project-authored", text)
            self.assertIn("SOURCE.json", text)

    def test_all_profiles_allow_nine_skills_without_new_readonly_writes(self):
        for filename in ("opencode.readonly.jsonc", "opencode.readonly-with-argocd.jsonc", "opencode.day2.jsonc"):
            config = load_jsonc(EXAMPLES / filename)
            for name in SKILL_NAMES:
                self.assertEqual(config["permission"]["skill"][name], "allow")
            readonly = "readonly" in filename
            kubeconfig = "{env:OPENSHIFT_MCP_READ_KUBECONFIG}" if readonly else "{env:OPENSHIFT_MCP_DAY2_KUBECONFIG}"
            rules = config["permission"]["bash"]
            for command in ("apply -f manifest.yaml", "patch pdb api -n shop --type merge -p '{}'", "adm drain worker-1", "delete backup shop -n openshift-adp", "adm upgrade --to=4.22.1"):
                self.assertEqual(permission(rules, f"oc --kubeconfig {kubeconfig} {command}"), "deny" if readonly else "ask")
            self.assertEqual(permission(rules, "oc-mirror --v2 --config images.yaml file:///transfer"), "deny" if readonly else "ask")
            self.assertEqual(permission(rules, f"oc --kubeconfig {kubeconfig} whoami -t"), "deny")
        # This approximates pattern matching only; the real OpenCode evaluator is a separate test.

    def test_fixture_coverage_and_bilingual_triggers(self):
        expected = {"missing-tool", "denied-access", "version-mismatch", "unknown-schema", "missing-source",
                    "secret-choice", "image-pull", "service-endpoints", "blocking-pdb", "controller-drift",
                    "incomplete-backup", "day2-approval", "devspaces-pending-pvc", "devspaces-registry",
                    "devspaces-controller", "devspaces-version", "devspaces-secret", "devspaces-missing-tool",
                    "devspaces-denied", "devspaces-schema", "devspaces-source"}
        self.assertEqual({case["id"] for case in CASES}, expected)
        self.assertEqual({case["skill"] for case in CASES}, set(DOMAINS))
        for case in CASES:
            self.assertEqual(set(case["prompts"]), {"en", "de"})
            self.assertTrue(case["expect"])
            self.assertTrue(case["forbid"])
        triggers = json.loads((ROOT / "tests/fixtures/skill_trigger_cases.json").read_text())
        for name in DOMAINS:
            self.assertGreaterEqual(sum(case["expected_skill"] == name for case in triggers), 2)

    def test_fake_mcp_observations_and_errors(self):
        for case in CASES:
            listed = mcp_response(case, {"id": 1, "method": "tools/list"})["result"]["tools"]
            self.assertEqual(listed, tools_for(case))
            for row in case.get("reads", []):
                args = {key: row[key] for key in ("kind", "name", "namespace") if key in row}
                response = mcp_response(case, {"id": 2, "method": "tools/call", "params": {"name": "resources_get", "arguments": args}})
                self.assertEqual(response["result"]["isError"], "error" in row)
            response = mcp_response(case, {"id": 3, "method": "tools/call", "params": {"name": "resources_delete", "arguments": {}}})
            self.assertEqual(response["error"]["code"], -32602)

    def test_fake_oc_exact_requests_and_fail_closed(self):
        for case in CASES:
            for row in case.get("oc", []):
                code, result = oc_response(case, ["--kubeconfig", "/fixture/readonly.kubeconfig", *row["args"]])
                self.assertEqual(code, int("error" in row))
                self.assertTrue(result)
            for args in (["get", "secrets"], ["--kubeconfig", "/fixture/readonly.kubeconfig", "delete", "pods", "--all"]):
                self.assertEqual(oc_response(case, args)[0], 2)

    def test_fake_stdio_protocol_and_trace(self):
        with tempfile.TemporaryDirectory() as temp:
            trace = Path(temp) / "trace.jsonl"
            env = {**os.environ, "DOMAIN_TRACE": str(trace)}
            requests = [{"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {"protocolVersion": "2024-11-05"}},
                        {"jsonrpc": "2.0", "method": "notifications/initialized"},
                        {"jsonrpc": "2.0", "id": 2, "method": "tools/list"}]
            result = subprocess.run([sys.executable, str(ROOT / "tests/fake_cluster.py"), "--transport", "mcp", "--scenario", "missing-tool"],
                                    input="\n".join(map(json.dumps, requests)) + "\n", env=env, capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            responses = [json.loads(line) for line in result.stdout.splitlines()]
            self.assertEqual([row["id"] for row in responses], [1, 2])
            self.assertEqual(responses[1]["result"]["tools"], [])
            self.assertEqual(len(trace.read_text().splitlines()), 3)


@unittest.skipUnless(importlib.util.find_spec("yaml"), "requires build dependency PyYAML")
class BuildDefinitionTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch.object(sys, "path", [str(ROOT / "tools/docs"), *sys.path]):
            spec = importlib.util.spec_from_file_location("domain_docs_build", ROOT / "tools/docs/build.py")
            cls.build = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(cls.build)

    def test_both_manifests_and_links_match_locks(self):
        for filename in ("build.lock.json", "gitops.lock.json"):
            lock = json.loads((ROOT / "tools/docs" / filename).read_text())
            definition = self.build.document_definition(lock)
            folder = ("gitops-" if filename == "gitops.lock.json" else "ocp-") + definition["version"]
            snapshot = SKILLS_ROOT / "openshift-docs/references" / folder
            count, digest = self.build.markdown_manifest(snapshot)
            self.assertEqual(count, lock["expected_output"]["markdown_files"])
            self.assertEqual(digest, lock["expected_output"]["markdown_manifest_sha256"])
            self.assertGreater(self.build.verify_local_links(snapshot), 100)
            self.build.verify_converter(lock)
            source = json.loads((snapshot / "SOURCE.json").read_text())
            self.assertEqual(source["artifact"]["product"], definition["product"])
            self.assertEqual(source["artifact"]["version"], definition["version"])
            self.assertEqual(source["sources"], lock["sources"])

    def test_definition_requires_explicit_fields(self):
        lock = json.loads((ROOT / "tools/docs/gitops.lock.json").read_text())
        for field in ("product", "version", "distro", "branch"):
            changed = json.loads(json.dumps(lock))
            del changed["document"][field]
            with self.assertRaises(RuntimeError):
                self.build.document_definition(changed)
        lock["document"]["version"] = "latest"
        with self.assertRaises(RuntimeError):
            self.build.document_definition(lock)
        lock["document"]["version"] = "1.21"
        lock["document"]["branch"] = "main"
        with self.assertRaises(RuntimeError):
            self.build.document_definition(lock)

    def test_default_lock_and_optional_selection(self):
        for suffix, expected in (([], self.build.LOCK_PATH), (["--lock", "custom.json"], Path("custom.json"))):
            with patch.object(sys, "argv", ["build.py", "--source-dir", "source", "--output-dir", "out", *suffix]):
                self.assertEqual(self.build.parse_args().lock, expected)

    def test_escape_and_different_product_rejected(self):
        with tempfile.TemporaryDirectory() as temp:
            base = Path(temp)
            snapshot = base / "snapshot"
            snapshot.mkdir()
            (base / "outside.md").write_text("outside")
            (snapshot / "index.md").write_text("[escape](../outside.md)")
            with self.assertRaises(RuntimeError):
                self.build.verify_local_links(snapshot)
            (snapshot / "SOURCE.json").write_text(json.dumps({"artifact": {"product": "other", "version": "1.21"}}))
            with self.assertRaises(RuntimeError):
                self.build.replace_output(base / "staged", snapshot, {"product": "Red Hat OpenShift GitOps", "version": "1.21"})
            self.assertTrue((snapshot / "index.md").is_file())

    def test_gitops_version_attributes(self):
        attrs = self.build.get_distro_attributes({"openshift-gitops": {"name": "Red Hat OpenShift GitOps", "branches": {}}},
                                                 "openshift-gitops", "gitops-docs-1.21")
        self.assertEqual(attrs["product-version"], "1.21")
        with self.assertRaises(ValueError):
            self.build.get_distro_attributes({}, "openshift-gitops", "main")


if __name__ == "__main__":
    unittest.main()
