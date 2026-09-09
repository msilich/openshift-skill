<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

If you are using [Sumo Logic](https://www.sumologic.com/), you can forward alerts from Red Hat Advanced Cluster Security for Kubernetes to Sumo Logic.

The following steps represent a high-level workflow for integrating Red Hat Advanced Cluster Security for Kubernetes with Sumo Logic:

1.  Add a new Custom App in Sumo Logic, set the HTTP source, and get the HTTP URL.

2.  Use the HTTP URL to integrate Sumo Logic with Red Hat Advanced Cluster Security for Kubernetes.

3.  Identify the policies you want to send notifications for, and update the notification settings for those policies.

<a id="configure-sumologic_integrate-with-sumologic"></a>

# Configuring Sumo Logic

Use the **Setup Wizard** to set up **Streaming Data** and get the HTTP URL.

<div>

<div class="title">

Procedure

</div>

1.  Log in to your Sumo Logic Home page and select **Setup Wizard**.

2.  Move your cursor over to **Set Up Streaming Data** and select **Get Started**.

3.  On the Select Data Type page, select **Your Custom App**.

4.  On the Set Up Collection page, select **HTTP Source**.

5.  Enter a name for **Source Category**, for example, `rhacs` and click **Continue**.

6.  **Copy** the generated URL.

</div>

<a id="sumologic-configuring-acs_integrate-with-sumologic"></a>

# Configuring Red Hat Advanced Cluster Security for Kubernetes

Create a new integration in Red Hat Advanced Cluster Security for Kubernetes by using the HTTP URL.

<div>

<div class="title">

Procedure

</div>

1.  In the RHACS portal, go to **Platform Configuration** → **Integrations**.

2.  Scroll down to the **Notifier Integrations** section and select **Sumo Logic**.

3.  Click **New Integration** (`add` icon).

4.  Enter a name for **Integration Name**.

5.  Enter the generated HTTP URL in the **HTTP Collector Source Address** field.

6.  Click **Test** (`checkmark` icon) to test that the integration with Sumo Logic is working.

7.  Click **Create** (`save` icon) to create the configuration.

</div>

<a id="configure-policy-notifications_integrate-with-sumologic"></a>

# Configuring policy notifications

Enable alert notifications for system policies.

<div>

<div class="title">

Procedure

</div>

1.  In the RHACS portal, go to **Platform Configuration** → **Policy Management**.

2.  Select one or more policies for which you want to send alerts.

3.  Under **Bulk actions**, select **Enable notification**.

4.  In the **Enable notification** window, select the **Sumo Logic** notifier.

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

<a id="view-alerts-in-sumo-logic_integrate-with-sumologic"></a>

# Viewing alerts in Sumo Logic

You can view alerts from Red Hat Advanced Cluster Security for Kubernetes in Sumo Logic.

1.  Log in to your Sumo Logic Home page and click **Log Search**.

2.  In the search box, enter `_sourceCategory=rhacs`. Make sure to use the same **Source Category** name that you entered while configuring Sumo Logic.

3.  Select the time and then click **Start**.
