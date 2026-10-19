<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

The Peripheral Component Interconnect (PCI) passthrough feature enables you to access and manage hardware devices from a virtual machine (VM). When PCI passthrough is configured, the PCI devices function as if they were physically attached to the guest operating system.

# Node preparation for GPU passthrough

You can prevent GPU operands from deploying on worker nodes that you designated for GPU passthrough.

## Preventing NVIDIA GPU operands from deploying on nodes

If you use the [NVIDIA GPU Operator](https://docs.nvidia.com/datacenter/cloud-native/gpu-operator/openshift/contents.html) in your cluster, you can apply the `nvidia.com/gpu.deploy.operands=false` label to nodes that you do not want to configure for GPU or vGPU operands. This prevents the creation of the pods that configure GPU or vGPU operands and terminates existing pods.

<div>

<div class="title">

Prerequisites

</div>

- The OpenShift CLI (`oc`) is installed.

</div>

<div>

<div class="title">

Procedure

</div>

- Label the node by running the following command:

  ``` terminal
  $ oc label node <node_name> nvidia.com/gpu.deploy.operands=false
  ```

  where:

  `<node_name>`
  Specifies the name of a node where you do not want to install the NVIDIA GPU operands.

</div>

<div>

<div class="title">

Verification

</div>

1.  Verify that the label was added to the node by running the following command:

    ``` terminal
    $ oc describe node <node_name>
    ```

2.  Optional: If GPU operands were previously deployed on the node, verify their removal.

    1.  Check the status of the pods in the `nvidia-gpu-operator` namespace by running the following command:

        ``` terminal
        $ oc get pods -n nvidia-gpu-operator
        ```

        Example output:

        ``` terminal
        NAME                             READY   STATUS        RESTARTS   AGE
        gpu-operator-59469b8c5c-hw9wj    1/1     Running       0          8d
        nvidia-sandbox-validator-7hx98   1/1     Running       0          8d
        nvidia-sandbox-validator-hdb7p   1/1     Running       0          8d
        nvidia-sandbox-validator-kxwj7   1/1     Terminating   0          9d
        nvidia-vfio-manager-7w9fs        1/1     Running       0          8d
        nvidia-vfio-manager-866pz        1/1     Running       0          8d
        nvidia-vfio-manager-zqtck        1/1     Terminating   0          9d
        ```

    2.  Monitor the pod status until the pods with `Terminating` status are removed:

        ``` terminal
        $ oc get pods -n nvidia-gpu-operator
        ```

        Example output:

        ``` terminal
        NAME                             READY   STATUS    RESTARTS   AGE
        gpu-operator-59469b8c5c-hw9wj    1/1     Running   0          8d
        nvidia-sandbox-validator-7hx98   1/1     Running   0          8d
        nvidia-sandbox-validator-hdb7p   1/1     Running   0          8d
        nvidia-vfio-manager-7w9fs        1/1     Running   0          8d
        nvidia-vfio-manager-866pz        1/1     Running   0          8d
        ```

</div>

# Preparing host devices for PCI passthrough

## About preparing a host device for PCI passthrough

To prepare a host device for PCI passthrough by using the CLI, create a `MachineConfig` object and add kernel arguments to enable the Input-Output Memory Management Unit (IOMMU).

Bind the PCI device to the Virtual Function I/O (VFIO) driver and then expose it in the cluster by editing the `permittedHostDevices` field of the `HyperConverged` custom resource (CR). The `permittedHostDevices` list is empty when you first install the OpenShift Virtualization Operator.

To remove a PCI host device from the cluster by using the CLI, delete the PCI device information from the `HyperConverged` CR.

## Kernel module blocklist for PCI passthrough

For `vfio-pci` to allocate a PCI device, no other kernel driver can manage that device. If a driver already manages the device, you must add the specific kernel module to a blocklist. Adding a kernel module to a blocklist makes all devices handled by that module unavailable to the host.

Cluster administrators can expose and manage host devices that are permitted to be used in the cluster by using the `oc` command-line interface (CLI).

You can add a kernel module to the blocklist by creating a `MachineConfig` object that generates a configuration file in `/etc/modprobe.d/` and adds kernel arguments.

The following example shows a `MachineConfig` object that adds the `enic` network driver to the blocklist:

``` yaml
apiVersion: machineconfiguration.openshift.io/v1
kind: MachineConfig
metadata:
  labels:
    machineconfiguration.openshift.io/role: worker
  name: 100-blocklist-enic
spec:
  config:
    ignition:
      version: 3.4.0
    storage:
      files:
      - contents:
          source: data:,blocklist%20enic%0A
        mode: 420
        overwrite: true
        path: /etc/modprobe.d/blocklist-enic.conf
  kernelArguments:
    - enic.blocklist=1
    - rd.driver.blocklist=enic
```

## Adding kernel arguments to enable the IOMMU driver

You must enable the Input-Output Memory Management Unit (IOMMU) driver before you can configure mediated devices. To enable the IOMMU driver in the kernel, create the `MachineConfig` object and add the kernel arguments.

<div>

<div class="title">

Prerequisites

</div>

- You have cluster administrator permissions.

- Your CPU hardware is Intel or AMD.

  > [!NOTE]
  > Enabling IOMMU is not required on `s390x` architecture.

- You enabled Intel Virtualization Technology for Directed I/O extensions or AMD IOMMU in the BIOS.

- You have installed the OpenShift CLI (`oc`).

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create a `MachineConfig` object that identifies the kernel argument. The following example shows a kernel argument for an Intel CPU.

    ``` yaml
    apiVersion: machineconfiguration.openshift.io/v1
    kind: MachineConfig
    metadata:
      labels:
        machineconfiguration.openshift.io/role: worker
      name: 100-worker-iommu
    spec:
      config:
        ignition:
          version: 3.2.0
      kernelArguments:
          - intel_iommu=on
    # ...
    ```

    - `metadata.labels.machineconfiguration.openshift.io/role` specifies that the new kernel argument is applied only to worker nodes.

    - `metadata.name` specifies the ranking of this kernel argument (100) among the machine configs and its purpose. If you have an AMD CPU, specify the kernel argument as `amd_iommu=on`.

    - `spec.kernelArguments` specifies the kernel argument as `intel_iommu` for an Intel CPU.

2.  Create the new `MachineConfig` object:

    ``` terminal
    $ oc create -f 100-worker-kernel-arg-iommu.yaml
    ```

</div>

<div>

<div class="title">

Verification

</div>

1.  Verify that the new `MachineConfig` object was added by entering the following command and observing the output:

    ``` terminal
    $ oc get MachineConfig
    ```

    Example output:

    ``` terminal
    NAME                                       IGNITIONVERSION                    AGE
    00-master                                   3.5.0                             164m
    00-worker                                   3.5.0                             164m
    01-master-container-runtime                 3.5.0                             164m
    01-master-kubelet                           3.5.0                             164m
    01-worker-container-runtime                 3.5.0                             164m
    01-worker-kubelet                           3.5.0                             164m
    100-master-chrony-configuration             3.5.0                             169m
    100-master-set-core-user-password           3.5.0                             169m
    100-worker-chrony-configuration             3.5.0                             169m
    100-worker-iommu                            3.5.0                             14s
    ```

2.  Verify that IOMMU is enabled at the operating system (OS) level by entering the following command:

    ``` terminal
    $ dmesg | grep -i iommu
    ```

    - If IOMMU is enabled, output is displayed as shown in the following example:

      Example output:

      ``` terminal
      Intel: [ 0.000000] DMAR: Intel(R) IOMMU Driver
      AMD: [ 0.000000] AMD-Vi: IOMMU Initialized
      ```

</div>

## Binding PCI devices to the VFIO driver

To bind PCI devices to the VFIO (Virtual Function I/O) driver, obtain the values for the vendor ID and the device ID from each device and create a list with the values. Add this list to the `MachineConfig` object.

The `MachineConfig` Operator generates the `/etc/modprobe.d/vfio.conf` on the nodes with the PCI devices, and binds the PCI devices to the VFIO driver.

<div>

<div class="title">

Prerequisites

</div>

- You added kernel arguments to enable IOMMU for the CPU.

  > [!NOTE]
  > Enabling IOMMU is not required on `s390x` architecture.

- You have installed the OpenShift CLI (`oc`).

</div>

<div>

<div class="title">

Procedure

</div>

1.  Run the `lspci` command with the name of the GPU accelerator to obtain the vendor ID and the device ID for the PCI device.

    > [!NOTE]
    > NVIDIA GPU is supported on `x86` and `aarch64` architectures, Intel QAT is supported on `x86` architecture, and IBM® Spyre is supported on `s390x` architecture.

    ``` terminal
    $ lspci -nnv | grep -i <gpu_accelerator>
    ```

    Valid values for `<gpu_accelerator>` are `nvidia`, `qat`, and `spyre`.

    Example output:

    ``` terminal
    02:01.0 3D controller [0302]: NVIDIA Corporation GV100GL [Tesla V100 PCIe 32GB] [10de:1eb8] (rev a1)
    ```

2.  Create a Butane config file, `100-worker-vfiopci.bu`, binding the PCI device to the VFIO driver.

    > [!NOTE]
    > The [Butane version](https://coreos.github.io/butane/specs/) you specify in the config file should match the OpenShift Container Platform version and always ends in `0`. For example, `4.22.0`. See "Creating machine configs with Butane" for information about Butane.

    Example:

    ``` yaml
    variant: openshift
    version: 4.22.0
    metadata:
      name: 100-worker-vfiopci
      labels:
        machineconfiguration.openshift.io/role: worker
    storage:
      files:
      - path: /etc/modprobe.d/vfio.conf
        mode: 0644
        overwrite: true
        contents:
          inline: |
            options vfio-pci ids=<vendor_id>:<device_id>
      - path: /etc/modules-load.d/vfio-pci.conf
        mode: 0644
        overwrite: true
        contents:
          inline: vfio-pci
    ```

    - `metadata.labels.machineconfiguration.openshift.io/role: worker` specifies that the new kernel argument is applied only to compute nodes.

    - `storage.files.contents.inline`, where the path is `/etc/modprobe.d/vfio.conf`, specifies the previously determined hexadecimal vendor ID and device ID values to bind a device to the VFIO driver. You can add a list of multiple devices with their vendor and device information.

    - `storage.files.path`, where the `contents.inline` is `vfio-pci`, specifies the file that loads the `vfio-pci` kernel module on the compute nodes.

3.  Use Butane to generate a `MachineConfig` object file, `100-worker-vfiopci.yaml`, containing the configuration to be delivered to the compute nodes:

    ``` terminal
    $ butane 100-worker-vfiopci.bu -o 100-worker-vfiopci.yaml
    ```

4.  Apply the `MachineConfig` object to the compute nodes:

    ``` terminal
    $ oc apply -f 100-worker-vfiopci.yaml
    ```

5.  Verify that the `MachineConfig` object was added.

    ``` terminal
    $ oc get MachineConfig
    ```

    Example output:

    ``` terminal
    NAME                             GENERATEDBYCONTROLLER                      IGNITIONVERSION  AGE
    00-master                        d3da910bfa9f4b599af4ed7f5ac270d55950a3a1   3.5.0            25h
    00-worker                        d3da910bfa9f4b599af4ed7f5ac270d55950a3a1   3.5.0            25h
    01-master-container-runtime      d3da910bfa9f4b599af4ed7f5ac270d55950a3a1   3.5.0            25h
    01-master-kubelet                d3da910bfa9f4b599af4ed7f5ac270d55950a3a1   3.5.0            25h
    01-worker-container-runtime      d3da910bfa9f4b599af4ed7f5ac270d55950a3a1   3.5.0            25h
    01-worker-kubelet                d3da910bfa9f4b599af4ed7f5ac270d55950a3a1   3.5.0            25h
    100-worker-iommu                                                            3.5.0            30s
    100-worker-vfiopci-configuration                                            3.5.0            30s
    ```

</div>

<div>

<div class="title">

Verification

</div>

- Verify that the VFIO driver is loaded.

  ``` terminal
  $ lspci -nnk -d <vendor_id>:
  ```

  The output confirms that the VFIO driver is being used.

  Example output:

      04:00.0 3D controller [0302]: NVIDIA Corporation GP102GL [Tesla P40] [10de:1eb8] (rev a1)
              Subsystem: NVIDIA Corporation Device [10de:1eb8]
              Kernel driver in use: vfio-pci
              Kernel modules: nouveau

</div>

## Exposing PCI host devices in the cluster using the CLI

To expose PCI host devices in the cluster, add details about the PCI devices to the `spec.permittedHostDevices.pciHostDevices` array of the `HyperConverged` custom resource (CR).

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

1.  Edit the `HyperConverged` CR in your default editor by running the following command:

    ``` terminal
    $ oc edit hyperconvergeds.v1beta1.hco.kubevirt.io kubevirt-hyperconverged -n openshift-cnv
    ```

2.  Add the PCI device information to the `spec.permittedHostDevices.pciHostDevices` array.

    Example configuration file:

    ``` yaml
    apiVersion: hco.kubevirt.io/v1beta1
    kind: HyperConverged
    metadata:
      name: kubevirt-hyperconverged
      namespace: openshift-cnv
    spec:
      permittedHostDevices:
        pciHostDevices:
        - pciDeviceSelector: "10DE:1DB6"
          resourceName: "nvidia.com/GV100GL_Tesla_V100"
        - pciDeviceSelector: "10DE:1EB8"
          resourceName: "nvidia.com/TU104GL_Tesla_T4"
        - pciDeviceSelector: "8086:6F54"
          resourceName: "intel.com/qat"
          externalResourceProvider: true
    # ...
    ```

    - `spec.permittedHostDevices` specifies the host devices that are permitted to be used in the cluster.

    - `spec.permittedHostDevices.pciHostDevices` specifies the list of PCI devices available on the node.

    - `spec.permittedHostDevices.pciHostDevices.pciDeviceSelector` specifies the vendor ID and the device ID required to identify the PCI device.

    - `spec.permittedHostDevices.pciHostDevices.resourceName` specifies the name of a PCI host device.

    - `spec.permittedHostDevices.pciHostDevices.externalResourceProvider` is an optional setting. Setting this field to `true` indicates that the resource is provided by an external device plugin. OpenShift Virtualization allows the usage of this device in the cluster but leaves the allocation and monitoring to an external device plugin.

      > [!NOTE]
      > The above example snippet shows two PCI host devices that are named `nvidia.com/GV100GL_Tesla_V100` and `nvidia.com/TU104GL_Tesla_T4` added to the list of permitted host devices in the `HyperConverged` CR. These devices have been tested and verified to work with OpenShift Virtualization.

      Example configuration file for an IBM® Spyre device on `s390x` architecture:

      ``` yaml
      apiVersion: hco.kubevirt.io/v1beta1
      kind: HyperConverged
      metadata:
        name: kubevirt-hyperconverged
        namespace: openshift-cnv
      spec:
        permittedHostDevices:
          pciHostDevices:
          - pciDeviceSelector: "1014:06a8"
            resourceName: "ibm.com/spyre"
      # ...
      ```

3.  Save your changes and exit the editor.

</div>

<div>

<div class="title">

Verification

</div>

- Verify that the PCI host devices were added to the node by running the following command. The example output shows that there is one device each associated with the `nvidia.com/GV100GL_Tesla_V100`, `nvidia.com/TU104GL_Tesla_T4`, and `intel.com/qat` resource names.

  ``` terminal
  $ oc describe node <node_name>
  ```

  Example output:

  ``` terminal
  Capacity:
    cpu:                            64
    devices.kubevirt.io/kvm:        110
    devices.kubevirt.io/tun:        110
    devices.kubevirt.io/vhost-net:  110
    ephemeral-storage:              915128Mi
    hugepages-1Gi:                  0
    hugepages-2Mi:                  0
    memory:                         131395264Ki
    nvidia.com/GV100GL_Tesla_V100   1
    nvidia.com/TU104GL_Tesla_T4     1
    intel.com/qat:                  1
    pods:                           250
  Allocatable:
    cpu:                            63500m
    devices.kubevirt.io/kvm:        110
    devices.kubevirt.io/tun:        110
    devices.kubevirt.io/vhost-net:  110
    ephemeral-storage:              863623130526
    hugepages-1Gi:                  0
    hugepages-2Mi:                  0
    memory:                         130244288Ki
    nvidia.com/GV100GL_Tesla_V100   1
    nvidia.com/TU104GL_Tesla_T4     1
    intel.com/qat:                  1
    pods:                           250
  ```

  > [!NOTE]
  > When using an IBM® Spyre device on `s390x` architecture, the allocated device is shown as follows: `ibm.com/spyre: 1`.

</div>

## Removing PCI host devices from the cluster using the CLI

To remove a PCI host device from the cluster, delete the information for that device from the `HyperConverged` custom resource (CR).

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

1.  Edit the `HyperConverged` CR in your default editor by running the following command:

    ``` terminal
    $ oc edit hyperconvergeds.v1beta1.hco.kubevirt.io kubevirt-hyperconverged -n openshift-cnv
    ```

2.  Remove the PCI device information from the `spec.permittedHostDevices.pciHostDevices` array by deleting the `pciDeviceSelector`, `resourceName` and `externalResourceProvider` (if applicable), fields for the appropriate device. In this example, the user deletes the `nvidia.com/TU104GL_Tesla_T4`.

    Example configuration file:

    ``` yaml
    apiVersion: hco.kubevirt.io/v1beta1
    kind: HyperConverged
    metadata:
      name: kubevirt-hyperconverged
      namespace: openshift-cnv
    spec:
      permittedHostDevices:
        pciHostDevices:
        - pciDeviceSelector: "10DE:1DB6"
          resourceName: "nvidia.com/GV100GL_Tesla_V100"
    # ...
    ```

3.  Save your changes and exit the editor.

</div>

<div>

<div class="title">

Verification

</div>

- Verify that you removed the PCI host device from the node by running the following command. The example output shows that there are zero devices associated with the `nvidia.com/TU104GL_Tesla_T4` resource name.

  ``` terminal
  $ oc describe node <node_name>
  ```

  Example output:

  ``` terminal
  Capacity:
    cpu:                            64
    devices.kubevirt.io/kvm:        110
    devices.kubevirt.io/tun:        110
    devices.kubevirt.io/vhost-net:  110
    ephemeral-storage:              915128Mi
    hugepages-1Gi:                  0
    hugepages-2Mi:                  0
    memory:                         131395264Ki
    nvidia.com/GV100GL_Tesla_V100   1
    nvidia.com/TU104GL_Tesla_T4     0
    pods:                           250
  Allocatable:
    cpu:                            63500m
    devices.kubevirt.io/kvm:        110
    devices.kubevirt.io/tun:        110
    devices.kubevirt.io/vhost-net:  110
    ephemeral-storage:              863623130526
    hugepages-1Gi:                  0
    hugepages-2Mi:                  0
    memory:                         130244288Ki
    nvidia.com/GV100GL_Tesla_V100   1
    nvidia.com/TU104GL_Tesla_T4     0
    pods:                           250
  ```

</div>

# Virtual machine configuration for PCI passthrough

After the PCI devices have been added to the cluster, you can assign them to virtual machines. The PCI devices are now available as if they are physically connected to the virtual machines.

## Assigning a PCI device to a virtual machine

When a PCI device is available in a cluster, you can assign it to a virtual machine and enable PCI passthrough.

<div>

<div class="title">

Procedure

</div>

- Assign the PCI device to a virtual machine as a host device.

  Example:

  ``` yaml
  apiVersion: kubevirt.io/v1
  kind: VirtualMachine
  spec:
    domain:
      devices:
        hostDevices:
        - deviceName: nvidia.com/TU104GL_Tesla_T4
          name: hostdevices1
  ```

  - `spec.template.spec.domain.devices.hostDevices.deviceName` specifies the name of the PCI device that is permitted on the cluster as a host device. The virtual machine can access this host device. When using an IBM® Spyre device on `s390x` architecture, specify `ibm.com/spyre:`.

</div>

<div>

<div class="title">

Verification

</div>

- Use the following command to verify that the host device is available from the virtual machine.

  ``` terminal
  $ lspci -nnk | grep <gpu_accelerator>
  ```

  Valid values for `<gpu_accelerator>` are `nvidia`, `qat`, and `spyre`.

  Example output:

  ``` terminal
  $ 02:01.0 3D controller [0302]: NVIDIA Corporation GV100GL [Tesla V100 PCIe 32GB] [10de:1eb8] (rev a1)
  ```

</div>

# PCI passthrough on IBM Z

On IBM Z® and IBM® LinuxONE, you can configure PCI passthrough for Network Express RoCE adapters and IBM® Internal Shared Memory (ISM) virtual PCI devices. Both use `vfio-pci` to pass devices directly to virtual machines.

## Configure PCI passthrough for Network Express RoCE adapters on IBM Z

On IBM Z® and IBM® LinuxONE, you can configure PCI passthrough for Network Express RoCE adapters by using `vfio-pci`. This procedure applies only when the adapter is configured in RoCE mode through the Hardware Management Console (HMC).

On IBM Z® and IBM® LinuxONE systems, Network Express adapters can be configured in two modes through the HMC:

- **Network Express RoCE**: The adapter is exposed as a PCI virtual function, managed by the `mlx5_core` kernel driver, and can be passed through to VMs by using `vfio-pci`.

- **Network Express OSA**: The adapter uses IBM Z® channel-based I/O (OSH PCI functions). OSH functions are not supported on Linux and are not exposed as PCI devices. Do not configure `vfio-pci` passthrough for adapters in OSA mode.

To use `vfio-pci` for PCI passthrough of RoCE virtual function devices, you must prevent the `mlx5_core` kernel driver from binding to the device. Because `mlx5_core` is included in the initramfs image and loads before the root filesystem is mounted, you must add the driver to a blocklist by using both a `modprobe.d` configuration file and a kernel boot argument. You then bind the device to `vfio-pci` by using a second `MachineConfig`.

<div>

<div class="title">

Prerequisites

</div>

- You have installed OpenShift Container Platform 4.21 or later.

- You have installed the OpenShift Virtualization Operator.

- You have cluster administrator permissions.

- You have installed the Butane tool for generating Ignition-compatible `MachineConfig` manifests.

- The Network Express adapter is configured in RoCE mode through the HMC.

- You have installed the OpenShift CLI (`oc`).

</div>

<div>

<div class="title">

Procedure

</div>

1.  On each node, identify the RoCE virtual function PCI address and vendor ID by running the following command:

    ``` terminal
    $ lspci | grep -i mellanox
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    0000:00:00.0 Ethernet controller: Mellanox Technologies ConnectX Family mlx5Gen Virtual Function [15b3:101e]
    ```

    </div>

    Record the combined PCI vendor and device ID `15b3:101e`. This value is used in the `vfio-pci` and `HyperConverged` configuration.

2.  Create a Butane configuration file named `machine-config-roce.bu` to add the `mlx5_core` driver to the blocklist:

    ``` yaml
    variant: openshift
    version: 4.22.0
    metadata:
      name: 100-worker-blocklist-mlx5
      labels:
        machineconfiguration.openshift.io/role: master
    storage:
      files:
        - path: /etc/modprobe.d/blocklist-mlx5.conf
          mode: 0644
          overwrite: true
          contents:
            inline: |
              blocklist mlx5_core
    openshift:
      kernel_arguments:
        - rd.driver.blacklist=mlx5_core
    ```

    > [!NOTE]
    > The `rd.driver.blacklist=mlx5_core` kernel argument is required in addition to the `modprobe.d` blocklist entry because `mlx5_core` is included in the initramfs image and loads before `/etc/modprobe.d/` is accessible. The kernel argument blocks the driver at the initramfs stage.

3.  Convert the Butane file to a `MachineConfig` manifest by running the following command:

    ``` terminal
    $ butane machine-config-roce.bu --output machine-config-roce.yaml
    ```

4.  Apply the `MachineConfig` to the cluster by running the following command:

    ``` terminal
    $ oc apply -f machine-config-roce.yaml
    ```

5.  Watch the `MachineConfig` rollout and wait for completion before proceeding:

    ``` terminal
    $ oc get mcp master -w
    ```

6.  Create a Butane configuration file named `machine-config-roce1.bu` to bind RoCE devices to `vfio-pci`:

    ``` yaml
    variant: openshift
    version: 4.22.0
    metadata:
      name: 100-worker-vfiopci
      labels:
        machineconfiguration.openshift.io/role: master
    storage:
      files:
        - path: /etc/modprobe.d/vfio.conf
          mode: 0644
          overwrite: true
          contents:
            inline: |
              options vfio-pci ids=15b3:101e
        - path: /etc/modules-load.d/vfio-pci.conf
          mode: 0644
          overwrite: true
          contents:
            inline: vfio-pci
    ```

7.  Convert the Butane file to a `MachineConfig` manifest by running the following command:

    ``` terminal
    $ butane machine-config-roce1.bu --output machine-config-roce1.yaml
    ```

8.  Apply the `MachineConfig` to the cluster by running the following command:

    ``` terminal
    $ oc apply -f machine-config-roce1.yaml
    ```

9.  Watch the `MachineConfig` rollout and wait for completion before proceeding:

    ``` terminal
    $ oc get mcp master -w
    ```

10. Edit the `HyperConverged` custom resource to expose the RoCE device:

    ``` terminal
    $ oc edit hyperconverged kubevirt-hyperconverged -n openshift-cnv
    ```

    Add the device under `spec.virtualization.permittedHostDevices`:

    ``` yaml
    spec:
      virtualization:
        permittedHostDevices:
          pciHostDevices:
            - pciDeviceSelector: "15b3:101e"
              resourceName: ibm.com/roce_vf
    ```

11. Add a `hostDevices` entry to the `VirtualMachine` manifest:

    ``` yaml
    apiVersion: kubevirt.io/v1
    kind: VirtualMachine
    metadata:
      name: <vm_name>
      namespace: <namespace>
    spec:
      template:
        spec:
          domain:
            devices:
              hostDevices:
                - deviceName: ibm.com/roce_vf
                  name: hostdevices1
    ```

12. Apply the `VirtualMachine` manifest by running the following command:

    ``` terminal
    $ oc apply -f <vm_manifest>.yaml
    ```

</div>

<div>

<div class="title">

Verification

</div>

1.  Verify `vfio-pci` binding on the nodes by running the following command:

    ``` terminal
    $ lspci -nnk | grep -A 3 "15b3:101e"
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    0000:00:00.0 Ethernet controller [0200]: Mellanox Technologies ConnectX Family mlx5Gen Virtual Function [15b3:101e]
            Subsystem: Mellanox Technologies Device [15b3:0002]
            Kernel driver in use: vfio-pci
            Kernel modules: mlx5_core
    ```

    </div>

    The `Kernel driver in use: vfio-pci` line confirms that the device is bound to `vfio-pci` on the host.

2.  Verify that the RoCE device is present inside the VM by running the following command:

    ``` terminal
    $ lspci -nnk | grep -A 3 "15b3:101e"
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    0001:00:00.0 Ethernet controller [0200]: Mellanox Technologies ConnectX Family mlx5Gen Virtual Function [15b3:101e]
            Subsystem: Mellanox Technologies Device [15b3:0002]
            Kernel driver in use: mlx5_core
            Kernel modules: mlx5_core
    ```

    </div>

    > [!NOTE]
    > Inside the VM, the RoCE device is managed by the guest kernel’s own `mlx5_core` driver. The host uses `vfio-pci` to pass the device through. The guest uses its native driver to operate it.

</div>

## Configure PCI passthrough for IBM ISM virtual PCI devices on IBM Z

On IBM Z® and IBM® LinuxONE, IBM® Internal Shared Memory (ISM) devices are exposed as virtual PCI devices. You can configure PCI passthrough for ISM devices by binding the device to the `vfio-pci` driver by using a single `MachineConfig`.

Unlike RoCE passthrough, which requires two separate `MachineConfig` objects to blocklist `mlx5_core` and bind `vfio-pci`, ISM passthrough requires only a single `MachineConfig`. The `ism` kernel module does not load during initramfs, so a `softdep` directive combined with kernel boot arguments is enough to ensure `vfio-pci` claims the device before `ism`.

> [!NOTE]
> The `softdep` directive ensures `vfio-pci` loads before the `ism` module without completely blocking `ism` from the host. The `ism` module remains available in the kernel but does not own the ISM device.

<div>

<div class="title">

Prerequisites

</div>

- You have installed OpenShift Container Platform 4.21 or later.

- You have installed the OpenShift Virtualization Operator.

- You have cluster administrator permissions.

- You have installed the Butane tool for generating Ignition-compatible `MachineConfig` manifests.

- The ISM virtual PCI device is present and visible on the PCI bus of the target nodes.

- You have installed the OpenShift CLI (`oc`).

</div>

<div>

<div class="title">

Procedure

</div>

1.  On each node, confirm the ISM device is displayed as a PCI device by running the following command:

    ``` terminal
    $ lspci | grep -i ism
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    0004:00:00.0 Non-VGA unclassified device: IBM Internal Shared Memory (ISM) virtual PCI device
    ```

    </div>

2.  Retrieve the PCI vendor and device ID by running the following command:

    ``` terminal
    $ lspci -n -s 0004:00:00.0
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    0004:00:00.0 0000: 1014:04ed
    ```

    </div>

    Record the combined PCI vendor and device ID `1014:04ed`. This value is used in the `vfio-pci` and `HyperConverged` configuration.

3.  Create a Butane configuration file named `100-master-vfio-ism.bu` to bind the ISM device to `vfio-pci`:

    ``` yaml
    variant: openshift
    version: 4.22.0
    metadata:
      name: 100-master-vfio-ism
      labels:
        machineconfiguration.openshift.io/role: master
    storage:
      files:
        - path: /etc/modprobe.d/vfio-ism.conf
          mode: 0644
          overwrite: true
          contents:
            inline: |
              softdep ism pre: vfio-pci
              options vfio-pci ids=1014:04ed
    openshift:
      kernel_arguments:
        - rd.driver.pre=vfio-pci
        - vfio-pci.ids=1014:04ed
    ```

    where:

    `storage.files[].contents.inline softdep ism pre: vfio-pci`
    Specifies that `vfio-pci` must load before the `ism` module. The `ism` module remains available on the host but does not own the device.

    `storage.files[].contents.inline options vfio-pci ids=1014:04ed`
    Specifies that `vfio-pci` claims devices with this PCI vendor and device ID.

    `openshift.kernel_arguments rd.driver.pre=vfio-pci`
    Specifies that `vfio-pci` loads during initramfs before any other driver.

    `openshift.kernel_arguments vfio-pci.ids=1014:04ed`
    Specifies the PCI device ID passed directly to `vfio-pci` at boot time.

4.  Convert the Butane file to a `MachineConfig` manifest by running the following command:

    ``` terminal
    $ butane 100-master-vfio-ism.bu -o 100-master-vfio-ism.yaml
    ```

5.  Apply the `MachineConfig` to the cluster by running the following command:

    ``` terminal
    $ oc apply -f 100-master-vfio-ism.yaml
    ```

6.  Watch the `MachineConfig` rollout and wait for completion before proceeding:

    ``` terminal
    $ oc get mcp master -w
    ```

    <div class="formalpara">

    <div class="title">

    Example output when complete

    </div>

    ``` terminal
    NAME     CONFIG                                             UPDATED   UPDATING   DEGRADED   MACHINECOUNT   READYMACHINECOUNT   UPDATEDMACHINECOUNT   DEGRADEDMACHINECOUNT   AGE
    master   rendered-master-3fb080e65525e49079d4b34e122fb64c   True      False      False      3              3                   3                     0                      27d
    ```

    </div>

7.  Confirm the ISM device resource is visible and allocatable on the nodes by running the following command:

    ``` terminal
    $ oc describe nodes | grep ibm.com/ism
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
      ibm.com/ism:    1
      ibm.com/ism:    1
    ```

    </div>

8.  Edit the `HyperConverged` custom resource to expose the ISM device by running the following command:

    ``` terminal
    $ oc edit hyperconverged kubevirt-hyperconverged -n openshift-cnv
    ```

    Add the ISM device under `spec.virtualization.permittedHostDevices`:

    ``` yaml
    spec:
      virtualization:
        permittedHostDevices:
          pciHostDevices:
            - pciDeviceSelector: "1014:04ed"
              resourceName: ibm.com/ism
    ```

9.  Verify the HyperConverged Operator accepted the configuration by running the following command:

    ``` terminal
    $ oc get hyperconverged kubevirt-hyperconverged \
      -n openshift-cnv -o json | jq '.spec.virtualization.permittedHostDevices'
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    {
      "pciHostDevices": [
        {
          "pciDeviceSelector": "1014:04ed",
          "resourceName": "ibm.com/ism"
        }
      ]
    }
    ```

    </div>

10. Add the ISM device to a `VirtualMachine` manifest:

    ``` yaml
    apiVersion: kubevirt.io/v1
    kind: VirtualMachine
    metadata:
      name: <vm_name>
      namespace: <namespace>
    spec:
      running: true
      template:
        spec:
          domain:
            devices:
              hostDevices:
                - deviceName: ibm.com/ism
                  name: ism-device
            resources:
              requests:
                memory: 1Gi
    ```

11. Apply the `VirtualMachine` manifest by running the following command:

    ``` terminal
    $ oc apply -f <vm_manifest>.yaml
    ```

</div>

<div>

<div class="title">

Verification

</div>

1.  Verify `vfio-pci` binding on all control plane nodes by running the following command:

    ``` terminal
    $ for node in $(oc get nodes -l node-role.kubernetes.io/master -o name); do
      echo "=== $node ==="
      oc debug $node -- chroot /host bash -c \
        "lspci -nnk | grep -A2 'ISM\|1014:04ed'" 2>/dev/null
    done
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    === node/master-0 ===
    0000:00:00.0 Non-VGA unclassified device [0000]: IBM Internal Shared Memory (ISM) virtual PCI device [1014:04ed]
            Kernel driver in use: vfio-pci
            Kernel modules: ism
    === node/master-1 ===
    0000:00:00.0 Non-VGA unclassified device [0000]: IBM Internal Shared Memory (ISM) virtual PCI device [1014:04ed]
            Kernel driver in use: vfio-pci
            Kernel modules: ism
    === node/master-2 ===
    0000:00:00.0 Non-VGA unclassified device [0000]: IBM Internal Shared Memory (ISM) virtual PCI device [1014:04ed]
            Kernel driver in use: vfio-pci
            Kernel modules: ism
    ```

    </div>

    `Kernel modules: ism` indicates the `ism` module is available in the kernel but is not actively managing the device. `vfio-pci` owns the device.

2.  Verify the ISM device is present inside the VM by connecting to the VM console and running the following command:

    ``` terminal
    $ lspci -nnk | grep -i ism
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    0001:00:00.0 Non-VGA unclassified device: IBM Internal Shared Memory (ISM) virtual PCI device
    ```

    </div>

    The output confirms PCI passthrough. The guest binds the `ism` driver only if the guest image includes that module.

</div>

# Additional resources

- [Enabling Intel VT-X and AMD-V Virtualization Hardware Extensions in BIOS](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/virtualization_deployment_and_administration_guide/sect-troubleshooting-enabling_intel_vt_x_and_amd_v_virtualization_hardware_extensions_in_bios)

- [Managing file permissions](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8/html/configuring_basic_system_settings/assembly_managing-file-permissions_configuring-basic-system-settings)

- [Machine Config Overview](../../../machine_configuration/index.md#machine-config-overview)

- [IBM® Spyre Accelerator User’s Guide](https://www.ibm.com/docs/en/systems-hardware/linuxone/9175-ML1?topic=library-spyre-accelerator-users-guide)

- [Network adapters as of IBM® z17 and IBM® LinuxONE 5](https://www.ibm.com/docs/en/linux-on-systems?topic=networking-pci-network-adapters)
