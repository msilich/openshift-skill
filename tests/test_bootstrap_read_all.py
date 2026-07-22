import os
import shutil
import stat
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
    / "bootstrap-read-all.sh"
)


def bash_path(path: Path) -> str:
    resolved = path.resolve()
    if os.name != "nt":
        return resolved.as_posix()
    drive, tail = os.path.splitdrive(str(resolved))
    tail = tail.lstrip("\\/").replace("\\", "/")
    return f"/{drive[0].lower()}/{tail}"


def find_bash() -> str | None:
    candidates = [
        shutil.which("bash"),
        r"C:\Program Files\Git\bin\bash.exe",
        r"C:\Program Files\Git\usr\bin\bash.exe",
    ]
    for candidate in candidates:
        if candidate and Path(candidate).is_file():
            if os.name == "nt" and Path(candidate).resolve() == Path(
                r"C:\Windows\System32\bash.exe"
            ).resolve():
                continue
            return candidate
    return None


class BootstrapReadAllTests(unittest.TestCase):
    def setUp(self) -> None:
        self.bash = find_bash()
        if not self.bash:
            self.skipTest("A non-WSL bash executable is required")

    def make_fake_oc(self, directory: Path) -> Path:
        fake_bin = directory / "bin"
        fake_bin.mkdir()
        fake_oc = fake_bin / "oc"
        fake_oc.write_text(
            textwrap.dedent(
                r"""\
                #!/usr/bin/env bash
                set -euo pipefail

                printf '%s\n' "$*" >>"$FAKE_OC_LOG"

                kubeconfig=""
                previous=""
                for argument in "$@"; do
                  if [[ "$previous" == "--kubeconfig" ]]; then
                    kubeconfig="$argument"
                  fi
                  case "$argument" in
                    --kubeconfig=*) kubeconfig="${argument#--kubeconfig=}" ;;
                  esac
                  previous="$argument"
                done

                arguments=" $* "

                if [[ "$arguments" == *" config current-context "* ]]; then
                  printf 'customer-admin-context\n'
                elif [[ "$arguments" == *" config set-cluster "* ]]; then
                  mkdir -p -- "$(dirname -- "$kubeconfig")"
                  : >"$kubeconfig"
                elif [[ "$arguments" == *" config set-credentials "* ||
                        "$arguments" == *" config set-context "* ||
                        "$arguments" == *" config use-context "* ]]; then
                  :
                elif [[ "$arguments" == *" config view "* ]]; then
                  if [[ "$arguments" == *"go-template="* ]]; then
                    printf '1 1 1\n'
                  elif [[ "$arguments" == *"certificate-authority-data"* ]]; then
                    base64 <"$FAKE_CA_PATH" | tr -d '\r\n'
                  elif [[ "$arguments" == *"insecure-skip-tls-verify"* ]]; then
                    printf '%s' "${FAKE_INSECURE_TLS:-}"
                  elif [[ "$arguments" == *"contexts[0].context.user"* ]]; then
                    printf 'opencode-admin-readonly\n'
                  elif [[ "$arguments" == *"clusters[0].cluster.server"* ]]; then
                    printf '%s\n' "$FAKE_SERVER"
                  else
                    printf 'unexpected config view: %s\n' "$*" >&2
                    exit 9
                  fi
                elif [[ "$arguments" == *" whoami --show-server "* ]]; then
                  printf '%s\n' "$FAKE_SERVER"
                elif [[ "$arguments" == *" whoami "* ]]; then
                  if [[ "$kubeconfig" == "$FAKE_ADMIN_KUBECONFIG" ]]; then
                    printf '%s\n' "$FAKE_ADMIN_IDENTITY"
                  else
                    printf 'system:serviceaccount:openshift-mcp:opencode-admin-readonly\n'
                  fi
                elif [[ "$arguments" == *" get --raw /version "* ]]; then
                  printf '{"gitVersion":"v1.fake"}\n'
                elif [[ "$arguments" == *" get serviceaccount opencode-admin-readonly "* ]]; then
                  printf 'serviceaccount/opencode-admin-readonly\n'
                elif [[ "$arguments" == *" auth can-i "* ]]; then
                  if [[ "$arguments" == *" create "* ||
                        "$arguments" == *" patch "* ||
                        "$arguments" == *" delete "* ]]; then
                    printf 'no\n'
                  else
                    printf 'yes\n'
                  fi
                elif [[ "$arguments" == *" diff -f "* ]]; then
                  exit 1
                elif [[ "$arguments" == *" apply --dry-run=server "* ]]; then
                  printf 'namespace/openshift-mcp\n'
                  printf 'serviceaccount/opencode-admin-readonly\n'
                  printf 'clusterrole.rbac.authorization.k8s.io/opencode-admin-read-all\n'
                  printf 'clusterrolebinding.rbac.authorization.k8s.io/opencode-admin-read-all\n'
                elif [[ "$arguments" == *" apply -f "* ]]; then
                  printf 'namespace/openshift-mcp configured\n'
                  printf 'serviceaccount/opencode-admin-readonly configured\n'
                  printf 'clusterrole.rbac.authorization.k8s.io/opencode-admin-read-all configured\n'
                  printf 'clusterrolebinding.rbac.authorization.k8s.io/opencode-admin-read-all configured\n'
                elif [[ "$arguments" == *" create token opencode-admin-readonly "* ]]; then
                  printf 'fake-service-account-token\n'
                else
                  printf 'unexpected fake oc arguments: %s\n' "$*" >&2
                  exit 10
                fi
                """
            ),
            encoding="utf-8",
            newline="\n",
        )
        fake_oc.chmod(0o755)
        return fake_bin

    def run_phase(
        self,
        phase: str,
        admin: Path,
        ca: Path,
        output: Path,
        log: Path,
        fake_bin: Path,
        expected_server: str = "https://api.customer.example:6443",
        include_explicit_ca: bool = True,
        fake_insecure_tls: str = "",
    ) -> subprocess.CompletedProcess[str]:
        environment = os.environ.copy()
        environment.update(
            {
                "PATH": f"{bash_path(fake_bin)}:/usr/bin:/bin",
                "FAKE_OC_LOG": bash_path(log),
                "FAKE_CA_PATH": bash_path(ca),
                "FAKE_OUTPUT": bash_path(output),
                "FAKE_ADMIN_KUBECONFIG": bash_path(admin),
                "FAKE_SERVER": "https://api.customer.example:6443",
                "FAKE_ADMIN_IDENTITY": "customer-admin",
                "FAKE_INSECURE_TLS": fake_insecure_tls,
            }
        )
        arguments = [
            self.bash,
            bash_path(SCRIPT),
            phase,
            "--admin-kubeconfig",
            bash_path(admin),
            "--expected-server",
            expected_server,
            "--expected-admin-identity",
            "customer-admin",
            "--output",
            bash_path(output),
        ]
        if include_explicit_ca:
            arguments.extend(["--cluster-ca", bash_path(ca)])
        return subprocess.run(
            arguments,
            cwd=ROOT,
            env=environment,
            text=True,
            capture_output=True,
            check=False,
        )

    def test_three_phases_are_ordered_and_do_not_expose_token(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            directory = Path(temporary)
            admin = directory / "admin.kubeconfig"
            ca = directory / "customer-ca.pem"
            output = directory / "read-all.kubeconfig"
            log = directory / "oc.log"
            admin.write_text("admin placeholder\n", encoding="utf-8")
            ca.write_text(
                "-----BEGIN CERTIFICATE-----\nZmFrZQ==\n-----END CERTIFICATE-----\n",
                encoding="utf-8",
            )
            fake_bin = self.make_fake_oc(directory)

            preview = self.run_phase("preview", admin, ca, output, log, fake_bin)
            self.assertEqual(preview.returncode, 0, preview.stderr)
            self.assertIn("Persistent changes: none", preview.stdout)
            self.assertFalse(output.exists())
            self.assertNotIn("fake-service-account-token", preview.stdout + preview.stderr)

            apply_rbac = self.run_phase(
                "apply-rbac", admin, ca, output, log, fake_bin
            )
            self.assertEqual(apply_rbac.returncode, 0, apply_rbac.stderr)
            self.assertIn("Credential created: no", apply_rbac.stdout)
            self.assertFalse(output.exists())

            create = self.run_phase(
                "create-kubeconfig", admin, ca, output, log, fake_bin
            )
            self.assertEqual(create.returncode, 0, create.stderr)
            self.assertIn("Bootstrap completed: yes", create.stdout)
            self.assertTrue(output.exists())
            self.assertNotIn("fake-service-account-token", create.stdout + create.stderr)
            if os.name != "nt":
                self.assertEqual(stat.S_IMODE(output.stat().st_mode), 0o600)

            calls = log.read_text(encoding="utf-8")
            self.assertIn("--insecure-skip-tls-verify=false", calls)
            self.assertNotIn("--insecure-skip-tls-verify=true", calls)
            self.assertNotIn(" login ", f" {calls} ")
            self.assertEqual(
                calls.count("create token opencode-admin-readonly"), 1
            )

    def test_rejects_insecure_admin_trust_when_copying_ca(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            directory = Path(temporary)
            admin = directory / "admin.kubeconfig"
            ca = directory / "customer-ca.pem"
            output = directory / "read-all.kubeconfig"
            log = directory / "oc.log"
            admin.write_text("admin placeholder\n", encoding="utf-8")
            ca.write_text(
                "-----BEGIN CERTIFICATE-----\nZmFrZQ==\n-----END CERTIFICATE-----\n",
                encoding="utf-8",
            )
            fake_bin = self.make_fake_oc(directory)

            result = self.run_phase(
                "preview",
                admin,
                ca,
                output,
                log,
                fake_bin,
                include_explicit_ca=False,
                fake_insecure_tls="true",
            )
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("disables TLS verification", result.stderr)
            calls = log.read_text(encoding="utf-8")
            self.assertNotIn(" diff -f ", f" {calls} ")
            self.assertNotIn(" apply -f ", f" {calls} ")
            self.assertNotIn(" create token ", f" {calls} ")
            self.assertFalse(output.exists())

    def test_can_copy_the_ca_from_the_admin_kubeconfig(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            directory = Path(temporary)
            admin = directory / "admin.kubeconfig"
            ca = directory / "customer-ca.pem"
            output = directory / "read-all.kubeconfig"
            log = directory / "oc.log"
            admin.write_text("admin placeholder\n", encoding="utf-8")
            ca.write_text(
                "-----BEGIN CERTIFICATE-----\nZmFrZQ==\n-----END CERTIFICATE-----\n",
                encoding="utf-8",
            )
            fake_bin = self.make_fake_oc(directory)

            result = self.run_phase(
                "preview",
                admin,
                ca,
                output,
                log,
                fake_bin,
                include_explicit_ca=False,
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn(
                "Customer CA source: embedded CA from admin kubeconfig",
                result.stdout,
            )
            self.assertFalse(output.exists())

    def test_target_mismatch_stops_before_persistent_action(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            directory = Path(temporary)
            admin = directory / "admin.kubeconfig"
            ca = directory / "customer-ca.pem"
            output = directory / "read-all.kubeconfig"
            log = directory / "oc.log"
            admin.write_text("admin placeholder\n", encoding="utf-8")
            ca.write_text(
                "-----BEGIN CERTIFICATE-----\nZmFrZQ==\n-----END CERTIFICATE-----\n",
                encoding="utf-8",
            )
            fake_bin = self.make_fake_oc(directory)

            result = self.run_phase(
                "apply-rbac",
                admin,
                ca,
                output,
                log,
                fake_bin,
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
