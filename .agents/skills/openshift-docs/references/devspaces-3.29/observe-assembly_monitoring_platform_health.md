> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/observe-assembly_monitoring_platform_health). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Monitor platform health

Monitor OpenShift Dev Spaces platform health by enabling Prometheus metrics for the OpenShift Dev Spaces server and the Dev Workspace Operator, then viewing dashboards in the OpenShift web console.

The procedures in this section require an active `oc` session with cluster administrator permissions and access to the OpenShift web console Administrator perspective.

- **[What OpenShift Dev Spaces server metrics reveal](observe-con_monitoring_devspaces.md)**  
  The OpenShift Dev Spaces server exposes JVM metrics such as memory usage and class loading on port `8087` on the `/metrics` endpoint. Monitoring these metrics helps administrators identify performance bottlenecks and plan server capacity.
- **[Enable OpenShift Dev Spaces server metrics](observe-proc_enabling_devspaces_metrics.md)**  
  Enable the OpenShift Dev Spaces JVM metrics endpoint on port `8087` of the `che-host` Service to support performance monitoring and capacity planning.
- **[Verify OpenShift Dev Spaces Server metrics collection with Prometheus](observe-proc_collecting_devspaces_metrics_with_prometheus.md)**  
  Verify that OpenShift Dev Spaces Server JVM metrics are available in Prometheus. The OpenShift Dev Spaces Operator automatically creates and reconciles the required Prometheus resources (ServiceMonitor, Role, and RoleBinding) and configures namespace labeling.
- **[View OpenShift Dev Spaces Server from an OpenShift web console dashboard](observe-proc_viewing_devspaces_server_from_openshift_dashboard.md)**  
  View OpenShift Dev Spaces Server JVM metrics on a custom dashboard in the **Administrator** perspective of the OpenShift web console. This dashboard helps you identify performance bottlenecks and monitor server health.
- **[What Dev Workspace Operator metrics reveal](observe-con_monitoring_devworkspace_operator.md)**  
  The Dev Workspace Operator exposes workspace startup, failure, and performance metrics on port `8443` on the `/metrics` endpoint of the `devworkspace-controller-metrics` Service. The OpenShift in-cluster monitoring stack can scrape these metrics to help administrators track workspace health and diagnose startup failures. For the Prometheus verification procedure, see Additional resources.
- **[Verify Dev Workspace Operator metrics collection with Prometheus](observe-proc_collecting_devworkspace_operator_metrics_with_prometheus.md)**  
  Verify that Dev Workspace Operator metrics are available in Prometheus. The OpenShift Dev Spaces Operator automatically creates and reconciles the required Prometheus resources (ServiceMonitor, Role, and RoleBinding) and configures namespace labeling.
- **[View Dev Workspace Operator metrics from an OpenShift web console dashboard](observe-proc_viewing_devworkspace_operator_from_openshift_dashboard.md)**  
  View Dev Workspace Operator metrics on a custom dashboard in the **Administrator** perspective of the OpenShift web console. This dashboard helps you monitor operator health and detect workspace provisioning issues.

**Related information**  

- [Configure logging](https://access.redhat.com/documentation/en-us/red_hat_openshift_dev_spaces/3.29/html-single/observe_logging/index#configure-logging_observe_logging)
