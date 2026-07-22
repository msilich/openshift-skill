<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Description
UserIdentityMapping maps a user to an identity

Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).

Type
`object`

# Specification

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `identity` | [`ObjectReference`](../objects/index.md#io-k8s-api-core-v1-ObjectReference) | identity is a reference to an identity |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ObjectMeta`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) | metadata is the standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |
| `user` | [`ObjectReference`](../objects/index.md#io-k8s-api-core-v1-ObjectReference) | user is a reference to a user |

# API endpoints

The following API endpoints are available:

- `/apis/user.openshift.io/v1/useridentitymappings`

  - `POST`: create an UserIdentityMapping

- `/apis/user.openshift.io/v1/useridentitymappings/{name}`

  - `DELETE`: delete an UserIdentityMapping

  - `GET`: read the specified UserIdentityMapping

  - `PATCH`: partially update the specified UserIdentityMapping

  - `PUT`: replace the specified UserIdentityMapping

## /apis/user.openshift.io/v1/useridentitymappings

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Global query parameters

HTTP method
`POST`

Description
create an UserIdentityMapping

| Parameter | Type | Description |
|----|----|----|
| `body` | [`UserIdentityMapping`](useridentitymapping-user-openshift-io-v1.md#useridentitymapping-user-openshift-io-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`UserIdentityMapping`](useridentitymapping-user-openshift-io-v1.md#useridentitymapping-user-openshift-io-v1) schema |
| 201 - Created | [`UserIdentityMapping`](useridentitymapping-user-openshift-io-v1.md#useridentitymapping-user-openshift-io-v1) schema |
| 202 - Accepted | [`UserIdentityMapping`](useridentitymapping-user-openshift-io-v1.md#useridentitymapping-user-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/user.openshift.io/v1/useridentitymappings/{name}

| Parameter | Type     | Description                     |
|-----------|----------|---------------------------------|
| `name`    | `string` | name of the UserIdentityMapping |

Global path parameters

HTTP method
`DELETE`

Description
delete an UserIdentityMapping

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
read the specified UserIdentityMapping

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`UserIdentityMapping`](useridentitymapping-user-openshift-io-v1.md#useridentitymapping-user-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PATCH`

Description
partially update the specified UserIdentityMapping

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`UserIdentityMapping`](useridentitymapping-user-openshift-io-v1.md#useridentitymapping-user-openshift-io-v1) schema |
| 201 - Created | [`UserIdentityMapping`](useridentitymapping-user-openshift-io-v1.md#useridentitymapping-user-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PUT`

Description
replace the specified UserIdentityMapping

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`UserIdentityMapping`](useridentitymapping-user-openshift-io-v1.md#useridentitymapping-user-openshift-io-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`UserIdentityMapping`](useridentitymapping-user-openshift-io-v1.md#useridentitymapping-user-openshift-io-v1) schema |
| 201 - Created | [`UserIdentityMapping`](useridentitymapping-user-openshift-io-v1.md#useridentitymapping-user-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses
