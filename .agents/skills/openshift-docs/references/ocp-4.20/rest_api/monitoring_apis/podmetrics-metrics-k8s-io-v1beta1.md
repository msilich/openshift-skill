<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Description
PodMetrics sets resource usage metrics of a pod.

Type
`object`

Required
- `timestamp`

- `window`

- `containers`

# Specification

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `containers` | `array` | Metrics for all containers are collected within the same time window. |
| `containers[]` | `object` | ContainerMetrics sets resource usage metrics of a container. |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ObjectMeta`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) | Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |
| `timestamp` | [`Time`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-Time) | The following fields define time interval from which metrics were collected from the interval \[Timestamp-Window, Timestamp\]. |
| `window` | [`Duration`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-Duration) |  |

## .containers

Description
Metrics for all containers are collected within the same time window.

Type
`array`

## .containers\[\]

Description
ContainerMetrics sets resource usage metrics of a container.

Type
`object`

Required
- `name`

- `usage`

| Property | Type | Description |
|----|----|----|
| `name` | `string` | Container name corresponding to the one from pod.spec.containers. |
| `usage` | [`object (Quantity)`](../objects/index.md#io-k8s-apimachinery-pkg-api-resource-Quantity) | The memory usage is the memory working set. |

# API endpoints

The following API endpoints are available:

- `/apis/metrics.k8s.io/v1beta1/pods`

  - `GET`: list objects of kind PodMetrics

- `/apis/metrics.k8s.io/v1beta1/namespaces/{namespace}/pods`

  - `GET`: list objects of kind PodMetrics

- `/apis/metrics.k8s.io/v1beta1/namespaces/{namespace}/pods/{name}`

  - `GET`: read the specified PodMetrics

## /apis/metrics.k8s.io/v1beta1/pods

HTTP method
`GET`

Description
list objects of kind PodMetrics

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`PodMetricsList`](../objects/index.md#io-k8s-metrics-pkg-apis-metrics-v1beta1-PodMetricsList) schema |

HTTP responses

## /apis/metrics.k8s.io/v1beta1/namespaces/{namespace}/pods

HTTP method
`GET`

Description
list objects of kind PodMetrics

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`PodMetricsList`](../objects/index.md#io-k8s-metrics-pkg-apis-metrics-v1beta1-PodMetricsList) schema |

HTTP responses

## /apis/metrics.k8s.io/v1beta1/namespaces/{namespace}/pods/{name}

| Parameter | Type     | Description            |
|-----------|----------|------------------------|
| `name`    | `string` | name of the PodMetrics |

Global path parameters

HTTP method
`GET`

Description
read the specified PodMetrics

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`PodMetrics`](podmetrics-metrics-k8s-io-v1beta1.md#podmetrics-metrics-k8s-io-v1beta1) schema |

HTTP responses
