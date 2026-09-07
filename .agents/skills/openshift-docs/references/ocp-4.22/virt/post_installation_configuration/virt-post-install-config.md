<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

After you have installed OpenShift Virtualization, there are procedures that you can complete to ensure that your environment is properly set up. You can configure the components that are relevant for your environment.

- As a cluster administrator, you can run a self validation checkup to verify that the environment is fully functional and self-sustained before you deploy production workloads.

- The hostpath provisioner is a local storage provisioner designed for OpenShift Virtualization. If you want to configure local storage for virtual machines, you must enable the hostpath provisioner first.

- Node placement rules for OpenShift Virtualization Operators, workloads, and controllers.

- Network configuration:

  - Installing the Kubernetes NMState and SR-IOV Operators

  - Configuring a Linux bridge network for external access to virtual machines (VMs)

  - Configuring a dedicated secondary network for live migration

  - Configuring an SR-IOV network

  - Enabling the creation of load balancer services by using the OpenShift Container Platform web console

- Storage configuration:

  - Defining a default storage class for the Container Storage Interface (CSI)

  - Configuring local storage by using the Hostpath Provisioner (HPP)

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

- [Specifying nodes for OpenShift Virtualization components](virt-node-placement-virt-components.md#virt-node-placement-virt-components)

- [Postinstallation network configuration](virt-post-install-network-config.md#virt-post-install-network-config)

- [Postinstallation storage configuration](virt-post-install-storage-config.md#virt-post-install-storage-config)
