<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

You can connect a virtual machine (VM) to an OVN-Kubernetes localnet secondary network by using the CLI. Cluster administrators can use the `ClusterUserDefinedNetwork` (CUDN) custom resource definition (CRD) to create a shared OVN-Kubernetes network across multiple namespaces.

An OVN-Kubernetes secondary network is compatible with the multi-network policy API which provides the `MultiNetworkPolicy` custom resource definition (CRD) to control traffic flow to and from VMs. For more information, see "Additional resources".

> [!IMPORTANT]
> You must use the `ipBlock` attribute to define network policy ingress and egress rules for specific CIDR blocks. Using pod or namespace selector policy peers is not supported.

A localnet topology connects the secondary network to the physical underlay. This enables both east-west cluster traffic and access to services running outside the cluster, but it requires additional configuration of the underlying Open vSwitch (OVS) system on cluster nodes.

# Creating a user-defined-network for localnet topology by using the CLI

You can create a secondary cluster-scoped user-defined-network (CUDN) for the localnet network topology by using the CLI.

<div>

<div class="title">

Prerequisites

</div>

- You are logged in to the cluster as a user with `cluster-admin` privileges.

- You have installed the OpenShift CLI (`oc`).

- You installed the Kubernetes NMState Operator.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create a `NodeNetworkConfigurationPolicy` object to map the OVN-Kubernetes secondary network to an Open vSwitch (OVS) bridge.

    Example `NodeNetworkConfigurationPolicy` manifest:

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

    - `metadata.name` specifies the name of the configuration object.

    - `spec.nodeSelector` specifies the nodes to which the node network configuration policy is applied. The recommended node selector value is `node-role.kubernetes.io/worker: ''`.

    - `spec.desiredState.ovn.bridge-mappings.localnet` specifies the name of the additional network from which traffic is forwarded to the OVS bridge. This attribute must match the value of the `spec.network.localnet.physicalNetworkName` field of the `ClusterUserDefinedNetwork` object that defines the OVN-Kubernetes additional network. This example uses the name `localnet1`.

    - `spec.desiredState.ovn.bridge-mappings.bridge` specifies name of the OVS bridge on the node. This value is required if the `state` attribute is `present` or not specified.

    - `spec.desiredState.ovn.bridge-mappings.state` specifies the state of the mapping. Must be either `present` to add the mapping or `absent` to remove the mapping. The default value is `present`.

      > [!IMPORTANT]
      > OpenShift Virtualization does not support Linux bridge bonding modes 0, 5, and 6. For more information, see [Which bonding modes work when used with a bridge that virtual machine guests or containers connect to?](https://access.redhat.com/solutions/67546).

2.  Apply the `NodeNetworkConfigurationPolicy` manifest by running the following command:

    ``` terminal
    $ oc apply -f <filename>.yaml
    ```

    where:

    `<filename>`
    Specifies the name of your `NodeNetworkConfigurationPolicy` manifest YAML file.

3.  Create a `ClusterUserDefinedNetwork` object to create a localnet secondary network.

    Example `ClusterUserDefinedNetwork` manifest:

    ``` yaml
    apiVersion: k8s.ovn.org/v1
    kind: ClusterUserDefinedNetwork
    metadata:
      name: cudn-localnet
    spec:
      namespaceSelector:
        matchExpressions:
        - key: kubernetes.io/metadata.name
          operator: In
          values: ["red", "blue"]
      network:
        topology: Localnet
        localnet:
            role: Secondary
            physicalNetworkName: localnet1
            ipam:
              mode: Disabled
    # ...
    ```

    - `metadata.name` specifies the name of the `ClusterUserDefinedNetwork` custom resource.

    - `spec.namespaceSelector` specifies a set of namespaces that the cluster UDN applies to. The namespace selector must not point to the following values: `default`; an `openshift-*` namespace; or any global namespaces that are defined by the Cluster Network Operator (CNO).

    - `spec.namespaceSelector.matchExpressions` specifies the type of selector. In this example, the `matchExpressions` selector selects objects that have the label `kubernetes.io/metadata.name` with the value `red` or `blue`.

    - `spec.namespaceSelector.matchExpressions.operator` specifies the type of operator. Possible values are `In`, `NotIn`, and `Exists`.

    - `spec.network.topology` specifies the topological configuration of the network. A `Localnet` topology connects the logical network to the physical underlay.

    - `spec.network.localnet.role` specifies whether the UDN is primary or secondary. The required value is `Secondary` for `topology: Localnet`.

    - `spec.network.localnet.physicalNetworkName` specifies the name of the OVN-Kubernetes bridge mapping that is configured on the node. This value must match the `spec.desiredState.ovn.bridge-mappings.localnet` field in the `NodeNetworkConfigurationPolicy` manifest that you previously created. This ensures that you are bridging to the intended segment of your physical network.

    - `spec.network.localnet.ipam.mode` specifies whether IP address management (IPAM) is enabled or disabled. The required value is `Disabled`. OpenShift Virtualization does not support configuring IPAM for virtual machines.

4.  Apply the `ClusterUserDefinedNetwork` manifest by running the following command:

    ``` terminal
    $ oc apply -f <filename>.yaml
    ```

    where:

    `<filename>`
    Specifies the name of your `ClusterUserDefinedNetwork` manifest YAML file.

</div>

# Creating a namespace for secondary user-defined networks by using the CLI

You can create a namespace to be used with an existing secondary cluster-scoped user-defined network (CUDN) by using the CLI.

<div>

<div class="title">

Prerequisites

</div>

- You are logged in to the cluster as a user with `cluster-admin` permissions.

- You have installed the OpenShift CLI (`oc`).

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create a `Namespace` object similar to the following example:

    ``` yaml
    apiVersion: v1
    kind: Namespace
    metadata:
      name: red
    # ...
    ```

2.  Apply the `Namespace` manifest by running the following command:

    ``` terminal
    oc apply -f <filename>.yaml
    ```

    where:

    `<filename>`
    Specifies the name of your `Namespace` manifest YAML file.

</div>

# Attaching a virtual machine to secondary user-defined networks by using the CLI

You can connect a virtual machine (VM) to multiple secondary cluster-scoped user-defined networks (CUDNs) by configuring the interface binding.

<div>

<div class="title">

Prerequisites

</div>

- You have installed the OpenShift CLI (`oc`).

</div>

<div>

<div class="title">

Procedure

</div>

1.  Edit the `VirtualMachine` manifest to add the CUDN interface details, as in the following example:

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
                - name: secondary_localnet
                  bridge: {}
            machine:
              type: ""
            resources:
              requests:
                memory: 2048M
          networks:
          - name: secondary_localnet
            multus:
              networkName: <localnet_cudn_name>
    ```

    - `metadata.namespace` specifies the namespace in which the VM is located. This value must match a namespace that is associated with the secondary CUDN.

    - `spec.template.spec.domain.devices.interfaces.name` specifies the name of the secondary user-defined network interface.

    - `spec.template.spec.networks.name` specifies the name of the network. This value must match the value of the `spec.template.spec.domain.devices.interfaces.name` field.

    - `spec.template.spec.networks.multus.networkName` specifies the name of the localnet `ClusterUserDefinedNetwork` object that you previously created.

2.  Apply the `VirtualMachine` manifest by running the following command:

    ``` terminal
    $ oc apply -f <filename>.yaml
    ```

    where:

    `<filename>`
    Specifies the name of your `VirtualMachine` manifest YAML file.

</div>

# Considerations when running OpenShift Virtualization on IBM Z®

When running OpenShift Virtualization on IBM Z®, the required network configuration depends on the hardware generation and the network adapter in use. Network interfaces on IBM Z® behave differently from standard Ethernet devices, which affects how the bridge forwards virtual machine traffic.

Review the following considerations before configuring a user-defined network (UDN) for virtual machines on IBM Z®. Applying the correct settings ensures stable layer 2 connectivity between the virtual machine and the network bridge.

# Configuring a RoCE adapter for virtual machine networking on IBM Z®

On IBM Z® z17, RoCE adapters support promiscuous mode at the hardware level, which forwards traffic for all virtual machine MAC addresses without manual registration. On earlier IBM Z® generations, each virtual machine MAC address must be manually registered with the RoCE interface because promiscuous mode is not available.

Use the following procedure to enable promiscuous mode on IBM Z® z17.

<div>

<div class="title">

Prerequisites

</div>

- You have access to the LPAR configuration for the IBM Z® z17 system.

- You have the name of the RoCE network interface, for example `ens329`.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Enable promiscuous mode on the RoCE adapter at the hardware level in the LPAR. See [Configuring FIDPARM to support promiscuous mode on a VF](https://www.ibm.com/docs/en/linux-on-systems?topic=mode-configuring-fidparm-support-promiscuous-vf)

2.  Enable promiscuous mode on the corresponding network interface by running the following command:

    ``` terminal
    $ ip link set dev <interface> promisc on
    ```

    where `<interface>` is the name of the RoCE network interface, for example `ens329`.

</div>

<div>

<div class="title">

Verification

</div>

1.  Verify that promiscuous mode is active by running the following command:

    ``` terminal
    $ ip link show dev <interface>
    ```

    Example output:

    ``` terminal
    3: ens329: <BROADCAST,MULTICAST,PROMISC,UP,LOWER_UP> mtu 1500 qdisc mq state UP mode DEFAULT group default qlen 1000
        link/ether 22:4b:c0:53:05:be brd ff:ff:ff:ff:ff:ff
        altname enp0s0
    ```

    The presence of the `PROMISC` flag confirms that promiscuous mode is active.

</div>

# Configuring OSA and HiperSockets adapters for virtual machine networking on IBM Z®

You can configure OSA and HiperSockets interfaces on IBM Z® for virtual machine networking by enabling Virtual NIC Characteristics (VNICC) attributes on the qeth driver. Without them, the qeth driver silently drops packets destined for virtual machine MAC addresses.

<div>

<div class="title">

Prerequisites

</div>

- You have the bus ID of the qeth network device, for example `0.0.1100`.

- The `chzdev` command-line tool is available on the host node.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Enable flooding on the qeth device by running the following command:

    ``` terminal
    $ echo 1 > /sys/devices/qeth/0.0.1100/vnicc/flooding
    ```

2.  Enable multicast flooding on the qeth device by running the following command:

    ``` terminal
    $ echo 1 > /sys/devices/qeth/0.0.1100/vnicc/mcast_flooding
    ```

3.  Enable MAC address learning on the qeth device by running the following command:

    ``` terminal
    $ echo 1 > /sys/devices/qeth/0.0.1100/vnicc/learning
    ```

4.  Or, enable MAC address learning by using `chzdev`:

    ``` terminal
    $ sudo chzdev <device_bus_id> vnicc/learning=1
    ```

    where:

    `chzdev`
    Specifies the tool to configure IBM Z® devices.

    `<device_bus_id>`
    Specifies the bus ID of the qeth network device, for example `0.0.1100`.

    `vnicc/learning=1`
    Enables MAC address learning.

</div>

# Additional resources

- [About the `ClusterUserDefinedNetwork` CR](../../networking/multiple_networks/primary_networks/about-user-defined-networks.md#about-cudn_about-user-defined-networks)

- [Multi-network policy API](../../networking/multiple_networks/secondary_networks/configuring-multi-network-policy.md#configuring-multi-network-policy)
