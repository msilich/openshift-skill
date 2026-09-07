<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Description
InsightsOperator holds cluster-wide information about the Insights Operator. Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).

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
| `spec` | `object` | spec is the specification of the desired behavior of the Insights. |
| `status` | `object` | status is the most recently observed status of the Insights operator. |

## .spec

Description
spec is the specification of the desired behavior of the Insights.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `logLevel` | `string` | logLevel is an intent based logging for an overall component. It does not give fine grained control, but it is a simple way to manage coarse grained logging choices that operators have to interpret for their operands. Valid values are: "Normal", "Debug", "Trace", "TraceAll". Defaults to "Normal". |
| `managementState` | `string` | managementState indicates whether and how the operator should manage the component |
| `observedConfig` | \`\` | observedConfig holds a sparse config that controller has observed from the cluster state. It exists in spec because it is an input to the level for the operator |
| `operatorLogLevel` | `string` | operatorLogLevel is an intent based logging for the operator itself. It does not give fine grained control, but it is a simple way to manage coarse grained logging choices that operators have to interpret for themselves. Valid values are: "Normal", "Debug", "Trace", "TraceAll". Defaults to "Normal". |
| `unsupportedConfigOverrides` | \`\` | unsupportedConfigOverrides holds a sparse config that will override any previously set options. It only needs to be the fields to override it will end up overlaying in the following order: 1. hardcoded defaults 2. observedConfig 3. unsupportedConfigOverrides |

## .status

Description
status is the most recently observed status of the Insights operator.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `conditions` | `array` | conditions is a list of conditions and their status |
| `conditions[]` | `object` | OperatorCondition is just the standard condition fields. |
| `gatherStatus` | `object` | gatherStatus provides basic information about the last Insights data gathering. When omitted, this means no data gathering has taken place yet. |
| `generations` | `array` | generations are used to determine when an item needs to be reconciled or has changed in a way that needs a reaction. |
| `generations[]` | `object` | GenerationStatus keeps track of the generation for a given resource so that decisions about forced updates can be made. |
| `insightsReport` | `object` | insightsReport provides general Insights analysis results. When omitted, this means no data gathering has taken place yet. |
| `observedGeneration` | `integer` | observedGeneration is the last generation change you’ve dealt with |
| `readyReplicas` | `integer` | readyReplicas indicates how many replicas are ready and at the desired state |
| `version` | `string` | version is the level this availability applies to |

## .status.conditions

Description
conditions is a list of conditions and their status

Type
`array`

## .status.conditions\[\]

Description
OperatorCondition is just the standard condition fields.

Type
`object`

| Property             | Type     | Description |
|----------------------|----------|-------------|
| `lastTransitionTime` | `string` |             |
| `message`            | `string` |             |
| `reason`             | `string` |             |
| `status`             | `string` |             |
| `type`               | `string` |             |

## .status.gatherStatus

Description
gatherStatus provides basic information about the last Insights data gathering. When omitted, this means no data gathering has taken place yet.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `gatherers` | `array` | gatherers is a list of active gatherers (and their statuses) in the last gathering. |
| `gatherers[]` | `object` | gathererStatus represents information about a particular data gatherer. |
| `lastGatherDuration` | `string` | lastGatherDuration is the total time taken to process all gatherers during the last gather event. |
| `lastGatherTime` | `string` | lastGatherTime is the last time when Insights data gathering finished. An empty value means that no data has been gathered yet. |

## .status.gatherStatus.gatherers

Description
gatherers is a list of active gatherers (and their statuses) in the last gathering.

Type
`array`

## .status.gatherStatus.gatherers\[\]

Description
gathererStatus represents information about a particular data gatherer.

Type
`object`

Required
- `conditions`

- `lastGatherDuration`

- `name`

| Property | Type | Description |
|----|----|----|
| `conditions` | `array` | conditions provide details on the status of each gatherer. |
| `conditions[]` | `object` | Condition contains details for one aspect of the current state of this API Resource. --- This struct is intended for direct use as an array at the field path .status.conditions. For example, type FooStatus struct{ // Represents the observations of a foo’s current state. // Known .status.conditions.type are: "Available", "Progressing", and "Degraded" // +patchMergeKey=type // +patchStrategy=merge // +listType=map // +listMapKey=type Conditions \[\]metav1.Condition `json:"conditions,omitempty" patchStrategy:"merge" patchMergeKey:"type" protobuf:"bytes,1,rep,name=conditions"` // other fields } |
| `lastGatherDuration` | `string` | lastGatherDuration represents the time spent gathering. |
| `name` | `string` | name is the name of the gatherer. |

## .status.gatherStatus.gatherers\[\].conditions

Description
conditions provide details on the status of each gatherer.

Type
`array`

## .status.gatherStatus.gatherers\[\].conditions\[\]

Description
Condition contains details for one aspect of the current state of this API Resource. --- This struct is intended for direct use as an array at the field path .status.conditions. For example, type FooStatus struct{ // Represents the observations of a foo’s current state. // Known .status.conditions.type are: "Available", "Progressing", and "Degraded" // +patchMergeKey=type // +patchStrategy=merge // +listType=map // +listMapKey=type Conditions \[\]metav1.Condition `json:"conditions,omitempty" patchStrategy:"merge" patchMergeKey:"type" protobuf:"bytes,1,rep,name=conditions"` // other fields }

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
| `type` | `string` | type of condition in CamelCase or in foo.example.com/CamelCase. --- Many .condition.type values are consistent across resources like Available, but because arbitrary conditions can be useful (see .node.status.conditions), the ability to deconflict is important. The regex it matches is (dns1123SubdomainFmt/)?(qualifiedNameFmt) |

## .status.generations

Description
generations are used to determine when an item needs to be reconciled or has changed in a way that needs a reaction.

Type
`array`

## .status.generations\[\]

Description
GenerationStatus keeps track of the generation for a given resource so that decisions about forced updates can be made.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `group` | `string` | group is the group of the thing you’re tracking |
| `hash` | `string` | hash is an optional field set for resources without generation that are content sensitive like secrets and configmaps |
| `lastGeneration` | `integer` | lastGeneration is the last generation of the workload controller involved |
| `name` | `string` | name is the name of the thing you’re tracking |
| `namespace` | `string` | namespace is where the thing you’re tracking is |
| `resource` | `string` | resource is the resource type of the thing you’re tracking |

## .status.insightsReport

Description
insightsReport provides general Insights analysis results. When omitted, this means no data gathering has taken place yet.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `downloadedAt` | `string` | downloadedAt is the time when the last Insights report was downloaded. An empty value means that there has not been any Insights report downloaded yet and it usually appears in disconnected clusters (or clusters when the Insights data gathering is disabled). |
| `healthChecks` | `array` | healthChecks provides basic information about active Insights health checks in a cluster. |
| `healthChecks[]` | `object` | healthCheck represents an Insights health check attributes. |

## .status.insightsReport.healthChecks

Description
healthChecks provides basic information about active Insights health checks in a cluster.

Type
`array`

## .status.insightsReport.healthChecks\[\]

Description
healthCheck represents an Insights health check attributes.

Type
`object`

Required
- `advisorURI`

- `description`

- `state`

- `totalRisk`

| Property | Type | Description |
|----|----|----|
| `advisorURI` | `string` | advisorURI provides the URL link to the Insights Advisor. |
| `description` | `string` | description provides basic description of the healtcheck. |
| `state` | `string` | state determines what the current state of the health check is. Health check is enabled by default and can be disabled by the user in the Insights advisor user interface. |
| `totalRisk` | `integer` | totalRisk of the healthcheck. Indicator of the total risk posed by the detected issue; combination of impact and likelihood. The values can be from 1 to 4, and the higher the number, the more important the issue. |

# API endpoints

The following API endpoints are available:

- `/apis/operator.openshift.io/v1/insightsoperators`

  - `DELETE`: delete collection of InsightsOperator

  - `GET`: list objects of kind InsightsOperator

  - `POST`: create an InsightsOperator

- `/apis/operator.openshift.io/v1/insightsoperators/{name}`

  - `DELETE`: delete an InsightsOperator

  - `GET`: read the specified InsightsOperator

  - `PATCH`: partially update the specified InsightsOperator

  - `PUT`: replace the specified InsightsOperator

- `/apis/operator.openshift.io/v1/insightsoperators/{name}/scale`

  - `GET`: read scale of the specified InsightsOperator

  - `PATCH`: partially update scale of the specified InsightsOperator

  - `PUT`: replace scale of the specified InsightsOperator

- `/apis/operator.openshift.io/v1/insightsoperators/{name}/status`

  - `GET`: read status of the specified InsightsOperator

  - `PATCH`: partially update status of the specified InsightsOperator

  - `PUT`: replace status of the specified InsightsOperator

## /apis/operator.openshift.io/v1/insightsoperators

HTTP method
`DELETE`

Description
delete collection of InsightsOperator

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Status`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`GET`

Description
list objects of kind InsightsOperator

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`InsightsOperatorList`](../objects/index.md#io-openshift-operator-v1-InsightsOperatorList) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`POST`

Description
create an InsightsOperator

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`InsightsOperator`](insightsoperator-operator-openshift-io-v1.md#insightsoperator-operator-openshift-io-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`InsightsOperator`](insightsoperator-operator-openshift-io-v1.md#insightsoperator-operator-openshift-io-v1) schema |
| 201 - Created | [`InsightsOperator`](insightsoperator-operator-openshift-io-v1.md#insightsoperator-operator-openshift-io-v1) schema |
| 202 - Accepted | [`InsightsOperator`](insightsoperator-operator-openshift-io-v1.md#insightsoperator-operator-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/operator.openshift.io/v1/insightsoperators/{name}

| Parameter | Type     | Description                  |
|-----------|----------|------------------------------|
| `name`    | `string` | name of the InsightsOperator |

Global path parameters

HTTP method
`DELETE`

Description
delete an InsightsOperator

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
read the specified InsightsOperator

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`InsightsOperator`](insightsoperator-operator-openshift-io-v1.md#insightsoperator-operator-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PATCH`

Description
partially update the specified InsightsOperator

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`InsightsOperator`](insightsoperator-operator-openshift-io-v1.md#insightsoperator-operator-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PUT`

Description
replace the specified InsightsOperator

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`InsightsOperator`](insightsoperator-operator-openshift-io-v1.md#insightsoperator-operator-openshift-io-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`InsightsOperator`](insightsoperator-operator-openshift-io-v1.md#insightsoperator-operator-openshift-io-v1) schema |
| 201 - Created | [`InsightsOperator`](insightsoperator-operator-openshift-io-v1.md#insightsoperator-operator-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/operator.openshift.io/v1/insightsoperators/{name}/scale

| Parameter | Type     | Description                  |
|-----------|----------|------------------------------|
| `name`    | `string` | name of the InsightsOperator |

Global path parameters

HTTP method
`GET`

Description
read scale of the specified InsightsOperator

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Scale`](../autoscale_apis/scale-autoscaling-v1.md#scale-autoscaling-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PATCH`

Description
partially update scale of the specified InsightsOperator

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
replace scale of the specified InsightsOperator

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

## /apis/operator.openshift.io/v1/insightsoperators/{name}/status

| Parameter | Type     | Description                  |
|-----------|----------|------------------------------|
| `name`    | `string` | name of the InsightsOperator |

Global path parameters

HTTP method
`GET`

Description
read status of the specified InsightsOperator

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`InsightsOperator`](insightsoperator-operator-openshift-io-v1.md#insightsoperator-operator-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PATCH`

Description
partially update status of the specified InsightsOperator

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`InsightsOperator`](insightsoperator-operator-openshift-io-v1.md#insightsoperator-operator-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PUT`

Description
replace status of the specified InsightsOperator

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`InsightsOperator`](insightsoperator-operator-openshift-io-v1.md#insightsoperator-operator-openshift-io-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`InsightsOperator`](insightsoperator-operator-openshift-io-v1.md#insightsoperator-operator-openshift-io-v1) schema |
| 201 - Created | [`InsightsOperator`](insightsoperator-operator-openshift-io-v1.md#insightsoperator-operator-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses
