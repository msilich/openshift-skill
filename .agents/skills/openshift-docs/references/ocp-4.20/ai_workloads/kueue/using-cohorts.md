<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

You can use cohorts to group cluster queues and determine which cluster queues can share borrowable resources with each other.

Borrowable resources are defined as the unused nominal quota of all the cluster queues in a cohort.

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

All cluster queues that have a matching `spec.cohortName` are part of the same cohort.

If the `spec.cohortName` field is omitted, the cluster queue does not belong to any cohort and cannot access borrowable resources.
