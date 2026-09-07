<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Description
KubeScheduler provides information to configure an operator to manage scheduler.

Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).

Type
`object`

Required
- `spec`

# Specification

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ObjectMeta`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) | Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |
| `spec` | `object` | spec is the specification of the desired behavior of the Kubernetes Scheduler |
| `status` | `object` | status is the most recently observed status of the Kubernetes Scheduler |

## .spec

Description
spec is the specification of the desired behavior of the Kubernetes Scheduler

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
<td style="text-align: left;"><p><code>failedRevisionLimit</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p>failedRevisionLimit is the number of failed static pod installer revisions to keep on disk and in the api -1 = unlimited, 0 or unset = 5 (default)</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>forceRedeploymentReason</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>forceRedeploymentReason can be used to force the redeployment of the operand by providing a unique string. This provides a mechanism to kick a previously failed deployment and provide a reason why you think it will work this time instead of failing again on the same config.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>logLevel</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>logLevel is an intent based logging for an overall component. It does not give fine grained control, but it is a simple way to manage coarse grained logging choices that operators have to interpret for their operands.</p>
<p>Valid values are: "Normal", "Debug", "Trace", "TraceAll". Defaults to "Normal".</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>managementState</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>managementState indicates whether and how the operator should manage the component</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>observedConfig</code></p></td>
<td style="text-align: left;"><p>``</p></td>
<td style="text-align: left;"><p>observedConfig holds a sparse config that controller has observed from the cluster state. It exists in spec because it is an input to the level for the operator</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>operatorLogLevel</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>operatorLogLevel is an intent based logging for the operator itself. It does not give fine grained control, but it is a simple way to manage coarse grained logging choices that operators have to interpret for themselves.</p>
<p>Valid values are: "Normal", "Debug", "Trace", "TraceAll". Defaults to "Normal".</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>succeededRevisionLimit</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p>succeededRevisionLimit is the number of successful static pod installer revisions to keep on disk and in the api -1 = unlimited, 0 or unset = 5 (default)</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>unsupportedConfigOverrides</code></p></td>
<td style="text-align: left;"><p>``</p></td>
<td style="text-align: left;"><p>unsupportedConfigOverrides overrides the final configuration that was computed by the operator. Red Hat does not support the use of this field. Misuse of this field could lead to unexpected behavior or conflict with other configuration options. Seek guidance from the Red Hat support before using this field. Use of this property blocks cluster upgrades, it must be removed before upgrading your cluster.</p></td>
</tr>
</tbody>
</table>

## .status

Description
status is the most recently observed status of the Kubernetes Scheduler

Type
`object`

| Property | Type | Description |
|----|----|----|
| `conditions` | `array` | conditions is a list of conditions and their status |
| `conditions[]` | `object` | OperatorCondition is just the standard condition fields. |
| `generations` | `array` | generations are used to determine when an item needs to be reconciled or has changed in a way that needs a reaction. |
| `generations[]` | `object` | GenerationStatus keeps track of the generation for a given resource so that decisions about forced updates can be made. |
| `latestAvailableRevision` | `integer` | latestAvailableRevision is the deploymentID of the most recent deployment |
| `latestAvailableRevisionReason` | `string` | latestAvailableRevisionReason describe the detailed reason for the most recent deployment |
| `nodeStatuses` | `array` | nodeStatuses track the deployment values and errors across individual nodes |
| `nodeStatuses[]` | `object` | NodeStatus provides information about the current state of a particular node managed by this operator. |
| `observedGeneration` | `integer` | observedGeneration is the last generation change you’ve dealt with |
| `readyReplicas` | `integer` | readyReplicas indicates how many replicas are ready and at the desired state |
| `version` | `string` | version is the level this availability applies to |

## .status.conditions

Description
conditions is a list of conditions and their status

Type
`array`

## .status.conditions\[\]

Description
OperatorCondition is just the standard condition fields.

Type
`object`

Required
- `lastTransitionTime`

- `status`

- `type`

| Property | Type | Description |
|----|----|----|
| `lastTransitionTime` | `string` | lastTransitionTime is the last time the condition transitioned from one status to another. This should be when the underlying condition changed. If that is not known, then using the time when the API field changed is acceptable. |
| `message` | `string` |  |
| `reason` | `string` |  |
| `status` | `string` | status of the condition, one of True, False, Unknown. |
| `type` | `string` | type of condition in CamelCase or in foo.example.com/CamelCase. |

## .status.generations

Description
generations are used to determine when an item needs to be reconciled or has changed in a way that needs a reaction.

Type
`array`

## .status.generations\[\]

Description
GenerationStatus keeps track of the generation for a given resource so that decisions about forced updates can be made.

Type
`object`

Required
- `group`

- `name`

- `namespace`

- `resource`

| Property | Type | Description |
|----|----|----|
| `group` | `string` | group is the group of the thing you’re tracking |
| `hash` | `string` | hash is an optional field set for resources without generation that are content sensitive like secrets and configmaps |
| `lastGeneration` | `integer` | lastGeneration is the last generation of the workload controller involved |
| `name` | `string` | name is the name of the thing you’re tracking |
| `namespace` | `string` | namespace is where the thing you’re tracking is |
| `resource` | `string` | resource is the resource type of the thing you’re tracking |

## .status.nodeStatuses

Description
nodeStatuses track the deployment values and errors across individual nodes

Type
`array`

## .status.nodeStatuses\[\]

Description
NodeStatus provides information about the current state of a particular node managed by this operator.

Type
`object`

Required
- `nodeName`

| Property | Type | Description |
|----|----|----|
| `currentRevision` | `integer` | currentRevision is the generation of the most recently successful deployment. Can not be set on creation of a nodeStatus. Updates must only increase the value. |
| `lastFailedCount` | `integer` | lastFailedCount is how often the installer pod of the last failed revision failed. |
| `lastFailedReason` | `string` | lastFailedReason is a machine readable failure reason string. |
| `lastFailedRevision` | `integer` | lastFailedRevision is the generation of the deployment we tried and failed to deploy. |
| `lastFailedRevisionErrors` | `array (string)` | lastFailedRevisionErrors is a list of human readable errors during the failed deployment referenced in lastFailedRevision. |
| `lastFailedTime` | `string` | lastFailedTime is the time the last failed revision failed the last time. |
| `lastFallbackCount` | `integer` | lastFallbackCount is how often a fallback to a previous revision happened. |
| `nodeName` | `string` | nodeName is the name of the node |
| `targetRevision` | `integer` | targetRevision is the generation of the deployment we’re trying to apply. Can not be set on creation of a nodeStatus. |

# API endpoints

The following API endpoints are available:

- `/apis/operator.openshift.io/v1/kubeschedulers`

  - `DELETE`: delete collection of KubeScheduler

  - `GET`: list objects of kind KubeScheduler

  - `POST`: create a KubeScheduler

- `/apis/operator.openshift.io/v1/kubeschedulers/{name}`

  - `DELETE`: delete a KubeScheduler

  - `GET`: read the specified KubeScheduler

  - `PATCH`: partially update the specified KubeScheduler

  - `PUT`: replace the specified KubeScheduler

- `/apis/operator.openshift.io/v1/kubeschedulers/{name}/status`

  - `GET`: read status of the specified KubeScheduler

  - `PATCH`: partially update status of the specified KubeScheduler

  - `PUT`: replace status of the specified KubeScheduler

## /apis/operator.openshift.io/v1/kubeschedulers

HTTP method
`DELETE`

Description
delete collection of KubeScheduler

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Status`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`GET`

Description
list objects of kind KubeScheduler

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`KubeSchedulerList`](../objects/index.md#io-openshift-operator-v1-KubeSchedulerList) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`POST`

Description
create a KubeScheduler

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`KubeScheduler`](kubescheduler-operator-openshift-io-v1.md#kubescheduler-operator-openshift-io-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`KubeScheduler`](kubescheduler-operator-openshift-io-v1.md#kubescheduler-operator-openshift-io-v1) schema |
| 201 - Created | [`KubeScheduler`](kubescheduler-operator-openshift-io-v1.md#kubescheduler-operator-openshift-io-v1) schema |
| 202 - Accepted | [`KubeScheduler`](kubescheduler-operator-openshift-io-v1.md#kubescheduler-operator-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/operator.openshift.io/v1/kubeschedulers/{name}

| Parameter | Type     | Description               |
|-----------|----------|---------------------------|
| `name`    | `string` | name of the KubeScheduler |

Global path parameters

HTTP method
`DELETE`

Description
delete a KubeScheduler

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
read the specified KubeScheduler

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`KubeScheduler`](kubescheduler-operator-openshift-io-v1.md#kubescheduler-operator-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PATCH`

Description
partially update the specified KubeScheduler

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`KubeScheduler`](kubescheduler-operator-openshift-io-v1.md#kubescheduler-operator-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PUT`

Description
replace the specified KubeScheduler

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`KubeScheduler`](kubescheduler-operator-openshift-io-v1.md#kubescheduler-operator-openshift-io-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`KubeScheduler`](kubescheduler-operator-openshift-io-v1.md#kubescheduler-operator-openshift-io-v1) schema |
| 201 - Created | [`KubeScheduler`](kubescheduler-operator-openshift-io-v1.md#kubescheduler-operator-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/operator.openshift.io/v1/kubeschedulers/{name}/status

| Parameter | Type     | Description               |
|-----------|----------|---------------------------|
| `name`    | `string` | name of the KubeScheduler |

Global path parameters

HTTP method
`GET`

Description
read status of the specified KubeScheduler

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`KubeScheduler`](kubescheduler-operator-openshift-io-v1.md#kubescheduler-operator-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PATCH`

Description
partially update status of the specified KubeScheduler

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`KubeScheduler`](kubescheduler-operator-openshift-io-v1.md#kubescheduler-operator-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PUT`

Description
replace status of the specified KubeScheduler

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`KubeScheduler`](kubescheduler-operator-openshift-io-v1.md#kubescheduler-operator-openshift-io-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`KubeScheduler`](kubescheduler-operator-openshift-io-v1.md#kubescheduler-operator-openshift-io-v1) schema |
| 201 - Created | [`KubeScheduler`](kubescheduler-operator-openshift-io-v1.md#kubescheduler-operator-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses
