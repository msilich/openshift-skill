<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

You can gather metrics for hosted control planes by configuring metrics sets. Monitoring dashboards are created in the management cluster for each hosted cluster that it manages.

# Configuring metrics sets for hosted control planes

Hosted control planes creates `ServiceMonitor` resources in each control plane namespace that allow a Prometheus stack to gather metrics from the control planes.

The `ServiceMonitor` resources use metrics relabelings to define which metrics are included or excluded from a particular component, such as etcd or the Kubernetes API server. The number of metrics that are produced by control planes directly impacts the resource requirements of the monitoring stack that gathers them.

Instead of producing a fixed number of metrics that apply to all situations, you can configure a metrics set that identifies a set of metrics to produce for each control plane. The following metrics sets are supported:

- `Telemetry`: These metrics are needed for telemetry. This set is the default set and is the smallest set of metrics.

- `SRE`: This set includes the necessary metrics to produce alerts and allow the troubleshooting of control plane components.

- `All`: This set includes all of the metrics that are produced by standalone OpenShift Container Platform control plane components.

<div>

<div class="title">

Procedure

</div>

- To configure a metrics set, set the `METRICS_SET` environment variable in the HyperShift Operator deployment by entering the following command:

  ``` terminal
  $ oc set env -n hypershift deployment/operator METRICS_SET=All
  ```

</div>

## SRE metrics set example

When you specify the `SRE` metrics set, the HyperShift Operator looks for a config map named `sre-metric-set` with a single key: `config`. The value of the `config` key must contain a set of `RelabelConfigs` that are organized by control plane component.

You can specify the following components:

- `etcd`

- `kubeAPIServer`

- `kubeControllerManager`

- `openshiftAPIServer`

- `openshiftControllerManager`

- `openshiftRouteControllerManager`

- `cvo`

- `olm`

- `catalogOperator`

- `registryOperator`

- `nodeTuningOperator`

- `controlPlaneOperator`

- `hostedClusterConfigOperator`

A configuration of the `SRE` metrics set is illustrated in the following example:

``` terminal
kubeAPIServer:
  - action:       "drop"
    regex:        "etcd_(debugging|disk|server).*"
    sourceLabels: ["__name__"]
  - action:       "drop"
    regex:        "apiserver_admission_controller_admission_latencies_seconds_.*"
    sourceLabels: ["__name__"]
  - action:       "drop"
    regex:        "apiserver_admission_step_admission_latencies_seconds_.*"
    sourceLabels: ["__name__"]
  - action:       "drop"
    regex:        "scheduler_(e2e_scheduling_latency_microseconds|scheduling_algorithm_predicate_evaluation|scheduling_algorithm_priority_evaluation|scheduling_algorithm_preemption_evaluation|scheduling_algorithm_latency_microseconds|binding_latency_microseconds|scheduling_latency_seconds)"
    sourceLabels: ["__name__"]
  - action:       "drop"
    regex:        "apiserver_(request_count|request_latencies|request_latencies_summary|dropped_requests|storage_data_key_generation_latencies_microseconds|storage_transformation_failures_total|storage_transformation_latencies_microseconds|proxy_tunnel_sync_latency_secs)"
    sourceLabels: ["__name__"]
  - action:       "drop"
    regex:        "docker_(operations|operations_latency_microseconds|operations_errors|operations_timeout)"
    sourceLabels: ["__name__"]
  - action:       "drop"
    regex:        "reflector_(items_per_list|items_per_watch|list_duration_seconds|lists_total|short_watches_total|watch_duration_seconds|watches_total)"
    sourceLabels: ["__name__"]
  - action:       "drop"
    regex:        "etcd_(helper_cache_hit_count|helper_cache_miss_count|helper_cache_entry_count|request_cache_get_latencies_summary|request_cache_add_latencies_summary|request_latencies_summary)"
    sourceLabels: ["__name__"]
  - action:       "drop"
    regex:        "transformation_(transformation_latencies_microseconds|failures_total)"
    sourceLabels: ["__name__"]
  - action:       "drop"
    regex:        "network_plugin_operations_latency_microseconds|sync_proxy_rules_latency_microseconds|rest_client_request_latency_seconds"
    sourceLabels: ["__name__"]
  - action:       "drop"
    regex:        "apiserver_request_duration_seconds_bucket;(0.15|0.25|0.3|0.35|0.4|0.45|0.6|0.7|0.8|0.9|1.25|1.5|1.75|2.5|3|3.5|4.5|6|7|8|9|15|25|30|50)"
    sourceLabels: ["__name__", "le"]
kubeControllerManager:
  - action:       "drop"
    regex:        "etcd_(debugging|disk|request|server).*"
    sourceLabels: ["__name__"]
  - action:       "drop"
    regex:        "rest_client_request_latency_seconds_(bucket|count|sum)"
    sourceLabels: ["__name__"]
  - action:       "drop"
    regex:        "root_ca_cert_publisher_sync_duration_seconds_(bucket|count|sum)"
    sourceLabels: ["__name__"]
openshiftAPIServer:
  - action:       "drop"
    regex:        "etcd_(debugging|disk|server).*"
    sourceLabels: ["__name__"]
  - action:       "drop"
    regex:        "apiserver_admission_controller_admission_latencies_seconds_.*"
    sourceLabels: ["__name__"]
  - action:       "drop"
    regex:        "apiserver_admission_step_admission_latencies_seconds_.*"
    sourceLabels: ["__name__"]
  - action:       "drop"
    regex:        "apiserver_request_duration_seconds_bucket;(0.15|0.25|0.3|0.35|0.4|0.45|0.6|0.7|0.8|0.9|1.25|1.5|1.75|2.5|3|3.5|4.5|6|7|8|9|15|25|30|50)"
    sourceLabels: ["__name__", "le"]
openshiftControllerManager:
  - action:       "drop"
    regex:        "etcd_(debugging|disk|request|server).*"
    sourceLabels: ["__name__"]
openshiftRouteControllerManager:
  - action:       "drop"
    regex:        "etcd_(debugging|disk|request|server).*"
    sourceLabels: ["__name__"]
olm:
  - action:       "drop"
    regex:        "etcd_(debugging|disk|server).*"
    sourceLabels: ["__name__"]
catalogOperator:
  - action:       "drop"
    regex:        "etcd_(debugging|disk|server).*"
    sourceLabels: ["__name__"]
cvo:
  - action: drop
    regex: "etcd_(debugging|disk|server).*"
    sourceLabels: ["__name__"]
```

# Customized hosted cluster identifiers

When you enable observability for hosted control planes, control plane metrics include an `_id` label that identifies the hosted cluster. You can set `spec.clusterID` in the `HostedCluster` custom resource (CR) at creation time to use a stable identifier instead of a randomly assigned UUID.

When you forward hosted cluster metrics to an external monitoring system, the `_id` label is commonly used to identify the cluster. If you reinstall a hosted cluster, specifying the same `clusterID` value preserves your external monitoring configuration.

Each hosted cluster has a unique cluster identifier. The HyperShift Operator uses this identifier in telemetry and in metrics that the control plane operators produce. The identifier is exposed on time series as the `_id` label.

If you do not specify `spec.clusterID` when you create a `HostedCluster` CR, the HyperShift controller generates a random RFC4122 UUID and sets the field for you.

> [!NOTE]
> The `spec.clusterID` specification is not the same as the `spec.infraID` specification. The `infraID` value identifies cloud infrastructure resources.

## Example: Setting a custom cluster identifier

You can set the `spec.clusterID` value only when you create a `HostedCluster` custom resource (CR).

> [!IMPORTANT]
> After you set `spec.clusterID` is set, you cannot change it. Plan the identifier before you create the hosted cluster.

The following example shows a `HostedCluster` CR with a custom cluster identifier set:

<div class="formalpara">

<div class="title">

Example `HostedCluster` CR with a custom cluster identifier

</div>

``` yaml
apiVersion: hypershift.openshift.io/v1beta1
kind: HostedCluster
metadata:
  name: <hosted_cluster_name>
  namespace: <hosted_cluster_namespace>
spec:
  clusterID: fa45babd-40f3-4085-9b30-8bc3b7df1557
  controllerAvailabilityPolicy: SingleReplica
  dns:
    baseDomain: example.com
  platform:
    type: AWS
  release:
    image: <ocp_release_image>
  pullSecret:
    name: <pull_secret_name>
```

</div>

The `spec.clusterID` value is the UUID that you want to use as the stable cluster identifier in metrics. The value must be a valid RFC4122 UUID: `xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx` in hexadecimal digits.

The value of `spec.clusterID` is added as the `_id` label on control plane metrics through Prometheus relabeling rules on `ServiceMonitor` and `PodMonitor` resources. HyperShift Operator metrics for the hosted cluster also use the same `_id` label, so you can correlate metrics from the management cluster and the hosted control plane in one query.

For example, to filter metrics for a specific hosted cluster, use the `_id` label in a PromQL expression:

``` promql
{__name__=~"hypershift_.*", _id="fa45babd-40f3-4085-9b30-8bc3b7df1557"}
```

When you enable monitoring dashboards, the `CLUSTER_ID` placeholder in the dashboard template is replaced with the same UUID. For more information, see "Dashboard customization".

### Cluster identifier reuse after a reinstall

If you delete and re-create a hosted cluster, a new random `clusterID` is assigned unless you specify one. To keep the same identifier in external monitoring systems, set `spec.clusterID` in the new `HostedCluster` CR to the UUID that you used before.

<div>

<div class="title">

Additional resources

</div>

- [Dashboard customization](hcp-observability.md#hcp-customize-dashboards_hcp-observability)

- [Configuring metrics sets for hosted control planes](hcp-observability.md#hosted-control-planes-metrics-sets_hcp-observability)

- [Enabling monitoring dashboards in a hosted cluster](hcp-observability.md#hosted-control-planes-monitoring-dashboard_hcp-observability)

</div>

# Enabling monitoring dashboards in a hosted cluster

You can enable monitoring dashboards in a hosted cluster by creating a config map.

<div>

<div class="title">

Procedure

</div>

1.  Create the `hypershift-operator-install-flags` config map in the `local-cluster` namespace. See the following example configuration:

    ``` yaml
    kind: ConfigMap
    apiVersion: v1
    metadata:
      name: hypershift-operator-install-flags
      namespace: local-cluster
    data:
      installFlagsToAdd: "--monitoring-dashboards --metrics-set=All"
      installFlagsToRemove: ""
    ```

    The `--monitoring-dashboards --metrics-set=All` flag adds the monitoring dashboard for all metrics.

2.  Wait a couple of minutes for the HyperShift Operator deployment in the `hypershift` namespace to be updated to include the following environment variable:

    ``` yaml
        - name: MONITORING_DASHBOARDS
          value: "1"
    ```

    When monitoring dashboards are enabled, for each hosted cluster that the HyperShift Operator manages, the Operator creates a config map named `hc-<hosted_cluster_namespace>-<hosted_cluster_name>` in the `openshift-config-managed` namespace, where `<hosted_cluster_namespace>` is the namespace of the hosted cluster and `<hosted_cluster_name>` is the name of the hosted cluster. As a result, a new dashboard is added in the administrative console of the management cluster.

3.  To view the dashboard, log in to the management cluster’s console and go to the dashboard for the hosted cluster by clicking **Observe → Dashboards**.

4.  Optional: To disable monitoring dashboards in a hosted cluster, remove the `--monitoring-dashboards --metrics-set=All` flag from the `hypershift-operator-install-flags` config map. When you delete a hosted cluster, its corresponding dashboard is also deleted.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Customized hosted cluster identifiers](hcp-observability.md#hcp-cluster-ids_hcp-observability)

</div>

## Dashboard customization

To generate dashboards for each hosted cluster, the HyperShift Operator uses a template that is stored in the `monitoring-dashboard-template` config map in the Operator namespace (`hypershift`). This template contains a set of Grafana panels that contain the metrics for the dashboard.

You can edit the content of the config map to customize the dashboards.

When a dashboard is generated, the following strings are replaced with values that correspond to a specific hosted cluster:

| Name | Description |
|----|----|
| `__NAME__` | The name of the hosted cluster |
| `__NAMESPACE__` | The namespace of the hosted cluster |
| `__CONTROL_PLANE_NAMESPACE__` | The namespace where the control plane pods of the hosted cluster are placed |
| `__CLUSTER_ID__` | The UUID of the hosted cluster, which matches the `_id` label of the hosted cluster metrics |

To set a custom cluster identifier when you create the hosted cluster, see "Customized hosted cluster identifiers".

# Control plane metrics for hosted control planes

You can observe hosted control plane health from the hosted cluster monitoring stack when metrics forwarding is enabled.

With propagated metrics, you can diagnose API server, etcd, Operator, and scheduling issues from the hosted cluster web console and CLI without management cluster credentials.

This capability is available in OpenShift Container Platform 4.22 and later.

Before OpenShift Container Platform 4.22, control plane components for hosted control planes ran on the management cluster and were invisible to the Cluster Monitoring Operator stack in the hosted cluster. Hosted cluster administrators could not query metrics such as `apiserver_request_total`, `etcd_mvcc_db_total_size_in_bytes`, or `csv_succeeded` from the hosted cluster Prometheus.

With metrics forwarding, selected control plane metrics are propagated from the management cluster into the hosted cluster platform Prometheus.

After you enable forwarding on the `HostedCluster` resource, you can use familiar PromQL queries, alerts, and dashboards.

## Metrics forwarding architecture

When you enable metrics forwarding, hosted control planes deploys components on both the management cluster and the hosted cluster.

On the management cluster, in the hosted control plane namespace, the following steps take place:

- The `endpoint-resolver` deployment discovers pod IP addresses for control plane components.

- The `metrics-proxy` deployment scrapes control plane pods, applies per-component metric filters, injects OpenShift Container Platform-compatible labels, and serves aggregated metrics at paths, such as `/metrics/kube-apiserver` and `/metrics/etcd`, behind a TLS-passthrough Route.

On the hosted cluster, in the `openshift-monitoring` namespace, the following steps take place:

- The `control-plane-metrics-forwarder` deployment runs HAProxy and TCP-proxies scrape requests to the management cluster `metrics-proxy` Route.

- A `PodMonitor` named `control-plane-metrics-forwarder` configures platform Prometheus to scrape the forwarder using mutual TLS (mTLS).

The data path is as follows:

1.  Platform Prometheus in the hosted cluster discovers the `PodMonitor` and scrapes the metrics-forwarder.

2.  The metrics-forwarder forwards the scrape over mTLS to the management cluster `metrics-proxy` Route.

3.  The metrics-proxy scrapes control plane pods through the endpoint-resolver and returns filtered, relabeled metrics.

## Enabling metrics forwarding

Enable metrics forwarding so that you can observe hosted control plane health from the hosted cluster monitoring stack.

If you are a hosted cluster administrator without management cluster access, ask a platform administrator enable metrics forwarding on your `HostedCluster` resource.

<div>

<div class="title">

Prerequisites

</div>

- You have a hosted cluster that is version 4.22 or later.

- You have the multicluster engine for Kubernetes Operator version 2.17 or later.

- You are logged in to the management cluster. Alternatively, you can use a `kubeconfig` file with access to the namespace that contains the `HostedCluster` resource. The `HostedCluster` object exists on the management cluster; annotating it from a hosted cluster `kubeconfig` file fails or targets the wrong resource.

</div>

<div>

<div class="title">

Procedure

</div>

- Add the `hypershift.openshift.io/enable-metrics-forwarding=true` annotation to the `HostedCluster` resource on the management cluster by entering the following command:

  ``` terminal
  $ oc annotate hostedcluster -n <hosted_cluster_namespace> <hosted_cluster_name> \
    hypershift.openshift.io/enable-metrics-forwarding=true
  ```

  Replace `<hosted_cluster_namespace>` with the namespace of the hosted cluster and `<hosted_cluster_name>` with the name of the hosted cluster.

- To disable metrics forwarding, remove the annotation by entering the following command:

  ``` terminal
  $ oc annotate hostedcluster -n <hosted_cluster_namespace> <hosted_cluster_name> \
    hypershift.openshift.io/enable-metrics-forwarding-
  ```

</div>

## Querying control plane metrics in hosted clusters by using the CLI

After you enable metrics forwarding, you can verify that control plane metrics are ingested and query them from the CLI.

Use the same PromQL patterns as standalone OpenShift Container Platform clusters because the metrics-proxy injects compatible labels.

<div>

<div class="title">

Prerequisites

</div>

- Metrics forwarding is enabled on the `HostedCluster` resource. For enablement steps, see "Enabling metrics forwarding".

- You have `cluster-admin` access to the hosted cluster.

- At least two minutes have elapsed since you enabled forwarding so Prometheus can complete initial scrapes.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Verify that the `control-plane-metrics-forwarder` deployment exists in the `openshift-monitoring` namespace:

    ``` terminal
    $ oc get deployment control-plane-metrics-forwarder -n openshift-monitoring
    ```

    > [!NOTE]
    > Control plane metrics are available when the Cluster Monitoring Operator and platform Prometheus are running, even if no compute nodes are scheduled. Data-plane node and workload metrics still require compute nodes.

2.  Verify that the `control-plane-metrics-forwarder` `PodMonitor` exists:

    ``` terminal
    $ oc get podmonitor control-plane-metrics-forwarder -n openshift-monitoring
    ```

3.  Optional: Verify that management-cluster components are running by logging in to the management cluster:

    1.  Enter the following command:

        ``` terminal
        $ oc get deployment endpoint-resolver metrics-proxy -n <hcp_namespace>
        ```

        Replace `<hcp_namespace>` with the namespace for your hosted cluster. Typically, the format of the namespace is `<hosted_cluster_namespace>-<hosted_cluster_name>`.

    2.  Enter the following command:

        ``` terminal
        $ oc get route metrics-proxy -n <hcp_namespace>
        ```

4.  Verify that Prometheus scraped targets for the forwarder report:

    ``` terminal
    $ oc exec -n openshift-monitoring prometheus-k8s-0 -c prometheus -- \
      curl -s http://localhost:9090/api/v1/targets \
      | jq '.data.activeTargets[] | select(.scrapePool | contains("control-plane-metrics-forwarder")) | {scrapePool, scrapeUrl: .scrapeUrl, health}'
    ```

    You should see one target per forwarded component with the status of `"health": "up"`.

5.  Confirm that Kubernetes API server metrics are ingested by querying `apiserver_request_total`:

    ``` terminal
    $ oc exec -n openshift-monitoring prometheus-k8s-0 -c prometheus -- \
      curl -gs 'http://localhost:9090/api/v1/query?query=apiserver_request_total{job="apiserver"}' \
      | jq '.data.result | length'
    ```

    A nonzero result confirms that API server metrics are available in the guest cluster monitoring stack.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Exposed metrics](../operators/understanding/olm/olm-understanding-metrics.md#olm-metrics_olm-understanding-metrics)

</div>

## Querying control plane metrics in hosted clusters by using the web console

After you enable metrics forwarding, you can verify that control plane metrics are ingested and query them from the web console.

Use the same PromQL patterns as standalone OpenShift Container Platform clusters because the metrics-proxy injects compatible labels.

<div>

<div class="title">

Prerequisites

</div>

- Metrics forwarding is enabled on the `HostedCluster` resource. For enablement steps, see "Enabling metrics forwarding".

- You have `cluster-admin` access to the hosted cluster.

- At least two minutes have elapsed since you enabled forwarding so Prometheus can complete initial scrapes.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Log in to the OpenShift Container Platform web console for the hosted cluster.

2.  Click **Observe** → **Metrics**.

3.  In the query field, enter a PromQL expression and run the query.

    Use the following examples:

    <div class="formalpara">

    <div class="title">

    Operator health

    </div>

    ``` text
    csv_succeeded{job="olm-operator-metrics"} == 0
    ```

    </div>

    This query lists CSVs that are not in the `Succeeded` state.

    <div class="formalpara">

    <div class="title">

    API server request rate

    </div>

    ``` text
    sum(rate(apiserver_request_total{job="apiserver"}[5m])) by (verb, code)
    ```

    </div>

    <div class="formalpara">

    <div class="title">

    Scheduler activity

    </div>

    ``` text
    sum(rate(scheduler_schedule_attempts_total[5m])) by (result)
    ```

    </div>

    This query is available on OpenShift Container Platform 4.22 and later with metrics forwarding enabled.

    <div class="formalpara">

    <div class="title">

    Workload-oriented API saturation

    </div>

    ``` text
    apiserver_current_inflight_requests{job="apiserver"}
    ```

    </div>

    <div class="formalpara">

    <div class="title">

    Scheduling backlog

    </div>

    ``` text
    scheduler_pending_pods
    ```

    </div>

    <div class="formalpara">

    <div class="title">

    Controller workqueue depth

    </div>

    ``` text
    workqueue_depth{job="kube-controller-manager"}
    ```

    </div>

    For `csv_succeeded` and other OLM metrics, see "Exposed metrics".

</div>

<div>

<div class="title">

Verification

</div>

- Prometheus targets for `control-plane-metrics-forwarder` scrape pools report the `health: up` status.

- PromQL queries for `apiserver_request_total{job="apiserver"}` return nonzero results.

- Example queries in the web console return time series for enabled components.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Exposed metrics](../operators/understanding/olm/olm-understanding-metrics.md#olm-metrics_olm-understanding-metrics)

</div>

## Importing control plane health dashboards

You can import a sample Grafana dashboard that visualizes propagated control plane metrics in the hosted cluster web console. The dashboard covers API server, etcd, cluster Operators, scheduler, controller manager, and OLM health panels.

<div>

<div class="title">

Prerequisites

</div>

- Metrics forwarding is enabled and verified.

- The HyperShift Operator uses `METRICS_SET=All` or `METRICS_SET=SRE` with a matching `sre-metric-set` `ConfigMap` object in the hosted control plane namespace. The default `Telemetry` metrics set forwards only a small metric subset and leaves most dashboard panels empty.

- You have `cluster-admin` access to the hosted cluster.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Download the sample dashboard JSON file by entering the following command:

    ``` terminal
    $ curl -LO https://raw.githubusercontent.com/openshift/hypershift/main/contrib/metrics/guest-control-plane-dashboard.json
    ```

    > [!NOTE]
    > If you deploy user-workload Grafana through the Grafana Operator, import the dashboard JSON as a `GrafanaDashboard` custom resource instead of using a console `ConfigMap` object.

2.  Create a `ConfigMap` object from the dashboard file in the `openshift-config-managed` namespace by entering the following command:

    ``` terminal
    $ oc create configmap guest-control-plane-dashboard \
      --from-file=guest-control-plane-dashboard.json=guest-control-plane-dashboard.json \
      -n openshift-config-managed
    ```

3.  Label the `ConfigMap` object so the console discovers it as a dashboard by entering the following command:

    ``` terminal
    $ oc label configmap guest-control-plane-dashboard \
      console.openshift.io/dashboard=true \
      -n openshift-config-managed
    ```

4.  Log in to the web console and click **Observe** → **Dashboards**.

5.  Select the **Hosted Cluster Control Plane** dashboard.

6.  Optional: If you use `METRICS_SET=SRE` on the HyperShift Operator, configure the Operator and create or update the `sre-metric-set` `ConfigMap` object in the hosted control plane namespace with relabel configurations that forward the dashboard metric names.

    1.  Log in to the management cluster and set the metrics set on the HyperShift Operator by entering the following command:

        ``` terminal
        $ oc set env -n hypershift deployment/operator METRICS_SET=SRE
        ```

    2.  Replace `<hcp_namespace>` with your hosted control plane namespace and create the `ConfigMap` object:

        ``` yaml
        apiVersion: v1
        kind: ConfigMap
        metadata:
          name: sre-metric-set
          namespace: <hcp_namespace>
        data:
          config: |
            kubeAPIServer:
              - action: keep
                sourceLabels: ["__name__"]
                regex: "(apiserver_request_total|apiserver_request_duration_seconds_bucket|apiserver_current_inflight_requests|apiserver_storage_objects)"
            etcd:
              - action: keep
                sourceLabels: ["__name__"]
                regex: "(etcd_mvcc_db_total_size_in_bytes|etcd_mvcc_db_total_size_in_use_in_bytes|etcd_disk_wal_fsync_duration_seconds_bucket|etcd_disk_backend_commit_duration_seconds_bucket|etcd_network_peer_round_trip_time_seconds_bucket|etcd_server_leader_changes_seen_total|etcd_server_has_leader)"
            kubeControllerManager:
              - action: keep
                sourceLabels: ["__name__"]
                regex: "(workqueue_depth|workqueue_adds_total)"
            kubeScheduler:
              - action: keep
                sourceLabels: ["__name__"]
                regex: "(scheduler_e2e_scheduling_duration_seconds_count|scheduler_schedule_attempts_total|scheduler_pending_pods)"
            cvo:
              - action: keep
                sourceLabels: ["__name__"]
                regex: "(cluster_version|cluster_operator_up|cluster_operator_conditions)"
            olm:
              - action: keep
                sourceLabels: ["__name__"]
                regex: "(csv_succeeded)"
        ```

        This configuration forwards 20 metric names across five components that the dashboard uses.

        For full `SRE` metrics set configuration, see "Configuring the SRE metrics set".

    3.  Apply the `ConfigMap` object on the management cluster:

        ``` terminal
        $ oc apply -f sre-metric-set.yaml
        ```

        The Control Plane Operator detects the `ConfigMap` object change and updates the `metrics-proxy` configuration.

</div>

<div>

<div class="title">

Verification

</div>

- The dashboard is displayed under **Observe** → **Dashboards** in the web console.

- Panels display data when the configured metrics set includes the required metric names.

- The etcd database size panels show current use relative to the 8 GB limit.

</div>

# Connectivity monitoring for hosted control planes

Cluster service providers can monitor connectivity metrics to ensure proper function during an update. They can also use the metrics to find connectivity issues between the control plane and the data plane, or vice versa.

Studying these metrics over time can inform decisions about capacity planning and scaling.

## Connectivity monitoring from the control plane to the data plane

Cluster administrators can monitor network activity between a hosted control plane and the compute nodes in a data plane by using the `DataPlaneConnectionAvailable` condition. This condition is useful for identifying and troubleshooting network connectivity issues in hosted clusters.

The `DataPlaneConnectionAvailable` condition is available by default starting with version 4.21.

The `DataPlaneConnectionAvailable` condition monitors the connectivity from the control plane to the data plane by taking the following steps:

1.  Counts available compute nodes in the hosted cluster.

2.  Lists the `konnectivity-agent` pods that are running in the `kube-system` namespace on the data plane.

3.  Reads the logs from the running `konnectivity-agent` pod to verify that it can communicate with the data plane.

The `hosted-cluster-config-operator` component that runs in the control plane namespace evaluates the condition and provides status and reason information.

The following table details the status and reason values that can be displayed for the condition:

| Status | Reason value | Description |
|----|----|----|
| `True` | `AsExpected` | The control plane can reach the data plane nodes through the `konnectivity-agent` pods. |
| `False` | `KonnectivityAgentPodsNotFound` | No `konnectivity-agent` pods are running, or none are found. |
| `False` | `ReconciliationError` | An error occurred while listing the `konnectivity-agent` pods. |
| `Unknown` | `NoWorkerNodesAvailable` | No compute nodes are available in the cluster. No errors occurred, but no compute nodes were found. |
| `Unknown` | `ReconcileError` | Unable to count compute nodes because an error occurred. |

For information about how to troubleshoot connectivity issues, see "Troubleshooting connectivity for hosted control planes".

<div>

<div class="title">

Additional resources

</div>

- [Troubleshooting connectivity for hosted control planes](hcp-troubleshooting.md#hcp-ts-connectivity_hcp-troubleshooting)

</div>

## Connectivity monitoring from the data plane to the control plane

Cluster administrators can monitor network activity between the compute nodes in a data plane and a hosted control plane by using the `ControlPlaneConnectionAvailable` condition. This condition is useful for identifying and troubleshooting network connectivity issues in hosted clusters.

The `ControlPlaneConnectionAvailable` condition detects whether data plane nodes can reach control plane components. The `hosted-cluster-config-operator` component evaluates the condition, and a deployment with 3 replicas checks connectivity.

The condition monitors the connectivity between the data plane and the control plane by taking the following steps:

1.  Deploys a `kas-connection-checker` deployment to the `kube-system` namespace on the data plane.

2.  Each pod runs a shell script in an infinite loop that transfers data to and from the Kubernetes API server endpoint every 60 seconds. On success, the script patches the `control-plane-connectivity-check` config map with a `lastSucceeded` timestamp.

3.  The `hosted-cluster-config-operator` component checks whether the `control-plane-connectivity-check` config map exists and whether the `lastSucceeded` timestamp is within the last 5 minutes. It does not check pod readiness counts.

The following table details the status and reason values that can be displayed for the condition:

| Status | Reason value | Description |
|----|----|----|
| `True` | `AsExpected` | All data plane nodes can reach the control plane (`NumberReady = DesiredNumberScheduled`). |
| `False` | `KASAccessFailed` | At least one data plane node cannot reach the control plane. The message shows the ratio of pods that are ready; for example, `1/3 pods ready`. |
| `Unknown` | `NoWorkerNodesAvailable` | No compute nodes are available to check connectivity (`DesiredNumberScheduled = 0`). |
| `Unknown` | `StatusUnknown` | The Kubernetes API server connection checker DaemonSet was not found. |
| `Unknown` | `ReconcileError` | An API error blocked the retrieval of the DaemonSet status. |

> [!IMPORTANT]
> This condition has a known limitation with HTTPS proxy environments. In HTTPS proxy environments, the condition might incorrectly report `False` because of probe limitations.
