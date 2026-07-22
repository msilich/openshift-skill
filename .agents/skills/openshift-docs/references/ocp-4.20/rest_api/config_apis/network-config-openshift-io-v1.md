<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Description
Network holds cluster-wide information about Network. The canonical name is `cluster`. It is used to configure the desired network configuration, such as: IP address pools for services/pod IPs, network plugin, etc. Please view network.spec for an explanation on what applies when configuring this resource.

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
| `spec` | `object` | spec holds user settable values for configuration. As a general rule, this SHOULD NOT be read directly. Instead, you should consume the NetworkStatus, as it indicates the currently deployed configuration. Currently, most spec fields are immutable after installation. Please view the individual ones for further details on each. |
| `status` | `object` | status holds observed values from the cluster. They may not be overridden. |

## .spec

Description
spec holds user settable values for configuration. As a general rule, this SHOULD NOT be read directly. Instead, you should consume the NetworkStatus, as it indicates the currently deployed configuration. Currently, most spec fields are immutable after installation. Please view the individual ones for further details on each.

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
<td style="text-align: left;"><p><code>clusterNetwork</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>IP address pool to use for pod IPs. This field is immutable after installation.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>clusterNetwork[]</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>ClusterNetworkEntry is a contiguous block of IP addresses from which pod IPs are allocated.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>externalIP</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>externalIP defines configuration for controllers that affect Service.ExternalIP. If nil, then ExternalIP is not allowed to be set.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>networkDiagnostics</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>networkDiagnostics defines network diagnostics configuration.</p>
<p>Takes precedence over spec.disableNetworkDiagnostics in network.operator.openshift.io. If networkDiagnostics is not specified or is empty, and the spec.disableNetworkDiagnostics flag in network.operator.openshift.io is set to true, the network diagnostics feature will be disabled.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>networkType</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>networkType is the plugin that is to be deployed (e.g. OVNKubernetes). This should match a value that the cluster-network-operator understands, or else no networking will be installed. Currently supported values are: - OVNKubernetes This field is immutable after installation.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>serviceNetwork</code></p></td>
<td style="text-align: left;"><p><code>array (string)</code></p></td>
<td style="text-align: left;"><p>IP address pool for services. Currently, we only support a single entry here. This field is immutable after installation.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>serviceNodePortRange</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>The port range allowed for Services of type NodePort. If not specified, the default of 30000-32767 will be used. Such Services without a NodePort specified will have one automatically allocated from this range. This parameter can be updated after the cluster is installed.</p></td>
</tr>
</tbody>
</table>

## .spec.clusterNetwork

Description
IP address pool to use for pod IPs. This field is immutable after installation.

Type
`array`

## .spec.clusterNetwork\[\]

Description
ClusterNetworkEntry is a contiguous block of IP addresses from which pod IPs are allocated.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `cidr` | `string` | The complete block for pod IPs. |
| `hostPrefix` | `integer` | The size (prefix) of block to allocate to each node. If this field is not used by the plugin, it can be left unset. |

## .spec.externalIP

Description
externalIP defines configuration for controllers that affect Service.ExternalIP. If nil, then ExternalIP is not allowed to be set.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `autoAssignCIDRs` | `array (string)` | autoAssignCIDRs is a list of CIDRs from which to automatically assign Service.ExternalIP. These are assigned when the service is of type LoadBalancer. In general, this is only useful for bare-metal clusters. In Openshift 3.x, this was misleadingly called "IngressIPs". Automatically assigned External IPs are not affected by any ExternalIPPolicy rules. Currently, only one entry may be provided. |
| `policy` | `object` | policy is a set of restrictions applied to the ExternalIP field. If nil or empty, then ExternalIP is not allowed to be set. |

## .spec.externalIP.policy

Description
policy is a set of restrictions applied to the ExternalIP field. If nil or empty, then ExternalIP is not allowed to be set.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `allowedCIDRs` | `array (string)` | allowedCIDRs is the list of allowed CIDRs. |
| `rejectedCIDRs` | `array (string)` | rejectedCIDRs is the list of disallowed CIDRs. These take precedence over allowedCIDRs. |

## .spec.networkDiagnostics

Description
networkDiagnostics defines network diagnostics configuration.

Takes precedence over spec.disableNetworkDiagnostics in network.operator.openshift.io. If networkDiagnostics is not specified or is empty, and the spec.disableNetworkDiagnostics flag in network.operator.openshift.io is set to true, the network diagnostics feature will be disabled.

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
<td style="text-align: left;"><p><code>mode</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>mode controls the network diagnostics mode</p>
<p>When omitted, this means the user has no opinion and the platform is left to choose reasonable defaults. These defaults are subject to change over time. The current default is All.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>sourcePlacement</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>sourcePlacement controls the scheduling of network diagnostics source deployment</p>
<p>See NetworkDiagnosticsSourcePlacement for more details about default values.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>targetPlacement</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>targetPlacement controls the scheduling of network diagnostics target daemonset</p>
<p>See NetworkDiagnosticsTargetPlacement for more details about default values.</p></td>
</tr>
</tbody>
</table>

## .spec.networkDiagnostics.sourcePlacement

Description
sourcePlacement controls the scheduling of network diagnostics source deployment

See NetworkDiagnosticsSourcePlacement for more details about default values.

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
<td style="text-align: left;"><p><code>nodeSelector</code></p></td>
<td style="text-align: left;"><p><code>object (string)</code></p></td>
<td style="text-align: left;"><p>nodeSelector is the node selector applied to network diagnostics components</p>
<p>When omitted, this means the user has no opinion and the platform is left to choose reasonable defaults. These defaults are subject to change over time. The current default is <code>kubernetes.io/os: linux</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>tolerations</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>tolerations is a list of tolerations applied to network diagnostics components</p>
<p>When omitted, this means the user has no opinion and the platform is left to choose reasonable defaults. These defaults are subject to change over time. The current default is an empty list.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>tolerations[]</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>The pod this Toleration is attached to tolerates any taint that matches the triple &lt;key,value,effect&gt; using the matching operator &lt;operator&gt;.</p></td>
</tr>
</tbody>
</table>

## .spec.networkDiagnostics.sourcePlacement.tolerations

Description
tolerations is a list of tolerations applied to network diagnostics components

When omitted, this means the user has no opinion and the platform is left to choose reasonable defaults. These defaults are subject to change over time. The current default is an empty list.

Type
`array`

## .spec.networkDiagnostics.sourcePlacement.tolerations\[\]

Description
The pod this Toleration is attached to tolerates any taint that matches the triple \<key,value,effect\> using the matching operator \<operator\>.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `effect` | `string` | Effect indicates the taint effect to match. Empty means match all taint effects. When specified, allowed values are NoSchedule, PreferNoSchedule and NoExecute. |
| `key` | `string` | Key is the taint key that the toleration applies to. Empty means match all taint keys. If the key is empty, operator must be Exists; this combination means to match all values and all keys. |
| `operator` | `string` | Operator represents a key’s relationship to the value. Valid operators are Exists and Equal. Defaults to Equal. Exists is equivalent to wildcard for value, so that a pod can tolerate all taints of a particular category. |
| `tolerationSeconds` | `integer` | TolerationSeconds represents the period of time the toleration (which must be of effect NoExecute, otherwise this field is ignored) tolerates the taint. By default, it is not set, which means tolerate the taint forever (do not evict). Zero and negative values will be treated as 0 (evict immediately) by the system. |
| `value` | `string` | Value is the taint value the toleration matches to. If the operator is Exists, the value should be empty, otherwise just a regular string. |

## .spec.networkDiagnostics.targetPlacement

Description
targetPlacement controls the scheduling of network diagnostics target daemonset

See NetworkDiagnosticsTargetPlacement for more details about default values.

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
<td style="text-align: left;"><p><code>nodeSelector</code></p></td>
<td style="text-align: left;"><p><code>object (string)</code></p></td>
<td style="text-align: left;"><p>nodeSelector is the node selector applied to network diagnostics components</p>
<p>When omitted, this means the user has no opinion and the platform is left to choose reasonable defaults. These defaults are subject to change over time. The current default is <code>kubernetes.io/os: linux</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>tolerations</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>tolerations is a list of tolerations applied to network diagnostics components</p>
<p>When omitted, this means the user has no opinion and the platform is left to choose reasonable defaults. These defaults are subject to change over time. The current default is <code>- operator: "Exists"</code> which means that all taints are tolerated.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>tolerations[]</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>The pod this Toleration is attached to tolerates any taint that matches the triple &lt;key,value,effect&gt; using the matching operator &lt;operator&gt;.</p></td>
</tr>
</tbody>
</table>

## .spec.networkDiagnostics.targetPlacement.tolerations

Description
tolerations is a list of tolerations applied to network diagnostics components

When omitted, this means the user has no opinion and the platform is left to choose reasonable defaults. These defaults are subject to change over time. The current default is `- operator: "Exists"` which means that all taints are tolerated.

Type
`array`

## .spec.networkDiagnostics.targetPlacement.tolerations\[\]

Description
The pod this Toleration is attached to tolerates any taint that matches the triple \<key,value,effect\> using the matching operator \<operator\>.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `effect` | `string` | Effect indicates the taint effect to match. Empty means match all taint effects. When specified, allowed values are NoSchedule, PreferNoSchedule and NoExecute. |
| `key` | `string` | Key is the taint key that the toleration applies to. Empty means match all taint keys. If the key is empty, operator must be Exists; this combination means to match all values and all keys. |
| `operator` | `string` | Operator represents a key’s relationship to the value. Valid operators are Exists and Equal. Defaults to Equal. Exists is equivalent to wildcard for value, so that a pod can tolerate all taints of a particular category. |
| `tolerationSeconds` | `integer` | TolerationSeconds represents the period of time the toleration (which must be of effect NoExecute, otherwise this field is ignored) tolerates the taint. By default, it is not set, which means tolerate the taint forever (do not evict). Zero and negative values will be treated as 0 (evict immediately) by the system. |
| `value` | `string` | Value is the taint value the toleration matches to. If the operator is Exists, the value should be empty, otherwise just a regular string. |

## .status

Description
status holds observed values from the cluster. They may not be overridden.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `clusterNetwork` | `array` | IP address pool to use for pod IPs. |
| `clusterNetwork[]` | `object` | ClusterNetworkEntry is a contiguous block of IP addresses from which pod IPs are allocated. |
| `clusterNetworkMTU` | `integer` | clusterNetworkMTU is the MTU for inter-pod networking. |
| `conditions` | `array` | conditions represents the observations of a network.config current state. Known .status.conditions.type are: "NetworkDiagnosticsAvailable" |
| `conditions[]` | `object` | Condition contains details for one aspect of the current state of this API Resource. |
| `migration` | `object` | migration contains the cluster network migration configuration. |
| `networkType` | `string` | networkType is the plugin that is deployed (e.g. OVNKubernetes). |
| `serviceNetwork` | `array (string)` | IP address pool for services. Currently, we only support a single entry here. |

## .status.clusterNetwork

Description
IP address pool to use for pod IPs.

Type
`array`

## .status.clusterNetwork\[\]

Description
ClusterNetworkEntry is a contiguous block of IP addresses from which pod IPs are allocated.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `cidr` | `string` | The complete block for pod IPs. |
| `hostPrefix` | `integer` | The size (prefix) of block to allocate to each node. If this field is not used by the plugin, it can be left unset. |

## .status.conditions

Description
conditions represents the observations of a network.config current state. Known .status.conditions.type are: "NetworkDiagnosticsAvailable"

Type
`array`

## .status.conditions\[\]

Description
Condition contains details for one aspect of the current state of this API Resource.

Type
`object`

Required
- `lastTransitionTime`

- `message`

- `reason`

- `status`

- `type`

| Property | Type | Description |
|----|----|----|
| `lastTransitionTime` | `string` | lastTransitionTime is the last time the condition transitioned from one status to another. This should be when the underlying condition changed. If that is not known, then using the time when the API field changed is acceptable. |
| `message` | `string` | message is a human readable message indicating details about the transition. This may be an empty string. |
| `observedGeneration` | `integer` | observedGeneration represents the .metadata.generation that the condition was set based upon. For instance, if .metadata.generation is currently 12, but the .status.conditions\[x\].observedGeneration is 9, the condition is out of date with respect to the current state of the instance. |
| `reason` | `string` | reason contains a programmatic identifier indicating the reason for the condition’s last transition. Producers of specific condition types may define expected values and meanings for this field, and whether the values are considered a guaranteed API. The value should be a CamelCase string. This field may not be empty. |
| `status` | `string` | status of the condition, one of True, False, Unknown. |
| `type` | `string` | type of condition in CamelCase or in foo.example.com/CamelCase. |

## .status.migration

Description
migration contains the cluster network migration configuration.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `mtu` | `object` | mtu is the MTU configuration that is being deployed. |
| `networkType` | `string` | networkType is the target plugin that is being deployed. DEPRECATED: network type migration is no longer supported, so this should always be unset. |

## .status.migration.mtu

Description
mtu is the MTU configuration that is being deployed.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `machine` | `object` | machine contains MTU migration configuration for the machine’s uplink. |
| `network` | `object` | network contains MTU migration configuration for the default network. |

## .status.migration.mtu.machine

Description
machine contains MTU migration configuration for the machine’s uplink.

Type
`object`

| Property | Type      | Description                      |
|----------|-----------|----------------------------------|
| `from`   | `integer` | from is the MTU to migrate from. |
| `to`     | `integer` | to is the MTU to migrate to.     |

## .status.migration.mtu.network

Description
network contains MTU migration configuration for the default network.

Type
`object`

| Property | Type      | Description                      |
|----------|-----------|----------------------------------|
| `from`   | `integer` | from is the MTU to migrate from. |
| `to`     | `integer` | to is the MTU to migrate to.     |

# API endpoints

The following API endpoints are available:

- `/apis/config.openshift.io/v1/networks`

  - `DELETE`: delete collection of Network

  - `GET`: list objects of kind Network

  - `POST`: create a Network

- `/apis/config.openshift.io/v1/networks/{name}`

  - `DELETE`: delete a Network

  - `GET`: read the specified Network

  - `PATCH`: partially update the specified Network

  - `PUT`: replace the specified Network

## /apis/config.openshift.io/v1/networks

HTTP method
`DELETE`

Description
delete collection of Network

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Status`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`GET`

Description
list objects of kind Network

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`NetworkList`](../objects/index.md#io-openshift-config-v1-NetworkList) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`POST`

Description
create a Network

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`Network`](network-config-openshift-io-v1.md#network-config-openshift-io-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Network`](network-config-openshift-io-v1.md#network-config-openshift-io-v1) schema |
| 201 - Created | [`Network`](network-config-openshift-io-v1.md#network-config-openshift-io-v1) schema |
| 202 - Accepted | [`Network`](network-config-openshift-io-v1.md#network-config-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/config.openshift.io/v1/networks/{name}

| Parameter | Type     | Description         |
|-----------|----------|---------------------|
| `name`    | `string` | name of the Network |

Global path parameters

HTTP method
`DELETE`

Description
delete a Network

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
read the specified Network

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Network`](network-config-openshift-io-v1.md#network-config-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PATCH`

Description
partially update the specified Network

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Network`](network-config-openshift-io-v1.md#network-config-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PUT`

Description
replace the specified Network

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`Network`](network-config-openshift-io-v1.md#network-config-openshift-io-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Network`](network-config-openshift-io-v1.md#network-config-openshift-io-v1) schema |
| 201 - Created | [`Network`](network-config-openshift-io-v1.md#network-config-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses
