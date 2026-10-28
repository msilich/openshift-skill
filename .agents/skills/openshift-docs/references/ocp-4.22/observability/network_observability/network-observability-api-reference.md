<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

The Network Observability Operator provides custom resources for configuring flow collection, defining custom metrics, and managing per-tenant configurations. See the included links to the API specifications for these resources and related documentation.

# Network observability API specifications

Reference documentation for Network Observability custom resources and flow data formats.

## FlowCollector API

The `FlowCollector` resource configures the Network Observability Operator.

- [FlowCollector API for network observability 2.0](../../offline-references/netobserv/2.0/flowcollector-flows-netobserv-io-v1beta2.md)

- [FlowCollector API for network observability 1.12](../../offline-references/netobserv/1.12/flowcollector-flows-netobserv-io-v1beta2.md)

## FlowMetric API

The `FlowMetric` resource creates custom metrics from collected flow logs.

- [FlowMetric API for network observability 2.0](../../offline-references/netobserv/2.0/flowmetric-flows-netobserv-io-v1alpha1.md)

- [FlowMetric API for network observability 1.12](../../offline-references/netobserv/1.12/flowmetric-flows-netobserv-io-v1alpha1.md)

## FlowCollectorSlice API

The `FlowCollectorSlice` resource enables per-tenant flow collection configuration.

- [FlowCollectorSlice API for network observability 2.0](../../offline-references/netobserv/2.0/FlowCollectorSlice.md)

- [FlowCollectorSlice API for network observability 1.12](../../offline-references/netobserv/1.12/FlowCollectorSlice.md)

## Network flows format

The network flows format reference describes the structure and fields of flow data.

- [Network flows format reference for network observability 2.0](../../offline-references/netobserv/2.0/flows-format.md)

- [Network flows format reference for network observability 1.12](../../offline-references/netobserv/1.12/flows-format.md)

## Network Observability CLI usage

The Network Observability CLI (`oc netobserv`) provides feature and filtering parity with the Network Observability Operator. Use command-line arguments to dynamically toggle features and isolate specific cluster network traffic flows.

- [Network Observability CLI usage](../../offline-references/netobserv/cli/netobserv_cli.md)
