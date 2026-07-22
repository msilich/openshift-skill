<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Container Storage Interface (CSI) volume cloning duplicates existing persistent volumes to create independent copies for data protection, testing, or deployment. You can use cloning to create new volumes from existing data without manual copying or backup restoration.

# Overview of CSI volume cloning

You can use Container Storage Interface (CSI) volume clones to create point-in-time duplicates of existing persistent volumes.

Volume cloning is similar to volume snapshots, although it is more efficient. For example, a cluster administrator can duplicate a cluster volume by creating another instance of the existing cluster volume.

Cloning creates an exact duplicate of the specified volume on the back-end device, rather than creating a new empty volume. After dynamic provisioning, you can use a volume clone just as you would use any standard volume.

No new API objects are required for cloning. The existing `dataSource` field in the `PersistentVolumeClaim` object is expanded so that it can accept the name of an existing PersistentVolumeClaim in the same namespace.

Before you provision a CSI volume clone, you should be familiar with persistent volumes. For information about persistent volumes, see *Understanding persistent volumes* in *Additional resources*.

## Support limitations

By default, OpenShift Container Platform supports CSI volume cloning with these limitations:

- The destination persistent volume claim (PVC) must exist in the same namespace as the source PVC.

- Cloning is supported with a different Storage Class.

  - Destination volume can be the same for a different storage class as the source.

  - You can use the default storage class and omit `storageClassName` in the `spec`.

- Support is only available for CSI drivers. In-tree and FlexVolumes are not supported.

- CSI drivers might not have implemented the volume cloning functionality. For details, see the CSI driver documentation.

# Provisioning a CSI volume clone

Create a new persistent volume claim (PVC) that specifies an existing PVC as its data source. The new volume automatically populates with a copy of the source PVC’s data and must be created in the same namespace as the source.

When you create a cloned persistent volume claim (PVC) API object, you trigger the provisioning of a CSI volume clone. The clone pre-populates with the contents of another PVC, adhering to the same rules as any other persistent volume. The one exception is that you must add a `dataSource` that references an existing PVC in the same namespace.

<div>

<div class="title">

Prerequisites

</div>

- You are logged in to a running OpenShift Container Platform cluster.

- Your PVC is created using a CSI driver that supports volume cloning.

- Your storage back end is configured for dynamic provisioning. Cloning support is not available for static provisioners.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create and save a file with the `PersistentVolumeClaim` object described by the following YAML:

    <div class="formalpara">

    <div class="title">

    Example pvc-clone.yaml

    </div>

    ``` yaml
    apiVersion: v1
    kind: PersistentVolumeClaim
    metadata:
      name: pvc-1-clone
      namespace: mynamespace
    spec:
      storageClassName: csi-cloning
      accessModes:
        - ReadWriteOnce
      resources:
        requests:
          storage: 5Gi
      dataSource:
        kind: PersistentVolumeClaim
        name: pvc-1
    ```

    </div>

    Where `spec.storageClassName` is the name of the storage class that provisions the storage back end. The default storage class can be used and `storageClassName` can be omitted in the spec.

2.  Create the object you saved in the previous step by running the following command:

    ``` terminal
    $ oc create -f pvc-clone.yaml
    ```

    A new PVC `pvc-1-clone` is created.

3.  Verify that the volume clone was created and is ready by running the following command:

    ``` terminal
    $ oc get pvc pvc-1-clone
    ```

    The `pvc-1-clone` shows that it is `Bound`.

    You are now ready to use the newly cloned PVC to configure a pod.

4.  Create and save a file with the `Pod` object described by the YAML. For example:

    <div class="formalpara">

    <div class="title">

    Example pod YAML file

    </div>

    ``` yaml
    kind: Pod
    apiVersion: v1
    metadata:
      name: mypod
    spec:
      containers:
        - name: myfrontend
          image: dockerfile/nginx
          volumeMounts:
          - mountPath: "/var/www/html"
            name: mypd
      volumes:
        - name: mypd
          persistentVolumeClaim:
            claimName: pvc-1-clone
    ```

    </div>

    Where `spec.volumes.persistentVolumeClaim.claimName` is the cloned PVC created during the CSI volume cloning operation.

</div>

<div class="formalpara">

<div class="title">

Result

</div>

The created `Pod` object is now ready to consume, clone, snapshot, or delete your cloned PVC independently of its original `dataSource` PVC.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Understanding persistent volumes](../understanding-persistent-storage.md#persistent-volumes_understanding-persistent-storage)

</div>
