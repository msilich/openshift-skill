---
name: openshift-gitops
description: Investigate OpenShift GitOps Applications and ApplicationSets, Argo CD sync/health differences, resource ownership, repository access, RBAC and CA trust. Use the configured read-only Argo CD MCP and OpenShift MCP. Use openshift-mcp for installing the MCP connection and openshift-api for isolated schema questions.
---

# OpenShift GitOps operations

Correlate the Argo CD view with its destination cluster and declared Git source before recommending a change.

## Start here

1. Read [the shared domain contract](../openshift-mcp/references/domain-contract.md).
2. Read [the source map](references/sources.md) and the local sections relevant to this task.
3. Use [reconciliation.md](references/reconciliation.md) for applications and drift. Use [access-and-changes.md](references/access-and-changes.md) for repository access, TLS, RBAC and approved configuration changes.
4. Use [openshift-api](../openshift-api/SKILL.md) to verify schemas and [openshift-mcp](../openshift-mcp/SKILL.md) to perform permitted operations.

This skill depends on the other seven skills being installed as sibling directories.
Resolve every path from this file. Missing documentation, a version mismatch, a
denied access or an unknown schema must remain explicit; do not silently proceed
with a substitute. Pure document lookup belongs to [openshift-docs](../openshift-docs/SKILL.md).

## Report

State the evidence-backed result, target and observed versions, local source path
and section, changes actually performed, verification, and any remaining unknowns.
