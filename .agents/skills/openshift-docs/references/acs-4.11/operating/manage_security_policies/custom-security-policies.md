<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Create custom security policies in the {product-title-short} portal to enforce configuration rules and minimize risks. Define detailed criteria, lifecycle stages, and automated enforcement options to detect and block noncompliant images or workloads. By using these policies, you support consistent security standards across the build, deploy, and runtime phases.

<a id="create-policy-from-system-policies-view_custom-security-policies"></a>

# Creating a security policy from the system policies view

Define a new security policy in the RHACS portal to enforce security rules in your environment. Go to **Policy Management** to create a new policy and enter the required definition information. You can manage security settings by creating policies in the **Platform Configuration → Policy** page.

<div>

<div class="title">

Procedure

</div>

1.  In the RHACS portal, go to **Platform Configuration** → **Policy Management**.

2.  Click **Create policy**.

3.  Configure the policy definition information in the following sections.

</div>

<a id="enter-policy-details_custom-security-policies"></a>

## Entering policy details

Configure the core attributes of your custom security policy to ensure exact threat classification. Assign a severity level and offer clear remediation guidance to resolve policy violations effectively. Additionally, specify MITRE ATT&CK tactics and techniques to contextualize the potential security risk.

<div>

<div class="title">

Procedure

</div>

1.  Enter a **Name** for the policy. A policy must have a name between 5 and 128 characters, and cannot contain new lines or dollar signs.

2.  Select a **Severity** level for the policy.

3.  From the **Select categories** list, select a category for the policy. You can select one or more categories for the policy.

4.  Enter details about the policy in the **Description** field.

5.  Enter an explanation about why the policy exists in the **Rationale** field.

6.  Enter steps to resolve violations of the policy in the **Guidance** field.

7.  Select the [tactic and the techniques](https://attack.mitre.org/matrices/enterprise/containers/) you want to specify for the policy:

    1.  From the **Add tactic** list, select a tactic.

    2.  From the **Add technique** list, select a technique for the tactic. You can specify one or more techniques for a tactic.

8.  Click **Next**.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Creating and using collections](../create-use-collections.md)

</div>

<a id="select-policy-lifecycle_custom-security-policies"></a>

## Selecting the policy lifecycle stage

Define when RHACS evaluates policies by assigning a specific lifecycle stage. You can target these specific phases to inspect images during the continuous integration (CI) process or monitor workload activity on a live node, ensuring that enforcement actions occur at the appropriate time.

For more information, see "Understanding the RHACS policy evaluation engine".

<div>

<div class="title">

Procedure

</div>

1.  Select the **Lifecycle stages** for the policy:

    The following options are associated with the lifecycle stages:

    Build  
    Policies in this stage inspect image criteria such as the image registry, content, vulnerability data, and the scanning process. The CI pipeline evaluates these policies during the build process. If you enable enforcement, a policy violation fails the build. RHACS does not store violations from this stage.

    Deploy  
    Policies in this stage inspect workload configurations and their images. RHACS evaluates these policies when you create or update a workload resource and re-evaluates them periodically or on-demand. When you enable enforcement, a policy violation causes the admission controller to reject the deployment or update try, or scale the workload replicas to zero.

    Build and Deploy  
    Select this stage if you want your policy to inspect images in both the build pipeline and during workload admission, and to apply enforcement to either or both stages.

    Runtime  
    Policies in this stage inspect either workload activity or Kubernetes resource operations associated with the following event sources:

    Deployment  
    To use runtime policies for workload activity, you must include at least one workload activity criterion. You can combine workload activity criteria with image or workload configuration criteria. If you enable enforcement, RHACS terminates the offending pod, and the orchestrator then re-creates the pod.

    Audit logs  
    Runtime policies that evaluate Kubernetes resource operations look for sensitive operations by using the Kubernetes audit log. You cannot configure enforcement for policies that use this source, because the operations have already occurred. Audit log policies support cluster and namespace scoping, but not deployment-level scoping, because audit events operate at the Kubernetes API level rather than at the deployment level.

    Node  
    Runtime policies that monitor file activity on the host operating system of your Kubernetes nodes. These policies detect unauthorized file operations, such as changes to sensitive system files, by using the actual file path on the host. Policies that use this event source do not support automated enforcement or exclusions in the RHACS console.

2.  Click **Next**.

</div>

<a id="configure-policy-rules_custom-security-policies"></a>

## Configuring policy rules

To control when a policy is triggered, configure the specific conditions and rules that apply to your environment. You can customize these rules by dragging and dropping policy fields, such as networking or workload activity, to define criteria appropriate for the build or runtime lifecycle stages.

<div>

<div class="title">

Procedure

</div>

1.  Configure the conditions that you want to trigger the policy. You can edit the rule titles; for example, you can change `Rule 1` to something more descriptive.

2.  For each rule, click and drag policy fields into the policy section to add policy fields or criteria.

    > [!NOTE]
    > The policy fields that are available depend on the lifecycle stage you chose for the policy. For example, the criteria associated to **Networking** or **Workload activity** are available when creating a policy for the runtime lifecycle, but not when creating a policy for the build lifecycle. For more information about policy criteria, including information about criteria and the lifecycle phase in which they are available, see "Policy criteria".

3.  For each field, you can select from options that are specific to the field. These differ depending on the type of field. For example:

    - The default behavior for a value that is a string is to match on a policy field, and select the **Not** checkbox to indicate when you do not want the field to match.

    - Some fields contain a value that is either `true` or `false`.

    - Some fields require you to select a value from a drop-down list.

    - If you select an attribute with Boolean values, such as `Read-Only Root Filesystem`, the `READ-ONLY` and `WRITABLE` options are available.

    - If you select an attribute with compound values, such as `Environment variable`, you can enter values for the `Key`, `Value`, and `Value From` fields, and then click the icon to add more values for the available options.

      > [!NOTE]
      > For more information about values available for policy criteria, see "Policy criteria".

4.  To combine multiple values for an attribute, click the **Add value of policy field** icon.

5.  Optional: To add an additional rule, click **Add a new rule** .

6.  Click **Next**.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Policy criteria](security-policy-reference.md#policy-criteria_security-policy-reference)

</div>

<a id="configure-policy-scope_custom-security-policies"></a>

## Configuring policy resources

Define the policy resources to target the resources in your environment that you want to monitor. You can configure the policy to include specific clusters and namespaces and identify the cluster or namespace by name or by label. Labels are a key/value pair that RHACS sources from Kubernetes cluster or namespace data, or Helm chart values for Helm-based deployments. You can also configure the policy to include deployments with a specified label.

The following guidelines apply:

- Policies automatically apply to new resources based on metadata labels without requiring policy updates. By configuring these resources, you ensure that the policy triggers violations only for relevant resources.

- If you do not configure any resource rules, the policy applies globally to all secured clusters, all namespaces, and all deployments. This is the default behavior.

- The node event source does not support resource scoping.

- Audit log event source policies support cluster and namespace scoping, but not deployment-level scoping.

- Cluster-scoped resources (for example, ClusterRoles) ignore namespace-level matchers.

The following restrictions apply:

- Label-based resource targeting is not supported on secured clusters installed by using the manifest install method. Only Helm and Operator-based installations support label-based targeting.

- Cluster and namespace resource targeting (both name-based and label-based) only applies to deploy-time and runtime policies. Build-time policies do not evaluate cluster or namespace scopes.

You can use these fields to make sure policies apply to only the clusters that you want. For example, to apply a policy to all clusters except a specific development cluster, leave **Included resources** empty (policies apply to all clusters by default). Then, add an **Excluded resources** rule specifying the cluster name. This configuration applies the policy globally except to the named cluster.

For more information about using cluster and namespace labels to scope policies, see "Policy resource evaluation logic".

<div>

<div class="title">

Prerequisites

</div>

- Cluster labels and namespace labels require the following:

  - Both Central and secured clusters must run RHACS 4.11 or later

  - You install secured clusters by using Helm or the Operator (manifest, or `roxctl` installation, is not supported)

- Secured clusters running earlier versions or that you installed by using the manifest install method ignore the cluster label and namespace label fields in resource rules.

</div>

<div>

<div class="title">

Procedure

</div>

1.  You can configure the resources to which your policy applies.

    1.  **Included resources**: To specify resources to include in the policy, select **Add inclusion** and configure the policy to specify certain clusters, namespaces, or deployments:

        - **Cluster**: To select resources from a specified cluster, configure **one** of the following options:

          - **By name**: Select a specific cluster by name.

          - **By label**: Target a cluster by label `key=value` pairs (for example, `environment=production`). RHACS sources cluster labels from the Kubernetes cluster metadata; for example, labels on the `SecuredCluster` custom resource for Operator deployments, or Helm chart values for Helm-based deployments.

        - **Namespace**: To select resources from specified namespaces, select **one** of the following options:

          - **By name**: Target a namespace by name. You can use regular expression in RE2 syntax in this field.

          - **By label**: Target a namespace by `label key=value` pairs (for example, `compliance=pci`). For example, to restrict a policy to production clusters with PCI compliance namespaces, add a resource rule with cluster label `environment=production` and namespace label `compliance=pci`.

        - **Deployment label**: To select resources from deployments with a specific label, you can enter the label, or `key=value` pair.

          Within a single resource rule, the system combines the cluster, namespace, and deployment label criteria by using `AND` logic. If you add multiple resource rules, the policy applies to resources matching `ANY` of the resource rules (OR logic). After adding a resource rule, you can click **Add resource rule** to add additional rules.

2.  **Excluded resources**: To configure the policy to *not* apply to specific resources, you can exclude them. The policy will not apply to the entities you select. To exclude specific resources from the policy:

    1.  Select **Add exclusion** and configure the policy to specify certain clusters, namespaces, or deployments:

        - **Cluster**: To exclude resources from a specified cluster, select a specific cluster by name. You cannot use labels to target clusters to exclude.

        - **Namespace**: To exclude resources from specified namespaces, enter the namespace name. You can use regular expression in RE2 syntax in this field.

        - **Deployment**: To exclude specific deployments from the policy, enter the deployment name. You can use regular expression in RE2 syntax in this field. For example, to exclude test namespaces, add an exclusion rule with the namespace name pattern `test-.*`.

        - **Deployment label**: To exclude deployments with a specific label, you can enter the label, or `key=value` pair.

3.  **Exclude images**: To exclude specific images from the policy, you can specify them. This setting only applies when you check images in a continuous integration system with the **Build** lifecycle stage. It does not have any effect if you use this policy to check running deployments in the **Deploy** lifecycle stage or runtime activities in the **Runtime** lifecycle stage. To exclude specific images from the policy, select them from the list of images.

</div>

<a id="scope-rule-evaluation-logic_custom-security-policies"></a>

### Policy resource evaluation logic

RHACS evaluates policy resource rules by combining cluster ID or labels, namespace name or labels, and deployment labels to find the resources that a policy applies to. Understanding the evaluation logic helps you design resource rules that target the intended resources without unintended matches or exclusions.

A policy resource rule consists of up to three types of selection criteria: cluster selection, namespace selection, and deployment label selection. RHACS combines these criteria by using `AND` logic and `OR` logic to find whether a policy applies to a specific resource.

<a id="resource-rule-structure_custom-security-policies"></a>

#### Resource rule structure

Within a single resource rule, RHACS combines the specified criteria by using `AND` logic. For example, `(Cluster ID OR Cluster label) AND (Namespace name OR Namespace label) AND (Deployment label)` means that a deployment must match all specified criteria within a resource rule for the policy to apply.

If a field is not specified in a resource rule, it matches all resources of that type. For example, a resource rule with only cluster label `environment=production` (no namespace or deployment criteria) applies to all namespaces and all deployments on clusters labeled `environment=production`.

> [!IMPORTANT]
> You cannot specify both cluster ID and cluster label in the same resource rule. Similarly, you cannot specify both namespace name and namespace label in the same resource rule. These fields are mutually exclusive within a single rule. If you specify both in the RHACS web console or via the API, the system prevents you from saving the policy configuration with a validation error.

If you add multiple resource rules to a policy, RHACS combines the rules by using `OR` logic. A deployment matches the policy if it satisfies any one of the resource rules.

For example, a policy with two resource rules applies to deployments that match either rule:

- Rule 1: Cluster label `environment=production` AND Namespace label `compliance=pci`

- Rule 2: Cluster ID `staging-cluster-1` AND Namespace name `pci-test`

This policy applies to the following entities:

- All deployments in namespaces labeled `compliance=pci` on clusters labeled `environment=production`, OR

- All deployments in the `pci-test` namespace on the `staging-cluster-1` cluster

<a id="label-matching_custom-security-policies"></a>

#### Label matching

Cluster labels and namespace labels use exact `key=value` matching. When you specify a label such as `environment=production`, the policy applies only to resources with that exact label key and value. For example, for the label selector `environment=production`:

- This policy applies to resources that match clusters or namespaces with the label `environment=production`.

- This policy does not match resources with `environment=prod` or `environment=production-east`.

Namespace names and deployment labels support regular expressions by using RE2 syntax.

<a id="ref-policy-scope-label-syntax_custom-security-policies"></a>

### Policy resource label syntax reference

This reference provides syntax examples for cluster labels and namespace labels in policy resource rules. Use these patterns to configure label-based policy targeting.

<a id="label-format_custom-security-policies"></a>

#### Label format

Policy resource labels use the `key=value` format. Both cluster labels and namespace labels use exact string matching.

Label matching is case-sensitive. The label key `Environment` is different from the key `environment`.

<a id="common-label-patterns_custom-security-policies"></a>

#### Common label patterns

The following table shows common label patterns for policy resource configuration:

| Use case              | Cluster label example    | Namespace label example |
|-----------------------|--------------------------|-------------------------|
| Environment targeting | `environment=production` | `environment=staging`   |
| Compliance zone       | `compliance=pci`         | `compliance=hipaa`      |
| Geographic region     | `region=us-east-1`       | `region=eu-west-1`      |
| Team or organization  | `owner=platform-team`    | `team=security`         |
| Application grouping  | `app=medical-portal`     | `app=financial-api`     |

Policy resource label patterns

<a id="label-examples_custom-security-policies"></a>

#### Label examples

The following examples show policy resource labels:

- Target production clusters: `environment=production`. This matches clusters with the exact label `environment=production`.

- PCI compliance: `compliance=pci`. This matches namespaces with the exact label `compliance=pci`.

- Target namespaces owned by the security team: `team=security`: This matches namespaces with the exact label `team=security`.

<a id="mutual-exclusivity-rules_custom-security-policies"></a>

#### Mutual exclusivity rules

When configuring policy scope rules, note the following mutual exclusivity constraints:

- You cannot specify both cluster ID and cluster label in the same resource rule. Choose one cluster selection method per rule.

- You cannot specify both namespace name and namespace label in the same resource rule. Choose one namespace selection method per rule.

- You can combine cluster label AND namespace label AND deployment label in a single resource rule.

- Label-based targeting is only available for included resources in RHACS 4.11. Excluded resources do not support cluster label or namespace label targeting.

If you need to target resources by using both ID-based and label-based criteria, create multiple resource rules. RHACS combines multiple resource rules with OR logic.

**Example**: To target a specific staging cluster by ID and all production clusters by label, create two resource rules:

- Rule 1: Cluster ID `staging-cluster-1`

- Rule 2: Cluster label `environment=production`

<a id="managing-cluster-and-namespace-labels_custom-security-policies"></a>

#### Managing cluster and namespace labels

RHACS sources the cluster labels used for policy resource targeting from Kubernetes cluster metadata:

- For Operator-based secured cluster deployments: Define labels on the `SecuredCluster` custom resource

- For Helm-based secured cluster deployments: Define labels in Helm chart values

RHACS sources namespace labels from Kubernetes namespace metadata.

To verify the labels that are available for targeting:

1.  Navigate to **Platform Configuration** → **Clusters** to view cluster labels.

2.  Use `kubectl get namespace <namespace_name> --show-labels` to view namespace labels.

<a id="enable-policy_custom-security-policies"></a>

## Enable the policy

Apply the configured rules to your environment by activating the policy. You can enable the policy to enforce these settings or disable the policy to stop its application.

<div>

<div class="title">

Procedure

</div>

- Select whether to enable or disable the policy:

  - To enable the policy, select **Enable**.

  - To disable the policy, select **Disable**.

</div>

<a id="configure-policy-enforcement-creating-policies_custom-security-policies"></a>

## Configuring policy enforcement

To address security violations effectively, configure RHACS to apply specific enforcement behaviors across the build, deploy, and runtime lifecycles. You can adjust the configuration to receive alerts for violations or automatically block noncompliant images and workloads to stop them from entering your environment. Implementing these controls ensures that your clusters remain secure and compliant with your defined policies.

<div>

<div class="title">

Procedure

</div>

1.  Select a method to address the violations of the policy:

    > [!NOTE]
    > Enforcement is not available for node event sources.

    Inform  
    Include the violation in the violations list.

    Inform and enforce  
    Include the violation in the violation list and enforce actions that you have configured. If you select this option, you must select the enforcement behavior for the policy by using the toggle for the appropriate lifecycles.

2.  If you select policy enforcement, configure the enforcement behavior. The enforcement behavior you can select depends on the lifecycle stages you selected for the policy in the **Lifecycle** section of the policy definition.

    The following enforcement behaviors are available depending on the lifecycle stage:

    Build  
    Set **Enforce on Build** to on to have RHACS fail your continuous integration (CI) builds when images match the criteria of the policy. You can download the `roxctl` CLI and configure the `roxctl image check` command to work with the policy.

    Deploy  
    Set **Enforce on Deploy** to on to have RHACS block any workload admissions or updates that match the policy criteria. You must configure and run the RHACS admission controller for this enforcement to take effect.

    - In clusters with admission controller enforcement, the Kubernetes or OpenShift Container Platform API server blocks all noncompliant deployments. In clusters without admission controller enforcement, RHACS modifies noncompliant deployments to prevent pods from scheduling.

    - For existing deployments, policy changes only result in enforcement at the next detection of the criteria, when a Kubernetes event occurs. For more information about enforcement, see "Deploy stage enforcement".

    Runtime  
    Set **Enforce on Runtime** to on to have RHACS delete all pods when an event in the pods matches the criteria of the policy.

    > [!WARNING]
    > Policy enforcement can impact running applications or development processes. Before you enable enforcement options, inform all stakeholders and plan how to respond to automated enforcement actions.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Deploy stage enforcement](about-security-policies.md#policy-enforcement-deploy_about-security-policies)

</div>

<a id="selecting-policy-notifiers_custom-security-policies"></a>

## Selecting policy notifiers

To receive alerts by email or an external tool when a policy violation occurs, select notifiers from the available list. These integrations notify you immediately of compliance events so you can respond quickly.

<div>

<div class="title">

Prerequisite

</div>

- You have configured the notifier before it is visible and available to select in the list. You configure these integrations in the **Platform Configuration** → **Integrations** page, in the **Notifier Integrations** section.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Select one or more notifiers for RHACS to use to inform you when a policy violation occurs.

2.  Click **Next**.

</div>

<a id="preview-policy-violations_custom-security-policies"></a>

## Reviewing the policy and previewing violations

To ensure the policy is working correctly, verify the configuration options and examine potential violations in the **Preview policy violations** panel. Validate the build and deploy phase results to confirm the accuracy of the policy before you save the changes.

<div>

<div class="title">

Procedure

</div>

1.  Verify that the policy configuration is configured with the correct options.

2.  View the results in the **Preview policy violations** panel to ensure that the policy is working. This panel provides additional information, including whether build phase or deploy phase deployments have policy violations.

    > [!NOTE]
    > Runtime violations are not available in this preview because they are generated when events occur in the future.

    Before you save the policy, verify that the violations seem accurate.

3.  Click **Save**.

</div>

<a id="verifying-file-activity-policies_custom-security-policies"></a>

## Verifying file activity policies

You can verify that your file activity policies are functioning correctly by manually triggering a violation on a monitored component.

<div>

<div class="title">

Prerequisites

</div>

- You have configured a file activity policy for a **Deployment** or **Node** event source.

- You have identified the specific files and operations monitored by your policy.

- You have access to the command line interface of the monitored node or deployment.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Trigger a file activity violation on a monitored node or deployment by running the following command, for example:

    ``` terminal
    $ touch /etc/passwd
    ```

2.  Choose the appropriate method to confirm that the alert is displayed:

    - For deployment policies, complete the following steps:

      1.  In the RHACS portal, click **Violations**.

      2.  Verify that the alert is displayed in the list.

    - For node policies, verify that the notifier has received an alert, or query the alerts API to locate the violation JSON data.

      > [!NOTE]
      > The RHACS portal does not display node violations. To view these alerts, use the API or configured notifiers.

</div>

<a id="create-policy-from-risk-view_custom-security-policies"></a>

# Creating a security policy from the risk view

You can generate a new security policy directly from the **Risk** view in the RHACS portal to address specific security concerns. Use this method to create a policy based on the local page filtering criteria you apply to your risk data, ensuring the policy targets the specific risks you are analyzing.

<div>

<div class="title">

Procedure

</div>

1.  In the RHACS portal, click **Risk**.

2.  Apply the local page filtering criteria that you want to create a policy for. For example, you can filter by using criteria such as a specific CVE, a cluster, a deployment, an image, or various other criteria.

3.  Click **Create policy** and complete the required fields to create a new policy. For the steps to create a policy, see "Creating a security policy from the system policies view".

</div>

<a id="modify-existing-security-policies_custom-security-policies"></a>

# Modifying existing security policies

You can update security configurations in the RHACS portal to adapt to changing security requirements. Select a specific policy to edit its fields and save your changes. To customize a default system policy, you must clone the policy to create an editable copy.

<div>

<div class="title">

Procedure

</div>

1.  In the RHACS portal, click **Platform Configuration** → **Policy Management**.

2.  Select the policy you want to edit.

3.  From the **Actions** list, select **Edit policy**.

    > [!NOTE]
    > You cannot edit certain fields of default system policies. To make changes to a default policy, clone the policy and edit the copy.

4.  Edit the fields that you want to change, and then click **Save**.

</div>

<a id="disable-associated-policies_custom-security-policies"></a>

## Disabling a policy

Disable a policy in the RHACS portal to prevent the system from using it when evaluating workload operations. To deactivate the policy, edit the policy behavior settings and turn off the activation state.

<div>

<div class="title">

Procedure

</div>

1.  In the RHACS portal, click **Platform Configuration** → **Policy Management**. For default policies, you cannot edit enforcement options.

2.  Select the policy you want to edit.

3.  From the **Actions** list, select **Edit policy**.

4.  Expand **Policy behavior**, and then select **Actions**.

5.  In the **Activation state** field, select **Disable**.

6.  Save the policy.

</div>

<a id="create-policy-categories-using-tab_custom-security-policies"></a>

## Creating policy categories by using the Policy categories tab

You can create policy categories by using the **Policy categories** tab. You can also configure policy categories by using the `PolicyCategoryService` API object. For more information, go to **Help** → **API reference** in the RHACS portal.

<div>

<div class="title">

Procedure

</div>

1.  In the RHACS portal, go to **Platform Configuration** → **Policy Management**.

2.  Click the **Policy categories** tab. This tab provides a list of existing categories and allows you to filter the list by category name. You can also click **Show all categories** and select the checkbox to remove default or custom categories from the displayed list.

3.  Click **Create category**.

4.  Enter a category name and click **Create**.

</div>

<a id="modify-policy-categories-using-tab_custom-security-policies"></a>

## Modifying policy categories by using the Policy categories tab

You can modify policy categories by using the policy categories tab. You can also configure policy categories by using the `PolicyCategoryService` API object. For more information, go to **Help** → **API reference** in the RHACS portal.

<div>

<div class="title">

Procedure

</div>

1.  In the RHACS portal, go to **Platform Configuration** → **Policy Management**.

2.  Click the **Policy categories** tab. This tab provides a list of existing categories and allows you to filter the list by category name. You can also click **Show all categories** and select the checkbox to remove default or custom categories from the displayed list.

3.  Click a policy name to edit or delete it. Default policy categories cannot be selected, edited, or deleted.

</div>
