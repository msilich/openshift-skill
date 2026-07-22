<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Description
ReplicaSet ensures that a specified number of pod replicas are running at any given time.

Type
`object`

# Specification

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ObjectMeta`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) | If the Labels of a ReplicaSet are empty, they are defaulted to be the same as the Pod(s) that the ReplicaSet manages. Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |
| `spec` | `object` | ReplicaSetSpec is the specification of a ReplicaSet. |
| `status` | `object` | ReplicaSetStatus represents the current status of a ReplicaSet. |

## .spec

Description
ReplicaSetSpec is the specification of a ReplicaSet.

Type
`object`

Required
- `selector`

| Property | Type | Description |
|----|----|----|
| `minReadySeconds` | `integer` | Minimum number of seconds for which a newly created pod should be ready without any of its container crashing, for it to be considered available. Defaults to 0 (pod will be considered available as soon as it is ready) |
| `replicas` | `integer` | Replicas is the number of desired pods. This is a pointer to distinguish between explicit zero and unspecified. Defaults to 1. More info: <https://kubernetes.io/docs/concepts/workloads/controllers/replicaset> |
| `selector` | [`LabelSelector`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-LabelSelector) | Selector is a label query over pods that should match the replica count. Label keys and values that must match in order to be controlled by this replica set. It must match the pod template’s labels. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#label-selectors> |
| `template` | [`PodTemplateSpec`](../objects/index.md#io-k8s-api-core-v1-PodTemplateSpec) | Template is the object that describes the pod that will be created if insufficient replicas are detected. More info: <https://kubernetes.io/docs/concepts/workloads/controllers/replicaset/#pod-template> |

## .status

Description
ReplicaSetStatus represents the current status of a ReplicaSet.

Type
`object`

Required
- `replicas`

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
<td style="text-align: left;"><p>The number of available non-terminating pods (ready for at least minReadySeconds) for this replica set.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>conditions</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>Represents the latest available observations of a replica set’s current state.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>conditions[]</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>ReplicaSetCondition describes the state of a replica set at a certain point.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>fullyLabeledReplicas</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p>The number of non-terminating pods that have labels matching the labels of the pod template of the replicaset.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>observedGeneration</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p>ObservedGeneration reflects the generation of the most recently observed ReplicaSet.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>readyReplicas</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p>The number of non-terminating pods targeted by this ReplicaSet with a Ready Condition.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>replicas</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p>Replicas is the most recently observed number of non-terminating pods. More info: <a href="https://kubernetes.io/docs/concepts/workloads/controllers/replicaset">https://kubernetes.io/docs/concepts/workloads/controllers/replicaset</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>terminatingReplicas</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p>The number of terminating pods for this replica set. Terminating pods have a non-null .metadata.deletionTimestamp and have not yet reached the Failed or Succeeded .status.phase.</p>
<p>This is an alpha field. Enable DeploymentReplicaSetTerminatingReplicas to be able to use this field.</p></td>
</tr>
</tbody>
</table>

## .status.conditions

Description
Represents the latest available observations of a replica set’s current state.

Type
`array`

## .status.conditions\[\]

Description
ReplicaSetCondition describes the state of a replica set at a certain point.

Type
`object`

Required
- `type`

- `status`

| Property | Type | Description |
|----|----|----|
| `lastTransitionTime` | [`Time`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-Time) | The last time the condition transitioned from one status to another. |
| `message` | `string` | A human readable message indicating details about the transition. |
| `reason` | `string` | The reason for the condition’s last transition. |
| `status` | `string` | Status of the condition, one of True, False, Unknown. |
| `type` | `string` | Type of replica set condition. |

# API endpoints

The following API endpoints are available:

- `/apis/apps/v1/replicasets`

  - `GET`: list or watch objects of kind ReplicaSet

- `/apis/apps/v1/watch/replicasets`

  - `GET`: watch individual changes to a list of ReplicaSet. deprecated: use the 'watch' parameter with a list operation instead.

- `/apis/apps/v1/namespaces/{namespace}/replicasets`

  - `DELETE`: delete collection of ReplicaSet

  - `GET`: list or watch objects of kind ReplicaSet

  - `POST`: create a ReplicaSet

- `/apis/apps/v1/watch/namespaces/{namespace}/replicasets`

  - `GET`: watch individual changes to a list of ReplicaSet. deprecated: use the 'watch' parameter with a list operation instead.

- `/apis/apps/v1/namespaces/{namespace}/replicasets/{name}`

  - `DELETE`: delete a ReplicaSet

  - `GET`: read the specified ReplicaSet

  - `PATCH`: partially update the specified ReplicaSet

  - `PUT`: replace the specified ReplicaSet

- `/apis/apps/v1/watch/namespaces/{namespace}/replicasets/{name}`

  - `GET`: watch changes to an object of kind ReplicaSet. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.

- `/apis/apps/v1/namespaces/{namespace}/replicasets/{name}/status`

  - `GET`: read status of the specified ReplicaSet

  - `PATCH`: partially update status of the specified ReplicaSet

  - `PUT`: replace status of the specified ReplicaSet

## /apis/apps/v1/replicasets

HTTP method
`GET`

Description
list or watch objects of kind ReplicaSet

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ReplicaSetList`](../objects/index.md#io-k8s-api-apps-v1-ReplicaSetList) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/apps/v1/watch/replicasets

HTTP method
`GET`

Description
watch individual changes to a list of ReplicaSet. deprecated: use the 'watch' parameter with a list operation instead.

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`WatchEvent`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/apps/v1/namespaces/{namespace}/replicasets

HTTP method
`DELETE`

Description
delete collection of ReplicaSet

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
list or watch objects of kind ReplicaSet

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ReplicaSetList`](../objects/index.md#io-k8s-api-apps-v1-ReplicaSetList) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`POST`

Description
create a ReplicaSet

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`ReplicaSet`](replicaset-apps-v1.md#replicaset-apps-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ReplicaSet`](replicaset-apps-v1.md#replicaset-apps-v1) schema |
| 201 - Created | [`ReplicaSet`](replicaset-apps-v1.md#replicaset-apps-v1) schema |
| 202 - Accepted | [`ReplicaSet`](replicaset-apps-v1.md#replicaset-apps-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/apps/v1/watch/namespaces/{namespace}/replicasets

HTTP method
`GET`

Description
watch individual changes to a list of ReplicaSet. deprecated: use the 'watch' parameter with a list operation instead.

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`WatchEvent`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/apps/v1/namespaces/{namespace}/replicasets/{name}

| Parameter | Type     | Description            |
|-----------|----------|------------------------|
| `name`    | `string` | name of the ReplicaSet |

Global path parameters

HTTP method
`DELETE`

Description
delete a ReplicaSet

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
read the specified ReplicaSet

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ReplicaSet`](replicaset-apps-v1.md#replicaset-apps-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PATCH`

Description
partially update the specified ReplicaSet

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ReplicaSet`](replicaset-apps-v1.md#replicaset-apps-v1) schema |
| 201 - Created | [`ReplicaSet`](replicaset-apps-v1.md#replicaset-apps-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PUT`

Description
replace the specified ReplicaSet

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`ReplicaSet`](replicaset-apps-v1.md#replicaset-apps-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ReplicaSet`](replicaset-apps-v1.md#replicaset-apps-v1) schema |
| 201 - Created | [`ReplicaSet`](replicaset-apps-v1.md#replicaset-apps-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/apps/v1/watch/namespaces/{namespace}/replicasets/{name}

| Parameter | Type     | Description            |
|-----------|----------|------------------------|
| `name`    | `string` | name of the ReplicaSet |

Global path parameters

HTTP method
`GET`

Description
watch changes to an object of kind ReplicaSet. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`WatchEvent`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/apps/v1/namespaces/{namespace}/replicasets/{name}/status

| Parameter | Type     | Description            |
|-----------|----------|------------------------|
| `name`    | `string` | name of the ReplicaSet |

Global path parameters

HTTP method
`GET`

Description
read status of the specified ReplicaSet

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ReplicaSet`](replicaset-apps-v1.md#replicaset-apps-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PATCH`

Description
partially update status of the specified ReplicaSet

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ReplicaSet`](replicaset-apps-v1.md#replicaset-apps-v1) schema |
| 201 - Created | [`ReplicaSet`](replicaset-apps-v1.md#replicaset-apps-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PUT`

Description
replace status of the specified ReplicaSet

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`ReplicaSet`](replicaset-apps-v1.md#replicaset-apps-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ReplicaSet`](replicaset-apps-v1.md#replicaset-apps-v1) schema |
| 201 - Created | [`ReplicaSet`](replicaset-apps-v1.md#replicaset-apps-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses
