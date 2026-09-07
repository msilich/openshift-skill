> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/install-proc_installing_dev_spaces_using_web_console). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Deploy using the web console

Deploy OpenShift Dev Spaces through the OpenShift web console using the standard OperatorHub workflow so that you can install without command-line access.

## Before you begin

- You have an OpenShift web console session as a cluster administrator. See [Accessing the web console](https://docs.openshift.com/container-platform/4.22/web_console/web-console.html).
- You have an active `oc` session with administrative permissions to the OpenShift cluster. See [Getting started with the OpenShift CLI](https://docs.openshift.com/container-platform/4.22/cli_reference/openshift_cli/getting-started-cli.html).
- For a repeat installation: you have uninstalled the previous OpenShift Dev Spaces instance according to [Remove OpenShift Dev Spaces from your cluster](install-proc_uninstalling_dev_spaces.md "Remove OpenShift Dev Spaces and all related user data from your OpenShift cluster when you no longer need the platform or want to perform a clean reinstallation.").

## Procedure

1.  In the **Administrator** view of the OpenShift web console, go to **Operators** **OperatorHub** and search for `Red Hat OpenShift Dev Spaces`.

2.  Install the Red Hat OpenShift Dev Spaces Operator. Tip

    See [Installing from OperatorHub using the web console](https://docs.openshift.com/container-platform/4.22/operators/admin/olm-adding-operators-to-cluster.html#olm-installing-from-operatorhub-using-web-console_olm-adding-operators-to-a-cluster).

    Important

    The Red Hat OpenShift Dev Spaces Operator depends on the Dev Workspace Operator. If you install the Red Hat OpenShift Dev Spaces Operator manually to a non-default namespace, ensure that the Dev Workspace Operator is also installed in the same namespace. The Operator Lifecycle Manager installs the Dev Workspace Operator as a dependency within the Red Hat OpenShift Dev Spaces Operator namespace. If the Dev Workspace Operator is already installed in a different namespace, two conflicting installations can result.

    Important

    If you want to onboard [Web Terminal Operator](https://docs.openshift.com/container-platform/4.22/web_console/web_terminal/installing-web-terminal.html) on the cluster, use the same installation namespace as the Red Hat OpenShift Dev Spaces Operator. Both operators depend on the Dev Workspace Operator, so all three must be installed in the same namespace.

3.  Create the `openshift-devspaces` namespace:

    ``` bash
    oc create namespace openshift-devspaces
    ```

4.  Go to **Operators** **Installed Operators** **Red Hat OpenShift Dev Spaces instance Specification** **Create CheCluster** **YAML view**.

5.  In the **YAML view**, replace `namespace: openshift-operators` with `namespace: openshift-devspaces`.

6.  Select **Create**. Tip

    See [Creating applications from installed Operators](https://docs.openshift.com/container-platform/4.22/operators/user/olm-creating-apps-from-installed-operators.html).

## Results

1.  In **Red Hat OpenShift Dev Spaces instance Specification**, go to **devspaces**, landing on the **Details** tab.

<!-- -->

1.  Under **Message**, check that there is **None**, which means no errors.
2.  Under **Red Hat OpenShift Dev Spaces URL**, wait until the URL of the OpenShift Dev Spaces instance appears, and then open the URL to check the OpenShift Dev Spaces dashboard.
3.  In the **Resources** tab, view the resources for the OpenShift Dev Spaces deployment and their status.

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

- If the Operator installation fails, verify that your account has the required cluster permissions. See [Permissions required for web console installation](install-ref_permissions_to_install_devspaces_using_web_console.md "Install OpenShift Dev Spaces through the OpenShift web console with a specific set of cluster permissions. Apply this ClusterRole to the installer’s service account or user to grant the minimum required permissions for web console installation.").
- If the `CheCluster` resource reports errors, verify that the Dev Workspace Operator is installed in the same namespace as the Red Hat OpenShift Dev Spaces Operator.

**Related reference**  

- [Permissions required for web console installation](install-ref_permissions_to_install_devspaces_using_web_console.md "Install OpenShift Dev Spaces through the OpenShift web console with a specific set of cluster permissions. Apply this ClusterRole to the installer’s service account or user to grant the minimum required permissions for web console installation.")
