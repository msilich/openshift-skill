<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

<a id="GetCertExpiry_CredentialExpiryService"></a>

# GetCertExpiry

`GET /v1/credentialexpiry`

GetCertExpiry returns information related to the expiry component mTLS certificate.

<a id="_description"></a>

## Description

<a id="_parameters"></a>

## Parameters

<a id="_query_parameters"></a>

### Query Parameters

| Name      | Description | Required | Default | Pattern |
|-----------|-------------|----------|---------|---------|
| component |             | \-       | UNKNOWN |         |

<a id="_return_type"></a>

## Return Type

[V1GetCertExpiryResponse](../CommonObjectReference/CommonObjectReference.md#V1GetCertExpiryResponse_CommonObjectReference)

<a id="_content_type"></a>

## Content Type

- application/json

<a id="_responses"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V1GetCertExpiryResponse](../CommonObjectReference/CommonObjectReference.md#V1GetCertExpiryResponse_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples"></a>

## Samples
