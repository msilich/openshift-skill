<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

You can create virtual machines (VMs) by using the OpenShift Container Platform web console. The web console creation wizard provides workflows for configuring a custom VM, creating a VM from a template, and cloning an existing VM.

# VM creation methods

The web console creation wizard provides three workflows for creating a virtual machine (VM). Choose the workflow that matches your situation.

| If you want to | Use this workflow | Requirements |
|----|----|----|
| Build a VM with a specific combination of compute, storage, and network settings, when no existing template matches your requirements | **Custom configuration** | A boot source, such as a custom disk image, container image, or URL |
| Deploy a standardized VM quickly from a preconfigured image and settings | **Create from Template** | A template that has an available boot source in the cluster |
| Create one or more VMs that duplicate an existing VM and its configuration | **Clone existing VirtualMachine** | Access to the source VM that you want to clone |

VM creation methods

For any method, the creation wizard reference explains how boot source, instance type, and customization options affect the VM.

<div>

<div class="title">

Additional resources

</div>

- [Virtual machine creation wizard reference](virt-creating-vms-web.md#virt-vm-creation-considerations-web_virt-creating-vms-web)

</div>

# Create a VM with custom configuration by using the web console

You can use the **Custom configuration** workflow in the web console to create a virtual machine (VM) by selecting a guest operating system, boot source, compute resources, and advanced settings.

Use this workflow when:

- No existing template matches your requirements.

- You need a specific combination of compute, storage, and network settings.

- You want to boot from a custom disk image.

<div>

<div class="title">

Prerequisites

</div>

- You have access to the OpenShift Container Platform web console.

- You have `edit` or `admin` permissions in the target project.

</div>

<div>

<div class="title">

Procedure

</div>

1.  In the OpenShift Container Platform web console, navigate to **Virtualization** → **VirtualMachines**.

2.  Click **Create**.

3.  On the **Deployment details** page, configure the following settings:

    1.  Select **Custom configuration**.

    2.  In the **Name** field, enter a name for the VM. You can also click the refresh icon to generate a name automatically.

    3.  Optional: Enter a **Description** for the VM.

    4.  Review the **Location** to verify the target cluster and project. If the folder preview feature is enabled, you can also verify the folder. To change the location, click the edit icon.

    5.  Click **Next**.

4.  On the **Guest operating system** page, specify the operating system:

    1.  Select the guest operating system, such as **RHEL**, **Microsoft Windows**, or **Other Linux**.

    2.  Select the operating system version from the **Guest operating system type** list.

    3.  Click **Next**.

5.  On the **Boot source** page, specify the boot volume:

    1.  Select **Boot volume** to use an existing boot volume or add a new one, or select **No boot source** to assign an empty disk that you can configure later.

    2.  If you selected **Boot volume**, select an existing volume from the list, or click **Add volume** to configure a new boot volume.

    3.  Click **Next**.

6.  On the **Compute resources** page, define the instance type:

    1.  Select an instance type series, such as **General purpose** or **Compute Exclusive**.

    2.  Select the vCPU and memory size from the drop-down list.

    3.  Click **Next**.

7.  Optional: On the **Customization** page, configure advanced settings by navigating the following tabs:

    - **Details**: Configure the **Hostname**, **Headless mode**, **Guest system log access**, and **Deletion protection**.

    - **Storage**: Add or change storage disks.

    - **Network**: Add network interfaces.

    - **Scheduling**: Configure scheduling requirements and the run strategy.

    - **SSH**: Configure SSH key settings.

    - **Initial run**: Define **Cloud-init** or **Sysprep** initialization scripts.

    - **Labels and annotations**: Add labels to help organize and categorize VMs, and use annotations to store extra metadata.

      1.  Click **Next**.

8.  On the **Review and create** page, review the VM configuration:

    1.  Optional: Select the **Start this VirtualMachine after creation** checkbox.

    2.  Click **Create VirtualMachine**.

</div>

<div>

<div class="title">

Verification

</div>

- Navigate to **Virtualization** → **VirtualMachines** and verify that the VM is displayed in the list.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Organize virtual machines by using the web console](../managing_vms/virt-list-vms.md#virt-organize-vms-web_virt-list-vms)

</div>

# Create a VM from a template by using the web console

You can use the **Create from Template** workflow in the web console to create a virtual machine (VM) by selecting a preconfigured template that provides standardized images and settings.

Use this workflow when:

- A template matches your workload requirements and operating system.

- You want to use a preconfigured VM with standardized settings.

- You want to quickly deploy a VM with minimal customization.

<div>

<div class="title">

Prerequisites

</div>

- You have access to the OpenShift Container Platform web console.

- You have `edit` or `admin` permissions in the target project.

- A template with an available boot source exists in the cluster.

</div>

<div>

<div class="title">

Procedure

</div>

1.  In the OpenShift Container Platform web console, navigate to **Virtualization** → **VirtualMachines**.

2.  Click **Create**.

3.  On the **Deployment details** page, configure the following settings:

    1.  Select **Create from Template**.

    2.  In the **Name** field, enter a name for the VM. You can also click the refresh icon to generate a name automatically.

    3.  Optional: Enter a **Description** for the VM.

    4.  Review the **Location** to verify the target cluster and project. If the folder preview feature is enabled, you can also verify the folder. To change the location, click the edit icon.

    5.  Click **Next**.

4.  On the **Template** page, select a template:

    1.  Optional: Filter the template list. You can select a project from the **All projects** menu, apply a **Filter** for categories such as operating system or workload type, or enter a keyword in the **Filter by keyword** field.

    2.  Click a template tile to select it and view its details.

    3.  Click **Next**.

5.  Optional: On the **Customization** page, configure advanced settings by navigating the following tabs:

    - **Details**: Configure the **Hostname**, **Headless mode**, **Guest system log access**, and **Deletion protection**.

    - **Storage**: Add or change storage disks.

    - **Network**: Add network interfaces.

    - **Scheduling**: Configure scheduling requirements and the run strategy.

    - **SSH**: Configure SSH key settings.

    - **Initial run**: Define **Cloud-init** or **Sysprep** initialization scripts.

    - **Labels and annotations**: Add labels to help organize and categorize VMs, and use annotations to store extra metadata.

      1.  Click **Next**.

6.  On the **Review and create** page, review the VM configuration:

    1.  Optional: Select the **Start this VirtualMachine after creation** checkbox.

    2.  Click **Create VirtualMachine**.

</div>

<div>

<div class="title">

Verification

</div>

- Navigate to **Virtualization** → **VirtualMachines** and verify that the VM is displayed in the list.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Organize virtual machines by using the web console](../managing_vms/virt-list-vms.md#virt-organize-vms-web_virt-list-vms)

</div>

# Clone an existing VM by using the web console

You can use the **Clone existing VirtualMachine** workflow in the web console to create a new virtual machine (VM) by cloning an existing VM and its configuration.

Use this workflow when:

- You want to duplicate an existing VM with the same configuration.

- You need multiple VMs with a consistent setup.

<div>

<div class="title">

Prerequisites

</div>

- You have access to the OpenShift Container Platform web console.

- You have `edit` or `admin` permissions in the target project.

- The source VM that you want to clone exists in a project that you can access.

</div>

<div>

<div class="title">

Procedure

</div>

1.  In the OpenShift Container Platform web console, navigate to **Virtualization** → **VirtualMachines**.

2.  Click **Create**.

3.  On the **Deployment details** page, configure the following settings:

    1.  Select **Clone existing VirtualMachine**.

    2.  Review the **Project** and **Group** under **Location**. To change the target project or group, click the edit icon.

    3.  Click **Next**.

4.  On the **Source** page, select the VM to clone:

    1.  Browse the list of available VMs, or use the search and filter options to locate a specific VM.

        You can filter by **Status**, **Operating system**, **Storage class**, **Hardware devices**, **Scheduling**, **Node**, **Guest agent**, and **Architecture type**.

    2.  Select the VM that you want to clone.

    3.  Click **Next**.

5.  On the **Review and create** page, review the VM configuration:

    1.  Optional: In the **Name** field, enter a name for the VM. You can also click the refresh icon to generate a name automatically.

    2.  Optional: Enter a **Description** for the VM.

    3.  Review the **Location** to verify the target cluster and project. If the folder preview feature is enabled, you can also verify the folder. To change the location, click the edit icon.

    4.  Optional: The **Start this VirtualMachine after creation** checkbox is selected by default. Clear the checkbox if you do not want the cloned VM to start immediately.

    5.  Click **Clone VirtualMachine**.

</div>

<div>

<div class="title">

Verification

</div>

- Navigate to **Virtualization** → **VirtualMachines** and verify that the VM is displayed in the list.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Organize virtual machines by using the web console](../managing_vms/virt-list-vms.md#virt-organize-vms-web_virt-list-vms)

</div>

# Virtual machine creation wizard reference

The virtual machine (VM) creation wizard in the web console presents several options that affect how a VM runs. The following tables describe the options that have the greatest impact.

## Boot source options

On the **Boot source** page, you can select an existing boot volume or click **Add volume** to create one. When you add a volume, the **Source type** list determines where the boot disk image comes from.

| Source type | Description | When to use |
|----|----|----|
| Volume (upload new) | Uploads a persistent volume claim (PVC) image or ISO file from your local machine. | You have a disk image or ISO on your workstation. Select **This is an ISO file** for installation media. |
| Volume (use existing) | Reuses a volume that is already available on the cluster. | A boot volume is already prepared in the cluster. |
| Volume snapshot | Creates a boot disk from an existing volume snapshot. | You want fast provisioning from a point-in-time image. |
| Registry | Imports a container disk from a container registry. | The image is published to a registry such as Quay. Requires a container image URL and, for private registries, credentials. |
| URL | Imports an image from an HTTP or HTTPS endpoint. | The image is hosted at a web address. Select **TLS certificate required** for endpoints that need a certificate. |

Boot source types

When you add a volume, the following settings affect how the disk is stored and identified:

**Preference**
The preferred VM attribute values required to run a given workload, such as the guest operating system. The preference influences default values elsewhere in the wizard.

**Default InstanceType**
The default instance type associated with the boot volume.

**StorageClass**
The storage class used to provision the volume. The default storage class is used unless you select another.

**Volume Mode**
Determines whether the volume is presented as a raw block device (**Block**) or a formatted file system (**Filesystem**).

**Access Mode**
Controls how many nodes can mount the volume: shared access (**RWX**), single-user (**RWO**), or read-only (**ROX**). Live migration requires shared access (**RWX**).

## Instance type series

On the **Compute resources** page, you select an instance type series and then a size. The series determines the CPU and memory characteristics of the VM. Some series require specially configured nodes.

| Series | Name | Characteristics | Node requirement |
|----|----|----|----|
| U | General Purpose | Neutral, general-purpose resources. VMs share physical CPU cores with other VMs on a time-slice basis. | None |
| O | Overcommitted | Based on the U series, but memory is overcommitted. | None |
| CX | Compute Exclusive | Exclusive compute resources for compute-intensive workloads, with dedicated CPUs, isolated emulator threads, and virtual non-uniform memory access (NUMA) topology. | CPU manager enabled and huge pages available on the nodes. |
| M | Memory Intensive | Resources for memory-intensive workloads, with burstable CPU performance. | None |
| D | Dedicated vCPU | Consistent, predictable performance. VMs are assigned exclusive physical CPU cores, which avoids CPU sharing and time-slice contention. | None |
| N | Network | Resources for network-intensive Data Plane Development Kit (DPDK) workloads, such as virtual network functions (VNFs). | Nodes capable of running DPDK workloads and labeled with `node-role.kubevirt.io/worker-dpdk`. |
| RT | Realtime | Resources for realtime workloads, such as `oslat`. | Nodes capable of running realtime workloads. |

Instance type series

Instance types are named in the format `series.size`, where the size ranges from `nano` to `8xlarge`. For example, `u1.medium` provides 1 vCPU and 4 GiB of memory. You can select a **Red Hat provided** instance type or a **User provided** instance type that an administrator has defined.

## Customization settings

The optional **Customization** step groups advanced settings into tabs. The following settings are the ones that most commonly affect VM behavior.

| Setting | Tab | Description |
|----|----|----|
| Disk interface | Storage | Determines disk performance and compatibility. **VirtIO** offers the best performance but requires additional drivers on Windows. **SATA** has lower performance but is supported by most operating systems, including Windows. **SCSI** supports large numbers of devices. |
| Ephemeral disk | Storage | Adds a disk from a container image whose changes are lost when the VM reboots. |
| Use this disk as a boot source | Storage | Marks a disk as bootable. Only one disk can be bootable at a time. |
| Headless mode | Details | Removes the default graphics device. VNC console access is not available when this option is enabled. |
| Deletion protection | Details | Prevents the VM from being deleted through the web console. |
| Boot mode | Details | Sets the firmware interface, such as BIOS or UEFI, used to boot the VM. |
| Run strategy | Scheduling | Controls how the VM behaves after a failure, shutdown, or restart, such as **Rerun on failure**. |
| Eviction strategy | Scheduling | Determines what happens to the VM when its node is drained. **LiveMigrate** moves the VM to another node instead of stopping it. |
| Network binding | Network | Sets how the network interface connects. **Masquerade** is the default for pod networking; **Bridge** connects to an L2 network; **SR-IOV** attaches a virtual function for high performance. |
| Initialization method | Initial run | Configures first-boot settings by using **cloud-init** for Linux guests or **Sysprep** for Windows guests. |
| Dynamic SSH key injection | SSH | Injects a public SSH key that is applied without restarting the VM. When it is not enabled, keys are applied through `virtctl`. |
| Labels and annotations | Metadata | **Labels** are key-value pairs that you can query to organize and select VMs. **Annotations** store arbitrary metadata that cannot be queried. |

Key customization settings
