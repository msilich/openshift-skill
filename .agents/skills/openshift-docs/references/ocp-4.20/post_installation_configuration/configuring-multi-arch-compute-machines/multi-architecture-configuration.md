<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

An OpenShift Container Platform cluster with multi-architecture compute machines is a cluster that supports compute machines with different architectures.

Configuring multi-architecture compute machines involves some additional considerations:

- When there are nodes with multiple architectures in your cluster, the architecture of the container image that you deploy to a node must be consistent with the architecture of that node. You need to ensure that the pod is assigned to the node with the appropriate architecture and that it matches the container image architecture. For more information on assigning pods to nodes, see "Assigning pods to nodes".

- In installer-provisioned installations, you are restricted to using the infrastructure provided by a single cloud provider. Adding external nodes, regardless of their architecture, to these clusters is not supported.

- Clusters that are installed with the platform type `none` are unable to use some features, such as managing compute machines with the Machine API. This limitation applies even if the compute machines that are attached to the cluster are installed on a platform that would normally support the feature. This parameter cannot be changed after installation.

  > [!IMPORTANT]
  > See "Deploying OpenShift 4.x on non-tested platforms using the bare metal install method" before you attempt to install an OpenShift Container Platform cluster in virtualized or cloud environments.

- The Cluster Samples Operator is not supported on clusters with multi-architecture compute machines. Your cluster can be created without this capability. For more information, see "Cluster capabilities".

- For information on migrating your single-architecture cluster to a cluster that supports multi-architecture compute machines, see "Migrating to a cluster with multi-architecture compute machines".

# Configuring your cluster with multi-architecture compute machines

To create a cluster with multi-architecture compute machines with different installation options and platforms, see the documentation references.

| Documentation section | Platform | User-provisioned installation | Installer-provisioned installation | Control Plane | Compute node |
|----|----|----|----|----|----|
| "Creating a cluster with multi-architecture compute machines on Azure" | Microsoft Azure | ✓ | ✓ | `aarch64` or `x86_64` | `aarch64`, `x86_64` |
| "Creating a cluster with multi-architecture compute machines on AWS" | Amazon Web Services (AWS) | ✓ | ✓ | `aarch64` or `x86_64` | `aarch64`, `x86_64` |
| "Creating a cluster with multi-architecture compute machines on Google Cloud" | Google Cloud |  | ✓ | `aarch64` or `x86_64` | `aarch64`, `x86_64` |
| "Creating a cluster with multi-architecture compute machines on bare metal, IBM Power, or IBM Z" | Bare metal | ✓ | ✓ | `aarch64` or `x86_64` | `aarch64`, `x86_64` |
| IBM Power | ✓ |  | `x86_64` or `ppc64le` | `x86_64`, `ppc64le` |  |
| IBM Z | ✓ |  | `x86_64` or `s390x` | `x86_64`, `s390x` |  |
| "Creating a cluster with multi-architecture compute machines on IBM Z® and IBM® LinuxONE with z/VM" | IBM Z® and IBM® LinuxONE | ✓ |  | `x86_64`, `s390x` | `x86_64`, `s390x` |
| "Creating a cluster with multi-architecture compute machines on IBM Z® and IBM® LinuxONE with RHEL KVM" | IBM Z® and IBM® LinuxONE | ✓ |  | `x86_64`, `s390x` | `x86_64`, `s390x` |
| "Creating a cluster with multi-architecture compute machines on IBM Power®" | IBM Power® | ✓ |  | `x86_64` | `x86_64`, `ppc64le` |

Cluster with multi-architecture compute machine installation options

<div>

<div class="title">

Additional resources

</div>

- [Creating a cluster with multi-architecture compute machines on Azure](creating-multi-arch-compute-nodes-azure.md#creating-multi-arch-compute-nodes-azure)

- [Creating a cluster with multi-architecture compute machines on AWS](creating-multi-arch-compute-nodes-aws.md#creating-multi-arch-compute-nodes-aws)

- [Creating a cluster with multi-architecture compute machines on Google Cloud](creating-multi-arch-compute-nodes-google-cloud.md#creating-multi-arch-compute-nodes-google-cloud)

- [Creating a cluster with multi-architecture compute machines on bare metal, IBM Power, or IBM Z](creating-multi-arch-compute-nodes-bare-metal.md#creating-multi-arch-compute-nodes-bare-metal)

- [Creating a cluster with multi-architecture compute machines on IBM Z® and IBM® LinuxONE with z/VM](creating-multi-arch-compute-nodes-ibm-z.md#creating-multi-arch-compute-nodes-ibm-z)

- [Creating a cluster with multi-architecture compute machines on IBM Z® and IBM® LinuxONE with RHEL KVM](creating-multi-arch-compute-nodes-ibm-z-kvm.md#creating-multi-arch-compute-nodes-ibm-z-kvm)

- [Creating a cluster with multi-architecture compute machines on IBM Power®](creating-multi-arch-compute-nodes-ibm-power.md#creating-multi-arch-compute-nodes-ibm-power)

</div>

> [!IMPORTANT]
> Autoscaling from zero is currently not supported on Google Cloud.

# Verifying cluster compatibility

Before you can start adding compute nodes of different architectures to your cluster, you must verify that your cluster is multi-architecture compatible.

<div>

<div class="title">

Prerequisites

</div>

- You installed the OpenShift CLI (`oc`).

- IBM Power only: Ensure that you meet the following prerequisites:

  - When using multiple architectures, hosts for OpenShift Container Platform nodes must share the same storage layer. If they do not have the same storage layer, use a storage provider such as `nfs-provisioner`.

  - You should limit the number of network hops between the compute and control plane as much as possible.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Log in to the OpenShift CLI (`oc`).

2.  You can check that your cluster uses the architecture payload by running the following command:

    ``` terminal
    $ oc adm release info -o jsonpath="{ .metadata.metadata}"
    ```

</div>

<div>

<div class="title">

Verification

</div>

- If you see the following output, your cluster is using the multi-architecture payload:

  ``` terminal
  {
   "release.openshift.io/architecture": "multi",
   "url": "https://access.redhat.com/errata/<errata_version>"
  }
  ```

  You can then begin adding multi-arch compute nodes to your cluster.

- If you see the following output, your cluster is not using the multi-architecture payload:

  ``` terminal
  {
   "url": "https://access.redhat.com/errata/<errata_version>"
  }
  ```

  > [!IMPORTANT]
  > To migrate your cluster so the cluster supports multi-architecture compute machines, see "Migrating to a cluster with multi-architecture compute machines".

</div>

<div>

<div class="title">

Additional resources

</div>

- [Migrating to a cluster with multi-architecture compute machines](../../updating/updating_a_cluster/migrating-to-multi-payload.md#migrating-to-multi-payload)

</div>

# Additional resources

- [Assigning pods to nodes](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/)

- [Deploying OpenShift 4.x on non-tested platforms using the bare metal install method (Red Hat Knowledgebase article)](https://access.redhat.com/articles/4207611)

- [Cluster capabilities](../../installing/overview/cluster-capabilities.md#cluster-capabilities)

- [Migrating to a cluster with multi-architecture compute machines](../../updating/updating_a_cluster/migrating-to-multi-payload.md#migrating-to-multi-payload)
