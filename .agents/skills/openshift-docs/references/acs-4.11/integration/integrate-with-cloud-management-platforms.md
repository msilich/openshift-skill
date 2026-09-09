<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

You can integrate Red Hat Advanced Cluster Security for Kubernetes (RHACS) with different cloud management platforms to discover potential clusters to secure. The cluster discovery aims to gain a detailed overview of the cluster assets already or not yet secured by RHACS.

<a id="cloud-management-platforms-overview_integrate-with-cloud-management-platforms"></a>

# Cloud management platform integration overview

RHACS integrates with cloud management platforms to discover potential clusters to secure and provides detailed visibility into cluster assets.

The clusters discovered from a cloud management platform are accessible from the **Platform Configuration** → **Clusters** → **Discovered clusters** page.

RHACS matches the discovered clusters against already secured clusters. Based on the result of the matching, a discovered cluster has one of the following statuses:

- **Secured**: RHACS secures the cluster.

- **Unsecured**: RHACS does not secure the cluster.

- **Undetermined**: The metadata collected from secured clusters is not enough for a unique match. The cluster is either secured or unsecured.

For successful cluster matching, ensure the following conditions:

- Update Sensors running on secured clusters to the latest version.

- Grant access to instance tags via the metadata service for secured clusters running on AWS. Sensors require access to the AWS EC2 instance tags to identify the cluster status.

You can integrate RHACS with the following cloud management platforms:

- Paladin Cloud

- Red Hat OpenShift Cluster Manager

<div>

<div class="title">

Additional resources

</div>

- [Access to instance tags via the metadata service](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html#allow-access-to-tags-in-IMDS)

- [Paladin Cloud](https://paladincloud.io/)

- [Red Hat OpenShift Cluster Manager](https://console.redhat.com/openshift/)

</div>

<a id="cloud-management-platforms-paladin-cloud_integrate-with-cloud-management-platforms"></a>

# Configuring Paladin Cloud integration

To discover cluster assets from Paladin Cloud, create a new integration in Red Hat Advanced Cluster Security for Kubernetes.

<div>

<div class="title">

Prerequisites

</div>

- A Paladin Cloud account.

- A Paladin Cloud API token.

</div>

<div>

<div class="title">

Procedure

</div>

1.  In the RHACS portal, go to **Platform Configuration** → **Integrations**.

2.  Scroll down to the **Cloud source integrations** section and select **Paladin Cloud**.

3.  Click **New integration**.

4.  Enter a name for **Integration name**.

5.  Enter the Paladin Cloud API endpoint for **Paladin Cloud endpoint**. The default is `https://api.paladincloud.io`.

6.  Enter the Paladin Cloud API token for **Paladin Cloud token**.

7.  Select **Test** to confirm that authentication is working.

8.  Select **Create** to generate the configuration.

    Once configured, Red Hat Advanced Cluster Security for Kubernetes discovers cluster assets from your connected Paladin Cloud account.

</div>

<a id="cloud-management-platforms-ocm_integrate-with-cloud-management-platforms"></a>

# Configuring Red Hat OpenShift Cluster Manager integration

To discover cluster assets from Red Hat OpenShift Cluster Manager, create a new integration in Red Hat Advanced Cluster Security for Kubernetes.

<div>

<div class="title">

Prerequisites

</div>

- A Red Hat account.

- A Red Hat service account.

</div>

<div>

<div class="title">

Procedure

</div>

1.  In the RHACS portal, go to **Platform Configuration** → **Integrations**.

2.  Scroll down to the **Cloud source integrations** section and select **Red Hat OpenShift Cluster Manager**.

3.  Click **New integration**.

4.  Enter a name for **Integration name**.

5.  Enter the Red Hat OpenShift Cluster Manager API endpoint for **Endpoint**. The default is `https://api.openshift.com`.

6.  Enter the Red Hat service account credentials for **Client ID** and **Client secret**.

7.  Select **Test** to confirm that authentication is working.

8.  Select **Create** to generate the configuration.

    Once configured, Red Hat Advanced Cluster Security for Kubernetes discovers cluster assets from your connected Red Hat account.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Red Hat service account](https://console.redhat.com/iam/service-accounts)

</div>
