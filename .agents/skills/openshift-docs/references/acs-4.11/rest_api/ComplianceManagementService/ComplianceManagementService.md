<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

<a id="GetRecentRuns_ComplianceManagementService"></a>

# GetRecentRuns

`GET /v1/complianceManagement/runs`

<a id="_description"></a>

## Description

<a id="_parameters"></a>

## Parameters

<a id="_query_parameters"></a>

### Query Parameters

| Name       | Description | Required | Default | Pattern |
|------------|-------------|----------|---------|---------|
| clusterId  |             | \-       | null    |         |
| standardId |             | \-       | null    |         |
| since      |             | \-       | null    |         |

<a id="_return_type"></a>

## Return Type

[V1GetRecentComplianceRunsResponse](../CommonObjectReference/CommonObjectReference.md#V1GetRecentComplianceRunsResponse_CommonObjectReference)

<a id="_content_type"></a>

## Content Type

- application/json

<a id="_responses"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V1GetRecentComplianceRunsResponse](../CommonObjectReference/CommonObjectReference.md#V1GetRecentComplianceRunsResponse_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples"></a>

## Samples

<a id="GetRunStatuses_ComplianceManagementService"></a>

# GetRunStatuses

`GET /v1/compliancemanagement/runstatuses`

<a id="_description_2"></a>

## Description

<a id="_parameters_2"></a>

## Parameters

<a id="_query_parameters_2"></a>

### Query Parameters

| Name   | Description | Required | Default | Pattern |
|--------|-------------|----------|---------|---------|
| runIds | `String`    | \-       | null    |         |
| latest |             | \-       | null    |         |

<a id="_return_type_2"></a>

## Return Type

[V1GetComplianceRunStatusesResponse](../CommonObjectReference/CommonObjectReference.md#V1GetComplianceRunStatusesResponse_CommonObjectReference)

<a id="_content_type_2"></a>

## Content Type

- application/json

<a id="_responses_2"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V1GetComplianceRunStatusesResponse](../CommonObjectReference/CommonObjectReference.md#V1GetComplianceRunStatusesResponse_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_2"></a>

## Samples

<a id="TriggerRuns_ComplianceManagementService"></a>

# TriggerRuns

`POST /v1/compliancemanagement/runs`

<a id="_description_3"></a>

## Description

<a id="_parameters_3"></a>

## Parameters

<a id="_body_parameter"></a>

### Body Parameter

| Name | Description | Required | Default | Pattern |
|----|----|----|----|----|
| body | [V1TriggerComplianceRunsRequest](../CommonObjectReference/CommonObjectReference.md#V1TriggerComplianceRunsRequest_CommonObjectReference) | X |  |  |

<a id="_return_type_3"></a>

## Return Type

[V1TriggerComplianceRunsResponse](../CommonObjectReference/CommonObjectReference.md#V1TriggerComplianceRunsResponse_CommonObjectReference)

<a id="_content_type_3"></a>

## Content Type

- application/json

<a id="_responses_3"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V1TriggerComplianceRunsResponse](../CommonObjectReference/CommonObjectReference.md#V1TriggerComplianceRunsResponse_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_3"></a>

## Samples
