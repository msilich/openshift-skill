<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Configure the Network Observability Operator by updating the cluster-wide `FlowCollector` API resource (cluster) to manage component configurations and flow collection settings.

The `FlowCollector` is explicitly created during installation. Since this resource operates cluster-wide, only a single `FlowCollector` is allowed, and it must be named `cluster`. For more information, see the "FlowCollector API reference".

# View the FlowCollector resource

View and modify the `FlowCollector` resource in the OpenShift Container Platform web console through the integrated setup, advanced form, or by editing the YAML directly to configure the Network Observability Operator.

<div>

<div class="title">

Procedure

</div>

1.  In the web console, navigate to **Ecosystem** → **Installed Operators**.

2.  Under the **Provided APIs** heading for the **NetObserv Operator**, select **Flow Collector**.

3.  Select **cluster** then select the **YAML** tab. There, you can modify the `FlowCollector` resource to configure the Network Observability Operator.

</div>

## Example of a FlowCollector resource

Review a comprehensive, annotated example of the `FlowCollector` custom resource that demonstrates configurations for `eBPF` sampling, conversation tracking, Loki integration, and console quick filters.

### Sample `FlowCollector` resource

``` yaml
apiVersion: flows.netobserv.io/v1beta2
kind: FlowCollector
metadata:
  name: cluster
spec:
  namespace: netobserv
  deploymentModel: Service
  networkPolicy:
    enable: true
  agent:
    type: eBPF
    ebpf:
      sampling: 50
      privileged: false
      features: []
  processor:
    addZone: false
    subnetLabels:
      openShiftAutoDetect: true
      customLabels: []
    consumerReplicas: 3
  loki:
    enable: true
    mode: LokiStack
    lokiStack:
      name: loki
      namespace: netobserv-loki
  consolePlugin:
    enable: true
  exporters: []
```

where:

`spec.agent.type`
Must be `eBPF` as eBPF is the only OpenShift Container Platform supported option.

`spec.agent.ebpf.sampling`
Specifies the sampling interval. By default, eBPF sampling is set to `50`, so a packet has a 1 in 50 chance of being sampled. A lower sampling interval value requires more computational, memory, and storage resources. A value of `0` or `1` means all packets are sampled. It is recommended to start with the default value and refine it empirically to determine the optimal setting for your cluster.

`spec.agent.ebpf.privileged`
Specifies if the eBPF agent pods should run as privileged. Running as privileged is required for several features, such as monitoring non-default networks and tracking packet drops. For security, in accordance with the principle of least privilege, it should only be enabled when some of those features are desired. A warning will be displayed if you enabled a feature requiring privileged mode without setting it to true explicitly.

`spec.processor.addZone`
Used to inject cloud availability zones in network flows.

`spec.processor.subnetLabels`
Specifies a list of customized labels to inject in network flows, based on CIDR matching.

`spec.processor.consumerReplicas`
Specifies the number of replicas for the processor pods (flowlogs-pipeline). Refer to the Resource management and performance considerations section for recommendations based on the cluster size.

`spec.loki.mode`
Specifies how to configure the connection to Loki, depending on its installation mode. If you use the install paths described in "Installing the Loki Operator", the mode must be set to `LokiStack`, and `spec.loki.lokiStack` should refer to the installed `LokiStack` resource name and namespace.

`spec.loki.lokistack.namespace`
Specifies the namespace for the `LokiStack` resource. This value must match the `metadata.namespace` defined in the `LokiStack` custom resource. While this example uses `netobserv-loki`, you can use a different namespace for different components.

<div>

<div class="title">

Additional resources

</div>

- [FlowCollector API reference](flowcollector-api.md#network-observability-flowcollector-api-specifications_network_observability)

- [Working with conversation tracking](observing-network-traffic.md#network-observability-working-with-conversations_nw-observe-network-traffic)

</div>

# Configuring the FlowCollector resource with Kafka

Configure the `FlowCollector` resource to use Kafka for high-throughput and low-latency data feeds.

You must have a running Kafka instance and create a Kafka topic in that instance dedicated to OpenShift Container Platform Network Observability. For more information, see [Kafka documentation with AMQ Streams](https://access.redhat.com/documentation/en-us/red_hat_amq/7.7/html/using_amq_streams_on_openshift/using-the-topic-operator-str).

<div>

<div class="title">

Prerequisites

</div>

- You have installed Kafka. Red Hat supports Kafka with AMQ Streams Operator.

</div>

<div>

<div class="title">

Procedure

</div>

1.  In the web console, navigate to **Ecosystem** → **Installed Operators**.

2.  Under the **Provided APIs** heading for the Network Observability Operator, select **Flow Collector**.

3.  Select the cluster and then click the **YAML** tab.

4.  Change the `FlowCollector` resource for OpenShift Container Platform Network Observability Operator to use Kafka, as shown in the following sample YAML:

    <div class="formalpara">

    <div class="title">

    Sample Kafka configuration in `FlowCollector` resource

    </div>

    ``` yaml
    apiVersion: flows.netobserv.io/v1beta2
    kind: FlowCollector
    metadata:
      name: cluster
    spec:
      deploymentModel: Kafka
      kafka:
        address: "kafka-cluster-kafka-bootstrap.netobserv"
        topic: network-flows
        tls:
          enable: false
    ```

    </div>

    where:

    `spec.deploymentModel`
    Specifies the deployment model. Set to `Kafka` instead of `Service` to enable the Kafka deployment model.

    `spec.kafka.address`
    Specifies the Kafka bootstrap server address. You can specify a port if needed, for instance `kafka-cluster-kafka-bootstrap.netobserv:9093` for using TLS on port 9093.

    `spec.kafka.topic`
    Specifies the name of the topic created in Kafka. It should match the name of a topic created in Kafka.

    `spec.kafka.tls`
    Specifies communication encryption. Use this setting to encrypt all communications to and from Kafka with TLS or mTLS. When enabled, the Kafka CA certificate must be available as a ConfigMap or a Secret in both namespaces: the namespace where you deploy the `flowlogs-pipeline` processor component (default: `netobserv`) and the namespace where you deploy the eBPF agents (default: `netobserv-privileged`). Reference the certificate by using `spec.kafka.tls.caCert`. When you use mTLS, make the client secrets available in these namespaces as well. You can generate the secrets by using the Red Hat AMQ Streams User Operator. Reference the secrets by using `spec.kafka.tls.userCert`.

</div>

# Export enriched network flow data

Configure the `FlowCollector` resource to export enriched network flow data simultaneously to Kafka, IPFIX, or an OpenTelemetry endpoint for external consumption by tools like Splunk or Prometheus.

For Kafka or IPFIX, any processor or storage that supports those inputs, such as Splunk, Elasticsearch, or Fluentd, can consume the enriched network flow data.

For OpenTelemetry, network flow data and metrics can be exported to a compatible OpenTelemetry endpoint, such as Red Hat build of OpenTelemetry or Prometheus.

After configuration, network flows data can be sent to an available output. For more information, see "Network flows format reference".

<div>

<div class="title">

Prerequisites

</div>

- Your Kafka, IPFIX, or OpenTelemetry collector endpoints are available from Network Observability `flowlogs-pipeline` pods.

</div>

<div>

<div class="title">

Procedure

</div>

1.  In the web console, navigate to **Ecosystem** → **Installed Operators**.

2.  Under the **Provided APIs** heading for the **NetObserv Operator**, select **Flow Collector**.

3.  Select **cluster** and then select the **YAML** tab.

4.  Edit the `FlowCollector` to configure `spec.exporters` as follows:

    ``` yaml
    apiVersion: flows.netobserv.io/v1beta2
    kind: FlowCollector
    metadata:
      name: cluster
    spec:
      exporters:
      - type: Kafka
          kafka:
            address: "kafka-cluster-kafka-bootstrap.netobserv"
            topic: netobserv-flows-export
            tls:
              enable: false
      - type: IPFIX
          ipfix:
            targetHost: "ipfix-collector.ipfix.svc.cluster.local"
            targetPort: 4739
            transport: tcp
     -  type: OpenTelemetry
          openTelemetry:
            targetHost: my-otelcol-collector-headless.otlp.svc
            targetPort: 4317
            type: grpc
            logs:
              enable: true
            metrics:
              enable: true
              prefix: netobserv
              pushTimeInterval: 20s
              expiryTime: 2m
       #    fieldsMapping:
       #      input: SrcAddr
       #      output: source.address
    ```

    where:

    `spec.exporters.type`
    Specifies the export type. You can export flows to `IPFIX`, `OpenTelemetry`, and `Kafka` individually or concurrently.

    `spec.exporters.kafka.topic`
    Specifies the Kafka topic where the Network Observability Operator exports all flows.

    `spec.exporters.kafka.tls.enable`
    Specifies whether to encrypt communications to and from Kafka with SSL/TLS or mTLS. When enabled, the Kafka CA certificate must be available as a `ConfigMap` or a `Secret` in the namespace where the `flowlogs-pipeline` processor component is deployed (default: `netobserv`). Reference the certificate with `spec.exporters.tls.caCert`. For mTLS, client secrets must also be available in these namespaces and referenced with `spec.exporters.tls.userCert`.

    `spec.exporters.ipfix.transport`
    Specifies the transport protocol. The default value is `tcp`, but you can also specify `udp`.

    `spec.exporters.openTelemetry.type`
    Specifies the OpenTelemetry connection protocol. The available options are `http` and `grpc`.

    `spec.exporters.openTelemetry.logs`
    Specifies the OpenTelemetry configuration for exporting logs, which are identical to the logs created for Loki.

    `spec.exporters.openTelemetry.metrics`
    Specifies the OpenTelemetry configuration for exporting metrics, which are identical to the metrics created for Prometheus. These are defined in the `spec.processor.metrics.includeList` parameter of the `FlowCollector` resource or via the `FlowMetrics` resource.

    `spec.exporters.openTelemetry.metrics.pushTimeInterval`
    Specifies the time interval for sending metrics to the OpenTelemetry collector.

    `spec.exporters.openTelemetry.fieldsMapping`
    Specifies an optional mapping to customize the OpenTelemetry format output. Network Observability flow formats are automatically renamed to an OpenTelemetry-compliant format, but this parameter allows for custom overrides. For example in the YAML sample, `SrcAddr` is the Network Observability input field, and it is being renamed to `source.address` in OpenTelemetry output. You can see both Network Observability and OpenTelemetry formats in the "Network flows format reference".

</div>

<div>

<div class="title">

Additional resources

</div>

- [Network flows format reference](json-flows-format-reference.md#network-observability-flows-format_json_reference)

</div>

# Updating the FlowCollector resource

As an alternative to using the web console, use the `oc patch` command with the `flowcollector` custom resource to quickly update specific specifications, such as eBPF sampling

<div>

<div class="title">

Procedure

</div>

1.  Run the following command to patch the `flowcollector` CR and update the `spec.agent.ebpf.sampling` value:

    ``` terminal
    $ oc patch flowcollector cluster --type=json -p "[{"op": "replace", "path": "/spec/agent/ebpf/sampling", "value": <new value>}] -n netobserv"
    ```

</div>

# Filter network flows at ingestion

Create filters to reduce the number of generated network flows. Filtering network flows can reduce the resource usage of the network observability components.

You can configure two kinds of filters:

- eBPF agent filters

- Flowlogs-pipeline filters

## eBPF agent filters

eBPF agent filters maximize performance because they take effect at the earliest stage of the network flows collection process.

To configure eBPF agent filters with the Network Observability Operator, see "Filtering eBPF flow data using multiple rules".

## Flowlogs-pipeline filters

Flowlogs-pipeline filters provide greater control over traffic selection because they take effect later in the network flows collection process. They are primarily used to improve data storage.

Flowlogs-pipeline filters use a simple query language to filter network flow, as shown in the following example:

``` terminal
(srcnamespace="netobserv" OR (srcnamespace="ingress" AND dstnamespace="netobserv")) AND srckind!="service"
```

The query language uses the following syntax:

<table>
<caption>Query language syntax</caption>
<colgroup>
<col style="width: 25%" />
<col style="width: 75%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Category</th>
<th style="text-align: left;">Operators</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>Logical boolean operators (not case-sensitive)</p></td>
<td style="text-align: left;"><p><code>and</code>, <code>or</code></p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Comparison operators</p></td>
<td style="text-align: left;"><p><code>=</code> (equals),</p>
<p><code>!=</code> (not equals),</p>
<p><code>=~</code> (matches regexp),</p>
<p><code>!~</code> (not matches regexp),</p>
<p><code>&lt;</code> / <code>&lt;=</code> (less than or equal to),</p>
<p><code>&gt;</code> / <code>&gt;=</code> (greater than or equal to)</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Unary operations</p></td>
<td style="text-align: left;"><p><code>with(field)</code> (field is present),</p>
<p><code>without(field)</code> (field is absent)</p></td>
</tr>
</tbody>
</table>

You can configure flowlogs-pipeline filters in the `spec.processor.filters` section of the `FlowCollector` resource. For example:

<div class="formalpara">

<div class="title">

Example YAML Flowlogs-pipeline filter

</div>

``` yaml
apiVersion: flows.netobserv.io/v1beta2
kind: FlowCollector
metadata:
  name: cluster
spec:
  namespace: netobserv
  agent:
  processor:
    filters:
      - query: |
          (SrcK8S_Namespace="netobserv" OR (SrcK8S_Namespace="openshift-ingress" AND DstK8S_Namespace="netobserv"))
        outputTarget: Loki
        sampling: 10
```

</div>

where:

`spec.processor.filters.outputTarget`
Specifies the output destination for matching flows, such as `Loki`, `Prometheus`, or an external system. If you omit this parameter, the system sends the flows to all configured outputs.

`spec.processor.filters.sampling`
Specifies an optional sampling interval to limit the number of matching flows stored or exported. For example, a value of `10` means there is a 1 in 10 chance that a flow is kept.

<div>

<div class="title">

Additional resources

</div>

- [Filtering eBPF flow data using multiple rules](observing-network-traffic.md#network-observability-filtering-ebpf-rule_nw-observe-network-traffic)

</div>

# Configuring quick filters

Use the list of available source, destination, and universal filter keys to modify quick filters within the `FlowCollector` resource.

Exact matches are possible using double-quotes around values. Otherwise, partial matches are used for textual values. The bang (!) character, placed at the end of a key, means negation. See the sample `FlowCollector` resource for more context about modifying the YAML.

> [!NOTE]
> The filter matching types "all of" or "any of" is a UI setting that the users can modify from the query options. It is not part of this resource configuration.

Here is a list of all available filter keys:

| Universal\* | Source | Destination | Description |
|----|----|----|----|
| namespace | `src_namespace` | `dst_namespace` | Filter traffic related to a specific namespace. |
| name | `src_name` | `dst_name` | Filter traffic related to a given leaf resource name, such as a specific pod, service, or node (for host-network traffic). |
| kind | `src_kind` | `dst_kind` | Filter traffic related to a given resource kind. The resource kinds include the leaf resource (Pod, Service or Node), or the owner resource (Deployment and StatefulSet). |
| owner_name | `src_owner_name` | `dst_owner_name` | Filter traffic related to a given resource owner; that is, a workload or a set of pods. For example, it can be a Deployment name, a StatefulSet name, etc. |
| resource | `src_resource` | `dst_resource` | Filter traffic related to a specific resource that is denoted by its canonical name, that identifies it uniquely. The canonical notation is `kind.namespace.name` for namespaced kinds, or `node.name` for nodes. For example, `Deployment.my-namespace.my-web-server`. |
| address | `src_address` | `dst_address` | Filter traffic related to an IP address. IPv4 and IPv6 are supported. CIDR ranges are also supported. |
| mac | `src_mac` | `dst_mac` | Filter traffic related to a MAC address. |
| port | `src_port` | `dst_port` | Filter traffic related to a specific port. |
| host_address | `src_host_address` | `dst_host_address` | Filter traffic related to the host IP address where the pods are running. |
| protocol | N/A | N/A | Filter traffic related to a protocol, such as TCP or UDP. |

Filter keys

- Universal keys filter for any of source or destination. For example, filtering `name: 'my-pod'` means all traffic from `my-pod` and all traffic to `my-pod`, regardless of the matching type used, whether **Match all** or **Match any**.

# Resource management and performance considerations

Review the key configuration settings, including eBPF sampling, feature enablement, and resource limits, necessary to manage performance criteria and optimize resource consumption for network observability.

The amount of resources required by network observability depends on the size of your cluster and your requirements for the cluster to ingest and store observability data. To manage resources and set performance criteria for your cluster, consider configuring the following settings. Configuring these settings might meet your optimal setup and observability needs.

The following settings can help you manage resources and performance from the outset:

eBPF Sampling
You can set the Sampling specification, `spec.agent.ebpf.sampling`, to manage resources. By default, eBPF sampling is set to `50`, so a flow has a 1 in 50 chance of being sampled. A lower sampling interval value requires more computational, memory, and storage resources. A value of `0` or `1` means all flows are sampled. It is recommended to start with the default value and refine it empirically to determine the optimal setting for your cluster.

eBPF features
The more features that are enabled, the more CPU and memory are impacted. See "Observing the network traffic" for a complete list of these features.

Without Loki
You can reduce the amount of resources that network observability requires by not using Loki and instead relying on Prometheus. For example, when network observability is configured without Loki, the total savings of memory usage are in the 20-65% range and CPU utilization is lower by 10-30%, depending upon the sampling interval value. See "Network observability without Loki" for more information.

Restricting or excluding interfaces
Reduce the overall observed traffic by setting the values for `spec.agent.ebpf.interfaces` and `spec.agent.ebpf.excludeInterfaces`. By default, the agent fetches all the interfaces in the system, except the ones listed in `excludeInterfaces` and `lo` (local interface). Note that the interface names might vary according to the Container Network Interface (CNI) used.

Performance fine-tuning
The following settings can be used to fine-tune performance after the Network Observability has been running for a while:

- **Resource requirements and limits**: Adapt the resource requirements and limits to the load and memory usage you expect on your cluster by using the `spec.agent.ebpf.resources` and `spec.processor.resources` specifications. The default limits of 800MB might be sufficient for most medium-sized clusters.

- **Cache max flows timeout**: Control how often flows are reported by the agents by using the eBPF agent’s `spec.agent.ebpf.cacheMaxFlows` and `spec.agent.ebpf.cacheActiveTimeout` specifications. A larger value results in less traffic being generated by the agents, which correlates with a lower CPU load. However, a larger value leads to a slightly higher memory consumption, and might generate more latency in the flow collection.

## Resource considerations

The Network Observability Operator configuration can be adjusted based on the cluster workload size. Use the following baseline examples to determine the appropriate resource limits and configuration settings for the environment.

The examples outlined in the table demonstrate scenarios that are tailored to specific workloads. Consider each example only as a baseline from which adjustments can be made to accommodate your workload needs.

The test beds used for these recommendations are:

- Extra small: 10-node cluster, 4 vCPUs and 16 GiB memory per worker, `LokiStack` size `1x.extra-small`, tested on AWS M6i instances.

- Small: 25-node cluster, 16 vCPUs and 64 GiB memory per worker, `LokiStack` size `1x.small`, tested on AWS M6i instances.

- Large: 250-node cluster, 16 vCPUs and 64 GiB memory per worker, `LokiStack` size `1x.medium`, tested on AWS M6i instances. In addition to the worker and controller nodes, three infrastructure nodes (size `M6i.12xlarge`) and one workload node (size `M6i.8xlarge`) were tested.

| Criterion | Extra small (10 nodes) | Small (25 nodes) | Large (250 nodes) |
|----|----|----|----|
| **Operator memory limit: `Subscription` `spec.config.resources`** | `400Mi` (default) | `400Mi` (default) | `400Mi` (default) |
| **eBPF agent sampling interval: `FlowCollector` `spec.agent.ebpf.sampling`** | `50` (default) | `50` (default) | `50` (default) |
| **eBPF agent memory limit: `FlowCollector` `spec.agent.ebpf.resources`** | `800Mi` (default) | `800Mi` (default) | `1600Mi` |
| **eBPF agent cache size: `FlowCollector` `spec.agent.ebpf.cacheMaxSize`** | `50,000` | `120,000` (default) | `120,000` (default) |
| **Processor memory limit: `FlowCollector` `spec.processor.resources`** | `800Mi` (default) | `800Mi` (default) | `800Mi` (default) |
| **Processor replicas: `FlowCollector` `spec.processor.consumerReplicas`** | `3` (default) | `6` | `18` |
| **Deployment model: `FlowCollector` `spec.deploymentModel`** | `Service` (default) | `Kafka` | `Kafka` |
| **Kafka partitions: Kafka installation** | N/A | `48` | `48` |
| **Kafka brokers: Kafka installation** | N/A | `3` (default) | `3` (default) |

Resource recommendations for cluster sizes {#network-observability-resource-recommendations-table_network_observability}

## Total average memory and CPU usage

Review the table detailing the total average CPU and memory usage for network observability components under two distinct traffic scenarios (`Test 1` and `Test 2`) at different eBPF sampling values.

The following table outlines averages of total resource usage for clusters with a sampling value of `1` and `50` for two different tests: `Test 1` and `Test 2`. The tests differ in the following ways:

- `Test 1` takes into account high ingress traffic volume in addition to the total number of namespace, pods and services in an OpenShift Container Platform cluster, places load on the eBPF agent, and represents use cases with a high number of workloads for a given cluster size. For example, `Test 1` consists of 76 Namespaces, 5153 Pods, and 2305 Services with a network traffic scale of ~350 MB/s.

- `Test 2` takes into account high ingress traffic volume in addition to the total number of namespace, pods and services in an OpenShift Container Platform cluster and represents use cases with a high number of workloads for a given cluster size. For example, `Test 2` consists of 553 Namespaces, 6998 Pods, and 2508 Services with a network traffic scale of ~950 MB/s.

Since different types of cluster use cases are exemplified in the different tests, the numbers in this table do not scale linearly when compared side-by-side. Instead, they are intended to be used as a benchmark for evaluating your personal cluster usage. The examples outlined in the table demonstrate scenarios that are tailored to specific workloads. Consider each example only as a baseline from which adjustments can be made to accommodate your workload needs.

> [!NOTE]
> Metrics exported to Prometheus can impact the resource usage. Cardinality values for the metrics can help determine how much resources are impacted. For more information, see "Network Flows format" in the Additional resources section.

| Sampling value | Resources used | Test 1 (25 nodes) | Test 2 (250 nodes) |
|----|----|----|----|
| **Sampling = 50** | Total NetObserv CPU Usage | 1.35 | 5.39 |
| Total NetObserv RSS (Memory) Usage | 16 GB | 63 GB |  |
| **Sampling = 1** | Total NetObserv CPU Usage | 1.82 | 11.99 |
| Total NetObserv RSS (Memory) Usage | 22 GB | 87 GB |  |

Total average resource usage

Summary: This table shows average total resource usage of Network Observability, which includes Agents, FLP, Kafka, and Loki with all features enabled. For details about what features are enabled, see the features covered in "Observing the network traffic", which comprises all the features that are enabled for this testing.

<div>

<div class="title">

Additional resources

</div>

- [Observing the network traffic from the traffic flows view](observing-network-traffic.md#network-observability-trafficflow_nw-observe-network-traffic)

- [Network observability without Loki](installing-operators.md#network-observability-without-loki_network_observability)

- [Network Flows format reference](json-flows-format-reference.md#network-observability-flows-format_json_reference)

</div>
