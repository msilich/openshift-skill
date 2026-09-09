<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

<a id="GetCurrentSecuredUnitsUsage_AdministrationUsageService"></a>

# GetCurrentSecuredUnitsUsage

`GET /v1/administration/usage/secured-units/current`

GetCurrentSecuredUnitsUsage returns the current secured units usage metrics values.

<a id="_description"></a>

## Description

The secured units metrics are collected from all connected clusters every 5 minutes, so the returned result includes data for the connected clusters accurate to about these 5 minutes, and potentially some outdated data for the disconnected clusters.

<a id="_parameters"></a>

## Parameters

<a id="_return_type"></a>

## Return Type

[V1SecuredUnitsUsageResponse](../CommonObjectReference/CommonObjectReference.md#V1SecuredUnitsUsageResponse_CommonObjectReference)

<a id="_content_type"></a>

## Content Type

- application/json

<a id="_responses"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V1SecuredUnitsUsageResponse](../CommonObjectReference/CommonObjectReference.md#V1SecuredUnitsUsageResponse_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples"></a>

## Samples

<a id="GetMaxSecuredUnitsUsage_AdministrationUsageService"></a>

# GetMaxSecuredUnitsUsage

`GET /v1/administration/usage/secured-units/max`

GetMaxSecuredUnitsUsage returns the maximum, i.e. peak, secured units usage observed during a given time range, together with the time when this maximum was aggregated and stored.

<a id="_description_2"></a>

## Description

The usage metrics are continuously collected from all the connected clusters. The maximum values are kept for some period of time in memory, and then, periodically, are stored to the database. The last data from disconnected clusters are taken into account.

<a id="_parameters_2"></a>

## Parameters

<a id="_query_parameters"></a>

### Query Parameters

| Name | Description | Required | Default | Pattern |
|------|-------------|----------|---------|---------|
| from |             | \-       | null    |         |
| to   |             | \-       | null    |         |

<a id="_return_type_2"></a>

## Return Type

[V1MaxSecuredUnitsUsageResponse](../CommonObjectReference/CommonObjectReference.md#V1MaxSecuredUnitsUsageResponse_CommonObjectReference)

<a id="_content_type_2"></a>

## Content Type

- application/json

<a id="_responses_2"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V1MaxSecuredUnitsUsageResponse](../CommonObjectReference/CommonObjectReference.md#V1MaxSecuredUnitsUsageResponse_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_2"></a>

## Samples
