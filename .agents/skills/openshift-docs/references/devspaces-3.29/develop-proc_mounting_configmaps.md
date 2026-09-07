> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/develop-proc_mounting_configmaps). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Mount ConfigMaps

Mount Kubernetes ConfigMaps into workspace containers to provide non-sensitive configuration data.

## Before you begin

- You have an active `oc` session with your project. See [Getting started with the CLI](https://docs.openshift.com/container-platform/4.22/cli_reference/openshift_cli/getting-started-cli.html). Warning

  By default, applying a `ConfigMap` with the `controller.devfile.io/mount-to-devworkspace: 'true'` label restarts all running workspaces in the project. To mount the ConfigMap only at workspace start and prevent automatic restarts, add the `controller.devfile.io/mount-on-start: 'true'` annotation.

## Procedure

1.  Create a ConfigMap with the required labels and annotations:

    ``` yaml
    kind: ConfigMap
    apiVersion: v1
    metadata:
      name: my-config
      labels:
        controller.devfile.io/mount-to-devworkspace: 'true'
        controller.devfile.io/watch-configmap: 'true'
      annotations:
        controller.devfile.io/mount-as: file
        controller.devfile.io/mount-path: /etc/my-config
    data:
      settings.json: |
        {
          "editor.fontSize": 14,
          "editor.tabSize": 2
        }
    ```

    where:

    controller.devfile.io/mount-to-devworkspace  
    Required label to mount the ConfigMap to all workspaces.

    controller.devfile.io/watch-configmap  
    Watch the ConfigMap for changes and update mounted files.

    controller.devfile.io/mount-as  
    Mount type: `file`, `subpath`, or `env`.

    controller.devfile.io/mount-path  
    Path where the ConfigMap data is mounted.

2.  Apply the ConfigMap to your project:

    ``` bash
    $ oc apply -f my-config.yaml -n <your_namespace>
    ```

3.  Optional: Add annotations to the ConfigMap to customize the mounting behavior. <span id="mounting-configmaps_devspaces__entry__1"></span><span id="mounting-configmaps_devspaces__entry__2"></span>

    | Annotation | Description |
    |----|----|
    | `controller.devfile.io/mount-path: `*`<path>`* | Overrides the default mount path. The default mount path is `/etc/config/`*`<ConfigMap_name>`*. |
    | `controller.devfile.io/mount-as: file` | Each key in the ConfigMap data becomes a file in the mount path directory. |
    | `controller.devfile.io/mount-as: subpath` | Similar to `file`, but uses subPath volumes for better compatibility. |
    | `controller.devfile.io/mount-as: env` | Each key-value pair becomes an environment variable in all workspace containers. |
    | `controller.devfile.io/mount-on-start: 'true'` | When set to `true`, the ConfigMap is mounted only when a workspace starts, not while it is already running. This prevents workspace restarts when the ConfigMap is created. |
    | `controller.devfile.io/mount-to-devworkspace-include:` | Specifies a comma-separated list of `Dev Workspace` name patterns. When set, the ConfigMap is mounted only to workspaces whose names match at least one pattern. |
    | `controller.devfile.io/mount-to-devworkspace-exclude:` | Specifies a comma-separated list of `Dev Workspace` name patterns. When set, the ConfigMap is mounted to all workspaces except those whose names match a pattern. |

    Table 1. ConfigMap mounting annotations

    Note

    When both `controller.devfile.io/mount-to-devworkspace-include` and `controller.devfile.io/mount-to-devworkspace-exclude` annotations are set, the ConfigMap is mounted only to workspaces that match the include pattern and do not match the exclude pattern.

    For example, to mount ConfigMap data as environment variables:

    ``` yaml
    kind: ConfigMap
    apiVersion: v1
    metadata:
      name: my-env-config
      labels:
        controller.devfile.io/mount-to-devworkspace: 'true'
        controller.devfile.io/watch-configmap: 'true'
      annotations:
        controller.devfile.io/mount-as: env
    data:
      LOG_LEVEL: debug
      MAX_CONNECTIONS: "100"
    ```

4.  Start or restart your workspace to apply the mounted ConfigMap.

## Results

- For `file` or `subpath` mounts, verify the ConfigMap data is available at the mount path:

  ``` bash
  $ cat /etc/my-config/settings.json
  ```

- For `env` mounts, verify the environment variables are set:

  ``` bash
  $ echo $LOG_LEVEL
  ```

**Related concepts**  

- [How credentials and configurations work in workspaces](develop-con_using_credentials_and_configurations_in_workspaces.md "Mount credentials and configurations into your workspaces so that tools such as Git, Maven, and cloud CLIs authenticate automatically without manual setup each time you start a workspace.")

**Related tasks**  

- [Mount Secrets](develop-proc_mounting_secrets.md "Mount Kubernetes Secrets into workspace containers to provide sensitive configuration data such as credentials, API keys, and certificates.")
- [Create an image pull Secret with oc](develop-proc_creating_image_pull_secrets.md "Create an image pull Secret with oc to allow Dev Workspace Pods to access container registries that require authentication.")
