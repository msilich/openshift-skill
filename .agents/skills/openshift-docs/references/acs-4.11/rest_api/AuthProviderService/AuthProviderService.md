<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

<a id="DeleteAuthProvider_AuthProviderService"></a>

# DeleteAuthProvider

`DELETE /v1/authProviders/{id}`

<a id="_description"></a>

## Description

<a id="_parameters"></a>

## Parameters

<a id="_path_parameters"></a>

### Path Parameters

| Name | Description | Required | Default | Pattern |
|------|-------------|----------|---------|---------|
| id   |             | X        | null    |         |

<a id="_query_parameters"></a>

### Query Parameters

| Name  | Description | Required | Default | Pattern |
|-------|-------------|----------|---------|---------|
| force |             | \-       | null    |         |

<a id="_return_type"></a>

## Return Type

`Object`

<a id="_content_type"></a>

## Content Type

- application/json

<a id="_responses"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | `Object` |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples"></a>

## Samples

<a id="ExchangeToken_AuthProviderService"></a>

# ExchangeToken

`POST /v1/authProviders/exchangeToken`

<a id="_description_2"></a>

## Description

<a id="_parameters_2"></a>

## Parameters

<a id="_body_parameter"></a>

### Body Parameter

| Name | Description | Required | Default | Pattern |
|----|----|----|----|----|
| body | [V1ExchangeTokenRequest](../CommonObjectReference/CommonObjectReference.md#V1ExchangeTokenRequest_CommonObjectReference) | X |  |  |

<a id="_return_type_2"></a>

## Return Type

[V1ExchangeTokenResponse](../CommonObjectReference/CommonObjectReference.md#V1ExchangeTokenResponse_CommonObjectReference)

<a id="_content_type_2"></a>

## Content Type

- application/json

<a id="_responses_2"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V1ExchangeTokenResponse](../CommonObjectReference/CommonObjectReference.md#V1ExchangeTokenResponse_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_2"></a>

## Samples

<a id="GetAuthProvider_AuthProviderService"></a>

# GetAuthProvider

`GET /v1/authProviders/{id}`

<a id="_description_3"></a>

## Description

<a id="_parameters_3"></a>

## Parameters

<a id="_path_parameters_2"></a>

### Path Parameters

| Name | Description | Required | Default | Pattern |
|------|-------------|----------|---------|---------|
| id   |             | X        | null    |         |

<a id="_return_type_3"></a>

## Return Type

[StorageAuthProvider](../CommonObjectReference/CommonObjectReference.md#StorageAuthProvider_CommonObjectReference)

<a id="_content_type_3"></a>

## Content Type

- application/json

<a id="_responses_3"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [StorageAuthProvider](../CommonObjectReference/CommonObjectReference.md#StorageAuthProvider_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_3"></a>

## Samples

<a id="GetAuthProviders_AuthProviderService"></a>

# GetAuthProviders

`GET /v1/authProviders`

<a id="_description_4"></a>

## Description

<a id="_parameters_4"></a>

## Parameters

<a id="_query_parameters_2"></a>

### Query Parameters

| Name | Description | Required | Default | Pattern |
|------|-------------|----------|---------|---------|
| name |             | \-       | null    |         |
| type |             | \-       | null    |         |

<a id="_return_type_4"></a>

## Return Type

[V1GetAuthProvidersResponse](../CommonObjectReference/CommonObjectReference.md#V1GetAuthProvidersResponse_CommonObjectReference)

<a id="_content_type_4"></a>

## Content Type

- application/json

<a id="_responses_4"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V1GetAuthProvidersResponse](../CommonObjectReference/CommonObjectReference.md#V1GetAuthProvidersResponse_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_4"></a>

## Samples

<a id="GetLoginAuthProviders_AuthProviderService"></a>

# GetLoginAuthProviders

`GET /v1/login/authproviders`

<a id="_description_5"></a>

## Description

<a id="_parameters_5"></a>

## Parameters

<a id="_return_type_5"></a>

## Return Type

[V1GetLoginAuthProvidersResponse](../CommonObjectReference/CommonObjectReference.md#V1GetLoginAuthProvidersResponse_CommonObjectReference)

<a id="_content_type_5"></a>

## Content Type

- application/json

<a id="_responses_5"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V1GetLoginAuthProvidersResponse](../CommonObjectReference/CommonObjectReference.md#V1GetLoginAuthProvidersResponse_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_5"></a>

## Samples

<a id="ListAvailableProviderTypes_AuthProviderService"></a>

# ListAvailableProviderTypes

`GET /v1/availableAuthProviders`

<a id="_description_6"></a>

## Description

<a id="_parameters_6"></a>

## Parameters

<a id="_return_type_6"></a>

## Return Type

[V1AvailableProviderTypesResponse](../CommonObjectReference/CommonObjectReference.md#V1AvailableProviderTypesResponse_CommonObjectReference)

<a id="_content_type_6"></a>

## Content Type

- application/json

<a id="_responses_6"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V1AvailableProviderTypesResponse](../CommonObjectReference/CommonObjectReference.md#V1AvailableProviderTypesResponse_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_6"></a>

## Samples

<a id="PostAuthProvider_AuthProviderService"></a>

# PostAuthProvider

`POST /v1/authProviders`

<a id="_description_7"></a>

## Description

<a id="_parameters_7"></a>

## Parameters

<a id="_body_parameter_2"></a>

### Body Parameter

| Name | Description | Required | Default | Pattern |
|----|----|----|----|----|
| provider | [StorageAuthProvider](../CommonObjectReference/CommonObjectReference.md#StorageAuthProvider_CommonObjectReference) | X |  |  |

<a id="_return_type_7"></a>

## Return Type

[StorageAuthProvider](../CommonObjectReference/CommonObjectReference.md#StorageAuthProvider_CommonObjectReference)

<a id="_content_type_7"></a>

## Content Type

- application/json

<a id="_responses_7"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [StorageAuthProvider](../CommonObjectReference/CommonObjectReference.md#StorageAuthProvider_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_7"></a>

## Samples

<a id="PutAuthProvider_AuthProviderService"></a>

# PutAuthProvider

`PUT /v1/authProviders/{id}`

<a id="_description_8"></a>

## Description

<a id="_parameters_8"></a>

## Parameters

<a id="_path_parameters_3"></a>

### Path Parameters

| Name | Description | Required | Default | Pattern |
|------|-------------|----------|---------|---------|
| id   |             | X        | null    |         |

<a id="_body_parameter_3"></a>

### Body Parameter

| Name | Description | Required | Default | Pattern |
|----|----|----|----|----|
| body | [AuthProviderServicePutAuthProviderBody](../CommonObjectReference/CommonObjectReference.md#AuthProviderServicePutAuthProviderBody_CommonObjectReference) | X |  |  |

<a id="_return_type_8"></a>

## Return Type

[StorageAuthProvider](../CommonObjectReference/CommonObjectReference.md#StorageAuthProvider_CommonObjectReference)

<a id="_content_type_8"></a>

## Content Type

- application/json

<a id="_responses_8"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [StorageAuthProvider](../CommonObjectReference/CommonObjectReference.md#StorageAuthProvider_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_8"></a>

## Samples

<a id="UpdateAuthProvider_AuthProviderService"></a>

# UpdateAuthProvider

`PATCH /v1/authProviders/{id}`

<a id="_description_9"></a>

## Description

<a id="_parameters_9"></a>

## Parameters

<a id="_path_parameters_4"></a>

### Path Parameters

| Name | Description | Required | Default | Pattern |
|------|-------------|----------|---------|---------|
| id   |             | X        | null    |         |

<a id="_body_parameter_4"></a>

### Body Parameter

| Name | Description | Required | Default | Pattern |
|----|----|----|----|----|
| body | [AuthProviderServiceUpdateAuthProviderBody](../CommonObjectReference/CommonObjectReference.md#AuthProviderServiceUpdateAuthProviderBody_CommonObjectReference) | X |  |  |

<a id="_return_type_9"></a>

## Return Type

[StorageAuthProvider](../CommonObjectReference/CommonObjectReference.md#StorageAuthProvider_CommonObjectReference)

<a id="_content_type_9"></a>

## Content Type

- application/json

<a id="_responses_9"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [StorageAuthProvider](../CommonObjectReference/CommonObjectReference.md#StorageAuthProvider_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_9"></a>

## Samples
