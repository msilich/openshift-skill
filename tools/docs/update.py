#!/usr/bin/env python3
"""Prepare reviewed documentation updates; never change product versions or binaries."""
from __future__ import annotations

import argparse
import copy
import hashlib
import json
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[2]
TOOLS = ROOT / "tools/docs"
SNAPSHOTS = ROOT / ".agents/skills/openshift-docs/references"
PRODUCTS = {
    "ocp": ("build.lock.json", "openshift_docs"),
    "gitops": ("gitops.lock.json", "openshift_gitops_docs"),
    "acs": ("acs.lock.json", "openshift_acs_docs"),
    "devspaces": ("devspaces.lock.json", "devspaces_docs"),
}


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path, value):
    path.write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8")


def run(*command):
    return subprocess.run(list(map(str, command)), check=True, text=True, capture_output=True).stdout


def file_hashes(root):
    return {path.relative_to(root).as_posix(): hashlib.sha256(path.read_bytes()).hexdigest()
            for path in sorted(root.rglob("*")) if path.is_file()}


def require_identical(first, second):
    if file_hashes(first) != file_hashes(second):
        raise RuntimeError("Repeated documentation builds differ; update rejected")


def prepare_git(product, lock, work):
    source = lock["sources"]["openshift_docs"]
    url, branch = source["url"], source["branch_hint"]
    if url != "https://github.com/openshift/openshift-docs" or not re.fullmatch(
        r"(?:enterprise|gitops-docs|rhacs-docs)-\d+\.\d+", branch
    ):
        raise ValueError("Unexpected documentation repository or versioned branch")
    revision = run("git", "ls-remote", "--exit-code", url, "refs/heads/" + branch).split()[0]
    if not re.fullmatch(r"[0-9a-f]{40}", revision):
        raise ValueError("Invalid upstream commit")
    if revision == source["commit"]:
        return None
    checkout = work / "source"
    run("git", "init", checkout)
    run("git", "-C", checkout, "fetch", "--depth=1", url, revision)
    run("git", "-C", checkout, "checkout", "--detach", "FETCH_HEAD")
    candidate = copy.deepcopy(lock)
    candidate["sources"]["openshift_docs"]["commit"] = revision
    candidate_path = work / "candidate.lock.json"
    write_json(candidate_path, candidate)
    first, second = work / "first", work / "second"
    command = (sys.executable, TOOLS / "build.py", "--lock", candidate_path,
               "--source-dir", checkout)
    run(*command, "--output-dir", first, "--refresh-lock")
    run(*command, "--output-dir", second)
    require_identical(first, second)
    return read_json(candidate_path), first, None


def prepare_devspaces(lock, work):
    import import_devspaces as importer
    archive = work / "source.zip"
    importer.fetch(lock, work / "fresh-cache", archive)
    candidate = copy.deepcopy(lock)
    candidate["archive_sha256"] = hashlib.sha256(archive.read_bytes()).hexdigest()
    candidate.pop("expected_output", None)
    first, second = work / "first", work / "second"
    importer.build(candidate, archive, first)
    source = read_json(first / "SOURCE.json")
    candidate["expected_output"] = {
        "topics": source["artifact"]["converted_topics"],
        "content_manifest_sha256": source["integrity"]["content_manifest_sha256"],
    }
    importer.build(candidate, archive, second)
    require_identical(first, second)
    # Retrieval timestamps change on every fetch; retain provenance on content no-ops.
    if candidate["expected_output"] == lock["expected_output"]:
        return None
    return candidate, first, archive


def sync_provenance(updates):
    sources_path = ROOT / "sources.lock.json"
    sources = read_json(sources_path)
    replacements = {}
    for product, old, new, _, _ in updates:
        entry = sources["sources"][PRODUCTS[product][1]]
        if product == "devspaces":
            before, after = old["archive_sha256"], new["archive_sha256"]
            entry["archive_sha256"] = after
        else:
            before = old["sources"]["openshift_docs"]["commit"]
            after = new["sources"]["openshift_docs"]["commit"]
            entry["commit"] = after
        replacements[before] = after
    write_json(sources_path, sources)
    paths = [ROOT / "README.md", ROOT / "THIRD_PARTY_NOTICES.md"]
    paths += list((ROOT / ".agents/skills").glob("*/references/sources.md"))
    for path in paths:
        text = path.read_text(encoding="utf-8")
        changed = re.sub(r"\b(?:[0-9a-f]{64}|[0-9a-f]{40})\b",
                         lambda match: replacements.get(match[0], match[0]), text)
        if changed != text:
            path.write_text(changed, encoding="utf-8")


def update(products, report):
    updates, lines = [], ["# Documentation update", "",
        "Product versions, skill instructions, converter and MCP/runtime baselines remain fixed.",
        "Changed snapshots were built twice; every output file matched. Review the diff and source gaps before merging.", ""]
    with tempfile.TemporaryDirectory(prefix="openshift-docs-update-") as temporary:
        for product in products:
            old = read_json(TOOLS / PRODUCTS[product][0])
            work = Path(temporary) / product
            work.mkdir()
            print(f"Checking {product} {old['document']['version']}", flush=True)
            result = prepare_devspaces(old, work) if product == "devspaces" else prepare_git(product, old, work)
            if result is None:
                lines.append(f"- {product} {old['document']['version']}: unchanged.")
                continue
            new, output, archive = result
            updates.append((product, old, new, output, archive))
            source = read_json(output / "SOURCE.json")
            before = old.get("archive_sha256") or old["sources"]["openshift_docs"]["commit"]
            after = new.get("archive_sha256") or new["sources"]["openshift_docs"]["commit"]
            lines.append(f"- {product} {new['document']['version']}: `{before}` → `{after}`; "
                         f"{source['artifact']['converted_topics']} topics.")
            if product == "acs":
                quality = read_json(output / "CONVERSION.json")
                lines.append(f"  Source gaps: {len(quality['source_issues'])}; fragment adjustments: "
                             f"{len(quality['fragment_adjustments'])}; external references: {len(quality['external_references'])}.")
            elif product == "devspaces":
                lines.append(f"  Link adjustments: {len(source['conversion']['link_adjustments'])}; "
                             f"external references: {len(source['external_references'])}.")
        # Finish all builds before touching the checkout; any failed product aborts the batch.
        for product, old, new, output, archive in updates:
            destination = SNAPSHOTS / f"{product}-{new['document']['version']}"
            if not destination.is_dir() or not (destination / "SOURCE.json").is_file():
                raise RuntimeError(f"Expected existing snapshot is missing: {destination}")
        for product, old, new, output, archive in updates:
            destination = SNAPSHOTS / f"{product}-{new['document']['version']}"
            shutil.rmtree(destination)
            shutil.copytree(output, destination)
            write_json(TOOLS / PRODUCTS[product][0], new)
            if archive:
                shutil.copyfile(archive, TOOLS / old["archive"])
        if updates:
            sync_provenance(updates)
    text = "\n".join(lines) + "\n"
    print(text)
    if report:
        report.write_text(text, encoding="utf-8")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--product", choices=("all", *PRODUCTS), default="all")
    parser.add_argument("--report", type=Path, help="Write the PR body to this Markdown file")
    args = parser.parse_args()
    try:
        if run("git", "-C", ROOT, "status", "--porcelain"):
            raise RuntimeError("Documentation updates require a clean checkout; commit or preserve local changes first")
        update(list(PRODUCTS) if args.product == "all" else [args.product], args.report)
    except subprocess.CalledProcessError as error:
        # Keep converter diagnostics available in Actions when a build is rejected.
        print(error.stdout or "", file=sys.stderr)
        print(error.stderr or "", file=sys.stderr)
        raise


if __name__ == "__main__":
    main()
