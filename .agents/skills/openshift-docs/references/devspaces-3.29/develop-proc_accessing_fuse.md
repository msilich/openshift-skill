> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/develop-proc_accessing_fuse). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Access /dev/fuse in workspace containers

Access `/dev/fuse` in workspace containers to use fuse-overlayfs as a storage driver for Podman.

## Before you begin

- For OpenShift versions older than 4.15: you have administrator-enabled access to `/dev/fuse`. See [Configuring fuse-overlayfs](configure-assembly_configuring_fuse_overlayfs.md).
- You have identified a workspace to use with fuse-overlayfs.

## Procedure

Use the `pod-overrides` attribute to add the required annotations defined in [Configuring fuse-overlayfs](configure-assembly_configuring_fuse_overlayfs.md) to the workspace. The `pod-overrides` attribute allows merging certain fields in the workspace pod’s `spec`.

**For OpenShift versions older than 4.15:**

``` bash
$ oc patch devworkspace <DevWorkspace_name> \
  --patch '{"spec":{"template":{"attributes":{"pod-overrides":{"metadata":{"annotations":{"io.kubernetes.cri-o.Devices":"/dev/fuse","io.openshift.podman-fuse":""}}}}}}}' \
  --type=merge
```

**For OpenShift version 4.15 and later:**

``` bash
$ oc patch devworkspace <DevWorkspace_name> \
  --patch '{"spec":{"template":{"attributes":{"pod-overrides":{"metadata":{"annotations":{"io.kubernetes.cri-o.Devices":"/dev/fuse"}}}}}}}' \
  --type=merge
```

## Results

1.  Start the workspace and verify that `/dev/fuse` is available in the workspace container:

    ``` bash
    $ stat /dev/fuse
    ```

## What to do next

- [Enable fuse-overlayfs with a ConfigMap](develop-proc_enabling_overlay_with_a_configmap.md "Enable fuse-overlayfs as the storage driver for Podman and Buildah by mounting a storage.conf ConfigMap into all workspaces in your project.")

**Related concepts**  

- [How fuse-overlayfs works in Cloud Development Environments](develop-con_using_the_fuse_overlay_storage_driver.md "By default, newly created workspaces that do not specify a devfile use the Universal Developer Image (UDI). The UDI contains common development tools and dependencies commonly used by developers.")
- [How kubedock works](develop-con_running_containers_with_kubedock.md "Kubedock is a minimal container engine implementation that gives you a Podman-/docker-like experience inside an OpenShift Dev Spaces workspace.")

**Related tasks**  

- [Enable fuse-overlayfs with a ConfigMap](develop-proc_enabling_overlay_with_a_configmap.md "Enable fuse-overlayfs as the storage driver for Podman and Buildah by mounting a storage.conf ConfigMap into all workspaces in your project.")
