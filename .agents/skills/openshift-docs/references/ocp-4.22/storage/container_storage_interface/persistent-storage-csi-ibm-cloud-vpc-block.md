<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

You can provision and manage IBM Cloud® Virtual Private Cloud (VPC) Block Storage in OpenShift Container Platform using the IBM Cloud® VPC Block Container Storage Interface (CSI) Driver Operator and driver, which provide dynamic volume provisioning.

# Overview of IBM Cloud® VPC Block CSI Driver Operator

You can dynamically provision block storage volumes on IBM Cloud® Virtual Private Cloud (VPC) infrastructure by using the Container Storage Interface (CSI) driver, which supports multiple IOPS tiers to match your workload performance requirements.

Familiarity with persistent storage and configuring CSI volumes is recommended when working with a CSI Operator and driver. For more information, see "Understanding persistent storage" and "Configuring CSI volumes".

To create CSI-provisioned PVs that mount to IBM Cloud® VPC Block storage assets, OpenShift Container Platform installs the IBM Cloud® VPC Block CSI Driver Operator and the IBM Cloud® VPC Block CSI driver by default in the `openshift-cluster-csi-drivers` namespace.

IBM Cloud® VPC Block CSI Driver Operator
The IBM Cloud® VPC Block CSI Driver Operator provides three storage classes named `ibmc-vpc-block-10iops-tier` (default), `ibmc-vpc-block-5iops-tier`, and `ibmc-vpc-block-custom` for different tiers that you can use to create persistent volume claims (PVCs). The IBM Cloud® VPC Block CSI Driver Operator supports dynamic volume provisioning by allowing storage volumes to be created on-demand, eliminating the need for cluster administrators to pre-provision storage. You can disable this default storage class if necessary (see "Managing the default storage class").

IBM Cloud® VPC Block CSI driver
The IBM Cloud® VPC Block CSI driver enables you to create and mount IBM Cloud® VPC Block PVs.

<div>

<div class="title">

Additional resources

</div>

- [Understanding persistent storage](../understanding-persistent-storage.md#understanding-persistent-storage)

- [Configuring CSI volumes](persistent-storage-csi.md#persistent-storage-csi)

- [Managing the default storage class](persistent-storage-csi-sc-manage.md#persistent-storage-csi-sc-manage)

</div>

# About CSI

The Container Storage Interface (CSI) enables storage vendors to deliver plugins through a standard interface without modifying Kubernetes core code, replacing traditional embedded storage drivers.

CSI Operators give OpenShift Container Platform users storage options, such as volume snapshots, that are not possible with in-tree volume plugins.

# User-managed encryption

The user-managed encryption feature allows you to provide keys during installation that encrypt OpenShift Container Platform node root volumes, and enables all managed storage classes to use these keys to encrypt provisioned storage volumes.

You must specify the custom key in the `platform.<cloud_type>.defaultMachinePlatform` field in the install-config YAML file.

This features supports the following storage types:

- Amazon Web Services (AWS) Elastic Block storage (EBS)

  > [!NOTE]
  > If there is no encrypted key defined in the storage class, only set `encrypted: "true"` in the storage class. The AWS EBS CSI driver uses the AWS managed alias/aws/ebs, which is created by Amazon EBS automatically in each region by default to encrypt provisioned storage volumes. In addition, the managed storage classes all have the `encrypted: "true"` setting.

  For information about installing AWS EBS with user-managed encryption, see "Optional AWS configuration parameters".

- Microsoft Azure Disk storage

  > [!NOTE]
  > If the OS (root) disk is encrypted, and there is no encrypted key defined in the storage class, Azure Disk CSI driver uses the OS disk encryption key by default to encrypt provisioned storage volumes.

  For information about installing Azure Disk with user-managed encryption, see "Preparing an Azure Disk Encryption Set".

- Google Cloud Platform (GCP) persistent disk (PD) storage

  For information about installing GCP PD with user-managed encryption, see "Additional Google Cloud configuration parameters".

- IBM Cloud® Virtual Private Cloud (VPC) Block storage

  For information about installing with IBM Cloud with user-managed encryption, see "User-managed encryption for IBM Cloud" and "Installing on IBM Cloud".

<div>

<div class="title">

Additional resources

</div>

- [User-managed encryption for IBM Cloud](../../installing/installing_ibm_cloud/user-managed-encryption-ibm-cloud.md#user-managed-encryption-ibm-cloud)

- [Preparing to install on IBM Cloud](../../installing/installing_ibm_cloud/preparing-to-install-on-ibm-cloud.md#prerequisites_preparing-to-install-on-ibm-cloud)

</div>
