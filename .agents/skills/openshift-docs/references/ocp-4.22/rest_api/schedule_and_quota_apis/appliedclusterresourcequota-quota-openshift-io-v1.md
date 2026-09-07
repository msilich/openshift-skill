<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Description
AppliedClusterResourceQuota mirrors ClusterResourceQuota at a project scope, for projection into a project. It allows a project-admin to know which ClusterResourceQuotas are applied to his project and their associated usage.

Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).

Type
`object`

Required
- `metadata`

- `spec`

# Specification

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ObjectMeta`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) | metadata is the standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |
| `spec` | `object` | ClusterResourceQuotaSpec defines the desired quota restrictions |
| `status` | `object` | ClusterResourceQuotaStatus defines the actual enforced quota and its current usage |

## .spec

Description
ClusterResourceQuotaSpec defines the desired quota restrictions

Type
`object`

Required
- `selector`

- `quota`

| Property | Type | Description |
|----|----|----|
| `quota` | [`ResourceQuotaSpec`](../objects/index.md#io-k8s-api-core-v1-ResourceQuotaSpec) | quota defines the desired quota |
| `selector` | `object` | ClusterResourceQuotaSelector is used to select projects. At least one of LabelSelector or AnnotationSelector must present. If only one is present, it is the only selection criteria. If both are specified, the project must match both restrictions. |

## .spec.selector

Description
ClusterResourceQuotaSelector is used to select projects. At least one of LabelSelector or AnnotationSelector must present. If only one is present, it is the only selection criteria. If both are specified, the project must match both restrictions.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `annotations` | `object (string)` | AnnotationSelector is used to select projects by annotation. |
| `labels` | [`LabelSelector`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-LabelSelector) | LabelSelector is used to select projects by label. |

## .status

Description
ClusterResourceQuotaStatus defines the actual enforced quota and its current usage

Type
`object`

Required
- `total`

| Property | Type | Description |
|----|----|----|
| `namespaces` | `array` | namespaces slices the usage by project. This division allows for quick resolution of deletion reconciliation inside of a single project without requiring a recalculation across all projects. This can be used to pull the deltas for a given project. |
| `namespaces[]` | `object` | ResourceQuotaStatusByNamespace gives status for a particular project |
| `total` | [`ResourceQuotaStatus`](../objects/index.md#io-k8s-api-core-v1-ResourceQuotaStatus) | total defines the actual enforced quota and its current usage across all projects |

## .status.namespaces

Description
namespaces slices the usage by project. This division allows for quick resolution of deletion reconciliation inside of a single project without requiring a recalculation across all projects. This can be used to pull the deltas for a given project.

Type
`array`

## .status.namespaces\[\]

Description
ResourceQuotaStatusByNamespace gives status for a particular project

Type
`object`

Required
- `namespace`

- `status`

| Property | Type | Description |
|----|----|----|
| `namespace` | `string` | namespace the project this status applies to |
| `status` | [`ResourceQuotaStatus`](../objects/index.md#io-k8s-api-core-v1-ResourceQuotaStatus) | status indicates how many resources have been consumed by this project |

# API endpoints

The following API endpoints are available:

- `/apis/quota.openshift.io/v1/appliedclusterresourcequotas`

  - `GET`: list objects of kind AppliedClusterResourceQuota

- `/apis/quota.openshift.io/v1/namespaces/{namespace}/appliedclusterresourcequotas`

  - `GET`: list objects of kind AppliedClusterResourceQuota

- `/apis/quota.openshift.io/v1/namespaces/{namespace}/appliedclusterresourcequotas/{name}`

  - `GET`: read the specified AppliedClusterResourceQuota

## /apis/quota.openshift.io/v1/appliedclusterresourcequotas

HTTP method
`GET`

Description
list objects of kind AppliedClusterResourceQuota

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`AppliedClusterResourceQuotaList`](../objects/index.md#com-github-openshift-api-quota-v1-AppliedClusterResourceQuotaList) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/quota.openshift.io/v1/namespaces/{namespace}/appliedclusterresourcequotas

HTTP method
`GET`

Description
list objects of kind AppliedClusterResourceQuota

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`AppliedClusterResourceQuotaList`](../objects/index.md#com-github-openshift-api-quota-v1-AppliedClusterResourceQuotaList) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/quota.openshift.io/v1/namespaces/{namespace}/appliedclusterresourcequotas/{name}

| Parameter | Type     | Description                             |
|-----------|----------|-----------------------------------------|
| `name`    | `string` | name of the AppliedClusterResourceQuota |

Global path parameters

HTTP method
`GET`

Description
read the specified AppliedClusterResourceQuota

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`AppliedClusterResourceQuota`](appliedclusterresourcequota-quota-openshift-io-v1.md#appliedclusterresourcequota-quota-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses
