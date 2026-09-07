> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/upgrade-ref_pre_upgrade_checklist). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Pre-upgrade checklist

Complete the following checklist before upgrading OpenShift Dev Spaces so that no work is lost and the upgrade proceeds without errors.

<span id="ref_pre-upgrade-checklist_devspaces__entry__1"></span><span id="ref_pre-upgrade-checklist_devspaces__entry__2"></span>

| Step | Action |
|----|----|
| 1 | Review the [OpenShift Dev Spaces 3.29 release notes](https://access.redhat.com/documentation/en-us/red_hat_openshift_dev_spaces/3.29/html-single/release_notes/) for breaking changes and new features. |
| 2 | Verify that your OpenShift cluster version is between 4.16 and 4.22. |
| 3 | Notify developers to save and push all uncommitted work in their running workspaces. |
| 4 | Stop all running workspaces. The upgrade does not automatically stop workspaces, and running workspaces might encounter errors during the upgrade. |
| 5 | If you plan to upgrade from the command line, install `dsc` version 3.29. See [Set up the dsc command-line tool](plan-proc_installing_the_dsc_management_tool.md). |
| 6 | Verify the current OpenShift Dev Spaces Operator subscription and update approval strategy. See [Choose how updates are applied](upgrade-proc_specifying_update_approval_strategy.md "Choose between automatic and manual update approval for the Red Hat OpenShift Dev Spaces Operator so that you control when new versions are installed on your cluster."). |
