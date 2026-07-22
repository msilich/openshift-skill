<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Description
IngressController describes a managed ingress controller for the cluster. The controller can service OpenShift Route and Kubernetes Ingress resources.

When an IngressController is created, a new ingress controller deployment is created to allow external traffic to reach the services that expose Ingress or Route resources. Updating this resource may lead to disruption for public facing network connections as a new ingress controller revision may be rolled out.

<https://kubernetes.io/docs/concepts/services-networking/ingress-controllers>

Whenever possible, sensible defaults for the platform are used. See each field for more details.

Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).

Type
`object`

# Specification

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ObjectMeta`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) | Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |
| `spec` | `object` | spec is the specification of the desired behavior of the IngressController. |
| `status` | `object` | status is the most recently observed status of the IngressController. |

## .spec

Description
spec is the specification of the desired behavior of the IngressController.

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
<td style="text-align: left;"><p><code>clientTLS</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>clientTLS specifies settings for requesting and verifying client certificates, which can be used to enable mutual TLS for edge-terminated and reencrypt routes.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>defaultCertificate</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>defaultCertificate is a reference to a secret containing the default certificate served by the ingress controller. When Routes don’t specify their own certificate, defaultCertificate is used.</p>
<p>The secret must contain the following keys and data:</p>
<p>tls.crt: certificate file contents tls.key: key file contents</p>
<p>If unset, a wildcard certificate is automatically generated and used. The certificate is valid for the ingress controller domain (and subdomains) and the generated certificate’s CA will be automatically integrated with the cluster’s trust store.</p>
<p>If a wildcard certificate is used and shared by multiple HTTP/2 enabled routes (which implies ALPN) then clients (i.e., notably browsers) are at liberty to reuse open connections. This means a client can reuse a connection to another route and that is likely to fail. This behaviour is generally known as connection coalescing.</p>
<p>The in-use certificate (whether generated or user-specified) will be automatically integrated with OpenShift’s built-in OAuth server.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>domain</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>domain is a DNS name serviced by the ingress controller and is used to configure multiple features:</p>
<p>* For the LoadBalancerService endpoint publishing strategy, domain is used to configure DNS records. See endpointPublishingStrategy.</p>
<p>* When using a generated default certificate, the certificate will be valid for domain and its subdomains. See defaultCertificate.</p>
<p>* The value is published to individual Route statuses so that end-users know where to target external DNS records.</p>
<p>domain must be unique among all IngressControllers, and cannot be updated.</p>
<p>If empty, defaults to ingress.config.openshift.io/cluster .spec.domain.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>endpointPublishingStrategy</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>endpointPublishingStrategy is used to publish the ingress controller endpoints to other networks, enable load balancer integrations, etc.</p>
<p>If unset, the default is based on infrastructure.config.openshift.io/cluster .status.platform:</p>
<p>AWS: LoadBalancerService (with External scope) Azure: LoadBalancerService (with External scope) GCP: LoadBalancerService (with External scope) IBMCloud: LoadBalancerService (with External scope) AlibabaCloud: LoadBalancerService (with External scope) Libvirt: HostNetwork</p>
<p>Any other platform types (including None) default to HostNetwork.</p>
<p>endpointPublishingStrategy cannot be updated.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>httpCompression</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>httpCompression defines a policy for HTTP traffic compression. By default, there is no HTTP compression.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>httpEmptyRequestsPolicy</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>httpEmptyRequestsPolicy describes how HTTP connections should be handled if the connection times out before a request is received. Allowed values for this field are "Respond" and "Ignore". If the field is set to "Respond", the ingress controller sends an HTTP 400 or 408 response, logs the connection (if access logging is enabled), and counts the connection in the appropriate metrics. If the field is set to "Ignore", the ingress controller closes the connection without sending a response, logging the connection, or incrementing metrics. The default value is "Respond".</p>
<p>Typically, these connections come from load balancers' health probes or Web browsers' speculative connections ("preconnect") and can be safely ignored. However, these requests may also be caused by network errors, and so setting this field to "Ignore" may impede detection and diagnosis of problems. In addition, these requests may be caused by port scans, in which case logging empty requests may aid in detecting intrusion attempts.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>httpErrorCodePages</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>httpErrorCodePages specifies a configmap with custom error pages. The administrator must create this configmap in the openshift-config namespace. This configmap should have keys in the format "error-page-&lt;error code&gt;.http", where &lt;error code&gt; is an HTTP error code. For example, "error-page-503.http" defines an error page for HTTP 503 responses. Currently only error pages for 503 and 404 responses can be customized. Each value in the configmap should be the full response, including HTTP headers. Eg- <a href="https://raw.githubusercontent.com/openshift/router/fadab45747a9b30cc3f0a4b41ad2871f95827a93/images/router/haproxy/conf/error-page-503.http">https://raw.githubusercontent.com/openshift/router/fadab45747a9b30cc3f0a4b41ad2871f95827a93/images/router/haproxy/conf/error-page-503.http</a> If this field is empty, the ingress controller uses the default error pages.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>httpHeaders</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>httpHeaders defines policy for HTTP headers.</p>
<p>If this field is empty, the default values are used.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>idleConnectionTerminationPolicy</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>idleConnectionTerminationPolicy maps directly to HAProxy’s idle-close-on-response option and controls whether HAProxy keeps idle frontend connections open during a soft stop (router reload).</p>
<p>Allowed values for this field are "Immediate" and "Deferred". The default value is "Immediate".</p>
<p>When set to "Immediate", idle connections are closed immediately during router reloads. This ensures immediate propagation of route changes but may impact clients sensitive to connection resets.</p>
<p>When set to "Deferred", HAProxy will maintain idle connections during a soft reload instead of closing them immediately. These connections remain open until any of the following occurs:</p>
<p>- A new request is received on the connection, in which case HAProxy handles it in the old process and closes the connection after sending the response.</p>
<p>- HAProxy’s <code>timeout http-keep-alive</code> duration expires (300 seconds in OpenShift’s configuration, not configurable).</p>
<p>- The client’s keep-alive timeout expires, causing the client to close the connection.</p>
<p>Setting Deferred can help prevent errors in clients or load balancers that do not properly handle connection resets. Additionally, this option allows you to retain the pre-2.4 HAProxy behaviour: in HAProxy version 2.2 (OpenShift versions &lt; 4.14), maintaining idle connections during a soft reload was the default behaviour, but starting with HAProxy 2.4, the default changed to closing idle connections immediately.</p>
<p>Important Consideration:</p>
<p>- Using Deferred will result in temporary inconsistencies for the first request on each persistent connection after a route update and router reload. This request will be processed by the old HAProxy process using its old configuration. Subsequent requests will use the updated configuration.</p>
<p>Operational Considerations:</p>
<p>- Keeping idle connections open during reloads may lead to an accumulation of old HAProxy processes if connections remain idle for extended periods, especially in environments where frequent reloads occur.</p>
<p>- Consider monitoring the number of HAProxy processes in the router pods when Deferred is set.</p>
<p>- You may need to enable or adjust the <code>ingress.operator.openshift.io/hard-stop-after</code> duration (configured via an annotation on the IngressController resource) in environments with frequent reloads to prevent resource exhaustion.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>logging</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>logging defines parameters for what should be logged where. If this field is empty, operational logs are enabled but access logs are disabled.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>namespaceSelector</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>namespaceSelector is used to filter the set of namespaces serviced by the ingress controller. This is useful for implementing shards.</p>
<p>If unset, the default is no filtering.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>nodePlacement</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>nodePlacement enables explicit control over the scheduling of the ingress controller.</p>
<p>If unset, defaults are used. See NodePlacement for more details.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>replicas</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p>replicas is the desired number of ingress controller replicas. If unset, the default depends on the value of the defaultPlacement field in the cluster config.openshift.io/v1/ingresses status.</p>
<p>The value of replicas is set based on the value of a chosen field in the Infrastructure CR. If defaultPlacement is set to ControlPlane, the chosen field will be controlPlaneTopology. If it is set to Workers the chosen field will be infrastructureTopology. Replicas will then be set to 1 or 2 based whether the chosen field’s value is SingleReplica or HighlyAvailable, respectively.</p>
<p>These defaults are subject to change.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>routeAdmission</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>routeAdmission defines a policy for handling new route claims (for example, to allow or deny claims across namespaces).</p>
<p>If empty, defaults will be applied. See specific routeAdmission fields for details about their defaults.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>routeSelector</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>routeSelector is used to filter the set of Routes serviced by the ingress controller. This is useful for implementing shards.</p>
<p>If unset, the default is no filtering.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>tlsSecurityProfile</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>tlsSecurityProfile specifies settings for TLS connections for ingresscontrollers.</p>
<p>If unset, the default is based on the apiservers.config.openshift.io/cluster resource.</p>
<p>Note that when using the Old, Intermediate, and Modern profile types, the effective profile configuration is subject to change between releases. For example, given a specification to use the Intermediate profile deployed on release X.Y.Z, an upgrade to release X.Y.Z+1 may cause a new profile configuration to be applied to the ingress controller, resulting in a rollout.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>tuningOptions</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>tuningOptions defines parameters for adjusting the performance of ingress controller pods. All fields are optional and will use their respective defaults if not set. See specific tuningOptions fields for more details.</p>
<p>Setting fields within tuningOptions is generally not recommended. The default values are suitable for most configurations.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>unsupportedConfigOverrides</code></p></td>
<td style="text-align: left;"><p>``</p></td>
<td style="text-align: left;"><p>unsupportedConfigOverrides allows specifying unsupported configuration options. Its use is unsupported.</p></td>
</tr>
</tbody>
</table>

## .spec.clientTLS

Description
clientTLS specifies settings for requesting and verifying client certificates, which can be used to enable mutual TLS for edge-terminated and reencrypt routes.

Type
`object`

Required
- `clientCA`

- `clientCertificatePolicy`

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
<td style="text-align: left;"><p><code>allowedSubjectPatterns</code></p></td>
<td style="text-align: left;"><p><code>array (string)</code></p></td>
<td style="text-align: left;"><p>allowedSubjectPatterns specifies a list of regular expressions that should be matched against the distinguished name on a valid client certificate to filter requests. The regular expressions must use PCRE syntax. If this list is empty, no filtering is performed. If the list is nonempty, then at least one pattern must match a client certificate’s distinguished name or else the ingress controller rejects the certificate and denies the connection.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>clientCA</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>clientCA specifies a configmap containing the PEM-encoded CA certificate bundle that should be used to verify a client’s certificate. The administrator must create this configmap in the openshift-config namespace.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>clientCertificatePolicy</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>clientCertificatePolicy specifies whether the ingress controller requires clients to provide certificates. This field accepts the values "Required" or "Optional".</p>
<p>Note that the ingress controller only checks client certificates for edge-terminated and reencrypt TLS routes; it cannot check certificates for cleartext HTTP or passthrough TLS routes.</p></td>
</tr>
</tbody>
</table>

## .spec.clientTLS.clientCA

Description
clientCA specifies a configmap containing the PEM-encoded CA certificate bundle that should be used to verify a client’s certificate. The administrator must create this configmap in the openshift-config namespace.

Type
`object`

Required
- `name`

| Property | Type     | Description                                            |
|----------|----------|--------------------------------------------------------|
| `name`   | `string` | name is the metadata.name of the referenced config map |

## .spec.defaultCertificate

Description
defaultCertificate is a reference to a secret containing the default certificate served by the ingress controller. When Routes don’t specify their own certificate, defaultCertificate is used.

The secret must contain the following keys and data:

    tls.crt: certificate file contents
    tls.key: key file contents

If unset, a wildcard certificate is automatically generated and used. The certificate is valid for the ingress controller domain (and subdomains) and the generated certificate’s CA will be automatically integrated with the cluster’s trust store.

If a wildcard certificate is used and shared by multiple HTTP/2 enabled routes (which implies ALPN) then clients (i.e., notably browsers) are at liberty to reuse open connections. This means a client can reuse a connection to another route and that is likely to fail. This behaviour is generally known as connection coalescing.

The in-use certificate (whether generated or user-specified) will be automatically integrated with OpenShift’s built-in OAuth server.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `name` | `string` | Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names> |

## .spec.endpointPublishingStrategy

Description
endpointPublishingStrategy is used to publish the ingress controller endpoints to other networks, enable load balancer integrations, etc.

If unset, the default is based on infrastructure.config.openshift.io/cluster .status.platform:

    AWS:          LoadBalancerService (with External scope)
    Azure:        LoadBalancerService (with External scope)
    GCP:          LoadBalancerService (with External scope)
    IBMCloud:     LoadBalancerService (with External scope)
    AlibabaCloud: LoadBalancerService (with External scope)
    Libvirt:      HostNetwork

Any other platform types (including None) default to HostNetwork.

endpointPublishingStrategy cannot be updated.

Type
`object`

Required
- `type`

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
<td style="text-align: left;"><p><code>hostNetwork</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>hostNetwork holds parameters for the HostNetwork endpoint publishing strategy. Present only if type is HostNetwork.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>loadBalancer</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>loadBalancer holds parameters for the load balancer. Present only if type is LoadBalancerService.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>nodePort</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>nodePort holds parameters for the NodePortService endpoint publishing strategy. Present only if type is NodePortService.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>private</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>private holds parameters for the Private endpoint publishing strategy. Present only if type is Private.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>type</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>type is the publishing strategy to use. Valid values are:</p>
<p>* LoadBalancerService</p>
<p>Publishes the ingress controller using a Kubernetes LoadBalancer Service.</p>
<p>In this configuration, the ingress controller deployment uses container networking. A LoadBalancer Service is created to publish the deployment.</p>
<p>See: <a href="https://kubernetes.io/docs/concepts/services-networking/service/#loadbalancer">https://kubernetes.io/docs/concepts/services-networking/service/#loadbalancer</a></p>
<p>If domain is set, a wildcard DNS record will be managed to point at the LoadBalancer Service’s external name. DNS records are managed only in DNS zones defined by dns.config.openshift.io/cluster .spec.publicZone and .spec.privateZone.</p>
<p>Wildcard DNS management is currently supported only on the AWS, Azure, and GCP platforms.</p>
<p>* HostNetwork</p>
<p>Publishes the ingress controller on node ports where the ingress controller is deployed.</p>
<p>In this configuration, the ingress controller deployment uses host networking, bound to node ports 80 and 443. The user is responsible for configuring an external load balancer to publish the ingress controller via the node ports.</p>
<p>* Private</p>
<p>Does not publish the ingress controller.</p>
<p>In this configuration, the ingress controller deployment uses container networking, and is not explicitly published. The user must manually publish the ingress controller.</p>
<p>* NodePortService</p>
<p>Publishes the ingress controller using a Kubernetes NodePort Service.</p>
<p>In this configuration, the ingress controller deployment uses container networking. A NodePort Service is created to publish the deployment. The specific node ports are dynamically allocated by OpenShift; however, to support static port allocations, user changes to the node port field of the managed NodePort Service will preserved.</p></td>
</tr>
</tbody>
</table>

## .spec.endpointPublishingStrategy.hostNetwork

Description
hostNetwork holds parameters for the HostNetwork endpoint publishing strategy. Present only if type is HostNetwork.

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
<td style="text-align: left;"><p><code>httpPort</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p>httpPort is the port on the host which should be used to listen for HTTP requests. This field should be set when port 80 is already in use. The value should not coincide with the NodePort range of the cluster. When the value is 0 or is not specified it defaults to 80.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>httpsPort</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p>httpsPort is the port on the host which should be used to listen for HTTPS requests. This field should be set when port 443 is already in use. The value should not coincide with the NodePort range of the cluster. When the value is 0 or is not specified it defaults to 443.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>protocol</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>protocol specifies whether the IngressController expects incoming connections to use plain TCP or whether the IngressController expects PROXY protocol.</p>
<p>PROXY protocol can be used with load balancers that support it to communicate the source addresses of client connections when forwarding those connections to the IngressController. Using PROXY protocol enables the IngressController to report those source addresses instead of reporting the load balancer’s address in HTTP headers and logs. Note that enabling PROXY protocol on the IngressController will cause connections to fail if you are not using a load balancer that uses PROXY protocol to forward connections to the IngressController. See <a href="http://www.haproxy.org/download/2.2/doc/proxy-protocol.txt">http://www.haproxy.org/download/2.2/doc/proxy-protocol.txt</a> for information about PROXY protocol.</p>
<p>The following values are valid for this field:</p>
<p>* The empty string. * "TCP". * "PROXY".</p>
<p>The empty string specifies the default, which is TCP without PROXY protocol. Note that the default is subject to change.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>statsPort</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p>statsPort is the port on the host where the stats from the router are published. The value should not coincide with the NodePort range of the cluster. If an external load balancer is configured to forward connections to this IngressController, the load balancer should use this port for health checks. The load balancer can send HTTP probes on this port on a given node, with the path /healthz/ready to determine if the ingress controller is ready to receive traffic on the node. For proper operation the load balancer must not forward traffic to a node until the health check reports ready. The load balancer should also stop forwarding requests within a maximum of 45 seconds after /healthz/ready starts reporting not-ready. Probing every 5 to 10 seconds, with a 5-second timeout and with a threshold of two successful or failed requests to become healthy or unhealthy respectively, are well-tested values. When the value is 0 or is not specified it defaults to 1936.</p></td>
</tr>
</tbody>
</table>

## .spec.endpointPublishingStrategy.loadBalancer

Description
loadBalancer holds parameters for the load balancer. Present only if type is LoadBalancerService.

Type
`object`

Required
- `dnsManagementPolicy`

- `scope`

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
<td style="text-align: left;"><p><code>allowedSourceRanges</code></p></td>
<td style="text-align: left;"><p>``</p></td>
<td style="text-align: left;"><p>allowedSourceRanges specifies an allowlist of IP address ranges to which access to the load balancer should be restricted. Each range must be specified using CIDR notation (e.g. "10.0.0.0/8" or "fd00::/8"). If no range is specified, "0.0.0.0/0" for IPv4 and "::/0" for IPv6 are used by default, which allows all source addresses.</p>
<p>To facilitate migration from earlier versions of OpenShift that did not have the allowedSourceRanges field, you may set the service.beta.kubernetes.io/load-balancer-source-ranges annotation on the "router-&lt;ingresscontroller name&gt;" service in the "openshift-ingress" namespace, and this annotation will take effect if allowedSourceRanges is empty on OpenShift 4.12.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>dnsManagementPolicy</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>dnsManagementPolicy indicates if the lifecycle of the wildcard DNS record associated with the load balancer service will be managed by the ingress operator. It defaults to Managed. Valid values are: Managed and Unmanaged.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>providerParameters</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>providerParameters holds desired load balancer information specific to the underlying infrastructure provider.</p>
<p>If empty, defaults will be applied. See specific providerParameters fields for details about their defaults.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>scope</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>scope indicates the scope at which the load balancer is exposed. Possible values are "External" and "Internal".</p></td>
</tr>
</tbody>
</table>

## .spec.endpointPublishingStrategy.loadBalancer.providerParameters

Description
providerParameters holds desired load balancer information specific to the underlying infrastructure provider.

If empty, defaults will be applied. See specific providerParameters fields for details about their defaults.

Type
`object`

Required
- `type`

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
<td style="text-align: left;"><p><code>aws</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>aws provides configuration settings that are specific to AWS load balancers.</p>
<p>If empty, defaults will be applied. See specific aws fields for details about their defaults.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>gcp</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>gcp provides configuration settings that are specific to GCP load balancers.</p>
<p>If empty, defaults will be applied. See specific gcp fields for details about their defaults.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>ibm</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>ibm provides configuration settings that are specific to IBM Cloud load balancers.</p>
<p>If empty, defaults will be applied. See specific ibm fields for details about their defaults.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>openstack</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>openstack provides configuration settings that are specific to OpenStack load balancers.</p>
<p>If empty, defaults will be applied. See specific openstack fields for details about their defaults.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>type</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>type is the underlying infrastructure provider for the load balancer. Allowed values are "AWS", "Azure", "BareMetal", "GCP", "IBM", "Nutanix", "OpenStack", and "VSphere".</p></td>
</tr>
</tbody>
</table>

## .spec.endpointPublishingStrategy.loadBalancer.providerParameters.aws

Description
aws provides configuration settings that are specific to AWS load balancers.

If empty, defaults will be applied. See specific aws fields for details about their defaults.

Type
`object`

Required
- `type`

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
<td style="text-align: left;"><p><code>classicLoadBalancer</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>classicLoadBalancerParameters holds configuration parameters for an AWS classic load balancer. Present only if type is Classic.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>networkLoadBalancer</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>networkLoadBalancerParameters holds configuration parameters for an AWS network load balancer. Present only if type is NLB.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>type</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>type is the type of AWS load balancer to instantiate for an ingresscontroller.</p>
<p>Valid values are:</p>
<p>* "Classic": A Classic Load Balancer that makes routing decisions at either the transport layer (TCP/SSL) or the application layer (HTTP/HTTPS). See the following for additional details:</p>
<p><a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/load-balancer-types.html#clb">https://docs.aws.amazon.com/AmazonECS/latest/developerguide/load-balancer-types.html#clb</a></p>
<p>* "NLB": A Network Load Balancer that makes routing decisions at the transport layer (TCP/SSL). See the following for additional details:</p>
<p><a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/load-balancer-types.html#nlb">https://docs.aws.amazon.com/AmazonECS/latest/developerguide/load-balancer-types.html#nlb</a></p></td>
</tr>
</tbody>
</table>

## .spec.endpointPublishingStrategy.loadBalancer.providerParameters.aws.classicLoadBalancer

Description
classicLoadBalancerParameters holds configuration parameters for an AWS classic load balancer. Present only if type is Classic.

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
<td style="text-align: left;"><p><code>connectionIdleTimeout</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>connectionIdleTimeout specifies the maximum time period that a connection may be idle before the load balancer closes the connection. The value must be parseable as a time duration value; see <a href="https://pkg.go.dev/time#ParseDuration">https://pkg.go.dev/time#ParseDuration</a>. A nil or zero value means no opinion, in which case a default value is used. The default value for this field is 60s. This default is subject to change.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>subnets</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>subnets specifies the subnets to which the load balancer will attach. The subnets may be specified by either their ID or name. The total number of subnets is limited to 10.</p>
<p>In order for the load balancer to be provisioned with subnets, each subnet must exist, each subnet must be from a different availability zone, and the load balancer service must be recreated to pick up new values.</p>
<p>When omitted from the spec, the subnets will be auto-discovered for each availability zone. Auto-discovered subnets are not reported in the status of the IngressController object.</p></td>
</tr>
</tbody>
</table>

## .spec.endpointPublishingStrategy.loadBalancer.providerParameters.aws.classicLoadBalancer.subnets

Description
subnets specifies the subnets to which the load balancer will attach. The subnets may be specified by either their ID or name. The total number of subnets is limited to 10.

In order for the load balancer to be provisioned with subnets, each subnet must exist, each subnet must be from a different availability zone, and the load balancer service must be recreated to pick up new values.

When omitted from the spec, the subnets will be auto-discovered for each availability zone. Auto-discovered subnets are not reported in the status of the IngressController object.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `ids` | `array (string)` | ids specifies a list of AWS subnets by subnet ID. Subnet IDs must start with "subnet-", consist only of alphanumeric characters, must be exactly 24 characters long, must be unique, and the total number of subnets specified by ids and names must not exceed 10. |
| `names` | `array (string)` | names specifies a list of AWS subnets by subnet name. Subnet names must not start with "subnet-", must not include commas, must be under 256 characters in length, must be unique, and the total number of subnets specified by ids and names must not exceed 10. |

## .spec.endpointPublishingStrategy.loadBalancer.providerParameters.aws.networkLoadBalancer

Description
networkLoadBalancerParameters holds configuration parameters for an AWS network load balancer. Present only if type is NLB.

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
<td style="text-align: left;"><p><code>eipAllocations</code></p></td>
<td style="text-align: left;"><p><code>array (string)</code></p></td>
<td style="text-align: left;"><p>eipAllocations is a list of IDs for Elastic IP (EIP) addresses that are assigned to the Network Load Balancer. The following restrictions apply:</p>
<p>eipAllocations can only be used with external scope, not internal. An EIP can be allocated to only a single IngressController. The number of EIP allocations must match the number of subnets that are used for the load balancer. Each EIP allocation must be unique. A maximum of 10 EIP allocations are permitted.</p>
<p>See <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/elastic-ip-addresses-eip.html">https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/elastic-ip-addresses-eip.html</a> for general information about configuration, characteristics, and limitations of Elastic IP addresses.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>subnets</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>subnets specifies the subnets to which the load balancer will attach. The subnets may be specified by either their ID or name. The total number of subnets is limited to 10.</p>
<p>In order for the load balancer to be provisioned with subnets, each subnet must exist, each subnet must be from a different availability zone, and the load balancer service must be recreated to pick up new values.</p>
<p>When omitted from the spec, the subnets will be auto-discovered for each availability zone. Auto-discovered subnets are not reported in the status of the IngressController object.</p></td>
</tr>
</tbody>
</table>

## .spec.endpointPublishingStrategy.loadBalancer.providerParameters.aws.networkLoadBalancer.subnets

Description
subnets specifies the subnets to which the load balancer will attach. The subnets may be specified by either their ID or name. The total number of subnets is limited to 10.

In order for the load balancer to be provisioned with subnets, each subnet must exist, each subnet must be from a different availability zone, and the load balancer service must be recreated to pick up new values.

When omitted from the spec, the subnets will be auto-discovered for each availability zone. Auto-discovered subnets are not reported in the status of the IngressController object.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `ids` | `array (string)` | ids specifies a list of AWS subnets by subnet ID. Subnet IDs must start with "subnet-", consist only of alphanumeric characters, must be exactly 24 characters long, must be unique, and the total number of subnets specified by ids and names must not exceed 10. |
| `names` | `array (string)` | names specifies a list of AWS subnets by subnet name. Subnet names must not start with "subnet-", must not include commas, must be under 256 characters in length, must be unique, and the total number of subnets specified by ids and names must not exceed 10. |

## .spec.endpointPublishingStrategy.loadBalancer.providerParameters.gcp

Description
gcp provides configuration settings that are specific to GCP load balancers.

If empty, defaults will be applied. See specific gcp fields for details about their defaults.

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
<td style="text-align: left;"><p><code>clientAccess</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>clientAccess describes how client access is restricted for internal load balancers.</p>
<p>Valid values are: * "Global": Specifying an internal load balancer with Global client access allows clients from any region within the VPC to communicate with the load balancer.</p>
<p><a href="https://cloud.google.com/kubernetes-engine/docs/how-to/internal-load-balancing#global_access">https://cloud.google.com/kubernetes-engine/docs/how-to/internal-load-balancing#global_access</a></p>
<p>* "Local": Specifying an internal load balancer with Local client access means only clients within the same region (and VPC) as the GCP load balancer can communicate with the load balancer. Note that this is the default behavior.</p>
<p><a href="https://cloud.google.com/load-balancing/docs/internal#client_access">https://cloud.google.com/load-balancing/docs/internal#client_access</a></p></td>
</tr>
</tbody>
</table>

## .spec.endpointPublishingStrategy.loadBalancer.providerParameters.ibm

Description
ibm provides configuration settings that are specific to IBM Cloud load balancers.

If empty, defaults will be applied. See specific ibm fields for details about their defaults.

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
<td style="text-align: left;"><p><code>protocol</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>protocol specifies whether the load balancer uses PROXY protocol to forward connections to the IngressController. See "service.kubernetes.io/ibm-load-balancer-cloud-provider-enable-features: "proxy-protocol"" at <a href="https://cloud.ibm.com/docs/containers?topic=containers-vpc-lbaas">https://cloud.ibm.com/docs/containers?topic=containers-vpc-lbaas</a></p>
<p>PROXY protocol can be used with load balancers that support it to communicate the source addresses of client connections when forwarding those connections to the IngressController. Using PROXY protocol enables the IngressController to report those source addresses instead of reporting the load balancer’s address in HTTP headers and logs. Note that enabling PROXY protocol on the IngressController will cause connections to fail if you are not using a load balancer that uses PROXY protocol to forward connections to the IngressController. See <a href="http://www.haproxy.org/download/2.2/doc/proxy-protocol.txt">http://www.haproxy.org/download/2.2/doc/proxy-protocol.txt</a> for information about PROXY protocol.</p>
<p>Valid values for protocol are TCP, PROXY and omitted. When omitted, this means no opinion and the platform is left to choose a reasonable default, which is subject to change over time. The current default is TCP, without the proxy protocol enabled.</p></td>
</tr>
</tbody>
</table>

## .spec.endpointPublishingStrategy.loadBalancer.providerParameters.openstack

Description
openstack provides configuration settings that are specific to OpenStack load balancers.

If empty, defaults will be applied. See specific openstack fields for details about their defaults.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `floatingIP` | `string` | floatingIP specifies the IP address that the load balancer will use. When not specified, an IP address will be assigned randomly by the OpenStack cloud provider. When specified, the floating IP has to be pre-created. If the specified value is not a floating IP or is already claimed, the OpenStack cloud provider won’t be able to provision the load balancer. This field may only be used if the IngressController has External scope. This value must be a valid IPv4 or IPv6 address. |

## .spec.endpointPublishingStrategy.nodePort

Description
nodePort holds parameters for the NodePortService endpoint publishing strategy. Present only if type is NodePortService.

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
<td style="text-align: left;"><p><code>protocol</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>protocol specifies whether the IngressController expects incoming connections to use plain TCP or whether the IngressController expects PROXY protocol.</p>
<p>PROXY protocol can be used with load balancers that support it to communicate the source addresses of client connections when forwarding those connections to the IngressController. Using PROXY protocol enables the IngressController to report those source addresses instead of reporting the load balancer’s address in HTTP headers and logs. Note that enabling PROXY protocol on the IngressController will cause connections to fail if you are not using a load balancer that uses PROXY protocol to forward connections to the IngressController. See <a href="http://www.haproxy.org/download/2.2/doc/proxy-protocol.txt">http://www.haproxy.org/download/2.2/doc/proxy-protocol.txt</a> for information about PROXY protocol.</p>
<p>The following values are valid for this field:</p>
<p>* The empty string. * "TCP". * "PROXY".</p>
<p>The empty string specifies the default, which is TCP without PROXY protocol. Note that the default is subject to change.</p></td>
</tr>
</tbody>
</table>

## .spec.endpointPublishingStrategy.private

Description
private holds parameters for the Private endpoint publishing strategy. Present only if type is Private.

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
<td style="text-align: left;"><p><code>protocol</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>protocol specifies whether the IngressController expects incoming connections to use plain TCP or whether the IngressController expects PROXY protocol.</p>
<p>PROXY protocol can be used with load balancers that support it to communicate the source addresses of client connections when forwarding those connections to the IngressController. Using PROXY protocol enables the IngressController to report those source addresses instead of reporting the load balancer’s address in HTTP headers and logs. Note that enabling PROXY protocol on the IngressController will cause connections to fail if you are not using a load balancer that uses PROXY protocol to forward connections to the IngressController. See <a href="http://www.haproxy.org/download/2.2/doc/proxy-protocol.txt">http://www.haproxy.org/download/2.2/doc/proxy-protocol.txt</a> for information about PROXY protocol.</p>
<p>The following values are valid for this field:</p>
<p>* The empty string. * "TCP". * "PROXY".</p>
<p>The empty string specifies the default, which is TCP without PROXY protocol. Note that the default is subject to change.</p></td>
</tr>
</tbody>
</table>

## .spec.httpCompression

Description
httpCompression defines a policy for HTTP traffic compression. By default, there is no HTTP compression.

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
<td style="text-align: left;"><p><code>mimeTypes</code></p></td>
<td style="text-align: left;"><p><code>array (string)</code></p></td>
<td style="text-align: left;"><p>mimeTypes is a list of MIME types that should have compression applied. This list can be empty, in which case the ingress controller does not apply compression.</p>
<p>Note: Not all MIME types benefit from compression, but HAProxy will still use resources to try to compress if instructed to. Generally speaking, text (html, css, js, etc.) formats benefit from compression, but formats that are already compressed (image, audio, video, etc.) benefit little in exchange for the time and cpu spent on compressing again. See <a href="https://joehonton.medium.com/the-gzip-penalty-d31bd697f1a2">https://joehonton.medium.com/the-gzip-penalty-d31bd697f1a2</a></p></td>
</tr>
</tbody>
</table>

## .spec.httpErrorCodePages

Description
httpErrorCodePages specifies a configmap with custom error pages. The administrator must create this configmap in the openshift-config namespace. This configmap should have keys in the format "error-page-\<error code\>.http", where \<error code\> is an HTTP error code. For example, "error-page-503.http" defines an error page for HTTP 503 responses. Currently only error pages for 503 and 404 responses can be customized. Each value in the configmap should be the full response, including HTTP headers. Eg- <https://raw.githubusercontent.com/openshift/router/fadab45747a9b30cc3f0a4b41ad2871f95827a93/images/router/haproxy/conf/error-page-503.http> If this field is empty, the ingress controller uses the default error pages.

Type
`object`

Required
- `name`

| Property | Type     | Description                                            |
|----------|----------|--------------------------------------------------------|
| `name`   | `string` | name is the metadata.name of the referenced config map |

## .spec.httpHeaders

Description
httpHeaders defines policy for HTTP headers.

If this field is empty, the default values are used.

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
<td style="text-align: left;"><p><code>actions</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>actions specifies options for modifying headers and their values. Note that this option only applies to cleartext HTTP connections and to secure HTTP connections for which the ingress controller terminates encryption (that is, edge-terminated or reencrypt connections). Headers cannot be modified for TLS passthrough connections. Setting the HSTS (<code>Strict-Transport-Security</code>) header is not supported via actions. <code>Strict-Transport-Security</code> may only be configured using the "haproxy.router.openshift.io/hsts_header" route annotation, and only in accordance with the policy specified in Ingress.Spec.RequiredHSTSPolicies. Any actions defined here are applied after any actions related to the following other fields: cache-control, spec.clientTLS, spec.httpHeaders.forwardedHeaderPolicy, spec.httpHeaders.uniqueId, and spec.httpHeaders.headerNameCaseAdjustments. In case of HTTP request headers, the actions specified in spec.httpHeaders.actions on the Route will be executed after the actions specified in the IngressController’s spec.httpHeaders.actions field. In case of HTTP response headers, the actions specified in spec.httpHeaders.actions on the IngressController will be executed after the actions specified in the Route’s spec.httpHeaders.actions field. Headers set using this API cannot be captured for use in access logs. The following header names are reserved and may not be modified via this API: Strict-Transport-Security, Proxy, Host, Cookie, Set-Cookie. Note that the total size of all net added headers <strong>after</strong> interpolating dynamic values must not exceed the value of spec.tuningOptions.headerBufferMaxRewriteBytes on the IngressController. Please refer to the documentation for that API field for more details.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>forwardedHeaderPolicy</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>forwardedHeaderPolicy specifies when and how the IngressController sets the Forwarded, X-Forwarded-For, X-Forwarded-Host, X-Forwarded-Port, X-Forwarded-Proto, and X-Forwarded-Proto-Version HTTP headers. The value may be one of the following:</p>
<p>* "Append", which specifies that the IngressController appends the headers, preserving existing headers.</p>
<p>* "Replace", which specifies that the IngressController sets the headers, replacing any existing Forwarded or X-Forwarded-* headers.</p>
<p>* "IfNone", which specifies that the IngressController sets the headers if they are not already set.</p>
<p>* "Never", which specifies that the IngressController never sets the headers, preserving any existing headers.</p>
<p>By default, the policy is "Append".</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>headerNameCaseAdjustments</code></p></td>
<td style="text-align: left;"><p>``</p></td>
<td style="text-align: left;"><p>headerNameCaseAdjustments specifies case adjustments that can be applied to HTTP header names. Each adjustment is specified as an HTTP header name with the desired capitalization. For example, specifying "X-Forwarded-For" indicates that the "x-forwarded-for" HTTP header should be adjusted to have the specified capitalization.</p>
<p>These adjustments are only applied to cleartext, edge-terminated, and re-encrypt routes, and only when using HTTP/1.</p>
<p>For request headers, these adjustments are applied only for routes that have the haproxy.router.openshift.io/h1-adjust-case=true annotation. For response headers, these adjustments are applied to all HTTP responses.</p>
<p>If this field is empty, no request headers are adjusted.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>uniqueId</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>uniqueId describes configuration for a custom HTTP header that the ingress controller should inject into incoming HTTP requests. Typically, this header is configured to have a value that is unique to the HTTP request. The header can be used by applications or included in access logs to facilitate tracing individual HTTP requests.</p>
<p>If this field is empty, no such header is injected into requests.</p></td>
</tr>
</tbody>
</table>

## .spec.httpHeaders.actions

Description
actions specifies options for modifying headers and their values. Note that this option only applies to cleartext HTTP connections and to secure HTTP connections for which the ingress controller terminates encryption (that is, edge-terminated or reencrypt connections). Headers cannot be modified for TLS passthrough connections. Setting the HSTS (`Strict-Transport-Security`) header is not supported via actions. `Strict-Transport-Security` may only be configured using the "haproxy.router.openshift.io/hsts_header" route annotation, and only in accordance with the policy specified in Ingress.Spec.RequiredHSTSPolicies. Any actions defined here are applied after any actions related to the following other fields: cache-control, spec.clientTLS, spec.httpHeaders.forwardedHeaderPolicy, spec.httpHeaders.uniqueId, and spec.httpHeaders.headerNameCaseAdjustments. In case of HTTP request headers, the actions specified in spec.httpHeaders.actions on the Route will be executed after the actions specified in the IngressController’s spec.httpHeaders.actions field. In case of HTTP response headers, the actions specified in spec.httpHeaders.actions on the IngressController will be executed after the actions specified in the Route’s spec.httpHeaders.actions field. Headers set using this API cannot be captured for use in access logs. The following header names are reserved and may not be modified via this API: Strict-Transport-Security, Proxy, Host, Cookie, Set-Cookie. Note that the total size of all net added headers **after** interpolating dynamic values must not exceed the value of spec.tuningOptions.headerBufferMaxRewriteBytes on the IngressController. Please refer to the documentation for that API field for more details.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `request` | `array` | request is a list of HTTP request headers to modify. Actions defined here will modify the request headers of all requests passing through an ingress controller. These actions are applied to all Routes i.e. for all connections handled by the ingress controller defined within a cluster. IngressController actions for request headers will be executed before Route actions. Currently, actions may define to either `Set` or `Delete` headers values. Actions are applied in sequence as defined in this list. A maximum of 20 request header actions may be configured. Sample fetchers allowed are "req.hdr" and "ssl_c_der". Converters allowed are "lower" and "base64". Example header values: "%\[req.hdr(X-target),lower\]", "%{+Q}\[ssl_c_der,base64\]". |
| `request[]` | `object` | IngressControllerHTTPHeader specifies configuration for setting or deleting an HTTP header. |
| `response` | `array` | response is a list of HTTP response headers to modify. Actions defined here will modify the response headers of all requests passing through an ingress controller. These actions are applied to all Routes i.e. for all connections handled by the ingress controller defined within a cluster. IngressController actions for response headers will be executed after Route actions. Currently, actions may define to either `Set` or `Delete` headers values. Actions are applied in sequence as defined in this list. A maximum of 20 response header actions may be configured. Sample fetchers allowed are "res.hdr" and "ssl_c_der". Converters allowed are "lower" and "base64". Example header values: "%\[res.hdr(X-target),lower\]", "%{+Q}\[ssl_c_der,base64\]". |
| `response[]` | `object` | IngressControllerHTTPHeader specifies configuration for setting or deleting an HTTP header. |

## .spec.httpHeaders.actions.request

Description
request is a list of HTTP request headers to modify. Actions defined here will modify the request headers of all requests passing through an ingress controller. These actions are applied to all Routes i.e. for all connections handled by the ingress controller defined within a cluster. IngressController actions for request headers will be executed before Route actions. Currently, actions may define to either `Set` or `Delete` headers values. Actions are applied in sequence as defined in this list. A maximum of 20 request header actions may be configured. Sample fetchers allowed are "req.hdr" and "ssl_c_der". Converters allowed are "lower" and "base64". Example header values: "%\[req.hdr(X-target),lower\]", "%{+Q}\[ssl_c_der,base64\]".

Type
`array`

## .spec.httpHeaders.actions.request\[\]

Description
IngressControllerHTTPHeader specifies configuration for setting or deleting an HTTP header.

Type
`object`

Required
- `action`

- `name`

| Property | Type | Description |
|----|----|----|
| `action` | `object` | action specifies actions to perform on headers, such as setting or deleting headers. |
| `name` | `string` | name specifies the name of a header on which to perform an action. Its value must be a valid HTTP header name as defined in RFC 2616 section 4.2. The name must consist only of alphanumeric and the following special characters, "-!#\$%&'\*+.^\_\`". The following header names are reserved and may not be modified via this API: Strict-Transport-Security, Proxy, Host, Cookie, Set-Cookie. It must be no more than 255 characters in length. Header name must be unique. |

## .spec.httpHeaders.actions.request\[\].action

Description
action specifies actions to perform on headers, such as setting or deleting headers.

Type
`object`

Required
- `type`

| Property | Type | Description |
|----|----|----|
| `set` | `object` | set specifies how the HTTP header should be set. This field is required when type is Set and forbidden otherwise. |
| `type` | `string` | type defines the type of the action to be applied on the header. Possible values are Set or Delete. Set allows you to set HTTP request and response headers. Delete allows you to delete HTTP request and response headers. |

## .spec.httpHeaders.actions.request\[\].action.set

Description
set specifies how the HTTP header should be set. This field is required when type is Set and forbidden otherwise.

Type
`object`

Required
- `value`

| Property | Type | Description |
|----|----|----|
| `value` | `string` | value specifies a header value. Dynamic values can be added. The value will be interpreted as an HAProxy format string as defined in <http://cbonte.github.io/haproxy-dconv/2.6/configuration.html#8.2.6> and may use HAProxy’s %\[\] syntax and otherwise must be a valid HTTP header value as defined in <https://datatracker.ietf.org/doc/html/rfc7230#section-3.2>. The value of this field must be no more than 16384 characters in length. Note that the total size of all net added headers **after** interpolating dynamic values must not exceed the value of spec.tuningOptions.headerBufferMaxRewriteBytes on the IngressController. |

## .spec.httpHeaders.actions.response

Description
response is a list of HTTP response headers to modify. Actions defined here will modify the response headers of all requests passing through an ingress controller. These actions are applied to all Routes i.e. for all connections handled by the ingress controller defined within a cluster. IngressController actions for response headers will be executed after Route actions. Currently, actions may define to either `Set` or `Delete` headers values. Actions are applied in sequence as defined in this list. A maximum of 20 response header actions may be configured. Sample fetchers allowed are "res.hdr" and "ssl_c_der". Converters allowed are "lower" and "base64". Example header values: "%\[res.hdr(X-target),lower\]", "%{+Q}\[ssl_c_der,base64\]".

Type
`array`

## .spec.httpHeaders.actions.response\[\]

Description
IngressControllerHTTPHeader specifies configuration for setting or deleting an HTTP header.

Type
`object`

Required
- `action`

- `name`

| Property | Type | Description |
|----|----|----|
| `action` | `object` | action specifies actions to perform on headers, such as setting or deleting headers. |
| `name` | `string` | name specifies the name of a header on which to perform an action. Its value must be a valid HTTP header name as defined in RFC 2616 section 4.2. The name must consist only of alphanumeric and the following special characters, "-!#\$%&'\*+.^\_\`". The following header names are reserved and may not be modified via this API: Strict-Transport-Security, Proxy, Host, Cookie, Set-Cookie. It must be no more than 255 characters in length. Header name must be unique. |

## .spec.httpHeaders.actions.response\[\].action

Description
action specifies actions to perform on headers, such as setting or deleting headers.

Type
`object`

Required
- `type`

| Property | Type | Description |
|----|----|----|
| `set` | `object` | set specifies how the HTTP header should be set. This field is required when type is Set and forbidden otherwise. |
| `type` | `string` | type defines the type of the action to be applied on the header. Possible values are Set or Delete. Set allows you to set HTTP request and response headers. Delete allows you to delete HTTP request and response headers. |

## .spec.httpHeaders.actions.response\[\].action.set

Description
set specifies how the HTTP header should be set. This field is required when type is Set and forbidden otherwise.

Type
`object`

Required
- `value`

| Property | Type | Description |
|----|----|----|
| `value` | `string` | value specifies a header value. Dynamic values can be added. The value will be interpreted as an HAProxy format string as defined in <http://cbonte.github.io/haproxy-dconv/2.6/configuration.html#8.2.6> and may use HAProxy’s %\[\] syntax and otherwise must be a valid HTTP header value as defined in <https://datatracker.ietf.org/doc/html/rfc7230#section-3.2>. The value of this field must be no more than 16384 characters in length. Note that the total size of all net added headers **after** interpolating dynamic values must not exceed the value of spec.tuningOptions.headerBufferMaxRewriteBytes on the IngressController. |

## .spec.httpHeaders.uniqueId

Description
uniqueId describes configuration for a custom HTTP header that the ingress controller should inject into incoming HTTP requests. Typically, this header is configured to have a value that is unique to the HTTP request. The header can be used by applications or included in access logs to facilitate tracing individual HTTP requests.

If this field is empty, no such header is injected into requests.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `format` | `string` | format specifies the format for the injected HTTP header’s value. This field has no effect unless name is specified. For the HAProxy-based ingress controller implementation, this format uses the same syntax as the HTTP log format. If the field is empty, the default value is "%{+X}o\\ %ci:%cp\_%fi:%fp\_%Ts\_%rt:%pid"; see the corresponding HAProxy documentation: <http://cbonte.github.io/haproxy-dconv/2.0/configuration.html#8.2.3> |
| `name` | `string` | name specifies the name of the HTTP header (for example, "unique-id") that the ingress controller should inject into HTTP requests. The field’s value must be a valid HTTP header name as defined in RFC 2616 section 4.2. If the field is empty, no header is injected. |

## .spec.logging

Description
logging defines parameters for what should be logged where. If this field is empty, operational logs are enabled but access logs are disabled.

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
<td style="text-align: left;"><p><code>access</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>access describes how the client requests should be logged.</p>
<p>If this field is empty, access logging is disabled.</p></td>
</tr>
</tbody>
</table>

## .spec.logging.access

Description
access describes how the client requests should be logged.

If this field is empty, access logging is disabled.

Type
`object`

Required
- `destination`

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
<td style="text-align: left;"><p><code>destination</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>destination is where access logs go.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>httpCaptureCookies</code></p></td>
<td style="text-align: left;"><p>``</p></td>
<td style="text-align: left;"><p>httpCaptureCookies specifies HTTP cookies that should be captured in access logs. If this field is empty, no cookies are captured.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>httpCaptureHeaders</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>httpCaptureHeaders defines HTTP headers that should be captured in access logs. If this field is empty, no headers are captured.</p>
<p>Note that this option only applies to cleartext HTTP connections and to secure HTTP connections for which the ingress controller terminates encryption (that is, edge-terminated or reencrypt connections). Headers cannot be captured for TLS passthrough connections.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>httpLogFormat</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>httpLogFormat specifies the format of the log message for an HTTP request.</p>
<p>If this field is empty, log messages use the implementation’s default HTTP log format. For HAProxy’s default HTTP log format, see the HAProxy documentation: <a href="http://cbonte.github.io/haproxy-dconv/2.0/configuration.html#8.2.3">http://cbonte.github.io/haproxy-dconv/2.0/configuration.html#8.2.3</a></p>
<p>Note that this format only applies to cleartext HTTP connections and to secure HTTP connections for which the ingress controller terminates encryption (that is, edge-terminated or reencrypt connections). It does not affect the log format for TLS passthrough connections.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>logEmptyRequests</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>logEmptyRequests specifies how connections on which no request is received should be logged. Typically, these empty requests come from load balancers' health probes or Web browsers' speculative connections ("preconnect"), in which case logging these requests may be undesirable. However, these requests may also be caused by network errors, in which case logging empty requests may be useful for diagnosing the errors. In addition, these requests may be caused by port scans, in which case logging empty requests may aid in detecting intrusion attempts. Allowed values for this field are "Log" and "Ignore". The default value is "Log".</p></td>
</tr>
</tbody>
</table>

## .spec.logging.access.destination

Description
destination is where access logs go.

Type
`object`

Required
- `type`

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
<td style="text-align: left;"><p><code>container</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>container holds parameters for the Container logging destination. Present only if type is Container.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>syslog</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>syslog holds parameters for a syslog endpoint. Present only if type is Syslog.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>type</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>type is the type of destination for logs. It must be one of the following:</p>
<p>* Container</p>
<p>The ingress operator configures the sidecar container named "logs" on the ingress controller pod and configures the ingress controller to write logs to the sidecar. The logs are then available as container logs. The expectation is that the administrator configures a custom logging solution that reads logs from this sidecar. Note that using container logs means that logs may be dropped if the rate of logs exceeds the container runtime’s or the custom logging solution’s capacity.</p>
<p>* Syslog</p>
<p>Logs are sent to a syslog endpoint. The administrator must specify an endpoint that can receive syslog messages. The expectation is that the administrator has configured a custom syslog instance.</p></td>
</tr>
</tbody>
</table>

## .spec.logging.access.destination.container

Description
container holds parameters for the Container logging destination. Present only if type is Container.

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
<td style="text-align: left;"><p><code>maxLength</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p>maxLength is the maximum length of the log message.</p>
<p>Valid values are integers in the range 480 to 8192, inclusive.</p>
<p>When omitted, the default value is 1024.</p></td>
</tr>
</tbody>
</table>

## .spec.logging.access.destination.syslog

Description
syslog holds parameters for a syslog endpoint. Present only if type is Syslog.

Type
`object`

Required
- `address`

- `port`

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
<td style="text-align: left;"><p><code>address</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>address is the IP address of the syslog endpoint that receives log messages.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>facility</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>facility specifies the syslog facility of log messages.</p>
<p>If this field is empty, the facility is "local1".</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>maxLength</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p>maxLength is the maximum length of the log message.</p>
<p>Valid values are integers in the range 480 to 4096, inclusive.</p>
<p>When omitted, the default value is 1024.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>port</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p>port is the UDP port number of the syslog endpoint that receives log messages.</p></td>
</tr>
</tbody>
</table>

## .spec.logging.access.httpCaptureHeaders

Description
httpCaptureHeaders defines HTTP headers that should be captured in access logs. If this field is empty, no headers are captured.

Note that this option only applies to cleartext HTTP connections and to secure HTTP connections for which the ingress controller terminates encryption (that is, edge-terminated or reencrypt connections). Headers cannot be captured for TLS passthrough connections.

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
<td style="text-align: left;"><p><code>request</code></p></td>
<td style="text-align: left;"><p>``</p></td>
<td style="text-align: left;"><p>request specifies which HTTP request headers to capture.</p>
<p>If this field is empty, no request headers are captured.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>response</code></p></td>
<td style="text-align: left;"><p>``</p></td>
<td style="text-align: left;"><p>response specifies which HTTP response headers to capture.</p>
<p>If this field is empty, no response headers are captured.</p></td>
</tr>
</tbody>
</table>

## .spec.namespaceSelector

Description
namespaceSelector is used to filter the set of namespaces serviced by the ingress controller. This is useful for implementing shards.

If unset, the default is no filtering.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `matchExpressions` | `array` | matchExpressions is a list of label selector requirements. The requirements are ANDed. |
| `matchExpressions[]` | `object` | A label selector requirement is a selector that contains values, a key, and an operator that relates the key and values. |
| `matchLabels` | `object (string)` | matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed. |

## .spec.namespaceSelector.matchExpressions

Description
matchExpressions is a list of label selector requirements. The requirements are ANDed.

Type
`array`

## .spec.namespaceSelector.matchExpressions\[\]

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

## .spec.nodePlacement

Description
nodePlacement enables explicit control over the scheduling of the ingress controller.

If unset, defaults are used. See NodePlacement for more details.

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
<td style="text-align: left;"><p><code>nodeSelector</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>nodeSelector is the node selector applied to ingress controller deployments.</p>
<p>If set, the specified selector is used and replaces the default.</p>
<p>If unset, the default depends on the value of the defaultPlacement field in the cluster config.openshift.io/v1/ingresses status.</p>
<p>When defaultPlacement is Workers, the default is:</p>
<p>kubernetes.io/os: linux node-role.kubernetes.io/worker: ''</p>
<p>When defaultPlacement is ControlPlane, the default is:</p>
<p>kubernetes.io/os: linux node-role.kubernetes.io/master: ''</p>
<p>These defaults are subject to change.</p>
<p>Note that using nodeSelector.matchExpressions is not supported. Only nodeSelector.matchLabels may be used. This is a limitation of the Kubernetes API: the pod spec does not allow complex expressions for node selectors.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>tolerations</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>tolerations is a list of tolerations applied to ingress controller deployments.</p>
<p>The default is an empty list.</p>
<p>See <a href="https://kubernetes.io/docs/concepts/configuration/taint-and-toleration/">https://kubernetes.io/docs/concepts/configuration/taint-and-toleration/</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>tolerations[]</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>The pod this Toleration is attached to tolerates any taint that matches the triple &lt;key,value,effect&gt; using the matching operator &lt;operator&gt;.</p></td>
</tr>
</tbody>
</table>

## .spec.nodePlacement.nodeSelector

Description
nodeSelector is the node selector applied to ingress controller deployments.

If set, the specified selector is used and replaces the default.

If unset, the default depends on the value of the defaultPlacement field in the cluster config.openshift.io/v1/ingresses status.

When defaultPlacement is Workers, the default is:

    kubernetes.io/os: linux
    node-role.kubernetes.io/worker: ''

When defaultPlacement is ControlPlane, the default is:

    kubernetes.io/os: linux
    node-role.kubernetes.io/master: ''

These defaults are subject to change.

Note that using nodeSelector.matchExpressions is not supported. Only nodeSelector.matchLabels may be used. This is a limitation of the Kubernetes API: the pod spec does not allow complex expressions for node selectors.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `matchExpressions` | `array` | matchExpressions is a list of label selector requirements. The requirements are ANDed. |
| `matchExpressions[]` | `object` | A label selector requirement is a selector that contains values, a key, and an operator that relates the key and values. |
| `matchLabels` | `object (string)` | matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed. |

## .spec.nodePlacement.nodeSelector.matchExpressions

Description
matchExpressions is a list of label selector requirements. The requirements are ANDed.

Type
`array`

## .spec.nodePlacement.nodeSelector.matchExpressions\[\]

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

## .spec.nodePlacement.tolerations

Description
tolerations is a list of tolerations applied to ingress controller deployments.

The default is an empty list.

See <https://kubernetes.io/docs/concepts/configuration/taint-and-toleration/>

Type
`array`

## .spec.nodePlacement.tolerations\[\]

Description
The pod this Toleration is attached to tolerates any taint that matches the triple \<key,value,effect\> using the matching operator \<operator\>.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `effect` | `string` | Effect indicates the taint effect to match. Empty means match all taint effects. When specified, allowed values are NoSchedule, PreferNoSchedule and NoExecute. |
| `key` | `string` | Key is the taint key that the toleration applies to. Empty means match all taint keys. If the key is empty, operator must be Exists; this combination means to match all values and all keys. |
| `operator` | `string` | Operator represents a key’s relationship to the value. Valid operators are Exists and Equal. Defaults to Equal. Exists is equivalent to wildcard for value, so that a pod can tolerate all taints of a particular category. |
| `tolerationSeconds` | `integer` | TolerationSeconds represents the period of time the toleration (which must be of effect NoExecute, otherwise this field is ignored) tolerates the taint. By default, it is not set, which means tolerate the taint forever (do not evict). Zero and negative values will be treated as 0 (evict immediately) by the system. |
| `value` | `string` | Value is the taint value the toleration matches to. If the operator is Exists, the value should be empty, otherwise just a regular string. |

## .spec.routeAdmission

Description
routeAdmission defines a policy for handling new route claims (for example, to allow or deny claims across namespaces).

If empty, defaults will be applied. See specific routeAdmission fields for details about their defaults.

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
<td style="text-align: left;"><p><code>namespaceOwnership</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>namespaceOwnership describes how host name claims across namespaces should be handled.</p>
<p>Value must be one of:</p>
<p>- Strict: Do not allow routes in different namespaces to claim the same host.</p>
<p>- InterNamespaceAllowed: Allow routes to claim different paths of the same host name across namespaces.</p>
<p>If empty, the default is Strict.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>wildcardPolicy</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>wildcardPolicy describes how routes with wildcard policies should be handled for the ingress controller. WildcardPolicy controls use of routes [1] exposed by the ingress controller based on the route’s wildcard policy.</p>
<p>[1] <a href="https://github.com/openshift/api/blob/master/route/v1/types.go">https://github.com/openshift/api/blob/master/route/v1/types.go</a></p>
<p>Note: Updating WildcardPolicy from WildcardsAllowed to WildcardsDisallowed will cause admitted routes with a wildcard policy of Subdomain to stop working. These routes must be updated to a wildcard policy of None to be readmitted by the ingress controller.</p>
<p>WildcardPolicy supports WildcardsAllowed and WildcardsDisallowed values.</p>
<p>If empty, defaults to "WildcardsDisallowed".</p></td>
</tr>
</tbody>
</table>

## .spec.routeSelector

Description
routeSelector is used to filter the set of Routes serviced by the ingress controller. This is useful for implementing shards.

If unset, the default is no filtering.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `matchExpressions` | `array` | matchExpressions is a list of label selector requirements. The requirements are ANDed. |
| `matchExpressions[]` | `object` | A label selector requirement is a selector that contains values, a key, and an operator that relates the key and values. |
| `matchLabels` | `object (string)` | matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed. |

## .spec.routeSelector.matchExpressions

Description
matchExpressions is a list of label selector requirements. The requirements are ANDed.

Type
`array`

## .spec.routeSelector.matchExpressions\[\]

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

## .spec.tlsSecurityProfile

Description
tlsSecurityProfile specifies settings for TLS connections for ingresscontrollers.

If unset, the default is based on the apiservers.config.openshift.io/cluster resource.

Note that when using the Old, Intermediate, and Modern profile types, the effective profile configuration is subject to change between releases. For example, given a specification to use the Intermediate profile deployed on release X.Y.Z, an upgrade to release X.Y.Z+1 may cause a new profile configuration to be applied to the ingress controller, resulting in a rollout.

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
<td style="text-align: left;"><p><code>custom</code></p></td>
<td style="text-align: left;"><p>``</p></td>
<td style="text-align: left;"><p>custom is a user-defined TLS security profile. Be extremely careful using a custom profile as invalid configurations can be catastrophic. An example custom profile looks like this:</p>
<p>ciphers:</p>
<p>- ECDHE-ECDSA-CHACHA20-POLY1305</p>
<p>- ECDHE-RSA-CHACHA20-POLY1305</p>
<p>- ECDHE-RSA-AES128-GCM-SHA256</p>
<p>- ECDHE-ECDSA-AES128-GCM-SHA256</p>
<p>minTLSVersion: VersionTLS11</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>intermediate</code></p></td>
<td style="text-align: left;"><p>``</p></td>
<td style="text-align: left;"><p>intermediate is a TLS security profile based on:</p>
<p><a href="https://wiki.mozilla.org/Security/Server_Side_TLS#Intermediate_compatibility_.28recommended.29">https://wiki.mozilla.org/Security/Server_Side_TLS#Intermediate_compatibility_.28recommended.29</a></p>
<p>and looks like this (yaml):</p>
<p>ciphers:</p>
<p>- TLS_AES_128_GCM_SHA256</p>
<p>- TLS_AES_256_GCM_SHA384</p>
<p>- TLS_CHACHA20_POLY1305_SHA256</p>
<p>- ECDHE-ECDSA-AES128-GCM-SHA256</p>
<p>- ECDHE-RSA-AES128-GCM-SHA256</p>
<p>- ECDHE-ECDSA-AES256-GCM-SHA384</p>
<p>- ECDHE-RSA-AES256-GCM-SHA384</p>
<p>- ECDHE-ECDSA-CHACHA20-POLY1305</p>
<p>- ECDHE-RSA-CHACHA20-POLY1305</p>
<p>- DHE-RSA-AES128-GCM-SHA256</p>
<p>- DHE-RSA-AES256-GCM-SHA384</p>
<p>minTLSVersion: VersionTLS12</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>modern</code></p></td>
<td style="text-align: left;"><p>``</p></td>
<td style="text-align: left;"><p>modern is a TLS security profile based on:</p>
<p><a href="https://wiki.mozilla.org/Security/Server_Side_TLS#Modern_compatibility">https://wiki.mozilla.org/Security/Server_Side_TLS#Modern_compatibility</a></p>
<p>and looks like this (yaml):</p>
<p>ciphers:</p>
<p>- TLS_AES_128_GCM_SHA256</p>
<p>- TLS_AES_256_GCM_SHA384</p>
<p>- TLS_CHACHA20_POLY1305_SHA256</p>
<p>minTLSVersion: VersionTLS13</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>old</code></p></td>
<td style="text-align: left;"><p>``</p></td>
<td style="text-align: left;"><p>old is a TLS security profile based on:</p>
<p><a href="https://wiki.mozilla.org/Security/Server_Side_TLS#Old_backward_compatibility">https://wiki.mozilla.org/Security/Server_Side_TLS#Old_backward_compatibility</a></p>
<p>and looks like this (yaml):</p>
<p>ciphers:</p>
<p>- TLS_AES_128_GCM_SHA256</p>
<p>- TLS_AES_256_GCM_SHA384</p>
<p>- TLS_CHACHA20_POLY1305_SHA256</p>
<p>- ECDHE-ECDSA-AES128-GCM-SHA256</p>
<p>- ECDHE-RSA-AES128-GCM-SHA256</p>
<p>- ECDHE-ECDSA-AES256-GCM-SHA384</p>
<p>- ECDHE-RSA-AES256-GCM-SHA384</p>
<p>- ECDHE-ECDSA-CHACHA20-POLY1305</p>
<p>- ECDHE-RSA-CHACHA20-POLY1305</p>
<p>- DHE-RSA-AES128-GCM-SHA256</p>
<p>- DHE-RSA-AES256-GCM-SHA384</p>
<p>- DHE-RSA-CHACHA20-POLY1305</p>
<p>- ECDHE-ECDSA-AES128-SHA256</p>
<p>- ECDHE-RSA-AES128-SHA256</p>
<p>- ECDHE-ECDSA-AES128-SHA</p>
<p>- ECDHE-RSA-AES128-SHA</p>
<p>- ECDHE-ECDSA-AES256-SHA384</p>
<p>- ECDHE-RSA-AES256-SHA384</p>
<p>- ECDHE-ECDSA-AES256-SHA</p>
<p>- ECDHE-RSA-AES256-SHA</p>
<p>- DHE-RSA-AES128-SHA256</p>
<p>- DHE-RSA-AES256-SHA256</p>
<p>- AES128-GCM-SHA256</p>
<p>- AES256-GCM-SHA384</p>
<p>- AES128-SHA256</p>
<p>- AES256-SHA256</p>
<p>- AES128-SHA</p>
<p>- AES256-SHA</p>
<p>- DES-CBC3-SHA</p>
<p>minTLSVersion: VersionTLS10</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>type</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>type is one of Old, Intermediate, Modern or Custom. Custom provides the ability to specify individual TLS security profile parameters. Old, Intermediate and Modern are TLS security profiles based on:</p>
<p><a href="https://wiki.mozilla.org/Security/Server_Side_TLS#Recommended_configurations">https://wiki.mozilla.org/Security/Server_Side_TLS#Recommended_configurations</a></p>
<p>The profiles are intent based, so they may change over time as new ciphers are developed and existing ciphers are found to be insecure. Depending on precisely which ciphers are available to a process, the list may be reduced.</p>
<p>Note that the Modern profile is currently not supported because it is not yet well adopted by common software libraries.</p></td>
</tr>
</tbody>
</table>

## .spec.tuningOptions

Description
tuningOptions defines parameters for adjusting the performance of ingress controller pods. All fields are optional and will use their respective defaults if not set. See specific tuningOptions fields for more details.

Setting fields within tuningOptions is generally not recommended. The default values are suitable for most configurations.

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
<td style="text-align: left;"><p><code>clientFinTimeout</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>clientFinTimeout defines how long a connection will be held open while waiting for the client response to the server/backend closing the connection.</p>
<p>If unset, the default timeout is 1s</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>clientTimeout</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>clientTimeout defines how long a connection will be held open while waiting for a client response.</p>
<p>If unset, the default timeout is 30s</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>connectTimeout</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>connectTimeout defines the maximum time to wait for a connection attempt to a server/backend to succeed.</p>
<p>This field expects an unsigned duration string of decimal numbers, each with optional fraction and a unit suffix, e.g. "300ms", "1.5h" or "2h45m". Valid time units are "ns", "us" (or "µs" U+00B5 or "μs" U+03BC), "ms", "s", "m", "h".</p>
<p>When omitted, this means the user has no opinion and the platform is left to choose a reasonable default. This default is subject to change over time. The current default is 5s.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>headerBufferBytes</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p>headerBufferBytes describes how much memory should be reserved (in bytes) for IngressController connection sessions. Note that this value must be at least 16384 if HTTP/2 is enabled for the IngressController (<a href="https://tools.ietf.org/html/rfc7540">https://tools.ietf.org/html/rfc7540</a>). If this field is empty, the IngressController will use a default value of 32768 bytes.</p>
<p>Setting this field is generally not recommended as headerBufferBytes values that are too small may break the IngressController and headerBufferBytes values that are too large could cause the IngressController to use significantly more memory than necessary.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>headerBufferMaxRewriteBytes</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p>headerBufferMaxRewriteBytes describes how much memory should be reserved (in bytes) from headerBufferBytes for HTTP header rewriting and appending for IngressController connection sessions. Note that incoming HTTP requests will be limited to (headerBufferBytes - headerBufferMaxRewriteBytes) bytes, meaning headerBufferBytes must be greater than headerBufferMaxRewriteBytes. If this field is empty, the IngressController will use a default value of 8192 bytes.</p>
<p>Setting this field is generally not recommended as headerBufferMaxRewriteBytes values that are too small may break the IngressController and headerBufferMaxRewriteBytes values that are too large could cause the IngressController to use significantly more memory than necessary.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>healthCheckInterval</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>healthCheckInterval defines how long the router waits between two consecutive health checks on its configured backends. This value is applied globally as a default for all routes, but may be overridden per-route by the route annotation "router.openshift.io/haproxy.health.check.interval".</p>
<p>Expects an unsigned duration string of decimal numbers, each with optional fraction and a unit suffix, eg "300ms", "1.5h" or "2h45m". Valid time units are "ns", "us" (or "µs" U+00B5 or "μs" U+03BC), "ms", "s", "m", "h".</p>
<p>Setting this to less than 5s can cause excess traffic due to too frequent TCP health checks and accompanying SYN packet storms. Alternatively, setting this too high can result in increased latency, due to backend servers that are no longer available, but haven’t yet been detected as such.</p>
<p>An empty or zero healthCheckInterval means no opinion and IngressController chooses a default, which is subject to change over time. Currently the default healthCheckInterval value is 5s.</p>
<p>Currently the minimum allowed value is 1s and the maximum allowed value is 2147483647ms (24.85 days). Both are subject to change over time.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>maxConnections</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p>maxConnections defines the maximum number of simultaneous connections that can be established per HAProxy process. Increasing this value allows each ingress controller pod to handle more connections but at the cost of additional system resources being consumed.</p>
<p>Permitted values are: empty, 0, -1, and the range 2000-2000000.</p>
<p>If this field is empty or 0, the IngressController will use the default value of 50000, but the default is subject to change in future releases.</p>
<p>If the value is -1 then HAProxy will dynamically compute a maximum value based on the available ulimits in the running container. Selecting -1 (i.e., auto) will result in a large value being computed (~520000 on OpenShift &gt;=4.10 clusters) and therefore each HAProxy process will incur significant memory usage compared to the current default of 50000.</p>
<p>Setting a value that is greater than the current operating system limit will prevent the HAProxy process from starting.</p>
<p>If you choose a discrete value (e.g., 750000) and the router pod is migrated to a new node, there’s no guarantee that that new node has identical ulimits configured. In such a scenario the pod would fail to start. If you have nodes with different ulimits configured (e.g., different tuned profiles) and you choose a discrete value then the guidance is to use -1 and let the value be computed dynamically at runtime.</p>
<p>You can monitor memory usage for router containers with the following metric: 'container_memory_working_set_bytes{container="router",namespace="openshift-ingress"}'.</p>
<p>You can monitor memory usage of individual HAProxy processes in router containers with the following metric: 'container_memory_working_set_bytes{container="router",namespace="openshift-ingress"}/container_processes{container="router",namespace="openshift-ingress"}'.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>reloadInterval</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>reloadInterval defines the minimum interval at which the router is allowed to reload to accept new changes. Increasing this value can prevent the accumulation of HAProxy processes, depending on the scenario. Increasing this interval can also lessen load imbalance on a backend’s servers when using the roundrobin balancing algorithm. Alternatively, decreasing this value may decrease latency since updates to HAProxy’s configuration can take effect more quickly.</p>
<p>The value must be a time duration value; see <a href="https://pkg.go.dev/time#ParseDuration">https://pkg.go.dev/time#ParseDuration</a>. Currently, the minimum value allowed is 1s, and the maximum allowed value is 120s. Minimum and maximum allowed values may change in future versions of OpenShift. Note that if a duration outside of these bounds is provided, the value of reloadInterval will be capped/floored and not rejected (e.g. a duration of over 120s will be capped to 120s; the IngressController will not reject and replace this disallowed value with the default).</p>
<p>A zero value for reloadInterval tells the IngressController to choose the default, which is currently 5s and subject to change without notice.</p>
<p>This field expects an unsigned duration string of decimal numbers, each with optional fraction and a unit suffix, e.g. "300ms", "1.5h" or "2h45m". Valid time units are "ns", "us" (or "µs" U+00B5 or "μs" U+03BC), "ms", "s", "m", "h".</p>
<p>Note: Setting a value significantly larger than the default of 5s can cause latency in observing updates to routes and their endpoints. HAProxy’s configuration will be reloaded less frequently, and newly created routes will not be served until the subsequent reload.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>serverFinTimeout</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>serverFinTimeout defines how long a connection will be held open while waiting for the server/backend response to the client closing the connection.</p>
<p>If unset, the default timeout is 1s</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>serverTimeout</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>serverTimeout defines how long a connection will be held open while waiting for a server/backend response.</p>
<p>If unset, the default timeout is 30s</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>threadCount</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p>threadCount defines the number of threads created per HAProxy process. Creating more threads allows each ingress controller pod to handle more connections, at the cost of more system resources being used. HAProxy currently supports up to 64 threads. If this field is empty, the IngressController will use the default value. The current default is 4 threads, but this may change in future releases.</p>
<p>Setting this field is generally not recommended. Increasing the number of HAProxy threads allows ingress controller pods to utilize more CPU time under load, potentially starving other pods if set too high. Reducing the number of threads may cause the ingress controller to perform poorly.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>tlsInspectDelay</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>tlsInspectDelay defines how long the router can hold data to find a matching route.</p>
<p>Setting this too short can cause the router to fall back to the default certificate for edge-terminated or reencrypt routes even when a better matching certificate could be used.</p>
<p>If unset, the default inspect delay is 5s</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>tunnelTimeout</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>tunnelTimeout defines how long a tunnel connection (including websockets) will be held open while the tunnel is idle.</p>
<p>If unset, the default timeout is 1h</p></td>
</tr>
</tbody>
</table>

## .status

Description
status is the most recently observed status of the IngressController.

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
<td style="text-align: left;"><p><code>availableReplicas</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p>availableReplicas is number of observed available replicas according to the ingress controller deployment.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>conditions</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>conditions is a list of conditions and their status.</p>
<p>Available means the ingress controller deployment is available and servicing route and ingress resources (i.e, .status.availableReplicas equals .spec.replicas)</p>
<p>There are additional conditions which indicate the status of other ingress controller features and capabilities.</p>
<p>* LoadBalancerManaged - True if the following conditions are met: * The endpoint publishing strategy requires a service load balancer. - False if any of those conditions are unsatisfied.</p>
<p>* LoadBalancerReady - True if the following conditions are met: * A load balancer is managed. * The load balancer is ready. - False if any of those conditions are unsatisfied.</p>
<p>* DNSManaged - True if the following conditions are met: * The endpoint publishing strategy and platform support DNS. * The ingress controller domain is set. * dns.config.openshift.io/cluster configures DNS zones. - False if any of those conditions are unsatisfied.</p>
<p>* DNSReady - True if the following conditions are met: * DNS is managed. * DNS records have been successfully created. - False if any of those conditions are unsatisfied.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>conditions[]</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>OperatorCondition is just the standard condition fields.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>domain</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>domain is the actual domain in use.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>endpointPublishingStrategy</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>endpointPublishingStrategy is the actual strategy in use.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>namespaceSelector</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>namespaceSelector is the actual namespaceSelector in use.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>observedGeneration</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p>observedGeneration is the most recent generation observed.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>routeSelector</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>routeSelector is the actual routeSelector in use.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>selector</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>selector is a label selector, in string format, for ingress controller pods corresponding to the IngressController. The number of matching pods should equal the value of availableReplicas.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>tlsProfile</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>tlsProfile is the TLS connection configuration that is in effect.</p></td>
</tr>
</tbody>
</table>

## .status.conditions

Description
conditions is a list of conditions and their status.

Available means the ingress controller deployment is available and servicing route and ingress resources (i.e, .status.availableReplicas equals .spec.replicas)

There are additional conditions which indicate the status of other ingress controller features and capabilities.

- LoadBalancerManaged

  - True if the following conditions are met:

- The endpoint publishing strategy requires a service load balancer.

  - False if any of those conditions are unsatisfied.

- LoadBalancerReady

  - True if the following conditions are met:

- A load balancer is managed.

- The load balancer is ready.

  - False if any of those conditions are unsatisfied.

- DNSManaged

  - True if the following conditions are met:

- The endpoint publishing strategy and platform support DNS.

- The ingress controller domain is set.

- dns.config.openshift.io/cluster configures DNS zones.

  - False if any of those conditions are unsatisfied.

- DNSReady

  - True if the following conditions are met:

- DNS is managed.

- DNS records have been successfully created.

  - False if any of those conditions are unsatisfied.

Type
`array`

## .status.conditions\[\]

Description
OperatorCondition is just the standard condition fields.

Type
`object`

Required
- `lastTransitionTime`

- `status`

- `type`

| Property | Type | Description |
|----|----|----|
| `lastTransitionTime` | `string` | lastTransitionTime is the last time the condition transitioned from one status to another. This should be when the underlying condition changed. If that is not known, then using the time when the API field changed is acceptable. |
| `message` | `string` |  |
| `reason` | `string` |  |
| `status` | `string` | status of the condition, one of True, False, Unknown. |
| `type` | `string` | type of condition in CamelCase or in foo.example.com/CamelCase. |

## .status.endpointPublishingStrategy

Description
endpointPublishingStrategy is the actual strategy in use.

Type
`object`

Required
- `type`

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
<td style="text-align: left;"><p><code>hostNetwork</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>hostNetwork holds parameters for the HostNetwork endpoint publishing strategy. Present only if type is HostNetwork.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>loadBalancer</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>loadBalancer holds parameters for the load balancer. Present only if type is LoadBalancerService.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>nodePort</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>nodePort holds parameters for the NodePortService endpoint publishing strategy. Present only if type is NodePortService.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>private</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>private holds parameters for the Private endpoint publishing strategy. Present only if type is Private.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>type</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>type is the publishing strategy to use. Valid values are:</p>
<p>* LoadBalancerService</p>
<p>Publishes the ingress controller using a Kubernetes LoadBalancer Service.</p>
<p>In this configuration, the ingress controller deployment uses container networking. A LoadBalancer Service is created to publish the deployment.</p>
<p>See: <a href="https://kubernetes.io/docs/concepts/services-networking/service/#loadbalancer">https://kubernetes.io/docs/concepts/services-networking/service/#loadbalancer</a></p>
<p>If domain is set, a wildcard DNS record will be managed to point at the LoadBalancer Service’s external name. DNS records are managed only in DNS zones defined by dns.config.openshift.io/cluster .spec.publicZone and .spec.privateZone.</p>
<p>Wildcard DNS management is currently supported only on the AWS, Azure, and GCP platforms.</p>
<p>* HostNetwork</p>
<p>Publishes the ingress controller on node ports where the ingress controller is deployed.</p>
<p>In this configuration, the ingress controller deployment uses host networking, bound to node ports 80 and 443. The user is responsible for configuring an external load balancer to publish the ingress controller via the node ports.</p>
<p>* Private</p>
<p>Does not publish the ingress controller.</p>
<p>In this configuration, the ingress controller deployment uses container networking, and is not explicitly published. The user must manually publish the ingress controller.</p>
<p>* NodePortService</p>
<p>Publishes the ingress controller using a Kubernetes NodePort Service.</p>
<p>In this configuration, the ingress controller deployment uses container networking. A NodePort Service is created to publish the deployment. The specific node ports are dynamically allocated by OpenShift; however, to support static port allocations, user changes to the node port field of the managed NodePort Service will preserved.</p></td>
</tr>
</tbody>
</table>

## .status.endpointPublishingStrategy.hostNetwork

Description
hostNetwork holds parameters for the HostNetwork endpoint publishing strategy. Present only if type is HostNetwork.

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
<td style="text-align: left;"><p><code>httpPort</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p>httpPort is the port on the host which should be used to listen for HTTP requests. This field should be set when port 80 is already in use. The value should not coincide with the NodePort range of the cluster. When the value is 0 or is not specified it defaults to 80.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>httpsPort</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p>httpsPort is the port on the host which should be used to listen for HTTPS requests. This field should be set when port 443 is already in use. The value should not coincide with the NodePort range of the cluster. When the value is 0 or is not specified it defaults to 443.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>protocol</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>protocol specifies whether the IngressController expects incoming connections to use plain TCP or whether the IngressController expects PROXY protocol.</p>
<p>PROXY protocol can be used with load balancers that support it to communicate the source addresses of client connections when forwarding those connections to the IngressController. Using PROXY protocol enables the IngressController to report those source addresses instead of reporting the load balancer’s address in HTTP headers and logs. Note that enabling PROXY protocol on the IngressController will cause connections to fail if you are not using a load balancer that uses PROXY protocol to forward connections to the IngressController. See <a href="http://www.haproxy.org/download/2.2/doc/proxy-protocol.txt">http://www.haproxy.org/download/2.2/doc/proxy-protocol.txt</a> for information about PROXY protocol.</p>
<p>The following values are valid for this field:</p>
<p>* The empty string. * "TCP". * "PROXY".</p>
<p>The empty string specifies the default, which is TCP without PROXY protocol. Note that the default is subject to change.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>statsPort</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p>statsPort is the port on the host where the stats from the router are published. The value should not coincide with the NodePort range of the cluster. If an external load balancer is configured to forward connections to this IngressController, the load balancer should use this port for health checks. The load balancer can send HTTP probes on this port on a given node, with the path /healthz/ready to determine if the ingress controller is ready to receive traffic on the node. For proper operation the load balancer must not forward traffic to a node until the health check reports ready. The load balancer should also stop forwarding requests within a maximum of 45 seconds after /healthz/ready starts reporting not-ready. Probing every 5 to 10 seconds, with a 5-second timeout and with a threshold of two successful or failed requests to become healthy or unhealthy respectively, are well-tested values. When the value is 0 or is not specified it defaults to 1936.</p></td>
</tr>
</tbody>
</table>

## .status.endpointPublishingStrategy.loadBalancer

Description
loadBalancer holds parameters for the load balancer. Present only if type is LoadBalancerService.

Type
`object`

Required
- `dnsManagementPolicy`

- `scope`

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
<td style="text-align: left;"><p><code>allowedSourceRanges</code></p></td>
<td style="text-align: left;"><p>``</p></td>
<td style="text-align: left;"><p>allowedSourceRanges specifies an allowlist of IP address ranges to which access to the load balancer should be restricted. Each range must be specified using CIDR notation (e.g. "10.0.0.0/8" or "fd00::/8"). If no range is specified, "0.0.0.0/0" for IPv4 and "::/0" for IPv6 are used by default, which allows all source addresses.</p>
<p>To facilitate migration from earlier versions of OpenShift that did not have the allowedSourceRanges field, you may set the service.beta.kubernetes.io/load-balancer-source-ranges annotation on the "router-&lt;ingresscontroller name&gt;" service in the "openshift-ingress" namespace, and this annotation will take effect if allowedSourceRanges is empty on OpenShift 4.12.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>dnsManagementPolicy</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>dnsManagementPolicy indicates if the lifecycle of the wildcard DNS record associated with the load balancer service will be managed by the ingress operator. It defaults to Managed. Valid values are: Managed and Unmanaged.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>providerParameters</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>providerParameters holds desired load balancer information specific to the underlying infrastructure provider.</p>
<p>If empty, defaults will be applied. See specific providerParameters fields for details about their defaults.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>scope</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>scope indicates the scope at which the load balancer is exposed. Possible values are "External" and "Internal".</p></td>
</tr>
</tbody>
</table>

## .status.endpointPublishingStrategy.loadBalancer.providerParameters

Description
providerParameters holds desired load balancer information specific to the underlying infrastructure provider.

If empty, defaults will be applied. See specific providerParameters fields for details about their defaults.

Type
`object`

Required
- `type`

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
<td style="text-align: left;"><p><code>aws</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>aws provides configuration settings that are specific to AWS load balancers.</p>
<p>If empty, defaults will be applied. See specific aws fields for details about their defaults.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>gcp</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>gcp provides configuration settings that are specific to GCP load balancers.</p>
<p>If empty, defaults will be applied. See specific gcp fields for details about their defaults.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>ibm</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>ibm provides configuration settings that are specific to IBM Cloud load balancers.</p>
<p>If empty, defaults will be applied. See specific ibm fields for details about their defaults.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>openstack</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>openstack provides configuration settings that are specific to OpenStack load balancers.</p>
<p>If empty, defaults will be applied. See specific openstack fields for details about their defaults.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>type</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>type is the underlying infrastructure provider for the load balancer. Allowed values are "AWS", "Azure", "BareMetal", "GCP", "IBM", "Nutanix", "OpenStack", and "VSphere".</p></td>
</tr>
</tbody>
</table>

## .status.endpointPublishingStrategy.loadBalancer.providerParameters.aws

Description
aws provides configuration settings that are specific to AWS load balancers.

If empty, defaults will be applied. See specific aws fields for details about their defaults.

Type
`object`

Required
- `type`

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
<td style="text-align: left;"><p><code>classicLoadBalancer</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>classicLoadBalancerParameters holds configuration parameters for an AWS classic load balancer. Present only if type is Classic.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>networkLoadBalancer</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>networkLoadBalancerParameters holds configuration parameters for an AWS network load balancer. Present only if type is NLB.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>type</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>type is the type of AWS load balancer to instantiate for an ingresscontroller.</p>
<p>Valid values are:</p>
<p>* "Classic": A Classic Load Balancer that makes routing decisions at either the transport layer (TCP/SSL) or the application layer (HTTP/HTTPS). See the following for additional details:</p>
<p><a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/load-balancer-types.html#clb">https://docs.aws.amazon.com/AmazonECS/latest/developerguide/load-balancer-types.html#clb</a></p>
<p>* "NLB": A Network Load Balancer that makes routing decisions at the transport layer (TCP/SSL). See the following for additional details:</p>
<p><a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/load-balancer-types.html#nlb">https://docs.aws.amazon.com/AmazonECS/latest/developerguide/load-balancer-types.html#nlb</a></p></td>
</tr>
</tbody>
</table>

## .status.endpointPublishingStrategy.loadBalancer.providerParameters.aws.classicLoadBalancer

Description
classicLoadBalancerParameters holds configuration parameters for an AWS classic load balancer. Present only if type is Classic.

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
<td style="text-align: left;"><p><code>connectionIdleTimeout</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>connectionIdleTimeout specifies the maximum time period that a connection may be idle before the load balancer closes the connection. The value must be parseable as a time duration value; see <a href="https://pkg.go.dev/time#ParseDuration">https://pkg.go.dev/time#ParseDuration</a>. A nil or zero value means no opinion, in which case a default value is used. The default value for this field is 60s. This default is subject to change.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>subnets</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>subnets specifies the subnets to which the load balancer will attach. The subnets may be specified by either their ID or name. The total number of subnets is limited to 10.</p>
<p>In order for the load balancer to be provisioned with subnets, each subnet must exist, each subnet must be from a different availability zone, and the load balancer service must be recreated to pick up new values.</p>
<p>When omitted from the spec, the subnets will be auto-discovered for each availability zone. Auto-discovered subnets are not reported in the status of the IngressController object.</p></td>
</tr>
</tbody>
</table>

## .status.endpointPublishingStrategy.loadBalancer.providerParameters.aws.classicLoadBalancer.subnets

Description
subnets specifies the subnets to which the load balancer will attach. The subnets may be specified by either their ID or name. The total number of subnets is limited to 10.

In order for the load balancer to be provisioned with subnets, each subnet must exist, each subnet must be from a different availability zone, and the load balancer service must be recreated to pick up new values.

When omitted from the spec, the subnets will be auto-discovered for each availability zone. Auto-discovered subnets are not reported in the status of the IngressController object.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `ids` | `array (string)` | ids specifies a list of AWS subnets by subnet ID. Subnet IDs must start with "subnet-", consist only of alphanumeric characters, must be exactly 24 characters long, must be unique, and the total number of subnets specified by ids and names must not exceed 10. |
| `names` | `array (string)` | names specifies a list of AWS subnets by subnet name. Subnet names must not start with "subnet-", must not include commas, must be under 256 characters in length, must be unique, and the total number of subnets specified by ids and names must not exceed 10. |

## .status.endpointPublishingStrategy.loadBalancer.providerParameters.aws.networkLoadBalancer

Description
networkLoadBalancerParameters holds configuration parameters for an AWS network load balancer. Present only if type is NLB.

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
<td style="text-align: left;"><p><code>eipAllocations</code></p></td>
<td style="text-align: left;"><p><code>array (string)</code></p></td>
<td style="text-align: left;"><p>eipAllocations is a list of IDs for Elastic IP (EIP) addresses that are assigned to the Network Load Balancer. The following restrictions apply:</p>
<p>eipAllocations can only be used with external scope, not internal. An EIP can be allocated to only a single IngressController. The number of EIP allocations must match the number of subnets that are used for the load balancer. Each EIP allocation must be unique. A maximum of 10 EIP allocations are permitted.</p>
<p>See <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/elastic-ip-addresses-eip.html">https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/elastic-ip-addresses-eip.html</a> for general information about configuration, characteristics, and limitations of Elastic IP addresses.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>subnets</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>subnets specifies the subnets to which the load balancer will attach. The subnets may be specified by either their ID or name. The total number of subnets is limited to 10.</p>
<p>In order for the load balancer to be provisioned with subnets, each subnet must exist, each subnet must be from a different availability zone, and the load balancer service must be recreated to pick up new values.</p>
<p>When omitted from the spec, the subnets will be auto-discovered for each availability zone. Auto-discovered subnets are not reported in the status of the IngressController object.</p></td>
</tr>
</tbody>
</table>

## .status.endpointPublishingStrategy.loadBalancer.providerParameters.aws.networkLoadBalancer.subnets

Description
subnets specifies the subnets to which the load balancer will attach. The subnets may be specified by either their ID or name. The total number of subnets is limited to 10.

In order for the load balancer to be provisioned with subnets, each subnet must exist, each subnet must be from a different availability zone, and the load balancer service must be recreated to pick up new values.

When omitted from the spec, the subnets will be auto-discovered for each availability zone. Auto-discovered subnets are not reported in the status of the IngressController object.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `ids` | `array (string)` | ids specifies a list of AWS subnets by subnet ID. Subnet IDs must start with "subnet-", consist only of alphanumeric characters, must be exactly 24 characters long, must be unique, and the total number of subnets specified by ids and names must not exceed 10. |
| `names` | `array (string)` | names specifies a list of AWS subnets by subnet name. Subnet names must not start with "subnet-", must not include commas, must be under 256 characters in length, must be unique, and the total number of subnets specified by ids and names must not exceed 10. |

## .status.endpointPublishingStrategy.loadBalancer.providerParameters.gcp

Description
gcp provides configuration settings that are specific to GCP load balancers.

If empty, defaults will be applied. See specific gcp fields for details about their defaults.

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
<td style="text-align: left;"><p><code>clientAccess</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>clientAccess describes how client access is restricted for internal load balancers.</p>
<p>Valid values are: * "Global": Specifying an internal load balancer with Global client access allows clients from any region within the VPC to communicate with the load balancer.</p>
<p><a href="https://cloud.google.com/kubernetes-engine/docs/how-to/internal-load-balancing#global_access">https://cloud.google.com/kubernetes-engine/docs/how-to/internal-load-balancing#global_access</a></p>
<p>* "Local": Specifying an internal load balancer with Local client access means only clients within the same region (and VPC) as the GCP load balancer can communicate with the load balancer. Note that this is the default behavior.</p>
<p><a href="https://cloud.google.com/load-balancing/docs/internal#client_access">https://cloud.google.com/load-balancing/docs/internal#client_access</a></p></td>
</tr>
</tbody>
</table>

## .status.endpointPublishingStrategy.loadBalancer.providerParameters.ibm

Description
ibm provides configuration settings that are specific to IBM Cloud load balancers.

If empty, defaults will be applied. See specific ibm fields for details about their defaults.

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
<td style="text-align: left;"><p><code>protocol</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>protocol specifies whether the load balancer uses PROXY protocol to forward connections to the IngressController. See "service.kubernetes.io/ibm-load-balancer-cloud-provider-enable-features: "proxy-protocol"" at <a href="https://cloud.ibm.com/docs/containers?topic=containers-vpc-lbaas">https://cloud.ibm.com/docs/containers?topic=containers-vpc-lbaas</a></p>
<p>PROXY protocol can be used with load balancers that support it to communicate the source addresses of client connections when forwarding those connections to the IngressController. Using PROXY protocol enables the IngressController to report those source addresses instead of reporting the load balancer’s address in HTTP headers and logs. Note that enabling PROXY protocol on the IngressController will cause connections to fail if you are not using a load balancer that uses PROXY protocol to forward connections to the IngressController. See <a href="http://www.haproxy.org/download/2.2/doc/proxy-protocol.txt">http://www.haproxy.org/download/2.2/doc/proxy-protocol.txt</a> for information about PROXY protocol.</p>
<p>Valid values for protocol are TCP, PROXY and omitted. When omitted, this means no opinion and the platform is left to choose a reasonable default, which is subject to change over time. The current default is TCP, without the proxy protocol enabled.</p></td>
</tr>
</tbody>
</table>

## .status.endpointPublishingStrategy.loadBalancer.providerParameters.openstack

Description
openstack provides configuration settings that are specific to OpenStack load balancers.

If empty, defaults will be applied. See specific openstack fields for details about their defaults.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `floatingIP` | `string` | floatingIP specifies the IP address that the load balancer will use. When not specified, an IP address will be assigned randomly by the OpenStack cloud provider. When specified, the floating IP has to be pre-created. If the specified value is not a floating IP or is already claimed, the OpenStack cloud provider won’t be able to provision the load balancer. This field may only be used if the IngressController has External scope. This value must be a valid IPv4 or IPv6 address. |

## .status.endpointPublishingStrategy.nodePort

Description
nodePort holds parameters for the NodePortService endpoint publishing strategy. Present only if type is NodePortService.

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
<td style="text-align: left;"><p><code>protocol</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>protocol specifies whether the IngressController expects incoming connections to use plain TCP or whether the IngressController expects PROXY protocol.</p>
<p>PROXY protocol can be used with load balancers that support it to communicate the source addresses of client connections when forwarding those connections to the IngressController. Using PROXY protocol enables the IngressController to report those source addresses instead of reporting the load balancer’s address in HTTP headers and logs. Note that enabling PROXY protocol on the IngressController will cause connections to fail if you are not using a load balancer that uses PROXY protocol to forward connections to the IngressController. See <a href="http://www.haproxy.org/download/2.2/doc/proxy-protocol.txt">http://www.haproxy.org/download/2.2/doc/proxy-protocol.txt</a> for information about PROXY protocol.</p>
<p>The following values are valid for this field:</p>
<p>* The empty string. * "TCP". * "PROXY".</p>
<p>The empty string specifies the default, which is TCP without PROXY protocol. Note that the default is subject to change.</p></td>
</tr>
</tbody>
</table>

## .status.endpointPublishingStrategy.private

Description
private holds parameters for the Private endpoint publishing strategy. Present only if type is Private.

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
<td style="text-align: left;"><p><code>protocol</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>protocol specifies whether the IngressController expects incoming connections to use plain TCP or whether the IngressController expects PROXY protocol.</p>
<p>PROXY protocol can be used with load balancers that support it to communicate the source addresses of client connections when forwarding those connections to the IngressController. Using PROXY protocol enables the IngressController to report those source addresses instead of reporting the load balancer’s address in HTTP headers and logs. Note that enabling PROXY protocol on the IngressController will cause connections to fail if you are not using a load balancer that uses PROXY protocol to forward connections to the IngressController. See <a href="http://www.haproxy.org/download/2.2/doc/proxy-protocol.txt">http://www.haproxy.org/download/2.2/doc/proxy-protocol.txt</a> for information about PROXY protocol.</p>
<p>The following values are valid for this field:</p>
<p>* The empty string. * "TCP". * "PROXY".</p>
<p>The empty string specifies the default, which is TCP without PROXY protocol. Note that the default is subject to change.</p></td>
</tr>
</tbody>
</table>

## .status.namespaceSelector

Description
namespaceSelector is the actual namespaceSelector in use.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `matchExpressions` | `array` | matchExpressions is a list of label selector requirements. The requirements are ANDed. |
| `matchExpressions[]` | `object` | A label selector requirement is a selector that contains values, a key, and an operator that relates the key and values. |
| `matchLabels` | `object (string)` | matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed. |

## .status.namespaceSelector.matchExpressions

Description
matchExpressions is a list of label selector requirements. The requirements are ANDed.

Type
`array`

## .status.namespaceSelector.matchExpressions\[\]

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

## .status.routeSelector

Description
routeSelector is the actual routeSelector in use.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `matchExpressions` | `array` | matchExpressions is a list of label selector requirements. The requirements are ANDed. |
| `matchExpressions[]` | `object` | A label selector requirement is a selector that contains values, a key, and an operator that relates the key and values. |
| `matchLabels` | `object (string)` | matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed. |

## .status.routeSelector.matchExpressions

Description
matchExpressions is a list of label selector requirements. The requirements are ANDed.

Type
`array`

## .status.routeSelector.matchExpressions\[\]

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

## .status.tlsProfile

Description
tlsProfile is the TLS connection configuration that is in effect.

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
<td style="text-align: left;"><p><code>ciphers</code></p></td>
<td style="text-align: left;"><p><code>array (string)</code></p></td>
<td style="text-align: left;"><p>ciphers is used to specify the cipher algorithms that are negotiated during the TLS handshake. Operators may remove entries their operands do not support. For example, to use DES-CBC3-SHA (yaml):</p>
<p>ciphers: - DES-CBC3-SHA</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>minTLSVersion</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>minTLSVersion is used to specify the minimal version of the TLS protocol that is negotiated during the TLS handshake. For example, to use TLS versions 1.1, 1.2 and 1.3 (yaml):</p>
<p>minTLSVersion: VersionTLS11</p>
<p>NOTE: currently the highest minTLSVersion allowed is VersionTLS12</p></td>
</tr>
</tbody>
</table>

# API endpoints

The following API endpoints are available:

- `/apis/operator.openshift.io/v1/ingresscontrollers`

  - `GET`: list objects of kind IngressController

- `/apis/operator.openshift.io/v1/namespaces/{namespace}/ingresscontrollers`

  - `DELETE`: delete collection of IngressController

  - `GET`: list objects of kind IngressController

  - `POST`: create an IngressController

- `/apis/operator.openshift.io/v1/namespaces/{namespace}/ingresscontrollers/{name}`

  - `DELETE`: delete an IngressController

  - `GET`: read the specified IngressController

  - `PATCH`: partially update the specified IngressController

  - `PUT`: replace the specified IngressController

- `/apis/operator.openshift.io/v1/namespaces/{namespace}/ingresscontrollers/{name}/scale`

  - `GET`: read scale of the specified IngressController

  - `PATCH`: partially update scale of the specified IngressController

  - `PUT`: replace scale of the specified IngressController

- `/apis/operator.openshift.io/v1/namespaces/{namespace}/ingresscontrollers/{name}/status`

  - `GET`: read status of the specified IngressController

  - `PATCH`: partially update status of the specified IngressController

  - `PUT`: replace status of the specified IngressController

## /apis/operator.openshift.io/v1/ingresscontrollers

HTTP method
`GET`

Description
list objects of kind IngressController

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`IngressControllerList`](../objects/index.md#io-openshift-operator-v1-IngressControllerList) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/operator.openshift.io/v1/namespaces/{namespace}/ingresscontrollers

HTTP method
`DELETE`

Description
delete collection of IngressController

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Status`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`GET`

Description
list objects of kind IngressController

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`IngressControllerList`](../objects/index.md#io-openshift-operator-v1-IngressControllerList) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`POST`

Description
create an IngressController

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`IngressController`](ingresscontroller-operator-openshift-io-v1.md#ingresscontroller-operator-openshift-io-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`IngressController`](ingresscontroller-operator-openshift-io-v1.md#ingresscontroller-operator-openshift-io-v1) schema |
| 201 - Created | [`IngressController`](ingresscontroller-operator-openshift-io-v1.md#ingresscontroller-operator-openshift-io-v1) schema |
| 202 - Accepted | [`IngressController`](ingresscontroller-operator-openshift-io-v1.md#ingresscontroller-operator-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/operator.openshift.io/v1/namespaces/{namespace}/ingresscontrollers/{name}

| Parameter | Type     | Description                   |
|-----------|----------|-------------------------------|
| `name`    | `string` | name of the IngressController |

Global path parameters

HTTP method
`DELETE`

Description
delete an IngressController

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
read the specified IngressController

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`IngressController`](ingresscontroller-operator-openshift-io-v1.md#ingresscontroller-operator-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PATCH`

Description
partially update the specified IngressController

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`IngressController`](ingresscontroller-operator-openshift-io-v1.md#ingresscontroller-operator-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PUT`

Description
replace the specified IngressController

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`IngressController`](ingresscontroller-operator-openshift-io-v1.md#ingresscontroller-operator-openshift-io-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`IngressController`](ingresscontroller-operator-openshift-io-v1.md#ingresscontroller-operator-openshift-io-v1) schema |
| 201 - Created | [`IngressController`](ingresscontroller-operator-openshift-io-v1.md#ingresscontroller-operator-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/operator.openshift.io/v1/namespaces/{namespace}/ingresscontrollers/{name}/scale

| Parameter | Type     | Description                   |
|-----------|----------|-------------------------------|
| `name`    | `string` | name of the IngressController |

Global path parameters

HTTP method
`GET`

Description
read scale of the specified IngressController

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Scale`](../autoscale_apis/scale-autoscaling-v1.md#scale-autoscaling-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PATCH`

Description
partially update scale of the specified IngressController

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Scale`](../autoscale_apis/scale-autoscaling-v1.md#scale-autoscaling-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PUT`

Description
replace scale of the specified IngressController

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`Scale`](../autoscale_apis/scale-autoscaling-v1.md#scale-autoscaling-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Scale`](../autoscale_apis/scale-autoscaling-v1.md#scale-autoscaling-v1) schema |
| 201 - Created | [`Scale`](../autoscale_apis/scale-autoscaling-v1.md#scale-autoscaling-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/operator.openshift.io/v1/namespaces/{namespace}/ingresscontrollers/{name}/status

| Parameter | Type     | Description                   |
|-----------|----------|-------------------------------|
| `name`    | `string` | name of the IngressController |

Global path parameters

HTTP method
`GET`

Description
read status of the specified IngressController

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`IngressController`](ingresscontroller-operator-openshift-io-v1.md#ingresscontroller-operator-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PATCH`

Description
partially update status of the specified IngressController

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`IngressController`](ingresscontroller-operator-openshift-io-v1.md#ingresscontroller-operator-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PUT`

Description
replace status of the specified IngressController

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`IngressController`](ingresscontroller-operator-openshift-io-v1.md#ingresscontroller-operator-openshift-io-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`IngressController`](ingresscontroller-operator-openshift-io-v1.md#ingresscontroller-operator-openshift-io-v1) schema |
| 201 - Created | [`IngressController`](ingresscontroller-operator-openshift-io-v1.md#ingresscontroller-operator-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses
