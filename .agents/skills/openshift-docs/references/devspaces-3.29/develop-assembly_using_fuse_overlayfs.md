> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/develop-assembly_using_fuse_overlayfs). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Build and run containers in workspaces

Build and run container images in OpenShift Dev Spaces workspaces using fuse-overlayfs for Podman and Buildah, and kubedock for Testcontainers and similar frameworks.

- **[How fuse-overlayfs works in Cloud Development Environments](develop-con_using_the_fuse_overlay_storage_driver.md)**  
  By default, newly created workspaces that do not specify a devfile use the Universal Developer Image (UDI). The UDI contains common development tools and dependencies commonly used by developers.
- **[Access /dev/fuse in workspace containers](develop-proc_accessing_fuse.md)**  
  Access `/dev/fuse` in workspace containers to use fuse-overlayfs as a storage driver for Podman.
- **[Enable fuse-overlayfs with a ConfigMap](develop-proc_enabling_overlay_with_a_configmap.md)**  
  Enable fuse-overlayfs as the storage driver for Podman and Buildah by mounting a `storage.conf` ConfigMap into all workspaces in your project.
- **[How kubedock works](develop-con_running_containers_with_kubedock.md)**  
  Kubedock is a minimal container engine implementation that gives you a Podman-/docker-like experience inside an OpenShift Dev Spaces workspace.
- **[Enable kubedock in a workspace](develop-proc_enabling_kubedock.md)**  
  Enable kubedock in an OpenShift Dev Spaces workspace by adding environment variables to the devfile.
- **[Use Kubedock in a workspace](develop-proc_using_kubedock_in_workspace.md)**  
  Use Kubedock to run containers in your workspace when Docker-in-Docker or privileged containers are not available.
