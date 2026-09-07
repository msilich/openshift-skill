<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Expand the persistent volume claim (PVC) of your virtual machine disk to accomodate growing data requirements. If your storage provider does not support volume expansion, you can expand the available virtual storage of a VM by adding blank data volumes.

You cannot reduce the size of a VM disk.

# Expand a VM disk PVC by using the web console

You can increase the size of a virtual machine (VM) disk by expanding the persistent volume claim (PVC) of the disk. To specify the increased PVC volume, you can use the **VirtualMachines** page in the web console, with the VM running.

> [!NOTE]
> If the PVC uses the file system volume mode, the disk image file expands to the available size while reserving some space for file system overhead.

<div>

<div class="title">

Procedure

</div>

1.  In the **Administrator** or **Virtualization** perspective, open the **VirtualMachines** page.

2.  Select the running VM to open its **Details** page.

3.  Select the **Configuration** tab and click **Storage**.

4.  Click the options menu ![kebab](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABsAAAAjCAIAAADqn+bCAAAACXBIWXMAAA7EAAAOxAGVKw4bAAAA+0lEQVRIie2WMQqEMBBFJ47gUXRBLyBYqbUXULCx9CR2XsAb6AlUEM9kpckW7obdZhwWYWHXX/3i8TPJZEKEUgpOlXFu3JX4V4kmB2qaZhgGKSUiZlkWxzEBC84N9zxv27bdO47Tti0Bs3at4wBgXVca/lJnfN/XPggCGmadIwAsywIAiGhZFk1ydy2EYJKgGCqK4vZUVVU0zKpxnmftp2mi4S/1GhG1N82DMWNNYVmW4zgqpRAxTVMa5t4evlg11nXd9/1eY57nSZIQMKtG13WllLu3bbvrOgJmdUbHwfur8Xniqw6Hh5UYRdGDNowwDA+WvP4UV+JPJ94B1gKUWcTOCT0AAAAASUVORK5CYII=) next to the disk you want to expand. Select the **Edit** option.

    The **Edit disk** dialog opens.

5.  In the **PersistentVolumeClaim size** field, enter the desired size.

    > [!NOTE]
    > You can enter any value greater than the current one. However, if the new value exceeds the available size, an error is displayed.

6.  Click **Save**.

</div>

# Expanding a VM disk PVC by using the CLI

You can increase the size of a virtual machine (VM) disk by expanding the persistent volume claim (PVC) of the disk. To specify the increased PVC volume, you can edit the `PersistentVolumeClaim` manifest by using the OpenShift CLI (`oc`).

> [!NOTE]
> If the PVC uses the file system volume mode, the disk image file expands to the available size while reserving some space for file system overhead.

<div>

<div class="title">

Prerequisites

</div>

- You have installed the OpenShift CLI (`oc`).

</div>

<div>

<div class="title">

Procedure

</div>

1.  Edit the `PersistentVolumeClaim` manifest of the VM disk that you want to expand:

    ``` terminal
    $ oc edit pvc <pvc_name>
    ```

2.  Update the disk size:

    ``` yaml
    apiVersion: v1
    kind: PersistentVolumeClaim
    metadata:
       name: vm-disk-expand
    spec:
      accessModes:
         - ReadWriteMany
      resources:
        requests:
           storage: 3Gi
    # ...
    ```

    - `spec.resources.requests.storage` specifies the new disk size.

</div>

# Expanding available virtual storage by adding blank data volumes

You can expand the available storage of a virtual machine (VM) by adding blank data volumes.

<div>

<div class="title">

Prerequisites

</div>

- You must have at least one persistent volume.

- You have installed the OpenShift CLI (`oc`).

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create a `DataVolume` manifest as shown in the following example:

    ``` yaml
    apiVersion: cdi.kubevirt.io/v1beta1
    kind: DataVolume
    metadata:
      name: blank-image-datavolume
    spec:
      source:
        blank: {}
      storage:
        resources:
          requests:
            storage: <2Gi>
      storageClassName: "<storage_class>"
    ```

    - `spec.storage.resources.requests.storage` specifies the amount of available space requested for the data volume.

    - `spec.storageClassName` is an optional field that specifies a storage class. If you do not specify a storage class, the default storage class is used.

2.  Create the data volume by running the following command:

    ``` terminal
    $ oc create -f <blank-image-datavolume>.yaml
    ```

</div>

# Additional resources

- [Extending a basic volume in Windows](https://docs.microsoft.com/en-us/windows-server/storage/disk-management/extend-a-basic-volume)

- [Extending an existing file system partition without destroying data in Red Hat Enterprise Linux](https://access.redhat.com/solutions/29095)

- [Extending a logical volume and its file system online in Red Hat Enterprise Linux](https://access.redhat.com/solutions/24770)

- [Configuring preallocation mode for data volumes](../../storage/virt-using-preallocation-for-datavolumes.md#virt-using-preallocation-for-datavolumes)

- [Managing data volume annotations](../../storage/virt-managing-data-volume-annotations.md#virt-managing-data-volume-annotations)
