<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Before you begin an installation using installer-provisioned infrastructure, be sure that your vSphere environment meets the following installation requirements.

# VMware vSphere infrastructure requirements

You must install an OpenShift Container Platform cluster on one of the following versions of a VMware vSphere instance that meets the requirements for the components that you use:

- Version 8.0 Update 1 or later, or VMware Cloud Foundation 5.0 or later

- VMware vSphere Foundation 9 or later, or VMware Cloud Foundation 9 or later

Both of these releases support Container Storage Interface (CSI) migration, which is enabled by default on OpenShift Container Platform 4.17.

> [!NOTE]
> Red Hat follows Broadcom’s End of Support dates for VMware products that OpenShift Container Platform runs on. After a VMware product version reaches End of Support, that version is no longer supported for use with OpenShift Container Platform.

You can host the VMware vSphere infrastructure on-premise or on a [VMware Cloud Verified provider](https://cloud.vmware.com/providers) that meets the requirements outlined in the following tables:

| Virtual environment product | Required version |
|----|----|
| VMware virtual hardware | 15 or later |
| vSphere ESXi hosts | 8.0 Update 1 or later, or VMware vSphere Foundation 9 or later; VMware Cloud Foundation 5.0 or later, or VMware Cloud Foundation 9 or later |
| vCenter host | 8.0 Update 1 or later, or VMware vSphere Foundation 9 or later; VMware Cloud Foundation 5.0 or later, or VMware Cloud Foundation 9 or later |

Version requirements for vSphere virtual environments

> [!IMPORTANT]
> You must ensure that the time on your ESXi hosts is synchronized before you install OpenShift Container Platform. See [Edit Time Configuration for a Host](https://docs.vmware.com/en/VMware-vSphere/6.7/com.vmware.vsphere.vcenterhost.doc/GUID-8756D419-A878-4AE0-9183-C6D5A91A8FB1.html) in the VMware documentation.

| Component | Minimum supported versions | Description |
|----|----|----|
| Hypervisor | vSphere 8.0 Update 1 or later, or VMware Cloud Foundation 5.0 or later with virtual hardware version 15; VMware vSphere Foundation 9 or later, or VMware Cloud Foundation 9 or later | This hypervisor version is the minimum version that Red Hat Enterprise Linux CoreOS (RHCOS) supports. For more information about supported hardware on the latest version of Red Hat Enterprise Linux (RHEL) that is compatible with RHCOS, see [Hardware](https://catalog.redhat.com/hardware/search) on the Red Hat Customer Portal. |
| Networking (NSX) | vSphere 8.0 Update 1 or later, or VMware Cloud Foundation 5.0 or later; VMware vSphere Foundation 9 or later, or VMware Cloud Foundation 9 or later | Red Hat uses the Partner Certification process to verify NSX compatibility. |
| CPU micro-architecture | x86-64-v2 or higher | OpenShift Container Platform version 4.13 and later are based on the RHEL 9.2 host operating system, which raised the microarchitecture requirements to x86-64-v2. See [Architectures](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/9/html-single/9.2_release_notes/index#architectures) in the RHEL documentation. |

Minimum supported vSphere version for VMware components

> [!IMPORTANT]
> To ensure the best performance conditions for your cluster workloads that operate on Oracle® Cloud Infrastructure (OCI) and on the Oracle® Cloud VMware Solution (OCVS) service, ensure volume performance units (VPUs) for your block volume are sized for your workloads.
>
> The following list provides some guidance in selecting the VPUs needed for specific performance needs:
>
> - Test or proof of concept environment: 100 GB, and 20 to 30 VPUs.
>
> - Base-production environment: 500 GB, and 60 VPUs.
>
> - Heavy-use production environment: More than 500 GB, and 100 or more VPUs.
>
> Consider allocating additional VPUs to give enough capacity for updates and scaling activities. See [Block Volume Performance Levels (Oracle documentation)](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/blockvolumeperformance.htm).

> [!NOTE]
> The following additional VMware vSphere Foundation and VMware Cloud Foundation components are outside the scope of Red Hat support:
>
> - Management: VCF Operations, VCF Automation, VCF Fleet Management, and VCF Identity Broker.
>
> - Networking: VMware NSX Container Plugin (NCP).
>
> - Migration: VMware HCX.

# Network connectivity requirements

You must configure the network connectivity between machines to allow OpenShift Container Platform cluster components to communicate.

Review the following details about the required network ports.

| Protocol | Port | Description |
|----|----|----|
| VRRP | N/A | Required for keepalived |
| ICMP | N/A | Network reachability tests |
| TCP | `1936` | Metrics |
| `9000`-`9999` | Host level services, including the node exporter on ports `9100`-`9101` and the Cluster Version Operator on port `9099`. |  |
| `10250`-`10259` | The default ports that Kubernetes reserves |  |
| UDP | `6081` | Geneve |
| `9000`-`9999` | Host level services, including the node exporter on ports `9100`-`9101`. |  |
| `500` | IPsec IKE packets |  |
| `4500` | IPsec NAT-T packets |  |
| TCP/UDP | `30000`-`32767` |  |
| Kubernetes node port | ESP | N/A |

Ports used for all-machine to all-machine communications

| Protocol | Port   | Description    |
|----------|--------|----------------|
| TCP      | `6443` | Kubernetes API |

Ports used for all-machine to control plane communications

| Protocol | Port          | Description                |
|----------|---------------|----------------------------|
| TCP      | `2379`-`2380` | etcd server and peer ports |

Ports used for control plane machine to control plane machine communications

# VMware vSphere CSI Driver Operator requirements

To install the vSphere Container Storage Interface (CSI) Driver Operator, the following requirements must be met:

- VMware vSphere version 8.0 Update 1 or later; or VMware vSphere Foundation (VVF) 9; or VMware Cloud Foundation (VCF) 5 or later

- vCenter version 8.0 Update 1 or later; or VVF 9; or VCF 5 or later

- Virtual machines of hardware version 15 or later

- No third-party vSphere CSI driver already installed in the cluster

If a third-party vSphere CSI driver is present in the cluster, OpenShift Container Platform does not overwrite it. The presence of a third-party vSphere CSI driver prevents OpenShift Container Platform from updating to OpenShift Container Platform 4.13 or later.

> [!NOTE]
> The VMware vSphere CSI Driver Operator is supported only on clusters deployed with `platform: vsphere` in the installation manifest.

You can create a custom role for the Container Storage Interface (CSI) driver, the vSphere CSI Driver Operator, and the vSphere Problem Detector Operator. The custom role can include privilege sets that assign a minimum set of permissions to each vSphere object. This means that the CSI driver, the vSphere CSI Driver Operator, and the vSphere Problem Detector Operator can establish a basic interaction with these objects.

> [!IMPORTANT]
> Installing an OpenShift Container Platform cluster in a vCenter is tested against a full list of privileges as described in the "Required vCenter account privileges" section. By adhering to the full list of privileges, you can reduce the possibility of unexpected and unsupported behaviors that might occur when creating a custom role with a set of restricted privileges.

<div>

<div class="title">

Additional resources

</div>

- To remove a third-party vSphere CSI driver, see [Removing a third-party vSphere CSI Driver](../../../storage/container_storage_interface/persistent-storage-csi-vsphere.md#persistent-storage-csi-vsphere-install-issues_persistent-storage-csi-vsphere).

- To update the hardware version for your vSphere nodes, see [Updating hardware on nodes running in vSphere](../../../updating/updating_a_cluster/updating-hardware-on-nodes-running-on-vsphere.md#updating-hardware-on-nodes-running-on-vsphere).

- [Minimum permissions for the storage components](ipi-vsphere-installation-reqs.md#installation-vsphere-minimum-permissions-storage_ipi-vsphere-installation-reqs)

</div>

# vCenter requirements

Before you install an OpenShift Container Platform cluster on your vCenter that uses infrastructure that the installation program provisions, you must prepare your environment.

## Required vCenter account privileges

To install an OpenShift Container Platform cluster in a vCenter, the installation program requires access to an account with privileges to read and create the required resources. Using an account that has global administrative privileges is the simplest way to access all of the necessary permissions.

If you cannot use an account with global administrative privileges, you must create roles to grant the privileges necessary for OpenShift Container Platform cluster installation. Most of the privileges are always required. Some privileges are required only if you plan for the installation program to provision a folder to contain the OpenShift Container Platform cluster on your vCenter instance, which is the default behavior. You must create or change vSphere roles for the specified objects to grant the required privileges.

The installation program requires an additional role to create a vSphere virtual machine folder.

> [!NOTE]
> The following tables do not explicitly list the ESXi host object. In the vSphere hierarchy, ESXi hosts are child objects of the cluster. If you apply your custom role to the vSphere vCenter Cluster object with the "Propagate to children" setting enabled, the required privileges automatically propagate down to the ESXi hosts. You do not need to apply permissions directly to individual ESXi host objects.

<div class="example">

<div class="title">

Roles and privileges required for installation in vSphere API

</div>

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">vSphere object for role</th>
<th style="text-align: left;">When required</th>
<th style="text-align: left;">Required privileges in vSphere API</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>vSphere vCenter</p></td>
<td style="text-align: left;"><p>Always</p></td>
<td style="text-align: left;"><p><code>Cns.Searchable</code><br />
<code>InventoryService.Tagging.AttachTag</code><br />
<code>InventoryService.Tagging.CreateCategory</code><br />
<code>InventoryService.Tagging.CreateTag</code><br />
<code>InventoryService.Tagging.DeleteCategory</code><br />
<code>InventoryService.Tagging.DeleteTag</code><br />
<code>InventoryService.Tagging.EditCategory</code><br />
<code>InventoryService.Tagging.EditTag</code><br />
<code>Sessions.ValidateSession</code><br />
<code>StorageProfile.Update</code><br />
<code>StorageProfile.View</code></p></td>
</tr>
<tr>
<td style="text-align: left;"><p>vSphere vCenter Cluster</p></td>
<td style="text-align: left;"><p>Always</p></td>
<td style="text-align: left;"><p><code>Host.Config.Storage</code><br />
<code>Resource.AssignVMToPool</code><br />
<code>VApp.AssignResourcePool</code><br />
<code>VApp.Import</code><br />
<code>VirtualMachine.Config.AddNewDisk</code></p></td>
</tr>
<tr>
<td style="text-align: left;"><p>vSphere vCenter Resource Pool</p></td>
<td style="text-align: left;"><p>For a provided existing resource pool</p></td>
<td style="text-align: left;"><p><code>Resource.AssignVMToPool</code><br />
<code>VApp.AssignResourcePool</code><br />
<code>VApp.Import</code><br />
<code>VirtualMachine.Config.AddNewDisk</code></p></td>
</tr>
<tr>
<td style="text-align: left;"><p>vSphere Datastore</p></td>
<td style="text-align: left;"><p>Always</p></td>
<td style="text-align: left;"><p><code>Datastore.AllocateSpace</code><br />
<code>Datastore.Browse</code><br />
<code>Datastore.FileManagement</code><br />
<code>InventoryService.Tagging.ObjectAttachable</code></p></td>
</tr>
<tr>
<td style="text-align: left;"><p>vSphere Port Group</p></td>
<td style="text-align: left;"><p>Always</p></td>
<td style="text-align: left;"><p><code>Network.Assign</code></p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Virtual Machine Folder</p></td>
<td style="text-align: left;"><p>Always</p></td>
<td style="text-align: left;"><p><code>InventoryService.Tagging.ObjectAttachable</code><br />
<code>Resource.AssignVMToPool</code><br />
<code>VApp.Import</code><br />
<code>VirtualMachine.Config.AddExistingDisk</code><br />
<code>VirtualMachine.Config.AddNewDisk</code><br />
<code>VirtualMachine.Config.AddRemoveDevice</code><br />
<code>VirtualMachine.Config.AdvancedConfig</code><br />
<code>VirtualMachine.Config.Annotation</code><br />
<code>VirtualMachine.Config.CPUCount</code><br />
<code>VirtualMachine.Config.DiskExtend</code><br />
<code>VirtualMachine.Config.DiskLease</code><br />
<code>VirtualMachine.Config.EditDevice</code><br />
<code>VirtualMachine.Config.Memory</code><br />
<code>VirtualMachine.Config.RemoveDisk</code><br />
<code>VirtualMachine.Config.Rename</code><br />
<code>Host.Config.Storage</code><br />
<code>VirtualMachine.Config.ResetGuestInfo</code><br />
<code>VirtualMachine.Config.Resource</code><br />
<code>VirtualMachine.Config.Settings</code><br />
<code>VirtualMachine.Config.UpgradeVirtualHardware</code><br />
<code>VirtualMachine.Interact.GuestControl</code><br />
<code>VirtualMachine.Interact.PowerOff</code><br />
<code>VirtualMachine.Interact.PowerOn</code><br />
<code>VirtualMachine.Interact.Reset</code><br />
<code>VirtualMachine.Inventory.Create</code><br />
<code>VirtualMachine.Inventory.CreateFromExisting</code><br />
<code>VirtualMachine.Inventory.Delete</code><br />
<code>VirtualMachine.Provisioning.Clone</code><br />
<code>VirtualMachine.Provisioning.MarkAsTemplate</code><br />
<code>VirtualMachine.Provisioning.DeployTemplate</code></p></td>
</tr>
<tr>
<td style="text-align: left;"><p>vSphere vCenter data center</p></td>
<td style="text-align: left;"><p>The installation program creates the virtual machine folder.</p></td>
<td style="text-align: left;"><p><code>InventoryService.Tagging.ObjectAttachable</code><br />
<code>Resource.AssignVMToPool</code><br />
<code>VirtualMachine.Config.AddExistingDisk</code><br />
<code>VirtualMachine.Config.AddNewDisk</code><br />
<code>VirtualMachine.Config.AddRemoveDevice</code><br />
<code>VirtualMachine.Config.AdvancedConfig</code><br />
<code>VirtualMachine.Config.Annotation</code><br />
<code>VirtualMachine.Config.CPUCount</code><br />
<code>VirtualMachine.Config.DiskExtend</code><br />
<code>VirtualMachine.Config.DiskLease</code><br />
<code>VirtualMachine.Config.EditDevice</code><br />
<code>VirtualMachine.Config.Memory</code><br />
<code>VirtualMachine.Config.RemoveDisk</code><br />
<code>VirtualMachine.Config.Rename</code><br />
<code>VirtualMachine.Config.ResetGuestInfo</code><br />
<code>VirtualMachine.Config.Resource</code><br />
<code>VirtualMachine.Config.Settings</code><br />
<code>VirtualMachine.Config.UpgradeVirtualHardware</code><br />
<code>VirtualMachine.Interact.GuestControl</code><br />
<code>VirtualMachine.Interact.PowerOff</code><br />
<code>VirtualMachine.Interact.PowerOn</code><br />
<code>VirtualMachine.Interact.Reset</code><br />
<code>VirtualMachine.Inventory.Create</code><br />
<code>VirtualMachine.Inventory.CreateFromExisting</code><br />
<code>VirtualMachine.Inventory.Delete</code><br />
<code>VirtualMachine.Provisioning.Clone</code><br />
<code>VirtualMachine.Provisioning.DeployTemplate</code><br />
<code>VirtualMachine.Provisioning.MarkAsTemplate</code><br />
<code>Folder.Create</code><br />
<code>Folder.Delete</code></p></td>
</tr>
</tbody>
</table>

</div>

<div class="example">

<div class="title">

Roles and privileges required for installation in vCenter graphical user interface (GUI)

</div>

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 37%" />
<col style="width: 37%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">vSphere object for role</th>
<th style="text-align: left;">When required</th>
<th style="text-align: left;">Required privileges in vCenter GUI</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>vSphere vCenter</p></td>
<td style="text-align: left;"><p>Always</p></td>
<td style="text-align: left;"><p><code>Cns.Searchable</code><br />
<code>"vSphere Tagging"."Assign or Unassign vSphere Tag"</code><br />
<code>"vSphere Tagging"."Create vSphere Tag Category"</code><br />
<code>"vSphere Tagging"."Create vSphere Tag"</code><br />
<code>vSphere Tagging"."Delete vSphere Tag Category"</code><br />
<code>"vSphere Tagging"."Delete vSphere Tag"</code><br />
<code>"vSphere Tagging"."Edit vSphere Tag Category"</code><br />
<code>"vSphere Tagging"."Edit vSphere Tag"</code><br />
<code>Sessions."Validate session"</code><br />
<code>"VM storage policies"."Update VM storage policies"</code><br />
<code>"VM storage policies"."View VM storage policies"</code></p></td>
</tr>
<tr>
<td style="text-align: left;"><p>vSphere vCenter Cluster</p></td>
<td style="text-align: left;"><p>Always</p></td>
<td style="text-align: left;"><p><code>Host.Configuration."Storage partition configuration"</code><br />
<code>Resource."Assign virtual machine to resource pool"</code><br />
<code>VApp."Assign resource pool"</code><br />
<code>VApp.Import</code><br />
<code>"Virtual machine"."Change Configuration"."Add new disk"</code></p></td>
</tr>
<tr>
<td style="text-align: left;"><p>vSphere vCenter Resource Pool</p></td>
<td style="text-align: left;"><p>If providing an existing resource pool</p></td>
<td style="text-align: left;"><p><code>Host.Configuration."Storage partition configuration"</code><br />
<code>Resource."Assign virtual machine to resource pool"</code><br />
<code>VApp."Assign resource pool"</code><br />
<code>VApp.Import</code><br />
<code>"Virtual machine"."Change Configuration"."Add new disk"</code></p></td>
</tr>
<tr>
<td style="text-align: left;"><p>vSphere Datastore</p></td>
<td style="text-align: left;"><p>Always</p></td>
<td style="text-align: left;"><p><code>Datastore."Allocate space"</code><br />
<code>Datastore."Browse datastore"</code><br />
<code>Datastore."Low level file operations"</code><br />
<code>"vSphere Tagging"."Assign or Unassign vSphere Tag on Object"</code></p></td>
</tr>
<tr>
<td style="text-align: left;"><p>vSphere Port Group</p></td>
<td style="text-align: left;"><p>Always</p></td>
<td style="text-align: left;"><p><code>Network."Assign network"</code></p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Virtual Machine Folder</p></td>
<td style="text-align: left;"><p>Always</p></td>
<td style="text-align: left;"><p><code>"vSphere Tagging"."Assign or Unassign vSphere Tag on Object"</code><br />
<code>Resource."Assign virtual machine to resource pool"</code><br />
<code>VApp.Import</code><br />
<code>"Virtual machine"."Change Configuration"."Add existing disk"</code><br />
<code>"Virtual machine"."Change Configuration"."Add new disk"</code><br />
<code>"Virtual machine"."Change Configuration"."Add or remove device"</code><br />
<code>"Virtual machine"."Change Configuration"."Advanced configuration"</code><br />
<code>"Virtual machine"."Change Configuration"."Set annotation"</code><br />
<code>"Virtual machine"."Change Configuration"."Change CPU count"</code><br />
<code>"Virtual machine"."Change Configuration"."Extend virtual disk"</code><br />
<code>"Virtual machine"."Change Configuration"."Acquire disk lease"</code><br />
<code>"Virtual machine"."Change Configuration"."Modify device settings"</code><br />
<code>"Virtual machine"."Change Configuration"."Change Memory"</code><br />
<code>"Virtual machine"."Change Configuration"."Remove disk"</code><br />
<code>"Virtual machine"."Change Configuration".Rename</code><br />
<code>"Virtual machine"."Change Configuration"."Reset guest information"</code><br />
<code>"Virtual machine"."Change Configuration"."Change resource"</code><br />
<code>"Virtual machine"."Change Configuration"."Change Settings"</code><br />
<code>"Virtual machine"."Change Configuration"."Upgrade virtual machine compatibility"</code><br />
<code>"Virtual machine".Interaction."Guest operating system management by VIX API"</code><br />
<code>"Virtual machine".Interaction."Power off"</code><br />
<code>"Virtual machine".Interaction."Power on"</code><br />
<code>"Virtual machine".Interaction.Reset</code><br />
<code>"Virtual machine"."Edit Inventory"."Create new"</code><br />
<code>"Virtual machine"."Edit Inventory"."Create from existing"</code><br />
<code>"Virtual machine"."Edit Inventory"."Remove"</code><br />
<code>"Virtual machine".Provisioning."Clone virtual machine"</code><br />
<code>"Virtual machine".Provisioning."Mark as template"</code><br />
<code>"Virtual machine".Provisioning."Deploy template"</code></p></td>
</tr>
<tr>
<td style="text-align: left;"><p>vSphere vCenter data center</p></td>
<td style="text-align: left;"><p>The installation program creates the virtual machine folder.</p></td>
<td style="text-align: left;"><p><code>"vSphere Tagging"."Assign or Unassign vSphere Tag on Object"</code><br />
<code>Resource."Assign virtual machine to resource pool"</code><br />
<code>VApp.Import</code><br />
<code>"Virtual machine"."Change Configuration"."Add existing disk"</code><br />
<code>"Virtual machine"."Change Configuration"."Add new disk"</code><br />
<code>"Virtual machine"."Change Configuration"."Add or remove device"</code><br />
<code>"Virtual machine"."Change Configuration"."Advanced configuration"</code><br />
<code>"Virtual machine"."Change Configuration"."Set annotation"</code><br />
<code>"Virtual machine"."Change Configuration"."Change CPU count"</code><br />
<code>"Virtual machine"."Change Configuration"."Extend virtual disk"</code><br />
<code>"Virtual machine"."Change Configuration"."Acquire disk lease"</code><br />
<code>"Virtual machine"."Change Configuration"."Modify device settings"</code><br />
<code>"Virtual machine"."Change Configuration"."Change Memory"</code><br />
<code>"Virtual machine"."Change Configuration"."Remove disk"</code><br />
<code>"Virtual machine"."Change Configuration".Rename</code><br />
<code>"Virtual machine"."Change Configuration"."Reset guest information"</code><br />
<code>"Virtual machine"."Change Configuration"."Change resource"</code><br />
<code>"Virtual machine"."Change Configuration"."Change Settings"</code><br />
<code>"Virtual machine"."Change Configuration"."Upgrade virtual machine compatibility"</code><br />
<code>"Virtual machine".Interaction."Guest operating system management by VIX API"</code><br />
<code>"Virtual machine".Interaction."Power off"</code><br />
<code>"Virtual machine".Interaction."Power on"</code><br />
<code>"Virtual machine".Interaction.Reset</code><br />
<code>"Virtual machine"."Edit Inventory"."Create new"</code><br />
<code>"Virtual machine"."Edit Inventory"."Create from existing"</code><br />
<code>"Virtual machine"."Edit Inventory"."Remove"</code><br />
<code>"Virtual machine".Provisioning."Clone virtual machine"</code><br />
<code>"Virtual machine".Provisioning."Deploy template"</code><br />
<code>"Virtual machine".Provisioning."Mark as template"</code><br />
<code>Folder."Create folder"</code><br />
<code>Folder."Delete folder"</code></p></td>
</tr>
</tbody>
</table>

</div>

Additionally, the user requires some `ReadOnly` permissions, and some of the roles require permission to propagate the permissions to child objects. These settings vary depending on whether or not you install the cluster into an existing folder.

<div class="example">

<div class="title">

Required permissions and propagation settings

</div>

| vSphere object | When required | Propagate to children | Permissions required |
|----|----|----|----|
| vSphere vCenter | Always | False | Listed required privileges |
| vSphere vCenter data center | Existing folder | False | `ReadOnly` permission |
| Installation program creates the folder | True | Listed required privileges |  |
| vSphere vCenter Cluster | Always | True | Listed required privileges |
| vSphere vCenter Datastore | Always | False | Listed required privileges |
| vSphere Switch | Always | False | `ReadOnly` permission |
| vSphere Port Group | Always | False | Listed required privileges |
| vSphere vCenter Virtual Machine Folder | Existing folder | True | Listed required privileges |
| vSphere vCenter Resource Pool | Existing resource pool | True | Listed required privileges |

</div>

For more information about creating an account with only the required privileges, see [vSphere Permissions and User Management Tasks](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.security.doc/GUID-5372F580-5C23-4E9C-8A4E-EF1B4DD9033E.html) in the vSphere documentation.

## Minimum required vCenter account privileges

After you create a custom role and assign privileges to the role, you can create permissions by selecting specific vSphere objects. You can then assign the custom role to a user or group for each object.

Before you create permissions or request for the creation of permissions for a vSphere object, decide what minimum permissions apply to the vSphere object. By doing this task, you can ensure a basic interaction exists between a vSphere object and OpenShift Container Platform architecture.

> [!IMPORTANT]
> If you create a custom role and you do not assign privileges to it, the vSphere Server by default assigns a `Read Only` role to the custom role. Note that for the cloud provider API, the custom role only needs to inherit the privileges of the `Read Only` role.

Consider creating a custom role when an account with global administrative privileges does not meet your needs.

> [!IMPORTANT]
> Red Hat does not support configuring an account without including the required privileges. Red Hat tests OpenShift Container Platform cluster installations in vCenter against the full list of privileges described in the "Required vCenter account privileges" section. By adhering to the full list of privileges, you can reduce the possibility of unexpected behaviors that might occur when creating a custom role with a restricted set of privileges. You must retain the full set of privileges from the "Required vCenter account privileges" section after cluster installation. Reducing the account to only the permissions listed in the minimum permission tables in the "Minimum required vCenter account privileges" section after installation is not supported and can cause unexpected cluster behavior. The minimum permission tables are for reference only; they show which privileges apply to which OpenShift Container Platform components (such as storage or the Machine API) when you design or audit custom roles. The supported configuration is to assign the full set of privileges from the "Required vCenter account privileges" section at all times, both during and after installation.

The following tables specify how the required vCenter account privileges provided earlier in this document are relevant to different aspects of OpenShift Container Platform architecture.

<div id="installation-vsphere-minimum-permissions-ipi_ipi-vsphere-installation-reqs" class="example">

<div class="title">

Minimum permissions on installer-provisioned infrastructure

</div>

<table>
<colgroup>
<col style="width: 36%" />
<col style="width: 36%" />
<col style="width: 27%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">vSphere object for role</th>
<th style="text-align: left;">When required</th>
<th style="text-align: left;">Required privileges</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>vSphere vCenter</p></td>
<td style="text-align: left;"><p>Always</p></td>
<td style="text-align: left;"><p><code>Cns.Searchable</code><br />
<code>InventoryService.Tagging.AttachTag</code><br />
<code>InventoryService.Tagging.CreateCategory</code><br />
<code>InventoryService.Tagging.CreateTag</code><br />
<code>InventoryService.Tagging.DeleteCategory</code><br />
<code>InventoryService.Tagging.DeleteTag</code><br />
<code>InventoryService.Tagging.EditCategory</code><br />
<code>InventoryService.Tagging.EditTag</code><br />
<code>Sessions.ValidateSession</code><br />
<code>StorageProfile.Update</code><br />
<code>StorageProfile.View</code></p></td>
</tr>
<tr>
<td style="text-align: left;"><p>vSphere vCenter Cluster</p></td>
<td style="text-align: left;"><p>If you intend to create VMs in the cluster root</p></td>
<td style="text-align: left;"><p><code>Host.Config.Storage</code><br />
<code>Resource.AssignVMToPool</code><br />
<code>VApp.AssignResourcePool</code><br />
<code>VApp.Import</code><br />
<code>VirtualMachine.Config.AddNewDisk</code></p></td>
</tr>
<tr>
<td style="text-align: left;"><p>vSphere vCenter Resource Pool</p></td>
<td style="text-align: left;"><p>If you included an existing resource pool in the <code>install-config.yaml</code> file</p></td>
<td style="text-align: left;"><p><code>Host.Config.Storage</code><br />
<code>Resource.AssignVMToPool</code><br />
<code>VApp.AssignResourcePool</code><br />
<code>VApp.Import`minimum</code></p></td>
</tr>
<tr>
<td style="text-align: left;"><p>vSphere Datastore</p></td>
<td style="text-align: left;"><p>If you referenced a datastore in the <code>install-config.yaml</code> file</p></td>
<td style="text-align: left;"><p><code>Datastore.Browse</code><br />
<code>Datastore.FileManagement</code><br />
<code>InventoryService.Tagging.ObjectAttachable</code></p></td>
</tr>
<tr>
<td style="text-align: left;"><p>vSphere Port Group</p></td>
<td style="text-align: left;"><p>Always</p></td>
<td style="text-align: left;"><p><code>Network.Assign</code></p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Virtual Machine Folder</p></td>
<td style="text-align: left;"><p>Always</p></td>
<td style="text-align: left;"><p><code>InventoryService.Tagging.ObjectAttachable</code><br />
<code>Resource.AssignVMToPool</code><br />
<code>VApp.Import</code><br />
<code>VirtualMachine.Config.AddExistingDisk</code><br />
<code>VirtualMachine.Config.AddNewDisk</code><br />
<code>VirtualMachine.Config.AddRemoveDevice</code><br />
<code>VirtualMachine.Config.AdvancedConfig</code><br />
<code>VirtualMachine.Config.Annotation</code><br />
<code>VirtualMachine.Config.CPUCount</code><br />
<code>VirtualMachine.Config.DiskExtend</code><br />
<code>VirtualMachine.Config.DiskLease</code><br />
<code>VirtualMachine.Config.EditDevice</code><br />
<code>VirtualMachine.Config.Memory</code><br />
<code>VirtualMachine.Config.RemoveDisk</code><br />
<code>VirtualMachine.Config.Rename</code><br />
<code>VirtualMachine.Config.ResetGuestInfo</code><br />
<code>VirtualMachine.Config.Resource</code><br />
<code>VirtualMachine.Config.Settings</code><br />
<code>VirtualMachine.Config.UpgradeVirtualHardware</code><br />
<code>VirtualMachine.Interact.GuestControl</code><br />
<code>VirtualMachine.Interact.PowerOff</code><br />
<code>VirtualMachine.Interact.PowerOn</code><br />
<code>VirtualMachine.Interact.Reset</code><br />
<code>VirtualMachine.Inventory.Create</code><br />
<code>VirtualMachine.Inventory.CreateFromExisting</code><br />
<code>VirtualMachine.Inventory.Delete</code><br />
<code>VirtualMachine.Provisioning.Clone</code><br />
<code>VirtualMachine.Provisioning.MarkAsTemplate</code><br />
<code>VirtualMachine.Provisioning.DeployTemplate</code></p></td>
</tr>
<tr>
<td style="text-align: left;"><p>vSphere vCenter data center</p></td>
<td style="text-align: left;"><p>If the virtual machine folder does not already exist, the installation program creates the virtual machine folder. If your cluster does use the Machine API and you want to set the minimum set of permissions for the API, see the "Minimum permissions for the Machine API" table.</p></td>
<td style="text-align: left;"><p><code>Folder.Create</code><br />
<code>Folder.Delete</code><br />
<code>InventoryService.Tagging.ObjectAttachable</code><br />
<code>Resource.AssignVMToPool</code><br />
<code>VApp.Import</code><br />
<code>VirtualMachine.Config.AddExistingDisk</code><br />
<code>VirtualMachine.Config.AddNewDisk</code><br />
<code>VirtualMachine.Config.AddRemoveDevice</code><br />
<code>VirtualMachine.Config.AdvancedConfig</code><br />
<code>VirtualMachine.Config.Annotation</code><br />
<code>VirtualMachine.Config.CPUCount</code><br />
<code>VirtualMachine.Config.DiskExtend</code><br />
<code>VirtualMachine.Config.DiskLease</code><br />
<code>VirtualMachine.Config.EditDevice</code><br />
<code>VirtualMachine.Config.Memory</code><br />
<code>VirtualMachine.Config.RemoveDisk</code><br />
<code>VirtualMachine.Config.Rename</code><br />
<code>VirtualMachine.Config.ResetGuestInfo</code><br />
<code>VirtualMachine.Config.Resource</code><br />
<code>VirtualMachine.Config.Settings</code><br />
<code>VirtualMachine.Config.UpgradeVirtualHardware</code><br />
<code>VirtualMachine.Interact.GuestControl</code><br />
<code>VirtualMachine.Interact.PowerOff</code><br />
<code>VirtualMachine.Interact.PowerOn</code><br />
<code>VirtualMachine.Interact.Reset</code><br />
<code>VirtualMachine.Inventory.Create</code><br />
<code>VirtualMachine.Inventory.CreateFromExisting</code><br />
<code>VirtualMachine.Inventory.Delete</code><br />
<code>VirtualMachine.Provisioning.Clone</code><br />
<code>VirtualMachine.Provisioning.DeployTemplate</code><br />
<code>VirtualMachine.Provisioning.MarkAsTemplate</code></p></td>
</tr>
</tbody>
</table>

</div>

<div id="post-installation-vsphere-minimum-permissions_ipi-vsphere-installation-reqs" class="example">

<div class="title">

Minimum permissions for postinstallation management of components

</div>

<table>
<colgroup>
<col style="width: 36%" />
<col style="width: 36%" />
<col style="width: 27%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">vSphere object for role</th>
<th style="text-align: left;">When required</th>
<th style="text-align: left;">Required privileges</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>vSphere vCenter</p></td>
<td style="text-align: left;"><p>Always</p></td>
<td style="text-align: left;"><p><code>Cns.Searchable</code><br />
<code>InventoryService.Tagging.AttachTag</code><br />
<code>InventoryService.Tagging.CreateCategory</code><br />
<code>InventoryService.Tagging.CreateTag</code><br />
<code>InventoryService.Tagging.DeleteCategory</code><br />
<code>InventoryService.Tagging.DeleteTag</code><br />
<code>InventoryService.Tagging.EditCategory</code><br />
<code>InventoryService.Tagging.EditTag</code><br />
<code>Sessions.ValidateSession</code><br />
<code>StorageProfile.Update</code><br />
<code>StorageProfile.View</code></p></td>
</tr>
<tr>
<td style="text-align: left;"><p>vSphere vCenter Cluster</p></td>
<td style="text-align: left;"><p>If you intend to create VMs in the cluster root</p></td>
<td style="text-align: left;"><p><code>Host.Config.Storage</code><br />
<code>Resource.AssignVMToPool</code></p></td>
</tr>
<tr>
<td style="text-align: left;"><p>vSphere vCenter Resource Pool</p></td>
<td style="text-align: left;"><p>If you included an existing resource pool in the <code>install-config.yaml</code> file</p></td>
<td style="text-align: left;"><p><code>Host.Config.Storage</code></p></td>
</tr>
<tr>
<td style="text-align: left;"><p>vSphere Datastore</p></td>
<td style="text-align: left;"><p>Always</p></td>
<td style="text-align: left;"><p><code>Datastore.AllocateSpace</code><br />
<code>Datastore.Browse</code><br />
<code>Datastore.FileManagement</code><br />
<code>InventoryService.Tagging.ObjectAttachable</code></p></td>
</tr>
<tr>
<td style="text-align: left;"><p>vSphere Port Group</p></td>
<td style="text-align: left;"><p>Always</p></td>
<td style="text-align: left;"><p><code>Network.Assign</code></p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Virtual Machine Folder</p></td>
<td style="text-align: left;"><p>Always</p></td>
<td style="text-align: left;"><p><code>VirtualMachine.Config.AddExistingDisk</code><br />
<code>VirtualMachine.Config.AddRemoveDevice</code><br />
<code>VirtualMachine.Config.AdvancedConfig</code><br />
<code>VirtualMachine.Config.Annotation</code><br />
<code>VirtualMachine.Config.CPUCount</code><br />
<code>VirtualMachine.Config.DiskExtend</code><br />
<code>VirtualMachine.Config.Memory</code><br />
<code>VirtualMachine.Config.Settings</code><br />
<code>VirtualMachine.Interact.PowerOff</code><br />
<code>VirtualMachine.Interact.PowerOn</code><br />
<code>VirtualMachine.Inventory.CreateFromExisting</code><br />
<code>VirtualMachine.Inventory.Delete</code><br />
<code>VirtualMachine.Provisioning.Clone</code><br />
<code>VirtualMachine.Provisioning.DeployTemplate</code></p></td>
</tr>
<tr>
<td style="text-align: left;"><p>vSphere vCenter data center</p></td>
<td style="text-align: left;"><p>If the virtual machine folder does not already exist, the installation program creates the virtual machine folder.</p></td>
<td style="text-align: left;"><p><code>Resource.AssignVMToPool</code><br />
<code>VirtualMachine.Config.AddExistingDisk</code><br />
<code>VirtualMachine.Config.AddRemoveDevice</code><br />
<code>VirtualMachine.Interact.PowerOff</code><br />
<code>VirtualMachine.Interact.PowerOn</code><br />
<code>VirtualMachine.Provisioning.DeployTemplate</code></p></td>
</tr>
</tbody>
</table>

</div>

<div id="installation-vsphere-minimum-permissions-storage_ipi-vsphere-installation-reqs" class="example">

<div class="title">

Minimum permissions for the storage components

</div>

<table>
<colgroup>
<col style="width: 36%" />
<col style="width: 36%" />
<col style="width: 27%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">vSphere object for role</th>
<th style="text-align: left;">When required</th>
<th style="text-align: left;">Required privileges</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>vSphere vCenter</p></td>
<td style="text-align: left;"><p>Always</p></td>
<td style="text-align: left;"><p><code>Cns.Searchable</code><br />
<code>InventoryService.Tagging.CreateCategory</code><br />
<code>InventoryService.Tagging.CreateTag</code><br />
<code>InventoryService.Tagging.EditCategory</code><br />
<code>InventoryService.Tagging.EditTag</code><br />
<code>StorageProfile.Update</code><br />
<code>StorageProfile.View</code></p></td>
</tr>
<tr>
<td style="text-align: left;"><p>vSphere vCenter Cluster</p></td>
<td style="text-align: left;"><p>If you intend to create VMs in the cluster root</p></td>
<td style="text-align: left;"><p><code>Host.Config.Storage</code></p></td>
</tr>
<tr>
<td style="text-align: left;"><p>vSphere vCenter Resource Pool</p></td>
<td style="text-align: left;"><p>If you included an existing resource pool in the <code>install-config.yaml</code> file</p></td>
<td style="text-align: left;"><p><code>Host.Config.Storage</code></p></td>
</tr>
<tr>
<td style="text-align: left;"><p>vSphere Datastore</p></td>
<td style="text-align: left;"><p>Always</p></td>
<td style="text-align: left;"><p><code>Datastore.Browse</code><br />
<code>Datastore.FileManagement</code><br />
<code>InventoryService.Tagging.ObjectAttachable</code></p></td>
</tr>
<tr>
<td style="text-align: left;"><p>vSphere Port Group</p></td>
<td style="text-align: left;"><p>Always</p></td>
<td style="text-align: left;"><p><code>Read Only</code></p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Virtual Machine Folder</p></td>
<td style="text-align: left;"><p>Always</p></td>
<td style="text-align: left;"><p><code>VirtualMachine.Config.AddExistingDisk</code><br />
<code>VirtualMachine.Config.AddRemoveDevice</code></p></td>
</tr>
<tr>
<td style="text-align: left;"><p>vSphere vCenter data center</p></td>
<td style="text-align: left;"><p>If the virtual machine folder does not already exist, the installation program creates the virtual machine folder.</p></td>
<td style="text-align: left;"><p><code>VirtualMachine.Config.AddExistingDisk</code><br />
<code>VirtualMachine.Config.AddRemoveDevice</code></p></td>
</tr>
</tbody>
</table>

</div>

<div id="post-installation-vsphere-minimum-machine-api_ipi-vsphere-installation-reqs" class="example">

<div class="title">

Minimum permissions for the Machine API

</div>

<table>
<colgroup>
<col style="width: 36%" />
<col style="width: 36%" />
<col style="width: 27%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">vSphere object for role</th>
<th style="text-align: left;">When required</th>
<th style="text-align: left;">Required privileges</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>vSphere vCenter</p></td>
<td style="text-align: left;"><p>Always</p></td>
<td style="text-align: left;"><p><code>InventoryService.Tagging.AttachTag</code><br />
<code>InventoryService.Tagging.CreateCategory</code><br />
<code>InventoryService.Tagging.CreateTag</code><br />
<code>InventoryService.Tagging.DeleteCategory</code><br />
<code>InventoryService.Tagging.DeleteTag</code><br />
<code>InventoryService.Tagging.EditCategory</code><br />
<code>InventoryService.Tagging.EditTag</code><br />
<code>Sessions.ValidateSession</code><br />
<code>StorageProfile.Update</code><br />
<code>StorageProfile.View</code></p></td>
</tr>
<tr>
<td style="text-align: left;"><p>vSphere vCenter Cluster</p></td>
<td style="text-align: left;"><p>If you intend to create VMs in the cluster root</p></td>
<td style="text-align: left;"><p><code>Resource.AssignVMToPool</code></p></td>
</tr>
<tr>
<td style="text-align: left;"><p>vSphere vCenter Resource Pool</p></td>
<td style="text-align: left;"><p>If you included an existing resource pool in the <code>install-config.yaml</code> file</p></td>
<td style="text-align: left;"><p><code>Read Only</code></p></td>
</tr>
<tr>
<td style="text-align: left;"><p>vSphere Datastore</p></td>
<td style="text-align: left;"><p>Always</p></td>
<td style="text-align: left;"><p><code>Datastore.AllocateSpace</code><br />
<code>Datastore.Browse</code></p></td>
</tr>
<tr>
<td style="text-align: left;"><p>vSphere Port Group</p></td>
<td style="text-align: left;"><p>Always</p></td>
<td style="text-align: left;"><p><code>Network.Assign</code></p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Virtual Machine Folder</p></td>
<td style="text-align: left;"><p>Always</p></td>
<td style="text-align: left;"><p><code>VirtualMachine.Config.AddRemoveDevice</code><br />
<code>VirtualMachine.Config.AdvancedConfig</code><br />
<code>VirtualMachine.Config.Annotation</code><br />
<code>VirtualMachine.Config.CPUCount</code><br />
<code>VirtualMachine.Config.DiskExtend</code><br />
<code>VirtualMachine.Config.Memory</code><br />
<code>VirtualMachine.Config.Settings</code><br />
<code>VirtualMachine.Interact.PowerOff</code><br />
<code>VirtualMachine.Interact.PowerOn</code><br />
<code>VirtualMachine.Inventory.CreateFromExisting</code><br />
<code>VirtualMachine.Inventory.Delete</code><br />
<code>VirtualMachine.Provisioning.Clone</code><br />
<code>VirtualMachine.Provisioning.DeployTemplate</code></p></td>
</tr>
<tr>
<td style="text-align: left;"><p>vSphere vCenter data center</p></td>
<td style="text-align: left;"><p>If the virtual machine folder does not already exist, the installation program creates the virtual machine folder.</p></td>
<td style="text-align: left;"><p><code>Resource.AssignVMToPool</code><br />
<code>VirtualMachine.Interact.PowerOff</code><br />
<code>VirtualMachine.Interact.PowerOn</code><br />
<code>VirtualMachine.Provisioning.DeployTemplate</code></p></td>
</tr>
</tbody>
</table>

</div>

## Using OpenShift Container Platform with vMotion

If you intend on using vMotion in your vSphere environment, consider the following before installing an OpenShift Container Platform cluster.

- Using Storage vMotion can cause issues and is not supported.

- Using VMware compute vMotion to migrate the workloads for both OpenShift Container Platform compute machines and control plane machines is generally supported, where *generally* implies that you meet all VMware best practices for vMotion.

  To help ensure the uptime of your compute and control plane nodes, ensure that you follow the VMware best practices for vMotion, and use VMware anti-affinity rules to improve the availability of OpenShift Container Platform during maintenance or hardware issues.

  For more information about vMotion and anti-affinity rules, see the VMware vSphere documentation for [vMotion networking requirements](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.vcenterhost.doc/GUID-3B41119A-1276-404B-8BFB-A32409052449.html) and [VM anti-affinity rules](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.resmgmt.doc/GUID-FBE46165-065C-48C2-B775-7ADA87FF9A20.html).

- If you are using VMware vSphere volumes in your pods, migrating a VM across datastores, either manually or through Storage vMotion, causes invalid references within OpenShift Container Platform persistent volume (PV) objects that can result in data loss.

- OpenShift Container Platform does not support selective migration of virtual machine disks (VMDKs) across datastores, using datastore clusters for VM provisioning or for dynamic or static provisioning of PVs, or using a datastore that is part of a datastore cluster for dynamic or static provisioning of PVs.

  > [!IMPORTANT]
  > You can specify the path of any datastore that exists in a datastore cluster. By default, Storage Distributed Resource Scheduler (SDRS), which uses Storage vMotion, is automatically enabled for a datastore cluster. Red Hat does not support Storage vMotion, so you must disable SDRS to avoid data loss issues for your OpenShift Container Platform cluster. If you must specify VMs across many datastores, use a `datastore` object to specify a failure domain in your cluster’s `install-config.yaml` configuration file. For more information, see "VMware vSphere region and zone enablement".

## Cluster resources

When you deploy an OpenShift Container Platform cluster that uses installer-provisioned infrastructure, the installation program must be able to create several resources in your vCenter instance.

A standard OpenShift Container Platform installation creates the following vCenter resources:

- 1 Folder

- 1 Tag category

- 1 Tag

- Virtual machines:

  - 1 template

  - 1 temporary bootstrap node

  - 3 control plane nodes

  - 3 compute machines

Although these resources use 856 GB of storage, the bootstrap node gets deleted during the cluster installation process. At a minimum, a standard cluster requires 800 GB of storage.

If you deploy more compute machines, the OpenShift Container Platform cluster will use more storage.

## Cluster limits

Available resources vary between clusters. A limit exists for the number of possible clusters within vCenter, primarily by available storage space and any limitations on the number of required resources. Be sure to consider both limitations to the vCenter resources that the cluster creates and the resources that you require to deploy a cluster, such as IP addresses and networks.

## Networking requirements

You can use Dynamic Host Configuration Protocol (DHCP) for the network and configure the DHCP server to set persistent IP addresses to machines in your cluster. In the DHCP lease, you must configure the DHCP to use the default gateway.

> [!NOTE]
> You do not need to use the DHCP for the network if you want to provision nodes with static IP addresses.

If you are installing to a restricted environment, the VM in your restricted network must have access to vCenter so that it can provision and manage nodes, persistent volume claims (PVCs), and other resources.

> [!NOTE]
> Ensure that each OpenShift Container Platform node in the cluster has access to a Network Time Protocol (NTP) server that is discoverable by DHCP. Installation is possible without an NTP server. However, asynchronous server clocks can cause errors, which the NTP server prevents.

Additionally, you must create the following networking resources before you install the OpenShift Container Platform cluster:

### Required IP addresses

For a network that uses DHCP, an installer-provisioned vSphere installation requires two static IP addresses:

- The **API** address for accessing the cluster API.

- The **Ingress** address for cluster ingress traffic.

You must give these IP addresses to the installation program when you install the OpenShift Container Platform cluster.

### DNS records

You must create DNS records for two static IP addresses in the appropriate DNS server for the vCenter instance that hosts your OpenShift Container Platform cluster. In each record, `<cluster_name>` is the cluster name and `<base_domain>` is the cluster base domain that you specify when you install the cluster. A complete DNS record takes the form: `<component>.<cluster_name>.<base_domain>.`.

| Component | Record | Description |
|----|----|----|
| API VIP | `api.<cluster_name>.<base_domain>.` | This DNS A/AAAA or CNAME (Canonical Name) record must point to the load balancer for the control plane machines. This record must be resolvable by both clients external to the cluster and from all the nodes within the cluster. |
| Ingress VIP | `*.apps.<cluster_name>.<base_domain>.` | A wildcard DNS A/AAAA or CNAME record that points to the load balancer that targets the machines that run the Ingress router pods, which are the worker nodes by default. This record must be resolvable by both clients external to the cluster and from all the nodes within the cluster. |

Required DNS records

### Static IP addresses for vSphere nodes

You can provision bootstrap, control plane, and compute nodes to be configured with static IP addresses in environments where Dynamic Host Configuration Protocol (DHCP) does not exist. To configure this environment, you must provide values to the `platform.vsphere.hosts.role` parameter in the `install-config.yaml` file.

By default, the installation program is configured to use the DHCP for the network, but this network has limited configurable capabilities.

After you define one or more machine pools in your `install-config.yaml` file, you can define network definitions for nodes on your network. Ensure that the number of network definitions matches the number of machine pools that you configured for your cluster.

<div class="formalpara">

<div class="title">

Example network configuration that specifies different roles

</div>

``` yaml
# ...
platform:
  vsphere:
    hosts:
    - role: bootstrap
      networkDevice:
        ipAddrs:
        - 192.168.204.10/24
        gateway: 192.168.204.1
        nameservers:
        - 192.168.204.1
    - role: control-plane
      networkDevice:
        ipAddrs:
        - 192.168.204.11/24
        gateway: 192.168.204.1
        nameservers:
        - 192.168.204.1
    - role: control-plane
      networkDevice:
        ipAddrs:
        - 192.168.204.12/24
        gateway: 192.168.204.1
        nameservers:
        - 192.168.204.1
    - role: control-plane
      networkDevice:
        ipAddrs:
        - 192.168.204.13/24
        gateway: 192.168.204.1
        nameservers:
        - 192.168.204.1
    - role: compute
      networkDevice:
        ipAddrs:
        - 192.168.204.14/24
        gateway: 192.168.204.1
        nameservers:
        - 192.168.204.1
# ...
```

</div>

- Valid network definition values include `bootstrap`, `control-plane`, and `compute`. You must list at least one `bootstrap` network definition in your `install-config.yaml` configuration file.

- Lists IPv4, IPv6, or both IP addresses that the installation program passes to the network interface. The machine API controller assigns all configured IP addresses to the default network interface.

- The default gateway for the network interface.

- Lists up to 3 DNS nameservers.

After you deployed your cluster to run nodes with static IP addresses, you can scale a machine to use one of these static IP addresses. Additionally, you can use a machine set to configure a machine to use one of the configured static IP addresses.

<div>

<div class="title">

Additional resources

</div>

- [Scaling machines to use static IP addresses](../../../post_installation_configuration/node-tasks.html#nodes-vsphere-scaling-machines-static-ip_post-install-node-tasks)

- [Using a machine set to scale machines with configured static IP addresses](../../../post_installation_configuration/node-tasks.html#nodes-vsphere-machine-set-scaling-static-ip_post-install-node-tasks)

</div>
