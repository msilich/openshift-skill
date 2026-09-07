<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

You should understand how OpenShift Container Platform secures attached storage to protect persistent data in containerized workloads. OpenShift Container Platform uses Security-Enhanced Linux (SELinux) capabilities, group ID (GID) annotations, and Container Storage Interface (CSI)-compliant storage providers to isolate storage access and prevent unauthorized data exposure.

# Persistent volume plugins

Containers are useful for both stateless and stateful applications. Protecting attached storage is a key element of securing stateful services. Using the Container Storage Interface (CSI), OpenShift Container Platform can incorporate storage from any storage back end that supports the CSI interface.

OpenShift Container Platform provides plugins for multiple types of storage, including:

- Red Hat OpenShift Data Foundation \*

- AWS Elastic Block Stores (EBS) \*

- AWS Elastic File System (EFS) \*

- Azure Disk \*

- Azure File \*

- OpenStack Cinder \*

- Google Compute Engine (GCE) Persistent Disks \*

- VMware vSphere \*

- Network File System (NFS)

- FlexVolume

- Fibre Channel

- Internet Small Computer Systems Interface (iSCSI)

Plugins for those storage types with dynamic provisioning are marked with an asterisk (\*). Data in transit is encrypted via HTTPS for all OpenShift Container Platform components communicating with each other.

You can mount a persistent volume (PV) on a host in any way supported by your storage type. Different types of storage have different capabilities and each PV’s access modes are set to the specific modes supported by that particular volume.

For example, NFS can support multiple read/write clients, but a specific NFS PV might be exported on the server as read-only. Each PV has its own set of access modes describing that specific PV’s capabilities, such as `ReadWriteOnce`, `ReadOnlyMany`, and `ReadWriteMany`.

# Shared storage

For shared storage providers such as Network File System (NFS), the persistent volume (PV) registers its group ID (GID) as an annotation on the PV resource.

Then, when the PV is claimed by the pod, the annotated GID is added to the supplemental groups of the pod, giving that pod access to the contents of the shared storage.

# Block storage

For block storage providers such as AWS Elastic Block Store (EBS), Google Compute Engine (GCE) Persistent Disks, and Internet Small Computer Systems Interface (iSCSI), OpenShift Container Platform uses Security-Enhanced Linux (SELinux) capabilities to secure the root of the mounted volume for non-privileged pods, making the mounted volume owned by and only visible to the container with which it is associated.

<div>

<div class="title">

Additional resources

</div>

- [Understanding persistent storage](../../storage/understanding-persistent-storage.md#understanding-persistent-storage)

- [Configuring CSI volumes](../../storage/container_storage_interface/persistent-storage-csi.md#persistent-storage-csi)

- [Dynamic provisioning](../../storage/dynamic-provisioning.md#dynamic-provisioning)

- [Persistent storage using NFS](../../storage/persistent_storage/persistent-storage-nfs.md#persistent-storage-using-nfs)

- [Persistent storage using AWS Elastic Block Store](../../storage/persistent_storage/persistent-storage-aws.md#persistent-storage-aws)

- [Persistent storage using GCE Persistent Disk](../../storage/persistent_storage/persistent-storage-gce.md#persistent-storage-using-gce)

</div>
