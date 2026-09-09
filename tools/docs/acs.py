"""RHACS-only conversion quality checks; no network access.

Keep this product-specific path separate so older snapshots remain byte-identical.
"""
from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
from urllib.parse import unquote, urlsplit


def pandoc(source: str, reader: str, writer: str) -> str:
    return subprocess.run(["pandoc", "-f", reader, "-t", writer, "--wrap=none"],
                          input=source, text=True, capture_output=True, check=True).stdout


def nodes(value):
    if isinstance(value, dict):
        if "t" in value:
            yield value
        for child in value.values():
            yield from nodes(child)
    elif isinstance(value, list):
        for child in value:
            yield from nodes(child)


def signature(tree):
    codes = [n["c"][1] for n in nodes(tree) if n["t"] == "CodeBlock"]
    # Compare table cell text, not Pandoc's layout/alignment representation.
    tables = []
    for table in (n for n in nodes(tree) if n["t"] == "Table"):
        words = [n["c"] if n["t"] == "Str" else n["c"][1]
                 for n in nodes(table["c"][2:]) if n["t"] in ("Str", "Code")]
        tables.append(" ".join(words))
    return codes, tables


def redact_examples(text):
    """Do not redistribute credential-shaped webhook examples from vendor docs."""
    return re.subn(r"https://hooks\.slack\.com/services/[A-Za-z0-9/_-]+",
                   "https://hooks.slack.com/services/REPLACE_WORKSPACE/REPLACE_CHANNEL/REPLACE_TOKEN", text)


def render_topic(xml: Path, target: Path, warnings: str, source: Path):
    xml_text, redactions = redact_examples(xml.read_text())
    tree = json.loads(pandoc(xml_text, "docbook", "json"))
    before = signature(tree)
    blocks = []
    anchors = []
    for block in tree["blocks"]:
        if block["t"] == "Header" and block["c"][1][0]:
            anchor = block["c"][1][0]
            anchors.append(anchor)
            blocks.append({"t": "RawBlock", "c": ["html", f'<a id="{anchor}"></a>']})
        blocks.append(block)
    tree["blocks"] = blocks
    content = pandoc(json.dumps(tree), "json", "gfm")
    # Pandoc 3.7 can emit unescaped pipes inside inline code in pipe tables,
    # causing cells after flags such as false|true|auto to be lost by GFM.
    content = "\n".join(
        re.sub(r"(?<!\\)`+[^`\n]*(?<!\\)`+", lambda m: re.sub(r"(?<!\\)\|", r"\\|", m[0]), line)
        if line.startswith("|") else line for line in content.split("\n")
    )
    # GFM retains complex tables as HTML; parse the rendered HTML to check both
    # pipe tables and spanning/multi-paragraph cells rather than dropping them.
    after = signature(json.loads(pandoc(pandoc(content, "gfm", "html"), "html", "json")))
    if before != after:
        raise RuntimeError(f"RHACS code/table round-trip changed content: {target}")
    if redactions:
        content = ("<!-- Security modification: credential-shaped Slack webhook examples "
                   "replaced with placeholders. No endpoint was contacted. -->\n\n" + content)
    target.write_text(content)
    target.with_suffix(".quality.json").write_text(json.dumps({
        "code_blocks": len(before[0]), "tables": len(before[1]),
        "code_sha256": hashlib.sha256(json.dumps(before[0]).encode()).hexdigest(),
        "table_text_sha256": hashlib.sha256(json.dumps(before[1]).encode()).hexdigest(),
        "anchors": anchors,
        "redacted_webhook_examples": redactions,
        "source_warnings": warnings.replace(str(source), "<source>").strip().splitlines(),
    }, indent=2, sort_keys=True) + "\n")


def finish_snapshot(root: Path, source: Path):
    """Bundle images and inventory all links, retaining explicit source gaps."""
    root = root.resolve()
    docs = sorted(root.rglob("*.md"))
    quality = {}
    for path in sorted(root.rglob("*.quality.json")):
        quality[path.relative_to(root).as_posix().replace(".quality.json", ".md")] = json.loads(path.read_text())
    from convert import collect_topics, parse_topic_map, should_include_topic
    expected = []
    for group in parse_topic_map(str(source)):
        if group and should_include_topic(group, "openshift-acs"):
            expected.extend(collect_topics(group.get("Topics", []), group.get("Dir", ""), "openshift-acs"))
    expected_paths = sorted(str(Path(topic["source"]).with_suffix(".md")) for topic in expected)
    if sorted(quality) != expected_paths:
        raise RuntimeError("RHACS quality inventory does not cover the complete topic map")
    shutil.copyfile(source / "_topic_maps/_topic_map.yml", root / "TOPIC_MAP.yml")
    anchors = {}
    for path in docs:
        anchors[path] = set(re.findall(r'<a id="([^"]+)"', path.read_text()))
    issues, external, adjustments, assets = [], set(), [], {}
    link_re = re.compile(r'(!?\[[^\]\n]*\])\(([^\s)]+)(?:\s+"[^"\n]*")?\)')
    for path in docs:
        relative = path.relative_to(root).as_posix()

        def rewrite(match):
            label, target = match.groups()
            parts = urlsplit(target)
            if parts.scheme or target.startswith("//"):
                external.add(target)
                return match.group(0)
            local = unquote(parts.path)
            if local.endswith((".xml", ".html")):
                candidate = (path.parent / str(Path(local).with_suffix(".md"))).resolve()
                if not candidate.is_file():
                    candidates = list(root.rglob(Path(local).stem + ".md"))
                    if len(candidates) == 1:
                        candidate = candidates[0]
                if candidate.is_relative_to(root) and candidate.is_file():
                    local = os.path.relpath(candidate, path.parent)
            if label.startswith("!"):
                # The source uses :imagesdir: images, relative to the publication root.
                image_name = local.removeprefix("images/")
                origin = (source / "images" / image_name).resolve()
                if not origin.is_relative_to((source / "images").resolve()) or not origin.is_file():
                    raise RuntimeError(f"Missing RHACS illustration: {relative} -> {target}")
                dest = root / "images" / image_name
                dest.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(origin, dest)
                assets[dest.relative_to(root).as_posix()] = hashlib.sha256(dest.read_bytes()).hexdigest()
                return f"{label}({os.path.relpath(dest, path.parent)})"
            resolved = (path.parent / local).resolve() if local else path
            if local and (not resolved.is_relative_to(root) or not resolved.is_file()):
                issues.append({"document": relative, "target": target, "kind": "missing-source-target"})
                return f"{label[1:-1]} (unavailable upstream reference: `{target}`)"
            if parts.fragment and unquote(parts.fragment) not in anchors.get(resolved, set()):
                # Navigation index links can use automatic GFM headings; retain only explicit source IDs here.
                adjustments.append({"document": relative, "target": target, "kind": "unresolved-output-fragment"})
                if local:
                    return f"{label}({local})"
                return label[1:-1] + f" (source section ID unavailable: `{parts.fragment}`)"
            return f"{label}({local}{'#' + parts.fragment if parts.fragment else ''})"

        content = link_re.sub(rewrite, path.read_text())

        def html_link(match):
            attribute, target = match.groups()
            # Complex GFM tables can contain raw HTML links and images.
            label = "![image]" if attribute == "src" else "[link]"
            adjusted = rewrite(link_re.fullmatch(f"{label}({target})"))
            found = link_re.fullmatch(adjusted)
            if found:
                return f'{attribute}="{found[2]}"'
            return 'data-unavailable-reference="true"'

        content = re.sub(r'(href|src)="([^"]+)"', html_link, content)
        path.write_text(content)
    report = {"topics": quality, "image_sha256": dict(sorted(assets.items())),
              "topic_map_sha256": hashlib.sha256((root / "TOPIC_MAP.yml").read_bytes()).hexdigest(),
              "external_references": sorted(external), "source_issues": issues,
              "fragment_adjustments": adjustments,
              "checks": "DocBook -> GFM -> AST code values and table text compared before link rewriting; explicit section IDs retained"}
    (root / "CONVERSION.json").write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    for path in root.rglob("*.quality.json"):
        path.unlink()
    return report
