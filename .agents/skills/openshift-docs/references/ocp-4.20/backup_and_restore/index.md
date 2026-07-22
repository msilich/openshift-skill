<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

# Control plane backup and restore operations

As a cluster administrator, you might need to stop an OpenShift Container Platform cluster for a period and restart it later. Some reasons for restarting a cluster are that you need to perform maintenance on a cluster or want to reduce resource costs. In OpenShift Container Platform, you can perform a [graceful shutdown of a cluster](graceful-cluster-shutdown.md#graceful-shutdown-cluster) so that you can easily restart the cluster later.

You must [back up etcd data](control_plane_backup_and_restore/backing-up-etcd.md#backup-etcd) before shutting down a cluster; etcd is the key-value store for OpenShift Container Platform, which persists the state of all resource objects. An etcd backup plays a crucial role in disaster recovery. In OpenShift Container Platform, you can also [replace an unhealthy etcd member](control_plane_backup_and_restore/replacing-unhealthy-etcd-member.md#replacing-unhealthy-etcd-member).

When you want to get your cluster running again, [restart the cluster gracefully](graceful-cluster-restart.md#graceful-restart-cluster).

> [!NOTE]
> A cluster’s certificates expire one year after the installation date. You can shut down a cluster and expect it to restart gracefully while the certificates are still valid. Although the cluster automatically retrieves the expired control plane certificates, you must still [approve the certificate signing requests (CSRs)](control_plane_backup_and_restore/disaster_recovery/scenario-3-expired-certs.md#dr-recovering-expired-certs).

You might run into several situations where OpenShift Container Platform does not work as expected, such as:

- You have a cluster that is not functional after the restart because of unexpected conditions, such as node failure or network connectivity issues.

- You have deleted something critical in the cluster by mistake.

- You have lost the majority of your control plane hosts, leading to etcd quorum loss.

You can always recover from a disaster situation by [restoring your cluster to its previous state](control_plane_backup_and_restore/disaster_recovery/scenario-2-restoring-cluster-state.md#dr-restoring-cluster-state) using the saved etcd snapshots.

<div>

<div class="title">

Additional resources

</div>

- [Quorum protection with machine lifecycle hooks](../machine_management/deleting-machine.md#machine-lifecycle-hook-deletion-etcd_deleting-machine)

</div>

# Application backup and restore operations

As a cluster administrator, you can back up and restore applications running on OpenShift Container Platform by using the OpenShift API for Data Protection (OADP).

OADP backs up and restores Kubernetes resources and internal images, at the granularity of a namespace, by using the version of Velero that is appropriate for the version of OADP you install, according to the table in [Downloading the Velero CLI tool](application_backup_and_restore/troubleshooting/velero-cli-tool.md#velero-obtaining-by-downloading_velero-cli-tool). OADP backs up and restores persistent volumes (PVs) by using snapshots or Restic. For details, see [OADP features](application_backup_and_restore/oadp-features-plugins.md#oadp-features_oadp-features-plugins).

## OADP requirements

OADP has the following requirements:

- You must be logged in as a user with a `cluster-admin` role.

- You must have object storage for storing backups, such as one of the following storage types:

  - OpenShift Data Foundation

  - Amazon Web Services

  - Microsoft Azure

  - Google Cloud

  - S3-compatible object storage

  - IBM Cloud® Object Storage S3

> [!NOTE]
> If you want to use CSI backup on OCP 4.11 and later, install OADP 1.1.*x*.
>
> OADP 1.0.*x* does not support CSI backup on OCP 4.11 and later. OADP 1.0.*x* includes Velero 1.7.*x* and expects the API group `snapshot.storage.k8s.io/v1beta1`, which is not present on OCP 4.11 and later.

- To back up PVs with snapshots, you must have cloud storage that has a native snapshot API or supports Container Storage Interface (CSI) snapshots, such as the following providers:

  - Amazon Web Services

  - Microsoft Azure

  - Google Cloud

  - CSI snapshot-enabled cloud storage, such as Ceph RBD or Ceph FS

> [!NOTE]
> If you do not want to back up PVs by using snapshots, you can use [Restic](https://restic.net/), which is installed by the OADP Operator by default.

## Backing up and restoring applications

You back up applications by creating a `Backup` custom resource (CR). See [Creating a Backup CR](application_backup_and_restore/backing_up_and_restoring/oadp-creating-backup-cr.md#backing-up-applications). You can configure the following backup options:

- [Creating backup hooks](application_backup_and_restore/backing_up_and_restoring/oadp-creating-backup-hooks-doc.md#backing-up-applications) to run commands before or after the backup operation

- [Scheduling backups](application_backup_and_restore/backing_up_and_restoring/oadp-scheduling-backups-doc.md#backing-up-applications)

- [Backing up applications with File System Backup: Kopia or Restic](application_backup_and_restore/backing_up_and_restoring/oadp-backing-up-applications-restic-doc.md#backing-up-applications)

- You restore application backups by creating a `Restore` (CR). See [Creating a Restore CR](application_backup_and_restore/backing_up_and_restoring/restoring-applications.md#oadp-creating-restore-cr_restoring-applications).

- You can configure [restore hooks](application_backup_and_restore/backing_up_and_restoring/restoring-applications.md#oadp-creating-restore-hooks_restoring-applications) to run commands in init containers or in the application container during the restore operation.
