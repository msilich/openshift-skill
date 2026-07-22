<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Description
RuntimeClass defines a class of container runtime supported in the cluster. The RuntimeClass is used to determine which container runtime is used to run all containers in a pod. RuntimeClasses are manually defined by a user or cluster provisioner, and referenced in the PodSpec. The Kubelet is responsible for resolving the RuntimeClassName reference before running the pod. For more details, see <https://kubernetes.io/docs/concepts/containers/runtime-class/>

Type
`object`

Required
- `handler`

# Specification

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `handler` | `string` | handler specifies the underlying runtime and configuration that the CRI implementation will use to handle pods of this class. The possible values are specific to the node & CRI configuration. It is assumed that all handlers are available on every node, and handlers of the same name are equivalent on every node. For example, a handler called "runc" might specify that the runc OCI runtime (using native Linux containers) will be used to run the containers in a pod. The Handler must be lowercase, conform to the DNS Label (RFC 1123) requirements, and is immutable. |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ObjectMeta`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) | More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |
| `overhead` | `object` | Overhead structure represents the resource overhead associated with running a pod. |
| `scheduling` | `object` | Scheduling specifies the scheduling constraints for nodes supporting a RuntimeClass. |

## .overhead

Description
Overhead structure represents the resource overhead associated with running a pod.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `podFixed` | [`object (Quantity)`](../objects/index.md#io-k8s-apimachinery-pkg-api-resource-Quantity) | podFixed represents the fixed resource overhead associated with running a pod. |

## .scheduling

Description
Scheduling specifies the scheduling constraints for nodes supporting a RuntimeClass.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `nodeSelector` | `object (string)` | nodeSelector lists labels that must be present on nodes that support this RuntimeClass. Pods using this RuntimeClass can only be scheduled to a node matched by this selector. The RuntimeClass nodeSelector is merged with a pod’s existing nodeSelector. Any conflicts will cause the pod to be rejected in admission. |
| `tolerations` | [`array (Toleration)`](../objects/index.md#io-k8s-api-core-v1-Toleration) | tolerations are appended (excluding duplicates) to pods running with this RuntimeClass during admission, effectively unioning the set of nodes tolerated by the pod and the RuntimeClass. |

# API endpoints

The following API endpoints are available:

- `/apis/node.k8s.io/v1/runtimeclasses`

  - `DELETE`: delete collection of RuntimeClass

  - `GET`: list or watch objects of kind RuntimeClass

  - `POST`: create a RuntimeClass

- `/apis/node.k8s.io/v1/watch/runtimeclasses`

  - `GET`: watch individual changes to a list of RuntimeClass. deprecated: use the 'watch' parameter with a list operation instead.

- `/apis/node.k8s.io/v1/runtimeclasses/{name}`

  - `DELETE`: delete a RuntimeClass

  - `GET`: read the specified RuntimeClass

  - `PATCH`: partially update the specified RuntimeClass

  - `PUT`: replace the specified RuntimeClass

- `/apis/node.k8s.io/v1/watch/runtimeclasses/{name}`

  - `GET`: watch changes to an object of kind RuntimeClass. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.

## /apis/node.k8s.io/v1/runtimeclasses

HTTP method
`DELETE`

Description
delete collection of RuntimeClass

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |

Query parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Status`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`GET`

Description
list or watch objects of kind RuntimeClass

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`RuntimeClassList`](../objects/index.md#io-k8s-api-node-v1-RuntimeClassList) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`POST`

Description
create a RuntimeClass

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`RuntimeClass`](runtimeclass-node-k8s-io-v1.md#runtimeclass-node-k8s-io-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`RuntimeClass`](runtimeclass-node-k8s-io-v1.md#runtimeclass-node-k8s-io-v1) schema |
| 201 - Created | [`RuntimeClass`](runtimeclass-node-k8s-io-v1.md#runtimeclass-node-k8s-io-v1) schema |
| 202 - Accepted | [`RuntimeClass`](runtimeclass-node-k8s-io-v1.md#runtimeclass-node-k8s-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/node.k8s.io/v1/watch/runtimeclasses

HTTP method
`GET`

Description
watch individual changes to a list of RuntimeClass. deprecated: use the 'watch' parameter with a list operation instead.

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`WatchEvent`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/node.k8s.io/v1/runtimeclasses/{name}

| Parameter | Type     | Description              |
|-----------|----------|--------------------------|
| `name`    | `string` | name of the RuntimeClass |

Global path parameters

HTTP method
`DELETE`

Description
delete a RuntimeClass

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |

Query parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Status`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 202 - Accepted | [`Status`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`GET`

Description
read the specified RuntimeClass

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`RuntimeClass`](runtimeclass-node-k8s-io-v1.md#runtimeclass-node-k8s-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PATCH`

Description
partially update the specified RuntimeClass

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`RuntimeClass`](runtimeclass-node-k8s-io-v1.md#runtimeclass-node-k8s-io-v1) schema |
| 201 - Created | [`RuntimeClass`](runtimeclass-node-k8s-io-v1.md#runtimeclass-node-k8s-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PUT`

Description
replace the specified RuntimeClass

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`RuntimeClass`](runtimeclass-node-k8s-io-v1.md#runtimeclass-node-k8s-io-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`RuntimeClass`](runtimeclass-node-k8s-io-v1.md#runtimeclass-node-k8s-io-v1) schema |
| 201 - Created | [`RuntimeClass`](runtimeclass-node-k8s-io-v1.md#runtimeclass-node-k8s-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/node.k8s.io/v1/watch/runtimeclasses/{name}

| Parameter | Type     | Description              |
|-----------|----------|--------------------------|
| `name`    | `string` | name of the RuntimeClass |

Global path parameters

HTTP method
`GET`

Description
watch changes to an object of kind RuntimeClass. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`WatchEvent`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema |
| 401 - Unauthorized | Empty |

HTTP responses
