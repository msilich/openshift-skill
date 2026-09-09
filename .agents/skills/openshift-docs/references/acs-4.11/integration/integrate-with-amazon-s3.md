<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

You can integrate Red Hat Advanced Cluster Security for Kubernetes with Amazon S3 to enable data backups. You can use these backups for data restoration in the case of an infrastructure disaster or corrupt data. After you integrate with Amazon S3, you can schedule daily or weekly backups and perform manual on-demand backups.

<a id="integrate-amazon-s3-overview_integrate-with-amazon-s3"></a>

# Amazon S3 backup integration overview

The backup includes the entire Red Hat Advanced Cluster Security for Kubernetes database, which includes all configurations, resources, events, and certificates. Make sure to store backups securely.

<div class="important">

<div class="title">

</div>

- If you are using Red Hat Advanced Cluster Security for Kubernetes version 3.0.53 or older, the backup does not include certificates.

- If your Amazon S3 is part of an air-gapped environment, you must add your AWS root CA as a trusted certificate authority in Red Hat Advanced Cluster Security for Kubernetes.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Amazon S3](https://aws.amazon.com/s3/)

- [Adding a trusted certificate authority](../configuration/add-trusted-ca.md)

</div>

<a id="amazon-s3-configuring-acs_integrate-with-amazon-s3"></a>

# Configuring Amazon S3 integration in Red Hat Advanced Cluster Security for Kubernetes

To configure Amazon S3 backups, create a new integration in Red Hat Advanced Cluster Security for Kubernetes.

<div>

<div class="title">

Prerequisites

</div>

- An existing S3 Bucket. To create a new bucket with required permissions, see the "Creating a bucket" Amazon documentation topic.

- `Read`, `write`, and `delete` permissions for the S3 bucket, the **Access key ID**, and the **Secret access key**.

- If you are using **KIAM**, **kube2iam** or another proxy, then an **IAM role** that has the `read`, `write`, and `delete` permissions.

</div>

<div>

<div class="title">

Procedure

</div>

1.  In the RHACS portal, go to **Platform Configuration** → **Integrations**.

2.  Scroll down to the **External backups** section and select **Amazon S3**.

3.  Click **New Integration** (**`add`** icon).

4.  Enter a name for **Integration Name**.

5.  Enter the number of backups to retain in the **Backups To Retain** box.

6.  For **Schedule**, select the backup frequency as daily or weekly and the time to run the backup process.

7.  Enter the **Bucket** name where you want to store the backup.

8.  Optionally, enter an **Object Prefix** if you want to save the backups in a specific folder structure. For more information, see the "Working with object metadata" Amazon documentation topic.

9.  Enter the **Endpoint** for the bucket if you are using a non-public S3 instance, otherwise leave it blank.

10. Enter the **Region** for the bucket.

11. Turn on the **Use Container IAM Role** toggle or enter the **Access Key ID**, and the **Secret Access Key**.

12. Select **Test** to confirm that the integration with Amazon S3 is working.

13. Select **Create** to generate the configuration.

    Once configured, Red Hat Advanced Cluster Security for Kubernetes automatically backs up all data according to the specified schedule.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Creating a bucket in Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/user-guide/create-bucket.html)

- [Working with object metadata in Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingMetadata.html#object-keys)

</div>

<a id="perform-on-demand-backups-amazon-s3_integrate-with-amazon-s3"></a>

# Performing on-demand backups on Amazon S3

Use the RHACS portal to trigger manual backups of Red Hat Advanced Cluster Security for Kubernetes on Amazon S3.

<div>

<div class="title">

Prerequisites

</div>

- You must have already integrated Red Hat Advanced Cluster Security for Kubernetes with Amazon S3.

</div>

<div>

<div class="title">

Procedure

</div>

1.  In the RHACS portal, go to **Platform Configuration** → **Integrations**.

2.  Under the **External backups** section, click **Amazon S3**.

3.  Select the integration name for the S3 bucket where you want to do a backup.

4.  Click **Trigger Backup**.

    > [!NOTE]
    > Currently, when you select the **Trigger Backup** option, there is no notification. However, Red Hat Advanced Cluster Security for Kubernetes begins the backup task in the background.

</div>

<a id="additional-resources_integrate-with-amazon-s3"></a>

# Additional resources

- [Backing up Red Hat Advanced Cluster Security for Kubernetes](../backup_and_restore/backing-up-acs.md)

- [Restoring from a backup](../backup_and_restore/restore-acs.md)
