<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Use the OADP CLI plugin for all backup and restore operations, including viewing logs and descriptions. You do not need to download the `velero` CLI tool to debug `Backup` and `Restore` custom resources (CRs) or troubleshoot failed operations.

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

## OADP-Velero-OpenShift Container Platform version relationship

Review the version relationship between OADP, Velero, and OpenShift Container Platform to decide compatible version combinations. This helps you select the appropriate OADP version for your cluster environment.

| OADP version | Velero version | OpenShift Container Platform version |
|--------------|----------------|--------------------------------------|
| 1.3.0        | 1.12           | 4.12-4.15                            |
| 1.3.1        | 1.12           | 4.12-4.15                            |
| 1.3.2        | 1.12           | 4.12-4.15                            |
| 1.3.3        | 1.12           | 4.12-4.15                            |
| 1.3.4        | 1.12           | 4.12-4.15                            |
| 1.3.5        | 1.12           | 4.12-4.15                            |
| 1.4.0        | 1.14           | 4.14-4.18                            |
| 1.4.1        | 1.14           | 4.14-4.18                            |
| 1.4.2        | 1.14           | 4.14-4.18                            |
| 1.4.3        | 1.14           | 4.14-4.18                            |
| 1.5.0        | 1.16           | 4.19                                 |

### Additional resources

- [Velero 1.12 documentation](https://velero.io/docs/v1.12/)

- [Velero 1.14 documentation](https://velero.io/docs/v1.14/)

- [Velero 1.16 documentation](https://velero.io/docs/v1.16/)

# Debugging Velero resources with the OpenShift CLI tool

Debug a failed backup or restore by checking Velero custom resources (CRs) and the `Velero` pod log with the OpenShift CLI tool.

<div>

<div class="title">

Procedure

</div>

- Retrieve a summary of warnings and errors associated with a `Backup` or `Restore` CR by using the following `oc describe` command:

  ``` terminal
  $ oc describe <velero_cr> <cr_name>
  ```

- Retrieve the `Velero` pod logs by using the following `oc logs` command:

  ``` terminal
  $ oc logs pod/<velero>
  ```

- Specify the Velero log level in the `DataProtectionApplication` resource as shown in the following example.

  > [!NOTE]
  > This option is available starting from OADP 1.0.3.

  ``` yaml
  apiVersion: oadp.openshift.io/v1alpha1
  kind: DataProtectionApplication
  metadata:
    name: velero-sample
  spec:
    configuration:
      velero:
        logLevel: warning
  ```

  The following `logLevel` values are available:

  - `trace`

  - `debug`

  - `info`

  - `warning`

  - `error`

  - `fatal`

  - `panic`

    Use the `info` `logLevel` value for most logs.

</div>

# Debugging backups and restores using the OADP CLI

Use the OADP CLI plugin to retrieve logs and descriptions of backup and restore custom resources (CRs). Use the following information to interpret the output.

To retrieve backup and restore information, use the following OADP CLI plugin commands:

- `oc oadp backup describe <backup_name> --details`

- `oc oadp backup logs <backup_name>`

- `oc oadp restore describe <restore_name> --details`

- `oc oadp restore logs <restore_name>`

The following types of errors and warnings appear in describe output:

- `Velero`: Messages related to the operation of Velero itself, for example, connecting to the cloud or reading a backup file.

- `Cluster`: Messages related to backing up or restoring cluster-scoped resources.

- `Namespaces`: Messages related to backing up or restoring resources stored in namespaces.

One or more errors in one of these categories results in a `Restore` operation receiving the status of `PartiallyFailed` and not `Completed`. Warnings do not lead to a change in the completion status.

Consider the following points when you encounter restore errors:

- For resource-specific errors (`Cluster` and `Namespaces`), the `restore describe --details` output includes a resource list of all resources that Velero attempted to restore. For any resource that has such an error, check whether the resource exists in the cluster.

- If there are `Velero` errors but no resource-specific errors, it is possible that the restore completed without problems restoring workloads. In this case, carefully validate post-restore applications.

  For example, if the output contains `PodVolumeRestore` or node agent-related errors, check the status of `PodVolumeRestores` and `DataDownloads`. If none of these are failed or still running, volume data might have been fully restored.
