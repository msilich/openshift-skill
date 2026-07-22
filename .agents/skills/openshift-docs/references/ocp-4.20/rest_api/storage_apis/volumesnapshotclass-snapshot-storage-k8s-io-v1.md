<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Description
VolumeSnapshotClass specifies parameters that a underlying storage system uses when creating a volume snapshot. A specific VolumeSnapshotClass is used by specifying its name in a VolumeSnapshot object. VolumeSnapshotClasses are non-namespaced

Type
`object`

Required
- `deletionPolicy`

- `driver`

# Specification

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `deletionPolicy` | `string` | deletionPolicy determines whether a VolumeSnapshotContent created through the VolumeSnapshotClass should be deleted when its bound VolumeSnapshot is deleted. Supported values are "Retain" and "Delete". "Retain" means that the VolumeSnapshotContent and its physical snapshot on underlying storage system are kept. "Delete" means that the VolumeSnapshotContent and its physical snapshot on underlying storage system are deleted. Required. |
| `driver` | `string` | driver is the name of the storage driver that handles this VolumeSnapshotClass. Required. |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ObjectMeta`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) | Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |
| `parameters` | `object (string)` | parameters is a key-value map with storage driver specific parameters for creating snapshots. These values are opaque to Kubernetes. |

# API endpoints

The following API endpoints are available:

- `/apis/snapshot.storage.k8s.io/v1/volumesnapshotclasses`

  - `DELETE`: delete collection of VolumeSnapshotClass

  - `GET`: list objects of kind VolumeSnapshotClass

  - `POST`: create a VolumeSnapshotClass

- `/apis/snapshot.storage.k8s.io/v1/volumesnapshotclasses/{name}`

  - `DELETE`: delete a VolumeSnapshotClass

  - `GET`: read the specified VolumeSnapshotClass

  - `PATCH`: partially update the specified VolumeSnapshotClass

  - `PUT`: replace the specified VolumeSnapshotClass

## /apis/snapshot.storage.k8s.io/v1/volumesnapshotclasses

HTTP method
`DELETE`

Description
delete collection of VolumeSnapshotClass

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Status`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`GET`

Description
list objects of kind VolumeSnapshotClass

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`VolumeSnapshotClassList`](../objects/index.md#io-k8s-storage-snapshot-v1-VolumeSnapshotClassList) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`POST`

Description
create a VolumeSnapshotClass

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`VolumeSnapshotClass`](volumesnapshotclass-snapshot-storage-k8s-io-v1.md#volumesnapshotclass-snapshot-storage-k8s-io-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`VolumeSnapshotClass`](volumesnapshotclass-snapshot-storage-k8s-io-v1.md#volumesnapshotclass-snapshot-storage-k8s-io-v1) schema |
| 201 - Created | [`VolumeSnapshotClass`](volumesnapshotclass-snapshot-storage-k8s-io-v1.md#volumesnapshotclass-snapshot-storage-k8s-io-v1) schema |
| 202 - Accepted | [`VolumeSnapshotClass`](volumesnapshotclass-snapshot-storage-k8s-io-v1.md#volumesnapshotclass-snapshot-storage-k8s-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/snapshot.storage.k8s.io/v1/volumesnapshotclasses/{name}

| Parameter | Type     | Description                     |
|-----------|----------|---------------------------------|
| `name`    | `string` | name of the VolumeSnapshotClass |

Global path parameters

HTTP method
`DELETE`

Description
delete a VolumeSnapshotClass

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
read the specified VolumeSnapshotClass

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`VolumeSnapshotClass`](volumesnapshotclass-snapshot-storage-k8s-io-v1.md#volumesnapshotclass-snapshot-storage-k8s-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PATCH`

Description
partially update the specified VolumeSnapshotClass

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`VolumeSnapshotClass`](volumesnapshotclass-snapshot-storage-k8s-io-v1.md#volumesnapshotclass-snapshot-storage-k8s-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PUT`

Description
replace the specified VolumeSnapshotClass

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`VolumeSnapshotClass`](volumesnapshotclass-snapshot-storage-k8s-io-v1.md#volumesnapshotclass-snapshot-storage-k8s-io-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`VolumeSnapshotClass`](volumesnapshotclass-snapshot-storage-k8s-io-v1.md#volumesnapshotclass-snapshot-storage-k8s-io-v1) schema |
| 201 - Created | [`VolumeSnapshotClass`](volumesnapshotclass-snapshot-storage-k8s-io-v1.md#volumesnapshotclass-snapshot-storage-k8s-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses
