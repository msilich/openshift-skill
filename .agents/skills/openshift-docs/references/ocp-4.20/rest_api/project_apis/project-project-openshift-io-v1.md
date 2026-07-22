<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Description
Projects are the unit of isolation and collaboration in OpenShift. A project has one or more members, a quota on the resources that the project may consume, and the security controls on the resources in the project. Within a project, members may have different roles - project administrators can set membership, editors can create and manage the resources, and viewers can see but not access running containers. In a normal cluster project administrators are not able to alter their quotas - that is restricted to cluster administrators.

Listing or watching projects will return only projects the user has the reader role on.

An OpenShift project is an alternative representation of a Kubernetes namespace. Projects are exposed as editable to end users while namespaces are not. Direct creation of a project is typically restricted to administrators, while end users should use the requestproject resource.

Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).

Type
`object`

# Specification

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ObjectMeta_v2`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta_v2) | metadata is the standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |
| `spec` | `object` | ProjectSpec describes the attributes on a Project |
| `status` | `object` | ProjectStatus is information about the current status of a Project |

## .spec

Description
ProjectSpec describes the attributes on a Project

Type
`object`

| Property | Type | Description |
|----|----|----|
| `finalizers` | `array (string)` | Finalizers is an opaque list of values that must be empty to permanently remove object from storage |

## .status

Description
ProjectStatus is information about the current status of a Project

Type
`object`

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Property</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>conditions</code></p></td>
<td style="text-align: left;"><p><a href="../objects/index.xml#io-k8s-api-core-v1-NamespaceCondition_v2"><code>array (NamespaceCondition_v2)</code></a></p></td>
<td style="text-align: left;"><p>Represents the latest available observations of the project current state.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>phase</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Phase is the current lifecycle phase of the project</p>
<p>Possible enum values: - <code>"Active"</code> means the namespace is available for use in the system - <code>"Terminating"</code> means the namespace is undergoing graceful termination</p></td>
</tr>
</tbody>
</table>

# API endpoints

The following API endpoints are available:

- `/apis/project.openshift.io/v1/projects`

  - `GET`: list or watch objects of kind Project

  - `POST`: create a Project

- `/apis/project.openshift.io/v1/watch/projects`

  - `GET`: watch individual changes to a list of Project. deprecated: use the 'watch' parameter with a list operation instead.

- `/apis/project.openshift.io/v1/projects/{name}`

  - `DELETE`: delete a Project

  - `GET`: read the specified Project

  - `PATCH`: partially update the specified Project

  - `PUT`: replace the specified Project

- `/apis/project.openshift.io/v1/watch/projects/{name}`

  - `GET`: watch changes to an object of kind Project. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.

## /apis/project.openshift.io/v1/projects

HTTP method
`GET`

Description
list or watch objects of kind Project

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ProjectList`](../objects/index.md#com-github-openshift-api-project-v1-ProjectList) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`POST`

Description
create a Project

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`Project`](project-project-openshift-io-v1.md#project-project-openshift-io-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Project`](project-project-openshift-io-v1.md#project-project-openshift-io-v1) schema |
| 201 - Created | [`Project`](project-project-openshift-io-v1.md#project-project-openshift-io-v1) schema |
| 202 - Accepted | [`Project`](project-project-openshift-io-v1.md#project-project-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/project.openshift.io/v1/watch/projects

HTTP method
`GET`

Description
watch individual changes to a list of Project. deprecated: use the 'watch' parameter with a list operation instead.

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`WatchEvent`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/project.openshift.io/v1/projects/{name}

| Parameter | Type     | Description         |
|-----------|----------|---------------------|
| `name`    | `string` | name of the Project |

Global path parameters

HTTP method
`DELETE`

Description
delete a Project

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |

Query parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Status_v6`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-Status_v6) schema |
| 202 - Accepted | [`Status_v6`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-Status_v6) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`GET`

Description
read the specified Project

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Project`](project-project-openshift-io-v1.md#project-project-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PATCH`

Description
partially update the specified Project

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Project`](project-project-openshift-io-v1.md#project-project-openshift-io-v1) schema |
| 201 - Created | [`Project`](project-project-openshift-io-v1.md#project-project-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PUT`

Description
replace the specified Project

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`Project`](project-project-openshift-io-v1.md#project-project-openshift-io-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Project`](project-project-openshift-io-v1.md#project-project-openshift-io-v1) schema |
| 201 - Created | [`Project`](project-project-openshift-io-v1.md#project-project-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/project.openshift.io/v1/watch/projects/{name}

| Parameter | Type     | Description         |
|-----------|----------|---------------------|
| `name`    | `string` | name of the Project |

Global path parameters

HTTP method
`GET`

Description
watch changes to an object of kind Project. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`WatchEvent`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema |
| 401 - Unauthorized | Empty |

HTTP responses
