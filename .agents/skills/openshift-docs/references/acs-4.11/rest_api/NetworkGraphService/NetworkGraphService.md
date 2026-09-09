<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

<a id="CreateExternalNetworkEntity_NetworkGraphService"></a>

# CreateExternalNetworkEntity

`POST /v1/networkgraph/cluster/{clusterId}/externalentities`

<a id="_description"></a>

## Description

<a id="_parameters"></a>

## Parameters

<a id="_path_parameters"></a>

### Path Parameters

| Name      | Description | Required | Default | Pattern |
|-----------|-------------|----------|---------|---------|
| clusterId |             | X        | null    |         |

<a id="_body_parameter"></a>

### Body Parameter

| Name | Description | Required | Default | Pattern |
|----|----|----|----|----|
| body | [NetworkGraphServiceCreateExternalNetworkEntityBody](../CommonObjectReference/CommonObjectReference.md#NetworkGraphServiceCreateExternalNetworkEntityBody_CommonObjectReference) | X |  |  |

<a id="_return_type"></a>

## Return Type

[StorageNetworkEntity](../CommonObjectReference/CommonObjectReference.md#StorageNetworkEntity_CommonObjectReference)

<a id="_content_type"></a>

## Content Type

- application/json

<a id="_responses"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [StorageNetworkEntity](../CommonObjectReference/CommonObjectReference.md#StorageNetworkEntity_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples"></a>

## Samples

<a id="DeleteExternalNetworkEntity_NetworkGraphService"></a>

# DeleteExternalNetworkEntity

`DELETE /v1/networkgraph/externalentities/{id}`

<a id="_description_2"></a>

## Description

<a id="_parameters_2"></a>

## Parameters

<a id="_path_parameters_2"></a>

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

<a id="GetExternalNetworkEntities_NetworkGraphService"></a>

# GetExternalNetworkEntities

`GET /v1/networkgraph/cluster/{clusterId}/externalentities`

<a id="_description_3"></a>

## Description

<a id="_parameters_3"></a>

## Parameters

<a id="_path_parameters_3"></a>

### Path Parameters

| Name      | Description | Required | Default | Pattern |
|-----------|-------------|----------|---------|---------|
| clusterId |             | X        | null    |         |

<a id="_query_parameters"></a>

### Query Parameters

| Name  | Description | Required | Default | Pattern |
|-------|-------------|----------|---------|---------|
| query |             | \-       | null    |         |

<a id="_return_type_3"></a>

## Return Type

[V1GetExternalNetworkEntitiesResponse](../CommonObjectReference/CommonObjectReference.md#V1GetExternalNetworkEntitiesResponse_CommonObjectReference)

<a id="_content_type_3"></a>

## Content Type

- application/json

<a id="_responses_3"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V1GetExternalNetworkEntitiesResponse](../CommonObjectReference/CommonObjectReference.md#V1GetExternalNetworkEntitiesResponse_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_3"></a>

## Samples

<a id="GetExternalNetworkFlows_NetworkGraphService"></a>

# GetExternalNetworkFlows

`GET /v1/networkgraph/cluster/{clusterId}/externalentities/{entityId}/flows`

<a id="_description_4"></a>

## Description

<a id="_parameters_4"></a>

## Parameters

<a id="_path_parameters_4"></a>

### Path Parameters

| Name      | Description | Required | Default | Pattern |
|-----------|-------------|----------|---------|---------|
| clusterId |             | X        | null    |         |
| entityId  |             | X        | null    |         |

<a id="_query_parameters_2"></a>

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

<a id="_return_type_4"></a>

## Return Type

[V1GetExternalNetworkFlowsResponse](../CommonObjectReference/CommonObjectReference.md#V1GetExternalNetworkFlowsResponse_CommonObjectReference)

<a id="_content_type_4"></a>

## Content Type

- application/json

<a id="_responses_4"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V1GetExternalNetworkFlowsResponse](../CommonObjectReference/CommonObjectReference.md#V1GetExternalNetworkFlowsResponse_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_4"></a>

## Samples

<a id="GetExternalNetworkFlowsMetadata_NetworkGraphService"></a>

# GetExternalNetworkFlowsMetadata

`GET /v1/networkgraph/cluster/{clusterId}/externalentities/metadata`

<a id="_description_5"></a>

## Description

<a id="_parameters_5"></a>

## Parameters

<a id="_path_parameters_5"></a>

### Path Parameters

| Name      | Description | Required | Default | Pattern |
|-----------|-------------|----------|---------|---------|
| clusterId |             | X        | null    |         |

<a id="_query_parameters_3"></a>

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

<a id="_return_type_5"></a>

## Return Type

[V1GetExternalNetworkFlowsMetadataResponse](../CommonObjectReference/CommonObjectReference.md#V1GetExternalNetworkFlowsMetadataResponse_CommonObjectReference)

<a id="_content_type_5"></a>

## Content Type

- application/json

<a id="_responses_5"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V1GetExternalNetworkFlowsMetadataResponse](../CommonObjectReference/CommonObjectReference.md#V1GetExternalNetworkFlowsMetadataResponse_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_5"></a>

## Samples

<a id="GetNetworkGraph_NetworkGraphService"></a>

# GetNetworkGraph

`GET /v1/networkgraph/cluster/{clusterId}`

<a id="_description_6"></a>

## Description

<a id="_parameters_6"></a>

## Parameters

<a id="_path_parameters_6"></a>

### Path Parameters

| Name      | Description | Required | Default | Pattern |
|-----------|-------------|----------|---------|---------|
| clusterId |             | X        | null    |         |

<a id="_query_parameters_4"></a>

### Query Parameters

| Name            | Description | Required | Default | Pattern |
|-----------------|-------------|----------|---------|---------|
| query           |             | \-       | null    |         |
| since           |             | \-       | null    |         |
| includePorts    |             | \-       | null    |         |
| scope.query     |             | \-       | null    |         |
| includePolicies |             | \-       | null    |         |

<a id="_return_type_6"></a>

## Return Type

[V1NetworkGraph](../CommonObjectReference/CommonObjectReference.md#V1NetworkGraph_CommonObjectReference)

<a id="_content_type_6"></a>

## Content Type

- application/json

<a id="_responses_6"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V1NetworkGraph](../CommonObjectReference/CommonObjectReference.md#V1NetworkGraph_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_6"></a>

## Samples

<a id="GetNetworkGraphConfig_NetworkGraphService"></a>

# GetNetworkGraphConfig

`GET /v1/networkgraph/config`

<a id="_description_7"></a>

## Description

<a id="_parameters_7"></a>

## Parameters

<a id="_return_type_7"></a>

## Return Type

[StorageNetworkGraphConfig](../CommonObjectReference/CommonObjectReference.md#StorageNetworkGraphConfig_CommonObjectReference)

<a id="_content_type_7"></a>

## Content Type

- application/json

<a id="_responses_7"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [StorageNetworkGraphConfig](../CommonObjectReference/CommonObjectReference.md#StorageNetworkGraphConfig_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_7"></a>

## Samples

<a id="PatchExternalNetworkEntity_NetworkGraphService"></a>

# PatchExternalNetworkEntity

`PATCH /v1/networkgraph/externalentities/{id}`

<a id="_description_8"></a>

## Description

<a id="_parameters_8"></a>

## Parameters

<a id="_path_parameters_7"></a>

### Path Parameters

| Name | Description | Required | Default | Pattern |
|------|-------------|----------|---------|---------|
| id   |             | X        | null    |         |

<a id="_body_parameter_2"></a>

### Body Parameter

| Name | Description | Required | Default | Pattern |
|----|----|----|----|----|
| body | [NetworkGraphServicePatchExternalNetworkEntityBody](../CommonObjectReference/CommonObjectReference.md#NetworkGraphServicePatchExternalNetworkEntityBody_CommonObjectReference) | X |  |  |

<a id="_return_type_8"></a>

## Return Type

[StorageNetworkEntity](../CommonObjectReference/CommonObjectReference.md#StorageNetworkEntity_CommonObjectReference)

<a id="_content_type_8"></a>

## Content Type

- application/json

<a id="_responses_8"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [StorageNetworkEntity](../CommonObjectReference/CommonObjectReference.md#StorageNetworkEntity_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_8"></a>

## Samples

<a id="PutNetworkGraphConfig_NetworkGraphService"></a>

# PutNetworkGraphConfig

`PUT /v1/networkgraph/config`

<a id="_description_9"></a>

## Description

<a id="_parameters_9"></a>

## Parameters

<a id="_body_parameter_3"></a>

### Body Parameter

| Name | Description | Required | Default | Pattern |
|----|----|----|----|----|
| body | [V1PutNetworkGraphConfigRequest](../CommonObjectReference/CommonObjectReference.md#V1PutNetworkGraphConfigRequest_CommonObjectReference) | X |  |  |

<a id="_return_type_9"></a>

## Return Type

[StorageNetworkGraphConfig](../CommonObjectReference/CommonObjectReference.md#StorageNetworkGraphConfig_CommonObjectReference)

<a id="_content_type_9"></a>

## Content Type

- application/json

<a id="_responses_9"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [StorageNetworkGraphConfig](../CommonObjectReference/CommonObjectReference.md#StorageNetworkGraphConfig_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_9"></a>

## Samples
