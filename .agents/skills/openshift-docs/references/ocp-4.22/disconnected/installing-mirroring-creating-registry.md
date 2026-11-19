<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

The *mirror registry for Red Hat OpenShift* 3.0 is a streamlined container registry that you can use as a target for mirroring the required container images of OpenShift Container Platform for disconnected installations.

> [!IMPORTANT]
> Mirror registry for Red Hat OpenShift 3.0 is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.
>
> For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

> [!IMPORTANT]
> The *mirror registry for Red Hat OpenShift* is not intended to be a substitute for a production deployment of Red Hat Quay.

If you already have a container image registry, such as Red Hat Quay, you can skip this section and go straight to "Mirroring the OpenShift Container Platform image repository".

# Mirror registry for Red Hat OpenShift introduction

For disconnected deployments of OpenShift Container Platform, a container registry is required to carry out the installation of the clusters.

To run a production-grade registry service on such a cluster, you must create a separate registry deployment to install the first cluster. The *mirror registry for Red Hat OpenShift* addresses this need and is included in every OpenShift Container Platform subscription. It is available for download on the "OpenShift console Downloads" page.

The *mirror registry for Red Hat OpenShift* 3.0 is a single Go binary (`mirror-registry`) that installs and manages a lightweight OCI container registry on the local host. It handles initialization, TLS certificate generation, systemd service management, and image serving through a single command, with no external dependencies beyond Podman. The registry runs as a Podman container managed by systemd using a Quadlet `.container` unit file.

The `mirror-registry install` command is the one-command setup. It handles everything from database and admin user initialization to TLS certificate generation, container image loading, and systemd service creation in a single step. All access credentials and the registry URL are printed at the end of the install routine.

Use of the *mirror registry for Red Hat OpenShift* is optional if another container registry is already available in the install environment.

## Mirror registry for Red Hat OpenShift limitations

The following limitations apply to the *mirror registry for Red Hat OpenShift*:

- The *mirror registry for Red Hat OpenShift* is not a highly-available registry and only local file system storage is supported. It is not intended to replace Red Hat Quay or the internal image registry for OpenShift Container Platform.

- The *mirror registry for Red Hat OpenShift* is not intended to be a substitute for a production deployment of Red Hat Quay.

- The *mirror registry for Red Hat OpenShift* is only supported for hosting images that are required to install a disconnected OpenShift Container Platform cluster, such as release images or Red Hat Operator images. It uses local storage on your Red Hat Enterprise Linux (RHEL) machine, and storage supported by RHEL is supported by the *mirror registry for Red Hat OpenShift*.

  > [!NOTE]
  > Because the *mirror registry for Red Hat OpenShift* uses local storage, you should remain aware of the storage usage consumed when mirroring images. The registry includes a built-in garbage collector that runs automatically every 30 seconds inside the registry container. Deleted tags are permanently removed after a 14-day grace period. No user action is required for garbage collection.
  >
  > To manually delete images, use standard OCI registry tools:
  >
  > - `skopeo delete docker://<host>:<port>/<repository>/<image>:<tag>` to delete a specific manifest or tag.
  >
  > - `oc-mirror delete` for bulk cleanup of mirrored OpenShift Container Platform content.

- The *mirror registry for Red Hat OpenShift* has no web UI or Red Hat Quay console. All registry management is performed through the CLI or the registry API.

- The *mirror registry for Red Hat OpenShift* installs only on the local host. Remote host installation is not supported.

- Support for Red Hat product images that are pushed to the *mirror registry for Red Hat OpenShift* for bootstrapping purposes are covered by valid subscriptions for each respective product. For a list of exceptions to further enable the bootstrap experience, see "Self-managed Red Hat OpenShift sizing and subscription guide".

- Content built by customers should not be hosted by the *mirror registry for Red Hat OpenShift*.

- Using the *mirror registry for Red Hat OpenShift* with more than one cluster is discouraged because multiple clusters can create a single point of failure when updating your cluster fleet. Instead, use the *mirror registry for Red Hat OpenShift* to install a cluster that can host a production-grade, highly-available registry such as Red Hat Quay, which can serve OpenShift Container Platform content to other clusters.

<div>

<div class="title">

Additional resources

</div>

- [Creating a mirror registry with mirror registry for Red Hat OpenShift](https://docs.redhat.com/en/documentation/openshift_container_platform/4.21/html-single/disconnected_environments/index#installing-mirroring-creating-registry)

- [OpenShift console Downloads](https://console.redhat.com/openshift/downloads#tool-mirror-registry)

- [Self-managed Red Hat OpenShift sizing and subscription guide](https://www.redhat.com/en/resources/self-managed-openshift-sizing-subscription-guide)

</div>

# Configure rootless Podman networking

To restore rootless Podman networking when the default `pasta` stack fails on OpenShift Container Platform mirror or install hosts, you can set the default rootless network back to `slirp4netns` in the `/etc/containers/containers.conf` file, or in the user’s `~/.config/containers/container.conf` file.

You might need to configure rootless Podman networking after upgrading to RHEL 9.5 or Podman 5.0. In these versions, the default networking stack changed from `slirp4netns` to `pasta`. As a result, systems that previously operated without a default route might no longer be able to establish network connectivity and could display the following error:

``` terminal
Error: pasta failed with exit code 1:
External interface not usable
```

<div>

<div class="title">

Prerequisites

</div>

- You have updated to RHEL 9.5 or Podman 5.0.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Use your preferred IDE to modify the `/etc/containers/containers.conf` or `~/.config/containers/container.conf` file.

    1.  To modify the `/etc/containers/containers.conf` file, enter the following command:

        ``` terminal
        $ nano /etc/containers/containers.conf
        ```

    2.  To modify the `~/.config/containers/container.conf` file, enter the following command:

        ``` terminal
        $ nano ~/.config/containers/container.conf
        ```

2.  Add, or update, the `[network]` section as in the following example:

    ``` text
    # ...
    [network]
    default_rootless_network_cmd = "slirp4netns"
    # ...
    ```

3.  Restart the Podman system as the rootless user by entering the following command. Note that all containers must be stopped and restarted for the change to take effect.

    ``` terminal
    $ podman system migrate
    ```

</div>

# Installing mirror registry for Red Hat OpenShift

You can install the *mirror registry for Red Hat OpenShift* on a local host by using the `mirror-registry install` command. This creates a registry running on port 8443 for the purpose of storing a mirror of OpenShift Container Platform images.

> [!NOTE]
> The `mirror-registry install` command is for new installations only. If a registry is already installed on the host, use `mirror-registry upgrade` to update it or `mirror-registry uninstall` to remove it.

After installation, a systemd service (`quay.service`) is created and started. The registry runs as a Podman container managed by a systemd Quadlet unit file. All access credentials and the registry URL are printed at the end of the install routine.

<div>

<div class="title">

Prerequisites

</div>

- An OpenShift Container Platform subscription.

- Red Hat Enterprise Linux (RHEL) 9 or later.

- Podman 4.4 or later.

- A fully qualified domain name (FQDN) or IP address for the registry host. When using auto-detection, the hostname must be a FQDN. If you pass a hostname explicitly with `-hostname`, an IP address is also supported. The hostname or IP address must resolve by DNS or be present in `/etc/hosts` on each client machine that will access the registry.

- About 50 GB or more of available disk space for mirrored OpenShift Container Platform images, depending on the number of releases you mirror.

  > [!NOTE]
  > Up to 1 TB per stream or more is suggested. Storage requirements can vary based on your organization’s needs. To remove unnecessary images and free up space, use `skopeo delete` to delete individual tags or `oc-mirror delete` for bulk cleanup of mirrored OpenShift Container Platform content. The registry reclaims space automatically through its built-in garbage collector.

- A valid OpenShift Container Platform pull secret from [console.redhat.com](https://console.redhat.com/openshift/install/pull-secret).

</div>

<div>

<div class="title">

Procedure

</div>

1.  Download the `mirror-registry` bundle for the latest version of the *mirror registry for Red Hat OpenShift* found on the [OpenShift console **Downloads**](https://console.redhat.com/openshift/downloads#tool-mirror-registry) page.

2.  Extract the bundle and make the binary executable by running the following commands:

    ``` terminal
    $ tar -xzf mirror-registry-amd64.tar.gz
    ```

    ``` terminal
    $ chmod +x mirror-registry
    ```

3.  Install the *mirror registry for Red Hat OpenShift* on your local host by using the `mirror-registry` tool. For a full list of available flags, see "Mirror registry for Red Hat OpenShift flags".

    - For an air-gapped environment, specify the path to the included container image archive:

      ``` terminal
      $ ./mirror-registry install \
        -data-dir /var/lib/quay \
        -image-archive image-archive.tar
      ```

    - For a non-root installation, use a user-writable path for the data directory.

      - Non-root installations require cgroups v2. RHEL 9 uses cgroups v2 by default. Verify that cgroups v2 is enabled by running the following command:

        ``` terminal
        $ podman info --format '{{.Host.CgroupsVersion}}'
        ```

      - Install the registry as a non-root user by running the following command:

        ``` terminal
        $ ./mirror-registry install \
          -data-dir ~/quay-data \
          -image-archive image-archive.tar
        ```

      - Optional: The installation program automatically detects the system hostname. To specify a hostname, pass the `-hostname` flag by entering the following command:

        ``` terminal
        $ ./mirror-registry install \
          -data-dir <data_dir> \
          -hostname <host_example_com> \
          -image-archive image-archive.tar
        ```

4.  Use the username and password generated during installation to log in to the registry by running the following command:

    ``` terminal
    $ podman login -u admin \
      -p $(cat <data_dir>/auth/admin-password) \
      <host_example_com>:8443 \
      --tls-verify=false
    ```

    - Substitute `<data_dir>` with the data directory you specified during installation.

      You can avoid running `--tls-verify=false` by adding `/ssl.cert` to your system’s trusted certificate store. For example:

      ``` terminal
      $ sudo cp <data_dir>/ssl.cert /etc/pki/ca-trust/source/anchors/ && sudo update-ca-trust
      ```

5.  Mirror OpenShift Container Platform images after logging in. Depending on your needs, see either the "Mirroring the OpenShift Container Platform image repository" or the "Mirroring Operator catalogs for use with disconnected clusters" sections of this document.

    > [!NOTE]
    > If there are issues with images stored by the *mirror registry for Red Hat OpenShift* due to storage layer problems, you can re-mirror the OpenShift Container Platform images, or reinstall the mirror registry on more stable storage.

</div>

## Data directory layout for mirror registry for Red Hat OpenShift

After installation, the *mirror registry for Red Hat OpenShift* stores all data under a single configurable data directory. The following describes the contents of the data directory.

``` text
<data_dir>/
├── quay.db
├── auth/
│   └── admin-password
├── ssl.cert
├── ssl.key
├── registry-jwt.pem
└── storage/
    ├── sha256/
    └── uploads/
```

`<data_dir>/quay.db`
The SQLite database containing users, repositories, and manifests.

`<data_dir>/auth/admin-password`
The admin credentials file. This file has mode 0600 and can only be read by the user who ran `mirror-registry install`.

`<data_dir>/ssl.cert`
The TLS certificate used for HTTPS.

`<data_dir>/ssl.key`
The TLS private key used for HTTPS.

`<data_dir>/registry-jwt.pem`
The JWT signing key used for registry authentication tokens.

`<data_dir>/storage/`
The image blob storage directory containing content-addressable blobs and in-progress uploads.

# Upgrading mirror registry for Red Hat OpenShift

You can upgrade the *mirror registry for Red Hat OpenShift* by using the `mirror-registry upgrade` command. Use this command for z-stream updates only, for example, from 3.0.0 to 3.0.1. The `upgrade` command replaces the container image of the installed registry in place and preserves all existing data, credentials, certificates, hostname, and port.

> [!IMPORTANT]
> Use `mirror-registry upgrade` only for *mirror registry for Red Hat OpenShift* 3.0 z-stream updates. To migrate from *mirror registry for Red Hat OpenShift* 2.0.x to 3.0, use `mirror-registry migrate` instead.

The upgrade preserves the following:

- All registry data, including the database, images, and blob storage

- Credentials, including the admin password and JWT signing keys

- TLS certificates

- Hostname and port

<div>

<div class="title">

Prerequisites

</div>

- You have installed the *mirror registry for Red Hat OpenShift* 3.0 on the local host.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Download the `mirror-registry` bundle for the latest version of the *mirror registry for Red Hat OpenShift* from the [OpenShift console **Downloads**](https://console.redhat.com/openshift/downloads#tool-mirror-registry) page.

2.  Extract the bundle and make the binary executable by running the following commands:

    ``` terminal
    $ tar -xzf mirror-registry-amd64.tar.gz
    ```

    ``` terminal
    $ chmod +x mirror-registry
    ```

3.  Upgrade the *mirror registry for Red Hat OpenShift* by running the `mirror-registry upgrade` command from the new binary:

    - For a connected environment, run `upgrade` without `-image-archive`. The new binary pulls its matching container image from the registry automatically:

      ``` terminal
      $ ./mirror-registry upgrade
      ```

    - For an air-gapped environment, download the full bundle and pass the `-image-archive` flag:

      ``` terminal
      $ ./mirror-registry upgrade -image-archive image-archive.tar
      ```

      > [!NOTE]
      > The hostname, port, and data directory are detected from the existing installation and do not need to be specified.

    - Optional: To replace TLS certificates during upgrade, pass both the `-ssl-cert` and `-ssl-key` flags together:

      ``` terminal
      $ ./mirror-registry upgrade \
        -image-archive image-archive.tar \
        -ssl-cert /path/to/new-cert.pem \
        -ssl-key /path/to/new-key.pem
      ```

</div>

<div>

<div class="title">

Verification

</div>

1.  Verify that the *mirror registry for Red Hat OpenShift* is running with the updated image by entering the following command:

    ``` terminal
    $ systemctl status quay.service
    ```

    For a non-root installation, use:

    ``` terminal
    $ systemctl --user status quay.service
    ```

</div>

# Migrating from mirror registry for Red Hat OpenShift 2.0.x (SQLite)

If you are running *mirror registry for Red Hat OpenShift* 2.0.x with the default SQLite backend, you can migrate to 3.0 by using the `mirror-registry migrate` command. The command auto-detects the existing installation, copies all data to the new data directory, upgrades the database schema, and installs the new registry.

> [!IMPORTANT]
> Use `mirror-registry migrate` only to migrate from a 2.0.x installation to 3.0. For 3.0 z-stream updates, use `mirror-registry upgrade` instead. The `migrate` command exits with an error if a 3.0 installation already exists on the host.

> [!NOTE]
> Do not run `mirror-registry migrate` and `mirror-registry install` separately. The `migrate` command calls `install` internally after copying data.

<div>

<div class="title">

Prerequisites

</div>

- The 2.0.x registry is running and healthy before migration.

- You can pull images from the old registry.

- Sufficient free disk space is available for the new data directory. The migration copies data rather than moving it.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Download the new `mirror-registry` bundle for the latest version of the *mirror registry for Red Hat OpenShift* from the [OpenShift console **Downloads**](https://console.redhat.com/openshift/downloads#tool-mirror-registry) page.

2.  Extract the bundle and make the binary executable by running the following commands:

    ``` terminal
    $ tar -xzf mirror-registry-amd64.tar.gz
    ```

    ``` terminal
    $ chmod +x mirror-registry
    ```

3.  Run the migration by entering the following command. The `mirror-registry migrate` command auto-detects your 2.0.x installation by probing systemd units, Podman volumes, and the default `~/quay-install/` path:

    ``` terminal
    $ ./mirror-registry migrate -image-archive image-archive.tar
    ```

    If auto-detection fails, or if you installed 2.0.x in a non-default location, specify the source root explicitly:

    ``` terminal
    $ ./mirror-registry migrate \
      -source-root ~/quay-install \
      -data-dir /var/lib/quay \
      -image-archive image-archive.tar
    ```

    Alternatively, specify individual paths:

    ``` terminal
    $ ./mirror-registry migrate \
      -source-db ~/quay-install/sqlite-storage/quay_sqlite.db \
      -source-storage ~/quay-install/quay-storage \
      -source-certs ~/quay-install/quay-config \
      -data-dir /var/lib/quay \
      -hostname <host_example_com> \
      -image-archive image-archive.tar
    ```

4.  Optional: Preview the migration plan without making any changes by running the following command:

    ``` terminal
    $ ./mirror-registry migrate -source-root ~/quay-install -dry-run
    ```

    The output shows the detected source paths, hostname, and target directory.

</div>

<div>

<div class="title">

Verification

</div>

1.  Log in to the new registry by entering the following command:

    ``` terminal
    $ podman login -u admin \
      -p $(cat /var/lib/quay/auth/admin-password) \
      --tls-verify=false \
      <host_example_com>:8443
    ```

2.  Pull an image that existed before migration to verify the data was copied successfully:

    ``` terminal
    $ podman pull <host_example_com>:8443/<repository>/<image>:<tag> --tls-verify=false
    ```

3.  Push a new test image to verify write access:

    ``` terminal
    $ podman tag docker.io/library/alpine:latest <host_example_com>:8443/admin/alpine:test
    ```

    ``` terminal
    $ podman push <host_example_com>:8443/admin/alpine:test --tls-verify=false
    ```

4.  After verifying the migration, remove the old 2.0.x services and Podman volumes by running the following command:

    ``` terminal
    $ ./mirror-registry migrate -source-root ~/quay-install -cleanup
    ```

    > [!NOTE]
    > The `~/quay-install` directory itself is preserved after cleanup because it may contain the `quay-rootCA/` directory that clients trust.

</div>

# Migrating from mirror registry for Red Hat OpenShift 2.0.x (PostgreSQL)

If your *mirror registry for Red Hat OpenShift* 2.0.x installation uses PostgreSQL, you can migrate to 3.0 by using the `mirror-registry migrate` command.

The PostgreSQL migration path converts the PostgreSQL data to SQLite and installs the new registry. The `mirror-registry migrate` command handles the database connection automatically by re-executing itself inside the PostgreSQL container’s network namespace using `nsenter`.

<div class="important">

<div class="title">

</div>

- The PostgreSQL migration path does not support the `-dry-run`, `-cleanup`, or `-skip-install` flags. These flags are available for SQLite source migrations only.

- The target directory must be clean, that is, empty or non-existent. The PostgreSQL migration does not support resuming a previous attempt. If a previous attempt left partial data, remove the target directory before retrying.

</div>

If the PostgreSQL migration fails at any point, the following actions are taken automatically:

- Intermediate migration artifacts (`quay.db.partial`) are removed.

- Any partially created 3.0 Quadlet installation is removed.

- The old 2.0.x services (`quay-pod`, `quay-postgres`, `quay-redis`, `quay-app`) are restarted.

A failed PostgreSQL migration is safe to retry after addressing the root cause and providing a clean target directory.

<div>

<div class="title">

Prerequisites

</div>

- The 2.0.x `quay-postgres` container and `quay-pod` must be running. The migration connects to PostgreSQL through the pod’s network namespace.

- The old `quay-app` service must be stoppable.

- No existing 3.0 Quadlet installation may be present. Uninstall it first if needed.

- Sufficient free disk space is available for the new data directory. The migration copies data rather than moving it.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Download the new `mirror-registry` bundle for the latest version of the *mirror registry for Red Hat OpenShift* from the [OpenShift console **Downloads**](https://console.redhat.com/openshift/downloads#tool-mirror-registry) page.

2.  Extract the bundle and make the binary executable by running the following commands:

    ``` terminal
    $ tar -xzf mirror-registry-amd64.tar.gz
    ```

    ``` terminal
    $ chmod +x mirror-registry
    ```

3.  Run the migration, specifying your 2.0.x installation directory and the target data directory:

    ``` terminal
    $ ./mirror-registry migrate \
      -source-root ~/quay-install \
      -data-dir /var/lib/quay \
      -image-archive image-archive.tar
    ```

    The `-source-root` flag points to the 2.0.x installation directory (typically `~/quay-install`). The migration reads `quay-config/config.yaml` within it to determine the database type and connection details.

</div>

<div>

<div class="title">

Verification

</div>

1.  Log in to the new registry by entering the following command:

    ``` terminal
    $ podman login -u admin \
      -p $(cat /var/lib/quay/auth/admin-password) \
      --tls-verify=false \
      <host_example_com>:8443
    ```

2.  Pull an image that existed before migration to verify the data was copied successfully:

    ``` terminal
    $ podman pull <host_example_com>:8443/<repository>/<image>:<tag> --tls-verify=false
    ```

3.  Push a new test image to verify write access by running the following commands:

    ``` terminal
    $ podman tag docker.io/library/alpine:latest <host_example_com>:8443/admin/alpine:test
    ```

    ``` terminal
    $ podman push <host_example_com>:8443/admin/alpine:test --tls-verify=false
    ```

</div>

# Replacing mirror registry for Red Hat OpenShift SSL/TLS certificates

In some cases, you might want to update your SSL/TLS certificates for the *mirror registry for Red Hat OpenShift*. You can replace certificates at installation time or during an upgrade by passing the `-ssl-cert` and `-ssl-key` flags.

<div>

<div class="title">

Prerequisites

</div>

- You have downloaded the `mirror-registry` binary from the [OpenShift console **Downloads**](https://console.redhat.com/openshift/downloads#tool-mirror-registry) page.

- You have a valid TLS certificate (PEM format) and its corresponding private key.

</div>

<div>

<div class="title">

Procedure

</div>

- To use custom TLS certificates at installation time, pass the `-ssl-cert` and `-ssl-key` flags to the `mirror-registry install` command:

  ``` terminal
  $ ./mirror-registry install \
    -data-dir /var/lib/quay \
    -image-archive image-archive.tar \
    -ssl-cert /path/to/cert.pem \
    -ssl-key /path/to/key.pem
  ```

- To replace TLS certificates on an existing installation, pass the `-ssl-cert` and `-ssl-key` flags to the `mirror-registry upgrade` command:

  ``` terminal
  $ ./mirror-registry upgrade \
    -image-archive image-archive.tar \
    -ssl-cert /path/to/new-cert.pem \
    -ssl-key /path/to/new-key.pem
  ```

  > [!NOTE]
  > You must provide `-ssl-cert` and `-ssl-key` together. Passing only one of these flags causes the command to fail.

  If the certificate hostname does not match the registry hostname, for example when using a wildcard or internal CA certificate, add the `-ssl-skip-hostname-verification` flag:

  ``` terminal
  $ ./mirror-registry upgrade \
    -image-archive image-archive.tar \
    -ssl-cert /path/to/cert.pem \
    -ssl-key /path/to/key.pem \
    -ssl-skip-hostname-verification
  ```

</div>

# Uninstalling the mirror registry for Red Hat OpenShift

You can uninstall the *mirror registry for Red Hat OpenShift* from your local host.

<div>

<div class="title">

Prerequisites

</div>

- You have installed the *mirror registry for Red Hat OpenShift* on the local host.

</div>

<div>

<div class="title">

Procedure

</div>

- Uninstall the *mirror registry for Red Hat OpenShift* from your local host by running the following command:

  ``` terminal
  $ ./mirror-registry uninstall -data-dir /var/lib/quay
  ```

  You are prompted for confirmation before the registry is removed. To skip the confirmation prompt and also delete the data directory, add the `-auto-approve` flag:

  ``` terminal
  $ ./mirror-registry uninstall -data-dir /var/lib/quay -auto-approve
  ```

  > [!NOTE]
  > You must pass the same `-data-dir` path that was used during installation. The uninstall command stops the `quay.service`, removes the systemd Quadlet unit file, and, when `-auto-approve` is specified, deletes the data directory.

</div>

# Mirror registry for Red Hat OpenShift flags

You can use flags when managing the *mirror registry for Red Hat OpenShift*. Flags are organized by subcommand. Global flags apply to all subcommands.

## Global flags

The following flags are available for all `mirror-registry` subcommands:

| Flag | Default | Description |
|----|----|----|
| `-log-format` | `json` | The log output format. Accepted values are `json` and `text`. |
| `-log-level` | `info` | The log verbosity level. Accepted values are `debug`, `info`, `warn`, and `error`. |

## install flags

The `install` subcommand sets up a new registry. If a registry is already installed on the host, use `mirror-registry upgrade` instead.

| Flag | Default | Description |
|----|----|----|
| `-data-dir` | `/var/lib/quay` | The directory for the database, image storage, TLS certificates, and credentials. All registry data is stored under this path. |
| `-hostname` | Auto-detected FQDN | The server hostname or IP address used for TLS configuration and the registry URL. When auto-detected, the hostname must be a fully qualified domain name (FQDN). IP addresses are supported when passed explicitly with `-hostname`. The hostname or IP address must resolve by DNS or be present in `/etc/hosts` on all clients. |
| `-port` | `8443` | The HTTPS port for the registry. |
| `-image-archive` | *(none)* | The path to the container image tar archive. Required for air-gapped installations. If omitted on a connected host, the image is pulled from the registry automatically. |
| `-init-user` | `admin` | The username of the initial admin user created during installation. |
| `-init-password-stdin` | `false` | When set, reads the admin password from stdin instead of auto-generating one. |
| `-ssl-cert` | *(auto-generated)* | The path to a custom TLS certificate in PEM format. If omitted, a self-signed certificate is generated. |
| `-ssl-key` | *(auto-generated)* | The path to the TLS private key in PEM format. Must be provided together with `-ssl-cert`. |
| `-ssl-skip-hostname-verification` | `false` | Skips the check that the TLS certificate hostname matches `-hostname`. Use when you have a wildcard or internal CA certificate. |

## upgrade flags

The `upgrade` subcommand replaces the container image of an existing installation in place. The hostname, port, and data directory are preserved from the existing installation unless explicitly overridden.

| Flag | Default | Description |
|----|----|----|
| `-image-archive` | *(none)* | The path to the new container image tar archive. Required for air-gapped upgrades. If omitted on a connected host, the image is pulled automatically. |
| `-data-dir` | *(detected from the existing installation)* | Must match the data directory of the installed registry. Passing a path that differs from the installed one is rejected before any changes are made. |
| `-hostname` | *(preserved from the existing installation)* | Overrides the server hostname. Use only when you want to change the hostname. |
| `-port` | *(preserved from the existing installation)* | Overrides the HTTPS port. Use only when you want to change the port. |
| `-ssl-cert` | *(preserved from the existing installation)* | The path to a replacement TLS certificate in PEM format. Must be provided together with `-ssl-key`. |
| `-ssl-key` | *(preserved from the existing installation)* | The path to a replacement TLS private key in PEM format. Must be provided together with `-ssl-cert`. |
| `-ssl-skip-hostname-verification` | `false` | Skips the check that the TLS certificate hostname matches `-hostname`. Use together with `-ssl-cert` and `-ssl-key` when you have a wildcard or internal CA certificate. |

## migrate flags

The `migrate` subcommand is used to migrate a 2.0.x installation to a 3.0.x installation.

| Flag | Default | Description |
|----|----|----|
| `-source-root` | *(auto-detected)* | The path to the old `quay-install` directory from the 2.0.x installation. |
| `-source-db` | *(auto-detected)* | The path to the old `quay_sqlite.db` file. Supported for SQLite source only. Use when auto-detection fails. |
| `-source-storage` | *(auto-detected)* | The path to the old image blob storage directory. Use when auto-detection fails. |
| `-source-certs` | *(auto-detected)* | The path to the old TLS certificate directory (`quay-config/`). Use when auto-detection fails. |
| `-data-dir` | `/var/lib/quay` | The target directory for the new 3.0 installation. |
| `-hostname` | *(auto-detected from the old configuration)* | The server hostname for the new registry. Defaults to the hostname from the old installation. |
| `-image-archive` | *(auto-detected)* | The path to the container image tar archive for the new installation. |
| `-dry-run` | `false` | Shows the migration plan without making any changes. Supported for SQLite source only. |
| `-cleanup` | `false` | Removes the old 2.0.x services, Podman volumes, and the Redis secret after a successful migration. Supported for SQLite source only. |
| `-skip-install` | `false` | Copies data only and does not deploy the Quadlet service. Supported for SQLite source only. |

## uninstall flags

The `uninstall` subcommand is used to uninstall the mirror registry.

| Flag | Default | Description |
|----|----|----|
| `-data-dir` | `/var/lib/quay` | The data directory of the registry to uninstall. Must match the path used during installation. |
| `-auto-approve` | `false` | Skips the confirmation prompt and deletes the data directory along with the registry. |

## config validate flags

The `config validate` subcommand is used to validate the configuration file.

| Flag | Default | Description |
|----|----|----|
| `-config` | *(required)* | The path to the `config.yaml` file or the configuration directory to validate. |
| `-mode` | `offline` | The validation mode. Accepted values are `offline` and `online`. |

# Mirror registry for Red Hat OpenShift release notes

The *mirror registry for Red Hat OpenShift* is a small and streamlined container registry that you can use as a target for mirroring the required container images of OpenShift Container Platform for disconnected installations.

These release notes track the development of the *mirror registry for Red Hat OpenShift* in OpenShift Container Platform.

## Mirror registry for Red Hat OpenShift 3.0 release notes

See the *mirror registry for Red Hat OpenShift* 3.0 release notes for information about updates and changes.

### Mirror registry for Red Hat OpenShift 3.0.0 (Technology Preview)

Issued: TBA September 2026

*Mirror registry for Red Hat OpenShift* 3.0 is now available with Red Hat Quay TBD.

The following advisory is available for the *mirror registry for Red Hat OpenShift*:

- [RHBA-2026:TBA - mirror registry for Red Hat OpenShift 3.0.0](https://access.redhat.com/errata/RHBA-2026:TBA)

The following new features are available with *mirror registry for Red Hat OpenShift* 3.0:

- With this release, the *mirror registry for Red Hat OpenShift* is distributed as a single, self-contained Go binary (`mirror-registry`) that requires no external dependencies beyond Podman. The Ansible-based installation tooling used in version 2.0.x has been removed.

- With this release, the `mirror-registry install` command performs fresh installations only. Running `install` on a host where a registry is already installed exits with an error and points to `mirror-registry upgrade`. This prevents unintended reconfiguration of a running registry.

- A new `mirror-registry upgrade` command has been added. The `upgrade` command replaces the container image of an existing installation in place while preserving the data directory, credentials, TLS certificates, hostname, and port. It exits with an error if no existing installation is found.

- With this release, the registry runs as a Podman container managed by systemd using a Quadlet `.container` unit file (`quay.service`). The separate `quay-app`, `quay-redis`, and `quay-pod` services used in version 2.0.x have been replaced by this single unit.

- With this release, the *mirror registry for Red Hat OpenShift* uses SQLite exclusively as its internal database for new installations. PostgreSQL is supported only as a migration source from version 2.0.x. The `quay-redis` container dependency has been removed.

- A new `mirror-registry migrate` command has been added to migrate existing version 2.0.x installations to version 3.0. Both SQLite and PostgreSQL source databases are supported. The command auto-detects the existing installation and copies all data, certificates, and credentials to the new data directory. For PostgreSQL sources, the migration converts the database to SQLite before deploying the new registry.

- With this release, the *mirror registry for Red Hat OpenShift* installs only on the local host. Remote host installation, which previously required SSH keys and the `--targetHostname` flag, is no longer supported.

- With this release, repositories are created automatically on the first image push. Manual repository creation through the Red Hat Quay web console, which was required in version 2.0.x, is no longer necessary. The web console and Red Hat Quay UI have been removed from the *mirror registry for Red Hat OpenShift*; all management is performed through the CLI or the registry API.

- All registry data, including the SQLite database, TLS certificates, credentials, and image blob storage, is stored under a single configurable data directory (default: `/var/lib/quay`). The separate Podman volumes (`quay-storage`, `sqlite-storage`) used in version 2.0.x are no longer used for new installations.

- Root access is no longer required when uninstalling the *mirror registry for Red Hat OpenShift*.

## Mirror registry for Red Hat OpenShift 2.0 release notes

See the *mirror registry for Red Hat OpenShift* 2.0 release notes for information about updates and changes.

To view the *mirror registry for Red Hat OpenShift* 2.0 release notes, see [Mirror registry for Red Hat OpenShift 2.0 release notes](https://docs.redhat.com/en/documentation/openshift_container_platform/4.21/html/disconnected_environments/installing-mirroring-creating-registry#mirror-registry-release-notes-2-0_installing-mirroring-creating-registry).

## Mirror registry for Red Hat OpenShift 1.3 release notes

See the *mirror registry for Red Hat OpenShift* 1.3 release notes for information about updates and changes.

To view the *mirror registry for Red Hat OpenShift* 1.3 release notes, see [Mirror registry for Red Hat OpenShift 1.3 release notes](https://docs.redhat.com/en/documentation/openshift_container_platform/4.13/html/disconnected_installation_mirroring/installing-mirroring-creating-registry#mirror-registry-release-notes-1-3_installing-mirroring-creating-registry).

## Mirror registry for Red Hat OpenShift 1.2 release notes

See the *mirror registry for Red Hat OpenShift* 1.2 release notes for information about updates and changes.

To view the *mirror registry for Red Hat OpenShift* 1.2 release notes, see [Mirror registry for Red Hat OpenShift 1.2 release notes](https://docs.openshift.com/container-platform/4.13/installing/disconnected_install/installing-mirroring-creating-registry.html#mirror-registry-release-notes-1-2_installing-mirroring-creating-registry).

## Mirror registry for Red Hat OpenShift 1.1 release notes

See the *mirror registry for Red Hat OpenShift* 1.1 release notes for information about updates and changes.

To view the *mirror registry for Red Hat OpenShift* 1.1 release notes, see [Mirror registry for Red Hat OpenShift 1.1 release notes](https://docs.openshift.com/container-platform/4.13/installing/disconnected_install/installing-mirroring-creating-registry.html#mirror-registry-release-notes-1-1_installing-mirroring-creating-registry).

# Troubleshooting mirror registry for Red Hat OpenShift

To assist in troubleshooting the *mirror registry for Red Hat OpenShift*, you can check the status of the systemd service, view registry logs, and verify the registry health endpoint.

<div>

<div class="title">

Prerequisites

</div>

- You have installed the *mirror registry for Red Hat OpenShift*.

</div>

<div>

<div class="title">

Procedure

</div>

- Check the status of the `quay.service` systemd service:

  - For a root installation, enter the following command:

    ``` terminal
    $ systemctl status quay.service
    ```

  - For a non-root installation, enter the following command:

    ``` terminal
    $ systemctl --user status quay.service
    ```

- View the registry container logs by entering the following command:

  ``` terminal
  $ podman logs systemd-quay
  ```

- Verify that the registry is healthy by querying the health endpoint:

  ``` terminal
  $ curl -k https://<host_example_com>:8443/healthz
  ```

- If the registry is unresponsive or corrupted, you can reset it by uninstalling and reinstalling:

  ``` terminal
  $ ./mirror-registry uninstall -data-dir /var/lib/quay -auto-approve
  $ ./mirror-registry install -data-dir /var/lib/quay -image-archive image-archive.tar
  ```

</div>

# Additional resources

- [Securing Red Hat Quay](https://docs.redhat.com/en/documentation/red_hat_quay/3/html-single/securing_red_hat_quay/index)

- [Configuring the system to trust the certificate authority](https://docs.redhat.com/en/documentation/red_hat_quay/3/html-single/securing_red_hat_quay/index#configuring-system-trust-ca)

- [Mirroring the OpenShift Container Platform image repository](installing-mirroring-installation-images.md#installation-mirror-repository_installing-mirroring-installation-images)

- [Mirroring Operator catalogs for use with disconnected clusters](installing-mirroring-installation-images.md#olm-mirror-catalog_installing-mirroring-installation-images)
