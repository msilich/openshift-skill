> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/observe-proc_viewing_devworkspace_operator_from_openshift_dashboard). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# View Dev Workspace Operator metrics from an OpenShift web console dashboard

View Dev Workspace Operator metrics on a custom dashboard in the **Administrator** perspective of the OpenShift web console. This dashboard helps you monitor operator health and detect workspace provisioning issues.

## Before you begin

- You have an instance of OpenShift Dev Spaces installed and running in OpenShift.
- You have an active `oc` session with administrative permissions to the OpenShift cluster. See [Getting started with the CLI](https://docs.openshift.com/container-platform/4.22/cli_reference/openshift_cli/getting-started-cli.html).
- The in-cluster Prometheus instance is collecting metrics. See [Verify Dev Workspace Operator metrics collection with Prometheus](observe-proc_collecting_devworkspace_operator_metrics_with_prometheus.md "Verify that Dev Workspace Operator metrics are available in Prometheus. The OpenShift Dev Spaces Operator automatically creates and reconciles the required Prometheus resources (ServiceMonitor, Role, and RoleBinding) and configures namespace labeling.").

## Procedure

Create a ConfigMap for the dashboard definition in the `openshift-config-managed` project and apply the necessary label.

1.  Create the ConfigMap:

    ``` bash
    $ oc create configmap grafana-dashboard-dwo \
      --from-literal=dwo-dashboard.json="$(curl https://raw.githubusercontent.com/devfile/devworkspace-operator/main/docs/grafana/openshift-console-dashboard.json)" \
      -n openshift-config-managed
    ```

    Note

    The previous command contains a link to material from the upstream community. This material represents the very latest available content and the most recent best practices. These tips have not yet been vetted by Red Hat's QE department, and they have not yet been proven by a wide user group. Please, use this information cautiously.

2.  Apply the dashboard label:

    ``` bash
    $ oc label configmap grafana-dashboard-dwo console.openshift.io/dashboard=true -n openshift-config-managed
    ```

    Note

    The dashboard definition is based on Grafana 6.x dashboards. Not all Grafana 6.x dashboard features are supported in the OpenShift web console.

## Results

1.  In the **Administrator** view of the OpenShift web console, go to **Observe** **Dashboards**.
2.  Go to **Dashboard** **Dev Workspace Operator** and verify that the dashboard panels contain data.

**Related concepts**  

- [What Dev Workspace Operator metrics reveal](observe-con_monitoring_devworkspace_operator.md "The Dev Workspace Operator exposes workspace startup, failure, and performance metrics on port 8443 on the /metrics endpoint of the devworkspace-controller-metrics Service. The OpenShift in-cluster monitoring stack can scrape these metrics to help administrators track workspace health and diagnose startup failures. For the Prometheus verification procedure, see Additional resources.")

**Related tasks**  

- [Verify Dev Workspace Operator metrics collection with Prometheus](observe-proc_collecting_devworkspace_operator_metrics_with_prometheus.md "Verify that Dev Workspace Operator metrics are available in Prometheus. The OpenShift Dev Spaces Operator automatically creates and reconciles the required Prometheus resources (ServiceMonitor, Role, and RoleBinding) and configures namespace labeling.")

**Related information**  

- [OpenShift Documentation: Managing metrics](https://docs.openshift.com/container-platform/4.22/monitoring/managing-metrics.html)
