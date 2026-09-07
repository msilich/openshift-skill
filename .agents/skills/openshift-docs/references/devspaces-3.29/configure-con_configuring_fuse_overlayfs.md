> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/configure-con_configuring_fuse_overlayfs). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# When to enable fuse-overlayfs

Use the fuse-overlayfs storage driver for Podman and Buildah in the Universal Developer Image (UDI) instead of the default `vfs` driver, which does not provide copy-on-write support.

This page is for platform administrators who enable fuse-overlayfs cluster-wide, and for developers who want to enable it for individual workspaces.

To enable fuse-overlayfs for workspaces for OpenShift versions older than 4.15, the administrator must first enable `/dev/fuse` access on the cluster.

Note

This is not necessary for OpenShift versions 4.15 and later, since the `/dev/fuse` device is available by default.

After enabling `/dev/fuse` access, fuse-overlayfs can be enabled in two ways:

1.  For all user workspaces within the cluster.
2.  For workspaces belonging to certain users.

For instructions on enabling `/dev/fuse` access and configuring fuse-overlayfs for your workspaces, see Additional resources.

**Related tasks**  

- [Enable /dev/fuse access on OpenShift 4.14 and earlier](configure-proc_enabling_access_to_dev_fuse_for_openshift.md "Enable /dev/fuse access for workspace containers on OpenShift versions older than 4.15, so that workspaces can use the fuse-overlayfs storage driver for Podman and Buildah.")
- [Enable fuse-overlayfs for all workspaces](configure-proc_enabling_fuse_for_all_workspaces.md "Enable fuse-overlayfs for all workspaces to use the overlay storage driver.")

**Related information**  

- [OpenShift Container Platform 4.15 Release Notes](https://docs.openshift.com/container-platform/4.15/release_notes/ocp-4-15-release-notes.html#ocp-4-15-nodes-dev-fuse)
- [Using the fuse-overlayfs storage driver](https://access.redhat.com/documentation/en-us/red_hat_openshift_dev_spaces/3.29/html-single/develop/index#using-the-fuse-overlay-storage-driver_develop)
