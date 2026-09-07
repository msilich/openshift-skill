> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/develop-proc_mounting_ssh_configuration). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Mount SSH configuration

Mount custom SSH configurations into workspaces by using a ConfigMap. Extend the default SSH settings with additional parameters or host-specific configurations.

## Before you begin

- You have an active `oc` session with your project. See [Getting started with the CLI](https://docs.openshift.com/container-platform/4.22/cli_reference/openshift_cli/getting-started-cli.html).

## About this task

Note

The system sets the default SSH configuration automatically from the SSH secret in User Preferences. You can extend it by mounting an additional `.conf` file to `/etc/ssh/ssh_config.d/`.

## Procedure

1.  Create a ConfigMap with the SSH configuration:

    ``` yaml
    kind: ConfigMap
    apiVersion: v1
    metadata:
      name: workspace-userdata-sshconfig-configmap
      namespace: <your_namespace>
      labels:
        controller.devfile.io/mount-to-devworkspace: 'true'
        controller.devfile.io/watch-configmap: 'true'
      annotations:
        controller.devfile.io/mount-as: subpath
        controller.devfile.io/mount-path: /etc/ssh/ssh_config.d/
    data:
      ssh-config.conf: |
        <ssh_config_content>
    ```

    where:

    ` `*`<your_namespace>`*` `  
    Your project name. To find your project, go to `https://__<openshift_dev_spaces_fqdn>__/api/kubernetes/namespace`.

    ` `*`<ssh_config_content>`*` `  
    The SSH configuration file content, for example `Host`, `IdentityFile`, or `ProxyCommand` directives.

2.  Apply the ConfigMap:

    ``` bash
    oc apply -f - <<EOF
    kind: ConfigMap
    apiVersion: v1
    metadata:
      name: workspace-userdata-sshconfig-configmap
      namespace: <your_namespace>
      labels:
        controller.devfile.io/mount-to-devworkspace: 'true'
        controller.devfile.io/watch-configmap: 'true'
      annotations:
        controller.devfile.io/mount-as: subpath
        controller.devfile.io/mount-path: /etc/ssh/ssh_config.d/
    data:
      ssh-config.conf: |
        <ssh_config_content>
    EOF
    ```

## Results

- Start a workspace and verify the SSH configuration file is mounted:

  ``` shell-session
  $ cat /etc/ssh/ssh_config.d/ssh-config.conf
  ```

**Related tasks**  

- [Mount ConfigMaps](develop-proc_mounting_configmaps.md "Mount Kubernetes ConfigMaps into workspace containers to provide non-sensitive configuration data.")

**Related information**  

- [Configuring a user namespace](configure-proc_configuring_a_user_namespace.md)
