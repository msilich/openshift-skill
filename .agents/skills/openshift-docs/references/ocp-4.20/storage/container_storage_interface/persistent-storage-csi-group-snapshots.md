<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

This document describes how to use volume group snapshots with supported Container Storage Interface (CSI) drivers to help protect against data loss in OpenShift Container Platform. Familiarity with [persistent volumes](../understanding-persistent-storage.md#persistent-volumes_understanding-persistent-storage) is suggested.

> [!IMPORTANT]
> CSI volume group snapshots is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.
>
> For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

To use this Technology Preview feature, you must enable it using feature gates.

# Overview of CSI volume group snapshots

A *snapshot* represents the state of the storage volume in a cluster at a particular point in time. Volume snapshots can be used to provision a new volume.

A *volume group snapshot* uses a label selector to group multiple persistent volume claims for snapshotting. A volume group snapshot represents copies from multiple volumes that are taken at the same point-in-time. This can be useful for applications that contain multiple volumes.

Container Storage Interface (CSI) volume group snapshots needs to be supported by the CSI driver. OpenShift Data Foundation supports volume group snapshots.

Volume group snapshots provide three new API objects for managing snapshots:

`VolumeGroupSnapshot`
Requests creation of a volume group snapshot for multiple persistent volume claims. It contains information about the volume group snapshot operation, such as the timestamp when the volume group snapshot was taken, and whether it is ready to use.

`VolumeGroupSnapshotContent`
Created by the snapshot controller for a dynamically created volumeGroupSnapshot. It contains information about the volume group snapshot including the volume group snapshot ID. This object represents a provisioned resource on the cluster (a group snapshot). The `VolumeGroupSnapshotContent` object binds to the volume group snapshot for which it was created with a one-to-one mapping.

`VolumeGroupSnapshotClass`
Created by cluster administrators to describe how volume group snapshots should be created, including the driver information, the deletion policy, etc.

These three API kinds are defined as `CustomResourceDefinitions` (CRDs). These CRDs must be installed in a OpenShift Container Platform cluster for a CSI driver to support volume group snapshots.

# CSI volume group snapshots limitations

Volume group snapshots has the following limitations:

- Does not support reverting an existing persistent volume claim (PVC) to an earlier state represented by a snapshot It only supports provisioning a new volume from a snapshot.

- No guarantees of application consistency, for example, crash consistency, are provided beyond those provided by the storage system. For more information about application consistency, see [Quiesce and Unquiesce Hooks](https://github.com/kubernetes/community/blob/master/wg-data-protection/data-protection-workflows-white-paper.md#quiesce-and-unquiesce-hooks).

# Creating a volume group snapshot class

Before you can create volume group snapshots, the cluster administrator needs to create a `VolumeGroupSnapshotClass`.

This object describes how volume group snapshots should be created, including the driver information, the deletion policy, etc.

<div>

<div class="title">

Prerequisites

</div>

- Logged in to a running OpenShift Container Platform cluster with administrator privileges.

- Enabled this feature using feature gates. For information about how to use feature gates, see *Enabling features sets by using feature gates*.

</div>

<div class="formalpara">

<div class="title">

Procedure

</div>

To create a `VolumeGroupSnapshotClass`:

</div>

1.  Create a `VolumeGroupSnapshotClass` YAML file using the following example file:

    <div class="formalpara">

    <div class="title">

    Example volume group snapshot class YAML file

    </div>

    ``` yaml
    apiVersion: groupsnapshot.storage.k8s.io/v1beta1
    kind: VolumeGroupSnapshotClass
    metadata:
      name: csi-hostpath-groupsnapclass
    deletionPolicy: Delete
    driver: hostpath.csi.k8s.io
         …...
    ```

    </div>

    - Specifies the `VolumeGroupSnapshotClass` object.

    - Name of the `VolumeGroupSnapshotClass`.

2.  Create the 'VolumeGroupSnapshotClass' object by running the following command:

    ``` terminal
    $ oc create -f <volume-group-snapshot-class-filename>.yaml
    ```

# Creating a volume group snapshot

When you create a `VolumeGroupSnapshot` object, OpenShift Container Platform creates a volume group snapshot.

<div>

<div class="title">

Prerequisites

</div>

- Logged in to a running OpenShift Container Platform cluster.

- Enabled this feature using feature gates. For information about how to use feature gates, see *Enabling features sets by using feature gates*.

- The persistent volume claims (PVCs) that you want to group for the snapshot have been created using a CSI driver that supports `VolumeGroupSnapshot` objects.

- A storage class to provision the storage back end.

- Administrator has created the `VolumeGroupSnapshotClass` object.

</div>

<div class="formalpara">

<div class="title">

Procedure

</div>

To create a volume group snapshot:

</div>

1.  Locate (or create) the PVCs that you want to include in the volume group snapshot:

    ``` terminal
    $ oc get pvc
    ```

    <div class="formalpara">

    <div class="title">

    Example command output

    </div>

    ``` terminal
    NAME        STATUS    VOLUME                                     CAPACITY   ACCESSMODES   AGE
    pvc-0       Bound     pvc-a42d7ea2-e3df-11ed-b5ea-0242ac120002   1Gi        RWO           48s
    pvc-1       Bound     pvc-a42d81b8-e3df-11ed-b5ea-0242ac120002   1Gi        RWO           48S
    ```

    </div>

    This example uses two PVCs

2.  Label the PVCs to belong to a snapshot group:

    1.  Label PVC pvc-0 by running the following command:

        ``` terminal
        $ oc label pvc pvc-0 group=myGroup
        ```

        <div class="formalpara">

        <div class="title">

        Example output

        </div>

        ``` terminal
        persistentvolumeclaim/pvc-0 labeled
        ```

        </div>

    2.  Label PVC pvc-1 by running the following command:

        ``` terminal
        $ oc label pvc pvc-1 group=myGroup
        ```

        <div class="formalpara">

        <div class="title">

        Example output

        </div>

        ``` terminal
        persistentvolumeclaim/pvc-1 labeled
        ```

        </div>

        In this example, you are labeling PVC "pvc-0" and "pvc-1" to belong to group "myGroup".

3.  Create a `VolumeGroupSnapshot` object to specify your volume group snapshot:

    1.  Create a `VolumeGroupSnapshot` object YAML file with the following example file:

        <div class="formalpara">

        <div class="title">

        Example VolumeGroupSnapshot YAML file

        </div>

        ``` yaml
        apiVersion: groupsnapshot.storage.k8s.io/v1beta1
        kind: VolumeGroupSnapshot
        metadata:
          name: <volume-group-snapshot-name>
          namespace: <namespace>
        spec:
          volumeGroupSnapshotClassName: <volume-group-snapshot-class-name>
          source:
            selector:
              matchLabels:
                group: myGroup
        ```

        </div>

        - The `VolumeGroupSnapshot` object requests creation of a volume group snapshot for multiple PVCs.

        - Name of the volume group snapshot.

        - Namespace for the volume group snapshot.

        - The `VolumeGroupSnapshotClass` name. This object is created by the administrator and describes how volume group snapshots should be created.

        - The name of the label used to group the desired PVCs for the snapshot. In this example, it is "myGroup".

    2.  Create the `VolumeGroupSnapshot` object by running the following command:

        ``` terminal
        $ oc create -f <volume-group-snapshot-filename>.yaml
        ```

<div class="formalpara">

<div class="title">

Results

</div>

Individual volume snapshots are created according to how many PVCs were specified as part of the volume group snapshot.

</div>

These individual volume snapshots are named with the following format: \<hash of VolumeGroupSnaphotContentUUID+volumeHandle\>:

<div class="formalpara">

<div class="title">

Example individual volume snapshot

</div>

``` yaml
apiVersion: snapshot.storage.k8s.io/v1
kind: VolumeSnapshot
metadata:
  name: snapshot-4dc1c53a29538b36e85003503a4bcac5dbde4cff59e81f1e3bb80b6c18c3fd03
  namespace: default
  ownerReferences:
  - apiVersion: groupsnapshot.storage.k8s.io/v1beta1
    kind: VolumeGroupSnapshot
    name: my-groupsnapshot
    uid: ba2d60c5-5082-4279-80c2-daa85f0af354
  resourceVersion: "124503"
  uid: c0137282-f161-4e86-92c1-c41d36c6d04c
spec:
  source:
    persistentVolumeClaimName:pvc-1
status:
  volumeGroupSnapshotName: volume-group-snapshot-name
```

</div>

In the preceding example, two individual volume snapshots are created as part of the volume group snapshot.

``` terminal
snapshot-4dc1c53a29538b36e85003503a4bcac5dbde4cff59e81f1e3bb80b6c18c3fd03
snapshot-fbfe59eff570171765df664280910c3bf1a4d56e233a5364cd8cb0152a35965b
```

# Restoring a volume group snapshot

You can use the `VolumeGroupSnapshot` custom resource definition (CRD) content to restore the existing volumes to a previous state.

To restore existing volumes, you can request a new persistent volume claim (PVC) to be created from a `VolumeSnapshot` object that is part of a `VolumeGroupSnapshot`. This triggers provisioning of a new volume that is populated with data from the specified snapshot. Repeat this process until all volumes are created from all the snapshots that are part of a volume group snapshot.

<div>

<div class="title">

Prerequisites

</div>

- Logged in to a running OpenShift Container Platform cluster.

- PVC has been created using a Container Storage Interface (CSI) driver that supports volume group snapshots.

- A storage class to provision the storage back end.

- A volume group snapshot has been created and is ready to use.

</div>

<div class="formalpara">

<div class="title">

Procedure

</div>

To restore existing volumes to a previous state from a volume group snapshot:

</div>

1.  Specify a `VolumeSnapshot` data source from a volume group snapshot for a PVC as shown in the following example:

    <div class="formalpara">

    <div class="title">

    Example restore PVC YAML file

    </div>

    ``` yaml
    apiVersion: v1
    kind: PersistentVolumeClaim
    metadata:
      name: <pvc-restore-name>
      namespace: <namespace>
    spec:
      storageClassName: csi-hostpath-sc
      dataSource:
        name: snapshot-fbfe59eff570171765df664280910c3bf1a4d56e233a5364cd8cb0152a35965b
        kind: VolumeSnapshot
        apiGroup: snapshot.storage.k8s.io
      accessModes:
        - ReadWriteOnce
      resources:
        requests:
          storage: 1Gi
    ```

    </div>

    - Name of the restore PVC.

    - Name of the namespace.

    - Name of an individual volume snapshot that is part of the volume group snapshot to use as source.

    - Must be set to the `VolumeSnapshot` value.

    - Must be set to the `snapshot.storage.k8s.io` value

2.  Create the PVC by running the following command:

    ``` terminal
    $ oc create -f <pvc-restore-filename>.yaml
    ```

    - Name of the PVC restore file specified in the preceding step.

3.  Verify that the restored PVC has been created by running the following command:

    ``` terminal
    $ oc get pvc
    ```

    A new PVC with the name you specified in the first step appears.

4.  Repeat the procedure as needed until all volumes are created from all the snapshots that are part of a volume group snapshot.

# Additional resources

- [CSI volume snapshots](persistent-storage-csi-snapshots.md#persistent-storage-csi-snapshots)

- [Enabling features sets by using feature gates](../../hosted_control_planes/hcp-using-feature-gates.md#hcp-enable-feature-sets_hcp-using-feature-gates)
