<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Description
NodeSlicePool is the Schema for the nodesliceippools API

Type
`object`

# Specification

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ObjectMeta`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) | Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |
| `spec` | `object` | NodeSlicePoolSpec defines the desired state of NodeSlicePool |
| `status` | `object` | NodeSlicePoolStatus defines the desired state of NodeSlicePool |

## .spec

Description
NodeSlicePoolSpec defines the desired state of NodeSlicePool

Type
`object`

Required
- `range`

- `sliceSize`

| Property | Type | Description |
|----|----|----|
| `range` | `string` | Range is a RFC 4632/4291-style string that represents an IP address and prefix length in CIDR notation this refers to the entire range where the node is allocated a subset |
| `sliceSize` | `string` | SliceSize is the size of subnets or slices of the range that each node will be assigned |

## .status

Description
NodeSlicePoolStatus defines the desired state of NodeSlicePool

Type
`object`

Required
- `allocations`

| Property | Type | Description |
|----|----|----|
| `allocations` | `array` | Allocations holds the allocations of nodes to slices |
| `allocations[]` | `object` |  |

## .status.allocations

Description
Allocations holds the allocations of nodes to slices

Type
`array`

## .status.allocations\[\]

Description

Type
`object`

Required
- `nodeName`

- `sliceRange`

| Property | Type | Description |
|----|----|----|
| `nodeName` | `string` | NodeName is the name of the node assigned to this slice, empty node name is an available slice for assignment |
| `sliceRange` | `string` | SliceRange is the subnet of this slice |

# API endpoints

The following API endpoints are available:

- `/apis/whereabouts.cni.cncf.io/v1alpha1/nodeslicepools`

  - `GET`: list objects of kind NodeSlicePool

- `/apis/whereabouts.cni.cncf.io/v1alpha1/namespaces/{namespace}/nodeslicepools`

  - `DELETE`: delete collection of NodeSlicePool

  - `GET`: list objects of kind NodeSlicePool

  - `POST`: create a NodeSlicePool

- `/apis/whereabouts.cni.cncf.io/v1alpha1/namespaces/{namespace}/nodeslicepools/{name}`

  - `DELETE`: delete a NodeSlicePool

  - `GET`: read the specified NodeSlicePool

  - `PATCH`: partially update the specified NodeSlicePool

  - `PUT`: replace the specified NodeSlicePool

## /apis/whereabouts.cni.cncf.io/v1alpha1/nodeslicepools

HTTP method
`GET`

Description
list objects of kind NodeSlicePool

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`NodeSlicePoolList`](../objects/index.md#io-cncf-cni-whereabouts-v1alpha1-NodeSlicePoolList) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/whereabouts.cni.cncf.io/v1alpha1/namespaces/{namespace}/nodeslicepools

HTTP method
`DELETE`

Description
delete collection of NodeSlicePool

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Status`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`GET`

Description
list objects of kind NodeSlicePool

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`NodeSlicePoolList`](../objects/index.md#io-cncf-cni-whereabouts-v1alpha1-NodeSlicePoolList) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`POST`

Description
create a NodeSlicePool

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`NodeSlicePool`](nodeslicepool-whereabouts-cni-cncf-io-v1alpha1.md#nodeslicepool-whereabouts-cni-cncf-io-v1alpha1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`NodeSlicePool`](nodeslicepool-whereabouts-cni-cncf-io-v1alpha1.md#nodeslicepool-whereabouts-cni-cncf-io-v1alpha1) schema |
| 201 - Created | [`NodeSlicePool`](nodeslicepool-whereabouts-cni-cncf-io-v1alpha1.md#nodeslicepool-whereabouts-cni-cncf-io-v1alpha1) schema |
| 202 - Accepted | [`NodeSlicePool`](nodeslicepool-whereabouts-cni-cncf-io-v1alpha1.md#nodeslicepool-whereabouts-cni-cncf-io-v1alpha1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/whereabouts.cni.cncf.io/v1alpha1/namespaces/{namespace}/nodeslicepools/{name}

| Parameter | Type     | Description               |
|-----------|----------|---------------------------|
| `name`    | `string` | name of the NodeSlicePool |

Global path parameters

HTTP method
`DELETE`

Description
delete a NodeSlicePool

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
read the specified NodeSlicePool

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`NodeSlicePool`](nodeslicepool-whereabouts-cni-cncf-io-v1alpha1.md#nodeslicepool-whereabouts-cni-cncf-io-v1alpha1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PATCH`

Description
partially update the specified NodeSlicePool

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`NodeSlicePool`](nodeslicepool-whereabouts-cni-cncf-io-v1alpha1.md#nodeslicepool-whereabouts-cni-cncf-io-v1alpha1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PUT`

Description
replace the specified NodeSlicePool

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`NodeSlicePool`](nodeslicepool-whereabouts-cni-cncf-io-v1alpha1.md#nodeslicepool-whereabouts-cni-cncf-io-v1alpha1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`NodeSlicePool`](nodeslicepool-whereabouts-cni-cncf-io-v1alpha1.md#nodeslicepool-whereabouts-cni-cncf-io-v1alpha1) schema |
| 201 - Created | [`NodeSlicePool`](nodeslicepool-whereabouts-cni-cncf-io-v1alpha1.md#nodeslicepool-whereabouts-cni-cncf-io-v1alpha1) schema |
| 401 - Unauthorized | Empty |

HTTP responses
