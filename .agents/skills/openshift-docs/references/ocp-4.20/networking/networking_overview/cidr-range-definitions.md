<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

If your cluster uses OVN-Kubernetes, you must specify non-overlapping ranges for Classless Inter-Domain Routing (CIDR) subnet ranges.

> [!IMPORTANT]
> For OpenShift Container Platform 4.17 and later versions, clusters use `169.254.0.0/17` for IPv4 and `fd69::/112` for IPv6 as the default masquerade subnet. You must avoid these ranges. For upgraded clusters, there is no change to the default masquerade subnet.

> [!TIP]
> You can use the [Red Hat OpenShift Network Calculator](https://access.redhat.com/labs/ocpnc/) to decide your networking needs before setting CIDR range during cluster creation.
>
> You must have a Red Hat account to use the calculator.

The following subnet types are mandatory for a cluster that uses OVN-Kubernetes:

- Join: Uses a join switch to connect gateway routers to distributed routers. A join switch reduces the number of IP addresses for a distributed router. For a cluster that uses the OVN-Kubernetes plugin, an IP address from a dedicated subnet is assigned to any logical port that attaches to the join switch.

- Masquerade: Prevents collisions for identical source and destination IP addresses that are sent from a node as hairpin traffic to the same node after a load balancer makes a routing decision.

- Transit: A transit switch is a type of distributed switch that spans across all nodes in the cluster. A transit switch routes traffic between different zones. For a cluster that uses the OVN-Kubernetes plugin, an IP address from a dedicated subnet is assigned to any logical port that attaches to the transit switch.

> [!NOTE]
> You can change the join, masquerade, and transit CIDR ranges for your cluster as a postinstallation task.

OVN-Kubernetes, the default network provider in OpenShift Container Platform 4.14 and later versions, internally uses the following IP address subnet ranges:

- `V4JoinSubnet`: `100.64.0.0/16`

- `V6JoinSubnet`: `fd98::/64`

- `V4TransitSwitchSubnet`: `100.88.0.0/16`

- `V6TransitSwitchSubnet`: `fd97::/64`

- `defaultV4MasqueradeSubnet`: `169.254.0.0/17`

- `defaultV6MasqueradeSubnet`: `fd69::/112`

> [!IMPORTANT]
> The earlier list includes join, transit, and masquerade IPv4 and IPv6 address subnets. If your cluster uses OVN-Kubernetes, do not include any of these IP address subnet ranges in any other CIDR definitions in your cluster or infrastructure.

<div>

<div class="title">

Additional resources

</div>

- [Configuring OVN-Kubernetes internal IP address subnets](../ovn_kubernetes_network_provider/configure-ovn-kubernetes-subnets.md#configure-ovn-kubernetes-subnets)

</div>

# Machine CIDR

In the Machine classless inter-domain routing (CIDR) field, you must specify the IP address range for machines or cluster nodes.

> [!NOTE]
> You cannot change Machine CIDR ranges after you create your cluster.

The default is `10.0.0.0/16`. This range must not conflict with any connected networks.

<div>

<div class="title">

Additional resources

</div>

- [Cluster Network Operator configuration](../networking_operators/cluster-network-operator.md#nw-operator-cr_cluster-network-operator)

</div>

# Service classless inter-domain routing (CIDR)

In the Service CIDR field, you must specify the IP address range for services.

The range must be large enough to accommodate your workload. The address block must not overlap with any external service accessed from within the cluster. The default is `172.30.0.0/16`.

# Pod classless inter-domain routing (CIDR)

In the pod CIDR field, you must specify the IP address range for pods.

The pod CIDR is the same as the `clusterNetwork` CIDR and the cluster CIDR. The range must be large enough to accommodate your workload. The address block must not overlap with any external service accessed from within the cluster. The default is `10.128.0.0/14`. You can expand the range after cluster installation.

<div>

<div class="title">

Additional resources

</div>

- [Cluster Network Operator configuration](../networking_operators/cluster-network-operator.md#nw-operator-cr_cluster-network-operator)

- [Configuring the cluster network range](../configuring_network_settings/configuring-cluster-network-range.md#configuring-cluster-network-range)

</div>

# Host prefix

In the `hostPrefix` parameter, you must specify the subnet prefix length assigned to pods scheduled to individual machines. The host prefix determines the pod IP address pool for each machine.

For example, if the host prefix is set to `/23`, each machine is assigned a `/23` subnet from the pod CIDR address range. The default is `/23`, allowing 510 cluster nodes and 510 pod IP addresses per node.

Consider another example where you set the `clusterNetwork.cidr` parameter to `10.128.0.0/16`, you define the complete address space for the cluster. This assigns a pool of 65,536 IP addresses to your cluster. If you then set the `hostPrefix` parameter to `/23`, you define a subnet slice to each node in the cluster, where the `/23` slice becomes a subnet of the `/16` subnet network. This assigns 512 IP addresses to each node, where 2 IP addresses get reserved for networking and broadcasting purposes. The following example calculation uses these IP address figures to determine the maximum number of nodes that you can create for your cluster:

``` text
65536 / 512 = 128
```

You can use the [Red Hat OpenShift Network Calculator](https://access.redhat.com/labs/ocpnc/) to calculate the maximum number of nodes for your cluster.

# CIDR ranges for hosted control planes

To successfully deploy hosted control planes on OpenShift Container Platform, define the network environment by using specific Classless Inter-Domain Routing (CIDR) subnet ranges.

The following Classless Inter-Domain Routing (CIDR) subnet ranges are the default settings for hosted control planes:

- `v4InternalSubnet`: 100.65.0.0/16 (OVN-Kubernetes)

- `clusterNetwork`: 10.132.0.0/14 (pod network)

- `serviceNetwork`: 172.31.0.0/16

By using one of the default subnet ranges, you can avoid CIDR overlap with the management cluster and avoid connectivity issues. However, you can use other CIDR subnet ranges if they do not overlap with the management cluster.
