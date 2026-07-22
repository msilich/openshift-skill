<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Description
InstallPlan defines the installation of a set of operators.

Type
`object`

Required
- `metadata`

- `spec`

# Specification

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
<td style="text-align: left;"><p><code>apiVersion</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <a href="https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources">https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>kind</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <a href="https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds">https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>metadata</code></p></td>
<td style="text-align: left;"><p><a href="../objects/index.xml#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta"><code>ObjectMeta</code></a></p></td>
<td style="text-align: left;"><p>Standard object’s metadata. More info: <a href="https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata">https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>spec</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>InstallPlanSpec defines a set of Application resources to be installed</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>status</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>InstallPlanStatus represents the information about the status of steps required to complete installation.</p>
<p>Status may trail the actual state of a system.</p></td>
</tr>
</tbody>
</table>

## .spec

Description
InstallPlanSpec defines a set of Application resources to be installed

Type
`object`

Required
- `approval`

- `approved`

- `clusterServiceVersionNames`

| Property | Type | Description |
|----|----|----|
| `approval` | `string` | Approval is the user approval policy for an InstallPlan. It must be one of "Automatic" or "Manual". |
| `approved` | `boolean` |  |
| `clusterServiceVersionNames` | `array (string)` |  |
| `generation` | `integer` |  |
| `source` | `string` |  |
| `sourceNamespace` | `string` |  |

## .status

Description
InstallPlanStatus represents the information about the status of steps required to complete installation.

Status may trail the actual state of a system.

Type
`object`

Required
- `catalogSources`

- `phase`

| Property | Type | Description |
|----|----|----|
| `attenuatedServiceAccountRef` | `object` | AttenuatedServiceAccountRef references the service account that is used to do scoped operator install. |
| `bundleLookups` | `array` | BundleLookups is the set of in-progress requests to pull and unpackage bundle content to the cluster. |
| `bundleLookups[]` | `object` | BundleLookup is a request to pull and unpackage the content of a bundle to the cluster. |
| `catalogSources` | `array (string)` |  |
| `conditions` | `array` |  |
| `conditions[]` | `object` | InstallPlanCondition represents the overall status of the execution of an InstallPlan. |
| `message` | `string` | Message is a human-readable message containing detailed information that may be important to understanding why the plan has its current status. |
| `phase` | `string` | InstallPlanPhase is the current status of a InstallPlan as a whole. |
| `plan` | `array` |  |
| `plan[]` | `object` | Step represents the status of an individual step in an InstallPlan. |
| `startTime` | `string` | StartTime is the time when the controller began applying the resources listed in the plan to the cluster. |

## .status.attenuatedServiceAccountRef

Description
AttenuatedServiceAccountRef references the service account that is used to do scoped operator install.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | API version of the referent. |
| `fieldPath` | `string` | If referring to a piece of an object instead of an entire object, this string should contain a valid JSON/Go field access statement, such as desiredState.manifest.containers\[2\]. For example, if the object reference is to a container within a pod, this would take on a value like: "spec.containers{name}" (where "name" refers to the name of the container that triggered the event) or if no container name is specified "spec.containers\[2\]" (container with index 2 in this pod). This syntax is chosen only to have some well-defined way of referencing a part of an object. |
| `kind` | `string` | Kind of the referent. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `name` | `string` | Name of the referent. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names> |
| `namespace` | `string` | Namespace of the referent. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/> |
| `resourceVersion` | `string` | Specific resourceVersion to which this reference is made, if any. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#concurrency-control-and-consistency> |
| `uid` | `string` | UID of the referent. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#uids> |

## .status.bundleLookups

Description
BundleLookups is the set of in-progress requests to pull and unpackage bundle content to the cluster.

Type
`array`

## .status.bundleLookups\[\]

Description
BundleLookup is a request to pull and unpackage the content of a bundle to the cluster.

Type
`object`

Required
- `catalogSourceRef`

- `identifier`

- `path`

- `replaces`

| Property | Type | Description |
|----|----|----|
| `catalogSourceRef` | `object` | CatalogSourceRef is a reference to the CatalogSource the bundle path was resolved from. |
| `conditions` | `array` | Conditions represents the overall state of a BundleLookup. |
| `conditions[]` | `object` |  |
| `identifier` | `string` | Identifier is the catalog-unique name of the operator (the name of the CSV for bundles that contain CSVs) |
| `path` | `string` | Path refers to the location of a bundle to pull. It’s typically an image reference. |
| `properties` | `string` | The effective properties of the unpacked bundle. |
| `replaces` | `string` | Replaces is the name of the bundle to replace with the one found at Path. |

## .status.bundleLookups\[\].catalogSourceRef

Description
CatalogSourceRef is a reference to the CatalogSource the bundle path was resolved from.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | API version of the referent. |
| `fieldPath` | `string` | If referring to a piece of an object instead of an entire object, this string should contain a valid JSON/Go field access statement, such as desiredState.manifest.containers\[2\]. For example, if the object reference is to a container within a pod, this would take on a value like: "spec.containers{name}" (where "name" refers to the name of the container that triggered the event) or if no container name is specified "spec.containers\[2\]" (container with index 2 in this pod). This syntax is chosen only to have some well-defined way of referencing a part of an object. |
| `kind` | `string` | Kind of the referent. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `name` | `string` | Name of the referent. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names> |
| `namespace` | `string` | Namespace of the referent. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/> |
| `resourceVersion` | `string` | Specific resourceVersion to which this reference is made, if any. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#concurrency-control-and-consistency> |
| `uid` | `string` | UID of the referent. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#uids> |

## .status.bundleLookups\[\].conditions

Description
Conditions represents the overall state of a BundleLookup.

Type
`array`

## .status.bundleLookups\[\].conditions\[\]

Description

Type
`object`

Required
- `status`

- `type`

| Property | Type | Description |
|----|----|----|
| `lastTransitionTime` | `string` | Last time the condition transitioned from one status to another. |
| `lastUpdateTime` | `string` | Last time the condition was probed. |
| `message` | `string` | A human readable message indicating details about the transition. |
| `reason` | `string` | The reason for the condition’s last transition. |
| `status` | `string` | Status of the condition, one of True, False, Unknown. |
| `type` | `string` | Type of condition. |

## .status.conditions

Description

Type
`array`

## .status.conditions\[\]

Description
InstallPlanCondition represents the overall status of the execution of an InstallPlan.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `lastTransitionTime` | `string` |  |
| `lastUpdateTime` | `string` |  |
| `message` | `string` |  |
| `reason` | `string` | ConditionReason is a camelcased reason for the state transition. |
| `status` | `string` |  |
| `type` | `string` | InstallPlanConditionType describes the state of an InstallPlan at a certain point as a whole. |

## .status.plan

Description

Type
`array`

## .status.plan\[\]

Description
Step represents the status of an individual step in an InstallPlan.

Type
`object`

Required
- `resolving`

- `resource`

- `status`

| Property | Type | Description |
|----|----|----|
| `optional` | `boolean` |  |
| `resolving` | `string` |  |
| `resource` | `object` | StepResource represents the status of a resource to be tracked by an InstallPlan. |
| `status` | `string` | StepStatus is the current status of a particular resource an in InstallPlan |

## .status.plan\[\].resource

Description
StepResource represents the status of a resource to be tracked by an InstallPlan.

Type
`object`

Required
- `group`

- `kind`

- `name`

- `sourceName`

- `sourceNamespace`

- `version`

| Property          | Type     | Description |
|-------------------|----------|-------------|
| `group`           | `string` |             |
| `kind`            | `string` |             |
| `manifest`        | `string` |             |
| `name`            | `string` |             |
| `sourceName`      | `string` |             |
| `sourceNamespace` | `string` |             |
| `version`         | `string` |             |

# API endpoints

The following API endpoints are available:

- `/apis/operators.coreos.com/v1alpha1/installplans`

  - `GET`: list objects of kind InstallPlan

- `/apis/operators.coreos.com/v1alpha1/namespaces/{namespace}/installplans`

  - `DELETE`: delete collection of InstallPlan

  - `GET`: list objects of kind InstallPlan

  - `POST`: create an InstallPlan

- `/apis/operators.coreos.com/v1alpha1/namespaces/{namespace}/installplans/{name}`

  - `DELETE`: delete an InstallPlan

  - `GET`: read the specified InstallPlan

  - `PATCH`: partially update the specified InstallPlan

  - `PUT`: replace the specified InstallPlan

- `/apis/operators.coreos.com/v1alpha1/namespaces/{namespace}/installplans/{name}/status`

  - `GET`: read status of the specified InstallPlan

  - `PATCH`: partially update status of the specified InstallPlan

  - `PUT`: replace status of the specified InstallPlan

## /apis/operators.coreos.com/v1alpha1/installplans

HTTP method
`GET`

Description
list objects of kind InstallPlan

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`InstallPlanList`](../objects/index.md#com-coreos-operators-v1alpha1-InstallPlanList) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/operators.coreos.com/v1alpha1/namespaces/{namespace}/installplans

HTTP method
`DELETE`

Description
delete collection of InstallPlan

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Status`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`GET`

Description
list objects of kind InstallPlan

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`InstallPlanList`](../objects/index.md#com-coreos-operators-v1alpha1-InstallPlanList) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`POST`

Description
create an InstallPlan

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`InstallPlan`](installplan-operators-coreos-com-v1alpha1.md#installplan-operators-coreos-com-v1alpha1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`InstallPlan`](installplan-operators-coreos-com-v1alpha1.md#installplan-operators-coreos-com-v1alpha1) schema |
| 201 - Created | [`InstallPlan`](installplan-operators-coreos-com-v1alpha1.md#installplan-operators-coreos-com-v1alpha1) schema |
| 202 - Accepted | [`InstallPlan`](installplan-operators-coreos-com-v1alpha1.md#installplan-operators-coreos-com-v1alpha1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/operators.coreos.com/v1alpha1/namespaces/{namespace}/installplans/{name}

| Parameter | Type     | Description             |
|-----------|----------|-------------------------|
| `name`    | `string` | name of the InstallPlan |

Global path parameters

HTTP method
`DELETE`

Description
delete an InstallPlan

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
read the specified InstallPlan

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`InstallPlan`](installplan-operators-coreos-com-v1alpha1.md#installplan-operators-coreos-com-v1alpha1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PATCH`

Description
partially update the specified InstallPlan

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`InstallPlan`](installplan-operators-coreos-com-v1alpha1.md#installplan-operators-coreos-com-v1alpha1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PUT`

Description
replace the specified InstallPlan

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`InstallPlan`](installplan-operators-coreos-com-v1alpha1.md#installplan-operators-coreos-com-v1alpha1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`InstallPlan`](installplan-operators-coreos-com-v1alpha1.md#installplan-operators-coreos-com-v1alpha1) schema |
| 201 - Created | [`InstallPlan`](installplan-operators-coreos-com-v1alpha1.md#installplan-operators-coreos-com-v1alpha1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/operators.coreos.com/v1alpha1/namespaces/{namespace}/installplans/{name}/status

| Parameter | Type     | Description             |
|-----------|----------|-------------------------|
| `name`    | `string` | name of the InstallPlan |

Global path parameters

HTTP method
`GET`

Description
read status of the specified InstallPlan

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`InstallPlan`](installplan-operators-coreos-com-v1alpha1.md#installplan-operators-coreos-com-v1alpha1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PATCH`

Description
partially update status of the specified InstallPlan

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`InstallPlan`](installplan-operators-coreos-com-v1alpha1.md#installplan-operators-coreos-com-v1alpha1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PUT`

Description
replace status of the specified InstallPlan

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`InstallPlan`](installplan-operators-coreos-com-v1alpha1.md#installplan-operators-coreos-com-v1alpha1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`InstallPlan`](installplan-operators-coreos-com-v1alpha1.md#installplan-operators-coreos-com-v1alpha1) schema |
| 201 - Created | [`InstallPlan`](installplan-operators-coreos-com-v1alpha1.md#installplan-operators-coreos-com-v1alpha1) schema |
| 401 - Unauthorized | Empty |

HTTP responses
