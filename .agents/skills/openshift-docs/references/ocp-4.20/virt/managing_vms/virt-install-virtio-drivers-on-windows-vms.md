<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

VirtIO drivers are paravirtualized device drivers required for Microsoft Windows virtual machines (VMs) to run in OpenShift Virtualization. The drivers are shipped with the rest of the images and do not require a separate download.

The `container-native-virtualization/virtio-win` container disk must be attached to the VM as a SATA CD drive to enable driver installation. You can install VirtIO drivers during Windows installation or add them to an existing Windows installation.

After the drivers are installed, the `container-native-virtualization/virtio-win` container disk can be removed from the VM.

| Driver name | Hardware ID | Description |
|----|----|----|
| **viostor** | VEN_1AF4&DEV_1001, VEN_1AF4&DEV_1042 | The block driver. Sometimes labeled as an **SCSI Controller** in the **Other devices** group. |
| **viorng** | VEN_1AF4&DEV_1005, VEN_1AF4&DEV_1044 | The entropy source driver. Sometimes labeled as a **PCI Device** in the **Other devices** group. |
| **NetKVM** | VEN_1AF4&DEV_1000, VEN_1AF4&DEV_1041 | The network driver. Sometimes labeled as an **Ethernet Controller** in the **Other devices** group. Available only if a VirtIO NIC is configured. |

Supported drivers

# Attaching VirtIO container disk to Windows VMs during installation

You must attach the VirtIO container disk to the Windows VM to install the necessary Windows drivers. This can be done during creation of the VM.

<div>

<div class="title">

Procedure

</div>

1.  When creating a Windows VM from a template, click **Customize VirtualMachine**.

2.  Select **Mount Windows drivers disk**.

3.  Click the **Customize VirtualMachine parameters**.

4.  Click **Create VirtualMachine**.

</div>

<div class="formalpara">

<div class="title">

Result

</div>

After the VM is created, the `virtio-win` SATA CD disk will be attached to the VM.

</div>

# Attaching VirtIO container disk to an existing Windows VM

You must attach the VirtIO container disk to the Windows VM to install the necessary Windows drivers. This can be done to an existing VM.

<div>

<div class="title">

Procedure

</div>

1.  Navigate to the existing Windows VM, and click **Actions** → **Stop**.

2.  Go to **VM Details** → **Configuration** → **Storage**.

3.  Select the **Mount Windows drivers disk** checkbox.

4.  Click **Save**.

5.  Start the VM, and connect to a graphical console.

</div>

# Installing VirtIO drivers from a container disk added as a SATA CD drive

You can install VirtIO drivers from a container disk that you add to a Windows virtual machine (VM) as a SATA CD drive.

> [!TIP]
> You do not need to download the `container-native-virtualization/virtio-win-rhel9` container disk. If the container disk is not present, the cluster downloads it from the Red Hat registry. However, to reduce the installation time, you can download the container disk in advance from the [Red Hat Ecosystem Catalog](https://catalog.redhat.com/en/software/containers/container-native-virtualization/virtio-win-rhel9/633ffae83be061d37b2770f6).

<div>

<div class="title">

Prerequisites

</div>

- You must have access to the Red Hat registry or to the downloaded `container-native-virtualization/virtio-win` container disk in a restricted environment.

- You have installed the `virtctl` CLI.

- You have installed the OpenShift CLI (`oc`).

</div>

<div>

<div class="title">

Procedure

</div>

1.  Add the `container-native-virtualization/virtio-win` container disk as a CD drive by editing the `VirtualMachine` manifest:

    ``` yaml
    # ...
    spec:
      domain:
        devices:
          disks:
            - name: virtiocontainerdisk
              bootOrder: 2
              cdrom:
                bus: sata
    volumes:
      - containerDisk:
          image: registry.redhat.io/container-native-virtualization/virtio-win-rhel9:v4.22
        name: virtiocontainerdisk
    ```

    OpenShift Virtualization boots the VM disks in the order defined in the `VirtualMachine` manifest. You can either define other VM disks that boot before the `container-native-virtualization/virtio-win` container disk, or use the optional `bootOrder` parameter to ensure the VM boots from the correct disk. If you configure the boot order for a disk, you must configure the boot order for the other disks.

2.  Apply the changes:

    - If the VM is not running, run the following command:

      ``` terminal
      $ virtctl start <vm> -n <namespace>
      ```

    - If the VM is running, reboot the VM or run the following command:

      ``` terminal
      $ oc apply -f <vm.yaml>
      ```

3.  After the VM has started, install the VirtIO drivers from the SATA CD drive.

</div>

# Installing VirtIO drivers during Windows installation

You can install the VirtIO drivers while installing Windows on a virtual machine (VM).

> [!NOTE]
> This procedure uses a generic approach to the Windows installation and the installation method might differ between versions of Windows. See the documentation for the version of Windows that you are installing.

<div>

<div class="title">

Prerequisites

</div>

- A storage device containing the `virtio` drivers must be attached to the VM.

</div>

<div>

<div class="title">

Procedure

</div>

1.  In the Windows operating system, use the `File Explorer` to navigate to the `virtio-win` CD drive.

2.  Double-click the drive to run the appropriate installer for your VM.

    For a 64-bit vCPU, select the `virtio-win-gt-x64` installer. 32-bit vCPUs are no longer supported.

3.  Optional: During the **Custom Setup** step of the installer, select the device drivers you want to install. The recommended driver set is selected by default.

4.  After the installation is complete, select **Finish**.

5.  Reboot the VM.

</div>

<div>

<div class="title">

Verification

</div>

1.  Open the system disk on the PC. This is typically `C:`.

2.  Navigate to **Program Files** → **Virtio-Win**.

</div>

If the **Virtio-Win** directory is present and contains a sub-directory for each driver, the installation was successful.

# Installing VirtIO drivers from a SATA CD drive on an existing Windows VM

You can install the VirtIO drivers from a SATA CD drive on an existing Windows virtual machine (VM).

> [!NOTE]
> This procedure uses a generic approach to adding drivers to Windows. See the installation documentation for your version of Windows for specific installation steps.

<div>

<div class="title">

Prerequisites

</div>

- A storage device containing the virtio drivers must be attached to the VM as a SATA CD drive.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Start the VM and connect to a graphical console.

2.  Log in to a Windows user session.

3.  Open **Device Manager** and expand **Other devices** to list any **Unknown device**.

    1.  Open the **Device Properties** to identify the unknown device.

    2.  Right-click the device and select **Properties**.

    3.  Click the **Details** tab and select **Hardware Ids** in the **Property** list.

    4.  Compare the **Value** for the **Hardware Ids** with the supported VirtIO drivers.

4.  Right-click the device and select **Update Driver Software**.

5.  Click **Browse my computer for driver software** and browse to the attached SATA CD drive, where the VirtIO drivers are located. The drivers are arranged hierarchically according to their driver type, operating system, and CPU architecture.

6.  Click **Next** to install the driver.

7.  Repeat this process for all the necessary VirtIO drivers.

8.  After the driver installs, click **Close** to close the window.

9.  Reboot the VM to complete the driver installation.

</div>
