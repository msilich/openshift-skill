> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/observe-con_monitoring_devspaces). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# What OpenShift Dev Spaces server metrics reveal

The OpenShift Dev Spaces server exposes JVM metrics such as memory usage and class loading on port `8087` on the `/metrics` endpoint. Monitoring these metrics helps administrators identify performance bottlenecks and plan server capacity.

**Related tasks**  

- [Enable OpenShift Dev Spaces server metrics](observe-proc_enabling_devspaces_metrics.md "Enable the OpenShift Dev Spaces JVM metrics endpoint on port 8087 of the che-host Service to support performance monitoring and capacity planning.")
- [Verify OpenShift Dev Spaces Server metrics collection with Prometheus](observe-proc_collecting_devspaces_metrics_with_prometheus.md "Verify that OpenShift Dev Spaces Server JVM metrics are available in Prometheus. The OpenShift Dev Spaces Operator automatically creates and reconciles the required Prometheus resources (ServiceMonitor, Role, and RoleBinding) and configures namespace labeling.")
- [View OpenShift Dev Spaces Server from an OpenShift web console dashboard](observe-proc_viewing_devspaces_server_from_openshift_dashboard.md "View OpenShift Dev Spaces Server JVM metrics on a custom dashboard in the Administrator perspective of the OpenShift web console. This dashboard helps you identify performance bottlenecks and monitor server health.")
