<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Description
ValidatingAdmissionPolicyBinding binds the ValidatingAdmissionPolicy with paramerized resources. ValidatingAdmissionPolicyBinding and parameter CRDs together define how cluster administrators configure policies for clusters.

For a given admission request, each binding will cause its policy to be evaluated N times, where N is 1 for policies/bindings that don’t use params, otherwise N is the number of parameters selected by the binding.

The CEL expressions of a policy must have a computed CEL cost below the maximum CEL budget. Each evaluation of the policy is given an independent CEL cost budget. Adding/removing policies, bindings, or params can not affect whether a given (policy, binding, param) combination is within its own CEL budget.

Type
`object`

# Specification

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ObjectMeta`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) | Standard object metadata; More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata>. |
| `spec` | `object` | ValidatingAdmissionPolicyBindingSpec is the specification of the ValidatingAdmissionPolicyBinding. |

## .spec

Description
ValidatingAdmissionPolicyBindingSpec is the specification of the ValidatingAdmissionPolicyBinding.

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
<td style="text-align: left;"><p><code>matchResources</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>MatchResources decides whether to run the admission control policy on an object based on whether it meets the match criteria. The exclude rules take precedence over include rules (if a resource matches both, it is excluded)</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>paramRef</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>ParamRef describes how to locate the params to be used as input to expressions of rules applied by a policy binding.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>policyName</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>PolicyName references a ValidatingAdmissionPolicy name which the ValidatingAdmissionPolicyBinding binds to. If the referenced resource does not exist, this binding is considered invalid and will be ignored Required.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>validationActions</code></p></td>
<td style="text-align: left;"><p><code>array (string)</code></p></td>
<td style="text-align: left;"><p>validationActions declares how Validations of the referenced ValidatingAdmissionPolicy are enforced. If a validation evaluates to false it is always enforced according to these actions.</p>
<p>Failures defined by the ValidatingAdmissionPolicy’s FailurePolicy are enforced according to these actions only if the FailurePolicy is set to Fail, otherwise the failures are ignored. This includes compilation errors, runtime errors and misconfigurations of the policy.</p>
<p>validationActions is declared as a set of action values. Order does not matter. validationActions may not contain duplicates of the same action.</p>
<p>The supported actions values are:</p>
<p>"Deny" specifies that a validation failure results in a denied request.</p>
<p>"Warn" specifies that a validation failure is reported to the request client in HTTP Warning headers, with a warning code of 299. Warnings can be sent both for allowed or denied admission responses.</p>
<p>"Audit" specifies that a validation failure is included in the published audit event for the request. The audit event will contain a <code>validation.policy.admission.k8s.io/validation_failure</code> audit annotation with a value containing the details of the validation failures, formatted as a JSON list of objects, each with the following fields: - message: The validation failure message string - policy: The resource name of the ValidatingAdmissionPolicy - binding: The resource name of the ValidatingAdmissionPolicyBinding - expressionIndex: The index of the failed validations in the ValidatingAdmissionPolicy - validationActions: The enforcement actions enacted for the validation failure Example audit annotation: <code>"validation.policy.admission.k8s.io/validation_failure": "[{\"message\": \"Invalid value\", {\"policy\": \"policy.example.com\", {\"binding\": \"policybinding.example.com\", {\"expressionIndex\": \"1\", {\"validationActions\": [\"Audit\"]}]"</code></p>
<p>Clients should expect to handle additional values by ignoring any values not recognized.</p>
<p>"Deny" and "Warn" may not be used together since this combination needlessly duplicates the validation failure both in the API response body and the HTTP warning headers.</p>
<p>Required.</p></td>
</tr>
</tbody>
</table>

## .spec.matchResources

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

## .spec.matchResources.excludeResourceRules

Description
ExcludeResourceRules describes what operations on what resources/subresources the ValidatingAdmissionPolicy should not care about. The exclude rules take precedence over include rules (if a resource matches both, it is excluded)

Type
`array`

## .spec.matchResources.excludeResourceRules\[\]

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

## .spec.matchResources.resourceRules

Description
ResourceRules describes what operations on what resources/subresources the ValidatingAdmissionPolicy matches. The policy cares about an operation if it matches *any* Rule.

Type
`array`

## .spec.matchResources.resourceRules\[\]

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

## .spec.paramRef

Description
ParamRef describes how to locate the params to be used as input to expressions of rules applied by a policy binding.

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
<td style="text-align: left;"><p><code>name</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>name is the name of the resource being referenced.</p>
<p>One of <code>name</code> or <code>selector</code> must be set, but <code>name</code> and <code>selector</code> are mutually exclusive properties. If one is set, the other must be unset.</p>
<p>A single parameter used for all admission requests can be configured by setting the <code>name</code> field, leaving <code>selector</code> blank, and setting namespace if <code>paramKind</code> is namespace-scoped.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>namespace</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>namespace is the namespace of the referenced resource. Allows limiting the search for params to a specific namespace. Applies to both <code>name</code> and <code>selector</code> fields.</p>
<p>A per-namespace parameter may be used by specifying a namespace-scoped <code>paramKind</code> in the policy and leaving this field empty.</p>
<p>- If <code>paramKind</code> is cluster-scoped, this field MUST be unset. Setting this field results in a configuration error.</p>
<p>- If <code>paramKind</code> is namespace-scoped, the namespace of the object being evaluated for admission will be used when this field is left unset. Take care that if this is left empty the binding must not match any cluster-scoped resources, which will result in an error.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>parameterNotFoundAction</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p><code>parameterNotFoundAction</code> controls the behavior of the binding when the resource exists, and name or selector is valid, but there are no parameters matched by the binding. If the value is set to <code>Allow</code>, then no matched parameters will be treated as successful validation by the binding. If set to <code>Deny</code>, then no matched parameters will be subject to the <code>failurePolicy</code> of the policy.</p>
<p>Allowed values are <code>Allow</code> or <code>Deny</code></p>
<p>Required</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>selector</code></p></td>
<td style="text-align: left;"><p><a href="../objects/index.xml#io-k8s-apimachinery-pkg-apis-meta-v1-LabelSelector"><code>LabelSelector</code></a></p></td>
<td style="text-align: left;"><p>selector can be used to match multiple param objects based on their labels. Supply selector: {} to match all resources of the ParamKind.</p>
<p>If multiple params are found, they are all evaluated with the policy expressions and the results are ANDed together.</p>
<p>One of <code>name</code> or <code>selector</code> must be set, but <code>name</code> and <code>selector</code> are mutually exclusive properties. If one is set, the other must be unset.</p></td>
</tr>
</tbody>
</table>

# API endpoints

The following API endpoints are available:

- `/apis/admissionregistration.k8s.io/v1/validatingadmissionpolicybindings`

  - `DELETE`: delete collection of ValidatingAdmissionPolicyBinding

  - `GET`: list or watch objects of kind ValidatingAdmissionPolicyBinding

  - `POST`: create a ValidatingAdmissionPolicyBinding

- `/apis/admissionregistration.k8s.io/v1/watch/validatingadmissionpolicybindings`

  - `GET`: watch individual changes to a list of ValidatingAdmissionPolicyBinding. deprecated: use the 'watch' parameter with a list operation instead.

- `/apis/admissionregistration.k8s.io/v1/validatingadmissionpolicybindings/{name}`

  - `DELETE`: delete a ValidatingAdmissionPolicyBinding

  - `GET`: read the specified ValidatingAdmissionPolicyBinding

  - `PATCH`: partially update the specified ValidatingAdmissionPolicyBinding

  - `PUT`: replace the specified ValidatingAdmissionPolicyBinding

- `/apis/admissionregistration.k8s.io/v1/watch/validatingadmissionpolicybindings/{name}`

  - `GET`: watch changes to an object of kind ValidatingAdmissionPolicyBinding. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.

## /apis/admissionregistration.k8s.io/v1/validatingadmissionpolicybindings

HTTP method
`DELETE`

Description
delete collection of ValidatingAdmissionPolicyBinding

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
list or watch objects of kind ValidatingAdmissionPolicyBinding

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ValidatingAdmissionPolicyBindingList`](../objects/index.md#io-k8s-api-admissionregistration-v1-ValidatingAdmissionPolicyBindingList) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`POST`

Description
create a ValidatingAdmissionPolicyBinding

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`ValidatingAdmissionPolicyBinding`](validatingadmissionpolicybinding-admissionregistration-k8s-io-v1.md#validatingadmissionpolicybinding-admissionregistration-k8s-io-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ValidatingAdmissionPolicyBinding`](validatingadmissionpolicybinding-admissionregistration-k8s-io-v1.md#validatingadmissionpolicybinding-admissionregistration-k8s-io-v1) schema |
| 201 - Created | [`ValidatingAdmissionPolicyBinding`](validatingadmissionpolicybinding-admissionregistration-k8s-io-v1.md#validatingadmissionpolicybinding-admissionregistration-k8s-io-v1) schema |
| 202 - Accepted | [`ValidatingAdmissionPolicyBinding`](validatingadmissionpolicybinding-admissionregistration-k8s-io-v1.md#validatingadmissionpolicybinding-admissionregistration-k8s-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/admissionregistration.k8s.io/v1/watch/validatingadmissionpolicybindings

HTTP method
`GET`

Description
watch individual changes to a list of ValidatingAdmissionPolicyBinding. deprecated: use the 'watch' parameter with a list operation instead.

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`WatchEvent`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/admissionregistration.k8s.io/v1/validatingadmissionpolicybindings/{name}

| Parameter | Type     | Description                                  |
|-----------|----------|----------------------------------------------|
| `name`    | `string` | name of the ValidatingAdmissionPolicyBinding |

Global path parameters

HTTP method
`DELETE`

Description
delete a ValidatingAdmissionPolicyBinding

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
read the specified ValidatingAdmissionPolicyBinding

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ValidatingAdmissionPolicyBinding`](validatingadmissionpolicybinding-admissionregistration-k8s-io-v1.md#validatingadmissionpolicybinding-admissionregistration-k8s-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PATCH`

Description
partially update the specified ValidatingAdmissionPolicyBinding

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ValidatingAdmissionPolicyBinding`](validatingadmissionpolicybinding-admissionregistration-k8s-io-v1.md#validatingadmissionpolicybinding-admissionregistration-k8s-io-v1) schema |
| 201 - Created | [`ValidatingAdmissionPolicyBinding`](validatingadmissionpolicybinding-admissionregistration-k8s-io-v1.md#validatingadmissionpolicybinding-admissionregistration-k8s-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PUT`

Description
replace the specified ValidatingAdmissionPolicyBinding

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`ValidatingAdmissionPolicyBinding`](validatingadmissionpolicybinding-admissionregistration-k8s-io-v1.md#validatingadmissionpolicybinding-admissionregistration-k8s-io-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ValidatingAdmissionPolicyBinding`](validatingadmissionpolicybinding-admissionregistration-k8s-io-v1.md#validatingadmissionpolicybinding-admissionregistration-k8s-io-v1) schema |
| 201 - Created | [`ValidatingAdmissionPolicyBinding`](validatingadmissionpolicybinding-admissionregistration-k8s-io-v1.md#validatingadmissionpolicybinding-admissionregistration-k8s-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/admissionregistration.k8s.io/v1/watch/validatingadmissionpolicybindings/{name}

| Parameter | Type     | Description                                  |
|-----------|----------|----------------------------------------------|
| `name`    | `string` | name of the ValidatingAdmissionPolicyBinding |

Global path parameters

HTTP method
`GET`

Description
watch changes to an object of kind ValidatingAdmissionPolicyBinding. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`WatchEvent`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema |
| 401 - Unauthorized | Empty |

HTTP responses
