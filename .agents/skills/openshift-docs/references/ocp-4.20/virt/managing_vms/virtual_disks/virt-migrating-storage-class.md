<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

You can migrate one or more virtual disks to a different storage class to optimize storage performance or reduce costs without stopping your virtual machine (VM) or virtual machine instance (VMI).

# Migrating VM disks to a different storage class by using the web console

You can migrate one or more disks attached to a virtual machine (VM) to a different storage class by using the OpenShift Container Platform web console. When performing this action on a running VM, the operation of the VM is not interrupted and the data on the migrated disks remains accessible.

<div>

<div class="title">

Prerequisites

</div>

- You must have a data volume or a persistent volume claim (PVC) available for storage class migration.

- The cluster must have a node available for live migration. As part of the storage class migration, the VM is live migrated to a different node.

- The VM must be running.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Navigate to **Virtualization** → **VirtualMachines** in the web console.

2.  Click the Options menu ![kebab](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABsAAAAjCAIAAADqn+bCAAAACXBIWXMAAA7EAAAOxAGVKw4bAAAA+0lEQVRIie2WMQqEMBBFJ47gUXRBLyBYqbUXULCx9CR2XsAb6AlUEM9kpckW7obdZhwWYWHXX/3i8TPJZEKEUgpOlXFu3JX4V4kmB2qaZhgGKSUiZlkWxzEBC84N9zxv27bdO47Tti0Bs3at4wBgXVca/lJnfN/XPggCGmadIwAsywIAiGhZFk1ydy2EYJKgGCqK4vZUVVU0zKpxnmftp2mi4S/1GhG1N82DMWNNYVmW4zgqpRAxTVMa5t4evlg11nXd9/1eY57nSZIQMKtG13WllLu3bbvrOgJmdUbHwfur8Xniqw6Hh5UYRdGDNowwDA+WvP4UV+JPJ94B1gKUWcTOCT0AAAAASUVORK5CYII=) beside the virtual machine and select **Migration** → **Storage**.

    You can also access this option from the **VirtualMachine details** page by selecting **Actions** → **Migration** → **Storage**.

    Alternatively, right-click the VM in the tree view and select **Migration** from the menu.

3.  On the **Migration details** page, choose whether to migrate the entire VM storage or selected volumes only. If you click **Selected volumes**, select any disks that you intend to migrate. Click **Next** to proceed.

4.  From the list of available options on the **Destination StorageClass** page, select the storage class to migrate to. Click **Next** to proceed.

5.  On the **Review** page, review the list of affected disks and the target storage class. To start the migration, click **Migrate VirtualMachine storage**.

6.  Stay on the **Migrate VirtualMachine storage** page to watch the progress and wait for the confirmation that the migration completed successfully.

</div>

<div>

<div class="title">

Verification

</div>

1.  From the **VirtualMachine details** page, navigate to **Configuration** → **Storage**.

2.  Verify that all disks have the expected storage class listed in the **Storage class** column.

</div>
