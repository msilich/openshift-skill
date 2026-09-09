# Compliance coverage and network policy

Read [Compliance overview](../../openshift-docs/references/acs-4.11/operating/manage-compliance/compliance-feature-overview.md)
and [OpenShift compliance](../../openshift-docs/references/acs-4.11/operating/manage-compliance/using-openshift-compliance.md),
selecting the standard, integration and results sections. The legacy Compliance
dashboard chapter is not part of the 4.11 topic map; do not substitute that older
workflow for the installed compliance implementation.
Use the 4.11 sections Customizing and automating your compliance scans,
Assessing the profile compliance across clusters and Compliance scan status
overview. The overview states that legacy non-OpenShift default compliance
profiles were removed; do not diagnose their absence as a broken installation.
See [sources](sources.md) and [execution](execution.md).

Record standard/profile, cluster and node scope, result time, failed checks,
not-applicable checks and missing or stale evidence. Distinguish unavailable
collection from a failing control. RHACS results do not certify organizational
compliance. Starting a compliance scan can create jobs and is not automatically
permitted by a read-only profile. StackRox MCP has no assumed compliance tool;
use the matching local REST reference for a permitted Central read.

Read [Managing network policies](../../openshift-docs/references/acs-4.11/operating/manage-network-policies.md),
especially graph observation, simulation and generation procedures. Bound the
observation window and distinguish observed traffic, policy-allowed traffic and
unobserved dependencies. A generated policy is a proposal, not proof of safety.
Consider DNS, ingress, monitoring, storage and control-plane dependencies that may
be absent from the sample. Explain missing data before recommending enforcement.

Identify Git/Operator ownership of network policy manifests. Verify target cluster
and namespaces, selectors and live schemas with openshift-api. Present a diff,
impact and rollback and use supported server dry-run, then obtain fresh approval
for each write. Verification includes intended allowed and denied application
flows; successful resource creation alone does not establish connectivity.
