> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/troubleshoot-proc_viewing_workspace_logs_in_openshift_console). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# View workspace logs in OpenShift console

View OpenShift Dev Spaces workspace logs in the OpenShift web console to diagnose startup failures and runtime errors from the Administrator perspective.

## Before you begin

- You have an active `oc` session with administrative permissions to the OpenShift cluster. See [Getting started with the CLI](https://docs.openshift.com/container-platform/4.22/cli_reference/openshift_cli/getting-started-cli.html).
- You have a running OpenShift Dev Spaces workspace.

## Procedure

1.  In the OpenShift Dev Spaces dashboard, go to **Workspaces**.
2.  Click a workspace name to display the workspace overview page. This page displays the OpenShift project name *\<project_name\>*.
3.  Click the upper right **Applications** menu, and click the OpenShift console link.
4.  Run the next steps in the OpenShift console, in the **Administrator** perspective.
5.  Click **Workloads** \> **Pods** to see a list of all the active workspaces.
6.  In the **Project** drop-down menu, select the *\<project_name\>* project to narrow the search.
7.  Click the name of the running pod that runs the workspace. The **Details** tab contains the list of all containers with additional information.
8.  Go to the **Logs** tab.

## Results

- The **Logs** tab displays container logs for the workspace Pod.

**Related concepts**  

- [Diagnose slow Cloud Development Environments](troubleshoot-con_diagnose_slow_cdes.md "Diagnose slow Cloud Development Environment startup by pre-pulling images, tuning storage strategy, installing offline, and reducing public endpoints.")

**Related tasks**  

- [View workspace logs in CLI](troubleshoot-proc_viewing_workspace_logs_in_cli.md "View OpenShift Dev Spaces workspace logs from the OpenShift command-line interface (CLI) to troubleshoot startup failures and runtime errors.")

**Related information**  

- [Fix webview loading errors in private browsing](troubleshoot-con_troubleshooting_webview_loading_error.md)
