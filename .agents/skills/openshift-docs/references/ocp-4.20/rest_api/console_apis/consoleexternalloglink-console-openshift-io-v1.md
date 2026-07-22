<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Description
ConsoleExternalLogLink is an extension for customizing OpenShift web console log links.

Compatibility level 2: Stable within a major release for a minimum of 9 months or 3 minor releases (whichever is longer).

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
| `spec` | `object` | ConsoleExternalLogLinkSpec is the desired log link configuration. The log link will appear on the logs tab of the pod details page. |

## .spec

Description
ConsoleExternalLogLinkSpec is the desired log link configuration. The log link will appear on the logs tab of the pod details page.

Type
`object`

Required
- `hrefTemplate`

- `text`

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
<td style="text-align: left;"><p><code>hrefTemplate</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>hrefTemplate is an absolute secure URL (must use https) for the log link including variables to be replaced. Variables are specified in the URL with the format ${variableName}, for instance, ${containerName} and will be replaced with the corresponding values from the resource. Resource is a pod. Supported variables are: - ${resourceName} - name of the resource which containes the logs - ${resourceUID} - UID of the resource which contains the logs - e.g. <code>11111111-2222-3333-4444-555555555555</code> - ${containerName} - name of the resource’s container that contains the logs - ${resourceNamespace} - namespace of the resource that contains the logs - ${resourceNamespaceUID} - namespace UID of the resource that contains the logs - ${podLabels} - JSON representation of labels matching the pod with the logs - e.g. <code>{"key1":"value1","key2":"value2"}</code></p>
<p>e.g., <a href="https://example.com/logs?resourceName=${resourceName}&amp;containerName=${containerName}&amp;resourceNamespace=${resourceNamespace}&amp;podLabels=${podLabels}">https://example.com/logs?resourceName=${resourceName}&amp;containerName=${containerName}&amp;resourceNamespace=${resourceNamespace}&amp;podLabels=${podLabels}</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>namespaceFilter</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>namespaceFilter is a regular expression used to restrict a log link to a matching set of namespaces (e.g., <code>^openshift-</code>). The string is converted into a regular expression using the JavaScript RegExp constructor. If not specified, links will be displayed for all the namespaces.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>text</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>text is the display text for the link</p></td>
</tr>
</tbody>
</table>

# API endpoints

The following API endpoints are available:

- `/apis/console.openshift.io/v1/consoleexternalloglinks`

  - `DELETE`: delete collection of ConsoleExternalLogLink

  - `GET`: list objects of kind ConsoleExternalLogLink

  - `POST`: create a ConsoleExternalLogLink

- `/apis/console.openshift.io/v1/consoleexternalloglinks/{name}`

  - `DELETE`: delete a ConsoleExternalLogLink

  - `GET`: read the specified ConsoleExternalLogLink

  - `PATCH`: partially update the specified ConsoleExternalLogLink

  - `PUT`: replace the specified ConsoleExternalLogLink

- `/apis/console.openshift.io/v1/consoleexternalloglinks/{name}/status`

  - `GET`: read status of the specified ConsoleExternalLogLink

  - `PATCH`: partially update status of the specified ConsoleExternalLogLink

  - `PUT`: replace status of the specified ConsoleExternalLogLink

## /apis/console.openshift.io/v1/consoleexternalloglinks

HTTP method
`DELETE`

Description
delete collection of ConsoleExternalLogLink

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Status`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`GET`

Description
list objects of kind ConsoleExternalLogLink

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ConsoleExternalLogLinkList`](../objects/index.md#io-openshift-console-v1-ConsoleExternalLogLinkList) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`POST`

Description
create a ConsoleExternalLogLink

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`ConsoleExternalLogLink`](consoleexternalloglink-console-openshift-io-v1.md#consoleexternalloglink-console-openshift-io-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ConsoleExternalLogLink`](consoleexternalloglink-console-openshift-io-v1.md#consoleexternalloglink-console-openshift-io-v1) schema |
| 201 - Created | [`ConsoleExternalLogLink`](consoleexternalloglink-console-openshift-io-v1.md#consoleexternalloglink-console-openshift-io-v1) schema |
| 202 - Accepted | [`ConsoleExternalLogLink`](consoleexternalloglink-console-openshift-io-v1.md#consoleexternalloglink-console-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/console.openshift.io/v1/consoleexternalloglinks/{name}

| Parameter | Type     | Description                        |
|-----------|----------|------------------------------------|
| `name`    | `string` | name of the ConsoleExternalLogLink |

Global path parameters

HTTP method
`DELETE`

Description
delete a ConsoleExternalLogLink

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
read the specified ConsoleExternalLogLink

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ConsoleExternalLogLink`](consoleexternalloglink-console-openshift-io-v1.md#consoleexternalloglink-console-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PATCH`

Description
partially update the specified ConsoleExternalLogLink

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ConsoleExternalLogLink`](consoleexternalloglink-console-openshift-io-v1.md#consoleexternalloglink-console-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PUT`

Description
replace the specified ConsoleExternalLogLink

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`ConsoleExternalLogLink`](consoleexternalloglink-console-openshift-io-v1.md#consoleexternalloglink-console-openshift-io-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ConsoleExternalLogLink`](consoleexternalloglink-console-openshift-io-v1.md#consoleexternalloglink-console-openshift-io-v1) schema |
| 201 - Created | [`ConsoleExternalLogLink`](consoleexternalloglink-console-openshift-io-v1.md#consoleexternalloglink-console-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/console.openshift.io/v1/consoleexternalloglinks/{name}/status

| Parameter | Type     | Description                        |
|-----------|----------|------------------------------------|
| `name`    | `string` | name of the ConsoleExternalLogLink |

Global path parameters

HTTP method
`GET`

Description
read status of the specified ConsoleExternalLogLink

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ConsoleExternalLogLink`](consoleexternalloglink-console-openshift-io-v1.md#consoleexternalloglink-console-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PATCH`

Description
partially update status of the specified ConsoleExternalLogLink

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ConsoleExternalLogLink`](consoleexternalloglink-console-openshift-io-v1.md#consoleexternalloglink-console-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PUT`

Description
replace status of the specified ConsoleExternalLogLink

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`ConsoleExternalLogLink`](consoleexternalloglink-console-openshift-io-v1.md#consoleexternalloglink-console-openshift-io-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ConsoleExternalLogLink`](consoleexternalloglink-console-openshift-io-v1.md#consoleexternalloglink-console-openshift-io-v1) schema |
| 201 - Created | [`ConsoleExternalLogLink`](consoleexternalloglink-console-openshift-io-v1.md#consoleexternalloglink-console-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses
