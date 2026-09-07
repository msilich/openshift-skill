<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Description
OverlappingRangeIPReservation is the Schema for the OverlappingRangeIPReservations API

Type
`object`

Required
- `spec`

# Specification

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ObjectMeta`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) | Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |
| `spec` | `object` | OverlappingRangeIPReservationSpec defines the desired state of OverlappingRangeIPReservation |

## .spec

Description
OverlappingRangeIPReservationSpec defines the desired state of OverlappingRangeIPReservation

Type
`object`

Required
- `podref`

| Property      | Type     | Description |
|---------------|----------|-------------|
| `containerid` | `string` |             |
| `ifname`      | `string` |             |
| `podref`      | `string` |             |

# API endpoints

The following API endpoints are available:

- `/apis/whereabouts.cni.cncf.io/v1alpha1/overlappingrangeipreservations`

  - `GET`: list objects of kind OverlappingRangeIPReservation

- `/apis/whereabouts.cni.cncf.io/v1alpha1/namespaces/{namespace}/overlappingrangeipreservations`

  - `DELETE`: delete collection of OverlappingRangeIPReservation

  - `GET`: list objects of kind OverlappingRangeIPReservation

  - `POST`: create an OverlappingRangeIPReservation

- `/apis/whereabouts.cni.cncf.io/v1alpha1/namespaces/{namespace}/overlappingrangeipreservations/{name}`

  - `DELETE`: delete an OverlappingRangeIPReservation

  - `GET`: read the specified OverlappingRangeIPReservation

  - `PATCH`: partially update the specified OverlappingRangeIPReservation

  - `PUT`: replace the specified OverlappingRangeIPReservation

## /apis/whereabouts.cni.cncf.io/v1alpha1/overlappingrangeipreservations

HTTP method
`GET`

Description
list objects of kind OverlappingRangeIPReservation

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`OverlappingRangeIPReservationList`](../objects/index.md#io-cncf-cni-whereabouts-v1alpha1-OverlappingRangeIPReservationList) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/whereabouts.cni.cncf.io/v1alpha1/namespaces/{namespace}/overlappingrangeipreservations

HTTP method
`DELETE`

Description
delete collection of OverlappingRangeIPReservation

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Status`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`GET`

Description
list objects of kind OverlappingRangeIPReservation

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`OverlappingRangeIPReservationList`](../objects/index.md#io-cncf-cni-whereabouts-v1alpha1-OverlappingRangeIPReservationList) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`POST`

Description
create an OverlappingRangeIPReservation

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`OverlappingRangeIPReservation`](overlappingrangeipreservation-whereabouts-cni-cncf-io-v1alpha1.md#overlappingrangeipreservation-whereabouts-cni-cncf-io-v1alpha1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`OverlappingRangeIPReservation`](overlappingrangeipreservation-whereabouts-cni-cncf-io-v1alpha1.md#overlappingrangeipreservation-whereabouts-cni-cncf-io-v1alpha1) schema |
| 201 - Created | [`OverlappingRangeIPReservation`](overlappingrangeipreservation-whereabouts-cni-cncf-io-v1alpha1.md#overlappingrangeipreservation-whereabouts-cni-cncf-io-v1alpha1) schema |
| 202 - Accepted | [`OverlappingRangeIPReservation`](overlappingrangeipreservation-whereabouts-cni-cncf-io-v1alpha1.md#overlappingrangeipreservation-whereabouts-cni-cncf-io-v1alpha1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/whereabouts.cni.cncf.io/v1alpha1/namespaces/{namespace}/overlappingrangeipreservations/{name}

| Parameter | Type     | Description                               |
|-----------|----------|-------------------------------------------|
| `name`    | `string` | name of the OverlappingRangeIPReservation |

Global path parameters

HTTP method
`DELETE`

Description
delete an OverlappingRangeIPReservation

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
read the specified OverlappingRangeIPReservation

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`OverlappingRangeIPReservation`](overlappingrangeipreservation-whereabouts-cni-cncf-io-v1alpha1.md#overlappingrangeipreservation-whereabouts-cni-cncf-io-v1alpha1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PATCH`

Description
partially update the specified OverlappingRangeIPReservation

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`OverlappingRangeIPReservation`](overlappingrangeipreservation-whereabouts-cni-cncf-io-v1alpha1.md#overlappingrangeipreservation-whereabouts-cni-cncf-io-v1alpha1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PUT`

Description
replace the specified OverlappingRangeIPReservation

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`OverlappingRangeIPReservation`](overlappingrangeipreservation-whereabouts-cni-cncf-io-v1alpha1.md#overlappingrangeipreservation-whereabouts-cni-cncf-io-v1alpha1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`OverlappingRangeIPReservation`](overlappingrangeipreservation-whereabouts-cni-cncf-io-v1alpha1.md#overlappingrangeipreservation-whereabouts-cni-cncf-io-v1alpha1) schema |
| 201 - Created | [`OverlappingRangeIPReservation`](overlappingrangeipreservation-whereabouts-cni-cncf-io-v1alpha1.md#overlappingrangeipreservation-whereabouts-cni-cncf-io-v1alpha1) schema |
| 401 - Unauthorized | Empty |

HTTP responses
