<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

The **Observe** view in the **Developer** perspective enables you to monitor project and application metrics to track performance, troubleshoot issues, and respond to alerts. For example, CPU, memory, and bandwidth usage, and network related information.

# Prerequisites

- You have created and deployed applications on OpenShift Container Platform.

- You have logged in to the web console.

- The **Developer** perspective is enabled and you have switched to it.

> [!IMPORTANT]
> Starting with OpenShift Container Platform 4.19, the perspectives in the web console have unified. The **Developer** perspective is no longer enabled by default.
>
> All users can interact with all OpenShift Container Platform web console features. However, if you are not the cluster owner, you might need to request permission to access certain features from the cluster owner.
>
> You can still enable the **Developer** perspective. On the **Getting Started** pane in the web console, you can take a tour of the console, find information on setting up your cluster, view a quick start for enabling the **Developer** perspective, and follow links to explore new features and capabilities.
>
> See also, "Enabling the **Developer** perspective in the web console".

# Enabling the **Developer** perspective in the web console

Enable the **Developer** perspective in the web console to give your developers tools to manage applications, visualize topology, and monitor projects as they develop and build them.

Starting with OpenShift Container Platform 4.19, the perspectives in the web console have unified. There is no longer a **Developer** perspective by default; however, cluster administrators can enable the **Developer** perspective for developers to use.

You can enable the **Developer** perspective with the following steps:

<div>

<div class="title">

Prerequisites

</div>

- You have access to the web console as a user with `cluster-admin` privileges.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Navigate to the **Cluster Settings** page by clicking <span class="menuchoice">Administration \> Cluster Settings</span>.

2.  Select the **Configuration** tab.

3.  Type `console` in the search field to locate the Console Operator resource and select `operator.openshift.io`.

4.  On the **Cluster Details** page, click the **Actions** menu and select **Customize**.

5.  In the **General** tab, locate the **Perspectives** section. You can enable or disable the **Developer** perspective as needed. Changes are automatically applied.

6.  Optional: You can enable the **Developer** perspective by using the CLI with the following command:

    ``` terminal
    $ oc patch console.operator.openshift.io/cluster --type='merge' -p '{"spec":{"customization":{"perspectives":[{"id":"dev","visibility":{"state":"Enabled"}}]}}}'
    ```

    > [!NOTE]
    > The change reflects in the web console after the console pod restarts successfully.

</div>

<div>

<div class="title">

Verification

</div>

1.  Locate the perspective switcher in the web console.

2.  Verify that **Developer** is displayed as an available perspective option.

</div>

# Monitoring capabilities from the Developer perspective

The **Observe** view in the **Developer** perspective shows monitoring tools filtered by your project access permissions to track performance, troubleshoot issues, and respond to alerts. You can monitor CPU, memory, bandwidth, and network metrics.

> [!IMPORTANT]
> Starting with OpenShift Container Platform 4.19, the perspectives in the web console have unified. The **Developer** perspective is no longer enabled by default.
>
> All users can interact with all OpenShift Container Platform web console features. However, if you are not the cluster owner, you might need to request permission to access certain features from the cluster owner.
>
> You can still enable the **Developer** perspective. On the **Getting Started** pane in the web console, you can take a tour of the console, find information on setting up your cluster, view a quick start for enabling the **Developer** perspective, and follow links to explore new features and capabilities.
>
> See also, "Enabling the **Developer** perspective in the web console".

The **Observe** view in the **Developer** perspective uses the same monitoring components as the **Administrator** perspective, but displays only the projects you have permissions for. You can monitor your applications without seeing cluster-wide metrics you cannot access.

> [!NOTE]
> A project represents a Kubernetes namespace with additional annotations. When you select a project in the **Developer** perspective, you view the topology and metrics for that namespace.

After selecting a project in the **Observe** view, the following tabs become available:

- **Events**: Cluster events filtered by the selected project

- **Alerting rules**: Configured alerting rules and their current state

- **Alerts**: Firing alerts for the selected project

- **Dashboards**: Pre-built visual dashboards showing resource consumption graphs including CPU usage, memory usage, bandwidth consumption, and network-related information

- **Metrics**: Prometheus query interface for analyzing specific metrics

- **Silences**: Create and manage alert silences to temporarily suppress alert notifications

The monitoring interface is the same as the **Administrator** perspective, with the key difference being project filtering based on your access permissions.

> [!NOTE]
> In the **Administrator** perspective, the monitoring tabs are immediately available with a project dropdown for filtering. In the **Developer** perspective, you must select a project before the tabs are displayed. This scoping enables your developers to observe their applications by using the same monitoring tools as cluster administrators, focused only on their assigned projects.

# Viewing project dashboards

View pre-built dashboards showing CPU usage, memory usage, bandwidth consumption, and network information across your project (namespace) topology to help you monitor application performance.

<div>

<div class="title">

Procedure

</div>

1.  In the **Developer** perspective navigation menu, select **Observe**.

2.  Select a project from the **Project** list. After you select a project, the monitoring tabs are displayed.

3.  Click the **Dashboards** tab.

    The **Dashboards** tab displays pre-built Kubernetes compute resources dashboards showing metrics such as CPU usage, memory usage, bandwidth consumption, and network-related information. The dashboard layout includes metric cards at the top showing current utilization percentages, and expandable graph sections below showing detailed resource usage trends over time.

</div>

# Monitoring your application metrics

Inspect alerts, metric charts, and health check status for individual application workloads to troubleshoot performance issues and monitor health directly from the topology view.

<div>

<div class="title">

Procedure

</div>

1.  In the **Developer** perspective, navigate to the **Topology** view.

2.  Click the workload node to open the side panel.

3.  Select the **Observe** tab to view workload-specific metrics:

    - Review active critical and warning alerts associated with the workload.

    - View CPU, memory, and bandwidth usage charts.

    - Click **View monitoring dashboard** to open the full metrics dashboard for the workload.

      > [!NOTE]
      > Only critical and warning alerts in the **Firing** state are displayed in the **Topology** view. Alerts in the **Silenced**, **Pending** and **Not Firing** states are not displayed.

</div>

# Image vulnerability metrics and severity levels

Review container image security scan results on the project dashboard to identify and prioritize vulnerabilities for remediation.

In the **Developer** perspective, the project dashboard shows the **Image Vulnerabilities** link in the **Status** section. Using this link, you can view the **Image Vulnerabilities breakdown** window, which displays metrics such as the total count of vulnerable container images and fixable container images, organized by severity. The icon color indicates severity:

- Red: High severity. Fix immediately.

- Orange: Medium severity. Can be fixed after high-severity vulnerabilities.

- Yellow: Low severity. Can be fixed after high and medium-severity vulnerabilities.

Based on the severity level, you can prioritize vulnerabilities and fix them in an organized manner.

# Monitoring your application and image vulnerabilities metrics

Analyze application dependency vulnerabilities across your cluster to identify and remediate security issues in container images.

After you create applications in your project and deploy them, use the **Developer** perspective in the web console to see the metrics for your application dependency vulnerabilities across your cluster. The metrics help you to analyze the following image vulnerabilities in detail:

- Total count of vulnerable images in a selected project

- Severity-based counts of all vulnerable images in a selected project

- Drill down into severity to obtain the details, such as count of vulnerabilities, count of fixable vulnerabilities, and number of affected pods for each vulnerable image

<div>

<div class="title">

Prerequisites

</div>

- You have installed the Red Hat Quay Container Security Operator.

  > [!NOTE]
  > The Red Hat Quay Container Security Operator detects vulnerabilities by scanning the images that are in the Red Hat Quay registry.

</div>

<div>

<div class="title">

Procedure

</div>

1.  In the **Developer** perspective, click **Project** to open the project dashboard.

2.  For a detailed vulnerabilities overview, click the **Vulnerabilities** tab.

    1.  To get more detail about an image, click its name.

    2.  View the default graph with all types of vulnerabilities in the **Details** tab.

    3.  Optional: Click the toggle button to view a specific type of vulnerability. For example, click **App dependency** to see vulnerabilities specific to application dependency.

    4.  Optional: You can filter the list of vulnerabilities based on their **Severity** and **Type** or sort them by **Severity**, **Package**, **Type**, **Source**, **Current Version**, and **Fixed in Version**.

    5.  Click a **Vulnerability** to get its associated details:

        - **Base image** vulnerabilities display information from a Red Hat Security Advisory (RHSA).

        - **App dependency** vulnerabilities display information from the Snyk security application.

</div>

# Additional resources

- [Monitoring stack for Red Hat OpenShift](https://docs.redhat.com/en/documentation/monitoring_stack_for_red_hat_openshift/4.22)

- [About OpenShift Container Platform monitoring](../observability/monitoring/about-ocp-monitoring.md#about-ocp-monitoring)

- [Creating applications by using the Developer perspective](creating_applications/odc-creating-applications-using-developer-perspective.md#odc-creating-applications-using-developer-perspective)

- [Accessing the web console](../web_console/web-console.md#web-console)

- [About the Developer perspective](../web_console/web-console-overview.md#about-developer-perspective_web-console-overview)
