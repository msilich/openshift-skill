<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Description
ClusterRoleBinding references a ClusterRole, but not contain it. It can reference any ClusterRole in the same namespace or in the global namespace. It adds who information via (Users and Groups) OR Subjects and namespace information by which namespace it exists in. ClusterRoleBindings in a given namespace only have effect in that namespace (excepting the master namespace which has power in all namespaces).

Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).

Type
`object`

Required
- `subjects`

- `roleRef`

# Specification

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `groupNames` | `array (string)` | GroupNames holds all the groups directly bound to the role. This field should only be specified when supporting legacy clients and servers. See Subjects for further details. |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ObjectMeta_v2`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta_v2) | metadata is the standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |
| `roleRef` | [`ObjectReference`](../objects/index.md#io-k8s-api-core-v1-ObjectReference) | RoleRef can only reference the current namespace and the global namespace. If the ClusterRoleRef cannot be resolved, the Authorizer must return an error. Since Policy is a singleton, this is sufficient knowledge to locate a role. |
| `subjects` | [`array (ObjectReference)`](../objects/index.md#io-k8s-api-core-v1-ObjectReference) | Subjects hold object references to authorize with this rule. This field is ignored if UserNames or GroupNames are specified to support legacy clients and servers. Thus newer clients that do not need to support backwards compatibility should send only fully qualified Subjects and should omit the UserNames and GroupNames fields. Clients that need to support backwards compatibility can use this field to build the UserNames and GroupNames. |
| `userNames` | `array (string)` | UserNames holds all the usernames directly bound to the role. This field should only be specified when supporting legacy clients and servers. See Subjects for further details. |

# API endpoints

The following API endpoints are available:

- `/apis/authorization.openshift.io/v1/clusterrolebindings`

  - `GET`: list objects of kind ClusterRoleBinding

  - `POST`: create a ClusterRoleBinding

- `/apis/authorization.openshift.io/v1/clusterrolebindings/{name}`

  - `DELETE`: delete a ClusterRoleBinding

  - `GET`: read the specified ClusterRoleBinding

  - `PATCH`: partially update the specified ClusterRoleBinding

  - `PUT`: replace the specified ClusterRoleBinding

## /apis/authorization.openshift.io/v1/clusterrolebindings

HTTP method
`GET`

Description
list objects of kind ClusterRoleBinding

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ClusterRoleBindingList`](../objects/index.md#com-github-openshift-api-authorization-v1-ClusterRoleBindingList) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`POST`

Description
create a ClusterRoleBinding

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`ClusterRoleBinding`](clusterrolebinding-authorization-openshift-io-v1.md#clusterrolebinding-authorization-openshift-io-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ClusterRoleBinding`](clusterrolebinding-authorization-openshift-io-v1.md#clusterrolebinding-authorization-openshift-io-v1) schema |
| 201 - Created | [`ClusterRoleBinding`](clusterrolebinding-authorization-openshift-io-v1.md#clusterrolebinding-authorization-openshift-io-v1) schema |
| 202 - Accepted | [`ClusterRoleBinding`](clusterrolebinding-authorization-openshift-io-v1.md#clusterrolebinding-authorization-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/authorization.openshift.io/v1/clusterrolebindings/{name}

| Parameter | Type     | Description                    |
|-----------|----------|--------------------------------|
| `name`    | `string` | name of the ClusterRoleBinding |

Global path parameters

HTTP method
`DELETE`

Description
delete a ClusterRoleBinding

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |

Query parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Status_v3`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-Status_v3) schema |
| 202 - Accepted | [`Status_v3`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-Status_v3) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`GET`

Description
read the specified ClusterRoleBinding

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ClusterRoleBinding`](clusterrolebinding-authorization-openshift-io-v1.md#clusterrolebinding-authorization-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PATCH`

Description
partially update the specified ClusterRoleBinding

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ClusterRoleBinding`](clusterrolebinding-authorization-openshift-io-v1.md#clusterrolebinding-authorization-openshift-io-v1) schema |
| 201 - Created | [`ClusterRoleBinding`](clusterrolebinding-authorization-openshift-io-v1.md#clusterrolebinding-authorization-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PUT`

Description
replace the specified ClusterRoleBinding

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`ClusterRoleBinding`](clusterrolebinding-authorization-openshift-io-v1.md#clusterrolebinding-authorization-openshift-io-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ClusterRoleBinding`](clusterrolebinding-authorization-openshift-io-v1.md#clusterrolebinding-authorization-openshift-io-v1) schema |
| 201 - Created | [`ClusterRoleBinding`](clusterrolebinding-authorization-openshift-io-v1.md#clusterrolebinding-authorization-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses
