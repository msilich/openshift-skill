> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/configure-assembly_configuring_fuse_overlayfs). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Configure fuse-overlayfs

Configure fuse-overlayfs for building container images within OpenShift Dev Spaces workspaces. For related container build procedures, see Additional resources.

- **[When to enable fuse-overlayfs](configure-con_configuring_fuse_overlayfs.md)**  
  Use the fuse-overlayfs storage driver for Podman and Buildah in the Universal Developer Image (UDI) instead of the default `vfs` driver, which does not provide copy-on-write support.
- **[Enable /dev/fuse access on OpenShift 4.14 and earlier](configure-proc_enabling_access_to_dev_fuse_for_openshift.md)**  
  Enable `/dev/fuse` access for workspace containers on OpenShift versions older than 4.15, so that workspaces can use the fuse-overlayfs storage driver for Podman and Buildah.
- **[Enable fuse-overlayfs for all workspaces](configure-proc_enabling_fuse_for_all_workspaces.md)**  
  Enable fuse-overlayfs for all workspaces to use the overlay storage driver.

**Related information**  

- [Build and run containers in workspaces](https://access.redhat.com/documentation/en-us/red_hat_openshift_dev_spaces/3.29/html-single/develop/index#assembly_building-and-running-containers_develop)
