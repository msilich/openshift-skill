<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Description
VolumeSnapshot is a user’s request for either creating a point-in-time snapshot of a persistent volume, or binding to a pre-existing snapshot.

Type
`object`

Required
- `spec`

# Specification

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ObjectMeta`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) | Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |
| `spec` | `object` | spec defines the desired characteristics of a snapshot requested by a user. More info: <https://kubernetes.io/docs/concepts/storage/volume-snapshots#volumesnapshots> Required. |
| `status` | `object` | status represents the current information of a snapshot. Consumers must verify binding between VolumeSnapshot and VolumeSnapshotContent objects is successful (by validating that both VolumeSnapshot and VolumeSnapshotContent point at each other) before using this object. |

## .spec

Description
spec defines the desired characteristics of a snapshot requested by a user. More info: <https://kubernetes.io/docs/concepts/storage/volume-snapshots#volumesnapshots> Required.

Type
`object`

Required
- `source`

| Property | Type | Description |
|----|----|----|
| `source` | `object` | source specifies where a snapshot will be created from. This field is immutable after creation. Required. |
| `volumeSnapshotClassName` | `string` | VolumeSnapshotClassName is the name of the VolumeSnapshotClass requested by the VolumeSnapshot. VolumeSnapshotClassName may be left nil to indicate that the default SnapshotClass should be used. A given cluster may have multiple default Volume SnapshotClasses: one default per CSI Driver. If a VolumeSnapshot does not specify a SnapshotClass, VolumeSnapshotSource will be checked to figure out what the associated CSI Driver is, and the default VolumeSnapshotClass associated with that CSI Driver will be used. If more than one VolumeSnapshotClass exist for a given CSI Driver and more than one have been marked as default, CreateSnapshot will fail and generate an event. Empty string is not allowed for this field. |

## .spec.source

Description
source specifies where a snapshot will be created from. This field is immutable after creation. Required.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `persistentVolumeClaimName` | `string` | persistentVolumeClaimName specifies the name of the PersistentVolumeClaim object representing the volume from which a snapshot should be created. This PVC is assumed to be in the same namespace as the VolumeSnapshot object. This field should be set if the snapshot does not exists, and needs to be created. This field is immutable. |
| `volumeSnapshotContentName` | `string` | volumeSnapshotContentName specifies the name of a pre-existing VolumeSnapshotContent object representing an existing volume snapshot. This field should be set if the snapshot already exists and only needs a representation in Kubernetes. This field is immutable. |

## .status

Description
status represents the current information of a snapshot. Consumers must verify binding between VolumeSnapshot and VolumeSnapshotContent objects is successful (by validating that both VolumeSnapshot and VolumeSnapshotContent point at each other) before using this object.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `boundVolumeSnapshotContentName` | `string` | boundVolumeSnapshotContentName is the name of the VolumeSnapshotContent object to which this VolumeSnapshot object intends to bind to. If not specified, it indicates that the VolumeSnapshot object has not been successfully bound to a VolumeSnapshotContent object yet. NOTE: To avoid possible security issues, consumers must verify binding between VolumeSnapshot and VolumeSnapshotContent objects is successful (by validating that both VolumeSnapshot and VolumeSnapshotContent point at each other) before using this object. |
| `creationTime` | `string` | creationTime is the timestamp when the point-in-time snapshot is taken by the underlying storage system. In dynamic snapshot creation case, this field will be filled in by the snapshot controller with the "creation_time" value returned from CSI "CreateSnapshot" gRPC call. For a pre-existing snapshot, this field will be filled with the "creation_time" value returned from the CSI "ListSnapshots" gRPC call if the driver supports it. If not specified, it may indicate that the creation time of the snapshot is unknown. |
| `error` | `object` | error is the last observed error during snapshot creation, if any. This field could be helpful to upper level controllers(i.e., application controller) to decide whether they should continue on waiting for the snapshot to be created based on the type of error reported. The snapshot controller will keep retrying when an error occurs during the snapshot creation. Upon success, this error field will be cleared. |
| `readyToUse` | `boolean` | readyToUse indicates if the snapshot is ready to be used to restore a volume. In dynamic snapshot creation case, this field will be filled in by the snapshot controller with the "ready_to_use" value returned from CSI "CreateSnapshot" gRPC call. For a pre-existing snapshot, this field will be filled with the "ready_to_use" value returned from the CSI "ListSnapshots" gRPC call if the driver supports it, otherwise, this field will be set to "True". If not specified, it means the readiness of a snapshot is unknown. |
| `restoreSize` | `integer-or-string` | restoreSize represents the minimum size of volume required to create a volume from this snapshot. In dynamic snapshot creation case, this field will be filled in by the snapshot controller with the "size_bytes" value returned from CSI "CreateSnapshot" gRPC call. For a pre-existing snapshot, this field will be filled with the "size_bytes" value returned from the CSI "ListSnapshots" gRPC call if the driver supports it. When restoring a volume from this snapshot, the size of the volume MUST NOT be smaller than the restoreSize if it is specified, otherwise the restoration will fail. If not specified, it indicates that the size is unknown. |
| `volumeGroupSnapshotName` | `string` | VolumeGroupSnapshotName is the name of the VolumeGroupSnapshot of which this VolumeSnapshot is a part of. |

## .status.error

Description
error is the last observed error during snapshot creation, if any. This field could be helpful to upper level controllers(i.e., application controller) to decide whether they should continue on waiting for the snapshot to be created based on the type of error reported. The snapshot controller will keep retrying when an error occurs during the snapshot creation. Upon success, this error field will be cleared.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `message` | `string` | message is a string detailing the encountered error during snapshot creation if specified. NOTE: message may be logged, and it should not contain sensitive information. |
| `time` | `string` | time is the timestamp when the error was encountered. |

# API endpoints

The following API endpoints are available:

- `/apis/snapshot.storage.k8s.io/v1/volumesnapshots`

  - `GET`: list objects of kind VolumeSnapshot

- `/apis/snapshot.storage.k8s.io/v1/namespaces/{namespace}/volumesnapshots`

  - `DELETE`: delete collection of VolumeSnapshot

  - `GET`: list objects of kind VolumeSnapshot

  - `POST`: create a VolumeSnapshot

- `/apis/snapshot.storage.k8s.io/v1/namespaces/{namespace}/volumesnapshots/{name}`

  - `DELETE`: delete a VolumeSnapshot

  - `GET`: read the specified VolumeSnapshot

  - `PATCH`: partially update the specified VolumeSnapshot

  - `PUT`: replace the specified VolumeSnapshot

- `/apis/snapshot.storage.k8s.io/v1/namespaces/{namespace}/volumesnapshots/{name}/status`

  - `GET`: read status of the specified VolumeSnapshot

  - `PATCH`: partially update status of the specified VolumeSnapshot

  - `PUT`: replace status of the specified VolumeSnapshot

## /apis/snapshot.storage.k8s.io/v1/volumesnapshots

HTTP method
`GET`

Description
list objects of kind VolumeSnapshot

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`VolumeSnapshotList`](../objects/index.md#io-k8s-storage-snapshot-v1-VolumeSnapshotList) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/snapshot.storage.k8s.io/v1/namespaces/{namespace}/volumesnapshots

HTTP method
`DELETE`

Description
delete collection of VolumeSnapshot

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Status`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`GET`

Description
list objects of kind VolumeSnapshot

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`VolumeSnapshotList`](../objects/index.md#io-k8s-storage-snapshot-v1-VolumeSnapshotList) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`POST`

Description
create a VolumeSnapshot

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`VolumeSnapshot`](volumesnapshot-snapshot-storage-k8s-io-v1.md#volumesnapshot-snapshot-storage-k8s-io-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`VolumeSnapshot`](volumesnapshot-snapshot-storage-k8s-io-v1.md#volumesnapshot-snapshot-storage-k8s-io-v1) schema |
| 201 - Created | [`VolumeSnapshot`](volumesnapshot-snapshot-storage-k8s-io-v1.md#volumesnapshot-snapshot-storage-k8s-io-v1) schema |
| 202 - Accepted | [`VolumeSnapshot`](volumesnapshot-snapshot-storage-k8s-io-v1.md#volumesnapshot-snapshot-storage-k8s-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/snapshot.storage.k8s.io/v1/namespaces/{namespace}/volumesnapshots/{name}

| Parameter | Type     | Description                |
|-----------|----------|----------------------------|
| `name`    | `string` | name of the VolumeSnapshot |

Global path parameters

HTTP method
`DELETE`

Description
delete a VolumeSnapshot

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |

Query parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Status`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 202 - Accepted | [`Status`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`GET`

Description
read the specified VolumeSnapshot

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`VolumeSnapshot`](volumesnapshot-snapshot-storage-k8s-io-v1.md#volumesnapshot-snapshot-storage-k8s-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PATCH`

Description
partially update the specified VolumeSnapshot

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`VolumeSnapshot`](volumesnapshot-snapshot-storage-k8s-io-v1.md#volumesnapshot-snapshot-storage-k8s-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PUT`

Description
replace the specified VolumeSnapshot

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`VolumeSnapshot`](volumesnapshot-snapshot-storage-k8s-io-v1.md#volumesnapshot-snapshot-storage-k8s-io-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`VolumeSnapshot`](volumesnapshot-snapshot-storage-k8s-io-v1.md#volumesnapshot-snapshot-storage-k8s-io-v1) schema |
| 201 - Created | [`VolumeSnapshot`](volumesnapshot-snapshot-storage-k8s-io-v1.md#volumesnapshot-snapshot-storage-k8s-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/snapshot.storage.k8s.io/v1/namespaces/{namespace}/volumesnapshots/{name}/status

| Parameter | Type     | Description                |
|-----------|----------|----------------------------|
| `name`    | `string` | name of the VolumeSnapshot |

Global path parameters

HTTP method
`GET`

Description
read status of the specified VolumeSnapshot

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`VolumeSnapshot`](volumesnapshot-snapshot-storage-k8s-io-v1.md#volumesnapshot-snapshot-storage-k8s-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PATCH`

Description
partially update status of the specified VolumeSnapshot

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`VolumeSnapshot`](volumesnapshot-snapshot-storage-k8s-io-v1.md#volumesnapshot-snapshot-storage-k8s-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PUT`

Description
replace status of the specified VolumeSnapshot

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`VolumeSnapshot`](volumesnapshot-snapshot-storage-k8s-io-v1.md#volumesnapshot-snapshot-storage-k8s-io-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`VolumeSnapshot`](volumesnapshot-snapshot-storage-k8s-io-v1.md#volumesnapshot-snapshot-storage-k8s-io-v1) schema |
| 201 - Created | [`VolumeSnapshot`](volumesnapshot-snapshot-storage-k8s-io-v1.md#volumesnapshot-snapshot-storage-k8s-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses
