<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

<a id="SuppressCVEs_ClusterCVEService"></a>

# SuppressCVEs

`PATCH /v1/clustercves/suppress`

SuppressCVE suppresses cluster cves.

<a id="_description"></a>

## Description

<a id="_parameters"></a>

## Parameters

<a id="_body_parameter"></a>

### Body Parameter

| Name | Description | Required | Default | Pattern |
|----|----|----|----|----|
| body | [V1SuppressCVERequest](../CommonObjectReference/CommonObjectReference.md#V1SuppressCVERequest_CommonObjectReference) | X |  |  |

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

<a id="UnsuppressCVEs_ClusterCVEService"></a>

# UnsuppressCVEs

`PATCH /v1/clustercves/unsuppress`

UnsuppressCVE unsuppresses cluster cves.

<a id="_description_2"></a>

## Description

<a id="_parameters_2"></a>

## Parameters

<a id="_body_parameter_2"></a>

### Body Parameter

| Name | Description | Required | Default | Pattern |
|----|----|----|----|----|
| body | [V1UnsuppressCVERequest](../CommonObjectReference/CommonObjectReference.md#V1UnsuppressCVERequest_CommonObjectReference) | X |  |  |

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
