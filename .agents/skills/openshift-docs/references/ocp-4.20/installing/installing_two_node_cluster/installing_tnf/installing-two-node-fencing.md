<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

> [!IMPORTANT]
> Two-node OpenShift cluster with fencing is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.
>
> For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

A two-node OpenShift cluster with fencing provides high availability (HA) with a reduced hardware footprint. This configuration is designed for distributed or edge environments where deploying a full three-node control plane cluster is not practical.

A two-node cluster does not include compute nodes. The two control plane machines run user workloads in addition to managing the cluster.

Fencing is managed by Pacemaker, which can isolate an unresponsive node by using the Baseboard Management Console (BMC) of the node. After the unresponsive node is fenced, the remaining node can safely continue operating the cluster without the risk of resource corruption.

> [!NOTE]
> You can deploy a two-node OpenShift cluster with fencing by using either the user-provisioned infrastructure method or the installer-provisioned infrastructure method.

The two-node OpenShift cluster with fencing requires the following hosts:

| Hosts | Description |
|----|----|
| Two control plane machines | The control plane machines run the Kubernetes and OpenShift Container Platform services that form the control plane. |
| One temporary bootstrap machine | You need a bootstrap machine to deploy the OpenShift Container Platform cluster on the control plane machines. You can remove the bootstrap machine after you install the cluster. |

Minimum required hosts

The bootstrap and control plane machines must use Red Hat Enterprise Linux CoreOS (RHCOS) as the operating system. For instructions on installing RHCOS and starting the bootstrap process, see [Installing RHCOS and starting the OpenShift Container Platform bootstrap process](../../installing_bare_metal/upi/installing-bare-metal-network-customizations.md#creating-machines-bare-metal_installing-bare-metal-network-customizations)

> [!NOTE]
> The requirement to use RHCOS applies only to user-provisioned infrastructure deployments. For installer-provisioned infrastructure deployments, the bootstrap and control plane machines are provisioned automatically by the installation program, and you do not need to manually install RHCOS.

# Minimum resource requirements for installing a two-node OpenShift cluster with fencing

Each cluster must meet minimum requirements so that the cluster runs as expected.

Each cluster machine must meet the following minimum requirements:

| Machine | Operating System | CPU <sup>\[1\]</sup> | RAM | Storage | Input/Output Per Second (IOPS) <sup>\[1\]</sup> |
|----|----|----|----|----|----|
| Bootstrap | RHCOS | 4 | 16 GB | 120 GB | 300 |
| Control plane | RHCOS | 4 | 16 GB | 120 GB | 300 |

Minimum resource requirements

1.  One CPU is equivalent to one physical core when simultaneous multithreading (SMT), or Hyper-Threading, is not enabled. When enabled, use the following formula to calculate the corresponding ratio: (threads per core × cores) × sockets = CPUs.

2.  OpenShift Container Platform and Kubernetes are sensitive to disk performance, and faster storage is recommended, particularly for etcd on the control plane nodes. Note that on many cloud platforms, storage size and IOPS scale together, so you might need to over-allocate storage volume to obtain sufficient performance.

# User-provisioned DNS requirements

In OpenShift Container Platform deployments, you must ensure that cluster components meet certain DNS name resolution criteria for internal communication, certificate validation, and automated node discovery purposes.

The following is a list of required cluster components:

- The Kubernetes API

- The OpenShift Container Platform application wildcard

- The bootstrap and control plane machines

Reverse DNS resolution is also required for the Kubernetes API, the bootstrap machine, and the control plane machines.

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
<td style="text-align: left;"><p>A wildcard DNS A/AAAA or CNAME record that refers to the application ingress load balancer. The application ingress load balancer targets the machines that run the Ingress Controller pods. By default, the Ingress Controller pods run on compute nodes. In cluster topologies without dedicated compute nodes, such as two-node or three-node clusters, the control plane nodes also carry the worker label, so the Ingress pods are scheduled on the control plane nodes. These records must be resolvable by both clients external to the cluster and from all the nodes within the cluster.</p>
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
</tbody>
</table>

> [!NOTE]
> In OpenShift Container Platform 4.4 and later, you do not need to specify etcd host and SRV records in your DNS configuration.

> [!TIP]
> You can use the `dig` command to verify name and reverse name resolution. See the section on *Validating DNS resolution for user-provisioned infrastructure* for detailed validation steps.

## Example DNS configuration for user-provisioned clusters

Reference the example DNS configurations to understand how A and PTR record configuration samples meet the DNS requirements for deploying OpenShift Container Platform on user-provisioned infrastructure.

The DNS configuration examples provided here are for reference only and are not meant to provide advice for choosing one DNS solution over another.

In the examples, the cluster name is `ocp4` and the base domain is `example.com`.

> [!NOTE]
> In a two-node cluster with fencing, the control plane machines are also schedulable worker nodes. The DNS configuration must therefore include only the two control plane nodes. If you later add compute machines, provide corresponding A and PTR records for them as in a standard user-provisioned installation.

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

> [!NOTE]
> A PTR record is not required for the OpenShift Container Platform application wildcard.

# Installer-provisioned DNS requirements

In OpenShift Container Platform deployments, you must ensure that cluster components meet certain DNS name resolution criteria for internal communication, certificate validation, and automated node discovery purposes.

Clients access the OpenShift Container Platform cluster nodes over the `baremetal` network. A network administrator must configure a subdomain or subzone where the canonical name extension is the cluster name.

``` text
<cluster_name>.<base_domain>
```

For example:

``` text
test-cluster.example.com
```

OpenShift Container Platform includes functionality that uses cluster membership information to generate A/AAAA records. This resolves the node names to their IP addresses. After the nodes are registered with the API, the cluster can disperse node information without using CoreDNS-mDNS. This eliminates the network traffic associated with multicast DNS.

CoreDNS requires both TCP and UDP connections to the upstream DNS server to function correctly. Ensure the upstream DNS server can receive both TCP and UDP connections from OpenShift Container Platform cluster nodes.

In OpenShift Container Platform deployments, DNS name resolution is required for the following components:

- The Kubernetes API

- The OpenShift Container Platform application wildcard ingress API

A/AAAA records are used for name resolution and PTR records are used for reverse name resolution. Red Hat Enterprise Linux CoreOS (RHCOS) uses the reverse records or DHCP to set the hostnames for all the nodes.

Installer-provisioned installation includes functionality that uses cluster membership information to generate A/AAAA records. This resolves the node names to their IP addresses. In each record, `<cluster_name>` is the cluster name and `<base_domain>` is the base domain that you specify in the `install-config.yaml` file. A complete DNS record takes the form: `<component>.<cluster_name>.<base_domain>.`.

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
<td style="text-align: left;"><p>An A/AAAA record and a PTR record identify the API load balancer. These records must be resolvable by both clients external to the cluster and from all the nodes within the cluster.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Routes</p></td>
<td style="text-align: left;"><p><code>*.apps.&lt;cluster_name&gt;.&lt;base_domain&gt;.</code></p></td>
<td style="text-align: left;"><p>The wildcard A/AAAA record refers to the application ingress load balancer. The application ingress load balancer targets the nodes that run the Ingress Controller pods. The Ingress Controller pods run on the worker nodes by default. These records must be resolvable by both clients external to the cluster and from all the nodes within the cluster.</p>
<p>For example, <code>console-openshift-console.apps.&lt;cluster_name&gt;.&lt;base_domain&gt;</code> is used as a wildcard route to the OpenShift Container Platform console.</p></td>
</tr>
</tbody>
</table>

> [!TIP]
> You can use the `dig` command to verify DNS resolution.

# Configuring an Ingress load balancer for a two-node cluster with fencing

You must configure an external Ingress load balancer (LB) before you install a two-node OpenShift cluster with fencing. The Ingress LB forwards external application traffic to the Ingress Controller pods that run on the control plane nodes. Both nodes can actively receive traffic.

<div>

<div class="title">

Prerequisites

</div>

- You have two control plane nodes with fencing enabled.

- You have network connectivity from the load balancer to both control plane nodes.

- You created DNS records for `api.<cluster_name>.<base_domain>` and `*.apps.<cluster_name>.<base_domain>`.

- You have an external load balancer that supports health checks on endpoints.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Configure the load balancer to forward traffic for the following ports:

    - `6443`: Kubernetes API server

    - `80` and `443`: Application ingress

      You must forward traffic to both control plane nodes.

2.  Configure health checks on the load balancer. You must monitor the backend endpoints so that the load balancer only sends traffic to nodes that respond.

3.  Configure the load balancer to forward traffic to both control plane nodes. The following example shows how to configure two control plane nodes:

    ``` terminal
    frontend api_frontend
        bind *:6443
        mode tcp
        default_backend api_backend

    backend api_backend
        mode tcp
        balance roundrobin
        server cp0 <cp0_ip>:6443 check
        server cp1 <cp1_ip>:6443 check

    frontend ingress_frontend
        bind *:80
        bind *:443
        mode tcp
        default_backend ingress_backend

    backend ingress_backend
        mode tcp
        balance roundrobin
        server cp0 <cp0_ip>:80 check
        server cp1 <cp1_ip>:80 check
        server cp0 <cp0_ip>:443 check
        server cp1 <cp1_ip>:443 check
    ```

4.  Verify the load balancer configuration:

    1.  From an external client, run the following command:

        ``` terminal
        $ curl -k https://api.<cluster_name>.<base_domain>:6443/version
        ```

    2.  From an external client, access an application route by running the following command:

        ``` terminal
        $ curl https://<app>.<cluster_name>.<base_domain>
        ```

</div>

You can shut down a control plane node and verify that the load balancer stops sending traffic to that node while the other node continues to serve requests.

# Creating a manifest object for a customized br-ex bridge

You must create a manifest object to modify the cluster’s network configuration after installation. The manifest configures the br-ex bridge, which manages external network connectivity for the cluster.

For instructions on creating this manifest, see "Creating a manifest file for a customized br-ex bridge".

# Additional resources

- [Creating a manifest file for a customized br-ex bridge](../../installing_bare_metal/ipi/ipi-install-installation-workflow.md#creating-manifest-file-customized-br-ex-bridge_ipi-install-installation-workflow)

- [Configuring and managing high availability clusters in RHEL](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/9/html/configuring_and_managing_high_availability_clusters/index)
