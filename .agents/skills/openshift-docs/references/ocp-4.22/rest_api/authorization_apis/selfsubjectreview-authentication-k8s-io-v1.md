<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Description
SelfSubjectReview contains the user information that the kube-apiserver has about the user making this request. When using impersonation, users will receive the user info of the user being impersonated. If impersonation or request header authentication is used, any extra keys will have their case ignored and returned as lowercase.

Type
`object`

# Specification

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ObjectMeta`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) | Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |
| `status` | `object` | SelfSubjectReviewStatus is filled by the kube-apiserver and sent back to a user. |

## .status

Description
SelfSubjectReviewStatus is filled by the kube-apiserver and sent back to a user.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `userInfo` | `object` | UserInfo holds the information about the user needed to implement the user.Info interface. |

## .status.userInfo

Description
UserInfo holds the information about the user needed to implement the user.Info interface.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `extra` | `object` | Any additional information provided by the authenticator. |
| `extra{}` | `array (string)` |  |
| `groups` | `array (string)` | The names of groups this user is a part of. |
| `uid` | `string` | A unique value that identifies this user across time. If this user is deleted and another user by the same name is added, they will have different UIDs. |
| `username` | `string` | The name that uniquely identifies this user among all active users. |

## .status.userInfo.extra

Description
Any additional information provided by the authenticator.

Type
`object`

# API endpoints

The following API endpoints are available:

- `/apis/authentication.k8s.io/v1/selfsubjectreviews`

  - `POST`: create a SelfSubjectReview

## /apis/authentication.k8s.io/v1/selfsubjectreviews

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Global query parameters

HTTP method
`POST`

Description
create a SelfSubjectReview

| Parameter | Type | Description |
|----|----|----|
| `body` | [`SelfSubjectReview`](selfsubjectreview-authentication-k8s-io-v1.md#selfsubjectreview-authentication-k8s-io-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`SelfSubjectReview`](selfsubjectreview-authentication-k8s-io-v1.md#selfsubjectreview-authentication-k8s-io-v1) schema |
| 201 - Created | [`SelfSubjectReview`](selfsubjectreview-authentication-k8s-io-v1.md#selfsubjectreview-authentication-k8s-io-v1) schema |
| 202 - Accepted | [`SelfSubjectReview`](selfsubjectreview-authentication-k8s-io-v1.md#selfsubjectreview-authentication-k8s-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses
