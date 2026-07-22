#!/usr/bin/env python3
"""Search the bundled OCP 4.20 Markdown snapshot without external tools."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


DOCS_ROOT = Path(__file__).resolve().parent.parent / "references" / "ocp-4.20"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Search bundled OpenShift Container Platform 4.20 Markdown files."
    )
    parser.add_argument("query", help="Literal text to find, or a regular expression with --regex")
    parser.add_argument(
        "--regex",
        action="store_true",
        help="Interpret QUERY as a Python regular expression",
    )
    parser.add_argument(
        "--case-sensitive",
        action="store_true",
        help="Use case-sensitive matching (the default is case-insensitive)",
    )
    parser.add_argument(
        "--path",
        default="",
        help="Restrict results to relative paths containing this text",
    )
    parser.add_argument(
        "--max-results",
        type=int,
        default=40,
        help="Stop after this many matching lines (default: 40)",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.max_results < 1:
        print("error: --max-results must be at least 1", file=sys.stderr)
        return 2
    if not DOCS_ROOT.is_dir():
        print(f"error: documentation directory not found: {DOCS_ROOT}", file=sys.stderr)
        return 2

    flags = 0 if args.case_sensitive else re.IGNORECASE
    expression = args.query if args.regex else re.escape(args.query)
    try:
        matcher = re.compile(expression, flags)
    except re.error as error:
        print(f"error: invalid regular expression: {error}", file=sys.stderr)
        return 2

    path_filter = args.path if args.case_sensitive else args.path.casefold()
    matches = 0
    for document in sorted(DOCS_ROOT.rglob("*.md")):
        relative = document.relative_to(DOCS_ROOT).as_posix()
        comparable_path = relative if args.case_sensitive else relative.casefold()
        if path_filter and path_filter not in comparable_path:
            continue
        with document.open(encoding="utf-8", errors="replace") as stream:
            for line_number, line in enumerate(stream, 1):
                if not matcher.search(line):
                    continue
                excerpt = line.strip()
                if len(excerpt) > 400:
                    excerpt = excerpt[:397] + "..."
                print(f"{relative}:{line_number}:{excerpt}")
                matches += 1
                if matches >= args.max_results:
                    return 0

    return 0 if matches else 1


if __name__ == "__main__":
    raise SystemExit(main())
