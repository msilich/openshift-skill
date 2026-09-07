> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/upgrade-proc_upgrading_using_cli). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Upgrade by using the dsc management tool

Upgrade OpenShift Dev Spaces from the previous minor version by using the `dsc` management tool so that your deployment receives the latest bug fixes, security patches, and features.

## Before you begin

- You have an administrative account on OpenShift.
- You have a previous minor version of CodeReady Workspaces installed using the CLI management tool on the same instance of OpenShift, in the `openshift-devspaces` project.
- You have `dsc` for OpenShift Dev Spaces version 3.29 installed. See [Installing the dsc management tool](plan-proc_installing_the_dsc_management_tool.md).

## Procedure

1.  Save and push changes back to the Git repositories for all running CodeReady Workspaces 3.27 workspaces.

2.  Shut down all workspaces in the CodeReady Workspaces 3.27 instance.

3.  Upgrade OpenShift Dev Spaces:

    ``` bash
    $ dsc server:update -n openshift-devspaces
    ```

    Note

    For slow systems or internet connections, add the `--k8spodwaittimeout=1800000` flag option to extend the Pod timeout period to 1800000 ms or longer.

## Results

1.  Navigate to the OpenShift Dev Spaces instance.
2.  The 3.29 version number is visible at the bottom of the page.

**Related tasks**  

- [Choose how updates are applied](upgrade-proc_specifying_update_approval_strategy.md "Choose between automatic and manual update approval for the Red Hat OpenShift Dev Spaces Operator so that you control when new versions are installed on your cluster.")
- [Approve a pending update in the web console](upgrade-proc_upgrading_using_web_console.md "Approve a pending OpenShift Dev Spaces Operator update in the OpenShift web console so that your deployment receives the latest bug fixes, security patches, and features at the time you choose.")

**Related information**  

- [Installing the dsc management tool](plan-proc_installing_the_dsc_management_tool.md)
