<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

<a id="GetMitreAttackVector_MitreAttackService"></a>

# GetMitreAttackVector

`GET /v1/mitreattackvectors/{id}`

GetMitreAttackVector returns the full MITRE ATT&CK vector for a tactic with all its techniques.

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

[V1GetMitreVectorResponse](../CommonObjectReference/CommonObjectReference.md#V1GetMitreVectorResponse_CommonObjectReference)

<a id="_content_type"></a>

## Content Type

- application/json

<a id="_responses"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V1GetMitreVectorResponse](../CommonObjectReference/CommonObjectReference.md#V1GetMitreVectorResponse_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples"></a>

## Samples

<a id="ListMitreAttackVectors_MitreAttackService"></a>

# ListMitreAttackVectors

`GET /v1/mitreattackvectors`

ListMitreAttackVectors returns all MITRE ATT&CK vectors.

<a id="_description_2"></a>

## Description

<a id="_parameters_2"></a>

## Parameters

<a id="_return_type_2"></a>

## Return Type

[V1ListMitreAttackVectorsResponse](../CommonObjectReference/CommonObjectReference.md#V1ListMitreAttackVectorsResponse_CommonObjectReference)

<a id="_content_type_2"></a>

## Content Type

- application/json

<a id="_responses_2"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V1ListMitreAttackVectorsResponse](../CommonObjectReference/CommonObjectReference.md#V1ListMitreAttackVectorsResponse_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_2"></a>

## Samples
