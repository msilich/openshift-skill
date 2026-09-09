<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

You can integrate with Google Cloud Storage (GCS) to enable data backups. You can use these backups for data restoration in the case of an infrastructure disaster, or corrupt data.

<a id="google-cloud-storage-integration-overview_integrate-with-google-cloud-storage"></a>

# Google Cloud Storage integration overview

After integrating with Google Cloud Storage, you can schedule daily or weekly backups and perform manual on-demand backups.

The backup includes the Red Hat Advanced Cluster Security for Kubernetes entire database, which includes all configurations, resources, events, and certificates. Make sure that you store backups securely.

> [!NOTE]
> If you are using Red Hat Advanced Cluster Security for Kubernetes version 3.0.53 or older, the backup does not include certificates.

<a id="google-cloud-storage-configuring-acs_integrate-with-google-cloud-storage"></a>

# Configuring Red Hat Advanced Cluster Security for Kubernetes

To configure data backups on Google Cloud Storage (GCS), create an integration in Red Hat Advanced Cluster Security for Kubernetes. Once configured, Red Hat Advanced Cluster Security for Kubernetes automatically backs up all data according to the specified schedule.

<div>

<div class="title">

Prerequisites

</div>

- An existing **bucket**. To create a new bucket, see "Creating storage buckets" in the official Google Cloud Storage documentation.

- A **service account** with the `Storage Object Admin` IAM role in the storage bucket you want to use. See "Using Cloud IAM permissions" for more information.

- Either a workload identity or a **Service account key (JSON)** for the service account. See "Creating a service account" and "Creating service account keys" for more information.

</div>

<div>

<div class="title">

Procedure

</div>

1.  In the RHACS portal, go to **Platform Configuration** → **Integrations**.

2.  Scroll down to the **External backups** section and select **Google Cloud Storage**.

3.  Click **New Integration** (**`add`** icon).

4.  Enter a name for **Integration Name**.

5.  Enter the number of backups to retain in the **Backups To Retain** box.

6.  For **Schedule**, select the backup frequency (daily or weekly) and the time to run the backup process.

7.  Enter the **Bucket** name in which you want to store the backup.

8.  When using a workload identity, check **Use workload identity**. Otherwise, enter the contents of your service account key file into the **Service account key (JSON)** field.

9.  Select **Test** to confirm that the integration with GCS is working.

10. Select **Create** to generate the configuration.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Google Cloud Storage](https://cloud.google.com/storage/)

- [Creating storage buckets](https://cloud.google.com/storage/docs/creating-buckets)

- [Using Cloud IAM permissions](https://cloud.google.com/storage/docs/access-control/using-iam-permissions)

- [Workload identity](https://cloud.google.com/kubernetes-engine/docs/how-to/workload-identity)

- [Creating a service account](https://cloud.google.com/iam/docs/creating-managing-service-accounts#creating)

- [Creating service account keys](https://cloud.google.com/iam/docs/creating-managing-service-account-keys#creating_service_account_keys)

</div>

<a id="perform-on-demand-backups-google-cloud-storage_integrate-with-google-cloud-storage"></a>

## Perform on-demand backups on Google Cloud Storage

Uses the RHACS portal to trigger manual backups of Red Hat Advanced Cluster Security for Kubernetes on Google Cloud Storage.

<div>

<div class="title">

Prerequisites

</div>

- You must have already integrated Red Hat Advanced Cluster Security for Kubernetes with Google Cloud Storage.

</div>

<div>

<div class="title">

Procedure

</div>

1.  In the RHACS portal, go to **Platform Configuration** → **Integrations**.

2.  Under the **External backups** section, click **Google Cloud Storage**.

3.  Select the integration name for the GCS bucket in which you want to do a backup.

4.  Click **Trigger Backup**.

    > [!NOTE]
    > Currently, when you select the **Trigger Backup** option, there is no notification. However, Red Hat Advanced Cluster Security for Kubernetes begins the backup task in the background.

</div>

<a id="additional-resources_integrate-with-google-cloud-storage"></a>

# Additional resources

- [Backing up Red Hat Advanced Cluster Security for Kubernetes](../backup_and_restore/backing-up-acs.md)

- [Restoring from a backup](../backup_and_restore/restore-acs.md)
