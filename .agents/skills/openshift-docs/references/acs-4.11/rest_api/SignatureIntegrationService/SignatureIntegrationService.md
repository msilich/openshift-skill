<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

<a id="DeleteSignatureIntegration_SignatureIntegrationService"></a>

# DeleteSignatureIntegration

`DELETE /v1/signatureintegrations/{id}`

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

<a id="GetSignatureIntegration_SignatureIntegrationService"></a>

# GetSignatureIntegration

`GET /v1/signatureintegrations/{id}`

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

[StorageSignatureIntegration](../CommonObjectReference/CommonObjectReference.md#StorageSignatureIntegration_CommonObjectReference)

<a id="_content_type_2"></a>

## Content Type

- application/json

<a id="_responses_2"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [StorageSignatureIntegration](../CommonObjectReference/CommonObjectReference.md#StorageSignatureIntegration_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_2"></a>

## Samples

<a id="ListSignatureIntegrations_SignatureIntegrationService"></a>

# ListSignatureIntegrations

`GET /v1/signatureintegrations`

<a id="_description_3"></a>

## Description

<a id="_parameters_3"></a>

## Parameters

<a id="_return_type_3"></a>

## Return Type

[V1ListSignatureIntegrationsResponse](../CommonObjectReference/CommonObjectReference.md#V1ListSignatureIntegrationsResponse_CommonObjectReference)

<a id="_content_type_3"></a>

## Content Type

- application/json

<a id="_responses_3"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V1ListSignatureIntegrationsResponse](../CommonObjectReference/CommonObjectReference.md#V1ListSignatureIntegrationsResponse_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_3"></a>

## Samples

<a id="PostSignatureIntegration_SignatureIntegrationService"></a>

# PostSignatureIntegration

`POST /v1/signatureintegrations`

Integration id should not be set. Returns signature integration with id filled.

<a id="_description_4"></a>

## Description

<a id="_parameters_4"></a>

## Parameters

<a id="_body_parameter"></a>

### Body Parameter

| Name | Description | Required | Default | Pattern |
|----|----|----|----|----|
| body | [StorageSignatureIntegration](../CommonObjectReference/CommonObjectReference.md#StorageSignatureIntegration_CommonObjectReference) | X |  |  |

<a id="_return_type_4"></a>

## Return Type

[StorageSignatureIntegration](../CommonObjectReference/CommonObjectReference.md#StorageSignatureIntegration_CommonObjectReference)

<a id="_content_type_4"></a>

## Content Type

- application/json

<a id="_responses_4"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [StorageSignatureIntegration](../CommonObjectReference/CommonObjectReference.md#StorageSignatureIntegration_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_4"></a>

## Samples

<a id="PutSignatureIntegration_SignatureIntegrationService"></a>

# PutSignatureIntegration

`PUT /v1/signatureintegrations/{id}`

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
| body | [SignatureIntegrationServicePutSignatureIntegrationBody](../CommonObjectReference/CommonObjectReference.md#SignatureIntegrationServicePutSignatureIntegrationBody_CommonObjectReference) | X |  |  |

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
