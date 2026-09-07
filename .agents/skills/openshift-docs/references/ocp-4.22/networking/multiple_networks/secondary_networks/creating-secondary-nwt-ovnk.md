<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

As a cluster administrator, you can configure a secondary network for your cluster by using the `NetworkAttachmentDefinition` (NAD) resource.

# Configuration for an OVN-Kubernetes secondary network

The Red Hat OpenShift Networking OVN-Kubernetes network plugin allows the configuration of secondary network interfaces for pods. To configure secondary network interfaces, you must define the configurations in the `NetworkAttachmentDefinition` custom resource definition (CRD).

> [!NOTE]
> Pod and multi-network policy creation might remain in a pending state until the OVN-Kubernetes control plane agent in the nodes processes the associated `network-attachment-definition` CRD.

You can configure an OVN-Kubernetes secondary network in layer 2, layer 3, or localnet topologies. For more information about features supported on these topologies, see "UserDefinedNetwork and NetworkAttachmentDefinition support matrix".

The following sections provide example configurations for each of the topologies that OVN-Kubernetes currently allows for secondary networks.

> [!NOTE]
> Networks names must be unique. For example, creating multiple `NetworkAttachmentDefinition` CRDs with different configurations that reference the same network is unsupported.

## Supported platforms for OVN-Kubernetes secondary network

You can use an OVN-Kubernetes secondary network with the following supported platforms:

- Bare metal

- IBM Power®

- IBM Z®

- IBM® LinuxONE

- VMware vSphere

- Red Hat OpenStack Platform (RHOSP)

## OVN-Kubernetes network plugin JSON configuration table

The OVN-Kubernetes network plugin JSON configuration object describes the configuration parameters for the OVN-Kubernetes CNI network plugin.

<table>
<caption>OVN-Kubernetes network plugin JSON configuration table</caption>
<colgroup>
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 60%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Field</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>cniVersion</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>The CNI specification version. The required value is <code>0.3.1</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>name</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>The name of the network. These networks are not namespaced. For example, a network named <code>l2-network</code> can be referenced by <code>NetworkAttachmentDefinition</code> custom resources (CRs) that exist in different namespaces. This configuration allows pods that use the <code>NetworkAttachmentDefinition</code> CR in different namespaces to communicate over the same secondary network. However, the <code>NetworkAttachmentDefinition</code> CRs must share the same network-specific parameters, such as <code>topology</code>, <code>subnets</code>, <code>mtu</code>, <code>excludeSubnets</code>, and <code>vlanID</code>. The <code>vlanID</code> parameter applies only when the <code>topology</code> field is set to <code>localnet</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>type</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>The name of the CNI plugin to configure. This value must be set to <code>ovn-k8s-cni-overlay</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>topology</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>The topological configuration for the network. Must be one of <code>layer2</code> or <code>localnet</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>subnets</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>The subnet to use for the network across the cluster.</p>
<p>For <code>"topology":"layer2"</code> deployments, IPv6 (<code>2001:DBB::/64</code>) and dual-stack (<code>192.168.100.0/24,2001:DBB::/64</code>) subnets are supported.</p>
<p>When omitted, the logical switch implementing the network only provides layer 2 communication, and users must configure IP addresses for the pods. Port security only prevents MAC spoofing.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>mtu</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>The maximum transmission unit (MTU). If you do not set a value, the Cluster Network Operator (CNO) sets a default MTU value by calculating the difference among the underlay MTU of the primary network interface, the overlay MTU of the pod network, such as the Geneve (Generic Network Virtualization Encapsulation), and byte capacity of any enabled features, such as IPsec.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>netAttachDefName</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>The metadata <code>namespace</code> and <code>name</code> of the network attachment definition CRD where this configuration is included. For example, if this configuration is defined in a <code>NetworkAttachmentDefinition</code> CRD in namespace <code>ns1</code> named <code>l2-network</code>, this should be set to <code>ns1/l2-network</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>excludeSubnets</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>A comma-separated list of CIDRs and IP addresses. IP addresses are removed from the assignable IP address pool and are never passed to the pods.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>vlanID</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p>If topology is set to <code>localnet</code>, the specified VLAN tag is assigned to traffic from this secondary network. The default is to not assign a VLAN tag.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>physicalNetworkName</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>If topology is set to <code>localnet</code>, you can reuse the same physical network mapping with multiple network overlays. Specifies the name of the physical network to which the OVN overlay connects. When omitted, the default value is the <code>name</code> of the <code>localnet</code> network. To isolate the different networks, ensure that a different VLAN tag is used when sharing the same physical network between overlays.</p></td>
</tr>
</tbody>
</table>

## Compatibility with multi-network policy

When defining a network policy, the network policy rules that can be used depend on whether the OVN-Kubernetes secondary network defines the `subnets` field.

The multi-network policy API, which is provided by the `MultiNetworkPolicy` custom resource definition (CRD) in the `k8s.cni.cncf.io` API group, is compatible with an OVN-Kubernetes secondary network.

Refer to the following table that details supported multi-network policy selectors that are based on a `subnets` CNI configuration:

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 70%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;"><code>subnets</code> field specified</th>
<th style="text-align: left;">Allowed multi-network policy selectors</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>Yes</p></td>
<td style="text-align: left;"><ul>
<li><p><code>podSelector</code> and <code>namespaceSelector</code></p></li>
<li><p><code>ipBlock</code></p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: left;"><p>No</p></td>
<td style="text-align: left;"><ul>
<li><p><code>ipBlock</code></p></li>
</ul></td>
</tr>
</tbody>
</table>

You can use the `k8s.v1.cni.cncf.io/policy-for` annotation on a `MultiNetworkPolicy` object to point to a `NetworkAttachmentDefinition` (NAD) custom resource (CR). The NAD CR defines the network to which the policy applies. The following example multi-network policy that uses a pod selector is valid only if the `subnets` field is defined in the secondary network CNI configuration for the secondary network named `blue2`:

``` yaml
apiVersion: k8s.cni.cncf.io/v1beta1
kind: MultiNetworkPolicy
metadata:
  name: allow-same-namespace
  annotations:
    k8s.v1.cni.cncf.io/policy-for: blue2
spec:
  podSelector:
  ingress:
  - from:
    - podSelector: {}
```

The following example uses the `ipBlock` network multi-network policy that is always valid for an OVN-Kubernetes secondary network:

<div class="formalpara">

<div class="title">

Example multi-network policy that uses an IP block selector

</div>

``` yaml
apiVersion: k8s.cni.cncf.io/v1beta1
kind: MultiNetworkPolicy
metadata:
  name:  ingress-ipblock
  annotations:
    k8s.v1.cni.cncf.io/policy-for: default/flatl2net
spec:
  podSelector:
    matchLabels:
      name: access-control
  policyTypes:
  - Ingress
  ingress:
  - from:
    - ipBlock:
        cidr: 10.200.0.0/30
```

</div>

## Configuration for a localnet switched topology

The switched `localnet` topology interconnects the workloads created as Network Attachment Definitions (NADs) through a cluster-wide logical switch to a physical network.

> [!IMPORTANT]
> When creating multiple NADs, ensure that each NAD references a unique VLAN ID number. If two NADs reference the same VLAN ID, the OVN-Kubernetes network plugin experiences networking issues.

You must map a secondary network to the OVS bridge to use it as an OVN-Kubernetes secondary network. Bridge mappings allow network traffic to reach the physical network. A bridge mapping associates a physical network name, also known as an interface label, to a bridge created with Open vSwitch (OVS).

You can create an `NodeNetworkConfigurationPolicy` (NNCP) object, part of the `nmstate.io/v1` API group, to declaratively create the mapping. This API is provided by the NMState Operator. By using this API you can apply the bridge mapping to nodes that match your specified `nodeSelector` expression, such as `node-role.kubernetes.io/worker: ''`. With this declarative approach, the NMState Operator applies secondary network configuration to all nodes specified by the node selector automatically and transparently.

When attaching a secondary network, you can either use the existing `br-ex` bridge or create a new bridge. Which approach to use depends on your specific network infrastructure. Consider the following approaches:

- If your nodes include only a single network interface, you must use the existing bridge. This network interface is owned and managed by OVN-Kubernetes and you must not remove it from the `br-ex` bridge or alter the interface configuration. If you remove or alter the network interface, your cluster network stops working correctly.

- If your nodes include several network interfaces, you can attach a different network interface to a new bridge, and use that for your secondary network. This approach provides for traffic isolation from your primary cluster network.

> [!NOTE]
> You cannot make configuration changes to the `br-ex` bridge or its underlying interfaces in the `NodeNetworkConfigurationPolicy` (NNCP) resource as a postinstallation task. As a workaround, use a secondary network interface connected to your host or switch.

The `localnet1` network is mapped to the `br-ex` bridge in the following sharing-a-bridge example:

``` yaml
apiVersion: nmstate.io/v1
kind: NodeNetworkConfigurationPolicy
metadata:
  name: mapping
spec:
  nodeSelector:
    node-role.kubernetes.io/worker: ''
  desiredState:
    ovn:
      bridge-mappings:
      - localnet: localnet1
        bridge: br-ex
        state: present
```

where:

`metadata.name`
The name for the configuration object.

`spec.nodeSelector.node-role.kubernetes.io/worker`
A node selector that specifies the nodes to apply the node network configuration policy to.

`spec.desiredState.ovn.bridge-mappings.localnet`
The name for the secondary network from which traffic is forwarded to the OVS bridge. This secondary network must match the name of the `spec.config.name` field of the `NetworkAttachmentDefinition` CRD that defines the OVN-Kubernetes secondary network.

`spec.desiredState.ovn.bridge-mappings.bridge`
The name of the OVS bridge on the node. This value is required only if you specify `state: present`.

`spec.desiredState.ovn.bridge-mappings.state`
The state for the mapping. Must be either `present` to add the bridge or `absent` to remove the bridge. The default value is `present`.

The following JSON example configures a localnet secondary network that is named `localnet1`. Note that the value for the `mtu` parameter must match the MTU value that was set for the secondary network interface that is mapped to the `br-ex` bridge interface.

``` json
{
  "cniVersion": "0.3.1",
  "name": "localnet1",
  "type": "ovn-k8s-cni-overlay",
  "topology":"localnet",
  "physicalNetworkName": "localnet1",
  "subnets": "202.10.130.112/28",
  "vlanID": 33,
  "mtu": 1500,
  "netAttachDefName": "ns1/localnet-network",
  "excludeSubnets": "10.100.200.0/29"
}
```

In the following multiple interfaces example, the `localnet2` network interface is attached to the `ovs-br1` bridge. Through this attachment, the network interface is available to the OVN-Kubernetes network plugin as a secondary network.

``` yaml
apiVersion: nmstate.io/v1
kind: NodeNetworkConfigurationPolicy
metadata:
  name: ovs-br1-multiple-networks
spec:
  nodeSelector:
    node-role.kubernetes.io/worker: ''
  desiredState:
    interfaces:
    - name: ovs-br1
      description: |-
        A dedicated OVS bridge with eth1 as a port
        allowing all VLANs and untagged traffic
      type: ovs-bridge
      state: up
      bridge:
        allow-extra-patch-ports: true
        options:
          stp: false
          mcast-snooping-enable: true
        port:
        - name: eth1
    ovn:
      bridge-mappings:
      - localnet: localnet2
        bridge: ovs-br1
        state: present
```

where:

`metadata.name`
Specifies the name of the configuration object.

`node-role.kubernetes.io/worker`
Specifies a node selector that identifies the nodes to which the node network configuration policy applies.

`desiredState.interfaces.name`
Specifies a new OVS bridge that operates separately from the default bridge used by OVN-Kubernetes for cluster traffic.

`options.mcast-snooping-enable`
Specifies whether to enable multicast snooping. When enabled, multicast snooping prevents network devices from flooding multicast traffic to all network members. By default, an OVS bridge does not enable multicast snooping. The default value is `false`.

`bridge.port.name`
Specifies the network device on the host system to associate with the new OVS bridge.

`ovn.bridge-mappings.localnet`
Specifies the name of the secondary network that forwards traffic to the OVS bridge. This name must match the value of the `spec.config.name` field in the `NetworkAttachmentDefinition` CRD that defines the OVN-Kubernetes secondary network.

`ovn.bridge-mappings.bridge`
Specifies the name of the OVS bridge on the node. The value is required only when `state: present` is set.

`ovn.bridge-mappings.state`
Specifies the state of the mapping. Valid values are `present` to add the bridge or `absent` to remove the bridge. The default value is `present`.

The following JSON example configures a localnet secondary network that is named `localnet2`. Note that the value for the `mtu` parameter must match the MTU value that was set for the `eth1` secondary network interface.

``` json
{
  "cniVersion": "0.3.1",
  "name": "localnet2",
  "type": "ovn-k8s-cni-overlay",
  "topology":"localnet",
  "physicalNetworkName": "localnet2",
  "subnets": "202.10.130.112/28",
  "vlanID": 33,
  "mtu": 1500,
  "netAttachDefName": "ns1/localnet-network",
  "excludeSubnets": "10.100.200.0/29"
}
```

### Configuration for a layer 2 switched topology

The switched (layer 2) topology networks interconnect the workloads through a cluster-wide logical switch. This configuration can be used for IPv6 and dual-stack deployments.

> [!NOTE]
> Layer 2 switched topology networks only allow for the transfer of data packets between pods within a cluster.

The following JSON example configures a switched secondary network:

``` json
{
  "cniVersion": "0.3.1",
  "name": "l2-network",
  "type": "ovn-k8s-cni-overlay",
  "topology":"layer2",
  "subnets": "10.100.200.0/24",
  "mtu": 1300,
  "netAttachDefName": "ns1/l2-network",
  "excludeSubnets": "10.100.200.0/29"
}
```

## Configuring pods for secondary networks

You must specify the secondary network attachments through the `k8s.v1.cni.cncf.io/networks` annotation.

The following example provisions a pod with two secondary attachments, one for each of the attachment configurations presented in this guide:

``` yaml
apiVersion: v1
kind: Pod
metadata:
  annotations:
    k8s.v1.cni.cncf.io/networks: l2-network
  name: tinypod
  namespace: ns1
spec:
  containers:
  - args:
    - pause
    image: k8s.gcr.io/e2e-test-images/agnhost:2.36
    imagePullPolicy: IfNotPresent
    name: agnhost-container
```

## Configuring pods with a static IP address

You can configure pods with a static IP address. The example in the procedure provisions a pod with a static IP address.

<div class="note">

<div class="title">

</div>

- You can specify the IP address for the secondary network attachment of a pod only when the secondary network attachment, a namespaced-scoped object, uses a layer 2 or localnet topology.

- Specifying a static IP address for the pod is only possible when the attachment configuration does not feature subnets.

</div>

``` yaml
apiVersion: v1
kind: Pod
metadata:
  annotations:
    k8s.v1.cni.cncf.io/networks: '[
      {
        "name": "l2-network",
        "mac": "02:03:04:05:06:07",
        "interface": "myiface1",
        "ips": [
          "192.0.2.20/24"
          ]
      }
    ]'
  name: tinypod
  namespace: ns1
spec:
  containers:
  - args:
    - pause
    image: k8s.gcr.io/e2e-test-images/agnhost:2.36
    imagePullPolicy: IfNotPresent
    name: agnhost-container
```

where:

`k8s.v1.cni.cncf.io/networks.name`
The name of the network. This value must be unique across all `NetworkAttachmentDefinition` CRDs.

`k8s.v1.cni.cncf.io/networks.mac`
The MAC address to be assigned for the interface.

`k8s.v1.cni.cncf.io/networks.interface`
The name of the network interface to be created for the pod.

`k8s.v1.cni.cncf.io/networks.ips`
The IP addresses to be assigned to the network interface.
