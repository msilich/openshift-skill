<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Customize network policies and security hardening measures for network observability components. By default, TLS encryption and network policies are automatically configured to secure traffic between components.

# Network observability security architecture

Understanding how network observability components communicate helps you configure appropriate network policies and security hardening measures. Components communicate across different namespaces to collect, process, and display network flow data.

## Components and security boundaries

The Network Observability Operator consists of the following components:

Network Observability Operator
Runs in the `openshift-netobserv-operator` namespace. This component manages the deployment and configuration of all other network observability components. It requires egress access to the API server and ingress access for webhooks and metrics.

eBPF agents
Run as a `DaemonSet` on each node to capture network flow data from the Linux kernel.

FlowLogs Pipeline (FLP)
Runs in the `netobserv` namespace (configurable). This component receives flow data from the eBPF agents, enriches it with Kubernetes metadata, and forwards it to storage backends such as Loki or exports it to external systems.

Console plugin
Runs in the `netobserv` namespace and provides the web console interface for viewing network flow data. It requires access to query the storage backend and serves content to the OpenShift web console.

Static console plugin
Runs in the `openshift-netobserv-operator` namespace alongside the Operator. This static plugin component serves static assets and requires ingress access from the OpenShift web console.

## Network traffic flows

Understanding the network traffic flows between components helps you configure minimal network policies:

Agent to FlowLogs Pipeline
If not configured with Kafka, eBPF agents send flow data to the FLP over gRPC. This connection can be secured with TLS or mTLS. The default configuration uses automatic TLS with OpenShift service CA annotations.

Agent to Kafka
If configured with Kafka, eBPF agents send flow data to Kafka. This connection can be secured with TLS, mTLS, or Simple Authentication and Security Layer (SASL).

FlowLogs Pipeline to Loki
If using Loki as the storage backend, FLP sends enriched flow data to Loki over HTTP or HTTPS. When using the Loki Operator, HTTPS is enforced.

FlowLogs Pipeline to Kafka
If using Kafka as a buffer, FLP pulls flow data from Kafka brokers. This connection can be secured with TLS, mTLS, or SASL.

FlowLogs Pipeline to API Server
FLP watches Pods, Nodes, Services and other cluster data from the API Server to enrich flow data. This connection uses TLS.

Console plugin to Loki
The console plugin queries Loki directly to retrieve and display flow data in the web console. When using the Loki Operator, HTTPS is enforced.

Console plugin to OpenShift web console
The OpenShift web console loads the network observability plugin to display the network flow visualization interface.

Network Observability Operator to API server
The Network Observability Operator communicates with the Kubernetes API server to manage resources, watch for configuration changes, and perform reconciliation.

All components to DNS
All components require access to DNS for service discovery and name resolution.

## Security model

The network observability security model uses the following mechanisms:

Network policies
Control ingress and egress traffic for components. The Network Observability Operator can deploy network policies automatically by using the `FlowCollector` custom resource, or you can create custom policies manually.

Automatic network policy deployment
The Network Observability Operator automatically deploys network policies at runtime. This is controlled by the `OPERATOR_NETWORK_POLICY` environment variable in the Cluster Service Version (CSV), which defaults to `true`. The StaticReconciler deploys and owns the following policies in the `openshift-netobserv-operator` namespace:

- Operator network policy with egress rules for DNS, API server access, and ingress rules for webhooks and metrics endpoints

- Static plugin network policy with egress rules for DNS and ingress rules to allow the OpenShift web console to access the static plugin

Once a `FlowCollector` resource is installed, the NetPol Controller deploys network policies for the two operand namespaces (`netobserv` and `netobserv-privileged` by default). This is controlled by the `spec.networkPolicy.enable` setting in `FlowCollector`. These policies are automatically restored if manually deleted.

Transport Layer Security (TLS)
Secure communications between eBPF agents and the FlowLogs Pipeline by using TLS or mutual TLS. The default configuration uses automatic TLS with zero configuration required.

Pod Security Standards
Network observability components follow OpenShift Container Platform pod security standards and use Security Context Constraints (SCCs) appropriately.

Service accounts
Each component uses dedicated service accounts with minimal required permissions following the principle of least privilege.

## Network policy integration considerations

If you have installed Loki, Kafka, or any exporter in a different namespace that also has a network policy, you must ensure that the network observability components can communicate with them. Consider the following integration points when configuring network policies:

- Connection to Loki (as defined in the `FlowCollector` CR `spec.loki` parameter)

- Connection to Kafka (as defined in the `FlowCollector` CR `spec.kafka` parameter)

- Connection to any exporter (as defined in the `FlowCollector` CR `spec.exporters` parameter)

- Connection to external object storage (as defined in your `LokiStack` related `Secret`) when using Loki

# Configure network policy by using the FlowCollector custom resource

Configure ingress and egress network policies to control pod traffic for network observability components. Network policies enhance security, reduce noise, support compliance, and improve visibility into network communication.

You can configure the `FlowCollector` custom resource (CR) to deploy network policies for network observability. By default, network policy management is enabled.

<div>

<div class="title">

Prerequisites

</div>

- You have installed the Network Observability Operator.

- You have cluster administrator permissions.

</div>

<div>

<div class="title">

Procedure

</div>

1.  In the web console, go to **Ecosystem** → **Installed Operators** page.

2.  Under the **Provided APIs** heading for **Network Observability**, select **Flow Collector**.

3.  Select **cluster** then select the **YAML** tab.

4.  Configure the `FlowCollector` CR. A sample configuration is as follows:

    <div id="network-observability-flowcollector-configuring-network-policy_network_observability" class="formalpara">

    <div class="title">

    Example `FlowCollector` CR for network policy

    </div>

    ``` yaml
    apiVersion: flows.netobserv.io/v1beta2
    kind: FlowCollector
    metadata:
      name: cluster
    spec:
      namespace: netobserv
      networkPolicy:
        enable: true
        additionalNamespaces: ["my-kafka-exporter"]
    # ...
    ```

    </div>

    where:

    `spec.networkPolicy.enable`
    Specifies whether to enable network policy management. The default value is `true`.

    `spec.networkPolicy.additionalNamespaces`
    Specifies additional namespaces to include in the network policy. Use this parameter to add namespaces where flows are exported. For example, if you configured `spec.exporters` to a Kafka broker in a namespace such as `my-kafka-exporter`, you should include that namespace in the list.

</div>

# Configure secure communications between the agent and the FlowLogs Pipeline

Configure Transport Layer Security (TLS) or mutual TLS (mTLS) to secure communications between eBPF agents and the FlowLogs Pipeline.

By default, communications are secured automatically by using OpenShift service Certificate Authority (CA) annotations with zero configuration required.

The following example demonstrates how to provide your own certificates rather than relying on automatic TLS configuration. This configuration applies only when the deployment model is set to `Service` mode.

<div>

<div class="title">

Prerequisites

</div>

- You have installed the Network Observability Operator.

- You have cluster administrator permissions.

</div>

<div>

<div class="title">

Procedure

</div>

1.  In the web console, go to **Ecosystem** → **Installed Operators** page.

2.  Under the **Provided APIs** heading for **Network Observability**, select **Flow Collector**.

3.  Select **cluster** then select the **YAML** tab.

4.  Configure the `FlowCollector` CR for agent TLS settings. A sample configuration is as follows:

    <div id="network-observability-flowcollector-agent-tls_network_observability" class="formalpara">

    <div class="title">

    Example `FlowCollector` CR for provided certificates mode

    </div>

    ``` yaml
    apiVersion: flows.netobserv.io/v1beta2
    kind: FlowCollector
    metadata:
      name: cluster
    spec:
      processor:
        service:
          tlsType: Provided
          providedCertificates:
            caFile:
              type: configmap
              name: my-ca-configmap
              file: service-ca.crt
            serverCert:
              type: secret
              name: my-server-cert-secret
              certFile: tls.crt
              certKey: tls.key
            clientCert: {}
    # ...
    ```

    </div>

    where:

    `spec.processor.service.tlsType`
    Specifies the TLS configuration mode:

    - `Auto` (default): Communications are automatically secured by using OpenShift service CA annotations. This provides TLS encryption with zero configuration.

    - `Disabled`: TLS is disabled. Communications between agents and FLP are not encrypted. Use this option only in development or testing environments.

    - `Provided`: You provide your own certificates for TLS or mutual TLS. This option requires additional configuration by using the `caFile`, `serverCert`, and `clientCert` fields. When `clientCert` is omitted, TLS is configured rather than mTLS.

    `spec.processor.service.providedCertificates.caFile.type`
    Specifies how the CA certificate is provided. Valid values are `configmap` or `secret`.

    `spec.processor.service.providedCertificates.caFile.name`
    Name of the `configmap` or `secret`.

    `spec.processor.service.providedCertificates.caFile.file`
    Name of the CA file within the `configmap` or `secret`.

    `spec.processor.service.providedCertificates.serverCert.type`
    Specifies how the server (FLP) certificate is provided for both TLS and mutual TLS. Valid values are `configmap` or `secret`.

    `spec.processor.service.providedCertificates.serverCert.name`
    Name of the `configmap` or `secret`.

    `spec.processor.service.providedCertificates.serverCert.certFile`
    Name of the server certificate file within the `configmap` or `secret`.

    `spec.processor.service.providedCertificates.serverCert.certKey`
    Name of the server certificate key file within the `configmap` or `secret`.

    `spec.processor.service.providedCertificates.clientCert.type`
    Specifies how the client (eBPF Agent) certificate is provided when using mutual TLS. Valid values are `configmap` or `secret`.

    `spec.processor.service.providedCertificates.clientCert.name`
    Name of the `configmap` or `secret`.

    `spec.processor.service.providedCertificates.clientCert.certFile`
    Name of the client certificate file within the `configmap` or `secret`.

    `spec.processor.service.providedCertificates.clientCert.certKey`
    Name of the client certificate key file within the `configmap` or `secret`.

</div>

<div>

<div class="title">

Verification

</div>

1.  After configuring TLS, verify that the agents are communicating securely with FLP by running the following command:

    ``` terminal
    $ oc logs -n netobserv-privileged ds/netobserv-ebpf-agent | grep -i "starting grpc"
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    time="2026-09-30T07:19:14Z" level=info msg="Starting GRPC client with TLS" component=grpc.Client
    ```

    </div>

    > [!NOTE]
    > Using the `Auto` mode provides the best balance of security and ease of use for most deployments. Consider using `Provided` mode only if you have specific certificate requirements or are integrating with an existing Public Key Infrastructure (PKI).
    >
    > When using mutual TLS (mTLS) with the `Provided` mode, both the CA certificate and user certificate must be configured. The FLP verifies the agent certificate, and the agent verifies the FLP certificate.

</div>

# Example NetworkPolicy manifests for network observability

You can use these example NetworkPolicy manifests as a starting point for securing network observability components. Customize these examples based on your specific environment and security requirements.

> [!NOTE]
> These examples provide a foundation for securing network observability. You might need to add additional egress rules for Kafka exporters, external storage, or other integrations based on your specific deployment.
>
> For security best practices, avoid using allow-all CIDR rules such as `0.0.0.0/0` or `::/0` in network policies. Instead, use specific namespace selectors and pod selectors to limit traffic to only required destinations.

## Default deny policy for the netobserv namespace

This policy sets a default deny for all ingress and egress traffic in the `netobserv` namespace. Apply this first, then add specific `allow` policies for required traffic.

``` yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: default-deny
  namespace: netobserv
spec:
  podSelector: {}
  policyTypes:
  - Ingress
  - Egress
```

## Allow DNS for all pods

This policy allows all pods in the `netobserv` namespace to access DNS for name resolution.

``` yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: allow-to-dns
  namespace: netobserv
spec:
  podSelector: {}
  egress:
  - to:
    - namespaceSelector:
        matchLabels:
          kubernetes.io/metadata.name: openshift-dns
    ports:
    - protocol: TCP
      port: 5353
    - protocol: UDP
      port: 5353
  policyTypes:
  - Egress
```

## Allow FlowLogs pipeline to access Loki

This policy allows the FlowLogs Pipeline to send flow data to Loki.

``` yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: allow-flp-to-loki
  namespace: netobserv
spec:
  podSelector:
    matchLabels:
      app: flowlogs-pipeline
  egress:
  - to:
    - namespaceSelector:
        matchLabels:
          kubernetes.io/metadata.name: openshift-netobserv
    ports:
    - protocol: TCP
      port: 3100
  policyTypes:
  - Egress
```

where:

`kubernetes.io/metadata.name: openshift-netobserv`
Replace with the namespace where Loki is deployed in your environment.

`port: 3100`
Adjust the port number if Loki uses a different port.

## Allow console plugin to query Loki

This policy allows the console plugin to query Loki for displaying flow data in the web console.

``` yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: allow-plugin-to-loki
  namespace: netobserv
spec:
  podSelector:
    matchLabels:
      app: netobserv-plugin
  egress:
  - to:
    - namespaceSelector:
        matchLabels:
          kubernetes.io/metadata.name: openshift-netobserv
    ports:
    - protocol: TCP
      port: 3100
  policyTypes:
  - Egress
```

where:

`kubernetes.io/metadata.name: openshift-netobserv`
Replace with the namespace where Loki is deployed in your environment.

`port: 3100`
Adjust the port number if Loki uses a different port.

## Allow console plugin ingress from OpenShift web console

This policy allows the OpenShift Console to access the Network Observability console plugin.

``` yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: allow-console-to-plugin
  namespace: netobserv
spec:
  podSelector:
    matchLabels:
      app: netobserv-plugin
  ingress:
  - from:
    - namespaceSelector:
        matchLabels:
          kubernetes.io/metadata.name: openshift-console
    ports:
    - protocol: TCP
      port: 9001
  policyTypes:
  - Ingress
```

## Allow metrics scraping from monitoring

This policy allows Prometheus in the `openshift-monitoring` namespace to scrape metrics from network observability components.

``` yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: allow-metrics-scraping
  namespace: netobserv
spec:
  podSelector:
    matchLabels:
      app: flowlogs-pipeline
  ingress:
  - from:
    - namespaceSelector:
        matchLabels:
          kubernetes.io/metadata.name: openshift-monitoring
    ports:
    - protocol: TCP
      port: 9102
  policyTypes:
  - Ingress
```

where:

`app: flowlogs-pipeline`
Adjust the label selector to match your component. Apply similar policies for other components that expose metrics.

`port: 9102`
Adjust the port number based on your metrics endpoint configuration.

## Allow agent to FlowLogs pipeline communication

This policy allows eBPF agents running on nodes to send flow data to the FlowLogs Pipeline.

``` yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: allow-agents-to-flp
  namespace: netobserv
spec:
  podSelector:
    matchLabels:
      app: flowlogs-pipeline
  ingress:
  - from:
    - namespaceSelector:
        matchLabels:
          policy-group.network.openshift.io/host-network: ""
    ports:
    - protocol: TCP
      port: 2055
  policyTypes:
  - Ingress
```

where:

`policy-group.network.openshift.io/host-network: ""`
This namespace selector allows traffic from host-networked pods, which includes the eBPF agents.

`port: 2055`
Adjust the port number based on your FlowCollector configuration for agent-to-FLP communication.

## Complete example for standard deployment

This example combines multiple policies for a standard Network Observability Operator deployment with Loki storage.

``` yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: netobserv-policies
  namespace: netobserv
spec:
  podSelector: {}
  policyTypes:
  - Ingress
  - Egress
  egress:
  # Allow DNS
  - to:
    - namespaceSelector:
        matchLabels:
          kubernetes.io/metadata.name: openshift-dns
    ports:
    - protocol: TCP
      port: 5353
    - protocol: UDP
      port: 5353
  # Allow access to Loki
  - to:
    - namespaceSelector:
        matchLabels:
          kubernetes.io/metadata.name: openshift-netobserv
    ports:
    - protocol: TCP
      port: 3100
  ingress:
  # Allow from OpenShift Console
  - from:
    - namespaceSelector:
        matchLabels:
          kubernetes.io/metadata.name: openshift-console
    ports:
    - protocol: TCP
      port: 9001
  # Allow from monitoring
  - from:
    - namespaceSelector:
        matchLabels:
          kubernetes.io/metadata.name: openshift-monitoring
    ports:
    - protocol: TCP
      port: 9102
  # Allow from agents
  - from:
    - namespaceSelector:
        matchLabels:
          policy-group.network.openshift.io/host-network: ""
    ports:
    - protocol: TCP
      port: 2055
```

## Operator network policy

This example shows the automatically deployed network policy for the Network Observability Operator in the `openshift-netobserv-operator` namespace. This policy is deployed by the StaticReconciler when `OPERATOR_NETWORK_POLICY` is set to `true` in the CSV.

``` yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: netobserv-operator
  namespace: openshift-netobserv-operator
spec:
  podSelector:
    matchLabels:
      app: netobserv-operator
  policyTypes:
  - Ingress
  - Egress
  egress:
  # Allow DNS
  - to:
    - namespaceSelector:
        matchLabels:
          kubernetes.io/metadata.name: openshift-dns
    ports:
    - protocol: TCP
      port: 5353
    - protocol: UDP
      port: 5353
  # Allow API server access
  - to:
    - namespaceSelector:
        matchLabels:
          kubernetes.io/metadata.name: default
    ports:
    - protocol: TCP
      port: 6443
  ingress:
  # Allow webhooks
  - from:
    - namespaceSelector: {}
    ports:
    - protocol: TCP
      port: 9443
  # Allow metrics scraping
  - from:
    - namespaceSelector:
        matchLabels:
          kubernetes.io/metadata.name: openshift-monitoring
    ports:
    - protocol: TCP
      port: 8443
```

where:

`app: netobserv-operator`
Pod selector that targets the Network Observability Operator pods.

`port: 6443`
API server port for Kubernetes API access.

`port: 9443`
Webhook server port for admission webhooks.

`port: 8443`
Metrics endpoint port for Prometheus scraping.

## Static plugin network policy

This example shows the automatically deployed network policy for the static console plugin in the `openshift-netobserv-operator` namespace. This policy is deployed by the StaticReconciler when `OPERATOR_NETWORK_POLICY` is set to `true` in the CSV.

``` yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: netobserv-plugin-static
  namespace: openshift-netobserv-operator
spec:
  podSelector:
    matchLabels:
      app: netobserv-plugin-static
  policyTypes:
  - Ingress
  - Egress
  egress:
  # Allow DNS
  - to:
    - namespaceSelector:
        matchLabels:
          kubernetes.io/metadata.name: openshift-dns
    ports:
    - protocol: TCP
      port: 5353
    - protocol: UDP
      port: 5353
  ingress:
  # Allow OpenShift Console to access static plugin
  - from:
    - namespaceSelector:
        matchLabels:
          kubernetes.io/metadata.name: openshift-console
    ports:
    - protocol: TCP
      port: 9443
```

where:

`app: netobserv-plugin-static`
Pod selector that targets the static console plugin pods.

`port: 9443`
Static plugin server port for serving static assets to the OpenShift web console.

<div>

<div class="title">

Additional resources

</div>

- [Creating a network policy using the CLI](../../networking/network_security/network_policy/creating-network-policy.md#nw-networkpolicy-object_creating-network-policy)

</div>
