# Procedure sources

Product: Red Hat OpenShift GitOps 1.21. Source: openshift/openshift-docs at commit `ca5db8539a097b38e2975980963e0959782d105f`.
Read [snapshot provenance](../../openshift-docs/references/gitops-1.21/SOURCE.json) for the source, license and conversion details.

| Procedure | Local chapter | Sections to read |
| --- | --- | --- |
| Desired state and instance ownership | [managing-openshift-cluster-configuration.md](../../openshift-docs/references/gitops-1.21/managing_cluster_configuration/managing-openshift-cluster-configuration.md) | Document introduction and configuration procedures |
| Instance schema and repo-server CA | [argo-cd-cr-component-properties.md](../../openshift-docs/references/gitops-1.21/argocd_instance/argo-cd-cr-component-properties.md) | Argo CD custom resource properties; Configure TLS trust for the repo server |
| Argo CD authorization | [configuring-argo-cd-rbac.md](../../openshift-docs/references/gitops-1.21/accesscontrol_usermanagement/configuring-argo-cd-rbac.md) | Configuring user level access |
| ApplicationSet behavior | [using-progressive-sync-in-openshift-gitops.md](../../openshift-docs/references/gitops-1.21/argocd_application_sets/using-progressive-sync-in-openshift-gitops.md) | Understanding ApplicationSet strategies |
| Health and deployment history | [health-information-for-resources-deployment.md](../../openshift-docs/references/gitops-1.21/observability/monitoring/health-information-for-resources-deployment.md) | Checking health information |

These workflows are project-authored adaptations of the cited procedures. MCP
selection, bounded diagnostics, target checks, approval handling and offline
routing are project integration decisions, not statements of Red Hat support.
Documentation snippets still require live schema verification.
