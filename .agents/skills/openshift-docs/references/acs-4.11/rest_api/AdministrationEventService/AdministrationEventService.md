<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

<a id="CountAdministrationEvents_AdministrationEventService"></a>

# CountAdministrationEvents

`GET /v1/count/administration/events`

CountAdministrationEvents returns the number of events after filtering by requested fields.

<a id="_description"></a>

## Description

<a id="_parameters"></a>

## Parameters

<a id="_query_parameters"></a>

### Query Parameters

| Name | Description | Required | Default | Pattern |
|----|----|----|----|----|
| filter.from | Matches events with last_occurred_at after a specific timestamp, i.e. the lower boundary. | \- | null |  |
| filter.until | Matches events with last_occurred_at before a specific timestamp, i.e. the upper boundary. | \- | null |  |
| filter.domain | Matches events from a specific domain. `String` | \- | null |  |
| filter.resourceType | Matches events associated with a specific resource type. `String` | \- | null |  |
| filter.type | Matches events based on their type. `String` | \- | null |  |
| filter.level | Matches events based on their level. `String` | \- | null |  |

<a id="_return_type"></a>

## Return Type

[V1CountAdministrationEventsResponse](../CommonObjectReference/CommonObjectReference.md#V1CountAdministrationEventsResponse_CommonObjectReference)

<a id="_content_type"></a>

## Content Type

- application/json

<a id="_responses"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V1CountAdministrationEventsResponse](../CommonObjectReference/CommonObjectReference.md#V1CountAdministrationEventsResponse_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples"></a>

## Samples

<a id="GetAdministrationEvent_AdministrationEventService"></a>

# GetAdministrationEvent

`GET /v1/administration/events/{id}`

GetAdministrationEvent retrieves an event by ID.

<a id="_description_2"></a>

## Description

<a id="_parameters_2"></a>

## Parameters

<a id="_path_parameters"></a>

### Path Parameters

| Name | Description | Required | Default | Pattern |
|------|-------------|----------|---------|---------|
| id   |             | X        | null    |         |

<a id="_return_type_2"></a>

## Return Type

[V1GetAdministrationEventResponse](../CommonObjectReference/CommonObjectReference.md#V1GetAdministrationEventResponse_CommonObjectReference)

<a id="_content_type_2"></a>

## Content Type

- application/json

<a id="_responses_2"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V1GetAdministrationEventResponse](../CommonObjectReference/CommonObjectReference.md#V1GetAdministrationEventResponse_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_2"></a>

## Samples

<a id="ListAdministrationEvents_AdministrationEventService"></a>

# ListAdministrationEvents

`GET /v1/administration/events`

ListAdministrationEvents returns the list of events after filtered by requested fields.

<a id="_description_3"></a>

## Description

<a id="_parameters_3"></a>

## Parameters

<a id="_query_parameters_2"></a>

### Query Parameters

| Name | Description | Required | Default | Pattern |
|----|----|----|----|----|
| pagination.limit |  | \- | null |  |
| pagination.offset |  | \- | null |  |
| pagination.sortOption.field |  | \- | null |  |
| pagination.sortOption.reversed |  | \- | null |  |
| pagination.sortOption.aggregateBy.aggrFunc |  | \- | UNSET |  |
| pagination.sortOption.aggregateBy.distinct |  | \- | null |  |
| filter.from | Matches events with last_occurred_at after a specific timestamp, i.e. the lower boundary. | \- | null |  |
| filter.until | Matches events with last_occurred_at before a specific timestamp, i.e. the upper boundary. | \- | null |  |
| filter.domain | Matches events from a specific domain. `String` | \- | null |  |
| filter.resourceType | Matches events associated with a specific resource type. `String` | \- | null |  |
| filter.type | Matches events based on their type. `String` | \- | null |  |
| filter.level | Matches events based on their level. `String` | \- | null |  |

<a id="_return_type_3"></a>

## Return Type

[V1ListAdministrationEventsResponse](../CommonObjectReference/CommonObjectReference.md#V1ListAdministrationEventsResponse_CommonObjectReference)

<a id="_content_type_3"></a>

## Content Type

- application/json

<a id="_responses_3"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V1ListAdministrationEventsResponse](../CommonObjectReference/CommonObjectReference.md#V1ListAdministrationEventsResponse_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_3"></a>

## Samples
