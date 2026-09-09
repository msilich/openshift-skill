<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

<a id="ApplyNetworkPolicy_NetworkPolicyService"></a>

# ApplyNetworkPolicy

`POST /v1/networkpolicies/apply/{clusterId}`

<a id="_description"></a>

## Description

<a id="_parameters"></a>

## Parameters

<a id="_path_parameters"></a>

### Path Parameters

| Name      | Description | Required | Default | Pattern |
|-----------|-------------|----------|---------|---------|
| clusterId |             | X        | null    |         |

<a id="_body_parameter"></a>

### Body Parameter

| Name | Description | Required | Default | Pattern |
|----|----|----|----|----|
| modification | [StorageNetworkPolicyModification](../CommonObjectReference/CommonObjectReference.md#StorageNetworkPolicyModification_CommonObjectReference) | X |  |  |

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

<a id="ApplyNetworkPolicyYamlForDeployment_NetworkPolicyService"></a>

# ApplyNetworkPolicyYamlForDeployment

`POST /v1/networkpolicies/apply/deployment/{deploymentId}`

<a id="_description_2"></a>

## Description

<a id="_parameters_2"></a>

## Parameters

<a id="_path_parameters_2"></a>

### Path Parameters

| Name         | Description | Required | Default | Pattern |
|--------------|-------------|----------|---------|---------|
| deploymentId |             | X        | null    |         |

<a id="_body_parameter_2"></a>

### Body Parameter

| Name | Description | Required | Default | Pattern |
|----|----|----|----|----|
| body | [NetworkPolicyServiceApplyNetworkPolicyYamlForDeploymentBody](../CommonObjectReference/CommonObjectReference.md#NetworkPolicyServiceApplyNetworkPolicyYamlForDeploymentBody_CommonObjectReference) | X |  |  |

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

<a id="GenerateNetworkPolicies_NetworkPolicyService"></a>

# GenerateNetworkPolicies

`GET /v1/networkpolicies/generate/{clusterId}`

<a id="_description_3"></a>

## Description

<a id="_parameters_3"></a>

## Parameters

<a id="_path_parameters_3"></a>

### Path Parameters

| Name      | Description | Required | Default | Pattern |
|-----------|-------------|----------|---------|---------|
| clusterId |             | X        | null    |         |

<a id="_query_parameters"></a>

### Query Parameters

| Name | Description | Required | Default | Pattern |
|----|----|----|----|----|
| query |  | \- | null |  |
| deleteExisting | \- NONE: Do not delete any existing network policies. - GENERATED_ONLY: Delete any existing **auto-generated** network policies. - ALL: Delete all existing network policies in the respective namespace. | \- | UNKNOWN |  |
| networkDataSince |  | \- | null |  |
| includePorts |  | \- | null |  |

<a id="_return_type_3"></a>

## Return Type

[V1GenerateNetworkPoliciesResponse](../CommonObjectReference/CommonObjectReference.md#V1GenerateNetworkPoliciesResponse_CommonObjectReference)

<a id="_content_type_3"></a>

## Content Type

- application/json

<a id="_responses_3"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V1GenerateNetworkPoliciesResponse](../CommonObjectReference/CommonObjectReference.md#V1GenerateNetworkPoliciesResponse_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_3"></a>

## Samples

<a id="GetAllowedPeersFromCurrentPolicyForDeployment_NetworkPolicyService"></a>

# GetAllowedPeersFromCurrentPolicyForDeployment

`GET /v1/networkpolicies/allowedpeers/{id}`

<a id="_description_4"></a>

## Description

<a id="_parameters_4"></a>

## Parameters

<a id="_path_parameters_4"></a>

### Path Parameters

| Name | Description | Required | Default | Pattern |
|------|-------------|----------|---------|---------|
| id   |             | X        | null    |         |

<a id="_return_type_4"></a>

## Return Type

[V1GetAllowedPeersFromCurrentPolicyForDeploymentResponse](../CommonObjectReference/CommonObjectReference.md#V1GetAllowedPeersFromCurrentPolicyForDeploymentResponse_CommonObjectReference)

<a id="_content_type_4"></a>

## Content Type

- application/json

<a id="_responses_4"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V1GetAllowedPeersFromCurrentPolicyForDeploymentResponse](../CommonObjectReference/CommonObjectReference.md#V1GetAllowedPeersFromCurrentPolicyForDeploymentResponse_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_4"></a>

## Samples

<a id="GetBaselineGeneratedNetworkPolicyForDeployment_NetworkPolicyService"></a>

# GetBaselineGeneratedNetworkPolicyForDeployment

`POST /v1/networkpolicies/generate/baseline/{deploymentId}`

<a id="_description_5"></a>

## Description

<a id="_parameters_5"></a>

## Parameters

<a id="_path_parameters_5"></a>

### Path Parameters

| Name         | Description | Required | Default | Pattern |
|--------------|-------------|----------|---------|---------|
| deploymentId |             | X        | null    |         |

<a id="_body_parameter_3"></a>

### Body Parameter

| Name | Description | Required | Default | Pattern |
|----|----|----|----|----|
| body | [NetworkPolicyServiceGetBaselineGeneratedNetworkPolicyForDeploymentBody](../CommonObjectReference/CommonObjectReference.md#NetworkPolicyServiceGetBaselineGeneratedNetworkPolicyForDeploymentBody_CommonObjectReference) | X |  |  |

<a id="_return_type_5"></a>

## Return Type

[V1GetBaselineGeneratedPolicyForDeploymentResponse](../CommonObjectReference/CommonObjectReference.md#V1GetBaselineGeneratedPolicyForDeploymentResponse_CommonObjectReference)

<a id="_content_type_5"></a>

## Content Type

- application/json

<a id="_responses_5"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V1GetBaselineGeneratedPolicyForDeploymentResponse](../CommonObjectReference/CommonObjectReference.md#V1GetBaselineGeneratedPolicyForDeploymentResponse_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_5"></a>

## Samples

<a id="GetDiffFlowsBetweenPolicyAndBaselineForDeployment_NetworkPolicyService"></a>

# GetDiffFlowsBetweenPolicyAndBaselineForDeployment

`GET /v1/networkpolicies/baselinecomparison/{id}`

<a id="_description_6"></a>

## Description

<a id="_parameters_6"></a>

## Parameters

<a id="_path_parameters_6"></a>

### Path Parameters

| Name | Description | Required | Default | Pattern |
|------|-------------|----------|---------|---------|
| id   |             | X        | null    |         |

<a id="_return_type_6"></a>

## Return Type

[V1GetDiffFlowsResponse](../CommonObjectReference/CommonObjectReference.md#V1GetDiffFlowsResponse_CommonObjectReference)

<a id="_content_type_6"></a>

## Content Type

- application/json

<a id="_responses_6"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V1GetDiffFlowsResponse](../CommonObjectReference/CommonObjectReference.md#V1GetDiffFlowsResponse_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_6"></a>

## Samples

<a id="GetDiffFlowsFromUndoModificationForDeployment_NetworkPolicyService"></a>

# GetDiffFlowsFromUndoModificationForDeployment

`GET /v1/networkpolicies/undobaselinecomparison/{id}`

<a id="_description_7"></a>

## Description

<a id="_parameters_7"></a>

## Parameters

<a id="_path_parameters_7"></a>

### Path Parameters

| Name | Description | Required | Default | Pattern |
|------|-------------|----------|---------|---------|
| id   |             | X        | null    |         |

<a id="_return_type_7"></a>

## Return Type

[V1GetDiffFlowsResponse](../CommonObjectReference/CommonObjectReference.md#V1GetDiffFlowsResponse_CommonObjectReference)

<a id="_content_type_7"></a>

## Content Type

- application/json

<a id="_responses_7"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V1GetDiffFlowsResponse](../CommonObjectReference/CommonObjectReference.md#V1GetDiffFlowsResponse_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_7"></a>

## Samples

<a id="GetNetworkGraph_NetworkPolicyService"></a>

# GetNetworkGraph

`GET /v1/networkpolicies/cluster/{clusterId}`

<a id="_description_8"></a>

## Description

<a id="_parameters_8"></a>

## Parameters

<a id="_path_parameters_8"></a>

### Path Parameters

| Name      | Description | Required | Default | Pattern |
|-----------|-------------|----------|---------|---------|
| clusterId |             | X        | null    |         |

<a id="_query_parameters_2"></a>

### Query Parameters

| Name | Description | Required | Default | Pattern |
|----|----|----|----|----|
| query |  | \- | null |  |
| includePorts | If set to true, include port-level information in the network policy graph. | \- | null |  |
| scope.query |  | \- | null |  |

<a id="_return_type_8"></a>

## Return Type

[V1NetworkGraph](../CommonObjectReference/CommonObjectReference.md#V1NetworkGraph_CommonObjectReference)

<a id="_content_type_8"></a>

## Content Type

- application/json

<a id="_responses_8"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V1NetworkGraph](../CommonObjectReference/CommonObjectReference.md#V1NetworkGraph_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_8"></a>

## Samples

<a id="GetNetworkGraphEpoch_NetworkPolicyService"></a>

# GetNetworkGraphEpoch

`GET /v1/networkpolicies/graph/epoch`

<a id="_description_9"></a>

## Description

<a id="_parameters_9"></a>

## Parameters

<a id="_query_parameters_3"></a>

### Query Parameters

| Name      | Description | Required | Default | Pattern |
|-----------|-------------|----------|---------|---------|
| clusterId |             | \-       | null    |         |

<a id="_return_type_9"></a>

## Return Type

[V1NetworkGraphEpoch](../CommonObjectReference/CommonObjectReference.md#V1NetworkGraphEpoch_CommonObjectReference)

<a id="_content_type_9"></a>

## Content Type

- application/json

<a id="_responses_9"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V1NetworkGraphEpoch](../CommonObjectReference/CommonObjectReference.md#V1NetworkGraphEpoch_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_9"></a>

## Samples

<a id="GetNetworkPolicies_NetworkPolicyService"></a>

# GetNetworkPolicies

`GET /v1/networkpolicies`

<a id="_description_10"></a>

## Description

<a id="_parameters_10"></a>

## Parameters

<a id="_query_parameters_4"></a>

### Query Parameters

| Name            | Description | Required | Default | Pattern |
|-----------------|-------------|----------|---------|---------|
| clusterId       |             | \-       | null    |         |
| deploymentQuery |             | \-       | null    |         |
| namespace       |             | \-       | null    |         |

<a id="_return_type_10"></a>

## Return Type

[V1NetworkPoliciesResponse](../CommonObjectReference/CommonObjectReference.md#V1NetworkPoliciesResponse_CommonObjectReference)

<a id="_content_type_10"></a>

## Content Type

- application/json

<a id="_responses_10"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V1NetworkPoliciesResponse](../CommonObjectReference/CommonObjectReference.md#V1NetworkPoliciesResponse_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_10"></a>

## Samples

<a id="GetNetworkPolicy_NetworkPolicyService"></a>

# GetNetworkPolicy

`GET /v1/networkpolicies/{id}`

<a id="_description_11"></a>

## Description

<a id="_parameters_11"></a>

## Parameters

<a id="_path_parameters_9"></a>

### Path Parameters

| Name | Description | Required | Default | Pattern |
|------|-------------|----------|---------|---------|
| id   |             | X        | null    |         |

<a id="_return_type_11"></a>

## Return Type

[StorageNetworkPolicy](../CommonObjectReference/CommonObjectReference.md#StorageNetworkPolicy_CommonObjectReference)

<a id="_content_type_11"></a>

## Content Type

- application/json

<a id="_responses_11"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [StorageNetworkPolicy](../CommonObjectReference/CommonObjectReference.md#StorageNetworkPolicy_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_11"></a>

## Samples

<a id="GetUndoModification_NetworkPolicyService"></a>

# GetUndoModification

`GET /v1/networkpolicies/undo/{clusterId}`

<a id="_description_12"></a>

## Description

<a id="_parameters_12"></a>

## Parameters

<a id="_path_parameters_10"></a>

### Path Parameters

| Name      | Description | Required | Default | Pattern |
|-----------|-------------|----------|---------|---------|
| clusterId |             | X        | null    |         |

<a id="_return_type_12"></a>

## Return Type

[V1GetUndoModificationResponse](../CommonObjectReference/CommonObjectReference.md#V1GetUndoModificationResponse_CommonObjectReference)

<a id="_content_type_12"></a>

## Content Type

- application/json

<a id="_responses_12"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V1GetUndoModificationResponse](../CommonObjectReference/CommonObjectReference.md#V1GetUndoModificationResponse_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_12"></a>

## Samples

<a id="GetUndoModificationForDeployment_NetworkPolicyService"></a>

# GetUndoModificationForDeployment

`GET /v1/networkpolicies/undo/deployment/{id}`

<a id="_description_13"></a>

## Description

<a id="_parameters_13"></a>

## Parameters

<a id="_path_parameters_11"></a>

### Path Parameters

| Name | Description | Required | Default | Pattern |
|------|-------------|----------|---------|---------|
| id   |             | X        | null    |         |

<a id="_return_type_13"></a>

## Return Type

[V1GetUndoModificationForDeploymentResponse](../CommonObjectReference/CommonObjectReference.md#V1GetUndoModificationForDeploymentResponse_CommonObjectReference)

<a id="_content_type_13"></a>

## Content Type

- application/json

<a id="_responses_13"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V1GetUndoModificationForDeploymentResponse](../CommonObjectReference/CommonObjectReference.md#V1GetUndoModificationForDeploymentResponse_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_13"></a>

## Samples

<a id="SendNetworkPolicyYAML_NetworkPolicyService"></a>

# SendNetworkPolicyYAML

`POST /v1/networkpolicies/simulate/{clusterId}/notify`

<a id="_description_14"></a>

## Description

<a id="_parameters_14"></a>

## Parameters

<a id="_path_parameters_12"></a>

### Path Parameters

| Name      | Description | Required | Default | Pattern |
|-----------|-------------|----------|---------|---------|
| clusterId |             | X        | null    |         |

<a id="_body_parameter_4"></a>

### Body Parameter

| Name | Description | Required | Default | Pattern |
|----|----|----|----|----|
| modification | [StorageNetworkPolicyModification](../CommonObjectReference/CommonObjectReference.md#StorageNetworkPolicyModification_CommonObjectReference) | X |  |  |

<a id="_query_parameters_5"></a>

### Query Parameters

| Name        | Description | Required | Default | Pattern |
|-------------|-------------|----------|---------|---------|
| notifierIds | `String`    | \-       | null    |         |

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

<a id="SimulateNetworkGraph_NetworkPolicyService"></a>

# SimulateNetworkGraph

`POST /v1/networkpolicies/simulate/{clusterId}`

<a id="_description_15"></a>

## Description

<a id="_parameters_15"></a>

## Parameters

<a id="_path_parameters_13"></a>

### Path Parameters

| Name      | Description | Required | Default | Pattern |
|-----------|-------------|----------|---------|---------|
| clusterId |             | X        | null    |         |

<a id="_body_parameter_5"></a>

### Body Parameter

| Name | Description | Required | Default | Pattern |
|----|----|----|----|----|
| modification | [StorageNetworkPolicyModification](../CommonObjectReference/CommonObjectReference.md#StorageNetworkPolicyModification_CommonObjectReference) | X |  |  |

<a id="_query_parameters_6"></a>

### Query Parameters

| Name | Description | Required | Default | Pattern |
|----|----|----|----|----|
| query |  | \- | null |  |
| includePorts | If set to true, include port-level information in the network policy graph. | \- | null |  |
| includeNodeDiff |  | \- | null |  |
| scope.query |  | \- | null |  |

<a id="_return_type_15"></a>

## Return Type

[V1SimulateNetworkGraphResponse](../CommonObjectReference/CommonObjectReference.md#V1SimulateNetworkGraphResponse_CommonObjectReference)

<a id="_content_type_15"></a>

## Content Type

- application/json

<a id="_responses_15"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V1SimulateNetworkGraphResponse](../CommonObjectReference/CommonObjectReference.md#V1SimulateNetworkGraphResponse_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_15"></a>

## Samples
