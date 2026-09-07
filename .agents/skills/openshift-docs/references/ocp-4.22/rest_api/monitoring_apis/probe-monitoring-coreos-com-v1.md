<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Description
The `Probe` custom resource definition (CRD) defines how to scrape metrics from prober exporters such as the \[blackbox exporter\](<https://github.com/prometheus/blackbox_exporter>).

The `Probe` resource needs 2 pieces of information: \* The list of probed addresses which can be defined statically or by discovering Kubernetes Ingress objects. \* The prober which exposes the availability of probed endpoints (over various protocols such HTTP, TCP, ICMP, …​) as Prometheus metrics.

`Prometheus` and `PrometheusAgent` objects select `Probe` objects using label and namespace selectors.

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
<td style="text-align: left;"><p>spec defines the specification of desired Ingress selection for target discovery by Prometheus.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>status</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>status defines the status subresource. It is under active development and is updated only when the "StatusForConfigurationResources" feature gate is enabled.</p>
<p>Most recent observed status of the Probe. Read-only. More info: <a href="https://github.com/kubernetes/community/blob/master/contributors/devel/sig-architecture/api-conventions.md#spec-and-status">https://github.com/kubernetes/community/blob/master/contributors/devel/sig-architecture/api-conventions.md#spec-and-status</a></p></td>
</tr>
</tbody>
</table>

## .spec

Description
spec defines the specification of desired Ingress selection for target discovery by Prometheus.

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
<td style="text-align: left;"><p>authorization configures the Authorization header credentials used by the client.</p>
<p>Cannot be set at the same time as <code>basicAuth</code>, <code>bearerTokenSecret</code> or <code>oauth2</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>basicAuth</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>basicAuth defines the Basic Authentication credentials used by the client.</p>
<p>Cannot be set at the same time as <code>authorization</code>, <code>bearerTokenSecret</code> or <code>oauth2</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>bearerTokenSecret</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>bearerTokenSecret defines a key of a Secret containing the bearer token used by the client for authentication. The secret needs to be in the same namespace as the custom resource and readable by the Prometheus Operator.</p>
<p>Cannot be set at the same time as <code>authorization</code>, <code>basicAuth</code> or <code>oauth2</code>.</p>
<p>Deprecated: use <code>authorization</code> instead.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>convertClassicHistogramsToNHCB</code></p></td>
<td style="text-align: left;"><p><code>boolean</code></p></td>
<td style="text-align: left;"><p>convertClassicHistogramsToNHCB defines whether to convert all scraped classic histograms into a native histogram with custom buckets. It requires Prometheus &gt;= v3.0.0.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>enableHttp2</code></p></td>
<td style="text-align: left;"><p><code>boolean</code></p></td>
<td style="text-align: left;"><p>enableHttp2 can be used to disable HTTP2.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>fallbackScrapeProtocol</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>fallbackScrapeProtocol defines the protocol to use if a scrape returns blank, unparseable, or otherwise invalid Content-Type.</p>
<p>It requires Prometheus &gt;= v3.0.0.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>followRedirects</code></p></td>
<td style="text-align: left;"><p><code>boolean</code></p></td>
<td style="text-align: left;"><p>followRedirects defines whether the client should follow HTTP 3xx redirects.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>interval</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>interval at which targets are probed using the configured prober. If not specified Prometheus' global scrape interval is used.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>jobName</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>jobName assigned to scraped metrics by default.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>keepDroppedTargets</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p>keepDroppedTargets defines the per-scrape limit on the number of targets dropped by relabeling that will be kept in memory. 0 means no limit.</p>
<p>It requires Prometheus &gt;= v2.47.0.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>labelLimit</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p>labelLimit defines the per-scrape limit on number of labels that will be accepted for a sample. Only valid in Prometheus versions 2.27.0 and newer.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>labelNameLengthLimit</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p>labelNameLengthLimit defines the per-scrape limit on length of labels name that will be accepted for a sample. Only valid in Prometheus versions 2.27.0 and newer.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>labelValueLengthLimit</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p>labelValueLengthLimit defines the per-scrape limit on length of labels value that will be accepted for a sample. Only valid in Prometheus versions 2.27.0 and newer.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>metricRelabelings</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>metricRelabelings defines the RelabelConfig to apply to samples before ingestion.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>metricRelabelings[]</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>RelabelConfig allows dynamic rewriting of the label set for targets, alerts, scraped samples and remote write samples.</p>
<p>More info: <a href="https://prometheus.io/docs/prometheus/latest/configuration/configuration/#relabel_config">https://prometheus.io/docs/prometheus/latest/configuration/configuration/#relabel_config</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>module</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>module to use for probing specifying how to probe the target. Example module configuring in the blackbox exporter: <a href="https://github.com/prometheus/blackbox_exporter/blob/master/example.yml">https://github.com/prometheus/blackbox_exporter/blob/master/example.yml</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>nativeHistogramBucketLimit</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p>nativeHistogramBucketLimit defines ff there are more than this many buckets in a native histogram, buckets will be merged to stay within the limit. It requires Prometheus &gt;= v2.45.0.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>nativeHistogramMinBucketFactor</code></p></td>
<td style="text-align: left;"><p><code>integer-or-string</code></p></td>
<td style="text-align: left;"><p>nativeHistogramMinBucketFactor defines if the growth factor of one bucket to the next is smaller than this, buckets will be merged to increase the factor sufficiently. It requires Prometheus &gt;= v2.50.0.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>oauth2</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>oauth2 defines the OAuth2 settings used by the client.</p>
<p>It requires Prometheus &gt;= 2.27.0.</p>
<p>Cannot be set at the same time as <code>authorization</code>, <code>basicAuth</code> or <code>bearerTokenSecret</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>params</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>params defines the list of HTTP query parameters for the scrape. Please note that the <code>.spec.module</code> field takes precedence over the <code>module</code> parameter from this list when both are defined. The module name must be added using Module under ProbeSpec.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>params[]</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>ProbeParam defines specification of extra parameters for a Probe.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>prober</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>prober defines the specification for the prober to use for probing targets. The prober.URL parameter is required. Targets cannot be probed if left empty.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>sampleLimit</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p>sampleLimit defines per-scrape limit on number of scraped samples that will be accepted.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>scrapeClass</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>scrapeClass defines the scrape class to apply.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>scrapeClassicHistograms</code></p></td>
<td style="text-align: left;"><p><code>boolean</code></p></td>
<td style="text-align: left;"><p>scrapeClassicHistograms defines whether to scrape a classic histogram that is also exposed as a native histogram. It requires Prometheus &gt;= v2.45.0.</p>
<p>Notice: <code>scrapeClassicHistograms</code> corresponds to the <code>always_scrape_classic_histograms</code> field in the Prometheus configuration.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>scrapeNativeHistograms</code></p></td>
<td style="text-align: left;"><p><code>boolean</code></p></td>
<td style="text-align: left;"><p>scrapeNativeHistograms defines whether to enable scraping of native histograms. It requires Prometheus &gt;= v3.8.0.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>scrapeProtocols</code></p></td>
<td style="text-align: left;"><p><code>array (string)</code></p></td>
<td style="text-align: left;"><p>scrapeProtocols defines the protocols to negotiate during a scrape. It tells clients the protocols supported by Prometheus in order of preference (from most to least preferred).</p>
<p>If unset, Prometheus uses its default value.</p>
<p>It requires Prometheus &gt;= v2.49.0.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>scrapeTimeout</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>scrapeTimeout defines the timeout for scraping metrics from the Prometheus exporter. If not specified, the Prometheus global scrape timeout is used. The value cannot be greater than the scrape interval otherwise the operator will reject the resource.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>targetLimit</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p>targetLimit defines a limit on the number of scraped targets that will be accepted.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>targets</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>targets defines a set of static or dynamically discovered targets to probe.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>tlsConfig</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>tlsConfig defines the TLS configuration used by the client.</p></td>
</tr>
</tbody>
</table>

## .spec.authorization

Description
authorization configures the Authorization header credentials used by the client.

Cannot be set at the same time as `basicAuth`, `bearerTokenSecret` or `oauth2`.

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
<td style="text-align: left;"><p>credentials defines a key of a Secret in the namespace that contains the credentials for authentication.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>type</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>type defines the authentication type. The value is case-insensitive.</p>
<p>"Basic" is not a supported value.</p>
<p>Default: "Bearer"</p></td>
</tr>
</tbody>
</table>

## .spec.authorization.credentials

Description
credentials defines a key of a Secret in the namespace that contains the credentials for authentication.

Type
`object`

Required
- `key`

| Property | Type | Description |
|----|----|----|
| `key` | `string` | The key of the secret to select from. Must be a valid secret key. |
| `name` | `string` | Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names> |
| `optional` | `boolean` | Specify whether the Secret or its key must be defined |

## .spec.basicAuth

Description
basicAuth defines the Basic Authentication credentials used by the client.

Cannot be set at the same time as `authorization`, `bearerTokenSecret` or `oauth2`.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `password` | `object` | password defines a key of a Secret containing the password for authentication. |
| `username` | `object` | username defines a key of a Secret containing the username for authentication. |

## .spec.basicAuth.password

Description
password defines a key of a Secret containing the password for authentication.

Type
`object`

Required
- `key`

| Property | Type | Description |
|----|----|----|
| `key` | `string` | The key of the secret to select from. Must be a valid secret key. |
| `name` | `string` | Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names> |
| `optional` | `boolean` | Specify whether the Secret or its key must be defined |

## .spec.basicAuth.username

Description
username defines a key of a Secret containing the username for authentication.

Type
`object`

Required
- `key`

| Property | Type | Description |
|----|----|----|
| `key` | `string` | The key of the secret to select from. Must be a valid secret key. |
| `name` | `string` | Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names> |
| `optional` | `boolean` | Specify whether the Secret or its key must be defined |

## .spec.bearerTokenSecret

Description
bearerTokenSecret defines a key of a Secret containing the bearer token used by the client for authentication. The secret needs to be in the same namespace as the custom resource and readable by the Prometheus Operator.

Cannot be set at the same time as `authorization`, `basicAuth` or `oauth2`.

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

## .spec.metricRelabelings

Description
metricRelabelings defines the RelabelConfig to apply to samples before ingestion.

Type
`array`

## .spec.metricRelabelings\[\]

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
<td style="text-align: left;"><p>action to perform based on the regex matching.</p>
<p><code>Uppercase</code> and <code>Lowercase</code> actions require Prometheus &gt;= v2.36.0. <code>DropEqual</code> and <code>KeepEqual</code> actions require Prometheus &gt;= v2.41.0.</p>
<p>Default: "Replace"</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>modulus</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p>modulus to take of the hash of the source label values.</p>
<p>Only applicable when the action is <code>HashMod</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>regex</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>regex defines the regular expression against which the extracted value is matched.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>replacement</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>replacement value against which a Replace action is performed if the regular expression matches.</p>
<p>Regex capture groups are available.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>separator</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>separator defines the string between concatenated SourceLabels.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>sourceLabels</code></p></td>
<td style="text-align: left;"><p><code>array (string)</code></p></td>
<td style="text-align: left;"><p>sourceLabels defines the source labels select values from existing labels. Their content is concatenated using the configured Separator and matched against the configured regular expression.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>targetLabel</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>targetLabel defines the label to which the resulting string is written in a replacement.</p>
<p>It is mandatory for <code>Replace</code>, <code>HashMod</code>, <code>Lowercase</code>, <code>Uppercase</code>, <code>KeepEqual</code> and <code>DropEqual</code> actions.</p>
<p>Regex capture groups are available.</p></td>
</tr>
</tbody>
</table>

## .spec.oauth2

Description
oauth2 defines the OAuth2 settings used by the client.

It requires Prometheus \>= 2.27.0.

Cannot be set at the same time as `authorization`, `basicAuth` or `bearerTokenSecret`.

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
<td style="text-align: left;"><p>clientId defines a key of a Secret or ConfigMap containing the OAuth2 client’s ID.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>clientSecret</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>clientSecret defines a key of a Secret containing the OAuth2 client’s secret.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>endpointParams</code></p></td>
<td style="text-align: left;"><p><code>object (string)</code></p></td>
<td style="text-align: left;"><p>endpointParams configures the HTTP parameters to append to the token URL.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>noProxy</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>noProxy defines a comma-separated string that can contain IPs, CIDR notation, domain names that should be excluded from proxying. IP and domain names can contain port numbers.</p>
<p>It requires Prometheus &gt;= v2.43.0, Alertmanager &gt;= v0.25.0 or Thanos &gt;= v0.32.0.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>proxyConnectHeader</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>proxyConnectHeader optionally specifies headers to send to proxies during CONNECT requests.</p>
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
<td style="text-align: left;"><p>proxyFromEnvironment defines whether to use the proxy configuration defined by environment variables (HTTP_PROXY, HTTPS_PROXY, and NO_PROXY).</p>
<p>It requires Prometheus &gt;= v2.43.0, Alertmanager &gt;= v0.25.0 or Thanos &gt;= v0.32.0.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>proxyUrl</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>proxyUrl defines the HTTP proxy server to use.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>scopes</code></p></td>
<td style="text-align: left;"><p><code>array (string)</code></p></td>
<td style="text-align: left;"><p>scopes defines the OAuth2 scopes used for the token request.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>tlsConfig</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>tlsConfig defines the TLS configuration to use when connecting to the OAuth2 server. It requires Prometheus &gt;= v2.43.0.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>tokenUrl</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>tokenUrl defines the URL to fetch the token from.</p></td>
</tr>
</tbody>
</table>

## .spec.oauth2.clientId

Description
clientId defines a key of a Secret or ConfigMap containing the OAuth2 client’s ID.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `configMap` | `object` | configMap defines the ConfigMap containing data to use for the targets. |
| `secret` | `object` | secret defines the Secret containing data to use for the targets. |

## .spec.oauth2.clientId.configMap

Description
configMap defines the ConfigMap containing data to use for the targets.

Type
`object`

Required
- `key`

| Property | Type | Description |
|----|----|----|
| `key` | `string` | The key to select. |
| `name` | `string` | Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names> |
| `optional` | `boolean` | Specify whether the ConfigMap or its key must be defined |

## .spec.oauth2.clientId.secret

Description
secret defines the Secret containing data to use for the targets.

Type
`object`

Required
- `key`

| Property | Type | Description |
|----|----|----|
| `key` | `string` | The key of the secret to select from. Must be a valid secret key. |
| `name` | `string` | Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names> |
| `optional` | `boolean` | Specify whether the Secret or its key must be defined |

## .spec.oauth2.clientSecret

Description
clientSecret defines a key of a Secret containing the OAuth2 client’s secret.

Type
`object`

Required
- `key`

| Property | Type | Description |
|----|----|----|
| `key` | `string` | The key of the secret to select from. Must be a valid secret key. |
| `name` | `string` | Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names> |
| `optional` | `boolean` | Specify whether the Secret or its key must be defined |

## .spec.oauth2.proxyConnectHeader

Description
proxyConnectHeader optionally specifies headers to send to proxies during CONNECT requests.

It requires Prometheus \>= v2.43.0, Alertmanager \>= v0.25.0 or Thanos \>= v0.32.0.

Type
`object`

## .spec.oauth2.proxyConnectHeader{}

Description

Type
`array`

## .spec.oauth2.proxyConnectHeader{}\[\]

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

## .spec.oauth2.tlsConfig

Description
tlsConfig defines the TLS configuration to use when connecting to the OAuth2 server. It requires Prometheus \>= v2.43.0.

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
<td style="text-align: left;"><p>ca defines the Certificate authority used when verifying server certificates.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>cert</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>cert defines the Client certificate to present when doing client-authentication.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>insecureSkipVerify</code></p></td>
<td style="text-align: left;"><p><code>boolean</code></p></td>
<td style="text-align: left;"><p>insecureSkipVerify defines how to disable target certificate validation.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>keySecret</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>keySecret defines the Secret containing the client key file for the targets.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>maxVersion</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>maxVersion defines the maximum acceptable TLS version.</p>
<p>It requires Prometheus &gt;= v2.41.0 or Thanos &gt;= v0.31.0.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>minVersion</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>minVersion defines the minimum acceptable TLS version.</p>
<p>It requires Prometheus &gt;= v2.35.0 or Thanos &gt;= v0.28.0.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>serverName</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>serverName is used to verify the hostname for the targets.</p></td>
</tr>
</tbody>
</table>

## .spec.oauth2.tlsConfig.ca

Description
ca defines the Certificate authority used when verifying server certificates.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `configMap` | `object` | configMap defines the ConfigMap containing data to use for the targets. |
| `secret` | `object` | secret defines the Secret containing data to use for the targets. |

## .spec.oauth2.tlsConfig.ca.configMap

Description
configMap defines the ConfigMap containing data to use for the targets.

Type
`object`

Required
- `key`

| Property | Type | Description |
|----|----|----|
| `key` | `string` | The key to select. |
| `name` | `string` | Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names> |
| `optional` | `boolean` | Specify whether the ConfigMap or its key must be defined |

## .spec.oauth2.tlsConfig.ca.secret

Description
secret defines the Secret containing data to use for the targets.

Type
`object`

Required
- `key`

| Property | Type | Description |
|----|----|----|
| `key` | `string` | The key of the secret to select from. Must be a valid secret key. |
| `name` | `string` | Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names> |
| `optional` | `boolean` | Specify whether the Secret or its key must be defined |

## .spec.oauth2.tlsConfig.cert

Description
cert defines the Client certificate to present when doing client-authentication.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `configMap` | `object` | configMap defines the ConfigMap containing data to use for the targets. |
| `secret` | `object` | secret defines the Secret containing data to use for the targets. |

## .spec.oauth2.tlsConfig.cert.configMap

Description
configMap defines the ConfigMap containing data to use for the targets.

Type
`object`

Required
- `key`

| Property | Type | Description |
|----|----|----|
| `key` | `string` | The key to select. |
| `name` | `string` | Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names> |
| `optional` | `boolean` | Specify whether the ConfigMap or its key must be defined |

## .spec.oauth2.tlsConfig.cert.secret

Description
secret defines the Secret containing data to use for the targets.

Type
`object`

Required
- `key`

| Property | Type | Description |
|----|----|----|
| `key` | `string` | The key of the secret to select from. Must be a valid secret key. |
| `name` | `string` | Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names> |
| `optional` | `boolean` | Specify whether the Secret or its key must be defined |

## .spec.oauth2.tlsConfig.keySecret

Description
keySecret defines the Secret containing the client key file for the targets.

Type
`object`

Required
- `key`

| Property | Type | Description |
|----|----|----|
| `key` | `string` | The key of the secret to select from. Must be a valid secret key. |
| `name` | `string` | Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names> |
| `optional` | `boolean` | Specify whether the Secret or its key must be defined |

## .spec.params

Description
params defines the list of HTTP query parameters for the scrape. Please note that the `.spec.module` field takes precedence over the `module` parameter from this list when both are defined. The module name must be added using Module under ProbeSpec.

Type
`array`

## .spec.params\[\]

Description
ProbeParam defines specification of extra parameters for a Probe.

Type
`object`

Required
- `name`

| Property | Type             | Description                         |
|----------|------------------|-------------------------------------|
| `name`   | `string`         | name defines the parameter name     |
| `values` | `array (string)` | values defines the parameter values |

## .spec.prober

Description
prober defines the specification for the prober to use for probing targets. The prober.URL parameter is required. Targets cannot be probed if left empty.

Type
`object`

Required
- `url`

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
<td style="text-align: left;"><p><code>noProxy</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>noProxy defines a comma-separated string that can contain IPs, CIDR notation, domain names that should be excluded from proxying. IP and domain names can contain port numbers.</p>
<p>It requires Prometheus &gt;= v2.43.0, Alertmanager &gt;= v0.25.0 or Thanos &gt;= v0.32.0.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>path</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>path to collect metrics from. Defaults to <code>/probe</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>proxyConnectHeader</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>proxyConnectHeader optionally specifies headers to send to proxies during CONNECT requests.</p>
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
<td style="text-align: left;"><p>proxyFromEnvironment defines whether to use the proxy configuration defined by environment variables (HTTP_PROXY, HTTPS_PROXY, and NO_PROXY).</p>
<p>It requires Prometheus &gt;= v2.43.0, Alertmanager &gt;= v0.25.0 or Thanos &gt;= v0.32.0.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>proxyUrl</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>proxyUrl defines the HTTP proxy server to use.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>scheme</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>scheme defines the HTTP scheme to use when scraping the prober.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>url</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>url defines the address of the prober.</p>
<p>Unlike what the name indicates, the value should be in the form of <code>address:port</code> without any scheme which should be specified in the <code>scheme</code> field.</p></td>
</tr>
</tbody>
</table>

## .spec.prober.proxyConnectHeader

Description
proxyConnectHeader optionally specifies headers to send to proxies during CONNECT requests.

It requires Prometheus \>= v2.43.0, Alertmanager \>= v0.25.0 or Thanos \>= v0.32.0.

Type
`object`

## .spec.prober.proxyConnectHeader{}

Description

Type
`array`

## .spec.prober.proxyConnectHeader{}\[\]

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

## .spec.targets

Description
targets defines a set of static or dynamically discovered targets to probe.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `ingress` | `object` | ingress defines the Ingress objects to probe and the relabeling configuration. If `staticConfig` is also defined, `staticConfig` takes precedence. |
| `staticConfig` | `object` | staticConfig defines the static list of targets to probe and the relabeling configuration. If `ingress` is also defined, `staticConfig` takes precedence. More info: <https://prometheus.io/docs/prometheus/latest/configuration/configuration/#static_config>. |

## .spec.targets.ingress

Description
ingress defines the Ingress objects to probe and the relabeling configuration. If `staticConfig` is also defined, `staticConfig` takes precedence.

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
<td style="text-align: left;"><p><code>namespaceSelector</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>namespaceSelector defines from which namespaces to select Ingress objects.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>relabelingConfigs</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>relabelingConfigs to apply to the label set of the target before it gets scraped. The original ingress address is available via the <code>__tmp_prometheus_ingress_address</code> label. It can be used to customize the probed URL. The original scrape job’s name is available via the <code>\__tmp_prometheus_job_name</code> label. More info: <a href="https://prometheus.io/docs/prometheus/latest/configuration/configuration/#relabel_config">https://prometheus.io/docs/prometheus/latest/configuration/configuration/#relabel_config</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>relabelingConfigs[]</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>RelabelConfig allows dynamic rewriting of the label set for targets, alerts, scraped samples and remote write samples.</p>
<p>More info: <a href="https://prometheus.io/docs/prometheus/latest/configuration/configuration/#relabel_config">https://prometheus.io/docs/prometheus/latest/configuration/configuration/#relabel_config</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>selector</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>selector to select the Ingress objects.</p></td>
</tr>
</tbody>
</table>

## .spec.targets.ingress.namespaceSelector

Description
namespaceSelector defines from which namespaces to select Ingress objects.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `any` | `boolean` | any defines the boolean describing whether all namespaces are selected in contrast to a list restricting them. |
| `matchNames` | `array (string)` | matchNames defines the list of namespace names to select from. |

## .spec.targets.ingress.relabelingConfigs

Description
relabelingConfigs to apply to the label set of the target before it gets scraped. The original ingress address is available via the `__tmp_prometheus_ingress_address` label. It can be used to customize the probed URL. The original scrape job’s name is available via the `\__tmp_prometheus_job_name` label. More info: <https://prometheus.io/docs/prometheus/latest/configuration/configuration/#relabel_config>

Type
`array`

## .spec.targets.ingress.relabelingConfigs\[\]

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
<td style="text-align: left;"><p>action to perform based on the regex matching.</p>
<p><code>Uppercase</code> and <code>Lowercase</code> actions require Prometheus &gt;= v2.36.0. <code>DropEqual</code> and <code>KeepEqual</code> actions require Prometheus &gt;= v2.41.0.</p>
<p>Default: "Replace"</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>modulus</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p>modulus to take of the hash of the source label values.</p>
<p>Only applicable when the action is <code>HashMod</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>regex</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>regex defines the regular expression against which the extracted value is matched.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>replacement</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>replacement value against which a Replace action is performed if the regular expression matches.</p>
<p>Regex capture groups are available.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>separator</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>separator defines the string between concatenated SourceLabels.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>sourceLabels</code></p></td>
<td style="text-align: left;"><p><code>array (string)</code></p></td>
<td style="text-align: left;"><p>sourceLabels defines the source labels select values from existing labels. Their content is concatenated using the configured Separator and matched against the configured regular expression.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>targetLabel</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>targetLabel defines the label to which the resulting string is written in a replacement.</p>
<p>It is mandatory for <code>Replace</code>, <code>HashMod</code>, <code>Lowercase</code>, <code>Uppercase</code>, <code>KeepEqual</code> and <code>DropEqual</code> actions.</p>
<p>Regex capture groups are available.</p></td>
</tr>
</tbody>
</table>

## .spec.targets.ingress.selector

Description
selector to select the Ingress objects.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `matchExpressions` | `array` | matchExpressions is a list of label selector requirements. The requirements are ANDed. |
| `matchExpressions[]` | `object` | A label selector requirement is a selector that contains values, a key, and an operator that relates the key and values. |
| `matchLabels` | `object (string)` | matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed. |

## .spec.targets.ingress.selector.matchExpressions

Description
matchExpressions is a list of label selector requirements. The requirements are ANDed.

Type
`array`

## .spec.targets.ingress.selector.matchExpressions\[\]

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

## .spec.targets.staticConfig

Description
staticConfig defines the static list of targets to probe and the relabeling configuration. If `ingress` is also defined, `staticConfig` takes precedence. More info: <https://prometheus.io/docs/prometheus/latest/configuration/configuration/#static_config>.

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
<td style="text-align: left;"><p><code>labels</code></p></td>
<td style="text-align: left;"><p><code>object (string)</code></p></td>
<td style="text-align: left;"><p>labels defines all labels assigned to all metrics scraped from the targets.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>relabelingConfigs</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>relabelingConfigs defines relabelings to be apply to the label set of the targets before it gets scraped. More info: <a href="https://prometheus.io/docs/prometheus/latest/configuration/configuration/#relabel_config">https://prometheus.io/docs/prometheus/latest/configuration/configuration/#relabel_config</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>relabelingConfigs[]</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>RelabelConfig allows dynamic rewriting of the label set for targets, alerts, scraped samples and remote write samples.</p>
<p>More info: <a href="https://prometheus.io/docs/prometheus/latest/configuration/configuration/#relabel_config">https://prometheus.io/docs/prometheus/latest/configuration/configuration/#relabel_config</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>static</code></p></td>
<td style="text-align: left;"><p><code>array (string)</code></p></td>
<td style="text-align: left;"><p>static defines the list of hosts to probe.</p></td>
</tr>
</tbody>
</table>

## .spec.targets.staticConfig.relabelingConfigs

Description
relabelingConfigs defines relabelings to be apply to the label set of the targets before it gets scraped. More info: <https://prometheus.io/docs/prometheus/latest/configuration/configuration/#relabel_config>

Type
`array`

## .spec.targets.staticConfig.relabelingConfigs\[\]

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
<td style="text-align: left;"><p>action to perform based on the regex matching.</p>
<p><code>Uppercase</code> and <code>Lowercase</code> actions require Prometheus &gt;= v2.36.0. <code>DropEqual</code> and <code>KeepEqual</code> actions require Prometheus &gt;= v2.41.0.</p>
<p>Default: "Replace"</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>modulus</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p>modulus to take of the hash of the source label values.</p>
<p>Only applicable when the action is <code>HashMod</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>regex</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>regex defines the regular expression against which the extracted value is matched.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>replacement</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>replacement value against which a Replace action is performed if the regular expression matches.</p>
<p>Regex capture groups are available.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>separator</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>separator defines the string between concatenated SourceLabels.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>sourceLabels</code></p></td>
<td style="text-align: left;"><p><code>array (string)</code></p></td>
<td style="text-align: left;"><p>sourceLabels defines the source labels select values from existing labels. Their content is concatenated using the configured Separator and matched against the configured regular expression.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>targetLabel</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>targetLabel defines the label to which the resulting string is written in a replacement.</p>
<p>It is mandatory for <code>Replace</code>, <code>HashMod</code>, <code>Lowercase</code>, <code>Uppercase</code>, <code>KeepEqual</code> and <code>DropEqual</code> actions.</p>
<p>Regex capture groups are available.</p></td>
</tr>
</tbody>
</table>

## .spec.tlsConfig

Description
tlsConfig defines the TLS configuration used by the client.

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
<td style="text-align: left;"><p>ca defines the Certificate authority used when verifying server certificates.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>cert</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>cert defines the Client certificate to present when doing client-authentication.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>insecureSkipVerify</code></p></td>
<td style="text-align: left;"><p><code>boolean</code></p></td>
<td style="text-align: left;"><p>insecureSkipVerify defines how to disable target certificate validation.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>keySecret</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>keySecret defines the Secret containing the client key file for the targets.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>maxVersion</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>maxVersion defines the maximum acceptable TLS version.</p>
<p>It requires Prometheus &gt;= v2.41.0 or Thanos &gt;= v0.31.0.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>minVersion</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>minVersion defines the minimum acceptable TLS version.</p>
<p>It requires Prometheus &gt;= v2.35.0 or Thanos &gt;= v0.28.0.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>serverName</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>serverName is used to verify the hostname for the targets.</p></td>
</tr>
</tbody>
</table>

## .spec.tlsConfig.ca

Description
ca defines the Certificate authority used when verifying server certificates.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `configMap` | `object` | configMap defines the ConfigMap containing data to use for the targets. |
| `secret` | `object` | secret defines the Secret containing data to use for the targets. |

## .spec.tlsConfig.ca.configMap

Description
configMap defines the ConfigMap containing data to use for the targets.

Type
`object`

Required
- `key`

| Property | Type | Description |
|----|----|----|
| `key` | `string` | The key to select. |
| `name` | `string` | Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names> |
| `optional` | `boolean` | Specify whether the ConfigMap or its key must be defined |

## .spec.tlsConfig.ca.secret

Description
secret defines the Secret containing data to use for the targets.

Type
`object`

Required
- `key`

| Property | Type | Description |
|----|----|----|
| `key` | `string` | The key of the secret to select from. Must be a valid secret key. |
| `name` | `string` | Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names> |
| `optional` | `boolean` | Specify whether the Secret or its key must be defined |

## .spec.tlsConfig.cert

Description
cert defines the Client certificate to present when doing client-authentication.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `configMap` | `object` | configMap defines the ConfigMap containing data to use for the targets. |
| `secret` | `object` | secret defines the Secret containing data to use for the targets. |

## .spec.tlsConfig.cert.configMap

Description
configMap defines the ConfigMap containing data to use for the targets.

Type
`object`

Required
- `key`

| Property | Type | Description |
|----|----|----|
| `key` | `string` | The key to select. |
| `name` | `string` | Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names> |
| `optional` | `boolean` | Specify whether the ConfigMap or its key must be defined |

## .spec.tlsConfig.cert.secret

Description
secret defines the Secret containing data to use for the targets.

Type
`object`

Required
- `key`

| Property | Type | Description |
|----|----|----|
| `key` | `string` | The key of the secret to select from. Must be a valid secret key. |
| `name` | `string` | Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names> |
| `optional` | `boolean` | Specify whether the Secret or its key must be defined |

## .spec.tlsConfig.keySecret

Description
keySecret defines the Secret containing the client key file for the targets.

Type
`object`

Required
- `key`

| Property | Type | Description |
|----|----|----|
| `key` | `string` | The key of the secret to select from. Must be a valid secret key. |
| `name` | `string` | Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names> |
| `optional` | `boolean` | Specify whether the Secret or its key must be defined |

## .status

Description
status defines the status subresource. It is under active development and is updated only when the "StatusForConfigurationResources" feature gate is enabled.

Most recent observed status of the Probe. Read-only. More info: <https://github.com/kubernetes/community/blob/master/contributors/devel/sig-architecture/api-conventions.md#spec-and-status>

Type
`object`

| Property | Type | Description |
|----|----|----|
| `bindings` | `array` | bindings defines the list of workload resources (Prometheus, PrometheusAgent, ThanosRuler or Alertmanager) which select the configuration resource. |
| `bindings[]` | `object` | WorkloadBinding is a link between a configuration resource and a workload resource. |

## .status.bindings

Description
bindings defines the list of workload resources (Prometheus, PrometheusAgent, ThanosRuler or Alertmanager) which select the configuration resource.

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
| `conditions` | `array` | conditions defines the current state of the configuration resource when bound to the referenced Workload object. |
| `conditions[]` | `object` | ConfigResourceCondition describes the status of configuration resources linked to Prometheus, PrometheusAgent, Alertmanager or ThanosRuler. |
| `group` | `string` | group defines the group of the referenced resource. |
| `name` | `string` | name defines the name of the referenced object. |
| `namespace` | `string` | namespace defines the namespace of the referenced object. |
| `resource` | `string` | resource defines the type of resource being referenced (e.g. Prometheus, PrometheusAgent, ThanosRuler or Alertmanager). |

## .status.bindings\[\].conditions

Description
conditions defines the current state of the configuration resource when bound to the referenced Workload object.

Type
`array`

## .status.bindings\[\].conditions\[\]

Description
ConfigResourceCondition describes the status of configuration resources linked to Prometheus, PrometheusAgent, Alertmanager or ThanosRuler.

Type
`object`

Required
- `lastTransitionTime`

- `status`

- `type`

| Property | Type | Description |
|----|----|----|
| `lastTransitionTime` | `string` | lastTransitionTime defines the time of the last update to the current status property. |
| `message` | `string` | message defines the human-readable message indicating details for the condition’s last transition. |
| `observedGeneration` | `integer` | observedGeneration defines the .metadata.generation that the condition was set based upon. For instance, if `.metadata.generation` is currently 12, but the `.status.conditions[].observedGeneration` is 9, the condition is out of date with respect to the current state of the object. |
| `reason` | `string` | reason for the condition’s last transition. |
| `status` | `string` | status of the condition. |
| `type` | `string` | type of the condition being reported. Currently, only "Accepted" is supported. |

# API endpoints

The following API endpoints are available:

- `/apis/monitoring.coreos.com/v1/probes`

  - `GET`: list objects of kind Probe

- `/apis/monitoring.coreos.com/v1/namespaces/{namespace}/probes`

  - `DELETE`: delete collection of Probe

  - `GET`: list objects of kind Probe

  - `POST`: create a Probe

- `/apis/monitoring.coreos.com/v1/namespaces/{namespace}/probes/{name}`

  - `DELETE`: delete a Probe

  - `GET`: read the specified Probe

  - `PATCH`: partially update the specified Probe

  - `PUT`: replace the specified Probe

- `/apis/monitoring.coreos.com/v1/namespaces/{namespace}/probes/{name}/status`

  - `GET`: read status of the specified Probe

  - `PATCH`: partially update status of the specified Probe

  - `PUT`: replace status of the specified Probe

## /apis/monitoring.coreos.com/v1/probes

HTTP method
`GET`

Description
list objects of kind Probe

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ProbeList`](../objects/index.md#com-coreos-monitoring-v1-ProbeList) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/monitoring.coreos.com/v1/namespaces/{namespace}/probes

HTTP method
`DELETE`

Description
delete collection of Probe

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Status`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`GET`

Description
list objects of kind Probe

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ProbeList`](../objects/index.md#com-coreos-monitoring-v1-ProbeList) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`POST`

Description
create a Probe

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`Probe`](probe-monitoring-coreos-com-v1.md#probe-monitoring-coreos-com-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Probe`](probe-monitoring-coreos-com-v1.md#probe-monitoring-coreos-com-v1) schema |
| 201 - Created | [`Probe`](probe-monitoring-coreos-com-v1.md#probe-monitoring-coreos-com-v1) schema |
| 202 - Accepted | [`Probe`](probe-monitoring-coreos-com-v1.md#probe-monitoring-coreos-com-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/monitoring.coreos.com/v1/namespaces/{namespace}/probes/{name}

| Parameter | Type     | Description       |
|-----------|----------|-------------------|
| `name`    | `string` | name of the Probe |

Global path parameters

HTTP method
`DELETE`

Description
delete a Probe

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
read the specified Probe

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Probe`](probe-monitoring-coreos-com-v1.md#probe-monitoring-coreos-com-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PATCH`

Description
partially update the specified Probe

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Probe`](probe-monitoring-coreos-com-v1.md#probe-monitoring-coreos-com-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PUT`

Description
replace the specified Probe

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`Probe`](probe-monitoring-coreos-com-v1.md#probe-monitoring-coreos-com-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Probe`](probe-monitoring-coreos-com-v1.md#probe-monitoring-coreos-com-v1) schema |
| 201 - Created | [`Probe`](probe-monitoring-coreos-com-v1.md#probe-monitoring-coreos-com-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/monitoring.coreos.com/v1/namespaces/{namespace}/probes/{name}/status

| Parameter | Type     | Description       |
|-----------|----------|-------------------|
| `name`    | `string` | name of the Probe |

Global path parameters

HTTP method
`GET`

Description
read status of the specified Probe

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Probe`](probe-monitoring-coreos-com-v1.md#probe-monitoring-coreos-com-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PATCH`

Description
partially update status of the specified Probe

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Probe`](probe-monitoring-coreos-com-v1.md#probe-monitoring-coreos-com-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PUT`

Description
replace status of the specified Probe

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`Probe`](probe-monitoring-coreos-com-v1.md#probe-monitoring-coreos-com-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Probe`](probe-monitoring-coreos-com-v1.md#probe-monitoring-coreos-com-v1) schema |
| 201 - Created | [`Probe`](probe-monitoring-coreos-com-v1.md#probe-monitoring-coreos-com-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses
