---
name: openshift-disconnected
description: Plan and troubleshoot OpenShift disconnected image mirroring, oc-mirror v2, internal registries, mirror resources, CA trust and image-pull failures. Use when preparing release or Operator content for an air gap or diagnosing registry access. Use openshift-upgrade for cluster update execution.
---

# OpenShift disconnected operations

Identify whether the task is mirror preparation, transfer, target-registry import, cluster configuration, or a failing image pull.

## Start here

1. Read [the shared domain contract](../openshift-mcp/references/domain-contract.md).
2. Read [the source map](references/sources.md) and the local sections relevant to this task.
3. Use [mirroring.md](references/mirroring.md) for content preparation and import. Use [image-pulls.md](references/image-pulls.md) for registry, trust and mirror diagnosis.
4. Use [openshift-api](../openshift-api/SKILL.md) to verify schemas and [openshift-mcp](../openshift-mcp/SKILL.md) to perform permitted operations.

This skill depends on the other seven skills being installed as sibling directories.
Resolve every path from this file. Missing documentation, a version mismatch, a
denied access or an unknown schema must remain explicit; do not silently proceed
with a substitute. Pure document lookup belongs to [openshift-docs](../openshift-docs/SKILL.md).

## Report

State the evidence-backed result, target and observed versions, local source path
and section, changes actually performed, verification, and any remaining unknowns.
