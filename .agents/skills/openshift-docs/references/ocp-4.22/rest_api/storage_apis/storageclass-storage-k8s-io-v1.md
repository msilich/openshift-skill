<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Description
StorageClass describes the parameters for a class of storage for which PersistentVolumes can be dynamically provisioned.

StorageClasses are non-namespaced; the name of the storage class according to etcd is in ObjectMeta.Name.

Type
`object`

Required
- `provisioner`

# Specification

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
<td style="text-align: left;"><p><code>allowVolumeExpansion</code></p></td>
<td style="text-align: left;"><p><code>boolean</code></p></td>
<td style="text-align: left;"><p>allowVolumeExpansion shows whether the storage class allow volume expand.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>allowedTopologies</code></p></td>
<td style="text-align: left;"><p><a href="../objects/index.xml#io-k8s-api-core-v1-TopologySelectorTerm"><code>array (TopologySelectorTerm)</code></a></p></td>
<td style="text-align: left;"><p>allowedTopologies restrict the node topologies where volumes can be dynamically provisioned. Each volume plugin defines its own supported topology specifications. An empty TopologySelectorTerm list means there is no topology restriction. This field is only honored by servers that enable the VolumeScheduling feature.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>apiVersion</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <a href="https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources">https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>kind</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <a href="https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds">https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>metadata</code></p></td>
<td style="text-align: left;"><p><a href="../objects/index.xml#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta"><code>ObjectMeta</code></a></p></td>
<td style="text-align: left;"><p>Standard object’s metadata. More info: <a href="https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata">https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>mountOptions</code></p></td>
<td style="text-align: left;"><p><code>array (string)</code></p></td>
<td style="text-align: left;"><p>mountOptions controls the mountOptions for dynamically provisioned PersistentVolumes of this storage class. e.g. ["ro", "soft"]. Not validated - mount of the PVs will simply fail if one is invalid.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>parameters</code></p></td>
<td style="text-align: left;"><p><code>object (string)</code></p></td>
<td style="text-align: left;"><p>parameters holds the parameters for the provisioner that should create volumes of this storage class.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>provisioner</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>provisioner indicates the type of the provisioner.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>reclaimPolicy</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>reclaimPolicy controls the reclaimPolicy for dynamically provisioned PersistentVolumes of this storage class. Defaults to Delete.</p>
<p>Possible enum values: - <code>"Delete"</code> means the volume will be deleted from Kubernetes on release from its claim. The volume plugin must support Deletion. - <code>"Recycle"</code> means the volume will be recycled back into the pool of unbound persistent volumes on release from its claim. The volume plugin must support Recycling. - <code>"Retain"</code> means the volume will be left in its current phase (Released) for manual reclamation by the administrator. The default policy is Retain.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>volumeBindingMode</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>volumeBindingMode indicates how PersistentVolumeClaims should be provisioned and bound. When unset, VolumeBindingImmediate is used. This field is only honored by servers that enable the VolumeScheduling feature.</p>
<p>Possible enum values: - <code>"Immediate"</code> indicates that PersistentVolumeClaims should be immediately provisioned and bound. This is the default mode. - <code>"WaitForFirstConsumer"</code> indicates that PersistentVolumeClaims should not be provisioned and bound until the first Pod is created that references the PeristentVolumeClaim. The volume provisioning and binding will occur during Pod scheduing.</p></td>
</tr>
</tbody>
</table>

# API endpoints

The following API endpoints are available:

- `/apis/storage.k8s.io/v1/storageclasses`

  - `DELETE`: delete collection of StorageClass

  - `GET`: list or watch objects of kind StorageClass

  - `POST`: create a StorageClass

- `/apis/storage.k8s.io/v1/watch/storageclasses`

  - `GET`: watch individual changes to a list of StorageClass. deprecated: use the 'watch' parameter with a list operation instead.

- `/apis/storage.k8s.io/v1/storageclasses/{name}`

  - `DELETE`: delete a StorageClass

  - `GET`: read the specified StorageClass

  - `PATCH`: partially update the specified StorageClass

  - `PUT`: replace the specified StorageClass

- `/apis/storage.k8s.io/v1/watch/storageclasses/{name}`

  - `GET`: watch changes to an object of kind StorageClass. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.

## /apis/storage.k8s.io/v1/storageclasses

HTTP method
`DELETE`

Description
delete collection of StorageClass

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
list or watch objects of kind StorageClass

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`StorageClassList`](../objects/index.md#io-k8s-api-storage-v1-StorageClassList) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`POST`

Description
create a StorageClass

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`StorageClass`](storageclass-storage-k8s-io-v1.md#storageclass-storage-k8s-io-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`StorageClass`](storageclass-storage-k8s-io-v1.md#storageclass-storage-k8s-io-v1) schema |
| 201 - Created | [`StorageClass`](storageclass-storage-k8s-io-v1.md#storageclass-storage-k8s-io-v1) schema |
| 202 - Accepted | [`StorageClass`](storageclass-storage-k8s-io-v1.md#storageclass-storage-k8s-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/storage.k8s.io/v1/watch/storageclasses

HTTP method
`GET`

Description
watch individual changes to a list of StorageClass. deprecated: use the 'watch' parameter with a list operation instead.

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`WatchEvent`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/storage.k8s.io/v1/storageclasses/{name}

| Parameter | Type     | Description              |
|-----------|----------|--------------------------|
| `name`    | `string` | name of the StorageClass |

Global path parameters

HTTP method
`DELETE`

Description
delete a StorageClass

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |

Query parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`StorageClass`](storageclass-storage-k8s-io-v1.md#storageclass-storage-k8s-io-v1) schema |
| 202 - Accepted | [`StorageClass`](storageclass-storage-k8s-io-v1.md#storageclass-storage-k8s-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`GET`

Description
read the specified StorageClass

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`StorageClass`](storageclass-storage-k8s-io-v1.md#storageclass-storage-k8s-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PATCH`

Description
partially update the specified StorageClass

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`StorageClass`](storageclass-storage-k8s-io-v1.md#storageclass-storage-k8s-io-v1) schema |
| 201 - Created | [`StorageClass`](storageclass-storage-k8s-io-v1.md#storageclass-storage-k8s-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PUT`

Description
replace the specified StorageClass

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`StorageClass`](storageclass-storage-k8s-io-v1.md#storageclass-storage-k8s-io-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`StorageClass`](storageclass-storage-k8s-io-v1.md#storageclass-storage-k8s-io-v1) schema |
| 201 - Created | [`StorageClass`](storageclass-storage-k8s-io-v1.md#storageclass-storage-k8s-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/storage.k8s.io/v1/watch/storageclasses/{name}

| Parameter | Type     | Description              |
|-----------|----------|--------------------------|
| `name`    | `string` | name of the StorageClass |

Global path parameters

HTTP method
`GET`

Description
watch changes to an object of kind StorageClass. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`WatchEvent`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema |
| 401 - Unauthorized | Empty |

HTTP responses
