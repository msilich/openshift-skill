> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/observe-proc_collecting_devspaces_metrics_with_prometheus). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Verify OpenShift Dev Spaces Server metrics collection with Prometheus

Verify that OpenShift Dev Spaces Server JVM metrics are available in Prometheus. The OpenShift Dev Spaces Operator automatically creates and reconciles the required Prometheus resources (ServiceMonitor, Role, and RoleBinding) and configures namespace labeling.

## Before you begin

- You have an active `oc` session with administrative permissions to the OpenShift cluster. See [Getting started with the CLI](https://docs.openshift.com/container-platform/4.22/cli_reference/openshift_cli/getting-started-cli.html).
- OpenShift Dev Spaces is installed and running on the OpenShift cluster.

## Procedure

1.  In the **Administrator** view of the OpenShift web console, go to **Observe** **Metrics**.
2.  Run a PromQL query to confirm that the metrics are available. For example, enter `process_uptime_seconds{job="che-host"}` and click **Run queries**.

## Results

- The query returns data points from the OpenShift Dev Spaces Server JVM.

If the query returns no data, view the Prometheus container logs for possible RBAC-related errors:

1.  Get the name of the Prometheus pod:

    ``` shell-session
    $ oc get pods -l app.kubernetes.io/name=prometheus -n openshift-monitoring -o=jsonpath='{.items[*].metadata.name}'
    ```

2.  Print the last 20 lines of the Prometheus container logs from the Prometheus pod from the previous step:

    ``` shell-session
    $ oc logs --tail=20 <prometheus_pod_name> -c prometheus -n openshift-monitoring
    ```

**Related information**  

- [Querying Prometheus](https://prometheus.io/docs/prometheus/latest/querying/basics/)
- [Prometheus metric types](https://prometheus.io/docs/concepts/metric_types/)
