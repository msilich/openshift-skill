<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Download the `velero` CLI tool or access the `velero` binary in your cluster to debug `Backup` and `Restore` custom resources (CRs) and retrieve logs. This helps you to troubleshoot failed backup and restore operations.

# Downloading the Velero CLI tool

Download and install the `velero` CLI tool from the Velero documentation page, which provides instructions for macOS by using Homebrew, GitHub, and Windows by using Chocolatey. This helps you to access the `velero` CLI for debugging backup and restore operations.

<div>

<div class="title">

Prerequisites

</div>

- You have access to a Kubernetes cluster, v1.16 or later, with DNS and container networking enabled.

- You have installed `kubectl` locally.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Open a browser and navigate to ["Install the CLI" on the Velero website](https://velero.io/docs/v1.16/basic-install/#install-the-cli).

2.  Follow the appropriate procedure for macOS, GitHub, or Windows.

3.  Download the Velero version appropriate for your version of OADP and OpenShift Container Platform.

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

# Accessing the Velero binary in the Velero deployment in the cluster

Use a shell command to access the Velero binary in the Velero deployment in the cluster.

<div>

<div class="title">

Prerequisites

</div>

- Your `DataProtectionApplication` custom resource has a status of `Reconcile complete`.

</div>

<div>

<div class="title">

Procedure

</div>

- Set the needed alias by using the following command:

  ``` terminal
  $ alias velero='oc -n openshift-adp exec deployment/velero -c velero -it -- ./velero'
  ```

</div>

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

# Debugging Velero resources with the Velero CLI tool

Debug `Backup` and `Restore` custom resources (CRs) and retrieve logs with the Velero CLI tool. The Velero CLI tool provides more detailed information than the OpenShift CLI tool.

<div>

<div class="title">

Procedure

</div>

- Use the `oc exec` command to run a Velero CLI command:

  ``` terminal
  $ oc -n openshift-adp exec deployment/velero -c velero -- ./velero \
    <backup_restore_cr> <command> <cr_name>
  ```

  <div class="formalpara">

  <div class="title">

  Example `oc exec` command

  </div>

  ``` terminal
  $ oc -n openshift-adp exec deployment/velero -c velero -- ./velero \
    backup describe 0e44ae00-5dc3-11eb-9ca8-df7e5254778b-2d8ql
  ```

  </div>

- List all Velero CLI commands by using the following `velero --help` option:

  ``` terminal
  $ oc -n openshift-adp exec deployment/velero -c velero -- ./velero \
    --help
  ```

- Retrieve the logs of a `Backup` or `Restore` CR by using the following `velero logs` command:

  ``` terminal
  $ oc -n openshift-adp exec deployment/velero -c velero -- ./velero \
    <backup_restore_cr> logs <cr_name>
  ```

  <div class="formalpara">

  <div class="title">

  Example `velero logs` command

  </div>

  ``` terminal
  $ oc -n openshift-adp exec deployment/velero -c velero -- ./velero \
    restore logs ccc7c2d0-6017-11eb-afab-85d0007f5a19-x4lbf
  ```

  </div>

- Retrieve a summary of warnings and errors associated with a `Backup` or `Restore` CR by using the following `velero describe` command:

  ``` terminal
  $ oc -n openshift-adp exec deployment/velero -c velero -- ./velero \
    <backup_restore_cr> describe <cr_name>
  ```

  <div class="formalpara">

  <div class="title">

  Example `velero describe` command

  </div>

  ``` terminal
  $ oc -n openshift-adp exec deployment/velero -c velero -- ./velero \
    backup describe 0e44ae00-5dc3-11eb-9ca8-df7e5254778b-2d8ql
  ```

  </div>

  The following types of restore errors and warnings are shown in the output of a `velero describe` request:

- `Velero`: A list of messages related to the operation of Velero itself, for example, messages related to connecting to the cloud, reading a backup file, and so on

- `Cluster`: A list of messages related to backing up or restoring cluster-scoped resources

- `Namespaces`: A list of list of messages related to backing up or restoring resources stored in namespaces

  One or more errors in one of these categories results in a `Restore` operation receiving the status of `PartiallyFailed` and not `Completed`. Warnings do not lead to a change in the completion status.

  Consider the following points for these restore errors:

- For resource-specific errors, that is, `Cluster` and `Namespaces` errors, the `restore describe --details` output includes a resource list that includes all resources that Velero restored. For any resource that has such an error, check if the resource is actually in the cluster.

- For resource-specific errors, that is, `Cluster` and `Namespaces` errors, the `restore describe --details` output includes a resource list that includes all resources that Velero restored. For any resource that has such an error, check if the resource is actually in the cluster.

- If there are `Velero` errors but no resource-specific errors in the output of a `describe` command, it is possible that the restore completed without any actual problems in restoring workloads. In this case, carefully validate post-restore applications.

  For example, if the output contains `PodVolumeRestore` or node agent-related errors, check the status of `PodVolumeRestores` and `DataDownloads`. If none of these are failed or still running, then volume data might have been fully restored.

</div>
