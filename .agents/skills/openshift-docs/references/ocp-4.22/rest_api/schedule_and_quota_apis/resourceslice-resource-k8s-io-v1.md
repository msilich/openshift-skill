<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Description
ResourceSlice represents one or more resources in a pool of similar resources, managed by a common driver. A pool may span more than one ResourceSlice, and exactly how many ResourceSlices comprise a pool is determined by the driver.

At the moment, the only supported resources are devices with attributes and capacities. Each device in a given pool, regardless of how many ResourceSlices, must have a unique name. The ResourceSlice in which a device gets published may change over time. The unique identifier for a device is the tuple \<driver name\>, \<pool name\>, \<device name\>.

Whenever a driver needs to update a pool, it increments the pool.Spec.Pool.Generation number and updates all ResourceSlices with that new number and new resource definitions. A consumer must only use ResourceSlices with the highest generation number and ignore all others.

When allocating all resources in a pool matching certain criteria or when looking for the best solution among several different alternatives, a consumer should check the number of ResourceSlices in a pool (included in each ResourceSlice) to determine whether its view of a pool is complete and if not, should wait until the driver has completed updating the pool.

For resources that are not local to a node, the node name is not set. Instead, the driver may use a node selector to specify where the devices are available.

This is an alpha type and requires enabling the DynamicResourceAllocation feature gate.

Type
`object`

Required
- `spec`

# Specification

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ObjectMeta`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) | Standard object metadata |
| `spec` | `object` | ResourceSliceSpec contains the information published by the driver in one ResourceSlice. |

## .spec

Description
ResourceSliceSpec contains the information published by the driver in one ResourceSlice.

Type
`object`

Required
- `driver`

- `pool`

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
<td style="text-align: left;"><p><code>allNodes</code></p></td>
<td style="text-align: left;"><p><code>boolean</code></p></td>
<td style="text-align: left;"><p>AllNodes indicates that all nodes have access to the resources in the pool.</p>
<p>Exactly one of NodeName, NodeSelector, AllNodes, and PerDeviceNodeSelection must be set.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>devices</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>Devices lists some or all of the devices in this pool.</p>
<p>Must not have more than 128 entries. If any device uses taints or consumes counters the limit is 64.</p>
<p>Only one of Devices and SharedCounters can be set in a ResourceSlice.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>devices[]</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>Device represents one individual hardware instance that can be selected based on its attributes. Besides the name, exactly one field must be set.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>driver</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Driver identifies the DRA driver providing the capacity information. A field selector can be used to list only ResourceSlice objects with a certain driver name.</p>
<p>Must be a DNS subdomain and should end with a DNS domain owned by the vendor of the driver. It should use only lower case characters. This field is immutable.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>nodeName</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>NodeName identifies the node which provides the resources in this pool. A field selector can be used to list only ResourceSlice objects belonging to a certain node.</p>
<p>This field can be used to limit access from nodes to ResourceSlices with the same node name. It also indicates to autoscalers that adding new nodes of the same type as some old node might also make new resources available.</p>
<p>Exactly one of NodeName, NodeSelector, AllNodes, and PerDeviceNodeSelection must be set. This field is immutable.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>nodeSelector</code></p></td>
<td style="text-align: left;"><p><a href="../objects/index.xml#io-k8s-api-core-v1-NodeSelector"><code>NodeSelector</code></a></p></td>
<td style="text-align: left;"><p>NodeSelector defines which nodes have access to the resources in the pool, when that pool is not limited to a single node.</p>
<p>Must use exactly one term.</p>
<p>Exactly one of NodeName, NodeSelector, AllNodes, and PerDeviceNodeSelection must be set.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>perDeviceNodeSelection</code></p></td>
<td style="text-align: left;"><p><code>boolean</code></p></td>
<td style="text-align: left;"><p>PerDeviceNodeSelection defines whether the access from nodes to resources in the pool is set on the ResourceSlice level or on each device. If it is set to true, every device defined the ResourceSlice must specify this individually.</p>
<p>Exactly one of NodeName, NodeSelector, AllNodes, and PerDeviceNodeSelection must be set.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>pool</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>ResourcePool describes the pool that ResourceSlices belong to.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>sharedCounters</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>SharedCounters defines a list of counter sets, each of which has a name and a list of counters available.</p>
<p>The names of the counter sets must be unique in the ResourcePool.</p>
<p>Only one of Devices and SharedCounters can be set in a ResourceSlice.</p>
<p>The maximum number of counter sets is 8.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>sharedCounters[]</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>CounterSet defines a named set of counters that are available to be used by devices defined in the ResourcePool.</p>
<p>The counters are not allocatable by themselves, but can be referenced by devices. When a device is allocated, the portion of counters it uses will no longer be available for use by other devices.</p></td>
</tr>
</tbody>
</table>

## .spec.devices

Description
Devices lists some or all of the devices in this pool.

Must not have more than 128 entries. If any device uses taints or consumes counters the limit is 64.

Only one of Devices and SharedCounters can be set in a ResourceSlice.

Type
`array`

## .spec.devices\[\]

Description
Device represents one individual hardware instance that can be selected based on its attributes. Besides the name, exactly one field must be set.

Type
`object`

Required
- `name`

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
<td style="text-align: left;"><p><code>allNodes</code></p></td>
<td style="text-align: left;"><p><code>boolean</code></p></td>
<td style="text-align: left;"><p>AllNodes indicates that all nodes have access to the device.</p>
<p>Must only be set if Spec.PerDeviceNodeSelection is set to true. At most one of NodeName, NodeSelector and AllNodes can be set.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>allowMultipleAllocations</code></p></td>
<td style="text-align: left;"><p><code>boolean</code></p></td>
<td style="text-align: left;"><p>AllowMultipleAllocations marks whether the device is allowed to be allocated to multiple DeviceRequests.</p>
<p>If AllowMultipleAllocations is set to true, the device can be allocated more than once, and all of its capacity is consumable, regardless of whether the requestPolicy is defined or not.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>attributes</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>Attributes defines the set of attributes for this device. The name of each attribute must be unique in that set.</p>
<p>The maximum number of attributes and capacities combined is 32.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>attributes{}</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>DeviceAttribute must have exactly one field set.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>bindingConditions</code></p></td>
<td style="text-align: left;"><p><code>array (string)</code></p></td>
<td style="text-align: left;"><p>BindingConditions defines the conditions for proceeding with binding. All of these conditions must be set in the per-device status conditions with a value of True to proceed with binding the pod to the node while scheduling the pod.</p>
<p>The maximum number of binding conditions is 4.</p>
<p>The conditions must be a valid condition type string.</p>
<p>This is an alpha field and requires enabling the DRADeviceBindingConditions and DRAResourceClaimDeviceStatus feature gates.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>bindingFailureConditions</code></p></td>
<td style="text-align: left;"><p><code>array (string)</code></p></td>
<td style="text-align: left;"><p>BindingFailureConditions defines the conditions for binding failure. They may be set in the per-device status conditions. If any is set to "True", a binding failure occurred.</p>
<p>The maximum number of binding failure conditions is 4.</p>
<p>The conditions must be a valid condition type string.</p>
<p>This is an alpha field and requires enabling the DRADeviceBindingConditions and DRAResourceClaimDeviceStatus feature gates.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>bindsToNode</code></p></td>
<td style="text-align: left;"><p><code>boolean</code></p></td>
<td style="text-align: left;"><p>BindsToNode indicates if the usage of an allocation involving this device has to be limited to exactly the node that was chosen when allocating the claim. If set to true, the scheduler will set the ResourceClaim.Status.Allocation.NodeSelector to match the node where the allocation was made.</p>
<p>This is an alpha field and requires enabling the DRADeviceBindingConditions and DRAResourceClaimDeviceStatus feature gates.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>capacity</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>Capacity defines the set of capacities for this device. The name of each capacity must be unique in that set.</p>
<p>The maximum number of attributes and capacities combined is 32.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>capacity{}</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>DeviceCapacity describes a quantity associated with a device.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>consumesCounters</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>ConsumesCounters defines a list of references to sharedCounters and the set of counters that the device will consume from those counter sets.</p>
<p>There can only be a single entry per counterSet.</p>
<p>The maximum number of device counter consumptions per device is 2.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>consumesCounters[]</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>DeviceCounterConsumption defines a set of counters that a device will consume from a CounterSet.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>name</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Name is unique identifier among all devices managed by the driver in the pool. It must be a DNS label.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>nodeName</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>NodeName identifies the node where the device is available.</p>
<p>Must only be set if Spec.PerDeviceNodeSelection is set to true. At most one of NodeName, NodeSelector and AllNodes can be set.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>nodeSelector</code></p></td>
<td style="text-align: left;"><p><a href="../objects/index.xml#io-k8s-api-core-v1-NodeSelector"><code>NodeSelector</code></a></p></td>
<td style="text-align: left;"><p>NodeSelector defines the nodes where the device is available.</p>
<p>Must use exactly one term.</p>
<p>Must only be set if Spec.PerDeviceNodeSelection is set to true. At most one of NodeName, NodeSelector and AllNodes can be set.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>taints</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>If specified, these are the driver-defined taints.</p>
<p>The maximum number of taints is 16. If taints are set for any device in a ResourceSlice, then the maximum number of allowed devices per ResourceSlice is 64 instead of 128.</p>
<p>This is an alpha field and requires enabling the DRADeviceTaints feature gate.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>taints[]</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>The device this taint is attached to has the "effect" on any claim which does not tolerate the taint and, through the claim, to pods using the claim.</p></td>
</tr>
</tbody>
</table>

## .spec.devices\[\].attributes

Description
Attributes defines the set of attributes for this device. The name of each attribute must be unique in that set.

The maximum number of attributes and capacities combined is 32.

Type
`object`

## .spec.devices\[\].attributes{}

Description
DeviceAttribute must have exactly one field set.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `bool` | `boolean` | BoolValue is a true/false value. |
| `int` | `integer` | IntValue is a number. |
| `string` | `string` | StringValue is a string. Must not be longer than 64 characters. |
| `version` | `string` | VersionValue is a semantic version according to semver.org spec 2.0.0. Must not be longer than 64 characters. |

## .spec.devices\[\].capacity

Description
Capacity defines the set of capacities for this device. The name of each capacity must be unique in that set.

The maximum number of attributes and capacities combined is 32.

Type
`object`

## .spec.devices\[\].capacity{}

Description
DeviceCapacity describes a quantity associated with a device.

Type
`object`

Required
- `value`

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
<td style="text-align: left;"><p><code>requestPolicy</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>CapacityRequestPolicy defines how requests consume device capacity.</p>
<p>Must not set more than one ValidRequestValues.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>value</code></p></td>
<td style="text-align: left;"><p><a href="../objects/index.xml#io-k8s-apimachinery-pkg-api-resource-Quantity"><code>Quantity</code></a></p></td>
<td style="text-align: left;"><p>Value defines how much of a certain capacity that device has.</p>
<p>This field reflects the fixed total capacity and does not change. The consumed amount is tracked separately by scheduler and does not affect this value.</p></td>
</tr>
</tbody>
</table>

## .spec.devices\[\].capacity{}.requestPolicy

Description
CapacityRequestPolicy defines how requests consume device capacity.

Must not set more than one ValidRequestValues.

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
<td style="text-align: left;"><p><code>default</code></p></td>
<td style="text-align: left;"><p><a href="../objects/index.xml#io-k8s-apimachinery-pkg-api-resource-Quantity"><code>Quantity</code></a></p></td>
<td style="text-align: left;"><p>Default specifies how much of this capacity is consumed by a request that does not contain an entry for it in DeviceRequest’s Capacity.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>validRange</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>CapacityRequestPolicyRange defines a valid range for consumable capacity values.</p>
<p>- If the requested amount is less than Min, it is rounded up to the Min value. - If Step is set and the requested amount is between Min and Max but not aligned with Step, it will be rounded up to the next value equal to Min + (n * Step). - If Step is not set, the requested amount is used as-is if it falls within the range Min to Max (if set). - If the requested or rounded amount exceeds Max (if set), the request does not satisfy the policy, and the device cannot be allocated.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>validValues</code></p></td>
<td style="text-align: left;"><p><a href="../objects/index.xml#io-k8s-apimachinery-pkg-api-resource-Quantity"><code>array (Quantity)</code></a></p></td>
<td style="text-align: left;"><p>ValidValues defines a set of acceptable quantity values in consuming requests.</p>
<p>Must not contain more than 10 entries. Must be sorted in ascending order.</p>
<p>If this field is set, Default must be defined and it must be included in ValidValues list.</p>
<p>If the requested amount does not match any valid value but smaller than some valid values, the scheduler calculates the smallest valid value that is greater than or equal to the request. That is: min(ceil(requestedValue) ∈ validValues), where requestedValue ≤ max(validValues).</p>
<p>If the requested amount exceeds all valid values, the request violates the policy, and this device cannot be allocated.</p></td>
</tr>
</tbody>
</table>

## .spec.devices\[\].capacity{}.requestPolicy.validRange

Description
CapacityRequestPolicyRange defines a valid range for consumable capacity values.

- If the requested amount is less than Min, it is rounded up to the Min value.

- If Step is set and the requested amount is between Min and Max but not aligned with Step, it will be rounded up to the next value equal to Min + (n \* Step).

- If Step is not set, the requested amount is used as-is if it falls within the range Min to Max (if set).

- If the requested or rounded amount exceeds Max (if set), the request does not satisfy the policy, and the device cannot be allocated.

Type
`object`

Required
- `min`

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
<td style="text-align: left;"><p><code>max</code></p></td>
<td style="text-align: left;"><p><a href="../objects/index.xml#io-k8s-apimachinery-pkg-api-resource-Quantity"><code>Quantity</code></a></p></td>
<td style="text-align: left;"><p>Max defines the upper limit for capacity that can be requested.</p>
<p>Max must be less than or equal to the capacity value. Min and requestPolicy.default must be less than or equal to the maximum.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>min</code></p></td>
<td style="text-align: left;"><p><a href="../objects/index.xml#io-k8s-apimachinery-pkg-api-resource-Quantity"><code>Quantity</code></a></p></td>
<td style="text-align: left;"><p>Min specifies the minimum capacity allowed for a consumption request.</p>
<p>Min must be greater than or equal to zero, and less than or equal to the capacity value. requestPolicy.default must be more than or equal to the minimum.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>step</code></p></td>
<td style="text-align: left;"><p><a href="../objects/index.xml#io-k8s-apimachinery-pkg-api-resource-Quantity"><code>Quantity</code></a></p></td>
<td style="text-align: left;"><p>Step defines the step size between valid capacity amounts within the range.</p>
<p>Max (if set) and requestPolicy.default must be a multiple of Step. Min + Step must be less than or equal to the capacity value.</p></td>
</tr>
</tbody>
</table>

## .spec.devices\[\].consumesCounters

Description
ConsumesCounters defines a list of references to sharedCounters and the set of counters that the device will consume from those counter sets.

There can only be a single entry per counterSet.

The maximum number of device counter consumptions per device is 2.

Type
`array`

## .spec.devices\[\].consumesCounters\[\]

Description
DeviceCounterConsumption defines a set of counters that a device will consume from a CounterSet.

Type
`object`

Required
- `counterSet`

- `counters`

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
<td style="text-align: left;"><p><code>counterSet</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>CounterSet is the name of the set from which the counters defined will be consumed.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>counters</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>Counters defines the counters that will be consumed by the device.</p>
<p>The maximum number of counters is 32.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>counters{}</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>Counter describes a quantity associated with a device.</p></td>
</tr>
</tbody>
</table>

## .spec.devices\[\].consumesCounters\[\].counters

Description
Counters defines the counters that will be consumed by the device.

The maximum number of counters is 32.

Type
`object`

## .spec.devices\[\].consumesCounters\[\].counters{}

Description
Counter describes a quantity associated with a device.

Type
`object`

Required
- `value`

| Property | Type | Description |
|----|----|----|
| `value` | [`Quantity`](../objects/index.md#io-k8s-apimachinery-pkg-api-resource-Quantity) | Value defines how much of a certain device counter is available. |

## .spec.devices\[\].taints

Description
If specified, these are the driver-defined taints.

The maximum number of taints is 16. If taints are set for any device in a ResourceSlice, then the maximum number of allowed devices per ResourceSlice is 64 instead of 128.

This is an alpha field and requires enabling the DRADeviceTaints feature gate.

Type
`array`

## .spec.devices\[\].taints\[\]

Description
The device this taint is attached to has the "effect" on any claim which does not tolerate the taint and, through the claim, to pods using the claim.

Type
`object`

Required
- `key`

- `effect`

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
<td style="text-align: left;"><p><code>effect</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>The effect of the taint on claims that do not tolerate the taint and through such claims on the pods using them.</p>
<p>Valid effects are None, NoSchedule and NoExecute. PreferNoSchedule as used for nodes is not valid here. More effects may get added in the future. Consumers must treat unknown effects like None.</p>
<p>Possible enum values: - <code>"NoExecute"</code> Evict any already-running pods that do not tolerate the device taint. - <code>"NoSchedule"</code> Do not allow new pods to schedule which use a tainted device unless they tolerate the taint, but allow all pods submitted to Kubelet without going through the scheduler to start, and allow all already-running pods to continue running. - <code>"None"</code> No effect, the taint is purely informational.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>key</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>The taint key to be applied to a device. Must be a label name.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>timeAdded</code></p></td>
<td style="text-align: left;"><p><a href="../objects/index.xml#io-k8s-apimachinery-pkg-apis-meta-v1-Time"><code>Time</code></a></p></td>
<td style="text-align: left;"><p>TimeAdded represents the time at which the taint was added. Added automatically during create or update if not set.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>value</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>The taint value corresponding to the taint key. Must be a label value.</p></td>
</tr>
</tbody>
</table>

## .spec.pool

Description
ResourcePool describes the pool that ResourceSlices belong to.

Type
`object`

Required
- `name`

- `generation`

- `resourceSliceCount`

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
<td style="text-align: left;"><p><code>generation</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p>Generation tracks the change in a pool over time. Whenever a driver changes something about one or more of the resources in a pool, it must change the generation in all ResourceSlices which are part of that pool. Consumers of ResourceSlices should only consider resources from the pool with the highest generation number. The generation may be reset by drivers, which should be fine for consumers, assuming that all ResourceSlices in a pool are updated to match or deleted.</p>
<p>Combined with ResourceSliceCount, this mechanism enables consumers to detect pools which are comprised of multiple ResourceSlices and are in an incomplete state.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>name</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Name is used to identify the pool. For node-local devices, this is often the node name, but this is not required.</p>
<p>It must not be longer than 253 characters and must consist of one or more DNS sub-domains separated by slashes. This field is immutable.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>resourceSliceCount</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p>ResourceSliceCount is the total number of ResourceSlices in the pool at this generation number. Must be greater than zero.</p>
<p>Consumers can use this to check whether they have seen all ResourceSlices belonging to the same pool.</p></td>
</tr>
</tbody>
</table>

## .spec.sharedCounters

Description
SharedCounters defines a list of counter sets, each of which has a name and a list of counters available.

The names of the counter sets must be unique in the ResourcePool.

Only one of Devices and SharedCounters can be set in a ResourceSlice.

The maximum number of counter sets is 8.

Type
`array`

## .spec.sharedCounters\[\]

Description
CounterSet defines a named set of counters that are available to be used by devices defined in the ResourcePool.

The counters are not allocatable by themselves, but can be referenced by devices. When a device is allocated, the portion of counters it uses will no longer be available for use by other devices.

Type
`object`

Required
- `name`

- `counters`

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
<td style="text-align: left;"><p><code>counters</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>Counters defines the set of counters for this CounterSet The name of each counter must be unique in that set and must be a DNS label.</p>
<p>The maximum number of counters is 32.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>counters{}</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>Counter describes a quantity associated with a device.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>name</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Name defines the name of the counter set. It must be a DNS label.</p></td>
</tr>
</tbody>
</table>

## .spec.sharedCounters\[\].counters

Description
Counters defines the set of counters for this CounterSet The name of each counter must be unique in that set and must be a DNS label.

The maximum number of counters is 32.

Type
`object`

## .spec.sharedCounters\[\].counters{}

Description
Counter describes a quantity associated with a device.

Type
`object`

Required
- `value`

| Property | Type | Description |
|----|----|----|
| `value` | [`Quantity`](../objects/index.md#io-k8s-apimachinery-pkg-api-resource-Quantity) | Value defines how much of a certain device counter is available. |

# API endpoints

The following API endpoints are available:

- `/apis/resource.k8s.io/v1/resourceslices`

  - `DELETE`: delete collection of ResourceSlice

  - `GET`: list or watch objects of kind ResourceSlice

  - `POST`: create a ResourceSlice

- `/apis/resource.k8s.io/v1/watch/resourceslices`

  - `GET`: watch individual changes to a list of ResourceSlice. deprecated: use the 'watch' parameter with a list operation instead.

- `/apis/resource.k8s.io/v1/resourceslices/{name}`

  - `DELETE`: delete a ResourceSlice

  - `GET`: read the specified ResourceSlice

  - `PATCH`: partially update the specified ResourceSlice

  - `PUT`: replace the specified ResourceSlice

- `/apis/resource.k8s.io/v1/watch/resourceslices/{name}`

  - `GET`: watch changes to an object of kind ResourceSlice. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.

## /apis/resource.k8s.io/v1/resourceslices

HTTP method
`DELETE`

Description
delete collection of ResourceSlice

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
list or watch objects of kind ResourceSlice

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ResourceSliceList`](../objects/index.md#io-k8s-api-resource-v1-ResourceSliceList) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`POST`

Description
create a ResourceSlice

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`ResourceSlice`](resourceslice-resource-k8s-io-v1.md#resourceslice-resource-k8s-io-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ResourceSlice`](resourceslice-resource-k8s-io-v1.md#resourceslice-resource-k8s-io-v1) schema |
| 201 - Created | [`ResourceSlice`](resourceslice-resource-k8s-io-v1.md#resourceslice-resource-k8s-io-v1) schema |
| 202 - Accepted | [`ResourceSlice`](resourceslice-resource-k8s-io-v1.md#resourceslice-resource-k8s-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/resource.k8s.io/v1/watch/resourceslices

HTTP method
`GET`

Description
watch individual changes to a list of ResourceSlice. deprecated: use the 'watch' parameter with a list operation instead.

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`WatchEvent`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/resource.k8s.io/v1/resourceslices/{name}

| Parameter | Type     | Description               |
|-----------|----------|---------------------------|
| `name`    | `string` | name of the ResourceSlice |

Global path parameters

HTTP method
`DELETE`

Description
delete a ResourceSlice

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |

Query parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ResourceSlice`](resourceslice-resource-k8s-io-v1.md#resourceslice-resource-k8s-io-v1) schema |
| 202 - Accepted | [`ResourceSlice`](resourceslice-resource-k8s-io-v1.md#resourceslice-resource-k8s-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`GET`

Description
read the specified ResourceSlice

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ResourceSlice`](resourceslice-resource-k8s-io-v1.md#resourceslice-resource-k8s-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PATCH`

Description
partially update the specified ResourceSlice

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ResourceSlice`](resourceslice-resource-k8s-io-v1.md#resourceslice-resource-k8s-io-v1) schema |
| 201 - Created | [`ResourceSlice`](resourceslice-resource-k8s-io-v1.md#resourceslice-resource-k8s-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PUT`

Description
replace the specified ResourceSlice

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`ResourceSlice`](resourceslice-resource-k8s-io-v1.md#resourceslice-resource-k8s-io-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ResourceSlice`](resourceslice-resource-k8s-io-v1.md#resourceslice-resource-k8s-io-v1) schema |
| 201 - Created | [`ResourceSlice`](resourceslice-resource-k8s-io-v1.md#resourceslice-resource-k8s-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/resource.k8s.io/v1/watch/resourceslices/{name}

| Parameter | Type     | Description               |
|-----------|----------|---------------------------|
| `name`    | `string` | name of the ResourceSlice |

Global path parameters

HTTP method
`GET`

Description
watch changes to an object of kind ResourceSlice. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`WatchEvent`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema |
| 401 - Unauthorized | Empty |

HTTP responses
