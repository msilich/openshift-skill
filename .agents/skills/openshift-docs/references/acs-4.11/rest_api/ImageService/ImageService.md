<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

<a id="GenerateSBOM_ImageService"></a>

# GenerateSBOM

`POST /api/v1/images/sbom`

Generate an SPDX 2.3 SBOM from an image scan.

<a id="_description"></a>

## Description

<a id="_parameters"></a>

## Parameters

<a id="_body_parameter"></a>

### Body Parameter

| Name | Description | Required | Default | Pattern |
|----|----|----|----|----|
| body | [ImageSBOMRequest](../CommonObjectReference/CommonObjectReference.md#ImageSBOMRequest_CommonObjectReference) | X |  |  |

<a id="_return_type"></a>

## Return Type

[SBOMSPDX23Document](../CommonObjectReference/CommonObjectReference.md#SBOMSPDX23Document_CommonObjectReference)

<a id="_content_type"></a>

## Content Type

- application/json

<a id="_responses"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [SBOMSPDX23Document](../CommonObjectReference/CommonObjectReference.md#SBOMSPDX23Document_CommonObjectReference) |
| 0 | An unexpected error response. | [GooglerpcStatus](../CommonObjectReference/CommonObjectReference.md#GooglerpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples"></a>

## Samples

<a id="CountImages_ImageService"></a>

# CountImages

`GET /v1/imagescount`

CountImages returns a count of images that match the input query.

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

[V1CountImagesResponse](../CommonObjectReference/CommonObjectReference.md#V1CountImagesResponse_CommonObjectReference)

<a id="_content_type_2"></a>

## Content Type

- application/json

<a id="_responses_2"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V1CountImagesResponse](../CommonObjectReference/CommonObjectReference.md#V1CountImagesResponse_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_2"></a>

## Samples

<a id="DeleteImages_ImageService"></a>

# DeleteImages

`DELETE /v1/images`

DeleteImage removes the images based on a query

<a id="_description_3"></a>

## Description

<a id="_parameters_3"></a>

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

<a id="_return_type_3"></a>

## Return Type

[V1DeleteImagesResponse](../CommonObjectReference/CommonObjectReference.md#V1DeleteImagesResponse_CommonObjectReference)

<a id="_content_type_3"></a>

## Content Type

- application/json

<a id="_responses_3"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V1DeleteImagesResponse](../CommonObjectReference/CommonObjectReference.md#V1DeleteImagesResponse_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_3"></a>

## Samples

<a id="ExportImages_ImageService"></a>

# ExportImages

`GET /v1/export/images`

<a id="_description_4"></a>

## Description

<a id="_parameters_4"></a>

## Parameters

<a id="_query_parameters_3"></a>

### Query Parameters

| Name    | Description | Required | Default | Pattern |
|---------|-------------|----------|---------|---------|
| timeout |             | \-       | null    |         |
| query   |             | \-       | null    |         |

<a id="_return_type_4"></a>

## Return Type

Stream result of v1ExportImageResponse.

<a id="_content_type_4"></a>

## Content Type

- application/json

<a id="_responses_4"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response.(streaming responses) | Stream result of v1ExportImageResponse. |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_4"></a>

## Samples

<a id="GetImage_ImageService"></a>

# GetImage

`GET /v1/images/{id}`

GetImage returns the image given its ID.

<a id="_description_5"></a>

## Description

<a id="_parameters_5"></a>

## Parameters

<a id="_path_parameters"></a>

### Path Parameters

| Name | Description | Required | Default | Pattern |
|------|-------------|----------|---------|---------|
| id   |             | X        | null    |         |

<a id="_query_parameters_4"></a>

### Query Parameters

| Name             | Description | Required | Default | Pattern |
|------------------|-------------|----------|---------|---------|
| includeSnoozed   |             | \-       | null    |         |
| stripDescription |             | \-       | null    |         |

<a id="_return_type_5"></a>

## Return Type

[StorageImage](../CommonObjectReference/CommonObjectReference.md#StorageImage_CommonObjectReference)

<a id="_content_type_5"></a>

## Content Type

- application/json

<a id="_responses_5"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [StorageImage](../CommonObjectReference/CommonObjectReference.md#StorageImage_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_5"></a>

## Samples

<a id="GetWatchedImages_ImageService"></a>

# GetWatchedImages

`GET /v1/watchedimages`

GetWatchedImages returns the list of image names that are currently being watched.

<a id="_description_6"></a>

## Description

<a id="_parameters_6"></a>

## Parameters

<a id="_return_type_6"></a>

## Return Type

[V1GetWatchedImagesResponse](../CommonObjectReference/CommonObjectReference.md#V1GetWatchedImagesResponse_CommonObjectReference)

<a id="_content_type_6"></a>

## Content Type

- application/json

<a id="_responses_6"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V1GetWatchedImagesResponse](../CommonObjectReference/CommonObjectReference.md#V1GetWatchedImagesResponse_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_6"></a>

## Samples

<a id="InvalidateScanAndRegistryCaches_ImageService"></a>

# InvalidateScanAndRegistryCaches

`GET /v1/images/cache/invalidate`

InvalidateScanAndRegistryCaches removes the image metadata cache.

<a id="_description_7"></a>

## Description

<a id="_parameters_7"></a>

## Parameters

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

<a id="ListImages_ImageService"></a>

# ListImages

`GET /v1/images`

ListImages returns all the images that match the input query.

<a id="_description_8"></a>

## Description

<a id="_parameters_8"></a>

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

<a id="_return_type_8"></a>

## Return Type

[V1ListImagesResponse](../CommonObjectReference/CommonObjectReference.md#V1ListImagesResponse_CommonObjectReference)

<a id="_content_type_8"></a>

## Content Type

- application/json

<a id="_responses_8"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V1ListImagesResponse](../CommonObjectReference/CommonObjectReference.md#V1ListImagesResponse_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_8"></a>

## Samples

<a id="ScanImage_ImageService"></a>

# ScanImage

`POST /v1/images/scan`

ScanImage scans a single image and returns the result

<a id="_description_9"></a>

## Description

<a id="_parameters_9"></a>

## Parameters

<a id="_body_parameter_2"></a>

### Body Parameter

| Name | Description | Required | Default | Pattern |
|----|----|----|----|----|
| body | [V1ScanImageRequest](../CommonObjectReference/CommonObjectReference.md#V1ScanImageRequest_CommonObjectReference) | X |  |  |

<a id="_return_type_9"></a>

## Return Type

[StorageImage](../CommonObjectReference/CommonObjectReference.md#StorageImage_CommonObjectReference)

<a id="_content_type_9"></a>

## Content Type

- application/json

<a id="_responses_9"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [StorageImage](../CommonObjectReference/CommonObjectReference.md#StorageImage_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_9"></a>

## Samples

<a id="UnwatchImage_ImageService"></a>

# UnwatchImage

`DELETE /v1/watchedimages`

UnwatchImage marks an image name to no longer be watched. It returns successfully if the image is no longer being watched after the call, irrespective of whether the image was already being watched.

<a id="_description_10"></a>

## Description

<a id="_parameters_10"></a>

## Parameters

<a id="_query_parameters_6"></a>

### Query Parameters

| Name | Description | Required | Default | Pattern |
|----|----|----|----|----|
| name | The name of the image to unwatch. Should match the name of a previously watched image. | \- | null |  |

<a id="_return_type_10"></a>

## Return Type

`Object`

<a id="_content_type_10"></a>

## Content Type

- application/json

<a id="_responses_10"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | `Object` |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_10"></a>

## Samples

<a id="WatchImage_ImageService"></a>

# WatchImage

`POST /v1/watchedimages`

WatchImage marks an image name as to be watched.

<a id="_description_11"></a>

## Description

<a id="_parameters_11"></a>

## Parameters

<a id="_body_parameter_3"></a>

### Body Parameter

| Name | Description | Required | Default | Pattern |
|----|----|----|----|----|
| body | [V1WatchImageRequest](../CommonObjectReference/CommonObjectReference.md#V1WatchImageRequest_CommonObjectReference) | X |  |  |

<a id="_return_type_11"></a>

## Return Type

[V1WatchImageResponse](../CommonObjectReference/CommonObjectReference.md#V1WatchImageResponse_CommonObjectReference)

<a id="_content_type_11"></a>

## Content Type

- application/json

<a id="_responses_11"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V1WatchImageResponse](../CommonObjectReference/CommonObjectReference.md#V1WatchImageResponse_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_11"></a>

## Samples
