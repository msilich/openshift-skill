<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Accelerate the resolution of cluster and virtual machine (VM) issues by using the integrated diagnostic tools and support provided by OpenShift Virtualization.

To gather debugging information, configure Prometheus and Alertmanager and collect `must-gather` data for OpenShift Container Platform and OpenShift Virtualization.

# Opening a support case

Open a support case with Red Hat Support when you encounter an issue that requires immediate assistance.

## Collecting data for Red Hat Support

Gather information about the issue affecting your environment to submit with your support case. This aids Red Hat Support in effectively diagnosing your issue.

Gather troubleshooting information by using the following tools:

- Configure Prometheus and Alertmanager.

<!-- -->

- Configure and use the `must-gather` tool.

- Collect `must-gather` data and memory dumps from VMs.

- Collect `must-gather` data for OpenShift Container Platform and OpenShift Virtualization

## Submitting a support case

Submit a support case to resolve a cluster issue that is affecting the ability of OpenShift Virtualization to function properly in your environment.

You can submit a support case to Red Hat Support by using the Customer Support page. Include data that you collected about your issue with your support request.

# Creating a Jira issue

To report a bug, use the Red Hat Issue Router (RHIR), which is available in the Customer Portal Labs.

<div>

<div class="title">

Procedure

</div>

1.  Access the RHIR.

2.  In the list of all OpenShift Virtualization components, find the component for which you want to report an issue.

3.  Click the **Report a bug** link of the component.

4.  On the **Create issue** page, fill out the form:

    1.  Complete the **Summary** and **Description** fields. In the **Description** field, include a detailed description of the issue.

    2.  Submit any collected troubleshooting information:

        1.  Add any textual troubleshooting information, such as command outputs, in the **Description** field.

        2.  Add troubleshooting files using the **Attachment** field.

5.  Click **Create** at the bottom of the page.

6.  Review the details of the bug you created.

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

# Provide feedback on OpenShift Virtualization documentation

To report an error or request an enhancement in the documentation, log in to your Red Hat Jira account and submit an issue. If you do not have a Red Hat Jira account, you are prompted to create an account.

<div>

<div class="title">

Procedure

</div>

1.  Create a [Jira issue](https://redhat.atlassian.net/secure/CreateIssueDetails!init.jspa?priority=1003&summary=%5BDoc%5D&pid=10270&issuetype=10016&components=13563) and in the **Component** field, select **CNV Documentation**.

2.  Enter a brief description of the issue in the **Summary**.

3.  Provide a detailed description of the issue or requested enhancement in the **Description**. Include a URL to where the issue occurs in the documentation.

4.  Click **Create**.

</div>

# Web console monitoring

Monitor cluster and virtual machine (VM) health with the OpenShift Container Platform web console.

The OpenShift Container Platform web console displays resource usage, alerts, events, and trends for your cluster and for OpenShift Virtualization components and resources.

| Page | Description |
|----|----|
| **Virtualization** → **VirtualMachines** → **Overview** page | Cluster details, status, alerts, inventory, and resource usage |
| **Virtualization** → **VirtualMachines** → **Overview** → **Overview** tab | OpenShift Virtualization resources, usage, alerts, and status |
| **Virtualization** → **Migrations** page | Progress of live migrations |
| **Virtualization** → **VirtualMachines** → **Virtual machines** tab | CPU, memory, and storage usage summary |
| **Virtualization** → **VirtualMachines** → **Virtual machines** → **VirtualMachine details** → **Metrics** tab | VM resource usage, storage, network, and migration |
| **Virtualization** → **VirtualMachines** → **Virtual machines** → **VirtualMachine details** → **Events** tab | List of VM events |
| **Virtualization** → **VirtualMachines** → **Virtual machines** → **VirtualMachine details** → **Diagnostics** tab | VM status conditions and volume snapshot status |

Web console pages for monitoring and troubleshooting

# Additional resources

- [Submitting a support case](../../support/getting-support.md#support-submitting-a-case_getting-support)

- [Collecting data about your environment](virt-collecting-virt-data.md#virt-collecting-data-about-your-environment_virt-collecting-virt-data)

- [Using the `must-gather` tool for OpenShift Virtualization](virt-collecting-virt-data.md#virt-using-virt-must-gather_virt-collecting-virt-data)

- [Red Hat Issue Router](https://access.redhat.com/labs/rhir/?product=cnv)

- [Red Hat Jira account](https://redhat.atlassian.net/jira)
