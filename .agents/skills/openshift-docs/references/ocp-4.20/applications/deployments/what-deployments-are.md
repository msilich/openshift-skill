<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

You can use `Deployment` and `DeploymentConfig` objects in OpenShift Container Platform to describe the desired state of an application and to manage pods through replica sets or replication controllers. Use `Deployment` objects unless you need a feature that only `DeploymentConfig` objects provide.

The `Deployment` and `DeploymentConfig` API objects provide two similar but different methods for fine-grained management over common user applications. They are composed of the following separate API objects:

- A `Deployment` or `DeploymentConfig` object, either of which describes the desired state of a particular component of the application as a pod template.

- `Deployment` objects involve one or more *replica sets*, which contain a point-in-time record of the state of a deployment as a pod template. Similarly, `DeploymentConfig` objects involve one or more *replication controllers*, which preceded replica sets.

- One or more pods, which represent an instance of a particular version of an application.

> [!IMPORTANT]
> As of OpenShift Container Platform 4.14, `DeploymentConfig` objects are deprecated. `DeploymentConfig` objects are still supported, but are not recommended for new installations. Only security-related and critical issues will be fixed.
>
> Instead, use `Deployment` objects or another alternative to provide declarative updates for pods.

# Building blocks of a deployment

Deployments and deployment configs are enabled by the use of native Kubernetes API objects `ReplicaSet` and `ReplicationController`, respectively, as their building blocks.

Users do not have to manipulate replica sets, replication controllers, or pods owned by `Deployment` or `DeploymentConfig` objects. The deployment systems ensure changes are propagated appropriately.

> [!TIP]
> If the existing deployment strategies are not suited for your use case and you must run manual steps during the lifecycle of your deployment, then you should consider creating a custom deployment strategy.

The following sections provide further details on these objects.

## Replica sets

To keep a specified number of identical pods running in OpenShift Container Platform, you can use a Kubernetes `ReplicaSet` object. Deployments create and manage replica sets for you, so use a replica set directly only when you need custom update orchestration or no updates at all.

> [!NOTE]
> Only use replica sets if you require custom update orchestration or do not require updates at all. Otherwise, use deployments. Replica sets can be used independently, but are used by deployments to orchestrate pod creation, deletion, and updates. Deployments manage their replica sets automatically, provide declarative updates to pods, and do not have to manually manage the replica sets that they create.

The following is an example `ReplicaSet` definition:

``` yaml
apiVersion: apps/v1
kind: ReplicaSet
metadata:
  name: frontend-1
  labels:
    tier: frontend
spec:
  replicas: 3
  selector:
    matchLabels:
      tier: frontend
    matchExpressions:
      - {key: tier, operator: In, values: [frontend]}
  template:
    metadata:
      labels:
        tier: frontend
    spec:
      containers:
      - image: openshift/hello-openshift
        name: helloworld
        ports:
        - containerPort: 8080
          protocol: TCP
      restartPolicy: Always
```

- `spec.selector` is a label query over a set of resources. The result of `matchLabels` and `matchExpressions` are logically conjoined.

- `spec.selector.matchLabels` is an equality-based selector that specifies resources with labels that match the selector.

- `spec.selector.matchExpressions` is a set-based selector that filters keys. This parameter selects all resources with key equal to `tier` and value equal to `frontend`.

## Replication controllers

To keep a specified number of identical pods running in OpenShift Container Platform, you can use a replication controller. Create one through a `DeploymentConfig` object rather than directly, and use a replica set instead when you need set-based selectors or custom update orchestration.

Similar to a replica set, a replication controller ensures that a specified number of replicas of a pod are running at all times. If pods exit or are deleted, the replication controller instantiates more up to the defined number. Likewise, if there are more running than desired, it deletes as many as necessary to match the defined amount. The difference between a replica set and a replication controller is that a replica set supports set-based selector requirements whereas a replication controller only supports equality-based selector requirements.

A replication controller configuration consists of:

- The number of replicas desired, which can be adjusted at run time.

- A `Pod` definition to use when creating a replicated pod.

- A selector for identifying managed pods.

A selector is a set of labels assigned to the pods that are managed by the replication controller. These labels are included in the `Pod` definition that the replication controller instantiates. The replication controller uses the selector to determine how many instances of the pod are already running in order to adjust as needed.

The replication controller does not perform auto-scaling based on load or traffic, as it does not track either. Rather, this requires its replica count to be adjusted by an external auto-scaler.

> [!NOTE]
> Use a `DeploymentConfig` to create a replication controller instead of creating replication controllers directly.
>
> If you require custom orchestration or do not require updates, use replica sets instead of replication controllers.

The following is an example definition of a replication controller:

``` yaml
apiVersion: v1
kind: ReplicationController
metadata:
  name: frontend-1
spec:
  replicas: 1
  selector:
    name: frontend
  template:
    metadata:
      labels:
        name: frontend
    spec:
      containers:
      - image: openshift/hello-openshift
        name: helloworld
        ports:
        - containerPort: 8080
          protocol: TCP
      restartPolicy: Always
```

- `spec.replicas` specifies the number of copies of the pod to run.

- `spec.selector` specifies the label selector of the pod to run.

- `spec.template` specifies the template for the pod the controller creates.

- `spec.template.metadata.labels` specifies the labels that the pod should include from the label selector.

- `spec.template.metadata.labels.name` specifies the name of the labels. The maximum name length after expanding any parameters is 63 characters.

# Deployments

To run and update application pods in OpenShift Container Platform, you can use a Kubernetes `Deployment` object. A deployment describes the desired state of an application component as a pod template and creates replica sets that manage pod lifecycles.

For example, the following deployment definition creates a replica set to bring up one `hello-openshift` pod:

<div class="formalpara">

<div class="title">

Deployment definition

</div>

``` yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: hello-openshift
spec:
  replicas: 1
  selector:
    matchLabels:
      app: hello-openshift
  template:
    metadata:
      labels:
        app: hello-openshift
    spec:
      containers:
      - name: hello-openshift
        image: openshift/hello-openshift:latest
        ports:
        - containerPort: 80
```

</div>

# DeploymentConfig objects

> [!IMPORTANT]
> As of OpenShift Container Platform 4.14, `DeploymentConfig` objects are deprecated. `DeploymentConfig` objects are still supported, but are not recommended for new installations. Only security-related and critical issues will be fixed.
>
> Instead, use `Deployment` objects or another alternative to provide declarative updates for pods.

You can use `DeploymentConfig` objects in OpenShift Container Platform to roll out image updates, run lifecycle hooks, trigger automated deployments, and scale or roll back applications. A `DeploymentConfig` object builds on replication controllers to manage the application deployment lifecycle.

Building on replication controllers, OpenShift Container Platform adds expanded support for the software development and deployment lifecycle with the concept of `DeploymentConfig` objects. In the simplest case, a `DeploymentConfig` object creates a new replication controller and lets it start up pods.

However, OpenShift Container Platform deployments from `DeploymentConfig` objects also provide the ability to transition from an existing deployment of an image to a new one and also define hooks to be run before or after creating the replication controller.

The `DeploymentConfig` deployment system provides the following capabilities:

- A `DeploymentConfig` object, which is a template for running applications.

- Triggers that drive automated deployments in response to events.

- User-customizable deployment strategies to transition from the previous version to the new version. A strategy runs inside a pod commonly referred as the deployment process.

- A set of hooks (lifecycle hooks) for executing custom behavior in different points during the lifecycle of a deployment.

- Versioning of your application to support rollbacks either manually or automatically in case of deployment failure.

- Manual replication scaling and autoscaling.

When you create a `DeploymentConfig` object, a replication controller is created representing the `DeploymentConfig` object’s pod template. If the deployment changes, a new replication controller is created with the latest pod template, and a deployment process runs to scale down the old replication controller and scale up the new one.

Instances of your application are automatically added and removed from both service load balancers and routers as they are created. As long as your application supports graceful shutdown when it receives the `TERM` signal, you can ensure that running user connections are given a chance to complete normally.

The OpenShift Container Platform `DeploymentConfig` object defines the following details:

1.  The elements of a `ReplicationController` definition.

2.  Triggers for creating a new deployment automatically.

3.  The strategy for transitioning between deployments.

4.  Lifecycle hooks.

Each time a deployment is triggered, whether manually or automatically, a deployer pod manages the deployment (including scaling down the old replication controller, scaling up the new one, and running hooks). The deployment pod remains for an indefinite amount of time after it completes the deployment to retain its logs of the deployment. When a deployment is superseded by another, the previous replication controller is retained to enable easy rollback if needed.

<div class="formalpara">

<div class="title">

Example `DeploymentConfig` definition

</div>

``` yaml
apiVersion: apps.openshift.io/v1
kind: DeploymentConfig
metadata:
  name: frontend
spec:
  replicas: 5
  selector:
    name: frontend
  template: { ... }
  triggers:
  - type: ConfigChange
  - imageChangeParams:
      automatic: true
      containerNames:
      - helloworld
      from:
        kind: ImageStreamTag
        name: hello-openshift:latest
    type: ImageChange
  strategy:
    type: Rolling
```

</div>

- `spec.triggers.type.ConfigChange` is a configuration change trigger that creates a new replication controller whenever changes are detected in the pod template of the deployment configuration.

- `spec.triggers.type.ImageChange` is an image change trigger that causes a new deployment to be created each time a new version of the backing image is available in the named image stream.

- `spec.strategy.type.Rolling` is the default strategy that makes a downtime-free transition between deployments.

# Comparing Deployment and DeploymentConfig objects

You can use both Kubernetes `Deployment` objects and OpenShift Container Platform `DeploymentConfig` objects to manage application rollouts. Before deciding which to use, understand the differences between the two objects in design and supported features.

Use `Deployment` objects unless you need a capability that only `DeploymentConfig` objects provide.

The following sections go into more detail on the differences between the two object types to further help you decide which type to use.

> [!IMPORTANT]
> As of OpenShift Container Platform 4.14, `DeploymentConfig` objects are deprecated. `DeploymentConfig` objects are still supported, but are not recommended for new installations. Only security-related and critical issues will be fixed.
>
> Instead, use `Deployment` objects or another alternative to provide declarative updates for pods.

## Design

One important difference between `Deployment` and `DeploymentConfig` objects is the properties of the [CAP theorem](https://en.wikipedia.org/wiki/CAP_theorem) that each design has chosen for the rollout process. `DeploymentConfig` objects prefer consistency, whereas `Deployments` objects take availability over consistency.

For `DeploymentConfig` objects, if a node running a deployer pod goes down, it will not get replaced. The process waits until the node comes back online or is manually deleted. Manually deleting the node also deletes the corresponding pod. This means that you can not delete the pod to unstick the rollout, as the kubelet is responsible for deleting the associated pod.

However, deployment rollouts are driven from a controller manager. The controller manager runs in high availability mode on masters and uses leader election algorithms to value availability over consistency. During a failure it is possible for other masters to act on the same deployment at the same time, but this issue will be reconciled shortly after the failure occurs.

## Deployment-specific features

You can use `Deployment` objects in OpenShift Container Platform to roll out multiple sets of rollouts, scale ongoing rollouts during updates, or pause mid-rollout. These capabilities differ from `DeploymentConfig` objects and can make application updates faster and more flexible.

### Rollover

The deployment process for `Deployment` objects is driven by a controller loop, in contrast to `DeploymentConfig` objects that use deployer pods for every new rollout. This means that the `Deployment` object can have as many active replica sets as possible, and eventually the deployment controller will scale down all old replica sets and scale up the newest one.

`DeploymentConfig` objects can have at most one deployer pod running, otherwise multiple deployers might conflict when trying to scale up what they think should be the newest replication controller. Because of this, only two replication controllers can be active at any point in time. Ultimately, this results in faster rapid rollouts for `Deployment` objects.

### Proportional scaling

Because the deployment controller is the sole source of truth for the sizes of new and old replica sets owned by a `Deployment` object, it can scale ongoing rollouts. Additional replicas are distributed proportionally based on the size of each replica set.

`DeploymentConfig` objects cannot be scaled when a rollout is ongoing because the controller will have issues with the deployer process about the size of the new replication controller.

### Pausing mid-rollout

Deployments can be paused at any point in time, meaning you can also pause ongoing rollouts. However, you currently cannot pause deployer pods; if you try to pause a deployment in the middle of a rollout, the deployer process is not affected and continues until it finishes.

## DeploymentConfig object-specific features

When using `DeploymentConfig` objects in OpenShift Container Platform, you can set Lifecycle hooks and configure custom deployment strategies. `DeploymentConfig` objects also provide automatic replica set rollbacks upon failure and automatic roll out of updates.

These capabilities are specific to `DeploymentConfig` objects and are not available on Kubernetes `Deployment` objects.

### Automatic rollbacks

Currently, deployments do not support automatically rolling back to the last successfully deployed replica set in case of a failure.

### Triggers

Deployments have an implicit config change trigger in that every change in the pod template of a deployment automatically triggers a new rollout. If you do not want new rollouts on pod template changes, pause the deployment:

``` terminal
$ oc rollout pause deployments/<name>
```

### Lifecycle hooks

Deployments do not yet support any lifecycle hooks.

### Custom strategies

Deployments do not support user-specified custom deployment strategies.
