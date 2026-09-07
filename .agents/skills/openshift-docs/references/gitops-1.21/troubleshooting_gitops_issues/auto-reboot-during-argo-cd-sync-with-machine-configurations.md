<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

When using the Machine Config Operator (MCO) with Argo CD GitOps workflows, node reboots triggered by machine configuration changes can interrupt application synchronization and impact performance. This can occur when the MCO reboots a node that hosts the Argo CD application controller, terminating an active sync operation. Prevent these interruptions and ensure that the MCO and Argo CD work together reliably.

# Enhance performance in machine configurations and Argo CD

Using the Machine Config Operator (MCO) with Argo CD GitOps workflows can impact performance when node reboots interrupt synchronization operations.

## Problem description

The following sequence leads to synchronization failures and performance degradation:

1.  Argo CD starts an automated sync after a commit to the Git repository that contains application resources.

2.  If Argo CD detects a new or updated machine configuration during the sync, the MCO applies the change and begins rebooting nodes.

3.  If a rebooting node hosts the Argo CD application controller, the controller stops and the sync is aborted.

Because the MCO reboots nodes sequentially and Argo CD workloads can be rescheduled during each reboot, synchronization takes significant time to complete. This results in unpredictable behavior until the MCO finishes rebooting all affected nodes.

## Solution

To prevent node reboots from interrupting Argo CD sync operations, use one of the following approaches:

- **Sync waves**: Configure Argo CD sync waves to apply machine configurations in a separate phase from application resources.

- **Manual sync**: Disable automatic syncing for machine configurations and trigger syncs during maintenance windows.

- **Resource hooks**: Use Argo CD resource hooks to control when machine configurations are applied.

For implementation details, see the additional resources section.

# Additional resources

- [Preventing nodes from auto-rebooting during Argo CD sync with machine configs](https://developers.redhat.com/articles/2021/12/20/prevent-auto-reboot-during-argo-cd-sync-machine-configs#)
