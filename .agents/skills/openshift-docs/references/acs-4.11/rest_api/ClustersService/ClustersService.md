<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

<a id="DeleteCluster_ClustersService"></a>

# DeleteCluster

`DELETE /v1/clusters/{id}`

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

<a id="GetCluster_ClustersService"></a>

# GetCluster

`GET /v1/clusters/{id}`

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

[V1ClusterResponse](../CommonObjectReference/CommonObjectReference.md#V1ClusterResponse_CommonObjectReference)

<a id="_content_type_2"></a>

## Content Type

- application/json

<a id="_responses_2"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V1ClusterResponse](../CommonObjectReference/CommonObjectReference.md#V1ClusterResponse_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_2"></a>

## Samples

<a id="GetClusterDefaultValues_ClustersService"></a>

# GetClusterDefaultValues

`GET /v1/cluster-defaults`

<a id="_description_3"></a>

## Description

<a id="_parameters_3"></a>

## Parameters

<a id="_return_type_3"></a>

## Return Type

[V1ClusterDefaultsResponse](../CommonObjectReference/CommonObjectReference.md#V1ClusterDefaultsResponse_CommonObjectReference)

<a id="_content_type_3"></a>

## Content Type

- application/json

<a id="_responses_3"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V1ClusterDefaultsResponse](../CommonObjectReference/CommonObjectReference.md#V1ClusterDefaultsResponse_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_3"></a>

## Samples

<a id="GetClusters_ClustersService"></a>

# GetClusters

`GET /v1/clusters`

<a id="_description_4"></a>

## Description

<a id="_parameters_4"></a>

## Parameters

<a id="_query_parameters"></a>

### Query Parameters

| Name  | Description | Required | Default | Pattern |
|-------|-------------|----------|---------|---------|
| query |             | \-       | null    |         |

<a id="_return_type_4"></a>

## Return Type

[V1ClustersList](../CommonObjectReference/CommonObjectReference.md#V1ClustersList_CommonObjectReference)

<a id="_content_type_4"></a>

## Content Type

- application/json

<a id="_responses_4"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V1ClustersList](../CommonObjectReference/CommonObjectReference.md#V1ClustersList_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_4"></a>

## Samples

<a id="GetKernelSupportAvailable_ClustersService"></a>

# GetKernelSupportAvailable

`GET /v1/clusters-env/kernel-support-available`

GetKernelSupportAvailable is deprecated in favor of GetClusterDefaultValues.

<a id="_description_5"></a>

## Description

<a id="_parameters_5"></a>

## Parameters

<a id="_return_type_5"></a>

## Return Type

[V1KernelSupportAvailableResponse](../CommonObjectReference/CommonObjectReference.md#V1KernelSupportAvailableResponse_CommonObjectReference)

<a id="_content_type_5"></a>

## Content Type

- application/json

<a id="_responses_5"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V1KernelSupportAvailableResponse](../CommonObjectReference/CommonObjectReference.md#V1KernelSupportAvailableResponse_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_5"></a>

## Samples

<a id="PostCluster_ClustersService"></a>

# PostCluster

`POST /v1/clusters`

PostCluster is deprecated. Use operator-based installation with CRS instead.

<a id="_description_6"></a>

## Description

<a id="_parameters_6"></a>

## Parameters

<a id="_body_parameter"></a>

### Body Parameter

| Name | Description | Required | Default | Pattern |
|----|----|----|----|----|
| body | [StorageCluster](../CommonObjectReference/CommonObjectReference.md#StorageCluster_CommonObjectReference) | X |  |  |

<a id="_return_type_6"></a>

## Return Type

[V1ClusterResponse](../CommonObjectReference/CommonObjectReference.md#V1ClusterResponse_CommonObjectReference)

<a id="_content_type_6"></a>

## Content Type

- application/json

<a id="_responses_6"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V1ClusterResponse](../CommonObjectReference/CommonObjectReference.md#V1ClusterResponse_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_6"></a>

## Samples

<a id="PutCluster_ClustersService"></a>

# PutCluster

`PUT /v1/clusters/{id}`

PutCluster is deprecated. Use operator-based installation with CRS instead.

<a id="_description_7"></a>

## Description

<a id="_parameters_7"></a>

## Parameters

<a id="_path_parameters_3"></a>

### Path Parameters

| Name | Description | Required | Default | Pattern |
|------|-------------|----------|---------|---------|
| id   |             | X        | null    |         |

<a id="_body_parameter_2"></a>

### Body Parameter

| Name | Description | Required | Default | Pattern |
|----|----|----|----|----|
| body | [ClustersServicePutClusterBody](../CommonObjectReference/CommonObjectReference.md#ClustersServicePutClusterBody_CommonObjectReference) | X |  |  |

<a id="_return_type_7"></a>

## Return Type

[V1ClusterResponse](../CommonObjectReference/CommonObjectReference.md#V1ClusterResponse_CommonObjectReference)

<a id="_content_type_7"></a>

## Content Type

- application/json

<a id="_responses_7"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V1ClusterResponse](../CommonObjectReference/CommonObjectReference.md#V1ClusterResponse_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_7"></a>

## Samples
