<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Description
MachineSet ensures that a specified number of machines replicas are running at any given time. Compatibility level 2: Stable within a major release for a minimum of 9 months or 3 minor releases (whichever is longer).

Type
`object`

# Specification

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ObjectMeta`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) | Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |
| `spec` | `object` | MachineSetSpec defines the desired state of MachineSet |
| `status` | `object` | MachineSetStatus defines the observed state of MachineSet |

## .spec

Description
MachineSetSpec defines the desired state of MachineSet

Type
`object`

| Property | Type | Description |
|----|----|----|
| `deletePolicy` | `string` | deletePolicy defines the policy used to identify nodes to delete when downscaling. Defaults to "Random". Valid values are "Random, "Newest", "Oldest" |
| `minReadySeconds` | `integer` | minReadySeconds is the minimum number of seconds for which a newly created machine should be ready. Defaults to 0 (machine will be considered available as soon as it is ready) |
| `replicas` | `integer` | replicas is the number of desired replicas. This is a pointer to distinguish between explicit zero and unspecified. Defaults to 1. |
| `selector` | `object` | selector is a label query over machines that should match the replica count. Label keys and values that must match in order to be controlled by this MachineSet. It must match the machine template’s labels. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#label-selectors> |
| `template` | `object` | template is the object that describes the machine that will be created if insufficient replicas are detected. |

## .spec.selector

Description
selector is a label query over machines that should match the replica count. Label keys and values that must match in order to be controlled by this MachineSet. It must match the machine template’s labels. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#label-selectors>

Type
`object`

| Property | Type | Description |
|----|----|----|
| `matchExpressions` | `array` | matchExpressions is a list of label selector requirements. The requirements are ANDed. |
| `matchExpressions[]` | `object` | A label selector requirement is a selector that contains values, a key, and an operator that relates the key and values. |
| `matchLabels` | `object (string)` | matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed. |

## .spec.selector.matchExpressions

Description
matchExpressions is a list of label selector requirements. The requirements are ANDed.

Type
`array`

## .spec.selector.matchExpressions\[\]

Description
A label selector requirement is a selector that contains values, a key, and an operator that relates the key and values.

Type
`object`

Required
- `key`

- `operator`

| Property | Type | Description |
|----|----|----|
| `key` | `string` | key is the label key that the selector applies to. |
| `operator` | `string` | operator represents a key’s relationship to a set of values. Valid operators are In, NotIn, Exists and DoesNotExist. |
| `values` | `array (string)` | values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch. |

## .spec.template

Description
template is the object that describes the machine that will be created if insufficient replicas are detected.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `metadata` | `object` | Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |
| `spec` | `object` | Specification of the desired behavior of the machine. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status> |

## .spec.template.metadata

Description
Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata>

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
<td style="text-align: left;"><p><code>annotations</code></p></td>
<td style="text-align: left;"><p><code>object (string)</code></p></td>
<td style="text-align: left;"><p>annotations is an unstructured key value map stored with a resource that may be set by external tools to store and retrieve arbitrary metadata. They are not queryable and should be preserved when modifying objects. More info: <a href="http://kubernetes.io/docs/user-guide/annotations">http://kubernetes.io/docs/user-guide/annotations</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>generateName</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>generateName is an optional prefix, used by the server, to generate a unique name ONLY IF the Name field has not been provided. If this field is used, the name returned to the client will be different than the name passed. This value will also be combined with a unique suffix. The provided value has the same validation rules as the Name field, and may be truncated by the length of the suffix required to make the value unique on the server.</p>
<p>If this field is specified and the generated name exists, the server will NOT return a 409 - instead, it will either return 201 Created or 500 with Reason ServerTimeout indicating a unique name could not be found in the time allotted, and the client should retry (optionally after the time indicated in the Retry-After header).</p>
<p>Applied only if Name is not specified. More info: <a href="https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#idempotency">https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#idempotency</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>labels</code></p></td>
<td style="text-align: left;"><p><code>object (string)</code></p></td>
<td style="text-align: left;"><p>Map of string keys and values that can be used to organize and categorize (scope and select) objects. May match selectors of replication controllers and services. More info: <a href="http://kubernetes.io/docs/user-guide/labels">http://kubernetes.io/docs/user-guide/labels</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>name</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>name must be unique within a namespace. Is required when creating resources, although some resources may allow a client to request the generation of an appropriate name automatically. Name is primarily intended for creation idempotence and configuration definition. Cannot be updated. More info: <a href="http://kubernetes.io/docs/user-guide/identifiers#names">http://kubernetes.io/docs/user-guide/identifiers#names</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>namespace</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>namespace defines the space within each name must be unique. An empty namespace is equivalent to the "default" namespace, but "default" is the canonical representation. Not all objects are required to be scoped to a namespace - the value of this field for those objects will be empty.</p>
<p>Must be a DNS_LABEL. Cannot be updated. More info: <a href="http://kubernetes.io/docs/user-guide/namespaces">http://kubernetes.io/docs/user-guide/namespaces</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>ownerReferences</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>List of objects depended by this object. If ALL objects in the list have been deleted, this object will be garbage collected. If this object is managed by a controller, then an entry in this list will point to this controller, with the controller field set to true. There cannot be more than one managing controller.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>ownerReferences[]</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>OwnerReference contains enough information to let you identify an owning object. An owning object must be in the same namespace as the dependent, or be cluster-scoped, so there is no namespace field.</p></td>
</tr>
</tbody>
</table>

## .spec.template.metadata.ownerReferences

Description
List of objects depended by this object. If ALL objects in the list have been deleted, this object will be garbage collected. If this object is managed by a controller, then an entry in this list will point to this controller, with the controller field set to true. There cannot be more than one managing controller.

Type
`array`

## .spec.template.metadata.ownerReferences\[\]

Description
OwnerReference contains enough information to let you identify an owning object. An owning object must be in the same namespace as the dependent, or be cluster-scoped, so there is no namespace field.

Type
`object`

Required
- `apiVersion`

- `kind`

- `name`

- `uid`

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | API version of the referent. |
| `blockOwnerDeletion` | `boolean` | If true, AND if the owner has the "foregroundDeletion" finalizer, then the owner cannot be deleted from the key-value store until this reference is removed. See <https://kubernetes.io/docs/concepts/architecture/garbage-collection/#foreground-deletion> for how the garbage collector interacts with this field and enforces the foreground deletion. Defaults to false. To set this field, a user needs "delete" permission of the owner, otherwise 422 (Unprocessable Entity) will be returned. |
| `controller` | `boolean` | If true, this reference points to the managing controller. |
| `kind` | `string` | Kind of the referent. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `name` | `string` | Name of the referent. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names#names> |
| `uid` | `string` | UID of the referent. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names#uids> |

## .spec.template.spec

Description
Specification of the desired behavior of the machine. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status>

Type
`object`

| Property | Type | Description |
|----|----|----|
| `lifecycleHooks` | `object` | lifecycleHooks allow users to pause operations on the machine at certain predefined points within the machine lifecycle. |
| `metadata` | `object` | ObjectMeta will autopopulate the Node created. Use this to indicate what labels, annotations, name prefix, etc., should be used when creating the Node. |
| `providerID` | `string` | providerID is the identification ID of the machine provided by the provider. This field must match the provider ID as seen on the node object corresponding to this machine. This field is required by higher level consumers of cluster-api. Example use case is cluster autoscaler with cluster-api as provider. Clean-up logic in the autoscaler compares machines to nodes to find out machines at provider which could not get registered as Kubernetes nodes. With cluster-api as a generic out-of-tree provider for autoscaler, this field is required by autoscaler to be able to have a provider view of the list of machines. Another list of nodes is queried from the k8s apiserver and then a comparison is done to find out unregistered machines and are marked for delete. This field will be set by the actuators and consumed by higher level entities like autoscaler that will be interfacing with cluster-api as generic provider. |
| `providerSpec` | `object` | providerSpec details Provider-specific configuration to use during node creation. |
| `taints` | `array` | The list of the taints to be applied to the corresponding Node in additive manner. This list will not overwrite any other taints added to the Node on an ongoing basis by other entities. These taints should be actively reconciled e.g. if you ask the machine controller to apply a taint and then manually remove the taint the machine controller will put it back) but not have the machine controller remove any taints |
| `taints[]` | `object` | The node this Taint is attached to has the "effect" on any pod that does not tolerate the Taint. |

## .spec.template.spec.lifecycleHooks

Description
lifecycleHooks allow users to pause operations on the machine at certain predefined points within the machine lifecycle.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `preDrain` | `array` | preDrain hooks prevent the machine from being drained. This also blocks further lifecycle events, such as termination. |
| `preDrain[]` | `object` | LifecycleHook represents a single instance of a lifecycle hook |
| `preTerminate` | `array` | preTerminate hooks prevent the machine from being terminated. PreTerminate hooks be actioned after the Machine has been drained. |
| `preTerminate[]` | `object` | LifecycleHook represents a single instance of a lifecycle hook |

## .spec.template.spec.lifecycleHooks.preDrain

Description
preDrain hooks prevent the machine from being drained. This also blocks further lifecycle events, such as termination.

Type
`array`

## .spec.template.spec.lifecycleHooks.preDrain\[\]

Description
LifecycleHook represents a single instance of a lifecycle hook

Type
`object`

Required
- `name`

- `owner`

| Property | Type | Description |
|----|----|----|
| `name` | `string` | name defines a unique name for the lifcycle hook. The name should be unique and descriptive, ideally 1-3 words, in CamelCase or it may be namespaced, eg. foo.example.com/CamelCase. Names must be unique and should only be managed by a single entity. |
| `owner` | `string` | owner defines the owner of the lifecycle hook. This should be descriptive enough so that users can identify who/what is responsible for blocking the lifecycle. This could be the name of a controller (e.g. clusteroperator/etcd) or an administrator managing the hook. |

## .spec.template.spec.lifecycleHooks.preTerminate

Description
preTerminate hooks prevent the machine from being terminated. PreTerminate hooks be actioned after the Machine has been drained.

Type
`array`

## .spec.template.spec.lifecycleHooks.preTerminate\[\]

Description
LifecycleHook represents a single instance of a lifecycle hook

Type
`object`

Required
- `name`

- `owner`

| Property | Type | Description |
|----|----|----|
| `name` | `string` | name defines a unique name for the lifcycle hook. The name should be unique and descriptive, ideally 1-3 words, in CamelCase or it may be namespaced, eg. foo.example.com/CamelCase. Names must be unique and should only be managed by a single entity. |
| `owner` | `string` | owner defines the owner of the lifecycle hook. This should be descriptive enough so that users can identify who/what is responsible for blocking the lifecycle. This could be the name of a controller (e.g. clusteroperator/etcd) or an administrator managing the hook. |

## .spec.template.spec.metadata

Description
ObjectMeta will autopopulate the Node created. Use this to indicate what labels, annotations, name prefix, etc., should be used when creating the Node.

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
<td style="text-align: left;"><p><code>annotations</code></p></td>
<td style="text-align: left;"><p><code>object (string)</code></p></td>
<td style="text-align: left;"><p>annotations is an unstructured key value map stored with a resource that may be set by external tools to store and retrieve arbitrary metadata. They are not queryable and should be preserved when modifying objects. More info: <a href="http://kubernetes.io/docs/user-guide/annotations">http://kubernetes.io/docs/user-guide/annotations</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>generateName</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>generateName is an optional prefix, used by the server, to generate a unique name ONLY IF the Name field has not been provided. If this field is used, the name returned to the client will be different than the name passed. This value will also be combined with a unique suffix. The provided value has the same validation rules as the Name field, and may be truncated by the length of the suffix required to make the value unique on the server.</p>
<p>If this field is specified and the generated name exists, the server will NOT return a 409 - instead, it will either return 201 Created or 500 with Reason ServerTimeout indicating a unique name could not be found in the time allotted, and the client should retry (optionally after the time indicated in the Retry-After header).</p>
<p>Applied only if Name is not specified. More info: <a href="https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#idempotency">https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#idempotency</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>labels</code></p></td>
<td style="text-align: left;"><p><code>object (string)</code></p></td>
<td style="text-align: left;"><p>Map of string keys and values that can be used to organize and categorize (scope and select) objects. May match selectors of replication controllers and services. More info: <a href="http://kubernetes.io/docs/user-guide/labels">http://kubernetes.io/docs/user-guide/labels</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>name</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>name must be unique within a namespace. Is required when creating resources, although some resources may allow a client to request the generation of an appropriate name automatically. Name is primarily intended for creation idempotence and configuration definition. Cannot be updated. More info: <a href="http://kubernetes.io/docs/user-guide/identifiers#names">http://kubernetes.io/docs/user-guide/identifiers#names</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>namespace</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>namespace defines the space within each name must be unique. An empty namespace is equivalent to the "default" namespace, but "default" is the canonical representation. Not all objects are required to be scoped to a namespace - the value of this field for those objects will be empty.</p>
<p>Must be a DNS_LABEL. Cannot be updated. More info: <a href="http://kubernetes.io/docs/user-guide/namespaces">http://kubernetes.io/docs/user-guide/namespaces</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>ownerReferences</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>List of objects depended by this object. If ALL objects in the list have been deleted, this object will be garbage collected. If this object is managed by a controller, then an entry in this list will point to this controller, with the controller field set to true. There cannot be more than one managing controller.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>ownerReferences[]</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>OwnerReference contains enough information to let you identify an owning object. An owning object must be in the same namespace as the dependent, or be cluster-scoped, so there is no namespace field.</p></td>
</tr>
</tbody>
</table>

## .spec.template.spec.metadata.ownerReferences

Description
List of objects depended by this object. If ALL objects in the list have been deleted, this object will be garbage collected. If this object is managed by a controller, then an entry in this list will point to this controller, with the controller field set to true. There cannot be more than one managing controller.

Type
`array`

## .spec.template.spec.metadata.ownerReferences\[\]

Description
OwnerReference contains enough information to let you identify an owning object. An owning object must be in the same namespace as the dependent, or be cluster-scoped, so there is no namespace field.

Type
`object`

Required
- `apiVersion`

- `kind`

- `name`

- `uid`

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | API version of the referent. |
| `blockOwnerDeletion` | `boolean` | If true, AND if the owner has the "foregroundDeletion" finalizer, then the owner cannot be deleted from the key-value store until this reference is removed. See <https://kubernetes.io/docs/concepts/architecture/garbage-collection/#foreground-deletion> for how the garbage collector interacts with this field and enforces the foreground deletion. Defaults to false. To set this field, a user needs "delete" permission of the owner, otherwise 422 (Unprocessable Entity) will be returned. |
| `controller` | `boolean` | If true, this reference points to the managing controller. |
| `kind` | `string` | Kind of the referent. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `name` | `string` | Name of the referent. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names#names> |
| `uid` | `string` | UID of the referent. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names#uids> |

## .spec.template.spec.providerSpec

Description
providerSpec details Provider-specific configuration to use during node creation.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `value` | \`\` | value is an inlined, serialized representation of the resource configuration. It is recommended that providers maintain their own versioned API types that should be serialized/deserialized from this field, akin to component config. |

## .spec.template.spec.taints

Description
The list of the taints to be applied to the corresponding Node in additive manner. This list will not overwrite any other taints added to the Node on an ongoing basis by other entities. These taints should be actively reconciled e.g. if you ask the machine controller to apply a taint and then manually remove the taint the machine controller will put it back) but not have the machine controller remove any taints

Type
`array`

## .spec.template.spec.taints\[\]

Description
The node this Taint is attached to has the "effect" on any pod that does not tolerate the Taint.

Type
`object`

Required
- `effect`

- `key`

| Property | Type | Description |
|----|----|----|
| `effect` | `string` | Required. The effect of the taint on pods that do not tolerate the taint. Valid effects are NoSchedule, PreferNoSchedule and NoExecute. |
| `key` | `string` | Required. The taint key to be applied to a node. |
| `timeAdded` | `string` | TimeAdded represents the time at which the taint was added. It is only written for NoExecute taints. |
| `value` | `string` | The taint value corresponding to the taint key. |

## .status

Description
MachineSetStatus defines the observed state of MachineSet

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
<td style="text-align: left;"><p>The number of available replicas (ready for at least minReadySeconds) for this MachineSet.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>conditions</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>conditions defines the current state of the MachineSet</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>conditions[]</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>Condition defines an observation of a Machine API resource operational state.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>errorMessage</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>errorReason</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>In the event that there is a terminal problem reconciling the replicas, both ErrorReason and ErrorMessage will be set. ErrorReason will be populated with a succinct value suitable for machine interpretation, while ErrorMessage will contain a more verbose string suitable for logging and human consumption.</p>
<p>These fields should not be set for transitive errors that a controller faces that are expected to be fixed automatically over time (like service outages), but instead indicate that something is fundamentally wrong with the MachineTemplate’s spec or the configuration of the machine controller, and that manual intervention is required. Examples of terminal errors would be invalid combinations of settings in the spec, values that are unsupported by the machine controller, or the responsible machine controller itself being critically misconfigured.</p>
<p>Any transient errors that occur during the reconciliation of Machines can be added as events to the MachineSet object and/or logged in the controller’s output.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>fullyLabeledReplicas</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p>The number of replicas that have labels matching the labels of the machine template of the MachineSet.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>observedGeneration</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p>observedGeneration reflects the generation of the most recently observed MachineSet.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>readyReplicas</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p>The number of ready replicas for this MachineSet. A machine is considered ready when the node has been created and is "Ready".</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>replicas</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p>replicas is the most recently observed number of replicas.</p></td>
</tr>
</tbody>
</table>

## .status.conditions

Description
conditions defines the current state of the MachineSet

Type
`array`

## .status.conditions\[\]

Description
Condition defines an observation of a Machine API resource operational state.

Type
`object`

Required
- `lastTransitionTime`

- `status`

- `type`

| Property | Type | Description |
|----|----|----|
| `lastTransitionTime` | `string` | Last time the condition transitioned from one status to another. This should be when the underlying condition changed. If that is not known, then using the time when the API field changed is acceptable. |
| `message` | `string` | A human readable message indicating details about the transition. This field may be empty. |
| `reason` | `string` | The reason for the condition’s last transition in CamelCase. The specific API may choose whether or not this field is considered a guaranteed API. This field may not be empty. |
| `severity` | `string` | severity provides an explicit classification of Reason code, so the users or machines can immediately understand the current situation and act accordingly. The Severity field MUST be set only when Status=False. |
| `status` | `string` | status of the condition, one of True, False, Unknown. |
| `type` | `string` | type of condition in CamelCase or in foo.example.com/CamelCase. Many .condition.type values are consistent across resources like Available, but because arbitrary conditions can be useful (see .node.status.conditions), the ability to deconflict is important. |

# API endpoints

The following API endpoints are available:

- `/apis/machine.openshift.io/v1beta1/machinesets`

  - `GET`: list objects of kind MachineSet

- `/apis/machine.openshift.io/v1beta1/namespaces/{namespace}/machinesets`

  - `DELETE`: delete collection of MachineSet

  - `GET`: list objects of kind MachineSet

  - `POST`: create a MachineSet

- `/apis/machine.openshift.io/v1beta1/namespaces/{namespace}/machinesets/{name}`

  - `DELETE`: delete a MachineSet

  - `GET`: read the specified MachineSet

  - `PATCH`: partially update the specified MachineSet

  - `PUT`: replace the specified MachineSet

- `/apis/machine.openshift.io/v1beta1/namespaces/{namespace}/machinesets/{name}/scale`

  - `GET`: read scale of the specified MachineSet

  - `PATCH`: partially update scale of the specified MachineSet

  - `PUT`: replace scale of the specified MachineSet

- `/apis/machine.openshift.io/v1beta1/namespaces/{namespace}/machinesets/{name}/status`

  - `GET`: read status of the specified MachineSet

  - `PATCH`: partially update status of the specified MachineSet

  - `PUT`: replace status of the specified MachineSet

## /apis/machine.openshift.io/v1beta1/machinesets

HTTP method
`GET`

Description
list objects of kind MachineSet

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`MachineSetList`](../objects/index.md#io-openshift-machine-v1beta1-MachineSetList) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/machine.openshift.io/v1beta1/namespaces/{namespace}/machinesets

HTTP method
`DELETE`

Description
delete collection of MachineSet

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Status`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`GET`

Description
list objects of kind MachineSet

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`MachineSetList`](../objects/index.md#io-openshift-machine-v1beta1-MachineSetList) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`POST`

Description
create a MachineSet

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`MachineSet`](machineset-machine-openshift-io-v1beta1.md#machineset-machine-openshift-io-v1beta1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`MachineSet`](machineset-machine-openshift-io-v1beta1.md#machineset-machine-openshift-io-v1beta1) schema |
| 201 - Created | [`MachineSet`](machineset-machine-openshift-io-v1beta1.md#machineset-machine-openshift-io-v1beta1) schema |
| 202 - Accepted | [`MachineSet`](machineset-machine-openshift-io-v1beta1.md#machineset-machine-openshift-io-v1beta1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/machine.openshift.io/v1beta1/namespaces/{namespace}/machinesets/{name}

| Parameter | Type     | Description            |
|-----------|----------|------------------------|
| `name`    | `string` | name of the MachineSet |

Global path parameters

HTTP method
`DELETE`

Description
delete a MachineSet

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
read the specified MachineSet

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`MachineSet`](machineset-machine-openshift-io-v1beta1.md#machineset-machine-openshift-io-v1beta1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PATCH`

Description
partially update the specified MachineSet

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`MachineSet`](machineset-machine-openshift-io-v1beta1.md#machineset-machine-openshift-io-v1beta1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PUT`

Description
replace the specified MachineSet

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`MachineSet`](machineset-machine-openshift-io-v1beta1.md#machineset-machine-openshift-io-v1beta1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`MachineSet`](machineset-machine-openshift-io-v1beta1.md#machineset-machine-openshift-io-v1beta1) schema |
| 201 - Created | [`MachineSet`](machineset-machine-openshift-io-v1beta1.md#machineset-machine-openshift-io-v1beta1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/machine.openshift.io/v1beta1/namespaces/{namespace}/machinesets/{name}/scale

| Parameter | Type     | Description            |
|-----------|----------|------------------------|
| `name`    | `string` | name of the MachineSet |

Global path parameters

HTTP method
`GET`

Description
read scale of the specified MachineSet

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Scale`](../autoscale_apis/scale-autoscaling-v1.md#scale-autoscaling-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PATCH`

Description
partially update scale of the specified MachineSet

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Scale`](../autoscale_apis/scale-autoscaling-v1.md#scale-autoscaling-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PUT`

Description
replace scale of the specified MachineSet

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`Scale`](../autoscale_apis/scale-autoscaling-v1.md#scale-autoscaling-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Scale`](../autoscale_apis/scale-autoscaling-v1.md#scale-autoscaling-v1) schema |
| 201 - Created | [`Scale`](../autoscale_apis/scale-autoscaling-v1.md#scale-autoscaling-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/machine.openshift.io/v1beta1/namespaces/{namespace}/machinesets/{name}/status

| Parameter | Type     | Description            |
|-----------|----------|------------------------|
| `name`    | `string` | name of the MachineSet |

Global path parameters

HTTP method
`GET`

Description
read status of the specified MachineSet

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`MachineSet`](machineset-machine-openshift-io-v1beta1.md#machineset-machine-openshift-io-v1beta1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PATCH`

Description
partially update status of the specified MachineSet

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`MachineSet`](machineset-machine-openshift-io-v1beta1.md#machineset-machine-openshift-io-v1beta1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PUT`

Description
replace status of the specified MachineSet

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`MachineSet`](machineset-machine-openshift-io-v1beta1.md#machineset-machine-openshift-io-v1beta1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`MachineSet`](machineset-machine-openshift-io-v1beta1.md#machineset-machine-openshift-io-v1beta1) schema |
| 201 - Created | [`MachineSet`](machineset-machine-openshift-io-v1beta1.md#machineset-machine-openshift-io-v1beta1) schema |
| 401 - Unauthorized | Empty |

HTTP responses
