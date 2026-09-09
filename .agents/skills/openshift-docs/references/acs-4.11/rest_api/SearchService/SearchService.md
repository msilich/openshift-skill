<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

<a id="Autocomplete_SearchService"></a>

# Autocomplete

`GET /v1/search/autocomplete`

<a id="_description"></a>

## Description

<a id="_parameters"></a>

## Parameters

<a id="_query_parameters"></a>

### Query Parameters

| Name       | Description | Required | Default | Pattern |
|------------|-------------|----------|---------|---------|
| query      |             | \-       | null    |         |
| categories | `String`    | \-       | null    |         |

<a id="_return_type"></a>

## Return Type

[V1AutocompleteResponse](../CommonObjectReference/CommonObjectReference.md#V1AutocompleteResponse_CommonObjectReference)

<a id="_content_type"></a>

## Content Type

- application/json

<a id="_responses"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V1AutocompleteResponse](../CommonObjectReference/CommonObjectReference.md#V1AutocompleteResponse_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples"></a>

## Samples

<a id="Options_SearchService"></a>

# Options

`GET /v1/search/metadata/options`

<a id="_description_2"></a>

## Description

<a id="_parameters_2"></a>

## Parameters

<a id="_query_parameters_2"></a>

### Query Parameters

| Name       | Description | Required | Default | Pattern |
|------------|-------------|----------|---------|---------|
| categories | `String`    | \-       | null    |         |

<a id="_return_type_2"></a>

## Return Type

[V1SearchOptionsResponse](../CommonObjectReference/CommonObjectReference.md#V1SearchOptionsResponse_CommonObjectReference)

<a id="_content_type_2"></a>

## Content Type

- application/json

<a id="_responses_2"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V1SearchOptionsResponse](../CommonObjectReference/CommonObjectReference.md#V1SearchOptionsResponse_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_2"></a>

## Samples

<a id="Search_SearchService"></a>

# Search

`GET /v1/search`

<a id="_description_3"></a>

## Description

<a id="_parameters_3"></a>

## Parameters

<a id="_query_parameters_3"></a>

### Query Parameters

| Name       | Description | Required | Default | Pattern |
|------------|-------------|----------|---------|---------|
| query      |             | \-       | null    |         |
| categories | `String`    | \-       | null    |         |

<a id="_return_type_3"></a>

## Return Type

[V1SearchResponse](../CommonObjectReference/CommonObjectReference.md#V1SearchResponse_CommonObjectReference)

<a id="_content_type_3"></a>

## Content Type

- application/json

<a id="_responses_3"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V1SearchResponse](../CommonObjectReference/CommonObjectReference.md#V1SearchResponse_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_3"></a>

## Samples
