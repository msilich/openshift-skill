<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Description
UserOAuthAccessToken is a virtual resource to mirror OAuthAccessTokens to the user the access token was issued for

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

- `/apis/oauth.openshift.io/v1/useroauthaccesstokens`

  - `GET`: list or watch objects of kind UserOAuthAccessToken

- `/apis/oauth.openshift.io/v1/watch/useroauthaccesstokens`

  - `GET`: watch individual changes to a list of UserOAuthAccessToken. deprecated: use the 'watch' parameter with a list operation instead.

- `/apis/oauth.openshift.io/v1/useroauthaccesstokens/{name}`

  - `DELETE`: delete an UserOAuthAccessToken

  - `GET`: read the specified UserOAuthAccessToken

- `/apis/oauth.openshift.io/v1/watch/useroauthaccesstokens/{name}`

  - `GET`: watch changes to an object of kind UserOAuthAccessToken. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.

## /apis/oauth.openshift.io/v1/useroauthaccesstokens

HTTP method
`GET`

Description
list or watch objects of kind UserOAuthAccessToken

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`UserOAuthAccessTokenList`](../objects/index.md#com-github-openshift-api-oauth-v1-UserOAuthAccessTokenList) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/oauth.openshift.io/v1/watch/useroauthaccesstokens

HTTP method
`GET`

Description
watch individual changes to a list of UserOAuthAccessToken. deprecated: use the 'watch' parameter with a list operation instead.

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`WatchEvent`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/oauth.openshift.io/v1/useroauthaccesstokens/{name}

| Parameter | Type     | Description                      |
|-----------|----------|----------------------------------|
| `name`    | `string` | name of the UserOAuthAccessToken |

Global path parameters

HTTP method
`DELETE`

Description
delete an UserOAuthAccessToken

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
read the specified UserOAuthAccessToken

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`UserOAuthAccessToken`](useroauthaccesstoken-oauth-openshift-io-v1.md#useroauthaccesstoken-oauth-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/oauth.openshift.io/v1/watch/useroauthaccesstokens/{name}

| Parameter | Type     | Description                      |
|-----------|----------|----------------------------------|
| `name`    | `string` | name of the UserOAuthAccessToken |

Global path parameters

HTTP method
`GET`

Description
watch changes to an object of kind UserOAuthAccessToken. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`WatchEvent`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema |
| 401 - Unauthorized | Empty |

HTTP responses
