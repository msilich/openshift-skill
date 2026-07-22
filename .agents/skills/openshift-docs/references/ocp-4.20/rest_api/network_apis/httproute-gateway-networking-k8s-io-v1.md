<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Description
HTTPRoute provides a way to route HTTP requests. This includes the capability to match requests by hostname, path, header, or query param. Filters can be used to specify additional processing steps. Backends specify where matching requests should be routed.

Type
`object`

Required
- `spec`

# Specification

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ObjectMeta`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) | Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |
| `spec` | `object` | Spec defines the desired state of HTTPRoute. |
| `status` | `object` | Status defines the current state of HTTPRoute. |

## .spec

Description
Spec defines the desired state of HTTPRoute.

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
<td style="text-align: left;"><p><code>hostnames</code></p></td>
<td style="text-align: left;"><p><code>array (string)</code></p></td>
<td style="text-align: left;"><p>Hostnames defines a set of hostnames that should match against the HTTP Host header to select a HTTPRoute used to process the request. Implementations MUST ignore any port value specified in the HTTP Host header while performing a match and (absent of any applicable header modification configuration) MUST forward this header unmodified to the backend.</p>
<p>Valid values for Hostnames are determined by RFC 1123 definition of a hostname with 2 notable exceptions:</p>
<p>1. IPs are not allowed. 2. A hostname may be prefixed with a wildcard label (<code>*.</code>). The wildcard label must appear by itself as the first label.</p>
<p>If a hostname is specified by both the Listener and HTTPRoute, there must be at least one intersecting hostname for the HTTPRoute to be attached to the Listener. For example:</p>
<p>* A Listener with <code>test.example.com</code> as the hostname matches HTTPRoutes that have either not specified any hostnames, or have specified at least one of <code>test.example.com</code> or <code>*.example.com</code>. * A Listener with <code>*.example.com</code> as the hostname matches HTTPRoutes that have either not specified any hostnames or have specified at least one hostname that matches the Listener hostname. For example, <code>\*.example.com</code>, <code>test.example.com</code>, and <code>foo.test.example.com</code> would all match. On the other hand, <code>example.com</code> and <code>test.example.net</code> would not match.</p>
<p>Hostnames that are prefixed with a wildcard label (<code>*.</code>) are interpreted as a suffix match. That means that a match for <code>*.example.com</code> would match both <code>test.example.com</code>, and <code>foo.test.example.com</code>, but not <code>example.com</code>.</p>
<p>If both the Listener and HTTPRoute have specified hostnames, any HTTPRoute hostnames that do not match the Listener hostname MUST be ignored. For example, if a Listener specified <code>*.example.com</code>, and the HTTPRoute specified <code>test.example.com</code> and <code>test.example.net</code>, <code>test.example.net</code> must not be considered for a match.</p>
<p>If both the Listener and HTTPRoute have specified hostnames, and none match with the criteria above, then the HTTPRoute is not accepted. The implementation must raise an 'Accepted' Condition with a status of <code>False</code> in the corresponding RouteParentStatus.</p>
<p>In the event that multiple HTTPRoutes specify intersecting hostnames (e.g. overlapping wildcard matching and exact matching hostnames), precedence must be given to rules from the HTTPRoute with the largest number of:</p>
<p>* Characters in a matching non-wildcard hostname. * Characters in a matching hostname.</p>
<p>If ties exist across multiple Routes, the matching precedence rules for HTTPRouteMatches takes over.</p>
<p>Support: Core</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>parentRefs</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>ParentRefs references the resources (usually Gateways) that a Route wants to be attached to. Note that the referenced parent resource needs to allow this for the attachment to be complete. For Gateways, that means the Gateway needs to allow attachment from Routes of this kind and namespace. For Services, that means the Service must either be in the same namespace for a "producer" route, or the mesh implementation must support and allow "consumer" routes for the referenced Service. ReferenceGrant is not applicable for governing ParentRefs to Services - it is not possible to create a "producer" route for a Service in a different namespace from the Route.</p>
<p>There are two kinds of parent resources with "Core" support:</p>
<p>* Gateway (Gateway conformance profile) * Service (Mesh conformance profile, ClusterIP Services only)</p>
<p>This API may be extended in the future to support additional kinds of parent resources.</p>
<p>ParentRefs must be <em>distinct</em>. This means either that:</p>
<p>* They select different objects. If this is the case, then parentRef entries are distinct. In terms of fields, this means that the multi-part key defined by <code>group</code>, <code>kind</code>, <code>namespace</code>, and <code>name</code> must be unique across all parentRef entries in the Route. * They do not select different objects, but for each optional field used, each ParentRef that selects the same object must set the same set of optional fields to different values. If one ParentRef sets a combination of optional fields, all must set the same combination.</p>
<p>Some examples:</p>
<p>* If one ParentRef sets <code>sectionName</code>, all ParentRefs referencing the same object must also set <code>sectionName</code>. * If one ParentRef sets <code>port</code>, all ParentRefs referencing the same object must also set <code>port</code>. * If one ParentRef sets <code>sectionName</code> and <code>port</code>, all ParentRefs referencing the same object must also set <code>sectionName</code> and <code>port</code>.</p>
<p>It is possible to separately reference multiple distinct objects that may be collapsed by an implementation. For example, some implementations may choose to merge compatible Gateway Listeners together. If that is the case, the list of routes attached to those resources should also be merged.</p>
<p>Note that for ParentRefs that cross namespace boundaries, there are specific rules. Cross-namespace references are only valid if they are explicitly allowed by something in the namespace they are referring to. For example, Gateway has the AllowedRoutes field, and ReferenceGrant provides a generic way to enable other kinds of cross-namespace reference.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>parentRefs[]</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>ParentReference identifies an API object (usually a Gateway) that can be considered a parent of this resource (usually a route). There are two kinds of parent resources with "Core" support:</p>
<p>* Gateway (Gateway conformance profile) * Service (Mesh conformance profile, ClusterIP Services only)</p>
<p>This API may be extended in the future to support additional kinds of parent resources.</p>
<p>The API object must be valid in the cluster; the Group and Kind must be registered in the cluster for this reference to be valid.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>rules</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>Rules are a list of HTTP matchers, filters and actions.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>rules[]</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>HTTPRouteRule defines semantics for matching an HTTP request based on conditions (matches), processing it (filters), and forwarding the request to an API object (backendRefs).</p></td>
</tr>
</tbody>
</table>

## .spec.parentRefs

Description
ParentRefs references the resources (usually Gateways) that a Route wants to be attached to. Note that the referenced parent resource needs to allow this for the attachment to be complete. For Gateways, that means the Gateway needs to allow attachment from Routes of this kind and namespace. For Services, that means the Service must either be in the same namespace for a "producer" route, or the mesh implementation must support and allow "consumer" routes for the referenced Service. ReferenceGrant is not applicable for governing ParentRefs to Services - it is not possible to create a "producer" route for a Service in a different namespace from the Route.

There are two kinds of parent resources with "Core" support:

- Gateway (Gateway conformance profile)

- Service (Mesh conformance profile, ClusterIP Services only)

This API may be extended in the future to support additional kinds of parent resources.

ParentRefs must be *distinct*. This means either that:

- They select different objects. If this is the case, then parentRef entries are distinct. In terms of fields, this means that the multi-part key defined by `group`, `kind`, `namespace`, and `name` must be unique across all parentRef entries in the Route.

- They do not select different objects, but for each optional field used, each ParentRef that selects the same object must set the same set of optional fields to different values. If one ParentRef sets a combination of optional fields, all must set the same combination.

Some examples:

- If one ParentRef sets `sectionName`, all ParentRefs referencing the same object must also set `sectionName`.

- If one ParentRef sets `port`, all ParentRefs referencing the same object must also set `port`.

- If one ParentRef sets `sectionName` and `port`, all ParentRefs referencing the same object must also set `sectionName` and `port`.

It is possible to separately reference multiple distinct objects that may be collapsed by an implementation. For example, some implementations may choose to merge compatible Gateway Listeners together. If that is the case, the list of routes attached to those resources should also be merged.

Note that for ParentRefs that cross namespace boundaries, there are specific rules. Cross-namespace references are only valid if they are explicitly allowed by something in the namespace they are referring to. For example, Gateway has the AllowedRoutes field, and ReferenceGrant provides a generic way to enable other kinds of cross-namespace reference.

Type
`array`

## .spec.parentRefs\[\]

Description
ParentReference identifies an API object (usually a Gateway) that can be considered a parent of this resource (usually a route). There are two kinds of parent resources with "Core" support:

- Gateway (Gateway conformance profile)

- Service (Mesh conformance profile, ClusterIP Services only)

This API may be extended in the future to support additional kinds of parent resources.

The API object must be valid in the cluster; the Group and Kind must be registered in the cluster for this reference to be valid.

Type
`object`

Required
- `name`

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
<td style="text-align: left;"><p><code>group</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Group is the group of the referent. When unspecified, "gateway.networking.k8s.io" is inferred. To set the core API group (such as for a "Service" kind referent), Group must be explicitly set to "" (empty string).</p>
<p>Support: Core</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>kind</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Kind is kind of the referent.</p>
<p>There are two kinds of parent resources with "Core" support:</p>
<p>* Gateway (Gateway conformance profile) * Service (Mesh conformance profile, ClusterIP Services only)</p>
<p>Support for other resources is Implementation-Specific.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>name</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Name is the name of the referent.</p>
<p>Support: Core</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>namespace</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Namespace is the namespace of the referent. When unspecified, this refers to the local namespace of the Route.</p>
<p>Note that there are specific rules for ParentRefs which cross namespace boundaries. Cross-namespace references are only valid if they are explicitly allowed by something in the namespace they are referring to. For example: Gateway has the AllowedRoutes field, and ReferenceGrant provides a generic way to enable any other kind of cross-namespace reference.</p>
<p>Support: Core</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>port</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p>Port is the network port this Route targets. It can be interpreted differently based on the type of parent resource.</p>
<p>When the parent resource is a Gateway, this targets all listeners listening on the specified port that also support this kind of Route(and select this Route). It’s not recommended to set <code>Port</code> unless the networking behaviors specified in a Route must apply to a specific port as opposed to a listener(s) whose port(s) may be changed. When both Port and SectionName are specified, the name and port of the selected listener must match both specified values.</p>
<p>Implementations MAY choose to support other parent resources. Implementations supporting other types of parent resources MUST clearly document how/if Port is interpreted.</p>
<p>For the purpose of status, an attachment is considered successful as long as the parent resource accepts it partially. For example, Gateway listeners can restrict which Routes can attach to them by Route kind, namespace, or hostname. If 1 of 2 Gateway listeners accept attachment from the referencing Route, the Route MUST be considered successfully attached. If no Gateway listeners accept attachment from this Route, the Route MUST be considered detached from the Gateway.</p>
<p>Support: Extended</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>sectionName</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>SectionName is the name of a section within the target resource. In the following resources, SectionName is interpreted as the following:</p>
<p>* Gateway: Listener name. When both Port (experimental) and SectionName are specified, the name and port of the selected listener must match both specified values. * Service: Port name. When both Port (experimental) and SectionName are specified, the name and port of the selected listener must match both specified values.</p>
<p>Implementations MAY choose to support attaching Routes to other resources. If that is the case, they MUST clearly document how SectionName is interpreted.</p>
<p>When unspecified (empty string), this will reference the entire resource. For the purpose of status, an attachment is considered successful if at least one section in the parent resource accepts it. For example, Gateway listeners can restrict which Routes can attach to them by Route kind, namespace, or hostname. If 1 of 2 Gateway listeners accept attachment from the referencing Route, the Route MUST be considered successfully attached. If no Gateway listeners accept attachment from this Route, the Route MUST be considered detached from the Gateway.</p>
<p>Support: Core</p></td>
</tr>
</tbody>
</table>

## .spec.rules

Description
Rules are a list of HTTP matchers, filters and actions.

Type
`array`

## .spec.rules\[\]

Description
HTTPRouteRule defines semantics for matching an HTTP request based on conditions (matches), processing it (filters), and forwarding the request to an API object (backendRefs).

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
<td style="text-align: left;"><p><code>backendRefs</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>BackendRefs defines the backend(s) where matching requests should be sent.</p>
<p>Failure behavior here depends on how many BackendRefs are specified and how many are invalid.</p>
<p>If <strong>all</strong> entries in BackendRefs are invalid, and there are also no filters specified in this route rule, <strong>all</strong> traffic which matches this rule MUST receive a 500 status code.</p>
<p>See the HTTPBackendRef definition for the rules about what makes a single HTTPBackendRef invalid.</p>
<p>When a HTTPBackendRef is invalid, 500 status codes MUST be returned for requests that would have otherwise been routed to an invalid backend. If multiple backends are specified, and some are invalid, the proportion of requests that would otherwise have been routed to an invalid backend MUST receive a 500 status code.</p>
<p>For example, if two backends are specified with equal weights, and one is invalid, 50 percent of traffic must receive a 500. Implementations may choose how that 50 percent is determined.</p>
<p>When a HTTPBackendRef refers to a Service that has no ready endpoints, implementations SHOULD return a 503 for requests to that backend instead. If an implementation chooses to do this, all of the above rules for 500 responses MUST also apply for responses that return a 503.</p>
<p>Support: Core for Kubernetes Service</p>
<p>Support: Extended for Kubernetes ServiceImport</p>
<p>Support: Implementation-specific for any other resource</p>
<p>Support for weight: Core</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>backendRefs[]</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>HTTPBackendRef defines how a HTTPRoute forwards a HTTP request.</p>
<p>Note that when a namespace different than the local namespace is specified, a ReferenceGrant object is required in the referent namespace to allow that namespace’s owner to accept the reference. See the ReferenceGrant documentation for details.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>filters</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>Filters define the filters that are applied to requests that match this rule.</p>
<p>Wherever possible, implementations SHOULD implement filters in the order they are specified.</p>
<p>Implementations MAY choose to implement this ordering strictly, rejecting any combination or order of filters that cannot be supported. If implementations choose a strict interpretation of filter ordering, they MUST clearly document that behavior.</p>
<p>To reject an invalid combination or order of filters, implementations SHOULD consider the Route Rules with this configuration invalid. If all Route Rules in a Route are invalid, the entire Route would be considered invalid. If only a portion of Route Rules are invalid, implementations MUST set the "PartiallyInvalid" condition for the Route.</p>
<p>Conformance-levels at this level are defined based on the type of filter:</p>
<p>- ALL core filters MUST be supported by all implementations. - Implementers are encouraged to support extended filters. - Implementation-specific custom filters have no API guarantees across implementations.</p>
<p>Specifying the same filter multiple times is not supported unless explicitly indicated in the filter.</p>
<p>All filters are expected to be compatible with each other except for the URLRewrite and RequestRedirect filters, which may not be combined. If an implementation cannot support other combinations of filters, they must clearly document that limitation. In cases where incompatible or unsupported filters are specified and cause the <code>Accepted</code> condition to be set to status <code>False</code>, implementations may use the <code>IncompatibleFilters</code> reason to specify this configuration error.</p>
<p>Support: Core</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>filters[]</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>HTTPRouteFilter defines processing steps that must be completed during the request or response lifecycle. HTTPRouteFilters are meant as an extension point to express processing that may be done in Gateway implementations. Some examples include request or response modification, implementing authentication strategies, rate-limiting, and traffic shaping. API guarantee/conformance is defined based on the type of the filter.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>matches</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>Matches define conditions used for matching the rule against incoming HTTP requests. Each match is independent, i.e. this rule will be matched if <strong>any</strong> one of the matches is satisfied.</p>
<p>For example, take the following matches configuration:</p>
<p>matches: - path: value: "/foo" headers: - name: "version" value: "v2" - path: value: "/v2/foo"</p>
<p>For a request to match against this rule, a request must satisfy EITHER of the two conditions:</p>
<p>- path prefixed with <code>/foo</code> AND contains the header <code>version: v2</code> - path prefix of <code>/v2/foo</code></p>
<p>See the documentation for HTTPRouteMatch on how to specify multiple match conditions that should be ANDed together.</p>
<p>If no matches are specified, the default is a prefix path match on "/", which has the effect of matching every HTTP request.</p>
<p>Proxy or Load Balancer routing configuration generated from HTTPRoutes MUST prioritize matches based on the following criteria, continuing on ties. Across all rules specified on applicable Routes, precedence must be given to the match having:</p>
<p>* "Exact" path match. * "Prefix" path match with largest number of characters. * Method match. * Largest number of header matches. * Largest number of query param matches.</p>
<p>Note: The precedence of RegularExpression path matches are implementation-specific.</p>
<p>If ties still exist across multiple Routes, matching precedence MUST be determined in order of the following criteria, continuing on ties:</p>
<p>* The oldest Route based on creation timestamp. * The Route appearing first in alphabetical order by "{namespace}/{name}".</p>
<p>If ties still exist within an HTTPRoute, matching precedence MUST be granted to the FIRST matching rule (in list order) with a match meeting the above criteria.</p>
<p>When no rules matching a request have been successfully attached to the parent a request is coming from, a HTTP 404 status code MUST be returned.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>matches[]</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>HTTPRouteMatch defines the predicate used to match requests to a given action. Multiple match types are ANDed together, i.e. the match will evaluate to true only if all conditions are satisfied.</p>
<p>For example, the match below will match a HTTP request only if its path starts with <code>/foo</code> AND it contains the <code>version: v1</code> header:</p>
<p>match:</p>
<p>path: value: "/foo" headers: - name: "version" value "v1"</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>timeouts</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>Timeouts defines the timeouts that can be configured for an HTTP request.</p>
<p>Support: Extended</p></td>
</tr>
</tbody>
</table>

## .spec.rules\[\].backendRefs

Description
BackendRefs defines the backend(s) where matching requests should be sent.

Failure behavior here depends on how many BackendRefs are specified and how many are invalid.

If **all** entries in BackendRefs are invalid, and there are also no filters specified in this route rule, **all** traffic which matches this rule MUST receive a 500 status code.

See the HTTPBackendRef definition for the rules about what makes a single HTTPBackendRef invalid.

When a HTTPBackendRef is invalid, 500 status codes MUST be returned for requests that would have otherwise been routed to an invalid backend. If multiple backends are specified, and some are invalid, the proportion of requests that would otherwise have been routed to an invalid backend MUST receive a 500 status code.

For example, if two backends are specified with equal weights, and one is invalid, 50 percent of traffic must receive a 500. Implementations may choose how that 50 percent is determined.

When a HTTPBackendRef refers to a Service that has no ready endpoints, implementations SHOULD return a 503 for requests to that backend instead. If an implementation chooses to do this, all of the above rules for 500 responses MUST also apply for responses that return a 503.

Support: Core for Kubernetes Service

Support: Extended for Kubernetes ServiceImport

Support: Implementation-specific for any other resource

Support for weight: Core

Type
`array`

## .spec.rules\[\].backendRefs\[\]

Description
HTTPBackendRef defines how a HTTPRoute forwards a HTTP request.

Note that when a namespace different than the local namespace is specified, a ReferenceGrant object is required in the referent namespace to allow that namespace’s owner to accept the reference. See the ReferenceGrant documentation for details.

Type
`object`

Required
- `name`

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
<td style="text-align: left;"><p><code>filters</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>Filters defined at this level should be executed if and only if the request is being forwarded to the backend defined here.</p>
<p>Support: Implementation-specific (For broader support of filters, use the Filters field in HTTPRouteRule.)</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>filters[]</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>HTTPRouteFilter defines processing steps that must be completed during the request or response lifecycle. HTTPRouteFilters are meant as an extension point to express processing that may be done in Gateway implementations. Some examples include request or response modification, implementing authentication strategies, rate-limiting, and traffic shaping. API guarantee/conformance is defined based on the type of the filter.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>group</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Group is the group of the referent. For example, "gateway.networking.k8s.io". When unspecified or empty string, core API group is inferred.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>kind</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Kind is the Kubernetes resource kind of the referent. For example "Service".</p>
<p>Defaults to "Service" when not specified.</p>
<p>ExternalName services can refer to CNAME DNS records that may live outside of the cluster and as such are difficult to reason about in terms of conformance. They also may not be safe to forward to (see CVE-2021-25740 for more information). Implementations SHOULD NOT support ExternalName Services.</p>
<p>Support: Core (Services with a type other than ExternalName)</p>
<p>Support: Implementation-specific (Services with type ExternalName)</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>name</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Name is the name of the referent.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>namespace</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Namespace is the namespace of the backend. When unspecified, the local namespace is inferred.</p>
<p>Note that when a namespace different than the local namespace is specified, a ReferenceGrant object is required in the referent namespace to allow that namespace’s owner to accept the reference. See the ReferenceGrant documentation for details.</p>
<p>Support: Core</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>port</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p>Port specifies the destination port number to use for this resource. Port is required when the referent is a Kubernetes Service. In this case, the port number is the service port number, not the target port. For other resources, destination port might be derived from the referent resource or this field.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>weight</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p>Weight specifies the proportion of requests forwarded to the referenced backend. This is computed as weight/(sum of all weights in this BackendRefs list). For non-zero values, there may be some epsilon from the exact proportion defined here depending on the precision an implementation supports. Weight is not a percentage and the sum of weights does not need to equal 100.</p>
<p>If only one backend is specified and it has a weight greater than 0, 100% of the traffic is forwarded to that backend. If weight is set to 0, no traffic should be forwarded for this entry. If unspecified, weight defaults to 1.</p>
<p>Support for this field varies based on the context where used.</p></td>
</tr>
</tbody>
</table>

## .spec.rules\[\].backendRefs\[\].filters

Description
Filters defined at this level should be executed if and only if the request is being forwarded to the backend defined here.

Support: Implementation-specific (For broader support of filters, use the Filters field in HTTPRouteRule.)

Type
`array`

## .spec.rules\[\].backendRefs\[\].filters\[\]

Description
HTTPRouteFilter defines processing steps that must be completed during the request or response lifecycle. HTTPRouteFilters are meant as an extension point to express processing that may be done in Gateway implementations. Some examples include request or response modification, implementing authentication strategies, rate-limiting, and traffic shaping. API guarantee/conformance is defined based on the type of the filter.

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
<td style="text-align: left;"><p><code>extensionRef</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>ExtensionRef is an optional, implementation-specific extension to the "filter" behavior. For example, resource "myroutefilter" in group "networking.example.net"). ExtensionRef MUST NOT be used for core and extended filters.</p>
<p>This filter can be used multiple times within the same rule.</p>
<p>Support: Implementation-specific</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>requestHeaderModifier</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>RequestHeaderModifier defines a schema for a filter that modifies request headers.</p>
<p>Support: Core</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>requestMirror</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>RequestMirror defines a schema for a filter that mirrors requests. Requests are sent to the specified destination, but responses from that destination are ignored.</p>
<p>This filter can be used multiple times within the same rule. Note that not all implementations will be able to support mirroring to multiple backends.</p>
<p>Support: Extended</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>requestRedirect</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>RequestRedirect defines a schema for a filter that responds to the request with an HTTP redirection.</p>
<p>Support: Core</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>responseHeaderModifier</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>ResponseHeaderModifier defines a schema for a filter that modifies response headers.</p>
<p>Support: Extended</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>type</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Type identifies the type of filter to apply. As with other API fields, types are classified into three conformance levels:</p>
<p>- Core: Filter types and their corresponding configuration defined by "Support: Core" in this package, e.g. "RequestHeaderModifier". All implementations must support core filters.</p>
<p>- Extended: Filter types and their corresponding configuration defined by "Support: Extended" in this package, e.g. "RequestMirror". Implementers are encouraged to support extended filters.</p>
<p>- Implementation-specific: Filters that are defined and supported by specific vendors. In the future, filters showing convergence in behavior across multiple implementations will be considered for inclusion in extended or core conformance levels. Filter-specific configuration for such filters is specified using the ExtensionRef field. <code>Type</code> should be set to "ExtensionRef" for custom filters.</p>
<p>Implementers are encouraged to define custom implementation types to extend the core API with implementation-specific behavior.</p>
<p>If a reference to a custom filter type cannot be resolved, the filter MUST NOT be skipped. Instead, requests that would have been processed by that filter MUST receive a HTTP error response.</p>
<p>Note that values may be added to this enum, implementations must ensure that unknown values will not cause a crash.</p>
<p>Unknown values here must result in the implementation setting the Accepted Condition for the Route to <code>status: False</code>, with a Reason of <code>UnsupportedValue</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>urlRewrite</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>URLRewrite defines a schema for a filter that modifies a request during forwarding.</p>
<p>Support: Extended</p></td>
</tr>
</tbody>
</table>

## .spec.rules\[\].backendRefs\[\].filters\[\].extensionRef

Description
ExtensionRef is an optional, implementation-specific extension to the "filter" behavior. For example, resource "myroutefilter" in group "networking.example.net"). ExtensionRef MUST NOT be used for core and extended filters.

This filter can be used multiple times within the same rule.

Support: Implementation-specific

Type
`object`

Required
- `group`

- `kind`

- `name`

| Property | Type | Description |
|----|----|----|
| `group` | `string` | Group is the group of the referent. For example, "gateway.networking.k8s.io". When unspecified or empty string, core API group is inferred. |
| `kind` | `string` | Kind is kind of the referent. For example "HTTPRoute" or "Service". |
| `name` | `string` | Name is the name of the referent. |

## .spec.rules\[\].backendRefs\[\].filters\[\].requestHeaderModifier

Description
RequestHeaderModifier defines a schema for a filter that modifies request headers.

Support: Core

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
<td style="text-align: left;"><p><code>add</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>Add adds the given header(s) (name, value) to the request before the action. It appends to any existing values associated with the header name.</p>
<p>Input: GET /foo HTTP/1.1 my-header: foo</p>
<p>Config: add: - name: "my-header" value: "bar,baz"</p>
<p>Output: GET /foo HTTP/1.1 my-header: foo,bar,baz</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>add[]</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>HTTPHeader represents an HTTP Header name and value as defined by RFC 7230.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>remove</code></p></td>
<td style="text-align: left;"><p><code>array (string)</code></p></td>
<td style="text-align: left;"><p>Remove the given header(s) from the HTTP request before the action. The value of Remove is a list of HTTP header names. Note that the header names are case-insensitive (see <a href="https://datatracker.ietf.org/doc/html/rfc2616#section-4.2">https://datatracker.ietf.org/doc/html/rfc2616#section-4.2</a>).</p>
<p>Input: GET /foo HTTP/1.1 my-header1: foo my-header2: bar my-header3: baz</p>
<p>Config: remove: ["my-header1", "my-header3"]</p>
<p>Output: GET /foo HTTP/1.1 my-header2: bar</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>set</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>Set overwrites the request with the given header (name, value) before the action.</p>
<p>Input: GET /foo HTTP/1.1 my-header: foo</p>
<p>Config: set: - name: "my-header" value: "bar"</p>
<p>Output: GET /foo HTTP/1.1 my-header: bar</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>set[]</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>HTTPHeader represents an HTTP Header name and value as defined by RFC 7230.</p></td>
</tr>
</tbody>
</table>

## .spec.rules\[\].backendRefs\[\].filters\[\].requestHeaderModifier.add

Description
Add adds the given header(s) (name, value) to the request before the action. It appends to any existing values associated with the header name.

Input: GET /foo HTTP/1.1 my-header: foo

Config: add: - name: "my-header" value: "bar,baz"

Output: GET /foo HTTP/1.1 my-header: foo,bar,baz

Type
`array`

## .spec.rules\[\].backendRefs\[\].filters\[\].requestHeaderModifier.add\[\]

Description
HTTPHeader represents an HTTP Header name and value as defined by RFC 7230.

Type
`object`

Required
- `name`

- `value`

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
<td style="text-align: left;"><p><code>name</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Name is the name of the HTTP Header to be matched. Name matching MUST be case-insensitive. (See <a href="https://tools.ietf.org/html/rfc7230#section-3.2">https://tools.ietf.org/html/rfc7230#section-3.2</a>).</p>
<p>If multiple entries specify equivalent header names, the first entry with an equivalent name MUST be considered for a match. Subsequent entries with an equivalent header name MUST be ignored. Due to the case-insensitivity of header names, "foo" and "Foo" are considered equivalent.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>value</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Value is the value of HTTP Header to be matched.</p></td>
</tr>
</tbody>
</table>

## .spec.rules\[\].backendRefs\[\].filters\[\].requestHeaderModifier.set

Description
Set overwrites the request with the given header (name, value) before the action.

Input: GET /foo HTTP/1.1 my-header: foo

Config: set: - name: "my-header" value: "bar"

Output: GET /foo HTTP/1.1 my-header: bar

Type
`array`

## .spec.rules\[\].backendRefs\[\].filters\[\].requestHeaderModifier.set\[\]

Description
HTTPHeader represents an HTTP Header name and value as defined by RFC 7230.

Type
`object`

Required
- `name`

- `value`

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
<td style="text-align: left;"><p><code>name</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Name is the name of the HTTP Header to be matched. Name matching MUST be case-insensitive. (See <a href="https://tools.ietf.org/html/rfc7230#section-3.2">https://tools.ietf.org/html/rfc7230#section-3.2</a>).</p>
<p>If multiple entries specify equivalent header names, the first entry with an equivalent name MUST be considered for a match. Subsequent entries with an equivalent header name MUST be ignored. Due to the case-insensitivity of header names, "foo" and "Foo" are considered equivalent.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>value</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Value is the value of HTTP Header to be matched.</p></td>
</tr>
</tbody>
</table>

## .spec.rules\[\].backendRefs\[\].filters\[\].requestMirror

Description
RequestMirror defines a schema for a filter that mirrors requests. Requests are sent to the specified destination, but responses from that destination are ignored.

This filter can be used multiple times within the same rule. Note that not all implementations will be able to support mirroring to multiple backends.

Support: Extended

Type
`object`

Required
- `backendRef`

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
<td style="text-align: left;"><p><code>backendRef</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>BackendRef references a resource where mirrored requests are sent.</p>
<p>Mirrored requests must be sent only to a single destination endpoint within this BackendRef, irrespective of how many endpoints are present within this BackendRef.</p>
<p>If the referent cannot be found, this BackendRef is invalid and must be dropped from the Gateway. The controller must ensure the "ResolvedRefs" condition on the Route status is set to <code>status: False</code> and not configure this backend in the underlying implementation.</p>
<p>If there is a cross-namespace reference to an <strong>existing</strong> object that is not allowed by a ReferenceGrant, the controller must ensure the "ResolvedRefs" condition on the Route is set to <code>status: False</code>, with the "RefNotPermitted" reason and not configure this backend in the underlying implementation.</p>
<p>In either error case, the Message of the <code>ResolvedRefs</code> Condition should be used to provide more detail about the problem.</p>
<p>Support: Extended for Kubernetes Service</p>
<p>Support: Implementation-specific for any other resource</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>fraction</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>Fraction represents the fraction of requests that should be mirrored to BackendRef.</p>
<p>Only one of Fraction or Percent may be specified. If neither field is specified, 100% of requests will be mirrored.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>percent</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p>Percent represents the percentage of requests that should be mirrored to BackendRef. Its minimum value is 0 (indicating 0% of requests) and its maximum value is 100 (indicating 100% of requests).</p>
<p>Only one of Fraction or Percent may be specified. If neither field is specified, 100% of requests will be mirrored.</p></td>
</tr>
</tbody>
</table>

## .spec.rules\[\].backendRefs\[\].filters\[\].requestMirror.backendRef

Description
BackendRef references a resource where mirrored requests are sent.

Mirrored requests must be sent only to a single destination endpoint within this BackendRef, irrespective of how many endpoints are present within this BackendRef.

If the referent cannot be found, this BackendRef is invalid and must be dropped from the Gateway. The controller must ensure the "ResolvedRefs" condition on the Route status is set to `status: False` and not configure this backend in the underlying implementation.

If there is a cross-namespace reference to an **existing** object that is not allowed by a ReferenceGrant, the controller must ensure the "ResolvedRefs" condition on the Route is set to `status: False`, with the "RefNotPermitted" reason and not configure this backend in the underlying implementation.

In either error case, the Message of the `ResolvedRefs` Condition should be used to provide more detail about the problem.

Support: Extended for Kubernetes Service

Support: Implementation-specific for any other resource

Type
`object`

Required
- `name`

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
<td style="text-align: left;"><p><code>group</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Group is the group of the referent. For example, "gateway.networking.k8s.io". When unspecified or empty string, core API group is inferred.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>kind</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Kind is the Kubernetes resource kind of the referent. For example "Service".</p>
<p>Defaults to "Service" when not specified.</p>
<p>ExternalName services can refer to CNAME DNS records that may live outside of the cluster and as such are difficult to reason about in terms of conformance. They also may not be safe to forward to (see CVE-2021-25740 for more information). Implementations SHOULD NOT support ExternalName Services.</p>
<p>Support: Core (Services with a type other than ExternalName)</p>
<p>Support: Implementation-specific (Services with type ExternalName)</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>name</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Name is the name of the referent.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>namespace</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Namespace is the namespace of the backend. When unspecified, the local namespace is inferred.</p>
<p>Note that when a namespace different than the local namespace is specified, a ReferenceGrant object is required in the referent namespace to allow that namespace’s owner to accept the reference. See the ReferenceGrant documentation for details.</p>
<p>Support: Core</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>port</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p>Port specifies the destination port number to use for this resource. Port is required when the referent is a Kubernetes Service. In this case, the port number is the service port number, not the target port. For other resources, destination port might be derived from the referent resource or this field.</p></td>
</tr>
</tbody>
</table>

## .spec.rules\[\].backendRefs\[\].filters\[\].requestMirror.fraction

Description
Fraction represents the fraction of requests that should be mirrored to BackendRef.

Only one of Fraction or Percent may be specified. If neither field is specified, 100% of requests will be mirrored.

Type
`object`

Required
- `numerator`

| Property      | Type      | Description |
|---------------|-----------|-------------|
| `denominator` | `integer` |             |
| `numerator`   | `integer` |             |

## .spec.rules\[\].backendRefs\[\].filters\[\].requestRedirect

Description
RequestRedirect defines a schema for a filter that responds to the request with an HTTP redirection.

Support: Core

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
<td style="text-align: left;"><p><code>hostname</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Hostname is the hostname to be used in the value of the <code>Location</code> header in the response. When empty, the hostname in the <code>Host</code> header of the request is used.</p>
<p>Support: Core</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>path</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>Path defines parameters used to modify the path of the incoming request. The modified path is then used to construct the <code>Location</code> header. When empty, the request path is used as-is.</p>
<p>Support: Extended</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>port</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p>Port is the port to be used in the value of the <code>Location</code> header in the response.</p>
<p>If no port is specified, the redirect port MUST be derived using the following rules:</p>
<p>* If redirect scheme is not-empty, the redirect port MUST be the well-known port associated with the redirect scheme. Specifically "http" to port 80 and "https" to port 443. If the redirect scheme does not have a well-known port, the listener port of the Gateway SHOULD be used. * If redirect scheme is empty, the redirect port MUST be the Gateway Listener port.</p>
<p>Implementations SHOULD NOT add the port number in the 'Location' header in the following cases:</p>
<p>* A Location header that will use HTTP (whether that is determined via the Listener protocol or the Scheme field) <em>and</em> use port 80. * A Location header that will use HTTPS (whether that is determined via the Listener protocol or the Scheme field) <em>and</em> use port 443.</p>
<p>Support: Extended</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>scheme</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Scheme is the scheme to be used in the value of the <code>Location</code> header in the response. When empty, the scheme of the request is used.</p>
<p>Scheme redirects can affect the port of the redirect, for more information, refer to the documentation for the port field of this filter.</p>
<p>Note that values may be added to this enum, implementations must ensure that unknown values will not cause a crash.</p>
<p>Unknown values here must result in the implementation setting the Accepted Condition for the Route to <code>status: False</code>, with a Reason of <code>UnsupportedValue</code>.</p>
<p>Support: Extended</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>statusCode</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p>StatusCode is the HTTP status code to be used in response.</p>
<p>Note that values may be added to this enum, implementations must ensure that unknown values will not cause a crash.</p>
<p>Unknown values here must result in the implementation setting the Accepted Condition for the Route to <code>status: False</code>, with a Reason of <code>UnsupportedValue</code>.</p>
<p>Support: Core</p></td>
</tr>
</tbody>
</table>

## .spec.rules\[\].backendRefs\[\].filters\[\].requestRedirect.path

Description
Path defines parameters used to modify the path of the incoming request. The modified path is then used to construct the `Location` header. When empty, the request path is used as-is.

Support: Extended

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
<td style="text-align: left;"><p><code>replaceFullPath</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>ReplaceFullPath specifies the value with which to replace the full path of a request during a rewrite or redirect.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>replacePrefixMatch</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>ReplacePrefixMatch specifies the value with which to replace the prefix match of a request during a rewrite or redirect. For example, a request to "/foo/bar" with a prefix match of "/foo" and a ReplacePrefixMatch of "/xyz" would be modified to "/xyz/bar".</p>
<p>Note that this matches the behavior of the PathPrefix match type. This matches full path elements. A path element refers to the list of labels in the path split by the <code>/</code> separator. When specified, a trailing <code>/</code> is ignored. For example, the paths <code>/abc</code>, <code>/abc/</code>, and <code>/abc/def</code> would all match the prefix <code>/abc</code>, but the path <code>/abcd</code> would not.</p>
<p>ReplacePrefixMatch is only compatible with a <code>PathPrefix</code> HTTPRouteMatch. Using any other HTTPRouteMatch type on the same HTTPRouteRule will result in the implementation setting the Accepted Condition for the Route to <code>status: False</code>.</p>
<p>Request Path | Prefix Match | Replace Prefix | Modified Path</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>type</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Type defines the type of path modifier. Additional types may be added in a future release of the API.</p>
<p>Note that values may be added to this enum, implementations must ensure that unknown values will not cause a crash.</p>
<p>Unknown values here must result in the implementation setting the Accepted Condition for the Route to <code>status: False</code>, with a Reason of <code>UnsupportedValue</code>.</p></td>
</tr>
</tbody>
</table>

## .spec.rules\[\].backendRefs\[\].filters\[\].responseHeaderModifier

Description
ResponseHeaderModifier defines a schema for a filter that modifies response headers.

Support: Extended

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
<td style="text-align: left;"><p><code>add</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>Add adds the given header(s) (name, value) to the request before the action. It appends to any existing values associated with the header name.</p>
<p>Input: GET /foo HTTP/1.1 my-header: foo</p>
<p>Config: add: - name: "my-header" value: "bar,baz"</p>
<p>Output: GET /foo HTTP/1.1 my-header: foo,bar,baz</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>add[]</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>HTTPHeader represents an HTTP Header name and value as defined by RFC 7230.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>remove</code></p></td>
<td style="text-align: left;"><p><code>array (string)</code></p></td>
<td style="text-align: left;"><p>Remove the given header(s) from the HTTP request before the action. The value of Remove is a list of HTTP header names. Note that the header names are case-insensitive (see <a href="https://datatracker.ietf.org/doc/html/rfc2616#section-4.2">https://datatracker.ietf.org/doc/html/rfc2616#section-4.2</a>).</p>
<p>Input: GET /foo HTTP/1.1 my-header1: foo my-header2: bar my-header3: baz</p>
<p>Config: remove: ["my-header1", "my-header3"]</p>
<p>Output: GET /foo HTTP/1.1 my-header2: bar</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>set</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>Set overwrites the request with the given header (name, value) before the action.</p>
<p>Input: GET /foo HTTP/1.1 my-header: foo</p>
<p>Config: set: - name: "my-header" value: "bar"</p>
<p>Output: GET /foo HTTP/1.1 my-header: bar</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>set[]</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>HTTPHeader represents an HTTP Header name and value as defined by RFC 7230.</p></td>
</tr>
</tbody>
</table>

## .spec.rules\[\].backendRefs\[\].filters\[\].responseHeaderModifier.add

Description
Add adds the given header(s) (name, value) to the request before the action. It appends to any existing values associated with the header name.

Input: GET /foo HTTP/1.1 my-header: foo

Config: add: - name: "my-header" value: "bar,baz"

Output: GET /foo HTTP/1.1 my-header: foo,bar,baz

Type
`array`

## .spec.rules\[\].backendRefs\[\].filters\[\].responseHeaderModifier.add\[\]

Description
HTTPHeader represents an HTTP Header name and value as defined by RFC 7230.

Type
`object`

Required
- `name`

- `value`

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
<td style="text-align: left;"><p><code>name</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Name is the name of the HTTP Header to be matched. Name matching MUST be case-insensitive. (See <a href="https://tools.ietf.org/html/rfc7230#section-3.2">https://tools.ietf.org/html/rfc7230#section-3.2</a>).</p>
<p>If multiple entries specify equivalent header names, the first entry with an equivalent name MUST be considered for a match. Subsequent entries with an equivalent header name MUST be ignored. Due to the case-insensitivity of header names, "foo" and "Foo" are considered equivalent.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>value</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Value is the value of HTTP Header to be matched.</p></td>
</tr>
</tbody>
</table>

## .spec.rules\[\].backendRefs\[\].filters\[\].responseHeaderModifier.set

Description
Set overwrites the request with the given header (name, value) before the action.

Input: GET /foo HTTP/1.1 my-header: foo

Config: set: - name: "my-header" value: "bar"

Output: GET /foo HTTP/1.1 my-header: bar

Type
`array`

## .spec.rules\[\].backendRefs\[\].filters\[\].responseHeaderModifier.set\[\]

Description
HTTPHeader represents an HTTP Header name and value as defined by RFC 7230.

Type
`object`

Required
- `name`

- `value`

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
<td style="text-align: left;"><p><code>name</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Name is the name of the HTTP Header to be matched. Name matching MUST be case-insensitive. (See <a href="https://tools.ietf.org/html/rfc7230#section-3.2">https://tools.ietf.org/html/rfc7230#section-3.2</a>).</p>
<p>If multiple entries specify equivalent header names, the first entry with an equivalent name MUST be considered for a match. Subsequent entries with an equivalent header name MUST be ignored. Due to the case-insensitivity of header names, "foo" and "Foo" are considered equivalent.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>value</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Value is the value of HTTP Header to be matched.</p></td>
</tr>
</tbody>
</table>

## .spec.rules\[\].backendRefs\[\].filters\[\].urlRewrite

Description
URLRewrite defines a schema for a filter that modifies a request during forwarding.

Support: Extended

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
<td style="text-align: left;"><p><code>hostname</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Hostname is the value to be used to replace the Host header value during forwarding.</p>
<p>Support: Extended</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>path</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>Path defines a path rewrite.</p>
<p>Support: Extended</p></td>
</tr>
</tbody>
</table>

## .spec.rules\[\].backendRefs\[\].filters\[\].urlRewrite.path

Description
Path defines a path rewrite.

Support: Extended

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
<td style="text-align: left;"><p><code>replaceFullPath</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>ReplaceFullPath specifies the value with which to replace the full path of a request during a rewrite or redirect.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>replacePrefixMatch</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>ReplacePrefixMatch specifies the value with which to replace the prefix match of a request during a rewrite or redirect. For example, a request to "/foo/bar" with a prefix match of "/foo" and a ReplacePrefixMatch of "/xyz" would be modified to "/xyz/bar".</p>
<p>Note that this matches the behavior of the PathPrefix match type. This matches full path elements. A path element refers to the list of labels in the path split by the <code>/</code> separator. When specified, a trailing <code>/</code> is ignored. For example, the paths <code>/abc</code>, <code>/abc/</code>, and <code>/abc/def</code> would all match the prefix <code>/abc</code>, but the path <code>/abcd</code> would not.</p>
<p>ReplacePrefixMatch is only compatible with a <code>PathPrefix</code> HTTPRouteMatch. Using any other HTTPRouteMatch type on the same HTTPRouteRule will result in the implementation setting the Accepted Condition for the Route to <code>status: False</code>.</p>
<p>Request Path | Prefix Match | Replace Prefix | Modified Path</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>type</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Type defines the type of path modifier. Additional types may be added in a future release of the API.</p>
<p>Note that values may be added to this enum, implementations must ensure that unknown values will not cause a crash.</p>
<p>Unknown values here must result in the implementation setting the Accepted Condition for the Route to <code>status: False</code>, with a Reason of <code>UnsupportedValue</code>.</p></td>
</tr>
</tbody>
</table>

## .spec.rules\[\].filters

Description
Filters define the filters that are applied to requests that match this rule.

Wherever possible, implementations SHOULD implement filters in the order they are specified.

Implementations MAY choose to implement this ordering strictly, rejecting any combination or order of filters that cannot be supported. If implementations choose a strict interpretation of filter ordering, they MUST clearly document that behavior.

To reject an invalid combination or order of filters, implementations SHOULD consider the Route Rules with this configuration invalid. If all Route Rules in a Route are invalid, the entire Route would be considered invalid. If only a portion of Route Rules are invalid, implementations MUST set the "PartiallyInvalid" condition for the Route.

Conformance-levels at this level are defined based on the type of filter:

- ALL core filters MUST be supported by all implementations.

- Implementers are encouraged to support extended filters.

- Implementation-specific custom filters have no API guarantees across implementations.

Specifying the same filter multiple times is not supported unless explicitly indicated in the filter.

All filters are expected to be compatible with each other except for the URLRewrite and RequestRedirect filters, which may not be combined. If an implementation cannot support other combinations of filters, they must clearly document that limitation. In cases where incompatible or unsupported filters are specified and cause the `Accepted` condition to be set to status `False`, implementations may use the `IncompatibleFilters` reason to specify this configuration error.

Support: Core

Type
`array`

## .spec.rules\[\].filters\[\]

Description
HTTPRouteFilter defines processing steps that must be completed during the request or response lifecycle. HTTPRouteFilters are meant as an extension point to express processing that may be done in Gateway implementations. Some examples include request or response modification, implementing authentication strategies, rate-limiting, and traffic shaping. API guarantee/conformance is defined based on the type of the filter.

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
<td style="text-align: left;"><p><code>extensionRef</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>ExtensionRef is an optional, implementation-specific extension to the "filter" behavior. For example, resource "myroutefilter" in group "networking.example.net"). ExtensionRef MUST NOT be used for core and extended filters.</p>
<p>This filter can be used multiple times within the same rule.</p>
<p>Support: Implementation-specific</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>requestHeaderModifier</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>RequestHeaderModifier defines a schema for a filter that modifies request headers.</p>
<p>Support: Core</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>requestMirror</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>RequestMirror defines a schema for a filter that mirrors requests. Requests are sent to the specified destination, but responses from that destination are ignored.</p>
<p>This filter can be used multiple times within the same rule. Note that not all implementations will be able to support mirroring to multiple backends.</p>
<p>Support: Extended</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>requestRedirect</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>RequestRedirect defines a schema for a filter that responds to the request with an HTTP redirection.</p>
<p>Support: Core</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>responseHeaderModifier</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>ResponseHeaderModifier defines a schema for a filter that modifies response headers.</p>
<p>Support: Extended</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>type</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Type identifies the type of filter to apply. As with other API fields, types are classified into three conformance levels:</p>
<p>- Core: Filter types and their corresponding configuration defined by "Support: Core" in this package, e.g. "RequestHeaderModifier". All implementations must support core filters.</p>
<p>- Extended: Filter types and their corresponding configuration defined by "Support: Extended" in this package, e.g. "RequestMirror". Implementers are encouraged to support extended filters.</p>
<p>- Implementation-specific: Filters that are defined and supported by specific vendors. In the future, filters showing convergence in behavior across multiple implementations will be considered for inclusion in extended or core conformance levels. Filter-specific configuration for such filters is specified using the ExtensionRef field. <code>Type</code> should be set to "ExtensionRef" for custom filters.</p>
<p>Implementers are encouraged to define custom implementation types to extend the core API with implementation-specific behavior.</p>
<p>If a reference to a custom filter type cannot be resolved, the filter MUST NOT be skipped. Instead, requests that would have been processed by that filter MUST receive a HTTP error response.</p>
<p>Note that values may be added to this enum, implementations must ensure that unknown values will not cause a crash.</p>
<p>Unknown values here must result in the implementation setting the Accepted Condition for the Route to <code>status: False</code>, with a Reason of <code>UnsupportedValue</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>urlRewrite</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>URLRewrite defines a schema for a filter that modifies a request during forwarding.</p>
<p>Support: Extended</p></td>
</tr>
</tbody>
</table>

## .spec.rules\[\].filters\[\].extensionRef

Description
ExtensionRef is an optional, implementation-specific extension to the "filter" behavior. For example, resource "myroutefilter" in group "networking.example.net"). ExtensionRef MUST NOT be used for core and extended filters.

This filter can be used multiple times within the same rule.

Support: Implementation-specific

Type
`object`

Required
- `group`

- `kind`

- `name`

| Property | Type | Description |
|----|----|----|
| `group` | `string` | Group is the group of the referent. For example, "gateway.networking.k8s.io". When unspecified or empty string, core API group is inferred. |
| `kind` | `string` | Kind is kind of the referent. For example "HTTPRoute" or "Service". |
| `name` | `string` | Name is the name of the referent. |

## .spec.rules\[\].filters\[\].requestHeaderModifier

Description
RequestHeaderModifier defines a schema for a filter that modifies request headers.

Support: Core

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
<td style="text-align: left;"><p><code>add</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>Add adds the given header(s) (name, value) to the request before the action. It appends to any existing values associated with the header name.</p>
<p>Input: GET /foo HTTP/1.1 my-header: foo</p>
<p>Config: add: - name: "my-header" value: "bar,baz"</p>
<p>Output: GET /foo HTTP/1.1 my-header: foo,bar,baz</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>add[]</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>HTTPHeader represents an HTTP Header name and value as defined by RFC 7230.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>remove</code></p></td>
<td style="text-align: left;"><p><code>array (string)</code></p></td>
<td style="text-align: left;"><p>Remove the given header(s) from the HTTP request before the action. The value of Remove is a list of HTTP header names. Note that the header names are case-insensitive (see <a href="https://datatracker.ietf.org/doc/html/rfc2616#section-4.2">https://datatracker.ietf.org/doc/html/rfc2616#section-4.2</a>).</p>
<p>Input: GET /foo HTTP/1.1 my-header1: foo my-header2: bar my-header3: baz</p>
<p>Config: remove: ["my-header1", "my-header3"]</p>
<p>Output: GET /foo HTTP/1.1 my-header2: bar</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>set</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>Set overwrites the request with the given header (name, value) before the action.</p>
<p>Input: GET /foo HTTP/1.1 my-header: foo</p>
<p>Config: set: - name: "my-header" value: "bar"</p>
<p>Output: GET /foo HTTP/1.1 my-header: bar</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>set[]</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>HTTPHeader represents an HTTP Header name and value as defined by RFC 7230.</p></td>
</tr>
</tbody>
</table>

## .spec.rules\[\].filters\[\].requestHeaderModifier.add

Description
Add adds the given header(s) (name, value) to the request before the action. It appends to any existing values associated with the header name.

Input: GET /foo HTTP/1.1 my-header: foo

Config: add: - name: "my-header" value: "bar,baz"

Output: GET /foo HTTP/1.1 my-header: foo,bar,baz

Type
`array`

## .spec.rules\[\].filters\[\].requestHeaderModifier.add\[\]

Description
HTTPHeader represents an HTTP Header name and value as defined by RFC 7230.

Type
`object`

Required
- `name`

- `value`

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
<td style="text-align: left;"><p><code>name</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Name is the name of the HTTP Header to be matched. Name matching MUST be case-insensitive. (See <a href="https://tools.ietf.org/html/rfc7230#section-3.2">https://tools.ietf.org/html/rfc7230#section-3.2</a>).</p>
<p>If multiple entries specify equivalent header names, the first entry with an equivalent name MUST be considered for a match. Subsequent entries with an equivalent header name MUST be ignored. Due to the case-insensitivity of header names, "foo" and "Foo" are considered equivalent.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>value</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Value is the value of HTTP Header to be matched.</p></td>
</tr>
</tbody>
</table>

## .spec.rules\[\].filters\[\].requestHeaderModifier.set

Description
Set overwrites the request with the given header (name, value) before the action.

Input: GET /foo HTTP/1.1 my-header: foo

Config: set: - name: "my-header" value: "bar"

Output: GET /foo HTTP/1.1 my-header: bar

Type
`array`

## .spec.rules\[\].filters\[\].requestHeaderModifier.set\[\]

Description
HTTPHeader represents an HTTP Header name and value as defined by RFC 7230.

Type
`object`

Required
- `name`

- `value`

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
<td style="text-align: left;"><p><code>name</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Name is the name of the HTTP Header to be matched. Name matching MUST be case-insensitive. (See <a href="https://tools.ietf.org/html/rfc7230#section-3.2">https://tools.ietf.org/html/rfc7230#section-3.2</a>).</p>
<p>If multiple entries specify equivalent header names, the first entry with an equivalent name MUST be considered for a match. Subsequent entries with an equivalent header name MUST be ignored. Due to the case-insensitivity of header names, "foo" and "Foo" are considered equivalent.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>value</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Value is the value of HTTP Header to be matched.</p></td>
</tr>
</tbody>
</table>

## .spec.rules\[\].filters\[\].requestMirror

Description
RequestMirror defines a schema for a filter that mirrors requests. Requests are sent to the specified destination, but responses from that destination are ignored.

This filter can be used multiple times within the same rule. Note that not all implementations will be able to support mirroring to multiple backends.

Support: Extended

Type
`object`

Required
- `backendRef`

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
<td style="text-align: left;"><p><code>backendRef</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>BackendRef references a resource where mirrored requests are sent.</p>
<p>Mirrored requests must be sent only to a single destination endpoint within this BackendRef, irrespective of how many endpoints are present within this BackendRef.</p>
<p>If the referent cannot be found, this BackendRef is invalid and must be dropped from the Gateway. The controller must ensure the "ResolvedRefs" condition on the Route status is set to <code>status: False</code> and not configure this backend in the underlying implementation.</p>
<p>If there is a cross-namespace reference to an <strong>existing</strong> object that is not allowed by a ReferenceGrant, the controller must ensure the "ResolvedRefs" condition on the Route is set to <code>status: False</code>, with the "RefNotPermitted" reason and not configure this backend in the underlying implementation.</p>
<p>In either error case, the Message of the <code>ResolvedRefs</code> Condition should be used to provide more detail about the problem.</p>
<p>Support: Extended for Kubernetes Service</p>
<p>Support: Implementation-specific for any other resource</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>fraction</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>Fraction represents the fraction of requests that should be mirrored to BackendRef.</p>
<p>Only one of Fraction or Percent may be specified. If neither field is specified, 100% of requests will be mirrored.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>percent</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p>Percent represents the percentage of requests that should be mirrored to BackendRef. Its minimum value is 0 (indicating 0% of requests) and its maximum value is 100 (indicating 100% of requests).</p>
<p>Only one of Fraction or Percent may be specified. If neither field is specified, 100% of requests will be mirrored.</p></td>
</tr>
</tbody>
</table>

## .spec.rules\[\].filters\[\].requestMirror.backendRef

Description
BackendRef references a resource where mirrored requests are sent.

Mirrored requests must be sent only to a single destination endpoint within this BackendRef, irrespective of how many endpoints are present within this BackendRef.

If the referent cannot be found, this BackendRef is invalid and must be dropped from the Gateway. The controller must ensure the "ResolvedRefs" condition on the Route status is set to `status: False` and not configure this backend in the underlying implementation.

If there is a cross-namespace reference to an **existing** object that is not allowed by a ReferenceGrant, the controller must ensure the "ResolvedRefs" condition on the Route is set to `status: False`, with the "RefNotPermitted" reason and not configure this backend in the underlying implementation.

In either error case, the Message of the `ResolvedRefs` Condition should be used to provide more detail about the problem.

Support: Extended for Kubernetes Service

Support: Implementation-specific for any other resource

Type
`object`

Required
- `name`

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
<td style="text-align: left;"><p><code>group</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Group is the group of the referent. For example, "gateway.networking.k8s.io". When unspecified or empty string, core API group is inferred.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>kind</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Kind is the Kubernetes resource kind of the referent. For example "Service".</p>
<p>Defaults to "Service" when not specified.</p>
<p>ExternalName services can refer to CNAME DNS records that may live outside of the cluster and as such are difficult to reason about in terms of conformance. They also may not be safe to forward to (see CVE-2021-25740 for more information). Implementations SHOULD NOT support ExternalName Services.</p>
<p>Support: Core (Services with a type other than ExternalName)</p>
<p>Support: Implementation-specific (Services with type ExternalName)</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>name</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Name is the name of the referent.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>namespace</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Namespace is the namespace of the backend. When unspecified, the local namespace is inferred.</p>
<p>Note that when a namespace different than the local namespace is specified, a ReferenceGrant object is required in the referent namespace to allow that namespace’s owner to accept the reference. See the ReferenceGrant documentation for details.</p>
<p>Support: Core</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>port</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p>Port specifies the destination port number to use for this resource. Port is required when the referent is a Kubernetes Service. In this case, the port number is the service port number, not the target port. For other resources, destination port might be derived from the referent resource or this field.</p></td>
</tr>
</tbody>
</table>

## .spec.rules\[\].filters\[\].requestMirror.fraction

Description
Fraction represents the fraction of requests that should be mirrored to BackendRef.

Only one of Fraction or Percent may be specified. If neither field is specified, 100% of requests will be mirrored.

Type
`object`

Required
- `numerator`

| Property      | Type      | Description |
|---------------|-----------|-------------|
| `denominator` | `integer` |             |
| `numerator`   | `integer` |             |

## .spec.rules\[\].filters\[\].requestRedirect

Description
RequestRedirect defines a schema for a filter that responds to the request with an HTTP redirection.

Support: Core

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
<td style="text-align: left;"><p><code>hostname</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Hostname is the hostname to be used in the value of the <code>Location</code> header in the response. When empty, the hostname in the <code>Host</code> header of the request is used.</p>
<p>Support: Core</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>path</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>Path defines parameters used to modify the path of the incoming request. The modified path is then used to construct the <code>Location</code> header. When empty, the request path is used as-is.</p>
<p>Support: Extended</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>port</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p>Port is the port to be used in the value of the <code>Location</code> header in the response.</p>
<p>If no port is specified, the redirect port MUST be derived using the following rules:</p>
<p>* If redirect scheme is not-empty, the redirect port MUST be the well-known port associated with the redirect scheme. Specifically "http" to port 80 and "https" to port 443. If the redirect scheme does not have a well-known port, the listener port of the Gateway SHOULD be used. * If redirect scheme is empty, the redirect port MUST be the Gateway Listener port.</p>
<p>Implementations SHOULD NOT add the port number in the 'Location' header in the following cases:</p>
<p>* A Location header that will use HTTP (whether that is determined via the Listener protocol or the Scheme field) <em>and</em> use port 80. * A Location header that will use HTTPS (whether that is determined via the Listener protocol or the Scheme field) <em>and</em> use port 443.</p>
<p>Support: Extended</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>scheme</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Scheme is the scheme to be used in the value of the <code>Location</code> header in the response. When empty, the scheme of the request is used.</p>
<p>Scheme redirects can affect the port of the redirect, for more information, refer to the documentation for the port field of this filter.</p>
<p>Note that values may be added to this enum, implementations must ensure that unknown values will not cause a crash.</p>
<p>Unknown values here must result in the implementation setting the Accepted Condition for the Route to <code>status: False</code>, with a Reason of <code>UnsupportedValue</code>.</p>
<p>Support: Extended</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>statusCode</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p>StatusCode is the HTTP status code to be used in response.</p>
<p>Note that values may be added to this enum, implementations must ensure that unknown values will not cause a crash.</p>
<p>Unknown values here must result in the implementation setting the Accepted Condition for the Route to <code>status: False</code>, with a Reason of <code>UnsupportedValue</code>.</p>
<p>Support: Core</p></td>
</tr>
</tbody>
</table>

## .spec.rules\[\].filters\[\].requestRedirect.path

Description
Path defines parameters used to modify the path of the incoming request. The modified path is then used to construct the `Location` header. When empty, the request path is used as-is.

Support: Extended

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
<td style="text-align: left;"><p><code>replaceFullPath</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>ReplaceFullPath specifies the value with which to replace the full path of a request during a rewrite or redirect.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>replacePrefixMatch</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>ReplacePrefixMatch specifies the value with which to replace the prefix match of a request during a rewrite or redirect. For example, a request to "/foo/bar" with a prefix match of "/foo" and a ReplacePrefixMatch of "/xyz" would be modified to "/xyz/bar".</p>
<p>Note that this matches the behavior of the PathPrefix match type. This matches full path elements. A path element refers to the list of labels in the path split by the <code>/</code> separator. When specified, a trailing <code>/</code> is ignored. For example, the paths <code>/abc</code>, <code>/abc/</code>, and <code>/abc/def</code> would all match the prefix <code>/abc</code>, but the path <code>/abcd</code> would not.</p>
<p>ReplacePrefixMatch is only compatible with a <code>PathPrefix</code> HTTPRouteMatch. Using any other HTTPRouteMatch type on the same HTTPRouteRule will result in the implementation setting the Accepted Condition for the Route to <code>status: False</code>.</p>
<p>Request Path | Prefix Match | Replace Prefix | Modified Path</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>type</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Type defines the type of path modifier. Additional types may be added in a future release of the API.</p>
<p>Note that values may be added to this enum, implementations must ensure that unknown values will not cause a crash.</p>
<p>Unknown values here must result in the implementation setting the Accepted Condition for the Route to <code>status: False</code>, with a Reason of <code>UnsupportedValue</code>.</p></td>
</tr>
</tbody>
</table>

## .spec.rules\[\].filters\[\].responseHeaderModifier

Description
ResponseHeaderModifier defines a schema for a filter that modifies response headers.

Support: Extended

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
<td style="text-align: left;"><p><code>add</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>Add adds the given header(s) (name, value) to the request before the action. It appends to any existing values associated with the header name.</p>
<p>Input: GET /foo HTTP/1.1 my-header: foo</p>
<p>Config: add: - name: "my-header" value: "bar,baz"</p>
<p>Output: GET /foo HTTP/1.1 my-header: foo,bar,baz</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>add[]</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>HTTPHeader represents an HTTP Header name and value as defined by RFC 7230.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>remove</code></p></td>
<td style="text-align: left;"><p><code>array (string)</code></p></td>
<td style="text-align: left;"><p>Remove the given header(s) from the HTTP request before the action. The value of Remove is a list of HTTP header names. Note that the header names are case-insensitive (see <a href="https://datatracker.ietf.org/doc/html/rfc2616#section-4.2">https://datatracker.ietf.org/doc/html/rfc2616#section-4.2</a>).</p>
<p>Input: GET /foo HTTP/1.1 my-header1: foo my-header2: bar my-header3: baz</p>
<p>Config: remove: ["my-header1", "my-header3"]</p>
<p>Output: GET /foo HTTP/1.1 my-header2: bar</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>set</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>Set overwrites the request with the given header (name, value) before the action.</p>
<p>Input: GET /foo HTTP/1.1 my-header: foo</p>
<p>Config: set: - name: "my-header" value: "bar"</p>
<p>Output: GET /foo HTTP/1.1 my-header: bar</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>set[]</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>HTTPHeader represents an HTTP Header name and value as defined by RFC 7230.</p></td>
</tr>
</tbody>
</table>

## .spec.rules\[\].filters\[\].responseHeaderModifier.add

Description
Add adds the given header(s) (name, value) to the request before the action. It appends to any existing values associated with the header name.

Input: GET /foo HTTP/1.1 my-header: foo

Config: add: - name: "my-header" value: "bar,baz"

Output: GET /foo HTTP/1.1 my-header: foo,bar,baz

Type
`array`

## .spec.rules\[\].filters\[\].responseHeaderModifier.add\[\]

Description
HTTPHeader represents an HTTP Header name and value as defined by RFC 7230.

Type
`object`

Required
- `name`

- `value`

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
<td style="text-align: left;"><p><code>name</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Name is the name of the HTTP Header to be matched. Name matching MUST be case-insensitive. (See <a href="https://tools.ietf.org/html/rfc7230#section-3.2">https://tools.ietf.org/html/rfc7230#section-3.2</a>).</p>
<p>If multiple entries specify equivalent header names, the first entry with an equivalent name MUST be considered for a match. Subsequent entries with an equivalent header name MUST be ignored. Due to the case-insensitivity of header names, "foo" and "Foo" are considered equivalent.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>value</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Value is the value of HTTP Header to be matched.</p></td>
</tr>
</tbody>
</table>

## .spec.rules\[\].filters\[\].responseHeaderModifier.set

Description
Set overwrites the request with the given header (name, value) before the action.

Input: GET /foo HTTP/1.1 my-header: foo

Config: set: - name: "my-header" value: "bar"

Output: GET /foo HTTP/1.1 my-header: bar

Type
`array`

## .spec.rules\[\].filters\[\].responseHeaderModifier.set\[\]

Description
HTTPHeader represents an HTTP Header name and value as defined by RFC 7230.

Type
`object`

Required
- `name`

- `value`

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
<td style="text-align: left;"><p><code>name</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Name is the name of the HTTP Header to be matched. Name matching MUST be case-insensitive. (See <a href="https://tools.ietf.org/html/rfc7230#section-3.2">https://tools.ietf.org/html/rfc7230#section-3.2</a>).</p>
<p>If multiple entries specify equivalent header names, the first entry with an equivalent name MUST be considered for a match. Subsequent entries with an equivalent header name MUST be ignored. Due to the case-insensitivity of header names, "foo" and "Foo" are considered equivalent.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>value</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Value is the value of HTTP Header to be matched.</p></td>
</tr>
</tbody>
</table>

## .spec.rules\[\].filters\[\].urlRewrite

Description
URLRewrite defines a schema for a filter that modifies a request during forwarding.

Support: Extended

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
<td style="text-align: left;"><p><code>hostname</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Hostname is the value to be used to replace the Host header value during forwarding.</p>
<p>Support: Extended</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>path</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>Path defines a path rewrite.</p>
<p>Support: Extended</p></td>
</tr>
</tbody>
</table>

## .spec.rules\[\].filters\[\].urlRewrite.path

Description
Path defines a path rewrite.

Support: Extended

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
<td style="text-align: left;"><p><code>replaceFullPath</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>ReplaceFullPath specifies the value with which to replace the full path of a request during a rewrite or redirect.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>replacePrefixMatch</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>ReplacePrefixMatch specifies the value with which to replace the prefix match of a request during a rewrite or redirect. For example, a request to "/foo/bar" with a prefix match of "/foo" and a ReplacePrefixMatch of "/xyz" would be modified to "/xyz/bar".</p>
<p>Note that this matches the behavior of the PathPrefix match type. This matches full path elements. A path element refers to the list of labels in the path split by the <code>/</code> separator. When specified, a trailing <code>/</code> is ignored. For example, the paths <code>/abc</code>, <code>/abc/</code>, and <code>/abc/def</code> would all match the prefix <code>/abc</code>, but the path <code>/abcd</code> would not.</p>
<p>ReplacePrefixMatch is only compatible with a <code>PathPrefix</code> HTTPRouteMatch. Using any other HTTPRouteMatch type on the same HTTPRouteRule will result in the implementation setting the Accepted Condition for the Route to <code>status: False</code>.</p>
<p>Request Path | Prefix Match | Replace Prefix | Modified Path</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>type</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Type defines the type of path modifier. Additional types may be added in a future release of the API.</p>
<p>Note that values may be added to this enum, implementations must ensure that unknown values will not cause a crash.</p>
<p>Unknown values here must result in the implementation setting the Accepted Condition for the Route to <code>status: False</code>, with a Reason of <code>UnsupportedValue</code>.</p></td>
</tr>
</tbody>
</table>

## .spec.rules\[\].matches

Description
Matches define conditions used for matching the rule against incoming HTTP requests. Each match is independent, i.e. this rule will be matched if **any** one of the matches is satisfied.

For example, take the following matches configuration:

matches: - path: value: "/foo" headers: - name: "version" value: "v2" - path: value: "/v2/foo"

For a request to match against this rule, a request must satisfy EITHER of the two conditions:

- path prefixed with `/foo` AND contains the header `version: v2`

- path prefix of `/v2/foo`

See the documentation for HTTPRouteMatch on how to specify multiple match conditions that should be ANDed together.

If no matches are specified, the default is a prefix path match on "/", which has the effect of matching every HTTP request.

Proxy or Load Balancer routing configuration generated from HTTPRoutes MUST prioritize matches based on the following criteria, continuing on ties. Across all rules specified on applicable Routes, precedence must be given to the match having:

- "Exact" path match.

- "Prefix" path match with largest number of characters.

- Method match.

- Largest number of header matches.

- Largest number of query param matches.

Note: The precedence of RegularExpression path matches are implementation-specific.

If ties still exist across multiple Routes, matching precedence MUST be determined in order of the following criteria, continuing on ties:

- The oldest Route based on creation timestamp.

- The Route appearing first in alphabetical order by "{namespace}/{name}".

If ties still exist within an HTTPRoute, matching precedence MUST be granted to the FIRST matching rule (in list order) with a match meeting the above criteria.

When no rules matching a request have been successfully attached to the parent a request is coming from, a HTTP 404 status code MUST be returned.

Type
`array`

## .spec.rules\[\].matches\[\]

Description
HTTPRouteMatch defines the predicate used to match requests to a given action. Multiple match types are ANDed together, i.e. the match will evaluate to true only if all conditions are satisfied.

For example, the match below will match a HTTP request only if its path starts with `/foo` AND it contains the `version: v1` header:

match:

    path:
      value: "/foo"
    headers:
    - name: "version"
      value "v1"

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
<td style="text-align: left;"><p><code>headers</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>Headers specifies HTTP request header matchers. Multiple match values are ANDed together, meaning, a request must match all the specified headers to select the route.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>headers[]</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>HTTPHeaderMatch describes how to select a HTTP route by matching HTTP request headers.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>method</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Method specifies HTTP method matcher. When specified, this route will be matched only if the request has the specified method.</p>
<p>Support: Extended</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>path</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>Path specifies a HTTP request path matcher. If this field is not specified, a default prefix match on the "/" path is provided.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>queryParams</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>QueryParams specifies HTTP query parameter matchers. Multiple match values are ANDed together, meaning, a request must match all the specified query parameters to select the route.</p>
<p>Support: Extended</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>queryParams[]</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>HTTPQueryParamMatch describes how to select a HTTP route by matching HTTP query parameters.</p></td>
</tr>
</tbody>
</table>

## .spec.rules\[\].matches\[\].headers

Description
Headers specifies HTTP request header matchers. Multiple match values are ANDed together, meaning, a request must match all the specified headers to select the route.

Type
`array`

## .spec.rules\[\].matches\[\].headers\[\]

Description
HTTPHeaderMatch describes how to select a HTTP route by matching HTTP request headers.

Type
`object`

Required
- `name`

- `value`

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
<td style="text-align: left;"><p><code>name</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Name is the name of the HTTP Header to be matched. Name matching MUST be case-insensitive. (See <a href="https://tools.ietf.org/html/rfc7230#section-3.2">https://tools.ietf.org/html/rfc7230#section-3.2</a>).</p>
<p>If multiple entries specify equivalent header names, only the first entry with an equivalent name MUST be considered for a match. Subsequent entries with an equivalent header name MUST be ignored. Due to the case-insensitivity of header names, "foo" and "Foo" are considered equivalent.</p>
<p>When a header is repeated in an HTTP request, it is implementation-specific behavior as to how this is represented. Generally, proxies should follow the guidance from the RFC: <a href="https://www.rfc-editor.org/rfc/rfc7230.html#section-3.2.2">https://www.rfc-editor.org/rfc/rfc7230.html#section-3.2.2</a> regarding processing a repeated header, with special handling for "Set-Cookie".</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>type</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Type specifies how to match against the value of the header.</p>
<p>Support: Core (Exact)</p>
<p>Support: Implementation-specific (RegularExpression)</p>
<p>Since RegularExpression HeaderMatchType has implementation-specific conformance, implementations can support POSIX, PCRE or any other dialects of regular expressions. Please read the implementation’s documentation to determine the supported dialect.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>value</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Value is the value of HTTP Header to be matched.</p></td>
</tr>
</tbody>
</table>

## .spec.rules\[\].matches\[\].path

Description
Path specifies a HTTP request path matcher. If this field is not specified, a default prefix match on the "/" path is provided.

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
<td style="text-align: left;"><p><code>type</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Type specifies how to match against the path Value.</p>
<p>Support: Core (Exact, PathPrefix)</p>
<p>Support: Implementation-specific (RegularExpression)</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>value</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Value of the HTTP path to match against.</p></td>
</tr>
</tbody>
</table>

## .spec.rules\[\].matches\[\].queryParams

Description
QueryParams specifies HTTP query parameter matchers. Multiple match values are ANDed together, meaning, a request must match all the specified query parameters to select the route.

Support: Extended

Type
`array`

## .spec.rules\[\].matches\[\].queryParams\[\]

Description
HTTPQueryParamMatch describes how to select a HTTP route by matching HTTP query parameters.

Type
`object`

Required
- `name`

- `value`

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
<td style="text-align: left;"><p><code>name</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Name is the name of the HTTP query param to be matched. This must be an exact string match. (See <a href="https://tools.ietf.org/html/rfc7230#section-2.7.3">https://tools.ietf.org/html/rfc7230#section-2.7.3</a>).</p>
<p>If multiple entries specify equivalent query param names, only the first entry with an equivalent name MUST be considered for a match. Subsequent entries with an equivalent query param name MUST be ignored.</p>
<p>If a query param is repeated in an HTTP request, the behavior is purposely left undefined, since different data planes have different capabilities. However, it is <strong>recommended</strong> that implementations should match against the first value of the param if the data plane supports it, as this behavior is expected in other load balancing contexts outside of the Gateway API.</p>
<p>Users SHOULD NOT route traffic based on repeated query params to guard themselves against potential differences in the implementations.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>type</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Type specifies how to match against the value of the query parameter.</p>
<p>Support: Extended (Exact)</p>
<p>Support: Implementation-specific (RegularExpression)</p>
<p>Since RegularExpression QueryParamMatchType has Implementation-specific conformance, implementations can support POSIX, PCRE or any other dialects of regular expressions. Please read the implementation’s documentation to determine the supported dialect.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>value</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Value is the value of HTTP query param to be matched.</p></td>
</tr>
</tbody>
</table>

## .spec.rules\[\].timeouts

Description
Timeouts defines the timeouts that can be configured for an HTTP request.

Support: Extended

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
<td style="text-align: left;"><p><code>backendRequest</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>BackendRequest specifies a timeout for an individual request from the gateway to a backend. This covers the time from when the request first starts being sent from the gateway to when the full response has been received from the backend.</p>
<p>Setting a timeout to the zero duration (e.g. "0s") SHOULD disable the timeout completely. Implementations that cannot completely disable the timeout MUST instead interpret the zero duration as the longest possible value to which the timeout can be set.</p>
<p>An entire client HTTP transaction with a gateway, covered by the Request timeout, may result in more than one call from the gateway to the destination backend, for example, if automatic retries are supported.</p>
<p>The value of BackendRequest must be a Gateway API Duration string as defined by GEP-2257. When this field is unspecified, its behavior is implementation-specific; when specified, the value of BackendRequest must be no more than the value of the Request timeout (since the Request timeout encompasses the BackendRequest timeout).</p>
<p>Support: Extended</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>request</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Request specifies the maximum duration for a gateway to respond to an HTTP request. If the gateway has not been able to respond before this deadline is met, the gateway MUST return a timeout error.</p>
<p>For example, setting the <code>rules.timeouts.request</code> field to the value <code>10s</code> in an <code>HTTPRoute</code> will cause a timeout if a client request is taking longer than 10 seconds to complete.</p>
<p>Setting a timeout to the zero duration (e.g. "0s") SHOULD disable the timeout completely. Implementations that cannot completely disable the timeout MUST instead interpret the zero duration as the longest possible value to which the timeout can be set.</p>
<p>This timeout is intended to cover as close to the whole request-response transaction as possible although an implementation MAY choose to start the timeout after the entire request stream has been received instead of immediately after the transaction is initiated by the client.</p>
<p>The value of Request is a Gateway API Duration string as defined by GEP-2257. When this field is unspecified, request timeout behavior is implementation-specific.</p>
<p>Support: Extended</p></td>
</tr>
</tbody>
</table>

## .status

Description
Status defines the current state of HTTPRoute.

Type
`object`

Required
- `parents`

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
<td style="text-align: left;"><p><code>parents</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>Parents is a list of parent resources (usually Gateways) that are associated with the route, and the status of the route with respect to each parent. When this route attaches to a parent, the controller that manages the parent must add an entry to this list when the controller first sees the route and should update the entry as appropriate when the route or gateway is modified.</p>
<p>Note that parent references that cannot be resolved by an implementation of this API will not be added to this list. Implementations of this API can only populate Route status for the Gateways/parent resources they are responsible for.</p>
<p>A maximum of 32 Gateways will be represented in this list. An empty list means the route has not been attached to any Gateway.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>parents[]</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>RouteParentStatus describes the status of a route with respect to an associated Parent.</p></td>
</tr>
</tbody>
</table>

## .status.parents

Description
Parents is a list of parent resources (usually Gateways) that are associated with the route, and the status of the route with respect to each parent. When this route attaches to a parent, the controller that manages the parent must add an entry to this list when the controller first sees the route and should update the entry as appropriate when the route or gateway is modified.

Note that parent references that cannot be resolved by an implementation of this API will not be added to this list. Implementations of this API can only populate Route status for the Gateways/parent resources they are responsible for.

A maximum of 32 Gateways will be represented in this list. An empty list means the route has not been attached to any Gateway.

Type
`array`

## .status.parents\[\]

Description
RouteParentStatus describes the status of a route with respect to an associated Parent.

Type
`object`

Required
- `controllerName`

- `parentRef`

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
<td style="text-align: left;"><p><code>conditions</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>Conditions describes the status of the route with respect to the Gateway. Note that the route’s availability is also subject to the Gateway’s own status conditions and listener status.</p>
<p>If the Route’s ParentRef specifies an existing Gateway that supports Routes of this kind AND that Gateway’s controller has sufficient access, then that Gateway’s controller MUST set the "Accepted" condition on the Route, to indicate whether the route has been accepted or rejected by the Gateway, and why.</p>
<p>A Route MUST be considered "Accepted" if at least one of the Route’s rules is implemented by the Gateway.</p>
<p>There are a number of cases where the "Accepted" condition may not be set due to lack of controller visibility, that includes when:</p>
<p>* The Route refers to a nonexistent parent. * The Route is of a type that the controller does not support. * The Route is in a namespace the controller does not have access to.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>conditions[]</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>Condition contains details for one aspect of the current state of this API Resource.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>controllerName</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>ControllerName is a domain/path string that indicates the name of the controller that wrote this status. This corresponds with the controllerName field on GatewayClass.</p>
<p>Example: "example.net/gateway-controller".</p>
<p>The format of this field is DOMAIN "/" PATH, where DOMAIN and PATH are valid Kubernetes names (<a href="https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names">https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names</a>).</p>
<p>Controllers MUST populate this field when writing status. Controllers should ensure that entries to status populated with their ControllerName are cleaned up when they are no longer necessary.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>parentRef</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>ParentRef corresponds with a ParentRef in the spec that this RouteParentStatus struct describes the status of.</p></td>
</tr>
</tbody>
</table>

## .status.parents\[\].conditions

Description
Conditions describes the status of the route with respect to the Gateway. Note that the route’s availability is also subject to the Gateway’s own status conditions and listener status.

If the Route’s ParentRef specifies an existing Gateway that supports Routes of this kind AND that Gateway’s controller has sufficient access, then that Gateway’s controller MUST set the "Accepted" condition on the Route, to indicate whether the route has been accepted or rejected by the Gateway, and why.

A Route MUST be considered "Accepted" if at least one of the Route’s rules is implemented by the Gateway.

There are a number of cases where the "Accepted" condition may not be set due to lack of controller visibility, that includes when:

- The Route refers to a nonexistent parent.

- The Route is of a type that the controller does not support.

- The Route is in a namespace the controller does not have access to.

Type
`array`

## .status.parents\[\].conditions\[\]

Description
Condition contains details for one aspect of the current state of this API Resource.

Type
`object`

Required
- `lastTransitionTime`

- `message`

- `reason`

- `status`

- `type`

| Property | Type | Description |
|----|----|----|
| `lastTransitionTime` | `string` | lastTransitionTime is the last time the condition transitioned from one status to another. This should be when the underlying condition changed. If that is not known, then using the time when the API field changed is acceptable. |
| `message` | `string` | message is a human readable message indicating details about the transition. This may be an empty string. |
| `observedGeneration` | `integer` | observedGeneration represents the .metadata.generation that the condition was set based upon. For instance, if .metadata.generation is currently 12, but the .status.conditions\[x\].observedGeneration is 9, the condition is out of date with respect to the current state of the instance. |
| `reason` | `string` | reason contains a programmatic identifier indicating the reason for the condition’s last transition. Producers of specific condition types may define expected values and meanings for this field, and whether the values are considered a guaranteed API. The value should be a CamelCase string. This field may not be empty. |
| `status` | `string` | status of the condition, one of True, False, Unknown. |
| `type` | `string` | type of condition in CamelCase or in foo.example.com/CamelCase. |

## .status.parents\[\].parentRef

Description
ParentRef corresponds with a ParentRef in the spec that this RouteParentStatus struct describes the status of.

Type
`object`

Required
- `name`

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
<td style="text-align: left;"><p><code>group</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Group is the group of the referent. When unspecified, "gateway.networking.k8s.io" is inferred. To set the core API group (such as for a "Service" kind referent), Group must be explicitly set to "" (empty string).</p>
<p>Support: Core</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>kind</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Kind is kind of the referent.</p>
<p>There are two kinds of parent resources with "Core" support:</p>
<p>* Gateway (Gateway conformance profile) * Service (Mesh conformance profile, ClusterIP Services only)</p>
<p>Support for other resources is Implementation-Specific.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>name</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Name is the name of the referent.</p>
<p>Support: Core</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>namespace</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Namespace is the namespace of the referent. When unspecified, this refers to the local namespace of the Route.</p>
<p>Note that there are specific rules for ParentRefs which cross namespace boundaries. Cross-namespace references are only valid if they are explicitly allowed by something in the namespace they are referring to. For example: Gateway has the AllowedRoutes field, and ReferenceGrant provides a generic way to enable any other kind of cross-namespace reference.</p>
<p>Support: Core</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>port</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p>Port is the network port this Route targets. It can be interpreted differently based on the type of parent resource.</p>
<p>When the parent resource is a Gateway, this targets all listeners listening on the specified port that also support this kind of Route(and select this Route). It’s not recommended to set <code>Port</code> unless the networking behaviors specified in a Route must apply to a specific port as opposed to a listener(s) whose port(s) may be changed. When both Port and SectionName are specified, the name and port of the selected listener must match both specified values.</p>
<p>Implementations MAY choose to support other parent resources. Implementations supporting other types of parent resources MUST clearly document how/if Port is interpreted.</p>
<p>For the purpose of status, an attachment is considered successful as long as the parent resource accepts it partially. For example, Gateway listeners can restrict which Routes can attach to them by Route kind, namespace, or hostname. If 1 of 2 Gateway listeners accept attachment from the referencing Route, the Route MUST be considered successfully attached. If no Gateway listeners accept attachment from this Route, the Route MUST be considered detached from the Gateway.</p>
<p>Support: Extended</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>sectionName</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>SectionName is the name of a section within the target resource. In the following resources, SectionName is interpreted as the following:</p>
<p>* Gateway: Listener name. When both Port (experimental) and SectionName are specified, the name and port of the selected listener must match both specified values. * Service: Port name. When both Port (experimental) and SectionName are specified, the name and port of the selected listener must match both specified values.</p>
<p>Implementations MAY choose to support attaching Routes to other resources. If that is the case, they MUST clearly document how SectionName is interpreted.</p>
<p>When unspecified (empty string), this will reference the entire resource. For the purpose of status, an attachment is considered successful if at least one section in the parent resource accepts it. For example, Gateway listeners can restrict which Routes can attach to them by Route kind, namespace, or hostname. If 1 of 2 Gateway listeners accept attachment from the referencing Route, the Route MUST be considered successfully attached. If no Gateway listeners accept attachment from this Route, the Route MUST be considered detached from the Gateway.</p>
<p>Support: Core</p></td>
</tr>
</tbody>
</table>

# API endpoints

The following API endpoints are available:

- `/apis/gateway.networking.k8s.io/v1/httproutes`

  - `GET`: list objects of kind HTTPRoute

- `/apis/gateway.networking.k8s.io/v1/namespaces/{namespace}/httproutes`

  - `DELETE`: delete collection of HTTPRoute

  - `GET`: list objects of kind HTTPRoute

  - `POST`: create a HTTPRoute

- `/apis/gateway.networking.k8s.io/v1/namespaces/{namespace}/httproutes/{name}`

  - `DELETE`: delete a HTTPRoute

  - `GET`: read the specified HTTPRoute

  - `PATCH`: partially update the specified HTTPRoute

  - `PUT`: replace the specified HTTPRoute

- `/apis/gateway.networking.k8s.io/v1/namespaces/{namespace}/httproutes/{name}/status`

  - `GET`: read status of the specified HTTPRoute

  - `PATCH`: partially update status of the specified HTTPRoute

  - `PUT`: replace status of the specified HTTPRoute

## /apis/gateway.networking.k8s.io/v1/httproutes

HTTP method
`GET`

Description
list objects of kind HTTPRoute

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`HTTPRouteList`](../objects/index.md#io-k8s-networking-gateway-v1-HTTPRouteList) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/gateway.networking.k8s.io/v1/namespaces/{namespace}/httproutes

HTTP method
`DELETE`

Description
delete collection of HTTPRoute

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Status`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`GET`

Description
list objects of kind HTTPRoute

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`HTTPRouteList`](../objects/index.md#io-k8s-networking-gateway-v1-HTTPRouteList) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`POST`

Description
create a HTTPRoute

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`HTTPRoute`](httproute-gateway-networking-k8s-io-v1.md#httproute-gateway-networking-k8s-io-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`HTTPRoute`](httproute-gateway-networking-k8s-io-v1.md#httproute-gateway-networking-k8s-io-v1) schema |
| 201 - Created | [`HTTPRoute`](httproute-gateway-networking-k8s-io-v1.md#httproute-gateway-networking-k8s-io-v1) schema |
| 202 - Accepted | [`HTTPRoute`](httproute-gateway-networking-k8s-io-v1.md#httproute-gateway-networking-k8s-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/gateway.networking.k8s.io/v1/namespaces/{namespace}/httproutes/{name}

| Parameter | Type     | Description           |
|-----------|----------|-----------------------|
| `name`    | `string` | name of the HTTPRoute |

Global path parameters

HTTP method
`DELETE`

Description
delete a HTTPRoute

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
read the specified HTTPRoute

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`HTTPRoute`](httproute-gateway-networking-k8s-io-v1.md#httproute-gateway-networking-k8s-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PATCH`

Description
partially update the specified HTTPRoute

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`HTTPRoute`](httproute-gateway-networking-k8s-io-v1.md#httproute-gateway-networking-k8s-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PUT`

Description
replace the specified HTTPRoute

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`HTTPRoute`](httproute-gateway-networking-k8s-io-v1.md#httproute-gateway-networking-k8s-io-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`HTTPRoute`](httproute-gateway-networking-k8s-io-v1.md#httproute-gateway-networking-k8s-io-v1) schema |
| 201 - Created | [`HTTPRoute`](httproute-gateway-networking-k8s-io-v1.md#httproute-gateway-networking-k8s-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/gateway.networking.k8s.io/v1/namespaces/{namespace}/httproutes/{name}/status

| Parameter | Type     | Description           |
|-----------|----------|-----------------------|
| `name`    | `string` | name of the HTTPRoute |

Global path parameters

HTTP method
`GET`

Description
read status of the specified HTTPRoute

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`HTTPRoute`](httproute-gateway-networking-k8s-io-v1.md#httproute-gateway-networking-k8s-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PATCH`

Description
partially update status of the specified HTTPRoute

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`HTTPRoute`](httproute-gateway-networking-k8s-io-v1.md#httproute-gateway-networking-k8s-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PUT`

Description
replace status of the specified HTTPRoute

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`HTTPRoute`](httproute-gateway-networking-k8s-io-v1.md#httproute-gateway-networking-k8s-io-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`HTTPRoute`](httproute-gateway-networking-k8s-io-v1.md#httproute-gateway-networking-k8s-io-v1) schema |
| 201 - Created | [`HTTPRoute`](httproute-gateway-networking-k8s-io-v1.md#httproute-gateway-networking-k8s-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses
