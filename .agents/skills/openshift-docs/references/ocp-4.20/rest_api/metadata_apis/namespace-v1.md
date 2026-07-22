<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Description
Namespace provides a scope for Names. Use of multiple namespaces is optional.

Type
`object`

# Specification

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ObjectMeta`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) | Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |
| `spec` | `object` | NamespaceSpec describes the attributes on a Namespace. |
| `status` | `object` | NamespaceStatus is information about the current status of a Namespace. |

## .spec

Description
NamespaceSpec describes the attributes on a Namespace.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `finalizers` | `array (string)` | Finalizers is an opaque list of values that must be empty to permanently remove object from storage. More info: <https://kubernetes.io/docs/tasks/administer-cluster/namespaces/> |

## .status

Description
NamespaceStatus is information about the current status of a Namespace.

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
<td style="text-align: left;"><p><code>conditions</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>Represents the latest available observations of a namespace’s current state.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>conditions[]</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>NamespaceCondition contains details about state of namespace.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>phase</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Phase is the current lifecycle phase of the namespace. More info: <a href="https://kubernetes.io/docs/tasks/administer-cluster/namespaces/">https://kubernetes.io/docs/tasks/administer-cluster/namespaces/</a></p>
<p>Possible enum values: - <code>"Active"</code> means the namespace is available for use in the system - <code>"Terminating"</code> means the namespace is undergoing graceful termination</p></td>
</tr>
</tbody>
</table>

## .status.conditions

Description
Represents the latest available observations of a namespace’s current state.

Type
`array`

## .status.conditions\[\]

Description
NamespaceCondition contains details about state of namespace.

Type
`object`

Required
- `type`

- `status`

| Property | Type | Description |
|----|----|----|
| `lastTransitionTime` | [`Time`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-Time) | Last time the condition transitioned from one status to another. |
| `message` | `string` | Human-readable message indicating details about last transition. |
| `reason` | `string` | Unique, one-word, CamelCase reason for the condition’s last transition. |
| `status` | `string` | Status of the condition, one of True, False, Unknown. |
| `type` | `string` | Type of namespace controller condition. |

# API endpoints

The following API endpoints are available:

- `/api/v1/namespaces`

  - `GET`: list or watch objects of kind Namespace

  - `POST`: create a Namespace

- `/api/v1/watch/namespaces`

  - `GET`: watch individual changes to a list of Namespace. deprecated: use the 'watch' parameter with a list operation instead.

- `/api/v1/namespaces/{name}`

  - `DELETE`: delete a Namespace

  - `GET`: read the specified Namespace

  - `PATCH`: partially update the specified Namespace

  - `PUT`: replace the specified Namespace

- `/api/v1/watch/namespaces/{name}`

  - `GET`: watch changes to an object of kind Namespace. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.

- `/api/v1/namespaces/{name}/status`

  - `GET`: read status of the specified Namespace

  - `PATCH`: partially update status of the specified Namespace

  - `PUT`: replace status of the specified Namespace

- `/api/v1/namespaces/{name}/finalize`

  - `PUT`: replace finalize of the specified Namespace

## /api/v1/namespaces

HTTP method
`GET`

Description
list or watch objects of kind Namespace

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`NamespaceList`](../objects/index.md#io-k8s-api-core-v1-NamespaceList) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`POST`

Description
create a Namespace

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`Namespace`](namespace-v1.md#namespace-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Namespace`](namespace-v1.md#namespace-v1) schema |
| 201 - Created | [`Namespace`](namespace-v1.md#namespace-v1) schema |
| 202 - Accepted | [`Namespace`](namespace-v1.md#namespace-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /api/v1/watch/namespaces

HTTP method
`GET`

Description
watch individual changes to a list of Namespace. deprecated: use the 'watch' parameter with a list operation instead.

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`WatchEvent`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /api/v1/namespaces/{name}

| Parameter | Type     | Description           |
|-----------|----------|-----------------------|
| `name`    | `string` | name of the Namespace |

Global path parameters

HTTP method
`DELETE`

Description
delete a Namespace

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
read the specified Namespace

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Namespace`](namespace-v1.md#namespace-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PATCH`

Description
partially update the specified Namespace

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Namespace`](namespace-v1.md#namespace-v1) schema |
| 201 - Created | [`Namespace`](namespace-v1.md#namespace-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PUT`

Description
replace the specified Namespace

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`Namespace`](namespace-v1.md#namespace-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Namespace`](namespace-v1.md#namespace-v1) schema |
| 201 - Created | [`Namespace`](namespace-v1.md#namespace-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /api/v1/watch/namespaces/{name}

| Parameter | Type     | Description           |
|-----------|----------|-----------------------|
| `name`    | `string` | name of the Namespace |

Global path parameters

HTTP method
`GET`

Description
watch changes to an object of kind Namespace. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`WatchEvent`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /api/v1/namespaces/{name}/status

| Parameter | Type     | Description           |
|-----------|----------|-----------------------|
| `name`    | `string` | name of the Namespace |

Global path parameters

HTTP method
`GET`

Description
read status of the specified Namespace

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Namespace`](namespace-v1.md#namespace-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PATCH`

Description
partially update status of the specified Namespace

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Namespace`](namespace-v1.md#namespace-v1) schema |
| 201 - Created | [`Namespace`](namespace-v1.md#namespace-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PUT`

Description
replace status of the specified Namespace

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`Namespace`](namespace-v1.md#namespace-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Namespace`](namespace-v1.md#namespace-v1) schema |
| 201 - Created | [`Namespace`](namespace-v1.md#namespace-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /api/v1/namespaces/{name}/finalize

| Parameter | Type     | Description           |
|-----------|----------|-----------------------|
| `name`    | `string` | name of the Namespace |

Global path parameters

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Global query parameters

HTTP method
`PUT`

Description
replace finalize of the specified Namespace

| Parameter | Type | Description |
|----|----|----|
| `body` | [`Namespace`](namespace-v1.md#namespace-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Namespace`](namespace-v1.md#namespace-v1) schema |
| 201 - Created | [`Namespace`](namespace-v1.md#namespace-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses
