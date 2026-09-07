<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

To back up etcd data for hosted control planes, you can use the default volume snapshot approach, or you can take the etcd snapshot approach, which results in smaller backup artifacts.

> [!IMPORTANT]
> The etcd snapshot method is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.
>
> For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

# Overview of the etcd snapshot method

You can use the etcd snapshot method as an alternative to the default volume snapshot approach to back up etcd data for hosted control planes. The etcd snapshot method results in smaller backup artifacts.

Instead of capturing persistent volume claim (PVC) content by using container storage interface (CSI) volume snapshots or a filesystem backup, you can take a snapshot of the etcd database and upload it to object storage.

The etcd snapshot approach is driven by the `HCPEtcdBackup` custom resource and is orchestrated through the OpenShift API for Data Protection (OADP) HyperShift plugin during Velero backup operations.

For a more detailed comparison of the etcd snapshot method and the default volume snapshot method, see the following table.

| Aspect | Volume snapshot (default) | etcd snapshot |
|----|----|----|
| Backup mechanism | CSI volume snapshots or a Kopia filesystem backup of etcd PVCs. One per replica; typically 3. | The `etcdctl snapshot save` mechanism produces a single snapshot file and uploads it to object storage. |
| Portability | Tied to the storage provider and the CSI driver. | Storage-agnostic. |
| Backup size | Full PVC content. Highly available deployments have 3 PVCs. | A single etcd database snapshot. |
| Restore mechanism | PVC restore from snapshot. | `etcdutl snapshot restore` by using the init container. |
| Requirements | A CSI driver with snapshot support or a Kopia node agent. | The `HCPEtcdBackup` feature gate must be enabled. |
| Encryption | Depends on the storage provider. | Optional Key Management Service (KMS) encryption for hosted control planes on AWS. |

Comparing the etcd snapshot and volume snapshot methods

# Configuring the etcd snapshot method

Before you can use the etcd snapshot method to back up your etcd data for hosted control planes, you must meet a few prerequisites and configure a plugin.

<div>

<div class="title">

Prerequisites

</div>

- The `HCPEtcdBackup` feature gate is enabled in the HyperShift Operator.

- The OpenShift API for Data Protection (OADP) Operator version 1.6 or later with the HyperShift plugin is deployed. For more information, see "Configuring OADP" and "Automating the backup and restore process by using a DPA".

- Object storage is configured. Use a Velero backup storage location that points to AWS S3.

- Service publishing requirements:

  - If you are restoring a hosted cluster to a different management cluster, use a fixed hostname that is configured through DNS so that you can update the DNS record to point to the endpoint of the new management cluster and make the migration transparent for existing nodes.

  - For production environments, all services must have fixed hostnames.

  - On AWS, the API server can also use a `Route` service publishing strategy with a fixed hostname.

- Platform-specific requirements:

  - For hosted control planes on AWS, ensure that the OIDC provider configuration is accessible for any fixes that are needed after the restore process. If you use AWS S3 for backup storage, ensure that IAM roles and policies are configured according to "About installing OADP".

  - For hosted control planes on bare metal with the Agent provider, ensure that the `InfraEnv` resource is in a separate namespace from the hosted control plane namespace. Be careful to not delete the `InfraEnv` resource during the backup or restore processes.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Configure the OADP HyperShift plugin by creating a config map in the OADP namespace and specifying the etcd backup method, as shown in the following example:

    ``` yaml
    apiVersion: v1
    kind: ConfigMap
    metadata:
      name: hypershift-oadp-plugin-config
      namespace: openshift-adp
    data:
      etcdBackupMethod: "etcdSnapshot"
    ```

    where:

    metadata.name
    Specifies the name of the config map. Use `hypershift-oadp-plugin-config` as the name of the config map.

    metadata.namespace
    Specifies the OADP namespace.

    data.etcdBackupMethod
    Specifies the etcd backup method. The default is `volumeSnapshot`. Use `etcdSnapshot` to enable the etcd snapshot method. If the `etcdBackupMethod` parameter is set to `etcdSnapshot` but the `HCPEtcdBackup` custom resource is not installed, the plugin fails.

2.  Apply the configuration by entering the following command:

    ``` terminal
    $ oc apply -f hypershift-oadp-plugin-config.yaml
    ```

</div>

<div>

<div class="title">

Additional resources

</div>

- [Configuring OADP](hcp-disaster-recovery-oadp-auto.md#hcp-dr-prep-oadp-auto_hcp-disaster-recovery-oadp-auto)

- [Automating the backup and restore process by using DPA](hcp-disaster-recovery-oadp-auto.md#hcp-dr-oadp-dpa_hcp-disaster-recovery-oadp-auto)

- [About installing OADP](../../backup_and_restore/application_backup_and_restore/installing/about-installing-oadp.md#about-installing-oadp)

</div>

# Backing up etcd data by using the etcd snapshot method

You can start the etcd snapshot backup process from the hosted control planes command-line interface (CLI).

<div>

<div class="title">

Prerequisite

</div>

- You completed the steps in "Configuring the etcd snapshot method".

</div>

<div>

<div class="title">

Procedure

</div>

- Start the backup process by entering the following command:

  ``` terminal
  $ hcp create oadp-backup \
    --hc-name <my_hosted_cluster> \
    --hc-namespace <my_hosted_cluster_namespace> \
    --name <my_backup> \
    --storage-location default \
    --use-etcd-snapshot
  ```

  The command generates an `oadp-backup` custom resource (CR) that includes the namespaces of the hosted cluster and the hosted control plane, a platform-aware resource list that excludes etcd-related resources, and snapshot settings.

  Next, the OADP HyperShift plugin and the `HCPEtcdBackup` CR work to complete the backup process.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Configuring the etcd snapshot method](hcp-backup-etcd-snapshot.md#hcp-backup-etcd-snapshot-config_hcp-backup-etcd-snapshot)

</div>

# Restoring etcd data by using the etcd snapshot method

You can specify a backup to recover from or set a schedule to run the recovery process on.

The process to recover a hosted control plane from an etcd snapshot backup involves the OADP HyperShift plugin, the Control Plane Operator, and the etcd init container.

<div>

<div class="title">

Prerequisites

</div>

- You completed the steps in "Configuring the etcd snapshot method".

- No running pods or persistent volume claims (PVCs) are in the hosted control plane namespace. If you are restoring on the same management cluster, delete the hosted cluster and node pools first.

- The status of the Velero backup is `status.phase: Completed`.

- The OADP components are running and the `DataProtectionApplication` (DPA) custom resource (CR) is reconciled.

- For hosted control planes on AWS, your backup storage location (BSL) credentials are valid and have permission to read the snapshot from S3.

- For bare metal on the Agent platform, your `InfraEnv` objects are preserved. Do not delete them.

</div>

<div>

<div class="title">

Procedure

</div>

- Start the restore process by entering the following command:

  ``` terminal
  $ hcp create oadp-restore \
    --hc-name <my_hosted_cluster> \
    --hc-namespace <my_hosted_cluster_namespace> \
    --name <my_restore> \
    --from-backup <my_backup>
  ```

  where:

  `<my_backup>`
  Specifies the name of the backup to use. If you run the restore process on a schedule, replace the `--from-backup` flag with the `--from-schedule` flag and specify the name of the schedule to use.

</div>

<div>

<div class="title">

Verification

</div>

1.  Check that the etcd pods are running and that the cluster is functioning as expected by entering the following command:

    ``` terminal
    $ oc get pods -n <my_hosted_cluster_namespace>-<my_hosted_cluster> -l app=etcd
    ```

2.  Check the restore conditions by entering the following command:

    ``` terminal
    $ oc get hostedcluster <my_hosted_cluster> -n <my_hosted_cluster_namespace> -o jsonpath='{.status.conditions}' | jq '.[] | select(.type | test("Restore|Etcd"))'
    ```

3.  On AWS deployments, when you restore to a different management cluster, the OIDC provider might need to be updated. Enter the following command:

    ``` terminal
    $ hcp fix dr-oidc-iam --hc-name <my_hosted_cluster> --hc-namespace <my_hosted_cluster_namespace>
    ```

4.  Confirm that the API server of the hosted cluster is accessible by entering the following command:

    ``` terminal
    $ oc --kubeconfig <hosted_cluster_kubeconfig> get nodes
    ```

5.  Confirm that workloads are running by entering the following command:

    ``` terminal
    $ oc --kubeconfig <hosted_cluster_kubeconfig> get clusteroperators
    ```

</div>

<div>

<div class="title">

Additional resources

</div>

- [Configuring the etcd snapshot method](hcp-backup-etcd-snapshot.md#hcp-backup-etcd-snapshot-config_hcp-backup-etcd-snapshot)

</div>

# Condition codes for the etcd snapshot method

During the backup and restore process with the etcd snapshot method, you might see messages about the condition of hosted control planes resources.

| Resource | Condition, field, or annotation | Meaning |
|----|----|----|
| `HCPEtcdBackup` | `BackupCompleted` | Tracks the backup lifecycle: `InProgress`, `Succeeded`, `Failed`, `Rejected`, or `EtcdUnhealthy`. |
| `HostedControlPlane` | `EtcdSnapshotRestored` | This value is set to `True` after etcd is restored from the snapshot. |
| `HostedCluster` | `Status.LastSuccessfulEtcdBackupURL` | Persists the last snapshot URL. After a successful backup, the HyperShift Operator sets this condition. |
| `HostedCluster` | `etcd-snapshot-url` | The OADP plugin inserts this annotation during the backup process. During the restore process, the plugin reads this annotation to set the `RestoreSnapshotURL` value. |
| `HostedCluster` | `restored-from-backup` | This annotation is set during the restore process. It is removed after the `HostedClusterRestoredFromBackup` condition is `True`. |

Explanations of conditions during etcd snapshot backup and restore processes
