<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Description
Deployment enables declarative updates for Pods and ReplicaSets.

Type
`object`

# Specification

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ObjectMeta`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) | Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |
| `spec` | `object` | DeploymentSpec is the specification of the desired behavior of the Deployment. |
| `status` | `object` | DeploymentStatus is the most recently observed status of the Deployment. |

## .spec

Description
DeploymentSpec is the specification of the desired behavior of the Deployment.

Type
`object`

Required
- `selector`

- `template`

| Property | Type | Description |
|----|----|----|
| `minReadySeconds` | `integer` | Minimum number of seconds for which a newly created pod should be ready without any of its container crashing, for it to be considered available. Defaults to 0 (pod will be considered available as soon as it is ready) |
| `paused` | `boolean` | Indicates that the deployment is paused. |
| `progressDeadlineSeconds` | `integer` | The maximum time in seconds for a deployment to make progress before it is considered to be failed. The deployment controller will continue to process failed deployments and a condition with a ProgressDeadlineExceeded reason will be surfaced in the deployment status. Note that progress will not be estimated during the time a deployment is paused. Defaults to 600s. |
| `replicas` | `integer` | Number of desired pods. This is a pointer to distinguish between explicit zero and not specified. Defaults to 1. |
| `revisionHistoryLimit` | `integer` | The number of old ReplicaSets to retain to allow rollback. This is a pointer to distinguish between explicit zero and not specified. Defaults to 10. |
| `selector` | [`LabelSelector`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-LabelSelector) | Label selector for pods. Existing ReplicaSets whose pods are selected by this will be the ones affected by this deployment. It must match the pod template’s labels. |
| `strategy` | `object` | DeploymentStrategy describes how to replace existing pods with new ones. |
| `template` | [`PodTemplateSpec`](../objects/index.md#io-k8s-api-core-v1-PodTemplateSpec) | Template describes the pods that will be created. The only allowed template.spec.restartPolicy value is "Always". |

## .spec.strategy

Description
DeploymentStrategy describes how to replace existing pods with new ones.

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
<td style="text-align: left;"><p><code>rollingUpdate</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>Spec to control the desired behavior of rolling update.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>type</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Type of deployment. Can be "Recreate" or "RollingUpdate". Default is RollingUpdate.</p>
<p>Possible enum values: - <code>"Recreate"</code> Kill all existing pods before creating new ones. - <code>"RollingUpdate"</code> Replace the old ReplicaSets by new one using rolling update i.e gradually scale down the old ReplicaSets and scale up the new one.</p></td>
</tr>
</tbody>
</table>

## .spec.strategy.rollingUpdate

Description
Spec to control the desired behavior of rolling update.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `maxSurge` | [`IntOrString`](../objects/index.md#io-k8s-apimachinery-pkg-util-intstr-IntOrString) | The maximum number of pods that can be scheduled above the desired number of pods. Value can be an absolute number (ex: 5) or a percentage of desired pods (ex: 10%). This can not be 0 if MaxUnavailable is 0. Absolute number is calculated from percentage by rounding up. Defaults to 25%. Example: when this is set to 30%, the new ReplicaSet can be scaled up immediately when the rolling update starts, such that the total number of old and new pods do not exceed 130% of desired pods. Once old pods have been killed, new ReplicaSet can be scaled up further, ensuring that total number of pods running at any time during the update is at most 130% of desired pods. |
| `maxUnavailable` | [`IntOrString`](../objects/index.md#io-k8s-apimachinery-pkg-util-intstr-IntOrString) | The maximum number of pods that can be unavailable during the update. Value can be an absolute number (ex: 5) or a percentage of desired pods (ex: 10%). Absolute number is calculated from percentage by rounding down. This can not be 0 if MaxSurge is 0. Defaults to 25%. Example: when this is set to 30%, the old ReplicaSet can be scaled down to 70% of desired pods immediately when the rolling update starts. Once new pods are ready, old ReplicaSet can be scaled down further, followed by scaling up the new ReplicaSet, ensuring that the total number of pods available at all times during the update is at least 70% of desired pods. |

## .status

Description
DeploymentStatus is the most recently observed status of the Deployment.

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
<td style="text-align: left;"><p><code>availableReplicas</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p>Total number of available non-terminating pods (ready for at least minReadySeconds) targeted by this deployment.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>collisionCount</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p>Count of hash collisions for the Deployment. The Deployment controller uses this field as a collision avoidance mechanism when it needs to create the name for the newest ReplicaSet.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>conditions</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>Represents the latest available observations of a deployment’s current state.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>conditions[]</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>DeploymentCondition describes the state of a deployment at a certain point.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>observedGeneration</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p>The generation observed by the deployment controller.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>readyReplicas</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p>Total number of non-terminating pods targeted by this Deployment with a Ready Condition.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>replicas</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p>Total number of non-terminating pods targeted by this deployment (their labels match the selector).</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>terminatingReplicas</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p>Total number of terminating pods targeted by this deployment. Terminating pods have a non-null .metadata.deletionTimestamp and have not yet reached the Failed or Succeeded .status.phase.</p>
<p>This is an alpha field. Enable DeploymentReplicaSetTerminatingReplicas to be able to use this field.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>unavailableReplicas</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p>Total number of unavailable pods targeted by this deployment. This is the total number of pods that are still required for the deployment to have 100% available capacity. They may either be pods that are running but not yet available or pods that still have not been created.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>updatedReplicas</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p>Total number of non-terminating pods targeted by this deployment that have the desired template spec.</p></td>
</tr>
</tbody>
</table>

## .status.conditions

Description
Represents the latest available observations of a deployment’s current state.

Type
`array`

## .status.conditions\[\]

Description
DeploymentCondition describes the state of a deployment at a certain point.

Type
`object`

Required
- `type`

- `status`

| Property | Type | Description |
|----|----|----|
| `lastTransitionTime` | [`Time`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-Time) | Last time the condition transitioned from one status to another. |
| `lastUpdateTime` | [`Time`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-Time) | The last time this condition was updated. |
| `message` | `string` | A human readable message indicating details about the transition. |
| `reason` | `string` | The reason for the condition’s last transition. |
| `status` | `string` | Status of the condition, one of True, False, Unknown. |
| `type` | `string` | Type of deployment condition. |

# API endpoints

The following API endpoints are available:

- `/apis/apps/v1/deployments`

  - `GET`: list or watch objects of kind Deployment

- `/apis/apps/v1/watch/deployments`

  - `GET`: watch individual changes to a list of Deployment. deprecated: use the 'watch' parameter with a list operation instead.

- `/apis/apps/v1/namespaces/{namespace}/deployments`

  - `DELETE`: delete collection of Deployment

  - `GET`: list or watch objects of kind Deployment

  - `POST`: create a Deployment

- `/apis/apps/v1/watch/namespaces/{namespace}/deployments`

  - `GET`: watch individual changes to a list of Deployment. deprecated: use the 'watch' parameter with a list operation instead.

- `/apis/apps/v1/namespaces/{namespace}/deployments/{name}`

  - `DELETE`: delete a Deployment

  - `GET`: read the specified Deployment

  - `PATCH`: partially update the specified Deployment

  - `PUT`: replace the specified Deployment

- `/apis/apps/v1/watch/namespaces/{namespace}/deployments/{name}`

  - `GET`: watch changes to an object of kind Deployment. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.

- `/apis/apps/v1/namespaces/{namespace}/deployments/{name}/status`

  - `GET`: read status of the specified Deployment

  - `PATCH`: partially update status of the specified Deployment

  - `PUT`: replace status of the specified Deployment

## /apis/apps/v1/deployments

HTTP method
`GET`

Description
list or watch objects of kind Deployment

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`DeploymentList`](../objects/index.md#io-k8s-api-apps-v1-DeploymentList) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/apps/v1/watch/deployments

HTTP method
`GET`

Description
watch individual changes to a list of Deployment. deprecated: use the 'watch' parameter with a list operation instead.

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`WatchEvent`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/apps/v1/namespaces/{namespace}/deployments

HTTP method
`DELETE`

Description
delete collection of Deployment

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
list or watch objects of kind Deployment

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`DeploymentList`](../objects/index.md#io-k8s-api-apps-v1-DeploymentList) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`POST`

Description
create a Deployment

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`Deployment`](deployment-apps-v1.md#deployment-apps-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Deployment`](deployment-apps-v1.md#deployment-apps-v1) schema |
| 201 - Created | [`Deployment`](deployment-apps-v1.md#deployment-apps-v1) schema |
| 202 - Accepted | [`Deployment`](deployment-apps-v1.md#deployment-apps-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/apps/v1/watch/namespaces/{namespace}/deployments

HTTP method
`GET`

Description
watch individual changes to a list of Deployment. deprecated: use the 'watch' parameter with a list operation instead.

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`WatchEvent`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/apps/v1/namespaces/{namespace}/deployments/{name}

| Parameter | Type     | Description            |
|-----------|----------|------------------------|
| `name`    | `string` | name of the Deployment |

Global path parameters

HTTP method
`DELETE`

Description
delete a Deployment

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
read the specified Deployment

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Deployment`](deployment-apps-v1.md#deployment-apps-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PATCH`

Description
partially update the specified Deployment

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Deployment`](deployment-apps-v1.md#deployment-apps-v1) schema |
| 201 - Created | [`Deployment`](deployment-apps-v1.md#deployment-apps-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PUT`

Description
replace the specified Deployment

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`Deployment`](deployment-apps-v1.md#deployment-apps-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Deployment`](deployment-apps-v1.md#deployment-apps-v1) schema |
| 201 - Created | [`Deployment`](deployment-apps-v1.md#deployment-apps-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/apps/v1/watch/namespaces/{namespace}/deployments/{name}

| Parameter | Type     | Description            |
|-----------|----------|------------------------|
| `name`    | `string` | name of the Deployment |

Global path parameters

HTTP method
`GET`

Description
watch changes to an object of kind Deployment. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`WatchEvent`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/apps/v1/namespaces/{namespace}/deployments/{name}/status

| Parameter | Type     | Description            |
|-----------|----------|------------------------|
| `name`    | `string` | name of the Deployment |

Global path parameters

HTTP method
`GET`

Description
read status of the specified Deployment

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Deployment`](deployment-apps-v1.md#deployment-apps-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PATCH`

Description
partially update status of the specified Deployment

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Deployment`](deployment-apps-v1.md#deployment-apps-v1) schema |
| 201 - Created | [`Deployment`](deployment-apps-v1.md#deployment-apps-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PUT`

Description
replace status of the specified Deployment

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`Deployment`](deployment-apps-v1.md#deployment-apps-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Deployment`](deployment-apps-v1.md#deployment-apps-v1) schema |
| 201 - Created | [`Deployment`](deployment-apps-v1.md#deployment-apps-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses
