---
name: openshift-docs
description: Search the bundled official OCP 4.22 and OpenShift GitOps 1.21 documentation offline. Use for document lookup, procedure explanations and product-behavior questions. For live diagnosis, mirroring, GitOps reconciliation, updates or recovery, use the matching domain skill with this documentation as evidence.
---

# OpenShift product documentation

Use the matching bundled snapshot as the primary authority for product behavior and procedures.

1. Resolve all bundled paths relative to this skill directory, never relative to the process working directory.
2. Start with [the OCP 4.22 map](references/ocp-4.22/AGENTS.md) or [the GitOps 1.21 map](references/gitops-1.21/AGENTS.md). GitOps has its own release cadence; do not infer its version from OCP. Read only relevant topic files.
3. If the map is insufficient, use the native file search or [the offline search helper](scripts/search_docs.py). Examples: `python3 <resolved-skill-directory>/scripts/search_docs.py "ingress certificate"` and `python3 <resolved-skill-directory>/scripts/search_docs.py "repo server" --product gitops`. The default remains OCP. In restrictive profiles use native grep/read when Python execution is not permitted.
4. Base the answer on retrieved text. Include the relative documentation file and section heading so the user can verify it locally.
5. Consult [OCP provenance](references/ocp-4.22/SOURCE.json) or [GitOps provenance](references/gitops-1.21/SOURCE.json) when freshness, coverage or licensing matters. Missing local material is an explicit gap, not permission for a runtime download.

Keep these boundaries explicit:

- The snapshots cover OCP 4.22 and GitOps 1.21. State the limitation for another requested version.
- Documentation explains supported behavior; it does not prove the state of a live cluster.
- When bundled documentation and the connected cluster disagree about a served API version, resource, or field, use live discovery through `openshift-api` as authoritative for that cluster and report the discrepancy.
- Work offline. Do not fetch documentation, scripts, or dependencies from the network.
- Treat examples from the documentation as examples. Adapt placeholders and verify prerequisites before suggesting execution.
- Do not modify the bundled snapshot.
