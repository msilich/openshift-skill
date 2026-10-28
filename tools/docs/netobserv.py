"""Bundle pinned Network Observability references without build-time downloads."""
from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import tempfile

from acs import pandoc, render_topic, signature
from convert import sanitize_docbook_xml

SOURCES = Path(__file__).resolve().parent / "netobserv"
CATALOG = "observability/network_observability/network-observability-api-reference.md"
PREFIX = "offline-references/netobserv"
NOTICE = "<!-- Modified: bundled offline; AsciiDoc converted to Markdown. See ../SOURCE.json for provenance. -->\n\n"


def safe_path(root: Path, name: str) -> Path:
    path = (root / name).resolve()
    if not path.is_relative_to(root.resolve()) or path == root.resolve():
        raise RuntimeError(f"escaping offline reference path: {name}")
    return path


def load_sources(expected: str) -> dict:
    data = (SOURCES / "manifest.json").read_bytes()
    if hashlib.sha256(data).hexdigest() != expected:
        raise RuntimeError("Network Observability manifest checksum mismatch")
    manifest = json.loads(data)
    for document in manifest["documents"].values():
        if document["source"] not in manifest["files"]:
            raise RuntimeError("offline reference source is not checksummed")
    for name, digest in manifest["files"].items():
        if hashlib.sha256(safe_path(SOURCES, name).read_bytes()).hexdigest() != digest:
            raise RuntimeError(f"offline reference checksum mismatch: {name}")
    return manifest


def finish_snapshot(root: Path, expected: str) -> int:
    manifest = load_sources(expected)
    catalog = root / CATALOG
    if not catalog.is_file():
        raise RuntimeError("Network Observability API catalog missing; review offline coverage")
    text = catalog.read_text()
    links = re.findall(r"https://github\.com/(?:openshift/network-observability-operator|netobserv/netobserv-cli)/blob/[^\s)<>\"]+", text)
    unknown = set(links) - manifest["documents"].keys()
    if unknown:
        raise RuntimeError(f"unbundled Network Observability reference: {sorted(unknown)}")

    destination = root / PREFIX
    destination.mkdir(parents=True, exist_ok=True)
    quality = {}
    for version in manifest["sources"]:
        target = safe_path(destination, version + "/LICENSE")
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(safe_path(SOURCES, version + "/LICENSE"), target)
    with tempfile.TemporaryDirectory(prefix="netobserv-render-") as temporary:
        xml = Path(temporary) / "reference.xml"
        for url, document in manifest["documents"].items():
            source = safe_path(SOURCES, document["source"])
            target = safe_path(destination, document["output"])
            target.parent.mkdir(parents=True, exist_ok=True)
            adjustments = []
            if source.suffix == ".adoc":
                source_text = source.read_text()
                if document["source"] == "cli/docs/netobserv_cli.adoc":
                    # Upstream omits a table separator, shifting every later row.
                    source_text, count = re.subn(
                        r"^(\|--tls-keylog\|[^\n|]+?) +(collector setting)$",
                        r"\1 | \2", source_text, flags=re.MULTILINE,
                    )
                    if count != 1:
                        raise RuntimeError("CLI table correction no longer matches pinned source")
                    adjustments.append("Inserted the missing Default-cell separator in the --tls-keylog row; unmodified source is retained and checksummed.")
                result = subprocess.run([
                    "asciidoctor", "-b", "docbook5", "--safe-mode", "secure",
                    "-a", "reproducible", "-a", "context=offline-reference",
                    "-o", "-", "-",
                ], input=source_text, check=True, text=True, capture_output=True)
                if result.stderr.strip():
                    raise RuntimeError(f"offline reference conversion warning: {result.stderr}")
                xml.write_text(result.stdout)
                sanitize_docbook_xml(str(xml))
                # Reuse the existing anchor-preserving renderer and code/table checks.
                render_topic(xml, target, "", SOURCES)
                report = target.with_suffix(".quality.json")
                quality[document["output"]] = json.loads(report.read_text())
                quality[document["output"]]["source_adjustments"] = adjustments
                report.unlink()
            else:
                shutil.copyfile(source, target)
                codes, tables = signature(json.loads(pandoc(pandoc(source.read_text(), "gfm", "html"), "html", "json")))
                quality[document["output"]] = {
                    "code_blocks": len(codes), "tables": len(tables),
                    "code_sha256": hashlib.sha256(json.dumps(codes).encode()).hexdigest(),
                    "table_text_sha256": hashlib.sha256(json.dumps(tables).encode()).hexdigest(),
                }
            version = document["source"].split("/", 1)[0]
            origin = manifest["sources"][version]
            pinned = url.replace("/blob/" + origin["branch"] + "/", "/blob/" + origin["commit"] + "/")
            target.write_text(NOTICE + f"> Source: [{version} at {origin['commit']}]({pinned}). Match the installed Operator/CLI version; OCP does not select it.\n\n" + target.read_text())

    mapping = {url: destination / row["output"] for url, row in manifest["documents"].items()}
    for document in root.rglob("*.md"):
        content = document.read_text()
        rewritten = content
        for url, target in mapping.items():
            rewritten = rewritten.replace(url, os.path.relpath(target, document.parent).replace(os.sep, "/"))
        if rewritten != content:
            document.write_text(rewritten)
    navigation = "\n## Bundled Network Observability references\n\nMatch the installed Operator/CLI version, not the OCP version. Sources and licenses are pinned in `offline-references/netobserv/SOURCE.json`.\n\n"
    navigation += "".join(f"- [{row['output']}]({PREFIX}/{row['output']})\n" for row in manifest["documents"].values())
    for name in ("index.md", "AGENTS.md"):
        path = root / name
        path.write_text(path.read_text() + navigation)
    files = {p.relative_to(destination).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
             for p in sorted(destination.rglob("*")) if p.is_file()}
    external = sorted({url for p in destination.rglob("*.md")
                       for url in re.findall(r"https?://[^\s<>\"')]+", p.read_text())})
    (destination / "SOURCE.json").write_text(json.dumps({
        "sources": manifest["sources"], "source_files": manifest["files"],
        "manifest_sha256": expected, "documents": manifest["documents"],
        "conversion": quality, "files": files, "external_references": external,
        "build_tools": {"asciidoctor": "2.0.23", "pandoc": "3.7.0.2"},
        "scope": "Nine directly linked API/flow-format/CLI references; further external citations are inventoried, not fetched.",
        "runtime_network_required": False,
    }, indent=2, sort_keys=True) + "\n")
    return len(manifest["documents"])
