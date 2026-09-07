> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/develop-proc_creating_image_pull_secrets). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Create an image pull Secret with `oc`

Create an image pull Secret with `oc` to allow `Dev Workspace` Pods to access container registries that require authentication.

## Before you begin

- You have an active `oc` session with administrative permissions to the OpenShift cluster. See [Getting started with the CLI](https://docs.openshift.com/container-platform/4.22/cli_reference/openshift_cli/getting-started-cli.html).

## Procedure

1.  In your user project, create an image pull Secret with your private container registry details and credentials:

    ``` bash
    $ oc create secret docker-registry <Secret_name> \
        --docker-server=<registry_server> \
        --docker-username=<username> \
        --docker-password=<password> \
        --docker-email=<email_address>
    ```

2.  Add the required labels to the image pull Secret:

    ``` bash
    $ oc label secret <Secret_name> controller.devfile.io/devworkspace_pullsecret=true controller.devfile.io/watch-secret=true
    ```

## Results

- Verify the Secret exists and has the required labels:

  ``` bash
  $ oc get secret <Secret_name> --show-labels
  ```

**Related concepts**  

- [How credentials and configurations work in workspaces](develop-con_using_credentials_and_configurations_in_workspaces.md "Mount credentials and configurations into your workspaces so that tools such as Git, Maven, and cloud CLIs authenticate automatically without manual setup each time you start a workspace.")

**Related tasks**  

- [Create an image pull Secret from a .dockercfg file](develop-proc_creating_image_pull_secret_from_dockercfg.md "Create an image pull Secret from an existing .dockercfg file to allow Dev Workspace Pods to access container registries that require authentication.")
- [Create an image pull Secret from a config.json file](develop-proc_creating_image_pull_secret_from_config_json.md "Create an image pull Secret from an existing $HOME/.docker/config.json file to allow Dev Workspace Pods to access container registries that require authentication.")
- [Mount Secrets](develop-proc_mounting_secrets.md "Mount Kubernetes Secrets into workspace containers to provide sensitive configuration data such as credentials, API keys, and certificates.")
