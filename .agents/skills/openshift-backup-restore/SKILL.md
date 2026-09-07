---
name: openshift-backup-restore
description: Assess OpenShift backup coverage and failures, OADP application/PV backups, and documented etcd/control-plane recovery. Use to plan or accompany an explicitly requested backup or restore and verify application recovery. Distinguish application backup from full-cluster recovery.
---

# OpenShift backup and restore

Establish whether the task protects an application, persistent data, or the control plane before selecting a procedure.

## Start here

1. Read [the shared domain contract](../openshift-mcp/references/domain-contract.md).
2. Read [the source map](references/sources.md) and the local sections relevant to this task.
3. Use [applications.md](references/applications.md) for OADP and persistent data. Use [control-plane.md](references/control-plane.md) for etcd and disaster recovery.
4. Use [openshift-api](../openshift-api/SKILL.md) to verify schemas and [openshift-mcp](../openshift-mcp/SKILL.md) to perform permitted operations.

This skill depends on the other seven skills being installed as sibling directories.
Resolve every path from this file. Missing documentation, a version mismatch, a
denied access or an unknown schema must remain explicit; do not silently proceed
with a substitute. Pure document lookup belongs to [openshift-docs](../openshift-docs/SKILL.md).

## Report

State the evidence-backed result, target and observed versions, local source path
and section, changes actually performed, verification, and any remaining unknowns.
