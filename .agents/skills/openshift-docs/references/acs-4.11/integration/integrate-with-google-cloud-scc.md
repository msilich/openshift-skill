<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

If you are using [Google Cloud Security Command Center](https://cloud.google.com/security-command-center/) (Cloud SCC), you can forward alerts from Red Hat Advanced Cluster Security for Kubernetes to Cloud SCC. This guide explains how to integrate Red Hat Advanced Cluster Security for Kubernetes with Cloud SCC.

The following steps represent a high-level workflow for integrating Red Hat Advanced Cluster Security for Kubernetes with Cloud SCC.

1.  Register a new security source with Google Cloud.

2.  Provide the source ID and service account key to Red Hat Advanced Cluster Security for Kubernetes.

3.  Identify the policies you want to send notifications for, and update the notification settings for those policies.

<a id="configure-google-cloud-scc_integrate-with-google-cloud-scc"></a>

# Configuring Google Cloud SCC

Start by adding Red Hat Advanced Cluster Security for Kubernetes as a trusted Cloud SCC source.

<div>

<div class="title">

Procedure

</div>

1.  Follow the [Adding vulnerability and threat sources to Cloud Security Command Center](https://cloud.google.com/security-command-center/docs/how-to-security-sources) guide and add Red Hat Advanced Cluster Security for Kubernetes as a trusted Cloud SCC source. Make a note of the **Source ID** that Google Cloud creates for your Red Hat Advanced Cluster Security for Kubernetes integration. If you do not see a source ID after registering, you can find it on the [Cloud SCC Security Sources page](https://console.cloud.google.com/security/command-center/settings/source-management).

2.  Create a key for the service account you created, or the existing account you used, in the previous step. See Google Cloud’s guide to [creating and managing service account keys](https://cloud.google.com/iam/docs/creating-managing-service-account-keys) for details.

</div>

<a id="google-cloud-scc-configuring-acs_integrate-with-google-cloud-scc"></a>

# Configuring Red Hat Advanced Cluster Security for Kubernetes for integrating with Google Cloud SCC

You can create a new Google Cloud SCC integration in Red Hat Advanced Cluster Security for Kubernetes by using the source ID and a Google service account.

<div>

<div class="title">

Prerequisites

</div>

- A **service account** with the `Security Center Findings Editor` IAM role on the organization level. See [Access control with IAM](https://cloud.google.com/security-command-center/docs/access-control) for more information.

- Either a [workload identity](https://cloud.google.com/kubernetes-engine/docs/how-to/workload-identity) or a **Service account key (JSON)** for the service account. See [Creating a service account](https://cloud.google.com/iam/docs/creating-managing-service-accounts#creating) and [Creating service account keys](https://cloud.google.com/iam/docs/creating-managing-service-account-keys#creating_service_account_keys) for more information.

</div>

<div>

<div class="title">

Procedure

</div>

1.  In the RHACS portal, go to **Platform Configuration** → **Integrations**.

2.  Scroll down to the **Notifier Integrations** section and select **Google Cloud SCC**.

3.  Click **New Integration** (**`add`** icon).

4.  Enter a name for **Integration Name**.

5.  Enter the **Cloud SCC Source ID**.

6.  When using a workload identity, check **Use workload identity**. Otherwise, enter the contents of your service account key file into the **Service account key (JSON)** field.

7.  Select **Create** to generate the configuration.

</div>

<a id="configure-policy-notifications_integrate-with-google-cloud-scc"></a>

# Configuring policy notifications

Enable alert notifications for system policies.

<div>

<div class="title">

Procedure

</div>

1.  In the RHACS portal, go to **Platform Configuration** → **Policy Management**.

2.  Select one or more policies for which you want to send alerts.

3.  Under **Bulk actions**, select **Enable notification**.

4.  In the **Enable notification** window, select the **Google Cloud SCC** notifier.

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
