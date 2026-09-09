---
name: openshift-acs
description: Operate and troubleshoot self-managed Red Hat Advanced Cluster Security (RHACS/ACS/StackRox) using bundled 4.11 documentation. Use for Central, Sensor, Collector, Scanner, CVEs, violations, enforcement, compliance coverage, network policies, airgap feeds, upgrades and ACS recovery. Diagnose first; perform only explicitly requested Day-2 changes. Use openshift-docs for pure document lookup, openshift-api for Kubernetes schemas, and openshift-mcp for OpenShift connection setup.
---

# OpenShift ACS

Read [the shared contract](../openshift-mcp/references/domain-contract.md),
[sources](references/sources.md) and [execution](references/execution.md) first.
Install all ten skills as sibling directories; resolve paths from this file,
not the current working directory. Instructions are project-authored adaptations.

Choose the relevant procedure and read its local source chapters before access:

- [Platform](references/platform.md): component health, connectivity, Operator ownership and certificates.
- [Vulnerabilities](references/vulnerabilities.md): affected workloads/nodes, failed scans and data freshness.
- [Policies](references/policies.md): violations, enforcement, exceptions and ownership.
- [Compliance and network](references/compliance-network.md): evidence coverage and policy proposals.
- [Airgap and lifecycle](references/lifecycle.md): feeds, mirrors, upgrades and ACS backup/restore.

Use [optional StackRox MCP setup](references/stackrox-mcp.md) only when requested.
Loading this skill never installs or starts a server. The MCP is Developer Preview
and read-only; it does not expose general Central administration.

Before interpreting findings, establish the Central instance, ACS cluster ID and,
where applicable, the explicit OpenShift kubeconfig/context and namespace. Names
alone do not establish identity. Compare installed Central, secured-cluster,
Scanner, Operator and roxctl versions with RHACS 4.11; OCP has a separate lifecycle.
A version mismatch permits generic read-only investigation, not unsupported
version-specific changes. Missing local documentation or schemas are explicit gaps.

OpenShift MCP operates cluster resources. StackRox MCP reads only supported Central
data. Missing Central functions require documented REST/roxctl, not an `oc` substitute.
An authorization denial stops that access: never bypass it via another tool or
identity. Do not switch context, log in, fetch runtime dependencies, or choose a
Secret mode for the user. Follow the existing four-choice Secret policy unchanged.

For an explicitly requested change, verify state/owner and schema, show the delta,
impact and rollback, preview where supported, obtain a fresh OpenCode `once`
approval, then verify the result and original symptom. Never use `--auto` or an
`always` approval. Read-only mode forbids writing fallbacks. Scan, compliance and
dry-run jobs can create state and require the same approval when they do.

Report the mapped target, observed versions, local document path and section,
scan/evidence timestamps, scope actually checked, outcome and remaining uncertainty.
No findings is not proof of absence; backup success is not recovery proof.
