<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Description
PinnedImageSet describes a set of images that should be pinned by CRI-O and pulled to the nodes which are members of the declared MachineConfigPools.

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
| `spec` | `object` | spec describes the configuration of this pinned image set. |

## .spec

Description
spec describes the configuration of this pinned image set.

Type
`object`

Required
- `pinnedImages`

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
<td style="text-align: left;"><p><code>pinnedImages</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>pinnedImages is a list of OCI Image referenced by digest that should be pinned and pre-loaded by the nodes of a MachineConfigPool. Translates into a new file inside the /etc/crio/crio.conf.d directory with content similar to this:</p>
<p>pinned_images = [ "quay.io/openshift-release-dev/ocp-release@sha256:…​", "quay.io/openshift-release-dev/ocp-v4.0-art-dev@sha256:…​", "quay.io/openshift-release-dev/ocp-v4.0-art-dev@sha256:…​", …​ ]</p>
<p>Image references must be by digest. A maximum of 500 images may be specified.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>pinnedImages[]</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>PinnedImageRef represents a reference to an OCI image</p></td>
</tr>
</tbody>
</table>

## .spec.pinnedImages

Description
pinnedImages is a list of OCI Image referenced by digest that should be pinned and pre-loaded by the nodes of a MachineConfigPool. Translates into a new file inside the /etc/crio/crio.conf.d directory with content similar to this:

    pinned_images = [
            "quay.io/openshift-release-dev/ocp-release@sha256:...",
            "quay.io/openshift-release-dev/ocp-v4.0-art-dev@sha256:...",
            "quay.io/openshift-release-dev/ocp-v4.0-art-dev@sha256:...",
            ...
    ]

Image references must be by digest. A maximum of 500 images may be specified.

Type
`array`

## .spec.pinnedImages\[\]

Description
PinnedImageRef represents a reference to an OCI image

Type
`object`

Required
- `name`

| Property | Type | Description |
|----|----|----|
| `name` | `string` | name is an OCI Image referenced by digest. The format of the image pull spec is: host\[:port\]\[/namespace\]/name@sha256:\<digest\>, where the digest must be 64 characters long, and consist only of lowercase hexadecimal characters, a-f and 0-9. The length of the whole spec must be between 1 to 447 characters. |

# API endpoints

The following API endpoints are available:

- `/apis/machineconfiguration.openshift.io/v1/pinnedimagesets`

  - `DELETE`: delete collection of PinnedImageSet

  - `GET`: list objects of kind PinnedImageSet

  - `POST`: create a PinnedImageSet

- `/apis/machineconfiguration.openshift.io/v1/pinnedimagesets/{name}`

  - `DELETE`: delete a PinnedImageSet

  - `GET`: read the specified PinnedImageSet

  - `PATCH`: partially update the specified PinnedImageSet

  - `PUT`: replace the specified PinnedImageSet

## /apis/machineconfiguration.openshift.io/v1/pinnedimagesets

HTTP method
`DELETE`

Description
delete collection of PinnedImageSet

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Status`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`GET`

Description
list objects of kind PinnedImageSet

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`PinnedImageSetList`](../objects/index.md#io-openshift-machineconfiguration-v1-PinnedImageSetList) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`POST`

Description
create a PinnedImageSet

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`PinnedImageSet`](pinnedimageset-machineconfiguration-openshift-io-v1.md#pinnedimageset-machineconfiguration-openshift-io-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`PinnedImageSet`](pinnedimageset-machineconfiguration-openshift-io-v1.md#pinnedimageset-machineconfiguration-openshift-io-v1) schema |
| 201 - Created | [`PinnedImageSet`](pinnedimageset-machineconfiguration-openshift-io-v1.md#pinnedimageset-machineconfiguration-openshift-io-v1) schema |
| 202 - Accepted | [`PinnedImageSet`](pinnedimageset-machineconfiguration-openshift-io-v1.md#pinnedimageset-machineconfiguration-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/machineconfiguration.openshift.io/v1/pinnedimagesets/{name}

| Parameter | Type     | Description                |
|-----------|----------|----------------------------|
| `name`    | `string` | name of the PinnedImageSet |

Global path parameters

HTTP method
`DELETE`

Description
delete a PinnedImageSet

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
read the specified PinnedImageSet

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`PinnedImageSet`](pinnedimageset-machineconfiguration-openshift-io-v1.md#pinnedimageset-machineconfiguration-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PATCH`

Description
partially update the specified PinnedImageSet

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`PinnedImageSet`](pinnedimageset-machineconfiguration-openshift-io-v1.md#pinnedimageset-machineconfiguration-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PUT`

Description
replace the specified PinnedImageSet

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`PinnedImageSet`](pinnedimageset-machineconfiguration-openshift-io-v1.md#pinnedimageset-machineconfiguration-openshift-io-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`PinnedImageSet`](pinnedimageset-machineconfiguration-openshift-io-v1.md#pinnedimageset-machineconfiguration-openshift-io-v1) schema |
| 201 - Created | [`PinnedImageSet`](pinnedimageset-machineconfiguration-openshift-io-v1.md#pinnedimageset-machineconfiguration-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses
