<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

<a id="DeleteNotifier_NotifierService"></a>

# DeleteNotifier

`DELETE /v1/notifiers/{id}`

DeleteNotifier removes a notifier configuration given its ID.

<a id="_description"></a>

## Description

<a id="_parameters"></a>

## Parameters

<a id="_path_parameters"></a>

### Path Parameters

| Name | Description | Required | Default | Pattern |
|------|-------------|----------|---------|---------|
| id   |             | X        | null    |         |

<a id="_query_parameters"></a>

### Query Parameters

| Name  | Description | Required | Default | Pattern |
|-------|-------------|----------|---------|---------|
| force |             | \-       | null    |         |

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
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples"></a>

## Samples

<a id="GetNotifier_NotifierService"></a>

# GetNotifier

`GET /v1/notifiers/{id}`

GetNotifier returns the notifier configuration given its ID.

<a id="_description_2"></a>

## Description

<a id="_parameters_2"></a>

## Parameters

<a id="_path_parameters_2"></a>

### Path Parameters

| Name | Description | Required | Default | Pattern |
|------|-------------|----------|---------|---------|
| id   |             | X        | null    |         |

<a id="_return_type_2"></a>

## Return Type

[StorageNotifier](../CommonObjectReference/CommonObjectReference.md#StorageNotifier_CommonObjectReference)

<a id="_content_type_2"></a>

## Content Type

- application/json

<a id="_responses_2"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [StorageNotifier](../CommonObjectReference/CommonObjectReference.md#StorageNotifier_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_2"></a>

## Samples

<a id="GetNotifiers_NotifierService"></a>

# GetNotifiers

`GET /v1/notifiers`

GetNotifiers returns all notifier configurations.

<a id="_description_3"></a>

## Description

<a id="_parameters_3"></a>

## Parameters

<a id="_return_type_3"></a>

## Return Type

[V1GetNotifiersResponse](../CommonObjectReference/CommonObjectReference.md#V1GetNotifiersResponse_CommonObjectReference)

<a id="_content_type_3"></a>

## Content Type

- application/json

<a id="_responses_3"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V1GetNotifiersResponse](../CommonObjectReference/CommonObjectReference.md#V1GetNotifiersResponse_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_3"></a>

## Samples

<a id="PostNotifier_NotifierService"></a>

# PostNotifier

`POST /v1/notifiers`

PostNotifier creates a notifier configuration.

<a id="_description_4"></a>

## Description

<a id="_parameters_4"></a>

## Parameters

<a id="_body_parameter"></a>

### Body Parameter

| Name | Description | Required | Default | Pattern |
|----|----|----|----|----|
| body | [StorageNotifier](../CommonObjectReference/CommonObjectReference.md#StorageNotifier_CommonObjectReference) | X |  |  |

<a id="_return_type_4"></a>

## Return Type

[StorageNotifier](../CommonObjectReference/CommonObjectReference.md#StorageNotifier_CommonObjectReference)

<a id="_content_type_4"></a>

## Content Type

- application/json

<a id="_responses_4"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [StorageNotifier](../CommonObjectReference/CommonObjectReference.md#StorageNotifier_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_4"></a>

## Samples

<a id="PutNotifier_NotifierService"></a>

# PutNotifier

`PUT /v1/notifiers/{id}`

PutNotifier modifies a given notifier, without using stored credential reconciliation.

<a id="_description_5"></a>

## Description

<a id="_parameters_5"></a>

## Parameters

<a id="_path_parameters_3"></a>

### Path Parameters

| Name | Description | Required | Default | Pattern |
|------|-------------|----------|---------|---------|
| id   |             | X        | null    |         |

<a id="_body_parameter_2"></a>

### Body Parameter

| Name | Description | Required | Default | Pattern |
|----|----|----|----|----|
| body | [NotifierServicePutNotifierBody](../CommonObjectReference/CommonObjectReference.md#NotifierServicePutNotifierBody_CommonObjectReference) | X |  |  |

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

<a id="TestNotifier_NotifierService"></a>

# TestNotifier

`POST /v1/notifiers/test`

TestNotifier checks if a notifier is correctly configured.

<a id="_description_6"></a>

## Description

<a id="_parameters_6"></a>

## Parameters

<a id="_body_parameter_3"></a>

### Body Parameter

| Name | Description | Required | Default | Pattern |
|----|----|----|----|----|
| body | [StorageNotifier](../CommonObjectReference/CommonObjectReference.md#StorageNotifier_CommonObjectReference) | X |  |  |

<a id="_return_type_6"></a>

## Return Type

`Object`

<a id="_content_type_6"></a>

## Content Type

- application/json

<a id="_responses_6"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | `Object` |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_6"></a>

## Samples

<a id="TestUpdatedNotifier_NotifierService"></a>

# TestUpdatedNotifier

`POST /v1/notifiers/test/updated`

TestUpdatedNotifier checks if the given notifier is correctly configured, with optional stored credential reconciliation.

<a id="_description_7"></a>

## Description

<a id="_parameters_7"></a>

## Parameters

<a id="_body_parameter_4"></a>

### Body Parameter

| Name | Description | Required | Default | Pattern |
|----|----|----|----|----|
| body | [V1UpdateNotifierRequest](../CommonObjectReference/CommonObjectReference.md#V1UpdateNotifierRequest_CommonObjectReference) | X |  |  |

<a id="_return_type_7"></a>

## Return Type

`Object`

<a id="_content_type_7"></a>

## Content Type

- application/json

<a id="_responses_7"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | `Object` |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_7"></a>

## Samples

<a id="UpdateNotifier_NotifierService"></a>

# UpdateNotifier

`PATCH /v1/notifiers/{notifier.id}`

UpdateNotifier modifies a given notifier, with optional stored credential reconciliation.

<a id="_description_8"></a>

## Description

<a id="_parameters_8"></a>

## Parameters

<a id="_path_parameters_4"></a>

### Path Parameters

| Name        | Description | Required | Default | Pattern |
|-------------|-------------|----------|---------|---------|
| notifier.id |             | X        | null    |         |

<a id="_body_parameter_5"></a>

### Body Parameter

| Name | Description | Required | Default | Pattern |
|----|----|----|----|----|
| body | [NotifierServiceUpdateNotifierBody](../CommonObjectReference/CommonObjectReference.md#NotifierServiceUpdateNotifierBody_CommonObjectReference) | X |  |  |

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
