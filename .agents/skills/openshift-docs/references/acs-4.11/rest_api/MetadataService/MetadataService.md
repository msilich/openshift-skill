<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

<a id="GetCentralCapabilities_MetadataService"></a>

# GetCentralCapabilities

`GET /v1/central-capabilities`

<a id="_description"></a>

## Description

<a id="_parameters"></a>

## Parameters

<a id="_return_type"></a>

## Return Type

[V1CentralServicesCapabilities](../CommonObjectReference/CommonObjectReference.md#V1CentralServicesCapabilities_CommonObjectReference)

<a id="_content_type"></a>

## Content Type

- application/json

<a id="_responses"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V1CentralServicesCapabilities](../CommonObjectReference/CommonObjectReference.md#V1CentralServicesCapabilities_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples"></a>

## Samples

<a id="GetDatabaseBackupStatus_MetadataService"></a>

# GetDatabaseBackupStatus

`GET /v1/backup/status`

<a id="_description_2"></a>

## Description

<a id="_parameters_2"></a>

## Parameters

<a id="_return_type_2"></a>

## Return Type

[V1DatabaseBackupStatus](../CommonObjectReference/CommonObjectReference.md#V1DatabaseBackupStatus_CommonObjectReference)

<a id="_content_type_2"></a>

## Content Type

- application/json

<a id="_responses_2"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V1DatabaseBackupStatus](../CommonObjectReference/CommonObjectReference.md#V1DatabaseBackupStatus_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_2"></a>

## Samples

<a id="GetDatabaseStatus_MetadataService"></a>

# GetDatabaseStatus

`GET /v1/database/status`

<a id="_description_3"></a>

## Description

<a id="_parameters_3"></a>

## Parameters

<a id="_return_type_3"></a>

## Return Type

[V1DatabaseStatus](../CommonObjectReference/CommonObjectReference.md#V1DatabaseStatus_CommonObjectReference)

<a id="_content_type_3"></a>

## Content Type

- application/json

<a id="_responses_3"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V1DatabaseStatus](../CommonObjectReference/CommonObjectReference.md#V1DatabaseStatus_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_3"></a>

## Samples

<a id="GetMetadata_MetadataService"></a>

# GetMetadata

`GET /v1/metadata`

<a id="_description_4"></a>

## Description

<a id="_parameters_4"></a>

## Parameters

<a id="_return_type_4"></a>

## Return Type

[V1Metadata](../CommonObjectReference/CommonObjectReference.md#V1Metadata_CommonObjectReference)

<a id="_content_type_4"></a>

## Content Type

- application/json

<a id="_responses_4"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V1Metadata](../CommonObjectReference/CommonObjectReference.md#V1Metadata_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_4"></a>

## Samples

<a id="TLSChallenge_MetadataService"></a>

# TLSChallenge

`GET /v1/tls-challenge`

TLSChallenge

<a id="_description_5"></a>

## Description

Returns all trusted CAs, i.e., secret/additional-ca and Central’s cert chain. This is necessary if Central is running behind a load balancer with self-signed certificates. Does not require authentication.

<a id="_parameters_5"></a>

## Parameters

<a id="_query_parameters"></a>

### Query Parameters

| Name | Description | Required | Default | Pattern |
|----|----|----|----|----|
| challengeToken | generated challenge token by the service asking for TLS certs | \- | null |  |

<a id="_return_type_5"></a>

## Return Type

[V1TLSChallengeResponse](../CommonObjectReference/CommonObjectReference.md#V1TLSChallengeResponse_CommonObjectReference)

<a id="_content_type_5"></a>

## Content Type

- application/json

<a id="_responses_5"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V1TLSChallengeResponse](../CommonObjectReference/CommonObjectReference.md#V1TLSChallengeResponse_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_5"></a>

## Samples
