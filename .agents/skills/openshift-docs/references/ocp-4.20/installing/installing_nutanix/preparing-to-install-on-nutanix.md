<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

You can install an OpenShift Container Platform cluster on Nutanix by using a variety of different installation methods. Each method has qualities that can make the method more suitable for different use cases, such as installing a cluster in a disconnected environment or installing a cluster that requires minimal configuration and provisioning. Before you install OpenShift Container Platform, ensure that your Nutanix environment meets specific requirements.

# Nutanix version requirements

You must install the OpenShift Container Platform cluster to a Nutanix environment that meets the following requirements:

| Component     | Required version   |
|---------------|--------------------|
| Nutanix AOS   | 6.5.2.7 or later   |
| Prism Central | pc.2022.6 or later |

Version requirements for Nutanix virtual environments

# Agent-based Installer

You can install an OpenShift Container Platform cluster on Nutanix by using the Agent-based Installer. For example, the Agent-based Installer can be used to install a three-node cluster, which is a smaller, more resource efficient cluster for testing, development, and production. See [Preparing to install with the Agent-based Installer](../installing_with_agent_based_installer/preparing-to-install-with-agent-based-installer.md#preparing-to-install-with-agent-based-installer) for additional details.

# Environment requirements

Before you install an OpenShift Container Platform cluster, review the following Nutanix AOS environment requirements.

## Infrastructure requirements

You can install OpenShift Container Platform on on-premise Nutanix clusters, Nutanix Cloud Clusters (NC2) on Amazon Web Services (AWS), or NC2 on Microsoft Azure.

For more information, see [Nutanix Cloud Clusters on AWS](https://www.nutanix.com/products/nutanix-cloud-clusters/aws) and [Nutanix Cloud Clusters on Microsoft Azure](https://www.nutanix.com/products/nutanix-cloud-clusters/azure).

## Required account privileges

The installation program requires access to a Nutanix account with the necessary permissions to deploy the cluster and to maintain the daily operation of it. The following options are available to you:

- You can use a local Prism Central user account with administrative privileges. Using a local account is the quickest way to grant access to an account with the required permissions.

- If your organization’s security policies require that you use a more restrictive set of permissions, use the permissions that are listed in the following table to create a custom Cloud Native role in Prism Central. You can then assign the role to a user account that is a member of a Prism Central authentication directory.

Consider the following when managing this user account:

- When assigning entities to the role, ensure that the user can access only the Prism Element and subnet that are required to deploy the virtual machines.

- Ensure that the user is a member of the project to which it needs to assign virtual machines.

For more information, see the Nutanix documentation about creating a [Custom Cloud Native role](https://opendocs.nutanix.com/guides/cloud_native_role/), [assigning a role](https://portal.nutanix.com/page/documents/details?targetId=Nutanix-Security-Guide:ssp-ssp-role-assignment-pc-t.html), and [adding a user to a project](https://portal.nutanix.com/page/documents/details?targetId=Prism-Central-Admin-Center-Guide-vpc_2023_1_0_1:ssp-projects-add-users-t.html).

<div class="example">

<div class="title">

Required permissions for creating a Custom Cloud Native role

</div>

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Nutanix Object</th>
<th style="text-align: left;">When required</th>
<th style="text-align: left;">Required permissions in Nutanix API</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>Categories</p></td>
<td style="text-align: left;"><p>Always</p></td>
<td style="text-align: left;"><p><code>Create_Category_Mapping</code><br />
<code>Create_Or_Update_Name_Category</code><br />
<code>Create_Or_Update_Value_Category</code><br />
<code>Delete_Category_Mapping</code><br />
<code>Delete_Name_Category</code><br />
<code>Delete_Value_Category</code><br />
<code>View_Category_Mapping</code><br />
<code>View_Name_Category</code><br />
<code>View_Value_Category</code></p></td>
<td style="text-align: left;"><p>Create, read, and delete categories that are assigned to the OpenShift Container Platform machines.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Images</p></td>
<td style="text-align: left;"><p>Always</p></td>
<td style="text-align: left;"><p><code>Create_Image</code><br />
<code>Delete_Image</code><br />
<code>View_Image</code></p></td>
<td style="text-align: left;"><p>Create, read, and delete the operating system images used for the OpenShift Container Platform machines.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Virtual Machines</p></td>
<td style="text-align: left;"><p>Always</p></td>
<td style="text-align: left;"><p><code>Create_Virtual_Machine</code><br />
<code>Delete_Virtual_Machine</code><br />
<code>View_Virtual_Machine</code></p></td>
<td style="text-align: left;"><p>Create, read, and delete the OpenShift Container Platform machines.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Clusters</p></td>
<td style="text-align: left;"><p>Always</p></td>
<td style="text-align: left;"><p><code>View_Cluster</code></p></td>
<td style="text-align: left;"><p>View the Prism Element clusters that host the OpenShift Container Platform machines.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Subnets</p></td>
<td style="text-align: left;"><p>Always</p></td>
<td style="text-align: left;"><p><code>View_Subnet</code></p></td>
<td style="text-align: left;"><p>View the subnets that host the OpenShift Container Platform machines.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Projects</p></td>
<td style="text-align: left;"><p>If you will associate a project with compute machines, control plane machines, or all machines.</p></td>
<td style="text-align: left;"><p><code>View_Project</code></p></td>
<td style="text-align: left;"><p>View the projects defined in Prism Central and allow a project to be assigned to the OpenShift Container Platform machines.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Tasks</p></td>
<td style="text-align: left;"><p>Always</p></td>
<td style="text-align: left;"><p><code>View_Task</code></p></td>
<td style="text-align: left;"><p>Fetch and view tasks on the Prism Element that contain OpenShift Container Platform machines and nodes.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Hosts</p></td>
<td style="text-align: left;"><p>If you use GPUs with compute machines.</p></td>
<td style="text-align: left;"><p><code>View_Host</code></p></td>
<td style="text-align: left;"><p>Fetch and view hosts on the Prism Element that have GPUs attached.</p></td>
</tr>
</tbody>
</table>

</div>

## Cluster limits

Available resources vary between clusters. The number of possible clusters within a Nutanix environment is limited primarily by available storage space and any limitations associated with the resources that the cluster creates, and resources that you require to deploy the cluster, such a IP addresses and networks.

## Cluster resources

A minimum of 800 GB of storage is required to use a standard cluster.

When you deploy a OpenShift Container Platform cluster that uses installer-provisioned infrastructure, the installation program must be able to create several resources in your Nutanix instance. Although these resources use 856 GB of storage, the bootstrap node is destroyed as part of the installation process.

A standard OpenShift Container Platform installation creates the following resources:

- 1 label

- Virtual machines:

  - 1 disk image

  - 1 temporary bootstrap node

  - 3 control plane nodes

  - 3 compute machines

## Networking requirements

You must use either AHV IP Address Management (IPAM) or Dynamic Host Configuration Protocol (DHCP) for the network and ensure that it is configured to provide persistent IP addresses to the cluster machines. Additionally, create the following networking resources before you install the OpenShift Container Platform cluster:

- IP addresses

- DNS records

Nutanix Flow Virtual Networking is supported for new cluster installations. To use this feature, enable Flow Virtual Networking on your AHV cluster before installing. For more information, see [Flow Virtual Networking overview](https://portal.nutanix.com/page/documents/details?targetId=Nutanix-Flow-Virtual-Networking-Guide-vpc_2024_1:ear-flow-nw-overview-pc.html).

> [!NOTE]
> It is recommended that each OpenShift Container Platform node in the cluster have access to a Network Time Protocol (NTP) server that is discoverable via DHCP. Installation is possible without an NTP server. However, an NTP server prevents errors typically associated with asynchronous server clocks.

### Required IP Addresses

An installer-provisioned installation requires two static virtual IP (VIP) addresses:

- A VIP address for the API is required. This address is used to access the cluster API.

- A VIP address for ingress is required. This address is used for cluster ingress traffic.

You specify these IP addresses when you install the OpenShift Container Platform cluster.

### DNS records

You must create DNS records for two static IP addresses in the appropriate DNS server for the Nutanix instance that hosts your OpenShift Container Platform cluster. In each record, `<cluster_name>` is the cluster name and `<base_domain>` is the cluster base domain that you specify when you install the cluster.

If you use your own DNS or DHCP server, you must also create records for each node, including the bootstrap, control plane, and compute nodes.

A complete DNS record takes the form: `<component>.<cluster_name>.<base_domain>.`.

| Component | Record | Description |
|----|----|----|
| API VIP | `api.<cluster_name>.<base_domain>.` | This DNS A/AAAA or CNAME record must point to the load balancer for the control plane machines. This record must be resolvable by both clients external to the cluster and from all the nodes within the cluster. |
| Ingress VIP | `*.apps.<cluster_name>.<base_domain>.` | A wildcard DNS A/AAAA or CNAME record that points to the load balancer that targets the machines that run the Ingress router pods, which are the worker nodes by default. This record must be resolvable by both clients external to the cluster and from all the nodes within the cluster. |

Required DNS records

# Configuring the Cloud Credential Operator utility

The Cloud Credential Operator (CCO) manages cloud provider credentials as Kubernetes custom resource definitions (CRDs). To install a cluster on Nutanix, you must set the CCO to `manual` mode as part of the installation process.

To create and manage cloud credentials from outside of the cluster when the Cloud Credential Operator (CCO) is operating in manual mode, extract and prepare the CCO utility (`ccoctl`) binary.

> [!NOTE]
> The `ccoctl` utility is a Linux binary that must run in a Linux environment.

<div>

<div class="title">

Prerequisites

</div>

- You have access to an OpenShift Container Platform account with cluster administrator access.

- You have installed the OpenShift CLI (`oc`).

</div>

<div>

<div class="title">

Procedure

</div>

1.  Set a variable for the OpenShift Container Platform release image by running the following command:

    ``` terminal
    $ RELEASE_IMAGE=$(./openshift-install version | awk '/release image/ {print $3}')
    ```

2.  Obtain the CCO container image from the OpenShift Container Platform release image by running the following command:

    ``` terminal
    $ CCO_IMAGE=$(oc adm release info --image-for='cloud-credential-operator' $RELEASE_IMAGE -a ~/.pull-secret)
    ```

    > [!NOTE]
    > Ensure that the architecture of the `$RELEASE_IMAGE` matches the architecture of the environment in which you will use the `ccoctl` tool.

3.  Extract the `ccoctl` binary from the CCO container image within the OpenShift Container Platform release image by running the following command:

    ``` terminal
    $ oc image extract $CCO_IMAGE \
      --file="/usr/bin/ccoctl.<rhel_version>" \
      -a ~/.pull-secret
    ```

    For `<rhel_version>`, specify the value that corresponds to the version of Red Hat Enterprise Linux (RHEL) that the host uses. If no value is specified, `ccoctl.rhel8` is used by default. The following values are valid:

    - `rhel8`: Specify this value for hosts that use RHEL 8.

    - `rhel9`: Specify this value for hosts that use RHEL 9.

    > [!NOTE]
    > The `ccoctl` binary is created in the directory from where you executed the command and not in `/usr/bin/`. You must rename the directory or move the `ccoctl.<rhel_version>` binary to `ccoctl`.

4.  Change the permissions to make `ccoctl` executable by running the following command:

    ``` terminal
    $ chmod 775 ccoctl
    ```

</div>

<div>

<div class="title">

Verification

</div>

- To verify that `ccoctl` is ready to use, display the help file. Use a relative file name when you run the command, for example:

  ``` terminal
  $ ./ccoctl
  ```

  <div class="formalpara">

  <div class="title">

  Example output

  </div>

  ``` terminal
  OpenShift credentials provisioning tool

  Usage:
    ccoctl [command]

  Available Commands:
    aws          Manage credentials objects for AWS cloud
    azure        Manage credentials objects for Azure
    gcp          Manage credentials objects for Google cloud
    help         Help about any command
    ibmcloud     Manage credentials objects for IBM Cloud
    nutanix      Manage credentials objects for Nutanix

  Flags:
    -h, --help   help for ccoctl

  Use "ccoctl [command] --help" for more information about a command.
  ```

  </div>

</div>

<div>

<div class="title">

Additional resources

</div>

- [Preparing to update a cluster with manually maintained credentials](../../updating/preparing_for_updates/preparing-manual-creds-update.md#preparing-manual-creds-update)

</div>
