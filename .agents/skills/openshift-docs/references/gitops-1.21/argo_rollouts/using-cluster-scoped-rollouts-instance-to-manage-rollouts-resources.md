<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Cluster-scoped installation mode allows a single Argo Rollouts controller instance to manage rollout resources across multiple namespaces. This reduces resource consumption compared to deploying separate namespace-scoped controllers in each namespace. You can control which namespaces a cluster-scoped RolloutManager instance manages by setting the `CLUSTER_SCOPED_ARGO_ROLLOUTS_NAMESPACES` environment variable in the Red Hat OpenShift GitOps Operator Subscription to a comma-separated list of namespace names.

To configure a cluster-scoped Argo Rollouts instance, you must first install the Red Hat OpenShift GitOps Operator, create a `RolloutManager` custom resource (CR), and then update the Operator Subscription to specify the namespaces.

# Prerequisites

- You have logged in to the OpenShift Container Platform cluster as an administrator.

- You have installed the Red Hat OpenShift GitOps Operator on your OpenShift Container Platform cluster.

- You have created a `RolloutManager` custom resource in the namespace where you want to run the Argo Rollouts controller.

# Configuring a cluster-scoped Argo Rollouts instance to manage rollout resources

To configure which namespaces a cluster-scoped Argo Rollouts instance manages, set the `CLUSTER_SCOPED_ARGO_ROLLOUTS_NAMESPACES` environment variable in the Red Hat OpenShift GitOps Operator Subscription to a comma-separated list of namespace names. If this variable is not set, the RolloutManager manages rollouts only in the namespace where it is deployed.

<div>

<div class="title">

Procedure

</div>

1.  In the **Administrator** perspective of the web console, navigate to **Operators** → **Installed Operators** → **Red Hat OpenShift GitOps** → **Subscription**.

2.  Click the **Actions** list and then click **Edit Subscription**.

3.  On the **openshift-gitops-operator** Subscription details page, under the **YAML** tab, edit the `Subscription` YAML file by setting the `CLUSTER_SCOPED_ARGO_ROLLOUTS_NAMESPACES` environment variable to a comma-separated list of namespaces:

    **Example configuring the `CLUSTER_SCOPED_ARGO_ROLLOUTS_NAMESPACES` environment variable:**

    ``` yaml
    apiVersion: operators.coreos.com/v1alpha1
    kind: Subscription
    metadata:
      name: openshift-gitops-operator
    spec:
      config:
        env:
          - name: NAMESPACE_SCOPED_ARGO_ROLLOUTS
            value: "false"
          - name: CLUSTER_SCOPED_ARGO_ROLLOUTS_NAMESPACES
            value: "namespace1,namespace2,namespace3"
    ```

    where:

    `spec.config.env[].value` (NAMESPACE_SCOPED_ARGO_ROLLOUTS)
    Specify this value to enable or disable the cluster-scoped installation. Set the value to `'false'` to enable cluster-scoped installation. Set to `'true'` to enable namespace-scoped installation. If this value is empty, the operator defaults to `false`.

    `spec.config.env[].value` (CLUSTER_SCOPED_ARGO_ROLLOUTS_NAMESPACES)
    Specifies a comma-separated list of namespaces that can host a cluster-scoped Argo Rollouts instance. For example `test-123-cluster-scoped,test-456-cluster-scoped`.

4.  Click **Save** and **Reload**.

</div>

<div class="formalpara">

<div class="title">

Verification

</div>

Verify that the Red Hat OpenShift GitOps Operator has restarted after the Subscription update:

</div>

1.  In the Administrator perspective, navigate to **Workloads** → **Pods**.

2.  Locate the `openshift-gitops-operator-controller-manager` pod and verify that it has a recent restart time.

3.  Verify that the Argo Rollouts controller is managing the specified namespaces:

    1.  Navigate to the namespace where you created the RolloutManager CR.

    2.  Click the argo-rollouts- pod, and then click the Logs tab.

    3.  Confirm that the logs show the controller is watching the namespaces you specified in CLUSTER_SCOPED_ARGO_ROLLOUTS_NAMESPACES.

# Additional resources

- [Creating RolloutManager custom resources](using-argo-rollouts-for-progressive-deployment-delivery.md#gitops-creating-rolloutmanager-custom-resource_using-argo-rollouts-for-progressive-deployment-delivery)
