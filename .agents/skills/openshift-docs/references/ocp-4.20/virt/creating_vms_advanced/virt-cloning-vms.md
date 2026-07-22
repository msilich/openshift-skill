<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

You can clone virtual machines (VMs) or create new VMs from snapshots.

> [!IMPORTANT]
> Cloning a VM with a vTPM device attached to it or creating a new VM from its snapshot is not supported.

# Cloning a VM by using the web console

You can clone an existing VM by using the web console.

<div>

<div class="title">

Procedure

</div>

1.  Navigate to **Virtualization** → **VirtualMachines** in the web console.

2.  Select a VM to open the **VirtualMachine details** page.

3.  Click **Actions**.

    Alternatively, access the same menu in the tree view by right-clicking the VM.

4.  Select **Clone**.

5.  On the **Clone VirtualMachine** page, enter the name of the new VM.

6.  (Optional) Select the **Start cloned VM** checkbox to start the cloned VM.

7.  Click **Clone**.

</div>

# Creating a VM from an existing snapshot by using the web console

You can create a new VM by copying an existing snapshot.

<div>

<div class="title">

Procedure

</div>

1.  Navigate to **Virtualization** → **VirtualMachines** in the web console.

2.  Select a VM to open the **VirtualMachine details** page.

3.  Click the **Snapshots** tab.

4.  Click the Options menu ![kebab](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABsAAAAjCAIAAADqn+bCAAAACXBIWXMAAA7EAAAOxAGVKw4bAAAA+0lEQVRIie2WMQqEMBBFJ47gUXRBLyBYqbUXULCx9CR2XsAb6AlUEM9kpckW7obdZhwWYWHXX/3i8TPJZEKEUgpOlXFu3JX4V4kmB2qaZhgGKSUiZlkWxzEBC84N9zxv27bdO47Tti0Bs3at4wBgXVca/lJnfN/XPggCGmadIwAsywIAiGhZFk1ydy2EYJKgGCqK4vZUVVU0zKpxnmftp2mi4S/1GhG1N82DMWNNYVmW4zgqpRAxTVMa5t4evlg11nXd9/1eY57nSZIQMKtG13WllLu3bbvrOgJmdUbHwfur8Xniqw6Hh5UYRdGDNowwDA+WvP4UV+JPJ94B1gKUWcTOCT0AAAAASUVORK5CYII=) for the snapshot you want to copy.

5.  Select **Create VirtualMachine**.

6.  Enter the name of the virtual machine.

7.  (Optional) Select the **Start this VirtualMachine after creation** checkbox to start the new virtual machine.

8.  Click **Create**.

</div>

# Additional resources

- [Creating VMs by cloning PVCs](virt-creating-vms-by-cloning-pvcs.md#virt-creating-vms-by-cloning-pvcs)
