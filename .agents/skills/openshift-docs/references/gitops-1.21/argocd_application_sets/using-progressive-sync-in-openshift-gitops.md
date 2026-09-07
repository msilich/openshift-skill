<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

> [!IMPORTANT]
> Progressive Sync is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.
>
> For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

Progressive Sync is an advanced feature that supports application rollout strategies by managing synchronization across multiple clusters. You can configure `ApplicationSet` strategies to control how applications are created, updated, and deleted, as well as how to enable and use the **Progressive Sync** status panel in the **Application details** view.

You can configure creation strategies (`AllAtOnce` or `RollingSync`) to control application deployment patterns and deletion strategies to manage application removal order. When you enable Progressive Sync and configure a `RollingSync` strategy, the Red Hat OpenShift GitOps console displays real-time visibility into sync waves, application health, and deployment progress.

> [!NOTE]
> To monitor Progressive Sync status in the GitOps Web UI, ensure that the feature is enabled in your Argo CD controller and your `ApplicationSet` uses a `RollingSync` strategy.

Enable Progressive Sync, configure `ApplicationSet` strategies, and monitor rollout behavior.

# Prerequisites

- You have logged in to the OpenShift Container Platform cluster as an administrator.

- You have installed the GitOps Operator on your OpenShift Container Platform cluster.

- You can access the default Argo CD instance in the `openshift-gitops` namespace.

- You have created an Argo CD `ApplicationSet` resource in your defined namespace, for example, `openshift-gitops`.

# Overview of enabling Progressive Sync

Progressive Sync in GitOps enables administrators to orchestrate safe, staged rollouts of changes across groups of applications.

When enabled:

- The UI displays rollout wave, health, and messages for each application.

- Teams can track rollout progress, identify bottlenecks, and ensure compliance with deployment policies.

- A new section, **Progressive Sync**, appears in the Application details panel when an application is managed by an `ApplicationSet` controller with the `RollingSync` strategy.

This feature enhances transparency for multi-wave, staged, or progressive deployments managed through GitOps.

# Enabling Progressive Sync

Progressive Sync is not enabled by default. You must explicitly enable this feature for the `ApplicationSet` controller in GitOps. You can enable this feature using either one of the following two methods:

- Add the `extraCommandArgs` argument to the Argo CD CR

- Set the `env` environment variable in the Argo CD CR

## Adding the extraCommandArgs argument to the Argo CD CR

You can enable Progressive Sync by adding the `extraCommandArgs` argument in the `spec` section of your Argo CD CR.

<div>

<div class="title">

Procedure

</div>

1.  Log in to the OpenShift Container Platform web console.

2.  In the **Administrator** perspective of the web console, click **Operators** → **Installed Operators**.

3.  From the **Project** list, select the default Argo CD instance in the `openshift-gitops` namespace.

4.  From the installed Operators list, select **Red Hat OpenShift GitOps**, and then click the **Argo CD** tab.

5.  Add the following YAML configuration in the `spec` section of the Argo CD instance.

    **Example adding the `enable-progressive-syncs` parameter:**

    ``` yaml
    apiVersion: argoproj.io/v1alpha1
    kind: ArgoCD
    metadata:
      name: openshift-gitops
      namespace: openshift-gitops
    spec:
      applicationSet:
        extraCommandArgs:
        - --enable-progressive-syncs
    ```

6.  Click **Save**.

    The Operator automatically reconciles and updates the `ApplicationSet` controller deployment.

</div>

## Setting the env environment variable in the Argo CD CR

You can also enable Progressive Sync by setting the `env` environment variable in the Argo CD CR.

<div>

<div class="title">

Procedure

</div>

1.  Log in to the OpenShift Container Platform web console.

2.  In the **Administrator** perspective of the web console, click **Operators** → **Installed Operators**.

3.  From the **Project** list, select the default Argo CD instance in the `openshift-gitops` namespace.

4.  From the installed Operators list, select **Red Hat OpenShift GitOps**, and then click the **Argo CD** tab.

5.  Add the following YAML configuration in the `spec` section of the Argo CD instance.

    **Example adding the `enable-progressive-syncs` parameter:**

    ``` yaml
    apiVersion: argoproj.io/v1alpha1
    kind: ArgoCD
    metadata:
      name: openshift-gitops
      namespace: openshift-gitops
    spec:
      applicationSet:
        env:
        - name: ARGOCD_APPLICATIONSET_CONTROLLER_ENABLE_PROGRESSIVE_SYNCS
          value: "true"
    ```

6.  Click **Save**.

    The Operator automatically reconciles and updates the `ApplicationSet` controller deployment.

</div>

# Understanding ApplicationSet strategies

ApplicationSet strategies provide control over both application lifecycle operations: creation and deletion. These operations are configured using separate fields in the ApplicationSet specification, allowing you to independently control deployment patterns and cleanup sequences.

The strategy configuration consists of two primary components:

Creation strategy (`type` field)
Controls how applications are created and updated when the ApplicationSet resource is modified. This determines the deployment pattern for applications managed by the ApplicationSet.

Deletion strategy (`deletionOrder` field)
Controls the order in which applications are deleted when they are removed from the ApplicationSet. This ensures proper cleanup sequences, particularly when managing dependent services.

> [!NOTE]
> The ApplicationSet finalizer is not removed until all applications are successfully deleted. This ensures proper cleanup and prevents the ApplicationSet from being removed before its managed applications.

> [!IMPORTANT]
> ApplicationSet strategies apply only when progressive sync is enabled. If progressive sync is not enabled, the configured strategies are ignored, and applications are processed using the default ApplicationSet behavior.

# Understanding creation strategies

The `type` field in the ApplicationSet strategy configuration controls how applications are created and updated. Red Hat OpenShift GitOps supports two creation strategies: AllAtOnce and RollingSync.

AllAtOnce
All applications managed by the ApplicationSet resource are created or updated simultaneously when the ApplicationSet is applied or modified. This is the default creation strategy.

RollingSync
Applications are created or updated in stages based on labels present on the generated Application resources. When the ApplicationSet is applied or modified, changes are applied to each group of Application resources sequentially according to the steps defined in the `rollingSync` configuration.

When using the RollingSync strategy, the following behavior applies:

- Applications are grouped by labels and processed sequentially according to the defined steps.

- Each step processes applications matching the specified label selectors.

- The next step begins only after applications in the current step reach a healthy state.

- Applications not selected in any step are excluded from the rolling sync and must be manually synced through the CLI or UI.

> [!IMPORTANT]
> When using RollingSync strategy, ensure that all applications you want to update are covered by at least one step’s label selectors. Applications not matched by any step will not be automatically updated.

## Configuring AllAtOnce creation strategy

You can configure the AllAtOnce creation strategy to update all applications managed by the ApplicationSet simultaneously. This is the default behavior, but you can explicitly configure it for clarity in your ApplicationSet specification.

<div>

<div class="title">

Prerequisites

</div>

- You have created an ApplicationSet resource.

- You have access to edit the ApplicationSet configuration.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Edit the ApplicationSet custom resource:

    ``` terminal
    $ oc edit applicationset <applicationset_name> -n <namespace>
    ```

    where:

    `<applicationset_name>`
    Specifies the name of your ApplicationSet resource.

    `<namespace>`
    Specifies the namespace where the ApplicationSet is deployed.

2.  Add or update the `spec.strategy` section with the AllAtOnce type:

    ``` yaml
    apiVersion: argoproj.io/v1alpha1
    kind: ApplicationSet
    metadata:
      name: <applicationset_name>
      namespace: <namespace>
    spec:
      strategy:
        type: AllAtOnce
      # ... other ApplicationSet configuration
    ```

    where:

    `metadata.name`
    Specifies the name of your ApplicationSet resource.

    `metadata.namespace`
    Specifies the namespace where the ApplicationSet is deployed.

    `spec.type`
    Specifies the creation strategy type. Set to `AllAtOnce` to update all applications simultaneously.

3.  Save the changes to apply the configuration.

</div>

<div>

<div class="title">

Verification

</div>

1.  Verify that the strategy is configured:

    ``` terminal
    $ oc get applicationset <applicationset_name> -n <namespace> -o jsonpath='{.spec.strategy.type}'
    ```

    **Example output:**

    ``` terminal
    AllAtOnce
    ```

2.  When you update the ApplicationSet, observe that all applications are updated simultaneously:

    ``` terminal
    $ oc get applications -n <namespace> -l app.kubernetes.io/instance=<applicationset_name>
    ```

</div>

## Example: AllAtOnce creation strategy for simultaneous deployment

The following example illustrates how to configure AllAtOnce creation strategy to deploy all applications simultaneously across multiple clusters:

``` yaml
apiVersion: argoproj.io/v1alpha1
kind: ApplicationSet
metadata:
  name: monitoring-apps
  namespace: openshift-gitops
spec:
  strategy:
    type: AllAtOnce
  generators:
    - list:
        elements:
          - cluster: us-east-cluster
            url: https://us-east-cluster.example.com
            region: us-east
          - cluster: us-west-cluster
            url: https://us-west-cluster.example.com
            region: us-west
          - cluster: eu-central-cluster
            url: https://eu-central-cluster.example.com
            region: eu-central
  template:
    metadata:
      name: 'monitoring-{{cluster}}'
      labels:
        region: '{{region}}'
    spec:
      project: default
      source:
        repoURL: https://github.com/example/monitoring-stack.git
        targetRevision: HEAD
        path: manifests
      destination:
        server: '{{url}}'
        namespace: monitoring
      syncPolicy:
        automated:
          prune: true
          selfHeal: true
```

In this example:

- All applications are created and updated simultaneously across all three clusters.

- The AllAtOnce strategy is suitable for this monitoring stack deployment because all cluster monitoring instances are independent and do not have dependencies on each other.

- When the ApplicationSet is updated, all monitoring applications across all regions receive the update at the same time.

- This approach ensures consistent monitoring coverage is deployed across all clusters without delays.

## Configuring RollingSync strategy

You can configure the RollingSync strategy to update applications in stages based on labels. This allows you to group applications and update them sequentially, providing controlled progressive deployment. When Progressive Sync is enabled, the rollout status is displayed in the GitOps Web UI.

<div>

<div class="title">

Prerequisites

</div>

- You have created an ApplicationSet resource.

- Applications generated by the ApplicationSet have labels that can be used for grouping.

- You have access to edit the ApplicationSet configuration.

- You have enabled Progressive Sync in your Argo CD instance if you want to view rollout status in the UI.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create or edit the ApplicationSet custom resource with the RollingSync strategy:

    ``` yaml
    apiVersion: argoproj.io/v1alpha1
    kind: ApplicationSet
    metadata:
      name: guestbook-rollingsync
      namespace: openshift-gitops
    spec:
      generators:
        - list:
            elements:
              - cluster: in-cluster
                env: dev
              - cluster: in-cluster
                env: qa
              - cluster: in-cluster
                env: prod
      strategy:
        type: RollingSync
        rollingSync:
          steps:
            - matchExpressions:
                - key: envLabel
                  operator: In
                  values: [dev]
            - matchExpressions:
                - key: envLabel
                  operator: In
                  values: [qa]
              maxUpdate: 0
            - matchExpressions:
                - key: envLabel
                  operator: In
                  values: [prod]
              maxUpdate: 10%
      template:
        metadata:
          name: 'guestbook-{}'
          labels:
            envLabel: '{}'
        spec:
          project: default
          source:
            repoURL: https://github.com/your-org/your-repo.git
            targetRevision: HEAD
            path: guestbook/{}
          destination:
            server: https://kubernetes.default.svc
            namespace: guestbook-{}
    ```

    where:

    `metadata.name`
    Specifies the name of your ApplicationSet resource.

    `metadata.namespace`
    Specifies the namespace where the ApplicationSet is deployed.

    `spec.strategy.type`
    Specifies the creation strategy type. Set to `RollingSync` to enable staged application updates.

    `spec.strategy.rollingSync.steps`
    Defines the sequential rollout stages using label selectors.

    `matchExpressions.key`
    Specifies the label key used to group applications (for example, `envLabel` or `tier`).

    `matchExpressions.operator`
    Specifies the operator for label matching (for example, `In`).

    `matchExpressions.values`
    Specifies the label values for applications to update in this step (for example, `[dev]`).

    `maxUpdate`
    (Optional) Specifies the maximum percentage of applications to update simultaneously within a step (for example, `10%`). Set to `0` to process applications sequentially one at a time.

2.  Apply the YAML file:

    ``` terminal
    $ oc apply -f guestbook-rollingsync.yaml
    ```

</div>

<div>

<div class="title">

Verification

</div>

1.  Verify that the RollingSync strategy is configured:

    ``` terminal
    $ oc get applicationset guestbook-rollingsync -n openshift-gitops -o yaml
    ```

2.  Update the ApplicationSet and observe that applications are updated in stages:

    ``` terminal
    $ oc get applications -n openshift-gitops -l app.kubernetes.io/instance=guestbook-rollingsync -w
    ```

3.  If Progressive Sync is enabled, verify the Progressive Sync panel in the Argo CD Web UI:

    1.  Navigate to the **Argo CD Application details** page for your deployed application.

    2.  In the **Application Status** panel, a **PROGRESSIVE SYNC** section appears displaying the rollout status.

        The Progressive Sync panel displays the following information:

        | Field | Description |
        |----|----|
        | Progressive Sync Status | Health status: `Waiting`, `Pending`, `Progressing`, or `Healthy` |
        | Last Transition | Timestamp of the last state change |
        | Message | Additional details or error messages |

</div>

<div class="note">

<div class="title">

</div>

- When deploying an application by using the `ApplicationSet` controller, the Argo CD controller will only manage an application in its own namespace. If an application is created in another namespace, it will not be recognized.

- RollingSync updates application groups sequentially based on `matchExpressions`, and the `rollingSync.steps` field defines which groups to sync and in what order using label selectors.

- Applications not matched by any step’s label selectors will not be automatically updated and must be manually synced.

</div>

## Example: Progressive sync with environment labels

The following example illustrates how to configure a progressive sync over applications with environment labels:

``` yaml
apiVersion: argoproj.io/v1alpha1
kind: ApplicationSet
metadata:
  name: cluster-apps
  namespace: openshift-gitops
spec:
  strategy:
    type: RollingSync
    rollingSync:
      steps:
        - matchExpressions:
            - key: envLabel
              operator: In
              values:
                - env-dev
        - matchExpressions:
            - key: envLabel
              operator: In
              values:
                - env-prod
          maxUpdate: 10%
  generators:
    - list:
        elements:
          - cluster: dev-cluster
            url: https://dev-cluster.example.com
            envLabel: env-dev
          - cluster: prod-cluster
            url: https://prod-cluster.example.com
            envLabel: env-prod
  template:
    metadata:
      name: '{{cluster}}-app'
      labels:
        envLabel: '{{envLabel}}'
    spec:
      project: default
      source:
        repoURL: https://github.com/example/repo.git
        targetRevision: HEAD
        path: apps
      destination:
        server: '{{url}}'
        namespace: default
```

In this example:

- Step 1 updates applications with the `envLabel: env-dev` label.

- Step 2 updates applications with the `envLabel: env-prod` label, with a maximum of 10% of production applications updated simultaneously.

# Understanding deletion strategies

The `deletionOrder` field in the ApplicationSet strategy configuration controls the order in which applications are deleted when ApplicationSet is deleted. Red Hat OpenShift GitOps supports two deletion strategies: AllAtOnce and Reverse.

AllAtOnce deletion
All applications are deleted simultaneously when deleting ApplicationSet. This is the default deletion behavior and works with both AllAtOnce and RollingSync creation strategies.

Reverse deletion
Applications are deleted in reverse order of the steps defined in `rollingSync.steps`. This ensures that applications deployed in later steps are deleted before applications deployed in earlier steps.

The Reverse deletion strategy is particularly useful when you need to tear down dependent services in a specific sequence, such as deleting frontend services before backend dependencies. The following requirements apply for Reverse deletion:

- Must be used with `type: RollingSync` creation strategy.

- Requires `rollingSync.steps` to be defined in the strategy configuration.

For example, if you have two steps where Step 1 deploys development environment applications and Step 2 deploys production environment applications, using Reverse deletion order will:

1.  Delete production environment applications (Step 2) first

2.  Delete development environment applications (Step 1) second

> [!NOTE]
> The ApplicationSet finalizer ensures that the ApplicationSet resource is not removed until all managed applications are successfully deleted, regardless of the deletion strategy used.

## Configuring AllAtOnce deletion strategy

You can configure the AllAtOnce deletion strategy to remove all applications managed by the ApplicationSet simultaneously when they are deleted. This is the default deletion behavior, but you can explicitly configure it for clarity in your ApplicationSet specification.

The AllAtOnce deletion strategy works with both AllAtOnce and RollingSync creation strategies, making it a versatile option for most use cases where you do not need to delete applications in a specific order.

<div>

<div class="title">

Prerequisites

</div>

- You have created an ApplicationSet resource.

- You have access to edit the ApplicationSet configuration.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Edit the ApplicationSet custom resource:

    ``` terminal
    $ oc edit applicationset <applicationset_name> -n <namespace>
    ```

    where:

    `<applicationset_name>`
    Specifies the name of your ApplicationSet resource.

    `<namespace>`
    Specifies the namespace where the ApplicationSet is deployed.

2.  Add or update the `spec.strategy.deletionOrder` field with the AllAtOnce value:

    ``` yaml
    apiVersion: argoproj.io/v1alpha1
    kind: ApplicationSet
    metadata:
      name: <applicationset_name>
      namespace: <namespace>
    spec:
      strategy:
        type: AllAtOnce
        deletionOrder: AllAtOnce
    ```

    where:

    `metadata.name`
    Specifies the name of your ApplicationSet resource.

    `metadata.namespace`
    Specifies the namespace where the ApplicationSet is deployed.

    `spec.strategy.type`
    Specifies the creation strategy type. Can be set to `AllAtOnce` or `RollingSync`.

    `spec.strategy.deletionOrder`
    Specifies the deletion strategy. Set to `AllAtOnce` to remove all applications simultaneously.

3.  Save the changes to apply the configuration.

</div>

<div>

<div class="title">

Verification

</div>

1.  Verify that the deletion strategy is configured:

    ``` terminal
    $ oc get applicationset <applicationset_name> -n <namespace> -o jsonpath='{.spec.strategy.deletionOrder}'
    ```

    **Example output:**

    ``` terminal
    AllAtOnce
    ```

2.  When you delete applications from the ApplicationSet, observe that all matching applications are removed simultaneously:

    ``` terminal
    $ oc get applications -n <namespace> -l app.kubernetes.io/instance=<applicationset_name>
    ```

</div>

> [!NOTE]
> The ApplicationSet finalizer ensures that the ApplicationSet resource is not removed until all managed applications are successfully deleted, even when using the AllAtOnce deletion strategy.

## Example: AllAtOnce deletion strategy for multi-cluster deployments

The following example illustrates how to configure AllAtOnce deletion strategy for a multi-cluster deployment scenario where all applications across different clusters can be deleted simultaneously:

``` yaml
apiVersion: argoproj.io/v1alpha1
kind: ApplicationSet
metadata:
  name: multi-cluster-apps
  namespace: openshift-gitops
spec:
  strategy:
    type: AllAtOnce
    deletionOrder: AllAtOnce
  generators:
    - list:
        elements:
          - cluster: dev-cluster
            url: https://dev-cluster.example.com
            environment: development
          - cluster: staging-cluster
            url: https://staging-cluster.example.com
            environment: staging
          - cluster: prod-cluster
            url: https://prod-cluster.example.com
            environment: production
  template:
    metadata:
      name: 'myapp-{{cluster}}'
      labels:
        environment: '{{environment}}'
    spec:
      project: default
      source:
        repoURL: https://github.com/example/myapp.git
        targetRevision: HEAD
        path: manifests
      destination:
        server: '{{url}}'
        namespace: myapp
      syncPolicy:
        automated:
          prune: true
          selfHeal: true
```

In this example:

- The ApplicationSet manages applications across three clusters: development, staging, and production.

- The `deletionOrder: AllAtOnce` configuration ensures that when applications are removed from the ApplicationSet, all applications across all clusters are deleted simultaneously.

- This approach is useful when the applications are independent and do not have cross-cluster dependencies that require ordered deletion.

## Configuring ApplicationSet reverse deletion order

You can configure the reverse deletion strategy such that applications are deleted in reverse order of the steps defined in `rollingSync.steps` of ApplicationSet. This is particularly useful when managing dependent services that must be removed in a specific order.

<div>

<div class="title">

Prerequisites

</div>

- You have created an ApplicationSet resource.

- For Reverse deletion order, the ApplicationSet must use `type: RollingSync` with defined `rollingSync.steps`.

- You have access to edit the ApplicationSet configuration.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Edit the ApplicationSet custom resource:

    ``` terminal
    $ oc edit applicationset <applicationset_name> -n <namespace>
    ```

    where:

    `<applicationset_name>`
    Specifies the name of your ApplicationSet resource.

    `<namespace>`
    Specifies the namespace where the ApplicationSet is deployed.

2.  Add or update the `spec.strategy.deletionOrder` field:

    ``` yaml
    apiVersion: argoproj.io/v1alpha1
    kind: ApplicationSet
    metadata:
      name: <applicationset_name>
      namespace: <namespace>
    spec:
      strategy:
        type: RollingSync
        deletionOrder: Reverse
        rollingSync:
          steps:
            - matchExpressions:
                - key: <label_key>
                  operator: In
                  values:
                    - <label_value_step1>
            - matchExpressions:
                - key: <label_key>
                  operator: In
                  values:
                    - <label_value_step2>
    ```

    where:

    `metadata.name`
    Specifies the name of your ApplicationSet resource.

    `metadata.namespace`
    Specifies the namespace where the ApplicationSet is deployed.

    `spec.strategy.type`
    Specifies the creation strategy type. Set to `AllAtOnce` or `RollingSync`. For Reverse deletion order, you must use `RollingSync`.

    `spec.strategy.deletionOrder`
    Specifies the deletion order. Set to `Reverse` to delete applications in reverse order of the defined steps.

    `spec.strategy.rollingSync.steps.matchExpressions.key`
    Specifies the label key used to group applications. Required when using Reverse deletion order.

3.  Save the changes to apply the configuration.

</div>

<div>

<div class="title">

Verification

</div>

1.  Verify that the deletion order is configured:

    ``` terminal
    $ oc get applicationset <applicationset_name> -n <namespace> -o jsonpath='{.spec.strategy.deletionOrder}'
    ```

    **Example output:**

    ``` terminal
    Reverse
    ```

</div>

> [!NOTE]
> The ApplicationSet finalizer ensures that the ApplicationSet resource is not removed until all managed applications are successfully deleted.

## Example: Reverse deletion order with dependent services

The following example illustrates how to configure Reverse deletion order for a scenario where frontend services must be deleted before backend services:

``` yaml
apiVersion: argoproj.io/v1alpha1
kind: ApplicationSet
metadata:
  name: microservices-apps
  namespace: openshift-gitops
spec:
  strategy:
    type: RollingSync
    deletionOrder: Reverse
    rollingSync:
      steps:
        - matchExpressions:
            - key: tier
              operator: In
              values:
                - backend
        - matchExpressions:
            - key: tier
              operator: In
              values:
                - frontend
  generators:
    - list:
        elements:
          - service: database
            tier: backend
          - service: api
            tier: backend
          - service: web
            tier: frontend
  template:
    metadata:
      name: '{{service}}-app'
      labels:
        tier: '{{tier}}'
    spec:
      project: default
      source:
        repoURL: https://github.com/example/repo.git
        targetRevision: HEAD
        path: services/{{service}}
      destination:
        server: https://kubernetes.default.svc
        namespace: microservices
```

In this example:

- Step 1 defines backend services (database and API).

- Step 2 defines frontend services (web).

- When applications are deleted, the frontend services are deleted first, followed by the backend services.

- This ensures that frontend services do not attempt to connect to already-deleted backend services during the deletion process.

# Troubleshooting Progressive Sync

When working with Progressive Sync in Red Hat OpenShift GitOps, you might encounter issues related to the visibility of the Progressive Sync status panel or application states.

Common troubleshooting scenarios include:

- The Progressive Sync section does not appear in the **Application details** view

- Applications display an `Unknown` state in the Progressive Sync panel

To troubleshoot these issues, verify that Progressive Sync is properly enabled in your Argo CD custom resource and that your ApplicationSet is configured with a `RollingSync` strategy.

## Troubleshooting when Progressive Sync section does not appear

If the Progressive Sync section is missing from the Application details, verify the configuration and application resources.

<div>

<div class="title">

Procedure

</div>

- Confirm that the application is managed by an `ApplicationSet` controller with the `RollingSync` strategy.

- Verify that Progressive Sync is enabled in the Argo CD CR.

- Inspect the resources by running the following commands:

  ``` terminal
  $ oc get applicationsets -n openshift-gitops
  $ oc get applications -n openshift-gitops
  ```

</div>

## Troubleshooting when application shows Unknown state

If the status of an application is Unknown, verify the application configuration and check the ApplicationSet controller logs.

- Ensure that the required labels and annotations are applied.

- Verify that the application exists in the same namespace as the Argo CD instance.

- Review the `ApplicationSet` controller logs for error messages.

# Additional resources

- [Red Hat OpenShift GitOps](../installing_gitops/installing-openshift-gitops.md#installing-openshift-gitops)

- [The `ApplicationSet` resource](https://argo-cd.readthedocs.io/en/stable/operator-manual/applicationset/#the-applicationset-resource)

- [Argo CD custom resource and component properties](../argocd_instance/argo-cd-cr-component-properties.md#argo-cd-cr-component-properties)

- [Progressive Sync, Argo CD upstream documentation](https://argo-cd.readthedocs.io/en/stable/operator-manual/applicationset/Progressive-Syncs/)
