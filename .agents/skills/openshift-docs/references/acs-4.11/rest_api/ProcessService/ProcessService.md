<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

<a id="CountProcesses_ProcessService"></a>

# CountProcesses

`GET /v1/processcount`

CountProcesses returns the count of processes.

<a id="_description"></a>

## Description

<a id="_parameters"></a>

## Parameters

<a id="_query_parameters"></a>

### Query Parameters

| Name | Description | Required | Default | Pattern |
|----|----|----|----|----|
| query |  | \- | null |  |
| pagination.limit |  | \- | null |  |
| pagination.offset |  | \- | null |  |
| pagination.sortOption.field |  | \- | null |  |
| pagination.sortOption.reversed |  | \- | null |  |
| pagination.sortOption.aggregateBy.aggrFunc |  | \- | UNSET |  |
| pagination.sortOption.aggregateBy.distinct |  | \- | null |  |

<a id="_return_type"></a>

## Return Type

[V1CountProcessesResponse](../CommonObjectReference/CommonObjectReference.md#V1CountProcessesResponse_CommonObjectReference)

<a id="_content_type"></a>

## Content Type

- application/json

<a id="_responses"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V1CountProcessesResponse](../CommonObjectReference/CommonObjectReference.md#V1CountProcessesResponse_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples"></a>

## Samples

<a id="GetGroupedProcessByDeployment_ProcessService"></a>

# GetGroupedProcessByDeployment

`GET /v1/processes/deployment/{deploymentId}/grouped`

GetGroupedProcessByDeployment returns all the processes executed grouped by deployment.

<a id="_description_2"></a>

## Description

<a id="_parameters_2"></a>

## Parameters

<a id="_path_parameters"></a>

### Path Parameters

| Name         | Description | Required | Default | Pattern |
|--------------|-------------|----------|---------|---------|
| deploymentId |             | X        | null    |         |

<a id="_return_type_2"></a>

## Return Type

[V1GetGroupedProcessesResponse](../CommonObjectReference/CommonObjectReference.md#V1GetGroupedProcessesResponse_CommonObjectReference)

<a id="_content_type_2"></a>

## Content Type

- application/json

<a id="_responses_2"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V1GetGroupedProcessesResponse](../CommonObjectReference/CommonObjectReference.md#V1GetGroupedProcessesResponse_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_2"></a>

## Samples

<a id="GetGroupedProcessByDeploymentAndContainer_ProcessService"></a>

# GetGroupedProcessByDeploymentAndContainer

`GET /v1/processes/deployment/{deploymentId}/grouped/container`

GetGroupedProcessByDeploymentAndContainer returns all the processes executed grouped by deployment and container.

<a id="_description_3"></a>

## Description

<a id="_parameters_3"></a>

## Parameters

<a id="_path_parameters_2"></a>

### Path Parameters

| Name         | Description | Required | Default | Pattern |
|--------------|-------------|----------|---------|---------|
| deploymentId |             | X        | null    |         |

<a id="_return_type_3"></a>

## Return Type

[V1GetGroupedProcessesWithContainerResponse](../CommonObjectReference/CommonObjectReference.md#V1GetGroupedProcessesWithContainerResponse_CommonObjectReference)

<a id="_content_type_3"></a>

## Content Type

- application/json

<a id="_responses_3"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V1GetGroupedProcessesWithContainerResponse](../CommonObjectReference/CommonObjectReference.md#V1GetGroupedProcessesWithContainerResponse_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_3"></a>

## Samples

<a id="GetProcessesByDeployment_ProcessService"></a>

# GetProcessesByDeployment

`GET /v1/processes/deployment/{deploymentId}`

GetProcessesByDeployment returns the processes executed in the given deployment.

<a id="_description_4"></a>

## Description

<a id="_parameters_4"></a>

## Parameters

<a id="_path_parameters_3"></a>

### Path Parameters

| Name         | Description | Required | Default | Pattern |
|--------------|-------------|----------|---------|---------|
| deploymentId |             | X        | null    |         |

<a id="_return_type_4"></a>

## Return Type

[V1GetProcessesResponse](../CommonObjectReference/CommonObjectReference.md#V1GetProcessesResponse_CommonObjectReference)

<a id="_content_type_4"></a>

## Content Type

- application/json

<a id="_responses_4"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V1GetProcessesResponse](../CommonObjectReference/CommonObjectReference.md#V1GetProcessesResponse_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_4"></a>

## Samples
