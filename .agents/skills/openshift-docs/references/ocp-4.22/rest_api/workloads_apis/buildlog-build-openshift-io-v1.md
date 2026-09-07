<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Description
BuildLog is the (unused) resource associated with the build log redirector

Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).

Type
`object`

# Specification

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

# API endpoints

The following API endpoints are available:

- `/apis/build.openshift.io/v1/namespaces/{namespace}/builds/{name}/log`

  - `GET`: read log of the specified Build

## /apis/build.openshift.io/v1/namespaces/{namespace}/builds/{name}/log

| Parameter | Type     | Description          |
|-----------|----------|----------------------|
| `name`    | `string` | name of the BuildLog |

Global path parameters

HTTP method
`GET`

Description
read log of the specified Build

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`BuildLog`](buildlog-build-openshift-io-v1.md#buildlog-build-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses
