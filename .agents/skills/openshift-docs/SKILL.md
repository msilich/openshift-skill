---
name: openshift-docs
description: Search the bundled official OCP 4.20, OpenShift GitOps 1.21, Dev Spaces 3.29 and RHACS 4.11 documentation offline. Use for document lookup, procedure explanations and product-behavior questions. For live diagnosis, mirroring, GitOps, Dev Spaces, ACS operations, updates or recovery, use the matching domain skill with this documentation as evidence.
---

# OpenShift product documentation

Use the matching bundled snapshot as the primary authority for product behavior and procedures.

1. Resolve all bundled paths relative to this skill directory, never relative to the process working directory.
2. Start with [the OCP 4.20 map](references/ocp-4.20/AGENTS.md), [the GitOps 1.21 map](references/gitops-1.21/AGENTS.md) or [the Dev Spaces 3.29 map](references/devspaces-3.29/AGENTS.md). GitOps and Dev Spaces have their own release cadences; do not infer their versions from OCP. Read only relevant topic files.
3. If the map is insufficient, use the native file search or [the offline search helper](scripts/search_docs.py). Examples: `python3 <resolved-skill-directory>/scripts/search_docs.py "ingress certificate"` and `python3 <resolved-skill-directory>/scripts/search_docs.py "repo server" --product gitops`. The default remains OCP. In restrictive profiles use native grep/read when Python execution is not permitted.
4. Base the answer on retrieved text. Include the relative documentation file and section heading so the user can verify it locally.
5. Consult [OCP provenance](references/ocp-4.20/SOURCE.json), [GitOps provenance](references/gitops-1.21/SOURCE.json) or [Dev Spaces provenance](references/devspaces-3.29/SOURCE.json) when freshness, coverage or licensing matters. Missing local material is an explicit gap, not permission for a runtime download.

For Dev Spaces use `python3 <resolved-skill-directory>/scripts/search_docs.py "CheCluster" --product devspaces`.
Its HTML snapshot records retrieval dates and hashes, not an unverified Git commit.
External references and missing upstream fragment identifiers are recorded in SOURCE.json;
they are not proof that the linked external information is available offline.

Keep these boundaries explicit:

- The snapshots cover OCP 4.20, GitOps 1.21, Dev Spaces 3.29 and RHACS 4.11. State the limitation for another requested version. Bundling them together does not certify product compatibility.
- Documentation explains supported behavior; it does not prove the state of a live cluster.
- When bundled documentation and the connected cluster disagree about a served API version, resource, or field, use live discovery through `openshift-api` as authoritative for that cluster and report the discrepancy.
- Work offline. Do not fetch documentation, scripts, or dependencies from the network.
- Treat examples from the documentation as examples. Adapt placeholders and verify prerequisites before suggesting execution.
- Do not modify the bundled snapshot.

For RHACS start with [the ACS 4.11 map](references/acs-4.11/AGENTS.md) and use
`python3 <resolved-skill-directory>/scripts/search_docs.py "Scanner" --product acs`.
Read only relevant chapters, including linked REST request/response models.
Cite [ACS provenance](references/acs-4.11/SOURCE.json) and inspect
[the conversion report](references/acs-4.11/CONVERSION.json) for source gaps,
external references and fragment adjustments. Live Central API evidence is the
authority for Central schemas; Kubernetes `oc explain` cannot substitute for it.
Use openshift-acs for RHACS operations and optional StackRox MCP setup.
