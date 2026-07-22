<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Use the Network Observability Operator to observe network traffic via `eBPF` technology, providing troubleshooting insights through Prometheus metrics and Loki logs.

You can view and analyze this stored information in the OpenShift Container Platform console for further insight and troubleshooting.

# Network Observability Operator

The Network Observability Operator provides the cluster-scoped `FlowCollector` API custom resource, which manages a pipeline of eBPF agents and services that collect, enrich, and store network flows in Loki or Prometheus.

A `FlowCollector` instance deploys pods and services that form a monitoring pipeline.

The `eBPF` agent is deployed as a `daemonset` object and creates the network flows. The pipeline collects and enriches network flows with Kubernetes metadata before storing them in Loki or generating Prometheus metrics.

# Optional dependencies of the Network Observability Operator

Integrate the Network Observability Operator with optional dependencies, such as the Loki Operator for flow storage and AMQ Streams (Kafka) for resilient, large-scale data handling and scalability.

Supported optional dependencies include the Loki Operator for flow storage, and AMQ Streams for large-scale data handling with Kafka.

Loki Operator
You can use Loki as the backend to store all collected flows with a maximal level of details. It is recommended to use the Red Hat supported Loki Operator to install Loki. You can also choose to use network observability without Loki, but you need to consider some factors. For more information, see "Network observability without Loki".

AMQ Streams Operator
Kafka provides scalability, resiliency and high availability in the OpenShift Container Platform cluster for large scale deployments.

> [!NOTE]
> If you choose to use Kafka, it is recommended to use Red Hat supported AMQ Streams Operator.

<div id="additional-resources-operator_network-observability-overview">

<div class="title">

Additional resources

</div>

- [Network observability without Loki](installing-operators.md#network-observability-without-loki_network_observability)

- [Red Hat AMQ Streams](https://docs.redhat.com/en/documentation/red_hat_streams_for_apache_kafka/2.2)

</div>

# OpenShift Container Platform console integration

The Network Observability Operator integrates with the OpenShift Container Platform console, providing an overview, topology view, and traffic flow tables.

The Network observability metrics dashboards in **Observe** → **Dashboards** are available only to users with administrator access.

> [!NOTE]
> To enable multi-tenancy for developer access and for administrators with limited access to namespaces, you must specify permissions by defining roles. For more information, see "Enabling multi-tenancy in network observability".

<div id="additional-resources-console_network-observability-overview">

<div class="title">

Additional resources

</div>

- [Enabling multi-tenancy in network observability](installing-operators.md#network-observability-multi-tenancy_network_observability)

</div>

## Network observability metrics dashboards

Review the network observability metrics dashboards in the OpenShift Container Platform console, which provide overall traffic flow aggregation, filtering options, and dedicated dashboards for monitoring operator health.

In the OpenShift Container Platform console on the **Overview** tab, you can view the overall aggregated metrics of the network traffic flow on the cluster. You can choose to display the information by cluster, node, namespace, owner, pod, and service. Filters and display options can further refine the metrics. For more information, see "Observing the network traffic from the Overview view".

In **Observe** → **Dashboards**, the **Netobserv** dashboards provide a quick overview of the network flows in your OpenShift Container Platform cluster. The **Netobserv/Health** dashboard provides metrics about the health of the Operator. For more information, see "Network observability metrics" and "Viewing health information".

<div id="additional-resources-dashboards_network-observability-overview">

<div class="title">

Additional resources

</div>

- [Observing the network traffic from the Overview view](observing-network-traffic.md#network-observability-network-traffic-overview-view_nw-observe-network-traffic)

- [Network observability metrics](metrics-alerts-dashboards.md#network-observability-metrics_metrics-dashboards-alerts)

- [Health dashboards](network-observability-operator-monitoring.md#network-observability-health-dashboard-overview_network_observability)

</div>

## Network observability topology views

The network observability topology view in the OpenShift Container Platform console displays a graphical representation of traffic flow between components, which you can refine using various filters and display options.

The OpenShift Container Platform console offers the **Topology** tab which represents traffic between the OpenShift Container Platform components as a network graph. You can refine the graph by using the filters and display options. You can access the information for cluster, zone, udn, node, namespace, owner, pod, and service.

## Traffic flow tables

The **Traffic flow** tables in the OpenShift Container Platform web console provide a detailed view of raw network flows, offering powerful filtering options and configurable columns for in-depth analysis.

The **Traffic flows** tab in the OpenShift Container Platform web console displays the data of the network flows and the amount of traffic.

# Network Observability CLI

The Network Observability CLI (`oc netobserv`) is a lightweight tool that streams flow and packet data for quick, live insight into networking issues without requiring the full Network Observability Operator installation.

The Network Observability CLI is a flow and packet visualization tool that relies on eBPF agents to stream collected data to an ephemeral collector pod. It requires no persistent storage during the capture. After the run, the output is transferred to your local machine. This enables quick, live insight into packets and flow data without installing the Network Observability Operator.
