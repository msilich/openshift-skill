"""ACS integrity, permission patterns and synthetic transports, NOT Qwen behavior."""
from __future__ import annotations

import copy
import hashlib
import importlib.util
import json
from pathlib import Path
import re
import shutil
import subprocess
import sys
import unittest

from fake_acs import FakeACS, HOST, CLUSTER_ID, TOOLS
from test_bundle import ROOT, SKILLS_ROOT, SKILL_NAMES, load_jsonc
from test_domain_skills import permission

ACS = SKILLS_ROOT / "openshift-acs"
DOCS = SKILLS_ROOT / "openshift-docs/references/acs-4.11"


class ACSContracts(unittest.TestCase):
    def test_exact_mcp_inventory_and_read_only_in_both_profiles(self):
        for mode in ("readonly", "day2"):
            config = load_jsonc(ACS / f"assets/opencode.acs-{mode}.jsonc")
            rules = config["permission"]
            self.assertEqual({n for n in SKILL_NAMES if rules["skill"].get(n) == "allow"}, set(SKILL_NAMES))
            self.assertEqual({k for k, v in rules.items() if k.startswith("acs_read_") and v == "allow"}, {"acs_read_" + n for n in TOOLS})
            self.assertEqual(permission(rules, "acs_read_delete_policy"), "deny")
            mcp = config["mcp"]["acs_read"]
            self.assertEqual(mcp["command"], ["{env:ACS_MCP_BINARY}"])
            env = mcp["environment"]
            for key, value in {"SERVER__TYPE": "stdio", "CENTRAL__AUTH_TYPE": "static",
                               "GLOBAL__READ_ONLY_TOOLS": "true", "CENTRAL__INSECURE_SKIP_TLS_VERIFY": "false",
                               "CENTRAL__MAX_RETRIES": "0"}.items():
                self.assertEqual(env["STACKROX_MCP__" + key], value)
            self.assertEqual(env["STACKROX_MCP__CENTRAL__API_TOKEN"], "{env:ACS_READ_TOKEN}")

    def test_narrow_http_and_cli_patterns(self):
        read = load_jsonc(ACS / "assets/opencode.acs-readonly.jsonc")["permission"]["bash"]
        day = load_jsonc(ACS / "assets/opencode.acs-day2.jsonc")["permission"]["bash"]
        writes = [k for k in day if "--request PUT" in k or "--request POST" in k]
        self.assertEqual(len(writes), 2)
        for command in writes:
            self.assertEqual(permission(day, command), "ask")
            self.assertEqual(permission(read, command), "deny")
        for rules in (read, day):
            self.assertNotIn("curl *", rules)
            self.assertNotIn("roxctl *", rules)
            for command in [k for k in rules if k.startswith("curl ")]:
                self.assertIn("--proto =https", command)
                self.assertIn("--max-redirs 0", command)
                self.assertIn("--cacert {env:ACS_CA_FILE}", command)
                self.assertIn("--url https://{env:ACS_CENTRAL_HOST}/v1/policies", command)
                for unsafe in (command + " -L", command + " --insecure",
                               command.replace("{env:ACS_CENTRAL_HOST}", "evil.example.invalid"),
                               command.replace("--request GET", "--request DELETE")):
                    if unsafe != command:
                        self.assertEqual(permission(rules, unsafe), "deny")
            self.assertEqual(permission(rules, "roxctl image scan --image private:latest"), "deny")

    def test_scenario_corpus_is_bilingual_and_not_a_model_claim(self):
        scenarios = json.loads((ROOT / "tests/fixtures/acs_scenarios.json").read_text())
        self.assertEqual({s["id"] for s in scenarios}, {"missing-tool", "forbidden", "mapping", "version", "schema", "stale-feed", "missing-source", "secret", "central-write", "uncertain-write", "controller"})
        for case in scenarios:
            self.assertEqual(set(case["prompts"]), {"en", "de"})
            self.assertTrue(case["expect"])
            self.assertTrue(case["forbid"])
        text = (ACS / "references/execution.md").read_text()
        for marker in ("once", "Forbidden", "four choices", "model context", "Read-only", "unknown"):
            self.assertIn(marker.lower(), text.lower())

    def test_missing_source_is_reported_by_offline_search(self):
        # Existing relocation tests exercise the installed ACS tree. Point this
        # isolated module at an absent source without altering the shipped snapshot.
        spec = importlib.util.spec_from_file_location("acs_search", SKILLS_ROOT / "openshift-docs/scripts/search_docs.py")
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        from unittest.mock import patch
        with patch.object(module, "ACS_ROOT", DOCS / "absent-source"), patch.object(sys, "argv", ["search", "restore", "--product", "acs"]):
            self.assertEqual(module.main(), 2)


class SyntheticACS(unittest.TestCase):
    def test_missing_tool_forbidden_mapping_and_stale_observation(self):
        lab = FakeACS()
        self.assertEqual(lab.mcp({"method": "tools/list"}, missing=True)["tools"], [])
        request = {"method": "tools/call", "params": {"name": "get_nodes_for_cve", "arguments": {"filterClusterId": CLUSTER_ID, "cveName": "CVE-2021-44228"}}}
        observation = lab.mcp(request)
        self.assertLess(observation["feedTime"], observation["scanTime"])
        wrong = copy.deepcopy(request)
        wrong["params"]["arguments"]["filterClusterId"] = "same-name-other-Central"
        self.assertEqual(lab.mcp(wrong)["error"], "target mismatch")
        self.assertEqual(lab.central("other.example.invalid:443", "GET", "/v1/policies/policy-fixture-01")[0], 421)
        denied = FakeACS(forbidden=True)
        self.assertEqual(denied.mcp(request)["error"], "Forbidden")
        self.assertEqual(len(denied.trace), 1)  # No automatic CLI fallback in this test driver.

    def test_full_synthetic_central_write_preview_denial_approval_verification(self):
        lab = FakeACS(readonly=False)
        path = "/v1/policies/policy-fixture-01"
        code, before = lab.central(HOST, "GET", path)
        self.assertEqual(code, 200)
        desired = {**before, "name": "reviewed fixture policy"}
        body = {k: v for k, v in desired.items() if k != "id"}
        # Local reviewed delta, followed by a separately approved server preview.
        self.assertEqual({k for k in before if before[k] != desired[k]}, {"name"})
        self.assertEqual(lab.central(HOST, "POST", "/v1/policies/dryrun", desired)[0], 403)
        lab.approve_once("POST", "/v1/policies/dryrun", desired)
        self.assertEqual(lab.central(HOST, "POST", "/v1/policies/dryrun", desired)[0], 200)
        self.assertEqual(lab.central(HOST, "PUT", path, body)[0], 403)
        self.assertEqual(lab.central(HOST, "GET", path)[1], before)
        lab.approve_once("PUT", path, body)
        self.assertEqual(lab.central(HOST, "PUT", path, body)[0], 200)
        self.assertEqual(lab.central(HOST, "GET", path)[1], desired)
        self.assertEqual(lab.central(HOST, "PUT", path, body)[0], 403)
        readonly = FakeACS()
        readonly.approve_once("PUT", path, body)
        self.assertEqual(readonly.central(HOST, "PUT", path, body)[0], 403)
        unknown = {**body, "imaginaryFlag": True}
        lab.approve_once("PUT", path, unknown)
        self.assertEqual(lab.central(HOST, "PUT", path, unknown)[0], 400)
        self.assertEqual(lab.cli("roxctl", ["image", "scan", "--image", "fixture:latest"])[0], 2)
        self.assertEqual(lab.cli("oc", ["get", "central", "-o", "yaml"])[0], 2)

    def test_uncertain_result_is_read_back_not_blindly_retried(self):
        lab = FakeACS(readonly=False)
        path = "/v1/policies/policy-fixture-01"
        body = {"name": "timeout fixture", "disabled": False}
        lab.approve_once("PUT", path, body)
        self.assertEqual(lab.central(HOST, "PUT", path, body, uncertain=True)[0], 504)
        self.assertEqual(lab.central(HOST, "GET", path)[1]["name"], "timeout fixture")
        self.assertEqual([r[1] for r in lab.trace], ["PUT", "GET"])

    def test_real_subprocesses_are_only_fake_transports(self):
        for binary, command in (("roxctl", ["version"]), ("oc", ["--kubeconfig", "/fixture/readonly.kubeconfig", "explain", "central.spec", "--api-version=platform.stackrox.io/v1alpha1"])):
            result = subprocess.run([sys.executable, str(ROOT / "tests/fake_acs.py"), "--transport", binary, "--", *command], text=True, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn("synthetic", result.stdout)
        requests = [{"id": 1, "method": "initialize"}, {"id": 2, "method": "tools/list"}]
        result = subprocess.run([sys.executable, str(ROOT / "tests/fake_acs.py"), "--transport", "mcp"], input="\n".join(map(json.dumps, requests)), text=True, capture_output=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual({t["name"] for t in json.loads(result.stdout.splitlines()[1])["result"]["tools"]}, set(TOOLS))


@unittest.skipUnless(importlib.util.find_spec("yaml"), "requires pinned PyYAML")
class ACSIntegrity(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        sys.path.insert(0, str(ROOT / "tools/docs"))
        import build
        cls.build = build

    @unittest.skipUnless(shutil.which("pandoc"), "requires pinned Pandoc")
    def test_final_code_and_table_text_still_match_before_link_rewriting(self):
        from concurrent.futures import ThreadPoolExecutor
        from acs import pandoc, signature
        report = json.loads((DOCS / "CONVERSION.json").read_text())
        def check(item):
            path, recorded = item
            codes, tables = signature(json.loads(pandoc(pandoc((DOCS / path).read_text(), "gfm", "html"), "html", "json")))
            return (path, hashlib.sha256(json.dumps(codes).encode()).hexdigest() == recorded["code_sha256"],
                    hashlib.sha256(json.dumps(tables).encode()).hexdigest() == recorded["table_text_sha256"])
        with ThreadPoolExecutor(max_workers=4) as pool:
            results = list(pool.map(check, report["topics"].items()))
        self.assertEqual([r for r in results if not all(r[1:])], [])

    def test_topic_map_api_refs_hashes_assets_and_provenance(self):
        from convert import parse_topic_map, collect_topics, should_include_topic
        import yaml
        lock = json.loads((ROOT / "tools/docs/acs.lock.json").read_text())
        source = json.loads((DOCS / "SOURCE.json").read_text())
        report = json.loads((DOCS / "CONVERSION.json").read_text())
        self.build.verify_converter(lock)
        self.assertEqual(source["sources"], lock["sources"])
        self.assertEqual(source["artifact"]["version"], "4.11")
        self.assertEqual(self.build.markdown_manifest(DOCS), (227, lock["expected_output"]["markdown_manifest_sha256"]))
        self.assertEqual(hashlib.sha256((DOCS / "CONVERSION.json").read_bytes()).hexdigest(), source["integrity"]["conversion_report_sha256"])
        self.assertEqual(hashlib.sha256((DOCS / "TOPIC_MAP.yml").read_bytes()).hexdigest(), report["topic_map_sha256"])
        expected = []
        for group in yaml.safe_load_all((DOCS / "TOPIC_MAP.yml").read_text()):
            if group and should_include_topic(group, "openshift-acs"):
                expected += collect_topics(group.get("Topics", []), group.get("Dir", ""), "openshift-acs")
        self.assertEqual(sorted(report["topics"]), sorted(str(Path(t["source"]).with_suffix(".md")) for t in expected))
        self.assertEqual(len(expected), 225)
        self.assertEqual(report["topics"]["rest_api/PolicyService/PolicyService.md"]["tables"], 37)
        self.assertGreater(report["topics"]["rest_api/CommonObjectReference/CommonObjectReference.md"]["tables"], 500)
        self.assertGreater(sum(t["code_blocks"] for t in report["topics"].values()), 100)
        self.assertGreater(len(report["image_sha256"]), 5)
        for path, digest in report["image_sha256"].items():
            self.assertEqual(hashlib.sha256((DOCS / path).read_bytes()).hexdigest(), digest)
        self.assertGreater(self.build.verify_local_links(DOCS), 1500)

    @unittest.skipUnless(importlib.util.find_spec("bs4"), "requires pinned BeautifulSoup")
    def test_rendered_local_links_fragments_and_images(self):
        from bs4 import BeautifulSoup
        anchors = {p: set(re.findall(r'<a id="([^"]+)"', p.read_text())) for p in DOCS.rglob("*.md")}
        from urllib.parse import unquote, urlsplit
        for path in DOCS.rglob("*.md"):
            text = path.read_text()
            targets = re.findall(r'!?\[[^\]\n]*\]\(([^\s)]+)(?:\s+"[^"\n]*")?\)', text)
            soup = BeautifulSoup(text, "html.parser")
            targets += [n.get("href") or n.get("src") for n in soup.find_all(["a", "img"]) if n.get("href") or n.get("src")]
            for target in targets:
                parts = urlsplit(target)
                if parts.scheme or target.startswith("//"):
                    self.assertFalse(target.startswith("data:"), path)
                    continue
                resolved = (path.parent / unquote(parts.path)).resolve() if parts.path else path.resolve()
                self.assertTrue(resolved.is_relative_to(DOCS.resolve()) and resolved.is_file(), (path, target))
                if parts.fragment:
                    self.assertIn(unquote(parts.fragment), anchors.get(resolved, set()), (path, target))

    def test_acs_version_derivation_rejects_unknown_and_conflicts(self):
        from convert import get_distro_attributes
        self.assertEqual(get_distro_attributes({}, "openshift-acs", "rhacs-docs-4.11")["product-version"], "4.11")
        with self.assertRaises(ValueError):
            get_distro_attributes({}, "openshift-acs", "rhacs-docs")
        with self.assertRaises(ValueError):
            get_distro_attributes({"openshift-acs": {"branches": {"rhacs-docs-4.11": {"name": "4.10"}}}}, "openshift-acs", "rhacs-docs-4.11")

    def test_vendor_webhook_examples_are_sanitized_not_bypassed(self):
        from acs import redact_examples
        sample = "https://hooks.slack.com/" + "services/" + "/".join(("synthetic", "example", "not-a-credential"))
        redacted, count = redact_examples(sample)
        self.assertEqual(count, 1)
        self.assertTrue(redacted.endswith("REPLACE_WORKSPACE/REPLACE_CHANNEL/REPLACE_TOKEN"))
        report = json.loads((DOCS / "CONVERSION.json").read_text())
        self.assertGreater(sum(t["redacted_webhook_examples"] for t in report["topics"].values()), 0)
        for path in DOCS.rglob("*.md"):
            for value in re.findall(r"https://hooks\.slack\.com/services/[A-Za-z0-9/_-]+", path.read_text()):
                self.assertEqual(value, redacted, path)
