<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Use the following information to diagnose and resolve network reconfiguration issues on single-node OpenShift clusters.

# Gather diagnostic information for network reconfiguration issues

You can gather diagnostic information to help troubleshoot network reconfiguration issues on single-node OpenShift clusters.

<div>

<div class="title">

Procedure

</div>

1.  Inspect the `IPConfig` custom resource (CR) status by running the following command:

    ``` terminal
    $ oc get ipc ipconfig -o yaml
    ```

    Review the `status.conditions` field for the current state, reason, and message. Check `status.validNextStages` for possible stage transitions, and `status.history` for timestamps of stage progression.

2.  View the Lifecycle Agent controller logs by running the following command:

    ``` terminal
    $ oc logs -n openshift-lifecycle-agent deployment/lifecycle-agent-controller-manager -c manager
    ```

3.  Create a debug session on the target node by running the following command:

    ``` terminal
    $ oc debug node/<node_name>
    # chroot /host
    ```

    - Replace `<node_name>` with the name of your single-node OpenShift node.

4.  View the relevant service logs depending on which phase you are troubleshooting by running one of the following commands:

    - View the logs for pre-pivot issues by running the following command:

      ``` terminal
      $ sudo journalctl -u lca-ipconfig-pre-pivot -b --no-pager
      ```

    - View the logs for post-pivot issues by running the following command:

      ``` terminal
      $ sudo journalctl -u ip-configuration.service -b --no-pager
      ```

    - View the logs for `init-monitor` watchdog issues by running the following command:

      ``` terminal
      $ sudo journalctl -u lca-init-monitor.service -b --no-pager
      ```

    - View the logs for rollback issues by running the following command:

      ``` terminal
      $ sudo journalctl -u lca-ipconfig-rollback -b --no-pager
      ```

</div>

# Network reconfiguration troubleshooting reference

Use the following reference information to help diagnose and resolve network reconfiguration issues on single-node OpenShift clusters.

| File | Description |
|----|----|
| `/var/lib/lca/workspace/ip-config-pre-pivot.json` | Pre-pivot configuration data |
| `/var/lib/lca/workspace/ip-config-post-pivot.json` | Post-pivot configuration data |
| `/var/lib/lca/workspace/nmstate.yaml` | Generated `nmstate` configuration for network changes |
| `/var/lib/lca/workspace/recert_config.json` | Configuration for certificate regeneration |
| `/var/lib/lca/workspace/ip-config-autorollback-config.json` | Auto-rollback configuration |
| `/var/lib/lca/workspace/recert-pull-secret.json` | Pull secret for the recert image, if a custom pull secret was specified |
| `/var/lib/lca/ipc.json` | Persistence file that stores `IPConfig` state for rollback and status continuity across restarts |

On-node artifacts for troubleshooting

| Issue | Cause | Solution |
|----|----|----|
| Stage transition rejected | You attempted to transition to a stage not in `status.validNextStages`. | Check `status.validNextStages` and only transition to an allowed stage. |
| Specification fields cannot be changed | You attempted to modify `spec` fields while the CR is not in the `Idle` stage. | Wait for the current operation to complete and the CR to return to `Idle`. |
| Health checks never pass | Cluster health blockers are preventing progress. | Investigate cluster health issues. |
| Post-pivot phase failed | An error occurred during network configuration or certificate regeneration. | Review the post-pivot service logs. If auto-rollback is enabled, the node automatically reverts. Otherwise, manually trigger rollback by setting `spec.stage: Rollback`. |
| Pods not receiving new IP family | Pre-existing pods might not automatically receive an IP address from the new family because of CNI behavior. | Delete and re-create the affected pods to obtain addresses from the new IP family. |
| Configuration stuck in disconnected environment | The Lifecycle Agent or recert container might be attempting to pull images not available in the disconnected registry. | Ensure all required images are mirrored to your disconnected registry before starting. Verify the `lca.openshift.io/recert-pull-secret` annotation references a valid pull secret. |

Common failure patterns

<div>

<div class="title">

Additional resources

</div>

- [Gathering data about your cluster](../../support/gathering-cluster-data.md#gathering-cluster-data)

</div>
