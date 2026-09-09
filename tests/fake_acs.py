"""Test-only ACS transports and approval driver. Not a production gateway or agent.

No sockets, credentials, clusters or model calls. Assertions here establish only
the synthetic test protocol, never that Qwen follows the skill instructions.
"""
from __future__ import annotations

import argparse
import copy
import hashlib
import json
import sys

TOOLS = ("list_secured_clusters", "get_deployments_for_cve", "get_nodes_for_cve",
         "get_clusters_with_orchestrator_cve")
HOST = "central.example.invalid:443"
CLUSTER_ID = "cluster-fixture-01"


class FakeACS:
    def __init__(self, readonly=True, forbidden=False):
        self.readonly = readonly
        self.forbidden = forbidden
        self.policy = {"id": "policy-fixture-01", "name": "fixture policy", "disabled": False}
        self.trace = []
        self.grants = set()

    def mcp(self, request, missing=False):
        self.trace.append(("mcp", request["method"]))
        if request["method"] == "tools/list":
            return {"tools": [] if missing else [{"name": name,
                    "description": "Synthetic ACS test fixture, not a production tool",
                    "inputSchema": {"type": "object", "properties": {
                        "limit": {"type": "integer"}, "offset": {"type": "integer"},
                        "filterClusterId": {"type": "string"}, "cveName": {"type": "string"}}},
                    "annotations": {"readOnlyHint": True}} for name in TOOLS]}
        name = request["params"]["name"]
        args = request["params"].get("arguments", {})
        if name not in TOOLS or missing:
            return {"error": "unknown tool"}
        if self.forbidden:
            return {"error": "Forbidden"}
        if name == "list_secured_clusters":
            if args.get("limit", 0) <= 0:
                return {"error": "fixture requires bounded limit"}
            return {"clusters": [{"id": CLUSTER_ID, "name": "production", "type": "OPENSHIFT_CLUSTER"}]}
        if args.get("filterClusterId") != CLUSTER_ID:
            return {"error": "target mismatch"}
        return {"fixture": "stale offline feed", "scanTime": "2026-09-01T12:00:00Z",
                "feedTime": "2026-07-01T00:00:00Z", "clusterId": CLUSTER_ID}

    def cli(self, binary, args):
        self.trace.append((binary, args))
        if self.forbidden:
            return 1, "Forbidden"
        if binary == "roxctl" and args == ["version"]:
            return 0, "roxctl version 4.11.0 (synthetic)"
        if binary == "oc" and args == ["--kubeconfig", "/fixture/readonly.kubeconfig",
                                        "explain", "central.spec", "--api-version=platform.stackrox.io/v1alpha1"]:
            return 0, "spec (synthetic schema fixture; not a live cluster observation)"
        return 2, "unknown or unapproved fixture command"

    @staticmethod
    def ticket(method, path, body):
        return hashlib.sha256(json.dumps([method, path, body], sort_keys=True).encode()).hexdigest()

    def approve_once(self, method, path, body):
        self.grants.add(self.ticket(method, path, body))

    def central(self, host, method, path, body=None, uncertain=False):
        self.trace.append(("central", method, path))
        if host != HOST:
            return 421, {"error": "Central mismatch"}
        if self.forbidden:
            return 403, {"error": "Forbidden"}
        if method == "GET" and path == "/v1/policies/policy-fixture-01":
            return 200, copy.deepcopy(self.policy)
        if (method, path) not in (("POST", "/v1/policies/dryrun"),
                                 ("PUT", "/v1/policies/policy-fixture-01")):
            return 404, {"error": "unknown fixture operation"}
        if self.readonly:
            return 403, {"error": "read-only identity"}
        token = self.ticket(method, path, body)
        if token not in self.grants:
            return 403, {"error": "fresh once approval required"}
        self.grants.remove(token)
        # Minimal synthetic subset of PolicyServicePutPolicyBody, not a schema validator.
        if method == "PUT":
            if not isinstance(body, dict) or "name" not in body:
                return 400, {"error": "unknown request model"}
            if set(body) - {"name", "disabled"}:
                return 400, {"error": "unknown policy field"}
            self.policy = {"id": "policy-fixture-01", **copy.deepcopy(body)}
        if uncertain:
            return 504, {"error": "result unknown after submission"}
        return 200, {"result": "synthetic preview" if method == "POST" else "submitted"}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--transport", choices=("mcp", "oc", "roxctl"), required=True)
    parser.add_argument("--missing", action="store_true")
    parser.add_argument("--forbidden", action="store_true")
    args, command = parser.parse_known_args()
    lab = FakeACS(forbidden=args.forbidden)
    if args.transport != "mcp":
        code, result = lab.cli(args.transport, command[1:] if command[:1] == ["--"] else command)
        print(result)
        return code
    for line in sys.stdin:
        request = json.loads(line)
        if "id" not in request:
            continue
        if request["method"] == "initialize":
            result = {"protocolVersion": "2024-11-05", "capabilities": {"tools": {}},
                      "serverInfo": {"name": "test-only-acs", "version": "0"}}
        else:
            result = lab.mcp(request, args.missing)
            if request["method"] == "tools/call":
                result = {"content": [{"type": "text", "text": json.dumps(result)}], "isError": "error" in result}
        print(json.dumps({"jsonrpc": "2.0", "id": request["id"], "result": result}), flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
