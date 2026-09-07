<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

A hostPath volume mounts a file or directory from the host node’s filesystem into your pod. Use hostPath volumes primarily for testing or development, as they require privileged pods and grant access to the host node’s filesystem.

# Overview of hostPath

A hostPath volume mounts files or directories from the host node’s filesystem into pods for development and testing on single-node clusters. Because hostPath requires privileged pods and must be statically provisioned, it is not recommended for production. Use network storage with dynamic provisioning instead.

> [!IMPORTANT]
> The cluster administrator must configure pods to run as privileged. This grants access to pods in the same node.

Most pods do not need a hostPath volume, but it does offer a quick option for testing should an application require it.

In a production cluster, you would not use hostPath. Instead, a cluster administrator would provision a network resource, such as a GCE Persistent Disk volume, an NFS share, or an Amazon EBS volume. Network resources support the use of storage classes to set up dynamic provisioning.

A hostPath volume must be provisioned statically.

> [!IMPORTANT]
> Do not mount to the container root, `/`, or any path that is the same in the host and the container. This can corrupt your host system if the container is sufficiently privileged. It is safe to mount the host by using `/host`. The following example shows the `/` directory from the host being mounted into the container at `/host`.
>
> ``` yaml
> apiVersion: v1
> kind: Pod
> metadata:
>   name: test-host-mount
> spec:
>   containers:
>   - image: registry.access.redhat.com/ubi9/ubi
>     name: test-container
>     command: ['sh', '-c', 'sleep 3600']
>     volumeMounts:
>     - mountPath: /host
>       name: host-slash
>   volumes:
>    - name: host-slash
>      hostPath:
>        path: /
>        type: ''
> ```

# Statically provisioning hostPath volumes

Statically provision hostPath volumes by creating a persistent volume (PV) that maps to a path on the host node’s filesystem, then creating a persistent volume claim (PVC) that binds to the PV. Dynamic provisioning is not supported for hostPath volumes.

A pod that uses a hostPath volume must be referenced by manual (static) provisioning.

<div>

<div class="title">

Procedure

</div>

1.  Define the persistent volume (PV) by creating a `pv.yaml` file with the `PersistentVolume` object definition:

    ``` yaml
    apiVersion: v1
    kind: PersistentVolume
    metadata:
      name: task-pv-volume
      labels:
        type: local
    spec:
      storageClassName: manual
      capacity:
        storage: 5Gi
      accessModes:
        - ReadWriteOnce
      persistentVolumeReclaimPolicy: Retain
      hostPath:
        path: "/mnt/data"
    ```

    - `metadata.name`: Specifies the name of the volume. This name is how the volume is identified by persistent volume (PV) claims or pods.

    - `spec.storageClassName`: The storage class is used to bind persistent volume claim (PVC) requests to the PV.

    - `spec.accessModes`: Specifies the access mode. The volume can be mounted as `read-write` by a single node.

    - `spec.hostPath.path`: The configuration file specifies that the volume is at `/mnt/data` on the cluster’s node. To avoid corrupting your host system, do not mount to the container root, `/`, or any path that is the same in the host and the container. You can safely mount the host by using `/host`

2.  Create the PV from the file:

    ``` terminal
    $ oc create -f pv.yaml
    ```

3.  Define the PVC by creating a `pvc.yaml` file with the `PersistentVolumeClaim` object definition:

    ``` yaml
    apiVersion: v1
    kind: PersistentVolumeClaim
    metadata:
      name: task-pvc-volume
    spec:
      accessModes:
        - ReadWriteOnce
      resources:
        requests:
          storage: 1Gi
      storageClassName: manual
    ```

4.  Create the PVC from the file:

    ``` terminal
    $ oc create -f pvc.yaml
    ```

</div>

# Mounting the hostPath share in a privileged pod

Mount a hostPath share in a privileged pod by referencing an existing persistent volume claim (PVC) in the pod specification. The pod must run as privileged to access the node’s storage. Do not mount to the container root or any path that matches the host to avoid corrupting the host system.

After the PVC has been created, it can be used inside by an application. The following example demonstrates mounting this share inside of a pod.

<div>

<div class="title">

Prerequisites

</div>

- A persistent volume claim exists that is mapped to the underlying hostPath share.

</div>

<div>

<div class="title">

Procedure

</div>

- Create a privileged pod that mounts the existing persistent volume claim:

  ``` yaml
  apiVersion: v1
  kind: Pod
  metadata:
    name: pod-name
  spec:
    containers:
      ...
      securityContext:
        privileged: true
      volumeMounts:
      - mountPath: /data
        name: hostpath-privileged
    ...
    securityContext: {}
    volumes:
      - name: hostpath-privileged
        persistentVolumeClaim:
          claimName: task-pvc-volume
  ```

  - `metadata.name`: Specifies the name of the pod.

  - `spec.containers.securityContext.privileged`: The pod must run as privileged to access the node’s storage.

  - `spec.containers.volumeMounts.mountPath`: The path to mount the host path share inside the privileged pod. Do not mount to the container root, `/`, or any path that is the same in the host and the container. This can corrupt your host system if the container is sufficiently privileged, such as the host `/dev/pts` files. It is safe to mount the host by using `/host`.

  - `spec.volumes.persistentVolumeClaim.claimName`: Specifies the name of the `PersistentVolumeClaim` object that has been previously created.

</div>
