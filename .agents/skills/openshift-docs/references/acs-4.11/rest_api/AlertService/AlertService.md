<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

<a id="CountAlerts_AlertService"></a>

# CountAlerts

`GET /v1/alertscount`

CountAlerts counts how many alerts match the get request.

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

[V1CountAlertsResponse](../CommonObjectReference/CommonObjectReference.md#V1CountAlertsResponse_CommonObjectReference)

<a id="_content_type"></a>

## Content Type

- application/json

<a id="_responses"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V1CountAlertsResponse](../CommonObjectReference/CommonObjectReference.md#V1CountAlertsResponse_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples"></a>

## Samples

<a id="DeleteAlerts_AlertService"></a>

# DeleteAlerts

`DELETE /v1/alerts`

<a id="_description_2"></a>

## Description

<a id="_parameters_2"></a>

## Parameters

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
| confirm |  | \- | null |  |

<a id="_return_type_2"></a>

## Return Type

[V1DeleteAlertsResponse](../CommonObjectReference/CommonObjectReference.md#V1DeleteAlertsResponse_CommonObjectReference)

<a id="_content_type_2"></a>

## Content Type

- application/json

<a id="_responses_2"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V1DeleteAlertsResponse](../CommonObjectReference/CommonObjectReference.md#V1DeleteAlertsResponse_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_2"></a>

## Samples

<a id="GetAlert_AlertService"></a>

# GetAlert

`GET /v1/alerts/{id}`

GetAlert returns the alert given its id.

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

[StorageAlert](../CommonObjectReference/CommonObjectReference.md#StorageAlert_CommonObjectReference)

<a id="_content_type_3"></a>

## Content Type

- application/json

<a id="_responses_3"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [StorageAlert](../CommonObjectReference/CommonObjectReference.md#StorageAlert_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_3"></a>

## Samples

<a id="GetAlertTimeseries_AlertService"></a>

# GetAlertTimeseries

`GET /v1/alerts/summary/timeseries`

GetAlertTimeseries returns the alerts sorted by time.

<a id="_description_4"></a>

## Description

<a id="_parameters_4"></a>

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

<a id="_return_type_4"></a>

## Return Type

[V1GetAlertTimeseriesResponse](../CommonObjectReference/CommonObjectReference.md#V1GetAlertTimeseriesResponse_CommonObjectReference)

<a id="_content_type_4"></a>

## Content Type

- application/json

<a id="_responses_4"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V1GetAlertTimeseriesResponse](../CommonObjectReference/CommonObjectReference.md#V1GetAlertTimeseriesResponse_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_4"></a>

## Samples

<a id="GetAlertsCounts_AlertService"></a>

# GetAlertsCounts

`GET /v1/alerts/summary/counts`

GetAlertsCounts returns the number of alerts in the requested cluster or category.

<a id="_description_5"></a>

## Description

<a id="_parameters_5"></a>

## Parameters

<a id="_query_parameters_4"></a>

### Query Parameters

| Name | Description | Required | Default | Pattern |
|----|----|----|----|----|
| request.query |  | \- | null |  |
| request.pagination.limit |  | \- | null |  |
| request.pagination.offset |  | \- | null |  |
| request.pagination.sortOption.field |  | \- | null |  |
| request.pagination.sortOption.reversed |  | \- | null |  |
| request.pagination.sortOption.aggregateBy.aggrFunc |  | \- | UNSET |  |
| request.pagination.sortOption.aggregateBy.distinct |  | \- | null |  |
| groupBy |  | \- | UNSET |  |

<a id="_return_type_5"></a>

## Return Type

[V1GetAlertsCountsResponse](../CommonObjectReference/CommonObjectReference.md#V1GetAlertsCountsResponse_CommonObjectReference)

<a id="_content_type_5"></a>

## Content Type

- application/json

<a id="_responses_5"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V1GetAlertsCountsResponse](../CommonObjectReference/CommonObjectReference.md#V1GetAlertsCountsResponse_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_5"></a>

## Samples

<a id="GetAlertsGroup_AlertService"></a>

# GetAlertsGroup

`GET /v1/alerts/summary/groups`

GetAlertsGroup returns alerts grouped by policy.

<a id="_description_6"></a>

## Description

<a id="_parameters_6"></a>

## Parameters

<a id="_query_parameters_5"></a>

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

<a id="_return_type_6"></a>

## Return Type

[V1GetAlertsGroupResponse](../CommonObjectReference/CommonObjectReference.md#V1GetAlertsGroupResponse_CommonObjectReference)

<a id="_content_type_6"></a>

## Content Type

- application/json

<a id="_responses_6"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V1GetAlertsGroupResponse](../CommonObjectReference/CommonObjectReference.md#V1GetAlertsGroupResponse_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_6"></a>

## Samples

<a id="ListAlerts_AlertService"></a>

# ListAlerts

`GET /v1/alerts`

List returns the slim list version of the alerts.

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

[V1ListAlertsResponse](../CommonObjectReference/CommonObjectReference.md#V1ListAlertsResponse_CommonObjectReference)

<a id="_content_type_7"></a>

## Content Type

- application/json

<a id="_responses_7"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V1ListAlertsResponse](../CommonObjectReference/CommonObjectReference.md#V1ListAlertsResponse_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_7"></a>

## Samples

<a id="ResolveAlert_AlertService"></a>

# ResolveAlert

`PATCH /v1/alerts/{id}/resolve`

ResolveAlert marks the given alert (by ID) as resolved.

<a id="_description_8"></a>

## Description

<a id="_parameters_8"></a>

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
| body | [AlertServiceResolveAlertBody](../CommonObjectReference/CommonObjectReference.md#AlertServiceResolveAlertBody_CommonObjectReference) | X |  |  |

<a id="_return_type_8"></a>

## Return Type

`Object`

<a id="_content_type_8"></a>

## Content Type

- application/json

<a id="_responses_8"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | `Object` |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_8"></a>

## Samples

<a id="ResolveAlerts_AlertService"></a>

# ResolveAlerts

`PATCH /v1/alerts/resolve`

ResolveAlertsByQuery marks alerts matching search query as resolved.

<a id="_description_9"></a>

## Description

<a id="_parameters_9"></a>

## Parameters

<a id="_body_parameter_2"></a>

### Body Parameter

| Name | Description | Required | Default | Pattern |
|----|----|----|----|----|
| body | [V1ResolveAlertsRequest](../CommonObjectReference/CommonObjectReference.md#V1ResolveAlertsRequest_CommonObjectReference) | X |  |  |

<a id="_return_type_9"></a>

## Return Type

`Object`

<a id="_content_type_9"></a>

## Content Type

- application/json

<a id="_responses_9"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | `Object` |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_9"></a>

## Samples
