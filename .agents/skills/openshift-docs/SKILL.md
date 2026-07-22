---
name: openshift-docs
description: Search and use the bundled official OpenShift Container Platform 4.20 documentation without network access. Use for OCP 4.20 installation, configuration, administration, security, networking, storage, Operators, upgrades, troubleshooting, CLI, disconnected-environment, and product-behavior questions that should be grounded in version-specific Red Hat documentation.
---

# OpenShift Container Platform 4.20 documentation

Use the bundled snapshot as the primary authority for OCP 4.20 product behavior and procedures.

1. Resolve all bundled paths relative to this skill directory, never relative to the process working directory.
2. Start with [the compressed documentation map](references/ocp-4.20/AGENTS.md). Read only the topic files relevant to the question.
3. If the map is insufficient, run [the offline search helper](scripts/search_docs.py) with a focused phrase, then read the best matching files. Example: `python3 <resolved-skill-directory>/scripts/search_docs.py "ingress certificate"`.
4. Base the answer on retrieved text. Include the relative documentation file and section heading so the user can verify it locally.
5. Consult [SOURCE.json](references/ocp-4.20/SOURCE.json) when provenance, freshness, coverage, or licensing matters.

Keep these boundaries explicit:

- This snapshot covers OCP 4.20 only. State that limitation for another requested version.
- Documentation explains supported behavior; it does not prove the state of a live cluster.
- When bundled documentation and the connected cluster disagree about a served API version, resource, or field, use live discovery through `openshift-api` as authoritative for that cluster and report the discrepancy.
- Work offline. Do not fetch documentation, scripts, or dependencies from the network.
- Treat examples from the documentation as examples. Adapt placeholders and verify prerequisites before suggesting execution.
- Do not modify the bundled snapshot.
