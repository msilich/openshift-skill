<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

The `FlowCollector` API is the underlying schema used to pilot and configure the deployments for collecting network flows. This reference guide helps you manage those critical settings.

# FlowCollector API specifications

Description
`FlowCollector` is the schema for the network flows collection API, which pilots and configures the underlying deployments.

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
<td style="text-align: left;"><p><code>apiVersion</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and might reject unrecognized values. More info: <a href="https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources">https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>kind</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Kind is a string value representing the REST resource this object represents. Servers might infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <a href="https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds">https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>metadata</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>Standard object’s metadata. More info: <a href="https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata">https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>spec</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>Defines the desired state of the FlowCollector resource.<br />
<br />
</p>
<p>*: the mention of "unsupported" or "deprecated" for a feature throughout this document means that this feature is not officially supported by Red Hat. It might have been, for example, contributed by the community and accepted without a formal agreement for maintenance. The product maintainers might provide some support for these features as a best effort only.</p></td>
</tr>
</tbody>
</table>

## .metadata

Description
Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata>

Type
`object`

## .spec

Description
Defines the desired state of the FlowCollector resource.


\*: the mention of "unsupported" or "deprecated" for a feature throughout this document means that this feature is not officially supported by Red Hat. It might have been, for example, contributed by the community and accepted without a formal agreement for maintenance. The product maintainers might provide some support for these features as a best effort only.

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
<td style="text-align: left;"><p><code>agent</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>Agent configuration for flows extraction.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>consolePlugin</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p><code>consolePlugin</code> defines the settings related to the OpenShift Container Platform Console plugin, when available.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>deploymentModel</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p><code>deploymentModel</code> defines the desired type of deployment for flow processing. Possible values are:<br />
</p>
<p>- <code>Service</code> (default) to make the flow processor listen as a Kubernetes Service, backed by a scalable Deployment.<br />
</p>
<p>- <code>Kafka</code> to make flows sent to a Kafka pipeline before consumption by the processor.<br />
</p>
<p>- <code>Direct</code> to make the flow processor listen directly from the agents using the host network, backed by a DaemonSet. Only recommended on small clusters, below 15 nodes.<br />
</p>
<p>Kafka can provide better scalability, resiliency, and high availability (for more details, see <a href="https://www.redhat.com/en/topics/integration/what-is-apache-kafka">https://www.redhat.com/en/topics/integration/what-is-apache-kafka</a>).<br />
</p>
<p><code>Direct</code> is not recommended on large clusters as it is less memory efficient.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>execution</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p><code>execution</code> defines configuration related to the execution of the flow collection process.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>exporters</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p><code>exporters</code> defines additional optional exporters for custom consumption or storage.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>kafka</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>Kafka configuration, allowing to use Kafka as a broker as part of the flow collection pipeline. Available when the <code>spec.deploymentModel</code> is <code>Kafka</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>loki</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p><code>loki</code>, the flow store, client settings.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>namespace</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Namespace where Network Observability pods are deployed.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>networkPolicy</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p><code>networkPolicy</code> defines network policy settings for Network Observability components isolation.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>processor</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p><code>processor</code> defines the settings of the component that receives the flows from the agent, enriches them, generates metrics, and forwards them to the Loki persistence layer and/or any available exporter.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>prometheus</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p><code>prometheus</code> defines Prometheus settings, such as querier configuration used to fetch metrics from the Console plugin.</p></td>
</tr>
</tbody>
</table>

## .spec.agent

Description
Agent configuration for flows extraction.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `ebpf` | `object` | `ebpf` describes the settings related to the eBPF-based flow reporter when `spec.agent.type` is set to `eBPF`. |
| `type` | `string` | `type` \[deprecated (\*)\] selects the flows tracing agent. Previously, this field allowed to select between `eBPF` or `IPFIX`. Only `eBPF` is allowed now, so this field is deprecated and is planned for removal in a future version of the API. |

## .spec.agent.ebpf

Description
`ebpf` describes the settings related to the eBPF-based flow reporter when `spec.agent.type` is set to `eBPF`.

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
<td style="text-align: left;"><p><code>advanced</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p><code>advanced</code> allows setting some aspects of the internal configuration of the eBPF agent. This section is aimed mostly for debugging and fine-grained performance optimizations, such as <code>GOGC</code> and <code>GOMAXPROCS</code> environment variables. Set these values at your own risk. You can also override the default Linux capabilities from there.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>cacheActiveTimeout</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p><code>cacheActiveTimeout</code> is the period during which the agent aggregates flows before sending. Increasing <code>cacheMaxFlows</code> and <code>cacheActiveTimeout</code> can decrease the network traffic overhead and the CPU load, however you can expect higher memory consumption and an increased latency in the flow collection.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>cacheMaxFlows</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p><code>cacheMaxFlows</code> is the maximum number of flows in an aggregate; when reached, the reporter sends the flows. Increasing <code>cacheMaxFlows</code> and <code>cacheActiveTimeout</code> can decrease the network traffic overhead and the CPU load, however you can expect higher memory consumption and an increased latency in the flow collection.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>excludeInterfaces</code></p></td>
<td style="text-align: left;"><p><code>array (string)</code></p></td>
<td style="text-align: left;"><p><code>excludeInterfaces</code> contains the interface names that are excluded from flow tracing. An entry enclosed by slashes, such as <code>/br-/</code>, is matched as a regular expression. Otherwise it is matched as a case-sensitive string.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>features</code></p></td>
<td style="text-align: left;"><p><code>array (string)</code></p></td>
<td style="text-align: left;"><p>List of additional features to enable. They are all disabled by default. Enabling additional features might have performance impacts. Possible values are:<br />
</p>
<p>- <code>PacketDrop</code>: Enable the packets drop flows logging feature. This feature requires mounting the kernel debug filesystem, so the eBPF agent pods must run as privileged via <code>spec.agent.ebpf.privileged</code>.<br />
</p>
<p>- <code>DNSTracking</code>: Enable the DNS tracking feature.<br />
</p>
<p>- <code>FlowRTT</code>: Enable flow latency (sRTT) extraction in the eBPF agent from TCP traffic.<br />
</p>
<p>- <code>NetworkEvents</code>: Enable the network events monitoring feature, such as correlating flows and network policies. This feature requires mounting the kernel debug filesystem, so the eBPF agent pods must run as privileged via <code>spec.agent.ebpf.privileged</code>. It requires using the OVN-Kubernetes network plugin with the Observability feature. IMPORTANT: This feature is available as a Technology Preview.<br />
</p>
<p>- <code>PacketTranslation</code>: Enable enriching flows with packet translation information, such as Service NAT.<br />
</p>
<p>- <code>EbpfManager</code>: [Unsupported (*)]. Use eBPF Manager to manage Network Observability eBPF programs. Pre-requisite: the eBPF Manager operator (or upstream bpfman operator) must be installed.<br />
</p>
<p>- <code>UDNMapping</code>: Enable interfaces mapping to User Defined Networks (UDN).<br />
</p>
<p>This feature requires mounting the kernel debug filesystem, so the eBPF agent pods must run as privileged via <code>spec.agent.ebpf.privileged</code>. It requires using the OVN-Kubernetes network plugin with the Observability feature.<br />
</p>
<p>- <code>IPSec</code>, to track flows between nodes with IPsec encryption.<br />
</p>
<p>- <code>TLSTracking</code>, to track TLS usage.<br />
</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>flowFilter</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p><code>flowFilter</code> defines the eBPF agent configuration regarding flow filtering.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>imagePullPolicy</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p><code>imagePullPolicy</code> is the Kubernetes pull policy for the image defined above</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>interfaces</code></p></td>
<td style="text-align: left;"><p><code>array (string)</code></p></td>
<td style="text-align: left;"><p><code>interfaces</code> contains the interface names from where flows are collected. If empty, the agent fetches all the interfaces in the system, excepting the ones listed in <code>excludeInterfaces</code>. An entry enclosed by slashes, such as <code>/br-/</code>, is matched as a regular expression. Otherwise it is matched as a case-sensitive string.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>kafkaBatchSize</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p><code>kafkaBatchSize</code> limits the maximum size of a request in bytes before being sent to a partition. Ignored when not using Kafka. Default: 1MB.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>logLevel</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p><code>logLevel</code> defines the log level for the Network Observability eBPF Agent</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>metrics</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p><code>metrics</code> defines the eBPF agent configuration regarding metrics.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>privileged</code></p></td>
<td style="text-align: left;"><p><code>boolean</code></p></td>
<td style="text-align: left;"><p>Privileged mode for the eBPF Agent container. When set to <code>true</code>, the agent is able to capture more traffic, including from secondary interfaces. When ignored or set to <code>false</code>, the operator sets granular capabilities (BPF, PERFMON, NET_ADMIN) to the container. Some agent features require the privileged mode, such as packet drops tracking (see <code>features</code>) and SR-IOV support.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>resources</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p><code>resources</code> are the compute resources required by this container. For more information, see <a href="https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/">https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>sampling</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p>Sampling interval of the eBPF probe. 100 means one packet on 100 is sent. 0 or 1 means all packets are sampled.</p></td>
</tr>
</tbody>
</table>

## .spec.agent.ebpf.advanced

Description
`advanced` allows setting some aspects of the internal configuration of the eBPF agent. This section is aimed mostly for debugging and fine-grained performance optimizations, such as `GOGC` and `GOMAXPROCS` environment variables. Set these values at your own risk. You can also override the default Linux capabilities from there.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `capOverride` | `array (string)` | Linux capabilities override, when not running as privileged. Default capabilities are BPF, PERFMON and NET_ADMIN. |
| `env` | `object (string)` | `env` allows passing custom environment variables to underlying components. Useful for passing some very concrete performance-tuning options, such as `GOGC` and `GOMAXPROCS`, that should not be publicly exposed as part of the FlowCollector descriptor, as they are only useful in edge debug or support scenarios. |
| `scheduling` | `object` | scheduling controls how the pods are scheduled on nodes. |

## .spec.agent.ebpf.advanced.scheduling

Description
scheduling controls how the pods are scheduled on nodes.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `affinity` | `object` | If specified, the pod’s scheduling constraints. For documentation, refer to <https://kubernetes.io/docs/reference/kubernetes-api/workload-resources/pod-v1/#scheduling>. |
| `nodeSelector` | `object (string)` | `nodeSelector` allows scheduling of pods only onto nodes that have each of the specified labels. For documentation, refer to <https://kubernetes.io/docs/concepts/configuration/assign-pod-node/>. |
| `priorityClassName` | `string` | If specified, indicates the pod’s priority. For documentation, refer to <https://kubernetes.io/docs/concepts/scheduling-eviction/pod-priority-preemption/#how-to-use-priority-and-preemption>. If not specified, default priority is used, or zero if there is no default. |
| `tolerations` | `array` | `tolerations` is a list of tolerations that allow the pod to schedule onto nodes with matching taints. For documentation, refer to <https://kubernetes.io/docs/reference/kubernetes-api/workload-resources/pod-v1/#scheduling>. |

## .spec.agent.ebpf.advanced.scheduling.affinity

Description
If specified, the pod’s scheduling constraints. For documentation, refer to <https://kubernetes.io/docs/reference/kubernetes-api/workload-resources/pod-v1/#scheduling>.

Type
`object`

## .spec.agent.ebpf.advanced.scheduling.tolerations

Description
`tolerations` is a list of tolerations that allow the pod to schedule onto nodes with matching taints. For documentation, refer to <https://kubernetes.io/docs/reference/kubernetes-api/workload-resources/pod-v1/#scheduling>.

Type
`array`

## .spec.agent.ebpf.flowFilter

Description
`flowFilter` defines the eBPF agent configuration regarding flow filtering.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `action` | `string` | `action` defines the action to perform on the flows that match the filter. The available options are `Accept`, which is the default, and `Reject`. |
| `cidr` | `string` | `cidr` defines the IP CIDR to filter flows by. Examples: `10.10.10.0/24` or `100:100:100:100::/64` |
| `destPorts` | `integer-or-string` | `destPorts` optionally defines the destination ports to filter flows by. To filter a single port, set a single port as an integer value. For example, `destPorts: 80`. To filter a range of ports, use a "start-end" range in string format. For example, `destPorts: "80-100"`. To filter two ports, use a "port1,port2" in string format. For example, `ports: "80,100"`. |
| `direction` | `string` | `direction` optionally defines a direction to filter flows by. The available options are `Ingress` and `Egress`. |
| `enable` | `boolean` | Set `enable` to `true` to enable the eBPF flow filtering feature. |
| `icmpCode` | `integer` | `icmpCode`, for Internet Control Message Protocol (ICMP) traffic, optionally defines the ICMP code to filter flows by. |
| `icmpType` | `integer` | `icmpType`, for ICMP traffic, optionally defines the ICMP type to filter flows by. |
| `peerCIDR` | `string` | `peerCIDR` defines the Peer IP CIDR to filter flows by. Examples: `10.10.10.0/24` or `100:100:100:100::/64` |
| `peerIP` | `string` | `peerIP` optionally defines the remote IP address to filter flows by. Example: `10.10.10.10`. |
| `pktDrops` | `boolean` | `pktDrops` optionally filters only flows containing packet drops. |
| `ports` | `integer-or-string` | `ports` optionally defines the ports to filter flows by. It is used both for source and destination ports. To filter a single port, set a single port as an integer value. For example, `ports: 80`. To filter a range of ports, use a "start-end" range in string format. For example, `ports: "80-100"`. To filter two ports, use a "port1,port2" in string format. For example, `ports: "80,100"`. |
| `protocol` | `string` | `protocol` optionally defines a protocol to filter flows by. The available options are `TCP`, `UDP`, `ICMP`, `ICMPv6`, and `SCTP`. |
| `rules` | `array` | `rules` defines a list of filtering rules on the eBPF Agents. When filtering is enabled, by default, flows that don’t match any rule are rejected. To change the default, you can define a rule that accepts everything: `{ action: "Accept", cidr: "0.0.0.0/0" }`, and then refine with rejecting rules. |
| `sampling` | `integer` | `sampling` is the sampling interval for the matched packets, overriding the global sampling defined at `spec.agent.ebpf.sampling`. |
| `sourcePorts` | `integer-or-string` | `sourcePorts` optionally defines the source ports to filter flows by. To filter a single port, set a single port as an integer value. For example, `sourcePorts: 80`. To filter a range of ports, use a "start-end" range in string format. For example, `sourcePorts: "80-100"`. To filter two ports, use a "port1,port2" in string format. For example, `ports: "80,100"`. |
| `tcpFlags` | `string` | `tcpFlags` optionally defines TCP flags to filter flows by. In addition to the standard flags (RFC-9293), you can also filter by one of the three following combinations: `SYN-ACK`, `FIN-ACK`, and `RST-ACK`. |

## .spec.agent.ebpf.flowFilter.rules

Description
`rules` defines a list of filtering rules on the eBPF Agents. When filtering is enabled, by default, flows that don’t match any rule are rejected. To change the default, you can define a rule that accepts everything: `{ action: "Accept", cidr: "0.0.0.0/0" }`, and then refine with rejecting rules.

Type
`array`

## .spec.agent.ebpf.flowFilter.rules\[\]

Description
`EBPFFlowFilterRule` defines the desired eBPF agent configuration regarding flow filtering rule.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `action` | `string` | `action` defines the action to perform on the flows that match the filter. The available options are `Accept`, which is the default, and `Reject`. |
| `cidr` | `string` | `cidr` defines the IP CIDR to filter flows by. Examples: `10.10.10.0/24` or `100:100:100:100::/64` |
| `destPorts` | `integer-or-string` | `destPorts` optionally defines the destination ports to filter flows by. To filter a single port, set a single port as an integer value. For example, `destPorts: 80`. To filter a range of ports, use a "start-end" range in string format. For example, `destPorts: "80-100"`. To filter two ports, use a "port1,port2" in string format. For example, `ports: "80,100"`. |
| `direction` | `string` | `direction` optionally defines a direction to filter flows by. The available options are `Ingress` and `Egress`. |
| `icmpCode` | `integer` | `icmpCode`, for Internet Control Message Protocol (ICMP) traffic, optionally defines the ICMP code to filter flows by. |
| `icmpType` | `integer` | `icmpType`, for ICMP traffic, optionally defines the ICMP type to filter flows by. |
| `peerCIDR` | `string` | `peerCIDR` defines the Peer IP CIDR to filter flows by. Examples: `10.10.10.0/24` or `100:100:100:100::/64` |
| `peerIP` | `string` | `peerIP` optionally defines the remote IP address to filter flows by. Example: `10.10.10.10`. |
| `pktDrops` | `boolean` | `pktDrops` optionally filters only flows containing packet drops. |
| `ports` | `integer-or-string` | `ports` optionally defines the ports to filter flows by. It is used both for source and destination ports. To filter a single port, set a single port as an integer value. For example, `ports: 80`. To filter a range of ports, use a "start-end" range in string format. For example, `ports: "80-100"`. To filter two ports, use a "port1,port2" in string format. For example, `ports: "80,100"`. |
| `protocol` | `string` | `protocol` optionally defines a protocol to filter flows by. The available options are `TCP`, `UDP`, `ICMP`, `ICMPv6`, and `SCTP`. |
| `sampling` | `integer` | `sampling` is the sampling interval for the matched packets, overriding the global sampling defined at `spec.agent.ebpf.sampling`. |
| `sourcePorts` | `integer-or-string` | `sourcePorts` optionally defines the source ports to filter flows by. To filter a single port, set a single port as an integer value. For example, `sourcePorts: 80`. To filter a range of ports, use a "start-end" range in string format. For example, `sourcePorts: "80-100"`. To filter two ports, use a "port1,port2" in string format. For example, `ports: "80,100"`. |
| `tcpFlags` | `string` | `tcpFlags` optionally defines TCP flags to filter flows by. In addition to the standard flags (RFC-9293), you can also filter by one of the three following combinations: `SYN-ACK`, `FIN-ACK`, and `RST-ACK`. |

## .spec.agent.ebpf.metrics

Description
`metrics` defines the eBPF agent configuration regarding metrics.

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
<td style="text-align: left;"><p><code>disableAlerts</code></p></td>
<td style="text-align: left;"><p><code>array (string)</code></p></td>
<td style="text-align: left;"><p><code>disableAlerts</code> is a list of alerts that should be disabled. Possible values are:<br />
</p>
<p><code>NetObservDroppedFlows</code>, which is triggered when the eBPF agent is missing packets or flows, such as when the BPF hashmap is busy or full, or the capacity limiter is being triggered.<br />
</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>enable</code></p></td>
<td style="text-align: left;"><p><code>boolean</code></p></td>
<td style="text-align: left;"><p>Set <code>enable</code> to <code>false</code> to disable eBPF agent metrics collection. It is enabled by default.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>server</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>Metrics server endpoint configuration for the Prometheus scraper.</p></td>
</tr>
</tbody>
</table>

## .spec.agent.ebpf.metrics.server

Description
Metrics server endpoint configuration for the Prometheus scraper.

Type
`object`

| Property | Type      | Description                   |
|----------|-----------|-------------------------------|
| `port`   | `integer` | The metrics server HTTP port. |
| `tls`    | `object`  | TLS configuration.            |

## .spec.agent.ebpf.metrics.server.tls

Description
TLS configuration.

Type
`object`

Required
- `type`

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
<td style="text-align: left;"><p><code>insecureSkipVerify</code></p></td>
<td style="text-align: left;"><p><code>boolean</code></p></td>
<td style="text-align: left;"><p><code>insecureSkipVerify</code> allows skipping client-side verification of the provided certificate. If set to <code>true</code>, the <code>providedCaFile</code> field is ignored.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>provided</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>TLS configuration when <code>type</code> is set to <code>Provided</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>providedCaFile</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>Reference to the CA file when <code>type</code> is set to <code>Provided</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>type</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Select the type of TLS configuration:<br />
</p>
<p>- <code>Disabled</code> (default) to not configure TLS for the endpoint. - <code>Provided</code> to manually provide cert file and a key file. [Unsupported (*)]. - <code>Auto</code> to use OpenShift Container Platform auto generated certificate using annotations.</p></td>
</tr>
</tbody>
</table>

## .spec.agent.ebpf.metrics.server.tls.provided

Description
TLS configuration when `type` is set to `Provided`.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `certFile` | `string` | `certFile` defines the path to the certificate file name within the config map or secret. |
| `certKey` | `string` | `certKey` defines the path to the certificate private key file name within the config map or secret. Omit when the key is not necessary. |
| `name` | `string` | Name of the config map or secret containing certificates. |
| `namespace` | `string` | Namespace of the config map or secret containing certificates. If omitted, the default is to use the same namespace as where Network Observability is deployed. If the namespace is different, the config map or the secret is copied so that it can be mounted as required. |
| `type` | `string` | Type for the certificate reference: `configmap` or `secret`. |

## .spec.agent.ebpf.metrics.server.tls.providedCaFile

Description
Reference to the CA file when `type` is set to `Provided`.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `file` | `string` | File name within the config map or secret. |
| `name` | `string` | Name of the config map or secret containing the file. |
| `namespace` | `string` | Namespace of the config map or secret containing the file. If omitted, the default is to use the same namespace as where Network Observability is deployed. If the namespace is different, the config map or the secret is copied so that it can be mounted as required. |
| `type` | `string` | Type for the file reference: `configmap` or `secret`. |

## .spec.agent.ebpf.resources

Description
`resources` are the compute resources required by this container. For more information, see <https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/>

Type
`object`

| Property | Type | Description |
|----|----|----|
| `limits` | `integer-or-string` | Limits describes the maximum amount of compute resources allowed. More info: <https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/> |
| `requests` | `integer-or-string` | Requests describes the minimum amount of compute resources required. If Requests is omitted for a container, it defaults to Limits if that is explicitly specified, otherwise to an implementation-defined value. Requests cannot exceed Limits. More info: <https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/> |

## .spec.consolePlugin

Description
`consolePlugin` defines the settings related to the OpenShift Container Platform Console plugin, when available.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `advanced` | `object` | `advanced` allows setting some aspects of the internal configuration of the console plugin. This section is aimed mostly for debugging and fine-grained performance optimizations, such as `GOGC` and `GOMAXPROCS` environment variables. Set these values at your own risk. |
| `autoscaler` | `object` | `autoscaler` \[deprecated (\*)\] spec of a horizontal pod autoscaler to set up for the plugin Deployment. Deprecation notice: managed autoscaler will be removed in a future version. You might configure instead an autoscaler of your choice, and set `spec.consolePlugin.unmanagedReplicas` to `true`. Refer to HorizontalPodAutoscaler documentation (autoscaling/v2). |
| `enable` | `boolean` | Enables the console plugin deployment. |
| `imagePullPolicy` | `string` | `imagePullPolicy` is the Kubernetes pull policy for the image defined above. |
| `logLevel` | `string` | `logLevel` for the console plugin backend. |
| `portNaming` | `object` | `portNaming` defines the configuration of the port-to-service name translation. |
| `quickFilters` | `array` | `quickFilters` configures quick filter presets for the Console plugin. Filters for external traffic assume the subnet labels are configured to distinguish internal and external traffic (see `spec.processor.subnetLabels`). |
| `replicas` | `integer` | `replicas` defines the number of replicas (pods) to start. |
| `resources` | `object` | `resources`, in terms of compute resources, required by this container. For more information, see <https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/>. |
| `standalone` | `boolean` | Deploy as a standalone console, instead of a plugin of the OpenShift Container Platform Console. This is not recommended when using with OpenShift Container Platform, as it doesn’t provide an integrated experience. \[Unsupported (\*)\]. |
| `unmanagedReplicas` | `boolean` | If `unmanagedReplicas` is `true`, the operator will not reconcile `replicas`. This is useful when using a pod autoscaler. |

## .spec.consolePlugin.advanced

Description
`advanced` allows setting some aspects of the internal configuration of the console plugin. This section is aimed mostly for debugging and fine-grained performance optimizations, such as `GOGC` and `GOMAXPROCS` environment variables. Set these values at your own risk.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `args` | `array (string)` | `args` allows passing custom arguments to underlying components. Useful for overriding some parameters, such as a URL or a configuration path, that should not be publicly exposed as part of the FlowCollector descriptor, as they are only useful in edge debug or support scenarios. |
| `env` | `object (string)` | `env` allows passing custom environment variables to underlying components. Useful for passing some very concrete performance-tuning options, such as `GOGC` and `GOMAXPROCS`, that should not be publicly exposed as part of the FlowCollector descriptor, as they are only useful in edge debug or support scenarios. |
| `port` | `integer` | `port` is the plugin service port. Do not use 9002, which is reserved for metrics. |
| `register` | `boolean` | `register` allows, when set to `true`, to automatically register the provided console plugin with the OpenShift Container Platform Console operator. When set to `false`, you can still register it manually by editing console.operator.openshift.io/cluster with the following command: `oc patch console.operator.openshift.io cluster --type='json' -p '[{"op": "add", "path": "/spec/plugins/-", "value": "netobserv-plugin"}]'` |
| `scheduling` | `object` | `scheduling` controls how the pods are scheduled on nodes. |

## .spec.consolePlugin.advanced.scheduling

Description
`scheduling` controls how the pods are scheduled on nodes.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `affinity` | `object` | If specified, the pod’s scheduling constraints. For documentation, refer to <https://kubernetes.io/docs/reference/kubernetes-api/workload-resources/pod-v1/#scheduling>. |
| `nodeSelector` | `object (string)` | `nodeSelector` allows scheduling of pods only onto nodes that have each of the specified labels. For documentation, refer to <https://kubernetes.io/docs/concepts/configuration/assign-pod-node/>. |
| `priorityClassName` | `string` | If specified, indicates the pod’s priority. For documentation, refer to <https://kubernetes.io/docs/concepts/scheduling-eviction/pod-priority-preemption/#how-to-use-priority-and-preemption>. If not specified, default priority is used, or zero if there is no default. |
| `tolerations` | `array` | `tolerations` is a list of tolerations that allow the pod to schedule onto nodes with matching taints. For documentation, refer to <https://kubernetes.io/docs/reference/kubernetes-api/workload-resources/pod-v1/#scheduling>. |

## .spec.consolePlugin.advanced.scheduling.affinity

Description
If specified, the pod’s scheduling constraints. For documentation, refer to <https://kubernetes.io/docs/reference/kubernetes-api/workload-resources/pod-v1/#scheduling>.

Type
`object`

## .spec.consolePlugin.advanced.scheduling.tolerations

Description
`tolerations` is a list of tolerations that allow the pod to schedule onto nodes with matching taints. For documentation, refer to <https://kubernetes.io/docs/reference/kubernetes-api/workload-resources/pod-v1/#scheduling>.

Type
`array`

## .spec.consolePlugin.autoscaler

Description
`autoscaler` \[deprecated (\*)\] spec of a horizontal pod autoscaler to set up for the plugin Deployment. Deprecation notice: managed autoscaler will be removed in a future version. You might configure instead an autoscaler of your choice, and set `spec.consolePlugin.unmanagedReplicas` to `true`. Refer to HorizontalPodAutoscaler documentation (autoscaling/v2).

Type
`object`

## .spec.consolePlugin.portNaming

Description
`portNaming` defines the configuration of the port-to-service name translation.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `enable` | `boolean` | Enable the console plugin port-to-service name translation |
| `portNames` | `object (string)` | `portNames` defines additional port names to use in the console, for example, `portNames: {"3100": "loki"}`. |

## .spec.consolePlugin.quickFilters

Description
`quickFilters` configures quick filter presets for the Console plugin. Filters for external traffic assume the subnet labels are configured to distinguish internal and external traffic (see `spec.processor.subnetLabels`).

Type
`array`

## .spec.consolePlugin.quickFilters\[\]

Description
`QuickFilter` defines preset configuration for Console’s quick filters

Type
`object`

Required
- `filter`

- `name`

| Property | Type | Description |
|----|----|----|
| `default` | `boolean` | `default` defines whether this filter should be active by default or not |
| `filter` | `object (string)` | `filter` is a set of keys and values to be set when this filter is selected. Each key can relate to a list of values using a coma-separated string, for example, `filter: {"src_namespace": "namespace1,namespace2"}`. |
| `name` | `string` | Name of the filter, that is displayed in the Console |

## .spec.consolePlugin.resources

Description
`resources`, in terms of compute resources, required by this container. For more information, see <https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/>.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `limits` | `integer-or-string` | Limits describes the maximum amount of compute resources allowed. More info: <https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/> |
| `requests` | `integer-or-string` | Requests describes the minimum amount of compute resources required. If Requests is omitted for a container, it defaults to Limits if that is explicitly specified, otherwise to an implementation-defined value. Requests cannot exceed Limits. More info: <https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/> |

## .spec.execution

Description
`execution` defines configuration related to the execution of the flow collection process.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `mode` | `string` | `mode` is the flow collection process execution desired mode: `Running` or `OnHold`. When `OnHold`, the operator deletes all managed services and workloads, with the exception of the static console plugin, and the operator itself. It allows to use minimal cluster resources without losing configuration. |

## .spec.exporters

Description
`exporters` defines additional optional exporters for custom consumption or storage.

Type
`array`

## .spec.exporters\[\]

Description
`FlowCollectorExporter` defines an additional exporter to send enriched flows to.

Type
`object`

Required
- `type`

| Property | Type | Description |
|----|----|----|
| `ipfix` | `object` | IPFIX configuration, such as the IP address and port to send enriched IPFIX flows to. |
| `kafka` | `object` | Kafka configuration, such as the address and topic, to send enriched flows to. |
| `openTelemetry` | `object` | OpenTelemetry configuration, such as the IP address and port to send enriched logs or metrics to. |
| `type` | `string` | `type` selects the type of exporters. The available options are `Kafka`, `IPFIX`, and `OpenTelemetry`. |

## .spec.exporters\[\].ipfix

Description
IPFIX configuration, such as the IP address and port to send enriched IPFIX flows to.

Type
`object`

Required
- `enterpriseID`

- `targetHost`

- `targetPort`

| Property | Type | Description |
|----|----|----|
| `enterpriseID` | `integer` | EnterpriseID, or Private Enterprise Number (PEN). To date, Network Observability does not own an assigned number, so it is left open for configuration. The PEN is needed to collect non standard data, such as Kubernetes names, RTT, etc. |
| `targetHost` | `string` | Address of the IPFIX external receiver. |
| `targetPort` | `integer` | Port for the IPFIX external receiver. |
| `transport` | `string` | Transport protocol (`TCP` or `UDP`) to be used for the IPFIX connection, defaults to `TCP`. |

## .spec.exporters\[\].kafka

Description
Kafka configuration, such as the address and topic, to send enriched flows to.

Type
`object`

Required
- `address`

- `topic`

| Property | Type | Description |
|----|----|----|
| `address` | `string` | Address of the Kafka server |
| `compression` | `string` | Compression codec to use when producing messages to Kafka. Accepted values are: `none` (default), `gzip`, `snappy`, `lz4`, `zstd`. |
| `sasl` | `object` | SASL authentication configuration. \[Unsupported (\*)\]. |
| `tls` | `object` | TLS and mTLS client configuration. When using TLS, verify that the address matches the Kafka port used for TLS, generally 9093. We recommend the use of mTLS for higher security standards. |
| `topic` | `string` | Kafka topic to use. It must exist. Network Observability does not create it. |

## .spec.exporters\[\].kafka.sasl

Description
SASL authentication configuration. \[Unsupported (\*)\].

Type
`object`

| Property | Type | Description |
|----|----|----|
| `clientIDReference` | `object` | Reference to the secret or config map containing the client ID |
| `clientSecretReference` | `object` | Reference to the secret or config map containing the client secret |
| `type` | `string` | Type of SASL authentication to use, or `Disabled` if SASL is not used |

## .spec.exporters\[\].kafka.sasl.clientIDReference

Description
Reference to the secret or config map containing the client ID

Type
`object`

| Property | Type | Description |
|----|----|----|
| `file` | `string` | File name within the config map or secret. |
| `name` | `string` | Name of the config map or secret containing the file. |
| `namespace` | `string` | Namespace of the config map or secret containing the file. If omitted, the default is to use the same namespace as where Network Observability is deployed. If the namespace is different, the config map or the secret is copied so that it can be mounted as required. |
| `type` | `string` | Type for the file reference: `configmap` or `secret`. |

## .spec.exporters\[\].kafka.sasl.clientSecretReference

Description
Reference to the secret or config map containing the client secret

Type
`object`

| Property | Type | Description |
|----|----|----|
| `file` | `string` | File name within the config map or secret. |
| `name` | `string` | Name of the config map or secret containing the file. |
| `namespace` | `string` | Namespace of the config map or secret containing the file. If omitted, the default is to use the same namespace as where Network Observability is deployed. If the namespace is different, the config map or the secret is copied so that it can be mounted as required. |
| `type` | `string` | Type for the file reference: `configmap` or `secret`. |

## .spec.exporters\[\].kafka.tls

Description
TLS and mTLS client configuration. When using TLS, verify that the address matches the Kafka port used for TLS, generally 9093. We recommend the use of mTLS for higher security standards.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `caCert` | `object` | `caCert` defines the reference of the certificate for the Certificate Authority. |
| `enable` | `boolean` | Enable TLS |
| `insecureSkipVerify` | `boolean` | `insecureSkipVerify` allows skipping client-side verification of the server certificate. If set to `true`, the `caCert` field is ignored. |
| `userCert` | `object` | `userCert` defines the user certificate reference and is used for mTLS. When you use one-way TLS, you can ignore this property. |

## .spec.exporters\[\].kafka.tls.caCert

Description
`caCert` defines the reference of the certificate for the Certificate Authority.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `certFile` | `string` | `certFile` defines the path to the certificate file name within the config map or secret. |
| `certKey` | `string` | `certKey` defines the path to the certificate private key file name within the config map or secret. Omit when the key is not necessary. |
| `name` | `string` | Name of the config map or secret containing certificates. |
| `namespace` | `string` | Namespace of the config map or secret containing certificates. If omitted, the default is to use the same namespace as where Network Observability is deployed. If the namespace is different, the config map or the secret is copied so that it can be mounted as required. |
| `type` | `string` | Type for the certificate reference: `configmap` or `secret`. |

## .spec.exporters\[\].kafka.tls.userCert

Description
`userCert` defines the user certificate reference and is used for mTLS. When you use one-way TLS, you can ignore this property.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `certFile` | `string` | `certFile` defines the path to the certificate file name within the config map or secret. |
| `certKey` | `string` | `certKey` defines the path to the certificate private key file name within the config map or secret. Omit when the key is not necessary. |
| `name` | `string` | Name of the config map or secret containing certificates. |
| `namespace` | `string` | Namespace of the config map or secret containing certificates. If omitted, the default is to use the same namespace as where Network Observability is deployed. If the namespace is different, the config map or the secret is copied so that it can be mounted as required. |
| `type` | `string` | Type for the certificate reference: `configmap` or `secret`. |

## .spec.exporters\[\].openTelemetry

Description
OpenTelemetry configuration, such as the IP address and port to send enriched logs or metrics to.

Type
`object`

Required
- `targetHost`

- `targetPort`

| Property | Type | Description |
|----|----|----|
| `fieldsMapping` | `array` | Custom fields mapping to an OpenTelemetry conformant format. By default, Network Observability format proposal is used: <https://github.com/rhobs/observability-data-model/blob/main/network-observability.md#format-proposal> . As there is currently no accepted standard for L3 or L4 enriched network logs, you can freely override it with your own. |
| `headers` | `object (string)` | Headers to add to messages (optional) |
| `logs` | `object` | OpenTelemetry configuration for logs. |
| `metrics` | `object` | OpenTelemetry configuration for metrics. |
| `protocol` | `string` | Protocol of the OpenTelemetry connection. The available options are `http` and `grpc`. |
| `targetHost` | `string` | Address of the OpenTelemetry receiver. |
| `targetPort` | `integer` | Port for the OpenTelemetry receiver. |
| `tls` | `object` | TLS client configuration. |

## .spec.exporters\[\].openTelemetry.fieldsMapping

Description
Custom fields mapping to an OpenTelemetry conformant format. By default, Network Observability format proposal is used: <https://github.com/rhobs/observability-data-model/blob/main/network-observability.md#format-proposal> . As there is currently no accepted standard for L3 or L4 enriched network logs, you can freely override it with your own.

Type
`array`

## .spec.exporters\[\].openTelemetry.fieldsMapping\[\]

Description

Type
`object`

| Property     | Type      | Description |
|--------------|-----------|-------------|
| `input`      | `string`  |             |
| `multiplier` | `integer` |             |
| `output`     | `string`  |             |

## .spec.exporters\[\].openTelemetry.logs

Description
OpenTelemetry configuration for logs.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `enable` | `boolean` | Set `enable` to `true` to send logs to an OpenTelemetry receiver. |

## .spec.exporters\[\].openTelemetry.metrics

Description
OpenTelemetry configuration for metrics.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `enable` | `boolean` | Set `enable` to `true` to send metrics to an OpenTelemetry receiver. |
| `pushTimeInterval` | `string` | Specify how often metrics are sent to a collector. |

## .spec.exporters\[\].openTelemetry.tls

Description
TLS client configuration.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `caCert` | `object` | `caCert` defines the reference of the certificate for the Certificate Authority. |
| `enable` | `boolean` | Enable TLS |
| `insecureSkipVerify` | `boolean` | `insecureSkipVerify` allows skipping client-side verification of the server certificate. If set to `true`, the `caCert` field is ignored. |
| `userCert` | `object` | `userCert` defines the user certificate reference and is used for mTLS. When you use one-way TLS, you can ignore this property. |

## .spec.exporters\[\].openTelemetry.tls.caCert

Description
`caCert` defines the reference of the certificate for the Certificate Authority.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `certFile` | `string` | `certFile` defines the path to the certificate file name within the config map or secret. |
| `certKey` | `string` | `certKey` defines the path to the certificate private key file name within the config map or secret. Omit when the key is not necessary. |
| `name` | `string` | Name of the config map or secret containing certificates. |
| `namespace` | `string` | Namespace of the config map or secret containing certificates. If omitted, the default is to use the same namespace as where Network Observability is deployed. If the namespace is different, the config map or the secret is copied so that it can be mounted as required. |
| `type` | `string` | Type for the certificate reference: `configmap` or `secret`. |

## .spec.exporters\[\].openTelemetry.tls.userCert

Description
`userCert` defines the user certificate reference and is used for mTLS. When you use one-way TLS, you can ignore this property.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `certFile` | `string` | `certFile` defines the path to the certificate file name within the config map or secret. |
| `certKey` | `string` | `certKey` defines the path to the certificate private key file name within the config map or secret. Omit when the key is not necessary. |
| `name` | `string` | Name of the config map or secret containing certificates. |
| `namespace` | `string` | Namespace of the config map or secret containing certificates. If omitted, the default is to use the same namespace as where Network Observability is deployed. If the namespace is different, the config map or the secret is copied so that it can be mounted as required. |
| `type` | `string` | Type for the certificate reference: `configmap` or `secret`. |

## .spec.kafka

Description
Kafka configuration, allowing to use Kafka as a broker as part of the flow collection pipeline. Available when the `spec.deploymentModel` is `Kafka`.

Type
`object`

Required
- `address`

- `topic`

| Property | Type | Description |
|----|----|----|
| `address` | `string` | Address of the Kafka server |
| `compression` | `string` | Compression codec to use when producing messages to Kafka. Accepted values are: `none` (default), `gzip`, `snappy`, `lz4`, `zstd`. |
| `sasl` | `object` | SASL authentication configuration. \[Unsupported (\*)\]. |
| `tls` | `object` | TLS and mTLS client configuration. When using TLS, verify that the address matches the Kafka port used for TLS, generally 9093. We recommend the use of mTLS for higher security standards. |
| `topic` | `string` | Kafka topic to use. It must exist. Network Observability does not create it. |

## .spec.kafka.sasl

Description
SASL authentication configuration. \[Unsupported (\*)\].

Type
`object`

| Property | Type | Description |
|----|----|----|
| `clientIDReference` | `object` | Reference to the secret or config map containing the client ID |
| `clientSecretReference` | `object` | Reference to the secret or config map containing the client secret |
| `type` | `string` | Type of SASL authentication to use, or `Disabled` if SASL is not used |

## .spec.kafka.sasl.clientIDReference

Description
Reference to the secret or config map containing the client ID

Type
`object`

| Property | Type | Description |
|----|----|----|
| `file` | `string` | File name within the config map or secret. |
| `name` | `string` | Name of the config map or secret containing the file. |
| `namespace` | `string` | Namespace of the config map or secret containing the file. If omitted, the default is to use the same namespace as where Network Observability is deployed. If the namespace is different, the config map or the secret is copied so that it can be mounted as required. |
| `type` | `string` | Type for the file reference: `configmap` or `secret`. |

## .spec.kafka.sasl.clientSecretReference

Description
Reference to the secret or config map containing the client secret

Type
`object`

| Property | Type | Description |
|----|----|----|
| `file` | `string` | File name within the config map or secret. |
| `name` | `string` | Name of the config map or secret containing the file. |
| `namespace` | `string` | Namespace of the config map or secret containing the file. If omitted, the default is to use the same namespace as where Network Observability is deployed. If the namespace is different, the config map or the secret is copied so that it can be mounted as required. |
| `type` | `string` | Type for the file reference: `configmap` or `secret`. |

## .spec.kafka.tls

Description
TLS and mTLS client configuration. When using TLS, verify that the address matches the Kafka port used for TLS, generally 9093. We recommend the use of mTLS for higher security standards.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `caCert` | `object` | `caCert` defines the reference of the certificate for the Certificate Authority. |
| `enable` | `boolean` | Enable TLS |
| `insecureSkipVerify` | `boolean` | `insecureSkipVerify` allows skipping client-side verification of the server certificate. If set to `true`, the `caCert` field is ignored. |
| `userCert` | `object` | `userCert` defines the user certificate reference and is used for mTLS. When you use one-way TLS, you can ignore this property. |

## .spec.kafka.tls.caCert

Description
`caCert` defines the reference of the certificate for the Certificate Authority.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `certFile` | `string` | `certFile` defines the path to the certificate file name within the config map or secret. |
| `certKey` | `string` | `certKey` defines the path to the certificate private key file name within the config map or secret. Omit when the key is not necessary. |
| `name` | `string` | Name of the config map or secret containing certificates. |
| `namespace` | `string` | Namespace of the config map or secret containing certificates. If omitted, the default is to use the same namespace as where Network Observability is deployed. If the namespace is different, the config map or the secret is copied so that it can be mounted as required. |
| `type` | `string` | Type for the certificate reference: `configmap` or `secret`. |

## .spec.kafka.tls.userCert

Description
`userCert` defines the user certificate reference and is used for mTLS. When you use one-way TLS, you can ignore this property.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `certFile` | `string` | `certFile` defines the path to the certificate file name within the config map or secret. |
| `certKey` | `string` | `certKey` defines the path to the certificate private key file name within the config map or secret. Omit when the key is not necessary. |
| `name` | `string` | Name of the config map or secret containing certificates. |
| `namespace` | `string` | Namespace of the config map or secret containing certificates. If omitted, the default is to use the same namespace as where Network Observability is deployed. If the namespace is different, the config map or the secret is copied so that it can be mounted as required. |
| `type` | `string` | Type for the certificate reference: `configmap` or `secret`. |

## .spec.loki

Description
`loki`, the flow store, client settings.

Type
`object`

Required
- `mode`

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
<td style="text-align: left;"><p><code>advanced</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p><code>advanced</code> allows setting some aspects of the internal configuration of the Loki clients. This section is aimed mostly for debugging and fine-grained performance optimizations.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>enable</code></p></td>
<td style="text-align: left;"><p><code>boolean</code></p></td>
<td style="text-align: left;"><p>Set <code>enable</code> to <code>true</code> to store flows in Loki. The Console plugin can use either Loki or Prometheus as a data source for metrics (see also <code>spec.prometheus.querier</code>), or both. Not all queries are transposable from Loki to Prometheus. Hence, if Loki is disabled, some features of the plugin are disabled as well, such as getting per-pod information or viewing raw flows. If both Prometheus and Loki are enabled, Prometheus takes precedence and Loki is used as a fallback for queries that Prometheus cannot handle. If they are both disabled, the Console plugin is not deployed.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>lokiStack</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>Loki configuration for <code>LokiStack</code> mode. This is useful for an easy Loki Operator configuration. It is ignored for other modes.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>manual</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>Loki configuration for <code>Manual</code> mode. This is the most flexible configuration. It is ignored for other modes.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>microservices</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>Loki configuration for <code>Microservices</code> mode. Use this option when Loki is installed using the microservices deployment mode (<a href="https://grafana.com/docs/loki/latest/fundamentals/architecture/deployment-modes/#microservices-mode">https://grafana.com/docs/loki/latest/fundamentals/architecture/deployment-modes/#microservices-mode</a>). It is ignored for other modes.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>mode</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p><code>mode</code> must be set according to the installation mode of Loki:<br />
</p>
<p>- Use <code>LokiStack</code> when Loki is managed using the Loki Operator<br />
</p>
<p>- Use <code>Monolithic</code> when Loki is installed as a monolithic workload<br />
</p>
<p>- Use <code>Microservices</code> when Loki is installed as microservices, but without Loki Operator<br />
</p>
<p>- Use <code>Manual</code> if none of the options above match your setup<br />
</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>monolithic</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>Loki configuration for <code>Monolithic</code> mode. Use this option when Loki is installed using the monolithic deployment mode (<a href="https://grafana.com/docs/loki/latest/fundamentals/architecture/deployment-modes/#monolithic-mode">https://grafana.com/docs/loki/latest/fundamentals/architecture/deployment-modes/#monolithic-mode</a>). It is ignored for other modes.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>readTimeout</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p><code>readTimeout</code> is the maximum console plugin loki query total time limit. A timeout of zero means no timeout.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>writeBatchSize</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p><code>writeBatchSize</code> is the maximum batch size (in bytes) of Loki logs to accumulate before sending.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>writeBatchWait</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p><code>writeBatchWait</code> is the maximum time to wait before sending a Loki batch.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>writeTimeout</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p><code>writeTimeout</code> is the maximum Loki time connection / request limit. A timeout of zero means no timeout.</p></td>
</tr>
</tbody>
</table>

## .spec.loki.advanced

Description
`advanced` allows setting some aspects of the internal configuration of the Loki clients. This section is aimed mostly for debugging and fine-grained performance optimizations.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `excludeLabels` | `array (string)` | `excludeLabels` is a list of fields to be excluded from the list of Loki labels. \[Unsupported (\*)\]. |
| `staticLabels` | `object (string)` | `staticLabels` is a map of common labels to set on each flow in Loki storage. |
| `writeMaxBackoff` | `string` | `writeMaxBackoff` is the maximum backoff time for Loki client connection between retries. |
| `writeMaxRetries` | `integer` | `writeMaxRetries` is the maximum number of retries for Loki client connections. |
| `writeMinBackoff` | `string` | `writeMinBackoff` is the initial backoff time for Loki client connection between retries. |

## .spec.loki.lokiStack

Description
Loki configuration for `LokiStack` mode. This is useful for an easy Loki Operator configuration. It is ignored for other modes.

Type
`object`

Required
- `name`

| Property | Type | Description |
|----|----|----|
| `name` | `string` | Name of an existing LokiStack resource to use. |
| `namespace` | `string` | Namespace where this `LokiStack` resource is located. If omitted, it is assumed to be the same as `spec.namespace`. |

## .spec.loki.manual

Description
Loki configuration for `Manual` mode. This is the most flexible configuration. It is ignored for other modes.

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
<td style="text-align: left;"><p><code>authToken</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p><code>authToken</code> describes the way to get a token to authenticate to Loki.<br />
</p>
<p>- <code>Disabled</code> does not send any token with the request.<br />
</p>
<p>- <code>Forward</code> forwards the user token for authorization.<br />
</p>
<p>- <code>Host</code> [deprecated (*)] - uses the local pod service account to authenticate to Loki.<br />
</p>
<p>When using the Loki Operator, this must be set to <code>Forward</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>ingesterUrl</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p><code>ingesterUrl</code> is the address of an existing Loki ingester service to push the flows to. When using the Loki Operator, set it to the Loki gateway service with the <code>network</code> tenant set in path, for example <a href="https://loki-gateway-http.netobserv.svc:8080/api/logs/v1/network">https://loki-gateway-http.netobserv.svc:8080/api/logs/v1/network</a>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>querierUrl</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p><code>querierUrl</code> specifies the address of the Loki querier service. When using the Loki Operator, set it to the Loki gateway service with the <code>network</code> tenant set in path, for example <a href="https://loki-gateway-http.netobserv.svc:8080/api/logs/v1/network">https://loki-gateway-http.netobserv.svc:8080/api/logs/v1/network</a>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>statusTls</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>TLS client configuration for Loki status URL.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>statusUrl</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p><code>statusUrl</code> specifies the address of the Loki <code>/ready</code>, <code>/metrics</code> and <code>/config</code> endpoints, in case it is different from the Loki querier URL. If empty, the <code>querierUrl</code> value is used. This is useful to show error messages and some context in the frontend. When using the Loki Operator, set it to the Loki HTTP query frontend service, for example <a href="https://loki-query-frontend-http.netobserv.svc:3100/">https://loki-query-frontend-http.netobserv.svc:3100/</a>. <code>statusTLS</code> configuration is used when <code>statusUrl</code> is set.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>tenantID</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p><code>tenantID</code> is the Loki <code>X-Scope-OrgID</code> that identifies the tenant for each request. When using the Loki Operator, set it to <code>network</code>, which corresponds to a special tenant mode.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>tls</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>TLS client configuration for Loki URL.</p></td>
</tr>
</tbody>
</table>

## .spec.loki.manual.statusTls

Description
TLS client configuration for Loki status URL.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `caCert` | `object` | `caCert` defines the reference of the certificate for the Certificate Authority. |
| `enable` | `boolean` | Enable TLS |
| `insecureSkipVerify` | `boolean` | `insecureSkipVerify` allows skipping client-side verification of the server certificate. If set to `true`, the `caCert` field is ignored. |
| `userCert` | `object` | `userCert` defines the user certificate reference and is used for mTLS. When you use one-way TLS, you can ignore this property. |

## .spec.loki.manual.statusTls.caCert

Description
`caCert` defines the reference of the certificate for the Certificate Authority.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `certFile` | `string` | `certFile` defines the path to the certificate file name within the config map or secret. |
| `certKey` | `string` | `certKey` defines the path to the certificate private key file name within the config map or secret. Omit when the key is not necessary. |
| `name` | `string` | Name of the config map or secret containing certificates. |
| `namespace` | `string` | Namespace of the config map or secret containing certificates. If omitted, the default is to use the same namespace as where Network Observability is deployed. If the namespace is different, the config map or the secret is copied so that it can be mounted as required. |
| `type` | `string` | Type for the certificate reference: `configmap` or `secret`. |

## .spec.loki.manual.statusTls.userCert

Description
`userCert` defines the user certificate reference and is used for mTLS. When you use one-way TLS, you can ignore this property.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `certFile` | `string` | `certFile` defines the path to the certificate file name within the config map or secret. |
| `certKey` | `string` | `certKey` defines the path to the certificate private key file name within the config map or secret. Omit when the key is not necessary. |
| `name` | `string` | Name of the config map or secret containing certificates. |
| `namespace` | `string` | Namespace of the config map or secret containing certificates. If omitted, the default is to use the same namespace as where Network Observability is deployed. If the namespace is different, the config map or the secret is copied so that it can be mounted as required. |
| `type` | `string` | Type for the certificate reference: `configmap` or `secret`. |

## .spec.loki.manual.tls

Description
TLS client configuration for Loki URL.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `caCert` | `object` | `caCert` defines the reference of the certificate for the Certificate Authority. |
| `enable` | `boolean` | Enable TLS |
| `insecureSkipVerify` | `boolean` | `insecureSkipVerify` allows skipping client-side verification of the server certificate. If set to `true`, the `caCert` field is ignored. |
| `userCert` | `object` | `userCert` defines the user certificate reference and is used for mTLS. When you use one-way TLS, you can ignore this property. |

## .spec.loki.manual.tls.caCert

Description
`caCert` defines the reference of the certificate for the Certificate Authority.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `certFile` | `string` | `certFile` defines the path to the certificate file name within the config map or secret. |
| `certKey` | `string` | `certKey` defines the path to the certificate private key file name within the config map or secret. Omit when the key is not necessary. |
| `name` | `string` | Name of the config map or secret containing certificates. |
| `namespace` | `string` | Namespace of the config map or secret containing certificates. If omitted, the default is to use the same namespace as where Network Observability is deployed. If the namespace is different, the config map or the secret is copied so that it can be mounted as required. |
| `type` | `string` | Type for the certificate reference: `configmap` or `secret`. |

## .spec.loki.manual.tls.userCert

Description
`userCert` defines the user certificate reference and is used for mTLS. When you use one-way TLS, you can ignore this property.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `certFile` | `string` | `certFile` defines the path to the certificate file name within the config map or secret. |
| `certKey` | `string` | `certKey` defines the path to the certificate private key file name within the config map or secret. Omit when the key is not necessary. |
| `name` | `string` | Name of the config map or secret containing certificates. |
| `namespace` | `string` | Namespace of the config map or secret containing certificates. If omitted, the default is to use the same namespace as where Network Observability is deployed. If the namespace is different, the config map or the secret is copied so that it can be mounted as required. |
| `type` | `string` | Type for the certificate reference: `configmap` or `secret`. |

## .spec.loki.microservices

Description
Loki configuration for `Microservices` mode. Use this option when Loki is installed using the microservices deployment mode (<https://grafana.com/docs/loki/latest/fundamentals/architecture/deployment-modes/#microservices-mode>). It is ignored for other modes.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `ingesterUrl` | `string` | `ingesterUrl` is the address of an existing Loki ingester service to push the flows to. |
| `querierUrl` | `string` | `querierURL` specifies the address of the Loki querier service. |
| `tenantID` | `string` | `tenantID` is the Loki `X-Scope-OrgID` header that identifies the tenant for each request. |
| `tls` | `object` | TLS client configuration for Loki URL. |

## .spec.loki.microservices.tls

Description
TLS client configuration for Loki URL.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `caCert` | `object` | `caCert` defines the reference of the certificate for the Certificate Authority. |
| `enable` | `boolean` | Enable TLS |
| `insecureSkipVerify` | `boolean` | `insecureSkipVerify` allows skipping client-side verification of the server certificate. If set to `true`, the `caCert` field is ignored. |
| `userCert` | `object` | `userCert` defines the user certificate reference and is used for mTLS. When you use one-way TLS, you can ignore this property. |

## .spec.loki.microservices.tls.caCert

Description
`caCert` defines the reference of the certificate for the Certificate Authority.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `certFile` | `string` | `certFile` defines the path to the certificate file name within the config map or secret. |
| `certKey` | `string` | `certKey` defines the path to the certificate private key file name within the config map or secret. Omit when the key is not necessary. |
| `name` | `string` | Name of the config map or secret containing certificates. |
| `namespace` | `string` | Namespace of the config map or secret containing certificates. If omitted, the default is to use the same namespace as where Network Observability is deployed. If the namespace is different, the config map or the secret is copied so that it can be mounted as required. |
| `type` | `string` | Type for the certificate reference: `configmap` or `secret`. |

## .spec.loki.microservices.tls.userCert

Description
`userCert` defines the user certificate reference and is used for mTLS. When you use one-way TLS, you can ignore this property.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `certFile` | `string` | `certFile` defines the path to the certificate file name within the config map or secret. |
| `certKey` | `string` | `certKey` defines the path to the certificate private key file name within the config map or secret. Omit when the key is not necessary. |
| `name` | `string` | Name of the config map or secret containing certificates. |
| `namespace` | `string` | Namespace of the config map or secret containing certificates. If omitted, the default is to use the same namespace as where Network Observability is deployed. If the namespace is different, the config map or the secret is copied so that it can be mounted as required. |
| `type` | `string` | Type for the certificate reference: `configmap` or `secret`. |

## .spec.loki.monolithic

Description
Loki configuration for `Monolithic` mode. Use this option when Loki is installed using the monolithic deployment mode (<https://grafana.com/docs/loki/latest/fundamentals/architecture/deployment-modes/#monolithic-mode>). It is ignored for other modes.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `installDemoLoki` | `boolean` | Set `installDemoLoki` to `true` to automatically create Loki deployment, service and storage. This is useful for development and demo purposes. Do not use it in production. \[Unsupported (\*)\]. |
| `tenantID` | `string` | `tenantID` is the Loki `X-Scope-OrgID` header that identifies the tenant for each request. |
| `tls` | `object` | TLS client configuration for Loki URL. |
| `url` | `string` | `url` is the unique address of an existing Loki service that points to both the ingester and the querier. |

## .spec.loki.monolithic.tls

Description
TLS client configuration for Loki URL.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `caCert` | `object` | `caCert` defines the reference of the certificate for the Certificate Authority. |
| `enable` | `boolean` | Enable TLS |
| `insecureSkipVerify` | `boolean` | `insecureSkipVerify` allows skipping client-side verification of the server certificate. If set to `true`, the `caCert` field is ignored. |
| `userCert` | `object` | `userCert` defines the user certificate reference and is used for mTLS. When you use one-way TLS, you can ignore this property. |

## .spec.loki.monolithic.tls.caCert

Description
`caCert` defines the reference of the certificate for the Certificate Authority.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `certFile` | `string` | `certFile` defines the path to the certificate file name within the config map or secret. |
| `certKey` | `string` | `certKey` defines the path to the certificate private key file name within the config map or secret. Omit when the key is not necessary. |
| `name` | `string` | Name of the config map or secret containing certificates. |
| `namespace` | `string` | Namespace of the config map or secret containing certificates. If omitted, the default is to use the same namespace as where Network Observability is deployed. If the namespace is different, the config map or the secret is copied so that it can be mounted as required. |
| `type` | `string` | Type for the certificate reference: `configmap` or `secret`. |

## .spec.loki.monolithic.tls.userCert

Description
`userCert` defines the user certificate reference and is used for mTLS. When you use one-way TLS, you can ignore this property.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `certFile` | `string` | `certFile` defines the path to the certificate file name within the config map or secret. |
| `certKey` | `string` | `certKey` defines the path to the certificate private key file name within the config map or secret. Omit when the key is not necessary. |
| `name` | `string` | Name of the config map or secret containing certificates. |
| `namespace` | `string` | Namespace of the config map or secret containing certificates. If omitted, the default is to use the same namespace as where Network Observability is deployed. If the namespace is different, the config map or the secret is copied so that it can be mounted as required. |
| `type` | `string` | Type for the certificate reference: `configmap` or `secret`. |

## .spec.networkPolicy

Description
`networkPolicy` defines network policy settings for Network Observability components isolation.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `additionalNamespaces` | `array (string)` | `additionalNamespaces` contains additional namespaces allowed to connect to the Network Observability namespace. It provides flexibility in the network policy configuration, but if you need a more specific configuration, you can disable it and install your own instead. |
| `enable` | `boolean` | Deploys network policies on the namespaces used by Network Observability (main and privileged). These network policies better isolate the Network Observability components to prevent undesired connections from and to them. Because it cannot be tested with all CNIs, this option is only enabled by default when Network Observability runs in a known supported environment, and it is disabled by default otherwise. When disabled, it is highly recommended to create network policies manually, to prevent undesired accesses. More information: <https://github.com/netobserv/netobserv-operator/blob/main/docs/NetworkPolicy.md>. |

## .spec.processor

Description
`processor` defines the settings of the component that receives the flows from the agent, enriches them, generates metrics, and forwards them to the Loki persistence layer and/or any available exporter.

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
<td style="text-align: left;"><p><code>addZone</code></p></td>
<td style="text-align: left;"><p><code>boolean</code></p></td>
<td style="text-align: left;"><p><code>addZone</code> allows availability zone awareness by labeling flows with their source and destination zones. This feature requires the "topology.kubernetes.io/zone" label to be set on nodes.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>advanced</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p><code>advanced</code> allows setting some aspects of the internal configuration of the flow processor. This section is aimed mostly for debugging and fine-grained performance optimizations, such as <code>GOGC</code> and <code>GOMAXPROCS</code> environment variables. Set these values at your own risk.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>clusterName</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p><code>clusterName</code> is the name of the cluster to appear in the flows data. This is useful in a multi-cluster context. When using OpenShift Container Platform, leave empty to make it automatically determined.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>consumerReplicas</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p><code>consumerReplicas</code> defines the number of replicas (pods) to start for <code>flowlogs-pipeline</code>, default is 3. This setting is ignored when <code>spec.deploymentModel</code> is <code>Direct</code> or when <code>spec.processor.unmanagedReplicas</code> is <code>true</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>deduper</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p><code>deduper</code> allows you to sample or drop flows identified as duplicates, in order to save on resource usage.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>filters</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p><code>filters</code> lets you define custom filters to limit the amount of generated flows. These filters provide more flexibility than the eBPF Agent filters (in <code>spec.agent.ebpf.flowFilter</code>), such as allowing to filter by Kubernetes namespace, but with a lesser improvement in performance.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>imagePullPolicy</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p><code>imagePullPolicy</code> is the Kubernetes pull policy for the image defined above</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>kafkaConsumerAutoscaler</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p><code>kafkaConsumerAutoscaler</code> [deprecated (*)] is the spec of a horizontal pod autoscaler to set up for <code>flowlogs-pipeline-transformer</code>, which consumes Kafka messages. This setting is ignored when Kafka is disabled. Deprecation notice: managed autoscaler will be removed in a future version. You might configure instead an autoscaler of your choice, and set <code>spec.processor.unmanagedReplicas</code> to <code>true</code>. Refer to HorizontalPodAutoscaler documentation (autoscaling/v2).</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>kafkaConsumerBatchSize</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p><code>kafkaConsumerBatchSize</code> indicates to the broker the maximum batch size, in bytes, that the consumer accepts. Ignored when not using Kafka. Default: 10MB.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>kafkaConsumerQueueCapacity</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p><code>kafkaConsumerQueueCapacity</code> defines the capacity of the internal message queue used in the Kafka consumer client. Ignored when not using Kafka.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>kafkaConsumerReplicas</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p><code>kafkaConsumerReplicas</code> [deprecated (*)] defines the number of replicas (pods) to start for <code>flowlogs-pipeline-transformer</code>, which consumes Kafka messages. This setting is ignored when Kafka is disabled. Deprecation notice: use <code>spec.processor.consumerReplicas</code> instead.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>logLevel</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p><code>logLevel</code> of the processor runtime</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>logTypes</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p><code>logTypes</code> defines the desired record types to generate. Possible values are:<br />
</p>
<p>- <code>Flows</code> to export regular network flows. This is the default.<br />
</p>
<p>- <code>Conversations</code> to generate events for started conversations, ended conversations as well as periodic "tick" updates. Note that in this mode, Prometheus metrics are not accurate on long-standing conversations.<br />
</p>
<p>- <code>EndedConversations</code> to generate only ended conversations events. Note that in this mode, Prometheus metrics are not accurate on long-standing conversations.<br />
</p>
<p>- <code>All</code> to generate both network flows and all conversations events. It is not recommended due to the impact on resources footprint.<br />
</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>metrics</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p><code>Metrics</code> define the processor configuration regarding metrics</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>multiClusterDeployment</code></p></td>
<td style="text-align: left;"><p><code>boolean</code></p></td>
<td style="text-align: left;"><p>Set <code>multiClusterDeployment</code> to <code>true</code> to enable multi clusters feature. This adds <code>clusterName</code> label to flows data</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>resources</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p><code>resources</code> are the compute resources required by this container. For more information, see <a href="https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/">https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>service</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>Service configuration, only used when <code>spec.deploymentModel</code> is <code>Service</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>slicesConfig</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>Global configuration managing FlowCollectorSlices custom resources.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>subnetLabels</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p><code>subnetLabels</code> allows to define custom labels on subnets and IPs or to enable automatic labeling of recognized subnets in OpenShift Container Platform, which is used to identify cluster external traffic. When a subnet matches the source or destination IP of a flow, a corresponding field is added: <code>SrcSubnetLabel</code> or <code>DstSubnetLabel</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>unmanagedReplicas</code></p></td>
<td style="text-align: left;"><p><code>boolean</code></p></td>
<td style="text-align: left;"><p>If <code>unmanagedReplicas</code> is <code>true</code>, the operator will not reconcile <code>consumerReplicas</code>. This is useful when using a pod autoscaler.</p></td>
</tr>
</tbody>
</table>

## .spec.processor.advanced

Description
`advanced` allows setting some aspects of the internal configuration of the flow processor. This section is aimed mostly for debugging and fine-grained performance optimizations, such as `GOGC` and `GOMAXPROCS` environment variables. Set these values at your own risk.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `conversationEndTimeout` | `string` | `conversationEndTimeout` is the time to wait after a network flow is received, to consider the conversation ended. This delay is ignored when a FIN packet is collected for TCP flows (see `conversationTerminatingTimeout` instead). |
| `conversationHeartbeatInterval` | `string` | `conversationHeartbeatInterval` is the time to wait between "tick" events of a conversation |
| `conversationTerminatingTimeout` | `string` | `conversationTerminatingTimeout` is the time to wait from detected FIN flag to end a conversation. Only relevant for TCP flows. |
| `dropUnusedFields` | `boolean` | `dropUnusedFields` \[deprecated (\*)\] this setting is not used anymore. |
| `enableKubeProbes` | `boolean` | `enableKubeProbes` is a flag to enable or disable Kubernetes liveness and readiness probes |
| `env` | `object (string)` | `env` allows passing custom environment variables to underlying components. Useful for passing some very concrete performance-tuning options, such as `GOGC` and `GOMAXPROCS`, that should not be publicly exposed as part of the FlowCollector descriptor, as they are only useful in edge debug or support scenarios. |
| `healthPort` | `integer` | `healthPort` is a collector HTTP port in the Pod that exposes the health check API |
| `port` | `integer` | Port of the flow collector (host port). By convention, some values are forbidden. It must be greater than 1024 and different from 4500, 4789 and 6081. |
| `profilePort` | `integer` | `profilePort` allows setting up a Go pprof profiler listening to this port |
| `scheduling` | `object` | scheduling controls how the pods are scheduled on nodes. |
| `secondaryNetworks` | `array` | Defines secondary networks to be checked for resources identification. To guarantee a correct identification, indexed values must form an unique identifier across the cluster. If the same index is used by several resources, those resources might be incorrectly labeled. If not provided and `spec.agent.ebpf.privileged` is `true`, secondary networks are detected automatically. |

## .spec.processor.advanced.scheduling

Description
scheduling controls how the pods are scheduled on nodes.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `affinity` | `object` | If specified, the pod’s scheduling constraints. For documentation, refer to <https://kubernetes.io/docs/reference/kubernetes-api/workload-resources/pod-v1/#scheduling>. |
| `nodeSelector` | `object (string)` | `nodeSelector` allows scheduling of pods only onto nodes that have each of the specified labels. For documentation, refer to <https://kubernetes.io/docs/concepts/configuration/assign-pod-node/>. |
| `priorityClassName` | `string` | If specified, indicates the pod’s priority. For documentation, refer to <https://kubernetes.io/docs/concepts/scheduling-eviction/pod-priority-preemption/#how-to-use-priority-and-preemption>. If not specified, default priority is used, or zero if there is no default. |
| `tolerations` | `array` | `tolerations` is a list of tolerations that allow the pod to schedule onto nodes with matching taints. For documentation, refer to <https://kubernetes.io/docs/reference/kubernetes-api/workload-resources/pod-v1/#scheduling>. |

## .spec.processor.advanced.scheduling.affinity

Description
If specified, the pod’s scheduling constraints. For documentation, refer to <https://kubernetes.io/docs/reference/kubernetes-api/workload-resources/pod-v1/#scheduling>.

Type
`object`

## .spec.processor.advanced.scheduling.tolerations

Description
`tolerations` is a list of tolerations that allow the pod to schedule onto nodes with matching taints. For documentation, refer to <https://kubernetes.io/docs/reference/kubernetes-api/workload-resources/pod-v1/#scheduling>.

Type
`array`

## .spec.processor.advanced.secondaryNetworks

Description
Defines secondary networks to be checked for resources identification. To guarantee a correct identification, indexed values must form an unique identifier across the cluster. If the same index is used by several resources, those resources might be incorrectly labeled.

Type
`array`

## .spec.processor.advanced.secondaryNetworks\[\]

Description

Type
`object`

Required
- `index`

| Property | Type | Description |
|----|----|----|
| `index` | `array (string)` | `index` is a list of fields to use for indexing the pods. They should form a unique Pod identifier across the cluster. Can be any of: `MAC`, `IP`, `Interface`. Fields absent from the 'k8s.v1.cni.cncf.io/network-status' annotation must not be added to the index. |
| `name` | `string` | Deprecated: `name` is unused. |

## .spec.processor.deduper

Description
`deduper` allows you to sample or drop flows identified as duplicates, in order to save on resource usage.

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
<td style="text-align: left;"><p>Set the Processor de-duplication mode. It comes in addition to the Agent-based deduplication, since the Agent cannot de-duplicate same flows reported from different nodes.<br />
</p>
<p>- Use <code>Drop</code> to drop every flow considered as duplicates, allowing saving more on resource usage but potentially losing some information such as the network interfaces used from peer, or network events.<br />
</p>
<p>- Use <code>Sample</code> to randomly keep only one flow on 50, which is the default, among the ones considered as duplicates. This is a compromise between dropping every duplicate or keeping every duplicate. This sampling action comes in addition to the Agent-based sampling. If both Agent and Processor sampling values are <code>50</code>, the combined sampling is 1:2500.<br />
</p>
<p>- Use <code>Disabled</code> to turn off Processor-based de-duplication.<br />
</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>sampling</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p><code>sampling</code> is the sampling interval when deduper <code>mode</code> is <code>Sample</code>. For example, a value of <code>50</code> means that 1 flow in 50 is sampled.</p></td>
</tr>
</tbody>
</table>

## .spec.processor.filters

Description
`filters` lets you define custom filters to limit the amount of generated flows. These filters provide more flexibility than the eBPF Agent filters (in `spec.agent.ebpf.flowFilter`), such as allowing to filter by Kubernetes namespace, but with a lesser improvement in performance.

Type
`array`

## .spec.processor.filters\[\]

Description
`FLPFilterSet` defines the desired configuration for FLP-based filtering satisfying all conditions.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `outputTarget` | `string` | If specified, these filters target a single output: `Loki`, `Metrics` or `Exporters`. By default, all outputs are targeted. |
| `query` | `string` | A query that selects the network flows to keep. More information about this query language in <https://github.com/netobserv/flowlogs-pipeline/blob/main/docs/filtering.md>. |
| `sampling` | `integer` | `sampling` is an optional sampling interval to apply to this filter. For example, a value of `50` means that 1 matching flow in 50 is sampled. |

## .spec.processor.kafkaConsumerAutoscaler

Description
`kafkaConsumerAutoscaler` \[deprecated (\*)\] is the spec of a horizontal pod autoscaler to set up for `flowlogs-pipeline-transformer`, which consumes Kafka messages. This setting is ignored when Kafka is disabled. Deprecation notice: managed autoscaler will be removed in a future version. You might configure instead an autoscaler of your choice, and set `spec.processor.unmanagedReplicas` to `true`. Refer to HorizontalPodAutoscaler documentation (autoscaling/v2).

Type
`object`

## .spec.processor.metrics

Description
`Metrics` define the processor configuration regarding metrics

Type
`object`

| Property | Type | Description |
|----|----|----|
| `additionalIncludeList` | `array (string)` | `additionalIncludeList` is a list of metric names to include in addition to the default metrics. Unlike `includeList`, this appends to the default list rather than replacing it. This field is mutually exclusive with `includeList`. If `includeList` is set, `additionalIncludeList` is ignored. The names correspond to the names in Prometheus without the prefix. For example, `namespace_egress_packets_total` shows up as `netobserv_namespace_egress_packets_total` in Prometheus. Note that the more metrics you add, the bigger is the impact on Prometheus workload resources. More information, with full list of available metrics: <https://github.com/netobserv/network-observability-operator/blob/main/docs/Metrics.md> |
| `disableAlerts` | `array (string)` | `disableAlerts` is a list of alert groups that should be disabled from the default set of alerts. Possible values are: `NetObservNoFlows`, `NetObservLokiError`, `PacketDropsByKernel`, `PacketDropsByDevice`, `IPsecErrors`, `NetpolDenied`, `LatencyHighTrend`, `DNSErrors`, `DNSNxDomain`, `ExternalEgressHighTrend`, `ExternalIngressHighTrend`, `Ingress5xxErrors`, `IngressHTTPLatencyTrend`. More information on alerts: <https://github.com/netobserv/network-observability-operator/blob/main/docs/HealthRules.md> |
| `healthRules` | `array` | `healthRules` is a list of health rules to be created for Prometheus, organized by templates and variants. Each health rule can be configured to generate either alerts or recording rules based on the mode field. More information on health rules: <https://github.com/netobserv/network-observability-operator/blob/main/docs/HealthRules.md> |
| `includeList` | `array (string)` | `includeList` is a list of metric names to specify which ones to generate. The names correspond to the names in Prometheus without the prefix. For example, `namespace_egress_packets_total` shows up as `netobserv_namespace_egress_packets_total` in Prometheus. Note that the more metrics you add, the bigger is the impact on Prometheus workload resources. Metrics enabled by default are: `namespace_flows_total`, `node_ingress_bytes_total`, `node_egress_bytes_total`, `workload_ingress_bytes_total`, `workload_egress_bytes_total`, `namespace_drop_packets_total` (when `PacketDrop` feature is enabled), `namespace_rtt_seconds` (when `FlowRTT` feature is enabled), `namespace_dns_latency_seconds` (when `DNSTracking` feature is enabled), `namespace_network_policy_events_total` (when `NetworkEvents` feature is enabled). More information, with full list of available metrics: <https://github.com/netobserv/network-observability-operator/blob/main/docs/Metrics.md> |
| `server` | `object` | Metrics server endpoint configuration for Prometheus scraper |

## .spec.processor.metrics.healthRules

Description
`healthRules` is a list of health rules to be created for Prometheus, organized by templates and variants. Each health rule can be configured to generate either alerts or recording rules based on the mode field. More information on health rules: <https://github.com/netobserv/network-observability-operator/blob/main/docs/HealthRules.md>

Type
`array`

## .spec.processor.metrics.healthRules\[\]

Description

Type
`object`

Required
- `template`

- `variants`

| Property | Type | Description |
|----|----|----|
| `mode` | `string` | Mode defines whether this health rule should be generated as an alert or a recording rule. Possible values are: `Alert` (default), `Recording`. Recording rules violations are visible in the Network Health dashboard without generating any Prometheus alert. This provides an alternative way of getting Health information for SRE and cluster admins who might find many new alerts burdensome. |
| `template` | `string` | Health rule template name. Possible values are: `PacketDropsByKernel`, `PacketDropsByDevice`, `IPsecErrors`, `NetpolDenied`, `LatencyHighTrend`, `DNSErrors`, `DNSNxDomain`, `ExternalEgressHighTrend`, `ExternalIngressHighTrend`, `Ingress5xxErrors`, `IngressHTTPLatencyTrend`. Note: `NetObservNoFlows` and `NetObservLokiError` are alert-only and cannot be used as health rules. More information on health rules: <https://github.com/netobserv/network-observability-operator/blob/main/docs/HealthRules.md> |
| `variants` | `array` | A list of variants for this template |

## .spec.processor.metrics.healthRules\[\].variants

Description
A list of variants for this template

Type
`array`

## .spec.processor.metrics.healthRules\[\].variants\[\]

Description

Type
`object`

Required
- `thresholds`

| Property | Type | Description |
|----|----|----|
| `groupBy` | `string` | Optional grouping criteria, possible values are: `Node`, `Namespace`, `Workload`. |
| `lowVolumeThreshold` | `string` | The low volume threshold allows to ignore metrics with a too low volume of traffic, in order to improve signal-to-noise. It is provided as an absolute rate (bytes per second or packets per second, depending on the context). When provided, it must be parsable as a float. |
| `mode` | `string` | Mode overrides the health rule mode for this specific variant. If not specified, inherits from the parent health rule’s mode. Possible values are: `Alert`, `Recording`. |
| `thresholds` | `object` | Thresholds of the health rule per severity. They are expressed as a percentage of errors above which the alert is triggered. They must be parsable as floats. Required for both alert and recording modes |
| `trendDuration` | `string` | For trending health rules, the duration interval for baseline comparison. For example, "2h" means comparing against a 2-hours average. Defaults to 2h. |
| `trendOffset` | `string` | For trending health rules, the time offset for baseline comparison. For example, "1d" means comparing against yesterday. Defaults to 1d. |

## .spec.processor.metrics.healthRules\[\].variants\[\].thresholds

Description
Thresholds of the health rule per severity. They are expressed as a percentage of errors above which the alert is triggered. They must be parsable as floats. Required for both alert and recording modes

Type
`object`

| Property | Type | Description |
|----|----|----|
| `critical` | `string` | Threshold for severity `critical`. Leave empty to not generate a Critical alert. |
| `info` | `string` | Threshold for severity `info`. Leave empty to not generate an Info alert. |
| `warning` | `string` | Threshold for severity `warning`. Leave empty to not generate a Warning alert. |

## .spec.processor.metrics.server

Description
Metrics server endpoint configuration for Prometheus scraper

Type
`object`

| Property | Type      | Description                   |
|----------|-----------|-------------------------------|
| `port`   | `integer` | The metrics server HTTP port. |
| `tls`    | `object`  | TLS configuration.            |

## .spec.processor.metrics.server.tls

Description
TLS configuration.

Type
`object`

Required
- `type`

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
<td style="text-align: left;"><p><code>insecureSkipVerify</code></p></td>
<td style="text-align: left;"><p><code>boolean</code></p></td>
<td style="text-align: left;"><p><code>insecureSkipVerify</code> allows skipping client-side verification of the provided certificate. If set to <code>true</code>, the <code>providedCaFile</code> field is ignored.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>provided</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>TLS configuration when <code>type</code> is set to <code>Provided</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>providedCaFile</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>Reference to the CA file when <code>type</code> is set to <code>Provided</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>type</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Select the type of TLS configuration:<br />
</p>
<p>- <code>Disabled</code> (default) to not configure TLS for the endpoint. - <code>Provided</code> to manually provide cert file and a key file. [Unsupported (*)]. - <code>Auto</code> to use OpenShift Container Platform auto generated certificate using annotations.</p></td>
</tr>
</tbody>
</table>

## .spec.processor.metrics.server.tls.provided

Description
TLS configuration when `type` is set to `Provided`.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `certFile` | `string` | `certFile` defines the path to the certificate file name within the config map or secret. |
| `certKey` | `string` | `certKey` defines the path to the certificate private key file name within the config map or secret. Omit when the key is not necessary. |
| `name` | `string` | Name of the config map or secret containing certificates. |
| `namespace` | `string` | Namespace of the config map or secret containing certificates. If omitted, the default is to use the same namespace as where Network Observability is deployed. If the namespace is different, the config map or the secret is copied so that it can be mounted as required. |
| `type` | `string` | Type for the certificate reference: `configmap` or `secret`. |

## .spec.processor.metrics.server.tls.providedCaFile

Description
Reference to the CA file when `type` is set to `Provided`.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `file` | `string` | File name within the config map or secret. |
| `name` | `string` | Name of the config map or secret containing the file. |
| `namespace` | `string` | Namespace of the config map or secret containing the file. If omitted, the default is to use the same namespace as where Network Observability is deployed. If the namespace is different, the config map or the secret is copied so that it can be mounted as required. |
| `type` | `string` | Type for the file reference: `configmap` or `secret`. |

## .spec.processor.resources

Description
`resources` are the compute resources required by this container. For more information, see <https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/>

Type
`object`

| Property | Type | Description |
|----|----|----|
| `limits` | `integer-or-string` | Limits describes the maximum amount of compute resources allowed. More info: <https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/> |
| `requests` | `integer-or-string` | Requests describes the minimum amount of compute resources required. If Requests is omitted for a container, it defaults to Limits if that is explicitly specified, otherwise to an implementation-defined value. Requests cannot exceed Limits. More info: <https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/> |

## .spec.processor.service

Description
Service configuration, only used when `spec.deploymentModel` is `Service`.

Type
`object`

Required
- `tlsType`

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
<td style="text-align: left;"><p><code>providedCertificates</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>TLS or mTLS configuration when <code>type</code> is set to <code>Provided</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>tlsType</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Select the type of TLS configuration:<br />
</p>
<p>- <code>Disabled</code> to not configure TLS for the endpoint. Disabling TLS results in a less secure deployment model.<br />
</p>
<p>- <code>Provided</code> to manually provide the key and certificate references.<br />
</p>
<p>- <code>Auto</code> (default) to enable automatically based on the running environment.<br />
</p>
<p>- <code>Auto-mTLS</code> to preconfigure mTLS. [Unsupported (*)].<br />
</p>
<p>See also: <a href="https://github.com/netobserv/netobserv-operator/blob/main/docs/TLS.md">https://github.com/netobserv/netobserv-operator/blob/main/docs/TLS.md</a>.</p></td>
</tr>
</tbody>
</table>

## .spec.processor.service.providedCertificates

Description
TLS or mTLS configuration when `type` is set to `Provided`.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `caFile` | `object` | Reference to the CA file. |
| `clientCert` | `object` | TLS client certificate reference, used for mTLS. Leave unset for simple TLS. |
| `serverCert` | `object` | TLS server certificate reference. |

## .spec.processor.service.providedCertificates.caFile

Description
Reference to the CA file.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `file` | `string` | File name within the config map or secret. |
| `name` | `string` | Name of the config map or secret containing the file. |
| `namespace` | `string` | Namespace of the config map or secret containing the file. If omitted, the default is to use the same namespace as where Network Observability is deployed. If the namespace is different, the config map or the secret is copied so that it can be mounted as required. |
| `type` | `string` | Type for the file reference: `configmap` or `secret`. |

## .spec.processor.service.providedCertificates.clientCert

Description
TLS client certificate reference, used for mTLS. Leave unset for simple TLS.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `certFile` | `string` | `certFile` defines the path to the certificate file name within the config map or secret. |
| `certKey` | `string` | `certKey` defines the path to the certificate private key file name within the config map or secret. Omit when the key is not necessary. |
| `name` | `string` | Name of the config map or secret containing certificates. |
| `namespace` | `string` | Namespace of the config map or secret containing certificates. If omitted, the default is to use the same namespace as where Network Observability is deployed. If the namespace is different, the config map or the secret is copied so that it can be mounted as required. |
| `type` | `string` | Type for the certificate reference: `configmap` or `secret`. |

## .spec.processor.service.providedCertificates.serverCert

Description
TLS server certificate reference.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `certFile` | `string` | `certFile` defines the path to the certificate file name within the config map or secret. |
| `certKey` | `string` | `certKey` defines the path to the certificate private key file name within the config map or secret. Omit when the key is not necessary. |
| `name` | `string` | Name of the config map or secret containing certificates. |
| `namespace` | `string` | Namespace of the config map or secret containing certificates. If omitted, the default is to use the same namespace as where Network Observability is deployed. If the namespace is different, the config map or the secret is copied so that it can be mounted as required. |
| `type` | `string` | Type for the certificate reference: `configmap` or `secret`. |

## .spec.processor.slicesConfig

Description
Global configuration managing FlowCollectorSlices custom resources.

Type
`object`

Required
- `enable`

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
<td style="text-align: left;"><p><code>collectionMode</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p><code>collectionMode</code> determines how the FlowCollectorSlice custom resources impacts the flow collection process:<br />
</p>
<p>- When set to <code>AlwaysCollect</code>, all flows are collected regardless of the presence of FlowCollectorSlice.<br />
</p>
<p>- When set to <code>AllowList</code>, only the flows related to namespaces where a FlowCollectorSlice resource is present, or configured via the global <code>namespacesAllowList</code>, are collected.<br />
</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>enable</code></p></td>
<td style="text-align: left;"><p><code>boolean</code></p></td>
<td style="text-align: left;"><p><code>enable</code> determines if the FlowCollectorSlice feature is enabled. If not, all resources of kind FlowCollectorSlice are simply ignored.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>namespacesAllowList</code></p></td>
<td style="text-align: left;"><p><code>array (string)</code></p></td>
<td style="text-align: left;"><p><code>namespacesAllowList</code> is a list of namespaces for which flows are always collected, regardless of the presence of FlowCollectorSlice in those namespaces. An entry enclosed by slashes, such as <code>/openshift-.*/</code>, is matched as a regular expression. This setting is ignored if <code>collectionMode</code> is different from <code>AllowList</code>.</p></td>
</tr>
</tbody>
</table>

## .spec.processor.subnetLabels

Description
`subnetLabels` allows to define custom labels on subnets and IPs or to enable automatic labeling of recognized subnets in OpenShift Container Platform, which is used to identify cluster external traffic. When a subnet matches the source or destination IP of a flow, a corresponding field is added: `SrcSubnetLabel` or `DstSubnetLabel`.

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
<td style="text-align: left;"><p><code>customLabels</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p><code>customLabels</code> allows you to customize subnets and IPs labeling, such as to identify cluster external workloads or web services. External subnets must be labeled with the prefix <code>EXT:</code>, or not labeled at all, in order to work with default quick filters and some metrics examples provided.<br />
</p>
<p>If <code>openShiftAutoDetect</code> is disabled or you are not using OpenShift Container Platform, it is recommended to manually configure labels for the cluster subnets, to distinguish internal traffic from external traffic.<br />
</p>
<p>If <code>openShiftAutoDetect</code> is enabled, <code>customLabels</code> overrides the detected subnets when they overlap.<br />
</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>openShiftAutoDetect</code></p></td>
<td style="text-align: left;"><p><code>boolean</code></p></td>
<td style="text-align: left;"><p><code>openShiftAutoDetect</code> allows, when set to <code>true</code>, to detect automatically the machines, pods and services subnets based on the OpenShift Container Platform install configuration and the Cluster Network Operator configuration. Indirectly, this is a way to accurately detect external traffic: flows that are not labeled for those subnets are external to the cluster. Enabled by default on OpenShift Container Platform.</p></td>
</tr>
</tbody>
</table>

## .spec.processor.subnetLabels.customLabels

Description
`customLabels` allows you to customize subnets and IPs labeling, such as to identify cluster external workloads or web services. External subnets must be labeled with the prefix `EXT:`, or not labeled at all, in order to work with default quick filters and some metrics examples provided.

If `openShiftAutoDetect` is disabled or you are not using OpenShift Container Platform, it is recommended to manually configure labels for the cluster subnets, to distinguish internal traffic from external traffic.

If `openShiftAutoDetect` is enabled, `customLabels` overrides the detected subnets when they overlap.

Type
`array`

## .spec.processor.subnetLabels.customLabels\[\]

Description
SubnetLabel allows to label subnets and IPs, such as to identify cluster-external workloads or web services.

Type
`object`

Required
- `cidrs`

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
<td style="text-align: left;"><p><code>cidrs</code></p></td>
<td style="text-align: left;"><p><code>array (string)</code></p></td>
<td style="text-align: left;"><p>List of CIDRs, such as <code>["1.2.3.4/32"]</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>name</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Label name, used to flag matching flows. External subnets must be labeled with the prefix <code>EXT:</code>, or not labeled at all, in order to work with default quick filters and some metrics examples provided.<br />
</p></td>
</tr>
</tbody>
</table>

## .spec.prometheus

Description
`prometheus` defines Prometheus settings, such as querier configuration used to fetch metrics from the Console plugin.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `querier` | `object` | Prometheus querying configuration, such as client settings, used in the Console plugin. |

## .spec.prometheus.querier

Description
Prometheus querying configuration, such as client settings, used in the Console plugin.

Type
`object`

Required
- `mode`

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
<td style="text-align: left;"><p><code>enable</code></p></td>
<td style="text-align: left;"><p><code>boolean</code></p></td>
<td style="text-align: left;"><p>When <code>enable</code> is <code>true</code>, the Console plugin queries flow metrics from Prometheus instead of Loki whenever possible. It is enabled by default: set it to <code>false</code> to disable this feature. The Console plugin can use either Loki or Prometheus as a data source for metrics (see also <code>spec.loki</code>), or both. Not all queries are transposable from Loki to Prometheus. Hence, if Loki is disabled, some features of the plugin are disabled as well, such as getting per-pod information or viewing raw flows. If both Prometheus and Loki are enabled, Prometheus takes precedence and Loki is used as a fallback for queries that Prometheus cannot handle. If they are both disabled, the Console plugin is not deployed.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>manual</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>Prometheus configuration for <code>Manual</code> mode.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>mode</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p><code>mode</code> must be set according to the type of Prometheus installation that stores Network Observability metrics:<br />
</p>
<p>- Use <code>Auto</code> to try configuring automatically. In OpenShift Container Platform, it uses the Thanos querier from OpenShift Container Platform Cluster Monitoring.<br />
</p>
<p>- Use <code>Manual</code> for a manual setup.<br />
</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>timeout</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p><code>timeout</code> is the read timeout for console plugin queries to Prometheus. A timeout of zero means no timeout.</p></td>
</tr>
</tbody>
</table>

## .spec.prometheus.querier.manual

Description
Prometheus configuration for `Manual` mode.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `alertManager` | `object` | AlertManager configuration. This is used in the console to query silenced alerts, for displaying health information. When used in OpenShift Container Platform it can be left empty to use the Console API instead. \[Unsupported (\*)\]. |
| `forwardUserToken` | `boolean` | Set `true` to forward logged in user token in queries to Prometheus |
| `tls` | `object` | TLS client configuration for Prometheus URL. |
| `url` | `string` | `url` is the address of an existing Prometheus service to use for querying metrics. |

## .spec.prometheus.querier.manual.alertManager

Description
AlertManager configuration. This is used in the console to query silenced alerts, for displaying health information. When used in OpenShift Container Platform it can be left empty to use the Console API instead. \[Unsupported (\*)\].

Type
`object`

| Property | Type | Description |
|----|----|----|
| `tls` | `object` | TLS client configuration for Prometheus AlertManager URL. |
| `url` | `string` | `url` is the address of an existing Prometheus AlertManager service to use for querying alerts. |

## .spec.prometheus.querier.manual.alertManager.tls

Description
TLS client configuration for Prometheus AlertManager URL.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `caCert` | `object` | `caCert` defines the reference of the certificate for the Certificate Authority. |
| `enable` | `boolean` | Enable TLS |
| `insecureSkipVerify` | `boolean` | `insecureSkipVerify` allows skipping client-side verification of the server certificate. If set to `true`, the `caCert` field is ignored. |
| `userCert` | `object` | `userCert` defines the user certificate reference and is used for mTLS. When you use one-way TLS, you can ignore this property. |

## .spec.prometheus.querier.manual.alertManager.tls.caCert

Description
`caCert` defines the reference of the certificate for the Certificate Authority.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `certFile` | `string` | `certFile` defines the path to the certificate file name within the config map or secret. |
| `certKey` | `string` | `certKey` defines the path to the certificate private key file name within the config map or secret. Omit when the key is not necessary. |
| `name` | `string` | Name of the config map or secret containing certificates. |
| `namespace` | `string` | Namespace of the config map or secret containing certificates. If omitted, the default is to use the same namespace as where Network Observability is deployed. If the namespace is different, the config map or the secret is copied so that it can be mounted as required. |
| `type` | `string` | Type for the certificate reference: `configmap` or `secret`. |

## .spec.prometheus.querier.manual.alertManager.tls.userCert

Description
`userCert` defines the user certificate reference and is used for mTLS. When you use one-way TLS, you can ignore this property.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `certFile` | `string` | `certFile` defines the path to the certificate file name within the config map or secret. |
| `certKey` | `string` | `certKey` defines the path to the certificate private key file name within the config map or secret. Omit when the key is not necessary. |
| `name` | `string` | Name of the config map or secret containing certificates. |
| `namespace` | `string` | Namespace of the config map or secret containing certificates. If omitted, the default is to use the same namespace as where Network Observability is deployed. If the namespace is different, the config map or the secret is copied so that it can be mounted as required. |
| `type` | `string` | Type for the certificate reference: `configmap` or `secret`. |

## .spec.prometheus.querier.manual.tls

Description
TLS client configuration for Prometheus URL.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `caCert` | `object` | `caCert` defines the reference of the certificate for the Certificate Authority. |
| `enable` | `boolean` | Enable TLS |
| `insecureSkipVerify` | `boolean` | `insecureSkipVerify` allows skipping client-side verification of the server certificate. If set to `true`, the `caCert` field is ignored. |
| `userCert` | `object` | `userCert` defines the user certificate reference and is used for mTLS. When you use one-way TLS, you can ignore this property. |

## .spec.prometheus.querier.manual.tls.caCert

Description
`caCert` defines the reference of the certificate for the Certificate Authority.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `certFile` | `string` | `certFile` defines the path to the certificate file name within the config map or secret. |
| `certKey` | `string` | `certKey` defines the path to the certificate private key file name within the config map or secret. Omit when the key is not necessary. |
| `name` | `string` | Name of the config map or secret containing certificates. |
| `namespace` | `string` | Namespace of the config map or secret containing certificates. If omitted, the default is to use the same namespace as where Network Observability is deployed. If the namespace is different, the config map or the secret is copied so that it can be mounted as required. |
| `type` | `string` | Type for the certificate reference: `configmap` or `secret`. |

## .spec.prometheus.querier.manual.tls.userCert

Description
`userCert` defines the user certificate reference and is used for mTLS. When you use one-way TLS, you can ignore this property.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `certFile` | `string` | `certFile` defines the path to the certificate file name within the config map or secret. |
| `certKey` | `string` | `certKey` defines the path to the certificate private key file name within the config map or secret. Omit when the key is not necessary. |
| `name` | `string` | Name of the config map or secret containing certificates. |
| `namespace` | `string` | Namespace of the config map or secret containing certificates. If omitted, the default is to use the same namespace as where Network Observability is deployed. If the namespace is different, the config map or the secret is copied so that it can be mounted as required. |
| `type` | `string` | Type for the certificate reference: `configmap` or `secret`. |
