> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/get_started-proc_verify_the_platform_end_to_end). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Verify the platform works end-to-end

Verify that OpenShift Dev Spaces is operational by checking the Operator status, opening the dashboard, and creating a test workspace. This confirms that the full pipeline works before you invite developers.

## Before you begin

- You have an active `oc` session with administrative permissions to the OpenShift cluster. See [Getting started with the CLI](https://docs.openshift.com/container-platform/4.22/cli_reference/openshift_cli/getting-started-cli.html).
- You have installed OpenShift Dev Spaces on an OpenShift cluster. See [Install OpenShift Dev Spaces](install-assembly_installing_dev_spaces.md).

## Procedure

1.  Verify that the OpenShift Dev Spaces Operator pod is running:

    ``` bash
    $ oc get pods -n openshift-operators -l app.kubernetes.io/component=devspaces-operator
    ```

    Note The Operator pod runs in the `openshift-operators` namespace (where the Subscription was created), not in the `openshift-devspaces` namespace.

2.  Verify that the `CheCluster` custom resource reports no errors:

    ``` bash
    $ oc get checluster devspaces -n openshift-devspaces -o jsonpath='{.status.chePhase}'
    ```

    The expected output is `Active`.

3.  Retrieve the OpenShift Dev Spaces dashboard URL:

    ``` bash
    $ oc get checluster devspaces -n openshift-devspaces -o jsonpath='{.status.cheURL}'
    ```

4.  Open the URL in a web browser and log in with your OpenShift credentials.

5.  On the **Create Workspace** page, click any sample (for example, **Python**) to start a test workspace.

6.  Wait for the workspace to start. The first start takes 2-3 minutes while container images are pulled to the cluster node.

7.  Confirm that the IDE loads in your browser tab and that you can open a terminal.

8.  Return to the **Workspaces** page and stop the test workspace by selecting **⋮** \> **Stop Workspace**.

## Results

- The OpenShift Dev Spaces dashboard loads and displays the **Create Workspace** page.
- A test workspace starts and the IDE loads in the browser.
- You can open a terminal in the workspace.

**Related information**  

- [Confirm OpenShift Dev Spaces is running](install-proc_verifying_the_installation.md)
- [Get the dashboard URL to share with your team](install-proc_finding_the_fqdn.md)
