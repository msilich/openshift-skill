<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

<a id="CancelRestoreProcess_DBService"></a>

# CancelRestoreProcess

`DELETE /v1/db/restore/{id}`

<a id="_description"></a>

## Description

<a id="_parameters"></a>

## Parameters

<a id="_path_parameters"></a>

### Path Parameters

| Name | Description | Required | Default | Pattern |
|------|-------------|----------|---------|---------|
| id   |             | X        | null    |         |

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

<a id="GetActiveRestoreProcess_DBService"></a>

# GetActiveRestoreProcess

`GET /v1/db/restore`

<a id="_description_2"></a>

## Description

<a id="_parameters_2"></a>

## Parameters

<a id="_return_type_2"></a>

## Return Type

[V1GetActiveDBRestoreProcessResponse](../CommonObjectReference/CommonObjectReference.md#V1GetActiveDBRestoreProcessResponse_CommonObjectReference)

<a id="_content_type_2"></a>

## Content Type

- application/json

<a id="_responses_2"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V1GetActiveDBRestoreProcessResponse](../CommonObjectReference/CommonObjectReference.md#V1GetActiveDBRestoreProcessResponse_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_2"></a>

## Samples

<a id="GetExportCapabilities_DBService"></a>

# GetExportCapabilities

`GET /v1/db/exportcaps`

<a id="_description_3"></a>

## Description

<a id="_parameters_3"></a>

## Parameters

<a id="_return_type_3"></a>

## Return Type

[V1GetDBExportCapabilitiesResponse](../CommonObjectReference/CommonObjectReference.md#V1GetDBExportCapabilitiesResponse_CommonObjectReference)

<a id="_content_type_3"></a>

## Content Type

- application/json

<a id="_responses_3"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V1GetDBExportCapabilitiesResponse](../CommonObjectReference/CommonObjectReference.md#V1GetDBExportCapabilitiesResponse_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_3"></a>

## Samples

<a id="InterruptRestoreProcess_DBService"></a>

# InterruptRestoreProcess

`POST /v1/db/interruptrestore/{processId}/{attemptId}`

<a id="_description_4"></a>

## Description

<a id="_parameters_4"></a>

## Parameters

<a id="_path_parameters_2"></a>

### Path Parameters

| Name      | Description | Required | Default | Pattern |
|-----------|-------------|----------|---------|---------|
| processId |             | X        | null    |         |
| attemptId |             | X        | null    |         |

<a id="_return_type_4"></a>

## Return Type

[V1InterruptDBRestoreProcessResponse](../CommonObjectReference/CommonObjectReference.md#V1InterruptDBRestoreProcessResponse_CommonObjectReference)

<a id="_content_type_4"></a>

## Content Type

- application/json

<a id="_responses_4"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V1InterruptDBRestoreProcessResponse](../CommonObjectReference/CommonObjectReference.md#V1InterruptDBRestoreProcessResponse_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_4"></a>

## Samples
