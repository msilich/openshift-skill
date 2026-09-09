<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

You can configure a retention period for Red Hat Advanced Cluster Security for Kubernetes alerts to automatically delete older alerts and save storage costs.

<a id="alert-data-retention-overview_enable-alert-data-retention"></a>

# Alert data retention overview

You can configure a retention period for Red Hat Advanced Cluster Security for Kubernetes alerts to automatically delete older alerts and save storage costs.

With Red Hat Advanced Cluster Security for Kubernetes, you can configure the time to keep historical alerts stored. Red Hat Advanced Cluster Security for Kubernetes then deletes the older alerts after the specified time.

By automatically deleting alerts that are no longer needed, you can save storage costs.

The alerts for which you can configure the retention period include:

- Runtime alerts, both unresolved (active) and resolved.

- Stale deploy-time alerts that do not apply to the current deployment.

<div class="note">

<div class="title">

</div>

- RHACS enables data retention settings by default. You can change these settings after the installation.

- When you upgrade Red Hat Advanced Cluster Security for Kubernetes, data retention settings are not applied unless you have enabled them before.

- You can configure alert retention settings by using the RHACS portal or the API.

- The deletion process runs every hour. Currently, you cannot change this.

</div>

<a id="configure-alert-data-retention_enable-alert-data-retention"></a>

# Configuring alert data retention

You can configure alert retention settings by using the RHACS portal or the Red Hat Advanced Cluster Security for Kubernetes API.

<div>

<div class="title">

Prerequisites

</div>

- You must have the `Administration` role with `read` and `write` permissions to configure data retention.

</div>

<div>

<div class="title">

Procedure

</div>

1.  In the RHACS portal, go to **Platform Configuration** → **System Configuration**.

2.  On the **System Configuration** view header, click **Edit**.

3.  Under the **Data Retention Configuration** section, update the number of days for each type of data. To save a type of data forever, set the retention period to `0` days.

    - **All Runtime Violations**

    - **Resolved Deploy-Phase Violations**

    - **Runtime Violations For Deleted Deployments**

    - **Images No Longer Deployed**

4.  Click **Save**.

    > [!NOTE]
    > To configure alert data retention by using Red Hat Advanced Cluster Security for Kubernetes API, view the `PutConfig` API and related APIs in the `ConfigService` group in the API reference documentation.

</div>
