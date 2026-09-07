<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Description
RoleBindingRestriction is an object that can be matched against a subject (user, group, or service account) to determine whether rolebindings on that subject are allowed in the namespace to which the RoleBindingRestriction belongs. If any one of those RoleBindingRestriction objects matches a subject, rolebindings on that subject in the namespace are allowed.

Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).

Type
`object`

# Specification

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ObjectMeta`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) | Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |
| `spec` | `object` | spec defines the matcher. |

## .spec

Description
spec defines the matcher.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `grouprestriction` | \`\` | grouprestriction matches against group subjects. |
| `serviceaccountrestriction` | \`\` | serviceaccountrestriction matches against service-account subjects. |
| `userrestriction` | \`\` | userrestriction matches against user subjects. |

# API endpoints

The following API endpoints are available:

- `/apis/authorization.openshift.io/v1/rolebindingrestrictions`

  - `GET`: list objects of kind RoleBindingRestriction

- `/apis/authorization.openshift.io/v1/namespaces/{namespace}/rolebindingrestrictions`

  - `DELETE`: delete collection of RoleBindingRestriction

  - `GET`: list objects of kind RoleBindingRestriction

  - `POST`: create a RoleBindingRestriction

- `/apis/authorization.openshift.io/v1/namespaces/{namespace}/rolebindingrestrictions/{name}`

  - `DELETE`: delete a RoleBindingRestriction

  - `GET`: read the specified RoleBindingRestriction

  - `PATCH`: partially update the specified RoleBindingRestriction

  - `PUT`: replace the specified RoleBindingRestriction

## /apis/authorization.openshift.io/v1/rolebindingrestrictions

HTTP method
`GET`

Description
list objects of kind RoleBindingRestriction

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`RoleBindingRestrictionList`](../objects/index.md#io-openshift-authorization-v1-RoleBindingRestrictionList) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/authorization.openshift.io/v1/namespaces/{namespace}/rolebindingrestrictions

HTTP method
`DELETE`

Description
delete collection of RoleBindingRestriction

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Status`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`GET`

Description
list objects of kind RoleBindingRestriction

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`RoleBindingRestrictionList`](../objects/index.md#io-openshift-authorization-v1-RoleBindingRestrictionList) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`POST`

Description
create a RoleBindingRestriction

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`RoleBindingRestriction`](rolebindingrestriction-authorization-openshift-io-v1.md#rolebindingrestriction-authorization-openshift-io-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`RoleBindingRestriction`](rolebindingrestriction-authorization-openshift-io-v1.md#rolebindingrestriction-authorization-openshift-io-v1) schema |
| 201 - Created | [`RoleBindingRestriction`](rolebindingrestriction-authorization-openshift-io-v1.md#rolebindingrestriction-authorization-openshift-io-v1) schema |
| 202 - Accepted | [`RoleBindingRestriction`](rolebindingrestriction-authorization-openshift-io-v1.md#rolebindingrestriction-authorization-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/authorization.openshift.io/v1/namespaces/{namespace}/rolebindingrestrictions/{name}

| Parameter | Type     | Description                        |
|-----------|----------|------------------------------------|
| `name`    | `string` | name of the RoleBindingRestriction |

Global path parameters

HTTP method
`DELETE`

Description
delete a RoleBindingRestriction

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
read the specified RoleBindingRestriction

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`RoleBindingRestriction`](rolebindingrestriction-authorization-openshift-io-v1.md#rolebindingrestriction-authorization-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PATCH`

Description
partially update the specified RoleBindingRestriction

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`RoleBindingRestriction`](rolebindingrestriction-authorization-openshift-io-v1.md#rolebindingrestriction-authorization-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PUT`

Description
replace the specified RoleBindingRestriction

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`RoleBindingRestriction`](rolebindingrestriction-authorization-openshift-io-v1.md#rolebindingrestriction-authorization-openshift-io-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`RoleBindingRestriction`](rolebindingrestriction-authorization-openshift-io-v1.md#rolebindingrestriction-authorization-openshift-io-v1) schema |
| 201 - Created | [`RoleBindingRestriction`](rolebindingrestriction-authorization-openshift-io-v1.md#rolebindingrestriction-authorization-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses
