<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Red Hat Lightspeed repeatedly analyzes the data Insights Operator sends, which includes workload recommendations from Deployment Validation Operator (DVO). Users of OpenShift Container Platform can display the results in the [Advisor](https://console.redhat.com/openshift/insights/advisor/) service on the Red Hat Hybrid Cloud Console.

# About Red Hat Lightspeed Advisor for OpenShift Container Platform

You can use the Red Hat Lightspeed advisor service to assess and monitor the health of your OpenShift Container Platform clusters.

If you are concerned about individual clusters or with your whole infrastructure, be aware of the exposure of your cluster infrastructure to issues that can affect service availability, fault tolerance, performance, or security.

If the cluster has the Deployment Validation Operator (DVO) installed the recommendations also highlight workloads whose configuration might lead to cluster health issues.

The results of the Red Hat Lightspeed analysis are available in the Red Hat Lightspeed advisor service on Red Hat Hybrid Cloud Console. In the Red Hat Hybrid Cloud Console, you can perform the following actions:

- View clusters and workloads affected by specific recommendations.

- Use robust filtering capabilities to refine your results to those recommendations.

- Learn more about individual recommendations, details about the risks they present, and get resolutions tailored to your individual clusters.

- Share results with other stakeholders.

<div>

<div class="title">

Additional resources

</div>

- [Using the Deployment Validation Operator in your Red Hat Lightspeed workflow](https://docs.redhat.com/en/documentation/red_hat_lightspeed/1-latest/html-single/monitoring_your_openshift_cluster_health_with_red_hat_lightspeed_advisor/index#using-the-deployment-validation-operator)

</div>

# Understanding Red Hat Lightspeed advisor service recommendations

The Red Hat Lightspeed advisor service bundles information about various cluster states and component configurations that can negatively affect the service availability, fault tolerance, performance, or security of your clusters and workloads.

The information set is called a recommendation in the Red Hat Lightspeed advisor service. Recommendations for clusters includes the following information:

- **Name:** A concise description of the recommendation

- **Added:** When the recommendation was published to the Red Hat Lightspeed advisor service archive

- **Category:** Whether the issue has the potential to negatively affect service availability, fault tolerance, performance, or security

- **Total risk:** A value derived from the *likelihood* that the condition will negatively affect your cluster or workload, and the *impact* on operations if that were to happen

- **Clusters:** A list of clusters on which a recommendation is detected

- **Description:** A brief synopsis of the issue, including how it affects your clusters

# Displaying potential issues with your cluster

You can display a Red Hat Lightspeed report in **Red Hat Lightspeed Advisor** on [OpenShift Cluster Manager](https://console.redhat.com/openshift).

Note that Red Hat Lightspeed repeatedly analyzes your cluster and shows the latest results. These results can change, for example, if you fix an issue or a new issue has been detected.

<div>

<div class="title">

Prerequisites

</div>

- Your cluster is registered on [OpenShift Cluster Manager](https://console.redhat.com/openshift).

- Remote health reporting is enabled, which is the default.

- You are logged in to [OpenShift Cluster Manager](https://console.redhat.com/openshift).

</div>

<div>

<div class="title">

Procedure

</div>

1.  Navigate to **Advisor** → **Recommendations** on [OpenShift Cluster Manager](https://console.redhat.com/openshift).

    Depending on the result, the Red Hat Lightspeed advisor service displays one of the following:

    - **No matching recommendations found**, if Red Hat Lightspeed did not identify any issues.

    - A list of issues Red Hat Lightspeed has detected, grouped by risk (low, moderate, important, and critical).

    - **No clusters yet**, if Red Hat Lightspeed has not yet analyzed the cluster. The analysis starts shortly after the cluster has been installed, registered, and connected to the internet.

2.  If any issues are displayed, click the **\>** icon in front of the entry for more details.

    Depending on the issue, the details can also contain a link to more information from Red Hat about the issue.

</div>

# Displaying all Red Hat Lightspeed advisor service recommendations

The **Recommendations** view, by default, only displays the recommendations that are detected on your clusters. However, you can view all of the recommendations in the archive of the service.

<div>

<div class="title">

Prerequisites

</div>

- Remote health reporting is enabled, which is the default.

- Your cluster is [registered](https://console.redhat.com/openshift/register) on Red Hat Hybrid Cloud Console.

- You are logged in to [OpenShift Cluster Manager](https://console.redhat.com/openshift).

</div>

<div>

<div class="title">

Procedure

</div>

1.  Navigate to **Advisor** → **Recommendations** on [OpenShift Cluster Manager](https://console.redhat.com/openshift).

2.  Click the **X** icons next to the **Clusters Impacted** and **Status** filters.

    You can now browse through all of the potential recommendations for your cluster.

</div>

# Advisor recommendation filters

The Red Hat Lightspeed advisor service can return a large number of recommendations. To focus on your most critical recommendations, you can apply filters to the advisor recommendations list on the Hybrid Cloud Console to remove low-priority recommendations.

By default, filters are set to only show enabled recommendations that are impacting one or more clusters. To view all or disabled recommendations in the Red Hat Lightspeed library, you can customize the filters.

To apply a filter, select a filter type and then set its value based on the options that are available in the drop-down list. You can apply multiple filters to the list of recommendations.

You can set the following filter types:

- **Name:** Search for a recommendation by name.

- **Total risk:** Select one or more values from **Critical**, **Important**, **Moderate**, and **Low** indicating the likelihood and the severity of a negative impact on a cluster.

- **Impact:** Select one or more values from **Critical**, **High**, **Medium**, and **Low** indicating the potential impact to the continuity of cluster operations.

- **Likelihood:** Select one or more values from **Critical**, **High**, **Medium**, and **Low** indicating the potential for a negative impact to a cluster if the recommendation comes to fruition.

- **Category:** Select one or more categories from **Service Availability**, **Performance**, **Fault Tolerance**, **Security**, and **Best Practice** to focus your attention on.

- **Status:** Click a radio button to show enabled recommendations (default), disabled recommendations, or all recommendations.

- **Clusters impacted:** Set the filter to show recommendations currently impacting one or more clusters, non-impacting recommendations, or all recommendations.

- **Risk of change:** Select one or more values from **High**, **Moderate**, **Low**, and **Very low** indicating the risk that the implementation of the resolution could have on cluster operations.

<div>

<div class="title">

Additional resources

</div>

- [Advisor recommendations (Red Hat Hybrid Cloud Console)](https://console.redhat.com/openshift/insights/advisor/recommendations)

</div>

## Filtering Red Hat Lightspeed advisor service recommendations

As an OpenShift Container Platform cluster manager, you can filter the recommendations that are displayed on the recommendations list. By applying filters, you can reduce the number of reported recommendations and concentrate on your highest priority recommendations.

The following procedure demonstrates how to set and remove **Category** filters; however, the procedure is applicable to any of the filter types and respective values.

<div>

<div class="title">

Prerequisites

</div>

- You are logged in to the [OpenShift Cluster Manager](https://console.redhat.com/openshift) in the Hybrid Cloud Console.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Go to [**OpenShift** \> **Advisor** \> **Recommendations**](https://console.redhat.com/openshift/insights/advisor/recommendations?).

2.  In the main, filter-type drop-down list, select the **Category** filter type.

3.  Expand the filter-value drop-down list and select the checkbox next to each category of recommendation you want to view. Leave the checkboxes for unnecessary categories clear.

4.  Optional: Add additional filters to further refine the list.

</div>

Only recommendations from the selected categories are shown in the list.

<div>

<div class="title">

Verification

</div>

- After applying filters, you can view the updated recommendations list. The applied filters are added next to the default filters.

</div>

## Removing filters from Red Hat Lightspeed advisor service recommendations

You can apply multiple filters to the list of recommendations. When ready, you can remove them individually or completely reset them.

<div>

<div class="title">

Procedure

</div>

- To remove default or non-default filters individually, click the **X** icon next to each filter.

- To remove all non-default filters, click **Reset filters** to remove only the filters that you applied, leaving the default filters in place.

</div>

# Disabling Red Hat Lightspeed advisor service recommendations

You can disable specific recommendations that affect your clusters, so that they no longer show in your reports. You can disable a recommendation for a single cluster or all of your clusters.

> [!NOTE]
> Disabling a recommendation for all of your clusters also applies to any future clusters.

<div>

<div class="title">

Prerequisites

</div>

- Remote health reporting is enabled, which is the default.

- Your cluster is registered on [OpenShift Cluster Manager](https://console.redhat.com/openshift).

- You are logged in to [OpenShift Cluster Manager](https://console.redhat.com/openshift).

</div>

<div>

<div class="title">

Procedure

</div>

1.  Navigate to **Advisor** → **Recommendations** on [OpenShift Cluster Manager](https://console.redhat.com/openshift).

2.  Optional: Use the **Clusters Impacted** and **Status** filters as needed.

3.  Disable an alert by using one of the following methods:

    - To disable an alert:

      1.  Click the **Options** menu ![kebab](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABsAAAAjCAIAAADqn+bCAAAACXBIWXMAAA7EAAAOxAGVKw4bAAAA+0lEQVRIie2WMQqEMBBFJ47gUXRBLyBYqbUXULCx9CR2XsAb6AlUEM9kpckW7obdZhwWYWHXX/3i8TPJZEKEUgpOlXFu3JX4V4kmB2qaZhgGKSUiZlkWxzEBC84N9zxv27bdO47Tti0Bs3at4wBgXVca/lJnfN/XPggCGmadIwAsywIAiGhZFk1ydy2EYJKgGCqK4vZUVVU0zKpxnmftp2mi4S/1GhG1N82DMWNNYVmW4zgqpRAxTVMa5t4evlg11nXd9/1eY57nSZIQMKtG13WllLu3bbvrOgJmdUbHwfur8Xniqw6Hh5UYRdGDNowwDA+WvP4UV+JPJ94B1gKUWcTOCT0AAAAASUVORK5CYII=) for that alert, and then click **Disable recommendation**.

      2.  Enter a justification note and click **Save**.

    - To view the clusters affected by this alert before disabling the alert:

      1.  Click the name of the recommendation to disable. You are directed to the single recommendation page.

      2.  Review the list of clusters in the **Affected clusters** section.

      3.  Click **Actions** → **Disable recommendation** to disable the alert for all of your clusters.

      4.  Enter a justification note and click **Save**.

</div>

# Enabling a previously disabled Red Hat Lightspeed advisor service recommendation

When a recommendation is disabled for all clusters, you no longer see the recommendation in the Red Hat Lightspeed advisor service. You can change this behavior.

<div>

<div class="title">

Prerequisites

</div>

- Remote health reporting is enabled, which is the default.

- Your cluster is registered on [OpenShift Cluster Manager](https://console.redhat.com/openshift).

- You are logged in to [OpenShift Cluster Manager](https://console.redhat.com/openshift).

</div>

<div>

<div class="title">

Procedure

</div>

1.  Navigate to **Advisor** → **Recommendations** on [OpenShift Cluster Manager](https://console.redhat.com/openshift).

2.  Filter the recommendations to display on the disabled recommendations:

    1.  From the **Status** drop-down menu, select **Status**.

    2.  From the **Filter by status** drop-down menu, select **Disabled**.

    3.  Optional: Clear the **Clusters impacted** filter.

3.  Locate the recommendation to enable.

4.  Click the Options menu ![kebab](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABsAAAAjCAIAAADqn+bCAAAACXBIWXMAAA7EAAAOxAGVKw4bAAAA+0lEQVRIie2WMQqEMBBFJ47gUXRBLyBYqbUXULCx9CR2XsAb6AlUEM9kpckW7obdZhwWYWHXX/3i8TPJZEKEUgpOlXFu3JX4V4kmB2qaZhgGKSUiZlkWxzEBC84N9zxv27bdO47Tti0Bs3at4wBgXVca/lJnfN/XPggCGmadIwAsywIAiGhZFk1ydy2EYJKgGCqK4vZUVVU0zKpxnmftp2mi4S/1GhG1N82DMWNNYVmW4zgqpRAxTVMa5t4evlg11nXd9/1eY57nSZIQMKtG13WllLu3bbvrOgJmdUbHwfur8Xniqw6Hh5UYRdGDNowwDA+WvP4UV+JPJ94B1gKUWcTOCT0AAAAASUVORK5CYII=), and then click **Enable recommendation**.

</div>

# About Red Hat Lightspeed advisor service recommendations for workloads

You can use the Red Hat Lightspeed advisor service to view and manage information about recommendations that affect not only your clusters, but also your workloads. The advisor service takes advantage of deployment validation and helps OpenShift Container Platform cluster administrators to see all runtime violations of deployment policies.

You can see recommendations for workloads at **OpenShift** \> **Advisor** \> **Workloads** on the Red Hat Hybrid Cloud Console. For more information, see the following sections in the *Additional resources* section:

- Information about Kubernetes workloads

- Boost your cluster operations with Deployment Validation and Red Hat Lightspeed Advisor for Workloads

- Identifying workload recommendations for namespaces in your clusters

- Viewing workload recommendations for namespaces in your cluster

- Excluding objects from workload recommendations in your clusters

<div>

<div class="title">

Additional resources

</div>

- [OpenShift \> Advisor \> Workloads (Red Hat Hybrid Cloud Console)](https://console.redhat.com/openshift/insights/advisor/workloads)

- [Information about Kubernetes workloads (Kubernetes documentation)](https://kubernetes.io/docs/concepts/workloads/)

- [Boost your cluster operations with Deployment Validation and Red Hat Lightspeed Advisor for Workloads (Red Hat Blog)](https://www.redhat.com/en/blog/boost-your-cluster-operations-with-deployment-validation-and-insights-advisor-for-workloads)

- [Identifying workload recommendations for namespaces in your clusters](https://docs.redhat.com/en/documentation/red_hat_lightspeed/1-latest/html-single/monitoring_your_openshift_cluster_health_with_red_hat_lightspeed_advisor/index#identifying-workload-recommendations-for-namespaces-in-clusters_using-insights-advisor)

- [Viewing workload recommendations for namespaces in your cluster](https://docs.redhat.com/en/documentation/red_hat_lightspeed/1-latest/html-single/monitoring_your_openshift_cluster_health_with_red_hat_lightspeed_advisor/index#viewing-workload-recommendations-for-namespaces_using-insights-advisor)

- [Excluding objects from workload recommendations in your clusters](https://docs.redhat.com/en/documentation/red_hat_lightspeed/1-latest/html-single/monitoring_your_openshift_cluster_health_with_red_hat_lightspeed_advisor/index#excluding-objects-from-workload-recommendations_using-insights-advisor)

</div>

# Displaying the Red Hat Lightspeed status in the web console

Red Hat Lightspeed repeatedly analyzes your cluster and you can display the status of identified potential issues of your cluster in the OpenShift Container Platform web console. This status shows the number of issues in the different categories and, for further details, links to the reports in [OpenShift Cluster Manager](https://console.redhat.com/openshift).

<div>

<div class="title">

Prerequisites

</div>

- Your cluster is registered in [OpenShift Cluster Manager](https://console.redhat.com/openshift).

- Remote health reporting is enabled, which is the default.

- You are logged in to the OpenShift Container Platform web console.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Navigate to **Home** → **Overview** in the OpenShift Container Platform web console.

2.  Click **Red Hat Lightspeed** on the **Status** card.

    The pop-up window lists potential issues grouped by risk. Click the individual categories or **View all recommendations in Red Hat Lightspeed Advisor** to display more details.

</div>
