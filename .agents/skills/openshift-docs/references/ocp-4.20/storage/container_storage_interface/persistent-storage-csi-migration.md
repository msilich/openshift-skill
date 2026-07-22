<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

In-tree storage drivers that are traditionally shipped with OpenShift Container Platform are being deprecated and replaced by their equivalent Container Storage Interface (CSI) drivers. OpenShift Container Platform provides automatic migration for in-tree volume plugins to their equivalent CSI drivers.

# Overview

Container Storage Interface (CSI) migration transparently translates in-tree storage volumes to CSI equivalents in memory without data migration or API changes.

This process does not perform any data migration; OpenShift Container Platform only translates the persistent volume object in memory. As a result, the translated persistent volume object is not stored on disk, nor is its contents changed. CSI automatic migration should be seamless. This feature does not change how you use all existing API objects: for example, `PersistentVolumes`, `PersistentVolumeClaims`, and `StorageClasses`.

The following in-tree to CSI drivers are automatically migrated:

- Azure Disk

- OpenStack Cinder

- Amazon Web Services (AWS) Elastic Block Storage (EBS)

- Google Compute Engine Persistent Disk (GCP PD)

- Azure File

- VMware vSphere

CSI migration for these volume types is considered generally available (GA), and requires no manual intervention.

CSI automatic migration of in-tree persistent volumes (PVs) or persistent volume claims (PVCs) does not enable any new CSI driver features, such as snapshots or expansion, if the original in-tree storage plugin did not support it.

# Storage class implications

OpenShift Container Platform 4.13, and later, uses Container Storage Interface (CSI) storage classes for new installations. Upgraded clusters receive CSI storage classes as default if none existed. Existing in-tree classes remain for backward compatibility. Switching to CSI storage classes is recommended.

For new OpenShift Container Platform 4.13, and later, installations, the default storage class is the CSI storage class. All volumes provisioned using this storage class are CSI persistent volumes (PVs).

For clusters upgraded from 4.12, and earlier, to 4.13, and later, the CSI storage class is created, and is set as the default if no default storage class was set before the upgrade. In the very unlikely case that there is a storage class with the same name, the existing storage class remains unchanged. Any existing in-tree storage classes remain, and might be necessary for certain features, such as volume expansion to work for existing in-tree PVs. While storage class referencing to the in-tree storage plugin will continue working, we recommend that you switch the default storage class to the CSI storage class.

For information about changing the default storage class, see *Changing the default storage class* under *Additional resources*.

<div>

<div class="title">

Additional resources

</div>

- [Changing the default storage class](persistent-storage-csi-sc-manage.md#change-default-storage-class_persistent-storage-csi-sc-manage)

</div>
