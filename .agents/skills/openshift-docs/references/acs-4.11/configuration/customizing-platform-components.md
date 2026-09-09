<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Red Hat Advanced Cluster Security for Kubernetes (RHACS) includes enhanced capabilities to classify violations and vulnerabilities into User Workload or Platform categories, helping you focus on actionable data by segmenting issues based on who is responsible for addressing them.

<a id="customizing-platform-components-overview_customizing-platform-components"></a>

# User workloads and platform components

User workloads and platform components are distinct categories that help you rank security findings based on who is responsible for addressing them.

User workloads refer to the applications and images you deploy and manage directly. Platform components include the underlying infrastructure, Operators, and third-party services. By categorizing security findings, RHACS helps you keep oversight, which prioritizes fixes for issues you directly control.

RHACS automatically identifies platform components based on predefined namespaces. Additionally, you can also customize the namespaces that RHACS identifies as platform components. You can address platform issues by upgrading the offending component, such as OpenShift Container Platform or third-party software, rather than requiring direct user remediation. Thus, by customizing platform components, you can focus on actionable security findings within your user workloads.

<a id="understanding-platform-components_customizing-platform-components"></a>

# Understanding platform components

RHACS automatically identifies platform components by built-in definitions. However, with RHACS 4.8 and newer, you can view and customize these definitions, providing more granular control over how RHACS categorizes security findings.

When viewing violations and vulnerabilities in RHACS, they are categorized as either **User workloads** or **Platform**. This distinction helps you understand the scope and responsibility for addressing security findings.

**User workloads** include violations and vulnerabilities that affect the applications and images you deploy and manage in your system.

**Platform** includes violations and vulnerabilities related to the platform itself, such as those in workloads and images deployed by OpenShift Container Platform and layered services. Platform components are currently defined using entire namespaces, and RHACS uses regular expression patterns to specify such namespaces.

You can view the platform components definition in the RHACS portal by going to **Platform Configuration** \> **System Configuration**.

The **Platform components configuration** section lists platform components in the following categories:

- **Core system components**: These components are part of the core OpenShift Container Platform and Kubernetes namespaces. RHACS includes them in the platform definition by default. You cannot customize these definitions. These definitions might change when you upgrade the system.

- **Red Hat layered products**: Components found in Red Hat layered and partner product namespaces are included in the platform definition by default. Ensure that you update the definition if you install Red Hat products, including RHACS, into a non-default namespace.

- **Custom components**: You can extend the platform definition by defining namespaces for additional applications and products. You can use it to classify other namespaces as **Platform**, such as third-party applications, to exclude them from the focused **User workloads** views.

<a id="modifying-platform-component-definitions_customizing-platform-components"></a>

# Modifying platform component definitions

You can define platform components by using namespaces to segment platform security findings from user workloads.

<div>

<div class="title">

Prerequisites

</div>

- You must have the `Administration` role with `read` permission to view the platform component configuration options.

- You must have the `Administration` role with `write` permission to change the platform component configuration.

</div>

<div>

<div class="title">

Procedure

</div>

1.  In the RHACS portal, go to **Platform Configuration** \> **System Configuration**.

2.  On the **System Configuration** view header, click **Edit**.

3.  Under the **Platform components configuration** section, click the **Red Hat layered products** tab. Components found in Red Hat layered and partner product namespaces are included in the platform definition by default.

    To change the Red Hat layered products definition, enter one or more namespaces using regular expressions, separated by a pipe `|` symbol. For more information on the syntax structure, see the "RE2 syntax reference".

4.  Click the **Custom components** tab.

    1.  To add a custom platform component, click **Add custom platform component**. You can add more than one.

    2.  In the new **Custom component** entry, enter a descriptive **Name**.

    3.  Enter the **Namespace rules (Regex)** for this custom component. Enter one or more namespaces using regular expressions, separated by a pipe `|` symbol. For more information on the syntax structure, see the "RE2 syntax reference".

5.  Click **Save**.

</div>

<div>

<div class="title">

Additional resources

</div>

- [RE2 syntax reference](https://github.com/google/re2/wiki/syntax)

</div>
