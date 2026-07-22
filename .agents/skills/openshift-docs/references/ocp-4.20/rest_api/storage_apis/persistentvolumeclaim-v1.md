<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Description
PersistentVolumeClaim is a user’s request for and claim to a persistent volume

Type
`object`

# Specification

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ObjectMeta`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) | Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |
| `spec` | `object` | PersistentVolumeClaimSpec describes the common attributes of storage devices and allows a Source for provider-specific attributes |
| `status` | `object` | PersistentVolumeClaimStatus is the current status of a persistent volume claim. |

## .spec

Description
PersistentVolumeClaimSpec describes the common attributes of storage devices and allows a Source for provider-specific attributes

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
<td style="text-align: left;"><p>accessModes contains the desired access modes the volume should have. More info: <a href="https://kubernetes.io/docs/concepts/storage/persistent-volumes#access-modes-1">https://kubernetes.io/docs/concepts/storage/persistent-volumes#access-modes-1</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>dataSource</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>TypedLocalObjectReference contains enough information to let you locate the typed referenced object inside the same namespace.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>dataSourceRef</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>TypedObjectReference contains enough information to let you locate the typed referenced object</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>resources</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>VolumeResourceRequirements describes the storage resource requirements for a volume.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>selector</code></p></td>
<td style="text-align: left;"><p><a href="../objects/index.xml#io-k8s-apimachinery-pkg-apis-meta-v1-LabelSelector"><code>LabelSelector</code></a></p></td>
<td style="text-align: left;"><p>selector is a label query over volumes to consider for binding.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>storageClassName</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>storageClassName is the name of the StorageClass required by the claim. More info: <a href="https://kubernetes.io/docs/concepts/storage/persistent-volumes#class-1">https://kubernetes.io/docs/concepts/storage/persistent-volumes#class-1</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>volumeAttributesClassName</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>volumeAttributesClassName may be used to set the VolumeAttributesClass used by this claim. If specified, the CSI driver will create or update the volume with the attributes defined in the corresponding VolumeAttributesClass. This has a different purpose than storageClassName, it can be changed after the claim is created. An empty string value means that no VolumeAttributesClass will be applied to the claim but it’s not allowed to reset this field to empty string once it is set. If unspecified and the PersistentVolumeClaim is unbound, the default VolumeAttributesClass will be set by the persistentvolume controller if it exists. If the resource referred to by volumeAttributesClass does not exist, this PersistentVolumeClaim will be set to a Pending state, as reflected by the modifyVolumeStatus field, until such as a resource exists. More info: <a href="https://kubernetes.io/docs/concepts/storage/volume-attributes-classes/">https://kubernetes.io/docs/concepts/storage/volume-attributes-classes/</a> (Beta) Using this field requires the VolumeAttributesClass feature gate to be enabled (off by default).</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>volumeMode</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>volumeMode defines what type of volume is required by the claim. Value of Filesystem is implied when not included in claim spec.</p>
<p>Possible enum values: - <code>"Block"</code> means the volume will not be formatted with a filesystem and will remain a raw block device. - <code>"Filesystem"</code> means the volume will be or is formatted with a filesystem.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>volumeName</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>volumeName is the binding reference to the PersistentVolume backing this claim.</p></td>
</tr>
</tbody>
</table>

## .spec.dataSource

Description
TypedLocalObjectReference contains enough information to let you locate the typed referenced object inside the same namespace.

Type
`object`

Required
- `kind`

- `name`

| Property | Type | Description |
|----|----|----|
| `apiGroup` | `string` | APIGroup is the group for the resource being referenced. If APIGroup is not specified, the specified Kind must be in the core API group. For any other third-party types, APIGroup is required. |
| `kind` | `string` | Kind is the type of resource being referenced |
| `name` | `string` | Name is the name of resource being referenced |

## .spec.dataSourceRef

Description
TypedObjectReference contains enough information to let you locate the typed referenced object

Type
`object`

Required
- `kind`

- `name`

| Property | Type | Description |
|----|----|----|
| `apiGroup` | `string` | APIGroup is the group for the resource being referenced. If APIGroup is not specified, the specified Kind must be in the core API group. For any other third-party types, APIGroup is required. |
| `kind` | `string` | Kind is the type of resource being referenced |
| `name` | `string` | Name is the name of resource being referenced |
| `namespace` | `string` | Namespace is the namespace of resource being referenced Note that when a namespace is specified, a gateway.networking.k8s.io/ReferenceGrant object is required in the referent namespace to allow that namespace’s owner to accept the reference. See the ReferenceGrant documentation for details. (Alpha) This field requires the CrossNamespaceVolumeDataSource feature gate to be enabled. |

## .spec.resources

Description
VolumeResourceRequirements describes the storage resource requirements for a volume.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `limits` | [`object (Quantity)`](../objects/index.md#io-k8s-apimachinery-pkg-api-resource-Quantity) | Limits describes the maximum amount of compute resources allowed. More info: <https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/> |
| `requests` | [`object (Quantity)`](../objects/index.md#io-k8s-apimachinery-pkg-api-resource-Quantity) | Requests describes the minimum amount of compute resources required. If Requests is omitted for a container, it defaults to Limits if that is explicitly specified, otherwise to an implementation-defined value. Requests cannot exceed Limits. More info: <https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/> |

## .status

Description
PersistentVolumeClaimStatus is the current status of a persistent volume claim.

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
<td style="text-align: left;"><p>accessModes contains the actual access modes the volume backing the PVC has. More info: <a href="https://kubernetes.io/docs/concepts/storage/persistent-volumes#access-modes-1">https://kubernetes.io/docs/concepts/storage/persistent-volumes#access-modes-1</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>allocatedResourceStatuses</code></p></td>
<td style="text-align: left;"><p><code>object (string)</code></p></td>
<td style="text-align: left;"><p>allocatedResourceStatuses stores status of resource being resized for the given PVC. Key names follow standard Kubernetes label syntax. Valid values are either: * Un-prefixed keys: - storage - the capacity of the volume. * Custom resources must use implementation-defined prefixed names such as "example.com/my-custom-resource" Apart from above values - keys that are unprefixed or have kubernetes.io prefix are considered reserved and hence may not be used.</p>
<p>ClaimResourceStatus can be in any of following states: - ControllerResizeInProgress: State set when resize controller starts resizing the volume in control-plane. - ControllerResizeFailed: State set when resize has failed in resize controller with a terminal error. - NodeResizePending: State set when resize controller has finished resizing the volume but further resizing of volume is needed on the node. - NodeResizeInProgress: State set when kubelet starts resizing the volume. - NodeResizeFailed: State set when resizing has failed in kubelet with a terminal error. Transient errors don’t set NodeResizeFailed. For example: if expanding a PVC for more capacity - this field can be one of the following states: - pvc.status.allocatedResourceStatus['storage'] = "ControllerResizeInProgress" - pvc.status.allocatedResourceStatus['storage'] = "ControllerResizeFailed" - pvc.status.allocatedResourceStatus['storage'] = "NodeResizePending" - pvc.status.allocatedResourceStatus['storage'] = "NodeResizeInProgress" - pvc.status.allocatedResourceStatus['storage'] = "NodeResizeFailed" When this field is not set, it means that no resize operation is in progress for the given PVC.</p>
<p>A controller that receives PVC update with previously unknown resourceName or ClaimResourceStatus should ignore the update for the purpose it was designed. For example - a controller that only is responsible for resizing capacity of the volume, should ignore PVC updates that change other valid resources associated with PVC.</p>
<p>This is an alpha field and requires enabling RecoverVolumeExpansionFailure feature.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>allocatedResources</code></p></td>
<td style="text-align: left;"><p><a href="../objects/index.xml#io-k8s-apimachinery-pkg-api-resource-Quantity"><code>object (Quantity)</code></a></p></td>
<td style="text-align: left;"><p>allocatedResources tracks the resources allocated to a PVC including its capacity. Key names follow standard Kubernetes label syntax. Valid values are either: * Un-prefixed keys: - storage - the capacity of the volume. * Custom resources must use implementation-defined prefixed names such as "example.com/my-custom-resource" Apart from above values - keys that are unprefixed or have kubernetes.io prefix are considered reserved and hence may not be used.</p>
<p>Capacity reported here may be larger than the actual capacity when a volume expansion operation is requested. For storage quota, the larger value from allocatedResources and PVC.spec.resources is used. If allocatedResources is not set, PVC.spec.resources alone is used for quota calculation. If a volume expansion capacity request is lowered, allocatedResources is only lowered if there are no expansion operations in progress and if the actual volume capacity is equal or lower than the requested capacity.</p>
<p>A controller that receives PVC update with previously unknown resourceName should ignore the update for the purpose it was designed. For example - a controller that only is responsible for resizing capacity of the volume, should ignore PVC updates that change other valid resources associated with PVC.</p>
<p>This is an alpha field and requires enabling RecoverVolumeExpansionFailure feature.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>capacity</code></p></td>
<td style="text-align: left;"><p><a href="../objects/index.xml#io-k8s-apimachinery-pkg-api-resource-Quantity"><code>object (Quantity)</code></a></p></td>
<td style="text-align: left;"><p>capacity represents the actual resources of the underlying volume.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>conditions</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>conditions is the current Condition of persistent volume claim. If underlying persistent volume is being resized then the Condition will be set to 'Resizing'.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>conditions[]</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>PersistentVolumeClaimCondition contains details about state of pvc</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>currentVolumeAttributesClassName</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>currentVolumeAttributesClassName is the current name of the VolumeAttributesClass the PVC is using. When unset, there is no VolumeAttributeClass applied to this PersistentVolumeClaim This is a beta field and requires enabling VolumeAttributesClass feature (off by default).</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>modifyVolumeStatus</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>ModifyVolumeStatus represents the status object of ControllerModifyVolume operation</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>phase</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>phase represents the current phase of PersistentVolumeClaim.</p>
<p>Possible enum values: - <code>"Bound"</code> used for PersistentVolumeClaims that are bound - <code>"Lost"</code> used for PersistentVolumeClaims that lost their underlying PersistentVolume. The claim was bound to a PersistentVolume and this volume does not exist any longer and all data on it was lost. - <code>"Pending"</code> used for PersistentVolumeClaims that are not yet bound</p></td>
</tr>
</tbody>
</table>

## .status.conditions

Description
conditions is the current Condition of persistent volume claim. If underlying persistent volume is being resized then the Condition will be set to 'Resizing'.

Type
`array`

## .status.conditions\[\]

Description
PersistentVolumeClaimCondition contains details about state of pvc

Type
`object`

Required
- `type`

- `status`

| Property | Type | Description |
|----|----|----|
| `lastProbeTime` | [`Time`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-Time) | lastProbeTime is the time we probed the condition. |
| `lastTransitionTime` | [`Time`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-Time) | lastTransitionTime is the time the condition transitioned from one status to another. |
| `message` | `string` | message is the human-readable message indicating details about last transition. |
| `reason` | `string` | reason is a unique, this should be a short, machine understandable string that gives the reason for condition’s last transition. If it reports "Resizing" that means the underlying persistent volume is being resized. |
| `status` | `string` | Status is the status of the condition. Can be True, False, Unknown. More info: <https://kubernetes.io/docs/reference/kubernetes-api/config-and-storage-resources/persistent-volume-claim-v1/#:~:text=state%20of%20pvc-,conditions.status,-(string)%2C%20required> |
| `type` | `string` | Type is the type of the condition. More info: <https://kubernetes.io/docs/reference/kubernetes-api/config-and-storage-resources/persistent-volume-claim-v1/#:~:text=set%20to%20%27ResizeStarted%27.-,PersistentVolumeClaimCondition,-contains%20details%20about> |

## .status.modifyVolumeStatus

Description
ModifyVolumeStatus represents the status object of ControllerModifyVolume operation

Type
`object`

Required
- `status`

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
<td style="text-align: left;"><p><code>status</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>status is the status of the ControllerModifyVolume operation. It can be in any of following states: - Pending Pending indicates that the PersistentVolumeClaim cannot be modified due to unmet requirements, such as the specified VolumeAttributesClass not existing. - InProgress InProgress indicates that the volume is being modified. - Infeasible Infeasible indicates that the request has been rejected as invalid by the CSI driver. To resolve the error, a valid VolumeAttributesClass needs to be specified. Note: New statuses can be added in the future. Consumers should check for unknown statuses and fail appropriately.</p>
<p>Possible enum values: - <code>"InProgress"</code> InProgress indicates that the volume is being modified - <code>"Infeasible"</code> Infeasible indicates that the request has been rejected as invalid by the CSI driver. To resolve the error, a valid VolumeAttributesClass needs to be specified - <code>"Pending"</code> Pending indicates that the PersistentVolumeClaim cannot be modified due to unmet requirements, such as the specified VolumeAttributesClass not existing</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>targetVolumeAttributesClassName</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>targetVolumeAttributesClassName is the name of the VolumeAttributesClass the PVC currently being reconciled</p></td>
</tr>
</tbody>
</table>

# API endpoints

The following API endpoints are available:

- `/api/v1/persistentvolumeclaims`

  - `GET`: list or watch objects of kind PersistentVolumeClaim

- `/api/v1/watch/persistentvolumeclaims`

  - `GET`: watch individual changes to a list of PersistentVolumeClaim. deprecated: use the 'watch' parameter with a list operation instead.

- `/api/v1/namespaces/{namespace}/persistentvolumeclaims`

  - `DELETE`: delete collection of PersistentVolumeClaim

  - `GET`: list or watch objects of kind PersistentVolumeClaim

  - `POST`: create a PersistentVolumeClaim

- `/api/v1/watch/namespaces/{namespace}/persistentvolumeclaims`

  - `GET`: watch individual changes to a list of PersistentVolumeClaim. deprecated: use the 'watch' parameter with a list operation instead.

- `/api/v1/namespaces/{namespace}/persistentvolumeclaims/{name}`

  - `DELETE`: delete a PersistentVolumeClaim

  - `GET`: read the specified PersistentVolumeClaim

  - `PATCH`: partially update the specified PersistentVolumeClaim

  - `PUT`: replace the specified PersistentVolumeClaim

- `/api/v1/watch/namespaces/{namespace}/persistentvolumeclaims/{name}`

  - `GET`: watch changes to an object of kind PersistentVolumeClaim. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.

- `/api/v1/namespaces/{namespace}/persistentvolumeclaims/{name}/status`

  - `GET`: read status of the specified PersistentVolumeClaim

  - `PATCH`: partially update status of the specified PersistentVolumeClaim

  - `PUT`: replace status of the specified PersistentVolumeClaim

## /api/v1/persistentvolumeclaims

HTTP method
`GET`

Description
list or watch objects of kind PersistentVolumeClaim

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`PersistentVolumeClaimList`](../objects/index.md#io-k8s-api-core-v1-PersistentVolumeClaimList) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /api/v1/watch/persistentvolumeclaims

HTTP method
`GET`

Description
watch individual changes to a list of PersistentVolumeClaim. deprecated: use the 'watch' parameter with a list operation instead.

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`WatchEvent`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /api/v1/namespaces/{namespace}/persistentvolumeclaims

HTTP method
`DELETE`

Description
delete collection of PersistentVolumeClaim

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
list or watch objects of kind PersistentVolumeClaim

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`PersistentVolumeClaimList`](../objects/index.md#io-k8s-api-core-v1-PersistentVolumeClaimList) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`POST`

Description
create a PersistentVolumeClaim

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`PersistentVolumeClaim`](persistentvolumeclaim-v1.md#persistentvolumeclaim-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`PersistentVolumeClaim`](persistentvolumeclaim-v1.md#persistentvolumeclaim-v1) schema |
| 201 - Created | [`PersistentVolumeClaim`](persistentvolumeclaim-v1.md#persistentvolumeclaim-v1) schema |
| 202 - Accepted | [`PersistentVolumeClaim`](persistentvolumeclaim-v1.md#persistentvolumeclaim-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /api/v1/watch/namespaces/{namespace}/persistentvolumeclaims

HTTP method
`GET`

Description
watch individual changes to a list of PersistentVolumeClaim. deprecated: use the 'watch' parameter with a list operation instead.

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`WatchEvent`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /api/v1/namespaces/{namespace}/persistentvolumeclaims/{name}

| Parameter | Type     | Description                       |
|-----------|----------|-----------------------------------|
| `name`    | `string` | name of the PersistentVolumeClaim |

Global path parameters

HTTP method
`DELETE`

Description
delete a PersistentVolumeClaim

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |

Query parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`PersistentVolumeClaim`](persistentvolumeclaim-v1.md#persistentvolumeclaim-v1) schema |
| 202 - Accepted | [`PersistentVolumeClaim`](persistentvolumeclaim-v1.md#persistentvolumeclaim-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`GET`

Description
read the specified PersistentVolumeClaim

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`PersistentVolumeClaim`](persistentvolumeclaim-v1.md#persistentvolumeclaim-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PATCH`

Description
partially update the specified PersistentVolumeClaim

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`PersistentVolumeClaim`](persistentvolumeclaim-v1.md#persistentvolumeclaim-v1) schema |
| 201 - Created | [`PersistentVolumeClaim`](persistentvolumeclaim-v1.md#persistentvolumeclaim-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PUT`

Description
replace the specified PersistentVolumeClaim

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`PersistentVolumeClaim`](persistentvolumeclaim-v1.md#persistentvolumeclaim-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`PersistentVolumeClaim`](persistentvolumeclaim-v1.md#persistentvolumeclaim-v1) schema |
| 201 - Created | [`PersistentVolumeClaim`](persistentvolumeclaim-v1.md#persistentvolumeclaim-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /api/v1/watch/namespaces/{namespace}/persistentvolumeclaims/{name}

| Parameter | Type     | Description                       |
|-----------|----------|-----------------------------------|
| `name`    | `string` | name of the PersistentVolumeClaim |

Global path parameters

HTTP method
`GET`

Description
watch changes to an object of kind PersistentVolumeClaim. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`WatchEvent`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /api/v1/namespaces/{namespace}/persistentvolumeclaims/{name}/status

| Parameter | Type     | Description                       |
|-----------|----------|-----------------------------------|
| `name`    | `string` | name of the PersistentVolumeClaim |

Global path parameters

HTTP method
`GET`

Description
read status of the specified PersistentVolumeClaim

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`PersistentVolumeClaim`](persistentvolumeclaim-v1.md#persistentvolumeclaim-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PATCH`

Description
partially update status of the specified PersistentVolumeClaim

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`PersistentVolumeClaim`](persistentvolumeclaim-v1.md#persistentvolumeclaim-v1) schema |
| 201 - Created | [`PersistentVolumeClaim`](persistentvolumeclaim-v1.md#persistentvolumeclaim-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PUT`

Description
replace status of the specified PersistentVolumeClaim

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`PersistentVolumeClaim`](persistentvolumeclaim-v1.md#persistentvolumeclaim-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`PersistentVolumeClaim`](persistentvolumeclaim-v1.md#persistentvolumeclaim-v1) schema |
| 201 - Created | [`PersistentVolumeClaim`](persistentvolumeclaim-v1.md#persistentvolumeclaim-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses
