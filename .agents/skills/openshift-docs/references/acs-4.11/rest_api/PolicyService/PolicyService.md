<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

<a id="CancelDryRunJob_PolicyService"></a>

# CancelDryRunJob

`DELETE /v1/policies/dryrunjob/{jobId}`

<a id="_description"></a>

## Description

<a id="_parameters"></a>

## Parameters

<a id="_path_parameters"></a>

### Path Parameters

| Name  | Description | Required | Default | Pattern |
|-------|-------------|----------|---------|---------|
| jobId |             | X        | null    |         |

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

<a id="DeletePolicy_PolicyService"></a>

# DeletePolicy

`DELETE /v1/policies/{id}`

DeletePolicy removes a policy by ID.

<a id="_description_2"></a>

## Description

<a id="_parameters_2"></a>

## Parameters

<a id="_path_parameters_2"></a>

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

<a id="DryRunPolicy_PolicyService"></a>

# DryRunPolicy

`POST /v1/policies/dryrun`

DryRunPolicy evaluates the given policy and returns any alerts without creating the policy.

<a id="_description_3"></a>

## Description

<a id="_parameters_3"></a>

## Parameters

<a id="_body_parameter"></a>

### Body Parameter

| Name | Description | Required | Default | Pattern |
|----|----|----|----|----|
| body | [StoragePolicy](../CommonObjectReference/CommonObjectReference.md#StoragePolicy_CommonObjectReference) | X |  |  |

<a id="_return_type_3"></a>

## Return Type

[V1DryRunResponse](../CommonObjectReference/CommonObjectReference.md#V1DryRunResponse_CommonObjectReference)

<a id="_content_type_3"></a>

## Content Type

- application/json

<a id="_responses_3"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V1DryRunResponse](../CommonObjectReference/CommonObjectReference.md#V1DryRunResponse_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_3"></a>

## Samples

<a id="EnableDisablePolicyNotification_PolicyService"></a>

# EnableDisablePolicyNotification

`PATCH /v1/policies/{policyId}/notifiers`

EnableDisablePolicyNotification enables or disables notifications for a policy by ID.

<a id="_description_4"></a>

## Description

<a id="_parameters_4"></a>

## Parameters

<a id="_path_parameters_3"></a>

### Path Parameters

| Name     | Description | Required | Default | Pattern |
|----------|-------------|----------|---------|---------|
| policyId |             | X        | null    |         |

<a id="_body_parameter_2"></a>

### Body Parameter

| Name | Description | Required | Default | Pattern |
|----|----|----|----|----|
| body | [PolicyServiceEnableDisablePolicyNotificationBody](../CommonObjectReference/CommonObjectReference.md#PolicyServiceEnableDisablePolicyNotificationBody_CommonObjectReference) | X |  |  |

<a id="_return_type_4"></a>

## Return Type

`Object`

<a id="_content_type_4"></a>

## Content Type

- application/json

<a id="_responses_4"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | `Object` |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_4"></a>

## Samples

<a id="ExportPolicies_PolicyService"></a>

# ExportPolicies

`POST /v1/policies/export`

ExportPolicies takes a list of policy IDs and returns either the entire list of policies or an error message

<a id="_description_5"></a>

## Description

<a id="_parameters_5"></a>

## Parameters

<a id="_body_parameter_3"></a>

### Body Parameter

| Name | Description | Required | Default | Pattern |
|----|----|----|----|----|
| body | [V1ExportPoliciesRequest](../CommonObjectReference/CommonObjectReference.md#V1ExportPoliciesRequest_CommonObjectReference) | X |  |  |

<a id="_return_type_5"></a>

## Return Type

[StorageExportPoliciesResponse](../CommonObjectReference/CommonObjectReference.md#StorageExportPoliciesResponse_CommonObjectReference)

<a id="_content_type_5"></a>

## Content Type

- application/json

<a id="_responses_5"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [StorageExportPoliciesResponse](../CommonObjectReference/CommonObjectReference.md#StorageExportPoliciesResponse_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_5"></a>

## Samples

<a id="GetPolicy_PolicyService"></a>

# GetPolicy

`GET /v1/policies/{id}`

GetPolicy returns the requested policy by ID.

<a id="_description_6"></a>

## Description

<a id="_parameters_6"></a>

## Parameters

<a id="_path_parameters_4"></a>

### Path Parameters

| Name | Description | Required | Default | Pattern |
|------|-------------|----------|---------|---------|
| id   |             | X        | null    |         |

<a id="_return_type_6"></a>

## Return Type

[StoragePolicy](../CommonObjectReference/CommonObjectReference.md#StoragePolicy_CommonObjectReference)

<a id="_content_type_6"></a>

## Content Type

- application/json

<a id="_responses_6"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [StoragePolicy](../CommonObjectReference/CommonObjectReference.md#StoragePolicy_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_6"></a>

## Samples

<a id="GetPolicyCategories_PolicyService"></a>

# GetPolicyCategories

`GET /v1/policyCategories`

GetPolicyCategories returns the policy categories.

<a id="_description_7"></a>

## Description

<a id="_parameters_7"></a>

## Parameters

<a id="_return_type_7"></a>

## Return Type

[V1PolicyCategoriesResponse](../CommonObjectReference/CommonObjectReference.md#V1PolicyCategoriesResponse_CommonObjectReference)

<a id="_content_type_7"></a>

## Content Type

- application/json

<a id="_responses_7"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V1PolicyCategoriesResponse](../CommonObjectReference/CommonObjectReference.md#V1PolicyCategoriesResponse_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_7"></a>

## Samples

<a id="GetPolicyMitreVectors_PolicyService"></a>

# GetPolicyMitreVectors

`GET /v1/policies/{id}/mitrevectors`

GetMitreVectorsForPolicy returns the requested policy by ID.

<a id="_description_8"></a>

## Description

<a id="_parameters_8"></a>

## Parameters

<a id="_path_parameters_5"></a>

### Path Parameters

| Name | Description | Required | Default | Pattern |
|------|-------------|----------|---------|---------|
| id   |             | X        | null    |         |

<a id="_query_parameters"></a>

### Query Parameters

| Name | Description | Required | Default | Pattern |
|----|----|----|----|----|
| options.excludePolicy | If set to true, policy is excluded from the response. | \- | null |  |

<a id="_return_type_8"></a>

## Return Type

[V1GetPolicyMitreVectorsResponse](../CommonObjectReference/CommonObjectReference.md#V1GetPolicyMitreVectorsResponse_CommonObjectReference)

<a id="_content_type_8"></a>

## Content Type

- application/json

<a id="_responses_8"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V1GetPolicyMitreVectorsResponse](../CommonObjectReference/CommonObjectReference.md#V1GetPolicyMitreVectorsResponse_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_8"></a>

## Samples

<a id="ImportPolicies_PolicyService"></a>

# ImportPolicies

`POST /v1/policies/import`

ImportPolicies accepts a list of Policies and returns a list of the policies which could not be imported

<a id="_description_9"></a>

## Description

<a id="_parameters_9"></a>

## Parameters

<a id="_body_parameter_4"></a>

### Body Parameter

| Name | Description | Required | Default | Pattern |
|----|----|----|----|----|
| body | [V1ImportPoliciesRequest](../CommonObjectReference/CommonObjectReference.md#V1ImportPoliciesRequest_CommonObjectReference) | X |  |  |

<a id="_return_type_9"></a>

## Return Type

[V1ImportPoliciesResponse](../CommonObjectReference/CommonObjectReference.md#V1ImportPoliciesResponse_CommonObjectReference)

<a id="_content_type_9"></a>

## Content Type

- application/json

<a id="_responses_9"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V1ImportPoliciesResponse](../CommonObjectReference/CommonObjectReference.md#V1ImportPoliciesResponse_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_9"></a>

## Samples

<a id="ListPolicies_PolicyService"></a>

# ListPolicies

`GET /v1/policies`

ListPolicies returns the list of policies.

<a id="_description_10"></a>

## Description

<a id="_parameters_10"></a>

## Parameters

<a id="_query_parameters_2"></a>

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

<a id="_return_type_10"></a>

## Return Type

[V1ListPoliciesResponse](../CommonObjectReference/CommonObjectReference.md#V1ListPoliciesResponse_CommonObjectReference)

<a id="_content_type_10"></a>

## Content Type

- application/json

<a id="_responses_10"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V1ListPoliciesResponse](../CommonObjectReference/CommonObjectReference.md#V1ListPoliciesResponse_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_10"></a>

## Samples

<a id="PatchPolicy_PolicyService"></a>

# PatchPolicy

`PATCH /v1/policies/{id}`

PatchPolicy edits an existing policy.

<a id="_description_11"></a>

## Description

<a id="_parameters_11"></a>

## Parameters

<a id="_path_parameters_6"></a>

### Path Parameters

| Name | Description | Required | Default | Pattern |
|------|-------------|----------|---------|---------|
| id   |             | X        | null    |         |

<a id="_body_parameter_5"></a>

### Body Parameter

| Name | Description | Required | Default | Pattern |
|----|----|----|----|----|
| body | [PolicyServicePatchPolicyBody](../CommonObjectReference/CommonObjectReference.md#PolicyServicePatchPolicyBody_CommonObjectReference) | X |  |  |

<a id="_return_type_11"></a>

## Return Type

`Object`

<a id="_content_type_11"></a>

## Content Type

- application/json

<a id="_responses_11"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | `Object` |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_11"></a>

## Samples

<a id="PolicyFromSearch_PolicyService"></a>

# PolicyFromSearch

`POST /v1/policies/from-search`

<a id="_description_12"></a>

## Description

<a id="_parameters_12"></a>

## Parameters

<a id="_body_parameter_6"></a>

### Body Parameter

| Name | Description | Required | Default | Pattern |
|----|----|----|----|----|
| body | [V1PolicyFromSearchRequest](../CommonObjectReference/CommonObjectReference.md#V1PolicyFromSearchRequest_CommonObjectReference) | X |  |  |

<a id="_return_type_12"></a>

## Return Type

[V1PolicyFromSearchResponse](../CommonObjectReference/CommonObjectReference.md#V1PolicyFromSearchResponse_CommonObjectReference)

<a id="_content_type_12"></a>

## Content Type

- application/json

<a id="_responses_12"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V1PolicyFromSearchResponse](../CommonObjectReference/CommonObjectReference.md#V1PolicyFromSearchResponse_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_12"></a>

## Samples

<a id="PostPolicy_PolicyService"></a>

# PostPolicy

`POST /v1/policies`

PostPolicy creates a new policy.

<a id="_description_13"></a>

## Description

<a id="_parameters_13"></a>

## Parameters

<a id="_body_parameter_7"></a>

### Body Parameter

| Name | Description | Required | Default | Pattern |
|----|----|----|----|----|
| policy | [StoragePolicy](../CommonObjectReference/CommonObjectReference.md#StoragePolicy_CommonObjectReference) | X |  |  |

<a id="_query_parameters_3"></a>

### Query Parameters

| Name                   | Description | Required | Default | Pattern |
|------------------------|-------------|----------|---------|---------|
| enableStrictValidation |             | \-       | null    |         |

<a id="_return_type_13"></a>

## Return Type

[StoragePolicy](../CommonObjectReference/CommonObjectReference.md#StoragePolicy_CommonObjectReference)

<a id="_content_type_13"></a>

## Content Type

- application/json

<a id="_responses_13"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [StoragePolicy](../CommonObjectReference/CommonObjectReference.md#StoragePolicy_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_13"></a>

## Samples

<a id="PutPolicy_PolicyService"></a>

# PutPolicy

`PUT /v1/policies/{id}`

PutPolicy modifies an existing policy.

<a id="_description_14"></a>

## Description

<a id="_parameters_14"></a>

## Parameters

<a id="_path_parameters_7"></a>

### Path Parameters

| Name | Description | Required | Default | Pattern |
|------|-------------|----------|---------|---------|
| id   |             | X        | null    |         |

<a id="_body_parameter_8"></a>

### Body Parameter

| Name | Description | Required | Default | Pattern |
|----|----|----|----|----|
| body | [PolicyServicePutPolicyBody](../CommonObjectReference/CommonObjectReference.md#PolicyServicePutPolicyBody_CommonObjectReference) | X |  |  |

<a id="_return_type_14"></a>

## Return Type

`Object`

<a id="_content_type_14"></a>

## Content Type

- application/json

<a id="_responses_14"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | `Object` |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_14"></a>

## Samples

<a id="QueryDryRunJobStatus_PolicyService"></a>

# QueryDryRunJobStatus

`GET /v1/policies/dryrunjob/{jobId}`

<a id="_description_15"></a>

## Description

<a id="_parameters_15"></a>

## Parameters

<a id="_path_parameters_8"></a>

### Path Parameters

| Name  | Description | Required | Default | Pattern |
|-------|-------------|----------|---------|---------|
| jobId |             | X        | null    |         |

<a id="_return_type_15"></a>

## Return Type

[V1DryRunJobStatusResponse](../CommonObjectReference/CommonObjectReference.md#V1DryRunJobStatusResponse_CommonObjectReference)

<a id="_content_type_15"></a>

## Content Type

- application/json

<a id="_responses_15"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V1DryRunJobStatusResponse](../CommonObjectReference/CommonObjectReference.md#V1DryRunJobStatusResponse_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_15"></a>

## Samples

<a id="ReassessPolicies_PolicyService"></a>

# ReassessPolicies

`POST /v1/policies/reassess`

ReassessPolicies reevaluates all the policies.

<a id="_description_16"></a>

## Description

<a id="_parameters_16"></a>

## Parameters

<a id="_return_type_16"></a>

## Return Type

`Object`

<a id="_content_type_16"></a>

## Content Type

- application/json

<a id="_responses_16"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | `Object` |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_16"></a>

## Samples

<a id="SubmitDryRunPolicyJob_PolicyService"></a>

# SubmitDryRunPolicyJob

`POST /v1/policies/dryrunjob`

<a id="_description_17"></a>

## Description

<a id="_parameters_17"></a>

## Parameters

<a id="_body_parameter_9"></a>

### Body Parameter

| Name | Description | Required | Default | Pattern |
|----|----|----|----|----|
| body | [StoragePolicy](../CommonObjectReference/CommonObjectReference.md#StoragePolicy_CommonObjectReference) | X |  |  |

<a id="_return_type_17"></a>

## Return Type

[V1JobId](../CommonObjectReference/CommonObjectReference.md#V1JobId_CommonObjectReference)

<a id="_content_type_17"></a>

## Content Type

- application/json

<a id="_responses_17"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V1JobId](../CommonObjectReference/CommonObjectReference.md#V1JobId_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_17"></a>

## Samples
