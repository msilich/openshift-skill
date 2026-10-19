<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Red Hat Advanced Cluster Security for Kubernetes (RHACS) can automatically remove nonactive clusters so that you monitor active clusters only. You can set how long a cluster stays unreachable before removal, and label the clusters that you want to keep.

<a id="configure-inactive-cluster-deletion-overview_configure-nonactive-cluster-removal"></a>

# Overview of automatic cluster removal

RHACS provides the option to automatically remove nonactive clusters so that you can monitor active clusters only. You can configure the decommissioned cluster age and add labels to preserve specific clusters from removal.

Automatic removal of nonactive clusters from RHACS is disabled by default. To enable this setting, enter a nonzero number in the **Decommissioned cluster age** field, as described in the following procedure. The **Decommissioned cluster age** field indicates the number of days that a cluster can remain unreachable before it becomes nonactive. When a cluster is nonactive, the **Clusters** page displays the status of the cluster. Nonactive clusters show the `unhealthy` label and the window shows the number of days after which RHACS will remove the cluster if it continues to remain nonactive. After RHACS removes a cluster, an `info` log entry documents the action in the Central logs.

> [!NOTE]
> There is a 24-hour grace period after you enable this setting before RHACS removes any clusters. RHACS never removes the cluster that hosts Central.

<a id="configure-cluster-decommissioning_configure-nonactive-cluster-removal"></a>

# Configuring cluster decommissioning

You can configure RHACS to automatically remove clusters in which Central has been unable to reach Sensor for a specified number of days. You can also label specific clusters so that RHACS does not remove them.

<div>

<div class="title">

Procedure

</div>

1.  In the RHACS portal, go to **Platform Configuration** → **System Configuration**.

2.  In the **System Configuration** header, click **Edit**.

3.  In the **Cluster deletion** section, you can configure the following fields:

    - **Decommissioned cluster age**: The number of days that a cluster is unreachable before it becomes eligible for removal from RHACS. If Central cannot reach Sensor on the cluster for this number of days, RHACS removes the cluster and all of its resources. To leave this feature disabled, which is the default behavior, enter `0` in this field. To enable this feature, enter a nonzero number, such as `90`, to configure the number of unreachable days.

    - **Ignore clusters which have labels**: To prevent RHACS from removing a cluster, you can configure a label by entering a key and value. RHACS does not remove clusters with this label, even if they have been unreachable for the number of days set in the **Decommissioned cluster age** field.

      - **Key**: Enter the label to use for the cluster.

      - **Value**: Enter the value associated with the key.

        For example, to preserve production clusters from removal, you can configure a key of `cluster-type` and a value of `production`.

        > [!NOTE]
        > In the **Cluster deletion** section, click **Clusters which have Sensor Status: Unhealthy** to go to the **Clusters** list page. This page shows nonactive clusters that are subject to removal and a time frame for the removal from RHACS.

4.  Click **Save**.

    > [!NOTE]
    > To view and configure this option by using the API, use the `decommissionedClusterRetention` settings in the request payload for the `/v1/config` and `/v1/config/private` endpoints. For more information, see the API documentation for the `ConfigService` object by navigating to **Help** → **API reference** in the RHACS portal.

</div>

<a id="view-nonactive-clusters_configure-nonactive-cluster-removal"></a>

# Viewing nonactive clusters

Nonactive clusters are clusters that installed and performed a handshake with Central at least one time but have been unreachable by Sensor for a specified period of time. Use this procedure to view a list of these clusters.

<div>

<div class="title">

Procedure

</div>

1.  In the RHACS portal, go to **Platform Configuration** → **System Configuration**.

2.  In the **Cluster deletion** section, click **Clusters which have Sensor Status: Unhealthy** to go to the **Clusters** list page. This page shows nonactive clusters that are subject to removal from RHACS and a time frame for the removal.

    > [!NOTE]
    > If you enable this feature after a cluster becomes nonactive, the counting of days towards removal starts from the time the cluster became nonactive, not from the time that you enabled the feature. If there are any nonactive clusters that you do not want RHACS to remove, you can configure a label as described in "Configuring cluster decommissioning". The system ignores clusters with those labels when removing nonactive clusters.

</div>
