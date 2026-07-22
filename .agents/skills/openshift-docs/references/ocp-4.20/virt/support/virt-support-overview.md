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
| **Overview** page | Cluster details, status, alerts, inventory, and resource usage |
| **Virtualization** → **Overview** tab | OpenShift Virtualization resources, usage, alerts, and status |
| **Virtualization** → **Top consumers** tab | Top consumers of CPU, memory, and storage |
| **Virtualization** → **Migrations** tab | Progress of live migrations |
| **Virtualization** → **VirtualMachines** tab | CPU, memory, and storage usage summary |
| **Virtualization** → **VirtualMachines** → **VirtualMachine details** → **Metrics** tab | VM resource usage, storage, network, and migration |
| **Virtualization** → **VirtualMachines** → **VirtualMachine details** → **Events** tab | List of VM events |
| **Virtualization** → **VirtualMachines** → **VirtualMachine details** → **Diagnostics** tab | VM status conditions and volume snapshot status |

Web console pages for monitoring and troubleshooting

# Additional resources

- [Submitting a support case](../../support/getting-support.md#support-submitting-a-case_getting-support)

- [Collecting data about your environment](virt-collecting-virt-data.md#virt-collecting-data-about-your-environment_virt-collecting-virt-data)

- [Using the `must-gather` tool for OpenShift Virtualization](virt-collecting-virt-data.md#virt-using-virt-must-gather_virt-collecting-virt-data)

- [Red Hat Issue Router](https://access.redhat.com/labs/rhir/?product=cnv)

- [Red Hat Jira account](https://redhat.atlassian.net/jira)
