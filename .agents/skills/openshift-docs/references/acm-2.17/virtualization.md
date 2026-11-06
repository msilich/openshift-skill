> Source: [Red Hat Advanced Cluster Management for Kubernetes 2.17](https://docs.redhat.com/en/documentation/red_hat_advanced_cluster_management_for_kubernetes/2.17/html/virtualization/index). Copyright Red Hat.
> Adapted from AsciiDoc to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md), [CC BY-SA 3.0](LICENSE.md) and SOURCE.json for source revisions and gaps.

<a id="acm-virt"></a>

# Virtualization

Manage Red Hat OpenShift Virtualization virtual machine resources across all the clusters that Red Hat Advanced Cluster Management manages. To use virtualization capabilities in Red Hat Advanced Cluster Management, ensure that a supported version of OpenShift Container Platform and the Red Hat OpenShift Virtualization operator is installed on the clusters that you want to manage. For instance, for Red Hat Advanced Cluster Management 2.16, you need to use Red Hat OpenShift Virtualization 4.21.1 or later.

To view `VirtualMachine` resources across all the clusters that Red Hat Advanced Cluster Management manages, use the Search service to list and filter the `VirtualMachine` resources that are created with the Red Hat OpenShift Virtualization. You can also enable the following actions from the Red Hat Advanced Cluster Management console on your `VirtualMachine` resources:

- Start

- Stop

- Restart

- Pause

- Unpause

- Snapshot

Learn more about virtual machine capability:

- [Viewing virtual machine metrics through observability fields](virtualization.md#view-vm-metrics-observability)

- [Configuring backup policies for Red Hat OpenShift Virtualization](virtualization.md#backup-config-policy-virt)

- [Backing up and restoring a virtual machine](virtualization.md#backup-restore-vm)

- [Virtualization policies installed on the hub cluster](virtualization.md#backup-virt-policies)

- [Defining policies with *ConfigMap* resources](virtualization.md#backup-virt-define-configmap)

- [Virtualization policy *ConfigMap* overview](virtualization.md#backup-virt-configmap-ref)

- [Preparing to migrate virtual machines between clusters](virtualization.md#preparing-virt-migration)

- [Migrating virtual machines between clusters](virtualization.md#migrate-virt-machines)

<a id="view-vm-metrics-observability"></a>

## Viewing virtual machine metrics through Observability fields

If you have the Observability service installed on your hub cluster, you can access the Observability fields on the Red Hat Advanced Cluster Management console to view your virtual machine metrics.

<div>

<div class="title">

Procedure

</div>

1.  On the Red Hat Advanced Cluster Management console, go to the `Virtual Machine` page.

2.  Select the `Observability dashboards` link to launch the `Grafana` dashboard.

    1.  **Optional:** Select the `Observability metrics` link in the `Launch links` table cell to launch the `Grafana` dashboard,

3.  From the `Grafana` dashboard, view the virtual machines and their individual metrics.

</div>

<a id="backup-config-policy-virt"></a>

## Configuring backup policies for Red Hat OpenShift Virtualization

Use OpenShift APIs for Data Protection to backup and restore virtual machines. After you back up the virtual machines, you can restore it on the hub or managed clusters. To configure the policies, and either enable a backup schedule or run a restore operation for a virtual machine.

Red Hat Advanced Cluster Management policies for OpenShift Virtualization support the following backup and restore storage options:

- Container Storage Interface (CSI) backups

- Container Storage Interface (CSI) backups with DataMover

Red Hat Advanced Cluster Management policies do not support the following options:

- File system backup and restore

- Volume snapshot backups and restores

<div>

<div class="title">

Procedure

</div>

1.  Back up and restore a virtual machine. See [Backing up and restoring a virtual machine](virtualization.md#backup-restore-vm).

2.  Review the virtualization policies that are installed on the hub cluster. See [Virtualization policies installed on the hub cluster](virtualization.md#backup-virt-policies).

3.  Define the policies with `ConfigMaps`. See [Defining policies with *ConfigMap* resources](virtualization.md#backup-virt-define-configmap).

4.  Review the virtualization policy `ConfigMaps`. See [Virtualization policy *ConfigMap* overview](virtualization.md#backup-virt-configmap-ref).

</div>

<a id="backup-restore-vm"></a>

## Backing up and restoring a virtual machine

You can back up virtual machines that run on a cluster, or restore a virtual machine on a cluster. Complete the following steps.

<div>

<div class="title">

Procedure

</div>

1.  Enable the backup component on the hub cluster by setting the `cluster-backup` parameter in the `MultiClusterHub` resource to `true`.

2.  To place the policies on the `cluster-name` cluster, add the `acm-virt-config` label to the `ManagedCluster` resource by applying the following YAML sample:

    ``` yaml
    apiVersion: cluster.open-cluster-management.io/v1
    kind: ManagedCluster
    metadata:
     name: cluster-name
     labels:
       acm-virt-config: acm-dr-virt-config
    ```

    - The `acm-dr-virt-config` that passes through the label annotation is a `acm-virt-config` ConfigMap. Read the `acm-dr-virt-config` `ConfigMap` section to understand how to configure OpenShift APIs for Data Protection and backup storage location.

3.  Complete the following steps, depending on whether you want to backup or restore your virtual machine:

    1.  Back up your virtual machine by adding the `cluster.open-cluster-management.io/backup-vm` to the `kubevirt.io.VirtualMachine` resource. Your `kubevirt.io.VirtualMachine` resource might resemble the following YAML sample:

    ``` yaml
    apiVersion: kubevirt.io/v1
    kind: VirtualMachine
    metadata:
      name: vm-name
      labels:
        cluster.open-cluster-management.io/backup-vm: daily_8am
    ```

    1.  Restore your virtual machine by updating the `acm-dr-restore-config` `ConfigMap` as described in [Virtualization policy *ConfigMap* overview](virtualization.md#backup-virt-configmap-ref).

</div>

<a id="backup-virt-policies"></a>

## Virtualization policies installed on the hub cluster

When you enable the backup operator, a set of Red Hat Advanced Cluster Management policies and config maps are installed on the hub cluster. When you disable the policy or remove it from the cluster, all the resources that the policy created is removed. Learn more about the policies and config maps that are installed on the hub cluster.

- Installation policy

  The `acm-dr-virt-install` installation policy installs OpenShift APIs for Data Protection and configures the `oadp.openshift.io.DataProtectionApplication` resource on the cluster where this policy is placed.

  For the hub cluster, the policy verifies that OpenShift APIs for Data Protection is installed in the `open-cluster-management-backup` namespace, and that the `DataProtectionApplication` resource exists and has the required configuration. The policy does not attempt to install OpenShift APIs for Data Protection, or create the `DataProtectionApplication` resource on the hub cluster.

  When you enable the `cluster-backup` option on the `MultiClusterHub` resource, the backup chart installs the OpenShift APIs for Data Protection. When you enable the `cluster-backup-option`, you create the `DataProtectionApplication` on the hub cluster.

  |  |  |
  |----|----|
  | Template | Description |
  | `check-config-file` | Verifies that the `ConfigMap` that is defined by the `acm-virt-config` label set on the `ManagedCluster` resource exists on the hub cluster, in the `open-cluster-management-backup` namespace. |
  | `check-oadp-channel` | Verifies if there is an OpenShift APIs for Data Protection version installed on the cluster, and that it matches the version installed by the policy. |
  | `check-dpa-config` | Verifies that the `DataProtectionApplication` resource exists, has the expected configuration, and has a status of `Reconciled`. Verifies that the `BackupStorageLocation` exists and is in the `Available` status phase. |
  | `install-oadp-copy-config` | Creates the namespace where OpenShift APIs for Data Protection gets installed, if this namespace is not found. Copies the OpenShift APIs for Data Protection secret and installs OpenShift APIs for Data Protection, but only for managed clusters. Creates the `DataProtectionApplication` resource as defined by the `acm-virt-config` label, but only for the managed clusters. The user must manually create the OpenShift APIs for Data Protection and `DataProtectionApplication` on the hub cluster. |

  Installation policy templates

- Backup policy

  The `acm-dr-virt-backup` backup policy backs up the `kubevirt.io.VirtualMachine` resources that has the `cluster.open-cluster-management.io/backup-vm: schedule_cron_name` label.

  |  |  |
  |----|----|
  | Template | Description |
  | `check-cron-schedule-valid` | Shows a violation error if there is any cron schedule name used by a virtual machine `cluster.open-cluster-management.io/backup-vm` label which is not found in the `ConfigMap` for the cron schedules. The name of the `ConfigMap` for the cron schedules is defined by the `schedule_hub_config_name` property and is available within the `open-cluster-management-backup namespace`. |
  | `check-backup-status-completed` | If the schedule is not paused, it verifies that the status is `Enabled`. Finds the latest backup generated by this schedule and verifies that the status is `Completed`. If any `DataUpload` has been created for this backup, the status is `Completed`. Shows a violation if any of these conditions are not `True`. |
  | `create-virt-backup` | Creates Velero schedules for all virtual machine resources with a `cluster.open-cluster-management.io/backup-vm` label. Creates one schedule for each cron job schedule found with the virtual machines label. Backs up the virtual machine sharing the same cron job schedule within the same backup. Creates the Velero schedule resource only if the `acm-dr-virt-install` policy is compliant. |

  Backup policy templates

- Restore policy

  The `acm-dr-virt-restore` restore policy restores the `kubevirt.io.VirtualMachine` resources by UID. The policy creates Velero restore resources on clusters using the information from the `ConfigMap` that is identified by the `restore_hub_config_name` property from the `acm-dr-virt-config` `ConfigMap`.

  |  |  |
  |----|----|
  | Template | Description |
  | `check-velero-restore-status` | Verifies that the restore resource with the name defined by the `clusterID_restoreName` property exists and has a status of `Completed`. |
  | `create-velero-restore` | If the `clusterID_restoreName` property value is not empty, and the `clusterID` matches this cluster UID, it creates a Velero restore resources using the properties defined with the `ConfigMap` that is identified by the `restore_hub_config_name`. Creates the Velero restore resource only if the `acm-dr-virt-install` policy is compliant. |

  Restore policy templates

<a id="backup-virt-define-configmap"></a>

## Defining policies with *ConfigMap* resources

The `acm-dr-virt-config` config map defines the OpenShift APIs for Data Protection configuration and other settings that are related to the backup or restore operation. You can use the name of this resource as the value for the `acm-virt-config` label, which is set on the managed cluster where the policies are placed. You can also create a new `ConfigMap` resource that uses the `acm-dr-virt-config` as a sample, then use your new `ConfigMap` resource to place the virtualization policies on the cluster.

<div>

<div class="title">

Procedure

</div>

1.  Use the `acm-dr-virt-config` or create a new `ConfigMap` resource on the hub cluster in the `open-cluster-management-backup` namespace by using the `acm-dr-virt-config-new` `ConfigMap` as an example.

    1.  Update the `dpa_spec` section to match the storage location where you want to store the backups that are created by OpenShift APIs for Data Protection.

    2.  **Optional:** Update other properties that are available with the `acm-dr-virt-config-new` `ConfigMap`, such as OpenShift APIs for Data Protection version or channel.

2.  Add the `acm-virt-config=acm-dr-virt-config-new` label to the `ManagedCluster` resource. The value of the `acm-virt-config` label is the name of the config map that you created. For an example of a `ManagedCluster` resource with a virtualization backup label set to use `acm-dr-virt-config-new`, see the following YAML sample:

    ``` yaml
    apiVersion: cluster.open-cluster-management.io/v1
    kind: ManagedCluster
    metadata:
     name: managed-cluster-name
     labels:
       acm-virt-config: acm-dr-virt-config-new
    ```

</div>

<div>

<div class="title">

Next steps

</div>

- See [Virtualization policy *ConfigMap* overview](virtualization.md#backup-virt-configmap-ref) for ConfigMap properties, schedule configuration, and restore ConfigMap examples.

</div>

<a id="backup-virt-configmap-ref"></a>

## Virtualization policy *ConfigMap* overview

When you install the policies on the hub cluster, the following `ConfigMap` resources are created on the hub cluster, in the `open-cluster-management-backup` namespace. When you place the virtualization policies on the hub or managed cluster, these `ConfigMap` resources define the backup and restore configuration for the virtualization policies.

|  |  |  |  |  |
|----|----|----|----|----|
| Name | Description | Type | Default value | Optional |
| `channel` | The channel defaults to the supported OpenShift APIs for Data Protection version, which is based on the version of the OpenShift Container Platform cluster. Use this property to overwrite the default value. | String | None | Yes |
| `channelName` | OpenShift APIs for Data Protection channel name. Set this property for custom installation, for example: `offline install`. | String | `redhat-oadp-operator` | Yes |
| `subscriptionSource` | OpenShift APIs for Data Protection subscription. Set this property for custom installation, for example: `offline install`. | String | `redhat-operators` | Yes |
| `subscriptionSourceNamespace` | OpenShift APIs for Data Protection subscription source. Set this property for custom installation, for example: `offline install`. | String | `openshift-marketplace` | Yes |
| `subscriptionStartingCSV` | OpenShift APIs for Data Protection subscription startingCSV. | String | None | Yes |
| `subscriptionInstallPlanApproval` | OpenShift APIs for Data Protection install plan. | String | Automatic | Yes |
| `backupNS` | Namespace where OpenShift APIs for Data Protection gets installed on the managed cluster. | String | None | No |
| `credentials_hub_secret_name` | Name of the OpenShift APIs for Data Protection secret that you use on the managed cluster. A Secret with this name must exist on the hub cluster in the `open-cluster-management-backup` namespace. The install policy moves this secret to the hub cluster within the specified `backupNS` namespace. | String | None | No |
| `credentials_name` | Name of the secret used by the OpenShift APIs for Data Protection `DataProtectionApplication` resource on the managed cluster, when setting the Velero credential name. | JSON | None | No |
| `dpa_name` | Name of the `DataProtectionApplication` resource that gets created on the managed cluster. | String | None | No |
| `dpa_spec` | Valid JSON defining the `DataProtectionApplication` spec when created on the managed cluster. | JSON | None | No |

`ConfigMap` properties for the `acm-dr-virt-install` policy

|  |  |  |  |  |
|----|----|----|----|----|
| Name | Description | Type | Default value | Optional |
| `scheduleTTL` | Backup expiration time. | String | `24h0m0s` | Yes |
| `schedule_paused` | Set to `True` to pause the virtualization backup schedule. | String | False | Yes |
| `schedule_hub_config_name` | Name of the `ConfigMap` that is used to define the valid cron jobs schedules. A `ConfigMap` with this name must exist on the hub cluster in the `open-cluster-management-backup` namespace. | String | None | Yes |

`ConfigMap` properties for the `acm-dr-virt-backup` policy

|  |  |  |  |  |
|----|----|----|----|----|
| Name | Description | Type | Default value | Optional |
| `restore_hub_config_name` | Name of the ConfigMap that is used to define the restore operation. This name must exist on the hub cluster in the `open-cluster-management-backup` namespace | String | None | No |

`ConfigMap` properties for the `acm-dr-virt-restore` policy

- Example of a `acm-dr-virt-schedule-cron` `ConfigMap`

  Use the `acm-dr-virt-schedule-cron` `ConfigMap` to define the valid cron job schedules to use when you are scheduling a virtual machine backup. The `acm-dr-virt-schedule-cron` `ConfigMap` is created by the hub cluster backup component in the `open-cluster-management-backup` namespace and includes the following YAML:

  ``` yaml
  apiVersion: v1
  kind: ConfigMap
      metadata:
          name: acm-dr-virt-schedule-cron
          namespace: open-cluster-management-backup
      data:
          hourly: "0 */1 * * *"
          every_2_hours: "0 */2 * * *"
          every_3_hours: "0 */3 * * *"
          every_4_hours: "0 */4 * * *"
          every_5_hours: "0 */5 * * *"
          every_6_hours: "0 */6 * * *"
          twice_a_day: "0 */12 * * *"
          daily_8am: "0 8 * * *"
          every_sunday: "0 0 * * 0"
  ```

- Example `VirtualMachine` with a daily backup schedule

  You can use any of the schedules created by the `acm-dr-virt-schedule-cron` `ConfigMap` to set the backup schedule for a `kubevirt.io.VirtualMachine`. For example, if you want to backup a virtual machine every day at 8am, add the following label to the virtual machine resource:

  ``` yaml
  apiVersion: kubevirt.io/v1
  kind: VirtualMachine
  metadata:
    name: vm-name
    labels:
      cluster.open-cluster-management.io/backup-vm: daily_8am
  ```

  Since this `acm-dr-virt-schedule-cron` `ConfigMap` is created and managed by the hub cluster backup component, you cannot change any of the existing cron properties or delete them. The properties are recreated when the content is reconciled. You can only add new properties to the existing ones. For example, if you want to create a cron job to run every Saturday, add the following label to the existing `acm-dr-virt-schedule-cron` properties: `every_sunday: "0 0 * * SAT"`.

- Example of complete restore operation in the `acm-dr-virt-restore-config` `ConfigMap`

  Use the `acm-dr-virt-restore-config` `ConfigMap` to define the restore operations to be implemented by the `acm-dr-virt-restore` policy. Use the hub cluster backup component in the `open-cluster-management-backup` namespace to create the `ConfigMap`. For an example of a complete restore operation, see the following YAML sample:

  ``` yaml
  kind: ConfigMap
  apiVersion: v1
  metadata:
   name: acm-dr-virt-restore-config
   namespace: open-cluster-management-backup
  data:
   2a054d24-3235-4249-9c81-f58ebc6110c7_backupName: acm-rho-virt-schedule-every-10-hours-20250120230438
   2a054d24-3235-4249-9c81-f58ebc6110c7_restoreName: restore-20250120230438
   2a054d24-3235-4249-9c81-f58ebc6110c7_vmsUID: 2a054d24-3235-4249-9c81-f58ebc6110c7
   2a054d24-3235-4249-9c81-f58ebc6110c7_namespaceMapping: backup-ns-1=restore-ns-1{{ backup-ns-2=restore-ns-2}}
  ```

  - `2a054d24-3235-4249-9c81-f58ebc6110c7` is the cluster ID where the restore operation is complete. `acm-rho-virt-schedule-every-10-hours-20250120230438` is the name of the backup that is used for the restore operation example.

  - `restore-20250120230438` is the name of the `Restore` resource that is created as a result of this restore operation.

  - `2a054d24-3235-4249-9c81-f58ebc6110c7` is the UID of the virtual machine backed up with the `acm-rho-virt-schedule-every-10-hours-20250120230438` backup to be restored.

  - `namespaceMapping` is an optional property and is used to restore resources in a different namespace than the initial resource. Any source namespaces not included in the map is restored into namespaces of the same name. `backup-ns-1=restore-ns-1 backup-ns-2=restore-ns-2` is a space separated list of namespace mapping. In this sample, backup resources created within the `backup-ns-1` namespace are restored within the `restore-ns-1` namespace. The `restore-ns-1` is created on the restore cluster if it does not exist. Similarly, resources created within the `backup-ns-2` are restored within the `restore-ns-2` namespace.

- Virtualization policies for your restore operations scenarios

  - If you set the `clusterID_restoreName` property from the `acm-dr-virt-restore-config` `ConfigMap` to an empty value, then the restore resource created by the `acm-dr-virt-restore` policy on the cluster with `clusterID` gets deleted.

  - If you set the `clusterID_restoreName` property from the `acm-dr-virt-restore-config` `ConfigMap` to a non-empty value, then the `acm-dr-virt-restore` policy creates a Velero `Restore` resource . The name of the Velero restore resource matches the `clusterID_restoreName` value. If the restore resource with this name is deleted from the restore cluster, the `acm-dr-virt-restore` policy recreates the resource, which results in the restore operation running again.

- Important considerations for your restore operations scenarios

  - Do not delete the restore resource if you do not want to run the restore again.

  - Remove the value for the `clusterID_restoreName` parameter on the `acm-dr-virt-restore-config` `ConfigMap` when the restore operation gets verified to start. Doing this prevents you from having to rerun the restore operation if the `acm-dr-virt-restore` policy is disabled and enabled again. When you disable the `acm-dr-virt-restore` policy, all resources created by it on the restore cluster get cleaned up and recreated when you enable the policy again.

<div>

<div class="title">

Additional resources

</div>

- [Defining policies with *ConfigMap* resources](virtualization.md#backup-virt-define-configmap)

</div>

<a id="preparing-virt-migration"></a>

## Preparing to migrate virtual machines between clusters

Migrating virtual machines helps you move resources during cluster upgrades, times when you need to clear a node for maintenance, or during configuration changes. When you enable migration, the Red Hat OpenShift Virtualization is automatically installed on your managed clusters with the `acm/cnv-operator-install` label. The migration toolkit for virtualization is also installed on your hub cluster.

**Required access:** Cluster administrator

Before you perform migration operations or access the Fleet Virtualization console, ensure that the following requirements are met:

|  |  |  |
|----|----|----|
| Role | Location | Purpose |
| `acm-vm-fleet:admin` | Hub cluster | Perform migration operations and access the Fleet Virtualization console. |
| `acm-vm-extended:admin` | Source and target clusters | Manage virtual machine extended and related resources. |
| `acm-vm-cluster-migration:view` | Target cluster | Perform mandatory cluster version and Red Hat OpenShift Virtualization operator readiness checks. |

Required roles table

<div>

<div class="title">

Procedure

</div>

1.  Enable fine-grained RBAC on your clusters to assign and use the required roles. See [Enabling fine-grained role-based access control for virtualization](secure_clusters.md#fine-grain-enable).

2.  Ensure you have access to the `openshift-cnv` namespace.

3.  Ensure you have the `kubevirt.io:admin` role on both the source and target clusters.

4.  Install the latest supported version of OpenShift Container Platform. See the [OpenShift Container Platform overview](https://access.redhat.com/documentation/en-us/openshift_container_platform/).

5.  Understand the required roles for migration operations and access to the Fleet Virtualization console. See the following table for more information about the required roles. For additional details about fine-grained roles and permissions, see the [Fine-grained RBAC roles and descriptions](secure_clusters.md#fine-grain-roles-descriptions) documentation.

6.  See [Migrating virtual machines between clusters](virtualization.md#migrate-virt-machines) to complete the migration procedure.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Live migration](https://docs.redhat.com/en/documentation/openshift_container_platform/4.20/html/virtualization/live-migration#virt-preserving-lm-perms_virt-about-live-migration)

</div>

<a id="migrate-virt-machines"></a>

## Migrating virtual machines between clusters

Complete the following steps to enable virtual machine migration between clusters and verify that the required operators are available.

<div>

<div class="title">

Procedure

</div>

1.  Add the `ClusterPermission` resource to enable the `kubevirt.io:admin` role on both the source and target clusters. See the following YAML sample for the `ClusterPermission` resource. Replace `cluster-name` with the name of your cluster:

    ``` yaml
    apiVersion: rbac.open-cluster-management.io/v1alpha1
    kind: ClusterPermission
    metadata:
      name: kubevirt-admin
      namespace: cluster-name
    spec:
      clusterRoleBinding:
        roleRef:
          apiGroup: rbac.authorization.k8s.io
          kind: ClusterRole
          name: kubevirt.io:admin
        subject:
          kind: Group
          name: system:cluster-admins
          apiGroup: rbac.authorization.k8s.io
    ```

2.  Enable `cnv-mtv-integrations` component for the integration of Red Hat OpenShift Virtualization.

    1.  Run the following command to edit your `multiclusterhub` instance:

    ``` bash
    oc edit MultiClusterHub multiclusterhub -n open-cluster-management
    ```

    1.  From the `components` specification, set the `enabled` parameter to `true` for the `cnv-mtv-integrations` component.

3.  Verify that the migration toolkit for virtualization is available on your cluster. Run the following command:

    ``` bash
    oc get clustermanagementaddon mtv-operator  -o jsonpath='{.status.installProgressions[*].conditions[*].reason}'
    ```

4.  Verify that the `kubevirt-hyperconverged` resource is available on your cluster with the following command:

    ``` bash
    oc get clustermanagementaddon kubevirt-hyperconverged -o jsonpath='{.status.installProgressions[*].conditions[*].reason}
    ```

5.  Verify that the `kubevirt-hyperconverged-operator` is available on your cluster with the following command:

    ``` bash
    oc get clustermanagementaddon kubevirt-hyperconverged-operator -o jsonpath='{.status.installProgressions[*].conditions[*].reason}'
    ```

6.  To designate a cluster as a source or target for the virtual machine migration, apply the following label to your clusters: `acm/cnv-operator-install: "true"`.

7.  **Optional:** If you don’t see the Virtualization console, run the following command:

    ``` bash
    oc -n openshift-cnv patch hco kubevirt-hyperconverged --type='merge' -p '{"spec":{"featureGates":{"decentralizedLiveMigration":true}}}'
    ```

8.  **Optional:** If you want to further configure your environment in the managed cluster, edit the `HyperConverged` resource.

</div>
