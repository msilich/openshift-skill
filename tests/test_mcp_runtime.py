from __future__ import annotations

import os
from pathlib import Path
import re
import subprocess
import tempfile
import tomllib
import unittest


ROOT = Path(__file__).resolve().parents[1]
EXAMPLES = ROOT / ".agents" / "skills" / "openshift-mcp" / "assets"


class McpRuntimeTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.binary = os.environ.get("MCP_SERVER_BIN", "")
        if not cls.binary:
            raise unittest.SkipTest("set MCP_SERVER_BIN to test the real pinned MCP binary")

    def test_day2_enables_every_registered_toolset(self) -> None:
        help_result = subprocess.run(
            [self.binary, "--help"],
            check=False,
            capture_output=True,
            text=True,
            timeout=30,
        )
        self.assertEqual(help_result.returncode, 0, help_result.stderr)
        match = re.search(r"available toolsets: ([^)]+)", help_result.stdout)
        self.assertIsNotNone(match, help_result.stdout)
        registered = {item.strip() for item in match.group(1).split(",")}
        profile = tomllib.loads(
            (EXAMPLES / "openshift-mcp.day2.toml").read_text(encoding="utf-8")
        )
        self.assertEqual(set(profile["toolsets"]), registered)
        self.assertIn("configuration_view", profile["disabled_tools"])

    def test_real_server_accepts_both_profiles_without_cluster_access(self) -> None:
        kubeconfig = """\
apiVersion: v1
kind: Config
clusters:
  - name: validation
    cluster:
      server: https://127.0.0.1:9
      insecure-skip-tls-verify: true
contexts:
  - name: validation
    context:
      cluster: validation
      user: validation
current-context: validation
users:
  - name: validation
    user:
      token: validation-only
"""
        with tempfile.TemporaryDirectory() as temp:
            kubeconfig_path = Path(temp) / "kubeconfig"
            kubeconfig_path.write_text(kubeconfig, encoding="utf-8")
            for profile_name in ("readonly", "day2"):
                result = subprocess.run(
                    [
                        self.binary,
                        "--config",
                        str(EXAMPLES / f"openshift-mcp.{profile_name}.toml"),
                        "--kubeconfig",
                        str(kubeconfig_path),
                        "--cluster-provider",
                        "disabled",
                    ],
                    input="",
                    check=False,
                    capture_output=True,
                    text=True,
                    timeout=30,
                )
                self.assertEqual(
                    result.returncode,
                    0,
                    f"{profile_name} profile rejected by MCP runtime:\n{result.stderr}",
                )


if __name__ == "__main__":
    unittest.main()
