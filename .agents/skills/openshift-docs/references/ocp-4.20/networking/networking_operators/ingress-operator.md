<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

The Ingress Operator implements the `IngressController` API and is the component responsible for enabling external access to OpenShift Container Platform cluster services.

# OpenShift Container Platform Ingress Operator

When you create your OpenShift Container Platform cluster, pods and services running on the cluster are each allocated their own IP addresses. The IP addresses are accessible to other pods and services running nearby but are not accessible to outside clients.

The Ingress Operator makes it possible for external clients to access your service by deploying and managing one or more HAProxy-based [Ingress Controllers](https://kubernetes.io/docs/concepts/services-networking/ingress-controllers/) to handle routing. You can use the Ingress Operator to route traffic by specifying OpenShift Container Platform `Route` and Kubernetes `Ingress` resources. Configurations within the Ingress Controller, such as the ability to define `endpointPublishingStrategy` type and internal load balancing, provide ways to publish Ingress Controller endpoints.

# The Ingress configuration asset

The installation program generates an asset with an `Ingress` resource in the `config.openshift.io` API group, `cluster-ingress-02-config.yml`.

<div class="formalpara">

<div class="title">

YAML Definition of the `Ingress` resource

</div>

``` yaml
apiVersion: config.openshift.io/v1
kind: Ingress
metadata:
  name: cluster
spec:
  domain: apps.openshiftdemos.com
```

</div>

The installation program stores this asset in the `cluster-ingress-02-config.yml` file in the `manifests/` directory. This `Ingress` resource defines the cluster-wide configuration for Ingress. This Ingress configuration is used as follows:

- The Ingress Operator uses the domain from the cluster Ingress configuration as the domain for the default Ingress Controller.

- The OpenShift API Server Operator uses the domain from the cluster Ingress configuration. This domain is also used when generating a default host for a `Route` resource that does not specify an explicit host.

# Ingress Controller configuration parameters

The `IngressController` custom resource (CR) includes optional configuration parameters that you can configure to meet specific needs for your organization.

<table>
<colgroup>
<col style="width: 27%" />
<col style="width: 72%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Parameter</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>domain</code></p></td>
<td style="text-align: left;"><p><code>domain</code> is a DNS name serviced by the Ingress Controller and is used to configure multiple features:</p>
<ul>
<li><p>For the <code>LoadBalancerService</code> endpoint publishing strategy, <code>domain</code> is used to configure DNS records. See <code>endpointPublishingStrategy</code>.</p></li>
<li><p>When using a generated default certificate, the certificate is valid for <code>domain</code> and its <code>subdomains</code>. See <code>defaultCertificate</code>.</p></li>
<li><p>The value is published to individual Route statuses so that users know where to target external DNS records.</p></li>
</ul>
<p>The <code>domain</code> value must be unique among all Ingress Controllers and cannot be updated.</p>
<p>If empty, the default value is <code>ingress.config.openshift.io/cluster</code> <code>.spec.domain</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>replicas</code></p></td>
<td style="text-align: left;"><p><code>replicas</code> is the number of Ingress Controller replicas. If not set, the default value is <code>2</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>endpointPublishingStrategy</code></p></td>
<td style="text-align: left;"><p><code>endpointPublishingStrategy</code> is used to publish the Ingress Controller endpoints to other networks, enable load balancer integrations, and provide access to other systems.</p>
<p>For cloud environments, use the <code>loadBalancer</code> field to configure the endpoint publishing strategy for your Ingress Controller.</p>
<p>On Google Cloud, AWS, and Azure you can configure the following <code>endpointPublishingStrategy</code> fields:</p>
<ul>
<li><p><code>loadBalancer.scope</code></p></li>
<li><p><code>loadBalancer.allowedSourceRanges</code></p></li>
</ul>
<p>If not set, the default value is based on <code>infrastructure.config.openshift.io/cluster</code> <code>.status.platform</code>:</p>
<ul>
<li><p>Azure: <code>LoadBalancerService</code> (with External scope)</p></li>
<li><p>Google Cloud: <code>LoadBalancerService</code> (with External scope)</p></li>
</ul>
<p>For most platforms, the <code>endpointPublishingStrategy</code> value can be updated. On Google Cloud, you can configure the following <code>endpointPublishingStrategy</code> fields:</p>
<ul>
<li><p><code>loadBalancer.scope</code></p></li>
<li><p><code>loadbalancer.providerParameters.gcp.clientAccess</code></p></li>
</ul>
<p>For non-cloud environments, such as a bare-metal platform, use the <code>NodePortService</code>, <code>HostNetwork</code>, or <code>Private</code> fields to configure the endpoint publishing strategy for your Ingress Controller.</p>
<p>If you do not set a value in one of these fields, the default value is based on binding ports specified in the <code>.status.platform</code> value in the <code>IngressController</code> CR.</p>
<p>If you need to update the <code>endpointPublishingStrategy</code> value after your cluster is deployed, you can configure the following <code>endpointPublishingStrategy</code> fields:</p>
<ul>
<li><p><code>hostNetwork.protocol</code></p></li>
<li><p><code>nodePort.protocol</code></p></li>
<li><p><code>private.protocol</code></p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>defaultCertificate</code></p></td>
<td style="text-align: left;"><p>The <code>defaultCertificate</code> value is a reference to a secret that contains the default certificate that is served by the Ingress Controller. When Routes do not specify their own certificate, <code>defaultCertificate</code> is used.</p>
<p>The secret must contain the following keys and data: * <code>tls.crt</code>: certificate file contents * <code>tls.key</code>: key file contents</p>
<p>If not set, a wildcard certificate is automatically generated and used. The certificate is valid for the Ingress Controller <code>domain</code> and <code>subdomains</code>, and the generated certificate’s CA is automatically integrated with the cluster’s trust store.</p>
<p>The in-use certificate, whether generated or user-specified, is automatically integrated with OpenShift Container Platform built-in OAuth server.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>namespaceSelector</code></p></td>
<td style="text-align: left;"><p><code>namespaceSelector</code> is used to filter the set of namespaces serviced by the Ingress Controller. This is useful for implementing shards.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>routeSelector</code></p></td>
<td style="text-align: left;"><p><code>routeSelector</code> is used to filter the set of Routes serviced by the Ingress Controller. This is useful for implementing shards.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>nodePlacement</code></p></td>
<td style="text-align: left;"><p><code>nodePlacement</code> enables explicit control over the scheduling of the Ingress Controller.</p>
<p>If not set, the defaults values are used.</p>
<div class="note">
<div class="title">
&#10;</div>
<p>The <code>nodePlacement</code> parameter includes two parts, <code>nodeSelector</code> and <code>tolerations</code>. For example:</p>
<div class="sourceCode" id="cb1"><pre class="sourceCode yaml"><code class="sourceCode yaml"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a><span class="fu">nodePlacement</span><span class="kw">:</span></span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a><span class="at"> </span><span class="fu">nodeSelector</span><span class="kw">:</span></span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a><span class="at">   </span><span class="fu">matchLabels</span><span class="kw">:</span></span>
<span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a><span class="at">     </span><span class="fu">kubernetes.io/os</span><span class="kw">:</span><span class="at"> linux</span></span>
<span id="cb1-5"><a href="#cb1-5" aria-hidden="true" tabindex="-1"></a><span class="at"> </span><span class="fu">tolerations</span><span class="kw">:</span></span>
<span id="cb1-6"><a href="#cb1-6" aria-hidden="true" tabindex="-1"></a><span class="at"> </span><span class="kw">-</span><span class="at"> </span><span class="fu">effect</span><span class="kw">:</span><span class="at"> NoSchedule</span></span>
<span id="cb1-7"><a href="#cb1-7" aria-hidden="true" tabindex="-1"></a><span class="at">   </span><span class="fu">operator</span><span class="kw">:</span><span class="at"> Exists</span></span></code></pre></div>
</div></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>tlsSecurityProfile</code></p></td>
<td style="text-align: left;"><p><code>tlsSecurityProfile</code> specifies settings for TLS connections for Ingress Controllers.</p>
<p>If not set, the default value is based on the <code>apiservers.config.openshift.io/cluster</code> resource.</p>
<p>When using the <code>Old</code>, <code>Intermediate</code>, and <code>Modern</code> profile types, the effective profile configuration is subject to change between releases. For example, given a specification to use the <code>Intermediate</code> profile deployed on release <code>X.Y.Z</code>, an upgrade to release <code>X.Y.Z+1</code> may cause a new profile configuration to be applied to the Ingress Controller, resulting in a rollout.</p>
<p>The minimum TLS version for Ingress Controllers is <code>1.1</code>, and the maximum TLS version is <code>1.3</code>.</p>
<div class="note">
<div class="title">
&#10;</div>
<p>Ciphers and the minimum TLS version of the configured security profile are reflected in the <code>TLSProfile</code> status.</p>
</div>
<div class="important">
<div class="title">
&#10;</div>
<p>The Ingress Operator converts the TLS <code>1.0</code> of an <code>Old</code> or <code>Custom</code> profile to <code>1.1</code>.</p>
</div></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>clientTLS</code></p></td>
<td style="text-align: left;"><p><code>clientTLS</code> authenticates client access to the cluster and services; as a result, mutual TLS authentication is enabled. If not set, then client TLS is not enabled.</p>
<p><code>clientTLS</code> has the required subfields, <code>spec.clientTLS.clientCertificatePolicy</code> and <code>spec.clientTLS.ClientCA</code>.</p>
<p>The <code>ClientCertificatePolicy</code> subfield accepts one of the two values: <code>Required</code> or <code>Optional</code>. The <code>ClientCA</code> subfield specifies a config map that is in the openshift-config namespace. The config map should contain a CA certificate bundle.</p>
<p>The <code>AllowedSubjectPatterns</code> is an optional value that specifies a list of regular expressions, which are matched against the distinguished name on a valid client certificate to filter requests. The regular expressions must use PCRE syntax. At least one pattern must match a client certificate’s distinguished name; otherwise, the Ingress Controller rejects the certificate and denies the connection. If not specified, the Ingress Controller does not reject certificates based on the distinguished name.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>routeAdmission</code></p></td>
<td style="text-align: left;"><p><code>routeAdmission</code> defines a policy for handling new route claims, such as allowing or denying claims across namespaces.</p>
<p><code>namespaceOwnership</code> describes how hostname claims across namespaces should be handled. The default is <code>Strict</code>.</p>
<ul>
<li><p><code>Strict</code>: does not allow routes to claim the same hostname across namespaces.</p></li>
<li><p><code>InterNamespaceAllowed</code>: allows routes to claim different paths of the same hostname across namespaces.</p></li>
</ul>
<p><code>wildcardPolicy</code> describes how routes with wildcard policies are handled by the Ingress Controller.</p>
<ul>
<li><p><code>WildcardsAllowed</code>: Indicates routes with any wildcard policy are admitted by the Ingress Controller.</p></li>
<li><p><code>WildcardsDisallowed</code>: Indicates only routes with a wildcard policy of <code>None</code> are admitted by the Ingress Controller. Updating <code>wildcardPolicy</code> from <code>WildcardsAllowed</code> to <code>WildcardsDisallowed</code> causes admitted routes with a wildcard policy of <code>Subdomain</code> to stop working. These routes must be recreated to a wildcard policy of <code>None</code> to be readmitted by the Ingress Controller. <code>WildcardsDisallowed</code> is the default setting.</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>IngressControllerLogging</code></p></td>
<td style="text-align: left;"><p><code>logging</code> defines parameters for what is logged where. If this field is empty, operational logs are enabled but access logs are disabled.</p>
<ul>
<li><p><code>access</code> describes how client requests are logged. If this field is empty, access logging is disabled.</p>
<ul>
<li><p><code>destination</code> describes a destination for log messages.</p>
<ul>
<li><p><code>type</code> is the type of destination for logs:</p>
<ul>
<li><p><code>Container</code> specifies that logs should go to a sidecar container. The Ingress Operator configures the container, named <strong>logs</strong>, on the Ingress Controller pod and configures the Ingress Controller to write logs to the container. The expectation is that the administrator configures a custom logging solution that reads logs from this container. Using container logs means that logs may be dropped if the rate of logs exceeds the container runtime capacity or the custom logging solution capacity.</p></li>
<li><p><code>Syslog</code> specifies that logs are sent to a Syslog endpoint. The administrator must specify an endpoint that can receive Syslog messages. The expectation is that the administrator has configured a custom Syslog instance.</p></li>
</ul></li>
<li><p><code>container</code> describes parameters for the <code>Container</code> logging destination type. Currently there are no parameters for container logging, so this field must be empty.</p></li>
<li><p><code>syslog</code> describes parameters for the <code>Syslog</code> logging destination type:</p>
<ul>
<li><p><code>address</code> is the IP address of the syslog endpoint that receives log messages.</p></li>
<li><p><code>port</code> is the UDP port number of the syslog endpoint that receives log messages.</p></li>
<li><p><code>maxLength</code> is the maximum length of the syslog message. It must be between <code>480</code> and <code>4096</code> bytes. If this field is empty, the maximum length is set to the default value of <code>1024</code> bytes.</p></li>
<li><p><code>facility</code> specifies the syslog facility of log messages. If this field is empty, the facility is <code>local1</code>. Otherwise, it must specify a valid syslog facility: <code>kern</code>, <code>user</code>, <code>mail</code>, <code>daemon</code>, <code>auth</code>, <code>syslog</code>, <code>lpr</code>, <code>news</code>, <code>uucp</code>, <code>cron</code>, <code>auth2</code>, <code>ftp</code>, <code>ntp</code>, <code>audit</code>, <code>alert</code>, <code>cron2</code>, <code>local0</code>, <code>local1</code>, <code>local2</code>, <code>local3</code>. <code>local4</code>, <code>local5</code>, <code>local6</code>, or <code>local7</code>.</p></li>
</ul></li>
</ul></li>
<li><p><code>httpLogFormat</code> specifies the format of the log message for an HTTP request. If this field is empty, log messages use the implementation’s default HTTP log format. For HAProxy’s default HTTP log format, see <a href="http://cbonte.github.io/haproxy-dconv/2.0/configuration.html#8.2.3">the HAProxy documentation</a>.</p></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>httpHeaders</code></p></td>
<td style="text-align: left;"><p><code>httpHeaders</code> defines the policy for HTTP headers.</p>
<p>By setting the <code>forwardedHeaderPolicy</code> for the <code>IngressControllerHTTPHeaders</code>, you specify when and how the Ingress Controller sets the <code>Forwarded</code>, <code>X-Forwarded-For</code>, <code>X-Forwarded-Host</code>, <code>X-Forwarded-Port</code>, <code>X-Forwarded-Proto</code>, and <code>X-Forwarded-Proto-Version</code> HTTP headers.</p>
<p>By default, the policy is set to <code>Append</code>.</p>
<ul>
<li><p><code>Append</code> specifies that the Ingress Controller appends the headers, preserving any existing headers.</p></li>
<li><p><code>Replace</code> specifies that the Ingress Controller sets the headers, removing any existing headers.</p></li>
<li><p><code>IfNone</code> specifies that the Ingress Controller sets the headers if they are not already set.</p></li>
<li><p><code>Never</code> specifies that the Ingress Controller never sets the headers, preserving any existing headers.</p></li>
</ul>
<p>By setting <code>headerNameCaseAdjustments</code>, you can specify case adjustments that can be applied to HTTP header names. Each adjustment is specified as an HTTP header name with the desired capitalization. For example, specifying <code>X-Forwarded-For</code> indicates that the <code>x-forwarded-for</code> HTTP header should be adjusted to have the specified capitalization.</p>
<p>These adjustments are only applied to cleartext, edge-terminated, and re-encrypt routes, and only when using HTTP/1.</p>
<p>For request headers, these adjustments are applied only for routes that have the <code>haproxy.router.openshift.io/h1-adjust-case=true</code> annotation. For response headers, these adjustments are applied to all HTTP responses. If this field is empty, no request headers are adjusted.</p>
<p><code>actions</code> specifies options for performing certain actions on headers. Headers cannot be set or deleted for TLS passthrough connections. The <code>actions</code> field has additional subfields <code>spec.httpHeader.actions.response</code> and <code>spec.httpHeader.actions.request</code>:</p>
<ul>
<li><p>The <code>response</code> subfield specifies a list of HTTP response headers to set or delete.</p></li>
<li><p>The <code>request</code> subfield specifies a list of HTTP request headers to set or delete.</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>httpCompression</code></p></td>
<td style="text-align: left;"><p><code>httpCompression</code> defines the policy for HTTP traffic compression.</p>
<ul>
<li><p><code>mimeTypes</code> defines a list of MIME types to which compression should be applied. For example, <code>text/css; charset=utf-8</code>, <code>text/html</code>, <code>text/*</code>, <code>image/svg+xml</code>, <code>application/octet-stream</code>, <code>X-custom/customsub</code>, using the format pattern, <code>type/subtype; [;attribute=value]</code>. The <code>types</code> are: application, image, message, multipart, text, video, or a custom type prefaced by <code>X-</code>; e.g. To see the full notation for MIME types and subtypes, see <a href="https://datatracker.ietf.org/doc/html/rfc1341#page-7">RFC1341</a></p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>httpErrorCodePages</code></p></td>
<td style="text-align: left;"><p><code>httpErrorCodePages</code> specifies custom HTTP error code response pages. By default, an IngressController uses error pages built into the IngressController image.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>httpCaptureCookies</code></p></td>
<td style="text-align: left;"><p><code>httpCaptureCookies</code> specifies HTTP cookies that you want to capture in access logs. If the <code>httpCaptureCookies</code> field is empty, the access logs do not capture the cookies.</p>
<p>For any cookie that you want to capture, the following parameters must be in your <code>IngressController</code> configuration:</p>
<ul>
<li><p><code>name</code> specifies the name of the cookie.</p></li>
<li><p><code>maxLength</code> specifies tha maximum length of the cookie.</p></li>
<li><p><code>matchType</code> specifies if the field <code>name</code> of the cookie exactly matches the capture cookie setting or is a prefix of the capture cookie setting. The <code>matchType</code> field uses the <code>Exact</code> and <code>Prefix</code> parameters.</p></li>
</ul>
<p>For example:</p>
<div class="sourceCode" id="cb2"><pre class="sourceCode yaml"><code class="sourceCode yaml"><span id="cb2-1"><a href="#cb2-1" aria-hidden="true" tabindex="-1"></a><span class="at">  </span><span class="fu">httpCaptureCookies</span><span class="kw">:</span></span>
<span id="cb2-2"><a href="#cb2-2" aria-hidden="true" tabindex="-1"></a><span class="at">  </span><span class="kw">-</span><span class="at"> </span><span class="fu">matchType</span><span class="kw">:</span><span class="at"> Exact</span></span>
<span id="cb2-3"><a href="#cb2-3" aria-hidden="true" tabindex="-1"></a><span class="at">    </span><span class="fu">maxLength</span><span class="kw">:</span><span class="at"> </span><span class="dv">128</span></span>
<span id="cb2-4"><a href="#cb2-4" aria-hidden="true" tabindex="-1"></a><span class="at">    </span><span class="fu">name</span><span class="kw">:</span><span class="at"> MYCOOKIE</span></span></code></pre></div></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>httpCaptureHeaders</code></p></td>
<td style="text-align: left;"><p><code>httpCaptureHeaders</code> specifies the HTTP headers that you want to capture in the access logs. If the <code>httpCaptureHeaders</code> field is empty, the access logs do not capture the headers.</p>
<p><code>httpCaptureHeaders</code> contains two lists of headers to capture in the access logs. The two lists of header fields are <code>request</code> and <code>response</code>. In both lists, the <code>name</code> field must specify the header name and the <code>maxlength</code> field must specify the maximum length of the header. For example:</p>
<div class="sourceCode" id="cb3"><pre class="sourceCode yaml"><code class="sourceCode yaml"><span id="cb3-1"><a href="#cb3-1" aria-hidden="true" tabindex="-1"></a><span class="at">  </span><span class="fu">httpCaptureHeaders</span><span class="kw">:</span></span>
<span id="cb3-2"><a href="#cb3-2" aria-hidden="true" tabindex="-1"></a><span class="at">    </span><span class="fu">request</span><span class="kw">:</span></span>
<span id="cb3-3"><a href="#cb3-3" aria-hidden="true" tabindex="-1"></a><span class="at">    </span><span class="kw">-</span><span class="at"> </span><span class="fu">maxLength</span><span class="kw">:</span><span class="at"> </span><span class="dv">256</span></span>
<span id="cb3-4"><a href="#cb3-4" aria-hidden="true" tabindex="-1"></a><span class="at">      </span><span class="fu">name</span><span class="kw">:</span><span class="at"> Connection</span></span>
<span id="cb3-5"><a href="#cb3-5" aria-hidden="true" tabindex="-1"></a><span class="at">    </span><span class="kw">-</span><span class="at"> </span><span class="fu">maxLength</span><span class="kw">:</span><span class="at"> </span><span class="dv">128</span></span>
<span id="cb3-6"><a href="#cb3-6" aria-hidden="true" tabindex="-1"></a><span class="at">      </span><span class="fu">name</span><span class="kw">:</span><span class="at"> User-Agent</span></span>
<span id="cb3-7"><a href="#cb3-7" aria-hidden="true" tabindex="-1"></a><span class="at">    </span><span class="fu">response</span><span class="kw">:</span></span>
<span id="cb3-8"><a href="#cb3-8" aria-hidden="true" tabindex="-1"></a><span class="at">    </span><span class="kw">-</span><span class="at"> </span><span class="fu">maxLength</span><span class="kw">:</span><span class="at"> </span><span class="dv">256</span></span>
<span id="cb3-9"><a href="#cb3-9" aria-hidden="true" tabindex="-1"></a><span class="at">      </span><span class="fu">name</span><span class="kw">:</span><span class="at"> Content-Type</span></span>
<span id="cb3-10"><a href="#cb3-10" aria-hidden="true" tabindex="-1"></a><span class="at">    </span><span class="kw">-</span><span class="at"> </span><span class="fu">maxLength</span><span class="kw">:</span><span class="at"> </span><span class="dv">256</span></span>
<span id="cb3-11"><a href="#cb3-11" aria-hidden="true" tabindex="-1"></a><span class="at">      </span><span class="fu">name</span><span class="kw">:</span><span class="at"> Content-Length</span></span></code></pre></div></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>tuningOptions</code></p></td>
<td style="text-align: left;"><p><code>tuningOptions</code> specifies options for tuning the performance of Ingress Controller pods.</p>
<ul>
<li><p><code>clientFinTimeout</code> specifies how long a connection is held open while waiting for the client response to the server closing the connection. The default timeout is <code>1s</code>.</p></li>
<li><p><code>clientTimeout</code> specifies how long a connection is held open while waiting for a client response. The default timeout is <code>30s</code>.</p></li>
<li><p><code>headerBufferBytes</code> specifies how much memory is reserved, in bytes, for Ingress Controller connection sessions. This value must be at least <code>16384</code> if HTTP/2 is enabled for the Ingress Controller. If not set, the default value is <code>32768</code> bytes. Setting this field not recommended because <code>headerBufferBytes</code> values that are too small can break the Ingress Controller, and <code>headerBufferBytes</code> values that are too large could cause the Ingress Controller to use significantly more memory than necessary.</p></li>
<li><p><code>headerBufferMaxRewriteBytes</code> specifies how much memory should be reserved, in bytes, from <code>headerBufferBytes</code> for HTTP header rewriting and appending for Ingress Controller connection sessions. The minimum value for <code>headerBufferMaxRewriteBytes</code> is <code>4096</code>. <code>headerBufferBytes</code> must be greater than <code>headerBufferMaxRewriteBytes</code> for incoming HTTP requests. If not set, the default value is <code>8192</code> bytes. Setting this field not recommended because <code>headerBufferMaxRewriteBytes</code> values that are too small can break the Ingress Controller and <code>headerBufferMaxRewriteBytes</code> values that are too large could cause the Ingress Controller to use significantly more memory than necessary.</p></li>
<li><p><code>healthCheckInterval</code> specifies how long the router waits between health checks. The default is <code>5s</code>.</p></li>
<li><p><code>serverFinTimeout</code> specifies how long a connection is held open while waiting for the server response to the client that is closing the connection. The default timeout is <code>1s</code>.</p></li>
<li><p><code>serverTimeout</code> specifies how long a connection is held open while waiting for a server response. The default timeout is <code>30s</code>.</p></li>
<li><p><code>threadCount</code> specifies the number of threads to create per HAProxy process. Creating more threads allows each Ingress Controller pod to handle more connections, at the cost of more system resources being used. HAProxy supports up to <code>64</code> threads. If this field is empty, the Ingress Controller uses the default value of <code>4</code> threads. The default value can change in future releases. Setting this field is not recommended because increasing the number of HAProxy threads allows Ingress Controller pods to use more CPU time under load, and prevent other pods from receiving the CPU resources they need to perform. Reducing the number of threads can cause the Ingress Controller to perform poorly.</p></li>
<li><p><code>tlsInspectDelay</code> specifies how long the router can hold data to find a matching route. Setting this value too short can cause the router to fall back to the default certificate for edge-terminated, reencrypted, or passthrough routes, even when using a better matched certificate. The default inspect delay is <code>5s</code>.</p></li>
<li><p><code>tunnelTimeout</code> specifies how long a tunnel connection, including websockets, remains open while the tunnel is idle. The default timeout is <code>1h</code>.</p></li>
<li><p><code>maxConnections</code> specifies the maximum number of simultaneous connections that can be established per HAProxy process. Increasing this value allows each ingress controller pod to handle more connections at the cost of additional system resources. Permitted values are <code>0</code>, <code>-1</code>, any value within the range <code>2000</code> and <code>2000000</code>, or the field can be left empty.</p>
<ul>
<li><p>If this field is left empty or has the value <code>0</code>, the Ingress Controller will use the default value of <code>50000</code>. This value is subject to change in future releases.</p></li>
<li><p>If the field has the value of <code>-1</code>, then HAProxy will dynamically compute a maximum value based on the available <code>ulimits</code> in the running container. This process results in a large computed value that will incur significant memory usage compared to the current default value of <code>50000</code>.</p></li>
<li><p>If the field has a value that is greater than the current operating system limit, the HAProxy process will not start.</p></li>
<li><p>If you choose a discrete value and the router pod is migrated to a new node, it is possible the new node does not have an identical <code>ulimit</code> configured. In such cases, the pod fails to start.</p></li>
<li><p>If you have nodes with different <code>ulimits</code> configured, and you choose a discrete value, it is recommended to use the value of <code>-1</code> for this field so that the maximum number of connections is calculated at runtime.</p></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>logEmptyRequests</code></p></td>
<td style="text-align: left;"><p><code>logEmptyRequests</code> specifies connections for which no request is received and logged. These empty requests come from load balancer health probes or web browser speculative connections (preconnect) and logging these requests can be undesirable. However, these requests can be caused by network errors, in which case logging empty requests can be useful for diagnosing the errors. These requests can be caused by port scans, and logging empty requests can aid in detecting intrusion attempts. Allowed values for this field are <code>Log</code> and <code>Ignore</code>. The default value is <code>Log</code>.</p>
<p>The <code>LoggingPolicy</code> type accepts either one of two values:</p>
<ul>
<li><p><code>Log</code>: Setting this value to <code>Log</code> indicates that an event should be logged.</p></li>
<li><p><code>Ignore</code>: Setting this value to <code>Ignore</code> sets the <code>dontlognull</code> option in the HAproxy configuration.</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>HTTPEmptyRequestsPolicy</code></p></td>
<td style="text-align: left;"><p><code>HTTPEmptyRequestsPolicy</code> describes how HTTP connections are handled if the connection times out before a request is received. Allowed values for this field are <code>Respond</code> and <code>Ignore</code>. The default value is <code>Respond</code>.</p>
<p>The <code>HTTPEmptyRequestsPolicy</code> type accepts either one of two values:</p>
<ul>
<li><p><code>Respond</code>: If the field is set to <code>Respond</code>, the Ingress Controller sends an HTTP <code>400</code> or <code>408</code> response, logs the connection if access logging is enabled, and counts the connection in the appropriate metrics.</p></li>
<li><p><code>Ignore</code>: Setting this option to <code>Ignore</code> adds the <code>http-ignore-probes</code> parameter in the HAproxy configuration. If the field is set to <code>Ignore</code>, the Ingress Controller closes the connection without sending a response, then logs the connection, or incrementing metrics.</p></li>
</ul>
<p>These connections come from load balancer health probes or web browser speculative connections (preconnect) and can be safely ignored. However, these requests can be caused by network errors, so setting this field to <code>Ignore</code> can impede detection and diagnosis of problems. These requests can be caused by port scans, in which case logging empty requests can aid in detecting intrusion attempts.</p></td>
</tr>
</tbody>
</table>

## Ingress Controller TLS security profiles

TLS security profiles provide a way for servers to regulate which ciphers a connecting client can use when connecting to the server.

### Understanding TLS security profiles

You can use a TLS (Transport Layer Security) security profile, as described in this section, to define which TLS ciphers are required by various OpenShift Container Platform components.

The OpenShift Container Platform TLS security profiles are based on [Mozilla recommended configurations](https://wiki.mozilla.org/Security/Server_Side_TLS).

You can specify one of the following TLS security profiles for each component:

<table>
<caption>TLS security profiles</caption>
<colgroup>
<col style="width: 33%" />
<col style="width: 66%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Profile</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>Old</code></p></td>
<td style="text-align: left;"><p>This profile is intended for use with legacy clients or libraries. The profile is based on the <a href="https://wiki.mozilla.org/Security/Server_Side_TLS#Old_backward_compatibility">Old backward compatibility</a> recommended configuration.</p>
<p>The <code>Old</code> profile requires a minimum TLS version of 1.0.</p>
<div class="note">
<div class="title">
&#10;</div>
<p>For the Ingress Controller, the minimum TLS version is converted from 1.0 to 1.1.</p>
</div></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>Intermediate</code></p></td>
<td style="text-align: left;"><p>This profile is the default TLS security profile for the Ingress Controller, kubelet, and control plane. The profile is based on the <a href="https://wiki.mozilla.org/Security/Server_Side_TLS#Intermediate_compatibility_.28recommended.29">Intermediate compatibility</a> recommended configuration.</p>
<p>The <code>Intermediate</code> profile requires a minimum TLS version of 1.2.</p>
<div class="note">
<div class="title">
&#10;</div>
<p>This profile is the recommended configuration for the majority of clients.</p>
</div></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>Modern</code></p></td>
<td style="text-align: left;"><p>This profile is intended for use with modern clients that have no need for backwards compatibility. This profile is based on the <a href="https://wiki.mozilla.org/Security/Server_Side_TLS#Modern_compatibility">Modern compatibility</a> recommended configuration.</p>
<p>The <code>Modern</code> profile requires a minimum TLS version of 1.3.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>Custom</code></p></td>
<td style="text-align: left;"><p>This profile allows you to define the TLS version and ciphers to use.</p>
<div class="warning">
<div class="title">
&#10;</div>
<p>Use caution when using a <code>Custom</code> profile, because invalid configurations can cause problems.</p>
</div></td>
</tr>
</tbody>
</table>

> [!NOTE]
> When using one of the predefined profile types, the effective profile configuration is subject to change between releases. For example, given a specification to use the Intermediate profile deployed on release X.Y.Z, an upgrade to release X.Y.Z+1 might cause a new profile configuration to be applied, resulting in a rollout.

### Configuring the TLS security profile for the Ingress Controller

To configure a TLS security profile for an Ingress Controller, edit the `IngressController` custom resource (CR) to specify a predefined or custom TLS security profile. If a TLS security profile is not configured, the default value is based on the TLS security profile set for the API server.

<div class="formalpara">

<div class="title">

Sample `IngressController` CR that configures the `Old` TLS security profile

</div>

``` yaml
apiVersion: operator.openshift.io/v1
kind: IngressController
 ...
spec:
  tlsSecurityProfile:
    old: {}
    type: Old
 ...
```

</div>

The TLS security profile defines the minimum TLS version and the TLS ciphers for TLS connections for Ingress Controllers.

You can see the ciphers and the minimum TLS version of the configured TLS security profile in the `IngressController` custom resource (CR) under `Status.Tls Profile` and the configured TLS security profile under `Spec.Tls Security Profile`. For the `Custom` TLS security profile, the specific ciphers and minimum TLS version are listed under both parameters.

> [!NOTE]
> The HAProxy Ingress Controller image supports TLS `1.3` and the `Modern` profile.
>
> The Ingress Operator also converts the TLS `1.0` of an `Old` or `Custom` profile to `1.1`.

<div>

<div class="title">

Prerequisites

</div>

- You have access to the cluster as a user with the `cluster-admin` role.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Edit the `IngressController` CR in the `openshift-ingress-operator` project to configure the TLS security profile:

    ``` terminal
    $ oc edit IngressController default -n openshift-ingress-operator
    ```

2.  Add the `spec.tlsSecurityProfile` field:

    <div class="formalpara">

    <div class="title">

    Sample `IngressController` CR for a `Custom` profile

    </div>

    ``` yaml
    apiVersion: operator.openshift.io/v1
    kind: IngressController
     ...
    spec:
      tlsSecurityProfile:
        type: Custom
        custom:
          ciphers:
          - ECDHE-ECDSA-CHACHA20-POLY1305
          - ECDHE-RSA-CHACHA20-POLY1305
          - ECDHE-RSA-AES128-GCM-SHA256
          - ECDHE-ECDSA-AES128-GCM-SHA256
          minTLSVersion: VersionTLS11
     ...
    ```

    </div>

    - Specify the TLS security profile type (`Old`, `Intermediate`, or `Custom`). The default is `Intermediate`.

    - Specify the appropriate field for the selected type:

      - `old: {}`

      - `intermediate: {}`

      - `modern: {}`

      - `custom:`

    - For the `custom` type, specify a list of TLS ciphers and minimum accepted TLS version.

3.  Save the file to apply the changes.

</div>

<div>

<div class="title">

Verification

</div>

- Verify that the profile is set in the `IngressController` CR:

  ``` terminal
  $ oc describe IngressController default -n openshift-ingress-operator
  ```

  <div class="formalpara">

  <div class="title">

  Example output

  </div>

  ``` terminal
  Name:         default
  Namespace:    openshift-ingress-operator
  Labels:       <none>
  Annotations:  <none>
  API Version:  operator.openshift.io/v1
  Kind:         IngressController
   ...
  Spec:
   ...
    Tls Security Profile:
      Custom:
        Ciphers:
          ECDHE-ECDSA-CHACHA20-POLY1305
          ECDHE-RSA-CHACHA20-POLY1305
          ECDHE-RSA-AES128-GCM-SHA256
          ECDHE-ECDSA-AES128-GCM-SHA256
        Min TLS Version:  VersionTLS11
      Type:               Custom
   ...
  ```

  </div>

</div>

### Configuring mutual TLS authentication

You can configure the Ingress Controller to enable mutual TLS (mTLS) authentication by setting a `spec.clientTLS` value. The `clientTLS` value configures the Ingress Controller to verify client certificates. This configuration includes setting a `clientCA` value, which is a reference to a config map. The config map contains the PEM-encoded CA certificate bundle that is used to verify a client’s certificate. Optionally, you can also configure a list of certificate subject filters.

If the `clientCA` value specifies an X509v3 certificate revocation list (CRL) distribution point, the Ingress Operator downloads and manages a CRL config map based on the HTTP URI X509v3 `CRL Distribution Point` specified in each provided certificate. The Ingress Controller uses this config map during mTLS/TLS negotiation. Requests that do not provide valid certificates are rejected.

<div>

<div class="title">

Prerequisites

</div>

- You have access to the cluster as a user with the `cluster-admin` role.

- You have a PEM-encoded CA certificate bundle.

- If your CA bundle references a CRL distribution point, you must have also included the end-entity or leaf certificate to the client CA bundle. This certificate must have included an HTTP URI under `CRL Distribution Points`, as described in RFC 5280. For example:

  ``` terminal
   Issuer: C=US, O=Example Inc, CN=Example Global G2 TLS RSA SHA256 2020 CA1
           Subject: SOME SIGNED CERT            X509v3 CRL Distribution Points:
                  Full Name:
                    URI:http://crl.example.com/example.crl
  ```

</div>

<div>

<div class="title">

Procedure

</div>

1.  In the `openshift-config` namespace, create a config map from your CA bundle:

    ``` terminal
    $ oc create configmap \
      router-ca-certs-default \
      --from-file=ca-bundle.pem=client-ca.crt \
      -n openshift-config
    ```

    - The config map data key must be `ca-bundle.pem`, and the data value must be a CA certificate in PEM format.

2.  Edit the `IngressController` resource in the `openshift-ingress-operator` project:

    ``` terminal
    $ oc edit IngressController default -n openshift-ingress-operator
    ```

3.  Add the `spec.clientTLS` field and subfields to configure mutual TLS:

    <div class="formalpara">

    <div class="title">

    Sample `IngressController` CR for a `clientTLS` profile that specifies filtering patterns

    </div>

    ``` yaml
      apiVersion: operator.openshift.io/v1
      kind: IngressController
      metadata:
        name: default
        namespace: openshift-ingress-operator
      spec:
        clientTLS:
          clientCertificatePolicy: Required
          clientCA:
            name: router-ca-certs-default
          allowedSubjectPatterns:
          - "^/CN=example.com/ST=NC/C=US/O=Security/OU=OpenShift$"
    ```

    </div>

4.  Optional, get the Distinguished Name (DN) for `allowedSubjectPatterns` by entering the following command.

    ``` terminal
    $ openssl x509 -in custom-cert.pem -noout -subject
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` text
    subject=C=US, ST=NC, O=Security, OU=OpenShift, CN=example.com
    ```

    </div>

</div>

# View the default Ingress Controller

The Ingress Operator is a core feature of OpenShift Container Platform and is enabled out of the box.

Every new OpenShift Container Platform installation has an `ingresscontroller` named default. It can be supplemented with additional Ingress Controllers. If the default `ingresscontroller` is deleted, the Ingress Operator will automatically recreate it within a minute.

<div>

<div class="title">

Procedure

</div>

- View the default Ingress Controller:

  ``` terminal
  $ oc describe --namespace=openshift-ingress-operator ingresscontroller/default
  ```

</div>

# View Ingress Operator status

You can view and inspect the status of your Ingress Operator.

<div>

<div class="title">

Procedure

</div>

- View your Ingress Operator status:

  ``` terminal
  $ oc describe clusteroperators/ingress
  ```

</div>

# View Ingress Controller logs

You can view your Ingress Controller logs.

<div>

<div class="title">

Procedure

</div>

- View your Ingress Controller logs:

  ``` terminal
  $ oc logs --namespace=openshift-ingress-operator deployments/ingress-operator -c <container_name>
  ```

</div>

# View Ingress Controller status

Your can view the status of a particular Ingress Controller.

<div>

<div class="title">

Procedure

</div>

- View the status of an Ingress Controller:

  ``` terminal
  $ oc describe --namespace=openshift-ingress-operator ingresscontroller/<name>
  ```

</div>

# Creating a custom Ingress Controller

As a cluster administrator, you can create a new custom Ingress Controller. Because the default Ingress Controller might change during OpenShift Container Platform updates, creating a custom Ingress Controller can be helpful when maintaining a configuration manually that persists across cluster updates.

This example provides a minimal spec for a custom Ingress Controller. To further customize your custom Ingress Controller, see "Configuring the Ingress Controller".

<div>

<div class="title">

Prerequisites

</div>

- Install the OpenShift CLI (`oc`).

- Log in as a user with `cluster-admin` privileges.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create a YAML file that defines the custom `IngressController` object:

    <div class="formalpara">

    <div class="title">

    Example `custom-ingress-controller.yaml` file

    </div>

    ``` yaml
    apiVersion: operator.openshift.io/v1
    kind: IngressController
    metadata:
        name: <custom_name>
        namespace: openshift-ingress-operator
    spec:
        defaultCertificate:
            name: <custom-ingress-custom-certs>
        replicas: 1
        domain: <custom_domain>
    ```

    </div>

    - Specify the a custom `name` for the `IngressController` object.

    - Specify the name of the secret with the custom wildcard certificate.

    - Minimum replica needs to be ONE

    - Specify the domain to your domain name. The domain specified on the IngressController object and the domain used for the certificate must match. For example, if the domain value is "custom_domain.mycompany.com", then the certificate must have SAN \*.custom_domain.mycompany.com (with the `*.` added to the domain).

2.  Create the object by running the following command:

    ``` terminal
    $ oc create -f custom-ingress-controller.yaml
    ```

</div>

# Configuring the Ingress Controller

## Setting a custom default certificate

As an administrator, you can configure an Ingress Controller to use a custom certificate by creating a Secret resource and editing the `IngressController` custom resource (CR).

<div>

<div class="title">

Prerequisites

</div>

- You must have a certificate/key pair in PEM-encoded files, where the certificate is signed by a trusted certificate authority or by a private trusted certificate authority that you configured in a custom PKI.

- Your certificate meets the following requirements:

  - The certificate is valid for the ingress domain.

  - The certificate uses the `subjectAltName` extension to specify a wildcard domain, such as `*.apps.ocp4.example.com`.

- You must have an `IngressController` CR, which includes just having the `default` `IngressController` CR. You can run the following command to check that you have an `IngressController` CR:

  ``` terminal
  $ oc --namespace openshift-ingress-operator get ingresscontrollers
  ```

</div>

> [!NOTE]
> If you have intermediate certificates, they must be included in the `tls.crt` file of the secret containing a custom default certificate. Order matters when specifying a certificate; list your intermediate certificate(s) after any server certificate(s).

<div class="formalpara">

<div class="title">

Procedure

</div>

The following assumes that the custom certificate and key pair are in the `tls.crt` and `tls.key` files in the current working directory. Substitute the actual path names for `tls.crt` and `tls.key`. You also may substitute another name for `custom-certs-default` when creating the Secret resource and referencing it in the IngressController CR.

</div>

> [!NOTE]
> This action will cause the Ingress Controller to be redeployed, using a rolling deployment strategy.

1.  Create a Secret resource containing the custom certificate in the `openshift-ingress` namespace using the `tls.crt` and `tls.key` files.

    ``` terminal
    $ oc --namespace openshift-ingress create secret tls custom-certs-default --cert=tls.crt --key=tls.key
    ```

2.  Update the IngressController CR to reference the new certificate secret:

    ``` terminal
    $ oc patch --type=merge --namespace openshift-ingress-operator ingresscontrollers/default \
      --patch '{"spec":{"defaultCertificate":{"name":"custom-certs-default"}}}'
    ```

3.  Verify the update was effective:

    ``` terminal
    $ echo Q |\
      openssl s_client -connect console-openshift-console.apps.<domain>:443 -showcerts 2>/dev/null |\
      openssl x509 -noout -subject -issuer -enddate
    ```

    where:

    `<domain>`
    Specifies the base domain name for your cluster.

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` text
    subject=C = US, ST = NC, L = Raleigh, O = RH, OU = OCP4, CN = *.apps.example.com
    issuer=C = US, ST = NC, L = Raleigh, O = RH, OU = OCP4, CN = example.com
    notAfter=May 10 08:32:45 2022 GM
    ```

    </div>

    > [!TIP]
    > You can alternatively apply the following YAML to set a custom default certificate:
    >
    > ``` yaml
    > apiVersion: operator.openshift.io/v1
    > kind: IngressController
    > metadata:
    >   name: default
    >   namespace: openshift-ingress-operator
    > spec:
    >   defaultCertificate:
    >     name: custom-certs-default
    > ```

    The certificate secret name should match the value used to update the CR.

Once the IngressController CR has been modified, the Ingress Operator updates the Ingress Controller’s deployment to use the custom certificate.

## Removing a custom default certificate

As an administrator, you can remove a custom certificate that you configured an Ingress Controller to use.

<div>

<div class="title">

Prerequisites

</div>

- You have access to the cluster as a user with the `cluster-admin` role.

- You have installed the OpenShift CLI (`oc`).

- You previously configured a custom default certificate for the Ingress Controller.

</div>

<div>

<div class="title">

Procedure

</div>

- To remove the custom certificate and restore the certificate that ships with OpenShift Container Platform, enter the following command:

  ``` terminal
  $ oc patch -n openshift-ingress-operator ingresscontrollers/default \
    --type json -p $'- op: remove\n  path: /spec/defaultCertificate'
  ```

  There can be a delay while the cluster reconciles the new certificate configuration.

</div>

<div>

<div class="title">

Verification

</div>

- To confirm that the original cluster certificate is restored, enter the following command:

  ``` terminal
  $ echo Q | \
    openssl s_client -connect console-openshift-console.apps.<domain>:443 -showcerts 2>/dev/null | \
    openssl x509 -noout -subject -issuer -enddate
  ```

  where:

  `<domain>`
  Specifies the base domain name for your cluster.

  <div class="formalpara">

  <div class="title">

  Example output

  </div>

  ``` text
  subject=CN = *.apps.<domain>
  issuer=CN = ingress-operator@1620633373
  notAfter=May 10 10:44:36 2023 GMT
  ```

  </div>

</div>

## Autoscaling an Ingress Controller

You can automatically scale an Ingress Controller to dynamically meet routing performance or availability requirements. For example, the requirement to increase throughput.

The following procedure provides an example for scaling up the default Ingress Controller.

<div>

<div class="title">

Prerequisites

</div>

- You have the OpenShift CLI (`oc`) installed.

- You have access to an OpenShift Container Platform cluster as a user with the `cluster-admin` role.

- On VMware vSphere, bare-metal, and Nutanix installer-provisioned infrastructure, scaling up Ingress Controller pods does not improve external traffic performance. To improve performance, ensure that you complete the following prerequisites:

  - You manually configured a user-managed load balancer for your cluster.

  - You ensured that the load balancer was configured for the cluster nodes that handle incoming traffic from the Ingress Controller.

- You installed the Custom Metrics Autoscaler Operator and an associated KEDA Controller.

  - You can install the Operator by using the software catalog on the web console. After you install the Operator, you can create an instance of `KedaController`.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create a service account to authenticate with Thanos by running the following command:

    ``` terminal
    $ oc create -n openshift-ingress-operator serviceaccount thanos && oc describe -n openshift-ingress-operator serviceaccount thanos
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    Name:                thanos
    Namespace:           openshift-ingress-operator
    Labels:              <none>
    Annotations:         <none>
    Image pull secrets:  thanos-dockercfg-kfvf2
    Mountable secrets:   thanos-dockercfg-kfvf2
    Tokens:              <none>
    Events:              <none>
    ```

    </div>

2.  Manually create the service account secret token with the following command:

    ``` terminal
    $ oc apply -f - <<EOF
    apiVersion: v1
    kind: Secret
    metadata:
      name: thanos-token
      namespace: openshift-ingress-operator
      annotations:
        kubernetes.io/service-account.name: thanos
    type: kubernetes.io/service-account-token
    EOF
    ```

3.  Define a `TriggerAuthentication` object within the `openshift-ingress-operator` namespace by using the service account’s token.

    1.  Create the `TriggerAuthentication` object and pass the value of the `secret` variable to the `TOKEN` parameter:

        ``` terminal
        $ oc apply -f - <<EOF
        apiVersion: keda.sh/v1alpha1
        kind: TriggerAuthentication
        metadata:
          name: keda-trigger-auth-prometheus
          namespace: openshift-ingress-operator
        spec:
          secretTargetRef:
          - parameter: bearerToken
            name: thanos-token
            key: token
          - parameter: ca
            name: thanos-token
            key: ca.crt
        EOF
        ```

4.  Create and apply a role for reading metrics from Thanos:

    1.  Create a new role, `thanos-metrics-reader.yaml`, that reads metrics from pods and nodes:

        <div class="formalpara">

        <div class="title">

        thanos-metrics-reader.yaml

        </div>

        ``` yaml
        apiVersion: rbac.authorization.k8s.io/v1
        kind: Role
        metadata:
          name: thanos-metrics-reader
          namespace: openshift-ingress-operator
        rules:
        - apiGroups:
          - ""
          resources:
          - pods
          - nodes
          verbs:
          - get
        - apiGroups:
          - metrics.k8s.io
          resources:
          - pods
          - nodes
          verbs:
          - get
          - list
          - watch
        - apiGroups:
          - ""
          resources:
          - namespaces
          verbs:
          - get
        ```

        </div>

    2.  Apply the new role by running the following command:

        ``` terminal
        $ oc apply -f thanos-metrics-reader.yaml
        ```

5.  Add the new role to the service account by entering the following commands:

    ``` terminal
    $ oc adm policy -n openshift-ingress-operator add-role-to-user thanos-metrics-reader -z thanos --role-namespace=openshift-ingress-operator
    ```

    ``` terminal
    $ oc adm policy -n openshift-ingress-operator add-cluster-role-to-user cluster-monitoring-view -z thanos
    ```

    > [!NOTE]
    > The argument `add-cluster-role-to-user` is only required if you use cross-namespace queries. The following step uses a query from the `kube-metrics` namespace which requires this argument.

6.  Create a new `ScaledObject` YAML file, `ingress-autoscaler.yaml`, that targets the default Ingress Controller deployment:

    <div class="formalpara">

    <div class="title">

    Example `ScaledObject` definition

    </div>

    ``` yaml
    apiVersion: keda.sh/v1alpha1
    kind: ScaledObject
    metadata:
      name: ingress-scaler
      namespace: openshift-ingress-operator
    spec:
      scaleTargetRef:
        apiVersion: operator.openshift.io/v1
        kind: IngressController
        name: default
        envSourceContainerName: ingress-operator
      minReplicaCount: 1
      maxReplicaCount: 20
      cooldownPeriod: 1
      pollingInterval: 1
      triggers:
      - type: prometheus
        metricType: AverageValue
        metadata:
          serverAddress: https://thanos-querier.openshift-monitoring.svc.cluster.local:9091
          namespace: openshift-ingress-operator
          metricName: 'kube-node-role'
          threshold: '1'
          query: 'sum(kube_node_role{role="worker",service="kube-state-metrics"})'
          authModes: "bearer"
        authenticationRef:
          name: keda-trigger-auth-prometheus
    ```

    </div>

    - The custom resource that you are targeting. In this case, the Ingress Controller.

    - Optional: The maximum number of replicas. If you omit this field, the default maximum is set to 100 replicas.

    - The Thanos service endpoint in the `openshift-monitoring` namespace.

    - The Ingress Operator namespace.

    - This expression evaluates to however many worker nodes are present in the deployed cluster.

      > [!IMPORTANT]
      > If you are using cross-namespace queries, you must target port 9091 and not port 9092 in the `serverAddress` field. You also must have elevated privileges to read metrics from this port.

7.  Apply the custom resource definition by running the following command:

    ``` terminal
    $ oc apply -f ingress-autoscaler.yaml
    ```

</div>

<div>

<div class="title">

Verification

</div>

- Verify that the default Ingress Controller is scaled out to match the value returned by the `kube-state-metrics` query by running the following commands:

  - Use the `grep` command to search the Ingress Controller YAML file for the number of replicas:

    ``` terminal
    $ oc get -n openshift-ingress-operator ingresscontroller/default -o yaml | grep replicas:
    ```

  - Get the pods in the `openshift-ingress` project:

    ``` terminal
    $ oc get pods -n openshift-ingress
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    NAME                             READY   STATUS    RESTARTS   AGE
    router-default-7b5df44ff-l9pmm   2/2     Running   0          17h
    router-default-7b5df44ff-s5sl5   2/2     Running   0          3d22h
    router-default-7b5df44ff-wwsth   2/2     Running   0          66s
    ```

    </div>

</div>

<div>

<div class="title">

Additional resources

</div>

- [Installing the custom metrics autoscaler](../../nodes/cma/nodes-cma-autoscaling-custom-install.md#nodes-cma-autoscaling-custom-install_nodes-cma-autoscaling-custom-install)

- [Enabling monitoring for user-defined projects](https://docs.redhat.com/en/documentation/monitoring_stack_for_red_hat_openshift/4.20/html/configuring_user_workload_monitoring/preparing-to-configure-the-monitoring-stack-uwm#enabling-monitoring-for-user-defined-projects-uwm_preparing-to-configure-the-monitoring-stack-uwm)

- [Understanding custom metrics autoscaler trigger authentications](../../nodes/cma/nodes-cma-autoscaling-custom-trigger-auth.md#nodes-cma-autoscaling-custom-trigger-auth)

- [Understanding custom metrics autoscaler triggers](../../nodes/cma/nodes-cma-autoscaling-custom-trigger.md#nodes-cma-autoscaling-custom-prometheus)

- [Understanding how to add custom metrics autoscalers](../../nodes/cma/nodes-cma-autoscaling-custom-adding.md#nodes-cma-autoscaling-custom-adding)

</div>

## Scaling an Ingress Controller

Manually scale an Ingress Controller to meeting routing performance or availability requirements such as the requirement to increase throughput. `oc` commands are used to scale the `IngressController` resource. The following procedure provides an example for scaling up the default `IngressController`.

> [!NOTE]
> Scaling is not an immediate action, as it takes time to create the desired number of replicas.

<div>

<div class="title">

Prerequisites

</div>

- On VMware vSphere, bare-metal, and Nutanix installer-provisioned infrastructure, scaling up Ingress Controller pods does not improve external traffic performance. To improve performance, ensure that you complete the following prerequisites:

  - You manually configured a user-managed load balancer for your cluster.

  - You ensured that the load balancer was configured for the cluster nodes that handle incoming traffic from the Ingress Controller.

</div>

<div>

<div class="title">

Procedure

</div>

1.  View the current number of available replicas for the default `IngressController`:

    ``` terminal
    $ oc get -n openshift-ingress-operator ingresscontrollers/default -o jsonpath='{$.status.availableReplicas}'
    ```

2.  Scale the default `IngressController` to the desired number of replicas by using the `oc patch` command. The following example scales the default `IngressController` to 3 replicas.

    ``` terminal
    $ oc patch -n openshift-ingress-operator ingresscontroller/default --patch '{"spec":{"replicas": 3}}' --type=merge
    ```

3.  Verify that the default `IngressController` scaled to the number of replicas that you specified:

    ``` terminal
    $ oc get -n openshift-ingress-operator ingresscontrollers/default -o jsonpath='{$.status.availableReplicas}'
    ```

    > [!TIP]
    > You can alternatively apply the following YAML to scale an Ingress Controller to three replicas:
    >
    > ``` yaml
    > apiVersion: operator.openshift.io/v1
    > kind: IngressController
    > metadata:
    >   name: default
    >   namespace: openshift-ingress-operator
    > spec:
    >   replicas: 3
    > ```

    - If you need a different amount of replicas, change the `replicas` value.

</div>

## Configuring Ingress access logging

You can configure the Ingress Controller to enable access logs. If you have clusters that do not receive much traffic, then you can log to a sidecar. If you have high traffic clusters, to avoid exceeding the capacity of the logging stack or to integrate with a logging infrastructure outside of OpenShift Container Platform, you can forward logs to a custom syslog endpoint. You can also specify the format for access logs.

Container logging is useful to enable access logs on low-traffic clusters when there is no existing Syslog logging infrastructure, or for short-term use while diagnosing problems with the Ingress Controller.

Syslog is needed for high-traffic clusters where access logs could exceed the OpenShift Logging stack’s capacity, or for environments where any logging solution needs to integrate with an existing Syslog logging infrastructure. The Syslog use-cases can overlap.

<div>

<div class="title">

Prerequisites

</div>

- Log in as a user with `cluster-admin` privileges.

</div>

<div>

<div class="title">

Procedure

</div>

- For Ingress access logging to a sidecar, complete the following commands:

  - To enable Ingress access logging to a sidecar, enter the following command:

    ``` terminal
    $ oc patch ingresscontroller default -n openshift-ingress-operator --type=merge \
      -p '{"spec":{"logging":{"access":{"destination":{"type":"Container"}}}}}'
    ```

    After you configure the Ingress Controller to log to a sidecar, the Operator creates a container named `logs` inside a router pod that exists in the `openshift-ingress` namespace.

  - If you need to disable Ingress access logging, enter the following command that does not specify any values for `spec.logging`:

    ``` terminal
    $ oc patch ingresscontroller default -n openshift-ingress-operator --type=json \
      -p='[{"op": "remove", "path": "/spec/logging"}]'
    ```

  - To stream the access logs and system events from the OpenShift Container Platform Ingress Controller, enter the following command:

    ``` terminal
    $ oc -n openshift-ingress logs deployment.apps/router-default -c logs
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    2020-05-11T19:11:50.135710+00:00 router-default-57dfc6cd95-bpmk6 router-default-57dfc6cd95-bpmk6 haproxy[108]: 174.19.21.82:39654 [11/May/2020:19:11:50.133] public be_http:hello-openshift:hello-openshift/pod:hello-openshift:hello-openshift:10.128.2.12:8080 0/0/1/0/1 200 142 - - --NI 1/1/0/0/0 0/0 "GET / HTTP/1.1"
    ```

    </div>

- To enable logging to an external Syslog server, enter the following command. Use this option if you need to forward logs to a centralized logging solution such as Splunk, Rsyslog, or Logstash.

  ``` terminal
  $ oc patch ingresscontroller default -n openshift-ingress-operator --type=merge \
    -p '{"spec":{"logging":{"access":{"destination":{"type":"Syslog","syslog":{"address":"1.2.3.4","port":514,"maxLenght":1024}}}}}}'
  ```

  - Replace `1.2.3.4` with the destination IP address of your logging server. Syslog does not support a DNS hostname value.

  - Replace `514` with the UDP destination port of your logging server.

  - Replace `1024` with the maximum length of a log message in bytes that you want to set for log messages.

- To customize the log format, append an HAProxy-compatible log string to the following command. The string determines what information gets captured in the log format, such as a client IP address.

  ``` terminal
  $ oc patch ingresscontroller default -n openshift-ingress-operator --type=merge \
    -p '{"spec":{"logging":{"access":{"httpLogFormat":"%ci:%cp [%t] %ft %b/%s %B %bq %HM %HU %HV"}}}}'
  ```

  > [!NOTE]
  > For a list of HAProxy log variable descriptions, see [Custom log format](https://docs.haproxy.org/2.8/configuration.html#8.2.6) in the upstream HAProxy documentation.

- To capture custom HTTP headers or response headers in your logs, enter the following command. Consider this option if you need to track an `X-Forwarded-For` header or custom application IDs in the Ingress and application logs.

  ``` terminal
  $ oc patch ingresscontroller default -n openshift-ingress-operator --type=merge -p '{"spec":{"logging":{"access":{"httpCaptureHeaders":{"request":[{"name":"User-Agent","maxLength": 1024}],"response":[{"name":"Content-Type","maxLength": 1024}]}}}}}'
  ```

- To configure a log empty requests policy, enter the following command and set the `logEmptyRequests` parameter to `Log`. By default, HAProxy might not log empty requests or health checks, so you must manually enable this feature. To disable the feature, set the `logEmptyRequests` parameter to `Ignore`.

  ``` terminal
  $ oc patch ingresscontroller default -n openshift-ingress-operator --type=merge -p '{"spec":{"logging":{"access":{"logEmptyRequests":"Ignore"}}}}'
  ```

</div>

<div>

<div class="title">

Additional resources

</div>

- [Capturing Original Client IP from the X-Forwarded-For Header in Ingress and Application Logs](https://access.redhat.com/solutions/7096271)

</div>

## Setting Ingress Controller thread count

A cluster administrator can set the thread count to increase the amount of incoming connections a cluster can handle. You can patch an existing Ingress Controller to increase the amount of threads.

<div>

<div class="title">

Prerequisites

</div>

- The following assumes that you already created an Ingress Controller.

</div>

<div>

<div class="title">

Procedure

</div>

- Update the Ingress Controller to increase the number of threads:

  ``` terminal
  $ oc -n openshift-ingress-operator patch ingresscontroller/default --type=merge -p '{"spec":{"tuningOptions": {"threadCount": 8}}}'
  ```

  > [!NOTE]
  > If you have a node that is capable of running large amounts of resources, you can configure `spec.nodePlacement.nodeSelector` with labels that match the capacity of the intended node, and configure `spec.tuningOptions.threadCount` to an appropriately high value.

</div>

## Configuring an Ingress Controller to use an internal load balancer

When creating an Ingress Controller on cloud platforms, the Ingress Controller is published by a public cloud load balancer by default. As an administrator, you can create an Ingress Controller that uses an internal cloud load balancer.

> [!WARNING]
> If your cloud provider is Microsoft Azure, you must have at least one public load balancer that points to your nodes. If you do not, all of your nodes will lose egress connectivity to the internet.

> [!IMPORTANT]
> If you want to change the `scope` for an `IngressController`, you can change the `.spec.endpointPublishingStrategy.loadBalancer.scope` parameter after the custom resource (CR) is created.

<figure>
<img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAABfAAAAUNCAIAAAA7VPfnAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAyhpVFh0WE1MOmNvbS5hZG9iZS54bXAAAAAAADw/eHBhY2tldCBiZWdpbj0i77u/IiBpZD0iVzVNME1wQ2VoaUh6cmVTek5UY3prYzlkIj8+IDx4OnhtcG1ldGEgeG1sbnM6eD0iYWRvYmU6bnM6bWV0YS8iIHg6eG1wdGs9IkFkb2JlIFhNUCBDb3JlIDcuMS1jMDAwIDc5LmVkYTJiM2ZhYywgMjAyMS8xMS8xNy0xNzoyMzoxOSAgICAgICAgIj4gPHJkZjpSREYgeG1sbnM6cmRmPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5LzAyLzIyLXJkZi1zeW50YXgtbnMjIj4gPHJkZjpEZXNjcmlwdGlvbiByZGY6YWJvdXQ9IiIgeG1sbnM6eG1wPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvIiB4bWxuczp4bXBNTT0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wL21tLyIgeG1sbnM6c3RSZWY9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC9zVHlwZS9SZXNvdXJjZVJlZiMiIHhtcDpDcmVhdG9yVG9vbD0iQWRvYmUgUGhvdG9zaG9wIDIzLjEgKE1hY2ludG9zaCkiIHhtcE1NOkluc3RhbmNlSUQ9InhtcC5paWQ6RjJCNzA4NzQ4MDVFMTFFQzlENUQ4RDMyQkEzQTc5OTEiIHhtcE1NOkRvY3VtZW50SUQ9InhtcC5kaWQ6RjJCNzA4NzU4MDVFMTFFQzlENUQ4RDMyQkEzQTc5OTEiPiA8eG1wTU06RGVyaXZlZEZyb20gc3RSZWY6aW5zdGFuY2VJRD0ieG1wLmlpZDpGMkI3MDg3MjgwNUUxMUVDOUQ1RDhEMzJCQTNBNzk5MSIgc3RSZWY6ZG9jdW1lbnRJRD0ieG1wLmRpZDpGMkI3MDg3MzgwNUUxMUVDOUQ1RDhEMzJCQTNBNzk5MSIvPiA8L3JkZjpEZXNjcmlwdGlvbj4gPC9yZGY6UkRGPiA8L3g6eG1wbWV0YT4gPD94cGFja2V0IGVuZD0iciI/PikFl+IAAWJdSURBVHja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hPjvf//7u9/9LicnJxAISJIk1gSDwW3bti1fvnzo0KEvvvhiv379xEqPx1NQUCAK6PV68dVut2/dulXssn379urq6vbt21/0jhUVFb333nu5ubm///3vu3TpwpECAAAtjjt0AABARHjrrbfuueeer7/+Oi0t7Ve/+tWnn3762WefLV++fOLEiWLrhg0bJk2adOTIEbEsSZLRaFQzPkJ8fPxvf/vbYcOGiU+x76Xo25YtWxYsWLBmzRqn08mRAgAAkYA7dAAAQMvbsWPHr3/9a4/H079//7feeuvKK68Mb5oyZcqiRYsWLFhwyy23fNfdN3eEXLruWSwWo9Fos9msVisHCwAARAISOgAAoIUFAoE//elPdrs9OTn57bffzsjIaLxVp9P94he/6N+//7Bhw2T5zD9dCgsLKysr4+LievTo0WTTt99+W11dbbFYxCaj0dh4k9PpzMvLE61ffvnlNputqqpKFLZarb179w7f/lNcXFxWVpafny+aDgaDe/furampURSlZ8+eUVFRHDsAANBSeOQKAAC0sP3792/btk2n002ZMqVJNids5MiR35XNEX7zm99cddVVDz/8cOOV+/btmz59+vDhwwcPHjx06NDRo0f/61//alwgNzd32LBhV1999eHDh//xj38MGTLkmmuuufbaa2+66aavv/5aLbN48eKBAwf+4Q9/iIqK8nq9s2bNEsXEmr1793LgAABAC+IOHQAA0MK2b9/udDplWb7xxhvPrwaDwSA+G9+As2XLlpkzZxYXFycmJvbq1auurk6s2bVrV1lZ2fz589UyOp3OHPLqq69mZWXFx8enpaVVVFSsX7/+7rvvXrVqVVJSUlxcXJcuXSRJamhoEJ/t27cXbTkcDrEXBw4AALQg7tABAAAt7Ntvvw0GgwkJCZ07d74oFVZXV//yl78sLS0dO3bsJ598kpWVtW7dunnz5ul0umeffXb79u2NC/v9/tzc3A8++GDLli1r164dN26c0WjMzs4WO4qt999//7Zt2+bPn+9wOMT6t95667PPPtu6dWv//v05cAAAoAVxhw4AAGhhgUAgGAyaQi5KhevWrdu7d2+vXr2WL18eFxcn1qSkpCxevLiiouLf//73e++9N2TIkHBhr9f7/PPPjxo1Si32pz/9adeuXaJkQUFBm9ArtITk5GRFUSRJ6tChw6V4LToAAMAP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+J///EfN8kQOq9UqjuCiRYtOnDhxww03TJkyhT8wAAAAAAAuBTWH0PIPubz00ktvvfVWVFSUek+H2+2WZblfv35dunTxer25ublHjx41GAzqvSplZWU5OTmtL6ETFggEhg0blpiYqCiKOEJ+vz8/Pz8vL0+MXXyNjY1dv379Rx99NGPGjEjredu2bZ955hn+rgAAAAAAaAYtnNDZs2fPiy++aLVa1WyO0+ns37//b37zm9GjRxsMBrGmoqJi5cqVf/zjH8vKykwm0/PPP/+LX/zi3OuvqqrKz8+vqakRy2lpad26dTvjHDSiclFG9EGdhLhLly56vV7dJLp07NgxtXuKonTu3Fn09vQaRD+rq6vF7gkJCW3btjUajeocQD+U2+1++umnMzMzw2vU6Z+XLl2qTooseiICMn36dEmSxOjKy8ubdLu0tHTTpk2iA8OHD09OTv6hAfH5fN9++62oUNQvxisaPf3NU6KSkydPirbUMaanp8uyXFhYKPZV9xIRSExMvFhREm0dOXLEbreLVkRnunfvfsYD/UNDAQAAAACAdsni8js8A3EzE40uWbKkoaFBnY/Z7Xb369fv448/bteuXbiMuA6/7777+vbtO3v27F/+8pdz5849x8pPnjz55z//+ZNPPikqKlJHJ8ty9+7db7/99nvvvddsNjcu/Nxzz7355ps2m83r9Xbt2nXjxo3h6/+9e/ded911atbD4XCITddcc03jfQsLC1966aXPP/+8tLRUBDMlJWXy5MmilfN+Ksrn8zX+GhMT8/jjj69Zs6aiokJ9jdSJEydEP0X977zzzoIFC8Ld/vLLLzds2PDoo48WFxd7PJ7nn39eLP/QgIghzJs374svvrBYLH6/Pz4+ftOmTenp6Y27NGfOHNEfq9UqWhGHZvPmzXa7/ZZbbhGhMBqNIkoino2bPu8oHT169MUXXxSDKikpUZM1YrCDBg166KGHRowY0bjkDwoFAAAAAADapaZx5NjYWJfL1SJzshw/fnzjxo1qKkG9sUJceDfO5oQNHjxYlOzQocM51rx///677rrr8OHD6qzJ4QHn5uY+9thja9asWbp0aadOncLldTqd/v80mc1XkiR1fZvQdDZNphzatGnT/fffLwaiTt4s9i0rK3vllVc+++yz2tra8G0+F0idJTo8sU64D427bbPZ9uzZ8/Of/7yqqkpNPzUeyLkHRJwJs2bN2rZtmxxy8uTJtWvXzps3L1yV2OWLL74QTYhGnU7ntGnTRJ12u/0sMTy/KG3evHnOnDlHjx4VYxe9EsMXO3q93k8//VRseu655xpn9849FAAAAAAAaJq41BXX47revXv3799ffZynmeXl5Z08eVJ9tMrtdmdmZg4bNuy7Cp97NqegoGDmzJnffPNNbGys0WgUNTeEeL1es9kcHR29adOme+65p76+vvFeUiNNKvyuTYcOHbrzzjvFEGJiYsQo/H6/w+HweDx6vV4Mraam5vwSOk3uHhI+++yzoqIiNVCKokRFRanL4b6pd6+8/PLLpaWlgUBADE0c2vCdPj80IOPHj+/WrZu6u2ho9erV6gTaqk8++UTNwojxpqWlTZ069VJEKScn5+677y4pKYmLixMVnjpTdTrRc9Fn9X6uxx9/XHTs9MN09lAAAAAAAKB1nTt37t+/v3ofRsvMpHPkyJHwsqIoAwcOvPBXbomL+aeffjo/Pz82NrZNKE80dOjQsWPHiqv6lStX5ubmms1msWnLli1Lly6dP3/+eTckOvy73/2uvLxczS+4XK4OHTqIhkTleXl5GzZsOL83wev1+q1bt9bW1vr9fhENj8ezZ8+eZcuWqZPatAk9kDVixIgmt5wYDIZjx44dOnToJz/5ybhx4xITE0+cOKE+J3UeAWnbtu2ECRNee+01Ua3JZNq3b9/hw4fFuSI2if6sXr1aTSeJId96661nT7SdX5TEyqeeeqq0tDQmJsbr9SYkJDz22GNXXHHFyZMnX3nllb1791qtVhGHZ5555tprr1XHdS6hAAAAAACgFdDr9aeegGnBHojL+8Zfz/iw1Q+1f//+tWvXqukDp9M5c+bM1157Tb3/6L777ps+ffquXbvMZrNY8+677951111nnLv3XGRnZ2/cuFF9okcMJDMz8+9//3vnzp3VratXr37wwQdFB37oTTqib08//XR4SiOxEAgETCaTmnQTFfbo0WPWrFlnDOadd975hz/8IS4u7sIDMmXKlL/97W/qU051dXWrVq1SEzpi1AcOHBD9ER0Tu5yxJxcepX379ql7qR14/fXXw+81u/baa8XykSNHROuHDx/etm3bjTfeeI6hAAAAAACg1WjJuUWaPFtUV1d34XWKK3yHw6HT6fx+f7t27Z588snw02RJSUniq/pIjtFo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ffXVVxctWqRtM5dHPvroo40bN1Yr+eabb9Y2qDGnFueqVatmzJjx888/a71paWl9+vTRLqiCsXoL2lM7ycrNokpntJlFVstV+aDMmT179rZt29RO7dmz56WXXtqgQQPzahJraccff/wNN9ygpX3yySdab5s2ba655prOnTubZOGzMXAXtP1r16594oknMjMz9XnAgAGXX365GcKz1qXF3nTTTVrO008/rfNxzZo12jD9ve2225TV2oUrrrjioYce2rlzp7ZZLeZvv/3WfNW2bVvNWO4PMuH3VF2C9957T1/pwyWXXKKvlEuqHfVXK9q6dauW/Le//U37uGPHjoULFypLFTLM1XwnnXSSMrZu3bqh+X/VVVc98sgj8+bNU0FSMi1B6devXz9p0iQdPm3SaaedNnz4cK00cPftHLjQgqF8Xrly5fTp05cuXao9bdGixfnnn69DoDIZJqCp2Oi8ULb89NNPOqwNGzbUdp577rmNGjVSfpp807apvM2ZM0e7rEOmrLjwwgszMjKs0aL93mWCXkRRgVdRL/eks84sO+Vh/0KcuRoizPmltasw/+c//9FGBj2NRdObNGmiLdTm2bwmwgxzKJ7bP8vCny8HErGt2urGG2/UlmhPFVH37t378MMPb9++Xcvv37+/JlpLe/fdd1esWKGweeqppyqEBj5C2H7dZ522OnbXXnvtxIkTP/jgg65du95///1mGCjMgTZ5rpSK0q1bt1b1V+3Pd41rsarEX3zxRf2r3TFrCdy1wKiiul5hPD09fdiwYaEPQrZTPZmd1brMzmovtmzZ8s9//lOhL7SYmQ6PdlO1mLZcs2vjzzzzTGWjiZNVrWEJd0AUdD0U8cwldR6/igZflMwMl5ifAcpNFutnxcMqUUg3benA17zuxzZUtHfm19DAKlLfmqioNWq6UpoHD2nJ5dakdvLK5IC5QCn0wl6zOgV2rcXsr1k15RAHiylRbkY3jyD1SF944QU1xUxP0vzwpcDx+uuvqxF/zTXXqNmtWDBr1qwvvvjil19+0V+1a60Ioqa5mlZqeGl2JVM7+PnnnzcjBZpF/QST8o033hgyZIgaZOanOU0ZN26cUiq+qM9gEj/33HNq5KlJqkZwYDzSYtUAfeWVV9Sk01ea8v7775uio2V27NhRm/HOO+/ceeed69atMz8U6Nu33npr5syZ6iY1btzY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b/78+aph9UGB/euvvx4wYEDgTyyM5uCQD+uQBUeK2n9qx5s7/O+8886///3vanv99NNPkydPDh1JUfts69atal2py92wYcP169crZimSnnjiiTfddJNCodW6VYh56qmnFFO6d++u6Wrh/frrr2o633777ccdd5xiipq8V111ldZ7/vnnmzs8Z8+evWjRIjUle/XqpXj61ltvKUIpZd26dc27sSvaBTX11NNQFFu1atW11147ePBgRU9FNDW4VWFoiprRisvatkqTKfApjr/yyiuBq1ZT2OaMdrJIGX788cePHDlSrdupU6euXbtWKZXPP/zwwyeffHL22Wc/+eST1rtmwtNc7777bphsPBQFRg30lJQUdR60djXZ1XCvXbu2+irKB/UNRo0ape7Qd999N2vWLHUOw++pqknzVgL1XlTxNGnSRB/0V+lVMynrxo4d+8Ybb2j5PXr0UOU0ffp05bxye9euXR999NGHH354EMd07Jdtq15UwVNlr7KtXsfw4cPPPffcNm3aqL+kDdMWPvPMMyoq2t/Q4qS5VH5Wrlx52223vffee82bN1dlrxxQQ0FtHZ2Dyjc1CNQO0O6rd2d2+YMPPtBnZbWyRTvORbNHCQUZm+VBha3SSKXit3v37sDztFGjRuHPL9PM1VmpOkKhac+ePSrG1jXqCjX6SmsPWmZFZ1lWVlaYs0xrrOr5Yr1PKvDEtBOxtV/t2rXr0KHDkiVLZsyYoV044YQTNm3apLrJXINT7c87erQKbacimNkAxVsl09KqhdxFVWndp4qsolvL7R9os2Fa5sUXX6xYmpeXp4lDhgwxPx2HWfj111//0EMP6VgrT0w9q1xat26d9co85faBVE/mRS2htYBimhao9SpImkGohQsXmmUqjXbNfg0LIMJZjzgIbatX8z8zXs37zMzMFStWnHTSSeYSG3Pnrz7Xq1dPcVKRRGHzyy+/VDXx7LPPnnbaaYpsqj4UQBTorFur1FxUXaMaREFSccOMIJtfI2zeHqtk1atXNw/+V3NUEUlBT0vo2LGjple6DeXu+8yZM1XJXnnlldZ7G7U948aN++9//1vVnOzSpcu0adPWrFmjaDlw4EBz25c2Tzlp7us/5phjFD+1OtXXF1xwgYKzudrU3BjLU3JwBAZ0zLsJgp60h8MzoKP2sRpbd9555zvvvKOgYK71OPnkkxUO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fclXrlw5atSoyMhI81DAAQMG/Pnnn2oXrLM/Grqrvd63b9+sWbOURu2FOqfFixc7OPNtCqkNsTbN8fHxYWFhOacMlKFK8uOPPyYmJkZFRf373/9++eWXtaXqaG0vylWDu23btvHjx586dUop1fX2799/48aN6mn0Ip9SqebfeecdVeakSZNMG9qlS5cGDRpo24cMGaIctHWqqOnTpy9atEg76/HHHy9VqpTjxVOVPvPMM2pz1buPHj1a2arjUeKPPvpo2rRpOc+Szd+aNWtUKvOABuPChQvK0M/iHzqqtVNcLXQkqPzqyWJiYnIeYGZLlVj9xLPPPqujWpupoj7//POdO3c+efJkQesWAADgGmLga0hfoLA8Z/RYyHIayCOPPKLIc8uWLT/99JM+26NHD9v8HYyCgoODAwIClNt7772noirGjo2NnTx5srbFkVMqzJ10FYPZ3v94586dWp3dAN7x4NmRaPzjjz/WQr1Qyq5du2qskfhfKrn53TFn6OjguMPB0qqGNbQxj6/SW+aGOIcOHXrllVd27dpVoONNWzds2LBPP/00OTnZLNGGmwu7ihUr9s8d5+Y+QTowNm/erNpQvSnwznW0ohGcCqlN+/zzz2MtVI2q3pkzZ+qYKVDd4ubBJVc3XvPmzdV864sXEhJibfTbtGkzZ84cfYtq1KhRpUqVv5JefYl6AvU0hSxPZDSX2FSoUKF69er62qszsL31ur7A5k7+q1atGjFihLU11OjaXDms9D179rS7wdiTTz65ffv2jz76SA3HV199pU5FQ/HLly/rhZZoXSaZGkq9e+XKlTFjxqix0zBerafph2yn/83rnD8IqBFZs2aNCqYWv1WrVpcuXTIPUFdHZZdYxVMBOnXqZKbeL168qIZV2ztjxgy7G+6oKVfPp6pTL6gGTmVWqYYPH273E4G5gLbQf6fA1UnPmzdPPc3ixYsHDRqkzVQlv/vuu3369NmzZ4+ay2rVqik3lUF7RKV98cUXC1o8VakqfMGCBVOnTlWllSlTRtt75MgRZaiiDhw4MGepbCswy8IUdfTo0fv37//6668bN25ctmzZsLAw7WLt02effdaca5prhZvMrfc2zitZXjvL3d1dq1O/qK3QztI+at++/bRp03IeYGZLFy5cqE79u+++U5HU40ZERKj869evHzx4sIN1m2tt5NwKcwybhTQ+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vv7222/t27dXox0VFaV/1Qt4Wij/b7/9tlevXmY5ABBs3wzB9o0qPAD8E27ZEwjVUitA118NA37//ffx48fbvpudne1qcbPNlSQkJGzatCk6OtqMB27OQgLAP9Roi6JnDw+PkSNHHj582LbRtia42ZpEDQPOnTunsYGGGT179nznnXfee++99u3bZ2VlBQUFbd26dfny5exfAATbFB4A/nbut8NG+vn5zZ07t3nz5l26dHEk/bFjx/bu3RsXF6fovE6dOnXr1s01WUxMjJIlJiaGhoY2atTIy8tLrX+uKa9cuaKu4sKFCxqlVK1atWnTpnl1D8pB+bRt2/ahhx5auHDh+fPnOUYB3G7UDEZERLz00ksrVqywu5lOrpKSkrZu3XrmzJmsrKySJUveddddRYoUyTXl/v37z549a86iVwufT6SulHv27ElLSytatGiTJk1Kly6dV8oHHnhgypQpc+bMef/991u3bm0W9u3bt2vXrr/99pua/SNHjrBPARBs3yTB9l8vPADcPG79CZ2MjAxz1dKIESNq1aqlJj6fxBcvXpw4ceKqVauioqIUx6tLCAoKateu3aRJk8qWLWub8t///vc777xz7tw55a/epUOHDho/eHp65sxz+fLlU6dOPXnypHojjSLMzdUU/deuXTtnYg1dFi5cqB4rPT39448/1uCEYxTAbUXtnuL1woUL//zzz2oq33jjjfzTf/PNN2qijx49qjZWH9TYoHz58q+88kqfPn1sk/3555+jRo3asGFDcnKyeoQyZcoogYuFXYZnz54dN27cd999Fx0drRbe29u7dOnSgwYNGjp0aF7n3g8cOLBHjx7BwcH/61zd3VUMfbyQ5WoydisAgu2bJNj+K4UHgJvNrX/PdkXtmZmZ6gbOnDkzcuRI9Rx5pVTs3rNnz7lz56ozMKf9629qaqo6CUXq6k6sKWfPnv3MM8+cOnVKg4f09HR98N8WOW+ZptyefvppdTAaovj7+yuBCrB+/fpu3bpp+JGzDOqBmjRpolXHx8fn9RMEANyqzGVKoqbVz8/vgw8+UIOZT/olS5Y88cQTBw8e/L/9mYVeqHFWE63PWpNFRESoGV+2bJlaYK1CjfyhQ4cmTJhw/vx5jSVsM4yMjHz88cfVniclJekttclm+KHuQ+nzKoYabdvZHFELv2HDBm9vb7XkjRs3Zs8CINi+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cfnllyvx34RHjRolC20228qVK08++eSTTjrpuOOOk5jc0tLStsWNXAguueQSWSjB/LXXXpNYfeutt44fP/7444//3e9+N3fu3O02v5c6yQUXXLB06VKpDOiz8E6aNOm0zeS9rrrqKubBBUBh+8AvbO9k5wHgwPSL7XIV3axdm8lzzjnnyy+/fPzxx6Xkra+QeOqaa65Zvnz5m2++KReVFStWfP/995a4+vp6uYRIpUJfrWfPnnfeeadcJPRCf1FRkaxptVq7dOlSXV3d9jXz8/MffPBBqR5UVVXJwueff16uEPKCUuJ/7LHH5EI1derU3fgIAPDLI4EuEfTaLpdYLYH0pJNOksK63vEqERI7dep0//33X3bZZV6vV5bPmjVLnrLb7aFQyGazSaBODEh8ww03SKD+6KOP5NV8Pt+CBQv8fr9sbjKZ5GXbvubVV18t8f+VV16R11myZMnChQtlHXm1pqYmqSd8/PHH+gA9bZWVlckmcjnQ2/8XFBQkxnFQ4sNtyqWBMA6AwvYBVdjejZ0HgAPQL7aFjnUzCejtnpo2bdoRRxwhAVpfoW21QS4Dt99+u1wbzGazlObl2aysLKkJvPbaa20Hbzv33HOluH/UUUfJBUNWGzBggFQqLr300nA43O415eI0e/bsUaNG6UP6u1wuuSz16dPnoYceGjt27G5/BAD4pV2N4qNatguhukGDBklk1gv97ULiySef/Pbbb59wwgl6xNbvjzzyyNdff/38889PrJaWlvbyyy+PHz9eQrpsLn+OHj366aefzsvL04fISbymPgP6vffe26tXL3k7Z1xycrKEfXmFbt26bbvnsppEeH3P9U08baSkpMjFhf8vAArbB1Rhezd2HgAOQKby8vJ9/66xWCw9Pb3dHLR7kYTgiooKifjyODU1Vcri7VZobGysq6vTf3fNzs5u11FWnlqxYoUcGXmqf//+iTlu25HX37RpUygUysnJkVJ7S0tLdXW1vJRceGRJu8vD6tWr5TVlxzp16tSvX79td2knH0GOlVyiOFkB7DYJa4FAYLcHBdBbvqSlpf18eyhhub6+Xs+PbBtClfiombG4bUOiLPzxxx9XrlwpH7Bnz559+/bd0dDFEqVrampkc326q7Kysh1dKWR/li1bJhcCCe9SMejevfuO9lyuApWVlTtqgyPLt3uhAYCdCAaDtbW1exI3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KSlZWVnbfVYCrzwrZei9vu0uampq+tvf/ta9e/drrrkmsVBK83PmzLn++uulTH/YYYeFw+HvvvuuU6dOH3744bBtG58mrjVx9913X3V1dTQatVgsFRUVkUjkjDPOuPXWW/fO1IQAQNDeS0F77dq1Nputb9++Dz744MMPP+zxeDIyMmT3brrpppNOOkmCubwL5wNI6AB7JBYIKNGoEg7rf4YUxayq5u7dTT16WPr3b7dyUlGR6YgjrGPG2C65JKWpKZbI+FRWWkpLY8uXm9evN3ftavJ6tQ5NmzYphYWJjI9PUdSsLP8zzwSfeaYl3k0pMVGXKStLzcuzdekSnD9fcbv9d9wRicVa5BVqa7XBa+LTwJtDIXmRqxTlu6Skd3y+jP/+tznexEZNSorl5XkrK2ORSOzgg8u7dZNSfmTNmohsft11jrPPttnt2nslJW07pff6yso/3377qaeeemPbUeWCQa3S0NyskNABYAShUMhsNu+oI5LJZJKn2jX43yvb7gop9EuVYOnSpZ9++ml6enrbp7xer8Ra2YH169fLWwQCAXns8/l28mqZmZlnnXWW1FjOPPPMXr16uVyumpqat956S+oGa9asefvtt9uO1gkABO39G7QrKiokYkuIlg2ffvrpww47zOl0NjY2fvDBB1deeeWf/vQneeDZZgwHgIQOsPucdruE8qjfv/3sj8kkEdyclqZ066b159q6PWfqyy+HrrjC9eabjm7dbPG2M9HCwsjKlZFVq6wFBaaiokgsJtvHfL4tc3j/8EMi4yMCcinKywvOnBmKp5aUzX2jzPGv0/ikpHfc7lcHDDh62LBA376eAQPU/HzV7b7n4Ydvf+mlWx955ILRo9PiWZuapqbn/v3v0+64457OnS/905+2+1nkcnLR6NF9unT597/+1Xa51WqVy2FSUhInAwBjxG2nU4vbOyjBSzFantpR6X9Ptt0VN9xww+uvvz579uyhQ4e2XX7fffdNmzbt1ltvveCCC/Q6Q01NzXPPPfd///d/995776WXXrrdV8vOzn7qqafaLnG5XFL3SElJufjii996663zzz+f8wEAQfsACdpSqK6uru7atetDDz2UGKc5OTn57LPPlg9y+umnP//881dddRWnBA5YJHRgPN26dWtoaCgvLz/ooIO2fbaqurre6+3Rp0/rZaOpKab3h6qrM9fW5i1a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ES72lJbqSU5OrlGjRkFBQfEHyvLy8ipUqMDmOAAAAAAA4IyU5Qqd+Pj4fv36bdy40Y5ERUW98847MTExw4YN0097wCowMPDAgQOPP/74Bx98sHbt2qlTpzZo0MBZ/1JckYvza2Zmpr0WPcD1QiuPXXscubm5devWffrpp48dO3b48OEjR47s3r17zZo1y5YtUzsjIyPVhv379ycnJ1tCx+MqIS72QQWqVq1auXLlH3/8UZfLy8tTg19//XV9sHPtxeSFhYW6C91ddna2l9sBAAAAAAAoLqgMr52Tk9O/f/927drZHsP2LNJLL700YMAA/Vy0aNG//vWvJ554om/fvosXL65QocLu3btvvfXW1atXOzma4kJd7HNYWNi8efM2b94cGxsbFRX16aef7tmzx96S7i4kJCQjI2P48OHvv/++2lCvXr0uXboMHTr0ySefLFeunGVhgoKC3NfXOBkc+2rTpk0//vhjeHj4kSNHVFVCQkLnzp0tTRMZGalqx48fn5aWVuiyffv2Bx54YO3atfpWhdkfBwAAAAAAnKmy3BT55MmTMTExEyZMuPnmm7/77ruoqKigoKDIyMjNmzevX7/elsDoSFhYmL4KcD3KtGPHjjVr1nTq1KnECgsLCytVqpSYmHj8+PHg4ODQ0NBDhw4NGjSoVatWubm5OjE7O1uVeGyurPrfeOONadOmzZ49u0mTJu3atbvwwgsLCgpWrFihekJCQnRujRo1qlevbs9GqdnlypWzR7F0FVX4ySef9O7dWwd1F1OmTElKStIdLViwYO/evWq5Lvfss88uXLhQ1ebl5X3++ef79+9ftmzZuHHjunTpcs53BQIAAAAAAL95IWV7+dzc3Pr167/22msPPfTQli1boqOjg4ODw12KlwwMDBw+fPjQoUOL75psTp48mZiY2KtXr6efftpW4uhnSkrKRx99pFNq1qypbw8dOuT+4FVERMTy5ctffvnlhISEoKAge8WVZXxCQkL0re1PfMstt1SsWNG279FVKlWq1LRp0927d9tVVOH+/fu//vpre65KqlSp8sQTT9x9993p6emRkZFq+bZt27744osA1xqicuXKHThw4Lbbbps5c+all17K/scAAAAAAOCMBJV5C7Kzs5s3bz5z5sw77rgjPDw8KyvLtpUxeXl5+jUnJ6dBgwYvvfTSmDFjgoODT506VVRU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6E9+4MCB+ndA3bhjx46cnBwN1mkTOvo3YdWqVcOGDdM46rOOXHfddTVr1tQ/Dj7Wf6bzxMfCmgAXXnihrrJp06aVK1dqPmta8q8HAAAAgN9IQkcB2N/+9rdJkybFxsY+//zzCo/z8/NDQ0NffPHFNWvWKATStwqkFYMpQlOY1KtXrxYtWmRlZT388MPVq1d3j450lkJEhdyKuBTL2XNb7tGjba6h+C3cxcrYzhe25uK/+iU4ODo6WlUpKtNVqlWr1qlTp/Lly+vS7ttkuF9Un4vvt6or2nYwVsbL5qm2JYdd0b2MPTZiuzI7jXSvVl/ZYocS2++sVXGvymlGad3iXMU2NirtBt1PVwF9VhlbsOBezL0xtvWMitkWOc6dqsy3334bFxenyaB4e9euXU5Cx27Wubqa9M477yxZsqR+/frTp09v0qSJKq9SpUq3bt3WrVu3Z88e1danTx81SS0ZN27cihUr6tat+9Zbb/Xo0aNixYr6rPBbxXbu3Kmf3bt3j4+P19V/+OGHiRMnpqenjxgxQn8UmpkJCQmabImJiR9//LG+7dy5c61atdSYL7744tFHH1X999xzzzPPPKODlStX7tix40UXXfTvf/977969OleFT/u40O98xPVV1apVNb6tW7fW335ycrL+zHWka9eux44d27BhQ15env72VY9dt8S/L9W8e/fuIUOGpKSk3HjjjRomjeB1112nQcnNzfWxft2Oj/NEV/d9UqmL9PPKK688cODApk2bduzYccUVV5QrV85j4AAAAADg7JTlHq6K0BSAvf7664p8brrppr59+2ZkZFjAphBIYY+isoYNG6amproHqB06dGjZsqU+O0+12I4q+/btUzz//fffKw5v3rx5s2bN7DkICy/Xr19/9OjRpKSktm3bfvbZZ8uWLbvwwgsVzn3yySeZmZkVKlRQ6O4EWip//PhxxWCqoUmTJtWqVVu9erWdrpqtmIXK3377rWr75ptv1AAFdfpWVTkPViiCVVSv2M+WA1x88cXt27dX+KfPnnm14OC9LqpWkacqca6iiHTt2rVZWVk6UV/puEJuxaL/+c9/tm7dqvC1evXq6hBdXQedzTsUsm7evFmf1aTExESdpahVPaaqdL8qXLt2bX1bvFt0/Nprr7VNSXQjusSXX355+PBh3ax6TLGxanOePLLTFSfrdIWytp2NblPtsUZ6NEa3r2pXrVq1f/9+RbZqmy5ne4voZ7du3Xr37q0A2/3FQGq2emDGjBn6OXDgQNtf9sSJE7qj6i7qAR3RtTTu9evX1y3YU1rq/K+++mrp0qX6cOeddzZu3FgTyerUvQwfPnzNmjVqxqJFi4YMGaJ5om5RG3Q5zQSNmrN3T4MGDRSWqwdsTxa1/7333ktJSdFY3HPPPTpoWUWdq3C9T58+b7zxxvz58wcNGuT90TxG3HJMI0aMsP2JbZ+sANcDTTrrxRdfVO+ppL5Vte4TwEkJaWQ1E0aOHKkG33///TfffPPixYudHvaxfv3lbt++3cd5oi71fVKpwZpIavDjjz++3UVzY9y4cT5uDAQAAAAA529CR0GR4sndu3crbrzjjjvcd6lQDKk4ULGTCnTs2DHQxRI0OTk59p5gJ5ujeqZOnfrqq6/u27fPOf2Pf/zjqFGj7C1IitkmTJjwySef9OjRQxHg7bffruhOgXqvXr0UKM6dO7dWrVoLFixQmGrBeWRkpIJ2hWGKyT/66KP69evb6V26dPnnP/9pi3RCQkL+/ve/T548ec+ePc5ZjRo1UmB55ZVXqnm6qMJ1VfLpp59aikGBZdOmTR977LFu3bp57KahqO+bb75RRKo4XAUefvhhiz9ViULoAQMGKPIcPXp0u3btVEAln3jiiRUrVqSlpVkPKMIfNGjQvffea6stdNauXbtuvPFGfTtv3jxdTg3QV7b8RKc/+uijuoS+Ld4tutmrr75asffs2bNff/111WMZE2uMIlid0qJFC4uE7fTOnTvrlp999ll72VNcXNyll1761FNPaVitmDVGPfb0009rQJcvX67+0fiq2UOHDh08eLA60NY+KHR3H1y7qPr5kUce0eirl2677TZ9q35Q29TzW7ZsSU5O1lVUW0pKyueff65TLN+n+920adOPP/5Yo0YNDZx7Ek2fNfrNmzefP3++InDNPTVAc+Ciiy769ttvP/74Y005hf26osZ0w4YNR44cUSUqoCMK4Ddv3qzb7Nq1a8WKFTMyMpz0gXpePanWKqTX1FUneEnoMOKWcNFwuy8psoFTD+ug/vrUKp01Z84c9wlgfzv2uKW6Tt1y1VVX6Q9Nf24ey998qV/t932e6I58L2zHNaVtsNT/ixYtuvPOOytXrsyDVwAAAAD8OKGjOErhroI9/ezUqVPt2rWd/4Wu6EvhouJSBdJDhgxRxN6oUSMF24qLKlWqpJ8KyZzlOYoeX3rpJQWTOqgwtU2bNorrFi5cqNBUFT7//POWIFBkHhYWpkjsmWeeadq06SWXXGKbpN5yyy2KNnUhhan6bA/4KGhfsmSJKuzVq1ezZs10LXsftn5aZBgVFTV9+nTF22p8tWrVVEbfbtmy5bPPPlME27Jly6pVqx44cEDB2+eff66Wq57o6GjVqV8V0E6bNk0BsHs0qKhPR9T4jRs3rly5UmXUDAtHFyxYYJtx9O/fXyV/+OEHq7Z8+fJ9+/atUqWKIkz9qkhbMbzidnssxZ55ceJep8/tQRh7+MuSUMW7RV/pujrxiy++UDyvg0lJSd98882qVat0jw899NA//vEPRcLWq6pwx44dW7duVSeo2Pfff79t2zbd6bFjx9555x010mmMqJEVKlRQs9VvOuXgwYMKyPXtrbfe6uWdZRoUW71i+RH1laaHAmYNwV133aW+qlevnkZQvareu/zyywcPHpyfn6/72rNnj3pDXVSxYkX33Io1qUmTJpon6k8Nt9qmexk1apTaP3XqVM2ca665Rkf+/e9/6yoxMTEjRoyoVauWmnH48OGUlJTQ0ND69et7PDujdtasWVOXU1/t27evY8eOXuY/I255GY8UjOrXrb333ntquf5qEhIS7JlH9wngpHF1C++++67G8dlnn9W1SkyfnbZ+1ez7PFGBM5pU1mz9pV9xxRWvvvrq/v37165de/3115PQAQAAAODHCR0FP4qNFTQqnlTo6x7M5+bm9uzZ87vvvpsyZYoiz/nz5yvEVcCp6EvhYoMGDQYOHKi4XdGU4urt27ermM665557Ro8ebYHrrFmzHn744Tlz5iiOuvbaa61aFd69e/ewYcPuv//+iIgIewlOy5YtGzVqtH79+n/9618KtBTmhYeHr1u3TiGr4rHevXu775hjdIkvv/zyhRde0Olt27ZVVKkadFwtefnllxWEV6pUSb+qVZs3b27YsOEbb7yRnJysI4MGDbrvvvsU+j733HM6YjuPWJ2qSgHzVVddpVhdle/cudOe7VK0rGhfd6TgXxG+Prz22muKuhVMKlTu16+fbur48eNjxoxRZDt9+vSuXbt26NDhjAaieLfk5+frZ7du3dQnderUueCCC6wTdMuKnO1BGzXVaXlsbOz//M//aESioqIUx6oZ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" alt="OpenShift Container Platform Ingress LoadBalancerService endpoint publishing strategy" />
<figcaption>Diagram of LoadBalancer</figcaption>
</figure>

The preceding graphic shows the following concepts pertaining to OpenShift Container Platform Ingress LoadBalancerService endpoint publishing strategy:

- You can load balance externally, using the cloud provider load balancer, or internally, using the OpenShift Ingress Controller Load Balancer.

- You can use the single IP address of the load balancer and more familiar ports, such as 8080 and 4200 as shown on the cluster depicted in the graphic.

- Traffic from the external load balancer is directed at the pods, and managed by the load balancer, as depicted in the instance of a down node. See the [Kubernetes Services documentation](https://kubernetes.io/docs/concepts/services-networking/service/#internal-load-balancer) for implementation details.

<div>

<div class="title">

Prerequisites

</div>

- Install the OpenShift CLI (`oc`).

- Log in as a user with `cluster-admin` privileges.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create an `IngressController` custom resource (CR) in a file named `<name>-ingress-controller.yaml`, such as in the following example:

    ``` yaml
    apiVersion: operator.openshift.io/v1
    kind: IngressController
    metadata:
      namespace: openshift-ingress-operator
      name: <name>
    spec:
      domain: <domain>
      endpointPublishingStrategy:
        type: LoadBalancerService
        loadBalancer:
          scope: Internal
    ```

    - Replace `<name>` with a name for the `IngressController` object.

    - Specify the `domain` for the application published by the controller.

    - Specify a value of `Internal` to use an internal load balancer.

2.  Create the Ingress Controller defined in the previous step by running the following command:

    ``` terminal
    $ oc create -f <name>-ingress-controller.yaml
    ```

    - Replace `<name>` with the name of the `IngressController` object.

3.  Optional: Confirm that the Ingress Controller was created by running the following command:

    ``` terminal
    $ oc --all-namespaces=true get ingresscontrollers
    ```

</div>

## Configuring global access for an Ingress Controller on Google Cloud

An Ingress Controller created on Google Cloud with an internal load balancer generates an internal IP address for the service. A cluster administrator can specify the global access option, which enables clients in any region within the same VPC network and compute region as the load balancer, to reach the workloads running on your cluster.

For more information, see the Google Cloud documentation for [global access](https://cloud.google.com/kubernetes-engine/docs/how-to/internal-load-balancing#global_access).

<div>

<div class="title">

Prerequisites

</div>

- You deployed an OpenShift Container Platform cluster on Google Cloud infrastructure.

- You configured an Ingress Controller to use an internal load balancer.

- You installed the OpenShift CLI (`oc`).

</div>

<div>

<div class="title">

Procedure

</div>

1.  Configure the Ingress Controller resource to allow global access.

    > [!NOTE]
    > You can also create an Ingress Controller and specify the global access option.

    1.  Configure the Ingress Controller resource:

        ``` terminal
        $ oc -n openshift-ingress-operator edit ingresscontroller/default
        ```

    2.  Edit the YAML file:

        <div class="formalpara">

        <div class="title">

        Sample `clientAccess` configuration to `Global`

        </div>

        ``` yaml
          spec:
            endpointPublishingStrategy:
              loadBalancer:
                providerParameters:
                  gcp:
                    clientAccess: Global
                  type: GCP
                scope: Internal
              type: LoadBalancerService
        ```

        </div>

        - Set `gcp.clientAccess` to `Global`.

    3.  Save the file to apply the changes.

2.  Run the following command to verify that the service allows global access:

    ``` terminal
    $ oc -n openshift-ingress edit svc/router-default -o yaml
    ```

    The output shows that global access is enabled for Google Cloud with the annotation, `networking.gke.io/internal-load-balancer-allow-global-access`.

</div>

## Setting the Ingress Controller health check interval

A cluster administrator can set the health check interval to define how long the router waits between two consecutive health checks. This value is applied globally as a default for all routes. The default value is 5 seconds.

<div>

<div class="title">

Prerequisites

</div>

- The following assumes that you already created an Ingress Controller.

</div>

<div>

<div class="title">

Procedure

</div>

- Update the Ingress Controller to change the interval between back end health checks:

  ``` terminal
  $ oc -n openshift-ingress-operator patch ingresscontroller/default --type=merge -p '{"spec":{"tuningOptions": {"healthCheckInterval": "8s"}}}'
  ```

  > [!NOTE]
  > To override the `healthCheckInterval` for a single route, use the route annotation `router.openshift.io/haproxy.health.check.interval`

</div>

## Configuring the default Ingress Controller for your cluster to be internal

You can configure the `default` Ingress Controller for your cluster to be internal by deleting and recreating it.

> [!WARNING]
> If your cloud provider is Microsoft Azure, you must have at least one public load balancer that points to your nodes. If you do not, all of your nodes will lose egress connectivity to the internet.

> [!IMPORTANT]
> If you want to change the `scope` for an `IngressController`, you can change the `.spec.endpointPublishingStrategy.loadBalancer.scope` parameter after the custom resource (CR) is created.

<div>

<div class="title">

Prerequisites

</div>

- Install the OpenShift CLI (`oc`).

- Log in as a user with `cluster-admin` privileges.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Configure the `default` Ingress Controller for your cluster to be internal by deleting and recreating it.

    ``` terminal
    $ oc replace --force --wait --filename - <<EOF
    apiVersion: operator.openshift.io/v1
    kind: IngressController
    metadata:
      namespace: openshift-ingress-operator
      name: default
    spec:
      endpointPublishingStrategy:
        type: LoadBalancerService
        loadBalancer:
          scope: Internal
    EOF
    ```

</div>

## Configuring the route admission policy

Administrators and application developers can run applications in multiple namespaces with the same domain name. This is for organizations where multiple teams develop microservices that are exposed on the same hostname.

> [!WARNING]
> Allowing claims across namespaces should only be enabled for clusters with trust between namespaces, otherwise a malicious user could take over a hostname. For this reason, the default admission policy disallows hostname claims across namespaces.

<div>

<div class="title">

Prerequisites

</div>

- Cluster administrator privileges.

</div>

<div>

<div class="title">

Procedure

</div>

- Edit the `.spec.routeAdmission` field of the `ingresscontroller` resource variable using the following command:

  ``` terminal
  $ oc -n openshift-ingress-operator patch ingresscontroller/default --patch '{"spec":{"routeAdmission":{"namespaceOwnership":"InterNamespaceAllowed"}}}' --type=merge
  ```

  <div class="formalpara">

  <div class="title">

  Sample Ingress Controller configuration

  </div>

  ``` yaml
  spec:
    routeAdmission:
      namespaceOwnership: InterNamespaceAllowed
  ...
  ```

  </div>

  > [!TIP]
  > You can alternatively apply the following YAML to configure the route admission policy:
  >
  > ``` yaml
  > apiVersion: operator.openshift.io/v1
  > kind: IngressController
  > metadata:
  >   name: default
  >   namespace: openshift-ingress-operator
  > spec:
  >   routeAdmission:
  >     namespaceOwnership: InterNamespaceAllowed
  > ```

</div>

## Using wildcard routes

The HAProxy Ingress Controller has support for wildcard routes. The Ingress Operator uses `wildcardPolicy` to configure the `ROUTER_ALLOW_WILDCARD_ROUTES` environment variable of the Ingress Controller.

The default behavior of the Ingress Controller is to admit routes with a wildcard policy of `None`, which is backwards compatible with existing `IngressController` resources.

<div>

<div class="title">

Procedure

</div>

1.  Configure the wildcard policy.

    1.  Use the following command to edit the `IngressController` resource:

        ``` terminal
        $ oc edit IngressController
        ```

    2.  Under `spec`, set the `wildcardPolicy` field to `WildcardsDisallowed` or `WildcardsAllowed`:

        ``` yaml
        spec:
          routeAdmission:
            wildcardPolicy: WildcardsDisallowed # or WildcardsAllowed
        ```

</div>

## HTTP header configuration

To customize request and response headers for your applications, configure the Ingress Controller or apply specific route annotations. Understanding the interaction between these configuration methods ensures you effectively manage global and route-specific header policies.

You can also set certain headers by using route annotations. The various ways of configuring headers can present challenges when working together.

> [!NOTE]
> You can only set or delete headers within an `IngressController` or `Route` CR, you cannot append them. If an HTTP header is set with a value, that value must be complete and not require appending in the future. In situations where it makes sense to append a header, such as the X-Forwarded-For header, use the `spec.httpHeaders.forwardedHeaderPolicy` field, instead of `spec.httpHeaders.actions`.

Order of precedence
When the same HTTP header is modified both in the Ingress Controller and in a route, HAProxy prioritizes the actions in certain ways depending on whether it is a request or response header.

- For HTTP response headers, actions specified in the Ingress Controller are executed after the actions specified in a route. This means that the actions specified in the Ingress Controller take precedence.

- For HTTP request headers, actions specified in a route are executed after the actions specified in the Ingress Controller. This means that the actions specified in the route take precedence.

For example, a cluster administrator sets the X-Frame-Options response header with the value `DENY` in the Ingress Controller using the following configuration:

<div class="formalpara">

<div class="title">

Example `IngressController` spec

</div>

``` yaml
apiVersion: operator.openshift.io/v1
kind: IngressController
# ...
spec:
  httpHeaders:
    actions:
      response:
      - name: X-Frame-Options
        action:
          type: Set
          set:
            value: DENY
```

</div>

A route owner sets the same response header that the cluster administrator set in the Ingress Controller, but with the value `SAMEORIGIN` using the following configuration:

<div class="formalpara">

<div class="title">

Example `Route` spec

</div>

``` yaml
apiVersion: route.openshift.io/v1
kind: Route
# ...
spec:
  httpHeaders:
    actions:
      response:
      - name: X-Frame-Options
        action:
          type: Set
          set:
            value: SAMEORIGIN
```

</div>

When both the `IngressController` spec and `Route` spec are configuring the X-Frame-Options response header, then the value set for this header at the global level in the Ingress Controller takes precedence, even if a specific route allows frames. For a request header, the `Route` spec value overrides the `IngressController` spec value.

This prioritization occurs because the `haproxy.config` file uses the following logic, where the Ingress Controller is considered the front end and individual routes are considered the back end. The header value `DENY` applied to the front end configurations overrides the same header with the value `SAMEORIGIN` that is set in the back end:

``` text
frontend public
  http-response set-header X-Frame-Options 'DENY'

frontend fe_sni
  http-response set-header X-Frame-Options 'DENY'

frontend fe_no_sni
  http-response set-header X-Frame-Options 'DENY'

backend be_secure:openshift-monitoring:alertmanager-main
  http-response set-header X-Frame-Options 'SAMEORIGIN'
```

Additionally, any actions defined in either the Ingress Controller or a route override values set using route annotations.

Special case headers
The following headers are either prevented entirely from being set or deleted, or allowed under specific circumstances:

<table>
<caption>Special case header configuration options</caption>
<colgroup>
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Header name</th>
<th style="text-align: left;">Configurable using <code>IngressController</code> spec</th>
<th style="text-align: left;">Configurable using <code>Route</code> spec</th>
<th style="text-align: left;">Reason for disallowment</th>
<th style="text-align: left;">Configurable using another method</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>proxy</code></p></td>
<td style="text-align: left;"><p>No</p></td>
<td style="text-align: left;"><p>No</p></td>
<td style="text-align: left;"><p>The <code>proxy</code> HTTP request header can be used to exploit vulnerable CGI applications by injecting the header value into the <code>HTTP_PROXY</code> environment variable. The <code>proxy</code> HTTP request header is also non-standard and prone to error during configuration.</p></td>
<td style="text-align: left;"><p>No</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>host</code></p></td>
<td style="text-align: left;"><p>No</p></td>
<td style="text-align: left;"><p>Yes</p></td>
<td style="text-align: left;"><p>When the <code>host</code> HTTP request header is set using the <code>IngressController</code> CR, HAProxy can fail when looking up the correct route.</p></td>
<td style="text-align: left;"><p>No</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>strict-transport-security</code></p></td>
<td style="text-align: left;"><p>No</p></td>
<td style="text-align: left;"><p>No</p></td>
<td style="text-align: left;"><p>The <code>strict-transport-security</code> HTTP response header is already handled using route annotations and does not need a separate implementation.</p></td>
<td style="text-align: left;"><p>Yes: the <code>haproxy.router.openshift.io/hsts_header</code> route annotation</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>cookie</code> and <code>set-cookie</code></p></td>
<td style="text-align: left;"><p>No</p></td>
<td style="text-align: left;"><p>No</p></td>
<td style="text-align: left;"><p>The cookies that HAProxy sets are used for session tracking to map client connections to particular back-end servers. Allowing these headers to be set could interfere with HAProxy’s session affinity and restrict HAProxy’s ownership of a cookie.</p></td>
<td style="text-align: left;"><p>Yes:</p>
<ul>
<li><p>the <code>haproxy.router.openshift.io/disable_cookie</code> route annotation</p></li>
<li><p>the <code>haproxy.router.openshift.io/cookie_name</code> route annotation</p></li>
</ul></td>
</tr>
</tbody>
</table>

## Setting or deleting HTTP request and response headers in an Ingress Controller

You can set or delete certain HTTP request and response headers for compliance purposes or other reasons. You can set or delete these headers either for all routes served by an Ingress Controller or for specific routes.

For example, you might want to migrate an application running on your cluster to use mutual TLS, which requires that your application checks for an X-Forwarded-Client-Cert request header, but the OpenShift Container Platform default Ingress Controller provides an X-SSL-Client-Der request header.

The following procedure modifies the Ingress Controller to set the X-Forwarded-Client-Cert request header, and delete the X-SSL-Client-Der request header.

<div>

<div class="title">

Prerequisites

</div>

- You have installed the OpenShift CLI (`oc`).

- You have access to an OpenShift Container Platform cluster as a user with the `cluster-admin` role.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Edit the Ingress Controller resource:

    ``` terminal
    $ oc -n openshift-ingress-operator edit ingresscontroller/default
    ```

2.  Replace the X-SSL-Client-Der HTTP request header with the X-Forwarded-Client-Cert HTTP request header:

    ``` yaml
    apiVersion: operator.openshift.io/v1
    kind: IngressController
    metadata:
      name: default
      namespace: openshift-ingress-operator
    spec:
      httpHeaders:
        actions:
          request:
          - name: X-Forwarded-Client-Cert
            action:
              type: Set
              set:
               value: "%{+Q}[ssl_c_der,base64]"
          - name: X-SSL-Client-Der
            action:
              type: Delete
    ```

    - The list of actions you want to perform on the HTTP headers.

    - The type of header you want to change. In this case, a request header.

    - The name of the header you want to change. For a list of available headers you can set or delete, see *HTTP header configuration*.

    - The type of action being taken on the header. This field can have the value `Set` or `Delete`.

    - When setting HTTP headers, you must provide a `value`. The value can be a string from a list of available directives for that header, for example `DENY`, or it can be a dynamic value that will be interpreted using HAProxy’s dynamic value syntax. In this case, a dynamic value is added.

      > [!NOTE]
      > For setting dynamic header values for HTTP responses, allowed sample fetchers are `res.hdr` and `ssl_c_der`. For setting dynamic header values for HTTP requests, allowed sample fetchers are `req.hdr` and `ssl_c_der`. Both request and response dynamic values can use the `lower` and `base64` converters.

3.  Save the file to apply the changes.

</div>

## Using X-Forwarded headers

You configure the HAProxy Ingress Controller to specify a policy for how to handle HTTP headers including `Forwarded` and `X-Forwarded-For`. The Ingress Operator uses the `HTTPHeaders` field to configure the `ROUTER_SET_FORWARDED_HEADERS` environment variable of the Ingress Controller.

<div>

<div class="title">

Procedure

</div>

1.  Configure the `HTTPHeaders` field for the Ingress Controller.

    1.  Use the following command to edit the `IngressController` resource:

        ``` terminal
        $ oc edit IngressController
        ```

    2.  Under `spec`, set the `HTTPHeaders` policy field to `Append`, `Replace`, `IfNone`, or `Never`:

        ``` yaml
        apiVersion: operator.openshift.io/v1
        kind: IngressController
        metadata:
          name: default
          namespace: openshift-ingress-operator
        spec:
          httpHeaders:
            forwardedHeaderPolicy: Append
        ```

</div>

### Example use cases

**As a cluster administrator, you can:**

- Configure an external proxy that injects the `X-Forwarded-For` header into each request before forwarding it to an Ingress Controller.

  To configure the Ingress Controller to pass the header through unmodified, you specify the `never` policy. The Ingress Controller then never sets the headers, and applications receive only the headers that the external proxy provides.

- Configure the Ingress Controller to pass the `X-Forwarded-For` header that your external proxy sets on external cluster requests through unmodified.

  To configure the Ingress Controller to set the `X-Forwarded-For` header on internal cluster requests, which do not go through the external proxy, specify the `if-none` policy. If an HTTP request already has the header set through the external proxy, then the Ingress Controller preserves it. If the header is absent because the request did not come through the proxy, then the Ingress Controller adds the header.

**As an application developer, you can:**

- Configure an application-specific external proxy that injects the `X-Forwarded-For` header.

  To configure an Ingress Controller to pass the header through unmodified for an application’s Route, without affecting the policy for other Routes, add an annotation `haproxy.router.openshift.io/set-forwarded-headers: if-none` or `haproxy.router.openshift.io/set-forwarded-headers: never` on the Route for the application.

  > [!NOTE]
  > You can set the `haproxy.router.openshift.io/set-forwarded-headers` annotation on a per route basis, independent from the globally set value for the Ingress Controller.

## Enable or disable HTTP/2 on Ingress Controllers

You can enable or disable transparent end-to-end HTTP/2 connectivity in HAProxy. Application owners can use HTTP/2 protocol capabilities, including single connection, header compression, binary streams, and more.

You can enable or disable HTTP/2 connectivity for an individual Ingress Controller or for the entire cluster.

> [!NOTE]
> If you enable or disable HTTP/2 connectivity for an individual Ingress Controller and for the entire cluster, the HTTP/2 configuration for the Ingress Controller takes precedence over the HTTP/2 configuration for the cluster.

To enable the use of HTTP/2 for a connection from the client to an HAProxy instance, a route must specify a custom certificate. A route that uses the default certificate cannot use HTTP/2. This restriction is necessary to avoid problems from connection coalescing, where the client re-uses a connection for different routes that use the same certificate.

Consider the following use cases for an HTTP/2 connection for each route type:

- For a re-encrypt route, the connection from HAProxy to the application pod can use HTTP/2 if the application supports using Application-Level Protocol Negotiation (ALPN) to negotiate HTTP/2 with HAProxy. You cannot use HTTP/2 with a re-encrypt route unless the Ingress Controller has HTTP/2 enabled.

- For a passthrough route, the connection can use HTTP/2 if the application supports using ALPN to negotiate HTTP/2 with the client. You can use HTTP/2 with a passthrough route if the Ingress Controller has HTTP/2 enabled or disabled.

- For an edge-terminated secure route, the connection uses HTTP/2 if the service specifies only `appProtocol: kubernetes.io/h2c`. You can use HTTP/2 with an edge-terminated secure route if the Ingress Controller has HTTP/2 enabled or disabled.

- For an insecure route, the connection uses HTTP/2 if the service specifies only `appProtocol: kubernetes.io/h2c`. You can use HTTP/2 with an insecure route if the Ingress Controller has HTTP/2 enabled or disabled.

> [!IMPORTANT]
> For non-passthrough routes, the Ingress Controller negotiates its connection to the application independently of the connection from the client. This means a client might connect to the Ingress Controller and negotiate HTTP/1.1. The Ingress Controller might then connect to the application, negotiate HTTP/2, and forward the request from the client HTTP/1.1 connection by using the HTTP/2 connection to the application.
>
> This sequence of events causes an issue if the client subsequently tries to upgrade its connection from HTTP/1.1 to the WebSocket protocol. Consider that if you have an application that is intending to accept WebSocket connections, and the application attempts to allow for HTTP/2 protocol negotiation, the client fails any attempt to upgrade to the WebSocket protocol.

### Enabling HTTP/2

You can enable HTTP/2 on a specific Ingress Controller, or you can enable HTTP/2 for the entire cluster.

<div>

<div class="title">

Procedure

</div>

- To enable HTTP/2 on a specific Ingress Controller, enter the `oc annotate` command:

  ``` terminal
  $ oc -n openshift-ingress-operator annotate ingresscontrollers/<ingresscontroller_name> ingress.operator.openshift.io/default-enable-http2=true
  ```

  - Replace `<ingresscontroller_name>` with the name of an Ingress Controller to enable HTTP/2.

- To enable HTTP/2 for the entire cluster, enter the `oc annotate` command:

  ``` terminal
  $ oc annotate ingresses.config/cluster ingress.operator.openshift.io/default-enable-http2=true
  ```

</div>

> [!TIP]
> Alternatively, you can apply the following YAML code to enable HTTP/2:
>
> ``` yaml
> apiVersion: config.openshift.io/v1
> kind: Ingress
> metadata:
>   name: cluster
>   annotations:
>     ingress.operator.openshift.io/default-enable-http2: "true"
> ```

### Disabling HTTP/2

You can disable HTTP/2 on a specific Ingress Controller, or you can disable HTTP/2 for the entire cluster.

<div>

<div class="title">

Procedure

</div>

- To disable HTTP/2 on a specific Ingress Controller, enter the `oc annotate` command:

  ``` terminal
  $ oc -n openshift-ingress-operator annotate ingresscontrollers/<ingresscontroller_name> ingress.operator.openshift.io/default-enable-http2=false
  ```

  - Replace `<ingresscontroller_name>` with the name of an Ingress Controller to disable HTTP/2.

- To disable HTTP/2 for the entire cluster, enter the `oc annotate` command:

  ``` terminal
  $ oc annotate ingresses.config/cluster ingress.operator.openshift.io/default-enable-http2=false
  ```

</div>

> [!TIP]
> Alternatively, you can apply the following YAML code to disable HTTP/2:
>
> ``` yaml
> apiVersion: config.openshift.io/v1
> kind: Ingress
> metadata:
>   name: cluster
>   annotations:
>     ingress.operator.openshift.io/default-enable-http2: "false"
> ```

## Configuring the PROXY protocol for an Ingress Controller

A cluster administrator can configure [the PROXY protocol](https://www.haproxy.org/download/2.8/doc/proxy-protocol.txt) when an Ingress Controller uses either the `HostNetwork`, `NodePortService`, or `Private` endpoint publishing strategy types. The PROXY protocol enables the load balancer to preserve the original client addresses for connections that the Ingress Controller receives. The original client addresses are useful for logging, filtering, and injecting HTTP headers. In the default configuration, the connections that the Ingress Controller receives only contain the source address that is associated with the load balancer.

> [!WARNING]
> The default Ingress Controller with installer-provisioned clusters on non-cloud platforms that use a Keepalived Ingress Virtual IP (VIP) do not support the PROXY protocol.

The PROXY protocol enables the load balancer to preserve the original client addresses for connections that the Ingress Controller receives. The original client addresses are useful for logging, filtering, and injecting HTTP headers. In the default configuration, the connections that the Ingress Controller receives contain only the source IP address that is associated with the load balancer.

> [!IMPORTANT]
> For a passthrough route configuration, servers in OpenShift Container Platform clusters cannot observe the original client source IP address. If you need to know the original client source IP address, configure Ingress access logging for your Ingress Controller so that you can view the client source IP addresses.
>
> For re-encrypt and edge routes, the OpenShift Container Platform router sets the `Forwarded` and `X-Forwarded-For` headers so that application workloads check the client source IP address.
>
> For more information about Ingress access logging, see "Configuring Ingress access logging".

Configuring the PROXY protocol for an Ingress Controller is not supported when using the `LoadBalancerService` endpoint publishing strategy type. This restriction is because when OpenShift Container Platform runs in a cloud platform, and an Ingress Controller specifies that a service load balancer should be used, the Ingress Operator configures the load balancer service and enables the PROXY protocol based on the platform requirement for preserving source addresses.

> [!IMPORTANT]
> You must configure both OpenShift Container Platform and the external load balancer to use either the PROXY protocol or TCP.

This feature is not supported in cloud deployments. This restriction is because when OpenShift Container Platform runs in a cloud platform, and an Ingress Controller specifies that a service load balancer should be used, the Ingress Operator configures the load balancer service and enables the PROXY protocol based on the platform requirement for preserving source addresses.

> [!IMPORTANT]
> You must configure both OpenShift Container Platform and the external load balancer to either use the PROXY protocol or to use Transmission Control Protocol (TCP).

<div>

<div class="title">

Prerequisites

</div>

- You created an Ingress Controller.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Edit the Ingress Controller resource by entering the following command in your CLI:

    ``` terminal
    $ oc -n openshift-ingress-operator edit ingresscontroller/default
    ```

2.  Set the PROXY configuration:

    - If your Ingress Controller uses the `HostNetwork` endpoint publishing strategy type, set the `spec.endpointPublishingStrategy.hostNetwork.protocol` subfield to `PROXY`:

      <div class="formalpara">

      <div class="title">

      Sample `hostNetwork` configuration to `PROXY`

      </div>

      ``` yaml
      # ...
        spec:
          endpointPublishingStrategy:
            hostNetwork:
              protocol: PROXY
            type: HostNetwork
      # ...
      ```

      </div>

    - If your Ingress Controller uses the `NodePortService` endpoint publishing strategy type, set the `spec.endpointPublishingStrategy.nodePort.protocol` subfield to `PROXY`:

      <div class="formalpara">

      <div class="title">

      Sample `nodePort` configuration to `PROXY`

      </div>

      ``` yaml
      # ...
        spec:
          endpointPublishingStrategy:
            nodePort:
              protocol: PROXY
            type: NodePortService
      # ...
      ```

      </div>

    - If your Ingress Controller uses the `Private` endpoint publishing strategy type, set the `spec.endpointPublishingStrategy.private.protocol` subfield to `PROXY`:

      <div class="formalpara">

      <div class="title">

      Sample `private` configuration to `PROXY`

      </div>

      ``` yaml
      # ...
        spec:
          endpointPublishingStrategy:
            private:
              protocol: PROXY
          type: Private
      # ...
      ```

      </div>

</div>

<div>

<div class="title">

Additional resources

</div>

- [Configuring Ingress access logging](ingress-operator.md#nw-configure-ingress-access-logging_configuring-ingress)

</div>

## Specifying an alternative cluster domain using the appsDomain option

As a cluster administrator, you can specify an alternative to the default cluster domain for user-created routes by configuring the `appsDomain` field. The `appsDomain` field is an optional domain for OpenShift Container Platform to use instead of the default, which is specified in the `domain` field. If you specify an alternative domain, it overrides the default cluster domain for the purpose of determining the default host for a new route.

For example, you can use the DNS domain for your company as the default domain for routes and ingresses for applications running on your cluster.

<div>

<div class="title">

Prerequisites

</div>

- You deployed an OpenShift Container Platform cluster.

- You installed the `oc` command-line interface.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Configure the `appsDomain` field by specifying an alternative default domain for user-created routes.

    1.  Edit the ingress `cluster` resource:

        ``` terminal
        $ oc edit ingresses.config/cluster -o yaml
        ```

    2.  Edit the YAML file:

        <div class="formalpara">

        <div class="title">

        Sample `appsDomain` configuration to `test.example.com`

        </div>

        ``` yaml
        apiVersion: config.openshift.io/v1
        kind: Ingress
        metadata:
          name: cluster
        spec:
          domain: apps.example.com
          appsDomain: <test.example.com>
        ```

        </div>

        - Specifies the default domain. You cannot modify the default domain after installation.

        - Optional: Domain for OpenShift Container Platform infrastructure to use for application routes. Instead of the default prefix, `apps`, you can use an alternative prefix like `test`.

2.  Verify that an existing route contains the domain name specified in the `appsDomain` field by exposing the route and verifying the route domain change:

    > [!NOTE]
    > Wait for the `openshift-apiserver` finish rolling updates before exposing the route.

    1.  Expose the route by entering the following command. The command outputs `route.route.openshift.io/hello-openshift exposed` to designate exposure of the route.

        ``` terminal
        $ oc expose service hello-openshift
        ```

    2.  Get a list of routes by running the following command:

        ``` terminal
        $ oc get routes
        ```

        <div class="formalpara">

        <div class="title">

        Example output

        </div>

        ``` text
        NAME              HOST/PORT                                   PATH   SERVICES          PORT       TERMINATION   WILDCARD
        hello-openshift   hello_openshift-<my_project>.test.example.com
        hello-openshift   8080-tcp                 None
        ```

        </div>

</div>

## Converting HTTP header case

HAProxy lowercases HTTP header names by default; for example, changing `Host: xyz.com` to `host: xyz.com`. If legacy applications are sensitive to the capitalization of HTTP header names, use the Ingress Controller `spec.httpHeaders.headerNameCaseAdjustments` API field for a solution to accommodate legacy applications until they can be fixed.

> [!IMPORTANT]
> OpenShift Container Platform includes HAProxy 2.8. If you want to update to this version of the web-based load balancer, ensure that you add the `spec.httpHeaders.headerNameCaseAdjustments` section to your cluster’s configuration file.

As a cluster administrator, you can convert the HTTP header case by entering the `oc patch` command or by setting the `HeaderNameCaseAdjustments` field in the Ingress Controller YAML file.

<div>

<div class="title">

Prerequisites

</div>

- You have installed the OpenShift CLI (`oc`).

- You have access to the cluster as a user with the `cluster-admin` role.

</div>

<div>

<div class="title">

Procedure

</div>

- Capitalize an HTTP header by using the `oc patch` command.

  1.  Change the HTTP header from `host` to `Host` by running the following command:

      ``` terminal
      $ oc -n openshift-ingress-operator patch ingresscontrollers/default --type=merge --patch='{"spec":{"httpHeaders":{"headerNameCaseAdjustments":["Host"]}}}'
      ```

  2.  Create a `Route` resource YAML file so that the annotation can be applied to the application.

      <div class="formalpara">

      <div class="title">

      Example of a route named `my-application`

      </div>

      ``` yaml
      apiVersion: route.openshift.io/v1
      kind: Route
      metadata:
        annotations:
          haproxy.router.openshift.io/h1-adjust-case: true
        name: <application_name>
        namespace: <application_name>
      # ...
      ```

      </div>

      - Set `haproxy.router.openshift.io/h1-adjust-case` so that the Ingress Controller can adjust the `host` request header as specified.

- Specify adjustments by configuring the `HeaderNameCaseAdjustments` field in the Ingress Controller YAML configuration file.

  1.  The following example Ingress Controller YAML file adjusts the `host` header to `Host` for HTTP/1 requests to appropriately annotated routes:

      <div class="formalpara">

      <div class="title">

      Example Ingress Controller YAML

      </div>

      ``` yaml
      apiVersion: operator.openshift.io/v1
      kind: IngressController
      metadata:
        name: default
        namespace: openshift-ingress-operator
      spec:
        httpHeaders:
          headerNameCaseAdjustments:
          - Host
      ```

      </div>

  2.  The following example route enables HTTP response header name case adjustments by using the `haproxy.router.openshift.io/h1-adjust-case` annotation:

      <div class="formalpara">

      <div class="title">

      Example route YAML

      </div>

      ``` yaml
      apiVersion: route.openshift.io/v1
      kind: Route
      metadata:
        annotations:
          haproxy.router.openshift.io/h1-adjust-case: true
        name: my-application
        namespace: my-application
      spec:
        to:
          kind: Service
          name: my-application
      ```

      </div>

      - Set `haproxy.router.openshift.io/h1-adjust-case` to true.

</div>

## Using router compression

You configure the HAProxy Ingress Controller to specify router compression globally for specific MIME types. You can use the `mimeTypes` variable to define the formats of MIME types to which compression is applied. The types are: application, image, message, multipart, text, video, or a custom type prefaced by "X-". To see the full notation for MIME types and subtypes, see [RFC1341](https://datatracker.ietf.org/doc/html/rfc1341#page-7).

> [!NOTE]
> Memory allocated for compression can affect the max connections. Additionally, compression of large buffers can cause latency, like heavy regex or long lists of regex.
>
> Not all MIME types benefit from compression, but HAProxy still uses resources to try to compress if instructed to. Generally, text formats, such as html, css, and js, formats benefit from compression, but formats that are already compressed, such as image, audio, and video, benefit little in exchange for the time and resources spent on compression.

<div>

<div class="title">

Procedure

</div>

1.  Configure the `httpCompression` field for the Ingress Controller.

    1.  Use the following command to edit the `IngressController` resource:

        ``` terminal
        $ oc edit -n openshift-ingress-operator ingresscontrollers/default
        ```

    2.  Under `spec`, set the `httpCompression` policy field to `mimeTypes` and specify a list of MIME types that should have compression applied:

        ``` yaml
        apiVersion: operator.openshift.io/v1
        kind: IngressController
        metadata:
          name: default
          namespace: openshift-ingress-operator
        spec:
          httpCompression:
            mimeTypes:
            - "text/html"
            - "text/css; charset=utf-8"
            - "application/json"
           ...
        ```

</div>

## Exposing router metrics

You can expose the HAProxy router metrics by default in Prometheus format on the default stats port, 1936. The external metrics collection and aggregation systems such as Prometheus can access the HAProxy router metrics. You can view the HAProxy router metrics in a browser in the HTML and comma separated values (CSV) format.

<div>

<div class="title">

Prerequisites

</div>

- You configured your firewall to access the default stats port, 1936.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Get the router pod name by running the following command:

    ``` terminal
    $ oc get pods -n openshift-ingress
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    NAME                              READY   STATUS    RESTARTS   AGE
    router-default-76bfffb66c-46qwp   1/1     Running   0          11h
    ```

    </div>

2.  Get the router’s username and password, which the router pod stores in the `/var/lib/haproxy/conf/metrics-auth/statsUsername` and `/var/lib/haproxy/conf/metrics-auth/statsPassword` files:

    1.  Get the username by running the following command:

        ``` terminal
        $ oc rsh <router_pod_name> cat metrics-auth/statsUsername
        ```

    2.  Get the password by running the following command:

        ``` terminal
        $ oc rsh <router_pod_name> cat metrics-auth/statsPassword
        ```

3.  Get the router IP and metrics certificates by running the following command:

    ``` terminal
    $ oc describe pod <router_pod>
    ```

4.  Get the raw statistics in Prometheus format by running the following command:

    ``` terminal
    $ curl -u <user>:<password> http://<router_IP>:<stats_port>/metrics
    ```

5.  Access the metrics securely by running the following command:

    ``` terminal
    $ curl -u user:password https://<router_IP>:<stats_port>/metrics -k
    ```

6.  Access the default stats port, 1936, by running the following command:

    ``` terminal
    $ curl -u <user>:<password> http://<router_IP>:<stats_port>/metrics
    ```

    <div class="example">

    <div class="title">

    Example output

    </div>

    ``` terminal
    ...
    # HELP haproxy_backend_connections_total Total number of connections.
    # TYPE haproxy_backend_connections_total gauge
    haproxy_backend_connections_total{backend="http",namespace="default",route="hello-route"} 0
    haproxy_backend_connections_total{backend="http",namespace="default",route="hello-route-alt"} 0
    haproxy_backend_connections_total{backend="http",namespace="default",route="hello-route01"} 0
    ...
    # HELP haproxy_exporter_server_threshold Number of servers tracked and the current threshold value.
    # TYPE haproxy_exporter_server_threshold gauge
    haproxy_exporter_server_threshold{type="current"} 11
    haproxy_exporter_server_threshold{type="limit"} 500
    ...
    # HELP haproxy_frontend_bytes_in_total Current total of incoming bytes.
    # TYPE haproxy_frontend_bytes_in_total gauge
    haproxy_frontend_bytes_in_total{frontend="fe_no_sni"} 0
    haproxy_frontend_bytes_in_total{frontend="fe_sni"} 0
    haproxy_frontend_bytes_in_total{frontend="public"} 119070
    ...
    # HELP haproxy_server_bytes_in_total Current total of incoming bytes.
    # TYPE haproxy_server_bytes_in_total gauge
    haproxy_server_bytes_in_total{namespace="",pod="",route="",server="fe_no_sni",service=""} 0
    haproxy_server_bytes_in_total{namespace="",pod="",route="",server="fe_sni",service=""} 0
    haproxy_server_bytes_in_total{namespace="default",pod="docker-registry-5-nk5fz",route="docker-registry",server="10.130.0.89:5000",service="docker-registry"} 0
    haproxy_server_bytes_in_total{namespace="default",pod="hello-rc-vkjqx",route="hello-route",server="10.130.0.90:8080",service="hello-svc-1"} 0
    ...
    ```

    </div>

7.  Launch the stats window by entering the following URL in a browser:

    ``` terminal
    http://<user>:<password>@<router_IP>:<stats_port>
    ```

8.  Optional: Get the stats in CSV format by entering the following URL in a browser:

    ``` terminal
    http://<user>:<password>@<router_ip>:1936/metrics;csv
    ```

</div>

## Customizing HAProxy error code response pages

As a cluster administrator, you can specify a custom error code response page for either 503, 404, or both error pages. The HAProxy router serves a 503 error page when the application pod is not running or a 404 error page when the requested URL does not exist. For example, if you customize the 503 error code response page, then the page is served when the application pod is not running, and the default 404 error code HTTP response page is served by the HAProxy router for an incorrect route or a non-existing route.

Custom error code response pages are specified in a config map then patched to the Ingress Controller. The config map keys have two available file names as follows: `error-page-503.http` and `error-page-404.http`.

Custom HTTP error code response pages must follow the [HAProxy HTTP error page configuration guidelines](https://www.haproxy.com/documentation/hapee/latest/configuration/config-sections/http-errors/). Here is an example of the default OpenShift Container Platform HAProxy router [http 503 error code response page](https://raw.githubusercontent.com/openshift/router/master/images/router/haproxy/conf/error-page-503.http). You can use the default content as a template for creating your own custom page.

By default, the HAProxy router serves only a 503 error page when the application is not running or when the route is incorrect or non-existent. This default behavior is the same as the behavior on OpenShift Container Platform 4.8 and earlier. If a config map for the customization of an HTTP error code response is not provided, and you are using a custom HTTP error code response page, the router serves a default 404 or 503 error code response page.

> [!NOTE]
> If you use the OpenShift Container Platform default 503 error code page as a template for your customizations, the headers in the file require an editor that can use CRLF line endings.

<div>

<div class="title">

Procedure

</div>

1.  Create a config map named `my-custom-error-code-pages` in the `openshift-config` namespace:

    ``` terminal
    $ oc -n openshift-config create configmap my-custom-error-code-pages \
      --from-file=error-page-503.http \
      --from-file=error-page-404.http
    ```

    > [!IMPORTANT]
    > If you do not specify the correct format for the custom error code response page, a router pod outage occurs. To resolve this outage, you must delete or correct the config map and delete the affected router pods so they can be recreated with the correct information.

2.  Patch the Ingress Controller to reference the `my-custom-error-code-pages` config map by name:

    ``` terminal
    $ oc patch -n openshift-ingress-operator ingresscontroller/default --patch '{"spec":{"httpErrorCodePages":{"name":"my-custom-error-code-pages"}}}' --type=merge
    ```

    The Ingress Operator copies the `my-custom-error-code-pages` config map from the `openshift-config` namespace to the `openshift-ingress` namespace. The Operator names the config map according to the pattern, `<your_ingresscontroller_name>-errorpages`, in the `openshift-ingress` namespace.

3.  Display the copy:

    ``` terminal
    $ oc get cm default-errorpages -n openshift-ingress
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

        NAME                       DATA   AGE
        default-errorpages         2      25s

    </div>

    - The example config map name is `default-errorpages` because the `default` Ingress Controller custom resource (CR) was patched.

4.  Confirm that the config map containing the custom error response page mounts on the router volume where the config map key is the filename that has the custom HTTP error code response:

    - For 503 custom HTTP custom error code response:

      ``` terminal
      $ oc -n openshift-ingress rsh <router_pod> cat /var/lib/haproxy/conf/error_code_pages/error-page-503.http
      ```

    - For 404 custom HTTP custom error code response:

      ``` terminal
      $ oc -n openshift-ingress rsh <router_pod> cat /var/lib/haproxy/conf/error_code_pages/error-page-404.http
      ```

</div>

<div class="formalpara">

<div class="title">

Verification

</div>

Verify your custom error code HTTP response:

</div>

1.  Create a test project and application:

    ``` terminal
    $ oc new-project test-ingress
    ```

    ``` terminal
    $ oc new-app django-psql-example
    ```

2.  For 503 custom http error code response:

    1.  Stop all the pods for the application.

    2.  Run the following curl command or visit the route hostname in the browser:

        ``` terminal
        $ curl -vk <route_hostname>
        ```

3.  For 404 custom http error code response:

    1.  Visit a non-existent route or an incorrect route.

    2.  Run the following curl command or visit the route hostname in the browser:

        ``` terminal
        $ curl -vk <route_hostname>
        ```

4.  Check if the `errorfile` attribute is properly in the `haproxy.config` file:

    ``` terminal
    $ oc -n openshift-ingress rsh <router> cat /var/lib/haproxy/conf/haproxy.config | grep errorfile
    ```

## Setting the Ingress Controller maximum connections

A cluster administrator can set the maximum number of simultaneous connections for OpenShift router deployments. You can patch an existing Ingress Controller to increase the maximum number of connections.

<div>

<div class="title">

Prerequisites

</div>

- The following assumes that you already created an Ingress Controller

</div>

<div>

<div class="title">

Procedure

</div>

- Update the Ingress Controller to change the maximum number of connections for HAProxy:

  ``` terminal
  $ oc -n openshift-ingress-operator patch ingresscontroller/default --type=merge -p '{"spec":{"tuningOptions": {"maxConnections": 7500}}}'
  ```

  > [!WARNING]
  > If you set the `spec.tuningOptions.maxConnections` value greater than the current operating system limit, the HAProxy process will not start. See the table in the "Ingress Controller configuration parameters" section for more information about this parameter.

</div>

# Additional resources

- [Configuring a custom PKI](../configuring_network_settings/configuring-a-custom-pki.md#configuring-a-custom-pki)
