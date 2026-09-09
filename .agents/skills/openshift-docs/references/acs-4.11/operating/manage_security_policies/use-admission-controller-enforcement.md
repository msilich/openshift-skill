<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

RHACS works with [Kubernetes admission controllers](https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers/) and [OpenShift Container Platform admission plugins](https://docs.openshift.com/container-platform/4.21/architecture/admission-plug-ins.html) to give you the ability to enforce security policies before Kubernetes or OpenShift Container Platform creates workloads, for example, deployments, daemon sets or jobs. The RHACS admission controller prevents users from creating or updating workloads that violate policies that you configure in RHACS.

<a id="understand-admission-controller-enforcement_use-admission-controller-enforcement"></a>

# Understanding admission controller enforcement

RHACS uses an admission controller to provide enforcement for security policies that you have configured. The admission controller works with validating webhooks to evaluate requests to create, update, and perform workload operations against security policies. It can also evaluate running workloads and detect user-initiated container commands such as `pod exec` and `port forward`. If enforcement is configured for a policy and results in a violation, the request fails, preventing the operation from persisting in the API server and being successfully completed.

The workflow for evaluating requests and enforcing policies follows these steps:

1.  A user or system submits a request to create, update, or perform workload operations that is received by the Kubernetes or OpenShift Container Platform API server.

2.  The API server contacts the validating webhooks with an `AdmissionReview` request.

3.  The validating webhooks call the admission controller via the service endpoint to verify that the resource being provisioned or user-issued commands in the containers comply with the specified security policies.

4.  The review request is either passed or failed, or can time out in some cases:

    - If the review request violates an enforced security policy, the API server rejects the request.

    - If review request is not prevented by a security policy or times out, the API server accepts and persists the resource. In the case of a timeout, this behavior is known as "fail open", which is the default behavior. However, you can configure the default behavior in case of timeout to "fail closed" for stricter enforcement.

If you use admission controller enforcement, consider the following guidance:

- Using admission controller enforcement increases Kubernetes or OpenShift Container Platform API latency because it involves additional validation like policy evaluation on Kubernetes operations. Many standard Kubernetes libraries, such as fabric8, have short Kubernetes or OpenShift Container Platform API timeouts by default.

  Consider API timeouts in any custom automation you might be using. If a request does time out due to latency issues, you can configure if the admission controller will fail open, allowing the request to reach the API server, or fail closed, blocking the requested operation. This setting is configured during installation and you can verify the setting by selecting **Platform Configuration** → **Clusters** and checking the **Admission controller failure policy**.

- If you are using RHACS in a continuous development (CD) tool, set the admission controller failure policy to fail closed, so that your CD tool handles the enforcement.

- You can use admission controller enforcement for the following items:

  - Options in the pod `securityContext`

  - Deployment configurations

  - Image components and vulnerabilities

  - User-initiated container commands such as `pod exec` and `port forward`

- If you have deploy stage enforcement enabled for a policy and you enable the admission controller, RHACS attempts to block deployments that violate the policy. If a noncompliant deployment is not rejected by the admission controller, for example, in case of a timeout, RHACS still applies other deploy stage enforcement mechanisms, such as scaling to zero replicas.

<a id="enable-admission-controller-enforcement_use-admission-controller-enforcement"></a>

# Enabling admission controller enforcement during installation

You can enable admission controller enforcement when you install a cluster.

1.  When installing a cluster by using the Operator, Helm, or `roxctl` CLI methods, follow the instructions in "Installing Secured Cluster services for RHACS on Red Hat OpenShift" and "Installing Secured Cluster services for RHACS on other platforms" to enable admission controller enforcement during installation.

2.  When installing a cluster by using the legacy installation method, follow these steps:

    1.  In the RHACS portal, select **Platform Configuration** → **Clusters**.

    2.  Click **Secure a cluster** → **Legacy installation method**.

    3.  In the **Static configuration** section, in the **Admission controller enforcement behavior** field, select **Enforce policies**.

    4.  Select **Next**.

    5.  Click **Download YAML File and Keys** to download the updated cluster bundle.

    6.  Extract and run the `sensor` script from the cluster bundle to deploy the configuration to the cluster.

        > [!NOTE]
        > When you enable admission controller policy enforcement, the admission controller memory limit is automatically increased to 1 GiB per replica to support image scan data caching requirements. If you specify a custom memory limit override, the custom value takes priority. For more information, see "Admission controller settings for the Operator" and "Configuration parameters for Helm".

<div>

<div class="title">

Verification

</div>

- The `ValidatingWebhookConfiguration` Kubernetes resource contains information about enforcement configuration behavior. The configuration settings are available in the admission controller logs.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Installing Secured Cluster services for RHACS on Red Hat OpenShift](../../installing/installing_ocp/install-secured-cluster-ocp.md)

- [Installing Secured Cluster services for RHACS on other platforms](../../installing/installing_other/install-secured-cluster-other.md)

- [Admission controller settings for the Operator](../../installing/installing_ocp/install-secured-cluster-config-options-ocp.md#admission-controller-settings_install-secured-cluster-config-options-ocp)

- [Configuration parameters for Helm](../../installing/installing_ocp/install-secured-cluster-ocp.md#secured-cluster-services-config_install-secured-cluster-ocp)

</div>

<a id="enable-admission-controller-enforcement-existing-cluster_use-admission-controller-enforcement"></a>

# Viewing and enabling admission controller enforcement on an existing cluster

You can view whether admission controller enforcement was enabled on a cluster or change the enforcement behavior after installation.

<div>

<div class="title">

Procedure

</div>

1.  For a cluster that was installed by using the Operator, in the `SecuredCluster` custom resource (CR), edit the `spec.admissionControl.enforcement` parameter to `Enabled`.

2.  For a cluster that was installed by using Helm, in the `values-public.yaml` file, set the `admissionControl.enforce` value to `false` and run the following command:

    ``` terminal
    helm upgrade -n stackrox \
      stackrox-secured-cluster-services rhacs/secured-cluster-services \
      --reuse-values \
      -f /config/yaml/values-public.yaml \
      -f /config/yaml/values-private.yaml
    ```

3.  For clusters installed by another method, you can use the RHACS portal to edit the enforcement option. You cannot edit Operator- or Helm-managed clusters by using the portal. Follow these steps:

    1.  In the RHACS portal, go to **Platform Configuration** → **Clusters**.

    2.  Select an existing cluster from the list.

    3.  In the **Static configuration** section, in the **Admission controller enforcement behavior** field, select **Enforce policies**. The admission controller enforces policies that are configured for enforcement by rejecting the workload admission or update attempt.

    4.  Select **Next**.

    5.  Click **Download YAML File and Keys** to download the updated cluster bundle.

    6.  Extract and run the `sensor` script from the cluster bundle to redeploy the configuration to the cluster.

        > [!NOTE]
        > When you enable admission controller policy enforcement, the admission controller memory limit is automatically increased to 1 GiB per replica to support image scan data caching requirements. If you specify a custom memory limit override, the custom value takes priority. For more information, see "Admission controller settings for the Operator" and "Configuration parameters for Helm".

</div>

<div>

<div class="title">

Verification

</div>

- The `ValidatingWebhookConfiguration` Kubernetes resource contains information about enforcement configuration behavior. The configuration settings are available in the admission controller logs.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Admission controller settings for the Operator](../../installing/installing_ocp/install-secured-cluster-config-options-ocp.md#admission-controller-settings_install-secured-cluster-config-options-ocp)

- [Configuration parameters for Helm](../../installing/installing_ocp/install-secured-cluster-ocp.md#secured-cluster-services-config_install-secured-cluster-ocp)

</div>

<a id="bypass-admission-controller-enforcement_use-admission-controller-enforcement"></a>

# Bypassing admission controller enforcement

To configure a deployment to bypass the admission controller, you must set the `admission.stackrox.io/break-glass` annotation on the deployment. Bypassing the admission controller triggers a violation of the "StackRox Emergency Deployment Annotation" policy, which includes deployment details.

To help others understand why you bypassed the admission controller, use an issue-tracker link or some other reference as the value of this annotation.

<div>

<div class="title">

Prerequisites

</div>

- You have enabled the ability to bypass the admission controller on the secured cluster by using one of the following options:

  - Operator: You set the `admissionControl.bypass` parameter to `BreakGlassAnnotation`.

  - Helm: You set the `admissionControl.dynamic.disableBypass` parameter to `false`.

  - RHACS portal: You set the option in **Platform Configuration** → **Clusters** → **Admission controller bypass annotation** to **Enabled**.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create a deployment YAML that includes the `admission.stackrox.io/break-glass` annotation, as shown in the following example:

    ``` yaml
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      annotations:
        "admission.stackrox.io/break-glass": "jira-3423"
      creationTimestamp: "2025-03-07T03:18:21Z"
      generation: 1
      labels:
        app: hello-node
      name: hello-node
      namespace: test-bypass-adm
    ...
    ```

    where:

    `metadata.annotations.admission.stackrox.io/break-glass`  
    Specifies a change control reference or relevant explanation for why the admission controller was bypassed.

</div>

<a id="disable-admission-controller-enforcement_use-admission-controller-enforcement"></a>

# Disabling admission controller enforcement on a cluster

You can disable admission controller enforcement on a cluster when installing RHACS. For clusters that you did not install by using the Operator or Helm, you can disable admission controller enforcement from the **Clusters** view on the Red Hat Advanced Cluster Security for Kubernetes (RHACS) portal.

<div>

<div class="title">

Procedure

</div>

1.  For a cluster that was installed by using the Operator, in the `SecuredCluster` custom resource (CR), edit the `spec.admissionControl.enforcement` parameter to `Disabled`.

2.  For a cluster that was installed by using Helm, in the `values-public.yaml` file, set the `admissionControl.enforce` value to `false` and run the following command:

    ``` terminal
    helm upgrade -n stackrox \
      stackrox-secured-cluster-services rhacs/secured-cluster-services \
      --reuse-values \
      -f /config/yaml/values-public.yaml \
      -f /config/yaml/values-private.yaml
    ```

3.  For clusters that are not managed by the Operator or Helm, you can use the RHACS portal to change this setting:

    1.  In the RHACS portal, select **Platform Configuration** → **Clusters**.

    2.  Select an existing cluster from the list.

    3.  In the **Static configuration** section, in the **Admission controller enforcement behavior** field, select one of the following options:

        - Enforce policies: The admission controller enforces policies that are configured for enforcement by rejecting the workload admission or update attempt.

        - No enforcement: Even if enforcement is configured for a policy, if this option is selected, the admission controller does not enforce the policy and allows workload admission attempts or updates that violate the policy.

    4.  Select **Next**.

    5.  Click **Download YAML File and Keys** to download the updated cluster bundle.

    6.  Extract and run the `sensor` script from the cluster bundle to redeploy the configuration to the cluster.

</div>

<a id="admission-controller-failure-policy_use-admission-controller-enforcement"></a>

# Configuring the admission controller failure policy during installation

You can configure the admission controller failure policy when you install a cluster. This setting determines whether the API server request is allowed (fail open) or blocked (fail closed) if an error or timeout happens in the RHACS validating webhook evaluation.

1.  When installing a cluster by using the Operator, Helm, or `roxctl` CLI methods, follow the instructions in "Installing Secured Cluster services for RHACS on Red Hat OpenShift" and "Installing Secured Cluster services for RHACS on other platforms" to configure this parameter during installation.

2.  When installing a cluster by using the legacy installation method, follow these steps:

    1.  In the RHACS portal, select **Platform Configuration** → **Clusters**.

    2.  Select an existing cluster from the list.

    3.  In the **Static configuration (requires deployment)** section, in the **Admission controller failure policy** field, select one of the following options:

        - **Fail open**: If an error or timeout occurs when a workload admission or update request is being evaluated by the validating webhook, the request should be allowed to reach the API server.

        - **Fail closed**: If an error or timeout occurs when a workload admission or update request is being evaluated by the validating webhook, the request should not be allowed to reach the API server, but should be blocked.

    4.  Select **Next**.

    5.  Select **Finish**. Because this is a change to the static configuration, you must redeploy the cluster for your changes to take effect.

<div>

<div class="title">

Additional resources

</div>

- [Installing Secured Cluster services for RHACS on Red Hat OpenShift](../../installing/installing_ocp/install-secured-cluster-ocp.md)

- [Installing Secured Cluster services for RHACS on other platforms](../../installing/installing_other/install-secured-cluster-other.md)

</div>

<a id="admission-controller-failure-policy-changing_use-admission-controller-enforcement"></a>

# Configuring the admission controller failure policy on an existing cluster

You can configure the admission controller failure policy for an existing cluster. This setting determines whether the API server request is allowed (fail open) or blocked (fail closed) if an error or timeout happens in the RHACS validating webhook evaluation.

1.  For a cluster that was installed by using the Operator, in the `SecuredCluster` custom resource (CR), edit the `spec.admissionControl.failurePolicy` parameter to `Ignore` to fail open, or `Fail` to fail closed.

2.  For a cluster that was installed by using Helm, in the `values-public.yaml` file, set the `admissionControl.failurePolicy` value to parameter to `Ignore` to fail open, or `Fail` to fail closed. Then then run the following command:

    ``` terminal
    helm upgrade -n stackrox \
      stackrox-secured-cluster-services rhacs/secured-cluster-services \
      --reuse-values \
      -f /config/yaml/values-public.yaml \
      -f /config/yaml/values-private.yaml
    ```

3.  For clusters installed by another method, you can use the RHACS portal to edit the admission controller failure policy. You cannot edit Operator- or Helm-managed clusters by using the portal. Perform these steps:

    1.  In the RHACS portal, select **Platform Configuration** → **Clusters**.

    2.  Click **Secure a cluster** → **Legacy installation method**.

    3.  In the **Static configuration (requires deployment)** section, in the **Admission controller failure policy** field, select one of the following options:

        - **Fail open**: If an error or timeout occurs when a workload admission or update request is being evaluated by the validating webhook, the request should be allowed to reach the API server.

        - **Fail closed**: If an error or timeout occurs when a workload admission or update request is being evaluated by the validating webhook, the request should not be allowed to reach the API server, but should be blocked.

    4.  Select **Next**.

    5.  Select **Finish**. Because this is a change to the static configuration, you must redeploy the cluster for your changes to take effect.
