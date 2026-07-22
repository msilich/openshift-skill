<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Description
Event is a report of an event somewhere in the cluster. It generally denotes some state change in the system. Events have a limited retention time and triggers and messages may evolve with time. Event consumers should not rely on the timing of an event with a given Reason reflecting a consistent underlying trigger, or the continued existence of events with that Reason. Events should be treated as informative, best-effort, supplemental data.

Type
`object`

Required
- `eventTime`

# Specification

| Property | Type | Description |
|----|----|----|
| `action` | `string` | action is what action was taken/failed regarding to the regarding object. It is machine-readable. This field cannot be empty for new Events and it can have at most 128 characters. |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `deprecatedCount` | `integer` | deprecatedCount is the deprecated field assuring backward compatibility with core.v1 Event type. |
| `deprecatedFirstTimestamp` | [`Time`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-Time) | deprecatedFirstTimestamp is the deprecated field assuring backward compatibility with core.v1 Event type. |
| `deprecatedLastTimestamp` | [`Time`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-Time) | deprecatedLastTimestamp is the deprecated field assuring backward compatibility with core.v1 Event type. |
| `deprecatedSource` | [`EventSource`](../objects/index.md#io-k8s-api-core-v1-EventSource) | deprecatedSource is the deprecated field assuring backward compatibility with core.v1 Event type. |
| `eventTime` | [`MicroTime`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-MicroTime) | eventTime is the time when this Event was first observed. It is required. |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ObjectMeta`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) | Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |
| `note` | `string` | note is a human-readable description of the status of this operation. Maximal length of the note is 1kB, but libraries should be prepared to handle values up to 64kB. |
| `reason` | `string` | reason is why the action was taken. It is human-readable. This field cannot be empty for new Events and it can have at most 128 characters. |
| `regarding` | [`ObjectReference`](../objects/index.md#io-k8s-api-core-v1-ObjectReference) | regarding contains the object this Event is about. In most cases it’s an Object reporting controller implements, e.g. ReplicaSetController implements ReplicaSets and this event is emitted because it acts on some changes in a ReplicaSet object. |
| `related` | [`ObjectReference`](../objects/index.md#io-k8s-api-core-v1-ObjectReference) | related is the optional secondary object for more complex actions. E.g. when regarding object triggers a creation or deletion of related object. |
| `reportingController` | `string` | reportingController is the name of the controller that emitted this Event, e.g. `kubernetes.io/kubelet`. This field cannot be empty for new Events. |
| `reportingInstance` | `string` | reportingInstance is the ID of the controller instance, e.g. `kubelet-xyzf`. This field cannot be empty for new Events and it can have at most 128 characters. |
| `series` | `object` | EventSeries contain information on series of events, i.e. thing that was/is happening continuously for some time. How often to update the EventSeries is up to the event reporters. The default event reporter in "k8s.io/client-go/tools/events/event_broadcaster.go" shows how this struct is updated on heartbeats and can guide customized reporter implementations. |
| `type` | `string` | type is the type of this event (Normal, Warning), new types could be added in the future. It is machine-readable. This field cannot be empty for new Events. |

## .series

Description
EventSeries contain information on series of events, i.e. thing that was/is happening continuously for some time. How often to update the EventSeries is up to the event reporters. The default event reporter in "k8s.io/client-go/tools/events/event_broadcaster.go" shows how this struct is updated on heartbeats and can guide customized reporter implementations.

Type
`object`

Required
- `count`

- `lastObservedTime`

| Property | Type | Description |
|----|----|----|
| `count` | `integer` | count is the number of occurrences in this series up to the last heartbeat time. |
| `lastObservedTime` | [`MicroTime`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-MicroTime) | lastObservedTime is the time when last Event from the series was seen before last heartbeat. |

# API endpoints

The following API endpoints are available:

- `/apis/events.k8s.io/v1/events`

  - `GET`: list or watch objects of kind Event

- `/apis/events.k8s.io/v1/watch/events`

  - `GET`: watch individual changes to a list of Event. deprecated: use the 'watch' parameter with a list operation instead.

- `/apis/events.k8s.io/v1/namespaces/{namespace}/events`

  - `DELETE`: delete collection of Event

  - `GET`: list or watch objects of kind Event

  - `POST`: create an Event

- `/apis/events.k8s.io/v1/watch/namespaces/{namespace}/events`

  - `GET`: watch individual changes to a list of Event. deprecated: use the 'watch' parameter with a list operation instead.

- `/apis/events.k8s.io/v1/namespaces/{namespace}/events/{name}`

  - `DELETE`: delete an Event

  - `GET`: read the specified Event

  - `PATCH`: partially update the specified Event

  - `PUT`: replace the specified Event

- `/apis/events.k8s.io/v1/watch/namespaces/{namespace}/events/{name}`

  - `GET`: watch changes to an object of kind Event. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.

## /apis/events.k8s.io/v1/events

HTTP method
`GET`

Description
list or watch objects of kind Event

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`EventList`](../objects/index.md#io-k8s-api-events-v1-EventList) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/events.k8s.io/v1/watch/events

HTTP method
`GET`

Description
watch individual changes to a list of Event. deprecated: use the 'watch' parameter with a list operation instead.

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`WatchEvent`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/events.k8s.io/v1/namespaces/{namespace}/events

HTTP method
`DELETE`

Description
delete collection of Event

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |

Query parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Status`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`GET`

Description
list or watch objects of kind Event

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`EventList`](../objects/index.md#io-k8s-api-events-v1-EventList) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`POST`

Description
create an Event

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`Event`](event-events-k8s-io-v1.md#event-events-k8s-io-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Event`](event-events-k8s-io-v1.md#event-events-k8s-io-v1) schema |
| 201 - Created | [`Event`](event-events-k8s-io-v1.md#event-events-k8s-io-v1) schema |
| 202 - Accepted | [`Event`](event-events-k8s-io-v1.md#event-events-k8s-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/events.k8s.io/v1/watch/namespaces/{namespace}/events

HTTP method
`GET`

Description
watch individual changes to a list of Event. deprecated: use the 'watch' parameter with a list operation instead.

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`WatchEvent`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/events.k8s.io/v1/namespaces/{namespace}/events/{name}

| Parameter | Type     | Description       |
|-----------|----------|-------------------|
| `name`    | `string` | name of the Event |

Global path parameters

HTTP method
`DELETE`

Description
delete an Event

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |

Query parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Status`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 202 - Accepted | [`Status`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`GET`

Description
read the specified Event

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Event`](event-events-k8s-io-v1.md#event-events-k8s-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PATCH`

Description
partially update the specified Event

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Event`](event-events-k8s-io-v1.md#event-events-k8s-io-v1) schema |
| 201 - Created | [`Event`](event-events-k8s-io-v1.md#event-events-k8s-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PUT`

Description
replace the specified Event

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`Event`](event-events-k8s-io-v1.md#event-events-k8s-io-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Event`](event-events-k8s-io-v1.md#event-events-k8s-io-v1) schema |
| 201 - Created | [`Event`](event-events-k8s-io-v1.md#event-events-k8s-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/events.k8s.io/v1/watch/namespaces/{namespace}/events/{name}

| Parameter | Type     | Description       |
|-----------|----------|-------------------|
| `name`    | `string` | name of the Event |

Global path parameters

HTTP method
`GET`

Description
watch changes to an object of kind Event. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`WatchEvent`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema |
| 401 - Unauthorized | Empty |

HTTP responses
