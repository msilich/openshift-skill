<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Description
IPAMClaim is the Schema for the IPAMClaim API

Type
`object`

# Specification

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ObjectMeta`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) | Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |
| `spec` | `object` |  |
| `status` | `object` | IPAMClaimStatus contains the observed status of the IPAMClaim. |

## .spec

Description

Type
`object`

Required
- `interface`

- `network`

| Property | Type | Description |
|----|----|----|
| `interface` | `string` | The pod interface name for which this allocation was created |
| `network` | `string` | The network name for which this persistent allocation was created |

## .status

Description
IPAMClaimStatus contains the observed status of the IPAMClaim.

Type
`object`

Required
- `ips`

| Property | Type | Description |
|----|----|----|
| `ips` | `array (string)` | The list of IP addresses (v4, v6) that were allocated for the pod interface |

# API endpoints

The following API endpoints are available:

- `/apis/k8s.cni.cncf.io/v1alpha1/ipamclaims`

  - `GET`: list objects of kind IPAMClaim

- `/apis/k8s.cni.cncf.io/v1alpha1/namespaces/{namespace}/ipamclaims`

  - `DELETE`: delete collection of IPAMClaim

  - `GET`: list objects of kind IPAMClaim

  - `POST`: create an IPAMClaim

- `/apis/k8s.cni.cncf.io/v1alpha1/namespaces/{namespace}/ipamclaims/{name}`

  - `DELETE`: delete an IPAMClaim

  - `GET`: read the specified IPAMClaim

  - `PATCH`: partially update the specified IPAMClaim

  - `PUT`: replace the specified IPAMClaim

- `/apis/k8s.cni.cncf.io/v1alpha1/namespaces/{namespace}/ipamclaims/{name}/status`

  - `GET`: read status of the specified IPAMClaim

  - `PATCH`: partially update status of the specified IPAMClaim

  - `PUT`: replace status of the specified IPAMClaim

## /apis/k8s.cni.cncf.io/v1alpha1/ipamclaims

HTTP method
`GET`

Description
list objects of kind IPAMClaim

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`IPAMClaimList`](../objects/index.md#io-cncf-cni-k8s-v1alpha1-IPAMClaimList) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/k8s.cni.cncf.io/v1alpha1/namespaces/{namespace}/ipamclaims

HTTP method
`DELETE`

Description
delete collection of IPAMClaim

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Status`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`GET`

Description
list objects of kind IPAMClaim

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`IPAMClaimList`](../objects/index.md#io-cncf-cni-k8s-v1alpha1-IPAMClaimList) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`POST`

Description
create an IPAMClaim

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`IPAMClaim`](ipamclaim-k8s-cni-cncf-io-v1alpha1.md#ipamclaim-k8s-cni-cncf-io-v1alpha1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`IPAMClaim`](ipamclaim-k8s-cni-cncf-io-v1alpha1.md#ipamclaim-k8s-cni-cncf-io-v1alpha1) schema |
| 201 - Created | [`IPAMClaim`](ipamclaim-k8s-cni-cncf-io-v1alpha1.md#ipamclaim-k8s-cni-cncf-io-v1alpha1) schema |
| 202 - Accepted | [`IPAMClaim`](ipamclaim-k8s-cni-cncf-io-v1alpha1.md#ipamclaim-k8s-cni-cncf-io-v1alpha1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/k8s.cni.cncf.io/v1alpha1/namespaces/{namespace}/ipamclaims/{name}

| Parameter | Type     | Description           |
|-----------|----------|-----------------------|
| `name`    | `string` | name of the IPAMClaim |

Global path parameters

HTTP method
`DELETE`

Description
delete an IPAMClaim

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
read the specified IPAMClaim

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`IPAMClaim`](ipamclaim-k8s-cni-cncf-io-v1alpha1.md#ipamclaim-k8s-cni-cncf-io-v1alpha1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PATCH`

Description
partially update the specified IPAMClaim

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`IPAMClaim`](ipamclaim-k8s-cni-cncf-io-v1alpha1.md#ipamclaim-k8s-cni-cncf-io-v1alpha1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PUT`

Description
replace the specified IPAMClaim

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`IPAMClaim`](ipamclaim-k8s-cni-cncf-io-v1alpha1.md#ipamclaim-k8s-cni-cncf-io-v1alpha1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`IPAMClaim`](ipamclaim-k8s-cni-cncf-io-v1alpha1.md#ipamclaim-k8s-cni-cncf-io-v1alpha1) schema |
| 201 - Created | [`IPAMClaim`](ipamclaim-k8s-cni-cncf-io-v1alpha1.md#ipamclaim-k8s-cni-cncf-io-v1alpha1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/k8s.cni.cncf.io/v1alpha1/namespaces/{namespace}/ipamclaims/{name}/status

| Parameter | Type     | Description           |
|-----------|----------|-----------------------|
| `name`    | `string` | name of the IPAMClaim |

Global path parameters

HTTP method
`GET`

Description
read status of the specified IPAMClaim

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`IPAMClaim`](ipamclaim-k8s-cni-cncf-io-v1alpha1.md#ipamclaim-k8s-cni-cncf-io-v1alpha1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PATCH`

Description
partially update status of the specified IPAMClaim

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`IPAMClaim`](ipamclaim-k8s-cni-cncf-io-v1alpha1.md#ipamclaim-k8s-cni-cncf-io-v1alpha1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PUT`

Description
replace status of the specified IPAMClaim

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`IPAMClaim`](ipamclaim-k8s-cni-cncf-io-v1alpha1.md#ipamclaim-k8s-cni-cncf-io-v1alpha1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`IPAMClaim`](ipamclaim-k8s-cni-cncf-io-v1alpha1.md#ipamclaim-k8s-cni-cncf-io-v1alpha1) schema |
| 201 - Created | [`IPAMClaim`](ipamclaim-k8s-cni-cncf-io-v1alpha1.md#ipamclaim-k8s-cni-cncf-io-v1alpha1) schema |
| 401 - Unauthorized | Empty |

HTTP responses
