<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Description
BackendTLSPolicy provides a way to configure how a Gateway connects to a Backend via TLS.

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
| `spec` | `object` | Spec defines the desired state of BackendTLSPolicy. |
| `status` | `object` | Status defines the current state of BackendTLSPolicy. |

## .spec

Description
Spec defines the desired state of BackendTLSPolicy.

Type
`object`

Required
- `targetRefs`

- `validation`

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
<td style="text-align: left;"><p><code>options</code></p></td>
<td style="text-align: left;"><p><code>object (string)</code></p></td>
<td style="text-align: left;"><p>Options are a list of key/value pairs to enable extended TLS configuration for each implementation. For example, configuring the minimum TLS version or supported cipher suites.</p>
<p>A set of common keys MAY be defined by the API in the future. To avoid any ambiguity, implementation-specific definitions MUST use domain-prefixed names, such as <code>example.com/my-custom-option</code>. Un-prefixed names are reserved for key names defined by Gateway API.</p>
<p>Support: Implementation-specific</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>targetRefs</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>TargetRefs identifies an API object to apply the policy to. Only Services have Extended support. Implementations MAY support additional objects, with Implementation Specific support. Note that this config applies to the entire referenced resource by default, but this default may change in the future to provide a more granular application of the policy.</p>
<p>TargetRefs must be <em>distinct</em>. This means either that:</p>
<p>* They select different targets. If this is the case, then targetRef entries are distinct. In terms of fields, this means that the multi-part key defined by <code>group</code>, <code>kind</code>, and <code>name</code> must be unique across all targetRef entries in the BackendTLSPolicy. * They select different sectionNames in the same target.</p>
<p>When more than one BackendTLSPolicy selects the same target and sectionName, implementations MUST determine precedence using the following criteria, continuing on ties:</p>
<p>* The older policy by creation timestamp takes precedence. For example, a policy with a creation timestamp of "2021-07-15 01:02:03" MUST be given precedence over a policy with a creation timestamp of "2021-07-15 01:02:04". * The policy appearing first in alphabetical order by {name}. For example, a policy named <code>bar</code> is given precedence over a policy named <code>baz</code>.</p>
<p>For any BackendTLSPolicy that does not take precedence, the implementation MUST ensure the <code>Accepted</code> Condition is set to <code>status: False</code>, with Reason <code>Conflicted</code>.</p>
<p>Implementations SHOULD NOT support more than one targetRef at this time. Although the API technically allows for this, the current guidance for conflict resolution and status handling is lacking. Until that can be clarified in a future release, the safest approach is to support a single targetRef.</p>
<p>Support: Extended for Kubernetes Service</p>
<p>Support: Implementation-specific for any other resource</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>targetRefs[]</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>LocalPolicyTargetReferenceWithSectionName identifies an API object to apply a direct policy to. This should be used as part of Policy resources that can target single resources. For more information on how this policy attachment mode works, and a sample Policy resource, refer to the policy attachment documentation for Gateway API.</p>
<p>Note: This should only be used for direct policy attachment when references to SectionName are actually needed. In all other cases, LocalPolicyTargetReference should be used.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>validation</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>Validation contains backend TLS validation configuration.</p></td>
</tr>
</tbody>
</table>

## .spec.targetRefs

Description
TargetRefs identifies an API object to apply the policy to. Only Services have Extended support. Implementations MAY support additional objects, with Implementation Specific support. Note that this config applies to the entire referenced resource by default, but this default may change in the future to provide a more granular application of the policy.

TargetRefs must be *distinct*. This means either that:

- They select different targets. If this is the case, then targetRef entries are distinct. In terms of fields, this means that the multi-part key defined by `group`, `kind`, and `name` must be unique across all targetRef entries in the BackendTLSPolicy.

- They select different sectionNames in the same target.

When more than one BackendTLSPolicy selects the same target and sectionName, implementations MUST determine precedence using the following criteria, continuing on ties:

- The older policy by creation timestamp takes precedence. For example, a policy with a creation timestamp of "2021-07-15 01:02:03" MUST be given precedence over a policy with a creation timestamp of "2021-07-15 01:02:04".

- The policy appearing first in alphabetical order by {name}. For example, a policy named `bar` is given precedence over a policy named `baz`.

For any BackendTLSPolicy that does not take precedence, the implementation MUST ensure the `Accepted` Condition is set to `status: False`, with Reason `Conflicted`.

Implementations SHOULD NOT support more than one targetRef at this time. Although the API technically allows for this, the current guidance for conflict resolution and status handling is lacking. Until that can be clarified in a future release, the safest approach is to support a single targetRef.

Support: Extended for Kubernetes Service

Support: Implementation-specific for any other resource

Type
`array`

## .spec.targetRefs\[\]

Description
LocalPolicyTargetReferenceWithSectionName identifies an API object to apply a direct policy to. This should be used as part of Policy resources that can target single resources. For more information on how this policy attachment mode works, and a sample Policy resource, refer to the policy attachment documentation for Gateway API.

Note: This should only be used for direct policy attachment when references to SectionName are actually needed. In all other cases, LocalPolicyTargetReference should be used.

Type
`object`

Required
- `group`

- `kind`

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
<td style="text-align: left;"><p>Group is the group of the target resource.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>kind</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Kind is kind of the target resource.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>name</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Name is the name of the target resource.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>sectionName</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>SectionName is the name of a section within the target resource. When unspecified, this targetRef targets the entire resource. In the following resources, SectionName is interpreted as the following:</p>
<p>* Gateway: Listener name * HTTPRoute: HTTPRouteRule name * Service: Port name</p>
<p>If a SectionName is specified, but does not exist on the targeted object, the Policy must fail to attach, and the policy implementation should record a <code>ResolvedRefs</code> or similar Condition in the Policy’s status.</p></td>
</tr>
</tbody>
</table>

## .spec.validation

Description
Validation contains backend TLS validation configuration.

Type
`object`

Required
- `hostname`

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
<td style="text-align: left;"><p><code>caCertificateRefs</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>CACertificateRefs contains one or more references to Kubernetes objects that contain a PEM-encoded TLS CA certificate bundle, which is used to validate a TLS handshake between the Gateway and backend Pod.</p>
<p>If CACertificateRefs is empty or unspecified, then WellKnownCACertificates must be specified. Only one of CACertificateRefs or WellKnownCACertificates may be specified, not both. If CACertificateRefs is empty or unspecified, the configuration for WellKnownCACertificates MUST be honored instead if supported by the implementation.</p>
<p>A CACertificateRef is invalid if:</p>
<p>* It refers to a resource that cannot be resolved (e.g., the referenced resource does not exist) or is misconfigured (e.g., a ConfigMap does not contain a key named <code>ca.crt</code>). In this case, the Reason must be set to <code>InvalidCACertificateRef</code> and the Message of the Condition must indicate which reference is invalid and why.</p>
<p>* It refers to an unknown or unsupported kind of resource. In this case, the Reason must be set to <code>InvalidKind</code> and the Message of the Condition must explain which kind of resource is unknown or unsupported.</p>
<p>* It refers to a resource in another namespace. This may change in future spec updates.</p>
<p>Implementations MAY choose to perform further validation of the certificate content (e.g., checking expiry or enforcing specific formats). In such cases, an implementation-specific Reason and Message must be set for the invalid reference.</p>
<p>In all cases, the implementation MUST ensure the <code>ResolvedRefs</code> Condition on the BackendTLSPolicy is set to <code>status: False</code>, with a Reason and Message that indicate the cause of the error. Connections using an invalid CACertificateRef MUST fail, and the client MUST receive an HTTP 5xx error response. If ALL CACertificateRefs are invalid, the implementation MUST also ensure the <code>Accepted</code> Condition on the BackendTLSPolicy is set to <code>status: False</code>, with a Reason <code>NoValidCACertificate</code>.</p>
<p>A single CACertificateRef to a Kubernetes ConfigMap kind has "Core" support. Implementations MAY choose to support attaching multiple certificates to a backend, but this behavior is implementation-specific.</p>
<p>Support: Core - An optional single reference to a Kubernetes ConfigMap, with the CA certificate in a key named <code>ca.crt</code>.</p>
<p>Support: Implementation-specific - More than one reference, other kinds of resources, or a single reference that includes multiple certificates.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>caCertificateRefs[]</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>LocalObjectReference identifies an API object within the namespace of the referrer. The API object must be valid in the cluster; the Group and Kind must be registered in the cluster for this reference to be valid.</p>
<p>References to objects with invalid Group and Kind are not valid, and must be rejected by the implementation, with appropriate Conditions set on the containing object.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>hostname</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Hostname is used for two purposes in the connection between Gateways and backends:</p>
<p>1. Hostname MUST be used as the SNI to connect to the backend (RFC 6066). 2. Hostname MUST be used for authentication and MUST match the certificate served by the matching backend, unless SubjectAltNames is specified. 3. If SubjectAltNames are specified, Hostname can be used for certificate selection but MUST NOT be used for authentication. If you want to use the value of the Hostname field for authentication, you MUST add it to the SubjectAltNames list.</p>
<p>Support: Core</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>subjectAltNames</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>SubjectAltNames contains one or more Subject Alternative Names. When specified the certificate served from the backend MUST have at least one Subject Alternate Name matching one of the specified SubjectAltNames.</p>
<p>Support: Extended</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>subjectAltNames[]</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>SubjectAltName represents Subject Alternative Name.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>wellKnownCACertificates</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>WellKnownCACertificates specifies whether system CA certificates may be used in the TLS handshake between the gateway and backend pod.</p>
<p>If WellKnownCACertificates is unspecified or empty (""), then CACertificateRefs must be specified with at least one entry for a valid configuration. Only one of CACertificateRefs or WellKnownCACertificates may be specified, not both. If an implementation does not support the WellKnownCACertificates field, or the supplied value is not recognized, the implementation MUST ensure the <code>Accepted</code> Condition on the BackendTLSPolicy is set to <code>status: False</code>, with a Reason <code>Invalid</code>.</p>
<p>Support: Implementation-specific</p></td>
</tr>
</tbody>
</table>

## .spec.validation.caCertificateRefs

Description
CACertificateRefs contains one or more references to Kubernetes objects that contain a PEM-encoded TLS CA certificate bundle, which is used to validate a TLS handshake between the Gateway and backend Pod.

If CACertificateRefs is empty or unspecified, then WellKnownCACertificates must be specified. Only one of CACertificateRefs or WellKnownCACertificates may be specified, not both. If CACertificateRefs is empty or unspecified, the configuration for WellKnownCACertificates MUST be honored instead if supported by the implementation.

A CACertificateRef is invalid if:

- It refers to a resource that cannot be resolved (e.g., the referenced resource does not exist) or is misconfigured (e.g., a ConfigMap does not contain a key named `ca.crt`). In this case, the Reason must be set to `InvalidCACertificateRef` and the Message of the Condition must indicate which reference is invalid and why.

- It refers to an unknown or unsupported kind of resource. In this case, the Reason must be set to `InvalidKind` and the Message of the Condition must explain which kind of resource is unknown or unsupported.

- It refers to a resource in another namespace. This may change in future spec updates.

Implementations MAY choose to perform further validation of the certificate content (e.g., checking expiry or enforcing specific formats). In such cases, an implementation-specific Reason and Message must be set for the invalid reference.

In all cases, the implementation MUST ensure the `ResolvedRefs` Condition on the BackendTLSPolicy is set to `status: False`, with a Reason and Message that indicate the cause of the error. Connections using an invalid CACertificateRef MUST fail, and the client MUST receive an HTTP 5xx error response. If ALL CACertificateRefs are invalid, the implementation MUST also ensure the `Accepted` Condition on the BackendTLSPolicy is set to `status: False`, with a Reason `NoValidCACertificate`.

A single CACertificateRef to a Kubernetes ConfigMap kind has "Core" support. Implementations MAY choose to support attaching multiple certificates to a backend, but this behavior is implementation-specific.

Support: Core - An optional single reference to a Kubernetes ConfigMap, with the CA certificate in a key named `ca.crt`.

Support: Implementation-specific - More than one reference, other kinds of resources, or a single reference that includes multiple certificates.

Type
`array`

## .spec.validation.caCertificateRefs\[\]

Description
LocalObjectReference identifies an API object within the namespace of the referrer. The API object must be valid in the cluster; the Group and Kind must be registered in the cluster for this reference to be valid.

References to objects with invalid Group and Kind are not valid, and must be rejected by the implementation, with appropriate Conditions set on the containing object.

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

## .spec.validation.subjectAltNames

Description
SubjectAltNames contains one or more Subject Alternative Names. When specified the certificate served from the backend MUST have at least one Subject Alternate Name matching one of the specified SubjectAltNames.

Support: Extended

Type
`array`

## .spec.validation.subjectAltNames\[\]

Description
SubjectAltName represents Subject Alternative Name.

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
<td style="text-align: left;"><p><code>hostname</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Hostname contains Subject Alternative Name specified in DNS name format. Required when Type is set to Hostname, ignored otherwise.</p>
<p>Support: Core</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>type</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Type determines the format of the Subject Alternative Name. Always required.</p>
<p>Support: Core</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>uri</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>URI contains Subject Alternative Name specified in a full URI format. It MUST include both a scheme (e.g., "http" or "ftp") and a scheme-specific-part. Common values include SPIFFE IDs like "spiffe://mycluster.example.com/ns/myns/sa/svc1sa". Required when Type is set to URI, ignored otherwise.</p>
<p>Support: Core</p></td>
</tr>
</tbody>
</table>

## .status

Description
Status defines the current state of BackendTLSPolicy.

Type
`object`

Required
- `ancestors`

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
<td style="text-align: left;"><p><code>ancestors</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>Ancestors is a list of ancestor resources (usually Gateways) that are associated with the policy, and the status of the policy with respect to each ancestor. When this policy attaches to a parent, the controller that manages the parent and the ancestors MUST add an entry to this list when the controller first sees the policy and SHOULD update the entry as appropriate when the relevant ancestor is modified.</p>
<p>Note that choosing the relevant ancestor is left to the Policy designers; an important part of Policy design is designing the right object level at which to namespace this status.</p>
<p>Note also that implementations MUST ONLY populate ancestor status for the Ancestor resources they are responsible for. Implementations MUST use the ControllerName field to uniquely identify the entries in this list that they are responsible for.</p>
<p>Note that to achieve this, the list of PolicyAncestorStatus structs MUST be treated as a map with a composite key, made up of the AncestorRef and ControllerName fields combined.</p>
<p>A maximum of 16 ancestors will be represented in this list. An empty list means the Policy is not relevant for any ancestors.</p>
<p>If this slice is full, implementations MUST NOT add further entries. Instead they MUST consider the policy unimplementable and signal that on any related resources such as the ancestor that would be referenced here. For example, if this list was full on BackendTLSPolicy, no additional Gateways would be able to reference the Service targeted by the BackendTLSPolicy.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>ancestors[]</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>PolicyAncestorStatus describes the status of a route with respect to an associated Ancestor.</p>
<p>Ancestors refer to objects that are either the Target of a policy or above it in terms of object hierarchy. For example, if a policy targets a Service, the Policy’s Ancestors are, in order, the Service, the HTTPRoute, the Gateway, and the GatewayClass. Almost always, in this hierarchy, the Gateway will be the most useful object to place Policy status on, so we recommend that implementations SHOULD use Gateway as the PolicyAncestorStatus object unless the designers have a <em>very</em> good reason otherwise.</p>
<p>In the context of policy attachment, the Ancestor is used to distinguish which resource results in a distinct application of this policy. For example, if a policy targets a Service, it may have a distinct result per attached Gateway.</p>
<p>Policies targeting the same resource may have different effects depending on the ancestors of those resources. For example, different Gateways targeting the same Service may have different capabilities, especially if they have different underlying implementations.</p>
<p>For example, in BackendTLSPolicy, the Policy attaches to a Service that is used as a backend in a HTTPRoute that is itself attached to a Gateway. In this case, the relevant object for status is the Gateway, and that is the ancestor object referred to in this status.</p>
<p>Note that a parent is also an ancestor, so for objects where the parent is the relevant object for status, this struct SHOULD still be used.</p>
<p>This struct is intended to be used in a slice that’s effectively a map, with a composite key made up of the AncestorRef and the ControllerName.</p></td>
</tr>
</tbody>
</table>

## .status.ancestors

Description
Ancestors is a list of ancestor resources (usually Gateways) that are associated with the policy, and the status of the policy with respect to each ancestor. When this policy attaches to a parent, the controller that manages the parent and the ancestors MUST add an entry to this list when the controller first sees the policy and SHOULD update the entry as appropriate when the relevant ancestor is modified.

Note that choosing the relevant ancestor is left to the Policy designers; an important part of Policy design is designing the right object level at which to namespace this status.

Note also that implementations MUST ONLY populate ancestor status for the Ancestor resources they are responsible for. Implementations MUST use the ControllerName field to uniquely identify the entries in this list that they are responsible for.

Note that to achieve this, the list of PolicyAncestorStatus structs MUST be treated as a map with a composite key, made up of the AncestorRef and ControllerName fields combined.

A maximum of 16 ancestors will be represented in this list. An empty list means the Policy is not relevant for any ancestors.

If this slice is full, implementations MUST NOT add further entries. Instead they MUST consider the policy unimplementable and signal that on any related resources such as the ancestor that would be referenced here. For example, if this list was full on BackendTLSPolicy, no additional Gateways would be able to reference the Service targeted by the BackendTLSPolicy.

Type
`array`

## .status.ancestors\[\]

Description
PolicyAncestorStatus describes the status of a route with respect to an associated Ancestor.

Ancestors refer to objects that are either the Target of a policy or above it in terms of object hierarchy. For example, if a policy targets a Service, the Policy’s Ancestors are, in order, the Service, the HTTPRoute, the Gateway, and the GatewayClass. Almost always, in this hierarchy, the Gateway will be the most useful object to place Policy status on, so we recommend that implementations SHOULD use Gateway as the PolicyAncestorStatus object unless the designers have a *very* good reason otherwise.

In the context of policy attachment, the Ancestor is used to distinguish which resource results in a distinct application of this policy. For example, if a policy targets a Service, it may have a distinct result per attached Gateway.

Policies targeting the same resource may have different effects depending on the ancestors of those resources. For example, different Gateways targeting the same Service may have different capabilities, especially if they have different underlying implementations.

For example, in BackendTLSPolicy, the Policy attaches to a Service that is used as a backend in a HTTPRoute that is itself attached to a Gateway. In this case, the relevant object for status is the Gateway, and that is the ancestor object referred to in this status.

Note that a parent is also an ancestor, so for objects where the parent is the relevant object for status, this struct SHOULD still be used.

This struct is intended to be used in a slice that’s effectively a map, with a composite key made up of the AncestorRef and the ControllerName.

Type
`object`

Required
- `ancestorRef`

- `conditions`

- `controllerName`

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
<td style="text-align: left;"><p><code>ancestorRef</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>AncestorRef corresponds with a ParentRef in the spec that this PolicyAncestorStatus struct describes the status of.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>conditions</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>Conditions describes the status of the Policy with respect to the given Ancestor.</p></td>
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
</tbody>
</table>

## .status.ancestors\[\].ancestorRef

Description
AncestorRef corresponds with a ParentRef in the spec that this PolicyAncestorStatus struct describes the status of.

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

## .status.ancestors\[\].conditions

Description
Conditions describes the status of the Policy with respect to the given Ancestor.

Type
`array`

## .status.ancestors\[\].conditions\[\]

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

# API endpoints

The following API endpoints are available:

- `/apis/gateway.networking.k8s.io/v1/backendtlspolicies`

  - `GET`: list objects of kind BackendTLSPolicy

- `/apis/gateway.networking.k8s.io/v1/namespaces/{namespace}/backendtlspolicies`

  - `DELETE`: delete collection of BackendTLSPolicy

  - `GET`: list objects of kind BackendTLSPolicy

  - `POST`: create a BackendTLSPolicy

- `/apis/gateway.networking.k8s.io/v1/namespaces/{namespace}/backendtlspolicies/{name}`

  - `DELETE`: delete a BackendTLSPolicy

  - `GET`: read the specified BackendTLSPolicy

  - `PATCH`: partially update the specified BackendTLSPolicy

  - `PUT`: replace the specified BackendTLSPolicy

- `/apis/gateway.networking.k8s.io/v1/namespaces/{namespace}/backendtlspolicies/{name}/status`

  - `GET`: read status of the specified BackendTLSPolicy

  - `PATCH`: partially update status of the specified BackendTLSPolicy

  - `PUT`: replace status of the specified BackendTLSPolicy

## /apis/gateway.networking.k8s.io/v1/backendtlspolicies

HTTP method
`GET`

Description
list objects of kind BackendTLSPolicy

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`BackendTLSPolicyList`](../objects/index.md#io-k8s-networking-gateway-v1-BackendTLSPolicyList) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/gateway.networking.k8s.io/v1/namespaces/{namespace}/backendtlspolicies

HTTP method
`DELETE`

Description
delete collection of BackendTLSPolicy

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Status`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`GET`

Description
list objects of kind BackendTLSPolicy

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`BackendTLSPolicyList`](../objects/index.md#io-k8s-networking-gateway-v1-BackendTLSPolicyList) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`POST`

Description
create a BackendTLSPolicy

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`BackendTLSPolicy`](backendtlspolicy-gateway-networking-k8s-io-v1.md#backendtlspolicy-gateway-networking-k8s-io-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`BackendTLSPolicy`](backendtlspolicy-gateway-networking-k8s-io-v1.md#backendtlspolicy-gateway-networking-k8s-io-v1) schema |
| 201 - Created | [`BackendTLSPolicy`](backendtlspolicy-gateway-networking-k8s-io-v1.md#backendtlspolicy-gateway-networking-k8s-io-v1) schema |
| 202 - Accepted | [`BackendTLSPolicy`](backendtlspolicy-gateway-networking-k8s-io-v1.md#backendtlspolicy-gateway-networking-k8s-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/gateway.networking.k8s.io/v1/namespaces/{namespace}/backendtlspolicies/{name}

| Parameter | Type     | Description                  |
|-----------|----------|------------------------------|
| `name`    | `string` | name of the BackendTLSPolicy |

Global path parameters

HTTP method
`DELETE`

Description
delete a BackendTLSPolicy

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
read the specified BackendTLSPolicy

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`BackendTLSPolicy`](backendtlspolicy-gateway-networking-k8s-io-v1.md#backendtlspolicy-gateway-networking-k8s-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PATCH`

Description
partially update the specified BackendTLSPolicy

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`BackendTLSPolicy`](backendtlspolicy-gateway-networking-k8s-io-v1.md#backendtlspolicy-gateway-networking-k8s-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PUT`

Description
replace the specified BackendTLSPolicy

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`BackendTLSPolicy`](backendtlspolicy-gateway-networking-k8s-io-v1.md#backendtlspolicy-gateway-networking-k8s-io-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`BackendTLSPolicy`](backendtlspolicy-gateway-networking-k8s-io-v1.md#backendtlspolicy-gateway-networking-k8s-io-v1) schema |
| 201 - Created | [`BackendTLSPolicy`](backendtlspolicy-gateway-networking-k8s-io-v1.md#backendtlspolicy-gateway-networking-k8s-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/gateway.networking.k8s.io/v1/namespaces/{namespace}/backendtlspolicies/{name}/status

| Parameter | Type     | Description                  |
|-----------|----------|------------------------------|
| `name`    | `string` | name of the BackendTLSPolicy |

Global path parameters

HTTP method
`GET`

Description
read status of the specified BackendTLSPolicy

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`BackendTLSPolicy`](backendtlspolicy-gateway-networking-k8s-io-v1.md#backendtlspolicy-gateway-networking-k8s-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PATCH`

Description
partially update status of the specified BackendTLSPolicy

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`BackendTLSPolicy`](backendtlspolicy-gateway-networking-k8s-io-v1.md#backendtlspolicy-gateway-networking-k8s-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PUT`

Description
replace status of the specified BackendTLSPolicy

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`BackendTLSPolicy`](backendtlspolicy-gateway-networking-k8s-io-v1.md#backendtlspolicy-gateway-networking-k8s-io-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`BackendTLSPolicy`](backendtlspolicy-gateway-networking-k8s-io-v1.md#backendtlspolicy-gateway-networking-k8s-io-v1) schema |
| 201 - Created | [`BackendTLSPolicy`](backendtlspolicy-gateway-networking-k8s-io-v1.md#backendtlspolicy-gateway-networking-k8s-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses
