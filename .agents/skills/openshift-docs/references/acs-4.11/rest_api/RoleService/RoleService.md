<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

<a id="ComputeEffectiveAccessScope_RoleService"></a>

# ComputeEffectiveAccessScope

`POST /v1/computeeffectiveaccessscope`

ComputeEffectiveAccessScope

<a id="_description"></a>

## Description

Returns effective access scope based on the rules in the request. Does not persist anything; not idempotent due to possible changes to clusters and namespaces. POST is chosen due to potentially large payload. There are advantages in both keeping the response slim and detailed. If only IDs of selected clusters and namespaces are included, response latency and processing time are lower but the caller shall overlay the response with its view of the world which is susceptible to consistency issues. Listing all clusters and namespaces with related metadata is convenient for the caller but bloat the message with secondary data. We let the caller decide what level of detail they would like to have: - Minimal, when only roots of included subtrees are listed by their IDs. Clusters can be either INCLUDED (its namespaces are included but are not listed) or PARTIAL (at least one namespace is explicitly included). Namespaces can only be INCLUDED. - Standard \[default\], when all known clusters and namespaces are listed with their IDs and names. Clusters can be INCLUDED (all its namespaces are explicitly listed as INCLUDED), PARTIAL (all its namespaces are explicitly listed, some as INCLUDED and some as EXCLUDED), and EXCLUDED (all its namespaces are explicitly listed as EXCLUDED). Namespaces can be either INCLUDED or EXCLUDED. - High, when every cluster and namespace is augmented with metadata.

<a id="_parameters"></a>

## Parameters

<a id="_body_parameter"></a>

### Body Parameter

| Name | Description | Required | Default | Pattern |
|----|----|----|----|----|
| accessScope | [ComputeEffectiveAccessScopeRequestPayload](../CommonObjectReference/CommonObjectReference.md#ComputeEffectiveAccessScopeRequestPayload_CommonObjectReference) | X |  |  |

<a id="_query_parameters"></a>

### Query Parameters

| Name   | Description | Required | Default  | Pattern |
|--------|-------------|----------|----------|---------|
| detail |             | \-       | STANDARD |         |

<a id="_return_type"></a>

## Return Type

[StorageEffectiveAccessScope](../CommonObjectReference/CommonObjectReference.md#StorageEffectiveAccessScope_CommonObjectReference)

<a id="_content_type"></a>

## Content Type

- application/json

<a id="_responses"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [StorageEffectiveAccessScope](../CommonObjectReference/CommonObjectReference.md#StorageEffectiveAccessScope_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples"></a>

## Samples

<a id="CreateRole_RoleService"></a>

# CreateRole

`POST /v1/roles/{name}`

<a id="_description_2"></a>

## Description

<a id="_parameters_2"></a>

## Parameters

<a id="_path_parameters"></a>

### Path Parameters

| Name | Description | Required | Default | Pattern |
|------|-------------|----------|---------|---------|
| name |             | X        | null    |         |

<a id="_body_parameter_2"></a>

### Body Parameter

| Name | Description | Required | Default | Pattern |
|----|----|----|----|----|
| role | [StorageRole](../CommonObjectReference/CommonObjectReference.md#StorageRole_CommonObjectReference) | X |  |  |

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

<a id="DeletePermissionSet_RoleService"></a>

# DeletePermissionSet

`DELETE /v1/permissionsets/{id}`

<a id="_description_3"></a>

## Description

<a id="_parameters_3"></a>

## Parameters

<a id="_path_parameters_2"></a>

### Path Parameters

| Name | Description | Required | Default | Pattern |
|------|-------------|----------|---------|---------|
| id   |             | X        | null    |         |

<a id="_return_type_3"></a>

## Return Type

`Object`

<a id="_content_type_3"></a>

## Content Type

- application/json

<a id="_responses_3"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | `Object` |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_3"></a>

## Samples

<a id="DeleteRole_RoleService"></a>

# DeleteRole

`DELETE /v1/roles/{id}`

<a id="_description_4"></a>

## Description

<a id="_parameters_4"></a>

## Parameters

<a id="_path_parameters_3"></a>

### Path Parameters

| Name | Description | Required | Default | Pattern |
|------|-------------|----------|---------|---------|
| id   |             | X        | null    |         |

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

<a id="DeleteSimpleAccessScope_RoleService"></a>

# DeleteSimpleAccessScope

`DELETE /v1/simpleaccessscopes/{id}`

<a id="_description_5"></a>

## Description

<a id="_parameters_5"></a>

## Parameters

<a id="_path_parameters_4"></a>

### Path Parameters

| Name | Description | Required | Default | Pattern |
|------|-------------|----------|---------|---------|
| id   |             | X        | null    |         |

<a id="_return_type_5"></a>

## Return Type

`Object`

<a id="_content_type_5"></a>

## Content Type

- application/json

<a id="_responses_5"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | `Object` |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_5"></a>

## Samples

<a id="GetClustersForPermissions_RoleService"></a>

# GetClustersForPermissions

`GET /v1/sac/clusters`

GetClustersForPermissions

<a id="_description_6"></a>

## Description

Returns the list of cluster ID and cluster name pairs that have at least read allowed by the scope of the requesting user for the list of requested permissions. Effective access scopes are only considered for input permissions that have cluster scope or narrower (i.e. global permissions from the input are ignored). If the input only contains permissions at global level, the output will be an empty list. If no permission is given in input, all clusters allowed by the requester scope for any permission with cluster scope or narrower will be part of the response.

<a id="_parameters_6"></a>

## Parameters

<a id="_query_parameters_2"></a>

### Query Parameters

| Name | Description | Required | Default | Pattern |
|----|----|----|----|----|
| pagination.limit |  | \- | null |  |
| pagination.offset |  | \- | null |  |
| pagination.sortOption.field |  | \- | null |  |
| pagination.sortOption.reversed |  | \- | null |  |
| pagination.sortOption.aggregateBy.aggrFunc |  | \- | UNSET |  |
| pagination.sortOption.aggregateBy.distinct |  | \- | null |  |
| permissions | `String` | \- | null |  |

<a id="_return_type_6"></a>

## Return Type

[V1GetClustersForPermissionsResponse](../CommonObjectReference/CommonObjectReference.md#V1GetClustersForPermissionsResponse_CommonObjectReference)

<a id="_content_type_6"></a>

## Content Type

- application/json

<a id="_responses_6"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V1GetClustersForPermissionsResponse](../CommonObjectReference/CommonObjectReference.md#V1GetClustersForPermissionsResponse_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_6"></a>

## Samples

<a id="GetMyPermissions_RoleService"></a>

# GetMyPermissions

`GET /v1/mypermissions`

<a id="_description_7"></a>

## Description

<a id="_parameters_7"></a>

## Parameters

<a id="_return_type_7"></a>

## Return Type

[V1GetPermissionsResponse](../CommonObjectReference/CommonObjectReference.md#V1GetPermissionsResponse_CommonObjectReference)

<a id="_content_type_7"></a>

## Content Type

- application/json

<a id="_responses_7"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V1GetPermissionsResponse](../CommonObjectReference/CommonObjectReference.md#V1GetPermissionsResponse_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_7"></a>

## Samples

<a id="GetNamespacesForClusterAndPermissions_RoleService"></a>

# GetNamespacesForClusterAndPermissions

`GET /v1/sac/clusters/{clusterId}/namespaces`

GetNamespacesForClusterAndPermissions

<a id="_description_8"></a>

## Description

Returns the list of namespace ID and namespace name pairs that belong to the requested cluster and for which the user has at least read access granted for the list of requested permissions that have namespace scope or narrower (i.e. global and cluster permissions from the input are ignored). If the input only contains permissions at global or cluster level, the output will be an empty list. If no permission is given in input, all namespaces allowed by the requester scope for any permission with namespace scope or narrower will be part of the response.

<a id="_parameters_8"></a>

## Parameters

<a id="_path_parameters_5"></a>

### Path Parameters

| Name      | Description | Required | Default | Pattern |
|-----------|-------------|----------|---------|---------|
| clusterId |             | X        | null    |         |

<a id="_query_parameters_3"></a>

### Query Parameters

| Name        | Description | Required | Default | Pattern |
|-------------|-------------|----------|---------|---------|
| permissions | `String`    | \-       | null    |         |

<a id="_return_type_8"></a>

## Return Type

[V1GetNamespacesForClusterAndPermissionsResponse](../CommonObjectReference/CommonObjectReference.md#V1GetNamespacesForClusterAndPermissionsResponse_CommonObjectReference)

<a id="_content_type_8"></a>

## Content Type

- application/json

<a id="_responses_8"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V1GetNamespacesForClusterAndPermissionsResponse](../CommonObjectReference/CommonObjectReference.md#V1GetNamespacesForClusterAndPermissionsResponse_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_8"></a>

## Samples

<a id="GetPermissionSet_RoleService"></a>

# GetPermissionSet

`GET /v1/permissionsets/{id}`

<a id="_description_9"></a>

## Description

<a id="_parameters_9"></a>

## Parameters

<a id="_path_parameters_6"></a>

### Path Parameters

| Name | Description | Required | Default | Pattern |
|------|-------------|----------|---------|---------|
| id   |             | X        | null    |         |

<a id="_return_type_9"></a>

## Return Type

[StoragePermissionSet](../CommonObjectReference/CommonObjectReference.md#StoragePermissionSet_CommonObjectReference)

<a id="_content_type_9"></a>

## Content Type

- application/json

<a id="_responses_9"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [StoragePermissionSet](../CommonObjectReference/CommonObjectReference.md#StoragePermissionSet_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_9"></a>

## Samples

<a id="GetResources_RoleService"></a>

# GetResources

`GET /v1/resources`

<a id="_description_10"></a>

## Description

<a id="_parameters_10"></a>

## Parameters

<a id="_return_type_10"></a>

## Return Type

[V1GetResourcesResponse](../CommonObjectReference/CommonObjectReference.md#V1GetResourcesResponse_CommonObjectReference)

<a id="_content_type_10"></a>

## Content Type

- application/json

<a id="_responses_10"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V1GetResourcesResponse](../CommonObjectReference/CommonObjectReference.md#V1GetResourcesResponse_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_10"></a>

## Samples

<a id="GetRole_RoleService"></a>

# GetRole

`GET /v1/roles/{id}`

<a id="_description_11"></a>

## Description

<a id="_parameters_11"></a>

## Parameters

<a id="_path_parameters_7"></a>

### Path Parameters

| Name | Description | Required | Default | Pattern |
|------|-------------|----------|---------|---------|
| id   |             | X        | null    |         |

<a id="_return_type_11"></a>

## Return Type

[StorageRole](../CommonObjectReference/CommonObjectReference.md#StorageRole_CommonObjectReference)

<a id="_content_type_11"></a>

## Content Type

- application/json

<a id="_responses_11"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [StorageRole](../CommonObjectReference/CommonObjectReference.md#StorageRole_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_11"></a>

## Samples

<a id="GetRoles_RoleService"></a>

# GetRoles

`GET /v1/roles`

<a id="_description_12"></a>

## Description

<a id="_parameters_12"></a>

## Parameters

<a id="_return_type_12"></a>

## Return Type

[V1GetRolesResponse](../CommonObjectReference/CommonObjectReference.md#V1GetRolesResponse_CommonObjectReference)

<a id="_content_type_12"></a>

## Content Type

- application/json

<a id="_responses_12"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V1GetRolesResponse](../CommonObjectReference/CommonObjectReference.md#V1GetRolesResponse_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_12"></a>

## Samples

<a id="GetSimpleAccessScope_RoleService"></a>

# GetSimpleAccessScope

`GET /v1/simpleaccessscopes/{id}`

<a id="_description_13"></a>

## Description

<a id="_parameters_13"></a>

## Parameters

<a id="_path_parameters_8"></a>

### Path Parameters

| Name | Description | Required | Default | Pattern |
|------|-------------|----------|---------|---------|
| id   |             | X        | null    |         |

<a id="_return_type_13"></a>

## Return Type

[StorageSimpleAccessScope](../CommonObjectReference/CommonObjectReference.md#StorageSimpleAccessScope_CommonObjectReference)

<a id="_content_type_13"></a>

## Content Type

- application/json

<a id="_responses_13"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [StorageSimpleAccessScope](../CommonObjectReference/CommonObjectReference.md#StorageSimpleAccessScope_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_13"></a>

## Samples

<a id="ListPermissionSets_RoleService"></a>

# ListPermissionSets

`GET /v1/permissionsets`

<a id="_description_14"></a>

## Description

<a id="_parameters_14"></a>

## Parameters

<a id="_return_type_14"></a>

## Return Type

[V1ListPermissionSetsResponse](../CommonObjectReference/CommonObjectReference.md#V1ListPermissionSetsResponse_CommonObjectReference)

<a id="_content_type_14"></a>

## Content Type

- application/json

<a id="_responses_14"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V1ListPermissionSetsResponse](../CommonObjectReference/CommonObjectReference.md#V1ListPermissionSetsResponse_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_14"></a>

## Samples

<a id="ListSimpleAccessScopes_RoleService"></a>

# ListSimpleAccessScopes

`GET /v1/simpleaccessscopes`

<a id="_description_15"></a>

## Description

<a id="_parameters_15"></a>

## Parameters

<a id="_return_type_15"></a>

## Return Type

[V1ListSimpleAccessScopesResponse](../CommonObjectReference/CommonObjectReference.md#V1ListSimpleAccessScopesResponse_CommonObjectReference)

<a id="_content_type_15"></a>

## Content Type

- application/json

<a id="_responses_15"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V1ListSimpleAccessScopesResponse](../CommonObjectReference/CommonObjectReference.md#V1ListSimpleAccessScopesResponse_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_15"></a>

## Samples

<a id="PostPermissionSet_RoleService"></a>

# PostPermissionSet

`POST /v1/permissionsets`

PostPermissionSet

<a id="_description_16"></a>

## Description

PermissionSet.id is disallowed in request and set in response.

<a id="_parameters_16"></a>

## Parameters

<a id="_body_parameter_3"></a>

### Body Parameter

| Name | Description | Required | Default | Pattern |
|----|----|----|----|----|
| body | This encodes a set of permissions for StackRox resources. [StoragePermissionSet](../CommonObjectReference/CommonObjectReference.md#StoragePermissionSet_CommonObjectReference) | X |  |  |

<a id="_return_type_16"></a>

## Return Type

[StoragePermissionSet](../CommonObjectReference/CommonObjectReference.md#StoragePermissionSet_CommonObjectReference)

<a id="_content_type_16"></a>

## Content Type

- application/json

<a id="_responses_16"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [StoragePermissionSet](../CommonObjectReference/CommonObjectReference.md#StoragePermissionSet_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_16"></a>

## Samples

<a id="PostSimpleAccessScope_RoleService"></a>

# PostSimpleAccessScope

`POST /v1/simpleaccessscopes`

PostSimpleAccessScope

<a id="_description_17"></a>

## Description

SimpleAccessScope.id is disallowed in request and set in response.

<a id="_parameters_17"></a>

## Parameters

<a id="_body_parameter_4"></a>

### Body Parameter

| Name | Description | Required | Default | Pattern |
|----|----|----|----|----|
| body | Simple access scope is a (simple) selection criteria for scoped resources. It does **not** allow multi-component AND-rules nor set operations on names. [StorageSimpleAccessScope](../CommonObjectReference/CommonObjectReference.md#StorageSimpleAccessScope_CommonObjectReference) | X |  |  |

<a id="_return_type_17"></a>

## Return Type

[StorageSimpleAccessScope](../CommonObjectReference/CommonObjectReference.md#StorageSimpleAccessScope_CommonObjectReference)

<a id="_content_type_17"></a>

## Content Type

- application/json

<a id="_responses_17"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [StorageSimpleAccessScope](../CommonObjectReference/CommonObjectReference.md#StorageSimpleAccessScope_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_17"></a>

## Samples

<a id="PutPermissionSet_RoleService"></a>

# PutPermissionSet

`PUT /v1/permissionsets/{id}`

<a id="_description_18"></a>

## Description

<a id="_parameters_18"></a>

## Parameters

<a id="_path_parameters_9"></a>

### Path Parameters

| Name | Description                            | Required | Default | Pattern |
|------|----------------------------------------|----------|---------|---------|
| id   | id is generated and cannot be changed. | X        | null    |         |

<a id="_body_parameter_5"></a>

### Body Parameter

| Name | Description | Required | Default | Pattern |
|----|----|----|----|----|
| body | [RoleServicePutPermissionSetBody](../CommonObjectReference/CommonObjectReference.md#RoleServicePutPermissionSetBody_CommonObjectReference) | X |  |  |

<a id="_return_type_18"></a>

## Return Type

`Object`

<a id="_content_type_18"></a>

## Content Type

- application/json

<a id="_responses_18"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | `Object` |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_18"></a>

## Samples

<a id="PutSimpleAccessScope_RoleService"></a>

# PutSimpleAccessScope

`PUT /v1/simpleaccessscopes/{id}`

<a id="_description_19"></a>

## Description

<a id="_parameters_19"></a>

## Parameters

<a id="_path_parameters_10"></a>

### Path Parameters

| Name | Description                              | Required | Default | Pattern |
|------|------------------------------------------|----------|---------|---------|
| id   | `id` is generated and cannot be changed. | X        | null    |         |

<a id="_body_parameter_6"></a>

### Body Parameter

| Name | Description | Required | Default | Pattern |
|----|----|----|----|----|
| body | [RoleServicePutSimpleAccessScopeBody](../CommonObjectReference/CommonObjectReference.md#RoleServicePutSimpleAccessScopeBody_CommonObjectReference) | X |  |  |

<a id="_return_type_19"></a>

## Return Type

`Object`

<a id="_content_type_19"></a>

## Content Type

- application/json

<a id="_responses_19"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | `Object` |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_19"></a>

## Samples

<a id="UpdateRole_RoleService"></a>

# UpdateRole

`PUT /v1/roles/{name}`

<a id="_description_20"></a>

## Description

<a id="_parameters_20"></a>

## Parameters

<a id="_path_parameters_11"></a>

### Path Parameters

| Name | Description | Required | Default | Pattern |
|----|----|----|----|----|
| name | `name` and `description` are provided by the user and can be changed. | X | null |  |

<a id="_body_parameter_7"></a>

### Body Parameter

| Name | Description | Required | Default | Pattern |
|----|----|----|----|----|
| body | [RoleServiceUpdateRoleBody](../CommonObjectReference/CommonObjectReference.md#RoleServiceUpdateRoleBody_CommonObjectReference) | X |  |  |

<a id="_return_type_20"></a>

## Return Type

`Object`

<a id="_content_type_20"></a>

## Content Type

- application/json

<a id="_responses_20"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | `Object` |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_20"></a>

## Samples
