<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Description
BMCEventSubscription is the Schema for the fast eventing API

Type
`object`

# Specification

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ObjectMeta`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) | Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |
| `spec` | `object` |  |
| `status` | `object` |  |

## .spec

Description

Type
`object`

| Property | Type | Description |
|----|----|----|
| `context` | `string` | Arbitrary user-provided context for the event |
| `destination` | `string` | A webhook URL to send events to |
| `hostName` | `string` | A reference to a BareMetalHost |
| `httpHeadersRef` | `object` | A secret containing HTTP headers which should be passed along to the Destination when making a request |

## .spec.httpHeadersRef

Description
A secret containing HTTP headers which should be passed along to the Destination when making a request

Type
`object`

| Property | Type | Description |
|----|----|----|
| `name` | `string` | name is unique within a namespace to reference a secret resource. |
| `namespace` | `string` | namespace defines the space within which the secret name must be unique. |

## .status

Description

Type
`object`

| Property         | Type     | Description |
|------------------|----------|-------------|
| `error`          | `string` |             |
| `subscriptionID` | `string` |             |

# API endpoints

The following API endpoints are available:

- `/apis/metal3.io/v1alpha1/bmceventsubscriptions`

  - `GET`: list objects of kind BMCEventSubscription

- `/apis/metal3.io/v1alpha1/namespaces/{namespace}/bmceventsubscriptions`

  - `DELETE`: delete collection of BMCEventSubscription

  - `GET`: list objects of kind BMCEventSubscription

  - `POST`: create a BMCEventSubscription

- `/apis/metal3.io/v1alpha1/namespaces/{namespace}/bmceventsubscriptions/{name}`

  - `DELETE`: delete a BMCEventSubscription

  - `GET`: read the specified BMCEventSubscription

  - `PATCH`: partially update the specified BMCEventSubscription

  - `PUT`: replace the specified BMCEventSubscription

- `/apis/metal3.io/v1alpha1/namespaces/{namespace}/bmceventsubscriptions/{name}/status`

  - `GET`: read status of the specified BMCEventSubscription

  - `PATCH`: partially update status of the specified BMCEventSubscription

  - `PUT`: replace status of the specified BMCEventSubscription

## /apis/metal3.io/v1alpha1/bmceventsubscriptions

HTTP method
`GET`

Description
list objects of kind BMCEventSubscription

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`BMCEventSubscriptionList`](../objects/index.md#io-metal3-v1alpha1-BMCEventSubscriptionList) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/metal3.io/v1alpha1/namespaces/{namespace}/bmceventsubscriptions

HTTP method
`DELETE`

Description
delete collection of BMCEventSubscription

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Status`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`GET`

Description
list objects of kind BMCEventSubscription

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`BMCEventSubscriptionList`](../objects/index.md#io-metal3-v1alpha1-BMCEventSubscriptionList) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`POST`

Description
create a BMCEventSubscription

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`BMCEventSubscription`](bmceventsubscription-metal3-io-v1alpha1.md#bmceventsubscription-metal3-io-v1alpha1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`BMCEventSubscription`](bmceventsubscription-metal3-io-v1alpha1.md#bmceventsubscription-metal3-io-v1alpha1) schema |
| 201 - Created | [`BMCEventSubscription`](bmceventsubscription-metal3-io-v1alpha1.md#bmceventsubscription-metal3-io-v1alpha1) schema |
| 202 - Accepted | [`BMCEventSubscription`](bmceventsubscription-metal3-io-v1alpha1.md#bmceventsubscription-metal3-io-v1alpha1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/metal3.io/v1alpha1/namespaces/{namespace}/bmceventsubscriptions/{name}

| Parameter | Type     | Description                      |
|-----------|----------|----------------------------------|
| `name`    | `string` | name of the BMCEventSubscription |

Global path parameters

HTTP method
`DELETE`

Description
delete a BMCEventSubscription

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
read the specified BMCEventSubscription

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`BMCEventSubscription`](bmceventsubscription-metal3-io-v1alpha1.md#bmceventsubscription-metal3-io-v1alpha1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PATCH`

Description
partially update the specified BMCEventSubscription

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`BMCEventSubscription`](bmceventsubscription-metal3-io-v1alpha1.md#bmceventsubscription-metal3-io-v1alpha1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PUT`

Description
replace the specified BMCEventSubscription

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`BMCEventSubscription`](bmceventsubscription-metal3-io-v1alpha1.md#bmceventsubscription-metal3-io-v1alpha1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`BMCEventSubscription`](bmceventsubscription-metal3-io-v1alpha1.md#bmceventsubscription-metal3-io-v1alpha1) schema |
| 201 - Created | [`BMCEventSubscription`](bmceventsubscription-metal3-io-v1alpha1.md#bmceventsubscription-metal3-io-v1alpha1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/metal3.io/v1alpha1/namespaces/{namespace}/bmceventsubscriptions/{name}/status

| Parameter | Type     | Description                      |
|-----------|----------|----------------------------------|
| `name`    | `string` | name of the BMCEventSubscription |

Global path parameters

HTTP method
`GET`

Description
read status of the specified BMCEventSubscription

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`BMCEventSubscription`](bmceventsubscription-metal3-io-v1alpha1.md#bmceventsubscription-metal3-io-v1alpha1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PATCH`

Description
partially update status of the specified BMCEventSubscription

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`BMCEventSubscription`](bmceventsubscription-metal3-io-v1alpha1.md#bmceventsubscription-metal3-io-v1alpha1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PUT`

Description
replace status of the specified BMCEventSubscription

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`BMCEventSubscription`](bmceventsubscription-metal3-io-v1alpha1.md#bmceventsubscription-metal3-io-v1alpha1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`BMCEventSubscription`](bmceventsubscription-metal3-io-v1alpha1.md#bmceventsubscription-metal3-io-v1alpha1) schema |
| 201 - Created | [`BMCEventSubscription`](bmceventsubscription-metal3-io-v1alpha1.md#bmceventsubscription-metal3-io-v1alpha1) schema |
| 401 - Unauthorized | Empty |

HTTP responses
