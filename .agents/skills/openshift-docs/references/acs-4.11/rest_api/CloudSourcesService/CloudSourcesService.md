<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

<a id="CountCloudSources_CloudSourcesService"></a>

# CountCloudSources

`GET /v1/count/cloud-sources`

CountCloudSources returns the number of cloud sources after filtering by requested fields.

<a id="_description"></a>

## Description

<a id="_parameters"></a>

## Parameters

<a id="_query_parameters"></a>

### Query Parameters

| Name | Description | Required | Default | Pattern |
|----|----|----|----|----|
| filter.names | Matches cloud sources based on their name. `String` | \- | null |  |
| filter.types | Matches cloud sources based on their type. `String` | \- | null |  |

<a id="_return_type"></a>

## Return Type

[V1CountCloudSourcesResponse](../CommonObjectReference/CommonObjectReference.md#V1CountCloudSourcesResponse_CommonObjectReference)

<a id="_content_type"></a>

## Content Type

- application/json

<a id="_responses"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V1CountCloudSourcesResponse](../CommonObjectReference/CommonObjectReference.md#V1CountCloudSourcesResponse_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples"></a>

## Samples

<a id="CreateCloudSource_CloudSourcesService"></a>

# CreateCloudSource

`POST /v1/cloud-sources`

CreateCloudSource creates a cloud source.

<a id="_description_2"></a>

## Description

<a id="_parameters_2"></a>

## Parameters

<a id="_body_parameter"></a>

### Body Parameter

| Name | Description | Required | Default | Pattern |
|----|----|----|----|----|
| body | [V1CreateCloudSourceRequest](../CommonObjectReference/CommonObjectReference.md#V1CreateCloudSourceRequest_CommonObjectReference) | X |  |  |

<a id="_return_type_2"></a>

## Return Type

[V1CreateCloudSourceResponse](../CommonObjectReference/CommonObjectReference.md#V1CreateCloudSourceResponse_CommonObjectReference)

<a id="_content_type_2"></a>

## Content Type

- application/json

<a id="_responses_2"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V1CreateCloudSourceResponse](../CommonObjectReference/CommonObjectReference.md#V1CreateCloudSourceResponse_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_2"></a>

## Samples

<a id="DeleteCloudSource_CloudSourcesService"></a>

# DeleteCloudSource

`DELETE /v1/cloud-sources/{id}`

DeleteCloudSource removes a cloud source.

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

`Object`

<a id="_content_type_3"></a>

## Content Type

- application/json

<a id="_responses_3"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | `Object` |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_3"></a>

## Samples

<a id="GetCloudSource_CloudSourcesService"></a>

# GetCloudSource

`GET /v1/cloud-sources/{id}`

GetCloudSource retrieves a cloud source by ID.

<a id="_description_4"></a>

## Description

<a id="_parameters_4"></a>

## Parameters

<a id="_path_parameters_2"></a>

### Path Parameters

| Name | Description | Required | Default | Pattern |
|------|-------------|----------|---------|---------|
| id   |             | X        | null    |         |

<a id="_return_type_4"></a>

## Return Type

[V1GetCloudSourceResponse](../CommonObjectReference/CommonObjectReference.md#V1GetCloudSourceResponse_CommonObjectReference)

<a id="_content_type_4"></a>

## Content Type

- application/json

<a id="_responses_4"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V1GetCloudSourceResponse](../CommonObjectReference/CommonObjectReference.md#V1GetCloudSourceResponse_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_4"></a>

## Samples

<a id="ListCloudSources_CloudSourcesService"></a>

# ListCloudSources

`GET /v1/cloud-sources`

ListCloudSources returns the list of cloud sources after filtered by requested fields.

<a id="_description_5"></a>

## Description

<a id="_parameters_5"></a>

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
| filter.names | Matches cloud sources based on their name. `String` | \- | null |  |
| filter.types | Matches cloud sources based on their type. `String` | \- | null |  |

<a id="_return_type_5"></a>

## Return Type

[V1ListCloudSourcesResponse](../CommonObjectReference/CommonObjectReference.md#V1ListCloudSourcesResponse_CommonObjectReference)

<a id="_content_type_5"></a>

## Content Type

- application/json

<a id="_responses_5"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V1ListCloudSourcesResponse](../CommonObjectReference/CommonObjectReference.md#V1ListCloudSourcesResponse_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_5"></a>

## Samples

<a id="TestCloudSource_CloudSourcesService"></a>

# TestCloudSource

`POST /v1/cloud-sources/test`

TestCloudSource tests a cloud source.

<a id="_description_6"></a>

## Description

<a id="_parameters_6"></a>

## Parameters

<a id="_body_parameter_2"></a>

### Body Parameter

| Name | Description | Required | Default | Pattern |
|----|----|----|----|----|
| body | [V1TestCloudSourceRequest](../CommonObjectReference/CommonObjectReference.md#V1TestCloudSourceRequest_CommonObjectReference) | X |  |  |

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

<a id="UpdateCloudSource_CloudSourcesService"></a>

# UpdateCloudSource

`PUT /v1/cloud-sources/{cloudSource.id}`

UpdateCloudSource creates or replaces a cloud source.

<a id="_description_7"></a>

## Description

<a id="_parameters_7"></a>

## Parameters

<a id="_path_parameters_3"></a>

### Path Parameters

| Name           | Description | Required | Default | Pattern |
|----------------|-------------|----------|---------|---------|
| cloudSource.id |             | X        | null    |         |

<a id="_body_parameter_3"></a>

### Body Parameter

| Name | Description | Required | Default | Pattern |
|----|----|----|----|----|
| body | [CloudSourcesServiceUpdateCloudSourceBody](../CommonObjectReference/CommonObjectReference.md#CloudSourcesServiceUpdateCloudSourceBody_CommonObjectReference) | X |  |  |

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
