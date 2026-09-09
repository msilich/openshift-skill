<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

<a id="GetVM_VirtualMachineV2Service"></a>

# GetVM

`GET /v2/virtualmachines/{id}`

Single VM detail — registered first so literal paths below take priority.

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

[V2VMDetail](../CommonObjectReference/CommonObjectReference.md#V2VMDetail_CommonObjectReference)

<a id="_content_type"></a>

## Content Type

- application/json

<a id="_responses"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V2VMDetail](../CommonObjectReference/CommonObjectReference.md#V2VMDetail_CommonObjectReference) |
| 0 | An unexpected error response. | [RpcStatus](../CommonObjectReference/CommonObjectReference.md#RpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples"></a>

## Samples

<a id="GetVMCVEComponents_VirtualMachineV2Service"></a>

# GetVMCVEComponents

`GET /v2/virtualmachines/{vmId}/cves/{cveId}/components`

Components for a specific CVE on a specific VM (expanded row)

<a id="_description_2"></a>

## Description

<a id="_parameters_2"></a>

## Parameters

<a id="_path_parameters_2"></a>

### Path Parameters

| Name  | Description | Required | Default | Pattern |
|-------|-------------|----------|---------|---------|
| vmId  |             | X        | null    |         |
| cveId |             | X        | null    |         |

<a id="_return_type_2"></a>

## Return Type

[V2GetVMCVEComponentsResponse](../CommonObjectReference/CommonObjectReference.md#V2GetVMCVEComponentsResponse_CommonObjectReference)

<a id="_content_type_2"></a>

## Content Type

- application/json

<a id="_responses_2"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V2GetVMCVEComponentsResponse](../CommonObjectReference/CommonObjectReference.md#V2GetVMCVEComponentsResponse_CommonObjectReference) |
| 0 | An unexpected error response. | [RpcStatus](../CommonObjectReference/CommonObjectReference.md#RpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_2"></a>

## Samples

<a id="GetVMCVEDetail_VirtualMachineV2Service"></a>

# GetVMCVEDetail

`GET /v2/virtualmachines/cves/{cveId}`

Single CVE detail (across all VMs)

<a id="_description_3"></a>

## Description

<a id="_parameters_3"></a>

## Parameters

<a id="_path_parameters_3"></a>

### Path Parameters

| Name  | Description | Required | Default | Pattern |
|-------|-------------|----------|---------|---------|
| cveId |             | X        | null    |         |

<a id="_return_type_3"></a>

## Return Type

[V2VMCVEDetail](../CommonObjectReference/CommonObjectReference.md#V2VMCVEDetail_CommonObjectReference)

<a id="_content_type_3"></a>

## Content Type

- application/json

<a id="_responses_3"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V2VMCVEDetail](../CommonObjectReference/CommonObjectReference.md#V2VMCVEDetail_CommonObjectReference) |
| 0 | An unexpected error response. | [RpcStatus](../CommonObjectReference/CommonObjectReference.md#RpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_3"></a>

## Samples

<a id="GetVMDashboardCounts_VirtualMachineV2Service"></a>

# GetVMDashboardCounts

`GET /v2/virtualmachines/summary`

Dashboard tab counts

<a id="_description_4"></a>

## Description

<a id="_parameters_4"></a>

## Parameters

<a id="_query_parameters"></a>

### Query Parameters

| Name | Description | Required | Default | Pattern |
|----|----|----|----|----|
| query.query |  | \- | null |  |
| query.pagination.limit |  | \- | null |  |
| query.pagination.offset |  | \- | null |  |
| query.pagination.sortOption.field |  | \- | null |  |
| query.pagination.sortOption.reversed |  | \- | null |  |
| query.pagination.sortOption.aggregateBy.aggrFunc |  | \- | UNSET |  |
| query.pagination.sortOption.aggregateBy.distinct |  | \- | null |  |

<a id="_return_type_4"></a>

## Return Type

[V2VMDashboardCountsResponse](../CommonObjectReference/CommonObjectReference.md#V2VMDashboardCountsResponse_CommonObjectReference)

<a id="_content_type_4"></a>

## Content Type

- application/json

<a id="_responses_4"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V2VMDashboardCountsResponse](../CommonObjectReference/CommonObjectReference.md#V2VMDashboardCountsResponse_CommonObjectReference) |
| 0 | An unexpected error response. | [RpcStatus](../CommonObjectReference/CommonObjectReference.md#RpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_4"></a>

## Samples

<a id="GetVMVulnSummary_VirtualMachineV2Service"></a>

# GetVMVulnSummary

`GET /v2/virtualmachines/{id}/vuln-summary`

Single VM vulnerability summary cards

<a id="_description_5"></a>

## Description

<a id="_parameters_5"></a>

## Parameters

<a id="_path_parameters_4"></a>

### Path Parameters

| Name | Description | Required | Default | Pattern |
|------|-------------|----------|---------|---------|
| id   |             | X        | null    |         |

<a id="_query_parameters_2"></a>

### Query Parameters

| Name | Description | Required | Default | Pattern |
|----|----|----|----|----|
| query.query |  | \- | null |  |
| query.pagination.limit |  | \- | null |  |
| query.pagination.offset |  | \- | null |  |
| query.pagination.sortOption.field |  | \- | null |  |
| query.pagination.sortOption.reversed |  | \- | null |  |
| query.pagination.sortOption.aggregateBy.aggrFunc |  | \- | UNSET |  |
| query.pagination.sortOption.aggregateBy.distinct |  | \- | null |  |

<a id="_return_type_5"></a>

## Return Type

[V2VMVulnSummary](../CommonObjectReference/CommonObjectReference.md#V2VMVulnSummary_CommonObjectReference)

<a id="_content_type_5"></a>

## Content Type

- application/json

<a id="_responses_5"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V2VMVulnSummary](../CommonObjectReference/CommonObjectReference.md#V2VMVulnSummary_CommonObjectReference) |
| 0 | An unexpected error response. | [RpcStatus](../CommonObjectReference/CommonObjectReference.md#RpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_5"></a>

## Samples

<a id="ListVMCVEAffectedVMs_VirtualMachineV2Service"></a>

# ListVMCVEAffectedVMs

`GET /v2/virtualmachines/cves/{cveId}/vms`

VMs affected by a specific CVE

<a id="_description_6"></a>

## Description

<a id="_parameters_6"></a>

## Parameters

<a id="_path_parameters_5"></a>

### Path Parameters

| Name  | Description | Required | Default | Pattern |
|-------|-------------|----------|---------|---------|
| cveId |             | X        | null    |         |

<a id="_query_parameters_3"></a>

### Query Parameters

| Name | Description | Required | Default | Pattern |
|----|----|----|----|----|
| query.query |  | \- | null |  |
| query.pagination.limit |  | \- | null |  |
| query.pagination.offset |  | \- | null |  |
| query.pagination.sortOption.field |  | \- | null |  |
| query.pagination.sortOption.reversed |  | \- | null |  |
| query.pagination.sortOption.aggregateBy.aggrFunc |  | \- | UNSET |  |
| query.pagination.sortOption.aggregateBy.distinct |  | \- | null |  |

<a id="_return_type_6"></a>

## Return Type

[V2ListVMCVEAffectedVMsResponse](../CommonObjectReference/CommonObjectReference.md#V2ListVMCVEAffectedVMsResponse_CommonObjectReference)

<a id="_content_type_6"></a>

## Content Type

- application/json

<a id="_responses_6"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V2ListVMCVEAffectedVMsResponse](../CommonObjectReference/CommonObjectReference.md#V2ListVMCVEAffectedVMsResponse_CommonObjectReference) |
| 0 | An unexpected error response. | [RpcStatus](../CommonObjectReference/CommonObjectReference.md#RpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_6"></a>

## Samples

<a id="ListVMCVEs_VirtualMachineV2Service"></a>

# ListVMCVEs

`GET /v2/virtualmachines/cves`

CVE List View

<a id="_description_7"></a>

## Description

<a id="_parameters_7"></a>

## Parameters

<a id="_query_parameters_4"></a>

### Query Parameters

| Name | Description | Required | Default | Pattern |
|----|----|----|----|----|
| query.query |  | \- | null |  |
| query.pagination.limit |  | \- | null |  |
| query.pagination.offset |  | \- | null |  |
| query.pagination.sortOption.field |  | \- | null |  |
| query.pagination.sortOption.reversed |  | \- | null |  |
| query.pagination.sortOption.aggregateBy.aggrFunc |  | \- | UNSET |  |
| query.pagination.sortOption.aggregateBy.distinct |  | \- | null |  |

<a id="_return_type_7"></a>

## Return Type

[V2ListVMCVEsResponse](../CommonObjectReference/CommonObjectReference.md#V2ListVMCVEsResponse_CommonObjectReference)

<a id="_content_type_7"></a>

## Content Type

- application/json

<a id="_responses_7"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V2ListVMCVEsResponse](../CommonObjectReference/CommonObjectReference.md#V2ListVMCVEsResponse_CommonObjectReference) |
| 0 | An unexpected error response. | [RpcStatus](../CommonObjectReference/CommonObjectReference.md#RpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_7"></a>

## Samples

<a id="ListVMCVEsByVM_VirtualMachineV2Service"></a>

# ListVMCVEsByVM

`GET /v2/virtualmachines/{vmId}/cves`

Single VM CVE list

<a id="_description_8"></a>

## Description

<a id="_parameters_8"></a>

## Parameters

<a id="_path_parameters_6"></a>

### Path Parameters

| Name | Description | Required | Default | Pattern |
|------|-------------|----------|---------|---------|
| vmId |             | X        | null    |         |

<a id="_query_parameters_5"></a>

### Query Parameters

| Name | Description | Required | Default | Pattern |
|----|----|----|----|----|
| query.query |  | \- | null |  |
| query.pagination.limit |  | \- | null |  |
| query.pagination.offset |  | \- | null |  |
| query.pagination.sortOption.field |  | \- | null |  |
| query.pagination.sortOption.reversed |  | \- | null |  |
| query.pagination.sortOption.aggregateBy.aggrFunc |  | \- | UNSET |  |
| query.pagination.sortOption.aggregateBy.distinct |  | \- | null |  |

<a id="_return_type_8"></a>

## Return Type

[V2ListVMCVEsByVMResponse](../CommonObjectReference/CommonObjectReference.md#V2ListVMCVEsByVMResponse_CommonObjectReference)

<a id="_content_type_8"></a>

## Content Type

- application/json

<a id="_responses_8"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V2ListVMCVEsByVMResponse](../CommonObjectReference/CommonObjectReference.md#V2ListVMCVEsByVMResponse_CommonObjectReference) |
| 0 | An unexpected error response. | [RpcStatus](../CommonObjectReference/CommonObjectReference.md#RpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_8"></a>

## Samples

<a id="ListVMComponents_VirtualMachineV2Service"></a>

# ListVMComponents

`GET /v2/virtualmachines/{vmId}/components`

Single VM component list

<a id="_description_9"></a>

## Description

<a id="_parameters_9"></a>

## Parameters

<a id="_path_parameters_7"></a>

### Path Parameters

| Name | Description | Required | Default | Pattern |
|------|-------------|----------|---------|---------|
| vmId |             | X        | null    |         |

<a id="_query_parameters_6"></a>

### Query Parameters

| Name | Description | Required | Default | Pattern |
|----|----|----|----|----|
| query.query |  | \- | null |  |
| query.pagination.limit |  | \- | null |  |
| query.pagination.offset |  | \- | null |  |
| query.pagination.sortOption.field |  | \- | null |  |
| query.pagination.sortOption.reversed |  | \- | null |  |
| query.pagination.sortOption.aggregateBy.aggrFunc |  | \- | UNSET |  |
| query.pagination.sortOption.aggregateBy.distinct |  | \- | null |  |

<a id="_return_type_9"></a>

## Return Type

[V2ListVMComponentsResponse](../CommonObjectReference/CommonObjectReference.md#V2ListVMComponentsResponse_CommonObjectReference)

<a id="_content_type_9"></a>

## Content Type

- application/json

<a id="_responses_9"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V2ListVMComponentsResponse](../CommonObjectReference/CommonObjectReference.md#V2ListVMComponentsResponse_CommonObjectReference) |
| 0 | An unexpected error response. | [RpcStatus](../CommonObjectReference/CommonObjectReference.md#RpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_9"></a>

## Samples

<a id="ListVMs_VirtualMachineV2Service"></a>

# ListVMs

`GET /v2/virtualmachines/vms`

VM List View

<a id="_description_10"></a>

## Description

<a id="_parameters_10"></a>

## Parameters

<a id="_query_parameters_7"></a>

### Query Parameters

| Name | Description | Required | Default | Pattern |
|----|----|----|----|----|
| query.query |  | \- | null |  |
| query.pagination.limit |  | \- | null |  |
| query.pagination.offset |  | \- | null |  |
| query.pagination.sortOption.field |  | \- | null |  |
| query.pagination.sortOption.reversed |  | \- | null |  |
| query.pagination.sortOption.aggregateBy.aggrFunc |  | \- | UNSET |  |
| query.pagination.sortOption.aggregateBy.distinct |  | \- | null |  |

<a id="_return_type_10"></a>

## Return Type

[V2ListVMsResponse](../CommonObjectReference/CommonObjectReference.md#V2ListVMsResponse_CommonObjectReference)

<a id="_content_type_10"></a>

## Content Type

- application/json

<a id="_responses_10"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V2ListVMsResponse](../CommonObjectReference/CommonObjectReference.md#V2ListVMsResponse_CommonObjectReference) |
| 0 | An unexpected error response. | [RpcStatus](../CommonObjectReference/CommonObjectReference.md#RpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_10"></a>

## Samples
