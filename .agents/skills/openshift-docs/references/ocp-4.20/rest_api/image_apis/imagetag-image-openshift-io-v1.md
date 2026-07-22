<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Description
ImageTag represents a single tag within an image stream and includes the spec, the status history, and the currently referenced image (if any) of the provided tag. This type replaces the ImageStreamTag by providing a full view of the tag. ImageTags are returned for every spec or status tag present on the image stream. If no tag exists in either form a not found error will be returned by the API. A create operation will succeed if no spec tag has already been defined and the spec field is set. Delete will remove both spec and status elements from the image stream.

Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).

Type
`object`

Required
- `spec`

- `status`

- `image`

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
<td style="text-align: left;"><p><code>image</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>Image is an immutable representation of a container image and metadata at a point in time. Images are named by taking a hash of their contents (metadata and content) and any change in format, content, or metadata results in a new name. The images resource is primarily for use by cluster administrators and integrations like the cluster image registry - end users instead access images via the imagestreamtags or imagestreamimages resources. While image metadata is stored in the API, any integration that implements the container image registry API must provide its own storage for the raw manifest data, image config, and layer contents.</p>
<p>Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>kind</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <a href="https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds">https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>metadata</code></p></td>
<td style="text-align: left;"><p><a href="../objects/index.xml#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta_v2"><code>ObjectMeta_v2</code></a></p></td>
<td style="text-align: left;"><p>metadata is the standard object’s metadata. More info: <a href="https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata">https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>spec</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>TagReference specifies optional annotations for images using this tag and an optional reference to an ImageStreamTag, ImageStreamImage, or DockerImage this tag should track.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>status</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>NamedTagEventList relates a tag to its image history.</p></td>
</tr>
</tbody>
</table>

## .image

Description
Image is an immutable representation of a container image and metadata at a point in time. Images are named by taking a hash of their contents (metadata and content) and any change in format, content, or metadata results in a new name. The images resource is primarily for use by cluster administrators and integrations like the cluster image registry - end users instead access images via the imagestreamtags or imagestreamimages resources. While image metadata is stored in the API, any integration that implements the container image registry API must provide its own storage for the raw manifest data, image config, and layer contents.

Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).

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
<td style="text-align: left;"><p><code>apiVersion</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <a href="https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources">https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>dockerImageConfig</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>DockerImageConfig is a JSON blob that the runtime uses to set up the container. This is a part of manifest schema v2. Will not be set when the image represents a manifest list.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>dockerImageLayers</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>DockerImageLayers represents the layers in the image. May not be set if the image does not define that data or if the image represents a manifest list.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>dockerImageLayers[]</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>ImageLayer represents a single layer of the image. Some images may have multiple layers. Some may have none.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>dockerImageManifest</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>DockerImageManifest is the raw JSON of the manifest</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>dockerImageManifestMediaType</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>DockerImageManifestMediaType specifies the mediaType of manifest. This is a part of manifest schema v2.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>dockerImageManifests</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>DockerImageManifests holds information about sub-manifests when the image represents a manifest list. When this field is present, no DockerImageLayers should be specified.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>dockerImageManifests[]</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>ImageManifest represents sub-manifests of a manifest list. The Digest field points to a regular Image object.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>dockerImageMetadata</code></p></td>
<td style="text-align: left;"><p><a href="../objects/index.xml#io-k8s-apimachinery-pkg-runtime-RawExtension"><code>RawExtension</code></a></p></td>
<td style="text-align: left;"><p>DockerImageMetadata contains metadata about this image</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>dockerImageMetadataVersion</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>DockerImageMetadataVersion conveys the version of the object, which if empty defaults to "1.0"</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>dockerImageReference</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>DockerImageReference is the string that can be used to pull this image.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>dockerImageSignatures</code></p></td>
<td style="text-align: left;"><p><code>array (string)</code></p></td>
<td style="text-align: left;"><p>DockerImageSignatures provides the signatures as opaque blobs. This is a part of manifest schema v1.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>kind</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <a href="https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds">https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>metadata</code></p></td>
<td style="text-align: left;"><p><a href="../objects/index.xml#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta_v2"><code>ObjectMeta_v2</code></a></p></td>
<td style="text-align: left;"><p>metadata is the standard object’s metadata. More info: <a href="https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata">https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>signatures</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>Signatures holds all signatures of the image.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>signatures[]</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>ImageSignature holds a signature of an image. It allows to verify image identity and possibly other claims as long as the signature is trusted. Based on this information it is possible to restrict runnable images to those matching cluster-wide policy. Mandatory fields should be parsed by clients doing image verification. The others are parsed from signature’s content by the server. They serve just an informative purpose.</p>
<p>Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).</p></td>
</tr>
</tbody>
</table>

## .image.dockerImageLayers

Description
DockerImageLayers represents the layers in the image. May not be set if the image does not define that data or if the image represents a manifest list.

Type
`array`

## .image.dockerImageLayers\[\]

Description
ImageLayer represents a single layer of the image. Some images may have multiple layers. Some may have none.

Type
`object`

Required
- `name`

- `size`

- `mediaType`

| Property | Type | Description |
|----|----|----|
| `mediaType` | `string` | MediaType of the referenced object. |
| `name` | `string` | Name of the layer as defined by the underlying store. |
| `size` | `integer` | Size of the layer in bytes as defined by the underlying store. |

## .image.dockerImageManifests

Description
DockerImageManifests holds information about sub-manifests when the image represents a manifest list. When this field is present, no DockerImageLayers should be specified.

Type
`array`

## .image.dockerImageManifests\[\]

Description
ImageManifest represents sub-manifests of a manifest list. The Digest field points to a regular Image object.

Type
`object`

Required
- `digest`

- `mediaType`

- `manifestSize`

- `architecture`

- `os`

| Property | Type | Description |
|----|----|----|
| `architecture` | `string` | Architecture specifies the supported CPU architecture, for example `amd64` or `ppc64le`. |
| `digest` | `string` | Digest is the unique identifier for the manifest. It refers to an Image object. |
| `manifestSize` | `integer` | ManifestSize represents the size of the raw object contents, in bytes. |
| `mediaType` | `string` | MediaType defines the type of the manifest, possible values are application/vnd.oci.image.manifest.v1+json, application/vnd.docker.distribution.manifest.v2+json or application/vnd.docker.distribution.manifest.v1+json. |
| `os` | `string` | OS specifies the operating system, for example `linux`. |
| `variant` | `string` | Variant is an optional field repreenting a variant of the CPU, for example v6 to specify a particular CPU variant of the ARM CPU. |

## .image.signatures

Description
Signatures holds all signatures of the image.

Type
`array`

## .image.signatures\[\]

Description
ImageSignature holds a signature of an image. It allows to verify image identity and possibly other claims as long as the signature is trusted. Based on this information it is possible to restrict runnable images to those matching cluster-wide policy. Mandatory fields should be parsed by clients doing image verification. The others are parsed from signature’s content by the server. They serve just an informative purpose.

Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).

Type
`object`

Required
- `type`

- `content`

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `conditions` | `array` | Conditions represent the latest available observations of a signature’s current state. |
| `conditions[]` | `object` | SignatureCondition describes an image signature condition of particular kind at particular probe time. |
| `content` | `string` | Required: An opaque binary string which is an image’s signature. |
| `created` | [`Time`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-Time) | If specified, it is the time of signature’s creation. |
| `imageIdentity` | `string` | A human readable string representing image’s identity. It could be a product name and version, or an image pull spec (e.g. "registry.access.redhat.com/rhel7/rhel:7.2"). |
| `issuedBy` | `object` | SignatureIssuer holds information about an issuer of signing certificate or key. |
| `issuedTo` | `object` | SignatureSubject holds information about a person or entity who created the signature. |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ObjectMeta_v2`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta_v2) | metadata is the standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |
| `signedClaims` | `object (string)` | Contains claims from the signature. |
| `type` | `string` | Required: Describes a type of stored blob. |

## .image.signatures\[\].conditions

Description
Conditions represent the latest available observations of a signature’s current state.

Type
`array`

## .image.signatures\[\].conditions\[\]

Description
SignatureCondition describes an image signature condition of particular kind at particular probe time.

Type
`object`

Required
- `type`

- `status`

| Property | Type | Description |
|----|----|----|
| `lastProbeTime` | [`Time`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-Time) | Last time the condition was checked. |
| `lastTransitionTime` | [`Time`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-Time) | Last time the condition transit from one status to another. |
| `message` | `string` | Human readable message indicating details about last transition. |
| `reason` | `string` | (brief) reason for the condition’s last transition. |
| `status` | `string` | Status of the condition, one of True, False, Unknown. |
| `type` | `string` | Type of signature condition, Complete or Failed. |

## .image.signatures\[\].issuedBy

Description
SignatureIssuer holds information about an issuer of signing certificate or key.

Type
`object`

| Property       | Type     | Description                                   |
|----------------|----------|-----------------------------------------------|
| `commonName`   | `string` | Common name (e.g. openshift-signing-service). |
| `organization` | `string` | Organization name.                            |

## .image.signatures\[\].issuedTo

Description
SignatureSubject holds information about a person or entity who created the signature.

Type
`object`

Required
- `publicKeyID`

| Property | Type | Description |
|----|----|----|
| `commonName` | `string` | Common name (e.g. openshift-signing-service). |
| `organization` | `string` | Organization name. |
| `publicKeyID` | `string` | If present, it is a human readable key id of public key belonging to the subject used to verify image signature. It should contain at least 64 lowest bits of public key’s fingerprint (e.g. 0x685ebe62bf278440). |

## .spec

Description
TagReference specifies optional annotations for images using this tag and an optional reference to an ImageStreamTag, ImageStreamImage, or DockerImage this tag should track.

Type
`object`

Required
- `name`

| Property | Type | Description |
|----|----|----|
| `annotations` | `object (string)` | Optional; if specified, annotations that are applied to images retrieved via ImageStreamTags. |
| `from` | [`ObjectReference`](../objects/index.md#io-k8s-api-core-v1-ObjectReference) | Optional; if specified, a reference to another image that this tag should point to. Valid values are ImageStreamTag, ImageStreamImage, and DockerImage. ImageStreamTag references can only reference a tag within this same ImageStream. |
| `generation` | `integer` | Generation is a counter that tracks mutations to the spec tag (user intent). When a tag reference is changed the generation is set to match the current stream generation (which is incremented every time spec is changed). Other processes in the system like the image importer observe that the generation of spec tag is newer than the generation recorded in the status and use that as a trigger to import the newest remote tag. To trigger a new import, clients may set this value to zero which will reset the generation to the latest stream generation. Legacy clients will send this value as nil which will be merged with the current tag generation. |
| `importPolicy` | `object` | TagImportPolicy controls how images related to this tag will be imported. |
| `name` | `string` | Name of the tag |
| `reference` | `boolean` | Reference states if the tag will be imported. Default value is false, which means the tag will be imported. |
| `referencePolicy` | `object` | TagReferencePolicy describes how pull-specs for images in this image stream tag are generated when image change triggers in deployment configs or builds are resolved. This allows the image stream author to control how images are accessed. |

## .spec.importPolicy

Description
TagImportPolicy controls how images related to this tag will be imported.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `importMode` | `string` | ImportMode describes how to import an image manifest. |
| `insecure` | `boolean` | Insecure is true if the server may bypass certificate verification or connect directly over HTTP during image import. |
| `scheduled` | `boolean` | Scheduled indicates to the server that this tag should be periodically checked to ensure it is up to date, and imported |

## .spec.referencePolicy

Description
TagReferencePolicy describes how pull-specs for images in this image stream tag are generated when image change triggers in deployment configs or builds are resolved. This allows the image stream author to control how images are accessed.

Type
`object`

Required
- `type`

| Property | Type | Description |
|----|----|----|
| `type` | `string` | Type determines how the image pull spec should be transformed when the image stream tag is used in deployment config triggers or new builds. The default value is `Source`, indicating the original location of the image should be used (if imported). The user may also specify `Local`, indicating that the pull spec should point to the integrated container image registry and leverage the registry’s ability to proxy the pull to an upstream registry. `Local` allows the credentials used to pull this image to be managed from the image stream’s namespace, so others on the platform can access a remote image but have no access to the remote secret. It also allows the image layers to be mirrored into the local registry which the images can still be pulled even if the upstream registry is unavailable. |

## .status

Description
NamedTagEventList relates a tag to its image history.

Type
`object`

Required
- `tag`

- `items`

| Property | Type | Description |
|----|----|----|
| `conditions` | `array` | Conditions is an array of conditions that apply to the tag event list. |
| `conditions[]` | `object` | TagEventCondition contains condition information for a tag event. |
| `items` | `array` | Standard object’s metadata. |
| `items[]` | `object` | TagEvent is used by ImageStreamStatus to keep a historical record of images associated with a tag. |
| `tag` | `string` | Tag is the tag for which the history is recorded |

## .status.conditions

Description
Conditions is an array of conditions that apply to the tag event list.

Type
`array`

## .status.conditions\[\]

Description
TagEventCondition contains condition information for a tag event.

Type
`object`

Required
- `type`

- `status`

- `generation`

| Property | Type | Description |
|----|----|----|
| `generation` | `integer` | Generation is the spec tag generation that this status corresponds to |
| `lastTransitionTime` | [`Time`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-Time) | LastTransitionTIme is the time the condition transitioned from one status to another. |
| `message` | `string` | Message is a human readable description of the details about last transition, complementing reason. |
| `reason` | `string` | Reason is a brief machine readable explanation for the condition’s last transition. |
| `status` | `string` | Status of the condition, one of True, False, Unknown. |
| `type` | `string` | Type of tag event condition, currently only ImportSuccess |

## .status.items

Description
Standard object’s metadata.

Type
`array`

## .status.items\[\]

Description
TagEvent is used by ImageStreamStatus to keep a historical record of images associated with a tag.

Type
`object`

Required
- `created`

- `dockerImageReference`

- `image`

- `generation`

| Property | Type | Description |
|----|----|----|
| `created` | [`Time`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-Time) | Created holds the time the TagEvent was created |
| `dockerImageReference` | `string` | DockerImageReference is the string that can be used to pull this image |
| `generation` | `integer` | Generation is the spec tag generation that resulted in this tag being updated |
| `image` | `string` | Image is the image |

# API endpoints

The following API endpoints are available:

- `/apis/image.openshift.io/v1/imagetags`

  - `GET`: list objects of kind ImageTag

- `/apis/image.openshift.io/v1/namespaces/{namespace}/imagetags`

  - `GET`: list objects of kind ImageTag

  - `POST`: create an ImageTag

- `/apis/image.openshift.io/v1/namespaces/{namespace}/imagetags/{name}`

  - `DELETE`: delete an ImageTag

  - `GET`: read the specified ImageTag

  - `PATCH`: partially update the specified ImageTag

  - `PUT`: replace the specified ImageTag

## /apis/image.openshift.io/v1/imagetags

HTTP method
`GET`

Description
list objects of kind ImageTag

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ImageTagList`](../objects/index.md#com-github-openshift-api-image-v1-ImageTagList) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/image.openshift.io/v1/namespaces/{namespace}/imagetags

HTTP method
`GET`

Description
list objects of kind ImageTag

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ImageTagList`](../objects/index.md#com-github-openshift-api-image-v1-ImageTagList) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`POST`

Description
create an ImageTag

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`ImageTag`](imagetag-image-openshift-io-v1.md#imagetag-image-openshift-io-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ImageTag`](imagetag-image-openshift-io-v1.md#imagetag-image-openshift-io-v1) schema |
| 201 - Created | [`ImageTag`](imagetag-image-openshift-io-v1.md#imagetag-image-openshift-io-v1) schema |
| 202 - Accepted | [`ImageTag`](imagetag-image-openshift-io-v1.md#imagetag-image-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/image.openshift.io/v1/namespaces/{namespace}/imagetags/{name}

| Parameter | Type     | Description          |
|-----------|----------|----------------------|
| `name`    | `string` | name of the ImageTag |

Global path parameters

HTTP method
`DELETE`

Description
delete an ImageTag

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |

Query parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Status_v5`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-Status_v5) schema |
| 202 - Accepted | [`Status_v5`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-Status_v5) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`GET`

Description
read the specified ImageTag

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ImageTag`](imagetag-image-openshift-io-v1.md#imagetag-image-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PATCH`

Description
partially update the specified ImageTag

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ImageTag`](imagetag-image-openshift-io-v1.md#imagetag-image-openshift-io-v1) schema |
| 201 - Created | [`ImageTag`](imagetag-image-openshift-io-v1.md#imagetag-image-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PUT`

Description
replace the specified ImageTag

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`ImageTag`](imagetag-image-openshift-io-v1.md#imagetag-image-openshift-io-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ImageTag`](imagetag-image-openshift-io-v1.md#imagetag-image-openshift-io-v1) schema |
| 201 - Created | [`ImageTag`](imagetag-image-openshift-io-v1.md#imagetag-image-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses
