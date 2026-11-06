#!/usr/bin/env python3
"""Build pinned RHACM handbooks from local Git checkouts; never download at build time."""
from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor
import hashlib
import json
from pathlib import Path
import posixpath
import re
import shutil
import subprocess
import tempfile
from urllib.parse import unquote, urljoin, urlsplit

import build as common
from acs import pandoc, redact_examples, signature
from convert import sanitize_docbook_xml
from import_devspaces import check_dependencies, convert_html, encoded, soup, verify_generated

HERE = Path(__file__).resolve().parent
PRODUCT = "Red Hat Advanced Cluster Management for Kubernetes"


def definition(lock):
    doc = lock["document"]
    version = doc["version"]
    if not re.fullmatch(r"\d+\.\d+", version) or doc["product"] != PRODUCT:
        raise ValueError("ACM product and explicit major.minor version are required")
    expected = {
        "rhacm_docs": ("https://github.com/stolostron/rhacm-docs", version + "_prod"),
        "api_docs": ("https://github.com/stolostron/api-documentation", "release-" + version),
    }
    for name, (url, branch) in expected.items():
        source = lock["sources"][name]
        if (source["url"], source["branch"]) != (url, branch) or not re.fullmatch(r"[a-f0-9]{40}", source["commit"]):
            raise ValueError("Unexpected ACM source, versioned branch or revision")
    base = "https://docs.redhat.com/en/documentation/red_hat_advanced_cluster_management_for_kubernetes/" + version + "/"
    if doc["base_url"] != base:
        raise ValueError("ACM version and published documentation URL disagree")
    return doc


def verify_checkout(path, source):
    return common.verify_source(path, {"sources": {"openshift_docs": source}})


def inventory(source):
    books = sorted(source.glob("*/master.adoc"))
    if not books:
        raise ValueError("ACM handbook inventory is empty")
    for path in source.rglob("*"):
        if path.is_symlink() and not path.resolve().is_relative_to(source.resolve()):
            raise ValueError("Source symlink escapes checkout: " + str(path))
    for path in source.rglob("*.adoc"):
        if re.search(r"include::https?://|:allow-uri-read:", path.read_text()):
            raise ValueError("Network include is not allowed: " + str(path))
    return books


def preserve_blocks(value):
    """GFM merges adjacent unlabelled code blocks without an explicit separator."""
    if isinstance(value, dict):
        return {key: preserve_blocks(child) for key, child in value.items()}
    if not isinstance(value, list):
        return value
    result = []
    for child in value:
        if (result and isinstance(child, dict) and child.get("t") == "CodeBlock" and
                isinstance(result[-1], dict) and result[-1].get("t") == "CodeBlock"):
            result.append({"t": "RawBlock", "c": ["html", "<!-- Separate adjacent source examples. -->"]})
        result.append(preserve_blocks(child))
    return result


def render_topic(xml, target, warnings, source):
    # Adapt the RHACS renderer without changing any existing product build hashes.
    text, redactions = redact_examples(xml.read_text())
    tree = json.loads(pandoc(text, "docbook", "json"))
    before = signature(tree)
    anchors, blocks = [], []
    for block in tree["blocks"]:
        if block["t"] == "Header" and block["c"][1][0]:
            anchor = block["c"][1][0]
            anchors.append(anchor)
            blocks.append({"t": "RawBlock", "c": ["html", f'<a id="{anchor}"></a>']})
        blocks.append(block)
    tree["blocks"] = blocks
    content = pandoc(json.dumps(preserve_blocks(tree)), "json", "gfm")
    content = "\n".join(
        re.sub(r"(?<!\\)`+[^`\n]*(?<!\\)`+", lambda m: re.sub(r"(?<!\\)\|", r"\\|", m[0]), line)
        if line.startswith("|") else line for line in content.split("\n"))
    after = signature(json.loads(pandoc(pandoc(content, "gfm", "html"), "html", "json")))
    if before != after:
        raise ValueError("ACM code/table round-trip changed content: " + target.name)
    target.write_text(content)
    target.with_suffix(".quality.json").write_bytes(encoded({
        "code_blocks": len(before[0]), "tables": len(before[1]), "anchors": anchors,
        "code_sha256": hashlib.sha256(json.dumps(before[0]).encode()).hexdigest(),
        "table_text_sha256": hashlib.sha256(json.dumps(before[1]).encode()).hexdigest(),
        "redacted_webhook_examples": redactions,
        "source_warnings": warnings.replace(str(source), "<source>").strip().splitlines(),
    }))


def render_book(master, output, source):
    name = master.parent.name + ".md"
    process = subprocess.run([
        "asciidoctor", "-b", "docbook5", "-d", "book", "--safe-mode", "safe",
        "-a", "reproducible", "-o", "-", str(master),
    ], cwd=master.parent, check=True, capture_output=True, text=True, timeout=120)
    # Missing includes would silently publish an incomplete manual otherwise.
    if re.search(r"include file not found|Unresolved directive|asciidoctor: (?:ERROR|FATAL)", process.stderr):
        raise ValueError(process.stderr.replace(str(source), "<source>"))
    xml = output / (master.parent.name + ".xml")
    xml.write_text(process.stdout)
    sanitize_docbook_xml(str(xml))
    target = output / name
    render_topic(xml, target, process.stderr, source)
    quality = json.loads(target.with_suffix(".quality.json").read_text())
    xml.unlink()
    target.with_suffix(".quality.json").unlink()
    return name, quality


def rewrite_references(output, source, lock, quality):
    doc = lock["document"]
    files = set(quality)
    anchors = {name: set(row["anchors"]) for name, row in quality.items()}
    issues, external, assets = [], set(), {}
    catalog = {name[:-3]: name for name in files}
    topics = {}
    for name in sorted(files):
        pending, seen = [source / name[:-3] / "master.adoc"], set()
        while pending:
            origin = pending.pop().resolve()
            if origin in seen or not origin.is_relative_to(source.resolve()) or not origin.is_file():
                continue
            seen.add(origin)
            text = origin.read_text()
            ids = re.findall(r'^\[(?:#|id=")([^\]" ,]+)', text, re.MULTILINE)
            first = next((anchor for anchor in ids if anchor in anchors[name]), None)
            if first:
                topics.setdefault(origin.stem, set()).add((name, first))
            pending.extend(origin.parent / path for path in re.findall(r'^include::([^\[\n]+\.adoc)\[', text, re.MULTILINE))

    def target_for(name, target, image=False):
        parts = urlsplit(target)
        path, fragment = unquote(parts.path), unquote(parts.fragment)
        if image:
            if parts.scheme or parts.netloc:
                raise ValueError("Remote image is not permitted: " + target)
            origin = (source / name[:-3] / path).resolve()
            if not origin.is_relative_to(source.resolve()) or not origin.is_file():
                raise ValueError(f"Missing or escaping ACM image: {name} -> {target}")
            data = origin.read_bytes()
            if origin.suffix.lower() == ".svg" and re.search(rb'<script|(?:href|src)=["\x27]https?://', data):
                raise ValueError("Active or remote SVG content requires review: " + str(origin))
            local = "assets/" + hashlib.sha256(data).hexdigest()[:20] + origin.suffix.lower()
            assets[local] = data
            return local
        if parts.scheme or parts.netloc:
            # Published same-version handbook URLs can be local too.
            if target.startswith(doc["base_url"]):
                match = re.match(r"html(?:-single)?/([^/]+)(?:/|$)", target[len(doc["base_url"]):])
                candidate = catalog.get(match[1]) if match else None
            else:
                candidate = None
            if not candidate:
                external.add(target)
                return target
        else:
            normalized = posixpath.normpath(posixpath.join(name[:-3], path))
            candidate = catalog.get(normalized.split("/")[0]) if path else name
            if not candidate:
                candidate = next((catalog[part] for part in Path(path).parts if part in catalog), None)
            if not candidate and Path(path).suffix in (".adoc", ".xml", ".html"):
                candidate = catalog.get(Path(path).stem)
            choices = sorted(topics.get(Path(path).stem, ())) if path else []
            preferred = [row for row in choices if row[0] == candidate or row[0] == name]
            if len(preferred) == 1 or len(choices) == 1:
                chapter, chapter_anchor = (preferred or choices)[0]
                candidate = chapter
                if not fragment:
                    fragment = chapter_anchor
        if fragment:
            matches = [book for book, ids in anchors.items() if fragment in ids]
            if candidate not in matches:
                if name in matches:
                    candidate = name
                elif len(matches) == 1:
                    candidate = matches[0]
                elif candidate:
                    issues.append({"document": name, "target": target, "resolution": "Local handbook retained; upstream fragment absent"})
                    fragment = ""
        if candidate:
            return candidate + ("#" + fragment if fragment else "")
        if not path and not fragment:
            return name
        # Keep a source gap visible, not a broken relative link or invented ID.
        fallback = doc["base_url"] + "html/" + name[:-3] + "/index"
        issues.append({"document": name, "target": target, "resolution": "Unresolved source target; retained as published external reference"})
        external.add(fallback)
        return fallback

    for name in sorted(files):
        path = output / name
        content = path.read_text()
        content = re.sub(r'(!?)\[([^\]]*)\]\(([^)]+)\)',
                         lambda m: f'{m[1]}[{m[2]}]({target_for(name, m[3], bool(m[1]))})', content)
        content = re.sub(r'\b(href|src)="([^"]+)"',
                         lambda m: f'{m[1]}="{target_for(name, m[2], m[1] == "src")}"', content)
        origin = doc["base_url"] + "html/" + name[:-3] + "/index"
        notice = (f"> Source: [{PRODUCT} {doc['version']}]({origin}). Copyright Red Hat.\n"
                  "> Adapted from AsciiDoc to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md), "
                  "[CC BY-SA 3.0](LICENSE.md) and SOURCE.json for source revisions and gaps.\n\n")
        path.write_text(notice + content)
    return assets, issues, sorted(external)


def build(lock, source, api_source, output):
    doc = definition(lock)
    common.verify_tool_versions(lock)
    check_dependencies(lock)
    common.verify_converter(lock)
    times = {"rhacm_docs": verify_checkout(source, lock["sources"]["rhacm_docs"]),
             "api_docs": verify_checkout(api_source, lock["sources"]["api_docs"])}
    books = inventory(source)
    attributes = (source / "modules/common-attributes.adoc").read_text()
    if f":product-version: {doc['version']}\n" not in attributes:
        raise ValueError("Source product version disagrees with ACM lock")
    # The currently published release branch contains only .gitkeep. Do not
    # invent schemas or silently ignore generated API docs if they appear later.
    if any(path.is_file() and path.name != ".gitkeep" for path in (api_source / "api-docs").rglob("*")):
        raise ValueError("Generated ACM API documentation is now available; review and add its offline import")
    legal = {}
    for row in lock["legal_notices"]:
        path = (HERE / row["path"]).resolve()
        if not path.is_relative_to(HERE) or common.sha256_file(path) != row["sha256"]:
            raise ValueError("Legal source checksum mismatch")
        content = soup(path.read_bytes())
        for link in content.select("a[href]"):
            if not link["href"].startswith("#"):
                link["href"] = urljoin(row["url"], link["href"])
        legal[row["output"]] = ("Source: " + row["url"] + "\n\n" + convert_html(str(content))).encode()

    output.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="acm-stage-", dir=output.parent) as temporary:
        staged = Path(temporary) / "snapshot"
        staged.mkdir()
        with ThreadPoolExecutor(max_workers=4) as pool:
            results = list(pool.map(lambda master: render_book(master, staged, source), books))
        quality = dict(sorted(results))
        assets, issues, external = rewrite_references(staged, source, lock, quality)
        for name, data in {**assets, **legal}.items():
            target = staged / name
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(data)
        shutil.copyfile(api_source / "LICENSE", staged / "LICENSE.api-documentation")
        shutil.copyfile(HERE / "LICENSE.agentic-skills", staged / "LICENSE.agentic-skills")
        gap = {"kind": "missing-generated-api-reference", "source": lock["sources"]["api_docs"],
               "detail": "api-docs contains only a placeholder at this revision. No core API field reference is bundled; use openshift-api against the actual hub/managed cluster."}
        (staged / "api-reference.md").write_text("# ACM API reference coverage\n\n" + gap["detail"] + "\n\n"
            "The product manuals include API-discovery procedures. See [Get started](get_started.md). "
            "Do not infer hub/managed-cluster schemas or product compatibility from this snapshot.\n")
        title = f"# {PRODUCT} {doc['version']} — offline documentation\n\n"
        listing = "\n".join(f"- [{name[:-3]}]({name})" for name in quality) + "\n"
        (staged / "index.md").write_text(title + "All versioned source handbooks; "
            "[API coverage limitation](api-reference.md). External citations are inventoried, not fetched at runtime.\n\n" + listing)
        (staged / "AGENTS.md").write_text(title + "Search with the sibling skill's helper using `--product acm`. "
            "Retrieve relevant sections by matching line and anchor; do not read every handbook. "
            "Distinguish the hub from each managed cluster and verify ACM/MCE/OCP versions independently. "
            "Use openshift-api for live schemas and openshift-mcp for identity, Secret choices and approval. "
            "This documentation does not authorize cluster changes.\n\n" + listing + "\n[API coverage](api-reference.md)\n")
        report = {"handbooks": quality, "source_issues": [gap], "link_adjustments": issues,
                  "external_references": external, "image_sha256": {name: hashlib.sha256(data).hexdigest() for name, data in sorted(assets.items())}}
        (staged / "CONVERSION.json").write_bytes(encoded(report))
        generated = {p.relative_to(staged).as_posix(): p.read_bytes() for p in staged.rglob("*") if p.is_file()}
        links = verify_generated(generated)
        count, manifest = common.markdown_manifest(staged)
        measured = {"handbooks": len(books), "markdown_files": count,
                    "markdown_manifest_sha256": manifest}
        if lock.get("expected_output") and measured != lock["expected_output"]:
            raise ValueError("ACM output does not match the build lock")
        source_info = {"artifact": {**doc, "converted_topics": len(books), "assets": len(assets)},
            "sources": lock["sources"], "source_commit_times": times,
            "inventory": {str(p.relative_to(source)): common.sha256_file(p) for p in books},
            "legal_notices": lock["legal_notices"], "conversion": {"dependencies": lock["dependencies"],
                "local_build_helpers": lock["local_build_helpers"],
                "verified_local_links": links, "checks": "Exact code blocks and table text checked through Pandoc AST; local files, anchors and images verified"},
            "integrity": {"files": {name: hashlib.sha256(data).hexdigest() for name, data in sorted(generated.items())}, **measured},
            "source_issues": [gap], "runtime_network_required": False}
        (staged / "SOURCE.json").write_bytes(encoded(source_info))
        common.replace_output(staged, output, doc)
    print(json.dumps(measured))
    return measured


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--lock", type=Path, default=HERE / "acm.lock.json")
    parser.add_argument("--source-dir", type=Path, required=True)
    parser.add_argument("--api-source-dir", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--refresh-lock", action="store_true")
    args = parser.parse_args()
    lock = json.loads(args.lock.read_text())
    source, api_source, output = args.source_dir.resolve(), args.api_source_dir.resolve(), args.output_dir.resolve()
    if (output == Path.home() or output in Path.home().parents or
            any(output == path or output in path.parents or path in output.parents for path in (source, api_source))):
        raise ValueError("Unsafe or overlapping ACM output directory")
    if args.refresh_lock:
        lock.pop("expected_output", None)
    measured = build(lock, source, api_source, output)
    if args.refresh_lock:
        lock["expected_output"] = measured
        args.lock.write_bytes(encoded(lock))


if __name__ == "__main__":
    main()
