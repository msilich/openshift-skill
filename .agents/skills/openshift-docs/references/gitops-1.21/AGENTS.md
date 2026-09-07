<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

# Red Hat OpenShift GitOps Documentation Index

> IMPORTANT: Prefer retrieval-led reasoning over pre-training-led
> reasoning for OpenShift tasks. Read the referenced files rather
> than relying on training data which may be outdated.

## How to Use This Index

This is a compressed documentation map. Each section lists topic
files using pipe-delimited format: `section/subsection:{file1.md,file2.md}`.
Retrieve the specific file you need rather than reading everything.

Root: ./

## Documentation Map

### Release notes

|release_notes:{gitops-release-notes-1-21.md}

### Understanding OpenShift GitOps

|understanding_openshift_gitops:{what-is-gitops.md,about-redhat-openshift-gitops.md,gathering-gitops-diagnostic-information-for-support.md}

### Managing cluster configuration

|managing_cluster_configuration:{managing-openshift-cluster-configuration.md}

### Installing GitOps

|installing_gitops:{preparing-gitops-install.md,installing-openshift-gitops.md,installing-argocd-gitops-cli.md}

### Argo CD instance

|argocd_instance:{setting-up-argocd-instance.md,argo-cd-cr-component-properties.md,configure-webhook-secrets-git-providers.md,using-argo-cd-image-updater.md}

### Access control and user management

|accesscontrol_usermanagement:{configuring-argo-cd-rbac.md,configuring-sso-on-argo-cd-using-dex.md,configuring-sso-for-argo-cd-using-oidc.md,managing-local-users-in-argo-cd.md}

### Managing resource use

|managing_resource:{configuring-resource-quota.md,configure-resource-requests-and-limits-for-gitops-plugin-components.md}

### Argo CD applications

|argocd_applications:{deploying-a-spring-boot-application-with-argo-cd.md,creating-an-application-using-gitops-argocd-cli.md,managing-apps-in-non-control-plane-namespaces.md,managing-application-links-with-managed-by-url-annotation.md,working-with-gitops-console-plugin.md}

### Argo CD application sets

|argocd_application_sets:{managing-app-sets-in-non-control-plane-namespaces.md,using-progressive-sync-in-openshift-gitops.md}

### Multitenancy

|multitenancy:{multitenancy-support-in-gitops.md}

### Declarative cluster configuration

|declarative_clusterconfig:{configuring-an-openshift-cluster-by-deploying-an-application-with-cluster-configurations.md,customizing-permissions-by-creating-user-defined-cluster-roles-for-cluster-scoped-instances.md,customizing-permissions-by-creating-aggregated-cluster-roles.md,sharding-clusters-across-argo-cd-application-controller-replicas.md}

### Argo CD Agent architecture

|argo_cd_agent_architecture:{argocd-agent-architecture-overview.md}

### Argo CD Agent installation

|argocd_agent_installation:{argocd-agent-installation.md}

### Argo Rollouts

|argo_rollouts:{argo-rollouts-overview.md,using-argo-rollouts-for-progressive-deployment-delivery.md,getting-started-with-argo-rollouts.md,routing-traffic-by-using-argo-rollouts.md,routing-traffic-by-using-argo-rollouts-for-openshift-service-mesh.md,enable-support-for-namespace-scoped-argo-rollouts-installation.md,configuring_traffic_management_and_metric_plugins_in_argo_rollouts.md,enabling-ha-support-for-argo-rollouts.md,using-cluster-scoped-rollouts-instance-to-manage-rollouts-resources.md}

### Security

|securing_openshift_gitops:{configuring-secure-communication-with-redis.md,managing-secrets-securely-using-sscsid-with-gitops.md,masking-sensitive-annotations-in-the-argo-cd-web-ui.md}

### GitOps CLI (argocd) reference

|gitops_cli_argocd:{configuring-argocd-gitops-cli.md,logging-in-to-argocd-server-in-default-mode.md,argocd-gitops-cli-reference.md}

### Observability

|observability/logging:{viewing-argo-cd-logs.md}
|observability/monitoring:{monitoring-with-gitops-dashboards.md,monitoring-argo-cd-instances.md,monitoring-the-gitops-operator-performance.md,health-information-for-resources-deployment.md,monitoring-argo-cd-custom-resource-workloads.md}

### GitOps workloads on infrastructure nodes

|gitops_workloads_infranodes:{running-gitops-control-plane-workloads-on-infrastructure-nodes.md}

### Troubleshooting issues

|troubleshooting_gitops_issues:{auto-reboot-during-argo-cd-sync-with-machine-configurations.md}

### Removing GitOps

|removing_gitops:{uninstalling-openshift-gitops.md}

