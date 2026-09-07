# Procedure sources

Product: OpenShift Container Platform 4.22. Source: openshift/openshift-docs at commit `d8cc5bae880cc93ecd22fecd660c1b3a7f1358ff`.
Read [snapshot provenance](../../openshift-docs/references/ocp-4.22/SOURCE.json) for the source, license and conversion details.

| Procedure | Local chapter | Sections to read |
| --- | --- | --- |
| Readiness and API removals | [updating-cluster-prepare.md](../../openshift-docs/references/ocp-4.22/updating/preparing_for_updates/updating-cluster-prepare.md) | Kubernetes API removals; The risk of conditional updates; etcd backups before cluster updates; Best practices for cluster updates |
| Condition semantics | [intro-to-updates.md](../../openshift-docs/references/ocp-4.22/updating/understanding_updates/intro-to-updates.md) | Understanding cluster Operator condition types |
| Update mechanism | [how-updates-work.md](../../openshift-docs/references/ocp-4.22/updating/understanding_updates/how-updates-work.md) | Document introduction and update mechanism |
| Duration constraints | [understanding-openshift-update-duration.md](../../openshift-docs/references/ocp-4.22/updating/understanding_updates/understanding-openshift-update-duration.md) | Document introduction and factors affecting update duration |
| Disconnected prerequisites | [mirroring-image-repository.md](../../openshift-docs/references/ocp-4.22/disconnected/updating/mirroring-image-repository.md) | Document introduction and release mirroring procedure |

These workflows are project-authored adaptations of the cited procedures. MCP
selection, bounded diagnostics, target checks, approval handling and offline
routing are project integration decisions, not statements of Red Hat support.
Documentation snippets still require live schema verification.

Additional adapted reasoning: [cluster-update/cluster-update-advisor/SKILL.md](https://github.com/openshift/agentic-skills/blob/7aca4bee317cd70a4204795db6b1d7b9eb78f48c/cluster-update/cluster-update-advisor/SKILL.md), Apache-2.0. Adapted causal investigation/readiness assessment only; no token scripts, online lookups, environment-specific paths or universal numerical thresholds are imported.
