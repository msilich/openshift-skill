<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Description
OAuthAccessToken describes an OAuth access token. The name of a token must be prefixed with a `sha256~` string, must not contain "/" or "%" characters and must be at least 32 characters long.

The name of the token is constructed from the actual token by sha256-hashing it and using URL-safe unpadded base64-encoding (as described in RFC4648) on the hashed result.

Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).

Type
`object`

# Specification

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `authorizeToken` | `string` | authorizeToken contains the token that authorized this token |
| `clientName` | `string` | clientName references the client that created this token. |
| `expiresIn` | `integer` | expiresIn is the seconds from CreationTime before this token expires. |
| `inactivityTimeoutSeconds` | `integer` | inactivityTimeoutSeconds is the value in seconds, from the CreationTimestamp, after which this token can no longer be used. The value is automatically incremented when the token is used. |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ObjectMeta`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) | metadata is the standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |
| `redirectURI` | `string` | redirectURI is the redirection associated with the token. |
| `refreshToken` | `string` | refreshToken is the value by which this token can be renewed. Can be blank. |
| `scopes` | `array (string)` | scopes is an array of the requested scopes. |
| `userName` | `string` | userName is the user name associated with this token |
| `userUID` | `string` | userUID is the unique UID associated with this token |

# API endpoints

The following API endpoints are available:

- `/apis/oauth.openshift.io/v1/oauthaccesstokens`

  - `DELETE`: delete collection of OAuthAccessToken

  - `GET`: list or watch objects of kind OAuthAccessToken

  - `POST`: create an OAuthAccessToken

- `/apis/oauth.openshift.io/v1/watch/oauthaccesstokens`

  - `GET`: watch individual changes to a list of OAuthAccessToken. deprecated: use the 'watch' parameter with a list operation instead.

- `/apis/oauth.openshift.io/v1/oauthaccesstokens/{name}`

  - `DELETE`: delete an OAuthAccessToken

  - `GET`: read the specified OAuthAccessToken

  - `PATCH`: partially update the specified OAuthAccessToken

  - `PUT`: replace the specified OAuthAccessToken

- `/apis/oauth.openshift.io/v1/watch/oauthaccesstokens/{name}`

  - `GET`: watch changes to an object of kind OAuthAccessToken. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.

## /apis/oauth.openshift.io/v1/oauthaccesstokens

HTTP method
`DELETE`

Description
delete collection of OAuthAccessToken

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
list or watch objects of kind OAuthAccessToken

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`OAuthAccessTokenList`](../objects/index.md#com-github-openshift-api-oauth-v1-OAuthAccessTokenList) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`POST`

Description
create an OAuthAccessToken

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`OAuthAccessToken`](oauthaccesstoken-oauth-openshift-io-v1.md#oauthaccesstoken-oauth-openshift-io-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`OAuthAccessToken`](oauthaccesstoken-oauth-openshift-io-v1.md#oauthaccesstoken-oauth-openshift-io-v1) schema |
| 201 - Created | [`OAuthAccessToken`](oauthaccesstoken-oauth-openshift-io-v1.md#oauthaccesstoken-oauth-openshift-io-v1) schema |
| 202 - Accepted | [`OAuthAccessToken`](oauthaccesstoken-oauth-openshift-io-v1.md#oauthaccesstoken-oauth-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/oauth.openshift.io/v1/watch/oauthaccesstokens

HTTP method
`GET`

Description
watch individual changes to a list of OAuthAccessToken. deprecated: use the 'watch' parameter with a list operation instead.

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`WatchEvent`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/oauth.openshift.io/v1/oauthaccesstokens/{name}

| Parameter | Type     | Description                  |
|-----------|----------|------------------------------|
| `name`    | `string` | name of the OAuthAccessToken |

Global path parameters

HTTP method
`DELETE`

Description
delete an OAuthAccessToken

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |

Query parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`OAuthAccessToken`](oauthaccesstoken-oauth-openshift-io-v1.md#oauthaccesstoken-oauth-openshift-io-v1) schema |
| 202 - Accepted | [`OAuthAccessToken`](oauthaccesstoken-oauth-openshift-io-v1.md#oauthaccesstoken-oauth-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`GET`

Description
read the specified OAuthAccessToken

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`OAuthAccessToken`](oauthaccesstoken-oauth-openshift-io-v1.md#oauthaccesstoken-oauth-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PATCH`

Description
partially update the specified OAuthAccessToken

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`OAuthAccessToken`](oauthaccesstoken-oauth-openshift-io-v1.md#oauthaccesstoken-oauth-openshift-io-v1) schema |
| 201 - Created | [`OAuthAccessToken`](oauthaccesstoken-oauth-openshift-io-v1.md#oauthaccesstoken-oauth-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PUT`

Description
replace the specified OAuthAccessToken

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`OAuthAccessToken`](oauthaccesstoken-oauth-openshift-io-v1.md#oauthaccesstoken-oauth-openshift-io-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`OAuthAccessToken`](oauthaccesstoken-oauth-openshift-io-v1.md#oauthaccesstoken-oauth-openshift-io-v1) schema |
| 201 - Created | [`OAuthAccessToken`](oauthaccesstoken-oauth-openshift-io-v1.md#oauthaccesstoken-oauth-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/oauth.openshift.io/v1/watch/oauthaccesstokens/{name}

| Parameter | Type     | Description                  |
|-----------|----------|------------------------------|
| `name`    | `string` | name of the OAuthAccessToken |

Global path parameters

HTTP method
`GET`

Description
watch changes to an object of kind OAuthAccessToken. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`WatchEvent`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema |
| 401 - Unauthorized | Empty |

HTTP responses
