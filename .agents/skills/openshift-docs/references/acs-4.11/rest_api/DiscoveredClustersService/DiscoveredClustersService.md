<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

<a id="CountDiscoveredClusters_DiscoveredClustersService"></a>

# CountDiscoveredClusters

`GET /v1/count/discovered-clusters`

CountDiscoveredClusters returns the number of discovered clusters after filtering by requested fields.

<a id="_description"></a>

## Description

<a id="_parameters"></a>

## Parameters

<a id="_query_parameters"></a>

### Query Parameters

| Name | Description | Required | Default | Pattern |
|----|----|----|----|----|
| filter.names | Matches discovered clusters of specific names. `String` | \- | null |  |
| filter.types | Matches discovered clusters of specific types. `String` | \- | null |  |
| filter.statuses | Matches discovered clusters of specific statuses. - STATUS_UNSPECIFIED: The status of the cluster is unknown. May occur if a secured cluster is missing the metadata for a possible match. - STATUS_SECURED: The discovered cluster was matched with a secured cluster. - STATUS_UNSECURED: The discovered cluster was not matched with a secured cluster. `String` | \- | null |  |
| filter.sourceIds | Matches discovered clusters of specific cloud source IDs. `String` | \- | null |  |

<a id="_return_type"></a>

## Return Type

[V1CountDiscoveredClustersResponse](../CommonObjectReference/CommonObjectReference.md#V1CountDiscoveredClustersResponse_CommonObjectReference)

<a id="_content_type"></a>

## Content Type

- application/json

<a id="_responses"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V1CountDiscoveredClustersResponse](../CommonObjectReference/CommonObjectReference.md#V1CountDiscoveredClustersResponse_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples"></a>

## Samples

<a id="GetDiscoveredCluster_DiscoveredClustersService"></a>

# GetDiscoveredCluster

`GET /v1/discovered-clusters/{id}`

GetDiscoveredCluster retrieves a discovered cluster by ID.

<a id="_description_2"></a>

## Description

<a id="_parameters_2"></a>

## Parameters

<a id="_path_parameters"></a>

### Path Parameters

| Name | Description | Required | Default | Pattern |
|------|-------------|----------|---------|---------|
| id   |             | X        | null    |         |

<a id="_return_type_2"></a>

## Return Type

[V1GetDiscoveredClusterResponse](../CommonObjectReference/CommonObjectReference.md#V1GetDiscoveredClusterResponse_CommonObjectReference)

<a id="_content_type_2"></a>

## Content Type

- application/json

<a id="_responses_2"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V1GetDiscoveredClusterResponse](../CommonObjectReference/CommonObjectReference.md#V1GetDiscoveredClusterResponse_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_2"></a>

## Samples

<a id="ListDiscoveredClusters_DiscoveredClustersService"></a>

# ListDiscoveredClusters

`GET /v1/discovered-clusters`

ListDiscoveredClusters returns the list of discovered clusters after filtered by requested fields.

<a id="_description_3"></a>

## Description

<a id="_parameters_3"></a>

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
| filter.names | Matches discovered clusters of specific names. `String` | \- | null |  |
| filter.types | Matches discovered clusters of specific types. `String` | \- | null |  |
| filter.statuses | Matches discovered clusters of specific statuses. - STATUS_UNSPECIFIED: The status of the cluster is unknown. May occur if a secured cluster is missing the metadata for a possible match. - STATUS_SECURED: The discovered cluster was matched with a secured cluster. - STATUS_UNSECURED: The discovered cluster was not matched with a secured cluster. `String` | \- | null |  |
| filter.sourceIds | Matches discovered clusters of specific cloud source IDs. `String` | \- | null |  |

<a id="_return_type_3"></a>

## Return Type

[V1ListDiscoveredClustersResponse](../CommonObjectReference/CommonObjectReference.md#V1ListDiscoveredClustersResponse_CommonObjectReference)

<a id="_content_type_3"></a>

## Content Type

- application/json

<a id="_responses_3"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V1ListDiscoveredClustersResponse](../CommonObjectReference/CommonObjectReference.md#V1ListDiscoveredClustersResponse_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_3"></a>

## Samples
