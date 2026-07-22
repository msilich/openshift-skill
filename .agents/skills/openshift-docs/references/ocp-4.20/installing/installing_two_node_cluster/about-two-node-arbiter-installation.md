<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

An OpenShift Container Platform cluster with two control plane nodes and one local arbiter node is a compact, cost-effective OpenShift Container Platform topology.

The arbiter node stores the full etcd data, maintaining an etcd quorum and preventing split brain. The arbiter node does not run the additional control plane components `kube-apiserver` and `kube-controller-manager`, nor does it run workloads.

To install a cluster with two control plane nodes and one local arbiter node, assign an arbiter role to at least one of the nodes and set the control plane node count for the cluster to 2. Although OpenShift Container Platform does not currently impose a limit on the number of arbiter nodes, the typical deployment includes only one to minimize the use of hardware resources.

After installation, you can add additional arbiter nodes to a cluster with two control plane nodes and one local arbiter node but not to a standard multi-node cluster. It is also not possible to convert between a two-node OpenShift cluster with a local node arbiter and standard topology.

You can install a cluster with two control plane nodes and one local arbiter node by using one of the following methods:

- Installing on bare metal: [Configuring a local arbiter node](../installing_bare_metal/ipi/ipi-install-installation-workflow.md#ipi-install-config-local-arbiter-node_ipi-install-installation-workflow)

- Installing with the Agent-based Installer: [Configuring a local arbiter node](../installing_with_agent_based_installer/installing-with-agent-based-installer.md#installing-ocp-agent-local-arbiter-node_installing-with-agent-based-installer)

> [!NOTE]
> For a cluster with an arbiter, the same networking requirements as a regular cluster for connectivity between machines apply. For more information, see "Network connectivity requirements".

<div>

<div class="title">

Additional resources

</div>

- [Network connectivity requirements](../installing_platform_agnostic/installing-platform-agnostic.md#installation-network-connectivity-user-infra_installing-platform-agnostic)

- [About a local arbiter node](../installing_with_agent_based_installer/preparing-to-install-with-agent-based-installer.md#installing-ocp-agent-local-arbiter-node_preparing-to-install-with-agent-based-installer)

</div>
