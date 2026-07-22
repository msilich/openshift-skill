<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Review the specifications for the network flow format, which is used internally and for exporting flow data to Kafka.

# Network Flows format reference

This is the specification of the network flows format. That format is used when a Kafka exporter is configured, for Prometheus metrics labels as well as internally for the Loki store.

The "Filter ID" column shows which related name to use when defining Quick Filters (see `spec.consolePlugin.quickFilters` in the `FlowCollector` specification).

The "Loki label" column is useful when querying Loki directly: label fields need to be selected using [stream selectors](https://grafana.com/docs/loki/latest/logql/log_queries/#log-stream-selector).

The "Cardinality" column gives information about the implied metric cardinality if this field was to be used as a Prometheus label with the `FlowMetrics` API. Refer to the `FlowMetrics` documentation for more information on using this API.

<table style="width:100%;">
<colgroup>
<col style="width: 11%" />
<col style="width: 11%" />
<col style="width: 33%" />
<col style="width: 11%" />
<col style="width: 11%" />
<col style="width: 11%" />
<col style="width: 11%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Name</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Description</th>
<th style="text-align: left;">Filter ID</th>
<th style="text-align: left;">Loki label</th>
<th style="text-align: left;">Cardinality</th>
<th style="text-align: left;">OpenTelemetry</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>Bytes</code></p></td>
<td style="text-align: left;"><p>number</p></td>
<td style="text-align: left;"><p>Number of bytes</p></td>
<td style="text-align: left;"><p>n/a</p></td>
<td style="text-align: left;"><p>no</p></td>
<td style="text-align: left;"><p>avoid</p></td>
<td style="text-align: left;"><p>bytes</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>DnsErrno</code></p></td>
<td style="text-align: left;"><p>number</p></td>
<td style="text-align: left;"><p>Error number returned from DNS tracker ebpf hook function</p></td>
<td style="text-align: left;"><p><code>dns_errno</code></p></td>
<td style="text-align: left;"><p>no</p></td>
<td style="text-align: left;"><p>fine</p></td>
<td style="text-align: left;"><p>dns.errno</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>DnsFlags</code></p></td>
<td style="text-align: left;"><p>number</p></td>
<td style="text-align: left;"><p>DNS flags for DNS record</p></td>
<td style="text-align: left;"><p>n/a</p></td>
<td style="text-align: left;"><p>no</p></td>
<td style="text-align: left;"><p>fine</p></td>
<td style="text-align: left;"><p>dns.flags</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>DnsFlagsResponseCode</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p>Parsed DNS header RCODEs name</p></td>
<td style="text-align: left;"><p><code>dns_flag_response_code</code></p></td>
<td style="text-align: left;"><p>no</p></td>
<td style="text-align: left;"><p>fine</p></td>
<td style="text-align: left;"><p>dns.responsecode</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>DnsId</code></p></td>
<td style="text-align: left;"><p>number</p></td>
<td style="text-align: left;"><p>DNS record id</p></td>
<td style="text-align: left;"><p><code>dns_id</code></p></td>
<td style="text-align: left;"><p>no</p></td>
<td style="text-align: left;"><p>avoid</p></td>
<td style="text-align: left;"><p>dns.id</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>DnsLatencyMs</code></p></td>
<td style="text-align: left;"><p>number</p></td>
<td style="text-align: left;"><p>Time between a DNS request and response, in milliseconds</p></td>
<td style="text-align: left;"><p><code>dns_latency</code></p></td>
<td style="text-align: left;"><p>no</p></td>
<td style="text-align: left;"><p>avoid</p></td>
<td style="text-align: left;"><p>dns.latency</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>DnsName</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p>DNS queried name</p></td>
<td style="text-align: left;"><p><code>dns_name</code></p></td>
<td style="text-align: left;"><p>no</p></td>
<td style="text-align: left;"><p>careful</p></td>
<td style="text-align: left;"><p>dns.name</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>Dscp</code></p></td>
<td style="text-align: left;"><p>number</p></td>
<td style="text-align: left;"><p>Differentiated Services Code Point (DSCP) value</p></td>
<td style="text-align: left;"><p><code>dscp</code></p></td>
<td style="text-align: left;"><p>no</p></td>
<td style="text-align: left;"><p>fine</p></td>
<td style="text-align: left;"><p>dscp</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>DstAddr</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p>Destination IP address (ipv4 or ipv6)</p></td>
<td style="text-align: left;"><p><code>dst_address</code></p></td>
<td style="text-align: left;"><p>no</p></td>
<td style="text-align: left;"><p>avoid</p></td>
<td style="text-align: left;"><p>destination.address</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>DstK8S_HostIP</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p>Destination node IP</p></td>
<td style="text-align: left;"><p><code>dst_host_address</code></p></td>
<td style="text-align: left;"><p>no</p></td>
<td style="text-align: left;"><p>fine</p></td>
<td style="text-align: left;"><p>destination.k8s.host.address</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>DstK8S_HostName</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p>Destination node name</p></td>
<td style="text-align: left;"><p><code>dst_host_name</code></p></td>
<td style="text-align: left;"><p>no</p></td>
<td style="text-align: left;"><p>fine</p></td>
<td style="text-align: left;"><p>destination.k8s.host.name</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>DstK8S_Name</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p>Name of the destination Kubernetes object, such as Pod name, Service name or Node name.</p></td>
<td style="text-align: left;"><p><code>dst_name</code></p></td>
<td style="text-align: left;"><p>no</p></td>
<td style="text-align: left;"><p>careful</p></td>
<td style="text-align: left;"><p>destination.k8s.name</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>DstK8S_Namespace</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p>Destination namespace</p></td>
<td style="text-align: left;"><p><code>dst_namespace</code></p></td>
<td style="text-align: left;"><p>yes</p></td>
<td style="text-align: left;"><p>fine</p></td>
<td style="text-align: left;"><p>destination.k8s.namespace.name</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>DstK8S_NetworkName</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p>Destination network name</p></td>
<td style="text-align: left;"><p><code>dst_network</code></p></td>
<td style="text-align: left;"><p>no</p></td>
<td style="text-align: left;"><p>fine</p></td>
<td style="text-align: left;"><p>destination.network.name</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>DstK8S_OwnerName</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p>Name of the destination owner, such as Deployment name, StatefulSet name, etc.</p></td>
<td style="text-align: left;"><p><code>dst_owner_name</code></p></td>
<td style="text-align: left;"><p>yes</p></td>
<td style="text-align: left;"><p>fine</p></td>
<td style="text-align: left;"><p>destination.k8s.owner.name</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>DstK8S_OwnerType</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p>Kind of the destination owner, such as Deployment, StatefulSet, etc.</p></td>
<td style="text-align: left;"><p><code>dst_kind</code></p></td>
<td style="text-align: left;"><p>no</p></td>
<td style="text-align: left;"><p>fine</p></td>
<td style="text-align: left;"><p>destination.k8s.owner.kind</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>DstK8S_Type</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p>Kind of the destination Kubernetes object, such as Pod, Service or Node.</p></td>
<td style="text-align: left;"><p><code>dst_kind</code></p></td>
<td style="text-align: left;"><p>yes</p></td>
<td style="text-align: left;"><p>fine</p></td>
<td style="text-align: left;"><p>destination.k8s.kind</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>DstK8S_Zone</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p>Destination availability zone</p></td>
<td style="text-align: left;"><p><code>dst_zone</code></p></td>
<td style="text-align: left;"><p>yes</p></td>
<td style="text-align: left;"><p>fine</p></td>
<td style="text-align: left;"><p>destination.zone</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>DstMac</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p>Destination MAC address</p></td>
<td style="text-align: left;"><p><code>dst_mac</code></p></td>
<td style="text-align: left;"><p>no</p></td>
<td style="text-align: left;"><p>avoid</p></td>
<td style="text-align: left;"><p>destination.mac</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>DstPort</code></p></td>
<td style="text-align: left;"><p>number</p></td>
<td style="text-align: left;"><p>Destination port</p></td>
<td style="text-align: left;"><p><code>dst_port</code></p></td>
<td style="text-align: left;"><p>no</p></td>
<td style="text-align: left;"><p>careful</p></td>
<td style="text-align: left;"><p>destination.port</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>DstSubnetLabel</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p>Destination subnet label</p></td>
<td style="text-align: left;"><p><code>dst_subnet_label</code></p></td>
<td style="text-align: left;"><p>no</p></td>
<td style="text-align: left;"><p>fine</p></td>
<td style="text-align: left;"><p>destination.subnet.label</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>Flags</code></p></td>
<td style="text-align: left;"><p>string[]</p></td>
<td style="text-align: left;"><p>List of TCP flags comprised in the flow, according to RFC-9293, with additional custom flags to represent the following per-packet combinations:<br />
- SYN_ACK<br />
- FIN_ACK<br />
- RST_ACK</p></td>
<td style="text-align: left;"><p><code>tcp_flags</code></p></td>
<td style="text-align: left;"><p>no</p></td>
<td style="text-align: left;"><p>careful</p></td>
<td style="text-align: left;"><p>tcp.flags</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>FlowDirection</code></p></td>
<td style="text-align: left;"><p>number</p></td>
<td style="text-align: left;"><p>Flow interpreted direction from the node observation point. Can be one of:<br />
- 0: Ingress (incoming traffic, from the node observation point)<br />
- 1: Egress (outgoing traffic, from the node observation point)<br />
- 2: Inner (with the same source and destination node)</p></td>
<td style="text-align: left;"><p><code>node_direction</code></p></td>
<td style="text-align: left;"><p>yes</p></td>
<td style="text-align: left;"><p>fine</p></td>
<td style="text-align: left;"><p>host.direction</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>IPSecStatus</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p>Status of the IPsec encryption (on egress, given by the kernel xfrm_output function) or decryption (on ingress, via xfrm_input)</p></td>
<td style="text-align: left;"><p><code>ipsec_status</code></p></td>
<td style="text-align: left;"><p>no</p></td>
<td style="text-align: left;"><p>fine</p></td>
<td style="text-align: left;"><p>ipsec.status</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>IcmpCode</code></p></td>
<td style="text-align: left;"><p>number</p></td>
<td style="text-align: left;"><p>ICMP code</p></td>
<td style="text-align: left;"><p><code>icmp_code</code></p></td>
<td style="text-align: left;"><p>no</p></td>
<td style="text-align: left;"><p>fine</p></td>
<td style="text-align: left;"><p>icmp.code</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>IcmpType</code></p></td>
<td style="text-align: left;"><p>number</p></td>
<td style="text-align: left;"><p>ICMP type</p></td>
<td style="text-align: left;"><p><code>icmp_type</code></p></td>
<td style="text-align: left;"><p>no</p></td>
<td style="text-align: left;"><p>fine</p></td>
<td style="text-align: left;"><p>icmp.type</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>IfDirections</code></p></td>
<td style="text-align: left;"><p>number[]</p></td>
<td style="text-align: left;"><p>Flow directions from the network interface observation point. Can be one of:<br />
- 0: Ingress (interface incoming traffic)<br />
- 1: Egress (interface outgoing traffic)</p></td>
<td style="text-align: left;"><p><code>ifdirections</code></p></td>
<td style="text-align: left;"><p>no</p></td>
<td style="text-align: left;"><p>fine</p></td>
<td style="text-align: left;"><p>interface.directions</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>Interfaces</code></p></td>
<td style="text-align: left;"><p>string[]</p></td>
<td style="text-align: left;"><p>Network interfaces</p></td>
<td style="text-align: left;"><p><code>interfaces</code></p></td>
<td style="text-align: left;"><p>no</p></td>
<td style="text-align: left;"><p>careful</p></td>
<td style="text-align: left;"><p>interface.names</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>K8S_ClusterName</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p>Cluster name or identifier</p></td>
<td style="text-align: left;"><p><code>cluster_name</code></p></td>
<td style="text-align: left;"><p>yes</p></td>
<td style="text-align: left;"><p>fine</p></td>
<td style="text-align: left;"><p>k8s.cluster.name</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>K8S_FlowLayer</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p>Flow layer: 'app' or 'infra'</p></td>
<td style="text-align: left;"><p><code>flow_layer</code></p></td>
<td style="text-align: left;"><p>yes</p></td>
<td style="text-align: left;"><p>fine</p></td>
<td style="text-align: left;"><p>k8s.layer</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>NetworkEvents</code></p></td>
<td style="text-align: left;"><p>object[]</p></td>
<td style="text-align: left;"><p>Network events, such as network policy actions, composed of nested fields:<br />
- Feature (such as "acl" for network policies)<br />
- Type (such as an "AdminNetworkPolicy")<br />
- Namespace (namespace where the event applies, if any)<br />
- Name (name of the resource that triggered the event)<br />
- Action (such as "allow" or "drop")<br />
- Direction (Ingress or Egress)</p></td>
<td style="text-align: left;"><p><code>network_events</code></p></td>
<td style="text-align: left;"><p>no</p></td>
<td style="text-align: left;"><p>avoid</p></td>
<td style="text-align: left;"><p>n/a</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>Packets</code></p></td>
<td style="text-align: left;"><p>number</p></td>
<td style="text-align: left;"><p>Number of packets</p></td>
<td style="text-align: left;"><p>n/a</p></td>
<td style="text-align: left;"><p>no</p></td>
<td style="text-align: left;"><p>avoid</p></td>
<td style="text-align: left;"><p>packets</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>PktDropBytes</code></p></td>
<td style="text-align: left;"><p>number</p></td>
<td style="text-align: left;"><p>Number of bytes dropped by the kernel</p></td>
<td style="text-align: left;"><p>n/a</p></td>
<td style="text-align: left;"><p>no</p></td>
<td style="text-align: left;"><p>avoid</p></td>
<td style="text-align: left;"><p>drops.bytes</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>PktDropLatestDropCause</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p>Latest drop cause</p></td>
<td style="text-align: left;"><p><code>pkt_drop_cause</code></p></td>
<td style="text-align: left;"><p>no</p></td>
<td style="text-align: left;"><p>fine</p></td>
<td style="text-align: left;"><p>drops.latestcause</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>PktDropLatestFlags</code></p></td>
<td style="text-align: left;"><p>number</p></td>
<td style="text-align: left;"><p>TCP flags on last dropped packet</p></td>
<td style="text-align: left;"><p>n/a</p></td>
<td style="text-align: left;"><p>no</p></td>
<td style="text-align: left;"><p>fine</p></td>
<td style="text-align: left;"><p>drops.latestflags</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>PktDropLatestState</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p>TCP state on last dropped packet</p></td>
<td style="text-align: left;"><p><code>pkt_drop_state</code></p></td>
<td style="text-align: left;"><p>no</p></td>
<td style="text-align: left;"><p>fine</p></td>
<td style="text-align: left;"><p>drops.lateststate</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>PktDropPackets</code></p></td>
<td style="text-align: left;"><p>number</p></td>
<td style="text-align: left;"><p>Number of packets dropped by the kernel</p></td>
<td style="text-align: left;"><p>n/a</p></td>
<td style="text-align: left;"><p>no</p></td>
<td style="text-align: left;"><p>avoid</p></td>
<td style="text-align: left;"><p>drops.packets</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>Proto</code></p></td>
<td style="text-align: left;"><p>number</p></td>
<td style="text-align: left;"><p>L4 protocol</p></td>
<td style="text-align: left;"><p><code>protocol</code></p></td>
<td style="text-align: left;"><p>no</p></td>
<td style="text-align: left;"><p>fine</p></td>
<td style="text-align: left;"><p>protocol</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>Sampling</code></p></td>
<td style="text-align: left;"><p>number</p></td>
<td style="text-align: left;"><p>Sampling interval used for this flow</p></td>
<td style="text-align: left;"><p>n/a</p></td>
<td style="text-align: left;"><p>no</p></td>
<td style="text-align: left;"><p>fine</p></td>
<td style="text-align: left;"><p>n/a</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>SrcAddr</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p>Source IP address (ipv4 or ipv6)</p></td>
<td style="text-align: left;"><p><code>src_address</code></p></td>
<td style="text-align: left;"><p>no</p></td>
<td style="text-align: left;"><p>avoid</p></td>
<td style="text-align: left;"><p>source.address</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>SrcK8S_HostIP</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p>Source node IP</p></td>
<td style="text-align: left;"><p><code>src_host_address</code></p></td>
<td style="text-align: left;"><p>no</p></td>
<td style="text-align: left;"><p>fine</p></td>
<td style="text-align: left;"><p>source.k8s.host.address</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>SrcK8S_HostName</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p>Source node name</p></td>
<td style="text-align: left;"><p><code>src_host_name</code></p></td>
<td style="text-align: left;"><p>no</p></td>
<td style="text-align: left;"><p>fine</p></td>
<td style="text-align: left;"><p>source.k8s.host.name</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>SrcK8S_Name</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p>Name of the source Kubernetes object, such as Pod name, Service name or Node name.</p></td>
<td style="text-align: left;"><p><code>src_name</code></p></td>
<td style="text-align: left;"><p>no</p></td>
<td style="text-align: left;"><p>careful</p></td>
<td style="text-align: left;"><p>source.k8s.name</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>SrcK8S_Namespace</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p>Source namespace</p></td>
<td style="text-align: left;"><p><code>src_namespace</code></p></td>
<td style="text-align: left;"><p>yes</p></td>
<td style="text-align: left;"><p>fine</p></td>
<td style="text-align: left;"><p>source.k8s.namespace.name</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>SrcK8S_NetworkName</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p>Source network name</p></td>
<td style="text-align: left;"><p><code>src_network</code></p></td>
<td style="text-align: left;"><p>no</p></td>
<td style="text-align: left;"><p>fine</p></td>
<td style="text-align: left;"><p>source.network.name</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>SrcK8S_OwnerName</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p>Name of the source owner, such as Deployment name, StatefulSet name, etc.</p></td>
<td style="text-align: left;"><p><code>src_owner_name</code></p></td>
<td style="text-align: left;"><p>yes</p></td>
<td style="text-align: left;"><p>fine</p></td>
<td style="text-align: left;"><p>source.k8s.owner.name</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>SrcK8S_OwnerType</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p>Kind of the source owner, such as Deployment, StatefulSet, etc.</p></td>
<td style="text-align: left;"><p><code>src_kind</code></p></td>
<td style="text-align: left;"><p>no</p></td>
<td style="text-align: left;"><p>fine</p></td>
<td style="text-align: left;"><p>source.k8s.owner.kind</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>SrcK8S_Type</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p>Kind of the source Kubernetes object, such as Pod, Service or Node.</p></td>
<td style="text-align: left;"><p><code>src_kind</code></p></td>
<td style="text-align: left;"><p>yes</p></td>
<td style="text-align: left;"><p>fine</p></td>
<td style="text-align: left;"><p>source.k8s.kind</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>SrcK8S_Zone</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p>Source availability zone</p></td>
<td style="text-align: left;"><p><code>src_zone</code></p></td>
<td style="text-align: left;"><p>yes</p></td>
<td style="text-align: left;"><p>fine</p></td>
<td style="text-align: left;"><p>source.zone</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>SrcMac</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p>Source MAC address</p></td>
<td style="text-align: left;"><p><code>src_mac</code></p></td>
<td style="text-align: left;"><p>no</p></td>
<td style="text-align: left;"><p>avoid</p></td>
<td style="text-align: left;"><p>source.mac</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>SrcPort</code></p></td>
<td style="text-align: left;"><p>number</p></td>
<td style="text-align: left;"><p>Source port</p></td>
<td style="text-align: left;"><p><code>src_port</code></p></td>
<td style="text-align: left;"><p>no</p></td>
<td style="text-align: left;"><p>careful</p></td>
<td style="text-align: left;"><p>source.port</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>SrcSubnetLabel</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p>Source subnet label</p></td>
<td style="text-align: left;"><p><code>src_subnet_label</code></p></td>
<td style="text-align: left;"><p>no</p></td>
<td style="text-align: left;"><p>fine</p></td>
<td style="text-align: left;"><p>source.subnet.label</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>TLSCipherSuite</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p>TLS cipher suite</p></td>
<td style="text-align: left;"><p><code>tls_cipher_suite</code></p></td>
<td style="text-align: left;"><p>no</p></td>
<td style="text-align: left;"><p>fine</p></td>
<td style="text-align: left;"><p>tls.ciphersuite</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>TLSGroup</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p>TLS group name</p></td>
<td style="text-align: left;"><p><code>tls_group</code></p></td>
<td style="text-align: left;"><p>no</p></td>
<td style="text-align: left;"><p>fine</p></td>
<td style="text-align: left;"><p>tls.group</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>TLSTypes</code></p></td>
<td style="text-align: left;"><p>string[]</p></td>
<td style="text-align: left;"><p>TLS message types (bitfield)</p></td>
<td style="text-align: left;"><p><code>tls_types</code></p></td>
<td style="text-align: left;"><p>no</p></td>
<td style="text-align: left;"><p>careful</p></td>
<td style="text-align: left;"><p>tls.types</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>TLSVersion</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p>TLS version</p></td>
<td style="text-align: left;"><p><code>tls_version</code></p></td>
<td style="text-align: left;"><p>no</p></td>
<td style="text-align: left;"><p>fine</p></td>
<td style="text-align: left;"><p>tls.version</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>TimeFlowEndMs</code></p></td>
<td style="text-align: left;"><p>number</p></td>
<td style="text-align: left;"><p>End timestamp of this flow, in milliseconds</p></td>
<td style="text-align: left;"><p>n/a</p></td>
<td style="text-align: left;"><p>no</p></td>
<td style="text-align: left;"><p>avoid</p></td>
<td style="text-align: left;"><p>timeflowend</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>TimeFlowRttNs</code></p></td>
<td style="text-align: left;"><p>number</p></td>
<td style="text-align: left;"><p>TCP Smoothed Round Trip Time (SRTT), in nanoseconds</p></td>
<td style="text-align: left;"><p><code>time_flow_rtt</code></p></td>
<td style="text-align: left;"><p>no</p></td>
<td style="text-align: left;"><p>avoid</p></td>
<td style="text-align: left;"><p>tcp.rtt</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>TimeFlowStartMs</code></p></td>
<td style="text-align: left;"><p>number</p></td>
<td style="text-align: left;"><p>Start timestamp of this flow, in milliseconds</p></td>
<td style="text-align: left;"><p>n/a</p></td>
<td style="text-align: left;"><p>no</p></td>
<td style="text-align: left;"><p>avoid</p></td>
<td style="text-align: left;"><p>timeflowstart</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>TimeReceived</code></p></td>
<td style="text-align: left;"><p>number</p></td>
<td style="text-align: left;"><p>Timestamp when this flow was received and processed by the flow collector, in seconds</p></td>
<td style="text-align: left;"><p>n/a</p></td>
<td style="text-align: left;"><p>no</p></td>
<td style="text-align: left;"><p>avoid</p></td>
<td style="text-align: left;"><p>timereceived</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>Udns</code></p></td>
<td style="text-align: left;"><p>string[]</p></td>
<td style="text-align: left;"><p>List of User Defined Networks</p></td>
<td style="text-align: left;"><p><code>udns</code></p></td>
<td style="text-align: left;"><p>no</p></td>
<td style="text-align: left;"><p>careful</p></td>
<td style="text-align: left;"><p>n/a</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>XlatDstAddr</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p>packet translation destination address</p></td>
<td style="text-align: left;"><p><code>xlat_dst_address</code></p></td>
<td style="text-align: left;"><p>no</p></td>
<td style="text-align: left;"><p>avoid</p></td>
<td style="text-align: left;"><p>n/a</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>XlatDstPort</code></p></td>
<td style="text-align: left;"><p>number</p></td>
<td style="text-align: left;"><p>packet translation destination port</p></td>
<td style="text-align: left;"><p><code>xlat_dst_port</code></p></td>
<td style="text-align: left;"><p>no</p></td>
<td style="text-align: left;"><p>careful</p></td>
<td style="text-align: left;"><p>n/a</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>XlatSrcAddr</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p>packet translation source address</p></td>
<td style="text-align: left;"><p><code>xlat_src_address</code></p></td>
<td style="text-align: left;"><p>no</p></td>
<td style="text-align: left;"><p>avoid</p></td>
<td style="text-align: left;"><p>n/a</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>XlatSrcPort</code></p></td>
<td style="text-align: left;"><p>number</p></td>
<td style="text-align: left;"><p>packet translation source port</p></td>
<td style="text-align: left;"><p><code>xlat_src_port</code></p></td>
<td style="text-align: left;"><p>no</p></td>
<td style="text-align: left;"><p>careful</p></td>
<td style="text-align: left;"><p>n/a</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>ZoneId</code></p></td>
<td style="text-align: left;"><p>number</p></td>
<td style="text-align: left;"><p>packet translation zone id</p></td>
<td style="text-align: left;"><p><code>xlat_zone_id</code></p></td>
<td style="text-align: left;"><p>no</p></td>
<td style="text-align: left;"><p>avoid</p></td>
<td style="text-align: left;"><p>n/a</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>_HashId</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p>In conversation tracking, the conversation identifier</p></td>
<td style="text-align: left;"><p><code>id</code></p></td>
<td style="text-align: left;"><p>no</p></td>
<td style="text-align: left;"><p>avoid</p></td>
<td style="text-align: left;"><p>n/a</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>_RecordType</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p>Type of record: <code>flowLog</code> for regular flow logs, or <code>newConnection</code>, <code>heartbeat</code>, <code>endConnection</code> for conversation tracking</p></td>
<td style="text-align: left;"><p><code>type</code></p></td>
<td style="text-align: left;"><p>yes</p></td>
<td style="text-align: left;"><p>fine</p></td>
<td style="text-align: left;"><p>n/a</p></td>
</tr>
</tbody>
</table>
