<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

<a id="ConfigureTelemetry_TelemetryService"></a>

# ConfigureTelemetry

`PUT /v1/telemetry/configure`

<a id="_description"></a>

## Description

<a id="_parameters"></a>

## Parameters

<a id="_body_parameter"></a>

### Body Parameter

| Name | Description | Required | Default | Pattern |
|----|----|----|----|----|
| body | [V1ConfigureTelemetryRequest](../CommonObjectReference/CommonObjectReference.md#V1ConfigureTelemetryRequest_CommonObjectReference) | X |  |  |

<a id="_return_type"></a>

## Return Type

[StorageTelemetryConfiguration](../CommonObjectReference/CommonObjectReference.md#StorageTelemetryConfiguration_CommonObjectReference)

<a id="_content_type"></a>

## Content Type

- application/json

<a id="_responses"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [StorageTelemetryConfiguration](../CommonObjectReference/CommonObjectReference.md#StorageTelemetryConfiguration_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples"></a>

## Samples

<a id="GetConfig_TelemetryService"></a>

# GetConfig

`GET /v1/telemetry/config`

<a id="_description_2"></a>

## Description

<a id="_parameters_2"></a>

## Parameters

<a id="_return_type_2"></a>

## Return Type

[CentralTelemetryConfig](../CommonObjectReference/CommonObjectReference.md#CentralTelemetryConfig_CommonObjectReference)

<a id="_content_type_2"></a>

## Content Type

- application/json

<a id="_responses_2"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [CentralTelemetryConfig](../CommonObjectReference/CommonObjectReference.md#CentralTelemetryConfig_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_2"></a>

## Samples

<a id="GetTelemetryConfiguration_TelemetryService"></a>

# GetTelemetryConfiguration

`GET /v1/telemetry/configure`

<a id="_description_3"></a>

## Description

<a id="_parameters_3"></a>

## Parameters

<a id="_return_type_3"></a>

## Return Type

[StorageTelemetryConfiguration](../CommonObjectReference/CommonObjectReference.md#StorageTelemetryConfiguration_CommonObjectReference)

<a id="_content_type_3"></a>

## Content Type

- application/json

<a id="_responses_3"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [StorageTelemetryConfiguration](../CommonObjectReference/CommonObjectReference.md#StorageTelemetryConfiguration_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_3"></a>

## Samples

<a id="PostConfigReload_TelemetryService"></a>

# PostConfigReload

`POST /v1/telemetry/config/reload`

<a id="_description_4"></a>

## Description

<a id="_parameters_4"></a>

## Parameters

<a id="_return_type_4"></a>

## Return Type

`Object`

<a id="_content_type_4"></a>

## Content Type

- application/json

<a id="_responses_4"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | `Object` |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_4"></a>

## Samples
