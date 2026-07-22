from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import tempfile
import tomllib
import unittest


ROOT = Path(__file__).resolve().parents[1]
SKILLS_ROOT = ROOT / ".agents" / "skills"
SKILL_NAMES = ("openshift-mcp", "openshift-api", "openshift-docs")
EXAMPLES = SKILLS_ROOT / "openshift-mcp" / "assets"


def load_jsonc(path: Path) -> dict[str, object]:
    text = "\n".join(
        line for line in path.read_text(encoding="utf-8").splitlines() if not line.lstrip().startswith("//")
    )
    return json.loads(text)


def frontmatter(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    match = re.match(r"\A---\n(?P<header>.*?)\n---\n", text, re.DOTALL)
    if not match:
        raise AssertionError(f"missing YAML frontmatter: {path}")
    result: dict[str, str] = {}
    for line in match.group("header").splitlines():
        key, separator, value = line.partition(":")
        if not separator:
            raise AssertionError(f"unsupported frontmatter line in {path}: {line}")
        result[key.strip()] = value.strip()
    return result


class SkillBundleTest(unittest.TestCase):
    def test_public_readme_has_reproducible_mcp_installation(self) -> None:
        text = (ROOT / "README.md").read_text(encoding="utf-8")
        for marker in (
            "git clone https://github.com/openshift/openshift-mcp-server.git",
            "git checkout --detach a0a1c370fcce18f76cecdbb2e07d8f4dbafe92dd",
            "make build",
            "kubernetes-mcp-server --help",
            "sha256sum --check",
            "opencode mcp list",
        ):
            self.assertIn(marker, text)
        self.assertNotIn("/Users/", text)
        self.assertNotIn("INTERNAL_QWEN", text)

    def test_public_ignore_rules_cover_local_credentials_and_logs(self) -> None:
        text = (ROOT / ".gitignore").read_text(encoding="utf-8")
        for marker in ("*.log", ".env", "*.kubeconfig", "*.pem", "*.key"):
            self.assertIn(marker, text)

    def test_readme_local_links_resolve(self) -> None:
        readme = ROOT / "README.md"
        pattern = re.compile(r"\[[^]]+\]\(([^)]+)\)")
        for target in pattern.findall(readme.read_text(encoding="utf-8")):
            path_part = target.split("#", 1)[0]
            if not path_part or "://" in path_part:
                continue
            self.assertTrue((ROOT / path_part).resolve().exists(), target)

    def test_skills_have_minimal_frontmatter_and_no_placeholders(self) -> None:
        for name in SKILL_NAMES:
            skill = SKILLS_ROOT / name / "SKILL.md"
            self.assertTrue(skill.is_file(), skill)
            header = frontmatter(skill)
            self.assertEqual(set(header), {"name", "description"})
            self.assertEqual(header["name"], name)
            self.assertGreater(len(header["description"]), 40)
            self.assertNotRegex(skill.read_text(encoding="utf-8"), r"\bTODO\b|\[TODO")

    def test_all_local_skill_links_resolve(self) -> None:
        pattern = re.compile(r"\[[^]]+\]\(([^)]+)\)")
        for name in SKILL_NAMES:
            skill = SKILLS_ROOT / name / "SKILL.md"
            for target in pattern.findall(skill.read_text(encoding="utf-8")):
                if "://" in target or target.startswith("#"):
                    continue
                resolved = (skill.parent / target).resolve()
                self.assertTrue(resolved.exists(), f"broken link in {skill}: {target}")

    def test_trigger_corpus_covers_english_and_german(self) -> None:
        cases = json.loads(
            (ROOT / "tests" / "fixtures" / "skill_trigger_cases.json").read_text(encoding="utf-8")
        )
        self.assertEqual({case["expected_skill"] for case in cases}, set(SKILL_NAMES))
        prompts = [case["prompt"] for case in cases]
        self.assertTrue(any("Wie " in prompt or "Welche " in prompt or "Skaliere " in prompt for prompt in prompts))
        self.assertTrue(any(prompt.startswith(("Diagnose", "Verify", "Find")) for prompt in prompts))

    def test_source_lock_contains_exact_pins(self) -> None:
        lock = json.loads((ROOT / "sources.lock.json").read_text(encoding="utf-8"))
        sources = lock["sources"]
        self.assertEqual(sources["opencode"]["version"], "1.18.4")
        self.assertEqual(
            sources["openshift_mcp_server"]["commit"],
            "a0a1c370fcce18f76cecdbb2e07d8f4dbafe92dd",
        )
        self.assertEqual(
            sources["argocd_mcp_server"]["commit"],
            "1bb80b2816f0c8810efedc2fdcf318fd18ce214d",
        )
        self.assertEqual(
            sources["agentic_skills"]["commit"],
            "b09c2e645940b945c5a224a8f14927e10216ba07",
        )
        self.assertEqual(
            sources["openshift_docs"]["commit"],
            "5aee2719f9ad01a82bb80b391e5af25f566c73c0",
        )

    def test_opencode_profiles_are_airgap_scoped(self) -> None:
        for filename in ("opencode.readonly.jsonc", "opencode.day2.jsonc"):
            config = load_jsonc(EXAMPLES / filename)
            self.assertFalse(config["autoupdate"])
            self.assertEqual(config["share"], "disabled")
            self.assertNotIn("model", config)
            self.assertNotIn("provider", config)
            skill_rules = config["permission"]["skill"]
            for skill in SKILL_NAMES:
                self.assertEqual(skill_rules[skill], "allow")
            self.assertEqual(
                config["permission"]["bash"]["bash *openshift-api/scripts/collect-discovery.sh *"],
                "ask",
            )

    def test_optional_qwen_provider_uses_environment_secrets(self) -> None:
        config = load_jsonc(EXAMPLES / "opencode.qwen-provider.jsonc")
        self.assertEqual(config["enabled_providers"], ["qwen"])
        rendered = json.dumps(config)
        self.assertIn("{env:QWEN_BASE_URL}", rendered)
        self.assertIn("{env:QWEN_API_KEY}", rendered)
        self.assertIn("REPLACE_WITH_QWEN_MODEL_ID", rendered)

    def test_optional_argocd_profile_is_separate_and_read_only(self) -> None:
        config = load_jsonc(EXAMPLES / "opencode.readonly-with-argocd.jsonc")
        self.assertEqual(set(config["mcp"]), {"ocp_read", "argocd_read"})
        self.assertEqual(
            config["mcp"]["argocd_read"]["command"],
            ["{env:ARGOCD_MCP_NODE}", "{env:ARGOCD_MCP_ENTRYPOINT}", "stdio"],
        )
        self.assertEqual(config["permission"]["ocp_read_*"], "allow")
        self.assertEqual(config["permission"]["argocd_read_*"], "allow")
        rendered = json.dumps(config)
        self.assertNotIn("ARGOCD_API_TOKEN", rendered)
        self.assertNotIn("NODE_TLS_REJECT_UNAUTHORIZED", rendered)

    def test_argocd_account_policy_allows_only_reads(self) -> None:
        directory = EXAMPLES / "argocd-readonly-rbac"
        account = json.loads((directory / "argocd-cm.merge.json").read_text(encoding="utf-8"))
        self.assertEqual(account["data"]["accounts.opencode-mcp"], "apiKey")
        policy_patch = json.loads(
            (directory / "argocd-rbac-cm.merge.json").read_text(encoding="utf-8")
        )
        policy = policy_patch["data"]["policy.opencode-mcp.csv"]
        rules = [[part.strip() for part in line.split(",")] for line in policy.splitlines()]
        self.assertTrue(rules)
        self.assertTrue(all(len(rule) == 6 and rule[0] == "p" for rule in rules))
        allowed = [rule for rule in rules if rule[5] == "allow"]
        denied = [rule for rule in rules if rule[5] == "deny"]
        self.assertTrue(all(rule[3] == "get" for rule in allowed))
        self.assertIn(["p", "opencode-mcp", "applications", "sync", "*", "deny"], denied)
        self.assertIn(["p", "opencode-mcp", "exec", "create", "*", "deny"], denied)

    def test_readonly_profile_has_no_generic_oc_escape(self) -> None:
        config = load_jsonc(EXAMPLES / "opencode.readonly.jsonc")
        bash_rules = config["permission"]["bash"]
        self.assertEqual(bash_rules["*"], "deny")
        self.assertNotIn("oc --kubeconfig {env:OPENSHIFT_MCP_READ_KUBECONFIG} *", bash_rules)
        forbidden = (" apply", " create", " delete", " edit", " patch", " replace", " scale", " rollout restart")
        for command, action in bash_rules.items():
            if command == "*":
                continue
            self.assertIn(action, {"allow", "ask"})
            self.assertFalse(any(token in command for token in forbidden), command)

    def test_day2_profile_requires_ask_and_denies_identity_changes(self) -> None:
        config = load_jsonc(EXAMPLES / "opencode.day2.jsonc")
        permission = config["permission"]
        self.assertEqual(permission["ocp_day2_*"], "ask")
        bash_rules = permission["bash"]
        self.assertEqual(bash_rules["*"], "deny")
        self.assertEqual(
            bash_rules["oc --kubeconfig {env:OPENSHIFT_MCP_DAY2_KUBECONFIG} *"], "ask"
        )
        denied = [pattern for pattern, action in bash_rules.items() if action == "deny" and pattern != "*"]
        self.assertTrue(any("config use-context" in pattern for pattern in denied))
        self.assertTrue(any("whoami -t" in pattern for pattern in denied))

    def test_mcp_profiles_parse_and_day2_is_full(self) -> None:
        readonly = tomllib.loads((EXAMPLES / "openshift-mcp.readonly.toml").read_text(encoding="utf-8"))
        day2 = tomllib.loads((EXAMPLES / "openshift-mcp.day2.toml").read_text(encoding="utf-8"))
        self.assertTrue(readonly["read_only"])
        self.assertFalse(day2["read_only"])
        self.assertFalse(day2["disable_destructive"])
        self.assertTrue(day2["validation_enabled"])
        required_toolsets = {
            "core",
            "cluster-diagnostics",
            "helm",
            "kubevirt",
            "netedge",
            "netobserv",
            "oadp",
            "observability/logs",
            "observability/metrics",
            "observability/otelcol",
            "observability/traces",
            "openshift",
            "openshift/mustgather",
            "ossm",
            "tekton",
        }
        self.assertTrue(required_toolsets.issubset(set(day2["toolsets"])))
        self.assertIn("config", day2["toolsets"])
        self.assertIn("kcp", day2["toolsets"])
        self.assertIn("configuration_view", day2["disabled_tools"])
        self.assertNotIn("confirmation_rules", day2)
        self.assertEqual(day2["confirmation_fallback"], "deny")

    def test_secret_policy_requires_a_user_choice(self) -> None:
        text = (SKILLS_ROOT / "openshift-mcp" / "SKILL.md").read_text(encoding="utf-8")
        normalized = text.lower()
        self.assertIn("metadata and key names only", normalized)
        self.assertIn("placeholder commands only", normalized)
        self.assertIn("named raw secret processing", normalized)
        self.assertIn("abort secret access", normalized)
        self.assertIn("current task", normalized)
        self.assertIn("local opencode session data", normalized)
        self.assertRegex(
            text,
            r"(?i)(?:if no choice.*(?:stop|ask)|(?:stop|ask).*if no choice)",
        )
        self.assertNotRegex(text, r"(?i)default to option")

    def test_day2_contract_has_all_ordered_gates(self) -> None:
        text = (
            SKILLS_ROOT / "openshift-mcp" / "references" / "operations.md"
        ).read_text(encoding="utf-8")
        workflow = text.split("## Tool selection", 1)[0].lower()
        markers = [
            "inspect only the relevant objects",
            "verify the exact served api version",
            "explain the exact intended delta",
            "server-side dry-run or diff",
            "fresh `once` approval",
            "execute one bounded change",
            "re-read the changed object",
        ]
        positions = [workflow.index(marker) for marker in markers]
        self.assertEqual(positions, sorted(positions))
        self.assertIn("if the api or operation has no preview", workflow)
        for risk in ("delete", "drain", "debug", "rbac", "operator", "storage", "network"):
            self.assertIn(risk, text.lower())

    def test_docs_defers_to_the_connected_cluster_api(self) -> None:
        text = (SKILLS_ROOT / "openshift-docs" / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn("live discovery through `openshift-api` as authoritative", text)

    def test_complete_docs_snapshot_and_search(self) -> None:
        docs_skill = SKILLS_ROOT / "openshift-docs"
        docs = docs_skill / "references" / "ocp-4.20"
        source = json.loads((docs / "SOURCE.json").read_text(encoding="utf-8"))
        self.assertEqual(source["artifact"]["version"], "4.20")
        self.assertEqual(source["artifact"]["converted_topics"], 1746)
        self.assertEqual(source["conversion"]["failed_topics"], 0)
        self.assertEqual(
            source["sources"]["openshift_docs"]["commit"],
            "5aee2719f9ad01a82bb80b391e5af25f566c73c0",
        )
        markdown_files = sorted(docs.rglob("*.md"))
        self.assertEqual(len(markdown_files), 1748)
        manifest = "".join(
            f"{hashlib.sha256(path.read_bytes()).hexdigest()}  {path.relative_to(docs).as_posix()}\n"
            for path in markdown_files
        ).encode("utf-8")
        self.assertEqual(
            hashlib.sha256(manifest).hexdigest(),
            source["integrity"]["markdown_manifest_sha256"],
        )
        link_pattern = re.compile(r"\[[^]]*\]\(([^)]+)\)")
        checked_links = 0
        for document in markdown_files:
            for target in link_pattern.findall(document.read_text(encoding="utf-8")):
                path_part = target.split("#", 1)[0]
                if not path_part or "://" in path_part or not path_part.endswith(".md"):
                    continue
                checked_links += 1
                self.assertTrue(
                    (document.parent / path_part).resolve().is_file(),
                    f"broken offline documentation link in {document}: {target}",
                )
        self.assertGreater(checked_links, 10_000)
        result = subprocess.run(
            [
                os.environ.get("PYTHON", "python3"),
                str(docs_skill / "scripts" / "search_docs.py"),
                "ingress certificate",
                "--max-results",
                "3",
            ],
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn(":", result.stdout)

    def test_real_opencode_discovers_all_skills_when_available(self) -> None:
        binary = os.environ.get("OPENCODE_BIN")
        if not binary:
            self.skipTest("set OPENCODE_BIN to run the real OpenCode discovery check")
        with tempfile.TemporaryDirectory() as temp:
            base = Path(temp)
            env = os.environ.copy()
            env.update(
                {
                    "XDG_CONFIG_HOME": str(base / "config"),
                    "XDG_DATA_HOME": str(base / "data"),
                    "XDG_CACHE_HOME": str(base / "cache"),
                    "XDG_STATE_HOME": str(base / "state"),
                }
            )
            result = subprocess.run(
                [binary, "--pure", "debug", "skill"],
                cwd=ROOT,
                env=env,
                check=False,
                capture_output=True,
                text=True,
                timeout=30,
            )
        self.assertEqual(result.returncode, 0, result.stderr)
        discovered = {item["name"] for item in json.loads(result.stdout)}
        self.assertTrue(set(SKILL_NAMES).issubset(discovered))


if __name__ == "__main__":
    unittest.main()
