<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Ensure you are familiar with the general requirements to deploy hosted control planes.

The following requirements apply to hosted control planes:

- In order to run the HyperShift Operator, your management cluster needs at least three worker nodes. In the context of hosted control planes, a *management cluster* is an OpenShift Container Platform cluster where the HyperShift Operator is deployed and where the control planes for hosted clusters are hosted.

  The control plane is associated with a hosted cluster and runs as pods in a single namespace. When the cluster service consumer creates a hosted cluster, it creates a worker node that is independent of the control plane.

- You must open the firewall port `53` on Transmission Control Protocol (TCP) and User Datagram Protocol (UDP) to allow the Domain Name Service (DNS) protocol to work as expected.

- You can run both the management cluster and the worker nodes on-premise, such as on a bare-metal platform or on OpenShift Virtualization. In addition, you can run both the management cluster and the worker nodes on cloud infrastructure, such as Amazon Web Services (AWS).

- If you use a mixed infrastructure, such as running the management cluster on AWS and your worker nodes on-premise, or running your worker nodes on AWS and your management cluster on-premise, you must use the `PublicAndPrivate` publishing strategy and follow the latency requirements in the support matrix.

- In Bare Metal Host (BMH) deployments, where the Bare Metal Operator starts machines, the hosted control plane must be able to reach baseboard management controllers (BMCs). If your security profile does not permit the Cluster Baremetal Operator to access the network where the BMHs have their BMCs in order to enable Redfish automation, you can use BYO ISO support. However, in BYO mode, OpenShift Container Platform cannot automate the powering on of BMHs.

# Support matrix for hosted control planes

Because multicluster engine for Kubernetes Operator includes the HyperShift Operator, releases of hosted control planes align with releases of multicluster engine Operator. The support matrix includes details about supported clusters, platforms, and architectures, as well as information about updates and technology preview features.

For more information, see "OpenShift Operator Life Cycles".

## Management cluster support

Any supported OpenShift Container Platform cluster can be a management cluster.

> [!NOTE]
> A single-node OpenShift Container Platform cluster is not supported as a management cluster. If you have resource constraints, you can share infrastructure between a standalone OpenShift Container Platform control plane and hosted control planes. For more information, see "Shared infrastructure between hosted and standalone control planes".

The following table maps multicluster engine Operator versions to the management cluster versions that support them:

| Management cluster version | Supported multicluster engine Operator version |
|----------------------------|------------------------------------------------|
| 4.14, 4.16                 | 2.6                                            |
| 4.16                       | 2.7                                            |
| 4.16, 4.18                 | 2.8                                            |
| 4.18 - 4.19                | 2.9                                            |
| 4.18 - 4.20                | 2.10                                           |
| 4.19 - 4.21                | 2.11                                           |
| 4.20 - 4.22                | 2.17                                           |

Supported multicluster engine Operator versions for OpenShift Container Platform management clusters

## Hosted cluster support

For hosted clusters, no direct relationship exists between the management cluster version and the hosted cluster version. The hosted cluster version depends on the HyperShift Operator that is included with your multicluster engine Operator version.

> [!NOTE]
> Ensure a maximum latency of 200 ms between the management cluster and hosted clusters. This requirement is especially important for mixed infrastructure deployments, such as when your management cluster is on AWS and your compute nodes are on-premise.

The following table shows the hosted cluster versions that you can create by using the HyperShift Operator that is associated with a version of multicluster engine Operator:

> [!NOTE]
> Although the HyperShift Operator supports the hosted cluster versions in the following table, multicluster engine Operator supports only as far back as 2 versions earlier than the current version. For example, if the current hosted cluster version is 4.21, multicluster engine Operator supports as far back as version 4.19. If you want to use a hosted cluster version that is earlier than one of the versions that multicluster engine Operator supports, you can detach your hosted clusters from multicluster engine Operator to be unmanaged, or you can use an earlier version of multicluster engine Operator. For instructions to detach your hosted clusters from multicluster engine Operator, see "Removing a cluster from management" (RHACM documentation). For more information about multicluster engine Operator support, see "The multicluster engine for Kubernetes operator 2.17 Support Matrix" (Red Hat Knowledgebase).

| Hosted cluster version | HyperShift Operator in multicluster engine Operator 2.6 | HyperShift Operator in multicluster engine Operator 2.7 | HyperShift Operator in multicluster engine Operator 2.8 | HyperShift Operator in multicluster engine Operator 2.9 | HyperShift Operator in multicluster engine Operator 2.10 | HyperShift Operator in multicluster engine Operator 2.11 | HyperShift Operator in multicluster engine Operator 2.17 |
|----|----|----|----|----|----|----|----|
| 4.14 | Yes | Yes | Yes | No | No | No | No |
| 4.16 | Yes | Yes | Yes | Yes | No | No | No |
| 4.18 | No | No | Yes | Yes | Yes | No | No |
| 4.19 | No | No | No | Yes | Yes | Yes | No |
| 4.20 | No | No | No | No | Yes | Yes | Yes |
| 4.21 | No | No | No | No | No | Yes | Yes |
| 4.22 | No | No | No | No | No | No | Yes |

Hosted cluster version mapped to HyperShift Operator associated with multicluster engine Operator version

## Hosted cluster platform support

A hosted cluster supports only one infrastructure platform. For example, you cannot create multiple node pools on different infrastructure platforms.

The following table indicates which OpenShift Container Platform versions are supported for each platform of hosted control planes.

> [!IMPORTANT]
> For hosted control planes on IBM Power or IBM Z, the control plane must run on either 64_bit x86 architecture or s390x architecture. Node pools must run on either IBM Power or IBM Z. No other combinations are supported.

In the following table, the management cluster version is the OpenShift Container Platform version where the multicluster engine Operator is enabled:

| Hosted cluster platform | Management cluster version | Hosted cluster version |
|----|----|----|
| Amazon Web Services | 4.16, 4.18 - 4.22 | 4.16, 4.18 - 4.22 |
| IBM Power | 4.18 - 4.22 | 4.18 - 4.22 |
| IBM Z | 4.18 - 4.22 | 4.18 - 4.22 |
| OpenShift Virtualization | 4.14, 4.16, 4.18 - 4.22 | 4.14, 4.16, 4.18 - 4.22 |
| Bare metal | 4.14, 4.16, 4.18 - 4.22 | 4.14, 4.16, 4.18 - 4.22 |
| Non-bare-metal agent machines (Technology Preview) | 4.16, 4.18 - 4.22 | 4.16, 4.18 - 4.22 |
| Red Hat OpenStack Platform (RHOSP) (Technology Preview) | 4.19 - 4.22 | 4.19 - 4.22 |
| Microsoft Azure (Technology Preview) | 4.22 | 4.22 |

Required OpenShift Container Platform versions for platforms

## Multi-architecture support

The following table indicates the supported architectures for hosted control planes, organized by platform. If an architecture is not listed, it is not yet fully supported.

| Platform | Control planes | Compute nodes | OpenShift Container Platform version support |
|----|----|----|----|
| AWS | 64-bit x86 | 64-bit x86 | 4.16, 4.18 - 4.22 |
| AWS | 64-bit x86 | ARM64 | 4.18 - 4.22 |
| AWS | ARM64 | ARM64 | 4.18 - 4.22 |
| AWS | ARM64 | 64-bit x86 | 4.18 - 4.22 |
| Bare metal (Agent platform) | 64-bit x86 | 64-bit x86 | 4.14, 4.16, 4.18 - 4.22 |
| Bare metal (Agent platform) | 64-bit x86 | ARM64 | 4.21 - 4.22 |
| IBM Power | 64-bit x86 | ppc64le | 4.18 - 4.22 |
| IBM Z | 64-bit x86 | s390x | 4.18 - 4.22 |
| IBM Z | s390x | s390x | 4.20 - 4.22 |
| Non-bare-metal Agent machines (Technology Preview) | 64-bit x86 | 64-bit x86 | 4.16, 4.18 - 4.22 |
| OpenShift Virtualization | 64-bit x86 | 64-bit x86 | 4.14, 4.16, 4.18 - 4.22 |
| OpenShift Virtualization | s390x | s390x | 4.22 |
| Red Hat OpenStack Platform (RHOSP) (Technology Preview) | 64-bit x86 | 64-bit x86 | 4.19 - 4.22 |

Multi-architecture support for hosted control planes

## Updates of multicluster engine Operator

When you update to another version of the multicluster engine Operator, your hosted cluster can continue to run if the HyperShift Operator that is included in the version of multicluster engine Operator supports the hosted cluster version. The following table shows which hosted cluster versions are supported on which updated multicluster engine Operator versions.

> [!NOTE]
> Although the HyperShift Operator supports the hosted cluster versions in the following table, multicluster engine Operator supports only as far back as 2 versions earlier than the current version. For example, if the current hosted cluster version is 4.21, multicluster engine Operator supports as far back as version 4.19. If you want to use a hosted cluster version that is earlier than one of the versions that multicluster engine Operator supports, you can detach your hosted clusters from multicluster engine Operator to be unmanaged, or you can use an earlier version of multicluster engine Operator. For instructions to detach your hosted clusters from multicluster engine Operator, see "Removing a cluster from management" (RHACM documentation). For more information about multicluster engine Operator support, see "The multicluster engine for Kubernetes operator 2.17 Support Matrix" (Red Hat Knowledgebase).

| multicluster engine Operator version | Supported hosted cluster version while updating |
|----|----|
| Updating from 2.5 to 2.6 | OpenShift Container Platform 4.14, 4.16 |
| Updating from 2.6 to 2.7 | OpenShift Container Platform 4.14, 4.16 |
| Updating from 2.7 to 2.8 | OpenShift Container Platform 4.16 |
| Updating from 2.8 to 2.9 | OpenShift Container Platform 4.16, 4.18 |
| Updating from 2.9 to 2.10 | OpenShift Container Platform 4.18, 4.19 |
| Updating from 2.10 to 2.11 | OpenShift Container Platform 4.19, 4.20 |
| Updating from 2.11 to 2.17 | OpenShift Container Platform 4.20, 4.21 |

Hosted cluster version supported while updating multicluster engine Operator

For example, if you have an OpenShift Container Platform 4.18 hosted cluster on the management cluster and you update from multicluster engine Operator 2.8 to 2.9, the hosted cluster can continue to run.

## Technology Preview features

For a list of features in this release that have a Technology Preview status, see the "Technology Preview features status" section of the *Hosted control planes release notes*.

# Additional resources

- [OpenShift Operator Life Cycles](https://access.redhat.com/support/policy/updates/openshift_operators)

- [Shared infrastructure between hosted and standalone control planes](hcp-sizing-guidance.md#hcp-shared-infra_hcp-sizing-guidance)

- [Technology Preview features status](../hcp-release-notes.md#hcp-release-notes-technology-preview-tables_hcp-release-notes)

- [Removing a cluster from management](https://docs.redhat.com/en/documentation/red_hat_advanced_cluster_management_for_kubernetes/latest/html/clusters/cluster_mce_overview#remove-managed-cluster)

- [The multicluster engine for Kubernetes operator 2.17 Support Matrix](https://access.redhat.com/articles/7142379)

# FIPS-enabled hosted clusters

The binaries for hosted control planes are FIPs-compliant, with the exception of the hosted control planes command-line interface, `hcp`.

If you want to deploy a FIPS-enabled hosted cluster, you must use a FIPS-enabled management cluster. To enable FIPS mode for your management cluster, you must run the installation program from a Red Hat Enterprise Linux (RHEL) computer configured to operate in FIPS mode. For more information about configuring FIPS mode on RHEL, see [Switching RHEL to FIPS mode](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/security_hardening/switching-rhel-to-fips-mode_security-hardening).

When running RHEL or Red Hat Enterprise Linux CoreOS (RHCOS) booted in FIPS mode, OpenShift Container Platform core components use the RHEL cryptographic libraries that have been submitted to NIST for FIPS 140-2/140-3 Validation on only the x86_64, ppc64le, and s390x architectures.

After you set up your management cluster in FIPS mode, the hosted cluster creation process runs on that management cluster.

<div>

<div class="title">

Additional resources

</div>

- [The multicluster engine for Kubernetes operator 2.17 Support Matrix](https://access.redhat.com/articles/7142379)

- [Red Hat OpenShift Container Platform Operator Update Information Checker](https://access.redhat.com/labs/ocpouic/?operator=multicluster-engine&&upgrade_path=4.14%20to%204.16)

- [Shared infrastructure between hosted and standalone control planes](hcp-sizing-guidance.md#hcp-shared-infra_hcp-sizing-guidance)

</div>

# CIDR ranges for hosted control planes

To successfully deploy hosted control planes on OpenShift Container Platform, define the network environment by using specific Classless Inter-Domain Routing (CIDR) subnet ranges.

The following Classless Inter-Domain Routing (CIDR) subnet ranges are the default settings for hosted control planes:

- `v4InternalSubnet`: 100.65.0.0/16 (OVN-Kubernetes)

- `clusterNetwork`: 10.132.0.0/14 (pod network)

- `serviceNetwork`: 172.31.0.0/16

By using one of the default subnet ranges, you can avoid CIDR overlap with the management cluster and avoid connectivity issues. However, you can use other CIDR subnet ranges if they do not overlap with the management cluster.

<div>

<div class="title">

Additional resources

</div>

- [CIDR range definitions](../../networking/networking_overview/cidr-range-definitions.md#cidr-range-definitions)

</div>
