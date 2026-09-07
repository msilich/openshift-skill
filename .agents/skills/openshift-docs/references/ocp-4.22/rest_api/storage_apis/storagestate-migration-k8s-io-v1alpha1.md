<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Description
The state of the storage of a specific resource.

Type
`object`

# Specification

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ObjectMeta`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) | Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |
| `spec` | `object` | Specification of the storage state. |
| `status` | `object` | Status of the storage state. |

## .spec

Description
Specification of the storage state.

Type
`object`

| Property   | Type     | Description                              |
|------------|----------|------------------------------------------|
| `resource` | `object` | The resource this storageState is about. |

## .spec.resource

Description
The resource this storageState is about.

Type
`object`

| Property   | Type     | Description               |
|------------|----------|---------------------------|
| `group`    | `string` | The name of the group.    |
| `resource` | `string` | The name of the resource. |

## .status

Description
Status of the storage state.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `currentStorageVersionHash` | `string` | The hash value of the current storage version, as shown in the discovery document served by the API server. Storage Version is the version to which objects are converted to before persisted. |
| `lastHeartbeatTime` | `string` | LastHeartbeatTime is the last time the storage migration triggering controller checks the storage version hash of this resource in the discovery document and updates this field. |
| `persistedStorageVersionHashes` | `array (string)` | The hash values of storage versions that persisted instances of spec.resource might still be encoded in. "Unknown" is a valid value in the list, and is the default value. It is not safe to upgrade or downgrade to an apiserver binary that does not support all versions listed in this field, or if "Unknown" is listed. Once the storage version migration for this resource has completed, the value of this field is refined to only contain the currentStorageVersionHash. Once the apiserver has changed the storage version, the new storage version is appended to the list. |

# API endpoints

The following API endpoints are available:

- `/apis/migration.k8s.io/v1alpha1/storagestates`

  - `DELETE`: delete collection of StorageState

  - `GET`: list objects of kind StorageState

  - `POST`: create a StorageState

- `/apis/migration.k8s.io/v1alpha1/storagestates/{name}`

  - `DELETE`: delete a StorageState

  - `GET`: read the specified StorageState

  - `PATCH`: partially update the specified StorageState

  - `PUT`: replace the specified StorageState

- `/apis/migration.k8s.io/v1alpha1/storagestates/{name}/status`

  - `GET`: read status of the specified StorageState

  - `PATCH`: partially update status of the specified StorageState

  - `PUT`: replace status of the specified StorageState

## /apis/migration.k8s.io/v1alpha1/storagestates

HTTP method
`DELETE`

Description
delete collection of StorageState

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Status`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`GET`

Description
list objects of kind StorageState

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`StorageStateList`](../objects/index.md#io-k8s-migration-v1alpha1-StorageStateList) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`POST`

Description
create a StorageState

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`StorageState`](storagestate-migration-k8s-io-v1alpha1.md#storagestate-migration-k8s-io-v1alpha1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`StorageState`](storagestate-migration-k8s-io-v1alpha1.md#storagestate-migration-k8s-io-v1alpha1) schema |
| 201 - Created | [`StorageState`](storagestate-migration-k8s-io-v1alpha1.md#storagestate-migration-k8s-io-v1alpha1) schema |
| 202 - Accepted | [`StorageState`](storagestate-migration-k8s-io-v1alpha1.md#storagestate-migration-k8s-io-v1alpha1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/migration.k8s.io/v1alpha1/storagestates/{name}

| Parameter | Type     | Description              |
|-----------|----------|--------------------------|
| `name`    | `string` | name of the StorageState |

Global path parameters

HTTP method
`DELETE`

Description
delete a StorageState

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
read the specified StorageState

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`StorageState`](storagestate-migration-k8s-io-v1alpha1.md#storagestate-migration-k8s-io-v1alpha1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PATCH`

Description
partially update the specified StorageState

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`StorageState`](storagestate-migration-k8s-io-v1alpha1.md#storagestate-migration-k8s-io-v1alpha1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PUT`

Description
replace the specified StorageState

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`StorageState`](storagestate-migration-k8s-io-v1alpha1.md#storagestate-migration-k8s-io-v1alpha1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`StorageState`](storagestate-migration-k8s-io-v1alpha1.md#storagestate-migration-k8s-io-v1alpha1) schema |
| 201 - Created | [`StorageState`](storagestate-migration-k8s-io-v1alpha1.md#storagestate-migration-k8s-io-v1alpha1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/migration.k8s.io/v1alpha1/storagestates/{name}/status

| Parameter | Type     | Description              |
|-----------|----------|--------------------------|
| `name`    | `string` | name of the StorageState |

Global path parameters

HTTP method
`GET`

Description
read status of the specified StorageState

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`StorageState`](storagestate-migration-k8s-io-v1alpha1.md#storagestate-migration-k8s-io-v1alpha1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PATCH`

Description
partially update status of the specified StorageState

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`StorageState`](storagestate-migration-k8s-io-v1alpha1.md#storagestate-migration-k8s-io-v1alpha1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PUT`

Description
replace status of the specified StorageState

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`StorageState`](storagestate-migration-k8s-io-v1alpha1.md#storagestate-migration-k8s-io-v1alpha1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`StorageState`](storagestate-migration-k8s-io-v1alpha1.md#storagestate-migration-k8s-io-v1alpha1) schema |
| 201 - Created | [`StorageState`](storagestate-migration-k8s-io-v1alpha1.md#storagestate-migration-k8s-io-v1alpha1) schema |
| 401 - Unauthorized | Empty |

HTTP responses
