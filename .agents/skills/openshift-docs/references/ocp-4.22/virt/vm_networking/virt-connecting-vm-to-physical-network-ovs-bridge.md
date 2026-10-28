<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

You can connect a virtual machine (VM) to the physical network infrastructure by configuring an OVN-Kubernetes secondary user-defined network (UDN) with the localnet topology.

By configuring the `ClusterUserDefinedNetwork` custom resource (CR), you can select the projects that have access to the physical network and assign VLANs to projects.

# Localnet topology for OVS bridge networks

A localnet topology connects the secondary network to the physical network. This enables both east-west cluster traffic and access to services running outside the cluster, but it requires additional configuration of the underlying Open vSwitch (OVS) bridge on cluster nodes.

To configure a localnet UDN, use the following steps:

1.  Install the Kubernetes NMState Operator, which provides a state-driven network configuration across cluster nodes.

2.  Use the `NodeNetworkConfigurationPolicy` custom resource (CR) to configure OVS bridges and add the appropriate bridge mappings on the nodes.

3.  Use the `ClusterUserDefinedNetwork` CR from the UDN API to attach your workload to the physical network through the OVS bridges that you configured in the previous step.

# Node network considerations for localnet

Before attaching a VM to the physical network by using a localnet topology, you must prepare the node network by creating an Open vSwitch (OVS) bridge mapping.

> [!NOTE]
> In the OpenShift Container Platform web console, bridge mappings appear under **Networking** → **Physical networks**.

The following are key considerations when preparing the node network:

Uplink setup
The uplink connection determines how the network traffic enters and exits the node. You can either share the default machine network with VM traffic or use a dedicated network interface to connect to the physical network.

- Sharing the default machine network: You can achieve this by connecting your VM through the `br-ex` bridge by using a localnet network. This bridge and its underlying configuration must be defined during installation. For more information about creating a customized `br-ex` bridge, see "Postinstallation configuration" in the Additional resources section.

- Using a dedicated network interface: To prevent network congestion and isolate traffic, you can use a dedicated network interface controller (NIC) for the VM network. After installing your OpenShift Container Platform cluster, you can use the Kubernetes NMState Operator and the `NodeNetworkConfigurationPolicy` CR to create a bridge that maps localnet to the physical network.

<div class="formalpara">

<div class="title">

Example configuration of a secondary bridge with a single uplink interface

</div>

``` yaml
apiVersion: nmstate.io/v1
kind: NodeNetworkConfigurationPolicy
metadata:
  name: network-config
spec:
  desiredState:
    interfaces:
    - name: br1
      type: ovs-bridge
      state: up
      bridge:
       # ...
        port:
        - name: eno1np0
```

</div>

Bonding
Regardless of how the uplink connection is set up, run VM traffic over a bonded interface to increase resiliency. For details about supported bonding modes and their configuration, see "Which bonding modes work when used with a bridge that virtual machine guests or containers connect to?" in the Additional resources section.

> [!IMPORTANT]
> OpenShift Virtualization does not support linux bonding modes 0, 5, and 6. Bond mode 1 (`active-backup`) is only partially supported. For more information, see "Which bonding modes work when used with a bridge that virtual machine guests or containers connect to?" in the Additional resources section.

Node selection
By default, the node network configuration policy (NNCP) is applied to all nodes in the cluster. This works if your cluster nodes are homogeneous and each node has network interfaces of the same names connected to the same networks.

If your cluster is heterogeneous, you might need to apply multiple NNCPs, each selecting a group of nodes.

<div class="formalpara">

<div class="title">

Example `NodeNetworkConfigurationPolicy` manifests that target two different node groups

</div>

``` yaml
apiVersion: nmstate.io/v1
kind: NodeNetworkConfigurationPolicy
metadata:
  name: network-config-gen1
spec:
  nodeSelector:
    node-role.kubernetes.io/worker: gen1
  desiredState:
    interfaces:
    - name: br1
     # ...
      bridge:
       # ...
        port:
        - name: eno1np0
```

</div>

``` yaml
apiVersion: nmstate.io/v1
kind: NodeNetworkConfigurationPolicy
metadata:
  name: network-config-gen2
spec:
  nodeSelector:
    node-role.kubernetes.io/worker: gen2
  desiredState:
    interfaces:
    - name: br1
     # ...
      bridge:
      # ...
        port:
        - name: eno2np1
```

MTU configuration
During installation, the cluster network MTU is set automatically based on the primary network interface MTU of cluster nodes. Although you can change the cluster network MTU after installation, configure the MTU during cluster deployment if you are using a dedicated uplink.

If you created a custom bridge, set the desired MTU on the bridge uplink by using the `NodeNetworkConfigurationPolicy` manifest. For example:

``` yaml
apiVersion: nmstate.io/v1
kind: NodeNetworkConfigurationPolicy
metadata:
  name: network-config
spec:
  desiredState:
    interfaces:
    - name: eno1np0
      type: ethernet
      state: up
      mtu: 9000
    - name: br1
      type: ovs-bridge
      state: up
      bridge:
       # ...
        port:
        - name: eno1np0
```

> [!NOTE]
> If your cluster infrastructure can benefit from a higher MTU value for optimal performance, you must ensure that the VM, localnet network, the bridge uplink, and external routers and switches all support jumbo frames.

VM network requirements
To make the OVS bridge work when used for a VM network, set the following attributes in the `NodeNetworkConfigurationPolicy` CR:

- `allow-extra-patch-ports: true` to allow the creation of multiple OVS patch ports

- `stp: false` to allow VMs to live migrate between nodes

- `mcast-snooping-enable: true` to prevent flooding multicast packets to every port of the bridge

``` yaml
apiVersion: nmstate.io/v1
kind: NodeNetworkConfigurationPolicy
metadata:
  name: network-config
spec:
  desiredState:
    interfaces:
    - name: br1
      type: ovs-bridge
      state: up
      bridge:
        allow-extra-patch-ports: true
        options:
          stp: false
          mcast-snooping-enable: true
       # ...
```

Internal OVS interface
An OVS bridge acts as a virtual switch with virtual ports. The uplink port connects the bridge to the physical network through a NIC or bond. When the uplink is added to the bridge, the internal OVS interface takes over the MAC and IP addresses that the uplink interface previously held, representing the bridge on the host side. Even when no IP address is needed, the internal OVS interface is required for correct OVS operation.

The internal OVS interface is listed as one of the bridge ports in the `NodeNetworkConfigurationPolicy` manifest. Use the same name for the internal OVS interface as the OVS bridge.

``` yaml
apiVersion: nmstate.io/v1
kind: NodeNetworkConfigurationPolicy
metadata:
  name: network-config
spec:
  desiredState:
    interfaces:
    - name: br1
      type: ovs-bridge
      state: up
      bridge:
        port:
        - name: eno1np0
        - name: br1
    - name: br1
      type: ovs-interface
      state: up
      ipv4:
        enabled: false
      ipv6:
        enabled: false
```

Localnet identifier
To make the OVS bridge available for VM networks, the NNCP must include the `ovn.bridge-mappings.localnet` identifier. This attribute must match the value of the `spec.network.localnet.physicalNetworkName` field of the `ClusterUserDefinedNetwork` object that defines the custom localnet network.

``` yaml
apiVersion: nmstate.io/v1
kind: NodeNetworkConfigurationPolicy
metadata:
  name: network-config
spec:
  # ...
  desiredState:
    interfaces:
    - name: br1
      type: ovs-bridge
      state: up
     # ...
    ovn:
      bridge-mappings:
      - localnet: provider-network
        bridge: br1
        state: present
```

- `spec.desiredState.ovn.bridge-mappings.localnet` specifies the name of the localnet identifier. This value must match the `spec.network.localnet.physicalNetworkName` field of the `ClusterUserDefinedNetwork` CR.

- `spec.desiredState.ovn.bridge-mappings.bridge` specifies the name of the OVS bridge on the node.

- `spec.desiredState.ovn.bridge-mappings.state` specifies the state of the mapping. Must be `present` to add the mapping or `absent` to remove it.

# Recommended bonding modes for OVS bridges

You can run VM traffic over a bonded interface to increase resiliency. The following bonding modes are recommended when you configure an OVS bridge for a localnet network.

> [!NOTE]
> If you use the default machine network as the uplink connection, see "Postinstallation configuration" in the Additional resources section for Day 1 configuration.

Source load balancing (`balance-slb`)
This mode balances traffic from different VMs across the physical links based on the source MAC address and VLAN. It works without needing special switch support, making it useful when the physical switch is not configured for Link Aggregation Control Protocol (LACP).

<div class="formalpara">

<div class="title">

Example `NodeNetworkConfigurationPolicy` manifest with `balance-slb` bonding

</div>

``` yaml
apiVersion: nmstate.io/v1
kind: NodeNetworkConfigurationPolicy
metadata:
  name: network-config
spec:
  desiredState:
    interfaces:
    # ...
    - name: br1
      type: ovs-bridge
      state: up
      bridge:
        # ...
        port:
        - name: bond1
          link-aggregation:
            mode: balance-slb
            port:
              - name: eno1np0
              - name: eno2np1
```

</div>

LACP (mode 4 / IEEE 802.3ad)
Also known as Link Aggregation Control Protocol (LACP), this mode creates a single logical link from multiple physical interfaces for increased bandwidth and redundancy. This mode requires compatible switch configuration.

<div class="formalpara">

<div class="title">

Example `NodeNetworkConfigurationPolicy` manifest with `802.3ad` bonding

</div>

``` yaml
apiVersion: nmstate.io/v1
kind: NodeNetworkConfigurationPolicy
metadata:
  name: network-config
spec:
  desiredState:
    interfaces:
    # ...
    - name: bond1
      type: bond
      state: up
      link-aggregation:
        mode: 802.3ad
        port:
        - eno1np0
        - eno2np1
```

</div>

> [!IMPORTANT]
> OpenShift Virtualization does not support linux bonding modes 0, 5, and 6. Mode 1 is only partially supported. For more information, see "Which bonding modes work when used with a bridge that virtual machine guests or containers connect to?" in the Additional resources section.

# Create an OVS bridge mapping for a localnet network

You can prepare the node network for a localnet topology by creating a `NodeNetworkConfigurationPolicy` (NNCP) custom resource (CR) that configures an Open vSwitch (OVS) bridge and maps it to the physical network.

If you use a dedicated network interface for VM traffic, you must configure the full OVS bridge, including the uplink, internal interface, and bridge mapping. If you share the default machine network, you only need to add the bridge mapping to the existing `br-ex` bridge.

<div>

<div class="title">

Prerequisites

</div>

- You are logged in to the cluster as a user with `cluster-admin` privileges.

- You have installed the OpenShift CLI (`oc`).

- You have installed the Kubernetes NMState Operator.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create a `NodeNetworkConfigurationPolicy` manifest to configure the OVS bridge and map it to the physical network. The following example uses two dedicated uplink interfaces bonded with OVS `balance-slb` mode and configures jumbo frames.

    ``` yaml
    apiVersion: nmstate.io/v1
    kind: NodeNetworkConfigurationPolicy
    metadata:
      name: bridge-config-group-1
    spec:
      nodeSelector:
        vm-network-configuration: group-1
      desiredState:
        interfaces:
        - name: eno1np0
          type: ethernet
          state: up
          mtu: 9000
        - name: eno2np1
          type: ethernet
          state: up
          mtu: 9000
        - name: br1
          type: ovs-bridge
          state: up
          bridge:
            allow-extra-patch-ports: true
            options:
              stp: false
              mcast-snooping-enable: true
            port:
            - name: bond1
              link-aggregation:
                mode: balance-slb
                port:
                  - name: eno1np0
                  - name: eno2np1
            - name: br1
        - name: br1
          type: ovs-interface
          state: up
          mtu: 9000
          ipv4:
            enabled: false
          ipv6:
            enabled: false
        ovn:
          bridge-mappings:
          - localnet: provider-network
            bridge: br1
            state: present
    ```

    where:

    `spec.nodeSelector`
    Selects the nodes to which the node network configuration policy is applied. Use node selectors when your cluster has heterogeneous hardware where network interface names differ across node groups.

    `spec.desiredState.interfaces` (ethernet)
    Specifies the uplink interfaces and their MTU. Set the desired MTU on the uplink interfaces to match the physical network. In this example, jumbo frames are configured with an MTU of `9000`.

    `spec.desiredState.interfaces` (ovs-bridge)
    Specifies the OVS bridge configuration. The bridge name must match the name used in the `ovn.bridge-mappings.bridge` field.

    `bridge.allow-extra-patch-ports`
    Must be set to `true` to allow the creation of multiple OVS patch ports, which is required for VM networks.

    `bridge.options.stp`
    Must be set to `false` to allow VMs to live migrate between nodes.

    `bridge.options.mcast-snooping-enable`
    Set to `true` to prevent flooding multicast packets to every port on the bridge.

    `bridge.port` (link-aggregation)
    Specifies the bonding mode for the uplink interfaces. The `balance-slb` mode balances traffic based on source MAC address and VLAN without requiring special switch configuration.

    `spec.desiredState.interfaces` (ovs-interface)
    Specifies the internal OVS interface. This interface is required for correct OVS operation. Use the same name for the internal OVS interface as the OVS bridge.

    `ovn.bridge-mappings.localnet`
    Specifies the localnet identifier. This value must match the `spec.network.localnet.physicalNetworkName` field of the `ClusterUserDefinedNetwork` CR that defines the localnet network.

    `ovn.bridge-mappings.bridge`
    Specifies the name of the OVS bridge on the node.

    `ovn.bridge-mappings.state`
    Specifies the state of the mapping. Set to `present` to add the mapping or `absent` to remove it. The default value is `present`.

2.  Optional: If you share the default machine network with VM traffic instead of using a dedicated interface, the bridge and its uplinks are configured during cluster deployment. You only need to configure the bridge mapping. In this example, the machine network belongs to the native VLAN and the `br-ex` bridge is configured directly on the uplink, not on a VLAN sub-interface.

    ``` yaml
    apiVersion: nmstate.io/v1
    kind: NodeNetworkConfigurationPolicy
    metadata:
      name: network-config
    spec:
      desiredState:
        ovn:
          bridge-mappings:
          - localnet: provider-network
            bridge: br-ex
            state: present
    ```

3.  Apply the `NodeNetworkConfigurationPolicy` manifest by running the following command:

    ``` terminal
    $ oc apply -f <filename>.yaml
    ```

    where:

    `<filename>`
    Specifies the name of your `NodeNetworkConfigurationPolicy` manifest YAML file.

</div>

# Localnet network configuration considerations

After you configure the cluster node network, you can use the `ClusterUserDefinedNetwork` CR to create a localnet network that defines how VMs attach to the host-level bridge and any VLANs it provides.

By configuring the `ClusterUserDefinedNetwork` CR, you can select the projects that have access to the physical network and assign VLANs to projects.

The following are key attributes to specify when configuring the `ClusterUserDefinedNetwork` CR:

Physical network reference
The `ClusterUserDefinedNetwork` CR must reference the name of the localnet identifier that is configured on the node. This value must match the `spec.desiredState.ovn.bridge-mappings.localnet` field in the `NodeNetworkConfigurationPolicy` manifest that you previously created. This ensures that you are bridging to the intended physical network.

``` yaml
apiVersion: k8s.ovn.org/v1
kind: ClusterUserDefinedNetwork
metadata:
  name: provider-network
spec:
 # ...
  network:
    topology: Localnet
    localnet:
      physicalNetworkName: provider-network
    #  ...
```

> [!NOTE]
> If the physical network is configured only on a subset of the nodes, you must ensure that the VM is scheduled on the correct node. Otherwise, the VM will fail to start.

VLAN assignment
To isolate different tenants from each other, you can use unique VLANs for VMs instead of using the native network.

``` yaml
apiVersion: k8s.ovn.org/v1
kind: ClusterUserDefinedNetwork
metadata:
  name: provider-network-100
spec:
 # ...
  network:
   # ...
    localnet:
    #  ...
      vlan:
        mode: Access
        access:
          id: 100
```

> [!NOTE]
> If you have configured a VLAN sub-interface on the host, OVN-Kubernetes automatically handles VLAN tagging. OVN-Kubernetes currently does not support VLAN trunking.

Namespace selection
You can use one of the following three approaches to select which users or projects have access to the network.

- Namespaces by label: This is the recommended approach. You can use label selectors to select namespaces that the `ClusterUserDefinedNetwork` CR applies to. Namespaces can be granted or revoked access by adding or removing a label, without modifying the `ClusterUserDefinedNetwork` CR.

  ``` yaml
  apiVersion: k8s.ovn.org/v1
  kind: ClusterUserDefinedNetwork
  metadata:
    name: provider-network
  spec:
    namespaceSelector:
      matchLabels:
        provider-network-vlan: "100"
    network:
    # ...
  ```

  ``` yaml
  apiVersion: v1
  kind: Namespace
  metadata:
    name: red
    labels:
      provider-network-vlan: "100"
  ```

- All namespaces: To make the network available to all users in the cluster, create a `ClusterUserDefinedNetwork` CR that selects the `default` namespace.

  ``` yaml
  apiVersion: k8s.ovn.org/v1
  kind: ClusterUserDefinedNetwork
  metadata:
    name: provider-network
  spec:
    namespaceSelector:
      matchExpressions:
      - key: kubernetes.io/metadata.name
        operator: In
        values: ["default"]
    network:
    # ...
  ```

- Namespaces by name: You can specify the namespaces that have access to the network directly in the `ClusterUserDefinedNetwork` CR.

  ``` yaml
  apiVersion: k8s.ovn.org/v1
  kind: ClusterUserDefinedNetwork
  metadata:
    name: provider-network
  spec:
    namespaceSelector:
      matchExpressions:
      - key: kubernetes.io/metadata.name
        operator: In
        values: ["tenant-red", "tenant-blue"]
    network:
     # ...
  ```

  > [!IMPORTANT]
  > If you select namespaces by name and later need to delete one of those namespaces, the controller might get stuck in `Terminating` state. The `ClusterUserDefinedNetwork` controller cannot remove the network attachment from a namespace that is still explicitly listed in the selector. To successfully delete the namespace, you must first update the `ClusterUserDefinedNetwork` CR to remove the namespace from the list. To avoid this issue, consider selecting namespaces by label instead.

MTU configuration
The default MTU for a localnet network is 1500. To change it, set the `spec.network.localnet.mtu` attribute in the `ClusterUserDefinedNetwork` CR.

``` yaml
apiVersion: k8s.ovn.org/v1
kind: ClusterUserDefinedNetwork
metadata:
  name: provider-network-100
spec:
 # ...
  network:
   # ...
    localnet:
      mtu: 9000
    # ...
```

> [!NOTE]
> The MTU value for the localnet network must match the MTU of the node network and the physical network.

VM network requirements
OpenShift Virtualization does not support IP address management (IPAM) for VMs that use localnet networks. To make the localnet network work correctly as a VM network, set the `localnet.ipam.mode` attribute to `Disabled` in the `ClusterUserDefinedNetwork` CR.

``` yaml
apiVersion: k8s.ovn.org/v1
kind: ClusterUserDefinedNetwork
metadata:
  name: provider-network-100
spec:
 # ...
  network:
  #  ...
    localnet:
    #  ...
      ipam:
        mode: Disabled
```

# Define a localnet network

You can define a localnet network by creating a `ClusterUserDefinedNetwork` (CUDN) custom resource (CR) that specifies how virtual machines attach to the physical network through the OVS bridge, and which namespaces have access.

<div>

<div class="title">

Prerequisites

</div>

- You are logged in to the cluster as a user with `cluster-admin` privileges.

- You have installed the OpenShift CLI (`oc`).

- You have configured an OVS bridge mapping on the cluster nodes by creating a `NodeNetworkConfigurationPolicy` CR.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create a `ClusterUserDefinedNetwork` manifest to define the localnet network. The following example creates a localnet network on VLAN 100 with jumbo frames, accessible to namespaces labeled with `provider-network-vlan: "100"`.

    ``` yaml
    apiVersion: k8s.ovn.org/v1
    kind: ClusterUserDefinedNetwork
    metadata:
      name: provider-network-100
    spec:
      namespaceSelector:
        matchLabels:
          provider-network-vlan: "100"
      network:
        topology: Localnet
        localnet:
          role: Secondary
          physicalNetworkName: provider-network
          ipam:
            mode: Disabled
          mtu: 9000
          vlan:
            mode: Access
            access:
              id: 100
    ```

    where:

    `spec.namespaceSelector`
    Selects namespaces that have access to the network. You can use `matchLabels` or `matchExpressions` selectors. Using label selectors is recommended because namespaces can be granted or revoked access by adding or removing a label, without modifying the `ClusterUserDefinedNetwork` CR.

    > [!IMPORTANT]
    > If you select namespaces by name using `matchExpressions` and later need to delete one of those namespaces, the controller might get stuck in `Terminating` state. The `ClusterUserDefinedNetwork` controller cannot remove the network attachment from a namespace that is still explicitly listed in the selector. To successfully delete the namespace, you must first update the `ClusterUserDefinedNetwork` CR to remove the namespace from the list. To avoid this issue, select namespaces by label instead.

    `spec.network.topology`
    Specifies the topological configuration. Must be set to `Localnet` to connect the network to the physical underlay.

    `spec.network.localnet.role`
    Specifies the network role. Must be set to `Secondary` for localnet topology.

    `spec.network.localnet.physicalNetworkName`
    Specifies the name of the OVN-Kubernetes bridge mapping configured on the node. This value must match the `spec.desiredState.ovn.bridge-mappings.localnet` field in the `NodeNetworkConfigurationPolicy` manifest.

    `spec.network.localnet.ipam.mode`
    Specifies whether IP address management (IPAM) is enabled or disabled. Must be set to `Disabled` because OpenShift Virtualization does not support IPAM for VMs on localnet networks.

    `spec.network.localnet.mtu`
    Specifies the MTU for the localnet network. The default value is `1500`. This value must match the MTU of the node network and the physical network.

    `spec.network.localnet.vlan`
    Specifies the VLAN configuration. Set `mode` to `Access` and specify the VLAN ID to isolate traffic for different tenants.

    > [!NOTE]
    > OVN-Kubernetes does not support VLAN trunking.

2.  Apply the `ClusterUserDefinedNetwork` manifest by running the following command:

    ``` terminal
    $ oc apply -f <filename>.yaml
    ```

    where:

    `<filename>`
    Specifies the name of your `ClusterUserDefinedNetwork` manifest YAML file.

3.  Create a `Namespace` manifest with a label that matches the `ClusterUserDefinedNetwork` namespace selector, as in the following example:

    ``` yaml
    apiVersion: v1
    kind: Namespace
    metadata:
      name: red
      labels:
        provider-network-vlan: "100"
    ```

4.  Apply the `Namespace` manifest by running the following command:

    ``` terminal
    $ oc apply -f <filename>.yaml
    ```

    where:

    `<filename>`
    Specifies the name of your `Namespace` manifest YAML file.

</div>

# Attach a virtual machine to a localnet network

You can connect a virtual machine (VM) to the physical network by configuring the localnet network interface in the `VirtualMachine` manifest.

> [!NOTE]
> You can connect a VM to both the default pod network and a secondary localnet network.

<div>

<div class="title">

Prerequisites

</div>

- You have installed the OpenShift CLI (`oc`).

- You have created a `ClusterUserDefinedNetwork` CR that defines the localnet network.

- You have created a namespace with a label that matches the `ClusterUserDefinedNetwork` namespace selector.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Edit the `VirtualMachine` manifest to add the localnet network interface, as in the following example:

    ``` yaml
    apiVersion: kubevirt.io/v1
    kind: VirtualMachine
    metadata:
      name: example-vm
      namespace: red
    spec:
      template:
        spec:
          domain:
            devices:
        # ...
              interfaces:
              - name: provider-network  # must match networks.name
                bridge: {}
          networks:
          - name: provider-network
            multus:
              networkName: provider-network-100
    # ...
    ```

    > [!NOTE]
    > With a VirtIO driver, the VM automatically inherits the MTU value of the network. If you use the `e1000e` driver, you must configure the MTU value inside the guest operating system.

2.  Apply the `VirtualMachine` manifest by running the following command:

    ``` terminal
    $ oc apply -f <filename>.yaml
    ```

    where:

    `<filename>`
    Specifies the name of your `VirtualMachine` manifest YAML file.

</div>

# Localnet VM network configuration examples

The following examples show complete end-to-end configurations for connecting a virtual machine (VM) to a localnet network by using the machine network or dedicated network interfaces.

Connecting through the machine network
While it is recommended to use a dedicated network interface to separate VM traffic from management, you can also share a single uplink. In this example, the machine network belongs to the native VLAN.

<div class="formalpara">

<div class="title">

Example `NodeNetworkConfigurationPolicy` manifest

</div>

``` yaml
apiVersion: nmstate.io/v1
kind: NodeNetworkConfigurationPolicy
metadata:
  name: network-config
spec:
  desiredState:
    ovn:
      bridge-mappings:
      - localnet: provider-network
        bridge: br-ex
        state: present
```

</div>

- `spec.desiredState.ovn.bridge-mappings.localnet` specifies the localnet identifier. This value must match the `spec.network.localnet.physicalNetworkName` field in the `ClusterUserDefinedNetwork` manifest.

- `spec.desiredState.ovn.bridge-mappings.bridge` specifies the name of the existing OVS bridge on the node.

- `spec.desiredState.ovn.bridge-mappings.state` specifies the state of the mapping.

<div class="formalpara">

<div class="title">

Example `ClusterUserDefinedNetwork` manifest to request access to VLAN 100 on the physical network

</div>

``` yaml
apiVersion: k8s.ovn.org/v1
kind: ClusterUserDefinedNetwork
metadata:
  name: provider-network-100
spec:
  namespaceSelector:
    matchLabels:
      provider-network-vlan: "100"
  network:
    topology: Localnet
    localnet:
      role: Secondary
      physicalNetworkName: provider-network
      ipam:
        mode: Disabled
      mtu: 1500
      vlan:
        mode: Access
        access:
          id: 100
```

</div>

<div class="formalpara">

<div class="title">

Example `Namespace` manifest

</div>

``` yaml
apiVersion: v1
kind: Namespace
metadata:
  name: red
  labels:
    provider-network-vlan: "100"
```

</div>

<div class="formalpara">

<div class="title">

Example `VirtualMachine` manifest

</div>

``` yaml
apiVersion: kubevirt.io/v1
kind: VirtualMachine
metadata:
  name: example-vm
  namespace: red
spec:
  template:
    spec:
      domain:
        devices:
          interfaces:
            - name: provider-network
              bridge: {}
      networks:
      - name: provider-network
        multus:
          networkName: provider-network-100
# ...
```

</div>

Connecting through dedicated interfaces
To prevent network congestion and isolate the traffic, you can use dedicated network interface controllers (NICs) for the VM network. The following example uses two interfaces bonded with OVS `balance-slb` mode, to provide VM-friendly link redundancy without requiring switch-side link-aggregation configuration.

<div class="formalpara">

<div class="title">

Example `NodeNetworkConfigurationPolicy` manifest

</div>

``` yaml
apiVersion: nmstate.io/v1
kind: NodeNetworkConfigurationPolicy
metadata:
  name: network-config
spec:
  desiredState:
    interfaces:
    - name: eno1np0
      type: ethernet
      state: up
      mtu: 1500
    - name: eno2np1
      type: ethernet
      state: up
      mtu: 1500
    - name: br1
      type: ovs-bridge
      state: up
      bridge:
        allow-extra-patch-ports: true
        options:
          stp: false
          mcast-snooping-enable: true
        port:
        - name: bond1
          link-aggregation:
            mode: balance-slb
            port:
              - name: eno1np0
              - name: eno2np1
        - name: br1
    - name: br1
      type: ovs-interface
      state: up
      ipv4:
        enabled: false
      ipv6:
        enabled: false
    ovn:
      bridge-mappings:
      - localnet: provider-network
        bridge: br1
        state: present
```

</div>

- `spec.desiredState.ovn.bridge-mappings.localnet` specifies the localnet identifier. This value must match the `spec.network.localnet.physicalNetworkName` field in the `ClusterUserDefinedNetwork` manifest.

- `spec.desiredState.ovn.bridge-mappings.bridge` specifies the name of the OVS bridge on the node.

- `spec.desiredState.ovn.bridge-mappings.state` specifies the state of the mapping.

<div class="formalpara">

<div class="title">

Example `ClusterUserDefinedNetwork` manifest to request access to VLAN 100 on the physical network

</div>

``` yaml
apiVersion: k8s.ovn.org/v1
kind: ClusterUserDefinedNetwork
metadata:
  name: provider-network-100
spec:
  namespaceSelector:
    matchLabels:
      provider-network-vlan: "100"
  network:
    topology: Localnet
    localnet:
      role: Secondary
      physicalNetworkName: provider-network
      ipam:
        mode: Disabled
      mtu: 1500
      vlan:
        mode: Access
        access:
          id: 100
```

</div>

<div class="formalpara">

<div class="title">

Example `Namespace` manifest

</div>

``` yaml
apiVersion: v1
kind: Namespace
metadata:
  name: red
  labels:
    provider-network-vlan: "100"
```

</div>

<div class="formalpara">

<div class="title">

Example `VirtualMachine` manifest

</div>

``` yaml
apiVersion: kubevirt.io/v1
kind: VirtualMachine
metadata:
  name: example-vm
  namespace: red
spec:
  template:
    spec:
      domain:
        devices:
          interfaces:
            - name: provider-network
              bridge: {}
      networks:
      - name: provider-network
        multus:
          networkName: provider-network-100
# ...
```

</div>

# Additional network configuration for localnet networks

After you connect a virtual machine (VM) to a localnet network, you can configure micro segmentation, MAC address management, and IP address management for the VM network.

Micro segmentation
You can use the `MultiNetworkPolicy` API to create network policies that manage traffic for VMs attached to secondary networks. For example, you can create policies that allow or deny traffic based on specific ports, IP addresses and ranges, or labels. For more information, see "Configuring multi-network policy" in the Additional resources section.

The following example `MultiNetworkPolicy` manifests block all traffic to VMs on the localnet in a given namespace except for access to port 80 from one specific external IP address:

``` yaml
apiVersion: k8s.cni.cncf.io/v1beta1
kind: MultiNetworkPolicy
metadata:
  name: deny-by-default
  namespace: red
  annotations:
    k8s.v1.cni.cncf.io/policy-for: red/provider-network-100
spec:
  podSelector: {}
  policyTypes:
  - Ingress
```

``` yaml
apiVersion: k8s.cni.cncf.io/v1beta1
kind: MultiNetworkPolicy
metadata:
  name: allow-ingress-80
  namespace: red
  annotations:
    k8s.v1.cni.cncf.io/policy-for: red/provider-network-100
spec:
  podSelector:
    matchLabels:
      vm: my-virtual-machine
  policyTypes:
    - Ingress
  ingress:
  - from:
    - ipBlock:
        cidr: 203.0.113.50/32
    ports:
    - protocol: TCP
      port: 80
```

MAC address management
By default, the KubeMacPool component allocates MAC addresses for VM network interfaces from a shared MAC address pool. This ensures that each network interface is assigned a unique MAC address. You can request a specific MAC address when creating the VM. For more information, see "Managing MAC address pools for network interfaces" in the Additional resources section.

IP address management
OpenShift Virtualization does not support IP address management (IPAM) for VMs that use localnet networks. You can configure a static or dynamic IP address when you create a VM by using one of the following methods:

- **DHCP server**: Use your enterprise DHCP server running on the assigned VLANs.

- **Cloud-init**: Use the cloud-init API to set IP configuration through the `VirtualMachine` manifest, as in the following example:

  ``` yaml
  kind: VirtualMachine
  spec:
  # ...
    template:
    # ...
      spec:
        volumes:
        - cloudInitNoCloud:
            networkData: |
              version: 2
              ethernets:
                eth0:
                  addresses:
                  - 10.10.10.14/24
  ```

- `spec.volumes.cloudInitNoCloud.networkData.ethernets.eth0` specifies the name of the network interface in the guest operating system.

- `spec.volumes.cloudInitNoCloud.networkData.ethernets.eth0.addresses` specifies the static IP address and subnet mask to assign to the VM.

- **Custom solution**: You can set the IP address in the VM image or assign it by using Ansible.

Host IP address configuration
You can assign an IP address to OpenShift Container Platform nodes to access the secondary network by editing the `NodeNetworkConfigurationPolicy` manifest.

The following example shows a dynamic host IP configuration. This example assumes that the default gateway and DNS are configured through a different interface:

``` yaml
apiVersion: nmstate.io/v1
kind: NodeNetworkConfigurationPolicy
metadata:
  name: network-config
spec:
  desiredState:
    interfaces:
    - name: br1
      type: ovs-bridge
      state: up
      ipv4:
        dhcp: true
        auto-dns: false
        auto-gateway: false
        enabled: true
      # ...
```

For a static IP address, you must use one `NodeNetworkConfigurationPolicy` with a node selector per node, as in the following example:

``` yaml
apiVersion: nmstate.io/v1
kind: NodeNetworkConfigurationPolicy
metadata:
  name: network-config-node1
spec:
  nodeSelector:
    kubernetes.io/hostname: node1
  desiredState:
    interfaces:
    - name: br1
      type: ovs-bridge
      state: up
      ipv4:
        dhcp: false
        address:
        - ip: 192.168.122.201
          prefix-length: 24
        enabled: true
      # ...
```

``` yaml
apiVersion: nmstate.io/v1
kind: NodeNetworkConfigurationPolicy
metadata:
  name: network-config-node2
spec:
  nodeSelector:
    kubernetes.io/hostname: node2
  desiredState:
    interfaces:
    - name: br1
      type: ovs-bridge
      state: up
      ipv4:
        dhcp: false
        address:
        - ip: 192.168.122.202
          prefix-length: 24
        enabled: true
      # ...
```

# Localnet network limitations and alternatives

Before implementing a localnet network for virtual machines (VMs), review the following limitations and consider alternative networking approaches if your use case requires features that localnet does not support.

You must consider the following limitations before implementing a localnet network:

- After you define the localnet network, you can only change the node selector configuration. If you need to change the localnet network definition, create a new `ClusterUserDefinedNetwork` manifest and update your VMs to reference the new network.

- MAC spoof check is always enabled with OVN localnet. You cannot change the MAC address of the running guest interface.

- IP address management (IPAM) is not supported.

- Promiscuous mode is not supported.

- VLAN trunking is not supported.

The following alternative networking approaches are available if your use case requires features that localnet does not support:

SR-IOV
You can use Single Root I/O Virtualization (SR-IOV) network devices with additional networks on your OpenShift Container Platform cluster installed on bare metal or Red Hat OpenStack Platform (RHOSP) infrastructure for applications that require high bandwidth or low latency.

Linux bridge CNI
You can use a Linux bridge CNI to connect a VM to the physical network when VLAN trunking, MAC spoofing, or promiscuous mode is needed.

Primary layer 2 network
You can use a custom primary layer 2 network for a fully managed overlay network capable of Border Gateway Protocol (BGP) peering and Ethernet Virtual Private Network (EVPN).

Secondary layer 2 overlay network
You can configure a secondary layer 2 overlay network so that VMs can exchange traffic over a dedicated, persistent overlay subnet without touching the physical network switches or exposing traffic to the default pod network.

# Additional resources

- [About the Kubernetes NMState Operator](../../networking/networking_operators/k8s-nmstate-about-the-k8s-nmstate-operator.md#k8s-nmstate-about-the-k8s-nmstate-operator)

- [About the ClusterUserDefinedNetwork CR](../../networking/multiple_networks/primary_networks/about-user-defined-networks.md#about-cudn_about-user-defined-networks)

- [Configuring multi-network policy](../../networking/multiple_networks/secondary_networks/configuring-multi-network-policy.md#configuring-multi-network-policy)

- [Managing MAC address pools for network interfaces](virt-using-mac-address-pool-for-vms.md#virt-using-mac-address-pool-for-vms)

- [Postinstallation configuration](../../installing/installing_bare_metal/bare-metal-postinstallation-configuration.md#bare-metal-post-installation-configuration)

- [Which bonding modes work when used with a bridge that virtual machine guests or containers connect to?](https://access.redhat.com/solutions/67546)

- [Connecting a virtual machine to a Linux bridge network](virt-connecting-vm-to-linux-bridge.md#virt-connecting-vm-to-linux-bridge)

- [Connecting a virtual machine to an SR-IOV network](virt-connecting-vm-to-sriov.md#virt-connecting-vm-to-sriov)

- [Connecting a virtual machine to a primary user-defined network](virt-connecting-vm-to-primary-udn.md#virt-connecting-vm-to-primary-udn)

- [Connecting a virtual machine to an OVN-Kubernetes layer 2 secondary network](virt-connecting-vm-to-ovn-secondary-network.md#virt-connecting-vm-to-ovn-secondary-network)
