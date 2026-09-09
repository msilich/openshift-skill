<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Red Hat provides regular service updates for the components that it manages, including Central services. These service updates include upgrades to new versions of Red Hat Advanced Cluster Security Cloud Service.

You must regularly upgrade the version of RHACS on your secured clusters to ensure compatibility with RHACS Cloud Service.

<a id="prepare-operator-upgrades_upgrade-cloudsvc-operator"></a>

# Preparing to upgrade

Before you upgrade the Red Hat Advanced Cluster Security for Kubernetes (RHACS) version, complete the following steps:

- If the cluster you are upgrading has the `SecuredCluster` custom resource (CR), change the collection method to `CORE_BPF`. For more information, see "Changing the collection method".

<a id="change-collection-method_upgrade-cloudsvc-operator"></a>

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

</div>

<a id="rollback-operator-upgrade-cloud_upgrade-cloudsvc-operator"></a>

# Rolling back an Operator upgrade for secured clusters

To roll back an Operator upgrade, you can use either the CLI or the OpenShift Container Platform web console.

> [!NOTE]
> On secured clusters, you only need to roll back Operator upgrades in rare cases, for example, if an issue exists with the secured cluster.

<a id="rollback-operator-upgrades_upgrade-cloudsvc-operator"></a>

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

2.  Install the latest version of the Operator on the rolled back channel.

</div>

<a id="rollback-operator-upgrades-console_upgrade-cloudsvc-operator"></a>

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

    1.  Click the overflow menu ![kebab](../../images/kebab.png) → **Uninstall Operator**.

        The uninstall Operator dialog is displayed.

    2.  Ensure that the **Delete all operand instances for this operator** checkbox is clear to avoid uninstallation of Red Hat Advanced Cluster Security for Kubernetes (RHACS).

    3.  Click **Uninstall**.

4.  Install the latest version of the Operator on the rolled back channel.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Operator Lifecycle Manager workflow](https://access.redhat.com/documentation/en-us/openshift_container_platform/4.16/html/operators/understanding-operators#olm-workflow)

- [Manually approving a pending Operator update](https://access.redhat.com/documentation/en-us/openshift_container_platform/4.16/html/operators/administrator-tasks#olm-approving-pending-upgrade_olm-upgrading-operators)

</div>

<a id="operator-upgrade-troubleshooting_upgrade-cloudsvc-operator"></a>

# Troubleshooting operator upgrade issues

Follow these instructions to investigate and resolve upgrade-related issues for the RHACS Operator.

<a id="operator-upgrade-fail-to-deploy_upgrade-cloudsvc-operator"></a>

## Central or Secured cluster fails to deploy

When RHACS Operator has the following conditions, you must check the custom resource conditions to find the issue:

- If the Operator fails to deploy Secured Cluster

- If the Operator fails to apply CR changes to actual resources

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
