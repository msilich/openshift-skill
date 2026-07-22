<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

One of the challenges of scaling Kubernetes environments is managing the lifecycle of a growing fleet. To meet that challenge, you can use the multicluster engine Operator. The operator delivers full lifecycle capabilities for managed OpenShift Container Platform clusters and partial lifecycle management for other Kubernetes distributions. It is available in two ways:

- As a standalone operator that you install as part of your OpenShift Container Platform or OpenShift Kubernetes Engine subscription

- As part of [Red Hat Advanced Cluster Management for Kubernetes](https://docs.redhat.com/en/documentation/red_hat_advanced_cluster_management_for_kubernetes)

# Cluster management with multicluster engine on OpenShift Container Platform

When you enable multicluster engine on OpenShift Container Platform, you gain the following capabilities:

- [Hosted control planes](../hosted_control_planes/index.md#hcp-overview), which is a feature that is based on the HyperShift project. With a centralized hosted control plane, you can operate OpenShift Container Platform clusters in a hyperscale manner.

- Hive, which provisions self-managed OpenShift Container Platform clusters to the hub and completes the initial configurations for those clusters.

- klusterlet agent, which registers managed clusters to the hub.

- Infrastructure Operator, which manages the deployment of the Assisted Service to orchestrate on-premise bare metal and vSphere installations of OpenShift Container Platform, such as single-node OpenShift on bare metal. The Infrastructure Operator includes [GitOps Zero Touch Provisioning (ZTP)](../edge_computing/ztp-deploying-far-edge-clusters-at-scale.md#ztp-challenges-of-far-edge-deployments_ztp-deploying-far-edge-clusters-at-scale), which fully automates cluster creation on bare metal and vSphere provisioning with GitOps workflows to manage deployments and configuration changes.

- Open cluster management, which provides resources to manage Kubernetes clusters.

The multicluster engine is included with your OpenShift Container Platform support subscription and is delivered separately from the core payload. To start to use multicluster engine, you deploy the OpenShift Container Platform cluster and then install the operator. For more information, see [Installing and upgrading multicluster engine operator](https://docs.redhat.com/en/documentation/red_hat_advanced_cluster_management_for_kubernetes/2.15/html/clusters/cluster_mce_overview#mce-install-intro).

# Cluster management with Red Hat Advanced Cluster Management

If you need cluster management capabilities beyond what OpenShift Container Platform with multicluster engine can provide, consider Red Hat Advanced Cluster Management. The multicluster engine is an integral part of Red Hat Advanced Cluster Management and is enabled by default.

# Additional resources

For the complete documentation for multicluster engine, see [Cluster lifecycle with multicluster engine documentation](https://docs.redhat.com/en/documentation/red_hat_advanced_cluster_management_for_kubernetes/2.15/html/clusters/cluster_mce_overview), which is part of the product documentation for Red Hat Advanced Cluster Management.
