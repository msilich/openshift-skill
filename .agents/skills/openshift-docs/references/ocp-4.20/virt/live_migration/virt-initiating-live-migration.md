<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

To move a running virtual machine (VM) to a different node without interrupting the workload, you can initiate a live migration. You can also cancel an ongoing migration to keep the VM on its original node.

You can initiate the live migration of a virtual machine (VM) to another node by using the OpenShift Container Platform web console or the command line.

You can cancel a live migration by using the web console or the command line. The VM remains on its original node.

> [!TIP]
> You can also initiate and cancel live migration by using the `virtctl migrate <vm_name>` and `virtctl migrate-cancel <vm_name>` commands.

# Initiating live migration by using the web console

You can live migrate a running virtual machine (VM) to a different node in the cluster by using the OpenShift Container Platform web console.

> [!NOTE]
> The **Migrate** action is visible to all users but only cluster administrators can initiate a live migration.

<div>

<div class="title">

Prerequisites

</div>

- You have the `kubevirt.io:migrate` RBAC role or you are a cluster administrator.

- The VM is able to be migrated.

- If the VM is configured with a host model CPU, the cluster has an available node that supports the CPU model.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Navigate to **Virtualization** → **VirtualMachines** in the web console.

2.  Take either of the following steps:

    - Click the Options menu ![kebab](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABsAAAAjCAIAAADqn+bCAAAACXBIWXMAAA7EAAAOxAGVKw4bAAAA+0lEQVRIie2WMQqEMBBFJ47gUXRBLyBYqbUXULCx9CR2XsAb6AlUEM9kpckW7obdZhwWYWHXX/3i8TPJZEKEUgpOlXFu3JX4V4kmB2qaZhgGKSUiZlkWxzEBC84N9zxv27bdO47Tti0Bs3at4wBgXVca/lJnfN/XPggCGmadIwAsywIAiGhZFk1ydy2EYJKgGCqK4vZUVVU0zKpxnmftp2mi4S/1GhG1N82DMWNNYVmW4zgqpRAxTVMa5t4evlg11nXd9/1eY57nSZIQMKtG13WllLu3bbvrOgJmdUbHwfur8Xniqw6Hh5UYRdGDNowwDA+WvP4UV+JPJ94B1gKUWcTOCT0AAAAASUVORK5CYII=) beside the VM you want to migrate, hover over the **Migrate** option, and select **Compute**.

    - Open the **VM details** page of the VM you want to migrate, click the **Actions** menu, hover over the **Migrate** option, and select **Compute**.

3.  In the **Migrate Virtual Machine to a different Node** dialog box, select either **Automatically Selected Node** or **Specific Node**.

    1.  If you selected the **Specific Node** option, choose a node from the list.

4.  Click **Migrate Virtual Machine**.

</div>

# Initiating live migration by using the CLI

You can initiate the live migration of a running virtual machine (VM) by using the command line to create a `VirtualMachineInstanceMigration` object for the VM.

<div>

<div class="title">

Prerequisites

</div>

- You have installed the OpenShift CLI (`oc`).

- You have the `kubevirt.io:migrate` RBAC role or you are a cluster administrator.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create a `VirtualMachineInstanceMigration` manifest for the VM that you want to migrate:

    ``` yaml
    apiVersion: kubevirt.io/v1
    kind: VirtualMachineInstanceMigration
    metadata:
      name: <migration_name>
    spec:
      vmiName: <vm_name>
    ```

2.  Create the object by running the following command:

    ``` terminal
    $ oc create -f <migration_name>.yaml
    ```

    The `VirtualMachineInstanceMigration` object triggers a live migration of the VM. This object exists in the cluster only while the virtual machine instance is running, unless manually deleted.

</div>

<div>

<div class="title">

Verification

</div>

- Obtain the VM status by running the following command:

  ``` terminal
  $ oc describe vmi <vm_name> -n <namespace>
  ```

  Example output:

  ``` yaml
  # ...
  Status:
    Conditions:
      Last Probe Time:       <nil>
      Last Transition Time:  <nil>
      Status:                True
      Type:                  LiveMigratable
    Migration Method:  LiveMigration
    Migration State:
      Completed:                    true
      End Timestamp:                2018-12-24T06:19:42Z
      Migration UID:                d78c8962-0743-11e9-a540-fa163e0c69f1
      Source Node:                  node2.example.com
      Start Timestamp:              2018-12-24T06:19:35Z
      Target Node:                  node1.example.com
      Target Node Address:          10.9.0.18:43891
      Target Node Domain Detected:  true
  ```

</div>

# Canceling live migration by using the web console

You can cancel the live migration of a virtual machine (VM) by using the OpenShift Container Platform web console.

<div>

<div class="title">

Prerequisites

</div>

- You have the `kubevirt.io:migrate` RBAC role or you are a cluster administrator.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Navigate to **Virtualization** → **VirtualMachines** in the web console.

2.  Select **Cancel Migration** on the Options menu ![kebab](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABsAAAAjCAIAAADqn+bCAAAACXBIWXMAAA7EAAAOxAGVKw4bAAAA+0lEQVRIie2WMQqEMBBFJ47gUXRBLyBYqbUXULCx9CR2XsAb6AlUEM9kpckW7obdZhwWYWHXX/3i8TPJZEKEUgpOlXFu3JX4V4kmB2qaZhgGKSUiZlkWxzEBC84N9zxv27bdO47Tti0Bs3at4wBgXVca/lJnfN/XPggCGmadIwAsywIAiGhZFk1ydy2EYJKgGCqK4vZUVVU0zKpxnmftp2mi4S/1GhG1N82DMWNNYVmW4zgqpRAxTVMa5t4evlg11nXd9/1eY57nSZIQMKtG13WllLu3bbvrOgJmdUbHwfur8Xniqw6Hh5UYRdGDNowwDA+WvP4UV+JPJ94B1gKUWcTOCT0AAAAASUVORK5CYII=) beside a VM.

</div>

# Canceling live migration by using the CLI

Cancel the live migration of a virtual machine by deleting the `VirtualMachineInstanceMigration` object associated with the migration.

<div>

<div class="title">

Prerequisites

</div>

- You have installed the OpenShift CLI (`oc`).

- You have the `kubevirt.io:migrate` RBAC role or you are a cluster administrator.

</div>

<div>

<div class="title">

Procedure

</div>

- Delete the `VirtualMachineInstanceMigration` object that triggered the live migration, `migration-job` in this example:

  ``` terminal
  $ oc delete vmim migration-job
  ```

</div>

# Additional resources

- [About live migration permissions](virt-about-live-migration.md#virt-about-live-migration-permissions_virt-about-live-migration)

- [Initiating live migration by using the web console](virt-initiating-live-migration.md#virt-initiating-vm-migration-web_virt-initiating-live-migration)

- [Initiating live migration by using the CLI](virt-initiating-live-migration.md#virt-initiating-vm-migration-cli_virt-initiating-live-migration)

- [Canceling live migration by using the web console](virt-initiating-live-migration.md#virt-canceling-vm-migration-web_virt-initiating-live-migration)

- [Canceling live migration by using the CLI](virt-initiating-live-migration.md#virt-canceling-vm-migration-cli_virt-initiating-live-migration)
