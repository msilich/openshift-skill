<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

You can use a secondary network in situations where you require network isolation, including data plane and control plane separation.

Isolating network traffic is useful for the following performance and security reasons:

- Performance

  **Traffic management**: You can send traffic on two different planes to manage how much traffic is along each plane.

- Security

  **Network isolation**: You can send sensitive traffic onto a network plane that is managed specifically for security considerations, and you can separate private data that must not be shared between tenants or customers.

All of the pods in the cluster still use the cluster-wide default network to maintain connectivity across the cluster. Every pod has an `eth0` interface that is attached to the cluster-wide pod network. You can view the interfaces for a pod by using the `oc exec -it <pod_name> -- ip a` command. If you add secondary network interfaces that use the Multus Container Network Interface (CNI). These secondary networks are named `net1`, `net2`, and so on.

To attach secondary network interfaces to a pod, you must create configurations that define how the interfaces are attached. Use either a `UserDefinedNetwork` custom resource (CR) or a `NetworkAttachmentDefinition` CR to specify each interface. A CNI configuration inside each of these CRs defines how that interface is created.

# Secondary networks in OpenShift Container Platform

OpenShift Container Platform provides the following CNI plugins for creating secondary networks in your cluster:

- **bridge**: To configure a bridge-based secondary network to allow pods on the same host to communicate with each other and the host, use the following procedure:

  - [Configure a bridge-based secondary network](secondary_networks/creating-secondary-nwt-other-cni.md#nw-multus-bridge-object_configuring-additional-network-cni)

- **bond-cni**: To provide a method for aggregating multiple network interfaces into a single logical *bonded* interface, use the following procedure:

  - [Configure a Bond CNI secondary network](secondary_networks/creating-secondary-nwt-other-cni.md#nw-multus-bond-cni-object_configuring-additional-network-cni)

- **host-device**: To allow pods access to a physical Ethernet network device on the host system, use the following procedure:

  - [Configure a host-device secondary network](secondary_networks/creating-secondary-nwt-other-cni.md#nw-multus-host-device-object_configuring-additional-network-cni)

- **ipvlan**: Allow pods on a host to communicate with other hosts and pods on those hosts, similar to a macvlan-based secondary network. Unlike a macvlan-based secondary network, each pod shares the same MAC address as the parent physical network interface. Use the following procedure:

  - [Configure an ipvlan-based secondary network](secondary_networks/creating-secondary-nwt-other-cni.md#nw-multus-ipvlan-object_configuring-additional-network-cni)

- **VLAN**: To allow VLAN-based network isolation and connectivity for pods, use the following procedure:

  - [Configure a VLAN-based secondary network](secondary_networks/creating-secondary-nwt-other-cni.md#nw-multus-vlan-object_configuring-additional-network-cni)

- **macvlan**: To allow pods on a host to communicate with other hosts and pods on those hosts by using a physical network interface. Each pod that is attached to a macvlan-based secondary network is provided a unique MAC address:

  - [Configure a macvlan-based secondary network](secondary_networks/creating-secondary-nwt-other-cni.md#nw-multus-macvlan-object_configuring-additional-network-cni)

- **TAP**: A TAP device enables user space programs to send and receive network packets. To create a TAP device inside the container namespace, use the following procedure:

  - [Configure a TAP-based secondary network](secondary_networks/creating-secondary-nwt-other-cni.md#nw-multus-tap-object_configuring-additional-network-cni)

- **SR-IOV**: To allow pods to attach to a virtual function (VF) interface on SR-IOV capable hardware on the host system.

  - [Configure an SR-IOV based secondary network](../hardware_networks/about-sriov.md#about-sriov)

- **route-override**: To allow pods to override and set routes, use the following procedure:

  - [Configure a `route-override` based secondary network](secondary_networks/creating-secondary-nwt-other-cni.md#nw-route-override-cni_configuring-additional-network-cni)

# UserDefinedNetwork and NetworkAttachmentDefinition support matrix

You can use user defined networks and network attachment definitions to define and configure customized networks for your needs.

By creating `UserDefinedNetwork` and `NetworkAttachmentDefinition` custom resources (CRs), cluster administrators can complete the following tasks:

- Create customizable network configurations

- Define their own network topologies

- Ensure network isolation

- Manage IP addressing for workloads

- Configure advanced network features

By creating a `ClusterUserDefinedNetwork` CR, administrators can create and define secondary networks that span multiple namespaces at the cluster level.

User-defined networks and network attachment definitions can serve as both the primary and secondary network interface, and each support `layer2` and `layer3` topologies.

> [!NOTE]
> As of OpenShift Container Platform 4.19, the use of the `Localnet` topology by `ClusterUserDefinedNetwork` CRs is generally available. This configuration is the preferred method for connecting physical networks to virtual networks. Or, you can use the `NetworkAttachmentDefinition` CR to create secondary networks with `Localnet` topologies.

The following section highlights the supported features of the `UserDefinedNetwork` and `NetworkAttachmentDefinition` CRs when used as either the primary or secondary network. A separate table for the `ClusterUserDefinedNetwork` CR is also included.

| Network feature               | Layer2 topology | Layer3 topology |
|-------------------------------|-----------------|-----------------|
| east-west traffic             | ✓               | ✓               |
| north-south traffic           | ✓               | ✓               |
| Persistent IPs                | ✓               | X               |
| Services                      | ✓               | ✓               |
| Routes                        | X               | X               |
| `EgressIP` resource           | ✓               | ✓               |
| Multicast                     | X               | ✓               |
| `NetworkPolicy` resource      | ✓               | ✓               |
| `MultinetworkPolicy` resource | X               | X               |

Primary network support matrix for `UserDefinedNetwork` and `NetworkAttachmentDefinition` CRs

where:

Multicast
Must be enabled in the namespace, and it is only available between OVN-Kubernetes network pods. For more information, see "About multicast".

`NetworkPolicy` resource
When creating a `ClusterUserDefinedNetwork` CR with a primary network type, network policies must be created *after* the `UserDefinedNetwork` CR.

| Network feature | Layer2 topology | Layer3 topology | Localnet topology |
|----|----|----|----|
| east-west traffic | ✓ | ✓ | ✓ (`NetworkAttachmentDefinition` CR only) |
| north-south traffic | X | X | ✓ (`NetworkAttachmentDefinition` CR only) |
| Persistent IPs | ✓ | X | ✓ (`NetworkAttachmentDefinition` CR only) |
| Services | X | X | X |
| Routes | X | X | X |
| `EgressIP` resource | X | X | X |
| Multicast | X | X | X |
| `NetworkPolicy` resource | X | X | X |
| `MultinetworkPolicy` resource | ✓ | ✓ | ✓ (`NetworkAttachmentDefinition` CR only) |

Secondary network support matrix for `UserDefinedNetwork` and `NetworkAttachmentDefinition` CRs

The Localnet topology is unavailable for use with the `UserDefinedNetwork` CR. It is only supported on secondary networks for `NetworkAttachmentDefinition` CRs.

| Network feature | Layer2 topology | Layer3 topology | Localnet topology |
|----|----|----|----|
| east-west traffic | ✓ | ✓ | ✓ |
| north-south traffic | ✓ | ✓ | ✓ |
| Persistent IPs | ✓ | X | ✓ |
| Services | ✓ | ✓ |  |
| Routes | X | X |  |
| `EgressIP` resource | ✓ | ✓ |  |
| Multicast | X | ✓ |  |
| `MultinetworkPolicy` resource | X | X | ✓ |
| `NetworkPolicy` resource | ✓ | ✓ |  |

Support matrix for `ClusterUserDefinedNetwork` CRs

where:

Multicast
must be enabled in the namespace, and it is only available between OVN-Kubernetes network pods. For more information, see "About multicast".

`NetworkPolicy` resource
When creating a `ClusterUserDefinedNetwork` CR with a primary network type, network policies must be created *after* the `UserDefinedNetwork` CR.

# Additional resources

- [Enabling multicast for a project](../ovn_kubernetes_network_provider/enabling-multicast.md#nw-ovn-kubernetes-enabling-multicast)
