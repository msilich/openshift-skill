<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

These release notes describe new features and enhancements, Technology Preview features, deprecated and removed features, fixed issues, and known issues for OpenShift Virtualization 4.22.

# Supported guest operating systems

To view the supported guest operating systems for OpenShift Virtualization, see [Certified Guest Operating Systems in Red Hat OpenStack Platform, Red Hat Virtualization, OpenShift Virtualization and Red Hat Enterprise Linux with KVM](https://access.redhat.com/articles/973163#ocpvirt).

# New features and enhancements

Extended Upgrade Support enables 36-month lifecycle for OpenShift Virtualization clusters
OpenShift Virtualization now supports a 36-month cluster lifecycle policy with optional Extended Upgrade Support (EUS) add-ons. With EUS, you can remain on the same release for up to 36 months, enabling stable production environments for mission-critical applications.

For more information about EUS add-on subscriptions, see [OpenShift Container Platform Life Cycle Policy](https://access.redhat.com/support/policy/updates/openshift).

[CNV-73922](https://redhat.atlassian.net/browse/CNV-73922)

<!-- -->

Monitor node memory overcommit level for virtual machines
Cluster administrators can balance workloads using the VM memory overcommit and utilization dashboard. The dashboard allows you to monitor whether clusters are underutilized or at risk due to memory overcommit, or to decide whether to expand a cluster.

[CNV-44026](https://redhat.atlassian.net/browse/CNV-44026)

<!-- -->

Configure PSRP, WINRM, or SSH to manage Windows-detected hosts in OpenShift Virtualization
You can set a connection method to secure the communication between Windows hosts running on OpenShift Virtualization and the Ansible environment. Configure PowerShell Remote Protocol (PSRP), Windows Remote Management (WINRM), or Secure Shell (SSH) as a connection method in Ansible automation tasks to manage Windows hosts. The Ansible inventory plugin uses the protocol to manage the Windows hosts.

[CNV-73306](https://redhat.atlassian.net/browse/CNV-73306)

Configuring PCI passthrough for the IBM® Spyre Accelerator for VMs on IBM Z® and IBM® LinuxONE is generally available
You can attach the IBM® Spyre Accelerator to VMs using PCI passthrough on IBM® z17 and IBM® LinuxONE Emperor 5 or later. The IBM® Spyre Accelerator enhances AI inferencing capabilities on IBM Z® and IBM® LinuxONE systems.

For more information, see [Configuring PCI passthrough](../managing_vms/advanced_vm_management/virt-configuring-pci-passthrough.md#virt-configuring-pci-passthrough).

[CNV-83214](https://redhat.atlassian.net/browse/CNV-83214)

<!-- -->

Support for IPv6 single-stack clusters is generally available
With this release, support for IPv6 single-stack clusters is Generally Available (GA). OpenShift Virtualization supports single-stack IPv6 clusters for VMs that are connected to an OVN-Kubernetes localnet network, Linux bridge Container Network Interface (CNI) plugin, and Single Root I/O Virtualization (SR-IOV) network devices.

[CNV-28924](https://redhat.atlassian.net/browse/CNV-28924)

Live update NAD reference for secondary VM networks
The virtual machine (VM) administrator and the VM owner can change the Network Attachment Definition (NAD) of a running VM’s secondary network interface. Edit the `networkName` field in the VM custom resource (CR) to enter a NAD with a different VLAN. This triggers a live migration. The hot swap capability gives the flexibility to change VM networks, such as to a different VLAN, for a better link or an isolated segment while preserving the guest interface name and MAC address, without rebooting the VM.

[CNV-72329](https://redhat.atlassian.net/browse/CNV-72329)

Define physical networks from an existing node network configuration policy
Define physical networks based on existing node network configuration policies (NNCPs) in the OpenShift Virtualization user interface. A physical network is a logical grouping of one or more network configurations that represent the NNCP. Cluster administrators can extend a physical network to a set of new nodes, configure a virtual machine that uses the physical network through an OVN-Kubernetes Localnet network, and create new node network configurations for VMs.

[CNV-72621](https://redhat.atlassian.net/browse/CNV-72621)

<!-- -->

Insert and eject CD-ROMs in a live VM
OpenShift Virtualization support for declarative hot plug of CD-ROM storage devices in live virtual machines (VMs) is generally available. You can insert and eject CD-ROM storage in running VMs by enabling the `DeclarativeHotplugVolumes` feature gate in the `HyperConverged` custom resource (CR) without restarting the VM.

[CNV-68916](https://redhat.atlassian.net/browse/CNV-68916)

Option to automatically clean up source PVCs after storage migration
Virtual machine (VM) owners can now automatically clean up source persistent volume claims (PVCs) after a storage migration, reducing manual cleanup tasks. By default, OpenShift Virtualization retains the source PVCs so you can manually clean them up. You can deselect the option to keep source PVCs in the user interface to enable automatic cleanup after the migration completes.

[CNV-73509](https://redhat.atlassian.net/browse/CNV-73509)

Configure predictable PVC and DV names when cloning VMs
Virtual machine (VM) owners and cluster administrators can configure predictable persistent volume claim (PVC) and data volume (DV) names when cloning a VM. Use the `volumeNamePolicy` to include the target VM name in the restored PVC names to maintain consistency and manageability of the storage resources. This improves compatibility with orchestrators that rely on the original DV name after restoration.

[CNV-76230](https://redhat.atlassian.net/browse/CNV-76230)

Keep original PVC names when restoring a virtual machine from a VM snapshot
Virtual machine (VM) owners who restore a VM from a snapshot can retain the original names of persistent volume claims (PVCs). You can use the **In place Volume Restore Policy** section of the **Restore Snapshot** dialog in the web console to preserve the PVC names. This sets the `spec.volumeRestorePolicy` field on the `VirtualMachineRestore` resource. If users opt not to keep the original PVC name, OpenShift Virtualization assigns a randomized PVC name.

[CNV-71612](https://redhat.atlassian.net/browse/CNV-71612)

New default for PVC naming during VM restore and clone requests
With this update, the `volumeRestorePolicy` default setting has been changed to `PrefixTargetName`. This means that the name of the target virtual machine (VM) is now used as a prefix for new PVC names created with VM restore and clone requests.

[CNV-77397](https://redhat.atlassian.net/browse/CNV-77397)

<!-- -->

Configure AAQ to track resource utilization for VMs and mixed workloads
Cluster administrators can use the Application-Aware Quota (AAQ) Operator in the OpenShift Container Platform web console as the primary mechanism for defining and managing resource limits for virtual machines (VMs) and mixed workloads. You can configure AAQ to track resource utilization for VMs only, for both pods and VMs together, or for VMs and pods separately with dedicated quotas for each.

[CNV-61720](https://redhat.atlassian.net/browse/CNV-61720)

Configure a run strategy for virtual machines in the web console
Virtual machine (VM) owners can configure and edit a run strategy that models how the VMs behave after a shutdown, restart, or a failure. You can choose a run strategy from `Rerun on failure`, `Always`, `Halted`, and `Manual` in the **Scheduling** tab of the OpenShift Virtualization user interface. You can edit the run strategy across all VM creation flows and the details view for a streamlined experience when customizing VMs.

[CNV-82452](https://redhat.atlassian.net/browse/CNV-82452)

Export virtual machine data in CSV format for inventory management
You can export virtual machine (VM) information such as hostname, IP address, node name, namespace, memory, disk, operating system version, and more in CSV format to efficiently manage the inventory. You can also customize the view of VM tables by using automated sorting and built-in column filtering capabilities.

[CNV-74276](https://redhat.atlassian.net/browse/CNV-74276)

Hide YAML tab on virtual machines
Administrators can hide the YAML tab on virtual machines (VM) and other resources to prevent users from directly editing the YAML from the user interface, enhancing security and reducing potential errors. As a result, you can ensure that configuration changes are made through approved channels, maintaining consistency and compliance across the system.

[CNV-74216](https://redhat.atlassian.net/browse/CNV-74216)

Overview tab displays dynamic hierarchical view of VM data
The **Overview** tab displays a dynamic, hierarchical view of VM data that adapts to your tree view selection, supporting both cluster and multi-cluster levels.

[CNV-79560](https://redhat.atlassian.net/browse/CNV-79560)

Add an internal certificate authority or a self-signed certificate for virtual machine images
Cluster administrators can create a custom certificate authority (CA) or a self-signed certificate for URL images in a cluster in the Add Volume dialog. As a result, you can secure access to HTTPS sources to be used to create a virtual machine (VM) in a streamlined user workflow, without switching to the command line interface (CLI) for manual patching.

[CNV-79324](https://redhat.atlassian.net/browse/CNV-79324)

<!-- -->

Recording rule names updated to conform to Prometheus best practices
Recording rule names have been updated to follow the naming convention `<level>:<metric>:<operations>`. This aligns with the Prometheus best practices on naming rules, and helps users to distinguish between recording rules and metrics. For information about which rule names have changed, see the Knowledgebase article [Updates to OpenShift Virtualization 4.22 recording rules naming](https://access.redhat.com/articles/7144047).

[CNV-89006](https://redhat.atlassian.net/browse/CNV-89006)

# Deprecated features

Recording rules deprecated
The following recording rules are deprecated:

- `kubevirt_vm_created_total`

- `kubevirt_cnao_kubemacpool_duplicate_macs`

  If you reference these recording rules in custom alerts or dashboards, remove them before upgrading to a future release.

[CNV-89006](https://redhat.atlassian.net/browse/CNV-89006)

The `HotplugVolume` feature gate is deprecated
The `HotplugVolume` feature gate, which allows you to add storage without restarting your VM, is deprecated and will be removed in a future release. This feature gate will be replaced by `DeclarativeHotplugVolumes`.

> [!NOTE]
> `DeclarativeHotplugVolumes` does not support hot plugging ephemeral volumes. Ephemeral volumes are hot plugged to a VMI and do not persist in the owner VM. Existing ephemeral volumes that are hot plugged are automatically detached after you switch to the `DeclarativeHotplugVolumes` feature gate.

[CNV-73301](https://issues.redhat.com/browse/CNV-73301)

# Removed features

Removed features are no longer supported in OpenShift Virtualization.

Predefined latency checkup feature removed
In previous versions, cluster and project administrators could use a predefined latency checkup to verify network connectivity and measure latency between two virtual machines (VMs) that are attached to a secondary network interface. With this release, the predefined latency checkup feature is removed.

[CNV-77646](https://issues.redhat.com/browse/CNV-77646)

Removed deprecated label from localnet network attachment definition type
The web console no longer displays a **Deprecated** label next to the localnet `NetworkAttachmentDefinition` (NAD) type. This change clarifies that localnet NAD functionality is not deprecated and remains fully supported. You can use either the NAD-based approach or the VM network wizard to create localnet networks for connecting virtual machines to physical networks.

[OCPBUGS-83809](https://redhat.atlassian.net/browse/OCPBUGS-83809)

# Technology Preview features

Some features in this release are currently in Technology Preview. These experimental features are not intended for production use. Note the following scope of support on the Red Hat Customer Portal for these features:

[Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview)

KubeVirt Redfish for VM management through the Redfish API (Technology Preview)
KubeVirt Redfish exposes OpenShift Virtualization virtual machines through the standard Redfish API. Using KubeVirt Redfish, administrators can manage VM power states, boot configuration, and virtual media attachments. This feature is available as a Technology Preview.

For more information, see [Install KubeVirt Redfish](../post_installation_configuration/virt-kubevirt-redfish.md#proc_virt-installing-kubevirt-redfish_virt-kubevirt-redfish).

<!-- -->

Golden image support for heterogeneous clusters (Technology Preview)
Golden image support is available for heterogeneous clusters, which enables you to create and use golden images for virtual machines in environments with differing node configurations. This capability is a Technology Preview feature.

[CNV-62357](https://issues.redhat.com/browse/CNV-62357)

<!-- -->

Custom video device support in virtual machines (Technology Preview)
You can now configure a custom video device type when creating a virtual machine. Configuring a custom device type overrides the default video configuration, and allows you to specify different video devices, based on your guest operating system requirements and performance needs. This capability is a Technology Preview feature.

[CNV-71192](https://issues.redhat.com/browse/CNV-71192)

<!-- -->

Convert an existing VM to a template from the user interface (Technology Preview)
Virtual machine (VM) owners can create, filter, and delete a user-generated template. You can create a template from an existing VM in the same project as the running VM or a different project from the OpenShift Virtualization user interface. To make sure that the data is consistent, stop the VM before you create a template. This capability is a Technology Preview feature.

[CNV-81577](https://redhat.atlassian.net/browse/CNV-81577)

<!-- -->

Create virtual machines from in-cluster native templates (Technology Preview)
Virtual machine (VM) owners can create VMs from the OpenShift Virtualization cluster native template custom resource. The VM template tracks a golden image that is updated periodically, reducing errors and ensuring uniformity in the virtualized environment. You can host the template in all namespaces that you can control.

[CNV-73392](https://redhat.atlassian.net/browse/CNV-73392)

<!-- -->

Dual stream support for OpenShift Virtualization clusters (Technology Preview)
You can provision OpenShift Virtualization clusters that run Red Hat Enterprise Linux CoreOS (RHCOS) version 9.8 and version 10.2 in OpenShift Container Platform 4.22. RHCOS 9.8 is the default operating system. VM live migration between RHCOS 9.x and RHCOS 10.x worker nodes is supported in OpenShift Container Platform 4.22.

[CNV-49964](https://redhat.atlassian.net/browse/CNV-49964)

KubeVirt Redfish for VM management through the Redfish API (Technology Preview)
KubeVirt Redfish exposes OpenShift Virtualization virtual machines through the standard Redfish API. Using KubeVirt Redfish, administrators can manage VM power states, boot configuration, and virtual media attachments. This feature is available as a Technology Preview.

For more information, see [Install KubeVirt Redfish](../post_installation_configuration/virt-kubevirt-redfish.md#proc_virt-installing-kubevirt-redfish_virt-kubevirt-redfish).

# Fixed issues

The following issues are fixed for this release.

Service account volumes preserved during VM migration
Before this update, migrating a virtual machine (VM) invalidated any service account volumes attached to that VM. As a consequence, workloads that relied on service account tokens failed after migration. With this release, service account volumes are preserved during VM migration. As a result, workloads that use service account tokens continue to function correctly after live migration.

[CNV-33835](https://issues.redhat.com/browse/CNV-33835)

# Known issues

Some linked Jira tickets are accessible only with Red Hat credentials.

Non-versioned HyperConverged commands default to v1 API
In this release, the v1 API for the `HyperConverged` custom resource (CR) is introduced, in preparation for a future migration from v1beta1 to v1. Due to the way Kubernetes selects default API versions, non-versioned commands such as `oc get hco`, `oc edit hyperconverged`, and `oc patch hyperconverged` now default to the v1 API. As a consequence, these commands can behave unexpectedly or fail because the v1 API is not yet ready for production use.

To work around this problem, use the fully versioned type name `hyperconvergeds.v1beta1.hco.kubevirt.io` when running commands against the `HyperConverged` CR. For example, use `oc get hyperconvergeds.v1beta1.hco.kubevirt.io` instead of `oc get hco`. For the `oc explain` command, use the `--api-version` flag: `oc explain --api-version=hco.kubevirt.io/v1beta1 hco.spec`. As a result, commands target the v1beta1 API as intended.

[CNV-78892](https://redhat.atlassian.net/browse/CNV-78892)

<!-- -->

VMs using the cnv-bridge CNI fail to live migrate after updates from 4.12
When you update from OpenShift Container Platform 4.12 to a newer minor version, virtual machines that use the `cnv-bridge` Container Network Interface (CNI) fail to live migrate. As a consequence, live migration fails for affected VMs.

To work around this problem, change the `spec.config.type` field in your `NetworkAttachmentDefinition` manifest from `cnv-bridge` to `bridge` before you perform the update. As a result, live migration succeeds for VMs that use the updated network attachment definitions.

[Known issue when migrating VMs that use the cnv-bridge CNI](https://access.redhat.com/solutions/7069807)

VMs might lose ingress connectivity after live migration over an EVPN-enabled network
When you live migrate a VM across OpenShift Container Platform clusters that leverage a Border Gateway Protocol Ethernet Virtual Private Network (BGP EVPN)-enabled user-defined network, the VM might lose ingress connectivity.

[OCPBUGS-86503](https://redhat.atlassian.net/browse/OCPBUGS-86503)

<!-- -->

Red Hat OpenShift Service Mesh 3.1.1 and Istio 1.25 and later are incompatible with OpenShift Virtualization
Red Hat OpenShift Service Mesh 3.1.1 and Istio versions 1.25 and later are incompatible with OpenShift Virtualization 4.22 because the `traffic.sidecar.istio.io/kubevirtInterfaces` annotation is deprecated. As a consequence, service mesh integration with OpenShift Virtualization can fail when you use these versions.

To work around this problem, when you install Service Mesh for integration with OpenShift Virtualization, select Red Hat OpenShift Service Mesh version 3.0.4 and Istio 1.24.4 instead of the default versions that are displayed in the web console.

[OSSM-10883](https://issues.redhat.com/browse/OSSM-10883)

<!-- -->

Node labels remain after uninstalling OpenShift Virtualization
Uninstalling OpenShift Virtualization does not remove the `feature.node.kubevirt.io` node labels that OpenShift Virtualization creates. As a consequence, nodes can still appear as if they are configured for virtualization workloads.

To work around this problem, manually remove the `feature.node.kubevirt.io` labels from affected nodes after you uninstall OpenShift Virtualization.

[CNV-38543](https://issues.redhat.com/browse/CNV-38543)

<!-- -->

Live migration fails when VM names exceed 47 characters
Live migration fails if a virtual machine name exceeds 47 characters. As a consequence, you cannot live migrate VMs with longer names.

To work around this problem, use VM names that are 47 characters or fewer when you create VMs that you plan to live migrate.

[CNV-61066](https://issues.redhat.com/browse/CNV-61066)

Upgrading to OpenShift Virtualization 4.22 when using wasp-agent
If you are upgrading OpenShift Virtualization from version 4.20 to 4.22 and using `wasp-agent` to increase VM workload density, you must perform the following steps after you begin the upgrade:

1.  Wait for the Machine Configuration Pool (MCP) to complete updating the control-plane nodes.

2.  Edit the `KubeletConfig` file to remove the `failSwapOn: false` key-value pair.

3.  Wait for the MCP to finish updating the worker nodes.

[CNV-89504](https://redhat.atlassian.net/browse/CNV-89504)

# Maintenance releases

## OpenShift Virtualization 4.22.2 updates

OpenShift Virtualization 4.22.2 is now available with updates to packages and images that fix several bugs and add enhancements.

### New features and enhancements

Self-service Technical Supportability Review
You can use the self-service Technical Supportability Review (TSR) on the Red Hat Customer Portal to validate your cluster configuration against Red Hat common practices. The self-service TSR uses AI to evaluate your cluster’s `must-gather` data and provides a prioritized executive summary that identifies your cluster’s top risks and recommends corrective actions. The TSR performs hundreds of checks across the OpenShift Container Platform platform, including OpenShift Virtualization, and coverage is continually expanding.

For more information, see [Technical Supportability Review with AI tool](https://access.redhat.com/support/cases/#/analyze) and [Red Hat Technical Supportability Review with AI: Proactive AI-Driven Cluster Assessments for OpenShift Container Platform](https://access.redhat.com/solutions/7141255).
