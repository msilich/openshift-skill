> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/get_started-ref_basic_actions_on_a_workspace). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Manage your cloud development environments

Stop, restart, and delete cloud development environments from the OpenShift Dev Spaces dashboard to control resource usage and keep your environment organized. Access the **Workspaces** page at `https://`*`<openshift_dev_spaces_fqdn>`*`/dashboard/#/workspaces`.

<span id="ref_basic-actions-on-a-workspace_devspaces__entry__1"></span><span id="ref_basic-actions-on-a-workspace_devspaces__entry__2"></span>

| Action | GUI steps in the **Workspaces** page |
|----|----|
| *Reopen a running cloud development environment* | Click **Open**. |
| *Restart a running cloud development environment* | Go to **⋮\>Restart Workspace**. |
| *Stop a running cloud development environment* | Go to **⋮\>Stop Workspace**. |
| *Start a stopped cloud development environment* | Click **Open**. |
| *Delete a cloud development environment* | Go to **⋮\>Delete Workspace**. |

Table 1. Cloud development environment actions

Note Each cloud development environment is an OpenShift `DevWorkspace` custom resource. You can also manage cloud development environments from the command line with `oc`. See [How workspaces connect to OpenShift](integrate-con_integrating_with_openshift.md).
