<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

<a id="GetComplianceProfileCheckDetails_ComplianceResultsService"></a>

# GetComplianceProfileCheckDetails

`GET /v2/compliance/scan/results/profiles/{profileName}/checks/{checkName}/details`

GetComplianceProfileCheckDetails

<a id="_description"></a>

## Description

<a id="_parameters"></a>

## Parameters

<a id="_path_parameters"></a>

### Path Parameters

| Name        | Description | Required | Default | Pattern |
|-------------|-------------|----------|---------|---------|
| profileName |             | X        | null    |         |
| checkName   |             | X        | null    |         |

<a id="_query_parameters"></a>

### Query Parameters

| Name | Description | Required | Default | Pattern |
|----|----|----|----|----|
| query.query |  | \- | null |  |
| query.pagination.limit |  | \- | null |  |
| query.pagination.offset |  | \- | null |  |
| query.pagination.sortOption.field |  | \- | null |  |
| query.pagination.sortOption.reversed |  | \- | null |  |
| query.pagination.sortOption.aggregateBy.aggrFunc |  | \- | UNSET |  |
| query.pagination.sortOption.aggregateBy.distinct |  | \- | null |  |

<a id="_return_type"></a>

## Return Type

[V2ComplianceClusterCheckStatus](../CommonObjectReference/CommonObjectReference.md#V2ComplianceClusterCheckStatus_CommonObjectReference)

<a id="_content_type"></a>

## Content Type

- application/json

<a id="_responses"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V2ComplianceClusterCheckStatus](../CommonObjectReference/CommonObjectReference.md#V2ComplianceClusterCheckStatus_CommonObjectReference) |
| 0 | An unexpected error response. | [RpcStatus](../CommonObjectReference/CommonObjectReference.md#RpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples"></a>

## Samples

<a id="GetComplianceProfileCheckResult_ComplianceResultsService"></a>

# GetComplianceProfileCheckResult

`GET /v2/compliance/scan/results/profiles/{profileName}/checks/{checkName}`

GetComplianceProfileCheckResult lists status of a check per cluster

<a id="_description_2"></a>

## Description

<a id="_parameters_2"></a>

## Parameters

<a id="_path_parameters_2"></a>

### Path Parameters

| Name        | Description | Required | Default | Pattern |
|-------------|-------------|----------|---------|---------|
| profileName |             | X        | null    |         |
| checkName   |             | X        | null    |         |

<a id="_query_parameters_2"></a>

### Query Parameters

| Name | Description | Required | Default | Pattern |
|----|----|----|----|----|
| query.query |  | \- | null |  |
| query.pagination.limit |  | \- | null |  |
| query.pagination.offset |  | \- | null |  |
| query.pagination.sortOption.field |  | \- | null |  |
| query.pagination.sortOption.reversed |  | \- | null |  |
| query.pagination.sortOption.aggregateBy.aggrFunc |  | \- | UNSET |  |
| query.pagination.sortOption.aggregateBy.distinct |  | \- | null |  |

<a id="_return_type_2"></a>

## Return Type

[V2ListComplianceCheckClusterResponse](../CommonObjectReference/CommonObjectReference.md#V2ListComplianceCheckClusterResponse_CommonObjectReference)

<a id="_content_type_2"></a>

## Content Type

- application/json

<a id="_responses_2"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V2ListComplianceCheckClusterResponse](../CommonObjectReference/CommonObjectReference.md#V2ListComplianceCheckClusterResponse_CommonObjectReference) |
| 0 | An unexpected error response. | [RpcStatus](../CommonObjectReference/CommonObjectReference.md#RpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_2"></a>

## Samples

<a id="GetComplianceProfileClusterResults_ComplianceResultsService"></a>

# GetComplianceProfileClusterResults

`GET /v2/compliance/scan/results/profiles/{profileName}/clusters/{clusterId}`

GetComplianceProfileClusterResults lists check results for a specific profile on a specific cluster

<a id="_description_3"></a>

## Description

<a id="_parameters_3"></a>

## Parameters

<a id="_path_parameters_3"></a>

### Path Parameters

| Name        | Description | Required | Default | Pattern |
|-------------|-------------|----------|---------|---------|
| profileName |             | X        | null    |         |
| clusterId   |             | X        | null    |         |

<a id="_query_parameters_3"></a>

### Query Parameters

| Name | Description | Required | Default | Pattern |
|----|----|----|----|----|
| query.query |  | \- | null |  |
| query.pagination.limit |  | \- | null |  |
| query.pagination.offset |  | \- | null |  |
| query.pagination.sortOption.field |  | \- | null |  |
| query.pagination.sortOption.reversed |  | \- | null |  |
| query.pagination.sortOption.aggregateBy.aggrFunc |  | \- | UNSET |  |
| query.pagination.sortOption.aggregateBy.distinct |  | \- | null |  |

<a id="_return_type_3"></a>

## Return Type

[V2ListComplianceCheckResultResponse](../CommonObjectReference/CommonObjectReference.md#V2ListComplianceCheckResultResponse_CommonObjectReference)

<a id="_content_type_3"></a>

## Content Type

- application/json

<a id="_responses_3"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V2ListComplianceCheckResultResponse](../CommonObjectReference/CommonObjectReference.md#V2ListComplianceCheckResultResponse_CommonObjectReference) |
| 0 | An unexpected error response. | [RpcStatus](../CommonObjectReference/CommonObjectReference.md#RpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_3"></a>

## Samples

<a id="GetComplianceProfileResults_ComplianceResultsService"></a>

# GetComplianceProfileResults

`GET /v2/compliance/scan/results/profiles/{profileName}/checks`

GetComplianceProfileResults retrieves the most recent compliance operator scan results for the specified query Optional RawQuery query fields can be combined.

<a id="_description_4"></a>

## Description

<a id="_parameters_4"></a>

## Parameters

<a id="_path_parameters_4"></a>

### Path Parameters

| Name        | Description | Required | Default | Pattern |
|-------------|-------------|----------|---------|---------|
| profileName |             | X        | null    |         |

<a id="_query_parameters_4"></a>

### Query Parameters

| Name | Description | Required | Default | Pattern |
|----|----|----|----|----|
| query.query |  | \- | null |  |
| query.pagination.limit |  | \- | null |  |
| query.pagination.offset |  | \- | null |  |
| query.pagination.sortOption.field |  | \- | null |  |
| query.pagination.sortOption.reversed |  | \- | null |  |
| query.pagination.sortOption.aggregateBy.aggrFunc |  | \- | UNSET |  |
| query.pagination.sortOption.aggregateBy.distinct |  | \- | null |  |

<a id="_return_type_4"></a>

## Return Type

[V2ListComplianceProfileResults](../CommonObjectReference/CommonObjectReference.md#V2ListComplianceProfileResults_CommonObjectReference)

<a id="_content_type_4"></a>

## Content Type

- application/json

<a id="_responses_4"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V2ListComplianceProfileResults](../CommonObjectReference/CommonObjectReference.md#V2ListComplianceProfileResults_CommonObjectReference) |
| 0 | An unexpected error response. | [RpcStatus](../CommonObjectReference/CommonObjectReference.md#RpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_4"></a>

## Samples

<a id="GetComplianceScanCheckResult_ComplianceResultsService"></a>

# GetComplianceScanCheckResult

`GET /v2/compliance/scan/result/{id}`

GetComplianceScanCheckResult returns the specific result by ID

<a id="_description_5"></a>

## Description

<a id="_parameters_5"></a>

## Parameters

<a id="_path_parameters_5"></a>

### Path Parameters

| Name | Description | Required | Default | Pattern |
|------|-------------|----------|---------|---------|
| id   |             | X        | null    |         |

<a id="_return_type_5"></a>

## Return Type

[V2ComplianceClusterCheckStatus](../CommonObjectReference/CommonObjectReference.md#V2ComplianceClusterCheckStatus_CommonObjectReference)

<a id="_content_type_5"></a>

## Content Type

- application/json

<a id="_responses_5"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V2ComplianceClusterCheckStatus](../CommonObjectReference/CommonObjectReference.md#V2ComplianceClusterCheckStatus_CommonObjectReference) |
| 0 | An unexpected error response. | [RpcStatus](../CommonObjectReference/CommonObjectReference.md#RpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_5"></a>

## Samples

<a id="GetComplianceScanConfigurationResults_ComplianceResultsService"></a>

# GetComplianceScanConfigurationResults

`GET /v2/compliance/scan/results/{scanConfigName}`

GetComplianceScanConfigurationResults retrieves the most recent compliance operator scan results for the specified query Optional RawQuery query fields can be combined.

<a id="_description_6"></a>

## Description

<a id="_parameters_6"></a>

## Parameters

<a id="_path_parameters_6"></a>

### Path Parameters

| Name           | Description | Required | Default | Pattern |
|----------------|-------------|----------|---------|---------|
| scanConfigName |             | X        | null    |         |

<a id="_query_parameters_5"></a>

### Query Parameters

| Name | Description | Required | Default | Pattern |
|----|----|----|----|----|
| query.query |  | \- | null |  |
| query.pagination.limit |  | \- | null |  |
| query.pagination.offset |  | \- | null |  |
| query.pagination.sortOption.field |  | \- | null |  |
| query.pagination.sortOption.reversed |  | \- | null |  |
| query.pagination.sortOption.aggregateBy.aggrFunc |  | \- | UNSET |  |
| query.pagination.sortOption.aggregateBy.distinct |  | \- | null |  |

<a id="_return_type_6"></a>

## Return Type

[V2ListComplianceResultsResponse](../CommonObjectReference/CommonObjectReference.md#V2ListComplianceResultsResponse_CommonObjectReference)

<a id="_content_type_6"></a>

## Content Type

- application/json

<a id="_responses_6"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V2ListComplianceResultsResponse](../CommonObjectReference/CommonObjectReference.md#V2ListComplianceResultsResponse_CommonObjectReference) |
| 0 | An unexpected error response. | [RpcStatus](../CommonObjectReference/CommonObjectReference.md#RpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_6"></a>

## Samples

<a id="GetComplianceScanResults_ComplianceResultsService"></a>

# GetComplianceScanResults

`GET /v2/compliance/scan/results`

GetComplianceScanResults retrieves the most recent compliance operator scan results for the specified query Optional RawQuery query fields can be combined. Commonly used ones include but are not limited to - scan: id(s) of the compliance scan - cluster: id(s) of the cluster - profile: id(s) of the profile

<a id="_description_7"></a>

## Description

<a id="_parameters_7"></a>

## Parameters

<a id="_query_parameters_6"></a>

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

<a id="_return_type_7"></a>

## Return Type

[V2ListComplianceResultsResponse](../CommonObjectReference/CommonObjectReference.md#V2ListComplianceResultsResponse_CommonObjectReference)

<a id="_content_type_7"></a>

## Content Type

- application/json

<a id="_responses_7"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V2ListComplianceResultsResponse](../CommonObjectReference/CommonObjectReference.md#V2ListComplianceResultsResponse_CommonObjectReference) |
| 0 | An unexpected error response. | [RpcStatus](../CommonObjectReference/CommonObjectReference.md#RpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_7"></a>

## Samples
