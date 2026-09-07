> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/install-proc_verifying_the_installation). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Confirm OpenShift Dev Spaces is running

Confirm that OpenShift Dev Spaces is operational before you onboard users by checking the Operator pod, the `CheCluster` status, and the dashboard URL.

## Before you begin

- You have installed OpenShift Dev Spaces on an OpenShift cluster.
- You have an active `oc` session with administrative permissions to the OpenShift cluster.

## Procedure

1.  Verify that the OpenShift Dev Spaces Operator pod is running:

    ``` bash
    oc get pods --all-namespaces -l app.kubernetes.io/component=devspaces-operator
    ```

    Note

    On OpenShift, the Operator pod runs in the namespace where the Subscription was created (typically `openshift-operators` for a cluster-wide installation), not in `openshift-devspaces`.

2.  Verify that the `CheCluster` custom resource reports no errors:

    ``` bash
    oc get checluster devspaces -n openshift-devspaces -o jsonpath='{.status.chePhase}'
    ```

    The expected output is `Active`.

3.  Retrieve the OpenShift Dev Spaces dashboard URL:

    ``` bash
    oc get checluster devspaces -n openshift-devspaces -o jsonpath='{.status.cheURL}'
    ```

4.  Open the URL in a web browser and log in with your OpenShift credentials.

## Results

- The OpenShift Dev Spaces dashboard loads and displays the **Create Workspace** page.

**Related tasks**  

- [Deploy using the CLI](install-proc_installing_dev_spaces_using_cli.md "Deploy OpenShift Dev Spaces from the command line using the dsc management tool so that you have full control over configuration options and can automate the installation.")
- [Deploy using the web console](install-proc_installing_dev_spaces_using_web_console.md "Deploy OpenShift Dev Spaces through the OpenShift web console using the standard OperatorHub workflow so that you can install without command-line access.")
