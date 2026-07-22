<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Network security can be managed at several levels. At the pod level, network namespaces can prevent containers from seeing other pods or the host system by restricting network access. Network policies give you control over allowing and rejecting connections. You can manage ingress and egress traffic to and from your containerized applications.

# Using network namespaces

OpenShift Container Platform uses software-defined networking (SDN) to provide a unified cluster network that enables communication between containers across the cluster.

Network policy mode, by default, makes all pods in a project accessible from other pods and network endpoints. To isolate one or more pods in a project, you can create `NetworkPolicy` objects in that project to indicate the allowed incoming connections. Using multitenant mode, you can provide project-level isolation for pods and services.

# Isolating pods with network policies

Using *network policies*, you can isolate pods from each other in the same project. Network policies can deny all network access to a pod, only allow connections for the Ingress Controller, reject connections from pods in other projects, or set similar rules for how networks behave.

<div>

<div class="title">

Additional resources

</div>

- [About network policy](../../networking/network_security/network_policy/about-network-policy.md#about-network-policy)

</div>

# Using multiple pod networks

Each running container has only one network interface by default. The Multus CNI plugin lets you create multiple CNI networks, and then attach any of those networks to your pods. In that way, you can do things like separate private data onto a more restricted network and have multiple network interfaces on each node.

<div>

<div class="title">

Additional resources

</div>

- [Using multiple networks](../../networking/multiple_networks/understanding-multiple-networks.md#understanding-multiple-networks)

</div>

# Isolating applications

OpenShift Container Platform enables you to segment network traffic on a single cluster to make multitenant clusters that isolate users, teams, applications, and environments from non-global resources.

# Securing ingress traffic

There are many security implications related to how you configure access to your Kubernetes services from outside of your OpenShift Container Platform cluster. Besides exposing HTTP and HTTPS routes, ingress routing allows you to set up NodePort or LoadBalancer ingress types. NodePort exposes an application’s service API object from each cluster worker. LoadBalancer lets you assign an external load balancer to an associated service API object in your OpenShift Container Platform cluster.

<div>

<div class="title">

Additional resources

</div>

- [Configuring ingress cluster traffic](../../networking/ingress_load_balancing/configuring_ingress_cluster_traffic/configuring-ingress-cluster-traffic-ingress-controller.md#configuring-ingress-cluster-traffic-ingress-controller)

</div>

# Securing egress traffic

OpenShift Container Platform provides the ability to control egress traffic using either a router or firewall method. For example, you can use the IP allow list to control database access. A cluster administrator can assign one or more egress IP addresses to a project by [configuring an egress IP address](../../networking/ovn_kubernetes_network_provider/configuring-egress-ips-ovn.md#configuring-egress-ips-ovn). Likewise, a cluster administrator can prevent egress traffic from going outside of an OpenShift Container Platform cluster using an egress firewall.

By assigning a fixed egress IP address, you can have all outgoing traffic assigned to that IP address for a particular project. With the egress firewall, you can prevent a pod from connecting to an external network, prevent a pod from connecting to an internal network, or limit a pod’s access to specific internal subnets.

<div>

<div class="title">

Additional resources

</div>

- [Configuring an egress firewall for a project](../../networking/network_security/egress_firewall/configuring-egress-firewall-ovn.md#configuring-egress-firewall-ovn)

- [Configuring IPsec encryption](../../networking/network_security/configuring-ipsec-ovn.md#configuring-ipsec-ovn)

</div>
