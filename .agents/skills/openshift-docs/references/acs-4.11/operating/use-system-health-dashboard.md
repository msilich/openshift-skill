<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

The Red Hat Advanced Cluster Security for Kubernetes (RHACS) system health dashboard provides a single interface for viewing health-related information about the RHACS components.

<a id="analyzing-and-managing-the-system-health-information_use-system-health-dashboard"></a>

# Analyzing and managing the system health information

You can view all the health-related information associated with the Red Hat Advanced Cluster Security for Kubernetes (RHACS) components on the **System Health** page.

<div>

<div class="title">

Procedure

</div>

1.  In the RHACS portal, click **Platform Configuration** → **System Health**.

2.  Optional: To download the administration usage data as a CSV file, perform the following steps:

    1.  Click **Show administration usage**.

        > [!NOTE]
        > The **Administration usage** page displays the administration usage data you have collected, including the number of secured Kubernetes nodes and CPU units. The current usage reflects the last metrics received from Sensors, with a delay of about 5 minutes.
        >
        > Maximum usage is aggregated hourly and only includes clusters that are still connected. The date range is inclusive and matches your time zone. This data is not sent to Red Hat or displayed as Prometheus metrics.

    2.  Enter the start and end date in `YYYY-MM-DD` format. If you do not specify the start and end date, the first and last day of the month is selected automatically.

    3.  To download the administration usage data, click **Download CSV**.

3.  Optional: To download the platform data, perform the following steps:

    1.  Click **Generate diagnostic bundle**.

    2.  Optional: Choose the appropriate method to filter the platform data that you want to include in the compressed file:

        - To filter the platform data based on specific clusters, select one or more clusters from the **Filter by clusters** drop-down list. If you do not select a cluster, all clusters are selected automatically.

        - To filter the platform data according to the start time, enter a time in coordinated universal time (UTC) format, `yyyy-mm-ddThh:mmZ`. If you do not specify a start time, the diagnostic bundle includes the platform data for the last 20 minutes.

    3.  To download the platform data, click **Download diagnostic bundle**.

4.  Optional: To view the **Cluster status**, **Sensor upgrade**, or **Credential expiration** information associated with one or more clusters, perform the following steps:

    1.  Click **View clusters**.

    2.  To display further details on a cluster, click on the cluster name.

    3.  You can find all the status information associated with the selected cluster in the **Cluster summary** section.

    4.  Click **Next**.

    5.  Optional: To download the required YAML file to update your Helm values, click **Download Helm values**.

    6.  Click **Finish**.

5.  Optional: To update the certificate associated with the RHACS components such as Central, StackRox Scanner, or Scanner V4, perform the following steps:

    1.  Scroll down to locate the component for which you want to update the certificate.

    2.  Click **Download YAML**.

    3.  Optional: To reissue the internal certificates, perform the following steps:

        1.  Click **Reissuing internal certificates**.

        2.  Follow the instructions in the Red Hat documentation to apply the YAML and complete the reissue.

</div>

<a id="system-health-dashboard-page-overview_use-system-health-dashboard"></a>

# System health dashboard page overview

The **System Health** dashboard page organizes information into the following groups:

Cluster status  
Indicates the overall status of the cluster, and the status of essential Red Hat Advanced Cluster Security for Kubernetes (RHACS) components such as Sensor, Collector and Admission Controller.

Sensor upgrade  
Indicates the status of any pending or in-progress upgrades for Sensor.

Credential expiration  
Indicates the expiration date of the critical credentials.

StackRox Scanner Vulnerability Definitions  
Indicates the status of the vulnerability definitions database that StackRox Scanner uses.

Scanner V4 Vulnerabilities  
Indicates the status of the vulnerability definitions database that Scanner V4 uses.

Image Integrations  
Indicates the status of integrated image registries and scanners.

Notifier Integrations  
Indicates the status of any notifiers that you have integrated.

Backup Integrations  
Indicates the status of any backup providers that you have integrated.

Declarative configuration  
Indicates the status and consistency of the declarative configurations.

Central certificate  
Indicates the expiration date of the Central certificate.

StackRox Scanner certificate  
Indicates the expiration date of the StackRox Scanner certificate.

Scanner V4 certificate  
Indicates the expiration date of the Scanner V4 certificate.

<a id="image-integrations-section_use-system-health-dashboard"></a>

## Image Integrations section

The **Image Integrations** section organizes the information into the following groups:

Name  
Indicates the name of the integrated image.

Label  
Indicates a descriptive label associated with the integration for additional context.

Error message  
Indicates any issues or errors that the integration encounters.

Date  
Indicates the timestamp of the last health check or status update for the integration.

<a id="administration-usage-page-overview_use-system-health-dashboard"></a>

# Administration usage page overview

When you click **Show administration usage** in the **System Health** page, you can view the product usage data for the number of secured Kubernetes nodes and CPU units for secured clusters based on metrics collected from Sensors. You can use this information to estimate Red Hat Advanced Cluster Security for Kubernetes (RHACS) consumption data for reporting.

For more information on how CPU units are defined in Kubernetes, see [CPU resource units](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/#meaning-of-cpu) (Kubernetes documentation).

> [!NOTE]
> OpenShift Container Platform provides its own usage reports. You can use this information with self-managed Kubernetes systems.

RHACS provides the following usage data in the web portal and API:

Currently secured  
CPU units  
Indicates the number of Kubernetes CPU units that your RHACS secured clusters uses, as of the latest metrics collection.

Node count  
Indicates the number of Kubernetes nodes that RHACS secures, as of the latest metrics collection.

Maximum secured  
CPU units  
Indicates the maximum number of CPU units that your RHACS secured clusters use, measured hourly and aggregated for the time period that you specified.

Node count  
Indicates the maximum number of Kubernetes nodes that RHACS secures, measured hourly and aggregated for the time period that you specified.

CPU units observation date  
Indicates the date on which the maximum secured CPU units data was collected.

Node count observation date  
Indicates the date on which the maximum secured node count data was collected.
