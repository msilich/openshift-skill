<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

<a id="GenerateToken_APITokenService"></a>

# GenerateToken

`POST /v1/apitokens/generate`

GenerateToken generates API token for a given user and role.

<a id="_description"></a>

## Description

<a id="_parameters"></a>

## Parameters

<a id="_body_parameter"></a>

### Body Parameter

| Name | Description | Required | Default | Pattern |
|----|----|----|----|----|
| body | [V1GenerateTokenRequest](../CommonObjectReference/CommonObjectReference.md#V1GenerateTokenRequest_CommonObjectReference) | X |  |  |

<a id="_return_type"></a>

## Return Type

[V1GenerateTokenResponse](../CommonObjectReference/CommonObjectReference.md#V1GenerateTokenResponse_CommonObjectReference)

<a id="_content_type"></a>

## Content Type

- application/json

<a id="_responses"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V1GenerateTokenResponse](../CommonObjectReference/CommonObjectReference.md#V1GenerateTokenResponse_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples"></a>

## Samples

<a id="GetAPIToken_APITokenService"></a>

# GetAPIToken

`GET /v1/apitokens/{id}`

GetAPIToken returns API token metadata for a given id.

<a id="_description_2"></a>

## Description

<a id="_parameters_2"></a>

## Parameters

<a id="_path_parameters"></a>

### Path Parameters

| Name | Description | Required | Default | Pattern |
|------|-------------|----------|---------|---------|
| id   |             | X        | null    |         |

<a id="_return_type_2"></a>

## Return Type

[StorageTokenMetadata](../CommonObjectReference/CommonObjectReference.md#StorageTokenMetadata_CommonObjectReference)

<a id="_content_type_2"></a>

## Content Type

- application/json

<a id="_responses_2"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [StorageTokenMetadata](../CommonObjectReference/CommonObjectReference.md#StorageTokenMetadata_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_2"></a>

## Samples

<a id="GetAPITokens_APITokenService"></a>

# GetAPITokens

`GET /v1/apitokens`

GetAPITokens returns all the API tokens.

<a id="_description_3"></a>

## Description

<a id="_parameters_3"></a>

## Parameters

<a id="_query_parameters"></a>

### Query Parameters

| Name    | Description | Required | Default | Pattern |
|---------|-------------|----------|---------|---------|
| revoked |             | \-       | null    |         |

<a id="_return_type_3"></a>

## Return Type

[V1GetAPITokensResponse](../CommonObjectReference/CommonObjectReference.md#V1GetAPITokensResponse_CommonObjectReference)

<a id="_content_type_3"></a>

## Content Type

- application/json

<a id="_responses_3"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V1GetAPITokensResponse](../CommonObjectReference/CommonObjectReference.md#V1GetAPITokensResponse_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_3"></a>

## Samples

<a id="ListAllowedTokenRoles_APITokenService"></a>

# ListAllowedTokenRoles

`GET /v1/apitokens/generate/allowed-roles`

GetAllowedTokenRoles return roles that user is allowed to request for API token.

<a id="_description_4"></a>

## Description

<a id="_parameters_4"></a>

## Parameters

<a id="_return_type_4"></a>

## Return Type

[V1ListAllowedTokenRolesResponse](../CommonObjectReference/CommonObjectReference.md#V1ListAllowedTokenRolesResponse_CommonObjectReference)

<a id="_content_type_4"></a>

## Content Type

- application/json

<a id="_responses_4"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V1ListAllowedTokenRolesResponse](../CommonObjectReference/CommonObjectReference.md#V1ListAllowedTokenRolesResponse_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_4"></a>

## Samples

<a id="RevokeToken_APITokenService"></a>

# RevokeToken

`PATCH /v1/apitokens/revoke/{id}`

RevokeToken removes the API token for a given id.

<a id="_description_5"></a>

## Description

<a id="_parameters_5"></a>

## Parameters

<a id="_path_parameters_2"></a>

### Path Parameters

| Name | Description | Required | Default | Pattern |
|------|-------------|----------|---------|---------|
| id   |             | X        | null    |         |

<a id="_return_type_5"></a>

## Return Type

`Object`

<a id="_content_type_5"></a>

## Content Type

- application/json

<a id="_responses_5"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | `Object` |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_5"></a>

## Samples
