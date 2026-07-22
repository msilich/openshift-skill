<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Description
ClusterAutoscaler is the Schema for the clusterautoscalers API

Type
`object`

# Specification

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ObjectMeta`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) | Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |
| `spec` | `object` | Desired state of ClusterAutoscaler resource |
| `status` | `object` | Most recently observed status of ClusterAutoscaler resource |

## .spec

Description
Desired state of ClusterAutoscaler resource

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
<td style="text-align: left;"><p><code>balanceSimilarNodeGroups</code></p></td>
<td style="text-align: left;"><p><code>boolean</code></p></td>
<td style="text-align: left;"><p>BalanceSimilarNodeGroups enables/disables the <code>--balance-similar-node-groups</code> cluster-autoscaler feature. This feature will automatically identify node groups with the same instance type and the same set of labels and try to keep the respective sizes of those node groups balanced.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>balancingIgnoredLabels</code></p></td>
<td style="text-align: left;"><p><code>array (string)</code></p></td>
<td style="text-align: left;"><p>BalancingIgnoredLabels sets "--balancing-ignore-label &lt;label name&gt;" flag on cluster-autoscaler for each listed label. This option specifies labels that cluster autoscaler should ignore when considering node group similarity. For example, if you have nodes with "topology.ebs.csi.aws.com/zone" label, you can add name of this label here to prevent cluster autoscaler from spliting nodes into different node groups based on its value.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>expanders</code></p></td>
<td style="text-align: left;"><p><code>array (string)</code></p></td>
<td style="text-align: left;"><p>Sets the type and order of expanders to be used during scale out operations. This option specifies an ordered list, highest priority first, of expanders that will be used by the cluster autoscaler to select node groups for expansion when scaling out. Expanders instruct the autoscaler on how to choose node groups when scaling out the cluster. They can be specified in order so that the result from the first expander is used as the input to the second, and so forth. For example, if set to <code>[LeastWaste, Random]</code> the autoscaler will first evaluate node groups to determine which will have the least resource waste, if multiple groups are selected the autoscaler will then randomly choose between those groups to determine the group for scaling. The following expanders are available: * LeastWaste - selects the node group that will have the least idle CPU (if tied, unused memory) after scale-up. * Priority - selects the node group that has the highest priority assigned by the user. For details, please see <a href="https://github.com/openshift/kubernetes-autoscaler/blob/master/cluster-autoscaler/expander/priority/readme.md">https://github.com/openshift/kubernetes-autoscaler/blob/master/cluster-autoscaler/expander/priority/readme.md</a> * Random - selects the node group randomly. If not specified, the default value is <code>Random</code>, available options are: <code>LeastWaste</code>, <code>Priority</code>, <code>Random</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>ignoreDaemonsetsUtilization</code></p></td>
<td style="text-align: left;"><p><code>boolean</code></p></td>
<td style="text-align: left;"><p>Enables/Disables <code>--ignore-daemonsets-utilization</code> CA feature flag. Should CA ignore DaemonSet pods when calculating resource utilization for scaling down. false by default</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>logVerbosity</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p>Sets the autoscaler log level. Default value is 1, level 4 is recommended for DEBUGGING and level 6 will enable almost everything.</p>
<p>This option has priority over log level set by the <code>CLUSTER_AUTOSCALER_VERBOSITY</code> environment variable.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>maxNodeProvisionTime</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Maximum time CA waits for node to be provisioned</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>maxPodGracePeriod</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p>Gives pods graceful termination time before scaling down</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>podPriorityThreshold</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p>To allow users to schedule "best-effort" pods, which shouldn’t trigger Cluster Autoscaler actions, but only run when there are spare resources available, More info: <a href="https://github.com/kubernetes/autoscaler/blob/master/cluster-autoscaler/FAQ.md#how-does-cluster-autoscaler-work-with-pod-priority-and-preemption">https://github.com/kubernetes/autoscaler/blob/master/cluster-autoscaler/FAQ.md#how-does-cluster-autoscaler-work-with-pod-priority-and-preemption</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>resourceLimits</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>Constraints of autoscaling resources</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>scaleDown</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>Configuration of scale down operation</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>scaleUp</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>Configuration of scale up operation</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>skipNodesWithLocalStorage</code></p></td>
<td style="text-align: left;"><p><code>boolean</code></p></td>
<td style="text-align: left;"><p>Enables/Disables <code>--skip-nodes-with-local-storage</code> CA feature flag. If true cluster autoscaler will never delete nodes with pods with local storage, e.g. EmptyDir or HostPath. true by default at autoscaler</p></td>
</tr>
</tbody>
</table>

## .spec.resourceLimits

Description
Constraints of autoscaling resources

Type
`object`

| Property | Type | Description |
|----|----|----|
| `cores` | `object` | Minimum and maximum number of cores in cluster, in the format \<min\>:\<max\>. Cluster autoscaler will not scale the cluster beyond these numbers. |
| `gpus` | `array` | Minimum and maximum number of different GPUs in cluster, in the format \<gpu_type\>:\<min\>:\<max\>. Cluster autoscaler will not scale the cluster beyond these numbers. Can be passed multiple times. |
| `gpus[]` | `object` |  |
| `maxNodesTotal` | `integer` | Maximum number of nodes in all node groups. Cluster autoscaler will not grow the cluster beyond this number. |
| `memory` | `object` | Minimum and maximum number of GiB of memory in cluster, in the format \<min\>:\<max\>. Cluster autoscaler will not scale the cluster beyond these numbers. |

## .spec.resourceLimits.cores

Description
Minimum and maximum number of cores in cluster, in the format \<min\>:\<max\>. Cluster autoscaler will not scale the cluster beyond these numbers.

Type
`object`

Required
- `max`

- `min`

| Property | Type      | Description |
|----------|-----------|-------------|
| `max`    | `integer` |             |
| `min`    | `integer` |             |

## .spec.resourceLimits.gpus

Description
Minimum and maximum number of different GPUs in cluster, in the format \<gpu_type\>:\<min\>:\<max\>. Cluster autoscaler will not scale the cluster beyond these numbers. Can be passed multiple times.

Type
`array`

## .spec.resourceLimits.gpus\[\]

Description

Type
`object`

Required
- `max`

- `min`

- `type`

| Property | Type | Description |
|----|----|----|
| `max` | `integer` |  |
| `min` | `integer` |  |
| `type` | `string` | The type of GPU to associate with the minimum and maximum limits. This value is used by the Cluster Autoscaler to identify Nodes that will have GPU capacity by searching for it as a label value on the Node objects. For example, Nodes that carry the label key `cluster-api/accelerator` with the label value being the same as the Type field will be counted towards the resource limits by the Cluster Autoscaler. |

## .spec.resourceLimits.memory

Description
Minimum and maximum number of GiB of memory in cluster, in the format \<min\>:\<max\>. Cluster autoscaler will not scale the cluster beyond these numbers.

Type
`object`

Required
- `max`

- `min`

| Property | Type      | Description |
|----------|-----------|-------------|
| `max`    | `integer` |             |
| `min`    | `integer` |             |

## .spec.scaleDown

Description
Configuration of scale down operation

Type
`object`

Required
- `enabled`

| Property | Type | Description |
|----|----|----|
| `delayAfterAdd` | `string` | How long after scale up that scale down evaluation resumes |
| `delayAfterDelete` | `string` | How long after node deletion that scale down evaluation resumes, defaults to scan-interval |
| `delayAfterFailure` | `string` | How long after scale down failure that scale down evaluation resumes |
| `enabled` | `boolean` | Should CA scale down the cluster |
| `unneededTime` | `string` | How long a node should be unneeded before it is eligible for scale down |
| `utilizationThreshold` | `string` | Node utilization level, defined as sum of requested resources divided by capacity, below which a node can be considered for scale down |

## .spec.scaleUp

Description
Configuration of scale up operation

Type
`object`

| Property | Type | Description |
|----|----|----|
| `newPodScaleUpDelay` | `string` | Scale up delay for new pods, if omitted defaults to 0 seconds |

## .status

Description
Most recently observed status of ClusterAutoscaler resource

Type
`object`

# API endpoints

The following API endpoints are available:

- `/apis/autoscaling.openshift.io/v1/clusterautoscalers`

  - `DELETE`: delete collection of ClusterAutoscaler

  - `GET`: list objects of kind ClusterAutoscaler

  - `POST`: create a ClusterAutoscaler

- `/apis/autoscaling.openshift.io/v1/clusterautoscalers/{name}`

  - `DELETE`: delete a ClusterAutoscaler

  - `GET`: read the specified ClusterAutoscaler

  - `PATCH`: partially update the specified ClusterAutoscaler

  - `PUT`: replace the specified ClusterAutoscaler

- `/apis/autoscaling.openshift.io/v1/clusterautoscalers/{name}/status`

  - `GET`: read status of the specified ClusterAutoscaler

  - `PATCH`: partially update status of the specified ClusterAutoscaler

  - `PUT`: replace status of the specified ClusterAutoscaler

## /apis/autoscaling.openshift.io/v1/clusterautoscalers

HTTP method
`DELETE`

Description
delete collection of ClusterAutoscaler

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Status`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`GET`

Description
list objects of kind ClusterAutoscaler

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ClusterAutoscalerList`](../objects/index.md#io-openshift-autoscaling-v1-ClusterAutoscalerList) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`POST`

Description
create a ClusterAutoscaler

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`ClusterAutoscaler`](clusterautoscaler-autoscaling-openshift-io-v1.md#clusterautoscaler-autoscaling-openshift-io-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ClusterAutoscaler`](clusterautoscaler-autoscaling-openshift-io-v1.md#clusterautoscaler-autoscaling-openshift-io-v1) schema |
| 201 - Created | [`ClusterAutoscaler`](clusterautoscaler-autoscaling-openshift-io-v1.md#clusterautoscaler-autoscaling-openshift-io-v1) schema |
| 202 - Accepted | [`ClusterAutoscaler`](clusterautoscaler-autoscaling-openshift-io-v1.md#clusterautoscaler-autoscaling-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/autoscaling.openshift.io/v1/clusterautoscalers/{name}

| Parameter | Type     | Description                   |
|-----------|----------|-------------------------------|
| `name`    | `string` | name of the ClusterAutoscaler |

Global path parameters

HTTP method
`DELETE`

Description
delete a ClusterAutoscaler

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
read the specified ClusterAutoscaler

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ClusterAutoscaler`](clusterautoscaler-autoscaling-openshift-io-v1.md#clusterautoscaler-autoscaling-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PATCH`

Description
partially update the specified ClusterAutoscaler

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ClusterAutoscaler`](clusterautoscaler-autoscaling-openshift-io-v1.md#clusterautoscaler-autoscaling-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PUT`

Description
replace the specified ClusterAutoscaler

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`ClusterAutoscaler`](clusterautoscaler-autoscaling-openshift-io-v1.md#clusterautoscaler-autoscaling-openshift-io-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ClusterAutoscaler`](clusterautoscaler-autoscaling-openshift-io-v1.md#clusterautoscaler-autoscaling-openshift-io-v1) schema |
| 201 - Created | [`ClusterAutoscaler`](clusterautoscaler-autoscaling-openshift-io-v1.md#clusterautoscaler-autoscaling-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/autoscaling.openshift.io/v1/clusterautoscalers/{name}/status

| Parameter | Type     | Description                   |
|-----------|----------|-------------------------------|
| `name`    | `string` | name of the ClusterAutoscaler |

Global path parameters

HTTP method
`GET`

Description
read status of the specified ClusterAutoscaler

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ClusterAutoscaler`](clusterautoscaler-autoscaling-openshift-io-v1.md#clusterautoscaler-autoscaling-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PATCH`

Description
partially update status of the specified ClusterAutoscaler

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ClusterAutoscaler`](clusterautoscaler-autoscaling-openshift-io-v1.md#clusterautoscaler-autoscaling-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PUT`

Description
replace status of the specified ClusterAutoscaler

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`ClusterAutoscaler`](clusterautoscaler-autoscaling-openshift-io-v1.md#clusterautoscaler-autoscaling-openshift-io-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ClusterAutoscaler`](clusterautoscaler-autoscaling-openshift-io-v1.md#clusterautoscaler-autoscaling-openshift-io-v1) schema |
| 201 - Created | [`ClusterAutoscaler`](clusterautoscaler-autoscaling-openshift-io-v1.md#clusterautoscaler-autoscaling-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses
