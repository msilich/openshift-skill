<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Description
GatewayClass describes a class of Gateways available to the user for creating Gateway resources.

It is recommended that this resource be used as a template for Gateways. This means that a Gateway is based on the state of the GatewayClass at the time it was created and changes to the GatewayClass or associated parameters are not propagated down to existing Gateways. This recommendation is intended to limit the blast radius of changes to GatewayClass or associated parameters. If implementations choose to propagate GatewayClass changes to existing Gateways, that MUST be clearly documented by the implementation.

Whenever one or more Gateways are using a GatewayClass, implementations SHOULD add the `gateway-exists-finalizer.gateway.networking.k8s.io` finalizer on the associated GatewayClass. This ensures that a GatewayClass associated with a Gateway is not deleted while in use.

GatewayClass is a Cluster level resource.

Type
`object`

Required
- `spec`

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
<td style="text-align: left;"><p><code>spec</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>Spec defines the desired state of GatewayClass.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>status</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>Status defines the current state of GatewayClass.</p>
<p>Implementations MUST populate status on all GatewayClass resources which specify their controller name.</p></td>
</tr>
</tbody>
</table>

## .spec

Description
Spec defines the desired state of GatewayClass.

Type
`object`

Required
- `controllerName`

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
<td style="text-align: left;"><p><code>controllerName</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>ControllerName is the name of the controller that is managing Gateways of this class. The value of this field MUST be a domain prefixed path.</p>
<p>Example: "example.net/gateway-controller".</p>
<p>This field is not mutable and cannot be empty.</p>
<p>Support: Core</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>description</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Description helps describe a GatewayClass with more details.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>parametersRef</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>ParametersRef is a reference to a resource that contains the configuration parameters corresponding to the GatewayClass. This is optional if the controller does not require any additional configuration.</p>
<p>ParametersRef can reference a standard Kubernetes resource, i.e. ConfigMap, or an implementation-specific custom resource. The resource can be cluster-scoped or namespace-scoped.</p>
<p>If the referent cannot be found, refers to an unsupported kind, or when the data within that resource is malformed, the GatewayClass SHOULD be rejected with the "Accepted" status condition set to "False" and an "InvalidParameters" reason.</p>
<p>A Gateway for this GatewayClass may provide its own <code>parametersRef</code>. When both are specified, the merging behavior is implementation specific. It is generally recommended that GatewayClass provides defaults that can be overridden by a Gateway.</p>
<p>Support: Implementation-specific</p></td>
</tr>
</tbody>
</table>

## .spec.parametersRef

Description
ParametersRef is a reference to a resource that contains the configuration parameters corresponding to the GatewayClass. This is optional if the controller does not require any additional configuration.

ParametersRef can reference a standard Kubernetes resource, i.e. ConfigMap, or an implementation-specific custom resource. The resource can be cluster-scoped or namespace-scoped.

If the referent cannot be found, refers to an unsupported kind, or when the data within that resource is malformed, the GatewayClass SHOULD be rejected with the "Accepted" status condition set to "False" and an "InvalidParameters" reason.

A Gateway for this GatewayClass may provide its own `parametersRef`. When both are specified, the merging behavior is implementation specific. It is generally recommended that GatewayClass provides defaults that can be overridden by a Gateway.

Support: Implementation-specific

Type
`object`

Required
- `group`

- `kind`

- `name`

| Property | Type | Description |
|----|----|----|
| `group` | `string` | Group is the group of the referent. |
| `kind` | `string` | Kind is kind of the referent. |
| `name` | `string` | Name is the name of the referent. |
| `namespace` | `string` | Namespace is the namespace of the referent. This field is required when referring to a Namespace-scoped resource and MUST be unset when referring to a Cluster-scoped resource. |

## .status

Description
Status defines the current state of GatewayClass.

Implementations MUST populate status on all GatewayClass resources which specify their controller name.

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
<td style="text-align: left;"><p>Conditions is the current status from the controller for this GatewayClass.</p>
<p>Controllers should prefer to publish conditions using values of GatewayClassConditionType for the type of each Condition.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>conditions[]</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>Condition contains details for one aspect of the current state of this API Resource.</p></td>
</tr>
</tbody>
</table>

## .status.conditions

Description
Conditions is the current status from the controller for this GatewayClass.

Controllers should prefer to publish conditions using values of GatewayClassConditionType for the type of each Condition.

Type
`array`

## .status.conditions\[\]

Description
Condition contains details for one aspect of the current state of this API Resource.

Type
`object`

Required
- `lastTransitionTime`

- `message`

- `reason`

- `status`

- `type`

| Property | Type | Description |
|----|----|----|
| `lastTransitionTime` | `string` | lastTransitionTime is the last time the condition transitioned from one status to another. This should be when the underlying condition changed. If that is not known, then using the time when the API field changed is acceptable. |
| `message` | `string` | message is a human readable message indicating details about the transition. This may be an empty string. |
| `observedGeneration` | `integer` | observedGeneration represents the .metadata.generation that the condition was set based upon. For instance, if .metadata.generation is currently 12, but the .status.conditions\[x\].observedGeneration is 9, the condition is out of date with respect to the current state of the instance. |
| `reason` | `string` | reason contains a programmatic identifier indicating the reason for the condition’s last transition. Producers of specific condition types may define expected values and meanings for this field, and whether the values are considered a guaranteed API. The value should be a CamelCase string. This field may not be empty. |
| `status` | `string` | status of the condition, one of True, False, Unknown. |
| `type` | `string` | type of condition in CamelCase or in foo.example.com/CamelCase. |

# API endpoints

The following API endpoints are available:

- `/apis/gateway.networking.k8s.io/v1/gatewayclasses`

  - `DELETE`: delete collection of GatewayClass

  - `GET`: list objects of kind GatewayClass

  - `POST`: create a GatewayClass

- `/apis/gateway.networking.k8s.io/v1/gatewayclasses/{name}`

  - `DELETE`: delete a GatewayClass

  - `GET`: read the specified GatewayClass

  - `PATCH`: partially update the specified GatewayClass

  - `PUT`: replace the specified GatewayClass

- `/apis/gateway.networking.k8s.io/v1/gatewayclasses/{name}/status`

  - `GET`: read status of the specified GatewayClass

  - `PATCH`: partially update status of the specified GatewayClass

  - `PUT`: replace status of the specified GatewayClass

## /apis/gateway.networking.k8s.io/v1/gatewayclasses

HTTP method
`DELETE`

Description
delete collection of GatewayClass

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Status`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`GET`

Description
list objects of kind GatewayClass

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`GatewayClassList`](../objects/index.md#io-k8s-networking-gateway-v1-GatewayClassList) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`POST`

Description
create a GatewayClass

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`GatewayClass`](gatewayclass-gateway-networking-k8s-io-v1.md#gatewayclass-gateway-networking-k8s-io-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`GatewayClass`](gatewayclass-gateway-networking-k8s-io-v1.md#gatewayclass-gateway-networking-k8s-io-v1) schema |
| 201 - Created | [`GatewayClass`](gatewayclass-gateway-networking-k8s-io-v1.md#gatewayclass-gateway-networking-k8s-io-v1) schema |
| 202 - Accepted | [`GatewayClass`](gatewayclass-gateway-networking-k8s-io-v1.md#gatewayclass-gateway-networking-k8s-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/gateway.networking.k8s.io/v1/gatewayclasses/{name}

| Parameter | Type     | Description              |
|-----------|----------|--------------------------|
| `name`    | `string` | name of the GatewayClass |

Global path parameters

HTTP method
`DELETE`

Description
delete a GatewayClass

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
read the specified GatewayClass

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`GatewayClass`](gatewayclass-gateway-networking-k8s-io-v1.md#gatewayclass-gateway-networking-k8s-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PATCH`

Description
partially update the specified GatewayClass

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`GatewayClass`](gatewayclass-gateway-networking-k8s-io-v1.md#gatewayclass-gateway-networking-k8s-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PUT`

Description
replace the specified GatewayClass

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`GatewayClass`](gatewayclass-gateway-networking-k8s-io-v1.md#gatewayclass-gateway-networking-k8s-io-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`GatewayClass`](gatewayclass-gateway-networking-k8s-io-v1.md#gatewayclass-gateway-networking-k8s-io-v1) schema |
| 201 - Created | [`GatewayClass`](gatewayclass-gateway-networking-k8s-io-v1.md#gatewayclass-gateway-networking-k8s-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/gateway.networking.k8s.io/v1/gatewayclasses/{name}/status

| Parameter | Type     | Description              |
|-----------|----------|--------------------------|
| `name`    | `string` | name of the GatewayClass |

Global path parameters

HTTP method
`GET`

Description
read status of the specified GatewayClass

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`GatewayClass`](gatewayclass-gateway-networking-k8s-io-v1.md#gatewayclass-gateway-networking-k8s-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PATCH`

Description
partially update status of the specified GatewayClass

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`GatewayClass`](gatewayclass-gateway-networking-k8s-io-v1.md#gatewayclass-gateway-networking-k8s-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PUT`

Description
replace status of the specified GatewayClass

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`GatewayClass`](gatewayclass-gateway-networking-k8s-io-v1.md#gatewayclass-gateway-networking-k8s-io-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`GatewayClass`](gatewayclass-gateway-networking-k8s-io-v1.md#gatewayclass-gateway-networking-k8s-io-v1) schema |
| 201 - Created | [`GatewayClass`](gatewayclass-gateway-networking-k8s-io-v1.md#gatewayclass-gateway-networking-k8s-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses
