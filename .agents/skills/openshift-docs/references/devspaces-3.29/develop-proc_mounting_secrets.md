> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/develop-proc_mounting_secrets). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Mount Secrets

Mount Kubernetes Secrets into workspace containers to provide sensitive configuration data such as credentials, API keys, and certificates.

## Before you begin

- You have an active `oc` session with your project. See [Getting started with the CLI](https://docs.openshift.com/container-platform/4.22/cli_reference/openshift_cli/getting-started-cli.html). Warning

  By default, applying a `Secret` with the `controller.devfile.io/mount-to-devworkspace: 'true'` label restarts all running workspaces in the project. To mount the Secret only at workspace start and prevent automatic restarts, add the `controller.devfile.io/mount-on-start: 'true'` annotation.

## Procedure

1.  Create a Secret with the required labels and annotations:

    ``` yaml
    kind: Secret
    apiVersion: v1
    metadata:
      name: my-credentials
      labels:
        controller.devfile.io/mount-to-devworkspace: 'true'
        controller.devfile.io/watch-secret: 'true'
      annotations:
        controller.devfile.io/mount-as: file
        controller.devfile.io/mount-path: /etc/my-credentials
    type: Opaque
    data:
      api-key: <base64_encoded_api_key>
    ```

    where:

    controller.devfile.io/mount-to-devworkspace  
    Required label to mount the Secret to all workspaces.

    controller.devfile.io/watch-secret  
    Watch the Secret for changes and update mounted files.

    controller.devfile.io/mount-as  
    Mount type: `file`, `subpath`, or `env`.

    controller.devfile.io/mount-path  
    Path where the Secret data is mounted.

2.  Apply the Secret to your project:

    ``` bash
    $ oc apply -f my-credentials.yaml -n <your_namespace>
    ```

3.  Optional: Add annotations to the Secret to customize the mounting behavior. <span id="mounting-secrets_devspaces__entry__1"></span><span id="mounting-secrets_devspaces__entry__2"></span>

    | Annotation | Description |
    |----|----|
    | `controller.devfile.io/mount-path: `*`<path>`* | Overrides the default mount path. The default mount path is `/etc/secret/`*`<Secret_name>`*. |
    | `controller.devfile.io/mount-as: file` | Each key in the Secret data becomes a file in the mount path directory. |
    | `controller.devfile.io/mount-as: subpath` | Similar to `file`, but uses subPath volumes for better compatibility. |
    | `controller.devfile.io/mount-as: env` | Each key-value pair becomes an environment variable in all workspace containers. |
    | `controller.devfile.io/mount-on-start: 'true'` | When set to `true`, the Secret is mounted only when a workspace starts, not while it is already running. This prevents workspace restarts when the Secret is created. |
    | `controller.devfile.io/mount-to-devworkspace-include:` | Specifies a comma-separated list of `Dev Workspace` name patterns. When set, the Secret is mounted only to workspaces whose names match at least one pattern. |
    | `controller.devfile.io/mount-to-devworkspace-exclude:` | Specifies a comma-separated list of `Dev Workspace` name patterns. When set, the Secret is mounted to all workspaces except those whose names match a pattern. |

    Table 1. Secret mounting annotations

    Note

    When both `controller.devfile.io/mount-to-devworkspace-include` and `controller.devfile.io/mount-to-devworkspace-exclude` annotations are set, the Secret is mounted only to workspaces that match the include pattern and do not match the exclude pattern.

    For example, to mount Secret data as environment variables:

    ``` yaml
    kind: Secret
    apiVersion: v1
    metadata:
      name: my-env-secret
      labels:
        controller.devfile.io/mount-to-devworkspace: 'true'
        controller.devfile.io/watch-secret: 'true'
      annotations:
        controller.devfile.io/mount-as: env
    type: Opaque
    stringData:
      DATABASE_URL: postgresql://localhost:5432/mydb
      API_SECRET: my-secret-key
    ```

    For example, to mount a Maven `settings.xml` file to the `/home/user/.m2/` path using `subpath`:

    ``` yaml
    kind: Secret
    apiVersion: v1
    metadata:
      name: maven-settings
      labels:
        controller.devfile.io/mount-to-devworkspace: 'true'
        controller.devfile.io/watch-secret: 'true'
      annotations:
        controller.devfile.io/mount-path: /home/user/.m2/
        controller.devfile.io/mount-as: subpath
    type: Opaque
    stringData:
      settings.xml: |
        <settings xmlns="http://maven.apache.org/SETTINGS/1.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
          xsi:schemaLocation="http://maven.apache.org/SETTINGS/1.0.0 https://maven.apache.org/xsd/settings-1.0.0.xsd">
        </settings>
    ```

    After the workspace starts, the `/home/user/.m2/settings.xml` file is available in the `Dev Workspace` containers. To use a custom path with Maven, run `mvn --settings /home/user/.m2/settings.xml clean install`.

4.  Start or restart your workspace to apply the mounted Secret.

## Results

- For `file` or `subpath` mounts, verify the Secret data is available at the mount path:

  ``` bash
  $ ls /etc/my-credentials
  ```

- For `env` mounts, verify the environment variables are set:

  ``` bash
  $ echo $DATABASE_URL
  ```

**Related concepts**  

- [How credentials and configurations work in workspaces](develop-con_using_credentials_and_configurations_in_workspaces.md "Mount credentials and configurations into your workspaces so that tools such as Git, Maven, and cloud CLIs authenticate automatically without manual setup each time you start a workspace.")

**Related tasks**  

- [Configure an AI provider API key](develop-proc_configuring_an_ai_provider_api_key.md "Configure an AI provider API key so that it is automatically injected as an environment variable into all your workspaces.")
- [Create an image pull Secret with oc](develop-proc_creating_image_pull_secrets.md "Create an image pull Secret with oc to allow Dev Workspace Pods to access container registries that require authentication.")

**Related information**  

- [Use a Git provider access token](get_started-proc_using_a_git_provider_access_token.md)
