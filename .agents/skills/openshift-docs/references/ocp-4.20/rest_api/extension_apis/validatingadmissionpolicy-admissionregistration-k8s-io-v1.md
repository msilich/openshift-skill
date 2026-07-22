<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Description
ValidatingAdmissionPolicy describes the definition of an admission validation policy that accepts or rejects an object without changing it.

Type
`object`

# Specification

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ObjectMeta`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) | Standard object metadata; More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata>. |
| `spec` | `object` | ValidatingAdmissionPolicySpec is the specification of the desired behavior of the AdmissionPolicy. |
| `status` | `object` | ValidatingAdmissionPolicyStatus represents the status of an admission validation policy. |

## .spec

Description
ValidatingAdmissionPolicySpec is the specification of the desired behavior of the AdmissionPolicy.

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
<td style="text-align: left;"><p><code>auditAnnotations</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>auditAnnotations contains CEL expressions which are used to produce audit annotations for the audit event of the API request. validations and auditAnnotations may not both be empty; a least one of validations or auditAnnotations is required.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>auditAnnotations[]</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>AuditAnnotation describes how to produce an audit annotation for an API request.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>failurePolicy</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>failurePolicy defines how to handle failures for the admission policy. Failures can occur from CEL expression parse errors, type check errors, runtime errors and invalid or mis-configured policy definitions or bindings.</p>
<p>A policy is invalid if spec.paramKind refers to a non-existent Kind. A binding is invalid if spec.paramRef.name refers to a non-existent resource.</p>
<p>failurePolicy does not define how validations that evaluate to false are handled.</p>
<p>When failurePolicy is set to Fail, ValidatingAdmissionPolicyBinding validationActions define how failures are enforced.</p>
<p>Allowed values are Ignore or Fail. Defaults to Fail.</p>
<p>Possible enum values: - <code>"Fail"</code> means that an error calling the webhook causes the admission to fail. - <code>"Ignore"</code> means that an error calling the webhook is ignored.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>matchConditions</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>MatchConditions is a list of conditions that must be met for a request to be validated. Match conditions filter requests that have already been matched by the rules, namespaceSelector, and objectSelector. An empty list of matchConditions matches all requests. There are a maximum of 64 match conditions allowed.</p>
<p>If a parameter object is provided, it can be accessed via the <code>params</code> handle in the same manner as validation expressions.</p>
<p>The exact matching logic is (in order): 1. If ANY matchCondition evaluates to FALSE, the policy is skipped. 2. If ALL matchConditions evaluate to TRUE, the policy is evaluated. 3. If any matchCondition evaluates to an error (but none are FALSE): - If failurePolicy=Fail, reject the request - If failurePolicy=Ignore, the policy is skipped</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>matchConditions[]</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>MatchCondition represents a condition which must by fulfilled for a request to be sent to a webhook.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>matchConstraints</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>MatchResources decides whether to run the admission control policy on an object based on whether it meets the match criteria. The exclude rules take precedence over include rules (if a resource matches both, it is excluded)</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>paramKind</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>ParamKind is a tuple of Group Kind and Version.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>validations</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>Validations contain CEL expressions which is used to apply the validation. Validations and AuditAnnotations may not both be empty; a minimum of one Validations or AuditAnnotations is required.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>validations[]</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>Validation specifies the CEL expression which is used to apply the validation.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>variables</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>Variables contain definitions of variables that can be used in composition of other expressions. Each variable is defined as a named CEL expression. The variables defined here will be available under <code>variables</code> in other expressions of the policy except MatchConditions because MatchConditions are evaluated before the rest of the policy.</p>
<p>The expression of a variable can refer to other variables defined earlier in the list but not those after. Thus, Variables must be sorted by the order of first appearance and acyclic.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>variables[]</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>Variable is the definition of a variable that is used for composition. A variable is defined as a named expression.</p></td>
</tr>
</tbody>
</table>

## .spec.auditAnnotations

Description
auditAnnotations contains CEL expressions which are used to produce audit annotations for the audit event of the API request. validations and auditAnnotations may not both be empty; a least one of validations or auditAnnotations is required.

Type
`array`

## .spec.auditAnnotations\[\]

Description
AuditAnnotation describes how to produce an audit annotation for an API request.

Type
`object`

Required
- `key`

- `valueExpression`

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
<td style="text-align: left;"><p><code>key</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>key specifies the audit annotation key. The audit annotation keys of a ValidatingAdmissionPolicy must be unique. The key must be a qualified name ([A-Za-z0-9][-A-Za-z0-9_.]*) no more than 63 bytes in length.</p>
<p>The key is combined with the resource name of the ValidatingAdmissionPolicy to construct an audit annotation key: "{ValidatingAdmissionPolicy name}/{key}".</p>
<p>If an admission webhook uses the same resource name as this ValidatingAdmissionPolicy and the same audit annotation key, the annotation key will be identical. In this case, the first annotation written with the key will be included in the audit event and all subsequent annotations with the same key will be discarded.</p>
<p>Required.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>valueExpression</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>valueExpression represents the expression which is evaluated by CEL to produce an audit annotation value. The expression must evaluate to either a string or null value. If the expression evaluates to a string, the audit annotation is included with the string value. If the expression evaluates to null or empty string the audit annotation will be omitted. The valueExpression may be no longer than 5kb in length. If the result of the valueExpression is more than 10kb in length, it will be truncated to 10kb.</p>
<p>If multiple ValidatingAdmissionPolicyBinding resources match an API request, then the valueExpression will be evaluated for each binding. All unique values produced by the valueExpressions will be joined together in a comma-separated list.</p>
<p>Required.</p></td>
</tr>
</tbody>
</table>

## .spec.matchConditions

Description
MatchConditions is a list of conditions that must be met for a request to be validated. Match conditions filter requests that have already been matched by the rules, namespaceSelector, and objectSelector. An empty list of matchConditions matches all requests. There are a maximum of 64 match conditions allowed.

If a parameter object is provided, it can be accessed via the `params` handle in the same manner as validation expressions.

The exact matching logic is (in order): 1. If ANY matchCondition evaluates to FALSE, the policy is skipped. 2. If ALL matchConditions evaluate to TRUE, the policy is evaluated. 3. If any matchCondition evaluates to an error (but none are FALSE): - If failurePolicy=Fail, reject the request - If failurePolicy=Ignore, the policy is skipped

Type
`array`

## .spec.matchConditions\[\]

Description
MatchCondition represents a condition which must by fulfilled for a request to be sent to a webhook.

Type
`object`

Required
- `name`

- `expression`

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
<td style="text-align: left;"><p><code>expression</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Expression represents the expression which will be evaluated by CEL. Must evaluate to bool. CEL expressions have access to the contents of the AdmissionRequest and Authorizer, organized into CEL variables:</p>
<p>'object' - The object from the incoming request. The value is null for DELETE requests. 'oldObject' - The existing object. The value is null for CREATE requests. 'request' - Attributes of the admission request(/pkg/apis/admission/types.go#AdmissionRequest). 'authorizer' - A CEL Authorizer. May be used to perform authorization checks for the principal (user or service account) of the request. See <a href="https://pkg.go.dev/k8s.io/apiserver/pkg/cel/library#Authz">https://pkg.go.dev/k8s.io/apiserver/pkg/cel/library#Authz</a> 'authorizer.requestResource' - A CEL ResourceCheck constructed from the 'authorizer' and configured with the request resource. Documentation on CEL: <a href="https://kubernetes.io/docs/reference/using-api/cel/">https://kubernetes.io/docs/reference/using-api/cel/</a></p>
<p>Required.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>name</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Name is an identifier for this match condition, used for strategic merging of MatchConditions, as well as providing an identifier for logging purposes. A good name should be descriptive of the associated expression. Name must be a qualified name consisting of alphanumeric characters, '-', '<em>' or '.', and must start and end with an alphanumeric character (e.g. 'MyName', or 'my.name', or '123-abc', regex used for validation is '([A-Za-z0-9][-A-Za-z0-9</em>.]*)?[A-Za-z0-9]') with an optional DNS subdomain prefix and '/' (e.g. 'example.com/MyName')</p>
<p>Required.</p></td>
</tr>
</tbody>
</table>

## .spec.matchConstraints

Description
MatchResources decides whether to run the admission control policy on an object based on whether it meets the match criteria. The exclude rules take precedence over include rules (if a resource matches both, it is excluded)

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
<td style="text-align: left;"><p><code>excludeResourceRules</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>ExcludeResourceRules describes what operations on what resources/subresources the ValidatingAdmissionPolicy should not care about. The exclude rules take precedence over include rules (if a resource matches both, it is excluded)</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>excludeResourceRules[]</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>NamedRuleWithOperations is a tuple of Operations and Resources with ResourceNames.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>matchPolicy</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>matchPolicy defines how the "MatchResources" list is used to match incoming requests. Allowed values are "Exact" or "Equivalent".</p>
<p>- Exact: match a request only if it exactly matches a specified rule. For example, if deployments can be modified via apps/v1, apps/v1beta1, and extensions/v1beta1, but "rules" only included <code>apiGroups:["apps"], apiVersions:["v1"], resources: ["deployments"]</code>, a request to apps/v1beta1 or extensions/v1beta1 would not be sent to the ValidatingAdmissionPolicy.</p>
<p>- Equivalent: match a request if modifies a resource listed in rules, even via another API group or version. For example, if deployments can be modified via apps/v1, apps/v1beta1, and extensions/v1beta1, and "rules" only included <code>apiGroups:["apps"], apiVersions:["v1"], resources: ["deployments"]</code>, a request to apps/v1beta1 or extensions/v1beta1 would be converted to apps/v1 and sent to the ValidatingAdmissionPolicy.</p>
<p>Defaults to "Equivalent"</p>
<p>Possible enum values: - <code>"Equivalent"</code> means requests should be sent to the webhook if they modify a resource listed in rules via another API group or version. - <code>"Exact"</code> means requests should only be sent to the webhook if they exactly match a given rule.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>namespaceSelector</code></p></td>
<td style="text-align: left;"><p><a href="../objects/index.xml#io-k8s-apimachinery-pkg-apis-meta-v1-LabelSelector"><code>LabelSelector</code></a></p></td>
<td style="text-align: left;"><p>NamespaceSelector decides whether to run the admission control policy on an object based on whether the namespace for that object matches the selector. If the object itself is a namespace, the matching is performed on object.metadata.labels. If the object is another cluster scoped resource, it never skips the policy.</p>
<p>For example, to run the webhook on any objects whose namespace is not associated with "runlevel" of "0" or "1"; you will set the selector as follows: "namespaceSelector": { "matchExpressions": [ { "key": "runlevel", "operator": "NotIn", "values": [ "0", "1" ] } ] }</p>
<p>If instead you want to only run the policy on any objects whose namespace is associated with the "environment" of "prod" or "staging"; you will set the selector as follows: "namespaceSelector": { "matchExpressions": [ { "key": "environment", "operator": "In", "values": [ "prod", "staging" ] } ] }</p>
<p>See <a href="https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/">https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/</a> for more examples of label selectors.</p>
<p>Default to the empty LabelSelector, which matches everything.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>objectSelector</code></p></td>
<td style="text-align: left;"><p><a href="../objects/index.xml#io-k8s-apimachinery-pkg-apis-meta-v1-LabelSelector"><code>LabelSelector</code></a></p></td>
<td style="text-align: left;"><p>ObjectSelector decides whether to run the validation based on if the object has matching labels. objectSelector is evaluated against both the oldObject and newObject that would be sent to the cel validation, and is considered to match if either object matches the selector. A null object (oldObject in the case of create, or newObject in the case of delete) or an object that cannot have labels (like a DeploymentRollback or a PodProxyOptions object) is not considered to match. Use the object selector only if the webhook is opt-in, because end users may skip the admission webhook by setting the labels. Default to the empty LabelSelector, which matches everything.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>resourceRules</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>ResourceRules describes what operations on what resources/subresources the ValidatingAdmissionPolicy matches. The policy cares about an operation if it matches <em>any</em> Rule.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>resourceRules[]</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>NamedRuleWithOperations is a tuple of Operations and Resources with ResourceNames.</p></td>
</tr>
</tbody>
</table>

## .spec.matchConstraints.excludeResourceRules

Description
ExcludeResourceRules describes what operations on what resources/subresources the ValidatingAdmissionPolicy should not care about. The exclude rules take precedence over include rules (if a resource matches both, it is excluded)

Type
`array`

## .spec.matchConstraints.excludeResourceRules\[\]

Description
NamedRuleWithOperations is a tuple of Operations and Resources with ResourceNames.

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
<td style="text-align: left;"><p><code>apiGroups</code></p></td>
<td style="text-align: left;"><p><code>array (string)</code></p></td>
<td style="text-align: left;"><p>APIGroups is the API groups the resources belong to. '<strong>' is all groups. If '</strong>' is present, the length of the slice must be one. Required.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>apiVersions</code></p></td>
<td style="text-align: left;"><p><code>array (string)</code></p></td>
<td style="text-align: left;"><p>APIVersions is the API versions the resources belong to. '<strong>' is all versions. If '</strong>' is present, the length of the slice must be one. Required.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>operations</code></p></td>
<td style="text-align: left;"><p><code>array (string)</code></p></td>
<td style="text-align: left;"><p>Operations is the operations the admission hook cares about - CREATE, UPDATE, DELETE, CONNECT or * for all of those operations and any future admission operations that are added. If '*' is present, the length of the slice must be one. Required.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>resourceNames</code></p></td>
<td style="text-align: left;"><p><code>array (string)</code></p></td>
<td style="text-align: left;"><p>ResourceNames is an optional white list of names that the rule applies to. An empty set means that everything is allowed.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>resources</code></p></td>
<td style="text-align: left;"><p><code>array (string)</code></p></td>
<td style="text-align: left;"><p>Resources is a list of resources this rule applies to.</p>
<p>For example: 'pods' means pods. 'pods/log' means the log subresource of pods. '<strong>' means all resources, but not subresources. 'pods/</strong>' means all subresources of pods. '<strong>/scale' means all scale subresources. '</strong>/*' means all resources and their subresources.</p>
<p>If wildcard is present, the validation rule will ensure resources do not overlap with each other.</p>
<p>Depending on the enclosing object, subresources might not be allowed. Required.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>scope</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>scope specifies the scope of this rule. Valid values are "Cluster", "Namespaced", and "<strong>" "Cluster" means that only cluster-scoped resources will match this rule. Namespace API objects are cluster-scoped. "Namespaced" means that only namespaced resources will match this rule. "</strong>" means that there are no scope restrictions. Subresources match the scope of their parent resource. Default is "*".</p></td>
</tr>
</tbody>
</table>

## .spec.matchConstraints.resourceRules

Description
ResourceRules describes what operations on what resources/subresources the ValidatingAdmissionPolicy matches. The policy cares about an operation if it matches *any* Rule.

Type
`array`

## .spec.matchConstraints.resourceRules\[\]

Description
NamedRuleWithOperations is a tuple of Operations and Resources with ResourceNames.

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
<td style="text-align: left;"><p><code>apiGroups</code></p></td>
<td style="text-align: left;"><p><code>array (string)</code></p></td>
<td style="text-align: left;"><p>APIGroups is the API groups the resources belong to. '<strong>' is all groups. If '</strong>' is present, the length of the slice must be one. Required.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>apiVersions</code></p></td>
<td style="text-align: left;"><p><code>array (string)</code></p></td>
<td style="text-align: left;"><p>APIVersions is the API versions the resources belong to. '<strong>' is all versions. If '</strong>' is present, the length of the slice must be one. Required.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>operations</code></p></td>
<td style="text-align: left;"><p><code>array (string)</code></p></td>
<td style="text-align: left;"><p>Operations is the operations the admission hook cares about - CREATE, UPDATE, DELETE, CONNECT or * for all of those operations and any future admission operations that are added. If '*' is present, the length of the slice must be one. Required.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>resourceNames</code></p></td>
<td style="text-align: left;"><p><code>array (string)</code></p></td>
<td style="text-align: left;"><p>ResourceNames is an optional white list of names that the rule applies to. An empty set means that everything is allowed.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>resources</code></p></td>
<td style="text-align: left;"><p><code>array (string)</code></p></td>
<td style="text-align: left;"><p>Resources is a list of resources this rule applies to.</p>
<p>For example: 'pods' means pods. 'pods/log' means the log subresource of pods. '<strong>' means all resources, but not subresources. 'pods/</strong>' means all subresources of pods. '<strong>/scale' means all scale subresources. '</strong>/*' means all resources and their subresources.</p>
<p>If wildcard is present, the validation rule will ensure resources do not overlap with each other.</p>
<p>Depending on the enclosing object, subresources might not be allowed. Required.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>scope</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>scope specifies the scope of this rule. Valid values are "Cluster", "Namespaced", and "<strong>" "Cluster" means that only cluster-scoped resources will match this rule. Namespace API objects are cluster-scoped. "Namespaced" means that only namespaced resources will match this rule. "</strong>" means that there are no scope restrictions. Subresources match the scope of their parent resource. Default is "*".</p></td>
</tr>
</tbody>
</table>

## .spec.paramKind

Description
ParamKind is a tuple of Group Kind and Version.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion is the API group version the resources belong to. In format of "group/version". Required. |
| `kind` | `string` | Kind is the API kind the resources belong to. Required. |

## .spec.validations

Description
Validations contain CEL expressions which is used to apply the validation. Validations and AuditAnnotations may not both be empty; a minimum of one Validations or AuditAnnotations is required.

Type
`array`

## .spec.validations\[\]

Description
Validation specifies the CEL expression which is used to apply the validation.

Type
`object`

Required
- `expression`

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
<td style="text-align: left;"><p><code>expression</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Expression represents the expression which will be evaluated by CEL. ref: <a href="https://github.com/google/cel-spec">https://github.com/google/cel-spec</a> CEL expressions have access to the contents of the API request/response, organized into CEL variables as well as some other useful variables:</p>
<p>- 'object' - The object from the incoming request. The value is null for DELETE requests. - 'oldObject' - The existing object. The value is null for CREATE requests. - 'request' - Attributes of the API request([ref](/pkg/apis/admission/types.go#AdmissionRequest)). - 'params' - Parameter resource referred to by the policy binding being evaluated. Only populated if the policy has a ParamKind. - 'namespaceObject' - The namespace object that the incoming object belongs to. The value is null for cluster-scoped resources. - 'variables' - Map of composited variables, from its name to its lazily evaluated value. For example, a variable named 'foo' can be accessed as 'variables.foo'. - 'authorizer' - A CEL Authorizer. May be used to perform authorization checks for the principal (user or service account) of the request. See <a href="https://pkg.go.dev/k8s.io/apiserver/pkg/cel/library#Authz">https://pkg.go.dev/k8s.io/apiserver/pkg/cel/library#Authz</a> - 'authorizer.requestResource' - A CEL ResourceCheck constructed from the 'authorizer' and configured with the request resource.</p>
<p>The <code>apiVersion</code>, <code>kind</code>, <code>metadata.name</code> and <code>metadata.generateName</code> are always accessible from the root of the object. No other metadata properties are accessible.</p>
<p>Only property names of the form <code>[a-zA-Z_.-/][a-zA-Z0-9_.-/]*</code> are accessible. Accessible property names are escaped according to the following rules when accessed in the expression: - '<em>' escapes to '</em>underscores<em>' - '.' escapes to '</em>dot<em>' - '-' escapes to '</em>dash<em>' - '/' escapes to '</em>slash<em>' - Property names that exactly match a CEL RESERVED keyword escape to '</em>{keyword}<em>'. The keywords are: "true", "false", "null", "in", "as", "break", "const", "continue", "else", "for", "function", "if", "import", "let", "loop", "package", "namespace", "return". Examples: - Expression accessing a property named "namespace": {"Expression": "object.</em>namespace <em>&gt; 0"} - Expression accessing a property named "x-prop": {"Expression": "object.x</em>dash<em>prop &gt; 0"} - Expression accessing a property named "redact</em>d": {"Expression": "object.redact<em>underscores</em>d &gt; 0"}</p>
<p>Equality on arrays with list type of 'set' or 'map' ignores element order, i.e. [1, 2] == [2, 1]. Concatenation on arrays with x-kubernetes-list-type use the semantics of the list type: - 'set': <code>X + Y</code> performs a union where the array positions of all elements in <code>X</code> are preserved and non-intersecting elements in <code>Y</code> are appended, retaining their partial order. - 'map': <code>X + Y</code> performs a merge where the array positions of all keys in <code>X</code> are preserved but the values are overwritten by values in <code>Y</code> when the key sets of <code>X</code> and <code>Y</code> intersect. Elements in <code>Y</code> with non-intersecting keys are appended, retaining their partial order. Required.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>message</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Message represents the message displayed when validation fails. The message is required if the Expression contains line breaks. The message must not contain line breaks. If unset, the message is "failed rule: {Rule}". e.g. "must be a URL with the host matching spec.host" If the Expression contains line breaks. Message is required. The message must not contain line breaks. If unset, the message is "failed Expression: {Expression}".</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>messageExpression</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>messageExpression declares a CEL expression that evaluates to the validation failure message that is returned when this rule fails. Since messageExpression is used as a failure message, it must evaluate to a string. If both message and messageExpression are present on a validation, then messageExpression will be used if validation fails. If messageExpression results in a runtime error, the runtime error is logged, and the validation failure message is produced as if the messageExpression field were unset. If messageExpression evaluates to an empty string, a string with only spaces, or a string that contains line breaks, then the validation failure message will also be produced as if the messageExpression field were unset, and the fact that messageExpression produced an empty string/string with only spaces/string with line breaks will be logged. messageExpression has access to all the same variables as the <code>expression</code> except for 'authorizer' and 'authorizer.requestResource'. Example: "object.x must be less than max ("string(params.max)")"</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>reason</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Reason represents a machine-readable description of why this validation failed. If this is the first validation in the list to fail, this reason, as well as the corresponding HTTP response code, are used in the HTTP response to the client. The currently supported reasons are: "Unauthorized", "Forbidden", "Invalid", "RequestEntityTooLarge". If not set, StatusReasonInvalid is used in the response to the client.</p></td>
</tr>
</tbody>
</table>

## .spec.variables

Description
Variables contain definitions of variables that can be used in composition of other expressions. Each variable is defined as a named CEL expression. The variables defined here will be available under `variables` in other expressions of the policy except MatchConditions because MatchConditions are evaluated before the rest of the policy.

The expression of a variable can refer to other variables defined earlier in the list but not those after. Thus, Variables must be sorted by the order of first appearance and acyclic.

Type
`array`

## .spec.variables\[\]

Description
Variable is the definition of a variable that is used for composition. A variable is defined as a named expression.

Type
`object`

Required
- `name`

- `expression`

| Property | Type | Description |
|----|----|----|
| `expression` | `string` | Expression is the expression that will be evaluated as the value of the variable. The CEL expression has access to the same identifiers as the CEL expressions in Validation. |
| `name` | `string` | Name is the name of the variable. The name must be a valid CEL identifier and unique among all variables. The variable can be accessed in other expressions through `variables` For example, if name is "foo", the variable will be available as `variables.foo` |

## .status

Description
ValidatingAdmissionPolicyStatus represents the status of an admission validation policy.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `conditions` | [`array (Condition)`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-Condition) | The conditions represent the latest available observations of a policy’s current state. |
| `observedGeneration` | `integer` | The generation observed by the controller. |
| `typeChecking` | `object` | TypeChecking contains results of type checking the expressions in the ValidatingAdmissionPolicy |

## .status.typeChecking

Description
TypeChecking contains results of type checking the expressions in the ValidatingAdmissionPolicy

Type
`object`

| Property | Type | Description |
|----|----|----|
| `expressionWarnings` | `array` | The type checking warnings for each expression. |
| `expressionWarnings[]` | `object` | ExpressionWarning is a warning information that targets a specific expression. |

## .status.typeChecking.expressionWarnings

Description
The type checking warnings for each expression.

Type
`array`

## .status.typeChecking.expressionWarnings\[\]

Description
ExpressionWarning is a warning information that targets a specific expression.

Type
`object`

Required
- `fieldRef`

- `warning`

| Property | Type | Description |
|----|----|----|
| `fieldRef` | `string` | The path to the field that refers the expression. For example, the reference to the expression of the first item of validations is "spec.validations\[0\].expression" |
| `warning` | `string` | The content of type checking information in a human-readable form. Each line of the warning contains the type that the expression is checked against, followed by the type check error from the compiler. |

# API endpoints

The following API endpoints are available:

- `/apis/admissionregistration.k8s.io/v1/validatingadmissionpolicies`

  - `DELETE`: delete collection of ValidatingAdmissionPolicy

  - `GET`: list or watch objects of kind ValidatingAdmissionPolicy

  - `POST`: create a ValidatingAdmissionPolicy

- `/apis/admissionregistration.k8s.io/v1/watch/validatingadmissionpolicies`

  - `GET`: watch individual changes to a list of ValidatingAdmissionPolicy. deprecated: use the 'watch' parameter with a list operation instead.

- `/apis/admissionregistration.k8s.io/v1/validatingadmissionpolicies/{name}`

  - `DELETE`: delete a ValidatingAdmissionPolicy

  - `GET`: read the specified ValidatingAdmissionPolicy

  - `PATCH`: partially update the specified ValidatingAdmissionPolicy

  - `PUT`: replace the specified ValidatingAdmissionPolicy

- `/apis/admissionregistration.k8s.io/v1/watch/validatingadmissionpolicies/{name}`

  - `GET`: watch changes to an object of kind ValidatingAdmissionPolicy. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.

- `/apis/admissionregistration.k8s.io/v1/validatingadmissionpolicies/{name}/status`

  - `GET`: read status of the specified ValidatingAdmissionPolicy

  - `PATCH`: partially update status of the specified ValidatingAdmissionPolicy

  - `PUT`: replace status of the specified ValidatingAdmissionPolicy

## /apis/admissionregistration.k8s.io/v1/validatingadmissionpolicies

HTTP method
`DELETE`

Description
delete collection of ValidatingAdmissionPolicy

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |

Query parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Status`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`GET`

Description
list or watch objects of kind ValidatingAdmissionPolicy

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ValidatingAdmissionPolicyList`](../objects/index.md#io-k8s-api-admissionregistration-v1-ValidatingAdmissionPolicyList) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`POST`

Description
create a ValidatingAdmissionPolicy

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`ValidatingAdmissionPolicy`](validatingadmissionpolicy-admissionregistration-k8s-io-v1.md#validatingadmissionpolicy-admissionregistration-k8s-io-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ValidatingAdmissionPolicy`](validatingadmissionpolicy-admissionregistration-k8s-io-v1.md#validatingadmissionpolicy-admissionregistration-k8s-io-v1) schema |
| 201 - Created | [`ValidatingAdmissionPolicy`](validatingadmissionpolicy-admissionregistration-k8s-io-v1.md#validatingadmissionpolicy-admissionregistration-k8s-io-v1) schema |
| 202 - Accepted | [`ValidatingAdmissionPolicy`](validatingadmissionpolicy-admissionregistration-k8s-io-v1.md#validatingadmissionpolicy-admissionregistration-k8s-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/admissionregistration.k8s.io/v1/watch/validatingadmissionpolicies

HTTP method
`GET`

Description
watch individual changes to a list of ValidatingAdmissionPolicy. deprecated: use the 'watch' parameter with a list operation instead.

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`WatchEvent`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/admissionregistration.k8s.io/v1/validatingadmissionpolicies/{name}

| Parameter | Type     | Description                           |
|-----------|----------|---------------------------------------|
| `name`    | `string` | name of the ValidatingAdmissionPolicy |

Global path parameters

HTTP method
`DELETE`

Description
delete a ValidatingAdmissionPolicy

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
read the specified ValidatingAdmissionPolicy

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ValidatingAdmissionPolicy`](validatingadmissionpolicy-admissionregistration-k8s-io-v1.md#validatingadmissionpolicy-admissionregistration-k8s-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PATCH`

Description
partially update the specified ValidatingAdmissionPolicy

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ValidatingAdmissionPolicy`](validatingadmissionpolicy-admissionregistration-k8s-io-v1.md#validatingadmissionpolicy-admissionregistration-k8s-io-v1) schema |
| 201 - Created | [`ValidatingAdmissionPolicy`](validatingadmissionpolicy-admissionregistration-k8s-io-v1.md#validatingadmissionpolicy-admissionregistration-k8s-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PUT`

Description
replace the specified ValidatingAdmissionPolicy

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`ValidatingAdmissionPolicy`](validatingadmissionpolicy-admissionregistration-k8s-io-v1.md#validatingadmissionpolicy-admissionregistration-k8s-io-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ValidatingAdmissionPolicy`](validatingadmissionpolicy-admissionregistration-k8s-io-v1.md#validatingadmissionpolicy-admissionregistration-k8s-io-v1) schema |
| 201 - Created | [`ValidatingAdmissionPolicy`](validatingadmissionpolicy-admissionregistration-k8s-io-v1.md#validatingadmissionpolicy-admissionregistration-k8s-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/admissionregistration.k8s.io/v1/watch/validatingadmissionpolicies/{name}

| Parameter | Type     | Description                           |
|-----------|----------|---------------------------------------|
| `name`    | `string` | name of the ValidatingAdmissionPolicy |

Global path parameters

HTTP method
`GET`

Description
watch changes to an object of kind ValidatingAdmissionPolicy. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`WatchEvent`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/admissionregistration.k8s.io/v1/validatingadmissionpolicies/{name}/status

| Parameter | Type     | Description                           |
|-----------|----------|---------------------------------------|
| `name`    | `string` | name of the ValidatingAdmissionPolicy |

Global path parameters

HTTP method
`GET`

Description
read status of the specified ValidatingAdmissionPolicy

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ValidatingAdmissionPolicy`](validatingadmissionpolicy-admissionregistration-k8s-io-v1.md#validatingadmissionpolicy-admissionregistration-k8s-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PATCH`

Description
partially update status of the specified ValidatingAdmissionPolicy

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ValidatingAdmissionPolicy`](validatingadmissionpolicy-admissionregistration-k8s-io-v1.md#validatingadmissionpolicy-admissionregistration-k8s-io-v1) schema |
| 201 - Created | [`ValidatingAdmissionPolicy`](validatingadmissionpolicy-admissionregistration-k8s-io-v1.md#validatingadmissionpolicy-admissionregistration-k8s-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PUT`

Description
replace status of the specified ValidatingAdmissionPolicy

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`ValidatingAdmissionPolicy`](validatingadmissionpolicy-admissionregistration-k8s-io-v1.md#validatingadmissionpolicy-admissionregistration-k8s-io-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ValidatingAdmissionPolicy`](validatingadmissionpolicy-admissionregistration-k8s-io-v1.md#validatingadmissionpolicy-admissionregistration-k8s-io-v1) schema |
| 201 - Created | [`ValidatingAdmissionPolicy`](validatingadmissionpolicy-admissionregistration-k8s-io-v1.md#validatingadmissionpolicy-admissionregistration-k8s-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses
