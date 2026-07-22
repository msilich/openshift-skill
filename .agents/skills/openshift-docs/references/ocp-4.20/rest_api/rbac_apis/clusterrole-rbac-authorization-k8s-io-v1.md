<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Description
ClusterRole is a cluster level, logical grouping of PolicyRules that can be referenced as a unit by a RoleBinding or ClusterRoleBinding.

Type
`object`

# Specification

| Property | Type | Description |
|----|----|----|
| `aggregationRule` | `object` | AggregationRule describes how to locate ClusterRoles to aggregate into the ClusterRole |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ObjectMeta`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) | Standard object’s metadata. |
| `rules` | `array` | Rules holds all the PolicyRules for this ClusterRole |
| `rules[]` | `object` | PolicyRule holds information that describes a policy rule, but does not contain information about who the rule applies to or which namespace the rule applies to. |

## .aggregationRule

Description
AggregationRule describes how to locate ClusterRoles to aggregate into the ClusterRole

Type
`object`

| Property | Type | Description |
|----|----|----|
| `clusterRoleSelectors` | [`array (LabelSelector)`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-LabelSelector) | ClusterRoleSelectors holds a list of selectors which will be used to find ClusterRoles and create the rules. If any of the selectors match, then the ClusterRole’s permissions will be added |

## .rules

Description
Rules holds all the PolicyRules for this ClusterRole

Type
`array`

## .rules\[\]

Description
PolicyRule holds information that describes a policy rule, but does not contain information about who the rule applies to or which namespace the rule applies to.

Type
`object`

Required
- `verbs`

| Property | Type | Description |
|----|----|----|
| `apiGroups` | `array (string)` | APIGroups is the name of the APIGroup that contains the resources. If multiple API groups are specified, any action requested against one of the enumerated resources in any API group will be allowed. "" represents the core API group and "\*" represents all API groups. |
| `nonResourceURLs` | `array (string)` | NonResourceURLs is a set of partial urls that a user should have access to. \*s are allowed, but only as the full, final step in the path Since non-resource URLs are not namespaced, this field is only applicable for ClusterRoles referenced from a ClusterRoleBinding. Rules can either apply to API resources (such as "pods" or "secrets") or non-resource URL paths (such as "/api"), but not both. |
| `resourceNames` | `array (string)` | ResourceNames is an optional white list of names that the rule applies to. An empty set means that everything is allowed. |
| `resources` | `array (string)` | Resources is a list of resources this rule applies to. '\*' represents all resources. |
| `verbs` | `array (string)` | Verbs is a list of Verbs that apply to ALL the ResourceKinds contained in this rule. '\*' represents all verbs. |

# API endpoints

The following API endpoints are available:

- `/apis/rbac.authorization.k8s.io/v1/clusterroles`

  - `DELETE`: delete collection of ClusterRole

  - `GET`: list or watch objects of kind ClusterRole

  - `POST`: create a ClusterRole

- `/apis/rbac.authorization.k8s.io/v1/watch/clusterroles`

  - `GET`: watch individual changes to a list of ClusterRole. deprecated: use the 'watch' parameter with a list operation instead.

- `/apis/rbac.authorization.k8s.io/v1/clusterroles/{name}`

  - `DELETE`: delete a ClusterRole

  - `GET`: read the specified ClusterRole

  - `PATCH`: partially update the specified ClusterRole

  - `PUT`: replace the specified ClusterRole

- `/apis/rbac.authorization.k8s.io/v1/watch/clusterroles/{name}`

  - `GET`: watch changes to an object of kind ClusterRole. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.

## /apis/rbac.authorization.k8s.io/v1/clusterroles

HTTP method
`DELETE`

Description
delete collection of ClusterRole

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
list or watch objects of kind ClusterRole

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ClusterRoleList`](../objects/index.md#io-k8s-api-rbac-v1-ClusterRoleList) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`POST`

Description
create a ClusterRole

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`ClusterRole`](clusterrole-rbac-authorization-k8s-io-v1.md#clusterrole-rbac-authorization-k8s-io-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ClusterRole`](clusterrole-rbac-authorization-k8s-io-v1.md#clusterrole-rbac-authorization-k8s-io-v1) schema |
| 201 - Created | [`ClusterRole`](clusterrole-rbac-authorization-k8s-io-v1.md#clusterrole-rbac-authorization-k8s-io-v1) schema |
| 202 - Accepted | [`ClusterRole`](clusterrole-rbac-authorization-k8s-io-v1.md#clusterrole-rbac-authorization-k8s-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/rbac.authorization.k8s.io/v1/watch/clusterroles

HTTP method
`GET`

Description
watch individual changes to a list of ClusterRole. deprecated: use the 'watch' parameter with a list operation instead.

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`WatchEvent`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/rbac.authorization.k8s.io/v1/clusterroles/{name}

| Parameter | Type     | Description             |
|-----------|----------|-------------------------|
| `name`    | `string` | name of the ClusterRole |

Global path parameters

HTTP method
`DELETE`

Description
delete a ClusterRole

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
read the specified ClusterRole

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ClusterRole`](clusterrole-rbac-authorization-k8s-io-v1.md#clusterrole-rbac-authorization-k8s-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PATCH`

Description
partially update the specified ClusterRole

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ClusterRole`](clusterrole-rbac-authorization-k8s-io-v1.md#clusterrole-rbac-authorization-k8s-io-v1) schema |
| 201 - Created | [`ClusterRole`](clusterrole-rbac-authorization-k8s-io-v1.md#clusterrole-rbac-authorization-k8s-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PUT`

Description
replace the specified ClusterRole

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`ClusterRole`](clusterrole-rbac-authorization-k8s-io-v1.md#clusterrole-rbac-authorization-k8s-io-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ClusterRole`](clusterrole-rbac-authorization-k8s-io-v1.md#clusterrole-rbac-authorization-k8s-io-v1) schema |
| 201 - Created | [`ClusterRole`](clusterrole-rbac-authorization-k8s-io-v1.md#clusterrole-rbac-authorization-k8s-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/rbac.authorization.k8s.io/v1/watch/clusterroles/{name}

| Parameter | Type     | Description             |
|-----------|----------|-------------------------|
| `name`    | `string` | name of the ClusterRole |

Global path parameters

HTTP method
`GET`

Description
watch changes to an object of kind ClusterRole. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`WatchEvent`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema |
| 401 - Unauthorized | Empty |

HTTP responses
