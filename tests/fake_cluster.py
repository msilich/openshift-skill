#!/usr/bin/env python3
"""Test-only MCP/oc fixture transport. Never opens a cluster or network socket.

Unknown calls fail closed. Fixtures supply observations, not agent decisions.
Use DOMAIN_SCENARIO and DOMAIN_TRACE for an isolated model evaluation.
"""
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import sys

FIXTURES = Path(__file__).parent / "fixtures" / "domain_scenarios.json"


def scenario(name: str) -> dict:
    return next(item for item in json.loads(FIXTURES.read_text()) if item["id"] == name)


def trace(transport: str, request: object) -> None:
    if path := os.environ.get("DOMAIN_TRACE"):
        with open(path, "a", encoding="utf-8") as output:
            output.write(json.dumps({"transport": transport, "request": request}) + "\n")


def tools_for(case: dict) -> list[dict]:
    if not case.get("reads"):
        return []
    return [{
        "name": "resources_get",
        "description": "Read one synthetic fixture resource, never a real cluster.",
        "inputSchema": {"type": "object", "properties": {
            "kind": {"type": "string"}, "name": {"type": "string"},
            "namespace": {"type": "string"},
        }, "required": ["kind", "name"], "additionalProperties": False},
        "annotations": {"readOnlyHint": True, "destructiveHint": False},
    }]


def mcp_response(case: dict, request: dict) -> dict | None:
    trace("mcp", request)
    if "id" not in request:
        return None
    response = {"jsonrpc": "2.0", "id": request["id"]}
    method = request.get("method")
    if method == "initialize":
        response["result"] = {
            "protocolVersion": request.get("params", {}).get("protocolVersion", "2024-11-05"),
            "capabilities": {"tools": {}},
            "serverInfo": {"name": "offline-domain-fixtures", "version": "1.0.0"},
        }
    elif method == "ping":
        response["result"] = {}
    elif method == "tools/list":
        response["result"] = {"tools": tools_for(case)}
    elif method == "tools/call":
        params = request.get("params", {})
        args = params.get("arguments", {})
        row = next((row for row in case.get("reads", []) if
                    {key: row[key] for key in ("kind", "name", "namespace") if key in row} == args), None)
        if params.get("name") != "resources_get" or row is None:
            response["error"] = {"code": -32602, "message": "Unlisted fixture tool or resource"}
        else:
            response["result"] = {"isError": "error" in row, "content": [{
                "type": "text", "text": row.get("error") or json.dumps(row["result"]),
            }]}
    else:
        response["error"] = {"code": -32601, "message": "Unsupported fixture method"}
    return response


def oc_response(case: dict, args: list[str]) -> tuple[int, str]:
    trace("oc", args)
    if len(args) < 2 or args[:2] != ["--kubeconfig", "/fixture/readonly.kubeconfig"]:
        return 2, "fixture requires explicit /fixture/readonly.kubeconfig"
    args = args[2:]
    identity = {
        ("config", "current-context"): "fixture-context",
        ("whoami",): "fixture-reader",
        ("whoami", "--show-server"): "https://fixture.invalid:6443",
        ("config", "view", "--minify", "-o", "jsonpath={..namespace}"): "shop",
    }
    if tuple(args) in identity:
        return 0, identity[tuple(args)]
    for row in case.get("oc", []):
        if args == row["args"]:
            value = row.get("error", row.get("result"))
            return int("error" in row), value if isinstance(value, str) else json.dumps(value)
    return 2, "Unlisted fixture oc operation; no command was executed"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--scenario", default=os.environ.get("DOMAIN_SCENARIO"))
    parser.add_argument("--transport", choices=("mcp", "oc"), required=True)
    parser.add_argument("args", nargs=argparse.REMAINDER)
    args = parser.parse_args()
    if not args.scenario:
        parser.error("--scenario or DOMAIN_SCENARIO is required")
    case = scenario(args.scenario)
    if args.transport == "oc":
        command = args.args[1:] if args.args[:1] == ["--"] else args.args
        status, output = oc_response(case, command)
        print(output, file=sys.stderr if status else sys.stdout)
        return status
    for line in sys.stdin:
        result = mcp_response(case, json.loads(line))
        if result is not None:
            print(json.dumps(result), flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
