<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Red Hat OpenShift GitOps enables support for two modes of Argo Rollouts installations:

- **Cluster-scoped installation** (default): The Argo Rollouts custom resources (CRs) defined in any namespace are reconciled by the Argo Rollouts instance. As a result, you can use Argo Rollouts CR across any namespace on the cluster.

- **Namespace-scoped installation**: The Argo Rollouts instance is installed in a specific namespace and only handles an Argo Rollouts CR within the same namespace. This installation mode includes the following benefits:

  - This mode does not require cluster-wide `ClusterRole` or `ClusterRoleBinding` permissions. You can install and use Argo Rollouts within a single namespace without requiring cluster permissions.

  - This mode provides security benefits by limiting the cluster scope of a single Argo Rollouts instance to a specific namespace.

> [!NOTE]
> To prevent unintended privilege escalation, Red Hat OpenShift GitOps allows only one mode of Argo Rollout installation at a time.

To switch between cluster-scoped and namespace-scoped Argo Rollouts installations, complete the following steps.

# Configuring a namespace-scoped Argo Rollouts installation

Configuring a namespace-scoped Argo Rollouts installation allows you to limit Argo Rollouts access to a specific namespace instead of granting cluster-wide permissions.

<div>

<div class="title">

Prerequisites

</div>

- You are logged in to the Red Hat OpenShift GitOps cluster as an administrator.

- You have installed Red Hat OpenShift GitOps on your Red Hat OpenShift GitOps cluster.

- You have created the namespace where you want to install the namespace-scoped Argo Rollouts instance.

</div>

<div>

<div class="title">

Procedure

</div>

1.  In the **Administrator** perspective of the web console, go to **Administration** → **CustomResourceDefinitions**.

2.  Search for `Subscription` and click the **Subscription** CRD.

3.  Click the **Instances** tab and then click the **openshift-gitops-operator** subscription.

4.  Click the **YAML** tab and edit the YAML file.

    1.  Specify the `NAMESPACE_SCOPED_ARGO_ROLLOUTS` environment variable, with the value set to `true` in the `.spec.config.env` property.

        **Example of configuring the namespace-scoped Argo Rollouts installation:**

        ``` yaml
        apiVersion: operators.coreos.com/v1alpha1
        kind: Subscription
        metadata:
          name: openshift-gitops-operator
        spec:
          # (...)
          config:
            env:
              - name: NAMESPACE_SCOPED_ARGO_ROLLOUTS
                value: 'true'
        ```

        where:

        `config.env.value`
        Set the value to `'true'` to enable namespace-scoped installation. If the value is set to `'false'` or not specified, the installation defaults to cluster-scoped mode.

    2.  Click **Save**.

        The Red Hat OpenShift GitOps Operator helps with the reconciliation of the Argo Rollouts custom resource within a namespace-scoped installation.

5.  Verify that the Red Hat OpenShift GitOps Operator has enabled the namespace-scoped Argo Rollouts installation by viewing the logs of the GitOps container:

    1.  In the **Administrator** perspective of the web console, go to **Workloads** → **Pods**.

    2.  Click the **openshift-gitops-operator-controller-manager** pod, and then click the **Logs** tab.

    3.  Look for the following log statement: `Running in namespaced-scoped mode`. This statement indicates that the Red Hat OpenShift GitOps Operator has enabled the namespace-scoped Argo Rollouts installation.

6.  Create a `RolloutManager` resource to complete the namespace-scoped Argo Rollouts installation:

    1.  Go to **Operators** → **Installed Operators** → **Red Hat OpenShift GitOps**, and click the **RolloutManager** tab.

    2.  Click **Create RolloutManager**.

    3.  Select **YAML view** and enter the following snippet:

        **Example `RolloutManager` CR for a namespace-scoped Argo Rollouts installation:**

        ``` yaml
        apiVersion: argoproj.io/v1alpha1
        kind: RolloutManager
        metadata:
          name: rollout-manager
          namespace: my-application
        spec:
          namespaceScoped: true
        ```

        where:

        `metadata.namespace`
        Specifies the namespace where you want to install the namespace-scoped Argo Rollouts instance.

    4.  Click **Create**.

        After the `RolloutManager` CR is created, Red Hat OpenShift GitOps begins to install the namespace-scoped Argo Rollouts instance into the selected namespace.

7.  Verify that the namespace-scoped installation is successful.

    1.  In the **RolloutManager** tab, under the **RolloutManagers** section, ensure that the **Status** field of the `RolloutManager` instance is `Phase: Available`.

    2.  Examine the following output in the **YAML** tab under the **RolloutManagers** section to ensure that the installation is successful:

        **Example of namespace-scoped Argo Rollouts installation YAML file:**

        ``` yaml
        spec:
          namespaceScoped: true
        status:
          conditions:
            - lastTransitionTime: "2024-07-10T14:20:05Z"
              message: ""
              reason: Success
              status: "True"
              type: Reconciled
          phase: Available
          rolloutController: Available
        ```

        where:

        `status.rolloutController`
        Specifies the status of the Argo Rollouts controller. The value `Available` indicates that the namespace-scoped Argo Rollouts installation is successful.

        If you try to create a namespace-scoped RolloutManager instance while the GitOps Operator is configured for cluster-scoped mode, you receive the following error:

        **Example of an incorrect installation with an error message:**

        ``` yaml
        spec:
          namespaceScoped: true
        status:
          conditions:
            - lastTransitionTime: "2024-07-10T14:10:07Z"
              message: >
                when Subscription has environment variable
                NAMESPACE_SCOPED_ARGO_ROLLOUTS set to False, there may not exist any
                namespace-scoped RolloutManagers: only a single cluster-scoped
                RolloutManager is supported
              reason: InvalidRolloutManagerScope
              status: "False"
              type: Reconciled
          phase: Failure
          rolloutController: Failure
        ```

        where:

        `status.rolloutController`
        Specifies the status of the Argo Rollouts controller. The value `Failure` indicates that the namespace-scoped Argo Rollouts installation was unsuccessful. In this case, the installation defaults to cluster-scoped mode.

</div>
