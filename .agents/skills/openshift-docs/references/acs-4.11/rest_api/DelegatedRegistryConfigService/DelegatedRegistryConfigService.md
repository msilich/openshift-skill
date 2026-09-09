<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

<a id="GetClusters_DelegatedRegistryConfigService"></a>

# GetClusters

`GET /v1/delegatedregistryconfig/clusters`

GetClusters returns the list of clusters (id + name) and a flag indicating whether or not the cluster is valid for use in the delegated registry config

<a id="_description"></a>

## Description

<a id="_parameters"></a>

## Parameters

<a id="_return_type"></a>

## Return Type

[V1DelegatedRegistryClustersResponse](../CommonObjectReference/CommonObjectReference.md#V1DelegatedRegistryClustersResponse_CommonObjectReference)

<a id="_content_type"></a>

## Content Type

- application/json

<a id="_responses"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V1DelegatedRegistryClustersResponse](../CommonObjectReference/CommonObjectReference.md#V1DelegatedRegistryClustersResponse_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples"></a>

## Samples

<a id="GetConfig_DelegatedRegistryConfigService"></a>

# GetConfig

`GET /v1/delegatedregistryconfig`

GetConfig returns the current delegated registry configuration

<a id="_description_2"></a>

## Description

<a id="_parameters_2"></a>

## Parameters

<a id="_return_type_2"></a>

## Return Type

[V1DelegatedRegistryConfig](../CommonObjectReference/CommonObjectReference.md#V1DelegatedRegistryConfig_CommonObjectReference)

<a id="_content_type_2"></a>

## Content Type

- application/json

<a id="_responses_2"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V1DelegatedRegistryConfig](../CommonObjectReference/CommonObjectReference.md#V1DelegatedRegistryConfig_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_2"></a>

## Samples

<a id="UpdateConfig_DelegatedRegistryConfigService"></a>

# UpdateConfig

`PUT /v1/delegatedregistryconfig`

UpdateConfig updates the stored delegated registry configuration

<a id="_description_3"></a>

## Description

<a id="_parameters_3"></a>

## Parameters

<a id="_body_parameter"></a>

### Body Parameter

| Name | Description | Required | Default | Pattern |
|----|----|----|----|----|
| body | DelegatedRegistryConfig determines if and where scan requests are delegated to, such as kept in central services or sent to particular secured clusters. [V1DelegatedRegistryConfig](../CommonObjectReference/CommonObjectReference.md#V1DelegatedRegistryConfig_CommonObjectReference) | X |  |  |

<a id="_return_type_3"></a>

## Return Type

[V1DelegatedRegistryConfig](../CommonObjectReference/CommonObjectReference.md#V1DelegatedRegistryConfig_CommonObjectReference)

<a id="_content_type_3"></a>

## Content Type

- application/json

<a id="_responses_3"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V1DelegatedRegistryConfig](../CommonObjectReference/CommonObjectReference.md#V1DelegatedRegistryConfig_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_3"></a>

## Samples
