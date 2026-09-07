<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

# Red Hat OpenShift GitOps Documentation

> Auto-generated Markdown conversion of [openshift/openshift-docs](https://github.com/openshift/openshift-docs).
> Designed for offline AI-agent retrieval. Pinned to the source revision recorded in SOURCE.json.

## Table of Contents

### Release notes

- [OpenShift GitOps release notes](release_notes/gitops-release-notes-1-21.md)

### Understanding OpenShift GitOps

- [What is GitOps?](understanding_openshift_gitops/what-is-gitops.md)
- [About OpenShift GitOps](understanding_openshift_gitops/about-redhat-openshift-gitops.md)
- [Gathering diagnostic information for support](understanding_openshift_gitops/gathering-gitops-diagnostic-information-for-support.md)

### Managing cluster configuration

- [Managing OpenShift cluster configuration](managing_cluster_configuration/managing-openshift-cluster-configuration.md)

### Installing GitOps

- [Preparing to install OpenShift GitOps](installing_gitops/preparing-gitops-install.md)
- [Installing OpenShift GitOps](installing_gitops/installing-openshift-gitops.md)
- [Installing the GitOps CLI](installing_gitops/installing-argocd-gitops-cli.md)

### Argo CD instance

- [Setting up a new Argo CD instance](argocd_instance/setting-up-argocd-instance.md)
- [Argo CD custom resource and component properties](argocd_instance/argo-cd-cr-component-properties.md)
- [Configure webhook secrets for Git providers](argocd_instance/configure-webhook-secrets-git-providers.md)
- [Using Argo CD Image Updater](argocd_instance/using-argo-cd-image-updater.md)

### Access control and user management

- [Configuring Argo CD RBAC](accesscontrol_usermanagement/configuring-argo-cd-rbac.md)
- [Configuring SSO for Argo CD using Dex](accesscontrol_usermanagement/configuring-sso-on-argo-cd-using-dex.md)
- [Configuring SSO for Argo CD using external OIDC providers](accesscontrol_usermanagement/configuring-sso-for-argo-cd-using-oidc.md)
- [Managing local users in Argo CD](accesscontrol_usermanagement/managing-local-users-in-argo-cd.md)

### Managing resource use

- [Configuring Resource Quota](managing_resource/configuring-resource-quota.md)
- [Configure resource requests and limits for GitOps plugin components](managing_resource/configure-resource-requests-and-limits-for-gitops-plugin-components.md)

### Argo CD applications

- [Deploying a Spring Boot application with Argo CD](argocd_applications/deploying-a-spring-boot-application-with-argo-cd.md)
- [Creating an application by using the GitOps CLI](argocd_applications/creating-an-application-using-gitops-argocd-cli.md)
- [Managing the application resources in non-control plane namespaces](argocd_applications/managing-apps-in-non-control-plane-namespaces.md)
- [Managing application links with the managed-by-url annotation](argocd_applications/managing-application-links-with-managed-by-url-annotation.md)
- [Working with the GitOps Console plugin](argocd_applications/working-with-gitops-console-plugin.md)

### Argo CD application sets

- [Managing the application set resources in non-control plane namespaces](argocd_application_sets/managing-app-sets-in-non-control-plane-namespaces.md)
- [Using Progressive Sync in OpenShift GitOps](argocd_application_sets/using-progressive-sync-in-openshift-gitops.md)

### Multitenancy

- [Multitenancy support in GitOps](multitenancy/multitenancy-support-in-gitops.md)

### Declarative cluster configuration

- [Configuring an OpenShift cluster by deploying an application with cluster configurations](declarative_clusterconfig/configuring-an-openshift-cluster-by-deploying-an-application-with-cluster-configurations.md)
- [Customizing permissions by creating user-defined cluster roles for cluster-scoped instances](declarative_clusterconfig/customizing-permissions-by-creating-user-defined-cluster-roles-for-cluster-scoped-instances.md)
- [Customizing permissions by creating aggregated cluster roles](declarative_clusterconfig/customizing-permissions-by-creating-aggregated-cluster-roles.md)
- [Sharding clusters across Argo CD Application Controller replicas](declarative_clusterconfig/sharding-clusters-across-argo-cd-application-controller-replicas.md)

### Argo CD Agent architecture

- [Introduction to the Argo CD Agent architecture](argo_cd_agent_architecture/argocd-agent-architecture-overview.md)

### Argo CD Agent installation

- [Installing Argo CD Agent](argocd_agent_installation/argocd-agent-installation.md)

### Argo Rollouts

- [Argo Rollouts overview](argo_rollouts/argo-rollouts-overview.md)
- [Using Argo Rollouts for progressive deployment delivery](argo_rollouts/using-argo-rollouts-for-progressive-deployment-delivery.md)
- [Getting started with Argo Rollouts](argo_rollouts/getting-started-with-argo-rollouts.md)
- [Routing traffic by using Argo Rollouts](argo_rollouts/routing-traffic-by-using-argo-rollouts.md)
- [Routing traffic by using Argo Rollouts for OpenShift Service Mesh](argo_rollouts/routing-traffic-by-using-argo-rollouts-for-openshift-service-mesh.md)
- [Enabling support for namespace-scoped Argo Rollouts installation](argo_rollouts/enable-support-for-namespace-scoped-argo-rollouts-installation.md)
- [Configuring traffic management and metric plugins in Argo Rollouts](argo_rollouts/configuring_traffic_management_and_metric_plugins_in_argo_rollouts.md)
- [Enabling high availability support for Argo Rollouts](argo_rollouts/enabling-ha-support-for-argo-rollouts.md)
- [Using a cluster-scoped Argo Rollouts instance to manage resources](argo_rollouts/using-cluster-scoped-rollouts-instance-to-manage-rollouts-resources.md)

### Security

- [Configuring secure communication with Redis](securing_openshift_gitops/configuring-secure-communication-with-redis.md)
- [Managing secrets securely using Secrets Store CSI driver with GitOps](securing_openshift_gitops/managing-secrets-securely-using-sscsid-with-gitops.md)
- [Masking sensitive annotations in the Argo CD web UI](securing_openshift_gitops/masking-sensitive-annotations-in-the-argo-cd-web-ui.md)

### GitOps CLI (argocd) reference

- [Configuring the GitOps CLI](gitops_cli_argocd/configuring-argocd-gitops-cli.md)
- [Logging in to the Argo CD server in the default mode](gitops_cli_argocd/logging-in-to-argocd-server-in-default-mode.md)
- [Basic GitOps argocd commands](gitops_cli_argocd/argocd-gitops-cli-reference.md)

### Observability

- **Logging**
  - [Viewing Argo CD logs](observability/logging/viewing-argo-cd-logs.md)
- **Monitoring**
  - [Monitoring with GitOps dashboards](observability/monitoring/monitoring-with-gitops-dashboards.md)
  - [Monitoring Argo CD instances](observability/monitoring/monitoring-argo-cd-instances.md)
  - [Monitoring the GitOps Operator performance](observability/monitoring/monitoring-the-gitops-operator-performance.md)
  - [Monitoring application health status](observability/monitoring/health-information-for-resources-deployment.md)
  - [Monitoring Argo CD custom resource workloads](observability/monitoring/monitoring-argo-cd-custom-resource-workloads.md)

### GitOps workloads on infrastructure nodes

- [Running GitOps control plane workloads on infrastructure nodes](gitops_workloads_infranodes/running-gitops-control-plane-workloads-on-infrastructure-nodes.md)

### Troubleshooting issues

- [Auto-reboot during Argo CD sync with machine configurations](troubleshooting_gitops_issues/auto-reboot-during-argo-cd-sync-with-machine-configurations.md)

### Removing GitOps

- [Uninstalling OpenShift GitOps](removing_gitops/uninstalling-openshift-gitops.md)

