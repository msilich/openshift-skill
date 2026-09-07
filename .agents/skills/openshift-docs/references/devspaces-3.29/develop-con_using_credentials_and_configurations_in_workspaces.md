> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/develop-con_using_credentials_and_configurations_in_workspaces). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# How credentials and configurations work in workspaces

Mount credentials and configurations into your workspaces so that tools such as Git, Maven, and cloud CLIs authenticate automatically without manual setup each time you start a workspace.

To do so, mount your credentials and configurations to the `Dev Workspace` containers in the OpenShift cluster of your organization’s OpenShift Dev Spaces instance:

- Mount your credentials and sensitive configurations as Kubernetes Secrets.
- Mount your non-sensitive configurations as Kubernetes ConfigMaps.

If you need to allow the `Dev Workspace` Pods in the cluster to access container registries that require authentication, create an image pull Secret for the `Dev Workspace` Pods.

The mounting process uses the standard Kubernetes mounting mechanism and requires applying additional labels and annotations to your existing resources. Resources are mounted when starting a new workspace or restarting an existing one.

You can create permanent mount points for various components:

- Maven configuration, such as the user-specific `settings.xml` file
- Secure Shell (SSH) key pairs
- Git-provider access tokens
- Git configuration
- AWS authorization tokens
- Configuration files
- Persistent storage

For step-by-step instructions on each mounting method, see Additional resources.

**Related tasks**  

- [Mounting Secrets](develop-proc_mounting_secrets.md "Mount Kubernetes Secrets into workspace containers to provide sensitive configuration data such as credentials, API keys, and certificates.")
- [Mounting ConfigMaps](develop-proc_mounting_configmaps.md "Mount Kubernetes ConfigMaps into workspace containers to provide non-sensitive configuration data.")
- [Creating image pull Secrets](develop-proc_creating_image_pull_secrets.md "Create an image pull Secret with oc to allow Dev Workspace Pods to access container registries that require authentication.")
- [Mounting Git configuration](develop-proc_mounting_git_configuration.md "Mount your Git configuration into workspaces to set your Git identity and preferences.")

**Related information**  

- [Using a Git-provider access token](get_started-proc_using_a_git_provider_access_token.md)
- [Apache Maven Settings reference](https://maven.apache.org/settings.html)
- [Kubernetes Documentation: Secrets](https://kubernetes.io/docs/concepts/configuration/secret/)
- [Kubernetes Documentation: ConfigMaps](https://kubernetes.io/docs/concepts/configuration/configmap/)
