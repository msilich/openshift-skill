<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Description
TemplateInstance requests and records the instantiation of a Template. TemplateInstance is part of an experimental API.

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
| `metadata` | [`ObjectMeta_v2`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta_v2) | metadata is the standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |
| `spec` | `object` | TemplateInstanceSpec describes the desired state of a TemplateInstance. |
| `status` | `object` | TemplateInstanceStatus describes the current state of a TemplateInstance. |

## .spec

Description
TemplateInstanceSpec describes the desired state of a TemplateInstance.

Type
`object`

Required
- `template`

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
<td style="text-align: left;"><p><code>requester</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>TemplateInstanceRequester holds the identity of an agent requesting a template instantiation.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>secret</code></p></td>
<td style="text-align: left;"><p><code>LocalObjectReference_v2</code></p></td>
<td style="text-align: left;"><p>secret is a reference to a Secret object containing the necessary template parameters.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>template</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>Template contains the inputs needed to produce a Config.</p>
<p>Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).</p></td>
</tr>
</tbody>
</table>

## .spec.requester

Description
TemplateInstanceRequester holds the identity of an agent requesting a template instantiation.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `extra` | `object` | extra holds additional information provided by the authenticator. |
| `extra{}` | `array (string)` |  |
| `groups` | `array (string)` | groups represent the groups this user is a part of. |
| `uid` | `string` | uid is a unique value that identifies this user across time; if this user is deleted and another user by the same name is added, they will have different UIDs. |
| `username` | `string` | username uniquely identifies this user among all active users. |

## .spec.requester.extra

Description
extra holds additional information provided by the authenticator.

Type
`object`

## .spec.template

Description
Template contains the inputs needed to produce a Config.

Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).

Type
`object`

Required
- `objects`

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `labels` | `object (string)` | labels is a optional set of labels that are applied to every object during the Template to Config transformation. |
| `message` | `string` | message is an optional instructional message that will be displayed when this template is instantiated. This field should inform the user how to utilize the newly created resources. Parameter substitution will be performed on the message before being displayed so that generated credentials and other parameters can be included in the output. |
| `metadata` | [`ObjectMeta_v2`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta_v2) | metadata is the standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |
| `objects` | [`array (RawExtension)`](../objects/index.md#io-k8s-apimachinery-pkg-runtime-RawExtension) | objects is an array of resources to include in this template. If a namespace value is hardcoded in the object, it will be removed during template instantiation, however if the namespace value is, or contains, a \${PARAMETER_REFERENCE}, the resolved value after parameter substitution will be respected and the object will be created in that namespace. |
| `parameters` | `array` | parameters is an optional array of Parameters used during the Template to Config transformation. |
| `parameters[]` | `object` | Parameter defines a name/value variable that is to be processed during the Template to Config transformation. |

## .spec.template.parameters

Description
parameters is an optional array of Parameters used during the Template to Config transformation.

Type
`array`

## .spec.template.parameters\[\]

Description
Parameter defines a name/value variable that is to be processed during the Template to Config transformation.

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
<td style="text-align: left;"><p><code>description</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Description of a parameter. Optional.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>displayName</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Optional: The name that will show in UI instead of parameter 'Name'</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>from</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>From is an input value for the generator. Optional.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>generate</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>generate specifies the generator to be used to generate random string from an input value specified by From field. The result string is stored into Value field. If empty, no generator is being used, leaving the result Value untouched. Optional.</p>
<p>The only supported generator is "expression", which accepts a "from" value in the form of a simple regular expression containing the range expression "[a-zA-Z0-9]", and the length expression "a{length}".</p>
<p>Examples:</p>
<p>from | value ----------------------------- "test[0-9]{1}x" | "test7x" "[0-1]{8}" | "01001100" "0x[A-F0-9]{4}" | "0xB3AF" "[a-zA-Z0-9]{8}" | "hW4yQU5i"</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>name</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Name must be set and it can be referenced in Template Items using ${PARAMETER_NAME}. Required.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>required</code></p></td>
<td style="text-align: left;"><p><code>boolean</code></p></td>
<td style="text-align: left;"><p>Optional: Indicates the parameter must have a value. Defaults to false.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>value</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Value holds the Parameter data. If specified, the generator will be ignored. The value replaces all occurrences of the Parameter ${Name} expression during the Template to Config transformation. Optional.</p></td>
</tr>
</tbody>
</table>

## .status

Description
TemplateInstanceStatus describes the current state of a TemplateInstance.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `conditions` | `array` | conditions represent the latest available observations of a TemplateInstance’s current state. |
| `conditions[]` | `object` | TemplateInstanceCondition contains condition information for a TemplateInstance. |
| `objects` | `array` | Objects references the objects created by the TemplateInstance. |
| `objects[]` | `object` | TemplateInstanceObject references an object created by a TemplateInstance. |

## .status.conditions

Description
conditions represent the latest available observations of a TemplateInstance’s current state.

Type
`array`

## .status.conditions\[\]

Description
TemplateInstanceCondition contains condition information for a TemplateInstance.

Type
`object`

Required
- `type`

- `status`

- `lastTransitionTime`

- `reason`

- `message`

| Property | Type | Description |
|----|----|----|
| `lastTransitionTime` | [`Time`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-Time) | LastTransitionTime is the last time a condition status transitioned from one state to another. |
| `message` | `string` | Message is a human readable description of the details of the last transition, complementing reason. |
| `reason` | `string` | Reason is a brief machine readable explanation for the condition’s last transition. |
| `status` | `string` | Status of the condition, one of True, False or Unknown. |
| `type` | `string` | Type of the condition, currently Ready or InstantiateFailure. |

## .status.objects

Description
Objects references the objects created by the TemplateInstance.

Type
`array`

## .status.objects\[\]

Description
TemplateInstanceObject references an object created by a TemplateInstance.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `ref` | [`ObjectReference`](../objects/index.md#io-k8s-api-core-v1-ObjectReference) | ref is a reference to the created object. When used under .spec, only name and namespace are used; these can contain references to parameters which will be substituted following the usual rules. |

# API endpoints

The following API endpoints are available:

- `/apis/template.openshift.io/v1/templateinstances`

  - `GET`: list or watch objects of kind TemplateInstance

- `/apis/template.openshift.io/v1/watch/templateinstances`

  - `GET`: watch individual changes to a list of TemplateInstance. deprecated: use the 'watch' parameter with a list operation instead.

- `/apis/template.openshift.io/v1/namespaces/{namespace}/templateinstances`

  - `DELETE`: delete collection of TemplateInstance

  - `GET`: list or watch objects of kind TemplateInstance

  - `POST`: create a TemplateInstance

- `/apis/template.openshift.io/v1/watch/namespaces/{namespace}/templateinstances`

  - `GET`: watch individual changes to a list of TemplateInstance. deprecated: use the 'watch' parameter with a list operation instead.

- `/apis/template.openshift.io/v1/namespaces/{namespace}/templateinstances/{name}`

  - `DELETE`: delete a TemplateInstance

  - `GET`: read the specified TemplateInstance

  - `PATCH`: partially update the specified TemplateInstance

  - `PUT`: replace the specified TemplateInstance

- `/apis/template.openshift.io/v1/watch/namespaces/{namespace}/templateinstances/{name}`

  - `GET`: watch changes to an object of kind TemplateInstance. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.

- `/apis/template.openshift.io/v1/namespaces/{namespace}/templateinstances/{name}/status`

  - `GET`: read status of the specified TemplateInstance

  - `PATCH`: partially update status of the specified TemplateInstance

  - `PUT`: replace status of the specified TemplateInstance

## /apis/template.openshift.io/v1/templateinstances

HTTP method
`GET`

Description
list or watch objects of kind TemplateInstance

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`TemplateInstanceList`](../objects/index.md#com-github-openshift-api-template-v1-TemplateInstanceList) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/template.openshift.io/v1/watch/templateinstances

HTTP method
`GET`

Description
watch individual changes to a list of TemplateInstance. deprecated: use the 'watch' parameter with a list operation instead.

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`WatchEvent`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/template.openshift.io/v1/namespaces/{namespace}/templateinstances

HTTP method
`DELETE`

Description
delete collection of TemplateInstance

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |

Query parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Status_v9`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-Status_v9) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`GET`

Description
list or watch objects of kind TemplateInstance

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`TemplateInstanceList`](../objects/index.md#com-github-openshift-api-template-v1-TemplateInstanceList) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`POST`

Description
create a TemplateInstance

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`TemplateInstance`](templateinstance-template-openshift-io-v1.md#templateinstance-template-openshift-io-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`TemplateInstance`](templateinstance-template-openshift-io-v1.md#templateinstance-template-openshift-io-v1) schema |
| 201 - Created | [`TemplateInstance`](templateinstance-template-openshift-io-v1.md#templateinstance-template-openshift-io-v1) schema |
| 202 - Accepted | [`TemplateInstance`](templateinstance-template-openshift-io-v1.md#templateinstance-template-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/template.openshift.io/v1/watch/namespaces/{namespace}/templateinstances

HTTP method
`GET`

Description
watch individual changes to a list of TemplateInstance. deprecated: use the 'watch' parameter with a list operation instead.

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`WatchEvent`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/template.openshift.io/v1/namespaces/{namespace}/templateinstances/{name}

| Parameter | Type     | Description                  |
|-----------|----------|------------------------------|
| `name`    | `string` | name of the TemplateInstance |

Global path parameters

HTTP method
`DELETE`

Description
delete a TemplateInstance

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |

Query parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Status_v9`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-Status_v9) schema |
| 202 - Accepted | [`Status_v9`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-Status_v9) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`GET`

Description
read the specified TemplateInstance

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`TemplateInstance`](templateinstance-template-openshift-io-v1.md#templateinstance-template-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PATCH`

Description
partially update the specified TemplateInstance

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`TemplateInstance`](templateinstance-template-openshift-io-v1.md#templateinstance-template-openshift-io-v1) schema |
| 201 - Created | [`TemplateInstance`](templateinstance-template-openshift-io-v1.md#templateinstance-template-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PUT`

Description
replace the specified TemplateInstance

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`TemplateInstance`](templateinstance-template-openshift-io-v1.md#templateinstance-template-openshift-io-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`TemplateInstance`](templateinstance-template-openshift-io-v1.md#templateinstance-template-openshift-io-v1) schema |
| 201 - Created | [`TemplateInstance`](templateinstance-template-openshift-io-v1.md#templateinstance-template-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/template.openshift.io/v1/watch/namespaces/{namespace}/templateinstances/{name}

| Parameter | Type     | Description                  |
|-----------|----------|------------------------------|
| `name`    | `string` | name of the TemplateInstance |

Global path parameters

HTTP method
`GET`

Description
watch changes to an object of kind TemplateInstance. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`WatchEvent`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/template.openshift.io/v1/namespaces/{namespace}/templateinstances/{name}/status

| Parameter | Type     | Description                  |
|-----------|----------|------------------------------|
| `name`    | `string` | name of the TemplateInstance |

Global path parameters

HTTP method
`GET`

Description
read status of the specified TemplateInstance

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`TemplateInstance`](templateinstance-template-openshift-io-v1.md#templateinstance-template-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PATCH`

Description
partially update status of the specified TemplateInstance

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`TemplateInstance`](templateinstance-template-openshift-io-v1.md#templateinstance-template-openshift-io-v1) schema |
| 201 - Created | [`TemplateInstance`](templateinstance-template-openshift-io-v1.md#templateinstance-template-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PUT`

Description
replace status of the specified TemplateInstance

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`TemplateInstance`](templateinstance-template-openshift-io-v1.md#templateinstance-template-openshift-io-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`TemplateInstance`](templateinstance-template-openshift-io-v1.md#templateinstance-template-openshift-io-v1) schema |
| 201 - Created | [`TemplateInstance`](templateinstance-template-openshift-io-v1.md#templateinstance-template-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses
