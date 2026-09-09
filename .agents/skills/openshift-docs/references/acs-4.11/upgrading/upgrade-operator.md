<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Upgrades through the Red Hat Advanced Cluster Security for Kubernetes (RHACS) Operator are performed automatically by the Operator or manually by you, depending on the **Update approval** option you chose at installation.

> [!IMPORTANT]
> In RHACS 4.11, all container image names changed from the `-rhel8` suffix to `-rhel9` as part of the migration to UBI 9 Minimal base images. For example, `rhacs-main-rhel8` is now `rhacs-main-rhel9`.
>
> If you use image mirrors, allowlists, or firewall rules that reference specific RHACS image names, you must update them to use the new `-rhel9` names before upgrading.

<div>

<div class="title">

Additional resources

</div>

- [Image versions](../configuration/enable-offline-mode.md#image-versions_enable-offline-mode)

</div>

<a id="prepare-operator-upgrades_upgrade-operator"></a>

# Preparing to upgrade

Before you upgrade the Red Hat Advanced Cluster Security for Kubernetes (RHACS) version, complete the following steps:

- If you are upgrading from version 3.74, verify that you are running the latest patch release version of the RHACS Operator 3.74.

- Backup your existing Central database.

- If the cluster you are upgrading has the `SecuredCluster` custom resource (CR), change the collection method to `CORE_BPF`. For more information, see "Changing the collection method".

<a id="change-collection-method_upgrade-operator"></a>

## Changing the collection method

If the cluster that you are upgrading has the `SecuredCluster` CR, you must set the per node collection setting to `CORE_BPF` before you upgrade.

<div>

<div class="title">

Procedure

</div>

1.  In the OpenShift Container Platform web console, go to the RHACS Operator page.

2.  In the top navigation menu, select **Secured Cluster**.

3.  Click the instance name, for example, **stackrox-secured-cluster-services**.

4.  Use one of the following methods to change the setting:

    - In the **Form view**, under **Per Node Settings** → **Collector Settings** → **Collection**, select **CORE_BPF**.

    - Click **YAML** to open the YAML editor and locate the `spec.perNode.collector.collection` attribute. If the value is `KernelModule` or `EBPF`, then change it to `CORE_BPF`.

5.  Click **Save**.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Updating installed Operators](https://docs.openshift.com/container-platform/latest/operators/admin/olm-upgrading-operators.html)

- [Backing up Red Hat Advanced Cluster Security for Kubernetes](../backup_and_restore/backing-up-acs.md)

</div>

<a id="operator-upgrade-modify-central-custom-resource_upgrade-operator"></a>

# Modifying the Central custom resource

The Central DB service requires persistent storage. If you have not configured a default storage class for the Central cluster that is an SSD or is high performance, you must reinstall RHACS. Then, configure the `Central` custom resource (CR) with the storage class for the Central DB persistent volume claim (PVC).

When changing the `storageClassName`, because of limitations with the Kubernetes storage layer, you cannot change a claim’s storage class after Kubernetes binds it; therefore, you must re-create the Central CR.

> [!NOTE]
> Skip this procedure if you have already configured a default storage class for Central.

<div>

<div class="title">

Procedure

</div>

1.  Back up and uninstall the Central instance.

2.  Reinstall RHACS and configure the Central custom resource as shown in the following example:

    ``` terminal
    spec:
      central:
        db:
          isEnabled: Default
          persistence:
            persistentVolumeClaim:
              claimName: central-db
              size: 100Gi
              storageClassName: <storage_class_name>
    ```

    where:

    `spec.central.db.isEnabled`  
    Specifies that the database is enabled. Do not change this value from `IsEnabled` to `Enabled`.

    `spec.central.db.persistence.persistentVolumeClaim`  
    Specifies that your cluster uses the existing claim; otherwise, it creates a new claim.

3.  Restore the Central database backup by using the `roxctl` CLI.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Backing up Red Hat Advanced Cluster Security for Kubernetes](../backup_and_restore/backing-up-acs.md)

- [Restoring from a backup](../backup_and_restore/restore-acs.md)

</div>

<a id="operator-upgrade-modify-central-custom-resource-external-db_upgrade-operator"></a>

# Modifying Central custom resource for external database

You can configure the Central custom resource (CR) to use an external PostgreSQL database instead of the default embedded database.

<div>

<div class="title">

Prerequisites

</div>

- You must have a database in your database instance that supports PostgreSQL 13 or 15 and a user with the following permissions:

  - Connection rights to the database.

  - `Usage` and `Create` on the schema.

  - `Select`, `Insert`, `Update`, and `Delete` on all tables in the schema.

  - `Usage` on all sequences in the schema.

    <div class="important">

    <div class="title">

    </div>

    - Postgres 15 is the recommended and supported version. Red Hat has deprecated the support for Postgres 13 and will remove it in the newer versions of RHACS.

    - If you use Kubernetes, enter `kubectl` instead of `oc`.

    </div>

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create a password secret in the deployed namespace by using the OpenShift Container Platform web console or the terminal.

    - On the OpenShift Container Platform web console, go to the **Workloads** → **Secrets** page. Create a **Key/Value secret** with the key `password` and the value as the path of a plain text file containing the password for the superuser of the provisioned database.

    - Or, run the following command in your terminal:

      ``` terminal
      $ oc create secret generic external-db-password \
        --from-file=password=<password.txt>
      ```

      where:

      `<password.txt>`  
      Specifies the path of the file that has the plain text password.

2.  Go to the Red Hat Advanced Cluster Security for Kubernetes operator page in the OpenShift Container Platform web console. Select **Central** in the top navigation bar and select the instance you want to connect to the database.

3.  Go to the **YAML editor** view.

4.  For **`db.passwordSecret.name`** specify the referenced secret that you created in earlier steps. For example, `external-db-password`.

5.  For **`db.connectionString`** specify the connection string in `keyword=value` format, for example, `host=<host> port=5432 database=stackrox user=stackrox sslmode=verify-ca`

6.  For **`db.persistence`** delete the entire block.

7.  If necessary, you can specify a Certificate Authority for Central to trust the database certificate by adding a TLS block under the top-level spec, as shown in the following example:

    - Update the central custom resource with the following configuration:

      ``` terminal
      spec:
        tls:
          additionalCAs:
          - name: db-ca
            content: |
              <certificate>
        central:
          db:
            isEnabled: Default
            connectionString: "host=<host> port=5432 user=<user> sslmode=verify-ca"
            passwordSecret:
              name: external-db-password
      ```

      where:

      `spec.central.db.isEnabled`  
      Specifies that you must not change the value of `IsEnabled` to `Enabled`.

8.  Click **Save**.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Provisioning a database in your PostgreSQL instance](../installing/installing_ocp/install-central-ocp.md#provision-postgresql-database_install-central-ocp)

</div>

<a id="operator-upgrade-change-subscription-channel_upgrade-operator"></a>

# Changing the subscription channel

You can change the update channel for the RHACS Operator by using the OpenShift Container Platform web console or by using the command line. For upgrading to RHACS 4.0 from RHACS 3.74, you must change the update channel.

<div class="important">

<div class="title">

</div>

- You must change the subscription channel for all clusters where you installed the RHACS Operator, including Central and all secured clusters.

- If you use Kubernetes, enter `kubectl` instead of `oc`.

</div>

<a id="operator-upgrade-change-subscription-channel-console_upgrade-operator"></a>

## Changing the subscription channel by using the web console

You can change the update channel for the RHACS Operator by using the OpenShift Container Platform web console.

<div>

<div class="title">

Prerequisites

</div>

- You must verify that you backed up your Central database.

- You have access to an OpenShift Container Platform cluster web console using an account with `cluster-admin` permissions.

</div>

<div>

<div class="title">

Procedure

</div>

1.  In the **Administrator** perspective of the OpenShift Container Platform web console, go to **Ecosystem** → **Installed Operators**.

2.  Click the RHACS Operator.

3.  Click the **Subscription** tab.

4.  Click the name of the update channel under **Update Channel**.

5.  Select **stable**, then click **Save**.

6.  For subscriptions with an **Automatic** approval strategy, the update begins automatically. Go back to the **Ecosystem** → **Installed Operators** page to monitor the progress of the update. When complete, the status changes to **Succeeded** and **Up to date**.

    For subscriptions with a **Manual** approval strategy, you can manually approve the update from the **Subscription** tab.

</div>

<a id="operator-upgrade-change-subscription-channel-cli_upgrade-operator"></a>

## Changing the subscription channel by using command line

You can change the update channel for the RHACS Operator by using the command-line interface (CLI).

<div>

<div class="title">

Prerequisites

</div>

- You must verify that you backed up your Central database.

- You have access to an OpenShift Container Platform cluster web console using an account with `cluster-admin` permissions.

</div>

<div>

<div class="title">

Procedure

</div>

- Run the following command to change the subscription channel to `stable`:

  ``` terminal
  $ oc -n rhacs-operator \
    patch subscriptions.operators.coreos.com rhacs-operator \
    --type=merge --patch='{ "spec": { "channel": "stable" }}'
  ```

  During the update, the RHACS Operator provisions a new deployment called `central-db` and your data begins migrating. It takes around 30 minutes and happens only after you upgrade.

</div>

<a id="rollback-operator-upgrade_upgrade-operator"></a>

# Rolling back an Operator upgrade

To roll back an Operator upgrade, you must perform the steps described in one of the following sections. You can roll back an Operator upgrade by using the CLI or the OpenShift Container Platform web console.

> [!NOTE]
> If you are rolling back from RHACS 4.8 or newer, you can only roll back to the latest patch release version of RHACS 4.8.

<a id="rollback-operator-upgrades_upgrade-operator"></a>

## Rolling back an Operator upgrade by using the CLI

You can roll back the Operator version by using command-line interface (CLI) commands.

<div>

<div class="title">

Procedure

</div>

1.  Delete the Operator Lifecycle Manager (OLM) subscription and cluster service version (CSV):

    > [!NOTE]
    > If you use Kubernetes, enter `kubectl` instead of `oc`.

    1.  To delete the OLM subscription, run the following command:

        ``` terminal
        $ oc -n rhacs-operator delete subscription rhacs-operator
        ```

        <div class="formalpara">

        <div class="title">

        Example output

        </div>

        ``` terminal
        subscription.operators.coreos.com "rhacs-operator" deleted
        ```

        </div>

    2.  To delete the CSV, run the following command:

        ``` terminal
        $ oc -n rhacs-operator delete csv -l operators.coreos.com/rhacs-operator.rhacs-operator
        ```

        <div class="formalpara">

        <div class="title">

        Example output

        </div>

        ``` terminal
        clusterserviceversion.operators.coreos.com "rhacs-operator.v4.8.4" deleted
        ```

        </div>

2.  Install the earlier version of the RHACS Operator:

    1.  In the OpenShift web console, click **Ecosystem** → **Software Catalog**.

    2.  Search for **Advanced Cluster Security for Kubernetes**.

    3.  Select and install the earlier version of the Operator.

        > [!NOTE]
        > Installing the earlier Operator version rolls back RHACS to the same version as the Operator.

</div>

<a id="rollback-operator-upgrades-console_upgrade-operator"></a>

## Rolling back an Operator upgrade by using the web console

You can roll back the Operator version by using the OpenShift Container Platform web console.

<div>

<div class="title">

Prerequisites

</div>

- You have access to an OpenShift Container Platform cluster web console using an account with `cluster-admin` permissions.

</div>

<div>

<div class="title">

Procedure

</div>

1.  In the OpenShift web console, click **Ecosystem** → **Installed Operators**.

2.  From the list of projects, select **rhacs-operator**.

3.  Locate the **Advanced Cluster Security for Kubernetes** Operator:

    1.  Click the overflow menu ![kebab](../images/kebab.png) → **Uninstall Operator**.

        The uninstall Operator dialog is displayed.

    2.  Ensure that the **Delete all operand instances for this operator** checkbox is clear to avoid uninstallation of Red Hat Advanced Cluster Security for Kubernetes (RHACS).

    3.  Click **Uninstall**.

4.  Install the earlier version of RHACS Operator:

    1.  In the OpenShift web console, click **Ecosystem** → **Installed Operators**.

    2.  Search for **Advanced Cluster Security for Kubernetes**.

    3.  Select and install the earlier version of the Operator.

        > [!NOTE]
        > Installing the earlier Operator version rolls back RHACS to the same version as the Operator.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Installing Central using the Operator method](../installing/installing_ocp/install-central-ocp.md#install-central-operator_install-central-ocp)

- [Operator Lifecycle Manager workflow](https://access.redhat.com/documentation/en-us/openshift_container_platform/4.15/html/operators/understanding-operators#olm-workflow)

- [Manually approving a pending Operator update](https://access.redhat.com/documentation/en-us/openshift_container_platform/4.15/html/operators/administrator-tasks#olm-approving-pending-upgrade_olm-upgrading-operators)

</div>

<a id="operator-upgrade-troubleshooting_upgrade-operator"></a>

# Troubleshooting operator upgrade issues

Follow these instructions to investigate and resolve upgrade-related issues for the RHACS Operator.

<a id="operator-upgrade-centraldb-cannot-be-scheduled_upgrade-operator"></a>

## Central DB scheduling failure

Follow the instructions here to troubleshoot a failing Central DB pod during an upgrade:

> [!NOTE]
> If you use Kubernetes, enter `kubectl` instead of `oc`.

<div>

<div class="title">

Procedure

</div>

1.  Check the status of the `central-db` pod:

    ``` terminal
    $ oc -n <namespace_name> get pod -l app=central-db
    ```

2.  If the status of the pod is `Pending`, use the describe command to get more details:

    ``` terminal
    $ oc -n <namespace_name> describe po/<central_db_pod_name>
    ```

    You might see the `FailedScheduling` warning message:

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    Type     Reason            Age   From               Message
    ----     ------            ----  ----               -------
    Warning  FailedScheduling  54s   default-scheduler  0/7 nodes are available: 1 Insufficient memory, 3 node(s) had untolerated taint {node-role.kubernetes.io/master: }, 4 Insufficient cpu. preemption: 0/7 nodes are available: 3 Preemption is not helpful for scheduling, 4 No preemption victims found for incoming pod.
    ```

    </div>

    This warning message suggests that the scheduled node had insufficient memory to accommodate the pod’s resource requirements. If you have a small environment, consider increasing resources on the nodes or adding a larger node that can support the database.

    Otherwise, consider decreasing the resource requirements for the `central-db` pod in the custom resource under `central` → `db` → `resources`. However, running central with fewer resources than the recommended minimum might lead to degraded performance for RHACS.

</div>

<a id="operator-upgrade-fail-to-deploy_upgrade-operator"></a>

## Central or Secured cluster fails to deploy

When RHACS Operator has the following conditions, you must check the custom resource conditions to find the issue:

- If the Operator fails to deploy Central or Secured Cluster

- If the Operator fails to apply CR changes to actual resources

> [!NOTE]
> If you use Kubernetes, enter `kubectl` instead of `oc`.

- For Central, run the following command to check the conditions:

  ``` terminal
  $ oc -n rhacs-operator describe centrals.platform.stackrox.io
  ```

- For Secured clusters, run the following command to check the conditions:

  ``` terminal
  $ oc -n rhacs-operator describe securedclusters.platform.stackrox.io
  ```

  You can identify configuration errors from the conditions output:

  <div class="formalpara">

  <div class="title">

  Example output

  </div>

  ``` terminal
   Conditions:
      Last Transition Time:  2023-04-19T10:49:57Z
      Status:                False
      Type:                  Deployed
      Last Transition Time:  2023-04-19T10:49:57Z
      Status:                True
      Type:                  Initialized
      Last Transition Time:  2023-04-19T10:59:10Z
      Message:               Deployment.apps "central" is invalid: spec.template.spec.containers[0].resources.requests: Invalid value: "50": must be less than or equal to cpu limit
      Reason:                ReconcileError
      Status:                True
      Type:                  Irreconcilable
      Last Transition Time:  2023-04-19T10:49:57Z
      Message:               No proxy configuration is desired
      Reason:                NoProxyConfig
      Status:                False
      Type:                  ProxyConfigFailed
      Last Transition Time:  2023-04-19T10:49:57Z
      Message:               Deployment.apps "central" is invalid: spec.template.spec.containers[0].resources.requests: Invalid value: "50": must be less than or equal to cpu limit
      Reason:                InstallError
      Status:                True
      Type:                  ReleaseFailed
  ```

  </div>

  Additionally, you can view RHACS pod logs to find more information about the issue. Run the following command to view the logs:

  ``` terminal
  $ oc -n rhacs-operator logs deploy/rhacs-operator-controller-manager manager
  ```
