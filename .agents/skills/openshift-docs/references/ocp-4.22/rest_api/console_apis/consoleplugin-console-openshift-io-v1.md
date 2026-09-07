<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Description
ConsolePlugin is an extension for customizing OpenShift web console by dynamically loading code from another service running on the cluster.

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
| `spec` | `object` | spec contains the desired configuration for the console plugin. |

## .spec

Description
spec contains the desired configuration for the console plugin.

Type
`object`

Required
- `backend`

- `displayName`

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
<td style="text-align: left;"><p><code>backend</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>backend holds the configuration of backend which is serving console’s plugin .</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>contentSecurityPolicy</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>contentSecurityPolicy is a list of Content-Security-Policy (CSP) directives for the plugin. Each directive specifies a list of values, appropriate for the given directive type, for example a list of remote endpoints for fetch directives such as ScriptSrc. Console web application uses CSP to detect and mitigate certain types of attacks, such as cross-site scripting (XSS) and data injection attacks. Dynamic plugins should specify this field if need to load assets from outside the cluster or if violation reports are observed. Dynamic plugins should always prefer loading their assets from within the cluster, either by vendoring them, or fetching from a cluster service. CSP violation reports can be viewed in the browser’s console logs during development and testing of the plugin in the OpenShift web console. Available directive types are DefaultSrc, ScriptSrc, StyleSrc, ImgSrc, FontSrc and ConnectSrc. Each of the available directives may be defined only once in the list. The value 'self' is automatically included in all fetch directives by the OpenShift web console’s backend. For more information about the CSP directives, see: <a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Security-Policy">https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Security-Policy</a></p>
<p>The OpenShift web console server aggregates the CSP directives and values across its own default values and all enabled ConsolePlugin CRs, merging them into a single policy string that is sent to the browser via <code>Content-Security-Policy</code> HTTP response header.</p>
<p>Example: ConsolePlugin A directives: script-src: <a href="https://script1.com/">https://script1.com/</a>, <a href="https://script2.com/">https://script2.com/</a> font-src: <a href="https://font1.com/">https://font1.com/</a></p>
<p>ConsolePlugin B directives: script-src: <a href="https://script2.com/">https://script2.com/</a>, <a href="https://script3.com/">https://script3.com/</a> font-src: <a href="https://font2.com/">https://font2.com/</a> img-src: <a href="https://img1.com/">https://img1.com/</a></p>
<p>Unified set of CSP directives, passed to the OpenShift web console server: script-src: <a href="https://script1.com/">https://script1.com/</a>, <a href="https://script2.com/">https://script2.com/</a>, <a href="https://script3.com/">https://script3.com/</a> font-src: <a href="https://font1.com/">https://font1.com/</a>, <a href="https://font2.com/">https://font2.com/</a> img-src: <a href="https://img1.com/">https://img1.com/</a></p>
<p>OpenShift web console server CSP response header: Content-Security-Policy: default-src 'self'; base-uri 'self'; script-src 'self' <a href="https://script1.com/">https://script1.com/</a> <a href="https://script2.com/">https://script2.com/</a> <a href="https://script3.com/">https://script3.com/</a>; font-src 'self' <a href="https://font1.com/">https://font1.com/</a> <a href="https://font2.com/">https://font2.com/</a>; img-src 'self' <a href="https://img1.com/">https://img1.com/</a>; style-src 'self'; frame-src 'none'; object-src 'none'</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>contentSecurityPolicy[]</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>ConsolePluginCSP holds configuration for a specific CSP directive</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>displayName</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>displayName is the display name of the plugin. The dispalyName should be between 1 and 128 characters.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>i18n</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>i18n is the configuration of plugin’s localization resources.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>proxy</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>proxy is a list of proxies that describe various service type to which the plugin needs to connect to.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>proxy[]</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>ConsolePluginProxy holds information on various service types to which console’s backend will proxy the plugin’s requests.</p></td>
</tr>
</tbody>
</table>

## .spec.backend

Description
backend holds the configuration of backend which is serving console’s plugin .

Type
`object`

Required
- `type`

| Property | Type | Description |
|----|----|----|
| `service` | `object` | service is a Kubernetes Service that exposes the plugin using a deployment with an HTTP server. The Service must use HTTPS and Service serving certificate. The console backend will proxy the plugins assets from the Service using the service CA bundle. |
| `type` | `string` | type is the backend type which servers the console’s plugin. Currently only "Service" is supported. |

## .spec.backend.service

Description
service is a Kubernetes Service that exposes the plugin using a deployment with an HTTP server. The Service must use HTTPS and Service serving certificate. The console backend will proxy the plugins assets from the Service using the service CA bundle.

Type
`object`

Required
- `name`

- `namespace`

- `port`

| Property | Type | Description |
|----|----|----|
| `basePath` | `string` | basePath is the path to the plugin’s assets. The primary asset it the manifest file called `plugin-manifest.json`, which is a JSON document that contains metadata about the plugin and the extensions. |
| `name` | `string` | name of Service that is serving the plugin assets. |
| `namespace` | `string` | namespace of Service that is serving the plugin assets. |
| `port` | `integer` | port on which the Service that is serving the plugin is listening to. |

## .spec.contentSecurityPolicy

Description
contentSecurityPolicy is a list of Content-Security-Policy (CSP) directives for the plugin. Each directive specifies a list of values, appropriate for the given directive type, for example a list of remote endpoints for fetch directives such as ScriptSrc. Console web application uses CSP to detect and mitigate certain types of attacks, such as cross-site scripting (XSS) and data injection attacks. Dynamic plugins should specify this field if need to load assets from outside the cluster or if violation reports are observed. Dynamic plugins should always prefer loading their assets from within the cluster, either by vendoring them, or fetching from a cluster service. CSP violation reports can be viewed in the browser’s console logs during development and testing of the plugin in the OpenShift web console. Available directive types are DefaultSrc, ScriptSrc, StyleSrc, ImgSrc, FontSrc and ConnectSrc. Each of the available directives may be defined only once in the list. The value 'self' is automatically included in all fetch directives by the OpenShift web console’s backend. For more information about the CSP directives, see: <https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Security-Policy>

The OpenShift web console server aggregates the CSP directives and values across its own default values and all enabled ConsolePlugin CRs, merging them into a single policy string that is sent to the browser via `Content-Security-Policy` HTTP response header.

Example: ConsolePlugin A directives: script-src: <https://script1.com/>, <https://script2.com/> font-src: <https://font1.com/>

    ConsolePlugin B directives:
      script-src: https://script2.com/, https://script3.com/
      font-src: https://font2.com/
      img-src: https://img1.com/

    Unified set of CSP directives, passed to the OpenShift web console server:
      script-src: https://script1.com/, https://script2.com/, https://script3.com/
      font-src: https://font1.com/, https://font2.com/
      img-src: https://img1.com/

    OpenShift web console server CSP response header:
      Content-Security-Policy: default-src 'self'; base-uri 'self'; script-src 'self' https://script1.com/ https://script2.com/ https://script3.com/; font-src 'self' https://font1.com/ https://font2.com/; img-src 'self' https://img1.com/; style-src 'self'; frame-src 'none'; object-src 'none'

Type
`array`

## .spec.contentSecurityPolicy\[\]

Description
ConsolePluginCSP holds configuration for a specific CSP directive

Type
`object`

Required
- `directive`

- `values`

| Property | Type | Description |
|----|----|----|
| `directive` | `string` | directive specifies which Content-Security-Policy directive to configure. Available directive types are DefaultSrc, ScriptSrc, StyleSrc, ImgSrc, FontSrc and ConnectSrc. DefaultSrc directive serves as a fallback for the other CSP fetch directives. For more information about the DefaultSrc directive, see: <https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Security-Policy/default-src> ScriptSrc directive specifies valid sources for JavaScript. For more information about the ScriptSrc directive, see: <https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Security-Policy/script-src> StyleSrc directive specifies valid sources for stylesheets. For more information about the StyleSrc directive, see: <https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Security-Policy/style-src> ImgSrc directive specifies a valid sources of images and favicons. For more information about the ImgSrc directive, see: <https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Security-Policy/img-src> FontSrc directive specifies valid sources for fonts loaded using @font-face. For more information about the FontSrc directive, see: <https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Security-Policy/font-src> ConnectSrc directive restricts the URLs which can be loaded using script interfaces. For more information about the ConnectSrc directive, see: <https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Security-Policy/connect-src> |
| `values` | `array (string)` | values defines an array of values to append to the console defaults for this directive. Each ConsolePlugin may define their own directives with their values. These will be set by the OpenShift web console’s backend, as part of its Content-Security-Policy header. The array can contain at most 16 values. Each directive value must have a maximum length of 1024 characters and must not contain whitespace, commas (,), semicolons (;) or single quotes ('). The value '\*' is not permitted. Each value in the array must be unique. |

## .spec.i18n

Description
i18n is the configuration of plugin’s localization resources.

Type
`object`

Required
- `loadType`

| Property | Type | Description |
|----|----|----|
| `loadType` | `string` | loadType indicates how the plugin’s localization resource should be loaded. Valid values are Preload, Lazy and the empty string. When set to Preload, all localization resources are fetched when the plugin is loaded. When set to Lazy, localization resources are lazily loaded as and when they are required by the console. When omitted or set to the empty string, the behaviour is equivalent to Lazy type. |

## .spec.proxy

Description
proxy is a list of proxies that describe various service type to which the plugin needs to connect to.

Type
`array`

## .spec.proxy\[\]

Description
ConsolePluginProxy holds information on various service types to which console’s backend will proxy the plugin’s requests.

Type
`object`

Required
- `alias`

- `endpoint`

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
<td style="text-align: left;"><p><code>alias</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>alias is a proxy name that identifies the plugin’s proxy. An alias name should be unique per plugin. The console backend exposes following proxy endpoint:</p>
<p>/api/proxy/plugin/&lt;plugin-name&gt;/&lt;proxy-alias&gt;/&lt;request-path&gt;?&lt;optional-query-parameters&gt;</p>
<p>Request example path:</p>
<p>/api/proxy/plugin/acm/search/pods?namespace=openshift-apiserver</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>authorization</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>authorization provides information about authorization type, which the proxied request should contain</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>caCertificate</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>caCertificate provides the cert authority certificate contents, in case the proxied Service is using custom service CA. By default, the service CA bundle provided by the service-ca operator is used.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>endpoint</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>endpoint provides information about endpoint to which the request is proxied to.</p></td>
</tr>
</tbody>
</table>

## .spec.proxy\[\].endpoint

Description
endpoint provides information about endpoint to which the request is proxied to.

Type
`object`

Required
- `type`

| Property | Type | Description |
|----|----|----|
| `service` | `object` | service is an in-cluster Service that the plugin will connect to. The Service must use HTTPS. The console backend exposes an endpoint in order to proxy communication between the plugin and the Service. Note: service field is required for now, since currently only "Service" type is supported. |
| `type` | `string` | type is the type of the console plugin’s proxy. Currently only "Service" is supported. |

## .spec.proxy\[\].endpoint.service

Description
service is an in-cluster Service that the plugin will connect to. The Service must use HTTPS. The console backend exposes an endpoint in order to proxy communication between the plugin and the Service. Note: service field is required for now, since currently only "Service" type is supported.

Type
`object`

Required
- `name`

- `namespace`

- `port`

| Property | Type | Description |
|----|----|----|
| `name` | `string` | name of Service that the plugin needs to connect to. |
| `namespace` | `string` | namespace of Service that the plugin needs to connect to |
| `port` | `integer` | port on which the Service that the plugin needs to connect to is listening on. |

# API endpoints

The following API endpoints are available:

- `/apis/console.openshift.io/v1/consoleplugins`

  - `DELETE`: delete collection of ConsolePlugin

  - `GET`: list objects of kind ConsolePlugin

  - `POST`: create a ConsolePlugin

- `/apis/console.openshift.io/v1/consoleplugins/{name}`

  - `DELETE`: delete a ConsolePlugin

  - `GET`: read the specified ConsolePlugin

  - `PATCH`: partially update the specified ConsolePlugin

  - `PUT`: replace the specified ConsolePlugin

## /apis/console.openshift.io/v1/consoleplugins

HTTP method
`DELETE`

Description
delete collection of ConsolePlugin

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Status`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`GET`

Description
list objects of kind ConsolePlugin

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ConsolePluginList`](../objects/index.md#io-openshift-console-v1-ConsolePluginList) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`POST`

Description
create a ConsolePlugin

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`ConsolePlugin`](consoleplugin-console-openshift-io-v1.md#consoleplugin-console-openshift-io-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ConsolePlugin`](consoleplugin-console-openshift-io-v1.md#consoleplugin-console-openshift-io-v1) schema |
| 201 - Created | [`ConsolePlugin`](consoleplugin-console-openshift-io-v1.md#consoleplugin-console-openshift-io-v1) schema |
| 202 - Accepted | [`ConsolePlugin`](consoleplugin-console-openshift-io-v1.md#consoleplugin-console-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/console.openshift.io/v1/consoleplugins/{name}

| Parameter | Type     | Description               |
|-----------|----------|---------------------------|
| `name`    | `string` | name of the ConsolePlugin |

Global path parameters

HTTP method
`DELETE`

Description
delete a ConsolePlugin

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
read the specified ConsolePlugin

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ConsolePlugin`](consoleplugin-console-openshift-io-v1.md#consoleplugin-console-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PATCH`

Description
partially update the specified ConsolePlugin

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ConsolePlugin`](consoleplugin-console-openshift-io-v1.md#consoleplugin-console-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PUT`

Description
replace the specified ConsolePlugin

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`ConsolePlugin`](consoleplugin-console-openshift-io-v1.md#consoleplugin-console-openshift-io-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ConsolePlugin`](consoleplugin-console-openshift-io-v1.md#consoleplugin-console-openshift-io-v1) schema |
| 201 - Created | [`ConsolePlugin`](consoleplugin-console-openshift-io-v1.md#consoleplugin-console-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses
