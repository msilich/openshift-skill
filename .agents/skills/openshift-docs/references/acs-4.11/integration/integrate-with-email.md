<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

With Red Hat Advanced Cluster Security for Kubernetes (RHACS), you can configure your existing email provider to send notifications about policy violations. If you use Red Hat Advanced Cluster Security Cloud Service (RHACS Cloud Service), you can use your existing email provider or the built-in email notifier to send email notifications.

You can use the `Default recipient` field to forward alerts from RHACS and the RHACS Cloud Service to an email address. Otherwise, you can use annotations to define an audience and tell them about policy violations associated with a specific deployment or namespace.

<a id="integrate-email-rhacs-overview_integrate-with-email"></a>

# Integrating with email on RHACS

You can use email as a notification method by forwarding alerts from RHACS.

<a id="configure-acs-email_integrate-with-email"></a>

## Configuring the email plugin

The RHACS notifier can send email to a recipient specified in the integration, or it can use annotations to find the recipient.

> [!IMPORTANT]
> If you are using RHACS Cloud Service, it blocks port `25` by default. Configure your mail server to use port `587` or `465` to send email notifications.

<div>

<div class="title">

Procedure

</div>

1.  Go to **Platform Configuration** → **Integrations**.

2.  Under the **Notifier Integrations** section, select **Email**.

3.  Select **New Integration**.

4.  In the **Integration name** field, enter a name for your email integration.

5.  In the **Email server** field, enter the address of your email server. The email server address includes fully qualified domain name (FQDN) and the port number; for example, `smtp.example.com:465`.

6.  Optional: If you are using an unauthenticated Simple Mail Transfer Protocol (SMTP), select **Enable unauthenticated SMTP**. This is insecure and not recommended, but some integrations might require it. For example, you might need to enable this option if you use an internal server for notifications that does not require authentication.

    > [!NOTE]
    > You cannot change an existing email integration that uses authentication to enable unauthenticated SMTP. You must delete the existing integration and create a new one with **Enable unauthenticated SMTP** selected.

7.  Enter the user name and password of a service account for authentication.

8.  Optional: Enter the name that you want to appear in the `FROM` header of email notifications in the **From** field; for example, `Security Alerts`.

9.  Specify the email address that you want to appear in the `SENDER` header of email notifications in the **Sender** field.

10. Specify the email address that will receive the notifications in the **Default recipient** field.

11. Optional: Enter an annotation key in **Annotation key for recipient**. You can use annotations to dynamically find an email recipient. To do this:

    1.  Add an annotation similar to the following example in your namespace or deployment YAML file, where `email` is the `Annotation key` that you specify in your email integration. You can create an annotation for the deployment or the namespace.

            annotations:
              email: <email_address>

    2.  Use the annotation key `email` in the **Annotation key for recipient** field.

        If you configured the deployment or namespace with an annotation, the RHACS sends the alert to the email specified in the annotation. Otherwise, it sends the alert to the default recipient.

        > [!NOTE]
        > The following rules govern how RHACS determines the recipient of an email notification:
        >
        > - If the deployment has an annotation key, the annotation’s value overrides the default value.
        >
        > - If the namespace has an annotation key, the namespace’s value overrides the default value.
        >
        > - If a deployment has an annotation key and a defined audience, RHACS sends an email to the audience specified in the key.
        >
        > - If a deployment does not have an annotation key, RHACS checks the namespace for an annotation key and sends an email to the specified audience.
        >
        > - If no annotation keys exist, RHACS sends an email to the default recipient.

12. Optional: Select **Disable TLS certificate validation (insecure)** to send email without TLS. You should not disable TLS unless you are using StartTLS.

    > [!NOTE]
    > Use TLS for email notifications. Without TLS, all email is sent unencrypted.

13. Optional: To use StartTLS, select either **Login** or **Plain** from the **Use STARTTLS (requires TLS to be disabled)** drop-down menu.

    > [!IMPORTANT]
    > With StartTLS, credentials are passed in plain text to the email server before the session encryption is established.
    >
    > - StartTLS with the **Login** parameter sends authentication credentials in a `base64` encoded string.
    >
    > - StartTLS with the **Plain** parameter sends authentication credentials to your mail relay in plain text.

14. Optional: Enter a hostname to use for the SMTP HELO/EHLO messages sent during the SMTP handshake. If you do not specify a hostname, `localhost` is used by default.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Configuring delivery destinations and scheduling](../operating/manage-vulnerabilities/vulnerability-management.md) :!context:

</div>

<a id="configure-policy-notifications_rhacs"></a>

## Configuring policy notifications

Enable alert notifications for system policies.

<div>

<div class="title">

Procedure

</div>

1.  In the RHACS portal, go to **Platform Configuration** → **Policy Management**.

2.  Select one or more policies for which you want to send alerts.

3.  Under **Bulk actions**, select **Enable notification**.

4.  In the **Enable notification** window, select the **Email** notifier.

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

<a id="integrate-email-rhacs-cloud-overview_integrate-with-email"></a>

# Integrating with email on RHACS Cloud Service

You can use your existing email provider or the built-in email notifier in RHACS Cloud Service to send email alerts about policy violations.

You can use either of the following methods:

- To use your own email provider, you must configure the email provider as described in "Configuring the email plugin".

- To use the built-in email notifier, you must configure the RHACS Cloud Service email plugin.

<div>

<div class="title">

Additional resources

</div>

- [Configuring the email plugin](integrate-with-email.md#configure-acs-email_integrate-with-email)

</div>

<a id="configure-acscs-email_integrate-with-email"></a>

## Configuring the RHACS Cloud Service email plugin

The RHACS Cloud Service notifier sends an email to a recipient. You can specify the recipient in the integration, or RHACS Cloud Service can use annotation keys to find the recipient.

<div class="important">

<div class="title">

</div>

- You can only send 250 emails per 24-hour rolling period. If you exceed this limit, RHACS Cloud Service sends emails only after the 24-hour period ends.

- Because of rate limits, Red Hat recommends using email notifications only for critical alerts or vulnerability reports.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Go to **Platform Configuration** → **Integrations**.

2.  Under the **Notifier Integrations** section, select **RHACS Cloud Service Email**.

3.  Select **New Integration**.

4.  In the **Integration name** field, enter a name for your email integration.

5.  Specify the email address to which you want to send the email notifications in the **Default recipient** field.

6.  Optional: Enter an annotation key in **Annotation key for recipient**. You can use annotations to dynamically find an email recipient. To do this:

    1.  Add an annotation similar to the following example in your namespace or deployment YAML file, where `email` is the `Annotation key` that you specify in your email integration. You can create an annotation for the deployment or the namespace.

            annotations:
              email: <email_address>

    2.  Use the annotation key `email` in the **Annotation key for recipient** field.

        If you configured the deployment or namespace with an annotation, the RHACS Cloud Service sends the alert to the email specified in the annotation. Otherwise, it sends the alert to the default recipient.

        > [!NOTE]
        > The following rules govern how RHACS Cloud Service determines the recipient of an email notification:
        >
        > - If the deployment has an annotation key, the annotation’s value overrides the default value.
        >
        > - If the namespace has an annotation key, the namespace’s value overrides the default value.
        >
        > - If a deployment has an annotation key and a defined audience, RHACS Cloud Service sends an email to the audience specified in the key.
        >
        > - If a deployment does not have an annotation key, RHACS Cloud Service checks the namespace for an annotation key and sends an email to the specified audience.
        >
        > - If no annotation keys exist, RHACS Cloud Service sends an email to the default recipient.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Configuring delivery destinations and scheduling](../operating/manage-vulnerabilities/vulnerability-management.md) :!context:

</div>

<a id="configure-policy-notifications_rhacs-cloud-service"></a>

## Configuring policy notifications

Enable alert notifications for system policies.

<div>

<div class="title">

Procedure

</div>

1.  In the RHACS portal, go to **Platform Configuration** → **Policy Management**.

2.  Select one or more policies for which you want to send alerts.

3.  Under **Bulk actions**, select **Enable notification**.

4.  In the **Enable notification** window, select the **RHACS Cloud Service Email** notifier.

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
