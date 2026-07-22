<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Description
The `ServiceMonitor` custom resource definition (CRD) defines how `Prometheus` and `PrometheusAgent` can scrape metrics from a group of services. Among other things, it allows to specify: \* The services to scrape via label selectors. \* The container ports to scrape. \* Authentication credentials to use. \* Target and metric relabeling.

`Prometheus` and `PrometheusAgent` objects select `ServiceMonitor` objects using label and namespace selectors.

Type
`object`

Required
- `spec`

# Specification

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Property</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>apiVersion</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <a href="https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources">https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>kind</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <a href="https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds">https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>metadata</code></p></td>
<td style="text-align: left;"><p><a href="../objects/index.xml#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta"><code>ObjectMeta</code></a></p></td>
<td style="text-align: left;"><p>Standard object’s metadata. More info: <a href="https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata">https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>spec</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>Specification of desired Service selection for target discovery by Prometheus.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>status</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>This Status subresource is under active development and is updated only when the "StatusForConfigurationResources" feature gate is enabled.</p>
<p>Most recent observed status of the ServiceMonitor. Read-only. More info: <a href="https://github.com/kubernetes/community/blob/master/contributors/devel/sig-architecture/api-conventions.md#spec-and-status">https://github.com/kubernetes/community/blob/master/contributors/devel/sig-architecture/api-conventions.md#spec-and-status</a></p></td>
</tr>
</tbody>
</table>

## .spec

Description
Specification of desired Service selection for target discovery by Prometheus.

Type
`object`

Required
- `endpoints`

- `selector`

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Property</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>attachMetadata</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p><code>attachMetadata</code> defines additional metadata which is added to the discovered targets.</p>
<p>It requires Prometheus &gt;= v2.37.0.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>bodySizeLimit</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>When defined, bodySizeLimit specifies a job level limit on the size of uncompressed response body that will be accepted by Prometheus.</p>
<p>It requires Prometheus &gt;= v2.28.0.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>convertClassicHistogramsToNHCB</code></p></td>
<td style="text-align: left;"><p><code>boolean</code></p></td>
<td style="text-align: left;"><p>Whether to convert all scraped classic histograms into a native histogram with custom buckets. It requires Prometheus &gt;= v3.0.0.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>endpoints</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>List of endpoints part of this ServiceMonitor. Defines how to scrape metrics from Kubernetes [Endpoints](<a href="https://kubernetes.io/docs/concepts/services-networking/service/#endpoints">https://kubernetes.io/docs/concepts/services-networking/service/#endpoints</a>) objects. In most cases, an Endpoints object is backed by a Kubernetes [Service](<a href="https://kubernetes.io/docs/concepts/services-networking/service/">https://kubernetes.io/docs/concepts/services-networking/service/</a>) object with the same name and labels.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>endpoints[]</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>Endpoint defines an endpoint serving Prometheus metrics to be scraped by Prometheus.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>fallbackScrapeProtocol</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>The protocol to use if a scrape returns blank, unparseable, or otherwise invalid Content-Type.</p>
<p>It requires Prometheus &gt;= v3.0.0.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>jobLabel</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p><code>jobLabel</code> selects the label from the associated Kubernetes <code>Service</code> object which will be used as the <code>job</code> label for all metrics.</p>
<p>For example if <code>jobLabel</code> is set to <code>foo</code> and the Kubernetes <code>Service</code> object is labeled with <code>foo: bar</code>, then Prometheus adds the <code>job="bar"</code> label to all ingested metrics.</p>
<p>If the value of this field is empty or if the label doesn’t exist for the given Service, the <code>job</code> label of the metrics defaults to the name of the associated Kubernetes <code>Service</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>keepDroppedTargets</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p>Per-scrape limit on the number of targets dropped by relabeling that will be kept in memory. 0 means no limit.</p>
<p>It requires Prometheus &gt;= v2.47.0.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>labelLimit</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p>Per-scrape limit on number of labels that will be accepted for a sample.</p>
<p>It requires Prometheus &gt;= v2.27.0.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>labelNameLengthLimit</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p>Per-scrape limit on length of labels name that will be accepted for a sample.</p>
<p>It requires Prometheus &gt;= v2.27.0.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>labelValueLengthLimit</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p>Per-scrape limit on length of labels value that will be accepted for a sample.</p>
<p>It requires Prometheus &gt;= v2.27.0.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>namespaceSelector</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p><code>namespaceSelector</code> defines in which namespace(s) Prometheus should discover the services. By default, the services are discovered in the same namespace as the <code>ServiceMonitor</code> object but it is possible to select pods across different/all namespaces.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>nativeHistogramBucketLimit</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p>If there are more than this many buckets in a native histogram, buckets will be merged to stay within the limit. It requires Prometheus &gt;= v2.45.0.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>nativeHistogramMinBucketFactor</code></p></td>
<td style="text-align: left;"><p><code>integer-or-string</code></p></td>
<td style="text-align: left;"><p>If the growth factor of one bucket to the next is smaller than this, buckets will be merged to increase the factor sufficiently. It requires Prometheus &gt;= v2.50.0.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>podTargetLabels</code></p></td>
<td style="text-align: left;"><p><code>array (string)</code></p></td>
<td style="text-align: left;"><p><code>podTargetLabels</code> defines the labels which are transferred from the associated Kubernetes <code>Pod</code> object onto the ingested metrics.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>sampleLimit</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p><code>sampleLimit</code> defines a per-scrape limit on the number of scraped samples that will be accepted.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>scrapeClass</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>The scrape class to apply.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>scrapeClassicHistograms</code></p></td>
<td style="text-align: left;"><p><code>boolean</code></p></td>
<td style="text-align: left;"><p>Whether to scrape a classic histogram that is also exposed as a native histogram. It requires Prometheus &gt;= v2.45.0.</p>
<p>Notice: <code>scrapeClassicHistograms</code> corresponds to the <code>always_scrape_classic_histograms</code> field in the Prometheus configuration.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>scrapeProtocols</code></p></td>
<td style="text-align: left;"><p><code>array (string)</code></p></td>
<td style="text-align: left;"><p><code>scrapeProtocols</code> defines the protocols to negotiate during a scrape. It tells clients the protocols supported by Prometheus in order of preference (from most to least preferred).</p>
<p>If unset, Prometheus uses its default value.</p>
<p>It requires Prometheus &gt;= v2.49.0.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>selector</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>Label selector to select the Kubernetes <code>Endpoints</code> objects to scrape metrics from.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>selectorMechanism</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Mechanism used to select the endpoints to scrape. By default, the selection process relies on relabel configurations to filter the discovered targets. Alternatively, you can opt in for role selectors, which may offer better efficiency in large clusters. Which strategy is best for your use case needs to be carefully evaluated.</p>
<p>It requires Prometheus &gt;= v2.17.0.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>targetLabels</code></p></td>
<td style="text-align: left;"><p><code>array (string)</code></p></td>
<td style="text-align: left;"><p><code>targetLabels</code> defines the labels which are transferred from the associated Kubernetes <code>Service</code> object onto the ingested metrics.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>targetLimit</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p><code>targetLimit</code> defines a limit on the number of scraped targets that will be accepted.</p></td>
</tr>
</tbody>
</table>

## .spec.attachMetadata

Description
`attachMetadata` defines additional metadata which is added to the discovered targets.

It requires Prometheus \>= v2.37.0.

Type
`object`

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Property</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>node</code></p></td>
<td style="text-align: left;"><p><code>boolean</code></p></td>
<td style="text-align: left;"><p>When set to true, Prometheus attaches node metadata to the discovered targets.</p>
<p>The Prometheus service account must have the <code>list</code> and <code>watch</code> permissions on the <code>Nodes</code> objects.</p></td>
</tr>
</tbody>
</table>

## .spec.endpoints

Description
List of endpoints part of this ServiceMonitor. Defines how to scrape metrics from Kubernetes \[Endpoints\](<https://kubernetes.io/docs/concepts/services-networking/service/#endpoints>) objects. In most cases, an Endpoints object is backed by a Kubernetes \[Service\](<https://kubernetes.io/docs/concepts/services-networking/service/>) object with the same name and labels.

Type
`array`

## .spec.endpoints\[\]

Description
Endpoint defines an endpoint serving Prometheus metrics to be scraped by Prometheus.

Type
`object`

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Property</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>authorization</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p><code>authorization</code> configures the Authorization header credentials to use when scraping the target.</p>
<p>Cannot be set at the same time as <code>basicAuth</code>, or <code>oauth2</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>basicAuth</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p><code>basicAuth</code> configures the Basic Authentication credentials to use when scraping the target.</p>
<p>Cannot be set at the same time as <code>authorization</code>, or <code>oauth2</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>bearerTokenFile</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>File to read bearer token for scraping the target.</p>
<p>Deprecated: use <code>authorization</code> instead.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>bearerTokenSecret</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p><code>bearerTokenSecret</code> specifies a key of a Secret containing the bearer token for scraping targets. The secret needs to be in the same namespace as the ServiceMonitor object and readable by the Prometheus Operator.</p>
<p>Deprecated: use <code>authorization</code> instead.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>enableHttp2</code></p></td>
<td style="text-align: left;"><p><code>boolean</code></p></td>
<td style="text-align: left;"><p><code>enableHttp2</code> can be used to disable HTTP2 when scraping the target.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>filterRunning</code></p></td>
<td style="text-align: left;"><p><code>boolean</code></p></td>
<td style="text-align: left;"><p>When true, the pods which are not running (e.g. either in Failed or Succeeded state) are dropped during the target discovery.</p>
<p>If unset, the filtering is enabled.</p>
<p>More info: <a href="https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#pod-phase">https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#pod-phase</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>followRedirects</code></p></td>
<td style="text-align: left;"><p><code>boolean</code></p></td>
<td style="text-align: left;"><p><code>followRedirects</code> defines whether the scrape requests should follow HTTP 3xx redirects.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>honorLabels</code></p></td>
<td style="text-align: left;"><p><code>boolean</code></p></td>
<td style="text-align: left;"><p>When true, <code>honorLabels</code> preserves the metric’s labels when they collide with the target’s labels.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>honorTimestamps</code></p></td>
<td style="text-align: left;"><p><code>boolean</code></p></td>
<td style="text-align: left;"><p><code>honorTimestamps</code> controls whether Prometheus preserves the timestamps when exposed by the target.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>interval</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Interval at which Prometheus scrapes the metrics from the target.</p>
<p>If empty, Prometheus uses the global scrape interval.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>metricRelabelings</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p><code>metricRelabelings</code> configures the relabeling rules to apply to the samples before ingestion.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>metricRelabelings[]</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>RelabelConfig allows dynamic rewriting of the label set for targets, alerts, scraped samples and remote write samples.</p>
<p>More info: <a href="https://prometheus.io/docs/prometheus/latest/configuration/configuration/#relabel_config">https://prometheus.io/docs/prometheus/latest/configuration/configuration/#relabel_config</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>noProxy</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p><code>noProxy</code> is a comma-separated string that can contain IPs, CIDR notation, domain names that should be excluded from proxying. IP and domain names can contain port numbers.</p>
<p>It requires Prometheus &gt;= v2.43.0, Alertmanager &gt;= v0.25.0 or Thanos &gt;= v0.32.0.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>oauth2</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p><code>oauth2</code> configures the OAuth2 settings to use when scraping the target.</p>
<p>It requires Prometheus &gt;= 2.27.0.</p>
<p>Cannot be set at the same time as <code>authorization</code>, or <code>basicAuth</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>params</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>params define optional HTTP URL parameters.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>params{}</code></p></td>
<td style="text-align: left;"><p><code>array (string)</code></p></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>path</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>HTTP path from which to scrape for metrics.</p>
<p>If empty, Prometheus uses the default value (e.g. <code>/metrics</code>).</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>port</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Name of the Service port which this endpoint refers to.</p>
<p>It takes precedence over <code>targetPort</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>proxyConnectHeader</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>ProxyConnectHeader optionally specifies headers to send to proxies during CONNECT requests.</p>
<p>It requires Prometheus &gt;= v2.43.0, Alertmanager &gt;= v0.25.0 or Thanos &gt;= v0.32.0.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>proxyConnectHeader{}</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>proxyConnectHeader{}[]</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>SecretKeySelector selects a key of a Secret.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>proxyFromEnvironment</code></p></td>
<td style="text-align: left;"><p><code>boolean</code></p></td>
<td style="text-align: left;"><p>Whether to use the proxy configuration defined by environment variables (HTTP_PROXY, HTTPS_PROXY, and NO_PROXY).</p>
<p>It requires Prometheus &gt;= v2.43.0, Alertmanager &gt;= v0.25.0 or Thanos &gt;= v0.32.0.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>proxyUrl</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p><code>proxyURL</code> defines the HTTP proxy server to use.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>relabelings</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p><code>relabelings</code> configures the relabeling rules to apply the target’s metadata labels.</p>
<p>The Operator automatically adds relabelings for a few standard Kubernetes fields.</p>
<p>The original scrape job’s name is available via the <code>\__tmp_prometheus_job_name</code> label.</p>
<p>More info: <a href="https://prometheus.io/docs/prometheus/latest/configuration/configuration/#relabel_config">https://prometheus.io/docs/prometheus/latest/configuration/configuration/#relabel_config</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>relabelings[]</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>RelabelConfig allows dynamic rewriting of the label set for targets, alerts, scraped samples and remote write samples.</p>
<p>More info: <a href="https://prometheus.io/docs/prometheus/latest/configuration/configuration/#relabel_config">https://prometheus.io/docs/prometheus/latest/configuration/configuration/#relabel_config</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>scheme</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>HTTP scheme to use for scraping.</p>
<p><code>http</code> and <code>https</code> are the expected values unless you rewrite the <code>scheme</code> label via relabeling.</p>
<p>If empty, Prometheus uses the default value <code>http</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>scrapeTimeout</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Timeout after which Prometheus considers the scrape to be failed.</p>
<p>If empty, Prometheus uses the global scrape timeout unless it is less than the target’s scrape interval value in which the latter is used. The value cannot be greater than the scrape interval otherwise the operator will reject the resource.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>targetPort</code></p></td>
<td style="text-align: left;"><p><code>integer-or-string</code></p></td>
<td style="text-align: left;"><p>Name or number of the target port of the <code>Pod</code> object behind the Service. The port must be specified with the container’s port property.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>tlsConfig</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>TLS configuration to use when scraping the target.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>trackTimestampsStaleness</code></p></td>
<td style="text-align: left;"><p><code>boolean</code></p></td>
<td style="text-align: left;"><p><code>trackTimestampsStaleness</code> defines whether Prometheus tracks staleness of the metrics that have an explicit timestamp present in scraped data. Has no effect if <code>honorTimestamps</code> is false.</p>
<p>It requires Prometheus &gt;= v2.48.0.</p></td>
</tr>
</tbody>
</table>

## .spec.endpoints\[\].authorization

Description
`authorization` configures the Authorization header credentials to use when scraping the target.

Cannot be set at the same time as `basicAuth`, or `oauth2`.

Type
`object`

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Property</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>credentials</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>Selects a key of a Secret in the namespace that contains the credentials for authentication.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>type</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Defines the authentication type. The value is case-insensitive.</p>
<p>"Basic" is not a supported value.</p>
<p>Default: "Bearer"</p></td>
</tr>
</tbody>
</table>

## .spec.endpoints\[\].authorization.credentials

Description
Selects a key of a Secret in the namespace that contains the credentials for authentication.

Type
`object`

Required
- `key`

| Property | Type | Description |
|----|----|----|
| `key` | `string` | The key of the secret to select from. Must be a valid secret key. |
| `name` | `string` | Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names> |
| `optional` | `boolean` | Specify whether the Secret or its key must be defined |

## .spec.endpoints\[\].basicAuth

Description
`basicAuth` configures the Basic Authentication credentials to use when scraping the target.

Cannot be set at the same time as `authorization`, or `oauth2`.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `password` | `object` | `password` specifies a key of a Secret containing the password for authentication. |
| `username` | `object` | `username` specifies a key of a Secret containing the username for authentication. |

## .spec.endpoints\[\].basicAuth.password

Description
`password` specifies a key of a Secret containing the password for authentication.

Type
`object`

Required
- `key`

| Property | Type | Description |
|----|----|----|
| `key` | `string` | The key of the secret to select from. Must be a valid secret key. |
| `name` | `string` | Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names> |
| `optional` | `boolean` | Specify whether the Secret or its key must be defined |

## .spec.endpoints\[\].basicAuth.username

Description
`username` specifies a key of a Secret containing the username for authentication.

Type
`object`

Required
- `key`

| Property | Type | Description |
|----|----|----|
| `key` | `string` | The key of the secret to select from. Must be a valid secret key. |
| `name` | `string` | Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names> |
| `optional` | `boolean` | Specify whether the Secret or its key must be defined |

## .spec.endpoints\[\].bearerTokenSecret

Description
`bearerTokenSecret` specifies a key of a Secret containing the bearer token for scraping targets. The secret needs to be in the same namespace as the ServiceMonitor object and readable by the Prometheus Operator.

Deprecated: use `authorization` instead.

Type
`object`

Required
- `key`

| Property | Type | Description |
|----|----|----|
| `key` | `string` | The key of the secret to select from. Must be a valid secret key. |
| `name` | `string` | Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names> |
| `optional` | `boolean` | Specify whether the Secret or its key must be defined |

## .spec.endpoints\[\].metricRelabelings

Description
`metricRelabelings` configures the relabeling rules to apply to the samples before ingestion.

Type
`array`

## .spec.endpoints\[\].metricRelabelings\[\]

Description
RelabelConfig allows dynamic rewriting of the label set for targets, alerts, scraped samples and remote write samples.

More info: <https://prometheus.io/docs/prometheus/latest/configuration/configuration/#relabel_config>

Type
`object`

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Property</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>action</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Action to perform based on the regex matching.</p>
<p><code>Uppercase</code> and <code>Lowercase</code> actions require Prometheus &gt;= v2.36.0. <code>DropEqual</code> and <code>KeepEqual</code> actions require Prometheus &gt;= v2.41.0.</p>
<p>Default: "Replace"</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>modulus</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p>Modulus to take of the hash of the source label values.</p>
<p>Only applicable when the action is <code>HashMod</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>regex</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Regular expression against which the extracted value is matched.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>replacement</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Replacement value against which a Replace action is performed if the regular expression matches.</p>
<p>Regex capture groups are available.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>separator</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Separator is the string between concatenated SourceLabels.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>sourceLabels</code></p></td>
<td style="text-align: left;"><p><code>array (string)</code></p></td>
<td style="text-align: left;"><p>The source labels select values from existing labels. Their content is concatenated using the configured Separator and matched against the configured regular expression.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>targetLabel</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Label to which the resulting string is written in a replacement.</p>
<p>It is mandatory for <code>Replace</code>, <code>HashMod</code>, <code>Lowercase</code>, <code>Uppercase</code>, <code>KeepEqual</code> and <code>DropEqual</code> actions.</p>
<p>Regex capture groups are available.</p></td>
</tr>
</tbody>
</table>

## .spec.endpoints\[\].oauth2

Description
`oauth2` configures the OAuth2 settings to use when scraping the target.

It requires Prometheus \>= 2.27.0.

Cannot be set at the same time as `authorization`, or `basicAuth`.

Type
`object`

Required
- `clientId`

- `clientSecret`

- `tokenUrl`

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Property</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>clientId</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p><code>clientId</code> specifies a key of a Secret or ConfigMap containing the OAuth2 client’s ID.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>clientSecret</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p><code>clientSecret</code> specifies a key of a Secret containing the OAuth2 client’s secret.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>endpointParams</code></p></td>
<td style="text-align: left;"><p><code>object (string)</code></p></td>
<td style="text-align: left;"><p><code>endpointParams</code> configures the HTTP parameters to append to the token URL.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>noProxy</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p><code>noProxy</code> is a comma-separated string that can contain IPs, CIDR notation, domain names that should be excluded from proxying. IP and domain names can contain port numbers.</p>
<p>It requires Prometheus &gt;= v2.43.0, Alertmanager &gt;= v0.25.0 or Thanos &gt;= v0.32.0.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>proxyConnectHeader</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>ProxyConnectHeader optionally specifies headers to send to proxies during CONNECT requests.</p>
<p>It requires Prometheus &gt;= v2.43.0, Alertmanager &gt;= v0.25.0 or Thanos &gt;= v0.32.0.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>proxyConnectHeader{}</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>proxyConnectHeader{}[]</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>SecretKeySelector selects a key of a Secret.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>proxyFromEnvironment</code></p></td>
<td style="text-align: left;"><p><code>boolean</code></p></td>
<td style="text-align: left;"><p>Whether to use the proxy configuration defined by environment variables (HTTP_PROXY, HTTPS_PROXY, and NO_PROXY).</p>
<p>It requires Prometheus &gt;= v2.43.0, Alertmanager &gt;= v0.25.0 or Thanos &gt;= v0.32.0.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>proxyUrl</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p><code>proxyURL</code> defines the HTTP proxy server to use.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>scopes</code></p></td>
<td style="text-align: left;"><p><code>array (string)</code></p></td>
<td style="text-align: left;"><p><code>scopes</code> defines the OAuth2 scopes used for the token request.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>tlsConfig</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>TLS configuration to use when connecting to the OAuth2 server. It requires Prometheus &gt;= v2.43.0.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>tokenUrl</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p><code>tokenURL</code> configures the URL to fetch the token from.</p></td>
</tr>
</tbody>
</table>

## .spec.endpoints\[\].oauth2.clientId

Description
`clientId` specifies a key of a Secret or ConfigMap containing the OAuth2 client’s ID.

Type
`object`

| Property    | Type     | Description                                       |
|-------------|----------|---------------------------------------------------|
| `configMap` | `object` | ConfigMap containing data to use for the targets. |
| `secret`    | `object` | Secret containing data to use for the targets.    |

## .spec.endpoints\[\].oauth2.clientId.configMap

Description
ConfigMap containing data to use for the targets.

Type
`object`

Required
- `key`

| Property | Type | Description |
|----|----|----|
| `key` | `string` | The key to select. |
| `name` | `string` | Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names> |
| `optional` | `boolean` | Specify whether the ConfigMap or its key must be defined |

## .spec.endpoints\[\].oauth2.clientId.secret

Description
Secret containing data to use for the targets.

Type
`object`

Required
- `key`

| Property | Type | Description |
|----|----|----|
| `key` | `string` | The key of the secret to select from. Must be a valid secret key. |
| `name` | `string` | Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names> |
| `optional` | `boolean` | Specify whether the Secret or its key must be defined |

## .spec.endpoints\[\].oauth2.clientSecret

Description
`clientSecret` specifies a key of a Secret containing the OAuth2 client’s secret.

Type
`object`

Required
- `key`

| Property | Type | Description |
|----|----|----|
| `key` | `string` | The key of the secret to select from. Must be a valid secret key. |
| `name` | `string` | Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names> |
| `optional` | `boolean` | Specify whether the Secret or its key must be defined |

## .spec.endpoints\[\].oauth2.proxyConnectHeader

Description
ProxyConnectHeader optionally specifies headers to send to proxies during CONNECT requests.

It requires Prometheus \>= v2.43.0, Alertmanager \>= v0.25.0 or Thanos \>= v0.32.0.

Type
`object`

## .spec.endpoints\[\].oauth2.proxyConnectHeader{}

Description

Type
`array`

## .spec.endpoints\[\].oauth2.proxyConnectHeader{}\[\]

Description
SecretKeySelector selects a key of a Secret.

Type
`object`

Required
- `key`

| Property | Type | Description |
|----|----|----|
| `key` | `string` | The key of the secret to select from. Must be a valid secret key. |
| `name` | `string` | Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names> |
| `optional` | `boolean` | Specify whether the Secret or its key must be defined |

## .spec.endpoints\[\].oauth2.tlsConfig

Description
TLS configuration to use when connecting to the OAuth2 server. It requires Prometheus \>= v2.43.0.

Type
`object`

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Property</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>ca</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>Certificate authority used when verifying server certificates.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>cert</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>Client certificate to present when doing client-authentication.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>insecureSkipVerify</code></p></td>
<td style="text-align: left;"><p><code>boolean</code></p></td>
<td style="text-align: left;"><p>Disable target certificate validation.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>keySecret</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>Secret containing the client key file for the targets.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>maxVersion</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Maximum acceptable TLS version.</p>
<p>It requires Prometheus &gt;= v2.41.0 or Thanos &gt;= v0.31.0.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>minVersion</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Minimum acceptable TLS version.</p>
<p>It requires Prometheus &gt;= v2.35.0 or Thanos &gt;= v0.28.0.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>serverName</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Used to verify the hostname for the targets.</p></td>
</tr>
</tbody>
</table>

## .spec.endpoints\[\].oauth2.tlsConfig.ca

Description
Certificate authority used when verifying server certificates.

Type
`object`

| Property    | Type     | Description                                       |
|-------------|----------|---------------------------------------------------|
| `configMap` | `object` | ConfigMap containing data to use for the targets. |
| `secret`    | `object` | Secret containing data to use for the targets.    |

## .spec.endpoints\[\].oauth2.tlsConfig.ca.configMap

Description
ConfigMap containing data to use for the targets.

Type
`object`

Required
- `key`

| Property | Type | Description |
|----|----|----|
| `key` | `string` | The key to select. |
| `name` | `string` | Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names> |
| `optional` | `boolean` | Specify whether the ConfigMap or its key must be defined |

## .spec.endpoints\[\].oauth2.tlsConfig.ca.secret

Description
Secret containing data to use for the targets.

Type
`object`

Required
- `key`

| Property | Type | Description |
|----|----|----|
| `key` | `string` | The key of the secret to select from. Must be a valid secret key. |
| `name` | `string` | Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names> |
| `optional` | `boolean` | Specify whether the Secret or its key must be defined |

## .spec.endpoints\[\].oauth2.tlsConfig.cert

Description
Client certificate to present when doing client-authentication.

Type
`object`

| Property    | Type     | Description                                       |
|-------------|----------|---------------------------------------------------|
| `configMap` | `object` | ConfigMap containing data to use for the targets. |
| `secret`    | `object` | Secret containing data to use for the targets.    |

## .spec.endpoints\[\].oauth2.tlsConfig.cert.configMap

Description
ConfigMap containing data to use for the targets.

Type
`object`

Required
- `key`

| Property | Type | Description |
|----|----|----|
| `key` | `string` | The key to select. |
| `name` | `string` | Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names> |
| `optional` | `boolean` | Specify whether the ConfigMap or its key must be defined |

## .spec.endpoints\[\].oauth2.tlsConfig.cert.secret

Description
Secret containing data to use for the targets.

Type
`object`

Required
- `key`

| Property | Type | Description |
|----|----|----|
| `key` | `string` | The key of the secret to select from. Must be a valid secret key. |
| `name` | `string` | Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names> |
| `optional` | `boolean` | Specify whether the Secret or its key must be defined |

## .spec.endpoints\[\].oauth2.tlsConfig.keySecret

Description
Secret containing the client key file for the targets.

Type
`object`

Required
- `key`

| Property | Type | Description |
|----|----|----|
| `key` | `string` | The key of the secret to select from. Must be a valid secret key. |
| `name` | `string` | Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names> |
| `optional` | `boolean` | Specify whether the Secret or its key must be defined |

## .spec.endpoints\[\].params

Description
params define optional HTTP URL parameters.

Type
`object`

## .spec.endpoints\[\].proxyConnectHeader

Description
ProxyConnectHeader optionally specifies headers to send to proxies during CONNECT requests.

It requires Prometheus \>= v2.43.0, Alertmanager \>= v0.25.0 or Thanos \>= v0.32.0.

Type
`object`

## .spec.endpoints\[\].proxyConnectHeader{}

Description

Type
`array`

## .spec.endpoints\[\].proxyConnectHeader{}\[\]

Description
SecretKeySelector selects a key of a Secret.

Type
`object`

Required
- `key`

| Property | Type | Description |
|----|----|----|
| `key` | `string` | The key of the secret to select from. Must be a valid secret key. |
| `name` | `string` | Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names> |
| `optional` | `boolean` | Specify whether the Secret or its key must be defined |

## .spec.endpoints\[\].relabelings

Description
`relabelings` configures the relabeling rules to apply the target’s metadata labels.

The Operator automatically adds relabelings for a few standard Kubernetes fields.

The original scrape job’s name is available via the `\__tmp_prometheus_job_name` label.

More info: <https://prometheus.io/docs/prometheus/latest/configuration/configuration/#relabel_config>

Type
`array`

## .spec.endpoints\[\].relabelings\[\]

Description
RelabelConfig allows dynamic rewriting of the label set for targets, alerts, scraped samples and remote write samples.

More info: <https://prometheus.io/docs/prometheus/latest/configuration/configuration/#relabel_config>

Type
`object`

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Property</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>action</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Action to perform based on the regex matching.</p>
<p><code>Uppercase</code> and <code>Lowercase</code> actions require Prometheus &gt;= v2.36.0. <code>DropEqual</code> and <code>KeepEqual</code> actions require Prometheus &gt;= v2.41.0.</p>
<p>Default: "Replace"</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>modulus</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p>Modulus to take of the hash of the source label values.</p>
<p>Only applicable when the action is <code>HashMod</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>regex</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Regular expression against which the extracted value is matched.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>replacement</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Replacement value against which a Replace action is performed if the regular expression matches.</p>
<p>Regex capture groups are available.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>separator</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Separator is the string between concatenated SourceLabels.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>sourceLabels</code></p></td>
<td style="text-align: left;"><p><code>array (string)</code></p></td>
<td style="text-align: left;"><p>The source labels select values from existing labels. Their content is concatenated using the configured Separator and matched against the configured regular expression.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>targetLabel</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Label to which the resulting string is written in a replacement.</p>
<p>It is mandatory for <code>Replace</code>, <code>HashMod</code>, <code>Lowercase</code>, <code>Uppercase</code>, <code>KeepEqual</code> and <code>DropEqual</code> actions.</p>
<p>Regex capture groups are available.</p></td>
</tr>
</tbody>
</table>

## .spec.endpoints\[\].tlsConfig

Description
TLS configuration to use when scraping the target.

Type
`object`

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Property</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>ca</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>Certificate authority used when verifying server certificates.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>caFile</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Path to the CA cert in the Prometheus container to use for the targets.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>cert</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>Client certificate to present when doing client-authentication.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>certFile</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Path to the client cert file in the Prometheus container for the targets.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>insecureSkipVerify</code></p></td>
<td style="text-align: left;"><p><code>boolean</code></p></td>
<td style="text-align: left;"><p>Disable target certificate validation.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>keyFile</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Path to the client key file in the Prometheus container for the targets.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>keySecret</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>Secret containing the client key file for the targets.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>maxVersion</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Maximum acceptable TLS version.</p>
<p>It requires Prometheus &gt;= v2.41.0 or Thanos &gt;= v0.31.0.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>minVersion</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Minimum acceptable TLS version.</p>
<p>It requires Prometheus &gt;= v2.35.0 or Thanos &gt;= v0.28.0.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>serverName</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Used to verify the hostname for the targets.</p></td>
</tr>
</tbody>
</table>

## .spec.endpoints\[\].tlsConfig.ca

Description
Certificate authority used when verifying server certificates.

Type
`object`

| Property    | Type     | Description                                       |
|-------------|----------|---------------------------------------------------|
| `configMap` | `object` | ConfigMap containing data to use for the targets. |
| `secret`    | `object` | Secret containing data to use for the targets.    |

## .spec.endpoints\[\].tlsConfig.ca.configMap

Description
ConfigMap containing data to use for the targets.

Type
`object`

Required
- `key`

| Property | Type | Description |
|----|----|----|
| `key` | `string` | The key to select. |
| `name` | `string` | Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names> |
| `optional` | `boolean` | Specify whether the ConfigMap or its key must be defined |

## .spec.endpoints\[\].tlsConfig.ca.secret

Description
Secret containing data to use for the targets.

Type
`object`

Required
- `key`

| Property | Type | Description |
|----|----|----|
| `key` | `string` | The key of the secret to select from. Must be a valid secret key. |
| `name` | `string` | Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names> |
| `optional` | `boolean` | Specify whether the Secret or its key must be defined |

## .spec.endpoints\[\].tlsConfig.cert

Description
Client certificate to present when doing client-authentication.

Type
`object`

| Property    | Type     | Description                                       |
|-------------|----------|---------------------------------------------------|
| `configMap` | `object` | ConfigMap containing data to use for the targets. |
| `secret`    | `object` | Secret containing data to use for the targets.    |

## .spec.endpoints\[\].tlsConfig.cert.configMap

Description
ConfigMap containing data to use for the targets.

Type
`object`

Required
- `key`

| Property | Type | Description |
|----|----|----|
| `key` | `string` | The key to select. |
| `name` | `string` | Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names> |
| `optional` | `boolean` | Specify whether the ConfigMap or its key must be defined |

## .spec.endpoints\[\].tlsConfig.cert.secret

Description
Secret containing data to use for the targets.

Type
`object`

Required
- `key`

| Property | Type | Description |
|----|----|----|
| `key` | `string` | The key of the secret to select from. Must be a valid secret key. |
| `name` | `string` | Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names> |
| `optional` | `boolean` | Specify whether the Secret or its key must be defined |

## .spec.endpoints\[\].tlsConfig.keySecret

Description
Secret containing the client key file for the targets.

Type
`object`

Required
- `key`

| Property | Type | Description |
|----|----|----|
| `key` | `string` | The key of the secret to select from. Must be a valid secret key. |
| `name` | `string` | Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names> |
| `optional` | `boolean` | Specify whether the Secret or its key must be defined |

## .spec.namespaceSelector

Description
`namespaceSelector` defines in which namespace(s) Prometheus should discover the services. By default, the services are discovered in the same namespace as the `ServiceMonitor` object but it is possible to select pods across different/all namespaces.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `any` | `boolean` | Boolean describing whether all namespaces are selected in contrast to a list restricting them. |
| `matchNames` | `array (string)` | List of namespace names to select from. |

## .spec.selector

Description
Label selector to select the Kubernetes `Endpoints` objects to scrape metrics from.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `matchExpressions` | `array` | matchExpressions is a list of label selector requirements. The requirements are ANDed. |
| `matchExpressions[]` | `object` | A label selector requirement is a selector that contains values, a key, and an operator that relates the key and values. |
| `matchLabels` | `object (string)` | matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed. |

## .spec.selector.matchExpressions

Description
matchExpressions is a list of label selector requirements. The requirements are ANDed.

Type
`array`

## .spec.selector.matchExpressions\[\]

Description
A label selector requirement is a selector that contains values, a key, and an operator that relates the key and values.

Type
`object`

Required
- `key`

- `operator`

| Property | Type | Description |
|----|----|----|
| `key` | `string` | key is the label key that the selector applies to. |
| `operator` | `string` | operator represents a key’s relationship to a set of values. Valid operators are In, NotIn, Exists and DoesNotExist. |
| `values` | `array (string)` | values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch. |

## .status

Description
This Status subresource is under active development and is updated only when the "StatusForConfigurationResources" feature gate is enabled.

Most recent observed status of the ServiceMonitor. Read-only. More info: <https://github.com/kubernetes/community/blob/master/contributors/devel/sig-architecture/api-conventions.md#spec-and-status>

Type
`object`

| Property | Type | Description |
|----|----|----|
| `bindings` | `array` | The list of workload resources (Prometheus or PrometheusAgent) which select the configuration resource. |
| `bindings[]` | `object` | WorkloadBinding is a link between a configuration resource and a workload resource. |

## .status.bindings

Description
The list of workload resources (Prometheus or PrometheusAgent) which select the configuration resource.

Type
`array`

## .status.bindings\[\]

Description
WorkloadBinding is a link between a configuration resource and a workload resource.

Type
`object`

Required
- `group`

- `name`

- `namespace`

- `resource`

| Property | Type | Description |
|----|----|----|
| `conditions` | `array` | The current state of the configuration resource when bound to the referenced Prometheus object. |
| `conditions[]` | `object` | ConfigResourceCondition describes the status of configuration resources linked to Prometheus, PrometheusAgent, Alertmanager, or ThanosRuler. |
| `group` | `string` | The group of the referenced resource. |
| `name` | `string` | The name of the referenced object. |
| `namespace` | `string` | The namespace of the referenced object. |
| `resource` | `string` | The type of resource being referenced (e.g. Prometheus or PrometheusAgent). |

## .status.bindings\[\].conditions

Description
The current state of the configuration resource when bound to the referenced Prometheus object.

Type
`array`

## .status.bindings\[\].conditions\[\]

Description
ConfigResourceCondition describes the status of configuration resources linked to Prometheus, PrometheusAgent, Alertmanager, or ThanosRuler.

Type
`object`

Required
- `lastTransitionTime`

- `status`

- `type`

| Property | Type | Description |
|----|----|----|
| `lastTransitionTime` | `string` | LastTransitionTime is the time of the last update to the current status property. |
| `message` | `string` | Human-readable message indicating details for the condition’s last transition. |
| `observedGeneration` | `integer` | ObservedGeneration represents the .metadata.generation that the condition was set based upon. For instance, if `.metadata.generation` is currently 12, but the `.status.conditions[].observedGeneration` is 9, the condition is out of date with respect to the current state of the object. |
| `reason` | `string` | Reason for the condition’s last transition. |
| `status` | `string` | Status of the condition. |
| `type` | `string` | Type of the condition being reported. Currently, only "Accepted" is supported. |

# API endpoints

The following API endpoints are available:

- `/apis/monitoring.coreos.com/v1/servicemonitors`

  - `GET`: list objects of kind ServiceMonitor

- `/apis/monitoring.coreos.com/v1/namespaces/{namespace}/servicemonitors`

  - `DELETE`: delete collection of ServiceMonitor

  - `GET`: list objects of kind ServiceMonitor

  - `POST`: create a ServiceMonitor

- `/apis/monitoring.coreos.com/v1/namespaces/{namespace}/servicemonitors/{name}`

  - `DELETE`: delete a ServiceMonitor

  - `GET`: read the specified ServiceMonitor

  - `PATCH`: partially update the specified ServiceMonitor

  - `PUT`: replace the specified ServiceMonitor

- `/apis/monitoring.coreos.com/v1/namespaces/{namespace}/servicemonitors/{name}/status`

  - `GET`: read status of the specified ServiceMonitor

  - `PATCH`: partially update status of the specified ServiceMonitor

  - `PUT`: replace status of the specified ServiceMonitor

## /apis/monitoring.coreos.com/v1/servicemonitors

HTTP method
`GET`

Description
list objects of kind ServiceMonitor

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ServiceMonitorList`](../objects/index.md#com-coreos-monitoring-v1-ServiceMonitorList) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/monitoring.coreos.com/v1/namespaces/{namespace}/servicemonitors

HTTP method
`DELETE`

Description
delete collection of ServiceMonitor

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Status`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`GET`

Description
list objects of kind ServiceMonitor

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ServiceMonitorList`](../objects/index.md#com-coreos-monitoring-v1-ServiceMonitorList) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`POST`

Description
create a ServiceMonitor

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`ServiceMonitor`](servicemonitor-monitoring-coreos-com-v1.md#servicemonitor-monitoring-coreos-com-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ServiceMonitor`](servicemonitor-monitoring-coreos-com-v1.md#servicemonitor-monitoring-coreos-com-v1) schema |
| 201 - Created | [`ServiceMonitor`](servicemonitor-monitoring-coreos-com-v1.md#servicemonitor-monitoring-coreos-com-v1) schema |
| 202 - Accepted | [`ServiceMonitor`](servicemonitor-monitoring-coreos-com-v1.md#servicemonitor-monitoring-coreos-com-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/monitoring.coreos.com/v1/namespaces/{namespace}/servicemonitors/{name}

| Parameter | Type     | Description                |
|-----------|----------|----------------------------|
| `name`    | `string` | name of the ServiceMonitor |

Global path parameters

HTTP method
`DELETE`

Description
delete a ServiceMonitor

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |

Query parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Status`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 202 - Accepted | [`Status`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`GET`

Description
read the specified ServiceMonitor

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ServiceMonitor`](servicemonitor-monitoring-coreos-com-v1.md#servicemonitor-monitoring-coreos-com-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PATCH`

Description
partially update the specified ServiceMonitor

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ServiceMonitor`](servicemonitor-monitoring-coreos-com-v1.md#servicemonitor-monitoring-coreos-com-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PUT`

Description
replace the specified ServiceMonitor

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`ServiceMonitor`](servicemonitor-monitoring-coreos-com-v1.md#servicemonitor-monitoring-coreos-com-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ServiceMonitor`](servicemonitor-monitoring-coreos-com-v1.md#servicemonitor-monitoring-coreos-com-v1) schema |
| 201 - Created | [`ServiceMonitor`](servicemonitor-monitoring-coreos-com-v1.md#servicemonitor-monitoring-coreos-com-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/monitoring.coreos.com/v1/namespaces/{namespace}/servicemonitors/{name}/status

| Parameter | Type     | Description                |
|-----------|----------|----------------------------|
| `name`    | `string` | name of the ServiceMonitor |

Global path parameters

HTTP method
`GET`

Description
read status of the specified ServiceMonitor

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ServiceMonitor`](servicemonitor-monitoring-coreos-com-v1.md#servicemonitor-monitoring-coreos-com-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PATCH`

Description
partially update status of the specified ServiceMonitor

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ServiceMonitor`](servicemonitor-monitoring-coreos-com-v1.md#servicemonitor-monitoring-coreos-com-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PUT`

Description
replace status of the specified ServiceMonitor

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`ServiceMonitor`](servicemonitor-monitoring-coreos-com-v1.md#servicemonitor-monitoring-coreos-com-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ServiceMonitor`](servicemonitor-monitoring-coreos-com-v1.md#servicemonitor-monitoring-coreos-com-v1) schema |
| 201 - Created | [`ServiceMonitor`](servicemonitor-monitoring-coreos-com-v1.md#servicemonitor-monitoring-coreos-com-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses
