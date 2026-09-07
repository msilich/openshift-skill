<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Description
ResourceClaim describes a request for access to resources in the cluster, for use by workloads. For example, if a workload needs an accelerator device with specific properties, this is how that request is expressed. The status stanza tracks whether this claim has been satisfied and what specific resources have been allocated.

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
| `spec` | `object` | ResourceClaimSpec defines what is being requested in a ResourceClaim and how to configure it. |
| `status` | `object` | ResourceClaimStatus tracks whether the resource has been allocated and what the result of that was. |

## .spec

Description
ResourceClaimSpec defines what is being requested in a ResourceClaim and how to configure it.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `devices` | `object` | DeviceClaim defines how to request devices with a ResourceClaim. |

## .spec.devices

Description
DeviceClaim defines how to request devices with a ResourceClaim.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `config` | `array` | This field holds configuration for multiple potential drivers which could satisfy requests in this claim. It is ignored while allocating the claim. |
| `config[]` | `object` | DeviceClaimConfiguration is used for configuration parameters in DeviceClaim. |
| `constraints` | `array` | These constraints must be satisfied by the set of devices that get allocated for the claim. |
| `constraints[]` | `object` | DeviceConstraint must have exactly one field set besides Requests. |
| `requests` | `array` | Requests represent individual requests for distinct devices which must all be satisfied. If empty, nothing needs to be allocated. |
| `requests[]` | `object` | DeviceRequest is a request for devices required for a claim. This is typically a request for a single resource like a device, but can also ask for several identical devices. With FirstAvailable it is also possible to provide a prioritized list of requests. |

## .spec.devices.config

Description
This field holds configuration for multiple potential drivers which could satisfy requests in this claim. It is ignored while allocating the claim.

Type
`array`

## .spec.devices.config\[\]

Description
DeviceClaimConfiguration is used for configuration parameters in DeviceClaim.

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
<td style="text-align: left;"><p><code>opaque</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>OpaqueDeviceConfiguration contains configuration parameters for a driver in a format defined by the driver vendor.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>requests</code></p></td>
<td style="text-align: left;"><p><code>array (string)</code></p></td>
<td style="text-align: left;"><p>Requests lists the names of requests where the configuration applies. If empty, it applies to all requests.</p>
<p>References to subrequests must include the name of the main request and may include the subrequest using the format &lt;main request&gt;[/&lt;subrequest&gt;]. If just the main request is given, the configuration applies to all subrequests.</p></td>
</tr>
</tbody>
</table>

## .spec.devices.config\[\].opaque

Description
OpaqueDeviceConfiguration contains configuration parameters for a driver in a format defined by the driver vendor.

Type
`object`

Required
- `driver`

- `parameters`

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
<td style="text-align: left;"><p><code>driver</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Driver is used to determine which kubelet plugin needs to be passed these configuration parameters.</p>
<p>An admission policy provided by the driver developer could use this to decide whether it needs to validate them.</p>
<p>Must be a DNS subdomain and should end with a DNS domain owned by the vendor of the driver. It should use only lower case characters.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>parameters</code></p></td>
<td style="text-align: left;"><p><a href="../objects/index.xml#io-k8s-apimachinery-pkg-runtime-RawExtension"><code>RawExtension</code></a></p></td>
<td style="text-align: left;"><p>Parameters can contain arbitrary data. It is the responsibility of the driver developer to handle validation and versioning. Typically this includes self-identification and a version ("kind" + "apiVersion" for Kubernetes types), with conversion between different versions.</p>
<p>The length of the raw data must be smaller or equal to 10 Ki.</p></td>
</tr>
</tbody>
</table>

## .spec.devices.constraints

Description
These constraints must be satisfied by the set of devices that get allocated for the claim.

Type
`array`

## .spec.devices.constraints\[\]

Description
DeviceConstraint must have exactly one field set besides Requests.

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
<td style="text-align: left;"><p><code>distinctAttribute</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>DistinctAttribute requires that all devices in question have this attribute and that its type and value are unique across those devices.</p>
<p>This acts as the inverse of MatchAttribute.</p>
<p>This constraint is used to avoid allocating multiple requests to the same device by ensuring attribute-level differentiation.</p>
<p>This is useful for scenarios where resource requests must be fulfilled by separate physical devices. For example, a container requests two network interfaces that must be allocated from two different physical NICs.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>matchAttribute</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>MatchAttribute requires that all devices in question have this attribute and that its type and value are the same across those devices.</p>
<p>For example, if you specified "dra.example.com/numa" (a hypothetical example!), then only devices in the same NUMA node will be chosen. A device which does not have that attribute will not be chosen. All devices should use a value of the same type for this attribute because that is part of its specification, but if one device doesn’t, then it also will not be chosen.</p>
<p>Must include the domain qualifier.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>requests</code></p></td>
<td style="text-align: left;"><p><code>array (string)</code></p></td>
<td style="text-align: left;"><p>Requests is a list of the one or more requests in this claim which must co-satisfy this constraint. If a request is fulfilled by multiple devices, then all of the devices must satisfy the constraint. If this is not specified, this constraint applies to all requests in this claim.</p>
<p>References to subrequests must include the name of the main request and may include the subrequest using the format &lt;main request&gt;[/&lt;subrequest&gt;]. If just the main request is given, the constraint applies to all subrequests.</p></td>
</tr>
</tbody>
</table>

## .spec.devices.requests

Description
Requests represent individual requests for distinct devices which must all be satisfied. If empty, nothing needs to be allocated.

Type
`array`

## .spec.devices.requests\[\]

Description
DeviceRequest is a request for devices required for a claim. This is typically a request for a single resource like a device, but can also ask for several identical devices. With FirstAvailable it is also possible to provide a prioritized list of requests.

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
<td style="text-align: left;"><p><code>exactly</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>ExactDeviceRequest is a request for one or more identical devices.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>firstAvailable</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>FirstAvailable contains subrequests, of which exactly one will be selected by the scheduler. It tries to satisfy them in the order in which they are listed here. So if there are two entries in the list, the scheduler will only check the second one if it determines that the first one can not be used.</p>
<p>DRA does not yet implement scoring, so the scheduler will select the first set of devices that satisfies all the requests in the claim. And if the requirements can be satisfied on more than one node, other scheduling features will determine which node is chosen. This means that the set of devices allocated to a claim might not be the optimal set available to the cluster. Scoring will be implemented later.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>firstAvailable[]</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>DeviceSubRequest describes a request for device provided in the claim.spec.devices.requests[].firstAvailable array. Each is typically a request for a single resource like a device, but can also ask for several identical devices.</p>
<p>DeviceSubRequest is similar to ExactDeviceRequest, but doesn’t expose the AdminAccess field as that one is only supported when requesting a specific device.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>name</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Name can be used to reference this request in a pod.spec.containers[].resources.claims entry and in a constraint of the claim.</p>
<p>References using the name in the DeviceRequest will uniquely identify a request when the Exactly field is set. When the FirstAvailable field is set, a reference to the name of the DeviceRequest will match whatever subrequest is chosen by the scheduler.</p>
<p>Must be a DNS label.</p></td>
</tr>
</tbody>
</table>

## .spec.devices.requests\[\].exactly

Description
ExactDeviceRequest is a request for one or more identical devices.

Type
`object`

Required
- `deviceClassName`

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
<td style="text-align: left;"><p><code>adminAccess</code></p></td>
<td style="text-align: left;"><p><code>boolean</code></p></td>
<td style="text-align: left;"><p>AdminAccess indicates that this is a claim for administrative access to the device(s). Claims with AdminAccess are expected to be used for monitoring or other management services for a device. They ignore all ordinary claims to the device with respect to access modes and any resource allocations.</p>
<p>This is an alpha field and requires enabling the DRAAdminAccess feature gate. Admin access is disabled if this field is unset or set to false, otherwise it is enabled.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>allocationMode</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>AllocationMode and its related fields define how devices are allocated to satisfy this request. Supported values are:</p>
<p>- ExactCount: This request is for a specific number of devices. This is the default. The exact number is provided in the count field.</p>
<p>- All: This request is for all of the matching devices in a pool. At least one device must exist on the node for the allocation to succeed. Allocation will fail if some devices are already allocated, unless adminAccess is requested.</p>
<p>If AllocationMode is not specified, the default mode is ExactCount. If the mode is ExactCount and count is not specified, the default count is one. Any other requests must specify this field.</p>
<p>More modes may get added in the future. Clients must refuse to handle requests with unknown modes.</p>
<p>Possible enum values: - <code>"All"</code> - <code>"ExactCount"</code></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>capacity</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>CapacityRequirements defines the capacity requirements for a specific device request.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>count</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p>Count is used only when the count mode is "ExactCount". Must be greater than zero. If AllocationMode is ExactCount and this field is not specified, the default is one.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>deviceClassName</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>DeviceClassName references a specific DeviceClass, which can define additional configuration and selectors to be inherited by this request.</p>
<p>A DeviceClassName is required.</p>
<p>Administrators may use this to restrict which devices may get requested by only installing classes with selectors for permitted devices. If users are free to request anything without restrictions, then administrators can create an empty DeviceClass for users to reference.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>selectors</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>Selectors define criteria which must be satisfied by a specific device in order for that device to be considered for this request. All selectors must be satisfied for a device to be considered.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>selectors[]</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>DeviceSelector must have exactly one field set.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>tolerations</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>If specified, the request’s tolerations.</p>
<p>Tolerations for NoSchedule are required to allocate a device which has a taint with that effect. The same applies to NoExecute.</p>
<p>In addition, should any of the allocated devices get tainted with NoExecute after allocation and that effect is not tolerated, then all pods consuming the ResourceClaim get deleted to evict them. The scheduler will not let new pods reserve the claim while it has these tainted devices. Once all pods are evicted, the claim will get deallocated.</p>
<p>The maximum number of tolerations is 16.</p>
<p>This is an alpha field and requires enabling the DRADeviceTaints feature gate.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>tolerations[]</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>The ResourceClaim this DeviceToleration is attached to tolerates any taint that matches the triple &lt;key,value,effect&gt; using the matching operator &lt;operator&gt;.</p></td>
</tr>
</tbody>
</table>

## .spec.devices.requests\[\].exactly.capacity

Description
CapacityRequirements defines the capacity requirements for a specific device request.

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
<td style="text-align: left;"><p><code>requests</code></p></td>
<td style="text-align: left;"><p><a href="../objects/index.xml#io-k8s-apimachinery-pkg-api-resource-Quantity"><code>object (Quantity)</code></a></p></td>
<td style="text-align: left;"><p>Requests represent individual device resource requests for distinct resources, all of which must be provided by the device.</p>
<p>This value is used as an additional filtering condition against the available capacity on the device. This is semantically equivalent to a CEL selector with <code>device.capacity[&lt;domain&gt;].&lt;name&gt;.compareTo(quantity(&lt;request quantity&gt;)) &gt;= 0</code>. For example, device.capacity['test-driver.cdi.k8s.io'].counters.compareTo(quantity('2')) &gt;= 0.</p>
<p>When a requestPolicy is defined, the requested amount is adjusted upward to the nearest valid value based on the policy. If the requested amount cannot be adjusted to a valid value—because it exceeds what the requestPolicy allows— the device is considered ineligible for allocation.</p>
<p>For any capacity that is not explicitly requested: - If no requestPolicy is set, the default consumed capacity is equal to the full device capacity (i.e., the whole device is claimed). - If a requestPolicy is set, the default consumed capacity is determined according to that policy.</p>
<p>If the device allows multiple allocation, the aggregated amount across all requests must not exceed the capacity value. The consumed capacity, which may be adjusted based on the requestPolicy if defined, is recorded in the resource claim’s status.devices[*].consumedCapacity field.</p></td>
</tr>
</tbody>
</table>

## .spec.devices.requests\[\].exactly.selectors

Description
Selectors define criteria which must be satisfied by a specific device in order for that device to be considered for this request. All selectors must be satisfied for a device to be considered.

Type
`array`

## .spec.devices.requests\[\].exactly.selectors\[\]

Description
DeviceSelector must have exactly one field set.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `cel` | `object` | CELDeviceSelector contains a CEL expression for selecting a device. |

## .spec.devices.requests\[\].exactly.selectors\[\].cel

Description
CELDeviceSelector contains a CEL expression for selecting a device.

Type
`object`

Required
- `expression`

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
<td style="text-align: left;"><p><code>expression</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Expression is a CEL expression which evaluates a single device. It must evaluate to true when the device under consideration satisfies the desired criteria, and false when it does not. Any other result is an error and causes allocation of devices to abort.</p>
<p>The expression’s input is an object named "device", which carries the following properties: - driver (string): the name of the driver which defines this device. - attributes (map[string]object): the device’s attributes, grouped by prefix (e.g. device.attributes["dra.example.com"] evaluates to an object with all of the attributes which were prefixed by "dra.example.com". - capacity (map[string]object): the device’s capacities, grouped by prefix. - allowMultipleAllocations (bool): the allowMultipleAllocations property of the device (v1.34+ with the DRAConsumableCapacity feature enabled).</p>
<p>Example: Consider a device with driver="dra.example.com", which exposes two attributes named "model" and "ext.example.com/family" and which exposes one capacity named "modules". This input to this expression would have the following fields:</p>
<p>device.driver device.attributes["dra.example.com"].model device.attributes["ext.example.com"].family device.capacity["dra.example.com"].modules</p>
<p>The device.driver field can be used to check for a specific driver, either as a high-level precondition (i.e. you only want to consider devices from this driver) or as part of a multi-clause expression that is meant to consider devices from different drivers.</p>
<p>The value type of each attribute is defined by the device definition, and users who write these expressions must consult the documentation for their specific drivers. The value type of each capacity is Quantity.</p>
<p>If an unknown prefix is used as a lookup in either device.attributes or device.capacity, an empty map will be returned. Any reference to an unknown field will cause an evaluation error and allocation to abort.</p>
<p>A robust expression should check for the existence of attributes before referencing them.</p>
<p>For ease of use, the cel.bind() function is enabled, and can be used to simplify expressions that access multiple attributes with the same domain. For example:</p>
<p>cel.bind(dra, device.attributes["dra.example.com"], dra.someBool &amp;&amp; dra.anotherBool)</p>
<p>The length of the expression must be smaller or equal to 10 Ki. The cost of evaluating it is also limited based on the estimated number of logical steps.</p></td>
</tr>
</tbody>
</table>

## .spec.devices.requests\[\].exactly.tolerations

Description
If specified, the request’s tolerations.

Tolerations for NoSchedule are required to allocate a device which has a taint with that effect. The same applies to NoExecute.

In addition, should any of the allocated devices get tainted with NoExecute after allocation and that effect is not tolerated, then all pods consuming the ResourceClaim get deleted to evict them. The scheduler will not let new pods reserve the claim while it has these tainted devices. Once all pods are evicted, the claim will get deallocated.

The maximum number of tolerations is 16.

This is an alpha field and requires enabling the DRADeviceTaints feature gate.

Type
`array`

## .spec.devices.requests\[\].exactly.tolerations\[\]

Description
The ResourceClaim this DeviceToleration is attached to tolerates any taint that matches the triple \<key,value,effect\> using the matching operator \<operator\>.

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
<td style="text-align: left;"><p><code>effect</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Effect indicates the taint effect to match. Empty means match all taint effects. When specified, allowed values are NoSchedule and NoExecute.</p>
<p>Possible enum values: - <code>"NoExecute"</code> Evict any already-running pods that do not tolerate the device taint. - <code>"NoSchedule"</code> Do not allow new pods to schedule which use a tainted device unless they tolerate the taint, but allow all pods submitted to Kubelet without going through the scheduler to start, and allow all already-running pods to continue running. - <code>"None"</code> No effect, the taint is purely informational.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>key</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Key is the taint key that the toleration applies to. Empty means match all taint keys. If the key is empty, operator must be Exists; this combination means to match all values and all keys. Must be a label name.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>operator</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Operator represents a key’s relationship to the value. Valid operators are Exists and Equal. Defaults to Equal. Exists is equivalent to wildcard for value, so that a ResourceClaim can tolerate all taints of a particular category.</p>
<p>Possible enum values: - <code>"Equal"</code> - <code>"Exists"</code></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>tolerationSeconds</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p>TolerationSeconds represents the period of time the toleration (which must be of effect NoExecute, otherwise this field is ignored) tolerates the taint. By default, it is not set, which means tolerate the taint forever (do not evict). Zero and negative values will be treated as 0 (evict immediately) by the system. If larger than zero, the time when the pod needs to be evicted is calculated as &lt;time when taint was adedd&gt; + &lt;toleration seconds&gt;.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>value</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Value is the taint value the toleration matches to. If the operator is Exists, the value must be empty, otherwise just a regular string. Must be a label value.</p></td>
</tr>
</tbody>
</table>

## .spec.devices.requests\[\].firstAvailable

Description
FirstAvailable contains subrequests, of which exactly one will be selected by the scheduler. It tries to satisfy them in the order in which they are listed here. So if there are two entries in the list, the scheduler will only check the second one if it determines that the first one can not be used.

DRA does not yet implement scoring, so the scheduler will select the first set of devices that satisfies all the requests in the claim. And if the requirements can be satisfied on more than one node, other scheduling features will determine which node is chosen. This means that the set of devices allocated to a claim might not be the optimal set available to the cluster. Scoring will be implemented later.

Type
`array`

## .spec.devices.requests\[\].firstAvailable\[\]

Description
DeviceSubRequest describes a request for device provided in the claim.spec.devices.requests\[\].firstAvailable array. Each is typically a request for a single resource like a device, but can also ask for several identical devices.

DeviceSubRequest is similar to ExactDeviceRequest, but doesn’t expose the AdminAccess field as that one is only supported when requesting a specific device.

Type
`object`

Required
- `name`

- `deviceClassName`

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
<td style="text-align: left;"><p><code>allocationMode</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>AllocationMode and its related fields define how devices are allocated to satisfy this subrequest. Supported values are:</p>
<p>- ExactCount: This request is for a specific number of devices. This is the default. The exact number is provided in the count field.</p>
<p>- All: This subrequest is for all of the matching devices in a pool. Allocation will fail if some devices are already allocated, unless adminAccess is requested.</p>
<p>If AllocationMode is not specified, the default mode is ExactCount. If the mode is ExactCount and count is not specified, the default count is one. Any other subrequests must specify this field.</p>
<p>More modes may get added in the future. Clients must refuse to handle requests with unknown modes.</p>
<p>Possible enum values: - <code>"All"</code> - <code>"ExactCount"</code></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>capacity</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>CapacityRequirements defines the capacity requirements for a specific device request.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>count</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p>Count is used only when the count mode is "ExactCount". Must be greater than zero. If AllocationMode is ExactCount and this field is not specified, the default is one.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>deviceClassName</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>DeviceClassName references a specific DeviceClass, which can define additional configuration and selectors to be inherited by this subrequest.</p>
<p>A class is required. Which classes are available depends on the cluster.</p>
<p>Administrators may use this to restrict which devices may get requested by only installing classes with selectors for permitted devices. If users are free to request anything without restrictions, then administrators can create an empty DeviceClass for users to reference.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>name</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Name can be used to reference this subrequest in the list of constraints or the list of configurations for the claim. References must use the format &lt;main request&gt;/&lt;subrequest&gt;.</p>
<p>Must be a DNS label.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>selectors</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>Selectors define criteria which must be satisfied by a specific device in order for that device to be considered for this subrequest. All selectors must be satisfied for a device to be considered.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>selectors[]</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>DeviceSelector must have exactly one field set.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>tolerations</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>If specified, the request’s tolerations.</p>
<p>Tolerations for NoSchedule are required to allocate a device which has a taint with that effect. The same applies to NoExecute.</p>
<p>In addition, should any of the allocated devices get tainted with NoExecute after allocation and that effect is not tolerated, then all pods consuming the ResourceClaim get deleted to evict them. The scheduler will not let new pods reserve the claim while it has these tainted devices. Once all pods are evicted, the claim will get deallocated.</p>
<p>The maximum number of tolerations is 16.</p>
<p>This is an alpha field and requires enabling the DRADeviceTaints feature gate.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>tolerations[]</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>The ResourceClaim this DeviceToleration is attached to tolerates any taint that matches the triple &lt;key,value,effect&gt; using the matching operator &lt;operator&gt;.</p></td>
</tr>
</tbody>
</table>

## .spec.devices.requests\[\].firstAvailable\[\].capacity

Description
CapacityRequirements defines the capacity requirements for a specific device request.

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
<td style="text-align: left;"><p><code>requests</code></p></td>
<td style="text-align: left;"><p><a href="../objects/index.xml#io-k8s-apimachinery-pkg-api-resource-Quantity"><code>object (Quantity)</code></a></p></td>
<td style="text-align: left;"><p>Requests represent individual device resource requests for distinct resources, all of which must be provided by the device.</p>
<p>This value is used as an additional filtering condition against the available capacity on the device. This is semantically equivalent to a CEL selector with <code>device.capacity[&lt;domain&gt;].&lt;name&gt;.compareTo(quantity(&lt;request quantity&gt;)) &gt;= 0</code>. For example, device.capacity['test-driver.cdi.k8s.io'].counters.compareTo(quantity('2')) &gt;= 0.</p>
<p>When a requestPolicy is defined, the requested amount is adjusted upward to the nearest valid value based on the policy. If the requested amount cannot be adjusted to a valid value—because it exceeds what the requestPolicy allows— the device is considered ineligible for allocation.</p>
<p>For any capacity that is not explicitly requested: - If no requestPolicy is set, the default consumed capacity is equal to the full device capacity (i.e., the whole device is claimed). - If a requestPolicy is set, the default consumed capacity is determined according to that policy.</p>
<p>If the device allows multiple allocation, the aggregated amount across all requests must not exceed the capacity value. The consumed capacity, which may be adjusted based on the requestPolicy if defined, is recorded in the resource claim’s status.devices[*].consumedCapacity field.</p></td>
</tr>
</tbody>
</table>

## .spec.devices.requests\[\].firstAvailable\[\].selectors

Description
Selectors define criteria which must be satisfied by a specific device in order for that device to be considered for this subrequest. All selectors must be satisfied for a device to be considered.

Type
`array`

## .spec.devices.requests\[\].firstAvailable\[\].selectors\[\]

Description
DeviceSelector must have exactly one field set.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `cel` | `object` | CELDeviceSelector contains a CEL expression for selecting a device. |

## .spec.devices.requests\[\].firstAvailable\[\].selectors\[\].cel

Description
CELDeviceSelector contains a CEL expression for selecting a device.

Type
`object`

Required
- `expression`

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
<td style="text-align: left;"><p><code>expression</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Expression is a CEL expression which evaluates a single device. It must evaluate to true when the device under consideration satisfies the desired criteria, and false when it does not. Any other result is an error and causes allocation of devices to abort.</p>
<p>The expression’s input is an object named "device", which carries the following properties: - driver (string): the name of the driver which defines this device. - attributes (map[string]object): the device’s attributes, grouped by prefix (e.g. device.attributes["dra.example.com"] evaluates to an object with all of the attributes which were prefixed by "dra.example.com". - capacity (map[string]object): the device’s capacities, grouped by prefix. - allowMultipleAllocations (bool): the allowMultipleAllocations property of the device (v1.34+ with the DRAConsumableCapacity feature enabled).</p>
<p>Example: Consider a device with driver="dra.example.com", which exposes two attributes named "model" and "ext.example.com/family" and which exposes one capacity named "modules". This input to this expression would have the following fields:</p>
<p>device.driver device.attributes["dra.example.com"].model device.attributes["ext.example.com"].family device.capacity["dra.example.com"].modules</p>
<p>The device.driver field can be used to check for a specific driver, either as a high-level precondition (i.e. you only want to consider devices from this driver) or as part of a multi-clause expression that is meant to consider devices from different drivers.</p>
<p>The value type of each attribute is defined by the device definition, and users who write these expressions must consult the documentation for their specific drivers. The value type of each capacity is Quantity.</p>
<p>If an unknown prefix is used as a lookup in either device.attributes or device.capacity, an empty map will be returned. Any reference to an unknown field will cause an evaluation error and allocation to abort.</p>
<p>A robust expression should check for the existence of attributes before referencing them.</p>
<p>For ease of use, the cel.bind() function is enabled, and can be used to simplify expressions that access multiple attributes with the same domain. For example:</p>
<p>cel.bind(dra, device.attributes["dra.example.com"], dra.someBool &amp;&amp; dra.anotherBool)</p>
<p>The length of the expression must be smaller or equal to 10 Ki. The cost of evaluating it is also limited based on the estimated number of logical steps.</p></td>
</tr>
</tbody>
</table>

## .spec.devices.requests\[\].firstAvailable\[\].tolerations

Description
If specified, the request’s tolerations.

Tolerations for NoSchedule are required to allocate a device which has a taint with that effect. The same applies to NoExecute.

In addition, should any of the allocated devices get tainted with NoExecute after allocation and that effect is not tolerated, then all pods consuming the ResourceClaim get deleted to evict them. The scheduler will not let new pods reserve the claim while it has these tainted devices. Once all pods are evicted, the claim will get deallocated.

The maximum number of tolerations is 16.

This is an alpha field and requires enabling the DRADeviceTaints feature gate.

Type
`array`

## .spec.devices.requests\[\].firstAvailable\[\].tolerations\[\]

Description
The ResourceClaim this DeviceToleration is attached to tolerates any taint that matches the triple \<key,value,effect\> using the matching operator \<operator\>.

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
<td style="text-align: left;"><p><code>effect</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Effect indicates the taint effect to match. Empty means match all taint effects. When specified, allowed values are NoSchedule and NoExecute.</p>
<p>Possible enum values: - <code>"NoExecute"</code> Evict any already-running pods that do not tolerate the device taint. - <code>"NoSchedule"</code> Do not allow new pods to schedule which use a tainted device unless they tolerate the taint, but allow all pods submitted to Kubelet without going through the scheduler to start, and allow all already-running pods to continue running. - <code>"None"</code> No effect, the taint is purely informational.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>key</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Key is the taint key that the toleration applies to. Empty means match all taint keys. If the key is empty, operator must be Exists; this combination means to match all values and all keys. Must be a label name.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>operator</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Operator represents a key’s relationship to the value. Valid operators are Exists and Equal. Defaults to Equal. Exists is equivalent to wildcard for value, so that a ResourceClaim can tolerate all taints of a particular category.</p>
<p>Possible enum values: - <code>"Equal"</code> - <code>"Exists"</code></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>tolerationSeconds</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p>TolerationSeconds represents the period of time the toleration (which must be of effect NoExecute, otherwise this field is ignored) tolerates the taint. By default, it is not set, which means tolerate the taint forever (do not evict). Zero and negative values will be treated as 0 (evict immediately) by the system. If larger than zero, the time when the pod needs to be evicted is calculated as &lt;time when taint was adedd&gt; + &lt;toleration seconds&gt;.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>value</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Value is the taint value the toleration matches to. If the operator is Exists, the value must be empty, otherwise just a regular string. Must be a label value.</p></td>
</tr>
</tbody>
</table>

## .status

Description
ResourceClaimStatus tracks whether the resource has been allocated and what the result of that was.

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
<td style="text-align: left;"><p><code>allocation</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>AllocationResult contains attributes of an allocated resource.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>devices</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>Devices contains the status of each device allocated for this claim, as reported by the driver. This can include driver-specific information. Entries are owned by their respective drivers.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>devices[]</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>AllocatedDeviceStatus contains the status of an allocated device, if the driver chooses to report it. This may include driver-specific information.</p>
<p>The combination of Driver, Pool, Device, and ShareID must match the corresponding key in Status.Allocation.Devices.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>reservedFor</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>ReservedFor indicates which entities are currently allowed to use the claim. A Pod which references a ResourceClaim which is not reserved for that Pod will not be started. A claim that is in use or might be in use because it has been reserved must not get deallocated.</p>
<p>In a cluster with multiple scheduler instances, two pods might get scheduled concurrently by different schedulers. When they reference the same ResourceClaim which already has reached its maximum number of consumers, only one pod can be scheduled.</p>
<p>Both schedulers try to add their pod to the claim.status.reservedFor field, but only the update that reaches the API server first gets stored. The other one fails with an error and the scheduler which issued it knows that it must put the pod back into the queue, waiting for the ResourceClaim to become usable again.</p>
<p>There can be at most 256 such reservations. This may get increased in the future, but not reduced.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>reservedFor[]</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>ResourceClaimConsumerReference contains enough information to let you locate the consumer of a ResourceClaim. The user must be a resource in the same namespace as the ResourceClaim.</p></td>
</tr>
</tbody>
</table>

## .status.allocation

Description
AllocationResult contains attributes of an allocated resource.

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
<td style="text-align: left;"><p><code>allocationTimestamp</code></p></td>
<td style="text-align: left;"><p><a href="../objects/index.xml#io-k8s-apimachinery-pkg-apis-meta-v1-Time"><code>Time</code></a></p></td>
<td style="text-align: left;"><p>AllocationTimestamp stores the time when the resources were allocated. This field is not guaranteed to be set, in which case that time is unknown.</p>
<p>This is an alpha field and requires enabling the DRADeviceBindingConditions and DRAResourceClaimDeviceStatus feature gate.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>devices</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>DeviceAllocationResult is the result of allocating devices.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>nodeSelector</code></p></td>
<td style="text-align: left;"><p><a href="../objects/index.xml#io-k8s-api-core-v1-NodeSelector"><code>NodeSelector</code></a></p></td>
<td style="text-align: left;"><p>NodeSelector defines where the allocated resources are available. If unset, they are available everywhere.</p></td>
</tr>
</tbody>
</table>

## .status.allocation.devices

Description
DeviceAllocationResult is the result of allocating devices.

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
<td style="text-align: left;"><p><code>config</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>This field is a combination of all the claim and class configuration parameters. Drivers can distinguish between those based on a flag.</p>
<p>This includes configuration parameters for drivers which have no allocated devices in the result because it is up to the drivers which configuration parameters they support. They can silently ignore unknown configuration parameters.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>config[]</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>DeviceAllocationConfiguration gets embedded in an AllocationResult.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>results</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>Results lists all allocated devices.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>results[]</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>DeviceRequestAllocationResult contains the allocation result for one request.</p></td>
</tr>
</tbody>
</table>

## .status.allocation.devices.config

Description
This field is a combination of all the claim and class configuration parameters. Drivers can distinguish between those based on a flag.

This includes configuration parameters for drivers which have no allocated devices in the result because it is up to the drivers which configuration parameters they support. They can silently ignore unknown configuration parameters.

Type
`array`

## .status.allocation.devices.config\[\]

Description
DeviceAllocationConfiguration gets embedded in an AllocationResult.

Type
`object`

Required
- `source`

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
<td style="text-align: left;"><p><code>opaque</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>OpaqueDeviceConfiguration contains configuration parameters for a driver in a format defined by the driver vendor.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>requests</code></p></td>
<td style="text-align: left;"><p><code>array (string)</code></p></td>
<td style="text-align: left;"><p>Requests lists the names of requests where the configuration applies. If empty, its applies to all requests.</p>
<p>References to subrequests must include the name of the main request and may include the subrequest using the format &lt;main request&gt;[/&lt;subrequest&gt;]. If just the main request is given, the configuration applies to all subrequests.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>source</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Source records whether the configuration comes from a class and thus is not something that a normal user would have been able to set or from a claim.</p>
<p>Possible enum values: - <code>"FromClaim"</code> - <code>"FromClass"</code></p></td>
</tr>
</tbody>
</table>

## .status.allocation.devices.config\[\].opaque

Description
OpaqueDeviceConfiguration contains configuration parameters for a driver in a format defined by the driver vendor.

Type
`object`

Required
- `driver`

- `parameters`

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
<td style="text-align: left;"><p><code>driver</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Driver is used to determine which kubelet plugin needs to be passed these configuration parameters.</p>
<p>An admission policy provided by the driver developer could use this to decide whether it needs to validate them.</p>
<p>Must be a DNS subdomain and should end with a DNS domain owned by the vendor of the driver. It should use only lower case characters.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>parameters</code></p></td>
<td style="text-align: left;"><p><a href="../objects/index.xml#io-k8s-apimachinery-pkg-runtime-RawExtension"><code>RawExtension</code></a></p></td>
<td style="text-align: left;"><p>Parameters can contain arbitrary data. It is the responsibility of the driver developer to handle validation and versioning. Typically this includes self-identification and a version ("kind" + "apiVersion" for Kubernetes types), with conversion between different versions.</p>
<p>The length of the raw data must be smaller or equal to 10 Ki.</p></td>
</tr>
</tbody>
</table>

## .status.allocation.devices.results

Description
Results lists all allocated devices.

Type
`array`

## .status.allocation.devices.results\[\]

Description
DeviceRequestAllocationResult contains the allocation result for one request.

Type
`object`

Required
- `request`

- `driver`

- `pool`

- `device`

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
<td style="text-align: left;"><p><code>adminAccess</code></p></td>
<td style="text-align: left;"><p><code>boolean</code></p></td>
<td style="text-align: left;"><p>AdminAccess indicates that this device was allocated for administrative access. See the corresponding request field for a definition of mode.</p>
<p>This is an alpha field and requires enabling the DRAAdminAccess feature gate. Admin access is disabled if this field is unset or set to false, otherwise it is enabled.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>bindingConditions</code></p></td>
<td style="text-align: left;"><p><code>array (string)</code></p></td>
<td style="text-align: left;"><p>BindingConditions contains a copy of the BindingConditions from the corresponding ResourceSlice at the time of allocation.</p>
<p>This is an alpha field and requires enabling the DRADeviceBindingConditions and DRAResourceClaimDeviceStatus feature gates.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>bindingFailureConditions</code></p></td>
<td style="text-align: left;"><p><code>array (string)</code></p></td>
<td style="text-align: left;"><p>BindingFailureConditions contains a copy of the BindingFailureConditions from the corresponding ResourceSlice at the time of allocation.</p>
<p>This is an alpha field and requires enabling the DRADeviceBindingConditions and DRAResourceClaimDeviceStatus feature gates.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>consumedCapacity</code></p></td>
<td style="text-align: left;"><p><a href="../objects/index.xml#io-k8s-apimachinery-pkg-api-resource-Quantity"><code>object (Quantity)</code></a></p></td>
<td style="text-align: left;"><p>ConsumedCapacity tracks the amount of capacity consumed per device as part of the claim request. The consumed amount may differ from the requested amount: it is rounded up to the nearest valid value based on the device’s requestPolicy if applicable (i.e., may not be less than the requested amount).</p>
<p>The total consumed capacity for each device must not exceed the DeviceCapacity’s Value.</p>
<p>This field is populated only for devices that allow multiple allocations. All capacity entries are included, even if the consumed amount is zero.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>device</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Device references one device instance via its name in the driver’s resource pool. It must be a DNS label.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>driver</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Driver specifies the name of the DRA driver whose kubelet plugin should be invoked to process the allocation once the claim is needed on a node.</p>
<p>Must be a DNS subdomain and should end with a DNS domain owned by the vendor of the driver. It should use only lower case characters.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>pool</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>This name together with the driver name and the device name field identify which device was allocated (<code>&lt;driver name&gt;/&lt;pool name&gt;/&lt;device name&gt;</code>).</p>
<p>Must not be longer than 253 characters and may contain one or more DNS sub-domains separated by slashes.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>request</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Request is the name of the request in the claim which caused this device to be allocated. If it references a subrequest in the firstAvailable list on a DeviceRequest, this field must include both the name of the main request and the subrequest using the format &lt;main request&gt;/&lt;subrequest&gt;.</p>
<p>Multiple devices may have been allocated per request.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>shareID</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>ShareID uniquely identifies an individual allocation share of the device, used when the device supports multiple simultaneous allocations. It serves as an additional map key to differentiate concurrent shares of the same device.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>tolerations</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>A copy of all tolerations specified in the request at the time when the device got allocated.</p>
<p>The maximum number of tolerations is 16.</p>
<p>This is an alpha field and requires enabling the DRADeviceTaints feature gate.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>tolerations[]</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>The ResourceClaim this DeviceToleration is attached to tolerates any taint that matches the triple &lt;key,value,effect&gt; using the matching operator &lt;operator&gt;.</p></td>
</tr>
</tbody>
</table>

## .status.allocation.devices.results\[\].tolerations

Description
A copy of all tolerations specified in the request at the time when the device got allocated.

The maximum number of tolerations is 16.

This is an alpha field and requires enabling the DRADeviceTaints feature gate.

Type
`array`

## .status.allocation.devices.results\[\].tolerations\[\]

Description
The ResourceClaim this DeviceToleration is attached to tolerates any taint that matches the triple \<key,value,effect\> using the matching operator \<operator\>.

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
<td style="text-align: left;"><p><code>effect</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Effect indicates the taint effect to match. Empty means match all taint effects. When specified, allowed values are NoSchedule and NoExecute.</p>
<p>Possible enum values: - <code>"NoExecute"</code> Evict any already-running pods that do not tolerate the device taint. - <code>"NoSchedule"</code> Do not allow new pods to schedule which use a tainted device unless they tolerate the taint, but allow all pods submitted to Kubelet without going through the scheduler to start, and allow all already-running pods to continue running. - <code>"None"</code> No effect, the taint is purely informational.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>key</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Key is the taint key that the toleration applies to. Empty means match all taint keys. If the key is empty, operator must be Exists; this combination means to match all values and all keys. Must be a label name.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>operator</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Operator represents a key’s relationship to the value. Valid operators are Exists and Equal. Defaults to Equal. Exists is equivalent to wildcard for value, so that a ResourceClaim can tolerate all taints of a particular category.</p>
<p>Possible enum values: - <code>"Equal"</code> - <code>"Exists"</code></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>tolerationSeconds</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p>TolerationSeconds represents the period of time the toleration (which must be of effect NoExecute, otherwise this field is ignored) tolerates the taint. By default, it is not set, which means tolerate the taint forever (do not evict). Zero and negative values will be treated as 0 (evict immediately) by the system. If larger than zero, the time when the pod needs to be evicted is calculated as &lt;time when taint was adedd&gt; + &lt;toleration seconds&gt;.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>value</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Value is the taint value the toleration matches to. If the operator is Exists, the value must be empty, otherwise just a regular string. Must be a label value.</p></td>
</tr>
</tbody>
</table>

## .status.devices

Description
Devices contains the status of each device allocated for this claim, as reported by the driver. This can include driver-specific information. Entries are owned by their respective drivers.

Type
`array`

## .status.devices\[\]

Description
AllocatedDeviceStatus contains the status of an allocated device, if the driver chooses to report it. This may include driver-specific information.

The combination of Driver, Pool, Device, and ShareID must match the corresponding key in Status.Allocation.Devices.

Type
`object`

Required
- `driver`

- `pool`

- `device`

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
<td style="text-align: left;"><p><a href="../objects/index.xml#io-k8s-apimachinery-pkg-apis-meta-v1-Condition"><code>array (Condition)</code></a></p></td>
<td style="text-align: left;"><p>Conditions contains the latest observation of the device’s state. If the device has been configured according to the class and claim config references, the <code>Ready</code> condition should be True.</p>
<p>Must not contain more than 8 entries.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>data</code></p></td>
<td style="text-align: left;"><p><a href="../objects/index.xml#io-k8s-apimachinery-pkg-runtime-RawExtension"><code>RawExtension</code></a></p></td>
<td style="text-align: left;"><p>Data contains arbitrary driver-specific data.</p>
<p>The length of the raw data must be smaller or equal to 10 Ki.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>device</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Device references one device instance via its name in the driver’s resource pool. It must be a DNS label.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>driver</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Driver specifies the name of the DRA driver whose kubelet plugin should be invoked to process the allocation once the claim is needed on a node.</p>
<p>Must be a DNS subdomain and should end with a DNS domain owned by the vendor of the driver. It should use only lower case characters.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>networkData</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>NetworkDeviceData provides network-related details for the allocated device. This information may be filled by drivers or other components to configure or identify the device within a network context.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>pool</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>This name together with the driver name and the device name field identify which device was allocated (<code>&lt;driver name&gt;/&lt;pool name&gt;/&lt;device name&gt;</code>).</p>
<p>Must not be longer than 253 characters and may contain one or more DNS sub-domains separated by slashes.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>shareID</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>ShareID uniquely identifies an individual allocation share of the device.</p></td>
</tr>
</tbody>
</table>

## .status.devices\[\].networkData

Description
NetworkDeviceData provides network-related details for the allocated device. This information may be filled by drivers or other components to configure or identify the device within a network context.

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
<td style="text-align: left;"><p><code>hardwareAddress</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>HardwareAddress represents the hardware address (e.g. MAC Address) of the device’s network interface.</p>
<p>Must not be longer than 128 characters.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>interfaceName</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>InterfaceName specifies the name of the network interface associated with the allocated device. This might be the name of a physical or virtual network interface being configured in the pod.</p>
<p>Must not be longer than 256 characters.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>ips</code></p></td>
<td style="text-align: left;"><p><code>array (string)</code></p></td>
<td style="text-align: left;"><p>IPs lists the network addresses assigned to the device’s network interface. This can include both IPv4 and IPv6 addresses. The IPs are in the CIDR notation, which includes both the address and the associated subnet mask. e.g.: "192.0.2.5/24" for IPv4 and "2001:db8::5/64" for IPv6.</p></td>
</tr>
</tbody>
</table>

## .status.reservedFor

Description
ReservedFor indicates which entities are currently allowed to use the claim. A Pod which references a ResourceClaim which is not reserved for that Pod will not be started. A claim that is in use or might be in use because it has been reserved must not get deallocated.

In a cluster with multiple scheduler instances, two pods might get scheduled concurrently by different schedulers. When they reference the same ResourceClaim which already has reached its maximum number of consumers, only one pod can be scheduled.

Both schedulers try to add their pod to the claim.status.reservedFor field, but only the update that reaches the API server first gets stored. The other one fails with an error and the scheduler which issued it knows that it must put the pod back into the queue, waiting for the ResourceClaim to become usable again.

There can be at most 256 such reservations. This may get increased in the future, but not reduced.

Type
`array`

## .status.reservedFor\[\]

Description
ResourceClaimConsumerReference contains enough information to let you locate the consumer of a ResourceClaim. The user must be a resource in the same namespace as the ResourceClaim.

Type
`object`

Required
- `resource`

- `name`

- `uid`

| Property | Type | Description |
|----|----|----|
| `apiGroup` | `string` | APIGroup is the group for the resource being referenced. It is empty for the core API. This matches the group in the APIVersion that is used when creating the resources. |
| `name` | `string` | Name is the name of resource being referenced. |
| `resource` | `string` | Resource is the type of resource being referenced, for example "pods". |
| `uid` | `string` | UID identifies exactly one incarnation of the resource. |

# API endpoints

The following API endpoints are available:

- `/apis/resource.k8s.io/v1/resourceclaims`

  - `GET`: list or watch objects of kind ResourceClaim

- `/apis/resource.k8s.io/v1/watch/resourceclaims`

  - `GET`: watch individual changes to a list of ResourceClaim. deprecated: use the 'watch' parameter with a list operation instead.

- `/apis/resource.k8s.io/v1/namespaces/{namespace}/resourceclaims`

  - `DELETE`: delete collection of ResourceClaim

  - `GET`: list or watch objects of kind ResourceClaim

  - `POST`: create a ResourceClaim

- `/apis/resource.k8s.io/v1/watch/namespaces/{namespace}/resourceclaims`

  - `GET`: watch individual changes to a list of ResourceClaim. deprecated: use the 'watch' parameter with a list operation instead.

- `/apis/resource.k8s.io/v1/namespaces/{namespace}/resourceclaims/{name}`

  - `DELETE`: delete a ResourceClaim

  - `GET`: read the specified ResourceClaim

  - `PATCH`: partially update the specified ResourceClaim

  - `PUT`: replace the specified ResourceClaim

- `/apis/resource.k8s.io/v1/watch/namespaces/{namespace}/resourceclaims/{name}`

  - `GET`: watch changes to an object of kind ResourceClaim. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.

- `/apis/resource.k8s.io/v1/namespaces/{namespace}/resourceclaims/{name}/status`

  - `GET`: read status of the specified ResourceClaim

  - `PATCH`: partially update status of the specified ResourceClaim

  - `PUT`: replace status of the specified ResourceClaim

## /apis/resource.k8s.io/v1/resourceclaims

HTTP method
`GET`

Description
list or watch objects of kind ResourceClaim

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ResourceClaimList`](../objects/index.md#io-k8s-api-resource-v1-ResourceClaimList) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/resource.k8s.io/v1/watch/resourceclaims

HTTP method
`GET`

Description
watch individual changes to a list of ResourceClaim. deprecated: use the 'watch' parameter with a list operation instead.

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`WatchEvent`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/resource.k8s.io/v1/namespaces/{namespace}/resourceclaims

HTTP method
`DELETE`

Description
delete collection of ResourceClaim

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
list or watch objects of kind ResourceClaim

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ResourceClaimList`](../objects/index.md#io-k8s-api-resource-v1-ResourceClaimList) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`POST`

Description
create a ResourceClaim

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`ResourceClaim`](resourceclaim-resource-k8s-io-v1.md#resourceclaim-resource-k8s-io-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ResourceClaim`](resourceclaim-resource-k8s-io-v1.md#resourceclaim-resource-k8s-io-v1) schema |
| 201 - Created | [`ResourceClaim`](resourceclaim-resource-k8s-io-v1.md#resourceclaim-resource-k8s-io-v1) schema |
| 202 - Accepted | [`ResourceClaim`](resourceclaim-resource-k8s-io-v1.md#resourceclaim-resource-k8s-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/resource.k8s.io/v1/watch/namespaces/{namespace}/resourceclaims

HTTP method
`GET`

Description
watch individual changes to a list of ResourceClaim. deprecated: use the 'watch' parameter with a list operation instead.

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`WatchEvent`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/resource.k8s.io/v1/namespaces/{namespace}/resourceclaims/{name}

| Parameter | Type     | Description               |
|-----------|----------|---------------------------|
| `name`    | `string` | name of the ResourceClaim |

Global path parameters

HTTP method
`DELETE`

Description
delete a ResourceClaim

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |

Query parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ResourceClaim`](resourceclaim-resource-k8s-io-v1.md#resourceclaim-resource-k8s-io-v1) schema |
| 202 - Accepted | [`ResourceClaim`](resourceclaim-resource-k8s-io-v1.md#resourceclaim-resource-k8s-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`GET`

Description
read the specified ResourceClaim

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ResourceClaim`](resourceclaim-resource-k8s-io-v1.md#resourceclaim-resource-k8s-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PATCH`

Description
partially update the specified ResourceClaim

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ResourceClaim`](resourceclaim-resource-k8s-io-v1.md#resourceclaim-resource-k8s-io-v1) schema |
| 201 - Created | [`ResourceClaim`](resourceclaim-resource-k8s-io-v1.md#resourceclaim-resource-k8s-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PUT`

Description
replace the specified ResourceClaim

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`ResourceClaim`](resourceclaim-resource-k8s-io-v1.md#resourceclaim-resource-k8s-io-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ResourceClaim`](resourceclaim-resource-k8s-io-v1.md#resourceclaim-resource-k8s-io-v1) schema |
| 201 - Created | [`ResourceClaim`](resourceclaim-resource-k8s-io-v1.md#resourceclaim-resource-k8s-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/resource.k8s.io/v1/watch/namespaces/{namespace}/resourceclaims/{name}

| Parameter | Type     | Description               |
|-----------|----------|---------------------------|
| `name`    | `string` | name of the ResourceClaim |

Global path parameters

HTTP method
`GET`

Description
watch changes to an object of kind ResourceClaim. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`WatchEvent`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/resource.k8s.io/v1/namespaces/{namespace}/resourceclaims/{name}/status

| Parameter | Type     | Description               |
|-----------|----------|---------------------------|
| `name`    | `string` | name of the ResourceClaim |

Global path parameters

HTTP method
`GET`

Description
read status of the specified ResourceClaim

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ResourceClaim`](resourceclaim-resource-k8s-io-v1.md#resourceclaim-resource-k8s-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PATCH`

Description
partially update status of the specified ResourceClaim

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ResourceClaim`](resourceclaim-resource-k8s-io-v1.md#resourceclaim-resource-k8s-io-v1) schema |
| 201 - Created | [`ResourceClaim`](resourceclaim-resource-k8s-io-v1.md#resourceclaim-resource-k8s-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PUT`

Description
replace status of the specified ResourceClaim

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`ResourceClaim`](resourceclaim-resource-k8s-io-v1.md#resourceclaim-resource-k8s-io-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ResourceClaim`](resourceclaim-resource-k8s-io-v1.md#resourceclaim-resource-k8s-io-v1) schema |
| 201 - Created | [`ResourceClaim`](resourceclaim-resource-k8s-io-v1.md#resourceclaim-resource-k8s-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses
