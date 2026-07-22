<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Generic ephemeral volumes provide per-pod temporary storage backed by any storage driver that supports dynamic provisioning, unlike `emptyDir` volumes which are limited to local node storage. This flexibility lets you use network storage backends, control storage classes and volume characteristics, and leverage delayed volume binding for optimal pod scheduling.

# Overview of generic ephemeral volumes

Generic ephemeral volumes support network-attached storage, size limits, initial data population, and operations like cloning and snapshotting for temporary storage, with some driver-specific limitations.

Generic ephemeral volumes have the following features:

- Storage can be local or network-attached.

- Volumes can have a fixed size that pods cannot exceed.

- Volumes might have some initial data, depending on the driver and parameters.

- Typical operations on volumes are supported, assuming that the driver supports them, including snapshotting, cloning, resizing, and storage capacity tracking.

> [!NOTE]
> Generic ephemeral volumes do not support offline snapshotting and resizing.
>
> Due to this limitation, the following Container Storage Interface (CSI) drivers do not support the following features for generic ephemeral volumes:
>
> - Azure Disk CSI driver does not support resize.
>
> - Cinder CSI driver does not support snapshot.

# Lifecycle and persistent volume claims

Generic ephemeral volumes follow pod lifecycle through automatically managed persistent volume claims created at pod startup and deleted at termination. Choose volume binding mode and reclaim policy based on this lifecycle behavior.

Generic ephemeral volumes are specified inline in the pod spec and follow the pod’s lifecycle. They are created and deleted along with the pod.

The parameters for a volume claim are allowed inside a volume source of a pod. Labels, annotations, and the whole set of fields for PVCs are supported. When such a pod is created, the ephemeral volume controller then creates an actual PVC object (from the template shown in the *Creating generic ephemeral volumes* procedure) in the same namespace as the pod, and ensures that the PVC is deleted when the pod is deleted.

This triggers volume binding and provisioning in one of two ways:

- Either immediately, if the storage class uses immediate volume binding.

  With immediate binding, the scheduler is forced to select a node that has access to the volume after it is available.

- When the pod is tentatively scheduled onto a node (`WaitForFirstConsumer` volume binding mode).

  This volume binding option is recommended for generic ephemeral volumes because then the scheduler can choose a suitable node for the pod.

In terms of resource ownership, a pod that has generic ephemeral storage is the owner of the PVCs that provide that ephemeral storage. When the pod is deleted, the Kubernetes garbage collector deletes the PVC, which then usually triggers deletion of the volume because the default reclaim policy of storage classes is to delete volumes. You can create quasi-ephemeral local storage by using a storage class with a reclaim policy of retain. The storage outlives the pod, and in this case, you must ensure that volume clean-up happens separately. While these PVCs exist, they can be used like any other PVC. In particular, they can be referenced as data sources in volume cloning or snapshotting. The PVC object also holds the current status of the volume.

<div>

<div class="title">

Additional resources

</div>

- [Creating generic ephemeral volumes](generic-ephemeral-vols.md#generic-ephemeral-vols-procedure_generic-ephemeral-volumes)

</div>

# Security

Generic ephemeral volumes allow users who can create pods to indirectly create persistent volume claims (PVCs), even without direct PVC creation permissions. You can restrict this behavior if it conflicts with your security model.

To restrict this behavior, use an admission webhook that rejects objects such as pods that have a generic ephemeral volume.

The normal namespace quota for PVCs still applies, so even if users are allowed to use this new mechanism, they cannot use it to circumvent other policies.

# Persistent volume claim naming

Automatically created persistent volume claims (PVCs) are named using pod name and volume name with a hyphen separator, potentially causing conflicts with other pods or manual PVCs.

For example, `pod-a` with volume `scratch` and `pod` with volume `a-scratch` both end up with the same PVC name, `pod-a-scratch`.

Such conflicts are detected, and a PVC is only used for an ephemeral volume if it was created for the pod. This check is based on the ownership relationship. An existing PVC is not overwritten or modified, but this does not resolve the conflict. Without the right PVC, a pod cannot start.

> [!IMPORTANT]
> Be careful when naming pods and volumes inside the same namespace so that naming conflicts do not occur.

# Creating generic ephemeral volumes

To create ephemeral volumes that are automatically provisioned and deleted with pod lifecycle, define a `volumeClaimTemplate` in your pod spec specifying storage class, size, and access modes.

<div>

<div class="title">

Procedure

</div>

1.  Create the `pod` object definition and save it to a file.

2.  Include the generic ephemeral volume information in the file.

    <div class="formalpara">

    <div class="title">

    my-example-pod-with-generic-vols.yaml

    </div>

    ``` yaml
    kind: Pod
    apiVersion: v1
    metadata:
      name: my-app
    spec:
      containers:
        - name: my-frontend
          image: busybox:1.28
          volumeMounts:
          - mountPath: "/mnt/storage"
            name: data
          command: [ "sleep", "1000000" ]
      volumes:
        - name: data
          ephemeral:
            volumeClaimTemplate:
              metadata:
                labels:
                  type: my-app-ephvol
              spec:
                accessModes: [ "ReadWriteOnce" ]
                storageClassName: "gp2-csi"
                resources:
                  requests:
                    storage: 1Gi
    ```

    </div>

    Where `spec.volumes.name` is the name of the generic ephemeral volume.

</div>
