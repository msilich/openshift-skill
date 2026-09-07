<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

You can provision and manage AWS Elastic Block Storage (EBS) in OpenShift Container Platform by using the AWS EBS Container Storage Interface (CSI) Driver Operator and driver, which provide dynamic volume provisioning and eliminate the need to pre-provision storage.

# Overview of the AWS EBS CSI Driver Operator

OpenShift Container Platform is capable of provisioning persistent volumes (PVs) using the AWS Elastic Block Storage (EBS) Container Storage Interface (CSI) driver.

Familiarity with persistent storage and configuring CSI volumes is recommended when working with a CSI Operator and driver. For more information, see "Understanding persistent storage" and "Configuring CSI volumes".

To create CSI-provisioned PVs that mount to AWS EBS storage assets, OpenShift Container Platform installs the AWS EBS CSI Driver Operator (a Red Hat operator) and the AWS EBS CSI driver by default in the `openshift-cluster-csi-drivers` namespace.

AWS EBS CSI Driver Operator
The AWS EBS CSI Driver Operator provides a `StorageClass` by default that you can use to create persistent volume claims (PVCs). You can disable this default storage class if desired (see "Managing the default storage class"). You also have the option to create the AWS EBS `StorageClass` as described in "Creating the EBS storage class".

AWS EBS CSI driver
The AWS EBS CSI driver enables you to create and mount AWS EBS PVs.

> [!NOTE]
> If you installed the AWS EBS CSI Operator and driver on an OpenShift Container Platform 4.5 cluster, you must uninstall the 4.5 Operator and driver before you update to OpenShift Container Platform 4.20.

> [!IMPORTANT]
> OpenShift Container Platform defaults to using the CSI plugin to provision Amazon Elastic Block Store (Amazon EBS) storage.

For information about dynamically provisioning AWS EBS persistent volumes in OpenShift Container Platform, see "Dynamic provisioning".

<div>

<div class="title">

Additional resources

</div>

- [Understanding persistent storage](../understanding-persistent-storage.md#understanding-persistent-storage)

- [Configuring CSI volumes](persistent-storage-csi.md#persistent-storage-csi)

- [Managing the default storage class](persistent-storage-csi-sc-manage.md#persistent-storage-csi-sc-manage)

- [Creating the EBS storage class](../persistent_storage/persistent-storage-aws.md#storage-create-storage-class_persistent-storage-aws)

- [Dynamic provisioning](../dynamic-provisioning.md#dynamic-provisioning)

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

- [Optional AWS configuration parameters](../../installing/installing_aws/installation-config-parameters-aws.md#installation-configuration-parameters-optional-aws_installation-config-parameters-aws)

</div>
