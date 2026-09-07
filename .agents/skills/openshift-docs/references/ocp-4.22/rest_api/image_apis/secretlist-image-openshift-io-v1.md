<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Description
SecretList is a list of Secret.

Type
`object`

Required
- `items`

# Specification

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (Secret)`](../security_apis/secret-v1.md#secret-v1) | Items is a list of secret objects. More info: <https://kubernetes.io/docs/concepts/configuration/secret> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

# API endpoints

The following API endpoints are available:

- `/apis/image.openshift.io/v1/namespaces/{namespace}/imagestreams/{name}/secrets`

  - `GET`: read secrets of the specified ImageStream

## /apis/image.openshift.io/v1/namespaces/{namespace}/imagestreams/{name}/secrets

| Parameter | Type     | Description            |
|-----------|----------|------------------------|
| `name`    | `string` | name of the SecretList |

Global path parameters

HTTP method
`GET`

Description
read secrets of the specified ImageStream

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`SecretList`](secretlist-image-openshift-io-v1.md#secretlist-image-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses
