<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Red Hat Advanced Cluster Security for Kubernetes (RHACS) provides the option to configure your system to automatically remove nonactive clusters from RHACS so that you can monitor active clusters only. RHACS monitors only clusters that were installed and performed a handshake with Central at least one time.

If you enable automatic removal of nonactive clusters, RHACS considers the cluster nonactive when Central has been unable to reach Sensor in the cluster for the period of time configured in the **Decommissioned cluster age** field. Central will then no longer monitor nonactive clusters. You can configure the **Decommissioned cluster age** field in the **Platform Configuration** → **System Configuration** page.

Removal of nonactive clusters from RHACS is disabled by default. To enable this setting, enter a nonzero number in the **Decommissioned cluster age** field, as described in the following procedure.

The **Decommissioned cluster age** field indicates the number of days that a cluster can remain unreachable before it is considered nonactive. When a cluster is nonactive, the **Clusters** page displays the status of the cluster.

Nonactive clusters are indicated with the `unhealthy` label and the window shows the number of days after which the cluster will be removed from RHACS if it continues to remain nonactive. After a cluster is removed from RHACS, that action is documented with an `info` log in the Central logs.

> [!NOTE]
> There is a 24-hour grace period after enabling this setting before clusters are removed. The cluster that hosts Central is never removed.

<a id="configure-cluster-decommissioning_configure-nonactive-cluster-removal"></a>

# Configuring cluster decommissioning

You can configure RHACS to automatically remove nonactive clusters from RHACS. Nonactive clusters are those that were installed and performed a handshake with Central at least once but have been unreachable by Sensor for a specified period of time. You can also label clusters so that they are not removed when they are unreachable.

<div>

<div class="title">

Procedure

</div>

1.  In the RHACS portal, go to **Platform Configuration** → **System Configuration**.

2.  In the **System Configuration** header, click **Edit**.

3.  In the **Cluster deletion** section, configure the **Decommissioned cluster age**. This is the number of days that a cluster is unreachable before RHACS considers it for removal. If Central cannot reach Sensor on the cluster for this number of days, RHACS removes the cluster and all of its resources. To leave this feature disabled, which is the default behavior, enter `0` in this field. To enable this feature, enter a nonzero number, such as `90`, to configure the number of unreachable days.

    > [!NOTE]
    > In the **Cluster deletion** section, click **Clusters which have Sensor Status: Unhealthy** to go to the **Clusters** list page. This page is filtered to show nonactive clusters that are subject to removal and a timeframe for the removal from RHACS.

4.  Click **Save**.

</div>

> [!NOTE]
> To view and configure this option by using the API, use the `decommissionedClusterRetention` settings in the request payload for the `/v1/config` and `/v1/config/private` endpoints. For more information, see the API documentation for the `ConfigService` object by navigating to **Help** → **API reference** in the RHACS portal.

<a id="view-nonactive-clusters_configure-nonactive-cluster-removal"></a>

# Viewing nonactive clusters

Nonactive clusters are clusters that were installed and performed a handshake with Central at least once but have been unreachable by Sensor for a specified period of time. Use this procedure to view a list of these clusters.

<div>

<div class="title">

Procedure

</div>

1.  In the RHACS portal, go to **Platform Configuration** → **System Configuration**.

2.  In the **Cluster deletion** section, click **Clusters which have Sensor Status: Unhealthy** to go to the **Clusters** list page. This page is filtered to show nonactive clusters that are subject to removal from RHACS and a timeframe for the removal.

    > [!NOTE]
    > If this feature is enabled after a cluster is considered nonactive, the counting of days towards removal starts from the time the cluster became nonactive, not from the time that the feature was enabled. If there are any nonactive clusters that you do not want removed, you can configure a label as described in the "Configuring cluster decommissioning" section. Clusters with those labels are ignored when the system removes nonactive clusters.

</div>
