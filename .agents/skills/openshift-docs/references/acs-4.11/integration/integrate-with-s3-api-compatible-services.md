<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Red Hat Advanced Cluster Security for Kubernetes can be integrated with S3 API compatible services to enable data backups. These backups can be used for data restoration in the case of an infrastructure disaster or corrupt data. After integrating with the S3 API compatible provider, you can schedule daily or weekly backups and do manual on-demand backups.

The backup includes the entire RHACS database, which includes all configurations, resources, events, and certificates. Make sure that backups are stored securely.

<div class="important">

<div class="title">

</div>

- To back up to Amazon S3, use the dedicated [Amazon S3](integrate-with-amazon-s3.md) integration to ensure the best compatibility.

- Red Hat does not test this integration with every S3 API compatible provider, so the integration is not guaranteed to work with all providers.

</div>

<a id="s3-api-compatible-services-configuring-acs_integrate-with-s3-api-compatible-services"></a>

# Configuring S3 API compatible integrations in Red Hat Advanced Cluster Security for Kubernetes

To configure S3 API compatible backups, create a new integration in Red Hat Advanced Cluster Security for Kubernetes.

<div>

<div class="title">

Prerequisites

</div>

- You have configured an existing S3 bucket. To create a new bucket with required permissions, see your S3 provider documentation.

- You have `read`, `write`, and `delete` permissions for the S3 bucket, the **Access key ID**, and the **Secret access key**.

</div>

<div>

<div class="title">

Procedure

</div>

1.  In the RHACS portal, go to **Platform Configuration** → **Integrations**.

2.  Scroll down to the **External backups** section and select **S3 API Compatible**.

3.  Click **New Integration**.

4.  Enter a name for **Integration Name**.

5.  Enter the number of backups to retain in the **Backups To Retain** box.

6.  For **Schedule**, select the backup frequency as daily or weekly, and select the time to run the backup process.

7.  Enter the **Bucket** name where you want to store the backup.

8.  Optionally, enter an **Object Prefix** if you want to save the backups in a specific folder structure.

9.  Enter the **Endpoint** under which the S3 compatible service is reachable. If no scheme is specified, the default, `https`, is used.

10. Enter the **Region** for the bucket. Consult your provider’s documentation to enter the correct region.

11. Select the **URL style**:

    - **Virtual hosted** style buckets are addressed as *https://\<bucket\>.\<endpoint\>*.  

    - **Path** style buckets are addressed as *https://\<endpoint\>/\<bucket\>*.

12. Enter the **Access Key ID** and the **Secret Access Key**.

13. Select **Test** to confirm that the integration with the S3 is working.

14. Select **Create** to generate the configuration.

</div>

After the integration is configured, RHACS automatically backs up all data according to the specified schedule.

<a id="perform-on-demand-backups-s3-api-compatible-services_integrate-with-s3-api-compatible-services"></a>

# Performing on-demand backups on an S3 API compatible bucket

Use the Red Hat Advanced Cluster Security for Kubernetes portal to trigger manual backups of RHACS to an S3 API compatible bucket.

<div>

<div class="title">

Prerequisites

</div>

- You have integrated RHACS with an S3 API compatible service.

</div>

<div>

<div class="title">

Procedure

</div>

1.  In the RHACS portal, go to **Platform Configuration** → **Integrations**.

2.  In the **External backups** section, click **S3 API Compatible**.

3.  Select the integration name for the S3 bucket where you want to do a backup.

4.  Click **Trigger backup**.

</div>

> [!NOTE]
> When you select **Trigger backup**, there is no notification. However, RHACS begins the backup task in the background.

<a id="_additional_resources"></a>

# Additional resources

- [Backing up Red Hat Advanced Cluster Security for Kubernetes](../backup_and_restore/backing-up-acs.md)

- [Restoring from a backup](../backup_and_restore/restore-acs.md)
