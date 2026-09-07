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

    3.  Select **4.22** from the **Version** drop-down.

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

# Self-service Technical Supportability Review

You can use the self-service Technical Supportability Review (TSR) on the Red Hat Customer Portal to validate your cluster configuration against Red Hat common practices.

> [!NOTE]
> The `must-gather` tool collects diagnostic information about your cluster, including resource definitions, service logs, and configuration data. For more information, see "Gathering data about your cluster" in the OpenShift Container Platform documentation.

The self-service TSR uses AI to evaluate your cluster’s `must-gather` data and provides a prioritized executive summary of recommendations. This serves as a starting point to help you identify and resolve potential issues before they impact your environment.

The TSR performs hundreds of checks across the OpenShift Container Platform platform, including OpenShift Virtualization. Coverage is continually expanding.

## When to use the self-service TSR tool

Integrating the self-service TSR into your regular operational workflow can be helpful in the following scenarios:

Routine benchmarking
Use the TSR quarterly to benchmark cluster health and plan for routine maintenance activities.

Pre-flight checks
Validate your cluster configuration before major structural changes, including upgrades, migrations, and expansions.

Critical event preparation
Confirm cluster stability ahead of high-traffic business events, such as seasonal peaks, or operational milestones, such as year-end shutdowns, business continuity drills, and compliance audits.

## How to access the TSR

To run a self-service review, upload your cluster’s `must-gather` data to the **Analyze** tab in the **Support** section of the Red Hat Customer Portal. For a direct link, see "Technical Supportability Review with AI tool" in the Additional resources section. The **Analyze** feature generates a prioritized executive summary that identifies your cluster’s top risks and recommends corrective actions. Review the recommendations and implement the suggested corrective actions to address the identified risks.

The self-service TSR provides a solid baseline for cluster health. If you need additional guidance or a more comprehensive review, contact your Red Hat account team to arrange an assisted review through a Technical Account Manager (TAM) or Red Hat consultant. An assisted review includes human analysis, deeper coverage, and access to checks that are updated more frequently than the self-service version.

<div>

<div class="title">

Additional resources

</div>

- [Technical Supportability Review with AI tool](https://access.redhat.com/support/cases/#/analyze)

- [Red Hat Technical Supportability Review with AI: Proactive AI-Driven Cluster Assessments for OpenShift Container Platform](https://access.redhat.com/solutions/7141255)

</div>

# Additional resources

- [Using Red Hat Lightspeed to identify issues with your cluster](remote_health_monitoring/using-insights-to-identify-issues-with-your-cluster.md#using-insights-to-identify-issues-with-your-cluster)
