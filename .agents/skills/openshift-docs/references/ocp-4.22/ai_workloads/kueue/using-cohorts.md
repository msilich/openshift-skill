<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

You can use cohorts to group cluster queues and determine which cluster queues can share borrowable resources with each other.

Cluster queues in the same cohort tree can borrow unused quota from other cluster queues or cohorts. Borrowing and lending limits apply throughout the tree.

By using cohorts, you can optimize resource utilization, prevent under-utilization, and enable fair sharing configurations. In addition, you can simplify resource management and allocation between teams, because you can group cluster queues for related workloads or for each team. You can also use cohorts to set resource quotas at a group level to define the limits for resources that a group of cluster queues can consume.

# Cohort configuration within a cluster queue spec

You can add a cluster queue to a cohort by specifying the cohort name in the `.spec.cohortName` field of the `ClusterQueue` object.

The following example shows a `ClusterQueue` object with a cohort configured:

``` yaml
apiVersion: kueue.x-k8s.io/v1beta2
kind: ClusterQueue
metadata:
  name: cluster-queue
spec:
# ...
  cohortName: example-cohort
# ...
```

All cluster queues that have a matching `spec.cohortName` field are part of the same cohort.

To add a cohort-level quota or place the cluster queue in a hierarchy, create a `Cohort` object with the same name.

If the `spec.cohortName` field is omitted, the cluster queue does not belong to any cohort and cannot access borrowable resources.

# Hierarchical cohorts

Use hierarchical cohorts to share unused quota between teams and control how much each group can borrow or lend. You can organize cluster queues into a hierarchy and add shared quota at different levels.

A cohort tree has cohorts and cluster queues. Each cohort is a cluster-scoped `Cohort` object that organizes quota but does not accept workloads. Cluster queues are the final level in a cohort tree and accept workloads.

A root cohort does not have a `spec.parentName` field. In a child cohort, the `spec.parentName` field identifies the parent cohort. To move a cohort, change its `spec.parentName` field. Moving a cohort also moves all cohorts and cluster queues below it to the new parent.

You can share unused quota only within the same cohort tree. To add shared quota, set the `spec.resourceGroups.flavors.resources.nominalQuota` field in a `Cohort` or `ClusterQueue` object.

For each resource in a child cohort, you can set two limits in the `spec.resourceGroups` field:

`borrowingLimit`
Restricts how much quota a child cohort and the cohorts and cluster queues below it can borrow through its parent.

`lendingLimit`
Restricts how much unused quota a child cohort and the cohorts and cluster queues below it can lend through its parent.

Set either limit to `0` to prevent that type of sharing. Omit a limit to leave that type of sharing unrestricted for the resource. Sharing is bounded by the quota available in the cohort tree and by any limits set at other levels.

The following example assigns two teams to separate cohorts under the `engineering` root cohort. Each team has a cluster queue and can use quota from the root cohort:

``` text
engineering
├── team-a
│   └── team-a-queue
└── team-b
    └── team-b-queue
```

The `reclaimWithinCohort` and `borrowWithinCohort` preemption policies on a cluster queue apply across the cohort tree.

With fair sharing enabled, you can set the `spec.fairSharing.weight` field on each `Cohort` object. These weights give cohorts with the same parent, and the cluster queues below them, different shares of common resources.

> [!WARNING]
> Do not create a cycle in a cohort hierarchy. When Red Hat build of Kueue detects a cycle, the affected cluster queues stop admitting new workloads. Remove the cycle to restore admission.
>
> Deleting a cohort immediately removes its quota and its parent connection. Workloads that Red Hat build of Kueue already admitted continue to run, but new workloads cannot borrow through the removed connection.

# Configuring hierarchical cohorts

You can configure hierarchical cohorts to share resource quota between teams.

In the following example, an engineering department shares 1 CPU and 256 MiB of memory quota between two teams that use separate cluster queues.

<div>

<div class="title">

Prerequisites

</div>

- You have cluster administrator permissions.

- You installed the Red Hat build of Kueue Operator on your cluster.

- You created a `Kueue` custom resource (CR).

- A `ResourceFlavor` object named `default-flavor` exists.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create a file named `cohorts.yaml` with the following content:

    ``` yaml
    apiVersion: kueue.x-k8s.io/v1beta2
    kind: Cohort
    metadata:
      name: engineering
    spec:
      resourceGroups:
      - coveredResources: ["cpu", "memory"]
        flavors:
        - name: default-flavor
          resources:
          - name: cpu
            nominalQuota: 1
          - name: memory
            nominalQuota: 256Mi
    ---
    apiVersion: kueue.x-k8s.io/v1beta2
    kind: Cohort
    metadata:
      name: team-a
    spec:
      parentName: engineering
    ---
    apiVersion: kueue.x-k8s.io/v1beta2
    kind: Cohort
    metadata:
      name: team-b
    spec:
      parentName: engineering
    ---
    apiVersion: kueue.x-k8s.io/v1beta2
    kind: ClusterQueue
    metadata:
      name: team-a-queue
    spec:
      namespaceSelector: {}
      cohortName: team-a
      resourceGroups:
      - coveredResources: ["cpu", "memory"]
        flavors:
        - name: default-flavor
          resources:
          - name: cpu
            nominalQuota: 0
          - name: memory
            nominalQuota: 0
    ---
    apiVersion: kueue.x-k8s.io/v1beta2
    kind: ClusterQueue
    metadata:
      name: team-b-queue
    spec:
      namespaceSelector: {}
      cohortName: team-b
      resourceGroups:
      - coveredResources: ["cpu", "memory"]
        flavors:
        - name: default-flavor
          resources:
          - name: cpu
            nominalQuota: 0
          - name: memory
            nominalQuota: 0
    ```

    where:

    `spec.resourceGroups.flavors.resources.nominalQuota`
    Specifies the resource quota that a cohort or cluster queue contributes to the hierarchy.

    `spec.parentName`
    Specifies the parent cohort in a cohort hierarchy.

    `spec.namespaceSelector`
    Specifies which namespaces can submit workloads to the cluster queue. An empty selector (`{}`) accepts workloads from all namespaces. If you omit this field, the cluster queue accepts no workloads and jobs stay pending.

    `spec.cohortName`
    Specifies the cohort to which a cluster queue belongs.

2.  Apply the configuration by running the following command:

    ``` terminal
    $ oc apply -f cohorts.yaml
    ```

</div>

<div>

<div class="title">

Verification

</div>

1.  Verify the cohort objects by running the following command:

    ``` terminal
    $ oc get cohorts
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    NAME               AGE
    engineering        10s
    team-a             10s
    team-b             10s
    ```

    </div>

2.  Verify that each cluster queue belongs to the correct cohort by running the following command:

    ``` terminal
    $ oc get clusterqueue team-a-queue team-b-queue -o custom-columns=NAME:.metadata.name,COHORT:.spec.cohortName
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    NAME             COHORT
    team-a-queue     team-a
    team-b-queue     team-b
    ```

    </div>

</div>

# Hierarchical cohort metrics

You can use cohort metrics to observe the hierarchy, shared quota, resource reservations, admitted workloads, and weighted share of each cohort subtree.

The following metrics describe hierarchical cohorts:

| Metric | Description |
|----|----|
| `kueue_cohort_info` | Reports the direct parent and root cohort for a cohort. |
| `kueue_cohort_subtree_admitted_active_workloads` | Reports the number of active, admitted workloads in a cohort subtree. |
| `kueue_cohort_subtree_admitted_workloads_total` | Reports the total number of workloads admitted in a cohort subtree. |
| `kueue_cohort_subtree_quota` | Reports nominal quota aggregated within a cohort subtree by resource and flavor. |
| `kueue_cohort_subtree_resource_reservations` | Reports resource reservations aggregated within a cohort subtree by resource and flavor. |
| `kueue_cohort_weighted_share` | Reports the highest ratio of resource usage that exceeds nominal quota to the resources that the cohort can lend, divided by the cohort weight. |
| `kueue_cluster_queue_info` | Reports the direct parent cohort and root cohort for a cluster queue. |

Red Hat build of Kueue enables cohort metrics by default. Only the `kueue_cohort_weighted_share` metric requires the `FairSharing` preemption policy. The cohort subtree metrics do not require fair sharing.

# Additional resources

- [Configuring quotas](configuring-quotas.md#configuring-quotas)

- [Configuring fair sharing](configuring-fairsharing.md#configuring-fairsharing)

- [Creating a Kueue custom resource](install-kueue.md#create-kueue-cr_install-kueue)

- [Cohorts (Kubernetes documentation)](https://kueue.sigs.k8s.io/docs/concepts/cohort/)
