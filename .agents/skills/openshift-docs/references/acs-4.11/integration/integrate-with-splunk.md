<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

If you are using [Splunk](https://www.splunk.com/), you can forward alerts from Red Hat Advanced Cluster Security for Kubernetes to Splunk and view the violations, vulnerability detection, and compliance related data from within Splunk.

> [!IMPORTANT]
> Currently, Splunk integration is not supported on IBM Power(`ppc64le`) and IBM Z(`s390x`).

Depending on your use case, you can integrate Red Hat Advanced Cluster Security for Kubernetes with Splunk by using the following ways:

- By [using an HTTP event collector](integrate-with-splunk.md#integrate-splunk-http-event-collector) in Splunk:

  - Use the event collector option to forward alerts and audit log data.

- By [using the Red Hat Advanced Cluster Security for Kubernetes add-on](integrate-with-splunk.md#integrate-splunk-add-on):

  - Use the add-on to pull the violations, vulnerability detection, and compliance data into Splunk.

You can use one or both of these integration options to integrate the Red Hat Advanced Cluster Security for Kubernetes with Splunk.

<a id="integrate-splunk-http-event-collector"></a>

# Using the HTTP event collector

You can forward alerts from Red Hat Advanced Cluster Security for Kubernetes to Splunk by using an HTTP event collector.

To integrate Red Hat Advanced Cluster Security for Kubernetes with Splunk by using the HTTP event collector, follow these steps:

1.  Add a new HTTP event collector in Splunk and get the token value.

2.  Use the token value to set up notifications in Red Hat Advanced Cluster Security for Kubernetes.

3.  Identify policies for which you want to send notifications, and update the notification settings for those policies.

<a id="add-http-event-collector-splunk_integrate-with-splunk"></a>

## Adding an HTTP event collector in Splunk

To configure Splunk to work with Red Hat Advanced Cluster Security for Kubernetes (RHACS), you must add a new HTTP event collector for your Splunk instance and get the token.

<div>

<div class="title">

Procedure

</div>

1.  In your Splunk dashboard, go to **Settings** → **Add Data**.

2.  Click **Monitor**.

3.  On the **Add Data** page, click **HTTP Event Collector**.

4.  Enter a **Name** for the event collector and then click **Next \>**.

5.  Accept the default **Input Settings** and click **Review \>**.

6.  Review the event collector properties and click **Submit \>**.

7.  Copy the **Token Value** for the event collector. You need this token value to configure integration with Splunk in Red Hat Advanced Cluster Security for Kubernetes.

</div>

<a id="integrate-splunk-enable-http-event-collector_integrate-with-splunk"></a>

### Enabling HTTP event collector

You must enable HTTP event collector tokens before you can receive events.

<div>

<div class="title">

Procedure

</div>

1.  In your Splunk dashboard, go to **Settings** → **Data inputs**.

2.  Click **HTTP Event Collector**.

3.  Click **Global Settings**.

4.  In the dialog that opens, click **Enabled** and then click **Save**.

</div>

<a id="splunk-configuring-acs_integrate-with-splunk"></a>

## Configuring Splunk integration in Red Hat Advanced Cluster Security for Kubernetes

Create a new Splunk integration in Red Hat Advanced Cluster Security for Kubernetes by using the token value.

<div>

<div class="title">

Procedure

</div>

1.  In the RHACS portal, go to **Platform Configuration** → **Integrations**.

2.  Scroll down to the **Notifier Integrations** section and select **Splunk**.

3.  Click **New Integration** (**`add`** icon).

4.  Enter a name for **Integration Name**.

5.  Enter your Splunk URL in the **HTTP Event Collector URL** field. You must specify the port number if it is not `443` for HTTPS or `80` for HTTP. You must also add the URL path `/services/collector/event` at the end of the URL. For example, `https://<splunk-server-path>:8088/services/collector/event`.

6.  Enter your token in the **HTTP Event Collector Token** field.

    > [!NOTE]
    > If you are using Red Hat Advanced Cluster Security for Kubernetes version 3.0.57 or newer, you can specify custom **Source Type for Alert** events and **Source Type for Audit** events.

7.  Select **Test** to send a test message to verify that the integration with Splunk is working.

8.  Select **Create** to generate the configuration.

</div>

<a id="configure-policy-notifications_integrate-with-splunk"></a>

## Configuring policy notifications

Enable alert notifications for system policies.

<div>

<div class="title">

Procedure

</div>

1.  In the RHACS portal, go to **Platform Configuration** → **Policy Management**.

2.  Select one or more policies for which you want to send alerts.

3.  Under **Bulk actions**, select **Enable notification**.

4.  In the **Enable notification** window, select the **Splunk** notifier.

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

<a id="integrate-splunk-add-on"></a>

# Using the Red Hat Advanced Cluster Security for Kubernetes add-on

You can use the Red Hat Advanced Cluster Security for Kubernetes add-on to forward the vulnerability detection and compliance related data from the Red Hat Advanced Cluster Security for Kubernetes to Splunk.

Generate an API token with `read` permission for all resources in Red Hat Advanced Cluster Security for Kubernetes and then use that token to install and configure the add-on.

<a id="install-and-configure-the-splunk-add-on_integrate-with-splunk"></a>

## Installing and configuring the Splunk add-on

You can install the Red Hat Advanced Cluster Security for Kubernetes add-on from your Splunk instance.

> [!NOTE]
> To maintain backward compatibility with the StackRox Kubernetes Security Platform add-on, the `source_type` and `input_type` parameters for configured inputs are still called `stackrox_compliance`, `stackrox_violations`, and `stackrox_vulnerability_management`.

<div>

<div class="title">

Prerequisites

</div>

- You must have an API token with `read` permission for all resources of Red Hat Advanced Cluster Security for Kubernetes. You can assign the **Analyst** system role to grant this level of access. The **Analyst** role has read permissions for all resources.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Download the Red Hat Advanced Cluster Security for Kubernetes add-on from [Splunkbase](https://splunkbase.splunk.com/app/5315/).

2.  Go to the Splunk home page on your Splunk instance.

3.  Go to **Apps** → **Manage Apps**.

4.  Select **Install app from file**.

5.  In the **Upload app** pop-up box, select **Choose File** and select the Red Hat Advanced Cluster Security for Kubernetes add-on file.

6.  Click **Upload**.

7.  Click **Restart Splunk**, and confirm to restart.

8.  After Splunk restarts, select **Red Hat Advanced Cluster Security for Kubernetes** from the **Apps** menu.

9.  Go to **Configuration** and then click **Add-on Settings**.

    1.  For **Central Endpoint**, enter the IP address or the name of your Central instance. For example, `central.custom:443`.

    2.  Enter the **API token** you have generated for the add-on.

    3.  Click **Save**.

10. Go to **Inputs**.

11. Click **Create New Input**, and select one of the following:

    - **ACS Compliance** to pull the compliance data.

    - **ACS Violations** to pull the violations data.

    - **ACS Vulnerability Management** to pull the vulnerabilities data.

12. Enter a **Name** for the input.

13. Select an **Interval** to pull data from Red Hat Advanced Cluster Security for Kubernetes. For example, every 14400 seconds.

14. Select the Splunk **Index** to which you want to send the data.

15. For **Central Endpoint**, enter the IP address or the name of your Central instance.

16. Enter the **API token** you have generated for the add-on.

17. Click **Add**.

</div>

<div>

<div class="title">

Verification

</div>

- To verify the the Red Hat Advanced Cluster Security for Kubernetes add-on installation, query the received data.

  1.  In your Splunk instance, go to **Search** and type `index=* sourcetype="stackrox-*"` as the query.

  2.  Press **Enter**.

</div>

Verify that your configured sources are displayed in the search results.

<a id="update-the-splunk-add-on_integrate-with-splunk"></a>

## Update the StackRox Kubernetes Security Platform add-on

If you are using the StackRox Kubernetes Security Platform add-on, you must upgrade to the new Red Hat Advanced Cluster Security for Kubernetes add-on.

You can see the update notification on the Splunk homepage under the list of apps on the left. Alternatively, you can also go to the **Apps** → **Manage apps** page to see the update notification.

<div>

<div class="title">

Prerequisites

</div>

- You must have an API token with `read` permission for all resources of Red Hat Advanced Cluster Security for Kubernetes. You can assign the **Analyst** system role to grant this level of access. The **Analyst** role has read permissions for all the resources.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Click **Update** on the update notification.

2.  Select the checkbox for accepting the terms and conditions, and then click **Accept and Continue** to install the update.

3.  After the installation, select **Red Hat Advanced Cluster Security for Kubernetes** from the **Apps** menu.

4.  Go to **Configuration** and then click **Add-on Settings**.

    1.  Enter the **API token** you have generated for the add-on.

    2.  Click **Save**.

</div>

<a id="troubleshoot-the-splunk-add-on_integrate-with-splunk"></a>

## Troubleshoot the Splunk add-on

If you stop receiving events from the Red Hat Advanced Cluster Security for Kubernetes add-on, check the Splunk add-on debug logs for errors.

Splunk creates a debug log file for every configured input in the `/opt/splunk/var/log/splunk` directory. Find the file named `stackrox_<input>_<uid>.log`, for example, `stackrox_compliance_29a3e14798aa2363d.log` and look for issues.
