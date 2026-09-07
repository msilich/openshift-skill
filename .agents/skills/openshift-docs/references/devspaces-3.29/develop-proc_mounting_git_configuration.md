> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/develop-proc_mounting_git_configuration). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Mount Git configuration

Mount your Git configuration into workspaces to set your Git identity and preferences.

## Before you begin

- You have an active `oc` session with your project. See [Getting started with the CLI](https://docs.openshift.com/container-platform/4.22/cli_reference/openshift_cli/getting-started-cli.html).

## About this task

Note

The `user.name` and `user.email` fields are set automatically to the `gitconfig` content from a git provider that is connected to OpenShift Dev Spaces. This connection requires a [Git-provider access token](get_started-proc_using_a_git_provider_access_token.md) or a token generated via OAuth, and you must set the username and email on the provider’s user profile page.

## Procedure

1.  Create a ConfigMap with your Git configuration:

    ``` yaml
    kind: ConfigMap
    apiVersion: v1
    metadata:
      name: workspace-userdata-gitconfig-configmap
      labels:
        controller.devfile.io/mount-to-devworkspace: 'true'
        controller.devfile.io/watch-configmap: 'true'
      annotations:
        controller.devfile.io/mount-as: subpath
        controller.devfile.io/mount-path: /home/user
    data:
      .gitconfig: |
        [user]
          name = Your Name
          email = your.email@example.com
        [core]
          editor = vim
        [pull]
          rebase = true
    ```

2.  Apply the ConfigMap to your project:

    ``` bash
    $ oc apply -f gitconfig.yaml -n <your_namespace>
    ```

3.  Start or restart your workspace.

## Results

1.  Open a terminal in your workspace.

2.  Verify the Git configuration:

    ``` bash
    $ git config --list
    ```

**Related concepts**  

- [How credentials and configurations work in workspaces](develop-con_using_credentials_and_configurations_in_workspaces.md "Mount credentials and configurations into your workspaces so that tools such as Git, Maven, and cloud CLIs authenticate automatically without manual setup each time you start a workspace.")

**Related tasks**  

- [Mount Secrets](develop-proc_mounting_secrets.md "Mount Kubernetes Secrets into workspace containers to provide sensitive configuration data such as credentials, API keys, and certificates.")
- [Create an image pull Secret with oc](develop-proc_creating_image_pull_secrets.md "Create an image pull Secret with oc to allow Dev Workspace Pods to access container registries that require authentication.")
