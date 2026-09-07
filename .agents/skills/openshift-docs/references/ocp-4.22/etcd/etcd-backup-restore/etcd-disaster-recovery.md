<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

To return your cluster to a working state after quorum loss, control plane failure, or expired certificates, follow the disaster recovery procedures for your situation. You can restore etcd quorum, restore the cluster from an etcd snapshot, or recover from expired control plane certificates.

> [!IMPORTANT]
> Disaster recovery requires you to have at least one healthy control plane host.

# Restoring etcd quorum for high availability clusters

You can restore etcd quorum on high availability (HA) clusters by running the `quorum-restore.sh` script on a recovery host. Restored quorum returns the OpenShift Container Platform API to read/write mode when quorum loss takes the cluster offline.

The `quorum-restore.sh` script creates a new single-member etcd cluster from the local data directory on the recovery host. No prior backup is required.

For high availability (HA) clusters, a three-node HA cluster requires you to shut down etcd on two hosts to avoid a cluster split. On four-node and five-node HA clusters, you must shut down three hosts. Quorum requires a majority of nodes. The minimum number of nodes required for quorum on a three-node HA cluster is two. On four-node and five-node HA clusters, the minimum number of nodes required for quorum is three. If you start a new cluster from backup on your recovery host, the other etcd members might still be able to form quorum and continue service.

> [!WARNING]
> You might experience data loss if the host that runs the restoration does not have all data replicated to it.

> [!IMPORTANT]
> Quorum restoration should not be used to decrease the number of nodes outside of the restoration process. Decreasing the number of nodes results in an unsupported cluster configuration.

<div>

<div class="title">

Prerequisites

</div>

- You have SSH access to the node used to restore quorum.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Select a control plane host to use as the recovery host. You run the restore operation on this host.

    1.  List the running etcd pods by running the following command:

        ``` terminal
        $ oc get pods -n openshift-etcd -l app=etcd --field-selector="status.phase==Running"
        ```

    2.  Choose a pod and run the following command to obtain its IP address:

        ``` terminal
        $ oc exec -n openshift-etcd <etcd-pod> -c etcdctl -- etcdctl endpoint status -w table
        ```

        Note the IP address of a member that is not a learner and has the highest Raft index.

    3.  List nodes by running the following command:

        ``` terminal
        $ oc get nodes -o jsonpath='{range .items[*]}[{.metadata.name},{.status.addresses[?(@.type=="InternalIP")].address}]{end}'
        ```

        Note the node name that corresponds to the IP address of the chosen etcd member.

2.  Using SSH, connect to the chosen recovery node and run the following command to restore etcd quorum:

    ``` terminal
    $ sudo -E /usr/local/bin/quorum-restore.sh
    ```

    After a few minutes, the nodes that went down are automatically synchronized with the node that the recovery script was run on. Any remaining online nodes automatically rejoin the new etcd cluster created by the `quorum-restore.sh` script. This process takes a few minutes.

3.  Exit the SSH session.

4.  Return to a three-node configuration if any nodes are offline. Repeat the following steps for each node that is offline to delete and re-create them. After the machines are re-created, a new revision is forced and etcd automatically scales up.

    - If you use a user-provisioned bare-metal installation, you can re-create a control plane machine by using the same method that you used to originally create it. For more information, see "Installing a user-provisioned cluster on bare metal".

      > [!WARNING]
      > Do not delete and re-create the machine for the recovery host.

    - If you are running installer-provisioned infrastructure, or you used the Machine API to create your machines, follow these steps:

      > [!WARNING]
      > Do not delete and re-create the machine for the recovery host.
      >
      > For bare-metal installations on installer-provisioned infrastructure, control plane machines are not re-created. For more information, see "Replacing a bare-metal control plane node".

      1.  In a terminal that has access to the cluster as a `cluster-admin` user, obtain the machine for one of the offline nodes by running the following command:

          ``` terminal
          $ oc get machines -n openshift-machine-api -o wide
          ```

          <div class="formalpara">

          <div class="title">

          Example output

          </div>

          ``` terminal
          NAME                                        PHASE     TYPE        REGION      ZONE         AGE     NODE                           PROVIDERID                              STATE
          clustername-8qw5l-master-0                  Running   m4.xlarge   us-east-1   us-east-1a   3h37m   ip-10-0-131-183.ec2.internal   aws:///us-east-1a/i-0ec2782f8287dfb7e   stopped
          clustername-8qw5l-master-1                  Running   m4.xlarge   us-east-1   us-east-1b   3h37m   ip-10-0-143-125.ec2.internal   aws:///us-east-1b/i-096c349b700a19631   running
          clustername-8qw5l-master-2                  Running   m4.xlarge   us-east-1   us-east-1c   3h37m   ip-10-0-154-194.ec2.internal    aws:///us-east-1c/i-02626f1dba9ed5bba  running
          clustername-8qw5l-worker-us-east-1a-wbtgd   Running   m4.large    us-east-1   us-east-1a   3h28m   ip-10-0-129-226.ec2.internal   aws:///us-east-1a/i-010ef6279b4662ced   running
          clustername-8qw5l-worker-us-east-1b-lrdxb   Running   m4.large    us-east-1   us-east-1b   3h28m   ip-10-0-144-248.ec2.internal   aws:///us-east-1b/i-0cb45ac45a166173b   running
          clustername-8qw5l-worker-us-east-1c-pkg26   Running   m4.large    us-east-1   us-east-1c   3h28m   ip-10-0-170-181.ec2.internal   aws:///us-east-1c/i-06861c00007751b0a   running
          ```

          </div>

          In the example output, `clustername-8qw5l-master-0` is the control plane machine for the offline node, `ip-10-0-131-183.ec2.internal`.

      2.  Delete the machine of the offline node by running the following command:

          ``` terminal
          $ oc delete machine -n openshift-machine-api clustername-8qw5l-master-0
          ```

          Specify the name of the control plane machine for the offline node.

          A new machine is automatically provisioned after deleting the machine of the offline node.

5.  Verify that a new machine has been created by running the following command:

    ``` terminal
    $ oc get machines -n openshift-machine-api -o wide
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    NAME                                        PHASE          TYPE        REGION      ZONE         AGE     NODE                           PROVIDERID                              STATE
    clustername-8qw5l-master-1                  Running        m4.xlarge   us-east-1   us-east-1b   3h37m   ip-10-0-143-125.ec2.internal   aws:///us-east-1b/i-096c349b700a19631   running
    clustername-8qw5l-master-2                  Running        m4.xlarge   us-east-1   us-east-1c   3h37m   ip-10-0-154-194.ec2.internal    aws:///us-east-1c/i-02626f1dba9ed5bba  running
    clustername-8qw5l-master-3                  Provisioning   m4.xlarge   us-east-1   us-east-1a   85s     ip-10-0-173-171.ec2.internal    aws:///us-east-1a/i-015b0888fe17bc2c8  running
    clustername-8qw5l-worker-us-east-1a-wbtgd   Running        m4.large    us-east-1   us-east-1a   3h28m   ip-10-0-129-226.ec2.internal   aws:///us-east-1a/i-010ef6279b4662ced   running
    clustername-8qw5l-worker-us-east-1b-lrdxb   Running        m4.large    us-east-1   us-east-1b   3h28m   ip-10-0-144-248.ec2.internal   aws:///us-east-1b/i-0cb45ac45a166173b   running
    clustername-8qw5l-worker-us-east-1c-pkg26   Running        m4.large    us-east-1   us-east-1c   3h28m   ip-10-0-170-181.ec2.internal   aws:///us-east-1c/i-06861c00007751b0a   running
    ```

    </div>

    In the example output, `clustername-8qw5l-master-3` is being created and is ready after the phase changes from `Provisioning` to `Running`.

    It might take a few minutes for the new machine to be created. The etcd cluster Operator automatically synchronizes when the machine or node returns to a healthy state.

6.  For each node that is offline, repeat the previous steps to delete and re-create the node.

7.  Wait until the control plane recovers by running the following command:

    ``` terminal
    $ oc adm wait-for-stable-cluster
    ```

    > [!NOTE]
    > It can take up to 15 minutes for the control plane to recover.

</div>

<div>

<div class="title">

Troubleshooting

</div>

- If you see no progress rolling out the etcd static pods, you can force redeployment from the etcd cluster Operator by running the following command:

  ``` terminal
  $ oc patch etcd cluster -p='{"spec": {"forceRedeploymentReason": "recovery-'"$(date --rfc-3339=ns )"'"}}' --type=merge
  ```

</div>

<div>

<div class="title">

Additional resources

</div>

- [Installing a user-provisioned cluster on bare metal](../../installing/installing_bare_metal/upi/installing-bare-metal.md#installing-bare-metal)

- [Replacing a bare-metal control plane node](../../installing/installing_bare_metal/bare-metal-expanding-the-cluster.md#replacing-a-bare-metal-control-plane-node_bare-metal-expanding)

- [Replacing an unhealthy etcd member](../../backup_and_restore/control_plane_backup_and_restore/replacing-unhealthy-etcd-member.md#replacing-unhealthy-etcd-member)

</div>

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

<div>

<div class="title">

Additional resources

</div>

- [Recovering from expired control plane certificates](../../backup_and_restore/control_plane_backup_and_restore/disaster_recovery/scenario-3-expired-certs.md#dr-recovering-expired-certs)

</div>

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

<div>

<div class="title">

Additional resources

</div>

- [Recovering a degraded etcd Operator](../../machine_management/control_plane_machine_management/cpmso-troubleshooting.md#cpmso-ts-etcd-degraded_cpmso-troubleshooting)

</div>

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

# Recovering from expired control plane certificates

You can restore kubelet certificates by manually approving pending `node-bootstrapper` certificate signing requests (CSRs) and, on user-provisioned installations, kubelet serving CSRs. Approved CSRs return nodes to a healthy state after control plane certificates expire.

<div>

<div class="title">

Prerequisites

</div>

- You have access to the cluster as a user with the `cluster-admin` role.

- You have access to the OpenShift CLI (`oc`).

</div>

<div>

<div class="title">

Procedure

</div>

1.  Get the list of current CSRs by running the following command:

    ``` terminal
    $ oc get csr
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    NAME        AGE    SIGNERNAME                                    REQUESTOR                                                                   CONDITION
    csr-2s94x   8m3s   kubernetes.io/kubelet-serving                 system:node:<node_name>                                                     Pending
    csr-4bd6t   8m3s   kubernetes.io/kubelet-serving                 system:node:<node_name>                                                     Pending
    csr-4hl85   13m    kubernetes.io/kube-apiserver-client-kubelet   system:serviceaccount:openshift-machine-config-operator:node-bootstrapper   Pending
    csr-zhhhp   3m8s   kubernetes.io/kube-apiserver-client-kubelet   system:serviceaccount:openshift-machine-config-operator:node-bootstrapper   Pending
    ...
    ```

    </div>

    In the example output, CSRs with a `SIGNERNAME` of `kubernetes.io/kubelet-serving` are kubelet serving CSRs. You see this CSR type on user-provisioned installations. CSRs with a `SIGNERNAME` of `kubernetes.io/kube-apiserver-client-kubelet` and a `node-bootstrapper` requestor are `node-bootstrapper` CSRs that you must approve to restore kubelet certificates.

2.  Review the details of a CSR to verify that it is valid by running the following command:

    ``` terminal
    $ oc describe csr <csr_name>
    ```

    `<csr_name>` is the name of a CSR from the list of current CSRs.

3.  Approve each valid `node-bootstrapper` CSR by running the following command:

    ``` terminal
    $ oc adm certificate approve <csr_name>
    ```

4.  For user-provisioned installations, approve each valid kubelet serving CSR by running the following command:

    ``` terminal
    $ oc adm certificate approve <csr_name>
    ```

</div>

# Testing restore procedures

You can test your cluster restore workflow by simulating etcd failure on nonrecovery nodes and restoring from backup. Use this test to confirm that your etcd backup and restore process works as expected.

> [!WARNING]
> You must have SSH access to the cluster. Without SSH access, you cannot disable etcd or manage the `kubelet` service on nonrecovery nodes.

<div>

<div class="title">

Prerequisites

</div>

- You have SSH access to control plane hosts.

- You have installed the OpenShift CLI (`oc`).

</div>

<div>

<div class="title">

Procedure

</div>

1.  Use SSH to connect to each of your nonrecovery nodes to disable etcd and the `kubelet` service:

    1.  Disable etcd by running the following command:

        ``` terminal
        $ sudo /usr/local/bin/disable-etcd.sh
        ```

    2.  Delete variable data for etcd by running the following command:

        ``` terminal
        $ sudo rm -rf /var/lib/etcd
        ```

    3.  Disable the `kubelet` service by running the following command:

        ``` terminal
        $ sudo systemctl disable kubelet.service
        ```

2.  Exit every SSH session.

3.  Ensure that your nonrecovery nodes are in a `NOT READY` state by running the following command:

    ``` terminal
    $ oc get nodes
    ```

4.  Restore your cluster to an earlier cluster state using an etcd backup. For more information, see "Restoring to an earlier cluster state".

5.  After you restore the cluster and the API responds, use SSH to connect to each nonrecovery node and enable the `kubelet` service by running the following command:

    ``` terminal
    $ sudo systemctl enable kubelet.service
    ```

6.  Exit every SSH session.

7.  Verify that your nodes return to the `READY` state by running the following command:

    ``` terminal
    $ oc get nodes
    ```

8.  Verify that etcd is available by running the following command:

    ``` terminal
    $ oc get pods -n openshift-etcd
    ```

</div>

<div>

<div class="title">

Additional resources

</div>

- [Restoring to an earlier cluster state](../../backup_and_restore/control_plane_backup_and_restore/disaster_recovery/scenario-2-restoring-cluster-state.md#dr-restoring-cluster-state)

</div>
