<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

You can upgrade the Migration Toolkit for Containers (MTC) on OpenShift Container Platform 4.17 by using Operator Lifecycle Manager.

You can upgrade MTC on OpenShift Container Platform 4.5, and earlier versions, by reinstalling the legacy Migration Toolkit for Containers Operator.

> [!IMPORTANT]
> If you are upgrading from MTC version 1.3, you must perform an additional procedure to update the `MigPlan` custom resource (CR).

# Upgrading the Migration Toolkit for Containers on OpenShift Container Platform 4.17

You can upgrade the Migration Toolkit for Containers (MTC) on OpenShift Container Platform 4.17 by using the Operator Lifecycle Manager.

> [!IMPORTANT]
> When upgrading the MTC by using the Operator Lifecycle Manager, you must use a supported migration path.

<div>

<div class="title">

Migration paths

</div>

- Migrating from OpenShift Container Platform 3 to OpenShift Container Platform 4 requires a legacy MTC Operator and MTC 1.7.x.

- Migrating from MTC 1.7.x to MTC 1.8.x is not supported.

- You must use MTC 1.7.x to migrate anything with a source of OpenShift Container Platform 4.9 or earlier.

  - MTC 1.7.x must be used on both source and destination.

- MTC 1.8.x only supports migrations from OpenShift Container Platform 4.10 or later to OpenShift Container Platform 4.10 or later. For migrations only involving cluster versions 4.10 and later, either 1.7.x or 1.8.x may be used. However, it must be the same MTC version on both source & destination.

  - Migration from source MTC 1.7.x to destination MTC 1.8.x is unsupported.

  - Migration from source MTC 1.8.x to destination MTC 1.7.x is unsupported.

  - Migration from source MTC 1.7.x to destination MTC 1.7.x is supported.

  - Migration from source MTC 1.8.x to destination MTC 1.8.x is supported

</div>

<div>

<div class="title">

Prerequisites

</div>

- You must be logged in as a user with `cluster-admin` privileges.

</div>

<div>

<div class="title">

Procedure

</div>

1.  In the OpenShift Container Platform console, navigate to **Ecosystem** → **Installed Operators**.

    Operators that have a pending upgrade display an **Upgrade available** status.

2.  Click **Migration Toolkit for Containers Operator**.

3.  Click the **Subscription** tab. Any upgrades requiring approval are displayed next to **Upgrade Status**. For example, it might display **1 requires approval**.

4.  Click **1 requires approval**, then click **Preview Install Plan**.

5.  Review the resources that are listed as available for upgrade and click **Approve**.

6.  Navigate back to the **Ecosystem** → **Installed Operators** page to monitor the progress of the upgrade. When complete, the status changes to **Succeeded** and **Up to date**.

7.  Click **Workloads** → **Pods** to verify that the MTC pods are running.

</div>

# Upgrading the Migration Toolkit for Containers to 1.8.0

To upgrade the Migration Toolkit for Containers to 1.8.0, complete the following steps.

<div>

<div class="title">

Procedure

</div>

1.  Determine subscription names and current channels to work with for upgrading by using one of the following methods:

    - Determine the subscription names and channels by running the following command:

      ``` terminal
      $ oc -n openshift-migration get sub
      ```

      <div class="formalpara">

      <div class="title">

      Example output

      </div>

      ``` terminal
      NAME                                                                         PACKAGE                SOURCE                 CHANNEL
      mtc-operator                                                                 mtc-operator           mtc-operator-catalog   release-v1.7
      redhat-oadp-operator-stable-1.0-mtc-operator-catalog-openshift-marketplace   redhat-oadp-operator   mtc-operator-catalog   stable-1.0
      ```

      </div>

    - Or return the subscription names and channels in JSON by running the following command:

      ``` terminal
      $ oc -n openshift-migration get sub -o json | jq -r '.items[] | { name: .metadata.name, package: .spec.name, channel: .spec.channel }'
      ```

      <div class="formalpara">

      <div class="title">

      Example output

      </div>

      ``` terminal
      {
        "name": "mtc-operator",
        "package": "mtc-operator",
        "channel": "release-v1.7"
      }
      {
        "name": "redhat-oadp-operator-stable-1.0-mtc-operator-catalog-openshift-marketplace",
        "package": "redhat-oadp-operator",
        "channel": "stable-1.0"
      }
      ```

      </div>

2.  For each subscription, patch to move from the MTC 1.7 channel to the MTC 1.8 channel by running the following command:

    ``` terminal
    $ oc -n openshift-migration patch subscription mtc-operator --type merge --patch '{"spec": {"channel": "release-v1.8"}}'
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    subscription.operators.coreos.com/mtc-operator patched
    ```

    </div>

</div>

## Upgrading OADP 1.0 to 1.2 for Migration Toolkit for Containers 1.8.0

To upgrade OADP 1.0 to 1.2 for Migration Toolkit for Containers 1.8.0, complete the following steps.

<div>

<div class="title">

Procedure

</div>

- For each subscription, patch the OADP operator from OADP 1.0 to OADP 1.2 by running the following command:

  ``` terminal
  $ oc -n openshift-migration patch subscription redhat-oadp-operator-stable-1.0-mtc-operator-catalog-openshift-marketplace --type merge --patch '{"spec": {"channel":"stable-1.2"}}'
  ```

  > [!NOTE]
  > Sections indicating the user-specific returned `NAME` values that are used for the installation of MTC & OADP, respectively.

  <div class="formalpara">

  <div class="title">

  Example output

  </div>

  ``` terminal
  subscription.operators.coreos.com/redhat-oadp-operator-stable-1.0-mtc-operator-catalog-openshift-marketplace patched
  ```

  </div>

  > [!NOTE]
  > The returned value will be similar to `redhat-oadp-operator-stable-1.0-mtc-operator-catalog-openshift-marketplace`, which is used in this example.

  - If the `installPlanApproval` parameter is set to `Automatic`, the Operator Lifecycle Manager (OLM) begins the upgrade process.

  - If the `installPlanApproval` parameter is set to `Manual`, you must approve each `installPlan` before the OLM begins the upgrades.

</div>

<div>

<div class="title">

Verification

</div>

1.  Verify that the OLM has completed the upgrades of OADP and MTC by running the following command:

    ``` terminal
    $ oc -n openshift-migration get subscriptions.operators.coreos.com mtc-operator -o json | jq '.status | (."state"=="AtLatestKnown")'
    ```

2.  When a value of `true` is returned, verify the channel used for each subscription by running the following command:

    ``` terminal
    $ oc -n openshift-migration get sub -o json | jq -r '.items[] | {name: .metadata.name, channel: .spec.channel }'
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    {
      "name": "mtc-operator",
      "channel": "release-v1.8"
    }
    {
      "name": "redhat-oadp-operator-stable-1.0-mtc-operator-catalog-openshift-marketplace",
      "channel": "stable-1.2"
    }
    ```

    </div>

        Confirm that the `mtc-operator.v1.8.0` and `oadp-operator.v1.2.x` packages are installed by running the following command:

    ``` terminal
    $ oc -n openshift-migration get csv
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    NAME                     DISPLAY                                     VERSION   REPLACES                 PHASE
    mtc-operator.v1.8.0      Migration Toolkit for Containers Operator   1.8.0     mtc-operator.v1.7.13     Succeeded
    oadp-operator.v1.2.2     OADP Operator                               1.2.2     oadp-operator.v1.0.13    Succeeded
    ```

    </div>

</div>

# Upgrading the Migration Toolkit for Containers on OpenShift Container Platform versions 4.2 to 4.5

You can upgrade Migration Toolkit for Containers (MTC) on OpenShift Container Platform versions 4.2 to 4.5 by manually installing the legacy Migration Toolkit for Containers Operator.

<div>

<div class="title">

Prerequisites

</div>

- You must be logged in as a user with `cluster-admin` privileges.

- You must have access to `registry.redhat.io`.

- You must have `podman` installed.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Log in to `registry.redhat.io` with your Red Hat Customer Portal credentials by entering the following command:

    ``` terminal
    $ podman login registry.redhat.io
    ```

2.  Download the `operator.yml` file by entering the following command:

    ``` terminal
    $ podman cp $(podman create registry.redhat.io/rhmtc/openshift-migration-legacy-rhel8-operator:v1.7:/operator.yml ./
    ```

3.  Replace the Migration Toolkit for Containers Operator by entering the following command:

    ``` terminal
    $ oc replace --force -f operator.yml
    ```

4.  Scale the `migration-operator` deployment to `0` to stop the deployment by entering the following command:

    ``` terminal
    $ oc scale -n openshift-migration --replicas=0 deployment/migration-operator
    ```

5.  Scale the `migration-operator` deployment to `1` to start the deployment and apply the changes by entering the following command:

    ``` terminal
    $ oc scale -n openshift-migration --replicas=1 deployment/migration-operator
    ```

6.  Verify that the `migration-operator` was upgraded by entering the following command:

    ``` terminal
    $ oc -o yaml -n openshift-migration get deployment/migration-operator | grep image: | awk -F ":" '{ print $NF }'
    ```

7.  Download the `controller.yml` file by entering the following command:

    ``` terminal
    $ podman cp $(podman create registry.redhat.io/rhmtc/openshift-migration-legacy-rhel8-operator:v1.7):/operator.yml ./
    ```

8.  Create the `migration-controller` object by entering the following command:

    ``` terminal
    $ oc create -f controller.yml
    ```

9.  Verify that the MTC pods are running by entering the following command:

    ``` terminal
    $ oc get pods -n openshift-migration
    ```

</div>

# Upgrading MTC 1.3 to 1.8

If you are upgrading Migration Toolkit for Containers (MTC) version 1.3.x to 1.8, you must update the `MigPlan` custom resource (CR) manifest on the cluster on which the `MigrationController` pod is running.

Because the `indirectImageMigration` and `indirectVolumeMigration` parameters do not exist in MTC 1.3, their default value in version 1.4 is `false`, which means that direct image migration and direct volume migration are enabled. Because the direct migration requirements are not fulfilled, the migration plan cannot reach a `Ready` state unless these parameter values are changed to `true`.

<div class="important">

<div class="title">

</div>

- Migrating from OpenShift Container Platform 3 to OpenShift Container Platform 4 requires a legacy MTC Operator and MTC 1.7.x.

- Upgrading MTC 1.7.x to 1.8.x requires manually updating the OADP channel from `stable-1.0` to `stable-1.2` in order to successfully complete the upgrade from 1.7.x to 1.8.x.

</div>

<div>

<div class="title">

Prerequisites

</div>

- You must be logged in as a user with `cluster-admin` privileges.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Log in to the cluster on which the `MigrationController` pod is running.

2.  Get the `MigPlan` CR manifest:

    ``` terminal
    $ oc get migplan <migplan> -o yaml -n openshift-migration
    ```

3.  Update the following parameter values and save the file as `migplan.yaml`:

    ``` yaml
    ...
    spec:
      indirectImageMigration: true
      indirectVolumeMigration: true
    ```

4.  Replace the `MigPlan` CR manifest to apply the changes:

    ``` terminal
    $ oc replace -f migplan.yaml -n openshift-migration
    ```

5.  Get the updated `MigPlan` CR manifest to verify the changes:

    ``` terminal
    $ oc get migplan <migplan> -o yaml -n openshift-migration
    ```

</div>
