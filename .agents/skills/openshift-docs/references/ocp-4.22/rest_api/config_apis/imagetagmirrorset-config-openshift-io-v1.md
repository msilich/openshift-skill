<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Description
ImageTagMirrorSet holds cluster-wide information about how to handle registry mirror rules on using tag pull specification. When multiple policies are defined, the outcome of the behavior is defined on each field.

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
| `status` | `object` | status contains the observed state of the resource. |

## .spec

Description
spec holds user settable values for configuration

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
<td style="text-align: left;"><p><code>imageTagMirrors</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>imageTagMirrors allows images referenced by image tags in pods to be pulled from alternative mirrored repository locations. The image pull specification provided to the pod will be compared to the source locations described in imageTagMirrors and the image may be pulled down from any of the mirrors in the list instead of the specified repository allowing administrators to choose a potentially faster mirror. To use mirrors to pull images using digest specification only, users should configure a list of mirrors using "ImageDigestMirrorSet" CRD.</p>
<p>If the image pull specification matches the repository of "source" in multiple imagetagmirrorset objects, only the objects which define the most specific namespace match will be used. For example, if there are objects using quay.io/libpod and quay.io/libpod/busybox as the "source", only the objects using quay.io/libpod/busybox are going to apply for pull specification quay.io/libpod/busybox. Each “source” repository is treated independently; configurations for different “source” repositories don’t interact.</p>
<p>If the "mirrors" is not specified, the image will continue to be pulled from the specified repository in the pull spec.</p>
<p>When multiple policies are defined for the same “source” repository, the sets of defined mirrors will be merged together, preserving the relative order of the mirrors, if possible. For example, if policy A has mirrors <code>a, b, c</code> and policy B has mirrors <code>c, d, e</code>, the mirrors will be used in the order <code>a, b, c, d, e</code>. If the orders of mirror entries conflict (e.g. <code>a, b</code> vs. <code>b, a</code>) the configuration is not rejected but the resulting order is unspecified. Users who want to use a deterministic order of mirrors, should configure them into one list of mirrors using the expected order.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>imageTagMirrors[]</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>ImageTagMirrors holds cluster-wide information about how to handle mirrors in the registries config.</p></td>
</tr>
</tbody>
</table>

## .spec.imageTagMirrors

Description
imageTagMirrors allows images referenced by image tags in pods to be pulled from alternative mirrored repository locations. The image pull specification provided to the pod will be compared to the source locations described in imageTagMirrors and the image may be pulled down from any of the mirrors in the list instead of the specified repository allowing administrators to choose a potentially faster mirror. To use mirrors to pull images using digest specification only, users should configure a list of mirrors using "ImageDigestMirrorSet" CRD.

If the image pull specification matches the repository of "source" in multiple imagetagmirrorset objects, only the objects which define the most specific namespace match will be used. For example, if there are objects using quay.io/libpod and quay.io/libpod/busybox as the "source", only the objects using quay.io/libpod/busybox are going to apply for pull specification quay.io/libpod/busybox. Each “source” repository is treated independently; configurations for different “source” repositories don’t interact.

If the "mirrors" is not specified, the image will continue to be pulled from the specified repository in the pull spec.

When multiple policies are defined for the same “source” repository, the sets of defined mirrors will be merged together, preserving the relative order of the mirrors, if possible. For example, if policy A has mirrors `a, b, c` and policy B has mirrors `c, d, e`, the mirrors will be used in the order `a, b, c, d, e`. If the orders of mirror entries conflict (e.g. `a, b` vs. `b, a`) the configuration is not rejected but the resulting order is unspecified. Users who want to use a deterministic order of mirrors, should configure them into one list of mirrors using the expected order.

Type
`array`

## .spec.imageTagMirrors\[\]

Description
ImageTagMirrors holds cluster-wide information about how to handle mirrors in the registries config.

Type
`object`

Required
- `source`

| Property | Type | Description |
|----|----|----|
| `mirrorSourcePolicy` | `string` | mirrorSourcePolicy defines the fallback policy if fails to pull image from the mirrors. If unset, the image will continue to be pulled from the repository in the pull spec. sourcePolicy is valid configuration only when one or more mirrors are in the mirror list. |
| `mirrors` | `array (string)` | mirrors is zero or more locations that may also contain the same images. No mirror will be configured if not specified. Images can be pulled from these mirrors only if they are referenced by their tags. The mirrored location is obtained by replacing the part of the input reference that matches source by the mirrors entry, e.g. for registry.redhat.io/product/repo reference, a (source, mirror) pair \*.redhat.io, mirror.local/redhat causes a mirror.local/redhat/product/repo repository to be used. Pulling images by tag can potentially yield different images, depending on which endpoint we pull from. Configuring a list of mirrors using "ImageDigestMirrorSet" CRD and forcing digest-pulls for mirrors avoids that issue. The order of mirrors in this list is treated as the user’s desired priority, while source is by default considered lower priority than all mirrors. If no mirror is specified or all image pulls from the mirror list fail, the image will continue to be pulled from the repository in the pull spec unless explicitly prohibited by "mirrorSourcePolicy". Other cluster configuration, including (but not limited to) other imageTagMirrors objects, may impact the exact order mirrors are contacted in, or some mirrors may be contacted in parallel, so this should be considered a preference rather than a guarantee of ordering. "mirrors" uses one of the following formats: host\[:port\] host\[:port\]/namespace\[/namespace…\] host\[:port\]/namespace\[/namespace…\]/repo for more information about the format, see the document about the location field: <https://github.com/containers/image/blob/main/docs/containers-registries.conf.5.md#choosing-a-registry-toml-table> |
| `source` | `string` | source matches the repository that users refer to, e.g. in image pull specifications. Setting source to a registry hostname e.g. docker.io. quay.io, or registry.redhat.io, will match the image pull specification of corressponding registry. "source" uses one of the following formats: host\[:port\] host\[:port\]/namespace\[/namespace…\] host\[:port\]/namespace\[/namespace…\]/repo \[\*.\]host for more information about the format, see the document about the location field: <https://github.com/containers/image/blob/main/docs/containers-registries.conf.5.md#choosing-a-registry-toml-table> |

## .status

Description
status contains the observed state of the resource.

Type
`object`

# API endpoints

The following API endpoints are available:

- `/apis/config.openshift.io/v1/imagetagmirrorsets`

  - `DELETE`: delete collection of ImageTagMirrorSet

  - `GET`: list objects of kind ImageTagMirrorSet

  - `POST`: create an ImageTagMirrorSet

- `/apis/config.openshift.io/v1/imagetagmirrorsets/{name}`

  - `DELETE`: delete an ImageTagMirrorSet

  - `GET`: read the specified ImageTagMirrorSet

  - `PATCH`: partially update the specified ImageTagMirrorSet

  - `PUT`: replace the specified ImageTagMirrorSet

- `/apis/config.openshift.io/v1/imagetagmirrorsets/{name}/status`

  - `GET`: read status of the specified ImageTagMirrorSet

  - `PATCH`: partially update status of the specified ImageTagMirrorSet

  - `PUT`: replace status of the specified ImageTagMirrorSet

## /apis/config.openshift.io/v1/imagetagmirrorsets

HTTP method
`DELETE`

Description
delete collection of ImageTagMirrorSet

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Status`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`GET`

Description
list objects of kind ImageTagMirrorSet

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ImageTagMirrorSetList`](../objects/index.md#io-openshift-config-v1-ImageTagMirrorSetList) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`POST`

Description
create an ImageTagMirrorSet

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`ImageTagMirrorSet`](imagetagmirrorset-config-openshift-io-v1.md#imagetagmirrorset-config-openshift-io-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ImageTagMirrorSet`](imagetagmirrorset-config-openshift-io-v1.md#imagetagmirrorset-config-openshift-io-v1) schema |
| 201 - Created | [`ImageTagMirrorSet`](imagetagmirrorset-config-openshift-io-v1.md#imagetagmirrorset-config-openshift-io-v1) schema |
| 202 - Accepted | [`ImageTagMirrorSet`](imagetagmirrorset-config-openshift-io-v1.md#imagetagmirrorset-config-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/config.openshift.io/v1/imagetagmirrorsets/{name}

| Parameter | Type     | Description                   |
|-----------|----------|-------------------------------|
| `name`    | `string` | name of the ImageTagMirrorSet |

Global path parameters

HTTP method
`DELETE`

Description
delete an ImageTagMirrorSet

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
read the specified ImageTagMirrorSet

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ImageTagMirrorSet`](imagetagmirrorset-config-openshift-io-v1.md#imagetagmirrorset-config-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PATCH`

Description
partially update the specified ImageTagMirrorSet

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ImageTagMirrorSet`](imagetagmirrorset-config-openshift-io-v1.md#imagetagmirrorset-config-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PUT`

Description
replace the specified ImageTagMirrorSet

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`ImageTagMirrorSet`](imagetagmirrorset-config-openshift-io-v1.md#imagetagmirrorset-config-openshift-io-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ImageTagMirrorSet`](imagetagmirrorset-config-openshift-io-v1.md#imagetagmirrorset-config-openshift-io-v1) schema |
| 201 - Created | [`ImageTagMirrorSet`](imagetagmirrorset-config-openshift-io-v1.md#imagetagmirrorset-config-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/config.openshift.io/v1/imagetagmirrorsets/{name}/status

| Parameter | Type     | Description                   |
|-----------|----------|-------------------------------|
| `name`    | `string` | name of the ImageTagMirrorSet |

Global path parameters

HTTP method
`GET`

Description
read status of the specified ImageTagMirrorSet

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ImageTagMirrorSet`](imagetagmirrorset-config-openshift-io-v1.md#imagetagmirrorset-config-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PATCH`

Description
partially update status of the specified ImageTagMirrorSet

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ImageTagMirrorSet`](imagetagmirrorset-config-openshift-io-v1.md#imagetagmirrorset-config-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PUT`

Description
replace status of the specified ImageTagMirrorSet

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`ImageTagMirrorSet`](imagetagmirrorset-config-openshift-io-v1.md#imagetagmirrorset-config-openshift-io-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ImageTagMirrorSet`](imagetagmirrorset-config-openshift-io-v1.md#imagetagmirrorset-config-openshift-io-v1) schema |
| 201 - Created | [`ImageTagMirrorSet`](imagetagmirrorset-config-openshift-io-v1.md#imagetagmirrorset-config-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses
