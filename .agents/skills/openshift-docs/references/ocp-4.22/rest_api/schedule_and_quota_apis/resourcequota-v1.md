<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Description
ResourceQuota sets aggregate quota restrictions enforced per namespace

Type
`object`

# Specification

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ObjectMeta`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) | Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |
| `spec` | `object` | ResourceQuotaSpec defines the desired hard limits to enforce for Quota. |
| `status` | `object` | ResourceQuotaStatus defines the enforced hard limits and observed use. |

## .spec

Description
ResourceQuotaSpec defines the desired hard limits to enforce for Quota.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `hard` | [`object (Quantity)`](../objects/index.md#io-k8s-apimachinery-pkg-api-resource-Quantity) | hard is the set of desired hard limits for each named resource. More info: <https://kubernetes.io/docs/concepts/policy/resource-quotas/> |
| `scopeSelector` | `object` | A scope selector represents the AND of the selectors represented by the scoped-resource selector requirements. |
| `scopes` | `array (string)` | A collection of filters that must match each object tracked by a quota. If not specified, the quota matches all objects. |

## .spec.scopeSelector

Description
A scope selector represents the AND of the selectors represented by the scoped-resource selector requirements.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `matchExpressions` | `array` | A list of scope selector requirements by scope of the resources. |
| `matchExpressions[]` | `object` | A scoped-resource selector requirement is a selector that contains values, a scope name, and an operator that relates the scope name and values. |

## .spec.scopeSelector.matchExpressions

Description
A list of scope selector requirements by scope of the resources.

Type
`array`

## .spec.scopeSelector.matchExpressions\[\]

Description
A scoped-resource selector requirement is a selector that contains values, a scope name, and an operator that relates the scope name and values.

Type
`object`

Required
- `scopeName`

- `operator`

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
<td style="text-align: left;"><p><code>operator</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Represents a scope’s relationship to a set of values. Valid operators are In, NotIn, Exists, DoesNotExist.</p>
<p>Possible enum values: - <code>"DoesNotExist"</code> - <code>"Exists"</code> - <code>"In"</code> - <code>"NotIn"</code></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>scopeName</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>The name of the scope that the selector applies to.</p>
<p>Possible enum values: - <code>"BestEffort"</code> Match all pod objects that have best effort quality of service - <code>"CrossNamespacePodAffinity"</code> Match all pod objects that have cross-namespace pod (anti)affinity mentioned. - <code>"NotBestEffort"</code> Match all pod objects that do not have best effort quality of service - <code>"NotTerminating"</code> Match all pod objects where spec.activeDeadlineSeconds is nil - <code>"PriorityClass"</code> Match all pod objects that have priority class mentioned - <code>"Terminating"</code> Match all pod objects where spec.activeDeadlineSeconds &gt;=0 - <code>"VolumeAttributesClass"</code> Match all pvc objects that have volume attributes class mentioned.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>values</code></p></td>
<td style="text-align: left;"><p><code>array (string)</code></p></td>
<td style="text-align: left;"><p>An array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch.</p></td>
</tr>
</tbody>
</table>

## .status

Description
ResourceQuotaStatus defines the enforced hard limits and observed use.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `hard` | [`object (Quantity)`](../objects/index.md#io-k8s-apimachinery-pkg-api-resource-Quantity) | Hard is the set of enforced hard limits for each named resource. More info: <https://kubernetes.io/docs/concepts/policy/resource-quotas/> |
| `used` | [`object (Quantity)`](../objects/index.md#io-k8s-apimachinery-pkg-api-resource-Quantity) | Used is the current observed total usage of the resource in the namespace. |

# API endpoints

The following API endpoints are available:

- `/api/v1/resourcequotas`

  - `GET`: list or watch objects of kind ResourceQuota

- `/api/v1/watch/resourcequotas`

  - `GET`: watch individual changes to a list of ResourceQuota. deprecated: use the 'watch' parameter with a list operation instead.

- `/api/v1/namespaces/{namespace}/resourcequotas`

  - `DELETE`: delete collection of ResourceQuota

  - `GET`: list or watch objects of kind ResourceQuota

  - `POST`: create a ResourceQuota

- `/api/v1/watch/namespaces/{namespace}/resourcequotas`

  - `GET`: watch individual changes to a list of ResourceQuota. deprecated: use the 'watch' parameter with a list operation instead.

- `/api/v1/namespaces/{namespace}/resourcequotas/{name}`

  - `DELETE`: delete a ResourceQuota

  - `GET`: read the specified ResourceQuota

  - `PATCH`: partially update the specified ResourceQuota

  - `PUT`: replace the specified ResourceQuota

- `/api/v1/watch/namespaces/{namespace}/resourcequotas/{name}`

  - `GET`: watch changes to an object of kind ResourceQuota. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.

- `/api/v1/namespaces/{namespace}/resourcequotas/{name}/status`

  - `GET`: read status of the specified ResourceQuota

  - `PATCH`: partially update status of the specified ResourceQuota

  - `PUT`: replace status of the specified ResourceQuota

## /api/v1/resourcequotas

HTTP method
`GET`

Description
list or watch objects of kind ResourceQuota

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ResourceQuotaList`](../objects/index.md#io-k8s-api-core-v1-ResourceQuotaList) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /api/v1/watch/resourcequotas

HTTP method
`GET`

Description
watch individual changes to a list of ResourceQuota. deprecated: use the 'watch' parameter with a list operation instead.

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`WatchEvent`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /api/v1/namespaces/{namespace}/resourcequotas

HTTP method
`DELETE`

Description
delete collection of ResourceQuota

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
list or watch objects of kind ResourceQuota

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ResourceQuotaList`](../objects/index.md#io-k8s-api-core-v1-ResourceQuotaList) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`POST`

Description
create a ResourceQuota

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`ResourceQuota`](resourcequota-v1.md#resourcequota-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ResourceQuota`](resourcequota-v1.md#resourcequota-v1) schema |
| 201 - Created | [`ResourceQuota`](resourcequota-v1.md#resourcequota-v1) schema |
| 202 - Accepted | [`ResourceQuota`](resourcequota-v1.md#resourcequota-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /api/v1/watch/namespaces/{namespace}/resourcequotas

HTTP method
`GET`

Description
watch individual changes to a list of ResourceQuota. deprecated: use the 'watch' parameter with a list operation instead.

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`WatchEvent`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /api/v1/namespaces/{namespace}/resourcequotas/{name}

| Parameter | Type     | Description               |
|-----------|----------|---------------------------|
| `name`    | `string` | name of the ResourceQuota |

Global path parameters

HTTP method
`DELETE`

Description
delete a ResourceQuota

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |

Query parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ResourceQuota`](resourcequota-v1.md#resourcequota-v1) schema |
| 202 - Accepted | [`ResourceQuota`](resourcequota-v1.md#resourcequota-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`GET`

Description
read the specified ResourceQuota

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ResourceQuota`](resourcequota-v1.md#resourcequota-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PATCH`

Description
partially update the specified ResourceQuota

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ResourceQuota`](resourcequota-v1.md#resourcequota-v1) schema |
| 201 - Created | [`ResourceQuota`](resourcequota-v1.md#resourcequota-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PUT`

Description
replace the specified ResourceQuota

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`ResourceQuota`](resourcequota-v1.md#resourcequota-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ResourceQuota`](resourcequota-v1.md#resourcequota-v1) schema |
| 201 - Created | [`ResourceQuota`](resourcequota-v1.md#resourcequota-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /api/v1/watch/namespaces/{namespace}/resourcequotas/{name}

| Parameter | Type     | Description               |
|-----------|----------|---------------------------|
| `name`    | `string` | name of the ResourceQuota |

Global path parameters

HTTP method
`GET`

Description
watch changes to an object of kind ResourceQuota. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`WatchEvent`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /api/v1/namespaces/{namespace}/resourcequotas/{name}/status

| Parameter | Type     | Description               |
|-----------|----------|---------------------------|
| `name`    | `string` | name of the ResourceQuota |

Global path parameters

HTTP method
`GET`

Description
read status of the specified ResourceQuota

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ResourceQuota`](resourcequota-v1.md#resourcequota-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PATCH`

Description
partially update status of the specified ResourceQuota

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ResourceQuota`](resourcequota-v1.md#resourcequota-v1) schema |
| 201 - Created | [`ResourceQuota`](resourcequota-v1.md#resourcequota-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PUT`

Description
replace status of the specified ResourceQuota

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`ResourceQuota`](resourcequota-v1.md#resourcequota-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ResourceQuota`](resourcequota-v1.md#resourcequota-v1) schema |
| 201 - Created | [`ResourceQuota`](resourcequota-v1.md#resourcequota-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses
