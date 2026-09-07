<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

OpenShift Container Platform allows use of VMware vSphere’s Virtual Machine Disk (VMDK) volumes. You can provision your OpenShift Container Platform cluster with persistent storage using VMware vSphere. Some familiarity with Kubernetes and VMware vSphere is assumed.

VMware vSphere volumes can be provisioned dynamically. OpenShift Container Platform creates the disk in vSphere and attaches this disk to the correct image.

> [!NOTE]
> OpenShift Container Platform provisions new volumes as independent persistent disks that can freely attach and detach the volume on any node in the cluster. Consequently, you cannot back up volumes that use snapshots, or restore volumes from snapshots. For more information, see "Snapshot Limitations".

The Kubernetes persistent volume framework allows administrators to provision a cluster with persistent storage and gives users a way to request those resources without having any knowledge of the underlying infrastructure.

Persistent volumes are not bound to a single project or namespace; they can be shared across the OpenShift Container Platform cluster. Persistent volume claims are specific to a project or namespace and can be requested by users.

> [!IMPORTANT]
> For new installations, OpenShift Container Platform 4.13 and later provides automatic migration for the vSphere in-tree volume plugin to its equivalent CSI driver. Updating to OpenShift Container Platform 4.15 and later also provides automatic migration. For more information about updating and migration, see "CSI automatic migration".
>
> CSI automatic migration should be seamless. Migration does not change how you use all existing API objects, such as persistent volumes, persistent volume claims, and storage classes.

You can provision VMware vSphere volumes dynamically or statically. However, dynamically provisioning VMware vSphere volumes is the recommended method.

<div>

<div class="title">

Additional resources

</div>

- [VMware vSphere](https://www.vmware.com/au/products/vsphere.html)

- [Installing a cluster on vSphere](../../installing/installing_vsphere/upi/installing-vsphere.md#installing-vsphere)

</div>

# Dynamically provisioning VMware vSphere volumes using the UI

You can dynamically provision VMware vSphere volumes by using the OpenShift Container Platform web console to create persistent volume claims with the default `thin` storage class, so that your applications have on-demand access to vSphere storage without manual volume creation.

OpenShift Container Platform installs a default storage class, named `thin`, that uses the `thin` disk format for provisioning volumes.

You can use the following procedure to dynamically provision these volumes using the default storage class.

<div>

<div class="title">

Prerequisites

</div>

- An OpenShift Container Platform cluster installed on a VMware vSphere version that meets the requirements for the components that you use. For more information, see "Installing a cluster on vSphere".

- Storage must exist in the underlying infrastructure before it can be mounted as a volume in OpenShift Container Platform.

</div>

<div>

<div class="title">

Procedure

</div>

1.  In the OpenShift Container Platform console, click **Storage** → **Persistent Volume Claims**.

2.  In the persistent volume claims overview, click **Create Persistent Volume Claim**.

3.  Define the required options on the resulting page.

    1.  Select the `thin` storage class.

    2.  Enter a unique name for the storage claim.

    3.  Select the access mode to determine the read and write access for the created storage claim.

    4.  Define the size of the storage claim.

4.  Click **Create** to create the persistent volume claim and generate a persistent volume.

</div>

# Dynamically provisioning VMware vSphere volumes using the CLI

You can dynamically provision VMware vSphere volumes from the CLI to provide persistent storage for your applications on-demand. OpenShift Container Platform installs a default StorageClass, named `thin`, that uses the `thin` disk format for provisioning.

<div>

<div class="title">

Prerequisites

</div>

- An OpenShift Container Platform cluster installed on a VMware vSphere version that meets the requirements for the components that you use. For more information, see "Installing a cluster on vSphere".

- Storage must exist in the underlying infrastructure before it can be mounted as a volume in OpenShift Container Platform.

</div>

<div>

<div class="title">

Procedure

</div>

1.  You can define a VMware vSphere PersistentVolumeClaim by creating a file, `pvc.yaml`, with the following contents:

    ``` yaml
    kind: PersistentVolumeClaim
    apiVersion: v1
    metadata:
      name: pvc
    spec:
      accessModes:
      - ReadWriteOnce
      resources:
        requests:
          storage: 1Gi
    ```

    where:

    `metadata.name`
    Specifies a unique name that represents the persistent volume claim.

    `spec.accessModes.ReadWriteOnce`
    Specifies the access mode of the persistent volume claim. With `ReadWriteOnce`, the volume can be mounted with read and write permissions by a single node.

    `spec.resources.requests.storage`
    Specifies the size of the persistent volume claim.

2.  Enter the following command to create the `PersistentVolumeClaim` object from the file:

    ``` terminal
    $ oc create -f pvc.yaml
    ```

</div>

# Statically provisioning VMware vSphere volumes

To statically provision VMware vSphere volumes you must create the virtual machine disks for reference by the persistent volume framework.

<div>

<div class="title">

Prerequisites

</div>

- Storage must exist in the underlying infrastructure before it can be mounted as a volume in OpenShift Container Platform.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create the virtual machine disks. Virtual machine disks (VMDKs) must be created manually before statically provisioning VMware vSphere volumes. Use either of the following methods:

    - Create using `vmkfstools`. Access ESX through Secure Shell (SSH) and then use following command to create a VMDK volume:

      ``` terminal
      $ vmkfstools -c <size> /vmfs/volumes/<datastore-name>/volumes/<disk-name>.vmdk
      ```

    - Create using `vmware-diskmanager`:

      ``` terminal
      $ shell vmware-vdiskmanager -c -t 0 -s <size> -a lsilogic <disk-name>.vmdk
      ```

2.  Create a persistent volume that references the VMDKs. Create a file, `pv1.yaml`, with the `PersistentVolume` object definition:

    ``` yaml
    apiVersion: v1
    kind: PersistentVolume
    metadata:
      name: pv1
    spec:
      capacity:
        storage: 1Gi
      accessModes:
        - ReadWriteOnce
      persistentVolumeReclaimPolicy: Retain
      vsphereVolume:
        volumePath: "[datastore1] volumes/myDisk"
        fsType: ext4
    ```

    where:

    `metadata.name`
    Specifies the name of the volume. This name is how it is identified by persistent volume claims or pods.

    `spec.capacity.storage`
    Specifies the amount of storage allocated to this volume.

    `spec.vsphereVolume`
    Specifies the volume type used, with `vsphereVolume` for vSphere volumes. The label is used to mount a vSphere VMDK volume into pods. The contents of a volume are preserved when it is unmounted. The volume type supports VMFS and VSAN datastore.

    `spec.vsphereVolume.volumePath`
    Specifies the existing VMDK volume to use. If you used `vmkfstools`, you must enclose the datastore name in square brackets, `[]`, in the volume definition, as shown previously.

    `spec.vsphereVolume.fsType`
    Specifies the file system type to mount. For example, ext4, xfs, or other file systems.

</div>

> [!IMPORTANT]
> Changing the value of the fsType parameter after the volume is formatted and provisioned can result in data loss and pod failure.

1.  Create the `PersistentVolume` object from the file:

    ``` terminal
    $ oc create -f pv1.yaml
    ```

2.  Create a persistent volume claim that maps to the persistent volume you created in the previous step. Create a file, `pvc1.yaml`, with the `PersistentVolumeClaim` object definition:

    ``` yaml
    apiVersion: v1
    kind: PersistentVolumeClaim
    metadata:
      name: pvc1
    spec:
      accessModes:
        - ReadWriteOnce
      resources:
       requests:
         storage: "1Gi"
      volumeName: pv1
    ```

    where:

    `metadata.name`
    Specifies a unique name that represents the persistent volume claim.

    `spec.accessModes.ReadWriteOnce`
    Specifies the access mode of the persistent volume claim. With `ReadWriteOnce`, the volume can be mounted with read and write permissions by a single node.

    `spec.resources.requests.storage`
    Specifies the size of the persistent volume claim.

    `spec.volumeName`
    Specifies the name of the existing persistent volume.

3.  Create the `PersistentVolumeClaim` object from the file:

    ``` terminal
    $ oc create -f pvc1.yaml
    ```

## Formatting VMware vSphere volumes

You can use unformatted vSphere volumes as PVs because OpenShift Container Platform formats them before the first use.

Before OpenShift Container Platform mounts the volume and passes it to a container, it checks that the volume contains a file system that is specified by the `fsType` parameter value in the `PersistentVolume` (PV) definition. If the device is not formatted with the file system, all data from the device is erased, and the device is automatically formatted with the specified file system.
