from __future__ import annotations

import ast
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
GENERATOR = (
    ROOT
    / ".agents"
    / "skills"
    / "openshift-mcp"
    / "scripts"
    / "generate-opencode-mcp-config.py"
)
PYTHON = os.environ.get("PYTHON", sys.executable)


class OpenCodeConfigGeneratorTest(unittest.TestCase):
    def run_generator(self, config: Path, *arguments: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [PYTHON, str(GENERATOR), "--config", str(config), *arguments],
            check=False,
            capture_output=True,
            text=True,
            timeout=20,
        )

    def test_generator_uses_python_39_grammar(self) -> None:
        source = GENERATOR.read_text(encoding="utf-8")
        ast.parse(source, filename=str(GENERATOR), feature_version=(3, 9))

    def test_preview_creates_no_file(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            config = Path(temporary) / "opencode.json"
            result = self.run_generator(config, "--profile", "both")

            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertFalse(config.exists())
            self.assertIn("Mode: preview", result.stdout)
            self.assertIn("MCP ocp_read: add", result.stdout)
            self.assertIn("MCP argocd_read: add", result.stdout)
            self.assertIn("Persistent changes: none", result.stdout)

    def test_apply_preserves_existing_config_and_is_idempotent(self) -> None:
        openshift_command = ["npx", "--no-install", "customer-ocp-mcp", "stdio"]
        argocd_command = ["npx", "--offline", "customer-argocd-mcp", "stdio"]
        with tempfile.TemporaryDirectory() as temporary:
            config = Path(temporary) / "opencode.json"
            original = {
                "$schema": "https://opencode.ai/config.json",
                "provider": {"customer": {"name": "preserve-me"}},
                "mcp": {"unrelated": {"type": "remote", "url": "https://mcp.example"}},
                "permission": {"*": "deny"},
            }
            config.write_text(json.dumps(original), encoding="utf-8")

            arguments = (
                "--profile",
                "both",
                "--openshift-command-json",
                json.dumps(openshift_command),
                "--argocd-command-json",
                json.dumps(argocd_command),
                "--include-argocd-ca",
                "--apply",
            )
            first = self.run_generator(config, *arguments)
            self.assertEqual(first.returncode, 0, first.stderr)
            generated = json.loads(config.read_text(encoding="utf-8"))

            self.assertEqual(generated["provider"], original["provider"])
            self.assertEqual(generated["mcp"]["unrelated"], original["mcp"]["unrelated"])
            self.assertEqual(generated["mcp"]["ocp_read"]["command"], openshift_command)
            self.assertEqual(generated["mcp"]["argocd_read"]["command"], argocd_command)
            self.assertEqual(generated["permission"]["ocp_read_*"], "allow")
            self.assertEqual(generated["permission"]["argocd_read_*"], "allow")
            environment = generated["mcp"]["argocd_read"]["environment"]
            self.assertEqual(environment["MCP_READ_ONLY"], "true")
            self.assertEqual(environment["NODE_EXTRA_CA_CERTS"], "{env:NODE_EXTRA_CA_CERTS}")
            self.assertNotIn("ARGOCD_API_TOKEN", config.read_text(encoding="utf-8"))
            self.assertEqual(len(list(config.parent.glob("opencode.json.backup-*"))), 1)

            second = self.run_generator(config, *arguments)
            self.assertEqual(second.returncode, 0, second.stderr)
            self.assertIn("configuration already matches", second.stdout)
            self.assertEqual(len(list(config.parent.glob("opencode.json.backup-*"))), 1)

    def test_conflicting_target_requires_replace(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            config = Path(temporary) / "opencode.json"
            original = {"mcp": {"ocp_read": {"type": "local", "command": ["old"]}}}
            config.write_text(json.dumps(original), encoding="utf-8")

            result = self.run_generator(config, "--profile", "openshift", "--apply")

            self.assertNotEqual(result.returncode, 0)
            self.assertIn("--replace", result.stderr)
            self.assertEqual(json.loads(config.read_text(encoding="utf-8")), original)

    def test_equivalent_command_under_another_name_is_rejected(self) -> None:
        command = ["npx", "--no-install", "customer-ocp-mcp", "stdio"]
        with tempfile.TemporaryDirectory() as temporary:
            config = Path(temporary) / "opencode.json"
            original = {"mcp": {"openshift-mcp": {"type": "local", "command": command}}}
            config.write_text(json.dumps(original), encoding="utf-8")

            result = self.run_generator(
                config,
                "--profile",
                "openshift",
                "--openshift-command-json",
                json.dumps(command),
                "--apply",
            )

            self.assertNotEqual(result.returncode, 0)
            self.assertIn("refusing duplicate", result.stderr)
            self.assertEqual(json.loads(config.read_text(encoding="utf-8")), original)

    def test_npx_must_be_offline_or_no_install(self) -> None:
        command = ["npx", "customer-ocp-mcp", "stdio"]
        with tempfile.TemporaryDirectory() as temporary:
            config = Path(temporary) / "opencode.json"
            result = self.run_generator(
                config,
                "--profile",
                "openshift",
                "--openshift-command-json",
                json.dumps(command),
            )

            self.assertNotEqual(result.returncode, 0)
            self.assertIn("without --no-install or --offline", result.stderr)
            self.assertFalse(config.exists())

    def test_command_must_not_contain_credential_arguments(self) -> None:
        command = ["npx", "--no-install", "customer-argocd-mcp", "--token=secret"]
        with tempfile.TemporaryDirectory() as temporary:
            config = Path(temporary) / "opencode.json"
            result = self.run_generator(
                config,
                "--profile",
                "argocd",
                "--argocd-command-json",
                json.dumps(command),
            )

            self.assertNotEqual(result.returncode, 0)
            self.assertIn("must not contain token", result.stderr)
            self.assertNotIn("secret", result.stderr)
            self.assertFalse(config.exists())


if __name__ == "__main__":
    unittest.main()
