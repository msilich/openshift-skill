<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Description
ValidatingWebhookConfiguration describes the configuration of and admission webhook that accept or reject and object without changing it.

Type
`object`

# Specification

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ObjectMeta`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) | Standard object metadata; More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata>. |
| `webhooks` | `array` | Webhooks is a list of webhooks and the affected resources and operations. |
| `webhooks[]` | `object` | ValidatingWebhook describes an admission webhook and the resources and operations it applies to. |

## .webhooks

Description
Webhooks is a list of webhooks and the affected resources and operations.

Type
`array`

## .webhooks\[\]

Description
ValidatingWebhook describes an admission webhook and the resources and operations it applies to.

Type
`object`

Required
- `name`

- `clientConfig`

- `sideEffects`

- `admissionReviewVersions`

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
<td style="text-align: left;"><p><code>admissionReviewVersions</code></p></td>
<td style="text-align: left;"><p><code>array (string)</code></p></td>
<td style="text-align: left;"><p>AdmissionReviewVersions is an ordered list of preferred <code>AdmissionReview</code> versions the Webhook expects. API server will try to use first version in the list which it supports. If none of the versions specified in this list supported by API server, validation will fail for this object. If a persisted webhook configuration specifies allowed versions and does not include any versions known to the API Server, calls to the webhook will fail and be subject to the failure policy.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>clientConfig</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>WebhookClientConfig contains the information to make a TLS connection with the webhook</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>failurePolicy</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>FailurePolicy defines how unrecognized errors from the admission endpoint are handled - allowed values are Ignore or Fail. Defaults to Fail.</p>
<p>Possible enum values: - <code>"Fail"</code> means that an error calling the webhook causes the admission to fail. - <code>"Ignore"</code> means that an error calling the webhook is ignored.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>matchConditions</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>MatchConditions is a list of conditions that must be met for a request to be sent to this webhook. Match conditions filter requests that have already been matched by the rules, namespaceSelector, and objectSelector. An empty list of matchConditions matches all requests. There are a maximum of 64 match conditions allowed.</p>
<p>The exact matching logic is (in order): 1. If ANY matchCondition evaluates to FALSE, the webhook is skipped. 2. If ALL matchConditions evaluate to TRUE, the webhook is called. 3. If any matchCondition evaluates to an error (but none are FALSE): - If failurePolicy=Fail, reject the request - If failurePolicy=Ignore, the error is ignored and the webhook is skipped</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>matchConditions[]</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>MatchCondition represents a condition which must by fulfilled for a request to be sent to a webhook.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>matchPolicy</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>matchPolicy defines how the "rules" list is used to match incoming requests. Allowed values are "Exact" or "Equivalent".</p>
<p>- Exact: match a request only if it exactly matches a specified rule. For example, if deployments can be modified via apps/v1, apps/v1beta1, and extensions/v1beta1, but "rules" only included <code>apiGroups:["apps"], apiVersions:["v1"], resources: ["deployments"]</code>, a request to apps/v1beta1 or extensions/v1beta1 would not be sent to the webhook.</p>
<p>- Equivalent: match a request if modifies a resource listed in rules, even via another API group or version. For example, if deployments can be modified via apps/v1, apps/v1beta1, and extensions/v1beta1, and "rules" only included <code>apiGroups:["apps"], apiVersions:["v1"], resources: ["deployments"]</code>, a request to apps/v1beta1 or extensions/v1beta1 would be converted to apps/v1 and sent to the webhook.</p>
<p>Defaults to "Equivalent"</p>
<p>Possible enum values: - <code>"Equivalent"</code> means requests should be sent to the webhook if they modify a resource listed in rules via another API group or version. - <code>"Exact"</code> means requests should only be sent to the webhook if they exactly match a given rule.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>name</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>The name of the admission webhook. Name should be fully qualified, e.g., imagepolicy.kubernetes.io, where "imagepolicy" is the name of the webhook, and kubernetes.io is the name of the organization. Required.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>namespaceSelector</code></p></td>
<td style="text-align: left;"><p><a href="../objects/index.xml#io-k8s-apimachinery-pkg-apis-meta-v1-LabelSelector"><code>LabelSelector</code></a></p></td>
<td style="text-align: left;"><p>NamespaceSelector decides whether to run the webhook on an object based on whether the namespace for that object matches the selector. If the object itself is a namespace, the matching is performed on object.metadata.labels. If the object is another cluster scoped resource, it never skips the webhook.</p>
<p>For example, to run the webhook on any objects whose namespace is not associated with "runlevel" of "0" or "1"; you will set the selector as follows: "namespaceSelector": { "matchExpressions": [ { "key": "runlevel", "operator": "NotIn", "values": [ "0", "1" ] } ] }</p>
<p>If instead you want to only run the webhook on any objects whose namespace is associated with the "environment" of "prod" or "staging"; you will set the selector as follows: "namespaceSelector": { "matchExpressions": [ { "key": "environment", "operator": "In", "values": [ "prod", "staging" ] } ] }</p>
<p>See <a href="https://kubernetes.io/docs/concepts/overview/working-with-objects/labels">https://kubernetes.io/docs/concepts/overview/working-with-objects/labels</a> for more examples of label selectors.</p>
<p>Default to the empty LabelSelector, which matches everything.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>objectSelector</code></p></td>
<td style="text-align: left;"><p><a href="../objects/index.xml#io-k8s-apimachinery-pkg-apis-meta-v1-LabelSelector"><code>LabelSelector</code></a></p></td>
<td style="text-align: left;"><p>ObjectSelector decides whether to run the webhook based on if the object has matching labels. objectSelector is evaluated against both the oldObject and newObject that would be sent to the webhook, and is considered to match if either object matches the selector. A null object (oldObject in the case of create, or newObject in the case of delete) or an object that cannot have labels (like a DeploymentRollback or a PodProxyOptions object) is not considered to match. Use the object selector only if the webhook is opt-in, because end users may skip the admission webhook by setting the labels. Default to the empty LabelSelector, which matches everything.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>rules</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>Rules describes what operations on what resources/subresources the webhook cares about. The webhook cares about an operation if it matches <em>any</em> Rule. However, in order to prevent ValidatingAdmissionWebhooks and MutatingAdmissionWebhooks from putting the cluster in a state which cannot be recovered from without completely disabling the plugin, ValidatingAdmissionWebhooks and MutatingAdmissionWebhooks are never called on admission requests for ValidatingWebhookConfiguration and MutatingWebhookConfiguration objects.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>rules[]</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>RuleWithOperations is a tuple of Operations and Resources. It is recommended to make sure that all the tuple expansions are valid.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>sideEffects</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>SideEffects states whether this webhook has side effects. Acceptable values are: None, NoneOnDryRun (webhooks created via v1beta1 may also specify Some or Unknown). Webhooks with side effects MUST implement a reconciliation system, since a request may be rejected by a future step in the admission chain and the side effects therefore need to be undone. Requests with the dryRun attribute will be auto-rejected if they match a webhook with sideEffects == Unknown or Some.</p>
<p>Possible enum values: - <code>"None"</code> means that calling the webhook will have no side effects. - <code>"NoneOnDryRun"</code> means that calling the webhook will possibly have side effects, but if the request being reviewed has the dry-run attribute, the side effects will be suppressed. - <code>"Some"</code> means that calling the webhook will possibly have side effects. If a request with the dry-run attribute would trigger a call to this webhook, the request will instead fail. - <code>"Unknown"</code> means that no information is known about the side effects of calling the webhook. If a request with the dry-run attribute would trigger a call to this webhook, the request will instead fail.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>timeoutSeconds</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p>TimeoutSeconds specifies the timeout for this webhook. After the timeout passes, the webhook call will be ignored or the API call will fail based on the failure policy. The timeout value must be between 1 and 30 seconds. Default to 10 seconds.</p></td>
</tr>
</tbody>
</table>

## .webhooks\[\].clientConfig

Description
WebhookClientConfig contains the information to make a TLS connection with the webhook

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
<td style="text-align: left;"><p><code>caBundle</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p><code>caBundle</code> is a PEM encoded CA bundle which will be used to validate the webhook’s server certificate. If unspecified, system trust roots on the apiserver are used.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>service</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>ServiceReference holds a reference to Service.legacy.k8s.io</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>url</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p><code>url</code> gives the location of the webhook, in standard URL form (<code>scheme://host:port/path</code>). Exactly one of <code>url</code> or <code>service</code> must be specified.</p>
<p>The <code>host</code> should not refer to a service running in the cluster; use the <code>service</code> field instead. The host might be resolved via external DNS in some apiservers (e.g., <code>kube-apiserver</code> cannot resolve in-cluster DNS as that would be a layering violation). <code>host</code> may also be an IP address.</p>
<p>Please note that using <code>localhost</code> or <code>127.0.0.1</code> as a <code>host</code> is risky unless you take great care to run this webhook on all hosts which run an apiserver which might need to make calls to this webhook. Such installs are likely to be non-portable, i.e., not easy to turn up in a new cluster.</p>
<p>The scheme must be "https"; the URL must begin with "https://".</p>
<p>A path is optional, and if present may be any string permissible in a URL. You may use the path to pass an arbitrary string to the webhook, for example, a cluster identifier.</p>
<p>Attempting to use a user or basic auth e.g. "user:password@" is not allowed. Fragments ("#…​") and query parameters ("?…​") are not allowed, either.</p></td>
</tr>
</tbody>
</table>

## .webhooks\[\].clientConfig.service

Description
ServiceReference holds a reference to Service.legacy.k8s.io

Type
`object`

Required
- `namespace`

- `name`

| Property | Type | Description |
|----|----|----|
| `name` | `string` | `name` is the name of the service. Required |
| `namespace` | `string` | `namespace` is the namespace of the service. Required |
| `path` | `string` | `path` is an optional URL path which will be sent in any request to this service. |
| `port` | `integer` | If specified, the port on the service that hosting webhook. Default to 443 for backward compatibility. `port` should be a valid port number (1-65535, inclusive). |

## .webhooks\[\].matchConditions

Description
MatchConditions is a list of conditions that must be met for a request to be sent to this webhook. Match conditions filter requests that have already been matched by the rules, namespaceSelector, and objectSelector. An empty list of matchConditions matches all requests. There are a maximum of 64 match conditions allowed.

The exact matching logic is (in order): 1. If ANY matchCondition evaluates to FALSE, the webhook is skipped. 2. If ALL matchConditions evaluate to TRUE, the webhook is called. 3. If any matchCondition evaluates to an error (but none are FALSE): - If failurePolicy=Fail, reject the request - If failurePolicy=Ignore, the error is ignored and the webhook is skipped

Type
`array`

## .webhooks\[\].matchConditions\[\]

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

## .webhooks\[\].rules

Description
Rules describes what operations on what resources/subresources the webhook cares about. The webhook cares about an operation if it matches *any* Rule. However, in order to prevent ValidatingAdmissionWebhooks and MutatingAdmissionWebhooks from putting the cluster in a state which cannot be recovered from without completely disabling the plugin, ValidatingAdmissionWebhooks and MutatingAdmissionWebhooks are never called on admission requests for ValidatingWebhookConfiguration and MutatingWebhookConfiguration objects.

Type
`array`

## .webhooks\[\].rules\[\]

Description
RuleWithOperations is a tuple of Operations and Resources. It is recommended to make sure that all the tuple expansions are valid.

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

# API endpoints

The following API endpoints are available:

- `/apis/admissionregistration.k8s.io/v1/validatingwebhookconfigurations`

  - `DELETE`: delete collection of ValidatingWebhookConfiguration

  - `GET`: list or watch objects of kind ValidatingWebhookConfiguration

  - `POST`: create a ValidatingWebhookConfiguration

- `/apis/admissionregistration.k8s.io/v1/watch/validatingwebhookconfigurations`

  - `GET`: watch individual changes to a list of ValidatingWebhookConfiguration. deprecated: use the 'watch' parameter with a list operation instead.

- `/apis/admissionregistration.k8s.io/v1/validatingwebhookconfigurations/{name}`

  - `DELETE`: delete a ValidatingWebhookConfiguration

  - `GET`: read the specified ValidatingWebhookConfiguration

  - `PATCH`: partially update the specified ValidatingWebhookConfiguration

  - `PUT`: replace the specified ValidatingWebhookConfiguration

- `/apis/admissionregistration.k8s.io/v1/watch/validatingwebhookconfigurations/{name}`

  - `GET`: watch changes to an object of kind ValidatingWebhookConfiguration. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.

## /apis/admissionregistration.k8s.io/v1/validatingwebhookconfigurations

HTTP method
`DELETE`

Description
delete collection of ValidatingWebhookConfiguration

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
list or watch objects of kind ValidatingWebhookConfiguration

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ValidatingWebhookConfigurationList`](../objects/index.md#io-k8s-api-admissionregistration-v1-ValidatingWebhookConfigurationList) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`POST`

Description
create a ValidatingWebhookConfiguration

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`ValidatingWebhookConfiguration`](validatingwebhookconfiguration-admissionregistration-k8s-io-v1.md#validatingwebhookconfiguration-admissionregistration-k8s-io-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ValidatingWebhookConfiguration`](validatingwebhookconfiguration-admissionregistration-k8s-io-v1.md#validatingwebhookconfiguration-admissionregistration-k8s-io-v1) schema |
| 201 - Created | [`ValidatingWebhookConfiguration`](validatingwebhookconfiguration-admissionregistration-k8s-io-v1.md#validatingwebhookconfiguration-admissionregistration-k8s-io-v1) schema |
| 202 - Accepted | [`ValidatingWebhookConfiguration`](validatingwebhookconfiguration-admissionregistration-k8s-io-v1.md#validatingwebhookconfiguration-admissionregistration-k8s-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/admissionregistration.k8s.io/v1/watch/validatingwebhookconfigurations

HTTP method
`GET`

Description
watch individual changes to a list of ValidatingWebhookConfiguration. deprecated: use the 'watch' parameter with a list operation instead.

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`WatchEvent`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/admissionregistration.k8s.io/v1/validatingwebhookconfigurations/{name}

| Parameter | Type     | Description                                |
|-----------|----------|--------------------------------------------|
| `name`    | `string` | name of the ValidatingWebhookConfiguration |

Global path parameters

HTTP method
`DELETE`

Description
delete a ValidatingWebhookConfiguration

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
read the specified ValidatingWebhookConfiguration

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ValidatingWebhookConfiguration`](validatingwebhookconfiguration-admissionregistration-k8s-io-v1.md#validatingwebhookconfiguration-admissionregistration-k8s-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PATCH`

Description
partially update the specified ValidatingWebhookConfiguration

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ValidatingWebhookConfiguration`](validatingwebhookconfiguration-admissionregistration-k8s-io-v1.md#validatingwebhookconfiguration-admissionregistration-k8s-io-v1) schema |
| 201 - Created | [`ValidatingWebhookConfiguration`](validatingwebhookconfiguration-admissionregistration-k8s-io-v1.md#validatingwebhookconfiguration-admissionregistration-k8s-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PUT`

Description
replace the specified ValidatingWebhookConfiguration

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`ValidatingWebhookConfiguration`](validatingwebhookconfiguration-admissionregistration-k8s-io-v1.md#validatingwebhookconfiguration-admissionregistration-k8s-io-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ValidatingWebhookConfiguration`](validatingwebhookconfiguration-admissionregistration-k8s-io-v1.md#validatingwebhookconfiguration-admissionregistration-k8s-io-v1) schema |
| 201 - Created | [`ValidatingWebhookConfiguration`](validatingwebhookconfiguration-admissionregistration-k8s-io-v1.md#validatingwebhookconfiguration-admissionregistration-k8s-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/admissionregistration.k8s.io/v1/watch/validatingwebhookconfigurations/{name}

| Parameter | Type     | Description                                |
|-----------|----------|--------------------------------------------|
| `name`    | `string` | name of the ValidatingWebhookConfiguration |

Global path parameters

HTTP method
`GET`

Description
watch changes to an object of kind ValidatingWebhookConfiguration. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`WatchEvent`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema |
| 401 - Unauthorized | Empty |

HTTP responses
