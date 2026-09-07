> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/install-assembly_installing_dev_spaces). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Install Red Hat OpenShift Dev Spaces

Install Red Hat OpenShift Dev Spaces on an OpenShift cluster using GitOps (Argo CD), the command-line interface (CLI), or the web console. Choose the method that matches your cluster environment and operational practices.

Note

You can deploy only one instance of OpenShift Dev Spaces per cluster.

- **[Deploy using GitOps and Argo CD](install-proc_deploying_devspaces_using_gitops.md)**  
  Deploy OpenShift Dev Spaces declaratively through OpenShift GitOps (Argo CD) so that every configuration change is tracked in Git, auditable, and automatically reconciled on the cluster.
- **[Deploy using the CLI](install-proc_installing_dev_spaces_using_cli.md)**  
  Deploy OpenShift Dev Spaces from the command line using the `dsc` management tool so that you have full control over configuration options and can automate the installation.
- **[Deploy using the web console](install-proc_installing_dev_spaces_using_web_console.md)**  
  Deploy OpenShift Dev Spaces through the OpenShift web console using the standard OperatorHub workflow so that you can install without command-line access.
- **[Deploy with GitOps in an air-gapped environment](install-proc_deploying_devspaces_using_gitops_in_a_restricted_environment.md)**  
  Deploy OpenShift Dev Spaces in a restricted network through OpenShift GitOps (Argo CD) by mirroring the required container images to a private registry and storing the deployment manifests in an internal Git repository.
- **[Deploy in an air-gapped environment](install-proc_installing_dev_spaces_in_a_restricted_environment_on_openshift.md)**  
  Deploy OpenShift Dev Spaces on an OpenShift cluster with no internet access by mirroring the required container images and Operator catalogs to a private registry.
- **[Enable the Ansible sample in a restricted environment](install-proc_setting_up_ansible_sample.md)**  
  Enable the Ansible getting-started sample in a restricted OpenShift Dev Spaces environment by mirroring the required container images and allowing access to the Ansible Galaxy domains.
- **[Deploy using an external identity provider](install-proc_installing_dev_spaces_on_openshift_with_keycloak_as_oidc.md)**  
  Deploy OpenShift Dev Spaces with Keycloak as the OIDC provider so that you can manage user authentication through your organization’s existing identity infrastructure instead of OpenShift OAuth.
- **[Customize settings during deployment](install-proc_using_dsc_to_configure_checluster_during_installation.md)**  
  Customize the `CheCluster` Custom Resource during installation so that OpenShift Dev Spaces deploys with your organization’s specific settings instead of Operator defaults.
