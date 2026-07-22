<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Description
Image governs policies related to imagestream imports and runtime configuration for external registries. It allows cluster admins to configure which registries OpenShift is allowed to import images from, extra CA trust bundles for external registries, and policies to block or allow registry hostnames. When exposing OpenShift’s image registry to the public, this also lets cluster admins specify the external hostname.

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
| `metadata` | [`ObjectMeta`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) | Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |
| `spec` | `object` | spec holds user settable values for configuration |
| `status` | `object` | status holds observed values from the cluster. They may not be overridden. |

## .spec

Description
spec holds user settable values for configuration

Type
`object`

| Property | Type | Description |
|----|----|----|
| `additionalTrustedCA` | `object` | additionalTrustedCA is a reference to a ConfigMap containing additional CAs that should be trusted during imagestream import, pod image pull, build image pull, and imageregistry pullthrough. The namespace for this config map is openshift-config. |
| `allowedRegistriesForImport` | `array` | allowedRegistriesForImport limits the container image registries that normal users may import images from. Set this list to the registries that you trust to contain valid Docker images and that you want applications to be able to import from. Users with permission to create Images or ImageStreamMappings via the API are not affected by this policy - typically only administrators or system integrations will have those permissions. |
| `allowedRegistriesForImport[]` | `object` | RegistryLocation contains a location of the registry specified by the registry domain name. The domain name might include wildcards, like '\*' or '??'. |
| `externalRegistryHostnames` | `array (string)` | externalRegistryHostnames provides the hostnames for the default external image registry. The external hostname should be set only when the image registry is exposed externally. The first value is used in 'publicDockerImageRepository' field in ImageStreams. The value must be in "hostname\[:port\]" format. |
| `registrySources` | `object` | registrySources contains configuration that determines how the container runtime should treat individual registries when accessing images for builds+pods. (e.g. whether or not to allow insecure access). It does not contain configuration for the internal cluster registry. |

## .spec.additionalTrustedCA

Description
additionalTrustedCA is a reference to a ConfigMap containing additional CAs that should be trusted during imagestream import, pod image pull, build image pull, and imageregistry pullthrough. The namespace for this config map is openshift-config.

Type
`object`

Required
- `name`

| Property | Type     | Description                                            |
|----------|----------|--------------------------------------------------------|
| `name`   | `string` | name is the metadata.name of the referenced config map |

## .spec.allowedRegistriesForImport

Description
allowedRegistriesForImport limits the container image registries that normal users may import images from. Set this list to the registries that you trust to contain valid Docker images and that you want applications to be able to import from. Users with permission to create Images or ImageStreamMappings via the API are not affected by this policy - typically only administrators or system integrations will have those permissions.

Type
`array`

## .spec.allowedRegistriesForImport\[\]

Description
RegistryLocation contains a location of the registry specified by the registry domain name. The domain name might include wildcards, like '\*' or '??'.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `domainName` | `string` | domainName specifies a domain name for the registry In case the registry use non-standard (80 or 443) port, the port should be included in the domain name as well. |
| `insecure` | `boolean` | insecure indicates whether the registry is secure (https) or insecure (http) By default (if not specified) the registry is assumed as secure. |

## .spec.registrySources

Description
registrySources contains configuration that determines how the container runtime should treat individual registries when accessing images for builds+pods. (e.g. whether or not to allow insecure access). It does not contain configuration for the internal cluster registry.

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
<td style="text-align: left;"><p><code>allowedRegistries</code></p></td>
<td style="text-align: left;"><p><code>array (string)</code></p></td>
<td style="text-align: left;"><p>allowedRegistries are the only registries permitted for image pull and push actions. All other registries are denied.</p>
<p>Only one of BlockedRegistries or AllowedRegistries may be set.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>blockedRegistries</code></p></td>
<td style="text-align: left;"><p><code>array (string)</code></p></td>
<td style="text-align: left;"><p>blockedRegistries cannot be used for image pull and push actions. All other registries are permitted.</p>
<p>Only one of BlockedRegistries or AllowedRegistries may be set.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>containerRuntimeSearchRegistries</code></p></td>
<td style="text-align: left;"><p><code>array (string)</code></p></td>
<td style="text-align: left;"><p>containerRuntimeSearchRegistries are registries that will be searched when pulling images that do not have fully qualified domains in their pull specs. Registries will be searched in the order provided in the list. Note: this search list only works with the container runtime, i.e CRI-O. Will NOT work with builds or imagestream imports.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>insecureRegistries</code></p></td>
<td style="text-align: left;"><p><code>array (string)</code></p></td>
<td style="text-align: left;"><p>insecureRegistries are registries which do not have a valid TLS certificates or only support HTTP connections.</p></td>
</tr>
</tbody>
</table>

## .status

Description
status holds observed values from the cluster. They may not be overridden.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `externalRegistryHostnames` | `array (string)` | externalRegistryHostnames provides the hostnames for the default external image registry. The external hostname should be set only when the image registry is exposed externally. The first value is used in 'publicDockerImageRepository' field in ImageStreams. The value must be in "hostname\[:port\]" format. |
| `internalRegistryHostname` | `string` | internalRegistryHostname sets the hostname for the default internal image registry. The value must be in "hostname\[:port\]" format. This value is set by the image registry operator which controls the internal registry hostname. |

# API endpoints

The following API endpoints are available:

- `/apis/config.openshift.io/v1/images`

  - `DELETE`: delete collection of Image

  - `GET`: list objects of kind Image

  - `POST`: create an Image

- `/apis/config.openshift.io/v1/images/{name}`

  - `DELETE`: delete an Image

  - `GET`: read the specified Image

  - `PATCH`: partially update the specified Image

  - `PUT`: replace the specified Image

- `/apis/config.openshift.io/v1/images/{name}/status`

  - `GET`: read status of the specified Image

  - `PATCH`: partially update status of the specified Image

  - `PUT`: replace status of the specified Image

## /apis/config.openshift.io/v1/images

HTTP method
`DELETE`

Description
delete collection of Image

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Status`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`GET`

Description
list objects of kind Image

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ImageList`](../objects/index.md#io-openshift-config-v1-ImageList) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`POST`

Description
create an Image

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`Image`](image-config-openshift-io-v1.md#image-config-openshift-io-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Image`](image-config-openshift-io-v1.md#image-config-openshift-io-v1) schema |
| 201 - Created | [`Image`](image-config-openshift-io-v1.md#image-config-openshift-io-v1) schema |
| 202 - Accepted | [`Image`](image-config-openshift-io-v1.md#image-config-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/config.openshift.io/v1/images/{name}

| Parameter | Type     | Description       |
|-----------|----------|-------------------|
| `name`    | `string` | name of the Image |

Global path parameters

HTTP method
`DELETE`

Description
delete an Image

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
read the specified Image

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Image`](image-config-openshift-io-v1.md#image-config-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PATCH`

Description
partially update the specified Image

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Image`](image-config-openshift-io-v1.md#image-config-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PUT`

Description
replace the specified Image

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`Image`](image-config-openshift-io-v1.md#image-config-openshift-io-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Image`](image-config-openshift-io-v1.md#image-config-openshift-io-v1) schema |
| 201 - Created | [`Image`](image-config-openshift-io-v1.md#image-config-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/config.openshift.io/v1/images/{name}/status

| Parameter | Type     | Description       |
|-----------|----------|-------------------|
| `name`    | `string` | name of the Image |

Global path parameters

HTTP method
`GET`

Description
read status of the specified Image

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Image`](image-config-openshift-io-v1.md#image-config-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PATCH`

Description
partially update status of the specified Image

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Image`](image-config-openshift-io-v1.md#image-config-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PUT`

Description
replace status of the specified Image

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`Image`](image-config-openshift-io-v1.md#image-config-openshift-io-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Image`](image-config-openshift-io-v1.md#image-config-openshift-io-v1) schema |
| 201 - Created | [`Image`](image-config-openshift-io-v1.md#image-config-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses
