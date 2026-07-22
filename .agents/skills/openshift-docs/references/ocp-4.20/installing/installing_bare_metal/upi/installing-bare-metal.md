<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

To optimize performance and maintain more control over your hardware in OpenShift Container Platform 4.17, you can install a cluster on bare-metal infrastructure that you provision.

> [!IMPORTANT]
> While you might be able to follow this procedure to deploy a cluster on virtualized or cloud environments, you must be aware of additional considerations for non-bare-metal platforms. Review the information in the [guidelines for deploying OpenShift Container Platform on non-tested platforms](https://access.redhat.com/articles/4207611) before you attempt to install an OpenShift Container Platform cluster in such an environment.

# Prerequisites

- You reviewed details about the [OpenShift Container Platform installation and update](../../../architecture/architecture-installation.md#architecture-installation) processes.

- You read the documentation on [selecting a cluster installation method and preparing it for users](../../overview/installing-preparing.md#installing-preparing).

- If you use a firewall, you [configured it to allow the sites](../../install_config/configuring-firewall.md#configuring-firewall-module_configuring-firewall) that your cluster requires access to.

  > [!NOTE]
  > Be sure to also review this site list if you are configuring a proxy.

# Internet access for OpenShift Container Platform

In OpenShift Container Platform 4.17, you require access to the internet to install your cluster.

You must have internet access to perform the following actions:

- Access Red Hat Hybrid Cloud Console to download the installation program and perform subscription management. If the cluster has internet access and you do not disable Telemetry, that service automatically entitles your cluster.

- Access Quay.io to obtain the packages that are required to install your cluster.

- Obtain the packages that are required to perform cluster updates.

> [!IMPORTANT]
> If your cluster cannot have direct internet access, you can perform a restricted network installation on some types of infrastructure that you provision. During that process, you download the required content and use it to populate a mirror registry with the installation packages. With some installation types, the environment that you install your cluster in will not require internet access. Before you update the cluster, you update the content of the mirror registry.

<div>

<div class="title">

Additional resources

</div>

- [Installing a user-provisioned bare metal cluster on a restricted network](installing-restricted-networks-bare-metal.md#installing-restricted-networks-bare-metal)

</div>

## Required machines for cluster installation

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

> [!NOTE]
> As an exception, you can run zero compute machines in a bare metal cluster that consists of three control plane machines only. This provides smaller, more resource efficient clusters for cluster administrators and developers to use for testing, development, and production. Running one compute machine is not supported.

> [!IMPORTANT]
> To maintain high availability of your cluster, use separate physical hosts for these cluster machines.

The bootstrap and control plane machines must use Red Hat Enterprise Linux CoreOS (RHCOS) as the operating system. However, the compute machines can choose between Red Hat Enterprise Linux CoreOS (RHCOS), Red Hat Enterprise Linux (RHEL) 8.6 and later.

Note that RHCOS is based on Red Hat Enterprise Linux (RHEL) 9.2 and inherits all of its hardware certifications and requirements. See [Red Hat Enterprise Linux technology capabilities and limits](https://access.redhat.com/articles/rhel-limits).

## Minimum resource requirements for cluster installation

Each created cluster must meet minimum requirements so that the cluster runs as expected.

| Machine | Operating System | CPU <sup>\[1\]</sup> | RAM | Storage | Input/Output Per Second (IOPS)<sup>\[2\]</sup> |
|----|----|----|----|----|----|
| Bootstrap | RHCOS | 4 | 16 GB | 100 GB | 300 |
| Control plane | RHCOS | 4 | 16 GB | 100 GB | 300 |
| Compute | RHCOS | 2 | 8 GB | 100 GB | 300 |

Minimum resource requirements

1.  One CPU is equivalent to one physical core when simultaneous multithreading (SMT), or Hyper-Threading, is not enabled. When enabled, use the following formula to calculate the corresponding ratio: (threads per core × cores) × sockets = CPUs.

2.  OpenShift Container Platform and Kubernetes are sensitive to disk performance, and faster storage is recommended, particularly for etcd on the control plane nodes which require a 10 ms p99 fsync duration. Note that on many cloud platforms, storage size and IOPS scale together, so you might need to over-allocate storage volume to obtain sufficient performance.

3.  As with all user-provisioned installations, if you choose to use RHEL compute machines in your cluster, you take responsibility for all operating system life cycle management and maintenance, including performing system updates, applying patches, and completing all other required tasks. Use of RHEL 7 compute machines is deprecated and has been removed in OpenShift Container Platform 4.10 and later.

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

- [Optimizing storage](../../../scalability_and_performance/optimization/optimizing-storage.md#optimizing-storage)

</div>

## Certificate signing requests management

On user-provisioned infrastructure, you must provide a mechanism for approving cluster certificate signing requests (CSRs) after installation when your cluster has limited access to automatic machine management.

The `kube-controller-manager` only approves the kubelet client CSRs. The `machine-approver` cannot guarantee the validity of a serving certificate that is requested by using kubelet credentials because it cannot confirm that the correct machine issued the request. You must determine and implement a method of verifying the validity of the kubelet serving certificate requests and approving them.

<div>

<div class="title">

Additional resources

</div>

- [Configuring a three-node cluster](installing-bare-metal.md#installation-three-node-cluster_installing-bare-metal)

- [Approving the certificate signing requests for your machines](installing-bare-metal.md#installation-approve-csrs_installing-bare-metal)

- [Installing RHCOS and starting the OpenShift Container Platform bootstrap process](../../installing_vsphere/upi/installing-vsphere.md#installation-vsphere-machines_installing-vsphere)

</div>

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

<div>

<div class="title">

Additional resources

</div>

- [Validating DNS resolution for user-provisioned infrastructure](installing-bare-metal.md#installation-user-provisioned-validating-dns_installing-bare-metal)

</div>

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

### Example load balancer configuration for user-provisioned clusters

Reference the example API and application Ingress load balancer configuration so that you can understand how to meet the load balancing requirements for user-provisioned clusters.

The sample is an `/etc/haproxy/haproxy.cfg` configuration for an HAProxy load balancer. The example is not meant to provide advice for choosing one load balancing solution over another.

> [!TIP]
> If you are using HAProxy as a load balancer, you can check that the `haproxy` process is listening on ports `6443`, `22623`, `443`, and `80` by running `netstat -nltupe` on the HAProxy node.

In the example, the same load balancer is used for the Kubernetes API and application ingress traffic. In production scenarios, you can deploy the API and application ingress load balancers separately so that you can scale the load balancer infrastructure for each in isolation.

> [!NOTE]
> If you are using HAProxy as a load balancer and SELinux is set to `enforcing`, you must ensure that the HAProxy service can bind to the configured TCP port by running `setsebool -P haproxy_connect_any=1`.

<div class="formalpara">

<div class="title">

Sample API and application Ingress load balancer configuration

</div>

``` text
global
  log         127.0.0.1 local2
  pidfile     /var/run/haproxy.pid
  maxconn     4000
  daemon
defaults
  mode                    http
  log                     global
  option                  dontlognull
  option http-server-close
  option                  redispatch
  retries                 3
  timeout http-request    10s
  timeout queue           1m
  timeout connect         10s
  timeout client          1m
  timeout server          1m
  timeout http-keep-alive 10s
  timeout check           10s
  maxconn                 3000
listen api-server-6443
  bind *:6443
  mode tcp
  option  httpchk GET /readyz HTTP/1.0
  option  log-health-checks
  balance roundrobin
  server bootstrap bootstrap.ocp4.example.com:6443 verify none check check-ssl inter 10s fall 2 rise 3 backup
  server master0 master0.ocp4.example.com:6443 weight 1 verify none check check-ssl inter 10s fall 2 rise 3
  server master1 master1.ocp4.example.com:6443 weight 1 verify none check check-ssl inter 10s fall 2 rise 3
  server master2 master2.ocp4.example.com:6443 weight 1 verify none check check-ssl inter 10s fall 2 rise 3
listen machine-config-server-22623
  bind *:22623
  mode tcp
  server bootstrap bootstrap.ocp4.example.com:22623 check inter 1s backup
  server master0 master0.ocp4.example.com:22623 check inter 1s
  server master1 master1.ocp4.example.com:22623 check inter 1s
  server master2 master2.ocp4.example.com:22623 check inter 1s
listen ingress-router-443
  bind *:443
  mode tcp
  balance source
  server compute0 compute0.ocp4.example.com:443 check inter 1s
  server compute1 compute1.ocp4.example.com:443 check inter 1s
listen ingress-router-80
  bind *:80
  mode tcp
  balance source
  server compute0 compute0.ocp4.example.com:80 check inter 1s
  server compute1 compute1.ocp4.example.com:80 check inter 1s
```

</div>

where:

`listen api-server-6443`
Port `6443` handles the Kubernetes API traffic and points to the control plane machines.

`server bootstrap bootstrap.ocp4.example.com`
The bootstrap entries must be in place before the OpenShift Container Platform cluster installation and they must be removed after the bootstrap process is complete.

`listen machine-config-server`
Port `22623` handles the machine config server traffic and points to the control plane machines.

`listen ingress-router-443`
Port `443` handles the HTTPS traffic and points to the machines that run the Ingress Controller pods. The Ingress Controller pods run on the compute machines by default.

`listen ingress-router-80`
Port `80` handles the HTTP traffic and points to the machines that run the Ingress Controller pods. The Ingress Controller pods run on the compute machines by default.

> [!NOTE]
> If you are deploying a three-node cluster with zero compute nodes, the Ingress Controller pods run on the control plane nodes. In three-node cluster deployments, you must configure your application Ingress load balancer to route HTTP and HTTPS traffic to the control plane nodes.

# Creating a manifest object that includes a customized br-ex bridge

By default, OpenShift Container Platform automatically configures the Open vSwitch (OVS) `br-ex` bridge on bare-metal nodes. For advanced networking requirements, you can override this default behavior on bare-metal platforms. To do this, create a `MachineConfig` object that includes an NMState configuration file.

Consider using the customized `br-ex` bridge configuration for any of the following tasks:

- You need to modify the `br-ex` bridge after you installed the cluster.

- You need to modify the maximum transmission unit (MTU) for your cluster.

- You need to update DNS values.

- You need to modify attributes for a different bond interface. Examples include MIImon (Media Independent Interface Monitor), bonding mode or Quality of Service (QoS).

- You need to enable Link Layer Discovery Protocol (LLDP) to discover and troubleshoot switch connectivity.

> [!NOTE]
> Use the default OVS `br-ex` bridge for standard environments.
>
> Use the default OVS `br-ex` bridge mechanism for single network interface controller (NIC) environments with default network settings.

After you install Red Hat Enterprise Linux CoreOS (RHCOS) and the system reboots, the Machine Config Operator injects Ignition configuration files into each node. This operation ensures that each node receives the `br-ex` bridge network configuration. To prevent configuration conflicts, the default OVS `br-ex` bridge mechanism is disabled.

> [!WARNING]
> The following list of interface names are reserved and you cannot use the names with NMstate configurations:
>
> - `br-ext`
>
> - `br-int`
>
> - `br-local`
>
> - `br-nexthop`
>
> - `br0`
>
> - `ext-vxlan`
>
> - `ext`
>
> - `genev_sys_*`
>
> - `int`
>
> - `k8s-*`
>
> - `ovn-k8s-*`
>
> - `patch-br-*`
>
> - `tun0`
>
> - `vxlan_sys_*`

<div>

<div class="title">

Prerequisites

</div>

- Optional: You have installed the [`nmstatectl`](https://nmstate.io/user/quick_guide.html) CLI tool to validate your NMState configuration.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create an NMState configuration file and define a customized `br-ex` bridge network configuration in the file:

    <div class="formalpara">

    <div class="title">

    Example of an NMState configuration for a customized `br-ex` bridge network

    </div>

    ``` yaml
    interfaces:
    - name: enp2s0
      type: ethernet
      state: up
      mtu: 9000
      ipv4:
        enabled: false
      ipv6:
        enabled: false
    - name: br-ex
      type: ovs-bridge
      state: up
      ipv4:
        enabled: false
        dhcp: false
      ipv6:
        enabled: false
        dhcp: false
      bridge:
        options:
          mcast-snooping-enable: true
        port:
        - name: enp2s0
        - name: br-ex
    - name: br-ex
      type: ovs-interface
      state: up
      copy-mac-from: enp2s0
      mtu: 9000
      ipv4:
        enabled: true
        dhcp: true
        auto-route-metric: 48
      ipv6:
        enabled: true
        dhcp: true
        auto-route-metric: 48
    # ...
    ```

    </div>

    where:

    `interfaces.name`
    Specifies the name of the interface.

    `interfaces.type`
    Specifies the type of ethernet.

    `interfaces.state`
    Specifies the requested state for the interface after creation.

    `mtu`
    To ensure network stability and performance, you must explicitly declare the MTU in the manifest for every interface. Do not rely on automatic MTU configuration. The MTU configured on a bridge port or VLAN-tagged interface must not exceed the maximum frame size supported by the attached physical medium. A mismatch causes packet fragmentation or connectivity loss.

    `ipv4.enabled`
    Disables IPv4 and IPv6 in this example.

    `port.name`
    Specifies the node NIC to which the bridge attaches.

    `auto-route-metric`
    Sets the parameter to `48` to ensure the `br-ex` default route always has the highest precedence (lowest metric). This configuration prevents routing conflicts with any other interfaces that are automatically configured by the `NetworkManager` service.

2.  Use the `cat` command to base64-encode the contents of the NMState configuration:

    ``` terminal
    $ cat <nmstate_configuration>.yml | base64
    ```

    where:

    `<nmstate_configuration>`
    Replace `<nmstate_configuration>` with the name of your NMState resource YAML file.

3.  Create a `MachineConfig` manifest file and define a customized `br-ex` bridge network configuration analogous to the following example. The installation program automatically applies the updates from the `MachineConfig` object to your cluster.

    ``` yaml
    apiVersion: machineconfiguration.openshift.io/v1
    kind: MachineConfig
    metadata:
      labels:
        machineconfiguration.openshift.io/role: worker
      name: 10-br-ex-worker
    spec:
      config:
        ignition:
          version: 3.2.0
        storage:
          files:
          - contents:
              source: data:text/plain;charset=utf-8;base64,<base64_encoded_nmstate_configuration>
            mode: 0644
            overwrite: true
            path: /etc/nmstate/openshift/worker-0.yml
          - contents:
              source: data:text/plain;charset=utf-8;base64,<base64_encoded_nmstate_configuration>
            mode: 0644
            overwrite: true
            path: /etc/nmstate/openshift/worker-1.yml
    # ...
    ```

    where:

    `metadata.name`
    Specifies the name of the policy.

    `contents.source`
    Writes the encoded base64 information to the specified path.

    `path`
    For each node in your cluster, specify the hostname path to your node and the base-64 encoded Ignition configuration file data for the machine type. The `worker` role is the default role for nodes in your cluster. You must use the `.yml` extension for configuration files. For example, use `$(hostname -s).yml` when specifying the short hostname path for each node or all nodes in the `MachineConfig` manifest file.

    You can apply a single global configuration to all nodes in your cluster by using the `/etc/nmstate/openshift/cluster.yml` configuration file. In this case, you do not need to specify the short hostname path for each node, such as `/etc/nmstate/openshift/<node_hostname>.yml`. For example:

    <div class="formalpara">

    <div class="title">

    Example /etc/nmstate/openshift/cluster.yml configuration file

    </div>

    ``` yaml
    # ...
          - contents:
              source: data:text/plain;charset=utf-8;base64,<base64_encoded_nmstate_configuration>
            mode: 0644
            overwrite: true
            path: /etc/nmstate/openshift/cluster.yml
    # ...
    ```

    </div>

</div>

<div>

<div class="title">

Next steps

</div>

- Scaling compute nodes to apply the manifest object that includes a customized `br-ex` bridge to each compute node that exists in your cluster. For more information, see "Expanding the cluster" in the *Additional resources* section.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Converting to a dual-stack cluster network](../../../networking/ovn_kubernetes_network_provider/converting-to-dual-stack.md#nw-dual-stack-convert_converting-to-dual-stack)

- [Expanding the cluster](../bare-metal-expanding-the-cluster.md#bare-metal-expanding-the-cluster)

</div>

## Scaling each machine set to compute nodes

To scale each machine set to compute nodes, you must apply a customized `br-ex` bridge configuration to all compute nodes in your OpenShift Container Platform cluster. You must then edit your `MachineConfig` custom resource (CR) and modify its roles.

Additionally, you must create a `BareMetalHost` CR that defines information for your bare-metal machine, such as hostname, credentials, and your other required parameters. After you configure these resources, you must scale machine sets, so that the machine sets can apply the resource configuration to each compute node and reboot the nodes.

<div>

<div class="title">

Prerequisites

</div>

- You created a `MachineConfig` manifest object that includes a customized `br-ex` bridge configuration.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Edit the `MachineConfig` CR by entering the following command:

    ``` terminal
    $ oc edit mc <machineconfig_custom_resource_name>
    ```

2.  Add each compute node configuration to the CR, so that the CR can manage roles for each defined compute node in your cluster.

3.  Create a `Secret` object named `extraworker-secret` that has a minimal static IP configuration.

4.  Apply the `extraworker-secret` secret to each node in your cluster by entering the following command. This step provides each compute node access to the Ignition config file.

    ``` terminal
    $ oc apply -f ./extraworker-secret.yaml
    ```

5.  Create a `BareMetalHost` resource and specify the network secret in the `preprovisioningNetworkDataName` parameter:

    <div class="formalpara">

    <div class="title">

    Example `BareMetalHost` resource with an attached network secret

    </div>

    ``` yaml
    apiVersion: metal3.io/v1alpha1
    kind: BareMetalHost
    spec:
    # ...
      preprovisioningNetworkDataName: ostest-extraworker-0-network-config-secret
    # ...
    ```

    </div>

6.  To manage the `BareMetalHost` object within the `openshift-machine-api` namespace of your cluster, change to the namespace by entering the following command:

    ``` terminal
    $ oc project openshift-machine-api
    ```

7.  Get the machine sets:

    ``` terminal
    $ oc get machinesets
    ```

8.  Scale each machine set by entering the following command. You must run this command for each machine set.

    ``` terminal
    $ oc scale machineset <machineset_name> --replicas=<n>
    ```

    - \<n\>: Where `<machineset_name>` is the name of the machine set and `<n>` is the number of compute nodes.

</div>

# Enabling OVS balance-slb mode for your cluster

You can enable the Open vSwitch (OVS) `balance-slb` mode so that two or more physical interfaces can share their network traffic. A `balance-slb` mode interface can give source load balancing (SLB) capabilities to a cluster that runs virtualization workloads, without requiring load balancing negotiation with the network switch.

Currently, source load balancing runs on a bond interface, where the interface connects to an auxiliary bridge, such as `br-phy`. Source load balancing balances only across different Media Access Control (MAC) address and virtual local area network (VLAN) combinations. Note that all OVN-Kubernetes pod traffic uses the same MAC address and VLAN, so this traffic cannot be load balanced across many physical interfaces.

The following diagram shows `balance-slb` mode on a simple cluster infrastructure layout. Virtual machines (VMs) connect to specific localnet `NetworkAttachmentDefinition` (NAD) custom resource definition (CRDs), `NAD 0` or `NAD 1`. Each NAD provides VMs with access to the underlying physical network, supporting VLAN-tagged or untagged traffic. A `br-ex` OVS bridge receives traffic from VMs and passes the traffic to the next OVS bridge, `br-phy`. The `br-phy` bridge functions as the controller for the SLB bond. The SLB bond balances traffic from different VM ports over the physical interface links, such as `eno0` and `eno1`. Additionally, ingress traffic from either physical interface can pass through the set of OVS bridges to reach the VMs.

<figure>
<img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAABfAAAARGCAYAAAB33pGrAAAACXBIWXMAAA7DAAAOwwHHb6hkAAAAGXRFWHRTb2Z0d2FyZQB3d3cuaW5rc2NhcGUub3Jnm+48GgAAIABJREFUeJzs3Xdgjff///+HSBArUmKEWrVH0BYtb3vzLtVl1Cq1o1U+Rb1LVa2+3zWq2tqjRqiixIi9QhISIUYSCRI7YmWSeX5//OR8HeckkqA51fvtr57XeV3X9cx1hp7H9bper1wGg8EgAAAAAAAAAABgVWxyugAAAAAAAAAAAGCOAB8AAAAAAAAAACtEgA8AAAAAAAAAgBUiwAcAAAAAAAAAwAoR4AMAAAAAAAAAYIUI8AEAAAAAAAAAsEIE+AAAAAAAAAAAWCECfAAAAAAAAAAArBABPgAAAAAAAAAAVogAHwAAAAAAAAAAK0SADwAAAAAAAACAFSLABwAAAAAAAADAChHgAwAAAAAAAABghQjwAQAAAAAAAACwQgT4AAAAAAAAAABYIQJ8AAAAAAAAAACsEAE+AAAAAAAAAABWiAAfAAAAAAAAAAArRIAPAAAAAAAAAIAVIsAHAAAAAAAAAMAKEeADAAAAAAAAAGCFCPABAAAAAAAAALBCBPgAAAAAAAAAAFghAnwAAAAAAAAAAKwQAT4AAAAAAAAAAFaIAB8AAAAAAAAAACtEgA8AAAAAAAAAgBUiwAcAAAAAAAAAwAoR4AMAAAAAAAAAYIUI8AEAAAAAAAAAsEIE+AAAAAAAAAAAWCECfAAAAAAAAAAArBABPgAAAAAAAAAAVogAHwAAAAAAAAAAK0SADwAAAAAAAACAFSLABwAAAAAAAADAChHgAwAAAAAAAABghQjwAQAAAAAAAACwQgT4AAAAAAAAAABYIQJ8AAAAAAAAAACsEAE+AAAAAAAAAABWiAAfAAAAAAAAAAArRIAPAAAAAAAAAIAVIsAHAAAAAAAAAMAKEeADAAAAAAAAAGCFCPABAAAAAAAAALBCBPgAAAAAAAAAAFghAnwAAAAAAAAAAKwQAT4AAAAAAAAAAFaIAB8AAAAAAAAAACtEgA8AAAAAAAAAgBUiwAcAAAAAAAAAwAoR4AMAAAAAAAAAYIUI8AEAAAAAAAAAsEIE+AAAAAAAAAAAWCECfAAAAAAAAAAArBABPgAAAAAAAAAAVogAHwAAAAAAAAAAK0SADwAAAAAAAACAFSLABwAAAAAAAADAChHgAwAAAAAAAABghQjwka7U1FQZDIacLiNdKSkpOV0CnrPMvKa87i8e5xgAAAAAAMA62OZ0ATklPj5eYWFhunXrlipUqKCSJUsqb968OV3WU927d0/Xrl3T7du35eDgIGdnZxUrVky5c+d+pv1GRkZq48aNunr1qq5fv64bN27oypUrWrx4sRo2bPjc6s+uwMBA7d69Wzdu3DDWGB8fLy8vr5wuDdm0efNmnTt3Tjdu3ND169d1/fp1NWjQQHPmzDH2CQsLk7u7u7FP2nvf29v7b/F5/Tvw8/PToUOHjOf35s2bsrW11a5du3K6NAAAAAAAgH+8f1SA7+Pjo82bN8vX11eXLl1SVFSUJCl37txydHRUtWrV9MYbb6hv374qU6aMxX3Mnz9fv//+u1l72bJltXz58kzXMmDAAF26dMmkLSUlRd9//73eeustk/Zjx45p3bp1OnnypC5duqTY2Fjjc3nz5lWxYsVUrVo1Va9eXR9++KGqV6+e6TrS7N+/XxMmTDBrt5YR+H/88Yd++uknk7ZXX301x+rBs/vpp58UEBBg0vb222+bPN68ebOmTp1q0ubo6Gg178uXwerVq7Vq1SqTNhcXlxyrBwAAAAAAAP/PPyLAv3Dhgv773/9q586dio+PN3s+JSVFt2/flqenpzw9PeXm5qauXbvqq6++Uv78+U36du7cWXPmzNHdu3dN2i9evKigoCBVq1btqfVcvHhRBw4cUExMjEm7i4uLyWj3xMREjRs3Ths3brRYtyQlJCTo2rVrunbtmvbu3atly5apcePGGjRokJo2bfrUWgAAAAAAAAAA1umlnwN/z5496tGjhzZt2pRuCP6kW7duacGCBerWrZsuXrxo8pyzs7MaNWpktk18fLzFkfmWuLm5mYX3ktS8eXPlypVLenRR4ZNPPtGqVasyXbckxcXFadeuXfrkk0/01VdfZXo7AAAAAAAAAIB1eakDfA8PDw0fPlxhYWHZ2t7Hx0d9+/bVlStXTNrbtm1rsf/Ro0cztV9PT0+zNgcHB/Xt29f4eM6cOdq9e3eWa04TExOjpKSkbG8PAAAAAAAAAMhZL22AHxgYqK+//lr37t1Lt0+xYsVUrlw5FS5cON0+wcHBcnV1VWJiorHtww8/VJUqVcz6nj59+qkh/tGjR83m/Zakxo0bG+d0NxgM2rJli1kfGxsb1alTRz179tSnn36qnj17qmnTpipatKhZ37p16+q7777LsBYAAAAAAAAAgPV6aefAnzFjhi5fvmzWnitXLjVt2lQ9e/bUO++8I1tbW0VHR2vNmjVau3atzp07Z7aNl5eXZs2apXHjxkmPFr1t1qyZzp8/b9IvKSlJW7ZssTjFTprNmzdbHBnfrl07438fP35cwcHBZn169+6t//73v8ZpdtJERUXp119/1ZYtWxQaGioHBwdNnDhR9vb26daRXfHx8bK1tVWePHmytX1KSorCw8N1+fJlxcfHq1SpUqpevbry5cv33GtNc/36dV28eFFRUVEqWrSoqlWrpiJFijzzfhMTExUSEqJr166pevXq2VpUNzk5WWFhYbp48aKcnJxUsWJFOTg4ZGkfCQkJCgkJ0fXr11W6dGlVrlw5269PdsXGxurMmTO6e/euihQpokqVKql48eJ/6fHt7e2VO3fuF36sO3fu6MyZM3JyclLlypVlZ2dnsd/t27d15swZFShQQHXr1k23X0Zu3rypkJAQJScnq2rVqnJ2dn6m2hMTE5WcnGy2tkd2JSUl6cKFC7p8+bJKlCihKlWqvJDvHQAAAAAAgH+qlzLA3717t/bu3WvWnitXLvXp08csBC9cuLCGDBmi7t27a8CAATp8+LDZtn/88YcGDRqkV155RZLUvXt3rVq1Sg8ePDDpd+TIEaWmpsrGxvzmhpSUFB05csSsvUqVKvroo4+Mj0NCQpSammpWe69evczCez2afmfcuHEaOnSovv76azk7O+tf//pXBmcoawICArRo0SL5+fnp9u3byp07t0qXLq233npLn3/+uZycnDLc3svLSzt37lRAQIAuXbqkmzdvKiUlxfi8k5OTatSooU6dOqlfv37PXG9oaKg2bdokf39/XbhwQVevXjW5aFKoUCFVrVpVzZo108iRI5U3b16zfWzcuFETJ040aUtNTdXKlStVqVIlTZkyRfv27TNOr5QvXz7VrVtXn376qTp37vzUGr28vLRixQr5+fnp8uXLMhgM0qP3Ys2aNdWoUSONGDEiw6DVw8NDbm5u8vf3182bN43tpUqV0htvvKE+ffqoefPmmTxrWZeSkqKff/5Ze/bsUVBQkO7fv298Ll++fKpQoYJq1aqltm3bqnPnzhbfu8/iwIEDWrVqlU6dOqV79+4pb968KleunJo2baqRI0dm66LQrFmztHTpUpO2PHny6NixYwoICNDMmTPl5eWl2NhY2djYqHz58nr33Xc1ZswY42d+06ZNWrVqlfz8/IzrV7z66qvq1KmTJk6cKFvbjL92b9y4oblz5+rYsWMKDg423v1jZ2enypUrq379+nJ1dVW5cuUy9TcFBgZq8eLFOnHihG7evKnk5GQVL15cDRs21MiRI7N8jvToTqLly5fLz8/PZIoxJycn1a1bV926dcvU5wAAAAAAAAAZeykD/C1btphMeZOmVatWFkewpylSpIh++eUXde3aVaGhoSbPXb58WW5ubho+fLgkqXbt2mrQoIEOHjxo0u/8+fPatm2b3nnnHYt1hYSEmLU3b978qSOHDQaD1q5dq9q1a1u8OKBHQf5PP/2U4X6yat26ddq+fbvZVER37txRQECAdu/erUmTJqlDhw5m2x46dEizZs3S8ePHM5yPPzIyUgcPHtThw4e1f/9+LVy40GKo/jS3b9/W559/Lm9vb4uLBKeJiYmRr6+vfH19tW/fPv3666+qWLGiSZ/k5GTdunXLbNvQ0FB9+eWXOnPmjEn7w4cP5e3trdOnT+vmzZsaNGiQxWOnpKRo3LhxWr9+vcXFiaOjo+Xl5SUvLy9t3bpVY8aMMXsvJSQkaOTIkdqyZYvF83rjxg1t3bpVe/bsUffu3TVjxox03zPZdffuXQ0cONDixS49Oh+BgYEKDAzUhg0btGTJEo0dO1aNGzd+LsefOnWqVq5caXYOIyMj5evrq127dmnmzJmqV69elvabK1cus9e9aNGicnd314QJE0yeS01N1cWLFzV79mxdvnxZv/zyi7777jstWrRIDx8+NNnHlStXNH/+fIWHh2v58uXpfgf99ttvmjlzpm7cuGH2XFJSks6dO6dz585p+/btcnV11dChQzP8e3744QctWbJEd+7cMWmPiopSSEiIDh48qNKlS2fq3KT9zePHj9fatWstvn8jIyO1e/duHThwQNu2bdPcuXOz9VkGAAAAAADA/++lmwM/NTVVfn5+Zu158uSRq6vrU0cBlyhRQl27drX43JP7bdmypVkfg8GgXbt2Wdx+165dxpHWafLnz6+ePXuatLm4uFicbmPp0qVq3bq1Pv/8c82ePVubN2/W3bt3M/x7ntX69eszXEfg0qVLGj16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elSDBg3S/Pnz1aRJk+dSQ3rKlClj1vbw4cPnHuA/T5Ze18en6XqSpXn1H79jyNLdJOnN2Z9ZWb2D6UnP670HAAAAAADwT/PSBfi5cuXSm2++aRbgJyUlaf78+WrdunWG836HhoZq8+bNFp97cnHQNKVLl1ajRo20bds2k/bjx49ry5Yt8vf3N9umRYsWT/1bvL29de/evQwvOhQpUkSDBg1SsWLFNGTIELPnX1RwFhAQYHGaocdH3y9evFgLFy60uKjwi3DixAl99913un///l9yvKywFKBmdVSypX2UL19eBQsWzNT2j/ezt7dX/fr1Mz0H/pPHePPNN7Vp0yb99NNP8vHxUWBgoJKSktLdPjIyUrNnz37hAb6lO20KFixocTS7tbD0uma0CLWl5x7fh6U7Qm7evPncayxTpozFiwmWZLYfAAAAAAAATL10Ab4kffTRR9q4caPZyFYvLy8NGTJEv/76q8WpLcLDwzVixAhdvXrV7LnKlSurR48e6R6zXbt2ZgF+TEyMvv/+e7PR/CVLltQnn3yS4d8QHx+vr7/+WiEhIerSpYu++eabDEdsPzk3fxpLi/E+D7///rtZMO/o6KjXX3/d+Hjz5s1mferVq6fWrVvL0dFRiYmJioiI0M6dO82mBMmO1atXm4X35cuX17///W+VKlVKqampunPnjjw9PeXr6/vMx8sKZ2dnnT171qTN29tbUVFRFl87X19fvfnmmyZtZcuWNZtLvGrVqlq5cmWW6ylWrJi2bNmS5e0eV7JkSU2dOlWSdOrUKfn4+BindfL399ft27dN+gcEBKT79z4PBoNBu3fvNmsvXbr0M49Af5EsLTR99uxZBQUFqVq1aibt169ftzh1UenSpS3+d5qAgAB5eHioffv22arx1VdfNWsrVaqU2XceAAAAAAAAnq/srepo5Ro2bKh27dpZfM7d3V0dO3bUvHnzFBYWppiYGJ08eVJTpkzRe++9l+4UKz179jRboPJxH3zwgcU5pkNCQszamjRp8tRAccKECQoICNCDBw+0du1atW7dWhMnTlR4eLhZ3ytXruinn34ya7exsUl32p/MWr58uUkonpKSounTp2vTpk1mfevUqWMMZw0Gg9k6Avnz59fixYv15Zdf6tNPP9WwYcP07bffWlwUNTssrVswZMgQTZw4UQMHDtTgwYM1fvx4k4sMf5U3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2bM5Xcozu379utasWaOkpKScLgXA31BCQoI8PT2VkpKS06U8F9euXdOZM2dyugwAAAAAAP5yBPgvsZiYGI0fP14zZszIVH8fHx998803cnNzkyTNmjVL7733no4ePfqCK30+li9friFDhsjT0zOnS3lm48eP13fffafY2Nin9k1JSdHw4cPVu3dv3bp16y+pLyOhoaGaPn26Fi1alNOlAJKkHTt2aPLkydq5c2em+u/cuVOTJ0/W/v37JUnff/+9Bg4cqLCwsBdc6fMzYMAADR48WPHx8TldyjM7ePCgWrZsqZUrV2aqf3h4uAYNGpTpf/teNIPBoO3bt+s///mPBg0apMGDB2vKlCk6depUTpcGAJkSGBgoLy8vPXz4MFP9AwIC5O3trdTUVCUlJWnRokU6fvz4C6/zeRk7dqy6du2a02U8s+TkZPXr10+DBw/OVP+UlBQtX75cR44ceeG1ZdbNmze1bt06LVy4UGvWrLGK3zr457l586a8vLx09erVTPW/ffu2Sf9jx45p2bJlf6vBeePHj1eXLl1yuoznYseOHfroo4+0bNmyTPW/d++eFixYoAsXLrzw2p7F1atX5eXlpdu3b+d0KfiLEOC/xAoVKqTQ0FAtWbJEPj4+T+2/du1arVixQvny5ZMk7d+/XydOnNChQ4eydNzk5GQdPXpUycnJ2a49O2xtbf/S471IWflb7ty5oz179ujw4cPy9vZ+oXVlJDAwUCNGjFDXrl21YMECHTt2LMdqAR6XP39+rVixQkuXLs1U/yVLlmjNmjUqWrSokpOT9ccff2j37t3avn17lo9948YNxcXFZaPqZ5MrVy7lypXrLz9udhkMhnSfS05OVkJCQqb/nh07dmjXrl1av369EhMTn2OVWXfmzBl9/PHHcnV1lbu7uy5fvqygoCAtX75cPXv21I8//pij9QFAZixZskQ9evTIVPgRERGhPn366JtvvpEkLVq0SFOnTtX48eP/gkqfj8DAQN25cyeny3hmSUlJ8vf3z/TF/DVr1mjSpEkaM2bMX/477knBwcEaNmyYWrdurbFjx2ratGkaP3682rRpo6+//vpvFYTi78/b21s9e/bUf/7zn0z1nz59unr06KG9e/fKYDBo7Nix+vbbb7V48eIXXuvzEhgYqIiIiJwu47kICwvTsWPHMv274Pvvv9f06dM1adKkF15b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/UzuVnJ1ddWxY8e0Z88elShRQpL0xRdf6NChQ5o7d64WLlyo48ePy97eXkeOHNHQoUN1+vRpYwA/btw44xQxM2fOVLt27TR9+nStX79eEyZMMLlYIEkrVqzQ7Nmz9emnn2rkyJHSo0XJly5dqkOHDikkJETR0dHKnTu3SpQooTZt2mjChAnZut39l19+0aJFi9S/f39duHBB+/bt04MHD1S0aFG9++67Gj9+vLZt26b58+cbv0MqVKggV1dXvfvuuyb72rRpkzw8POTv7687d+4oJSVFDg4Oev311zV+/HhVrlzZ7Pjr16/X6tWrdfbsWSUlJSlv3ryqWbOm3n//fbM7HwwGg2bOnKk//vhDN27cUN68eVWlShWNGDFCbdu2Nfa7efOm2rRpowYNGmjJkiXSo/C+efPmqlGjhtq1a6dly5bp4sWLsrOzU/ny5dW3b1+LdzKFhIRo5syZOnLkiGJiYmRra6tatWppwIABxn/jssvT01PJyckqU6bMM+0HAP4KH3/8sVasWKHDhw8rOTnZ4r857u7uSklJMbmr6Pr16/ruu+9Up04dDRkyRJJ08eJF/fDDD3rjjTfUsGFDLVmyRBEREXr//fdVqFAhubu76969e5IkX19fjRgxQpLUuHFjde/eXcePH9dvv/2mt99+22x6u7Nnz+rXX39V/fr11bdvX2N7VFSU1q5dq+DgYN26dUt58uSRs7Oz3n///QzvKMjI3Llzde7cOU2bNk1ubm46duyYDAaDqlevruHDh6tw4cLy9/fX6tWrdf36dRUoUEAtWrSwOCVfWFiY1q9fr/DwcN25c0eFCxdWhQoV1K9fP5UsWdLi8f/880/t379ft27dUr58+VSlShV1795dFSpUMOsbERGh+fPnKyQkRPb29qpWrZpcXV2VN29eY5+YmBh9+eWXql69uj7//HPp0Vpb//nPf1SrVi116tRJixcvVlhYmAoVKiQXFxcNGjTI4nshKSlJS5YskZ+fn2JiYlS8eHG1a9dOnTp1yta5flza4IW034vAX6FMmTJ6++235eHhoS1btui9994z63P8+HH5+/urcePGJneH/PjjjwoICNC0adOMvyXSfuNPnDhRW7Zskaenp1JTU7V06VL9+OOPunLlinFw0NKlS7V+/XoZDAYNGzZMderU0W+//aajR4+qT58+atSokUkd27Ztk7u7u9555x2Tz9yFCxe0YcMGXbhwQbdu3VKBAgXk7OysDz/8MFu5iiStWrVKnp6e6tevn4KCgrR3717FxsaqQoUK+uSTT1S7dm2FhYVp0aJFCg4OVr58+VSjRg198cUXsre3N9nX/fv3tW7dOgUEBOj27dsyGAwqUaKEWrZsme7C4hcuXNCKFSsUHByshIQEOTk5qX79+ma/59J4eHho06ZNunXrlpycnPT6669r4MCBJtnKwYMH5ebmplatWhkHuB45ckQrV65Us2bNVK5cOa1Zs0bXrl3TK6+8opo1a2rYsGHGtSQfFxMTo4ULF+rkyZOKjo5WsWLF1Lx5c3388cdZnvpm/fr1WrJkiTp06KAxY8Zken03vDwI8P8B2rZtqxo1asjb21tXrlzRq6++avL8hg0blJCQoJYtW5q0586dW3FxcSajLW1tbRUXF6eff/5ZRYoU0ejRoxUbGysbGxt17txZ0dHROnDggIKCgvTxxx8rT548MhgMxi8zGxubdEez29jYmI1eP3funA4dOqSmTZuqcuXKypcvn86ePautW7dqzJgx2rx5swoXLpyl85GamqrY2FgdOHBA5cqV08iRI5WQkKBt27bp999/1927d3XmzBm1bdvWeFFi48aNmj59ulxcXFStWjXjvg4ePKjbt2/rww8/VOnSpfXw4UPt27dPGzdulI2NjX744Qdj36SkJA0cOFCenp6qWbOmunTpIjs7O509e1YeHh46f/683N3djf/QpKamaurUqXrrrbfUuXNnRUREaMuWLVq2bJkKFiyo0aNHm5w7SyNxY2JiNG3aNLVu3Vrdu3dXeHi4Nm/erNmzZ6tYsWImF3SCg4M1ePBg3blzRx07dlTFihV148YNbd26VZ9//rnmzJmjZs2aZelcA9akc+fOxouZlgL8ffv2yd7e3uROJD36fD148MDkuzDt+3HOnDlycHDQF198oZiYGNnb26tTp0568803dezYMfn4+Kh9+/ZydnaWHt2pkrbP2NjYdEezp32vPn68P//8U05OTurdu7eKFy+uqKgo7dq1SytWrJCtra0mTJiQ5XOSVseGDRvk4uKisWPHKioqSlu2bNGSJUt09epVnTx5Uh07dlS3bt0UFhamjRs3asKECSpbtqxef/11476OHDmi8+fPq3379ipbtqxy5colPz8/7dy5U7dv39amTZtMfuT/+OOPmjdvngoVKqRu3bqpaNGiioyM1MGDBzVhwgQlJCSof//+xv4+Pj4qWLCgevXqJXt7e50+fVrbtm3TuHHj5OzsbJxf2WAwKD4+3uR/xA0GgxISEnTlyhUtX75cnTp1kpOTk4KDg7VlyxZNmTJFjo6OJj9yzp8/r0GDBikiIkIdOnRQ5cqVFRkZqe3bt2vMmDGKi4vL9u218fHxWrlypYoXL252YRgArNErr7yixo0ba/Pmzdq0aZPZv5UPHz7U4cOHValSJZOg5e7du9qxY4dJUBMREaHt27crMTFRK1askCQ5ODjoypUrKlmypK5cuWK8W+7+/fvGeX5v374tSbp8+bLc3d3l5ORkVue1a9e0detWOTo6Gtvi4+P1zjvv6OrVq6pQoYJKlixp/Pdm+/btmjlzplq0aJHlcxIUFKSdO3fq4cOHunDhgsqWLavw8HAdOnRIJ06cUN++fTVp0iQ5OzsrX7588vb21t69e3X79m199tlnxv0cOnRIw4YNU3JysipWrChHR0eFhoZq586d2rdvn1asWKFSpUoZ+yckJGjkyJHauXOn7O3tVbZsWcXFxenAgQP6448/NHLkSPXu3dvYPzY2Vr169ZKtra0cHR11+vRp7d69W0eOHNHy5cuNv6Xi4+PNptCJiYmRh4eH7t27p3Xr1snBwUGFChWSn5+fPDw85OXlpaVLlxqnCtGjC+murq7y9fXVq6++qmLFiunw4cPatm2bDh8+rOnTp2d77Ztbt25p9+7dql69ujp27JitfQDZ1b59e3l4eGj37t0WA/w///xTiYmJZlMjhoSEaO/evYqOjjYG+KGhodqzZ4/s7Ox05MgR1ahRQ/Hx8UpOTjbeSZ82GOjhw4fKlSuXDAaD8bvx0qVL8vDwUKtWrczquHLlijw8PFS3bl1j2+XLl/XBBx/o4cOHqlatmpycnBQVFaVNmzZp165dmjlzpsV9Pc3Fixfl4eGhiIgIRUZGqkaNGoqJidGff/6po0eP6ssvv9SPP/6oIkWKqESJEgoNDZWnp6cCAgK0evVqk/9f79Wrl86dO6eqVavK2dlZSUlJOnz4sLb/f+zdZ3gUZfv+8XPTSCAJBJBI6KGD0pSOEaQ/gnTBR9SHAAoCgiBIR7qA0quoFKmhKSC9twgB6U1A6aIGEhLSIMn+X/zJ/lg2DZKwg/l+joMXmZ2ZvXaBzc45933dGzbo8uXL+vTTT62ee/Xq1Ro9erRCQkJUvHhxeXh46MSJE9q6davWrl2rr776yiq72blzpy5duqSyZcvKw8NDhw8f1pYtW3T27FmrNkcJ71/RokUt227cuGH5LPzjjz9UokQJeXl56dSpU9q+fbuOHTum77//3upa5+LFi+rZs6flNeXOnVtnz57V9u3btXfvXs2cOTPVA7AOHTqkcePGqWzZsho/fny6rh+G5wcBfiZgMpnk5+enmTNnKiAgwCr4jY2N1b59+1SgQAGbUaDJyZMnj+bOnWv1gdu5c2fpYRCcEHyktaXK//73P7Vs2VI5c+a02u7o6Kjly5frxx9/1Pvvv5+qc5nNZqsPOl9fX82bN8/yodm8eXO1aNFC27dv1zGvAK4AACAASURBVLBhw6wCPi8vL02ePFnLli2zWo184sSJypEjh81o+GbNmmn37t2Kjo623LyYNGmS9u3bp/r162vKlClWC72uWLFCrq6uVneJHzx4oE6dOumdd96xbKtbt64++OADbdu2zervMSlRUVGaOHGi1fSql19+WX369NGmTZuswqdx48bp1q1bGjt2rFq1amXZXq9ePfXo0UOTJk3Sa6+9xiIpeG7Vrl1b5cuX16FDh3Tq1CmrBfWOHTumoKAgVa9e/Yn6qebNm1ezZ8+2+n+RMJK7f//+loWdn+YL8aOyZs2qFStWKHfu3FbbW7durebNm2vnzp1PFeAnqFmzpsaPH2/5uX79+nrnnXe0fft2jRs3zuoz4YUXXtD48eO1bNkyqwB/6NChcnNzs7qI79ixozp37qytW7dqy5YtlovtX375RXPmzFH+/Pk1efJklS9f3nLMX3/9pW+++cbmsz1HjhxavHixsmXLZtmWPXt2zZ8/X8uXL0/1Aonz5s1TwYIFLT/7+vpq5MiRWr16tVWAP3bsWN28eVOjR4+2Cqrefvtt+fv7a9q0aWrcuLGyZ8+equdNEB8frz59+ujs2bMaPHiwfH19n+h4ALCXxo0ba+3atdq+fbtNgB8QEKAbN27I398/1YHE4cOH1aJFCw0aNMjqmHbt2mnt2rX65JNPVK9ePavv3k8ja9asev/991WwYEHVr1/fcj0wb948jRo1St99991TBfh6eH3h4uKiLVu2yM3NTWFhYerRo4d2796tP/74Q71797aMuA8MDFSPHj20cOFC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0xpZadW2bVu99NJLWr16tebPn2/1WHh4uKZPn27XAZx4PjEMLJMpX768XnnlFR04cEAODg5q0qRJuj9HuXLltHbtWvXr10+FCxdWcHCw1q1bp2zZssnf3187d+5UUFCQmjdvrqJFiyo0NFQxMTEqW7as1VTIggUL6p133tHChQv15ptvqmzZsoqLi9PJkyef2Qif5HTs2FE7duzQzJkzdejQIeXPn1937tzRyZMn5eXlZbP/G2+8oc8++0yTJ0/WZ599punTp8vZ2VmXL19WfHy8mjRpovj4eLuNJvnkk09069YtrVy5Uq1atZKvr69iY2N15coVRUdHK1u2bKpUqZJdagPS23vvvaeFCxfq0qVLKlasWIb0C6xdu7aWLl2qGTNmaM2aNbp3755GjRqlxo0bq2zZsvr44481e/Zs9e3bV5MnT5ajo6OioqL06quv2ny5/vTTT3XmzBmNHj1aq1atUs6cOfX3338rKipK2bNnt1rUyR5atGihvXv36qefflKDBg1UuHBhRURE6MqVK/L19bXZ39nZWVOmTFHfvn21ceNGbd26VV5eXgoJCVFsbKyqVKliaWNjL++9957u3r2rb7/9Vl27dpW3t7f0cDHhLFmyJPo5/7ipU6cqLCxMZ8+eVaNGjRLdx83NTfv27UuyHygAGI2Tk5P8/Pw0f/583b59W5UqVVKVKlXS9TkqVKggNzc37d69W1OmTJGjo6Py5cunFi1aKEeOHKpbt65++uknvf/++2rcuLFy5MihoKCgRNuq1K1bV9u2bVOPHj3UvHlz+fj46MaNG9q4caPOnDlj1+sKk8mkGjVqaNGiRfr4449Vt25d5ciRQ+fPn9fatWt17949q/0dHBw0aNAgde/eXePGjVNQUJBKlSqliIgIBQYG6ty5c7p3754mTJhgl9fj5uamfv366fPPP1fPnj3VsGFDlShRQqGhoTpx4oQOHTqkfv36qXPnzkmeIyYmRiEhIerRo4f8/PxUrlw55cyZU7dv39ahQ4d04MABlSlTRj179nymrw14VNu2bbVkyRIdOHAgw1pxFilSRJL07bff6uTJk7pz547ee+89ValSRW+++aaWLl2qwMBAtWrVSpUrV5aDg4MCAwMT/U7ZrFkzDR06VP7+/qpXr56yZ8+uP//8Uzt37tS9e/fk6Oho1/WZWrZsqZ9//lljxozR0aNH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v3791KdPH6tzBg8erGXLlkmSYmNjVbduXU2ePFmlSpXSH3/8oXHjxum3335T+/btzeckJSXpww8/lI+PDwE+AAAA8BTQQgcAAADIYadPn5a7u7uWLl2qzZs3a/DgwTp//rw+/vhj3b5922JuWFiYatWqpd27d2vu3LlZus6FCxc0cuRIhYeH61//+pfKlCmj77//XkuWLLGYFx0dratXr+rPP//U/v37NXjwYO3Zs0ejRo2SJHXr1k2enp5WD98NDg7W+fPn1aJFi8d+LwAAAABkjh34AAAAQA57/vnnNXnyZPPrzz77TF5eXvryyy81bdo0ffrpp+axqlWrasyYMRbnx8bGKj093Wpdd3d3c9sbSerTp486deokSWrTpo0CAwMVFBSkOXPmqF27dhbnTZ8+XQUKFJDu7MbfsWOHDh8+LEkqUaKE6tWrp23btikmJkYeHh6SpJCQEJUvX17dunXLxncHAAAAwF3swAcAAABy2L0h+13dunVTmTJlzKH5XcWLF7eaGxgYqNq1a1v9Wbp0qcU8BwfL/Tqenp5q0KCBjhw5olu3blnUcze8v8vb21txcXHm1y1bttT169fN3wI4cuSIwsLC1LhxYzk6Omb5PQAAAADwcOzABwAAAGzEc889p6SkpIfOGzBggNLS0qyO169f/6Hnenh4KCEhQXFxcSpUqFCm8+5/WG3btm31yy+/aNOmTfr44481b9482dvbs/seAAAAeIoI8AEAAAAbEBUVpcjISFWrVu2hc3v27PnY14mIiFCJEiVUrFixLJ1nb2+vxo0ba86cOTp8+LBCQ0MVEBCgF1544bFrAQAAAPBgtNABAAAAclh0dLQiIiLMr9PT0zVs2DDFxcWpefPm2Xade68hSatWrVJISIgCAgKs2us8irfffluS9MUXX+j06dNq1apVttUKAAAAwBo78AEAAIAclpiYqE6dOqlRo0ZydXXV/v37tWvXLnXv3l3NmjXLtuvMnj1bx44dU4UKFXTp0iVt2LBBvr6++uqrrx5rvSpVqqhOnToKDQ1VlSpVzA/IBQAAAPB0sAMfAAAAyEHFixeXv7+/+vfvr4iICG3YsEH29vb69ttvNXbsWIu55cuXz3Krm3u9++67KlCggNatW6dTp06pTZs2mj9/vkqWLGme4+XlpfLly1ud6+XlJV9fX6vjAQEBMplMevXVV636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AACeroyf3vmMeP755/Xaa69Z/KlXr56KFy+uuLg4TZw4UT179rR4UOq6devMbVratm1rEd5LUrNmzdS8eXPpTquduzub73d/r/OiRYvqpZdeMr++deuW+ee77Xx0J+C+v9VN+fLlM32Y7e7du6U7H0i89957io6ONv+Ji4vTG2+8Id1p/7Nlyxar8wwGgwYMGGAR3ktStWrVHti253GVLFnS4rW3t7eqVKlifn23f/+j2rt3r/nDjxo1aqhu3boW70Hx4sXVsGFD6c7u/7u76O/Xr18/q/A+q4oWLZrhA3Mz+70vWbJEV65ckSQFBARYhPe6055n7Nix8vPzk+60BAoPD5fu9K6///edkJBg/ruZkpKiP//8U7rzAc3dh9suXLhQgwcP1rRp03Tw4EGlp6erWLFij/yQXQAAAAAAAADZ55negV+7dm398ssvVscvX76sjz/+WFu3btWaNWs0evRo8275e/vBV65cOcN17z1+7/yHKVSokPnne/udX758WbrT1/1u4P4ojEajOQBOSEhQq1atMpxnMBhkMpksdtPfvaaXl5eaNm36yNd8GgoWLGj++f4+8A9z+PBhc9/78PBw80Nu73VvD/t7d9Lf624v+ycRFham6dOn68yZM7p586YKFiwob29vFS5cOMP597ZFujfkz0xUVJT579vNmzfND9i9173v393fd+nSpdW2bVv997//1ZUrV8ytdezt7eXj46OaNWuqf//+mf59BwAAAAAAAPB0PNMBfmZKlSqlPn36aOvWrZKkjRs3msfufejs/Q9jvevesPf+B5w+jrsPPi1QoECWdkIbjUbzuS4uLhm28rnX3Qfumkwmi2tmR3idW+59aGyRIkUyDcvvsre3fyp1zJ8/X8OGDTM/FLdQoUJKSkrSuXPnMv07cu/xex+GnJm0tDTz38+CBQuqdOnSD5x/7+/1559/1vPPP6/169fryJEjiouLk9FoVEREhCIiIrR161YFBwebW/UAAIDcNWXKFF2/fj3T8bsPs4+KirJo25iRunXrqkmTJtleIwAAAIAnl3eT2afMy8tLdnZ25gfbJiUlydnZ2aJVzenTpzM8995e9MWKFXviWooVK6aTJ08qLi5OGzZsUNu2bR/pPEdHRxUrVkxRUVEymf6PvfsOi+LcwgD+LkvvIIoaWxQVo+KNXWPviYq9G2tijw0bauxd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Y8N4xjOe8YxnPOMZz3jGM57xjAr1oRUAACAASURBVGc84xnPeMYznvGMV0O8jo6OQiqVqsRpA62cgS+TyQAAhw8fVtlWu3Ztlc+8vb0RERGR77EYz3jGM57xjGc84xnPeMYznvGMZzzjGc94xjOe8Z8mftCgQZDJZFAoFPnu/6UTKLTwyuvVqwcACAsLU3cqRERERERERERERFQAPT09SKVSSCQS6Opq33x0rSzgS6VSANDKHzgRERERERERERFRSWFrawuxWIzk5GQIBAJ1p/PZaWUFm4V7IiIiIiIiIiIiIs0nEokgl8u1sngPbZ2BT0RERERERERERESk6XTUnQAREREREREREREREanSygK+o6MjHB0d1Z0GEREREREREREREVGBtLKFTm6/JC28dCIiIiIiIiIiIqISw8XFBRKJBLNmzVJ3KmrBAj4RERERERERERERaSRDQ0NIJBJkZWVBKBSqO53PTitb6BARERERERERERGR5pPJZJDL5Vo7GZsFfCIiIiIiIiIiIiIiDcQCPhERERERERERERGRBmIBn4iIiIiIiIiIiIhIA+mqOwF1cHBwUHcKRERERERERERERESFEii0sPu/VCoFAOjqauXzCyIiIiIiIiIiIqISwdbWFmKxGMnJyRAIBOpO57PTygo2C/dEREREREREREREmk8kEkEul2tl8R7aOgOfiIiIiIiIiIiIiEjTcRFbIiIiIiIiIiIiIiINpJUFfEdHRzg6Oqo7DSIiIiIiIiIiIiKiAmllC53cfklaeOlEREREREREREREJYaLiwskEglmzZql7lTUggV8IiIiIiIiIiIiItJIhoaGkEgkyMrKglAoVHc6n51WttAhIiIiIiIiIiIiIs0nk8kgl8u1djI2C/hERERERERERERERBqIBXwiIiIiIiIiIiIiIg3EAj4RERERERERERERkQbSVXcC6uDg4KDuFIiIiIiIiIiIiIiICiVQaGH3f6lUCgDQ1dXK5xdEREREREREREREJYKtrS3EYjGSk5MhEAjUnc5np5UVbBbuiYiIiIiIiIiIiDSfSCSCXC7XyuI9tHUGPhERERERERERERGRpuMitkREREREREREREREGkgrC/iOjo5wdHRUdxpERERERERERERERAXSyhY6uf2StPDSiYiIiIiIiIiIiEoMFxcXSCQSzJo1S92pqAUL+ERERERERERERESkkQwNDSGRSJCVlQWhUKjudD47rWyhQ0RERERERERERESaTyaTQS6Xa+1kbBbwiYiIiIiIiIiIiIg0EAv4REREREREREREREQaiAV8IiIiIiIiIiIiIiINpKvuBNTBwcFB3SkQERERERERERERERVKoNDC7v9SqRQAoKurmc8vYpOz1J0CERER0SdjaSSEmaFQ3WkQvZc0sRzJr6XqToOIiIjokzE3FMLCSPPG6ba2thCLxUhOToZAIFB3Op+dZlawPzFNLdznqjTnprpTICIiIvpk1vSpgJmdbNWdBtF72X4lEdMOx6o7DSIiIqJPZkYnW6ztU0HdaagQiUSQy+VaWbyHthbwS4pyFvrqToGIiIio2KRkypAulqk7DaKPYqKvA3Mj3kYRERHRlyNNLENqpuaO0+3s7NSdglpx5KnB/OfVVXcKRERERMVmxdk4bPWOV3caRB9lQGMbLHCsqO40iIiIiIrNFu94rDwbp+40qAA66k5AHRwdHeHo6KjuNIiIiIiIiIiIiIiICqSVM/BdXV3VnQIRERERERERERERvYOLiwskEglmzZql7lTUQisL+ERERERERERERESk+ZydnSGRSODk5AShUKjudD47rWyhQ0RERERERERERESaTyaTQS6XQ6FQqDsVtWABn4iIiIiIiIiIiIhIA7GAT0RERERERERERESkgVjAJyIiIiIiIiIiIiLSQFq5iK2Dg4O6UyAiIiIiIiIiIiIiKpRWFvBDQkLUnQIRERERERERERERvYO1tTXEYjGEQqG6U1ELrSzg6+pq5WUTERERERERERERlSgikQhyuRwCgUDdqagFK9lEREREREREREREpJHs7OzUnYJacRFbIiIiIiIiIiIiIiINpJUFfEdHRzg6Oqo7DSIiIiIiIiIiIiKiAmllCx1XV1d1p0BERERERERERERE7+Di4gKJRIJZs2apOxW10MoCPhERERERERERERFpPmdnZ0gkEjg5OUEoFKo7nc9OK1voEBEREREREREREZHmk8lkkMvlUCgU6k5FLVjAJyIiIiIiIiIiIiLSQCzgExERERERERERERFpIBbwiYiIiIiIiIiIiIg0kFYuYuvg4KDuFIiIiIiIiIiIiIiICqWVBfyQkBB1p0BERERERERERERE72BtbQ2xWAyhUKjuVNRCKwv4urpaedlEREREREREREREJYpIJIJcLodAIFB3KmrBSjYRERERERERERERaSQ7Ozt1p6BWXMSWiIiIiIiIiIiIiEgDaWUB39HREY6OjupOg4iIiIiIiIiIiIioQFrZQsfV1VXdKRARERERERERERHRO7i4uEAikWDWrFnqTkUttLKAT0RERERERERERESaz9nZGRKJBE5OThAKhepO57PTyhY6RERERERERERERKT5ZDIZ5HI5FAqFulNRCxbwiYiIiIiIiIiIiIg0EAv4REREREREREREREQaiAV8IiIiIiIiIiIiIiINpJWL2Do4OKg7BSIiIiIiIiIiIiKiQmllAT8kJETdKRARERERERERERHRO1hbW0MsFkMoFKo7FbXQygK+rq5WXjYRERERERERERFRiSISiSCXyyEQCNSdilqwkk1EREREREREREREGsnOzk7dKagVF7ElIiIiIiIiIiIiItJAWlnAd3R0hKOjo7rTICIiIiIiIiIiIiIqkFa20HF1dVV3CkRERERERERERET0Di4uLpBIJJg1a5a6U1ELrSzgExEREREREREREZHmc3Z2hkQigZOTE4RCobrT+ey0soUOEREREREREREREWk+mUwGuVwOhUKh7lTUggV8IiIiIiIiIiIiIiINxAI+EREREREREREREZEGYgGfiIiIiIiIiIiIiEgDaeUitg4ODupOgYiIiIiIiIiIiIioUFpZwA8JCVF3CkRERERERERERET0DtbW1hCLxRAKhepORS20soCvq6uVl01ERERERERERERUoohEIsjlcggEAnWnohasZBMRERERERERERGRRrKzs1N3CmrFAj4RfZH+3bUFj2MfYeaClZ/k+FliMfQNDD7JsT8HuVyOvds3IfJ2OBRyBZq2agvHPoPUnRYRUbGQSqXYtWsXbG1t4ejoqO506BM6duwYUlNT8eOPP2rtK9VE2sLz4lmEBl1F+y7dUa9B4092npI+zn9bgMgbnhfOIPlFIswsLDFy3BRUqFRF3WkREdF70FF3Aurg6OjImzmiYrJq4SxMGNYHh/Zsf2fs4tmTMXZIT6SlpnzyvPbt2IQgf99Pcuxfncaje+v6OPbv7k9y/M/hV6fx2Lh2KS6eOQH3cydxIyRQ3Sl9lL/Xr8aE4X0hk8nUncp7iXoQiSVzpqB/lxbo3Kw2+n/fEkucp+JR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Yd/t0d88pF/98m4d95zB/S0dx9GN37pWDz94v4yYoRed+lK95OVn+e/12a+6UIkBPYSfeOwRfffGb6lULGhqJqdXXfBqPf0ZxwysoVIu6YbrvqYnHn9UyWRSxz/nRJ13cX7FjXC7a/xPrztXTz3xuK76wnXaPmAjNY/rurrj1pt0z89/omazqdzmLbrotW/QliWr4qvViv5l4TZt3ry1rxeoJP3kRz/U/v17dcbZ5yqTGev7/sMP3v/b24BrVW3avFUXX/ImZQ9suDzMA7++T7d8Z5fKxaKmpmd03sX5ka7FnW/9E/3zt7+pv7zsCr1xhZX6QFh88PpH9fe3PaUPv/Fovf2CbevyGk8++aQuu+wyXXPNNbr88sv1h3/I5+NI9ulPf1rvfOc79drXvlbvfe97dfTRR6/ba33klj1621cf0X85c6venR/8/zdgo2o06lq47RZlsxND99/xPPzQA/r1fffqGc98lk448QUDx1SrFd34za9r3949SqZSOunkF+vFLz1jxeduNhu6cde12vPU4xofn9BZ516oo595rH7yox+qsLi/53fwbo7j6I5bb9Z9d/9c9XpVU9M5vezMV65qwcbPdt+l/fv26qSTT9WWrU+TDvx747bv3qhMZkxnnH1u32O8czc+ntXpr3jlwO9f95Wr9dSTjymdHtMLTzlNpw9YSX33z36sH37/e6pWykqPjen5s6fojLPP7VvQseepJ/SLn/5YW7Zu00knL38naavZ1B3fu3nZurxj+/aub+jJxx6WYcT03OedpLNedYEe/PV9euiB+3X8Cb+nZx07eHPWX917t/7l+99TpVLW1MyMznrlBTrm2OOWreeef/2p7rzjVlXLJWXGxnTiSSfrzHPOW9XK9F/de7f+66V5TU3P6HPXfEczm4a3R1vct1c33XCdnnricZmmqWcc8yyd/+pL+v6tJUnfu/nbchxH55x/kWKx/m7T3p5Xr7rwNQNfq16v6cZvfl179zypRCKpF7zoVJ12+iuG1vebh+7X/ff9Us889riB/56x2m390Zsu0q/vu1cf/Oin9KoLubMM6+eq257S317/qP73Bdt0+RvX7/eptUokEup0OrIsa2CedKQjwA8hAnwAWNnVn/mEPvqh9+js8y7SFZ/4xxEeceS49aYb9Nf/68/0nBOfr09/+VsjT3wAQTscAb7nrrsObNB3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" alt="OVS `balance-slb` mode ` operating on a localnet with two NADs" />
<figcaption>OVS <code>balance-slb</code> mode operating on a localnet with two NADs</figcaption>
</figure>

You can integrate the `balance-slb` mode interface into primary or secondary network types by using OVS bonding. Note the following points about OVS bonding:

- Supports the OVN-Kubernetes CNI plugin and easily integrates with the plugin.

- Natively supports `balance-slb` mode.

<div>

<div class="title">

Prerequisites

</div>

- You have more than one physical interface attached to your primary network and you defined the interfaces in a `MachineConfig` file.

- You created a manifest object and defined a customized `br-ex` bridge in the object configuration file.

- You have more than one physical interfaces attached to your primary network and you defined the interfaces in a NAD CRD file.

</div>

<div>

<div class="title">

Procedure

</div>

1.  For each bare-metal host that exists in a cluster, in the `install-config.yaml` file for your cluster define a `networkConfig` section similar to the following example:

    ``` yaml
    # ...
    networkConfig:
      interfaces:
        - name: enp1s0
          type: ethernet
          state: up
          ipv4:
            dhcp: true
            enabled: true
          ipv6:
            enabled: false
        - name: enp2s0
          type: ethernet
          state: up
          mtu: 1500
          ipv4:
            dhcp: true
            enabled: true
          ipv6:
            dhcp: true
            enabled: true
        - name: enp3s0
          type: ethernet
          state: up
          mtu: 1500
          ipv4:
            enabled: false
          ipv6:
            enabled: false
    # ...
    ```

    where:

    `enp1s0`
    The interface for the provisioned network interface controller (NIC).

    `enp2s0`
    The first bonded interface that pulls in the Ignition config file for the bond interface.

    `mtu`
    Manually set the `br-ex` maximum transmission unit (MTU) on the bond ports.

    `enp3s0`
    The second bonded interface is part of a minimal configuration that pulls ignition during cluster installation.

2.  Define each network interface in an NMState configuration file:

    <div class="formalpara">

    <div class="title">

    Example NMState configuration file that defines many network interfaces

    </div>

    ``` yaml
    ovn:
      bridge-mappings:
        - localnet: localnet-network
          bridge: br-ex
          state: present
    interfaces:
      - name: br-ex
        type: ovs-bridge
        state: up
        bridge:
          allow-extra-patch-ports: true
          port:
            - name: br-ex
            - name: patch-ex-to-phy
        ovs-db:
          external_ids:
            bridge-uplink: "patch-ex-to-phy"
      - name: br-ex
        type: ovs-interface
        state: up
        mtu: 1500
        ipv4:
          enabled: true
          dhcp: true
          auto-route-metric: 48
        ipv6:
          enabled: false
          dhcp: false
          auto-route-metric: 48
      - name: br-phy
        type: ovs-bridge
        state: up
        bridge:
          allow-extra-patch-ports: true
          port:
            - name: patch-phy-to-ex
            - name: ovs-bond
              link-aggregation:
                mode: balance-slb
                port:
                  - name: enp2s0
                  - name: enp3s0
      - name: patch-ex-to-phy
        type: ovs-interface
        state: up
        patch:
          peer: patch-phy-to-ex
      - name: patch-phy-to-ex
        type: ovs-interface
        state: up
        patch:
          peer: patch-ex-to-phy
      - name: enp1s0
        type: ethernet
        state: up
        ipv4:
          dhcp: true
          enabled: true
        ipv6:
          enabled: false
      - name: enp2s0
        type: ethernet
        state: up
        mtu: 1500
        ipv4:
          enabled: false
        ipv6:
          enabled: false
      - name: enp3s0
        type: ethernet
        state: up
        mtu: 1500
        ipv4:
          enabled: false
        ipv6:
          enabled: false
    # ...
    ```

    </div>

    where:

    `mtu`
    Manually set the `br-ex` MTU on the bond ports.

3.  Use the `base64` command to encode the interface content of the NMState configuration file:

    ``` terminal
    $ base64 -w0  <nmstate_configuration>.yml
    ```

    `<nmstate_configuration>`: Where the `-w0` option prevents line wrapping during the base64 encoding operation.

4.  Create `MachineConfig` manifest files for the `master` role and the `worker` role. Ensure that you embed the base64-encoded string from an earlier command into each `MachineConfig` manifest file. The following example manifest file configures the `master` role for all nodes that exist in a cluster. You can also create a manifest file for `master` and `worker` roles specific to a node.

    ``` yaml
    apiVersion: machineconfiguration.openshift.io/v1
    kind: MachineConfig
    metadata:
      labels:
        machineconfiguration.openshift.io/role: master
      name: 10-br-ex-master
    spec:
      config:
        ignition:
          version: 3.2.0
        storage:
          files:
          - contents:
              source: data:text/plain;charset=utf-8;base64,<base64_encoded_nmstate_configuration>
            mode: 0644
            overwrite: true
            path: /etc/nmstate/openshift/cluster.yml
    ```

    where:

    `name`
    The name of the policy.

    `source`
    Writes the encoded base64 information to the specified path.

    `path`
    Specify the path to the `cluster.yml` file. For each node in your cluster, you can specify the short hostname path to your node, such as `<node_short_hostname>`.yml.

5.  Save each `MachineConfig` manifest file to the `./<installation_directory>/manifests` directory, where `<installation_directory>` is the directory in which the installation program creates files.

    The Machine Config Operator (MCO) takes the content from each manifest file and consistently applies the content to all selected nodes during a rolling update.

</div>

# Preparing the user-provisioned infrastructure

Before you install OpenShift Container Platform on user-provisioned infrastructure, you must prepare the underlying infrastructure.

This section provides details about the high-level steps required to set up your cluster infrastructure in preparation for an OpenShift Container Platform installation. This includes configuring IP networking and network connectivity for your cluster nodes, enabling the required ports through your firewall, and setting up the required DNS and load balancing infrastructure.

After preparation, your cluster infrastructure must meet the requirements outlined in the *Requirements for a cluster with user-provisioned infrastructure* section.

<div>

<div class="title">

Prerequisites

</div>

- You have reviewed the [OpenShift Container Platform 4.x Tested Integrations](https://access.redhat.com/articles/4128421) page.

- You have reviewed the infrastructure requirements detailed in the *Requirements for a cluster with user-provisioned infrastructure* section.

</div>

<div>

<div class="title">

Procedure

</div>

1.  If you are using DHCP to provide the IP networking configuration to your cluster nodes, configure your DHCP service.

    1.  Add persistent IP addresses for the nodes to your DHCP server configuration. In your configuration, match the MAC address of the relevant network interface to the intended IP address for each node.

    2.  When you use DHCP to configure IP addressing for the cluster machines, the machines also obtain the DNS server information through DHCP. Define the persistent DNS server address that is used by the cluster nodes through your DHCP server configuration.

        > [!NOTE]
        > If you are not using a DHCP service, you must provide the IP networking configuration and the address of the DNS server to the nodes at RHCOS install time. These can be passed as boot arguments if you are installing from an ISO image. See the *Installing RHCOS and starting the OpenShift Container Platform bootstrap process* section for more information about static IP provisioning and advanced networking options.

    3.  Define the hostnames of your cluster nodes in your DHCP server configuration. See the *Setting the cluster node hostnames through DHCP* section for details about hostname considerations.

        > [!NOTE]
        > If you are not using a DHCP service, the cluster nodes obtain their hostname through a reverse DNS lookup.

2.  Ensure that your network infrastructure provides the required network connectivity between the cluster components. See the *Networking requirements for user-provisioned infrastructure* section for details about the requirements.

3.  Configure your firewall to enable the ports required for the OpenShift Container Platform cluster components to communicate. See *Networking requirements for user-provisioned infrastructure* section for details about the ports that are required.

    > [!IMPORTANT]
    > By default, port `1936` is accessible for an OpenShift Container Platform cluster, because each control plane node needs access to this port.
    >
    > For ingress health check probes, the `/healthz/ready` endpoint is available on this port.
    >
    > Avoid using the Ingress load balancer to expose this port, because doing so might result in the exposure of sensitive information, such as statistics and metrics, related to Ingress Controllers.

4.  Setup the required DNS infrastructure for your cluster.

    1.  Configure DNS name resolution for the Kubernetes API, the application wildcard, the bootstrap machine, the control plane machines, and the compute machines.

    2.  Configure reverse DNS resolution for the Kubernetes API, the bootstrap machine, the control plane machines, and the compute machines.

        See the *User-provisioned DNS requirements* section for more information about the OpenShift Container Platform DNS requirements.

5.  Validate your DNS configuration.

    1.  From your installation node, run DNS lookups against the record names of the Kubernetes API, the wildcard routes, and the cluster nodes. Validate that the IP addresses in the responses correspond to the correct components.

    2.  From your installation node, run reverse DNS lookups against the IP addresses of the load balancer and the cluster nodes. Validate that the record names in the responses correspond to the correct components.

        See the *Validating DNS resolution for user-provisioned infrastructure* section for detailed DNS validation steps.

6.  Provision the required API and application ingress load balancing infrastructure. See the *Load balancing requirements for user-provisioned infrastructure* section for more information about the requirements.

    > [!NOTE]
    > Some load balancing solutions require the DNS name resolution for the cluster nodes to be in place before the load balancing is initialized.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Installing RHCOS and starting the OpenShift Container Platform bootstrap process](installing-bare-metal.md#creating-machines-bare-metal_installing-bare-metal)

- [Setting the cluster node hostnames through DHCP](installing-bare-metal.md#installation-host-names-dhcp-user-infra_installing-bare-metal)

- [Advanced RHCOS installation configuration](installing-bare-metal.md#installation-user-infra-machines-advanced_installing-bare-metal)

- [Networking requirements for user-provisioned infrastructure](installing-bare-metal.md#installation-network-user-infra_installing-bare-metal)

- [User-provisioned DNS requirements](installing-bare-metal.md#installation-dns-user-infra_installing-bare-metal)

- [Validating DNS resolution for user-provisioned infrastructure](installing-bare-metal.md#installation-user-provisioned-validating-dns_installing-bare-metal)

- [Load balancing requirements for user-provisioned infrastructure](installing-bare-metal.md#installation-load-balancing-user-infra_installing-bare-metal)

</div>

# Validating DNS resolution for user-provisioned infrastructure

To prevent network-related installation failures and ensure node connectivity in OpenShift Container Platform, validate your DNS configuration before deploying on user-provisioned infrastructure.

> [!IMPORTANT]
> The validation steps detailed in this section must succeed before you install your cluster.

<div>

<div class="title">

Prerequisites

</div>

- You have configured the required DNS records for your user-provisioned infrastructure.

</div>

<div>

<div class="title">

Procedure

</div>

1.  From your installation node, run DNS lookups against the record names of the Kubernetes API, the wildcard routes, and the cluster nodes. Validate that the IP addresses contained in the responses correspond to the correct components.

    1.  Perform a lookup against the Kubernetes API record name. Check that the result points to the IP address of the API load balancer:

        ``` terminal
        $ dig +noall +answer @<nameserver_ip> api.<cluster_name>.<base_domain>
        ```

        Replace `<nameserver_ip>` with the IP address of the name server, `<cluster_name>` with your cluster name, and `<base_domain>` with your base domain name.

        <div class="formalpara">

        <div class="title">

        Example output

        </div>

        ``` terminal
        api.ocp4.example.com.        604800  IN  A   192.168.1.5
        ```

        </div>

    2.  Perform a lookup against the Kubernetes internal API record name. Check that the result points to the IP address of the API load balancer:

        ``` terminal
        $ dig +noall +answer @<nameserver_ip> api-int.<cluster_name>.<base_domain>
        ```

        <div class="formalpara">

        <div class="title">

        Example output

        </div>

        ``` terminal
        api-int.ocp4.example.com.        604800  IN  A   192.168.1.5
        ```

        </div>

    3.  Test an example `*.apps.<cluster_name>.<base_domain>` DNS wildcard lookup. All of the application wildcard lookups must resolve to the IP address of the application ingress load balancer:

        ``` terminal
        $ dig +noall +answer @<nameserver_ip> random.apps.<cluster_name>.<base_domain>
        ```

        <div class="formalpara">

        <div class="title">

        Example output

        </div>

        ``` terminal
        random.apps.ocp4.example.com.        604800  IN  A   192.168.1.5
        ```

        </div>

        > [!NOTE]
        > In the example outputs, the same load balancer is used for the Kubernetes API and application ingress traffic. In production scenarios, you can deploy the API and application ingress load balancers separately so that you can scale the load balancer infrastructure for each in isolation.

        You can replace `random` with another wildcard value. For example, you can query the route to the OpenShift Container Platform console:

        ``` terminal
        $ dig +noall +answer @<nameserver_ip> console-openshift-console.apps.<cluster_name>.<base_domain>
        ```

        <div class="formalpara">

        <div class="title">

        Example output

        </div>

        ``` terminal
        console-openshift-console.apps.ocp4.example.com. 604800 IN   A 192.168.1.5
        ```

        </div>

    4.  Run a lookup against the bootstrap DNS record name. Check that the result points to the IP address of the bootstrap node:

        ``` terminal
        $ dig +noall +answer @<nameserver_ip> bootstrap.<cluster_name>.<base_domain>
        ```

        <div class="formalpara">

        <div class="title">

        Example output

        </div>

        ``` terminal
        bootstrap.ocp4.example.com.      604800  IN  A   192.168.1.96
        ```

        </div>

    5.  Use this method to perform lookups against the DNS record names for the control plane and compute nodes. Check that the results correspond to the IP addresses of each node.

2.  From your installation node, run reverse DNS lookups against the IP addresses of the load balancer and the cluster nodes. Validate that the record names contained in the responses correspond to the correct components.

    1.  Perform a reverse lookup against the IP address of the API load balancer. Check that the response includes the record names for the Kubernetes API and the Kubernetes internal API:

        ``` terminal
        $ dig +noall +answer @<nameserver_ip> -x 192.168.1.5
        ```

        <div class="formalpara">

        <div class="title">

        Example output

        </div>

        ``` terminal
        5.1.168.192.in-addr.arpa. 604800 IN  PTR api-int.ocp4.example.com.
        5.1.168.192.in-addr.arpa. 604800    IN  PTR api.ocp4.example.com.
        ```

        </div>

        where:

        `api-int.ocp4.example.com`
        Specifies the record name for the Kubernetes internal API.

        `api.ocp4.example.com`
        Specifies the record name for the Kubernetes API.

        > [!NOTE]
        > A PTR record is not required for the OpenShift Container Platform application wildcard. No validation step is needed for reverse DNS resolution against the IP address of the application ingress load balancer.

    2.  Perform a reverse lookup against the IP address of the bootstrap node. Check that the result points to the DNS record name of the bootstrap node:

        ``` terminal
        $ dig +noall +answer @<nameserver_ip> -x 192.168.1.96
        ```

        <div class="formalpara">

        <div class="title">

        Example output

        </div>

        ``` terminal
        96.1.168.192.in-addr.arpa. 604800    IN  PTR bootstrap.ocp4.example.com.
        ```

        </div>

    3.  Use this method to perform reverse lookups against the IP addresses for the control plane and compute nodes. Check that the results correspond to the DNS record names of each node.

</div>

<div>

<div class="title">

Additional resources

</div>

- [User-provisioned DNS requirements](installing-bare-metal.md#installation-dns-user-infra_installing-bare-metal)

- [Load balancing requirements for user-provisioned infrastructure](installing-bare-metal.md#installation-load-balancing-user-infra_installing-bare-metal)

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

- When you install OpenShift Container Platform, provide the SSH public key to the installation program. If you install a cluster on infrastructure that you provision, you must provide the key to the installation program.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Verifying node health](../../../support/troubleshooting/verifying-node-health.md#verifying-node-health)

</div>

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

# Installing the OpenShift CLI on Linux

To manage your cluster and deploy applications from the command line on Linux, install the OpenShift CLI (`oc`) binary. You can download the OpenShift CLI (`oc`) from the Red  Customer Portal.

> [!IMPORTANT]
> If you installed an earlier version of `oc`, you cannot use it to complete all of the commands in OpenShift Container Platform.
>
> Download and install the new version of `oc`.

<div>

<div class="title">

Procedure

</div>

1.  Navigate to the [Download OpenShift Container Platform](https://access.redhat.com/downloads/content/290) page on the Red Hat Customer Portal.

2.  Select the architecture from the **Product Variant** list.

3.  Select the appropriate version from the **Version** list.

4.  Click **Download Now** next to the **OpenShift v4.17 Linux Clients** entry and save the file.

5.  Unpack the archive:

    ``` terminal
    $ tar xvf <file>
    ```

6.  Place the `oc` binary in a directory that is on your `PATH`.

    To check your `PATH`, execute the following command:

    ``` terminal
    $ echo $PATH
    ```

</div>

<div>

<div class="title">

Verification

</div>

- After you install the OpenShift CLI, it is available using the `oc` command:

  ``` terminal
  $ oc <command>
  ```

</div>

# Installing the OpenShift CLI on Windows

To manage your cluster and deploy applications from the command line on Windows, install the OpenShift CLI (`oc`) binary. You can download the OpenShift CLI (`oc`) from the Red  Customer Portal.

> [!IMPORTANT]
> If you installed an earlier version of `oc`, you cannot use it to complete all of the commands in OpenShift Container Platform.
>
> Download and install the new version of `oc`.

<div>

<div class="title">

Procedure

</div>

1.  Navigate to the [Download OpenShift Container Platform](https://access.redhat.com/downloads/content/290) page on the Red Hat Customer Portal.

2.  Select the appropriate version from the **Version** list.

3.  Click **Download Now** next to the **OpenShift v4.17 Windows Client** entry and save the file.

4.  Extract the archive with a ZIP program.

5.  Move the `oc` binary to a directory that is on your `PATH` variable.

    To check your `PATH` variable, open the command prompt and execute the following command:

    ``` terminal
    C:\> path
    ```

</div>

<div>

<div class="title">

Verification

</div>

- After you install the OpenShift CLI, it is available using the `oc` command:

  ``` terminal
  C:\> oc <command>
  ```

</div>

# Installing the OpenShift CLI on macOS

To manage your cluster and deploy applications from the command line on macOS, install the OpenShift CLI (`oc`) binary. You can download the OpenShift CLI (`oc`) from the Red  Customer Portal.

> [!IMPORTANT]
> If you installed an earlier version of `oc`, you cannot use it to complete all of the commands in OpenShift Container Platform.
>
> Download and install the new version of `oc`.

<div>

<div class="title">

Procedure

</div>

1.  Navigate to the [Download OpenShift Container Platform](https://access.redhat.com/downloads/content/290) page on the Red Hat Customer Portal.

2.  Select the architecture from the **Product Variant** list.

3.  Select the appropriate version from the **Version** list.

4.  Click **Download Now** next to the **OpenShift v4.17 macOS Clients** entry and save the file.

    > [!NOTE]
    > For macOS arm64, choose the **OpenShift v4.17 macOS arm64 Client** entry.

5.  Unpack and unzip the archive.

6.  Move the `oc` binary to a directory on your `PATH` variable.

    To check your `PATH` variable, open a terminal and execute the following command:

    ``` terminal
    $ echo $PATH
    ```

</div>

<div>

<div class="title">

Verification

</div>

- Verify your installation by using an `oc` command:

  ``` terminal
  $ oc <command>
  ```

</div>

# Manually creating the installation configuration file

Installing the cluster requires that you manually create the installation configuration file.

<div>

<div class="title">

Prerequisites

</div>

- You have an SSH public key on your local machine for use with the installation program. You can use the key for SSH authentication onto your cluster nodes for debugging and disaster recovery.

- You have obtained the OpenShift Container Platform installation program and the pull secret for your cluster.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create an installation directory to store your required installation assets in:

    ``` terminal
    $ mkdir <installation_directory>
    ```

    > [!IMPORTANT]
    > You must create a directory. Some installation assets, such as bootstrap X.509 certificates have short expiration intervals, so you must not reuse an installation directory. If you want to reuse individual files from another cluster installation, you can copy them into your directory. However, the file names for the installation assets might change between releases. Use caution when copying installation files from an earlier OpenShift Container Platform version.

2.  Customize the provided sample `install-config.yaml` file template and save the file in the `<installation_directory>`.

    > [!NOTE]
    > You must name this configuration file `install-config.yaml`.

3.  Back up the `install-config.yaml` file so that you can use it to install many clusters.

    > [!IMPORTANT]
    > Back up the `install-config.yaml` file now, because the installation process consumes the file in the next step.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Installation configuration parameters for bare metal](installation-config-parameters-bare-metal.md#installation-config-parameters-bare-metal)

</div>

## Sample install-config.yaml file for bare metal

You can customize the `install-config.yaml` file to specify more details about your OpenShift Container Platform cluster platform or modify the values of the required parameters.

``` yaml
apiVersion: v1
baseDomain: example.com
compute:
- hyperthreading: Enabled
  name: worker
  replicas: 0
controlPlane:
  hyperthreading: Enabled
  name: master
  replicas: 3
metadata:
  name: test
networking:
  clusterNetwork:
  - cidr: 10.128.0.0/14
    hostPrefix: 23
  networkType: OVNKubernetes
  machineNetwork:
  - cidr: 192.168.0.0/16
  serviceNetwork:
  - 172.30.0.0/16
platform:
  none: {}
fips: false
pullSecret: '{"auths": ...}'
sshKey: 'ssh-ed25519 AAAA...'
```

where:

`baseDomain`
Specifies the base domain of the cluster. All DNS records must be sub-domains of this base and include the cluster name.

`compute`
Specifies the `compute` node configurations, which is a sequence of mappings. To meet the requirements of the different data structures, the first line of the `compute` section must begin with a hyphen, `-`.

`controlPlane`
Specifies the `controlPlane` node configurations, which is a single mapping. To meet the requirements of the different data structures, the first line of the `controlPlane` section must not. Only one control plane pool is used.

`hyperthreading`
Specifies whether to enable or disable simultaneous multithreading (SMT), or hyperthreading. By default, SMT is enabled to increase the performance of the cores in your machines. You can disable it by setting the parameter value to `Disabled`. If you disable SMT, you must disable it in all cluster machines; this includes both control plane and compute machines.

> [!NOTE]
> Simultaneous multithreading (SMT) is enabled by default. If SMT is not enabled in your BIOS settings, the `hyperthreading` parameter has no effect.

> [!IMPORTANT]
> If you disable `hyperthreading`, whether in the BIOS or in the `install-config.yaml` file, ensure that your capacity planning accounts for the dramatically decreased machine performance.

`compute.replicas`
Specifies the number of compute machines that the cluster creates and manages for you on installer-provisioned installations. You must set this value to `0` when you install OpenShift Container Platform on user-provisioned infrastructure. Additionally for user-provisioned installations, you must manually deploy the compute machines before you finish installing the cluster.

> [!NOTE]
> If you are installing a three-node cluster, do not deploy any compute machines when you install the Red Hat Enterprise Linux CoreOS (RHCOS) machines.

`controlPlane.replicas`
Specifies the number of control plane machines that you add to the cluster. Because the cluster uses these values as the number of etcd endpoints in the cluster, the value must match the number of control plane machines that you deploy.

`metadata.name`
Specifies the cluster name that you specified in your DNS records.

`networking.clusterNetwork.cidr`
Specifies a block of IP addresses from which pod IP addresses are allocated. This block must not overlap with existing physical networks. These IP addresses are used for the pod network. If you need to access the pods from an external network, you must configure load balancers and routers to manage the traffic.

> [!NOTE]
> Class E CIDR range is reserved for a future use. To use the Class E CIDR range, you must ensure your networking environment accepts the IP addresses within the Class E CIDR range.

`networking.cidr.hostPrefix`
Specifies the subnet prefix length to assign to each individual node. For example, if `hostPrefix` is set to `23`, then each node is assigned a `/23` subnet out of the given `cidr`, which allows for 510 (2^(32 - 23) - 2) pod IP addresses. If you are required to provide access to nodes from an external network, configure load balancers and routers to manage the traffic.

`networking.networkType`
Specifies the cluster network plugin to install. The default value `OVNKubernetes` is the only supported value.

`networking.serviceNetwork`
Specifies the IP address pool to use for service IP addresses. You can enter only one IP address pool. This block must not overlap with existing physical networks. If you need to access the services from an external network, configure load balancers and routers to manage the traffic.

`platform`
Specifies the platform. You must set the platform to `none`. You cannot provide additional platform configuration variables for your platform.

> [!IMPORTANT]
> Clusters that are installed with the platform type `none` are unable to use some features, such as managing compute machines with the Machine API. This limitation applies even if the compute machines that are attached to the cluster are installed on a platform that would normally support the feature. This parameter cannot be changed after installation.

`fips`
Specifies either enabling or disabling FIPS mode. By default, FIPS mode is not enabled. If FIPS mode is enabled, the Red Hat Enterprise Linux CoreOS (RHCOS) machines that OpenShift Container Platform runs on bypass the default Kubernetes cryptography suite and use the cryptography modules that are provided with RHCOS instead.

> [!IMPORTANT]
> To enable FIPS mode for your cluster, you must run the installation program from a Red Hat Enterprise Linux (RHEL) computer configured to operate in FIPS mode. For more information about configuring FIPS mode on RHEL, see [Switching RHEL to FIPS mode](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/security_hardening/switching-rhel-to-fips-mode_security-hardening).
>
> When running Red Hat Enterprise Linux (RHEL) or Red Hat Enterprise Linux CoreOS (RHCOS) booted in FIPS mode, OpenShift Container Platform core components use the RHEL cryptographic libraries that have been submitted to NIST for FIPS 140-2/140-3 Validation on only the x86_64, ppc64le, and s390x architectures.

`pullSecret`
Specifies the [pull secret from Red Hat OpenShift Cluster Manager](https://console.redhat.com/openshift/install/pull-secret). This pull secret allows you to authenticate with the services that are provided by the included authorities, including Quay.io, which serves the container images for OpenShift Container Platform components.

`sshKey`
Specifies the SSH public key for the `core` user in Red Hat Enterprise Linux CoreOS (RHCOS).

> [!NOTE]
> For production OpenShift Container Platform clusters on which you want to perform installation debugging or disaster recovery, specify an SSH key that your `ssh-agent` process uses.

<div>

<div class="title">

Additional resources

</div>

- [Load balancing requirements for user-provisioned infrastructure](installing-bare-metal.md#installation-load-balancing-user-infra_installing-bare-metal)

- [Cluster capabilities](../../overview/cluster-capabilities.md#cluster-capabilities)

- [Optional cluster capabilities in OpenShift Container Platform 4.17](../../overview/cluster-capabilities.md#explanation_of_capabilities_cluster-capabilities)

</div>

## Configuring the cluster-wide proxy during installation

Production environments can deny direct access to the internet and instead have an HTTP or HTTPS proxy available. You can configure a new OpenShift Container Platform cluster to use a proxy by configuring the proxy settings in the `install-config.yaml` file.

> [!NOTE]
> For bare-metal installations, if you do not assign node IP addresses from the range that is specified in the `networking.machineNetwork[].cidr` field in the `install-config.yaml` file, you must include them in the `proxy.noProxy` field.

<div>

<div class="title">

Prerequisites

</div>

- You have an existing `install-config.yaml` file.

- You have reviewed the sites that your cluster requires access to and determined whether any of them need to bypass the proxy. By default, all cluster egress traffic is proxied, including calls to hosting cloud provider APIs. You added sites to the `Proxy` object’s `spec.noProxy` field to bypass the proxy if necessary.

  > [!NOTE]
  > The `Proxy` object `status.noProxy` field is populated with the values of the `networking.machineNetwork[].cidr`, `networking.clusterNetwork[].cidr`, and `networking.serviceNetwork[]` fields from your installation configuration.
  >
  > For installations on Amazon Web Services (AWS), Google Cloud, Microsoft Azure, and Red Hat OpenStack Platform (RHOSP), the `Proxy` object `status.noProxy` field is also populated with the instance metadata endpoint (`169.254.169.254`).

</div>

<div>

<div class="title">

Procedure

</div>

1.  Edit your `install-config.yaml` file and add the proxy settings. For example:

    ``` yaml
    apiVersion: v1
    baseDomain: my.domain.com
    proxy:
      httpProxy: http://<username>:<pswd>@<ip>:<port>
      httpsProxy: https://<username>:<pswd>@<ip>:<port>
      noProxy: example.com
    additionalTrustBundle: |
        -----BEGIN CERTIFICATE-----
        <MY_TRUSTED_CA_CERT>
        -----END CERTIFICATE-----
    additionalTrustBundlePolicy: <policy_to_add_additionalTrustBundle>
    # ...
    ```

    where:

    `proxy.httpProxy`
    Specifies a proxy URL to use for creating HTTP connections outside the cluster. The URL scheme must be `http`.

    `proxy.httpsProxy`
    Specifies a proxy URL to use for creating HTTPS connections outside the cluster.

    `proxy.noProxy`
    Specifies a comma-separated list of destination domain names, IP addresses, or other network CIDRs to exclude from proxying. Preface a domain with `.` to match subdomains only. For example, `.y.com` matches `x.y.com`, but not `y.com`. Use `*` to bypass the proxy for all destinations.

    `additionalTrustBundle`
    If provided, the installation program generates a config map that is named `user-ca-bundle` in the `openshift-config` namespace to hold the additional CA certificates. If you provide `additionalTrustBundle` and at least one proxy setting, the `Proxy` object is configured to reference the `user-ca-bundle` config map in the `trustedCA` field. The Cluster Network Operator then creates a `trusted-ca-bundle` config map that merges the contents specified for the `trustedCA` parameter with the RHCOS trust bundle. The `additionalTrustBundle` field is required unless the proxy’s identity certificate is signed by an authority from the RHCOS trust bundle.

    `additionalTrustBundlePolicy`
    Specifies the policy that determines the configuration of the `Proxy` object to reference the `user-ca-bundle` config map in the `trustedCA` field. The allowed values are `Proxyonly` and `Always`. Use `Proxyonly` to reference the `user-ca-bundle` config map only when `http/https` proxy is configured. Use `Always` to always reference the `user-ca-bundle` config map. The default value is `Proxyonly`. Optional parameter.

    > [!NOTE]
    > The installation program does not support the proxy `readinessEndpoints` field.

    > [!NOTE]
    > If the installation program times out, restart and then complete the deployment by using the `wait-for` command of the installation program. For example:
    >
    > ``` terminal
    > $ ./openshift-install wait-for install-complete --log-level debug
    > ```

2.  Save the file and reference it when installing OpenShift Container Platform.

    The installation program creates a cluster-wide proxy that is named `cluster` that uses the proxy settings in the provided `install-config.yaml` file. If no proxy settings are provided, a `cluster` `Proxy` object is still created, but it will have a nil `spec`.

    > [!NOTE]
    > Only the `Proxy` object named `cluster` is supported, and no additional proxies can be created.

</div>

## Configuring a three-node cluster

To create smaller, resource-efficient clusters for testing and production, deploy a bare-metal cluster with zero compute machines. This optional configuration uses only three control plane machines, optimizing infrastructure resources for administrators and developers.

In three-node OpenShift Container Platform environments, the three control plane machines are schedulable, which means that your application workloads are scheduled to run on them.

<div>

<div class="title">

Prerequisites

</div>

- You have an existing `install-config.yaml` file.

</div>

<div>

<div class="title">

Procedure

</div>

- Ensure that the number of compute replicas is set to `0` in your `install-config.yaml` file, as shown in the following `compute` stanza:

  ``` yaml
  compute:
  - name: worker
    platform: {}
    replicas: 0
  # ...
  ```

  > [!NOTE]
  > You must set the value of the `replicas` parameter for the compute machines to `0` when you install OpenShift Container Platform on user-provisioned infrastructure, regardless of the number of compute machines you are deploying. In installer-provisioned installations, the parameter controls the number of compute machines that the cluster creates and manages for you. This does not apply to user-provisioned installations, where the compute machines are deployed manually.

</div>

For three-node cluster installations, follow these next steps:

- If you are deploying a three-node cluster with zero compute nodes, the Ingress Controller pods run on the control plane nodes. In three-node cluster deployments, you must configure your application ingress load balancer to route HTTP and HTTPS traffic to the control plane nodes. See the *Load balancing requirements for user-provisioned infrastructure* section for more information.

- When you create the Kubernetes manifest files in the following procedure, ensure that the `mastersSchedulable` parameter in the `<installation_directory>/manifests/cluster-scheduler-02-config.yml` file is set to `true`. This enables your application workloads to run on the control plane nodes.

- Do not deploy any compute nodes when you create the Red Hat Enterprise Linux CoreOS (RHCOS) machines.

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

    > [!WARNING]
    > If you are installing a three-node cluster, skip the following step to allow the control plane nodes to be schedulable.

    \+

    > [!IMPORTANT]
    > When you configure control plane nodes from the default unschedulable to schedulable, additional subscriptions are required. This is because control plane nodes then become compute nodes.

2.  Check that the `mastersSchedulable` parameter in the `<installation_directory>/manifests/cluster-scheduler-02-config.yml` Kubernetes manifest file is set to `false`. This setting prevents pods from being scheduled on the control plane machines:

    1.  Open the `<installation_directory>/manifests/cluster-scheduler-02-config.yml` file.

    2.  Locate the `mastersSchedulable` parameter and ensure that it is set to `false`.

    3.  Save and exit the file.

3.  To create the Ignition configuration files, run the following command from the directory that contains the installation program:

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

</div>

<div>

<div class="title">

Additional resources

</div>

- [Recovering from expired control plane certificates](../../../backup_and_restore/control_plane_backup_and_restore/disaster_recovery/scenario-3-expired-certs.md#dr-recovering-expired-certs)

</div>

# Installing RHCOS and starting the OpenShift Container Platform bootstrap process

To install OpenShift Container Platform on bare-metal infrastructure that you provision, install Red Hat Enterprise Linux CoreOS (RHCOS) by using the generated Ignition config files. Providing these files ensures the bootstrap process begins automatically after the machines reboot.

If you have configured suitable networking, DNS, and load balancing infrastructure, the OpenShift Container Platform bootstrap process begins automatically after the RHCOS machines have rebooted.

To install RHCOS on the machines, follow either the steps to use an ISO image or network PXE booting.

> [!NOTE]
> The compute node deployment steps included in this installation document are RHCOS-specific. If you choose instead to deploy RHEL-based compute nodes, you take responsibility for all operating system life cycle management and maintenance, including performing system updates, applying patches, and completing all other required tasks. Only RHEL 8 compute machines are supported.

You can configure RHCOS during ISO and PXE installations by using the following methods:

- Kernel arguments: You can use kernel arguments to provide installation-specific information. For example, you can specify the locations of the RHCOS installation files that you uploaded to your HTTP server and the location of the Ignition config file for the type of node you are installing. For a PXE installation, you can use the `APPEND` parameter to pass the arguments to the kernel of the live installer. For an ISO installation, you can interrupt the live installation boot process to add the kernel arguments. In both installation cases, you can use special `coreos.inst.*` arguments to direct the live installer, as well as standard installation boot arguments for turning standard kernel services on or off.

- Ignition configs: OpenShift Container Platform Ignition config files (`*.ign`) are specific to the type of node you are installing. You pass the location of a bootstrap, control plane, or compute node Ignition config file during the RHCOS installation so that it takes effect on first boot. In special cases, you can create a separate, limited Ignition config to pass to the live system. That Ignition config could do a certain set of tasks, such as reporting success to a provisioning system after completing installation. This special Ignition config is consumed by the `coreos-installer` to be applied on first boot of the installed system. Do not provide the standard control plane and compute node Ignition configs to the live ISO directly.

- `coreos-installer`: You can boot the live ISO installer to a shell prompt, which allows you to prepare the permanent system in a variety of ways before first boot. In particular, you can run the `coreos-installer` command to identify various artifacts to include, work with disk partitions, and set up networking. In some cases, you can configure features on the live system and copy them to the installed system.

  > [!NOTE]
  > As of version `0.17.0-3`, `coreos-installer` requires RHEL 9 or later to run the program. You can still use older versions of `coreos-installer` to customize RHCOS artifacts of newer OpenShift Container Platform releases and install metal images to disk. See "coreos-installer image mirror" to download older versions of the `coreos-installer` binary.

Whether to use an ISO or PXE install depends on your situation. A PXE install requires an available DHCP service and more preparation, but can make the installation process more automated. An ISO install is a more manual process and can be inconvenient if you are setting up more than a few machines.

<div>

<div class="title">

Additional resources

</div>

- [coreos-installer image mirror](https://mirror.openshift.com/pub/openshift-v4/x86_64/clients/coreos-installer/)

</div>

## Installing RHCOS by using an ISO image

To provision physical or virtual machines, install RHCOS by using a bootable ISO image.

<div>

<div class="title">

Prerequisites

</div>

- You have created the Ignition config files for your cluster.

- You have configured a suitable network, DNS, and load balancing infrastructure.

- You have an HTTP server that can be accessed from your computer, and from the machines that you create.

- You have reviewed the *Advanced RHCOS installation configuration* section for different ways to configure features, such as networking and disk partitioning.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Obtain the SHA512 digest for each of your Ignition config files. For example, you can use the following on a system running Linux to get the SHA512 digest for your `bootstrap.ign` Ignition config file:

    ``` terminal
    $ sha512sum <installation_directory>/bootstrap.ign
    ```

    The digests are provided to the `coreos-installer` in a later step to validate the authenticity of the Ignition config files on the cluster nodes.

2.  Upload the bootstrap, control plane, and compute node Ignition config files that the installation program created to your HTTP server. Note the URLs of these files.

    > [!IMPORTANT]
    > You can add or change configuration settings in your Ignition configs before saving them to your HTTP server. If you plan to add more compute machines to your cluster after you finish installation, do not delete these files.

3.  From the installation host, validate that the Ignition config files are available on the URLs. The following example gets the Ignition config file for the bootstrap node:

    ``` terminal
    $ curl -k http://<HTTP_server>/bootstrap.ign
    ```

    - \<HTTP_server\>: Replace `bootstrap.ign` with `master.ign` or `worker.ign` in the command to validate that the Ignition config files for the control plane and compute nodes are also available.

      <div class="formalpara">

      <div class="title">

      Example output

      </div>

      ``` terminal
        % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                       Dload  Upload   Total   Spent    Left  Speed
        0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0{"ignition":{"version":"3.2.0"},"passwd":{"users":[{"name":"core","sshAuthorizedKeys":["ssh-rsa...
      ```

      </div>

4.  Although it is possible to obtain the RHCOS images that are required for your preferred method of installing operating system instances from the [RHCOS image mirror](https://mirror.openshift.com/pub/openshift-v4/x86_64/dependencies/rhcos/) page, the recommended way to obtain the correct version of your RHCOS images are from the output of `openshift-install` command:

    ``` terminal
    $ openshift-install coreos print-stream-json | grep '\.iso[^.]'
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    "location": "<url>/art/storage/releases/rhcos-4.20-aarch64/<release>/aarch64/rhcos-<release>-live.aarch64.iso",
    "location": "<url>/art/storage/releases/rhcos-4.20-ppc64le/<release>/ppc64le/rhcos-<release>-live.ppc64le.iso",
    "location": "<url>/art/storage/releases/rhcos-4.20-s390x/<release>/s390x/rhcos-<release>-live.s390x.iso",
    "location": "<url>/art/storage/releases/rhcos-4.20/<release>/x86_64/rhcos-<release>-live.x86_64.iso",
    ```

    </div>

    > [!IMPORTANT]
    > The RHCOS images might not change with every release of OpenShift Container Platform. You must download images with the highest version that is less than or equal to the OpenShift Container Platform version that you install. Use the image versions that match your OpenShift Container Platform version if they are available. Use only ISO images for this procedure. RHCOS qcow2 images are not supported for this installation type.

    ISO file names resemble the following example:

    `rhcos-<version>-live.<architecture>.iso`

5.  Use the ISO to start the RHCOS installation. Use one of the following installation options:

    - Burn the ISO image to a disk and boot it directly.

    - Use ISO redirection by using a lights-out management (LOM) interface.

6.  Boot the RHCOS ISO image without specifying any options or interrupting the live boot sequence. Wait for the installer to boot into a shell prompt in the RHCOS live environment.

    > [!NOTE]
    > It is possible to interrupt the RHCOS installation boot process to add kernel arguments. However, for this ISO procedure you should use the `coreos-installer` command as outlined in the following steps, instead of adding kernel arguments.

7.  Run the `coreos-installer` command and specify the options that meet your installation requirements. At a minimum, you must specify the URL that points to the Ignition config file for the node type, and the device that you are installing to:

    ``` terminal
    $ sudo coreos-installer install --ignition-url=http://<HTTP_server>/<node_type>.ign <device> \
    --ignition-hash=sha512-<digest>
    ```

    - `<device>`: You must run the `coreos-installer` command by using `sudo`, because the `core` user does not have the required root privileges to perform the installation.

    - `<digest>`: The `--ignition-hash` option is required when the Ignition config file is obtained through an HTTP URL to validate the authenticity of the Ignition config file on the cluster node. `<digest>` is the Ignition config file SHA512 digest obtained in a preceding step.

      > [!NOTE]
      > If you want to provide your Ignition config files through an HTTPS server that uses TLS, you can add the internal certificate authority (CA) to the system trust store before running `coreos-installer`.

      The following example initializes a bootstrap node installation to the `/dev/sda` device. The Ignition config file for the bootstrap node is obtained from an HTTP web server with the IP address 192.168.1.2:

      ``` terminal
      $ sudo coreos-installer install --ignition-url=http://192.168.1.2:80/installation_directory/bootstrap.ign /dev/sda \
      --ignition-hash=sha512-a5a2d43879223273c9b60af66b44202a1d1248fc01cf156c46d4a79f552b6bad47bc8cc78ddf0116e80c59d2ea9e32ba53bc807afbca581aa059311def2c3e3b
      ```

8.  Monitor the progress of the RHCOS installation on the console of the machine.

    > [!IMPORTANT]
    > Be sure that the installation is successful on each node before commencing with the OpenShift Container Platform installation. Observing the installation process can also help to determine the cause of RHCOS installation issues that might arise.

9.  After RHCOS installs, you must reboot the system. During the system reboot, it applies the Ignition config file that you specified.

10. Check the console output to verify that Ignition ran.

    <div class="formalpara">

    <div class="title">

    Example command

    </div>

    ``` terminal
    Ignition: ran on 2022/03/14 14:48:33 UTC (this boot)
    Ignition: user-provided config was applied
    ```

    </div>

11. Continue to create the other machines for your cluster.

    > [!IMPORTANT]
    > You must create the bootstrap and control plane machines at this time. If the control plane machines are not made schedulable, also create at least two compute machines before you install OpenShift Container Platform.

    If the required network, DNS, and load balancer infrastructure are in place, the OpenShift Container Platform bootstrap process begins automatically after the RHCOS nodes have rebooted.

    > [!NOTE]
    > RHCOS nodes do not include a default password for the `core` user. You can access the nodes by running `ssh core@<node>.<cluster_name>.<base_domain>` as a user with access to the SSH private key that is paired to the public key that you specified in your `install_config.yaml` file. OpenShift Container Platform 4 cluster nodes running RHCOS are immutable and rely on Operators to apply cluster changes. Accessing cluster nodes by using SSH is not recommended. However, when investigating installation issues, if the OpenShift Container Platform API is not available, or the kubelet is not properly functioning on a target node, SSH access might be required for debugging or disaster recovery.

</div>

## Installing RHCOS by using PXE or iPXE booting

You can use PXE or iPXE booting to install RHCOS on the machines.

<div>

<div class="title">

Prerequisites

</div>

- You have created the Ignition config files for your cluster.

- You have configured suitable network, DNS and load balancing infrastructure.

- You have configured suitable PXE or iPXE infrastructure.

- You have an HTTP server that can be accessed from your computer, and from the machines that you create.

- You have reviewed the *Advanced RHCOS installation configuration* section for different ways to configure features, such as networking and disk partitioning.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Upload the bootstrap, control plane, and compute node Ignition config files that the installation program created to your HTTP server. Note the URLs of these files.

    > [!IMPORTANT]
    > You can add or change configuration settings in your Ignition configs before saving them to your HTTP server. If you plan to add more compute machines to your cluster after you finish installation, do not delete these files.

2.  From the installation host, validate that the Ignition config files are available on the URLs. The following example gets the Ignition config file for the bootstrap node:

    ``` terminal
    $ curl -k http://<HTTP_server>/bootstrap.ign
    ```

    - `<HTTP_server>`: Replace `bootstrap.ign` with `master.ign` or `worker.ign` in the command to validate that the Ignition config files for the control plane and compute nodes are also available.

      <div class="formalpara">

      <div class="title">

      Example output

      </div>

      ``` terminal
        % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                       Dload  Upload   Total   Spent    Left  Speed
        0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0{"ignition":{"version":"3.2.0"},"passwd":{"users":[{"name":"core","sshAuthorizedKeys":["ssh-rsa...
      ```

      </div>

3.  Although it is possible to obtain the RHCOS `kernel`, `initramfs` and `rootfs` files that are required for your preferred method of installing operating system instances from the [RHCOS image mirror](https://mirror.openshift.com/pub/openshift-v4/x86_64/dependencies/rhcos/) page, the recommended way to obtain the correct version of your RHCOS files are from the output of `openshift-install` command:

    ``` terminal
    $ openshift-install coreos print-stream-json | grep -Eo '"https.*(kernel-|initramfs.|rootfs.)\w+(\.img)?"'
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    "<url>/art/storage/releases/rhcos-4.20-aarch64/<release>/aarch64/rhcos-<release>-live-kernel-aarch64"
    "<url>/art/storage/releases/rhcos-4.20-aarch64/<release>/aarch64/rhcos-<release>-live-initramfs.aarch64.img"
    "<url>/art/storage/releases/rhcos-4.20-aarch64/<release>/aarch64/rhcos-<release>-live-rootfs.aarch64.img"
    "<url>/art/storage/releases/rhcos-4.20-ppc64le/49.84.202110081256-0/ppc64le/rhcos-<release>-live-kernel-ppc64le"
    "<url>/art/storage/releases/rhcos-4.20-ppc64le/<release>/ppc64le/rhcos-<release>-live-initramfs.ppc64le.img"
    "<url>/art/storage/releases/rhcos-4.20-ppc64le/<release>/ppc64le/rhcos-<release>-live-rootfs.ppc64le.img"
    "<url>/art/storage/releases/rhcos-4.20-s390x/<release>/s390x/rhcos-<release>-live-kernel-s390x"
    "<url>/art/storage/releases/rhcos-4.20-s390x/<release>/s390x/rhcos-<release>-live-initramfs.s390x.img"
    "<url>/art/storage/releases/rhcos-4.20-s390x/<release>/s390x/rhcos-<release>-live-rootfs.s390x.img"
    "<url>/art/storage/releases/rhcos-4.20/<release>/x86_64/rhcos-<release>-live-kernel-x86_64"
    "<url>/art/storage/releases/rhcos-4.20/<release>/x86_64/rhcos-<release>-live-initramfs.x86_64.img"
    "<url>/art/storage/releases/rhcos-4.20/<release>/x86_64/rhcos-<release>-live-rootfs.x86_64.img"
    ```

    </div>

    > [!IMPORTANT]
    > The RHCOS artifacts might not change with every release of OpenShift Container Platform. You must download images with the highest version that is less than or equal to the OpenShift Container Platform version that you install. Only use the appropriate `kernel`, `initramfs`, and `rootfs` artifacts described below for this procedure. RHCOS QCOW2 images are not supported for this installation type.

    The file names contain the OpenShift Container Platform version number. They resemble the following examples:

    - `kernel`: `rhcos-<version>-live-kernel-<architecture>`

    - `initramfs`: `rhcos-<version>-live-initramfs.<architecture>.img`

    - `rootfs`: `rhcos-<version>-live-rootfs.<architecture>.img`

4.  Upload the `rootfs`, `kernel`, and `initramfs` files to your HTTP server.

    > [!IMPORTANT]
    > If you plan to add more compute machines to your cluster after you finish installation, do not delete these files.

5.  Configure the network boot infrastructure so that the machines boot from their local disks after RHCOS is installed on them.

6.  Configure PXE or iPXE installation for the RHCOS images and begin the installation.

7.  Modify one of the following example menu entries for your environment and verify that the image and Ignition files are properly accessible:

    - For PXE (`x86_64`):

          DEFAULT pxeboot
          TIMEOUT 20
          PROMPT 0
          LABEL pxeboot
              KERNEL http://<HTTP_server>/rhcos-<version>-live-kernel-<architecture>
              APPEND initrd=http://<HTTP_server>/rhcos-<version>-live-initramfs.<architecture>.img coreos.live.rootfs_url=http://<HTTP_server>/rhcos-<version>-live-rootfs.<architecture>.img coreos.inst.install_dev=/dev/sda coreos.inst.ignition_url=http://<HTTP_server>/bootstrap.ign

      where:

      `kernel`
      Specify the location of the live `kernel` file that you uploaded to your HTTP server. The URL must be HTTP, TFTP, or FTP; HTTPS and NFS are not supported.

      `initrd=main`
      If you use multiple NICs, specify a single interface in the `ip` option. For example, to use DHCP on a NIC that is named `eno1`, set `ip=eno1:dhcp`. Specify the locations of the RHCOS files that you uploaded to your HTTP server. The `initrd` parameter value is the location of the `initramfs` file, the `coreos.live.rootfs_url` parameter value is the location of the `rootfs` file, and the `coreos.inst.ignition_url` parameter value is the location of the bootstrap Ignition config file. You can also add more kernel arguments to the `APPEND` line to configure networking or other boot options.

      > [!NOTE]
      > This configuration does not enable serial console access on machines with a graphical console. To configure a different console, add one or more `console=` arguments to the `APPEND` line. For example, add `console=tty0 console=ttyS0` to set the first PC serial port as the primary console and the graphical console as a secondary console. For more information, see [How does one set up a serial terminal and/or console in Red Hat Enterprise Linux?](https://access.redhat.com/articles/7212) and "Enabling the serial console for PXE and ISO installation" in the "Advanced RHCOS installation configuration" section.

    - For iPXE (`x86_64` + `aarch64` ):

          kernel http://<HTTP_server>/rhcos-<version>-live-kernel-<architecture> initrd=main coreos.live.rootfs_url=http://<HTTP_server>/rhcos-<version>-live-rootfs.<architecture>.img coreos.inst.install_dev=/dev/sda coreos.inst.ignition_url=http://<HTTP_server>/bootstrap.ign
          initrd --name main http://<HTTP_server>/rhcos-<version>-live-initramfs.<architecture>.img
          boot

      `kernel`
      Specify the locations of the RHCOS files that you uploaded to your HTTP server. The `kernel` parameter value is the location of the `kernel` file, the `initrd=main` argument is needed for booting on UEFI systems, the `coreos.live.rootfs_url` parameter value is the location of the `rootfs` file, and the `coreos.inst.ignition_url` parameter value is the location of the bootstrap Ignition config file. If you use multiple NICs, specify a single interface in the `ip` option. For example, to use DHCP on a NIC that is named `eno1`, set `ip=eno1:dhcp`.

      `initrd`
      Specify the location of the `initramfs` file that you uploaded to your HTTP server.

      > [!NOTE]
      > This configuration does not enable serial console access on machines with a graphical console. To configure a different console, add one or more `console=` arguments to the `kernel` line. For example, add `console=tty0 console=ttyS0` to set the first PC serial port as the primary console and the graphical console as a secondary console. For more information, see [How does one set up a serial terminal and/or console in Red Hat Enterprise Linux?](https://access.redhat.com/articles/7212) and "Enabling the serial console for PXE and ISO installation" in the "Advanced RHCOS installation configuration" section.

      > [!NOTE]
      > To network boot the CoreOS `kernel` on `aarch64` architecture, you need to use a version of iPXE build with the `IMAGE_GZIP` option enabled. See [`IMAGE_GZIP` option in iPXE](https://ipxe.org/buildcfg/image_gzip).

    - For PXE (with UEFI and Grub as second stage) on `aarch64`:

          menuentry 'Install CoreOS' {
              linux rhcos-<version>-live-kernel-<architecture>  coreos.live.rootfs_url=http://<HTTP_server>/rhcos-<version>-live-rootfs.<architecture>.img coreos.inst.install_dev=/dev/sda coreos.inst.ignition_url=http://<HTTP_server>/bootstrap.ign
              initrd rhcos-<version>-live-initramfs.<architecture>.img
          }

      where:

      `coreos.live.rootfs_url`
      Specify the locations of the RHCOS files that you uploaded to your HTTP/TFTP server.

      `kernel`
      The `kernel` parameter value is the location of the `kernel` file on your TFTP server. The `coreos.live.rootfs_url` parameter value is the location of the `rootfs` file, and the `coreos.inst.ignition_url` parameter value is the location of the bootstrap Ignition config file on your HTTP Server. If you use multiple NICs, specify a single interface in the `ip` option. For example, to use DHCP on a NIC that is named `eno1`, set `ip=eno1:dhcp`.

      `initrd rhcos`
      Specify the location of the `initramfs` file that you uploaded to your TFTP server.

8.  Monitor the progress of the RHCOS installation on the console of the machine.

    > [!IMPORTANT]
    > Be sure that the installation is successful on each node before commencing with the OpenShift Container Platform installation. Observing the installation process can also help to determine the cause of RHCOS installation issues that might arise.

9.  After RHCOS installs, the system reboots. During reboot, the system applies the Ignition config file that you specified.

10. Check the console output to verify that Ignition ran.

    <div class="formalpara">

    <div class="title">

    Example command

    </div>

    ``` terminal
    Ignition: ran on 2022/03/14 14:48:33 UTC (this boot)
    Ignition: user-provided config was applied
    ```

    </div>

11. Continue to create the machines for your cluster.

    > [!IMPORTANT]
    > You must create the bootstrap and control plane machines at this time. If the control plane machines are not made schedulable, also create at least two compute machines before you install the cluster.

    If the required network, DNS, and load balancer infrastructure are in place, the OpenShift Container Platform bootstrap process begins automatically after the RHCOS nodes have rebooted.

    > [!NOTE]
    > RHCOS nodes do not include a default password for the `core` user. You can access the nodes by running `ssh core@<node>.<cluster_name>.<base_domain>` as a user with access to the SSH private key that is paired to the public key that you specified in your `install_config.yaml` file. OpenShift Container Platform 4 cluster nodes running RHCOS are immutable and rely on Operators to apply cluster changes. Accessing cluster nodes by using SSH is not recommended. However, when investigating installation issues, if the OpenShift Container Platform API is not available, or the kubelet is not properly functioning on a target node, SSH access might be required for debugging or disaster recovery.

</div>

## Advanced RHCOS installation configuration

To apply advanced configurations unavailable through default installation methods, manually provision Red Hat Enterprise Linux CoreOS (RHCOS) nodes for OpenShift Container Platform.

This approach enables granular control over the node infrastructure to meet specific deployment requirements.

- Passing kernel arguments to the live installer

- Running `coreos-installer` manually from the live system

- Customizing a live ISO or PXE boot image

The advanced configuration topics for manual Red Hat Enterprise Linux CoreOS (RHCOS) installations detailed in this section relate to disk partitioning, networking, and configuring Ignition in different ways.

### Using advanced networking options for PXE and ISO installations

Networking for OpenShift Container Platform nodes uses DHCP by default to gather all necessary configuration settings. You can set up static IP addresses or configure special settings.

To set up static IP addresses or configure special settings, such as bonding, you can do one of the following:

- Pass special kernel parameters when you boot the live installer.

- Use a machine config to copy networking files to the installed system.

- Configure networking from a live installer shell prompt, then copy those settings to the installed system so that they take effect when the installed system first boots.

To configure a PXE or iPXE installation, use one of the following options:

- See the "coreos-installer and boot options for ISO and PXE installations" tables.

- Use a machine config to copy networking files to the installed system.

To configure an ISO installation, use the following procedure.

<div>

<div class="title">

Procedure

</div>

1.  Boot the ISO installer.

2.  From the live system shell prompt, configure networking for the live system by using available RHEL tools, such as `nmcli` or `nmtui`.

3.  Run the `coreos-installer` command to install the system, adding the `--copy-network` option to copy networking configuration. For example:

    ``` terminal
    $ sudo coreos-installer install --copy-network \
         --ignition-url=http://host/worker.ign /dev/disk/by-id/scsi-<serial_number>
    ```

    > [!IMPORTANT]
    > The `--copy-network` option only copies networking configuration found under `/etc/NetworkManager/system-connections`. In particular, it does not copy the system hostname.

4.  Reboot into the installed system.

</div>

### Disk partitioning

Disk partitions are created on OpenShift Container Platform cluster nodes during the Red Hat Enterprise Linux CoreOS (RHCOS) installation. Each RHCOS node of a particular architecture uses the same partition layout, unless you override the default partitioning configuration.

During the RHCOS installation, the size of the root file system is increased to use any remaining available space on the target device.

> [!IMPORTANT]
> The use of a custom partition scheme on your node might result in OpenShift Container Platform not monitoring or alerting on some node partitions. For more information on monitoring host file systems when using custom partitioning, see [Understanding OpenShift File System Monitoring (eviction conditions)](https://access.redhat.com/articles/4766521).

OpenShift Container Platform monitors the following two filesystem identifiers:

- `nodefs`, which is the filesystem that contains `/var/lib/kubelet`.

- `imagefs`, which is the filesystem that contains `/var/lib/containers`.

For the default partition scheme, `nodefs` and `imagefs` monitor the same root filesystem, `/`.

To override the default partitioning when installing RHCOS on an OpenShift Container Platform cluster node, you must create separate partitions. Consider a situation where you want to add a separate storage partition for your containers and container images. For example, by mounting `/var/lib/containers` in a separate partition, the kubelet separately monitors `/var/lib/containers` as the `imagefs` directory and the root file system as the `nodefs` directory.

> [!IMPORTANT]
> If you have resized your disk size to host a larger file system, consider creating a separate `/var/lib/containers` partition. Consider resizing a disk that has an `xfs` format to reduce CPU time issues caused by a high number of allocation groups.

OpenShift Container Platform supports the addition of a single partition to attach storage to either the `/var` directory or a subdirectory of `/var`. For example:

- `/var/lib/containers`: Holds container-related content that can grow as more images and containers are added to a system.

- `/var/lib/etcd`: Holds data that you might want to keep separate for purposes such as performance optimization of etcd storage.

- `/var`: Holds data that you might want to keep separate for purposes such as auditing.

  > [!IMPORTANT]
  > For disk sizes larger than 100GB, and especially larger than 1TB, create a separate `/var` partition.

Storing the contents of a `/var` directory separately makes it easier to grow storage for those areas as needed and reinstall OpenShift Container Platform at a later date to keep that data intact. This method eliminates the need to re-pull containers or copy large log files during system updates.

The use of a separate partition for the `/var` directory or a subdirectory of `/var` also prevents data growth in the partitioned directory from filling up the root file system.

The following procedure sets up a separate `/var` partition by adding a machine config manifest that is wrapped into the Ignition config file for a node type during the preparation phase of an installation.

<div>

<div class="title">

Procedure

</div>

1.  On your installation host, change to the directory that contains the OpenShift Container Platform installation program and generate the Kubernetes manifests for the cluster:

    ``` terminal
    $ openshift-install create manifests --dir <installation_directory>
    ```

2.  Create a Butane config that configures the additional partition. For example, name the file `$HOME/clusterconfig/98-var-partition.bu`, change the disk device name to the name of the storage device on the `worker` systems, and set the storage size as appropriate. This example places the `/var` directory on a separate partition:

    ``` yaml
    variant: openshift
    version: 4.17.0
    metadata:
      labels:
        machineconfiguration.openshift.io/role: worker
      name: 98-var-partition
    storage:
      disks:
      - device: /dev/disk/by-id/<device_name>
        partitions:
        - label: var
          start_mib: <partition_start_offset>
          size_mib: <partition_size>
          number: 5
      filesystems:
        - device: /dev/disk/by-partlabel/var
          path: /var
          format: xfs
          mount_options: [defaults, prjquota]
          with_mount_unit: true
    ```

    where:

    `<device_name>`
    Specifies the storage device name of the disk that you want to partition.

    `<partition_start_offset>`
    Specifies the minimum offset value for the boot disk. For best performance, specify a minimum offset value of 25000 mebibytes. The root file system is automatically resized to fill all available space up to the specified offset. If no offset value is specified, or if the specified value is smaller than the recommended minimum, the resulting root file system will be too small, and future reinstalls of RHCOS might overwrite the beginning of the data partition.

    `<partition_size>`
    Specifies the size of the data partition in mebibytes.

    `mount_options`
    The `prjquota` mount option must be enabled for filesystems used for container storage.

    > [!NOTE]
    > When creating a separate `/var` partition, you cannot use different instance types for compute nodes, if the different instance types do not have the same device name.

3.  Create a manifest from the Butane config and save it to the `clusterconfig/openshift` directory. For example, run the following command:

    ``` terminal
    $ butane $HOME/clusterconfig/98-var-partition.bu -o $HOME/clusterconfig/openshift/98-var-partition.yaml
    ```

4.  Create the Ignition config files by running the following command:

    ``` terminal
    $ openshift-install create ignition-configs --dir <installation_directory>
    ```

    where:

    `<installation_directory>`
    Specifies the name of the installation directory.

    Ignition config files are created for the bootstrap, control plane, and compute nodes in the installation directory:

        .
        ├── auth
        │   ├── kubeadmin-password
        │   └── kubeconfig
        ├── bootstrap.ign
        ├── master.ign
        ├── metadata.json
        └── worker.ign

    The files in the `<installation_directory>/manifest` and `<installation_directory>/openshift` directories are wrapped into the Ignition config files, including the file that contains the `98-var-partition` custom `MachineConfig` object.

5.  Optional: You can apply the custom disk partitioning by referencing the Ignition config files during the RHCOS installations.

</div>

### Examples of retaining existing partitions

For an ISO installation, you can add options to the `coreos-installer` command that causes the installation program to maintain one or more existing partitions. For a PXE installation, you can add `coreos.inst.*` options to the `APPEND` parameter to preserve partitions.

Saved partitions might be data partitions from an existing OpenShift Container Platform system. You can identify the disk partitions you want to keep either by partition label or by number.

> [!NOTE]
> If you save existing partitions, and those partitions do not leave enough space for RHCOS, the installation fails without damaging the saved partitions.

The following examples preserve any existing partition during an ISO installation in which the partition label begins with `data` (`data*`):

``` terminal
# coreos-installer install --ignition-url http://10.0.2.2:8080/user.ign \
--save-partlabel 'data*' \
/dev/disk/by-id/scsi-<serial_number>
```

The following example runs the `coreos-installer` in a way that preserves the sixth (6) partition on the disk:

``` terminal
# coreos-installer install --ignition-url http://10.0.2.2:8080/user.ign \
--save-partindex 6 /dev/disk/by-id/scsi-<serial_number>
```

The following example preserves partitions 5 and higher:

``` terminal
# coreos-installer install --ignition-url http://10.0.2.2:8080/user.ign \
--save-partindex 5- /dev/disk/by-id/scsi-<serial_number>
```

In the earlier examples where partition saving is used, `coreos-installer` recreates the partition immediately.

The following examples preserve existing partitions during a PXE installation. The following `APPEND` option preserves any partition in which the partition label begins with 'data' ('data\*').

``` terminal
coreos.inst.save_partlabel=data*
```

The following `APPEND` option preserves partitions 5 and higher:

``` terminal
coreos.inst.save_partindex=5-
```

The following `APPEND` option preserves partition 6:

``` terminal
coreos.inst.save_partindex=6
```

### Identifying Ignition configs

When doing an RHCOS manual installation, there are two types of Ignition configs that you can provide: Permanent install Ignition config and live install Ignition config.

When manually installing RHCOS, you can provide the following two types of Ignition configs:

- **Permanent install Ignition config**: Every manual RHCOS installation needs to pass one of the Ignition config files generated by `openshift-installer`, such as `bootstrap.ign`, `master.ign` and `worker.ign`, to carry out the installation.

> [!IMPORTANT]
> Do not modify these Ignition config files directly. You can update the manifest files that are wrapped into the Ignition config files, as outlined in examples in the preceding sections.

For PXE installations, you can pass the Ignition configs on the `APPEND` line using the `coreos.inst.ignition_url=` option. For ISO installations, after the ISO boots to the shell prompt, you must identify the Ignition config on the `coreos-installer` command line with the `--ignition-url=` option. In both cases, only HTTP and HTTPS protocols are supported.

- **Live install Ignition config**: This type can be created by using the `coreos-installer` `customize` subcommand of `coreos-installer` and its various options. With this method, the Ignition config passes to the live install medium, runs immediately upon booting, and performs setup tasks before or after the RHCOS system installs to disk. This method must be only used for performing tasks that must be done once and not applied again later, such as with advanced partitioning that cannot be done using a machine config.

For PXE or ISO boots, you can create the Ignition config and `APPEND` the `ignition.config.url=` option to identify the location of the Ignition config. You also need to append `ignition.firstboot ignition.platform.id=metal` else the `ignition.config.url` option is ignored.

<div>

<div class="title">

Additional resources

</div>

- [Getting started with nmcli](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8/html-single/configuring_and_managing_networking/index#getting-started-with-nmcli_configuring-and-managing-networking)

- [Getting started with nmtui](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8/html-single/configuring_and_managing_networking/index#getting-started-with-nmtui_configuring-and-managing-networking)

</div>

### Default console configuration

Red Hat Enterprise Linux CoreOS (RHCOS) nodes installed from an OpenShift Container Platform 4.17 boot image use a default console that is meant to accomodate most virtualized and bare metal setups. Different cloud and virtualization platforms may use different default settings depending on the chosen architecture.

Bare-metal installations use the kernel default settings which typically means the graphical console is the primary console and the serial console is disabled.

The default consoles may not match your specific hardware configuration or you might have specific needs that require you to adjust the default console. For example:

- You want to access the emergency shell on the console for debugging purposes.

- Your cloud platform does not provide interactive access to the graphical console, but provides a serial console.

- You want to enable multiple consoles.

Console configuration is inherited from the boot image. This means that new nodes in existing clusters are unaffected by changes to the default console.

You can configure the console for bare metal installations in the following ways:

- Using `coreos-installer` manually on the command line.

- Using the `coreos-installer iso customize` or `coreos-installer pxe customize` subcommands with the `--dest-console` option to create a custom image that automates the process.

> [!NOTE]
> For advanced customization, perform console configuration using the `coreos-installer iso` or `coreos-installer pxe` subcommands, and not kernel arguments.

### Enabling the serial console for PXE and ISO installations

By default, the Red Hat Enterprise Linux CoreOS (RHCOS) serial console is disabled and all output is written to the graphical console. You can enable the serial console for PXE and ISO installations.

<div>

<div class="title">

Procedure

</div>

1.  Boot the ISO installer.

2.  Run the `coreos-installer` command to install the system, adding the `--console` option once to specify the graphical console, and a second time to specify the serial console:

    ``` terminal
    $ coreos-installer install \
    --console=tty0 \
    --console=ttyS0,<options> \
    --ignition-url=http://host/worker.ign /dev/disk/by-id/scsi-<serial_number>
    ```

    where:

    `--console=tty0`
    The desired secondary console. In this case, the graphical console. Omitting this option will disable the graphical console.

    `--console=ttyS0`
    The desired primary console. In this case, the serial console. The `options` field defines the baud rate and other settings. A common value for this field is `115200n8`. If no options are provided, the default kernel value of `9600n8` is used. For more information on the format of this option, see [Linux kernel serial console](https://www.kernel.org/doc/html/latest/admin-guide/serial-console.html) documentation.

3.  Reboot into the installed system.

    > [!NOTE]
    > A similar outcome can be obtained by using the `coreos-installer install --append-karg` option, and specifying the console with `console=`. However, this will only set the console for the kernel and not the bootloader.

    To configure a PXE installation, make sure the `coreos.inst.install_dev` kernel command-line option is omitted, and use the shell prompt to run `coreos-installer` manually using the above ISO installation procedure.

</div>

### Customizing a live RHCOS ISO or PXE install

You can use the live ISO image or PXE environment to install RHCOS by injecting an Ignition config file directly into the image. This creates a customized image that you can use to provision your system.

For an ISO image, the mechanism to do this is the `coreos-installer iso customize` subcommand, which modifies the `.iso` file with your configuration. Similarly, the mechanism for a PXE environment is the `coreos-installer pxe customize` subcommand, which creates a new `initramfs` file that includes your customizations.

The `customize` subcommand is a general-purpose tool that can embed other types of customizations as well. The following tasks are examples of some of the more common customizations:

- Inject custom CA certificates for when corporate security policy requires their use.

- Configure network settings without the need for kernel arguments.

- Embed arbitrary pre-install and post-install scripts or binaries.

### Customizing a live RHCOS ISO image

You can customize a live RHCOS ISO image directly with the `coreos-installer iso customize` subcommand. When you boot the ISO image, the customizations are applied automatically. You can use this feature to configure the ISO image to automatically install RHCOS.

<div>

<div class="title">

Procedure

</div>

1.  Download the `coreos-installer` binary from the [`coreos-installer` image mirror](https://mirror.openshift.com/pub/openshift-v4/clients/coreos-installer/latest/) page.

2.  Retrieve the RHCOS ISO image from the [RHCOS image mirror](https://mirror.openshift.com/pub/openshift-v4/dependencies/rhcos/latest/) page and the Ignition config file, and then run the following command to inject the Ignition config directly into the ISO image:

    ``` terminal
    $ coreos-installer iso customize rhcos-<version>-live.x86_64.iso \
        --dest-ignition bootstrap.ign \
        --dest-device /dev/disk/by-id/scsi-<serial_number>
    ```

    where:

    `--dest-ignition`
    Specifies the Ignition config file that is generated from the `openshift-installer` installation program.

    `--dest-device`
    When you specify this option, the ISO image automatically runs an installation. Otherwise, the image remains configured for installation, but does not install automatically unless you specify the `coreos.inst.install_dev` kernel argument.

3.  Optional: To remove the ISO image customizations and return the image to its pristine state, run:

    ``` terminal
    $ coreos-installer iso reset rhcos-<version>-live.x86_64.iso
    ```

    You can now re-customize the live ISO image or use it in its pristine state.

    Applying your customizations affects every subsequent boot of RHCOS.

</div>

### Modifying a live install ISO image to enable the serial console

To redirect system output from the default graphical interface, enable the serial console by modifying the live install ISO image. This configuration ensures access to boot messages on OpenShift Container Platform 4.12 and later clusters.

<div>

<div class="title">

Procedure

</div>

1.  Download the `coreos-installer` binary from the [`coreos-installer` image mirror](https://mirror.openshift.com/pub/openshift-v4/clients/coreos-installer/latest/) page.

2.  Retrieve the RHCOS ISO image from the [RHCOS image mirror](https://mirror.openshift.com/pub/openshift-v4/dependencies/rhcos/latest/) page and run the following command to customize the ISO image to enable the serial console to receive output:

    ``` terminal
    $ coreos-installer iso customize rhcos-<version>-live.x86_64.iso \
      --dest-ignition <path> \
      --dest-console tty0 \
      --dest-console ttyS0,<options> \
      --dest-device /dev/disk/by-id/scsi-<serial_number>
    ```

    where:

    `<path>`
    The location of the Ignition config to install.

    `tty0`
    The desired secondary console. In this case, the graphical console. Omitting this option will disable the graphical console.

    `<options>`
    The desired primary console. In this case, the serial console. The `options` field defines the baud rate and other settings. A common value for this field is `115200n8`. If no options are provided, the default kernel value of `9600n8` is used. For more information on the format of this option, see the [Linux kernel serial console](https://www.kernel.org/doc/html/latest/admin-guide/serial-console.html) documentation.

    `<serial_number>`
    The specified disk to install to. If you omit this option, the ISO image automatically runs the installation program which will fail unless you also specify the `coreos.inst.install_dev` kernel argument.

    > [!NOTE]
    > The `--dest-console` option affects the installed system and not the live ISO system. To modify the console for a live ISO system, use the `--live-karg-append` option and specify the console with `console=`.

    Your customizations are applied and affect every subsequent boot of the ISO image.

3.  Optional: To remove the ISO image customizations and return the image to its original state, run the following command:

    ``` terminal
    $ coreos-installer iso reset rhcos-<version>-live.x86_64.iso
    ```

    You can now recustomize the live ISO image or use it in its original state.

</div>

### Modifying a live install ISO image to use a custom certificate authority

You can provide certificate authority (CA) certificates to Ignition with the `--ignition-ca` flag of the `customize` subcommand. You can use the CA certificates during both the installation boot and when provisioning the installed system.

> [!NOTE]
> Custom CA certificates affect how Ignition fetches remote resources, but they do not affect the certificates installed onto the system.

<div>

<div class="title">

Procedure

</div>

1.  Download the `coreos-installer` binary from the [`coreos-installer` image mirror](https://mirror.openshift.com/pub/openshift-v4/clients/coreos-installer/latest/) page.

2.  Retrieve the RHCOS ISO image from the [RHCOS image mirror](https://mirror.openshift.com/pub/openshift-v4/dependencies/rhcos/latest/) page, and run the following command to customize the ISO image for use with a custom CA:

    ``` terminal
    $ coreos-installer iso customize rhcos-<version>-live.x86_64.iso --ignition-ca cert.pem
    ```

    > [!IMPORTANT]
    > The `coreos.inst.ignition_url` kernel parameter does not work with the `--ignition-ca` flag. You must use the `--dest-ignition` flag to create a customized image for each cluster.

    Applying your custom CA certificate affects every subsequent boot of RHCOS.

</div>

### Modifying a live install ISO image with customized network settings

You can embed a NetworkManager keyfile into the live ISO image and pass it through to the installed system with the `--network-keyfile` flag of the `customize` subcommand.

> [!WARNING]
> When creating a connection profile, you must use a `.nmconnection` filename extension in the filename of the connection profile. If you do not use a `.nmconnection` filename extension, the cluster will apply the connection profile to the live environment, but it will not apply the configuration when the cluster first boots up the nodes, resulting in a setup that does not work.

<div>

<div class="title">

Procedure

</div>

1.  Download the `coreos-installer` binary from the [`coreos-installer` image mirror](https://mirror.openshift.com/pub/openshift-v4/clients/coreos-installer/latest/) page.

2.  Create a connection profile for a bonded interface. For example, create the `bond0.nmconnection` file in your local directory with the following content:

    ``` terminal
    /[connection]
    id=bond0
    type=bond
    interface-name=bond0
    multi-connect=1

    /[bond]
    miimon=100
    mode=active-backup

    /[ipv4]
    method=auto

    /[ipv6]
    method=auto
    ```

3.  Create a connection profile for a secondary interface to add to the bond. For example, create the `bond0-proxy-em1.nmconnection` file in your local directory with the following content:

    ``` terminal
    /[connection]
    id=em1
    type=ethernet
    interface-name=em1
    master=bond0
    multi-connect=1
    slave-type=bond
    ```

4.  Create a connection profile for a secondary interface to add to the bond. For example, create the `bond0-proxy-em2.nmconnection` file in your local directory with the following content:

    ``` terminal
    /[connection]
    id=em2
    type=ethernet
    interface-name=em2
    master=bond0
    multi-connect=1
    slave-type=bond
    ```

5.  Retrieve the RHCOS ISO image from the [RHCOS image mirror](https://mirror.openshift.com/pub/openshift-v4/dependencies/rhcos/latest/) page and run the following command to customize the ISO image with your configured networking:

    ``` terminal
    $ coreos-installer iso customize rhcos-<version>-live.x86_64.iso \
        --network-keyfile bond0.nmconnection \
        --network-keyfile bond0-proxy-em1.nmconnection \
        --network-keyfile bond0-proxy-em2.nmconnection
    ```

    Network settings are applied to the live system and are carried over to the destination system.

</div>

### Customizing a live install ISO image for an iSCSI boot device

You can set the iSCSI target and initiator values for automatic mounting, booting and configuration by using a customized version of the live RHCOS image.

<div>

<div class="title">

Prerequisites

</div>

1.  You have an iSCSI target you want to install RHCOS on.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Download the `coreos-installer` binary from the [`coreos-installer` image mirror](https://mirror.openshift.com/pub/openshift-v4/clients/coreos-installer/latest/) page.

2.  Retrieve the RHCOS ISO image from the [RHCOS image mirror](https://mirror.openshift.com/pub/openshift-v4/dependencies/rhcos/latest/) page and run the following command to customize the ISO image with the following information:

    ``` text
    $ coreos-installer iso customize \
        --pre-install mount-iscsi.sh \
        --post-install unmount-iscsi.sh \
        --dest-device /dev/disk/by-path/<IP_address>:<port>-iscsi-<target_iqn>-lun-<lun> \
        --dest-ignition config.ign \
        --dest-karg-append rd.iscsi.initiator=<initiator_iqn> \
        --dest-karg-append netroot=<target_iqn> \
        -o custom.iso rhcos-<version>-live.x86_64.iso
    ```

    where:

    `mount-iscsi.sh`
    Specifies the script that gets run before installation. It should contain the `iscsiadm` commands for mounting the iSCSI target and any commands enabling multipathing.

    `unmount-iscsi.sh`
    Specifies the script that gets run after installation. It should contain the command `iscsiadm --mode node --logout=all`.

    `<target_iqn>`
    Specifies the location of the destination system. You must provide the IP address of the target portal, the associated port number, the target iSCSI node in IQN format, and the iSCSI logical unit number (LUN).

    `config.ign`
    Specifies the Ignition configuration for the destination system. `<initiator_iqn>`::Specifies the iSCSI initiator, or client, name in IQN format. The initiator forms a session to connect to the iSCSI target. `<target_iqn>`::Specifies the iSCSI target, or server, name in IQN format.

    For more information about the iSCSI options supported by `dracut`, see the `dracut.cmdline` manual page.

</div>

<div>

<div class="title">

Additional resources

</div>

- [`dracut.cmdline` manual page](https://www.man7.org/linux/man-pages/man7/dracut.cmdline.7.html)

</div>

### Customizing a live install ISO image for an iSCSI boot device with iBFT

You can set the iSCSI target and initiator values for automatic mounting, booting and configuration using a customized version of the live RHCOS image.

<div>

<div class="title">

Prerequisites

</div>

1.  You have an iSCSI target you want to install RHCOS on.

2.  Optional: You have multipathed your iSCSI target.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Download the `coreos-installer` binary from the [`coreos-installer` image mirror](https://mirror.openshift.com/pub/openshift-v4/clients/coreos-installer/latest/) page.

2.  Retrieve the RHCOS ISO image from the [RHCOS image mirror](https://mirror.openshift.com/pub/openshift-v4/dependencies/rhcos/latest/) page and run the following command to customize the ISO image with the following information:

    ``` text
    $ coreos-installer iso customize \
        --pre-install mount-iscsi.sh \
        --post-install unmount-iscsi.sh \
        --dest-device /dev/mapper/mpatha \
        --dest-ignition config.ign \
        --dest-karg-append rd.iscsi.firmware=1 \
        --dest-karg-append rd.multipath=default \
        -o custom.iso rhcos-<version>-live.x86_64.iso
    ```

    where:

    `mount-iscsi.sh`
    Specifies the script that gets run before installation. It should contain the `iscsiadm` commands for mounting the iSCSI target and any commands enabling multipathing.

    `unmount-iscsi.sh`
    Specifies the script that gets run after installation. It should contain the command `iscsiadm --mode node --logout=all`.

    `/dev/mapper/mpatha`
    Specifies the path to the device. If you are using multipath, the multipath device, `/dev/mapper/mpatha`, If there are multiple multipath devices connected, or to be explicit, you can use the World Wide Name (WWN) symlink available in `/dev/disk/by-path`.

    `config.ign`
    Specifies the Ignition configuration for the destination system. `rd.iscsi.firmware=1`::Specifies the iSCSI parameter is read from the BIOS firmware.

    `rd.multipath=default`
    Specifies if you want to enable multipathing. Optional parameter.

    For more information about see the `dracut.cmdline` manual page.

</div>

<div>

<div class="title">

Additional resources

</div>

- [`dracut.cmdline` manual page](https://www.man7.org/linux/man-pages/man7/dracut.cmdline.7.html)

</div>

### Customizing a live RHCOS PXE environment

You can customize a live RHCOS PXE environment directly with the `coreos-installer pxe customize` subcommand. When you boot the PXE environment, the customizations are applied automatically. You can use this feature to configure the PXE environment to automatically install RHCOS.

<div>

<div class="title">

Procedure

</div>

1.  Download the `coreos-installer` binary from the [`coreos-installer` image mirror](https://mirror.openshift.com/pub/openshift-v4/clients/coreos-installer/latest/) page.

2.  Retrieve the RHCOS `kernel`, `initramfs`, and `rootfs` files from the [RHCOS image mirror](https://mirror.openshift.com/pub/openshift-v4/dependencies/rhcos/latest/) page and the Ignition config file, and then run the following command to create a new `initramfs` file that contains the customizations from your Ignition config:

    ``` terminal
    $ coreos-installer pxe customize rhcos-<version>-live-initramfs.x86_64.img \
        --dest-ignition bootstrap.ign \
        --dest-device /dev/disk/by-id/scsi-<serial_number> \
        -o rhcos-<version>-custom-initramfs.x86_64.img
    ```

    where:

    `--dest-ignition`
    Specifies the Ignition config file that is generated from `openshift-installer`.

    `<serial_number>`
    When you specify this option, the PXE environment automatically runs an install. Otherwise, the image remains configured for installation, but does not do so automatically unless you specify the `coreos.inst.install_dev` kernel argument.

    `<version>`
    Use the customized `initramfs` file in your PXE configuration. Add the `ignition.firstboot` and `ignition.platform.id=metal` kernel arguments if they are not already present.

    Applying your customizations affects every subsequent boot of RHCOS.

</div>

### Modifying a live install PXE environment to enable the serial console

To redirect system output from the default graphical interface, enable the serial console by modifying the live install PXE environment. This configuration ensures access to boot messages on OpenShift Container Platform 4.12 and later clusters.

<div>

<div class="title">

Procedure

</div>

1.  Download the `coreos-installer` binary from the [`coreos-installer` image mirror](https://mirror.openshift.com/pub/openshift-v4/clients/coreos-installer/latest/) page.

2.  Retrieve the RHCOS `kernel`, `initramfs`, and `rootfs` files from the [RHCOS image mirror](https://mirror.openshift.com/pub/openshift-v4/dependencies/rhcos/latest/) page and the Ignition config file, and then run the following command to create a new customized `initramfs` file that enables the serial console to receive output:

    ``` terminal
    $ coreos-installer pxe customize rhcos-<version>-live-initramfs.x86_64.img \
      --dest-ignition <path> \
      --dest-console tty0 \
      --dest-console ttyS0,<options> \
      --dest-device /dev/disk/by-id/scsi-<serial_number> \
      -o rhcos-<version>-custom-initramfs.x86_64.img
    ```

    where:

    `<path>`
    The location of the Ignition config to install.

    `tty0`
    The desired secondary console. In this case, the graphical console. Omitting this option will disable the graphical console.

    `<options>`
    The desired primary console. In this case, the serial console. The `options` field defines the baud rate and other settings. A common value for this field is `115200n8`. If no options are provided, the default kernel value of `9600n8` is used. For more information on the format of this option, see the [Linux kernel serial console](https://www.kernel.org/doc/html/latest/admin-guide/serial-console.html) documentation.

    `<serial_number>`
    The specified disk to install to. If you omit this option, the PXE environment automatically runs the installation program which will fail unless you also specify the `coreos.inst.install_dev` kernel argument.

    `<version>`
    Use the customized `initramfs` file in your PXE configuration. Add the `ignition.firstboot` and `ignition.platform.id=metal` kernel arguments if they are not already present.

    Your customizations are applied and affect every subsequent boot of the PXE environment.

</div>

### Modifying a live install PXE environment to use a custom certificate authority

You can provide certificate authority (CA) certificates to Ignition with the `--ignition-ca` flag of the `customize` subcommand. You can use the CA certificates during both the installation boot and when provisioning the installed system.

> [!NOTE]
> Custom CA certificates affect how Ignition fetches remote resources, but they do not affect the certificates installed onto the system.

<div>

<div class="title">

Procedure

</div>

1.  Download the `coreos-installer` binary from the [`coreos-installer` image mirror](https://mirror.openshift.com/pub/openshift-v4/clients/coreos-installer/latest/) page.

2.  Retrieve the RHCOS `kernel`, `initramfs`, and `rootfs` files from the [RHCOS image mirror](https://mirror.openshift.com/pub/openshift-v4/dependencies/rhcos/latest/) page, and run the following command to create a new customized `initramfs` file for use with a custom CA:

    ``` terminal
    $ coreos-installer pxe customize rhcos-<version>-live-initramfs.x86_64.img \
        --ignition-ca cert.pem \
        -o rhcos-<version>-custom-initramfs.x86_64.img
    ```

3.  Use the customized `initramfs` file in your PXE configuration. Add the `ignition.firstboot` and `ignition.platform.id=metal` kernel arguments if they are not already present.

    > [!IMPORTANT]
    > The `coreos.inst.ignition_url` kernel parameter does not work with the `--ignition-ca` flag. You must use the `--dest-ignition` flag to create a customized image for each cluster.

    Applying your custom CA certificate affects every subsequent boot of RHCOS.

</div>

### Modifying a live install PXE environment with customized network settings

You can embed a NetworkManager keyfile into the live PXE environment and pass it through to the installed system with the `--network-keyfile` flag of the `customize` subcommand.

> [!WARNING]
> When creating a connection profile, you must use a `.nmconnection` filename extension in the filename of the connection profile. If you do not use a `.nmconnection` filename extension, the cluster will apply the connection profile to the live environment, but it will not apply the configuration when the cluster first boots up the nodes, resulting in a setup that does not work.

<div>

<div class="title">

Procedure

</div>

1.  Download the `coreos-installer` binary from the [`coreos-installer` image mirror](https://mirror.openshift.com/pub/openshift-v4/clients/coreos-installer/latest/) page.

2.  Create a connection profile for a bonded interface. For example, create the `bond0.nmconnection` file in your local directory with the following content:

    ``` terminal
    /[connection]
    id=bond0
    type=bond
    interface-name=bond0
    multi-connect=1

    /[bond]
    miimon=100
    mode=active-backup

    /[ipv4]
    method=auto

    /[ipv6]
    method=auto
    ```

3.  Create a connection profile for a secondary interface to add to the bond. For example, create the `bond0-proxy-em1.nmconnection` file in your local directory with the following content:

    ``` terminal
    /[connection]
    id=em1
    type=ethernet
    interface-name=em1
    master=bond0
    multi-connect=1
    slave-type=bond
    ```

4.  Create a connection profile for a secondary interface to add to the bond. For example, create the `bond0-proxy-em2.nmconnection` file in your local directory with the following content:

    ``` terminal
    /[connection]
    id=em2
    type=ethernet
    interface-name=em2
    master=bond0
    multi-connect=1
    slave-type=bond
    ```

5.  Retrieve the RHCOS `kernel`, `initramfs`, and `rootfs` files from the [RHCOS image mirror](https://mirror.openshift.com/pub/openshift-v4/dependencies/rhcos/latest/) page and run the following command to create a new customized `initramfs` file that contains your configured networking:

    ``` terminal
    $ coreos-installer pxe customize rhcos-<version>-live-initramfs.x86_64.img \
        --network-keyfile bond0.nmconnection \
        --network-keyfile bond0-proxy-em1.nmconnection \
        --network-keyfile bond0-proxy-em2.nmconnection \
        -o rhcos-<version>-custom-initramfs.x86_64.img
    ```

6.  Use the customized `initramfs` file in your PXE configuration. Add the `ignition.firstboot` and `ignition.platform.id=metal` kernel arguments if they are not already present.

    Network settings are applied to the live system and are carried over to the destination system.

</div>

### Customizing a live install PXE environment for an iSCSI boot device

You can set the iSCSI target and initiator values for automatic mounting, booting and configuration by using a customized version of the live RHCOS image.

<div>

<div class="title">

Prerequisites

</div>

1.  You have an iSCSI target you want to install RHCOS on.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Download the `coreos-installer` binary from the [`coreos-installer` image mirror](https://mirror.openshift.com/pub/openshift-v4/clients/coreos-installer/latest/) page.

2.  Retrieve the RHCOS `kernel`, `initramfs`, and `rootfs` files from the [RHCOS image mirror](https://mirror.openshift.com/pub/openshift-v4/dependencies/rhcos/latest/) page and run the following command to create a new customized `initramfs` file with the following information:

    ``` text
    $ coreos-installer pxe customize \
        --pre-install mount-iscsi.sh \
        --post-install unmount-iscsi.sh \
        --dest-device /dev/disk/by-path/<IP_address>:<port>-iscsi-<target_iqn>-lun-<lun> \
        --dest-ignition config.ign \
        --dest-karg-append rd.iscsi.initiator=<initiator_iqn> \
        --dest-karg-append netroot=<target_iqn> \
        -o custom.img rhcos-<version>-live-initramfs.x86_64.img
    ```

    where:

    `mount-iscsi.sh`
    Specifies the script that gets run before installation. It should contain the `iscsiadm` commands for mounting the iSCSI target and any commands enabling multipathing.

    `unmount-iscsi.sh`
    Specifies the script that gets run after installation. It should contain the command `iscsiadm --mode node --logout=all`.

    `<target_iqn>`
    Specifies the location of the destination system. You must provide the IP address of the target portal, the associated port number, the target iSCSI node in IQN format, and the iSCSI logical unit number (LUN).

    `config.ign`
    Specifies the Ignition configuration for the destination system.

    `<initiator_iqn>`
    Specifies the iSCSI initiator, or client, name in IQN format. The initiator forms a session to connect to the iSCSI target.

    `<target_iqn>`
    Specifies the iSCSI target, or server, name in IQN format.

    For more information about the iSCSI options supported by `dracut`, see the `dracut.cmdline` manual page.

</div>

### Customizing a live install PXE environment for an iSCSI boot device with iBFT

You can set the iSCSI target and initiator values for automatic mounting, booting and configuration using a customized version of the live RHCOS image.

<div>

<div class="title">

Prerequisites

</div>

1.  You have an iSCSI target you want to install RHCOS on.

2.  Optional: You have multipathed your iSCSI target.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Download the `coreos-installer` binary from the [`coreos-installer` image mirror](https://mirror.openshift.com/pub/openshift-v4/clients/coreos-installer/latest/) page.

2.  Retrieve the RHCOS `kernel`, `initramfs`, and `rootfs` files from the [RHCOS image mirror](https://mirror.openshift.com/pub/openshift-v4/dependencies/rhcos/latest/) page and run the following command to create a new customized `initramfs` file with the following information:

    ``` text
    $ coreos-installer pxe customize \
        --pre-install mount-iscsi.sh \
        --post-install unmount-iscsi.sh \
        --dest-device /dev/mapper/mpatha \
        --dest-ignition config.ign \
        --dest-karg-append rd.iscsi.firmware=1 \
        --dest-karg-append rd.multipath=default \
        -o custom.img rhcos-<version>-live-initramfs.x86_64.img
    ```

    where:

    `mount-iscsi.sh`
    Specifies the script that gets run before installation. It should contain the `iscsiadm` commands for mounting the iSCSI target.

    `unmount-iscsi.sh`
    Specifies the script that gets run after installation. It should contain the command `iscsiadm --mode node --logout=all`.

    `/dev/mapper/mpatha`
    Specifies the path to the device. If you are using multipath, the multipath device, `/dev/mapper/mpatha`, If there are multiple multipath devices connected, or to be explicit, you can use the World Wide Name (WWN) symlink available in `/dev/disk/by-path`.

    `config.ign`
    Specifies the Ignition configuration for the destination system.

    `rd.iscsi.firmware=1`
    Specifies the iSCSI parameter is read from the BIOS firmware.

    `rd.multipath=default`
    Specifies if you want to enable multipathing. Optional parameter.

    For more information about see the `dracut.cmdline` manual page.

</div>

## Networking and bonding options for ISO installations

You can configure advanced options so that you can modify the Red Hat Enterprise Linux CoreOS (RHCOS) manual installation process. The subsequent sections show examples of networking options for an ISO installation.

If you install RHCOS from an ISO image, you can add kernel arguments manually when you boot the image to configure networking for a node. If no networking arguments are specified, DHCP is activated in the initramfs when RHCOS detects that networking is required to fetch the Ignition config file.

> [!IMPORTANT]
> When adding networking arguments manually, you must also add the `rd.neednet=1` kernel argument to bring the network up in the initramfs.

The following information provides examples for configuring networking and bonding on your RHCOS nodes for ISO installations. The examples describe how to use the `ip=`, `nameserver=`, and `bond=` kernel arguments.

> [!NOTE]
> Ordering is important when adding the kernel arguments: `ip=`, `nameserver=`, and then `bond=`.

The networking options are passed to the `dracut` tool during system boot. For more information about the networking options supported by `dracut`, see `dracut.cmdline` manual page.

<div>

<div class="title">

Additional resources

</div>

- [`dracut.cmdline` manual page](https://www.man7.org/linux/man-pages/man7/dracut.cmdline.7.html)

</div>

### Configuring DHCP or static IP addresses

You can configure an IP address by using either DHCP or an individual static IP address. If you set a static IP, you must then identify the DNS server IP address on each node.

The configuration examples in the procedure, update the IP addresses for the following components:

- The node’s IP address to `10.10.10.2`

- The gateway address to `10.10.10.254`

- The netmask to `255.255.255.0`

- The hostname to `core0.example.com`

- The DNS server address to `4.4.4.41`

- The auto-configuration value to `none`. No auto-configuration is required when IP networking is configured statically.

<div>

<div class="title">

Procedure

</div>

1.  Enter a command like the following command to configure a static IP address:

    ``` terminal
    ip=10.10.10.2::10.10.10.254:255.255.255.0:core0.example.com:enp1s0:none
    nameserver=4.4.4.41
    ```

2.  Enter a command like the following command to configure a DHCP IP address:

    ``` terminal
    ip=enp1s0:dhcp
    ```

    > [!NOTE]
    > When you use DHCP to configure IP addressing for the RHCOS machines, the machines also obtain the DNS server information through DHCP. For DHCP-based deployments, you can define the DNS server address that is used by the RHCOS nodes through your DHCP server configuration.

3.  If two or more network interfaces and only one interface exists, disable DHCP on a single interface. In the example, the `enp1s0` interface has a static networking configuration and DHCP is disabled for `enp2s0`, which is not used:

    ``` terminal
    ip=10.10.10.2::10.10.10.254:255.255.255.0:core0.example.com:enp1s0:none
    ip=::::core0.example.com:enp2s0:none
    ```

4.  If you need to combine DHCP and static IP configurations on systems with multiple network interfaces, run the following example command:

    ``` terminal
    ip=enp1s0:dhcp
    ip=10.10.10.2::10.10.10.254:255.255.255.0:core0.example.com:enp2s0:none
    ```

</div>

### Configuring an IP address without a static hostname

You can configure an IP address without assigning a static hostname. If a static hostname is not set by the user, the static hostname gets picked up and automatically set by a reverse DNS lookup.

The configuration examples in the procedure, update the IP addresses for the following components:

- The node’s IP address to `10.10.10.2`

- The gateway address to `10.10.10.254`

- The netmask to `255.255.255.0`

- The DNS server address to `4.4.4.41`

- The auto-configuration value to `none`. No auto-configuration is required when IP networking is configured statically.

<div>

<div class="title">

Procedure

</div>

- To configure an IP address without a static hostname, enter a command like the following command:

  ``` terminal
  ip=10.10.10.2::10.10.10.254:255.255.255.0::enp1s0:none
  nameserver=4.4.4.41
  ```

</div>

### Specifying multiple network interfaces and DNS servers

You can specify multiple network interfaces by setting multiple `ip=` entries. You can provide multiple DNS servers by adding a `nameserver=` entry for each server,

<div>

<div class="title">

Procedure

</div>

- To specify multiple network interfaces for your interfaces, you can enter a command like the following command:

  ``` terminal
  ip=10.10.10.2::10.10.10.254:255.255.255.0:core0.example.com:enp1s0:none
  ip=10.10.10.3::10.10.10.254:255.255.255.0:core0.example.com:enp2s0:none
  ```

- To provide multiple DNS servers by adding a `nameserver=` entry for each server, enter a command like the following command:

  ``` terminal
  nameserver=1.1.1.1
  nameserver=8.8.8.8
  ```

</div>

### Configuring default gateway and route

As an optional task, you can configure routes to additional networks by setting an `rd.route=` value.

> [!NOTE]
> When you configure one or multiple networks, one default gateway is required. If the additional network gateway is different from the primary network gateway, the default gateway must be the primary network gateway.

<div>

<div class="title">

Procedure

</div>

- To configure the default gateway, enter the following command:

  ``` terminal
  ip=::10.10.10.254::::
  ```

- To configure the route for an additional network, enter the following command:

  ``` terminal
  rd.route=20.20.20.0/24:20.20.20.254:enp2s0
  ```

</div>

### Configuring VLANs on individual interfaces

As an optional task, you can configure VLANs on individual interfaces by using the `vlan=` parameter.

<div>

<div class="title">

Procedure

</div>

- To configure a VLAN on a network interface and use a static IP address, run the following command:

  ``` terminal
  ip=10.10.10.2::10.10.10.254:255.255.255.0:core0.example.com:enp2s0.100:none
  vlan=enp2s0.100:enp2s0
  ```

- To configure a VLAN on a network interface and to use DHCP, run the following command:

  ``` terminal
  ip=enp2s0.100:dhcp
  vlan=enp2s0.100:enp2s0
  ```

</div>

### Bonding multiple network interfaces to a single interface

As an optional task, you can bond multiple network interfaces to a single interface by using the `bond=` option.

The following example demonstrates editing the `/etc/config/network` file and specifying the following syntax for bonding multiple network interfaces to a single interface:

``` terminal
bond=<name>[:<network_interfaces>][:<options>]
```

- `<name>`: Specifies the bonding device name, for example `bond0`.

- `<network_interfaces>`: Specifies a comma-separated list of physical (ethernet) interfaces, such as `em1,em2`.

- `` <options>: Specifies a comma-separated list of bonding options. Enter the `modinfo bonding `` command to see available options.

When you create a bonded interface using the `bond=` command, you must specify how the IP address is assigned and other information for the bonded interface.

<div>

<div class="title">

Procedure

</div>

- To configure the bonded interface to use DHCP, edit the `/etc/config/network` file by setting the IP address for the bond to `dhcp`. For example:

  ``` terminal
  ip=bond0:dhcp
  ```

- To configure the bonded interface to use a static IP address, edit the `/etc/config/network` file entering the specific IP address you want and related information. For example:

  ``` terminal
  ip=10.10.10.2::10.10.10.254:255.255.255.0:core0.example.com:bond0:none
  ```

</div>

### Bonding multiple SR-IOV network interfaces to a dual port NIC interface

You can bond multiple SR-IOV network interfaces to a dual port NIC interface by using the `bond=` option. Ensure you apply the procedure tasks to each node.

<div>

<div class="title">

Procedure

</div>

1.  Create the SR-IOV virtual functions (VFs) following the guidance in [Managing SR-IOV devices](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/9/html/configuring_and_managing_virtualization/managing-virtual-devices_configuring-and-managing-virtualization#managing-sr-iov-devices_managing-virtual-devices). Follow the procedure in the "Attaching SR-IOV networking devices to virtual machines" section.

2.  Create the bond, attach the desired VFs to the bond and set the bond link state up following the guidance in [Configuring network bonding](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/9/html/configuring_and_managing_networking/configuring-network-bonding_configuring-and-managing-networking). Follow any of the described procedures to create the bond.

    The following examples illustrate the syntax you must use:

    - The syntax for configuring a bonded interface is `bond=<name>[:<network_interfaces>][:options]`.

      `<name>` is the bonding device name (`bond0`), `<network_interfaces>` represents the virtual functions (VFs) by their known name in the kernel and shown in the output of the `ip link` command(`eno1f0`, `eno2f0`), and *options* is a comma-separated list of bonding options. Enter `modinfo bonding` to see available options.

    - When you create a bonded interface using `bond=`, you must specify how the IP address is assigned and other information for the bonded interface.

      - To configure the bonded interface to use DHCP, set the bond’s IP address to `dhcp`. For example:

        ``` terminal
        bond=bond0:eno1f0,eno2f0:mode=active-backup
        ip=bond0:dhcp::AA:BB:CC:DD:EE:FF
        ip=eno1f0:none::AA:BB:CC:DD:EE:FF
        ip=eno2f0:none::AA:BB:CC:DD:EE:FF
        ```

      - To configure the bonded interface to use a static IP address, enter the specific IP address you want and related information. For example:

        ``` terminal
        bond=bond0:eno1f0,eno2f0:mode=active-backup
        ip=10.10.10.2::10.10.10.254:255.255.255.0:core0.example.com:bond0:none
        ```

3.  Optional: You can use network teaming as an alternative to bonding by using the `team=` parameter.

    - The syntax for configuring a team interface is: `team=name[:network_interfaces]`

      *name* is the team device name (`team0`) and *network_interfaces* represents a comma-separated list of physical (ethernet) interfaces (`em1, em2`).

      > [!NOTE]
      > Teaming is planned to be deprecated when RHCOS switches to an upcoming version of RHEL. For more information, see this [Red Hat Knowledgebase Article](https://access.redhat.com/solutions/6509691).

      Use the following example to configure a network team:

      ``` terminal
      team=team0:em1,em2
      ip=team0:dhcp
      ```

</div>

### `coreos-installer` and boot options for ISO and PXE installations

You can install RHCOS by running `coreos-installer install <options> <device>` at the command prompt, after booting into the RHCOS live environment from an ISO image.

The following table shows the subcommands, options, and arguments you can pass to the `coreos-installer` command.

<table>
<caption><code>coreos-installer</code> subcommands, command-line options, and arguments</caption>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td colspan="2" style="text-align: left;"><p><strong>coreos-installer install subcommand</strong></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><strong><em>Subcommand</em></strong></p></td>
<td style="text-align: left;"><p><strong><em>Description</em></strong></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>$ coreos-installer install &lt;options&gt; &lt;device&gt;</code></p></td>
<td style="text-align: left;"><p>Embed an Ignition config in an ISO image.</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><p><strong>coreos-installer install subcommand options</strong></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><strong><em>Option</em></strong></p></td>
<td style="text-align: left;"><p><strong><em>Description</em></strong></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>-u</code>, <code>--image-url &lt;url&gt;</code></p></td>
<td style="text-align: left;"><p>Specify the image URL manually.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>-f</code>, <code>--image-file &lt;path&gt;</code></p></td>
<td style="text-align: left;"><p>Specify a local image file manually. Used for debugging.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>-i,</code> <code>--ignition-file &lt;path&gt;</code></p></td>
<td style="text-align: left;"><p>Embed an Ignition config from a file.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>-I</code>, <code>--ignition-url &lt;URL&gt;</code></p></td>
<td style="text-align: left;"><p>Embed an Ignition config from a URL.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>--ignition-hash &lt;digest&gt;</code></p></td>
<td style="text-align: left;"><p>Digest <code>type-value</code> of the Ignition config.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>-p</code>, <code>--platform &lt;name&gt;</code></p></td>
<td style="text-align: left;"><p>Override the Ignition platform ID for the installed system.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>--console &lt;spec&gt;</code></p></td>
<td style="text-align: left;"><p>Set the kernel and boot loader console for the installed system. For more information about the format of <code>&lt;spec&gt;</code>, see the <a href="https://www.kernel.org/doc/html/latest/admin-guide/serial-console.html">Linux kernel serial console</a> documentation.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>--append-karg &lt;arg&gt;…​</code></p></td>
<td style="text-align: left;"><p>Append a default kernel argument to the installed system.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>--delete-karg &lt;arg&gt;…​</code></p></td>
<td style="text-align: left;"><p>Delete a default kernel argument from the installed system.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>-n</code>, <code>--copy-network</code></p></td>
<td style="text-align: left;"><p>Copy the network configuration from the install environment.</p>
<div class="important">
<div class="title">
&#10;</div>
<p>The <code>--copy-network</code> option only copies networking configuration found under <code>/etc/NetworkManager/system-connections</code>. In particular, it does not copy the system hostname.</p>
</div></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>--network-dir &lt;path&gt;</code></p></td>
<td style="text-align: left;"><p>For use with <code>-n</code>. Default is <code>/etc/NetworkManager/system-connections/</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>--save-partlabel &lt;lx&gt;..</code></p></td>
<td style="text-align: left;"><p>Save partitions with this label glob.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>--save-partindex &lt;id&gt;…​</code></p></td>
<td style="text-align: left;"><p>Save partitions with this number or range.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>--insecure</code></p></td>
<td style="text-align: left;"><p>Skip RHCOS image signature verification.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>--insecure-ignition</code></p></td>
<td style="text-align: left;"><p>Allow Ignition URL without HTTPS or hash.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>--architecture &lt;name&gt;</code></p></td>
<td style="text-align: left;"><p>Target CPU architecture. Valid values are <code>x86_64</code> and <code>aarch64</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>--preserve-on-error</code></p></td>
<td style="text-align: left;"><p>Do not clear partition table on error.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>-h</code>, <code>--help</code></p></td>
<td style="text-align: left;"><p>Print help information.</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><p><strong>coreos-installer install subcommand argument</strong></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><strong><em>Argument</em></strong></p></td>
<td style="text-align: left;"><p><strong><em>Description</em></strong></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>&lt;device&gt;</code></p></td>
<td style="text-align: left;"><p>The destination device.</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><p><strong>coreos-installer ISO subcommands</strong></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><strong><em>Subcommand</em></strong></p></td>
<td style="text-align: left;"><p><strong><em>Description</em></strong></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>$ coreos-installer iso customize &lt;options&gt; &lt;ISO_image&gt;</code></p></td>
<td style="text-align: left;"><p>Customize a RHCOS live ISO image.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>coreos-installer iso reset &lt;options&gt; &lt;ISO_image&gt;</code></p></td>
<td style="text-align: left;"><p>Restore a RHCOS live ISO image to default settings.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>coreos-installer iso ignition remove &lt;options&gt; &lt;ISO_image&gt;</code></p></td>
<td style="text-align: left;"><p>Remove the embedded Ignition config from an ISO image.</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><p><strong>coreos-installer ISO customize subcommand options</strong></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><strong><em>Option</em></strong></p></td>
<td style="text-align: left;"><p><strong><em>Description</em></strong></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>--dest-ignition &lt;path&gt;</code></p></td>
<td style="text-align: left;"><p>Merge the specified Ignition config file into a new configuration fragment for the destination system.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>--dest-console &lt;spec&gt;</code></p></td>
<td style="text-align: left;"><p>Specify the kernel and boot loader console for the destination system.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>--dest-device &lt;path&gt;</code></p></td>
<td style="text-align: left;"><p>Install and overwrite the specified destination device.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>--dest-karg-append &lt;arg&gt;</code></p></td>
<td style="text-align: left;"><p>Add a kernel argument to each boot of the destination system.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>--dest-karg-delete &lt;arg&gt;</code></p></td>
<td style="text-align: left;"><p>Delete a kernel argument from each boot of the destination system.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>--network-keyfile &lt;path&gt;</code></p></td>
<td style="text-align: left;"><p>Configure networking by using the specified NetworkManager keyfile for live and destination systems.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>--ignition-ca &lt;path&gt;</code></p></td>
<td style="text-align: left;"><p>Specify an additional TLS certificate authority to be trusted by Ignition.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>--pre-install &lt;path&gt;</code></p></td>
<td style="text-align: left;"><p>Run the specified script before installation.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>--post-install &lt;path&gt;</code></p></td>
<td style="text-align: left;"><p>Run the specified script after installation.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>--installer-config &lt;path&gt;</code></p></td>
<td style="text-align: left;"><p>Apply the specified installer configuration file.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>--live-ignition &lt;path&gt;</code></p></td>
<td style="text-align: left;"><p>Merge the specified Ignition config file into a new configuration fragment for the live environment.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>--live-karg-append &lt;arg&gt;</code></p></td>
<td style="text-align: left;"><p>Add a kernel argument to each boot of the live environment.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>--live-karg-delete &lt;arg&gt;</code></p></td>
<td style="text-align: left;"><p>Delete a kernel argument from each boot of the live environment.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>--live-karg-replace &lt;k=o=n&gt;</code></p></td>
<td style="text-align: left;"><p>Replace a kernel argument in each boot of the live environment, in the form <code>key=old=new</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>-f</code>, <code>--force</code></p></td>
<td style="text-align: left;"><p>Overwrite an existing Ignition config.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>-o</code>, <code>--output &lt;path&gt;</code></p></td>
<td style="text-align: left;"><p>Write the ISO to a new output file.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>-h</code>, <code>--help</code></p></td>
<td style="text-align: left;"><p>Print help information.</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><p><strong>coreos-installer PXE subcommands</strong></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><strong><em>Subcommand</em></strong></p></td>
<td style="text-align: left;"><p><strong><em>Description</em></strong></p></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><p>Note that not all of these options are accepted by all subcommands.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>coreos-installer pxe customize &lt;options&gt; &lt;path&gt;</code></p></td>
<td style="text-align: left;"><p>Customize a RHCOS live PXE boot config.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>coreos-installer pxe ignition wrap &lt;options&gt;</code></p></td>
<td style="text-align: left;"><p>Wrap an Ignition config in an image.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>coreos-installer pxe ignition unwrap &lt;options&gt; &lt;image_name&gt;</code></p></td>
<td style="text-align: left;"><p>Show the wrapped Ignition config in an image.</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><p><strong>coreos-installer PXE customize subcommand options</strong></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><strong><em>Option</em></strong></p></td>
<td style="text-align: left;"><p><strong><em>Description</em></strong></p></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><p>Note that not all of these options are accepted by all subcommands.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>--dest-ignition &lt;path&gt;</code></p></td>
<td style="text-align: left;"><p>Merge the specified Ignition config file into a new configuration fragment for the destination system.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>--dest-console &lt;spec&gt;</code></p></td>
<td style="text-align: left;"><p>Specify the kernel and boot loader console for the destination system.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>--dest-device &lt;path&gt;</code></p></td>
<td style="text-align: left;"><p>Install and overwrite the specified destination device.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>--network-keyfile &lt;path&gt;</code></p></td>
<td style="text-align: left;"><p>Configure networking by using the specified NetworkManager keyfile for live and destination systems.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>--ignition-ca &lt;path&gt;</code></p></td>
<td style="text-align: left;"><p>Specify an additional TLS certificate authority to be trusted by Ignition.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>--pre-install &lt;path&gt;</code></p></td>
<td style="text-align: left;"><p>Run the specified script before installation.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>post-install &lt;path&gt;</code></p></td>
<td style="text-align: left;"><p>Run the specified script after installation.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>--installer-config &lt;path&gt;</code></p></td>
<td style="text-align: left;"><p>Apply the specified installer configuration file.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>--live-ignition &lt;path&gt;</code></p></td>
<td style="text-align: left;"><p>Merge the specified Ignition config file into a new configuration fragment for the live environment.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>-o,</code> <code>--output &lt;path&gt;</code></p></td>
<td style="text-align: left;"><p>Write the initramfs to a new output file.</p>
<div class="note">
<div class="title">
&#10;</div>
<p>This option is required for PXE environments.</p>
</div></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>-h</code>, <code>--help</code></p></td>
<td style="text-align: left;"><p>Print help information.</p></td>
</tr>
</tbody>
</table>

You can automatically start `coreos-installer` options at boot time by passing `coreos.inst` boot arguments to the RHCOS live installer. These are provided in addition to the standard boot arguments.

- For ISO installations, the `coreos.inst` options can be added by interrupting the automatic boot at the boot loader menu. You can interrupt the automatic boot by pressing `TAB` while the **RHEL CoreOS (Live)** menu option is highlighted.

- For PXE or iPXE installations, the `coreos.inst` options must be added to the `APPEND` line before the RHCOS live installer is booted.

The following table shows the RHCOS live installer `coreos.inst` boot options for ISO and PXE installations.

<table>
<caption><code>coreos.inst</code> boot options</caption>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Argument</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>coreos.inst.install_dev</code></p></td>
<td style="text-align: left;"><p>Required. The block device on the system to install to.</p>
<div class="note">
<div class="title">
&#10;</div>
<p>It is recommended to use the full path, such as <code>/dev/sda</code>, although <code>sda</code> is allowed.</p>
</div></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>coreos.inst.ignition_url</code></p></td>
<td style="text-align: left;"><p>Optional: The URL of the Ignition config to embed into the installed system. If no URL is specified, no Ignition config is embedded. Only HTTP and HTTPS protocols are supported.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>coreos.inst.save_partlabel</code></p></td>
<td style="text-align: left;"><p>Optional: Comma-separated labels of partitions to preserve during the install. Glob-style wildcards are permitted. The specified partitions do not need to exist.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>coreos.inst.save_partindex</code></p></td>
<td style="text-align: left;"><p>Optional: Comma-separated indexes of partitions to preserve during the install. Ranges <code>m-n</code> are permitted, and either <code>m</code> or <code>n</code> can be omitted. The specified partitions do not need to exist.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>coreos.inst.insecure</code></p></td>
<td style="text-align: left;"><p>Optional: Permits the OS image that is specified by <code>coreos.inst.image_url</code> to be unsigned.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>coreos.inst.image_url</code></p></td>
<td style="text-align: left;"><p>Optional: Download and install the specified RHCOS image.</p>
<ul>
<li><p>This argument should not be used in production environments and is intended for debugging purposes only.</p></li>
<li><p>While this argument can be used to install a version of RHCOS that does not match the live media, it is recommended that you instead use the media that matches the version you want to install.</p></li>
<li><p>If you are using <code>coreos.inst.image_url</code>, you must also use <code>coreos.inst.insecure</code>. This is because the bare-metal media are not GPG-signed for OpenShift Container Platform.</p></li>
<li><p>Only HTTP and HTTPS protocols are supported.</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>coreos.inst.skip_reboot</code></p></td>
<td style="text-align: left;"><p>Optional: The system will not reboot after installing. After the install finishes, you will receive a prompt that allows you to inspect what is happening during installation. This argument should not be used in production environments and is intended for debugging purposes only.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>coreos.inst.platform_id</code></p></td>
<td style="text-align: left;"><p>Optional: The Ignition platform ID of the platform the RHCOS image is being installed on. Default is <code>metal</code>. This option determines whether or not to request an Ignition config from the cloud provider, such as VMware. For example: <code>coreos.inst.platform_id=vmware</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>ignition.config.url</code></p></td>
<td style="text-align: left;"><p>Optional: The URL of the Ignition config for the live boot. For example, this can be used to customize how <code>coreos-installer</code> is invoked, or to run code before or after the installation. This is different from <code>coreos.inst.ignition_url</code>, which is the Ignition config for the installed system.</p></td>
</tr>
</tbody>
</table>

## Enabling multipathing with kernel arguments on RHCOS

RHCOS supports multipathing on the primary disk, allowing stronger resilience to hardware failure to achieve higher host availability.

You can enable multipathing at installation time for nodes that were provisioned in OpenShift Container Platform 4.8 or later. While postinstallation support is available by activating multipathing through the machine config, Red Hat recommends enabling multipathing during installation.

In setups where any I/O to non-optimized paths results in I/O system errors, you must enable multipathing at installation time.

> [!IMPORTANT]
> On IBM Z® and IBM® LinuxONE, you can enable multipathing only if you configured your cluster for it during installation. For more information, see "Installing RHCOS and starting the OpenShift Container Platform bootstrap process" in *Installing a cluster with z/VM on IBM Z® and IBM® LinuxONE*.

The following procedure enables multipath at installation time and appends kernel arguments to the `coreos-installer install` command so that the installed system itself will use multipath beginning from the first boot.

> [!NOTE]
> OpenShift Container Platform does not support enabling multipathing as a day-2 activity on nodes that have been upgraded from 4.6 or earlier.

<div>

<div class="title">

Prerequisites

</div>

- You have created the Ignition config files for your cluster.

- You have reviewed *Installing RHCOS and starting the OpenShift Container Platform bootstrap process*.

</div>

<div>

<div class="title">

Procedure

</div>

1.  To enable multipath and start the `multipathd` daemon, run the following command on the installation host:

    ``` terminal
    $ mpathconf --enable && systemctl start multipathd.service
    ```

    1.  Optional: If booting the PXE or ISO, you can instead enable multipath by adding `rd.multipath=default` from the kernel command line.

2.  Append the kernel arguments by invoking the `coreos-installer` program:

    - If there is only one multipath device connected to the machine, the device should be available at path `/dev/mapper/mpatha`. For example:

      ``` terminal
      $ coreos-installer install /dev/mapper/mpatha \
      --ignition-url=http://host/worker.ign \
      --append-karg rd.multipath=default \
      --append-karg root=/dev/disk/by-label/dm-mpath-root \
      --append-karg rw
      ```

      - `/dev/mapper/mpatha`: Indicates the path of the single multipathed device.

    - If there are multiple multipath devices connected to the machine, instead of using `/dev/mapper/mpatha`, Red Hat recommends using the World Wide Name (WWN) symlink. The symlink is available in `/dev/disk/by-id`. For example:

      ``` terminal
      $ coreos-installer install /dev/disk/by-id/wwn-<wwn_ID> \
      --ignition-url=http://host/worker.ign \
      --append-karg rd.multipath=default \
      --append-karg root=/dev/disk/by-label/dm-mpath-root \
      --append-karg rw
      ```

      where:

    - `<wwn_ID>`:: Indicates the WWN ID of the target multipathed device. For example, `0xx194e957fcedb4841`.

      This symlink can also be used as the `coreos.inst.install_dev` kernel argument when using special `coreos.inst.*` arguments to direct the live installer. For more information, see "Installing RHCOS and starting the OpenShift Container Platform bootstrap process".

3.  Reboot into the installed system.

4.  Check that the kernel arguments worked by going to one of the worker nodes and listing the kernel command-line arguments (in `/proc/cmdline` on the host):

    ``` terminal
    $ oc debug node/ip-10-0-141-105.ec2.internal
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    Starting pod/ip-10-0-141-105ec2internal-debug ...
    To use host binaries, run `chroot /host`

    sh-4.2# cat /host/proc/cmdline
    ...
    rd.multipath=default root=/dev/disk/by-label/dm-mpath-root
    ...

    sh-4.2# exit
    ```

    </div>

    You should see the added kernel arguments.

</div>

### Enabling multipathing on secondary disks

RHCOS also supports multipathing on a secondary disk. Instead of kernel arguments, you use Ignition to enable multipathing for the secondary disk at installation time.

<div>

<div class="title">

Prerequisites

</div>

- You have read the section *Disk partitioning*.

- You have read *Enabling multipathing with kernel arguments on RHCOS*.

- You have installed the Butane utility.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create a Butane config with information similar to the following:

    <div class="formalpara">

    <div class="title">

    Example `multipath-config.bu`

    </div>

    ``` yaml
    variant: openshift
    version: 4.17.0
    systemd:
      units:
        - name: mpath-configure.service
          enabled: true
          contents: |
            [Unit]
            Description=Configure Multipath on Secondary Disk
            ConditionFirstBoot=true
            ConditionPathExists=!/etc/multipath.conf
            Before=multipathd.service
            DefaultDependencies=no

            [Service]
            Type=oneshot
            ExecStart=/usr/sbin/mpathconf --enable

            [Install]
            WantedBy=multi-user.target
        - name: mpath-var-lib-container.service
          enabled: true
          contents: |
            [Unit]
            Description=Set Up Multipath On /var/lib/containers
            ConditionFirstBoot=true
            Requires=dev-mapper-mpatha.device
            After=dev-mapper-mpatha.device
            After=ostree-remount.service
            Before=kubelet.service
            DefaultDependencies=no

            [Service]
            Type=oneshot
            ExecStart=/usr/sbin/mkfs.xfs -L containers -m reflink=1 /dev/mapper/mpatha
            ExecStart=/usr/bin/mkdir -p /var/lib/containers

            [Install]
            WantedBy=multi-user.target
        - name: var-lib-containers.mount
          enabled: true
          contents: |
            [Unit]
            Description=Mount /var/lib/containers
            After=mpath-var-lib-containers.service
            Before=kubelet.service

            [Mount]
            What=/dev/disk/by-label/dm-mpath-containers
            Where=/var/lib/containers
            Type=xfs

            [Install]
            WantedBy=multi-user.target
    ```

    </div>

    where:

    `Before=multipathd.service`
    Specifies that the configuration must be set before launching the multipath daemon.

    `ExecStart=/usr/sbin/mpathconf`
    Specifies starting the `mpathconf` utility.

    `ConditionFirstBoot=true`
    Set to the value `true`.

    `[Service]`
    Specifies the creation of the filesystem and directory `/var/lib/containers`.

    `Before=kubelet.service`
    Specifies that the device must be mounted before starting any nodes.

    `[Mount]`
    Specifies to mount the device to the `/var/lib/containers` mount point. This location cannot be a symlink.

2.  Create the Ignition configuration by running the following command:

    ``` terminal
    $ butane --pretty --strict multipath-config.bu > multipath-config.ign
    ```

3.  Continue with the rest of the first boot RHCOS installation process.

    > [!IMPORTANT]
    > Do not add the `rd.multipath` or `root` kernel arguments on the CLI during installation unless the primary disk is also multipathed.

</div>

## Installing RHCOS manually on an iSCSI boot device

You can manually install RHCOS on an iSCSI target.

<div>

<div class="title">

Prerequisites

</div>

1.  You are in the RHCOS live environment.

2.  You have an iSCSI target that you want to install RHCOS on.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Mount the iSCSI target from the live environment by running the following command:

    ``` text
    $ iscsiadm \
        --mode discovery \
        --type sendtargets
        --portal <IP_address> \
        --login
    ```

    where:

    `<IP_address>`
    Specifies the IP address of the target portal.

2.  Install RHCOS onto the iSCSI target by running the following command and using the necessary kernel arguments, for example:

    ``` text
    $ coreos-installer install \
    /dev/disk/by-path/ip-<IP_address>:<port>-iscsi-<target_iqn>-lun-<lun> \
    --append-karg rd.iscsi.initiator=<initiator_iqn> \
    --append.karg netroot=<target_iqn> \
    --console ttyS0,115200n8
    --ignition-file <path_to_file>
    ```

    where:

    `/dev/disk/by-path/ip`
    Specifies the installation location. You must provide the IP address of the target portal, the associated port number, the target iSCSI node in IQN format, and the iSCSI logical unit number (LUN).

    `<initiator_iqn>`
    Specifies the iSCSI initiator, or client, name in IQN format. The initiator forms a session to connect to the iSCSI target.

    `<target_iqn>`
    Specifies the iSCSI target, or server, name in IQN format.

    For more information about the iSCSI options supported by `dracut`, see the [`dracut.cmdline` manual page](https://www.man7.org/linux/man-pages/man7/dracut.cmdline.7.html).

3.  Unmount the iSCSI disk with the following command:

    ``` text
    $ iscsiadm --mode node --logoutall=all
    ```

    This procedure can also be performed using the `coreos-installer iso customize` or `coreos-installer pxe customize` subcommands.

</div>

## Installing RHCOS on an iSCSI boot device using iBFT

On a completely diskless machine, the iSCSI target and initiator values can be passed through iBFT. iSCSI multipathing is also supported.

<div>

<div class="title">

Prerequisites

</div>

1.  You are in the RHCOS live environment.

2.  You have an iSCSI target you want to install RHCOS on.

3.  Optional: You have configured multipathing for your iSCSI target.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Mount the iSCSI target from the live environment by running the following command:

    ``` text
    $ iscsiadm \
        --mode discovery \
        --type sendtargets
        --portal <IP_address> \
        --login
    ```

    where:

    `<IP_address>`
    Specifies the IP address of the target portal.

2.  Optional: enable multipathing and start the daemon with the following command:

    ``` text
    $ mpathconf --enable && systemctl start multipathd.service
    ```

3.  Install RHCOS onto the iSCSI target by running the following command and using the necessary kernel arguments, for example:

    ``` text
    $ coreos-installer install \
        /dev/mapper/mpatha \
        --append-karg rd.iscsi.firmware=1 \
        --append-karg rd.multipath=default \
        --console ttyS0 \
        --ignition-file <path_to_file>
    ```

    where:

    `/dev/mapper/mpatha`
    Specifies the path of a single multipathed device. If there are multiple multipath devices connected, or to be explicit, you can use the World Wide Name (WWN) symlink available in `/dev/disk/by-path`.

    `rd.iscsi.firmware=1`
    Specifies that the iSCSI parameter is read from the BIOS firmware.

    `rd.multipath=default`
    Specifies to enable multipathing. Optional parameter.

    For more information about the iSCSI options supported by `dracut`, see the `dracut.cmdline` manual page.

4.  Unmount the iSCSI disk:

    ``` text
    $ iscsiadm --mode node --logout=all
    ```

    You can also perform this procedure by using the `coreos-installer iso customize` or `coreos-installer pxe customize` subcommands.

</div>

<div>

<div class="title">

Additional resources

</div>

- [`dracut.cmdline` manual page](https://www.man7.org/linux/man-pages/man7/dracut.cmdline.7.html)

- [Installing RHCOS and starting the OpenShift Container Platform bootstrap process](installing-bare-metal.md#creating-machines-bare-metal_installing-bare-metal)

</div>

# Waiting for the bootstrap process to complete

The OpenShift Container Platform bootstrap process begins after the cluster nodes first boot into the persistent RHCOS environment that has been installed to disk. The configuration information provided through the Ignition config files is used to initialize the bootstrap process and install OpenShift Container Platform on the machines. You must wait for the bootstrap process to complete.

<div>

<div class="title">

Prerequisites

</div>

- You have created the Ignition config files for your cluster.

- You have configured suitable network, DNS, and load balancing infrastructure.

- You have obtained the installation program and generated the Ignition config files for your cluster.

- You installed RHCOS on your cluster machines and provided the Ignition config files that the OpenShift Container Platform installation program generated.

- Your machines have direct internet access or have an HTTP or HTTPS proxy available.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Monitor the bootstrap process:

    ``` terminal
    $ ./openshift-install --dir <installation_directory> wait-for bootstrap-complete \
        --log-level=info
    ```

    where:

    `<installation_directory>`
    Specifies the path to the directory that stores the installation files.

    `--log-level=info`
    Specifies `warn`, `debug`, or `error` instead of `info` to view different installation details.

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    INFO Waiting up to 30m0s for the Kubernetes API at https://api.test.example.com:6443...
    INFO API v1.33.4 up
    INFO Waiting up to 30m0s for bootstrapping to complete...
    INFO It is now safe to remove the bootstrap resources
    ```

    </div>

    The command succeeds when the Kubernetes API server signals that it has been bootstrapped on the control plane machines.

2.  After the bootstrap process is complete, remove the bootstrap machine from the load balancer.

    > [!IMPORTANT]
    > You must remove the bootstrap machine from the load balancer at this point. You can also remove or reformat the bootstrap machine itself.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Monitoring installation progress](../../../support/troubleshooting/troubleshooting-installations.md#monitoring-installation-progress_troubleshooting-installations)

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

<div>

<div class="title">

Additional resources

</div>

- [Certificate Signing Requests](https://kubernetes.io/docs/reference/access-authn-authz/certificate-signing-requests/)

</div>

# Initial Operator configuration

After the control plane initializes, you must immediately configure some Operators so that they all become available.

<div>

<div class="title">

Prerequisites

</div>

- Your control plane has initialized.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Watch the cluster components come online:

    ``` terminal
    $ watch -n5 oc get clusteroperators
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    NAME                                       VERSION   AVAILABLE   PROGRESSING   DEGRADED   SINCE
    authentication                             4.17.0    True        False         False      19m
    baremetal                                  4.17.0    True        False         False      37m
    cloud-credential                           4.17.0    True        False         False      40m
    cluster-autoscaler                         4.17.0    True        False         False      37m
    config-operator                            4.17.0    True        False         False      38m
    console                                    4.17.0    True        False         False      26m
    csi-snapshot-controller                    4.17.0    True        False         False      37m
    dns                                        4.17.0    True        False         False      37m
    etcd                                       4.17.0    True        False         False      36m
    image-registry                             4.17.0    True        False         False      31m
    ingress                                    4.17.0    True        False         False      30m
    insights                                   4.17.0    True        False         False      31m
    kube-apiserver                             4.17.0    True        False         False      26m
    kube-controller-manager                    4.17.0    True        False         False      36m
    kube-scheduler                             4.17.0    True        False         False      36m
    kube-storage-version-migrator              4.17.0    True        False         False      37m
    machine-api                                4.17.0    True        False         False      29m
    machine-approver                           4.17.0    True        False         False      37m
    machine-config                             4.17.0    True        False         False      36m
    marketplace                                4.17.0    True        False         False      37m
    monitoring                                 4.17.0    True        False         False      29m
    network                                    4.17.0    True        False         False      38m
    node-tuning                                4.17.0    True        False         False      37m
    openshift-apiserver                        4.17.0    True        False         False      32m
    openshift-controller-manager               4.17.0    True        False         False      30m
    openshift-samples                          4.17.0    True        False         False      32m
    operator-lifecycle-manager                 4.17.0    True        False         False      37m
    operator-lifecycle-manager-catalog         4.17.0    True        False         False      37m
    operator-lifecycle-manager-packageserver   4.17.0    True        False         False      32m
    service-ca                                 4.17.0    True        False         False      38m
    storage                                    4.17.0    True        False         False      37m
    ```

    </div>

2.  Configure the Operators that are not available.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Gathering logs from a failed installation](../../../support/troubleshooting/troubleshooting-installations.md#installation-bootstrap-gather_troubleshooting-installations)

- [Troubleshooting Operator issues](../../../support/troubleshooting/troubleshooting-operator-issues.md#troubleshooting-operator-issues)

</div>

## Image registry removed during installation

On platforms that do not provide shareable object storage, the OpenShift Image Registry Operator bootstraps itself as `Removed`. This allows `openshift-installer` to complete installations on these platform types.

After installation, you must edit the Image Registry Operator configuration to switch the `managementState` from `Removed` to `Managed`. When this has completed, you must configure storage.

## Image registry storage configuration

The Image Registry Operator is not initially available for platforms that do not provide default storage. After installation, you must configure your registry to use storage so that the Registry Operator is made available.

Configure a persistent volume, which is required for production clusters. Where applicable, you can configure an empty directory as the storage location for non-production clusters.

You can also allow the image registry to use block storage types by using the `Recreate` rollout strategy during upgrades.

### Configuring registry storage for bare metal and other manual installations

As a cluster administrator, following installation you must configure your registry to use storage.

<div>

<div class="title">

Prerequisites

</div>

- You have access to the cluster as a user with the `cluster-admin` role.

- You have a cluster that uses manually-provisioned Red Hat Enterprise Linux CoreOS (RHCOS) nodes, such as bare metal.

- You have provisioned persistent storage for your cluster, such as Red Hat OpenShift Data Foundation.

  > [!IMPORTANT]
  > OpenShift Container Platform supports `ReadWriteOnce` access for image registry storage when you have only one replica. `ReadWriteOnce` access also requires that the registry uses the `Recreate` rollout strategy. To deploy an image registry that supports high availability with two or more replicas, `ReadWriteMany` access is required.

- You must have a system with at least 100Gi capacity.

</div>

<div>

<div class="title">

Procedure

</div>

1.  To configure your registry to use storage, change the `spec.storage.pvc` in the `configs.imageregistry/cluster` resource.

    > [!NOTE]
    > When you use shared storage, review your security settings to prevent outside access.

2.  Verify that you do not have a registry pod:

    ``` terminal
    $ oc get pod -n openshift-image-registry -l docker-registry=default
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    No resources found in openshift-image-registry namespace
    ```

    </div>

    > [!NOTE]
    > If you do have a registry pod in your output, you do not need to continue with this procedure.

3.  Check the registry configuration:

    ``` terminal
    $ oc edit configs.imageregistry.operator.openshift.io
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` yaml
    storage:
      pvc:
        claim:
    ```

    </div>

    Leave the `claim` field blank to allow the automatic creation of an `image-registry-storage` PVC.

4.  Check the `clusteroperator` status:

    ``` terminal
    $ oc get clusteroperator image-registry
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    NAME             VERSION              AVAILABLE   PROGRESSING   DEGRADED   SINCE   MESSAGE
    image-registry   4.17                 True        False         False      6h50m
    ```

    </div>

5.  Ensure that your registry is set to managed to enable building and pushing of images.

    - Run:

          $ oc edit configs.imageregistry/cluster

      Then, change the line

          managementState: Removed

      to

          managementState: Managed

</div>

### Configuring storage for the image registry in non-production clusters

You must configure storage for the Image Registry Operator. For non-production clusters, you can set the image registry to an empty directory. If you do so, all images are lost if you restart the registry.

<div>

<div class="title">

Procedure

</div>

- To set the image registry storage to an empty directory:

  ``` terminal
  $ oc patch configs.imageregistry.operator.openshift.io cluster --type merge --patch '{"spec":{"storage":{"emptyDir":{}}}}'
  ```

  > [!WARNING]
  > Configure this option only for non-production clusters.

  If you run this command before the Image Registry Operator initializes its components, the `oc patch` command fails with the following error:

  ``` terminal
  Error from server (NotFound): configs.imageregistry.operator.openshift.io "cluster" not found
  ```

  Wait a few minutes and run the command again.

</div>

### Configuring block registry storage for bare metal

To allow the image registry to use block storage types during upgrades as a cluster administrator, you can use the `Recreate` rollout strategy.

> [!IMPORTANT]
> Block storage volumes, or block persistent volumes, are supported but not recommended for use with the image registry on production clusters. An installation where the registry is configured on block storage is not highly available because the registry cannot have more than one replica.
>
> If you choose to use a block storage volume with the image registry, you must use a filesystem persistent volume claim (PVC).

<div>

<div class="title">

Procedure

</div>

1.  Enter the following command to set the image registry storage as a block storage type, patch the registry so that it uses the `Recreate` rollout strategy, and runs with only one (`1`) replica:

    ``` terminal
    $ oc patch config.imageregistry.operator.openshift.io/cluster --type=merge -p '{"spec":{"rolloutStrategy":"Recreate","replicas":1}}'
    ```

2.  Provision the PV for the block storage device, and create a PVC for that volume. The requested block volume uses the ReadWriteOnce (RWO) access mode.

    1.  Create a `pvc.yaml` file with the following contents to define a VMware vSphere `PersistentVolumeClaim` object:

        ``` yaml
        kind: PersistentVolumeClaim
        apiVersion: v1
        metadata:
          name: image-registry-storage
          namespace: openshift-image-registry
        spec:
          accessModes:
          - ReadWriteOnce
          resources:
            requests:
              storage: 100Gi
        ```

        where:

        `metadata.name`
        Specifies a unique name that represents the `PersistentVolumeClaim` object.

        `metadata.namespace`
        Specifies the `namespace` for the `PersistentVolumeClaim` object, which is `openshift-image-registry`.

        `spec.accessModes`
        Specifies the access mode of the persistent volume claim. With `ReadWriteOnce`, the volume can be mounted with read and write permissions by a single node.

        `spec.resources.requests.storage`
        The size of the persistent volume claim.

    2.  Enter the following command to create the `PersistentVolumeClaim` object from the file:

        ``` terminal
        $ oc create -f pvc.yaml -n openshift-image-registry
        ```

3.  Enter the following command to edit the registry configuration so that it references the correct PVC:

    ``` terminal
    $ oc edit config.imageregistry.operator.openshift.io -o yaml
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` yaml
    storage:
      pvc:
        claim:
    ```

    </div>

    By creating a custom PVC, you can leave the `claim` field blank for the default automatic creation of an `image-registry-storage` PVC.

</div>

# Completing installation on user-provisioned infrastructure

To finalize the installation on user-provisioned infrastructure, complete the cluster deployment after configuring the Operators. This ensures the cluster is fully operational on the infrastructure that you provide.

<div>

<div class="title">

Prerequisites

</div>

- Your control plane has initialized.

- You have completed the initial Operator configuration.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Confirm that all the cluster components are online with the following command:

    ``` terminal
    $ watch -n5 oc get clusteroperators
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    NAME                                       VERSION   AVAILABLE   PROGRESSING   DEGRADED   SINCE
    authentication                             4.17.0    True        False         False      19m
    baremetal                                  4.17.0    True        False         False      37m
    cloud-credential                           4.17.0    True        False         False      40m
    cluster-autoscaler                         4.17.0    True        False         False      37m
    config-operator                            4.17.0    True        False         False      38m
    console                                    4.17.0    True        False         False      26m
    csi-snapshot-controller                    4.17.0    True        False         False      37m
    dns                                        4.17.0    True        False         False      37m
    etcd                                       4.17.0    True        False         False      36m
    image-registry                             4.17.0    True        False         False      31m
    ingress                                    4.17.0    True        False         False      30m
    insights                                   4.17.0    True        False         False      31m
    kube-apiserver                             4.17.0    True        False         False      26m
    kube-controller-manager                    4.17.0    True        False         False      36m
    kube-scheduler                             4.17.0    True        False         False      36m
    kube-storage-version-migrator              4.17.0    True        False         False      37m
    machine-api                                4.17.0    True        False         False      29m
    machine-approver                           4.17.0    True        False         False      37m
    machine-config                             4.17.0    True        False         False      36m
    marketplace                                4.17.0    True        False         False      37muser
    monitoring                                 4.17.0    True        False         False      29m
    network                                    4.17.0    True        False         False      38m
    node-tuning                                4.17.0    True        False         False      37m
    openshift-apiserver                        4.17.0    True        False         False      32muser
    openshift-controller-manager               4.17.0    True        False         False      30m
    openshift-samples                          4.17.0    True        False         False      32m
    operator-lifecycle-manager                 4.17.0    True        False         False      37m
    operator-lifecycle-manager-catalog         4.17.0    True        False         False      37m
    operator-lifecycle-manager-packageserver   4.17.0    True        False         False      32m
    service-ca                                 4.17.0    True        False         False      38m
    storage                                    4.17.0    True        False         False      37m
    ```

    </div>

    Alternatively, the following command notifies you when all of the clusters are available. The command also retrieves and displays credentials:

    ``` terminal
    $ ./openshift-install --dir <installation_directory> wait-for install-complete
    ```

    where:

    `<installation_directory>`
    Specifies the path to the directory that you stored the installation files in.

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    INFO Waiting up to 30m0s for the cluster to initialize...
    ```

    </div>

    The command succeeds when the Cluster Version Operator finishes deploying the OpenShift Container Platform cluster from Kubernetes API server.

    <div class="important">

    <div class="title">

    </div>

    - The Ignition config files that the installation program generates contain certificates that expire after 24 hours, which are then renewed at that time. If the cluster is shut down before renewing the certificates and the cluster is later restarted after the 24 hours have elapsed, the cluster automatically recovers the expired certificates. The exception is that you must manually approve the pending `node-bootstrapper` certificate signing requests (CSRs) to recover kubelet certificates. See the documentation for *Recovering from expired control plane certificates* for more information.

    - It is recommended that you use Ignition config files within 12 hours after they are generated because the 24-hour certificate rotates from 16 to 22 hours after the cluster is installed. By using the Ignition config files within 12 hours, you can avoid installation failure if the certificate update runs during installation.

    </div>

2.  Confirm that the Kubernetes API server is communicating with the pods.

    1.  To view a list of all pods, use the following command:

        ``` terminal
        $ oc get pods --all-namespaces
        ```

        <div class="formalpara">

        <div class="title">

        Example output

        </div>

        ``` terminal
        NAMESPACE                         NAME                                            READY   STATUS      RESTARTS   AGE
        openshift-apiserver-operator      openshift-apiserver-operator-85cb746d55-zqhs8   1/1     Running     1          9m
        openshift-apiserver               apiserver-67b9g                                 1/1     Running     0          3m
        openshift-apiserver               apiserver-ljcmx                                 1/1     Running     0          1m
        openshift-apiserver               apiserver-z25h4                                 1/1     Running     0          2m
        openshift-authentication-operator authentication-operator-69d5d8bf84-vh2n8        1/1     Running     0          5m
        ```

        </div>

    2.  View the logs for a pod that is listed in the output of the previous command by using the following command:

        ``` terminal
        $ oc logs <pod_name> -n <namespace>
        ```

        where:

        `<namespace>`
        Specifies the pod name and namespace, as shown in the output of an earlier command.

        If the pod logs display, the Kubernetes API server can communicate with the cluster machines.

3.  For an installation with Fibre Channel Protocol (FCP), additional steps are required to enable multipathing. Do not enable multipathing during installation.

    See "Enabling multipathing with kernel arguments on RHCOS" in the *Postinstallation machine configuration tasks* documentation for more information.

</div>

# Telemetry access for OpenShift Container Platform

To provide metrics about cluster health and the success of updates, the Telemetry service requires internet access. When connected, this service runs automatically by default and registers your cluster to [OpenShift Cluster Manager](https://console.redhat.com/openshift).

After you confirm that your [OpenShift Cluster Manager](https://console.redhat.com/openshift) inventory is correct, either maintained automatically by Telemetry or manually by using OpenShift Cluster Manager,use subscription watch to track your OpenShift Container Platform subscriptions at the account or multi-cluster level. For more information about subscription watch, see "Data Gathered and Used by Red Hat’s subscription services" in the *Additional resources* section.

<div>

<div class="title">

Additional resources

</div>

- [About remote health monitoring](../../../support/remote_health_monitoring/about-remote-health-monitoring.md#about-remote-health-monitoring)

- [Validating an installation](../../validation_and_troubleshooting/validating-an-installation.md#validating-an-installation)

- [Customize your cluster](../../../post_installation_configuration/cluster-tasks.md#available_cluster_customizations).

- [Remote health reporting](../../../support/remote_health_monitoring/remote-health-reporting.md#remote-health-reporting)

- [Set up your registry and configure registry storage](../../../registry/configuring_registry_storage/configuring-registry-storage-baremetal.md#configuring-registry-storage-baremetal)

- [Data Gathered and Used by Red Hat’s subscription services ](https://access.redhat.com/solutions/4656511)

</div>
