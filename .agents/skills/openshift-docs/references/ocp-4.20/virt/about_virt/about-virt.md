<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

OpenShift Virtualization provides a comprehensive virtualization solution that allows you to run and manage virtual machine workloads alongside container workloads in your OpenShift Container Platform cluster.

# What you can do with OpenShift Virtualization

OpenShift Virtualization provides scalable, enterprise-grade virtualization functionality for your cluster. You can use it to manage virtual machines (VMs) exclusively or alongside container workloads.

> [!NOTE]
> If you have a Red Hat OpenShift Virtualization Engine subscription, you can run unlimited VMs on subscribed hosts, but you cannot run application instances in containers. For more information, see the subscription guide section about "Red Hat OpenShift Virtualization Engine and related products".

OpenShift Virtualization adds new objects into your OpenShift Container Platform cluster by using Kubernetes custom resources to enable virtualization tasks. These tasks include:

- Creating and managing Linux and Windows VMs

- Running pod and VM workloads alongside each other in a cluster

- Connecting to VMs through a variety of consoles and CLI tools

- Importing and cloning existing VMs

- Managing network interface controllers and storage disks attached to VMs

- Live migrating VMs between nodes

You can manage your cluster and virtualization resources by using the **Virtualization** perspective of the OpenShift Container Platform web console, and by using the OpenShift CLI (`oc`).

> [!IMPORTANT]
> For supported and unsupported OVN-Kubernetes network plug-in use cases, see "OVN-Kubernetes purpose".

OpenShift Virtualization is designed and tested to work well with Red Hat OpenShift Data Foundation features.

> [!IMPORTANT]
> When you deploy OpenShift Virtualization with OpenShift Data Foundation, you must create a dedicated storage class for Windows virtual machine disks. See "Optimizing ODF PersistentVolumes for Windows VMs" for details.

You can use OpenShift Virtualization with OVN-Kubernetes or one of the other certified network plug-ins listed in "Certified OpenShift CNI Plug-ins".

You can check your OpenShift Virtualization cluster for compliance issues by installing the Compliance Operator and running a scan with the `ocp4-moderate` and `ocp4-moderate-node` profiles. The Compliance Operator uses OpenSCAP, a NIST-certified tool, to scan and enforce security policies.

For information about partnering with Independent Software Vendors (ISVs) and Services partners for specialized storage, networking, backup, and additional functionality, see the Red Hat Ecosystem Catalog.

# Comparing OpenShift Virtualization to VMware vSphere

If you are familiar with VMware vSphere, the following table lists OpenShift Virtualization components that you can use to accomplish similar tasks.

However, because OpenShift Virtualization is conceptually different from vSphere, and much of its functionality comes from the underlying OpenShift Container Platform, OpenShift Virtualization does not have direct alternatives for all vSphere concepts or components.

<table>
<caption>Mapping of vSphere concepts to their closest OpenShift Virtualization counterparts</caption>
<colgroup>
<col style="width: 28%" />
<col style="width: 28%" />
<col style="width: 42%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">vSphere concept</th>
<th style="text-align: left;">OpenShift Virtualization</th>
<th style="text-align: left;">Explanation</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>Datastore</p></td>
<td style="text-align: left;"><p>Persistent volume (PV)</p>
<p>Persistent volume claim (PVC)</p></td>
<td style="text-align: left;"><p>Stores VM disks. A PV represents existing storage and is attached to a VM through a PVC. When created with the <code>ReadWriteMany</code> (RWX) access mode, PVCs can be mounted by multiple VMs simultaneously.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Dynamic Resource Scheduling (DRS)</p></td>
<td style="text-align: left;"><p>Pod eviction policy</p>
<p>Descheduler</p></td>
<td style="text-align: left;"><p>Provides active resource balancing. A combination of pod eviction policies and a descheduler allows VMs to be live migrated to more appropriate nodes to keep node resource utilization manageable.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>NSX</p></td>
<td style="text-align: left;"><p>Multus</p>
<p>OVN-Kubernetes</p>
<p>Third-party container network interface (CNI) plug-ins</p></td>
<td style="text-align: left;"><p>Provides an overlay network configuration. There is no direct equivalent for NSX in OpenShift Virtualization, but you can use the OVN-Kubernetes network provider or install certified third-party CNI plug-ins.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Storage Policy Based Management (SPBM)</p></td>
<td style="text-align: left;"><p>Storage class</p></td>
<td style="text-align: left;"><p>Provides policy-based storage selection. Storage classes represent various storage types and describe storage capabilities, such as quality of service, backup policy, reclaim policy, and whether volume expansion is allowed. A PVC can request a specific storage class to satisfy application requirements.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>vCenter</p>
<p>vRealize Operations</p></td>
<td style="text-align: left;"><p>OpenShift Metrics and Monitoring</p></td>
<td style="text-align: left;"><p>Provides host and VM metrics. You can view metrics and monitor the overall health of the cluster and VMs by using the OpenShift Container Platform web console.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>vMotion</p></td>
<td style="text-align: left;"><p>Live migration</p></td>
<td style="text-align: left;"><p>Moves a running VM to another node without interruption. For live migration to be available, the PVC attached to the VM must have the <code>ReadWriteMany</code> (RWX) access mode.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>vSwitch</p>
<p>DvSwitch</p></td>
<td style="text-align: left;"><p>NMState Operator</p>
<p>Multus</p></td>
<td style="text-align: left;"><p>Provides a physical network configuration. You can use the NMState Operator to apply state-driven network configuration and manage various network interface types, including Linux bridges and network bonds. With Multus, you can attach multiple network interfaces and connect VMs to external networks.</p></td>
</tr>
</tbody>
</table>

# Supported cluster versions for OpenShift Virtualization

OpenShift Virtualization 4.20 is supported for use on OpenShift Container Platform 4.17 clusters. To use the latest z-stream release of OpenShift Virtualization, you must first upgrade to the latest version of OpenShift Container Platform.

The latest stable release of OpenShift Virtualization 4.20 is 4.20.21.

# About volume and access modes for virtual machine disks

If you use the storage API with known storage providers, the volume and access modes are selected automatically. However, if you use a storage class that does not have a storage profile, you must configure the volume and access mode.

For a list of known storage providers for OpenShift Virtualization, see [the Red Hat Ecosystem Catalog](https://catalog.redhat.com/search?searchType=software&badges_and_features=OpenShift+Virtualization&subcategories=Storage).

For best results, use the `ReadWriteMany` (RWX) access mode and the `Block` volume mode. This is important for the following reasons:

- `ReadWriteMany` (RWX) access mode is required for live migration.

- The `Block` volume mode performs significantly better than the `Filesystem` volume mode. This is because the `Filesystem` volume mode uses more storage layers, including a file system layer and a disk image file. These layers are not necessary for VM disk storage.

  For example, if you use Red Hat OpenShift Data Foundation, Ceph RBD volumes are preferable to CephFS volumes.

> [!IMPORTANT]
> You cannot live migrate virtual machines with the following configurations:
>
> - Storage volume with `ReadWriteOnce` (RWO) access mode
>
> - Passthrough features such as GPUs
>
> Set the `evictionStrategy` field to `None` for these virtual machines. The `None` strategy powers down VMs during node reboots.

# Single-node OpenShift differences

You can install OpenShift Virtualization on single-node OpenShift.

However, you should be aware that Single-node OpenShift does not support the following features:

- High availability

- Pod disruption

- Live migration

- Virtual machines or templates that have an eviction strategy configured

# Additional resources

- [Red Hat OpenShift Virtualization Engine and related products](https://www.redhat.com/en/resources/self-managed-openshift-subscription-guide#section-8)

- [Optimizing ODF PersistentVolumes for Windows VMs](https://access.redhat.com/articles/6978371)

- [OVN-Kubernetes](../../networking/ovn_kubernetes_network_provider/about-ovn-kubernetes.md#about-ovn-kubernetes)

- [Compliance Operator](../../security/compliance_operator/co-concepts/compliance-operator-understanding.md#understanding-compliance)

- [Supported compliance profiles](../../security/compliance_operator/co-scans/compliance-operator-supported-profiles.md#compliance-operator-supported-profiles)

- [OpenShift Virtualization supported limits](virt-supported-limits.md#virt-supported-limits)

- [OVN-Kubernetes purpose](../../networking/ovn_kubernetes_network_provider/about-ovn-kubernetes.md#nw-ovn-kubernetes-purpose_about-ovn-kubernetes)

- [Glossary of common terms for OpenShift Container Platform storage](../../storage/index.md#openshift-storage-common-terms_storage-overview)

- [About single-node OpenShift](../../installing/installing_sno/install-sno-preparing-to-install-sno.md#install-sno-about-installing-on-a-single-node_install-sno-preparing)

- [Using the OpenShift Assisted Installer Service to Deploy an OpenShift Cluster on Bare Metal and vSphere](https://cloud.redhat.com/blog/using-the-openshift-assisted-installer-service-to-deploy-an-openshift-cluster-on-metal-and-vsphere)

- [Certified OpenShift CNI Plug-ins](https://access.redhat.com/articles/5436171)

- [NIST-certified tool](https://www.nist.gov/)

- [Red Hat Ecosystem Catalog](https://red.ht/workswithvirt)

- [Pod disruption budgets](../../nodes/pods/nodes-pods-priority.md#priority-preemption-other_nodes-pods-priority)

- [About live migration](../live_migration/virt-about-live-migration.md#virt-about-live-migration)

- [Configure eviction and run strategies](../nodes/virt-eviction-strategies.md#virt-eviction-strategies)

- [Tuning & Scaling Guide in the Red Hat Knowledgebase](https://access.redhat.com/articles/6994974)
