<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

To tunnel traffic between nodes, use Generic Network Virtualization Encapsulation (Geneve). You can tune the network by using network interface controller (NIC) offloads.

Geneve provides benefits over VLANs, such as an increase in networks from 4096 to over 16 million, and layer 2 connectivity across physical networks. This allows for all pods behind a service to communicate with each other, even if they are running on different systems.

Cloud, virtual, and bare-metal environments running OpenShift Container Platform can use a high percentage of the capabilities of a network interface card (NIC) with minimal tuning. Production clusters using OVN-Kubernetes with Geneve tunneling can handle high-throughput traffic effectively and scale up (for example, utilizing 100 Gbps NICs) and scale out (for example, adding more NICs) without requiring special configuration.

In some high-performance scenarios where maximum efficiency is critical, targeted performance tuning can help optimize CPU usage, reduce overhead, and ensure that you are making full use of the NIC’s capabilities.

For environments where maximum throughput and CPU efficiency are critical, you can further optimize performance with the following strategies:

- Validate network performance by using tools such as `iPerf3` and `k8s-netperf`. By using these tools, you can benchmark throughput, latency, and packets-per-second (PPS) across pod and node interfaces.

- Evaluate OVN-Kubernetes User Defined Networking (UDN) routing techniques, such as border gateway protocol (BGP).

- Use Geneve-offload capable network adapters. Geneve-offload moves the packet checksum calculation and associated CPU overhead off of the system CPU and onto dedicated hardware on the network adapter. This frees up CPU cycles for use by pods and applications, so that users can use the full bandwidth of their network infrastructure.

# Additional resources

- [OVN-Kubernetes](../../networking/ovn_kubernetes_network_provider/about-ovn-kubernetes.md#about-ovn-kubernetes)

# Optimizing the MTU for your network

You can optimize the MTU value of your network so that your network is optimized for throughput or low latency.

There are two important maximum transmission units (MTUs): the network interface controller (NIC) MTU and the cluster network MTU.

The NIC MTU is configured at the time of OpenShift Container Platform installation, and you can also change the MTU of a cluster as a postinstallation task. For more information, see "Changing cluster network MTU".

For a cluster that uses the OVN-Kubernetes plugin, the MTU must be at least `100` bytes less than the maximum supported value of the NIC of your network. If you are optimizing for throughput, choose the largest possible value, such as `8900`. If you are optimizing for lowest latency, choose a lower value.

> [!IMPORTANT]
> If your cluster uses the OVN-Kubernetes plugin and the network uses a NIC to send and receive unfragmented jumbo frame packets over the network, you must specify `9000` bytes as the MTU value for the NIC so that pods do not fail.

<div>

<div class="title">

Additional resources

</div>

- [Changing cluster network MTU](../../networking/advanced_networking/changing-cluster-network-mtu.md#changing-cluster-network-mtu)

</div>

# Recommended practices for installing large-scale clusters

When installing large clusters or scaling the cluster to larger node counts, set the cluster network `cidr` accordingly in your `install-config.yaml` file before you install the cluster.

<div class="formalpara">

<div class="title">

Example `install-config.yaml` file with a network configuration for a cluster with a large node count

</div>

``` yaml
apiVersion: v1
metadata:
  name: cluster-name
# ...
networking:
  clusterNetwork:
  - cidr: 10.128.0.0/14
    hostPrefix: 23
  machineNetwork:
  - cidr: 10.0.0.0/16
  networkType: OVNKubernetes
  serviceNetwork:
  - 172.30.0.0/16
# ...
```

</div>

- The default cluster network `cidr` `10.128.0.0/14` cannot be used if the cluster size is more than 500 nodes. The `cidr` must be set to `10.128.0.0/12` or `10.128.0.0/10` to support larger node counts beyond 500 nodes.

# Impact of IPsec

Encrypting and decrypting node hosts uses CPU power so performance is affected both in throughput and CPU usage on the nodes when encryption is enabled, regardless of the IP security system being used. To account for performance overhead, review the impact of enabling IPsec.

IPSec encrypts traffic at the IP payload level, before it hits the NIC, protecting fields that would otherwise be used for NIC offloading. This means that some NIC acceleration features might not be usable when IPSec is enabled. This situation leads to decreased throughput and increased CPU usage.

# Additional resources

- [Specifying advanced network configuration](../../installing/installing_aws/ipi/installing-aws-customizations.md#modifying-nwoperator-config-startup_installing-aws-customizations)

- [Cluster Network Operator configuration](../../networking/networking_operators/cluster-network-operator.md#nw-operator-cr_cluster-network-operator)

- [Improving cluster stability in high latency environments using worker latency profiles](../scaling-worker-latency-profiles.md#scaling-worker-latency-profiles)
