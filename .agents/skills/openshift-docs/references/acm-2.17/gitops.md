> Source: [Red Hat Advanced Cluster Management for Kubernetes 2.17](https://docs.redhat.com/en/documentation/red_hat_advanced_cluster_management_for_kubernetes/2.17/html/gitops/index). Copyright Red Hat.
> Adapted from AsciiDoc to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md), [CC BY-SA 3.0](LICENSE.md) and SOURCE.json for source revisions and gaps.

<a id="gitops-overview"></a>

# Red Hat OpenShift GitOps overview

Red Hat OpenShift GitOps and Argo CD are integrated with Red Hat Advanced Cluster Management for Kubernetes. You can use the Red Hat OpenShift GitOps Operator to manage applications across your managed clusters with Argo CD.

Red Hat Advanced Cluster Management for Kubernetes supports two methods to use OpenShift GitOps with managed clusters: the *Push model* and the *Pull model*. In the Push model, the Argo CD server on the hub cluster deploys resources directly to managed clusters. In the Pull model, each managed cluster runs its own Argo CD instance and synchronizes it from Git.

All supported models use the `GitOpsCluster` custom resource for configuration and the `ApplicationSet` resource with a `clusterDecisionResource` generator to deploy applications across managed clusters.

**Important:** Red Hat Advanced Cluster Management does not include entitlements for OpenShift GitOps. You need a separate Red Hat OpenShift Container Platform subscription for the following features:

- Red Hat OpenShift GitOps (excluding the Argo CD Agent) requires an Red Hat OpenShift Container Platform subscription.

- The Argo CD Agent requires a Red Hat OpenShift Platform Plus subscription. The Argo CD Agent can run on OpenShift Container Platform or in supported Kubernetes environments.

For more information, see the [Self-managed Red Hat OpenShift subscription guide](https://www.redhat.com/en/resources/self-managed-openshift-subscription-guide).

<div>

<div class="title">

Additional resources

</div>

- [Push and Pull model overview](gitops.md#gitops-models)

- [Configure Placement resources for OpenShift GitOps](gitops.md#gitops-placement)

- [Push model overview](gitops.md#gitops-push-overview)

- [Pull model overview](gitops.md#gitops-pull-overview)

- [Query Argo CD applications](gitops.md#gitops-console-query)

- [Manage policy definitions with Red Hat OpenShift GitOps](gitops.md#gitops-policies)

</div>

<a id="gitops-models"></a>

## Push and Pull model overview

You can use Red Hat OpenShift GitOps with Red Hat Advanced Cluster Management for Kubernetes by choosing either the *Push model* or the *Pull model*. Choose a model based on your network topology, security requirements, and how much status detail you need on your hub cluster. The Pull model includes the Argo CD Agent-based pull and `ManifestWork`-based pull variants.

**Important:** Red Hat Advanced Cluster Management does not include entitlements for OpenShift GitOps. You need a separate Red Hat OpenShift Container Platform subscription for the following features:

- Red Hat OpenShift GitOps (excluding the Argo CD Agent) requires an Red Hat OpenShift Container Platform subscription.

- The Argo CD Agent requires a Red Hat OpenShift Platform Plus subscription. The Argo CD Agent can run on OpenShift Container Platform or in supported Kubernetes environments.

For more information, see the [Self-managed Red Hat OpenShift subscription guide](https://www.redhat.com/en/resources/self-managed-openshift-subscription-guide).

| Model | Description | `ApplicationSet` template key | Use case | Required subscription |
|----|----|----|----|----|
| Push | The Argo CD server on the hub cluster deploys application resources directly on the managed clusters. Managed clusters do not run their own Argo CD instances. | `destination.server: '\{{server}\}'` | Simple setups and small fleets | OpenShift Container Platform |
| Pull (Argo CD Agent-based pull) | The add-on installs the OpenShift GitOps operator and an Argo CD instance on each managed cluster. A principal and agent architecture enables the hub Argo CD UI to show full, real-time Application status, resource trees, and logs. | `destination.name: '\{{name}\}'` | Independent cluster Red Hat OpenShift GitOps, network-restricted environments, enhanced security, and full Argo CD UI on the hub | Red Hat OpenShift Platform Plus (Argo CD Agent) |
| Pull (`ManifestWork`-based pull) | The add-on installs the OpenShift GitOps operator and an Argo CD instance on each managed cluster. The propagation controller distributes Application resources by using `ManifestWork`. The hub shows aggregated overall health and sync status only. | `destination.server: https://kubernetes.default.svc` with pull annotations | Independent cluster OpenShift GitOps, network-restricted environments, and enhanced security | OpenShift Container Platform |

Push and Pull models overview table

<div>

<div class="title">

Additional resources

</div>

- [Push model overview](gitops.md#gitops-push-overview)

- [Pull model overview](gitops.md#gitops-pull-overview)

</div>

<a id="gitops-placement"></a>

## Placement resources for Red Hat OpenShift GitOps configuration

There are separate `Placement` resources for `GitOpsCluster` infrastructure and for `ApplicationSet` application delivery.

Red Hat Advanced Cluster Management uses `Placement` resources to select managed clusters for OpenShift GitOps workflows. There are two `Placement` resources used with OpenShift GitOps:

Placement for `GitOpsCluster`  
Selects which managed clusters are registered with the Argo CD server on the hub (push model) or receive the Red Hat OpenShift GitOps add-on (pull models). Referenced in the `GitOpsCluster` resource `placementRef` field.

Placement for `ApplicationSet`  
Selects which managed clusters receive applications deployed by the `ApplicationSet` resource. Referenced in the `ApplicationSet` generator `labelSelector`.

These two `Placement` resources must be separate resources, even if they select the same clusters, because they serve different purposes. The `GitOpsCluster` `Placement` determines where infrastructure is set up. The `ApplicationSet` `Placement` determines where applications are deployed.

You might install the add-on on all clusters but only deploy a specific application to a subset. They are also consumed by different controllers.

In some unstable network scenarios, the managed clusters might be temporarily placed in `Unavailable` state. Add tolerations to your `Placement` resources to continue to include unavailable clusters. The following example shows a `Placement` resource with tolerations:

``` yaml
apiVersion: cluster.open-cluster-management.io/v1beta1
kind: Placement
metadata:
  name: gitops-placement
  namespace: openshift-gitops
spec:
  tolerations:
  - key: cluster.open-cluster-management.io/unreachable
    operator: Exists
  - key: cluster.open-cluster-management.io/unavailable
    operator: Exists
  predicates:
  - requiredClusterSelector:
      labelSelector:
        matchExpressions:
        - key: vendor
          operator: "In"
          values:
          - OpenShift
        - key: local-cluster
          operator: DoesNotExist
```

Each deployment model section in this document includes the specific `Placement` resources needed. See those sections for complete end-to-end examples.

<a id="gitops-console-query"></a>

## Query Argo CD applications

Use the Red Hat Advanced Cluster Management console Search feature to find and view Argo CD `Application` resources on the hub cluster.

**Required access:** Access to the Red Hat Advanced Cluster Management console

<div>

<div class="title">

Procedure

</div>

1.  Log in to your Red Hat Advanced Cluster Management hub cluster.

2.  From the console header, select the **Search** icon.

3.  Filter your query with the following values: `kind:application` and `apigroup:argoproj.io`.

4.  Select an application to view.

</div>

<a id="gitops-push-overview"></a>

# Push model overview

With the Push model, the Argo CD server on the hub cluster deploys application resources directly to managed clusters. The managed clusters do not run their own Argo CD instances.

If you want to use the `ManifestWork`-based or Argo CD Agent-based model with the Red Hat OpenShift GitOps add-on, see [Pull model overview](gitops.md#gitops-pull-overview). The Red Hat OpenShift GitOps add-on handles all cluster registration and Argo CD deployment automatically through the `GitOpsCluster` resource by setting `gitopsAddon.enabled: true`.

**Important:** Red Hat Advanced Cluster Management does not include entitlements for OpenShift GitOps. You might need a separate Red Hat OpenShift Container Platform subscription for certain features. For more information, see the [Self-managed Red Hat OpenShift subscription guide](https://www.redhat.com/en/resources/self-managed-openshift-subscription-guide).

<div>

<div class="title">

Additional resources

</div>

- [Register OpenShift Container Platform managed clusters to the Red Hat OpenShift GitOps operator](gitops.md#gitops-push-register)

- [Register non-OpenShift Container Platform clusters to the Red Hat OpenShift GitOps operator](gitops.md#gitops-push-register-non-ocp)

- [Deploy an application with the Push model](gitops.md#gitops-push-deploy)

- [Create a custom service account for Argo CD Push model](gitops.md#gitops-push-service-account)

</div>

<a id="gitops-push-register"></a>

## Register OpenShift Container Platform managed clusters to the Red Hat OpenShift GitOps operator

Register OpenShift Container Platform managed clusters with the Argo CD server on the hub cluster so that you can deploy applications to managed clusters.

When you integrate managed clusters with the OpenShift GitOps operator, a secret containing a token to access each managed cluster is automatically created in the GitOps instance server namespace. The OpenShift GitOps controller requires this secret to successfully sync resources to the managed cluster.

By default, the `application-manager` service account operates with cluster-admin permissions on the managed cluster to generate the OpenShift GitOps cluster secret. If you do not want to use the default service account, see [Create a custom service account for Argo CD Push model](gitops.md#gitops-push-service-account).

**Note:** Cluster registration by using the `Placement` resource is for the Push model only. The Pull model handles registration automatically by using the `GitOpsCluster` resource.

**Required access:** Cluster administrator

<div>

<div class="title">

Prerequisites

</div>

- Install the Red Hat OpenShift GitOps operator on your Red Hat Advanced Cluster Management hub cluster.

- Import one or more OpenShift Container Platform managed clusters.

- Create a `ManagedClusterSet` and bind it to the namespace where OpenShift GitOps is deployed. See [*ManagedClusterSet* overview](clusters.md#creating-a-managedclusterset) and [*ManagedClusterSetBinding* resource overview](clusters.md#creating-managedclustersetbinding).

- Enable the `ManagedServiceAccount` add-on to rotate the token that the Argo CD Push model uses to connect to the managed cluster.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create a `Placement` resource for the `GitOpsCluster` to select which managed clusters to register. Add the following YAML sample:

    ``` yaml
    apiVersion: cluster.open-cluster-management.io/v1beta1
    kind: Placement
    metadata:
      name: gitops-placement
      namespace: openshift-gitops
    spec:
      tolerations:
      - key: cluster.open-cluster-management.io/unreachable
        operator: Exists
      - key: cluster.open-cluster-management.io/unavailable
        operator: Exists
      predicates:
      - requiredClusterSelector:
          labelSelector:
            matchExpressions:
            - key: vendor
              operator: "In"
              values:
              - OpenShift
            - key: local-cluster
              operator: DoesNotExist
    ```

2.  Apply the YAML sample. Run the following command:

    ``` bash
    oc apply -f placement.yaml
    ```

3.  Create a `GitOpsCluster` custom resource to register the managed clusters. Add the following YAML sample:

    ``` yaml
    apiVersion: apps.open-cluster-management.io/v1beta1
    kind: GitOpsCluster
    metadata:
      name: gitops-cluster-push
      namespace: openshift-gitops
    spec:
      argoServer:
        argoNamespace: openshift-gitops
      placementRef:
        kind: Placement
        apiVersion: cluster.open-cluster-management.io/v1beta1
        name: gitops-placement
    ```

4.  Apply the YAML sample. Run the following command:

    ``` bash
    oc apply -f gitops-cluster-push.yaml
    ```

    **Note:** The `GitOpsCluster` controller automatically creates the following resources during reconciliation:

    - The `acm-placement` duck-type `ConfigMap` in the `argoServer.argoNamespace`

    - A `Role` and `RoleBinding`

    - An `ArgoCD` `Policy` named `<gitopscluster-name>-argocd-policy`

</div>

<div>

<div class="title">

Verification

</div>

1.  Make sure that the `acm-placement` ConfigMap resembles the following example:

    ``` yaml
    apiVersion: v1
    kind: ConfigMap
    metadata:
      name: acm-placement
      namespace: openshift-gitops
    data:
      apiVersion: cluster.open-cluster-management.io/v1beta1
      kind: placementdecisions
      statusListKey: decisions
      matchKey: clusterName
    ```

2.  Verify that each of the resources were created. Run the following commands:

    ``` bash
    oc get configmap acm-placement -n openshift-gitops -o yaml
    oc get role openshift-gitops-applicationset-controller-placement -n openshift-gitops
    oc get rolebinding openshift-gitops-applicationset-controller-placement -n openshift-gitops
    ```

</div>

<div>

<div class="title">

Additional resources

</div>

- [Register non-OpenShift Container Platform clusters to the Red Hat OpenShift GitOps operator](gitops.md#gitops-push-register-non-ocp)

</div>

<a id="gitops-push-register-non-ocp"></a>

## Register non-OpenShift Container Platform clusters to the Red Hat OpenShift GitOps operator

Register non-OpenShift Container Platform managed clusters with the Argo CD server on the hub cluster so that you can deploy applications to managed clusters.

When you integrate managed clusters with the OpenShift GitOps operator, a secret containing a token to access each managed cluster is automatically created in the GitOps instance server namespace. The OpenShift GitOps controller requires this secret to successfully sync resources to the managed cluster.

By default, the `application-manager` service account operates with cluster-admin permissions on the managed cluster to generate the OpenShift GitOps cluster secret. If you do not want to use the default service account, see [Create a custom service account for Argo CD Push model](gitops.md#gitops-push-service-account).

**Note:** Registering non-OpenShift Container Platform clusters to the Red Hat OpenShift GitOps operator is only available for the Push model.

**Required access:** Cluster administrator

<div>

<div class="title">

Prerequisites

</div>

- Install the Red Hat OpenShift GitOps operator on your Red Hat Advanced Cluster Management hub cluster.

- Import one or more non-OpenShift Container Platform managed clusters.

- Create a `ManagedClusterSet` and bind it to the namespace where OpenShift GitOps is deployed. See [*ManagedClusterSet* overview](clusters.md#creating-a-managedclusterset) and [*ManagedClusterSetBinding* resource overview](clusters.md#creating-managedclustersetbinding).

- Enable the `ManagedServiceAccount` add-on to rotate the token that the Argo CD Push model uses to connect to the managed cluster.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create a `Placement` resource for the `GitOpsCluster` to select which managed clusters to register. Add the following YAML sample:

    ``` yaml
    apiVersion: cluster.open-cluster-management.io/v1beta1
    kind: Placement
    metadata:
      name: gitops-placement
      namespace: openshift-gitops
    spec:
      tolerations:
      - key: cluster.open-cluster-management.io/unreachable
        operator: Exists
      - key: cluster.open-cluster-management.io/unavailable
        operator: Exists
      predicates:
      - requiredClusterSelector:
          labelSelector:
            matchExpressions:
            - key: vendor
              operator: "NotIn"
              values:
              - OpenShift
            - key: local-cluster
              operator: DoesNotExist
    ```

2.  Apply the YAML sample. Run the following command:

    ``` bash
    oc apply -f placement.yaml
    ```

3.  Create a `GitOpsCluster` custom resource to register the managed clusters. Addthe following YAML sample:

    ``` yaml
    apiVersion: apps.open-cluster-management.io/v1beta1
    kind: GitOpsCluster
    metadata:
      name: gitops-cluster-push
      namespace: openshift-gitops
    spec:
      argoServer:
        argoNamespace: openshift-gitops
      placementRef:
        kind: Placement
        apiVersion: cluster.open-cluster-management.io/v1beta1
        name: gitops-placement
    ```

4.  Apply the YAML sample. Run the following command:

    ``` bash
    oc apply -f gitops-cluster-push.yaml
    ```

    **Note:** The `GitOpsCluster` controller automatically creates the following resources during reconciliation:

    - The `acm-placement` duck-type `ConfigMap` in the `argoServer.argoNamespace`

    - A `Role` and `RoleBinding`

    - An `ArgoCD` `Policy` named `<gitopscluster-name>-argocd-policy`

5.  If the API server URL in the `ManagedCluster` resource `spec` is empty, update it manually. Run the following command. Replace `<cluster-name>` with the name of the managed cluster:

    ``` bash
    oc edit managedclusters <cluster-name>
    ```

6.  Verify that the `spec` includes the client configuration. See the following example:

    ``` yaml
    spec:
      managedClusterClientConfigs:
      - caBundle: <base64-encoded-ca>
        url: https://<api-server-url>
    ```

</div>

<div>

<div class="title">

Verification

</div>

1.  Make sure that the `acm-placement` ConfigMap resembles the following example:

</div>

``` yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: acm-placement
  namespace: openshift-gitops
data:
  apiVersion: cluster.open-cluster-management.io/v1beta1
  kind: placementdecisions
  statusListKey: decisions
  matchKey: clusterName
```

1.  Verify that each of the resources were created. Run the following commands:

    ``` bash
    oc get configmap acm-placement -n openshift-gitops -o yaml
    oc get role openshift-gitops-applicationset-controller-placement -n openshift-gitops
    oc get rolebinding openshift-gitops-applicationset-controller-placement -n openshift-gitops
    ```

<div>

<div class="title">

Additional resources

</div>

- [Register OpenShift Container Platform managed clusters to the Red Hat OpenShift GitOps operator](gitops.md#gitops-push-register)

</div>

<a id="gitops-push-deploy"></a>

## Deploy an application with the Push model

Deploy applications from the hub Argo CD server to managed clusters by using an `ApplicationSet` resource. In the Push model, the hub Argo CD pushes resources directly to managed clusters. The `ApplicationSet` uses `destination.server: '\{{server}\}'` to target each managed cluster API server.

**Required access:** Cluster administrator

<div>

<div class="title">

Prerequisites

</div>

- Complete the [Register OpenShift Container Platform managed clusters to the Red Hat OpenShift GitOps operator](gitops.md#gitops-push-register) procedure.

- If your `openshift-gitops-argocd-application-controller` service account is not assigned as a cluster administrator, add `ClusterRoleBinding` privileges.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create a `Placement` resource for the `ApplicationSet` to select which managed clusters receive the application. Add the following YAML sample:

    ``` yaml
    apiVersion: cluster.open-cluster-management.io/v1beta1
    kind: Placement
    metadata:
      name: app-placement
      namespace: openshift-gitops
    spec:
      tolerations:
      - key: cluster.open-cluster-management.io/unreachable
        operator: Exists
      - key: cluster.open-cluster-management.io/unavailable
        operator: Exists
      predicates:
      - requiredClusterSelector:
          labelSelector:
            matchExpressions:
            - key: vendor
              operator: "In"
              values:
              - OpenShift
            - key: local-cluster
              operator: DoesNotExist
    ```

    **Note:**

    - This `Placement` is different from the `GitOpsCluster` `Placement`. See *Configure Placement resources for Red Hat OpenShift GitOps* in the Additional resources section for more information.

2.  Apply the YAML sample. Run the following command:

    ``` bash
    oc apply -f app-placement.yaml
    ```

3.  Create the `ApplicationSet` resource. Use `destination.server: '\{{server}\}'` to push application resources directly from the hub cluster to each managed cluster. Use the following YAML sample:

    ``` yaml
    apiVersion: argoproj.io/v1alpha1
    kind: ApplicationSet
    metadata:
      name: guestbook-allclusters
      namespace: openshift-gitops
    spec:
      generators:
      - clusterDecisionResource:
          configMapRef: acm-placement
          labelSelector:
            matchLabels:
              cluster.open-cluster-management.io/placement: app-placement
          requeueAfterSeconds: 30
      template:
        metadata:
          name: '{{name}}-guestbook'
        spec:
          destination:
            namespace: guestbook
            server: '{{server}}'
          project: default
          source:
            repoURL: https://github.com/argoproj/argocd-example-apps.git
            targetRevision: HEAD
            path: guestbook
          syncPolicy:
            automated:
              prune: true
              selfHeal: true
            syncOptions:
            - CreateNamespace=true
    ```

    **Note:** The `destination.server: '\{{server}\}'` field makes the Push model different from the Pull models. The hub cluster Argo CD agent directly communicates with each managed cluster API server. The `configMapRef: acm-placement` references the duck-type `ConfigMap` that the `GitOpsCluster` controller creates automatically during reconciliation.

4.  Apply the YAML sample. Run the following command:

    ``` bash
    oc apply -f applicationset.yaml
    ```

5.  Verify that the application is deployed. Run the following command:

    ``` bash
    oc get applications.argoproj.io -n openshift-gitops
    ```

    **Important:** With a large number of managed clusters, the OpenShift GitOps controller memory and CPU usage increases significantly.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Configure Placement resources for Red Hat OpenShift GitOps](gitops.md#gitops-placement)

</div>

<a id="gitops-push-service-account"></a>

## Create a custom service account for Argo CD Push model

Create a custom service account when you need a limited set of permissions for the Argo CD Push model on managed clusters. By using a different service account, you can control the permissions granted instead of using the default `application-manager` service account.

**Note:** Creating a custom service account is only available for the Push model.

**Required access:** Cluster administrator

<div>

<div class="title">

Prerequisites

</div>

- You have managed clusters registered with the Red Hat OpenShift GitOps operator.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create a service account on a managed cluster by creating a `ManagedServiceAccount` resource on the hub cluster.

2.  Update the `GitOpsCluster` resource to use the managed service account that you created by adding the `managedServiceAccountRef` property. See the following example. Replace `<managed-sa-sample>` with the name of the service account you created:

    ``` yaml
    apiVersion: apps.open-cluster-management.io/v1beta1
    kind: GitOpsCluster
    metadata:
      name: argo-acm-importer
      namespace: openshift-gitops
    spec:
      managedServiceAccountRef: <managed-sa-sample>
      argoServer:
        argoNamespace: openshift-gitops
      placementRef:
        kind: Placement
        apiVersion: cluster.open-cluster-management.io/v1beta1
        name: gitops-placement
        namespace: openshift-gitops
    ```

3.  Verification

    - Verify that the new Argo CD cluster secret is created. Run the following command. Replace `<managed-cluster>` with the name of the managed cluster and `<managed-sa-sample>` with the name of the service account you created:

    ``` bash
    oc get secrets -n openshift-gitops <managed-cluster>-<managed-sa-sample>-cluster-secret
    ```

</div>

<a id="gitops-pull-overview"></a>

# Pull model overview

In the Pull model, the Red Hat OpenShift GitOps add-on installs the OpenShift GitOps operator and an Argo CD instance on each managed cluster. Each instance synchronizes applications from Git repositories independently. Red Hat Advanced Cluster Management for Kubernetes supports the following two Pull variants:

- Argo CD Agent-based pull: Full, real-time application status on the hub cluster through a principal and agent architecture. Requires a Red Hat OpenShift Platform Plus subscription.

- `ManifestWork`-based pull: Aggregated overall health and synchronization status on the hub cluster by using the `ManifestWork` resource. Requires an Red Hat OpenShift Container Platform subscription.

**Important notes:**

- Red Hat Advanced Cluster Management does not include entitlements for OpenShift GitOps. You might need a separate Red Hat OpenShift Container Platform subscription for certain features. For more information, see the [Self-managed Red Hat OpenShift subscription guide](https://www.redhat.com/en/resources/self-managed-openshift-subscription-guide).

- If you enable the OpenShift GitOps add-on by using the `GitOpsCluster` custom resource, the `GitOpsCluster` disables the Push model for all applications.

<div>

<div class="title">

Additional resources

</div>

- [Argo CD with the Argo CD Agent-based pull model overview](gitops.md#gitops-pull-agent)

- [*ManifestWork*-based pull model overview](gitops.md#gitops-pull-manifest)

- [Red Hat OpenShift GitOps add-on overview](gitops.md#gitops-addon-overview)

- [Enable the *ApplicationSet* resource in any namespace (Technology Preview)](gitops.md#gitops-pull-appset-enable)

- [Implement progressive rollout strategy (Technology Preview)](gitops.md#gitops-pull-rollout)

</div>

<a id="gitops-pull-agent"></a>

## Argo CD with the Argo CD Agent-based pull model overview

With the Argo CD Agent-based pull model, you can enable the Red Hat OpenShift GitOps add-on with the Argo CD Agent. Like the `ManifestWork`-based pull model, this mode installs the OpenShift GitOps operator and an independent Argo CD instance on each managed cluster.

Additionally, the principal and agent architecture enables the hub cluster Argo CD user interface to show real-time Application status, resource trees, and logs from all managed clusters.

The Argo CD Agent-based pull model provides the same Argo CD user interface experience as the Push model, while keeping the security and network benefits of the pull architecture.

**Important:** The Argo CD Agent requires a Red Hat OpenShift Platform Plus subscription. Red Hat Advanced Cluster Management does not include this entitlement. See [Self-Managed OpenShift Subscription Guide](https://www.redhat.com/en/resources/self-managed-openshift-subscription-guide) for more information.

The Argo CD Agent-based pull model uses a principal and agent architecture:

Principal  
Runs in the `openshift-gitops` namespace on the hub cluster. It receives connections from agents, dispatches applications, and aggregates status.

Agent  
Runs on each managed cluster. It connects to the principal, receives application specs in managed mode, or synchronizes local applications back to the hub cluster in autonomous mode.

Application controller  
Reconciles applications locally on each managed cluster, regardless of mode.

The principal uses destination-based mapping to route applications to the correct agent based on `destination.name`.

See the following table to learn about the differences between managed and autonomous modes:

| Aspect | Managed mode | Autonomous mode |
|----|----|----|
| Source of truth | Principal hub cluster | Managed cluster |
| Application creation | On the hub cluster. The principal dispatches applications to agents. | On the managed cluster by using a Policy or Git. |
| Application reconciliation | Local on managed cluster. | Local on managed cluster. The agent synchronizes specs and status to the hub cluster. |
| Hub cluster capability | Full control. Create, modify, and delete applications. | Read-only mirror. Inspect only applications. |

Table comparing managed and autonomous mode

<div>

<div class="title">

Additional resources

</div>

- [Configure the hub cluster for Argo CD Agent](gitops.md#gitops-pull-agent-hub)

- [Enable the Red Hat OpenShift GitOps add-on with Argo CD Agent in managed mode](gitops.md#gitops-pull-agent-managed)

- [Enable the Red Hat OpenShift GitOps add-on with Argo CD Agent in autonomous mode](gitops.md#gitops-pull-agent-autonomous)

- [Disable agent version drift heal](gitops.md#gitops-pull-agent-drift)

</div>

<a id="gitops-pull-agent-hub"></a>

## Configure the hub cluster for Argo CD Agent

Configure the OpenShift GitOps operator subscription and the hub `ArgoCD` custom resource before you create the `GitOpsCluster` resource for the Argo CD Agent.

**Required access:** Cluster administrator

<div>

<div class="title">

Prerequisites

</div>

- You have managed clusters registered with Red Hat Advanced Cluster Management.

- The Red Hat OpenShift GitOps operator is installed on the hub cluster.

- The `ManagedClusterSet` is bound to the target namespace.

</div>

<div>

<div class="title">

Procedure

</div>

1.  On the hub cluster, modify the Red Hat OpenShift GitOps operator subscription to include the required environment variables by running the following command:

    ``` bash
    oc edit subscription openshift-gitops-operator -n openshift-gitops-operator
    ```

2.  Replace the existing `ArgoCD` custom resource on the hub cluster with the compatible Agent mode configuration by adding the following YAML sample:

    ``` yaml
    apiVersion: argoproj.io/v1beta1
    kind: ArgoCD
    metadata:
      name: openshift-gitops
      namespace: openshift-gitops
    spec:
      controller:
        enabled: false
      sourceNamespaces:
        - "*"
      argoCDAgent:
        principal:
          enabled: true
          destinationBasedMapping: true
          auth: "mtls:CN=system:open-cluster-management:cluster:([^:]+):addon:gitops-addon:agent:gitops-addon-agent"
          namespace:
            allowedNamespaces:
              - "*"
    ```

3.  Set `destinationBasedMapping` to `true` for managed mode, and to `false` for autonomous mode.

4.  Apply the YAML sample by running the following command:

    ``` bash
    oc apply -f argocd-hub.yaml
    ```

    **Note:** This configuration disables the traditional `ArgoCD` controller and enables the agent principal with mutual TLS authentication. The `sourceNamespaces` field with `*` allows applications from any namespace. The `server.route.enabled` field creates an OpenShift Container Platform route for the agent principal, which is used for agent to hub communication.

5.  Configure the `default` `AppProject` in `openshift-gitops` with wildcard settings. The principal only propagates `AppProject` resources whose destinations and `sourceNamespaces` match the agent configuration. Without wildcards, propagation is skipped and agents cannot find the `AppProject` for their applications. Apply the following YAML sample:

    ``` yaml
    apiVersion: argoproj.io/v1alpha1
    kind: AppProject
    metadata:
      name: default
      namespace: openshift-gitops
    spec:
      sourceNamespaces:
      - '*'
      destinations:
      - name: '*'
        namespace: '*'
        server: '*'
      clusterResourceWhitelist:
      - group: '*'
        kind: '*'
      sourceRepos:
      - '*'
    ```

6.  Apply the YAML sample by running the following command:

    ``` bash
    oc apply -f appproject.yaml
    ```

</div>

<div>

<div class="title">

Verification

</div>

1.  Verify that a `ManagedClusterSetBinding` resource for the `ManagedClusterSet` exists in the `openshift-gitops` namespace. Without the resource, the `Placement` controller does not find any managed clusters. See the following YAML sample:

    ``` yaml
    apiVersion: cluster.open-cluster-management.io/v1beta2
    kind: ManagedClusterSetBinding
    metadata:
      name: default
      namespace: openshift-gitops
    spec:
      clusterSet: default
    ```

</div>

<a id="gitops-pull-agent-managed"></a>

## Enable the Red Hat OpenShift GitOps add-on with Argo CD Agent in managed mode

In managed mode, the hub cluster is the source of truth. Applications are created on the hub cluster and the principal dispatches applications to agents for local reconciliation on managed clusters. Use managed more for centralized operation models where a single team manages everything from one place.

**Required access:** Cluster administrator

<div>

<div class="title">

Procedure

</div>

1.  Create a `Placement` resource for the `GitOpsCluster` to select which managed clusters receive the add-on by adding the following YAML sample:

    ``` yaml
    apiVersion: cluster.open-cluster-management.io/v1beta1
    kind: Placement
    metadata:
      name: gitops-placement
      namespace: openshift-gitops
    spec:
      tolerations:
      - key: cluster.open-cluster-management.io/unreachable
        operator: Exists
      - key: cluster.open-cluster-management.io/unavailable
        operator: Exists
      predicates:
      - requiredClusterSelector:
          labelSelector:
            matchExpressions:
            - key: vendor
              operator: "In"
              values:
              - OpenShift
            - key: local-cluster
              operator: DoesNotExist
    ```

2.  Apply the YAML sample by running the following command:

    ``` bash
    oc apply -f gitops-placement.yaml
    ```

3.  Create a `GitOpsCluster` resource with the Argo CD Agent enabled by adding the following YAML sample:

    ``` yaml
    apiVersion: apps.open-cluster-management.io/v1beta1
    kind: GitOpsCluster
    metadata:
      name: agent-gitops
      namespace: openshift-gitops
    spec:
      argoServer:
        argoNamespace: openshift-gitops
      placementRef:
        kind: Placement
        apiVersion: cluster.open-cluster-management.io/v1beta1
        name: gitops-placement
      gitopsAddon:
        enabled: true
        argoCDAgent:
          enabled: true
    ```

    **Note:** The `mode` field determines the agent operation mode. The default value is `managed`. For OpenShift Container Platform managed clusters, you can enable OLM-based deployment by adding `olmSubscription.enabled: true` to the `gitopsAddon` specification in case the add-on auto-detection of the cluster type is not working properly. For more information, see [Red Hat OpenShift GitOps add-on overview](gitops.md#gitops-addon-overview).

4.  Apply the YAML sample by running the following command:

    ``` bash
    oc apply -f gitopscluster.yaml
    ```

5.  Verify that the `ConfigMap` was created by running the following command:

    ``` bash
    oc get configmap acm-placement -n openshift-gitops -o yaml
    ```

6.  Verify that the `Role` was created by running the following command:

    ``` bash
    oc get role openshift-gitops-applicationset-controller-placement -n openshift-gitops
    ```

7.  Verify that the `RoleBinding` was created by running the following command:

    ``` bash
    oc get rolebinding openshift-gitops-applicationset-controller-placement -n openshift-gitops
    ```

8.  Customize the auto-generated `ArgoCD` `Policy` to add RBAC for the managed clusters. The following example shows the complete `Policy` with RBAC added as a second policy-template:

    ``` yaml
    apiVersion: policy.open-cluster-management.io/v1
    kind: Policy
    metadata:
      name: agent-gitops-argocd-policy
      namespace: openshift-gitops
      annotations:
        policy.open-cluster-management.io/standards: NIST-CSF
        policy.open-cluster-management.io/categories: PR.PT Protective Technology
        policy.open-cluster-management.io/controls: PR.PT-3 Least Functionality
    spec:
      remediationAction: enforce
      disabled: false
      policy-templates:
        - objectDefinition:
            apiVersion: policy.open-cluster-management.io/v1
            kind: ConfigurationPolicy
            metadata:
              name: agent-gitops-argocd-config-policy
            spec:
              pruneObjectBehavior: None
              remediationAction: enforce
              severity: medium
              object-templates:
                - complianceType: musthave
                  objectDefinition:
                    apiVersion: argoproj.io/v1beta1
                    kind: ArgoCD
                    metadata:
                      name: acm-openshift-gitops
                      namespace: openshift-gitops
                      labels:
                        apps.open-cluster-management.io/gitopsaddon: "true"
                    spec:
                      server:
                        enabled: false
                      argoCDAgent:
                        agent:
                          enabled: true
                          allowedNamespaces:
                            - "*"
                          client:
                            principalServerAddress: "<auto-discovered>"
                            principalServerPort:
                            mode: "managed"
                          tls:
                            secretName: argocd-agent-client-tls
                            rootCASecretName: argocd-agent-ca
        - objectDefinition:
            apiVersion: policy.open-cluster-management.io/v1
            kind: ConfigurationPolicy
            metadata:
              name: agent-gitops-argocd-rbac-policy
            spec:
              pruneObjectBehavior: None
              remediationAction: enforce
              severity: medium
              object-templates:
                - complianceType: musthave
                  objectDefinition:
                    apiVersion: rbac.authorization.k8s.io/v1
                    kind: ClusterRoleBinding
                    metadata:
                      name: acm-openshift-gitops-cluster-admin
                    roleRef:
                      apiGroup: rbac.authorization.k8s.io
                      kind: ClusterRole
                      name: cluster-admin
                    subjects:
                      - kind: ServiceAccount
                        name: acm-openshift-gitops-argocd-application-controller
                        namespace: openshift-gitops
                - complianceType: musthave
                  objectDefinition:
                    apiVersion: rbac.authorization.k8s.io/v1
                    kind: ClusterRoleBinding
                    metadata:
                      name: acm-openshift-gitops-argocd-agent-cluster-reader
                    roleRef:
                      apiGroup: rbac.authorization.k8s.io
                      kind: ClusterRole
                      name: view
                    subjects:
                      - kind: ServiceAccount
                        name: acm-openshift-gitops-agent-agent
                        namespace: openshift-gitops
    ```

9.  Apply the YAML sample by running the following command:

    ``` bash
    oc apply -f policy.yaml
    ```

    **Notes:**

    - The `cluster-admin` `ClusterRole` in this example grants full cluster administrator privileges.

    - Do not add `Application` resources to the auto-generated `ArgoCD` `Policy`. The auto-generated `Policy` is for configuring the managed cluster.

10. Create a `Placement` resource for the `ApplicationSet` to select which managed clusters receive the application. Add the following YAML sample:

    ``` yaml
    apiVersion: cluster.open-cluster-management.io/v1beta1
    kind: Placement
    metadata:
      name: app-placement
      namespace: openshift-gitops
    spec:
      tolerations:
      - key: cluster.open-cluster-management.io/unreachable
        operator: Exists
      - key: cluster.open-cluster-management.io/unavailable
        operator: Exists
      predicates:
      - requiredClusterSelector:
          labelSelector:
            matchExpressions:
            - key: vendor
              operator: "In"
              values:
              - OpenShift
            - key: local-cluster
              operator: DoesNotExist
    ```

    **Note:** This `Placement` is distinct from the `GitOpsCluster` `Placement` that you created in step 1. See *Configure Placement resources for Red Hat OpenShift GitOps* in the additional resource section for more information.

11. Apply the YAML sample by running the following command:

    ``` bash
    oc apply -f app-placement.yaml
    ```

12. Deploy applications by using an `ApplicationSet` resource on the hub cluster. In the Argo CD Agent-based pull model, use `destination.name` so that the principal routes the application to the correct agent. See the following YAML sample:

    ``` yaml
    apiVersion: argoproj.io/v1alpha1
    kind: ApplicationSet
    metadata:
      name: guestbook-appset
      namespace: openshift-gitops
    spec:
      generators:
      - clusterDecisionResource:
          configMapRef: acm-placement
          labelSelector:
            matchLabels:
              cluster.open-cluster-management.io/placement: app-placement
          requeueAfterSeconds: 30
      template:
        metadata:
          name: '{{name}}-guestbook'
        spec:
          project: default
          source:
            repoURL: https://github.com/argoproj/argocd-example-apps
            targetRevision: HEAD
            path: guestbook
          destination:
            name: '{{name}}'
            namespace: guestbook
          syncPolicy:
            automated:
              prune: true
              selfHeal: true
            syncOptions:
            - CreateNamespace=true
    ```

    **Note:** The `destination.name: '\{{name}\}'` field distinguishes the Argo CD Agent-based pull model from the other models. The principal uses destination-based mapping to route applications to the correct agent. The `configMapRef: acm-placement` references the `ConfigMap` that the `GitOpsCluster` controller creates automatically during reconciliation.

13. Apply the YAML sample by running the following command:

    ``` bash
    oc apply -f applicationset.yaml
    ```

</div>

<div>

<div class="title">

Verification

</div>

1.  Verify that the agent principal is running on the hub cluster by running the following command:

    ``` bash
    oc get pods -n openshift-gitops -l app.kubernetes.io/name=openshift-gitops-agent-principal
    ```

2.  On the managed cluster, verify the agent is running by running the following command:

    ``` bash
    oc get pods -n openshift-gitops -l app.kubernetes.io/part-of=argocd-agent --context <managed-cluster-context>
    ```

3.  On the hub cluster, verify that the application status shows `Synced` by running the following command:

    ``` bash
    oc get applications.argoproj.io -n openshift-gitops
    ```

</div>

<div>

<div class="title">

Additional resources

</div>

- [Configure Placement resources for Red Hat OpenShift GitOps](gitops.md#gitops-placement)

</div>

<a id="gitops-pull-agent-autonomous"></a>

## Enable the Red Hat OpenShift GitOps add-on with Argo CD Agent in autonomous mode

In autonomous mode, the managed cluster is the source of truth. Applications are created on the managed cluster, and the agent synchronizes specs and the status back to the principal on the hub cluster as a read-only mirror. Use autonomous mode for workflows where all ongoing changes go through Git after the initial bootstrap.

**Required access:** Cluster administrator

<div>

<div class="title">

Procedure

</div>

1.  Create a `GitOpsCluster` resource with autonomous mode by adding the following YAML sample:

    ``` yaml
    apiVersion: apps.open-cluster-management.io/v1beta1
    kind: GitOpsCluster
    metadata:
      name: autonomous-gitops
      namespace: openshift-gitops
    spec:
      argoServer:
        argoNamespace: openshift-gitops
      placementRef:
        kind: Placement
        apiVersion: cluster.open-cluster-management.io/v1beta1
        name: gitops-placement
      gitopsAddon:
        enabled: true
        argoCDAgent:
          enabled: true
          mode: autonomous
    ```

2.  Apply the YAML sample by running the following command:

    ``` bash
    oc apply -f gitopscluster.yaml
    ```

3.  Customize the auto-generated `ArgoCD` `Policy` to add RBAC for the managed clusters. The following example shows the complete `Policy` with RBAC added as a second policy-template:

    ``` yaml
    apiVersion: policy.open-cluster-management.io/v1
    kind: Policy
    metadata:
      name: agent-gitops-argocd-policy
      namespace: openshift-gitops
      annotations:
        policy.open-cluster-management.io/standards: NIST-CSF
        policy.open-cluster-management.io/categories: PR.PT Protective Technology
        policy.open-cluster-management.io/controls: PR.PT-3 Least Functionality
    spec:
      remediationAction: enforce
      disabled: false
      policy-templates:
        - objectDefinition:
            apiVersion: policy.open-cluster-management.io/v1
            kind: ConfigurationPolicy
            metadata:
              name: agent-gitops-argocd-config-policy
            spec:
              pruneObjectBehavior: None
              remediationAction: enforce
              severity: medium
              object-templates:
                - complianceType: musthave
                  objectDefinition:
                    apiVersion: argoproj.io/v1beta1
                    kind: ArgoCD
                    metadata:
                      name: acm-openshift-gitops
                      namespace: openshift-gitops
                      labels:
                        apps.open-cluster-management.io/gitopsaddon: "true"
                    spec:
                      server:
                        enabled: false
                      argoCDAgent:
                        agent:
                          enabled: true
                          allowedNamespaces:
                            - "*"
                          client:
                            principalServerAddress: "<auto-discovered>"
                            principalServerPort:
                            mode: "managed"
                          tls:
                            secretName: argocd-agent-client-tls
                            rootCASecretName: argocd-agent-ca
        - objectDefinition:
            apiVersion: policy.open-cluster-management.io/v1
            kind: ConfigurationPolicy
            metadata:
              name: agent-gitops-argocd-rbac-policy
            spec:
              pruneObjectBehavior: None
              remediationAction: enforce
              severity: medium
              object-templates:
                - complianceType: musthave
                  objectDefinition:
                    apiVersion: rbac.authorization.k8s.io/v1
                    kind: ClusterRoleBinding
                    metadata:
                      name: acm-openshift-gitops-cluster-admin
                    roleRef:
                      apiGroup: rbac.authorization.k8s.io
                      kind: ClusterRole
                      name: cluster-admin
                    subjects:
                      - kind: ServiceAccount
                        name: acm-openshift-gitops-argocd-application-controller
                        namespace: openshift-gitops
                - complianceType: musthave
                  objectDefinition:
                    apiVersion: rbac.authorization.k8s.io/v1
                    kind: ClusterRoleBinding
                    metadata:
                      name: acm-openshift-gitops-argocd-agent-cluster-reader
                    roleRef:
                      apiGroup: rbac.authorization.k8s.io
                      kind: ClusterRole
                      name: view
                    subjects:
                      - kind: ServiceAccount
                        name: acm-openshift-gitops-agent-agent
                        namespace: openshift-gitops
    ```

4.  Apply the YAML sample by running the following command:

    ``` bash
    oc apply -f policy.yaml
    ```

    **Notes:**

    - The `cluster-admin` `ClusterRole` in this example grants full cluster administrator privileges.

    - Do not add `Application` resources to the auto-generated `ArgoCD` `Policy`. The auto-generated `Policy` is for configuring the managed cluster.

5.  Export the `Policy` and add a `ClusterRoleBinding`. Run the following command:

    ``` bash
    oc get application -n openshift-gitops -l app=policies -o yaml > policies-app.yaml
    ```

6.  Apply the `Policy` by running the following command:

    ``` bash
    oc apply -f policies-app.yaml
    ```

7.  Deploy applications to the managed cluster by using one of the following methods:

    - Create a separate OCM Policy to deploy an App of Apps bootstrap `Application` to managed clusters. After the bootstrap `Application` is deployed, all ongoing changes flow through Git. See the following YAML sample for the bootstrap policy:

      ``` yaml
      apiVersion: policy.open-cluster-management.io/v1
      kind: Policy
      metadata:
        name: autonomous-app-bootstrap
        namespace: openshift-gitops
      spec:
        remediationAction: enforce
        disabled: false
        policy-templates:
          - objectDefinition:
              apiVersion: policy.open-cluster-management.io/v1
              kind: ConfigurationPolicy
              metadata:
                name: autonomous-app-bootstrap-config
              spec:
                pruneObjectBehavior: None
                remediationAction: enforce
                severity: medium
                object-templates:
                  - complianceType: musthave
                    objectDefinition:
                      apiVersion: argoproj.io/v1alpha1
                      kind: Application
                      metadata:
                        name: app-of-apps-root
                        namespace: openshift-gitops
                      spec:
                        project: default
                        source:
                          repoURL: https://github.com/YOUR-ORG/YOUR-GITOPS-REPO
                          targetRevision: HEAD
                          path: apps
                        destination:
                          server: https://kubernetes.default.svc
                          namespace: openshift-gitops
                        syncPolicy:
                          automated:
                            prune: true
                            selfHeal: true
      ```

    - Use Git to manage applications after initial bootstrap. With autonomous mode, the managed cluster Argo CD instance watches Git repositories and synchronizes changes automatically. The agent synchronizes application specs and the status back to the principal on the hub cluster for visibility.

</div>

<div>

<div class="title">

Verification

</div>

1.  On the hub cluster, verify that autonomous applications are visible as read-only mirrors by running the following command:

    ``` bash
    oc get applications.argoproj.io -n openshift-gitops
    ```

</div>

<a id="gitops-pull-agent-drift"></a>

## Disable agent version drift heal

Configure how the add-on responds when the Argo CD Agent version on a managed cluster drifts from the expected version. Configuring drift heal helps you maintain environment stability and reduce operational overhead

**Required access:** Cluster administrator

<div>

<div class="title">

Procedure

</div>

- Disable drift heal by setting the `apps.open-cluster-management.io/skip-agent-version-heal: "true"` annotation on the `GitOpsCluster`.

</div>

<a id="gitops-pull-manifest"></a>

## *ManifestWork*-based pull model overview

The `ManifestWork`-based pull model uses the Red Hat OpenShift GitOps add-on to install the OpenShift GitOps operator and an Argo CD instance on each managed cluster. Each instance synchronizes from Git repositories independently.

The propagation controller on the hub cluster distributes `Application` resources to managed clusters by using the `ManifestWork` resource. The hub cluster shows an overview of the health and synchronization status for each application.

After you enable the `ManifestWork`-based pull model, the controller creates an `ArgoCD` `Policy` named `<gitopscluster-name>-argocd-policy` that deploys and configures the `ArgoCD` custom resource on managed clusters through the Red Hat Advanced Cluster Management for Kubernetes governance framework.

The policy is user-owned after creation. You can modify the policy for RBAC or `ArgoCD` settings. The controller does not overwrite your customizations.

**Important notes:**

- The `ManifestWork`-based pull model is only supported on OpenShift Container Platform managed clusters. For managed clusters that are not OpenShift Container Platform, use the Argo CD Agent-based pull model.

- If you need full Argo CD user interface compatibility with real-time resource trees, logs, and detailed status from managed clusters, use the Argo CD Agent-based pull model instead.

- Red Hat Advanced Cluster Management does not include entitlements for OpenShift GitOps. You might need a separate Red Hat OpenShift Container Platform subscription for certain features. For more information, see the [Self-managed Red Hat OpenShift subscription guide](https://www.redhat.com/en/resources/self-managed-openshift-subscription-guide).

<div>

<div class="title">

Additional resources

</div>

- [Enable the Red Hat OpenShift GitOps add-on for the `ManifestWork`-based pull model](gitops.md#gitops-pull-manifest-enable)

- [Customize the Argo CD policy for the *ManifestWork*-based pull model](gitops.md#gitops-pull-manifest-customize)

- [Deploy an application with the `ManifestWork`-based pull model](gitops.md#gitops-pull-manifest-deploy)

</div>

<a id="gitops-pull-manifest-enable"></a>

## Enable the Red Hat OpenShift GitOps add-on for the `ManifestWork`-based pull model

Create the `Placement` and `GitOpsCluster` resources so that the Red Hat OpenShift GitOps add-on deploys Argo CD on the selected managed clusters.

**Required access:** Cluster administrator

<div>

<div class="title">

Prerequisites

</div>

- You have managed clusters registered with Red Hat Advanced Cluster Management.

- The Red Hat OpenShift GitOps operator is installed on your hub cluster.

- The `ManagedClusterSet` is bound to the target namespace.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create a `ManagedClusterSetBinding` resource to bind the `ManagedClusterSet` to the `openshift-gitops` namespace. Add the following YAML sample:

    ``` yaml
    apiVersion: cluster.open-cluster-management.io/v1beta2
    kind: ManagedClusterSetBinding
    metadata:
      name: default
      namespace: openshift-gitops
    spec:
      clusterSet: default
    ```

2.  Apply the YAML sample. Run the following command:

    ``` bash
    oc apply -f managedclustersetbinding.yaml
    ```

3.  Create a `Placement` resource for the `GitOpsCluster` to select which managed clusters receive the add-on. Add the following YAML sample:

    ``` yaml
    apiVersion: cluster.open-cluster-management.io/v1beta1
    kind: Placement
    metadata:
      name: gitops-placement
      namespace: openshift-gitops
    spec:
      tolerations:
      - key: cluster.open-cluster-management.io/unreachable
        operator: Exists
      - key: cluster.open-cluster-management.io/unavailable
        operator: Exists
      predicates:
      - requiredClusterSelector:
          labelSelector:
            matchExpressions:
            - key: vendor
              operator: "In"
              values:
              - OpenShift
            - key: local-cluster
              operator: DoesNotExist
    ```

4.  Apply the YAML sample. Run the following command:

    ``` bash
    oc apply -f gitops-placement.yaml
    ```

5.  Create a `GitOpsCluster` resource to enable the Red Hat OpenShift GitOps add-on. Add the following YAML sample:

    ``` yaml
    apiVersion: apps.open-cluster-management.io/v1beta1
    kind: GitOpsCluster
    metadata:
      name: gitops-clusters
      namespace: openshift-gitops
    spec:
      argoServer:
        argoNamespace: openshift-gitops
      placementRef:
        kind: Placement
        apiVersion: cluster.open-cluster-management.io/v1beta1
        name: gitops-placement
      gitopsAddon:
        enabled: true
    ```

6.  Apply the YAML sample. Run the following command:

    ``` bash
    oc apply -f gitopscluster.yaml
    ```

    **Note:** The `GitOpsCluster` controller automatically creates the following resources during reconciliation:

    - The `acm-placement` duck-type `ConfigMap` in the `argoServer.argoNamespace`

    - A `Role` and `RoleBinding`

    - An `ArgoCD` `Policy` named `<gitopscluster-name>-argocd-policy`

</div>

<div>

<div class="title">

Verification

</div>

1.  Make sure that the `acm-placement` ConfigMap resembled the following example:

    ``` yaml
    apiVersion: v1
    kind: ConfigMap
    metadata:
      name: acm-placement
      namespace: openshift-gitops
    data:
      apiVersion: cluster.open-cluster-management.io/v1beta1
      kind: placementdecisions
      statusListKey: decisions
      matchKey: clusterName
    ```

2.  Verify that each of the resources were created. Run the following commands:

    ``` bash
    oc get configmap acm-placement -n openshift-gitops -o yaml
    oc get role openshift-gitops-applicationset-controller-placement -n openshift-gitops
    oc get rolebinding openshift-gitops-applicationset-controller-placement -n openshift-gitops
    oc get policy <gitopscluster-name>-argocd-policy -n openshift-gitops
    ```

3.  Verify that the `ArgoCD` `Policy` was created on the hub cluster by running the following command:

    ``` bash
    oc get policy gitops-clusters-argocd-policy -n openshift-gitops
    ```

</div>

<a id="gitops-pull-manifest-customize"></a>

## Customize the Argo CD policy for the *ManifestWork*-based pull model

You can customize the automatically generated Argo CD `Policy` to add the RBAC that managed clusters need for the `ManifestWork`-based pull model. This `Policy` is for configuring managed clusters only, such as RBAC and Argo CD settings.

**Required access:** Cluster administrator

<div>

<div class="title">

Procedure

</div>

1.  Use the following `Policy` YAML sample as a template to customize your Argo CD policy:

    ``` yaml
    apiVersion: policy.open-cluster-management.io/v1
    kind: Policy
    metadata:
      name: gitops-clusters-argocd-policy
      namespace: openshift-gitops
      annotations:
        policy.open-cluster-management.io/standards: NIST-CSF
        policy.open-cluster-management.io/categories: PR.PT Protective Technology
        policy.open-cluster-management.io/controls: PR.PT-3 Least Functionality
    spec:
      remediationAction: enforce
      disabled: false
      policy-templates:
        - objectDefinition:
            apiVersion: policy.open-cluster-management.io/v1
            kind: ConfigurationPolicy
            metadata:
              name: gitops-clusters-argocd-config-policy
            spec:
              pruneObjectBehavior: None
              remediationAction: enforce
              severity: medium
              object-templates:
                - complianceType: musthave
                  objectDefinition:
                    apiVersion: argoproj.io/v1beta1
                    kind: ArgoCD
                    metadata:
                      name: acm-openshift-gitops
                      namespace: openshift-gitops
                      labels:
                        apps.open-cluster-management.io/gitopsaddon: "true"
                    spec:
                      server:
                        enabled: false
        - objectDefinition:
            apiVersion: policy.open-cluster-management.io/v1
            kind: ConfigurationPolicy
            metadata:
              name: gitops-clusters-argocd-rbac-policy
            spec:
              pruneObjectBehavior: None
              remediationAction: enforce
              severity: medium
              object-templates:
                - complianceType: musthave
                  objectDefinition:
                    apiVersion: rbac.authorization.k8s.io/v1
                    kind: ClusterRoleBinding
                    metadata:
                      name: acm-openshift-gitops-cluster-admin
                    roleRef:
                      apiGroup: rbac.authorization.k8s.io
                      kind: ClusterRole
                      name: cluster-admin
                    subjects:
                      - kind: ServiceAccount
                        name: acm-openshift-gitops-argocd-application-controller
                        namespace: openshift-gitops
    ```

2.  Apply the YAML sample. Run the following command:

    ``` bash
    oc apply -f policy.yaml
    ```

    **Notes:**

    - The `cluster-admin` `ClusterRole` in the example grants full cluster administrator privileges. For production environments, configure the Argo CD application controller with appropriate least-privilege permissions for managing resources outside the controller namespace.

    - By default, the Red Hat OpenShift GitOps add-on might not provide sufficient privileges for the OpenShift GitOps controllers on managed clusters when managing resources outside the `openshift-gitops` namespace. If the privileges are not sufficient, export the automatically generated `Policy`, add a `ClusterRoleBinding`, and apply the changes.

</div>

<a id="gitops-pull-manifest-deploy"></a>

## Deploy an application with the `ManifestWork`-based pull model

In the `ManifestWork`-based pull model, applications are deployed by using an `ApplicationSet` resource on the hub cluster with specific pull-model annotations and labels. The propagation controller detects these annotations and creates `ManifestWork` resources to distribute the `Application` to managed clusters, where the local Argo CD instance reconciles it.

**Required access:** Cluster administrator

<div>

<div class="title">

Procedure

</div>

1.  Create a `Placement` resource for the `ApplicationSet` to select which managed clusters receive the application. Add the following YAML sample:

    ``` yaml
    apiVersion: cluster.open-cluster-management.io/v1beta1
    kind: Placement
    metadata:
      name: app-placement
      namespace: openshift-gitops
    spec:
      tolerations:
      - key: cluster.open-cluster-management.io/unreachable
        operator: Exists
      - key: cluster.open-cluster-management.io/unavailable
        operator: Exists
      predicates:
      - requiredClusterSelector:
          labelSelector:
            matchExpressions:
            - key: vendor
              operator: "In"
              values:
              - OpenShift
            - key: local-cluster
              operator: DoesNotExist
    ```

    **Note:** This `Placement` is different from the `GitOpsCluster` `Placement` that you created previously.

2.  Apply the YAML sample by running the following command:

    ``` bash
    oc apply -f app-placement.yaml
    ```

3.  Create the `ApplicationSet` resource with the pull-model annotations and labels. Use the following YAML sample:

    ``` yaml
    apiVersion: argoproj.io/v1alpha1
    kind: ApplicationSet
    metadata:
      name: guestbook-appset
      namespace: openshift-gitops
    spec:
      generators:
      - clusterDecisionResource:
          configMapRef: acm-placement
          labelSelector:
            matchLabels:
              cluster.open-cluster-management.io/placement: app-placement
          requeueAfterSeconds: 30
      template:
        metadata:
          name: '{{name}}-guestbook'
          labels:
            apps.open-cluster-management.io/pull-to-ocm-managed-cluster: "true"
          annotations:
            argocd.argoproj.io/skip-reconcile: "true"
            apps.open-cluster-management.io/ocm-managed-cluster: '{{name}}'
            apps.open-cluster-management.io/ocm-managed-cluster-app-namespace: openshift-gitops
        spec:
          project: default
          source:
            repoURL: https://github.com/argoproj/argocd-example-apps
            targetRevision: HEAD
            path: guestbook
          destination:
            server: https://kubernetes.default.svc
            namespace: guestbook
          syncPolicy:
            automated:
              prune: true
              selfHeal: true
            syncOptions:
            - CreateNamespace=true
    ```

    The following annotations and labels are required for the `ManifestWork`-based pull model:

    - `apps.open-cluster-management.io/pull-to-ocm-managed-cluster: "true"`: Enables the propagation controller to distribute the `Application` by using the `ManifestWork` resource.

    - `apps.open-cluster-management.io/ocm-managed-cluster: '\{{name}\}'`: Specifies which managed cluster receives the `Application`.

    - `argocd.argoproj.io/skip-reconcile: "true"`: Prevents the hub cluster Argo CD instance from reconciling the `Application`.

    - `apps.open-cluster-management.io/ocm-managed-cluster-app-namespace`: Specifies the namespace on the managed cluster where the `Application` object is created.

    - `destination.server: https://kubernetes.default.svc`: The managed cluster Argo CD instance reconciles the `Application` locally.

      **Note:** The `destination.server: https://kubernetes.default.svc` and the pull-model annotations are what distinguish the `ManifestWork`-based pull model from the other models.

4.  Apply the YAML sample. Run the following command:

    ``` bash
    oc apply -f applicationset.yaml
    ```

5.  Verify the deployment. Run the following command on your hub cluster:

    ``` bash
    oc get applications.argoproj.io -n openshift-gitops
    ```

</div>

<div>

<div class="title">

Additional resources

</div>

- [Configure Placement resources for Red Hat OpenShift GitOps](gitops.md#gitops-placement) for details.

- [Red Hat OpenShift GitOps add-on overview](gitops.md#gitops-addon-overview)

</div>

<a id="gitops-addon-overview"></a>

## Red Hat OpenShift GitOps add-on overview

The Red Hat OpenShift GitOps add-on automates the deployment and lifecycle management of Red Hat OpenShift GitOps on managed clusters, including installation options, skip annotations, verification, and uninstall.

The OpenShift GitOps add-on supports the following configuration options in the `gitopsAddon` specification:

`enabled`  
Enable or disable the Red Hat OpenShift GitOps add-on. The default is `false`.

`gitOpsOperatorImage`  
The only custom container image for the OpenShift GitOps operator that you need to specify.

`overrideExistingConfigs`  
Override existing `AddOnDeploymentConfig` values with new values from the `GitOpsCluster` specification. If you use the default value of `false`, existing config values are preserved and only new values are added. If you set the value to `true`, config values from the `GitOpsCluster` specification override existing values.

`olmSubscription`  
The Operator Lifecycle Manager subscription configuration. If you set `olmSubscription.enabled` to `true`, the add-on agent uses the Operator Lifecycle Manager subscription mode for the operator installation, regardless of whether the agent automatically detects an OpenShift Container Platform cluster or not.

`argoCDAgent`  
Argo CD Agent configuration (`enabled`, `serverAddress`, `serverPort`, `mode`). The default mode is `managed`.

<div>

<div class="title">

Additional resources

</div>

- [Skip the OpenShift GitOps add-on enforcement](gitops.md#gitops-pull-skip-addon)

- [Skip the Argo CD policy recreation](gitops.md#gitops-pull-skip-policy)

- [Uninstall the OpenShift GitOps add-on](gitops.md#gitops-pull-uninstall)

- [Check the OpenShift GitOps add-on functions](gitops.md#gitops-pull-check)

- [Check the Argo CD Agent function](gitops.md#gitops-pull-check-agent)

</div>

<a id="gitops-pull-skip-addon"></a>

## Skip the OpenShift GitOps add-on enforcement

You can skip enforcement for specific resources by adding the `gitops-addon.open-cluster-management.io/skip` annotation to resources on the managed cluster. When a resource has the annotation, the add-on does not update or manage the resource.

**Required access:** Cluster administrator

<div>

<div class="title">

Procedure

</div>

- Add the `gitops-addon.open-cluster-management.io/skip` annotation to the resource that you want to skip enforcement for. See the following YAML sample:

  ``` yaml
  apiVersion: argoproj.io/v1beta1
  kind: ArgoCD
  metadata:
    name: openshift-gitops
    namespace: openshift-gitops
    annotations:
      gitops-addon.open-cluster-management.io/skip: "true"
  ```

</div>

<a id="gitops-pull-skip-policy"></a>

## Skip the Argo CD policy recreation

Prevent the controller from recreating a deleted `ArgoCD` `Policy` by setting an annotation on the `GitOpsCluster` resource.

**Required access:** Cluster administrator

<div>

<div class="title">

Procedure

</div>

- Set the `apps.open-cluster-management.io/skip-argocd-policy: "true"` annotation on the `GitOpsCluster` resource that you want to skip recreation for. See the following YAML sample:

  ``` yaml
  apiVersion: gitops.open-cluster-management.io/v1alpha1
  kind: GitOpsCluster
  metadata:
    name: my-gitops-cluster
    namespace: openshift-gitops
    annotations:
      apps.open-cluster-management.io/skip-argocd-policy: "true"
  ```

</div>

<a id="gitops-pull-uninstall"></a>

## Uninstall the OpenShift GitOps add-on

Uninstall the Red Hat OpenShift GitOps add-on in the correct order so that dependencies and finalizers are cleaned up successfully.

**Important:** The uninstall takes several minutes. Do not force-remove finalizers before the cleanup completes. You must complete the uninstall in the correct order due to resource dependencies.

**Required access:** Cluster administrator

<div>

<div class="title">

Procedure

</div>

1.  Delete any `ApplicationSet` resources and wait for the generated `Application` resources to be removed. Run the following command. Replace `<applicationset-name>` with the name of your `ApplicationSet`:

    ``` bash
    oc delete applicationset <applicationset-name> -n openshift-gitops --ignore-not-found
    ```

2.  Verify that all generated `Application` resources are removed. Run the following command:

    ``` bash
    oc get applications.argoproj.io -n openshift-gitops
    ```

3.  Delete the `GitOpsCluster` resource by running the following command. Replace `<name>` with the name of your `GitOpsCluster`:

    ``` bash
    oc delete gitopscluster <name> -n openshift-gitops --ignore-not-found
    ```

4.  Delete the auto-generated `Policy`. Run the following command. Replace `<name>` with the name of your `Policy`:

    ``` bash
    oc delete policy <name>-argocd-policy -n openshift-gitops --ignore-not-found
    ```

5.  Delete the `Placement` resources by running the following commands. Replace `<gitops-placement-name>` and `<app-placement-name>` with the names of your `Placement` resources:

    ``` bash
    oc delete placement <gitops-placement-name> -n openshift-gitops --ignore-not-found
    oc delete placement <app-placement-name> -n openshift-gitops --ignore-not-found
    ```

6.  Delete the `PlacementBinding` resources. Run the following command. Replace `<name>` with the name of your `PlacementBinding`:

    ``` bash
    oc delete placementbinding <name>-argocd-policy-binding -n openshift-gitops --ignore-not-found
    ```

    **Important:** If the `Policy` is not deleted, it continues to enforce the `ArgoCD` custom resource on managed clusters even after the add-on is removed. If the controller recreates the `Policy` before the `GitOpsCluster` is fully removed, delete the `Policy` and `PlacementBinding` again by repeating this step.

7.  Delete all `ManagedClusterAddOn` resources to remove OpenShift GitOps from all managed clusters. Run the following command:

    ``` bash
    oc delete mca -A --field-selector metadata.name=gitops-addon
    ```

8.  Alternatively, delete the `ManagedClusterAddOn` resource from a single managed cluster to remove OpenShift GitOps from a specific cluster. Run the following command. Replace `<managed-cluster>` with the name of the managed cluster that you want to remove OpenShift GitOps from:

    ``` bash
    oc delete mca -n <managed-cluster> gitops-addon
    ```

9.  Wait for the `ArgoCD` custom resource to be removed from each managed cluster. Monitor the removal. Run the following command. Replace `<managed-cluster-context>` with the context of the managed cluster:

    ``` bash
    oc get argocd acm-openshift-gitops -n openshift-gitops --context <managed-cluster-context>
    ```

10. For OpenShift Container Platform managed clusters with Operator Lifecycle Manager-based deployment, verify that the Operator Lifecycle Manager `Subscription` created by the add-on is also removed. Run the following command. Replace `<managed-cluster-context>` with the context of the managed cluster:

    ``` bash
    oc get subscription.operators.coreos.com -l apps.open-cluster-management.io/gitopsaddon=true -A --context <managed-cluster-context>
    ```

11. If you enabled agent mode, delete the hub cluster agent resources. Run the following commands. Replace `<managed-cluster-name>` with the name of the managed cluster:

    ``` bash
    oc delete appproject --all -n <managed-cluster-name> --ignore-not-found
    oc delete secret cluster-<managed-cluster-name> -n openshift-gitops --ignore-not-found
    oc delete secret <managed-cluster-name>-application-manager-cluster-secret -n openshift-gitops --ignore-not-found
    ```

12. Delete the `ManagedClusterSetBinding`. Run the following command:

    ``` bash
    oc delete managedclustersetbinding default -n openshift-gitops --ignore-not-found
    ```

</div>

<a id="gitops-pull-check"></a>

## Check the OpenShift GitOps add-on functions

Check that the `GitOpsCluster` resource and the OpenShift GitOps add-on controller are healthy.

**Required access:** Cluster administrator

<div>

<div class="title">

Procedure

</div>

1.  View the `GitOpsCluster` resource status. Run the following command. Replace `<gitopscluster-name>` with the name of your `GitOpsCluster`:

    ``` bash
    oc get gitopscluster <gitopscluster-name> -n openshift-gitops -o yaml
    ```

2.  Check the status conditions for specific failure information. Run the following command. Replace `<gitopscluster-name>` with the name of your `GitOpsCluster`:

    ``` bash
    oc get gitopscluster <gitopscluster-name> -n openshift-gitops -o jsonpath='{.status.conditions}' | python3 -m json.tool
    ```

    See the following common condition types:

    - `Ready`: Overall `GitOpsCluster` health.

    - `PlacementResolved`: `Placement` resource status.

    - `ClustersRegistered`: Cluster registration status.

    - `ArgoCDPolicyReady`: `ArgoCD` `Policy` creation status.

    - `ArgoCDAgentPrereqsReady`: Agent prerequisites, if you have enabled the agent.

    - `CertificatesReady`: TLS certificate status, if you have enabled the agent.

    - `ManifestWorksApplied`: `ManifestWork` propagation status, if you have enabled the agent.

3.  Check the Red Hat OpenShift GitOps add-on controller logs. Run the following command. Replace `<managed-cluster-context>` with the context of the managed cluster:

    ``` bash
    oc logs -n open-cluster-management-agent-addon -l app=gitops-addon --context <managed-cluster-context>
    ```

</div>

<a id="gitops-pull-check-agent"></a>

## Check the Argo CD Agent function

Check that the Argo CD Agent principal on the hub cluster and the agent on the managed cluster are running.

**Required access:** Cluster administrator

<div>

<div class="title">

Procedure

</div>

1.  On the hub cluster, verify the agent principal is running. Run the following command:

    ``` bash
    oc get pods -n openshift-gitops -l app.kubernetes.io/name=openshift-gitops-agent-principal
    ```

2.  On the managed cluster, verify the agent is running. Run the following command. Replace `<managed-cluster-context>` with the context of the managed cluster:

    ``` bash
    oc get pods -n openshift-gitops -l app.kubernetes.io/part-of=argocd-agent --context <managed-cluster-context>
    ```

</div>

<a id="gitops-pull-appset-enable"></a>

## Enable the *ApplicationSet* resource in any namespace (Technology Preview)

Enable the Argo CD `ApplicationSet` resource so that you can create it in namespaces other than the Argo CD installation namespace to support multi-tenancy, improve security isolation, and increase team autonomy.

**Required access:** Cluster administrator

<div>

<div class="title">

Procedure

</div>

1.  Enable the Argo CD `ApplicationSet` resource in any namespace on the hub cluster. Run the following commands:

    ``` bash
    git clone https://github.com/stolostron/multicloud-integrations
    cd multicloud-integrations/deploy/appset-any-namespace
    ./setup-appset-any-namespace.sh --namespace openshift-gitops --argocd-name openshift-gitops
    ```

2.  Verify that the OpenShift GitOps instance restarted and is running on your hub cluster. Run the following command:

    ``` bash
    oc get pods -n openshift-gitops
    ```

3.  Enable the `Application` resource in any namespace on the managed clusters. The following example shows the complete modified `Policy`. Replace `<gitopscluster-name>` with the name of your OpenShift GitOps cluster:

    ``` yaml
    apiVersion: policy.open-cluster-management.io/v1
    kind: Policy
    metadata:
      name: <gitopscluster-name>-argocd-policy
      namespace: openshift-gitops
      annotations:
        policy.open-cluster-management.io/standards: NIST-CSF
        policy.open-cluster-management.io/categories: PR.PT Protective Technology
        policy.open-cluster-management.io/controls: PR.PT-3 Least Functionality
    spec:
      disabled: false
      remediationAction: enforce
      policy-templates:
      - objectDefinition:
          apiVersion: policy.open-cluster-management.io/v1
          kind: ConfigurationPolicy
          metadata:
            name: <gitopscluster-name>-argocd-config-policy
          spec:
            pruneObjectBehavior: None
            remediationAction: enforce
            severity: medium
            object-templates:
            - complianceType: musthave
              objectDefinition:
                apiVersion: argoproj.io/v1beta1
                kind: ArgoCD
                metadata:
                  labels:
                    apps.open-cluster-management.io/gitopsaddon: "true"
                  name: acm-openshift-gitops
                  namespace: openshift-gitops
                spec:
                  controller:
                    enabled: true
                    env:
                    - name: ARGOCD_APPLICATION_NAMESPACES
                      value: '*'
                  server:
                    enabled: false
      - objectDefinition:
          apiVersion: policy.open-cluster-management.io/v1
          kind: ConfigurationPolicy
          metadata:
            name: <gitopscluster-name>-argocd-appset-rbac-policy
          spec:
            pruneObjectBehavior: None
            remediationAction: enforce
            severity: medium
            object-templates:
            - complianceType: musthave
              objectDefinition:
                apiVersion: argoproj.io/v1alpha1
                kind: AppProject
                metadata:
                  name: default
                  namespace: openshift-gitops
                spec:
                  clusterResourceWhitelist:
                  - group: '*'
                    kind: '*'
                  destinations:
                  - namespace: '*'
                    server: '*'
                  sourceRepos:
                  - '*'
                  sourceNamespaces:
                  - '*'
            - complianceType: musthave
              objectDefinition:
                apiVersion: rbac.authorization.k8s.io/v1
                kind: ClusterRoleBinding
                metadata:
                  name: argo-admin
                subjects:
                  - kind: ServiceAccount
                    name: acm-openshift-gitops-argocd-application-controller
                    namespace: openshift-gitops
                roleRef:
                  apiGroup: rbac.authorization.k8s.io
                  kind: ClusterRole
                  name: cluster-admin
    ```

4.  Apply the YAML file by running the following command:

    ``` bash
    oc apply -f policy.yaml
    ```

</div>

<a id="gitops-pull-appset-deploy"></a>

## Deploy the *ApplicationSet* resource for standard configurations

Deploy an `ApplicationSet` resource for standard Pull-model configurations after you enable `ApplicationSet` in any namespace to manage resources more flexibly and make resources behave more like Subscription applications.

**Required access:** Cluster administrator

<div>

<div class="title">

Procedure

</div>

- Create the `ApplicationSet` resource in a custom namespace with the default `AppProject`. See the following YAML example:

  ``` yaml
  apiVersion: argoproj.io/v1alpha1
  kind: ApplicationSet
  metadata:
    name: helloworld
    namespace: appset-2
  spec:
    generators:
    - clusterDecisionResource:
        configMapRef: acm-placement
        labelSelector:
          matchLabels:
            cluster.open-cluster-management.io/placement: app-placement
        requeueAfterSeconds: 30
    template:
      metadata:
        annotations:
          apps.open-cluster-management.io/ocm-managed-cluster: '{{name}}'
          argocd.argoproj.io/skip-reconcile: "true"
        labels:
          apps.open-cluster-management.io/pull-to-ocm-managed-cluster: "true"
        name: '{{name}}-helloworld'
      spec:
        destination:
          namespace: helloworld
          server: https://kubernetes.default.svc
        project: default
        source:
          path: helloworld
          repoURL: https://github.com/stolostron/application-samples.git
          targetRevision: HEAD
        syncPolicy:
          automated: {}
  ```

</div>

<a id="gitops-pull-rollout"></a>

## Implement progressive rollout strategy (Technology Preview)

Use a progressive rollout strategy with an `ApplicationSet` resource to control how applications are updated across managed clusters. Make changes safely and more reliably across your entire cluster fleet by catching configuration errors early, and rolling out changes in smaller, more manageable steps.

The `ApplicationSet` controller organizes the clusters into groups and processes one group at a time through the Argo CD health cycle.

**Required access:** Cluster administrator

<div>

<div class="title">

Procedure

</div>

1.  Enable progressive synchronization. Run the following command:

    ``` bash
    oc -n openshift-gitops patch argocd openshift-gitops --type='merge' -p '{"spec":{"applicationSet":{"extraCommandArgs":["--enable-progressive-syncs"]}}}'
    ```

2.  Restart the controller. Run the following command:

    ``` bash
    oc -n openshift-gitops rollout restart deployment openshift-gitops-applicationset-controller
    ```

3.  Customize the `ApplicationSet` resource for your progressive rollout strategy. Use the following YAML template:

</div>

``` yaml
apiVersion: argoproj.io/v1alpha1
kind: ApplicationSet
metadata:
  name: guestbook-allclusters-app-set
  namespace: openshift-gitops
spec:
  generators:
  - clusterDecisionResource:
      configMapRef: acm-placement
      labelSelector:
        matchLabels:
          cluster.open-cluster-management.io/placement: app-placement
      requeueAfterSeconds: 30
  strategy:
    type: RollingSync
    rollingSync:
      steps:
      - name: dev-stage
        matchExpressions:
        - key: envLabel
          operator: In
          values: [env-dev]
        maxUpdate: 100%
      - name: qa-stage
        matchExpressions:
        - key: envLabel
          operator: In
          values: [env-qa]
        maxUpdate: 100%
      - name: prod-stage
        matchExpressions:
        - key: envLabel
          operator: In
          values: [env-prod]
        maxUpdate: 100%
  template:
    preserveFields:
    - metadata.labels.envLabel
    metadata:
      annotations:
        apps.open-cluster-management.io/ocm-managed-cluster: '{{name}}'
        apps.open-cluster-management.io/ocm-managed-cluster-app-namespace: openshift-gitops
        argocd.argoproj.io/skip-reconcile: "true"
      labels:
        apps.open-cluster-management.io/pull-to-ocm-managed-cluster: "true"
      name: '{{name}}-guestbook-app'
    spec:
      destination:
        namespace: guestbook
        server: https://kubernetes.default.svc
      project: default
      sources:
      - repoURL: https://github.com/argoproj/argocd-example-apps.git
        targetRevision: main
        path: guestbook
      syncPolicy:
        syncOptions:
        - CreateNamespace=true
```

\+ \* Use the `preserveFields` parameter to list the labels that you want the `ApplicationSet` to ignore. Without this field, the controller overwrites or deletes labels not defined in the template.

1.  Apply the `ApplicationSet` resource. Run the following command:

    ``` bash
    oc apply -f guestbook-allclusters-app-set.yaml
    ```

<div>

<div class="title">

Verification

</div>

1.  Make sure the application has a unique label that specifies the promotion order. Run the following commands:

    ``` bash
    oc -n openshift-gitops label applications.argoproj.io/cluster1-guestbook-app envLabel=env-dev
    oc -n openshift-gitops label applications.argoproj.io/cluster2-guestbook-app envLabel=env-qa
    oc -n openshift-gitops label applications.argoproj.io/cluster3-guestbook-app envLabel=env-prod
    ```

    **Note:** When Argo CD detects committed changes, the `ApplicationSet` controller detects `OutOfSync` applications and schedules a staged rollout. The controller processes `env-dev` first, then `env-qa`, then `env-prod`. Each group must reach the `Healthy` status before the next begins.

</div>

<a id="gitops-policies"></a>

# Manage policy definitions with OpenShift GitOps

With the `ArgoCD` resource, you can use Red Hat OpenShift GitOps to manage policy definitions by giving OpenShift GitOps access to create policies on the hub cluster.

**Required access:** Cluster administrator

<div>

<div class="title">

Prerequisites

</div>

- You are logged in to your hub cluster.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create a `ClusterRole` with access to create, read, update, and delete policies and placements. Use the following sample content:

    ``` yaml
    kind: ClusterRole
    apiVersion: rbac.authorization.k8s.io/v1
    metadata:
      name: openshift-gitops-policy-admin
    rules:
      - verbs: [get, list, watch, create, update, patch, delete]
        apiGroups: [policy.open-cluster-management.io]
        resources: [policies, configurationpolicies, certificatepolicies, operatorpolicies, policysets, placementbindings]
      - verbs: [get, list, watch, create, update, patch, delete]
        apiGroups: [cluster.open-cluster-management.io]
        resources: [placements, placements/status, placementdecisions, placementdecisions/status]
    ```

2.  Create a `ClusterRoleBinding` with the following sample content:

    ``` yaml
    kind: ClusterRoleBinding
    apiVersion: rbac.authorization.k8s.io/v1
    metadata:
      name: openshift-gitops-policy-admin
    subjects:
      - kind: ServiceAccount
        name: openshift-gitops-argocd-application-controller
        namespace: openshift-gitops
    roleRef:
      apiGroup: rbac.authorization.k8s.io
      kind: ClusterRole
      name: openshift-gitops-policy-admin
    ```

    **Notes:**

    - The `argocd.argoproj.io/compare-options: IgnoreExtraneous` annotation applies to replicated policies automatically.

    - To hide replicated policies from Argo CD, set `spec.copyPolicyMetadata` to `false` on the policy definition.

3.  Configure the Init Container to copy the Policy Generator binary. Your `ArgoCD` resource might resemble the following example. Replace `<version>` with 2.17:

    ``` yaml
    apiVersion: argoproj.io/v1beta1
    kind: ArgoCD
    metadata:
      name: openshift-gitops
      namespace: openshift-gitops
    spec:
      kustomizeBuildOptions: --enable-alpha-plugins
      repo:
        env:
        - name: KUSTOMIZE_PLUGIN_HOME
          value: /etc/kustomize/plugin
        initContainers:
        - args: ["-c", "cp /policy-generator/PolicyGenerator-not-fips-compliant /policy-generator-tmp/PolicyGenerator"]
          command: ["/bin/bash"]
          image: registry.redhat.io/rhacm2/multicluster-operators-subscription-rhel9:v<version>
          name: policy-generator-install
          volumeMounts:
          - mountPath: /policy-generator-tmp
            name: policy-generator
        volumeMounts:
        - mountPath: /etc/kustomize/plugin/policy.open-cluster-management.io/v1/policygenerator
          name: policy-generator
        volumes:
        - emptyDir: {}
          name: policy-generator
    ```

4.  Configure policy health checks in OpenShift GitOps. Download and apply the health checks by running the following command:

    ``` bash
    wget https://raw.githubusercontent.com/open-cluster-management-io/policy-collection/main/stable/CM-Configuration-Management/argocd-policy-healthchecks.yaml
    ```

5.  Apply the policy in the console by navigating to **Governance** \> **Create policy**.

</div>
