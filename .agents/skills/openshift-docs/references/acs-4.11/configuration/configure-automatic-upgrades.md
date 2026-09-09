<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

If you installed Red Hat Advanced Cluster Security for Kubernetes by using the manifest installation method, also known as the *\`roxctl\` CLI method* or the *legacy installation method*, you can automate the upgrade process for each secured cluster. You can also view the upgrade status from the RHACS portal.

> [!NOTE]
> Automatic upgrades are only available for RHACS systems that you installed by using the manifest installation method. If you installed RHACS by using the Operator, Operator Lifecycle Manager (OLM) controls upgrades. If you installed RHACS by using Helm charts, you must use Helm to upgrade.

<a id="automatic-upgrades-overview_configure-automatic-upgrades"></a>

# Automatic upgrades overview

Automatic upgrades make it easier to stay up-to-date by automating the manual task of upgrading each secured cluster. The new **Clusters** view provides visibility into upgrade status across all secured clusters.

Automatic upgrades make it easier to stay up-to-date by automating the manual task of upgrading each secured cluster. If you enable automatic upgrades and configure the secured cluster for receiving automated upgrades, the upgrader upgrades the entire secured cluster to the same version as Central.

The new **Clusters** view displays information about all your secured clusters, the Sensor version for every cluster, and upgrade status messages. You can also use this view to selectively upgrade your secured clusters or change their configuration.

<div class="note">

<div class="title">

</div>

- By default, the automatic upgrade feature is enabled.

- If you are using a private image registry, you must first push the Sensor and Collector images to your private registry.

- The Sensor must run with the default RBAC permissions.

- Automatic upgrades do not preserve any patches that you have made to any RHACS services running in your cluster. However, it preserves all labels and annotations that you have added to any RHACS object.

- By default, Red Hat Advanced Cluster Security for Kubernetes creates a service account called `sensor-upgrader` in each secured cluster. This account is highly privileged but is only used during upgrades. If you remove this account, Sensor does not have enough permissions, and you must complete future upgrades manually.

</div>

<a id="enable-automatic-upgrades_configure-automatic-upgrades"></a>

# Enabling automatic upgrades for manifest-installed secured clusters

You can enable automatic upgrades for all secured clusters that you installed by using the manifest installation method, also known as the `roxctl` CLI method. This feature automatically upgrades Sensor, Admission Controller, Collector, and Compliance in all secured clusters to the same version as Central.

<div>

<div class="title">

Procedure

</div>

1.  In the RHACS portal, go to **Platform Configuration** → **Clusters**.

2.  Turn on the **Automatically upgrade secured clusters** toggle.

    > [!NOTE]
    > For new installations, the **Automatically upgrade secured clusters** toggle is enabled by default.

</div>

<a id="disable-automatic-upgrades_configure-automatic-upgrades"></a>

# Disabling automatic upgrades of manifest-installed secured clusters

If you want to manage your secured cluster upgrades manually, you can disable automatic upgrades.

<div>

<div class="title">

Procedure

</div>

1.  In the RHACS portal, go to **Platform Configuration** → **Clusters**.

2.  Turn off the **Automatically upgrade secured clusters** toggle.

    > [!NOTE]
    > For new installations, the **Automatically upgrade secured clusters** toggle is enabled by default.

</div>

<a id="automatic-upgrade-status_configure-automatic-upgrades"></a>

# Automatic upgrade status

The **Clusters** view lists all clusters and their upgrade statuses.

| Upgrade status | Description |
|----|----|
| Up to date with Central | The secured cluster is running the same version as Central. |
| Upgrade available | A new version is available for the Sensor and Collector. |
| Upgrade failed. Retry upgrade. | The earlier automatic upgrade failed. |
| Secured cluster version is not managed by RHACS. | External tools such as Helm or the Operator control the secured cluster version. You can upgrade the secured cluster using external tools. |
| Pre-flight checks complete | The upgrade is in progress. Before performing automatic upgrade, the upgrade installation program runs a pre-flight check. During the pre-flight check, the installation program verifies if certain conditions satisfy and then only starts the upgrade process. |
| Not applicable | RHACS cannot communicate with the cluster. |

<a id="automatic-upgrade-failure_configure-automatic-upgrades"></a>

# Automatic upgrade failure for manifest-installed secured clusters

Sometimes, RHACS automatic upgrades might fail to install. When an upgrade fails, the status message for the secured cluster changes to `Upgrade failed. Retry upgrade`. To view more information about the failure and understand why the upgrade failed, you can check the secured cluster row in the **Clusters** view. For more information, see "Troubleshooting the cluster upgrader".

Some common reasons for the failure are:

- The sensor-upgrader deployment might not have run because of a missing or a non-schedulable image.

- The pre-flight checks might have failed, either because of insufficient RBAC permissions or because the cluster state is not recognizable. This can happen if you have edited Red Hat Advanced Cluster Security for Kubernetes service configurations or the `auto-upgrade.stackrox.io/component` label is missing.

- There might be errors in executing the upgrade. If this happens, the upgrade installer automatically attempts to roll back the upgrade.

> [!NOTE]
> Sometimes, the rollback can also fail. For these cases, view the cluster logs to identify the issue or contact support. For more information, see "Troubleshooting the cluster upgrader".

After you identify and fix the root cause for the upgrade failure, you can use the **Retry Upgrade** option to upgrade your secured cluster.

<div>

<div class="title">

Additional resources

</div>

- [Troubleshooting the cluster upgrader](../upgrading/upgrade-roxctl.md#troubleshooting-upgrader_upgrade-roxctl)

</div>

<a id="manual-upgrade-secured-clusters_configure-automatic-upgrades"></a>

# Upgrading secured clusters manually from the RHACS portal

If you do not want to enable automatic upgrades, you can manage your secured cluster upgrades by using the **Clusters** view.

To manually trigger upgrades for your secured clusters:

<div>

<div class="title">

Procedure

</div>

1.  In the RHACS portal, go to **Platform Configuration** → **Clusters**.

2.  Take one of the following actions:

    - To upgrade a single cluster, select the **Upgrade available** option under the **Sensor Upgrade** column for the cluster you want to upgrade.

    - To upgrade many clusters at a time, select the checkboxes next to the **Name** column for the clusters you want to update, and then click **Upgrade**.

</div>
