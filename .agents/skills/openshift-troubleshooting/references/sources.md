# Procedure sources

Product: OpenShift Container Platform 4.22. Source: openshift/openshift-docs at commit `d8cc5bae880cc93ecd22fecd660c1b3a7f1358ff`.
Read [snapshot provenance](../../openshift-docs/references/ocp-4.22/SOURCE.json) for the source, license and conversion details.

| Procedure | Local chapter | Sections to read |
| --- | --- | --- |
| Pod startup and logs | [investigating-pod-issues.md](../../openshift-docs/references/ocp-4.22/support/troubleshooting/investigating-pod-issues.md) | Understanding pod error states; Reviewing pod status; Inspecting pod and container logs |
| Storage attachments | [troubleshooting-storage-issues.md](../../openshift-docs/references/ocp-4.22/support/troubleshooting/troubleshooting-storage-issues.md) | Resolving multi-attach errors |
| Node evidence | [verifying-node-health.md](../../openshift-docs/references/ocp-4.22/support/troubleshooting/verifying-node-health.md) | Reviewing node status, resource usage, and configuration |
| OLM and operands | [troubleshooting-operator-issues.md](../../openshift-docs/references/ocp-4.22/support/troubleshooting/troubleshooting-operator-issues.md) | Operator subscription condition types; Querying Operator pod status |
| Network escalation | [troubleshooting-network-issues.md](../../openshift-docs/references/ocp-4.22/support/troubleshooting/troubleshooting-network-issues.md) | Troubleshooting Open vSwitch issues |

These workflows are project-authored adaptations of the cited procedures. MCP
selection, bounded diagnostics, target checks, approval handling and offline
routing are project integration decisions, not statements of Red Hat support.
Documentation snippets still require live schema verification.

Additional adapted reasoning: [cluster-troubleshoot/investigate-alert/SKILL.md](https://github.com/openshift/agentic-skills/blob/7aca4bee317cd70a4204795db6b1d7b9eb78f48c/cluster-troubleshoot/investigate-alert/SKILL.md), Apache-2.0. Adapted causal investigation/readiness assessment only; no token scripts, online lookups, environment-specific paths or universal numerical thresholds are imported.
