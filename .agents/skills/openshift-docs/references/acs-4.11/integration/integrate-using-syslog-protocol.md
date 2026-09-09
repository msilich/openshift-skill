<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

[Syslog](https://tools.ietf.org/html/rfc5424) is an event logging protocol that applications use to send messages to a central location, such as a SIEM or a syslog collector, for data retention and security investigations. With Red Hat Advanced Cluster Security for Kubernetes, you can send alerts and audit events using the syslog protocol.

<div class="note">

<div class="title">

</div>

- Forwarding events by using the syslog protocol requires the Red Hat Advanced Cluster Security for Kubernetes version 3.0.52 or newer.

- When you use the syslog integration, Red Hat Advanced Cluster Security for Kubernetes forwards both violation alerts that you configure and all audit events.

- Currently, Red Hat Advanced Cluster Security for Kubernetes only supports **CEF** (Common Event Format).

</div>

The following steps represent a high-level workflow for integrating Red Hat Advanced Cluster Security for Kubernetes with a syslog events receiver:

1.  Set up a syslog events receiver to receive alerts.

2.  Use the receiver’s address and port number to set up notifications in the Red Hat Advanced Cluster Security for Kubernetes.

After the configuration, Red Hat Advanced Cluster Security for Kubernetes automatically sends all violations and audit events to the configured syslog receiver.

<a id="syslog-configuring-acs_integrate-using-syslog-protocol"></a>

# Configuring syslog integration with Red Hat Advanced Cluster Security for Kubernetes

Create a new syslog integration in Red Hat Advanced Cluster Security for Kubernetes (RHACS).

<div>

<div class="title">

Procedure

</div>

1.  In the RHACS portal, click the **Platform Configuration** → **Integrations** → **Notifier** tab.

2.  Select **Syslog**.

3.  Click **New integration**.

4.  In the **Create integration** page, provide the following information:

    1.  Enter a name for your integration.

    2.  Select the **Logging facility** value from `local0` through `local7`.

    3.  Enter your **Receiver host** address and **Receiver port** number.

    4.  Enter a value for the **Maximum message size**.

        Enter a value between `0` and `1048576`, which corresponds to the number of bytes used to chunk messages. You can adjust the value by using the up and down arrows in the spin button.

        If you do not want to chunk messages, enter `0`.

    5.  Select the appropriate **Message format**:

        - If you are creating a new integration, select **CEF**.

        - If you have an existing integration that relies on the old behavior, select **CEF (legacy field order)**.

    6.  Select the appropriate checkboxes:

        - If you are using TLS, select the **Use TLS** checkbox.

        - If your syslog receiver uses a certificate that is not trusted, select the **Disable TLS Certificate Validation (insecure)** checkbox.

    7.  To add extra fields, click **Add new extra field**.

        For example, if your syslog receiver accepts objects from multiple sources, type `source` and `rhacs` in the **Key** and **Value** fields.

        You can filter by using the custom values in your syslog receiver to identify all alerts from RHACS.

5.  To send a test message to verify that the integration with your generic webhook is working, click **Test**.

6.  To create the configuration, click **Save**.

</div>
