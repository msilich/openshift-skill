> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/upgrade-assembly_plan_your_upgrade). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Plan your upgrade

Plan your OpenShift Dev Spaces upgrade by reviewing supported upgrade paths, choosing an update approval strategy, and completing the pre-upgrade checklist so that the upgrade proceeds without disruption.

<span id="assembly_plan-your-upgrade_devspaces___choose_your_upgrade_method"></span>

## [Choose your upgrade method](upgrade-assembly_plan_your_upgrade.md#assembly_plan-your-upgrade_devspaces___choose_your_upgrade_method)

OpenShift Dev Spaces supports three upgrade methods. Choose based on your cluster's network access and your preferred management workflow:

Web console  
Approve the pending Operator update in the OpenShift web console. Use this method when your cluster has direct internet access and you manage Operators through the Red Hat Ecosystem Catalog.

Command line (standard)  
Run `dsc server:update` on a cluster with internet access. Use this method when you automate deployments through scripts or CI/CD pipelines, or need to pass custom configuration during the upgrade.

Command line (air-gapped)  
Mirror container images to your private registry, then run `dsc server:update` with the `--che-operator-image` flag. Use this method when your cluster operates in a restricted network.

<span id="assembly_plan-your-upgrade_devspaces___impact_on_running_workspaces"></span>

## [Impact on running workspaces](upgrade-assembly_plan_your_upgrade.md#assembly_plan-your-upgrade_devspaces___impact_on_running_workspaces)

The upgrade replaces server component pods but does not automatically restart running workspaces. However, running workspaces can encounter errors during the rollout. To prevent data loss:

1.  Notify developers to save and push all uncommitted work.
2.  Stop all running workspaces before starting the upgrade.
3.  After the upgrade completes, developers start new workspaces with the updated components.

- **[How the upgrade works](upgrade-con_upgrade_overview.md)**  
  Understand what happens during an OpenShift Dev Spaces upgrade so that you can plan the timing, communicate downtime expectations, and verify the result.
- **[Choose how updates are applied](upgrade-proc_specifying_update_approval_strategy.md)**  
  Choose between automatic and manual update approval for the Red Hat OpenShift Dev Spaces Operator so that you control when new versions are installed on your cluster.
- **[Pre-upgrade checklist](upgrade-ref_pre_upgrade_checklist.md)**  
  Complete the following checklist before upgrading OpenShift Dev Spaces so that no work is lost and the upgrade proceeds without errors.
