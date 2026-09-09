<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

<a id="DeletePolicyCategory_PolicyCategoryService"></a>

# DeletePolicyCategory

`DELETE /v1/policycategories/{id}`

DeletePolicyCategory removes the given policy category.

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

<a id="GetPolicyCategories_PolicyCategoryService"></a>

# GetPolicyCategories

`GET /v1/policycategories`

GetPolicyCategories returns the list of policy categories

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

[V1GetPolicyCategoriesResponse](../CommonObjectReference/CommonObjectReference.md#V1GetPolicyCategoriesResponse_CommonObjectReference)

<a id="_content_type_2"></a>

## Content Type

- application/json

<a id="_responses_2"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V1GetPolicyCategoriesResponse](../CommonObjectReference/CommonObjectReference.md#V1GetPolicyCategoriesResponse_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_2"></a>

## Samples

<a id="GetPolicyCategory_PolicyCategoryService"></a>

# GetPolicyCategory

`GET /v1/policycategories/{id}`

GetPolicyCategory returns the requested policy category by ID.

<a id="_description_3"></a>

## Description

<a id="_parameters_3"></a>

## Parameters

<a id="_path_parameters_2"></a>

### Path Parameters

| Name | Description | Required | Default | Pattern |
|------|-------------|----------|---------|---------|
| id   |             | X        | null    |         |

<a id="_return_type_3"></a>

## Return Type

[V1PolicyCategory](../CommonObjectReference/CommonObjectReference.md#V1PolicyCategory_CommonObjectReference)

<a id="_content_type_3"></a>

## Content Type

- application/json

<a id="_responses_3"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V1PolicyCategory](../CommonObjectReference/CommonObjectReference.md#V1PolicyCategory_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_3"></a>

## Samples

<a id="PostPolicyCategory_PolicyCategoryService"></a>

# PostPolicyCategory

`POST /v1/policycategories`

PostPolicyCategory creates a new policy category

<a id="_description_4"></a>

## Description

<a id="_parameters_4"></a>

## Parameters

<a id="_body_parameter"></a>

### Body Parameter

| Name | Description | Required | Default | Pattern |
|----|----|----|----|----|
| policyCategory | [V1PolicyCategory](../CommonObjectReference/CommonObjectReference.md#V1PolicyCategory_CommonObjectReference) | X |  |  |

<a id="_return_type_4"></a>

## Return Type

[V1PolicyCategory](../CommonObjectReference/CommonObjectReference.md#V1PolicyCategory_CommonObjectReference)

<a id="_content_type_4"></a>

## Content Type

- application/json

<a id="_responses_4"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V1PolicyCategory](../CommonObjectReference/CommonObjectReference.md#V1PolicyCategory_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_4"></a>

## Samples

<a id="RenamePolicyCategory_PolicyCategoryService"></a>

# RenamePolicyCategory

`PUT /v1/policycategories`

RenamePolicyCategory renames the given policy category.

<a id="_description_5"></a>

## Description

<a id="_parameters_5"></a>

## Parameters

<a id="_body_parameter_2"></a>

### Body Parameter

| Name | Description | Required | Default | Pattern |
|----|----|----|----|----|
| body | [V1RenamePolicyCategoryRequest](../CommonObjectReference/CommonObjectReference.md#V1RenamePolicyCategoryRequest_CommonObjectReference) | X |  |  |

<a id="_return_type_5"></a>

## Return Type

[V1PolicyCategory](../CommonObjectReference/CommonObjectReference.md#V1PolicyCategory_CommonObjectReference)

<a id="_content_type_5"></a>

## Content Type

- application/json

<a id="_responses_5"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V1PolicyCategory](../CommonObjectReference/CommonObjectReference.md#V1PolicyCategory_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_5"></a>

## Samples
