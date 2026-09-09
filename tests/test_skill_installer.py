"""Exercise the shell installer in temporary homes, never the real user config."""
import hashlib
import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
NAMES = (
    "openshift-api", "openshift-docs", "openshift-mcp", "openshift-troubleshooting",
    "openshift-disconnected", "openshift-gitops", "openshift-upgrade", "openshift-backup-restore", "openshift-devspaces", "openshift-acs",
)


@unittest.skipIf(os.name == "nt" or (hasattr(os, "geteuid") and os.geteuid() == 0),
                 "requires a non-root POSIX user")
class SkillInstallerTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="skill installer ")
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name)
        self.repo = self.base / "source repo"
        self.repo.mkdir()
        self.script = self.repo / "install-skills.sh"
        shutil.copy2(ROOT / "install-skills.sh", self.script)
        for name in NAMES:
            folder = self.repo / ".agents/skills" / name
            folder.mkdir(parents=True)
            (folder / "SKILL.md").write_text(f"---\nname: {name}\n---\n")
            (folder / "references").mkdir()
            (folder / "references/offline.md").write_text("offline document\n")
        self.user_home = self.base / "user home"
        self.user_home.mkdir()
        self.target = self.user_home / ".config/opencode/skills"
        # Isolate only the child process's environment; never change the login home.
        self.env = {key: value for key, value in os.environ.items()
                    if key not in ("SUDO_USER", "SUDO_UID", "XDG_CONFIG_HOME")}
        self.env["HOME"] = str(self.user_home)

    def run_installer(self, *args, env=None):
        return subprocess.run(["bash", str(self.script), *args], cwd=self.base,
                              env=env or self.env, capture_output=True, text=True, timeout=30)

    def test_dry_run_has_no_persistent_effect(self):
        result = self.run_installer("--dry-run")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn(str(self.target), result.stdout)
        self.assertEqual(list(self.user_home.iterdir()), [])

    def test_installs_all_complete_directories_without_touching_config(self):
        self.target.parent.mkdir(parents=True)
        config = self.target.parent / "opencode.json"
        config.write_text('{"model":"existing"}\n')
        result = self.run_installer()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(sorted(path.name for path in self.target.iterdir()), sorted(NAMES))
        for name in NAMES:
            self.assertEqual((self.target / name / "references/offline.md").read_text(), "offline document\n")
        self.assertEqual(config.read_text(), '{"model":"existing"}\n')
        self.assertFalse(list(self.target.parent.glob(".openshift-skills-install.*")))

    def test_collision_fails_before_installing_any_other_skill(self):
        old = self.target / "openshift-mcp"
        old.mkdir(parents=True)
        (old / "SKILL.md").write_text("custom")
        result = self.run_installer()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("--replace", result.stderr)
        self.assertEqual(list(self.target.iterdir()), [old])
        self.assertEqual((old / "SKILL.md").read_text(), "custom")

    def test_replace_preserves_backup_and_unrelated_skills(self):
        self.assertEqual(self.run_installer().returncode, 0)
        old = self.target / "openshift-docs"
        (old / "custom.md").write_text("local change")
        unrelated = self.target / "other-skill"
        unrelated.mkdir()
        result = self.run_installer("--replace")
        self.assertEqual(result.returncode, 0, result.stderr)
        backups = list(self.target.parent.glob(".openshift-skills-install.*/previous"))
        self.assertEqual(len(backups), 1)
        self.assertEqual((backups[0] / "openshift-docs/custom.md").read_text(), "local change")
        self.assertFalse((old / "custom.md").exists())
        self.assertTrue(unrelated.is_dir())
        self.assertEqual(len(list(backups[0].iterdir())), len(NAMES))

    def test_sudo_is_rejected(self):
        result = self.run_installer(env={**self.env, "SUDO_USER": "somebody"})
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("without sudo", result.stderr)
        self.assertEqual(list(self.user_home.iterdir()), [])

    def test_custom_xdg_requires_an_explicit_target(self):
        env = {**self.env, "XDG_CONFIG_HOME": str(self.base / "custom config")}
        self.assertNotEqual(self.run_installer(env=env).returncode, 0)
        custom = self.base / "custom config/opencode/skills"
        result = self.run_installer("--target-dir", str(custom), env=env)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertTrue((custom / "openshift-docs/references/offline.md").is_file())
        self.assertFalse(self.target.exists())

    def test_bad_paths_and_source_overlap_are_rejected(self):
        source = self.repo / ".agents/skills"
        for path in ("/", "relative", str(source), str(source / "nested"), str(self.repo),
                     str(self.base / ".." / "elsewhere")):
            with self.subTest(path=path):
                result = self.run_installer("--target-dir", path)
                self.assertNotEqual(result.returncode, 0)

    def test_existing_skill_symlink_is_never_followed(self):
        self.target.mkdir(parents=True)
        original = self.base / "original"
        original.mkdir()
        (original / "SKILL.md").write_text("leave unchanged")
        (self.target / "openshift-api").symlink_to(original, target_is_directory=True)
        result = self.run_installer("--replace")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("symlink", result.stderr)
        self.assertEqual((original / "SKILL.md").read_text(), "leave unchanged")

    def test_missing_source_aborts_before_creating_destination(self):
        (self.repo / ".agents/skills/openshift-upgrade/SKILL.md").unlink()
        self.assertNotEqual(self.run_installer().returncode, 0)
        self.assertFalse(self.target.exists())

    def test_real_bundle_is_copied_byte_for_byte(self):
        result = subprocess.run(["bash", str(ROOT / "install-skills.sh")], cwd=self.base,
                                env=self.env, capture_output=True, text=True, timeout=30)
        self.assertEqual(result.returncode, 0, result.stderr)
        for name in NAMES:
            source = ROOT / ".agents/skills" / name
            for original in source.rglob("*"):
                if original.is_file():
                    copied = self.target / name / original.relative_to(source)
                    self.assertTrue(copied.is_file(), copied)
                    self.assertEqual(hashlib.sha256(original.read_bytes()).digest(),
                                     hashlib.sha256(copied.read_bytes()).digest(), copied)

    def test_failed_replacement_restores_previous_directories(self):
        self.assertEqual(self.run_installer().returncode, 0)
        (self.target / "openshift-api/local.md").write_text("keep me")
        fake_bin = self.base / "bin"
        fake_bin.mkdir()
        real_mv = shutil.which("mv")
        fake_mv = fake_bin / "mv"
        fake_mv.write_text('#!/usr/bin/env bash\n'
                           'case "$1" in */payload/openshift-mcp) exit 23 ;; esac\n'
                           f'exec "{real_mv}" "$@"\n')
        fake_mv.chmod(0o755)
        env = {**self.env, "PATH": str(fake_bin) + os.pathsep + self.env["PATH"]}
        result = self.run_installer("--replace", env=env)
        self.assertNotEqual(result.returncode, 0)
        for name in NAMES:
            self.assertTrue((self.target / name / "SKILL.md").exists(), name)
        self.assertEqual((self.target / "openshift-api/local.md").read_text(), "keep me")
        self.assertFalse((self.target.parent / ".openshift-skills-install.lock").exists())

    def test_copy_failure_releases_lock_before_any_skill_is_installed(self):
        fake_bin = self.base / "bin"
        fake_bin.mkdir()
        fake_cp = fake_bin / "cp"
        fake_cp.write_text("#!/usr/bin/env bash\nexit 24\n")
        fake_cp.chmod(0o755)
        env = {**self.env, "PATH": str(fake_bin) + os.pathsep + self.env["PATH"]}
        result = self.run_installer(env=env)
        self.assertEqual(result.returncode, 24, result.stderr)
        self.assertFalse(self.target.exists())
        self.assertFalse((self.target.parent / ".openshift-skills-install.lock").exists())
        self.assertIn("Recovery files retained", result.stderr)


if __name__ == "__main__":
    unittest.main()
