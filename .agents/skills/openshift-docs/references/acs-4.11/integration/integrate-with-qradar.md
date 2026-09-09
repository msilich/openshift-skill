<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

You can configure Red Hat Advanced Cluster Security for Kubernetes to send events to QRadar by configuring a generic webhook integration in RHACS.

The following steps represent a high-level workflow for integrating RHACS with QRadar:

1.  In RHACS:

    1.  Configure the generic webhook.

        > [!NOTE]
        > When configuring the integration in RHACS, in the **Endpoint** field, use the following example as a guide: `<URL to QRadar Box>:<Port of Integration>`.

    2.  Identify policies for which you want to send notifications, and update the notification settings for those policies.

2.  If QRadar does not automatically detect the log source, add an RHACS log source on the QRadar Console. For more information on configuring QRadar and RHACS, see the [Red Hat Advanced Cluster Security for Kubernetes](https://www.ibm.com/docs/en/dsm?topic=configuration-red-hat-advanced-cluster-security-kubernetes) IBM resource.

<a id="webhook-configuring-acs_integrate-with-qradar"></a>

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

<a id="configure-policy-notifications_integrate-with-qradar"></a>

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
