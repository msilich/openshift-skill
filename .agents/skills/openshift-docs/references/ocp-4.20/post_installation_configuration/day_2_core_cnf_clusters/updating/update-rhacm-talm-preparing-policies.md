<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Before you can perform policy-based cluster updates, you must configure your hub cluster with the required Red Hat Advanced Cluster Management (RHACM) policies, placement rules, and Topology Aware Lifecycle Manager (TALM) `ClusterGroupUpgrade` custom resources (CRs).

# Preparing RHACM policies and placement rules for cluster updates

You can organize your Git repository, configure cluster labels, and create placement rules to target clusters for policy-based updates.

<div>

<div class="title">

Prerequisites

</div>

- RHACM hub cluster is deployed and managing target clusters. For more information, see [Red Hat Advanced Cluster Management for Kubernetes documentation](https://access.redhat.com/documentation/en-us/red_hat_advanced_cluster_management_for_kubernetes/).

- Topology Aware Lifecycle Manager (TALM) is installed on the RHACM hub cluster. For more information, see "Installing Topology Aware Lifecycle Manager by using the CLI".

- You have a Git repository for storing update policies with appropriate access controls.

- You have cluster-admin privileges on the RHACM hub cluster.

- The `oc` CLI tool is installed and configured.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Prepare your Git repository structure similar to the following example:

    ``` text
    upgrade-policies/
    ├── policies/
    │   ├── zstream/
    │   │   └── upgrade-4.20.1-policy.yaml
    │   ├── ystream/
    │   │   └── upgrade-4.20-policy.yaml
    │   └── eus/
    │       └── upgrade-4.20-eus-policy.yaml
    └── cgu/
        ├── core-zstream-upgrade.yaml
        ├── core-ystream-upgrade.yaml
        └── core-eus-upgrade.yaml
    ```

    > [!NOTE]
    > If you are using Kustomize for policy management with Argo CD or Flux, you can add a `kustomization.yaml` file to manage policy overlays. This file is optional if you apply policies directly with `oc apply`.

2.  Create a `Placement` rule so that update policies can be bound to clusters through labels.

    > [!NOTE]
    > If you use PolicyGenerator with Argo CD or a ZTP pipeline, `Placement` and `PlacementBinding` resources are generated automatically from your PolicyGenerator configuration. The following manual steps are provided for environments that do not use PolicyGenerator or for reference when troubleshooting placement issues.

    The following example uses the label `upgrade-version-to-4-21=""` to bind a policy to a cluster:

    ``` yaml
    apiVersion: cluster.open-cluster-management.io/v1beta1
    kind: Placement
    metadata:
      name: openshift-upgrade-placement
      namespace: openshift-upgrade-policies
      annotations:
        policy.open-cluster-management.io/description: |
          Placement rule for OpenShift upgrade policies. Targets clusters with
          the label "upgrade-version-to-4-21" for 4.20 to 4.21 upgrades.
    spec:
      predicates:
        - requiredClusterSelector:
            labelSelector:
              matchLabels:
                upgrade-version-to-4-21: ""
    ```

3.  Create a `PlacementBinding` resource to connect the policies to the placement rule:

    ``` yaml
    apiVersion: policy.open-cluster-management.io/v1
    kind: PlacementBinding
    metadata:
      name: openshift-upgrade-placement-binding
      namespace: openshift-upgrade-policies
      annotations:
        policy.open-cluster-management.io/description: |
          Binding that connects OpenShift upgrade policies to their placement rule.
          This binding ensures that both the main upgrade policy and pre-upgrade
          health check policy are applied to the same set of target clusters.
    placementRef:
      name: openshift-upgrade-placement
      kind: Placement
      apiGroup: cluster.open-cluster-management.io
    subjects:
      - name: openshift-upgrade-4.21-policy
        kind: Policy
        apiGroup: policy.open-cluster-management.io
      - name: pre-upgrade-health-check-policy
        kind: Policy
        apiGroup: policy.open-cluster-management.io
    ```

    A single policy, placement rule, and placement binding set can be bound to multiple clusters by adding the matching label to each cluster.

4.  Add an update label to your target clusters and verify by running the following commands:

    ``` terminal
    $ oc label managedcluster <cluster_name> upgrade-version-to-4-21=""
    $ oc get managedcluster <cluster_name> -o jsonpath='{.metadata.labels}'
    ```

    The following example shows the output:

    ``` terminal
    {
      "app.kubernetes.io/instance": "clusters",
      "cluster.open-cluster-management.io/clusterset": "default",
      "name": "test1",
      "ocp-version": "4.20",
      "openshiftVersion": "4.20.15",
      "upgrade-version-to-4-21": "",
      "upgrade-version-to-4-22": "",
      "unpause-worker-mcp": ""
    }
    ```

5.  Optional: Label clusters by site location for topology awareness by running the following command:

    ``` terminal
    $ oc label managedcluster <cluster_name> site=<site_name>
    ```

6.  Create and apply a `ManagedClusterSet` resource for update targets:

    ``` yaml
    apiVersion: cluster.open-cluster-management.io/v1beta2
    kind: ManagedClusterSet
    metadata:
      name: core-bm-clusters
    spec:
      clusterSelector:
        selectorType: LabelSelector
        labelSelector:
          matchLabels:
            cluster-type: bare-metal-core
    ```

    Apply the `ManagedClusterSet` resource by running the following command:

    ``` terminal
    $ oc apply -f managedclusterset.yaml
    ```

</div>

<div>

<div class="title">

Verification

</div>

- Verify that TALM is active, cluster labels are applied, and the `ManagedClusterSet` resource exists by running the following commands:

  ``` terminal
  $ oc get pods -n openshift-operators | grep cluster-group-upgrades
  $ oc get managedclusters --show-labels
  $ oc get managedclusterset core-bm-clusters
  ```

  The following example shows the output:

  ``` terminal
  cluster-group-upgrades-controller-manager-5d7b9c8f7d-abc12   2/2     Running   0          5m
  ```

</div>

# ClusterGroupUpgrade custom resource configuration

You can configure `ClusterGroupUpgrade` custom resources (CRs) to orchestrate cluster updates with Topology Aware Lifecycle Manager (TALM). A `ClusterGroupUpgrade` CR defines which clusters to update, which policies to apply, and how to manage batching and concurrency.

> [!IMPORTANT]
> RHACM policies used for updates must be set to `inform` mode. The `ClusterGroupUpgrade` CR temporarily changes these policies to `enforce` mode at the scheduled update time, applying them to the target clusters. When the `ClusterGroupUpgrade` CR completes or times out, the policies automatically revert to `inform` mode. This ensures that update policies are only enforced at the specific time you intend, rather than immediately when the policy is created.

## Basic ClusterGroupUpgrade CR

The following example shows a basic `ClusterGroupUpgrade` CR:

``` yaml
apiVersion: ran.openshift.io/v1alpha1
kind: ClusterGroupUpgrade
metadata:
  name: <cgu_name>
  namespace: <namespace>
spec:
  clusters:
  - <cluster_name_1>
  - <cluster_name_2>
  managedPolicies:
  - <policy_name>
  enable: false
  remediationStrategy:
    maxConcurrency: <max_concurrency>
    timeout: <timeout_minutes>
```

| Field | Description |
|----|----|
| `name` | Specifies a name for your `ClusterGroupUpgrade` CR, for example `core-zstream-upgrade-4.20.1`. |
| `namespace` | Specifies the namespace for the resource, for example `openshift-upgrade-policies`. |
| `clusters` | Specifies the names of your target clusters. |
| `managedPolicies` | Specifies the names of your update policies. |
| `enable` | Set to `false` to create the resource without starting the update. Set to `true` to start the update immediately. |
| `maxConcurrency` | Specifies the number of clusters to update simultaneously. Use `1` for canary testing, `2-5` for production rollouts, or higher for large fleets with proven procedures. |
| `timeout` | Specifies the maximum time in minutes to wait for each cluster update. See the timeout guidelines that follow. |

ClusterGroupUpgrade CR fields

## Timeout guidelines

Calculate appropriate timeout values based on your environment:

- Base timeout: 60 minutes for z-stream updates, 120 minutes for y-stream updates.

- Add 30 minutes for each additional worker node beyond 3.

- Add 60 minutes for disconnected environments.

- Add 30 minutes for clusters with large image registries.

## Optional configuration fields

You can add the following optional fields to the `spec` section to customize the update behavior:

- Canary cluster testing

- Pre-update blocking checks

- Post-update label management

## Canary cluster testing

To test the update on a canary cluster before rolling it out to the full fleet, add a `canaries` list under `remediationStrategy` and use `clusterSelector` instead of `clusters` to target clusters by label:

``` yaml
  clusterSelector:
  - <label_selector>
  remediationStrategy:
    canaries:
    - <canary_cluster_name>
    maxConcurrency: 1
```

where:

- `<label_selector>`: Specifies a label selector for the target clusters, for example `upgrade-wave=1`.

- `<canary_cluster_name>`: Specifies the name of the canary cluster to update first. TALM updates the canary cluster first, waits for success, and then proceeds with other clusters.

## Pre-update blocking checks

To require pre-update checks to pass before the update begins, add `blockingCRs` and `beforeEnable` fields:

``` yaml
  beforeEnable:
    addClusterLabels:
      pre-upgrade-check: pending
  blockingCRs:
  - name: <blocking_cr_name>
    namespace: <blocking_cr_namespace>
    kind: ConfigMap
    conditions:
    - type: <condition_type>
      status: "True"
```

where:

- `<blocking_cr_name>`: Specifies the name of the blocking custom resource, for example `etcd-backup`.

- `<condition_type>`: Specifies the condition that must be met before the update can proceed, for example `BackupComplete`.

## Post-update label management

To update cluster labels after the update completes, add an `afterCompletion` field:

``` yaml
  afterCompletion:
    addClusterLabels:
      upgraded-to: "<target_version>"
      upgrade-status: complete
    removeClusterLabels:
    - pre-upgrade-check
```

where `<target_version>` is the target version, for example `4.20`.

## Chained ClusterGroupUpgrade CRs for EUS-to-EUS updates

For Extended Update Support (EUS) to EUS updates, you can create chained `ClusterGroupUpgrade` CRs that use `blockingCRs` and `actions` to orchestrate a multi-step update:

``` yaml
---
apiVersion: ran.openshift.io/v1alpha1
kind: ClusterGroupUpgrade
metadata:
  name: upgrade-20to21
  namespace: openshift-upgrade-policies
spec:
  actions:
    afterCompletion:
      deleteClusterLabels:
        upgrade-version-to-4-21: ""
      deleteObjects: true
      addClusterLabels:
        unpause-workers-4-22: ""
  backup: false
  clusters:
  - <cluster_name>
  enable: true
  managedPolicies:
    - prep-20to22
    - upgrade-ocp-20to21
    - upgrade-olm-20to21
    - upgrade-validate-21
  preCaching: false
  preCachingConfigRef: {}
  remediationStrategy:
    maxConcurrency: 1
    timeout: 480
---
apiVersion: ran.openshift.io/v1alpha1
kind: ClusterGroupUpgrade
metadata:
  name: upgrade-21to22
  namespace: openshift-upgrade-policies
spec:
  actions:
    afterCompletion:
      deleteClusterLabels:
        upgrade-version-4-22: ""
        unpause-workers-4-22: ""
      deleteObjects: true
  backup: false
  clusters:
  - <cluster_name>
  enable: true
  managedPolicies:
    - upgrade-ocp-21to22
    - upgrade-olm-21to22
    - upgrade-validate-22
    - upgrade-worker-1
    - upgrade-worker-2
  preCaching: false
  preCachingConfigRef: {}
  remediationStrategy:
    maxConcurrency: 1
    timeout: 480
  blockingCRs:
  - name: upgrade-20to21
    namespace: openshift-upgrade-policies
```

where:

- `<cluster_name>`: Specifies the name of the target cluster.

- `actions`: Changes cluster labels as each step completes. This removes temporary update labels and unbinds completed update policies from the cluster.

- `blockingCRs`: Requires the first `ClusterGroupUpgrade` CR to complete before the second `ClusterGroupUpgrade` CR begins enforcing its policies.

- `upgrade-worker-1`, `upgrade-worker-2`: Separate unpause policies for each `MachineConfigPool` resource. Your cluster might have more machine config pools, requiring additional policies.

## Applying and monitoring a ClusterGroupUpgrade CR

After creating a `ClusterGroupUpgrade` CR, apply and enable it by running the following commands:

``` terminal
$ oc apply -f <cgu_cr_filename>.yaml
$ oc patch cgu <cgu_name> \
  -n <namespace> \
  --type merge \
  -p '{"spec":{"enable":true}}'
```

Monitor the `ClusterGroupUpgrade` status by running the following commands:

``` terminal
$ oc get cgu <cgu_name> -n <namespace> -o yaml
$ oc get cgu <cgu_name> -n <namespace> -w
```

Check the `status` section for update progress:

The following example shows the output:

\+

``` yaml
status:
  conditions:
  - message: Upgrade is progressing
    reason: InProgress
    status: "True"
    type: Progressing
  managedPoliciesForUpgrade:
  - name: core-upgrade-4.20.1-policy
    namespace: openshift-upgrade-policies
  remediationPlan:
  - - spoke1
    - spoke2
  status:
    spoke1: complete
    spoke2: inprogress
```

Verify the `ClusterGroupUpgrade` CR entered the expected state by running the following commands:

``` terminal
$ oc get cgu -n <namespace>
$ oc get cgu <cgu_name> -n <namespace> -o jsonpath='{.status.clusters}'
```

The following example shows the output:

\+

``` terminal
NAME                             AGE   STATE        DETAILS
core-zstream-upgrade-4.20.1     5m    InProgress   Remediating non-compliant policies
```

When the cluster is fully updated and the state of all `ClusterGroupUpgrade` CRs shows `Completed`, verify that all policies show `Compliant` by running the following command:

``` terminal
$ oc get policies -n <cluster_name>
```

The following example shows the output:

\+

``` terminal
NAME                        REMEDIATION ACTION   COMPLIANCE STATE   AGE
upgrade.upgrade-ocp-21to22  inform               Compliant          1h
upgrade.upgrade-olm-21to22  inform               Compliant          10m
```

Delete the completed `ClusterGroupUpgrade` CRs from the update namespace by running the following command:

``` terminal
$ oc delete cgu -n <namespace> <cgu_name>
```

## Troubleshooting

- If the `ClusterGroupUpgrade` CR is stuck in `Preparing` state, verify that all managed policies exist and are bound to target clusters.

- If the `ClusterGroupUpgrade` CR fails with a timeout error, increase the `timeout` value in the `remediationStrategy` section.

# Additional resources

- [Overview of cluster updates with RHACM and TALM](update-rhacm-talm-overview.md#core-cluster-upgrades-overview)

- [Installing Topology Aware Lifecycle Manager by using the CLI](../../../edge_computing/cnf-talm-for-cluster-upgrades.md#installing-topology-aware-lifecycle-manager-using-cli_cnf-topology-aware-lifecycle-manager)

- [RHACM](https://docs.redhat.com/en/documentation/red_hat_advanced_cluster_management_for_kubernetes)

- [`ClusterGroupUpgrade` samples on GitHub](https://github.com/openshift-kni/cluster-group-upgrades-operator/tree/main/samples)
