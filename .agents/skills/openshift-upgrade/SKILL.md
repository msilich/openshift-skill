---
name: openshift-upgrade
description: Assess OpenShift cluster update readiness, supported version paths, API removals, Operators, MachineConfigPools, disruption budgets and disconnected release availability. Use to plan or accompany an explicitly requested cluster update and verify completion. Use openshift-disconnected for building image mirrors.
---

# OpenShift update readiness and execution

Assess the requested current-to-target update with evidence, then accompany execution only when explicitly requested.

## Start here

1. Read [the shared domain contract](../openshift-mcp/references/domain-contract.md).
2. Read [the source map](references/sources.md) and the local sections relevant to this task.
3. Use [readiness.md](references/readiness.md) before an update. Use [execution.md](references/execution.md) for an approved update or a stalled update.
4. Use [openshift-api](../openshift-api/SKILL.md) to verify schemas and [openshift-mcp](../openshift-mcp/SKILL.md) to perform permitted operations.

This skill depends on the other seven skills being installed as sibling directories.
Resolve every path from this file. Missing documentation, a version mismatch, a
denied access or an unknown schema must remain explicit; do not silently proceed
with a substitute. Pure document lookup belongs to [openshift-docs](../openshift-docs/SKILL.md).

## Report

State the evidence-backed result, target and observed versions, local source path
and section, changes actually performed, verification, and any remaining unknowns.
