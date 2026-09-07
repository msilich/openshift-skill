> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/configure-assembly_configuring_projects). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Organize workspace namespaces

Organize how OpenShift Dev Spaces creates and manages projects for workspaces so that you can enforce naming conventions, pre-provision resources, and synchronize configurations across teams.

- **[How workspace namespaces are organized](configure-con_configuring_projects.md)**  
  OpenShift Dev Spaces isolates workspaces for each user in a project, identified by labels and annotations. If the project does not exist, OpenShift Dev Spaces creates it from a template.
- **[Set the workspace namespace naming convention](configure-proc_configuring_project_name.md)**  
  Set the project name template that OpenShift Dev Spaces uses when creating workspace projects to enforce naming conventions and organizational compliance.
- **[Provision projects in advance](configure-proc_provisioning_projects_in_advance.md)**  
  Provision workspace projects in advance, rather than relying on automatic provisioning, to control namespace naming and apply custom resource quotas. Repeat the procedure for each user.
- **[Synchronize resources across user namespaces](configure-proc_configuring_a_user_namespace.md)**  
  Synchronize `ConfigMaps`, `Secrets`, `PersistentVolumeClaims`, and other Kubernetes objects from the `openshift-devspaces` namespace to user-specific namespaces to provide consistent workspace configurations.
- **[Use Kubernetes namespaces instead of OpenShift projects](configure-proc_configuring_kubernetes_namespace_creation_on_openshift.md)**  
  Use standard Kubernetes namespaces directly on OpenShift Container Platform instead of using the ProjectRequest API to bypass cluster-specific Project Templates.

**Related concepts**  

- [Set workspace policies for all users](configure-assembly_configuring_workspaces_globally.md "Set workspace limits, Git certificate trust, node scheduling, allowed URLs, and container capabilities that apply to every developer on the platform.")
