<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

<a id="CreateCollection_CollectionService"></a>

# CreateCollection

`POST /v1/collections`

<a id="_description"></a>

## Description

<a id="_parameters"></a>

## Parameters

<a id="_body_parameter"></a>

### Body Parameter

| Name | Description | Required | Default | Pattern |
|----|----|----|----|----|
| body | [V1CreateCollectionRequest](../CommonObjectReference/CommonObjectReference.md#V1CreateCollectionRequest_CommonObjectReference) | X |  |  |

<a id="_return_type"></a>

## Return Type

[V1CreateCollectionResponse](../CommonObjectReference/CommonObjectReference.md#V1CreateCollectionResponse_CommonObjectReference)

<a id="_content_type"></a>

## Content Type

- application/json

<a id="_responses"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V1CreateCollectionResponse](../CommonObjectReference/CommonObjectReference.md#V1CreateCollectionResponse_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples"></a>

## Samples

<a id="DeleteCollection_CollectionService"></a>

# DeleteCollection

`DELETE /v1/collections/{id}`

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
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_2"></a>

## Samples

<a id="DryRunCollection_CollectionService"></a>

# DryRunCollection

`POST /v1/collections/dryrun`

<a id="_description_3"></a>

## Description

<a id="_parameters_3"></a>

## Parameters

<a id="_body_parameter_2"></a>

### Body Parameter

| Name | Description | Required | Default | Pattern |
|----|----|----|----|----|
| body | [V1DryRunCollectionRequest](../CommonObjectReference/CommonObjectReference.md#V1DryRunCollectionRequest_CommonObjectReference) | X |  |  |

<a id="_return_type_3"></a>

## Return Type

[V1DryRunCollectionResponse](../CommonObjectReference/CommonObjectReference.md#V1DryRunCollectionResponse_CommonObjectReference)

<a id="_content_type_3"></a>

## Content Type

- application/json

<a id="_responses_3"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V1DryRunCollectionResponse](../CommonObjectReference/CommonObjectReference.md#V1DryRunCollectionResponse_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_3"></a>

## Samples

<a id="GetCollection_CollectionService"></a>

# GetCollection

`GET /v1/collections/{id}`

<a id="_description_4"></a>

## Description

<a id="_parameters_4"></a>

## Parameters

<a id="_path_parameters_2"></a>

### Path Parameters

| Name | Description | Required | Default | Pattern |
|------|-------------|----------|---------|---------|
| id   |             | X        | null    |         |

<a id="_query_parameters"></a>

### Query Parameters

| Name | Description | Required | Default | Pattern |
|----|----|----|----|----|
| options.withMatches |  | \- | null |  |
| options.filterQuery.query |  | \- | null |  |
| options.filterQuery.pagination.limit |  | \- | null |  |
| options.filterQuery.pagination.offset |  | \- | null |  |
| options.filterQuery.pagination.sortOption.field |  | \- | null |  |
| options.filterQuery.pagination.sortOption.reversed |  | \- | null |  |
| options.filterQuery.pagination.sortOption.aggregateBy.aggrFunc |  | \- | UNSET |  |
| options.filterQuery.pagination.sortOption.aggregateBy.distinct |  | \- | null |  |

<a id="_return_type_4"></a>

## Return Type

[V1GetCollectionResponse](../CommonObjectReference/CommonObjectReference.md#V1GetCollectionResponse_CommonObjectReference)

<a id="_content_type_4"></a>

## Content Type

- application/json

<a id="_responses_4"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V1GetCollectionResponse](../CommonObjectReference/CommonObjectReference.md#V1GetCollectionResponse_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_4"></a>

## Samples

<a id="GetCollectionCount_CollectionService"></a>

# GetCollectionCount

`GET /v1/collectionscount`

<a id="_description_5"></a>

## Description

<a id="_parameters_5"></a>

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

<a id="_return_type_5"></a>

## Return Type

[V1GetCollectionCountResponse](../CommonObjectReference/CommonObjectReference.md#V1GetCollectionCountResponse_CommonObjectReference)

<a id="_content_type_5"></a>

## Content Type

- application/json

<a id="_responses_5"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V1GetCollectionCountResponse](../CommonObjectReference/CommonObjectReference.md#V1GetCollectionCountResponse_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_5"></a>

## Samples

<a id="ListCollectionSelectors_CollectionService"></a>

# ListCollectionSelectors

`GET /v1/collections/selectors`

<a id="_description_6"></a>

## Description

<a id="_parameters_6"></a>

## Parameters

<a id="_return_type_6"></a>

## Return Type

[V1ListCollectionSelectorsResponse](../CommonObjectReference/CommonObjectReference.md#V1ListCollectionSelectorsResponse_CommonObjectReference)

<a id="_content_type_6"></a>

## Content Type

- application/json

<a id="_responses_6"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V1ListCollectionSelectorsResponse](../CommonObjectReference/CommonObjectReference.md#V1ListCollectionSelectorsResponse_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_6"></a>

## Samples

<a id="ListCollections_CollectionService"></a>

# ListCollections

`GET /v1/collections`

<a id="_description_7"></a>

## Description

<a id="_parameters_7"></a>

## Parameters

<a id="_query_parameters_3"></a>

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

<a id="_return_type_7"></a>

## Return Type

[V1ListCollectionsResponse](../CommonObjectReference/CommonObjectReference.md#V1ListCollectionsResponse_CommonObjectReference)

<a id="_content_type_7"></a>

## Content Type

- application/json

<a id="_responses_7"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V1ListCollectionsResponse](../CommonObjectReference/CommonObjectReference.md#V1ListCollectionsResponse_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_7"></a>

## Samples

<a id="UpdateCollection_CollectionService"></a>

# UpdateCollection

`PATCH /v1/collections/{id}`

<a id="_description_8"></a>

## Description

<a id="_parameters_8"></a>

## Parameters

<a id="_path_parameters_3"></a>

### Path Parameters

| Name | Description | Required | Default | Pattern |
|------|-------------|----------|---------|---------|
| id   |             | X        | null    |         |

<a id="_body_parameter_3"></a>

### Body Parameter

| Name | Description | Required | Default | Pattern |
|----|----|----|----|----|
| body | [CollectionServiceUpdateCollectionBody](../CommonObjectReference/CommonObjectReference.md#CollectionServiceUpdateCollectionBody_CommonObjectReference) | X |  |  |

<a id="_return_type_8"></a>

## Return Type

[V1UpdateCollectionResponse](../CommonObjectReference/CommonObjectReference.md#V1UpdateCollectionResponse_CommonObjectReference)

<a id="_content_type_8"></a>

## Content Type

- application/json

<a id="_responses_8"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V1UpdateCollectionResponse](../CommonObjectReference/CommonObjectReference.md#V1UpdateCollectionResponse_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_8"></a>

## Samples
