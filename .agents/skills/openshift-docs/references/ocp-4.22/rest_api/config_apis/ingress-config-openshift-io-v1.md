<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Description
Ingress holds cluster-wide information about ingress, including the default ingress domain used for routes. The canonical name is `cluster`.

Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).

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
| `spec` | `object` | spec holds user settable values for configuration |
| `status` | `object` | status holds observed values from the cluster. They may not be overridden. |

## .spec

Description
spec holds user settable values for configuration

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
<td style="text-align: left;"><p><code>appsDomain</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>appsDomain is an optional domain to use instead of the one specified in the domain field when a Route is created without specifying an explicit host. If appsDomain is nonempty, this value is used to generate default host values for Route. Unlike domain, appsDomain may be modified after installation. This assumes a new ingresscontroller has been setup with a wildcard certificate.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>componentRoutes</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>componentRoutes is an optional list of routes that are managed by OpenShift components that a cluster-admin is able to configure the hostname and serving certificate for. The namespace and name of each route in this list should match an existing entry in the status.componentRoutes list.</p>
<p>To determine the set of configurable Routes, look at namespace and name of entries in the .status.componentRoutes list, where participating operators write the status of configurable routes.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>componentRoutes[]</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>ComponentRouteSpec allows for configuration of a route’s hostname and serving certificate.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>domain</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>domain is used to generate a default host name for a route when the route’s host name is empty. The generated host name will follow this pattern: "&lt;route-name&gt;.&lt;route-namespace&gt;.&lt;domain&gt;".</p>
<p>It is also used as the default wildcard domain suffix for ingress. The default ingresscontroller domain will follow this pattern: "*.&lt;domain&gt;".</p>
<p>Once set, changing domain is not currently supported.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>loadBalancer</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>loadBalancer contains the load balancer details in general which are not only specific to the underlying infrastructure provider of the current cluster and are required for Ingress Controller to work on OpenShift.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>requiredHSTSPolicies</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>requiredHSTSPolicies specifies HSTS policies that are required to be set on newly created or updated routes matching the domainPattern/s and namespaceSelector/s that are specified in the policy. Each requiredHSTSPolicy must have at least a domainPattern and a maxAge to validate a route HSTS Policy route annotation, and affect route admission.</p>
<p>A candidate route is checked for HSTS Policies if it has the HSTS Policy route annotation: "haproxy.router.openshift.io/hsts_header" E.g. haproxy.router.openshift.io/hsts_header: max-age=31536000;preload;includeSubDomains</p>
<p>- For each candidate route, if it matches a requiredHSTSPolicy domainPattern and optional namespaceSelector, then the maxAge, preloadPolicy, and includeSubdomainsPolicy must be valid to be admitted. Otherwise, the route is rejected. - The first match, by domainPattern and optional namespaceSelector, in the ordering of the RequiredHSTSPolicies determines the route’s admission status. - If the candidate route doesn’t match any requiredHSTSPolicy domainPattern and optional namespaceSelector, then it may use any HSTS Policy annotation.</p>
<p>The HSTS policy configuration may be changed after routes have already been created. An update to a previously admitted route may then fail if the updated route does not conform to the updated HSTS policy configuration. However, changing the HSTS policy configuration will not cause a route that is already admitted to stop working.</p>
<p>Note that if there are no RequiredHSTSPolicies, any HSTS Policy annotation on the route is valid.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>requiredHSTSPolicies[]</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"></td>
</tr>
</tbody>
</table>

## .spec.componentRoutes

Description
componentRoutes is an optional list of routes that are managed by OpenShift components that a cluster-admin is able to configure the hostname and serving certificate for. The namespace and name of each route in this list should match an existing entry in the status.componentRoutes list.

To determine the set of configurable Routes, look at namespace and name of entries in the .status.componentRoutes list, where participating operators write the status of configurable routes.

Type
`array`

## .spec.componentRoutes\[\]

Description
ComponentRouteSpec allows for configuration of a route’s hostname and serving certificate.

Type
`object`

Required
- `hostname`

- `name`

- `namespace`

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
<td style="text-align: left;"><p>hostname is the hostname that should be used by the route.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>name</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>name is the logical name of the route to customize.</p>
<p>The namespace and name of this componentRoute must match a corresponding entry in the list of status.componentRoutes if the route is to be customized.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>namespace</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>namespace is the namespace of the route to customize.</p>
<p>The namespace and name of this componentRoute must match a corresponding entry in the list of status.componentRoutes if the route is to be customized.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>servingCertKeyPairSecret</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>servingCertKeyPairSecret is a reference to a secret of type <code>kubernetes.io/tls</code> in the openshift-config namespace. The serving cert/key pair must match and will be used by the operator to fulfill the intent of serving with this name. If the custom hostname uses the default routing suffix of the cluster, the Secret specification for a serving certificate will not be needed.</p></td>
</tr>
</tbody>
</table>

## .spec.componentRoutes\[\].servingCertKeyPairSecret

Description
servingCertKeyPairSecret is a reference to a secret of type `kubernetes.io/tls` in the openshift-config namespace. The serving cert/key pair must match and will be used by the operator to fulfill the intent of serving with this name. If the custom hostname uses the default routing suffix of the cluster, the Secret specification for a serving certificate will not be needed.

Type
`object`

Required
- `name`

| Property | Type     | Description                                        |
|----------|----------|----------------------------------------------------|
| `name`   | `string` | name is the metadata.name of the referenced secret |

## .spec.loadBalancer

Description
loadBalancer contains the load balancer details in general which are not only specific to the underlying infrastructure provider of the current cluster and are required for Ingress Controller to work on OpenShift.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `platform` | `object` | platform holds configuration specific to the underlying infrastructure provider for the ingress load balancers. When omitted, this means the user has no opinion and the platform is left to choose reasonable defaults. These defaults are subject to change over time. |

## .spec.loadBalancer.platform

Description
platform holds configuration specific to the underlying infrastructure provider for the ingress load balancers. When omitted, this means the user has no opinion and the platform is left to choose reasonable defaults. These defaults are subject to change over time.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `aws` | `object` | aws contains settings specific to the Amazon Web Services infrastructure provider. |
| `type` | `string` | type is the underlying infrastructure provider for the cluster. Allowed values are "AWS", "Azure", "BareMetal", "GCP", "Libvirt", "OpenStack", "VSphere", "oVirt", "KubeVirt", "EquinixMetal", "PowerVS", "AlibabaCloud", "Nutanix" and "None". Individual components may not support all platforms, and must handle unrecognized platforms as None if they do not support that platform. |

## .spec.loadBalancer.platform.aws

Description
aws contains settings specific to the Amazon Web Services infrastructure provider.

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
<td style="text-align: left;"><p><code>type</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>type allows user to set a load balancer type. When this field is set the default ingresscontroller will get created using the specified LBType. If this field is not set then the default ingress controller of LBType Classic will be created. Valid values are:</p>
<p>* "Classic": A Classic Load Balancer that makes routing decisions at either the transport layer (TCP/SSL) or the application layer (HTTP/HTTPS). See the following for additional details:</p>
<p><a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/load-balancer-types.html#clb">https://docs.aws.amazon.com/AmazonECS/latest/developerguide/load-balancer-types.html#clb</a></p>
<p>* "NLB": A Network Load Balancer that makes routing decisions at the transport layer (TCP/SSL). See the following for additional details:</p>
<p><a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/load-balancer-types.html#nlb">https://docs.aws.amazon.com/AmazonECS/latest/developerguide/load-balancer-types.html#nlb</a></p></td>
</tr>
</tbody>
</table>

## .spec.requiredHSTSPolicies

Description
requiredHSTSPolicies specifies HSTS policies that are required to be set on newly created or updated routes matching the domainPattern/s and namespaceSelector/s that are specified in the policy. Each requiredHSTSPolicy must have at least a domainPattern and a maxAge to validate a route HSTS Policy route annotation, and affect route admission.

A candidate route is checked for HSTS Policies if it has the HSTS Policy route annotation: "haproxy.router.openshift.io/hsts_header" E.g. haproxy.router.openshift.io/hsts_header: max-age=31536000;preload;includeSubDomains

- For each candidate route, if it matches a requiredHSTSPolicy domainPattern and optional namespaceSelector, then the maxAge, preloadPolicy, and includeSubdomainsPolicy must be valid to be admitted. Otherwise, the route is rejected.

- The first match, by domainPattern and optional namespaceSelector, in the ordering of the RequiredHSTSPolicies determines the route’s admission status.

- If the candidate route doesn’t match any requiredHSTSPolicy domainPattern and optional namespaceSelector, then it may use any HSTS Policy annotation.

The HSTS policy configuration may be changed after routes have already been created. An update to a previously admitted route may then fail if the updated route does not conform to the updated HSTS policy configuration. However, changing the HSTS policy configuration will not cause a route that is already admitted to stop working.

Note that if there are no RequiredHSTSPolicies, any HSTS Policy annotation on the route is valid.

Type
`array`

## .spec.requiredHSTSPolicies\[\]

Description

Type
`object`

Required
- `domainPatterns`

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
<td style="text-align: left;"><p><code>domainPatterns</code></p></td>
<td style="text-align: left;"><p><code>array (string)</code></p></td>
<td style="text-align: left;"><p>domainPatterns is a list of domains for which the desired HSTS annotations are required. If domainPatterns is specified and a route is created with a spec.host matching one of the domains, the route must specify the HSTS Policy components described in the matching RequiredHSTSPolicy.</p>
<p>The use of wildcards is allowed like this: <strong>.foo.com matches everything under foo.com. foo.com only matches foo.com, so to cover foo.com and everything under it, you must specify *both</strong>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>includeSubDomainsPolicy</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>includeSubDomainsPolicy means the HSTS Policy should apply to any subdomains of the host’s domain name. Thus, for the host bar.foo.com, if includeSubDomainsPolicy was set to RequireIncludeSubDomains: - the host app.bar.foo.com would inherit the HSTS Policy of bar.foo.com - the host bar.foo.com would inherit the HSTS Policy of bar.foo.com - the host foo.com would NOT inherit the HSTS Policy of bar.foo.com - the host def.foo.com would NOT inherit the HSTS Policy of bar.foo.com</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>maxAge</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>maxAge is the delta time range in seconds during which hosts are regarded as HSTS hosts. If set to 0, it negates the effect, and hosts are removed as HSTS hosts. If set to 0 and includeSubdomains is specified, all subdomains of the host are also removed as HSTS hosts. maxAge is a time-to-live value, and if this policy is not refreshed on a client, the HSTS policy will eventually expire on that client.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>namespaceSelector</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>namespaceSelector specifies a label selector such that the policy applies only to those routes that are in namespaces with labels that match the selector, and are in one of the DomainPatterns. Defaults to the empty LabelSelector, which matches everything.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>preloadPolicy</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>preloadPolicy directs the client to include hosts in its host preload list so that it never needs to do an initial load to get the HSTS header (note that this is not defined in RFC 6797 and is therefore client implementation-dependent).</p></td>
</tr>
</tbody>
</table>

## .spec.requiredHSTSPolicies\[\].maxAge

Description
maxAge is the delta time range in seconds during which hosts are regarded as HSTS hosts. If set to 0, it negates the effect, and hosts are removed as HSTS hosts. If set to 0 and includeSubdomains is specified, all subdomains of the host are also removed as HSTS hosts. maxAge is a time-to-live value, and if this policy is not refreshed on a client, the HSTS policy will eventually expire on that client.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `largestMaxAge` | `integer` | The largest allowed value (in seconds) of the RequiredHSTSPolicy max-age This value can be left unspecified, in which case no upper limit is enforced. |
| `smallestMaxAge` | `integer` | The smallest allowed value (in seconds) of the RequiredHSTSPolicy max-age Setting max-age=0 allows the deletion of an existing HSTS header from a host. This is a necessary tool for administrators to quickly correct mistakes. This value can be left unspecified, in which case no lower limit is enforced. |

## .spec.requiredHSTSPolicies\[\].namespaceSelector

Description
namespaceSelector specifies a label selector such that the policy applies only to those routes that are in namespaces with labels that match the selector, and are in one of the DomainPatterns. Defaults to the empty LabelSelector, which matches everything.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `matchExpressions` | `array` | matchExpressions is a list of label selector requirements. The requirements are ANDed. |
| `matchExpressions[]` | `object` | A label selector requirement is a selector that contains values, a key, and an operator that relates the key and values. |
| `matchLabels` | `object (string)` | matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed. |

## .spec.requiredHSTSPolicies\[\].namespaceSelector.matchExpressions

Description
matchExpressions is a list of label selector requirements. The requirements are ANDed.

Type
`array`

## .spec.requiredHSTSPolicies\[\].namespaceSelector.matchExpressions\[\]

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
status holds observed values from the cluster. They may not be overridden.

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
<td style="text-align: left;"><p><code>componentRoutes</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>componentRoutes is where participating operators place the current route status for routes whose hostnames and serving certificates can be customized by the cluster-admin.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>componentRoutes[]</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>ComponentRouteStatus contains information allowing configuration of a route’s hostname and serving certificate.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>defaultPlacement</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>defaultPlacement is set at installation time to control which nodes will host the ingress router pods by default. The options are control-plane nodes or worker nodes.</p>
<p>This field works by dictating how the Cluster Ingress Operator will consider unset replicas and nodePlacement fields in IngressController resources when creating the corresponding Deployments.</p>
<p>See the documentation for the IngressController replicas and nodePlacement fields for more information.</p>
<p>When omitted, the default value is Workers</p></td>
</tr>
</tbody>
</table>

## .status.componentRoutes

Description
componentRoutes is where participating operators place the current route status for routes whose hostnames and serving certificates can be customized by the cluster-admin.

Type
`array`

## .status.componentRoutes\[\]

Description
ComponentRouteStatus contains information allowing configuration of a route’s hostname and serving certificate.

Type
`object`

Required
- `defaultHostname`

- `name`

- `namespace`

- `relatedObjects`

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
<td style="text-align: left;"><p>conditions are used to communicate the state of the componentRoutes entry.</p>
<p>Supported conditions include Available, Degraded and Progressing.</p>
<p>If available is true, the content served by the route can be accessed by users. This includes cases where a default may continue to serve content while the customized route specified by the cluster-admin is being configured.</p>
<p>If Degraded is true, that means something has gone wrong trying to handle the componentRoutes entry. The currentHostnames field may or may not be in effect.</p>
<p>If Progressing is true, that means the component is taking some action related to the componentRoutes entry.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>conditions[]</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>Condition contains details for one aspect of the current state of this API Resource.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>consumingUsers</code></p></td>
<td style="text-align: left;"><p><code>array (string)</code></p></td>
<td style="text-align: left;"><p>consumingUsers is a slice of ServiceAccounts that need to have read permission on the servingCertKeyPairSecret secret.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>currentHostnames</code></p></td>
<td style="text-align: left;"><p><code>array (string)</code></p></td>
<td style="text-align: left;"><p>currentHostnames is the list of current names used by the route. Typically, this list should consist of a single hostname, but if multiple hostnames are supported by the route the operator may write multiple entries to this list.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>defaultHostname</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>defaultHostname is the hostname of this route prior to customization.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>name</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>name is the logical name of the route to customize. It does not have to be the actual name of a route resource but it cannot be renamed.</p>
<p>The namespace and name of this componentRoute must match a corresponding entry in the list of spec.componentRoutes if the route is to be customized.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>namespace</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>namespace is the namespace of the route to customize. It must be a real namespace. Using an actual namespace ensures that no two components will conflict and the same component can be installed multiple times.</p>
<p>The namespace and name of this componentRoute must match a corresponding entry in the list of spec.componentRoutes if the route is to be customized.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>relatedObjects</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>relatedObjects is a list of resources which are useful when debugging or inspecting how spec.componentRoutes is applied.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>relatedObjects[]</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>ObjectReference contains enough information to let you inspect or modify the referred object.</p></td>
</tr>
</tbody>
</table>

## .status.componentRoutes\[\].conditions

Description
conditions are used to communicate the state of the componentRoutes entry.

Supported conditions include Available, Degraded and Progressing.

If available is true, the content served by the route can be accessed by users. This includes cases where a default may continue to serve content while the customized route specified by the cluster-admin is being configured.

If Degraded is true, that means something has gone wrong trying to handle the componentRoutes entry. The currentHostnames field may or may not be in effect.

If Progressing is true, that means the component is taking some action related to the componentRoutes entry.

Type
`array`

## .status.componentRoutes\[\].conditions\[\]

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

## .status.componentRoutes\[\].relatedObjects

Description
relatedObjects is a list of resources which are useful when debugging or inspecting how spec.componentRoutes is applied.

Type
`array`

## .status.componentRoutes\[\].relatedObjects\[\]

Description
ObjectReference contains enough information to let you inspect or modify the referred object.

Type
`object`

Required
- `group`

- `name`

- `resource`

| Property    | Type     | Description                |
|-------------|----------|----------------------------|
| `group`     | `string` | group of the referent.     |
| `name`      | `string` | name of the referent.      |
| `namespace` | `string` | namespace of the referent. |
| `resource`  | `string` | resource of the referent.  |

# API endpoints

The following API endpoints are available:

- `/apis/config.openshift.io/v1/ingresses`

  - `DELETE`: delete collection of Ingress

  - `GET`: list objects of kind Ingress

  - `POST`: create an Ingress

- `/apis/config.openshift.io/v1/ingresses/{name}`

  - `DELETE`: delete an Ingress

  - `GET`: read the specified Ingress

  - `PATCH`: partially update the specified Ingress

  - `PUT`: replace the specified Ingress

- `/apis/config.openshift.io/v1/ingresses/{name}/status`

  - `GET`: read status of the specified Ingress

  - `PATCH`: partially update status of the specified Ingress

  - `PUT`: replace status of the specified Ingress

## /apis/config.openshift.io/v1/ingresses

HTTP method
`DELETE`

Description
delete collection of Ingress

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Status`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`GET`

Description
list objects of kind Ingress

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`IngressList`](../objects/index.md#io-openshift-config-v1-IngressList) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`POST`

Description
create an Ingress

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`Ingress`](ingress-config-openshift-io-v1.md#ingress-config-openshift-io-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Ingress`](ingress-config-openshift-io-v1.md#ingress-config-openshift-io-v1) schema |
| 201 - Created | [`Ingress`](ingress-config-openshift-io-v1.md#ingress-config-openshift-io-v1) schema |
| 202 - Accepted | [`Ingress`](ingress-config-openshift-io-v1.md#ingress-config-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/config.openshift.io/v1/ingresses/{name}

| Parameter | Type     | Description         |
|-----------|----------|---------------------|
| `name`    | `string` | name of the Ingress |

Global path parameters

HTTP method
`DELETE`

Description
delete an Ingress

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
read the specified Ingress

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Ingress`](ingress-config-openshift-io-v1.md#ingress-config-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PATCH`

Description
partially update the specified Ingress

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Ingress`](ingress-config-openshift-io-v1.md#ingress-config-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PUT`

Description
replace the specified Ingress

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`Ingress`](ingress-config-openshift-io-v1.md#ingress-config-openshift-io-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Ingress`](ingress-config-openshift-io-v1.md#ingress-config-openshift-io-v1) schema |
| 201 - Created | [`Ingress`](ingress-config-openshift-io-v1.md#ingress-config-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/config.openshift.io/v1/ingresses/{name}/status

| Parameter | Type     | Description         |
|-----------|----------|---------------------|
| `name`    | `string` | name of the Ingress |

Global path parameters

HTTP method
`GET`

Description
read status of the specified Ingress

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Ingress`](ingress-config-openshift-io-v1.md#ingress-config-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PATCH`

Description
partially update status of the specified Ingress

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Ingress`](ingress-config-openshift-io-v1.md#ingress-config-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PUT`

Description
replace status of the specified Ingress

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`Ingress`](ingress-config-openshift-io-v1.md#ingress-config-openshift-io-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Ingress`](ingress-config-openshift-io-v1.md#ingress-config-openshift-io-v1) schema |
| 201 - Created | [`Ingress`](ingress-config-openshift-io-v1.md#ingress-config-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses
