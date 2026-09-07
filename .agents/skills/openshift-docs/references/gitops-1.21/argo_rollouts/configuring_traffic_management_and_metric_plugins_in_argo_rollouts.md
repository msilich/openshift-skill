<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Argo Rollouts supports configuring traffic management and metric plugins directly through the `RolloutManager` custom resource (CR). This eliminates the need to modify the config map manually, ensuring consistent configuration. Argo Rollouts no longer preserves user-defined plugins in the config map. Instead, it only applies plugins specified in the `RolloutManager` CR. By managing plugins in the CR, you can do the following:

- Centralize plugin configuration control.

- Avoid conflicts between the `RolloutManager` CR and config map.

- Simplify plugin management by allowing easy addition, removal, or modification of plugins without editing the config map directly.

The traffic management plugin controls how traffic routes between different versions of your application during a rollout, while the metric plugin collects and evaluates metrics to determine the success or failure of a rollout.

# Prerequisites

- You have logged in to the OpenShift Container Platform cluster as an administrator.

- You have access to the OpenShift Container Platform web console.

- You have installed [Red Hat OpenShift GitOps](../installing_gitops/installing-openshift-gitops.md#installing-openshift-gitops) on your OpenShift Container Platform cluster.

- You have installed [Argo Rollouts](using-argo-rollouts-for-progressive-deployment-delivery.md#gitops-creating-rolloutmanager-custom-resource_using-argo-rollouts-for-progressive-deployment-delivery) on your OpenShift Container Platform cluster.

# Enabling traffic management and metric plugins in Argo Rollouts

To enable traffic management and metric plugins in Argo Rollouts, complete the following steps.

<div>

<div class="title">

Procedure

</div>

1.  Log in to the OpenShift Container Platform web console as a cluster administrator.

2.  In the **Administrator** perspective, click **Operators** → **Installed Operators**.

3.  Create or select the project where you want to create and configure a `RolloutManager` custom resource (CR) from the **Project** drop-down menu.

4.  Select **Red Hat OpenShift GitOps** from the **Installed Operators**.

5.  In the **Details** tab, under the **Provided APIs** section, click **Create instance** in the **RolloutManager** pane.

6.  On the **Create RolloutManager** page, select the **YAML view** and edit the YAML.

    **Example adding the traffic management and metric plugins configuration in the `RolloutManager` CR:**

    ``` yaml
    apiVersion: argoproj.io/v1alpha1
    kind: RolloutManager
    metadata:
      name: argo-rollouts
    spec:
      plugins:
        trafficManagement:
          - name: argoproj-labs/gatewayAPI
            location: https://github.com/sample-trafficrouter-plugin
        metric:
          - name: argoproj-labs/sample-prometheus
            location: https://github.com/sample-metric-plugin
            sha256: dac10cbf57633c9832a17f8c27d2ca34aa97dd3d
    ```

    where:

    `spec.plugins.trafficManagement.name`
    Specifies the name of the `trafficManagement` plugin.

    `spec.plugins.trafficManagement.location`
    Specifies the location of the `trafficManagement` plugin.

    `spec.plugins.metric.name`
    Specifies the name of the `metric` plugin.

    `spec.plugins.metric.location`
    Specifies the location of the `metric` plugin.

    `spec.plugins.metric.sha256`
    Specifies the SHA256 signature of the plugin binary that is downloaded and installed by the Rollouts controller. Optional.

7.  Click **Create**.

8.  In the **RolloutManager** tab, under the **RolloutManagers** section, verify that the **Status** field of the RolloutManager instance shows as **Phase: Available**.

9.  Verify that the traffic management and metric plugins are installed correctly by completing the following steps:

    1.  In the **Administrator** perspective, click **Workloads** → **ConfigMaps**.

    2.  Click the **argo-rollouts-config** config map.

        As a result, the plugins defined in the `RolloutManager` CR are updated in the **argo-rollouts-config** config map.

        **Example updated traffic management and metric plugins in the argo-rollouts-config config map:**

        ``` yaml
        kind: ConfigMap
        apiVersion: v1
        metadata:
          name: argo-rollouts-config
          namespace: argo-rollouts
          labels:
            app.kubernetes.io/component: argo-rollouts
            app.kubernetes.io/name: argo-rollouts
            app.kubernetes.io/part-of: argo-rollouts
        data:
          metricPlugins: |
            - name: "argoproj-labs/sample-prometheus"
              location: https://github.com/sample-metric-plugin
              sha256: dac10cbf57633c9832a17f8c27d2ca34aa97dd3d
          trafficRouterPlugins: |
            - name: "argoproj-labs/gatewayAPI"
              location: https://github.com/sample-trafficrouter-plugin
              sha256: ""
            - name: argoproj-labs/openshift
              location: file:/plugins/rollouts-trafficrouter-openshift/openshift-route-plugin
              sha256: ""
        ```

        where:

        `data.metricPlugins.name`
        Specifies the name of the `metric` plugin.

        `data.metricPlugins.location`
        Specifies the location of the `metric` plugin.

        `data.metricPlugins.sha256`
        Specifies the SHA-256 signature of the `metric` plugin.

        `data.trafficRouterPlugins.name`
        Specifies the name of the traffic management plugin.

        `data.trafficRouterPlugins.location`
        Specifies the location of the traffic management plugin.

        `data.trafficRouterPlugins.sha256`
        Specifies the SHA-256 signature of the traffic management plugin.

</div>

# Additional resources

- [Traffic router plugin](https://argo-rollouts.readthedocs.io/en/stable/features/traffic-management/plugins/#traffic-router-plugins)

- [Metric plugin](https://argo-rollouts.readthedocs.io/en/stable/analysis/plugins/)
