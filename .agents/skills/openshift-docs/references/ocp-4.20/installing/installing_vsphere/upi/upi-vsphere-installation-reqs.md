<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Before you begin an installation on infrastructure that you provision, be sure that your vSphere environment meets the following installation requirements.

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

- [Minimum permissions for the storage components](upi-vsphere-installation-reqs.md#installation-vsphere-minimum-permissions-storage_upi-vsphere-installation-reqs)

</div>

# Requirements for a cluster with user-provisioned infrastructure

For a cluster that contains user-provisioned infrastructure, you must deploy all of the required machines.

This section describes the requirements for deploying OpenShift Container Platform on user-provisioned infrastructure.

## vCenter requirements

Before you install an OpenShift Container Platform cluster on your vCenter that uses infrastructure that you provided, you must prepare your environment.

### Required vCenter account privileges

To install an OpenShift Container Platform cluster in a vCenter, your vSphere account must include privileges for reading and creating the required resources. Using an account that has global administrative privileges is the simplest way to access all of the necessary permissions.

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
<td style="text-align: left;"><p><code>VirtualMachine.Inventory.Create</code> and <code>VirtualMachine.Inventory.Delete</code> privileges are optional if your cluster does not use the Machine API. See the "Minimum permissions for the Machine API" table.</p></td>
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
<td style="text-align: left;"><p><code>VirtualMachine.Inventory.Create</code> and <code>VirtualMachine.Inventory.Delete</code> privileges are optional if your cluster does not use the Machine API.</p></td>
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
| vSphere vCenter Cluster | Always | True | Listed required privileges |
| vSphere vCenter Datastore | Always | False | Listed required privileges |
| vSphere Switch | Always | False | `ReadOnly` permission |
| vSphere Port Group | Always | False | Listed required privileges |
| vSphere vCenter Virtual Machine Folder | Existing folder | True | Listed required privileges |
| vSphere vCenter Resource Pool | Existing resource pool | True | Listed required privileges |

</div>

For more information about creating an account with only the required privileges, see [vSphere Permissions and User Management Tasks](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.security.doc/GUID-5372F580-5C23-4E9C-8A4E-EF1B4DD9033E.html) in the vSphere documentation.

### Minimum required vCenter account privileges

After you create a custom role and assign privileges to the role, you can create permissions by selecting specific vSphere objects. You can then assign the custom role to a user or group for each object.

Before you create permissions or request for the creation of permissions for a vSphere object, decide what minimum permissions apply to the vSphere object. By doing this task, you can ensure a basic interaction exists between a vSphere object and OpenShift Container Platform architecture.

> [!IMPORTANT]
> If you create a custom role and you do not assign privileges to it, the vSphere Server by default assigns a `Read Only` role to the custom role. Note that for the cloud provider API, the custom role only needs to inherit the privileges of the `Read Only` role.

Consider creating a custom role when an account with global administrative privileges does not meet your needs.

> [!IMPORTANT]
> Red Hat does not support configuring an account without including the required privileges. Red Hat tests OpenShift Container Platform cluster installations in vCenter against the full list of privileges described in the "Required vCenter account privileges" section. By adhering to the full list of privileges, you can reduce the possibility of unexpected behaviors that might occur when creating a custom role with a restricted set of privileges. You must retain the full set of privileges from the "Required vCenter account privileges" section after cluster installation. Reducing the account to only the permissions listed in the minimum permission tables in the "Minimum required vCenter account privileges" section after installation is not supported and can cause unexpected cluster behavior. The minimum permission tables are for reference only; they show which privileges apply to which OpenShift Container Platform components (such as storage or the Machine API) when you design or audit custom roles. The supported configuration is to assign the full set of privileges from the "Required vCenter account privileges" section at all times, both during and after installation.

The following tables specify how the required vCenter account privileges provided earlier in this document are relevant to different aspects of OpenShift Container Platform architecture.

<div id="post-installation-vsphere-minimum-permissions_upi-vsphere-installation-reqs" class="example">

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
<td style="text-align: left;"><p><code>VirtualMachine.Inventory.Create</code> and <code>VirtualMachine.Inventory.Delete</code> privileges are optional if your cluster does not use the Machine API. If your cluster does use the Machine API and you want to set the minimum set of permissions for the API, see the "Minimum permissions for the Machine API" table.</p></td>
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

<div id="installation-vsphere-minimum-permissions-storage_upi-vsphere-installation-reqs" class="example">

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
<td style="text-align: left;"><p><code>VirtualMachine.Inventory.Create</code> and <code>VirtualMachine.Inventory.Delete</code> privileges are optional if your cluster does not use the Machine API. If your cluster does use the Machine API and you want to set the minimum set of permissions for the API, see the "Minimum permissions for the Machine API" table.</p></td>
<td style="text-align: left;"><p><code>VirtualMachine.Config.AddExistingDisk</code><br />
<code>VirtualMachine.Config.AddRemoveDevice</code></p></td>
</tr>
</tbody>
</table>

</div>

<div id="post-installation-vsphere-minimum-machine-api_upi-vsphere-installation-reqs" class="example">

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
<td style="text-align: left;"><p><code>VirtualMachine.Inventory.Create</code> and <code>VirtualMachine.Inventory.Delete</code> privileges are optional if your cluster does not use the Machine API.</p></td>
<td style="text-align: left;"><p><code>Resource.AssignVMToPool</code><br />
<code>VirtualMachine.Interact.PowerOff</code><br />
<code>VirtualMachine.Interact.PowerOn</code><br />
<code>VirtualMachine.Provisioning.DeployTemplate</code></p></td>
</tr>
</tbody>
</table>

</div>

### Using OpenShift Container Platform with vMotion

If you intend on using vMotion in your vSphere environment, consider the following before installing an OpenShift Container Platform cluster.

- Using Storage vMotion can cause issues and is not supported.

- Using VMware compute vMotion to migrate the workloads for both OpenShift Container Platform compute machines and control plane machines is generally supported, where *generally* implies that you meet all VMware best practices for vMotion.

  To help ensure the uptime of your compute and control plane nodes, ensure that you follow the VMware best practices for vMotion, and use VMware anti-affinity rules to improve the availability of OpenShift Container Platform during maintenance or hardware issues.

  For more information about vMotion and anti-affinity rules, see the VMware vSphere documentation for [vMotion networking requirements](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.vcenterhost.doc/GUID-3B41119A-1276-404B-8BFB-A32409052449.html) and [VM anti-affinity rules](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.resmgmt.doc/GUID-FBE46165-065C-48C2-B775-7ADA87FF9A20.html).

- If you are using VMware vSphere volumes in your pods, migrating a VM across datastores, either manually or through Storage vMotion, causes invalid references within OpenShift Container Platform persistent volume (PV) objects that can result in data loss.

- OpenShift Container Platform does not support selective migration of virtual machine disks (VMDKs) across datastores, using datastore clusters for VM provisioning or for dynamic or static provisioning of PVs, or using a datastore that is part of a datastore cluster for dynamic or static provisioning of PVs.

  > [!IMPORTANT]
  > You can specify the path of any datastore that exists in a datastore cluster. By default, Storage Distributed Resource Scheduler (SDRS), which uses Storage vMotion, is automatically enabled for a datastore cluster. Red Hat does not support Storage vMotion, so you must disable SDRS to avoid data loss issues for your OpenShift Container Platform cluster. If you must specify VMs across many datastores, use a `datastore` object to specify a failure domain in your cluster’s `install-config.yaml` configuration file. For more information, see "VMware vSphere region and zone enablement".

### Cluster resources

When you deploy an OpenShift Container Platform cluster that uses infrastructure that you provided, you must create the following resources in your vCenter instance:

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

### Cluster limits

Available resources vary between clusters. A limit exists for the number of possible clusters within vCenter, primarily by available storage space and any limitations on the number of required resources. Be sure to consider both limitations to the vCenter resources that the cluster creates and the resources that you require to deploy a cluster, such as IP addresses and networks.

### Networking requirements

You can use Dynamic Host Configuration Protocol (DHCP) for the network and configure the DHCP server to set persistent IP addresses to machines in your cluster. In the DHCP lease, you must configure the DHCP to use the default gateway.

> [!NOTE]
> You do not need to use the DHCP for the network if you want to provision nodes with static IP addresses.

If you specify nodes or groups of nodes on different VLANs for a cluster that you want to install on user-provisioned infrastructure, you must ensure that machines in your cluster meet the requirements outlined in the "Network connectivity requirements" section of the *Networking requirements for user-provisioned infrastructure* document.

If you are installing to a restricted environment, the VM in your restricted network must have access to vCenter so that it can provision and manage nodes, persistent volume claims (PVCs), and other resources.

> [!NOTE]
> Ensure that each OpenShift Container Platform node in the cluster has access to a Network Time Protocol (NTP) server that is discoverable by DHCP. Installation is possible without an NTP server. However, asynchronous server clocks can cause errors, which the NTP server prevents.

Additionally, you must create the following networking resources before you install the OpenShift Container Platform cluster:

#### DNS records

You must create DNS records for two static IP addresses in the appropriate DNS server for the vCenter instance that hosts your OpenShift Container Platform cluster. In each record, `<cluster_name>` is the cluster name and `<base_domain>` is the cluster base domain that you specify when you install the cluster. A complete DNS record takes the form: `<component>.<cluster_name>.<base_domain>.`.

| Component | Record | Description |
|----|----|----|
| API VIP | `api.<cluster_name>.<base_domain>.` | This DNS A/AAAA or CNAME (Canonical Name) record must point to the load balancer for the control plane machines. This record must be resolvable by both clients external to the cluster and from all the nodes within the cluster. |
| Ingress VIP | `*.apps.<cluster_name>.<base_domain>.` | A wildcard DNS A/AAAA or CNAME record that points to the load balancer that targets the machines that run the Ingress router pods, which are the worker nodes by default. This record must be resolvable by both clients external to the cluster and from all the nodes within the cluster. |

Required DNS records

<div>

<div class="title">

Additional resources

</div>

- [Creating a compute machine set on vSphere](../../../machine_management/creating_machinesets/creating-machineset-vsphere.md#creating-machineset-vsphere_creating-machineset-vsphere)

</div>

## Required machines for cluster installation

You must specify the minimum required machines or hosts for your cluster so that your cluster remains stable if a node fails.

The smallest OpenShift Container Platform clusters require the following hosts:

> [!IMPORTANT]
> For a cluster that contains user-provisioned infrastructure, you must deploy all of the required machines.

| Hosts | Description |
|----|----|
| One temporary bootstrap machine | The cluster requires the bootstrap machine to deploy the OpenShift Container Platform cluster on the three control plane machines. You can remove the bootstrap machine after you install the cluster. |
| Three control plane machines | The control plane machines run the Kubernetes and OpenShift Container Platform services that form the control plane. |
| At least two compute machines, which are also known as worker machines. | The workloads requested by OpenShift Container Platform users run on the compute machines. |

Minimum required hosts

> [!IMPORTANT]
> To maintain high availability of your cluster, use separate physical hosts for these cluster machines.

The bootstrap and control plane machines must use Red Hat Enterprise Linux CoreOS (RHCOS) as the operating system. However, the compute machines can choose between Red Hat Enterprise Linux CoreOS (RHCOS), Red Hat Enterprise Linux (RHEL) 8.6 and later.

Note that RHCOS is based on Red Hat Enterprise Linux (RHEL) 9.2 and inherits all of its hardware certifications and requirements. See [Red Hat Enterprise Linux technology capabilities and limits](https://access.redhat.com/articles/rhel-limits).

## Minimum resource requirements for cluster installation

Each created cluster must meet minimum requirements so that the cluster runs as expected.

| Machine | Operating System | vCPU | Virtual RAM | Storage | Input/Output Per Second (IOPS)<sup>\[1\]</sup> |
|----|----|----|----|----|----|
| Bootstrap | RHCOS | 4 | 16 GB | 100 GB | 300 |
| Control plane | RHCOS | 4 | 16 GB | 100 GB | 300 |
| Compute | RHCOS | 2 | 8 GB | 100 GB | 300 |

Minimum resource requirements

1.  OpenShift Container Platform and Kubernetes are sensitive to disk performance, and faster storage is recommended, particularly for etcd on the control plane nodes which require a 10 ms p99 fsync duration. Note that on many cloud platforms, storage size and IOPS scale together, so you might need to over-allocate storage volume to obtain sufficient performance.

2.  As with all user-provisioned installations, if you choose to use RHEL compute machines in your cluster, you take responsibility for all operating system life cycle management and maintenance, including performing system updates, applying patches, and completing all other required tasks. Use of RHEL 7 compute machines is deprecated and has been removed in OpenShift Container Platform 4.10 and later.

> [!NOTE]
> For OpenShift Container Platform version 4.19, RHCOS is based on RHEL version 9.6, which updates the micro-architecture requirements. The following list contains the minimum instruction set architectures (ISA) that each architecture requires:
>
> - x86-64 architecture requires x86-64-v2 ISA
>
> - ARM64 architecture requires ARMv8.0-A ISA
>
> - IBM Power architecture requires Power 9 ISA
>
> - s390x architecture requires z14 ISA
>
> For more information, see "Architectures".

If an instance type for your platform meets the minimum requirements for cluster machines, it is supported to use in OpenShift Container Platform.

> [!IMPORTANT]
> Do not use memory ballooning in OpenShift Container Platform clusters. Memory ballooning can cause cluster-wide instabilities, service degradation, or other undefined behaviors.
>
> - Control plane machines should have committed memory equal to or greater than the published minimum resource requirements for a cluster installation.
>
> - Compute machines should have a minimum reservation equal to or greater than the published minimum resource requirements for a cluster installation.
>
> These minimum CPU and memory requirements do not account for resources required by user workloads.
>
> For more information, see "Memory Ballooning and OpenShift".

<div>

<div class="title">

Additional resources

</div>

- [Architectures (RHEL documentation)](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/9/html-single/9.2_release_notes/index#architectures)

- [Memory Ballooning and OpenShift (Red Hat Knowledgebase article)](https://access.redhat.com/articles/7074533)

</div>

<div>

<div class="title">

Additional resources

</div>

- [Optimizing storage](../../../scalability_and_performance/optimization/optimizing-storage.md#optimizing-storage)

</div>

## Requirements for encrypting virtual machines

You can encrypt your virtual machines prior to installing OpenShift Container Platform 4.17 by meeting the following requirements.

- You have configured a Standard key provider in vSphere. For more information, see [Adding a KMS to vCenter Server](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.vsan.doc/GUID-AC06B3C3-901F-402E-B25F-1EE7809D1264.html).

  > [!IMPORTANT]
  > The Native key provider in vCenter is not supported. For more information, see [vSphere Native Key Provider Overview](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.security.doc/GUID-54B9FBA2-FDB1-400B-A6AE-81BF3AC9DF97.html).

- You have enabled host encryption mode on all of the ESXi hosts that are hosting the cluster. For more information, see [Enabling host encryption mode](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.security.doc/GUID-A9E1F016-51B3-472F-B8DE-803F6BDB70BC.html).

- You have a vSphere account which has all cryptographic privileges enabled. For more information, see [Cryptographic Operations Privileges](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.security.doc/GUID-660CCB35-847F-46B3-81CA-10DDDB9D7AA9.html).

When you deploy the OVF template in the section titled "Installing RHCOS and starting the OpenShift Container Platform bootstrap process", select the option to "Encrypt this virtual machine" when you are selecting storage for the OVF template. After completing cluster installation, create a storage class that uses the encryption storage policy you used to encrypt the virtual machines.

<div>

<div class="title">

Additional resources

</div>

- [Creating an encrypted storage class](../../../storage/container_storage_interface/persistent-storage-csi-vsphere.md#vsphere-pv-encryption)

</div>

## Certificate signing requests management

On user-provisioned infrastructure, you must provide a mechanism for approving cluster certificate signing requests (CSRs) after installation when your cluster has limited access to automatic machine management.

The `kube-controller-manager` only approves the kubelet client CSRs. The `machine-approver` cannot guarantee the validity of a serving certificate that is requested by using kubelet credentials because it cannot confirm that the correct machine issued the request. You must determine and implement a method of verifying the validity of the kubelet serving certificate requests and approving them.

## Networking requirements for user-provisioned infrastructure

You must configure networking for all the Red Hat Enterprise Linux CoreOS (RHCOS) machines in `initramfs` during boot, so that they can fetch their Ignition config files.

> [!IMPORTANT]
> Ensure you enable the `disk.EnableUUID` parameter on all virtual machines in your cluster.

During the initial boot, the machines require an IP address configuration that is set either through a DHCP server or statically by providing the required boot options. After a network connection is established, the machines download their Ignition config files from an HTTP or HTTPS server. The Ignition config files are then used to set the exact state of each machine. The Machine Config Operator completes more changes to the machines, such as the application of new certificates or keys, after installation.

<div class="note">

<div class="title">

</div>

- Consider using a DHCP server for long-term management of the cluster machines. Ensure that the DHCP server is configured to provide persistent IP addresses, DNS server information, and hostnames to the cluster machines.

- If a DHCP service is not available for your user-provisioned infrastructure, you can instead provide the IP networking configuration and the address of the DNS server to the nodes at RHCOS install time. These can be passed as boot arguments if you are installing from an ISO image. See the *Installing RHCOS and starting the OpenShift Container Platform bootstrap process* section for more information about static IP provisioning and advanced networking options.

</div>

The Kubernetes API server must be able to resolve the node names of the cluster machines. If the API servers and worker nodes are in different zones, you can configure a default DNS search zone to allow the API server to resolve the node names. Another supported approach is to always refer to hosts by their fully-qualified domain names in both the node objects and all DNS requests.

### Setting the cluster node hostnames through DHCP

On Red Hat Enterprise Linux CoreOS (RHCOS) machines, the hostname is set through NetworkManager. By default, the machines obtain their hostname through DHCP. If the hostname is not provided by DHCP, set statically through kernel arguments, or another method, it is obtained through a reverse DNS lookup. Reverse DNS lookup occurs after the network has been initialized on a node and can take time to resolve. Other system services can start prior to this and detect the hostname as `localhost` or similar. You can avoid this by using DHCP to provide the hostname for each cluster node.

Additionally, setting the hostnames through DHCP can bypass any manual DNS record name configuration errors in environments that have a DNS split-horizon implementation.

### Network connectivity requirements

You must configure the network connectivity between machines to allow OpenShift Container Platform cluster components to communicate. Each machine must be able to resolve the hostnames of all other machines in the cluster.

This section provides details about the ports that are required.

> [!IMPORTANT]
> In connected OpenShift Container Platform environments, all nodes are required to have internet access to pull images for platform containers and provide telemetry data to Red Hat.

| Protocol | Port | Description |
|----|----|----|
| ICMP | N/A | Network reachability tests |
| TCP | `1936` | Metrics |
| `9000`-`9999` | Host level services, including the node exporter on ports `9100`-`9101` and the Cluster Version Operator on port `9099`. |  |
| `10250`-`10259` | The default ports that Kubernetes reserves |  |
| `22623` | The port handles traffic from the Machine Config Server and directs the traffic to the control plane machines. |  |
| UDP | `6081` | Geneve |
| `9000`-`9999` | Host level services, including the node exporter on ports `9100`-`9101`. |  |
| `500` | IPsec IKE packets |  |
| `4500` | IPsec NAT-T packets |  |
| `123` | Network Time Protocol (NTP) on UDP port `123`. If an external NTP time server is configured, you must open UDP port `123`. |  |
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

### NTP configuration for user-provisioned infrastructure

OpenShift Container Platform clusters are configured to use a public Network Time Protocol (NTP) server by default. If you want to use a local enterprise NTP server, or if your cluster is being deployed in a disconnected network, you can configure the cluster to use a specific time server. For more information, see the documentation for *Configuring chrony time service*.

If a DHCP server provides NTP server information, the chrony time service on the Red Hat Enterprise Linux CoreOS (RHCOS) machines read the information and can sync the clock with the NTP servers.

<div>

<div class="title">

Additional resources

</div>

- [Configuring chrony time service](../../install_config/installing-customizing.md#installation-special-config-chrony_installing-customizing)

</div>

## User-provisioned DNS requirements

In OpenShift Container Platform deployments, you must ensure that cluster components meet certain DNS name resolution criteria for internal communication, certificate validation, and automated node discovery purposes.

The following is a list of required cluster components:

- The Kubernetes API

- The OpenShift Container Platform application wildcard

- The bootstrap and control plane machines

- The compute machines

Reverse DNS resolution is also required for the Kubernetes API, the bootstrap machine, the control plane machines, and the compute machines.

DNS A/AAAA or CNAME records are used for name resolution and PTR records are used for reverse name resolution. The reverse records are important because Red Hat Enterprise Linux CoreOS (RHCOS) uses the reverse records to set the hostnames for all the nodes, unless the hostnames are provided by DHCP. Additionally, the reverse records are used to generate the certificate signing requests (CSR) that OpenShift Container Platform needs to operate.

> [!NOTE]
> It is recommended to use a DHCP server to provide the hostnames to each cluster node. See the *DHCP recommendations for user-provisioned infrastructure* section for more information.

The following DNS records are required for a user-provisioned OpenShift Container Platform cluster and they must be in place before installation. In each record, `<cluster_name>` is the cluster name and `<base_domain>` is the base domain that you specify in the `install-config.yaml` file. A complete DNS record takes the form: `<component>.<cluster_name>.<base_domain>.`.

<table>
<caption>Required DNS records</caption>
<colgroup>
<col style="width: 11%" />
<col style="width: 33%" />
<col style="width: 55%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Component</th>
<th style="text-align: left;">Record</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>Kubernetes API</p></td>
<td style="text-align: left;"><p><code>api.&lt;cluster_name&gt;.&lt;base_domain&gt;.</code></p></td>
<td style="text-align: left;"><p>A DNS A/AAAA or CNAME record, and a DNS PTR record, to identify the API load balancer. These records must be resolvable by both clients external to the cluster and from all the nodes within the cluster.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>api-int.&lt;cluster_name&gt;.&lt;base_domain&gt;.</code></p></td>
<td style="text-align: left;"><p>A DNS A/AAAA or CNAME record, and a DNS PTR record, to internally identify the API load balancer. These records must be resolvable from all the nodes within the cluster.</p>
<div class="important">
<div class="title">
&#10;</div>
<p>The API server must be able to resolve the worker nodes by the hostnames that are recorded in Kubernetes. If the API server cannot resolve the node names, then proxied API calls can fail, and you cannot retrieve logs from pods.</p>
</div></td>
<td></td>
</tr>
<tr>
<td style="text-align: left;"><p>Routes</p></td>
<td style="text-align: left;"><p><code>*.apps.&lt;cluster_name&gt;.&lt;base_domain&gt;.</code></p></td>
<td style="text-align: left;"><p>A wildcard DNS A/AAAA or CNAME record that refers to the application ingress load balancer. The application ingress load balancer targets the machines that run the Ingress Controller pods. The Ingress Controller pods run on the compute machines by default. These records must be resolvable by both clients external to the cluster and from all the nodes within the cluster.</p>
<p>For example, <code>console-openshift-console.apps.&lt;cluster_name&gt;.&lt;base_domain&gt;</code> is used as a wildcard route to the OpenShift Container Platform console.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Bootstrap machine</p></td>
<td style="text-align: left;"><p><code>bootstrap.&lt;cluster_name&gt;.&lt;base_domain&gt;.</code></p></td>
<td style="text-align: left;"><p>A DNS A/AAAA or CNAME record, and a DNS PTR record, to identify the bootstrap machine. These records must be resolvable by the nodes within the cluster.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Control plane machines</p></td>
<td style="text-align: left;"><p><code>&lt;control_plane&gt;&lt;n&gt;.&lt;cluster_name&gt;.&lt;base_domain&gt;.</code></p></td>
<td style="text-align: left;"><p>DNS A/AAAA or CNAME records and DNS PTR records to identify each machine for the control plane nodes. These records must be resolvable by the nodes within the cluster.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Compute machines</p></td>
<td style="text-align: left;"><p><code>&lt;compute&gt;&lt;n&gt;.&lt;cluster_name&gt;.&lt;base_domain&gt;.</code></p></td>
<td style="text-align: left;"><p>DNS A/AAAA or CNAME records and DNS PTR records to identify each machine for the worker nodes. These records must be resolvable by the nodes within the cluster.</p></td>
</tr>
</tbody>
</table>

> [!NOTE]
> In OpenShift Container Platform 4.4 and later, you do not need to specify etcd host and SRV records in your DNS configuration.

> [!TIP]
> You can use the `dig` command to verify name and reverse name resolution. See the section on *Validating DNS resolution for user-provisioned infrastructure* for detailed validation steps.

### Example DNS configuration for user-provisioned clusters

Reference the example DNS configurations to understand how A and PTR record configuration samples meet the DNS requirements for deploying OpenShift Container Platform on user-provisioned infrastructure.

The DNS configuration examples provided here are for reference only and are not meant to provide advice for choosing one DNS solution over another.

In the examples, the cluster name is `ocp4` and the base domain is `example.com`.

The following example is a BIND zone file that shows sample DNS A records for name resolution in a user-provisioned cluster.

> [!NOTE]
> In the example, the same load balancer is used for the Kubernetes API and application ingress traffic. In production scenarios, you can deploy the API and application ingress load balancers separately so that you can scale the load balancer infrastructure for each in isolation.

``` text
$TTL 1W
@   IN  SOA ns1.example.com.    root (
            2019070700  ; serial
            3H      ; refresh (3 hours)
            30M     ; retry (30 minutes)
            2W      ; expiry (2 weeks)
            1W )        ; minimum (1 week)
    IN  NS  ns1.example.com.
    IN  MX 10   smtp.example.com.
;
;
ns1.example.com.        IN  A   192.168.1.5
smtp.example.com.       IN  A   192.168.1.5
;
helper.example.com.     IN  A   192.168.1.5
helper.ocp4.example.com.    IN  A   192.168.1.5
;
api.ocp4.example.com.       IN  A   192.168.1.5
api-int.ocp4.example.com.   IN  A   192.168.1.5
;
*.apps.ocp4.example.com.    IN  A   192.168.1.5
;
bootstrap.ocp4.example.com. IN  A   192.168.1.96
;
control-plane0.ocp4.example.com.    IN  A   192.168.1.97
control-plane1.ocp4.example.com.    IN  A   192.168.1.98
;
control-plane2.ocp4.example.com.    IN  A   192.168.1.99
;
compute0.ocp4.example.com.  IN  A   192.168.1.11
compute1.ocp4.example.com.  IN  A   192.168.1.7
;
;EOF
```

where:

`api.ocp4.example.com.`
Provides name resolution for the Kubernetes API. The record refers to the IP address of the API load balancer.

`api-int.ocp4.example.com.`
Provides name resolution for the Kubernetes API. The record refers to the IP address of the API load balancer and is used for internal cluster communications.

`*.apps.ocp4.example.com.`
Provides name resolution for the wildcard routes. The record refers to the IP address of the application ingress load balancer. The application ingress load balancer targets the machines that run the Ingress Controller pods.

`bootstrap.ocp4.example.com`
Provides name resolution for the bootstrap machine.

`control-plane0.ocp4.example.com`
Provides name resolution for the control plane machines.

`compute0.ocp4.example.com.`
Provides name resolution for the compute machines.

The following example BIND zone file shows sample PTR records for reverse name resolution in a user-provisioned cluster:

``` text
$TTL 1W
@   IN  SOA ns1.example.com.    root (
            2019070700  ; serial
            3H      ; refresh (3 hours)
            30M     ; retry (30 minutes)
            2W      ; expiry (2 weeks)
            1W )        ; minimum (1 week)
    IN  NS  ns1.example.com.
;
5.1.168.192.in-addr.arpa.   IN  PTR api.ocp4.example.com.
5.1.168.192.in-addr.arpa.   IN  PTR api-int.ocp4.example.com.
;
96.1.168.192.in-addr.arpa.  IN  PTR bootstrap.ocp4.example.com.
;
97.1.168.192.in-addr.arpa.  IN  PTR control-plane0.ocp4.example.com.
98.1.168.192.in-addr.arpa.  IN  PTR control-plane1.ocp4.example.com.
;
99.1.168.192.in-addr.arpa.  IN  PTR control-plane2.ocp4.example.com.
;
11.1.168.192.in-addr.arpa.  IN  PTR compute0.ocp4.example.com.
7.1.168.192.in-addr.arpa.   IN  PTR compute1.ocp4.example.com.
;
;EOF
```

where:

`api.ocp4.example.com.`
Provides reverse DNS resolution for the Kubernetes API. The PTR record refers to the record name of the API load balancer.

`api-int.ocp4.example.com.`
Provides reverse DNS resolution for the Kubernetes API. The PTR record refers to the record name of the API load balancer and is used for internal cluster communications.

`bootstrap.ocp4.example.com.`
Provides reverse DNS resolution for the bootstrap machine.

`control-plane0.ocp4.example.com.`
Provides rebootstrap.ocp4.example.com.verse DNS resolution for the control plane machines.

`compute0.ocp4.example.com.`
Provides reverse DNS resolution for the compute machines.

> [!NOTE]
> A PTR record is not required for the OpenShift Container Platform application wildcard.

## Load balancing requirements for user-provisioned infrastructure

Before you install OpenShift Container Platform, you must provision the API and application Ingress load balancing infrastructure. In production scenarios, you can deploy the API and application Ingress load balancers separately so that you can scale the load balancer infrastructure for each in isolation.

> [!NOTE]
> If you want to deploy the API and application Ingress load balancers with a Red Hat Enterprise Linux (RHEL) instance, you must purchase the RHEL subscription separately.

The load balancing infrastructure must meet the following requirements:

- API load balancer: Provides a common endpoint for users, both human and machine, to interact with and configure the platform. Configure the following conditions:

  - Layer 4 load balancing only. This can be referred to as Raw TCP or SSL Passthrough mode.

  - A stateless load balancing algorithm. The options vary based on the load balancer implementation.

> [!IMPORTANT]
> Do not configure session persistence for an API load balancer. Configuring session persistence for a Kubernetes API server might cause performance issues from excess application traffic for your OpenShift Container Platform cluster and the Kubernetes API that runs inside the cluster.

Configure the following ports on both the front and back of the API load balancers:

| Port | Back-end machines (pool members) | Internal | External | Description |
|----|----|----|----|----|
| `6443` | Bootstrap and control plane. You remove the bootstrap machine from the load balancer after the bootstrap machine initializes the cluster control plane. You must configure the `/readyz` endpoint for the API server health check probe. | X | X | Kubernetes API server |
| `22623` | Bootstrap and control plane. You remove the bootstrap machine from the load balancer after the bootstrap machine initializes the cluster control plane. | X |  | Machine config server |

> [!NOTE]
> The load balancer must be configured to take a maximum of 30 seconds from the time the API server turns off the `/readyz` endpoint to the removal of the API server instance from the pool. Within the time frame after `/readyz` returns an error or becomes healthy, the endpoint must have been removed or added. Probing every 5 or 10 seconds, with two successful requests to become healthy and three to become unhealthy, are well-tested values.

- Application Ingress load balancer: Provides an ingress point for application traffic flowing in from outside the cluster. A working configuration for the Ingress router is required for an OpenShift Container Platform cluster. Configure the following conditions:

  - Layer 4 load balancing only. This can be referred to as Raw TCP or SSL Passthrough mode.

  - A connection-based or session-based persistence is recommended, based on the options available and types of applications that will be hosted on the platform.

> [!TIP]
> If the true IP address of the client can be seen by the application Ingress load balancer, enabling source IP-based session persistence can improve performance for applications that use end-to-end TLS encryption.

Configure the following ports on both the front and back of the load balancers:

| Port | Back-end machines (pool members) | Internal | External | Description |
|----|----|----|----|----|
| `443` | The machines that run the Ingress Controller pods, compute, or worker, by default. | X | X | HTTPS traffic |
| `80` | The machines that run the Ingress Controller pods, compute, or worker, by default. | X | X | HTTP traffic |

Application Ingress load balancer

> [!NOTE]
> If you are deploying a three-node cluster with zero compute nodes, the Ingress Controller pods run on the control plane nodes. In three-node cluster deployments, you must configure your application Ingress load balancer to route HTTP and HTTPS traffic to the control plane nodes.

### Example load balancer configuration for user-provisioned clusters

Reference the example API and application Ingress load balancer configuration so that you can understand how to meet the load balancing requirements for user-provisioned clusters.

The sample is an `/etc/haproxy/haproxy.cfg` configuration for an HAProxy load balancer. The example is not meant to provide advice for choosing one load balancing solution over another.

> [!TIP]
> If you are using HAProxy as a load balancer, you can check that the `haproxy` process is listening on ports `6443`, `22623`, `443`, and `80` by running `netstat -nltupe` on the HAProxy node.

In the example, the same load balancer is used for the Kubernetes API and application ingress traffic. In production scenarios, you can deploy the API and application ingress load balancers separately so that you can scale the load balancer infrastructure for each in isolation.

> [!NOTE]
> If you are using HAProxy as a load balancer and SELinux is set to `enforcing`, you must ensure that the HAProxy service can bind to the configured TCP port by running `setsebool -P haproxy_connect_any=1`.

<div class="formalpara">

<div class="title">

Sample API and application Ingress load balancer configuration

</div>

``` text
global
  log         127.0.0.1 local2
  pidfile     /var/run/haproxy.pid
  maxconn     4000
  daemon
defaults
  mode                    http
  log                     global
  option                  dontlognull
  option http-server-close
  option                  redispatch
  retries                 3
  timeout http-request    10s
  timeout queue           1m
  timeout connect         10s
  timeout client          1m
  timeout server          1m
  timeout http-keep-alive 10s
  timeout check           10s
  maxconn                 3000
listen api-server-6443
  bind *:6443
  mode tcp
  option  httpchk GET /readyz HTTP/1.0
  option  log-health-checks
  balance roundrobin
  server bootstrap bootstrap.ocp4.example.com:6443 verify none check check-ssl inter 10s fall 2 rise 3 backup
  server master0 master0.ocp4.example.com:6443 weight 1 verify none check check-ssl inter 10s fall 2 rise 3
  server master1 master1.ocp4.example.com:6443 weight 1 verify none check check-ssl inter 10s fall 2 rise 3
  server master2 master2.ocp4.example.com:6443 weight 1 verify none check check-ssl inter 10s fall 2 rise 3
listen machine-config-server-22623
  bind *:22623
  mode tcp
  server bootstrap bootstrap.ocp4.example.com:22623 check inter 1s backup
  server master0 master0.ocp4.example.com:22623 check inter 1s
  server master1 master1.ocp4.example.com:22623 check inter 1s
  server master2 master2.ocp4.example.com:22623 check inter 1s
listen ingress-router-443
  bind *:443
  mode tcp
  balance source
  server compute0 compute0.ocp4.example.com:443 check inter 1s
  server compute1 compute1.ocp4.example.com:443 check inter 1s
listen ingress-router-80
  bind *:80
  mode tcp
  balance source
  server compute0 compute0.ocp4.example.com:80 check inter 1s
  server compute1 compute1.ocp4.example.com:80 check inter 1s
```

</div>

where:

`listen api-server-6443`
Port `6443` handles the Kubernetes API traffic and points to the control plane machines.

`server bootstrap bootstrap.ocp4.example.com`
The bootstrap entries must be in place before the OpenShift Container Platform cluster installation and they must be removed after the bootstrap process is complete.

`listen machine-config-server`
Port `22623` handles the machine config server traffic and points to the control plane machines.

`listen ingress-router-443`
Port `443` handles the HTTPS traffic and points to the machines that run the Ingress Controller pods. The Ingress Controller pods run on the compute machines by default.

`listen ingress-router-80`
Port `80` handles the HTTP traffic and points to the machines that run the Ingress Controller pods. The Ingress Controller pods run on the compute machines by default.

> [!NOTE]
> If you are deploying a three-node cluster with zero compute nodes, the Ingress Controller pods run on the control plane nodes. In three-node cluster deployments, you must configure your application Ingress load balancer to route HTTP and HTTPS traffic to the control plane nodes.
