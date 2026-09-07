> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/install-con_installation_overview). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# How the installation works

OpenShift Dev Spaces deploys on OpenShift as an Operator that manages a gateway, dashboard, server, and plug-in registry. The installation method you choose depends on your cluster environment and need for configuration control.

OpenShift Dev Spaces consists of an Operator, a user dashboard, a gateway, and a plug-in registry. The Operator manages the full lifecycle of all server components. You deploy OpenShift Dev Spaces by installing the Operator and creating a `CheCluster` custom resource.

<span id="con_installation-overview_devspaces___installation_methods"></span>

## [Installation methods](install-con_installation_overview.md#con_installation-overview_devspaces___installation_methods)

OpenShift GitOps (Argo CD)  
Choose this method for production deployments where every configuration change must be tracked in Git, auditable, and automatically reconciled on the cluster. Store the Operator subscription and `CheCluster` configuration in a Git repository and let Argo CD manage the deployment lifecycle.

`dsc` command-line tool  
Choose this method when you need to quickly deploy OpenShift Dev Spaces for evaluation, customize the `CheCluster` configuration during installation, or manage OpenShift Dev Spaces from scripts.

OpenShift web console  
Choose this method when you prefer a graphical workflow through OperatorHub and do not need advanced configuration options during deployment.

All methods produce the same result: an Operator subscription and a `CheCluster` custom resource. For step-by-step deployment instructions, see Additional resources.

<span id="con_installation-overview_devspaces___deployment_scenarios"></span>

## [Deployment scenarios](install-con_installation_overview.md#con_installation-overview_devspaces___deployment_scenarios)

Standard deployment  
Your OpenShift cluster has internet access. All installation methods are available. The Operator pulls container images directly from `registry.redhat.io`.

GitOps deployment  
Your organization manages cluster configuration declaratively through Argo CD. Store the Operator subscription and `CheCluster` configuration in a Git repository and let Argo CD reconcile the desired state. Available for both connected and air-gapped clusters.

Air-gapped deployment  
Your cluster has no internet access. Mirror the required container images and Operator catalogs to a private registry before installation. Both GitOps and CLI methods are available for air-gapped environments.

External identity provider  
Your organization manages authentication through an existing identity system such as Keycloak. Deploy OpenShift Dev Spaces with an external OIDC provider instead of the default OpenShift OAuth.

- **[Permissions required for CLI installation](install-ref_permissions_to_install_devspaces_using_cli.md)**  
  Apply this `ClusterRole` to the installer’s service account or user to grant the minimum permissions required for a `dsc`-based installation of OpenShift Dev Spaces.
- **[Permissions required for web console installation](install-ref_permissions_to_install_devspaces_using_web_console.md)**  
  Install OpenShift Dev Spaces through the OpenShift web console with a specific set of cluster permissions. Apply this `ClusterRole` to the installer’s service account or user to grant the minimum required permissions for web console installation.

**Related tasks**  

- [Deploy using GitOps and Argo CD](install-proc_deploying_devspaces_using_gitops.md "Deploy OpenShift Dev Spaces declaratively through OpenShift GitOps (Argo CD) so that every configuration change is tracked in Git, auditable, and automatically reconciled on the cluster.")
- [Deploy using the CLI](install-proc_installing_dev_spaces_using_cli.md "Deploy OpenShift Dev Spaces from the command line using the dsc management tool so that you have full control over configuration options and can automate the installation.")
- [Deploy using the web console](install-proc_installing_dev_spaces_using_web_console.md "Deploy OpenShift Dev Spaces through the OpenShift web console using the standard OperatorHub workflow so that you can install without command-line access.")
- [Deploy in an air-gapped environment](install-proc_installing_dev_spaces_in_a_restricted_environment_on_openshift.md "Deploy OpenShift Dev Spaces on an OpenShift cluster with no internet access by mirroring the required container images and Operator catalogs to a private registry.")
- [Deploy using an external identity provider](install-proc_installing_dev_spaces_on_openshift_with_keycloak_as_oidc.md "Deploy OpenShift Dev Spaces with Keycloak as the OIDC provider so that you can manage user authentication through your organization’s existing identity infrastructure instead of OpenShift OAuth.")
