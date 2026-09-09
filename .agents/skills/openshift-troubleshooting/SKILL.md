---
name: openshift-troubleshooting
description: Investigate OpenShift workload, networking, storage, node and Operator failures using local documentation and live evidence. Use for CrashLoopBackOff, Pending, ImagePullBackOff, unavailable services, unbound PVCs or degraded cluster components. Use openshift-gitops for GitOps reconciliation, openshift-upgrade for update readiness, and openshift-mcp for connection setup.
---

# OpenShift troubleshooting

Find the cause of the reported failure and verify any requested repair against the original symptom.

## Start here

1. Read [the shared domain contract](../openshift-mcp/references/domain-contract.md).
2. Read [the source map](references/sources.md) and the local sections relevant to this task.
3. Use [workloads.md](references/workloads.md) for pod startup, scheduling and service reachability. Use [infrastructure.md](references/infrastructure.md) for storage, nodes, Operators and alert correlation.
4. Use [openshift-api](../openshift-api/SKILL.md) to verify schemas and [openshift-mcp](../openshift-mcp/SKILL.md) to perform permitted operations.

This skill depends on the other nine skills being installed as sibling directories.
Resolve every path from this file. Missing documentation, a version mismatch, a
denied access or an unknown schema must remain explicit; do not silently proceed
with a substitute. Pure document lookup belongs to [openshift-docs](../openshift-docs/SKILL.md).

## Report

State the evidence-backed result, target and observed versions, local source path
and section, changes actually performed, verification, and any remaining unknowns.
