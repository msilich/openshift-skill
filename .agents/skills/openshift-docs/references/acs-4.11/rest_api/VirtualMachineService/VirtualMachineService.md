<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

<a id="ListVirtualMachines_VirtualMachineService"></a>

# ListVirtualMachines

`GET /v2/virtualmachines`

<a id="_description"></a>

## Description

<a id="_parameters"></a>

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

<a id="_return_type"></a>

## Return Type

[V2ListVirtualMachinesResponse](../CommonObjectReference/CommonObjectReference.md#V2ListVirtualMachinesResponse_CommonObjectReference)

<a id="_content_type"></a>

## Content Type

- application/json

<a id="_responses"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V2ListVirtualMachinesResponse](../CommonObjectReference/CommonObjectReference.md#V2ListVirtualMachinesResponse_CommonObjectReference) |
| 0 | An unexpected error response. | [RpcStatus](../CommonObjectReference/CommonObjectReference.md#RpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples"></a>

## Samples
