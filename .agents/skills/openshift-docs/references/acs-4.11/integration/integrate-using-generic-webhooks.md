<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

With Red Hat Advanced Cluster Security for Kubernetes, you can send alert notifications as JSON messages to any webhook receiver. When a violation occurs, Red Hat Advanced Cluster Security for Kubernetes makes an HTTP POST request on the configured URL. The POST request body includes JSON-formatted information about the alert.

The webhook POST request’s JSON data includes a `v1.Alert` object and any custom fields that you configure, as shown in the following example:

``` json
{
  "alert": {
    "id": "<id>",
    "time": "<timestamp>",
    "policy": {
      "name": "<name>",
      ...
    },
    ...
  },
  "<custom_field_1>": "<custom_value_1>"
}
```

You can create multiple webhooks. For example, you can create one webhook for receiving all audit logs and another webhook for alert notifications.

To forward alerts from Red Hat Advanced Cluster Security for Kubernetes to any webhook receiver:

1.  Set up a webhook URL to receive alerts.

2.  Use the webhook URL to set up notifications in Red Hat Advanced Cluster Security for Kubernetes.

3.  Identify the policies you want to send notifications for, and update the notification settings for those policies.

<a id="webhook-configuring-acs_integrate-using-generic-webhooks"></a>

# Configuring integrations by using webhooks

Create a new integration in Red Hat Advanced Cluster Security for Kubernetes by using the webhook URL.

<div>

<div class="title">

Procedure

</div>

1.  In the RHACS portal, go to **Platform Configuration** → **Integrations**.

2.  Scroll down to the **Notifier Integrations** section and select **Generic Webhook**.

3.  Click **New integration**.

4.  Enter a name for **Integration name**.

5.  Enter the webhook URL in the **Endpoint** field.

6.  If your webhook receiver uses an untrusted certificate, enter a CA certificate in the **CA certificate** field. Otherwise, leave it blank.

    > [!NOTE]
    > The server certificate used by the webhook receiver must be valid for the endpoint DNS name. You can click **Skip TLS verification** to ignore this validation. Red Hat does not suggest turning off TLS verification. Without TLS verification, data could be intercepted by an unintended recipient.

7.  Optional: Click **Enable audit logging** to receive alerts about all the changes made in Red Hat Advanced Cluster Security for Kubernetes.

    > [!NOTE]
    > Red Hat suggests using separate webhooks for alerts and audit logs to handle these messages differently.

8.  To authenticate with the webhook receiver, enter details for one of the following:

    - **Username** and **Password** for basic HTTP authentication

    - Custom **Header**, for example: `Authorization: Bearer <access_token>`

9.  Use **Extra fields** to include additional key-value pairs in the JSON object that Red Hat Advanced Cluster Security for Kubernetes sends. For example, if your webhook receiver accepts objects from multiple sources, you can add `"source": "rhacs"` as an extra field and filter on this value to identify all alerts from Red Hat Advanced Cluster Security for Kubernetes.

10. Select **Test** to send a test message to verify that the integration with your generic webhook is working.

11. Select **Save** to create the configuration.

</div>

<a id="configure-policy-notifications_integrate-using-generic-webhooks"></a>

# Configuring policy notifications

Enable alert notifications for system policies.

<div>

<div class="title">

Procedure

</div>

1.  In the RHACS portal, go to **Platform Configuration** → **Policy Management**.

2.  Select one or more policies for which you want to send alerts.

3.  Under **Bulk actions**, select **Enable notification**.

4.  In the **Enable notification** window, select the **webhook** notifier.

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
