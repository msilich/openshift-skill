<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

<a id="GenerateCRS_ClusterInitService"></a>

# GenerateCRS

`POST /v1/cluster-init/crs`

<a id="_description"></a>

## Description

<a id="_parameters"></a>

## Parameters

<a id="_body_parameter"></a>

### Body Parameter

| Name | Description | Required | Default | Pattern |
|----|----|----|----|----|
| body | [V1CRSGenRequest](../CommonObjectReference/CommonObjectReference.md#V1CRSGenRequest_CommonObjectReference) | X |  |  |

<a id="_return_type"></a>

## Return Type

[V1CRSGenResponse](../CommonObjectReference/CommonObjectReference.md#V1CRSGenResponse_CommonObjectReference)

<a id="_content_type"></a>

## Content Type

- application/json

<a id="_responses"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V1CRSGenResponse](../CommonObjectReference/CommonObjectReference.md#V1CRSGenResponse_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples"></a>

## Samples

<a id="GenerateCRSExtended_ClusterInitService"></a>

# GenerateCRSExtended

`POST /v1/cluster-init/crs-extended`

<a id="_description_2"></a>

## Description

<a id="_parameters_2"></a>

## Parameters

<a id="_body_parameter_2"></a>

### Body Parameter

| Name | Description | Required | Default | Pattern |
|----|----|----|----|----|
| body | [V1CRSGenRequestExtended](../CommonObjectReference/CommonObjectReference.md#V1CRSGenRequestExtended_CommonObjectReference) | X |  |  |

<a id="_return_type_2"></a>

## Return Type

[V1CRSGenResponse](../CommonObjectReference/CommonObjectReference.md#V1CRSGenResponse_CommonObjectReference)

<a id="_content_type_2"></a>

## Content Type

- application/json

<a id="_responses_2"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V1CRSGenResponse](../CommonObjectReference/CommonObjectReference.md#V1CRSGenResponse_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_2"></a>

## Samples

<a id="GenerateInitBundle_ClusterInitService"></a>

# GenerateInitBundle

`POST /v1/cluster-init/init-bundles`

Init bundles are deprecated in favor of Cluster Registration Secrets (CRS).

<a id="_description_3"></a>

## Description

<a id="_parameters_3"></a>

## Parameters

<a id="_body_parameter_3"></a>

### Body Parameter

| Name | Description | Required | Default | Pattern |
|----|----|----|----|----|
| body | [V1InitBundleGenRequest](../CommonObjectReference/CommonObjectReference.md#V1InitBundleGenRequest_CommonObjectReference) | X |  |  |

<a id="_return_type_3"></a>

## Return Type

[V1InitBundleGenResponse](../CommonObjectReference/CommonObjectReference.md#V1InitBundleGenResponse_CommonObjectReference)

<a id="_content_type_3"></a>

## Content Type

- application/json

<a id="_responses_3"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V1InitBundleGenResponse](../CommonObjectReference/CommonObjectReference.md#V1InitBundleGenResponse_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_3"></a>

## Samples

<a id="GetCAConfig_ClusterInitService"></a>

# GetCAConfig

`GET /v1/cluster-init/ca-config`

GetCAConfig is deprecated. Use operator-based installation with CRS instead.

<a id="_description_4"></a>

## Description

<a id="_parameters_4"></a>

## Parameters

<a id="_return_type_4"></a>

## Return Type

[V1GetCAConfigResponse](../CommonObjectReference/CommonObjectReference.md#V1GetCAConfigResponse_CommonObjectReference)

<a id="_content_type_4"></a>

## Content Type

- application/json

<a id="_responses_4"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V1GetCAConfigResponse](../CommonObjectReference/CommonObjectReference.md#V1GetCAConfigResponse_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_4"></a>

## Samples

<a id="GetCRSs_ClusterInitService"></a>

# GetCRSs

`GET /v1/cluster-init/crs`

<a id="_description_5"></a>

## Description

<a id="_parameters_5"></a>

## Parameters

<a id="_return_type_5"></a>

## Return Type

[V1CRSMetasResponse](../CommonObjectReference/CommonObjectReference.md#V1CRSMetasResponse_CommonObjectReference)

<a id="_content_type_5"></a>

## Content Type

- application/json

<a id="_responses_5"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V1CRSMetasResponse](../CommonObjectReference/CommonObjectReference.md#V1CRSMetasResponse_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_5"></a>

## Samples

<a id="GetInitBundles_ClusterInitService"></a>

# GetInitBundles

`GET /v1/cluster-init/init-bundles`

Init bundles are deprecated in favor of Cluster Registration Secrets (CRS).

<a id="_description_6"></a>

## Description

<a id="_parameters_6"></a>

## Parameters

<a id="_return_type_6"></a>

## Return Type

[V1InitBundleMetasResponse](../CommonObjectReference/CommonObjectReference.md#V1InitBundleMetasResponse_CommonObjectReference)

<a id="_content_type_6"></a>

## Content Type

- application/json

<a id="_responses_6"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V1InitBundleMetasResponse](../CommonObjectReference/CommonObjectReference.md#V1InitBundleMetasResponse_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_6"></a>

## Samples

<a id="RevokeCRS_ClusterInitService"></a>

# RevokeCRS

`PATCH /v1/cluster-init/crs/revoke`

RevokeCRSBundle deletes cluster registration secrets.

<a id="_description_7"></a>

## Description

<a id="_parameters_7"></a>

## Parameters

<a id="_body_parameter_4"></a>

### Body Parameter

| Name | Description | Required | Default | Pattern |
|----|----|----|----|----|
| body | [V1CRSRevokeRequest](../CommonObjectReference/CommonObjectReference.md#V1CRSRevokeRequest_CommonObjectReference) | X |  |  |

<a id="_return_type_7"></a>

## Return Type

[V1CRSRevokeResponse](../CommonObjectReference/CommonObjectReference.md#V1CRSRevokeResponse_CommonObjectReference)

<a id="_content_type_7"></a>

## Content Type

- application/json

<a id="_responses_7"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V1CRSRevokeResponse](../CommonObjectReference/CommonObjectReference.md#V1CRSRevokeResponse_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_7"></a>

## Samples

<a id="RevokeInitBundle_ClusterInitService"></a>

# RevokeInitBundle

`PATCH /v1/cluster-init/init-bundles/revoke`

RevokeInitBundle deletes cluster init bundle. If this operation impacts any cluster then its ID should be included in request. If confirm_impacted_clusters_ids does not match with current impacted clusters then request will fail with error that includes all impacted clusters. Init bundles are deprecated in favor of Cluster Registration Secrets (CRS).

<a id="_description_8"></a>

## Description

<a id="_parameters_8"></a>

## Parameters

<a id="_body_parameter_5"></a>

### Body Parameter

| Name | Description | Required | Default | Pattern |
|----|----|----|----|----|
| body | [V1InitBundleRevokeRequest](../CommonObjectReference/CommonObjectReference.md#V1InitBundleRevokeRequest_CommonObjectReference) | X |  |  |

<a id="_return_type_8"></a>

## Return Type

[V1InitBundleRevokeResponse](../CommonObjectReference/CommonObjectReference.md#V1InitBundleRevokeResponse_CommonObjectReference)

<a id="_content_type_8"></a>

## Content Type

- application/json

<a id="_responses_8"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V1InitBundleRevokeResponse](../CommonObjectReference/CommonObjectReference.md#V1InitBundleRevokeResponse_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_8"></a>

## Samples
