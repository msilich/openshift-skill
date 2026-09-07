<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

If a cluster update gets stuck, fails, or results in degraded cluster Operators, use the following diagnostic procedures to identify the root cause and take corrective action.

# Diagnosing a ClusterGroupUpgrade CR stuck in Preparing state

If a `ClusterGroupUpgrade` custom resource (CR) is stuck in the `Preparing` state, the issue is typically related to policy compliance, cluster readiness, or blocking custom resources.

<div>

<div class="title">

Prerequisites

</div>

- You have a `ClusterGroupUpgrade` CR that is stuck in `Preparing` state.

- You have access to the Red Hat Advanced Cluster Management (RHACM) hub cluster with cluster-admin privileges.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Check the `ClusterGroupUpgrade` status by running the following command:

    ``` terminal
    $ oc get cgu <cgu_name> -n <namespace> -o yaml
    ```

    Look for error messages in the `status.conditions` section. Common causes include managed policies that do not exist or are not bound to target clusters, target clusters that are not in a ready state, and blocking custom resources that are not ready.

2.  Check policy compliance in RHACM by running the following command:

    ``` terminal
    $ oc get policy <policy_name> -n <namespace>
    ```

3.  Check policy details for noncompliant policies by running the following command:

    ``` terminal
    $ oc describe policy <policy_name> -n <namespace>
    ```

    Resolve policy compliance issues before the `ClusterGroupUpgrade` CR can proceed.

</div>

# Diagnosing a ClusterGroupUpgrade CR that failed on some clusters

If a `ClusterGroupUpgrade` custom resource (CR) completes but some clusters show a `failed` status, investigate the failed clusters individually to identify the root cause.

<div>

<div class="title">

Prerequisites

</div>

- You have a `ClusterGroupUpgrade` CR that shows failed clusters.

- You have access to the Red Hat Advanced Cluster Management (RHACM) hub cluster with cluster-admin privileges.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Check detailed cluster status in the `ClusterGroupUpgrade` CR by running the following command:

    ``` terminal
    $ oc get cgu <cgu_name> -n <namespace> -o jsonpath='{.status.clusters}'
    ```

    The following example shows the output:

    ``` json
    {
      "spoke1": "complete",
      "spoke2": "failed",
      "spoke3": "inprogress"
    }
    ```

2.  Check TALM logs for errors related to the failed clusters by running the following command:

    ``` terminal
    $ oc logs -n openshift-operators deployment/cluster-group-upgrades-controller-manager
    ```

3.  Check policy violation events on the failed cluster by running the following command:

    ``` terminal
    $ oc --context=<failed_cluster> get events -A --sort-by='.lastTimestamp' | tail -20
    ```

</div>

# Diagnosing degraded cluster Operators during an update

If a cluster Operator becomes degraded during an update, identify the affected Operator and investigate the root cause.

Common Operators that degrade during updates include `authentication`, `console`, `monitoring`, and `network`.

<div>

<div class="title">

Prerequisites

</div>

- You have a cluster update in progress with one or more degraded Operators.

- You have access to the target cluster with cluster-admin privileges.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Identify degraded Operators by running the following command:

    ``` terminal
    $ oc get co | grep -v "True.*False.*False"
    ```

    The following example shows the output:

    ``` terminal
    NAME                                       VERSION   AVAILABLE   PROGRESSING   DEGRADED   SINCE   MESSAGE
    authentication                             4.20.0    True        False         True       5m      APIServerDeploymentDegraded: ...
    ```

2.  Check Operator details by running the following command:

    ``` terminal
    $ oc describe co authentication
    ```

    Look for error messages in the `status.conditions` section of the output.

3.  Check Operator pod logs by running the following command:

    ``` terminal
    $ oc logs -n openshift-authentication deployment/oauth-openshift
    ```

</div>

# Diagnosing an update stuck in Working towards state

If the cluster version shows a "Working towards" message for an extended period, identify which Operators are blocking the update from completing. Updates typically complete within 90 to 180 minutes.

<div>

<div class="title">

Prerequisites

</div>

- You have a cluster update that appears stuck in the "Working towards" state.

- You have access to the target cluster with cluster-admin privileges.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Check `ClusterVersion` status by running the following command:

    ``` terminal
    $ oc get clusterversion -o yaml
    ```

    Look for the `status.conditions` section to identify blocking resources.

2.  Check which Operators are still progressing by running the following command:

    ``` terminal
    $ oc get co | grep "True"
    ```

    Any Operator showing `PROGRESSING=True` is still updating.

3.  Check `ClusterVersion` history by running the following command:

    ``` terminal
    $ oc get clusterversion -o jsonpath='{.status.history}'
    ```

    A missing or stalled history entry indicates the update has timed out.

</div>

# Diagnosing worker nodes stuck in NotReady state

If worker nodes show `NotReady` status during an update, common causes include disk pressure, memory pressure, network connectivity issues, and PID pressure.

<div>

<div class="title">

Prerequisites

</div>

- You have worker nodes showing `NotReady` status during a cluster update.

- You have access to the target cluster with cluster-admin privileges.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Identify `NotReady` nodes by running the following command:

    ``` terminal
    $ oc get nodes | grep NotReady
    ```

2.  Check node conditions by running the following command:

    ``` terminal
    $ oc describe node <node_name> | grep -A 10 Conditions
    ```

3.  Check kubelet logs by running the following command:

    ``` terminal
    $ oc debug node/<node_name> -- chroot /host journalctl -u kubelet -n 100
    ```

</div>

# Diagnosing a stuck worker node update

If worker node updates are stuck, the issue is typically related to pod disruption budgets, machine config daemon failures, or node reboot failures.

<div>

<div class="title">

Prerequisites

</div>

- You have a worker node update that is not progressing.

- You have access to the target cluster with cluster-admin privileges.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Check the `MachineConfigPool` resource status by running the following command:

    ``` terminal
    $ oc get mcp worker -o yaml
    ```

    Look for degraded machine configs in the status.

2.  Check pod disruption budgets by running the following command:

    ``` terminal
    $ oc get pdb -A
    ```

    If a pod disruption budget (PDB) shows `ALLOWED DISRUPTIONS` of 0, adjust the PDB configuration.

3.  Check machine-config-daemon logs on the stuck node by running the following command:

    ``` terminal
    $ oc logs -n openshift-machine-config-operator <machine_config_daemon_pod>
    ```

</div>

# Diagnosing etcd issues during control plane updates

If etcd members become unhealthy during a control plane update, identify the affected members and investigate the root cause before proceeding.

<div>

<div class="title">

Prerequisites

</div>

- You have a control plane update with suspected etcd issues.

- You have access to the target cluster with cluster-admin privileges.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Check etcd cluster health by running the following command:

    ``` terminal
    $ oc get etcd -o yaml
    ```

    Look for the `EtcdMembersAvailable` condition in the output.

2.  Check etcd pod status by running the following command:

    ``` terminal
    $ oc get pods -n openshift-etcd -l app=etcd
    ```

    All etcd pods must be running.

3.  View etcd member status by running the following command:

    ``` terminal
    $ oc rsh -n openshift-etcd <etcd_pod> etcdctl member list -w table
    ```

4.  Monitor etcd logs for errors by running the following command:

    ``` terminal
    $ oc logs -n openshift-etcd <etcd_pod> etcd
    ```

</div>

# Diagnosing image pull failures during updates

If image pull failures occur during an update, common causes include registry connectivity issues, images not mirrored to a disconnected registry, and image pull authentication failures.

<div>

<div class="title">

Prerequisites

</div>

- You have image pull failures during a cluster update.

- You have access to the target cluster with cluster-admin privileges.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Check image pull status on nodes by running the following command:

    ``` terminal
    $ oc get events -A --field-selector reason=Failed --sort-by='.lastTimestamp' | grep -i image
    ```

2.  For disconnected environments, verify image mirroring by running the following command:

    ``` terminal
    $ oc get imagedigestmirrorset
    ```

    > [!NOTE]
    > In OpenShift Container Platform 4.13 and earlier, image mirroring was configured with `ImageContentSourcePolicy` resources. In OpenShift Container Platform 4.14 and later, `ImageDigestMirrorSet` resources replace `ImageContentSourcePolicy`. If your cluster was originally installed on a version earlier than 4.14, check both resource types.

3.  Test image pull from a node by running the following command:

    ``` terminal
    $ oc debug node/<node_name> -- chroot /host podman pull <image_url>
    ```

</div>

# Diagnosing update timeout exceeded

If TALM reports that the update timeout was exceeded, investigate cluster resource utilization, image pull speed, and network latency.

<div>

<div class="title">

Prerequisites

</div>

- You have a `ClusterGroupUpgrade` custom resource (CR) that has timed out.

- You have access to the target cluster with cluster-admin privileges.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Check cluster resource utilization by running the following command:

    ``` terminal
    $ oc adm top nodes
    ```

    High CPU or memory usage can slow updates.

2.  Check for slow image pulls by running the following command:

    ``` terminal
    $ oc get events -A --sort-by='.lastTimestamp' | grep -i "pull"
    ```

    Slow image pulls can indicate network latency between nodes and registries.

3.  Increase the `ClusterGroupUpgrade` CR timeout by running the following command if the cluster is healthy but updating slowly:

    ``` terminal
    $ oc patch cgu <cgu_name> -n <namespace> --type merge -p '{"spec":{"remediationStrategy":{"timeout":240}}}'
    ```

</div>

# Resolving a noncompliant policy hold during an update

During the update, TALM verifies the status of `ClusterVersion` for the OpenShift Container Platform update and `Subscription` for OLM Operators. If errors occur during those updates, the status does not change to the expected value and the policies do not become compliant. TALM holds at that point waiting for compliance.

If you are monitoring the update, you can fix the issue on the target cluster and the update continues automatically when the policy becomes compliant.

`ClusterGroupUpgrade` custom resource (CR) has timed out
Delete the timed-out CR by running the following command:

``` terminal
$ oc delete cgu <timed_out_cgu_name> -n <namespace>
```

All policies revert to `inform` mode, leaving the cluster at the point where the issue occurred.

Fix the issue that caused the timeout, then re-create the `ClusterGroupUpgrade` CR to resume the update by running the following command:

``` terminal
$ oc apply -f <cgu_cr_filename>.yaml
```

Policies or TALM are conflicting with changes you need to make
Delete the `ClusterGroupUpgrade` CR to revert all policies to `inform` mode by running the following command:

``` terminal
$ oc delete cgu <cgu_name> -n <namespace>
```

After the policies revert to `inform` mode, they do not enforce changes on the cluster.

Fix the issue, then re-create the `ClusterGroupUpgrade` CR to resume the update.

# Collecting diagnostic information for Red Hat support

If you cannot resolve the update issue, collect diagnostic information and contact Red Hat support for assistance.

<div>

<div class="title">

Prerequisites

</div>

- You have a cluster update issue that you cannot resolve.

- You have access to the target cluster and the Red Hat Advanced Cluster Management (RHACM) hub cluster with cluster-admin privileges.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Collect must-gather data by running the following command:

    ``` terminal
    $ oc adm must-gather
    ```

2.  Collect RHACM must-gather data for TALM-specific issues by running the following command:

    ``` terminal
    $ oc adm must-gather --image=registry.redhat.io/rhacm2/must-gather-rhel8
    ```

3.  Collect `ClusterVersion` history by running the following command:

    ``` terminal
    $ oc get clusterversion -o jsonpath='{.status.history}' > clusterversion-history.json
    ```

4.  Collect `ClusterGroupUpgrade` status by running the following command:

    ``` terminal
    $ oc get cgu <cgu_name> -n <namespace> -o yaml > cgu-status.yaml
    ```

</div>

# Additional resources

- [Perform health checks before a cluster update with TALM](update-rhacm-talm-health-checks.md#core-cluster-upgrades-health-checks)

- [Using the Topology Aware Lifecycle Manager for cluster updates](../../../edge_computing/cnf-talm-for-cluster-upgrades.md#cnf-talm-for-cluster-updates)

- [Contact Red Hat support](https://access.redhat.com/support)

- [Red Hat Knowledgebase](https://access.redhat.com/solutions)
