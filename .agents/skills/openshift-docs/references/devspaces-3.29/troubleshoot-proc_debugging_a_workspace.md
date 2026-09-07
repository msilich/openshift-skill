> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/troubleshoot-proc_debugging_a_workspace). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Debug a failing workspace

Debug a failing workspace by starting it in debug mode. Debug mode keeps containers running after `postStart` command failures, giving you time to inspect logs and diagnose the issue.

## Before you begin

- You have a running OpenShift Dev Spaces instance.
- You have access to the OpenShift Dev Spaces dashboard.

## About this task

When debug mode is enabled:

- If a `postStart` lifecycle command fails, the container sleeps instead of terminating, giving you time to connect and inspect the failure.
- Logs from `postStart` commands are written to `/tmp/poststart-stdout.txt` and `/tmp/poststart-stderr.txt` inside the workspace container.
- The workspace deployment remains available for the duration of the configured `progressTimeout` (default: 5 minutes) before scaling down.

## Procedure

1.  In the OpenShift Dev Spaces dashboard, go to the **Workspaces** page.

2.  To start a stopped workspace in debug mode, click the kebab menu (**⋮**) for the workspace and select **Open in Debug mode**. To restart a running workspace in debug mode, click the kebab menu (**⋮**) for the workspace and select **Restart in Debug mode**.

    The workspace starts with the `controller.devfile.io/debug-start` annotation set to `true`, and the **Logs** tab opens.

3.  Wait for the workspace to report a failure in the **Logs** tab. Look for error messages or status conditions indicating startup problems. If no failure occurs within the `progressTimeout` period (default: 5 minutes), the workspace will scale down automatically.

4.  Use `oc` to exec into the workspace container:

    ``` bash
    $ oc exec --namespace='<workspace_namespace>' \
      deploy/workspace<workspace_id> -- /bin/bash
    ```

5.  Review the `postStart` command logs:

    ``` bash
    $ cat /tmp/poststart-stderr.txt
    $ cat /tmp/poststart-stdout.txt
    ```

## Results

- In the **Logs** tab, verify that the workspace status conditions include the message `DevWorkspace is starting in debug mode`.
- If a `postStart` command fails, verify that the container remains running and that `/tmp/poststart-stderr.txt` contains the failure details.

Important

The `controller.devfile.io/debug-start` annotation is managed by the OpenShift Dev Spaces dashboard. Manually patching this annotation on a DevWorkspace resource using `oc` will not persist, because the dashboard reconciles the annotation on every start or restart operation.

Always use the dashboard actions described above to enable debug mode.

**Related tasks**  

- [View workspace logs in CLI](troubleshoot-proc_viewing_workspace_logs_in_cli.md "View OpenShift Dev Spaces workspace logs from the OpenShift command-line interface (CLI) to troubleshoot startup failures and runtime errors.")

**Related reference**  

- [Cloud Development Environment logs](troubleshoot-ref_viewing_devspaces_workspaces_logs.md "OpenShift Dev Spaces workspace logs capture IDE extension activity, container memory events, and process errors. Review these logs to diagnose workspace failures, debug misbehaving extensions, and identify memory issues.")
