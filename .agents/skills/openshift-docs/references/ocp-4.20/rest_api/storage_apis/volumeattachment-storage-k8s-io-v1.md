<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Description
VolumeAttachment captures the intent to attach or detach the specified volume to/from the specified node.

VolumeAttachment objects are non-namespaced.

Type
`object`

Required
- `spec`

# Specification

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ObjectMeta`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) | Standard object metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |
| `spec` | `object` | VolumeAttachmentSpec is the specification of a VolumeAttachment request. |
| `status` | `object` | VolumeAttachmentStatus is the status of a VolumeAttachment request. |

## .spec

Description
VolumeAttachmentSpec is the specification of a VolumeAttachment request.

Type
`object`

Required
- `attacher`

- `source`

- `nodeName`

| Property | Type | Description |
|----|----|----|
| `attacher` | `string` | attacher indicates the name of the volume driver that MUST handle this request. This is the name returned by GetPluginName(). |
| `nodeName` | `string` | nodeName represents the node that the volume should be attached to. |
| `source` | `object` | VolumeAttachmentSource represents a volume that should be attached. Right now only PersistentVolumes can be attached via external attacher, in the future we may allow also inline volumes in pods. Exactly one member can be set. |

## .spec.source

Description
VolumeAttachmentSource represents a volume that should be attached. Right now only PersistentVolumes can be attached via external attacher, in the future we may allow also inline volumes in pods. Exactly one member can be set.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `inlineVolumeSpec` | [`PersistentVolumeSpec`](../objects/index.md#io-k8s-api-core-v1-PersistentVolumeSpec) | inlineVolumeSpec contains all the information necessary to attach a persistent volume defined by a pod’s inline VolumeSource. This field is populated only for the CSIMigration feature. It contains translated fields from a pod’s inline VolumeSource to a PersistentVolumeSpec. This field is beta-level and is only honored by servers that enabled the CSIMigration feature. |
| `persistentVolumeName` | `string` | persistentVolumeName represents the name of the persistent volume to attach. |

## .status

Description
VolumeAttachmentStatus is the status of a VolumeAttachment request.

Type
`object`

Required
- `attached`

| Property | Type | Description |
|----|----|----|
| `attachError` | `object` | VolumeError captures an error encountered during a volume operation. |
| `attached` | `boolean` | attached indicates the volume is successfully attached. This field must only be set by the entity completing the attach operation, i.e. the external-attacher. |
| `attachmentMetadata` | `object (string)` | attachmentMetadata is populated with any information returned by the attach operation, upon successful attach, that must be passed into subsequent WaitForAttach or Mount calls. This field must only be set by the entity completing the attach operation, i.e. the external-attacher. |
| `detachError` | `object` | VolumeError captures an error encountered during a volume operation. |

## .status.attachError

Description
VolumeError captures an error encountered during a volume operation.

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
<td style="text-align: left;"><p><code>errorCode</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p>errorCode is a numeric gRPC code representing the error encountered during Attach or Detach operations.</p>
<p>This is an optional, alpha field that requires the MutableCSINodeAllocatableCount feature gate being enabled to be set.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>message</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>message represents the error encountered during Attach or Detach operation. This string may be logged, so it should not contain sensitive information.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>time</code></p></td>
<td style="text-align: left;"><p><a href="../objects/index.xml#io-k8s-apimachinery-pkg-apis-meta-v1-Time"><code>Time</code></a></p></td>
<td style="text-align: left;"><p>time represents the time the error was encountered.</p></td>
</tr>
</tbody>
</table>

## .status.detachError

Description
VolumeError captures an error encountered during a volume operation.

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
<td style="text-align: left;"><p><code>errorCode</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p>errorCode is a numeric gRPC code representing the error encountered during Attach or Detach operations.</p>
<p>This is an optional, alpha field that requires the MutableCSINodeAllocatableCount feature gate being enabled to be set.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>message</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>message represents the error encountered during Attach or Detach operation. This string may be logged, so it should not contain sensitive information.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>time</code></p></td>
<td style="text-align: left;"><p><a href="../objects/index.xml#io-k8s-apimachinery-pkg-apis-meta-v1-Time"><code>Time</code></a></p></td>
<td style="text-align: left;"><p>time represents the time the error was encountered.</p></td>
</tr>
</tbody>
</table>

# API endpoints

The following API endpoints are available:

- `/apis/storage.k8s.io/v1/volumeattachments`

  - `DELETE`: delete collection of VolumeAttachment

  - `GET`: list or watch objects of kind VolumeAttachment

  - `POST`: create a VolumeAttachment

- `/apis/storage.k8s.io/v1/watch/volumeattachments`

  - `GET`: watch individual changes to a list of VolumeAttachment. deprecated: use the 'watch' parameter with a list operation instead.

- `/apis/storage.k8s.io/v1/volumeattachments/{name}`

  - `DELETE`: delete a VolumeAttachment

  - `GET`: read the specified VolumeAttachment

  - `PATCH`: partially update the specified VolumeAttachment

  - `PUT`: replace the specified VolumeAttachment

- `/apis/storage.k8s.io/v1/watch/volumeattachments/{name}`

  - `GET`: watch changes to an object of kind VolumeAttachment. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.

- `/apis/storage.k8s.io/v1/volumeattachments/{name}/status`

  - `GET`: read status of the specified VolumeAttachment

  - `PATCH`: partially update status of the specified VolumeAttachment

  - `PUT`: replace status of the specified VolumeAttachment

## /apis/storage.k8s.io/v1/volumeattachments

HTTP method
`DELETE`

Description
delete collection of VolumeAttachment

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
list or watch objects of kind VolumeAttachment

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`VolumeAttachmentList`](../objects/index.md#io-k8s-api-storage-v1-VolumeAttachmentList) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`POST`

Description
create a VolumeAttachment

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`VolumeAttachment`](volumeattachment-storage-k8s-io-v1.md#volumeattachment-storage-k8s-io-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`VolumeAttachment`](volumeattachment-storage-k8s-io-v1.md#volumeattachment-storage-k8s-io-v1) schema |
| 201 - Created | [`VolumeAttachment`](volumeattachment-storage-k8s-io-v1.md#volumeattachment-storage-k8s-io-v1) schema |
| 202 - Accepted | [`VolumeAttachment`](volumeattachment-storage-k8s-io-v1.md#volumeattachment-storage-k8s-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/storage.k8s.io/v1/watch/volumeattachments

HTTP method
`GET`

Description
watch individual changes to a list of VolumeAttachment. deprecated: use the 'watch' parameter with a list operation instead.

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`WatchEvent`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/storage.k8s.io/v1/volumeattachments/{name}

| Parameter | Type     | Description                  |
|-----------|----------|------------------------------|
| `name`    | `string` | name of the VolumeAttachment |

Global path parameters

HTTP method
`DELETE`

Description
delete a VolumeAttachment

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |

Query parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`VolumeAttachment`](volumeattachment-storage-k8s-io-v1.md#volumeattachment-storage-k8s-io-v1) schema |
| 202 - Accepted | [`VolumeAttachment`](volumeattachment-storage-k8s-io-v1.md#volumeattachment-storage-k8s-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`GET`

Description
read the specified VolumeAttachment

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`VolumeAttachment`](volumeattachment-storage-k8s-io-v1.md#volumeattachment-storage-k8s-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PATCH`

Description
partially update the specified VolumeAttachment

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`VolumeAttachment`](volumeattachment-storage-k8s-io-v1.md#volumeattachment-storage-k8s-io-v1) schema |
| 201 - Created | [`VolumeAttachment`](volumeattachment-storage-k8s-io-v1.md#volumeattachment-storage-k8s-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PUT`

Description
replace the specified VolumeAttachment

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`VolumeAttachment`](volumeattachment-storage-k8s-io-v1.md#volumeattachment-storage-k8s-io-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`VolumeAttachment`](volumeattachment-storage-k8s-io-v1.md#volumeattachment-storage-k8s-io-v1) schema |
| 201 - Created | [`VolumeAttachment`](volumeattachment-storage-k8s-io-v1.md#volumeattachment-storage-k8s-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/storage.k8s.io/v1/watch/volumeattachments/{name}

| Parameter | Type     | Description                  |
|-----------|----------|------------------------------|
| `name`    | `string` | name of the VolumeAttachment |

Global path parameters

HTTP method
`GET`

Description
watch changes to an object of kind VolumeAttachment. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`WatchEvent`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/storage.k8s.io/v1/volumeattachments/{name}/status

| Parameter | Type     | Description                  |
|-----------|----------|------------------------------|
| `name`    | `string` | name of the VolumeAttachment |

Global path parameters

HTTP method
`GET`

Description
read status of the specified VolumeAttachment

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`VolumeAttachment`](volumeattachment-storage-k8s-io-v1.md#volumeattachment-storage-k8s-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PATCH`

Description
partially update status of the specified VolumeAttachment

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`VolumeAttachment`](volumeattachment-storage-k8s-io-v1.md#volumeattachment-storage-k8s-io-v1) schema |
| 201 - Created | [`VolumeAttachment`](volumeattachment-storage-k8s-io-v1.md#volumeattachment-storage-k8s-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PUT`

Description
replace status of the specified VolumeAttachment

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`VolumeAttachment`](volumeattachment-storage-k8s-io-v1.md#volumeattachment-storage-k8s-io-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`VolumeAttachment`](volumeattachment-storage-k8s-io-v1.md#volumeattachment-storage-k8s-io-v1) schema |
| 201 - Created | [`VolumeAttachment`](volumeattachment-storage-k8s-io-v1.md#volumeattachment-storage-k8s-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses
