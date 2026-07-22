<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

# Overview

OpenShift Container Platform is capable of provisioning persistent volumes (PVs) using the Container Storage Interface (CSI) driver for IBM® Virtual Private Cloud (VPC) Block Storage.

Familiarity with [persistent storage](../understanding-persistent-storage.md#understanding-persistent-storage) and [configuring CSI volumes](persistent-storage-csi.md#persistent-storage-csi) is recommended when working with a CSI Operator and driver.

To create CSI-provisioned PVs that mount to IBM Cloud® VPC Block storage assets, OpenShift Container Platform installs the IBM Cloud® VPC Block CSI Driver Operator and the IBM Cloud® VPC Block CSI driver by default in the `openshift-cluster-csi-drivers` namespace.

- The *IBM Cloud® VPC Block CSI Driver Operator* provides three storage classes named `ibmc-vpc-block-10iops-tier` (default), `ibmc-vpc-block-5iops-tier`, and `ibmc-vpc-block-custom` for different tiers that you can use to create persistent volume claims (PVCs). The IBM Cloud® VPC Block CSI Driver Operator supports dynamic volume provisioning by allowing storage volumes to be created on demand, eliminating the need for cluster administrators to pre-provision storage. You can disable this default storage class if desired (see [Managing the default storage class](persistent-storage-csi-sc-manage.md#persistent-storage-csi-sc-manage)).

- The *IBM Cloud® VPC Block CSI driver* enables you to create and mount IBM Cloud® VPC Block PVs.

# About CSI

Storage vendors have traditionally provided storage drivers as part of Kubernetes. With the implementation of the Container Storage Interface (CSI), third-party providers can instead deliver storage plugins using a standard interface without ever having to change the core Kubernetes code.

CSI Operators give OpenShift Container Platform users storage options, such as volume snapshots, that are not possible with in-tree volume plugins.

# User-managed encryption

The user-managed encryption feature allows you to provide keys during installation that encrypt OpenShift Container Platform node root volumes, and enables all managed storage classes to use these keys to encrypt provisioned storage volumes. You must specify the custom key in the `platform.<cloud_type>.defaultMachinePlatform` field in the install-config YAML file.

This features supports the following storage types:

- Amazon Web Services (AWS) Elastic Block storage (EBS)

- Microsoft Azure Disk storage

- Google Cloud Platform (GCP) persistent disk (PD) storage

- IBM Virtual Private Cloud (VPC) Block storage

For information about installing with user-managed encryption for IBM Cloud, see [User-managed encryption for IBM Cloud](../../installing/installing_ibm_cloud/user-managed-encryption-ibm-cloud.md#user-managed-encryption-ibm-cloud) and [Preparing to install on IBM Cloud](../../installing/installing_ibm_cloud/preparing-to-install-on-ibm-cloud.md#prerequisites_preparing-to-install-on-ibm-cloud).

<div>

<div class="title">

Additional resources

</div>

- [Configuring CSI volumes](persistent-storage-csi.md#persistent-storage-csi)

</div>
