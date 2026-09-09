<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

<a id="GetLogLevel_DebugService"></a>

# GetLogLevel

`GET /v1/debug/loglevel`

Get the current logging level for StackRox services.

<a id="_description"></a>

## Description

<a id="_parameters"></a>

## Parameters

<a id="_query_parameters"></a>

### Query Parameters

| Name    | Description | Required | Default | Pattern |
|---------|-------------|----------|---------|---------|
| modules | `String`    | \-       | null    |         |

<a id="_return_type"></a>

## Return Type

[V1LogLevelResponse](../CommonObjectReference/CommonObjectReference.md#V1LogLevelResponse_CommonObjectReference)

<a id="_content_type"></a>

## Content Type

- application/json

<a id="_responses"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V1LogLevelResponse](../CommonObjectReference/CommonObjectReference.md#V1LogLevelResponse_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples"></a>

## Samples

<a id="ResetDBStats_DebugService"></a>

# ResetDBStats

`POST /v1/debug/db/stats/reset`

Reset database debugging statistics.

<a id="_description_2"></a>

## Description

<a id="_parameters_2"></a>

## Parameters

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

<a id="SetLogLevel_DebugService"></a>

# SetLogLevel

`PATCH /v1/debug/loglevel`

Set logging level for StackRox services.

<a id="_description_3"></a>

## Description

<a id="_parameters_3"></a>

## Parameters

<a id="_body_parameter"></a>

### Body Parameter

| Name | Description | Required | Default | Pattern |
|----|----|----|----|----|
| body | [V1LogLevelRequest](../CommonObjectReference/CommonObjectReference.md#V1LogLevelRequest_CommonObjectReference) | X |  |  |

<a id="_return_type_3"></a>

## Return Type

`Object`

<a id="_content_type_3"></a>

## Content Type

- application/json

<a id="_responses_3"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | `Object` |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_3"></a>

## Samples

<a id="StreamAuthzTraces_DebugService"></a>

# StreamAuthzTraces

`GET /v1/debug/authz/trace`

Stream authorization traces for all incoming requests.

<a id="_description_4"></a>

## Description

<a id="_parameters_4"></a>

## Parameters

<a id="_return_type_4"></a>

## Return Type

Stream result of v1AuthorizationTraceResponse.

<a id="_content_type_4"></a>

## Content Type

- application/json

<a id="_responses_4"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response.(streaming responses) | Stream result of v1AuthorizationTraceResponse. |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_4"></a>

## Samples
