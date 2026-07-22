<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Description
OAuthClient describes an OAuth client

Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).

Type
`object`

# Specification

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Property</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>accessTokenInactivityTimeoutSeconds</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p>accessTokenInactivityTimeoutSeconds overrides the default token inactivity timeout for tokens granted to this client. The value represents the maximum amount of time that can occur between consecutive uses of the token. Tokens become invalid if they are not used within this temporal window. The user will need to acquire a new token to regain access once a token times out. This value needs to be set only if the default set in configuration is not appropriate for this client. Valid values are: - 0: Tokens for this client never time out - X: Tokens time out if there is no activity for X seconds The current minimum allowed value for X is 300 (5 minutes)</p>
<p>WARNING: existing tokens' timeout will not be affected (lowered) by changing this value</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>accessTokenMaxAgeSeconds</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p>accessTokenMaxAgeSeconds overrides the default access token max age for tokens granted to this client. 0 means no expiration.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>additionalSecrets</code></p></td>
<td style="text-align: left;"><p><code>array (string)</code></p></td>
<td style="text-align: left;"><p>additionalSecrets holds other secrets that may be used to identify the client. This is useful for rotation and for service account token validation</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>apiVersion</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <a href="https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources">https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>grantMethod</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>grantMethod is a required field which determines how to handle grants for this client. Valid grant handling methods are: - auto: always approves grant requests, useful for trusted clients - prompt: prompts the end user for approval of grant requests, useful for third-party clients</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>kind</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <a href="https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds">https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>metadata</code></p></td>
<td style="text-align: left;"><p><a href="../objects/index.xml#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta"><code>ObjectMeta</code></a></p></td>
<td style="text-align: left;"><p>metadata is the standard object’s metadata. More info: <a href="https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata">https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>redirectURIs</code></p></td>
<td style="text-align: left;"><p><code>array (string)</code></p></td>
<td style="text-align: left;"><p>redirectURIs is the valid redirection URIs associated with a client</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>respondWithChallenges</code></p></td>
<td style="text-align: left;"><p><code>boolean</code></p></td>
<td style="text-align: left;"><p>respondWithChallenges indicates whether the client wants authentication needed responses made in the form of challenges instead of redirects</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>scopeRestrictions</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>scopeRestrictions describes which scopes this client can request. Each requested scope is checked against each restriction. If any restriction matches, then the scope is allowed. If no restriction matches, then the scope is denied.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>scopeRestrictions[]</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>ScopeRestriction describe one restriction on scopes. Exactly one option must be non-nil.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>secret</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>secret is the unique secret associated with a client</p></td>
</tr>
</tbody>
</table>

## .scopeRestrictions

Description
scopeRestrictions describes which scopes this client can request. Each requested scope is checked against each restriction. If any restriction matches, then the scope is allowed. If no restriction matches, then the scope is denied.

Type
`array`

## .scopeRestrictions\[\]

Description
ScopeRestriction describe one restriction on scopes. Exactly one option must be non-nil.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `clusterRole` | `object` | ClusterRoleScopeRestriction describes restrictions on cluster role scopes |
| `literals` | `array (string)` | ExactValues means the scope has to match a particular set of strings exactly |

## .scopeRestrictions\[\].clusterRole

Description
ClusterRoleScopeRestriction describes restrictions on cluster role scopes

Type
`object`

Required
- `roleNames`

- `namespaces`

- `allowEscalation`

| Property | Type | Description |
|----|----|----|
| `allowEscalation` | `boolean` | allowEscalation indicates whether you can request roles and their escalating resources |
| `namespaces` | `array (string)` | namespaces is the list of namespaces that can be referenced. \* means any of them (including \*) |
| `roleNames` | `array (string)` | roleNames is the list of cluster roles that can referenced. \* means anything |

# API endpoints

The following API endpoints are available:

- `/apis/oauth.openshift.io/v1/oauthclients`

  - `DELETE`: delete collection of OAuthClient

  - `GET`: list or watch objects of kind OAuthClient

  - `POST`: create an OAuthClient

- `/apis/oauth.openshift.io/v1/watch/oauthclients`

  - `GET`: watch individual changes to a list of OAuthClient. deprecated: use the 'watch' parameter with a list operation instead.

- `/apis/oauth.openshift.io/v1/oauthclients/{name}`

  - `DELETE`: delete an OAuthClient

  - `GET`: read the specified OAuthClient

  - `PATCH`: partially update the specified OAuthClient

  - `PUT`: replace the specified OAuthClient

- `/apis/oauth.openshift.io/v1/watch/oauthclients/{name}`

  - `GET`: watch changes to an object of kind OAuthClient. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.

## /apis/oauth.openshift.io/v1/oauthclients

HTTP method
`DELETE`

Description
delete collection of OAuthClient

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
list or watch objects of kind OAuthClient

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`OAuthClientList`](../objects/index.md#com-github-openshift-api-oauth-v1-OAuthClientList) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`POST`

Description
create an OAuthClient

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`OAuthClient`](oauthclient-oauth-openshift-io-v1.md#oauthclient-oauth-openshift-io-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`OAuthClient`](oauthclient-oauth-openshift-io-v1.md#oauthclient-oauth-openshift-io-v1) schema |
| 201 - Created | [`OAuthClient`](oauthclient-oauth-openshift-io-v1.md#oauthclient-oauth-openshift-io-v1) schema |
| 202 - Accepted | [`OAuthClient`](oauthclient-oauth-openshift-io-v1.md#oauthclient-oauth-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/oauth.openshift.io/v1/watch/oauthclients

HTTP method
`GET`

Description
watch individual changes to a list of OAuthClient. deprecated: use the 'watch' parameter with a list operation instead.

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`WatchEvent`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/oauth.openshift.io/v1/oauthclients/{name}

| Parameter | Type     | Description             |
|-----------|----------|-------------------------|
| `name`    | `string` | name of the OAuthClient |

Global path parameters

HTTP method
`DELETE`

Description
delete an OAuthClient

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
read the specified OAuthClient

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`OAuthClient`](oauthclient-oauth-openshift-io-v1.md#oauthclient-oauth-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PATCH`

Description
partially update the specified OAuthClient

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`OAuthClient`](oauthclient-oauth-openshift-io-v1.md#oauthclient-oauth-openshift-io-v1) schema |
| 201 - Created | [`OAuthClient`](oauthclient-oauth-openshift-io-v1.md#oauthclient-oauth-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PUT`

Description
replace the specified OAuthClient

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`OAuthClient`](oauthclient-oauth-openshift-io-v1.md#oauthclient-oauth-openshift-io-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`OAuthClient`](oauthclient-oauth-openshift-io-v1.md#oauthclient-oauth-openshift-io-v1) schema |
| 201 - Created | [`OAuthClient`](oauthclient-oauth-openshift-io-v1.md#oauthclient-oauth-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/oauth.openshift.io/v1/watch/oauthclients/{name}

| Parameter | Type     | Description             |
|-----------|----------|-------------------------|
| `name`    | `string` | name of the OAuthClient |

Global path parameters

HTTP method
`GET`

Description
watch changes to an object of kind OAuthClient. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`WatchEvent`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema |
| 401 - Unauthorized | Empty |

HTTP responses
