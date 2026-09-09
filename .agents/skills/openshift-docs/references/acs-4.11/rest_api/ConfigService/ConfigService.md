<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

<a id="GetConfig_ConfigService"></a>

# GetConfig

`GET /v1/config`

<a id="_description"></a>

## Description

<a id="_parameters"></a>

## Parameters

<a id="_return_type"></a>

## Return Type

[StorageConfig](../CommonObjectReference/CommonObjectReference.md#StorageConfig_CommonObjectReference)

<a id="_content_type"></a>

## Content Type

- application/json

<a id="_responses"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [StorageConfig](../CommonObjectReference/CommonObjectReference.md#StorageConfig_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples"></a>

## Samples

<a id="GetDefaultRedHatLayeredProductsRegex_ConfigService"></a>

# GetDefaultRedHatLayeredProductsRegex

`GET /v1/config/platformcomponent/rhlp/default`

GetDefaultRedHatLayeredProductsRegex returns a static string containing the default Red Hat Layered Products regex.

<a id="_description_2"></a>

## Description

<a id="_parameters_2"></a>

## Parameters

<a id="_return_type_2"></a>

## Return Type

[V1GetDefaultRedHatLayeredProductsRegexResponse](../CommonObjectReference/CommonObjectReference.md#V1GetDefaultRedHatLayeredProductsRegexResponse_CommonObjectReference)

<a id="_content_type_2"></a>

## Content Type

- application/json

<a id="_responses_2"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V1GetDefaultRedHatLayeredProductsRegexResponse](../CommonObjectReference/CommonObjectReference.md#V1GetDefaultRedHatLayeredProductsRegexResponse_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_2"></a>

## Samples

<a id="GetPlatformComponentConfig_ConfigService"></a>

# GetPlatformComponentConfig

`GET /v1/config/platformcomponent`

<a id="_description_3"></a>

## Description

<a id="_parameters_3"></a>

## Parameters

<a id="_return_type_3"></a>

## Return Type

[StoragePlatformComponentConfig](../CommonObjectReference/CommonObjectReference.md#StoragePlatformComponentConfig_CommonObjectReference)

<a id="_content_type_3"></a>

## Content Type

- application/json

<a id="_responses_3"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [StoragePlatformComponentConfig](../CommonObjectReference/CommonObjectReference.md#StoragePlatformComponentConfig_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_3"></a>

## Samples

<a id="GetPrivateConfig_ConfigService"></a>

# GetPrivateConfig

`GET /v1/config/private`

<a id="_description_4"></a>

## Description

<a id="_parameters_4"></a>

## Parameters

<a id="_return_type_4"></a>

## Return Type

[StoragePrivateConfig](../CommonObjectReference/CommonObjectReference.md#StoragePrivateConfig_CommonObjectReference)

<a id="_content_type_4"></a>

## Content Type

- application/json

<a id="_responses_4"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [StoragePrivateConfig](../CommonObjectReference/CommonObjectReference.md#StoragePrivateConfig_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_4"></a>

## Samples

<a id="GetPublicConfig_ConfigService"></a>

# GetPublicConfig

`GET /v1/config/public`

<a id="_description_5"></a>

## Description

<a id="_parameters_5"></a>

## Parameters

<a id="_return_type_5"></a>

## Return Type

[StoragePublicConfig](../CommonObjectReference/CommonObjectReference.md#StoragePublicConfig_CommonObjectReference)

<a id="_content_type_5"></a>

## Content Type

- application/json

<a id="_responses_5"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [StoragePublicConfig](../CommonObjectReference/CommonObjectReference.md#StoragePublicConfig_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_5"></a>

## Samples

<a id="GetVulnerabilityExceptionConfig_ConfigService"></a>

# GetVulnerabilityExceptionConfig

`GET /v1/config/private/exception/vulnerabilities`

<a id="_description_6"></a>

## Description

<a id="_parameters_6"></a>

## Parameters

<a id="_return_type_6"></a>

## Return Type

[V1GetVulnerabilityExceptionConfigResponse](../CommonObjectReference/CommonObjectReference.md#V1GetVulnerabilityExceptionConfigResponse_CommonObjectReference)

<a id="_content_type_6"></a>

## Content Type

- application/json

<a id="_responses_6"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V1GetVulnerabilityExceptionConfigResponse](../CommonObjectReference/CommonObjectReference.md#V1GetVulnerabilityExceptionConfigResponse_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_6"></a>

## Samples

<a id="PutConfig_ConfigService"></a>

# PutConfig

`PUT /v1/config`

<a id="_description_7"></a>

## Description

<a id="_parameters_7"></a>

## Parameters

<a id="_body_parameter"></a>

### Body Parameter

| Name | Description | Required | Default | Pattern |
|----|----|----|----|----|
| body | [V1PutConfigRequest](../CommonObjectReference/CommonObjectReference.md#V1PutConfigRequest_CommonObjectReference) | X |  |  |

<a id="_return_type_7"></a>

## Return Type

[StorageConfig](../CommonObjectReference/CommonObjectReference.md#StorageConfig_CommonObjectReference)

<a id="_content_type_7"></a>

## Content Type

- application/json

<a id="_responses_7"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [StorageConfig](../CommonObjectReference/CommonObjectReference.md#StorageConfig_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_7"></a>

## Samples

<a id="UpdatePlatformComponentConfig_ConfigService"></a>

# UpdatePlatformComponentConfig

`PUT /v1/config/platformcomponent`

<a id="_description_8"></a>

## Description

<a id="_parameters_8"></a>

## Parameters

<a id="_body_parameter_2"></a>

### Body Parameter

| Name | Description | Required | Default | Pattern |
|----|----|----|----|----|
| body | [V1PutPlatformComponentConfigRequest](../CommonObjectReference/CommonObjectReference.md#V1PutPlatformComponentConfigRequest_CommonObjectReference) | X |  |  |

<a id="_return_type_8"></a>

## Return Type

[StoragePlatformComponentConfig](../CommonObjectReference/CommonObjectReference.md#StoragePlatformComponentConfig_CommonObjectReference)

<a id="_content_type_8"></a>

## Content Type

- application/json

<a id="_responses_8"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [StoragePlatformComponentConfig](../CommonObjectReference/CommonObjectReference.md#StoragePlatformComponentConfig_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_8"></a>

## Samples

<a id="UpdateVulnerabilityExceptionConfig_ConfigService"></a>

# UpdateVulnerabilityExceptionConfig

`PUT /v1/config/private/exception/vulnerabilities`

<a id="_description_9"></a>

## Description

<a id="_parameters_9"></a>

## Parameters

<a id="_body_parameter_3"></a>

### Body Parameter

| Name | Description | Required | Default | Pattern |
|----|----|----|----|----|
| body | [V1UpdateVulnerabilityExceptionConfigRequest](../CommonObjectReference/CommonObjectReference.md#V1UpdateVulnerabilityExceptionConfigRequest_CommonObjectReference) | X |  |  |

<a id="_return_type_9"></a>

## Return Type

[V1UpdateVulnerabilityExceptionConfigResponse](../CommonObjectReference/CommonObjectReference.md#V1UpdateVulnerabilityExceptionConfigResponse_CommonObjectReference)

<a id="_content_type_9"></a>

## Content Type

- application/json

<a id="_responses_9"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V1UpdateVulnerabilityExceptionConfigResponse](../CommonObjectReference/CommonObjectReference.md#V1UpdateVulnerabilityExceptionConfigResponse_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_9"></a>

## Samples
