> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/configure-proc_enabling_fuse_for_all_workspaces). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Enable fuse-overlayfs for all workspaces

Enable fuse-overlayfs for all workspaces to use the overlay storage driver.

## Before you begin

- You have completed the [Enable /dev/fuse access on OpenShift 4.14 and earlier](configure-proc_enabling_access_to_dev_fuse_for_openshift.md "Enable /dev/fuse access for workspace containers on OpenShift versions older than 4.15, so that workspaces can use the fuse-overlayfs storage driver for Podman and Buildah.") section. This is not required for OpenShift versions 4.15 and later.
- You have an active `oc` session with administrative permissions to the OpenShift cluster. See [Getting started with the CLI](https://docs.openshift.com/container-platform/4.22/cli_reference/openshift_cli/getting-started-cli.html).

## Procedure

Set the necessary annotation in the `spec.devEnvironments.workspacesPodAnnotations` field of the `CheCluster` Custom Resource.

``` yaml
kind: CheCluster
apiVersion: org.eclipse.che/v2
spec:
  devEnvironments:
    workspacesPodAnnotations:
      io.kubernetes.cri-o.Devices: /dev/fuse
```

Note

For OpenShift versions before 4.15, the `io.openshift.podman-fuse: ""` annotation is also required.

Note

The Universal Development Image (UDI) includes the following logic in the entrypoint script to detect fuse-overlayfs and set the storage driver. If you use a custom image, add equivalent logic to the image’s entrypoint.

``` bash
if [ ! -d "${HOME}/.config/containers" ]; then
  mkdir -p ${HOME}/.config/containers
  if [ -c "/dev/fuse" ] && [ -f "/usr/bin/fuse-overlayfs" ]; then
    (echo '[storage]';echo 'driver = "overlay"';echo '[storage.options.overlay]';echo 'mount_program = "/usr/bin/fuse-overlayfs"') > ${HOME}/.config/containers/storage.conf
  else
    (echo '[storage]';echo 'driver = "vfs"') > "${HOME}"/.config/containers/storage.conf
  fi
fi
```

## Results

1.  Start a workspace and verify that the storage driver is `overlay`.

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

    ``` plaintext
    ERRO[0000] User-selected graph driver "overlay" overwritten by graph driver "vfs" from database - delete libpod local files ("/home/user/.local/share/containers/storage") to resolve.  May prevent use of images created by other tools
    ```

    In this case, delete the libpod local files shown in the error message.

**Related concepts**  

- [When to enable fuse-overlayfs](configure-con_configuring_fuse_overlayfs.md "Use the fuse-overlayfs storage driver for Podman and Buildah in the Universal Developer Image (UDI) instead of the default vfs driver, which does not provide copy-on-write support.")

**Related tasks**  

- [Enable /dev/fuse access on OpenShift 4.14 and earlier](configure-proc_enabling_access_to_dev_fuse_for_openshift.md "Enable /dev/fuse access for workspace containers on OpenShift versions older than 4.15, so that workspaces can use the fuse-overlayfs storage driver for Podman and Buildah.")
