<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

<a id="GetListeningEndpoints_ListeningEndpointsService"></a>

# GetListeningEndpoints

`GET /v1/listening_endpoints/deployment/{deploymentId}`

GetListeningEndpoints returns the listening endpoints and the processes that opened them for a given deployment

<a id="_description"></a>

## Description

<a id="_parameters"></a>

## Parameters

<a id="_path_parameters"></a>

### Path Parameters

| Name         | Description | Required | Default | Pattern |
|--------------|-------------|----------|---------|---------|
| deploymentId |             | X        | null    |         |

<a id="_query_parameters"></a>

### Query Parameters

| Name | Description | Required | Default | Pattern |
|----|----|----|----|----|
| pagination.limit |  | \- | null |  |
| pagination.offset |  | \- | null |  |
| pagination.sortOption.field |  | \- | null |  |
| pagination.sortOption.reversed |  | \- | null |  |
| pagination.sortOption.aggregateBy.aggrFunc |  | \- | UNSET |  |
| pagination.sortOption.aggregateBy.distinct |  | \- | null |  |

<a id="_return_type"></a>

## Return Type

[V1GetProcessesListeningOnPortsResponse](../CommonObjectReference/CommonObjectReference.md#V1GetProcessesListeningOnPortsResponse_CommonObjectReference)

<a id="_content_type"></a>

## Content Type

- application/json

<a id="_responses"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V1GetProcessesListeningOnPortsResponse](../CommonObjectReference/CommonObjectReference.md#V1GetProcessesListeningOnPortsResponse_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples"></a>

## Samples
