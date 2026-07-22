from __future__ import annotations

import json
import os
from pathlib import Path
import subprocess
import tempfile
import textwrap
import unittest


ROOT = Path(__file__).resolve().parents[2]
SKILL = ROOT / ".agents" / "skills" / "openshift-api" / "SKILL.md"
COLLECTOR = SKILL.parent / "scripts" / "collect-discovery.sh"


class DiscoveryHarnessTest(unittest.TestCase):
    def make_fake_oc(self, directory: Path) -> Path:
        fake = directory / "oc"
        fake.write_text(
            textwrap.dedent(
                """\
                #!/usr/bin/env python3
                import json
                import os
                from pathlib import Path
                import sys

                raw_args = sys.argv[1:]
                with Path(os.environ["FAKE_OC_LOG"]).open("a", encoding="utf-8") as stream:
                    stream.write(json.dumps(raw_args) + "\\n")

                if raw_args[:1] != ["--kubeconfig"] or len(raw_args) < 3:
                    print("fake oc requires an explicit kubeconfig", file=sys.stderr)
                    raise SystemExit(23)
                args = raw_args[2:]

                failures = [item for item in os.environ.get("FAKE_OC_FAIL", "").split("|") if item]
                if any(" ".join(args).startswith(failure) for failure in failures):
                    print("fake failure", file=sys.stderr)
                    raise SystemExit(17)

                if args[:1] == ["api-resources"]:
                    print("widgets  wd  example.io/v1  true  Widget  get,list")
                elif args == ["api-versions"]:
                    print("example.io/v1")
                elif args[:1] == ["explain"]:
                    print("KIND: Widget\\nVERSION: example.io/v1\\nFIELDS: spec")
                elif args == ["get", "--raw", "/openapi/v3"]:
                    print('{"paths":{"apis/example.io/v1":{"serverRelativeURL":"/openapi/v3/apis/example.io/v1?hash=fake"}}}')
                elif args == ["get", "--raw", "/openapi/v3/apis/example.io/v1?hash=fake"]:
                    print('{"components":{"schemas":{"io.example.v1.Widget":{"type":"object"}}}}')
                elif args[:2] == ["get", "crd"]:
                    print('{"spec":{"versions":[{"name":"v1","schema":{"openAPIV3Schema":{"type":"object"}}}]}}')
                else:
                    print("unexpected fake oc arguments", file=sys.stderr)
                    raise SystemExit(19)
                """
            ),
            encoding="utf-8",
        )
        fake.chmod(0o755)
        return fake

    def run_collector(self, *args: str, fail: str = "") -> tuple[subprocess.CompletedProcess[str], list[list[str]]]:
        with tempfile.TemporaryDirectory() as temp:
            directory = Path(temp)
            fake_oc = self.make_fake_oc(directory)
            log = directory / "calls.jsonl"
            env = os.environ.copy()
            env.update({"OC_BIN": str(fake_oc), "FAKE_OC_LOG": str(log), "FAKE_OC_FAIL": fail})
            result = subprocess.run(
                ["bash", str(COLLECTOR), "--kubeconfig", str(directory / "kubeconfig"), *args],
                check=False,
                capture_output=True,
                text=True,
                env=env,
            )
            calls = [json.loads(line) for line in log.read_text(encoding="utf-8").splitlines()]
            return result, calls

    def commands_without_kubeconfig(self, calls: list[list[str]]) -> list[list[str]]:
        for call in calls:
            self.assertEqual(call[0], "--kubeconfig")
            self.assertTrue(call[1].endswith("/kubeconfig"))
        return [call[2:] for call in calls]

    def test_calls_fake_oc_in_fixed_order_and_cites_commands(self) -> None:
        result, calls = self.run_collector(
            "--resource",
            "widgets.example.io",
            "--api-version",
            "example.io/v1",
            "--field",
            "spec",
            "--crd",
            "widgets.example.io",
        )

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(
            self.commands_without_kubeconfig(calls),
            [
                ["api-resources", "-o", "wide"],
                ["api-versions"],
                ["explain", "widgets.example.io", "--api-version=example.io/v1"],
                ["explain", "widgets.example.io.spec", "--api-version=example.io/v1", "--recursive"],
                ["get", "--raw", "/openapi/v3"],
                ["get", "--raw", "/openapi/v3/apis/example.io/v1?hash=fake"],
                ["get", "crd", "widgets.example.io", "-o", "json"],
            ],
        )
        self.assertEqual(result.stdout.count("Source command: oc"), len(calls))
        self.assertIn("Cite the exact successful source command", result.stdout)

    def test_required_discovery_failure_stops_immediately(self) -> None:
        result, calls = self.run_collector(
            "--resource",
            "widgets.example.io",
            "--api-version",
            "example.io/v1",
            fail="api-resources",
        )

        self.assertEqual(result.returncode, 1)
        self.assertEqual(self.commands_without_kubeconfig(calls), [["api-resources", "-o", "wide"]])
        self.assertIn("Do not infer API data", result.stderr)

    def test_missing_field_schema_fails_closed_after_fallbacks(self) -> None:
        result, calls = self.run_collector(
            "--resource",
            "widgets.example.io",
            "--api-version",
            "example.io/v1",
            fail="explain|get --raw /openapi/v3/apis/example.io/v1?hash=fake",
        )

        self.assertEqual(result.returncode, 2)
        self.assertEqual(
            self.commands_without_kubeconfig(calls)[-1],
            ["get", "--raw", "/openapi/v3/apis/example.io/v1?hash=fake"],
        )
        self.assertIn("Never invent schema", result.stderr)

    def test_skill_declares_order_and_evidence_policy(self) -> None:
        text = SKILL.read_text(encoding="utf-8")
        markers = [
            "oc api-resources -o wide",
            "oc api-versions",
            "oc explain <resource> --api-version=<group/version>",
            "oc explain <resource>.<field> --api-version=<group/version> --recursive",
            "--recursive",
            "oc get --raw /openapi/v3",
            "oc get crd <plural>.<group> -o json",
        ]
        positions = [text.index(marker) for marker in markers]
        self.assertEqual(positions, sorted(positions))
        self.assertIn("Never invent", text)
        self.assertIn("Cite the exact successful command", text)


if __name__ == "__main__":
    unittest.main()
