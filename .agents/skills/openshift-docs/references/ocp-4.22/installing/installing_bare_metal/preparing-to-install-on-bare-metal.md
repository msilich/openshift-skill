<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Review the different methods for installing OpenShift Container Platform on bare metal and prepare your environment for installation.

# Prerequisites

- You have read details about the OpenShift Container Platform installation and update processes.

- You have read the documentation on selecting a cluster installation method and preparing it for users.

- You have read the documentation for supported and unsupported OVN-Kubernetes network plugin use cases.

# Choosing a method to install OpenShift Container Platform on bare metal

The OpenShift Container Platform installation program offers four methods for deploying a cluster:

- **Interactive**: You can deploy a cluster with the web-based Assisted Installer. This is the recommended approach for clusters with networks connected to the internet. The Assisted Installer is the easiest way to install OpenShift Container Platform, it provides smart defaults, and it performs pre-flight validations before installing the cluster. It also provides a RESTful API for automation and advanced configuration scenarios.

- **Local Agent-based**: You can deploy a cluster locally with the agent-based installer for air-gapped or restricted networks. It provides many of the benefits of the Assisted Installer, but you must download and configure the agent-based installer first. Configuration is done with a commandline interface. This approach is ideal for air-gapped or restricted networks.

- **Automated**: You can deploy a cluster on installer-provisioned infrastructure and the cluster it maintains. The installation program uses each cluster host’s baseboard management controller (BMC) for provisioning. You can deploy clusters with both connected or air-gapped or restricted networks.

- **Full control**: You can deploy a cluster on infrastructure that you prepare and maintain, which provides maximum customizability. You can deploy clusters with both connected or air-gapped or restricted networks.

The clusters have the following characteristics:

- Highly available infrastructure with no single points of failure is available by default.

- Administrators maintain control over what updates are applied and when.

# Installing a cluster on installer-provisioned infrastructure

You can install a cluster on bare-metal infrastructure that is provisioned by the OpenShift Container Platform installation program, by using the following method:

**Installing an installer-provisioned cluster on bare metal**
You can install OpenShift Container Platform on bare metal by using installer provisioning.

# Installing a cluster on user-provisioned infrastructure

You can install a cluster on bare-metal infrastructure that you provision, by using one of the following methods:

**Installing a user-provisioned cluster on bare metal**
You can install OpenShift Container Platform on bare-metal infrastructure that you provision. For a cluster that contains user-provisioned infrastructure, you must deploy all of the required machines.

**Installing a user-provisioned bare-metal cluster with network customizations**
You can install a bare-metal cluster on user-provisioned infrastructure with network-customizations. By customizing your network configuration, your cluster can coexist with existing IP address allocations in your environment and integrate with existing MTU and VXLAN configurations. Most of the network customizations must be applied at the installation stage.

**Installing a user-provisioned bare-metal cluster on a restricted network**
You can install a user-provisioned bare-metal cluster on a restricted or disconnected network by using a mirror registry. You can also use this installation method to ensure that your clusters only use container images that satisfy your organizational controls on external content.

# Bare-metal cluster installation requirements for OpenShift Virtualization

Configure your bare-metal cluster correctly during installation to support OpenShift Virtualization, as certain required settings cannot be changed after installation.

## High availability requirements for OpenShift Virtualization

When discussing high availability (HA) features in the context of OpenShift Virtualization, this refers only to the replication model of the core cluster components, determined by the `controlPlaneTopology` and `infrastructureTopology` fields in the `Infrastructure` custom resource (CR). Setting these fields to `HighlyAvailable` offers component redundancy, which is distinct from general cluster-wide application HA. Setting these fields to `SingleReplica` disables component redundancy, and therefore disables OpenShift Virtualization HA features.

If you plan to use OpenShift Virtualization HA features, you must have three control plane nodes at the time of cluster installation. The `controlPlaneTopology` status in the `Infrastructure` CR for the cluster must be `HighlyAvailable`.

> [!NOTE]
> You can install OpenShift Virtualization on a single-node cluster, but single-node OpenShift does not support HA features.

## Live migration requirements for OpenShift Virtualization

- If you plan to use live migration, you must have multiple worker nodes. The `infrastructureTopology` status in the `Infrastructure` CR for the cluster must be `HighlyAvailable`. A minimum of three worker nodes is recommended.

  > [!NOTE]
  > You can install OpenShift Virtualization on a single-node cluster, but single-node OpenShift does not support live migration.

- Live migration requires shared storage. Storage for OpenShift Virtualization must support and use the ReadWriteMany (RWX) access mode.

## SR-IOV requirements for OpenShift Virtualization

If you plan to use Single Root I/O Virtualization (SR-IOV), ensure that your network interface controllers (NICs) are supported by OpenShift Container Platform.

# NIC partitioning for SR-IOV devices

You can partition a single, high-speed dual port NIC into multiple virtual functions (VFs) and enable SR-IOV to support high availability with Link Aggregation Control Protocol (LACP) bonding.

This feature supports the use of bonds for high availability with the Link Aggregation Control Protocol (LACP).

> [!NOTE]
> Only one LACP can be declared by physical NIC.

An OpenShift Container Platform cluster can be deployed on a bond interface with 2 VFs on 2 physical functions (PFs) using the following methods:

- Agent-based installer

  > [!NOTE]
  > The minimum required version of `nmstate` is:
  >
  > - `1.4.2-4` for RHEL 8 versions
  >
  > - `2.2.7` for RHEL 9 versions

- Installer-provisioned infrastructure installation

- User-provisioned infrastructure installation

# Additional resources

- [OpenShift Container Platform installation and update processes](../../architecture/architecture-installation.md#architecture-installation)

- [Selecting a cluster installation method and preparing it for users](../overview/installing-preparing.md#installing-preparing)

- [OVN-Kubernetes purpose](../../networking/ovn_kubernetes_network_provider/about-ovn-kubernetes.md#nw-ovn-kubernetes-purpose_about-ovn-kubernetes)

- [Assisted Installer](https://access.redhat.com/documentation/en-us/assisted_installer_for_openshift_container_platform)

- [Preparing to install with the Agent-based Installer](../installing_with_agent_based_installer/preparing-to-install-with-agent-based-installer.md#preparing-to-install-with-agent-based-installer)

- [Agent-based installer](https://console.redhat.com/openshift/install/metal/agent-based)

- [Deploying installer-provisioned clusters on bare metal](ipi/ipi-install-overview.md#ipi-install-overview)

- [Installing a user-provisioned cluster on bare metal](upi/installing-bare-metal.md#installing-bare-metal)

- [Installing a user-provisioned bare-metal cluster with network customizations](upi/installing-bare-metal-network-customizations.md#installing-bare-metal-network-customizations)

- [Installing a user-provisioned bare-metal cluster on a restricted network](upi/installing-restricted-networks-bare-metal.md#installing-restricted-networks-bare-metal)

- [Installation process](../../architecture/architecture-installation.md#installation-process_architecture-installation)

- [Getting started with OpenShift Virtualization](../../virt/getting_started/virt-getting-started.md#virt-getting-started)

- [Preparing your cluster for OpenShift Virtualization](../../virt/install/preparing-cluster-for-virt.md#preparing-cluster-for-virt)

- [About Single Root I/O Virtualization (SR-IOV) hardware networks](../../networking/hardware_networks/about-sriov.md#about-sriov)

- [Connecting a virtual machine to an SR-IOV network](../../virt/vm_networking/virt-connecting-vm-to-sriov.md#virt-connecting-vm-to-sriov)

- [Example: Bonds and SR-IOV dual-NIC node network configuration](../installing_with_agent_based_installer/preparing-to-install-with-agent-based-installer.md#agent-install-sample-config-bond-sriov_preparing-to-install-with-agent-based-installer)

- [Optional: Configuring host network interfaces for dual port NIC](ipi/ipi-install-installation-workflow.md#configuring-host-dual-network-interfaces-in-the-install-config-yaml-file_ipi-install-installation-workflow)

- [Bonding multiple SR-IOV network interfaces to a dual port NIC interface](upi/installing-bare-metal.md#bonding-multiple-sriov-network-interfaces-to-dual-port_installing-bare-metal)
