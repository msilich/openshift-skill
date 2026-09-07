<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Description
IPPool is the Schema for the ippools API

Type
`object`

# Specification

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ObjectMeta`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) | Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |
| `spec` | `object` | IPPoolSpec defines the desired state of IPPool |

## .spec

Description
IPPoolSpec defines the desired state of IPPool

Type
`object`

Required
- `allocations`

- `range`

| Property | Type | Description |
|----|----|----|
| `allocations` | `object` | Allocations is the set of allocated IPs for the given range. Its\` indices are a direct mapping to the IP with the same index/offset for the pool’s range. |
| `allocations{}` | `object` | IPAllocation represents metadata about the pod/container owner of a specific IP |
| `range` | `string` | Range is a RFC 4632/4291-style string that represents an IP address and prefix length in CIDR notation |

## .spec.allocations

Description
Allocations is the set of allocated IPs for the given range. Its\` indices are a direct mapping to the IP with the same index/offset for the pool’s range.

Type
`object`

## .spec.allocations{}

Description
IPAllocation represents metadata about the pod/container owner of a specific IP

Type
`object`

Required
- `id`

- `podref`

| Property | Type     | Description |
|----------|----------|-------------|
| `id`     | `string` |             |
| `ifname` | `string` |             |
| `podref` | `string` |             |

# API endpoints

The following API endpoints are available:

- `/apis/whereabouts.cni.cncf.io/v1alpha1/ippools`

  - `GET`: list objects of kind IPPool

- `/apis/whereabouts.cni.cncf.io/v1alpha1/namespaces/{namespace}/ippools`

  - `DELETE`: delete collection of IPPool

  - `GET`: list objects of kind IPPool

  - `POST`: create an IPPool

- `/apis/whereabouts.cni.cncf.io/v1alpha1/namespaces/{namespace}/ippools/{name}`

  - `DELETE`: delete an IPPool

  - `GET`: read the specified IPPool

  - `PATCH`: partially update the specified IPPool

  - `PUT`: replace the specified IPPool

## /apis/whereabouts.cni.cncf.io/v1alpha1/ippools

HTTP method
`GET`

Description
list objects of kind IPPool

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`IPPoolList`](../objects/index.md#io-cncf-cni-whereabouts-v1alpha1-IPPoolList) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/whereabouts.cni.cncf.io/v1alpha1/namespaces/{namespace}/ippools

HTTP method
`DELETE`

Description
delete collection of IPPool

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Status`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`GET`

Description
list objects of kind IPPool

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`IPPoolList`](../objects/index.md#io-cncf-cni-whereabouts-v1alpha1-IPPoolList) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`POST`

Description
create an IPPool

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`IPPool`](ippool-whereabouts-cni-cncf-io-v1alpha1.md#ippool-whereabouts-cni-cncf-io-v1alpha1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`IPPool`](ippool-whereabouts-cni-cncf-io-v1alpha1.md#ippool-whereabouts-cni-cncf-io-v1alpha1) schema |
| 201 - Created | [`IPPool`](ippool-whereabouts-cni-cncf-io-v1alpha1.md#ippool-whereabouts-cni-cncf-io-v1alpha1) schema |
| 202 - Accepted | [`IPPool`](ippool-whereabouts-cni-cncf-io-v1alpha1.md#ippool-whereabouts-cni-cncf-io-v1alpha1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/whereabouts.cni.cncf.io/v1alpha1/namespaces/{namespace}/ippools/{name}

| Parameter | Type     | Description        |
|-----------|----------|--------------------|
| `name`    | `string` | name of the IPPool |

Global path parameters

HTTP method
`DELETE`

Description
delete an IPPool

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
read the specified IPPool

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`IPPool`](ippool-whereabouts-cni-cncf-io-v1alpha1.md#ippool-whereabouts-cni-cncf-io-v1alpha1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PATCH`

Description
partially update the specified IPPool

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`IPPool`](ippool-whereabouts-cni-cncf-io-v1alpha1.md#ippool-whereabouts-cni-cncf-io-v1alpha1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PUT`

Description
replace the specified IPPool

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`IPPool`](ippool-whereabouts-cni-cncf-io-v1alpha1.md#ippool-whereabouts-cni-cncf-io-v1alpha1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`IPPool`](ippool-whereabouts-cni-cncf-io-v1alpha1.md#ippool-whereabouts-cni-cncf-io-v1alpha1) schema |
| 201 - Created | [`IPPool`](ippool-whereabouts-cni-cncf-io-v1alpha1.md#ippool-whereabouts-cni-cncf-io-v1alpha1) schema |
| 401 - Unauthorized | Empty |

HTTP responses
