<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

To resolve issues with your OpenShift Container Platform cluster, you can search the Red Hat Knowledgebase, submit a support case, and use remote health monitoring tools.

# Get support

Red Hat offers several support channels to help you troubleshoot issues and get the most from OpenShift Container Platform.

From the Red Hat Customer Portal, you can:

- Search or browse through the Red Hat Knowledgebase of articles and solutions about Red Hat products.

- Submit a support case to Red Hat Support.

- Access other product documentation.

To identify issues with your cluster, you can use Red Hat Lightspeed in [OpenShift Cluster Manager](https://console.redhat.com/openshift). Red Hat Lightspeed provides details about issues and, if available, information about how to solve a problem.

To suggest improvements or report errors, give specific details such as the section name and OpenShift Container Platform version.

# About the Red Hat Knowledgebase

The Red Hat Knowledgebase helps you get the most from Red Hat products and technologies.

It includes articles, product documentation, and videos that outline best practices for installing, configuring, and using Red Hat products. You can also search for solutions to known issues. Each solution has a root cause description and steps to fix the problem.

<div>

<div class="title">

Additional resources

</div>

- [Red Hat Knowledgebase](https://access.redhat.com/knowledgebase)

</div>

# Search the Red Hat Knowledgebase

Search the Red Hat Knowledgebase to find solutions to known issues and resolve problems quickly without opening a support case.

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

1.  Log in to the [Red Hat Customer Portal](http://access.redhat.com).

2.  Click **Search**.

3.  In the search field, input keywords and strings relating to the problem, including:

    - OpenShift Container Platform components (such as **etcd**)

    - Related procedure (such as **installation**)

    - Warnings, error messages, and other outputs related to explicit failures

4.  Click the **Enter** key.

5.  Optional: Select the **OpenShift Container Platform** product filter.

6.  Optional: Select the **Documentation** content type filter.

</div>

# Submitting a support case

If you cannot resolve an OpenShift Container Platform issue by using the Red Hat Knowledgebase, submit a support case to get direct help from Red Hat Support.

<div>

<div class="title">

Prerequisites

</div>

- You have access to the cluster as a user with the `cluster-admin` role.

- You have installed the OpenShift CLI (`oc`).

- You have a Red Hat Customer Portal account.

- You have a Red Hat Standard or Premium subscription.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Log in to [the **Customer Support** page](https://access.redhat.com/support/cases/#/case/list) of the Red Hat Customer Portal.

2.  Click **Get support**.

3.  On the **Cases** tab of the **Customer Support** page:

    1.  Optional: Change the pre-filled account and owner details if needed.

    2.  Select the appropriate category for your issue, such as **Bug or Defect**, and click **Continue**.

4.  Enter the following information:

    1.  In the **Summary** field, enter a concise but descriptive problem summary and further details about the symptoms that you experience and your expectations.

    2.  Select **OpenShift Container Platform** from the **Product** drop-down menu.

    3.  Select **4.20** from the **Version** drop-down.

5.  Review the list of suggested Red Hat Knowledgebase solutions for a potential match against the problem that you are reporting. If the suggested articles do not address the issue, click **Continue**.

6.  Review the updated list of suggested Red Hat Knowledgebase solutions for a potential match against the problem that you are reporting. The list updates as you give more information during the case creation process. If the suggested articles do not address the issue, click **Continue**.

7.  Ensure that the account information presented is as expected, and if not, change it as needed.

8.  Check that the autofilled OpenShift Container Platform Cluster ID is correct. If it is not, manually obtain your cluster ID.

    - To manually obtain your cluster ID using the OpenShift Container Platform web console:

      1.  Navigate to **Home** → **Overview**.

      2.  Find the value in the **Cluster ID** field of the **Details** section.

    - Or, open a new support case from the OpenShift Container Platform web console, which automatically fills in your cluster ID.

      1.  From the toolbar, navigate to **(?) Help** → **Open Support Case**.

      2.  The **Cluster ID** value automatically fills in.

    - To obtain your cluster ID using the OpenShift CLI (`oc`), run the following command:

      ``` terminal
      $ oc get clusterversion -o jsonpath='{.items[].spec.clusterID}{"\n"}'
      ```

9.  Complete the following questions where prompted and then click **Continue**:

    - What are you experiencing? What are you expecting to happen?

    - Define the value or impact to you or the business.

    - Where are you experiencing this behavior? What environment?

    - When does this behavior occur? Frequency? Repeatedly? At certain times?

10. Upload relevant diagnostic data files and click **Continue**. Red Hat recommends including data gathered by using the `oc adm must-gather` command as a starting point, plus any issue-specific data that the command does not collect.

11. Input relevant case management details and click **Continue**.

12. Preview the case details and click **Submit**.

</div>

# Additional resources

- [Using Red Hat Lightspeed to identify issues with your cluster](remote_health_monitoring/using-insights-to-identify-issues-with-your-cluster.md#using-insights-to-identify-issues-with-your-cluster)
