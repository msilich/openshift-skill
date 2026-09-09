<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Learn about the technical support options available for Red Hat Advanced Cluster Security for Kubernetes.

If you experience difficulty with a procedure described in this documentation, or with Red Hat Advanced Cluster Security for Kubernetes in general, visit the Red Hat Customer Portal. From the Customer Portal, you can:

- Search or browse through the Red Hat Knowledgebase of articles and solutions relating to Red Hat products.

- Submit a support case to Red Hat Support.

- Access other product documentation.

If you have a suggestion for improving the documentation or have identified an error, create a Jira issue against the **Red Hat Advanced Cluster Security for Kubernetes** product for the **Documentation** component. Ensure that you include specific details such as the section name and the version of Red Hat Advanced Cluster Security for Kubernetes for us to manage your feedback effectively.

<div>

<div class="title">

Additional resources

</div>

- [Red Hat Customer Portal](http://access.redhat.com)

- [Report a documentation issue](https://red.ht/rhacsdocsissue)

</div>

<a id="support-knowledgebase-about_getting-support"></a>

# About the Red Hat Knowledgebase

The Red Hat Knowledgebase provides content to help you make the most of Red Hat products and technologies. The Knowledgebase consists of articles, product documentation, and videos. These resources outline best practices for installing, configuring, and using Red Hat products. You can also search for solutions to known issues, with root cause descriptions and remedial steps.

<div>

<div class="title">

Additional resources

</div>

- [Red Hat Knowledgebase](https://access.redhat.com/knowledgebase)

</div>

<a id="support-knowledgebase-search_getting-support"></a>

# Searching the Red Hat Knowledgebase

If you have a Red Hat Advanced Cluster Security for Kubernetes issue, you can perform an initial search to find if a solution already exists within the Red Hat Knowledgebase.

<div>

<div class="title">

Prerequisites

</div>

- You have a Red Hat Customer Portal account.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Log in to the Red Hat Customer Portal.

2.  In the main Red Hat Customer Portal search field, input keywords and strings relating to the problem, including:

    - Red Hat Advanced Cluster Security for Kubernetes components (such as **etcd**)

    - Related procedure (such as **installation**)

    - Warnings, error messages, and other outputs related to explicit failures

3.  Click **Search**.

4.  Select the **Red Hat Advanced Cluster Security for Kubernetes** product filter.

5.  Select the **Knowledgebase** content type filter.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Red Hat Customer Portal](http://access.redhat.com)

</div>

<a id="generating-diagnostic-bundle_getting-support"></a>

# Generating a diagnostic bundle

You can generate a diagnostic bundle to help the support team analyze the status and health of Red Hat Advanced Cluster Security for Kubernetes components.

> [!NOTE]
> The diagnostic bundle is not encrypted. Depending on the number of clusters in your environment, the bundle size is between 100 KB and 1 MB.

<a id="generate-diagnostic-bundle-using-acs-portal_getting-support"></a>

## Generating a diagnostic bundle by using the RHACS portal

You can generate a diagnostic bundle by using the system health dashboard in the RHACS portal.

<div>

<div class="title">

Prerequisites

</div>

- To generate a diagnostic bundle, you need `read` permission for the `Administration` resource.

</div>

<div>

<div class="title">

Procedure

</div>

1.  In the RHACS portal, select **Platform Configuration** → **System Health**.

2.  On the **System Health** view header, click **Generate Diagnostic Bundle**.

3.  For the **Filter by clusters** drop-down menu, select the clusters for which you want to generate the diagnostic data.

4.  For **Filter by starting time**, specify the date and time (in UTC format) from which you want to include the diagnostic data.

5.  Click **Download Diagnostic Bundle**.

</div>

<a id="generate-diagnostic-bundle-using-roxctl-cli_getting-support"></a>

## Generating a diagnostic bundle by using the roxctl CLI

You can use the `roxctl` CLI to generate a diagnostic bundle. You need the Red Hat Advanced Cluster Security for Kubernetes (RHACS) administrator password or API token and central address.

<div>

<div class="title">

Prerequisites

</div>

- To generate a diagnostic bundle, you need `read` permission for the `Administration` resource.

- You must have configured the RHACS administrator password or API token and central address.

</div>

<div>

<div class="title">

Procedure

</div>

- To generate a diagnostic bundle by using the RHACS administrator password, perform the following steps:

  1.  Run the following command to configure the `ROX_PASSWORD` and `ROX_CENTRAL_ADDRESS` environment variables:

      ``` terminal
      $ export ROX_PASSWORD=<rox_password> && export ROX_CENTRAL_ADDRESS=<address>:<port_number>
      ```

      where:

      \<rox_password\>  
      Specifies the RHACS administrator password.

  2.  Run the following command to generate a diagnostic bundle by using the RHACS administrator password:

      ``` terminal
      $ roxctl -e "$ROX_CENTRAL_ADDRESS" -p "$ROX_PASSWORD" central debug download-diagnostics
      ```

- To generate a diagnostic bundle by using the API token, perform the following steps:

  1.  Run the following command to configure the `ROX_API_TOKEN` environment variable:

      ``` terminal
      $ export ROX_API_TOKEN=<api_token>
      ```

  2.  Run the following command to generate a diagnostic bundle by using the API token:

      ``` terminal
      $ roxctl -e "$ROX_CENTRAL_ADDRESS" central debug download-diagnostics
      ```

</div>

<a id="support-submitting-a-case_getting-support"></a>

# Submitting a support case

You can submit a support case to Red Hat Support for help with Red Hat Advanced Cluster Security for Kubernetes issues.

<div>

<div class="title">

Prerequisites

</div>

- You have access to the cluster.

- You have a Red Hat Customer Portal account.

- You have a OpenShift Platform Plus subscription.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Log in to the Red Hat Customer Portal and select **SUPPORT CASES** → **Open a case**.

2.  Select the appropriate category for your issue (such as **Defect / Bug**), product (**Red Hat Advanced Cluster Security for Kubernetes**), and product version (**4.11**, if this is not already autofilled).

3.  Review the list of suggested Red Hat Knowledgebase solutions for a potential match against the problem you are reporting. If the suggested articles do not address the issue, click **Continue**.

4.  Enter a concise but descriptive problem summary and further details about the symptoms you are experiencing and your expectations.

5.  Review the updated list of suggested Red Hat Knowledgebase solutions for a potential match against the problem you are reporting. Providing more information during the case creation process refines the list. If the suggested articles do not address the issue, click **Continue**.

6.  Ensure that the account information presented is as expected, and if not, change it.

7.  Upload the generated diagnostic bundle and click **Continue**.

8.  Input relevant case management details and click **Continue**.

9.  Preview the case details and click **Submit**.

</div>

<div>

<div class="title">

Additional resources

</div>

- [OpenShift Platform Plus](https://www.redhat.com/en/technologies/cloud-computing/openshift/platform-plus)

- [Red Hat Customer Portal](http://access.redhat.com)

</div>
