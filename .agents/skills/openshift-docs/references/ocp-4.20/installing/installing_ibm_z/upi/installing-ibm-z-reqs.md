<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Before you begin an installation on IBM Z® infrastructure, be sure that your IBM Z® environment meets the following installation requirements.

For a cluster that contains user-provisioned infrastructure, you must deploy all of the required machines.

# Required machines for cluster installation

You must specify the minimum required machines or hosts for your cluster so that your cluster remains stable if a node fails.

The smallest OpenShift Container Platform clusters require the following hosts:

> [!IMPORTANT]
> For a cluster that contains user-provisioned infrastructure, you must deploy all of the required machines.

| Hosts | Description |
|----|----|
| One temporary bootstrap machine | The cluster requires the bootstrap machine to deploy the OpenShift Container Platform cluster on the three control plane machines. You can remove the bootstrap machine after you install the cluster. |
| Three control plane machines | The control plane machines run the Kubernetes and OpenShift Container Platform services that form the control plane. |
| At least two compute machines, which are also known as worker machines. | The workloads requested by OpenShift Container Platform users run on the compute machines. |

Minimum required hosts

> [!IMPORTANT]
> To improve high availability of your cluster, distribute the control plane machines over different hypervisor instances on at least two physical machines.

The bootstrap, control plane, and compute machines must use Red Hat Enterprise Linux CoreOS (RHCOS) as the operating system.

Note that RHCOS is based on Red Hat Enterprise Linux (RHEL) 9.2 and inherits all of its hardware certifications and requirements. See [Red Hat Enterprise Linux technology capabilities and limits](https://access.redhat.com/articles/rhel-limits).

## Minimum resource requirements for cluster installation

Each created cluster must meet minimum requirements so that the cluster runs as expected.

| Machine | Operating System | vCPU <sup>\[1\]</sup> | Virtual RAM | Storage | Input/Output Per Second (IOPS) |
|----|----|----|----|----|----|
| Bootstrap | RHCOS | 4 | 16 GB | 100 GB | N/A |
| Control plane | RHCOS | 4 | 16 GB | 100 GB | N/A |
| Compute | RHCOS | 2 | 8 GB | 100 GB | N/A |

Minimum resource requirements

1.  One physical core (IFL) provides two logical cores (threads) when SMT-2 is enabled. The hypervisor can provide two or more vCPUs.

> [!NOTE]
> For OpenShift Container Platform version 4.19, RHCOS is based on RHEL version 9.6, which updates the micro-architecture requirements. The following list contains the minimum instruction set architectures (ISA) that each architecture requires:
>
> - x86-64 architecture requires x86-64-v2 ISA
>
> - ARM64 architecture requires ARMv8.0-A ISA
>
> - IBM Power architecture requires Power 9 ISA
>
> - s390x architecture requires z14 ISA
>
> For more information, see "Architectures".

If an instance type for your platform meets the minimum requirements for cluster machines, it is supported to use in OpenShift Container Platform.

<div>

<div class="title">

Additional resources

</div>

- [Architectures (RHEL documentation)](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/9/html-single/9.2_release_notes/index#architectures)

</div>

<div>

<div class="title">

Additional resources

</div>

- See [Bridging a HiperSockets LAN with a z/VM Virtual Switch](https://www.ibm.com/docs/en/zvm/latest?topic=networks-bridging-hipersockets-lan-zvm-virtual-switch) in IBM® Documentation.

- See [Scaling HyperPAV alias devices on Linux guests on z/VM](https://public.dhe.ibm.com/software/dw/linux390/perf/zvm_hpav00.pdf) for performance optimization.

- [Processors Resource/Systems Manager Planning Guide](https://www.ibm.com/docs/en/systems-hardware/zsystems/3932-A02?topic=library-prsm-planning-guide) in IBM® Documentation for PR/SM mode considerations.

- [IBM Dynamic Partition Manager (DPM) Guide](https://www.ibm.com/docs/en/systems-hardware/zsystems/3932-A02?topic=library-dynamic-partition-manager-dpm-guide) in IBM® Documentation for DPM mode considerations.

- [Topics in LPAR performance](https://www.vm.ibm.com/library/presentations/lparperf.pdf) for LPAR weight management and entitlements.

- [Recommended host practices for IBM Z® & IBM® LinuxONE environments](../../../scalability_and_performance/ibm-z-recommended-host-practices.md#ibm-z-recommended-host-practices)

</div>

## Minimum IBM Z system environment

The following IBM® hardware is supported with OpenShift Container Platform version 4.17.

|  | z/VM | LPAR <sup>\[1\]</sup> | RHEL KVM <sup>\[2\]</sup> |
|----|----|----|----|
| IBM® z17 (all models) | supported | supported | supported |
| IBM® z16 (all models) | supported | supported | supported |
| IBM® z15 (all models) | supported | supported | supported |
| IBM® z14 (all models) | supported | supported | supported |
| IBM® LinuxONE 4 (all models) | supported | supported | supported |
| IBM® LinuxONE 5 (all models) | supported | supported | supported |
| IBM® LinuxONE III (all models) | supported | supported | supported |
| IBM® LinuxONE Emperor II | supported | supported | supported |
| IBM® LinuxONE Rockhopper II | supported | supported | supported |

Supported IBM® hardware

1.  When running OpenShift Container Platform on IBM Z® without a hypervisor use the Dynamic Partition Manager (DPM) to manage your machine.

2.  The RHEL KVM host in your environment must meet certain requirements to host the virtual machines that you plan for the OpenShift Container Platform environment. See [Enabling virtualization on IBM Z®](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/configuring_and_managing_virtualization/assembly_enabling-virtualization-in-rhel-9_configuring-and-managing-virtualization#enabling-virtualization-on-ibm-z_assembly_enabling-virtualization-in-rhel-9).

> [!NOTE]
> For detailed system requirements, see [Linux on IBM Z®/IBM® LinuxONE tested platforms](https://www.ibm.com/support/pages/linux-ibm-zibm-linuxone-tested-platforms) (IBM Support).

### Hardware requirements

- The equivalent of six Integrated Facilities for Linux (IFL), which are SMT2 enabled, for each cluster.

- At least one network connection to both connect to the `LoadBalancer` service and to serve data for traffic outside the cluster.

<div class="important">

<div class="title">

</div>

- You can use dedicated or shared IFLs to assign sufficient compute resources. Resource sharing is one of the key strengths of IBM Z®. However, you must adjust the capacity correctly on each hypervisor layer and ensure that there are sufficient resources for every OpenShift Container Platform cluster.

- Since the overall performance of the cluster can be impacted, the LPARs that are used to set up the OpenShift Container Platform clusters must provide sufficient compute capacity. In this context, LPAR weight management, entitlements, and CPU shares on the hypervisor level play an important role. For more information, see "Recommended host practices for IBM Z & IBM LinuxONE environments".

</div>

### IBM Z operating system requirements

|  | z/VM | LPAR | RHEL KVM |
|----|----|----|----|
| Hypervisor | One instance of z/VM 7.2 or later | IBM® z14 or later with DPM or PR/SM | One LPAR running on RHEL 8.6 or later with KVM, which is managed by libvirt |
| OpenShift Container Platform control plane machines | Three guest virtual machines | Three LPARs | Three guest virtual machines |
| OpenShift Container Platform compute machines | Two guest virtual machines | Two LPARs | Two guest virtual machines |
| Temporary OpenShift Container Platform bootstrap machine | One machine | One machine | One machine |

Operating system requirements

### IBM Z network connectivity

<table>
<caption>Network connectivity requirements</caption>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;"></th>
<th style="text-align: left;">z/VM</th>
<th style="text-align: left;">LPAR</th>
<th style="text-align: left;">RHEL KVM</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>Network Interface Card (NIC)</p></td>
<td style="text-align: left;"><p>One single z/VM virtual NIC in layer 2 mode</p></td>
<td style="text-align: left;"><p>-</p></td>
<td style="text-align: left;"><p>-</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Virtual switch (vSwitch)</p></td>
<td style="text-align: left;"><p>z/VM VSWITCH in layer 2 Ethernet mode</p></td>
<td style="text-align: left;"><p>-</p></td>
<td style="text-align: left;"><p>-</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Network adapter</p></td>
<td style="text-align: left;"><p>Direct-attached OSA, RoCE, or HiperSockets</p></td>
<td style="text-align: left;"><p>Direct-attached OSA, RoCE, or HiperSockets</p></td>
<td style="text-align: left;"><p>A RHEL KVM host configured with OSA, RoCE, or HiperSockets</p>
<p>Either a RHEL KVM host that is configured to use bridged networking in libvirt or MacVTap to connect the network to the guests.</p>
<p>See <a href="https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8/html-single/configuring_and_managing_virtualization/index#types-of-virtual-machine-network-connections_configuring-virtual-machine-network-connections">Types of virtual network connections</a>.</p></td>
</tr>
</tbody>
</table>

#### Disk storage

|  | z/VM | LPAR | RHEL KVM |
|----|----|----|----|
| Fibre Connection (FICON) | z/VM minidisks, fullpack minidisks, or dedicated DASDs, all of which must be formatted as CDL, which is the default. To reach the minimum required DASD size for Red Hat Enterprise Linux CoreOS (RHCOS) installations, you need extended address volumes (EAV). If available, use HyperPAV to ensure optimal performance. | Dedicated DASDs that must be formatted as CDL, which is the default. To reach the minimum required DASD size for Red Hat Enterprise Linux CoreOS (RHCOS) installations, you need extended address volumes (EAV). If available, use HyperPAV to ensure optimal performance. | Virtual block device |
| Fibre Channel Protocol (FCP) | Dedicated FCP or EDEV | Dedicated FCP or EDEV | Virtual block device |
| QCOW | Not supported | Not supported | Supported |
| NVMe | Not supported | Supported | Virtual block device |

Disk storage requirements

## Preferred IBM Z system environment

The preferred system environment for running OpenShift Container Platform version 4.17 on IBM Z® hardware is as follows:

### Hardware requirements

- Three logical partitions (LPARs) that each have the equivalent of six Integrated Facilities for Linux (IFLs), which are SMT2 enabled, for each cluster.

- Two network connections to both connect to the `LoadBalancer` service and to serve data for traffic outside the cluster.

- HiperSockets that are attached to a node directly as a device. To directly connect HiperSockets to a node, you must set up a gateway to the external network via a RHEL 8 guest to bridge to the HiperSockets network.

  > [!NOTE]
  > When installing in a z/VM environment, you can also bridge HiperSockets with one z/VM VSWITCH to be transparent to the z/VM guest.

### IBM Z operating system requirements

|  | z/VM <sup>\[1\]</sup> | LPAR | RHEL KVM |
|----|----|----|----|
| Hypervisor | One instance of z/VM 7.2 or later | IBM® z14 or later with DPM or PR/S | One LPAR running on RHEL 8.6 or later with KVM, which is managed by libvirt |
| OpenShift Container Platform control plane machines | Three guest virtual machines | Three LPARs | Three guest virtual machines |
| OpenShift Container Platform compute machines | Six guest virtual machines | Six LPARs | Six guest virtual machines |
| Temporary OpenShift Container Platform bootstrap machine | One machine | One machine | One machine |

Operating system requirements

1.  To ensure the availability of integral components in an overcommitted environment, increase the priority of the control plane by using the CP command `SET SHARE`. Do the same for infrastructure nodes, if they exist. See [SET SHARE](https://www.ibm.com/docs/en/zvm/latest?topic=commands-set-share) (IBM® Documentation).

<div>

<div class="title">

Additional resources

</div>

- [Optimizing storage](../../../scalability_and_performance/optimization/optimizing-storage.md#optimizing-storage)

</div>

## Certificate signing requests management

On user-provisioned infrastructure, you must provide a mechanism for approving cluster certificate signing requests (CSRs) after installation when your cluster has limited access to automatic machine management.

The `kube-controller-manager` only approves the kubelet client CSRs. The `machine-approver` cannot guarantee the validity of a serving certificate that is requested by using kubelet credentials because it cannot confirm that the correct machine issued the request. You must determine and implement a method of verifying the validity of the kubelet serving certificate requests and approving them.

## Networking requirements for user-provisioned infrastructure

You must configure networking for all the Red Hat Enterprise Linux CoreOS (RHCOS) machines in `initramfs` during boot, so that they can fetch their Ignition config files.

During the initial boot, the machines require an IP address configuration that is set either through a DHCP server or statically by providing the required boot options. After a network connection is established, the machines download their Ignition config files from an HTTP or HTTPS server. The Ignition config files are then used to set the exact state of each machine. The Machine Config Operator completes more changes to the machines, such as the application of new certificates or keys, after installation.

<div class="note">

<div class="title">

</div>

- Consider using a DHCP server for long-term management of the cluster machines. Ensure that the DHCP server is configured to provide persistent IP addresses, DNS server information, and hostnames to the cluster machines.

- If a DHCP service is not available for your user-provisioned infrastructure, you can instead provide the IP networking configuration and the address of the DNS server to the nodes at RHCOS install time. These can be passed as boot arguments if you are installing from an ISO image. See the *Installing RHCOS and starting the OpenShift Container Platform bootstrap process* section for more information about static IP provisioning and advanced networking options.

</div>

The Kubernetes API server must be able to resolve the node names of the cluster machines. If the API servers and worker nodes are in different zones, you can configure a default DNS search zone to allow the API server to resolve the node names. Another supported approach is to always refer to hosts by their fully-qualified domain names in both the node objects and all DNS requests.

### Setting the cluster node hostnames through DHCP

On Red Hat Enterprise Linux CoreOS (RHCOS) machines, the hostname is set through NetworkManager. By default, the machines obtain their hostname through DHCP. If the hostname is not provided by DHCP, set statically through kernel arguments, or another method, it is obtained through a reverse DNS lookup. Reverse DNS lookup occurs after the network has been initialized on a node and can take time to resolve. Other system services can start prior to this and detect the hostname as `localhost` or similar. You can avoid this by using DHCP to provide the hostname for each cluster node.

Additionally, setting the hostnames through DHCP can bypass any manual DNS record name configuration errors in environments that have a DNS split-horizon implementation.

### Network connectivity requirements

You must configure the network connectivity between machines to allow OpenShift Container Platform cluster components to communicate. Each machine must be able to resolve the hostnames of all other machines in the cluster.

This section provides details about the ports that are required.

> [!IMPORTANT]
> In connected OpenShift Container Platform environments, all nodes are required to have internet access to pull images for platform containers and provide telemetry data to Red Hat.

| Protocol | Port | Description |
|----|----|----|
| ICMP | N/A | Network reachability tests |
| TCP | `1936` | Metrics |
| `9000`-`9999` | Host level services, including the node exporter on ports `9100`-`9101` and the Cluster Version Operator on port `9099`. |  |
| `10250`-`10259` | The default ports that Kubernetes reserves |  |
| `22623` | The port handles traffic from the Machine Config Server and directs the traffic to the control plane machines. |  |
| UDP | `6081` | Geneve |
| `9000`-`9999` | Host level services, including the node exporter on ports `9100`-`9101`. |  |
| `500` | IPsec IKE packets |  |
| `4500` | IPsec NAT-T packets |  |
| `123` | Network Time Protocol (NTP) on UDP port `123`. If an external NTP time server is configured, you must open UDP port `123`. |  |
| TCP/UDP | `30000`-`32767` |  |
| Kubernetes node port | ESP | N/A |

Ports used for all-machine to all-machine communications

| Protocol | Port   | Description    |
|----------|--------|----------------|
| TCP      | `6443` | Kubernetes API |

Ports used for all-machine to control plane communications

| Protocol | Port          | Description                |
|----------|---------------|----------------------------|
| TCP      | `2379`-`2380` | etcd server and peer ports |

Ports used for control plane machine to control plane machine communications

### NTP configuration for user-provisioned infrastructure

OpenShift Container Platform clusters are configured to use a public Network Time Protocol (NTP) server by default. If you want to use a local enterprise NTP server, or if your cluster is being deployed in a disconnected network, you can configure the cluster to use a specific time server. For more information, see the documentation for *Configuring chrony time service*.

If a DHCP server provides NTP server information, the chrony time service on the Red Hat Enterprise Linux CoreOS (RHCOS) machines read the information and can sync the clock with the NTP servers.

<div>

<div class="title">

Additional resources

</div>

- [Configuring chrony time service](../../install_config/installing-customizing.md#installation-special-config-chrony_installing-customizing)

</div>

## User-provisioned DNS requirements

In OpenShift Container Platform deployments, you must ensure that cluster components meet certain DNS name resolution criteria for internal communication, certificate validation, and automated node discovery purposes.

The following is a list of required cluster components:

- The Kubernetes API

- The OpenShift Container Platform application wildcard

- The bootstrap and control plane machines

- The compute machines

Reverse DNS resolution is also required for the Kubernetes API, the bootstrap machine, the control plane machines, and the compute machines.

DNS A/AAAA or CNAME records are used for name resolution and PTR records are used for reverse name resolution. The reverse records are important because Red Hat Enterprise Linux CoreOS (RHCOS) uses the reverse records to set the hostnames for all the nodes, unless the hostnames are provided by DHCP. Additionally, the reverse records are used to generate the certificate signing requests (CSR) that OpenShift Container Platform needs to operate.

> [!NOTE]
> It is recommended to use a DHCP server to provide the hostnames to each cluster node. See the *DHCP recommendations for user-provisioned infrastructure* section for more information.

The following DNS records are required for a user-provisioned OpenShift Container Platform cluster and they must be in place before installation. In each record, `<cluster_name>` is the cluster name and `<base_domain>` is the base domain that you specify in the `install-config.yaml` file. A complete DNS record takes the form: `<component>.<cluster_name>.<base_domain>.`.

<table>
<caption>Required DNS records</caption>
<colgroup>
<col style="width: 11%" />
<col style="width: 33%" />
<col style="width: 55%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Component</th>
<th style="text-align: left;">Record</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>Kubernetes API</p></td>
<td style="text-align: left;"><p><code>api.&lt;cluster_name&gt;.&lt;base_domain&gt;.</code></p></td>
<td style="text-align: left;"><p>A DNS A/AAAA or CNAME record, and a DNS PTR record, to identify the API load balancer. These records must be resolvable by both clients external to the cluster and from all the nodes within the cluster.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>api-int.&lt;cluster_name&gt;.&lt;base_domain&gt;.</code></p></td>
<td style="text-align: left;"><p>A DNS A/AAAA or CNAME record, and a DNS PTR record, to internally identify the API load balancer. These records must be resolvable from all the nodes within the cluster.</p>
<div class="important">
<div class="title">
&#10;</div>
<p>The API server must be able to resolve the worker nodes by the hostnames that are recorded in Kubernetes. If the API server cannot resolve the node names, then proxied API calls can fail, and you cannot retrieve logs from pods.</p>
</div></td>
<td></td>
</tr>
<tr>
<td style="text-align: left;"><p>Routes</p></td>
<td style="text-align: left;"><p><code>*.apps.&lt;cluster_name&gt;.&lt;base_domain&gt;.</code></p></td>
<td style="text-align: left;"><p>A wildcard DNS A/AAAA or CNAME record that refers to the application ingress load balancer. The application ingress load balancer targets the machines that run the Ingress Controller pods. The Ingress Controller pods run on the compute machines by default. These records must be resolvable by both clients external to the cluster and from all the nodes within the cluster.</p>
<p>For example, <code>console-openshift-console.apps.&lt;cluster_name&gt;.&lt;base_domain&gt;</code> is used as a wildcard route to the OpenShift Container Platform console.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Bootstrap machine</p></td>
<td style="text-align: left;"><p><code>bootstrap.&lt;cluster_name&gt;.&lt;base_domain&gt;.</code></p></td>
<td style="text-align: left;"><p>A DNS A/AAAA or CNAME record, and a DNS PTR record, to identify the bootstrap machine. These records must be resolvable by the nodes within the cluster.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Control plane machines</p></td>
<td style="text-align: left;"><p><code>&lt;control_plane&gt;&lt;n&gt;.&lt;cluster_name&gt;.&lt;base_domain&gt;.</code></p></td>
<td style="text-align: left;"><p>DNS A/AAAA or CNAME records and DNS PTR records to identify each machine for the control plane nodes. These records must be resolvable by the nodes within the cluster.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Compute machines</p></td>
<td style="text-align: left;"><p><code>&lt;compute&gt;&lt;n&gt;.&lt;cluster_name&gt;.&lt;base_domain&gt;.</code></p></td>
<td style="text-align: left;"><p>DNS A/AAAA or CNAME records and DNS PTR records to identify each machine for the worker nodes. These records must be resolvable by the nodes within the cluster.</p></td>
</tr>
</tbody>
</table>

> [!NOTE]
> In OpenShift Container Platform 4.4 and later, you do not need to specify etcd host and SRV records in your DNS configuration.

> [!TIP]
> You can use the `dig` command to verify name and reverse name resolution. See the section on *Validating DNS resolution for user-provisioned infrastructure* for detailed validation steps.

### Example DNS configuration for user-provisioned clusters

Reference the example DNS configurations to understand how A and PTR record configuration samples meet the DNS requirements for deploying OpenShift Container Platform on user-provisioned infrastructure.

The DNS configuration examples provided here are for reference only and are not meant to provide advice for choosing one DNS solution over another.

In the examples, the cluster name is `ocp4` and the base domain is `example.com`.

The following example is a BIND zone file that shows sample DNS A records for name resolution in a user-provisioned cluster.

> [!NOTE]
> In the example, the same load balancer is used for the Kubernetes API and application ingress traffic. In production scenarios, you can deploy the API and application ingress load balancers separately so that you can scale the load balancer infrastructure for each in isolation.

``` text
$TTL 1W
@   IN  SOA ns1.example.com.    root (
            2019070700  ; serial
            3H      ; refresh (3 hours)
            30M     ; retry (30 minutes)
            2W      ; expiry (2 weeks)
            1W )        ; minimum (1 week)
    IN  NS  ns1.example.com.
    IN  MX 10   smtp.example.com.
;
;
ns1.example.com.        IN  A   192.168.1.5
smtp.example.com.       IN  A   192.168.1.5
;
helper.example.com.     IN  A   192.168.1.5
helper.ocp4.example.com.    IN  A   192.168.1.5
;
api.ocp4.example.com.       IN  A   192.168.1.5
api-int.ocp4.example.com.   IN  A   192.168.1.5
;
*.apps.ocp4.example.com.    IN  A   192.168.1.5
;
bootstrap.ocp4.example.com. IN  A   192.168.1.96
;
control-plane0.ocp4.example.com.    IN  A   192.168.1.97
control-plane1.ocp4.example.com.    IN  A   192.168.1.98
;
control-plane2.ocp4.example.com.    IN  A   192.168.1.99
;
compute0.ocp4.example.com.  IN  A   192.168.1.11
compute1.ocp4.example.com.  IN  A   192.168.1.7
;
;EOF
```

where:

`api.ocp4.example.com.`
Provides name resolution for the Kubernetes API. The record refers to the IP address of the API load balancer.

`api-int.ocp4.example.com.`
Provides name resolution for the Kubernetes API. The record refers to the IP address of the API load balancer and is used for internal cluster communications.

`*.apps.ocp4.example.com.`
Provides name resolution for the wildcard routes. The record refers to the IP address of the application ingress load balancer. The application ingress load balancer targets the machines that run the Ingress Controller pods.

`bootstrap.ocp4.example.com`
Provides name resolution for the bootstrap machine.

`control-plane0.ocp4.example.com`
Provides name resolution for the control plane machines.

`compute0.ocp4.example.com.`
Provides name resolution for the compute machines.

The following example BIND zone file shows sample PTR records for reverse name resolution in a user-provisioned cluster:

``` text
$TTL 1W
@   IN  SOA ns1.example.com.    root (
            2019070700  ; serial
            3H      ; refresh (3 hours)
            30M     ; retry (30 minutes)
            2W      ; expiry (2 weeks)
            1W )        ; minimum (1 week)
    IN  NS  ns1.example.com.
;
5.1.168.192.in-addr.arpa.   IN  PTR api.ocp4.example.com.
5.1.168.192.in-addr.arpa.   IN  PTR api-int.ocp4.example.com.
;
96.1.168.192.in-addr.arpa.  IN  PTR bootstrap.ocp4.example.com.
;
97.1.168.192.in-addr.arpa.  IN  PTR control-plane0.ocp4.example.com.
98.1.168.192.in-addr.arpa.  IN  PTR control-plane1.ocp4.example.com.
;
99.1.168.192.in-addr.arpa.  IN  PTR control-plane2.ocp4.example.com.
;
11.1.168.192.in-addr.arpa.  IN  PTR compute0.ocp4.example.com.
7.1.168.192.in-addr.arpa.   IN  PTR compute1.ocp4.example.com.
;
;EOF
```

where:

`api.ocp4.example.com.`
Provides reverse DNS resolution for the Kubernetes API. The PTR record refers to the record name of the API load balancer.

`api-int.ocp4.example.com.`
Provides reverse DNS resolution for the Kubernetes API. The PTR record refers to the record name of the API load balancer and is used for internal cluster communications.

`bootstrap.ocp4.example.com.`
Provides reverse DNS resolution for the bootstrap machine.

`control-plane0.ocp4.example.com.`
Provides rebootstrap.ocp4.example.com.verse DNS resolution for the control plane machines.

`compute0.ocp4.example.com.`
Provides reverse DNS resolution for the compute machines.

> [!NOTE]
> A PTR record is not required for the OpenShift Container Platform application wildcard.

## Load balancing requirements for user-provisioned infrastructure

Before you install OpenShift Container Platform, you must provision the API and application Ingress load balancing infrastructure. In production scenarios, you can deploy the API and application Ingress load balancers separately so that you can scale the load balancer infrastructure for each in isolation.

> [!NOTE]
> If you want to deploy the API and application Ingress load balancers with a Red Hat Enterprise Linux (RHEL) instance, you must purchase the RHEL subscription separately.

The load balancing infrastructure must meet the following requirements:

- API load balancer: Provides a common endpoint for users, both human and machine, to interact with and configure the platform. Configure the following conditions:

  - Layer 4 load balancing only. This can be referred to as Raw TCP or SSL Passthrough mode.

  - A stateless load balancing algorithm. The options vary based on the load balancer implementation.

> [!IMPORTANT]
> Do not configure session persistence for an API load balancer. Configuring session persistence for a Kubernetes API server might cause performance issues from excess application traffic for your OpenShift Container Platform cluster and the Kubernetes API that runs inside the cluster.

Configure the following ports on both the front and back of the API load balancers:

| Port | Back-end machines (pool members) | Internal | External | Description |
|----|----|----|----|----|
| `6443` | Bootstrap and control plane. You remove the bootstrap machine from the load balancer after the bootstrap machine initializes the cluster control plane. You must configure the `/readyz` endpoint for the API server health check probe. | X | X | Kubernetes API server |
| `22623` | Bootstrap and control plane. You remove the bootstrap machine from the load balancer after the bootstrap machine initializes the cluster control plane. | X |  | Machine config server |

> [!NOTE]
> The load balancer must be configured to take a maximum of 30 seconds from the time the API server turns off the `/readyz` endpoint to the removal of the API server instance from the pool. Within the time frame after `/readyz` returns an error or becomes healthy, the endpoint must have been removed or added. Probing every 5 or 10 seconds, with two successful requests to become healthy and three to become unhealthy, are well-tested values.

- Application Ingress load balancer: Provides an ingress point for application traffic flowing in from outside the cluster. A working configuration for the Ingress router is required for an OpenShift Container Platform cluster. Configure the following conditions:

  - Layer 4 load balancing only. This can be referred to as Raw TCP or SSL Passthrough mode.

  - A connection-based or session-based persistence is recommended, based on the options available and types of applications that will be hosted on the platform.

> [!TIP]
> If the true IP address of the client can be seen by the application Ingress load balancer, enabling source IP-based session persistence can improve performance for applications that use end-to-end TLS encryption.

Configure the following ports on both the front and back of the load balancers:

| Port | Back-end machines (pool members) | Internal | External | Description |
|----|----|----|----|----|
| `443` | The machines that run the Ingress Controller pods, compute, or worker, by default. | X | X | HTTPS traffic |
| `80` | The machines that run the Ingress Controller pods, compute, or worker, by default. | X | X | HTTP traffic |

Application Ingress load balancer

> [!NOTE]
> If you are deploying a three-node cluster with zero compute nodes, the Ingress Controller pods run on the control plane nodes. In three-node cluster deployments, you must configure your application Ingress load balancer to route HTTP and HTTPS traffic to the control plane nodes.
