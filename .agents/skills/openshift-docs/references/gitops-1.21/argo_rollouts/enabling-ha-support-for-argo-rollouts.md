<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Argo Rollouts supports high availability (HA) through the `RolloutManager` custom resource (CR). When you enable HA, the Red Hat OpenShift GitOps Operator sets the number of pods to 2 for the Argo Rollouts controller using the `.spec.ha` field. It also activates leader election, so the pods run in an active-passive configuration. One pod actively manages rollouts, while the other remains passive and provides redundancy if a node fails.

HA ensures the Rollouts controller runs without downtime or manual intervention. The second replica keeps the controller running smoothly during planned maintenance. The controller remains reliable and resilient even during node failures or heavy workloads.

The Red Hat OpenShift GitOps Operator also applies anti-affinity rules by default. These rules distribute controller pods across different nodes to avoid a single point of failure.

# Prerequisites

- You are logged in to the OpenShift Container Platform cluster as an administrator.

- You installed [Red Hat OpenShift GitOps](../installing_gitops/installing-openshift-gitops.md#installing-openshift-gitops) on your OpenShift Container Platform cluster.

- You installed [Argo Rollouts](using-argo-rollouts-for-progressive-deployment-delivery.md#gitops-creating-rolloutmanager-custom-resource_using-argo-rollouts-for-progressive-deployment-delivery) on your OpenShift Container Platform cluster.

# Configuring high availability for Argo Rollouts

To enable high availability, configure the `ha` specification in the `RolloutManager` custom resource (CR) by completing the following steps:

<div>

<div class="title">

Procedure

</div>

1.  Log in to the OpenShift Container Platform web console as a cluster administrator.

2.  In the **Administrator** perspective, click **Operators** → **Installed Operators**.

3.  Create or select the project where you want to create and configure a `RolloutManager` CR from the **Project** drop-down menu.

4.  Select **Red Hat OpenShift GitOps** from the installed Operators.

5.  In the **Details** tab, under the **Provided APIs** section, click **Create instance** in the **RolloutManager** pane.

6.  On the **Create RolloutManager** page, select the **YAML view** and edit the YAML.

    **Example enabling the `ha` field in the `RolloutManager` CR:**

    ``` yaml
    apiVersion: argoproj.io/v1beta1
    kind: RolloutManager
    metadata:
      name: argo-rollouts
      namespace: openshift-gitops
    spec:
      ha:
        enabled: true
    ```

    where:

    `spec.ha.enabled`
    Specifies whether high availability is enabled or not. If the value is set to `true`, high availability is enabled.

7.  Click **Create**.

8.  In the **RolloutManager** tab, under the **RolloutManagers** section, verify that the **Status** field of the RolloutManager instance shows **Phase: Available**.

9.  Verify the status of the Rollouts deployment by completing the following steps:

    1.  In the **Administrator** perspective, click **Workloads** → **Deployments**.

    2.  Click the **argo-rollouts** deployment.

    3.  Click the **Details** tab and confirm that the number of replicas in the Rollouts deployment is now set to 2.

    4.  Click the **YAML** tab and confirm that the following configuration is displayed:

        **Example Argo Rollouts deployment configuration file:**

        ``` yaml
        apiVersion: apps/v1
        kind: Deployment
        metadata:
          name: argo-rollouts
          namespace: openshift-gitops
        spec:
          replicas: 2
          selector:
            matchLabels:
              app.kubernetes.io/name: argo-rollouts
          template:
            metadata:
              labels:
                app.kubernetes.io/name: argo-rollouts
            spec:
              containers:
                - name: argo-rollouts
                  image: argoproj/argo-rollouts:latest
                  args:
                    - --leader-elect=true
        ```

        where:

        `spec.replicas`
        Specifies the number of pods.

        `spec.template.spec.containers.args`
        Specifies that the `--leader-elect=true` flag is passed to the Rollouts deployment. The `--leader-elect=true` flag enables leader election, allowing only one pod to actively manage rollouts while others remain in standby.

</div>
