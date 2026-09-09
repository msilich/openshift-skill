<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

<a id="GetComplianceClusterScanStats_ComplianceResultsStatsService"></a>

# GetComplianceClusterScanStats

`GET /v2/compliance/stats/configurations/clusters/{clusterId}`

GetComplianceClusterScanStats lists the current scan stats for a cluster for each scan configuration

<a id="_description"></a>

## Description

<a id="_parameters"></a>

## Parameters

<a id="_path_parameters"></a>

### Path Parameters

| Name      | Description | Required | Default | Pattern |
|-----------|-------------|----------|---------|---------|
| clusterId |             | X        | null    |         |

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

[V2ListComplianceClusterScanStatsResponse](../CommonObjectReference/CommonObjectReference.md#V2ListComplianceClusterScanStatsResponse_CommonObjectReference)

<a id="_content_type"></a>

## Content Type

- application/json

<a id="_responses"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V2ListComplianceClusterScanStatsResponse](../CommonObjectReference/CommonObjectReference.md#V2ListComplianceClusterScanStatsResponse_CommonObjectReference) |
| 0 | An unexpected error response. | [RpcStatus](../CommonObjectReference/CommonObjectReference.md#RpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples"></a>

## Samples

<a id="GetComplianceClusterStats_ComplianceResultsStatsService"></a>

# GetComplianceClusterStats

`GET /v2/compliance/scan/stats/profiles/{profileName}/clusters`

<a id="_description_2"></a>

## Description

<a id="_parameters_2"></a>

## Parameters

<a id="_path_parameters_2"></a>

### Path Parameters

| Name        | Description | Required | Default | Pattern |
|-------------|-------------|----------|---------|---------|
| profileName |             | X        | null    |         |

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

[V2ListComplianceClusterOverallStatsResponse](../CommonObjectReference/CommonObjectReference.md#V2ListComplianceClusterOverallStatsResponse_CommonObjectReference)

<a id="_content_type_2"></a>

## Content Type

- application/json

<a id="_responses_2"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V2ListComplianceClusterOverallStatsResponse](../CommonObjectReference/CommonObjectReference.md#V2ListComplianceClusterOverallStatsResponse_CommonObjectReference) |
| 0 | An unexpected error response. | [RpcStatus](../CommonObjectReference/CommonObjectReference.md#RpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_2"></a>

## Samples

<a id="GetComplianceOverallClusterStats_ComplianceResultsStatsService"></a>

# GetComplianceOverallClusterStats

`GET /v2/compliance/scan/stats/overall/cluster`

Deprecated in favor of GetComplianceClusterStats

<a id="_description_3"></a>

## Description

<a id="_parameters_3"></a>

## Parameters

<a id="_query_parameters_3"></a>

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

<a id="_return_type_3"></a>

## Return Type

[V2ListComplianceClusterOverallStatsResponse](../CommonObjectReference/CommonObjectReference.md#V2ListComplianceClusterOverallStatsResponse_CommonObjectReference)

<a id="_content_type_3"></a>

## Content Type

- application/json

<a id="_responses_3"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V2ListComplianceClusterOverallStatsResponse](../CommonObjectReference/CommonObjectReference.md#V2ListComplianceClusterOverallStatsResponse_CommonObjectReference) |
| 0 | An unexpected error response. | [RpcStatus](../CommonObjectReference/CommonObjectReference.md#RpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_3"></a>

## Samples

<a id="GetComplianceProfileCheckStats_ComplianceResultsStatsService"></a>

# GetComplianceProfileCheckStats

`GET /v2/compliance/scan/stats/profiles/{profileName}/checks/{checkName}`

GetComplianceProfileCheckStats lists current stats for a specific cluster check

<a id="_description_4"></a>

## Description

<a id="_parameters_4"></a>

## Parameters

<a id="_path_parameters_3"></a>

### Path Parameters

| Name        | Description | Required | Default | Pattern |
|-------------|-------------|----------|---------|---------|
| profileName |             | X        | null    |         |
| checkName   |             | X        | null    |         |

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

<a id="GetComplianceProfileStats_ComplianceResultsStatsService"></a>

# GetComplianceProfileStats

`GET /v2/compliance/scan/stats/profiles/{profileName}`

GetComplianceProfileStats lists current scan stats grouped by profile Optional RawQuery query fields can be combined. Commonly used ones include but are not limited to - scan: id(s) of the compliance scan - cluster: id(s) of the cluster - profile: id(s) of the profile

<a id="_description_5"></a>

## Description

<a id="_parameters_5"></a>

## Parameters

<a id="_path_parameters_4"></a>

### Path Parameters

| Name        | Description | Required | Default | Pattern |
|-------------|-------------|----------|---------|---------|
| profileName |             | X        | null    |         |

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

<a id="_return_type_5"></a>

## Return Type

[V2ListComplianceProfileScanStatsResponse](../CommonObjectReference/CommonObjectReference.md#V2ListComplianceProfileScanStatsResponse_CommonObjectReference)

<a id="_content_type_5"></a>

## Content Type

- application/json

<a id="_responses_5"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V2ListComplianceProfileScanStatsResponse](../CommonObjectReference/CommonObjectReference.md#V2ListComplianceProfileScanStatsResponse_CommonObjectReference) |
| 0 | An unexpected error response. | [RpcStatus](../CommonObjectReference/CommonObjectReference.md#RpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_5"></a>

## Samples

<a id="GetComplianceProfilesClusterStats_ComplianceResultsStatsService"></a>

# GetComplianceProfilesClusterStats

`GET /v2/compliance/scan/stats/profiles/clusters/{clusterId}`

GetComplianceProfilesClusterStats lists cluster stats grouped by profile

<a id="_description_6"></a>

## Description

<a id="_parameters_6"></a>

## Parameters

<a id="_path_parameters_5"></a>

### Path Parameters

| Name      | Description | Required | Default | Pattern |
|-----------|-------------|----------|---------|---------|
| clusterId |             | X        | null    |         |

<a id="_query_parameters_6"></a>

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

[V2ListComplianceClusterProfileStatsResponse](../CommonObjectReference/CommonObjectReference.md#V2ListComplianceClusterProfileStatsResponse_CommonObjectReference)

<a id="_content_type_6"></a>

## Content Type

- application/json

<a id="_responses_6"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V2ListComplianceClusterProfileStatsResponse](../CommonObjectReference/CommonObjectReference.md#V2ListComplianceClusterProfileStatsResponse_CommonObjectReference) |
| 0 | An unexpected error response. | [RpcStatus](../CommonObjectReference/CommonObjectReference.md#RpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_6"></a>

## Samples

<a id="GetComplianceProfilesStats_ComplianceResultsStatsService"></a>

# GetComplianceProfilesStats

`GET /v2/compliance/scan/stats/profiles`

GetComplianceProfileScanStats lists current scan stats grouped by profile Optional RawQuery query fields can be combined. Commonly used ones include but are not limited to - scan: id(s) of the compliance scan - cluster: id(s) of the cluster - profile: id(s) of the profile

<a id="_description_7"></a>

## Description

<a id="_parameters_7"></a>

## Parameters

<a id="_query_parameters_7"></a>

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

[V2ListComplianceProfileScanStatsResponse](../CommonObjectReference/CommonObjectReference.md#V2ListComplianceProfileScanStatsResponse_CommonObjectReference)

<a id="_content_type_7"></a>

## Content Type

- application/json

<a id="_responses_7"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V2ListComplianceProfileScanStatsResponse](../CommonObjectReference/CommonObjectReference.md#V2ListComplianceProfileScanStatsResponse_CommonObjectReference) |
| 0 | An unexpected error response. | [RpcStatus](../CommonObjectReference/CommonObjectReference.md#RpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_7"></a>

## Samples
