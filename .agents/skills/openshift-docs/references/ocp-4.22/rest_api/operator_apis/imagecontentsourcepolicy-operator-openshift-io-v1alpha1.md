<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Description
ImageContentSourcePolicy holds cluster-wide information about how to handle registry mirror rules. When multiple policies are defined, the outcome of the behavior is defined on each field.

Compatibility level 4: No compatibility is provided, the API can change at any point for any reason. These capabilities should not be used by applications needing long term support.

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
<td style="text-align: left;"><p><code>repositoryDigestMirrors</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>repositoryDigestMirrors allows images referenced by image digests in pods to be pulled from alternative mirrored repository locations. The image pull specification provided to the pod will be compared to the source locations described in RepositoryDigestMirrors and the image may be pulled down from any of the mirrors in the list instead of the specified repository allowing administrators to choose a potentially faster mirror. Only image pull specifications that have an image digest will have this behavior applied to them - tags will continue to be pulled from the specified repository in the pull spec.</p>
<p>Each “source” repository is treated independently; configurations for different “source” repositories don’t interact.</p>
<p>When multiple policies are defined for the same “source” repository, the sets of defined mirrors will be merged together, preserving the relative order of the mirrors, if possible. For example, if policy A has mirrors <code>a, b, c</code> and policy B has mirrors <code>c, d, e</code>, the mirrors will be used in the order <code>a, b, c, d, e</code>. If the orders of mirror entries conflict (e.g. <code>a, b</code> vs. <code>b, a</code>) the configuration is not rejected but the resulting order is unspecified.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>repositoryDigestMirrors[]</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>RepositoryDigestMirrors holds cluster-wide information about how to handle mirros in the registries config. Note: the mirrors only work when pulling the images that are referenced by their digests.</p></td>
</tr>
</tbody>
</table>

## .spec.repositoryDigestMirrors

Description
repositoryDigestMirrors allows images referenced by image digests in pods to be pulled from alternative mirrored repository locations. The image pull specification provided to the pod will be compared to the source locations described in RepositoryDigestMirrors and the image may be pulled down from any of the mirrors in the list instead of the specified repository allowing administrators to choose a potentially faster mirror. Only image pull specifications that have an image digest will have this behavior applied to them - tags will continue to be pulled from the specified repository in the pull spec.

Each “source” repository is treated independently; configurations for different “source” repositories don’t interact.

When multiple policies are defined for the same “source” repository, the sets of defined mirrors will be merged together, preserving the relative order of the mirrors, if possible. For example, if policy A has mirrors `a, b, c` and policy B has mirrors `c, d, e`, the mirrors will be used in the order `a, b, c, d, e`. If the orders of mirror entries conflict (e.g. `a, b` vs. `b, a`) the configuration is not rejected but the resulting order is unspecified.

Type
`array`

## .spec.repositoryDigestMirrors\[\]

Description
RepositoryDigestMirrors holds cluster-wide information about how to handle mirros in the registries config. Note: the mirrors only work when pulling the images that are referenced by their digests.

Type
`object`

Required
- `source`

| Property | Type | Description |
|----|----|----|
| `mirrors` | `array (string)` | mirrors is one or more repositories that may also contain the same images. The order of mirrors in this list is treated as the user’s desired priority, while source is by default considered lower priority than all mirrors. Other cluster configuration, including (but not limited to) other repositoryDigestMirrors objects, may impact the exact order mirrors are contacted in, or some mirrors may be contacted in parallel, so this should be considered a preference rather than a guarantee of ordering. |
| `source` | `string` | source is the repository that users refer to, e.g. in image pull specifications. |

# API endpoints

The following API endpoints are available:

- `/apis/operator.openshift.io/v1alpha1/imagecontentsourcepolicies`

  - `DELETE`: delete collection of ImageContentSourcePolicy

  - `GET`: list objects of kind ImageContentSourcePolicy

  - `POST`: create an ImageContentSourcePolicy

- `/apis/operator.openshift.io/v1alpha1/imagecontentsourcepolicies/{name}`

  - `DELETE`: delete an ImageContentSourcePolicy

  - `GET`: read the specified ImageContentSourcePolicy

  - `PATCH`: partially update the specified ImageContentSourcePolicy

  - `PUT`: replace the specified ImageContentSourcePolicy

- `/apis/operator.openshift.io/v1alpha1/imagecontentsourcepolicies/{name}/status`

  - `GET`: read status of the specified ImageContentSourcePolicy

  - `PATCH`: partially update status of the specified ImageContentSourcePolicy

  - `PUT`: replace status of the specified ImageContentSourcePolicy

## /apis/operator.openshift.io/v1alpha1/imagecontentsourcepolicies

HTTP method
`DELETE`

Description
delete collection of ImageContentSourcePolicy

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Status`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`GET`

Description
list objects of kind ImageContentSourcePolicy

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ImageContentSourcePolicyList`](../objects/index.md#io-openshift-operator-v1alpha1-ImageContentSourcePolicyList) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`POST`

Description
create an ImageContentSourcePolicy

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`ImageContentSourcePolicy`](imagecontentsourcepolicy-operator-openshift-io-v1alpha1.md#imagecontentsourcepolicy-operator-openshift-io-v1alpha1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ImageContentSourcePolicy`](imagecontentsourcepolicy-operator-openshift-io-v1alpha1.md#imagecontentsourcepolicy-operator-openshift-io-v1alpha1) schema |
| 201 - Created | [`ImageContentSourcePolicy`](imagecontentsourcepolicy-operator-openshift-io-v1alpha1.md#imagecontentsourcepolicy-operator-openshift-io-v1alpha1) schema |
| 202 - Accepted | [`ImageContentSourcePolicy`](imagecontentsourcepolicy-operator-openshift-io-v1alpha1.md#imagecontentsourcepolicy-operator-openshift-io-v1alpha1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/operator.openshift.io/v1alpha1/imagecontentsourcepolicies/{name}

| Parameter | Type     | Description                          |
|-----------|----------|--------------------------------------|
| `name`    | `string` | name of the ImageContentSourcePolicy |

Global path parameters

HTTP method
`DELETE`

Description
delete an ImageContentSourcePolicy

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
read the specified ImageContentSourcePolicy

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ImageContentSourcePolicy`](imagecontentsourcepolicy-operator-openshift-io-v1alpha1.md#imagecontentsourcepolicy-operator-openshift-io-v1alpha1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PATCH`

Description
partially update the specified ImageContentSourcePolicy

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ImageContentSourcePolicy`](imagecontentsourcepolicy-operator-openshift-io-v1alpha1.md#imagecontentsourcepolicy-operator-openshift-io-v1alpha1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PUT`

Description
replace the specified ImageContentSourcePolicy

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`ImageContentSourcePolicy`](imagecontentsourcepolicy-operator-openshift-io-v1alpha1.md#imagecontentsourcepolicy-operator-openshift-io-v1alpha1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ImageContentSourcePolicy`](imagecontentsourcepolicy-operator-openshift-io-v1alpha1.md#imagecontentsourcepolicy-operator-openshift-io-v1alpha1) schema |
| 201 - Created | [`ImageContentSourcePolicy`](imagecontentsourcepolicy-operator-openshift-io-v1alpha1.md#imagecontentsourcepolicy-operator-openshift-io-v1alpha1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/operator.openshift.io/v1alpha1/imagecontentsourcepolicies/{name}/status

| Parameter | Type     | Description                          |
|-----------|----------|--------------------------------------|
| `name`    | `string` | name of the ImageContentSourcePolicy |

Global path parameters

HTTP method
`GET`

Description
read status of the specified ImageContentSourcePolicy

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ImageContentSourcePolicy`](imagecontentsourcepolicy-operator-openshift-io-v1alpha1.md#imagecontentsourcepolicy-operator-openshift-io-v1alpha1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PATCH`

Description
partially update status of the specified ImageContentSourcePolicy

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ImageContentSourcePolicy`](imagecontentsourcepolicy-operator-openshift-io-v1alpha1.md#imagecontentsourcepolicy-operator-openshift-io-v1alpha1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PUT`

Description
replace status of the specified ImageContentSourcePolicy

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`ImageContentSourcePolicy`](imagecontentsourcepolicy-operator-openshift-io-v1alpha1.md#imagecontentsourcepolicy-operator-openshift-io-v1alpha1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ImageContentSourcePolicy`](imagecontentsourcepolicy-operator-openshift-io-v1alpha1.md#imagecontentsourcepolicy-operator-openshift-io-v1alpha1) schema |
| 201 - Created | [`ImageContentSourcePolicy`](imagecontentsourcepolicy-operator-openshift-io-v1alpha1.md#imagecontentsourcepolicy-operator-openshift-io-v1alpha1) schema |
| 401 - Unauthorized | Empty |

HTTP responses
