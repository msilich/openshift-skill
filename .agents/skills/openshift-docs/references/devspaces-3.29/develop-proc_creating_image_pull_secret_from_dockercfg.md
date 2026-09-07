> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/develop-proc_creating_image_pull_secret_from_dockercfg). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Create an image pull Secret from a `.dockercfg` file

Create an image pull Secret from an existing `.dockercfg` file to allow `Dev Workspace` Pods to access container registries that require authentication.

## Before you begin

- You have an active `oc` session with administrative permissions to the OpenShift cluster. See [Getting started with the CLI](https://docs.openshift.com/container-platform/4.22/cli_reference/openshift_cli/getting-started-cli.html).
- You have [`base64`](https://www.gnu.org/software/coreutils/base64) command-line tools installed.

## Procedure

1.  Encode the `.dockercfg` file to Base64:

    ``` bash
    $ cat .dockercfg | base64 | tr -d '\n'
    ```

2.  Create a new OpenShift Secret in your user project:

    ``` yaml
    apiVersion: v1
    kind: Secret
    metadata:
      name: <Secret_name>
      labels:
        controller.devfile.io/devworkspace_pullsecret: 'true'
        controller.devfile.io/watch-secret: 'true'
    data:
      .dockercfg: <Base64_content_of_.dockercfg>
    type: kubernetes.io/dockercfg
    ```

3.  Apply the Secret:

    ``` bash
    $ oc apply -f - <<EOF
    <Secret_prepared_in_the_previous_step>
    EOF
    ```

## Results

- Verify the Secret exists and has the required labels:

  ``` bash
  $ oc get secret <Secret_name> --show-labels
  ```

**Related concepts**  

- [How credentials and configurations work in workspaces](develop-con_using_credentials_and_configurations_in_workspaces.md "Mount credentials and configurations into your workspaces so that tools such as Git, Maven, and cloud CLIs authenticate automatically without manual setup each time you start a workspace.")

**Related tasks**  

- [Create an image pull Secret with oc](develop-proc_creating_image_pull_secrets.md "Create an image pull Secret with oc to allow Dev Workspace Pods to access container registries that require authentication.")
- [Create an image pull Secret from a config.json file](develop-proc_creating_image_pull_secret_from_config_json.md "Create an image pull Secret from an existing $HOME/.docker/config.json file to allow Dev Workspace Pods to access container registries that require authentication.")
- [Mount Secrets](develop-proc_mounting_secrets.md "Mount Kubernetes Secrets into workspace containers to provide sensitive configuration data such as credentials, API keys, and certificates.")
