<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

The Custom Metrics Autoscaler Operator exposes ready-to-use metrics that it pulls from the on-cluster monitoring component. You can query the metrics by using the Prometheus Query Language (PromQL) to analyze and diagnose issues. All metrics are reset when the controller pod restarts.

# Accessing performance metrics

You can access the metrics and run queries by using the OpenShift Container Platform web console.

<div>

<div class="title">

Procedure

</div>

1.  Select the **Administrator** perspective in the OpenShift Container Platform web console.

2.  Select **Observe** → **Metrics**.

3.  To create a custom query, add your PromQL query to the **Expression** field.

4.  To add multiple queries, select **Add Query**.

</div>

## Provided Operator metrics

The Custom Metrics Autoscaler Operator exposes the following metrics, which you can view by using the OpenShift Container Platform web console.

| Metric name | Description |
|----|----|
| `keda_scaler_activity` | Whether the particular scaler is active or inactive. A value of `1` indicates the scaler is active; a value of `0` indicates the scaler is inactive. |
| `keda_scaler_metrics_value` | The current value for each scaler’s metric, which is used by the Horizontal Pod Autoscaler (HPA) in computing the target average. |
| `keda_scaler_metrics_latency` | The latency of retrieving the current metric from each scaler. |
| `keda_scaler_errors` | The number of errors that have occurred for each scaler. |
| `keda_scaler_errors_total` | The total number of errors encountered for all scalers. |
| `keda_scaled_object_errors` | The number of errors that have occurred for each scaled obejct. |
| `keda_resource_totals` | The total number of Custom Metrics Autoscaler custom resources in each namespace for each custom resource type. |
| `keda_trigger_totals` | The total number of triggers by trigger type. |

Custom Metric Autoscaler Operator metrics

<div class="formalpara">

<div class="title">

Custom Metrics Autoscaler Admission webhook metrics

</div>

The Custom Metrics Autoscaler Admission webhook also exposes the following Prometheus metrics.

</div>

| Metric name | Description |
|----|----|
| `keda_scaled_object_validation_total` | The number of scaled object validations. |
| `keda_scaled_object_validation_errors` | The number of validation errors. |
