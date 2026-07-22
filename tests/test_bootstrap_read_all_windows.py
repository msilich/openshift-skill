import os
import shutil
import subprocess
import tempfile
import textwrap
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = (
    ROOT
    / ".agents"
    / "skills"
    / "openshift-mcp"
    / "scripts"
    / "Bootstrap-ReadAll.ps1"
)


def find_powershell() -> str | None:
    return shutil.which("pwsh") or shutil.which("powershell")


class BootstrapReadAllWindowsTests(unittest.TestCase):
    def setUp(self) -> None:
        self.powershell = find_powershell()
        if not self.powershell:
            self.skipTest("PowerShell is required")

    def make_harness(self, directory: Path) -> Path:
        harness = directory / "harness.ps1"
        harness.write_text(
            textwrap.dedent(
                r"""
                Set-StrictMode -Version Latest
                $ErrorActionPreference = "Stop"

                function global:oc {
                    $arguments = @($args | ForEach-Object { [string]$_ })
                    $joined = " " + ($arguments -join " ") + " "
                    Add-Content -LiteralPath $env:FAKE_OC_LOG -Value ($arguments -join " ")
                    $global:LASTEXITCODE = 0

                    $kubeconfig = ""
                    for ($index = 0; $index -lt $arguments.Count; $index++) {
                        if ($arguments[$index] -eq "--kubeconfig" -and $index + 1 -lt $arguments.Count) {
                            $kubeconfig = $arguments[$index + 1]
                        }
                        elseif ($arguments[$index].StartsWith("--kubeconfig=")) {
                            $kubeconfig = $arguments[$index].Substring("--kubeconfig=".Length)
                        }
                    }

                    if ($joined.Contains(" config current-context ")) {
                        "customer-admin-context"
                    }
                    elseif ($joined.Contains(" config set-cluster ")) {
                        $directory = Split-Path -Parent $kubeconfig
                        New-Item -ItemType Directory -Path $directory -Force | Out-Null
                        [IO.File]::WriteAllText($kubeconfig, "")
                    }
                    elseif (
                        $joined.Contains(" config set-credentials ") -or
                        $joined.Contains(" config set-context ") -or
                        $joined.Contains(" config use-context ")
                    ) {
                        return
                    }
                    elseif ($joined.Contains(" config view ")) {
                        if ($joined.Contains("go-template=")) {
                            "1 1 1"
                        }
                        elseif ($joined.Contains("certificate-authority-data")) {
                            [Convert]::ToBase64String([IO.File]::ReadAllBytes($env:FAKE_CA_PATH))
                        }
                        elseif ($joined.Contains("insecure-skip-tls-verify")) {
                            $env:FAKE_INSECURE_TLS
                        }
                        elseif ($joined.Contains("clusters[0].cluster.server")) {
                            $env:FAKE_SERVER
                        }
                        else {
                            $global:LASTEXITCODE = 9
                            "unexpected config view: $joined"
                        }
                    }
                    elseif ($joined.Contains(" whoami --show-server ")) {
                        $env:FAKE_SERVER
                    }
                    elseif ($joined.Contains(" whoami ")) {
                        if ($kubeconfig -eq $env:FAKE_ADMIN_KUBECONFIG) {
                            $env:FAKE_ADMIN_IDENTITY
                        }
                        else {
                            "system:serviceaccount:openshift-mcp:opencode-admin-readonly"
                        }
                    }
                    elseif ($joined.Contains(" get --raw /version ")) {
                        '{"gitVersion":"v1.fake"}'
                    }
                    elseif ($joined.Contains(" get serviceaccount opencode-admin-readonly ")) {
                        "serviceaccount/opencode-admin-readonly"
                    }
                    elseif ($joined.Contains(" auth can-i ")) {
                        if (
                            $joined.Contains(" create ") -or
                            $joined.Contains(" patch ") -or
                            $joined.Contains(" delete ")
                        ) {
                            "no"
                        }
                        else {
                            "yes"
                        }
                    }
                    elseif ($joined.Contains(" diff -f ")) {
                        $global:LASTEXITCODE = 1
                    }
                    elseif ($joined.Contains(" apply --dry-run=server ")) {
                        "namespace/openshift-mcp"
                        "serviceaccount/opencode-admin-readonly"
                        "clusterrole.rbac.authorization.k8s.io/opencode-admin-read-all"
                        "clusterrolebinding.rbac.authorization.k8s.io/opencode-admin-read-all"
                    }
                    elseif ($joined.Contains(" apply -f ")) {
                        "namespace/openshift-mcp configured"
                        "serviceaccount/opencode-admin-readonly configured"
                        "clusterrole.rbac.authorization.k8s.io/opencode-admin-read-all configured"
                        "clusterrolebinding.rbac.authorization.k8s.io/opencode-admin-read-all configured"
                    }
                    elseif ($joined.Contains(" create token opencode-admin-readonly ")) {
                        "fake-service-account-token"
                    }
                    else {
                        $global:LASTEXITCODE = 10
                        "unexpected fake oc arguments: $joined"
                    }
                }

                $parameters = @{
                    Command = $env:BOOTSTRAP_PHASE
                    AdminKubeconfig = $env:FAKE_ADMIN_KUBECONFIG
                    ExpectedServer = $env:EXPECTED_SERVER
                    ExpectedAdminIdentity = $env:FAKE_ADMIN_IDENTITY
                    OutputKubeconfig = $env:FAKE_OUTPUT
                }
                if ($env:INCLUDE_EXPLICIT_CA -eq "1") {
                    $parameters.ClusterCAPath = $env:FAKE_CA_PATH
                }

                & $env:BOOTSTRAP_SCRIPT @parameters | ConvertTo-Json -Depth 10
                """
            ).strip()
            + "\n",
            encoding="utf-8",
        )
        return harness

    def run_phase(
        self,
        phase: str,
        admin: Path,
        ca: Path,
        output: Path,
        log: Path,
        harness: Path,
        expected_server: str = "https://api.customer.example:6443",
        include_explicit_ca: bool = True,
        insecure_tls: str = "",
    ) -> subprocess.CompletedProcess[str]:
        environment = os.environ.copy()
        environment.update(
            {
                "BOOTSTRAP_SCRIPT": str(SCRIPT),
                "BOOTSTRAP_PHASE": phase,
                "FAKE_ADMIN_KUBECONFIG": str(admin),
                "FAKE_CA_PATH": str(ca),
                "FAKE_OUTPUT": str(output),
                "FAKE_OC_LOG": str(log),
                "FAKE_SERVER": "https://api.customer.example:6443",
                "EXPECTED_SERVER": expected_server,
                "FAKE_ADMIN_IDENTITY": "customer-admin",
                "FAKE_INSECURE_TLS": insecure_tls,
                "INCLUDE_EXPLICIT_CA": "1" if include_explicit_ca else "0",
            }
        )
        return subprocess.run(
            [
                self.powershell,
                "-NoProfile",
                "-NonInteractive",
                "-ExecutionPolicy",
                "Bypass",
                "-File",
                str(harness),
            ],
            cwd=ROOT,
            env=environment,
            text=True,
            capture_output=True,
            check=False,
        )

    def prepare(self, directory: Path) -> tuple[Path, Path, Path, Path, Path]:
        admin = directory / "admin.kubeconfig"
        ca = directory / "customer-ca.pem"
        output = directory / "read-all.kubeconfig"
        log = directory / "oc.log"
        admin.write_text("admin placeholder\n", encoding="utf-8")
        ca.write_text(
            "-----BEGIN CERTIFICATE-----\nZmFrZQ==\n-----END CERTIFICATE-----\n",
            encoding="utf-8",
        )
        return admin, ca, output, log, self.make_harness(directory)

    def test_three_phases_are_ordered_and_token_is_not_emitted(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            admin, ca, output, log, harness = self.prepare(Path(temporary))

            preview = self.run_phase("Preview", admin, ca, output, log, harness)
            self.assertEqual(preview.returncode, 0, preview.stderr)
            self.assertIn('"PersistentChanges":  "none"', preview.stdout)
            self.assertFalse(output.exists())

            apply_rbac = self.run_phase(
                "ApplyRbac", admin, ca, output, log, harness
            )
            self.assertEqual(apply_rbac.returncode, 0, apply_rbac.stderr)
            self.assertIn('"CredentialCreated":  false', apply_rbac.stdout)
            self.assertFalse(output.exists())

            create = self.run_phase(
                "CreateKubeconfig", admin, ca, output, log, harness
            )
            self.assertEqual(create.returncode, 0, create.stderr)
            self.assertIn('"BootstrapCompleted":  true', create.stdout)
            self.assertTrue(output.exists())
            self.assertNotIn(
                "fake-service-account-token",
                preview.stdout + preview.stderr + apply_rbac.stdout + apply_rbac.stderr + create.stdout + create.stderr,
            )

            calls = log.read_text(encoding="utf-8")
            self.assertIn("--insecure-skip-tls-verify=false", calls)
            self.assertNotIn("--insecure-skip-tls-verify=true", calls)
            self.assertNotIn(" login ", f" {calls} ")
            self.assertEqual(calls.count("create token opencode-admin-readonly"), 1)

    def test_can_copy_ca_from_admin_kubeconfig(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            admin, ca, output, log, harness = self.prepare(Path(temporary))
            result = self.run_phase(
                "Preview",
                admin,
                ca,
                output,
                log,
                harness,
                include_explicit_ca=False,
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn("embedded CA from admin kubeconfig", result.stdout)
            self.assertFalse(output.exists())

    def test_rejects_insecure_admin_trust(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            admin, ca, output, log, harness = self.prepare(Path(temporary))
            result = self.run_phase(
                "Preview",
                admin,
                ca,
                output,
                log,
                harness,
                include_explicit_ca=False,
                insecure_tls="true",
            )
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("disables TLS verification", result.stderr)
            calls = log.read_text(encoding="utf-8")
            self.assertNotIn(" diff -f ", f" {calls} ")
            self.assertNotIn(" apply -f ", f" {calls} ")
            self.assertNotIn(" create token ", f" {calls} ")
            self.assertFalse(output.exists())

    def test_target_mismatch_stops_before_mutation(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            admin, ca, output, log, harness = self.prepare(Path(temporary))
            result = self.run_phase(
                "ApplyRbac",
                admin,
                ca,
                output,
                log,
                harness,
                expected_server="https://wrong.example:6443",
            )
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("API server mismatch", result.stderr)
            calls = log.read_text(encoding="utf-8")
            self.assertNotIn(" apply -f ", f" {calls} ")
            self.assertNotIn(" create token ", f" {calls} ")
            self.assertFalse(output.exists())


if __name__ == "__main__":
    unittest.main()
