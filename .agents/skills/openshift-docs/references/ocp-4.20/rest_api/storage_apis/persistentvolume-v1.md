<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Description
PersistentVolume (PV) is a storage resource provisioned by an administrator. It is analogous to a node. More info: <https://kubernetes.io/docs/concepts/storage/persistent-volumes>

Type
`object`

# Specification

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ObjectMeta`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) | Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |
| `spec` | `object` | PersistentVolumeSpec is the specification of a persistent volume. |
| `status` | `object` | PersistentVolumeStatus is the current status of a persistent volume. |

## .spec

Description
PersistentVolumeSpec is the specification of a persistent volume.

Type
`object`

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Property</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>accessModes</code></p></td>
<td style="text-align: left;"><p><code>array (string)</code></p></td>
<td style="text-align: left;"><p>accessModes contains all ways the volume can be mounted. More info: <a href="https://kubernetes.io/docs/concepts/storage/persistent-volumes#access-modes">https://kubernetes.io/docs/concepts/storage/persistent-volumes#access-modes</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>awsElasticBlockStore</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>Represents a Persistent Disk resource in AWS.</p>
<p>An AWS EBS disk must exist before mounting to a container. The disk must also be in the same AWS zone as the kubelet. An AWS EBS disk can only be mounted as read/write once. AWS EBS volumes support ownership management and SELinux relabeling.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>azureDisk</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>AzureDisk represents an Azure Data Disk mount on the host and bind mount to the pod.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>azureFile</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>AzureFile represents an Azure File Service mount on the host and bind mount to the pod.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>capacity</code></p></td>
<td style="text-align: left;"><p><a href="../objects/index.xml#io-k8s-apimachinery-pkg-api-resource-Quantity"><code>object (Quantity)</code></a></p></td>
<td style="text-align: left;"><p>capacity is the description of the persistent volume’s resources and capacity. More info: <a href="https://kubernetes.io/docs/concepts/storage/persistent-volumes#capacity">https://kubernetes.io/docs/concepts/storage/persistent-volumes#capacity</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>cephfs</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>Represents a Ceph Filesystem mount that lasts the lifetime of a pod Cephfs volumes do not support ownership management or SELinux relabeling.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>cinder</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>Represents a cinder volume resource in Openstack. A Cinder volume must exist before mounting to a container. The volume must also be in the same region as the kubelet. Cinder volumes support ownership management and SELinux relabeling.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>claimRef</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>ObjectReference contains enough information to let you inspect or modify the referred object.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>csi</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>Represents storage that is managed by an external CSI volume driver</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>fc</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>Represents a Fibre Channel volume. Fibre Channel volumes can only be mounted as read/write once. Fibre Channel volumes support ownership management and SELinux relabeling.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>flexVolume</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>FlexPersistentVolumeSource represents a generic persistent volume resource that is provisioned/attached using an exec based plugin.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>flocker</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>Represents a Flocker volume mounted by the Flocker agent. One and only one of datasetName and datasetUUID should be set. Flocker volumes do not support ownership management or SELinux relabeling.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>gcePersistentDisk</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>Represents a Persistent Disk resource in Google Compute Engine.</p>
<p>A GCE PD must exist before mounting to a container. The disk must also be in the same GCE project and zone as the kubelet. A GCE PD can only be mounted as read/write once or read-only many times. GCE PDs support ownership management and SELinux relabeling.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>glusterfs</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>Represents a Glusterfs mount that lasts the lifetime of a pod. Glusterfs volumes do not support ownership management or SELinux relabeling.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>hostPath</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>Represents a host path mapped into a pod. Host path volumes do not support ownership management or SELinux relabeling.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>iscsi</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>ISCSIPersistentVolumeSource represents an ISCSI disk. ISCSI volumes can only be mounted as read/write once. ISCSI volumes support ownership management and SELinux relabeling.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>local</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>Local represents directly-attached storage with node affinity</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>mountOptions</code></p></td>
<td style="text-align: left;"><p><code>array (string)</code></p></td>
<td style="text-align: left;"><p>mountOptions is the list of mount options, e.g. ["ro", "soft"]. Not validated - mount will simply fail if one is invalid. More info: <a href="https://kubernetes.io/docs/concepts/storage/persistent-volumes/#mount-options">https://kubernetes.io/docs/concepts/storage/persistent-volumes/#mount-options</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>nfs</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>Represents an NFS mount that lasts the lifetime of a pod. NFS volumes do not support ownership management or SELinux relabeling.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>nodeAffinity</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>VolumeNodeAffinity defines constraints that limit what nodes this volume can be accessed from.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>persistentVolumeReclaimPolicy</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>persistentVolumeReclaimPolicy defines what happens to a persistent volume when released from its claim. Valid options are Retain (default for manually created PersistentVolumes), Delete (default for dynamically provisioned PersistentVolumes), and Recycle (deprecated). Recycle must be supported by the volume plugin underlying this PersistentVolume. More info: <a href="https://kubernetes.io/docs/concepts/storage/persistent-volumes#reclaiming">https://kubernetes.io/docs/concepts/storage/persistent-volumes#reclaiming</a></p>
<p>Possible enum values: - <code>"Delete"</code> means the volume will be deleted from Kubernetes on release from its claim. The volume plugin must support Deletion. - <code>"Recycle"</code> means the volume will be recycled back into the pool of unbound persistent volumes on release from its claim. The volume plugin must support Recycling. - <code>"Retain"</code> means the volume will be left in its current phase (Released) for manual reclamation by the administrator. The default policy is Retain.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>photonPersistentDisk</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>Represents a Photon Controller persistent disk resource.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>portworxVolume</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>PortworxVolumeSource represents a Portworx volume resource.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>quobyte</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>Represents a Quobyte mount that lasts the lifetime of a pod. Quobyte volumes do not support ownership management or SELinux relabeling.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>rbd</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>Represents a Rados Block Device mount that lasts the lifetime of a pod. RBD volumes support ownership management and SELinux relabeling.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>scaleIO</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>ScaleIOPersistentVolumeSource represents a persistent ScaleIO volume</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>storageClassName</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>storageClassName is the name of StorageClass to which this persistent volume belongs. Empty value means that this volume does not belong to any StorageClass.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>storageos</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>Represents a StorageOS persistent volume resource.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>volumeAttributesClassName</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Name of VolumeAttributesClass to which this persistent volume belongs. Empty value is not allowed. When this field is not set, it indicates that this volume does not belong to any VolumeAttributesClass. This field is mutable and can be changed by the CSI driver after a volume has been updated successfully to a new class. For an unbound PersistentVolume, the volumeAttributesClassName will be matched with unbound PersistentVolumeClaims during the binding process. This is a beta field and requires enabling VolumeAttributesClass feature (off by default).</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>volumeMode</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>volumeMode defines if a volume is intended to be used with a formatted filesystem or to remain in raw block state. Value of Filesystem is implied when not included in spec.</p>
<p>Possible enum values: - <code>"Block"</code> means the volume will not be formatted with a filesystem and will remain a raw block device. - <code>"Filesystem"</code> means the volume will be or is formatted with a filesystem.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>vsphereVolume</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>Represents a vSphere volume resource.</p></td>
</tr>
</tbody>
</table>

## .spec.awsElasticBlockStore

Description
Represents a Persistent Disk resource in AWS.

An AWS EBS disk must exist before mounting to a container. The disk must also be in the same AWS zone as the kubelet. An AWS EBS disk can only be mounted as read/write once. AWS EBS volumes support ownership management and SELinux relabeling.

Type
`object`

Required
- `volumeID`

| Property | Type | Description |
|----|----|----|
| `fsType` | `string` | fsType is the filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: <https://kubernetes.io/docs/concepts/storage/volumes#awselasticblockstore> |
| `partition` | `integer` | partition is the partition in the volume that you want to mount. If omitted, the default is to mount by volume name. Examples: For volume /dev/sda1, you specify the partition as "1". Similarly, the volume partition for /dev/sda is "0" (or you can leave the property empty). |
| `readOnly` | `boolean` | readOnly value true will force the readOnly setting in VolumeMounts. More info: <https://kubernetes.io/docs/concepts/storage/volumes#awselasticblockstore> |
| `volumeID` | `string` | volumeID is unique ID of the persistent disk resource in AWS (Amazon EBS volume). More info: <https://kubernetes.io/docs/concepts/storage/volumes#awselasticblockstore> |

## .spec.azureDisk

Description
AzureDisk represents an Azure Data Disk mount on the host and bind mount to the pod.

Type
`object`

Required
- `diskName`

- `diskURI`

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Property</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>cachingMode</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>cachingMode is the Host Caching mode: None, Read Only, Read Write.</p>
<p>Possible enum values: - <code>"None"</code> - <code>"ReadOnly"</code> - <code>"ReadWrite"</code></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>diskName</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>diskName is the Name of the data disk in the blob storage</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>diskURI</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>diskURI is the URI of data disk in the blob storage</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>fsType</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>fsType is Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>kind</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>kind expected values are Shared: multiple blob disks per storage account Dedicated: single blob disk per storage account Managed: azure managed data disk (only in managed availability set). defaults to shared</p>
<p>Possible enum values: - <code>"Dedicated"</code> - <code>"Managed"</code> - <code>"Shared"</code></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>readOnly</code></p></td>
<td style="text-align: left;"><p><code>boolean</code></p></td>
<td style="text-align: left;"><p>readOnly Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts.</p></td>
</tr>
</tbody>
</table>

## .spec.azureFile

Description
AzureFile represents an Azure File Service mount on the host and bind mount to the pod.

Type
`object`

Required
- `secretName`

- `shareName`

| Property | Type | Description |
|----|----|----|
| `readOnly` | `boolean` | readOnly defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts. |
| `secretName` | `string` | secretName is the name of secret that contains Azure Storage Account Name and Key |
| `secretNamespace` | `string` | secretNamespace is the namespace of the secret that contains Azure Storage Account Name and Key default is the same as the Pod |
| `shareName` | `string` | shareName is the azure Share Name |

## .spec.cephfs

Description
Represents a Ceph Filesystem mount that lasts the lifetime of a pod Cephfs volumes do not support ownership management or SELinux relabeling.

Type
`object`

Required
- `monitors`

| Property | Type | Description |
|----|----|----|
| `monitors` | `array (string)` | monitors is Required: Monitors is a collection of Ceph monitors More info: <https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it> |
| `path` | `string` | path is Optional: Used as the mounted root, rather than the full Ceph tree, default is / |
| `readOnly` | `boolean` | readOnly is Optional: Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts. More info: <https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it> |
| `secretFile` | `string` | secretFile is Optional: SecretFile is the path to key ring for User, default is /etc/ceph/user.secret More info: <https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it> |
| `secretRef` | `object` | SecretReference represents a Secret Reference. It has enough information to retrieve secret in any namespace |
| `user` | `string` | user is Optional: User is the rados user name, default is admin More info: <https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it> |

## .spec.cephfs.secretRef

Description
SecretReference represents a Secret Reference. It has enough information to retrieve secret in any namespace

Type
`object`

| Property | Type | Description |
|----|----|----|
| `name` | `string` | name is unique within a namespace to reference a secret resource. |
| `namespace` | `string` | namespace defines the space within which the secret name must be unique. |

## .spec.cinder

Description
Represents a cinder volume resource in Openstack. A Cinder volume must exist before mounting to a container. The volume must also be in the same region as the kubelet. Cinder volumes support ownership management and SELinux relabeling.

Type
`object`

Required
- `volumeID`

| Property | Type | Description |
|----|----|----|
| `fsType` | `string` | fsType Filesystem type to mount. Must be a filesystem type supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: <https://examples.k8s.io/mysql-cinder-pd/README.md> |
| `readOnly` | `boolean` | readOnly is Optional: Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts. More info: <https://examples.k8s.io/mysql-cinder-pd/README.md> |
| `secretRef` | `object` | SecretReference represents a Secret Reference. It has enough information to retrieve secret in any namespace |
| `volumeID` | `string` | volumeID used to identify the volume in cinder. More info: <https://examples.k8s.io/mysql-cinder-pd/README.md> |

## .spec.cinder.secretRef

Description
SecretReference represents a Secret Reference. It has enough information to retrieve secret in any namespace

Type
`object`

| Property | Type | Description |
|----|----|----|
| `name` | `string` | name is unique within a namespace to reference a secret resource. |
| `namespace` | `string` | namespace defines the space within which the secret name must be unique. |

## .spec.claimRef

Description
ObjectReference contains enough information to let you inspect or modify the referred object.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | API version of the referent. |
| `fieldPath` | `string` | If referring to a piece of an object instead of an entire object, this string should contain a valid JSON/Go field access statement, such as desiredState.manifest.containers\[2\]. For example, if the object reference is to a container within a pod, this would take on a value like: "spec.containers{name}" (where "name" refers to the name of the container that triggered the event) or if no container name is specified "spec.containers\[2\]" (container with index 2 in this pod). This syntax is chosen only to have some well-defined way of referencing a part of an object. |
| `kind` | `string` | Kind of the referent. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `name` | `string` | Name of the referent. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names> |
| `namespace` | `string` | Namespace of the referent. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/> |
| `resourceVersion` | `string` | Specific resourceVersion to which this reference is made, if any. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#concurrency-control-and-consistency> |
| `uid` | `string` | UID of the referent. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#uids> |

## .spec.csi

Description
Represents storage that is managed by an external CSI volume driver

Type
`object`

Required
- `driver`

- `volumeHandle`

| Property | Type | Description |
|----|----|----|
| `controllerExpandSecretRef` | `object` | SecretReference represents a Secret Reference. It has enough information to retrieve secret in any namespace |
| `controllerPublishSecretRef` | `object` | SecretReference represents a Secret Reference. It has enough information to retrieve secret in any namespace |
| `driver` | `string` | driver is the name of the driver to use for this volume. Required. |
| `fsType` | `string` | fsType to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". |
| `nodeExpandSecretRef` | `object` | SecretReference represents a Secret Reference. It has enough information to retrieve secret in any namespace |
| `nodePublishSecretRef` | `object` | SecretReference represents a Secret Reference. It has enough information to retrieve secret in any namespace |
| `nodeStageSecretRef` | `object` | SecretReference represents a Secret Reference. It has enough information to retrieve secret in any namespace |
| `readOnly` | `boolean` | readOnly value to pass to ControllerPublishVolumeRequest. Defaults to false (read/write). |
| `volumeAttributes` | `object (string)` | volumeAttributes of the volume to publish. |
| `volumeHandle` | `string` | volumeHandle is the unique volume name returned by the CSI volume plugin’s CreateVolume to refer to the volume on all subsequent calls. Required. |

## .spec.csi.controllerExpandSecretRef

Description
SecretReference represents a Secret Reference. It has enough information to retrieve secret in any namespace

Type
`object`

| Property | Type | Description |
|----|----|----|
| `name` | `string` | name is unique within a namespace to reference a secret resource. |
| `namespace` | `string` | namespace defines the space within which the secret name must be unique. |

## .spec.csi.controllerPublishSecretRef

Description
SecretReference represents a Secret Reference. It has enough information to retrieve secret in any namespace

Type
`object`

| Property | Type | Description |
|----|----|----|
| `name` | `string` | name is unique within a namespace to reference a secret resource. |
| `namespace` | `string` | namespace defines the space within which the secret name must be unique. |

## .spec.csi.nodeExpandSecretRef

Description
SecretReference represents a Secret Reference. It has enough information to retrieve secret in any namespace

Type
`object`

| Property | Type | Description |
|----|----|----|
| `name` | `string` | name is unique within a namespace to reference a secret resource. |
| `namespace` | `string` | namespace defines the space within which the secret name must be unique. |

## .spec.csi.nodePublishSecretRef

Description
SecretReference represents a Secret Reference. It has enough information to retrieve secret in any namespace

Type
`object`

| Property | Type | Description |
|----|----|----|
| `name` | `string` | name is unique within a namespace to reference a secret resource. |
| `namespace` | `string` | namespace defines the space within which the secret name must be unique. |

## .spec.csi.nodeStageSecretRef

Description
SecretReference represents a Secret Reference. It has enough information to retrieve secret in any namespace

Type
`object`

| Property | Type | Description |
|----|----|----|
| `name` | `string` | name is unique within a namespace to reference a secret resource. |
| `namespace` | `string` | namespace defines the space within which the secret name must be unique. |

## .spec.fc

Description
Represents a Fibre Channel volume. Fibre Channel volumes can only be mounted as read/write once. Fibre Channel volumes support ownership management and SELinux relabeling.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `fsType` | `string` | fsType is the filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. |
| `lun` | `integer` | lun is Optional: FC target lun number |
| `readOnly` | `boolean` | readOnly is Optional: Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts. |
| `targetWWNs` | `array (string)` | targetWWNs is Optional: FC target worldwide names (WWNs) |
| `wwids` | `array (string)` | wwids Optional: FC volume world wide identifiers (wwids) Either wwids or combination of targetWWNs and lun must be set, but not both simultaneously. |

## .spec.flexVolume

Description
FlexPersistentVolumeSource represents a generic persistent volume resource that is provisioned/attached using an exec based plugin.

Type
`object`

Required
- `driver`

| Property | Type | Description |
|----|----|----|
| `driver` | `string` | driver is the name of the driver to use for this volume. |
| `fsType` | `string` | fsType is the Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". The default filesystem depends on FlexVolume script. |
| `options` | `object (string)` | options is Optional: this field holds extra command options if any. |
| `readOnly` | `boolean` | readOnly is Optional: defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts. |
| `secretRef` | `object` | SecretReference represents a Secret Reference. It has enough information to retrieve secret in any namespace |

## .spec.flexVolume.secretRef

Description
SecretReference represents a Secret Reference. It has enough information to retrieve secret in any namespace

Type
`object`

| Property | Type | Description |
|----|----|----|
| `name` | `string` | name is unique within a namespace to reference a secret resource. |
| `namespace` | `string` | namespace defines the space within which the secret name must be unique. |

## .spec.flocker

Description
Represents a Flocker volume mounted by the Flocker agent. One and only one of datasetName and datasetUUID should be set. Flocker volumes do not support ownership management or SELinux relabeling.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `datasetName` | `string` | datasetName is Name of the dataset stored as metadata → name on the dataset for Flocker should be considered as deprecated |
| `datasetUUID` | `string` | datasetUUID is the UUID of the dataset. This is unique identifier of a Flocker dataset |

## .spec.gcePersistentDisk

Description
Represents a Persistent Disk resource in Google Compute Engine.

A GCE PD must exist before mounting to a container. The disk must also be in the same GCE project and zone as the kubelet. A GCE PD can only be mounted as read/write once or read-only many times. GCE PDs support ownership management and SELinux relabeling.

Type
`object`

Required
- `pdName`

| Property | Type | Description |
|----|----|----|
| `fsType` | `string` | fsType is filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: <https://kubernetes.io/docs/concepts/storage/volumes#gcepersistentdisk> |
| `partition` | `integer` | partition is the partition in the volume that you want to mount. If omitted, the default is to mount by volume name. Examples: For volume /dev/sda1, you specify the partition as "1". Similarly, the volume partition for /dev/sda is "0" (or you can leave the property empty). More info: <https://kubernetes.io/docs/concepts/storage/volumes#gcepersistentdisk> |
| `pdName` | `string` | pdName is unique name of the PD resource in GCE. Used to identify the disk in GCE. More info: <https://kubernetes.io/docs/concepts/storage/volumes#gcepersistentdisk> |
| `readOnly` | `boolean` | readOnly here will force the ReadOnly setting in VolumeMounts. Defaults to false. More info: <https://kubernetes.io/docs/concepts/storage/volumes#gcepersistentdisk> |

## .spec.glusterfs

Description
Represents a Glusterfs mount that lasts the lifetime of a pod. Glusterfs volumes do not support ownership management or SELinux relabeling.

Type
`object`

Required
- `endpoints`

- `path`

| Property | Type | Description |
|----|----|----|
| `endpoints` | `string` | endpoints is the endpoint name that details Glusterfs topology. More info: <https://examples.k8s.io/volumes/glusterfs/README.md#create-a-pod> |
| `endpointsNamespace` | `string` | endpointsNamespace is the namespace that contains Glusterfs endpoint. If this field is empty, the EndpointNamespace defaults to the same namespace as the bound PVC. More info: <https://examples.k8s.io/volumes/glusterfs/README.md#create-a-pod> |
| `path` | `string` | path is the Glusterfs volume path. More info: <https://examples.k8s.io/volumes/glusterfs/README.md#create-a-pod> |
| `readOnly` | `boolean` | readOnly here will force the Glusterfs volume to be mounted with read-only permissions. Defaults to false. More info: <https://examples.k8s.io/volumes/glusterfs/README.md#create-a-pod> |

## .spec.hostPath

Description
Represents a host path mapped into a pod. Host path volumes do not support ownership management or SELinux relabeling.

Type
`object`

Required
- `path`

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Property</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>path</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>path of the directory on the host. If the path is a symlink, it will follow the link to the real path. More info: <a href="https://kubernetes.io/docs/concepts/storage/volumes#hostpath">https://kubernetes.io/docs/concepts/storage/volumes#hostpath</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>type</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>type for HostPath Volume Defaults to "" More info: <a href="https://kubernetes.io/docs/concepts/storage/volumes#hostpath">https://kubernetes.io/docs/concepts/storage/volumes#hostpath</a></p>
<p>Possible enum values: - <code>""</code> For backwards compatible, leave it empty if unset - <code>"BlockDevice"</code> A block device must exist at the given path - <code>"CharDevice"</code> A character device must exist at the given path - <code>"Directory"</code> A directory must exist at the given path - <code>"DirectoryOrCreate"</code> If nothing exists at the given path, an empty directory will be created there as needed with file mode 0755, having the same group and ownership with Kubelet. - <code>"File"</code> A file must exist at the given path - <code>"FileOrCreate"</code> If nothing exists at the given path, an empty file will be created there as needed with file mode 0644, having the same group and ownership with Kubelet. - <code>"Socket"</code> A UNIX socket must exist at the given path</p></td>
</tr>
</tbody>
</table>

## .spec.iscsi

Description
ISCSIPersistentVolumeSource represents an ISCSI disk. ISCSI volumes can only be mounted as read/write once. ISCSI volumes support ownership management and SELinux relabeling.

Type
`object`

Required
- `targetPortal`

- `iqn`

- `lun`

| Property | Type | Description |
|----|----|----|
| `chapAuthDiscovery` | `boolean` | chapAuthDiscovery defines whether support iSCSI Discovery CHAP authentication |
| `chapAuthSession` | `boolean` | chapAuthSession defines whether support iSCSI Session CHAP authentication |
| `fsType` | `string` | fsType is the filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: <https://kubernetes.io/docs/concepts/storage/volumes#iscsi> |
| `initiatorName` | `string` | initiatorName is the custom iSCSI Initiator Name. If initiatorName is specified with iscsiInterface simultaneously, new iSCSI interface \<target portal\>:\<volume name\> will be created for the connection. |
| `iqn` | `string` | iqn is Target iSCSI Qualified Name. |
| `iscsiInterface` | `string` | iscsiInterface is the interface Name that uses an iSCSI transport. Defaults to 'default' (tcp). |
| `lun` | `integer` | lun is iSCSI Target Lun number. |
| `portals` | `array (string)` | portals is the iSCSI Target Portal List. The Portal is either an IP or ip_addr:port if the port is other than default (typically TCP ports 860 and 3260). |
| `readOnly` | `boolean` | readOnly here will force the ReadOnly setting in VolumeMounts. Defaults to false. |
| `secretRef` | `object` | SecretReference represents a Secret Reference. It has enough information to retrieve secret in any namespace |
| `targetPortal` | `string` | targetPortal is iSCSI Target Portal. The Portal is either an IP or ip_addr:port if the port is other than default (typically TCP ports 860 and 3260). |

## .spec.iscsi.secretRef

Description
SecretReference represents a Secret Reference. It has enough information to retrieve secret in any namespace

Type
`object`

| Property | Type | Description |
|----|----|----|
| `name` | `string` | name is unique within a namespace to reference a secret resource. |
| `namespace` | `string` | namespace defines the space within which the secret name must be unique. |

## .spec.local

Description
Local represents directly-attached storage with node affinity

Type
`object`

Required
- `path`

| Property | Type | Description |
|----|----|----|
| `fsType` | `string` | fsType is the filesystem type to mount. It applies only when the Path is a block device. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". The default value is to auto-select a filesystem if unspecified. |
| `path` | `string` | path of the full path to the volume on the node. It can be either a directory or block device (disk, partition, …​). |

## .spec.nfs

Description
Represents an NFS mount that lasts the lifetime of a pod. NFS volumes do not support ownership management or SELinux relabeling.

Type
`object`

Required
- `server`

- `path`

| Property | Type | Description |
|----|----|----|
| `path` | `string` | path that is exported by the NFS server. More info: <https://kubernetes.io/docs/concepts/storage/volumes#nfs> |
| `readOnly` | `boolean` | readOnly here will force the NFS export to be mounted with read-only permissions. Defaults to false. More info: <https://kubernetes.io/docs/concepts/storage/volumes#nfs> |
| `server` | `string` | server is the hostname or IP address of the NFS server. More info: <https://kubernetes.io/docs/concepts/storage/volumes#nfs> |

## .spec.nodeAffinity

Description
VolumeNodeAffinity defines constraints that limit what nodes this volume can be accessed from.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `required` | `object` | A node selector represents the union of the results of one or more label queries over a set of nodes; that is, it represents the OR of the selectors represented by the node selector terms. |

## .spec.nodeAffinity.required

Description
A node selector represents the union of the results of one or more label queries over a set of nodes; that is, it represents the OR of the selectors represented by the node selector terms.

Type
`object`

Required
- `nodeSelectorTerms`

| Property | Type | Description |
|----|----|----|
| `nodeSelectorTerms` | `array` | Required. A list of node selector terms. The terms are ORed. |
| `nodeSelectorTerms[]` | `object` | A null or empty node selector term matches no objects. The requirements of them are ANDed. The TopologySelectorTerm type implements a subset of the NodeSelectorTerm. |

## .spec.nodeAffinity.required.nodeSelectorTerms

Description
Required. A list of node selector terms. The terms are ORed.

Type
`array`

## .spec.nodeAffinity.required.nodeSelectorTerms\[\]

Description
A null or empty node selector term matches no objects. The requirements of them are ANDed. The TopologySelectorTerm type implements a subset of the NodeSelectorTerm.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `matchExpressions` | `array` | A list of node selector requirements by node’s labels. |
| `matchExpressions[]` | `object` | A node selector requirement is a selector that contains values, a key, and an operator that relates the key and values. |
| `matchFields` | `array` | A list of node selector requirements by node’s fields. |
| `matchFields[]` | `object` | A node selector requirement is a selector that contains values, a key, and an operator that relates the key and values. |

## .spec.nodeAffinity.required.nodeSelectorTerms\[\].matchExpressions

Description
A list of node selector requirements by node’s labels.

Type
`array`

## .spec.nodeAffinity.required.nodeSelectorTerms\[\].matchExpressions\[\]

Description
A node selector requirement is a selector that contains values, a key, and an operator that relates the key and values.

Type
`object`

Required
- `key`

- `operator`

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Property</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>key</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>The label key that the selector applies to.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>operator</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Represents a key’s relationship to a set of values. Valid operators are In, NotIn, Exists, DoesNotExist. Gt, and Lt.</p>
<p>Possible enum values: - <code>"DoesNotExist"</code> - <code>"Exists"</code> - <code>"Gt"</code> - <code>"In"</code> - <code>"Lt"</code> - <code>"NotIn"</code></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>values</code></p></td>
<td style="text-align: left;"><p><code>array (string)</code></p></td>
<td style="text-align: left;"><p>An array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. If the operator is Gt or Lt, the values array must have a single element, which will be interpreted as an integer. This array is replaced during a strategic merge patch.</p></td>
</tr>
</tbody>
</table>

## .spec.nodeAffinity.required.nodeSelectorTerms\[\].matchFields

Description
A list of node selector requirements by node’s fields.

Type
`array`

## .spec.nodeAffinity.required.nodeSelectorTerms\[\].matchFields\[\]

Description
A node selector requirement is a selector that contains values, a key, and an operator that relates the key and values.

Type
`object`

Required
- `key`

- `operator`

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Property</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>key</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>The label key that the selector applies to.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>operator</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Represents a key’s relationship to a set of values. Valid operators are In, NotIn, Exists, DoesNotExist. Gt, and Lt.</p>
<p>Possible enum values: - <code>"DoesNotExist"</code> - <code>"Exists"</code> - <code>"Gt"</code> - <code>"In"</code> - <code>"Lt"</code> - <code>"NotIn"</code></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>values</code></p></td>
<td style="text-align: left;"><p><code>array (string)</code></p></td>
<td style="text-align: left;"><p>An array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. If the operator is Gt or Lt, the values array must have a single element, which will be interpreted as an integer. This array is replaced during a strategic merge patch.</p></td>
</tr>
</tbody>
</table>

## .spec.photonPersistentDisk

Description
Represents a Photon Controller persistent disk resource.

Type
`object`

Required
- `pdID`

| Property | Type | Description |
|----|----|----|
| `fsType` | `string` | fsType is the filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. |
| `pdID` | `string` | pdID is the ID that identifies Photon Controller persistent disk |

## .spec.portworxVolume

Description
PortworxVolumeSource represents a Portworx volume resource.

Type
`object`

Required
- `volumeID`

| Property | Type | Description |
|----|----|----|
| `fsType` | `string` | fSType represents the filesystem type to mount Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs". Implicitly inferred to be "ext4" if unspecified. |
| `readOnly` | `boolean` | readOnly defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts. |
| `volumeID` | `string` | volumeID uniquely identifies a Portworx volume |

## .spec.quobyte

Description
Represents a Quobyte mount that lasts the lifetime of a pod. Quobyte volumes do not support ownership management or SELinux relabeling.

Type
`object`

Required
- `registry`

- `volume`

| Property | Type | Description |
|----|----|----|
| `group` | `string` | group to map volume access to Default is no group |
| `readOnly` | `boolean` | readOnly here will force the Quobyte volume to be mounted with read-only permissions. Defaults to false. |
| `registry` | `string` | registry represents a single or multiple Quobyte Registry services specified as a string as host:port pair (multiple entries are separated with commas) which acts as the central registry for volumes |
| `tenant` | `string` | tenant owning the given Quobyte volume in the Backend Used with dynamically provisioned Quobyte volumes, value is set by the plugin |
| `user` | `string` | user to map volume access to Defaults to serivceaccount user |
| `volume` | `string` | volume is a string that references an already created Quobyte volume by name. |

## .spec.rbd

Description
Represents a Rados Block Device mount that lasts the lifetime of a pod. RBD volumes support ownership management and SELinux relabeling.

Type
`object`

Required
- `monitors`

- `image`

| Property | Type | Description |
|----|----|----|
| `fsType` | `string` | fsType is the filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: <https://kubernetes.io/docs/concepts/storage/volumes#rbd> |
| `image` | `string` | image is the rados image name. More info: <https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it> |
| `keyring` | `string` | keyring is the path to key ring for RBDUser. Default is /etc/ceph/keyring. More info: <https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it> |
| `monitors` | `array (string)` | monitors is a collection of Ceph monitors. More info: <https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it> |
| `pool` | `string` | pool is the rados pool name. Default is rbd. More info: <https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it> |
| `readOnly` | `boolean` | readOnly here will force the ReadOnly setting in VolumeMounts. Defaults to false. More info: <https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it> |
| `secretRef` | `object` | SecretReference represents a Secret Reference. It has enough information to retrieve secret in any namespace |
| `user` | `string` | user is the rados user name. Default is admin. More info: <https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it> |

## .spec.rbd.secretRef

Description
SecretReference represents a Secret Reference. It has enough information to retrieve secret in any namespace

Type
`object`

| Property | Type | Description |
|----|----|----|
| `name` | `string` | name is unique within a namespace to reference a secret resource. |
| `namespace` | `string` | namespace defines the space within which the secret name must be unique. |

## .spec.scaleIO

Description
ScaleIOPersistentVolumeSource represents a persistent ScaleIO volume

Type
`object`

Required
- `gateway`

- `system`

- `secretRef`

| Property | Type | Description |
|----|----|----|
| `fsType` | `string` | fsType is the filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Default is "xfs" |
| `gateway` | `string` | gateway is the host address of the ScaleIO API Gateway. |
| `protectionDomain` | `string` | protectionDomain is the name of the ScaleIO Protection Domain for the configured storage. |
| `readOnly` | `boolean` | readOnly defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts. |
| `secretRef` | `object` | SecretReference represents a Secret Reference. It has enough information to retrieve secret in any namespace |
| `sslEnabled` | `boolean` | sslEnabled is the flag to enable/disable SSL communication with Gateway, default false |
| `storageMode` | `string` | storageMode indicates whether the storage for a volume should be ThickProvisioned or ThinProvisioned. Default is ThinProvisioned. |
| `storagePool` | `string` | storagePool is the ScaleIO Storage Pool associated with the protection domain. |
| `system` | `string` | system is the name of the storage system as configured in ScaleIO. |
| `volumeName` | `string` | volumeName is the name of a volume already created in the ScaleIO system that is associated with this volume source. |

## .spec.scaleIO.secretRef

Description
SecretReference represents a Secret Reference. It has enough information to retrieve secret in any namespace

Type
`object`

| Property | Type | Description |
|----|----|----|
| `name` | `string` | name is unique within a namespace to reference a secret resource. |
| `namespace` | `string` | namespace defines the space within which the secret name must be unique. |

## .spec.storageos

Description
Represents a StorageOS persistent volume resource.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `fsType` | `string` | fsType is the filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. |
| `readOnly` | `boolean` | readOnly defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts. |
| `secretRef` | `object` | ObjectReference contains enough information to let you inspect or modify the referred object. |
| `volumeName` | `string` | volumeName is the human-readable name of the StorageOS volume. Volume names are only unique within a namespace. |
| `volumeNamespace` | `string` | volumeNamespace specifies the scope of the volume within StorageOS. If no namespace is specified then the Pod’s namespace will be used. This allows the Kubernetes name scoping to be mirrored within StorageOS for tighter integration. Set VolumeName to any name to override the default behaviour. Set to "default" if you are not using namespaces within StorageOS. Namespaces that do not pre-exist within StorageOS will be created. |

## .spec.storageos.secretRef

Description
ObjectReference contains enough information to let you inspect or modify the referred object.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | API version of the referent. |
| `fieldPath` | `string` | If referring to a piece of an object instead of an entire object, this string should contain a valid JSON/Go field access statement, such as desiredState.manifest.containers\[2\]. For example, if the object reference is to a container within a pod, this would take on a value like: "spec.containers{name}" (where "name" refers to the name of the container that triggered the event) or if no container name is specified "spec.containers\[2\]" (container with index 2 in this pod). This syntax is chosen only to have some well-defined way of referencing a part of an object. |
| `kind` | `string` | Kind of the referent. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `name` | `string` | Name of the referent. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names> |
| `namespace` | `string` | Namespace of the referent. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/> |
| `resourceVersion` | `string` | Specific resourceVersion to which this reference is made, if any. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#concurrency-control-and-consistency> |
| `uid` | `string` | UID of the referent. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#uids> |

## .spec.vsphereVolume

Description
Represents a vSphere volume resource.

Type
`object`

Required
- `volumePath`

| Property | Type | Description |
|----|----|----|
| `fsType` | `string` | fsType is filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. |
| `storagePolicyID` | `string` | storagePolicyID is the storage Policy Based Management (SPBM) profile ID associated with the StoragePolicyName. |
| `storagePolicyName` | `string` | storagePolicyName is the storage Policy Based Management (SPBM) profile name. |
| `volumePath` | `string` | volumePath is the path that identifies vSphere volume vmdk |

## .status

Description
PersistentVolumeStatus is the current status of a persistent volume.

Type
`object`

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Property</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>lastPhaseTransitionTime</code></p></td>
<td style="text-align: left;"><p><a href="../objects/index.xml#io-k8s-apimachinery-pkg-apis-meta-v1-Time"><code>Time</code></a></p></td>
<td style="text-align: left;"><p>lastPhaseTransitionTime is the time the phase transitioned from one to another and automatically resets to current time everytime a volume phase transitions.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>message</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>message is a human-readable message indicating details about why the volume is in this state.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>phase</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>phase indicates if a volume is available, bound to a claim, or released by a claim. More info: <a href="https://kubernetes.io/docs/concepts/storage/persistent-volumes#phase">https://kubernetes.io/docs/concepts/storage/persistent-volumes#phase</a></p>
<p>Possible enum values: - <code>"Available"</code> used for PersistentVolumes that are not yet bound Available volumes are held by the binder and matched to PersistentVolumeClaims - <code>"Bound"</code> used for PersistentVolumes that are bound - <code>"Failed"</code> used for PersistentVolumes that failed to be correctly recycled or deleted after being released from a claim - <code>"Pending"</code> used for PersistentVolumes that are not available - <code>"Released"</code> used for PersistentVolumes where the bound PersistentVolumeClaim was deleted released volumes must be recycled before becoming available again this phase is used by the persistent volume claim binder to signal to another process to reclaim the resource</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>reason</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>reason is a brief CamelCase string that describes any failure and is meant for machine parsing and tidy display in the CLI.</p></td>
</tr>
</tbody>
</table>

# API endpoints

The following API endpoints are available:

- `/api/v1/persistentvolumes`

  - `DELETE`: delete collection of PersistentVolume

  - `GET`: list or watch objects of kind PersistentVolume

  - `POST`: create a PersistentVolume

- `/api/v1/watch/persistentvolumes`

  - `GET`: watch individual changes to a list of PersistentVolume. deprecated: use the 'watch' parameter with a list operation instead.

- `/api/v1/persistentvolumes/{name}`

  - `DELETE`: delete a PersistentVolume

  - `GET`: read the specified PersistentVolume

  - `PATCH`: partially update the specified PersistentVolume

  - `PUT`: replace the specified PersistentVolume

- `/api/v1/watch/persistentvolumes/{name}`

  - `GET`: watch changes to an object of kind PersistentVolume. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.

- `/api/v1/persistentvolumes/{name}/status`

  - `GET`: read status of the specified PersistentVolume

  - `PATCH`: partially update status of the specified PersistentVolume

  - `PUT`: replace status of the specified PersistentVolume

## /api/v1/persistentvolumes

HTTP method
`DELETE`

Description
delete collection of PersistentVolume

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |

Query parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Status`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`GET`

Description
list or watch objects of kind PersistentVolume

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`PersistentVolumeList`](../objects/index.md#io-k8s-api-core-v1-PersistentVolumeList) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`POST`

Description
create a PersistentVolume

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`PersistentVolume`](persistentvolume-v1.md#persistentvolume-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`PersistentVolume`](persistentvolume-v1.md#persistentvolume-v1) schema |
| 201 - Created | [`PersistentVolume`](persistentvolume-v1.md#persistentvolume-v1) schema |
| 202 - Accepted | [`PersistentVolume`](persistentvolume-v1.md#persistentvolume-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /api/v1/watch/persistentvolumes

HTTP method
`GET`

Description
watch individual changes to a list of PersistentVolume. deprecated: use the 'watch' parameter with a list operation instead.

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`WatchEvent`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /api/v1/persistentvolumes/{name}

| Parameter | Type     | Description                  |
|-----------|----------|------------------------------|
| `name`    | `string` | name of the PersistentVolume |

Global path parameters

HTTP method
`DELETE`

Description
delete a PersistentVolume

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |

Query parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`PersistentVolume`](persistentvolume-v1.md#persistentvolume-v1) schema |
| 202 - Accepted | [`PersistentVolume`](persistentvolume-v1.md#persistentvolume-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`GET`

Description
read the specified PersistentVolume

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`PersistentVolume`](persistentvolume-v1.md#persistentvolume-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PATCH`

Description
partially update the specified PersistentVolume

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`PersistentVolume`](persistentvolume-v1.md#persistentvolume-v1) schema |
| 201 - Created | [`PersistentVolume`](persistentvolume-v1.md#persistentvolume-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PUT`

Description
replace the specified PersistentVolume

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`PersistentVolume`](persistentvolume-v1.md#persistentvolume-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`PersistentVolume`](persistentvolume-v1.md#persistentvolume-v1) schema |
| 201 - Created | [`PersistentVolume`](persistentvolume-v1.md#persistentvolume-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /api/v1/watch/persistentvolumes/{name}

| Parameter | Type     | Description                  |
|-----------|----------|------------------------------|
| `name`    | `string` | name of the PersistentVolume |

Global path parameters

HTTP method
`GET`

Description
watch changes to an object of kind PersistentVolume. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`WatchEvent`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /api/v1/persistentvolumes/{name}/status

| Parameter | Type     | Description                  |
|-----------|----------|------------------------------|
| `name`    | `string` | name of the PersistentVolume |

Global path parameters

HTTP method
`GET`

Description
read status of the specified PersistentVolume

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`PersistentVolume`](persistentvolume-v1.md#persistentvolume-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PATCH`

Description
partially update status of the specified PersistentVolume

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`PersistentVolume`](persistentvolume-v1.md#persistentvolume-v1) schema |
| 201 - Created | [`PersistentVolume`](persistentvolume-v1.md#persistentvolume-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PUT`

Description
replace status of the specified PersistentVolume

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`PersistentVolume`](persistentvolume-v1.md#persistentvolume-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`PersistentVolume`](persistentvolume-v1.md#persistentvolume-v1) schema |
| 201 - Created | [`PersistentVolume`](persistentvolume-v1.md#persistentvolume-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses
