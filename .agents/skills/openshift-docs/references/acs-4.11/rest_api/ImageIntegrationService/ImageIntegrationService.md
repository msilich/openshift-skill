<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

<a id="DeleteImageIntegration_ImageIntegrationService"></a>

# DeleteImageIntegration

`DELETE /v1/imageintegrations/{id}`

DeleteImageIntegration removes a image integration given its ID.

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

<a id="GetImageIntegration_ImageIntegrationService"></a>

# GetImageIntegration

`GET /v1/imageintegrations/{id}`

GetImageIntegration returns the image integration given its ID.

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

[StorageImageIntegration](../CommonObjectReference/CommonObjectReference.md#StorageImageIntegration_CommonObjectReference)

<a id="_content_type_2"></a>

## Content Type

- application/json

<a id="_responses_2"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [StorageImageIntegration](../CommonObjectReference/CommonObjectReference.md#StorageImageIntegration_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_2"></a>

## Samples

<a id="GetImageIntegrations_ImageIntegrationService"></a>

# GetImageIntegrations

`GET /v1/imageintegrations`

GetImageIntegrations returns all image integrations that match the request filters.

<a id="_description_3"></a>

## Description

<a id="_parameters_3"></a>

## Parameters

<a id="_query_parameters"></a>

### Query Parameters

| Name    | Description | Required | Default | Pattern |
|---------|-------------|----------|---------|---------|
| name    |             | \-       | null    |         |
| cluster |             | \-       | null    |         |

<a id="_return_type_3"></a>

## Return Type

[V1GetImageIntegrationsResponse](../CommonObjectReference/CommonObjectReference.md#V1GetImageIntegrationsResponse_CommonObjectReference)

<a id="_content_type_3"></a>

## Content Type

- application/json

<a id="_responses_3"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V1GetImageIntegrationsResponse](../CommonObjectReference/CommonObjectReference.md#V1GetImageIntegrationsResponse_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_3"></a>

## Samples

<a id="PostImageIntegration_ImageIntegrationService"></a>

# PostImageIntegration

`POST /v1/imageintegrations`

PostImageIntegration creates a image integration.

<a id="_description_4"></a>

## Description

<a id="_parameters_4"></a>

## Parameters

<a id="_body_parameter"></a>

### Body Parameter

| Name | Description | Required | Default | Pattern |
|----|----|----|----|----|
| body | [StorageImageIntegration](../CommonObjectReference/CommonObjectReference.md#StorageImageIntegration_CommonObjectReference) | X |  |  |

<a id="_return_type_4"></a>

## Return Type

[StorageImageIntegration](../CommonObjectReference/CommonObjectReference.md#StorageImageIntegration_CommonObjectReference)

<a id="_content_type_4"></a>

## Content Type

- application/json

<a id="_responses_4"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [StorageImageIntegration](../CommonObjectReference/CommonObjectReference.md#StorageImageIntegration_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_4"></a>

## Samples

<a id="PutImageIntegration_ImageIntegrationService"></a>

# PutImageIntegration

`PUT /v1/imageintegrations/{id}`

PutImageIntegration modifies a given image integration, without using stored credential reconciliation.

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
| body | [ImageIntegrationServicePutImageIntegrationBody](../CommonObjectReference/CommonObjectReference.md#ImageIntegrationServicePutImageIntegrationBody_CommonObjectReference) | X |  |  |

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

<a id="TestImageIntegration_ImageIntegrationService"></a>

# TestImageIntegration

`POST /v1/imageintegrations/test`

TestImageIntegration checks if the given image integration is correctly configured, without using stored credential reconciliation.

<a id="_description_6"></a>

## Description

<a id="_parameters_6"></a>

## Parameters

<a id="_body_parameter_3"></a>

### Body Parameter

| Name | Description | Required | Default | Pattern |
|----|----|----|----|----|
| body | [StorageImageIntegration](../CommonObjectReference/CommonObjectReference.md#StorageImageIntegration_CommonObjectReference) | X |  |  |

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

<a id="TestUpdatedImageIntegration_ImageIntegrationService"></a>

# TestUpdatedImageIntegration

`POST /v1/imageintegrations/test/updated`

TestUpdatedImageIntegration checks if the given image integration is correctly configured, with optional stored credential reconciliation.

<a id="_description_7"></a>

## Description

<a id="_parameters_7"></a>

## Parameters

<a id="_body_parameter_4"></a>

### Body Parameter

| Name | Description | Required | Default | Pattern |
|----|----|----|----|----|
| body | [V1UpdateImageIntegrationRequest](../CommonObjectReference/CommonObjectReference.md#V1UpdateImageIntegrationRequest_CommonObjectReference) | X |  |  |

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

<a id="UpdateImageIntegration_ImageIntegrationService"></a>

# UpdateImageIntegration

`PATCH /v1/imageintegrations/{config.id}`

UpdateImageIntegration modifies a given image integration, with optional stored credential reconciliation.

<a id="_description_8"></a>

## Description

<a id="_parameters_8"></a>

## Parameters

<a id="_path_parameters_4"></a>

### Path Parameters

| Name      | Description | Required | Default | Pattern |
|-----------|-------------|----------|---------|---------|
| config.id |             | X        | null    |         |

<a id="_body_parameter_5"></a>

### Body Parameter

| Name | Description | Required | Default | Pattern |
|----|----|----|----|----|
| body | [ImageIntegrationServiceUpdateImageIntegrationBody](../CommonObjectReference/CommonObjectReference.md#ImageIntegrationServiceUpdateImageIntegrationBody_CommonObjectReference) | X |  |  |

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
