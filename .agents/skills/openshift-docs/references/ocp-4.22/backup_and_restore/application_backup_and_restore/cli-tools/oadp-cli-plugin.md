<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

The OpenShift API for Data Protection (OADP) command-line interface (CLI) plugin for the OpenShift CLI (`oc`) provides a kubectl-native interface for managing backup and restore operations on an OpenShift Container Platform cluster.

The plugin is available as `oc oadp` and supports both cluster administrator and non-administrator workflows. The administrator perspective provides cluster-wide backup and restore operations by using Velero resources. These commands are available when the OADP CLI is configured in admin mode.

# Install the OADP CLI plugin

The OADP command-line interface (CLI) plugin is available from the **Command-line tools** page in the OpenShift Container Platform web console when the OADP Operator is installed.

<div>

<div class="title">

Prerequisites

</div>

- You have access to an OpenShift Container Platform cluster with the OADP Operator installed.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Log in to the OpenShift Container Platform web console as a user with access to the cluster.

2.  Click the **?** icon in the toolbar and select **Command-line tools**.

3.  Download the `oc-oadp` binary for your operating system and architecture.

4.  Extract the archive and place the `oc-oadp` binary in a directory on your `PATH`.

5.  Verify the installation:

    ``` terminal
    $ oc oadp version
    ```

</div>

# Set up the OADP CLI plugin

After you install the OADP command-line interface (CLI) plugin, you must run the setup command to configure it for your user permissions.

The setup command automatically detects whether you have cluster-wide administrator permissions and configures the CLI accordingly. The CLI operates in one of the following two modes:

- **Admin mode**: Provides access to cluster-wide Velero backup and restore commands.

- **Non-administrator mode**: Provides access to namespace-scoped self-service backup and restore commands.

<div>

<div class="title">

Prerequisites

</div>

- The OADP CLI plugin is installed.

- You are logged in to the OpenShift Container Platform cluster by using the `oc login` command.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Run the setup command to auto-detect your permissions and configure the CLI:

    ``` terminal
    $ oc oadp setup
    ```

    The CLI checks whether you can create `backups.velero.io` resources across all namespaces. If you can, admin mode is enabled. Otherwise, non-administrator mode is enabled. The configuration is saved to `~/.config/velero/config.json`.

2.  To reconfigure the CLI after a change in permissions, run the setup command with the `--force` flag:

    ``` terminal
    $ oc oadp setup --force
    ```

</div>

<div>

<div class="title">

Verification

</div>

- Run the following command to confirm that the available commands match your configured mode:

  ``` terminal
  $ oc oadp --help
  ```

  > [!NOTE]
  > OADP CLI commands support both noun-verb and verb-noun ordering. For example, `oc oadp backup create` and `oc oadp create backup` are equivalent.

</div>

# OADP CLI client configuration commands

You can use the OADP command-line interface (CLI) to view and modify client configuration settings. Configuration is stored in `~/.config/velero/config.json`.

## Prerequisites

- The OADP CLI plugin is installed.

## Current configuration viewing command

To view the current client configuration, use the following command:

``` terminal
$ oc oadp client config get
```

## Configuration value setting command

To set a configuration value, use the following command:

``` terminal
$ oc oadp client config set <key>=<value>
```

where:

`<key>`
Specifies the configuration key to set.

`<value>`
Specifies the value for the configuration key.

<div class="formalpara">

<div class="title">

Example of setting the default namespace

</div>

``` terminal
$ oc oadp client config set namespace=openshift-adp
```

</div>

# Enable shell completion for the OADP CLI

You can use the OADP command-line interface (CLI) to generate and install shell completion scripts for command auto-completion.

<div>

<div class="title">

Prerequisites

</div>

- The OADP CLI plugin is installed.

</div>

<div>

<div class="title">

Procedure

</div>

- Choose one of the following methods to enable shell completion:

  - To install shell completions automatically for your current shell, use the following command:

    ``` terminal
    $ oc oadp completion install [flags]
    ```

    | Flag | Description |
    |----|----|
    | `--shell` | The shell type to install completions for. Supported values are `bash`, `zsh`, and `fish`. If this flag is not specified, the current shell is auto-detected. |

    Flags for the `oc oadp completion install` command

    <div class="formalpara">

    <div class="title">

    Example of installing completions for zsh

    </div>

    ``` terminal
    $ oc oadp completion install --shell zsh
    ```

    </div>

  - To generate a completion script for your shell without installing it, use the following command:

    ``` terminal
    $ oc oadp completion <shell_name>
    ```

    where:

    `<shell_name>`
    Specifies the name of your shell. Supported values are `bash`, `zsh`, `fish`, and `powershell`.

    You can redirect the output to a file or source it directly.

    <div class="formalpara">

    <div class="title">

    Example of writing a bash completion script

    </div>

    ``` terminal
    $ oc oadp completion bash > /etc/bash_completion.d/oc-oadp
    ```

    </div>

</div>

# Backup management commands

You can use the OADP command-line interface (CLI) to create, view, describe, download, and delete backups.

## Prerequisites

- The OADP CLI plugin is installed and configured in admin mode.

- You are logged in to the OpenShift Container Platform cluster as a user with `cluster-admin` privileges.

## Backup creation command

To create a backup of cluster resources, use the following command:

``` terminal
$ oc oadp backup create <backup_name> [flags]
```

| Flag | Description |
|----|----|
| `--include-namespaces` | The namespaces to include in the backup. The default value is `*` (all namespaces). |
| `--exclude-namespaces` | The namespaces to exclude from the backup. |
| `--include-resources` | The resources to include in the backup. You can specify simple kind names, for example, `deployments,services`, or you can use the `resource.group` format for disambiguation, for example, `deployments.apps`. The default value is `*` (all resources). |
| `--exclude-resources` | The resources to exclude from the backup. This flag uses the same format as the `--include-resources` flag. |
| `--storage-location` | The name of the backup storage location to use. |
| `--volume-snapshot-locations` | The volume snapshot location or locations to use. |
| `--selector`, `-l` | A label selector to filter resources. |
| `--or-selector` | An OR combination of label selectors. |
| `--snapshot-volumes` | Specifies whether to take persistent volume (PV) snapshots. The default value is `true`. |
| `--snapshot-move-data` | Specifies whether to move snapshot data to the backup storage location. |
| `--default-volumes-to-fs-backup` | Specifies whether to use a file system backup for all volumes. |
| `--include-cluster-resources` | Specifies whether to include cluster-scoped resources. |
| `--ttl` | The backup retention period. The default value is `720h`. |
| `--csi-snapshot-timeout` | The timeout for Container Storage Interface (CSI) snapshot creation. |
| `--item-operation-timeout` | The timeout for asynchronous plugin operations. |
| `--request-timeout` | The timeout for the request to the Kubernetes API server. |

Flags for the `oc oadp backup create` command

<div class="formalpara">

<div class="title">

Example of the backup creation command

</div>

``` terminal
$ oc oadp backup create my-backup \
    --include-namespaces my-namespace \
    --snapshot-volumes \
    --ttl 720h
```

</div>

## Backup listing command

To list all backups, use the following command:

``` terminal
$ oc oadp backup get [<backup_name>] [flags]
```

| Flag | Description                                                |
|------|------------------------------------------------------------|
| `-o` | The output format. Supported values are `json` and `yaml`. |

Flags for the `oc oadp backup get` command

## Backup description command

To view the details of a backup, use the following command:

``` terminal
$ oc oadp backup describe <backup_name> [flags]
```

| Flag | Description |
|----|----|
| `--details` | Specifies whether to display additional details in the output. |

Flags for the `oc oadp backup describe` command

## Backup logs command

To view the logs for a backup, use the following command:

``` terminal
$ oc oadp backup logs <backup_name>
```

## Backup download command

To download the contents of a backup, use the following command:

``` terminal
$ oc oadp backup download <backup_name> [flags]
```

## Backup deletion command

To delete a backup, use the following command:

``` terminal
$ oc oadp backup delete <backup_name> [flags]
```

| Flag        | Description                                                  |
|-------------|--------------------------------------------------------------|
| `--confirm` | Specifies whether to confirm the deletion without prompting. |

Flags for the `oc oadp backup delete` command

# Restore management commands

You can use the OADP command-line interface (CLI) to create, view, describe, and delete restores.

## Prerequisites

- The OADP CLI plugin is installed and configured in admin mode.

- You are logged in to the OpenShift Container Platform cluster as a user with `cluster-admin` privileges.

- A completed backup exists to restore from.

## Restore creation command

To create a restore from an existing backup, use the following command:

``` terminal
$ oc oadp restore create <restore_name> [flags]
```

| Flag | Description |
|----|----|
| `--from-backup` | The name of the backup to restore from. |
| `--from-schedule` | The name of the schedule to restore from. This flag uses the most recent backup. |
| `--include-namespaces` | The namespaces to include in the restore. The default value is `*` (all namespaces). |
| `--exclude-namespaces` | The namespaces to exclude from the restore. |
| `--include-resources` | The resources to include in the restore. You can specify simple kind names, for example, `deployments,services`, or you can use the `resource.group` format for disambiguation, for example, `deployments.apps`. The default value is `*` (all resources). |
| `--exclude-resources` | The resources to exclude from the restore. This flag uses the same format as the `--include-resources` flag. |
| `--selector`, `-l` | A label selector to filter resources. |
| `--or-selector` | An OR combination of label selectors. |
| `--include-cluster-resources` | Specifies whether to include cluster-scoped resources. |
| `--restore-volumes` | Specifies whether to restore persistent volume (PV) data from snapshots. |
| `--preserve-nodeports` | Specifies whether to preserve NodePort service port assignments. |
| `--item-operation-timeout` | The timeout for asynchronous plugin operations. |
| `--request-timeout` | The timeout for the request to the Kubernetes API server. |

Flags for the `oc oadp restore create` command

<div class="formalpara">

<div class="title">

Example of the restore creation command

</div>

``` terminal
$ oc oadp restore create my-restore \
    --from-backup my-backup \
    --include-namespaces my-namespace
```

</div>

## Restore listing command

To list all restores, use the following command:

``` terminal
$ oc oadp restore get [<restore_name>] [flags]
```

| Flag | Description                                                |
|------|------------------------------------------------------------|
| `-o` | The output format. Supported values are `json` and `yaml`. |

Flags for the `oc oadp restore get` command

## Restore description command

To view the details of a restore, use the following command:

``` terminal
$ oc oadp restore describe <restore_name> [flags]
```

| Flag | Description |
|----|----|
| `--details` | Specifies whether to display additional details in the output. |

Flags for the `oc oadp restore describe` command

## Restore logs command

To view the logs for a restore, use the following command:

``` terminal
$ oc oadp restore logs <restore_name>
```

## Restore deletion command

To delete a restore, use the following command:

``` terminal
$ oc oadp restore delete <restore_name> [flags]
```

| Flag        | Description                                                  |
|-------------|--------------------------------------------------------------|
| `--confirm` | Specifies whether to confirm the deletion without prompting. |

Flags for the `oc oadp restore delete` command

# Schedule management commands

You can use the OADP command-line interface (CLI) to create, view, describe, and delete backup schedules. Schedules automate the creation of backups at specified intervals by using a cron expression.

## Prerequisites

- The OADP CLI plugin is installed and configured in admin mode.

- You are logged in to the OpenShift Container Platform cluster as a user with `cluster-admin` privileges.

## Schedule creation command

To create a backup schedule, use the following command:

``` terminal
$ oc oadp schedule create <schedule_name> [flags]
```

| Flag | Description |
|----|----|
| `--schedule` | The cron expression for the schedule, for example, `0 1 * * *` for daily at 1 AM. |
| `--include-namespaces` | The namespaces to include in scheduled backups. The default value is `*` (all namespaces). |
| `--exclude-namespaces` | The namespaces to exclude from scheduled backups. |
| `--include-resources` | The resources to include in scheduled backups. You can specify simple kind names, for example, `deployments,services`, or you can use the `resource.group` format for disambiguation, for example, `deployments.apps`. The default value is `*` (all resources). |
| `--exclude-resources` | The resources to exclude from scheduled backups. This flag uses the same format as the `--include-resources` flag. |
| `--storage-location` | The name of the backup storage location to use. |
| `--volume-snapshot-locations` | The volume snapshot location or locations to use. |
| `--selector`, `-l` | A label selector to filter resources. |
| `--snapshot-volumes` | Specifies whether to take persistent volume (PV) snapshots. The default value is `true`. |
| `--snapshot-move-data` | Specifies whether to move snapshot data to the backup storage location. |
| `--default-volumes-to-fs-backup` | Specifies whether to use a file system backup for all volumes. |
| `--include-cluster-resources` | Specifies whether to include cluster-scoped resources. |
| `--ttl` | The backup retention period. The default value is `720h`. |
| `--request-timeout` | The timeout for the request to the Kubernetes API server. |

Flags for the `oc oadp schedule create` command

<div class="formalpara">

<div class="title">

Example of the schedule creation command

</div>

``` terminal
$ oc oadp schedule create daily-backup \
    --schedule "0 1 * * *" \
    --include-namespaces my-namespace \
    --ttl 720h
```

</div>

## Schedule listing command

To list all schedules, use the following command:

``` terminal
$ oc oadp schedule get [<schedule_name>] [flags]
```

| Flag | Description                                                |
|------|------------------------------------------------------------|
| `-o` | The output format. Supported values are `json` and `yaml`. |

Flags for the `oc oadp schedule get` command

## Schedule description command

To view the details of a schedule, use the following command:

``` terminal
$ oc oadp schedule describe <schedule_name>
```

## Schedule deletion command

To delete a schedule, use the following command:

``` terminal
$ oc oadp schedule delete <schedule_name> [flags]
```

| Flag        | Description                                                  |
|-------------|--------------------------------------------------------------|
| `--confirm` | Specifies whether to confirm the deletion without prompting. |

Flags for the `oc oadp schedule delete` command

# Backup storage location management commands

You can use the OADP command-line interface (CLI) to create, view, set, and delete backup storage locations (BSLs). Backup storage locations define where backup data is stored, such as an object storage bucket.

## Prerequisites

- The OADP CLI plugin is installed and configured in admin mode.

- You are logged in to the OpenShift Container Platform cluster as a user with `cluster-admin` privileges.

## Backup storage location creation command

To create a backup storage location, use the following command:

``` terminal
$ oc oadp backup-location create <bsl_name> [flags]
```

| Flag | Description |
|----|----|
| `--provider` | The name of the cloud provider, for example, `aws`, `gcp`, or `azure`. |
| `--bucket` | The name of the object storage bucket. |
| `--prefix` | The path prefix within the bucket. |
| `--credential` | The secret and key for the provider credentials in the format `SECRET_NAME=KEY`. |
| `--config` | The provider-specific configuration as `key=value` pairs. |
| `--backup-sync-period` | The frequency at which to synchronize the backup contents from object storage. |
| `--request-timeout` | The timeout for the request to the Kubernetes API server. |

Flags for the `oc oadp backup-location create` command

<div class="formalpara">

<div class="title">

Example of the backup storage location creation command

</div>

``` terminal
$ oc oadp backup-location create my-bsl \
    --provider aws \
    --bucket my-velero-bucket \
    --prefix velero \
    --credential cloud-credentials=cloud
```

</div>

## Backup storage location listing command

To list all backup storage locations, use the following command:

``` terminal
$ oc oadp backup-location get [<bsl_name>] [flags]
```

| Flag | Description                                                |
|------|------------------------------------------------------------|
| `-o` | The output format. Supported values are `json` and `yaml`. |

Flags for the `oc oadp backup-location get` command

## Default backup storage location command

To set the default backup storage location, use the following command:

``` terminal
$ oc oadp backup-location set <bsl_name>
```

## Backup storage location deletion command

To delete a backup storage location, use the following command:

``` terminal
$ oc oadp backup-location delete <bsl_name> [flags]
```

| Flag        | Description                                                  |
|-------------|--------------------------------------------------------------|
| `--confirm` | Specifies whether to confirm the deletion without prompting. |

Flags for the `oc oadp backup-location delete` command

# Volume snapshot location management commands

You can use the OADP command-line interface (CLI) to create, view, set, and delete volume snapshot locations (VSLs). Volume snapshot locations define where persistent volume (PV) snapshots are stored.

## Prerequisites

- The OADP CLI plugin is installed and configured in admin mode.

- You are logged in to the OpenShift Container Platform cluster as a user with `cluster-admin` privileges.

## Volume snapshot location creation command

To create a volume snapshot location, use the following command:

``` terminal
$ oc oadp snapshot-location create <vsl_name> [flags]
```

| Flag | Description |
|----|----|
| `--provider` | The name of the cloud provider, for example, `aws`, `gcp`, or `azure`. |
| `--config` | The provider-specific configuration as `key=value` pairs. |
| `--request-timeout` | The timeout for the request to the Kubernetes API server. |

Flags for the `oc oadp snapshot-location create` command

<div class="formalpara">

<div class="title">

Example of the volume snapshot location creation command

</div>

``` terminal
$ oc oadp snapshot-location create my-vsl \
    --provider aws \
    --config region=us-east-1
```

</div>

## Volume snapshot location listing command

To list all volume snapshot locations, use the following command:

``` terminal
$ oc oadp snapshot-location get [<vsl_name>] [flags]
```

| Flag | Description                                                |
|------|------------------------------------------------------------|
| `-o` | The output format. Supported values are `json` and `yaml`. |

Flags for the `oc oadp snapshot-location get` command

## Default volume snapshot location command

To set the default volume snapshot location, use the following command:

``` terminal
$ oc oadp snapshot-location set <vsl_name>
```

## Volume snapshot location deletion command

To delete a volume snapshot location, use the following command:

``` terminal
$ oc oadp snapshot-location delete <vsl_name> [flags]
```

| Flag        | Description                                                  |
|-------------|--------------------------------------------------------------|
| `--confirm` | Specifies whether to confirm the deletion without prompting. |

Flags for the `oc oadp snapshot-location delete` command

# NonAdminBackupStorageLocation approval request commands

When the OADP Operator is configured with `nonAdmin.requireApprovalForBSL: true`, non-admin users who create a `NonAdminBackupStorageLocation` (NABSL) object trigger an approval request. You can use the OADP command-line interface (CLI) to view, describe, approve, and reject these requests.

## Prerequisites

- The OADP CLI plugin is installed and configured in admin mode.

- You are logged in to the OpenShift Container Platform cluster as a user with `cluster-admin` privileges.

- The `DataProtectionApplication` custom resource (CR) is configured with `nonAdmin.enable: true` and `nonAdmin.requireApprovalForBSL: true`.

## NABSL approval request listing command

To list all pending NABSL approval requests, use the following command:

``` terminal
$ oc oadp nabsl-request get [<request_name>] [flags]
```

| Flag | Description                                                |
|------|------------------------------------------------------------|
| `-o` | The output format. Supported values are `json` and `yaml`. |

Flags for the `oc oadp nabsl-request get` command

The output displays the request name, namespace, phase, requested NABSL name, requested namespace, and age.

## NABSL approval request description command

To view the full details of an approval request, including the requested backup storage location specification, use the following command:

``` terminal
$ oc oadp nabsl-request describe <request_name>
```

You can specify the request by using either the NABSL name or the full UUID.

## NABSL approval request approval command

To approve a pending request and allow the controller to create the corresponding `BackupStorageLocation` object, use the following command:

``` terminal
$ oc oadp nabsl-request approve <request_name> [flags]
```

| Flag       | Description                                         |
|------------|-----------------------------------------------------|
| `--reason` | The reason for the approval. This flag is optional. |

Flags for the `oc oadp nabsl-request approve` command

You can specify the request by using either the NABSL name or the full UUID.

<div class="formalpara">

<div class="title">

Example of the NABSL approval request approval command

</div>

``` terminal
$ oc oadp nabsl-request approve user-test-bsl --reason "Approved for production use"
```

</div>

## NABSL approval request rejection command

To reject a pending request and deny the user’s request for a backup storage location, use the following command:

``` terminal
$ oc oadp nabsl-request reject <request_name> [flags]
```

| Flag       | Description                                             |
|------------|---------------------------------------------------------|
| `--reason` | The reason for the rejection. This flag is recommended. |

Flags for the `oc oadp nabsl-request reject` command

You can specify the request by using either the NABSL name or the full UUID.

<div class="formalpara">

<div class="title">

Example of the NABSL approval request rejection command

</div>

``` terminal
$ oc oadp nabsl-request reject user-test-bsl --reason "Invalid configuration"
```

</div>

# Collect diagnostic data

You can use the OADP command-line interface (CLI) to collect diagnostic information for OADP installations. The `must-gather` command runs the OADP must-gather tool to collect logs and cluster state information needed for troubleshooting and support cases.

<div>

<div class="title">

Prerequisites

</div>

- The OADP CLI plugin is installed and configured in admin mode.

- You are logged in to the OpenShift Container Platform cluster as a user with `cluster-admin` privileges.

- The `oc` CLI is installed and available on your `PATH`.

</div>

<div>

<div class="title">

Procedure

</div>

- Collect OADP diagnostic information:

  ``` terminal
  $ oc oadp must-gather [flags]
  ```

  | Flag | Description |
  |----|----|
  | `--dest-dir` | The directory where the must-gather output is stored. The default value is `./must-gather`. |
  | `--request-timeout` | The timeout for the gather script, for example, `30s` or `1m`. |
  | `--skip-tls` | Specifies whether to skip Transport Layer Security (TLS) verification. |

  Flags for the `oc oadp must-gather` command

  <div class="formalpara">

  <div class="title">

  Example of the must-gather command

  </div>

  ``` terminal
  $ oc oadp must-gather --dest-dir=/tmp/oadp-diagnostics --request-timeout=1m
  ```

  </div>

</div>

# OADP self-service

Non-administrator users can use OADP self-service to perform backup and restore operations in their authorized namespaces without requiring cluster-wide administrator privileges.

This feature provides secure, self-service data protection while maintaining administrator controls over backup and restore operations.

You can use OADP self-service to complete the following tasks:

- Create and manage namespace-scoped backups and restores.

- View backup and restore status and logs.

- Create dedicated backup storage locations with user-owned buckets and credentials.

## Limitations

- Cross-cluster operations and migrations are not supported for non-administrator users.

- Non-administrator volume snapshot locations (VSLs) are not supported. The VSL configured by the cluster administrator in the `DataProtectionApplication` custom resource (CR) is used.

- Backups and restores are scoped to the namespace from which the command is run. You cannot specify a different namespace.

- Cluster-scoped resources cannot be included in backups or restores.

- `ResourceModifiers` and volume policies are not supported for non-administrator backup and restore operations.

- Backup and restore logs by using a `NonAdminDownloadRequest` object are not supported for default backup storage locations (BSLs). To access logs, you must create a `NonAdminBackupStorageLocation` object.

## Prerequisites for non-administrator users

Before you use OADP self-service, a cluster administrator must complete the following tasks:

- Install and configure the OADP Operator with `nonAdmin.enable: true` in the `DataProtectionApplication` CR specification.

- Create your user account, namespace, and namespace privileges, such as namespace administrator.

- Grant editor roles for the following resources in your namespace:

  - `nonadminbackups.oadp.openshift.io`

  - `nonadminrestores.oadp.openshift.io`

  - `nonadminbackupstoragelocations.oadp.openshift.io`

  - `nonadmindownloadrequests.oadp.openshift.io`

- Optionally, create a `NonAdminBackupStorageLocation` object for your namespace.

# Non-admin backup management commands

You can use the OADP command-line interface (CLI) to create, view, describe, and delete non-admin backups in your namespace.

## Prerequisites

- The OADP CLI plugin is installed and configured in non-admin mode.

- You are logged in to the OpenShift Container Platform cluster and your current namespace context is set to the namespace you want to back up.

- You have editor roles for `nonadminbackups.oadp.openshift.io` in your namespace.

- A `NonAdminBackupStorageLocation` object exists in your namespace, or a default has been configured by running the `oc oadp client config set default-nabsl=<name>` command.

## Non-admin backup creation command

To create a backup of resources in your current namespace, use the following command:

``` terminal
$ oc oadp nonadmin backup create <backup_name> [flags]
```

| Flag | Description |
|----|----|
| `--storage-location` | The name of the `NonAdminBackupStorageLocation` object to use. This flag is required unless a default is configured. |
| `--include-resources` | The resources to include in the backup. You can specify simple kind names, for example, `deployments,services`, or you can use the `resource.group` format for disambiguation, for example, `deployments.apps`. The default value is `*` (all resources). |
| `--exclude-resources` | The resources to exclude from the backup. This flag uses the same format as the `--include-resources` flag. |
| `--selector`, `-l` | Specifies to back up only the resources that match this label selector. |
| `--or-selector` | Specifies to back up resources that match at least one of the label selectors, separated by `or`. |
| `--ttl` | The amount of time before the backup can be garbage collected. The default value is `720h`. |
| `--csi-snapshot-timeout` | The timeout for Container Storage Interface (CSI) snapshot creation. |
| `--item-operation-timeout` | The timeout for asynchronous plugin operations. |
| `--snapshot-volumes` | Specifies whether to take snapshots of persistent volumes (PVs) as part of the backup. |
| `--snapshot-move-data` | Specifies whether to move snapshot data to the backup storage location. |
| `--default-volumes-to-fs-backup` | Specifies whether to use pod volume file system backups by default for all volumes. |

Flags for the `oc oadp nonadmin backup create` command

<div class="formalpara">

<div class="title">

Example of the non-admin backup creation command

</div>

``` terminal
$ oc oadp nonadmin backup create my-backup \
    --storage-location my-nabsl \
    --include-resources deployments,services \
    --selector app=myapp \
    --snapshot-volumes \
    --ttl 720h
```

</div>

> [!TIP]
> To avoid specifying the storage location on each backup, run the following command to set a default:
>
> ``` terminal
> $ oc oadp client config set default-nabsl=<nabsl_name>
> ```

## Non-admin backup listing command

To list all backups in your current namespace, use the following command:

``` terminal
$ oc oadp nonadmin backup get [<backup_name>] [flags]
```

| Flag | Description                                                |
|------|------------------------------------------------------------|
| `-o` | The output format. Supported values are `json` and `yaml`. |

Flags for the `oc oadp nonadmin backup get` command

## Non-admin backup description command

To view the details of a backup, use the following command:

``` terminal
$ oc oadp nonadmin backup describe <backup_name> [flags]
```

| Flag | Description |
|----|----|
| `--details` | Specifies whether to display additional backup details, including volume snapshots, resource lists, and item operations. |
| `--request-timeout` | The timeout for fetching backup details from the server. |

Flags for the `oc oadp nonadmin backup describe` command

## Non-admin backup logs command

To view the logs for a backup, use the following command:

``` terminal
$ oc oadp nonadmin backup logs <backup_name> [flags]
```

| Flag                | Description                                    |
|---------------------|------------------------------------------------|
| `--request-timeout` | The timeout for fetching logs from the server. |

Flags for the `oc oadp nonadmin backup logs` command

> [!NOTE]
> Backup logs are available only when you use a `NonAdminBackupStorageLocation` object. Logs are not available for backups that use the default cluster backup storage location.

## Non-admin backup deletion command

To delete one or more backups, use the following command:

``` terminal
$ oc oadp nonadmin backup delete [<backup_name>...] [flags]
```

| Flag | Description |
|----|----|
| `--confirm` | Specifies whether to skip the confirmation prompt and delete immediately. |
| `--all` | Specifies whether to delete all backups in the current namespace. |

Flags for the `oc oadp nonadmin backup delete` command

Backup deletion is performed asynchronously by the OADP non-admin controller.

<div class="formalpara">

<div class="title">

Example of the non-admin backup deletion command

</div>

``` terminal
$ oc oadp nonadmin backup delete my-backup --confirm
```

</div>

# Non-administrator restore management commands

You can use the OADP command-line interface (CLI) to create, view, describe, and delete non-administrator restores in your namespace.

## Prerequisites

- The OADP CLI plugin is installed and configured in non-administrator mode.

- You are logged in to the OpenShift Container Platform cluster and your current namespace context is set to the namespace you want to restore into.

- You have editor roles for `nonadminrestores.oadp.openshift.io` in your namespace.

- A completed non-administrator backup exists to restore from.

## Non-administrator restore creation command

To create a restore from an existing non-administrator backup, use the following command:

``` terminal
$ oc oadp nonadmin restore create [<restore_name>] [flags]
```

where:

`<restore_name>`
Specifies the name of the restore. This value is optional. If you do not provide a name, a name is automatically generated.

| Flag | Description |
|----|----|
| `--backup-name` | The name of the non-administrator backup to restore from. This flag is required. |
| `--include-resources` | The resources to include in the restore. You can specify simple kind names, for example, `deployments,services`, or you can use the `resource.group` format for disambiguation, for example, `deployments.apps`. The default value is `*` (all resources). |
| `--exclude-resources` | The resources to exclude from the restore. This flag uses the same format as the `--include-resources` flag. |
| `--selector`, `-l` | Specifies that only the resources that match this label selector are restored. |
| `--or-selector` | Specifies that resources that match at least one of the label selectors, separated by `or`, are restored. |
| `--item-operation-timeout` | The timeout for asynchronous plugin operations. |

Flags for the `oc oadp nonadmin restore create` command

<div class="formalpara">

<div class="title">

Example of the non-administrator restore creation command

</div>

``` terminal
$ oc oadp nonadmin restore create my-restore \
    --backup-name my-backup \
    --include-resources deployments,services \
    --selector app=myapp
```

</div>

## Non-administrator restore listing command

To list all restores in your current namespace, use the following command:

``` terminal
$ oc oadp nonadmin restore get [<restore_name>] [flags]
```

where:

`<restore_name>`
Specifies the name of the restore. This value is optional.

| Flag | Description                                                |
|------|------------------------------------------------------------|
| `-o` | The output format. Supported values are `json` and `yaml`. |

Flags for the `oc oadp nonadmin restore get` command

## Non-administrator restore description command

To view the details of a restore, use the following command:

``` terminal
$ oc oadp nonadmin restore describe <restore_name> [flags]
```

where:

`<restore_name>`
Specifies the name of the restore.

| Flag | Description |
|----|----|
| `--details` | Specifies whether to display additional restore details. |
| `--request-timeout` | The timeout for fetching restore details from the server. |

Flags for the `oc oadp nonadmin restore describe` command

## Non-administrator restore logs command

To view the logs for a restore, use the following command:

``` terminal
$ oc oadp nonadmin restore logs <restore_name> [flags]
```

where:

`<restore_name>`
Specifies the name of the restore.

| Flag                | Description                                    |
|---------------------|------------------------------------------------|
| `--request-timeout` | The timeout for fetching logs from the server. |

Flags for the `oc oadp nonadmin restore logs` command

> [!NOTE]
> Restore logs are available only when you use a `NonAdminBackupStorageLocation` object. Logs are not available for restores associated with backups that use the default cluster backup storage location.

## Non-administrator restore deletion command

To delete one or more restores, use the following command:

``` terminal
$ oc oadp nonadmin restore delete [<restore_name>...] [flags]
```

where:

`<restore_name>`
Specifies the name of the restore. You can specify multiple restores.

| Flag | Description |
|----|----|
| `--confirm` | Specifies whether to skip the confirmation prompt and delete immediately. |
| `--all` | Specifies whether to delete all restores in the current namespace. |

Flags for the `oc oadp nonadmin restore delete` command

Restore deletion is performed asynchronously by the OADP non-administrator controller.

<div class="formalpara">

<div class="title">

Example of the non-administrator restore deletion command

</div>

``` terminal
$ oc oadp nonadmin restore delete my-restore --confirm
```

</div>

# NonAdminBackupStorageLocation management commands

You can use the OADP command-line interface (CLI) to create and view `NonAdminBackupStorageLocation` (NABSL) objects in your namespace. NABSLs define where your backup data is stored by using object storage that you own and manage.

> [!NOTE]
> Updating or deleting NABSLs after creation is not supported for non-administrator users.

## Prerequisites

- The OADP CLI plugin is installed and configured in non-administrator mode.

- You are logged in to the OpenShift Container Platform cluster and your current namespace context is set to the target namespace.

- You have editor roles for `nonadminbackupstoragelocations.oadp.openshift.io` in your namespace.

- You have a Kubernetes `Secret` object in your namespace that contains the credentials for your object storage provider.

## NonAdminBackupStorageLocation creation command

To create a non-administrator backup storage location, use the following command:

``` terminal
$ oc oadp nonadmin bsl create <bsl_name> [flags]
```

where:

`<bsl_name>`
Specifies the name of the backup storage location.

| Flag | Description |
|----|----|
| `--provider` | The storage provider, for example, `aws`, `azure`, or `gcp`. This flag is required. |
| `--bucket` | The name of the object storage bucket. This flag is required. |
| `--credential` | The credential for this location in the format `SECRET_NAME=KEY`, where `SECRET_NAME` is the name of the Kubernetes `Secret` object and `KEY` is the data key within the secret. This flag is required. |
| `--prefix` | The prefix for backup objects in the bucket. |
| `--region` | The storage region. This flag is required for some providers, such as AWS. |
| `--config` | Additional provider-specific configuration as `key=value` pairs. |

Flags for the `oc oadp nonadmin bsl create` command

If the cluster administrator has enabled the `requireApprovalForBSL` parameter, the NABSL remains in a pending state until an administrator approves the request.

<div class="formalpara">

<div class="title">

Example of the NABSL creation command

</div>

``` terminal
$ oc oadp nonadmin bsl create my-storage \
    --provider aws \
    --bucket my-velero-bucket \
    --prefix velero-backups \
    --credential cloud-credentials=cloud \
    --region us-east-1
```

</div>

> [!TIP]
> After you create a backup storage location (BSL), run the following command to set it as the default and avoid specifying the storage location on each backup:
>
> ``` terminal
> $ oc oadp client config set default-nabsl=<bsl_name>
> ```
>
> where:
>
> `<bsl_name>`
> Specifies the name of the backup storage location.

## NonAdminBackupStorageLocation listing command

To list all non-administrator backup storage locations in your current namespace, use the following command:

``` terminal
$ oc oadp nonadmin bsl get [<bsl_name>] [flags]
```

where:

`<bsl_name>`
Specifies the name of the backup storage location. This value is optional.

| Flag | Description                                                |
|------|------------------------------------------------------------|
| `-o` | The output format. Supported values are `json` and `yaml`. |

Flags for the `oc oadp nonadmin bsl get` command

# Additional resources

- [Backing up applications](../backing_up_and_restoring/backing-up-applications.md#backing-up-applications)

- [Velero 1.16 documentation](https://velero.io/docs/v1.16/)
