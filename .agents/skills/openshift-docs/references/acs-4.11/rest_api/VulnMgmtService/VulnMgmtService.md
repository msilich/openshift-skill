<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

<a id="VulnMgmtExportWorkloads_VulnMgmtService"></a>

# VulnMgmtExportWorkloads

`GET /v1/export/vuln-mgmt/workloads`

Streams vulnerability data upon request. Each entry consists of a deployment and the associated container images.

<a id="_description"></a>

## Description

The response is structured as: {"result": {"deployment": {…​}, "images": \[…​\]}} …​ {"result": {"deployment": {…​}, "images": \[…​\]}}

<a id="_parameters"></a>

## Parameters

<a id="_query_parameters"></a>

### Query Parameters

| Name | Description | Required | Default | Pattern |
|----|----|----|----|----|
| timeout | Request timeout in seconds. | \- | null |  |
| query | Query to constrain the deployments for which vulnerability data is returned. The queries contain pairs of `Search Option:Value` separated by `+` signs. For HTTP requests the query should be quoted. For example \> curl "\$ROX_ENDPOINT/v1/export/vuln-mgmt/workloads?query=Deployment%3Ascanner%2BNamespace%3Astackrox" queries vulnerability data for all scanner deployments in the stackrox namespace. See <https://docs.openshift.com/acs/operating/search-filter.html> for more information. | \- | null |  |

<a id="_return_type"></a>

## Return Type

Stream result of v1VulnMgmtExportWorkloadsResponse.

<a id="_content_type"></a>

## Content Type

- application/json

<a id="_responses"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response.(streaming responses) | Stream result of v1VulnMgmtExportWorkloadsResponse. |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples"></a>

## Samples
