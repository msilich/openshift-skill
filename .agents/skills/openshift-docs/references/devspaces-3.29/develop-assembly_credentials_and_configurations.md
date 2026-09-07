> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/develop-assembly_credentials_and_configurations). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Manage credentials and configurations in workspaces

Manage mounted Git credentials, SSH keys, image pull secrets, and configuration files in OpenShift Dev Spaces workspaces so that tools authenticate and configure automatically.

- **[How credentials and configurations work in workspaces](develop-con_using_credentials_and_configurations_in_workspaces.md)**  
  Mount credentials and configurations into your workspaces so that tools such as Git, Maven, and cloud CLIs authenticate automatically without manual setup each time you start a workspace.
- **[Mount Secrets](develop-proc_mounting_secrets.md)**  
  Mount Kubernetes Secrets into workspace containers to provide sensitive configuration data such as credentials, API keys, and certificates.
- **[Create an image pull Secret with oc](develop-proc_creating_image_pull_secrets.md)**  
  Create an image pull Secret with `oc` to allow `Dev Workspace` Pods to access container registries that require authentication.
- **[Create an image pull Secret from a .dockercfg file](develop-proc_creating_image_pull_secret_from_dockercfg.md)**  
  Create an image pull Secret from an existing `.dockercfg` file to allow `Dev Workspace` Pods to access container registries that require authentication.
- **[Create an image pull Secret from a config.json file](develop-proc_creating_image_pull_secret_from_config_json.md)**  
  Create an image pull Secret from an existing `$HOME/.docker/config.json` file to allow `Dev Workspace` Pods to access container registries that require authentication.
- **[Mount ConfigMaps](develop-proc_mounting_configmaps.md)**  
  Mount Kubernetes ConfigMaps into workspace containers to provide non-sensitive configuration data.
- **[Mount Git configuration](develop-proc_mounting_git_configuration.md)**  
  Mount your Git configuration into workspaces to set your Git identity and preferences.
- **[Mount SSH configuration](develop-proc_mounting_ssh_configuration.md)**  
  Mount custom SSH configurations into workspaces by using a ConfigMap. Extend the default SSH settings with additional parameters or host-specific configurations.
