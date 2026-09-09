<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

<a id="DeleteExternalBackup_ExternalBackupService"></a>

# DeleteExternalBackup

`DELETE /v1/externalbackups/{id}`

DeleteExternalBackup removes an external backup configuration given its ID.

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
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples"></a>

## Samples

<a id="GetExternalBackup_ExternalBackupService"></a>

# GetExternalBackup

`GET /v1/externalbackups/{id}`

GetExternalBackup returns the external backup configuration given its ID.

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

[StorageExternalBackup](../CommonObjectReference/CommonObjectReference.md#StorageExternalBackup_CommonObjectReference)

<a id="_content_type_2"></a>

## Content Type

- application/json

<a id="_responses_2"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [StorageExternalBackup](../CommonObjectReference/CommonObjectReference.md#StorageExternalBackup_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_2"></a>

## Samples

<a id="GetExternalBackups_ExternalBackupService"></a>

# GetExternalBackups

`GET /v1/externalbackups`

GetExternalBackups returns all external backup configurations.

<a id="_description_3"></a>

## Description

<a id="_parameters_3"></a>

## Parameters

<a id="_return_type_3"></a>

## Return Type

[V1GetExternalBackupsResponse](../CommonObjectReference/CommonObjectReference.md#V1GetExternalBackupsResponse_CommonObjectReference)

<a id="_content_type_3"></a>

## Content Type

- application/json

<a id="_responses_3"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V1GetExternalBackupsResponse](../CommonObjectReference/CommonObjectReference.md#V1GetExternalBackupsResponse_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_3"></a>

## Samples

<a id="PostExternalBackup_ExternalBackupService"></a>

# PostExternalBackup

`POST /v1/externalbackups`

PostExternalBackup creates an external backup configuration.

<a id="_description_4"></a>

## Description

<a id="_parameters_4"></a>

## Parameters

<a id="_body_parameter"></a>

### Body Parameter

| Name | Description | Required | Default | Pattern |
|----|----|----|----|----|
| body | [StorageExternalBackup](../CommonObjectReference/CommonObjectReference.md#StorageExternalBackup_CommonObjectReference) | X |  |  |

<a id="_return_type_4"></a>

## Return Type

[StorageExternalBackup](../CommonObjectReference/CommonObjectReference.md#StorageExternalBackup_CommonObjectReference)

<a id="_content_type_4"></a>

## Content Type

- application/json

<a id="_responses_4"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [StorageExternalBackup](../CommonObjectReference/CommonObjectReference.md#StorageExternalBackup_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_4"></a>

## Samples

<a id="PutExternalBackup_ExternalBackupService"></a>

# PutExternalBackup

`PUT /v1/externalbackups/{id}`

PutExternalBackup modifies a given external backup, without using stored credential reconciliation.

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
| body | [ExternalBackupServicePutExternalBackupBody](../CommonObjectReference/CommonObjectReference.md#ExternalBackupServicePutExternalBackupBody_CommonObjectReference) | X |  |  |

<a id="_return_type_5"></a>

## Return Type

[StorageExternalBackup](../CommonObjectReference/CommonObjectReference.md#StorageExternalBackup_CommonObjectReference)

<a id="_content_type_5"></a>

## Content Type

- application/json

<a id="_responses_5"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [StorageExternalBackup](../CommonObjectReference/CommonObjectReference.md#StorageExternalBackup_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_5"></a>

## Samples

<a id="TestExternalBackup_ExternalBackupService"></a>

# TestExternalBackup

`POST /v1/externalbackups/test`

TestExternalBackup tests an external backup configuration.

<a id="_description_6"></a>

## Description

<a id="_parameters_6"></a>

## Parameters

<a id="_body_parameter_3"></a>

### Body Parameter

| Name | Description | Required | Default | Pattern |
|----|----|----|----|----|
| body | [StorageExternalBackup](../CommonObjectReference/CommonObjectReference.md#StorageExternalBackup_CommonObjectReference) | X |  |  |

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

<a id="TestUpdatedExternalBackup_ExternalBackupService"></a>

# TestUpdatedExternalBackup

`POST /v1/externalbackups/test/updated`

TestUpdatedExternalBackup checks if the given external backup is correctly configured, with optional stored credential reconciliation.

<a id="_description_7"></a>

## Description

<a id="_parameters_7"></a>

## Parameters

<a id="_body_parameter_4"></a>

### Body Parameter

| Name | Description | Required | Default | Pattern |
|----|----|----|----|----|
| body | [V1UpdateExternalBackupRequest](../CommonObjectReference/CommonObjectReference.md#V1UpdateExternalBackupRequest_CommonObjectReference) | X |  |  |

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

<a id="TriggerExternalBackup_ExternalBackupService"></a>

# TriggerExternalBackup

`POST /v1/externalbackups/{id}`

TriggerExternalBackup initiates an external backup for the given configuration.

<a id="_description_8"></a>

## Description

<a id="_parameters_8"></a>

## Parameters

<a id="_path_parameters_4"></a>

### Path Parameters

| Name | Description | Required | Default | Pattern |
|------|-------------|----------|---------|---------|
| id   |             | X        | null    |         |

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

<a id="UpdateExternalBackup_ExternalBackupService"></a>

# UpdateExternalBackup

`PATCH /v1/externalbackups/{externalBackup.id}`

UpdateExternalBackup modifies a given external backup, with optional stored credential reconciliation.

<a id="_description_9"></a>

## Description

<a id="_parameters_9"></a>

## Parameters

<a id="_path_parameters_5"></a>

### Path Parameters

| Name              | Description | Required | Default | Pattern |
|-------------------|-------------|----------|---------|---------|
| externalBackup.id |             | X        | null    |         |

<a id="_body_parameter_5"></a>

### Body Parameter

| Name | Description | Required | Default | Pattern |
|----|----|----|----|----|
| body | [ExternalBackupServiceUpdateExternalBackupBody](../CommonObjectReference/CommonObjectReference.md#ExternalBackupServiceUpdateExternalBackupBody_CommonObjectReference) | X |  |  |

<a id="_return_type_9"></a>

## Return Type

[StorageExternalBackup](../CommonObjectReference/CommonObjectReference.md#StorageExternalBackup_CommonObjectReference)

<a id="_content_type_9"></a>

## Content Type

- application/json

<a id="_responses_9"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [StorageExternalBackup](../CommonObjectReference/CommonObjectReference.md#StorageExternalBackup_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_9"></a>

## Samples
