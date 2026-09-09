#!/usr/bin/env python3
"""Rebuild a pinned, Markdown-only OpenShift product documentation snapshot."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import platform
import re
import shutil
import subprocess
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path

import yaml
from convert import get_distro_attributes, parse_distro_map


TOOLS_DIR = Path(__file__).resolve().parent
LOCK_PATH = TOOLS_DIR / "build.lock.json"
CONVERTER_PATH = TOOLS_DIR / "convert.py"
CONVERTER_LICENSE_PATH = TOOLS_DIR / "LICENSE.agentic-skills"
MODIFICATION_NOTICE = (
    "<!-- Format modified: converted from AsciiDoc to Markdown. "
    "See SOURCE.json for provenance. -->\n\n"
)


def run(command: list[str], **kwargs: object) -> subprocess.CompletedProcess[str]:
    return subprocess.run(command, check=True, text=True, **kwargs)


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def markdown_manifest(root: Path) -> tuple[int, str]:
    entries: list[str] = []
    for document in sorted(root.rglob("*.md")):
        relative = document.relative_to(root).as_posix()
        entries.append(f"{sha256_file(document)}  {relative}\n")
    manifest = "".join(entries).encode("utf-8")
    return len(entries), hashlib.sha256(manifest).hexdigest()


def verify_tool_versions(lock: dict[str, object]) -> dict[str, str]:
    dependencies = lock["dependencies"]
    assert isinstance(dependencies, dict)

    expected_python = str(dependencies["python_minimum"])
    if tuple(sys.version_info[:2]) < tuple(map(int, expected_python.split("."))):
        raise RuntimeError(f"Python {expected_python} or newer is required")

    expected_yaml = str(dependencies["pyyaml"])
    if yaml.__version__ != expected_yaml:
        raise RuntimeError(f"PyYAML {expected_yaml} is required; found {yaml.__version__}")

    asciidoctor_line = run(
        ["asciidoctor", "--version"], capture_output=True
    ).stdout.splitlines()[0]
    pandoc_line = run(["pandoc", "--version"], capture_output=True).stdout.splitlines()[0]

    expected_asciidoctor = str(dependencies["asciidoctor"])
    expected_pandoc = str(dependencies["pandoc"])
    if not asciidoctor_line.startswith(f"Asciidoctor {expected_asciidoctor} "):
        raise RuntimeError(
            f"Asciidoctor {expected_asciidoctor} is required; found {asciidoctor_line}"
        )
    if pandoc_line != f"pandoc {expected_pandoc}":
        raise RuntimeError(f"Pandoc {expected_pandoc} is required; found {pandoc_line}")

    return {
        "python": platform.python_version(),
        "pyyaml": yaml.__version__,
        "asciidoctor": expected_asciidoctor,
        "pandoc": expected_pandoc,
    }


def verify_source(source_dir: Path, lock: dict[str, object]) -> str:
    source = lock["sources"]["openshift_docs"]
    assert isinstance(source, dict)
    revision = run(
        ["git", "-C", str(source_dir), "rev-parse", "HEAD"], capture_output=True
    ).stdout.strip()
    expected = str(source["commit"])
    if revision != expected:
        raise RuntimeError(f"openshift-docs must be at {expected}; found {revision}")

    status = run(
        ["git", "-C", str(source_dir), "status", "--porcelain"], capture_output=True
    ).stdout
    if status:
        raise RuntimeError("openshift-docs checkout has local changes")
    return run(
        ["git", "-C", str(source_dir), "show", "-s", "--format=%cI", "HEAD"],
        capture_output=True,
    ).stdout.strip()


def verify_converter(lock: dict[str, object]) -> None:
    converter = lock["sources"]["agentic_skills_converter"]
    assert isinstance(converter, dict)
    actual = sha256_file(CONVERTER_PATH)
    expected = str(converter["sha256"])
    if actual != expected:
        raise RuntimeError(f"converter checksum mismatch: expected {expected}; found {actual}")
    for filename, expected in lock.get("local_build_helpers", {}).items():
        path = (TOOLS_DIR / filename).resolve()
        if path.parent != TOOLS_DIR or sha256_file(path) != expected:
            raise RuntimeError(f"build helper checksum mismatch: {filename}")


def document_definition(lock: dict) -> dict:
    document = lock.get("document", {})
    for field in ("product", "version", "distro", "branch"):
        if not isinstance(document.get(field), str) or not document[field].strip():
            raise RuntimeError(f"lock document.{field} is required")
    if not re.fullmatch(r"\d+\.\d+", document["version"]):
        raise RuntimeError("lock document.version must be an explicit major.minor version")
    if document["branch"] != lock["sources"]["openshift_docs"]["branch_hint"]:
        raise RuntimeError("document branch and source branch_hint disagree")
    return document


def post_process(output_dir: Path, product: str = "OpenShift Container Platform") -> None:
    output_dir = output_dir.resolve()
    for html_file in (output_dir / "index.html", output_dir / "viewer.html"):
        html_file.unlink(missing_ok=True)

    index_path = output_dir / "index.md"
    index_text = index_path.read_text(encoding="utf-8")
    old = "> Designed for AI agent consumption. Updated weekly."
    new = (
        "> Designed for offline AI-agent retrieval. "
        "Pinned to the source revision recorded in SOURCE.json."
    )
    if old in index_text:
        index_path.write_text(index_text.replace(old, new, 1), encoding="utf-8")
    elif new not in index_text:
        raise RuntimeError("expected generated update marker is missing from index.md")

    if product != "OpenShift Container Platform":
        for navigation in (index_path, output_dir / "AGENTS.md"):
            content = navigation.read_text(encoding="utf-8")
            navigation.write_text(content.replace(
                "# OpenShift Container Platform Documentation", f"# {product} Documentation", 1
            ), encoding="utf-8")

    for document in sorted(output_dir.rglob("*.md")):
        content = document.read_text(encoding="utf-8")
        if not content.startswith(MODIFICATION_NOTICE):
            document.write_text(MODIFICATION_NOTICE + content, encoding="utf-8")

    documents_by_name: dict[str, list[Path]] = {}
    for document in sorted(output_dir.rglob("*.md")):
        documents_by_name.setdefault(document.name, []).append(document)

    cross_reference = re.compile(
        r"\]\((?P<target>[^)\s]+?)\.xml(?P<fragment>#[^)]*)?\)"
    )
    for document in sorted(output_dir.rglob("*.md")):
        content = document.read_text(encoding="utf-8")

        def rewrite(match: re.Match[str]) -> str:
            target = match.group("target")
            if "://" in target or target.startswith("/"):
                return match.group(0)
            candidate = (document.parent / f"{target}.md").resolve()
            try:
                candidate.relative_to(output_dir)
            except ValueError:
                candidate = Path()
            if not candidate.is_file():
                alternatives = documents_by_name.get(f"{Path(target).name}.md", [])
                if len(alternatives) != 1:
                    return match.group(0)
                candidate = alternatives[0]
            relative = os.path.relpath(candidate, document.parent).replace(os.sep, "/")
            return f"]({relative}{match.group('fragment') or ''})"

        rewritten = cross_reference.sub(rewrite, content)
        if rewritten != content:
            document.write_text(rewritten, encoding="utf-8")


def verify_local_links(root: Path) -> int:
    root = root.resolve()
    checked = 0
    for document in root.rglob("*.md"):
        for target in re.findall(r"\[[^]]*\]\(([^)]+)\)", document.read_text(encoding="utf-8")):
            path = target.split("#", 1)[0]
            if not path or "://" in path or not path.endswith(".md"):
                continue
            resolved = (document.parent / path).resolve()
            if not resolved.is_relative_to(root) or not resolved.is_file():
                raise RuntimeError(f"broken or escaping local link: {document.relative_to(root)} -> {target}")
            checked += 1
    return checked


def write_source_metadata(
    output_dir: Path,
    lock: dict[str, object],
    tool_versions: dict[str, str],
    source_commit_time: str,
    topics: int,
    markdown_files: int,
    manifest_sha256: str,
) -> None:
    source_time = datetime.fromisoformat(source_commit_time).astimezone(timezone.utc)
    sources = lock["sources"]
    definition = document_definition(lock)
    metadata = {
        "schema_version": 1,
        "artifact": {
            "product": definition["product"],
            "version": definition["version"],
            "format": "GitHub-Flavored Markdown",
            "scope": f"Complete {definition['distro']} topic map at the pinned revision",
            "markdown_files": markdown_files,
            "converted_topics": topics,
        },
        "sources": sources,
        "conversion": {
            "arguments": {
                "distro": definition["distro"],
                "branch": definition["branch"],
                "product-version": definition["version"],
                "topics": "all",
            },
            "successful_topics": topics,
            "failed_topics": 0,
            "modifications": [
                f"Resolved product-version={definition['version']} from the explicit {definition['branch']} branch because the source distro map is stale.",
                "Converted the source AsciiDoc files to GitHub-Flavored Markdown.",
                "Removed the generated HTML index and CDN-dependent viewer.",
                "Replaced the rolling weekly-update statement with pinned-snapshot provenance.",
                "Added a format-modification notice to every Markdown file.",
                "Rewrote DocBook .xml cross-references to bundled Markdown targets.",
                "Verified local Markdown links; set navigation titles to the selected product.",
            ],
            "build_tools": tool_versions,
        },
        "integrity": {
            "algorithm": "sha256",
            "markdown_manifest_algorithm": (
                "SHA-256 of sorted UTF-8 lines: '<file-sha256>  <relative-path>\\n'"
            ),
            "markdown_manifest_sha256": manifest_sha256,
            "openshift_docs_license_sha256": sha256_file(
                output_dir / "LICENSE.openshift-docs"
            ),
            "agentic_skills_license_sha256": sha256_file(
                output_dir / "LICENSE.agentic-skills"
            ),
        },
        "source_commit_time_utc": source_time.isoformat().replace("+00:00", "Z"),
        "runtime_network_required": False,
    }
    (output_dir / "SOURCE.json").write_text(
        json.dumps(metadata, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )


def replace_output(staged: Path, output_dir: Path, definition: dict) -> None:
    if output_dir.exists():
        marker = output_dir / "SOURCE.json"
        if not marker.is_file():
            raise RuntimeError(
                f"refusing to replace unrecognized output directory without SOURCE.json: {output_dir}"
            )
        existing = json.loads(marker.read_text(encoding="utf-8"))
        if any(existing.get("artifact", {}).get(key) != definition[key] for key in ("product", "version")):
            raise RuntimeError(f"refusing to replace a different product/version: {output_dir}")
        shutil.rmtree(output_dir)
    os.replace(staged, output_dir)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--lock", type=Path, default=LOCK_PATH, help="Build definition (default: OCP build.lock.json)")
    parser.add_argument("--source-dir", required=True, type=Path)
    parser.add_argument("--output-dir", required=True, type=Path)
    parser.add_argument("--workers", type=int, default=4)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    source_dir = args.source_dir.resolve()
    output_dir = args.output_dir.resolve()
    if args.workers < 1:
        raise RuntimeError("--workers must be at least 1")
    if output_dir == Path("/") or output_dir == Path.home() or output_dir == source_dir:
        raise RuntimeError(f"unsafe output directory: {output_dir}")

    lock = json.loads(args.lock.read_text(encoding="utf-8"))
    definition = document_definition(lock)
    source_commit_time = verify_source(source_dir, lock)
    verify_converter(lock)
    tool_versions = verify_tool_versions(lock)
    attributes = get_distro_attributes(parse_distro_map(str(source_dir)), definition["distro"], definition["branch"])
    if attributes["product-version"] != definition["version"] or attributes["product-title"] != definition["product"]:
        raise RuntimeError("source product/version attributes disagree with the build definition")

    output_dir.parent.mkdir(parents=True, exist_ok=True)
    staging_root = Path(tempfile.mkdtemp(prefix="docs-build-", dir=output_dir.parent))
    staged_output = staging_root / "snapshot"
    try:
        process = run(
            [
                sys.executable,
                str(CONVERTER_PATH),
                "--source-dir",
                str(source_dir),
                "--output-dir",
                str(staged_output),
                "--distro",
                definition["distro"],
                "--branch",
                definition["branch"],
                "--workers",
                str(args.workers),
            ],
            capture_output=True,
        )
        print(process.stdout, end="")
        summary = re.search(
            r"Conversion complete: (\d+) succeeded, (\d+) failed", process.stdout
        )
        if not summary:
            raise RuntimeError("converter did not emit a conversion summary")
        successful_topics, failed_topics = map(int, summary.groups())
        expected_topics = int(lock["expected_output"]["converted_topics"])
        if failed_topics or successful_topics != expected_topics:
            raise RuntimeError(
                f"unexpected conversion result: {successful_topics} succeeded, "
                f"{failed_topics} failed; expected {expected_topics} succeeded"
            )

        post_process(staged_output, definition["product"])
        if definition["distro"] == "openshift-acs":
            from acs import finish_snapshot
            finish_snapshot(staged_output, source_dir)
        print(f"Verified {verify_local_links(staged_output)} local Markdown links")
        shutil.copy2(source_dir / "LICENSE", staged_output / "LICENSE.openshift-docs")
        shutil.copy2(CONVERTER_LICENSE_PATH, staged_output / "LICENSE.agentic-skills")
        markdown_files, manifest_sha256 = markdown_manifest(staged_output)

        expected_files = int(lock["expected_output"]["markdown_files"])
        expected_manifest = str(lock["expected_output"]["markdown_manifest_sha256"])
        if markdown_files != expected_files:
            raise RuntimeError(
                f"generated {markdown_files} Markdown files; expected {expected_files}"
            )
        if manifest_sha256 != expected_manifest:
            raise RuntimeError(
                "generated Markdown manifest does not match build.lock.json: "
                f"expected {expected_manifest}; found {manifest_sha256}"
            )

        write_source_metadata(
            staged_output,
            lock,
            tool_versions,
            source_commit_time,
            successful_topics,
            markdown_files,
            manifest_sha256,
        )
        if definition["distro"] == "openshift-acs":
            metadata_path = staged_output / "SOURCE.json"
            metadata = json.loads(metadata_path.read_text())
            metadata["conversion"]["quality_report"] = "CONVERSION.json"
            metadata["conversion"]["local_build_helpers"] = lock["local_build_helpers"]
            metadata["integrity"]["asset_manifest"] = json.loads((staged_output / "CONVERSION.json").read_text())["image_sha256"]
            metadata["integrity"]["conversion_report_sha256"] = sha256_file(staged_output / "CONVERSION.json")
            metadata["conversion"]["modifications"].append("RHACS-only: retain explicit anchors, verify code/table round trips, bundle images and record missing source links/fragments and external references in CONVERSION.json.")
            metadata_path.write_text(json.dumps(metadata, indent=2, sort_keys=True) + "\n")
        replace_output(staged_output, output_dir, definition)
    finally:
        shutil.rmtree(staging_root, ignore_errors=True)

    print(f"Pinned {definition['product']} {definition['version']} documentation written to {output_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
