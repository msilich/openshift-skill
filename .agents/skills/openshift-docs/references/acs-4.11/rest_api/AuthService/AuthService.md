<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

<a id="AddAuthMachineToMachineConfig_AuthService"></a>

# AddAuthMachineToMachineConfig

`POST /v1/auth/m2m`

AddAuthMachineToMachineConfig creates a new auth machine to machine config.

<a id="_description"></a>

## Description

<a id="_parameters"></a>

## Parameters

<a id="_body_parameter"></a>

### Body Parameter

| Name | Description | Required | Default | Pattern |
|----|----|----|----|----|
| body | [V1AddAuthMachineToMachineConfigRequest](../CommonObjectReference/CommonObjectReference.md#V1AddAuthMachineToMachineConfigRequest_CommonObjectReference) | X |  |  |

<a id="_return_type"></a>

## Return Type

[V1AddAuthMachineToMachineConfigResponse](../CommonObjectReference/CommonObjectReference.md#V1AddAuthMachineToMachineConfigResponse_CommonObjectReference)

<a id="_content_type"></a>

## Content Type

- application/json

<a id="_responses"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V1AddAuthMachineToMachineConfigResponse](../CommonObjectReference/CommonObjectReference.md#V1AddAuthMachineToMachineConfigResponse_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples"></a>

## Samples

<a id="DeleteAuthMachineToMachineConfig_AuthService"></a>

# DeleteAuthMachineToMachineConfig

`DELETE /v1/auth/m2m/{id}`

DeleteAuthMachineToMachineConfig deletes the specific auth machine to machine config. In case a specified auth machine to machine config does not exist is deleted, no error will be returned.

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

`Object`

<a id="_content_type_2"></a>

## Content Type

- application/json

<a id="_responses_2"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | `Object` |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_2"></a>

## Samples

<a id="ExchangeAuthMachineToMachineToken_AuthService"></a>

# ExchangeAuthMachineToMachineToken

`POST /v1/auth/m2m/exchange`

ExchangeAuthMachineToMachineToken exchanges a given identity token for a Central access token based on configured auth machine to machine configs.

<a id="_description_3"></a>

## Description

<a id="_parameters_3"></a>

## Parameters

<a id="_body_parameter_2"></a>

### Body Parameter

| Name | Description | Required | Default | Pattern |
|----|----|----|----|----|
| body | [V1ExchangeAuthMachineToMachineTokenRequest](../CommonObjectReference/CommonObjectReference.md#V1ExchangeAuthMachineToMachineTokenRequest_CommonObjectReference) | X |  |  |

<a id="_return_type_3"></a>

## Return Type

[V1ExchangeAuthMachineToMachineTokenResponse](../CommonObjectReference/CommonObjectReference.md#V1ExchangeAuthMachineToMachineTokenResponse_CommonObjectReference)

<a id="_content_type_3"></a>

## Content Type

- application/json

<a id="_responses_3"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V1ExchangeAuthMachineToMachineTokenResponse](../CommonObjectReference/CommonObjectReference.md#V1ExchangeAuthMachineToMachineTokenResponse_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_3"></a>

## Samples

<a id="GetAuthMachineToMachineConfig_AuthService"></a>

# GetAuthMachineToMachineConfig

`GET /v1/auth/m2m/{id}`

GetAuthMachineToMachineConfig retrieves the specific auth machine to machine config.

<a id="_description_4"></a>

## Description

<a id="_parameters_4"></a>

## Parameters

<a id="_path_parameters_2"></a>

### Path Parameters

| Name | Description | Required | Default | Pattern |
|------|-------------|----------|---------|---------|
| id   |             | X        | null    |         |

<a id="_return_type_4"></a>

## Return Type

[V1GetAuthMachineToMachineConfigResponse](../CommonObjectReference/CommonObjectReference.md#V1GetAuthMachineToMachineConfigResponse_CommonObjectReference)

<a id="_content_type_4"></a>

## Content Type

- application/json

<a id="_responses_4"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V1GetAuthMachineToMachineConfigResponse](../CommonObjectReference/CommonObjectReference.md#V1GetAuthMachineToMachineConfigResponse_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_4"></a>

## Samples

<a id="GetAuthStatus_AuthService"></a>

# GetAuthStatus

`GET /v1/auth/status`

GetAuthStatus returns the status for the current client.

<a id="_description_5"></a>

## Description

<a id="_parameters_5"></a>

## Parameters

<a id="_return_type_5"></a>

## Return Type

[V1AuthStatus](../CommonObjectReference/CommonObjectReference.md#V1AuthStatus_CommonObjectReference)

<a id="_content_type_5"></a>

## Content Type

- application/json

<a id="_responses_5"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V1AuthStatus](../CommonObjectReference/CommonObjectReference.md#V1AuthStatus_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_5"></a>

## Samples

<a id="ListAuthMachineToMachineConfigs_AuthService"></a>

# ListAuthMachineToMachineConfigs

`GET /v1/auth/m2m`

ListAuthMachineToMachineConfigs lists the available auth machine to machine configs.

<a id="_description_6"></a>

## Description

<a id="_parameters_6"></a>

## Parameters

<a id="_return_type_6"></a>

## Return Type

[V1ListAuthMachineToMachineConfigResponse](../CommonObjectReference/CommonObjectReference.md#V1ListAuthMachineToMachineConfigResponse_CommonObjectReference)

<a id="_content_type_6"></a>

## Content Type

- application/json

<a id="_responses_6"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V1ListAuthMachineToMachineConfigResponse](../CommonObjectReference/CommonObjectReference.md#V1ListAuthMachineToMachineConfigResponse_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_6"></a>

## Samples

<a id="UpdateAuthMachineToMachineConfig_AuthService"></a>

# UpdateAuthMachineToMachineConfig

`PUT /v1/auth/m2m/{config.id}`

UpdateAuthMachineToMachineConfig updates an existing auth machine to machine config. In case the auth machine to machine config does not exist, a new one will be created.

<a id="_description_7"></a>

## Description

<a id="_parameters_7"></a>

## Parameters

<a id="_path_parameters_3"></a>

### Path Parameters

| Name | Description | Required | Default | Pattern |
|----|----|----|----|----|
| config.id | UUID of the config. Note that when adding a machine to machine config, this field should not be set. | X | null |  |

<a id="_body_parameter_3"></a>

### Body Parameter

| Name | Description | Required | Default | Pattern |
|----|----|----|----|----|
| body | [AuthServiceUpdateAuthMachineToMachineConfigBody](../CommonObjectReference/CommonObjectReference.md#AuthServiceUpdateAuthMachineToMachineConfigBody_CommonObjectReference) | X |  |  |

<a id="_return_type_7"></a>

## Return Type

`Object`

<a id="_content_type_7"></a>

## Content Type

- application/json

<a id="_responses_7"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | `Object` |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_7"></a>

## Samples
