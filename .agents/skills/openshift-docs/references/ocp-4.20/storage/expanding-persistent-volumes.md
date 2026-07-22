<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Expand persistent volumes to increase storage capacity as your application data grows. You can resize volumes without recreating volumes or disrupting running workloads.

# Enabling volume expansion support

To enable volume expansion, the `StorageClass` object must have the `allowVolumeExpansion` field set to `true`. This prerequisite configuration allows persistent volume claims (PVCs) to be expanded after creation as your storage needs grow.

<div>

<div class="title">

Procedure

</div>

- Edit the `StorageClass` object and add the `allowVolumeExpansion` attribute by running the following command:

  ``` terminal
  $ oc edit storageclass <storage_class_name>
  ```

  Enter the name of storage class in `<storage_class_name>`.

  The following example shows adding this line at the bottom of the storage class configuration.

  <div class="formalpara">

  <div class="title">

  Example storage class YAML file with `allowVolumeExpansion` field set to `true`

  </div>

  ``` yaml
  apiVersion: storage.k8s.io/v1
  kind: StorageClass
  ...
  parameters:
    type: gp2
  reclaimPolicy: Delete
  allowVolumeExpansion: true
  ```

  </div>

  - `parameters.allowVolumeExpansion`: Setting this field to `true` allows persistent volume claims (PVCs) to be expanded after creation.

</div>

# Expanding CSI volumes

You can use the Container Storage Interface (CSI) to expand storage volumes after they have already been created.

> [!IMPORTANT]
> Shrinking persistent volumes (PVs) is *not* supported.

<div>

<div class="title">

Prerequisites

</div>

- The underlying CSI driver supports resize.

  For information about which CSI drivers support resizing, see under the *Additional resources* section "CSI drivers supported by OpenShift Container Platform".

- Dynamic provisioning is used.

- The controlling `StorageClass` object has `allowVolumeExpansion` set to `true`.

  For more information, see section *Enabling volume expansion support*.

</div>

<div>

<div class="title">

Procedure

</div>

- For the persistent volume claim (PVC), set `.spec.resources.requests.storage` to the desired new size.

</div>

<div>

<div class="title">

Verification

</div>

- To confirm that the resize is finished, look at the `status.conditions` field of the PVC . OpenShift Container Platform adds the `Resizing` condition to the PVC during expansion, which is removed after expansion completes.

</div>

# Expanding FlexVolume with a supported driver

To expand your FlexVolume storage capacity and meet growing data needs, update the storage request in your persistent volume claim (PVC). This increases capacity for existing volumes without recreating them.

Similar to other volume types, FlexVolume volumes can also be expanded when in use by a pod.

> [!IMPORTANT]
> Because OpenShift Container Platform does not support installation of FlexVolume plugins on control plane nodes, it does not support control plane expansion of FlexVolume.

<div>

<div class="title">

Prerequisites

</div>

- The underlying volume driver supports resize.

  For information about which CSI drivers support resizing, see under the *Additional resources* section "CSI drivers supported by OpenShift Container Platform".

- The driver is set with the `RequiresFSResize` capability to `true`. The FlexVolume can then be expanded after restarting the pod.

- Dynamic provisioning is used.

- The controlling `StorageClass` object has `allowVolumeExpansion` set to `true`.

  For more information, see section *Enabling volume expansion support*.

</div>

<div>

<div class="title">

Procedure

</div>

- To use resizing in the FlexVolume plugin, you must implement the `ExpandableVolumePlugin` interface using these methods:

  - `RequiresFSResize`

    If `true`, updates the capacity directly. If `false`, calls the `ExpandFS` method to finish the filesystem resize.

  - `ExpandFS`

    If `true`, calls `ExpandFS` to resize filesystem after physical volume expansion is done. The volume driver can also perform physical volume resize together with filesystem resize.

</div>

# Expanding local volumes

To expand your Local Storage Operator (LSO) storage capacity and meet growing data needs, update the storage request in your persistent volume (PV) and persistent volume claim (PVC). This increases capacity for existing volumes without recreating them.

<div>

<div class="title">

Procedure

</div>

1.  Expand the underlying devices. Ensure that appropriate capacity is available on these devices.

2.  Update the corresponding PV objects to match the new device sizes by editing the `.spec.capacity` field of the PV.

3.  For the storage class that is used for binding the PVC to PV, set the `allowVolumeExpansion` field to `true`.

4.  For the PVC, set `.spec.resources.requests.storage` to match the new size.

</div>

<div class="formalpara">

<div class="title">

Result

</div>

Kubelet should automatically expand the underlying file system on the volume, if necessary, and update the status field of the PVC to reflect the new size.

</div>

# Expanding persistent volume claims (PVCs) with a file system

To expand your storage capacity and meet growing data needs, you can resize existing volumes without recreating them.

Expanding persistent volume claims (PVCs) based on volume types that need file system resizing, such as Google Cloud Platform (GCP) persistent disk (PD), AWS Elastic Block Storage (EBS), and Cinder, is a two-step process. First, expand the volume objects in the cloud provider. Second, expand the file system on the node.

Expanding the file system on the node only happens when a new pod is started with the volume.

<div>

<div class="title">

Prerequisites

</div>

- The controlling storage class has the `allowVolumeExpansion` field set to `true`.

  For more information, see section *Enabling volume expansion support*.

</div>

<div>

<div class="title">

Procedure

</div>

- Edit the PVC and request a new size by editing `spec.resources.requests`. For example, the following expands the `ebs` PVC to 8 Gi:

  <div class="formalpara">

  <div class="title">

  Example PVC YAML file

  </div>

  ``` yaml
  kind: PersistentVolumeClaim
  apiVersion: v1
  metadata:
    name: ebs
  spec:
    storageClass: "storageClassWithFlagSet"
    accessModes:
      - ReadWriteOnce
    resources:
      requests:
        storage: 8Gi
  ```

  </div>

  Where updating `spec.resources.requests` to a larger amount expands the PVC.

</div>

<div class="formalpara">

<div class="title">

Verification

</div>

After the cloud provider object has finished resizing, the PVC is set to `FileSystemResizePending`.

</div>

- Check the condition by running the following command:

  ``` terminal
  $ oc describe pvc <pvc_name>
  ```

<div class="formalpara">

<div class="title">

Next steps

</div>

When the cloud provider object has finished resizing, the `PersistentVolume` object reflects the newly requested size in `PersistentVolume.Spec.Capacity`. You can now create or recreate a new pod from the PVC to finish the file system resizing. After the pod is running, the newly requested size is available and the `FileSystemResizePending` condition is removed from the PVC.

</div>

# Recovering from failure when expanding volumes

If a resize request fails or remains in a pending state, you can try again by entering a different resize value in `.spec.resources.requests.storage` for the persistent volume claim (PVC). The new value must be larger than the original volume size.

If entering another smaller resize value in `.spec.resources.requests.storage` for the PVC does not work, use the following procedure to recover.

<div>

<div class="title">

Procedure

</div>

1.  Mark the persistent volume (PV) that is bound to the PVC with the `Retain` reclaim policy. Change the `persistentVolumeReclaimPolicy` field to `Retain`.

2.  Delete the PVC.

3.  Manually edit the PV and delete the `claimRef` entry from the PV specification to ensure that the newly created PVC can bind to the PV marked `Retain`. This marks the PV as `Available`.

4.  Recreate the PVC in a smaller size, or a size that can be allocated by the underlying storage provider.

5.  Set the `volumeName` field of the PVC to the name of the PV. This binds the PVC to the provisioned PV only.

6.  Restore the reclaim policy on the PV.

</div>

# Viewing the status of volume resize

The volume resize status shows the progress of persistent volume claim (PVC) expansion operations. By checking this status you can confirm that volume expansions are progressing correctly and troubleshoot stuck or failed resizes.

You can view the status of volume resizing with the `pvc.Status.AllocatedResourceStatus` field. If a user changes the size of their PVCs, the `pvc.Status.AllocatedResourceStatus` field allows resource quota to be tracked accurately.

The possible values for `pvc.Status.AllocatedResourceStatus` are:

- `ControllerResizeInProgress`: Controller resize attempt is in progress.

- `ControllerResizeFailed`: Controller resize attempt failed.

- `NodeResizeInProgress`: Node resize attempt is in progress.

- `NodeResizeFailed`: Node resize attempt failed.

For a typical block volume, the field transitions between `ControllerResizeInProgress`, `NodeResizePending`, `NodeResizeInProgress`, and then nil/empty when the volume expansion finishes.

# Additional resources

- [CSI drivers supported by OpenShift Container Platform](https://docs.redhat.com/en/documentation/openshift_container_platform/latest/html/storage/using-container-storage-interface-csi#csi-drivers-supported_persistent-storage-csi)
