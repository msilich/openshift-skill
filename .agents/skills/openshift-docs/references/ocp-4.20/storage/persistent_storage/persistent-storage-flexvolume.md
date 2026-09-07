<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

To use storage from a back-end that does not have a built-in plugin, you can extend OpenShift Container Platform through FlexVolume drivers and provide persistent storage to applications.

FlexVolume is an out-of-tree plugin that uses an executable model to interface with drivers.

> [!IMPORTANT]
> FlexVolume is a deprecated feature. Deprecated functionality is still included in OpenShift Container Platform and continues to be supported; however, it will be removed in a future release of this product and is not recommended for new deployments.
>
> Out-of-tree Container Storage Interface (CSI) driver is the recommended way to write volume drivers in OpenShift Container Platform. Maintainers of FlexVolume drivers should implement a CSI driver and move users of FlexVolume to CSI. Users of FlexVolume should move their workloads to CSI driver.
>
> For the most recent list of major functionality that has been deprecated or removed within OpenShift Container Platform, refer to the *Deprecated and removed features* section of the OpenShift Container Platform release notes.

Pods interact with FlexVolume drivers through the `flexvolume` in-tree plugin.

<div>

<div class="title">

Additional resources

</div>

- [Expanding persistent volumes](../expanding-persistent-volumes.md#expanding-persistent-volumes)

</div>

# About FlexVolume drivers

When working with FlexVolume drivers, it is helpful to understand how OpenShift Container Platform interact with the drivers.

A FlexVolume driver is an executable file that resides in a well-defined directory on all nodes in the cluster. OpenShift Container Platform calls the FlexVolume driver whenever it needs to mount or unmount a volume represented by a `PersistentVolume` object with `flexVolume` as the source.

> [!IMPORTANT]
> Attach and detach operations are not supported in OpenShift Container Platform for FlexVolume.

# FlexVolume driver example

When working with FlexVolume drivers, it is helpful to become familiar with structure of the driver.

The first command-line argument of the FlexVolume driver is always an operation name. Other parameters are specific to each operation. Most of the operations take a JavaScript Object Notation (JSON) string as a parameter. This parameter is a complete JSON string, and not the name of a file with the JSON data.

The FlexVolume driver contains:

- All `flexVolume.options`.

- Some options from `flexVolume` prefixed by `kubernetes.io/`, such as `fsType` and `readwrite`.

- The content of the referenced secret, if specified, prefixed by `kubernetes.io/secret/`.

<div class="formalpara">

<div class="title">

FlexVolume driver JSON input example

</div>

``` json
{
    "fooServer": "192.168.0.1:1234",
        "fooVolumeName": "bar",
    "kubernetes.io/fsType": "ext4",
    "kubernetes.io/readwrite": "ro",
    "kubernetes.io/secret/<key name>": "<key value>",
    "kubernetes.io/secret/<another key name>": "<another key value>",
}
```

</div>

where:

`fooServer`
Specifies all options from `flexVolume.options`.

`kubernetes.io/fsType`
Specifies the value of `flexVolume.fsType`.

`kubernetes.io/readwrite`
Specifies the value `ro` or `rw` based on `flexVolume.readOnly`.

`kubernetes.io/secret/<key name>`
Specifies all keys and their values from the secret referenced by `flexVolume.secretRef`.

OpenShift Container Platform expects JSON data on standard output of the driver. When not specified, the output describes the result of the operation.

<div class="formalpara">

<div class="title">

FlexVolume driver default output example

</div>

``` json
{
    "status": "<Success/Failure/Not supported>",
    "message": "<Reason for success/failure>"
}
```

</div>

Exit code of the driver should be `0` for success and `1` for error.

Operations should be idempotent, which means that the mounting of an already mounted volume should result in a successful operation.

# Installing FlexVolume drivers

You can implement FlexVolumes by using a list of operations to call and the installation path are all that is required. FlexVolume drivers that are used to extend OpenShift Container Platform are executed only on the node.

<div>

<div class="title">

Prerequisites

</div>

- FlexVolume drivers must implement these operations:

  `init`
  Initializes the driver. It is called during initialization of all nodes.

  - Arguments: none

  - Executed on: node

  - Expected output: default JSON

  `mount`
  Mounts a volume to directory. This can include anything that is necessary to mount the volume, including finding the device and then mounting the device.

  - Arguments: `<mount-dir>` `<json>`

  - Executed on: node

  - Expected output: default JSON

  `unmount`
  Unmounts a volume from a directory. This can include anything that is necessary to clean up the volume after unmounting.

  - Arguments: `<mount-dir>`

  - Executed on: node

  - Expected output: default JSON

  `mountdevice`
  Mounts a volume’s device to a directory where individual pods can then bind mount.

  This call-out does not pass "secrets" specified in the FlexVolume spec. If your driver requires secrets, do not implement this call-out.

  - Arguments: `<mount-dir>` `<json>`

  - Executed on: node

  - Expected output: default JSON

  `unmountdevice`
  Unmounts a volume’s device from a directory.

  - Arguments: `<mount-dir>`

  - Executed on: node

  - Expected output: default JSON

- All other operations should return JSON with `{"status": "Not supported"}` and exit code `1`.

</div>

<div class="formalpara">

<div class="title">

Procedure

</div>

To install the FlexVolume driver:

</div>

1.  Ensure that the executable file exists on all nodes in the cluster.

2.  Place the executable file at the volume plugin path: `/etc/kubernetes/kubelet-plugins/volume/exec/<vendor>~<driver>/<driver>`.

    For example, to install the FlexVolume driver for the storage `foo`, place the executable file at: `/etc/kubernetes/kubelet-plugins/volume/exec/openshift.com~foo/foo`.

# Consuming storage using FlexVolume drivers

You can consume a Fibre Channel volume by using a `PersistentVolume` object.

Each `PersistentVolume` object in OpenShift Container Platform represents one storage asset in the storage back-end, such as a volume.

<div>

<div class="title">

Procedure

</div>

- Use the `PersistentVolume` object to reference the installed storage.

  <div class="formalpara">

  <div class="title">

  Persistent volume object definition using FlexVolume drivers example

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
    flexVolume:
      driver: openshift.com/foo
      fsType: "ext4"
      secretRef: foo-secret
      readOnly: true
      options:
        fooServer: 192.168.0.1:1234
        fooVolumeName: bar
  ```

  </div>

  where:

  `metadata.name`
  Specifies the name of the volume. This is how it is identified through persistent volume claims or from pods. This name can be different from the name of the volume on back-end storage.

  `spec.capacity.storage`
  Specifies the amount of storage allocated to this volume.

  `spec.flexVolume.driver`
  Specifies the name of the driver. This field is mandatory.

  `spec.flexVolume.fsType`
  Specifies the file system that is present on the volume. This field is optional.

  `spec.flexVolume.secretRef`
  Specifies the reference to a secret. Keys and values from this secret are provided to the FlexVolume driver on invocation. This field is optional.

  `spec.flexVolume.readOnly`
  Specifies the read-only flag. This field is optional.

  `spec.flexVolume.options`
  Specifies the additional options for the FlexVolume driver. In addition to the flags specified by the user in the `options` field, the following flags are also passed to the executable:

  "fsType":"\<FS type\>", "readwrite":"\<rw\>", "secret/key1":"\<secret1\>" "secret/keyN":"\<secretN\>"

</div>

> [!NOTE]
> Secrets are passed only to mount or unmount call-outs.
