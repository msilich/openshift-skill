> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/observe-con_observing_devspaces). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# What you can observe about OpenShift Dev Spaces

OpenShift Dev Spaces exposes metrics, logs, and telemetry data that help you monitor platform health, diagnose issues, and track workspace usage.

OpenShift Dev Spaces provides three categories of observability data:

**Metrics**

The OpenShift Dev Spaces server exposes JVM metrics (memory usage, classloading, garbage collection) on port `8087` via the `che-host` Service `/metrics` endpoint. The Dev Workspace Operator exposes workspace startup, failure, and performance metrics on port `8443` via the `devworkspace-controller-metrics` Service `/metrics` endpoint. The OpenShift in-cluster monitoring stack (Prometheus) scrapes both endpoints. The OpenShift Dev Spaces Operator automatically creates the required ServiceMonitor, Role, and RoleBinding resources. You can view these metrics on custom dashboards in the OpenShift web console Administrator perspective.

**Logs**

The OpenShift Dev Spaces server uses configurable log levels for individual loggers. You can increase verbosity for specific components to isolate issues, log HTTP traffic between OpenShift Dev Spaces and the OpenShift API server, and collect diagnostic logs with the `dsc` command-line tool. For log configuration procedures, see Additional resources.

**Telemetry**

Workspace activity events (start, stop, editor actions) can be sent to Segment and Woopra using the built-in Woopra telemetry plugin, or to a custom analytics backend using a telemetry plugin you build yourself. For details on building a custom plugin, see Additional resources.

Note

OpenShift Dev Spaces does not include built-in alerting rules. To receive alerts when metrics exceed thresholds, configure Prometheus alerting rules for the metrics described in this guide.

<span id="con_observing-devspaces_devspaces__entry__1"></span><span id="con_observing-devspaces_devspaces__entry__2"></span>

| Goal | Description |
|----|----|
| Monitor platform health | Enable Prometheus metrics for the OpenShift Dev Spaces server and Dev Workspace Operator, then view dashboards in the OpenShift web console. |
| Configure logging | Control server log verbosity, log HTTP traffic, and collect diagnostic logs with dsc. |
| Configure the Woopra telemetry plugin | Send workspace activity data to Segment and Woopra with a CheCluster CR configuration change. |

Table 1. What do you need to observe?

**Related information**  

- [OpenShift Dev Spaces architecture](discover-con_architecture_overview.md)
- [Build a custom telemetry plugin](extend-assembly_building_telemetry_plugin.md)
- [Configure logging](https://access.redhat.com/documentation/en-us/red_hat_openshift_dev_spaces/3.29/html-single/observe_logging/index#configure-logging_observe_logging)
