<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Description
The `PrometheusRule` custom resource definition (CRD) defines \[alerting\](<https://prometheus.io/docs/prometheus/latest/configuration/alerting_rules/>) and \[recording\](<https://prometheus.io/docs/prometheus/latest/configuration/recording_rules/>) rules to be evaluated by `Prometheus` or `ThanosRuler` objects.

`Prometheus` and `ThanosRuler` objects select `PrometheusRule` objects using label and namespace selectors.

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
<td style="text-align: left;"><p>spec defines the specification of desired alerting rule definitions for Prometheus.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>status</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>status defines the status subresource. It is under active development and is updated only when the "StatusForConfigurationResources" feature gate is enabled.</p>
<p>Most recent observed status of the PrometheusRule. Read-only. More info: <a href="https://github.com/kubernetes/community/blob/master/contributors/devel/sig-architecture/api-conventions.md#spec-and-status">https://github.com/kubernetes/community/blob/master/contributors/devel/sig-architecture/api-conventions.md#spec-and-status</a></p></td>
</tr>
</tbody>
</table>

## .spec

Description
spec defines the specification of desired alerting rule definitions for Prometheus.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `groups` | `array` | groups defines the content of Prometheus rule file |
| `groups[]` | `object` | RuleGroup is a list of sequentially evaluated recording and alerting rules. |

## .spec.groups

Description
groups defines the content of Prometheus rule file

Type
`array`

## .spec.groups\[\]

Description
RuleGroup is a list of sequentially evaluated recording and alerting rules.

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
<td style="text-align: left;"><p><code>interval</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>interval defines how often rules in the group are evaluated.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>labels</code></p></td>
<td style="text-align: left;"><p><code>object (string)</code></p></td>
<td style="text-align: left;"><p>labels define the labels to add or overwrite before storing the result for its rules. The labels defined at the rule level take precedence.</p>
<p>It requires Prometheus &gt;= 3.0.0. The field is ignored for Thanos Ruler.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>limit</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p>limit defines the number of alerts an alerting rule and series a recording rule can produce. Limit is supported starting with Prometheus &gt;= 2.31 and Thanos Ruler &gt;= 0.24.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>name</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>name defines the name of the rule group.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>partial_response_strategy</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>partial_response_strategy is only used by ThanosRuler and will be ignored by Prometheus instances. More info: <a href="https://github.com/thanos-io/thanos/blob/main/docs/components/rule.md#partial-response">https://github.com/thanos-io/thanos/blob/main/docs/components/rule.md#partial-response</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>query_offset</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>query_offset defines the offset the rule evaluation timestamp of this particular group by the specified duration into the past.</p>
<p>It requires Prometheus &gt;= v2.53.0. It is not supported for ThanosRuler.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>rules</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>rules defines the list of alerting and recording rules.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>rules[]</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>Rule describes an alerting or recording rule See Prometheus documentation: [alerting](<a href="https://www.prometheus.io/docs/prometheus/latest/configuration/alerting_rules/">https://www.prometheus.io/docs/prometheus/latest/configuration/alerting_rules/</a>) or [recording](<a href="https://www.prometheus.io/docs/prometheus/latest/configuration/recording_rules/#recording-rules">https://www.prometheus.io/docs/prometheus/latest/configuration/recording_rules/#recording-rules</a>) rule</p></td>
</tr>
</tbody>
</table>

## .spec.groups\[\].rules

Description
rules defines the list of alerting and recording rules.

Type
`array`

## .spec.groups\[\].rules\[\]

Description
Rule describes an alerting or recording rule See Prometheus documentation: \[alerting\](<https://www.prometheus.io/docs/prometheus/latest/configuration/alerting_rules/>) or \[recording\](<https://www.prometheus.io/docs/prometheus/latest/configuration/recording_rules/#recording-rules>) rule

Type
`object`

Required
- `expr`

| Property | Type | Description |
|----|----|----|
| `alert` | `string` | alert defines the name of the alert. Must be a valid label value. Only one of `record` and `alert` must be set. |
| `annotations` | `object (string)` | annotations defines annotations to add to each alert. Only valid for alerting rules. |
| `expr` | `integer-or-string` | expr defines the PromQL expression to evaluate. |
| `for` | `string` | for defines how alerts are considered firing once they have been returned for this long. |
| `keep_firing_for` | `string` | keep_firing_for defines how long an alert will continue firing after the condition that triggered it has cleared. |
| `labels` | `object (string)` | labels defines labels to add or overwrite. |
| `record` | `string` | record defines the name of the time series to output to. Must be a valid metric name. Only one of `record` and `alert` must be set. |

## .status

Description
status defines the status subresource. It is under active development and is updated only when the "StatusForConfigurationResources" feature gate is enabled.

Most recent observed status of the PrometheusRule. Read-only. More info: <https://github.com/kubernetes/community/blob/master/contributors/devel/sig-architecture/api-conventions.md#spec-and-status>

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

- `/apis/monitoring.coreos.com/v1/prometheusrules`

  - `GET`: list objects of kind PrometheusRule

- `/apis/monitoring.coreos.com/v1/namespaces/{namespace}/prometheusrules`

  - `DELETE`: delete collection of PrometheusRule

  - `GET`: list objects of kind PrometheusRule

  - `POST`: create a PrometheusRule

- `/apis/monitoring.coreos.com/v1/namespaces/{namespace}/prometheusrules/{name}`

  - `DELETE`: delete a PrometheusRule

  - `GET`: read the specified PrometheusRule

  - `PATCH`: partially update the specified PrometheusRule

  - `PUT`: replace the specified PrometheusRule

- `/apis/monitoring.coreos.com/v1/namespaces/{namespace}/prometheusrules/{name}/status`

  - `GET`: read status of the specified PrometheusRule

  - `PATCH`: partially update status of the specified PrometheusRule

  - `PUT`: replace status of the specified PrometheusRule

## /apis/monitoring.coreos.com/v1/prometheusrules

HTTP method
`GET`

Description
list objects of kind PrometheusRule

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`PrometheusRuleList`](../objects/index.md#com-coreos-monitoring-v1-PrometheusRuleList) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/monitoring.coreos.com/v1/namespaces/{namespace}/prometheusrules

HTTP method
`DELETE`

Description
delete collection of PrometheusRule

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Status`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`GET`

Description
list objects of kind PrometheusRule

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`PrometheusRuleList`](../objects/index.md#com-coreos-monitoring-v1-PrometheusRuleList) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`POST`

Description
create a PrometheusRule

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`PrometheusRule`](prometheusrule-monitoring-coreos-com-v1.md#prometheusrule-monitoring-coreos-com-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`PrometheusRule`](prometheusrule-monitoring-coreos-com-v1.md#prometheusrule-monitoring-coreos-com-v1) schema |
| 201 - Created | [`PrometheusRule`](prometheusrule-monitoring-coreos-com-v1.md#prometheusrule-monitoring-coreos-com-v1) schema |
| 202 - Accepted | [`PrometheusRule`](prometheusrule-monitoring-coreos-com-v1.md#prometheusrule-monitoring-coreos-com-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/monitoring.coreos.com/v1/namespaces/{namespace}/prometheusrules/{name}

| Parameter | Type     | Description                |
|-----------|----------|----------------------------|
| `name`    | `string` | name of the PrometheusRule |

Global path parameters

HTTP method
`DELETE`

Description
delete a PrometheusRule

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
read the specified PrometheusRule

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`PrometheusRule`](prometheusrule-monitoring-coreos-com-v1.md#prometheusrule-monitoring-coreos-com-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PATCH`

Description
partially update the specified PrometheusRule

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`PrometheusRule`](prometheusrule-monitoring-coreos-com-v1.md#prometheusrule-monitoring-coreos-com-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PUT`

Description
replace the specified PrometheusRule

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`PrometheusRule`](prometheusrule-monitoring-coreos-com-v1.md#prometheusrule-monitoring-coreos-com-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`PrometheusRule`](prometheusrule-monitoring-coreos-com-v1.md#prometheusrule-monitoring-coreos-com-v1) schema |
| 201 - Created | [`PrometheusRule`](prometheusrule-monitoring-coreos-com-v1.md#prometheusrule-monitoring-coreos-com-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/monitoring.coreos.com/v1/namespaces/{namespace}/prometheusrules/{name}/status

| Parameter | Type     | Description                |
|-----------|----------|----------------------------|
| `name`    | `string` | name of the PrometheusRule |

Global path parameters

HTTP method
`GET`

Description
read status of the specified PrometheusRule

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`PrometheusRule`](prometheusrule-monitoring-coreos-com-v1.md#prometheusrule-monitoring-coreos-com-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PATCH`

Description
partially update status of the specified PrometheusRule

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`PrometheusRule`](prometheusrule-monitoring-coreos-com-v1.md#prometheusrule-monitoring-coreos-com-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PUT`

Description
replace status of the specified PrometheusRule

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`PrometheusRule`](prometheusrule-monitoring-coreos-com-v1.md#prometheusrule-monitoring-coreos-com-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`PrometheusRule`](prometheusrule-monitoring-coreos-com-v1.md#prometheusrule-monitoring-coreos-com-v1) schema |
| 201 - Created | [`PrometheusRule`](prometheusrule-monitoring-coreos-com-v1.md#prometheusrule-monitoring-coreos-com-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses
