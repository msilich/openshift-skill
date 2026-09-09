<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

<a id="GetAggregatedResults_ComplianceService"></a>

# GetAggregatedResults

`GET /v1/compliance/aggregatedresults`

<a id="_description"></a>

## Description

<a id="_parameters"></a>

## Parameters

<a id="_query_parameters"></a>

### Query Parameters

| Name | Description | Required | Default | Pattern |
|----|----|----|----|----|
| groupBy | `String` | \- | null |  |
| unit |  | \- | UNKNOWN |  |
| where.query |  | \- | null |  |
| where.pagination.limit |  | \- | null |  |
| where.pagination.offset |  | \- | null |  |
| where.pagination.sortOption.field |  | \- | null |  |
| where.pagination.sortOption.reversed |  | \- | null |  |
| where.pagination.sortOption.aggregateBy.aggrFunc |  | \- | UNSET |  |
| where.pagination.sortOption.aggregateBy.distinct |  | \- | null |  |

<a id="_return_type"></a>

## Return Type

[StorageComplianceAggregationResponse](../CommonObjectReference/CommonObjectReference.md#StorageComplianceAggregationResponse_CommonObjectReference)

<a id="_content_type"></a>

## Content Type

- application/json

<a id="_responses"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [StorageComplianceAggregationResponse](../CommonObjectReference/CommonObjectReference.md#StorageComplianceAggregationResponse_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples"></a>

## Samples

<a id="GetRunResults_ComplianceService"></a>

# GetRunResults

`GET /v1/compliance/runresults`

<a id="_description_2"></a>

## Description

<a id="_parameters_2"></a>

## Parameters

<a id="_query_parameters_2"></a>

### Query Parameters

| Name | Description | Required | Default | Pattern |
|----|----|----|----|----|
| clusterId |  | \- | null |  |
| standardId |  | \- | null |  |
| runId | Specifies the run ID for which to return results. If empty, the most recent run is returned. CAVEAT: Setting this field circumvents the results cache on the server-side, which may lead to significantly increased memory pressure and decreased performance. | \- | null |  |

<a id="_return_type_2"></a>

## Return Type

[V1GetComplianceRunResultsResponse](../CommonObjectReference/CommonObjectReference.md#V1GetComplianceRunResultsResponse_CommonObjectReference)

<a id="_content_type_2"></a>

## Content Type

- application/json

<a id="_responses_2"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V1GetComplianceRunResultsResponse](../CommonObjectReference/CommonObjectReference.md#V1GetComplianceRunResultsResponse_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_2"></a>

## Samples

<a id="GetStandard_ComplianceService"></a>

# GetStandard

`GET /v1/compliance/standards/{id}`

<a id="_description_3"></a>

## Description

<a id="_parameters_3"></a>

## Parameters

<a id="_path_parameters"></a>

### Path Parameters

| Name | Description | Required | Default | Pattern |
|------|-------------|----------|---------|---------|
| id   |             | X        | null    |         |

<a id="_return_type_3"></a>

## Return Type

[V1GetComplianceStandardResponse](../CommonObjectReference/CommonObjectReference.md#V1GetComplianceStandardResponse_CommonObjectReference)

<a id="_content_type_3"></a>

## Content Type

- application/json

<a id="_responses_3"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V1GetComplianceStandardResponse](../CommonObjectReference/CommonObjectReference.md#V1GetComplianceStandardResponse_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_3"></a>

## Samples

<a id="GetStandards_ComplianceService"></a>

# GetStandards

`GET /v1/compliance/standards`

<a id="_description_4"></a>

## Description

<a id="_parameters_4"></a>

## Parameters

<a id="_return_type_4"></a>

## Return Type

[V1GetComplianceStandardsResponse](../CommonObjectReference/CommonObjectReference.md#V1GetComplianceStandardsResponse_CommonObjectReference)

<a id="_content_type_4"></a>

## Content Type

- application/json

<a id="_responses_4"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V1GetComplianceStandardsResponse](../CommonObjectReference/CommonObjectReference.md#V1GetComplianceStandardsResponse_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_4"></a>

## Samples

<a id="UpdateComplianceStandardConfig_ComplianceService"></a>

# UpdateComplianceStandardConfig

`PATCH /v1/compliance/standards/{id}`

<a id="_description_5"></a>

## Description

<a id="_parameters_5"></a>

## Parameters

<a id="_path_parameters_2"></a>

### Path Parameters

| Name | Description | Required | Default | Pattern |
|------|-------------|----------|---------|---------|
| id   |             | X        | null    |         |

<a id="_body_parameter"></a>

### Body Parameter

| Name | Description | Required | Default | Pattern |
|----|----|----|----|----|
| body | [ComplianceServiceUpdateComplianceStandardConfigBody](../CommonObjectReference/CommonObjectReference.md#ComplianceServiceUpdateComplianceStandardConfigBody_CommonObjectReference) | X |  |  |

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
