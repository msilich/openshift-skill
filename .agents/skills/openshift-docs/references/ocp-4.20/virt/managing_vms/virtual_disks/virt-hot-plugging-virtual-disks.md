<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

You can hot-plug or hot-unplug virtual disks from running VMs to dynamically adjust storage without downtime.

Only data volumes and persistent volume claims (PVCs) can be hot plugged and hot-unplugged. You cannot hot plug or hot-unplug container disks.

A hot plugged disk remains attached to the VM even after reboot. You must unplug the disk to remove it from the VM.

> [!NOTE]
> Each VM has a `virtio-scsi` controller so that hot plugged disks can use the SCSI bus. The `virtio-scsi` controller overcomes the limitations of VirtIO while retaining its performance advantages. It is highly scalable and supports hot plugging over 4 million disks.
>
> When you hot plug disks to the VirtIO (`virtio-blk`) bus, each disk uses a PCI Express (PCIe) slot in the VM. The number of PCIe slots is limited and pre-set automatically at the VM creation as specified in the "Available VirtIO Ports" table. Therefore, you can use `virtio-blk` for a small number of disks that does not exceed the number of available slots.

# Hot plugging and hot unplugging a disk by using the web console

You can hot plug a disk by attaching it to a virtual machine (VM) while the VM is running by using the OpenShift Container Platform web console.

The hot plugged disk remains attached to the VM until you unplug it.

<div>

<div class="title">

Prerequisites

</div>

- You must have a data volume or persistent volume claim (PVC) available for hot plugging.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Navigate to **Virtualization** → **VirtualMachines** in the web console.

2.  Select a running VM to view its details.

3.  On the **VirtualMachine details** page, click **Configuration** → **Storage**.

4.  Add a hot plugged disk:

    1.  Click **Add**.

    2.  In the **Add disk (hot plugged)** window, select the disk from the **Source** list and click **Save**.

5.  Optional: Select the type of the interface bus. The options are **VirtIO** and **SCSI**. The default bus type is **VirtIO**.

6.  Optional: Change the type of the interface bus of an existing hot plugged disk:

    1.  Click the Options menu ![kebab](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABsAAAAjCAIAAADqn+bCAAAACXBIWXMAAA7EAAAOxAGVKw4bAAAA+0lEQVRIie2WMQqEMBBFJ47gUXRBLyBYqbUXULCx9CR2XsAb6AlUEM9kpckW7obdZhwWYWHXX/3i8TPJZEKEUgpOlXFu3JX4V4kmB2qaZhgGKSUiZlkWxzEBC84N9zxv27bdO47Tti0Bs3at4wBgXVca/lJnfN/XPggCGmadIwAsywIAiGhZFk1ydy2EYJKgGCqK4vZUVVU0zKpxnmftp2mi4S/1GhG1N82DMWNNYVmW4zgqpRAxTVMa5t4evlg11nXd9/1eY57nSZIQMKtG13WllLu3bbvrOgJmdUbHwfur8Xniqw6Hh5UYRdGDNowwDA+WvP4UV+JPJ94B1gKUWcTOCT0AAAAASUVORK5CYII=) beside the disk and select the **Edit** option.

    2.  In the **Interface** field, select the desired option.

7.  Optional: Unplug a hot plugged disk:

    1.  Click the Options menu ![kebab](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABsAAAAjCAIAAADqn+bCAAAACXBIWXMAAA7EAAAOxAGVKw4bAAAA+0lEQVRIie2WMQqEMBBFJ47gUXRBLyBYqbUXULCx9CR2XsAb6AlUEM9kpckW7obdZhwWYWHXX/3i8TPJZEKEUgpOlXFu3JX4V4kmB2qaZhgGKSUiZlkWxzEBC84N9zxv27bdO47Tti0Bs3at4wBgXVca/lJnfN/XPggCGmadIwAsywIAiGhZFk1ydy2EYJKgGCqK4vZUVVU0zKpxnmftp2mi4S/1GhG1N82DMWNNYVmW4zgqpRAxTVMa5t4evlg11nXd9/1eY57nSZIQMKtG13WllLu3bbvrOgJmdUbHwfur8Xniqw6Hh5UYRdGDNowwDA+WvP4UV+JPJ94B1gKUWcTOCT0AAAAASUVORK5CYII=) beside the disk and select **Detach**.

    2.  Click **Detach**.

</div>

# Hot plugging and hot unplugging a disk by using the CLI

You can hot plug and hot unplug a disk while a virtual machine (VM) is running by using the command line.

The hot plugged disk remains attached to the VM until you unplug it.

<div>

<div class="title">

Prerequisites

</div>

- You must have at least one data volume or persistent volume claim (PVC) available for hot plugging.

</div>

<div>

<div class="title">

Procedure

</div>

- Hot plug a disk by running the following command:

  ``` terminal
  $ virtctl addvolume <virtual-machine|virtual-machine-instance> \
    --volume-name=<datavolume|PVC> \
    [--bus <bus_type>] [--serial=<label_name>]
  ```

  - The optional `--bus` flag allows you to specify the bus type of the added disk. The options are `virtio` and `scsi`. The default bus type is `virtio`.

  - The optional `--serial` flag allows you to add an alphanumeric string label of your choice. This helps you to identify the hot plugged disk in a guest virtual machine. If you do not specify this option, the label defaults to the name of the hot plugged data volume or PVC.

- Hot unplug a disk by running the following command:

  ``` terminal
  $ virtctl removevolume <virtual-machine|virtual-machine-instance> \
    --volume-name=<datavolume|PVC>
  ```

</div>

# Additional resources

- [Available VirtIO Ports](https://kubevirt.io/user-guide/storage/hotplug_volumes/#available-virtio-ports)
