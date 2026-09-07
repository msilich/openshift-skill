<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Monitor Red Hat OpenShift GitOps Operator performance to identify resource bottlenecks, track reconciliation times, and optimize cluster performance. The Operator exposes performance metrics that the OpenShift monitoring stack collects and displays in the OpenShift Container Platform web console. You can track the following metrics:

| Metric name | Type | Description |
|----|----|----|
| `active_argocd_instances_total` | Gauge | The total number of active Argo CD instances currently managed by the Operator across the cluster. |
| `active_argocd_instances_by_phase` | Gauge | The number of active Argo CD instances in a given phase, such as Pending or Available. |
| `active_argocd_instance_reconciliation_count` | Counter | The total number of reconciliations that have occurred for an Argo CD instance in a given namespace. |
| `controller_runtime_reconcile_time_seconds_per_instance_bucket` | Counter | The number of reconciliation cycles completed under given time durations for an instance. For example, `controller_runtime_reconcile_time_seconds_per_instance_bucket{le="0.5"}` shows the number of reconciliations that took under 0.5 seconds to complete for a given instance. |
| `controller_runtime_reconcile_time_seconds_per_instance_count` | Counter | The total number of reconciliation cycles observed for a given instance. |
| `controller_runtime_reconcile_time_seconds_per_instance_sum` | Counter | The total amount of time taken for the observed reconciliations for a given instance. |

GitOps Operator performance metrics

> [!NOTE]
> Gauge is a value that can go up or down. Counter is a value that can only go up.

# Accessing the GitOps Operator metrics

The OpenShift Container Platform web console provides access to GitOps Operator metrics through the **Administrator** perspective. Use these metrics to track reconciliation performance, monitor active instances, and identify potential bottlenecks.

<div>

<div class="title">

Prerequisites

</div>

- You have access to the OpenShift Container Platform web console.

- The Red Hat OpenShift GitOps Operator is installed in the default `openshift-gitops-operator` namespace.

- Cluster monitoring is enabled for the `openshift-gitops-operator` namespace.

</div>

<div>

<div class="title">

Procedure

</div>

1.  In the **Administrator** perspective of the web console, go to **Observe** → **Metrics**.

2.  In the **Expression** field, enter the name of the metric you want to query. See the metrics table for available options.

    - `active_argocd_instances_total`

    - `active_argocd_instances_by_phase`

    - `active_argocd_instance_reconciliation_count`

    - `controller_runtime_reconcile_time_seconds_per_instance_bucket`

    - `controller_runtime_reconcile_time_seconds_per_instance_count`

    - `controller_runtime_reconcile_time_seconds_per_instance_sum`

3.  Optional: Filter the metric by its properties. For example, filter the `active_argocd_instances_by_phase` metric by the `Available` phase:

    **Example:**

    ``` terminal
    active_argocd_instances_by_phase{phase="Available"}
    ```

4.  Optional: Click **Add query** to enter multiple queries.

5.  Click **Run queries** to enable and observe the GitOps Operator metrics.

6.  Review the metrics visualization to monitor Operator performance.

</div>

# Additional resources

- [Installing Red Hat OpenShift GitOps Operator in web console](../../installing_gitops/installing-openshift-gitops.md#installing-gitops-operator-in-web-console_installing-openshift-gitops)
