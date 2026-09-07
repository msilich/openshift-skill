> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/install-proc_installing_dev_spaces_using_cli). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Deploy using the CLI

Deploy OpenShift Dev Spaces from the command line using the `dsc` management tool so that you have full control over configuration options and can automate the installation.

## Before you begin

- You have an OpenShift Container Platform 4.22 or later cluster.
- You have an active `oc` session with administrative permissions to the OpenShift cluster. See [Getting started with the OpenShift CLI](https://docs.openshift.com/container-platform/4.22/cli_reference/openshift_cli/getting-started-cli.html).
- You have the `dsc` management tool installed. See [Set up the dsc command-line tool](plan-proc_installing_the_dsc_management_tool.md).

## Procedure

1.  Optional: If you previously deployed OpenShift Dev Spaces on this OpenShift cluster, remove the previous OpenShift Dev Spaces instance:

    ``` bash
    $ dsc server:delete
    ```

2.  Create the OpenShift Dev Spaces instance:

    ``` bash
    $ dsc server:deploy --platform openshift
    ```

## Results

1.  Verify the OpenShift Dev Spaces instance status:

    ``` bash
    $ dsc server:status
    ```

2.  Navigate to the OpenShift Dev Spaces cluster instance:

    ``` bash
    $ dsc dashboard:open
    ```

Note

On ARM64 (AArch64) OpenShift clusters, you must override the gateway sidecar images after installing the Red Hat OpenShift Dev Spaces Operator, because the default images are not available for ARM64.

To patch the Red Hat OpenShift Dev Spaces Operator subscription, run the following commands:

``` bash
SUBSCRIPTION=$(oc get subscription -A \
  -o jsonpath='{.items[?(@.spec.name=="devspaces")]}')

SUBSCRIPTION_NAME=$(echo "$SUBSCRIPTION" | jq -r '.metadata.name')

SUBSCRIPTION_NAMESPACE=$(echo "$SUBSCRIPTION" | jq -r '.metadata.namespace')

oc patch subscription "$SUBSCRIPTION_NAME" \
  -n "$SUBSCRIPTION_NAMESPACE" \
  --type=merge \
  -p '{
    "spec": {
      "config": {
        "env": [
          {
            "name": "RELATED_IMAGE_gateway_authentication_sidecar",
            "value": "quay.io/openshift/origin-oauth-proxy:4.9"
          },
          {
            "name": "RELATED_IMAGE_gateway_authorization_sidecar",
            "value": "quay.io/openshift/origin-kube-rbac-proxy:4.9"
          }
        ]
      }
    }
  }'
```

- If `dsc server:deploy` fails with a permission error, verify that your `oc` session has the required cluster permissions. See [Permissions required for CLI installation](install-ref_permissions_to_install_devspaces_using_cli.md "Apply this ClusterRole to the installer’s service account or user to grant the minimum permissions required for a dsc-based installation of OpenShift Dev Spaces.").
- If `dsc server:deploy` reports that the namespace already exists, remove the previous OpenShift Dev Spaces instance first. See [Remove OpenShift Dev Spaces from your cluster](install-proc_uninstalling_dev_spaces.md "Remove OpenShift Dev Spaces and all related user data from your OpenShift cluster when you no longer need the platform or want to perform a clean reinstallation.").

**Related reference**  

- [Permissions required for CLI installation](install-ref_permissions_to_install_devspaces_using_cli.md "Apply this ClusterRole to the installer’s service account or user to grant the minimum permissions required for a dsc-based installation of OpenShift Dev Spaces.")
