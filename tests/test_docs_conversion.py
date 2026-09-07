"""Regression checks for version attributes in the offline docs build."""

from __future__ import annotations

import importlib.util
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


@unittest.skipUnless(importlib.util.find_spec("yaml"), "requires build dependency PyYAML")
class DocumentationVersionTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        spec = importlib.util.spec_from_file_location(
            "docs_converter", ROOT / "tools" / "docs" / "convert.py"
        )
        cls.converter = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(cls.converter)

    def test_explicit_branch_overrides_missing_distro_map_entry(self) -> None:
        stale_map = {
            "openshift-enterprise": {
                "name": "OpenShift Container Platform",
                "branches": {"enterprise-4.1": {"name": "4.1"}},
            }
        }
        attributes = self.converter.get_distro_attributes(
            stale_map, "openshift-enterprise", "enterprise-4.20"
        )
        self.assertEqual(attributes["product-version"], "4.20")

    def test_unknown_version_is_rejected(self) -> None:
        with self.assertRaises(ValueError):
            self.converter.get_distro_attributes({}, "openshift-enterprise", "main")

    def test_conflicting_distro_map_is_rejected(self) -> None:
        conflicting_map = {
            "openshift-enterprise": {
                "branches": {"enterprise-4.20": {"name": "4.19"}}
            }
        }
        with self.assertRaises(ValueError):
            self.converter.get_distro_attributes(
                conflicting_map, "openshift-enterprise", "enterprise-4.20"
            )


if __name__ == "__main__":
    unittest.main()
