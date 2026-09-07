<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

You can shard clusters across multiple Argo CD Application Controller replicas if the controller is managing too many clusters and uses too much memory.

# Round-robin sharding algorithm

> [!IMPORTANT]
> `round-robin` sharding algorithm is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.
>
> For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

By default, the Argo CD Application Controller uses the non-uniform `legacy` hash-based sharding algorithm. This can result in an uneven distribution of clusters across shards. You can enable the `round-robin` sharding algorithm to achieve more equal cluster distribution across all shards.

Using the `round-robin` sharding algorithm in Red Hat OpenShift GitOps provides the following benefits:

- Ensures more balanced workload distribution

- Prevents shards from being overloaded or underutilized

- Optimizes the efficiency of computing resources

- Reduces the risk of bottlenecks

- Improves overall performance and reliability of the Argo CD system

Alternative sharding algorithms let you customize sharding for different use cases. You can choose the algorithm that best fits your deployment. This provides more flexibility for different deployment scenarios.

> [!TIP]
> To use the benefits of alternative sharding algorithms in GitOps, it is crucial to enable sharding during deployment.

## Enabling the round-robin sharding algorithm in the web console

You can enable the `round-robin` sharding algorithm by using the OpenShift Container Platform web console.

<div>

<div class="title">

Prerequisites

</div>

- You have installed the Red Hat OpenShift GitOps Operator on your OpenShift Container Platform cluster.

- You have access to the OpenShift Container Platform web console.

- You have access to the cluster with `cluster-admin` privileges.

</div>

<div>

<div class="title">

Procedure

</div>

1.  In the **Administrator** perspective of the web console, go to **Operators** → **Installed Operators**.

2.  Click **Red Hat OpenShift GitOps** from the installed operators and go to the **Argo CD** tab.

3.  Click the Argo CD instance where you want to enable the `round-robin` sharding algorithm, for example, `openshift-gitops`.

4.  Click the **YAML** tab and edit the YAML file as shown in the following example:

    **Example Argo CD instance with round-robin sharding algorithm enabled:**

    ``` yaml
    apiVersion: argoproj.io/v1beta1
    kind: ArgoCD
    metadata:
      name: openshift-gitops
      namespace: openshift-gitops
    spec:
      controller:
        sharding:
          enabled: true
          replicas: 3
          algorithm: round-robin
        logLevel: debug
    ```

    where:

    `spec.controller.sharding.enabled`
    Specifies the value of the `sharding.enabled` parameter to enable sharding.

    `spec.controller.sharding.replicas`
    Specifies the number of controller replicas, for example, `3`.

    `spec.controller.sharding.algorithm`
    Specifies the cluster distribution algorithm, for example, round-robin.

    `spec.controller.env.value`
    Specifies the sharding algorithm to `round-robin`.

    `spec.controller.logLevel`
    Specifies the log level as `debug` so that you can verify to which shard each cluster is attached.

5.  Click **Save**.

    A success notification alert, `openshift-gitops has been updated to version <version>`, appears.

    > [!NOTE]
    > If you edit the default `openshift-gitops` instance, the **Managed resource** dialog box is displayed. Click **Save** again to confirm the changes.

6.  Verify that the sharding is enabled with `round-robin` as the sharding algorithm by performing the following steps:

    1.  Go to **Workloads** → **StatefulSets**.

    2.  Select the namespace where you installed the Argo CD instance from the **Project** drop-down list.

    3.  Click **\<instance_name\>-application-controller**, for example, **openshift-gitops-application-controller**, and go to the **Pods** tab.

    4.  Observe the number of created application controller pods. It should correspond with the number of set replicas.

    5.  Click on the controller pod you want to examine and go to the **Logs** tab to view the pod logs.

        **Example controller pod logs snippet:**

        ``` terminal
        time="2023-12-13T09:05:34Z" level=info msg="ArgoCD Application Controller is starting" built="2023-12-01T19:21:49Z" commit=a3vd5c3df52943a6fff6c0rg181fth3248976299 namespace=openshift-gitops version=v2.9.2+c5ea5c4
        time="2023-12-13T09:05:34Z" level=info msg="Processing clusters from shard 1"
        time="2023-12-13T09:05:34Z" level=info msg="Using filter function:  round-robin"
        time="2023-12-13T09:05:34Z" level=info msg="Using filter function:  round-robin"
        time="2023-12-13T09:05:34Z" level=info msg="appResyncPeriod=3m0s, appHardResyncPeriod=0s"
        ```

        Look for the `"Using filter function: round-robin"` message.

    6.  In the log **Search** field, search for `processed by shard` to verify that the cluster distribution across shards is even, as shown in the following example.

        > [!IMPORTANT]
        > Ensure that you set the log level to `debug` to observe these logs.

        **Example controller pod logs snippet:**

        ``` terminal
        time="2023-12-13T09:05:34Z" level=debug msg="ClustersList has 3 items"
        time="2023-12-13T09:05:34Z" level=debug msg="Adding cluster with id= and name=in-cluster to cluster's map"
        time="2023-12-13T09:05:34Z" level=debug msg="Adding cluster with id=068d8b26-6rhi-4w23-jrf6-wjjfyw833n23 and name=in-cluster2 to cluster's map"
        time="2023-12-13T09:05:34Z" level=debug msg="Adding cluster with id=836d8b53-96k4-f68r-8wq0-sh72j22kl90w and name=in-cluster3 to cluster's map"
        time="2023-12-13T09:05:34Z" level=debug msg="Cluster with id= will be processed by shard 0"
        time="2023-12-13T09:05:34Z" level=debug msg="Cluster with id=068d8b26-6rhi-4w23-jrf6-wjjfyw833n23 will be processed by shard 1"
        time="2023-12-13T09:05:34Z" level=debug msg="Cluster with id=836d8b53-96k4-f68r-8wq0-sh72j22kl90w will be processed by shard 2"
        ```

        In this example, 3 clusters are attached consecutively to shard 0, shard 1, and shard 2.

        > [!NOTE]
        > If the number of clusters "C" is a multiple of the number of shard replicas "R", then each shard must have the same number of assigned clusters "N", which is equal to "C" divided by "R". The previous example shows 3 clusters and 3 replicas; therefore, each shard has 1 cluster assigned.

</div>

## Enabling the round-robin sharding algorithm by using the CLI

You can enable the `round-robin` sharding algorithm by using the command-line interface.

<div>

<div class="title">

Prerequisites

</div>

- You have installed the Red Hat OpenShift GitOps Operator on your OpenShift Container Platform cluster.

- You have access to the cluster with `cluster-admin` privileges.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Enable sharding and set the number of replicas to the wanted value by running the following command:

    ``` terminal
    $ oc patch argocd <argocd_instance> -n --patch='{"spec":{"controller":{"sharding":{"enabled":true,"replicas":,"algorithm":"round-robin"}}}}' --type=merge
    ```

    **Example output:**

    ``` terminal
    argocd.argoproj.io/<argocd_instance> patched
    ```

2.  Verify that the number of Argo CD Application Controller pods corresponds with the number of set replicas by running the following command:

    ``` terminal
    $ oc get pods -l app.kubernetes.io/name=<argocd_instance>-application-controller -n <namespace>
    ```

    **Example output:**

    ``` terminal
    NAME                                        READY   STATUS    RESTARTS   AGE
    <argocd_instance>-application-controller-0   1/1     Running   0          11s
    <argocd_instance>-application-controller-1   1/1     Running   0          32s
    <argocd_instance>-application-controller-2   1/1     Running   0          22s
    ```

3.  Verify that the sharding is enabled with `round-robin` as the sharding algorithm by running the following command:

    ``` terminal
    $ oc logs <argocd_application_controller_pod> -n <namespace>
    ```

    **Example output snippet:**

    ``` terminal
    time="2023-12-13T09:05:34Z" level=info msg="ArgoCD Application Controller is starting" built="2023-12-01T19:21:49Z" commit=a3vd5c3df52943a6fff6c0rg181fth3248976299 namespace=<namespace> version=v2.9.2+c5ea5c4
    time="2023-12-13T09:05:34Z" level=info msg="Processing clusters from shard 1"
    time="2023-12-13T09:05:34Z" level=info msg="Using filter function:  round-robin"
    time="2023-12-13T09:05:34Z" level=info msg="Using filter function:  round-robin"
    time="2023-12-13T09:05:34Z" level=info msg="appResyncPeriod=3m0s, appHardResyncPeriod=0s"
    ```

    Verify that the `"Using filter function: round-robin"` message appears in the output. This message confirms that the Argo CD Application Controller is using the `round-robin` sharding algorithm.

4.  Verify that the cluster distribution across shards is even by performing the following steps:

    1.  Set the log level to `debug` by running the following command:

        ``` terminal
        $ oc patch argocd <argocd_instance> -n <namespace> --patch='{"spec":{"controller":{"logLevel":"debug"}}}' --type=merge
        ```

        **Example output:**

        ``` terminal
        argocd.argoproj.io/<argocd_instance> patched
        ```

    2.  View the logs and search for `processed by shard` to observe to which shard each cluster is attached by running the following command:

        ``` terminal
        $ oc logs <argocd_application_controller_pod> -n <namespace> | grep "processed by shard"
        ```

        **Example output snippet:**

        ``` terminal
        time="2023-12-13T09:05:34Z" level=debug msg="Cluster with id= will be processed by shard 0"
        time="2023-12-13T09:05:34Z" level=debug msg="Cluster with id=068d8b26-6rhi-4w23-jrf6-wjjfyw833n23 will be processed by shard 1"
        time="2023-12-13T09:05:34Z" level=debug msg="Cluster with id=836d8b53-96k4-f68r-8wq0-sh72j22kl90w will be processed by shard 2"
        ```

        In this example, 3 clusters are attached consecutively to shard 0, shard 1, and shard 2.

        > [!NOTE]
        > If the number of clusters "C" is a multiple of the number of shard replicas "R", then each shard must have the same number of assigned clusters "N", which is equal to "C" divided by "R". The previous example shows 3 clusters and 3 replicas; therefore, each shard has 1 cluster assigned.

</div>

# Dynamic scaling of shards for the Argo CD Application Controller

> [!IMPORTANT]
> Dynamic scaling of shards is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.
>
> For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

> [!IMPORTANT]
> Dynamic scaling of shards for the Argo CD Application Controller, including the `dynamicScalingEnabled` field, is deprecated and might be removed in a future GitOps release.

By default, the Argo CD Application Controller assigns clusters to shards indefinitely. If you are using the `round-robin` sharding algorithm, this static assignment can result in uneven distribution of shards, particularly when replicas are added or removed. You can enable dynamic scaling of shards to automatically adjust the number of shards based on the number of clusters managed by the Argo CD Application Controller at a given time. This ensures that shards are well-balanced and optimizes the use of compute resources.

> [!NOTE]
> After you enable dynamic scaling, you cannot manually modify the shard count. The system automatically adjusts the number of shards based on the number of clusters managed by the Argo CD Application Controller at a given time.

## Enabling dynamic scaling of shards in the web console

You can enable dynamic scaling of shards by using the OpenShift Container Platform web console.

> [!IMPORTANT]
> Dynamic scaling of shards for the Argo CD Application Controller, including the `dynamicScalingEnabled` field, is deprecated and might be removed in a future GitOps release.

<div>

<div class="title">

Prerequisites

</div>

- You have access to the cluster with `cluster-admin` privileges.

- You have access to the OpenShift Container Platform web console.

- You have installed the Red Hat OpenShift GitOps Operator on your OpenShift Container Platform cluster.

</div>

<div>

<div class="title">

Procedure

</div>

1.  In the **Administrator** perspective of the OpenShift Container Platform web console, go to **Operators** → **Installed Operators**.

2.  From the list of **Installed Operators**, select the Red Hat OpenShift GitOps Operator, and then click the **ArgoCD** tab.

3.  Select the Argo CD instance name for which you want to enable dynamic scaling of shards, for example, `openshift-gitops`.

4.  Click the **YAML** tab, and then edit and configure the `spec.controller.sharding` properties as follows:

    **Example Argo CD YAML file with dynamic scaling enabled:**

    ``` yaml
    apiVersion: argoproj.io/v1beta1
    kind: ArgoCD
    metadata:
      name: openshift-gitops
      namespace: openshift-gitops
    spec:
      controller:
        sharding:
          dynamicScalingEnabled: true
          minShards: 1
          maxShards: 3
          clustersPerShard: 1
    ```

    where:

    `spec.controller.sharding.dynamicScalingEnabled`
    Set to `true` to enable dynamic scaling.

    `spec.controller.sharding.minShards`
    Specifies the minimum number of shards. The value must be set to `1` or greater.

    `spec.controller.sharding.maxShards`
    Specifies the maximum number of shards. The value must be greater than the value of `minShards`.

    `spec.controller.sharding.clustersPerShard`
    Specifies the number of clusters per shard. The value must be set to `1` or greater.

5.  Click **Save**.

    A success notification alert, `openshift-gitops has been updated to version <version>`, appears.

    > [!NOTE]
    > If you edit the default `openshift-gitops` instance, the **Managed resource** dialog box is displayed. Click **Save** again to confirm the changes.

</div>

<div class="formalpara">

<div class="title">

Verification

</div>

Verify that sharding is enabled by checking the number of pods in the namespace:

</div>

1.  Go to **Workloads** → **StatefulSets**.

2.  Select the namespace where the Argo CD instance is deployed from the **Project** drop-down list, for example, `openshift-gitops`.

3.  Click the name of the `StatefulSet` object that has the name of the Argo CD instance, for example `openshift-gitops-application-controller`.

4.  Click the **Pods** tab, and then verify that the number of pods is equal to or greater than the value of `minShards` that you have set in the Argo CD `YAML` file.

## Enabling dynamic scaling of shards by using the CLI

You can enable dynamic scaling of shards by using the OpenShift CLI (`oc`).

> [!IMPORTANT]
> Dynamic scaling of shards for the Argo CD Application Controller, including the `dynamicScalingEnabled` field, is deprecated and might be removed in a future GitOps release.

<div>

<div class="title">

Prerequisites

</div>

- You have installed the Red Hat OpenShift GitOps Operator on your OpenShift Container Platform cluster.

- You have access to the cluster with `cluster-admin` privileges.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Log in to the cluster by using the `oc` tool as a user with `cluster-admin` privileges.

2.  Enable dynamic scaling by running the following command:

    ``` terminal
    $ oc patch argocd <argocd_instance> -n <namespace> --type=merge --patch='{"spec":{"controller":{"sharding":{"dynamicScalingEnabled":true,"minShards":<value>,"maxShards":<value>,"clustersPerShard":<value>}}}}'
    ```

    **Example command:**

    ``` terminal
    $ oc patch argocd openshift-gitops -n openshift-gitops --type=merge --patch='{"spec":{"controller":{"sharding":{"dynamicScalingEnabled":true,"minShards":1,"maxShards":3,"clustersPerShard":1}}}}'
    ```

    The example command enables dynamic scaling for the `openshift-gitops` Argo CD instance in the `openshift-gitops` namespace. It sets the minimum number of shards to `1`, the maximum number of shards to `3`, and the number of clusters per shard to `1`. The values of `minShards` and `clustersPerShard` must be set to `1` or greater. The value of `maxShards` must be equal to or greater than the value of `minShards`.

    **Example output:**

    ``` terminal
    argocd.argoproj.io/openshift-gitops patched
    ```

</div>

<div>

<div class="title">

Verification

</div>

1.  Check the `spec.controller.sharding` properties of the Argo CD instance:

    ``` terminal
    $ oc get argocd <argocd_instance> -n <namespace> -o jsonpath='{.spec.controller.sharding}'
    ```

    **Example command:**

    ``` terminal
    $ oc get argocd openshift-gitops -n openshift-gitops -o jsonpath='{.spec.controller.sharding}'
    ```

    **Example output when dynamic scaling of shards is enabled:**

    ``` terminal
    {"dynamicScalingEnabled":true,"minShards":1,"maxShards":3,"clustersPerShard":1}
    ```

2.  Optional: Verify that dynamic scaling is enabled by checking the configured `spec.controller.sharding` properties in the configuration `YAML` file of the Argo CD instance in the OpenShift Container Platform web console.

3.  Check the number of Argo CD Application Controller pods:

    ``` terminal
    $ oc get pods -n <namespace> -l app.kubernetes.io/name=<argocd_instance>-application-controller
    ```

    **Example command:**

    ``` terminal
    $ oc get pods -n openshift-gitops -l app.kubernetes.io/name=openshift-gitops-application-controller
    ```

    **Example output:**

    ``` terminal
    NAME                                           READY   STATUS    RESTARTS   AGE
    openshift-gitops-application-controller-0      1/1     Running   0          2m
    ```

    The number of Argo CD Application Controller pods must be greater than or equal to the value of `minShards`.

</div>

# Additional resources

- [Argo CD custom resource properties](../argocd_instance/argo-cd-cr-component-properties.md#argo-cd-properties_argo-cd-cr-component-properties)

- [Automatically scaling pods with the horizontal pod autoscaler](https://docs.openshift.com/container-platform/latest/nodes/pods/nodes-pods-autoscaling.html)
