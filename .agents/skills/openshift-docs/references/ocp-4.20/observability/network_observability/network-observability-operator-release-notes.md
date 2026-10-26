<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Review new features, enhancements, fixed issues, and known issues for the Network Observability Operator. These release notes provide information to help you understand changes and security advisories in the latest Operator release.

The Network Observability Operator enables administrators to observe and analyze network traffic flows for OpenShift Container Platform clusters.

These release notes track the development of the Network Observability Operator in the OpenShift Container Platform. It follows a rolling-stream release methodology, and customers are expected to continuously upgrade to new versions as they become available on the cluster.

Some referenced tickets are not linked. This means that the ticket is not accessible without Red Hat credentials.

# Network Observability Operator 2.0 advisory

Review the advisory for Network Observability Operator 2.0 release.

- [RHEA-2026:86986 Network Observability Operator 2.0](https://access.redhat.com/errata/RHEA-2026:86986)

# Network Observability Operator 2.0 new features and enhancements

The Network Observability Operator 2.0 release enhances cluster network visibility, security posture, and flow processing efficiency through preconfigured console views and optimized health monitoring tools.

Network policy and security hardening
The Network Observability Operator implements network policies and security hardening measures to improve cluster security posture. Network policies control traffic flow to and from Operator components, and the `openshift-netobserv-operator` namespace is now protected with appropriate network policy rules.

Security improvements:

- Enhanced security: Restrict network access to Operator components by using OpenShift network policies.

- Compliance alignment: Meet security requirements for restricted network environments and regulated workloads.

- Defense in-depth: Implement network-level access controls that complement existing security measures.

TLS security monitoring alerts
The Network Observability Operator provides preconfigured Prometheus alerts for Transport Layer Security (TLS) security compliance. Automated alerts notify administrators when workloads use deprecated TLS versions or non-compliant cryptographic protocols.

Alert capabilities:

- Automated security detection: Receive alerts when workloads use TLS versions earlier than 1.2, which are considered insecure.

- Post-quantum cryptography compliance: Identify workloads with cryptographic configurations that do not meet post-quantum cryptography standards.

- Proactive security remediation: Address security vulnerabilities before they impact production environments through early notification.

- Compliance enforcement: Support security auditing and regulatory compliance requirements with automated TLS version monitoring.

Network health monitoring improvements
The **Network Health** page in the Network Observability Operator web console plugin is enhanced with additional features and improvements for cluster and application administrators. Enhanced health monitoring capabilities provide better visibility into network reliability and performance.

New capabilities:

- Improved health score visualization: View network health scores with enhanced graphical displays that provide better context.

- Health rule creation wizard: Create alert rules and recording rules by using an intuitive wizard interface.

- Historical health tracking: Monitor network health trends over time to identify degradation patterns.

- Enhanced filtering and search: Quickly identify and troubleshoot network issues with improved filtering capabilities.

Preconfigured feature views in the web console
The Network Observability Operator web console plugin provides preconfigured feature views to streamline access to common monitoring tasks. Users can navigate directly to specialized views without manually configuring columns, panels, or metric selections.

Key benefits:

- Faster navigation: Access feature-specific views with preconfigured settings to reduce manual configuration steps.

- Improved usability: Reduce the number of clicks required to view relevant network flow data for specific use cases.

- Consistent experience: Use standardized views that display the most relevant information for each network observability feature.

Flowlogs-pipeline performance enhancements
The `flowlogs-pipeline` component is optimized to improve network flow processing performance and resource efficiency. Performance enhancements reduce CPU and memory usage when handling high-volume network traffic.

This enhancement provides:

- Reduced resource consumption: Lower network traffic to API server from the `flowlogs-pipeline` component, resulting in better operational efficiency.

- Improved throughput: Process higher volumes of network flow data without performance degradation.

- Better scalability: Support larger cluster deployments with minimal additional infrastructure requirements.

Improved cluster role binding management
The Network Observability Operator enhances cluster role binding management to support custom installation namespaces while maintaining security and simplifying configuration. The Network Observability Operator manages cluster role bindings dynamically, eliminating the need for manual updates when changing the default namespace.

This improvement delivers:

- Flexible namespace configuration: Install Network Observability Operator components in custom namespaces without manual cluster role binding adjustments.

- Enhanced security: Prevent unauthorized access through namespace squatting by dynamically updating role bindings based on actual installation namespace.

- Upgrade compatibility: Preserve permissions automatically when the default namespace changes during Operator upgrades.

- Simplified administration: Reduce configuration steps required for non-default namespace installations.

# Network Observability Operator 2.0 fixed issues

The Network Observability Operator 2.0 release contains several fixed issues that improve monitoring accuracy, console plugin reliability, and overall system stability.

Flowlogs-pipeline pods start successfully in direct deployment mode with informers
Before this update, enabling shared informers in direct deployment mode caused flowlogs-pipeline pods to fail with volume mount errors. As a consequence, flow collection was unavailable when using this configuration.

With this release, TLS certificate volumes are correctly configured for flowlogs-pipeline pods in direct mode when informers are enabled. As a result, flow collection operates reliably in direct deployment mode with shared informer optimization.

[NETOBSERV-2875](https://issues.redhat.com/browse/NETOBSERV-2875)

Fixed TLS certificate handling for Kubernetes cache with user-provided certificates
Before this update, when the `FlowCollector` processor service TLS type was set to `Provided` for user-supplied certificates, the Kubernetes cache component defaulted to automatic TLS mode and referenced a certificate secret that was never created. As a consequence, `flowlogs-pipeline` pods failed to start with a volume mount error.

With this release, the Kubernetes cache TLS configuration correctly handles user-provided service certificates. As a result, `flowlogs-pipeline` pods start successfully when using certificate manager for TLS certificates.

[NETOBSERV-2940](https://issues.redhat.com/browse/NETOBSERV-2940)

Network Observability CLI compatibility with default node selectors
Before this update, the Network Observability CLI failed to deploy in clusters with a configured default node selector because the CLI namespace did not override the cluster-level selector. As a consequence, many CLI pods remained in pending status when attempting to capture network flows.

With this release, the CLI namespace includes an annotation to ignore the cluster default node selector. As a result, the Network Observability CLI deploys successfully on all cluster nodes regardless of default node selector configuration.

[NETOBSERV-2845](https://issues.redhat.com/browse/NETOBSERV-2845)

Corrected DNS metric names for alerting
Before this update, DNS flow metrics included an incorrect `_count` suffix that prevented Prometheus alert rules from evaluating properly. As a consequence, DNS-related alerts for NXDomain responses and DNS errors never triggered.

With this release, DNS flow metrics use the correct naming convention without the extraneous suffix. As a result, DNS monitoring alerts trigger when domain resolution failures or DNS errors occur.

[NETOBSERV-2964](https://issues.redhat.com/browse/NETOBSERV-2964)

Preserved namespace metadata during label reconciliation
Before this update, the Operator replaced existing namespace metadata when adding required labels for monitoring and eBPF agent namespaces. As a consequence, custom annotations and labels were removed, and OpenShift Security Context Constraints allocation annotations could be reassigned with different values, potentially causing pod execution failures.

With this release, the Operator preserves existing namespace annotations and custom labels when reconciling namespace configuration. As a result, namespace security context allocations remain stable and custom metadata is maintained during Operator operations.

[NETOBSERV-3018](https://issues.redhat.com/browse/NETOBSERV-3018)

Console plugin namespace updated after Operator reinstallation
Before this update, when reinstalling the Operator by using a different installation method, the static console plugin failed to load because the `ConsolePlugin` resource namespace was not updated to match the new installation. As a consequence, the Network Observability web console plugin was unavailable after reinstallation.

With this release, the Operator reconciles the `ConsolePlugin` resource during installation and updates the namespace configuration when changes are detected. As a result, the web console plugin loads correctly regardless of installation method.

[NETOBSERV-2890](https://issues.redhat.com/browse/NETOBSERV-2890)

Owner-scoped queries available when Loki is disabled
Before this update, owner-scoped queries required Loki as the data source and were not handled by Prometheus when Loki was disabled. As a consequence, users could not retrieve owner-based network flow data in Prometheus-only configurations.

With this release, the console plugin processes owner-scoped queries through Prometheus when Loki is unavailable. As a result, you can access owner-based network flow data regardless of Loki availability.

[NETOBSERV-3042](https://issues.redhat.com/browse/NETOBSERV-3042)

Accurate byte and packet counts for IPsec UDP-encrypted traffic
Before this update, network flows for UDP-encapsulated IPsec packets reported zero bytes and zero packets when the IPsec eBPF feature was enabled. As a consequence, traffic volume metrics were incorrect for encrypted network communications.

With this release, the eBPF agent correctly counts bytes and packets for UDP-encrypted IPsec payloads. As a result, you can view accurate traffic metrics for IPsec-protected network flows.

[NETOBSERV-2343](https://issues.redhat.com/browse/NETOBSERV-2343)

Secondary network flow enrichment with flowlogs-pipeline informers
Before this update, secondary network flows were not enriched with Kubernetes metadata when flowlogs-pipeline informers were enabled. As a consequence, user-defined network flows lacked pod, namespace, and workload information.

With this release, the flowlogs-pipeline informers correctly enrich flows from secondary networks including user-defined networks. As a result, you can view complete Kubernetes metadata for all network flows regardless of network attachment.

[NETOBSERV-2916](https://issues.redhat.com/browse/NETOBSERV-2916)

IPFIX export record isolation between flows
Before this update, the IP Flow Information Export (IPFIX) exporter retained data from previously processed flows in memory and included stale values in later flow records. As a consequence, exported IPFIX data contained incorrect metrics such as round-trip time values from unrelated flows.

With this release, the IPFIX exporter resets record data between flows to ensure clean isolation. As a result, each exported IPFIX record contains only metrics relevant to that specific network flow.

[NETOBSERV-3011](https://issues.redhat.com/browse/NETOBSERV-3011)

Consistent health rule visibility across sampling rates
Before this update, health rules by using the low volume threshold filter evaluated sampled metric values rather than normalized traffic volumes. As a consequence, increasing the sampling rate caused health rules to disappear from the Network Health page because observed packet counts fell below the threshold.

With this release, health rules are evaluated using normalized metrics that account for the configured sampling rate. As a result, health monitoring alerts and recording rules are triggered consistently regardless of the sampling configuration.

[NETOBSERV-2613](https://issues.redhat.com/browse/NETOBSERV-2613)

Fixed topology view export rendering
Before this update, exporting the topology view to a PNG image file resulted in blackened node labels and icons. As a consequence, the exported topology diagrams were unreadable.

With this release, topology export correctly renders node labels and icons with appropriate colors. As a result, you can export readable topology diagrams for documentation and reporting.

[NETOBSERV-2774](https://issues.redhat.com/browse/NETOBSERV-2774)

Corrected donut panel alignment in overview tab
Before this update, donut panels displaying paired metrics such as TLS and DNS statistics were misaligned within their rows. As a consequence, the panels appeared shifted to the left instead of centered.

With this release, donut panel positioning is corrected to center the visualizations properly. As a result, the overview tab displays network metrics with consistent and balanced panel alignment.

[NETOBSERV-2754](https://issues.redhat.com/browse/NETOBSERV-2754)
