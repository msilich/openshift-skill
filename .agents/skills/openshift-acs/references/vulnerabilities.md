# Vulnerability evidence

Read [Vulnerability management](../../openshift-docs/references/acs-4.11/operating/manage-vulnerabilities/vulnerability-management.md),
[common tasks](../../openshift-docs/references/acs-4.11/operating/manage-vulnerabilities/common-vuln-management-tasks.md)
and [image examination](../../openshift-docs/references/acs-4.11/operating/examine-images-for-vulnerabilities.md),
selecting image, deployment, node or exception sections as appropriate.
See [sources](sources.md) and [execution](execution.md).

Record the vulnerability identifier, ACS cluster ID, namespace, immutable image
digest or node ID, affected package/version, available fix and scan timestamp.
Keep observed results separate from inferred exploitability or remediation.
Do not equate an image finding with a finding on every deployment using its tag.

Use only offered, approved StackRox tools. `get_deployments_for_cve` and
`get_nodes_for_cve` answer different scopes; `get_clusters_with_orchestrator_cve`
is specifically about orchestrator components, not all images in a cluster.
Pass the verified cluster ID and finite pagination where offered. Inspect schemas
for exact arguments; aggregate/group counts are not counts of individual nodes.
An empty or truncated response, Forbidden, unsupported package or failed scan is
not a clean bill of health. Do not invent a full image inventory MCP tool.

For failures distinguish image retrieval, registry trust/authentication, indexer
or matcher health, unsupported content, and stale vulnerability data. Compare the
scan time and offline database update time against the customer's freshness
requirement, without inventing a universal threshold. Read [offline mode](../../openshift-docs/references/acs-4.11/configuration/enable-offline-mode.md),
especially Updating Scanner definitions in offline mode. Missing feed evidence
means freshness is unknown. No runtime download is allowed in the airgap.

Rescanning, importing feed bundles or generating reports may create jobs or mutate
stored results. Inspect the documented operation and require Day-2 approval when
it writes; `roxctl image scan` is not automatically a read-only fallback.
After an approved repair verify a new successful scan and the original finding,
retaining evidence of the previous stale/failed result.
