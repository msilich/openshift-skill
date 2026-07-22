<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

You can manage the link state of a primary or secondary virtual machine (VM) interface by using the OpenShift Container Platform web console or the CLI. By specifying the link state, you can logically connect or disconnect the virtual network interface controller (vNIC) from a network.

> [!NOTE]
> OpenShift Virtualization does not support link state management for Single Root I/O Virtualization (SR-IOV) secondary network interfaces and their link states are not reported.

You can specify the desired link state when you first create a VM, by editing the configuration of an existing VM that is stopped or running, or when you hot plug a new network interface to a running VM. If you edit a running VM, you do not need to restart or migrate the VM for the changes to be applied. The current link state of a VM interface is reported in the `status.interfaces.linkState` field of the `VirtualMachineInstance` manifest.

# Setting the VM interface link state by using the web console

You can set the link state of a primary or secondary virtual machine (VM) network interface by using the web console.

<div>

<div class="title">

Prerequisites

</div>

- You are logged into the OpenShift Container Platform web console.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Navigate to **Virtualization** → **VirtualMachines**.

2.  Select a VM to view the **VirtualMachine details** page.

3.  On the **Configuration** tab, click **Network**. A list of network interfaces is displayed.

4.  Click the Options menu ![kebab](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABsAAAAjCAIAAADqn+bCAAAACXBIWXMAAA7EAAAOxAGVKw4bAAAA+0lEQVRIie2WMQqEMBBFJ47gUXRBLyBYqbUXULCx9CR2XsAb6AlUEM9kpckW7obdZhwWYWHXX/3i8TPJZEKEUgpOlXFu3JX4V4kmB2qaZhgGKSUiZlkWxzEBC84N9zxv27bdO47Tti0Bs3at4wBgXVca/lJnfN/XPggCGmadIwAsywIAiGhZFk1ydy2EYJKgGCqK4vZUVVU0zKpxnmftp2mi4S/1GhG1N82DMWNNYVmW4zgqpRAxTVMa5t4evlg11nXd9/1eY57nSZIQMKtG13WllLu3bbvrOgJmdUbHwfur8Xniqw6Hh5UYRdGDNowwDA+WvP4UV+JPJ94B1gKUWcTOCT0AAAAASUVORK5CYII=) of the interface that you want to edit.

5.  Choose the appropriate option to set the interface link state:

    - If the current interface link state is `up`, select **Set link down**.

    - If the current interface link state is `down`, select **Set link up**.

</div>

# Setting the VM interface link state by using the CLI

You can set the link state of a primary or secondary virtual machine (VM) network interface by using the CLI.

<div>

<div class="title">

Prerequisites

</div>

- You have installed the OpenShift CLI (`oc`).

</div>

<div>

<div class="title">

Procedure

</div>

1.  Edit the VM configuration to set the interface link state, as in the following example:

    ``` yaml
    apiVersion: kubevirt.io/v1
    kind: VirtualMachine
    metadata:
      name: my-vm
    spec:
      template:
        spec:
          domain:
            devices:
              interfaces:
                - name: default
                  state: down
                  masquerade: { }
          networks:
            - name: default
              pod: { }
    # ...
    ```

    - `spec.template.spec.domain.devices.interfaces.name` defines the name of the interface.

    - `spec.template.spec.domain.devices.interfaces.state` defines the state of the interface. The possible values are:

      - `up`: Represents an active network connection. This is the default if no value is specified.

      - `down`: Represents a network interface link that is switched off.

      - `absent`: Represents a network interface that is hot unplugged.

        > [!IMPORTANT]
        > If you have defined readiness or liveness probes to run VM health checks, setting the primary interface’s link state to `down` causes the probes to fail. If a liveness probe fails, the VM is deleted and a new VM is created to restore responsiveness.

2.  Apply the `VirtualMachine` manifest:

    ``` terminal
    $ oc apply -f <filename>.yaml
    ```

</div>

<div>

<div class="title">

Verification

</div>

- Verify that the desired link state is set by checking the `status.interfaces.linkState` field of the `VirtualMachineInstance` manifest.

  ``` terminal
  $ oc get vmi <vmi-name>
  ```

  Example output:

  ``` yaml
  apiVersion: kubevirt.io/v1
  kind: VirtualMachineInstance
  metadata:
    name: my-vm
  spec:
    domain:
      devices:
        interfaces:
        - name: default
          state: down
          masquerade: { }
    networks:
    - name: default
      pod: { }
  status:
    interfaces:
      - name: default
        linkState: down
  # ...
  ```

</div>
