#!/usr/bin/env python3
"""Fetch an explicit Red Hat HTML inventory, then build it WITHOUT network access.

Raw HTTP responses stay in the preparation cache. The portable ZIP retains the
original document HTML fragments (not site scripts/chrome), images, and a manifest
with both response and fragment hashes. No cluster or authentication operations.
"""
from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
import hashlib
from importlib.metadata import version
import json
from pathlib import Path
import re
import subprocess
import sys
from urllib.parse import unquote, urldefrag, urljoin, urlsplit
from urllib.request import Request, urlopen
import zipfile

from bs4 import BeautifulSoup

HERE = Path(__file__).resolve().parent
IMPORTER_VERSION = "1"


def digest(data):
    return hashlib.sha256(data).hexdigest()


def encoded(value):
    return (json.dumps(value, indent=2, ensure_ascii=False, sort_keys=True) + "\n").encode()


def soup(data):
    return BeautifulSoup(data, "html.parser")


def definition(lock):
    doc = lock["document"]
    if not re.fullmatch(r"\d+\.\d+", doc.get("version", "")):
        raise ValueError("An explicit major.minor version is required")
    expected = "https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/" + doc["version"] + "/"
    if doc.get("base_url") != expected or not doc["toc_url"].startswith(expected):
        raise ValueError("Product, version and inventory URL must agree")
    return doc


def check_dependencies(lock):
    deps = lock["dependencies"]
    if sys.version_info[:2] < tuple(map(int, deps["python_minimum"].split("."))):
        raise ValueError("Python is older than the pinned minimum")
    for name in ("beautifulsoup4", "soupsieve", "typing_extensions"):
        if version(name) != deps[name]:
            raise ValueError(f"Install the pinned {name}=={deps[name]}")
    found = subprocess.check_output(["pandoc", "--version"], text=True).splitlines()[0]
    if found != "pandoc " + deps["pandoc"]:
        raise ValueError("Install pinned Pandoc " + deps["pandoc"])


def local_topic(url, doc):
    url = urldefrag(url)[0]
    if not url.startswith(doc["base_url"]):
        return None
    slug = url[len(doc["base_url"]):]
    if not re.fullmatch(r"[a-zA-Z0-9_-]+", slug):
        return None
    return slug


def download(url, cache):
    """Resumable connected preparation; never used by build/verify."""
    if urlsplit(url).scheme != "https":
        raise ValueError(f"Only HTTPS downloads are permitted: {url}")
    key = digest(url.encode())
    body_path, meta_path = cache / (key + ".body"), cache / (key + ".json")
    if body_path.exists() and meta_path.exists():
        data, meta = body_path.read_bytes(), json.loads(meta_path.read_bytes())
        if digest(data) != meta["response_sha256"]:
            raise ValueError(f"Corrupt preparation cache: {url}")
        return data, meta
    # The public CC license endpoint rejects urllib's default user-agent.
    request = Request(url, headers={"User-Agent": "curl/8.7.1"}) if urlsplit(url).hostname == "creativecommons.org" else url
    with urlopen(request, timeout=45) as response:
        final = response.url
        if urlsplit(final).hostname != urlsplit(url).hostname:
            raise ValueError(f"Cross-host redirect requires review: {url} -> {final}")
        data = response.read(20 * 1024 * 1024 + 1)
        if len(data) > 20 * 1024 * 1024:
            raise ValueError(f"Source exceeds 20 MiB limit: {url}")
        meta = {"url": url, "final_url": final,
                "retrieved_at": datetime.now(timezone.utc).isoformat(),
                "content_type": response.headers.get("Content-Type", ""),
                "response_sha256": digest(data)}
    body_path.write_bytes(data)
    meta_path.write_bytes(encoded(meta))
    return data, meta


def fetch(lock, cache, archive):
    doc = definition(lock)
    cache.mkdir(parents=True, exist_ok=True)
    if archive.exists():
        raise ValueError("Archive already exists; choose a new output path")
    page, meta = download(doc["toc_url"], cache)
    toc = soup(page).select_one("#desktop-toc")
    if toc is None:
        raise ValueError("Full desktop table of contents is missing")
    inventory = sorted({urldefrag(urljoin(doc["toc_url"], a["href"]))[0]
                        for a in toc.select("a[href]")
                        if local_topic(urljoin(doc["toc_url"], a["href"]), doc)})
    if not inventory:
        raise ValueError("Empty topic inventory")
    files, records = {}, []

    def retain(path, data, metadata):
        files[path] = data
        records.append({**metadata, "path": path, "sha256": digest(data)})

    retain("inventory.html", str(toc).encode(), meta)
    pending, seen, external, asset_urls = set(inventory), set(), set(), set()
    titles = {}

    def read_topic(url):
        raw, metadata = download(url, cache)
        if not local_topic(metadata["final_url"], doc):
            raise ValueError(f"Redirect left the selected product/version: {url}")
        content = soup(raw).select_one("section.rhdocs")
        if content is None or content.find("article") is None:
            raise ValueError(f"No documentation article: {url}")
        title = content.find(re.compile("^h[1-6]$"))
        if title is None:
            raise ValueError(f"No topic title: {url}")
        return url, metadata, content, title.get_text(" ", strip=True)

    while pending:
        batch = sorted(pending - seen)
        if not batch:
            break
        if len(seen) + len(batch) > 1500:
            raise ValueError("Unexpected topic closure size; review the inventory")
        pending = set()
        with ThreadPoolExecutor(max_workers=6) as pool:
            for url, metadata, content, title in pool.map(read_topic, batch):
                seen.add(url)
                slug = local_topic(url, doc)
                titles[slug] = title
                retain("topics/" + slug + ".html", str(content).encode(), metadata)
                for a in content.select("a[href]"):
                    target = urldefrag(urljoin(url, a["href"]))[0]
                    if local_topic(target, doc):
                        pending.add(target)
                    elif target and target != doc["base_url"].rstrip("/"):
                        external.add(target)
                for img in content.select("img[src]"):
                    target = urljoin(url, img["src"])
                    if urlsplit(target).hostname != "docs.redhat.com":
                        raise ValueError(f"External image requires review: {target}")
                    asset_urls.add(target)
        print(f"Fetched {len(seen)} topics; {len(pending - seen)} additional references", flush=True)
    for url in sorted(asset_urls):
        data, meta = download(url, cache)
        suffix = Path(urlsplit(url).path).suffix.lower()
        if suffix not in (".svg", ".png", ".jpg", ".jpeg", ".gif", ".webp"):
            raise ValueError(f"Unexpected image type: {url}")
        retain("assets/" + digest(url.encode())[:20] + suffix, data, meta)
    raw, meta = download(doc["legal_url"], cache)
    legal = soup(raw).select_one(".legal-notice-content")
    if legal is None or "Share Alike 3.0" not in legal.get_text():
        raise ValueError("Expected Red Hat CC-BY-SA legal notice is missing")
    retain("legal-notice.html", str(legal).encode(), meta)
    raw, meta = download(doc["license_url"], cache)
    legalcode = soup(raw).select_one("#legal-code-body")
    if legalcode is None:
        legalcode = soup(raw).select_one("#deed-main-content")
    if legalcode is None or "3.0" not in legalcode.get_text():
        raise ValueError("Expected CC-BY-SA 3.0 legal code is missing")
    retain("license.html", str(legalcode).encode(), meta)
    manifest = {"schema_version": 1, "document": doc, "inventory": inventory,
                "topics": titles, "files": sorted(records, key=lambda x: x["path"]),
                "external_references": sorted(external),
                "exclusions": ["Website navigation, JavaScript, tracking and style assets",
                               "Duplicate PDF rendition; all HTML TOC topics are included",
                               "External products, support articles, repositories and downloads remain references"]}
    files["MANIFEST.json"] = encoded(manifest)
    archive.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(archive, "w", compression=zipfile.ZIP_DEFLATED) as zipped:
        for path, data in sorted(files.items()):
            info = zipfile.ZipInfo(path, (1980, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            zipped.writestr(info, data)
    print(json.dumps({"archive_sha256": digest(archive.read_bytes()),
                      "topics": len(titles), "toc_topics": len(inventory),
                      "assets": len(asset_urls)}, indent=2))


def convert_html(data):
    result = subprocess.run(["pandoc", "--from=html", "--to=gfm+raw_html", "--wrap=none", "--preserve-tabs"],
                            input=data, text=True, capture_output=True, check=True).stdout
    # Pandoc 3.7's GFM writer emits bare pipes inside table-cell code spans.
    # GFM readers treat those pipes as column delimiters even inside backticks.
    lines, fence = [], None
    for line in result.splitlines(keepends=True):
        marker = re.match(r"^\s*(`{3,}|~{3,})", line)
        if marker:
            token = marker[1]
            if fence is None:
                fence = token
            elif token[0] == fence[0] and len(token) >= len(fence):
                fence = None
        if fence is None and line.lstrip().startswith("|"):
            if lines and lines[-1].strip() and not lines[-1].lstrip().startswith("|"):
                lines.append("\n")  # Separate a table from preceding inline ID spans.
            line = re.sub(r"(`+)(.+?)\1", lambda match: match[1] + re.sub(r"(?<!\\)\|", r"\\|", match[2]) + match[1], line)
        lines.append(line)
    return "".join(lines)


def prepare_html(content):
    """Remove presentation controls, keep document content and valid table structure."""
    for node in content.select("script, style, button, rh-button, rh-tooltip"):
        node.decompose()
    # Adjacent inline code elements otherwise become invalid `a``b` in GFM.
    for node in list(content.select("code + code")):
        previous = node.previous_sibling
        if getattr(previous, "name", None) == "code":
            previous.append(node.get_text())
            node.decompose()
    for tag in list(content.select("[id]")):
        anchor = content.new_tag("span", id=tag["id"])
        # An anchor before a th/tr is invalid table HTML and truncates Pandoc's
        # table parser. Point those IDs at the enclosing table instead.
        (tag.find_parent("table") or tag).insert_before(anchor)
        del tag["id"]
    for tag in list(content.find_all(True)):
        if tag.name in ("div", "section", "main", "article", "nav", "rh-table", "rh-code-block", "rh-alert"):
            tag.unwrap()
        elif tag.name == "span" and not tag.get("id"):
            tag.unwrap()
        else:
            code_language = next((c for c in tag.get("class", []) if c.startswith("language-")), "language-text")
            tag.attrs = {k: v for k, v in tag.attrs.items()
                         if k in ("id", "href", "src", "alt", "title", "colspan", "rowspan", "start")}
            if tag.name == "code" and tag.find_parent("pre"):
                tag["class"] = [code_language]
    for pre in content.find_all("pre"):
        if pre.find("code") is None:
            pre["class"] = ["text"]
    return content


def legacy_topic(target, fragment, topics, doc):
    """Resolve old Red Hat book URLs only by a unique matching topic identifier."""
    parsed = urlsplit(target)
    if parsed.hostname not in ("docs.redhat.com", "access.redhat.com"):
        return None
    marker = "/red_hat_openshift_dev_spaces/" + doc["version"] + "/"
    if marker not in parsed.path or not fragment:
        return None
    normalized = unquote(fragment).replace("-", "_")
    matches = []
    for url, path in topics.items():
        identifier = Path(path).stem.split("-", 1)[-1]
        if normalized == identifier or normalized.startswith(identifier + "_"):
            matches.append(url)
    return matches[0] if len(matches) == 1 else None


def render_markdown(body):
    return soup(subprocess.run(["pandoc", "--from=gfm+raw_html", "--to=html", "--wrap=none", "--preserve-tabs"],
                              input=body, text=True, capture_output=True, check=True).stdout)


def verify_conversion(original, body):
    """Check retained prose, tables, warnings, exact code contents and images."""
    rendered = render_markdown(body)
    for tag in ("table", "tr", "img"):
        if len(rendered.find_all(tag)) < len(original.find_all(tag)):
            raise ValueError(f"Conversion lost {tag} elements")
    expected_code = [x.get_text().strip("\n") for x in original.find_all("pre")]
    actual_code = [x.get_text().strip("\n") for x in rendered.find_all("pre")]
    if expected_code != actual_code:
        raise ValueError("Conversion changed code blocks")
    normalize = lambda text: re.sub(r"\s+", "", text)
    result_text = normalize(rendered.get_text())
    for node in original.select("p, td, th, dt, dd, h1, h2, h3, h4, h5, h6, .note"):
        # GFM moves table captions below tables. Check nested-table containers
        # piecewise, while retaining contiguous prose checks for ordinary blocks.
        texts = list(node.stripped_strings) if node.find("table") else [node.get_text()]
        if any(normalize(text) not in result_text for text in texts):
            raise ValueError("Conversion lost document text: " + node.get_text()[:160])
    return rendered


def verify_generated(generated):
    """Validate local files, source IDs and image links, including raw HTML links."""
    parsed = {path: render_markdown(data.decode()) for path, data in generated.items() if path.endswith(".md")}
    checked = 0
    for path, content in parsed.items():
        for tag in content.select("a[href], img[src]"):
            target = tag.get("href", tag.get("src"))
            parts = urlsplit(target)
            if parts.scheme or parts.netloc:
                if tag.name == "img":
                    raise ValueError("Image still requires network: " + target)
                continue
            dest = unquote(parts.path) or path
            if dest not in generated:
                raise ValueError(f"Missing local target: {path} -> {target}")
            if parts.fragment and dest in parsed:
                if parsed[dest].find(id=unquote(parts.fragment)) is None:
                    raise ValueError(f"Missing local anchor: {path} -> {target}")
            checked += 1
    return checked


def load_archive(lock, archive):
    if digest(archive.read_bytes()) != lock.get("archive_sha256"):
        raise ValueError("Archive checksum does not match the lock")
    with zipfile.ZipFile(archive) as zipped:
        if len(zipped.namelist()) != len(set(zipped.namelist())):
            raise ValueError("Duplicate archive members")
        manifest = json.loads(zipped.read("MANIFEST.json"))
        if manifest["document"] != definition(lock):
            raise ValueError("Archive product/version does not match the lock")
        files = {}
        for row in manifest["files"]:
            path = row["path"]
            if Path(path).is_absolute() or ".." in Path(path).parts:
                raise ValueError("Unsafe archive member")
            data = zipped.read(path)
            if digest(data) != row["sha256"]:
                raise ValueError("Source checksum mismatch: " + path)
            files[path] = data
        if set(zipped.namelist()) != {*files, "MANIFEST.json"}:
            raise ValueError("Unexpected archive members")
    return manifest, files


def build(lock, archive, output):
    check_dependencies(lock)
    manifest, files = load_archive(lock, archive)
    if output.exists():
        raise ValueError("Output already exists; build into a fresh directory")
    doc = definition(lock)
    topics = {row["url"]: Path(row["path"]).stem + ".md"
              for row in manifest["files"] if row["path"].startswith("topics/")}
    assets = {row["url"]: row["path"] for row in manifest["files"] if row["path"].startswith("assets/")}
    generated, link_issues = {}, []
    anchors = {}
    for url, path in topics.items():
        content = soup(files["topics/" + Path(path).stem + ".html"])
        anchors[path] = {tag["id"] for tag in content.select("[id]")}
    for position, (url, path) in enumerate(sorted(topics.items()), 1):
        content = soup(files["topics/" + Path(path).stem + ".html"])
        content = prepare_html(content)
        for a in content.select("a[href]"):
            target, fragment = urldefrag(urljoin(url, a["href"]))
            legacy = legacy_topic(target, fragment, topics, doc) if target not in topics else None
            if legacy:
                link_issues.append({"source": path, "target": target + "#" + fragment,
                                    "resolution": "Legacy URL mapped to unique local topic: " + topics[legacy]})
                target = legacy
            if target in topics:
                dest = topics[target]
                if fragment and unquote(fragment) not in anchors[dest]:
                    link_issues.append({"source": path, "target": target + "#" + fragment,
                                        "resolution": "Linked to local topic; source fragment is absent"})
                    fragment = ""
                a["href"] = dest + ("#" + fragment if fragment else "")
            elif target.rstrip("/") == doc["base_url"].rstrip("/"):
                a["href"] = "index.md"
            else:
                a["href"] = urljoin(url, a["href"])
        for img in content.select("img[src]"):
            img["src"] = assets[urljoin(url, img["src"])]
            img.attrs.pop("srcset", None)
        body = convert_html(str(content))
        try:
            verify_conversion(content, body)
        except ValueError as error:
            raise ValueError(f"{path}: {error}") from error
        notice = (f"> Source: [{doc['product']} {doc['version']}]({url}). Copyright Red Hat.\n"
                  "> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) "
                  "and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.\n\n")
        generated[path] = (notice + body).encode()
        if position % 50 == 0:
            print(f"Converted and verified {position}/{len(topics)} topics", flush=True)
    generated.update({path: data for path, data in files.items() if path.startswith("assets/")})
    for source_path, target_path, url in (("legal-notice.html", "LEGAL-NOTICE.md", doc["legal_url"]),
                                          ("license.html", "LICENSE.md", doc["license_url"])):
        content = soup(files[source_path])
        for link in content.select("a[href]"):
            if not link["href"].startswith("#"):
                link["href"] = urljoin(url, link["href"])
        generated[target_path] = (f"Source: {url}\n\n" + convert_html(str(content))).encode()
    title = f"# {doc['product']} {doc['version']} — offline documentation\n\n"
    index = title + "Complete HTML table of contents and same-version topic-reference closure.\n" \
        "External references are not downloaded at runtime. See SOURCE.json for coverage and link gaps.\n\n"
    index += "\n".join(f"- [{manifest['topics'][Path(path).stem]}]({path})" for path in sorted(topics.values())) + "\n"
    generated["index.md"] = index.encode()
    generated["AGENTS.md"] = (title + "Use [index.md](index.md) or the sibling skill's offline search helper with `--product devspaces`.\n"
        "Read relevant chapters only; cite the local path and section. This is reference data, not execution authority.\n"
        "Follow openshift-mcp for identity, Secret choices and approval; use openshift-api for served schemas.\n"
        "Do not download external links in the airgap. A link is not proof of compatibility or local availability.\n"
        "Verify installed Dev Spaces, Dev Workspace Operator and OCP versions independently.\n").encode()
    generated["search-index.json"] = encoded([{"path": path, "title": manifest["topics"][Path(path).stem]} for path in sorted(topics.values())])
    checked_links = verify_generated(generated)
    content_hash = digest("".join(f"{digest(data)}  {path}\n" for path, data in sorted(generated.items())).encode())
    source = {"artifact": {"product": doc["product"], "version": doc["version"],
                           "converted_topics": len(topics), "toc_topics": len(manifest["inventory"]),
                           "assets": len(assets)},
              "archive_sha256": lock["archive_sha256"], "files": manifest["files"],
              "conversion": {"importer_version": IMPORTER_VERSION, "dependencies": lock["dependencies"],
                             "link_adjustments": link_issues, "verified_local_links": checked_links,
                             "content_checks": "Per-topic prose, table rows, code blocks and images checked after Markdown round-trip"},
              "exclusions": manifest["exclusions"], "external_references": manifest["external_references"],
              "integrity": {"content_manifest_sha256": content_hash,
                            "files": {path: digest(data) for path, data in sorted(generated.items())}}}
    expected = lock.get("expected_output")
    if expected and (expected["content_manifest_sha256"] != content_hash or expected["topics"] != len(topics)):
        raise ValueError("Generated output does not match the lock")
    generated["SOURCE.json"] = encoded(source)
    output.mkdir(parents=True)
    for path, data in generated.items():
        target = output / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(data)
    print(json.dumps({"topics": len(topics), "content_manifest_sha256": content_hash,
                      "link_adjustments": len(link_issues)}, indent=2))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("operation", choices=("fetch", "build"))
    parser.add_argument("--lock", type=Path, default=HERE / "devspaces.lock.json")
    parser.add_argument("--archive", type=Path, help="Override archive path; hash is still enforced for build")
    parser.add_argument("--cache-dir", type=Path, help="Connected fetch response cache (not installed)")
    parser.add_argument("--output-dir", type=Path, help="Fresh offline build destination")
    args = parser.parse_args()
    lock = json.loads(args.lock.read_bytes())
    archive = args.archive or args.lock.parent / lock["archive"]
    if args.operation == "fetch":
        if not args.cache_dir:
            parser.error("fetch requires --cache-dir")
        fetch(lock, args.cache_dir, archive)
    else:
        if not args.output_dir:
            parser.error("build requires --output-dir")
        build(lock, archive, args.output_dir)


if __name__ == "__main__":
    main()
