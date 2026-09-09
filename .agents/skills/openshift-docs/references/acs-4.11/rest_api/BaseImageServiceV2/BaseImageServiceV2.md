<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

<a id="CreateBaseImageReference_BaseImageServiceV2"></a>

# CreateBaseImageReference

`POST /v2/baseimages`

CreateBaseImageReference creates a new base image reference.

<a id="_description"></a>

## Description

<a id="_parameters"></a>

## Parameters

<a id="_body_parameter"></a>

### Body Parameter

| Name | Description | Required | Default | Pattern |
|----|----|----|----|----|
| body | [V2CreateBaseImageReferenceRequest](../CommonObjectReference/CommonObjectReference.md#V2CreateBaseImageReferenceRequest_CommonObjectReference) | X |  |  |

<a id="_return_type"></a>

## Return Type

[V2CreateBaseImageReferenceResponse](../CommonObjectReference/CommonObjectReference.md#V2CreateBaseImageReferenceResponse_CommonObjectReference)

<a id="_content_type"></a>

## Content Type

- application/json

<a id="_responses"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V2CreateBaseImageReferenceResponse](../CommonObjectReference/CommonObjectReference.md#V2CreateBaseImageReferenceResponse_CommonObjectReference) |
| 0 | An unexpected error response. | [RpcStatus](../CommonObjectReference/CommonObjectReference.md#RpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples"></a>

## Samples

<a id="DeleteBaseImageReference_BaseImageServiceV2"></a>

# DeleteBaseImageReference

`DELETE /v2/baseimages/{id}`

DeleteBaseImageReference deletes a base image reference.

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

`Object`

<a id="_content_type_2"></a>

## Content Type

- application/json

<a id="_responses_2"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | `Object` |
| 0 | An unexpected error response. | [RpcStatus](../CommonObjectReference/CommonObjectReference.md#RpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_2"></a>

## Samples

<a id="GetBaseImageReferences_BaseImageServiceV2"></a>

# GetBaseImageReferences

`GET /v2/baseimages`

GetBaseImageReferences returns all base image references.

<a id="_description_3"></a>

## Description

<a id="_parameters_3"></a>

## Parameters

<a id="_return_type_3"></a>

## Return Type

[V2GetBaseImageReferenceResponse](../CommonObjectReference/CommonObjectReference.md#V2GetBaseImageReferenceResponse_CommonObjectReference)

<a id="_content_type_3"></a>

## Content Type

- application/json

<a id="_responses_3"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V2GetBaseImageReferenceResponse](../CommonObjectReference/CommonObjectReference.md#V2GetBaseImageReferenceResponse_CommonObjectReference) |
| 0 | An unexpected error response. | [RpcStatus](../CommonObjectReference/CommonObjectReference.md#RpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_3"></a>

## Samples

<a id="UpdateBaseImageTagPattern_BaseImageServiceV2"></a>

# UpdateBaseImageTagPattern

`PUT /v2/baseimages/{id}`

UpdateBaseImageTagPattern updates the tag pattern of an existing base image reference.

<a id="_description_4"></a>

## Description

<a id="_parameters_4"></a>

## Parameters

<a id="_path_parameters_2"></a>

### Path Parameters

| Name | Description | Required | Default | Pattern |
|------|-------------|----------|---------|---------|
| id   |             | X        | null    |         |

<a id="_body_parameter_2"></a>

### Body Parameter

| Name | Description | Required | Default | Pattern |
|----|----|----|----|----|
| body | [BaseImageServiceV2UpdateBaseImageTagPatternBody](../CommonObjectReference/CommonObjectReference.md#BaseImageServiceV2UpdateBaseImageTagPatternBody_CommonObjectReference) | X |  |  |

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
