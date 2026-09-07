<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Description
Scale represents a scaling request for a resource.

Type
`object`

# Specification

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ObjectMeta`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) | Standard object metadata; More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata>. |
| `spec` | `object` | ScaleSpec describes the attributes of a scale subresource. |
| `status` | `object` | ScaleStatus represents the current status of a scale subresource. |

## .spec

Description
ScaleSpec describes the attributes of a scale subresource.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `replicas` | `integer` | replicas is the desired number of instances for the scaled object. |

## .status

Description
ScaleStatus represents the current status of a scale subresource.

Type
`object`

Required
- `replicas`

| Property | Type | Description |
|----|----|----|
| `replicas` | `integer` | replicas is the actual number of observed instances of the scaled object. |
| `selector` | `string` | selector is the label query over pods that should match the replicas count. This is same as the label selector but in the string format to avoid introspection by clients. The string will be in the same format as the query-param syntax. More info about label selectors: <https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/> |

# API endpoints

The following API endpoints are available:

- `/apis/apps/v1/namespaces/{namespace}/deployments/{name}/scale`

  - `GET`: read scale of the specified Deployment

  - `PATCH`: partially update scale of the specified Deployment

  - `PUT`: replace scale of the specified Deployment

- `/apis/apps/v1/namespaces/{namespace}/replicasets/{name}/scale`

  - `GET`: read scale of the specified ReplicaSet

  - `PATCH`: partially update scale of the specified ReplicaSet

  - `PUT`: replace scale of the specified ReplicaSet

- `/apis/apps/v1/namespaces/{namespace}/statefulsets/{name}/scale`

  - `GET`: read scale of the specified StatefulSet

  - `PATCH`: partially update scale of the specified StatefulSet

  - `PUT`: replace scale of the specified StatefulSet

- `/api/v1/namespaces/{namespace}/replicationcontrollers/{name}/scale`

  - `GET`: read scale of the specified ReplicationController

  - `PATCH`: partially update scale of the specified ReplicationController

  - `PUT`: replace scale of the specified ReplicationController

## /apis/apps/v1/namespaces/{namespace}/deployments/{name}/scale

| Parameter | Type     | Description       |
|-----------|----------|-------------------|
| `name`    | `string` | name of the Scale |

Global path parameters

HTTP method
`GET`

Description
read scale of the specified Deployment

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Scale`](scale-autoscaling-v1.md#scale-autoscaling-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PATCH`

Description
partially update scale of the specified Deployment

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Scale`](scale-autoscaling-v1.md#scale-autoscaling-v1) schema |
| 201 - Created | [`Scale`](scale-autoscaling-v1.md#scale-autoscaling-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PUT`

Description
replace scale of the specified Deployment

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`Scale`](scale-autoscaling-v1.md#scale-autoscaling-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Scale`](scale-autoscaling-v1.md#scale-autoscaling-v1) schema |
| 201 - Created | [`Scale`](scale-autoscaling-v1.md#scale-autoscaling-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/apps/v1/namespaces/{namespace}/replicasets/{name}/scale

| Parameter | Type     | Description       |
|-----------|----------|-------------------|
| `name`    | `string` | name of the Scale |

Global path parameters

HTTP method
`GET`

Description
read scale of the specified ReplicaSet

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Scale`](scale-autoscaling-v1.md#scale-autoscaling-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PATCH`

Description
partially update scale of the specified ReplicaSet

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Scale`](scale-autoscaling-v1.md#scale-autoscaling-v1) schema |
| 201 - Created | [`Scale`](scale-autoscaling-v1.md#scale-autoscaling-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PUT`

Description
replace scale of the specified ReplicaSet

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`Scale`](scale-autoscaling-v1.md#scale-autoscaling-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Scale`](scale-autoscaling-v1.md#scale-autoscaling-v1) schema |
| 201 - Created | [`Scale`](scale-autoscaling-v1.md#scale-autoscaling-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/apps/v1/namespaces/{namespace}/statefulsets/{name}/scale

| Parameter | Type     | Description       |
|-----------|----------|-------------------|
| `name`    | `string` | name of the Scale |

Global path parameters

HTTP method
`GET`

Description
read scale of the specified StatefulSet

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Scale`](scale-autoscaling-v1.md#scale-autoscaling-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PATCH`

Description
partially update scale of the specified StatefulSet

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Scale`](scale-autoscaling-v1.md#scale-autoscaling-v1) schema |
| 201 - Created | [`Scale`](scale-autoscaling-v1.md#scale-autoscaling-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PUT`

Description
replace scale of the specified StatefulSet

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`Scale`](scale-autoscaling-v1.md#scale-autoscaling-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Scale`](scale-autoscaling-v1.md#scale-autoscaling-v1) schema |
| 201 - Created | [`Scale`](scale-autoscaling-v1.md#scale-autoscaling-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /api/v1/namespaces/{namespace}/replicationcontrollers/{name}/scale

| Parameter | Type     | Description       |
|-----------|----------|-------------------|
| `name`    | `string` | name of the Scale |

Global path parameters

HTTP method
`GET`

Description
read scale of the specified ReplicationController

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Scale`](scale-autoscaling-v1.md#scale-autoscaling-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PATCH`

Description
partially update scale of the specified ReplicationController

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Scale`](scale-autoscaling-v1.md#scale-autoscaling-v1) schema |
| 201 - Created | [`Scale`](scale-autoscaling-v1.md#scale-autoscaling-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PUT`

Description
replace scale of the specified ReplicationController

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`Scale`](scale-autoscaling-v1.md#scale-autoscaling-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Scale`](scale-autoscaling-v1.md#scale-autoscaling-v1) schema |
| 201 - Created | [`Scale`](scale-autoscaling-v1.md#scale-autoscaling-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses
