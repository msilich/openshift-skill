<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

You can use the following APIs with OADP:

Velero API
Velero API documentation is maintained by Velero and is not maintained by Red Hat. For more information, see [API types](https://velero.io/docs/main/api-types/) (Velero documentation).

OADP API
The following are the OADP APIs:

- `DataProtectionApplicationSpec`

- `BackupLocation`

- `SnapshotLocation`

- `ApplicationConfig`

- `VeleroConfig`

- `CustomPlugin`

- `ResticConfig`

- `PodConfig`

- `Features`

- `DataMover`

  For more information, see in [OADP Operator](https://pkg.go.dev/github.com/openshift/oadp-operator)(Go documentation).

# DataProtectionApplicationSpec type

The following are `DataProtectionApplicationSpec` OADP APIs:

| Property | Type | Description |
|----|----|----|
| `backupLocations` | \[\] [`BackupLocation`](https://pkg.go.dev/github.com/openshift/oadp-operator/api/v1alpha1#BackupLocation) | Defines the list of configurations to use for `BackupStorageLocations`. |
| `snapshotLocations` | \[\] [`SnapshotLocation`](https://pkg.go.dev/github.com/openshift/oadp-operator/api/v1alpha1#SnapshotLocation) | Defines the list of configurations to use for `VolumeSnapshotLocations`. |
| `unsupportedOverrides` | map \[ [UnsupportedImageKey](https://pkg.go.dev/github.com/openshift/oadp-operator/api/v1alpha1#UnsupportedImageKey) \] [string](https://pkg.go.dev/builtin#string) | Can be used to override the deployed dependent images for development. Options are `veleroImageFqin`, `awsPluginImageFqin`, `hypershiftPluginImageFqin`, `openshiftPluginImageFqin`, `azurePluginImageFqin`, `gcpPluginImageFqin`, `csiPluginImageFqin`, `dataMoverImageFqin`, `resticRestoreImageFqin`, `kubevirtPluginImageFqin`, and `operator-type`. |
| `podAnnotations` | map \[ [string](https://pkg.go.dev/builtin#string) \] [string](https://pkg.go.dev/builtin#string) | Used to add annotations to pods deployed by Operators. |
| `podDnsPolicy` | [`DNSPolicy`](https://pkg.go.dev/k8s.io/api/core/v1#DNSPolicy) | Defines the configuration of the DNS of a pod. |
| `podDnsConfig` | [`PodDNSConfig`](https://pkg.go.dev/k8s.io/api/core/v1#PodDNSConfig) | Defines the DNS parameters of a pod in addition to those generated from `DNSPolicy`. |
| `backupImages` | \*[bool](https://pkg.go.dev/builtin#bool) | Used to specify whether or not you want to deploy a registry for enabling backup and restore of images. |
| `configuration` | \*[`ApplicationConfig`](https://pkg.go.dev/github.com/openshift/oadp-operator/api/v1alpha1#ApplicationConfig) | Used to define the data protection application’s server configuration. |
| `features` | \*[`Features`](https://pkg.go.dev/github.com/openshift/oadp-operator/api/v1alpha1#Features) | Defines the configuration for the DPA to enable the Technology Preview features. |

DataProtectionApplicationSpec

<div>

<div class="title">

Additional resources

</div>

- [Complete schema definitions for the OADP API](https://pkg.go.dev/github.com/openshift/oadp-operator/api/v1alpha1#DataProtectionApplicationSpec)

</div>

# BackupLocation type

The following are `BackupLocation` OADP APIs:

| Property | Type | Description |
|----|----|----|
| `velero` | \*[velero.BackupStorageLocationSpec](https://pkg.go.dev/github.com/vmware-tanzu/velero/pkg/apis/velero/v1#BackupStorageLocationSpec) | Location to store volume snapshots, as described in [Backup Storage Location](https://pkg.go.dev/github.com/vmware-tanzu/velero/pkg/apis/velero/v1#BackupStorageLocation). |
| `bucket` | \*[CloudStorageLocation](https://pkg.go.dev/github.com/openshift/oadp-operator/api/v1alpha1#CloudStorageLocation) | Automates creation of a bucket at some cloud storage providers for use as a backup storage location. |

BackupLocation

> [!IMPORTANT]
> The `bucket` parameter is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.
>
> For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

<div>

<div class="title">

Additional resources

</div>

- [Complete schema definitions for the type `BackupLocation`](https://pkg.go.dev/github.com/openshift/oadp-operator/api/v1alpha1#BackupLocation)

</div>

# SnapshotLocation type

The following are `SnapshotLocation` OADP APIs:

| Property | Type | Description |
|----|----|----|
| `velero` | \*[VolumeSnapshotLocationSpec](https://pkg.go.dev/github.com/vmware-tanzu/velero/pkg/apis/velero/v1#VolumeSnapshotLocationSpec) | Location to store volume snapshots, as described in [Volume Snapshot Location](https://pkg.go.dev/github.com/vmware-tanzu/velero/pkg/apis/velero/v1#VolumeSnapshotLocation). |

SnapshotLocation

<div>

<div class="title">

Additional resources

</div>

- [Complete schema definitions for the type `SnapshotLocation`](https://pkg.go.dev/github.com/openshift/oadp-operator/api/v1alpha1#SnapshotLocation)

</div>

# ApplicationConfig type

The following are `ApplicationConfig` OADP APIs:

| Property | Type | Description |
|----|----|----|
| `velero` | \*[VeleroConfig](https://pkg.go.dev/github.com/openshift/oadp-operator/api/v1alpha1#VeleroConfig) | Defines the configuration for the Velero server. |
| `restic` | \*[ResticConfig](https://pkg.go.dev/github.com/openshift/oadp-operator/api/v1alpha1#ResticConfig) | Defines the configuration for the Restic server. |

ApplicationConfig

<div>

<div class="title">

Additional resources

</div>

- [Complete schema definitions for the type `ApplicationConfig`](https://pkg.go.dev/github.com/openshift/oadp-operator/api/v1alpha1#ApplicationConfig)

</div>

# VeleroConfig type

The following are `VeleroConfig` OADP APIs:

| Property | Type | Description |
|----|----|----|
| `featureFlags` | \[\] [string](https://pkg.go.dev/builtin#string) | Defines the list of features to enable for the Velero instance. |
| `defaultPlugins` | \[\] [string](https://pkg.go.dev/builtin#string) | The following types of default Velero plugins can be installed: `aws`,`azure`, `csi`, `gcp`, `kubevirt`, and `openshift`. |
| `customPlugins` | \[\][CustomPlugin](https://pkg.go.dev/github.com/openshift/oadp-operator/api/v1alpha1#CustomPlugin) | Used for installation of custom Velero plugins. |
| `restoreResourcesVersionPriority` | [string](https://pkg.go.dev/builtin#string) | Represents a config map that is created if defined for use in conjunction with the `EnableAPIGroupVersions` feature flag. Defining this field automatically adds `EnableAPIGroupVersions` to the Velero server feature flag. |
| `noDefaultBackupLocation` | [bool](https://pkg.go.dev/builtin#bool) | To install Velero without a default backup storage location, you must set the `noDefaultBackupLocation` flag in order to confirm installation. |
| `podConfig` | \*[`PodConfig`](https://pkg.go.dev/github.com/openshift/oadp-operator/api/v1alpha1#PodConfig) | Defines the configuration of the `Velero` pod. |
| `logLevel` | [string](https://pkg.go.dev/builtin#string) | Velero server’s log level (use `debug` for the most granular logging, leave unset for Velero default). Valid options are `trace`, `debug`, `info`, `warning`, `error`, `fatal`, and `panic`. |

VeleroConfig

<div>

<div class="title">

Additional resources

</div>

- [Complete schema definitions for the type `VeleroConfig`](https://pkg.go.dev/github.com/openshift/oadp-operator/api/v1alpha1#VeleroConfig)

</div>

# CustomPlugin type

The following are `CustomPlugin` OADP APIs:

| Property | Type | Description |
|----|----|----|
| `name` | [string](https://pkg.go.dev/builtin#string) | Name of custom plugin. |
| `image` | [string](https://pkg.go.dev/builtin#string) | Image of custom plugin. |

CustomPlugin

<div>

<div class="title">

Additional resources

</div>

- [Complete schema definitions for the type `CustomPlugin`](https://pkg.go.dev/github.com/openshift/oadp-operator/api/v1alpha1#CustomPlugin)

</div>

# ResticConfig type

The following are `ResticConfig` OADP APIs:

| Property | Type | Description |
|----|----|----|
| `enable` | \*[bool](https://pkg.go.dev/builtin#bool) | If set to `true`, enables backup and restore using Restic. If set to `false`, snapshots are needed. |
| `supplementalGroups` | \[\][int64](https://pkg.go.dev/builtin#int64) | Defines the Linux groups to be applied to the `Restic` pod. |
| `timeout` | [string](https://pkg.go.dev/builtin#string) | A user-supplied duration string that defines the Restic timeout. Default value is `1hr` (1 hour). A duration string is a possibly signed sequence of decimal numbers, each with optional fraction and a unit suffix, such as `300ms`, `-1.5h`, or `2h45m`. Valid time units are `ns`, `us` (or `µs`), `ms`, `s`, `m`, and `h`. |
| `podConfig` | \*[`PodConfig`](https://pkg.go.dev/github.com/openshift/oadp-operator/api/v1alpha1#PodConfig) | Defines the configuration of the `Restic` pod. |

ResticConfig

<div>

<div class="title">

Additional resources

</div>

- [Complete schema definitions for the type `ResticConfig`](https://pkg.go.dev/github.com/openshift/oadp-operator/api/v1alpha1#ResticConfig)

</div>

# PodConfig type

The following are `PodConfig` OADP APIs:

| Property | Type | Description |
|----|----|----|
| `nodeSelector` | map \[ [string](https://pkg.go.dev/builtin#string) \] [string](https://pkg.go.dev/builtin#string) | Defines the `nodeSelector` to be supplied to a `Velero` `podSpec` or a `Restic` `podSpec`. |
| `tolerations` | \[\][Toleration](https://pkg.go.dev/k8s.io/api/core/v1#Toleration) | Defines the list of tolerations to be applied to a Velero deployment or a Restic `daemonset`. |
| `resourceAllocations` | [ResourceRequirements](https://pkg.go.dev/k8s.io/api/core/v1#ResourceRequirements) | Set specific resource `limits` and `requests` for a `Velero` pod or a `Restic` pod as described in the Setting Velero CPU and memory resource allocations section. |
| `labels` | map \[ [string](https://pkg.go.dev/builtin#string) \] [string](https://pkg.go.dev/builtin#string) | Labels to add to pods. |

PodConfig

<div>

<div class="title">

Additional resources

</div>

- [OADP plugins](oadp-features-plugins.md#oadp-features-plugins)

- [Complete schema definitions for the type `PodConfig`](https://pkg.go.dev/github.com/openshift/oadp-operator/api/v1alpha1#PodConfig)(Go documentation)

</div>

# Features type

The following are `Features` OADP APIs:

| Property | Type | Description |
|----|----|----|
| `dataMover` | \*[`DataMover`](https://pkg.go.dev/github.com/openshift/oadp-operator/api/v1alpha1#DataMover) | Defines the configuration of the Data Mover. |

Features

<div>

<div class="title">

Additional resources

</div>

- [Complete schema definitions for the type `Features`](https://pkg.go.dev/github.com/openshift/oadp-operator/api/v1alpha1#Features)

</div>

# DataMover type

The following are `DataMover` OADP APIs:

| Property | Type | Description |
|----|----|----|
| `enable` | [bool](https://pkg.go.dev/builtin#bool) | If set to `true`, deploys the volume snapshot mover controller and a modified CSI Data Mover plugin. If set to `false`, these are not deployed. |
| `credentialName` | [string](https://pkg.go.dev/builtin#string) | User-supplied Restic `Secret` name for Data Mover. |
| `timeout` | [string](https://pkg.go.dev/builtin#string) | A user-supplied duration string for `VolumeSnapshotBackup` and `VolumeSnapshotRestore` to complete. Default is `10m` (10 minutes). A duration string is a possibly signed sequence of decimal numbers, each with optional fraction and a unit suffix, such as `300ms`, `-1.5h`, or `2h45m`. Valid time units are `ns`, `us` (or `µs`), `ms`, `s`, `m`, and `h`. |

DataMover
