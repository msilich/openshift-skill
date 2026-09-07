<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Collect cluster data, logs, and update history to help Red Hat Support diagnose and troubleshoot failed cluster updates.

# Gathering log data for a support case

Use the `oc adm must-gather` command to collect cluster data and logs. Red Hat Support can then use the data and logs to diagnose and resolve support cases.

# Changing CVO log level (Technology Preview)

> [!IMPORTANT]
> Changing the CVO log level is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.
>
> For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

Adjust the verbosity of the Cluster Version Operator (CVO) log to troubleshoot update issues or diagnose errors by using four available log levels.

The following list outlines the four log levels:

- `Normal` - The default log level. Contains working log information. Used when everything is fine. Provides helpful notices for auditing or common operations.

- `Debug` - Used when something goes wrong. Expect a higher quantity of notices.

- `Trace` - Used to diagnose errors.

- `TraceAll` - Used to get the complete body content of the logs.

> [!NOTE]
> If `TraceAll` is turned on in a production cluster it may cause widespread performance issues and large log files.

<div>

<div class="title">

Prerequisites

</div>

- You have access to the cluster as a user with the `cluster-admin` role.

- You have installed the OpenShift CLI (`oc`).

- You have the `TechPreviewNoUpgrade` feature set enabled.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Enter the following command into the CLI to change the log level:

    ``` terminal
    $ oc patch clusterversionoperator/cluster --type=merge --patch '{"spec":{"operatorLogLevel":"<log_level>"}}'
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    clusterversionoperator.operator.openshift.io/cluster patched
    ```

    </div>

</div>

# Gathering ClusterVersion history

The Cluster Version Operator (CVO) records updates made to a cluster, known as the ClusterVersion history. The entries can reveal correlation between changes in cluster behavior with potential triggers, although correlation does not imply causation.

> [!NOTE]
> The initial, minor, and z-stream version updates are stored by the ClusterVersion history. However, the ClusterVersion history has a size limit. If the limit is reached, the oldest z-stream updates in previous minor versions are pruned to accommodate the limit.

You can view the ClusterVersion history by using the OpenShift Container Platform web console or by using the OpenShift CLI (`oc`).

## Gathering ClusterVersion history in the OpenShift Container Platform web console

You can view the ClusterVersion history and status information in the OpenShift Container Platform web console. Use the history to verify successful updates and to troubleshoot failures.

<div>

<div class="title">

Prerequisites

</div>

- You have access to the cluster as a user with the `cluster-admin` role.

- You have access to the OpenShift Container Platform web console.

</div>

<div>

<div class="title">

Procedure

</div>

- From the web console, click **Administration** → **Cluster Settings** and review the contents of the **Details** tab.

</div>

## Gathering ClusterVersion history using the OpenShift CLI (`oc`)

Use the OpenShift CLI (`oc`) to view ClusterVersion history. You can use the history to troubleshoot update issues or to verify completed updates.

<div>

<div class="title">

Prerequisites

</div>

- You have access to the cluster as a user with the `cluster-admin` role.

- You have installed the OpenShift CLI (`oc`).

</div>

<div>

<div class="title">

Procedure

</div>

1.  View the cluster update history by entering the following command:

    ``` terminal
    $ oc describe clusterversions/version
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
      Desired:
        Channels:
          candidate-4.13
          candidate-4.14
          fast-4.13
          fast-4.14
          stable-4.13
        Image:    quay.io/openshift-release-dev/ocp-release@sha256:a148b19231e4634196717c3597001b7d0af91bf3a887c03c444f59d9582864f4
        URL:      https://access.redhat.com/errata/RHSA-2023:6130
        Version:  4.13.19
      History:
        Completion Time:    2023-11-07T20:26:04Z
        Image:              quay.io/openshift-release-dev/ocp-release@sha256:a148b19231e4634196717c3597001b7d0af91bf3a887c03c444f59d9582864f4
        Started Time:       2023-11-07T19:11:36Z
        State:              Completed
        Verified:           true
        Version:            4.13.19
        Completion Time:    2023-10-04T18:53:29Z
        Image:              quay.io/openshift-release-dev/ocp-release@sha256:eac141144d2ecd6cf27d24efe9209358ba516da22becc5f0abc199d25a9cfcec
        Started Time:       2023-10-04T17:26:31Z
        State:              Completed
        Verified:           true
        Version:            4.13.13
        Completion Time:    2023-09-26T14:21:43Z
        Image:              quay.io/openshift-release-dev/ocp-release@sha256:371328736411972e9640a9b24a07be0af16880863e1c1ab8b013f9984b4ef727
        Started Time:       2023-09-26T14:02:33Z
        State:              Completed
        Verified:           false
        Version:            4.13.12
      Observed Generation:  4
      Version Hash:         CMLl3sLq-EA=
    Events:                 <none>
    ```

    </div>

</div>

<div id="additional-resources_gathering-cluster-data">

<div class="title">

Additional resources

</div>

- [Gathering data about your cluster for Red Hat Support](../../support/gathering-cluster-data.md#support_gathering_data_gathering-cluster-data)

</div>
