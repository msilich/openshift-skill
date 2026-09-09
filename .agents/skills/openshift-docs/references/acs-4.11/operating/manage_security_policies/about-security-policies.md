<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Red Hat Advanced Cluster Security for Kubernetes (RHACS) helps you secure your container infrastructure by using a robust policy engine and an admission controller. With RHACS, you can establish appropriate security guardrails, inform about policy violations, and selectively enforce policies to prevent insecure situations.

Specifically, RHACS can help you fail the CI pipeline in the build stage, reject deployments from being deployed in the deployment stage, and shut down running deployments that violate runtime policies. RHACS also provides policy management and violation management tools described in the following sections.

<a id="policy-evaluation-engine_about-security-policies"></a>

# Understanding the RHACS policy evaluation engine

The RHACS policy engine evaluates policies that you have created based on policy criteria. It operates differently in each of the build, deploy, and runtime stages.

Build stage  

RHACS can evaluate policy rules upon request by using the `roxctl` CLI. When a policy is violated during the build stage, the violation text and error code let developers know what failed and how to fix it. You can configure the error code to fail the pipeline. During this stage, RHACS can evaluate both standalone images and deployments against applicable policies. Violations from the build stage are not stored or routed using notifiers.

Deploy stage  

RHACS uses deploy stage policies when inspecting workloads during a deployment attempt. These policies are composed of workload criteria, such as the following criteria:

- Container configuration, including environment variables and privileges

- Deployment metadata, such as required or disallowed annotations and labels

- Storage volume information, such as volume name and mount configuration

- Networking configuration, such as port exposure and ingress or egress policy

- Kubernetes access configuration, which consists of criteria such as service account configuration and Role-based Access Control (RBAC) permissions

You can also include image criteria, such as image registry, image content, and CVE data, when building deploy stage policies. This is helpful if you want to evaluate the same requirements in both pipeline builds and deployment attempts. This eliminates the need to duplicate policies, because you can create a policy that includes both image and workload criteria and use it for both the build and deploy stages.

RHACS prevents Kubernetes or OpenShift Container Platform from creating or updating workloads, for example, deployments, daemon sets or jobs, that match the conditions of the policy. This is useful for shutting down deployments with serious problems even if the build was successful.

Runtime stage  

RHACS continuously evaluates deployments against applicable policies after a deployment is running. Runtime policies are used to monitor running pods within a Kubernetes cluster and report or prevent unauthorized workload activity, baseline deviations, or prohibited Kubernetes resource operations. RHACS can monitor unsafe Kubernetes requests and selectively block them by using the API. F example, RHACS can block attempted access to config maps or secrets.

Runtime policies can inspect the following two event sources:

- Deployment events: Real-time events such as running pods, process activity inside pods, deviations from networking or process baselines, or user-pod interaction such as port forwarding or port exec actions

- Audit log events: Logs that can be inspected for actions such as access to sensitive Kubernetes resources

Runtime policies can also include build and deploy stage criteria for the following reasons:

- These criteria can be used to identify high-risk situations combining runtime and workload/image criteria.

- These criteria can ensure that the build and deploy stage requirements are met during runtime, for example, when a new vulnerability is discovered, or a new requirement has been introduced.

Audit log policies are used to inspect the Kubernetes audit log for actions related to sensitive Kubernetes resources, such as secrets and `ClusterRoleBinding`. They have the following characteristics:

- Audit log policies are only composed of the audit log criteria.

- They are not associated with images or deployments. For this reason, audit log policies can only be associated with the runtime lifecycle stage.

- These policies are not enforceable, because the audited action has already occurred.

<a id="policy-enforcement-about_about-security-policies"></a>

# About policy enforcement

When you configure policies in RHACS, you can configure how RHACS responds when it detects a condition that violates a security policy.

RHACS allows you to enforce security policies during all phases of the development lifecycle: build, deploy, and runtime.

RHACS provides two types of policy enforcement:

- Sensor enforcement: Also known as *soft* enforcement, if a workload is examined and violates a policy, Sensor scales down pods by using the Kubernetes API.

- Admission controller enforcement: Also known as *hard* enforcement, an admission controller works with validating webhooks and the Kubernetes API server to block workload admission or update attempts that violate an enforced policy. When a request is made to deploy or update, the validating webhooks communicate with the admission controller and the admission controller responds to either allow or block the action based on whether a policy is enforced. The API server accepts or rejects the request based on whether it violates the policy and if the policy is enforced.

For more information about admission controller enforcement, see "Understanding admission controller enforcement".

<div>

<div class="title">

Additional resources

</div>

- [Understanding admission controller enforcement](use-admission-controller-enforcement.md#understand-admission-controller-enforcement_use-admission-controller-enforcement)

</div>

<a id="build-stage-policies_about-security-policies"></a>

## Build stage enforcement

RHACS uses build stage policies to discover and respond to security violations before code is deployed. Build stage policies are composed entirely of image criteria, such as image registry, image content, and CVE data, including scan results and status.

RHACS checks the build by using the `roxctl image check` and `roxctl deployment check` commands. You can configure RHACS to fail your continuous integration (CI) builds when images match the criteria of the policy. This means that when there is a condition in the build that violates the policy, for example, if there is a fixable CVE of a severity level and you have configured a policy for that condition, the build fails.

As an example, you can configure RHACS to check an image or deployment and integrate that check into a continuous integration/continuous development (CI/CD) pipeline. Then, if RHACS detects a condition that means a policy should fail, the RHACS API returns a non-zero exit code. These violations are not collected or acted on by RHACS, but are used with a CI/CD tool. You configure your CI/CD tool to act on those results, for example, to fail the build process if a violation is reported.

<a id="policy-enforcement-deploy_about-security-policies"></a>

## Deploy stage enforcement

Red Hat Advanced Cluster Security for Kubernetes supports two forms of security policy enforcement for deploy-time policies: hard enforcement through the admission controller and soft enforcement by RHACS Sensor. The admission controller blocks creation or updating of deployments that violate policy. If the admission controller is disabled or unavailable, Sensor can perform enforcement by scaling down replicas for deployments that violate policy to 0.

> [!WARNING]
> Policy enforcement can impact running applications or development processes. Before you enable enforcement options, inform all stakeholders and plan how to respond to the automated enforcement actions.

<a id="policy-enforcement-hard_about-security-policies"></a>

### Hard enforcement

Hard enforcement is performed by the RHACS admission controller. In clusters with admission controller enforcement, the Kubernetes or OpenShift Container Platform API server blocks all noncompliant deployments. The admission controller blocks `CREATE`, `UPDATE`, and `SCALE` operations. Any pod create, update, or scale request that satisfies a policy configured with deploy-time enforcement enabled will fail. The admission controller also blocks user-initiated container commands such as `pod exec` and `port forward` for policies configured with runtime enforcement.

> [!NOTE]
> Kubernetes admission webhooks support only `CREATE`, `UPDATE`, `DELETE`, and `CONNECT` operations. The RHACS admission controller supports only `CREATE`, `UPDATE`, and `SCALE` operations. Operations such as `kubectl patch`, `kubectl set`, and `kubectl scale` are `PATCH` operations, not `UPDATE` operations. Because `PATCH` operations are not supported in Kubernetes, RHACS cannot perform enforcement on PATCH operations. However, enforcement against `SCALE` operations is supported.

For hard enforcement, enable the enforcement settings for the cluster in RHACS. To verify that enforcement is enabled, in the **Static configuration** section, in the **Admission controller enforcement behavior** field, ensure that **Enforce policies** is selected. Additionally, for each policy that you want to enforce, select **Inform and enforce** when configuring the policy.

> [!NOTE]
> Because admission controller enforcement is a static configuration option, changing this setting for clusters that are installed by using the manifest or `roxctl` method requires you to download the updated YAML bundle and redeploy it to the cluster.

<a id="namespace-exclusions_about-security-policies"></a>

### Namespace exclusions from admission controller enforcement

By default, Red Hat Advanced Cluster Security for Kubernetes (RHACS) excludes certain administrative namespaces from from the validating webhook configurations in the admission controller. Policy evaluation and enforcement is not performed on review requests originating from these administrative namespaces. Some items in these namespaces must be deployed for RHACS to work correctly so they are excluded.

In addition to excluding namespaces, the RHACS admission controller bypasses requests that originate from from a Kubernetes `ServiceAccount` in a system namespace.

> [!NOTE]
> Consider this factor when choosing the namespace to deploy your continuous deployment tool of choice.

The following namespaces are excluded by default:

- `stackrox`

- `kube-system`

- `kube-public`

- `istio-system`

For Helm installations on Kubernetes secured clusters, you can customize the namespaces that are excluded from the validating webhook configuration by configuring the `values-public.yaml` file. In the `admissionControl.namespaceSelector` field, you can specify the namespaces that you want to exclude. See the following example:

``` yaml
...
admissionControl:
   namespaceSelector:
    matchExpressions:
    - key: namespace.metadata.stackrox.io/name
      operator: NotIn
      values:
        - stackrox
        - kube-system
        - kube-public
        - istio-system
        - example-namespace
...
```

where:

example-namespace  
Signifies the namespace that you want to exclude.

<a id="enforcement-existing-deployments_about-security-policies"></a>

### Enforcement on existing deployments

For existing deployments, policy changes only result in enforcement at the next detection of the criteria, when a Kubernetes event occurs. If you make changes to a policy, you must reassess policies by selecting **Policy Management** and clicking **Reassess All**. This action applies deploy policies on all existing deployments regardless of whether there are any new incoming Kubernetes events. If a policy is violated, then RHACS performs enforcement.

<a id="policy-enforcement-soft_about-security-policies"></a>

### Soft enforcement

Soft enforcement is performed by RHACS Sensor. This enforcement prevents an operation from being initiated. With soft enforcement, Sensor scales the replicas to 0, and prevents pods from being scheduled. In this enforcement, a non-ready deployment is available in the cluster.

By design, Sensor only performs this soft enforcement once, to prevent trapping of update requests to scale the deployment back down again.

If soft enforcement is configured, and Sensor is down, then RHACS cannot perform enforcement.

<a id="policy-enforcement-runtime_about-security-policies"></a>

## Runtime enforcement

You can configure policies that are enforced during runtime to terminate a pod that violates the policy or, in the case of audit log inspection, notify you of events that violate the policy but have already occurred and have been logged.

When enforced, a policy violation results in one or more of the following actions:

- Shutting down an offending pod, which results in creation of another healthy pod in its place

- RHACS intercepting and preventing certain Kubernetes API calls

> [!IMPORTANT]
> When a violation is triggered by an image or workload rule, a violation alert is generated, but the pod is *not* disrupted.

<a id="policy-structure_about-security-policies"></a>

# RHACS policy structure

RHACS policies are structured text objects that define security rules and the action RHACS performs when these rules are broken.

An RHACS policy contains the following parts:

<a id="policy-definition_about-security-policies"></a>

## Policy definition

The policy definition specifies the policy’s metadata and its rules, including the following components:

Policy details  
Text to assist policy authors in managing policies and end users in the remediation process.

Lifecycle  
A fundamental policy attribute that determines when RHACS evaluates that policy.

Policy rules  
A set of conditions that are used with an implied `OR`, for example, rule 1 *or* rule 2. Each rule consists of predefined building blocks called policy criteria that use an `AND` relationship, for example, criterion A *and* criterion B. RHACS uses intuitive text to describe the conditions that you want, rather than having you specify potentially complex Kubernetes conditions.

Most RHACS criteria configure the condition on which to trigger the policy, and many criteria include a `NOT` form. However, a few criteria define the positive, expected behavior. Whether a criteria defines a positive or negative condition depends on the context. Ccriteria are designed to make creating policies intuitive for policy users.

The following examples show negative and positive forms of policy criteria:

- Negative form: `Container Registry name is <gcr.io>` triggers if the specific `gcr.io` registry is used. Therefore, `Container Registry name is NOT <quay.io>` triggers if any registry is used other than the allowed registry, quay.io. This is a generalized rule.

- Negative form: `Liveness probe is <Not Defined>` triggers if a liveness probe is missing from the configuration. You can use `Liveness probe is <Defined>` to receive a positive notification by using a notifier for all compliant workloads.

- Positive form: The `Drop capabilities, Capabilities that MUST be dropped: <SYS_ADMIN>` rule defines the expected behavior. If a workload fails to drop the `SYS_ADMIN` property, it violates the policy and triggers a violation alert.

<a id="policy-behavior_about-security-policies"></a>

## Policy behavior

The policy behavior specifies the action, inform or enforce, that RHACS takes for given resources. Policy behavior includes the following items:

Resources  
By default, RHACS policies are *global*; they apply across all secured clusters, on all namespaces, for all workloads and images.

You can modify the policy resources by explicitly including or excluding a mix of cluster, namespace, and deployment selection criteria. Policy resource targeting can use cluster ID or cluster labels, namespace name or namespace labels, and deployment labels to target specific resources. Regular expressions in RE2 syntax are supported for namespace names and deployment labels.

Label-based resource targeting (cluster labels and namespace labels) uses exact `key=value` matching for *included* resources only and requires RHACS 4.11 or later on secured clusters installed by using Helm or the Operator. *Excluded* resources do not support cluster label or namespace label targeting.

Action  
Determines if a policy is active, for example, whether it is enabled or disabled, if it is enforced, and the notifiers to use for routing alerts.

<a id="policy-and-violation-management_about-security-policies"></a>

# Policy and violation management

*Policy management* encompasses the set of activities that security teams undertake to establish the appropriate guardrails. All of these activities happen **before** the policy is evaluated. *Violation management* is the set of activities that security and developer teams take to assist in addressing security incidents to remediate policy violations. All of these activities happen after a policy has been violated.

<a id="setting-policy-rules_about-security-policies"></a>

## Setting policy rules

With policy as code, RHACS supports both internal and external sources for policies. When using external policies, RHACS defines a Kubernetes native Custom Resource (CR) to streamline policy as code by using tools like OpenShift Pipelines and Argo CD.

You can use RHACS to perform the following actions:

- Define policy rules: Whether teams manage their policies as code or by using the RHACS internal database, authoring policies can be technically challenging. RHACS provides an intuitive user interface, or portal, that simplifies this task. You can focus on controls while hiding the specification complexity. You can author policies by using the portal and then exported them as YAML to be stored as code or be stored locally.

- Choose the lifecycle to which the policy applies: For internal policies, RHACS offers Create, Read, Update, Delete (CRUD) actions. For external policies, these actions are handled by users on their own, and the results are presented to RHACS using the CR. For internal policies, RHACS also offers role-based access control and tracks changes to policies in its audit log.

- Configure policy behavior: RHACS provides users with multi-cluster governance in a centralized manner. When configuring policies, you can configure the following:

  - Select the scope for inclusion or exclusion for individual clusters, or establish governance to apply to all clusters

  - Choose the action (inform/enforce), and enable or disable the policy

  - Configure notifiers

- Test policies:

  - You can perform a dry run to test the policy in the portal or by using the API, and perform policy CR validation

  - Create policy reports: You can configure reporting in the portal or by using the API to detail policy coverage

<a id="default-security-policies-about_about-security-policies"></a>

# Default security policies

The default security policies in Red Hat Advanced Cluster Security for Kubernetes provide broad coverage to identify security issues and ensure best practices for security in your environment. By configuring those policies, you can automatically prevent high-risk service deployments in your environment and respond to runtime security incidents.

For a list of default security policies categorized by severity, see "Security policy reference".

<div>

<div class="title">

Additional resources

</div>

- [Security policy reference](security-policy-reference.md)

</div>

<a id="viewing-default-security-policies_about-security-policies"></a>

## Viewing default security policies

You can use the RHACS portal to view default policies, clone them, and edit the cloned default policies. Default policies are not supported with the policies as code feature.

<div>

<div class="title">

Procedure

</div>

- In the RHACS portal, go to **Platform Configuration** → **Policy Management**. Default policies are indicated by the **System** label in the **Origin** column.

  > [!NOTE]
  > You cannot delete default policies or edit policy criteria for default policies.

</div>

<a id="custom-security-policies-about_about-security-policies"></a>

# Custom security policies

With RHACS, you can create custom security policies to provide security during the build, deploy, and run phases of development. You can create custom security policies by the following methods:

- You can clone a default policy and then modify it to configure specific information for your environment

- You can use the RHACS portal to create and save a new policy.

- With the policy as code feature, you can create and save policies as Kubernetes custom resources (CRs) and use a Kubernetes-native continuous delivery (CD) tool such as Argo CD to apply them to clusters.

For more information, see "Creating and modifying security policies".

> [!IMPORTANT]
> Use caution when enforcing custom policies in the `openshift-*` namespaces and for default OpenShift Container Platform pods. For example, a custom policy with enforcement configured can terminate pods with possible data loss if the policy is violated.

<a id="sharing-security-policies_about-security-policies"></a>

# Sharing security policies

You can share your security policies between different Central instances in the RHACS portal by exporting and importing policies. Sharing policies helps you enforce the same standards for all your clusters. To share policies, you export them as JSON files, and then import them back into another Central instance.

> [!NOTE]
> Currently, you cannot export multiple security policies at the same time by using the RHACS portal. However, you can use the API for exporting multiple security policies. In the RHACS portal, go to **Help** → **API reference** to see the API reference.

<a id="export-security-policy_about-security-policies"></a>

## Exporting a security policy

When you export a policy, it includes all the policy contents and also includes cluster scopes, cluster exclusions, and all configured notifications.

<div>

<div class="title">

Procedure

</div>

1.  In the RHACS portal, go to **Platform Configuration** → **Policy Management**.

2.  From the **Policies** page, select the policy you want to edit.

3.  Select **Actions** → **Export policy to JSON**.

</div>

<a id="import-security-policy_about-security-policies"></a>

## Importing a security policy

You can import a security policy from the **System Policies** view on the RHACS portal.

<div>

<div class="title">

Procedure

</div>

1.  In the RHACS portal, go to **Platform Configuration** → **Policy Management**.

2.  Click **Import policy**.

3.  In the **Import policy JSON** dialog, click **Upload** and select the JSON file you want to upload.

4.  Click **Begin import**.

    Each security policy in RHACS has a unique ID (UID) and a unique name. When you import a policy, RHACS handles the uploaded policy as follows:

    - If the imported policy UID and name do not match any existing policy, RHACS creates a new policy.

    - If the imported policy has the same UID as an existing policy, but a different name, you can either:

      - Keep both policies. RHACS saves the imported policy with a new UID.

      - Replace the existing policy with the imported policy.

    - If the imported policy has the same name as an existing policy, but a different UID, you can either:

      - Keep both policies by providing a new name for the imported policy.

      - Replace the existing policy with the imported policy.

    - If the imported policy has the same name and UID as an existing policy, the Red Hat Advanced Cluster Security for Kubernetes checks if the policy criteria match to the existing policy. If the policy criteria match, RHACS keeps the existing policy and shows a success message. If the policy criteria do not match, you can either:

      - Keep both policies by providing a new name for the imported policy.

      - Replace the existing policy with the imported policy.

        <div class="important">

        <div class="title">

        </div>

        - If you import into the same Central instance, RHACS uses all the exported fields.

        - If you import into a different Central instance, RHACS omits certain fields, such as cluster scopes, cluster exclusions, and notifications. RHACS shows these omitted fields in a message. These fields vary for every installation, and you cannot migrate them from one Central instance to another.

        </div>

</div>
