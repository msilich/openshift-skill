<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

# Persistent storage overview

Persistent volumes (PVs) are administrator-provisioned storage resources that exist independently of pods, while persistent volume claims (PVCs) are developer requests for those resources. Understanding this separation of concerns, where administrators manage storage infrastructure, and developers simply request capacity and access modes, helps both roles to configure and consume durable storage without requiring developers to know underlying storage details.

Managing storage is a distinct problem from managing compute resources. OpenShift Container Platform uses the Kubernetes persistent volume (PV) framework to allow cluster administrators to provision persistent storage for a cluster. Developers can use persistent volume claims (PVCs) to request PV resources without having specific knowledge of the underlying storage infrastructure.

PVCs are specific to a project, and are created and used by developers as a means to use a PV. PV resources on their own are not scoped to any single project; they can be shared across the entire OpenShift Container Platform cluster and claimed from any project. After a PV is bound to a PVC, that PV can not then be bound to additional PVCs. This has the effect of scoping a bound PV to a single namespace, that of the binding project.

PVs are defined by a `PersistentVolume` API object, which represents a piece of existing storage in the cluster that was either statically provisioned by the cluster administrator or dynamically provisioned using a `StorageClass` object. It is a resource in the cluster just like a node is a cluster resource.

PVs are volume plugins like `Volumes` but have a lifecycle that is independent of any individual pod that uses the PV. PV objects capture the details of the implementation of the storage, be that NFS, iSCSI, or a cloud-provider-specific storage system.

> [!IMPORTANT]
> High availability of storage in the infrastructure is left to the underlying storage provider.

PVCs are defined by a `PersistentVolumeClaim` API object, which represents a request for storage by a developer. It is similar to a pod in that pods consume node resources and PVCs consume PV resources. For example, pods can request specific levels of resources, such as CPU and memory, while PVCs can request specific storage capacity and access modes. For example, they can be mounted once read/write or many times read-only.

# Lifecycle of a volume and claim

PVs are resources in the cluster. PVCs are requests for those resources and also act as claim checks to the resource. The interaction between PVs and PVCs have the following lifecycle.

## Provision storage

In response to requests from a developer defined in a PVC, a cluster administrator configures one or more dynamic provisioners that provision storage and a matching PV.

Alternatively, a cluster administrator can create a number of PVs in advance that carry the details of the real storage that is available for use. PVs exist in the API and are available for use.

## Bind claims

When you create a PVC, you request a specific amount of storage, specify the required access mode, and create a storage class to describe and classify the storage. The control loop in the master watches for new PVCs and binds the new PVC to an appropriate PV. If an appropriate PV does not exist, a provisioner for the storage class creates one.

The size of all PVs might exceed your PVC size. This is especially true with manually provisioned PVs. To minimize the excess, OpenShift Container Platform binds to the smallest PV that matches all other criteria.

Claims remain unbound indefinitely if a matching volume does not exist or can not be created with any available provisioner servicing a storage class. Claims are bound as matching volumes become available. For example, a cluster with many manually provisioned 50Gi volumes would not match a PVC requesting 100Gi. The PVC can be bound when a 100Gi PV is added to the cluster.

## Use pods and claimed PVs

Pods use claims as volumes. The cluster inspects the claim to find the bound volume and mounts that volume for a pod. For those volumes that support multiple access modes, you must specify which mode applies when you use the claim as a volume in a pod.

Once you have a claim and that claim is bound, the bound PV belongs to you for as long as you need it. You can schedule pods and access claimed PVs by including `persistentVolumeClaim` in the pod’s volumes block.

> [!NOTE]
> If you attach persistent volumes that have high file counts to pods, those pods can fail or can take a long time to start. For more information, see [When using Persistent Volumes with high file counts in OpenShift, why do pods fail to start or take an excessive amount of time to achieve "Ready" state?](https://access.redhat.com/solutions/6221251).

## Storage Object in Use Protection

The Storage Object in Use Protection feature ensures that PVCs in active use by a pod and PVs that are bound to PVCs are not removed from the system, as this can result in data loss.

Storage Object in Use Protection is enabled by default.

> [!NOTE]
> A PVC is in active use by a pod when a `Pod` object exists that uses the PVC.

If a user deletes a PVC that is in active use by a pod, the PVC is not removed immediately. PVC removal is postponed until the PVC is no longer actively used by any pods. Also, if a cluster admin deletes a PV that is bound to a PVC, the PV is not removed immediately. PV removal is postponed until the PV is no longer bound to a PVC.

## Release a persistent volume

When you are finished with a volume, you can delete the PVC object from the API, which allows reclamation of the resource. The volume is considered released when the claim is deleted, but it is not yet available for another claim. The previous claimant’s data remains on the volume and must be handled according to policy.

## Reclaim policy for persistent volumes

The reclaim policy of a persistent volume tells the cluster what to do with the volume after it is released. A volume’s reclaim policy can be `Retain`, `Recycle`, or `Delete`.

- `Retain` reclaim policy allows manual reclamation of the resource for those volume plugins that support it.

- `Recycle` reclaim policy recycles the volume back into the pool of unbound persistent volumes once it is released from its claim.

> [!IMPORTANT]
> The `Recycle` reclaim policy is deprecated in OpenShift Container Platform 4. Dynamic provisioning is recommended for equivalent and better functionality.

- `Delete` reclaim policy deletes both the `PersistentVolume` object from OpenShift Container Platform and the associated storage asset in external infrastructure, such as Amazon Elastic Block Store (Amazon EBS) or VMware vSphere.

> [!NOTE]
> Dynamically provisioned volumes are always deleted.

## Reclaiming a persistent volume manually

When a persistent volume claim (PVC) is deleted, the persistent volume (PV) still exists and is considered "released". However, the PV is not yet available for another claim because the data of the previous claimant remains on the volume.

<div class="formalpara">

<div class="title">

Procedure

</div>

To manually reclaim the PV as a cluster administrator:

</div>

1.  Delete the PV by running the following command:

    ``` terminal
    $ oc delete pv <pv_name>
    ```

    The associated storage asset in the external infrastructure, such as an AWS EBS, GCE PD, Azure Disk, or Cinder volume, still exists after the PV is deleted.

2.  Clean up the data on the associated storage asset.

3.  Delete the associated storage asset. Alternately, to reuse the same storage asset, create a new PV with the storage asset definition.

The reclaimed PV is now available for use by another PVC.

## Changing the reclaim policy of a persistent volume

You can change the reclaim policy of a persistent volume.

<div>

<div class="title">

Procedure

</div>

1.  List the persistent volumes in your cluster:

    ``` terminal
    $ oc get pv
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    NAME                                       CAPACITY   ACCESSMODES   RECLAIMPOLICY   STATUS    CLAIM             STORAGECLASS     REASON    AGE
     pvc-b6efd8da-b7b5-11e6-9d58-0ed433a7dd94   4Gi        RWO           Delete          Bound     default/claim1    manual                     10s
     pvc-b95650f8-b7b5-11e6-9d58-0ed433a7dd94   4Gi        RWO           Delete          Bound     default/claim2    manual                     6s
     pvc-bb3ca71d-b7b5-11e6-9d58-0ed433a7dd94   4Gi        RWO           Delete          Bound     default/claim3    manual                     3s
    ```

    </div>

2.  Choose one of your persistent volumes and change its reclaim policy:

    ``` terminal
    $ oc patch pv <your-pv-name> -p '{"spec":{"persistentVolumeReclaimPolicy":"Retain"}}'
    ```

3.  Verify that your chosen persistent volume has the right policy:

    ``` terminal
    $ oc get pv
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    NAME                                       CAPACITY   ACCESSMODES   RECLAIMPOLICY   STATUS    CLAIM             STORAGECLASS     REASON    AGE
     pvc-b6efd8da-b7b5-11e6-9d58-0ed433a7dd94   4Gi        RWO           Delete          Bound     default/claim1    manual                     10s
     pvc-b95650f8-b7b5-11e6-9d58-0ed433a7dd94   4Gi        RWO           Delete          Bound     default/claim2    manual                     6s
     pvc-bb3ca71d-b7b5-11e6-9d58-0ed433a7dd94   4Gi        RWO           Retain          Bound     default/claim3    manual                     3s
    ```

    </div>

    In the preceding output, the volume bound to claim `default/claim3` now has a `Retain` reclaim policy. The volume will not be automatically deleted when a user deletes claim `default/claim3`.

</div>

# Persistent volumes

Each PV contains a `spec` and `status`, which is the specification and status of the volume, for example:

<div class="formalpara">

<div class="title">

`PersistentVolume` object definition example

</div>

``` yaml
apiVersion: v1
kind: PersistentVolume
metadata:
  name: pv0001
spec:
  capacity:
    storage: 5Gi
  accessModes:
    - ReadWriteOnce
  persistentVolumeReclaimPolicy: Retain
  ...
status:
  ...
```

</div>

- Name of the persistent volume.

- The amount of storage available to the volume.

- The access mode, defining the read-write and mount permissions.

- The reclaim policy, indicating how the resource should be handled once it is released.

You can view the name of a PVC that is bound to a PV by running the following command:

``` terminal
$ oc get pv <pv_name> -o jsonpath='{.spec.claimRef.name}'
```

## Types of PVs

OpenShift Container Platform supports the following persistent volume plugins:

- AWS Elastic Block Store (EBS), which is installed by default.

- AWS Elastic File Store (EFS)

- Azure Disk

- Azure File

- Cinder

- Fibre Channel

- GCP Persistent Disk

- GCP Filestore

- IBM Power Virtual Server Block

- IBM Cloud® VPC Block

- HostPath

- iSCSI

- Local volume

- LVM Storage

- NFS

- OpenStack Manila

- Red Hat OpenShift Data Foundation

- CIFS/SMB

- VMware vSphere

## Capacity

Generally, a persistent volume (PV) has a specific storage capacity. This is set by using the `capacity` attribute of the PV.

Currently, storage capacity is the only resource that can be set or requested. Future attributes may include IOPS, throughput, and so on.

## Access modes

A persistent volume can be mounted on a host in any way supported by the resource provider. Providers have different capabilities and each PV’s access modes are set to the specific modes supported by that particular volume. For example, NFS can support multiple read-write clients, but a specific NFS PV might be exported on the server as read-only. Each PV gets its own set of access modes describing that specific PV’s capabilities.

Claims are matched to volumes with similar access modes. The only two matching criteria are access modes and size. A claim’s access modes represent a request. Therefore, you might be granted more, but never less. For example, if a claim requests RWO, but the only volume available is an NFS PV (RWO+ROX+RWX), the claim would then match NFS because it supports RWO.

Direct matches are always attempted first. The volume’s modes must match or contain more modes than you requested. The size must be greater than or equal to what is expected. If two types of volumes, such as NFS and iSCSI, have the same set of access modes, either of them can match a claim with those modes. There is no ordering between types of volumes and no way to choose one type over another.

All volumes with the same modes are grouped, and then sorted by size, smallest to largest. The binder gets the group with matching modes and iterates over each, in size order, until one size matches.

> [!IMPORTANT]
> Volume access modes describe volume capabilities. They are not enforced constraints. The storage provider is responsible for runtime errors resulting from invalid use of the resource. Errors in the provider show up at runtime as mount errors.
>
> For example, NFS offers `ReadWriteOnce` access mode. If you want to use the volume’s ROX capability, mark the claims as `ReadOnlyMany`.
>
> iSCSI and Fibre Channel volumes do not currently have any fencing mechanisms. You must ensure the volumes are only used by one node at a time. In certain situations, such as draining a node, the volumes can be used simultaneously by two nodes. Before draining the node, delete the pods that use the volumes.

The following table lists the access modes:

| Access Mode | CLI abbreviation | Description |
|----|----|----|
| ReadWriteOnce | `RWO` | The volume can be mounted as read-write by a single node. |
| ReadWriteOncePod | `RWOP` | The volume can be mounted as read-write by a single pod on a single node. |
| ReadOnlyMany | `ROX` | The volume can be mounted as read-only by many nodes. |
| ReadWriteMany | `RWX` | The volume can be mounted as read-write by many nodes. |

Access modes

| Volume plugin | ReadWriteOnce <sup>\[1\]</sup> | ReadWriteOncePod | ReadOnlyMany | ReadWriteMany |
|----|----|----|----|----|
| AWS EBS <sup>\[2\]</sup> | ✅ | ✅ |  |  |
| AWS EFS | ✅ | ✅ | ✅ | ✅ |
| Azure File | ✅ | ✅ | ✅ | ✅ |
| Azure Disk | ✅ | ✅ |  |  |
| CIFS/SMB | ✅ | ✅ | ✅ | ✅ |
| Cinder | ✅ | ✅ |  |  |
| Fibre Channel | ✅ | ✅ | ✅ | ✅ <sup>\[3\]</sup> |
| GCP Persistent Disk | ✅ <sup>\[4\]</sup> | ✅ | ✅ | ✅ <sup>\[4\]</sup> |
| GCP Filestore | ✅ | ✅ | ✅ | ✅ |
| HostPath | ✅ | ✅ |  |  |
| IBM Power Virtual Server Disk | ✅ | ✅ | ✅ | ✅ |
| IBM Cloud® VPC Disk | ✅ | ✅ |  |  |
| iSCSI | ✅ | ✅ | ✅ | ✅ <sup>\[3\]</sup> |
| Local volume | ✅ | ✅ |  |  |
| LVM Storage | ✅ | ✅ |  |  |
| NFS | ✅ | ✅ | ✅ | ✅ |
| OpenStack Manila |  | ✅ |  | ✅ |
| Red Hat OpenShift Data Foundation | ✅ | ✅ |  | ✅ |
| VMware vSphere | ✅ | ✅ |  | ✅ <sup>\[5\]</sup> |

Supported access modes for persistent volumes

1.  ReadWriteOnce (RWO) volumes cannot be mounted on multiple nodes. If a node fails, the system does not allow the attached RWO volume to be mounted on a new node because it is already assigned to the failed node. If you encounter a multi-attach error message as a result, force delete the pod on a shutdown or crashed node to avoid data loss in critical workloads, such as when dynamic persistent volumes are attached.

2.  Use a recreate deployment strategy for pods that rely on AWS EBS.

3.  Only raw block volumes support the `ReadWriteMany` (RWX) access mode for Fibre Channel and iSCSI. For more information, see "Block volume support".

4.  For GCP hyperdisk-balanced disks:

    - The supported access modes are:

      - `ReadWriteOnce`

      - `ReadWriteMany`

    - Cloning and snapshotting is disabled for disks with `ReadWriteMany` access mode enabled.

    - You can attach a single hyperdisk-balanced disk volume in `ReadWriteMany` to a maximum of 8 instances.

    - You can only resize a disk in `ReadWriteMany` if you detach the disk from all instances.

    - [Additional limitations](https://cloud.google.com/compute/docs/disks/attach-disks).

5.  If the underlying vSphere environment supports the vSAN file service, the vSphere Container Storage Interface (CSI) Driver Operator installed by OpenShift Container Platform supports provisioning of ReadWriteMany (RWX) volumes. If you do not have vSAN file service configured, and you request RWX, the volume fails to get created and an error is logged. For more information, see "Using Container Storage Interface" → "VMware vSphere CSI Driver Operator".

## Phase

Volumes can be found in one of the following phases:

| Phase | Description |
|----|----|
| Available | A free resource not yet bound to a claim. |
| Bound | The volume is bound to a claim. |
| Released | The claim was deleted, but the resource is not yet reclaimed by the cluster. |
| Failed | The volume has failed its automatic reclamation. |

Volume phases

### Last phase transition time

The `LastPhaseTransitionTime` field has a timestamp that updates every time a persistent volume (PV) transitions to a different phase (`pv.Status.Phase`). To find the time of the last phase transition for a PV, run the following command:

``` terminal
$ oc get pv <pv_name> -o json | jq '.status.lastPhaseTransitionTime'
```

- Specify the name of the PV that you want to see the last phase transition.

### Mount options

You can specify mount options while mounting a PV by using the attribute `mountOptions`.

For example:

<div class="formalpara">

<div class="title">

Mount options example

</div>

``` yaml
apiVersion: v1
kind: PersistentVolume
metadata:
  name: pv0001
spec:
  capacity:
    storage: 1Gi
  accessModes:
    - ReadWriteOnce
  mountOptions:
    - nfsvers=4.1
  nfs:
    path: /tmp
    server: 172.17.0.2
  persistentVolumeReclaimPolicy: Retain
  claimRef:
    name: claim1
    namespace: default
```

</div>

- Specified mount options are used while mounting the PV to the disk.

The following PV types support mount options:

- AWS Elastic Block Store (EBS)

- AWS Elastic File Storage (EFS)

- Azure Disk

- Azure File

- Cinder

- GCE Persistent Disk

- iSCSI

- Local volume

- NFS

- Red Hat OpenShift Data Foundation (Ceph RBD only)

- CIFS/SMB

- VMware vSphere

> [!NOTE]
> Fibre Channel and HostPath PVs do not support mount options.

<div>

<div class="title">

Additional resources

</div>

- [ReadWriteMany vSphere volume support](container_storage_interface/persistent-storage-csi-vsphere.md#persistent-storage-csi-vsphere-rwx_persistent-storage-csi-vsphere)

</div>

# Persistent volume claims

To define storage requirements for your workloads, review the structure of a `PersistentVolumeClaim` (PVC). This object includes a `spec` field to configure the request and a `status` field to monitor the current state of the claim.

<div class="formalpara">

<div class="title">

`PersistentVolumeClaim` object definition example

</div>

``` yaml
kind: PersistentVolumeClaim
apiVersion: v1
metadata:
  name: myclaim
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 8Gi
  storageClassName: gold
status:
# ...
```

</div>

where:

`apiVersion`
Specifies the name of the PVC.

`spec.accessModes`
Specifies the access mode, defining the read/write and mount permissions.

`requests.storage`
Specifies the amount of storage available to the PVC.

`storageClassName`
Specifies the name of the `StorageClass` required by the claim.

## Volume Attributes Classes

Volume Attributes Classes provide a way for administrators to describe "classes" of storage they offer. Different classes might correspond to different quality-of-service levels.

> [!IMPORTANT]
> Volume Attributes Classes is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.
>
> For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

Volume Attributes Classes in OpenShift Container Platform is available only with AWS Elastic Block Storage (EBS) and Google Cloud Platform (GCP) persistent disk (PD) Container Storage Interface (CSI).

You can apply a Volume Attributes Class to a persistent volume claim (PVC). If a new Volume Attributes Class becomes available in the cluster, a user can update the PVC with the new Volume Attributes Class if needed.

Volume Attributes Classes have parameters that describe volumes belonging to them. If a parameter is omitted, the default is used at volume provisioning. If you apply the PVC with a different Volume Attributes Class with omitted parameters, the default value of the parameters might be used depending on the CSI driver implementation. For more information, see the related CSI driver documentation.

### Limitations

Volume Attributes Classes has the following limitations:

- With GCP PD, volume modification using Volume Attributes Classes is only possible for hyperdisk-balanced disk types.

- No more than 512 parameters can be defined for a `VolumeAttributesClass`.

- The total length of the parameter’s object, including its keys and values, cannot exceed 256 KiB.

- If you apply a Volume Attributes Class to a PVC, you can change the applied Volume Attributes Class for that PVC, but you cannot delete it from the PVC. To delete the Volume Attributes Class from the PVC, you must delete the PVC, and then re-create the PVC.

- Volume Attributes Class parameters cannot be edited. If you need to change Volume Attributes Class parameters, create a new Volume Attributes Class with the desired parameters, and then apply it to a PVC.

### Enabling Volume Attributes Classes

Volume Attributes Classes are not enabled by default.

To enable Volume Attributes Classes, follow the procedure in section *Enabling OpenShift Container Platform features using FeatureGates*.

### Defining Volume Attributes Classes

The following is an example Volume Attributes Class YAML file for AWS EBS.

<div class="formalpara">

<div class="title">

`VolumeAttributesClass` AWE EBS definition example

</div>

``` yaml
apiVersion: storage.k8s.io/v1beta1
kind: VolumeAttributesClass
metadata:
  name: silver
driverName: ebs.csi.aws.com
parameters:
  iops: "300"
  throughput: "125"
  type: io2
  ...
```

</div>

- Defines object as Volumes Attributes Classes.

- Name of the `VolumeAttributesClass`. In this example, it is "silver".

- The provisioner that determines what volume plugin is used for provisioning persistent volumes (PVs). In this example, it is "ebs.csi.aws.com" for AWS EBS.

- Disk type.

The following is an example Volume Attributes Class YAML file for GPC PD.

<div class="formalpara">

<div class="title">

`VolumeAttributesClass` GPC PD definition example

</div>

``` yaml
apiVersion: storage.k8s.io/v1beta1
kind: VolumeAttributesClass
metadata:
  name: silver
driverName: pd.csi.storage.gke.io
parameters:
  iops: "3000"
  throughput: "150Mi"
  ...
```

</div>

- Defines object as Volumes Attributes Classes.

- Name of the `VolumeAttributesClass`. In this example, it is "silver".

- The provisioner that determines what volume plugin is used for provisioning persistent volumes (PVs). In this example, it is "pd.csi.storage.gke.io" for GPC PD.

### Applying a Volume Attributes Class to a PVC

In addition to newly created PVCs, you can also update existing bound PVCs with a Volume Attributes Class.

To apply a Volume Attributes Class to a PVC:

- Set the PVC’s `volumeAttributesClassName` parameter to the Volume Attributes Class’s name:

  <div class="formalpara">

  <div class="title">

  PVC definition example specifying a Volume Attributes Class

  </div>

  ``` yaml
  apiVersion: v1
  kind: PersistentVolumeClaim
  metadata:
    name: test-pv-claim
  spec:
    …
    volumeAttributesClassName: silver
  ```

  </div>

  - Specifies using the Volume Attributes Class "silver" for this PVC.

### Deleting Volume Attributes Classes

You cannot delete a Volume Attributes Class while it is in use by PVCs.

If you try to delete a Volume Attributes Class while it is still being used by a PVC, the command does not complete until all resources that use the Volume Attributes Class are updated to not use it.

To delete a Volume Attributes Class:

1.  Search for PVCs that are using Volume Attributes Classes by running the following command:

    ``` terminal
    $ oc get pvc -A -o jsonpath='{range .items[?(@.spec.volumeAttributesClassName=="<vac-name>")]}{.metadata.name}{"\n"}{end}'
    ```

    - \<vac-name\> = Volume Attributes Class name

      <div class="formalpara">

      <div class="title">

      Sample command output

      </div>

      ``` terminal
      $ mypvc
      ```

      </div>

2.  Then either:

    - Specify a different Volume Attributes Class name in the PVC’s `volumeAttributesClassName` parameter:

      <div class="formalpara">

      <div class="title">

      PVC definition example specifying a Volume Attributes Class

      </div>

      ``` yaml
      apiVersion: v1
      kind: PersistentVolumeClaim
      metadata:
      name: mypvc
      spec:
      …
      volumeAttributesClassName: silver
      ```

      </div>

      - Specify a different Volume Attributes Class. In this example, "silver".

        Or

    - Delete all PVCs that specify the Volume Attributes Class by running the following command:

      ``` terminal
      $ oc delete pvc <pvc-name>
      ```

      - Name of the PVC that you want to delete.

3.  Now that the Volume Attributes Class is no longer being used by any PVC, delete the Volume Attributes Class by running the following command:

    ``` terminal
    $ oc delete vac <vac-name>
    ```

    - Name of the Volume Attributes Class that you want to delete.

<div>

<div class="title">

Additional resources

</div>

- [Enabling OpenShift Container Platform features using FeatureGates](../nodes/clusters/nodes-cluster-enabling-features.md#nodes-cluster-enabling-features)

</div>

# Block volume support

OpenShift Container Platform can statically provision raw block volumes. These volumes do not have a file system, and can provide performance benefits for applications that either write to the disk directly or implement their own storage service.

Raw block volumes are provisioned by specifying `volumeMode: Block` in the PV and PVC specification.

> [!IMPORTANT]
> Pods using raw block volumes must be configured to allow privileged containers.

The following table displays which volume plugins support block volumes.

| Volume Plugin | Manually provisioned | Dynamically provisioned | Fully supported |
|----|----|----|----|
| Amazon Elastic Block Store (Amazon EBS) | ✅ | ✅ | ✅ |
| Amazon Elastic File Storage (Amazon EFS) |  |  |  |
| Azure Disk | ✅ | ✅ | ✅ |
| Azure File |  |  |  |
| Cinder | ✅ | ✅ | ✅ |
| Fibre Channel | ✅ |  | ✅ |
| GCP | ✅ | ✅ | ✅ |
| HostPath |  |  |  |
| IBM Cloud Block Storage volume | ✅ | ✅ | ✅ |
| iSCSI | ✅ |  | ✅ |
| Local volume | ✅ |  | ✅ |
| LVM Storage | ✅ | ✅ | ✅ |
| NFS |  |  |  |
| Red Hat OpenShift Data Foundation | ✅ | ✅ | ✅ |
| CIFS/SMB |  |  |  |
| VMware vSphere | ✅ | ✅ | ✅ |

Block volume support

> [!IMPORTANT]
> Using any of the block volumes that can be provisioned manually, but are not provided as fully supported, is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.
>
> For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

## Block volume examples

<div class="formalpara">

<div class="title">

PV example

</div>

``` yaml
apiVersion: v1
kind: PersistentVolume
metadata:
  name: block-pv
spec:
  capacity:
    storage: 10Gi
  accessModes:
    - ReadWriteOnce
  volumeMode: Block
  persistentVolumeReclaimPolicy: Retain
  fc:
    targetWWNs: ["50060e801049cfd1"]
    lun: 0
    readOnly: false
```

</div>

- `volumeMode` must be set to `Block` to indicate that this PV is a raw block volume.

<div class="formalpara">

<div class="title">

PVC example

</div>

``` yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: block-pvc
spec:
  accessModes:
    - ReadWriteOnce
  volumeMode: Block
  resources:
    requests:
      storage: 10Gi
```

</div>

- `volumeMode` must be set to `Block` to indicate that a raw block PVC is requested.

<div class="formalpara">

<div class="title">

`Pod` specification example

</div>

``` yaml
apiVersion: v1
kind: Pod
metadata:
  name: pod-with-block-volume
spec:
  containers:
    - name: fc-container
      image: fedora:26
      command: ["/bin/sh", "-c"]
      args: [ "tail -f /dev/null" ]
      volumeDevices:
        - name: data
          devicePath: /dev/xvda
  volumes:
    - name: data
      persistentVolumeClaim:
        claimName: block-pvc
```

</div>

- `volumeDevices`, instead of `volumeMounts`, is used for block devices. Only `PersistentVolumeClaim` sources can be used with raw block volumes.

- `devicePath`, instead of `mountPath`, represents the path to the physical device where the raw block is mapped to the system.

- The volume source must be of type `persistentVolumeClaim` and must match the name of the PVC as expected.

| Value      | Default |
|------------|---------|
| Filesystem | Yes     |
| Block      | No      |

Accepted values for `volumeMode`

| PV `volumeMode` | PVC `volumeMode` | Binding result |
|-----------------|------------------|----------------|
| Filesystem      | Filesystem       | Bind           |
| Unspecified     | Unspecified      | Bind           |
| Filesystem      | Unspecified      | Bind           |
| Unspecified     | Filesystem       | Bind           |
| Block           | Block            | Bind           |
| Unspecified     | Block            | No Bind        |
| Block           | Unspecified      | No Bind        |
| Filesystem      | Block            | No Bind        |
| Block           | Filesystem       | No Bind        |

Binding scenarios for block volumes

> [!IMPORTANT]
> Unspecified values result in the default value of `Filesystem`.

# Reduce pod timeouts by using fsGroup

To reduce pod timeouts when using a storage volume with many files, configure the `fsGroup` field. By specifying this field, you can manage how file ownership and permissions are applied, preventing delays caused by the default recursive permission changes on large volumes.

This can occur because, by default, OpenShift Container Platform recursively changes ownership and permissions for the contents of each volume to match the `fsGroup` specified in the `securityContext` of the pod when that volume is mounted. For volumes with many files, checking and changing ownership and permissions can be time consuming, slowing pod startup. You can use the `fsGroupChangePolicy` field inside a `securityContext` to control the way that OpenShift Container Platform checks and manages ownership and permissions for a volume.

`fsGroupChangePolicy` defines behavior for changing ownership and permission of the volume before being exposed inside a pod. This field only applies to volume types that support `fsGroup`-controlled ownership and permissions. This field has two possible values:

- `OnRootMismatch`: Only change permissions and ownership if permission and ownership of root directory does not match with expected permissions of the volume. This can help shorten the time it takes to change ownership and permission of a volume to reduce pod timeouts.

- `Always`: (Default) Always change permission and ownership of the volume when a volume is mounted.

> [!NOTE]
> The `fsGroupChangePolicy` field has no effect on ephemeral volume types, such as secret, configMap, and emptydir.

You can set `fsGroupChangePolicy` at either the namespace or pod level.

## Changing fsGroup at the namespace level

After applying the desired setting for `fsGroupChangePolicy` at the namespace level, all subsequently created pods in that namespace inherit the setting. However, if desired, you can override the inherited `fsGroupChangePolicy` setting for individual pods. Setting `fsGroupChangePolicy` at the pod level overrides inheritance from the namespace level setting for that pod.

<div>

<div class="title">

Prerequisites

</div>

- Logged in to a running OpenShift Container Platform cluster with administrator privileges.

- Access to the OpenShift Container Platform console.

</div>

<div class="formalpara">

<div class="title">

Procedure

</div>

To set `fsGroupChangePolicy` per namespace:

</div>

1.  Select the desired namespace:

    1.  Click **Administration** \> **Namespaces**.

    2.  On the **Namespaces** page, click the desired namespace. The **Namespace details** page appears.

2.  Add the `fsGroupChangePolicy` label to the namespace:

    1.  On the **Namespace details** page, next to **Labels**, click **Edit**.

    2.  In the **Edit labels** dialog, add the label `storage.openshift.io/fsgroup-change-policy` and set it equal to either:

        - `OnRootMismatch`: Specifies only changing permissions and ownership if the permission and the ownership of root directory does not match with expected permissions of the volume, thus helping to avoid pod timeout problems.

        - `Always`: (Default) Specifies always changing permission and ownership of the volume when a volume is mounted.

    3.  Click **Save**.

<div class="formalpara">

<div class="title">

Verification

</div>

Start up a pod in the previously edited namespace and observe that the parameter `spec.securityContext.fsGroupChangePolicy` contains the value that you set for the namespace.

</div>

<div class="formalpara">

<div class="title">

Example pod YAML file showing `fsGroupChangePolicy` setting

</div>

``` yaml
securityContext:
  seLinuxOptions:
    level: 's0:c27,c24'
  runAsNonRoot: true
  fsGroup: 1000750000
  fsGroupChangePolicy: OnRootMismatch
  ...
```

</div>

- This value is inherited from the namespace.

## Changing fsGroup at the pod level

You can set the set the `fsGroupChangePolicy` parameter in a new or existing deployment, and then the pods that it manages will have this parameter value. You can similarly do this for a statefulset. You cannot edit an existing pod to set `fsGroupChangePolicy`; however, you can set this parameter when creating a new pod.

This procedure describes how to set the `fsGroupChangePolicy` parameter in an existing deployment.

<div>

<div class="title">

Prerequisites

</div>

- Access to the OpenShift Container Platform console.

</div>

<div class="formalpara">

<div class="title">

Procedure

</div>

To set the `fsGroupChangePolicy` parameter in an existing deployment:

</div>

1.  Click **Workloads** \> **Deployments**.

2.  On the **Deployment** page, click the desired deployment.

3.  On the **Deployment details** page, click the **YAML** tab.

4.  Edit the deployment’s YAML file under `spec.template.spec.securityContext` using the following example file:

    <div class="formalpara">

    <div class="title">

    Example deployment YAML file setting `fsGroupChangePolicy`

    </div>

    ``` yaml
    ...
    spec:
    replicas: 3
    selector:
    matchLabels:
    app: my-app
    template:
    metadata:
    creationTimestamp: null
    labels:
    app: my-app
    spec:
    containers:
    - name: container
    image: 'image-registry.openshift-image-registry.svc:5000/openshift/httpd:latest'
    ports:
    - containerPort: 8080
    protocol: TCP
    resources: {}
    terminationMessagePath: /dev/termination-log
    terminationMessagePolicy: File
    imagePullPolicy: Always
    restartPolicy: Always
    terminationGracePeriodSeconds: 30
    dnsPolicy: ClusterFirst
    securityContext:
      fsGroupChangePolicy: OnRootMismatch
    ...
    ```

    </div>

    - `OnRootMismatch` specifies skipping recursive permission change, thus helping to avoid pod timeout problems. The default value is `Always`, which always changes permission and ownership of the volume when a volume is mounted.

5.  Click **Save**.

# Reducing pod timeouts using seLinuxChangePolicy

SELinux (Security-Enhanced Linux) is a security mechanism that assigns security labels (contexts) to all objects (files, processes, network ports, etc.) on a system. These labels determine what a process can access. In OpenShift Container Platform, SELinux helps prevent containers from escaping and accessing the host system or other containers.

When a pod starts, the container runtime recursively relabels all files on a volume to match the pod’s SELinux context. For volumes with many files, this can significantly increase pod startup times.

Mount option specifies avoiding recursive relabeling of all files by attempting to mount the volume with the correct SELinux label directly using the -o context mount option, thus helping to avoid pod timeout problems.

<div class="formalpara">

<div class="title">

RWOP and SELinux mount option

</div>

ReadWriteOncePod (RWOP) persistent volumes use the SELinux mount feature by default.

</div>

The mount option feature is driver dependent, and enabled by default in AWS EBS , Azure Disk, GCP PD, IBM Cloud Block Storage volume, Cinder, vSphere, and Red Hat OpenShift Data Foundation. For third-party drivers, contact your storage vendor.

<div class="formalpara">

<div class="title">

RWO and RWX and SELinux mount option

</div>

ReadWriteOnce (RWO) and ReadWriteMany (RWX) volumes use recursive relabeling by default.

</div>

> [!IMPORTANT]
> In a future OpenShift Container Platform version, RWO and RWX volumes will use **mount option by default**.

To assist you with the upcoming move to the mount option default, OpenShift Container Platform 4.20 reports SELinux-related conflicts when creating pods, and on running pods, to make you aware of potential conflicts, and to help you resolve them. For more information about this reporting, see this [Kowledge Base article](https://access.redhat.com/solutions/7131398).

If you are unable to resolve the SELinux-related conflicts, you can proactively opt-out of the future move to mount option as default for selected pods or namespaces. To opt out, see *Opting out of the SELinux mount option default*.

## Testing the RWO and RWX and SELinux mount option feature

In OpenShift Container Platform 4.20, you can evaluate the mount option feature for RWO and RWX volumes as a Technology Preview feature.

> [!IMPORTANT]
> RWO/RWX SELinux mount is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.
>
> For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

To evaluate the mount option feature:

- Enable Feature Gates. For information about enabling Feature Gates, see *Section Enabling features using feature gates*.

  RWO and RWX volumes now have mount option as the default behavior.

Carefully test your applications and observe how they are using storage. Consult this [Knowledge Base article](https://access.redhat.com/solutions/7131398) and consider opting out from using mount option if you are experiencing issues. See Section *Opting out of the SELinux mount option default*.

## Opting out of the SELinux mount option default

If you want to opt out of the future move to mount option as default, you can affirmatively set the `seLinuxChangePolicy` parameter to `Recursive` at either the individual pod or namespace level.

### Changing seLinuxChangePolicy at the namespace level

After applying the desired setting for `seLinuxChangePolicy` at the namespace level, all subsequently created pods in that namespace inherit the setting. However, if desired, you can override the inherited `seLinuxChangePolicy` setting for individual pods. Setting `seLinuxChangePolicy` at the pod level overrides inheritance from the namespace level setting for that pod.

<div>

<div class="title">

Prerequisites

</div>

- Logged in to a running OpenShift Container Platform cluster with administrator privileges.

- Access to the OpenShift Container Platform console.

</div>

<div class="formalpara">

<div class="title">

Procedure

</div>

To set `SELinuxChangePolicy` per namespace:

</div>

1.  Select the desired namespace:

    1.  Click **Administration** \> **Namespaces**.

    2.  On the **Namespaces** page, click the desired namespace. The **Namespace details** page appears.

2.  Add the `seLinuxChangePolicy` label to the namespace:

    1.  On the **Namespace details** page, next to **Labels**, click **Edit**.

    2.  In the **Edit labels** dialog, add the label `storage.openshift.io/selinux-change-policy=Recursive`.

        This specifies recursively relabeling all files on pod volumes to the appropriate SELinux context.

    3.  Click **Save**.

<div class="formalpara">

<div class="title">

Verification

</div>

Start up a pod in the previously edited namespace and observe that the parameter `spec.securityContext.seLinuxChangePolicy` is set to `Recursive`.

</div>

<div class="formalpara">

<div class="title">

Example pod YAML file showing `seLinuxChangePolicy` setting

</div>

``` yaml
securityContext:
    seLinuxOptions:
      level: 's0:c27,c19'
    runAsNonRoot: true
    fsGroup: 1000740000
    seccompProfile:
      type: RuntimeDefault
    seLinuxChangePolicy: Recursive
  ...
```

</div>

- This value is inherited from the namespace.

### Changing seLinuxChangePolicy at the pod level

You can set the set the `seLinuxChangePolicy` parameter in a new or existing Deployment, and then the pods that it manages will have this parameter value. You can similarly do this for a StatefulSet. You cannot edit an existing pod to set `seLinuxChangePolicy`; however, you can set this parameter when creating a new pod.

This procedure describes how to set the `seLinuxChangePolicy` parameter in an existing deployment.

<div>

<div class="title">

Prerequisites

</div>

- Access to the OpenShift Container Platform console.

</div>

<div class="formalpara">

<div class="title">

Procedure

</div>

To set the `seLinuxChangePolicy` parameter in an existing deployment:

</div>

1.  Click **Workloads** \> **Deployments**.

2.  On the **Deployment** page, click the desired deployment.

3.  On the **Deployment details** page, click the **YAML** tab.

4.  Edit the deployment’s YAML file under `spec.template.spec.securityContext` as per the following example file:

    <div class="formalpara">

    <div class="title">

    Example deployment YAML file setting `seLinuxChangePolicy`

    </div>

    ``` yaml
      ...
    securityContext:
      seLinuxChangePolicy: Recursive
      ...
    ```

    </div>

    - Specifies recursively relabeling all files on all pod volumes to the appropriate SELinux context.

5.  Click **Save**.
