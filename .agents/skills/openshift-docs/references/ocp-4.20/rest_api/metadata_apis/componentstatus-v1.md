<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Description
ComponentStatus (and ComponentStatusList) holds the cluster validation info. Deprecated: This API is deprecated in v1.19+

Type
`object`

# Specification

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `conditions` | `array` | List of component conditions observed |
| `conditions[]` | `object` | Information about the condition of a component. |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ObjectMeta`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) | Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |

## .conditions

Description
List of component conditions observed

Type
`array`

## .conditions\[\]

Description
Information about the condition of a component.

Type
`object`

Required
- `type`

- `status`

| Property | Type | Description |
|----|----|----|
| `error` | `string` | Condition error code for a component. For example, a health check error code. |
| `message` | `string` | Message about the condition for a component. For example, information about a health check. |
| `status` | `string` | Status of the condition for a component. Valid values for "Healthy": "True", "False", or "Unknown". |
| `type` | `string` | Type of condition for a component. Valid value: "Healthy" |

# API endpoints

The following API endpoints are available:

- `/api/v1/componentstatuses`

  - `GET`: list objects of kind ComponentStatus

- `/api/v1/componentstatuses/{name}`

  - `GET`: read the specified ComponentStatus

## /api/v1/componentstatuses

HTTP method
`GET`

Description
list objects of kind ComponentStatus

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ComponentStatusList`](../objects/index.md#io-k8s-api-core-v1-ComponentStatusList) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /api/v1/componentstatuses/{name}

| Parameter | Type     | Description                 |
|-----------|----------|-----------------------------|
| `name`    | `string` | name of the ComponentStatus |

Global path parameters

HTTP method
`GET`

Description
read the specified ComponentStatus

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ComponentStatus`](componentstatus-v1.md#componentstatus-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses
