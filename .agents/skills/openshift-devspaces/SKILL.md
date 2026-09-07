---
name: openshift-devspaces
description: Operate and troubleshoot Red Hat OpenShift Dev Spaces using bundled 3.29 documentation, live CheCluster and DevWorkspace evidence, and approved OpenShift MCP access. Use for workspace startup, devfiles, platform configuration, internal registries and IDE access. Use openshift-mcp for connecting OpenCode to MCP, and openshift-api for isolated schema questions.
---

# OpenShift Dev Spaces

Use local product documentation to investigate the platform or a named developer
workspace. A running pod alone does not demonstrate that a workspace or IDE works.

## Start here

1. Read [the shared domain contract](../openshift-mcp/references/domain-contract.md).
2. Read [the source map](references/sources.md), then the relevant local chapters.
3. Select [administration](references/administration.md) for installation, CheCluster
   configuration and upgrades; [workspaces](references/workspaces.md) for devfiles,
   storage and lifecycle; [airgap](references/airgap.md) for mirrors, dependencies and
   extensions; [troubleshooting](references/troubleshooting.md) for failures.
4. For cluster operations load [openshift-mcp](../openshift-mcp/SKILL.md); verify
   served resources and fields with [openshift-api](../openshift-api/SKILL.md).

Install all nine skills as sibling directories. Resolve paths from this file.
Use [openshift-docs](../openshift-docs/SKILL.md) for pure document lookup. Documentation
3.29 does not establish compatibility with either bundled OCP version: compare the
installed Dev Spaces, Dev Workspace Operator and OCP versions with local support
evidence. Report missing compatibility information rather than assuming support.

Diagnosis is read-only. Follow the existing Day-2 approval workflow only for an
explicitly requested change. Do not invent Dev Spaces MCP tools, auto-install `dsc`,
switch identity, or choose a Secret policy for the user. A missing local source or
unknown schema stops that version-specific procedure; denied access is not an
invitation to retry through `oc`.

## Report

State the target workspace/platform, observed versions, local document path and
section, observed facts and remaining uncertainty. For changes report the actual
delta and verification, including the user's original workspace or IDE symptom.
