<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

<a id="GetComplianceProfile_ComplianceProfileService"></a>

# GetComplianceProfile

`GET /v2/compliance/profile/{id}`

GetComplianceProfile retrieves the specified compliance profile

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

[V2ComplianceProfile](../CommonObjectReference/CommonObjectReference.md#V2ComplianceProfile_CommonObjectReference)

<a id="_content_type"></a>

## Content Type

- application/json

<a id="_responses"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V2ComplianceProfile](../CommonObjectReference/CommonObjectReference.md#V2ComplianceProfile_CommonObjectReference) |
| 0 | An unexpected error response. | [RpcStatus](../CommonObjectReference/CommonObjectReference.md#RpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples"></a>

## Samples

<a id="ListComplianceProfiles_ComplianceProfileService"></a>

# ListComplianceProfiles

`GET /v2/compliance/profiles/cluster`

ListComplianceProfiles returns profiles matching given request

<a id="_description_2"></a>

## Description

<a id="_parameters_2"></a>

## Parameters

<a id="_query_parameters"></a>

### Query Parameters

| Name | Description | Required | Default | Pattern |
|----|----|----|----|----|
| clusterId |  | \- | null |  |
| query.query |  | \- | null |  |
| query.pagination.limit |  | \- | null |  |
| query.pagination.offset |  | \- | null |  |
| query.pagination.sortOption.field |  | \- | null |  |
| query.pagination.sortOption.reversed |  | \- | null |  |
| query.pagination.sortOption.aggregateBy.aggrFunc |  | \- | UNSET |  |
| query.pagination.sortOption.aggregateBy.distinct |  | \- | null |  |

<a id="_return_type_2"></a>

## Return Type

[V2ListComplianceProfilesResponse](../CommonObjectReference/CommonObjectReference.md#V2ListComplianceProfilesResponse_CommonObjectReference)

<a id="_content_type_2"></a>

## Content Type

- application/json

<a id="_responses_2"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V2ListComplianceProfilesResponse](../CommonObjectReference/CommonObjectReference.md#V2ListComplianceProfilesResponse_CommonObjectReference) |
| 0 | An unexpected error response. | [RpcStatus](../CommonObjectReference/CommonObjectReference.md#RpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_2"></a>

## Samples

<a id="ListProfileSummaries_ComplianceProfileService"></a>

# ListProfileSummaries

`GET /v2/compliance/profiles/summary`

ListProfileSummaries returns profiles matching each cluster and the given query

<a id="_description_3"></a>

## Description

<a id="_parameters_3"></a>

## Parameters

<a id="_query_parameters_2"></a>

### Query Parameters

| Name | Description | Required | Default | Pattern |
|----|----|----|----|----|
| clusterIds | `String` | \- | null |  |
| query.query |  | \- | null |  |
| query.pagination.limit |  | \- | null |  |
| query.pagination.offset |  | \- | null |  |
| query.pagination.sortOption.field |  | \- | null |  |
| query.pagination.sortOption.reversed |  | \- | null |  |
| query.pagination.sortOption.aggregateBy.aggrFunc |  | \- | UNSET |  |
| query.pagination.sortOption.aggregateBy.distinct |  | \- | null |  |

<a id="_return_type_3"></a>

## Return Type

[V2ListComplianceProfileSummaryResponse](../CommonObjectReference/CommonObjectReference.md#V2ListComplianceProfileSummaryResponse_CommonObjectReference)

<a id="_content_type_3"></a>

## Content Type

- application/json

<a id="_responses_3"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V2ListComplianceProfileSummaryResponse](../CommonObjectReference/CommonObjectReference.md#V2ListComplianceProfileSummaryResponse_CommonObjectReference) |
| 0 | An unexpected error response. | [RpcStatus](../CommonObjectReference/CommonObjectReference.md#RpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_3"></a>

## Samples
