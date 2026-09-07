> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/develop-proc_enabling_overlay_with_a_configmap). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Enable fuse-overlayfs with a ConfigMap

Enable fuse-overlayfs as the storage driver for Podman and Buildah by mounting a `storage.conf` ConfigMap into all workspaces in your project.

## Before you begin

- For OpenShift versions older than 4.15, the administrator has enabled access to `/dev/fuse`. See [Configuring fuse-overlayfs](configure-assembly_configuring_fuse_overlayfs.md).

- You have a workspace with the required annotations as described in [Access /dev/fuse in workspace containers](develop-proc_accessing_fuse.md "Access /dev/fuse in workspace containers to use fuse-overlayfs as a storage driver for Podman."). Note

  ConfigMaps mounted by following [this guide](develop-proc_mounting_configmaps.md "Mount Kubernetes ConfigMaps into workspace containers to provide non-sensitive configuration data.") apply to all workspaces and set the storage driver to fuse-overlayfs globally. Verify that your workspaces contain the required annotations to use fuse-overlayfs as described in [Access /dev/fuse in workspace containers](develop-proc_accessing_fuse.md "Access /dev/fuse in workspace containers to use fuse-overlayfs as a storage driver for Podman.").

## About this task

Here are the default contents of the `/home/user/.config/containers/storage.conf` file in the UDI container:

``` plaintext
# storage.conf
[storage]
driver = "vfs"
```

To use fuse-overlayfs, `storage.conf` can be set to the following:

``` plaintext
# storage.conf
[storage]
driver = "overlay"

[storage.options.overlay]
mount_program="/usr/bin/fuse-overlayfs"
```

where:

`mount_program`  
The absolute path to the `fuse-overlayfs` binary. The `/usr/bin/fuse-overlayfs` path is the default for the UDI.

You can do this manually after starting a workspace. Another option is to build a new image based on the UDI with changes to `storage.conf` and use the new image for workspaces.

Otherwise, you can update the `/home/user/.config/containers/storage.conf` for all workspaces in your project by creating a ConfigMap that mounts the updated file. See [Mount ConfigMaps](develop-proc_mounting_configmaps.md "Mount Kubernetes ConfigMaps into workspace containers to provide non-sensitive configuration data.").

## Procedure

1.  Create a ConfigMap that mounts a `/home/user/.config/containers/storage.conf` file:

    ``` yaml
    kind: ConfigMap
    apiVersion: v1
    metadata:
      name: fuse-overlay
      labels:
        controller.devfile.io/mount-to-devworkspace: 'true'
        controller.devfile.io/watch-configmap: 'true'
      annotations:
        controller.devfile.io/mount-as: subpath
        controller.devfile.io/mount-path: /home/user/.config/containers
    data:
      storage.conf: |
        [storage]
        driver = "overlay"

        [storage.options.overlay]
        mount_program = "/usr/bin/fuse-overlayfs"
    ```

2.  Apply the ConfigMap to your project: Warning

    Applying this ConfigMap causes all running workspaces in the project to restart.

    ``` bash
    $ oc apply -f fuse-overlay.yaml -n <your_namespace>
    ```

3.  Start or restart your workspace.

## Results

- Verify that the storage driver is `overlay`:

  ``` bash
  $ podman info | grep overlay
  ```

  Example output:

  ``` shell-session
  graphDriverName: overlay
    overlay.mount_program:
      Executable: /usr/bin/fuse-overlayfs
      Package: fuse-overlayfs-1.12-1.module+el8.9.0+20326+387084d0.x86_64
        fuse-overlayfs: version 1.12
    Backing Filesystem: overlayfs
  ```

Note

The following error might occur for existing workspaces:

`ERRO[0000] User-selected graph driver "overlay" overwritten by graph driver "vfs" from database - delete libpod local files ("/home/user/.local/share/containers/storage") to resolve. May prevent use of images created by other tools`

In this case, delete the libpod local files shown in the error message.

**Related concepts**  

- [How fuse-overlayfs works in Cloud Development Environments](develop-con_using_the_fuse_overlay_storage_driver.md "By default, newly created workspaces that do not specify a devfile use the Universal Developer Image (UDI). The UDI contains common development tools and dependencies commonly used by developers.")
- [How kubedock works](develop-con_running_containers_with_kubedock.md "Kubedock is a minimal container engine implementation that gives you a Podman-/docker-like experience inside an OpenShift Dev Spaces workspace.")

**Related tasks**  

- [Access /dev/fuse in workspace containers](develop-proc_accessing_fuse.md "Access /dev/fuse in workspace containers to use fuse-overlayfs as a storage driver for Podman.")
