<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

You can install single-node OpenShift by using either the web-based Assisted Installer or the `coreos-installer` tool to generate a discovery ISO image.

The discovery ISO image writes the Red Hat Enterprise Linux CoreOS (RHCOS) system configuration to the target installation disk, so that you can run a single-cluster node to meet your needs.

Consider using single-node OpenShift when you want to run a cluster in a low-resource or an isolated environment for testing, troubleshooting, training, or small-scale project purposes.

# Installing single-node OpenShift using the Assisted Installer

To install OpenShift Container Platform on a single node, use the web-based Assisted Installer wizard to guide you through the process and manage the installation.

See "Installing OpenShift Container Platform with the Assisted Installer" for details and configuration options.

<div>

<div class="title">

Additional resources

</div>

- [Installing OpenShift Container Platform with the Assisted Installer](https://docs.redhat.com/en/documentation/assisted_installer_for_openshift_container_platform/2026/html/installing_openshift_container_platform_with_the_assisted_installer/index)

</div>

## Generating the discovery ISO with the Assisted Installer

Installing OpenShift Container Platform on a single node requires a discovery ISO, which the Assisted Installer can generate.

<div>

<div class="title">

Procedure

</div>

1.  On the administration host, open a browser and navigate to [Red Hat OpenShift Cluster Manager](https://console.redhat.com/openshift/assisted-installer/clusters).

2.  Click **Create New Cluster** to create a new cluster.

3.  In the **Cluster name** field, enter a name for the cluster.

4.  In the **Base domain** field, enter a base domain. For example:

        example.com

    All DNS records must be subdomains of this base domain and include the cluster name, for example:

        <cluster_name>.example.com

    > [!NOTE]
    > You cannot change the base domain or cluster name after cluster installation.

5.  Select **Install single node OpenShift (SNO)** and complete the rest of the wizard steps. Download the discovery ISO.

6.  Complete the remaining Assisted Installer wizard steps.

    > [!IMPORTANT]
    > Ensure that you take note of the discovery ISO URL for installing with virtual media.
    >
    > If you enable OpenShift Virtualization during this process, you must have a second local storage device of at least 50GiB for your virtual machines.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Persistent storage using logical volume manager storage](../../storage/persistent_storage_local/persistent-storage-using-lvms.md#persistent-storage-using-lvms_logical-volume-manager-storage)

- [What you can do with OpenShift Virtualization](../../virt/about_virt/about-virt.md#virt-what-you-can-do-with-virt_about-virt)

</div>

## Installing single-node OpenShift with the Assisted Installer

Use the Assisted Installer to install the single-node cluster.

<div>

<div class="title">

Prerequisites

</div>

- Ensure that the boot drive order in the server BIOS settings defaults to booting the server from the target installation disk.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Attach the discovery ISO image to the target host.

2.  Boot the server from the discovery ISO image. The discovery ISO image writes the system configuration to the target installation disk and automatically triggers a server restart.

3.  On the administration host, return to the browser. Wait for the host to appear in the list of discovered hosts. If necessary, reload the [**Assisted Clusters**](https://console.redhat.com/openshift/assisted-installer/clusters) page and select the cluster name.

4.  Complete the install wizard steps. Add networking details, including a subnet from the available subnets. Add the SSH public key if necessary.

5.  Monitor the installation’s progress. Watch the cluster events. After the installation process finishes writing the operating system image to the server’s hard disk, the server restarts.

6.  Optional: Remove the discovery ISO image.

    The server restarts several times automatically, deploying the control plane.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Creating a bootable ISO image on a USB drive](install-sno-installing-sno.md#installing-with-usb-media_install-sno-installing-sno-with-the-assisted-installer)

- [Booting from an HTTP-hosted ISO image using the Redfish API](install-sno-installing-sno.md#install-booting-from-an-iso-over-http-redfish_install-sno-installing-sno-with-the-assisted-installer)

- [Adding worker nodes to single-node OpenShift clusters](../../nodes/nodes/nodes-sno-worker-nodes.md#nodes-sno-worker-nodes)

</div>

# Installing single-node OpenShift manually

To install OpenShift Container Platform on a single node, first generate the installation ISO, and then boot the server from the ISO. You can monitor the installation using the `openshift-install` installation program.

<div>

<div class="title">

Additional resources

</div>

- [Networking requirements for user-provisioned infrastructure](../installing_bare_metal/upi/installing-bare-metal-network-customizations.md#installation-network-user-infra_installing-bare-metal-network-customizations)

- [User-provisioned DNS requirements](../installing_bare_metal/upi/installing-bare-metal-network-customizations.md#installation-dns-user-infra_installing-bare-metal-network-customizations)

- [Configuring DHCP or static IP addresses](../installing_bare_metal/upi/installing-bare-metal-network-customizations.md#configuring-dhcp-or-static-ip-addresses_installing-bare-metal-network-customizations)

</div>

## Generating the installation ISO with coreos-installer

You can install OpenShift Container Platform on a single node by generating an installation ISO.

<div>

<div class="title">

Prerequisites

</div>

- Install `podman`.

</div>

> [!NOTE]
> See "Requirements for installing OpenShift on a single node" for networking requirements, including DNS records.

<div>

<div class="title">

Procedure

</div>

1.  Set the OpenShift Container Platform version:

    ``` terminal
    $ export OCP_VERSION=<ocp_version>
    ```

    Replace `<ocp_version>` with the current version, for example, `latest-4.17`

2.  Set the target cluster architecture:

    ``` terminal
    $ export ARCH=<architecture>
    ```

    Replace `<architecture>` with the target host architecture, for example, `aarch64` or `x86_64`.

3.  Set the installation host architecture:

    ``` terminal
    $ export HOST_ARCH=$(uname -m)
    ```

    This command detects the architecture of the installation host. If the installation host architecture differs from the target cluster architecture, the downloaded binaries must match the installation host. For example, if you are installing an `aarch64` cluster from an `x86_64` bastion host, `HOST_ARCH` is `x86_64`.

4.  Download the OpenShift Container Platform client (`oc`) and make it available for use by entering the following commands:

    ``` terminal
    $ curl -k https://mirror.openshift.com/pub/openshift-v4/$HOST_ARCH/clients/ocp/$OCP_VERSION/openshift-client-linux.tar.gz -o oc.tar.gz
    ```

    ``` terminal
    $ tar zxf oc.tar.gz
    ```

    ``` terminal
    $ chmod +x oc
    ```

5.  Download the OpenShift Container Platform installer and make it available for use by entering the following commands:

    ``` terminal
    $ curl -k https://mirror.openshift.com/pub/openshift-v4/$HOST_ARCH/clients/ocp/$OCP_VERSION/openshift-install-linux.tar.gz -o openshift-install-linux.tar.gz
    ```

    ``` terminal
    $ tar zxvf openshift-install-linux.tar.gz
    ```

    ``` terminal
    $ chmod +x openshift-install
    ```

6.  Retrieve the RHCOS ISO URL by running the following command:

    ``` terminal
    $ export ISO_URL=$(./openshift-install coreos print-stream-json | grep location | grep $ARCH | grep iso | cut -d\" -f4)
    ```

7.  Download the RHCOS ISO:

    ``` terminal
    $ curl -L $ISO_URL -o rhcos-live.iso
    ```

8.  Prepare the `install-config.yaml` file:

    ``` yaml
    apiVersion: v1
    baseDomain: <domain>
    compute:
    - name: worker
      replicas: 0
    controlPlane:
      name: master
      replicas: 1
    metadata:
      name: <name>
    networking:
      clusterNetwork:
      - cidr: 10.128.0.0/14
        hostPrefix: 23
      machineNetwork:
      - cidr: 10.0.0.0/16
      networkType: OVNKubernetes
      serviceNetwork:
      - 172.30.0.0/16
    platform:
      none: {}
    bootstrapInPlace:
      installationDisk: /dev/disk/by-id/<disk_id>
    pullSecret: '<pull_secret>'
    sshKey: |
      <ssh_key>
    ```

    where:

    `baseDomain`
    Specifies the cluster domain name.

    `compute.replicas`
    Specifies the value of `compute.replicas` as `0`. This makes the control plane node schedulable.

    `controlPlane.replicas`
    Specifies the value of `controlPlane.replicas` as `1`. In conjunction with the previous `compute` setting, this setting ensures the cluster runs on a single node.

    `metadata.name`
    Specifies the `metadata` name to the cluster name.

    `networking`
    Specifies the `networking` details. OVN-Kubernetes is the only allowed network plugin type for single-node clusters.

    `machineNetwork.cidr`
    Specifies the `cidr` value to match the subnet of the cluster.

    `installationDisk`
    Specifies the path to the installation disk drive, for example, `/dev/disk/by-id/wwn-0x64cd98f04fde100024684cf3034da5c2`.

    `pullSecret`
    Specifies the `pullSecret` parameter. Copy the [pull secret from Red Hat OpenShift Cluster Manager](https://console.redhat.com/openshift/install/pull-secret) and add the contents to this configuration setting.

    `sshKey`
    Specifies the `sshKey` parameter. Add the public SSH key from the administration host so that you can log in to the cluster after installation.

9.  Generate OpenShift Container Platform assets by running the following commands:

    ``` terminal
    $ mkdir ocp
    ```

    ``` terminal
    $ cp install-config.yaml ocp
    ```

    ``` terminal
    $ ./openshift-install --dir=ocp create single-node-ignition-config
    ```

10. Embed the ignition data into the RHCOS ISO by running the following commands:

    ``` terminal
    $ alias coreos-installer='podman run --privileged --pull always --rm \
            -v /dev:/dev -v /run/udev:/run/udev -v $PWD:/data \
            -w /data quay.io/coreos/coreos-installer:release'
    ```

    ``` terminal
    $ coreos-installer iso ignition embed -fi ocp/bootstrap-in-place-for-live-iso.ign rhcos-live.iso
    ```

    > [!IMPORTANT]
    > The SSL certificates for the RHCOS ISO installation image are only valid for 24 hours. If you use the ISO image to install a node more than 24 hours after creating the image, the installation can fail. To re-create the image after 24 hours, delete the `ocp` directory and re-create the OpenShift Container Platform assets.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Requirements for installing OpenShift on a single node](install-sno-preparing-to-install-sno.md#preparing-to-install-sno)

- [Cluster capabilities](../overview/cluster-capabilities.md#cluster-capabilities)

- [Optional cluster capabilities in OpenShift Container Platform 4.17](../overview/cluster-capabilities.md#explanation_of_capabilities_cluster-capabilities)

</div>

## Monitoring the cluster installation using openshift-install

Use the `openshift-install` binary to monitor the progress of the single-node cluster installation.

<div>

<div class="title">

Prerequisites

</div>

- Ensure that the boot drive order in the server BIOS settings defaults to booting the server from the target installation disk.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Attach the discovery ISO image to the target host.

2.  Boot the server from the discovery ISO image. The discovery ISO image writes the system configuration to the target installation disk and automatically triggers a server restart.

3.  On the administration host, monitor the installation by running the following command:

    ``` terminal
    $ ./openshift-install --dir=ocp wait-for install-complete
    ```

4.  Optional: Remove the discovery ISO image.

    The server restarts several times while deploying the control plane.

</div>

<div>

<div class="title">

Verification

</div>

- After the installation is complete, check the environment by running the following command:

  ``` terminal
  $ export KUBECONFIG=ocp/auth/kubeconfig
  ```

  ``` terminal
  $ oc get nodes
  ```

  <div class="formalpara">

  <div class="title">

  Example output

  </div>

  ``` terminal
  NAME                         STATUS   ROLES           AGE     VERSION
  control-plane.example.com    Ready    master,worker   10m     v1.33.4
  ```

  </div>

</div>

<div>

<div class="title">

Additional resources

</div>

- [Creating a bootable ISO image on a USB drive](install-sno-installing-sno.md#installing-with-usb-media_install-sno-installing-sno-with-the-assisted-installer)

- [Booting from an HTTP-hosted ISO image using the Redfish API](install-sno-installing-sno.md#install-booting-from-an-iso-over-http-redfish_install-sno-installing-sno-with-the-assisted-installer)

- [Adding worker nodes to single-node OpenShift clusters](../../nodes/nodes/nodes-sno-worker-nodes.md#nodes-sno-worker-nodes)

</div>

# Installing single-node OpenShift with the Agent-based Installer

You can use the Agent-based Installer to deploy single-node OpenShift on bare-metal servers running ARM (`aarch64`) architecture. The Agent-based Installer generates a self-contained bootable ISO image by using the OpenShift Container Platform installer for offline and automated deployments.

The following procedure describes how to create the required configuration files, generate the agent ISO image, and boot the target ARM server to install single-node OpenShift.

<div>

<div class="title">

Additional resources

</div>

- [Preparing to install with the Agent-based Installer](../installing_with_agent_based_installer/preparing-to-install-with-agent-based-installer.md#preparing-to-install-with-agent-based-installer)

</div>

## Installing single-node OpenShift with the Agent-based Installer on ARM architecture

You can use the Agent-based Installer to install single-node OpenShift on an `aarch64` (ARM) server. The Agent-based Installer generates a bootable ISO image that you use to boot the target machine and deploy the cluster.

<div>

<div class="title">

Prerequisites

</div>

- You downloaded the `openshift-install` binary for your installation host architecture from the [Red Hat Hybrid Cloud Console](https://console.redhat.com). When you select the architecture on the console, ensure that it matches your installation host and that you select `ARM64` (`aarch64`) as the target cluster architecture.

- You have a valid pull secret from the [Red Hat Hybrid Cloud Console](https://console.redhat.com).

- You have an SSH public key on the administration host.

- You configured DNS records for `api.<cluster_name>.<base_domain>` and `*.apps.<cluster_name>.<base_domain>` to point to the node IP address.

</div>

> [!NOTE]
> See "Requirements for installing OpenShift on a single node" for networking requirements, including DNS records.

<div>

<div class="title">

Procedure

</div>

1.  Create a directory to store the installation configuration by running the following command:

    ``` terminal
    $ mkdir ~/<install_directory>
    ```

2.  Create the `install-config.yaml` file in the installation directory as in the following example:

    ``` yaml
    apiVersion: v1
    baseDomain: <domain>
    compute:
    - architecture: arm64
      hyperthreading: Enabled
      name: worker
      replicas: 0
    controlPlane:
      architecture: arm64
      hyperthreading: Enabled
      name: master
      replicas: 1
    metadata:
      name: <cluster_name>
    networking:
      clusterNetwork:
      - cidr: 10.128.0.0/14
        hostPrefix: 23
      machineNetwork:
      - cidr: <machine_network_cidr>
      networkType: OVNKubernetes
      serviceNetwork:
      - 172.30.0.0/16
    platform:
      none: {}
    pullSecret: '<pull_secret>'
    sshKey: '<ssh_pub_key>'
    ```

    The following table describes the required parameters:

    | Parameter | Description |
    |----|----|
    | `baseDomain` | Specify the cluster base domain name. |
    | `compute[].architecture` | Set to `arm64` for ARM-based deployments. Must match the `controlPlane` architecture. |
    | `compute[].replicas` | Set to `0` to make the control plane node schedulable. |
    | `controlPlane.architecture` | Set to `arm64` for ARM-based deployments. Must match the `compute` architecture. |
    | `controlPlane.replicas` | Set to `1` to ensure the cluster runs on a single node. |
    | `metadata.name` | Specify the cluster name. |
    | `machineNetwork[].cidr` | Set the CIDR value to match the subnet of the single-node OpenShift cluster. |
    | `networkType` | Set to `OVNKubernetes`. This is the only supported network plugin for single-node clusters. |
    | `pullSecret` | Copy the [pull secret from Red Hat OpenShift Cluster Manager](https://console.redhat.com/openshift/install/pull-secret) and add the contents to this configuration setting. |
    | `sshKey` | Provide the public SSH key from the administration host so that you can log in to the cluster after installation. |

    Required `install-config.yaml` parameters

3.  Create the `agent-config.yaml` file in the same installation directory as in the following example:

    ``` yaml
    apiVersion: v1beta1
    kind: AgentConfig
    metadata:
      name: <cluster_name>
    rendezvousIP: <node_ip>
    ```

    Replace `<cluster_name>` with the cluster name. This value must match the `metadata.name` value in `install-config.yaml`. Replace `<node_ip>` with the IP address of the node. For single-node OpenShift, this is the IP address of the single node.

4.  Generate the agent ISO image by running the following command:

    ``` terminal
    $ openshift-install --dir ~/<install_directory> agent create image
    ```

    The command creates the `agent.aarch64.iso` image in the installation directory.

5.  Transfer the `agent.aarch64.iso` image to the target ARM server and boot from it. You can use one of the following methods:

    - Attach the ISO image by using a virtual media interface such as Redfish or a BMC console.

    - Write the ISO image to a USB drive and boot from it.

    - Host the ISO image on an HTTP server and boot from it by using the Redfish API.

    The ISO image writes the system configuration to the target installation disk and installs OpenShift Container Platform.

6.  Monitor the installation progress from the administration host by running the following command:

    ``` terminal
    $ openshift-install --dir ~/<install_directory> agent wait-for install-complete --log-level=info
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    ...................................................................
    INFO Cluster is installed
    INFO Install complete!
    INFO To access the cluster as the system:admin user when using 'oc', run
    INFO     export KUBECONFIG=~/<install_directory>/auth/kubeconfig
    INFO Access the OpenShift web-console here: https://console-openshift-console.apps.<cluster_name>.<domain>
    ```

    </div>

</div>

<div>

<div class="title">

Verification

</div>

- After the installation is complete, verify the cluster by running the following commands:

  ``` terminal
  $ export KUBECONFIG=~/<install_directory>/auth/kubeconfig
  ```

  ``` terminal
  $ oc get nodes
  ```

  <div class="formalpara">

  <div class="title">

  Example output

  </div>

  ``` terminal
  NAME                    STATUS   ROLES                         AGE     VERSION
  <node_name>             Ready    control-plane,master,worker   10m     v1.34.2
  ```

  </div>

</div>

# Additional requirements for installing single-node OpenShift on a cloud provider

Compared to installing a high-availability cluster, there are additional requirements for installing single-node OpenShift.

The documentation for installer-provisioned installation on cloud providers is based on a high availability cluster consisting of three control plane nodes. When referring to the documentation, consider the differences between the requirements for a single-node OpenShift cluster and a high availability cluster.

- A high availability cluster requires a temporary bootstrap machine, three control plane machines, and at least two compute machines. For a single-node OpenShift cluster, you need only a temporary bootstrap machine and one cloud instance for the control plane node and no compute nodes.

- The minimum resource requirements for high availability cluster installation include a control plane node with 4 vCPUs and 100GB of storage. For a single-node OpenShift cluster, you must have a minimum of 8 vCPUs and 120GB of storage.

- The `controlPlane.replicas` setting in the `install-config.yaml` file should be set to `1`.

- The `compute.replicas` setting in the `install-config.yaml` file should be set to `0`. This makes the control plane node schedulable.

# Supported cloud providers for single-node OpenShift

You can install a single-node cluster on several supported cloud providers.

The following table contains a list of supported cloud providers and CPU architectures.

| Cloud provider           | CPU architecture   |
|--------------------------|--------------------|
| Amazon Web Service (AWS) | x86_64 and AArch64 |
| Microsoft Azure          | x86_64             |
| Google Cloud             | x86_64 and AArch64 |

Supported cloud providers

# Installing single-node OpenShift on AWS

Installing a single-node cluster on AWS requires installer-provisioned installation using the "Installing a cluster on AWS with customizations" procedure.

<div>

<div class="title">

Additional resources

</div>

- [Installing a cluster on AWS with customizations](../installing_aws/ipi/installing-aws-customizations.md#installing-aws-customizations)

</div>

# Installing single-node OpenShift on Azure

Installing a single-node cluster on Azure requires installer-provisioned installation using the "Installing a cluster on Azure with customizations" procedure.

<div>

<div class="title">

Additional resources

</div>

- [Installing a cluster on Azure with customizations](../installing_azure/ipi/installing-azure-customizations.md#installing-azure-customizations)

</div>

# Installing single-node OpenShift on Google Cloud

Installing a single-node cluster on Google Cloud requires installer-provisioned installation using the "Installing a cluster on Google Cloud with customizations" procedure.

<div>

<div class="title">

Additional resources

</div>

- [Installing a cluster on Google Cloud with customizations](../installing_gcp/installing-gcp-customizations.md#installing-gcp-customizations)

</div>

# Creating a bootable ISO image on a USB drive

You can install software using a bootable USB drive that contains an ISO image. Booting the server with the USB drive prepares the server for the software installation.

<div>

<div class="title">

Procedure

</div>

1.  On the administration host, insert a USB drive into a USB port.

2.  Create a bootable USB drive, for example:

    ``` terminal
    # dd if=<path_to_iso> of=<path_to_usb> status=progress
    ```

    where:

    \<path_to_iso\>
    is the relative path to the downloaded ISO file, for example, `rhcos-live.iso`.

    \<path_to_usb\>
    is the location of the connected USB drive, for example, `/dev/sdb`.

    After the ISO is copied to the USB drive, you can use the USB drive to install software on the server.

</div>

# Booting from an HTTP-hosted ISO image using the Redfish API

You can provision hosts in your network using ISOs that you install using the Redfish Baseboard Management Controller (BMC) API.

> [!NOTE]
> This example procedure demonstrates the steps on a Dell server.

> [!IMPORTANT]
> Ensure that you have the latest firmware version of iDRAC that is compatible with your hardware. If you have any issues with the hardware or firmware, you must contact the provider.

<div>

<div class="title">

Prerequisites

</div>

- Download the installation Red Hat Enterprise Linux CoreOS (RHCOS) ISO.

- Use a Dell PowerEdge server that is compatible with iDRAC9.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Copy the ISO file to an HTTP server accessible in your network.

2.  Boot the host from the hosted ISO file, for example:

    1.  Call the Redfish API to set the hosted ISO as the `VirtualMedia` boot media by running the following command:

        ``` terminal
        $ curl -k -u <bmc_username>:<bmc_password> -d '{"Image":"<hosted_iso_file>", "Inserted": true}' -H "Content-Type: application/json" -X POST <host_bmc_address>/redfish/v1/Managers/iDRAC.Embedded.1/VirtualMedia/CD/Actions/VirtualMedia.InsertMedia
        ```

        Where:

        \<bmc_username\>:\<bmc_password\>
        Is the username and password for the target host BMC.

        \<hosted_iso_file\>
        Is the URL for the hosted installation ISO, for example: `http://webserver.example.com/rhcos-live-minimal.iso`. The ISO must be accessible from the target host machine.

        \<host_bmc_address\>
        Is the BMC IP address of the target host machine.

    2.  Set the host to boot from the `VirtualMedia` device by running the following command:

        ``` terminal
        $ curl -k -u <bmc_username>:<bmc_password> -X PATCH -H 'Content-Type: application/json' -d '{"Boot": {"BootSourceOverrideTarget": "Cd", "BootSourceOverrideMode": "UEFI", "BootSourceOverrideEnabled": "Once"}}' <host_bmc_address>/redfish/v1/Systems/System.Embedded.1
        ```

    3.  Reboot the host:

        ``` terminal
        $ curl -k -u <bmc_username>:<bmc_password> -d '{"ResetType": "ForceRestart"}' -H 'Content-type: application/json' -X POST <host_bmc_address>/redfish/v1/Systems/System.Embedded.1/Actions/ComputerSystem.Reset
        ```

    4.  Optional: If the host is powered off, you can boot it using the `{"ResetType": "On"}` switch. Run the following command:

        ``` terminal
        $ curl -k -u <bmc_username>:<bmc_password> -d '{"ResetType": "On"}' -H 'Content-type: application/json' -X POST <host_bmc_address>/redfish/v1/Systems/System.Embedded.1/Actions/ComputerSystem.Reset
        ```

</div>

# Creating a custom live RHCOS ISO for remote server access

In some cases, you cannot attach an external disk drive to a server, however, you need to access the server remotely to provision a node. It is recommended to enable SSH access to the server.

You can create a live RHCOS ISO with SSHd enabled and with predefined credentials so that you can access the server after it boots.

<div>

<div class="title">

Prerequisites

</div>

- You installed the `butane` utility.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Download the `coreos-installer` binary from the `coreos-installer` image [mirror](https://mirror.openshift.com/pub/openshift-v4/clients/coreos-installer/latest/) page.

2.  Download the latest live RHCOS ISO from [mirror.openshift.com](https://mirror.openshift.com/pub/openshift-v4/x86_64/dependencies/rhcos/4.12/latest/).

3.  Create the `embedded.yaml` file that the `butane` utility uses to create the Ignition file:

    ``` yaml
    variant: openshift
    version: 4.17.0
    metadata:
      name: sshd
      labels:
        machineconfiguration.openshift.io/role: worker
    passwd:
      users:
        - name: core
          ssh_authorized_keys:
            - '<ssh_key>'
    ```

    For the `passwd.users.name` parameter, the `core` user has sudo privileges.

4.  Run the `butane` utility to create the Ignition file using the following command:

    ``` terminal
    $ butane -pr embedded.yaml -o embedded.ign
    ```

5.  After the Ignition file is created, you can include the configuration in a new live RHCOS ISO, which is named `rhcos-sshd-4.17.0-x86_64-live.x86_64.iso`, with the `coreos-installer` utility:

    ``` terminal
    $ coreos-installer iso ignition embed -i embedded.ign rhcos-4.17.0-x86_64-live.x86_64.iso -o rhcos-sshd-4.17.0-x86_64-live.x86_64.iso
    ```

</div>

<div>

<div class="title">

Verification

</div>

- Check that the custom live ISO can be used to boot the server by running the following command:

  ``` terminal
  # coreos-installer iso ignition show rhcos-sshd-4.17.0-x86_64-live.x86_64.iso
  ```

  <div class="formalpara">

  <div class="title">

  Example output

  </div>

  ``` json
  {
    "ignition": {
      "version": "3.2.0"
    },
    "passwd": {
      "users": [
        {
          "name": "core",
          "sshAuthorizedKeys": [
            "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCZnG8AIzlDAhpyENpK2qKiTT8EbRWOrz7NXjRzopbPu215mocaJgjjwJjh1cYhgPhpAp6M/ttTk7I4OI7g4588Apx4bwJep6oWTU35LkY8ZxkGVPAJL8kVlTdKQviDv3XX12l4QfnDom4tm4gVbRH0gNT1wzhnLP+LKYm2Ohr9D7p9NBnAdro6k++XWgkDeijLRUTwdEyWunIdW1f8G0Mg8Y1Xzr13BUo3+8aey7HLKJMDtobkz/C8ESYA/f7HJc5FxF0XbapWWovSSDJrr9OmlL9f4TfE+cQk3s+eoKiz2bgNPRgEEwihVbGsCN4grA+RzLCAOpec+2dTJrQvFqsD alosadag@sonnelicht.local"
          ]
        }
      ]
    }
  }
  ```

  </div>

</div>

# Installing single-node OpenShift with IBM Z and IBM LinuxONE

You can install a single-node OpenShift cluster with IBM Z and IBM LinuxONE by performing a user-provisioned installation.

Installing a single-node cluster on IBM Z® and IBM® LinuxONE requires user-provisioned installation using one of the following procedures:

- "Installing a cluster with z/VM on IBM Z® and IBM® LinuxONE"

- "Installing a cluster with RHEL KVM on IBM Z® and IBM® LinuxONE"

- "Installing a cluster in an LPAR on IBM Z® and IBM® LinuxONE"

> [!NOTE]
> Installing a single-node cluster on IBM Z® simplifies installation for development and test environments and requires less resource requirements at entry level.

You must meet the following hardware requirements when installing a single-node cluster on IBM Z® and IBM® LinuxONE:

- The equivalent of two Integrated Facilities for Linux (IFL), which are SMT2 enabled, for each cluster.

- At least one network connection to both connect to the `LoadBalancer` service and to serve data for traffic outside the cluster.

> [!NOTE]
> You can use dedicated or shared IFLs to assign sufficient compute resources. Resource sharing is one of the key strengths of IBM Z®. However, you must adjust capacity correctly on each hypervisor layer and ensure sufficient resources for every OpenShift Container Platform cluster.

<div>

<div class="title">

Additional resources

</div>

- [Installing a cluster with z/VM on IBM Z® and IBM® LinuxONE](../installing_ibm_z/upi/installing-ibm-z.md#installing-ibm-z)

- [Installing a cluster with RHEL KVM on IBM Z® and IBM® LinuxONE](../installing_ibm_z/upi/installing-ibm-z-kvm.md#installing-ibm-z-kvm)

- [Installing a cluster in an LPAR on IBM Z® and IBM® LinuxONE](../installing_ibm_z/upi/installing-ibm-z-lpar.md#installing-ibm-z-lpar)

</div>

## Installing single-node OpenShift with z/VM on IBM Z and IBM LinuxONE

You can install single-node OpenShift with z/VM on IBM Z and IBM LinuxONE.

<div>

<div class="title">

Prerequisites

</div>

- You have installed `podman`.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Set the OpenShift Container Platform version by running the following command:

    ``` terminal
    $ OCP_VERSION=<ocp_version>
    ```

    Replace `<ocp_version>` with the current version. For example, `latest-4.17`.

2.  Set the host architecture by running the following command:

    ``` terminal
    $ ARCH=<architecture>
    ```

    Replace `<architecture>` with the target host architecture `s390x`.

3.  Download the OpenShift Container Platform client (`oc`) and make it available for use by entering the following commands:

    ``` terminal
    $ curl -k https://mirror.openshift.com/pub/openshift-v4/${ARCH}/clients/ocp/${OCP_VERSION}/openshift-client-linux.tar.gz -o oc.tar.gz
    ```

    ``` terminal
    $ tar zxf oc.tar.gz
    ```

    ``` terminal
    $ chmod +x oc
    ```

4.  Download the OpenShift Container Platform installer and make it available for use by entering the following commands:

    ``` terminal
    $ curl -k https://mirror.openshift.com/pub/openshift-v4/${ARCH}/clients/ocp/${OCP_VERSION}/openshift-install-linux.tar.gz -o openshift-install-linux.tar.gz
    ```

    ``` terminal
    $ tar zxvf openshift-install-linux.tar.gz
    ```

    ``` terminal
    $ chmod +x openshift-install
    ```

5.  Prepare the `install-config.yaml` file:

    ``` yaml
    apiVersion: v1
    baseDomain: <domain>
    compute:
    - name: worker
      replicas: 0
    controlPlane:
      name: master
      replicas: 1
    metadata:
      name: <name>
    networking:
      clusterNetwork:
      - cidr: 10.128.0.0/14
        hostPrefix: 23
      machineNetwork:
      - cidr: 10.0.0.0/16
      networkType: OVNKubernetes
      serviceNetwork:
      - 172.30.0.0/16
    platform:
      none: {}
    bootstrapInPlace:
      installationDisk: /dev/disk/by-id/<disk_id>
    pullSecret: '<pull_secret>'
    sshKey: |
      <ssh_key>
    ```

    where:

    `baseDomain`
    Specifies the cluster domain name.

    `compute.replicas`
    Specifies the `compute` replicas to `0`. This makes the control plane node schedulable.

    `controlPlane.replicas`
    Specifies the `controlPlane` replicas to `1`. In conjunction with the previous `compute` setting, this setting ensures the cluster runs on a single node.

    `metadata.name`
    Specifies the cluster name.

    `networking`
    Specifies the `networking` details. OVN-Kubernetes is the only allowed network plugin type for single-node clusters.

    `machineNetwork.cidr`
    Specifies the `cidr` value to match the subnet of the single-node OpenShift cluster.

    `bootstrapInPlace.installationDisk`
    Specifies the path to the installation disk drive, for example, `/dev/disk/by-id/wwn-0x64cd98f04fde100024684cf3034da5c2`.

    `pullSecret`
    Specifies the `pullSecret` parameter. Copy the [pull secret from Red Hat OpenShift Cluster Manager](https://console.redhat.com/openshift/install/pull-secret) and add the contents to this configuration setting.

    `sshKey`
    Specifies the `sshKey` parameter. Add the public SSH key from the administration host so that you can log in to the cluster after installation.

6.  Generate OpenShift Container Platform assets by running the following commands:

    ``` terminal
    $ mkdir ocp
    ```

    ``` terminal
    $ cp install-config.yaml ocp
    ```

    ``` terminal
    $ ./openshift-install --dir=ocp create single-node-ignition-config
    ```

7.  Obtain the RHEL `kernel`, `initramfs`, and `rootfs` artifacts from the [Product Downloads](https://access.redhat.com/downloads/content/290) page on the Red Hat Customer Portal or from the [RHCOS image mirror](https://mirror.openshift.com/pub/openshift-v4/s390x/dependencies/rhcos/latest/) page.

    > [!IMPORTANT]
    > The RHCOS images might not change with every release of OpenShift Container Platform. You must download images with the highest version that is less than or equal to the OpenShift Container Platform version that you install. Only use the appropriate `kernel`, `initramfs`, and `rootfs` artifacts described in the following procedure.

    The file names contain the OpenShift Container Platform version number. They resemble the following examples:

    `kernel`
    `rhcos-<version>-live-kernel-<architecture>`

    `initramfs`
    `rhcos-<version>-live-initramfs.<architecture>.img`

    `rootfs`
    `rhcos-<version>-live-rootfs.<architecture>.img`

    > [!NOTE]
    > The `rootfs` image is the same for FCP and DASD.

8.  Move the following artifacts and files to an HTTP or HTTPS server:

    - Downloaded RHEL live `kernel`, `initramfs`, and `rootfs` artifacts

    - Ignition files

9.  Create parameter files for a particular virtual machine:

    <div class="formalpara">

    <div class="title">

    Example parameter file

    </div>

    ``` terminal
    cio_ignore=all,!condev rd.neednet=1 \
    console=ttysclp0 \
    ignition.firstboot ignition.platform.id=metal \
    ignition.config.url=http://<http_server>:8080/ignition/bootstrap-in-place-for-live-iso.ign \
    coreos.live.rootfs_url=http://<http_server>/rhcos-<version>-live-rootfs.<architecture>.img \
    ip=<ip>::<gateway>:<mask>:<hostname>::none nameserver=<dns> \
    rd.znet=qeth,0.0.bdd0,0.0.bdd1,0.0.bdd2,layer2=1 \
    rd.dasd=0.0.4411 \
    rd.zfcp=0.0.8001,0x50050763040051e3,0x4000406300000000 \
    zfcp.allow_lun_scan=0
    ```

    </div>

    - For the `ignition.config.url=` parameter, specify the Ignition file for the machine role. Only HTTP and HTTPS protocols are supported.

    - For the `coreos.live.rootfs_url=` artifact, specify the matching `rootfs` artifact for the `` kernel`and `initramfs `` you are booting. Only HTTP and HTTPS protocols are supported.

    - For the `ip=` parameter, assign the IP address automatically using DHCP or manually as described in "Installing a cluster with z/VM on IBM Z® and IBM® LinuxONE".

    - For installations on DASD-type disks, use `rd.dasd=` to specify the DASD where RHCOS is to be installed. Omit this entry for FCP-type disks.

    - For installations on FCP-type disks, use `rd.zfcp=<adapter>,<wwpn>,<lun>` to specify the FCP disk where RHCOS is to be installed. Omit this entry for DASD-type disks.

    Leave all other parameters unchanged.

10. Transfer the following artifacts, files, and images to z/VM. For example by using FTP:

    - `kernel` and `initramfs` artifacts

    - Parameter files

    - RHCOS images

      For details about how to transfer the files with FTP and boot from the virtual reader, see [Installing under Z/VM](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/installation_guide/sect-installing-zvm-s390).

11. Punch the files to the virtual reader of the z/VM guest virtual machine that is to become your bootstrap node.

12. Log in to CMS on the bootstrap machine.

13. IPL the bootstrap machine from the reader by running the following command:

        $ cp ipl c

14. After the first reboot of the virtual machine, run the following commands directly after one another:

    1.  To boot a DASD device after first reboot, run the following commands:

        ``` terminal
        $ cp i <devno> clear loadparm prompt
        ```

        Replace `<devno>` with the device number of the boot device as seen by the guest.

        ``` terminal
        $ cp vi vmsg 0 <kernel_parameters>
        ```

        Replace `<kernel_parameters>` with a set of kernel parameters to be stored as system control program data (SCPDATA). When booting Linux, these kernel parameters are concatenated to the end of the existing kernel parameters that are used by your boot configuration. The combined parameter string must not exceed 896 characters.

    2.  To boot an FCP device after first reboot, run the following commands:

        ``` terminal
        $ cp set loaddev portname <wwpn> lun <lun>
        ```

        Replace `<wwpn>` with the target port and `<lun>` with the logical unit in hexadecimal format.

        ``` terminal
        $ cp set loaddev bootprog <n>
        ```

        Replace `<n>` with the kernel to be booted.

        ``` terminal
        $ cp set loaddev scpdata {APPEND|NEW} '<kernel_parameters>'
        ```

        where:

        `<kernel_parameters>`
        Specifies a set of kernel parameters to be stored as system control program data (SCPDATA). When booting Linux, these kernel parameters are concatenated to the end of the existing kernel parameters that are used by your boot configuration. The combined parameter string must not exceed 896 characters.

        `<APPEND|NEW>`
        Optional: Specify `APPEND` to append kernel parameters to existing SCPDATA. This is the default. Specify `NEW` to replace existing SCPDATA.

        <div class="formalpara">

        <div class="title">

        Example

        </div>

        ``` terminal
        $ cp set loaddev scpdata 'rd.zfcp=0.0.8001,0x500507630a0350a4,0x4000409D00000000
        ip=encbdd0:dhcp::02:00:00:02:34:02 rd.neednet=1'
        ```

        </div>

        To start the IPL and boot process, run the following command:

        ``` terminal
        $ cp i <devno>
        ```

        Replace `<devno>` with the device number of the boot device as seen by the guest.

</div>

## Installing single-node OpenShift with RHEL KVM on IBM Z and IBM LinuxONE

You can install single-node OpenShift with with RHEL KVM on IBM Z and IBM LinuxONE.

<div>

<div class="title">

Prerequisites

</div>

- You have installed `podman`.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Set the OpenShift Container Platform version by running the following command:

    ``` terminal
    $ OCP_VERSION=<ocp_version>
    ```

    Replace `<ocp_version>` with the current version. For example, `latest-4.17`.

2.  Set the host architecture by running the following command:

    ``` terminal
    $ ARCH=<architecture>
    ```

    Replace `<architecture>` with the target host architecture `s390x`.

3.  Download the OpenShift Container Platform client (`oc`) and make it available for use by entering the following commands:

    ``` terminal
    $ curl -k https://mirror.openshift.com/pub/openshift-v4/${ARCH}/clients/ocp/${OCP_VERSION}/openshift-client-linux.tar.gz -o oc.tar.gz
    ```

    ``` terminal
    $ tar zxf oc.tar.gz
    ```

    ``` terminal
    $ chmod +x oc
    ```

4.  Download the OpenShift Container Platform installer and make it available for use by entering the following commands:

    ``` terminal
    $ curl -k https://mirror.openshift.com/pub/openshift-v4/${ARCH}/clients/ocp/${OCP_VERSION}/openshift-install-linux.tar.gz -o openshift-install-linux.tar.gz
    ```

    ``` terminal
    $ tar zxvf openshift-install-linux.tar.gz
    ```

    ``` terminal
    $ chmod +x openshift-install
    ```

5.  Prepare the `install-config.yaml` file:

    ``` yaml
    apiVersion: v1
    baseDomain: <domain>
    compute:
    - name: worker
      replicas: 0
    controlPlane:
      name: master
      replicas: 1
    metadata:
      name: <name>
    networking:
      clusterNetwork:
      - cidr: 10.128.0.0/14
        hostPrefix: 23
      machineNetwork:
      - cidr: 10.0.0.0/16
      networkType: OVNKubernetes
      serviceNetwork:
      - 172.30.0.0/16
    platform:
      none: {}
    bootstrapInPlace:
      installationDisk: /dev/disk/by-id/<disk_id>
    pullSecret: '<pull_secret>'
    sshKey: |
      <ssh_key>
    ```

    where:

    `baseDomain`
    Specifies the cluster domain name.

    `compute.replicas`
    Specifies the `compute` replicas to `0`. This makes the control plane node schedulable.

    `controlPlane.replicas`
    Specifies the `controlPlane` replicas to `1`. In conjunction with the previous `compute` setting, this setting ensures the cluster runs on a single node.

    `metadata.name`
    Specifies the cluster name.

    `networking`
    Specifies the `networking` details. OVN-Kubernetes is the only allowed network plugin type for single-node clusters.

    `machineNetwork.cidr`
    Specifies the `cidr` value to match the subnet of the single-node OpenShift cluster.

    `bootstrapInPlace.installationDisk`
    Specifies the path to the installation disk drive, for example, `/dev/disk/by-id/wwn-0x64cd98f04fde100024684cf3034da5c2`.

    `pullSecret`
    Specifies the `pullSecret` parameter. Copy the [pull secret from Red Hat OpenShift Cluster Manager](https://console.redhat.com/openshift/install/pull-secret) and add the contents to this configuration setting.

    `sshKey`
    Specifies the `sshKey` parameter. Add the public SSH key from the administration host so that you can log in to the cluster after installation.

6.  Generate OpenShift Container Platform assets by running the following commands:

    ``` terminal
    $ mkdir ocp
    ```

    ``` terminal
    $ cp install-config.yaml ocp
    ```

    ``` terminal
    $ ./openshift-install --dir=ocp create single-node-ignition-config
    ```

7.  Obtain the RHEL `kernel`, `initramfs`, and `rootfs` artifacts from the [Product Downloads](https://access.redhat.com/downloads/content/290) page on the Red Hat Customer Portal or from the [RHCOS image mirror](https://mirror.openshift.com/pub/openshift-v4/s390x/dependencies/rhcos/latest/) page.

    > [!IMPORTANT]
    > The RHCOS images might not change with every release of OpenShift Container Platform. You must download images with the highest version that is less than or equal to the OpenShift Container Platform version that you install. Only use the appropriate `kernel`, `initramfs`, and `rootfs` artifacts described in the following procedure.

    The file names contain the OpenShift Container Platform version number. They resemble the following examples:

    `kernel`
    `rhcos-<version>-live-kernel-<architecture>`

    `initramfs`
    `rhcos-<version>-live-initramfs.<architecture>.img`

    `rootfs`
    `rhcos-<version>-live-rootfs.<architecture>.img`

8.  Before you launch `virt-install`, move the following files and artifacts to an HTTP or HTTPS server:

    - Downloaded RHEL live `kernel`, `initramfs`, and `rootfs` artifacts

    - Ignition files

9.  Create the KVM guest nodes by using the following components:

    - RHEL `kernel` and `initramfs` artifacts

    - Ignition files

    - The new disk image

    - Adjusted parm line arguments

    ``` terminal
    $ virt-install \
       --name <vm_name> \
       --autostart \
       --memory=<memory_mb> \
       --cpu host \
       --vcpus <vcpus> \
       --location <media_location>,kernel=<rhcos_kernel>,initrd=<rhcos_initrd> \
       --disk size=100 \
       --network network=<virt_network_parm> \
       --graphics none \
       --noautoconsole \
       --extra-args "rd.neednet=1 ignition.platform.id=metal ignition.firstboot" \
       --extra-args "ignition.config.url=http://<http_server>/bootstrap.ign" \
       --extra-args "coreos.live.rootfs_url=http://<http_server>/rhcos-<version>-live-rootfs.<architecture>.img" \
       --extra-args "ip=<ip>::<gateway>:<mask>:<hostname>::none" \
       --extra-args "nameserver=<dns>" \
       --extra-args "console=ttysclp0" \
       --wait
    ```

    - For the `--location` parameter, specify the location of the kernel/initrd on the HTTP or HTTPS server.

    - For the `ignition.config.url=` artifact, specify the location of the `bootstrap.ign` config file. Only HTTP and HTTPS protocols are supported.

    - For the `coreos.live.rootfs_url=` artifact, specify the matching `rootfs` artifact for the `kernel` and `initramfs` you are booting. Only HTTP and HTTPS protocols are supported.

    - For the `ip=` parameter, assign the IP address manually as described in "Installing a cluster with RHEL KVM on IBM Z® and IBM® LinuxONE".

</div>

## Installing single-node OpenShift in an LPAR on IBM Z and IBM LinuxONE

You can install single-node OpenShift in an LPAR on IBM Z and IBM LinuxONE.

<div>

<div class="title">

Prerequisites

</div>

- If you are deploying a single-node cluster there are zero compute nodes, the Ingress Controller pods run on the control plane nodes. In single-node cluster deployments, you must configure your application ingress load balancer to route HTTP and HTTPS traffic to the control plane nodes. See the *Load balancing requirements for user-provisioned infrastructure* section for more information.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Set the OpenShift Container Platform version by running the following command:

    ``` terminal
    $ OCP_VERSION=<ocp_version>
    ```

    Replace `<ocp_version>` with the current version. For example, `latest-4.17`.

2.  Set the host architecture by running the following command:

    ``` terminal
    $ ARCH=<architecture>
    ```

    Replace `<architecture>` with the target host architecture `s390x`.

3.  Download the OpenShift Container Platform client (`oc`) and make it available for use by entering the following commands:

    ``` terminal
    $ curl -k https://mirror.openshift.com/pub/openshift-v4/${ARCH}/clients/ocp/${OCP_VERSION}/openshift-client-linux.tar.gz -o oc.tar.gz
    ```

    ``` terminal
    $ tar zxvf oc.tar.gz
    ```

    ``` terminal
    $ chmod +x oc
    ```

4.  Download the OpenShift Container Platform installer and make it available for use by entering the following commands:

    ``` terminal
    $ curl -k https://mirror.openshift.com/pub/openshift-v4/${ARCH}/clients/ocp/${OCP_VERSION}/openshift-install-linux.tar.gz -o openshift-install-linux.tar.gz
    ```

    ``` terminal
    $ tar zxvf openshift-install-linux.tar.gz
    ```

    ``` terminal
    $ chmod +x openshift-install
    ```

5.  Prepare the `install-config.yaml` file:

    ``` yaml
    apiVersion: v1
    baseDomain: <domain>
    compute:
    - name: worker
      replicas: 0
    controlPlane:
      name: master
      replicas: 1
    metadata:
      name: <name>
    networking:
      clusterNetwork:
      - cidr: 10.128.0.0/14
        hostPrefix: 23
      machineNetwork:
      - cidr: 10.0.0.0/16
      networkType: OVNKubernetes
      serviceNetwork:
      - 172.30.0.0/16
    platform:
      none: {}
    pullSecret: '<pull_secret>'
    sshKey: |
      <ssh_key>
    ```

    where:

    `baseDomain`
    Specifies the cluster domain name.

    `compute.replicas`
    Specifies the `compute` replicas to `0`. This makes the control plane node schedulable.

    `controlPlane.replicas`
    Specifies the `controlPlane` replicas to `1`. In conjunction with the previous `compute` setting, this setting ensures the cluster runs on a single node.

    `metadata.name`
    Specifies the cluster name.

    `networking`
    Specifies the `networking` details. OVN-Kubernetes is the only allowed network plugin type for single-node clusters.

    `machineNetwork.cidr`
    Specifies the `cidr` value to match the subnet of the single-node OpenShift cluster.

    `pullSecret`
    Specifies the `pullSecret` parameter. Copy the [pull secret from Red Hat OpenShift Cluster Manager](https://console.redhat.com/openshift/install/pull-secret) and add the contents to this configuration setting.

    `sshKey`
    Specifies the `sshKey` parameter. Add the public SSH key from the administration host so that you can log in to the cluster after installation.

6.  Generate OpenShift Container Platform assets by running the following commands:

    ``` terminal
    $ mkdir ocp
    ```

    ``` terminal
    $ cp install-config.yaml ocp
    ```

7.  Change to the directory that contains the OpenShift Container Platform installation program and generate the Kubernetes manifests for the cluster:

    ``` terminal
    $ ./openshift-install create manifests --dir <installation_directory>
    ```

    Replace `<installation_directory>` with the installation directory that contains the `install-config.yaml` file you created.

8.  Check that the `mastersSchedulable` parameter in the `<installation_directory>/manifests/cluster-scheduler-02-config.yml` Kubernetes manifest file is set to `true`.

    1.  Open the `<installation_directory>/manifests/cluster-scheduler-02-config.yml` file.

    2.  Locate the `mastersSchedulable` parameter and ensure that it is set to `true` as shown in the following `spec` stanza:

        ``` yaml
        spec:
          mastersSchedulable: true
        status: {}
        ```

    3.  Save and exit the file.

9.  Create the Ignition configuration files by running the following command from the directory that contains the installation program:

    ``` terminal
    $ ./openshift-install create ignition-configs --dir <installation_directory>
    ```

    Replace `<installation_directory>` with the same installation directory.

10. Obtain the RHEL `kernel`, `initramfs`, and `rootfs` artifacts from the [Product Downloads](https://access.redhat.com/downloads/content/290) page on the Red Hat Customer Portal or from the [RHCOS image mirror](https://mirror.openshift.com/pub/openshift-v4/s390x/dependencies/rhcos/latest/) page.

    > [!IMPORTANT]
    > The RHCOS images might not change with every release of OpenShift Container Platform. You must download images with the highest version that is less than or equal to the OpenShift Container Platform version that you install. Only use the appropriate `kernel`, `initramfs`, and `rootfs` artifacts described in the following procedure.

    The file names contain the OpenShift Container Platform version number. They resemble the following examples:

    `kernel`
    `rhcos-<version>-live-kernel-<architecture>`

    `initramfs`
    `rhcos-<version>-live-initramfs.<architecture>.img`

    `rootfs`
    `rhcos-<version>-live-rootfs.<architecture>.img`

    > [!NOTE]
    > The `rootfs` image is the same for FCP and DASD.

11. Move the following artifacts and files to an HTTP or HTTPS server:

    - Downloaded RHEL live `kernel`, `initramfs`, and `rootfs` artifacts

    - Ignition files

12. Create a parameter file for the bootstrap in an LPAR:

    <div class="formalpara">

    <div class="title">

    Example parameter file for the bootstrap machine

    </div>

    ``` terminal
    cio_ignore=all,!condev rd.neednet=1 \
    console=ttysclp0 \
    coreos.inst.install_dev=/dev/<block_device> \
    coreos.inst.ignition_url=http://<http_server>/bootstrap.ign \
    coreos.live.rootfs_url=http://<http_server>/rhcos-<version>-live-rootfs.<architecture>.img \
    ip=<ip>::<gateway>:<netmask>:<hostname>::none nameserver=<dns> \
    rd.znet=qeth,0.0.1140,0.0.1141,0.0.1142,layer2=1,portno=0 \
    rd.dasd=0.0.4411 \
    rd.zfcp=0.0.8001,0x50050763040051e3,0x4000406300000000 \
    zfcp.allow_lun_scan=0
    ```

    </div>

    - For the `coreos.inst.install_dev=` artifact, specify the block device on the system to install to. For installations on DASD-type disk use `dasda`, for installations on FCP-type disks use `sda`.

    - For the `coreos.inst.ignition_url=` artifact, specify the location of the `bootstrap.ign` config file. Only HTTP and HTTPS protocols are supported.

    - For the `coreos.live.rootfs_url=` artifact, specify the matching `rootfs` artifact for the `` kernel`and `initramfs `` you are booting. Only HTTP and HTTPS protocols are supported.

    - For the `ip=` parameter, assign the IP address manually as described in "Installing a cluster in an LPAR on IBM Z® and IBM® LinuxONE".

    - For installations on DASD-type disks, use `rd.dasd=` to specify the DASD where RHCOS is to be installed. Omit this entry for FCP-type disks.

    - For installations on FCP-type disks, use `rd.zfcp=<adapter>,<wwpn>,<lun>` to specify the FCP disk where RHCOS is to be installed. Omit this entry for DASD-type disks.

      You can adjust further parameters if required.

13. Create a parameter file for the control plane in an LPAR:

    <div class="formalpara">

    <div class="title">

    Example parameter file for the control plane machine

    </div>

    ``` terminal
    cio_ignore=all,!condev rd.neednet=1 \
    console=ttysclp0 \
    coreos.inst.install_dev=/dev/<block_device> \
    coreos.inst.ignition_url=http://<http_server>/master.ign \
    coreos.live.rootfs_url=http://<http_server>/rhcos-<version>-live-rootfs.<architecture>.img \
    ip=<ip>::<gateway>:<netmask>:<hostname>::none nameserver=<dns> \
    rd.znet=qeth,0.0.1140,0.0.1141,0.0.1142,layer2=1,portno=0 \
    rd.dasd=0.0.4411 \
    rd.zfcp=0.0.8001,0x50050763040051e3,0x4000406300000000 \
    zfcp.allow_lun_scan=0
    ```

    </div>

    For the `coreos.inst.ignition_url=` artifact, specify the location of the `master.ign` config file. Only HTTP and HTTPS protocols are supported.

14. Transfer the following artifacts, files, and images to the LPAR. For example by using FTP:

    - `kernel` and `initramfs` artifacts

    - Parameter files

    - RHCOS images

      For details about how to transfer the files with FTP and boot, see [Installing in an LPAR](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/performing_a_standard_rhel_9_installation/assembly_installing-on-64-bit-ibm-z_installing-rhel#installing-in-an-lpar_installing-in-an-lpar).

15. Boot the bootstrap machine.

16. Boot the control plane machine.

</div>

# Installing single-node OpenShift with IBM Power

You can install a single-node OpenShift cluster with IBM Power by performing a user-provisioned installation.

Installing a single-node cluster on IBM Power® requires user-provisioned installation using the "Installing a cluster with IBM Power®" procedure.

> [!NOTE]
> Installing a single-node cluster on IBM Power® simplifies installation for development and test environments and requires less resource requirements at entry level.

You must meet the following hardware requirements when installing a single-node cluster on IBM Z® and IBM® LinuxONE:

- The equivalent of two Integrated Facilities for Linux (IFL), which are SMT2 enabled, for each cluster.

- At least one network connection to connect to the `LoadBalancer` service and to serve data for traffic outside of the cluster.

> [!NOTE]
> You can use dedicated or shared IFLs to assign sufficient compute resources. Resource sharing is one of the key strengths of IBM Power®. However, you must adjust capacity correctly on each hypervisor layer and ensure sufficient resources for every OpenShift Container Platform cluster.

<div>

<div class="title">

Additional resources

</div>

- [Installing a cluster on IBM Power®](../installing_ibm_power/installing-ibm-power.md#installing-ibm-power)

</div>

## Setting up bastion for single-node OpenShift with IBM Power

Before installing single-node OpenShift on IBM Power®, you must set up bastion.

Setting up a bastion server for single-node OpenShift on IBM Power® requires the configuration of the following services:

- PXE is used for the single-node OpenShift cluster installation. PXE requires the following services to be configured and run:

  - DNS to define api, api-int, and \*.apps

  - DHCP service to enable PXE and assign an IP address to single-node OpenShift node

  - HTTP to provide ignition and RHCOS rootfs image

  - TFTP to enable PXE

- You must install `dnsmasq` to support DNS, DHCP and PXE, httpd for HTTP.

Use the following procedure to configure a bastion server that meets these requirements.

<div>

<div class="title">

Procedure

</div>

1.  Use the following command to install `grub2`, which is required to enable PXE for PowerVM:

    ``` terminal
    grub2-mknetdir --net-directory=/var/lib/tftpboot
    ```

    <div class="formalpara">

    <div class="title">

    Example `/var/lib/tftpboot/boot/grub2/grub.cfg` file

    </div>

    ``` terminal
    default=0
    fallback=1
    timeout=1
    if [ ${net_default_mac} == fa:b0:45:27:43:20 ]; then
    menuentry "CoreOS (BIOS)" {
       echo "Loading kernel"
       linux "/rhcos/kernel" ip=dhcp rd.neednet=1 ignition.platform.id=metal ignition.firstboot coreos.live.rootfs_url=http://192.168.10.5:8000/install/rootfs.img ignition.config.url=http://192.168.10.5:8000/ignition/sno.ign
       echo "Loading initrd"
       initrd  "/rhcos/initramfs.img"
    }
    fi
    ```

    </div>

2.  Use the following commands to download RHCOS image files from the mirror repo for PXE.

    1.  Enter the following command to assign the `RHCOS_URL` variable the follow 4.12 URL:

        ``` terminal
        $ export RHCOS_URL=https://mirror.openshift.com/pub/openshift-v4/ppc64le/dependencies/rhcos/4.12/latest/
        ```

    2.  Enter the following command to navigate to the `/var/lib/tftpboot/rhcos` directory:

        ``` terminal
        $ cd /var/lib/tftpboot/rhcos
        ```

    3.  Enter the following command to download the specified RHCOS kernel file from the URL stored in the `RHCOS_URL` variable:

        ``` terminal
        $ wget ${RHCOS_URL}/rhcos-live-kernel-ppc64le -o kernel
        ```

    4.  Enter the following command to download the RHCOS `initramfs` file from the URL stored in the `RHCOS_URL` variable:

        ``` terminal
        $ wget ${RHCOS_URL}/rhcos-live-initramfs.ppc64le.img -o initramfs.img
        ```

    5.  Enter the following command to navigate to the `/var//var/www/html/install/` directory:

        ``` terminal
        $ cd /var//var/www/html/install/
        ```

    6.  Enter the following command to download, and save, the RHCOS `root filesystem` image file from the URL stored in the `RHCOS_URL` variable:

        ``` terminal
        $ wget ${RHCOS_URL}/rhcos-live-rootfs.ppc64le.img -o rootfs.img
        ```

3.  To create the ignition file for a single-node OpenShift cluster, you must create the `install-config.yaml` file.

    1.  Enter the following command to create the work directory that holds the file:

        ``` terminal
        $ mkdir -p ~/sno-work
        ```

    2.  Enter the following command to navigate to the `~/sno-work` directory:

        ``` terminal
        $ cd ~/sno-work
        ```

    3.  Use the following sample file can to create the required `install-config.yaml` in the `~/sno-work` directory:

        ``` yaml
        apiVersion: v1
        baseDomain: <domain>
        compute:
        - name: worker
          replicas: 0
        controlPlane:
          name: master
          replicas: 1
        metadata:
          name: <name>
        networking:
          clusterNetwork:
          - cidr: 10.128.0.0/14
            hostPrefix: 23
          machineNetwork:
          - cidr: 10.0.0.0/16
          networkType: OVNKubernetes
          serviceNetwork:
          - 172.30.0.0/16
        platform:
          none: {}
        bootstrapInPlace:
          installationDisk: /dev/disk/by-id/<disk_id>
        pullSecret: '<pull_secret>'
        sshKey: |
          <ssh_key>
        ```

        where:

        `baseDomain`
        Specifies the cluster domain name.

        `compute.replicas`
        Specifies the `compute` replicas to `0`. This makes the control plane node schedulable.

        `controlPlane.replicas`
        Specifies the `controlPlane` replicas to `1`. In conjunction with the previous `compute` setting, this setting ensures the cluster runs on a single node.

        `metadata.name`
        Specifies the cluster name.

        `networking`
        Specifies the `networking` details. OVN-Kubernetes is the only allowed network plugin type for single-node clusters.

        `machineNetwork.cidr`
        Specifies the `cidr` value to match the subnet of the single-node OpenShift cluster.

        `bootstrapInPlace.installationDisk`
        Specifies the path to the installation disk drive, for example, `/dev/disk/by-id/wwn-0x64cd98f04fde100024684cf3034da5c2`.

        `pullSecret`
        Specifies the `pullSecret` parameter. Copy the [pull secret from Red Hat OpenShift Cluster Manager](https://console.redhat.com/openshift/install/pull-secret) and add the contents to this configuration setting.

        `sshKey`
        Specifies the `sshKey` parameter. Add the public SSH key from the administration host so that you can log in to the cluster after installation.

4.  Download the `openshift-install` image to create the ignition file and copy it to the `http` directory.

    1.  Enter the following command to download the `openshift-install-linux-4.12.0` .tar file:

        ``` terminal
        $ wget https://mirror.openshift.com/pub/openshift-v4/ppc64le/clients/ocp/4.12.0/openshift-install-linux-4.12.0.tar.gz
        ```

    2.  Enter the following command to unpack the `openshift-install-linux-4.12.0.tar.gz` archive:

        ``` terminal
        $ tar xzvf openshift-install-linux-4.12.0.tar.gz
        ```

    3.  Enter the following command to

        ``` terminal
        $ ./openshift-install --dir=~/sno-work create create single-node-ignition-config
        ```

    4.  Enter the following command to create the ignition file:

        ``` terminal
        $ cp ~/sno-work/single-node-ignition-config.ign /var/www/html/ignition/sno.ign
        ```

    5.  Enter the following command to restore SELinux file for the `/var/www/html` directory:

        ``` terminal
        $ restorecon -vR /var/www/html || true
        ```

        Bastion now has all the required files and is properly configured in order to install single-node OpenShift.

</div>

## Installing single-node OpenShift with IBM Power

You can install single-node OpenShift with IBM Power.

There are two steps for the single-node OpenShift cluster installation. First the single-node OpenShift logical partition (LPAR) needs to boot up with PXE, then you need to monitor the installation progress.

<div>

<div class="title">

Prerequisites

</div>

- You have set up bastion.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Use the following command to boot powerVM with netboot:

    ``` terminal
    $ lpar_netboot -i -D -f -t ent -m <sno_mac> -s auto -d auto -S <server_ip> -C <sno_ip> -G <gateway> <lpar_name> default_profile <cec_name>
    ```

    where:

    sno_mac
    Specifies the MAC address of the single-node OpenShift cluster.

    sno_ip
    Specifies the IP address of the single-node OpenShift cluster.

    server_ip
    Specifies the IP address of bastion (PXE server).

    gateway
    Specifies the Network’s gateway IP.

    lpar_name
    Specifies the single-node OpenShift lpar name in HMC.

    cec_name
    Specifies the System name where the sno_lpar resides

2.  After the single-node OpenShift LPAR boots up with PXE, use the `openshift-install` command to monitor the progress of installation:

    1.  Run the following command after the bootstrap is complete:

        ``` terminal
        ./openshift-install wait-for bootstrap-complete
        ```

    2.  Run the following command after it returns successfully:

        ``` terminal
        ./openshift-install wait-for install-complete
        ```

</div>
