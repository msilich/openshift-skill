<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

The *mirror registry for Red Hat OpenShift* is a small and streamlined container registry that you can use as a target for mirroring the required container images of OpenShift Container Platform for disconnected installations.

If you already have a container image registry, such as [Red Hat Quay](https://www.redhat.com/en/technologies/cloud-computing/quay), you can skip this section and go straight to [Mirroring the OpenShift Container Platform image repository](installing-mirroring-installation-images.md#installation-mirror-repository_installing-mirroring-installation-images).

> [!IMPORTANT]
> The *mirror registry for Red Hat OpenShift* is not intended to be a substitute for a production deployment of Red Hat Quay.

# Prerequisites

- An OpenShift Container Platform subscription.

- Red Hat Enterprise Linux (RHEL) 8 and 9 with Podman 3.4.2 or later and OpenSSL installed. If you are using Podman 5.7 or later, see "Configuring rootless Podman networking".

- Fully qualified domain name for the Red Hat Quay service, which must resolve through a DNS server.

- Key-based SSH connectivity on the target host. SSH keys are automatically generated for local installs. For remote hosts, you must generate your own SSH keys.

- 2 or more vCPUs.

- 8 GB of RAM.

- About 12 GB for OpenShift Container Platform 4.17 release images, or about 358 GB for OpenShift Container Platform 4.17 release images and OpenShift Container Platform 4.17 Red Hat Operator images.

  <div class="important">

  <div class="title">

  </div>

  - Up to 1 TB per stream or more is suggested.

  - These requirements are based on local testing results with only release images and Operator images. Storage requirements can vary based on your organization’s needs. You might require more space, for example, when you mirror multiple z-streams. You can use standard [Red Hat Quay functionality](https://access.redhat.com/documentation/en-us/red_hat_quay/3/html/use_red_hat_quay/index) or the proper [API callout](https://access.redhat.com/documentation/en-us/red_hat_quay/3/html-single/red_hat_quay_api_guide/index#deletefulltag) to remove unnecessary images and free up space.

  </div>

# Mirror registry for Red Hat OpenShift introduction

For disconnected deployments of OpenShift Container Platform, a container registry is required to carry out the installation of the clusters. To run a production-grade registry service on such a cluster, you must create a separate registry deployment to install the first cluster. The *mirror registry for Red Hat OpenShift* addresses this need and is included in every OpenShift Container Platform subscription. It is available for download on the [OpenShift console **Downloads**](https://console.redhat.com/openshift/downloads#tool-mirror-registry) page.

The *mirror registry for Red Hat OpenShift* allows users to install a small-scale version of Red Hat Quay and its required components by using the `mirror-registry` command-line interface (CLI) tool. The *mirror registry for Red Hat OpenShift* is deployed automatically with pre-configured local storage and a local database. It also includes auto-generated user credentials and access permissions with a single set of inputs and no additional configuration choices to get started.

The *mirror registry for Red Hat OpenShift* provides a pre-determined network configuration and reports deployed component credentials and access URLs upon success. A limited set of optional configuration inputs such as fully qualified domain name (FQDN) services, superuser name and password, and custom TLS certificates are also provided. This provides users with a container registry so that they can easily create an offline mirror of all OpenShift Container Platform release content when running OpenShift Container Platform in restricted network environments.

Use of the *mirror registry for Red Hat OpenShift* is optional if another container registry is already available in the install environment.

## Mirror registry for Red Hat OpenShift limitations

The following limitations apply to the *mirror registry for Red Hat OpenShift*:

- The *mirror registry for Red Hat OpenShift* is not a highly-available registry and only local file system storage is supported. It is not intended to replace Red Hat Quay or the internal image registry for OpenShift Container Platform.

- The *mirror registry for Red Hat OpenShift* is not intended to be a substitute for a production deployment of Red Hat Quay.

- The *mirror registry for Red Hat OpenShift* is only supported for hosting images that are required to install a disconnected OpenShift Container Platform cluster, such as Release images or Red Hat Operator images. It uses local storage on your Red Hat Enterprise Linux (RHEL) machine, and storage supported by RHEL is supported by the *mirror registry for Red Hat OpenShift*.

  > [!NOTE]
  > Because the *mirror registry for Red Hat OpenShift* uses local storage, you should remain aware of the storage usage consumed when mirroring images and use Red Hat Quay’s garbage collection feature to mitigate potential issues. For more information about this feature, see "Red Hat Quay garbage collection".

- Support for Red Hat product images that are pushed to the *mirror registry for Red Hat OpenShift* for bootstrapping purposes are covered by valid subscriptions for each respective product. A list of exceptions to further enable the bootstrap experience can be found on the [Self-managed Red Hat OpenShift sizing and subscription guide](https://www.redhat.com/en/resources/self-managed-openshift-sizing-subscription-guide).

- Content built by customers should not be hosted by the *mirror registry for Red Hat OpenShift*.

- Using the *mirror registry for Red Hat OpenShift* with more than one cluster is discouraged because multiple clusters can create a single point of failure when updating your cluster fleet. Instead, use the *mirror registry for Red Hat OpenShift* to install a cluster that can host a production-grade, highly-available registry such as Red Hat Quay, which can serve OpenShift Container Platform content to other clusters.

# Configuring rootless Podman networking

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

# Mirroring on a local host with mirror registry for Red Hat OpenShift

This procedure explains how to install the *mirror registry for Red Hat OpenShift* on a local host by using the `mirror-registry` installer tool. By doing so, users can create a local host registry running on port 443 for the purpose of storing a mirror of OpenShift Container Platform images.

> [!NOTE]
> Installing the *mirror registry for Red Hat OpenShift* using the `mirror-registry` CLI tool makes several changes to your machine. After installation, a `$HOME/quay-install` directory is created, which has installation files, local storage, and the configuration bundle. Trusted SSH keys are generated in case the deployment target is the local host, and systemd files on the host machine are set up to ensure that container runtimes are persistent. Additionally, an initial user named `init` is created with an automatically generated password. All access credentials are printed at the end of the install routine.

<div>

<div class="title">

Procedure

</div>

1.  Download the `mirror-registry.tar.gz` package for the latest version of the *mirror registry for Red Hat OpenShift* found on the [OpenShift console **Downloads**](https://console.redhat.com/openshift/downloads#tool-mirror-registry) page.

2.  Install the *mirror registry for Red Hat OpenShift* on your local host with your current user account by using the `mirror-registry` tool. For a full list of available flags, see "mirror registry for Red Hat OpenShift flags".

    ``` terminal
    $ ./mirror-registry install \
      --quayHostname <host_example_com> \
      --quayRoot <example_directory_name>
    ```

3.  Use the username and password generated during installation to log in to the registry by running the following command:

    ``` terminal
    $ podman login -u init \
      -p <password> \
      <host_example_com>:8443> \
      --tls-verify=false
    ```

    - You can avoid running `--tls-verify=false` by configuring your system to trust the generated rootCA certificates. See "Securing Red Hat Quay" and "Configuring the system to trust the certificate authority" for more information.

      > [!NOTE]
      > You can also log in by accessing the UI at `https://<host.example.com>:8443` after installation.

4.  You can mirror OpenShift Container Platform images after logging in. Depending on your needs, see either the "Mirroring the OpenShift Container Platform image repository" or the "Mirroring Operator catalogs for use with disconnected clusters" sections of this document.

    > [!NOTE]
    > If there are issues with images stored by the *mirror registry for Red Hat OpenShift* due to storage layer problems, you can re-mirror the OpenShift Container Platform images, or reinstall mirror registry on more stable storage.

</div>

# Updating mirror registry for Red Hat OpenShift from a local host

This procedure explains how to update the *mirror registry for Red Hat OpenShift* from a local host by using the `upgrade` command. Updating to the latest version ensures new features, bug fixes, and security vulnerability fixes.

> [!IMPORTANT]
> When upgrading from version 1 to version 2, be aware of the following constraints:
>
> - The worker count is set to `1` because multiple writes are not allowed in SQLite.
>
> - You must not use the *mirror registry for Red Hat OpenShift* user interface (UP).
>
> - Do not access the `sqlite-storage` Podman volume during the upgrade.
>
> - There is intermittent downtime of your mirror registry because it is restarted during the upgrade process.
>
> - PostgreSQL data is backed up under the `/$HOME/quay-install/quay-postgres-backup/` directory for recovery.

<div>

<div class="title">

Prerequisites

</div>

- You have installed the *mirror registry for Red Hat OpenShift* on a local host.

</div>

<div>

<div class="title">

Procedure

</div>

- To upgrade the *mirror registry for Red Hat OpenShift* using the existing certificates, enter the following command:

  ``` terminal
  $ sudo ./mirror-registry upgrade -v
  ```

  <div class="note">

  <div class="title">

  </div>

  - Starting with *mirror registry for Red Hat OpenShift* 2.0.11, the `upgrade` command preserves the existing `SERVER_HOSTNAME`, including custom ports, and the `quayRoot`, `quayStorage`, and `sqliteStorage` settings from the current installation. You do not need to pass `--quayHostname`, `--quayRoot`, `--quayStorage`, or `--sqliteStorage` for a standard upgrade. Pass these flags only when you want to override the preserved values.

  - When upgrading from 1.3 to 2.y with the default installation directory at `/etc/quay-install`, *mirror registry for Red Hat OpenShift* migrates Podman volumes for Red Hat Quay storage, Postgres data, and `/etc/quay-install` data to the new `$HOME/quay-install` location.

  </div>

- Optional: To override preserved install or storage paths during upgrade, pass the `--quayRoot`, `--quayStorage`, or `--sqliteStorage` flags. For example:

  ``` terminal
  $ sudo ./mirror-registry upgrade --quayRoot <example_directory_name> \
    --quayStorage <example_directory_name>/quay-storage \
    --sqliteStorage <example_directory_name>/sqlite-storage -v
  ```

- Optional: To rotate SSL/TLS certificates during upgrade (*mirror registry for Red Hat OpenShift* 2.0.11 and later), pass both the `--sslCert` and `--sslKey` flags. You must provide both flags together; if you pass only `--sslCert` or only `--sslKey`, the upgrade command fails with an error. For example:

  ``` terminal
  $ sudo ./mirror-registry upgrade --sslCert /path/to/new.cert \
    --sslKey /path/to/new.key -v
  ```

  To skip hostname validation when the certificate does not match `SERVER_HOSTNAME` in the Quay `config.yaml` file, for example when you use a wildcard or internal CA certificate, pass the `--sslCheckSkip` flag together with `--sslCert` and `--sslKey`. For example:

  ``` terminal
  $ sudo ./mirror-registry upgrade --sslCert /path/to/cert \
    --sslKey /path/to/key --sslCheckSkip -v
  ```

  <div class="important">

  <div class="title">

  </div>

  - If you do not pass SSL flags, the upgrade uses the existing certificates. A warning is displayed if the existing certificates are not found on the target host.

  - During a PostgreSQL to SQLite migration, missing certificates block the upgrade before any database changes are made.

  - The `--sslCheckSkip` flag skips CLI hostname validation only. Quay still requires valid `ssl.cert` and `ssl.key` configuration to start.

  </div>

</div>

<div>

<div class="title">

Verification

</div>

1.  Ensure that *mirror registry for Red Hat OpenShift* has been updated by running the following command:

    ``` terminal
    $ podman ps
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    registry.redhat.io/quay/quay-rhel8:v3.12.10
    ```

    </div>

</div>

# Mirroring on a remote host with mirror registry for Red Hat OpenShift

This procedure explains how to install the *mirror registry for Red Hat OpenShift* on a remote host by using the `mirror-registry` tool. By doing so, users can create a registry to hold a mirror of OpenShift Container Platform images.

> [!NOTE]
> Installing the *mirror registry for Red Hat OpenShift* using the `mirror-registry` CLI tool makes several changes to your machine. After installation, a `$HOME/quay-install` directory is created, which has installation files, local storage, and the configuration bundle. Trusted SSH keys are generated in case the deployment target is the local host, and systemd files on the host machine are set up to ensure that container runtimes are persistent. Additionally, an initial user named `init` is created with an automatically generated password. All access credentials are printed at the end of the install routine.

<div>

<div class="title">

Procedure

</div>

1.  Download the `mirror-registry.tar.gz` package for the latest version of the *mirror registry for Red Hat OpenShift* found on the [OpenShift console **Downloads**](https://console.redhat.com/openshift/downloads#tool-mirror-registry) page.

2.  Install the *mirror registry for Red Hat OpenShift* on your local host with your current user account by using the `mirror-registry` tool. For a full list of available flags, see "mirror registry for Red Hat OpenShift flags".

    ``` terminal
    $ ./mirror-registry install -v \
      --targetHostname <host_example_com> \
      --targetUsername <example_user> \
      -k ~/.ssh/my_ssh_key \
      --quayHostname <host_example_com> \
      --quayRoot <example_directory_name>
    ```

3.  Use the username and password generated during installation to log in to the mirror registry by running the following command:

    ``` terminal
    $ podman login -u init \
      -p <password> \
      <host_example_com>:8443> \
      --tls-verify=false
    ```

    - You can avoid running `--tls-verify=false` by configuring your system to trust the generated rootCA certificates. See "Securing Red Hat Quay" and "Configuring the system to trust the certificate authority" for more information.

      > [!NOTE]
      > You can also log in by accessing the UI at `https://<host.example.com>:8443` after installation.

4.  You can mirror OpenShift Container Platform images after logging in. Depending on your needs, see either the "Mirroring the OpenShift Container Platform image repository" or the "Mirroring Operator catalogs for use with disconnected clusters" sections of this document.

    > [!NOTE]
    > If there are issues with images stored by the *mirror registry for Red Hat OpenShift* due to storage layer problems, you can re-mirror the OpenShift Container Platform images, or reinstall mirror registry on more stable storage.

</div>

# Updating mirror registry for Red Hat OpenShift from a remote host

This procedure explains how to update the *mirror registry for Red Hat OpenShift* from a remote host by using the `upgrade` command. Updating to the latest version ensures bug fixes and security vulnerability fixes.

> [!IMPORTANT]
> When upgrading from version 1 to version 2, be aware of the following constraints:
>
> - The worker count is set to `1` because multiple writes are not allowed in SQLite.
>
> - You must not use the *mirror registry for Red Hat OpenShift* user interface (UP).
>
> - Do not access the `sqlite-storage` Podman volume during the upgrade.
>
> - There is intermittent downtime of your mirror registry because it is restarted during the upgrade process.
>
> - PostgreSQL data is backed up under the `/$HOME/quay-install/quay-postgres-backup/` directory for recovery.

<div>

<div class="title">

Prerequisites

</div>

- You have installed the *mirror registry for Red Hat OpenShift* on a remote host.

</div>

<div>

<div class="title">

Procedure

</div>

- To upgrade the *mirror registry for Red Hat OpenShift* from a remote host using the existing certificates, enter the following command:

  ``` terminal
  $ ./mirror-registry upgrade -v --targetHostname <remote_host_url> \
    --targetUsername <user_name> -k ~/.ssh/my_ssh_key
  ```

  > [!NOTE]
  > Starting with *mirror registry for Red Hat OpenShift* 2.0.11, the `./mirror-registry upgrade` command preserves the existing `SERVER_HOSTNAME`, including custom ports, and the `quayRoot`, `quayStorage`, and `sqliteStorage` settings from the current installation. You do not need to pass `--quayHostname`, `--quayRoot`, `--quayStorage`, or `--sqliteStorage` for a standard upgrade. Pass these flags only when you want to override the preserved values.

- Optional: To override preserved hostname, install, or storage paths during upgrade, pass the corresponding flags. For example:

  ``` terminal
  $ ./mirror-registry upgrade -v --targetHostname <remote_host_url> \
    --targetUsername <user_name> -k ~/.ssh/my_ssh_key \
    --quayHostname <host_example_com> \
    --quayRoot <example_directory_name> \
    --quayStorage <example_directory_name>/quay-storage \
    --sqliteStorage <example_directory_name>/sqlite-storage
  ```

- Optional: To rotate SSL/TLS certificates during upgrade (*mirror registry for Red Hat OpenShift* 2.0.11 and later), pass both the `--sslCert` and `--sslKey` flags. You must provide both flags together; if you pass only `--sslCert` or only `--sslKey`, the upgrade command fails with an error. For example:

  ``` terminal
  $ ./mirror-registry upgrade -v --targetHostname <remote_host_url> \
    --targetUsername <user_name> -k ~/.ssh/my_ssh_key \
    --sslCert /path/to/new.cert --sslKey /path/to/new.key
  ```

  To skip hostname validation when the certificate does not match `SERVER_HOSTNAME` in the Quay `config.yaml` file, for example when you use a wildcard or internal CA certificate, pass the `--sslCheckSkip` flag together with `--sslCert` and `--sslKey`. For example:

  ``` terminal
  $ ./mirror-registry upgrade -v --targetHostname <remote_host_url> \
    --targetUsername <user_name> -k ~/.ssh/my_ssh_key \
    --sslCert /path/to/cert --sslKey /path/to/key --sslCheckSkip
  ```

  <div class="important">

  <div class="title">

  </div>

  - If you do not pass SSL flags, the upgrade uses the existing certificates. A warning is displayed if the existing certificates are not found on the target host.

  - During a PostgreSQL to SQLite migration, missing certificates block the upgrade before any database changes are made.

  - The `--sslCheckSkip` flag skips CLI hostname validation only. Quay still requires valid `ssl.cert` and `ssl.key` configuration to start.

  </div>

</div>

<div>

<div class="title">

Verification

</div>

1.  Ensure that *mirror registry for Red Hat OpenShift* has been updated by running the following command:

    ``` terminal
    $ podman ps
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    registry.redhat.io/quay/quay-rhel8:v3.12.10
    ```

    </div>

</div>

# Replacing mirror registry for Red Hat OpenShift SSL/TLS certificates

In some cases, you might want to update your SSL/TLS certificates for the *mirror registry for Red Hat OpenShift*. This is useful in the following scenarios:

- If you are replacing the current *mirror registry for Red Hat OpenShift* certificate.

- If you are using the same certificate as the previous *mirror registry for Red Hat OpenShift* installation.

- If you are periodically updating the *mirror registry for Red Hat OpenShift* certificate.

Use the following procedure to replace *mirror registry for Red Hat OpenShift* SSL/TLS certificates.

<div>

<div class="title">

Prerequisites

</div>

- You have downloaded and installed the `./mirror-registry` binary from the [OpenShift console **Downloads**](https://console.redhat.com/openshift/downloads#tool-mirror-registry) page.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Enter the following command to install the *mirror registry for Red Hat OpenShift*:

    ``` terminal
    $ ./mirror-registry install \
    --quayHostname <host_example_com> \
    --quayRoot <example_directory_name>
    ```

    This installs the *mirror registry for Red Hat OpenShift* to the `$HOME/quay-install` directory.

2.  Prepare a new certificate authority (CA) bundle and generate new `ssl.key` and `ssl.crt` key files. For more information, see [Configuring SSL and TLS for Red Hat Quay](https://docs.redhat.com/en/documentation/red_hat_quay/3.15/html-single/securing_red_hat_quay/index#ssl-tls-quay-overview).

3.  Assign `/$HOME/quay-install` an environment variable, for example, `QUAY`, by entering the following command:

    ``` terminal
    $ export QUAY=/$HOME/quay-install
    ```

4.  Copy the new `ssl.crt` file to the `/$HOME/quay-install` directory by entering the following command:

    ``` terminal
    $ cp ~/ssl.crt $QUAY/quay-config
    ```

5.  Copy the new `ssl.key` file to the `/$HOME/quay-install` directory by entering the following command:

    ``` terminal
    $ cp ~/ssl.key $QUAY/quay-config
    ```

6.  Restart the `quay-app` application pod by entering the following command:

    ``` terminal
    $ systemctl --user restart quay-app
    ```

</div>

# Uninstalling the mirror registry for Red Hat OpenShift

Use the following procedure to uninstall the *mirror registry for Red Hat OpenShift* from your local host.

<div>

<div class="title">

Prerequisites

</div>

- You have installed *mirror registry for Red Hat OpenShift* on a local host.

</div>

<div>

<div class="title">

Procedure

</div>

- Uninstall the *mirror registry for Red Hat OpenShift* from your local host by running the following command:

  ``` terminal
  $ ./mirror-registry uninstall -v \
    --quayRoot <example_directory_name>
  ```

  <div class="note">

  <div class="title">

  </div>

  - Deleting the *mirror registry for Red Hat OpenShift* prompts the user before deletion. You can use `--autoApprove` to skip this prompt.

  - Users who install the *mirror registry for Red Hat OpenShift* with the `--quayRoot` flag must include the `--quayRoot` flag when uninstalling. For example, if you installed the *mirror registry for Red Hat OpenShift* with `--quayRoot example_directory_name`, you must include that string to properly uninstall the mirror registry.

  </div>

</div>

# Mirror registry for Red Hat OpenShift flags

The following flags are available for the *mirror registry for Red Hat OpenShift*:

| Flags | Description |
|----|----|
| `--autoApprove` | A boolean value that disables interactive prompts. If set to `true`, the `quayRoot` directory is automatically deleted when uninstalling the mirror registry. Defaults to `false` if left unspecified. |
| `--initPassword` | The password of the init user created during Quay installation. Must be at least eight characters and contain no whitespace. |
| `--initUser string` | Shows the username of the initial user. Defaults to `init` if left unspecified. |
| `--no-color`, `-c` | Allows users to disable color sequences and propagate that to Ansible when running install, uninstall, and upgrade commands. |
| `--quayHostname` | The fully-qualified domain name of the mirror registry that clients will use to contact the registry. Equivalent to `SERVER_HOSTNAME` in the Quay `config.yaml`. Must resolve by DNS. Defaults to `<targetHostname>:8443` if left unspecified. <sup>\[1\]</sup> |
| `--quayStorage` | The folder where Quay persistent storage data is saved. Defaults to the `quay-storage` Podman volume. Root privileges are required to uninstall. |
| `--quayRoot`, `-r` | The directory where container image layer and configuration data is saved, including `rootCA.key`, `rootCA.pem`, and `rootCA.srl` certificates. Defaults to `$HOME/quay-install` if left unspecified. |
| `--sqliteStorage` | The folder where SQLite database data is saved. Defaults to `sqlite-storage` Podman volume if not specified. Root is required to uninstall. |
| `--ssh-key`, `-k` | The path of your SSH identity key. Defaults to `~/.ssh/quay_installer` if left unspecified. |
| `--sslCert` | The path to the SSL/TLS public key / certificate. Defaults to `{quayRoot}/quay-config` and is auto-generated if left unspecified. |
| `--sslCheckSkip` | Skips the check for the certificate hostname against the `SERVER_HOSTNAME` in the `config.yaml` file. <sup>\[2\]</sup> |
| `--sslKey` | The path to the SSL/TLS private key used for HTTPS communication. Defaults to `{quayRoot}/quay-config` and is auto-generated if left unspecified. |
| `--targetHostname`, `-H` | The hostname of the target you want to install Quay to. Defaults to `$HOST`, for example, a local host, if left unspecified. |
| `--targetUsername`, `-u` | The user on the target host which will be used for SSH. Defaults to `$USER`, for example, the current user if left unspecified. |
| `--verbose`, `-v` | Shows debug logs and Ansible Playbook outputs. |
| `--version` | Shows the version for the *mirror registry for Red Hat OpenShift*. |

1.  `--quayHostname` must be modified if the public DNS name of your system is different from the local hostname. Additionally, the `--quayHostname` flag does not support installation with an IP address. Installation with a hostname is required.

2.  `--sslCheckSkip` is used in cases when the mirror registry is set behind a proxy and the exposed hostname is different from the internal Quay hostname. It can also be used when users do not want the certificates to be validated against the provided Quay hostname during installation.

# Mirror registry for Red Hat OpenShift release notes

The *mirror registry for Red Hat OpenShift* is a small and streamlined container registry that you can use as a target for mirroring the required container images of OpenShift Container Platform for disconnected installations.

These release notes track the development of the *mirror registry for Red Hat OpenShift* in OpenShift Container Platform.

## Mirror registry for Red Hat OpenShift 2.0 release notes

The following sections provide details for each 2.0 release of the mirror registry for Red Hat OpenShift.

### Mirror registry for Red Hat OpenShift 2.0.11

Issued: 22 June 2026

*Mirror registry for Red Hat OpenShift* is now available with Red Hat Quay 3.12.18.

The following advisory, which includes bug fixes, is available for the *mirror registry for Red Hat OpenShift*:

- [RHSA-2026:28441 - mirror registry for Red Hat OpenShift 2.0.11](https://access.redhat.com/errata/RHSA-2026:28441)

The following enhancements were added to this release:

- With this release, the `./mirror-registry upgrade` command supports `--sslCert`, `--sslKey`, and `--sslCheckSkip` flags for SSL/TLS certificate rotation during upgrades. You must provide `--sslCert` and `--sslKey` together; passing only one of these flags causes the upgrade to fail. For example:

  Rotate certificates during upgrade:

  ``` terminal
  $ ./mirror-registry upgrade --sslCert /path/to/new.cert --sslKey /path/to/new.key
  ```

  Skip hostname validation, for example when you use wildcard or internal CA certificates:

  ``` terminal
  $ ./mirror-registry upgrade --sslCert /path/to/cert --sslKey /path/to/key --sslCheckSkip
  ```

  Normal upgrade that uses existing certificates; no SSL flags are required:

  ``` terminal
  $ ./mirror-registry upgrade
  ```

  If you do not pass SSL flags, a warning is displayed when existing certificates are not found on the target host. During a PostgreSQL to SQLite migration, missing certificates block the upgrade before any database changes are made. The `--sslCheckSkip` flag skips CLI hostname validation only; Quay still requires `ssl.cert` and `ssl.key` to start.

- With this release, the `./mirror-registry upgrade` command automatically preserves the existing `SERVER_HOSTNAME`, including custom ports, and the `quayRoot`, `quayStorage`, and `sqliteStorage` settings from the current installation. You do not need to pass `--quayHostname`, `--quayRoot`, `--quayStorage`, or `--sqliteStorage` for a standard upgrade. Explicit flags override the preserved values if you provide them.

### Mirror registry for Red Hat OpenShift 2.0.10

Issued: 03 March 2026

*Mirror registry for Red Hat OpenShift* is now available with Red Hat Quay 3.12.14.

The following advisory is available for the *mirror registry for Red Hat OpenShift*:

- [RHBA-2026:3953 - mirror registry for Red Hat OpenShift 2.0.10](https://access.redhat.com/errata/RHBA-2026:3953)

The following bugs were fixed as part of this release:

- [PROJQUAY-9799](https://redhat.atlassian.net/browse/PROJQUAY-9799). In this update, upgrading from PostgreSQL to SQLite without proper configuration previously triggered a SQLite cursor error. This error prevented Quay from starting after the SQLite upgrade, leading to service disruption. With this release, the SQLite upgrade process no longer triggers the cursor error, enabling a successful Quay upgrade without crashes due to SQLite optimization issues.

- [PROJQUAY-10093](https://redhat.atlassian.net/browse/PROJQUAY-10093). The *Mirror registry for Red Hat OpenShift* has been upgraded to use the latest Redis 6 (`redis-6:1-1766406130`) version.

### Mirror registry for Red Hat OpenShift 2.0.9

Issued: 17 November 2025

*Mirror registry for Red Hat OpenShift* is now available with Red Hat Quay 3.12.13.

The following advisory is available for the *mirror registry for Red Hat OpenShift*:

- [RHBA-2025:21600 - mirror registry for Red Hat OpenShift 2.0.9](https://access.redhat.com/errata/RHBA-2025:21600)

### Mirror registry for Red Hat OpenShift 2.0.8

Issued: 16 October 2025

*Mirror registry for Red Hat OpenShift* is now available with Red Hat Quay 3.12.12.

The following advisory is available for the *mirror registry for Red Hat OpenShift*:

- [RHBA-2025:17062 - mirror registry for Red Hat OpenShift 2.0.8](https://access.redhat.com/errata/RHBA-2025:17062)

### Mirror registry for Red Hat OpenShift 2.0.7

Issued: 14 July 2025

*Mirror registry for Red Hat OpenShift* is now available with Red Hat Quay 3.12.10.

The following advisory is available for the *mirror registry for Red Hat OpenShift*:

- [RHBA-2025:9645 - mirror registry for Red Hat OpenShift 2.0.7](https://access.redhat.com/errata/RHBA-2025:9645)

### Mirror registry for Red Hat OpenShift 2.0.6

Issued: 28 April 2025

*Mirror registry for Red Hat OpenShift* is now available with Red Hat Quay 3.12.8.

The following advisory is available for the *mirror registry for Red Hat OpenShift*:

- [RHBA-2025:4251 - mirror registry for Red Hat OpenShift 2.0.6](https://access.redhat.com/errata/RHBA-2025:4251)

### Mirror registry for Red Hat OpenShift 2.0.5

Issued: 13 January 2025

*Mirror registry for Red Hat OpenShift* is now available with Red Hat Quay 3.12.5.

The following advisory is available for the *mirror registry for Red Hat OpenShift*:

- [RHBA-2025:0298 - mirror registry for Red Hat OpenShift 2.0.5](https://access.redhat.com/errata/RHBA-2025:0298)

### Mirror registry for Red Hat OpenShift 2.0.4

Issued: 06 January 2025

*Mirror registry for Red Hat OpenShift* is now available with Red Hat Quay 3.12.4.

The following advisory is available for the *mirror registry for Red Hat OpenShift*:

- [RHBA-2025:0033 - mirror registry for Red Hat OpenShift 2.0.4](https://access.redhat.com/errata/RHBA-2025:0033)

### Mirror registry for Red Hat OpenShift 2.0.3

Issued: 25 November 2024

*Mirror registry for Red Hat OpenShift* is now available with Red Hat Quay 3.12.3.

The following advisory is available for the *mirror registry for Red Hat OpenShift*:

- [RHBA-2024:10181 - mirror registry for Red Hat OpenShift 2.0.3](https://access.redhat.com/errata/RHBA-2024:10181)

### Mirror registry for Red Hat OpenShift 2.0.2

Issued: 31 October 2024

*Mirror registry for Red Hat OpenShift* is now available with Red Hat Quay 3.12.2.

The following advisory is available for the *mirror registry for Red Hat OpenShift*:

- [RHBA-2024:8370 - mirror registry for Red Hat OpenShift 2.0.2](https://access.redhat.com/errata/RHBA-2024:8370)

### Mirror registry for Red Hat OpenShift 2.0.1

Issued: 26 September 2024

*Mirror registry for Red Hat OpenShift* is now available with Red Hat Quay 3.12.1.

The following advisory is available for the *mirror registry for Red Hat OpenShift*:

- [RHBA-2024:7070 - mirror registry for Red Hat OpenShift 2.0.1](https://access.redhat.com/errata/RHBA-2024:7070)

### Mirror registry for Red Hat OpenShift 2.0.0

Issued: 03 September 2024

*Mirror registry for Red Hat OpenShift* is now available with Red Hat Quay 3.12.0.

The following advisory is available for the *mirror registry for Red Hat OpenShift*:

- [RHBA-2024:5277 - mirror registry for Red Hat OpenShift 2.0.0](https://access.redhat.com/errata/RHBA-2024:5277)

The following new features are available with *mirror registry for Red Hat OpenShift* 2.0.0:

- With the release of *mirror registry for Red Hat OpenShift*, the internal database has been upgraded from PostgreSQL to SQLite. As a result, data is now stored on the `sqlite-storage` Podman volume by default, and the overall tarball size is reduced by 300 MB.

  New installations use SQLite by default. Before upgrading to version 2.0, see "Updating mirror registry for Red Hat OpenShift from a local host" or "Updating mirror registry for Red Hat OpenShift from a remote host" depending on your environment.

- A new feature flag, `--sqliteStorage` has been added. With this flag, you can manually set the location where SQLite database data is saved.

- *Mirror registry for Red Hat OpenShift* is now available on IBM Power and IBM Z architectures (`s390x` and `ppc64le`).

## Mirror registry for Red Hat OpenShift 1.3 release notes

To view the *mirror registry for Red Hat OpenShift* 1.3 release notes, see [Mirror registry for Red Hat OpenShift 1.3 release notes](https://docs.redhat.com/en/documentation/openshift_container_platform/4.13/html/disconnected_installation_mirroring/installing-mirroring-creating-registry#mirror-registry-release-notes-1-3_installing-mirroring-creating-registry).

## Mirror registry for Red Hat OpenShift 1.2 release notes

To view the *mirror registry for Red Hat OpenShift* 1.2 release notes, see [Mirror registry for Red Hat OpenShift 1.2 release notes](https://docs.openshift.com/container-platform/4.13/installing/disconnected_install/installing-mirroring-creating-registry.html#mirror-registry-release-notes-1-2_installing-mirroring-creating-registry).

## Mirror registry for Red Hat OpenShift 1.1 release notes

To view the *mirror registry for Red Hat OpenShift* 1.1 release notes, see [Mirror registry for Red Hat OpenShift 1.1 release notes](https://docs.openshift.com/container-platform/4.13/installing/disconnected_install/installing-mirroring-creating-registry.html#mirror-registry-release-notes-1-1_installing-mirroring-creating-registry).

# Troubleshooting mirror registry for Red Hat OpenShift

To assist in troubleshooting *mirror registry for Red Hat OpenShift*, you can gather logs of systemd services installed by the mirror registry. The following services are installed:

- quay-app.service

- quay-redis.service

- quay-pod.service

<div>

<div class="title">

Prerequisites

</div>

- You have installed *mirror registry for Red Hat OpenShift*.

</div>

<div>

<div class="title">

Procedure

</div>

- If you installed *mirror registry for Red Hat OpenShift* with root privileges, you can get the status information of its systemd services by entering the following command:

  ``` terminal
  $ sudo systemctl status <service>
  ```

- If you installed *mirror registry for Red Hat OpenShift* as a standard user, you can get the status information of its systemd services by entering the following command:

  ``` terminal
  $ systemctl --user status <service>
  ```

</div>

# Additional resources

- [Red Hat Quay garbage collection](https://access.redhat.com/documentation/en-us/red_hat_quay/3/html/manage_red_hat_quay/garbage-collection#doc-wrapper)

- [Securing Red Hat Quay](https://docs.redhat.com/en/documentation/red_hat_quay/3/html-single/securing_red_hat_quay/index)

- [Configuring the system to trust the certificate authority](https://docs.redhat.com/en/documentation/red_hat_quay/3/html-single/securing_red_hat_quay/index#configuring-system-trust-ca)

- [Mirroring the OpenShift Container Platform image repository](installing-mirroring-installation-images.md#installation-mirror-repository_installing-mirroring-installation-images)

- [Mirroring Operator catalogs for use with disconnected clusters](installing-mirroring-installation-images.md#olm-mirror-catalog_installing-mirroring-installation-images)
