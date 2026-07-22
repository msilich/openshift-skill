<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Description
A route allows developers to expose services through an HTTP(S) aware load balancing and proxy layer via a public DNS entry. The route may further specify TLS options and a certificate, or specify a public CNAME that the router should also accept for HTTP and HTTPS traffic. An administrator typically configures their router to be visible outside the cluster firewall, and may also add additional security, caching, or traffic controls on the service content. Routers usually talk directly to the service endpoints.

Once a route is created, the `host` field may not be changed. Generally, routers use the oldest route with a given host when resolving conflicts.

Routers are subject to additional customization and may support additional controls via the annotations field.

Because administrators may configure multiple routers, the route status field is used to return information to clients about the names and states of the route under each router. If a client chooses a duplicate name, for instance, the route status conditions are used to indicate the route cannot be chosen.

To enable HTTP/2 ALPN on a route it requires a custom (non-wildcard) certificate. This prevents connection coalescing by clients, notably web browsers. We do not support HTTP/2 ALPN on routes that use the default certificate because of the risk of connection re-use/coalescing. Routes that do not have their own custom certificate will not be HTTP/2 ALPN-enabled on either the frontend or the backend.

Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).

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
<td style="text-align: left;"><p><a href="../objects/index.xml#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta_v2"><code>ObjectMeta_v2</code></a></p></td>
<td style="text-align: left;"><p>metadata is the standard object’s metadata. More info: <a href="https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata">https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>spec</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>RouteSpec describes the hostname or path the route exposes, any security information, and one to four backends (services) the route points to. Requests are distributed among the backends depending on the weights assigned to each backend. When using roundrobin scheduling the portion of requests that go to each backend is the backend weight divided by the sum of all of the backend weights. When the backend has more than one endpoint the requests that end up on the backend are roundrobin distributed among the endpoints. Weights are between 0 and 256 with default 100. Weight 0 causes no requests to the backend. If all weights are zero the route will be considered to have no backends and return a standard 503 response.</p>
<p>The <code>tls</code> field is optional and allows specific certificates or behavior for the route. Routers typically configure a default certificate on a wildcard domain to terminate routes without explicit certificates, but custom hostnames usually must choose passthrough (send traffic directly to the backend via the TLS Server-Name- Indication field) or provide a certificate.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>status</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>RouteStatus provides relevant info about the status of a route, including which routers acknowledge it.</p></td>
</tr>
</tbody>
</table>

## .spec

Description
RouteSpec describes the hostname or path the route exposes, any security information, and one to four backends (services) the route points to. Requests are distributed among the backends depending on the weights assigned to each backend. When using roundrobin scheduling the portion of requests that go to each backend is the backend weight divided by the sum of all of the backend weights. When the backend has more than one endpoint the requests that end up on the backend are roundrobin distributed among the endpoints. Weights are between 0 and 256 with default 100. Weight 0 causes no requests to the backend. If all weights are zero the route will be considered to have no backends and return a standard 503 response.

The `tls` field is optional and allows specific certificates or behavior for the route. Routers typically configure a default certificate on a wildcard domain to terminate routes without explicit certificates, but custom hostnames usually must choose passthrough (send traffic directly to the backend via the TLS Server-Name- Indication field) or provide a certificate.

Type
`object`

Required
- `to`

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
<td style="text-align: left;"><p><code>alternateBackends</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>alternateBackends allows up to 3 additional backends to be assigned to the route. Only the Service kind is allowed, and it will be defaulted to Service. Use the weight field in RouteTargetReference object to specify relative preference.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>alternateBackends[]</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>RouteTargetReference specifies the target that resolve into endpoints. Only the 'Service' kind is allowed. Use 'weight' field to emphasize one over others.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>host</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>host is an alias/DNS that points to the service. Optional. If not specified a route name will typically be automatically chosen. Must follow DNS952 subdomain conventions.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>httpHeaders</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>RouteHTTPHeaders defines policy for HTTP headers.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>path</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>path that the router watches for, to route traffic for to the service. Optional</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>port</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>RoutePort defines a port mapping from a router to an endpoint in the service endpoints.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>subdomain</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>subdomain is a DNS subdomain that is requested within the ingress controller’s domain (as a subdomain). If host is set this field is ignored. An ingress controller may choose to ignore this suggested name, in which case the controller will report the assigned name in the status.ingress array or refuse to admit the route. If this value is set and the server does not support this field host will be populated automatically. Otherwise host is left empty. The field may have multiple parts separated by a dot, but not all ingress controllers may honor the request. This field may not be changed after creation except by a user with the update routes/custom-host permission.</p>
<p>Example: subdomain <code>frontend</code> automatically receives the router subdomain <code>apps.mycluster.com</code> to have a full hostname <code>frontend.apps.mycluster.com</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>tls</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>TLSConfig defines config used to secure a route and provide termination</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>to</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>RouteTargetReference specifies the target that resolve into endpoints. Only the 'Service' kind is allowed. Use 'weight' field to emphasize one over others.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>wildcardPolicy</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Wildcard policy if any for the route. Currently only 'Subdomain' or 'None' is allowed.</p></td>
</tr>
</tbody>
</table>

## .spec.alternateBackends

Description
alternateBackends allows up to 3 additional backends to be assigned to the route. Only the Service kind is allowed, and it will be defaulted to Service. Use the weight field in RouteTargetReference object to specify relative preference.

Type
`array`

## .spec.alternateBackends\[\]

Description
RouteTargetReference specifies the target that resolve into endpoints. Only the 'Service' kind is allowed. Use 'weight' field to emphasize one over others.

Type
`object`

Required
- `kind`

- `name`

| Property | Type | Description |
|----|----|----|
| `kind` | `string` | The kind of target that the route is referring to. Currently, only 'Service' is allowed |
| `name` | `string` | name of the service/target that is being referred to. e.g. name of the service |
| `weight` | `integer` | weight as an integer between 0 and 256, default 100, that specifies the target’s relative weight against other target reference objects. 0 suppresses requests to this backend. |

## .spec.httpHeaders

Description
RouteHTTPHeaders defines policy for HTTP headers.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `actions` | `object` | RouteHTTPHeaderActions defines configuration for actions on HTTP request and response headers. |

## .spec.httpHeaders.actions

Description
RouteHTTPHeaderActions defines configuration for actions on HTTP request and response headers.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `request` | `array` | request is a list of HTTP request headers to modify. Currently, actions may define to either `Set` or `Delete` headers values. Actions defined here will modify the request headers of all requests made through a route. These actions are applied to a specific Route defined within a cluster i.e. connections made through a route. Currently, actions may define to either `Set` or `Delete` headers values. Route actions will be executed after IngressController actions for request headers. Actions are applied in sequence as defined in this list. A maximum of 20 request header actions may be configured. You can use this field to specify HTTP request headers that should be set or deleted when forwarding connections from the client to your application. Sample fetchers allowed are "req.hdr" and "ssl_c_der". Converters allowed are "lower" and "base64". Example header values: "%\[req.hdr(X-target),lower\]", "%{+Q}\[ssl_c_der,base64\]". Any request header configuration applied directly via a Route resource using this API will override header configuration for a header of the same name applied via spec.httpHeaders.actions on the IngressController or route annotation. Note: This field cannot be used if your route uses TLS passthrough. |
| `request[]` | `object` | RouteHTTPHeader specifies configuration for setting or deleting an HTTP header. |
| `response` | `array` | response is a list of HTTP response headers to modify. Currently, actions may define to either `Set` or `Delete` headers values. Actions defined here will modify the response headers of all requests made through a route. These actions are applied to a specific Route defined within a cluster i.e. connections made through a route. Route actions will be executed before IngressController actions for response headers. Actions are applied in sequence as defined in this list. A maximum of 20 response header actions may be configured. You can use this field to specify HTTP response headers that should be set or deleted when forwarding responses from your application to the client. Sample fetchers allowed are "res.hdr" and "ssl_c_der". Converters allowed are "lower" and "base64". Example header values: "%\[res.hdr(X-target),lower\]", "%{+Q}\[ssl_c_der,base64\]". Note: This field cannot be used if your route uses TLS passthrough. |
| `response[]` | `object` | RouteHTTPHeader specifies configuration for setting or deleting an HTTP header. |

## .spec.httpHeaders.actions.request

Description
request is a list of HTTP request headers to modify. Currently, actions may define to either `Set` or `Delete` headers values. Actions defined here will modify the request headers of all requests made through a route. These actions are applied to a specific Route defined within a cluster i.e. connections made through a route. Currently, actions may define to either `Set` or `Delete` headers values. Route actions will be executed after IngressController actions for request headers. Actions are applied in sequence as defined in this list. A maximum of 20 request header actions may be configured. You can use this field to specify HTTP request headers that should be set or deleted when forwarding connections from the client to your application. Sample fetchers allowed are "req.hdr" and "ssl_c_der". Converters allowed are "lower" and "base64". Example header values: "%\[req.hdr(X-target),lower\]", "%{+Q}\[ssl_c_der,base64\]". Any request header configuration applied directly via a Route resource using this API will override header configuration for a header of the same name applied via spec.httpHeaders.actions on the IngressController or route annotation. Note: This field cannot be used if your route uses TLS passthrough.

Type
`array`

## .spec.httpHeaders.actions.request\[\]

Description
RouteHTTPHeader specifies configuration for setting or deleting an HTTP header.

Type
`object`

Required
- `name`

- `action`

| Property | Type | Description |
|----|----|----|
| `action` | `object` | RouteHTTPHeaderActionUnion specifies an action to take on an HTTP header. |
| `name` | `string` | name specifies the name of a header on which to perform an action. Its value must be a valid HTTP header name as defined in RFC 2616 section 4.2. The name must consist only of alphanumeric and the following special characters, "-!#\$%&'\*+.^\_\`". The following header names are reserved and may not be modified via this API: Strict-Transport-Security, Proxy, Cookie, Set-Cookie. It must be no more than 255 characters in length. Header name must be unique. |

## .spec.httpHeaders.actions.request\[\].action

Description
RouteHTTPHeaderActionUnion specifies an action to take on an HTTP header.

Type
`object`

Required
- `type`

| Property | Type | Description |
|----|----|----|
| `set` | `object` | RouteSetHTTPHeader specifies what value needs to be set on an HTTP header. |
| `type` | `string` | type defines the type of the action to be applied on the header. Possible values are Set or Delete. Set allows you to set HTTP request and response headers. Delete allows you to delete HTTP request and response headers. |

## .spec.httpHeaders.actions.request\[\].action.set

Description
RouteSetHTTPHeader specifies what value needs to be set on an HTTP header.

Type
`object`

Required
- `value`

| Property | Type | Description |
|----|----|----|
| `value` | `string` | value specifies a header value. Dynamic values can be added. The value will be interpreted as an HAProxy format string as defined in <http://cbonte.github.io/haproxy-dconv/2.6/configuration.html#8.2.6> and may use HAProxy’s %\[\] syntax and otherwise must be a valid HTTP header value as defined in <https://datatracker.ietf.org/doc/html/rfc7230#section-3.2>. The value of this field must be no more than 16384 characters in length. Note that the total size of all net added headers **after** interpolating dynamic values must not exceed the value of spec.tuningOptions.headerBufferMaxRewriteBytes on the IngressController. |

## .spec.httpHeaders.actions.response

Description
response is a list of HTTP response headers to modify. Currently, actions may define to either `Set` or `Delete` headers values. Actions defined here will modify the response headers of all requests made through a route. These actions are applied to a specific Route defined within a cluster i.e. connections made through a route. Route actions will be executed before IngressController actions for response headers. Actions are applied in sequence as defined in this list. A maximum of 20 response header actions may be configured. You can use this field to specify HTTP response headers that should be set or deleted when forwarding responses from your application to the client. Sample fetchers allowed are "res.hdr" and "ssl_c_der". Converters allowed are "lower" and "base64". Example header values: "%\[res.hdr(X-target),lower\]", "%{+Q}\[ssl_c_der,base64\]". Note: This field cannot be used if your route uses TLS passthrough.

Type
`array`

## .spec.httpHeaders.actions.response\[\]

Description
RouteHTTPHeader specifies configuration for setting or deleting an HTTP header.

Type
`object`

Required
- `name`

- `action`

| Property | Type | Description |
|----|----|----|
| `action` | `object` | RouteHTTPHeaderActionUnion specifies an action to take on an HTTP header. |
| `name` | `string` | name specifies the name of a header on which to perform an action. Its value must be a valid HTTP header name as defined in RFC 2616 section 4.2. The name must consist only of alphanumeric and the following special characters, "-!#\$%&'\*+.^\_\`". The following header names are reserved and may not be modified via this API: Strict-Transport-Security, Proxy, Cookie, Set-Cookie. It must be no more than 255 characters in length. Header name must be unique. |

## .spec.httpHeaders.actions.response\[\].action

Description
RouteHTTPHeaderActionUnion specifies an action to take on an HTTP header.

Type
`object`

Required
- `type`

| Property | Type | Description |
|----|----|----|
| `set` | `object` | RouteSetHTTPHeader specifies what value needs to be set on an HTTP header. |
| `type` | `string` | type defines the type of the action to be applied on the header. Possible values are Set or Delete. Set allows you to set HTTP request and response headers. Delete allows you to delete HTTP request and response headers. |

## .spec.httpHeaders.actions.response\[\].action.set

Description
RouteSetHTTPHeader specifies what value needs to be set on an HTTP header.

Type
`object`

Required
- `value`

| Property | Type | Description |
|----|----|----|
| `value` | `string` | value specifies a header value. Dynamic values can be added. The value will be interpreted as an HAProxy format string as defined in <http://cbonte.github.io/haproxy-dconv/2.6/configuration.html#8.2.6> and may use HAProxy’s %\[\] syntax and otherwise must be a valid HTTP header value as defined in <https://datatracker.ietf.org/doc/html/rfc7230#section-3.2>. The value of this field must be no more than 16384 characters in length. Note that the total size of all net added headers **after** interpolating dynamic values must not exceed the value of spec.tuningOptions.headerBufferMaxRewriteBytes on the IngressController. |

## .spec.port

Description
RoutePort defines a port mapping from a router to an endpoint in the service endpoints.

Type
`object`

Required
- `targetPort`

| Property | Type | Description |
|----|----|----|
| `targetPort` | [`IntOrString`](../objects/index.md#io-k8s-apimachinery-pkg-util-intstr-IntOrString) | The target port on pods selected by the service this route points to. If this is a string, it will be looked up as a named port in the target endpoints port list. Required |

## .spec.tls

Description
TLSConfig defines config used to secure a route and provide termination

Type
`object`

Required
- `termination`

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
<td style="text-align: left;"><p><code>caCertificate</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>caCertificate provides the cert authority certificate contents</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>certificate</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>certificate provides certificate contents. This should be a single serving certificate, not a certificate chain. Do not include a CA certificate.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>destinationCACertificate</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>destinationCACertificate provides the contents of the ca certificate of the final destination. When using reencrypt termination this file should be provided in order to have routers use it for health checks on the secure connection. If this field is not specified, the router may provide its own destination CA and perform hostname validation using the short service name (service.namespace.svc), which allows infrastructure generated certificates to automatically verify.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>externalCertificate</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>LocalObjectReference contains enough information to let you locate the referenced object inside the same namespace.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>insecureEdgeTerminationPolicy</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>insecureEdgeTerminationPolicy indicates the desired behavior for insecure connections to a route. While each router may make its own decisions on which ports to expose, this is normally port 80.</p>
<p>If a route does not specify insecureEdgeTerminationPolicy, then the default behavior is "None".</p>
<p>* Allow - traffic is sent to the server on the insecure port (edge/reencrypt terminations only).</p>
<p>* None - no traffic is allowed on the insecure port (default).</p>
<p>* Redirect - clients are redirected to the secure port.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>key</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>key provides key file contents</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>termination</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>termination indicates termination type.</p>
<p>* edge - TLS termination is done by the router and http is used to communicate with the backend (default) * passthrough - Traffic is sent straight to the destination without the router providing TLS termination * reencrypt - TLS termination is done by the router and https is used to communicate with the backend</p>
<p>Note: passthrough termination is incompatible with httpHeader actions</p></td>
</tr>
</tbody>
</table>

## .spec.tls.externalCertificate

Description
LocalObjectReference contains enough information to let you locate the referenced object inside the same namespace.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `name` | `string` | name of the referent. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names> |

## .spec.to

Description
RouteTargetReference specifies the target that resolve into endpoints. Only the 'Service' kind is allowed. Use 'weight' field to emphasize one over others.

Type
`object`

Required
- `kind`

- `name`

| Property | Type | Description |
|----|----|----|
| `kind` | `string` | The kind of target that the route is referring to. Currently, only 'Service' is allowed |
| `name` | `string` | name of the service/target that is being referred to. e.g. name of the service |
| `weight` | `integer` | weight as an integer between 0 and 256, default 100, that specifies the target’s relative weight against other target reference objects. 0 suppresses requests to this backend. |

## .status

Description
RouteStatus provides relevant info about the status of a route, including which routers acknowledge it.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `ingress` | `array` | ingress describes the places where the route may be exposed. The list of ingress points may contain duplicate Host or RouterName values. Routes are considered live once they are `Ready` |
| `ingress[]` | `object` | RouteIngress holds information about the places where a route is exposed. |

## .status.ingress

Description
ingress describes the places where the route may be exposed. The list of ingress points may contain duplicate Host or RouterName values. Routes are considered live once they are `Ready`

Type
`array`

## .status.ingress\[\]

Description
RouteIngress holds information about the places where a route is exposed.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `conditions` | `array` | Conditions is the state of the route, may be empty. |
| `conditions[]` | `object` | RouteIngressCondition contains details for the current condition of this route on a particular router. |
| `host` | `string` | Host is the host string under which the route is exposed; this value is required |
| `routerCanonicalHostname` | `string` | CanonicalHostname is the external host name for the router that can be used as a CNAME for the host requested for this route. This value is optional and may not be set in all cases. |
| `routerName` | `string` | Name is a name chosen by the router to identify itself; this value is required |
| `wildcardPolicy` | `string` | Wildcard policy is the wildcard policy that was allowed where this route is exposed. |

## .status.ingress\[\].conditions

Description
Conditions is the state of the route, may be empty.

Type
`array`

## .status.ingress\[\].conditions\[\]

Description
RouteIngressCondition contains details for the current condition of this route on a particular router.

Type
`object`

Required
- `type`

- `status`

| Property | Type | Description |
|----|----|----|
| `lastTransitionTime` | [`Time`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-Time) | RFC 3339 date and time when this condition last transitioned |
| `message` | `string` | Human readable message indicating details about last transition. |
| `reason` | `string` | (brief) reason for the condition’s last transition, and is usually a machine and human readable constant |
| `status` | `string` | Status is the status of the condition. Can be True, False, Unknown. |
| `type` | `string` | Type is the type of the condition. Currently only Admitted or UnservableInFutureVersions. |

# API endpoints

The following API endpoints are available:

- `/apis/route.openshift.io/v1/routes`

  - `GET`: list or watch objects of kind Route

- `/apis/route.openshift.io/v1/watch/routes`

  - `GET`: watch individual changes to a list of Route. deprecated: use the 'watch' parameter with a list operation instead.

- `/apis/route.openshift.io/v1/namespaces/{namespace}/routes`

  - `DELETE`: delete collection of Route

  - `GET`: list or watch objects of kind Route

  - `POST`: create a Route

- `/apis/route.openshift.io/v1/watch/namespaces/{namespace}/routes`

  - `GET`: watch individual changes to a list of Route. deprecated: use the 'watch' parameter with a list operation instead.

- `/apis/route.openshift.io/v1/namespaces/{namespace}/routes/{name}`

  - `DELETE`: delete a Route

  - `GET`: read the specified Route

  - `PATCH`: partially update the specified Route

  - `PUT`: replace the specified Route

- `/apis/route.openshift.io/v1/watch/namespaces/{namespace}/routes/{name}`

  - `GET`: watch changes to an object of kind Route. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.

- `/apis/route.openshift.io/v1/namespaces/{namespace}/routes/{name}/status`

  - `GET`: read status of the specified Route

  - `PATCH`: partially update status of the specified Route

  - `PUT`: replace status of the specified Route

## /apis/route.openshift.io/v1/routes

HTTP method
`GET`

Description
list or watch objects of kind Route

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`RouteList`](../objects/index.md#com-github-openshift-api-route-v1-RouteList) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/route.openshift.io/v1/watch/routes

HTTP method
`GET`

Description
watch individual changes to a list of Route. deprecated: use the 'watch' parameter with a list operation instead.

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`WatchEvent`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/route.openshift.io/v1/namespaces/{namespace}/routes

HTTP method
`DELETE`

Description
delete collection of Route

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |

Query parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Status_v7`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-Status_v7) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`GET`

Description
list or watch objects of kind Route

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`RouteList`](../objects/index.md#com-github-openshift-api-route-v1-RouteList) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`POST`

Description
create a Route

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`Route`](route-route-openshift-io-v1.md#route-route-openshift-io-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Route`](route-route-openshift-io-v1.md#route-route-openshift-io-v1) schema |
| 201 - Created | [`Route`](route-route-openshift-io-v1.md#route-route-openshift-io-v1) schema |
| 202 - Accepted | [`Route`](route-route-openshift-io-v1.md#route-route-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/route.openshift.io/v1/watch/namespaces/{namespace}/routes

HTTP method
`GET`

Description
watch individual changes to a list of Route. deprecated: use the 'watch' parameter with a list operation instead.

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`WatchEvent`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/route.openshift.io/v1/namespaces/{namespace}/routes/{name}

| Parameter | Type     | Description       |
|-----------|----------|-------------------|
| `name`    | `string` | name of the Route |

Global path parameters

HTTP method
`DELETE`

Description
delete a Route

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |

Query parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Status_v7`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-Status_v7) schema |
| 202 - Accepted | [`Status_v7`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-Status_v7) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`GET`

Description
read the specified Route

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Route`](route-route-openshift-io-v1.md#route-route-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PATCH`

Description
partially update the specified Route

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Route`](route-route-openshift-io-v1.md#route-route-openshift-io-v1) schema |
| 201 - Created | [`Route`](route-route-openshift-io-v1.md#route-route-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PUT`

Description
replace the specified Route

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`Route`](route-route-openshift-io-v1.md#route-route-openshift-io-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Route`](route-route-openshift-io-v1.md#route-route-openshift-io-v1) schema |
| 201 - Created | [`Route`](route-route-openshift-io-v1.md#route-route-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/route.openshift.io/v1/watch/namespaces/{namespace}/routes/{name}

| Parameter | Type     | Description       |
|-----------|----------|-------------------|
| `name`    | `string` | name of the Route |

Global path parameters

HTTP method
`GET`

Description
watch changes to an object of kind Route. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`WatchEvent`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/route.openshift.io/v1/namespaces/{namespace}/routes/{name}/status

| Parameter | Type     | Description       |
|-----------|----------|-------------------|
| `name`    | `string` | name of the Route |

Global path parameters

HTTP method
`GET`

Description
read status of the specified Route

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Route`](route-route-openshift-io-v1.md#route-route-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PATCH`

Description
partially update status of the specified Route

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Route`](route-route-openshift-io-v1.md#route-route-openshift-io-v1) schema |
| 201 - Created | [`Route`](route-route-openshift-io-v1.md#route-route-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PUT`

Description
replace status of the specified Route

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`Route`](route-route-openshift-io-v1.md#route-route-openshift-io-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Route`](route-route-openshift-io-v1.md#route-route-openshift-io-v1) schema |
| 201 - Created | [`Route`](route-route-openshift-io-v1.md#route-route-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses
