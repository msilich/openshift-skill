<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

The decision to opt out of telemetry should be based on your specific needs and requirements, as well as any applicable regulations or policies that you need to comply with.

<a id="consequences-of-disabling-telemetry_opting-out-telemetry"></a>

# Consequences of disabling Telemetry

In Red Hat Advanced Cluster Security for Kubernetes (RHACS) version 4.0, you can opt out of Telemetry. However, telemetry is embedded as a core component, so opting out is strongly discouraged. Opting out of telemetry limits the ability of Red Hat to understand how everyone uses the product and which areas to prioritize for improvements.

<a id="disabling-telemetry_opting-out-telemetry"></a>

# Disabling Telemetry

If you have configured Telemetry by setting the key in your environment, you can disable Telemetry data collection from the Red Hat Advanced Cluster Security for Kubernetes (RHACS) user interface (UI).

<div>

<div class="title">

Procedure

</div>

1.  In the RHACS portal, go to **Platform Configuration \> System Configuration**.

2.  In the **System Configuration** header, click **Edit**.

3.  Scroll down and ensure that **Online Telemetry Data Collection** is set to **Disabled**.

</div>
