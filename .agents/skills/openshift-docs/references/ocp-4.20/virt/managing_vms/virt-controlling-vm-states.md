<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

You can use `virtctl` to manage virtual machine states and perform other actions from the CLI. For example, you can use `virtctl` to force stop a VM or expose a port.

You can stop, start, restart, pause, and unpause virtual machines from the web console.

# Configuring RBAC permissions for managing VM states by using the web console

To allow users to manage virtual machine (VM) states by using the OpenShift Container Platform web console, you must create an RBAC cluster role and cluster role binding. The cluster role uses the `subresources.kubevirt.io` API to define which resources can be controlled by certain users or groups.

<div>

<div class="title">

Prerequisites

</div>

- You have cluster administrator access to an OpenShift Container Platform cluster where OpenShift Virtualization is installed.

- You have installed the OpenShift CLI (`oc`).

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create a `ClusterRole` object that allows the target user or group to manage VM states:

    ``` yaml
    apiVersion: rbac.authorization.k8s.io/v1
    kind: ClusterRole
    metadata:
      name: vm-manager-access
    rules:
      - apiGroups:
          - subresources.kubevirt.io
        resources:
          - virtualmachines/start
          - virtualmachines/stop
        verbs:
          - update
    # ...
    ```

2.  Run the following command to apply the cluster role:

    ``` terminal
    $ oc apply -f <filename>.yaml
    ```

3.  Confirm that the cluster role was created by running the following command and observing the output:

    ``` terminal
    $ oc get clusterrole <name>
    ```

    Example output:

    ``` terminal
    NAME                AGE
    vm-manager-access   15s
    ```

4.  Inspect the details of the cluster role, and ensure the intended rules for `subresources.kubevirt.io` are present, specifically the `virtualmachines/start` and `virtualmachines/stop` subresources.

    Run the following command and observe the output:

    ``` terminal
    $ oc describe clusterrole <name>
    ```

    Example output:

    ``` terminal
    Name:         vm-manager-access
    Labels:       <none>
    Annotations:  <none>
    PolicyRule:
      Resources  Non-Resource URLs  Resource Names  Verbs
      ---------  -----------------  --------------  -----
      virtualmachines/start, virtualmachines/stop with subresources.kubevirt.io group  []  []  [update]
    ```

5.  Create a `ClusterRoleBinding` object to bind the cluster role you have created to the target user or group:

    ``` yaml
    apiVersion: rbac.authorization.k8s.io/v1
    kind: ClusterRoleBinding
    metadata:
      name: vm-manager-access-binding
    subjects:
      - kind: User
        name: test-user
        apiGroup: rbac.authorization.k8s.io
    roleRef:
      kind: ClusterRole
      name: vm-manager-access
      apiGroup: rbac.authorization.k8s.io
    ```

6.  Run the following command to apply the cluster role binding:

    ``` terminal
    $ oc apply -f <filename>.yaml
    ```

7.  Confirm that the cluster role binding was created by running the following command and observing the output:

    ``` terminal
    $ oc get clusterrolebinding <name>
    ```

    Example output:

    ``` terminal
    NAME                        AGE
    vm-manager-access-binding   15s
    ```

</div>

<div>

<div class="title">

Verification

</div>

1.  Check if the user can start a VM by running the following command:

    ``` terminal
    $ oc auth can-i update virtualmachines/start --namespace=<namespace> --as=<user_name> --subresource=subresources.kubevirt.io
    ```

    Example output:

    ``` terminal
    yes
    ```

2.  Check if the user can stop a VM by running the following command:

    ``` terminal
    $ oc auth can-i update virtualmachines/stop --namespace=<namespace> --as=<user_name> --group=subresources.kubevirt.io
    ```

    Example output:

    ``` terminal
    yes
    ```

</div>

# Enabling confirmations of virtual machine actions

The **Stop**, **Restart**, and **Pause** actions can display confirmation dialogs if confirmation is enabled. By default, confirmation is disabled.

<div>

<div class="title">

Procedure

</div>

1.  In the **Virtualization** section of the OpenShift Container Platform web console, navigate to **Overview** → **Settings** → **Cluster** → **General settings**.

2.  Toggle the **VirtualMachine actions confirmation** setting to On.

</div>

# Starting a virtual machine

You can start a virtual machine (VM) from the web console.

<div>

<div class="title">

Procedure

</div>

1.  Click **Virtualization** → **VirtualMachines** from the side menu.

2.  In the tree view, select the project that contains the VM that you want to start.

3.  Navigate to the appropriate menu for your use case:

    - To stay on this page, where you can perform actions on multiple VMs:

      1.  Click the Options menu ![kebab](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABsAAAAjCAIAAADqn+bCAAAACXBIWXMAAA7EAAAOxAGVKw4bAAAA+0lEQVRIie2WMQqEMBBFJ47gUXRBLyBYqbUXULCx9CR2XsAb6AlUEM9kpckW7obdZhwWYWHXX/3i8TPJZEKEUgpOlXFu3JX4V4kmB2qaZhgGKSUiZlkWxzEBC84N9zxv27bdO47Tti0Bs3at4wBgXVca/lJnfN/XPggCGmadIwAsywIAiGhZFk1ydy2EYJKgGCqK4vZUVVU0zKpxnmftp2mi4S/1GhG1N82DMWNNYVmW4zgqpRAxTVMa5t4evlg11nXd9/1eY57nSZIQMKtG13WllLu3bbvrOgJmdUbHwfur8Xniqw6Hh5UYRdGDNowwDA+WvP4UV+JPJ94B1gKUWcTOCT0AAAAASUVORK5CYII=) located at the far right end of the row and click **Start VirtualMachine**.

    - To start the VM from the tree view:

      1.  Click the **\>** icon next to the project name to open the list of VMs.

      2.  Right-click the name of the VM and select **Start**.

    - To view comprehensive information about the selected VM before you start it:

      1.  Access the **VirtualMachine details** page by clicking the name of the VM.

      2.  Click **Actions** → **Start**.

          > [!NOTE]
          > When you start VM that is provisioned from a `URL` source for the first time, the VM has a status of **Importing** while OpenShift Virtualization imports the container from the URL endpoint. Depending on the size of the image, this process might take several minutes.

</div>

# Stopping a virtual machine

You can stop a virtual machine (VM) from the web console.

<div>

<div class="title">

Procedure

</div>

1.  Click **Virtualization** → **VirtualMachines** from the side menu.

2.  In the tree view, select the project that contains the VM that you want to stop.

3.  Navigate to the appropriate menu for your use case:

    - To stay on this page, where you can perform actions on multiple VMs:

      1.  Click the Options menu ![kebab](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABsAAAAjCAIAAADqn+bCAAAACXBIWXMAAA7EAAAOxAGVKw4bAAAA+0lEQVRIie2WMQqEMBBFJ47gUXRBLyBYqbUXULCx9CR2XsAb6AlUEM9kpckW7obdZhwWYWHXX/3i8TPJZEKEUgpOlXFu3JX4V4kmB2qaZhgGKSUiZlkWxzEBC84N9zxv27bdO47Tti0Bs3at4wBgXVca/lJnfN/XPggCGmadIwAsywIAiGhZFk1ydy2EYJKgGCqK4vZUVVU0zKpxnmftp2mi4S/1GhG1N82DMWNNYVmW4zgqpRAxTVMa5t4evlg11nXd9/1eY57nSZIQMKtG13WllLu3bbvrOgJmdUbHwfur8Xniqw6Hh5UYRdGDNowwDA+WvP4UV+JPJ94B1gKUWcTOCT0AAAAASUVORK5CYII=) located at the far right end of the row and click **Stop VirtualMachine**.

      2.  If action confirmation is enabled, click **Stop** in the confirmation dialog.

    - To stop the VM from the tree view:

      1.  Click the **\>** icon next to the project name to open the list of VMs.

      2.  Right-click the name of the VM and select **Stop**.

      3.  If action confirmation is enabled, click **Stop** in the confirmation dialog.

    - To view comprehensive information about the selected VM before you stop it:

      1.  Access the **VirtualMachine details** page by clicking the name of the VM.

      2.  Click **Actions** → **Stop**.

      3.  If action confirmation is enabled, click **Stop** in the confirmation dialog.

</div>

# Restarting a virtual machine

You can restart a running virtual machine (VM) from the web console.

> [!IMPORTANT]
> To avoid errors, do not restart a VM while it has a status of **Importing**.

<div>

<div class="title">

Procedure

</div>

1.  Click **Virtualization** → **VirtualMachines** from the side menu.

2.  In the tree view, select the project that contains the VM that you want to restart.

3.  Navigate to the appropriate menu for your use case:

    - To stay on this page, where you can perform actions on multiple VMs:

      1.  Click the Options menu ![kebab](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABsAAAAjCAIAAADqn+bCAAAACXBIWXMAAA7EAAAOxAGVKw4bAAAA+0lEQVRIie2WMQqEMBBFJ47gUXRBLyBYqbUXULCx9CR2XsAb6AlUEM9kpckW7obdZhwWYWHXX/3i8TPJZEKEUgpOlXFu3JX4V4kmB2qaZhgGKSUiZlkWxzEBC84N9zxv27bdO47Tti0Bs3at4wBgXVca/lJnfN/XPggCGmadIwAsywIAiGhZFk1ydy2EYJKgGCqK4vZUVVU0zKpxnmftp2mi4S/1GhG1N82DMWNNYVmW4zgqpRAxTVMa5t4evlg11nXd9/1eY57nSZIQMKtG13WllLu3bbvrOgJmdUbHwfur8Xniqw6Hh5UYRdGDNowwDA+WvP4UV+JPJ94B1gKUWcTOCT0AAAAASUVORK5CYII=) located at the far right end of the row and click **Restart**.

      2.  If action confirmation is enabled, click **Restart** in the confirmation dialog.

    - To restart the VM from the tree view:

      1.  Click the **\>** icon next to the project name to open the list of VMs.

      2.  Right-click the name of the VM and select **Restart**.

      3.  If action confirmation is enabled, click **Restart** in the confirmation dialog.

    - To view comprehensive information about the selected VM before you restart it:

      1.  Access the **VirtualMachine details** page by clicking the name of the virtual machine.

      2.  Click **Actions** → **Restart**.

      3.  If action confirmation is enabled, click **Restart** in the confirmation dialog.

</div>

# Pausing a virtual machine

You can pause a virtual machine (VM) from the web console.

<div>

<div class="title">

Procedure

</div>

1.  Click **Virtualization** → **VirtualMachines** from the side menu.

2.  In the tree view, select the project that contains the VM that you want to pause.

3.  Navigate to the appropriate menu for your use case:

    - To stay on this page, where you can perform actions on multiple VMs:

      1.  Click the Options menu ![kebab](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABsAAAAjCAIAAADqn+bCAAAACXBIWXMAAA7EAAAOxAGVKw4bAAAA+0lEQVRIie2WMQqEMBBFJ47gUXRBLyBYqbUXULCx9CR2XsAb6AlUEM9kpckW7obdZhwWYWHXX/3i8TPJZEKEUgpOlXFu3JX4V4kmB2qaZhgGKSUiZlkWxzEBC84N9zxv27bdO47Tti0Bs3at4wBgXVca/lJnfN/XPggCGmadIwAsywIAiGhZFk1ydy2EYJKgGCqK4vZUVVU0zKpxnmftp2mi4S/1GhG1N82DMWNNYVmW4zgqpRAxTVMa5t4evlg11nXd9/1eY57nSZIQMKtG13WllLu3bbvrOgJmdUbHwfur8Xniqw6Hh5UYRdGDNowwDA+WvP4UV+JPJ94B1gKUWcTOCT0AAAAASUVORK5CYII=) located at the far right end of the row and click **Pause VirtualMachine**.

      2.  If action confirmation is enabled, click **Pause** in the confirmation dialog.

    - To pause the VM from the tree view:

      1.  Click the **\>** icon next to the project name to open the list of VMs.

      2.  Right-click the name of the VM and select **Pause**.

      3.  If action confirmation is enabled, click **Pause** in the confirmation dialog.

    - To view comprehensive information about the selected VM before you pause it:

      1.  Access the **VirtualMachine details** page by clicking the name of the VM.

      2.  Click **Actions** → **Pause**.

      3.  If action confirmation is enabled, click **Pause** in the confirmation dialog.

</div>

# Unpausing a virtual machine

You can unpause a paused virtual machine (VM) from the web console.

<div>

<div class="title">

Prerequisites

</div>

- At least one of your VMs must have a status of **Paused**.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Click **Virtualization** → **VirtualMachines** from the side menu.

2.  In the tree view, select the project that contains the VM that you want to unpause.

3.  Navigate to the appropriate menu for your use case:

    - To stay on this page, where you can perform actions on multiple VMs:

      1.  Click the Options menu ![kebab](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABsAAAAjCAIAAADqn+bCAAAACXBIWXMAAA7EAAAOxAGVKw4bAAAA+0lEQVRIie2WMQqEMBBFJ47gUXRBLyBYqbUXULCx9CR2XsAb6AlUEM9kpckW7obdZhwWYWHXX/3i8TPJZEKEUgpOlXFu3JX4V4kmB2qaZhgGKSUiZlkWxzEBC84N9zxv27bdO47Tti0Bs3at4wBgXVca/lJnfN/XPggCGmadIwAsywIAiGhZFk1ydy2EYJKgGCqK4vZUVVU0zKpxnmftp2mi4S/1GhG1N82DMWNNYVmW4zgqpRAxTVMa5t4evlg11nXd9/1eY57nSZIQMKtG13WllLu3bbvrOgJmdUbHwfur8Xniqw6Hh5UYRdGDNowwDA+WvP4UV+JPJ94B1gKUWcTOCT0AAAAASUVORK5CYII=) located at the far right end of the row and click **Unpause VirtualMachine**.

    - To unpause the VM from the tree view:

      1.  Click the **\>** icon next to the project name to open the list of VMs.

      2.  Right-click the name of the VM and select **Unpause**.

    - To view comprehensive information about the selected VM before you unpause it:

      1.  Access the **VirtualMachine details** page by clicking the name of the virtual machine.

      2.  Click **Actions** → **Unpause**.

</div>

# Controlling the state of multiple virtual machines

You can start, stop, restart, pause, and unpause multiple virtual machines (VMs) from the web console.

<div>

<div class="title">

Procedure

</div>

1.  Navigate to **Virtualization** → **VirtualMachines** in the web console.

2.  Optional: Enable the **Show only projects with VirtualMachines** option above the tree view to limit the displayed projects.

3.  Select a relevant project from the tree view.

4.  Navigate to the appropriate menu for your use case:

    - To change the state of all VMs in the selected project:

      1.  Right-click the name of the project in the tree view and select the intended action from the menu.

      2.  If action confirmation is enabled, confirm the action in the confirmation dialog.

    - To change the state of specific VMs:

      1.  Select a checkbox next to the VMs you want to work with. To select all VMs, click the checkbox in the **VirtualMachines** table header.

      2.  Click **Actions** and select the intended action from the menu.

      3.  If action confirmation is enabled, confirm the action in the confirmation dialog.

</div>

# Additional resources

- [Using the CLI tools](../getting_started/virt-using-the-cli-tools.md#virt-using-the-cli-tools)
