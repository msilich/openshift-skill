<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

<a id="CancelReport_ReportService"></a>

# CancelReport

`DELETE /v2/reports/jobs/{id}/cancel`

Cancels a queued report job for the given report id. If the job is not active, it is a noop. If a report is already being prepared, it won’t be cancelled.

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
| 0 | An unexpected error response. | [RpcStatus](../CommonObjectReference/CommonObjectReference.md#RpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples"></a>

## Samples

<a id="CountReportConfigurations_ReportService"></a>

# CountReportConfigurations

`GET /v2/reports/configuration-count`

CountReportConfigurations returns the number of report configurations.

<a id="_description_2"></a>

## Description

<a id="_parameters_2"></a>

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

<a id="_return_type_2"></a>

## Return Type

[V2CountReportConfigurationsResponse](../CommonObjectReference/CommonObjectReference.md#V2CountReportConfigurationsResponse_CommonObjectReference)

<a id="_content_type_2"></a>

## Content Type

- application/json

<a id="_responses_2"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V2CountReportConfigurationsResponse](../CommonObjectReference/CommonObjectReference.md#V2CountReportConfigurationsResponse_CommonObjectReference) |
| 0 | An unexpected error response. | [RpcStatus](../CommonObjectReference/CommonObjectReference.md#RpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_2"></a>

## Samples

<a id="DeleteReport_ReportService"></a>

# DeleteReport

`DELETE /v2/reports/jobs/{id}/delete`

Deletes a generated report for the given report id

<a id="_description_3"></a>

## Description

<a id="_parameters_3"></a>

## Parameters

<a id="_path_parameters_2"></a>

### Path Parameters

| Name | Description | Required | Default | Pattern |
|------|-------------|----------|---------|---------|
| id   |             | X        | null    |         |

<a id="_return_type_3"></a>

## Return Type

`Object`

<a id="_content_type_3"></a>

## Content Type

- application/json

<a id="_responses_3"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | `Object` |
| 0 | An unexpected error response. | [RpcStatus](../CommonObjectReference/CommonObjectReference.md#RpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_3"></a>

## Samples

<a id="DeleteReportConfiguration_ReportService"></a>

# DeleteReportConfiguration

`DELETE /v2/reports/configurations/{id}`

DeleteReportConfiguration removes the report configuration with given ID

<a id="_description_4"></a>

## Description

<a id="_parameters_4"></a>

## Parameters

<a id="_path_parameters_3"></a>

### Path Parameters

| Name | Description | Required | Default | Pattern |
|------|-------------|----------|---------|---------|
| id   |             | X        | null    |         |

<a id="_return_type_4"></a>

## Return Type

`Object`

<a id="_content_type_4"></a>

## Content Type

- application/json

<a id="_responses_4"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | `Object` |
| 0 | An unexpected error response. | [RpcStatus](../CommonObjectReference/CommonObjectReference.md#RpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_4"></a>

## Samples

<a id="GetMyReportHistory_ReportService"></a>

# GetMyReportHistory

`GET /v2/reports/configurations/{id}/my-history`

GetMyReportHistory returns the requester’s report job history for a report configuration with the specified ID.

<a id="_description_5"></a>

## Description

<a id="_parameters_5"></a>

## Parameters

<a id="_path_parameters_4"></a>

### Path Parameters

| Name | Description | Required | Default | Pattern |
|------|-------------|----------|---------|---------|
| id   |             | X        | null    |         |

<a id="_query_parameters_2"></a>

### Query Parameters

| Name | Description | Required | Default | Pattern |
|----|----|----|----|----|
| reportParamQuery.query |  | \- | null |  |
| reportParamQuery.pagination.limit |  | \- | null |  |
| reportParamQuery.pagination.offset |  | \- | null |  |
| reportParamQuery.pagination.sortOption.field |  | \- | null |  |
| reportParamQuery.pagination.sortOption.reversed |  | \- | null |  |
| reportParamQuery.pagination.sortOption.aggregateBy.aggrFunc |  | \- | UNSET |  |
| reportParamQuery.pagination.sortOption.aggregateBy.distinct |  | \- | null |  |

<a id="_return_type_5"></a>

## Return Type

[V2ReportHistoryResponse](../CommonObjectReference/CommonObjectReference.md#V2ReportHistoryResponse_CommonObjectReference)

<a id="_content_type_5"></a>

## Content Type

- application/json

<a id="_responses_5"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V2ReportHistoryResponse](../CommonObjectReference/CommonObjectReference.md#V2ReportHistoryResponse_CommonObjectReference) |
| 0 | An unexpected error response. | [RpcStatus](../CommonObjectReference/CommonObjectReference.md#RpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_5"></a>

## Samples

<a id="GetReportConfiguration_ReportService"></a>

# GetReportConfiguration

`GET /v2/reports/configurations/{id}`

GetReportConfiguration returns the report configuration with given ID

<a id="_description_6"></a>

## Description

<a id="_parameters_6"></a>

## Parameters

<a id="_path_parameters_5"></a>

### Path Parameters

| Name | Description | Required | Default | Pattern |
|------|-------------|----------|---------|---------|
| id   |             | X        | null    |         |

<a id="_return_type_6"></a>

## Return Type

[V2ReportConfiguration](../CommonObjectReference/CommonObjectReference.md#V2ReportConfiguration_CommonObjectReference)

<a id="_content_type_6"></a>

## Content Type

- application/json

<a id="_responses_6"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V2ReportConfiguration](../CommonObjectReference/CommonObjectReference.md#V2ReportConfiguration_CommonObjectReference) |
| 0 | An unexpected error response. | [RpcStatus](../CommonObjectReference/CommonObjectReference.md#RpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_6"></a>

## Samples

<a id="GetReportHistory_ReportService"></a>

# GetReportHistory

`GET /v2/reports/configurations/{id}/history`

GetReportHistory returns the full report job history for a report configuration with the specified ID.

<a id="_description_7"></a>

## Description

<a id="_parameters_7"></a>

## Parameters

<a id="_path_parameters_6"></a>

### Path Parameters

| Name | Description | Required | Default | Pattern |
|------|-------------|----------|---------|---------|
| id   |             | X        | null    |         |

<a id="_query_parameters_3"></a>

### Query Parameters

| Name | Description | Required | Default | Pattern |
|----|----|----|----|----|
| reportParamQuery.query |  | \- | null |  |
| reportParamQuery.pagination.limit |  | \- | null |  |
| reportParamQuery.pagination.offset |  | \- | null |  |
| reportParamQuery.pagination.sortOption.field |  | \- | null |  |
| reportParamQuery.pagination.sortOption.reversed |  | \- | null |  |
| reportParamQuery.pagination.sortOption.aggregateBy.aggrFunc |  | \- | UNSET |  |
| reportParamQuery.pagination.sortOption.aggregateBy.distinct |  | \- | null |  |

<a id="_return_type_7"></a>

## Return Type

[V2ReportHistoryResponse](../CommonObjectReference/CommonObjectReference.md#V2ReportHistoryResponse_CommonObjectReference)

<a id="_content_type_7"></a>

## Content Type

- application/json

<a id="_responses_7"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V2ReportHistoryResponse](../CommonObjectReference/CommonObjectReference.md#V2ReportHistoryResponse_CommonObjectReference) |
| 0 | An unexpected error response. | [RpcStatus](../CommonObjectReference/CommonObjectReference.md#RpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_7"></a>

## Samples

<a id="GetReportStatus_ReportService"></a>

# GetReportStatus

`GET /v2/reports/jobs/{id}/status`

GetReportStatus returns report status for the given report id

<a id="_description_8"></a>

## Description

<a id="_parameters_8"></a>

## Parameters

<a id="_path_parameters_7"></a>

### Path Parameters

| Name | Description | Required | Default | Pattern |
|------|-------------|----------|---------|---------|
| id   |             | X        | null    |         |

<a id="_return_type_8"></a>

## Return Type

[V2ReportStatusResponse](../CommonObjectReference/CommonObjectReference.md#V2ReportStatusResponse_CommonObjectReference)

<a id="_content_type_8"></a>

## Content Type

- application/json

<a id="_responses_8"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V2ReportStatusResponse](../CommonObjectReference/CommonObjectReference.md#V2ReportStatusResponse_CommonObjectReference) |
| 0 | An unexpected error response. | [RpcStatus](../CommonObjectReference/CommonObjectReference.md#RpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_8"></a>

## Samples

<a id="GetViewBasedMyReportHistory_ReportService"></a>

# GetViewBasedMyReportHistory

`GET /v2/reports/view-based/my-history`

<a id="_description_9"></a>

## Description

<a id="_parameters_9"></a>

## Parameters

<a id="_query_parameters_4"></a>

### Query Parameters

| Name | Description | Required | Default | Pattern |
|----|----|----|----|----|
| reportParamQuery.query |  | \- | null |  |
| reportParamQuery.pagination.limit |  | \- | null |  |
| reportParamQuery.pagination.offset |  | \- | null |  |
| reportParamQuery.pagination.sortOption.field |  | \- | null |  |
| reportParamQuery.pagination.sortOption.reversed |  | \- | null |  |
| reportParamQuery.pagination.sortOption.aggregateBy.aggrFunc |  | \- | UNSET |  |
| reportParamQuery.pagination.sortOption.aggregateBy.distinct |  | \- | null |  |

<a id="_return_type_9"></a>

## Return Type

[V2ReportHistoryResponse](../CommonObjectReference/CommonObjectReference.md#V2ReportHistoryResponse_CommonObjectReference)

<a id="_content_type_9"></a>

## Content Type

- application/json

<a id="_responses_9"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V2ReportHistoryResponse](../CommonObjectReference/CommonObjectReference.md#V2ReportHistoryResponse_CommonObjectReference) |
| 0 | An unexpected error response. | [RpcStatus](../CommonObjectReference/CommonObjectReference.md#RpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_9"></a>

## Samples

<a id="GetViewBasedReportHistory_ReportService"></a>

# GetViewBasedReportHistory

`GET /v2/reports/view-based/history`

<a id="_description_10"></a>

## Description

<a id="_parameters_10"></a>

## Parameters

<a id="_query_parameters_5"></a>

### Query Parameters

| Name | Description | Required | Default | Pattern |
|----|----|----|----|----|
| reportParamQuery.query |  | \- | null |  |
| reportParamQuery.pagination.limit |  | \- | null |  |
| reportParamQuery.pagination.offset |  | \- | null |  |
| reportParamQuery.pagination.sortOption.field |  | \- | null |  |
| reportParamQuery.pagination.sortOption.reversed |  | \- | null |  |
| reportParamQuery.pagination.sortOption.aggregateBy.aggrFunc |  | \- | UNSET |  |
| reportParamQuery.pagination.sortOption.aggregateBy.distinct |  | \- | null |  |

<a id="_return_type_10"></a>

## Return Type

[V2ReportHistoryResponse](../CommonObjectReference/CommonObjectReference.md#V2ReportHistoryResponse_CommonObjectReference)

<a id="_content_type_10"></a>

## Content Type

- application/json

<a id="_responses_10"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V2ReportHistoryResponse](../CommonObjectReference/CommonObjectReference.md#V2ReportHistoryResponse_CommonObjectReference) |
| 0 | An unexpected error response. | [RpcStatus](../CommonObjectReference/CommonObjectReference.md#RpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_10"></a>

## Samples

<a id="ListReportConfigurations_ReportService"></a>

# ListReportConfigurations

`GET /v2/reports/configurations`

ListReportConfigurations returns report configurations matching given query

<a id="_description_11"></a>

## Description

<a id="_parameters_11"></a>

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

<a id="_return_type_11"></a>

## Return Type

[V2ListReportConfigurationsResponse](../CommonObjectReference/CommonObjectReference.md#V2ListReportConfigurationsResponse_CommonObjectReference)

<a id="_content_type_11"></a>

## Content Type

- application/json

<a id="_responses_11"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V2ListReportConfigurationsResponse](../CommonObjectReference/CommonObjectReference.md#V2ListReportConfigurationsResponse_CommonObjectReference) |
| 0 | An unexpected error response. | [RpcStatus](../CommonObjectReference/CommonObjectReference.md#RpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_11"></a>

## Samples

<a id="PostReportConfiguration_ReportService"></a>

# PostReportConfiguration

`POST /v2/reports/configurations`

PostReportConfiguration creates a report configuration

<a id="_description_12"></a>

## Description

<a id="_parameters_12"></a>

## Parameters

<a id="_body_parameter"></a>

### Body Parameter

| Name | Description | Required | Default | Pattern |
|----|----|----|----|----|
| body | [V2ReportConfiguration](../CommonObjectReference/CommonObjectReference.md#V2ReportConfiguration_CommonObjectReference) | X |  |  |

<a id="_return_type_12"></a>

## Return Type

[V2ReportConfiguration](../CommonObjectReference/CommonObjectReference.md#V2ReportConfiguration_CommonObjectReference)

<a id="_content_type_12"></a>

## Content Type

- application/json

<a id="_responses_12"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V2ReportConfiguration](../CommonObjectReference/CommonObjectReference.md#V2ReportConfiguration_CommonObjectReference) |
| 0 | An unexpected error response. | [RpcStatus](../CommonObjectReference/CommonObjectReference.md#RpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_12"></a>

## Samples

<a id="PostViewBasedReport_ReportService"></a>

# PostViewBasedReport

`POST /v2/reports/view-based/run`

<a id="_description_13"></a>

## Description

<a id="_parameters_13"></a>

## Parameters

<a id="_body_parameter_2"></a>

### Body Parameter

| Name | Description | Required | Default | Pattern |
|----|----|----|----|----|
| body | [V2ReportRequestViewBased](../CommonObjectReference/CommonObjectReference.md#V2ReportRequestViewBased_CommonObjectReference) | X |  |  |

<a id="_return_type_13"></a>

## Return Type

[V2RunReportResponseViewBased](../CommonObjectReference/CommonObjectReference.md#V2RunReportResponseViewBased_CommonObjectReference)

<a id="_content_type_13"></a>

## Content Type

- application/json

<a id="_responses_13"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V2RunReportResponseViewBased](../CommonObjectReference/CommonObjectReference.md#V2RunReportResponseViewBased_CommonObjectReference) |
| 0 | An unexpected error response. | [RpcStatus](../CommonObjectReference/CommonObjectReference.md#RpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_13"></a>

## Samples

<a id="RunReport_ReportService"></a>

# RunReport

`POST /v2/reports/run`

Submits a new report generation request if the user requesting this report does not have another waiting or preparing report for the same report configuration.

<a id="_description_14"></a>

## Description

<a id="_parameters_14"></a>

## Parameters

<a id="_body_parameter_3"></a>

### Body Parameter

| Name | Description | Required | Default | Pattern |
|----|----|----|----|----|
| body | [V2RunReportRequest](../CommonObjectReference/CommonObjectReference.md#V2RunReportRequest_CommonObjectReference) | X |  |  |

<a id="_return_type_14"></a>

## Return Type

[V2RunReportResponse](../CommonObjectReference/CommonObjectReference.md#V2RunReportResponse_CommonObjectReference)

<a id="_content_type_14"></a>

## Content Type

- application/json

<a id="_responses_14"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V2RunReportResponse](../CommonObjectReference/CommonObjectReference.md#V2RunReportResponse_CommonObjectReference) |
| 0 | An unexpected error response. | [RpcStatus](../CommonObjectReference/CommonObjectReference.md#RpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_14"></a>

## Samples

<a id="UpdateReportConfiguration_ReportService"></a>

# UpdateReportConfiguration

`PUT /v2/reports/configurations/{id}`

UpdateReportConfiguration updates a report configuration

<a id="_description_15"></a>

## Description

<a id="_parameters_15"></a>

## Parameters

<a id="_path_parameters_8"></a>

### Path Parameters

| Name | Description | Required | Default | Pattern |
|------|-------------|----------|---------|---------|
| id   |             | X        | null    |         |

<a id="_body_parameter_4"></a>

### Body Parameter

| Name | Description | Required | Default | Pattern |
|----|----|----|----|----|
| body | [ReportServiceUpdateReportConfigurationBody](../CommonObjectReference/CommonObjectReference.md#ReportServiceUpdateReportConfigurationBody_CommonObjectReference) | X |  |  |

<a id="_return_type_15"></a>

## Return Type

`Object`

<a id="_content_type_15"></a>

## Content Type

- application/json

<a id="_responses_15"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | `Object` |
| 0 | An unexpected error response. | [RpcStatus](../CommonObjectReference/CommonObjectReference.md#RpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_15"></a>

## Samples
