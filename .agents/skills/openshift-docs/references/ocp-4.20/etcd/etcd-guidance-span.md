<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Evaluate considerations and metrics for OpenShift Container Platform clusters that span data centers so you can design supported, resilient multisite deployments.

Red Hat strongly recommends a deployment model where OpenShift Container Platform clusters are deployed within a data center, but also acknowledges that there can be scenarios where a provider can use a deployment model where a cluster can span across data centers. This guidance outlines considerations when exploring the use of cluster deployments that span many data centers and describes important metrics that affect the supportability of such deployments. The design of such deployments must adhere to these guidelines for the product to function optimally and to ensure the highest quality of support with the appropriate product support subscriptions.

> [!WARNING]
> A cluster deployment that spans many data centers extends the cluster as a single failure domain across locations and must not be considered a replacement for a disaster recovery plan.

Clusters that span many data centers follow standard Red Hat OpenShift Container Platform support guidance. Review the "Red Hat OpenShift Container Platform Lifecycle" and "Red Hat Production Support Scope of Coverage" for more information.

Do not deploy an OpenShift Container Platform cluster that spans many sites. If you need presence in many data centers or regions, deploy one cluster per region or site, and use tools such as Red Hat Advanced Cluster Management to manage those clusters and deployments.

Some OpenShift Container Platform platforms support many data center deployments. Check the platform-specific product documentation and release notes for details. Other platforms can span data centers, depending on the quality of the network connectivity between nodes. For more information, see "Ensuring reliable etcd performance and scalability".

When you implement a cluster deployment that spans many data centers, implement the practices in "Red Hat High Availability, and Recommended Practices". An alternative to multisite deployments is to deploy one OpenShift Container Platform cluster per site, managed by Red Hat Advanced Cluster Management.

# Deployment caveats for spanned clusters

Review the guidance about the general aspects of a cluster deployment that spans data centers.

Some caveats to remember:

- Although the designs for deployments that span data centers are not bound by any special support requirements, these clusters do have additional inherent complexities that can require additional consideration or support involvement (time to identify, remediate and resolve issues) when compared to a standard single-site cluster.

- Applications might not work well or not work at all in clusters with high Kube API latency or low transaction rates.

- Layered products, such as storage providers, have lower latency requirements. In those cases, the latency limits are dictated by the architectures that are supported by the layered product.

- The failure scenarios are amplified with stretched control planes, and the way they are affected is specific to the deployment. Because of this, before using a deployment that spans data centers on a production environment, the organization should test and document the behavior of the cluster during disruptions such as:

  - When there is a network partition leaving one, two, or all control plane nodes isolated

  - When there are maximum transmission unit (MTU) mismatches on the transport network among the control plane nodes

  - When there is a sustained spike in latency as a Day 2 event towards one or more of the control plane nodes

  - When there is a considerable change in jitter due to network congestion, misconfiguration, or lack of QoS, an intermediate network device causing packet errors, and others

- Clusters deployed across many sites, network infrastructures, storage infrastructures, or other components inherently have a higher number of points of failure. Network disruptions or splits become a larger threat to such clusters especially, putting the nodes at risk of losing contact with each other. These multisite clusters must be designed with the potential for such failures in mind. Organizations deploying multisite clusters should extensively test failure scenarios, and should consider whether the cluster has protection from all points of failure. Consult with Red Hat Support for help to consider the important aspects of a resilient High Availability cluster design.

- In some cases, geographic (GEO) awareness is a requirement or issue that must be solved to minimize latency, so a proper implementation of a Global Service Load Balancing (GSLB) method must be available.

# Infrastructure as a Service (IaaS) and cloud provider considerations

Review infrastructure and cloud provider constraints for multisite OpenShift Container Platform control planes so you can plan maximum transmission unit (MTU), latency, and storage requirements.

This guidance applies to any infrastructure provider for which OpenShift Container Platform control plane nodes are supported by the user-provisioned infrastructure installer (platform=none) or the agent-based installer (platform=metal) using the ”User Managed Network” option.

Installer-provisioned infrastructure installers are not covered by these guidelines, however, where possible, installer-provisioned infrastructure deployments will span zones or availability zones on cloud or IaaS providers if possible by following these or similar guidelines. This means infrastructure provider-specific integrations will not be available; for example, integration with cloud provider services such as storage services and load balancers. Provider-specific services might still be used as external services.

Using different infrastructure platform providers for control plane nodes is discouraged; for example, mixing nodes across IaaS, cloud, and bare metal as control plane nodes. Consider the following guidelines when such combinations are needed:

- The minimum effective MTU across the infrastructure should be the maximum MTU used for the deployment. Using a lower MTU is acceptable. See "Understanding and Validating MTU setting with OpenShift Container Platform 4.x" for more information.

- The combined disk and network latency and jitter must keep an etcd peer round-trip time (RTT) of less than 100 ms. This is not the same as the network RTT.

- Layered products might have lower latency requirements. In those cases, the latency limits are dictated by the requirements of the architecture supported by the layered product. For example, OpenShift Container Platform cluster deployments that span data centers with Red Hat OpenShift Data Foundation must have a latency requirement of less than 10 ms RTT. For those cases, follow the specific product guidance.

- For guidance on cluster deployments that span data centers using OpenShift Data Foundation as the storage provider, see "Configuring OpenShift Data Foundation Disaster Recovery for OpenShift Workloads".

<div>

<div class="title">

Additional resources

</div>

- [Understanding and Validating MTU setting with OpenShift Container Platform 4.x (Red Hat Knowledgebase)](https://access.redhat.com/articles/7010220)

- [Configuring OpenShift Data Foundation Disaster Recovery for OpenShift Workloads](https://docs.redhat.com/en/documentation/red_hat_openshift_data_foundation/4.19/html-single/configuring_openshift_data_foundation_disaster_recovery_for_openshift_workloads/index)

</div>

# Site recommendations for multisite clusters

Plan control plane placement across data centers so your cluster maintains quorum when one site becomes unavailable.

Assuming that each site gets one control plane member, you theoretically define three sites, which is what Red Hat recommends. As a result, one data center can go into an inactive state and the cluster still maintains quorum and operational consistency.

When this assumption is not met, give attention to the needed and actual fault tolerance state of the cluster, as it often outlines or dictates the uptime and stability of the deployment.

# Requirements for etcd, networking, and storage

Apply etcd, networking, and storage requirements for multisite clusters so etcd stays healthy and workloads remain reachable across sites.

Consider the following requirements for clusters that span data centers.

## etcd requirements

There is a large list of factors and considerations that go into planning an etcd cluster deployment. When planning an OpenShift Container Platform cluster that spans data centers, you need to plan for situations that will likely stress or push etcd to the edge of its operational limits.

See "Ensuring reliable etcd performance and scalability" for more details on how to maintain operational capabilities and reduce service-affecting events and instability of the cluster.

## Network requirements

The chosen network topology must yield direct IP connectivity between nodes. The lowest effective maximum transmission unit (MTU) across the infrastructure should be the maximum MTU used for the deployment. Using a lower MTU is acceptable.

For more information, see "Understanding and Validating MTU setting with OpenShift Container Platform 4.x". The latency needs are ultimately defined by the services that use the network. See the sections related to etcd and storage for more details on requirements.

In addition to the base networking requirements, you need to think about how applications will be accessed. A top-level Global Service Load Balancing (GSLB) method will be needed outside of OpenShift Container Platform to enable external traffic to connect to the OpenShift Container Platform control plane services and ingress controllers.

## Storage requirements

When you plan a cluster deployment that spans data centers, consider the selected storage integration to ensure that it also meets multisite requirements, as it pertains to accessibility from all sites, fault tolerance, high availability, and so on.

An object storage solution should be used for the registry, and this storage solution needs to be in addition to any PV storage integration used for application volumes or workloads. This object storage solution should also have the same special considerations given to accessibility from all sites, fault tolerance, high availability, and so on.

Because disk I/O is a critical factor in the health of etcd database, it is required that they are deployed on a high speed, low latency media. See etcd guidance on "How etcd peer round trip time affects performance" and "Determining the size of the etcd database and understanding its effects" for more details on the exact requirements to meet.

<div>

<div class="title">

Additional resources

</div>

- [Ensuring reliable etcd performance and scalability](etcd-performance.md#etcd-leader-election-log-replication_etcd-performance)

- [Understanding and Validating MTU setting with OpenShift Container Platform 4.x (Red Hat Knowledgebase)](https://access.redhat.com/articles/7010220)

- [How etcd peer round trip time affects performance](etcd-performance.md#etcd-peer-round-trip_etcd-performance)

- [Determining the size of the etcd database and understanding its effects](etcd-performance.md#etcd-database-size_etcd-performance)

</div>

# Workload placement considerations

Place critical workloads across sites in a multisite cluster so you avoid single points of failure during a data center outage.

With multisite clusters, administrators and developers must take special considerations into account to ensure that critical workloads are scheduled or placed based on the proper hardware or hosts within the topology of the cluster. This planning ensures that the applications and services are highly available and fault-tolerant based on the topology of the cluster deployment.

Without this planning, OpenShift Container Platform might schedule workloads on hosts within the cluster so that a single point of failure (SPoF) exists for OpenShift Container Platform infrastructure services and other application services if a data center outage occurs.

# Additional resources

- [Red Hat OpenShift Container Platform Lifecycle](https://access.redhat.com/support/policy/updates/openshift)

- [Red Hat Production Support Scope of Coverage](https://access.redhat.com/support/offerings/production/soc)

- [Ensuring reliable etcd performance and scalability](etcd-performance.md#etcd-leader-election-log-replication_etcd-performance)

- [Red Hat OpenShift Container Platform High Availability, and Recommended Practices (Red Hat Knowledgebase)](https://access.redhat.com/articles/3221001)
