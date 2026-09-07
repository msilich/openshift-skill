<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

You can provision and manage Azure Stack Hub Storage in OpenShift Container Platform by using the Azure Stack Hub Container Storage Interface (CSI) Driver Operator and driver, which provide dynamic volume provisioning and eliminate the need to pre-provision storage.

# Overview of Azure Stack Hub

OpenShift Container Platform is capable of provisioning persistent volumes (PVs) using the Container Storage Interface (CSI) driver for Azure Stack Hub Storage, which allows you to run apps in an on-premise environment and deliver Azure services in your data center.

Familiarity with persistent storage and configuring CSI volumes is recommended when working with a CSI Operator and driver. For more information, see "Understanding persistent volumes" and "Configuring CSI volumes".

To create CSI-provisioned PVs that mount to Azure Stack Hub storage assets, OpenShift Container Platform installs the Azure Stack Hub CSI Driver Operator and the Azure Stack Hub CSI driver by default in the `openshift-cluster-csi-drivers` namespace.

Azure Stack Hub CSI Driver Operator
The Azure Stack CSI Driver Operator provides a storage class (`managed-csi`), with "Standard_LRS" as the default storage account type, that you can use to create persistent volume claims (PVCs). The Azure Stack Hub CSI Driver Operator supports dynamic volume provisioning by allowing storage volumes to be created on-demand, eliminating the need for cluster administrators to pre-provision storage.

Azure Stack Hub CSI driver
The Azure Stack Hub CSI driver enables you to create and mount Azure Stack Hub PVs.

# About CSI

The Container Storage Interface (CSI) enables storage vendors to deliver plugins through a standard interface without modifying Kubernetes core code, replacing traditional embedded storage drivers.

CSI Operators give OpenShift Container Platform users storage options, such as volume snapshots, that are not possible with in-tree volume plugins.

# Additional resources

- [Understanding persistent storage](../understanding-persistent-storage.md#understanding-persistent-storage)

- [Configuring CSI volumes](persistent-storage-csi.md#persistent-storage-csi)
