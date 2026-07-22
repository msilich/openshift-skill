<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Description
PriorityClass defines mapping from a priority class name to the priority integer value. The value can be any valid integer.

Type
`object`

Required
- `value`

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
<td style="text-align: left;"><p><code>apiVersion</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <a href="https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources">https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>description</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>description is an arbitrary string that usually provides guidelines on when this priority class should be used.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>globalDefault</code></p></td>
<td style="text-align: left;"><p><code>boolean</code></p></td>
<td style="text-align: left;"><p>globalDefault specifies whether this PriorityClass should be considered as the default priority for pods that do not have any priority class. Only one PriorityClass can be marked as <code>globalDefault</code>. However, if more than one PriorityClasses exists with their <code>globalDefault</code> field set to true, the smallest value of such global default PriorityClasses will be used as the default priority.</p></td>
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
<td style="text-align: left;"><p><code>preemptionPolicy</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>preemptionPolicy is the Policy for preempting pods with lower priority. One of Never, PreemptLowerPriority. Defaults to PreemptLowerPriority if unset.</p>
<p>Possible enum values: - <code>"Never"</code> means that pod never preempts other pods with lower priority. - <code>"PreemptLowerPriority"</code> means that pod can preempt other pods with lower priority.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>value</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p>value represents the integer value of this priority class. This is the actual priority that pods receive when they have the name of this class in their pod spec.</p></td>
</tr>
</tbody>
</table>

# API endpoints

The following API endpoints are available:

- `/apis/scheduling.k8s.io/v1/priorityclasses`

  - `DELETE`: delete collection of PriorityClass

  - `GET`: list or watch objects of kind PriorityClass

  - `POST`: create a PriorityClass

- `/apis/scheduling.k8s.io/v1/watch/priorityclasses`

  - `GET`: watch individual changes to a list of PriorityClass. deprecated: use the 'watch' parameter with a list operation instead.

- `/apis/scheduling.k8s.io/v1/priorityclasses/{name}`

  - `DELETE`: delete a PriorityClass

  - `GET`: read the specified PriorityClass

  - `PATCH`: partially update the specified PriorityClass

  - `PUT`: replace the specified PriorityClass

- `/apis/scheduling.k8s.io/v1/watch/priorityclasses/{name}`

  - `GET`: watch changes to an object of kind PriorityClass. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.

## /apis/scheduling.k8s.io/v1/priorityclasses

HTTP method
`DELETE`

Description
delete collection of PriorityClass

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
list or watch objects of kind PriorityClass

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`PriorityClassList`](../objects/index.md#io-k8s-api-scheduling-v1-PriorityClassList) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`POST`

Description
create a PriorityClass

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`PriorityClass`](priorityclass-scheduling-k8s-io-v1.md#priorityclass-scheduling-k8s-io-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`PriorityClass`](priorityclass-scheduling-k8s-io-v1.md#priorityclass-scheduling-k8s-io-v1) schema |
| 201 - Created | [`PriorityClass`](priorityclass-scheduling-k8s-io-v1.md#priorityclass-scheduling-k8s-io-v1) schema |
| 202 - Accepted | [`PriorityClass`](priorityclass-scheduling-k8s-io-v1.md#priorityclass-scheduling-k8s-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/scheduling.k8s.io/v1/watch/priorityclasses

HTTP method
`GET`

Description
watch individual changes to a list of PriorityClass. deprecated: use the 'watch' parameter with a list operation instead.

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`WatchEvent`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/scheduling.k8s.io/v1/priorityclasses/{name}

| Parameter | Type     | Description               |
|-----------|----------|---------------------------|
| `name`    | `string` | name of the PriorityClass |

Global path parameters

HTTP method
`DELETE`

Description
delete a PriorityClass

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
read the specified PriorityClass

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`PriorityClass`](priorityclass-scheduling-k8s-io-v1.md#priorityclass-scheduling-k8s-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PATCH`

Description
partially update the specified PriorityClass

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`PriorityClass`](priorityclass-scheduling-k8s-io-v1.md#priorityclass-scheduling-k8s-io-v1) schema |
| 201 - Created | [`PriorityClass`](priorityclass-scheduling-k8s-io-v1.md#priorityclass-scheduling-k8s-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PUT`

Description
replace the specified PriorityClass

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`PriorityClass`](priorityclass-scheduling-k8s-io-v1.md#priorityclass-scheduling-k8s-io-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`PriorityClass`](priorityclass-scheduling-k8s-io-v1.md#priorityclass-scheduling-k8s-io-v1) schema |
| 201 - Created | [`PriorityClass`](priorityclass-scheduling-k8s-io-v1.md#priorityclass-scheduling-k8s-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/scheduling.k8s.io/v1/watch/priorityclasses/{name}

| Parameter | Type     | Description               |
|-----------|----------|---------------------------|
| `name`    | `string` | name of the PriorityClass |

Global path parameters

HTTP method
`GET`

Description
watch changes to an object of kind PriorityClass. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`WatchEvent`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema |
| 401 - Unauthorized | Empty |

HTTP responses
