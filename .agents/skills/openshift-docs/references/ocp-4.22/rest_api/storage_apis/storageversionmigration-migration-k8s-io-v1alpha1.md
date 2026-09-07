<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Description
StorageVersionMigration represents a migration of stored data to the latest storage version.

Type
`object`

# Specification

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ObjectMeta`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) | Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |
| `spec` | `object` | Specification of the migration. |
| `status` | `object` | Status of the migration. |

## .spec

Description
Specification of the migration.

Type
`object`

Required
- `resource`

| Property | Type | Description |
|----|----|----|
| `continueToken` | `string` | The token used in the list options to get the next chunk of objects to migrate. When the .status.conditions indicates the migration is "Running", users can use this token to check the progress of the migration. |
| `resource` | `object` | The resource that is being migrated. The migrator sends requests to the endpoint serving the resource. Immutable. |

## .spec.resource

Description
The resource that is being migrated. The migrator sends requests to the endpoint serving the resource. Immutable.

Type
`object`

| Property   | Type     | Description               |
|------------|----------|---------------------------|
| `group`    | `string` | The name of the group.    |
| `resource` | `string` | The name of the resource. |
| `version`  | `string` | The name of the version.  |

## .status

Description
Status of the migration.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `conditions` | `array` | The latest available observations of the migration’s current state. |
| `conditions[]` | `object` | Describes the state of a migration at a certain point. |

## .status.conditions

Description
The latest available observations of the migration’s current state.

Type
`array`

## .status.conditions\[\]

Description
Describes the state of a migration at a certain point.

Type
`object`

Required
- `status`

- `type`

| Property | Type | Description |
|----|----|----|
| `lastUpdateTime` | `string` | The last time this condition was updated. |
| `message` | `string` | A human readable message indicating details about the transition. |
| `reason` | `string` | The reason for the condition’s last transition. |
| `status` | `string` | Status of the condition, one of True, False, Unknown. |
| `type` | `string` | Type of the condition. |

# API endpoints

The following API endpoints are available:

- `/apis/migration.k8s.io/v1alpha1/storageversionmigrations`

  - `DELETE`: delete collection of StorageVersionMigration

  - `GET`: list objects of kind StorageVersionMigration

  - `POST`: create a StorageVersionMigration

- `/apis/migration.k8s.io/v1alpha1/storageversionmigrations/{name}`

  - `DELETE`: delete a StorageVersionMigration

  - `GET`: read the specified StorageVersionMigration

  - `PATCH`: partially update the specified StorageVersionMigration

  - `PUT`: replace the specified StorageVersionMigration

- `/apis/migration.k8s.io/v1alpha1/storageversionmigrations/{name}/status`

  - `GET`: read status of the specified StorageVersionMigration

  - `PATCH`: partially update status of the specified StorageVersionMigration

  - `PUT`: replace status of the specified StorageVersionMigration

## /apis/migration.k8s.io/v1alpha1/storageversionmigrations

HTTP method
`DELETE`

Description
delete collection of StorageVersionMigration

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Status`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`GET`

Description
list objects of kind StorageVersionMigration

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`StorageVersionMigrationList`](../objects/index.md#io-k8s-migration-v1alpha1-StorageVersionMigrationList) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`POST`

Description
create a StorageVersionMigration

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`StorageVersionMigration`](storageversionmigration-migration-k8s-io-v1alpha1.md#storageversionmigration-migration-k8s-io-v1alpha1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`StorageVersionMigration`](storageversionmigration-migration-k8s-io-v1alpha1.md#storageversionmigration-migration-k8s-io-v1alpha1) schema |
| 201 - Created | [`StorageVersionMigration`](storageversionmigration-migration-k8s-io-v1alpha1.md#storageversionmigration-migration-k8s-io-v1alpha1) schema |
| 202 - Accepted | [`StorageVersionMigration`](storageversionmigration-migration-k8s-io-v1alpha1.md#storageversionmigration-migration-k8s-io-v1alpha1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/migration.k8s.io/v1alpha1/storageversionmigrations/{name}

| Parameter | Type     | Description                         |
|-----------|----------|-------------------------------------|
| `name`    | `string` | name of the StorageVersionMigration |

Global path parameters

HTTP method
`DELETE`

Description
delete a StorageVersionMigration

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
read the specified StorageVersionMigration

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`StorageVersionMigration`](storageversionmigration-migration-k8s-io-v1alpha1.md#storageversionmigration-migration-k8s-io-v1alpha1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PATCH`

Description
partially update the specified StorageVersionMigration

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`StorageVersionMigration`](storageversionmigration-migration-k8s-io-v1alpha1.md#storageversionmigration-migration-k8s-io-v1alpha1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PUT`

Description
replace the specified StorageVersionMigration

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`StorageVersionMigration`](storageversionmigration-migration-k8s-io-v1alpha1.md#storageversionmigration-migration-k8s-io-v1alpha1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`StorageVersionMigration`](storageversionmigration-migration-k8s-io-v1alpha1.md#storageversionmigration-migration-k8s-io-v1alpha1) schema |
| 201 - Created | [`StorageVersionMigration`](storageversionmigration-migration-k8s-io-v1alpha1.md#storageversionmigration-migration-k8s-io-v1alpha1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/migration.k8s.io/v1alpha1/storageversionmigrations/{name}/status

| Parameter | Type     | Description                         |
|-----------|----------|-------------------------------------|
| `name`    | `string` | name of the StorageVersionMigration |

Global path parameters

HTTP method
`GET`

Description
read status of the specified StorageVersionMigration

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`StorageVersionMigration`](storageversionmigration-migration-k8s-io-v1alpha1.md#storageversionmigration-migration-k8s-io-v1alpha1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PATCH`

Description
partially update status of the specified StorageVersionMigration

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`StorageVersionMigration`](storageversionmigration-migration-k8s-io-v1alpha1.md#storageversionmigration-migration-k8s-io-v1alpha1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PUT`

Description
replace status of the specified StorageVersionMigration

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`StorageVersionMigration`](storageversionmigration-migration-k8s-io-v1alpha1.md#storageversionmigration-migration-k8s-io-v1alpha1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`StorageVersionMigration`](storageversionmigration-migration-k8s-io-v1alpha1.md#storageversionmigration-migration-k8s-io-v1alpha1) schema |
| 201 - Created | [`StorageVersionMigration`](storageversionmigration-migration-k8s-io-v1alpha1.md#storageversionmigration-migration-k8s-io-v1alpha1) schema |
| 401 - Unauthorized | Empty |

HTTP responses
