<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

To return your OpenShift Container Platform cluster to a known good state, restore from a saved etcd snapshot after quorum loss or critical resource deletion. Understanding restore impact helps you decide whether rollback is appropriate before you begin.

# About restoring to an earlier cluster state

To assess restore risks before you choose rollback as a last resort, review how an etcd snapshot restore affects your OpenShift Container Platform cluster, including Operators, workloads, and persistent storage.

You can use an etcd backup to restore your cluster to an earlier state. This can be used to recover from the following situations:

- The cluster has lost the majority of control plane hosts and quorum.

- An administrator has deleted something critical and must restore to recover the cluster.

If applicable, you might also need to recover from expired control plane certificates.

> [!WARNING]
> Restoring to an earlier cluster state is a destructive and destabilizing action to take on a running cluster. This should only be used as a last resort.
>
> If you cannot retrieve data using the Kubernetes API server, then etcd is available and you should not restore using an etcd backup.

Restoring etcd effectively takes a cluster back in time and all clients experience a conflicting, parallel history. This can impact the behavior of watching components like kubelets, Kubernetes controller managers, persistent volume controllers, and OpenShift Container Platform Operators, including the network Operator.

It can cause Operator churn when the content in etcd does not match the actual content on disk, causing Operators for the Kubernetes API server, Kubernetes controller manager, Kubernetes scheduler, and etcd to get stuck when files on disk conflict with content in etcd. This can require manual actions to resolve the issues.

In extreme cases, the cluster can lose track of persistent volumes, delete critical workloads that no longer exist, reimage machines, and rewrite CA bundles with expired certificates.

# Restoring to an earlier cluster state for a single node

To restore your OpenShift Container Platform cluster on a single node, use a saved etcd snapshot to roll back to an earlier state after quorum loss or critical data deletion.

> [!IMPORTANT]
> When you restore your cluster, you must use an etcd backup that was taken from the same z-stream release. For example, an OpenShift Container Platform 4.22.2 cluster must use an etcd backup that was taken from 4.22.2.

<div>

<div class="title">

Prerequisites

</div>

- You have access to the cluster as a user with the `cluster-admin` role through a certificate-based `kubeconfig` file.

- You have SSH access to control plane hosts.

- You have a backup directory containing both the `etcd` snapshot and the resources for the static pods, which were from the same backup. The file names in the directory must be in the following formats: `snapshot_<datetimestamp>.db` and `static_kuberesources_<datetimestamp>.tar.gz`.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Use SSH to connect to the single node and copy the etcd backup to the `/home/core` directory by running the following command:

    ``` terminal
    $ cp <etcd_backup_directory> /home/core
    ```

2.  To restore the cluster from an earlier backup on the single node, run the following command:

    ``` terminal
    $ sudo -E /usr/local/bin/cluster-restore.sh /home/core/<etcd_backup_directory>
    ```

3.  Exit the SSH session.

4.  Monitor the recovery progress of the control plane by running the following command:

    ``` terminal
    $ oc adm wait-for-stable-cluster
    ```

    > [!NOTE]
    > It can take up to 15 minutes for the control plane to recover.

</div>

# Restoring to an earlier cluster state for more than one node

To restore your OpenShift Container Platform cluster with more than one control plane node to an earlier state, use a saved etcd snapshot after quorum loss or critical data deletion.

For a Two-Node with Fencing (TNF) setup, a single surviving node can continue to operate in degraded mode. Use a saved etcd backup to restore an earlier cluster state if only one node is operational, or when both nodes have failed and you need to restart the cluster from a known safe state. In both cases, perform the restore procedure on a single node. The peer node automatically synchronizes data with the restored node when it rejoins the cluster.

Before you restore from backup on the recovery host, shut down etcd on enough control plane nodes so the remaining members cannot form a quorum:

- Shut down etcd on 2 hosts in a 3-node cluster.

- Shut down etcd on 3 hosts in a 4-node or 5-node cluster.

If too few hosts are shut down, the other etcd members might still form a quorum and continue service while you restore.

> [!NOTE]
> If your cluster uses a control plane machine set, see "Recovering a degraded etcd Operator" in the control plane machine set troubleshooting topic for an etcd recovery procedure. For OpenShift Container Platform on a single node, follow the procedure to restore to an earlier cluster state for a single node.

> [!IMPORTANT]
> When you restore your cluster, you must use an etcd backup that was taken from the same z-stream release. For example, an OpenShift Container Platform 4.22.2 cluster must use an etcd backup that was taken from 4.22.2.

<div>

<div class="title">

Prerequisites

</div>

- You have access to the cluster as a user with the `cluster-admin` role through a certificate-based `kubeconfig` file, like the one that was used during installation.

- You have a healthy control plane host to use as the recovery host.

- You have SSH access to control plane hosts.

- You have a backup directory containing both the `etcd` snapshot and the resources for the static pods, which were from the same backup. The file names in the directory must be in the following formats: `snapshot_<datetimestamp>.db` and `static_kuberesources_<datetimestamp>.tar.gz`.

- Control plane nodes are accessible or bootable.

</div>

> [!IMPORTANT]
> For non-recovery control plane nodes, it is not required to establish SSH connectivity or to stop the static pods. You can delete and re-create other non-recovery, control plane machines, one by one.

<div>

<div class="title">

Procedure

</div>

1.  Select a control plane host to use as the recovery host. This is the host that you run the restore operation on.

2.  Establish SSH connectivity to each of the control plane nodes, including the recovery host.

    `kube-apiserver` becomes inaccessible after the restore process starts, so you cannot access the control plane nodes. Establish SSH connectivity to each control plane host in a separate terminal.

    > [!IMPORTANT]
    > If you do not complete this step, you cannot access the control plane hosts to complete the restore procedure, and you cannot recover your cluster from this state.

3.  Using SSH, connect to each control plane node to disable etcd by running the following command:

    ``` terminal
    $ sudo -E /usr/local/bin/disable-etcd.sh
    ```

4.  Copy the etcd backup directory to the recovery control plane host.

    This procedure assumes that you copied the `backup` directory containing the etcd snapshot and the resources for the static pods to the `/home/core/` directory of your recovery control plane host.

5.  Use SSH to connect to the recovery host. Restore the cluster from an earlier backup by running the following command:

    ``` terminal
    $ sudo -E /usr/local/bin/cluster-restore.sh /home/core/<etcd-backup-directory>
    ```

6.  Exit the SSH session.

7.  When the API responds, turn off the etcd Operator quorum guard by running the following command:

    ``` terminal
    $ oc patch etcd/cluster --type=merge -p '{"spec": {"unsupportedConfigOverrides": {"useUnsupportedUnsafeNonHANonProductionUnstableEtcd": true}}}'
    ```

    > [!IMPORTANT]
    > For a TNF setup, do not:
    >
    > - Change the etcd Operator quorum setting.
    >
    > - Turn the etcd Operator quorum off.
    >
    > - Turn the etcd Operator quorum back on.

8.  Monitor the recovery progress of the control plane by running the following command:

    ``` terminal
    $ oc adm wait-for-stable-cluster
    ```

    > [!NOTE]
    > It can take up to 15 minutes for the control plane to recover. Wait for the control plane to recover before using the next step.

9.  Enable the quorum guard by running the following command:

    ``` terminal
    $ oc patch etcd/cluster --type=merge -p '{"spec": {"unsupportedConfigOverrides": null}}'
    ```

</div>

<div class="formalpara">

<div class="title">

Troubleshooting

</div>

If the etcd static pods do not roll out, you can manually force an etcd redeployment from the `cluster-etcd-operator` by running the following command:

</div>

``` terminal
$ oc patch etcd cluster -p='{"spec": {"forceRedeploymentReason": "recovery-'"$(date --rfc-3339=ns )"'"}}' --type=merge
```

# Issues and workarounds for restoring a persistent storage state

To restore workloads safely after an etcd snapshot restore, identify and resolve outdated persistent storage references, including volumes, credentials, attachments, and devices on your OpenShift Container Platform cluster.

If your OpenShift Container Platform cluster uses persistent storage of any form, a state of the cluster is typically stored outside etcd. When you restore from an etcd backup, the status of the workloads in OpenShift Container Platform is also restored. However, if the etcd snapshot is old, the status might be invalid or outdated.

> [!IMPORTANT]
> The contents of persistent volumes (PVs) are never part of the etcd snapshot. When you restore an OpenShift Container Platform cluster from an etcd snapshot, non-critical workloads might gain access to critical data, or vice-versa.

The following are some example scenarios that produce an out-of-date status:

- MySQL database is running in a pod backed up by a PV object. Restoring OpenShift Container Platform from an etcd snapshot does not bring back the volume on the storage provider, and does not produce a running MySQL pod, despite the pod repeatedly attempting to start. You must manually restore this pod by restoring the volume on the storage provider, and then editing the PV to point to the new volume.

- Pod P1 is using volume A, which is attached to node X. If the etcd snapshot is taken while another pod uses the same volume on node Y, then when the etcd restore is performed, pod P1 might not be able to start correctly due to the volume still being attached to node Y. OpenShift Container Platform is not aware of the attachment, and does not automatically detach it. When this occurs, the volume must be manually detached from node Y so that the volume can attach on node X, and then pod P1 can start.

- Cloud provider or storage provider credentials were updated after the etcd snapshot was taken. This causes any CSI drivers or Operators that depend on those credentials to not work. You might have to manually update the credentials required by those drivers or Operators.

- A device is removed or renamed from OpenShift Container Platform nodes after the etcd snapshot is taken. The Local Storage Operator creates symlinks for each PV that it manages from `/dev/disk/by-id` or `/dev` directories. This situation might cause the local PVs to refer to devices that no longer exist.

  To fix this problem, an administrator must:

  1.  Manually remove the PVs with invalid devices.

  2.  Remove symlinks from respective nodes.

  3.  Delete `LocalVolume` or `LocalVolumeSet` objects. For more information, see "Deleting the Local Storage Operator resources".

<div>

<div class="title">

Additional resources

</div>

- [Recovering a degraded etcd Operator](../../../machine_management/control_plane_machine_management/cpmso-troubleshooting.md#cpmso-ts-etcd-degraded_cpmso-troubleshooting)

- [Deleting the Local Storage Operator resources](../../../storage/persistent_storage_local/persistent-storage-local.md#local-storage-deleting-resources-overview_persistent-storage-local)

</div>
