<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

If you are using [PagerDuty](https://www.pagerduty.com/), you can forward alerts from Red Hat Advanced Cluster Security for Kubernetes to PagerDuty.

The following steps represent a high-level workflow for integrating Red Hat Advanced Cluster Security for Kubernetes with PagerDuty:

1.  Add a new API service in PagerDuty and get the integration key.

2.  Use the integration key to set up notifications in Red Hat Advanced Cluster Security for Kubernetes.

3.  Identify the policies you want to send notifications for, and update the notification settings for those policies.

<a id="configure-pagerduty_integrate-with-pagerduty"></a>

# Configuring PagerDuty

Start integrating with PagerDuty by creating a new service and by getting the integration key.

<div>

<div class="title">

Procedure

</div>

1.  Go to **Configuration** → **Services**.

2.  Select **Add Services**.

3.  Under **General Settings**, specify a **Name** and **Description**.

4.  Under **Integration Setting**, click **Use our API Directly** with **Events v2 API** selected for the **Integration Type** drop-down menu.

5.  Under **Incident Settings**, select an **Escalation Policy**, and configure notification settings and incident timeouts.

6.  Accept default settings for **Incident Behavior** and **Alert Grouping**, or configure them as required.

7.  Click **Add Service**.

8.  From the **Service Details** page, make note of the **Integration Key**.

</div>

<a id="pagerduty-configuring-acs_integrate-with-pagerduty"></a>

# Configuring Red Hat Advanced Cluster Security for Kubernetes

Create a new integration in Red Hat Advanced Cluster Security for Kubernetes by using the integration key.

<div>

<div class="title">

Procedure

</div>

1.  In the RHACS portal, go to **Platform Configuration** → **Integrations**.

2.  Scroll down to the **Notifier Integrations** section and select **PagerDuty**.

3.  Click **New Integration** (**`add`** icon).

4.  Enter a name for **Integration Name**.

5.  Enter the integration key in the **PagerDuty integration key** field.

6.  Click **Test** to validate that the integration with PagerDuty is working.

7.  Click **Create** to create the configuration.

</div>

<a id="configure-policy-notifications_integrate-with-pagerduty"></a>

# Configuring policy notifications

Enable alert notifications for system policies.

<div>

<div class="title">

Procedure

</div>

1.  In the RHACS portal, go to **Platform Configuration** → **Policy Management**.

2.  Select one or more policies for which you want to send alerts.

3.  Under **Bulk actions**, select **Enable notification**.

4.  In the **Enable notification** window, select the **PagerDuty** notifier.

    > [!NOTE]
    > If you have not configured any other integrations, the system displays a message that no notifiers exist.

5.  Click **Enable**.

    <div class="note">

    <div class="title">

    </div>

    - Red Hat Advanced Cluster Security for Kubernetes sends notifications on an opt-in basis. To receive notifications, you must first assign a notifier to the policy.

    - Notifications are only sent once for a given alert. If you have assigned a notifier to a policy, you will not receive a notification unless a violation generates a new alert.

    - Red Hat Advanced Cluster Security for Kubernetes creates a new alert for the following scenarios:

      - A policy violation occurs for the first time in a deployment.

      - A runtime-phase policy violation occurs in a deployment after you resolved the earlier runtime alert for a policy in that deployment.

    </div>

</div>
