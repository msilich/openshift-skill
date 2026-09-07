> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/troubleshoot-ref_viewing_devspaces_workspaces_logs). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Cloud Development Environment logs

OpenShift Dev Spaces workspace logs capture IDE extension activity, container memory events, and process errors. Review these logs to diagnose workspace failures, debug misbehaving extensions, and identify memory issues.

An IDE extension misbehaves or needs debugging  
The logs list the plugins that have been loaded by the editor.

The container runs out of memory  
The logs contain an `OOMKilled` error message. Processes running in the container attempted to request more memory than is configured to be available to the container.

A process runs out of memory  
The logs contain an error message such as `OutOfMemoryException`. A process inside the container ran out of memory without the container noticing.

**Related tasks**  

- [View workspace logs in CLI](troubleshoot-proc_viewing_workspace_logs_in_cli.md "View OpenShift Dev Spaces workspace logs from the OpenShift command-line interface (CLI) to troubleshoot startup failures and runtime errors.")

**Related information**  

- [View workspace logs in OpenShift console](troubleshoot-proc_viewing_workspace_logs_in_openshift_console.md)
- [View language server and debug adapter logs in the editor](https://access.redhat.com/documentation/en-us/red_hat_openshift_dev_spaces/3.29/html-single/troubleshoot_workspaces/index#proc_viewing-language-server-logs-in-editor_troubleshoot_workspaces)
