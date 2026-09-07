<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Running pre-update health checks reduces the risk of update failures and identifies problems early. If any checks fail, resolve the issues before proceeding with the cluster update.

# Performing health checks before cluster updates

You can perform comprehensive health checks before updating clusters to ensure cluster components are ready for the update. These checks validate cluster Operators, etcd health, storage systems, network connectivity, and custom resources specific to your deployment.

Complete these health checks before starting any cluster update to minimize the risk of update failures.

<div>

<div class="title">

Prerequisites

</div>

- You have access to target clusters with cluster-admin privileges.

- The `oc` CLI tool is installed and configured for the target cluster.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Verify control plane node readiness by running the following command:

    ``` terminal
    $ oc get nodes -l node-role.kubernetes.io/master=
    ```

    The following example shows the output:

    ``` terminal
    NAME                   STATUS   ROLES                  AGE   VERSION
    master-0.example.com   Ready    control-plane,master   30d   v1.33.0
    master-1.example.com   Ready    control-plane,master   30d   v1.33.0
    master-2.example.com   Ready    control-plane,master   30d   v1.33.0
    ```

    All control plane nodes must show `Ready` status with no `SchedulingDisabled` notation. If any nodes show `NotReady` or `SchedulingDisabled`, investigate and resolve before updating.

2.  Verify worker node readiness by running the following command:

    ``` terminal
    $ oc get nodes -l node-role.kubernetes.io/worker=
    ```

    All worker nodes must show `Ready` status. If any nodes show `NotReady` or `SchedulingDisabled`, investigate and resolve before updating.

3.  Check cluster Operator status by running the following command:

    ``` terminal
    $ oc get co
    ```

    The following example shows the output:

    ``` terminal
    NAME                                       VERSION   AVAILABLE   PROGRESSING   DEGRADED   SINCE   MESSAGE
    authentication                             4.20.0    True        False         False      30d
    cloud-controller-manager                   4.20.0    True        False         False      30d
    cluster-autoscaler                         4.20.0    True        False         False      30d
    ```

    All cluster Operators must show the following:

    - `AVAILABLE`: `True`

    - `PROGRESSING`: `False`

    - `DEGRADED`: `False`

    If any Operator is degraded or progressing, resolve the issue before proceeding.

4.  Verify etcd cluster health by running the following command:

    ``` terminal
    $ oc get etcd -o=jsonpath='{range .items[0].status.conditions[?(@.type=="EtcdMembersAvailable")]}{"\n"}{end}'
    ```

    The following example shows the output:

    ``` terminal
    3 members are available
    ```

    All etcd members must be available. If the output indicates unhealthy members, investigate etcd pod logs before updating.

5.  Check your backup storage location for an etcd backup created within the past 24 hours.

    If no recent backup exists, create an etcd backup before proceeding. For more information, see "Backing up etcd" in the "Additional resources" section.

6.  Verify machine config pool status by running the following command:

    ``` terminal
    $ oc get mcp
    ```

    The following example shows the output:

    ``` terminal
    NAME     CONFIG                                             UPDATED   UPDATING   DEGRADED   MACHINECOUNT   READYMACHINECOUNT   UPDATEDMACHINECOUNT   DEGRADEDMACHINECOUNT   AGE
    master   rendered-master-abc123                             True      False      False      3              3                   3                     0                      30d
    worker   rendered-worker-def456                             True      False      False      3              3                   3                     0                      30d
    ```

    All machine config pools must show the following:

    - `UPDATED`: `True`

    - `UPDATING`: `False`

    - `DEGRADED`: `False`

    - `MACHINECOUNT` must equal `READYMACHINECOUNT` and `UPDATEDMACHINECOUNT`

7.  Verify persistent volume health by running the following command:

    ``` terminal
    $ oc get pv
    ```

    All persistent volumes must show `Bound` or `Available` status. Persistent volumes must not show `Failed` status.

8.  Verify that a default storage class exists by running the following command:

    ``` terminal
    $ oc get storageclass
    ```

    At least one storage class must be marked as `(default)`.

9.  If your cluster uses SR-IOV, verify network node policies by running the following command:

    ``` terminal
    $ oc get sriovnetworknodepolicy -n openshift-sriov-network-operator
    ```

    All SR-IOV network node policies must show `Succeeded` or `InProgress` state.

10. Verify OLM Operator health by running the following command:

    ``` terminal
    $ oc get csv -A
    ```

    All `ClusterServiceVersions` must show `Succeeded` phase. If any Operators show `Failed` or `Installing` phase, investigate before updating.

11. Verify that no pods are in an unexpected state by running the following command:

    ``` terminal
    $ oc get pod -A | grep -E -i -v 'complete|running'
    ```

    The command must produce no output. If any pods are listed, review their status before updating.

12. Verify that pod disruption budgets (PDBs) are configured for all critical cloud-native network function (CNF) workloads by running the following command:

    ``` terminal
    $ oc get pdb -A
    ```

    The following example shows the output:

    ``` terminal
    NAME                    MIN AVAILABLE   MAX UNAVAILABLE   ALLOWED DISRUPTIONS   AGE
    cnf-workload-pdb        2               N/A               1                     30d
    ```

    PDBs must allow at least one disruption. Setting `minAvailable` to 100% of replicas blocks node drains during updates.

13. Check `PerformanceProfile` status by running the following command:

    ``` terminal
    $ oc get performanceprofile
    ```

    The following example shows the output:

    ``` terminal
    NAME               AGE
    core-performance   30d
    ```

14. Verify the `PerformanceProfile` shows `Applied` status by running the following command:

    ``` terminal
    $ oc get performanceprofile core-performance -o jsonpath='{.status.conditions[?(@.type=="Applied")].status}'
    ```

    The output must be `True`.

15. Verify API server responsiveness by running the following command:

    ``` terminal
    $ oc version
    ```

    The command should complete within a few seconds. If the API server is slow to respond, investigate before updating.

16. Verify certificate validity by running the following command:

    ``` terminal
    $ oc -n openshift-kube-apiserver-operator get secret kube-apiserver-to-kubelet-signer -o jsonpath='{.metadata.annotations.auth\.openshift\.io/certificate-not-after}'
    ```

    Certificates that expire within 30 days must be renewed before updating. If `cert-manager` is installed in the cluster, you can also run `oc get certificates -A` to check additional managed certificates.

17. Check CPU and memory utilization on nodes by running the following command:

    ``` terminal
    $ oc adm top nodes
    ```

    The following example shows the output:

    ``` terminal
    NAME                   CPU(cores)   CPU%   MEMORY(bytes)   MEMORY%
    master-0.example.com   500m         25%    8Gi             50%
    worker-0.example.com   1000m        50%    16Gi            60%
    ```

    Nodes should have sufficient headroom for rolling updates. CPU usage should be below 80%, and memory usage should be below 85%.

</div>

<div>

<div class="title">

Troubleshooting

</div>

- If cluster Operators are degraded, check Operator logs by running the following command:

  ``` terminal
  $ oc logs -n openshift-<operator_namespace> <operator_pod_name>
  ```

- If etcd members are unhealthy, investigate etcd pod logs by running the following command:

  ``` terminal
  $ oc logs -n openshift-etcd <etcd_pod_name>
  ```

- If PDBs block updates, review PDB configuration to ensure they allow sufficient disruptions.

- If nodes show `NotReady` status, check the node conditions by running the following command:

  ``` terminal
  $ oc describe node <node_name> | grep -A 10 Conditions
  ```

  Check kubelet logs by running the following command:

  ``` terminal
  $ oc debug node/<node_name> -- chroot /host journalctl -u kubelet
  ```

  Common causes for `NotReady` nodes include disk pressure, memory pressure, and network connectivity issues.

</div>

# Additional resources

- [Checking the cluster health](update-before-the-update.md#update-checking-cluster-health_update-before-the-update)

- [Backing up etcd](../../../backup_and_restore/control_plane_backup_and_restore/backing-up-etcd.md#backup-etcd)
