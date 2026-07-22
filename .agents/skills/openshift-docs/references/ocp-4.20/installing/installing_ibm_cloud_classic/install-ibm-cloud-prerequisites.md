<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

You can use installer-provisioned installation to install OpenShift Container Platform on IBM Cloud® Bare Metal (Classic) nodes. This document describes the prerequisites and procedures when installing OpenShift Container Platform on IBM Cloud® nodes.

> [!IMPORTANT]
> Red Hat supports IPMI and PXE on the provisioning network only. Red Hat has not tested Red Fish, virtual media, or other complementary technologies such as Secure Boot on IBM Cloud® deployments. A provisioning network is required.

Installer-provisioned installation of OpenShift Container Platform requires:

- One node with Red Hat Enterprise Linux CoreOS (RHCOS) 8.x installed, for running the provisioner

- Three control plane nodes

- One routable network

- One provisioning network

Before starting an installer-provisioned installation of OpenShift Container Platform on IBM Cloud® Bare Metal (Classic), address the following prerequisites and requirements.

# Setting up IBM Cloud Bare Metal (Classic) infrastructure

To deploy an OpenShift Container Platform cluster on IBM Cloud® Bare Metal (Classic) infrastructure, you must first provision the IBM Cloud® nodes.

> [!IMPORTANT]
> Red Hat supports IPMI and PXE on the `provisioning` network only. Red Hat has not tested Red Fish, virtual media, or other complementary technologies such as Secure Boot on IBM Cloud® deployments. The `provisioning` network is required.

You can customize IBM Cloud® nodes using the IBM Cloud® API. When creating IBM Cloud® nodes, you must consider the following requirements.

## Use one data center per cluster

All nodes in the OpenShift Container Platform cluster must run in the same IBM Cloud® data center.

## Create public and private VLANs

Create all nodes with a single public VLAN and a single private VLAN.

## Ensure subnets have sufficient IP addresses

IBM Cloud® public VLAN subnets use a `/28` prefix by default, which provides 16 IP addresses. That is sufficient for a cluster consisting of three control plane nodes, four worker nodes, and two IP addresses for the API VIP and Ingress VIP on the `baremetal` network. For larger clusters, you might need a smaller prefix.

IBM Cloud® private VLAN subnets use a `/26` prefix by default, which provides 64 IP addresses. IBM Cloud® Bare Metal (Classic) uses private network IP addresses to access the Baseboard Management Controller (BMC) of each node. OpenShift Container Platform creates an additional subnet for the `provisioning` network. Network traffic for the `provisioning` network subnet routes through the private VLAN. For larger clusters, you might need a smaller prefix.

| IP addresses | Prefix |
|--------------|--------|
| 32           | `/27`  |
| 64           | `/26`  |
| 128          | `/25`  |
| 256          | `/24`  |

IP addresses per prefix

## Configuring NICs

OpenShift Container Platform deploys with two networks:

- `provisioning`: The `provisioning` network is a non-routable network used for provisioning the underlying operating system on each node that is a part of the OpenShift Container Platform cluster.

- `baremetal`: The `baremetal` network is a routable network. You can use any NIC order to interface with the `baremetal` network, provided it is not the NIC specified in the `provisioningNetworkInterface` configuration setting or the NIC associated to a node’s `bootMACAddress` configuration setting for the `provisioning` network.

While the cluster nodes can contain more than two NICs, the installation process only focuses on the first two NICs. For example:

| NIC  | Network        | VLAN                  |
|------|----------------|-----------------------|
| NIC1 | `provisioning` | \<provisioning_vlan\> |
| NIC2 | `baremetal`    | \<baremetal_vlan\>    |

In the previous example, NIC1 on all control plane and worker nodes connects to the non-routable network (`provisioning`) that is only used for the installation of the OpenShift Container Platform cluster. NIC2 on all control plane and worker nodes connects to the routable `baremetal` network.

| PXE                                     | Boot order |
|-----------------------------------------|------------|
| NIC1 PXE-enabled `provisioning` network | 1          |
| NIC2 `baremetal` network.               | 2          |

> [!NOTE]
> Ensure PXE is enabled on the NIC used for the `provisioning` network and is disabled on all other NICs.

## Configuring canonical names

Clients access the OpenShift Container Platform cluster nodes over the `baremetal` network. Configure IBM Cloud® subdomains or subzones where the canonical name extension is the cluster name.

    <cluster_name>.<domain>

For example:

    test-cluster.example.com

## Creating DNS entries

You must create DNS `A` record entries resolving to unused IP addresses on the public subnet for the following:

| Usage             | Host Name                           | IP     |
|-------------------|-------------------------------------|--------|
| API               | api.\<cluster_name\>.\<domain\>     | \<ip\> |
| Ingress LB (apps) | \*.apps.\<cluster_name\>.\<domain\> | \<ip\> |

Control plane and worker nodes already have DNS entries after provisioning.

The following table provides an example of fully qualified domain names. The API and Nameserver addresses begin with canonical name extensions. The host names of the control plane and worker nodes are examples, so you can use any host naming convention you prefer.

| Usage             | Host Name                                      | IP     |
|-------------------|------------------------------------------------|--------|
| API               | api.\<cluster_name\>.\<domain\>                | \<ip\> |
| Ingress LB (apps) | \*.apps.\<cluster_name\>.\<domain\>            | \<ip\> |
| Provisioner node  | provisioner.\<cluster_name\>.\<domain\>        | \<ip\> |
| Master-0          | openshift-master-0.\<cluster_name\>.\<domain\> | \<ip\> |
| Master-1          | openshift-master-1.\<cluster_name\>.\<domain\> | \<ip\> |
| Master-2          | openshift-master-2.\<cluster_name\>.\<domain\> | \<ip\> |
| Worker-0          | openshift-worker-0.\<cluster_name\>.\<domain\> | \<ip\> |
| Worker-1          | openshift-worker-1.\<cluster_name\>.\<domain\> | \<ip\> |
| Worker-n          | openshift-worker-n.\<cluster_name\>.\<domain\> | \<ip\> |

OpenShift Container Platform includes functionality that uses cluster membership information to generate `A` records. This resolves the node names to their IP addresses. After the nodes are registered with the API, the cluster can disperse node information without using CoreDNS-mDNS. This eliminates the network traffic associated with multicast DNS.

> [!IMPORTANT]
> After provisioning the IBM Cloud® nodes, you must create a DNS entry for the `api.<cluster_name>.<domain>` domain name on the external DNS because removing CoreDNS causes the local entry to disappear. Failure to create a DNS record for the `api.<cluster_name>.<domain>` domain name in the external DNS server prevents worker nodes from joining the cluster.

## Network Time Protocol (NTP)

Each OpenShift Container Platform node in the cluster must have access to an NTP server. OpenShift Container Platform nodes use NTP to synchronize their clocks. For example, cluster nodes use SSL certificates that require validation, which might fail if the date and time between the nodes are not in sync.

> [!IMPORTANT]
> Define a consistent clock date and time format in each cluster node’s BIOS settings, or installation might fail.

## Configure a DHCP server

IBM Cloud® Bare Metal (Classic) does not run DHCP on the public or private VLANs. After provisioning IBM Cloud® nodes, you must set up a DHCP server for the public VLAN, which corresponds to OpenShift Container Platform’s `baremetal` network.

> [!NOTE]
> The IP addresses allocated to each node do not need to match the IP addresses allocated by the IBM Cloud® Bare Metal (Classic) provisioning system.

See the "Configuring the public subnet" section for details.

## Ensure BMC access privileges

The "Remote management" page for each node on the dashboard contains the node’s intelligent platform management interface (IPMI) credentials. The default IPMI privileges prevent the user from making certain boot target changes. You must change the privilege level to `OPERATOR` so that Ironic can make those changes.

In the `install-config.yaml` file, add the `privilegelevel` parameter to the URLs used to configure each BMC. See the "Configuring the install-config.yaml file" section for additional details. For example:

``` yaml
ipmi://<IP>:<port>?privilegelevel=OPERATOR
```

Alternatively, contact IBM Cloud® support and request that they increase the IPMI privileges to `ADMINISTRATOR` for each node.

## Create bare metal servers

Create bare metal servers in the [IBM Cloud® dashboard](https://cloud.ibm.com) by navigating to **Create resource** → **Bare Metal Servers for Classic**.

Alternatively, you can create bare metal servers with the `ibmcloud` CLI utility. For example:

``` terminal
$ ibmcloud sl hardware create --hostname <SERVERNAME> \
                            --domain <DOMAIN> \
                            --size <SIZE> \
                            --os <OS-TYPE> \
                            --datacenter <DC-NAME> \
                            --port-speed <SPEED> \
                            --billing <BILLING>
```

See [Installing the stand-alone IBM Cloud® CLI](https://cloud.ibm.com/docs/cli?topic=cli-install-ibmcloud-cli) for details on installing the IBM Cloud® CLI.

> [!NOTE]
> IBM Cloud® servers might take 3-5 hours to become available.
