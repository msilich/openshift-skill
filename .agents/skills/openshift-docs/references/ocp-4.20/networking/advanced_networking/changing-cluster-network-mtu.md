<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

As a cluster administrator, you can change the maximum transmission unit (MTU) for the cluster network after cluster installation. This change is disruptive as cluster nodes must be rebooted to finalize the MTU change.

# About the cluster MTU

During installation, the cluster network maximum transmission unit (MTU) is set automatically based on the primary network interface MTU of cluster nodes. Typically, you do not need to override the detected MTU, but in some instances you must override it.

You might want to change the MTU of the cluster network for one of the following reasons:

- The MTU detected during cluster installation is not correct for your infrastructure.

- Your cluster infrastructure now requires a different MTU, such as from the addition of nodes that need a different MTU for optimal performance.

Only the OVN-Kubernetes network plugin supports changing the MTU value.

## Service interruption considerations

When you initiate a maximum transmission unit (MTU) change on your cluster the following effects might impact service availability:

- At least two rolling reboots are required to complete the migration to a new MTU. During this time, some nodes are not available as they restart.

- Specific applications deployed to the cluster with shorter timeout intervals than the absolute TCP timeout interval might experience disruption during the MTU change.

## MTU value selection

When planning your maximum transmission unit (MTU) migration there are two related but distinct MTU values to consider.

- **Hardware MTU**: This MTU value is set based on the specifics of your network infrastructure.

- **Cluster network MTU**: This MTU value is always less than your hardware MTU to account for the cluster network overlay overhead. The specific overhead is determined by your network plugin. For OVN-Kubernetes, the overhead is `100` bytes.

If your cluster requires different MTU values for different nodes, you must subtract the overhead value for your network plugin from the lowest MTU value that is used by any node in your cluster. For example, if some nodes in your cluster have an MTU of `9001`, and some have an MTU of `1500`, you must set this value to `1400`.

> [!IMPORTANT]
> To avoid selecting an MTU value that is not acceptable by a node, verify the maximum MTU value (`maxmtu`) that is accepted by the network interface by using the `ip -d link` command.

## How the migration process works

The following table summarizes the migration process by segmenting between the user-initiated steps in the process and the actions that the migration performs in response.

<table>
<caption>Live migration of the cluster MTU</caption>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">User-initiated steps</th>
<th style="text-align: left;">OpenShift Container Platform activity</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>Set the following values in the Cluster Network Operator configuration:</p>
<ul>
<li><p><code>spec.migration.mtu.machine.to</code></p></li>
<li><p><code>spec.migration.mtu.network.from</code></p></li>
<li><p><code>spec.migration.mtu.network.to</code></p></li>
</ul></td>
<td style="text-align: left;"><p><strong>Cluster Network Operator (CNO)</strong>: Confirms that each field is set to a valid value.</p>
<ul>
<li><p>The <code>mtu.machine.to</code> must be set to either the new hardware MTU or to the current hardware MTU if the MTU for the hardware is not changing. This value is transient and is used as part of the migration process. If you set a hardware MTU different from the current value, you must manually configure it to persist. Use methods such as a machine config, DHCP setting, or kernel command line.</p></li>
<li><p>The <code>mtu.network.from</code> field must equal the <code>network.status.clusterNetworkMTU</code> field, which is the current MTU of the cluster network.</p></li>
<li><p>The <code>mtu.network.to</code> field must be set to the target cluster network MTU. It must be lower than the hardware MTU to allow for the overlay overhead of the network plugin. For OVN-Kubernetes, the overhead is <code>100</code> bytes.</p></li>
</ul>
<p>If the values provided are valid, the CNO writes out a new temporary configuration with the MTU for the cluster network set to the value of the <code>mtu.network.to</code> field.</p>
<p><strong>Machine Config Operator (MCO)</strong>: Performs a rolling reboot of each node in the cluster.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Reconfigure the MTU of the primary network interface for the nodes on the cluster. You can use one of the following methods to accomplish this:</p>
<ul>
<li><p>Deploying a new NetworkManager connection profile with the MTU change</p></li>
<li><p>Changing the MTU through a DHCP server setting</p></li>
<li><p>Changing the MTU through boot parameters</p></li>
</ul></td>
<td style="text-align: left;"><p>N/A</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Set the <code>mtu</code> value in the CNO configuration for the network plugin and set <code>spec.migration</code> to <code>null</code>.</p></td>
<td style="text-align: left;"><p><strong>Machine Config Operator (MCO)</strong>: Performs a rolling reboot of each node in the cluster with the new MTU configuration.</p></td>
</tr>
</tbody>
</table>

# Changing the cluster network MTU

As a cluster administrator, you can increase or decrease the maximum transmission unit (MTU) for your cluster.

> [!IMPORTANT]
> You cannot roll back an MTU value for nodes during the MTU migration process, but you can roll back the value after the MTU migration process completes.
>
> The migration is disruptive and nodes in your cluster might be temporarily unavailable as the MTU update takes effect.

The following procedures describe how to change the cluster network MTU by using machine configs, Dynamic Host Configuration Protocol (DHCP), or an ISO image. If you use either the DHCP or ISO approaches, you must refer to configuration artifacts that you kept after installing your cluster to complete the procedure.

<div>

<div class="title">

Prerequisites

</div>

- You have installed the OpenShift CLI (`oc`).

- You have access to the cluster using an account with `cluster-admin` permissions.

- You have identified the target MTU for your cluster. The MTU for the OVN-Kubernetes network plugin must be set to `100` less than the lowest hardware MTU value in your cluster.

- If your nodes are physical machines, ensure that the cluster network and the connected network switches support jumbo frames.

- If your nodes are virtual machines (VMs), ensure that the hypervisor and the connected network switches support jumbo frames.

</div>

## Checking the current cluster MTU value

To ensure network stability and performance in a hybrid environment where part of your cluster is in the cloud and part is an on-premise environment, you can obtain the current maximum transmission unit (MTU) for the cluster network.

<div>

<div class="title">

Procedure

</div>

- To obtain the current MTU for the cluster network, enter the following command:

  ``` terminal
  $ oc describe network.config cluster
  ```

  <div class="formalpara">

  <div class="title">

  Example output

  </div>

  ``` text
  ...
  Status:
    Cluster Network:
      Cidr:               10.217.0.0/22
      Host Prefix:        23
    Cluster Network MTU:  1400
    Network Type:         OVNKubernetes
    Service Network:
      10.217.4.0/23
  ...
  ```

  </div>

</div>

## Preparing your hardware MTU configuration

To maintain network stability during an MTU change, you must prepare the configuration for your underlying hardware using a method such as DHCP, PXE, or NetworkManager. This preparation ensures that all cluster nodes are ready to accept the new MTU value before you apply the changes to the cluster network.

<div>

<div class="title">

Procedure

</div>

- Prepare your configuration for the hardware MTU:

  - If your hardware MTU is specified with DHCP, update your DHCP configuration such as with the following dnsmasq configuration:

    ``` text
    dhcp-option-force=26,<mtu>
    ```

    where:

    `<mtu>`
    Specifies the hardware MTU for the DHCP server to advertise.

  - If your hardware MTU is specified with a kernel command line with PXE, update that configuration accordingly.

  - If your hardware MTU is specified in a NetworkManager connection configuration, complete the following steps. This approach is the default for OpenShift Container Platform if you do not explicitly specify your network configuration with DHCP, a kernel command line, or some other method. Your cluster nodes must all use the same underlying network configuration for the following procedure to work unmodified.

    Find the primary network interface by entering the following command:

    ``` terminal
    $ oc debug node/<node_name> -- chroot /host nmcli -g connection.interface-name c show ovs-if-phys0
    ```

    where:

    `<node_name>`
    Specifies the name of a node in your cluster.

    Create the following `NetworkManager` configuration in the `<interface>-mtu.conf` file:

    ``` ini
    [connection-<interface>-mtu]
    match-device=interface-name:<interface>
    ethernet.mtu=<mtu>
    ```

    where:

    `<interface>`
    Specifies the primary network interface name.

    `<mtu>`
    Specifies the new hardware MTU value.

    If you used Kubernetes NMState to configure the `br-ex` bridge, use the Kubernetes NMState Operator to update the MTU for the `br-ex` bridge. Changing the MTU for this bridge in a `.nmconnection` file could lead to persistence issues as the Machine Config Operator (MCO) might overwrite the file.

</div>

## Creating MachineConfig objects

To prepare your nodes for a hardware MTU change, you must create `MachineConfig` objects for both control plane and compute nodes. Creating these objects ensures that the updated network interface settings are ready for deployment without causing immediate cluster instability.

<div>

<div class="title">

Procedure

</div>

1.  Create two `MachineConfig` objects, one for the control plane nodes and another for the worker nodes in your cluster:

    1.  Create the following Butane config in the `control-plane-interface.bu` file:

        > [!NOTE]
        > The [Butane version](https://coreos.github.io/butane/specs/) you specify in the config file should match the OpenShift Container Platform version and always ends in `0`. For example, `4.17.0`. See "Creating machine configs with Butane" for information about Butane.

        ``` yaml
        variant: openshift
        version: 4.17.0
        metadata:
          name: 01-control-plane-interface
          labels:
            machineconfiguration.openshift.io/role: master
        storage:
          files:
            - path: /etc/NetworkManager/conf.d/99-<interface>-mtu.conf
              contents:
                local: <interface>-mtu.conf
              mode: 0600
        ```

        where:

        `storage.files.path`
        Specifies the `NetworkManager` connection name for the primary network interface.

        `storage.files.local`
        Specifies the local filename for the updated `NetworkManager` configuration file from an earlier step.

    2.  Create the following Butane config in the `worker-interface.bu` file:

        > [!NOTE]
        > The [Butane version](https://coreos.github.io/butane/specs/) you specify in the config file should match the OpenShift Container Platform version and always ends in `0`. For example, `4.17.0`. See "Creating machine configs with Butane" for information about Butane.

        ``` yaml
        variant: openshift
        version: 4.17.0
        metadata:
          name: 01-worker-interface
          labels:
            machineconfiguration.openshift.io/role: worker
        storage:
          files:
            - path: /etc/NetworkManager/conf.d/99-<interface>-mtu.conf
              contents:
                local: <interface>-mtu.conf
              mode: 0600
        ```

        where:

        `storage.files.path`
        Specifies the `NetworkManager` connection name for the primary network interface.

        `storage.files.local`
        Specifies the local filename for the updated `NetworkManager` configuration file from an earlier step.

2.  Create `MachineConfig` objects from the Butane configs by running the following command:

    ``` terminal
    $ for manifest in control-plane-interface worker-interface; do
        butane --files-dir . $manifest.bu > $manifest.yaml
      done
    ```

    > [!WARNING]
    > Do not apply these machine configs until explicitly instructed later in this procedure. Applying these machine configs now causes a loss of stability for the cluster.

</div>

## Beginning the MTU migration

Start the maximum transmission unit (MTU) migration by specifying the migration configuration for the cluster network and machine interfaces. The Machine Config Operator performs a rolling reboot of the nodes to prepare the cluster for the MTU change.

<div>

<div class="title">

Procedure

</div>

1.  To begin the MTU migration, specify the migration configuration by entering the following command. The Machine Config Operator performs a rolling reboot of the nodes in the cluster in preparation for the MTU change.

    ``` terminal
    $ oc patch Network.operator.openshift.io cluster --type=merge --patch \
      '{"spec": { "migration": { "mtu": { "network": { "from": <overlay_from>, "to": <overlay_to> } , "machine": { "to" : <machine_to> } } } } }'
    ```

    where:

    `<overlay_from>`
    Specifies the current cluster network MTU value.

    `<overlay_to>`
    Specifies the target MTU for the cluster network. This value is set relative to the value of `<machine_to>`. For OVN-Kubernetes, this value must be `100` less than the value of `<machine_to>`.

    `<machine_to>`
    Specifies the MTU for the primary network interface on the underlying host network.

    ``` terminal
    $ oc patch Network.operator.openshift.io cluster --type=merge --patch \
      '{"spec": { "migration": { "mtu": { "network": { "from": 1400, "to": 9000 } , "machine": { "to" : 9100} } } } }'
    ```

2.  As the Machine Config Operator updates machines in each machine config pool, the Operator reboots each node one by one. You must wait until all the nodes are updated. Check the machine config pool status by entering the following command:

    ``` terminal
    $ oc get machineconfigpools
    ```

    A successfully updated node has the following status: `UPDATED=true`, `UPDATING=false`, `DEGRADED=false`.

    > [!NOTE]
    > By default, the Machine Config Operator updates one machine per pool at a time, causing the total time the migration takes to increase with the size of the cluster.

</div>

## Verifying the machine configuration

Verify the machine configuration on your hosts to confirm that the maximum transmission unit (MTU) migration applied successfully. Checking the configuration state and system settings help ensures that the nodes use the correct migration script.

<div>

<div class="title">

Procedure

</div>

- Confirm the status of the new machine configuration on the hosts:

  1.  To list the machine configuration state and the name of the applied machine configuration, enter the following command:

      ``` terminal
      $ oc describe node | egrep "hostname|machineconfig"
      ```

      <div class="formalpara">

      <div class="title">

      Example output

      </div>

      ``` text
      kubernetes.io/hostname=master-0
      machineconfiguration.openshift.io/currentConfig: rendered-master-c53e221d9d24e1c8bb6ee89dd3d8ad7b
      machineconfiguration.openshift.io/desiredConfig: rendered-master-c53e221d9d24e1c8bb6ee89dd3d8ad7b
      machineconfiguration.openshift.io/reason:
      machineconfiguration.openshift.io/state: Done
      ```

      </div>

  2.  Verify that the following statements are true:

      - The value of `machineconfiguration.openshift.io/state` field is `Done`.

      - The value of the `machineconfiguration.openshift.io/currentConfig` field is equal to the value of the `machineconfiguration.openshift.io/desiredConfig` field.

  3.  To confirm that the machine config is correct, enter the following command:

      ``` terminal
      $ oc get machineconfig <config_name> -o yaml | grep ExecStart
      ```

      where:

      `<config_name>`
      Specifies the name of the machine config from the `machineconfiguration.openshift.io/currentConfig` field.

      The machine config must include the following update to the systemd configuration:

      ``` plain
      ExecStart=/usr/local/bin/mtu-migration.sh
      ```

</div>

## Applying the new hardware MTU value

To ensure consistent network communication across your cluster, you must apply the new hardware maximum transmission unit (MTU) value to your nodes. This process involves updating the underlying network interfaces and verifying that the Machine Config Operator successfully reboots and updates each node.

<div>

<div class="title">

Procedure

</div>

1.  Update the underlying network interface MTU value:

    - If you are specifying the new MTU with a NetworkManager connection configuration, enter the following command. The MachineConfig Operator automatically performs a rolling reboot of the nodes in your cluster.

      ``` terminal
      $ for manifest in control-plane-interface worker-interface; do
          oc create -f $manifest.yaml
        done
      ```

    - If you are specifying the new MTU with a DHCP server option or a kernel command line and PXE, make the necessary changes for your infrastructure.

2.  As the Machine Config Operator updates machines in each machine config pool, the Operator reboots each node one by one. You must wait until all the nodes are updated. Check the machine config pool status by entering the following command:

    ``` terminal
    $ oc get machineconfigpools
    ```

    A successfully updated node has the following status: `UPDATED=true`, `UPDATING=false`, `DEGRADED=false`.

    > [!NOTE]
    > By default, the Machine Config Operator updates one machine per pool at a time, causing the total time the migration takes to increase with the size of the cluster.

3.  Confirm the status of the new machine configuration on the hosts:

    1.  To list the machine configuration state and the name of the applied machine configuration, enter the following command:

        ``` terminal
        $ oc describe node | egrep "hostname|machineconfig"
        ```

        <div class="formalpara">

        <div class="title">

        Example output

        </div>

        ``` text
        kubernetes.io/hostname=master-0
        machineconfiguration.openshift.io/currentConfig: rendered-master-c53e221d9d24e1c8bb6ee89dd3d8ad7b
        machineconfiguration.openshift.io/desiredConfig: rendered-master-c53e221d9d24e1c8bb6ee89dd3d8ad7b
        machineconfiguration.openshift.io/reason:
        machineconfiguration.openshift.io/state: Done
        ```

        </div>

        Verify that the following statements are true:

        - The value of `machineconfiguration.openshift.io/state` field is `Done`.

        - The value of the `machineconfiguration.openshift.io/currentConfig` field is equal to the value of the `machineconfiguration.openshift.io/desiredConfig` field.

    2.  To confirm that the machine config is correct, enter the following command:

        ``` terminal
        $ oc get machineconfig <config_name> -o yaml | grep path:
        ```

        where:

        `<config_name>`
        Specifies the name of the machine config from the `machineconfiguration.openshift.io/currentConfig` field.

        If the machine config is successfully deployed, the previous output contains the `/etc/NetworkManager/conf.d/99-<interface>-mtu.conf` file path and the `ExecStart=/usr/local/bin/mtu-migration.sh` line.

</div>

## Finalizing the MTU migration

Finalize the MTU migration to apply the new maximum transmission unit (MTU) settings to the OVN-Kubernetes network plugin. This updates the cluster configuration and triggers a rolling reboot of the nodes to complete the process.

<div>

<div class="title">

Procedure

</div>

1.  To finalize the MTU migration, enter the following command for the OVN-Kubernetes network plugin:

    ``` terminal
    $ oc patch Network.operator.openshift.io cluster --type=merge --patch \
      '{"spec": { "migration": null, "defaultNetwork":{ "ovnKubernetesConfig": { "mtu": <mtu> }}}}'
    ```

    where:

    `<mtu>`
    Specifies the new cluster network MTU that you specified with `<overlay_to>`.

2.  After finalizing the MTU migration, each machine config pool node is rebooted one by one. You must wait until all the nodes are updated. Check the machine config pool status by entering the following command:

    ``` terminal
    $ oc get machineconfigpools
    ```

    A successfully updated node has the following status: `UPDATED=true`, `UPDATING=false`, `DEGRADED=false`.

</div>

<div>

<div class="title">

Verification

</div>

1.  To get the current MTU for the cluster network, enter the following command:

    ``` terminal
    $ oc describe network.config cluster
    ```

2.  Get the current MTU for the primary network interface of a node:

    1.  To list the nodes in your cluster, enter the following command:

        ``` terminal
        $ oc get nodes
        ```

    2.  To obtain the current MTU setting for the primary network interface on a node, enter the following command:

        ``` terminal
        $ oc adm node-logs <node> -u ovs-configuration | grep configure-ovs.sh | grep mtu | grep <interface> | head -1
        ```

        where:

        `<node>`
        Specifies a node from the output from the previous step.

        `<interface>`
        Specifies the primary network interface name for the node.

        <div class="formalpara">

        <div class="title">

        Example output

        </div>

        ``` text
        ens3: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 8051
        ```

        </div>

</div>

# Additional resources

- [Using advanced networking options for PXE and ISO installations](../../installing/installing_bare_metal/upi/installing-bare-metal.md#installation-user-infra-machines-advanced_network_installing-bare-metal)

- [Manually creating NetworkManager profiles in key file format](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/9/html-single/configuring_and_managing_networking/index#proc_manually-creating-a-networkmanager-profile-in-keyfile-format_assembly_networkmanager-connection-profiles-in-keyfile-format)

- [Configuring a dynamic Ethernet connection using nmcli](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/9/html-single/configuring_and_managing_networking/index#configuring-a-dynamic-ethernet-connection-using-nmcli_configuring-an-ethernet-connection)
