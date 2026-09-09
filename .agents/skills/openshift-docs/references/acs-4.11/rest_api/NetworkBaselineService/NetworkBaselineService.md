<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

<a id="GetNetworkBaseline_NetworkBaselineService"></a>

# GetNetworkBaseline

`GET /v1/networkbaseline/{id}`

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

[StorageNetworkBaseline](../CommonObjectReference/CommonObjectReference.md#StorageNetworkBaseline_CommonObjectReference)

<a id="_content_type"></a>

## Content Type

- application/json

<a id="_responses"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [StorageNetworkBaseline](../CommonObjectReference/CommonObjectReference.md#StorageNetworkBaseline_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples"></a>

## Samples

<a id="GetNetworkBaselineStatusForExternalFlows_NetworkBaselineService"></a>

# GetNetworkBaselineStatusForExternalFlows

`GET /v1/networkbaseline/{deploymentId}/status/external`

<a id="_description_2"></a>

## Description

<a id="_parameters_2"></a>

## Parameters

<a id="_path_parameters_2"></a>

### Path Parameters

| Name         | Description | Required | Default | Pattern |
|--------------|-------------|----------|---------|---------|
| deploymentId |             | X        | null    |         |

<a id="_query_parameters"></a>

### Query Parameters

| Name | Description | Required | Default | Pattern |
|----|----|----|----|----|
| query |  | \- | null |  |
| since |  | \- | null |  |
| pagination.limit |  | \- | null |  |
| pagination.offset |  | \- | null |  |
| pagination.sortOption.field |  | \- | null |  |
| pagination.sortOption.reversed |  | \- | null |  |
| pagination.sortOption.aggregateBy.aggrFunc |  | \- | UNSET |  |
| pagination.sortOption.aggregateBy.distinct |  | \- | null |  |

<a id="_return_type_2"></a>

## Return Type

[V1NetworkBaselineExternalStatusResponse](../CommonObjectReference/CommonObjectReference.md#V1NetworkBaselineExternalStatusResponse_CommonObjectReference)

<a id="_content_type_2"></a>

## Content Type

- application/json

<a id="_responses_2"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V1NetworkBaselineExternalStatusResponse](../CommonObjectReference/CommonObjectReference.md#V1NetworkBaselineExternalStatusResponse_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_2"></a>

## Samples

<a id="GetNetworkBaselineStatusForFlows_NetworkBaselineService"></a>

# GetNetworkBaselineStatusForFlows

`POST /v1/networkbaseline/{deploymentId}/status`

<a id="_description_3"></a>

## Description

<a id="_parameters_3"></a>

## Parameters

<a id="_path_parameters_3"></a>

### Path Parameters

| Name         | Description | Required | Default | Pattern |
|--------------|-------------|----------|---------|---------|
| deploymentId |             | X        | null    |         |

<a id="_body_parameter"></a>

### Body Parameter

| Name | Description | Required | Default | Pattern |
|----|----|----|----|----|
| body | [NetworkBaselineServiceGetNetworkBaselineStatusForFlowsBody](../CommonObjectReference/CommonObjectReference.md#NetworkBaselineServiceGetNetworkBaselineStatusForFlowsBody_CommonObjectReference) | X |  |  |

<a id="_return_type_3"></a>

## Return Type

[V1NetworkBaselineStatusResponse](../CommonObjectReference/CommonObjectReference.md#V1NetworkBaselineStatusResponse_CommonObjectReference)

<a id="_content_type_3"></a>

## Content Type

- application/json

<a id="_responses_3"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V1NetworkBaselineStatusResponse](../CommonObjectReference/CommonObjectReference.md#V1NetworkBaselineStatusResponse_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_3"></a>

## Samples

<a id="LockNetworkBaseline_NetworkBaselineService"></a>

# LockNetworkBaseline

`PATCH /v1/networkbaseline/{id}/lock`

<a id="_description_4"></a>

## Description

<a id="_parameters_4"></a>

## Parameters

<a id="_path_parameters_4"></a>

### Path Parameters

| Name | Description | Required | Default | Pattern |
|------|-------------|----------|---------|---------|
| id   |             | X        | null    |         |

<a id="_body_parameter_2"></a>

### Body Parameter

| Name | Description | Required | Default | Pattern |
|------|-------------|----------|---------|---------|
| body | `object`    | X        |         |         |

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

<a id="ModifyBaselineStatusForPeers_NetworkBaselineService"></a>

# ModifyBaselineStatusForPeers

`PATCH /v1/networkbaseline/{deploymentId}/peers`

<a id="_description_5"></a>

## Description

<a id="_parameters_5"></a>

## Parameters

<a id="_path_parameters_5"></a>

### Path Parameters

| Name         | Description | Required | Default | Pattern |
|--------------|-------------|----------|---------|---------|
| deploymentId |             | X        | null    |         |

<a id="_body_parameter_3"></a>

### Body Parameter

| Name | Description | Required | Default | Pattern |
|----|----|----|----|----|
| body | [NetworkBaselineServiceModifyBaselineStatusForPeersBody](../CommonObjectReference/CommonObjectReference.md#NetworkBaselineServiceModifyBaselineStatusForPeersBody_CommonObjectReference) | X |  |  |

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

<a id="UnlockNetworkBaseline_NetworkBaselineService"></a>

# UnlockNetworkBaseline

`PATCH /v1/networkbaseline/{id}/unlock`

<a id="_description_6"></a>

## Description

<a id="_parameters_6"></a>

## Parameters

<a id="_path_parameters_6"></a>

### Path Parameters

| Name | Description | Required | Default | Pattern |
|------|-------------|----------|---------|---------|
| id   |             | X        | null    |         |

<a id="_body_parameter_4"></a>

### Body Parameter

| Name | Description | Required | Default | Pattern |
|------|-------------|----------|---------|---------|
| body | `object`    | X        |         |         |

<a id="_return_type_6"></a>

## Return Type

`Object`

<a id="_content_type_6"></a>

## Content Type

- application/json

<a id="_responses_6"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | `Object` |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_6"></a>

## Samples
