> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/develop-proc_requesting_persistent_storage_with_pvc). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Request persistent storage in a PVC

Request persistent storage by applying a PersistentVolumeClaim (PVC) to provision a PersistentVolume (PV) for your workspaces, so that data persists beyond workspace restarts and can be shared across workspaces.

## Before you begin

- You have not started the workspace.

<!-- -->

- You have an active `oc` session with administrative permissions to the OpenShift cluster. See [Getting started with the CLI](https://docs.openshift.com/container-platform/4.22/cli_reference/openshift_cli/getting-started-cli.html).
- You have a PVC created in your user project to mount to all `Dev Workspace` containers.

## About this task

A PVC is useful in the following cases:

- Not all developers of the project need the PV.
- The PV lifecycle goes beyond the lifecycle of a single workspace.
- The data included in the PV are shared across workspaces.

This also applies to ephemeral workspaces with the `controller.devfile.io/storage-type: ephemeral` attribute.

## Procedure

1.  Add the `controller.devfile.io/mount-to-devworkspace: true` label to the PVC.

    ``` bash
    $ oc label persistentvolumeclaim <PVC_name> \
              controller.devfile.io/mount-to-devworkspace=true
    ```

2.  Optional: Use the annotations to configure how the PVC is mounted: <span id="proc_requesting-persistent-storage-with-pvc_devspaces__entry__1"></span><span id="proc_requesting-persistent-storage-with-pvc_devspaces__entry__2"></span>

    <table>
    <caption>Table 1. Optional annotations</caption>
    <thead>
    <tr>
    <th>Annotation</th>
    <th>Description</th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td><p><code>controller.devfile.io/mount-path:</code></p></td>
    <td><p>The mount path for the PVC.</p>
    <p>Defaults to <code>/tmp/</code><em><code>&lt;PVC_name&gt;</code></em>.</p></td>
    </tr>
    <tr>
    <td><p><code>controller.devfile.io/read-only:</code></p></td>
    <td><p>Set to <code>'true'</code> or <code>'false'</code> to specify whether the PVC is to be mounted as read-only.</p>
    <p>Defaults to <code>'false'</code>, resulting in the PVC mounted as read/write.</p></td>
    </tr>
    </tbody>
    </table>

    For example, to mount a read-only PVC:

    ``` yaml
    apiVersion: v1
    kind: PersistentVolumeClaim
    metadata:
      name: <pvc_name>
      labels:
        controller.devfile.io/mount-to-devworkspace: 'true'
      annotations:
        controller.devfile.io/mount-path: </example/directory>
        controller.devfile.io/read-only: 'true'
    spec:
      accessModes:
        - ReadWriteOnce
      resources:
        requests:
          storage: 3Gi
      storageClassName: <storage_class_name>
      volumeMode: Filesystem
    ```

    where:

    ` `*`</example/directory>`*` `  
    The mounted PV is available at this path in the workspace.

    `3Gi`  
    Example size value of the requested storage.

    ` `*`<storage_class_name>`*` `  
    The name of the StorageClass required by the claim. Remove this line if you want to use a default StorageClass.

**Related concepts**  

- [Persistent storage for workspaces](develop-con_requesting_persistent_storage_for_workspaces.md "OpenShift Dev Spaces workspaces and workspace data are ephemeral and are lost when the workspace stops.")
