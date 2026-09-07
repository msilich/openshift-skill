> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/develop-con_using_the_fuse_overlay_storage_driver). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# How fuse-overlayfs works in Cloud Development Environments

By default, newly created workspaces that do not specify a devfile use the Universal Developer Image (UDI). The UDI contains common development tools and dependencies commonly used by developers.

Podman and Buildah are included in the UDI, allowing developers to build and push container images from their workspace.

By default, Podman and Buildah in the UDI are configured to use the `vfs` storage driver. For more efficient image management, use the fuse-overlayfs storage driver which supports copy-on-write in rootless environments.

You must meet the following requirements to use fuse-overlayfs in a workspace:

- For OpenShift versions older than 4.15, the administrator has enabled `/dev/fuse` access on the cluster.
- The workspace has the necessary annotations for using the `/dev/fuse` device.
- The `storage.conf` file in the workspace container is configured to use fuse-overlayfs.

For instructions on meeting each requirement, see Additional resources.

**Related tasks**  

- [Accessing /dev/fuse](develop-proc_accessing_fuse.md "Access /dev/fuse in workspace containers to use fuse-overlayfs as a storage driver for Podman.")
- [Enabling the overlay storage driver with a ConfigMap](develop-proc_enabling_overlay_with_a_configmap.md "Enable fuse-overlayfs as the storage driver for Podman and Buildah by mounting a storage.conf ConfigMap into all workspaces in your project.")

**Related information**  

- [Configuring fuse-overlayfs](configure-assembly_configuring_fuse_overlayfs.md)
- [Universal Developer Image](https://github.com/devfile/developer-images)
