<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

<a id="BulkLockProcessBaselines_ProcessBaselineService"></a>

# BulkLockProcessBaselines

`PUT /v1/processbaselines/bulk/lock`

`BulkLockProcessBaselines` locks process baselines given a cluster and an optional set of namespaces. It returns success or an error.

<a id="_description"></a>

## Description

<a id="_parameters"></a>

## Parameters

<a id="_body_parameter"></a>

### Body Parameter

| Name | Description | Required | Default | Pattern |
|----|----|----|----|----|
| body | [V1BulkProcessBaselinesRequest](../CommonObjectReference/CommonObjectReference.md#V1BulkProcessBaselinesRequest_CommonObjectReference) | X |  |  |

<a id="_return_type"></a>

## Return Type

[V1BulkUpdateProcessBaselinesResponse](../CommonObjectReference/CommonObjectReference.md#V1BulkUpdateProcessBaselinesResponse_CommonObjectReference)

<a id="_content_type"></a>

## Content Type

- application/json

<a id="_responses"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V1BulkUpdateProcessBaselinesResponse](../CommonObjectReference/CommonObjectReference.md#V1BulkUpdateProcessBaselinesResponse_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples"></a>

## Samples

<a id="BulkUnlockProcessBaselines_ProcessBaselineService"></a>

# BulkUnlockProcessBaselines

`PUT /v1/processbaselines/bulk/unlock`

`BulkUnockProcessBaselines` unlocks process baselines given a cluster and an optional set of namespaces. It returns success or an error.

<a id="_description_2"></a>

## Description

<a id="_parameters_2"></a>

## Parameters

<a id="_body_parameter_2"></a>

### Body Parameter

| Name | Description | Required | Default | Pattern |
|----|----|----|----|----|
| body | [V1BulkProcessBaselinesRequest](../CommonObjectReference/CommonObjectReference.md#V1BulkProcessBaselinesRequest_CommonObjectReference) | X |  |  |

<a id="_return_type_2"></a>

## Return Type

[V1BulkUpdateProcessBaselinesResponse](../CommonObjectReference/CommonObjectReference.md#V1BulkUpdateProcessBaselinesResponse_CommonObjectReference)

<a id="_content_type_2"></a>

## Content Type

- application/json

<a id="_responses_2"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V1BulkUpdateProcessBaselinesResponse](../CommonObjectReference/CommonObjectReference.md#V1BulkUpdateProcessBaselinesResponse_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_2"></a>

## Samples

<a id="DeleteProcessBaselines_ProcessBaselineService"></a>

# DeleteProcessBaselines

`DELETE /v1/processbaselines`

`DeleteProcessBaselines` deletes baselines.

<a id="_description_3"></a>

## Description

<a id="_parameters_3"></a>

## Parameters

<a id="_query_parameters"></a>

### Query Parameters

| Name    | Description | Required | Default | Pattern |
|---------|-------------|----------|---------|---------|
| query   |             | \-       | null    |         |
| confirm |             | \-       | null    |         |

<a id="_return_type_3"></a>

## Return Type

[V1DeleteProcessBaselinesResponse](../CommonObjectReference/CommonObjectReference.md#V1DeleteProcessBaselinesResponse_CommonObjectReference)

<a id="_content_type_3"></a>

## Content Type

- application/json

<a id="_responses_3"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V1DeleteProcessBaselinesResponse](../CommonObjectReference/CommonObjectReference.md#V1DeleteProcessBaselinesResponse_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_3"></a>

## Samples

<a id="GetProcessBaseline_ProcessBaselineService"></a>

# GetProcessBaseline

`GET /v1/processbaselines/key`

`GetProcessBaselineById` returns the single process baseline referenced by the given ID.

<a id="_description_4"></a>

## Description

<a id="_parameters_4"></a>

## Parameters

<a id="_query_parameters_2"></a>

### Query Parameters

| Name | Description | Required | Default | Pattern |
|----|----|----|----|----|
| key.deploymentId | The idea is for the keys to be flexible. Only certain combinations of these will be supported. | \- | null |  |
| key.containerName |  | \- | null |  |
| key.clusterId |  | \- | null |  |
| key.namespace |  | \- | null |  |

<a id="_return_type_4"></a>

## Return Type

[StorageProcessBaseline](../CommonObjectReference/CommonObjectReference.md#StorageProcessBaseline_CommonObjectReference)

<a id="_content_type_4"></a>

## Content Type

- application/json

<a id="_responses_4"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [StorageProcessBaseline](../CommonObjectReference/CommonObjectReference.md#StorageProcessBaseline_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_4"></a>

## Samples

<a id="LockProcessBaselines_ProcessBaselineService"></a>

# LockProcessBaselines

`PUT /v1/processbaselines/lock`

`LockProcessBaselines` accepts a list of baseline IDs, locks those baselines, and returns the updated baseline objects.

<a id="_description_5"></a>

## Description

<a id="_parameters_5"></a>

## Parameters

<a id="_body_parameter_3"></a>

### Body Parameter

| Name | Description | Required | Default | Pattern |
|----|----|----|----|----|
| body | [V1LockProcessBaselinesRequest](../CommonObjectReference/CommonObjectReference.md#V1LockProcessBaselinesRequest_CommonObjectReference) | X |  |  |

<a id="_return_type_5"></a>

## Return Type

[V1UpdateProcessBaselinesResponse](../CommonObjectReference/CommonObjectReference.md#V1UpdateProcessBaselinesResponse_CommonObjectReference)

<a id="_content_type_5"></a>

## Content Type

- application/json

<a id="_responses_5"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V1UpdateProcessBaselinesResponse](../CommonObjectReference/CommonObjectReference.md#V1UpdateProcessBaselinesResponse_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_5"></a>

## Samples

<a id="UpdateProcessBaselines_ProcessBaselineService"></a>

# UpdateProcessBaselines

`PUT /v1/processbaselines`

`AddToProcessBaselines` adds a list of process names to each of a list of process baselines.

<a id="_description_6"></a>

## Description

<a id="_parameters_6"></a>

## Parameters

<a id="_body_parameter_4"></a>

### Body Parameter

| Name | Description | Required | Default | Pattern |
|----|----|----|----|----|
| body | [V1UpdateProcessBaselinesRequest](../CommonObjectReference/CommonObjectReference.md#V1UpdateProcessBaselinesRequest_CommonObjectReference) | X |  |  |

<a id="_return_type_6"></a>

## Return Type

[V1UpdateProcessBaselinesResponse](../CommonObjectReference/CommonObjectReference.md#V1UpdateProcessBaselinesResponse_CommonObjectReference)

<a id="_content_type_6"></a>

## Content Type

- application/json

<a id="_responses_6"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V1UpdateProcessBaselinesResponse](../CommonObjectReference/CommonObjectReference.md#V1UpdateProcessBaselinesResponse_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_6"></a>

## Samples
