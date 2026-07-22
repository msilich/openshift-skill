<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

As a cluster administrator, you can configure the OVN-Kubernetes Container Network Interface (CNI) network plugin to assign one or more egress IP addresses to a namespace, or to specific pods in a namespace.

# Egress IP address architectural design and implementation

By using the OpenShift Container Platform egress IP address functionality, you can ensure that the traffic from one or more pods in one or more namespaces has a consistent source IP address for services outside the cluster network.

For example, you might have a pod that periodically queries a database that is hosted on a server outside of your cluster. To enforce access requirements for the server, a packet filtering device is configured to allow traffic only from specific IP addresses.

To ensure that you can reliably allow access to the server from only that specific pod, you can configure a specific egress IP address for the pod that makes the requests to the server.

An egress IP address assigned to a namespace is different from an egress router, which is used to send traffic to specific destinations.

In some cluster configurations, application pods and ingress router pods run on the same node. If you configure an egress IP address for an application project in this scenario, the IP address is not used when you send a request to a route from the application project.

> [!IMPORTANT]
> Egress IP addresses must not be configured in any Linux network configuration files, such as `ifcfg-eth0`.

> [!IMPORTANT]
> The assignment of egress IP addresses to control plane nodes with the EgressIP feature is not supported on a cluster provisioned on Amazon Web Services (AWS). For more information, see "BZ#2039656" in the *Additional resources* section.

The following example illustrates the annotation from nodes on several public cloud providers. The annotations are indented for readability.

<div class="formalpara">

<div class="title">

Example `cloud.network.openshift.io/egress-ipconfig` annotation on AWS

</div>

``` yaml
cloud.network.openshift.io/egress-ipconfig: [
  {
    "interface":"eni-078d267045138e436",
    "ifaddr":{"ipv4":"10.0.128.0/18"},
    "capacity":{"ipv4":14,"ipv6":15}
  }
]
```

</div>

The following sections describe the IP address capacity for supported public cloud environments for use in your capacity calculation.

Amazon Web Services (AWS) IP address capacity limits
On AWS, constraints on IP address assignments depend on the instance type configured. For more information, see "IP addresses per network interface per instance type" in the *Additional resources* section.

Google Cloud IP address capacity limits
On Google Cloud, the networking model implements additional node IP addresses through IP address aliasing, rather than IP address assignments. However, IP address capacity maps directly to IP aliasing capacity.

The following capacity limits exist for IP aliasing assignment:

- Per node, the maximum number of IP aliases, both IPv4 and IPv6, is 100.

- Per VPC, the maximum number of IP aliases is unspecified, but OpenShift Container Platform scalability testing reveals the maximum to be approximately 15,000.

For more information, see "Per instance" quotas and "Alias IP ranges overview" in the *Additional resources* section.

Microsoft Azure IP address capacity limits
On Azure, the following capacity limits exist for IP address assignment:

- Per NIC, the maximum number of assignable IP addresses, for both IPv4 and IPv6, is 256.

- Per virtual network, the maximum number of assigned IP addresses cannot exceed 65,536.

For more information, see "Networking limits" in the *Additional resources* section.

# Additional resources

- [BZ#2039656 (Red Hat Bugzilla)](https://bugzilla.redhat.com/show_bug.cgi?id=2039656)

- [Per instance (Google Cloud documentation)](https://cloud.google.com/vpc/docs/quota#per_instance)

- [Alias IP ranges overview (Google Cloud documentation)](https://cloud.google.com/vpc/docs/alias-ip)

- [Networking limits (Microsoft Azure documentation)](https://docs.microsoft.com/en-us/azure/azure-resource-manager/management/azure-subscription-service-limits?toc=/azure/virtual-network/toc.json#networking-limits)

- [IP addresses per network interface per instance type (AWS documentation)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-eni.html#AvailableIpPerENI)

## Platform support

The Egress IP address feature that runs on a primary host network is supported on specific platforms.

The following table shows supported platforms for egress IP on primary host networks:

| Platform | Supported |
|----|----|
| Bare metal | Yes |
| VMware vSphere | Yes |
| Red Hat OpenStack Platform (RHOSP) | Yes |
| Amazon Web Services (AWS) | Yes |
| Google Cloud | Yes |
| Microsoft Azure | Yes |
| IBM Z® and IBM® LinuxONE | Yes |
| IBM Z® and IBM® LinuxONE for Red Hat Enterprise Linux (RHEL) KVM | Yes |
| IBM Power® | Yes |
| Nutanix | Yes |

The Egress IP address feature that runs on secondary host networks is supported on the following platform:

| Platform   | Supported |
|------------|-----------|
| Bare metal | Yes       |

## Public cloud platform considerations

Typically, public cloud providers place a limit on egress IP addresses. You must understand the existence of a constraint on the absolute number of assignable IP addresses per node for clusters provisioned on public cloud infrastructure.

The maximum number of assignable IP addresses per node, or the *IP capacity*, can be described in the following formula:

``` text
IP capacity = public cloud default capacity - sum(current IP assignments)
```

While the Egress IP addresses capability manages the IP address capacity per node, ensure you plan for this constraint in your deployments. For example, if a public cloud provider limits IP address capacity to 10 IP addresses per node, and you have 8 nodes, the total number of assignable IP addresses is only 80. To achieve a higher IP address capacity, you would need to allocate additional nodes. For example, if you needed 150 assignable IP addresses, you would need to allocate 7 additional nodes.

To confirm the IP capacity and subnets for any node in your public cloud environment, you can enter the `oc get node <node_name> -o yaml` command. The `cloud.network.openshift.io/egress-ipconfig` annotation includes capacity and subnet information for the node.

The annotation value is an array with a single object with fields that provide the following information for the primary network interface:

- `interface`: Specifies the interface ID on AWS and Azure and the interface name on Google Cloud.

- `ifaddr`: Specifies the subnet mask for one or both IP address families.

- `capacity`: Specifies the IP address capacity for the node. On AWS, the IP address capacity is provided per IP address family. On Azure and Google Cloud, the IP address capacity includes both IPv4 and IPv6 addresses.

Automatic attachment and detachment of egress IP addresses for traffic between nodes are available. Traffic from many pods in namespaces can have a consistent source IP address to locations outside of the cluster.

> [!NOTE]
> When an RHOSP cluster administrator assigns a floating IP to the reservation port, OpenShift Container Platform cannot delete the reservation port. The `CloudPrivateIPConfig` object cannot perform delete and move operations until an RHOSP cluster administrator unassigns the floating IP from the reservation port.

The following examples illustrate the annotation from nodes on several public cloud providers. The annotations are indented for readability.

<div class="formalpara">

<div class="title">

Example `cloud.network.openshift.io/egress-ipconfig` annotation on AWS

</div>

``` yaml
cloud.network.openshift.io/egress-ipconfig: [
  {
    "interface":"eni-078d267045138e436",
    "ifaddr":{"ipv4":"10.0.128.0/18"},
    "capacity":{"ipv4":14,"ipv6":15}
  }
]
```

</div>

<div class="formalpara">

<div class="title">

Example `cloud.network.openshift.io/egress-ipconfig` annotation on Google Cloud

</div>

``` yaml
cloud.network.openshift.io/egress-ipconfig: [
  {
    "interface":"nic0",
    "ifaddr":{"ipv4":"10.0.128.0/18"},
    "capacity":{"ip":14}
  }
]
```

</div>

## Considerations for using an egress IP address on additional network interfaces

In OpenShift Container Platform, egress IP addresses provide administrators a way to control network traffic. Egress IP addresses can be used with a `br-ex` Open vSwitch (OVS) bridge interface and any physical interface that has IP connectivity enabled.

You can inspect your network interface type by running the following command:

``` terminal
$ ip -details link show
```

The primary network interface is assigned a node IP address which also contains a subnet mask. Information for this node IP address can be retrieved from the Kubernetes node object for each node within your cluster by inspecting the `k8s.ovn.org/node-primary-ifaddr` annotation. In an IPv4 cluster, this annotation is similar to the following example: `"k8s.ovn.org/node-primary-ifaddr: {"ipv4":"192.168.111.23/24"}"`.

If the egress IP address is not within the subnet of the primary network interface subnet, you can use an egress IP address on another Linux network interface that is not of the primary network interface type. By doing so, OpenShift Container Platform administrators are provided with a greater level of control over networking aspects such as routing, addressing, segmentation, and security policies. This feature provides users with the option to route workload traffic over specific network interfaces for purposes such as traffic segmentation or meeting specialized requirements.

If the egress IP address is not within the subnet of the primary network interface, then the selection of another network interface for egress traffic might occur if they are present on a node.

You can determine which other network interfaces might support egress IP address addresses by inspecting the `k8s.ovn.org/host-cidrs` Kubernetes node annotation. This annotation contains the addresses and subnet mask found for the primary network interface. The annotation also contains additional network interface addresses and subnet mask information. These addresses and subnet masks are assigned to network interfaces that use the longest prefix match routing mechanism to determine which network interface supports the egress IP address. For more information, see "Longest prefix match routing" in the *Additional resources* section.

> [!NOTE]
> OVN-Kubernetes provides a mechanism to control and direct outbound network traffic from specific namespaces and pods. This ensures that it exits the cluster through a particular network interface and with a specific egress IP address.

As an administrator who wants an egress IP address and traffic to route over a particular interface that is not the primary network interface, you must meet the following conditions:

- OpenShift Container Platform is installed on a bare-metal cluster. This feature is disabled within a cloud or a hypervisor environment.

- Your OpenShift Container Platform pods are not configured as *host-networked*.

- You understand that if a network interface is removed or if the IP address and subnet mask which allows the egress IP address to be hosted on the interface is removed, reconfiguration of the egress IP address occurs. Consequently, the egress IP address might get assigned to another node and interface.

- If you use an Egress IP address on a secondary network interface card (NIC), you must use the Node Tuning Operator to enable IP forwarding on the secondary NIC.

- You configured a NIC with routes by ensuring a gateway exists in the main routing table. As a postinstallation task, Red Hat does not support configuring a NIC on a cluster that uses OVN-Kubernetes.

- Routes associated with an egress interface get copied from the main routing table to the routing table that was created to support the Egress IP object.

<!-- -->

- [Longest prefix match routing (NetworkLessons documentation)](https://networklessons.com/cisco/ccna-200-301/longest-prefix-match-routing)

## Architectural diagram of an egress IP address configuration

To better understand egress IP address configuration, reference the architectural diagram.

The following diagram shows an egress IP address configuration. The diagram describes four pods in two different namespaces running on three nodes in a cluster. The nodes are assigned IP addresses from the `192.168.126.0/18` CIDR block on the host network.

<figure>
<img src="data:image/svg+xml;base64,PHN2ZyBpZD0iYWRmYTcxNDQtMjdhOC00N2NkLTg2OTUtZTVlODA3NDA3NGRjIiBkYXRhLW5hbWU9ImFydHdvcmsiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgd2lkdGg9Ijc2MCIgaGVpZ2h0PSI1MjYuMjE4Ij48ZGVmcz48c3R5bGU+LmIwMmJhNjUwLWQ3MmQtNDA5YS1hYjMwLWE0YzA0ZjYyYWQyYiwuYmQ1MjJhMzMtMTVmYy00ZGM3LWFhYmYtNGFhZGMwM2U2OTk0LC5lYmZhNjdiNi1lM2VmLTQ5YWItYjM5My04Nzc1YjYzZjdlZGIsLmY5ZDI3M2FhLWM0NTQtNDA3Ni1iYWIwLTJlMDFmYWZkZWNlNXtmaWxsOm5vbmV9LmIwMmJhNjUwLWQ3MmQtNDA5YS1hYjMwLWE0YzA0ZjYyYWQyYiwuYmQ1MjJhMzMtMTVmYy00ZGM3LWFhYmYtNGFhZGMwM2U2OTk0LC5lYmZhNjdiNi1lM2VmLTQ5YWItYjM5My04Nzc1YjYzZjdlZGJ7c3Ryb2tlOiMwNmN9LmIwMmJhNjUwLWQ3MmQtNDA5YS1hYjMwLWE0YzA0ZjYyYWQyYiwuYmQ1MjJhMzMtMTVmYy00ZGM3LWFhYmYtNGFhZGMwM2U2OTk0LC5lYmZhNjdiNi1lM2VmLTQ5YWItYjM5My04Nzc1YjYzZjdlZGIsLmY5ZDI3M2FhLWM0NTQtNDA3Ni1iYWIwLTJlMDFmYWZkZWNlNXtzdHJva2UtbGluZWNhcDpyb3VuZDtzdHJva2UtbGluZWpvaW46cm91bmR9LmIwMmJhNjUwLWQ3MmQtNDA5YS1hYjMwLWE0YzA0ZjYyYWQyYiwuZjlkMjczYWEtYzQ1NC00MDc2LWJhYjAtMmUwMWZhZmRlY2U1e3N0cm9rZS13aWR0aDoycHh9LmY5ZDI3M2FhLWM0NTQtNDA3Ni1iYWIwLTJlMDFmYWZkZWNlNXtzdHJva2U6IzRjYjZkNn0uYjcyZDNjYmMtNmJmYy00ZWZjLTkxN2ItOGRmOTU3YTUyMTY0e2ZpbGw6I2ZmZn0uYTdlMDNmYjQtNDQxYS00MmVkLWIxODYtZWI4YmZkMTMzMWYye2ZvbnQtc2l6ZToxMnB4O2ZvbnQtZmFtaWx5OlJlZEhhdFRleHQsJnF1b3Q7UmVkIEhhdCBUZXh0JnF1b3Q7LE92ZXJwYXNzLCZxdW90O0hlbHZldGljYSBOZXVlJnF1b3Q7LEFyaWFsLHNhbnMtc2VyaWY7Zm9udC13ZWlnaHQ6NTAwO2ZpbGw6IzE1MTUxNX0uYWM4MzAyYTEtZjliNS00ODU4LWJlMWQtYTc5ZTlhY2FjZGYyLC5lMTg4MTg2ZS03MmJlLTQwMTgtOWE0NC01MzVjMGEwMTQ4M2R7ZmlsbDojMTUxNTE1fS5hYjllOTU4NS05ZGNlLTQyMTUtYjlhNS1lNWY1MzQ5OGRiOGZ7ZmlsbDojZThlOGU4fS5hYzgzMDJhMS1mOWI1LTQ4NTgtYmUxZC1hNzllOWFjYWNkZjJ7Zm9udC1zaXplOjE0cHg7Zm9udC1mYW1pbHk6UmVkSGF0VGV4dCwmcXVvdDtSZWQgSGF0IFRleHQmcXVvdDssT3ZlcnBhc3MsJnF1b3Q7SGVsdmV0aWNhIE5ldWUmcXVvdDssQXJpYWwsc2Fucy1zZXJpZjtmb250LXdlaWdodDo3MDB9LmI4MTRiMDM2LWZjNmEtNDI5NC1iZWVmLWYyZWJjMzRmZTg0ZCwuZTE4ODE4NmUtNzJiZS00MDE4LTlhNDQtNTM1YzBhMDE0ODNke2ZvbnQtc2l6ZToxMXB4O2ZvbnQtZmFtaWx5OkxpYmVyYXRpb25Nb25vLCZxdW90O0xpYmVyYXRpb24gTW9ubyZxdW90OyxDb25zb2xhcyxNb25hY28sJnF1b3Q7QW5kYWxlIE1vbm8mcXVvdDssbW9ub3NwYWNlfS5iODE0YjAzNi1mYzZhLTQyOTQtYmVlZi1mMmViYzM0ZmU4NGR7Zm9udC13ZWlnaHQ6NDAwfS5iNTkyNjQwYi1jMzE2LTQ3NWUtYmNlNi1iN2EzNzg5ZjM2YTV7ZmlsbDojZDVkNWQ1fS5iZDUyMmEzMy0xNWZjLTRkYzctYWFiZi00YWFkYzAzZTY5OTR7c3Ryb2tlLWRhc2hhcnJheTozLjQgMy40fTwvc3R5bGU+PC9kZWZzPjxwYXRoIGNsYXNzPSJiMDJiYTY1MC1kNzJkLTQwOWEtYWIzMC1hNGMwNGY2MmFkMmIiIGQ9Ik00MjQuNzc0IDExNy41aDM0LjgxN3YzMjEuNzE4aC0zNC40OTgiLz48cGF0aCBjbGFzcz0iZjlkMjczYWEtYzQ1NC00MDc2LWJhYjAtMmUwMWZhZmRlY2U1IiBkPSJNNDI0LjYxNCA5Ny41MDFoMTY0Ljk3N3YzNjEuNzE3SDQyNC45MzMiLz48cGF0aCBjbGFzcz0iYjcyZDNjYmMtNmJmYy00ZWZjLTkxN2ItOGRmOTU3YTUyMTY0IiBkPSJNNDY0LjE4NSA0NDkuMDA1aDkxLjA1OHYyMC40MjZoLTkxLjA1OHoiLz48dGV4dCBjbGFzcz0iYTdlMDNmYjQtNDQxYS00MmVkLWIxODYtZWI4YmZkMTMzMWYyIiB0cmFuc2Zvcm09InRyYW5zbGF0ZSg0NjcuMDg5IDQ2Mi45NDYpIj4xOTIuMTY4LjEyNi4xMDI8L3RleHQ+PHBhdGggY2xhc3M9ImFiOWU5NTg1LTlkY2UtNDIxNS1iOWE1LWU1ZjUzNDk4ZGI4ZiIgZD0iTS4wNyAzNzQuMjE4aDQyNXYxMzVILjA3eiIvPjx0ZXh0IGNsYXNzPSJhYzgzMDJhMS1mOWI1LTQ4NTgtYmUxZC1hNzllOWFjYWNkZjIiIHRyYW5zZm9ybT0idHJhbnNsYXRlKDIwLjA3IDQwNi4xNDYpIj5Ob2RlIDM8dHNwYW4gY2xhc3M9ImI4MTRiMDM2LWZjNmEtNDI5NC1iZWVmLWYyZWJjMzRmZTg0ZCI+PHRzcGFuIHg9IjAiIHk9IjI2Ij5tZXRhOjwvdHNwYW4+PC90c3Bhbj48L3RleHQ+PHRleHQgY2xhc3M9ImUxODgxODZlLTcyYmUtNDAxOC05YTQ0LTUzNWMwYTAxNDgzZCIgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoMjYuNjgyIDQ0NS4xNDUpIj5uYW1lOiBub2RlMzwvdGV4dD48dGV4dCBjbGFzcz0iZTE4ODE4NmUtNzJiZS00MDE4LTlhNDQtNTM1YzBhMDE0ODNkIiB0cmFuc2Zvcm09InRyYW5zbGF0ZSgyNi42NDUgNDU4LjE0NikiPmxhYmVsczo8L3RleHQ+PHRleHQgY2xhc3M9ImUxODgxODZlLTcyYmUtNDAxOC05YTQ0LTUzNWMwYTAxNDgzZCIgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoMzMuMjE5IDQ3MS4xNDYpIj5rOHMub3ZuLm9yZy9lZ3Jlc3MtYXNzaWduYWJsZTogJnF1b3Q7JnF1b3Q7PC90ZXh0Pjx0ZXh0IGNsYXNzPSJhN2UwM2ZiNC00NDFhLTQyZWQtYjE4Ni1lYjhiZmQxMzMxZjIiIHRyYW5zZm9ybT0idHJhbnNsYXRlKDQ2Ny4wODkgMTUyLjkwNCkiPlBvZCBuZXR3b3JrPHRzcGFuIHg9IjAiIHk9IjE1Ij4xMC4xMjguMC4wLzE0PC90c3Bhbj48L3RleHQ+PHRleHQgY2xhc3M9ImE3ZTAzZmI0LTQ0MWEtNDJlZC1iMTg2LWViOGJmZDEzMzFmMiIgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoNTk3LjA4OSAxNTIuOTA0KSI+SW5mcmFzdHJ1Y3R1cmUgbmV0d29yazx0c3BhbiB4PSIwIiB5PSIxNSI+MTkyLjE2OC4xMjYuMC8xODwvdHNwYW4+PC90ZXh0PjxwYXRoIGNsYXNzPSJhYjllOTU4NS05ZGNlLTQyMTUtYjlhNS1lNWY1MzQ5OGRiOGYiIGQ9Ik02MzMuMDcgMjIwaDEyN3Y5NWgtMTI3eiIvPjx0ZXh0IGNsYXNzPSJhYzgzMDJhMS1mOWI1LTQ4NTgtYmUxZC1hNzllOWFjYWNkZjIiIHRyYW5zZm9ybT0idHJhbnNsYXRlKDY1My4wNyAyNTEuNzg4KSI+RXh0ZXJuYWw8dHNwYW4geD0iMCIgeT0iMTUiPnNlcnZpY2U8L3RzcGFuPjwvdGV4dD48cGF0aCBjbGFzcz0iYjAyYmE2NTAtZDcyZC00MDlhLWFiMzAtYTRjMDRmNjJhZDJiIiBkPSJNNDU5LjU5MSAyNjBINDI1LjA3Ii8+PHBhdGggc3Ryb2tlPSIjZmZmIiBzdHJva2Utd2lkdGg9IjgiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgZmlsbD0ibm9uZSIgZD0iTTQ2OS41OTEgMjQwSDQyNS4wNyIvPjxwYXRoIGNsYXNzPSJmOWQyNzNhYS1jNDU0LTQwNzYtYmFiMC0yZTAxZmFmZGVjZTUiIGQ9Ik01ODkuNTkxIDI0MEg0MjUuMDdNNTg5LjU5MSAyNjcuNWgzMy44MDMiLz48cGF0aCBmaWxsPSIjNGNiNmQ2IiBkPSJNNjIxLjkzNSAyNzIuNDg2bDguNjM1LTQuOTg2LTguNjM1LTQuOTg2djkuOTcyeiIvPjxwYXRoIGNsYXNzPSJiNzJkM2NiYy02YmZjLTRlZmMtOTE3Yi04ZGY5NTdhNTIxNjQiIGQ9Ik00NjQuMTg1IDg3LjcwNmg4My41NTh2MjAuNDI2aC04My41NTh6Ii8+PHRleHQgY2xhc3M9ImE3ZTAzZmI0LTQ0MWEtNDJlZC1iMTg2LWViOGJmZDEzMzFmMiIgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoNDY3LjA4OSAxMDEuNjQ3KSI+MTkyLjE2OC4xMjYuMTA8L3RleHQ+PHBhdGggY2xhc3M9ImFiOWU5NTg1LTlkY2UtNDIxNS1iOWE1LWU1ZjUzNDk4ZGI4ZiIgZD0iTS4wNyA1NWg0MjV2MTM1SC4wN3oiLz48cGF0aCBjbGFzcz0iYjU5MjY0MGItYzMxNi00NzVlLWJjZTYtYjdhMzc4OWYzNmE1IiBkPSJNMzk0Ljk5NiA0NDQuMjE4SDI2NS4wN2wuMDc1LTcwSDM5NS4wN2wtLjA3NCA3MHoiLz48cGF0aCBjbGFzcz0iYWI5ZTk1ODUtOWRjZS00MjE1LWI5YTUtZTVmNTM0OThkYjhmIiBkPSJNMzk0Ljk5NiAzMzkuMjE4SDI2NS4wN2wuMDc1IDM1SDM5NS4wN2wtLjA3NC0zNXoiLz48cGF0aCBjbGFzcz0iYjU5MjY0MGItYzMxNi00NzVlLWJjZTYtYjdhMzc4OWYzNmE1IiBkPSJNMjY1LjEwNyA1NWgxMjkuOTI1djEzNUgyNjUuMTA3eiIvPjxwYXRoIGNsYXNzPSJhYjllOTU4NS05ZGNlLTQyMTUtYjlhNS1lNWY1MzQ5OGRiOGYiIGQ9Ik0zOTQuOTk2IDIwSDI2NS4wN2wuMDc1IDM1SDM5NS4wN2wtLjA3NC0zNXoiLz48cGF0aCBjbGFzcz0iZWJmYTY3YjYtZTNlZi00OWFiLWIzOTMtODc3NWI2M2Y3ZWRiIiBkPSJNMzg1LjA3IDE0MGgxLjUiLz48cGF0aCBjbGFzcz0iYmQ1MjJhMzMtMTVmYy00ZGM3LWFhYmYtNGFhZGMwM2U2OTk0IiBkPSJNMzg5Ljk3IDE0MGgxMS45Ii8+PHBhdGggY2xhc3M9ImViZmE2N2I2LWUzZWYtNDlhYi1iMzkzLTg3NzViNjNmN2VkYiIgZD0iTTQwMy41NyAxNDBoMS41di0xLjUiLz48cGF0aCBzdHJva2UtZGFzaGFycmF5PSIyLjggMi44IiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIHN0cm9rZT0iIzA2YyIgZmlsbD0ibm9uZSIgZD0iTTQwNS4wNyAxMzUuN1Y5Ny45Ii8+PHBhdGggY2xhc3M9ImViZmE2N2I2LWUzZWYtNDlhYi1iMzkzLTg3NzViNjNmN2VkYiIgZD0iTTQwNS4wNyA5Ni41Vjk1aC0xLjUiLz48cGF0aCBjbGFzcz0iYmQ1MjJhMzMtMTVmYy00ZGM3LWFhYmYtNGFhZGMwM2U2OTk0IiBkPSJNNDAwLjE3IDk1aC0xMS45Ii8+PHBhdGggY2xhc3M9ImViZmE2N2I2LWUzZWYtNDlhYi1iMzkzLTg3NzViNjNmN2VkYiIgZD0iTTM4Ni41NyA5NWgtMS41TTQyNS4wNyAxMTcuNWgtMS41Ii8+PHBhdGggc3Ryb2tlLWRhc2hhcnJheT0iMy4zIDMuMyIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBzdHJva2U9IiMwNmMiIGZpbGw9Im5vbmUiIGQ9Ik00MjAuMjcgMTE3LjVoLTExLjU1Ii8+PHBhdGggY2xhc3M9ImViZmE2N2I2LWUzZWYtNDlhYi1iMzkzLTg3NzViNjNmN2VkYiIgZD0iTTQwNy4wNyAxMTcuNWgtMS41Ii8+PHBhdGggY2xhc3M9ImI3MmQzY2JjLTZiZmMtNGVmYy05MTdiLThkZjk1N2E1MjE2NCIgZD0iTTI3NS4wNyAzOTQuMjE4aDExMHY0MGgtMTEweiIvPjx0ZXh0IGNsYXNzPSJhN2UwM2ZiNC00NDFhLTQyZWQtYjE4Ni1lYjhiZmQxMzMxZjIiIHRyYW5zZm9ybT0idHJhbnNsYXRlKDMxNS4yNTEgNDE3LjU0MikiPnBvZDQ8L3RleHQ+PHBhdGggY2xhc3M9ImI3MmQzY2JjLTZiZmMtNGVmYy05MTdiLThkZjk1N2E1MjE2NCIgZD0iTTI3NS4wNyAxMjBoMTEwdjQwaC0xMTB6Ii8+PHRleHQgY2xhc3M9ImE3ZTAzZmI0LTQ0MWEtNDJlZC1iMTg2LWViOGJmZDEzMzFmMiIgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoMzE1LjczNiAxNDMuMzIzKSI+cG9kMjwvdGV4dD48cGF0aCBjbGFzcz0iYjcyZDNjYmMtNmJmYy00ZWZjLTkxN2ItOGRmOTU3YTUyMTY0IiBkPSJNMjc1LjA3IDc1aDExMHY0MGgtMTEweiIvPjx0ZXh0IGNsYXNzPSJhN2UwM2ZiNC00NDFhLTQyZWQtYjE4Ni1lYjhiZmQxMzMxZjIiIHRyYW5zZm9ybT0idHJhbnNsYXRlKDMxNy4xMDQgOTguMzIzKSI+cG9kMTwvdGV4dD48dGV4dCBjbGFzcz0iYWM4MzAyYTEtZjliNS00ODU4LWJlMWQtYTc5ZTlhY2FjZGYyIiB0cmFuc2Zvcm09InRyYW5zbGF0ZSgyMC4wNyA4Ni45MjgpIj5Ob2RlIDE8dHNwYW4gY2xhc3M9ImI4MTRiMDM2LWZjNmEtNDI5NC1iZWVmLWYyZWJjMzRmZTg0ZCI+PHRzcGFuIHg9IjAiIHk9IjI2Ij5tZXRhOjwvdHNwYW4+PC90c3Bhbj48L3RleHQ+PHRleHQgY2xhc3M9ImUxODgxODZlLTcyYmUtNDAxOC05YTQ0LTUzNWMwYTAxNDgzZCIgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoMjYuNjgyIDEyNS45MjgpIj5uYW1lOiBub2RlMTwvdGV4dD48dGV4dCBjbGFzcz0iZTE4ODE4NmUtNzJiZS00MDE4LTlhNDQtNTM1YzBhMDE0ODNkIiB0cmFuc2Zvcm09InRyYW5zbGF0ZSgyNi42NDUgMTM4LjkyOCkiPmxhYmVsczo8L3RleHQ+PHRleHQgY2xhc3M9ImUxODgxODZlLTcyYmUtNDAxOC05YTQ0LTUzNWMwYTAxNDgzZCIgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoMzMuMjE5IDE1MS45MjgpIj5rOHMub3ZuLm9yZy9lZ3Jlc3MtYXNzaWduYWJsZTogJnF1b3Q7JnF1b3Q7PC90ZXh0Pjx0ZXh0IGNsYXNzPSJhN2UwM2ZiNC00NDFhLTQyZWQtYjE4Ni1lYjhiZmQxMzMxZjIiIHRyYW5zZm9ybT0idHJhbnNsYXRlKDI5Ni4xMTcgNDMuNTMxKSI+bmFtZXNwYWNlMTwvdGV4dD48dGV4dCBjbGFzcz0iYTdlMDNmYjQtNDQxYS00MmVkLWIxODYtZWI4YmZkMTMzMWYyIiB0cmFuc2Zvcm09InRyYW5zbGF0ZSgyOTQuNzQ5IDM2Mi43NDIpIj5uYW1lc3BhY2UyPC90ZXh0PjxnPjx0ZXh0IHRyYW5zZm9ybT0idHJhbnNsYXRlKDY3MS4wMTIgNTA5LjIzNSkiIGZvbnQtc2l6ZT0iMTAiIGZpbGw9IiNmM2YzZjMiIGZvbnQtZmFtaWx5PSJSZWRIYXRUZXh0LCZxdW90O1JlZCBIYXQgVGV4dCZxdW90OyxPdmVycGFzcywmcXVvdDtIZWx2ZXRpY2EgTmV1ZSZxdW90OyxBcmlhbCxzYW5zLXNlcmlmIj4xMjFfT3BlblNoaWZ0XzEwMjA8L3RleHQ+PHBhdGggZmlsbD0ibm9uZSIgZD0iTTAgNDg2LjIxOGg3NjB2NDBIMHoiLz48L2c+PGc+PHBhdGggY2xhc3M9ImFiOWU5NTg1LTlkY2UtNDIxNS1iOWE1LWU1ZjUzNDk4ZGI4ZiIgZD0iTS4wNyAyMjBoNDI1djk1SC4wN3oiLz48dGV4dCBjbGFzcz0iYWM4MzAyYTEtZjliNS00ODU4LWJlMWQtYTc5ZTlhY2FjZGYyIiB0cmFuc2Zvcm09InRyYW5zbGF0ZSgyMC4wNyAyNTEuOTI4KSI+Tm9kZSAyPHRzcGFuIGNsYXNzPSJiODE0YjAzNi1mYzZhLTQyOTQtYmVlZi1mMmViYzM0ZmU4NGQiPjx0c3BhbiB4PSIwIiB5PSIyNiI+bWV0YTo8L3RzcGFuPjwvdHNwYW4+PC90ZXh0Pjx0ZXh0IGNsYXNzPSJlMTg4MTg2ZS03MmJlLTQwMTgtOWE0NC01MzVjMGEwMTQ4M2QiIHRyYW5zZm9ybT0idHJhbnNsYXRlKDI2LjY4MiAyOTAuOTI4KSI+bmFtZTogbm9kZTI8L3RleHQ+PC9nPjxwYXRoIGNsYXNzPSJiNTkyNjQwYi1jMzE2LTQ3NWUtYmNlNi1iN2EzNzg5ZjM2YTUiIGQ9Ik0zOTQuOTk2IDI5MEgyNjUuMDdsLjA3NS03MEgzOTUuMDdsLS4wNzQgNzB6Ii8+PHBhdGggY2xhc3M9ImFiOWU5NTg1LTlkY2UtNDIxNS1iOWE1LWU1ZjUzNDk4ZGI4ZiIgZD0iTTM5NC45OTYgMTkwSDI2NS4wN2wuMDc1IDMwSDM5NS4wN2wtLjA3NC0zMHoiLz48Zz48cGF0aCBjbGFzcz0iZWJmYTY3YjYtZTNlZi00OWFiLWIzOTMtODc3NWI2M2Y3ZWRiIiBkPSJNNDI1LjA3IDI2MGgtMS41Ii8+PHBhdGggc3Ryb2tlLWRhc2hhcnJheT0iMi44NDYgMi44NDYiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgc3Ryb2tlPSIjMDZjIiBmaWxsPSJub25lIiBkPSJNNDIwLjcyNCAyNjBoLTMyLjczMSIvPjxwYXRoIGNsYXNzPSJlYmZhNjdiNi1lM2VmLTQ5YWItYjM5My04Nzc1YjYzZjdlZGIiIGQ9Ik0zODYuNTcgMjYwaC0xLjUiLz48L2c+PHBhdGggY2xhc3M9ImI3MmQzY2JjLTZiZmMtNGVmYy05MTdiLThkZjk1N2E1MjE2NCIgZD0iTTI3NS4wNyAyNDBoMTEwdjQwaC0xMTB6Ii8+PHRleHQgY2xhc3M9ImE3ZTAzZmI0LTQ0MWEtNDJlZC1iMTg2LWViOGJmZDEzMzFmMiIgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoMzE1LjUxNCAyNjMuMzIzKSI+cG9kMzwvdGV4dD48L3N2Zz4=" alt="Architectural diagram for the egress IP feature" />
</figure>

Both Node 1 and Node 3 are labeled with `k8s.ovn.org/egress-assignable: ""` and thus available for the assignment of egress IP addresses.

The dashed lines in the diagram depict the traffic flow from pod1, pod2, and pod3 traveling through the pod network to egress the cluster from Node 1 and Node 3. When an external service receives traffic from any of the pods selected by the example `EgressIP` object, the source IP address is either `192.168.126.10` or `192.168.126.102`. The traffic is balanced roughly equally between these two nodes.

Based on the diagram, the following manifest file defines namespaces:

<div class="formalpara">

<div class="title">

Namespace objects

</div>

``` yaml
apiVersion: v1
kind: Namespace
metadata:
  name: namespace1
  labels:
    env: prod
---
apiVersion: v1
kind: Namespace
metadata:
  name: namespace2
  labels:
    env: prod
```

</div>

Based on the diagram, the following `EgressIP` object describes a configuration that selects all pods in any namespace with the `env` label set to `prod`. The egress IP addresses for the selected pods are `192.168.126.10` and `192.168.126.102`.

<div class="formalpara">

<div class="title">

`EgressIP` object

</div>

``` yaml
apiVersion: k8s.ovn.org/v1
kind: EgressIP
metadata:
  name: egressips-prod
spec:
  egressIPs:
  - 192.168.126.10
  - 192.168.126.102
  namespaceSelector:
    matchLabels:
      env: prod
status:
  items:
  - node: node1
    egressIP: 192.168.126.10
  - node: node3
    egressIP: 192.168.126.102
```

</div>

For the configuration in the previous example, OpenShift Container Platform assigns both egress IP addresses to the available nodes. The `status` field reflects whether and where the egress IP addresses are assigned.

# EgressIP object

You can view YAML files to better understand how you can effectively configure an `EgressIP` object to better meet your needs.

When the `EgressIP` namespace selector matches the label on multiple namespaces, consider the following behaviors:

- All traffic for selected pods must pass through a single node. During times of high traffic, the network interface of the node might experience performance issues.

- An error in a label selector might change the outbound IP address for many cluster namespaces.

- Only a cluster administrator can create or change cluster-scoped objects.

- Packets must move from a pod that exists in a node to the named host node that is referenced in the `EgressIP` object. This approach adds a network hop.

> [!IMPORTANT]
> Do not create egress rules, such as a single label selector, that forces all namespaces that exist in a cluster to use the same outbound IP address. This configuration can cause the node that hosts the IP address to crash during times of high network traffic.

The following YAML describes the API for the `EgressIP` object. The scope of the object is cluster-wide and is not created in a namespace.

``` yaml
apiVersion: k8s.ovn.org/v1
kind: EgressIP
metadata:
  name: <name>
spec:
  egressIPs:
  - <ip_address>
  namespaceSelector:
    ...
  podSelector:
    ...
```

where:

`<name>`
Specifies the name for the `EgressIPs` object.

`<egressIPs>`
Specifies an array of one or more IP addresses.

`<namespaceSelector>`
Specifies one or more selectors for the namespaces to associate the egress IP addresses with.

`<podSelector>`
Optional parameter. Specifies one or more selectors for pods in the specified namespaces to associate egress IP addresses with. Applying these selectors allows for the selection of a subset of pods within a namespace.

The following YAML describes the stanza for the namespace selector:

<div class="formalpara">

<div class="title">

Namespace selector stanza

</div>

``` yaml
namespaceSelector:
  matchLabels:
    <label_name>: <label_value>
```

</div>

where:

`<namespaceSelector>`
Specifies one or more matching rules for namespaces. If more than one match rule is provided, all matching namespaces are selected.

The following YAML describes the optional stanza for the pod selector:

<div class="formalpara">

<div class="title">

Pod selector stanza

</div>

``` yaml
podSelector:
  matchLabels:
    <label_name>: <label_value>
```

</div>

where:

`<podSelector>`
Optional parameter. Specifies one or more matching rules for pods in the namespaces that match the specified `namespaceSelector` rules. If specified, only pods that match are selected. Others pods in the namespace are not selected.

In the following example, the `EgressIP` object associates the `192.168.126.11` and `192.168.126.102` egress IP addresses with pods that have the `app` label set to `web` and are in the namespaces that have the `env` label set to `prod`:

<div class="formalpara">

<div class="title">

Example `EgressIP` object

</div>

``` yaml
apiVersion: k8s.ovn.org/v1
kind: EgressIP
metadata:
  name: egress-group1
spec:
  egressIPs:
  - 192.168.126.11
  - 192.168.126.102
  podSelector:
    matchLabels:
      app: web
  namespaceSelector:
    matchLabels:
      env: prod
```

</div>

In the following example, the `EgressIP` object associates the `192.168.127.30` and `192.168.127.40` egress IP addresses with any pods that do not have the `environment` label set to `development`:

<div class="formalpara">

<div class="title">

Example `EgressIP` object

</div>

``` yaml
apiVersion: k8s.ovn.org/v1
kind: EgressIP
metadata:
  name: egress-group2
spec:
  egressIPs:
  - 192.168.127.30
  - 192.168.127.40
  namespaceSelector:
    matchExpressions:
    - key: environment
      operator: NotIn
      values:
      - development
```

</div>

# Assignment of egress IPs to a namespace, nodes, and pods

To assign one or more egress IPs to a namespace or specific pods in a namespace, you must meet specific conditions.

- At least one node in your cluster must have the `k8s.ovn.org/egress-assignable: ""` label.

- An `EgressIP` object exists that defines one or more egress IP addresses to use as the source IP address for traffic leaving the cluster from pods in a namespace.

> [!IMPORTANT]
> If you create `EgressIP` objects prior to labeling any nodes in your cluster for egress IP assignment, OpenShift Container Platform might assign every egress IP address to the first node with the `k8s.ovn.org/egress-assignable: ""` label.
>
> To ensure that egress IP addresses are widely distributed across nodes in the cluster, always apply the label to the nodes you intend to host the egress IP addresses before creating any `EgressIP` objects.

When creating an `EgressIP` object, the following conditions apply to nodes that are labeled with the `k8s.ovn.org/egress-assignable: ""` label:

- An egress IP address is never assigned to more than one node at a time.

- An egress IP address is equally balanced between available nodes that can host the egress IP address.

- If the `spec.EgressIPs` array in an `EgressIP` object specifies more than one IP address, the following conditions apply:

  - No node will ever host more than one of the specified IP addresses.

  - Traffic is balanced roughly equally between the specified IP addresses for a given namespace.

- If a node becomes unavailable, any egress IP addresses assigned to it are automatically reassigned, subject to the previously described conditions.

> [!IMPORTANT]
> If the number of nodes labeled with `k8s.ovn.org/egress-assignable` is less than the number of egress IP addresses specified in the `EgressIP` object, the additional egress IP addresses remain unassigned. To ensure all specified egress IP addresses are active and traffic is balanced as expected, verify that the number of egress-assignable nodes is equal to or greater than the number of egress IP addresses defined in the `EgressIP` object.

When a pod matches the selector for multiple `EgressIP` objects, there is no guarantee which of the egress IP addresses that are specified in the `EgressIP` objects is assigned as the egress IP address for the pod.

Additionally, if an `EgressIP` object specifies multiple egress IP addresses, there is no guarantee which of the egress IP addresses might be used. For example, if a pod matches a selector for an `EgressIP` object with two egress IP addresses, `10.10.20.1` and `10.10.20.2`, either might be used for each TCP connection or UDP conversation.

# Assigning an egress IP address to a namespace

You can assign one or more egress IP addresses to a namespace or to specific pods in a namespace.

<div>

<div class="title">

Prerequisites

</div>

- The OpenShift CLI (`oc`) is installed.

- You are logged in to the cluster as a cluster administrator.

- At least one node is configured to host an egress IP address.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create an `EgressIP` object.

    1.  Create a `<egressips_name>.yaml` file where `<egressips_name>` is the name of the object.

    2.  In the file that you created, define an `EgressIP` object, as in the following example:

        ``` yaml
        apiVersion: k8s.ovn.org/v1
        kind: EgressIP
        metadata:
          name: egress-project1
        spec:
          egressIPs:
          - 192.168.127.10
          - 192.168.127.11
          namespaceSelector:
            matchLabels:
              env: qa
        # ...
        ```

2.  To create the object, enter the following command.

    ``` terminal
    $ oc apply -f <egressips_name>.yaml
    ```

    where:

    `<egressips_name>`
    Replace `<egressips_name>` with the name of the object.

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    egressips.k8s.ovn.org/<egressips_name> created
    ```

    </div>

3.  Optional: Store the `<egressips_name>.yaml` file so that you can make changes later.

4.  Add labels to the namespace that requires egress IP addresses. To add a label to the namespace of an `EgressIP` object defined in a previous step, run the following command:

    ``` terminal
    $ oc label ns <namespace> env=qa
    ```

    where:

    `<namespace>`
    Replace `<namespace>` with the namespace that requires egress IP addresses.

</div>

<div>

<div class="title">

Verification

</div>

- To show all egress IP addresses that are in use in your cluster, enter the following command:

  ``` terminal
  $ oc get egressip -o yaml
  ```

  > [!NOTE]
  > The command `oc get egressip` only returns one egress IP address regardless of how many are configured. This is not a bug and is a limitation of Kubernetes. As a workaround, you can pass in the `-o yaml` or `-o json` flags to return all egress IPs addresses in use.

  <div class="formalpara">

  <div class="title">

  Example output

  </div>

  ``` terminal
  # ...
  spec:
    egressIPs:
    - 192.168.127.10
    - 192.168.127.11
  # ...
  ```

  </div>

</div>

# Understanding EgressIP failover control

The `reachabilityTotalTimeoutSeconds` parameter controls how quickly the system detects a failing `egressIP` node and initiates a failover. This parameter directly determines the maximum time the platform waits before declaring a node unreachable.

> [!IMPORTANT]
> When you configure `egressIP` with multiple egress nodes, the complete failover time from node failure to recovery on a new node is expected to be on the order of seconds or longer. This is because the new IP assignment can only begin after the `reachabilityTotalTimeoutSeconds` period has fully elapsed without a successful check.

To ensure traffic uses the correct external path, `egressIP` traffic on a node will always egress through the network interface on which the `egressIP` address has been assigned.

## Configuring the EgressIP failover time limit

You can configure the `reachabilityTotalTimeoutSeconds` parameter to control how quickly the system detects a failing `egressIP` node and initiates a failover.

<div>

<div class="title">

Prerequisites

</div>

- You installed the OpenShift CLI (`oc`).

- You logged in to the cluster as a cluster administrator.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Edit the `Network` custom resource by running the following command:

    ``` bash
    $ oc edit network.operator cluster
    ```

2.  Navigate to the `egressIPConfig: {}` section under `spec:defaultNetwork:ovnKubernetesConfig:`

3.  Modify the block to include the `reachabilityTotalTimeoutSeconds` parameter with your chosen value, 5 seconds for example. Make sure to use the correct indentation:

    ``` yaml
      defaultNetwork:
        ovnKubernetesConfig:
          egressIPConfig:
            reachabilityTotalTimeoutSeconds: 5
    ```

    > [!NOTE]
    > The value must be an integer between 0 and 60. For details on possible values, see the "EgressIP failover settings" section.

4.  Save and exit the editor. The operator automatically applies the changes.

</div>

<div>

<div class="title">

Verification

</div>

1.  Verify that the system correctly accepted the `reachabilityTotalTimeoutSeconds` parameter by running the following command:

    ``` terminal
    $ oc get network.operator cluster -o yaml
    ```

2.  Inspect the output and confirm that the `reachabilityTotalTimeoutSeconds` parameter is correctly nested under `spec:defaultNetwork:ovnKubernetesConfig:egressIPConfig:` with your intended value:

    ``` yaml
     # ...
      spec:
        # ...
        defaultNetwork:
          ovnKubernetesConfig:
            egressIPConfig:
              reachabilityTotalTimeoutSeconds: 5
            gatewayConfig:
      # ...
    ```

</div>

## EgressIP failover settings

The `reachabilityTotalTimeoutSeconds` parameter defines the total time limit in seconds for the platform health check process before a node is declared down.

The following table summarizes the acceptable values and their implications:

| Parameter Value (Seconds) | Effect on reachability check | Failover impact and use case |
|----|----|----|
| `0` | Disables the reachability check. | No automatic failover: Use only if an external system handles node health monitoring and failover. The platform will not automatically react to node failures. |
| `1 - 60` | Sets the total time limit for reachability probing. | Directly controls detection time: This value defines the lower limit for your overall failover time. A smaller value leads to faster failover but might increase network traffic. Default: 1 second. The maximum accepted integer value is 60. |

# Labeling a node to host egress IP addresses

You can apply the `k8s.ovn.org/egress-assignable=""` label to a node in your cluster so that OpenShift Container Platform can assign one or more egress IP addresses to the node.

<div>

<div class="title">

Prerequisites

</div>

- You installed the OpenShift CLI (`oc`).

- You logged in to the cluster as a cluster administrator.

</div>

<div>

<div class="title">

Procedure

</div>

- To label a node so that it can host one or more egress IP addresses, enter the following command:

  ``` terminal
  $ oc label nodes <node_name> k8s.ovn.org/egress-assignable=""
  ```

  `<node_name>`
  Specifies the name of the node to label.

  > [!TIP]
  > You can alternatively apply the following YAML to add the label to a node:
  >
  > ``` yaml
  > apiVersion: v1
  > kind: Node
  > metadata:
  >   labels:
  >     k8s.ovn.org/egress-assignable: ""
  >   name: <node_name>
  > ```

</div>

# Configuring dual-stack networking for an EgressIP object

For a cluster configured for dual-stack networking, you can apply dual-stack networking to a single `EgressIP` object. The `EgressIP` object can then extend dual-stack networking capabilities to a pod.

> [!IMPORTANT]
> Red Hat does not support creating two `EgressIP` objects to represent dual-stack networking capabilities. For example, specifying IPv4 addresses with one object and using another object to specify IPv6 addresses. This configuration limit impacts address-type assignments to pods.

<div>

<div class="title">

Prerequisites

</div>

- You created two egress nodes so that an `EgressIP` object can allocate IPv4 addresses to one node and IPv6 addresses to the other node. For more information, see "Assignment of egress IP addresses to nodes".

</div>

<div>

<div class="title">

Procedure

</div>

- Create an `EgressIP` object and configure IPv4 and IPv6 addresses for the object. The following example `EgressIP` object uses selectors to identify which pods use the specified egress IP addresses for their outbound traffic:

  ``` yaml
  kind: EgressIP
  metadata:
    name: egressip-dual
  spec:
    egressIPs:
      - 192.168.118.30
      - 2600:52:7:94::30
    namespaceSelector:
      matchLabels:
        env: qa
    podSelector:
      matchLabels:
        egressip: ds
  # ...
  ```

</div>

<div>

<div class="title">

Verification

</div>

1.  Create a `Pod` manifest file to test and validate your `EgressIP` object. The pod serves as a client workload that sends outbound traffic to verify that your `EgressIP` policy works as expected.

    ``` yaml
    apiVersion: v1
    kind: Pod
    metadata:
      name: ubi-egressip-pod
      namespace: test
      labels:
        egressip: ds
    spec:
      containers:
      - name: fedora-curl
        image: registry.redhat.io/ubi9/ubi
        command: ["/bin/bash", "-c", "sleep infinity"]
    # ...
    ```

    where:

    `<labels>`
    Sets custom identifiers so that the `EgressIP` object can use these labels to apply egress IP address to target pods.

2.  Run a `curl` request from inside a pod to an external server. This action verifies that outbound traffic correctly uses an address that you specified in the `EgressIP` object.

    ``` terminal
    $ curl <ipv_address>
    ```

    where:

    `<ipv_address>`
    Depending on the `EgressIP` object, enter an IPv4 or IPv6 address.

</div>

# Additional resources

- [LabelSelector meta/v1](../../rest_api/objects/index.md#labelselector-meta-v1)

- [LabelSelectorRequirement meta/v1](../../rest_api/objects/index.md#labelselectorrequirement-meta-v1)
