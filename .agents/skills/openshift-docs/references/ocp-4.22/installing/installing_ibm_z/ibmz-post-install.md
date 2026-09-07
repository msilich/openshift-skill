<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

After installing OpenShift Container Platform, you can configure additional devices for your cluster in an IBM Z® or IBM® LinuxONE environment, which is installed with z/VM.

The following devices can be configured:

- Fibre Channel Protocol (FCP) host

- FCP LUN

- DASD

- qeth

You can configure devices by adding udev rules by using the Machine Config Operator (MCO) or you can configure devices manually.

> [!NOTE]
> The procedures described here apply only to z/VM installations. If you have installed your cluster with RHEL KVM on IBM Z® or IBM® LinuxONE infrastructure, no additional configuration is needed inside the KVM guest after the devices were added to the KVM guests. However, both in z/VM and RHEL KVM environments the next steps to configure the Local Storage Operator and Kubernetes NMState Operator need to be applied.

<div>

<div class="title">

Additional resources

</div>

- [Machine configuration overview](../../machine_configuration/index.md#machine-config-overview)

</div>

# Configuring additional devices by using the Machine Config Operator

You can use the Machine Config Operator (MCO) to configure additional devices in an IBM Z® or IBM® LinuxONE environment. Configuring devices with the MCO is persistent but only allows specific configurations for compute nodes. MCO does not allow control plane nodes to have different configurations.

<div>

<div class="title">

Prerequisites

</div>

- You are logged in to the cluster as a user with administrative privileges.

- The device must be available to the z/VM guest.

- The device is already attached.

- The device is not included in the `cio_ignore` list, which can be set in the kernel parameters.

- You have created a `MachineConfig` object file with the following YAML:

  ``` yaml
  apiVersion: machineconfiguration.openshift.io/v1
  kind: MachineConfigPool
  metadata:
    name: worker0
  spec:
    machineConfigSelector:
      matchExpressions:
        - {key: machineconfiguration.openshift.io/role, operator: In, values: [worker,worker0]}
    nodeSelector:
      matchLabels:
        node-role.kubernetes.io/worker0: ""
  ```

</div>

<div>

<div class="title">

Procedure

</div>

1.  To configure an FCP host adapter with N_Port Identifier Virtualization (NPIV) by adding a udev rule, complete the following steps:

    1.  Take the following sample udev rule `441-zfcp-host-0.0.8000.rules`:

        ``` terminal
        ACTION=="add", SUBSYSTEM=="ccw", KERNEL=="0.0.8000", DRIVER=="zfcp", GOTO="cfg_zfcp_host_0.0.8000"
        ACTION=="add", SUBSYSTEM=="drivers", KERNEL=="zfcp", TEST=="[ccw/0.0.8000]", GOTO="cfg_zfcp_host_0.0.8000"
        GOTO="end_zfcp_host_0.0.8000"

        LABEL="cfg_zfcp_host_0.0.8000"
        ATTR{[ccw/0.0.8000]online}="1"

        LABEL="end_zfcp_host_0.0.8000"
        ```

    2.  Convert the rule to Base64 encoded by running the following command:

        ``` terminal
        $ base64 /path/to/file/
        ```

    3.  Copy the following MCO sample profile into a YAML file:

        ``` yaml
        apiVersion: machineconfiguration.openshift.io/v1
        kind: MachineConfig
        metadata:
           labels:
             machineconfiguration.openshift.io/role: worker0
           name: 99-worker0-devices
        spec:
           config:
             ignition:
               version: 3.2.0
             storage:
               files:
               - contents:
                   source: <base64_data_uri>
                 filesystem: root
                 mode: 420
                 path: /etc/udev/rules.d/41-zfcp-host-0.0.8000.rules
        ```

        where:

        `metadata.labels.machineconfiguration.openshift.io/role`
        Specifies the role you have defined in the machine config file.

        `spec.config.storage.files.contents.source`
        Specifies the data URI for the Base64 encoded udev rule. The value is the Base64 encoded string that you generated in the previous step, formatted as an Ignition data URI.

        `spec.config.storage.files.path`
        Specifies the path where the udev rule is located.

2.  To configure an FCP LUN by adding a udev rule, complete the following steps. You can add new FCP LUNs or add additional paths to LUNs that are already configured with multipathing.

    1.  Take the following sample udev rule `41-zfcp-lun-0.0.8000:0x500507680d760026:0x00bc000000000000.rules`:

        ``` terminal
        ACTION=="add", SUBSYSTEMS=="ccw", KERNELS=="0.0.8000", GOTO="start_zfcp_lun_0.0.8207"
        GOTO="end_zfcp_lun_0.0.8000"

        LABEL="start_zfcp_lun_0.0.8000"
        SUBSYSTEM=="fc_remote_ports", ATTR{port_name}=="0x500507680d760026", GOTO="cfg_fc_0.0.8000_0x500507680d760026"
        GOTO="end_zfcp_lun_0.0.8000"

        LABEL="cfg_fc_0.0.8000_0x500507680d760026"
        ATTR{[ccw/0.0.8000]0x500507680d760026/unit_add}="0x00bc000000000000"
        GOTO="end_zfcp_lun_0.0.8000"

        LABEL="end_zfcp_lun_0.0.8000"
        ```

    2.  Convert the rule to Base64 encoded by running the following command:

        ``` terminal
        $ base64 /path/to/file/
        ```

    3.  Copy the following MCO sample profile into a YAML file:

        ``` yaml
        apiVersion: machineconfiguration.openshift.io/v1
        kind: MachineConfig
        metadata:
           labels:
             machineconfiguration.openshift.io/role: worker0
           name: 99-worker0-devices
        spec:
           config:
             ignition:
               version: 3.2.0
             storage:
               files:
               - contents:
                   source: <base64_data_uri>
                 filesystem: root
                 mode: 420
                 path: /etc/udev/rules.d/41-zfcp-lun-0.0.8000:0x500507680d760026:0x00bc000000000000.rules
        ```

        where:

        `metadata.labels.machineconfiguration.openshift.io/role`
        Specifies the role you have defined in the machine config file.

        `spec.config.storage.files.contents.source`
        Specifies the data URI for the Base64 encoded udev rule. The value is the Base64 encoded string that you generated in the previous step, formatted as an Ignition data URI.

        `spec.config.storage.files.path`
        Specifies the path where the udev rule is located.

3.  To configure a DASD device by adding a udev rule, complete the following steps:

    1.  Take the following sample udev rule `41-dasd-eckd-0.0.4444.rules`:

        ``` terminal
        ACTION=="add", SUBSYSTEM=="ccw", KERNEL=="0.0.4444", DRIVER=="dasd-eckd", GOTO="cfg_dasd_eckd_0.0.4444"
        ACTION=="add", SUBSYSTEM=="drivers", KERNEL=="dasd-eckd", TEST=="[ccw/0.0.4444]", GOTO="cfg_dasd_eckd_0.0.4444"
        GOTO="end_dasd_eckd_0.0.4444"

        LABEL="cfg_dasd_eckd_0.0.4444"
        ATTR{[ccw/0.0.4444]online}="1"

        LABEL="end_dasd_eckd_0.0.4444"
        ```

    2.  Convert the rule to Base64 encoded by running the following command:

        ``` terminal
        $ base64 /path/to/file/
        ```

    3.  Copy the following MCO sample profile into a YAML file:

        ``` yaml
        apiVersion: machineconfiguration.openshift.io/v1
        kind: MachineConfig
        metadata:
           labels:
             machineconfiguration.openshift.io/role: worker0
           name: 99-worker0-devices
        spec:
           config:
             ignition:
               version: 3.2.0
             storage:
               files:
               - contents:
                   source: <base64_data_uri>
                 filesystem: root
                 mode: 420
                 path: /etc/udev/rules.d/41-dasd-eckd-0.0.4444.rules
        ```

        where:

        `metadata.labels.machineconfiguration.openshift.io/role`
        Specifies the role you have defined in the machine config file.

        `spec.config.storage.files.contents.source`
        Specifies the data URI for the Base64 encoded udev rule. The value is the Base64 encoded string that you generated in the previous step, formatted as an Ignition data URI.

        `spec.config.storage.files.path`
        Specifies the path where the udev rule is located.

4.  To configure a qeth device by adding a udev rule, complete the following steps:

    1.  Take the following sample udev rule `41-qeth-0.0.1000.rules`:

        ``` terminal
        ACTION=="add", SUBSYSTEM=="drivers", KERNEL=="qeth", GOTO="group_qeth_0.0.1000"
        ACTION=="add", SUBSYSTEM=="ccw", KERNEL=="0.0.1000", DRIVER=="qeth", GOTO="group_qeth_0.0.1000"
        ACTION=="add", SUBSYSTEM=="ccw", KERNEL=="0.0.1001", DRIVER=="qeth", GOTO="group_qeth_0.0.1000"
        ACTION=="add", SUBSYSTEM=="ccw", KERNEL=="0.0.1002", DRIVER=="qeth", GOTO="group_qeth_0.0.1000"
        ACTION=="add", SUBSYSTEM=="ccwgroup", KERNEL=="0.0.1000", DRIVER=="qeth", GOTO="cfg_qeth_0.0.1000"
        GOTO="end_qeth_0.0.1000"

        LABEL="group_qeth_0.0.1000"
        TEST=="[ccwgroup/0.0.1000]", GOTO="end_qeth_0.0.1000"
        TEST!="[ccw/0.0.1000]", GOTO="end_qeth_0.0.1000"
        TEST!="[ccw/0.0.1001]", GOTO="end_qeth_0.0.1000"
        TEST!="[ccw/0.0.1002]", GOTO="end_qeth_0.0.1000"
        ATTR{[drivers/ccwgroup:qeth]group}="0.0.1000,0.0.1001,0.0.1002"
        GOTO="end_qeth_0.0.1000"

        LABEL="cfg_qeth_0.0.1000"
        ATTR{[ccwgroup/0.0.1000]online}="1"

        LABEL="end_qeth_0.0.1000"
        ```

    2.  Convert the rule to Base64 encoded by running the following command:

        ``` terminal
        $ base64 /path/to/file/
        ```

    3.  Copy the following MCO sample profile into a YAML file:

        ``` yaml
        apiVersion: machineconfiguration.openshift.io/v1
        kind: MachineConfig
        metadata:
           labels:
             machineconfiguration.openshift.io/role: worker0
           name: 99-worker0-devices
        spec:
           config:
             ignition:
               version: 3.2.0
             storage:
               files:
               - contents:
                   source: <base64_data_uri>
                 filesystem: root
                 mode: 420
                 path: /etc/udev/rules.d/41-dasd-eckd-0.0.4444.rules
        ```

        where:

        `metadata.labels.machineconfiguration.openshift.io/role`
        Specifies the role you have defined in the machine config file.

        `spec.config.storage.files.contents.source`
        Specifies the data URI for the Base64 encoded udev rule. The value is the Base64 encoded string that you generated in the previous step, formatted as an Ignition data URI.

        `spec.config.storage.files.path`
        Specifies the path where the udev rule is located.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Install and configure the Local Storage Operator](../../storage/persistent_storage_local/persistent-storage-local.md#persistent-storage-using-local-volume)

- [Observing and updating the node network state and configuration](../../networking/k8s_nmstate/k8s-nmstate-updating-node-network-config.md#k8s-nmstate-updating-node-network-config)

</div>

# Configuring additional devices manually

After installation, you can manually configure additional devices on IBM Z® or IBM® LinuxONE nodes. This configuration persists across node restarts, but you must redo the steps if you replace the node.

<div>

<div class="title">

Prerequisites

</div>

- You are logged in to the cluster as a user with administrative privileges.

- The device must be available to the node.

- In a z/VM environment, the device must be attached to the z/VM guest.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Connect to the node via SSH by running the following command:

    ``` terminal
    $ ssh <user>@<node_ip_address>
    ```

    You can also start a debug session to the node by running the following command:

    ``` terminal
    $ oc debug node/<node_name>
    ```

2.  To enable the devices with the `chzdev` command, enter the following command:

    ``` terminal
    $ sudo chzdev -e <device>
    ```

</div>

<div>

<div class="title">

Additional resources

</div>

- [chzdev - Configure IBM Z® devices (IBM® Documentation)](https://www.ibm.com/docs/en/linux-on-systems?topic=commands-chzdev)

- [Persistent device configuration (IBM® Documentation)](https://www.ibm.com/docs/en/linux-on-systems?topic=linuxonibm/com.ibm.linux.z.ludd/ludd_c_perscfg.html)

</div>

# RoCE network cards

You can configure RoCE (RDMA over Converged Ethernet) interfaces with the Kubernetes NMState Operator when RoCE network cards are available on a node. For example, the cards are available if they are attached in a z/VM environment or passed through in a RHEL KVM environment.

# Enabling multipathing for FCP LUNs

After installation, you can enable multipathing for Fibre Channel Protocol (FCP) logical unit numbers (LUNs) on IBM Z® or IBM® LinuxONE nodes. This configuration persists across node restarts, but you must redo the steps if you replace the node.

> [!IMPORTANT]
> On IBM Z® and IBM® LinuxONE, you can enable multipathing only if you configured your cluster for it during installation. For more information, see "Installing RHCOS and starting the OpenShift Container Platform bootstrap process" in *Installing a cluster with z/VM on IBM Z® and IBM® LinuxONE*.

<div>

<div class="title">

Prerequisites

</div>

- You are logged in to the cluster as a user with administrative privileges.

- You have configured multiple paths to a LUN with either method explained above.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Connect to the node via SSH by running the following command:

    ``` terminal
    $ ssh <user>@<node_ip_address>
    ```

    You can also start a debug session to the node by running the following command:

    ``` terminal
    $ oc debug node/<node_name>
    ```

2.  To enable multipathing, run the following command:

    ``` terminal
    $ sudo /sbin/mpathconf --enable
    ```

3.  To start the `multipathd` daemon, run the following command:

    ``` terminal
    $ sudo multipath
    ```

4.  Optional: To format your multipath device with fdisk, run the following command:

    ``` terminal
    $ sudo fdisk /dev/mapper/mpatha
    ```

</div>

<div>

<div class="title">

Verification

</div>

- To verify that the devices have been grouped, run the following command:

  ``` terminal
  $ sudo multipath -ll
  ```

  For example:

  ``` terminal
  mpatha (20017380030290197) dm-1 IBM,2810XIV
     size=512G features='1 queue_if_no_path' hwhandler='1 alua' wp=rw
      -+- policy='service-time 0' prio=50 status=enabled
      |- 1:0:0:6  sde 68:16  active ready running
      |- 1:0:1:6  sdf 69:24  active ready running
      |- 0:0:0:6  sdg  8:80  active ready running
      `- 0:0:1:6  sdh 66:48  active ready running
  ```

</div>

<div>

<div class="title">

Additional resources

</div>

- [Install and configure the Local Storage Operator](../../storage/persistent_storage_local/persistent-storage-local.md#persistent-storage-using-local-volume)

- [Observing and updating the node network state and configuration](../../networking/k8s_nmstate/k8s-nmstate-updating-node-network-config.md#k8s-nmstate-updating-node-network-config)

</div>
