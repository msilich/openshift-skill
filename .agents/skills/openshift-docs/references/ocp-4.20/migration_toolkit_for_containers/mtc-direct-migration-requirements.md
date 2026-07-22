<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Direct Migration is available with Migration Toolkit for Containers (MTC) 1.4.0 or later.

There are two parts of the Direct Migration:

- Direct Volume Migration

- Direct Image Migration

Direct Migration enables the migration of persistent volumes and internal images directly from the source cluster to the destination cluster without an intermediary replication repository (object storage).

# Prerequisites

- Expose the internal registries for both clusters (source and destination) involved in the migration for external traffic.

- Ensure the remote source and destination clusters can communicate using OpenShift Container Platform routes on port 443.

- Configure the exposed registry route in the source and destination MTC clusters; do this by specifying the `spec.exposedRegistryPath` field or from the MTC UI.

  <div class="note">

  <div class="title">

  </div>

  - If the destination cluster is the same as the host cluster (where a migration controller exists), there is no need to configure the exposed registry route for that particular MTC cluster.

  - The `spec.exposedRegistryPath` is required only for Direct Image Migration and not Direct Volume Migration.

  </div>

- Ensure the two spec flags in `MigPlan` custom resource (CR) `indirectImageMigration` and `indirectVolumeMigration` are set to `false` for Direct Migration to be performed. The default value for these flags is `false`.

The Direct Migration feature of MTC uses the Rsync utility.

# Rsync configuration for direct volume migration

Direct Volume Migration (DVM) in MTC uses Rsync to synchronize files between the source and the target persistent volumes (PVs), using a direct connection between the two PVs.

Rsync is a command-line tool that allows you to transfer files and directories to local and remote destinations.

The `rsync` command used by DVM is optimized for clusters functioning as expected.

The `MigrationController` CR exposes the following variables to configure `rsync_options` in Direct Volume Migration:

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 15%" />
<col style="width: 20%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Variable</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Default value</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>rsync_opt_bwlimit</code></p></td>
<td style="text-align: left;"><p>int</p></td>
<td style="text-align: left;"><p>Not set</p></td>
<td style="text-align: left;"><p>When set to a positive integer, <code>--bwlimit=&lt;int&gt;</code> option is added to Rsync command.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>rsync_opt_archive</code></p></td>
<td style="text-align: left;"><p>bool</p></td>
<td style="text-align: left;"><p><code>true</code></p></td>
<td style="text-align: left;"><p>Sets the <code>--archive</code> option in the Rsync command.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>rsync_opt_partial</code></p></td>
<td style="text-align: left;"><p>bool</p></td>
<td style="text-align: left;"><p><code>true</code></p></td>
<td style="text-align: left;"><p>Sets the <code>--partial</code> option in the Rsync command.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>rsync_opt_delete</code></p></td>
<td style="text-align: left;"><p>bool</p></td>
<td style="text-align: left;"><p><code>true</code></p></td>
<td style="text-align: left;"><p>Sets the <code>--delete</code> option in the Rsync command.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>rsync_opt_hardlinks</code></p></td>
<td style="text-align: left;"><p>bool</p></td>
<td style="text-align: left;"><p><code>true</code></p></td>
<td style="text-align: left;"><p>Sets the <code>--hard-links</code> option is the Rsync command.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>rsync_opt_info</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p><code>COPY2</code></p>
<p><code>DEL2</code></p>
<p><code>REMOVE2</code></p>
<p><code>SKIP2</code></p>
<p><code>FLIST2</code></p>
<p><code>PROGRESS2</code></p>
<p><code>STATS2</code></p></td>
<td style="text-align: left;"><p>Enables detailed logging in Rsync Pod.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>rsync_opt_extras</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p>Empty</p></td>
<td style="text-align: left;"><p>Reserved for any other arbitrary options.</p></td>
</tr>
</tbody>
</table>

- Setting the options set through the variables above are *global* for all migrations. The configuration will take effect for all future migrations as soon as the Operator successfully reconciles the `MigrationController` CR. Any ongoing migration can use the updated settings depending on which step it currently is in. Therefore, it is recommended that the settings be applied before running a migration. The users can always update the settings as needed.

- Use the `rsync_opt_extras` variable with caution. Any options passed using this variable are appended to the `rsync` command, with addition. Ensure you add white spaces when specifying more than one option. Any error in specifying options can lead to a failed migration. However, you can update `MigrationController` CR as many times as you require for future migrations.

- Customizing the `rsync_opt_info` flag can adversely affect the progress reporting capabilities in MTC. However, removing progress reporting can have a performance advantage. This option should only be used when the performance of Rsync operation is observed to be unacceptable.

> [!NOTE]
> The default configuration used by DVM is tested in various environments. It is acceptable for most production use cases provided the clusters are healthy and performing well. These configuration variables should be used in case the default settings do not work and the Rsync operation fails.

## Resource limit configurations for Rsync pods

The `MigrationController` CR exposes following variables to configure resource usage requirements and limits on Rsync:

| Variable | Type | Default | Description |
|----|----|----|----|
| `source_rsync_pod_cpu_limits` | string | `1` | Source rsync pod’s CPU limit |
| `source_rsync_pod_memory_limits` | string | `1Gi` | Source rsync pod’s memory limit |
| `source_rsync_pod_cpu_requests` | string | `400m` | Source rsync pod’s cpu requests |
| `source_rsync_pod_memory_requests` | string | `1Gi` | Source rsync pod’s memory requests |
| `target_rsync_pod_cpu_limits` | string | `1` | Target rsync pod’s cpu limit |
| `target_rsync_pod_cpu_requests` | string | `400m` | Target rsync pod’s cpu requests |
| `target_rsync_pod_memory_limits` | string | `1Gi` | Target rsync pod’s memory limit |
| `target_rsync_pod_memory_requests` | string | `1Gi` | Target rsync pod’s memory requests |

### Supplemental group configuration for Rsync pods

If Persistent Volume Claims (PVC) are using a shared storage, the access to storage can be configured by adding supplemental groups to Rsync pod definitions in order for the pods to allow access:

| Variable | Type | Default | Description |
|----|----|----|----|
| `src_supplemental_groups` | string | Not Set | Comma separated list of supplemental groups for source Rsync pods |
| `target_supplemental_groups` | string | Not Set | Comma separated list of supplemental groups for target Rsync Pods |

For example, the `MigrationController` CR can be updated to set the previous values:

``` yaml
spec:
  src_supplemental_groups: "1000,2000"
  target_supplemental_groups: "2000,3000"
```

### Rsync retry configuration

With Migration Toolkit for Containers (MTC) 1.4.3 and later, a new ability of retrying a failed Rsync operation is introduced.

By default, the migration controller retries Rsync until all of the data is successfully transferred from the source to the target volume or a specified number of retries is met. The default retry limit is set to `20`.

For larger volumes, a limit of `20` retries may not be sufficient.

You can increase the retry limit by using the following variable in the `MigrationController` CR:

``` yaml
apiVersion: migration.openshift.io/v1alpha1
kind: MigrationController
metadata:
  name: migration-controller
  namespace: openshift-migration
spec:
  [...]
  rsync_backoff_limit: 40
```

In this example, the retry limit is increased to `40`.

### Running Rsync as either root or non-root

OpenShift Container Platform environments have the `PodSecurityAdmission` controller enabled by default. This controller requires cluster administrators to enforce Pod Security Standards by means of namespace labels. All workloads in the cluster are expected to run one of the following Pod Security Standard levels: `privileged`, `baseline` or `restricted`. Every cluster has its own default policy set.

To guarantee successful data transfer in all environments, Migration Toolkit for Containers (MTC) 1.7.5 introduced changes in Rsync pods, including running Rsync pods as non-root user by default. This ensures that data transfer is possible even for workloads that do not necessarily require higher privileges. This change was made because it is best to run workloads with the lowest level of privileges possible.

#### Manually overriding default non-root operation for data transfer

Although running Rsync pods as non-root user works in most cases, data transfer might fail when you run workloads as root user on the source side. MTC provides two ways to manually override default non-root operation for data transfer:

- Configure all migrations to run an Rsync pod as root on the destination cluster for all migrations.

- Run an Rsync pod as root on the destination cluster per migration.

In both cases, you must set the following labels on the source side of any namespaces that are running workloads with higher privileges before migration: `enforce`, `audit`, and `warn.`

#### About pod security admission

OpenShift Container Platform includes [Kubernetes pod security admission](https://kubernetes.io/docs/concepts/security/pod-security-admission). Pods that do not comply with the pod security admission defined globally or at the namespace level are not admitted to the cluster and cannot run.

Globally, the `privileged` profile is enforced, and the `restricted` profile is used for warnings and audits.

You can also configure the pod security admission settings at the namespace level.

> [!IMPORTANT]
> Do not run workloads in or share access to default projects. Default projects are reserved for running core cluster components.
>
> The following default projects are considered highly privileged: `default`, `kube-public`, `kube-system`, `openshift`, `openshift-infra`, `openshift-node`, and other system-created projects that have the `openshift.io/run-level` label set to `0` or `1`. Functionality that relies on admission plugins, such as pod security admission, security context constraints, cluster resource quotas, and image reference resolution, does not work in highly privileged projects.

##### Pod security admission modes

You can configure the following pod security admission modes for a namespace:

| Mode | Label | Description |
|----|----|----|
| `enforce` | `pod-security.kubernetes.io/enforce` | Rejects a pod from admission if it does not comply with the set profile |
| `audit` | `pod-security.kubernetes.io/audit` | Logs audit events if a pod does not comply with the set profile |
| `warn` | `pod-security.kubernetes.io/warn` | Displays warnings if a pod does not comply with the set profile |

Pod security admission modes

##### Pod security admission profiles

You can set each of the pod security admission modes to one of the following profiles:

| Profile | Description |
|----|----|
| `privileged` | Least restrictive policy; allows for known privilege escalation |
| `baseline` | Minimally restrictive policy; prevents known privilege escalations |
| `restricted` | Most restrictive policy; follows current pod hardening best practices |

Pod security admission profiles

##### Privileged namespaces

The following system namespaces are always set to the `privileged` pod security admission profile:

- `default`

- `kube-public`

- `kube-system`

You cannot change the pod security profile for these privileged namespaces.

<div class="formalpara">

<div class="title">

Example privileged namespace configuration

</div>

``` yaml
apiVersion: v1
kind: Namespace
metadata:
  labels:
    openshift.io/cluster-monitoring: "true"
    pod-security.kubernetes.io/enforce: privileged
    pod-security.kubernetes.io/audit: privileged
    pod-security.kubernetes.io/warn: privileged
  name: "<mig_namespace>"
# ...
```

</div>

<div>

<div class="title">

Additional resources

</div>

- [Controlling pod security admission synchronization](../authentication/understanding-and-managing-pod-security-admission.md#security-context-constraints-psa-opting_understanding-and-managing-pod-security-admission).

</div>

#### Configuring the MigrationController CR as root or non-root for all migrations

By default, Rsync runs as non-root.

On the destination cluster, you can configure the `MigrationController` CR to run Rsync as root.

<div>

<div class="title">

Procedure

</div>

- Configure the `MigrationController` CR as follows:

  ``` yaml
  apiVersion: migration.openshift.io/v1alpha1
  kind: MigrationController
  metadata:
    name: migration-controller
    namespace: openshift-migration
  spec:
    [...]
    migration_rsync_privileged: true
  ```

  This configuration will apply to all future migrations.

</div>

#### Configuring the MigMigration CR as root or non-root per migration

On the destination cluster, you can configure the `MigMigration` CR to run Rsync as root or non-root, with the following non-root options:

- As a specific user ID (UID)

- As a specific group ID (GID)

<div>

<div class="title">

Procedure

</div>

1.  To run Rsync as root, configure the `MigMigration` CR according to this example:

    ``` yaml
    apiVersion: migration.openshift.io/v1alpha1
    kind: MigMigration
    metadata:
      name: migration-controller
      namespace: openshift-migration
    spec:
      [...]
      runAsRoot: true
    ```

2.  To run Rsync as a specific User ID (UID) or as a specific Group ID (GID), configure the `MigMigration` CR according to this example:

    ``` yaml
    apiVersion: migration.openshift.io/v1alpha1
    kind: MigMigration
    metadata:
      name: migration-controller
      namespace: openshift-migration
    spec:
      [...]
      runAsUser: 10010001
      runAsGroup: 3
    ```

</div>

## MigCluster Configuration

For every `MigCluster` resource created in Migration Toolkit for Containers (MTC), a `ConfigMap` named `migration-cluster-config` is created in the Migration Operator’s namespace on the cluster which MigCluster resource represents.

The `migration-cluster-config` allows you to configure MigCluster specific values. The Migration Operator manages the `migration-cluster-config`.

You can configure every value in the `ConfigMap` using the variables exposed in the `MigrationController` CR:

| Variable | Type | Required | Description |
|----|----|----|----|
| `migration_stage_image_fqin` | string | No | Image to use for Stage Pods (applicable only to IndirectVolumeMigration) |
| `migration_registry_image_fqin` | string | No | Image to use for Migration Registry |
| `rsync_endpoint_type` | string | No | Type of endpoint for data transfer (`Route`, `ClusterIP`, `NodePort`) |
| `rsync_transfer_image_fqin` | string | No | Image to use for Rsync Pods (applicable only to DirectVolumeMigration) |
| `migration_rsync_privileged` | bool | No | Whether to run Rsync Pods as privileged or not |
| `migration_rsync_super_privileged` | bool | No | Whether to run Rsync Pods as super privileged containers (`spc_t` SELinux context) or not |
| `cluster_subdomain` | string | No | Cluster’s subdomain |
| `migration_registry_readiness_timeout` | int | No | Readiness timeout (in seconds) for Migration Registry Deployment |
| `migration_registry_liveness_timeout` | int | No | Liveness timeout (in seconds) for Migration Registry Deployment |
| `exposed_registry_validation_path` | string | No | Subpath to validate exposed registry in a MigCluster (for example /v2) |

# Direct migration known issues

## Applying the Skip SELinux relabel workaround with `spc_t` automatically on workloads running on OpenShift Container Platform

When attempting to migrate a namespace with Migration Toolkit for Containers (MTC) and a substantial volume associated with it, the `rsync-server` may become frozen without any further information to troubleshoot the issue.

### Diagnosing the need for the Skip SELinux relabel workaround

Search for an error of `Unable to attach or mount volumes for pod…​timed out waiting for the condition` in the kubelet logs from the node where the `rsync-server` for the Direct Volume Migration (DVM) runs.

<div class="formalpara">

<div class="title">

Example kubelet log

</div>

``` yaml
kubenswrapper[3879]: W0326 16:30:36.749224    3879 volume_linux.go:49] Setting volume ownership for /var/lib/kubelet/pods/8905d88e-6531-4d65-9c2a-eff11dc7eb29/volumes/kubernetes.io~csi/pvc-287d1988-3fd9-4517-a0c7-22539acd31e6/mount and fsGroup set. If the volume has a lot of files then setting volume ownership could be slow, see https://github.com/kubernetes/kubernetes/issues/69699

kubenswrapper[3879]: E0326 16:32:02.706363    3879 kubelet.go:1841] "Unable to attach or mount volumes for pod; skipping pod" err="unmounted volumes=[8db9d5b032dab17d4ea9495af12e085a], unattached volumes=[crane2-rsync-server-secret 8db9d5b032dab17d4ea9495af12e085a kube-api-access-dlbd2 crane2-stunnel-server-config crane2-stunnel-server-secret crane2-rsync-server-config]: timed out waiting for the condition" pod="caboodle-preprod/rsync-server"

kubenswrapper[3879]: E0326 16:32:02.706496    3879 pod_workers.go:965] "Error syncing pod, skipping" err="unmounted volumes=[8db9d5b032dab17d4ea9495af12e085a], unattached volumes=[crane2-rsync-server-secret 8db9d5b032dab17d4ea9495af12e085a kube-api-access-dlbd2 crane2-stunnel-server-config crane2-stunnel-server-secret crane2-rsync-server-config]: timed out waiting for the condition" pod="caboodle-preprod/rsync-server" podUID=8905d88e-6531-4d65-9c2a-eff11dc7eb29
```

</div>

### Resolving using the Skip SELinux relabel workaround

To resolve this issue, set the `migration_rsync_super_privileged` parameter to `true` in both the source and destination `MigClusters` using the `MigrationController` custom resource (CR).

<div class="formalpara">

<div class="title">

Example MigrationController CR

</div>

``` yaml
apiVersion: migration.openshift.io/v1alpha1
kind: MigrationController
metadata:
  name: migration-controller
  namespace: openshift-migration
spec:
  migration_rsync_super_privileged: true
  azure_resource_group: ""
  cluster_name: host
  mig_namespace_limit: "10"
  mig_pod_limit: "100"
  mig_pv_limit: "100"
  migration_controller: true
  migration_log_reader: true
  migration_ui: true
  migration_velero: true
  olm_managed: true
  restic_timeout: 1h
  version: 1.8.3
```

</div>

- The value of the `migration_rsync_super_privileged` parameter indicates whether or not to run Rsync Pods as *super privileged* containers (`spc_t selinux context`). Valid settings are `true` or `false`.
