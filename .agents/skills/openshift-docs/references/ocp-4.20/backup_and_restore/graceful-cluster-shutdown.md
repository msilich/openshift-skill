<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

You can shut down your OpenShift Container Platform cluster for planned maintenance by cordoning nodes, draining workloads, and stopping nodes in order. Graceful shutdown preserves cluster state so you can restart the cluster when maintenance is complete.

# Shutting down the cluster

You can shut down a OpenShift Container Platform cluster gracefully by cordoning nodes, draining worker nodes, and stopping nodes in order. This preserves cluster data so you can restart the cluster after maintenance or a planned outage.

> [!NOTE]
> You can shut down a cluster until a year from the installation date and expect it to restart gracefully. After a year from the installation date, the cluster certificates expire. However, you might need to manually approve the pending certificate signing requests (CSRs) to recover kubelet certificates when the cluster restarts.

Take an etcd backup before shutting down the cluster so that you can restore the cluster if you encounter issues when restarting it.

You might need to restore from the backup if any of the following conditions occur:

- etcd data is corrupted during shutdown

- A node fails because of hardware

- Network connectivity is interrupted

If the cluster does not recover after restart, follow the steps to restore to a previous cluster state.

<div>

<div class="title">

Prerequisites

</div>

- You have access to the cluster as a user with the `cluster-admin` role.

- You created an etcd backup before shutting down the cluster.

  > [!IMPORTANT]
  > Without a recent etcd backup, you might not be able to restore the cluster if shutdown or restart fails.

- If you are running a single-node OpenShift cluster, you must evacuate all workload pods off of the cluster before you shut it down.

</div>

<div>

<div class="title">

Procedure

</div>

1.  If you are shutting the cluster down for an extended period, determine the date on which certificates expire by running the following command:

    ``` terminal
    $ oc -n openshift-kube-apiserver-operator get secret kube-apiserver-to-kubelet-signer -o jsonpath='{.metadata.annotations.auth\.openshift\.io/certificate-not-after}'
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    2030-08-05T14:37:50Z
    ```

    </div>

    Plan to restart the cluster on or before the displayed date so the cluster can restart gracefully. When the cluster restarts, you might need to manually approve pending certificate signing requests (CSRs) to recover kubelet certificates.

2.  Mark all the nodes in the cluster as unschedulable by running the following command:

    ``` terminal
    $ for node in $(oc get nodes -o jsonpath='{.items[*].metadata.name}'); do echo ${node} ; oc adm cordon ${node} ; done
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    ci-ln-mgdnf4b-72292-n547t-master-0
    node/ci-ln-mgdnf4b-72292-n547t-master-0 cordoned
    ci-ln-mgdnf4b-72292-n547t-master-1
    node/ci-ln-mgdnf4b-72292-n547t-master-1 cordoned
    ci-ln-mgdnf4b-72292-n547t-master-2
    node/ci-ln-mgdnf4b-72292-n547t-master-2 cordoned
    ci-ln-mgdnf4b-72292-n547t-worker-a-s7ntl
    node/ci-ln-mgdnf4b-72292-n547t-worker-a-s7ntl cordoned
    ci-ln-mgdnf4b-72292-n547t-worker-b-cmc9k
    node/ci-ln-mgdnf4b-72292-n547t-worker-b-cmc9k cordoned
    ci-ln-mgdnf4b-72292-n547t-worker-c-vcmtn
    node/ci-ln-mgdnf4b-72292-n547t-worker-c-vcmtn cordoned
    ```

    </div>

3.  Evacuate the pods by running the following command:

    ``` terminal
    $ for node in $(oc get nodes -l node-role.kubernetes.io/worker -o jsonpath='{.items[*].metadata.name}'); do echo ${node} ; oc adm drain ${node} --delete-emptydir-data --ignore-daemonsets=true --timeout=15s --force ; done
    ```

    Draining worker nodes before shutdown allows pods to terminate gracefully, which reduces the chance of data corruption.

4.  Shut down all of the nodes in the cluster by running the following command:

    ``` terminal
    $ for node in $(oc get nodes -o jsonpath='{.items[*].metadata.name}'); do oc debug node/${node} -- chroot /host shutdown -h 1; done
    ```

    > [!NOTE]
    > Ensure that the control plane node with the API VIP assigned is the last node processed in the loop. Otherwise, the shutdown command fails.

    The `-h 1` option indicates how long, in minutes, this process lasts before the control plane nodes are shut down. For large-scale clusters with 10 nodes or more, set to `-h 10` or longer to ensure all the compute nodes have time to shut down first.

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    Starting pod/ip-10-0-130-169us-east-2computeinternal-debug ...
    To use host binaries, run `chroot /host`
    Shutdown scheduled for Mon 2021-09-13 09:36:17 UTC, use 'shutdown -c' to cancel.
    Removing debug pod ...
    Starting pod/ip-10-0-150-116us-east-2computeinternal-debug ...
    To use host binaries, run `chroot /host`
    Shutdown scheduled for Mon 2021-09-13 09:36:29 UTC, use 'shutdown -c' to cancel.
    ```

    </div>

    > [!NOTE]
    > It is not necessary to drain control plane nodes of the standard pods that ship with OpenShift Container Platform before shutdown. Cluster administrators are responsible for ensuring a clean restart of workloads they deploy after the cluster is restarted. If you drained control plane nodes before shutdown because of custom workloads, you must mark the control plane nodes as schedulable before the cluster is functional again after restart.

5.  Shut off any cluster dependencies that are no longer needed, such as external storage or a Lightweight Directory Access Protocol (LDAP) server. Be sure to consult documentation from the vendor before doing so.

    > [!IMPORTANT]
    > If you deployed your cluster on a cloud-provider platform, do not shut down, suspend, or delete the associated cloud resources. If you delete the cloud resources of a suspended virtual machine, OpenShift Container Platform might not restore successfully.

</div>

# Additional resources

- [Backing up etcd](control_plane_backup_and_restore/backing-up-etcd.md#backup-etcd)

- [Restoring to an earlier cluster state](control_plane_backup_and_restore/disaster_recovery/scenario-2-restoring-cluster-state.md#dr-restoring-cluster-state)

- [Restarting the cluster gracefully](graceful-cluster-restart.md#graceful-restart-cluster)
