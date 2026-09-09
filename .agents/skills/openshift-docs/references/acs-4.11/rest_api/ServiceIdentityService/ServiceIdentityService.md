<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

<a id="CreateServiceIdentity_ServiceIdentityService"></a>

# CreateServiceIdentity

`POST /v1/serviceIdentities`

CreateServiceIdentity creates a new key pair and certificate. The key and certificate are not retained and can never be retrieved again.

<a id="_description"></a>

## Description

<a id="_parameters"></a>

## Parameters

<a id="_body_parameter"></a>

### Body Parameter

| Name | Description | Required | Default | Pattern |
|----|----|----|----|----|
| body | [V1CreateServiceIdentityRequest](../CommonObjectReference/CommonObjectReference.md#V1CreateServiceIdentityRequest_CommonObjectReference) | X |  |  |

<a id="_return_type"></a>

## Return Type

[V1CreateServiceIdentityResponse](../CommonObjectReference/CommonObjectReference.md#V1CreateServiceIdentityResponse_CommonObjectReference)

<a id="_content_type"></a>

## Content Type

- application/json

<a id="_responses"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V1CreateServiceIdentityResponse](../CommonObjectReference/CommonObjectReference.md#V1CreateServiceIdentityResponse_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples"></a>

## Samples

<a id="GetAuthorities_ServiceIdentityService"></a>

# GetAuthorities

`GET /v1/authorities`

GetAuthorities returns the authorities currently in use.

<a id="_description_2"></a>

## Description

<a id="_parameters_2"></a>

## Parameters

<a id="_return_type_2"></a>

## Return Type

[V1Authorities](../CommonObjectReference/CommonObjectReference.md#V1Authorities_CommonObjectReference)

<a id="_content_type_2"></a>

## Content Type

- application/json

<a id="_responses_2"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V1Authorities](../CommonObjectReference/CommonObjectReference.md#V1Authorities_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_2"></a>

## Samples

<a id="GetServiceIdentities_ServiceIdentityService"></a>

# GetServiceIdentities

`GET /v1/serviceIdentities`

<a id="_description_3"></a>

## Description

<a id="_parameters_3"></a>

## Parameters

<a id="_return_type_3"></a>

## Return Type

[V1ServiceIdentityResponse](../CommonObjectReference/CommonObjectReference.md#V1ServiceIdentityResponse_CommonObjectReference)

<a id="_content_type_3"></a>

## Content Type

- application/json

<a id="_responses_3"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V1ServiceIdentityResponse](../CommonObjectReference/CommonObjectReference.md#V1ServiceIdentityResponse_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_3"></a>

## Samples
