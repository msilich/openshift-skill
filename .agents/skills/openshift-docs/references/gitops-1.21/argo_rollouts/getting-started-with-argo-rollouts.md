<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Argo Rollouts supports [canary](https://docs.openshift.com/container-platform/latest/applications/deployments/deployment-strategies.html#deployments-canary-deployments_deployment-strategies) and [blue-green](https://docs.openshift.com/container-platform/latest/applications/deployments/route-based-deployment-strategies.html#deployments-blue-green_route-based-deployment-strategies) deployment strategies. This guide provides instructions with examples using a canary deployment strategy to help you deploy, update, promote and manually abort rollouts.

With a canary-based deployment strategy, you split traffic between two application versions:

- Canary version: A new version of an application where you gradually route the traffic.

- Stable version: The current version of an application. After the canary version is stable and has all the user traffic directed to it, it becomes the new stable version. The previous stable version is discarded.

# Prerequisites

- You have logged in to the OpenShift Container Platform cluster as an administrator.

- You have access to the OpenShift Container Platform web console.

- You have installed [Red Hat OpenShift GitOps](../installing_gitops/installing-openshift-gitops.md#installing-openshift-gitops) on your OpenShift Container Platform cluster.

- You have installed [Argo Rollouts](using-argo-rollouts-for-progressive-deployment-delivery.md#gitops-creating-rolloutmanager-custom-resource_using-argo-rollouts-for-progressive-deployment-delivery) on your OpenShift Container Platform cluster.

- You have installed the [Argo Rollouts CLI](using-argo-rollouts-for-progressive-deployment-delivery.md#gitops-installing-argo-rollouts-cli-on-linux_using-argo-rollouts-for-progressive-deployment-delivery) on your system.

# Deploying a rollout

As a cluster administrator, you can configure Argo Rollouts to progressively route a subset of user traffic to a new application version. Then you can test whether the application is deployed and working.

The following example procedure creates a `rollouts-demo` rollout and service. The rollout then routes 20% of traffic to a canary version of the application, waits for a manual promotion, and then performs multiple automated promotions until it routes the entire traffic to the new application version.

<div>

<div class="title">

Procedure

</div>

1.  In the **Administrator** perspective of the web console, click **Operators** → **Installed Operators** → **Red Hat OpenShift GitOps** → **Rollout**.

2.  Create or select the project in which you want to create and configure a `Rollout` custom resource (CR) from the **Project** drop-down menu.

3.  Click **Create Rollout** and enter the following configuration in the YAML view:

    ``` yaml
    apiVersion: argoproj.io/v1alpha1
    kind: Rollout
    metadata:
      name: rollouts-demo
    spec:
      replicas: 5
      strategy:
        canary:
          steps:
          - setWeight: 20
          - pause: {}
          - setWeight: 40
          - pause: {duration: 45}
          - setWeight: 60
          - pause: {duration: 20}
          - setWeight: 80
          - pause: {duration: 10}
      revisionHistoryLimit: 2
      selector:
        matchLabels:
          app: rollouts-demo
      template:
        metadata:
          labels:
            app: rollouts-demo
        spec:
          containers:
          - name: rollouts-demo
            image: argoproj/rollouts-demo:blue
            ports:
            - name: http
              containerPort: 8080
              protocol: TCP
            resources:
              requests:
                memory: 32Mi
                cpu: 5m
    ```

    where:

    `spec.strategy.canary`
    Specifies the deployment strategy that the rollout must use.

    `spec.strategy.canary.steps`
    Specifies the steps for the rollout. This example gradually routes 20%, 40%, 60%, and 80% of traffic to the canary version.

    `spec.strategy.canary.steps.setWeight`
    Specifies the percentage of traffic that must be directed to the canary version. A value of 20 means that 20% of traffic is directed to the canary version.

    `spec.strategy.canary.steps.pause`
    Instructs the Argo Rollouts controller to pause indefinitely until it finds a request for promotion.

    `spec.strategy.canary.steps.pause.duration`
    Instructs the Argo Rollouts controller to pause for a specified duration. You can set the duration value in seconds (`s`), minutes (`m`), or hours (`h`). For example, you can specify `1h` for an hour. If no value is specified, the duration value defaults to seconds.

    `spec.template`
    Specifies the pods that are to be created.

4.  Click **Create**.

    > [!NOTE]
    > To ensure that the rollout becomes available quickly on creation, the Argo Rollouts controller automatically treats the `argoproj/rollouts-demo:blue` initial container image specified in the `.spec.template.spec.containers.image` field as a stable version. In the initial instance, the creation of the `Rollout` resource routes all of the traffic towards the stable version of the application and skips the part where the traffic is sent to the canary version. However, for all subsequent application upgrades with the modifications to the `.spec.template.spec.containers.image` field, the Argo Rollouts controller performs the canary steps, as usual.

5.  Verify that your rollout was created correctly by running the following command:

    ``` terminal
    $ oc argo rollouts list rollouts -n <namespace>
    ```

    where:

    `<namespace>`
    Specifies the namespace where the `Rollout` resource is defined.

    **Example output:**

    ``` terminal
    NAME           STRATEGY   STATUS        STEP  SET-WEIGHT  READY  DESIRED  UP-TO-DATE  AVAILABLE
    rollouts-demo  Canary     Healthy       8/8   100         5/5    5        5           5
    ```

6.  Create the Kubernetes services that targets the `rollouts-demo` rollout.

    1.  In the **Administrator** perspective of the web console, click **Networking** → **Services**.

    2.  Click **Create Service** and enter the following configuration in the YAML view:

        ``` yaml
        apiVersion: v1
        kind: Service
        metadata:
          name: rollouts-demo
        spec:
          ports:
          - port: 80
            targetPort: http
            protocol: TCP
            name: http

          selector:
            app: rollouts-demo
        ```

        where:

        `spec.ports`
        Specifies the name of the port used by the application for running inside the container.

        `spec.selector`
        Specifies the selector to match pods. Ensure that the contents of the `selector` field are the same as in the `Rollout` custom resource (CR).

    3.  Click **Create**.

        Rollouts automatically update the created service with pod template hash of the canary `ReplicaSet`. For example, `rollouts-pod-template-hash: 687d76d795`.

7.  Watch the progression of your rollout by running the following command:

    ``` terminal
    $ oc argo rollouts get rollout rollouts-demo --watch -n <namespace>
    ```

    where:

    `<namespace>`
    Specifies the namespace where the `Rollout` resource is defined.

    **Example output:**

    ``` terminal
    Name:            rollouts-demo
    Namespace:       spring-petclinic
    Status:          ✔ Healthy
    Strategy:        Canary
      Step:          8/8
      SetWeight:     100
      ActualWeight:  100
    Images:          argoproj/rollouts-demo:blue (stable)
    Replicas:
      Desired:       5
      Current:       5
      Updated:       5
      Ready:         5
      Available:     5

    NAME                                       KIND        STATUS     AGE    INFO
    ⟳ rollouts-demo                            Rollout     ✔ Healthy  4m50s
    └──# revision:1
       └──⧉ rollouts-demo-687d76d795           ReplicaSet  ✔ Healthy  4m50s  stable
          ├──□ rollouts-demo-687d76d795-75k57  Pod         ✔ Running  4m49s  ready:1/1
          ├──□ rollouts-demo-687d76d795-bv5zf  Pod         ✔ Running  4m49s  ready:1/1
          ├──□ rollouts-demo-687d76d795-jsxg8  Pod         ✔ Running  4m49s  ready:1/1
          ├──□ rollouts-demo-687d76d795-rsgtv  Pod         ✔ Running  4m49s  ready:1/1
          └──□ rollouts-demo-687d76d795-xrmrj  Pod         ✔ Running  4m49s  ready:1/1
    ```

    After the rollout has been created, you can verify that the **Status** field of the rollout shows **Phase: Healthy**.

8.  In the **Rollout** tab, under the **Rollouts** section, verify that the **Status** field of the `rollouts-demo` rollout shows as **Phase: Healthy**.

    > [!TIP]
    > Alternatively, you can verify that the rollout is healthy by running the following command:
    >
    > ``` terminal
    > $ oc argo rollouts status rollouts-demo -n <namespace>
    > ```
    >
    > \+ Specify the namespace where the `Rollout` resource is defined.
    >
    > **Example output:**
    >
    > ``` terminal
    > Healthy
    > ```

    You are now ready to perform a canary deployment, with the next update of the `Rollout` CR.

</div>

# Updating the rollout

When you update the `.spec.template.spec` fields in the Rollout custom resource (CR), such as the container image version, the `ReplicaSet` creates new pods with the updated container image.

<div>

<div class="title">

Procedure

</div>

1.  Simulate the new canary version of the application by modifying the container image deployed in the rollout.

    1.  In the **Administrator** perspective of the web console, go to **Operators** → **Installed Operators** → **Red Hat OpenShift GitOps** → **Rollout**.

    2.  Select the existing `rollouts-demo` rollout and modify the `.spec.template.spec.containers.image` value from `argoproj/rollouts-demo:blue` to `argoproj/rollouts-demo:yellow` in the YAML view.

    3.  Click **Save** and then click **Reload**.

        The container image deployed in the rollout is modified and the rollout initiates a new canary deployment.

        > [!NOTE]
        > Initially, the `setWeight` value in `.spec.strategy.canary.steps` routes 20% of traffic to the canary version and pauses the rollout until promotion is requested.

        **Example route with 20% of traffic directed to the canary version and rollout is paused indefinitely until a request for promotion is specified in the subsequent step:**

        ``` yaml
        spec:
          replicas: 5
          strategy:
            canary:
              steps:
              - setWeight: 20
              - pause: {}
          # (...)
        ```

        where:

        `spec.strategy.canary`
        Specifies the deployment strategy that the rollout must use.

        `spec.strategy.canary.steps`
        Specifies the steps for the rollout. This example gradually routes 20%, 40%, 60%, and 80% of traffic to the canary version.

        `spec.strategy.canary.steps.setWeight`
        Specifies the percentage of traffic that must be directed to the canary version. A value of 20 means that 20% of traffic is directed to the canary version.

        `spec.strategy.canary.steps.pause`
        Instructs the Argo Rollouts controller to pause indefinitely until it finds a request for promotion.

2.  Watch the progression of your rollout by running the following command:

    ``` terminal
    $ oc argo rollouts get rollout rollouts-demo --watch -n <namespace>
    ```

    where:

    `<namespace>`
    Specifies the namespace where the `Rollout` CR is defined.

    **Example output:**

    ``` terminal
    Name:            rollouts-demo
    Namespace:       spring-petclinic
    Status:          ॥ Paused
    Message:         CanaryPauseStep
    Strategy:        Canary
      Step:          1/8
      SetWeight:     20
      ActualWeight:  20
    Images:          argoproj/rollouts-demo:blue (stable)
                     argoproj/rollouts-demo:yellow (canary)
    Replicas:
      Desired:       5
      Current:       5
      Updated:       1
      Ready:         5
      Available:     5

    NAME                                       KIND        STATUS     AGE    INFO
    ⟳ rollouts-demo                            Rollout     ॥ Paused   9m51s
    ├──# revision:2
    │  └──⧉ rollouts-demo-6cf78c66c5           ReplicaSet  ✔ Healthy  99s    canary
    │     └──□ rollouts-demo-6cf78c66c5-zrgd4  Pod         ✔ Running  98s    ready:1/1
    └──# revision:1
       └──⧉ rollouts-demo-687d76d795           ReplicaSet  ✔ Healthy  9m51s  stable
          ├──□ rollouts-demo-687d76d795-75k57  Pod         ✔ Running  9m50s  ready:1/1
          ├──□ rollouts-demo-687d76d795-jsxg8  Pod         ✔ Running  9m50s  ready:1/1
          ├──□ rollouts-demo-687d76d795-rsgtv  Pod         ✔ Running  9m50s  ready:1/1
          └──□ rollouts-demo-687d76d795-xrmrj  Pod         ✔ Running  9m50s  ready:1/1
    ```

    The rollout is now in a paused status, because there is no pause duration specified in the rollout’s update strategy configuration.

3.  Repeat the previous step to test the newly deployed version of application and ensure that it is working as expected. For example, verify the application by interacting with the application through the browser and try running tests or observing container logs.

    The rollout will remain paused until you advance it to the next step.

    After you verify that the new version of the application is working as expected, you can decide whether to continue with promotion or to cancel the rollout. Accordingly, follow the instructions in "Promoting the rollout" or "Manually aborting the rollout".

</div>

# Promoting the rollout

Because your rollout is now in a paused status, as a cluster administrator, you must now manually promote the rollout to allow it to progress to the next step.

<div>

<div class="title">

Procedure

</div>

1.  Simulate another new canary version of the application by running the following command in the Argo Rollouts CLI:

    ``` terminal
    $ oc argo rollouts promote rollouts-demo -n <namespace>
    ```

    where:

    `<namespace>`
    Specifies the namespace where the `Rollout` resource is defined.

    **Example output:**

    ``` terminal
    rollout 'rollouts-demo' promoted
    ```

    This increases the traffic weight to 40% in the canary version.

2.  Verify that the rollout progresses through the rest of the steps, by running the following command:

    ``` terminal
    $ oc argo rollouts get rollout rollouts-demo -n <namespace> --watch
    ```

    where:

    `<namespace>`
    Specifies the namespace where the `Rollout` resource is defined.

    Because the rest of the steps as defined in the `Rollout` CR have set durations, for example, `pause: {duration: 45}`, the Argo Rollouts controller waits that duration and then automatically moves to the next step.

    After all steps are completed successfully, the new `ReplicaSet` object is marked as the stable replica set.

    **Example output:**

    ``` terminal
    Name:            rollouts-demo
    Namespace:       spring-petclinic
    Status:          ✔ Healthy
    Strategy:        Canary
      Step:          8/8
      SetWeight:     100
      ActualWeight:  100
    Images:          argoproj/rollouts-demo:yellow (stable)
    Replicas:
      Desired:       5
      Current:       5
      Updated:       5
      Ready:         5
      Available:     5

    NAME                                       KIND        STATUS        AGE   INFO
    ⟳ rollouts-demo                            Rollout     ✔ Healthy     14m
    ├──# revision:2
    │  └──⧉ rollouts-demo-6cf78c66c5           ReplicaSet  ✔ Healthy     6m5s  stable
    │     ├──□ rollouts-demo-6cf78c66c5-zrgd4  Pod         ✔ Running     6m4s  ready:1/1
    │     ├──□ rollouts-demo-6cf78c66c5-g9kd5  Pod         ✔ Running     2m4s  ready:1/1
    │     ├──□ rollouts-demo-6cf78c66c5-2ptpp  Pod         ✔ Running     78s   ready:1/1
    │     ├──□ rollouts-demo-6cf78c66c5-tmk6c  Pod         ✔ Running     58s   ready:1/1
    │     └──□ rollouts-demo-6cf78c66c5-zv6lx  Pod         ✔ Running     47s   ready:1/1
    └──# revision:1
       └──⧉ rollouts-demo-687d76d795           ReplicaSet  • ScaledDown  14m
    ```

</div>

# Manually aborting the rollout

When using a canary deployment, the rollout deploys an initial canary version of the application. You can verify it either manually or programmatically. After you verify the canary version and promote it to stable, the new stable version is made available to all users.

However, sometimes bugs, errors, or deployment issues are discovered in the canary version, and you might want to abort the canary rollout and rollback to a stable version of your application.

Aborting a canary rollout deletes the resources of the new canary version and restores the previous stable version of your application. All network traffic such as ingress, route, or virtual service that was being directed to the canary returns to the original stable version.

The following example procedure deploys a new `red` canary version of your application, and then aborts it before it is fully promoted to stable.

<div>

<div class="title">

Procedure

</div>

1.  Update the container image version and modify the `.spec.template.spec.containers.image` value from `argoproj/rollouts-demo:yellow` to `argoproj/rollouts-demo:red` by running the following command in the Argo Rollouts CLI:

    ``` terminal
    $ oc argo rollouts set image rollouts-demo rollouts-demo=argoproj/rollouts-demo:red -n <namespace>
    ```

    where:

    `<namespace>`
    Specifies the namespace where the `Rollout` custom resource (CR) is defined.

    **Example output:**

    ``` terminal
    rollout "rollouts-demo" image updated
    ```

    The container image deployed in the rollout is modified and the rollout initiates a new canary deployment.

2.  Wait for the rollout to reach the paused status.

3.  Verify that the rollout deploys the `rollouts-demo:red` canary version and reaches the paused status by running the following command:

    ``` terminal
    $ oc argo rollouts get rollout rollouts-demo --watch -n <namespace>
    ```

    where:

    `<namespace>`
    Specifies the namespace where the `Rollout` CR is defined.

    **Example output:**

    ``` terminal
    Name:            rollouts-demo
    Namespace:       spring-petclinic
    Status:          ॥ Paused
    Message:         CanaryPauseStep
    Strategy:        Canary
      Step:          1/8
      SetWeight:     20
      ActualWeight:  20
    Images:          argoproj/rollouts-demo:red (canary)
                     argoproj/rollouts-demo:yellow (stable)
    Replicas:
      Desired:       5
      Current:       5
      Updated:       1
      Ready:         5
      Available:     5

    NAME                                       KIND        STATUS        AGE    INFO
    ⟳ rollouts-demo                            Rollout     ॥ Paused      17m
    ├──# revision:3
    │  └──⧉ rollouts-demo-5747959bdb           ReplicaSet  ✔ Healthy     75s    canary
    │     └──□ rollouts-demo-5747959bdb-fdrsg  Pod         ✔ Running     75s    ready:1/1
    ├──# revision:2
    │  └──⧉ rollouts-demo-6cf78c66c5           ReplicaSet  ✔ Healthy     9m45s  stable
    │     ├──□ rollouts-demo-6cf78c66c5-zrgd4  Pod         ✔ Running     9m44s  ready:1/1
    │     ├──□ rollouts-demo-6cf78c66c5-2ptpp  Pod         ✔ Running     4m58s  ready:1/1
    │     ├──□ rollouts-demo-6cf78c66c5-tmk6c  Pod         ✔ Running     4m38s  ready:1/1
    │     └──□ rollouts-demo-6cf78c66c5-zv6lx  Pod         ✔ Running     4m27s  ready:1/1
    └──# revision:1
       └──⧉ rollouts-demo-687d76d795           ReplicaSet  • ScaledDown  17m
    ```

4.  Abort the update of the rollout by running the following command:

    ``` terminal
    $ oc argo rollouts abort rollouts-demo -n <namespace>
    ```

    where:

    `<namespace>`
    Specifies the namespace where the `Rollout` CR is defined.

    **Example output:**

    ``` terminal
    rollout 'rollouts-demo' aborted
    ```

    The Argo Rollouts controller deletes the canary resources of the application, and rolls back to the stable version.

5.  Verify that after aborting the rollout, now the canary `ReplicaSet` is scaled to 0 replicas by running the following command:

    ``` terminal
    $ oc argo rollouts get rollout rollouts-demo --watch -n <namespace>
    ```

    where:

    `<namespace>`
    Specifies the namespace where the `Rollout` CR is defined.

    **Example output:**

    ``` terminal
    Name:            rollouts-demo
    Namespace:       spring-petclinic
    Status:          ✖ Degraded
    Message:         RolloutAborted: Rollout aborted update to revision 3
    Strategy:        Canary
      Step:          0/8
      SetWeight:     0
      ActualWeight:  0
    Images:          argoproj/rollouts-demo:yellow (stable)
    Replicas:
      Desired:       5
      Current:       5
      Updated:       0
      Ready:         5
      Available:     5

    NAME                                       KIND        STATUS        AGE    INFO
    ⟳ rollouts-demo                            Rollout     ✖ Degraded    24m
    ├──# revision:3
    │  └──⧉ rollouts-demo-5747959bdb           ReplicaSet  • ScaledDown  7m38s  canary
    ├──# revision:2
    │  └──⧉ rollouts-demo-6cf78c66c5           ReplicaSet  ✔ Healthy     16m    stable
    │     ├──□ rollouts-demo-6cf78c66c5-zrgd4  Pod         ✔ Running     16m    ready:1/1
    │     ├──□ rollouts-demo-6cf78c66c5-2ptpp  Pod         ✔ Running     11m    ready:1/1
    │     ├──□ rollouts-demo-6cf78c66c5-tmk6c  Pod         ✔ Running     11m    ready:1/1
    │     ├──□ rollouts-demo-6cf78c66c5-zv6lx  Pod         ✔ Running     10m    ready:1/1
    │     └──□ rollouts-demo-6cf78c66c5-mlbsh  Pod         ✔ Running     4m47s  ready:1/1
    └──# revision:1
       └──⧉ rollouts-demo-687d76d795           ReplicaSet  • ScaledDown  24m
    ```

    The rollout status is marked as `Degraded` indicating that even though the application has rolled back to the previous stable version, `yellow`, the rollout is not currently at the wanted version, `red`, that was set within the `.spec.template.spec.containers.image` field.

    > [!NOTE]
    > The `Degraded` status does not reflect the health of the application. It only indicates that there is a mismatch between the wanted and running container image versions.

6.  Update the container image version to the previous stable version, `yellow`, and modify the `.spec.template.spec.containers.image` value by running the following command:

    ``` terminal
    $ oc argo rollouts set image rollouts-demo rollouts-demo=argoproj/rollouts-demo:yellow -n <namespace>
    ```

    where:

    `<namespace>`
    Specifies the namespace where the `Rollout` CR is defined.

    **Example output:**

    ``` terminal
    rollout "rollouts-demo" image updated
    ```

    The rollout skips the analysis and promotion steps, rolls back to the previous stable version, `yellow`, and fast-tracks the deployment of the stable `ReplicaSet`.

7.  Verify that the rollout status is immediately marked as `Healthy` by running the following command:

    ``` terminal
    $ oc argo rollouts get rollout rollouts-demo --watch -n <namespace>
    ```

    where:

    `<namespace>`
    Specifies the namespace where the `Rollout` CR is defined.

    **Example output:**

    ``` terminal
    Name:            rollouts-demo
    Namespace:       spring-petclinic
    Status:          ✔ Healthy
    Strategy:        Canary
      Step:          8/8
      SetWeight:     100
      ActualWeight:  100
    Images:          argoproj/rollouts-demo:yellow (stable)
    Replicas:
      Desired:       5
      Current:       5
      Updated:       5
      Ready:         5
      Available:     5

    NAME                                       KIND        STATUS        AGE  INFO
    ⟳ rollouts-demo                            Rollout     ✔ Healthy     63m
    ├──# revision:4
    │  └──⧉ rollouts-demo-6cf78c66c5           ReplicaSet  ✔ Healthy     55m  stable
    │     ├──□ rollouts-demo-6cf78c66c5-zrgd4  Pod         ✔ Running     55m  ready:1/1
    │     ├──□ rollouts-demo-6cf78c66c5-2ptpp  Pod         ✔ Running     50m  ready:1/1
    │     ├──□ rollouts-demo-6cf78c66c5-tmk6c  Pod         ✔ Running     50m  ready:1/1
    │     ├──□ rollouts-demo-6cf78c66c5-zv6lx  Pod         ✔ Running     50m  ready:1/1
    │     └──□ rollouts-demo-6cf78c66c5-mlbsh  Pod         ✔ Running     44m  ready:1/1
    ├──# revision:3
    │  └──⧉ rollouts-demo-5747959bdb           ReplicaSet  • ScaledDown  46m
    └──# revision:1
       └──⧉ rollouts-demo-687d76d795           ReplicaSet  • ScaledDown  63m
    ```

</div>

# Additional resources

- [Installing Red Hat OpenShift GitOps](../installing_gitops/installing-openshift-gitops.md#installing-openshift-gitops)

- [Uninstalling Red Hat OpenShift GitOps](../removing_gitops/uninstalling-openshift-gitops.md#uninstalling-openshift-gitops)

- [`RolloutManager` Custom Resource specification](https://argo-rollouts-manager.readthedocs.io/en/latest/crd_reference/)

- [Argo Rollouts CLI overview](argo-rollouts-overview.md#gitops-argo-rollouts-cli-overview_argo-rollouts-overview)
