<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

In OpenShift Container Platform version 4.17, you can install a cluster on Red Hat OpenStack Platform (RHOSP) that runs on user-provisioned infrastructure.

Using your own infrastructure allows you to integrate your cluster with existing infrastructure and modifications. The process requires more labor on your part than installer-provisioned installations, because you must create all RHOSP resources, like Nova servers, Neutron ports, and security groups. However, Red Hat provides Ansible playbooks to help you in the deployment process.

# Prerequisites

- You reviewed details about the [OpenShift Container Platform installation and update](../../architecture/architecture-installation.md#architecture-installation) processes.

- You read the documentation on [selecting a cluster installation method and preparing it for users](../overview/installing-preparing.md#installing-preparing).

- You verified that OpenShift Container Platform 4.17 is compatible with your RHOSP version by using the [Supported platforms for OpenShift clusters](../../architecture/architecture-installation.md#supported-platforms-for-openshift-clusters_architecture-installation) section. You can also compare platform support across different versions by viewing the [OpenShift Container Platform on RHOSP support matrix](https://access.redhat.com/articles/4679401).

- You have an RHOSP account where you want to install OpenShift Container Platform.

- You understand performance and scalability practices for cluster scaling, control plane sizing, and etcd. For more information, see [Recommended practices for scaling the cluster](../../scalability_and_performance/recommended-performance-scale-practices/recommended-control-plane-practices.md#recommended-host-practices).

- On the machine from which you run the installation program, you have:

  - A single directory in which you can keep the files you create during the installation process

  - Python 3

# Internet access for OpenShift Container Platform

In OpenShift Container Platform 4.17, you require access to the internet to install your cluster.

You must have internet access to perform the following actions:

- Access Red Hat Hybrid Cloud Console to download the installation program and perform subscription management. If the cluster has internet access and you do not disable Telemetry, that service automatically entitles your cluster.

- Access Quay.io to obtain the packages that are required to install your cluster.

- Obtain the packages that are required to perform cluster updates.

> [!IMPORTANT]
> If your cluster cannot have direct internet access, you can perform a restricted network installation on some types of infrastructure that you provision. During that process, you download the required content and use it to populate a mirror registry with the installation packages. With some installation types, the environment that you install your cluster in will not require internet access. Before you update the cluster, you update the content of the mirror registry.

# Resource guidelines for installing OpenShift Container Platform on RHOSP

To support an OpenShift Container Platform installation, your Red Hat OpenStack Platform (RHOSP) quota must meet the following requirements:

| Resource | Value |
|----|----|
| Floating IP addresses | 3 |
| Ports | 15 |
| Routers | 1 |
| Subnets | 1 |
| RAM | 88 GB |
| vCPUs | 22 |
| Volume storage | 275 GB |
| Instances | 7 |
| Security groups | 3 |
| Security group rules | 60 |
| Server groups | 2 - plus 1 for each additional availability zone in each machine pool |

Recommended resources for a default OpenShift Container Platform cluster on RHOSP

A cluster might function with fewer than recommended resources, but its performance is not guaranteed.

> [!IMPORTANT]
> If RHOSP object storage (Swift) is available and operated by a user account with the `swiftoperator` role, it is used as the default backend for the OpenShift Container Platform image registry. In this case, the volume storage requirement is 175 GB. Swift space requirements vary depending on the size of the image registry.

> [!NOTE]
> By default, your security group and security group rule quotas might be low. If you encounter problems, run `openstack quota set --secgroups 3 --secgroup-rules 60 <project>` as an administrator to increase them.

An OpenShift Container Platform deployment comprises control plane machines, compute machines, and a bootstrap machine.

## Control plane machines

By default, the OpenShift Container Platform installation process creates three control plane machines.

Each machine requires:

- An instance from the RHOSP quota

- A port from the RHOSP quota

- A flavor with at least 16 GB memory and 4 vCPUs

- At least 100 GB storage space from the RHOSP quota

## Compute machines

By default, the OpenShift Container Platform installation process creates three compute machines.

Each machine requires:

- An instance from the RHOSP quota

- A port from the RHOSP quota

- A flavor with at least 8 GB memory and 2 vCPUs

- At least 100 GB storage space from the RHOSP quota

> [!TIP]
> Compute machines host the applications that you run on OpenShift Container Platform; aim to run as many as you can.

## Bootstrap machine

During installation, a bootstrap machine is temporarily provisioned to stand up the control plane. After the production control plane is ready, the bootstrap machine is deprovisioned.

The bootstrap machine requires:

- An instance from the RHOSP quota

- A port from the RHOSP quota

- A flavor with at least 16 GB memory and 4 vCPUs

- At least 100 GB storage space from the RHOSP quota

# Downloading playbook dependencies

The Ansible playbooks that simplify the installation process on user-provisioned infrastructure require several ansible collections and Python modules. On the machine where you will run the installation program, add the Red Hat OpenStack Platform (RHOSP) repositories and then install the packages.

The following dependencies are required:

- Python modules:

  - `openstackclient`

  - `openstacksdk`

  - `netaddr`

  - `pip`

- Ansible collections:

  - `ansible-collections-openstack`, which installs Ansible Core

  - `ansible-collection-community-general`

  - `ansible-collection-ansible-netcommon`

> [!NOTE]
> These instructions assume that you are using Red Hat Enterprise Linux (RHEL) 8.

<div>

<div class="title">

Prerequisites

</div>

- Python 3 is installed on your machine.

</div>

<div>

<div class="title">

Procedure

</div>

1.  On a command line, add the repositories:

    1.  Register with Red Hat Subscription Manager:

        ``` terminal
        $ sudo subscription-manager register # If not done already
        ```

    2.  Pull the latest subscription data:

        ``` terminal
        $ sudo subscription-manager attach --pool=$YOUR_POOLID # If not done already
        ```

    3.  Disable the current repositories:

        ``` terminal
        $ sudo subscription-manager repos --disable=* # If not done already
        ```

    4.  Add the required repositories:

        ``` terminal
        $ sudo subscription-manager repos \
          --enable=rhel-9-for-x86_64-appstream-rpms \
          --enable=rhel-9-for-x86_64-baseos-rpms \
          --enable=openstack-17.1-for-rhel-9-x86_64-rpms
        ```

2.  Install the modules:

    ``` terminal
    $ sudo dnf install ansible-collection-ansible-netcommon \
        ansible-collection-community-general \
        ansible-collections-openstack \
        python3-netaddr \
        python3-openstackclient \
        python3-openstacksdk \
        python3-pip
    ```

3.  Ensure that the `python` command points to `python3`:

    ``` terminal
    $ sudo alternatives --set python /usr/bin/python3
    ```

</div>

# Downloading the installation playbooks

Download Ansible playbooks that you can use to install OpenShift Container Platform on your own Red Hat OpenStack Platform (RHOSP) infrastructure.

<div>

<div class="title">

Prerequisites

</div>

- The curl command-line tool is available on your machine.

</div>

<div>

<div class="title">

Procedure

</div>

- To download the playbooks to your working directory, run the following script from a command line:

  ``` terminal
  $ xargs -n 1 curl -O <<< '
          https://raw.githubusercontent.com/openshift/installer/release-4.17/upi/openstack/bootstrap.yaml
          https://raw.githubusercontent.com/openshift/installer/release-4.17/upi/openstack/common.yaml
          https://raw.githubusercontent.com/openshift/installer/release-4.17/upi/openstack/compute-nodes.yaml
          https://raw.githubusercontent.com/openshift/installer/release-4.17/upi/openstack/control-plane.yaml
          https://raw.githubusercontent.com/openshift/installer/release-4.17/upi/openstack/down-bootstrap.yaml
          https://raw.githubusercontent.com/openshift/installer/release-4.17/upi/openstack/down-compute-nodes.yaml
          https://raw.githubusercontent.com/openshift/installer/release-4.17/upi/openstack/down-control-plane.yaml
          https://raw.githubusercontent.com/openshift/installer/release-4.17/upi/openstack/down-network.yaml
          https://raw.githubusercontent.com/openshift/installer/release-4.17/upi/openstack/down-security-groups.yaml
          https://raw.githubusercontent.com/openshift/installer/release-4.17/upi/openstack/down-containers.yaml
          https://raw.githubusercontent.com/openshift/installer/release-4.17/upi/openstack/inventory.yaml
          https://raw.githubusercontent.com/openshift/installer/release-4.17/upi/openstack/network.yaml
          https://raw.githubusercontent.com/openshift/installer/release-4.17/upi/openstack/security-groups.yaml
          https://raw.githubusercontent.com/openshift/installer/release-4.17/upi/openstack/update-network-resources.yaml'
  ```

</div>

The playbooks are downloaded to your machine.

> [!IMPORTANT]
> During the installation process, you can modify the playbooks to configure your deployment.
>
> Retain all playbooks for the life of your cluster. You must have the playbooks to remove your OpenShift Container Platform cluster from RHOSP.

> [!IMPORTANT]
> You must match any edits you make in the `bootstrap.yaml`, `compute-nodes.yaml`, `control-plane.yaml`, `network.yaml`, and `security-groups.yaml` files to the corresponding playbooks that are prefixed with `down-`. For example, edits to the `bootstrap.yaml` file must be reflected in the `down-bootstrap.yaml` file, too. If you do not edit both files, the supported cluster removal process will fail.

# Obtaining the installation program

Before you install OpenShift Container Platform, download the installation file on the host you are using for installation.

<div>

<div class="title">

Prerequisites

</div>

- You have a computer that runs Linux or macOS, with 500 MB of local disk space.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Go to the [Cluster Type](https://console.redhat.com/openshift/install) page on the Red Hat Hybrid Cloud Console. If you have a Red Hat account, log in with your credentials. If you do not, create an account.

    > [!TIP]
    > You can also [download the binaries for a specific OpenShift Container Platform release](https://mirror.openshift.com/pub/openshift-v4/clients/ocp/).

2.  Select your infrastructure provider from the **Run it yourself** section of the page.

3.  Select your host operating system and architecture from the dropdown menus under **OpenShift Installer** and click **Download Installer**.

4.  Place the downloaded file in the directory where you want to store the installation configuration files.

    <div class="important">

    <div class="title">

    </div>

    - The installation program creates several files on the computer that you use to install your cluster. You must keep the installation program and the files that the installation program creates after you finish installing the cluster. Both of the files are required to delete the cluster.

    - Deleting the files created by the installation program does not remove your cluster, even if the cluster failed during installation. To remove your cluster, complete the OpenShift Container Platform uninstallation procedures for your specific cloud provider.

    </div>

5.  Extract the installation program. For example, on a computer that uses a Linux operating system, run the following command:

    ``` terminal
    $ tar -xvf openshift-install-linux.tar.gz
    ```

6.  Download your installation [pull secret from Red Hat OpenShift Cluster Manager](https://console.redhat.com/openshift/install/pull-secret). This pull secret allows you to authenticate with the services that are provided by the included authorities, including Quay.io, which serves the container images for OpenShift Container Platform components.

    > [!TIP]
    > Alternatively, you can retrieve the installation program from the [Red Hat Customer Portal](https://access.redhat.com/downloads/content/290/), where you can specify a version of the installation program to download. However, you must have an active subscription to access this page.

</div>

# Generating a key pair for cluster node SSH access

During an OpenShift Container Platform installation, you can provide an SSH public key to the installation program. The key is passed to the Red Hat Enterprise Linux CoreOS (RHCOS) nodes through their Ignition config files and is used to authenticate SSH access to the nodes. The key is added to the `~/.ssh/authorized_keys` list for the `core` user on each node, which enables password-less authentication.

The key is added to the `~/.ssh/authorized_keys` list for the `core` user on each node, which enables password-less authentication. After the key is passed to the nodes, you can use the key pair to SSH in to the RHCOS nodes as the user `core`. To access the nodes through SSH, the private key identity must be managed by SSH for your local user.

If you want to SSH in to your cluster nodes to perform installation debugging or disaster recovery, you must provide the SSH public key during the installation process. The `./openshift-install gather` command also requires the SSH public key to be in place on the cluster nodes.

> [!IMPORTANT]
> Do not skip this procedure in production environments, where disaster recovery and debugging is required.

> [!NOTE]
> You must use a local key, not one that you configured with platform-specific approaches.

<div>

<div class="title">

Procedure

</div>

1.  If you do not have an existing SSH key pair on your local machine to use for authentication onto your cluster nodes, create one. For example, on a computer that uses a Linux operating system, run the following command:

    ``` terminal
    $ ssh-keygen -t ed25519 -N '' -f <path>/<file_name>
    ```

    Specifies the path and file name, such as `~/.ssh/id_ed25519`, of the new SSH key. If you have an existing key pair, ensure your public key is in the your `~/.ssh` directory.

    > [!NOTE]
    > If you plan to install an OpenShift Container Platform cluster that uses the RHEL cryptographic libraries that have been submitted to NIST for FIPS 140-2/140-3 Validation on only the `x86_64`, `ppc64le`, and `s390x` architectures, do not create a key that uses the `ed25519` algorithm. Instead, create a key that uses the `rsa` or `ecdsa` algorithm.

2.  View the public SSH key:

    ``` terminal
    $ cat <path>/<file_name>.pub
    ```

    For example, run the following to view the `~/.ssh/id_ed25519.pub` public key:

    ``` terminal
    $ cat ~/.ssh/id_ed25519.pub
    ```

3.  Add the SSH private key identity to the SSH agent for your local user, if it has not already been added. SSH agent management of the key is required for password-less SSH authentication onto your cluster nodes, or if you want to use the `./openshift-install gather` command.

    > [!NOTE]
    > On some distributions, default SSH private key identities such as `~/.ssh/id_rsa` and `~/.ssh/id_dsa` are managed automatically.

    1.  If the `ssh-agent` process is not already running for your local user, start it as a background task:

        ``` terminal
        $ eval "$(ssh-agent -s)"
        ```

        <div class="formalpara">

        <div class="title">

        Example output

        </div>

        ``` terminal
        Agent pid 31874
        ```

        </div>

        > [!NOTE]
        > If your cluster is in FIPS mode, only use FIPS-compliant algorithms to generate the SSH key. The key must be either RSA or ECDSA.

4.  Add your SSH private key to the `ssh-agent`:

    ``` terminal
    $ ssh-add <path>/<file_name>
    ```

    Specifies the path and file name for your SSH private key, such as `~/.ssh/id_ed25519`

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    Identity added: /home/<you>/<path>/<file_name> (<computer_name>)
    ```

    </div>

</div>

<div>

<div class="title">

Next steps

</div>

- When you install OpenShift Container Platform, provide the SSH public key to the installation program.

</div>

# Creating the Red Hat Enterprise Linux CoreOS (RHCOS) image

The OpenShift Container Platform installation program requires that a Red Hat Enterprise Linux CoreOS (RHCOS) image be present in the Red Hat OpenStack Platform (RHOSP) cluster. Retrieve the latest RHCOS image, then upload it using the RHOSP CLI.

<div>

<div class="title">

Prerequisites

</div>

- The RHOSP CLI is installed.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Log in to the Red Hat Customer Portal’s [Product Downloads page](https://access.redhat.com/downloads/content/290).

2.  Under **Version**, select the most recent release of OpenShift Container Platform 4.17 for Red Hat Enterprise Linux (RHEL) 8.

    > [!IMPORTANT]
    > The RHCOS images might not change with every release of OpenShift Container Platform. You must download images with the highest version that is less than or equal to the OpenShift Container Platform version that you install. Use the image versions that match your OpenShift Container Platform version if they are available.

3.  Download the *Red Hat Enterprise Linux CoreOS (RHCOS) - OpenStack Image (QCOW)*.

4.  Decompress the image.

    > [!NOTE]
    > You must decompress the RHOSP image before the cluster can use it. The name of the downloaded file might not contain a compression extension, like `.gz` or `.tgz`. To find out if or how the file is compressed, in a command line, enter:
    >
    > ``` terminal
    > $ file <name_of_downloaded_file>
    > ```

5.  From the image that you downloaded, create an image that is named `rhcos` in your cluster by using the RHOSP CLI:

    ``` terminal
    $ openstack image create --container-format=bare --disk-format=qcow2 --file rhcos-${RHCOS_VERSION}-openstack.qcow2 rhcos
    ```

    > [!IMPORTANT]
    > Depending on your RHOSP environment, you might be able to upload the image in either [`.raw` or `.qcow2` formats](https://access.redhat.com/documentation/en-us/red_hat_openstack_platform/15/html/instances_and_images_guide/index). If you use Ceph, you must use the `.raw` format.

    > [!WARNING]
    > If the installation program finds multiple images with the same name, it chooses one of them at random. To avoid this behavior, create unique names for resources in RHOSP.

</div>

After you upload the image to RHOSP, it is usable in the installation process.

# Verifying external network access

The OpenShift Container Platform installation process requires external network access. You must provide an external network value to it, or deployment fails. Before you begin the process, verify that a network with the external router type exists in Red Hat OpenStack Platform (RHOSP).

<div>

<div class="title">

Prerequisites

</div>

- [Configure OpenStack’s networking service to have DHCP agents forward instances' DNS queries](https://docs.openstack.org/neutron/rocky/admin/config-dns-res.html#case-2-dhcp-agents-forward-dns-queries-from-instances)

</div>

<div>

<div class="title">

Procedure

</div>

1.  Using the RHOSP CLI, verify the name and ID of the 'External' network:

    ``` terminal
    $ openstack network list --long -c ID -c Name -c "Router Type"
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    +--------------------------------------+----------------+-------------+
    | ID                                   | Name           | Router Type |
    +--------------------------------------+----------------+-------------+
    | 148a8023-62a7-4672-b018-003462f8d7dc | public_network | External    |
    +--------------------------------------+----------------+-------------+
    ```

    </div>

</div>

A network with an external router type appears in the network list. If at least one does not, see [Creating a default floating IP network](https://access.redhat.com/documentation/en-us/red_hat_openstack_platform/16.0/html/director_installation_and_usage/performing-overcloud-post-installation-tasks#creating-a-default-floating-ip-network) and [Creating a default provider network](https://access.redhat.com/documentation/en-us/red_hat_openstack_platform/16.0/html/director_installation_and_usage/performing-overcloud-post-installation-tasks#creating-a-default-provider-network).

> [!NOTE]
> If the Neutron trunk service plugin is enabled, a trunk port is created by default. For more information, see [Neutron trunk port](https://wiki.openstack.org/wiki/Neutron/TrunkPort).

# Enabling access to the environment

At deployment, all OpenShift Container Platform machines are created in a Red Hat OpenStack Platform (RHOSP)-tenant network. Therefore, they are not accessible directly in most RHOSP deployments.

You can configure OpenShift Container Platform API and application access by using floating IP addresses (FIPs) during installation. You can also complete an installation without configuring FIPs, but the installer will not configure a way to reach the API or applications externally.

## Enabling access with floating IP addresses

Create floating IP (FIP) addresses for external access to the OpenShift Container Platform API, cluster applications, and the bootstrap process.

<div>

<div class="title">

Procedure

</div>

1.  Using the Red Hat OpenStack Platform (RHOSP) CLI, create the API FIP:

    ``` terminal
    $ openstack floating ip create --description "API <cluster_name>.<base_domain>" <external_network>
    ```

2.  Using the Red Hat OpenStack Platform (RHOSP) CLI, create the apps, or Ingress, FIP:

    ``` terminal
    $ openstack floating ip create --description "Ingress <cluster_name>.<base_domain>" <external_network>
    ```

3.  By using the Red Hat OpenStack Platform (RHOSP) CLI, create the bootstrap FIP:

    ``` terminal
    $ openstack floating ip create --description "bootstrap machine" <external_network>
    ```

4.  Add records that follow these patterns to your DNS server for the API and Ingress FIPs:

    ``` dns
    api.<cluster_name>.<base_domain>.  IN  A  <API_FIP>
    *.apps.<cluster_name>.<base_domain>. IN  A <apps_FIP>
    ```

    > [!NOTE]
    > If you do not control the DNS server, you can access the cluster by adding the cluster domain names such as the following to your `/etc/hosts` file:
    >
    > - `<api_floating_ip> api.<cluster_name>.<base_domain>`
    >
    > - `<application_floating_ip> grafana-openshift-monitoring.apps.<cluster_name>.<base_domain>`
    >
    > - `<application_floating_ip> prometheus-k8s-openshift-monitoring.apps.<cluster_name>.<base_domain>`
    >
    > - `<application_floating_ip> oauth-openshift.apps.<cluster_name>.<base_domain>`
    >
    > - `<application_floating_ip> console-openshift-console.apps.<cluster_name>.<base_domain>`
    >
    > - `application_floating_ip integrated-oauth-server-openshift-authentication.apps.<cluster_name>.<base_domain>`
    >
    > The cluster domain names in the `/etc/hosts` file grant access to the web console and the monitoring interface of your cluster locally. You can also use the `kubectl` or `oc`. You can access the user applications by using the additional entries pointing to the \<application_floating_ip\>. This action makes the API and applications accessible to only you, which is not suitable for production deployment, but does allow installation for development and testing.

5.  Add the FIPs to the `inventory.yaml` file as the values of the following variables:

    - `os_api_fip`

    - `os_bootstrap_fip`

    - `os_ingress_fip`

</div>

If you use these values, you must also enter an external network as the value of the `os_external_network` variable in the `inventory.yaml` file.

> [!TIP]
> You can make OpenShift Container Platform resources available outside of the cluster by assigning a floating IP address and updating your firewall configuration.

## Completing installation without floating IP addresses

You can install OpenShift Container Platform on Red Hat OpenStack Platform (RHOSP) without providing floating IP addresses.

In the `inventory.yaml` file, do not define the following variables:

- `os_api_fip`

- `os_bootstrap_fip`

- `os_ingress_fip`

If you cannot provide an external network, you can also leave `os_external_network` blank. If you do not provide a value for `os_external_network`, a router is not created for you, and, without additional action, the installer will fail to retrieve an image from Glance. Later in the installation process, when you create network resources, you must configure external connectivity on your own.

If you run the installer with the `wait-for` command from a system that cannot reach the cluster API due to a lack of floating IP addresses or name resolution, installation fails. To prevent installation failure in these cases, you can use a proxy network or run the installer from a system that is on the same network as your machines.

> [!NOTE]
> You can enable name resolution by creating DNS records for the API and Ingress ports. For example:
>
> ``` dns
> api.<cluster_name>.<base_domain>.  IN  A  <api_port_IP>
> *.apps.<cluster_name>.<base_domain>. IN  A <ingress_port_IP>
> ```
>
> If you do not control the DNS server, you can add the record to your `/etc/hosts` file. This action makes the API accessible to only you, which is not suitable for production deployment but does allow installation for development and testing.

# Defining parameters for the installation program

The OpenShift Container Platform installation program relies on a file that is called `clouds.yaml`. The file describes Red Hat OpenStack Platform (RHOSP) configuration parameters, including the project name, log in information, and authorization service URLs.

<div>

<div class="title">

Procedure

</div>

1.  Create the `clouds.yaml` file:

    - If your RHOSP distribution includes the Horizon web UI, generate a `clouds.yaml` file in it.

      > [!IMPORTANT]
      > Remember to add a password to the `auth` field. You can also keep secrets in [a separate file](https://docs.openstack.org/os-client-config/latest/user/configuration.html#splitting-secrets) from `clouds.yaml`.

    - If your RHOSP distribution does not include the Horizon web UI, or you do not want to use Horizon, create the file yourself. For detailed information about `clouds.yaml`, see [Config files](https://docs.openstack.org/openstacksdk/latest/user/config/configuration.html#config-files) in the RHOSP documentation.

      ``` yaml
      clouds:
        shiftstack:
          auth:
            auth_url: http://10.10.14.42:5000/v3
            project_name: shiftstack
            username: <username>
            password: <password>
            user_domain_name: Default
            project_domain_name: Default
        dev-env:
          region_name: RegionOne
          auth:
            username: <username>
            password: <password>
            project_name: 'devonly'
            auth_url: 'https://10.10.14.22:5001/v2.0'
      ```

2.  If your RHOSP installation uses self-signed certificate authority (CA) certificates for endpoint authentication:

    1.  Copy the certificate authority file to your machine.

    2.  Add the `cacerts` key to the `clouds.yaml` file. The value must be an absolute, non-root-accessible path to the CA certificate:

        ``` yaml
        clouds:
          shiftstack:
            ...
            cacert: "/etc/pki/ca-trust/source/anchors/ca.crt.pem"
        ```

        > [!TIP]
        > After you run the installer with a custom CA certificate, you can update the certificate by editing the value of the `ca-cert.pem` key in the `cloud-provider-config` keymap. On a command line, run:
        >
        > ``` terminal
        > $ oc edit configmap -n openshift-config cloud-provider-config
        > ```

3.  Place the `clouds.yaml` file in one of the following locations:

    1.  The value of the `OS_CLIENT_CONFIG_FILE` environment variable

    2.  The current directory

    3.  A Unix-specific user configuration directory, for example `~/.config/openstack/clouds.yaml`

    4.  A Unix-specific site configuration directory, for example `/etc/openstack/clouds.yaml`

        The installation program searches for `clouds.yaml` in that order.

</div>

# Creating network resources on RHOSP

Create the network resources that an OpenShift Container Platform on Red Hat OpenStack Platform (RHOSP) installation on your own infrastructure requires. To save time, run supplied Ansible playbooks that generate security groups, networks, subnets, routers, and ports.

<div>

<div class="title">

Prerequisites

</div>

- You downloaded the modules in "Downloading playbook dependencies".

- You downloaded the playbooks in "Downloading the installation playbooks".

</div>

<div>

<div class="title">

Procedure

</div>

1.  For a dual stack cluster deployment, edit the `inventory.yaml` file and uncomment the `os_subnet6` attribute.

2.  To ensure that your network resources have unique names on the RHOSP deployment, create an environment variable and JSON file for use in the Ansible playbooks:

    1.  Create an environment variable that has a unique name value by running the following command:

        ``` terminal
        $ export OS_NET_ID="openshift-$(dd if=/dev/urandom count=4 bs=1 2>/dev/null |hexdump -e '"%02x"')"
        ```

    2.  Verify that the variable is set by running the following command on a command line:

        ``` terminal
        $ echo $OS_NET_ID
        ```

    3.  Create a JSON object that includes the variable in a file called `netid.json` by running the following command:

        ``` terminal
        $ echo "{\"os_net_id\": \"$OS_NET_ID\"}" | tee netid.json
        ```

3.  On a command line, create the network resources by running the following command:

    ``` terminal
    $ ansible-playbook -i inventory.yaml network.yaml
    ```

    > [!NOTE]
    > The API and Ingress VIP fields will be overwritten in the `inventory.yaml` playbook with the IP addresses assigned to the network ports.

    > [!NOTE]
    > The resources created by the `network.yaml` playbook are deleted by the `down-network.yaml` playbook.

</div>

# Creating the installation configuration file

You can customize the OpenShift Container Platform cluster you install on Red Hat OpenStack Platform (RHOSP).

<div>

<div class="title">

Prerequisites

</div>

- You have the OpenShift Container Platform installation program and the pull secret for your cluster.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create the `install-config.yaml` file.

    1.  Change to the directory that contains the installation program and run the following command:

        ``` terminal
        $ ./openshift-install create install-config --dir <installation_directory>
        ```

        - `<installation_directory>`: For `<installation_directory>`, specify the directory name to store the files that the installation program creates.

          When specifying the directory:

        - Verify that the directory has the `execute` permission. This permission is required to run Terraform binaries under the installation directory.

        - Use an empty directory. Some installation assets, such as bootstrap X.509 certificates, have short expiration intervals, therefore you must not reuse an installation directory. If you want to reuse individual files from another cluster installation, you can copy them into your directory. However, the file names for the installation assets might change between releases. Use caution when copying installation files from an earlier OpenShift Container Platform version.

    2.  At the prompts, provide the configuration details for your cloud:

        1.  Optional: Select an SSH key to use to access your cluster machines.

            > [!NOTE]
            > For production OpenShift Container Platform clusters on which you want to perform installation debugging or disaster recovery, specify an SSH key that your `ssh-agent` process uses.

        2.  Select **openstack** as the platform to target.

        3.  Specify the Red Hat OpenStack Platform (RHOSP) external network name to use for installing the cluster.

        4.  Specify the floating IP address to use for external access to the OpenShift API.

        5.  Specify a RHOSP flavor with at least 16 GB RAM to use for control plane nodes and 8 GB RAM for compute nodes.

        6.  Select the base domain to deploy the cluster to. All DNS records will be sub-domains of this base and will also include the cluster name.

        7.  Enter a name for your cluster. The name must be 14 or fewer characters long.

2.  Modify the `install-config.yaml` file. You can find more information about the available parameters in the "Installation configuration parameters" section.

3.  Back up the `install-config.yaml` file so that you can use it to install multiple clusters.

    > [!IMPORTANT]
    > The `install-config.yaml` file is consumed during the installation process. If you want to reuse the file, you must back it up now.

</div>

You now have the file `install-config.yaml` in the directory that you specified.

<div>

<div class="title">

Additional resources

</div>

- [Installation configuration parameters for OpenStack](installation-config-parameters-openstack.md#installation-config-parameters-openstack)

</div>

## Custom subnets in RHOSP deployments

Optionally, you can deploy a cluster on a Red Hat OpenStack Platform (RHOSP) subnet of your choice. The subnet’s GUID is passed as the value of `platform.openstack.machinesSubnet` in the `install-config.yaml` file.

This subnet is used as the cluster’s primary subnet. By default, nodes and ports are created on it. You can create nodes and ports on a different RHOSP subnet by setting the value of the `platform.openstack.machinesSubnet` property to the subnet’s UUID.

Before you run the OpenShift Container Platform installer with a custom subnet, verify that your configuration meets the following requirements:

- The subnet that is used by `platform.openstack.machinesSubnet` has DHCP enabled.

- The CIDR of `platform.openstack.machinesSubnet` matches the CIDR of `networking.machineNetwork`.

- The installation program user has permission to create ports on this network, including ports with fixed IP addresses.

Clusters that use custom subnets have the following limitations:

- If you plan to install a cluster that uses floating IP addresses, the `platform.openstack.machinesSubnet` subnet must be attached to a router that is connected to the `externalNetwork` network.

- If the `platform.openstack.machinesSubnet` value is set in the `install-config.yaml` file, the installation program does not create a private network or subnet for your RHOSP machines.

- You cannot use the `platform.openstack.externalDNS` property at the same time as a custom subnet. To add DNS to a cluster that uses a custom subnet, configure DNS on the RHOSP network.

> [!NOTE]
> By default, the API VIP takes x.x.x.5 and the Ingress VIP takes x.x.x.7 from your network’s CIDR block. To override these default values, set values for `platform.openstack.apiVIPs` and `platform.openstack.ingressVIPs` that are outside of the DHCP allocation pool.

> [!IMPORTANT]
> The CIDR ranges for networks are not adjustable after cluster installation. Red Hat does not provide direct guidance on determining the range during cluster installation because it requires careful consideration of the number of created pods per namespace.

## Sample customized install-config.yaml file for RHOSP

The following example `install-config.yaml` files demonstrate all of the possible Red Hat OpenStack Platform (RHOSP) customization options.

> [!IMPORTANT]
> This sample file is provided for reference only. You must obtain your `install-config.yaml` file by using the installation program.

<div class="example">

<div class="title">

Example single stack `install-config.yaml` file

</div>

``` yaml
apiVersion: v1
baseDomain: example.com
controlPlane:
  name: master
  platform: {}
  replicas: 3
compute:
- name: worker
  platform:
    openstack:
      type: ml.large
  replicas: 3
metadata:
  name: example
networking:
  clusterNetwork:
  - cidr: 10.128.0.0/14
    hostPrefix: 23
  machineNetwork:
  - cidr: 10.0.0.0/16
  serviceNetwork:
  - 172.30.0.0/16
  networkType: OVNKubernetes
platform:
  openstack:
    cloud: mycloud
    externalNetwork: external
    computeFlavor: m1.xlarge
    apiFloatingIP: 128.0.0.1
fips: false
pullSecret: '{"auths": ...}'
sshKey: ssh-ed25519 AAAA...
```

</div>

<div class="example">

<div class="title">

Example dual stack `install-config.yaml` file

</div>

``` yaml
apiVersion: v1
baseDomain: example.com
controlPlane:
  name: master
  platform: {}
  replicas: 3
compute:
- name: worker
  platform:
    openstack:
      type: ml.large
  replicas: 3
metadata:
  name: example
networking:
  clusterNetwork:
  - cidr: 10.128.0.0/14
    hostPrefix: 23
  - cidr: fd01::/48
    hostPrefix: 64
  machineNetwork:
  - cidr: 192.168.25.0/24
  - cidr: fd2e:6f44:5dd8:c956::/64
  serviceNetwork:
  - 172.30.0.0/16
  - fd02::/112
  networkType: OVNKubernetes
platform:
  openstack:
    cloud: mycloud
    externalNetwork: external
    computeFlavor: m1.xlarge
    apiVIPs:
    - 192.168.25.10
    - fd2e:6f44:5dd8:c956:f816:3eff:fec3:5955
    ingressVIPs:
    - 192.168.25.132
    - fd2e:6f44:5dd8:c956:f816:3eff:fe40:aecb
    controlPlanePort:
      fixedIPs:
      - subnet:
          name: openshift-dual4
      - subnet:
          name: openshift-dual6
      network:
        name: openshift-dual
fips: false
pullSecret: '{"auths": ...}'
sshKey: ssh-ed25519 AAAA...
```

</div>

## Setting a custom subnet for machines

The IP range that the installation program uses by default might not match the Neutron subnet that you create when you install OpenShift Container Platform. If necessary, update the CIDR value for new machines by editing the installation configuration file.

<div>

<div class="title">

Prerequisites

</div>

- You have the `install-config.yaml` file that was generated by the OpenShift Container Platform installation program.

- You have Python 3 installed.

</div>

<div>

<div class="title">

Procedure

</div>

1.  On a command line, browse to the directory that contains the `install-config.yaml` and `inventory.yaml` files.

2.  From that directory, either run a script to edit the `install-config.yaml` file or update the file manually:

    - To set the value by using a script, run the following command:

      ``` terminal
      $ python -c 'import os
      import sys
      import yaml
      import re
      re_os_net_id = re.compile(r"{{\s*os_net_id\s*}}")
      os_net_id = os.getenv("OS_NET_ID")
      path = "common.yaml"
      facts = None
      for _dict in yaml.safe_load(open(path))[0]["tasks"]:
          if "os_network" in _dict.get("set_fact", {}):
              facts = _dict["set_fact"]
              break
      if not facts:
          print("Cannot find `os_network` in common.yaml file. Make sure OpenStack resource names are defined in one of the tasks.")
          sys.exit(1)
      os_network = re_os_net_id.sub(os_net_id, facts["os_network"])
      os_subnet = re_os_net_id.sub(os_net_id, facts["os_subnet"])
      path = "install-config.yaml"
      data = yaml.safe_load(open(path))
      inventory = yaml.safe_load(open("inventory.yaml"))["all"]["hosts"]["localhost"]
      machine_net = [{"cidr": inventory["os_subnet_range"]}]
      api_vips = [inventory["os_apiVIP"]]
      ingress_vips = [inventory["os_ingressVIP"]]
      ctrl_plane_port = {"network": {"name": os_network}, "fixedIPs": [{"subnet": {"name": os_subnet}}]}
      if inventory.get("os_subnet6_range"):
          os_subnet6 = re_os_net_id.sub(os_net_id, facts["os_subnet6"])
          machine_net.append({"cidr": inventory["os_subnet6_range"]})
          api_vips.append(inventory["os_apiVIP6"])
          ingress_vips.append(inventory["os_ingressVIP6"])
          data["networking"]["networkType"] = "OVNKubernetes"
          data["networking"]["clusterNetwork"].append({"cidr": inventory["cluster_network6_cidr"], "hostPrefix": inventory["cluster_network6_prefix"]})
          data["networking"]["serviceNetwork"].append(inventory["service_subnet6_range"])
          ctrl_plane_port["fixedIPs"].append({"subnet": {"name": os_subnet6}})
      data["networking"]["machineNetwork"] = machine_net
      data["platform"]["openstack"]["apiVIPs"] = api_vips
      data["platform"]["openstack"]["ingressVIPs"] = ingress_vips
      data["platform"]["openstack"]["controlPlanePort"] = ctrl_plane_port
      del data["platform"]["openstack"]["externalDNS"]
      open(path, "w").write(yaml.dump(data, default_flow_style=False))'
      ```

      - Applies to dual stack (IPv4/IPv6) environments.

</div>

## Emptying compute machine pools

To proceed with an installation that uses your own infrastructure, set the number of compute machines in the installation configuration file to zero. Later, you create these machines manually.

<div>

<div class="title">

Prerequisites

</div>

- You have the `install-config.yaml` file that was generated by the OpenShift Container Platform installation program.

</div>

<div>

<div class="title">

Procedure

</div>

1.  On a command line, browse to the directory that contains `install-config.yaml`.

2.  From that directory, either run a script to edit the `install-config.yaml` file or update the file manually:

    - To set the value by using a script, run:

      ``` terminal
      $ python -c '
      import yaml;
      path = "install-config.yaml";
      data = yaml.safe_load(open(path));
      data["compute"][0]["replicas"] = 0;
      open(path, "w").write(yaml.dump(data, default_flow_style=False))'
      ```

    - To set the value manually, open the file and set the value of `compute.<first entry>.replicas` to `0`.

</div>

## Cluster deployment on RHOSP provider networks

You can deploy your OpenShift Container Platform clusters on Red Hat OpenStack Platform (RHOSP) with a primary network interface on a provider network. Provider networks are commonly used to give projects direct access to a public network that can be used to reach the internet. You can also share provider networks among projects as part of the network creation process.

RHOSP provider networks map directly to an existing physical network in the data center. A RHOSP administrator must create them.

In the following example, OpenShift Container Platform workloads are connected to a data center by using a provider network:

<figure>
<img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAABfAAAAUYCAIAAABoT2TPAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAyZpVFh0WE1MOmNvbS5hZG9iZS54bXAAAAAAADw/eHBhY2tldCBiZWdpbj0i77u/IiBpZD0iVzVNME1wQ2VoaUh6cmVTek5UY3prYzlkIj8+IDx4OnhtcG1ldGEgeG1sbnM6eD0iYWRvYmU6bnM6bWV0YS8iIHg6eG1wdGs9IkFkb2JlIFhNUCBDb3JlIDYuMC1jMDA2IDc5LmRhYmFjYmIsIDIwMjEvMDQvMTQtMDA6Mzk6NDQgICAgICAgICI+IDxyZGY6UkRGIHhtbG5zOnJkZj0iaHR0cDovL3d3dy53My5vcmcvMTk5OS8wMi8yMi1yZGYtc3ludGF4LW5zIyI+IDxyZGY6RGVzY3JpcHRpb24gcmRmOmFib3V0PSIiIHhtbG5zOnhtcD0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wLyIgeG1sbnM6eG1wTU09Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC9tbS8iIHhtbG5zOnN0UmVmPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvc1R5cGUvUmVzb3VyY2VSZWYjIiB4bXA6Q3JlYXRvclRvb2w9IkFkb2JlIFBob3Rvc2hvcCAyMi40IChNYWNpbnRvc2gpIiB4bXBNTTpJbnN0YW5jZUlEPSJ4bXAuaWlkOjRBN0NERkY5QzYzQjExRUJBRDhERDhDMzQ3RkI2NDdEIiB4bXBNTTpEb2N1bWVudElEPSJ4bXAuZGlkOjRBN0NERkZBQzYzQjExRUJBRDhERDhDMzQ3RkI2NDdEIj4gPHhtcE1NOkRlcml2ZWRGcm9tIHN0UmVmOmluc3RhbmNlSUQ9InhtcC5paWQ6NEE3Q0RGRjdDNjNCMTFFQkFEOEREOEMzNDdGQjY0N0QiIHN0UmVmOmRvY3VtZW50SUQ9InhtcC5kaWQ6NEE3Q0RGRjhDNjNCMTFFQkFEOEREOEMzNDdGQjY0N0QiLz4gPC9yZGY6RGVzY3JpcHRpb24+IDwvcmRmOlJERj4gPC94OnhtcG1ldGE+IDw/eHBhY2tldCBlbmQ9InIiPz7pqhGHAAG1z0lEQVR42uzd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WIbhEzfkb968+YknnpBx3WAwyMhktVozMzNvvPHGsWPHpqenV1RULF++fN68efv375dtkDJSUsqfd955Q4cODeFmSLuys/X19bGxsd27dw8+9ekn7d69++DBg7JK//79g5eXlJSsWbNGfelkt9svu+yyOXPmBC7w3NDQsH79etm1JUuWSCc/++yzvXv3Dl5dBR31XJ60/hbIe1RVVVVbW+tyuWSY79atW9euXVvfbKfTKe+xrCI1d+rU6SfLAwCAEJKBW/LDCU1ZJ0O7NpvtueeeO+2001SeKSgo+O9//ysBSVqX4Cfx6eOPPx48ePCRjr+WKKiuPyiFU1JSevTocaRjiyQlquDUluOa215tQGVlpXSdxCfZZglarZc/cOCANCEBLy0trW/fvm3vrrq6uj179siTPn36yLrHv6fHszESjIuLi2V/JRvr9Xo+swAQQRmjpqbGqAaME/cNgNfrlTG+qalJnWklQ/6pp576zjvvBGZGunbtesYZZ0yaNOnqq6/euXNnTEyM0WiU8s8//7wUCwwtTz755Pr16+VVu93+i1/84qabbtq6devixYu3bdtmMpnOOeecyy+//Ei3ypLh/J///KcUVlcslnghg9Z555131113NZug2bFjx4MPPqgObZWGXnzxRdn++++//5tvvpHOkjHyrLPOeuyxx4YPH67Kl5eXSz+qCR23233HHXcEb0NSUtJFfh999NEPP/wgmx0YO6UVGXdlNwNHIMsTaUgCh7QoAeJPf/qTJI8o/yXxvvKTPZWcIflMcoZsoeSMoUOHSouBjWm2y6+99tqnn34quyxbHh8f36lTJ8lS11133dixY9vyxr399tsSv6Qh+fWQRHjbbbcFth8AALSF3k/74yw0blci0MiRIyUjqR8vvvjia6+99vHHH3/11VfVjJI8SqaaMmVKv379Aqts375dstl3331XXFwsWUXSkWywZK1evXpNmzZtxowZgfO5Pvnkk7feeksyyZYtW1Rwkkd5fsUVV6jANmHChFtuueVoqw22cuXK119/fcOGDZK1HA6HpKZTTjnl0ksvvf7661vGy5ycnH/961+bNm0qKyvzeDydO3eWPCkbIymr2eRLcHyVsPrQQw+9/PLL//73v4uKiuRV2aRf//rX99xzT+DSB23f0+PcGMmQEmgl7P3tb38rLCyUYCyhsU+fPnxmASCy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szlSUsrffffdh00hUmb9+vV//etfi4uL6+vrv//++1tuuWXVqlVqXRl6f/7zn6tU8bOf/axr165ut1tGu/379997773B18TZtm3bypUrj38Hn3vuuU2bNn300Udjxox54YUXAscKKd99993bb7+t0oDL5ZLc0KtXr+AZluBDbPbu3duscukTNcsjo7Vs/x133HHxxRfLDl5//fUjRoxoeRFleVX6QR2YY7Va//CHPwTqrKmpufHGGx9//PEj7YiUl+hzww03yJuipoRKSkpuu+02i8XCpwUAgGMgiWXp0qUnLmWdJO1K6ti8efN6v7Vr17777rtTp06dPXu2miiJ8h8jE3yHBwknZWVl0dHRkkSzs7Nff/31iRMnSoa57LLLfv/738taRzohKLBcImJ1dXWzYkdbraTEoUOHqjQl0XHhwoWvvvpq4NUlS5bI6gUFBYH8OWrUKHU/Cik8d+7c3Nzc4NoWLFigElRItL6nGm8MAODkzBhffvmlUQ3Dh72fVKicc845DzzwwGOPPaYO0omLiysuLp41a1Z6enpGRoa6frCMsrJc3ULSYrE8+eSTRzrfSmqw2+2PPPLIK6+80qlTpwMHDtTW1qoLD8vyHj16zJgxQ5Xs2bPn9OnT//73v6ekpEiB+fPnS1uyJC0tbevWre+8846s+Pzzz1977bXHvGuLFi365z//qfZLKn/ooYdeeumlgQMHSoyQAbiwsPC7776T3TGbzbJrVqt18uTJwUcJyXgsw7A6cEaePP744zt37oyPj5edkqrS/NRbI7WtW7du2rRp6puuffv27dixo+URPWeeeeaYMWNkq5KTk6VCWUWyyPnnny8lV69era4SLY3efffdzQ7tifrxykRPPfXURj9pSLYkLy/v4YcffuGFF/jAAABwtNSV6U5oyjoZ2pVocddddwUOoFbBRn3TJs/r6+vHjx8vyS1QXt0AVF6SeFNVVSVhSZ0Xb7PZvvrqK4lzRzphPHDGliSr7du3X3nllRdeeOHu3btHjBghGekYqr3hhhskNalvwmRF2cilS5f269evpKREIlBdXd1VV131n//8R12rURKjPG9sbJTWJdRdffXV11133bBhw6TYsmXLpJ6xY8dKLJRwe/xd2vqearwxAICTNmNodIfCe+65p6mpac6cOdHR0TLwqDOPGhoaampqjMb/v9OWjKMOh8Pl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d/Xq1fJcWlFNSCVSYY8ePW6//XY1S6UuCx046SywqVH+88LU1jbbd6lE9veRRx6RYlLm4MGDbbnBOQAAAAAAOKno5X/18p/8jvO/eoPBYLPZHnjgge3btycnJ8uOu93ugQMHDhkyJDo62uVyxcfHWyyWxx57rLS0tOUttEwmU2Fh4datWxMSEqTrAidwxcXF7dq16/PPP1erSD1XXnll//79HQ5HY2OjTqfr2rVrWlqaOmJIfoyNjZXNePXVV6VAy2kXvV6fm5srlZjN5sC1nNUVfz788MPKykrZC9ly2c6Ghgar1RqoQZ7Ij41+TU1NzS6gEyDbIMWO9CoAAAgJr5/2KStc7QIAAC3HemN6err85z82NraD7LbZbP7000/VPZ5UF9x3330zZswwmUy5ubnyvLq6OiYmprCw8L333nvggQeandil7u19/fXXT5061e12//Of/1yxYoU648lgMGzcuFEVczqd3bt3nz59+uLFi6dMmTJixAjpZ8lVBQUFs2fPLioqio6OlrXUTSj69evXbCOl0ezs7FmzZvXt23fTpk1z5syxWq1Sv6y1f//+vXv3dunSJSkpSZbL9kgl8kRdUNlut99///2DBg1yOBxSPjMzs+WlmgEAgDZSU1Pr6+u1T1nhahcAAGg21jc1NRlHjhwp//mPj4/vCPus0+m8Xu+iRYvUc5vNNnHixHvvvdfpdHo8nsmTJzc0NNxxxx1GozE6OnrFihU333xz8J2novwzJsOHD3/uuef0er0U6969+/fff19VVaVOdKqurg4uOWPGjOuvvz4jIyPqx/uIDRkyRB6lWp/PZzAYampqZJWBAwc2207ZngceeGD69OkWi0XeoLKyspdeeikuLk5dO1lE+WemLrnkkoSEhOTkZLfbrbZTnowYMeLnP/+5rBjlv1M7h+EAABAugwYNysrK0j5lhatdAACg5VivbqvdUa6kYzAYysvLi4qK1C7r9frU1NRFixbZbDZ1i/HGxsa0tDR5jI6OPnDgwP79+wcMGBBcg8/nk3gk9ahZlV69evXt21eKqQqDT57yeDxSeUxMjFTe0NDgcrli/U499dTk5GSLxSKVuP0Ou6lSxmq1qg0bMWLESy+9pJYH3/5cXeIncNVk9ar8KNsWfJcuAAAQruARllmVcLULAAC0HOuNHW2fa2tr6+vr1U2dzGbzhx9++O67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bN/Ksle6REREZLO6PjIyUnrjxo2UlJT8/HyWCBEREVENSk5OTkpKsn0ry17pEhERkc3q+pSUFLlMJjOZTBKJhCVCREREVIOkUikaWrZvZdkrXSIiIrJlXc9JkYmIiIiIiIiIahkO6BARERERERER1TJyFgERERERERFVxBciE92nB/oEtBwfUYPBwFImIiIiqvGOkF1aWWzdEVGNKCgoKCsr44RcRPdTI7u7uysUigdU18s7dOiQl5fn4eHBsiYiIiKqQUFBQS4uLrZvZdkrXSKqY3Q6HQd0iO6HyewB1fUajUYeHBzMUiYiIiKqcf5m9SddIqpjJL9jURA5ZhuDkyITEREREREREdUyHNAhIiIiIiIiIqplfhvQ4dTlRERERA+CvVpZbN0RERHV+TaGNCYm5ujRo1qtlsVBREREVINiY2MPHz5s+1aWvdIlIiIim9X1R48eld64cSM5ObmgoIAlQkRERFSD0MRKSkqyfSvLXukSERGRzep6kMtkMt6US0RERFTjpFIpGlr1J10iIiKyZV3PSZGJiIiIiIiIiGoZDugQEREREREREdUychYBERGRI7t7925ZWRkWfHx8VCpVVcF0Ol1GRgYWlEplw4YNsZCVlVVaWiqVSvGnXP4nanyj0Zienu5kfntCo0aNKt0XWULGsODq6urh4VFpPMhASUmJQqFABpCNSsNkZmZqtVqJRFJxE1L38vJSq9XiTxwLIqwqJI4a5VPpViIiIqI6SYo2kMFgYEEQERE5pvXr17du3bpt27bz5s2rPhjCICQWxJopU6aEhob26tUrNjb2T6X4448/hoWFdenSpU2bNl999VWlYaKjo5FceHh4//7909LSKg2DDISEhAwfPjwrK6vSAHl5eU888USHDh06derUsYJWrVrt3LnTEhg5QYrIVcWQyOeoUaPEsJdDsVcri607IiKiuk3U9VK0otDYquq3NSIiIrKvJ5980tXVtays7KeffsrPz680jE6n2759e2lpqZub21NPPWVZqdVqseOfffvBN998U2Km1+u3bNmCeCptRiBy/Hv58uXp06dXlSuRgaoSwtaCggIEMBqNcvlvL2oox/qOGxy7iE3MAlhOVXcA2VdQUFBoaKjtW1n2SpeIiIhsVteHhITIg4ODWRbWxJ3taEGikeri4tKgQYOq2qCZmZmWhmbjxo3RlBQ3t4uV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06aBgYFpvwsJCfHx8UGjYfv27SLRqkybNq1Pnz5Y2LRp03fffXcviXbq1OnQoUMbN248evQo/p09e/YH/w979wEeVbH3DzzbN71BEmoKBAihKFUQQhdUlKoUURRFUK+IXjt6vVhRlBfrtSL2gpeigHQpIbQAAVJIgJBCQjppu8n2/5edv/vmTTPgsrtJvh948mzOzjkzZ06b3+ScOS+/vGXLlueffx5XYVxA33zzTYPBIBK/9957a9eu/fXXX3fu3PnWW2+98MILn3322aZNm3A1dHd3R46Yzp2EiIiIWg926NRv4MCB119/vU6nUygUOTk5aG6K6fn5+Xv37kUr02g0olV966231js7mryzZ88eOnQoPnh4ePz+++9okh46dAgtTo1GM3Xq1JiYmCt9FQgUFhbee++9qampcrncbDY/+eSTzW5sSCIiumodO3YcM2aMxWI5efLk0aNHMSU5OTk+Ph4fxo8fj6vS31k4lpOQkIDLSlFREZZ2/Z8mT56s1WpxLUtKSoqLi2tkCUizYsWKoKAgg8Hwwgsv4JqlVqv/ohUilfbq1WvGjBkhISG2iUql8rnnnhs1apREIsGaZmZmiul+fn647I4YMaLmywQw+7Jly8RlsaGRm4mIiIhaJHbo1E+lUk2ZMkX8VRANx/Xr14vpf/zxB1qWCoWiurp69OjRaFvXO7vJZPL393/00UfdrPerl5WVvf322+L2HLRHH3rooat46ypaxvfcc48YU7miomLx4sX1Dt9DREQt2J133imuQWKUYlyeLl26hOvC378irFmzRqvV4pKH5Uv+L3Evql6vb2hoZJvevXs///zzbtbheJ599llcraTSq2xpjBgxAvPi2peXl9d4yr59+3bu3NloNIpXfRERERG1ElKz2Xx1z/60eBMnTmzbti0aiCqV6tChQxkZGW7W91uhaSsGPJ4+fXojs2s0mptuumnIkCFoH4vmLGbE5zlz5oSHh1/p7TloE99///27d+/29PTE50cfffTll1/mNiIiam2GDx/eu3dvXIb27t2bl5e3bds2XMf79OkzePDgv7PYoqIiLAofunTp8uuvv27+v37++WfxqNfOnTsvXrzY+KLmzZs3bdo0lBBXzPj4+Ka82LFepaWlWDUvq8ZT4pIquqJw1Xa17YV6cEory1n5EhERkSOv9dK+fft269bN19eXNVJL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rgkhGUL9lJSUX3/9NT4+PjMzs7y8HPF8aGjogAEDbr/99qioKJ1O10gvgOOJ4WM3bty4YcOGs2fPFhQUILYMCgpq167dwIEDx40bhzIjgV6vl0qlWq32448/Pn78eEhIyLJlyxrqhVEoFNhrH3jgAVTF8OHDV61ahUowGo0SiQQLefnllzEFdSW6imJiYqZOnWqbV2Llsg/OoNhZWVnHjh07ffr09OnTu3XrhrWom0ytVq9du/ajjz5CS/3LL78cMWIEqs5hhUQll5SUJCcnY4OOGjUqPDycpw5XhrMEK4HIuXBpxkXK8adKZ+VLREREjrzWX37+BSEu/8zuyuRyObbR+++//8knn+Tn54uhYaCgoODcuXO7d+/+5ptvFixYMH/+fKTERnWR7omqqqoXX3zxl19+qa6uRpnd3d1R5pycnBMnTuzYsQPrctNNNz388MNdunTB7ldZWbl69erz58+PGzeukSdEFApFbm5uamqqUqlMTk4uLCz09/fHKqtUqqNHjyIvT0/PkJCQWbNmYSFRUVGiT0Tc/oN2LXJx2bcUYRU2btz46quvoszDhg2Ljo6ut0MH65WRkZGQkOCUFVGr1WvWrHn99dexTdeuXdu9e/cWEy2IQZeu7lsXJAbQwTF47c7tqBAceuKBSjtuBVv5eeanlkHyp1aSLxERETnyWs9BkV2dTCZD1LRkyZLvv/9e3KfTp0+fG264oX379rm5uUeOHDl+/HhJScmrr76anp7+2muvIY0r3KeDcr733nvffvuth4dHVFTUpEmTunbtigjw3LlzKHN8fHxpaelXX33VpUuXxYsXiyd3vLy8lEpl489bVVdX9+rV66GHHtq6des999wTFhYmej0QVSYmJiJ8xYdFixYtXLhQp9NptVosGVMw/eeff963b1+bNm1EZ4TL9imIwYawERsZzlk8meWsQmLvEo/ONV7IZgdVin21oc7Exr91zfM7DgEcHdconBNdtDioKyoqMjMz/34u2K+wTDHGFvYrceTyYTEiIiIiokawQ8fVIXJ+8803v/32W4SU3t7ezz///OTJk318fMTNOIimNmzYsGzZskuXLiFNu3btnnnmGY1G4+S9Si7Pzc1dv369UqkMDw9ftWpVz549bd1MKN7BgwffeustBGz33nsvws6mx8kI+VAhL7300lNPPeXp6Ymoz9anUFZWJpaD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zsqXiIiIHHatt1gscl7s7WjQoEG8vZmopeLZkoiulLM6gtkBTURE1BraGLwXl/EeERERERERETUz/AMOEREREREREVEzI83JyTl37pzRaGRdEBEREdlRUVHRmTNnHN/Kcla+RERE5LBr/blz5+QHDhwwGAy+vr5t2rRhpRARERHZS3JycmZmpr+/v4NbWc7Kl4iIiBx2rc/JyZGKFzOxOoiIiIjsSyKROKWV5ax8iYiIyJHXeo6hQ0RERERERETUzLBDh4iIiIiIiIiomWGHDhERERERERFRMyM1m80mk4kVQURERGRfFovFKa0sZ+VLREREjrzWy3v16lVWVubj48MaISIiIrKjsLAwhULh+FaWs/IlIiIih13rVSqVvEePHqwLIiIiIrvrbNV68iUiIiJHXus5hg4RERERERERUTPDDh0iIiIiIiIiomaGHTpERERERERERM2MNCkp6cCBA3q9nnVBREREZEcZGRmxsbGOb2U5K18iIiJy2LX+wIED0pSUFHwqLy9njRARERHZUWZm5vnz5x3fynJWvkREROSwa31GRoZcKpXKZDJWBxEREZF9OauVxdYdOVJ1dXV+fn5WVlZhYWFJSYlWq9VoNJgukUi8vb09PT0DAgJCQkI6d+4cGBioUChYY0RE9rrWy1kRRERERER0RcrLy48fP56cnJyamlpSUqLT6QwGg5u1HwcsFov4aTabEXUolUqVShUSEhIVFdWrV6/evXtjCuuQiOhvYocOERERERE1VWpqamxs7JEjR4qLi81ms7gdDB8sFotUKlUoFHL55RADvxqt8MFgMCBBenp6Wlra77//3qFDhyFDhgwbNiwkJIT1SUR01dihQ0REREREf+3s2bMbNmw4fvx4VVWVXC6XSCSYqFKp/Pz8wsPDO3TogA8+Pj7e3t74ymg0VlRUVFZW5ufn5+TkZGVllZeXi/6d7Ozs8+fPb9myJSYm5tZbbw0MDGTdEhFdBbnZbDaZTKwIIiIiIvtyViuLrTuyu8rKyv/+9787d+7UaDRKpVIikUil0vDw8AEDBkRHR4eGhqrV6saXUFFRcebMmcTExPj4+IsXL8pkMixz/fr1Bw4cmDx58vjx41nJRERXeq2X9+rVq6yszMfHhzVCREREZEcIdxH6Or6V5ax8qaVKSkr68ssv09PTVSqVVCqVSCSDBw8eN25c7969mz78tre3dz+radOmxcfH//HHH1isXC6/dOnSp59+euzYsblz57Zv3561TUTUxGu9Wq2W9+jRg3VBREREZHedrVpPvtQibdq06ccff9TpdEql0mg09uvX77bbbuvVq9dVL9DT03PEiBExMTFxcXHr1q07f/48lhwfH5+VlbVw4cK+ffuyzomImnit5xg6RERERERUj2+//XbdunVKpdJsNvv4+MyaNWvMmDF2WbJEIrnxxhuvu+66//73v1u2bJHL5SUlJW+//fbcuXPHjh3Lmiciagp26BARERER0f9hMpk+/vjjnTt3qtVqnU4XFRU1f/780NBQ++bi6el5zz339O7d+/PPPy8oKDAajZ9++ml1dfXEiRO5CYiI/pKUVUBERERERDV99913O3bscHd31+l0w4cPf+655+zem2Nz/fXXL1mypEuXLgaDQS6Xf/XVVzt37uQmICL6S9Lk5OQDBw7o9XrWBREREZEdZWRkxMbGOr6V5ax8qcX49ddfN2zY4OHhUVVVNW7cuEcffdTT0/Oa5ti+ffunn366W7du2G/lcvmqVauOHz/ODUFE1Mi1/sCBA/Lk5GSDwRAZGdmmTZtmVHqLxWI2m7kViYiIyGVlZmZmZWX16NHDwa0sZ+VLLUNCQsIPP/ygUqmqq6tHjx49f/78pr/K6u8ICAh48skn33rrrXPnzkml0k8//fTll19u27YttwgRUb3X+tzcXDlOl445R9uRRCIpKyvjJiSiFsBiseCcxnogapGc1cpqjq07chEVFRWrV682mUxmszk6Ovr+++935L4UEBDw2GOPLV269NKlSwUFBV988cXTTz+N/ZnbhYio3mt9cx0UGSEQNyERERER0VWorq4uKCi4cOFCaWmpRqORSCRoXXt4eKSmpubk5CBI8Pf3f+SRR9zd3R1csHbt2j344IPLly9XqVRHjhzZtWsXX3pFRNQQvuWKiIiIiKhV0Gg0R48ePXHixJkzZ0pLS/V6vcFgMJlMokPn8h975XKlUonpc+fODQ4Odkoh+/Xrd8stt6xfv16hUKxdu3bAgAF+fn7cdkREdbFDh4iIiIiohcvPz9++ffvBgwfxwWw2iwep8EE8+StufsdPk8mk1WpHjRo1dOhQJ5Z22rRpCQkJFy5cyMvL++233+6++25uQSKiuuQ4j+PEzYogIiIisi9ntbLYuqOaDAbD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4Qe3292/f385oguL1uVySVk5nc5hw4b5I7n33nubNWt24sSJRYsWVbdjjx49/v73vyuKsmTJkg8//LA2abVt21auEynzwYMHy1n78ssvX375Zdly8ODBxx57bMaMGecVDAAavHMjdDwezwWvLwAAAIDqBKuWVX9qd9Kev93HYrGcOnUqOzt73759K3x27Nghze+lS5fGxMRIazw5Ofnw4cNZWVlNmjRZt25d69atH3nkkcmTJ69cuVKCbd26tbS0VIK1aNGiurT8MyiXn0pZ4szIyJBs3H///ZKQf3u0T/ndNRpN+WW85dOkpKTt27fb7faQuNhSU1P79es3f/78ZcuW/eUvfwkPD//555+lkI1G4y233HLB0UokGzdulJKR8n/77bfVybalTGRLYWHhDz/8MGnSpOpG39x3331r1qz56quvpk2bdvXVV0dERNSc1oABA+TUl5WVlX9ySuK/66675IL54IMPxo0bJ5dHLYPx+4M6JL+oGh+119j/OCcQ5DqG/MguX75cfqApDgAAgDq0e/fuJUuWBL6WFax0ayaN+TZt2kir/qGHHpo7d+5jjz1mMBgkq+qsxs2bN+/cubPdbt+6devevXv379/fvXv30aNHJyUlyZb8/PwdO3ZIsCuvvNK/EFUtFRYWFhcX63S69u3b/2bg8j1Bal05rNzSV/Wc5HPcuHF6vX7fvn1Sw5ct33//vRx+hw4dhg0bdsHRysmSa0las999992TTz75lM9zzz135MgRs9ksp6+GEUySpVdeeUVK/syZM08//fTJkyf9k/tUJyoqqsI8OPLnI488Imfw8OHDBw8ePK9gCBVer1cu3ZhywsPD68lCzJKxyMhIyYx8EeQLZbFY5MKWHzTm5EbQ6xjLly9X5IfV5XKVlZWV/xcJAAAA/E5nz57Nz88PfC0rWOlW5nQ6T58+3bJly8ofjRo16rXXXnO73ercxmG+p66+++67rVu3Wq1W2VH+lPz36dPn888/nz9/vjTRzWbzlVdeWcuuDf/72NjY6OhoaYbt27dPnVinAbv22mvbtWuXkZGxcOHCP/zhD0uXLpVW6DXXXFN+aNJ5kXJbsmSJVqvt2rVrz549/cu9Swk7HA756MSJE3PmzOnXr191McjZf/XVV9UZjl555RWj0VjdmvE18Oe/5hZ+LYOhHjIYDIcPH543b546N5b8AqSl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M4uKirp3767X6ykOYbPZwnyDl7xer+JTQ0h1PLPH4zGZTPLe6XS63W51o+wuG6vcUcI7HA5/sJpTUe3Zs0fO1KlTp8xmc2JiYufOnS+99FJOFgAA9dnRo0ePHTt2+eWXB7iWFax0AQBAwO71J06cUHbt2uV0OpOTk+Pj4ykU8e67737wwQeRkZF2u71jx45z5sypsl9mxowZr776anh4uM1m69u372effSZ1psmTJ69atUo2SgCr1Tpx4sSpU6dW3leCpaenm81mNdiECRNeeOGF6vLz448/fvLJJ9u2bSstLS0rK1MUReKXkzV+/PinnnoqNjaWUwYAQP106NChnJyctm3bBriWFax0AQBAwO71x44d0wqdTkdx+F111VUFBQW5ubmnT59OT0/fsmVL5TBOp/Obb7455nP48OFBgwap/wJ25swZ2fGoj+w+c+ZMKeUK+27YsOG7777Ly8tTg0l4Sa7KnMhH99xzz+23375ixQp1NJDRaDQYDPLRqVOnpk2bNmHChMLCQk4ZAAD1k9y7g1LLCla6AAAgkPd65tCpqGfPngMGDPB4PEaj0eVyLVy4sHKY3bt379mzJyoqKsy3Wth1112nblcUxfCr8PDwvLy86dOnV9j3vffes9vtJpPJH7K6KtcXX3zx2Wefmc1mvV4v+UlNTR05cqS8Op1O2RIbG7t06dJ3332XUwYAAAAAQGNDh05FOp1u7NixLpdL3huNxuXLlxcXF1cI8+OPP8pGCWm324cPH96qVasqozKbzd988035QTobNmxYsmSJ+kzWb3rooYcmTJiQn5/funXrL7/88qeffpozZ468Tp061e12q3P0SGxlZWWcNQAAAAAAGhU6dKowbNiwli1bOp1Og8GQmZm5cePG8p+WlZX973//U0fNSIBx48ZVjsHjI2FOnTpVfpDOe++9J7trtVq32/2b2YiLi/voo4+eeeaZWbNmXX/99ZGRkbJRXp988skePXrYbDadTldaWlpSUsIpAwAAAACgUdF6PJ7adC40KgkJCUOHDrXb7fJeCmf+/PnlP92yZcsvv/xiNBolQJcuXfr161dhdynSmJiYyMhI2VcdpHPw4MGwcsNzJEB0dHRtchIREfHqq6+mpaVV2G4ymbxer8vlivPhlAEAUA8Fq5ZF7Q4AgMZQx9B26NAhISFBnQ4GfmPHjlWntjEYDOnp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umaNwWAwGo02m83lctXPPEuGpTEsOXQ6nV6vVw5B8qzX6+UoyudZwkRERMhByfaax0FIDKdPn/7ll1969OgRGxvrj0TtLZo3b156evrx48fNZvOECROGDBkiEYbK+VVPqByg1WqV46quv0btyZK2uhyynP0ADxuRRCWHcgbVq45OpXpLTk1xcbGcowbcswkAAAA06i4CiiBU2mZms/nEiRPLly/ftGnTgQMHCgsLY2Nj27Vr17dv36FDh7Zo0aKsrKxePRKi0+mk2b9t27aFCxfu3btXMu/xeJo3b56YmCh5HjhwYMuWLR0OhzQ4tVqtzWabN2/ezp07o6Ojn3nmmep6YaRpmpeXN3ny5K1bt44YMeLdd981mUxut1s+krRee+21t99+W1KRaGVLamrq8OHDy0clxVhvn5qRQsjPz8/Kyjp06NCgQYOklKqczNJoNC5btuzzzz/PzMyUw7/yyivlvAfyOpTkcnNzc3JyunbtKlddve1JhCgqKqLHDQAAAGioFLcPBVGf6Xy+/fbbd95558CBA9KE9vhotdotW7bI9nbt2j3++ONjxoypP2dT8iY5/Oc//zlz5syCggLJlTpMYM+ePXIsX331VUJCgmT4rrvuio+Pl8DFxcWvvvrq4cOHhwwZIiGr69AxGAyHDh3asGGDyWRas2bN0aNHU1NTJXKj0ZiRkfHpp59KgNjY2GuuuUbasfKR2t2gPooV5lurqN5e7XJEP/zwwyuvvFJSUiJv5JxW2aEjhSNluHjxYnkT+AEyZrP5iy++eO211+R8ffPNN0lJSQ2pQ6fmzr7QmkBHLgw5NWVlZRfvCpECUXtjmacDqIHcCoNy3wlWugAAIJD3eiUlJUXaZlFRUZRI/aROPfP666+/9957aidO+/bte/Tocckll5w+fXrXrl2HfB5//PEDBw48/fTT0sqqD4srS8t/+vTpb7/9tsFgSEhIGDx4cLt27SRjkknJc2Zm5pEjR1599VX5VPLsdDql2RkZGak+QVZDy9lut3fs2HHcuHHp6em3335769at1V4PaVLu2LFDrmRFUaZMmfLUU085HI6SkhIJLzHL+1WrVm3YsEFy9ac//anePoQlGZPDiYiIkKOorhBku16vV/ungjL4wmKxSDmrzfiGNO10zROIhtz0opJh9dnMi3SRqI9PtmnTprS09NSpU79/mh61eyjM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jx45ckQpy8rKNmzYoE/NQ6Yef/xxpe/Ro8f5558/d+7cw4cPT506VWXr3bu3/vbs2bNz584qreJ8M7zIe0e0+tatW++44w59esUVV+j1nj179FdbePfdd7UF03ul/VIZtClFlQomDxw4UFxcbO730UaUo9KoPIWFhaGhoUoZHh5u+pJU1H379pl+Is+wHUMliY+P10Z279793Xff3XLLLeYQqFpUY0r51VdfXXnllS3c41ZWrFixc+fOvn37al+0oio2NTVVq6i0KkP79u2jo6OzsrJ0LGbOnKnyz5o1KyIiQhsxhd+/f7++dw8//PCuXbsGDhyoaqyzeysyMvLLL7+8++67dRBHjBjx0EMPtW7dunbniBkG9cQTTygXM46mX79+qluttXbt2ltvvfWZZ54xh8/s0b///W+VPy4ubujQoTqOqh+VZ926dXfeeaepZB0+JVNdTZ8+/b333jNl06FZs2aNKkHVbkZyeXpzVEUPPPBAaWnpoEGDdIh1LNLS0jZu3KgflnHjxrVq1arhdOjYGuT9ByqV/ufbeyO0wVOrdu877LQFz2zQem2GpHn36ZinaNXozTEregavmSlyag+IM18lnSQ6S3USJiQknO4OnYZz9LkNplnRT7F+9s844wyLW1n+yhcAAFh2rVfIaVcgqthPcamZEAENKMyz2fLcFCDp6CiYNzF5bYqX9KnSKKVZxYRSasZFRERs375dYfaf/vQnhUx79uyZN2/e1q1bP//888jIyBkzZph47OjRo48++mh2drZSPv3008OHD9fCjIyMRx55ZNWqVY8//vjAgQO7du1qojjF9nqh6Gv27NnmORra2sMPP2xe3HzzzcpIUdyDDz6ozS5evLiysjLDzdy4FBUV1aFDhyuuuOL66683Q1e8d/nYsWPKdPz48Up5+PDhadOmzZ8/X2fqJ5980r9/f5PYTNxjt9v1VgV46623tOTDDz9855139Kl2RE1Y1ZXOaiX77LPPVCGPPfbY/v37zzrrLL0oKyvTXmhF724Ula1ly5bDhg1bvXr1zp071Q6OjY1VvLpixQqT16ZNmw4cOBAXF1dcXLxmzRptQbnobXl5uZJpswpKVdu//vWvb7rpJtWttqCaXLhw4bfffvviiy8qgclORVVG+t4pry+++EKFLCws1Io1bnfSFj766KP//d//zczMHDNmjI6Uue+s9oTEoaGhqpxXX31VW+7Zs6cOhApWVVX11VdfqQAKmHX4VHVmZqWwsDAdl/T09IsuukhHUFsrKipS8ebMmaNKVo7mfj2dFVpL9al9T0xMvPzyy3v37q0EKrDOB/OMLc8hU83rqP3iF794/fXXtSPaTR24d999t1evXjoTvG/48rtKp6uFrcE9mavC6apw+rhDJ1CbPcEguHrotOnXr5++6fpJWbp0qU5ynVHt2rVr4e4n3bZtm75Kpk/HO+X333+v08zT76OTSiebvuPm8Tr6SD8s+nbom1Jj4mSdPPrI3IxpwUzbOvpVzgZx9KtdXN+aEV1QdP7ry2JxK8tf+QIAAMuu9QcPHrQ3usfxNh9m9hYJ+FH9iQ0zhsWzXEGUgvm5c+d27NjRTCc8fvz422+/fe3atfPmzbvyyivPP/98raVIXkF+aGiowvirrrrKTBBz7rnn/vWvfx03bpxOlM8+++zee+/1DvzuuusuBXsFBQVa/ZprrlmyZMkHH3xw5MgRJe7WrVtJSYniwNdee22B265du/bt21dUVKTyKPjXWps3b9byWbNmxcbGejZbVlaWkpLym9/8RikrKys7dep0zz33rFixQmFkRkZG7RletadhYWFnn312eHj4qlWrzJAExZkjR45UAcxsNdpIZmZmcHCw3prBR2YGYpWkxv1reqtNvfLKK/v379+6dav2IjU1dcuWLa1bt1bkqfKrzFq4Y8eOPXv2KP5UYjML8ldffWW6eFSfTzzxhDJSSQYMGPDSSy9de+212sjHH398/fXX9+jR4z8BfEWFXj///PM6KKWlpeamJO/CREREfPnll//7v/976NChsWPHvvDCCzWmwvEOiVWZb775plZv06bNjBkzhg4dqtpTwW677Tb9ffjhh7X7npmVtJFzzjnnoosu8sxs3bZtW6X84osvDhw4sH37dtWY6mrlypU6mjpbzjrrrL/97W8qrY64dvnmm2++77779JF3GRTqqxiK3lVsMytzly5dHnjgAZNdw/lChTts172xe92uihZBDWuExPEejRa+DvGdAVP7lfWLtpX/zBlpdPj0O6ATMi4urm/fvp5/2+/cuXP79u2XLVuWm5trLhkmpbmV7z95Op06DQYNGuQdQCqNvuP64mzYsMGcKjVOYKkxUu/0HP3Aa1/ftSMvuyH06B0urGrhYNbnZnQp90sri9Yd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XpFRwDQ6zec67pdWFq07AACaQxvDPnjwYIXWZpw8GhrFxoMGDbrxxhtfeOEFhUz33XdfQUHB5ZdfHh4ebuL24uLi999///HHH1cgraj79ttvV/qSkhJPNOVwODIyMubNmzdq1Cgt1CHXa7O19u3bX3TRRWZQyciRI9u0aaNI7Jlnnunfv398fLyZAScnJ2fLli1Dhw79WZOhKOxfsGDB008/rVNLud92220dO3Y0U9iYYr/xxhubN29WyqSkJOV1uhudntu4lJF5RFcL961ntfuntNfd3FS8Tz/9VOm1761atdJHqqKvv/56/vz55eXlnTt37t27t6kT7ZTq9rXXXtOxePnll5OTkxMSEsz800uWLPnwww+VS69evbS8/pDY+5upunrqqaeOHTv2wQcfLF68+P7773/uuefMvM61O3SU3dlnn7137961a9e+/fbbkyZNMk+bVuX/7W9/y8rK0utf/vKX2nEz35C2HxMTExsbq3PG9EnpI++5M7X6JZdcMnv27Pz8/L/+9a8tW7bU6iEhIVp9zZo1qgRzInnCflWIjnK/fv20PCwsLDIycuLEiabnq0HNoaOj3bFVUEBgg3uCbxt7UFl5tW97PeyBgUVZjoI8n22w/uKZXkuT5iTPc78c/ahoR0MoTGhQQAtG6DQb+v1v27at9a0sf+ULAAAsu9YrorcrNKUuGjJFy1OnTt29e/enn36al5d33333zZ07d/jw4R06dDh06NCqVasUxpuHYV1xxRVKWWMch2Lso0eP/uY3vzGz1Wo7GzZsUFSv5Q888EBiYqKZDqNPnz433HCDovfNmzfrxY033piUlHTkyBHltXTp0kcfffT666/3nrq4fgrtfvjhh8LCQgV4f//737/++uvRo0cPGDBAoX5OTs7ixYvnz5+vqC88PPzWW28NDg4+rR065klYDodDu5yRkfHSSy916tSptLR0xIgR5vFSNRKr+Tto0KCNGzfqo8DAwJEjR5oZglSB+khVZx7YbB5QZQ6Q0o8fP/61115bv379r3/9a1Vgu3btlNecOXMOHz6sjdx2220xMTEnH+iauZafeuqpoqKir776at68earSGTNm1L5pxfRJTZo0aeHCharbJ598cseOHdo1lfOzzz5TzWsvhg4dOm7cOC1RVZ9xxhlaqKP8/vvvX3bZZdrsgQMH3nrrraysLM/GtUc6H3Qu/eEPf9DJ89vf/nb27Nk9e/ZUGjP9s/chU61q9T/96U9jx44dM2ZMQkKCtvnNN99s2rRJL1SSBvVtqnS6HA3vqS/lVa6KU5rAuB7O46OorBsAYm7kNF8Zfa9r3KbnmWjZ70e/gRxxHlverLR3az75AgAAK6/1zKHT0ClGCgkJ+etf/5qYmDhnzpwjR44sc/Pc9mImQr7xxhsnT56slDXGRCiMVzzftWvXuXPnLlq0SEvCwsI6duyoKP26667zPApKMfzdd99dUFDw9ttvr127NjU1tVWrVoWFhSUlJYrzFy5cOG7cOK2ovJTSzKBhhoF4wjnv5cr0pptuio2Nfemll9LS0rZv356RkRHsphxVwqCgoLi4uEceeeSCCy4w44m0O0VFRRUVFXrrHfjVXl5nyhMVzLyNiYlJSUnZuHFjTk6OMtUWVGP//ve/o6Oja/dSmVmQ//a3v2n7PXr06Nu3r4lUVf/du3dXzSvNsGHDPCGreTjUAw88kJeX98knn6xZs2b9+vU6EKanLDIycurUqRMmTDA1eaLdrL0LSqN1X3jhhUmTJn399dfvvPOOEjz55JMqeY091dsBAwY8++yzDz300IEDB2bNmqXzRB9puXJMTk5+5plnWrZsqYOicl5zzTX/+te/0tPTdbhfffVVHZGtW7eax4qVuJlSKfEtt9yi46J6yMzMXL58uXZcb3UaqNK0opkXSdG7dsdM9/PGG298+OGHrVu31kdZWVna5pgxY5TdiWb/wenmGYxmAX0ddE7m5+fr/NQZ0q5dO502OmHM/N86T8wAvYZw7xUAAADQZAQ+9thjp2/rCgtrRNe+Ehoa6n2TSKMo8ylTIKTY7LzzzktJSVFkbiasVQTVvn17RfJXXHHF9OnTJ0yY0MI9suM/x9UdaSvAPnLkSN++fWfPnj1w4MAuXboMGjTouuuuu//++88555zS0lLPPUdmytILLrigZ8+eJgLX6nFxcYMHD546deq9996rCjfVovpp1arVWWedNXLkSL0wHSK1l6sk/fv3v/TSS3v16hUWFhYSEqKUykWRnsqs0v7hD38wZTCrax8rKyuTkpKGDx+uono2W2N5tVudKessmKcCk5OTlUa1oXVVGL295JJLtFO1p+9RIaOiolTJffr0URrVuZlBRmtFREQoXh06dOhVV12l1551zaTRv/jFLxISElR7ZsBUp06dzj333IcfflgVbmaGPtFuejp0vHdBUbEZxKTslPUZZ5zRwt0LqywUOdfYU21TR1lniDkHtB3VuVaZOHGi6lmrmGmJlXubNm2Utbag47tnzx5loYP++OOPa8s9evTwlMrcpDZkyJCLLroo0e3CCy+cPHnylClTVJjIyEiTuypKxdYWunXrZu7DOnbsmFbv16/fjTfeOG3aNKVsUJM4nL7fjYb2m2Nmqjp69Gj9c1rX/qnRt14niY6+Tg8zhblZHh8fr5PNs1wLa6Q0fXxmiJa+JjrBzLdb57BOxQ4dOmRnZ5+oT0fLW7durQ3q9b59+7Tuzyr2Se5a165d9b1oCEf8zRXH9hwuPz45t9N14zkxXdoE0xYBAADAKQg4rQ/byM3NNU9T8u1mVWa1/k/Tvz+fpjL74FAFBAQHBytsVgmPz6JaUaEaUEStyN88tcr7UCpZVlbW//zP/2zdulWh+AcffKBYy/yDuQJsrVvn5Cb6VAGPwjBlob8K3bVxxWN6bboeTL+GmfpUQZc24hk1U+dyu91uBg2ZeVK1EVNmRYamzN5ZR0REKNjWcqX0HnpTY3mdKU9UAA+VRLuvkFKf6nXLli3reeyUgkllob/ajueBPspClaNDoBdaWDsLpVcCbf/YsWPaNdWbwlrl5d1xdqLdrL8OtSmTpqSkxExjXOeeqmza8uHDh82W9R3R4asxI7VJpuBWob4Kpu20a9dOiVU5dZZKy81mzUAkz5POvXPXp1qikF47rhKqHqLdTN9Ww/kG1f+7Uf9tQaf1pqHT8Zujg5KTk2NufDv5tXS8zjzzzMTERH1VFy1apIKZ/i8zmVTnzp09y1UhtVPqvNLC7t27mxozHTqqcHM3X2pqqn6O6nzWlbbfo0eP5ORkvV66dGlmZqbPH4mlLEaNGhUTE9MQTsXzn9u2eHN+i2Bbi/LqRdN6nZcUSVsEAAAAp8C+cuVKxWBqrHuCRjRMZkZbMxNKbGyswj8zt0thYeFPrqtkngdL1Z9FcXGxIkCFPWb7itbMk7k9/RHlbp639S9XEGU6CFq2bGmmFjZl9t6mJ2vPjtTo5qixvM6UJyqAdzinfVE8byI6z2PUT1Rdnud8ee+7dx3WzsLsl3mklKk903d2MrtZfx3m5+f/ZLIW7vvm9Fb1rN00+1i7nk0y70NsRg95nixeo1SVbjVWr5G7yUjbbNOmTdu2bc2S2k+2buDWrFlz6NChkSNHmtr7WZ82zJ8LM2+UmfX8Z/UEmb811qq9vPYSvdi4caPOpZ49e9rtds9wGJ1C27dv37t3bz3DozwdT9yWhSYmPT394MGDw4cPt7iV5a98AQCAZdf64xOh7tu3T9FXSUkJl/zGov7OiP+eua3Jt7FlQxipYU0xfF57p2MfT0ch/bvj/73S0lIziOwUPm2AdCYEBwc7HI7aQ8nqYbPZDh8+bI6m96AhLdfVoqKiwrNcaqc0XYRbtmw5cOBAbGxsZOTxgSd5eXlKWVBQULuTyDvf/Pz8Xbt2tXAPQ/P5/VaAH+n819fH+laWv/IFAACWXeuzs7PtZmQ7/yja9NQz/y6AGmxu9fQ41PNpw/z6BwUFhYSE1DlKq55K2L9//549e1q477bzdKzoxa5du3bs2OG9vM6UqiJdUwoLC/Py8sx9aqbq6r+FSgmOHDmSmZlZY2tAExDoZv2vh7/yBQAAVl7recpV02Sm6b322muzs7N79epV54w5AJq2qKioo0ePnsKFofby2j0yJ0rZ4sdOnJ+Vr9Jb+VguAAAAoAmgQ6dpcjqdERERDz/8cJ0z3QJoDqKiohrgU70AAAAA+IS9urraPKKYumhi6pl/F0CTp9/28PBw8+Q1bmIC/Hgt9ksry1/5AgAAK6/1ttDQ0MDAwKCgIGoEAJrST7x+2Fu3bt2oJ6sGGjuHw+GXVpa/8gUAAFZe6+0jRowoKiqKioqiRgCgKamurm7Xrt2hQ4ecTifD9AC/6NevX3x8vPWtLH/lCwAALLvWJyQk2KPcqA4AaGKqq6sjIiLatm178ODB+p8zBeA0iXBrPvkCAAArr/VMrAAATZbL5erUqVNoaCg3XgEAAABNDB06ANBkVVdXh4aGdu/e3Waz0acDAAAANCX28vLy0tLSVq1aURcA0PQ4nc527drpxY4dO/SD3zyfelNVVcXjfuAXFRUVxcXF0dHRzSRfAABg2bW+pKTEvmzZsqKiolGjRkVGRlIpAND0mD4d/cgfOXKktLS0GU6QrBoIDg7mTID10tLS9uzZM3r0aItbWf7KFwAAWHat379/vz0nJ0ct3bKyMi75ANBU6Xc+JCSkc+fOzXP3XS5XaGgopwGsV1hYWFJSYn0ry1/5AgAAy671paWl9sDAQLV0eaItADRt1W7Nc99dbpwDsJ7NzfpWlr/yBQAAVl7rmRQZAAAAAACgkaFDBwAAAAAAoJGxuX5EXQAAAPiQv1pZtO4AAGgObQxbSEhIYGBgUFAQNQIAAOBDDofDL60sf+ULAACsvNbbU1JSiouLo6KiqBEAAAAf6tevX3x8vPWtLH/lCwAALLvWJyQk2Fu5UR0AAAC+FeHWfPIFAABWXuuZFBkAAAAAAKCRoUMHAAAAAACgkbGVl5fn5eVREQAAAL5VWVnpl1aWv/IFAABWXutty5YtW7JkSWFhITUCAADgQ5s3b164cKH1rSx/5QsAACy71i9ZssSWk5NTWlpaVlZGjQAAAPhQYWFhSUmJ9a0sf+ULAAAsu9aXlpbaAwMDXS5XQEAANQIAAOBDNjfrW1n+yhcAAFh5rbdTETVERUW5XC7qAWiSv3pUAgAAAICmgQ4dQj4AAAAAANDI2Fw/oi4AAAB8yF+tLFp3AAA0hzaGLSQkJDAwMCgoiBoBAADwIYfD4ZdWlr/yBQAAVl7r7SkpKcXFxVFRUdQIAACAD/Xr169jx47Wt7L8lS8AALDsWp+QkGBv5UZ1AAAA+FaEW/PJFwAAWHmtZwJgAAAAAACARoYOHQAAAAAAgEbGXl5eXlZWxl3WJ49nRgAAgJNRWVlZXFxs/b3t/soXAABYdq0vKSmxL1u2rKioaNSoUZGRkVTKT1q9evXhw4ftdjtVATQlZWVlgYGB1AMA39q8efOePXtGjx5tcSvLX/kCAADLrvX79++35+TkOJ1OBTNc8k8y6isqKqJDB2hibG7UAwDfKiwsLCkpsb6V5a98AQCAZdf60tJSe2BgoMvlCggIoEZOxpAhQ5xOJ9UFND36JQwNDaUeAPiQ6Sy2vtngr3wBAICV13pGmvw8ISEhVAIAAAAAAPAvbjEAAAAAAABoZGyuH1EXAAAAPuSvVhatOwAAmkMbwxYSEmKz2YKCgqgRAAAAH3I4HIGBgda3svyVLwAAsOxaf3wOnZSUlKKioqioKGoEAADAh/r169exY0frW1n+yhcAAFh2rY+Pj7e3cqM6AAAAfCvCrfnkCwAArLzW85QrH+N+dQAAAAAAcLrRoeNLq1evPnz4sN1OrQJNSllZWWBgIPUAAAAAoOGwl5eXK1bhLmtfRX1FRUV06ABNjM2NegDwc1VWVhYXF1t/b7u/8gUAAJZd60tKSuzLly8vKio6//zzIyMjqZT/0pAhQ5xOZ0BAAFUBNDEulyskJIR6APCzpKWl7d69e/To0Ra3svyVLwAAsOxav3//fvuxY8ecTmdZWRmX/P8e8R4AAPAoKCgoKSmxvpXlr3wBAICV13p7YGCgy+ViUAkAAIBvmRs2rW9l+StfAABg5bWeWSEAAAAAAAAaGTp0AAAAAAAAGhmb60fUBQAAgA/5q5VF6w4AgObQxrAFBwfbbLagoCBqBAAAwIccDkdgYKD1rSx/5QsAACy71ttsNvuIESOKioqioqKoEQAAAB/q169fx44drW9l+StfAABg2bU+Pj7e3sqN6gAAAPCtCLfmky8AALDyWs+kyAAAAAAAAI0MHToAAAAAAACNjK28vDw/P5+KAAAA8K3Kykq/tLL8lS8AALDyWm9bvnz5kiVLCgsLqREAAAAfSktL+/bbb61vZfkrXwAAYNm1fsmSJbZjx46VlJSUlZVRIwAAAD5UUFDgl1aWv/IFAABWXuvtgYGBLpcrICCAGgEAAPAhm5v1rSx/5QsAAKy81jMpMgAAAAAAQCNDhw4AAAAAAEAjY3P9iLoAAADwIX+1smjdAQDQHNoYtuDgYJvNFhQURI0AAAD4kMPhCAwMtL6V5a98AQCAZdd6m81mT0lJKS4ujoqKokYAAAB8qF+/fh06dLC+leWvfAEAgGXX+vj4eHu0G9UBAADgWxFuzSdfAABg5bWeSZEBAAAAAAAaGTp0AAAAAAAAGhlbeXl5QUEBFQEAAOBblZWV+fn5zSdfAABg2bW+oKDAtnz58sWLFxcWFlIjAAAAPpSWlrZw4ULrW1n+yhcAAFh2rV+8eLHt2LFjJSUlZWVl1AgAAIAPFRQUFBcXW9/K8le+AADAsmt9SUmJPTAw0OVyBQQEUCMAAAA+ZHOzvpXlr3wBAICV13omRQYAAAAAAGhk6NABAAAAAABoZOyuHzWiQgcEBOTn5zOQGEATUF1dza8Z0FT5q5XVGFt3AADg517r7cHBwQongoKCGl0IRDMFQBNAbw7QhDkcDpvNZn0ry1/5AgAAK6/19pSUlKKioqioKKIgAAAAH+rbt2+HDh2sb2X5K18AAGDZtb5jx472aDeqAwAAwLci3ZpPvgAAwMprPZMiAwAAAAAANDJ06AAAAAAAADQytoqKioKCAioCAADAtyorK/Pz85tPvgAAwLJrfUFBgW3ZsmWLFy8uLCykRgAAAHwoLS1t4cKF1rey/JUvAACw7Fq/ePFi27Fjx0pKSsrKyqgRAAAAHyooKCguLra+leWvfAEAgGXX+pKSEntgYKDL5eIR4AAAAL5lc7O+leWvfAEAgJXXeiZFBgAAAAAAaGTo0AEAAAAAAGhkbNVuLpeLugAAAPAhf7WyaN0BANAc2hj2qKio0tJSh8NBjQAAAPhQREREeHi49a0sf+ULAAAsu9aHhYUFVFZWOp3O4ODg05FHbm5ueXk5c/IBAPzI5XK1bt26gQS35z+3bfHm/BbBthbl1Yum9TovKZID1ISpiaWGVkhISDPJFwAAWHatr6qqshtUBwAAgG8FujWffAEAgJXXeiZFBgAAAAAAaGTo0AEAAAAAAGhk7AcPHnQ6nbGxscycBwAA4ENHjhwpLi7u0KGDxa0sf+ULAAAsu9aXlpbaly9fXllZefHFF8fExDSi0ttsjC0C0BS43KgHoEnavHnzgQMHLrnkEotbWf7KFwAAWHatz8rKapQzIiv4admyZVBQEEcRQGOXn5/P0wCBpkptFb80tPyVLwAAsPJa31gv9gp+GKQDAAAAAACaJ/pEAAAAAAAAGhk6dAAAAAAAABoZm9PprK6uZkpOAAAA31ITSw0t61tZ/soXAABYdq0Xe/fu3QsKCiIjI6kRAAAAH+rQoUNVVZX1rSx/5QsAACy71rtcLntycrLT6QwMDKRGAAAAfCgxMbFbt27Wt7L8lS8AALDyWn98Dh2u9wAAAKeDv1pZtO4AAGjybQwmRQYAAAAAAGhk6NABAAAAAABoZGy5ublZWVnV1dXUBQAAgA8VFhZmZmZa38ryV74AAMCya31WVpZtiVteXh41AgAA4EOpqakLFy60vpXlr3wBAIBl1/olS5bYnE5nC/czzKkRAAAAHzLtK+tbWf7KFwAAWHmttwW4UR0AAAC+5a9WFq07AACaQxuDSZEBAAAAAAAaGTp0AAAAAAAAGpnjc+hUV1e7XC7qAgAAwIfUxFJDy/pWlr/yBQAAll3rxd69e/eCgoLIyEhqBAAAwIc6dOhQVVVlfSvLX/kCAADLrvUul8uenJzsdDoDAwOpEQAAAB9KTEzs1q2b9a0sf+ULAACsvNYfn0OH6z0AAMDp4K9WFq07AACafBuDSZEBAAAAAAAaGTp0AAAAAAAAGhnb7t27U1NTq6qqqAsAAAAfysrK2rBhg/WtLH/lCwAALLvWp6am2tavX5+enp6fn0+NAAAA+NC2bdvS0tKsb2X5K18AAGDZtT49Pf0/kyK7XC5qBAAAwIcCAgL80sryV74AAMDKa71N/6EuAAAAAAAAGhEmRQYAAAAAAGhk6NABAAAAAABoZGxOp7O6upq7rAEAAHxLTSw1tKxvZfkrXwAAYNm1Xuzdu3fPz8+PjIykRgAAAHwoLi6usrLS+laWv/IFAACWXeuPd+gkJyc7nc7AwEBqBAAAwIeSkpK6d+9ufSvLX/kCAAArr/X/eWw51QEAAOBz/mpl0boDAKDJtzGYFLmm6urqn7uKy42qAwAAAAAA1rBTBTU8//zzb775Znh4eFlZWZ8+ff7xj38EBQXVTvb2228/++yzYWFhSnbmmWfOmjXL4XDcddddy5Yt00IlKCkpueGGG37729/WXveee+5ZvHhxaGioSXb11VdPmzbtJIvncrkefPDB+fPnh4SEVFRUxMfHz549u3Xr1hw4AAAAAACaD/uePXvy8/P79u1rt9O5c9ygQYOmT59uBipv3759/fr1Q4cOrZHG6XS+/fbbaWlpYWFhhYWFv/rVrxwOh5bv3r178+bN4eHhel1ZWfnyyy9fffXVCQkJ3utqg2+99VZZWZnJori4OCUl5eSL98ILLzz//PPKLiAgoKKiQqtXVVVx1AAAaICysrIyMzP79+9vcSvLX/kCAADLrvXZ2dm2devWpaen5+fnUyPG8OHDR4wYoRehoaFVVVWff/557TSqsdTU1KioKLWTOnfuPGbMGLPc4XCE/CgyMvLQoUNvvPFGjXVffvnl0tLS8PBwT8o6RwDVSYV54oknwsLCPOsGBwcHBARw1AAAaIC2bdu2ZcsW61tZ/soXAABYdq1PT0//z6TITAHjYbfbx40bZ4a9OByOb775pqioqEaazz77LDc3VynLysouvPDCrl271rmp0NDQt99+e//+/Z4l69ev17rmnqyfS+veddddKliQG4cMAIAGLiAgwGazWX/J9le+AADAsmv98UmRGd9R2y9+8Yv27dtXVVU5HI6MjIw1a9Z4f1peXv7111/rI7WT7Hb7hAkTam+h2k1pDhw44D1I5+WXXy4qKlIb6+dOvZyVlXXbbbcdPXpUuU+cOHHw4MFlZWUcKQAAAAAAmieeclWHrl27nn/++eXl5QEBAZWVlTXuutqwYcOmTZuCg4OVoHfv3ub+LG8ulysiIiIkJMTpdHoP0vEMz6murjYzIp8kZTRlypS0tDS9TklJ+eMf/6iNn8LTuAAAAAAAQNNAh07dxo8fb8YuORyOBQsW5OTkeD6aN29eWVmZzWarqKgYO3asmQLZW2VlZXx8/LXXXlteXm4G6cyePbvFj8NztNmQkJAbbrjh5AdCT58+/fPPPw8KCurYsePMmTNDQ0OVNccIAAAAAIBmy+Z0Oqurq7nLuoZzzjmnV69epkdm586dK1euNMsLCgoWLFighVVVVa1atRo7dmydq2vFW2+9tU+fPnoRGhr64YcffvTRR998801YWFhJScmFF144bty40tLSkynJ3//+97/97W8hISHK9OWXX+7ZsydHBwCARsHcgm19K8tf+QIAACuv9bZu3bq1b98+MjKSGvHWsmXLyy67zAyEUTXNmzfPLF++fPm2bduCg4PLyspSUlJ69+5d5+qVlZWdO3e+4447tIWgoKDMzMx77723tLQ0ICBAb6dMmXKSsxrPnz9/+vTpISEh2s7jjz9+4YUX1k7DLEgAADRMcXFxsbGx1rey/JUvAACw7Frfvn1721lnnTVy5MiQkBBqpIZx48apJVRdXR0cHPzdd99lZ2dr4aeffup0Ok2Cq666qp7VS0pKJkyYYAbp2Gw2MxdycXHxpZdeqjo/meE5qampU6ZMqaioqKqquvnmmydPnuz5yLsThw4dAAAapqSkpPPPP9/6Vpa/8gUAAJZd60eOHPmfx5ZTHbX1799/yJAhZWVlQUFBBw4cWLFiRWFh4cKFC4ODgysqKrp163bxxRfXs3pVVVV4ePjtt99unoCuSnY6nREREffdd18L98TJP1mAp59+eteuXaGhocpx1apVI0aMGP6jdevWabkKdvjw4dGjR48dO9Z7lh8AANBA+KuVResOAIAm38awUwsnYrPZxo8f/+2335q3n3/+eUBAwIEDB8LDwwsLCy+66KLWrVv/5EauvfbaOXPmbNq0KSQkpLS0VG/PPPPMkyxAcXGx3W4/fl+czbZt2zbPyCAJDg7Wwhbue7vS09NLSkpMtxEAAAAAAGgOeMpVfS6++OKEhISqqiozRuYvf/mLw+Gorq6OiIi45pprTmYL4eHhd9xxh9OtZcuWd91118nn7nK5qtwqKysDAgLsXrxvszreLfd/lwAAAAAAgKbNvmfPnoKCgj59+tjtjNapKS4u7sILL5wzZ05ERERmZubBgweDgoJKS0vPPvvskx9oM27cuFmzZi1fvvyuu+46+bXkD3/4w5QpU2oPmdaRevTRR9evX68X7du3f/LJJ1XOqKgojhcAAA1Kllu/fv0sbmX5K18AAGDZtf7w4cP2devWVVZWduzYsU2bNlRKbRMmTHjnnXdcLpfNrYV7cpwrr7wyKCjoJLcQFhY2ZcqUH3744Y477vhZWScnJ5/oo5iYGKfTqfKEhIT84he/CA8P50gBANDQbN++fe/evQkJCRa3svyVLwAAsOxaf/DgweP/bmOz2U5mjt7maciQIX379t28ebN5VERVVVWHDh0uu+yyOhO7vHgvv/zyy8vLy/v06XMyiU+GimFWrK6uLikpoUMHAICGyV+tLFp3AAA0+TaGjblX6hceHj5mzJjKykrTgVJWVnbBBRckJCTUmfhEfTRhYWG/+tWvTiblSfovVwcAAAAAAI0ad1b/tClTpowbN870fFVXV8fGxp4o5cyZM4uLi/UiKCio/mdgJScnp6amapsul+sUpr85+YwAAAAAAEDTQ4fOTwsLC0tKSjqZlB07djzJbYaGhp7kNv/LjAAAAAAAQNNjczqd1dXV3LkDAADgW9Vu1rey/JUvAACw8lpv79atW0FBQWRkJDUCAADgQ3FxcZWVlda3svyVLwAAsOxaf7xD56yzznI6nYGBgdQIAACADyUlJXXv3t36Vpa/8gUAAFZe6216xfUeAADgdPBXK4vWHQAATb6NYaMWAAAAAAAAGhc6dAAAAAAAABoZ2549ezZt2lRVVUVdAAAA+FBWVtbGjRutb2X5K18AAGDZtX7Tpk22devWpaen5+fnUyMAAAA+tH379rS0NOtbWf7KFwAAWHatT09PP37Llc1mc7lc1AgAAIBv+auVResOAIAm38awBQQEUBEAAAAAAACNCJMiAwAAAAAANDJ06AAAAAAAADQyNqfTWV1dzV3WAAAAvlXtZn0ry1/5AgAAK6/19m7duuXn50dERFAjAAAAPhQXF1dZWWl9K8tf+QIAAMuu9U6n037WWWfpP4GBgdQIAACADyUlJXXr1s1utzeTfAEAgGXX+u7dux+fQ4feHAAAgNPBX70q9OYAANC0BQYGMikyAAAAAABAI0OHDgAAAAAAQCNj27t376ZNm6qqqqgLAAAAH8rOzt64caP1rSx/5QsAACy71m/atMm2bt269PT0/Px8agQAAMCHtm3blpaWZn0ry1/5AgAAy6716enpdpfLZbPZ9JcaMVxu1APQ9Oi3jkoAYP0vj1/aFbTuAABo8m0Me0BAABXhraCgoKKignoAmp5WrVoFBQVRDwAAAACaAB5pWVN1dXVVVRX9XEATw+A7AAAAAE0JHTp1CHCjHgAAAAAAQMNkczqd1dXV/MM1AACAb1W7Wd/K8le+AADAymu9vWvXrgUFBREREdQIAACAD8XFxVVUVFjfyvJXvgAAwLJrvdPptA8aNKiqqspu594rAAAAX0pKSurWrZv1rSx/5QsAAKy81h9/iC/XewAAgNPBX60sWncAADT5NoaNWgAAAAAAAGhc6NABAAAAAABoZGx79+7dvHlzVVUVdQGg2aqsrCwvL+eJMAB8Kzs7OzU11fpWlr/yBQAAll3rN2/ebFu3bt2WLVvy8/OpEQDN1oYNG7788svc3FyqAoAPbdu2TY0t61tZ/soXAABYdq3fsmWLzeVy2Ww2/l0aQHNWWlpaVFRUXV1NVQDwLX+1smjdAQDQ5NsYtoCAACoCAL+GQj0AAAAAaCx4pCUANAsBAQHNttPK5XLxrxcAAABoYujQAYCmz2azOZ3O3NzckpKS6urq5ta7oX3v3bt3UFAQZwIAAACaDLuauVVVVdxlDQBNVWBgYH5+/s6dOwsKCpphb04L91PMunTpEhERwckAi+kb55dWlr/yBQAAVl7r7WeccUZpaWlUVBQ1AgBNj+nNSUtLq6io0OvmedcVt1zBX3r06BHl1kzyBQAAll3ro6Oj7YmJidQFADRJAQEBlZWV27dvN705VAhgsY5uzSdfAABg5bWep7oAQJNls9n2799fUFBAbw4AAADQ1Fr7VAEA1K+ysrK8vLzRzUYREBBQWlqalZVFbw4AAADQ9NChAwA/YcOGDV9++WVubm4j+3232Y4ePVpeXs70MQAAAEDTY1+8eHFlZeWQIUOYOQ8A6lRaWlpUVOR0OhtXsaurq48ePcrhA/xo48aNWVlZw4YNs7iV5a98AQCAZdd6NfXtR44cqaqqqqiooEYaEc+/tzeie0BMmX1S4MDAwKCgIJ20ildrZBESEqIXCrz1Wn91bjftc4BH0lrD5ta4xrmowEVuzfOxVkADkZubq4aW9a0sf+ULAACsvNbbFRvzPNfGQgcrODi4urra6XTqr+I08xDi8vLyBjt2wOFw2O32qqoq0/liyqzzrUaZtSQ0NLSFe7ISqWeD2lpBQcGOHTt69eqlVTwb0Rb00WK3AwcOhIWFTZgwYfjw4Y2oOavKCQoK0l6UlZXVc0DtbiaNXljcp2PqWVSxjW7ESrOiI6Vvir5NOljUBuAv+gKaq14zyRcAAFh5raeh32his5CQkLy8vG+++WblypXbt2/Pzc2Njo5OTEw8++yzR4wY0apVK0X4DWq8hs1mCw4O3rp165dffrlly5ZDhw5VV1fHxcV17tx5qFvr1q1Nt455svKiRYvS0tK0yp133nmiXhidstrxKVOmLF++fMyYMX/5y190HpuuIq348ssv/+lPf9K62pqqQnmde+65jaVDR9VVWFh44MCBvXv3Jicnx8bG1jm8yOFwLF269L333svIyNDODhs2rLS01MrzUMcrMzNT5ezevXtMTAx9Og1Zfn4+4RwAAADQVNGh0zhCfYXx33zzzYwZMzZt2lRZWekZobNw4cLZs2cPGDDg3nvvHT16dO27kPxFYaSK9/LLL8+cOTM7O7uqqsrc96Hi2e32119/vUePHle7RUREBAYGHj16dNq0abt27Ro1atTdd999ol6Y4ODgbdu2zZ8/PzQ09Kuvvrrzzjt79epVXl5ueo6UnXKJiYkZNmyYEnft2tX0iZjuMH1k+noa5lFWCd98880///nPx44d+/jjjzt37lxnh05QUNDatWvfffddVZp2x+JwXYWcM2fOc889l5OT8/bbb3fs2LGkpIRvaAOkE0PnT2lp6ek7Q1wul+mN5RFaAAAAgF/QodMIAjOHwzFr1qy//OUv5eXlWqIoum/fvm3atFHk/8MPP2RmZqampk6aNOn++++/4447GsjDlcPCwv7f//t/jz/+uN1ub9u27dlnn92jRw+Ffzt37szIyNi7d69K/tBDD5WUlNx3332mkyU8PFx7GhISUk/5KyoqEhMTL7744qVLl44ZMyYhIcGsq1zWr1+fk5OjF7fddtsDDzygvAoKCszzfRTZrlixYs2aNTabTVXUYMfsFBcXFxYWhoaG1nMjlZYHBQWprlp4TaVk5dmoSjaPwW5iYbzL7dQ+bZi/G+Vup+kkUW3o22R69HRK/PfT9Hi6hzxvuVsEAAAAqN/xyU3M/SnURcMUFhb2zjvvPPXUU+YOpuuvv/7GG2/s3LlzREREUVHRvn375syZowQ6iEoTHR09ceLE4uJi/5ZZkdixY8dUMMVjbdu2nTFjxoUXXmjif0WYBw8e/Pe//z1r1qyQkJArr7zyZw2Z0enaunVrrauNdO3a1W63m1t+dAIfPXrUTAg1ePBgbVOVoBrTW6VRYe65554ffvhh1KhRU6dObbAdOipww5/uxMxI3fS+aIMGDRo4cKC+VqfwaQOkr16F22maEVnfLFVIt27d9AVctmzZ4cOHT7mDz3Tl6NegQ4cO+gVzOBz6mufm5mqbZWVlDP9BY6fT2y+tLH/lCwAArLzW23v06KH/hIWFUSMNkGKbXbt2Pffcc+YJO/e66XgpTsvLy9PCrl27Pv300wkJCU8++aTeKuWwYcP01vRZ1H4QkpbU37xTgiA3M7Clznu4vDfrSex9N5OWqNi7d+/W8rFjx/7yl78sKCgw29EShW1TpkwZMWJEVlZWly5dFLPV7iAwd5kpltNa5eXl3mVQqcLDw/v06eOZlDfAzbNfnozMEvNCmzLDf1rU+3yoOj86+YWeClH5zRes9m1T3iuqVGZEUv3z4Jz8Q81MvZkBPubwnWg3VUgzyqb+lPXvbI2sg4ODPRvUvjeQu/9OUv2/gY3xF/L0DdYzw8Ti4uLMOdy2bdvs7OxT25Q5SXQZSkpKqtFfVlRUlJaWtn//fvp00KjpkqffRut/Q/yVLwAAsOxaf/zejuTkZOqiwVLU9P777yukUYh+ySWXTJ06taSkxDMNrensUPA8adKkNWvWfPHFF0qp9A899JDp0DHdQCaoU8POPGrK82Cs2vG2w+FQ4oyMjF27dikXBWx9+/ZVlOXd3WCe3+wJ6vbs2bNjxw5tuYebmd9HCYqLi1VU5R4eHm6CfE8oaAYO9O7dWxsvKyurvdchISGFhYWpqamHDx+Ojo4eMGCAyuCd0nQZmF4GM4WH2SlPCc0S7aDpyvHcu+FJ3MLdo1k73PXUmKeSzdbMHTeehWaD3ktM7Wnhzp07VXuKRWNiYhITEzt27FjjeV4mC5VNtZeXl7dgwQLt7+DBg0/U7DYHRer/t1bzmLDc3NwNGzaYW6K6dOmiAmjj3lVnkqlIOmqZmZkqgLafkJCglDpDzD193olNf5PpllKBlbjO3JUsPz9/9erVOmTajn5ctMGWLVsq68bVrdOUnL6RaKYDV+e5vsL6cTh48OCpjQPSqaUz6swzz9QZaN7qi29G1el3Q9/6oUOHKqPs7Gz6dNB4JSUlNat8AQCAldd65tBpuMwTnRYuXKjwRgHzjTfeaJ4xVCOZmXhCnyql4mf9vf322xULKbT+3e9+t2fPnnPOOeexxx574403Fi1adPTo0e7du19wwQWXXHKJ4nPv253CwsLS0tJmzJixcuXKrKwsbTYmJkYB27333nveeeeZuW9VjLffflubUvz25z//WSlnzpx57NgxFbVdu3bXXHPNPffcYwantG3btnXr1nl5efPmzRs8ePCwYcMU55uozwzfqGfa4w0bNqjk+lteXh4ZGdmvX7/f//732ohCR1WFdsHs19lnn/3CCy+ozHqrlMrLDMCZNm2aokEV+M4774yOjn7qqafMWqqTzZs3jx49WgVQymeeeaZHjx6eYiiw3LlzpzalOr/11ltvuOEGZafCbNmy5f7779fWHnjgAVWaFmrd5cuXT58+XXv99NNPDxo0SNWuhfv371d5FixYoLyUPioqKi4ubsKECZMmTdKn5unRnsKfe+65N998s0q4du1aHb7PPvts1KhRtWtDZf7uu++Ui0p1xhlnPPLII9ps7WSm1+mjjz6aNWvW7t27lVhvdfgGDhyoIzJkyBDTJWc68v75z38qu61bt6owRUVFKlubNm0GDBigHVQWnt4f0/P17bffzp8/X5Ws+unfv7/KbJ4u701nzpdffqn61DYVkCsXHX39vlx99dWXX365PqVPp4l16JjTIyMj49ChQ8pFZ9cpd+joqxofH6/X+r3Saabzx3zUtWtXffG12T59+hw5coSjCQAAANRGh04DPjZ2u+KlzMxMhT1dunTp1avXiSI0LdenSmPmSNZaffv2raqqUoC9fft2RdS33HLLp59+au7EWbNmzccffzx+/PjHH39c0ZQZfKEofe3atbfffvvOnTuVXuG9Avht27YtW7ZM23zxxRd/+ctflpSUKL5S3LVp0yaleeyxx7Txnj17du7cWaHdsWPH/vrXvwYEBDz44IPl5eWJiYnDhw//5JNPDh48+Jvf/EbFU3jWrVs3LVf8pqKa8SA1+qfMLWY333xzZWXl0KFDd+/enZ2dvXr16jvvvHPu3LmK8cxoEe2Xyta+fXvtUVlZ2caNG4uKirQvpkNHpVIabVxF1dv169druT5VYiXTbipTvdWK3lGoVomNjdU+pqamfvvttzfccEML95iUJUuWrFy5Uvv1xRdfXHrppSaUXb58+YYNG7QvHTp00Na0L8r01ltvTU9P1zajoqK0XFGo9uXpp5/Wwueff96M3/EUvm3btg8//LB2TXWiqqvzaUQRERGq/ylTpuigDBw4UJXQpk2b2j165v6pGTNmPPfcc/pUr3VEVIEqgHZElaPjYg6fuTftzTff1DnQqlUrlV/HUQdIFbVo0SKV1lSyTiczKOkPf/jDP/7xD5XNPFJNW9NZlJSU5D2WR69VP3fffXdOTo6Osg6u0ut8WLp06Z49e0aOHBkZGdlwOnQa5hS7AT/+z7fbrPMpaSfTyeI5r8wYN8/z6cyj67wT5+bm1n7KlRm5ZkaimRVPNMOx0ujkX7dunb4ymzdvVoHNppRe35rWrVvrdNL5o18n8+PTJI8+AAAAQIdOE6QARvFSXl6ewhvF/wrmTzTTigIhfao0ioKU3gzQUPikYFuRkultuf/++xXnK2g3d2YpdFcw/9RTT5kgLT8/f/r06YrAO3bs+Nhjj5133nnaQmpq6hNPPKG/v//97/v06aOPTDeTeQS4Vvz444+7d++u4O2jjz7SpvTphx9+OHHixA4dOujThx56KCsra/Xq1WVlZWvXrlXYph1RkVTULl26jB079qqrrjJDVzw7okwPHjx47733aiOK4lTOhx9++Pvvv9+9e7fyevDBB82DurURh5veqlSvvfaaSvXZZ5+pGNqIkvXr108RYM+ePZXyvffeKywsfOaZZ7TlgQMH/u53vzMzrWpF7w4yhZ3R0dHDhg3bsGHDzp07VfKYmBilVO4qpLa/cePGzMxMVbKOgnZKW0hOTlbAqTSqAVWaKl9VeuWVV95yyy2q9n379inTVatW/etf/0pKSvIuvD5Vrfbv33/evHmqQFW+yatGb878+fMnT56sfb/gggteeOGFTp06aadqz5qsivr666+ff/55HRRVrHbQTAv9+eefv/TSSzofdPh69eplZlZSeHzfffetX7/+kksuUQ1oa0qgjevAKaN//vOfqnAzmEiH/u9//7vpHrrooov69u2r3f/qq6+WLFniPdeJ6uH999/XR6NGjXrllVdUh8rlwIEDb731lo6C1q3zrjp/CbQ1xKBeX9bA49+nAN9u0/nzO3R0JutU0VHT10FnvpYkJia2b99eL7Kzs3fs2FFUVOS5Y9Gk1Is1a9YUFBR49/voPNSPQMuWLbVEp7dOD337PP01/+cKZLfv3bvX9Bh6zm3T82hG65jXTezo8/AuAAAA+KZDR6GdokSFpsyc19AojKl0M30u9f8DtUlgxoB4/8u8GbwzZ84cBWZarpBp4sSJd9xxx5YtW959993LL788JSVFa3366acbNmwICQlR8H/TTTeZuZD1aevWra+++mqF+p999tldd93l2axKdd999w0ePDgvL08x/y233LJq1apPPvnk8OHD+/fv79SpU2lpqYK9N998UysuWLBg3759hw4d0kKtqBcKDhUumm4IZeHZrBKcffbZd999t14oUOzTp8/vfve76667TmulpaXVnkFGhYyMjLz44ovDw8O3bt1qRq8MHTp01KhROqvNRL89evRQPPnSSy/prfLSTukjLa89i5DeDhs27I033lBpt23bpr1QLSnfqKgo1a3CTr2+9NJL09PTVSEKTVVU00Hz1VdfLV26VHWrT80wJVW1Ytpu3bqp8D/88MP7779/zTXXaImnA07h7osvvqiDoj3V6xpTCEdERCxfvlyHSRldeOGFM2fObNeunbnrrfZxLy4unj17trYQHR393HPPad+1RGVQ1enQPPXUUyr5e++9N23aNHN3zOjRo1UJZgyOMo2Pj586deqiRYuysrJUVNPppp+Ft956S3ukQ6ByDhgwQHWrt5MnT9Zx1zH1LoNidWUXGxurTWmDoaGhqrEnn3xSu9mgenPCHLZfzdmTureiRVDDiqePT+dU7fLtAJKA6oDfJJb2jLJV/JzRUTr6uhC0bNlSx1GnXN++fT132GmhTlSd54WFhebkMSndnUf/mSRLa+k35KyzzjLzJXtWTEhIyMnJ2bhxY50POK9zjI+SxcTE6LVO5jrHr/38ox94wz927yk43CLQ/w/92X20vIXDxjWumdDVRNegeiZKa2L5AgAAy671ir7tZkbbnj17cslvaBQdRbkV/EjxeZ13ryj4MQn02qziSaaD27Fjx6SkpLy8PLNEIfq99947adKk8vLyxYsXjxgxQgu///57BVFaUbHTu+++a0bNmI6k9u3bHzlyZM2aNd5PktJrc7tTtZvD4ejVq5fJzjNdsbYfERFx0003TZw48ajbnj17tm7dum7dupUr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eesFk5X8UutLxx09FddMYydFznUM7z9eKo625zpO75untkxVuoAXjsqlKXXiu6VtZumr9H5o7TtksQGXmcnd486K+yt28tBDD8X1OXce5dM/+2+7sKf/rKVwxn/uY0//17eKptEBAODlBnRmveHCkhKdqJtuuunuu+/+y7/8yzhNv/Irv/KHf/iHd9xxR3SW0ow20dOOjvd73vOe6EjH7z/90z8d6eNTtfEgkTI66jt27Egz+MaW7du3//Ef/3F89qyzznr961+fhmDccsstg4ODaTWo6O1Htyq6Ummd771790b3/mQjROYV3f7ojL33ve8tlUpPPfXUW9/61thhbQnk6KF98pOffOyxxyLlRRdddN55553pmVZqF3ma7ifFO+aNT0Udbt68+cILL3ziiSc+85nPxFFff/31adrm17zmNQ888MD9998fH9y0aVPUSYqwxN5uvfXWOEFxsPfee+911123du3a+FN0Sr/yla/cd999kcvFF1989dVXL7IO07CID3/4w9Gn/T8zfvd3f/eee+6J0zG3oiKjKMy11147NDT05S9/+bOf/exP/uRPpuW0omB/8Rd/sX///kgW10yUJ0oSPe3Yfu6550bNp9l20vCr+jBNFODOO+/8q7/6q9HR0Q996ENxOLfddlt6IevJJ5/80pe+FL/XxnClgTxxkcQO4/fVq1dH+l/8xV+MinrmmWfSCKYlolJtu3RDd1uuc8nd5oMvDrxr9CpXHV8/sWr/cFtHg3a4cPHSSLEUu4mDOY1jiasobrRt27Z1d3fHlb979+64oRoVzZk5+9Xv39DTv7pnKZzx/u6ONk/dFaNZrSytOwBYCW2MfHTkom/WwHYzjT1JaT2p6DA/8MADBw8e/Pmf//mbb775Na95TfTJn3vuuej2/Md//EdaPSp63ZGyNpiiFluJLv3dd9/92te+dvPmzbGfhx56KA3A+dVf/dUtW7ak6TCuvPLKn/iJn7j33nu/8pWvvPWtb33HO94RiY8cOfLJT35y+/bt99xzz4/+6I8uPuySz+cjl0OHDkXu73//+//lX/7ljW984xVXXNHX1xddtR07dnzuc58bHx+Pv7797W/v7e1d4AWxhtRhWnc8LvWnnnrqb/7mb9L631dddVWhUJg1yXTcC2vWrLnmmmsee+yxycnJ6KBGVaeox4033tjf3x+d1Sht1Nv555+fxizElh/4gR+IA/zUpz4Vp+PtM9auXfutb33rIx/5SJyjSBNbNmzYsPigWGTR09PzgQ98IM7Url27Pv7xj0dJ4izMvU9TR/qd73xn1Oro6Ghaez6ukCjV5z//+fvuuy9KHif3zW9+c2yJCr/88su/+MUvPv744/fff//rXve6+Ovx48c//elPx6VV23mkvPrqq2Ofce6ef/75uOSuu+66OOQDBw48+OCDcQbjlNVeulm1atU//uM//sEf/EFcPz/yIz+ycePGKGpcq3v27IlfomaW1A01OV2deQ1oaSlNVSemqo2d6aLjxWWzshsAkmYlj6+IuMZqC2O9pGjO6tWrb7rppvjs8PDwl7/85bjAGv5G8MR0pX9pnPGKbvZKkiayyb6V1ax8AYAsn/X5bdu2jYyMRGNajSxN0dUZGBj40z/90w9+8IN/93d/Fz38/zsjjdBJY176+/t/9md/9l3veleknBU1iM75Nddcs27duuh1p0BP9MDXrl37y7/8y+94xztqr1HEp37jN37j6NGj//AP/xCd9ocffjjSnJgRf/3bv/3b22+/PbrxkWmkTJ35+tlVZm2P3f7cz/1cXFRR7DS16qOPPtozIy629BrFWWed9e53v/uNb3xjqVSKazHKlhYan7VE8dzt86Y8WcFSBZ5zzjnXXXfdf//3fx8+fPjXfu3XosbOPvvsf/qnf0rLM88Nkdx8881/9md/FuV8xSteccUVV0RPNfZ58cUXX3TRRdHVjATR86y1klO453d+53eOHDny7//+71/60pceeuihqKv0ZlzUdtTzT/3UT6XhBic7zLmHELnHKfjIRz7y9re/fdeuXffee298/D3veU/U4awjjdq+/vrr77nnnlSG973vfX19ffGnSBNHeumll37gAx+IXUWO8c+77rorroTvfve7v/ALvxAXRnd39+OPP/7CCy+0zawZXytV5P5Lv/RLkf7P//zP46qI6+0LX/hCbL/zzjs3btz48Y9/PM3OE0WKE3r//fcPDQ19+MMf/sQnPhFVHcf49NNPx2Hecccdd99990sa20UDdWUYu0qLu8W3U9xZaUGruKjSsK/6iaXmHbmTZu+Ke6pQKKQIZpqu2xlkedi6deuGDRuyb2U1K18AILNn/bnnntvx/ve/P573Z2gdhOhqnnJS1dMT3doz9N+dzlyZT1uUp7e393Wv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" alt="A diagram that depicts four OpenShift workloads on OpenStack. Each workload is connected by its NIC to an external data center by using a provider network." />
</figure>

OpenShift Container Platform clusters that are installed on provider networks do not require tenant networks or floating IP addresses. The installer does not create these resources during installation.

Example provider network types include flat (untagged) and VLAN (802.1Q tagged).

> [!NOTE]
> A cluster can support as many provider network connections as the network type allows. For example, VLAN networks typically support up to 4096 connections.

You can learn more about provider and tenant networks in [the RHOSP documentation](https://access.redhat.com/documentation/en-us/red_hat_openstack_platform/16.1/html/networking_guide/networking-overview_rhosp-network#tenant-provider-networks_network-overview).

### RHOSP provider network requirements for cluster installation

Before you install an OpenShift Container Platform cluster, your Red Hat OpenStack Platform (RHOSP) deployment and provider network must meet a number of conditions:

- The [RHOSP networking service (Neutron) is enabled](https://access.redhat.com/documentation/en-us/red_hat_openstack_platform/16.1/html/networking_guide/networking-overview_rhosp-network#install-networking_network-overview) and accessible through the RHOSP networking API.

- The RHOSP networking service has the [port security and allowed address pairs extensions enabled](https://access.redhat.com/documentation/en-us/red_hat_openstack_platform/16.1/html/networking_guide/config-allowed-address-pairs_rhosp-network#overview-allow-addr-pairs_config-allowed-address-pairs).

- The provider network can be shared with other tenants.

  > [!TIP]
  > Use the `openstack network create` command with the `--share` flag to create a network that can be shared.

- The RHOSP project that you use to install the cluster must own the provider network, as well as an appropriate subnet.

  <div class="tip">

  <div class="title">

  </div>

  To create a network for a project that is named "openshift," enter the following command

  ``` terminal
  $ openstack network create --project openshift
  ```

  To create a subnet for a project that is named "openshift," enter the following command

  ``` terminal
  $ openstack subnet create --project openshift
  ```

  To learn more about creating networks on RHOSP, read [the provider networks documentation](https://access.redhat.com/documentation/en-us/red_hat_openstack_platform/16.1/html/networking_guide/networking-overview_rhosp-network#tenant-provider-networks_network-overview).

  </div>

  If the cluster is owned by the `admin` user, you must run the installer as that user to create ports on the network.

  > [!IMPORTANT]
  > Provider networks must be owned by the RHOSP project that is used to create the cluster. If they are not, the RHOSP Compute service (Nova) cannot request a port from that network.

- Verify that the provider network can reach the RHOSP metadata service IP address, which is `169.254.169.254` by default.

  Depending on your RHOSP SDN and networking service configuration, you might need to provide the route when you create the subnet. For example:

  ``` terminal
  $ openstack subnet create --dhcp --host-route destination=169.254.169.254/32,gateway=192.0.2.2 ...
  ```

- Optional: To secure the network, create [role-based access control (RBAC)](https://access.redhat.com/documentation/en-us/red_hat_openstack_platform/16.1/html/networking_guide/config-rbac-policies_rhosp-network#proc_create-rbac-policies_config-rbac-policies) rules that limit network access to a single project.

### Deploying a cluster that has a primary interface on a provider network

You can deploy an OpenShift Container Platform cluster that has its primary network interface on an Red Hat OpenStack Platform (RHOSP) provider network.

<div>

<div class="title">

Prerequisites

</div>

- Your Red Hat OpenStack Platform (RHOSP) deployment is configured as described by "RHOSP provider network requirements for cluster installation".

</div>

<div>

<div class="title">

Procedure

</div>

1.  In a text editor, open the `install-config.yaml` file.

2.  Set the value of the `platform.openstack.apiVIPs` property to the IP address for the API VIP.

3.  Set the value of the `platform.openstack.ingressVIPs` property to the IP address for the Ingress VIP.

4.  Set the value of the `platform.openstack.machinesSubnet` property to the UUID of the provider network subnet.

5.  Set the value of the `networking.machineNetwork.cidr` property to the CIDR block of the provider network subnet.

</div>

> [!IMPORTANT]
> The `platform.openstack.apiVIPs` and `platform.openstack.ingressVIPs` properties must both be unassigned IP addresses from the `networking.machineNetwork.cidr` block.

<div class="formalpara">

<div class="title">

Section of an installation configuration file for a cluster that relies on a RHOSP provider network

</div>

``` yaml
        ...
        platform:
          openstack:
            apiVIPs:
              - 192.0.2.13
            ingressVIPs:
              - 192.0.2.23
            machinesSubnet: fa806b2f-ac49-4bce-b9db-124bc64209bf
            # ...
        networking:
          machineNetwork:
          - cidr: 192.0.2.0/24
```

</div>

- In OpenShift Container Platform 4.12 and later, the `apiVIP` and `ingressVIP` configuration settings are deprecated. Instead, use a list format to enter values in the `apiVIPs` and `ingressVIPs` configuration settings.

> [!WARNING]
> You cannot set the `platform.openstack.externalNetwork` or `platform.openstack.externalDNS` parameters while using a provider network for the primary network interface.

When you deploy the cluster, the installer uses the `install-config.yaml` file to deploy the cluster on the provider network.

> [!TIP]
> You can add additional networks, including provider networks, to the `platform.openstack.additionalNetworkIDs` list.
>
> After you deploy your cluster, you can attach pods to additional networks. For more information, see [Understanding multiple networks](../../networking/multiple_networks/understanding-multiple-networks.md#understanding-multiple-networks).

# Creating the Kubernetes manifest and Ignition config files

To customize cluster definitions and manually start machines, generate the Kubernetes manifest and Ignition config files.

The installation configuration file transforms into the Kubernetes manifests. The manifests wrap into the Ignition configuration files, which are later used to configure the cluster machines.

<div class="important">

<div class="title">

</div>

- The Ignition config files that the OpenShift Container Platform installation program generates contain certificates that expire after 24 hours, which are then renewed at that time. If the cluster is shut down before renewing the certificates and the cluster is later restarted after the 24 hours have elapsed, the cluster automatically recovers the expired certificates. The exception is that you must manually approve the pending `node-bootstrapper` certificate signing requests (CSRs) to recover kubelet certificates. See the documentation for *Recovering from expired control plane certificates* for more information.

- It is recommended that you use Ignition config files within 12 hours after they are generated because the 24-hour certificate rotates from 16 to 22 hours after the cluster is installed. By using the Ignition config files within 12 hours, you can avoid installation failure if the certificate update runs during installation.

</div>

<div>

<div class="title">

Prerequisites

</div>

- You obtained the OpenShift Container Platform installation program.

- You created the `install-config.yaml` installation configuration file.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Change to the directory that contains the OpenShift Container Platform installation program and generate the Kubernetes manifests for the cluster:

    ``` terminal
    $ ./openshift-install create manifests --dir <installation_directory>
    ```

    where

    `<installation_directory>`
    Specifies the installation directory that contains the `install-config.yaml` file you created.

2.  Remove the Kubernetes manifest files that define the control plane machines, compute machine sets, and control plane machine sets:

    ``` terminal
    $ rm -f openshift/99_openshift-cluster-api_master-machines-*.yaml openshift/99_openshift-cluster-api_worker-machineset-*.yaml openshift/99_openshift-machine-api_master-control-plane-machine-set.yaml
    ```

    Because you create and manage these resources yourself, you do not have to initialize them. You can preserve the compute machine set files to create compute machines by using the machine API, but you must update references to them to match your environment.

3.  Check that the `mastersSchedulable` parameter in the `<installation_directory>/manifests/cluster-scheduler-02-config.yml` Kubernetes manifest file is set to `false`. This setting prevents pods from being scheduled on the control plane machines:

    1.  Open the `<installation_directory>/manifests/cluster-scheduler-02-config.yml` file.

    2.  Locate the `mastersSchedulable` parameter and ensure that it is set to `false`.

    3.  Save and exit the file.

4.  To create the Ignition configuration files, run the following command from the directory that contains the installation program:

    ``` terminal
    $ ./openshift-install create ignition-configs --dir <installation_directory>
    ```

    where:

    `<installation_directory>`
    Specifies the same installation directory.

    Ignition config files are created for the bootstrap, control plane, and compute nodes in the installation directory. The `kubeadmin-password` and `kubeconfig` files are created in the `./<installation_directory>/auth` directory:

        .
        ├── auth
        │   ├── kubeadmin-password
        │   └── kubeconfig
        ├── bootstrap.ign
        ├── master.ign
        ├── metadata.json
        └── worker.ign

5.  Export the metadata file’s `infraID` key as an environment variable:

    ``` terminal
    $ export INFRA_ID=$(jq -r .infraID metadata.json)
    ```

    > [!TIP]
    > Extract the `infraID` key from `metadata.json` and use it as a prefix for all of the RHOSP resources that you create. By doing so, you avoid name conflicts when making multiple deployments in the same project.

</div>

# Preparing the bootstrap Ignition files

The OpenShift Container Platform installation process relies on bootstrap machines that are created from a bootstrap Ignition configuration file.

Edit the file and upload it. Then, create a secondary bootstrap Ignition configuration file that Red Hat OpenStack Platform (RHOSP) uses to download the primary file.

<div>

<div class="title">

Prerequisites

</div>

- You have the bootstrap Ignition file that the installer program generates, `bootstrap.ign`.

- The infrastructure ID from the installer’s metadata file is set as an environment variable (`$INFRA_ID`).

  - If the variable is not set, see **Creating the Kubernetes manifest and Ignition config files**.

- You have an HTTP(S)-accessible way to store the bootstrap Ignition file.

  - The documented procedure uses the RHOSP image service (Glance), but you can also use the RHOSP storage service (Swift), Amazon S3, an internal HTTP server, or an ad hoc Nova server.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Run the following Python script. The script modifies the bootstrap Ignition file to set the hostname and, if available, CA certificate file when it runs:

    ``` python
    import base64
    import json
    import os

    with open('bootstrap.ign', 'r') as f:
        ignition = json.load(f)

    files = ignition['storage'].get('files', [])

    infra_id = os.environ.get('INFRA_ID', 'openshift').encode()
    hostname_b64 = base64.standard_b64encode(infra_id + b'-bootstrap\n').decode().strip()
    files.append(
    {
        'path': '/etc/hostname',
        'mode': 420,
        'contents': {
            'source': 'data:text/plain;charset=utf-8;base64,' + hostname_b64
        }
    })

    ca_cert_path = os.environ.get('OS_CACERT', '')
    if ca_cert_path:
        with open(ca_cert_path, 'r') as f:
            ca_cert = f.read().encode()
            ca_cert_b64 = base64.standard_b64encode(ca_cert).decode().strip()

        files.append(
        {
            'path': '/opt/openshift/tls/cloud-ca-cert.pem',
            'mode': 420,
            'contents': {
                'source': 'data:text/plain;charset=utf-8;base64,' + ca_cert_b64
            }
        })

    ignition['storage']['files'] = files;

    with open('bootstrap.ign', 'w') as f:
        json.dump(ignition, f)
    ```

2.  Using the RHOSP CLI, create an image that uses the bootstrap Ignition file:

    ``` terminal
    $ openstack image create --disk-format=raw --container-format=bare --file bootstrap.ign <image_name>
    ```

3.  Get the image’s details:

    ``` terminal
    $ openstack image show <image_name>
    ```

    Make a note of the `file` value; it follows the pattern `v2/images/<image_ID>/file`.

    > [!NOTE]
    > Verify that the image you created is active.

4.  Retrieve the image service’s public address:

    ``` terminal
    $ openstack catalog show image
    ```

5.  Combine the public address with the image `file` value and save the result as the storage location. The location follows the pattern `<image_service_public_URL>/v2/images/<image_ID>/file`.

6.  Generate an auth token and save the token ID:

    ``` terminal
    $ openstack token issue -c id -f value
    ```

7.  Insert the following content into a file called `$INFRA_ID-bootstrap-ignition.json` and edit the placeholders to match your own values:

    ``` json
    {
      "ignition": {
        "config": {
          "merge": [{
            "source": "<storage_url>",
            "httpHeaders": [{
              "name": "X-Auth-Token",
              "value": "<token_ID>"
            }]
          }]
        },
        "security": {
          "tls": {
            "certificateAuthorities": [{
              "source": "data:text/plain;charset=utf-8;base64,<base64_encoded_certificate>"
            }]
          }
        },
        "version": "3.2.0"
      }
    }
    ```

    - Replace the value of `ignition.config.merge.source` with the bootstrap Ignition file storage URL.

    - Set `name` in `httpHeaders` to `"X-Auth-Token"`.

    - Set `value` in `httpHeaders` to your token’s ID.

    - If the bootstrap Ignition file server uses a self-signed certificate, include the base64-encoded certificate.

8.  Save the secondary Ignition config file.

</div>

The bootstrap Ignition data will be passed to RHOSP during installation.

> [!WARNING]
> The bootstrap Ignition file contains sensitive information, like `clouds.yaml` credentials. Ensure that you store it in a secure place, and delete it after you complete the installation process.

# Creating control plane Ignition config files on RHOSP

Installing OpenShift Container Platform on Red Hat OpenStack Platform (RHOSP) on your own infrastructure requires control plane Ignition config files. You must create multiple config files.

> [!NOTE]
> As with the bootstrap Ignition configuration, you must explicitly define a hostname for each control plane machine.

<div>

<div class="title">

Prerequisites

</div>

- The infrastructure ID from the installation program’s metadata file is set as an environment variable (`$INFRA_ID`).

  - If the variable is not set, see "Creating the Kubernetes manifest and Ignition config files".

</div>

<div>

<div class="title">

Procedure

</div>

- On a command line, run the following Python script:

  ``` terminal
  $ for index in $(seq 0 2); do
      MASTER_HOSTNAME="$INFRA_ID-master-$index\n"
      python -c "import base64, json, sys;
  ignition = json.load(sys.stdin);
  storage = ignition.get('storage', {});
  files = storage.get('files', []);
  files.append({'path': '/etc/hostname', 'mode': 420, 'contents': {'source': 'data:text/plain;charset=utf-8;base64,' + base64.standard_b64encode(b'$MASTER_HOSTNAME').decode().strip(), 'verification': {}}, 'filesystem': 'root'});
  storage['files'] = files;
  ignition['storage'] = storage
  json.dump(ignition, sys.stdout)" <master.ign >"$INFRA_ID-master-$index-ignition.json"
  done
  ```

  You now have three control plane Ignition files: `<INFRA_ID>-master-0-ignition.json`, `<INFRA_ID>-master-1-ignition.json`, and `<INFRA_ID>-master-2-ignition.json`.

</div>

# Updating network resources on RHOSP

Update the network resources that an OpenShift Container Platform on Red Hat OpenStack Platform (RHOSP) installation on your own infrastructure requires.

<div>

<div class="title">

Prerequisites

</div>

- Python 3 is installed on your machine.

- You downloaded the modules in "Downloading playbook dependencies".

- You downloaded the playbooks in "Downloading the installation playbooks".

</div>

<div>

<div class="title">

Procedure

</div>

1.  Optional: Add an external network value to the `inventory.yaml` playbook:

    <div class="formalpara">

    <div class="title">

    Example external network value in the `inventory.yaml` Ansible Playbook

    </div>

    ``` yaml
    ...
          # The public network providing connectivity to the cluster. If not
          # provided, the cluster external connectivity must be provided in another
          # way.

          # Required for os_api_fip, os_ingress_fip, os_bootstrap_fip.
          os_external_network: 'external'
    ...
    ```

    </div>

    > [!IMPORTANT]
    > If you did not provide a value for `os_external_network` in the `inventory.yaml` file, you must ensure that VMs can access Glance and an external connection yourself.

2.  Optional: Add external network and floating IP (FIP) address values to the `inventory.yaml` playbook:

    <div class="formalpara">

    <div class="title">

    Example FIP values in the `inventory.yaml` Ansible Playbook

    </div>

    ``` yaml
    ...
          # OpenShift API floating IP address. If this value is non-empty, the
          # corresponding floating IP will be attached to the Control Plane to
          # serve the OpenShift API.
          os_api_fip: '203.0.113.23'

          # OpenShift Ingress floating IP address. If this value is non-empty, the
          # corresponding floating IP will be attached to the worker nodes to serve
          # the applications.
          os_ingress_fip: '203.0.113.19'

          # If this value is non-empty, the corresponding floating IP will be
          # attached to the bootstrap machine. This is needed for collecting logs
          # in case of install failure.
          os_bootstrap_fip: '203.0.113.20'
    ```

    </div>

    > [!IMPORTANT]
    > If you do not define values for `os_api_fip` and `os_ingress_fip`, you must perform postinstallation network configuration.
    >
    > If you do not define a value for `os_bootstrap_fip`, the installation program cannot download debugging information from failed installations.
    >
    > See "Enabling access to the environment" for more information.

3.  On a command line, create security groups by running the `security-groups.yaml` playbook:

    ``` terminal
    $ ansible-playbook -i inventory.yaml security-groups.yaml
    ```

4.  On a command line, update the network resources by running the `update-network-resources.yaml` playbook:

    ``` terminal
    $ ansible-playbook -i inventory.yaml update-network-resources.yaml
    ```

    - This playbook will add tags to the network, subnets, ports, and router. It also attaches floating IP addresses to the API and Ingress ports and sets the security groups for those ports.

5.  Optional: If you want to control the default resolvers that Nova servers use, run the RHOSP CLI command:

    ``` terminal
    $ openstack subnet set --dns-nameserver <server_1> --dns-nameserver <server_2> "$INFRA_ID-nodes"
    ```

6.  Optional: You can use the `inventory.yaml` file that you created to customize your installation. For example, you can deploy a cluster that uses bare metal machines.

</div>

## Deploying a cluster with bare metal machines

If you want your cluster to use bare metal machines, modify the `inventory.yaml` file. Your cluster can have compute machines running on bare metal.

> [!NOTE]
> Be sure that your `install-config.yaml` file reflects whether the RHOSP network that you use for bare metal workers supports floating IP addresses or not.

<div>

<div class="title">

Prerequisites

</div>

- The RHOSP [Bare Metal service (Ironic)](https://access.redhat.com/documentation/en-us/red_hat_openstack_platform/16.1/html/bare_metal_provisioning/index) is enabled and accessible via the RHOSP Compute API.

- Bare metal is available as [a RHOSP flavor](https://docs.redhat.com/en/documentation/red_hat_openstack_platform/17.1/html/configuring_the_bare_metal_provisioning_service/assembly_configuring-the-bare-metal-provisioning-service-after-deployment#proc_creating-flavors-for-launching-bare-metal-instances_bare-metal-post-deployment).

- If your cluster runs on an RHOSP version that is more than 16.1.6 and less than 16.2.4, bare metal workers do not function due to a [known issue](https://bugzilla.redhat.com/show_bug.cgi?id=2033953) that causes the metadata service to be unavailable for services on OpenShift Container Platform nodes.

- The RHOSP network supports both VM and bare metal server attachment.

- If you want to deploy the machines on a pre-existing network, a RHOSP subnet is provisioned.

- If you want to deploy the machines on an installer-provisioned network, the RHOSP Bare Metal service (Ironic) is able to listen for and interact with Preboot eXecution Environment (PXE) boot machines that run on tenant networks.

- You created an `inventory.yaml` file as part of the OpenShift Container Platform installation process.

</div>

<div>

<div class="title">

Procedure

</div>

1.  In the `inventory.yaml` file, edit the flavors for machines:

    1.  Change the value of `os_flavor_worker` to a bare metal flavor.

        <div class="formalpara">

        <div class="title">

        An example bare metal `inventory.yaml` file

        </div>

        ``` yaml
        all:
          hosts:
            localhost:
              ansible_connection: local
              ansible_python_interpreter: "{{ansible_playbook_python}}"

              # User-provided values
              os_subnet_range: '10.0.0.0/16'
              os_flavor_master: 'my-vm-flavor'
              os_flavor_worker: 'my-bare-metal-flavor'
              os_image_rhcos: 'rhcos'
              os_external_network: 'external'
        ...
        ```

        </div>

        - Change this value to a bare metal flavor to use for compute machines.

</div>

Use the updated `inventory.yaml` file to complete the installation process. Machines that are created during deployment use the flavor that you added to the file.

> [!NOTE]
> The installation program may time out while waiting for bare metal machines to boot.
>
> If the installation program times out, restart and then complete the deployment by using the `wait-for` command of the installation program. For example:
>
> ``` terminal
> $ ./openshift-install wait-for install-complete --log-level debug
> ```

# Creating the bootstrap machine on RHOSP

Create a bootstrap machine and give it the network access it needs to run on Red Hat OpenStack Platform (RHOSP). Red Hat provides an Ansible playbook that you run to simplify this process.

<div>

<div class="title">

Prerequisites

</div>

- You downloaded the modules in "Downloading playbook dependencies".

- You downloaded the playbooks in "Downloading the installation playbooks".

- The `inventory.yaml`, `common.yaml`, and `bootstrap.yaml` Ansible playbooks are in a common directory.

- The `metadata.json` file that the installation program created is in the same directory as the Ansible playbooks.

</div>

<div>

<div class="title">

Procedure

</div>

1.  On a command line, change the working directory to the location of the playbooks.

2.  On a command line, run the `bootstrap.yaml` playbook:

    ``` terminal
    $ ansible-playbook -i inventory.yaml bootstrap.yaml
    ```

3.  After the bootstrap server is active, view the logs to verify that the Ignition files were received:

    ``` terminal
    $ openstack console log show "$INFRA_ID-bootstrap"
    ```

</div>

# Creating the control plane machines on RHOSP

Create three control plane machines by using the Ignition config files that you generated. Red Hat provides an Ansible playbook that you run to simplify this process.

<div>

<div class="title">

Prerequisites

</div>

- You downloaded the modules in "Downloading playbook dependencies".

- You downloaded the playbooks in "Downloading the installation playbooks".

- The infrastructure ID from the installation program’s metadata file is set as an environment variable (`$INFRA_ID`).

- The `inventory.yaml`, `common.yaml`, and `control-plane.yaml` Ansible playbooks are in a common directory.

- You have the three Ignition files that were created in "Creating control plane Ignition config files".

</div>

<div>

<div class="title">

Procedure

</div>

1.  On a command line, change the working directory to the location of the playbooks.

2.  If the control plane Ignition config files are not already in your working directory, copy them into it.

3.  On a command line, run the `control-plane.yaml` playbook:

    ``` terminal
    $ ansible-playbook -i inventory.yaml control-plane.yaml
    ```

4.  Run the following command to monitor the bootstrapping process:

    ``` terminal
    $ openshift-install wait-for bootstrap-complete
    ```

    You will see messages that confirm that the control plane machines are running and have joined the cluster:

    ``` terminal
    INFO API v1.33.4 up
    INFO Waiting up to 30m0s for bootstrapping to complete...
    ...
    INFO It is now safe to remove the bootstrap resources
    ```

</div>

# Logging in to the cluster by using the CLI

To log in to your cluster as the default system user, export the `kubeconfig` file. This configuration enables the CLI to authenticate and connect to the specific API server created during OpenShift Container Platform installation.

The `kubeconfig` file is specific to a cluster and is created during OpenShift Container Platform installation.

<div>

<div class="title">

Prerequisites

</div>

- You deployed an OpenShift Container Platform cluster.

- You installed the OpenShift CLI (`oc`).

</div>

<div>

<div class="title">

Procedure

</div>

1.  Export the `kubeadmin` credentials by running the following command:

    ``` terminal
    $ export KUBECONFIG=<installation_directory>/auth/kubeconfig
    ```

    where:

    `<installation_directory>`
    Specifies the path to the directory that stores the installation files.

2.  Verify you can run `oc` commands successfully using the exported configuration by running the following command:

    ``` terminal
    $ oc whoami
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    system:admin
    ```

    </div>

</div>

<div>

<div class="title">

Next steps

</div>

- "Customize your cluster"

- "Remote health reporting"

</div>

# Deleting bootstrap resources from RHOSP

Delete the bootstrap resources that you no longer need.

<div>

<div class="title">

Prerequisites

</div>

- You downloaded the modules in "Downloading playbook dependencies".

- You downloaded the playbooks in "Downloading the installation playbooks".

- The `inventory.yaml`, `common.yaml`, and `down-bootstrap.yaml` Ansible playbooks are in a common directory.

- The control plane machines are running.

  - If you do not know the status of the machines, see "Verifying cluster status".

</div>

<div>

<div class="title">

Procedure

</div>

1.  On a command line, change the working directory to the location of the playbooks.

2.  On a command line, run the `down-bootstrap.yaml` playbook:

    ``` terminal
    $ ansible-playbook -i inventory.yaml down-bootstrap.yaml
    ```

</div>

The bootstrap port, server, and floating IP address are deleted.

> [!WARNING]
> If you did not disable the bootstrap Ignition file URL earlier, do so now.

# Creating compute machines on RHOSP

After standing up the control plane, create compute machines. Red Hat provides an Ansible playbook that you run to simplify this process.

<div>

<div class="title">

Prerequisites

</div>

- You downloaded the modules in "Downloading playbook dependencies".

- You downloaded the playbooks in "Downloading the installation playbooks".

- The `inventory.yaml`, `common.yaml`, and `compute-nodes.yaml` Ansible playbooks are in a common directory.

- The `metadata.json` file that the installation program created is in the same directory as the Ansible playbooks.

- The control plane is active.

</div>

<div>

<div class="title">

Procedure

</div>

1.  On a command line, change the working directory to the location of the playbooks.

2.  On a command line, run the playbook:

    ``` terminal
    $ ansible-playbook -i inventory.yaml compute-nodes.yaml
    ```

</div>

<div>

<div class="title">

Next steps

</div>

- Approve the certificate signing requests for the machines.

</div>

# Approving the certificate signing requests for your machines

When you add machines to a cluster, two pending certificate signing requests (CSRs) are generated for each machine that you added. You must confirm that these CSRs are approved or, if necessary, approve them yourself. The client requests must be approved first, followed by the server requests.

<div>

<div class="title">

Prerequisites

</div>

- You added machines to your cluster.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Confirm that the cluster recognizes the machines:

    ``` terminal
    $ oc get nodes
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    NAME      STATUS    ROLES   AGE  VERSION
    master-0  Ready     master  63m  v1.33.4
    master-1  Ready     master  63m  v1.33.4
    master-2  Ready     master  64m  v1.33.4
    ```

    </div>

    The output lists all of the machines that you created.

    > [!NOTE]
    > The preceding output might not include the compute nodes until some CSRs are approved.

2.  Review the pending CSRs and ensure that you see the client requests with the `Pending` or `Approved` status for each machine that you added to the cluster:

    ``` terminal
    $ oc get csr
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    NAME        AGE     REQUESTOR                                                                   CONDITION
    csr-8b2br   15m     system:serviceaccount:openshift-machine-config-operator:node-bootstrapper   Pending
    csr-8vnps   15m     system:serviceaccount:openshift-machine-config-operator:node-bootstrapper   Pending
    ...
    ```

    </div>

    In this example, two machines are joining the cluster. You might see more approved CSRs in the list.

3.  If the CSRs were not approved, after all of the pending CSRs for the machines you added are in `Pending` status, approve the CSRs for your cluster machines:

    > [!NOTE]
    > You must approve your CSRs within an hour of adding the machines to the cluster. If you do not approve them within an hour, the certificates will rotate, and more than two certificates will be present for each node. You must approve all of these certificates. After the client CSR is approved, the Kubelet creates a secondary CSR for the serving certificate, which requires manual approval. The subsequent serving certificate renewal requests are then automatically approved by the `machine-approver` if the Kubelet requests a new certificate with identical parameters.

    > [!NOTE]
    > For clusters running on platforms that are not machine API enabled, such as bare metal and other user-provisioned infrastructure, you must implement a method of automatically approving the kubelet serving certificate requests (CSRs). If a request is not approved, then the `oc exec`, `oc rsh`, and `oc logs` commands cannot succeed, because a serving certificate is required when the API server connects to the kubelet. Any operation that contacts the Kubelet endpoint requires this certificate approval to be in place. The method must watch for new CSRs, confirm that the CSR was submitted by the `node-bootstrapper` service account in the `system:node` or `system:admin` groups, and confirm the identity of the node.

    - To approve them individually, run the following command for each valid CSR:

      ``` terminal
      $ oc adm certificate approve <csr_name>
      ```

      where:

      `<csr_name>`
      Specifies the name of a CSR from the list of current CSRs.

    - To approve all pending CSRs, run the following command:

      ``` terminal
      $ oc get csr -o go-template='{{range .items}}{{if not .status}}{{.metadata.name}}{{"\n"}}{{end}}{{end}}' | xargs --no-run-if-empty oc adm certificate approve
      ```

      > [!NOTE]
      > Some Operators might not become available until some CSRs are approved.

4.  Now that your client requests are approved, you must review the server requests for each machine that you added to the cluster:

    ``` terminal
    $ oc get csr
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    NAME        AGE     REQUESTOR                                                                   CONDITION
    csr-bfd72   5m26s   system:node:ip-10-0-50-126.us-east-2.compute.internal                       Pending
    csr-c57lv   5m26s   system:node:ip-10-0-95-157.us-east-2.compute.internal                       Pending
    ...
    ```

    </div>

5.  If the remaining CSRs are not approved, and are in the `Pending` status, approve the CSRs for your cluster machines:

    - To approve them individually, run the following command for each valid CSR:

      ``` terminal
      $ oc adm certificate approve <csr_name>
      ```

      where:

      `<csr_name>`
      Specifies the name of a CSR from the list of current CSRs.

    - To approve all pending CSRs, run the following command:

      ``` terminal
      $ oc get csr -o go-template='{{range .items}}{{if not .status}}{{.metadata.name}}{{"\n"}}{{end}}{{end}}' | xargs oc adm certificate approve
      ```

6.  After all client and server CSRs have been approved, the machines have the `Ready` status. Verify this by running the following command:

    ``` terminal
    $ oc get nodes
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    NAME      STATUS    ROLES   AGE  VERSION
    master-0  Ready     master  73m  v1.33.4
    master-1  Ready     master  73m  v1.33.4
    master-2  Ready     master  74m  v1.33.4
    worker-0  Ready     worker  11m  v1.33.4
    worker-1  Ready     worker  11m  v1.33.4
    ```

    </div>

    > [!NOTE]
    > You might need to wait a few minutes after approval of the server CSRs for the machines to transition to the `Ready` status.

</div>

# Verifying a successful installation

Verify that the OpenShift Container Platform installation is complete.

<div>

<div class="title">

Prerequisites

</div>

- You have the installation program (`openshift-install`)

</div>

<div>

<div class="title">

Procedure

</div>

- On a command line, enter:

  ``` terminal
  $ openshift-install --log-level debug wait-for install-complete
  ```

</div>

The program outputs the console URL, as well as the administrator’s login information.

# Telemetry access for OpenShift Container Platform

To provide metrics about cluster health and the success of updates, the Telemetry service requires internet access. When connected, this service runs automatically by default and registers your cluster to [OpenShift Cluster Manager](https://console.redhat.com/openshift).

After you confirm that your [OpenShift Cluster Manager](https://console.redhat.com/openshift) inventory is correct, either maintained automatically by Telemetry or manually by using OpenShift Cluster Manager,use subscription watch to track your OpenShift Container Platform subscriptions at the account or multi-cluster level. For more information about subscription watch, see "Data Gathered and Used by Red Hat’s subscription services" in the *Additional resources* section.

<div>

<div class="title">

Additional resources

</div>

- See [About remote health monitoring](../../support/remote_health_monitoring/about-remote-health-monitoring.md#about-remote-health-monitoring) for more information about the Telemetry service

</div>

# Next steps

- [Customize your cluster](../../post_installation_configuration/cluster-tasks.md#available_cluster_customizations).

- If necessary, you can [Remote health reporting](../../support/remote_health_monitoring/remote-health-reporting.md#remote-health-reporting).

- If you need to enable external access to node ports, [configure ingress cluster traffic by using a node port](../../networking/ingress_load_balancing/configuring_ingress_cluster_traffic/configuring-ingress-cluster-traffic-nodeport.md#nw-using-nodeport_configuring-ingress-cluster-traffic-nodeport).

- If you did not configure RHOSP to accept application traffic over floating IP addresses, [configure RHOSP access with floating IP addresses](installing-openstack-network-config.md#installation-osp-configuring-api-floating-ip_installing-openstack-network-config).
