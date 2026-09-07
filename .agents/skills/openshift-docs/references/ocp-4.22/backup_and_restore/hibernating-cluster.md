<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Hibernate your OpenShift Container Platform cluster for up to 90 days to pause cluster operation without deprovisioning it. You can resume the cluster within that window to restore normal operation.

# About cluster hibernation

Review cluster hibernation limits and supported behavior before you pause a cluster. Understanding timing, node, and resume requirements helps you hibernate and resume successfully within 90 days.

You must wait at least 24 hours after cluster installation before hibernating your cluster to allow for the first certificate rotation.

Take an etcd backup before hibernating so that your cluster can be restored if you encounter issues when resuming the cluster.

You might need to restore from the backup if any of the following conditions occur:

- etcd data is corrupted during hibernation

- A node fails because of hardware

- Network connectivity is interrupted

If the cluster does not recover after restart, follow the steps to restore to a previous cluster state.

> [!IMPORTANT]
> If you must hibernate your cluster before the 24 hour certificate rotation, use the workaround in "Enabling OpenShift 4 Clusters to Stop and Resume Cluster VMs" instead.

When hibernating a cluster, you must hibernate all cluster nodes. Suspending only selected nodes is not supported.

After resuming, it can take up to 45 minutes for the cluster to become ready.

<div>

<div class="title">

Additional resources

</div>

- [Enabling OpenShift 4 Clusters to Stop and Resume Cluster VMs (Red Hat Blog)](https://www.redhat.com/en/blog/enabling-openshift-4-clusters-to-stop-and-resume-cluster-vms)

</div>

# Hibernating a cluster

Hibernate your cluster by verifying node and Operator health, then stopping the cluster virtual machines. This process pauses the cluster in a supported state so you can resume it later.

<div>

<div class="title">

Prerequisites

</div>

- The cluster has been running for at least 24 hours to allow the first certificate rotation to complete.

- You created an etcd backup before hibernating the cluster.

  > [!IMPORTANT]
  > Without a recent etcd backup, you might not be able to restore the cluster if hibernation or resume fails.

- You have access to the cluster as a user with the `cluster-admin` role.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Confirm that your cluster has been installed for at least 24 hours.

2.  Ensure that all nodes are in a good state by running the following command:

    ``` terminal
    $ oc get nodes
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    NAME                                      STATUS  ROLES                 AGE   VERSION
    ci-ln-812tb4k-72292-8bcj7-master-0        Ready   control-plane,master  32m   v1.35.4
    ci-ln-812tb4k-72292-8bcj7-master-1        Ready   control-plane,master  32m   v1.35.4
    ci-ln-812tb4k-72292-8bcj7-master-2        Ready   control-plane,master  32m   v1.35.4
    Ci-ln-812tb4k-72292-8bcj7-worker-a-zhdvk  Ready   worker                19m   v1.35.4
    ci-ln-812tb4k-72292-8bcj7-worker-b-9hrmv  Ready   worker                19m   v1.35.4
    ci-ln-812tb4k-72292-8bcj7-worker-c-q8mw2  Ready   worker                19m   v1.35.4
    ```

    </div>

    All nodes should show `Ready` in the `STATUS` column.

3.  Ensure that all cluster Operators are in a good state by running the following command:

    ``` terminal
    $ oc get clusteroperators
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    NAME                      VERSION   AVAILABLE  PROGRESSING  DEGRADED  SINCE   MESSAGE
    authentication            4.22.0-0  True       False        False     51m
    baremetal                 4.22.0-0  True       False        False     72m
    cloud-controller-manager  4.22.0-0  True       False        False     75m
    cloud-credential          4.22.0-0  True       False        False     77m
    cluster-api               4.22.0-0  True       False        False     42m
    cluster-autoscaler        4.22.0-0  True       False        False     72m
    config-operator           4.22.0-0  True       False        False     72m
    console                   4.22.0-0  True       False        False     55m
    ...
    ```

    </div>

    All cluster Operators should show `AVAILABLE`=`True`, `PROGRESSING`=`False`, and `DEGRADED`=`False`.

4.  Ensure that all machine config pools are in a good state by running the following command:

    ``` terminal
    $ oc get mcp
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    NAME    CONFIG                                            UPDATED  UPDATING  DEGRADED  MACHINECOUNT  READYMACHINECOUNT  UPDATEDMACHINECOUNT  DEGRADEDMACHINECOUNT  AGE
    master  rendered-master-87871f187930e67233c837e1d07f49c7  True     False     False     3             3                  3                    0                     96m
    worker  rendered-worker-3c4c459dc5d90017983d7e72928b8aed  True     False     False     3             3                  3                    0                     96m
    ```

    </div>

    All machine config pools should show `UPDATING`=`False` and `DEGRADED`=`False`.

5.  Stop the cluster virtual machines:

    Use the tools native to the cloud environment of your cluster to shut down the cluster virtual machines.

    > [!IMPORTANT]
    > If you use a bastion virtual machine, do not shut down this virtual machine.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Backing up etcd](control_plane_backup_and_restore/backing-up-etcd.md#backup-etcd)

- [Restoring to an earlier cluster state](control_plane_backup_and_restore/disaster_recovery/scenario-2-restoring-cluster-state.md#dr-restoring-cluster-state)

</div>

# Resuming a hibernated cluster

Resume a hibernated cluster by starting the cluster virtual machines and approving certificate signing requests (CSRs) as needed. This process restores the cluster to a ready state within the supported 90-day window.

It can take around 45 minutes for the cluster to resume, depending on the size of your cluster.

<div>

<div class="title">

Prerequisites

</div>

- You hibernated your cluster less than 90 days ago.

- You have access to the cluster as a user with the `cluster-admin` role.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Within 90 days of cluster hibernation, resume the cluster virtual machines:

    Use the tools native to the cloud environment of your cluster to resume the cluster virtual machines.

2.  Wait about 5 minutes, depending on the number of nodes in your cluster.

3.  Approve CSRs for the nodes:

    1.  Check that there is a CSR for each node in the `NotReady` state by running the following command:

        ``` terminal
        $ oc get csr
        ```

        <div class="formalpara">

        <div class="title">

        Example output

        </div>

        ``` terminal
        NAME       AGE  SIGNERNAME                                   REQUESTOR                                                                  REQUESTEDDURATION  CONDITION
        csr-4dwsd  37m  kubernetes.io/kube-apiserver-client          system:node:ci-ln-812tb4k-72292-8bcj7-worker-c-q8mw2                       24h                Pending
        csr-4vrbr  49m  kubernetes.io/kube-apiserver-client          system:node:ci-ln-812tb4k-72292-8bcj7-master-1                             24h                Pending
        csr-4wk5x  51m  kubernetes.io/kubelet-serving                system:node:ci-ln-812tb4k-72292-8bcj7-master-1                             <none>             Pending
        csr-84vb6  51m  kubernetes.io/kube-apiserver-client-kubelet  system:serviceaccount:openshift-machine-config-operator:node-bootstrapper  <none>             Pending
        ```

        </div>

    2.  Approve each valid CSR by running the following command:

        ``` terminal
        $ oc adm certificate approve <csr_name>
        ```

    3.  Verify that all necessary CSRs were approved by running the following command:

        ``` terminal
        $ oc get csr
        ```

        <div class="formalpara">

        <div class="title">

        Example output

        </div>

        ``` terminal
        NAME       AGE  SIGNERNAME                                   REQUESTOR                                                                  REQUESTEDDURATION  CONDITION
        csr-4dwsd  37m  kubernetes.io/kube-apiserver-client          system:node:ci-ln-812tb4k-72292-8bcj7-worker-c-q8mw2                       24h                Approved,Issued
        csr-4vrbr  49m  kubernetes.io/kube-apiserver-client          system:node:ci-ln-812tb4k-72292-8bcj7-master-1                             24h                Approved,Issued
        csr-4wk5x  51m  kubernetes.io/kubelet-serving                system:node:ci-ln-812tb4k-72292-8bcj7-master-1                             <none>             Approved,Issued
        csr-84vb6  51m  kubernetes.io/kube-apiserver-client-kubelet  system:serviceaccount:openshift-machine-config-operator:node-bootstrapper  <none>             Approved,Issued
        ```

        </div>

        CSRs should show `Approved,Issued` in the `CONDITION` column.

4.  Verify that all nodes now show as ready by running the following command:

    ``` terminal
    $ oc get nodes
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    NAME                                      STATUS  ROLES                 AGE   VERSION
    ci-ln-812tb4k-72292-8bcj7-master-0        Ready   control-plane,master  32m   v1.35.4
    ci-ln-812tb4k-72292-8bcj7-master-1        Ready   control-plane,master  32m   v1.35.4
    ci-ln-812tb4k-72292-8bcj7-master-2        Ready   control-plane,master  32m   v1.35.4
    Ci-ln-812tb4k-72292-8bcj7-worker-a-zhdvk  Ready   worker                19m   v1.35.4
    ci-ln-812tb4k-72292-8bcj7-worker-b-9hrmv  Ready   worker                19m   v1.35.4
    ci-ln-812tb4k-72292-8bcj7-worker-c-q8mw2  Ready   worker                19m   v1.35.4
    ```

    </div>

    All nodes should show `Ready` in the `STATUS` column. It might take a few minutes for all nodes to become ready after approving the CSRs.

5.  Wait for cluster Operators to restart to load the new certificates.

    This might take 5 or 10 minutes.

6.  Verify that all cluster Operators are in a good state by running the following command:

    ``` terminal
    $ oc get clusteroperators
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    NAME                      VERSION   AVAILABLE  PROGRESSING  DEGRADED  SINCE   MESSAGE
    authentication            4.22.0-0  True       False        False     51m
    baremetal                 4.22.0-0  True       False        False     72m
    cloud-controller-manager  4.22.0-0  True       False        False     75m
    cloud-credential          4.22.0-0  True       False        False     77m
    cluster-api               4.22.0-0  True       False        False     42m
    cluster-autoscaler        4.22.0-0  True       False        False     72m
    config-operator           4.22.0-0  True       False        False     72m
    console                   4.22.0-0  True       False        False     55m
    ...
    ```

    </div>

    All cluster Operators should show `AVAILABLE`=`True`, `PROGRESSING`=`False`, and `DEGRADED`=`False`.

</div>
