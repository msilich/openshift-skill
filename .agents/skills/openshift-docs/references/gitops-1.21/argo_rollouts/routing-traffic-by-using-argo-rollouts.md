<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

You can progressively route a subset of user traffic to a new application version by using Argo Rollouts and its traffic-splitting mechanisms. Then you can test whether the application is deployed and working.

With OpenShift Routes, you can configure Argo Rollouts to reduce or increase the amount of traffic by directing it to various applications in a cluster environment based on your requirements.

You can use OpenShift Routes to split traffic between two application versions:

- **Canary version**: A new version of an application where you gradually route the traffic.

- **Stable version**: The current version of an application. After the canary version is stable and has all the user traffic directed to it, it becomes the new stable version. The previous stable version is discarded.

# Prerequisites

- You have logged in to the OpenShift Container Platform cluster as an administrator.

- You have installed [Red Hat OpenShift GitOps](../installing_gitops/installing-openshift-gitops.md#installing-openshift-gitops) on your OpenShift Container Platform cluster.

- You have installed [Argo Rollouts](using-argo-rollouts-for-progressive-deployment-delivery.md#gitops-creating-rolloutmanager-custom-resource_using-argo-rollouts-for-progressive-deployment-delivery) on your OpenShift Container Platform cluster.

- You have installed the [Red Hat OpenShift GitOps CLI](../installing_gitops/installing-argocd-gitops-cli.md#installing-argocd-gitops-cli) on your system.

- You have installed the [Argo Rollouts CLI](using-argo-rollouts-for-progressive-deployment-delivery.md#gitops-installing-argo-rollouts-cli-on-linux_using-argo-rollouts-for-progressive-deployment-delivery) on your system.

# Configuring Argo Rollouts to route traffic by using OpenShift Routes

You can use OpenShift Routes to configure Argo Rollouts to create routes, rollouts, and services.

The following example procedure creates a route, a rollout, and two services. It then gradually routes an increasing percentage of traffic to a canary version of the application before that canary state is marked as successful and becomes the new stable version.

<div>

<div class="title">

Prerequisites

</div>

- You have logged in to the OpenShift Container Platform cluster as an administrator.

- You have installed the Red Hat OpenShift GitOps on your OpenShift Container Platform cluster.

- You have installed Argo Rollouts on your OpenShift Container Platform cluster. For more information, see "Creating a RolloutManager custom resource".

- You have installed the Red Hat OpenShift GitOps CLI on your system. For more information, see "Installing the GitOps CLI".

- You have installed the Argo Rollouts CLI on your system. For more information, see "Argo Rollouts CLI overview".

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create a `Route` object.

    1.  In the **Administrator** perspective of the web console, click **Networking** → **Routes**.

    2.  Click **Create Route**.

    3.  On the **Create Route** page, click **YAML view** and add the following snippet:

        The following example creates a route called `rollouts-demo-route`:

        ``` yaml
        apiVersion: route.openshift.io/v1
        kind: Route
        metadata:
          name: rollouts-demo-route
        spec:
          port:
            targetPort: http
          tls:
            insecureEdgeTerminationPolicy: Redirect
            termination: edge
          to:
            kind: Service
            name: argo-rollouts-stable-service
            weight: 100

          alternateBackends:
            - kind: Service
              name: argo-rollouts-canary-service
              weight: 0
        ```

        where:

        `spec.port.targetPort`
        Specifies the port name that the application uses to run inside the container.

        `spec.tls`
        Specifies the TLS configuration used to secure the route.

        `spec.to.name`
        Specifies the name of the targeted stable service.

        `spec.to.weight`
        Specifies the traffic weight for the stable service. The Route Rollout plugin automatically modifies this field to the stable weight.

        `spec.alternateBackends.name`
        Specifies the name of the targeted canary service.

        `spec.alternateBackends.weight`
        Specifies the traffic weight for the canary service. The Route Rollout plugin automatically modifies this field to the canary weight.

    4.  Click **Create** to create the route. It is then displayed on the **Routes** page.

2.  Create the services, canary and stable, to be referenced in the route.

    1.  In the **Administrator** perspective of the web console, click **Networking** → **Services**.

    2.  Click **Create Service**.

    3.  On the **Create Service** page, click **YAML view** and add the following snippet:

        The following example creates a canary service called `argo-rollouts-canary-service`. Canary traffic is directed to this service.

        ``` yaml
        apiVersion: v1
        kind: Service
        metadata:
          name: argo-rollouts-canary-service
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
        Specifies the port name that the application uses to run inside the container.

        `spec.selector`
        Specifies the selector to match pods. Ensure that the contents of the `selector` field are the same as in stable service and `Rollout` custom resource (CR).

        > [!IMPORTANT]
        > Ensure that the name of the canary service specified in the `Route` object matches with the name of the canary service specified in the `Service` object.

    4.  Click **Create** to create the canary service.

        Rollouts automatically update the created service with pod template hash of the canary `ReplicaSet`. For example, `rollouts-pod-template-hash: 7bf84f9696`.

    5.  Repeat these steps to create the stable service:

        The following example creates a stable service called `argo-rollouts-stable-service`. Stable traffic is directed to this service.

        ``` yaml
        apiVersion: v1
        kind: Service
        metadata:
          name: argo-rollouts-stable-service
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
        Specifies the port name that the application uses to run inside the container.

        `spec.selector`
        Specifies the selector to match pods. Ensure that the contents of the `selector` field are the same as in canary service and `Rollout` CR.

        > [!IMPORTANT]
        > Ensure that the name of the stable service specified in the `Route` object matches with the name of the stable service specified in the `Service` object.

    6.  Click **Create** to create the stable service.

        Rollouts automatically update the created service with pod template hash of the stable `ReplicaSet`. For example, `rollouts-pod-template-hash: 1b6a7733`.

3.  Create the `Rollout` CR to reference the `Route` and `Service` objects.

    1.  In the **Administrator** perspective of the web console, go to **Operators** → **Installed Operators** → **Red Hat OpenShift GitOps** → **Rollout**.

    2.  On the **Create Rollout** page, click **YAML view** and add the following snippet:

        The following example creates a `Rollout` CR called `rollouts-demo`:

        ``` yaml
        apiVersion: argoproj.io/v1alpha1
        kind: Rollout
        metadata:
          name: rollouts-demo
        spec:
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

          revisionHistoryLimit: 2
          replicas: 5
          strategy:
            canary:
              canaryService: argo-rollouts-canary-service
              stableService: argo-rollouts-stable-service
              trafficRouting:
                plugins:
                  argoproj-labs/openshift:
                    routes:
                      - rollouts-demo-route
              steps:
              - setWeight: 30
              - pause: {}
              - setWeight: 60
              - pause: {}
          selector:
            matchLabels:
              app: rollouts-demo
        ```

        where:

        `spec.template`
        Specifies the pods that are to be created.

        `spec.strategy.canary.canaryService`
        Specifies the name of the canary service. This value must match the name of the created canary `Service`.

        `spec.strategy.canary.stableService`
        Specifies the name of the stable service. This value must match the name of the created stable `Service`.

        `spec.strategy.canary.trafficRouting.plugins.argoproj-labs/openshift.routes`
        Specifies the name of the route. This value must match the name of the created `Route` CR.

        `spec.strategy.canary.steps`
        Specifies the steps for the rollout. This example gradually routes 30%, 60%, and 100% of traffic to the canary version.

        `spec.selector`
        Specifies the selector to match pods. Ensure that the contents of the `selector` field are the same as in canary and stable service.

    3.  Click **Create**.

    4.  In the **Rollout** tab, under the **Rollout** section, verify that the **Status** field of the rollout shows **Phase: Healthy**.

4.  Verify that the route is directing 100% of the traffic towards the stable version of the application.

    > [!NOTE]
    > When the first instance of the `Rollout` resource is created, the rollout regulates the amount of traffic to be directed towards the stable and canary application versions. In the initial instance, the creation of the `Rollout` resource routes all of the traffic towards the stable version of the application and skips the part where the traffic is sent to the canary version.

    1.  Go to **Networking** → **Routes** and look for the `Route` resource you want to verify.

    2.  Select the **YAML** tab and view the following snippet:

        **Example route**

        ``` yaml
        kind: Route
        metadata:
          name: rollouts-demo-route
        spec:
          alternateBackends:
          - kind: Service
            name: argo-rollouts-canary-service
            weight: 0
          # (...)
          to:
            kind: Service
            name: argo-rollouts-stable-service
            weight: 100
        ```

        where:

        `alternateBackends.weight`
        Specifies the percentage of traffic directed to the canary version. A value of `0` means that 0% of traffic is directed to the canary version.

        `to.weight`
        Specifies the percentage of traffic directed to the stable version. A value of `100` means that 100% of traffic is directed to the stable version.

5.  Simulate the new canary version of the application by modifying the container image deployed in the rollout.

    1.  In the **Administrator** perspective of the web console, go to **Operators** → **Installed Operators** → **Red Hat OpenShift GitOps** → **Rollout**.

    2.  Select the existing **Rollout** and modify the `.spec.template.spec.containers.image` value from `argoproj/rollouts-demo:blue` to `argoproj/rollouts-demo:yellow`.

        As a result, the container image deployed in the rollout is modified and the rollout initiates a new canary deployment.

        > [!NOTE]
        > As per the `setWeight` property defined in the `.spec.strategy.canary.steps` field of the `Rollout` resource, initially 30% of traffic to the route reaches the canary version and 70% of traffic is directed towards the stable version. The rollout is paused after 30% of traffic is directed to the canary version.

        **Example route with 30% of traffic directed to the canary version and 70% directed to the stable version:**

        ``` yaml
        spec:
          alternateBackends:
          - kind: Service
            name: argo-rollouts-canary-service
            weight: 30
          # (...)
          to:
            kind: Service
            name: argo-rollouts-stable-service
            weight: 70
        ```

6.  Simulate another new canary version of the application by running the following command in the Argo Rollouts CLI:

    ``` terminal
    $ oc argo rollouts promote rollouts-demo -n <namespace>
    ```

    where:

    `<namespace>`
    Specifies the namespace where the `Rollout` resource is defined.

    This increases the traffic weight to 60% in the canary version and 40% in the stable version.

    **Example route with 60% of traffic directed to the canary version and 40% directed to the stable version:**

    ``` yaml
    spec:
      alternateBackends:
      - kind: Service
        name: argo-rollouts-canary-service
        weight: 60
      # (...)
      to:
        kind: Service
        name: argo-rollouts-stable-service
        weight: 40
    ```

7.  Increase the traffic weight in the canary version to 100% and discard the traffic in the old stable version of the application by running the following command:

    ``` terminal
    $ oc argo rollouts promote rollouts-demo -n <namespace>
    ```

    where:

    `<namespace>`
    Specifies the namespace where the `Rollout` resource is defined.

    **Example route with 0% of traffic directed to the canary version and 100% directed to the stable version:**

    ``` yaml
    spec:
      # (...)
      to:
        kind: Service
        name: argo-rollouts-stable-service
        weight: 100
    ```

</div>

# Additional resources

- [Configuring the GitOps CLI](../gitops_cli_argocd/configuring-argocd-gitops-cli.md#configuring-argocd-gitops-cli)

- [Argo Rollouts CLI overview](argo-rollouts-overview.md#gitops-argo-rollouts-cli-overview_argo-rollouts-overview)
