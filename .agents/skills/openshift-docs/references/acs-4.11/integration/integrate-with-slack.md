<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

<!-- Security modification: credential-shaped Slack webhook examples replaced with placeholders. No endpoint was contacted. -->

If you are using Slack, you can forward alerts from Red Hat Advanced Cluster Security for Kubernetes to Slack.

The following steps represent a high-level workflow for integrating Red Hat Advanced Cluster Security for Kubernetes with Slack:

1.  Create a new Slack app, enable incoming webhooks, and get a webhook URL.

2.  Use the webhook URL to integrate Slack with Red Hat Advanced Cluster Security for Kubernetes.

3.  Identify policies for which you want to send notifications, and update the notification settings for those policies.

<a id="configure-slack_integrate-with-slack"></a>

# Configuring Slack

Start by creating a new Slack app, and get the webhook URL.

<div>

<div class="title">

Prerequisites

</div>

- You need an administrator account or a user account with permissions to create webhooks.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create a new Slack app:

    > [!NOTE]
    > If you want to use an existing Slack app, go to <https://api.slack.com/apps> and select an app.

    1.  Go to <https://api.slack.com/apps/new>.

    2.  Enter the **App Name** and choose a **Development Slack Workspace** to install your app.

    3.  Click **Create App**.

2.  On the settings page, **Basic Information** section, select **Incoming Webhooks** (under **Add features and functionality**).

3.  Turn on the **Activate Incoming Webhooks** toggle.

4.  Select **Add New Webhook to Workspace**.

5.  Choose a **channel** that the app will post to, and then select **Authorize**. The page refreshes and you are sent back to your app settings page.

6.  Copy the webhook URL located in the **Webhook URLs for Your Workspace** section.

</div>

For more information, see the Slack documentation topic, [Getting started with Incoming Webhooks](https://api.slack.com/incoming-webhooks#getting_started_with_incoming_webhooks).

<a id="send-alerts-to-different-slack-channels_integrate-with-slack"></a>

## Sending alerts to different Slack channels

You can configure Red Hat Advanced Cluster Security for Kubernetes to send notifications to different Slack channels so that they directly go to the right team.

<div>

<div class="title">

Procedure

</div>

1.  After you configure incoming webhooks, add an annotation similar to the following in your deployment YAML file:

    ``` yaml
    example.com/slack-webhook: https://hooks.slack.com/services/REPLACE_WORKSPACE/REPLACE_CHANNEL/REPLACE_TOKEN
    ```

2.  Use the annotation key `example.com/slack-webhook` in the **Label/Annotation Key For Slack Webhook** field when you configure Red Hat Advanced Cluster Security for Kubernetes.

</div>

After the configuration is complete, if a deployment has the annotation that you configured in the YAML file, Red Hat Advanced Cluster Security for Kubernetes sends the alert to the webhook URL you specified for that annotation. Otherwise, it sends the alert to the default webhook URL.

<a id="slack-configuring-acs_integrate-with-slack"></a>

# Configuring Red Hat Advanced Cluster Security for Kubernetes

Create a new integration in Red Hat Advanced Cluster Security for Kubernetes by using the webhook URL.

<div>

<div class="title">

Procedure

</div>

1.  In the RHACS portal, go to **Platform Configuration** → **Integrations**.

2.  Scroll down to the **Notifier Integrations** section and select **Slack**.

3.  Click **New Integration** (**`add`** icon).

4.  Enter a name for **Integration Name**.

5.  Enter the generated webhook URL in the **Default Slack Webhook** field.

6.  Select **Test** to test that the integration with Slack is working.

7.  Select **Create** to generate the configuration.

</div>

<a id="configure-policy-notifications_integrate-with-slack"></a>

# Configuring policy notifications

Enable alert notifications for system policies.

<div>

<div class="title">

Procedure

</div>

1.  In the RHACS portal, go to **Platform Configuration** → **Policy Management**.

2.  Select one or more policies for which you want to send alerts.

3.  Under **Bulk actions**, select **Enable notification**.

4.  In the **Enable notification** window, select the **Slack** notifier.

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
