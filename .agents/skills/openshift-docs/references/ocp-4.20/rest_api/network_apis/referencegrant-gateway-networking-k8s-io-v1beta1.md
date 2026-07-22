<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Description
ReferenceGrant identifies kinds of resources in other namespaces that are trusted to reference the specified kinds of resources in the same namespace as the policy.

Each ReferenceGrant can be used to represent a unique trust relationship. Additional Reference Grants can be used to add to the set of trusted sources of inbound references for the namespace they are defined within.

All cross-namespace references in Gateway API (with the exception of cross-namespace Gateway-route attachment) require a ReferenceGrant.

ReferenceGrant is a form of runtime verification allowing users to assert which cross-namespace object references are permitted. Implementations that support ReferenceGrant MUST NOT permit cross-namespace references which have no grant, and MUST respond to the removal of a grant by revoking the access that the grant allowed.

Type
`object`

# Specification

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ObjectMeta`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) | Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |
| `spec` | `object` | Spec defines the desired state of ReferenceGrant. |

## .spec

Description
Spec defines the desired state of ReferenceGrant.

Type
`object`

Required
- `from`

- `to`

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
<td style="text-align: left;"><p><code>from</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>From describes the trusted namespaces and kinds that can reference the resources described in "To". Each entry in this list MUST be considered to be an additional place that references can be valid from, or to put this another way, entries MUST be combined using OR.</p>
<p>Support: Core</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>from[]</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>ReferenceGrantFrom describes trusted namespaces and kinds.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>to</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>To describes the resources that may be referenced by the resources described in "From". Each entry in this list MUST be considered to be an additional place that references can be valid to, or to put this another way, entries MUST be combined using OR.</p>
<p>Support: Core</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>to[]</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>ReferenceGrantTo describes what Kinds are allowed as targets of the references.</p></td>
</tr>
</tbody>
</table>

## .spec.from

Description
From describes the trusted namespaces and kinds that can reference the resources described in "To". Each entry in this list MUST be considered to be an additional place that references can be valid from, or to put this another way, entries MUST be combined using OR.

Support: Core

Type
`array`

## .spec.from\[\]

Description
ReferenceGrantFrom describes trusted namespaces and kinds.

Type
`object`

Required
- `group`

- `kind`

- `namespace`

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
<td style="text-align: left;"><p><code>group</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Group is the group of the referent. When empty, the Kubernetes core API group is inferred.</p>
<p>Support: Core</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>kind</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Kind is the kind of the referent. Although implementations may support additional resources, the following types are part of the "Core" support level for this field.</p>
<p>When used to permit a SecretObjectReference:</p>
<p>* Gateway</p>
<p>When used to permit a BackendObjectReference:</p>
<p>* GRPCRoute * HTTPRoute * TCPRoute * TLSRoute * UDPRoute</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>namespace</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Namespace is the namespace of the referent.</p>
<p>Support: Core</p></td>
</tr>
</tbody>
</table>

## .spec.to

Description
To describes the resources that may be referenced by the resources described in "From". Each entry in this list MUST be considered to be an additional place that references can be valid to, or to put this another way, entries MUST be combined using OR.

Support: Core

Type
`array`

## .spec.to\[\]

Description
ReferenceGrantTo describes what Kinds are allowed as targets of the references.

Type
`object`

Required
- `group`

- `kind`

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
<td style="text-align: left;"><p><code>group</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Group is the group of the referent. When empty, the Kubernetes core API group is inferred.</p>
<p>Support: Core</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>kind</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Kind is the kind of the referent. Although implementations may support additional resources, the following types are part of the "Core" support level for this field:</p>
<p>* Secret when used to permit a SecretObjectReference * Service when used to permit a BackendObjectReference</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>name</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Name is the name of the referent. When unspecified, this policy refers to all resources of the specified Group and Kind in the local namespace.</p></td>
</tr>
</tbody>
</table>

# API endpoints

The following API endpoints are available:

- `/apis/gateway.networking.k8s.io/v1beta1/referencegrants`

  - `GET`: list objects of kind ReferenceGrant

- `/apis/gateway.networking.k8s.io/v1beta1/namespaces/{namespace}/referencegrants`

  - `DELETE`: delete collection of ReferenceGrant

  - `GET`: list objects of kind ReferenceGrant

  - `POST`: create a ReferenceGrant

- `/apis/gateway.networking.k8s.io/v1beta1/namespaces/{namespace}/referencegrants/{name}`

  - `DELETE`: delete a ReferenceGrant

  - `GET`: read the specified ReferenceGrant

  - `PATCH`: partially update the specified ReferenceGrant

  - `PUT`: replace the specified ReferenceGrant

## /apis/gateway.networking.k8s.io/v1beta1/referencegrants

HTTP method
`GET`

Description
list objects of kind ReferenceGrant

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ReferenceGrantList`](../objects/index.md#io-k8s-networking-gateway-v1beta1-ReferenceGrantList) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/gateway.networking.k8s.io/v1beta1/namespaces/{namespace}/referencegrants

HTTP method
`DELETE`

Description
delete collection of ReferenceGrant

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Status`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`GET`

Description
list objects of kind ReferenceGrant

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ReferenceGrantList`](../objects/index.md#io-k8s-networking-gateway-v1beta1-ReferenceGrantList) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`POST`

Description
create a ReferenceGrant

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`ReferenceGrant`](referencegrant-gateway-networking-k8s-io-v1beta1.md#referencegrant-gateway-networking-k8s-io-v1beta1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ReferenceGrant`](referencegrant-gateway-networking-k8s-io-v1beta1.md#referencegrant-gateway-networking-k8s-io-v1beta1) schema |
| 201 - Created | [`ReferenceGrant`](referencegrant-gateway-networking-k8s-io-v1beta1.md#referencegrant-gateway-networking-k8s-io-v1beta1) schema |
| 202 - Accepted | [`ReferenceGrant`](referencegrant-gateway-networking-k8s-io-v1beta1.md#referencegrant-gateway-networking-k8s-io-v1beta1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/gateway.networking.k8s.io/v1beta1/namespaces/{namespace}/referencegrants/{name}

| Parameter | Type     | Description                |
|-----------|----------|----------------------------|
| `name`    | `string` | name of the ReferenceGrant |

Global path parameters

HTTP method
`DELETE`

Description
delete a ReferenceGrant

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
read the specified ReferenceGrant

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ReferenceGrant`](referencegrant-gateway-networking-k8s-io-v1beta1.md#referencegrant-gateway-networking-k8s-io-v1beta1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PATCH`

Description
partially update the specified ReferenceGrant

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ReferenceGrant`](referencegrant-gateway-networking-k8s-io-v1beta1.md#referencegrant-gateway-networking-k8s-io-v1beta1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PUT`

Description
replace the specified ReferenceGrant

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`ReferenceGrant`](referencegrant-gateway-networking-k8s-io-v1beta1.md#referencegrant-gateway-networking-k8s-io-v1beta1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ReferenceGrant`](referencegrant-gateway-networking-k8s-io-v1beta1.md#referencegrant-gateway-networking-k8s-io-v1beta1) schema |
| 201 - Created | [`ReferenceGrant`](referencegrant-gateway-networking-k8s-io-v1beta1.md#referencegrant-gateway-networking-k8s-io-v1beta1) schema |
| 401 - Unauthorized | Empty |

HTTP responses
