> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/observe-proc_collecting_devworkspace_operator_metrics_with_prometheus). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Verify Dev Workspace Operator metrics collection with Prometheus

Verify that Dev Workspace Operator metrics are available in Prometheus. The OpenShift Dev Spaces Operator automatically creates and reconciles the required Prometheus resources (ServiceMonitor, Role, and RoleBinding) and configures namespace labeling.

## Before you begin

- You have an active `oc` session with administrative permissions to the OpenShift cluster. See [Getting started with the CLI](https://docs.openshift.com/container-platform/4.22/cli_reference/openshift_cli/getting-started-cli.html).
- OpenShift Dev Spaces is installed and running on the OpenShift cluster.
- At least one workspace has been started to generate metrics.

## Procedure

1.  For a fresh installation of OpenShift Dev Spaces, generate metrics by creating a OpenShift Dev Spaces workspace from the Dashboard.
2.  In the **Administrator** view of the OpenShift web console, go to **Observe** **Metrics**.
3.  Run a PromQL query to confirm that the metrics are available. For example, enter `devworkspace_started_total` and click **Run queries**.

## Results

- The query returns data points from the Dev Workspace Operator.

If the query returns no data, view the Prometheus container logs for possible RBAC-related errors:

1.  Get the name of the Prometheus pod:

    ``` shell-session
    $ oc get pods -l app.kubernetes.io/name=prometheus -n openshift-monitoring -o=jsonpath='{.items[*].metadata.name}'
    ```

2.  Print the last 20 lines of the Prometheus container logs from the Prometheus pod from the previous step:

    ``` shell-session
    $ oc logs --tail=20 <prometheus_pod_name> -c prometheus -n openshift-monitoring
    ```

**Related concepts**  

- [What Dev Workspace Operator metrics reveal](observe-con_monitoring_devworkspace_operator.md "The Dev Workspace Operator exposes workspace startup, failure, and performance metrics on port 8443 on the /metrics endpoint of the devworkspace-controller-metrics Service. The OpenShift in-cluster monitoring stack can scrape these metrics to help administrators track workspace health and diagnose startup failures. For the Prometheus verification procedure, see Additional resources.")

**Related information**  

- [Querying Prometheus](https://prometheus.io/docs/prometheus/latest/querying/basics/)
- [Prometheus metric types](https://prometheus.io/docs/concepts/metric_types/)
