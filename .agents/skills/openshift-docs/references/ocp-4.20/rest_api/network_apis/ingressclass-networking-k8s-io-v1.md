<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Description
IngressClass represents the class of the Ingress, referenced by the Ingress Spec. The `ingressclass.kubernetes.io/is-default-class` annotation can be used to indicate that an IngressClass should be considered default. When a single IngressClass resource has this annotation set to true, new Ingress resources without a class specified will be assigned this default class.

Type
`object`

# Specification

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ObjectMeta`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) | Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |
| `spec` | `object` | IngressClassSpec provides information about the class of an Ingress. |

## .spec

Description
IngressClassSpec provides information about the class of an Ingress.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `controller` | `string` | controller refers to the name of the controller that should handle this class. This allows for different "flavors" that are controlled by the same controller. For example, you may have different parameters for the same implementing controller. This should be specified as a domain-prefixed path no more than 250 characters in length, e.g. "acme.io/ingress-controller". This field is immutable. |
| `parameters` | `object` | IngressClassParametersReference identifies an API object. This can be used to specify a cluster or namespace-scoped resource. |

## .spec.parameters

Description
IngressClassParametersReference identifies an API object. This can be used to specify a cluster or namespace-scoped resource.

Type
`object`

Required
- `kind`

- `name`

| Property | Type | Description |
|----|----|----|
| `apiGroup` | `string` | apiGroup is the group for the resource being referenced. If APIGroup is not specified, the specified Kind must be in the core API group. For any other third-party types, APIGroup is required. |
| `kind` | `string` | kind is the type of resource being referenced. |
| `name` | `string` | name is the name of resource being referenced. |
| `namespace` | `string` | namespace is the namespace of the resource being referenced. This field is required when scope is set to "Namespace" and must be unset when scope is set to "Cluster". |
| `scope` | `string` | scope represents if this refers to a cluster or namespace scoped resource. This may be set to "Cluster" (default) or "Namespace". |

# API endpoints

The following API endpoints are available:

- `/apis/networking.k8s.io/v1/ingressclasses`

  - `DELETE`: delete collection of IngressClass

  - `GET`: list or watch objects of kind IngressClass

  - `POST`: create an IngressClass

- `/apis/networking.k8s.io/v1/watch/ingressclasses`

  - `GET`: watch individual changes to a list of IngressClass. deprecated: use the 'watch' parameter with a list operation instead.

- `/apis/networking.k8s.io/v1/ingressclasses/{name}`

  - `DELETE`: delete an IngressClass

  - `GET`: read the specified IngressClass

  - `PATCH`: partially update the specified IngressClass

  - `PUT`: replace the specified IngressClass

- `/apis/networking.k8s.io/v1/watch/ingressclasses/{name}`

  - `GET`: watch changes to an object of kind IngressClass. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.

## /apis/networking.k8s.io/v1/ingressclasses

HTTP method
`DELETE`

Description
delete collection of IngressClass

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
list or watch objects of kind IngressClass

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`IngressClassList`](../objects/index.md#io-k8s-api-networking-v1-IngressClassList) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`POST`

Description
create an IngressClass

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`IngressClass`](ingressclass-networking-k8s-io-v1.md#ingressclass-networking-k8s-io-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`IngressClass`](ingressclass-networking-k8s-io-v1.md#ingressclass-networking-k8s-io-v1) schema |
| 201 - Created | [`IngressClass`](ingressclass-networking-k8s-io-v1.md#ingressclass-networking-k8s-io-v1) schema |
| 202 - Accepted | [`IngressClass`](ingressclass-networking-k8s-io-v1.md#ingressclass-networking-k8s-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/networking.k8s.io/v1/watch/ingressclasses

HTTP method
`GET`

Description
watch individual changes to a list of IngressClass. deprecated: use the 'watch' parameter with a list operation instead.

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`WatchEvent`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/networking.k8s.io/v1/ingressclasses/{name}

| Parameter | Type     | Description              |
|-----------|----------|--------------------------|
| `name`    | `string` | name of the IngressClass |

Global path parameters

HTTP method
`DELETE`

Description
delete an IngressClass

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
read the specified IngressClass

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`IngressClass`](ingressclass-networking-k8s-io-v1.md#ingressclass-networking-k8s-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PATCH`

Description
partially update the specified IngressClass

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`IngressClass`](ingressclass-networking-k8s-io-v1.md#ingressclass-networking-k8s-io-v1) schema |
| 201 - Created | [`IngressClass`](ingressclass-networking-k8s-io-v1.md#ingressclass-networking-k8s-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PUT`

Description
replace the specified IngressClass

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`IngressClass`](ingressclass-networking-k8s-io-v1.md#ingressclass-networking-k8s-io-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`IngressClass`](ingressclass-networking-k8s-io-v1.md#ingressclass-networking-k8s-io-v1) schema |
| 201 - Created | [`IngressClass`](ingressclass-networking-k8s-io-v1.md#ingressclass-networking-k8s-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/networking.k8s.io/v1/watch/ingressclasses/{name}

| Parameter | Type     | Description              |
|-----------|----------|--------------------------|
| `name`    | `string` | name of the IngressClass |

Global path parameters

HTTP method
`GET`

Description
watch changes to an object of kind IngressClass. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`WatchEvent`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema |
| 401 - Unauthorized | Empty |

HTTP responses
