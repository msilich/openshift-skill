<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Description
NodeMetrics sets resource usage metrics of a node.

Type
`object`

Required
- `timestamp`

- `window`

- `usage`

# Specification

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ObjectMeta`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) | Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |
| `timestamp` | [`Time`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-Time) | The following fields define time interval from which metrics were collected from the interval \[Timestamp-Window, Timestamp\]. |
| `usage` | [`object (Quantity)`](../objects/index.md#io-k8s-apimachinery-pkg-api-resource-Quantity) | The memory usage is the memory working set. |
| `window` | [`Duration`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-Duration) |  |

# API endpoints

The following API endpoints are available:

- `/apis/metrics.k8s.io/v1beta1/nodes`

  - `GET`: list objects of kind NodeMetrics

- `/apis/metrics.k8s.io/v1beta1/nodes/{name}`

  - `GET`: read the specified NodeMetrics

## /apis/metrics.k8s.io/v1beta1/nodes

HTTP method
`GET`

Description
list objects of kind NodeMetrics

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`NodeMetricsList`](../objects/index.md#io-k8s-metrics-pkg-apis-metrics-v1beta1-NodeMetricsList) schema |

HTTP responses

## /apis/metrics.k8s.io/v1beta1/nodes/{name}

| Parameter | Type     | Description             |
|-----------|----------|-------------------------|
| `name`    | `string` | name of the NodeMetrics |

Global path parameters

HTTP method
`GET`

Description
read the specified NodeMetrics

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`NodeMetrics`](nodemetrics-metrics-k8s-io-v1beta1.md#nodemetrics-metrics-k8s-io-v1beta1) schema |

HTTP responses
