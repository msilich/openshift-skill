<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Description
ConsoleSample is an extension to customizing OpenShift web console by adding samples.

Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).

Type
`object`

Required
- `metadata`

- `spec`

# Specification

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ObjectMeta`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) | Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |
| `spec` | `object` | spec contains configuration for a console sample. |

## .spec

Description
spec contains configuration for a console sample.

Type
`object`

Required
- `abstract`

- `description`

- `source`

- `title`

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
<td style="text-align: left;"><p><code>abstract</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>abstract is a short introduction to the sample.</p>
<p>It is required and must be no more than 100 characters in length.</p>
<p>The abstract is shown on the sample card tile below the title and provider and is limited to three lines of content.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>description</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>description is a long form explanation of the sample.</p>
<p>It is required and can have a maximum length of <strong>4096</strong> characters.</p>
<p>It is a README.md-like content for additional information, links, pre-conditions, and other instructions. It will be rendered as Markdown so that it can contain line breaks, links, and other simple formatting.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>icon</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>icon is an optional base64 encoded image and shown beside the sample title.</p>
<p>The format must follow the data: URL format and can have a maximum size of <strong>10 KB</strong>.</p>
<p>data:[&lt;mediatype&gt;][;base64],&lt;base64 encoded image&gt;</p>
<p>For example:</p>
<p>data:image;base64, plus the base64 encoded image.</p>
<p>Vector images can also be used. SVG icons must start with:</p>
<p>data:image/svg+xml;base64, plus the base64 encoded SVG image.</p>
<p>All sample catalog icons will be shown on a white background (also when the dark theme is used). The web console ensures that different aspect ratios work correctly. Currently, the surface of the icon is at most 40x100px.</p>
<p>For more information on the data URL format, please visit <a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/Data_URLs">https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/Data_URLs</a>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>provider</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>provider is an optional label to honor who provides the sample.</p>
<p>It is optional and must be no more than 50 characters in length.</p>
<p>A provider can be a company like "Red Hat" or an organization like "CNCF" or "Knative".</p>
<p>Currently, the provider is only shown on the sample card tile below the title with the prefix "Provided by "</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>source</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>source defines where to deploy the sample service from. The sample may be sourced from an external git repository or container image.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>tags</code></p></td>
<td style="text-align: left;"><p><code>array (string)</code></p></td>
<td style="text-align: left;"><p>tags are optional string values that can be used to find samples in the samples catalog.</p>
<p>Examples of common tags may be "Java", "Quarkus", etc.</p>
<p>They will be displayed on the samples details page.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>title</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>title is the display name of the sample.</p>
<p>It is required and must be no more than 50 characters in length.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>type</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>type is an optional label to group multiple samples.</p>
<p>It is optional and must be no more than 20 characters in length.</p>
<p>Recommendation is a singular term like "Builder Image", "Devfile" or "Serverless Function".</p>
<p>Currently, the type is shown a badge on the sample card tile in the top right corner.</p></td>
</tr>
</tbody>
</table>

## .spec.source

Description
source defines where to deploy the sample service from. The sample may be sourced from an external git repository or container image.

Type
`object`

Required
- `type`

| Property | Type | Description |
|----|----|----|
| `containerImport` | `object` | containerImport allows the user import a container image. |
| `gitImport` | `object` | gitImport allows the user to import code from a git repository. |
| `type` | `string` | type of the sample, currently supported: "GitImport";"ContainerImport" |

## .spec.source.containerImport

Description
containerImport allows the user import a container image.

Type
`object`

Required
- `image`

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
<td style="text-align: left;"><p><code>image</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>reference to a container image that provides a HTTP service. The service must be exposed on the default port (8080) unless otherwise configured with the port field.</p>
<p>Supported formats: - &lt;repository-name&gt;/&lt;image-name&gt; - docker.io/&lt;repository-name&gt;/&lt;image-name&gt; - quay.io/&lt;repository-name&gt;/&lt;image-name&gt; - quay.io/&lt;repository-name&gt;/&lt;image-name&gt;@sha256:&lt;image hash&gt; - quay.io/&lt;repository-name&gt;/&lt;image-name&gt;:&lt;tag&gt;</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>service</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>service contains configuration for the Service resource created for this sample.</p></td>
</tr>
</tbody>
</table>

## .spec.source.containerImport.service

Description
service contains configuration for the Service resource created for this sample.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `targetPort` | `integer` | targetPort is the port that the service listens on for HTTP requests. This port will be used for Service and Route created for this sample. Port must be in the range 1 to 65535. Default port is 8080. |

## .spec.source.gitImport

Description
gitImport allows the user to import code from a git repository.

Type
`object`

Required
- `repository`

| Property | Type | Description |
|----|----|----|
| `repository` | `object` | repository contains the reference to the actual Git repository. |
| `service` | `object` | service contains configuration for the Service resource created for this sample. |

## .spec.source.gitImport.repository

Description
repository contains the reference to the actual Git repository.

Type
`object`

Required
- `url`

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
<td style="text-align: left;"><p><code>contextDir</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>contextDir is used to specify a directory within the repository to build the component. Must start with <code>/</code> and have a maximum length of 256 characters. When omitted, the default value is to build from the root of the repository.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>revision</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>revision is the git revision at which to clone the git repository Can be used to clone a specific branch, tag or commit SHA. Must be at most 256 characters in length. When omitted the repository’s default branch is used.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>url</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>url of the Git repository that contains a HTTP service. The HTTP service must be exposed on the default port (8080) unless otherwise configured with the port field.</p>
<p>Only public repositories on GitHub, GitLab and Bitbucket are currently supported:</p>
<p>- <a href="https://github.com/&lt;org&gt;/&lt;repository&gt;">https://github.com/&lt;org&gt;/&lt;repository&gt;</a>; - <a href="https://gitlab.com/&lt;org&gt;/&lt;repository&gt;">https://gitlab.com/&lt;org&gt;/&lt;repository&gt;</a>; - <a href="https://bitbucket.org/&lt;org&gt;/&lt;repository&gt;">https://bitbucket.org/&lt;org&gt;/&lt;repository&gt;</a>;</p>
<p>The url must have a maximum length of 256 characters.</p></td>
</tr>
</tbody>
</table>

## .spec.source.gitImport.service

Description
service contains configuration for the Service resource created for this sample.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `targetPort` | `integer` | targetPort is the port that the service listens on for HTTP requests. This port will be used for Service created for this sample. Port must be in the range 1 to 65535. Default port is 8080. |

# API endpoints

The following API endpoints are available:

- `/apis/console.openshift.io/v1/consolesamples`

  - `DELETE`: delete collection of ConsoleSample

  - `GET`: list objects of kind ConsoleSample

  - `POST`: create a ConsoleSample

- `/apis/console.openshift.io/v1/consolesamples/{name}`

  - `DELETE`: delete a ConsoleSample

  - `GET`: read the specified ConsoleSample

  - `PATCH`: partially update the specified ConsoleSample

  - `PUT`: replace the specified ConsoleSample

## /apis/console.openshift.io/v1/consolesamples

HTTP method
`DELETE`

Description
delete collection of ConsoleSample

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Status`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`GET`

Description
list objects of kind ConsoleSample

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ConsoleSampleList`](../objects/index.md#io-openshift-console-v1-ConsoleSampleList) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`POST`

Description
create a ConsoleSample

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`ConsoleSample`](consolesample-console-openshift-io-v1.md#consolesample-console-openshift-io-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ConsoleSample`](consolesample-console-openshift-io-v1.md#consolesample-console-openshift-io-v1) schema |
| 201 - Created | [`ConsoleSample`](consolesample-console-openshift-io-v1.md#consolesample-console-openshift-io-v1) schema |
| 202 - Accepted | [`ConsoleSample`](consolesample-console-openshift-io-v1.md#consolesample-console-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/console.openshift.io/v1/consolesamples/{name}

| Parameter | Type     | Description               |
|-----------|----------|---------------------------|
| `name`    | `string` | name of the ConsoleSample |

Global path parameters

HTTP method
`DELETE`

Description
delete a ConsoleSample

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
read the specified ConsoleSample

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ConsoleSample`](consolesample-console-openshift-io-v1.md#consolesample-console-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PATCH`

Description
partially update the specified ConsoleSample

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ConsoleSample`](consolesample-console-openshift-io-v1.md#consolesample-console-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PUT`

Description
replace the specified ConsoleSample

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`ConsoleSample`](consolesample-console-openshift-io-v1.md#consolesample-console-openshift-io-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ConsoleSample`](consolesample-console-openshift-io-v1.md#consolesample-console-openshift-io-v1) schema |
| 201 - Created | [`ConsoleSample`](consolesample-console-openshift-io-v1.md#consolesample-console-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses
