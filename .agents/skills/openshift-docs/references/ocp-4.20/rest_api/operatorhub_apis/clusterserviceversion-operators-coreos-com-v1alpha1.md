<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Description
ClusterServiceVersion is a Custom Resource of type `ClusterServiceVersionSpec`.

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
| `spec` | `object` | ClusterServiceVersionSpec declarations tell OLM how to install an operator that can manage apps for a given version. |
| `status` | `object` | ClusterServiceVersionStatus represents information about the status of a CSV. Status may trail the actual state of a system. |

## .spec

Description
ClusterServiceVersionSpec declarations tell OLM how to install an operator that can manage apps for a given version.

Type
`object`

Required
- `displayName`

- `install`

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
<td style="text-align: left;"><p><code>annotations</code></p></td>
<td style="text-align: left;"><p><code>object (string)</code></p></td>
<td style="text-align: left;"><p>Annotations is an unstructured key value map stored with a resource that may be set by external tools to store and retrieve arbitrary metadata.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>apiservicedefinitions</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>APIServiceDefinitions declares all of the extension apis managed or required by an operator being ran by ClusterServiceVersion.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>cleanup</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>Cleanup specifies the cleanup behaviour when the CSV gets deleted</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>customresourcedefinitions</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>CustomResourceDefinitions declares all of the CRDs managed or required by an operator being ran by ClusterServiceVersion.</p>
<p>If the CRD is present in the Owned list, it is implicitly required.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>description</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Description of the operator. Can include the features, limitations or use-cases of the operator.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>displayName</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>The name of the operator in display format.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>icon</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>The icon for this operator.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>icon[]</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>install</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>NamedInstallStrategy represents the block of an ClusterServiceVersion resource where the install strategy is specified.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>installModes</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>InstallModes specify supported installation types</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>installModes[]</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>InstallMode associates an InstallModeType with a flag representing if the CSV supports it</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>keywords</code></p></td>
<td style="text-align: left;"><p><code>array (string)</code></p></td>
<td style="text-align: left;"><p>A list of keywords describing the operator.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>labels</code></p></td>
<td style="text-align: left;"><p><code>object (string)</code></p></td>
<td style="text-align: left;"><p>Map of string keys and values that can be used to organize and categorize (scope and select) objects.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>links</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>A list of links related to the operator.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>links[]</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>maintainers</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>A list of organizational entities maintaining the operator.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>maintainers[]</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>maturity</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>minKubeVersion</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>nativeAPIs</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>nativeAPIs[]</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>GroupVersionKind unambiguously identifies a kind. It doesn’t anonymously include GroupVersion to avoid automatic coercion. It doesn’t use a GroupVersion to avoid custom marshalling</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>provider</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>The publishing entity behind the operator.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>relatedImages</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>List any related images, or other container images that your Operator might require to perform their functions. This list should also include operand images as well. All image references should be specified by digest (SHA) and not by tag. This field is only used during catalog creation and plays no part in cluster runtime.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>relatedImages[]</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>replaces</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>The name of a CSV this one replaces. Should match the <code>metadata.Name</code> field of the old CSV.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>selector</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>Label selector for related resources.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>skips</code></p></td>
<td style="text-align: left;"><p><code>array (string)</code></p></td>
<td style="text-align: left;"><p>The name(s) of one or more CSV(s) that should be skipped in the upgrade graph. Should match the <code>metadata.Name</code> field of the CSV that should be skipped. This field is only used during catalog creation and plays no part in cluster runtime.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>version</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>webhookdefinitions</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>webhookdefinitions[]</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>WebhookDescription provides details to OLM about required webhooks</p></td>
</tr>
</tbody>
</table>

## .spec.apiservicedefinitions

Description
APIServiceDefinitions declares all of the extension apis managed or required by an operator being ran by ClusterServiceVersion.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `owned` | `array` |  |
| `owned[]` | `object` | APIServiceDescription provides details to OLM about apis provided via aggregation |
| `required` | `array` |  |
| `required[]` | `object` | APIServiceDescription provides details to OLM about apis provided via aggregation |

## .spec.apiservicedefinitions.owned

Description

Type
`array`

## .spec.apiservicedefinitions.owned\[\]

Description
APIServiceDescription provides details to OLM about apis provided via aggregation

Type
`object`

Required
- `group`

- `kind`

- `name`

- `version`

| Property | Type | Description |
|----|----|----|
| `actionDescriptors` | `array` |  |
| `actionDescriptors[]` | `object` | ActionDescriptor describes a declarative action that can be performed on a custom resource instance |
| `containerPort` | `integer` |  |
| `deploymentName` | `string` |  |
| `description` | `string` |  |
| `displayName` | `string` |  |
| `group` | `string` |  |
| `kind` | `string` |  |
| `name` | `string` |  |
| `resources` | `array` |  |
| `resources[]` | `object` | APIResourceReference is a reference to a Kubernetes resource type that the referrer utilizes. |
| `specDescriptors` | `array` |  |
| `specDescriptors[]` | `object` | SpecDescriptor describes a field in a spec block of a CRD so that OLM can consume it |
| `statusDescriptors` | `array` |  |
| `statusDescriptors[]` | `object` | StatusDescriptor describes a field in a status block of a CRD so that OLM can consume it |
| `version` | `string` |  |

## .spec.apiservicedefinitions.owned\[\].actionDescriptors

Description

Type
`array`

## .spec.apiservicedefinitions.owned\[\].actionDescriptors\[\]

Description
ActionDescriptor describes a declarative action that can be performed on a custom resource instance

Type
`object`

Required
- `path`

| Property | Type | Description |
|----|----|----|
| `description` | `string` |  |
| `displayName` | `string` |  |
| `path` | `string` |  |
| `value` | `string` | RawMessage is a raw encoded JSON value. It implements \[Marshaler\] and \[Unmarshaler\] and can be used to delay JSON decoding or precompute a JSON encoding. |
| `x-descriptors` | `array (string)` |  |

## .spec.apiservicedefinitions.owned\[\].resources

Description

Type
`array`

## .spec.apiservicedefinitions.owned\[\].resources\[\]

Description
APIResourceReference is a reference to a Kubernetes resource type that the referrer utilizes.

Type
`object`

Required
- `kind`

- `name`

- `version`

| Property | Type | Description |
|----|----|----|
| `kind` | `string` | Kind of the referenced resource type. |
| `name` | `string` | Plural name of the referenced resource type (CustomResourceDefinition.Spec.Names\[\].Plural). Empty string if the referenced resource type is not a custom resource. |
| `version` | `string` | API Version of the referenced resource type. |

## .spec.apiservicedefinitions.owned\[\].specDescriptors

Description

Type
`array`

## .spec.apiservicedefinitions.owned\[\].specDescriptors\[\]

Description
SpecDescriptor describes a field in a spec block of a CRD so that OLM can consume it

Type
`object`

Required
- `path`

| Property | Type | Description |
|----|----|----|
| `description` | `string` |  |
| `displayName` | `string` |  |
| `path` | `string` |  |
| `value` | `string` | RawMessage is a raw encoded JSON value. It implements \[Marshaler\] and \[Unmarshaler\] and can be used to delay JSON decoding or precompute a JSON encoding. |
| `x-descriptors` | `array (string)` |  |

## .spec.apiservicedefinitions.owned\[\].statusDescriptors

Description

Type
`array`

## .spec.apiservicedefinitions.owned\[\].statusDescriptors\[\]

Description
StatusDescriptor describes a field in a status block of a CRD so that OLM can consume it

Type
`object`

Required
- `path`

| Property | Type | Description |
|----|----|----|
| `description` | `string` |  |
| `displayName` | `string` |  |
| `path` | `string` |  |
| `value` | `string` | RawMessage is a raw encoded JSON value. It implements \[Marshaler\] and \[Unmarshaler\] and can be used to delay JSON decoding or precompute a JSON encoding. |
| `x-descriptors` | `array (string)` |  |

## .spec.apiservicedefinitions.required

Description

Type
`array`

## .spec.apiservicedefinitions.required\[\]

Description
APIServiceDescription provides details to OLM about apis provided via aggregation

Type
`object`

Required
- `group`

- `kind`

- `name`

- `version`

| Property | Type | Description |
|----|----|----|
| `actionDescriptors` | `array` |  |
| `actionDescriptors[]` | `object` | ActionDescriptor describes a declarative action that can be performed on a custom resource instance |
| `containerPort` | `integer` |  |
| `deploymentName` | `string` |  |
| `description` | `string` |  |
| `displayName` | `string` |  |
| `group` | `string` |  |
| `kind` | `string` |  |
| `name` | `string` |  |
| `resources` | `array` |  |
| `resources[]` | `object` | APIResourceReference is a reference to a Kubernetes resource type that the referrer utilizes. |
| `specDescriptors` | `array` |  |
| `specDescriptors[]` | `object` | SpecDescriptor describes a field in a spec block of a CRD so that OLM can consume it |
| `statusDescriptors` | `array` |  |
| `statusDescriptors[]` | `object` | StatusDescriptor describes a field in a status block of a CRD so that OLM can consume it |
| `version` | `string` |  |

## .spec.apiservicedefinitions.required\[\].actionDescriptors

Description

Type
`array`

## .spec.apiservicedefinitions.required\[\].actionDescriptors\[\]

Description
ActionDescriptor describes a declarative action that can be performed on a custom resource instance

Type
`object`

Required
- `path`

| Property | Type | Description |
|----|----|----|
| `description` | `string` |  |
| `displayName` | `string` |  |
| `path` | `string` |  |
| `value` | `string` | RawMessage is a raw encoded JSON value. It implements \[Marshaler\] and \[Unmarshaler\] and can be used to delay JSON decoding or precompute a JSON encoding. |
| `x-descriptors` | `array (string)` |  |

## .spec.apiservicedefinitions.required\[\].resources

Description

Type
`array`

## .spec.apiservicedefinitions.required\[\].resources\[\]

Description
APIResourceReference is a reference to a Kubernetes resource type that the referrer utilizes.

Type
`object`

Required
- `kind`

- `name`

- `version`

| Property | Type | Description |
|----|----|----|
| `kind` | `string` | Kind of the referenced resource type. |
| `name` | `string` | Plural name of the referenced resource type (CustomResourceDefinition.Spec.Names\[\].Plural). Empty string if the referenced resource type is not a custom resource. |
| `version` | `string` | API Version of the referenced resource type. |

## .spec.apiservicedefinitions.required\[\].specDescriptors

Description

Type
`array`

## .spec.apiservicedefinitions.required\[\].specDescriptors\[\]

Description
SpecDescriptor describes a field in a spec block of a CRD so that OLM can consume it

Type
`object`

Required
- `path`

| Property | Type | Description |
|----|----|----|
| `description` | `string` |  |
| `displayName` | `string` |  |
| `path` | `string` |  |
| `value` | `string` | RawMessage is a raw encoded JSON value. It implements \[Marshaler\] and \[Unmarshaler\] and can be used to delay JSON decoding or precompute a JSON encoding. |
| `x-descriptors` | `array (string)` |  |

## .spec.apiservicedefinitions.required\[\].statusDescriptors

Description

Type
`array`

## .spec.apiservicedefinitions.required\[\].statusDescriptors\[\]

Description
StatusDescriptor describes a field in a status block of a CRD so that OLM can consume it

Type
`object`

Required
- `path`

| Property | Type | Description |
|----|----|----|
| `description` | `string` |  |
| `displayName` | `string` |  |
| `path` | `string` |  |
| `value` | `string` | RawMessage is a raw encoded JSON value. It implements \[Marshaler\] and \[Unmarshaler\] and can be used to delay JSON decoding or precompute a JSON encoding. |
| `x-descriptors` | `array (string)` |  |

## .spec.cleanup

Description
Cleanup specifies the cleanup behaviour when the CSV gets deleted

Type
`object`

Required
- `enabled`

| Property  | Type      | Description |
|-----------|-----------|-------------|
| `enabled` | `boolean` |             |

## .spec.customresourcedefinitions

Description
CustomResourceDefinitions declares all of the CRDs managed or required by an operator being ran by ClusterServiceVersion.

If the CRD is present in the Owned list, it is implicitly required.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `owned` | `array` |  |
| `owned[]` | `object` | CRDDescription provides details to OLM about the CRDs |
| `required` | `array` |  |
| `required[]` | `object` | CRDDescription provides details to OLM about the CRDs |

## .spec.customresourcedefinitions.owned

Description

Type
`array`

## .spec.customresourcedefinitions.owned\[\]

Description
CRDDescription provides details to OLM about the CRDs

Type
`object`

Required
- `kind`

- `name`

- `version`

| Property | Type | Description |
|----|----|----|
| `actionDescriptors` | `array` |  |
| `actionDescriptors[]` | `object` | ActionDescriptor describes a declarative action that can be performed on a custom resource instance |
| `description` | `string` |  |
| `displayName` | `string` |  |
| `kind` | `string` |  |
| `name` | `string` |  |
| `resources` | `array` |  |
| `resources[]` | `object` | APIResourceReference is a reference to a Kubernetes resource type that the referrer utilizes. |
| `specDescriptors` | `array` |  |
| `specDescriptors[]` | `object` | SpecDescriptor describes a field in a spec block of a CRD so that OLM can consume it |
| `statusDescriptors` | `array` |  |
| `statusDescriptors[]` | `object` | StatusDescriptor describes a field in a status block of a CRD so that OLM can consume it |
| `version` | `string` |  |

## .spec.customresourcedefinitions.owned\[\].actionDescriptors

Description

Type
`array`

## .spec.customresourcedefinitions.owned\[\].actionDescriptors\[\]

Description
ActionDescriptor describes a declarative action that can be performed on a custom resource instance

Type
`object`

Required
- `path`

| Property | Type | Description |
|----|----|----|
| `description` | `string` |  |
| `displayName` | `string` |  |
| `path` | `string` |  |
| `value` | `string` | RawMessage is a raw encoded JSON value. It implements \[Marshaler\] and \[Unmarshaler\] and can be used to delay JSON decoding or precompute a JSON encoding. |
| `x-descriptors` | `array (string)` |  |

## .spec.customresourcedefinitions.owned\[\].resources

Description

Type
`array`

## .spec.customresourcedefinitions.owned\[\].resources\[\]

Description
APIResourceReference is a reference to a Kubernetes resource type that the referrer utilizes.

Type
`object`

Required
- `kind`

- `name`

- `version`

| Property | Type | Description |
|----|----|----|
| `kind` | `string` | Kind of the referenced resource type. |
| `name` | `string` | Plural name of the referenced resource type (CustomResourceDefinition.Spec.Names\[\].Plural). Empty string if the referenced resource type is not a custom resource. |
| `version` | `string` | API Version of the referenced resource type. |

## .spec.customresourcedefinitions.owned\[\].specDescriptors

Description

Type
`array`

## .spec.customresourcedefinitions.owned\[\].specDescriptors\[\]

Description
SpecDescriptor describes a field in a spec block of a CRD so that OLM can consume it

Type
`object`

Required
- `path`

| Property | Type | Description |
|----|----|----|
| `description` | `string` |  |
| `displayName` | `string` |  |
| `path` | `string` |  |
| `value` | `string` | RawMessage is a raw encoded JSON value. It implements \[Marshaler\] and \[Unmarshaler\] and can be used to delay JSON decoding or precompute a JSON encoding. |
| `x-descriptors` | `array (string)` |  |

## .spec.customresourcedefinitions.owned\[\].statusDescriptors

Description

Type
`array`

## .spec.customresourcedefinitions.owned\[\].statusDescriptors\[\]

Description
StatusDescriptor describes a field in a status block of a CRD so that OLM can consume it

Type
`object`

Required
- `path`

| Property | Type | Description |
|----|----|----|
| `description` | `string` |  |
| `displayName` | `string` |  |
| `path` | `string` |  |
| `value` | `string` | RawMessage is a raw encoded JSON value. It implements \[Marshaler\] and \[Unmarshaler\] and can be used to delay JSON decoding or precompute a JSON encoding. |
| `x-descriptors` | `array (string)` |  |

## .spec.customresourcedefinitions.required

Description

Type
`array`

## .spec.customresourcedefinitions.required\[\]

Description
CRDDescription provides details to OLM about the CRDs

Type
`object`

Required
- `kind`

- `name`

- `version`

| Property | Type | Description |
|----|----|----|
| `actionDescriptors` | `array` |  |
| `actionDescriptors[]` | `object` | ActionDescriptor describes a declarative action that can be performed on a custom resource instance |
| `description` | `string` |  |
| `displayName` | `string` |  |
| `kind` | `string` |  |
| `name` | `string` |  |
| `resources` | `array` |  |
| `resources[]` | `object` | APIResourceReference is a reference to a Kubernetes resource type that the referrer utilizes. |
| `specDescriptors` | `array` |  |
| `specDescriptors[]` | `object` | SpecDescriptor describes a field in a spec block of a CRD so that OLM can consume it |
| `statusDescriptors` | `array` |  |
| `statusDescriptors[]` | `object` | StatusDescriptor describes a field in a status block of a CRD so that OLM can consume it |
| `version` | `string` |  |

## .spec.customresourcedefinitions.required\[\].actionDescriptors

Description

Type
`array`

## .spec.customresourcedefinitions.required\[\].actionDescriptors\[\]

Description
ActionDescriptor describes a declarative action that can be performed on a custom resource instance

Type
`object`

Required
- `path`

| Property | Type | Description |
|----|----|----|
| `description` | `string` |  |
| `displayName` | `string` |  |
| `path` | `string` |  |
| `value` | `string` | RawMessage is a raw encoded JSON value. It implements \[Marshaler\] and \[Unmarshaler\] and can be used to delay JSON decoding or precompute a JSON encoding. |
| `x-descriptors` | `array (string)` |  |

## .spec.customresourcedefinitions.required\[\].resources

Description

Type
`array`

## .spec.customresourcedefinitions.required\[\].resources\[\]

Description
APIResourceReference is a reference to a Kubernetes resource type that the referrer utilizes.

Type
`object`

Required
- `kind`

- `name`

- `version`

| Property | Type | Description |
|----|----|----|
| `kind` | `string` | Kind of the referenced resource type. |
| `name` | `string` | Plural name of the referenced resource type (CustomResourceDefinition.Spec.Names\[\].Plural). Empty string if the referenced resource type is not a custom resource. |
| `version` | `string` | API Version of the referenced resource type. |

## .spec.customresourcedefinitions.required\[\].specDescriptors

Description

Type
`array`

## .spec.customresourcedefinitions.required\[\].specDescriptors\[\]

Description
SpecDescriptor describes a field in a spec block of a CRD so that OLM can consume it

Type
`object`

Required
- `path`

| Property | Type | Description |
|----|----|----|
| `description` | `string` |  |
| `displayName` | `string` |  |
| `path` | `string` |  |
| `value` | `string` | RawMessage is a raw encoded JSON value. It implements \[Marshaler\] and \[Unmarshaler\] and can be used to delay JSON decoding or precompute a JSON encoding. |
| `x-descriptors` | `array (string)` |  |

## .spec.customresourcedefinitions.required\[\].statusDescriptors

Description

Type
`array`

## .spec.customresourcedefinitions.required\[\].statusDescriptors\[\]

Description
StatusDescriptor describes a field in a status block of a CRD so that OLM can consume it

Type
`object`

Required
- `path`

| Property | Type | Description |
|----|----|----|
| `description` | `string` |  |
| `displayName` | `string` |  |
| `path` | `string` |  |
| `value` | `string` | RawMessage is a raw encoded JSON value. It implements \[Marshaler\] and \[Unmarshaler\] and can be used to delay JSON decoding or precompute a JSON encoding. |
| `x-descriptors` | `array (string)` |  |

## .spec.icon

Description
The icon for this operator.

Type
`array`

## .spec.icon\[\]

Description

Type
`object`

Required
- `base64data`

- `mediatype`

| Property     | Type     | Description |
|--------------|----------|-------------|
| `base64data` | `string` |             |
| `mediatype`  | `string` |             |

## .spec.install

Description
NamedInstallStrategy represents the block of an ClusterServiceVersion resource where the install strategy is specified.

Type
`object`

Required
- `strategy`

| Property | Type | Description |
|----|----|----|
| `spec` | `object` | StrategyDetailsDeployment represents the parsed details of a Deployment InstallStrategy. |
| `strategy` | `string` |  |

## .spec.install.spec

Description
StrategyDetailsDeployment represents the parsed details of a Deployment InstallStrategy.

Type
`object`

Required
- `deployments`

| Property | Type | Description |
|----|----|----|
| `clusterPermissions` | `array` |  |
| `clusterPermissions[]` | `object` | StrategyDeploymentPermissions describe the rbac rules and service account needed by the install strategy |
| `deployments` | `array` |  |
| `deployments[]` | `object` | StrategyDeploymentSpec contains the name, spec and labels for the deployment ALM should create |
| `permissions` | `array` |  |
| `permissions[]` | `object` | StrategyDeploymentPermissions describe the rbac rules and service account needed by the install strategy |

## .spec.install.spec.clusterPermissions

Description

Type
`array`

## .spec.install.spec.clusterPermissions\[\]

Description
StrategyDeploymentPermissions describe the rbac rules and service account needed by the install strategy

Type
`object`

Required
- `rules`

- `serviceAccountName`

| Property | Type | Description |
|----|----|----|
| `rules` | `array` |  |
| `rules[]` | `object` | PolicyRule holds information that describes a policy rule, but does not contain information about who the rule applies to or which namespace the rule applies to. |
| `serviceAccountName` | `string` |  |

## .spec.install.spec.clusterPermissions\[\].rules

Description

Type
`array`

## .spec.install.spec.clusterPermissions\[\].rules\[\]

Description
PolicyRule holds information that describes a policy rule, but does not contain information about who the rule applies to or which namespace the rule applies to.

Type
`object`

Required
- `verbs`

| Property | Type | Description |
|----|----|----|
| `apiGroups` | `array (string)` | APIGroups is the name of the APIGroup that contains the resources. If multiple API groups are specified, any action requested against one of the enumerated resources in any API group will be allowed. "" represents the core API group and "\*" represents all API groups. |
| `nonResourceURLs` | `array (string)` | NonResourceURLs is a set of partial urls that a user should have access to. \*s are allowed, but only as the full, final step in the path Since non-resource URLs are not namespaced, this field is only applicable for ClusterRoles referenced from a ClusterRoleBinding. Rules can either apply to API resources (such as "pods" or "secrets") or non-resource URL paths (such as "/api"), but not both. |
| `resourceNames` | `array (string)` | ResourceNames is an optional white list of names that the rule applies to. An empty set means that everything is allowed. |
| `resources` | `array (string)` | Resources is a list of resources this rule applies to. '\*' represents all resources. |
| `verbs` | `array (string)` | Verbs is a list of Verbs that apply to ALL the ResourceKinds contained in this rule. '\*' represents all verbs. |

## .spec.install.spec.deployments

Description

Type
`array`

## .spec.install.spec.deployments\[\]

Description
StrategyDeploymentSpec contains the name, spec and labels for the deployment ALM should create

Type
`object`

Required
- `name`

- `spec`

| Property | Type | Description |
|----|----|----|
| `label` | `object (string)` | Set is a map of label:value. It implements Labels. |
| `name` | `string` |  |
| `spec` | `object` | DeploymentSpec is the specification of the desired behavior of the Deployment. |

## .spec.install.spec.deployments\[\].spec

Description
DeploymentSpec is the specification of the desired behavior of the Deployment.

Type
`object`

Required
- `selector`

- `template`

| Property | Type | Description |
|----|----|----|
| `minReadySeconds` | `integer` | Minimum number of seconds for which a newly created pod should be ready without any of its container crashing, for it to be considered available. Defaults to 0 (pod will be considered available as soon as it is ready) |
| `paused` | `boolean` | Indicates that the deployment is paused. |
| `progressDeadlineSeconds` | `integer` | The maximum time in seconds for a deployment to make progress before it is considered to be failed. The deployment controller will continue to process failed deployments and a condition with a ProgressDeadlineExceeded reason will be surfaced in the deployment status. Note that progress will not be estimated during the time a deployment is paused. Defaults to 600s. |
| `replicas` | `integer` | Number of desired pods. This is a pointer to distinguish between explicit zero and not specified. Defaults to 1. |
| `revisionHistoryLimit` | `integer` | The number of old ReplicaSets to retain to allow rollback. This is a pointer to distinguish between explicit zero and not specified. Defaults to 10. |
| `selector` | `object` | Label selector for pods. Existing ReplicaSets whose pods are selected by this will be the ones affected by this deployment. It must match the pod template’s labels. |
| `strategy` | `object` | The deployment strategy to use to replace existing pods with new ones. |
| `template` | `object` | Template describes the pods that will be created. The only allowed template.spec.restartPolicy value is "Always". |

## .spec.install.spec.deployments\[\].spec.selector

Description
Label selector for pods. Existing ReplicaSets whose pods are selected by this will be the ones affected by this deployment. It must match the pod template’s labels.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `matchExpressions` | `array` | matchExpressions is a list of label selector requirements. The requirements are ANDed. |
| `matchExpressions[]` | `object` | A label selector requirement is a selector that contains values, a key, and an operator that relates the key and values. |
| `matchLabels` | `object (string)` | matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed. |

## .spec.install.spec.deployments\[\].spec.selector.matchExpressions

Description
matchExpressions is a list of label selector requirements. The requirements are ANDed.

Type
`array`

## .spec.install.spec.deployments\[\].spec.selector.matchExpressions\[\]

Description
A label selector requirement is a selector that contains values, a key, and an operator that relates the key and values.

Type
`object`

Required
- `key`

- `operator`

| Property | Type | Description |
|----|----|----|
| `key` | `string` | key is the label key that the selector applies to. |
| `operator` | `string` | operator represents a key’s relationship to a set of values. Valid operators are In, NotIn, Exists and DoesNotExist. |
| `values` | `array (string)` | values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch. |

## .spec.install.spec.deployments\[\].spec.strategy

Description
The deployment strategy to use to replace existing pods with new ones.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `rollingUpdate` | `object` | Rolling update config params. Present only if DeploymentStrategyType = RollingUpdate. |
| `type` | `string` | Type of deployment. Can be "Recreate" or "RollingUpdate". Default is RollingUpdate. |

## .spec.install.spec.deployments\[\].spec.strategy.rollingUpdate

Description
Rolling update config params. Present only if DeploymentStrategyType = RollingUpdate.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `maxSurge` | `integer-or-string` | The maximum number of pods that can be scheduled above the desired number of pods. Value can be an absolute number (ex: 5) or a percentage of desired pods (ex: 10%). This can not be 0 if MaxUnavailable is 0. Absolute number is calculated from percentage by rounding up. Defaults to 25%. Example: when this is set to 30%, the new ReplicaSet can be scaled up immediately when the rolling update starts, such that the total number of old and new pods do not exceed 130% of desired pods. Once old pods have been killed, new ReplicaSet can be scaled up further, ensuring that total number of pods running at any time during the update is at most 130% of desired pods. |
| `maxUnavailable` | `integer-or-string` | The maximum number of pods that can be unavailable during the update. Value can be an absolute number (ex: 5) or a percentage of desired pods (ex: 10%). Absolute number is calculated from percentage by rounding down. This can not be 0 if MaxSurge is 0. Defaults to 25%. Example: when this is set to 30%, the old ReplicaSet can be scaled down to 70% of desired pods immediately when the rolling update starts. Once new pods are ready, old ReplicaSet can be scaled down further, followed by scaling up the new ReplicaSet, ensuring that the total number of pods available at all times during the update is at least 70% of desired pods. |

## .spec.install.spec.deployments\[\].spec.template

Description
Template describes the pods that will be created. The only allowed template.spec.restartPolicy value is "Always".

Type
`object`

| Property | Type | Description |
|----|----|----|
| `metadata` | \`\` | Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |
| `spec` | `object` | Specification of the desired behavior of the pod. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status> |

## .spec.install.spec.deployments\[\].spec.template.spec

Description
Specification of the desired behavior of the pod. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status>

Type
`object`

Required
- `containers`

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
<td style="text-align: left;"><p><code>activeDeadlineSeconds</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p>Optional duration in seconds the pod may be active on the node relative to StartTime before the system will actively try to mark it failed and kill associated containers. Value must be a positive integer.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>affinity</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>If specified, the pod’s scheduling constraints</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>automountServiceAccountToken</code></p></td>
<td style="text-align: left;"><p><code>boolean</code></p></td>
<td style="text-align: left;"><p>AutomountServiceAccountToken indicates whether a service account token should be automatically mounted.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>containers</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>List of containers belonging to the pod. Containers cannot currently be added or removed. There must be at least one container in a Pod. Cannot be updated.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>containers[]</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>A single application container that you want to run within a pod.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>dnsConfig</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>Specifies the DNS parameters of a pod. Parameters specified here will be merged to the generated DNS configuration based on DNSPolicy.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>dnsPolicy</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Set DNS policy for the pod. Defaults to "ClusterFirst". Valid values are 'ClusterFirstWithHostNet', 'ClusterFirst', 'Default' or 'None'. DNS parameters given in DNSConfig will be merged with the policy selected with DNSPolicy. To have DNS options set along with hostNetwork, you have to specify DNS policy explicitly to 'ClusterFirstWithHostNet'.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>enableServiceLinks</code></p></td>
<td style="text-align: left;"><p><code>boolean</code></p></td>
<td style="text-align: left;"><p>EnableServiceLinks indicates whether information about services should be injected into pod’s environment variables, matching the syntax of Docker links. Optional: Defaults to true.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>ephemeralContainers</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>List of ephemeral containers run in this pod. Ephemeral containers may be run in an existing pod to perform user-initiated actions such as debugging. This list cannot be specified when creating a pod, and it cannot be modified by updating the pod spec. In order to add an ephemeral container to an existing pod, use the pod’s ephemeralcontainers subresource.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>ephemeralContainers[]</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>An EphemeralContainer is a temporary container that you may add to an existing Pod for user-initiated activities such as debugging. Ephemeral containers have no resource or scheduling guarantees, and they will not be restarted when they exit or when a Pod is removed or restarted. The kubelet may evict a Pod if an ephemeral container causes the Pod to exceed its resource allocation.</p>
<p>To add an ephemeral container, use the ephemeralcontainers subresource of an existing Pod. Ephemeral containers may not be removed or restarted.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>hostAliases</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>HostAliases is an optional list of hosts and IPs that will be injected into the pod’s hosts file if specified.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>hostAliases[]</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>HostAlias holds the mapping between IP and hostnames that will be injected as an entry in the pod’s hosts file.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>hostIPC</code></p></td>
<td style="text-align: left;"><p><code>boolean</code></p></td>
<td style="text-align: left;"><p>Use the host’s ipc namespace. Optional: Default to false.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>hostNetwork</code></p></td>
<td style="text-align: left;"><p><code>boolean</code></p></td>
<td style="text-align: left;"><p>Host networking requested for this pod. Use the host’s network namespace. If this option is set, the ports that will be used must be specified. Default to false.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>hostPID</code></p></td>
<td style="text-align: left;"><p><code>boolean</code></p></td>
<td style="text-align: left;"><p>Use the host’s pid namespace. Optional: Default to false.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>hostUsers</code></p></td>
<td style="text-align: left;"><p><code>boolean</code></p></td>
<td style="text-align: left;"><p>Use the host’s user namespace. Optional: Default to true. If set to true or not present, the pod will be run in the host user namespace, useful for when the pod needs a feature only available to the host user namespace, such as loading a kernel module with CAP_SYS_MODULE. When set to false, a new userns is created for the pod. Setting false is useful for mitigating container breakout vulnerabilities even allowing users to run their containers as root without actually having root privileges on the host. This field is alpha-level and is only honored by servers that enable the UserNamespacesSupport feature.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>hostname</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Specifies the hostname of the Pod If not specified, the pod’s hostname will be set to a system-defined value.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>imagePullSecrets</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>ImagePullSecrets is an optional list of references to secrets in the same namespace to use for pulling any of the images used by this PodSpec. If specified, these secrets will be passed to individual puller implementations for them to use. More info: <a href="https://kubernetes.io/docs/concepts/containers/images#specifying-imagepullsecrets-on-a-pod">https://kubernetes.io/docs/concepts/containers/images#specifying-imagepullsecrets-on-a-pod</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>imagePullSecrets[]</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>LocalObjectReference contains enough information to let you locate the referenced object inside the same namespace.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>initContainers</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>List of initialization containers belonging to the pod. Init containers are executed in order prior to containers being started. If any init container fails, the pod is considered to have failed and is handled according to its restartPolicy. The name for an init container or normal container must be unique among all containers. Init containers may not have Lifecycle actions, Readiness probes, Liveness probes, or Startup probes. The resourceRequirements of an init container are taken into account during scheduling by finding the highest request/limit for each resource type, and then using the max of that value or the sum of the normal containers. Limits are applied to init containers in a similar fashion. Init containers cannot currently be added or removed. Cannot be updated. More info: <a href="https://kubernetes.io/docs/concepts/workloads/pods/init-containers/">https://kubernetes.io/docs/concepts/workloads/pods/init-containers/</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>initContainers[]</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>A single application container that you want to run within a pod.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>nodeName</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>NodeName indicates in which node this pod is scheduled. If empty, this pod is a candidate for scheduling by the scheduler defined in schedulerName. Once this field is set, the kubelet for this node becomes responsible for the lifecycle of this pod. This field should not be used to express a desire for the pod to be scheduled on a specific node. <a href="https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/#nodename">https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/#nodename</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>nodeSelector</code></p></td>
<td style="text-align: left;"><p><code>object (string)</code></p></td>
<td style="text-align: left;"><p>NodeSelector is a selector which must be true for the pod to fit on a node. Selector which must match a node’s labels for the pod to be scheduled on that node. More info: <a href="https://kubernetes.io/docs/concepts/configuration/assign-pod-node/">https://kubernetes.io/docs/concepts/configuration/assign-pod-node/</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>os</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>Specifies the OS of the containers in the pod. Some pod and container fields are restricted if this is set.</p>
<p>If the OS field is set to linux, the following fields must be unset: -securityContext.windowsOptions</p>
<p>If the OS field is set to windows, following fields must be unset: - spec.hostPID - spec.hostIPC - spec.hostUsers - spec.securityContext.appArmorProfile - spec.securityContext.seLinuxOptions - spec.securityContext.seccompProfile - spec.securityContext.fsGroup - spec.securityContext.fsGroupChangePolicy - spec.securityContext.sysctls - spec.shareProcessNamespace - spec.securityContext.runAsUser - spec.securityContext.runAsGroup - spec.securityContext.supplementalGroups - spec.securityContext.supplementalGroupsPolicy - spec.containers[<strong>].securityContext.appArmorProfile - spec.containers[</strong>].securityContext.seLinuxOptions - spec.containers[<strong>].securityContext.seccompProfile - spec.containers[</strong>].securityContext.capabilities - spec.containers[<strong>].securityContext.readOnlyRootFilesystem - spec.containers[</strong>].securityContext.privileged - spec.containers[<strong>].securityContext.allowPrivilegeEscalation - spec.containers[</strong>].securityContext.procMount - spec.containers[<strong>].securityContext.runAsUser - spec.containers[</strong>].securityContext.runAsGroup</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>overhead</code></p></td>
<td style="text-align: left;"><p><code>integer-or-string</code></p></td>
<td style="text-align: left;"><p>Overhead represents the resource overhead associated with running a pod for a given RuntimeClass. This field will be autopopulated at admission time by the RuntimeClass admission controller. If the RuntimeClass admission controller is enabled, overhead must not be set in Pod create requests. The RuntimeClass admission controller will reject Pod create requests which have the overhead already set. If RuntimeClass is configured and selected in the PodSpec, Overhead will be set to the value defined in the corresponding RuntimeClass, otherwise it will remain unset and treated as zero. More info: <a href="https://git.k8s.io/enhancements/keps/sig-node/688-pod-overhead/README.md">https://git.k8s.io/enhancements/keps/sig-node/688-pod-overhead/README.md</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>preemptionPolicy</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>PreemptionPolicy is the Policy for preempting pods with lower priority. One of Never, PreemptLowerPriority. Defaults to PreemptLowerPriority if unset.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>priority</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p>The priority value. Various system components use this field to find the priority of the pod. When Priority Admission Controller is enabled, it prevents users from setting this field. The admission controller populates this field from PriorityClassName. The higher the value, the higher the priority.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>priorityClassName</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>If specified, indicates the pod’s priority. "system-node-critical" and "system-cluster-critical" are two special keywords which indicate the highest priorities with the former being the highest priority. Any other name must be defined by creating a PriorityClass object with that name. If not specified, the pod priority will be default or zero if there is no default.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>readinessGates</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>If specified, all readiness gates will be evaluated for pod readiness. A pod is ready when all its containers are ready AND all conditions specified in the readiness gates have status equal to "True" More info: <a href="https://git.k8s.io/enhancements/keps/sig-network/580-pod-readiness-gates">https://git.k8s.io/enhancements/keps/sig-network/580-pod-readiness-gates</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>readinessGates[]</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>PodReadinessGate contains the reference to a pod condition</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>resourceClaims</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>ResourceClaims defines which ResourceClaims must be allocated and reserved before the Pod is allowed to start. The resources will be made available to those containers which consume them by name.</p>
<p>This is an alpha field and requires enabling the DynamicResourceAllocation feature gate.</p>
<p>This field is immutable.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>resourceClaims[]</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>PodResourceClaim references exactly one ResourceClaim, either directly or by naming a ResourceClaimTemplate which is then turned into a ResourceClaim for the pod.</p>
<p>It adds a name to it that uniquely identifies the ResourceClaim inside the Pod. Containers that need access to the ResourceClaim reference it with this name.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>resources</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>Resources is the total amount of CPU and Memory resources required by all containers in the pod. It supports specifying Requests and Limits for "cpu" and "memory" resource names only. ResourceClaims are not supported.</p>
<p>This field enables fine-grained control over resource allocation for the entire pod, allowing resource sharing among containers in a pod.</p>
<p>This is an alpha field and requires enabling the PodLevelResources feature gate.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>restartPolicy</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Restart policy for all containers within the pod. One of Always, OnFailure, Never. In some contexts, only a subset of those values may be permitted. Default to Always. More info: <a href="https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#restart-policy">https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#restart-policy</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>runtimeClassName</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>RuntimeClassName refers to a RuntimeClass object in the node.k8s.io group, which should be used to run this pod. If no RuntimeClass resource matches the named class, the pod will not be run. If unset or empty, the "legacy" RuntimeClass will be used, which is an implicit class with an empty definition that uses the default runtime handler. More info: <a href="https://git.k8s.io/enhancements/keps/sig-node/585-runtime-class">https://git.k8s.io/enhancements/keps/sig-node/585-runtime-class</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>schedulerName</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>If specified, the pod will be dispatched by specified scheduler. If not specified, the pod will be dispatched by default scheduler.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>schedulingGates</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>SchedulingGates is an opaque list of values that if specified will block scheduling the pod. If schedulingGates is not empty, the pod will stay in the SchedulingGated state and the scheduler will not attempt to schedule the pod.</p>
<p>SchedulingGates can only be set at pod creation time, and be removed only afterwards.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>schedulingGates[]</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>PodSchedulingGate is associated to a Pod to guard its scheduling.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>securityContext</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>SecurityContext holds pod-level security attributes and common container settings. Optional: Defaults to empty. See type description for default values of each field.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>serviceAccount</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>DeprecatedServiceAccount is a deprecated alias for ServiceAccountName. Deprecated: Use serviceAccountName instead.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>serviceAccountName</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>ServiceAccountName is the name of the ServiceAccount to use to run this pod. More info: <a href="https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/">https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>setHostnameAsFQDN</code></p></td>
<td style="text-align: left;"><p><code>boolean</code></p></td>
<td style="text-align: left;"><p>If true the pod’s hostname will be configured as the pod’s FQDN, rather than the leaf name (the default). In Linux containers, this means setting the FQDN in the hostname field of the kernel (the nodename field of struct utsname). In Windows containers, this means setting the registry value of hostname for the registry key HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Parameters to FQDN. If a pod does not have FQDN, this has no effect. Default to false.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>shareProcessNamespace</code></p></td>
<td style="text-align: left;"><p><code>boolean</code></p></td>
<td style="text-align: left;"><p>Share a single process namespace between all of the containers in a pod. When this is set containers will be able to view and signal processes from other containers in the same pod, and the first process in each container will not be assigned PID 1. HostPID and ShareProcessNamespace cannot both be set. Optional: Default to false.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>subdomain</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>If specified, the fully qualified Pod hostname will be "&lt;hostname&gt;.&lt;subdomain&gt;.&lt;pod namespace&gt;.svc.&lt;cluster domain&gt;". If not specified, the pod will not have a domainname at all.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>terminationGracePeriodSeconds</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p>Optional duration in seconds the pod needs to terminate gracefully. May be decreased in delete request. Value must be non-negative integer. The value zero indicates stop immediately via the kill signal (no opportunity to shut down). If this value is nil, the default grace period will be used instead. The grace period is the duration in seconds after the processes running in the pod are sent a termination signal and the time when the processes are forcibly halted with a kill signal. Set this value longer than the expected cleanup time for your process. Defaults to 30 seconds.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>tolerations</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>If specified, the pod’s tolerations.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>tolerations[]</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>The pod this Toleration is attached to tolerates any taint that matches the triple &lt;key,value,effect&gt; using the matching operator &lt;operator&gt;.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>topologySpreadConstraints</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>TopologySpreadConstraints describes how a group of pods ought to spread across topology domains. Scheduler will schedule pods in a way which abides by the constraints. All topologySpreadConstraints are ANDed.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>topologySpreadConstraints[]</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>TopologySpreadConstraint specifies how to spread matching pods among the given topology.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>volumes</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>List of volumes that can be mounted by containers belonging to the pod. More info: <a href="https://kubernetes.io/docs/concepts/storage/volumes">https://kubernetes.io/docs/concepts/storage/volumes</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>volumes[]</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>Volume represents a named volume in a pod that may be accessed by any container in the pod.</p></td>
</tr>
</tbody>
</table>

## .spec.install.spec.deployments\[\].spec.template.spec.affinity

Description
If specified, the pod’s scheduling constraints

Type
`object`

| Property | Type | Description |
|----|----|----|
| `nodeAffinity` | `object` | Describes node affinity scheduling rules for the pod. |
| `podAffinity` | `object` | Describes pod affinity scheduling rules (e.g. co-locate this pod in the same node, zone, etc. as some other pod(s)). |
| `podAntiAffinity` | `object` | Describes pod anti-affinity scheduling rules (e.g. avoid putting this pod in the same node, zone, etc. as some other pod(s)). |

## .spec.install.spec.deployments\[\].spec.template.spec.affinity.nodeAffinity

Description
Describes node affinity scheduling rules for the pod.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `preferredDuringSchedulingIgnoredDuringExecution` | `array` | The scheduler will prefer to schedule pods to nodes that satisfy the affinity expressions specified by this field, but it may choose a node that violates one or more of the expressions. The node that is most preferred is the one with the greatest sum of weights, i.e. for each node that meets all of the scheduling requirements (resource request, requiredDuringScheduling affinity expressions, etc.), compute a sum by iterating through the elements of this field and adding "weight" to the sum if the node matches the corresponding matchExpressions; the node(s) with the highest sum are the most preferred. |
| `preferredDuringSchedulingIgnoredDuringExecution[]` | `object` | An empty preferred scheduling term matches all objects with implicit weight 0 (i.e. it’s a no-op). A null preferred scheduling term matches no objects (i.e. is also a no-op). |
| `requiredDuringSchedulingIgnoredDuringExecution` | `object` | If the affinity requirements specified by this field are not met at scheduling time, the pod will not be scheduled onto the node. If the affinity requirements specified by this field cease to be met at some point during pod execution (e.g. due to an update), the system may or may not try to eventually evict the pod from its node. |

## .spec.install.spec.deployments\[\].spec.template.spec.affinity.nodeAffinity.preferredDuringSchedulingIgnoredDuringExecution

Description
The scheduler will prefer to schedule pods to nodes that satisfy the affinity expressions specified by this field, but it may choose a node that violates one or more of the expressions. The node that is most preferred is the one with the greatest sum of weights, i.e. for each node that meets all of the scheduling requirements (resource request, requiredDuringScheduling affinity expressions, etc.), compute a sum by iterating through the elements of this field and adding "weight" to the sum if the node matches the corresponding matchExpressions; the node(s) with the highest sum are the most preferred.

Type
`array`

## .spec.install.spec.deployments\[\].spec.template.spec.affinity.nodeAffinity.preferredDuringSchedulingIgnoredDuringExecution\[\]

Description
An empty preferred scheduling term matches all objects with implicit weight 0 (i.e. it’s a no-op). A null preferred scheduling term matches no objects (i.e. is also a no-op).

Type
`object`

Required
- `preference`

- `weight`

| Property | Type | Description |
|----|----|----|
| `preference` | `object` | A node selector term, associated with the corresponding weight. |
| `weight` | `integer` | Weight associated with matching the corresponding nodeSelectorTerm, in the range 1-100. |

## .spec.install.spec.deployments\[\].spec.template.spec.affinity.nodeAffinity.preferredDuringSchedulingIgnoredDuringExecution\[\].preference

Description
A node selector term, associated with the corresponding weight.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `matchExpressions` | `array` | A list of node selector requirements by node’s labels. |
| `matchExpressions[]` | `object` | A node selector requirement is a selector that contains values, a key, and an operator that relates the key and values. |
| `matchFields` | `array` | A list of node selector requirements by node’s fields. |
| `matchFields[]` | `object` | A node selector requirement is a selector that contains values, a key, and an operator that relates the key and values. |

## .spec.install.spec.deployments\[\].spec.template.spec.affinity.nodeAffinity.preferredDuringSchedulingIgnoredDuringExecution\[\].preference.matchExpressions

Description
A list of node selector requirements by node’s labels.

Type
`array`

## .spec.install.spec.deployments\[\].spec.template.spec.affinity.nodeAffinity.preferredDuringSchedulingIgnoredDuringExecution\[\].preference.matchExpressions\[\]

Description
A node selector requirement is a selector that contains values, a key, and an operator that relates the key and values.

Type
`object`

Required
- `key`

- `operator`

| Property | Type | Description |
|----|----|----|
| `key` | `string` | The label key that the selector applies to. |
| `operator` | `string` | Represents a key’s relationship to a set of values. Valid operators are In, NotIn, Exists, DoesNotExist. Gt, and Lt. |
| `values` | `array (string)` | An array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. If the operator is Gt or Lt, the values array must have a single element, which will be interpreted as an integer. This array is replaced during a strategic merge patch. |

## .spec.install.spec.deployments\[\].spec.template.spec.affinity.nodeAffinity.preferredDuringSchedulingIgnoredDuringExecution\[\].preference.matchFields

Description
A list of node selector requirements by node’s fields.

Type
`array`

## .spec.install.spec.deployments\[\].spec.template.spec.affinity.nodeAffinity.preferredDuringSchedulingIgnoredDuringExecution\[\].preference.matchFields\[\]

Description
A node selector requirement is a selector that contains values, a key, and an operator that relates the key and values.

Type
`object`

Required
- `key`

- `operator`

| Property | Type | Description |
|----|----|----|
| `key` | `string` | The label key that the selector applies to. |
| `operator` | `string` | Represents a key’s relationship to a set of values. Valid operators are In, NotIn, Exists, DoesNotExist. Gt, and Lt. |
| `values` | `array (string)` | An array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. If the operator is Gt or Lt, the values array must have a single element, which will be interpreted as an integer. This array is replaced during a strategic merge patch. |

## .spec.install.spec.deployments\[\].spec.template.spec.affinity.nodeAffinity.requiredDuringSchedulingIgnoredDuringExecution

Description
If the affinity requirements specified by this field are not met at scheduling time, the pod will not be scheduled onto the node. If the affinity requirements specified by this field cease to be met at some point during pod execution (e.g. due to an update), the system may or may not try to eventually evict the pod from its node.

Type
`object`

Required
- `nodeSelectorTerms`

| Property | Type | Description |
|----|----|----|
| `nodeSelectorTerms` | `array` | Required. A list of node selector terms. The terms are ORed. |
| `nodeSelectorTerms[]` | `object` | A null or empty node selector term matches no objects. The requirements of them are ANDed. The TopologySelectorTerm type implements a subset of the NodeSelectorTerm. |

## .spec.install.spec.deployments\[\].spec.template.spec.affinity.nodeAffinity.requiredDuringSchedulingIgnoredDuringExecution.nodeSelectorTerms

Description
Required. A list of node selector terms. The terms are ORed.

Type
`array`

## .spec.install.spec.deployments\[\].spec.template.spec.affinity.nodeAffinity.requiredDuringSchedulingIgnoredDuringExecution.nodeSelectorTerms\[\]

Description
A null or empty node selector term matches no objects. The requirements of them are ANDed. The TopologySelectorTerm type implements a subset of the NodeSelectorTerm.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `matchExpressions` | `array` | A list of node selector requirements by node’s labels. |
| `matchExpressions[]` | `object` | A node selector requirement is a selector that contains values, a key, and an operator that relates the key and values. |
| `matchFields` | `array` | A list of node selector requirements by node’s fields. |
| `matchFields[]` | `object` | A node selector requirement is a selector that contains values, a key, and an operator that relates the key and values. |

## .spec.install.spec.deployments\[\].spec.template.spec.affinity.nodeAffinity.requiredDuringSchedulingIgnoredDuringExecution.nodeSelectorTerms\[\].matchExpressions

Description
A list of node selector requirements by node’s labels.

Type
`array`

## .spec.install.spec.deployments\[\].spec.template.spec.affinity.nodeAffinity.requiredDuringSchedulingIgnoredDuringExecution.nodeSelectorTerms\[\].matchExpressions\[\]

Description
A node selector requirement is a selector that contains values, a key, and an operator that relates the key and values.

Type
`object`

Required
- `key`

- `operator`

| Property | Type | Description |
|----|----|----|
| `key` | `string` | The label key that the selector applies to. |
| `operator` | `string` | Represents a key’s relationship to a set of values. Valid operators are In, NotIn, Exists, DoesNotExist. Gt, and Lt. |
| `values` | `array (string)` | An array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. If the operator is Gt or Lt, the values array must have a single element, which will be interpreted as an integer. This array is replaced during a strategic merge patch. |

## .spec.install.spec.deployments\[\].spec.template.spec.affinity.nodeAffinity.requiredDuringSchedulingIgnoredDuringExecution.nodeSelectorTerms\[\].matchFields

Description
A list of node selector requirements by node’s fields.

Type
`array`

## .spec.install.spec.deployments\[\].spec.template.spec.affinity.nodeAffinity.requiredDuringSchedulingIgnoredDuringExecution.nodeSelectorTerms\[\].matchFields\[\]

Description
A node selector requirement is a selector that contains values, a key, and an operator that relates the key and values.

Type
`object`

Required
- `key`

- `operator`

| Property | Type | Description |
|----|----|----|
| `key` | `string` | The label key that the selector applies to. |
| `operator` | `string` | Represents a key’s relationship to a set of values. Valid operators are In, NotIn, Exists, DoesNotExist. Gt, and Lt. |
| `values` | `array (string)` | An array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. If the operator is Gt or Lt, the values array must have a single element, which will be interpreted as an integer. This array is replaced during a strategic merge patch. |

## .spec.install.spec.deployments\[\].spec.template.spec.affinity.podAffinity

Description
Describes pod affinity scheduling rules (e.g. co-locate this pod in the same node, zone, etc. as some other pod(s)).

Type
`object`

| Property | Type | Description |
|----|----|----|
| `preferredDuringSchedulingIgnoredDuringExecution` | `array` | The scheduler will prefer to schedule pods to nodes that satisfy the affinity expressions specified by this field, but it may choose a node that violates one or more of the expressions. The node that is most preferred is the one with the greatest sum of weights, i.e. for each node that meets all of the scheduling requirements (resource request, requiredDuringScheduling affinity expressions, etc.), compute a sum by iterating through the elements of this field and adding "weight" to the sum if the node has pods which matches the corresponding podAffinityTerm; the node(s) with the highest sum are the most preferred. |
| `preferredDuringSchedulingIgnoredDuringExecution[]` | `object` | The weights of all of the matched WeightedPodAffinityTerm fields are added per-node to find the most preferred node(s) |
| `requiredDuringSchedulingIgnoredDuringExecution` | `array` | If the affinity requirements specified by this field are not met at scheduling time, the pod will not be scheduled onto the node. If the affinity requirements specified by this field cease to be met at some point during pod execution (e.g. due to a pod label update), the system may or may not try to eventually evict the pod from its node. When there are multiple elements, the lists of nodes corresponding to each podAffinityTerm are intersected, i.e. all terms must be satisfied. |
| `requiredDuringSchedulingIgnoredDuringExecution[]` | `object` | Defines a set of pods (namely those matching the labelSelector relative to the given namespace(s)) that this pod should be co-located (affinity) or not co-located (anti-affinity) with, where co-located is defined as running on a node whose value of the label with key \<topologyKey\> matches that of any node on which a pod of the set of pods is running |

## .spec.install.spec.deployments\[\].spec.template.spec.affinity.podAffinity.preferredDuringSchedulingIgnoredDuringExecution

Description
The scheduler will prefer to schedule pods to nodes that satisfy the affinity expressions specified by this field, but it may choose a node that violates one or more of the expressions. The node that is most preferred is the one with the greatest sum of weights, i.e. for each node that meets all of the scheduling requirements (resource request, requiredDuringScheduling affinity expressions, etc.), compute a sum by iterating through the elements of this field and adding "weight" to the sum if the node has pods which matches the corresponding podAffinityTerm; the node(s) with the highest sum are the most preferred.

Type
`array`

## .spec.install.spec.deployments\[\].spec.template.spec.affinity.podAffinity.preferredDuringSchedulingIgnoredDuringExecution\[\]

Description
The weights of all of the matched WeightedPodAffinityTerm fields are added per-node to find the most preferred node(s)

Type
`object`

Required
- `podAffinityTerm`

- `weight`

| Property | Type | Description |
|----|----|----|
| `podAffinityTerm` | `object` | Required. A pod affinity term, associated with the corresponding weight. |
| `weight` | `integer` | weight associated with matching the corresponding podAffinityTerm, in the range 1-100. |

## .spec.install.spec.deployments\[\].spec.template.spec.affinity.podAffinity.preferredDuringSchedulingIgnoredDuringExecution\[\].podAffinityTerm

Description
Required. A pod affinity term, associated with the corresponding weight.

Type
`object`

Required
- `topologyKey`

| Property | Type | Description |
|----|----|----|
| `labelSelector` | `object` | A label query over a set of resources, in this case pods. If it’s null, this PodAffinityTerm matches with no Pods. |
| `matchLabelKeys` | `array (string)` | MatchLabelKeys is a set of pod label keys to select which pods will be taken into consideration. The keys are used to lookup values from the incoming pod labels, those key-value labels are merged with `labelSelector` as `key in (value)` to select the group of existing pods which pods will be taken into consideration for the incoming pod’s pod (anti) affinity. Keys that don’t exist in the incoming pod labels will be ignored. The default value is empty. The same key is forbidden to exist in both matchLabelKeys and labelSelector. Also, matchLabelKeys cannot be set when labelSelector isn’t set. |
| `mismatchLabelKeys` | `array (string)` | MismatchLabelKeys is a set of pod label keys to select which pods will be taken into consideration. The keys are used to lookup values from the incoming pod labels, those key-value labels are merged with `labelSelector` as `key notin (value)` to select the group of existing pods which pods will be taken into consideration for the incoming pod’s pod (anti) affinity. Keys that don’t exist in the incoming pod labels will be ignored. The default value is empty. The same key is forbidden to exist in both mismatchLabelKeys and labelSelector. Also, mismatchLabelKeys cannot be set when labelSelector isn’t set. |
| `namespaceSelector` | `object` | A label query over the set of namespaces that the term applies to. The term is applied to the union of the namespaces selected by this field and the ones listed in the namespaces field. null selector and null or empty namespaces list means "this pod’s namespace". An empty selector ({}) matches all namespaces. |
| `namespaces` | `array (string)` | namespaces specifies a static list of namespace names that the term applies to. The term is applied to the union of the namespaces listed in this field and the ones selected by namespaceSelector. null or empty namespaces list and null namespaceSelector means "this pod’s namespace". |
| `topologyKey` | `string` | This pod should be co-located (affinity) or not co-located (anti-affinity) with the pods matching the labelSelector in the specified namespaces, where co-located is defined as running on a node whose value of the label with key topologyKey matches that of any node on which any of the selected pods is running. Empty topologyKey is not allowed. |

## .spec.install.spec.deployments\[\].spec.template.spec.affinity.podAffinity.preferredDuringSchedulingIgnoredDuringExecution\[\].podAffinityTerm.labelSelector

Description
A label query over a set of resources, in this case pods. If it’s null, this PodAffinityTerm matches with no Pods.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `matchExpressions` | `array` | matchExpressions is a list of label selector requirements. The requirements are ANDed. |
| `matchExpressions[]` | `object` | A label selector requirement is a selector that contains values, a key, and an operator that relates the key and values. |
| `matchLabels` | `object (string)` | matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed. |

## .spec.install.spec.deployments\[\].spec.template.spec.affinity.podAffinity.preferredDuringSchedulingIgnoredDuringExecution\[\].podAffinityTerm.labelSelector.matchExpressions

Description
matchExpressions is a list of label selector requirements. The requirements are ANDed.

Type
`array`

## .spec.install.spec.deployments\[\].spec.template.spec.affinity.podAffinity.preferredDuringSchedulingIgnoredDuringExecution\[\].podAffinityTerm.labelSelector.matchExpressions\[\]

Description
A label selector requirement is a selector that contains values, a key, and an operator that relates the key and values.

Type
`object`

Required
- `key`

- `operator`

| Property | Type | Description |
|----|----|----|
| `key` | `string` | key is the label key that the selector applies to. |
| `operator` | `string` | operator represents a key’s relationship to a set of values. Valid operators are In, NotIn, Exists and DoesNotExist. |
| `values` | `array (string)` | values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch. |

## .spec.install.spec.deployments\[\].spec.template.spec.affinity.podAffinity.preferredDuringSchedulingIgnoredDuringExecution\[\].podAffinityTerm.namespaceSelector

Description
A label query over the set of namespaces that the term applies to. The term is applied to the union of the namespaces selected by this field and the ones listed in the namespaces field. null selector and null or empty namespaces list means "this pod’s namespace". An empty selector ({}) matches all namespaces.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `matchExpressions` | `array` | matchExpressions is a list of label selector requirements. The requirements are ANDed. |
| `matchExpressions[]` | `object` | A label selector requirement is a selector that contains values, a key, and an operator that relates the key and values. |
| `matchLabels` | `object (string)` | matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed. |

## .spec.install.spec.deployments\[\].spec.template.spec.affinity.podAffinity.preferredDuringSchedulingIgnoredDuringExecution\[\].podAffinityTerm.namespaceSelector.matchExpressions

Description
matchExpressions is a list of label selector requirements. The requirements are ANDed.

Type
`array`

## .spec.install.spec.deployments\[\].spec.template.spec.affinity.podAffinity.preferredDuringSchedulingIgnoredDuringExecution\[\].podAffinityTerm.namespaceSelector.matchExpressions\[\]

Description
A label selector requirement is a selector that contains values, a key, and an operator that relates the key and values.

Type
`object`

Required
- `key`

- `operator`

| Property | Type | Description |
|----|----|----|
| `key` | `string` | key is the label key that the selector applies to. |
| `operator` | `string` | operator represents a key’s relationship to a set of values. Valid operators are In, NotIn, Exists and DoesNotExist. |
| `values` | `array (string)` | values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch. |

## .spec.install.spec.deployments\[\].spec.template.spec.affinity.podAffinity.requiredDuringSchedulingIgnoredDuringExecution

Description
If the affinity requirements specified by this field are not met at scheduling time, the pod will not be scheduled onto the node. If the affinity requirements specified by this field cease to be met at some point during pod execution (e.g. due to a pod label update), the system may or may not try to eventually evict the pod from its node. When there are multiple elements, the lists of nodes corresponding to each podAffinityTerm are intersected, i.e. all terms must be satisfied.

Type
`array`

## .spec.install.spec.deployments\[\].spec.template.spec.affinity.podAffinity.requiredDuringSchedulingIgnoredDuringExecution\[\]

Description
Defines a set of pods (namely those matching the labelSelector relative to the given namespace(s)) that this pod should be co-located (affinity) or not co-located (anti-affinity) with, where co-located is defined as running on a node whose value of the label with key \<topologyKey\> matches that of any node on which a pod of the set of pods is running

Type
`object`

Required
- `topologyKey`

| Property | Type | Description |
|----|----|----|
| `labelSelector` | `object` | A label query over a set of resources, in this case pods. If it’s null, this PodAffinityTerm matches with no Pods. |
| `matchLabelKeys` | `array (string)` | MatchLabelKeys is a set of pod label keys to select which pods will be taken into consideration. The keys are used to lookup values from the incoming pod labels, those key-value labels are merged with `labelSelector` as `key in (value)` to select the group of existing pods which pods will be taken into consideration for the incoming pod’s pod (anti) affinity. Keys that don’t exist in the incoming pod labels will be ignored. The default value is empty. The same key is forbidden to exist in both matchLabelKeys and labelSelector. Also, matchLabelKeys cannot be set when labelSelector isn’t set. |
| `mismatchLabelKeys` | `array (string)` | MismatchLabelKeys is a set of pod label keys to select which pods will be taken into consideration. The keys are used to lookup values from the incoming pod labels, those key-value labels are merged with `labelSelector` as `key notin (value)` to select the group of existing pods which pods will be taken into consideration for the incoming pod’s pod (anti) affinity. Keys that don’t exist in the incoming pod labels will be ignored. The default value is empty. The same key is forbidden to exist in both mismatchLabelKeys and labelSelector. Also, mismatchLabelKeys cannot be set when labelSelector isn’t set. |
| `namespaceSelector` | `object` | A label query over the set of namespaces that the term applies to. The term is applied to the union of the namespaces selected by this field and the ones listed in the namespaces field. null selector and null or empty namespaces list means "this pod’s namespace". An empty selector ({}) matches all namespaces. |
| `namespaces` | `array (string)` | namespaces specifies a static list of namespace names that the term applies to. The term is applied to the union of the namespaces listed in this field and the ones selected by namespaceSelector. null or empty namespaces list and null namespaceSelector means "this pod’s namespace". |
| `topologyKey` | `string` | This pod should be co-located (affinity) or not co-located (anti-affinity) with the pods matching the labelSelector in the specified namespaces, where co-located is defined as running on a node whose value of the label with key topologyKey matches that of any node on which any of the selected pods is running. Empty topologyKey is not allowed. |

## .spec.install.spec.deployments\[\].spec.template.spec.affinity.podAffinity.requiredDuringSchedulingIgnoredDuringExecution\[\].labelSelector

Description
A label query over a set of resources, in this case pods. If it’s null, this PodAffinityTerm matches with no Pods.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `matchExpressions` | `array` | matchExpressions is a list of label selector requirements. The requirements are ANDed. |
| `matchExpressions[]` | `object` | A label selector requirement is a selector that contains values, a key, and an operator that relates the key and values. |
| `matchLabels` | `object (string)` | matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed. |

## .spec.install.spec.deployments\[\].spec.template.spec.affinity.podAffinity.requiredDuringSchedulingIgnoredDuringExecution\[\].labelSelector.matchExpressions

Description
matchExpressions is a list of label selector requirements. The requirements are ANDed.

Type
`array`

## .spec.install.spec.deployments\[\].spec.template.spec.affinity.podAffinity.requiredDuringSchedulingIgnoredDuringExecution\[\].labelSelector.matchExpressions\[\]

Description
A label selector requirement is a selector that contains values, a key, and an operator that relates the key and values.

Type
`object`

Required
- `key`

- `operator`

| Property | Type | Description |
|----|----|----|
| `key` | `string` | key is the label key that the selector applies to. |
| `operator` | `string` | operator represents a key’s relationship to a set of values. Valid operators are In, NotIn, Exists and DoesNotExist. |
| `values` | `array (string)` | values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch. |

## .spec.install.spec.deployments\[\].spec.template.spec.affinity.podAffinity.requiredDuringSchedulingIgnoredDuringExecution\[\].namespaceSelector

Description
A label query over the set of namespaces that the term applies to. The term is applied to the union of the namespaces selected by this field and the ones listed in the namespaces field. null selector and null or empty namespaces list means "this pod’s namespace". An empty selector ({}) matches all namespaces.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `matchExpressions` | `array` | matchExpressions is a list of label selector requirements. The requirements are ANDed. |
| `matchExpressions[]` | `object` | A label selector requirement is a selector that contains values, a key, and an operator that relates the key and values. |
| `matchLabels` | `object (string)` | matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed. |

## .spec.install.spec.deployments\[\].spec.template.spec.affinity.podAffinity.requiredDuringSchedulingIgnoredDuringExecution\[\].namespaceSelector.matchExpressions

Description
matchExpressions is a list of label selector requirements. The requirements are ANDed.

Type
`array`

## .spec.install.spec.deployments\[\].spec.template.spec.affinity.podAffinity.requiredDuringSchedulingIgnoredDuringExecution\[\].namespaceSelector.matchExpressions\[\]

Description
A label selector requirement is a selector that contains values, a key, and an operator that relates the key and values.

Type
`object`

Required
- `key`

- `operator`

| Property | Type | Description |
|----|----|----|
| `key` | `string` | key is the label key that the selector applies to. |
| `operator` | `string` | operator represents a key’s relationship to a set of values. Valid operators are In, NotIn, Exists and DoesNotExist. |
| `values` | `array (string)` | values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch. |

## .spec.install.spec.deployments\[\].spec.template.spec.affinity.podAntiAffinity

Description
Describes pod anti-affinity scheduling rules (e.g. avoid putting this pod in the same node, zone, etc. as some other pod(s)).

Type
`object`

| Property | Type | Description |
|----|----|----|
| `preferredDuringSchedulingIgnoredDuringExecution` | `array` | The scheduler will prefer to schedule pods to nodes that satisfy the anti-affinity expressions specified by this field, but it may choose a node that violates one or more of the expressions. The node that is most preferred is the one with the greatest sum of weights, i.e. for each node that meets all of the scheduling requirements (resource request, requiredDuringScheduling anti-affinity expressions, etc.), compute a sum by iterating through the elements of this field and adding "weight" to the sum if the node has pods which matches the corresponding podAffinityTerm; the node(s) with the highest sum are the most preferred. |
| `preferredDuringSchedulingIgnoredDuringExecution[]` | `object` | The weights of all of the matched WeightedPodAffinityTerm fields are added per-node to find the most preferred node(s) |
| `requiredDuringSchedulingIgnoredDuringExecution` | `array` | If the anti-affinity requirements specified by this field are not met at scheduling time, the pod will not be scheduled onto the node. If the anti-affinity requirements specified by this field cease to be met at some point during pod execution (e.g. due to a pod label update), the system may or may not try to eventually evict the pod from its node. When there are multiple elements, the lists of nodes corresponding to each podAffinityTerm are intersected, i.e. all terms must be satisfied. |
| `requiredDuringSchedulingIgnoredDuringExecution[]` | `object` | Defines a set of pods (namely those matching the labelSelector relative to the given namespace(s)) that this pod should be co-located (affinity) or not co-located (anti-affinity) with, where co-located is defined as running on a node whose value of the label with key \<topologyKey\> matches that of any node on which a pod of the set of pods is running |

## .spec.install.spec.deployments\[\].spec.template.spec.affinity.podAntiAffinity.preferredDuringSchedulingIgnoredDuringExecution

Description
The scheduler will prefer to schedule pods to nodes that satisfy the anti-affinity expressions specified by this field, but it may choose a node that violates one or more of the expressions. The node that is most preferred is the one with the greatest sum of weights, i.e. for each node that meets all of the scheduling requirements (resource request, requiredDuringScheduling anti-affinity expressions, etc.), compute a sum by iterating through the elements of this field and adding "weight" to the sum if the node has pods which matches the corresponding podAffinityTerm; the node(s) with the highest sum are the most preferred.

Type
`array`

## .spec.install.spec.deployments\[\].spec.template.spec.affinity.podAntiAffinity.preferredDuringSchedulingIgnoredDuringExecution\[\]

Description
The weights of all of the matched WeightedPodAffinityTerm fields are added per-node to find the most preferred node(s)

Type
`object`

Required
- `podAffinityTerm`

- `weight`

| Property | Type | Description |
|----|----|----|
| `podAffinityTerm` | `object` | Required. A pod affinity term, associated with the corresponding weight. |
| `weight` | `integer` | weight associated with matching the corresponding podAffinityTerm, in the range 1-100. |

## .spec.install.spec.deployments\[\].spec.template.spec.affinity.podAntiAffinity.preferredDuringSchedulingIgnoredDuringExecution\[\].podAffinityTerm

Description
Required. A pod affinity term, associated with the corresponding weight.

Type
`object`

Required
- `topologyKey`

| Property | Type | Description |
|----|----|----|
| `labelSelector` | `object` | A label query over a set of resources, in this case pods. If it’s null, this PodAffinityTerm matches with no Pods. |
| `matchLabelKeys` | `array (string)` | MatchLabelKeys is a set of pod label keys to select which pods will be taken into consideration. The keys are used to lookup values from the incoming pod labels, those key-value labels are merged with `labelSelector` as `key in (value)` to select the group of existing pods which pods will be taken into consideration for the incoming pod’s pod (anti) affinity. Keys that don’t exist in the incoming pod labels will be ignored. The default value is empty. The same key is forbidden to exist in both matchLabelKeys and labelSelector. Also, matchLabelKeys cannot be set when labelSelector isn’t set. |
| `mismatchLabelKeys` | `array (string)` | MismatchLabelKeys is a set of pod label keys to select which pods will be taken into consideration. The keys are used to lookup values from the incoming pod labels, those key-value labels are merged with `labelSelector` as `key notin (value)` to select the group of existing pods which pods will be taken into consideration for the incoming pod’s pod (anti) affinity. Keys that don’t exist in the incoming pod labels will be ignored. The default value is empty. The same key is forbidden to exist in both mismatchLabelKeys and labelSelector. Also, mismatchLabelKeys cannot be set when labelSelector isn’t set. |
| `namespaceSelector` | `object` | A label query over the set of namespaces that the term applies to. The term is applied to the union of the namespaces selected by this field and the ones listed in the namespaces field. null selector and null or empty namespaces list means "this pod’s namespace". An empty selector ({}) matches all namespaces. |
| `namespaces` | `array (string)` | namespaces specifies a static list of namespace names that the term applies to. The term is applied to the union of the namespaces listed in this field and the ones selected by namespaceSelector. null or empty namespaces list and null namespaceSelector means "this pod’s namespace". |
| `topologyKey` | `string` | This pod should be co-located (affinity) or not co-located (anti-affinity) with the pods matching the labelSelector in the specified namespaces, where co-located is defined as running on a node whose value of the label with key topologyKey matches that of any node on which any of the selected pods is running. Empty topologyKey is not allowed. |

## .spec.install.spec.deployments\[\].spec.template.spec.affinity.podAntiAffinity.preferredDuringSchedulingIgnoredDuringExecution\[\].podAffinityTerm.labelSelector

Description
A label query over a set of resources, in this case pods. If it’s null, this PodAffinityTerm matches with no Pods.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `matchExpressions` | `array` | matchExpressions is a list of label selector requirements. The requirements are ANDed. |
| `matchExpressions[]` | `object` | A label selector requirement is a selector that contains values, a key, and an operator that relates the key and values. |
| `matchLabels` | `object (string)` | matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed. |

## .spec.install.spec.deployments\[\].spec.template.spec.affinity.podAntiAffinity.preferredDuringSchedulingIgnoredDuringExecution\[\].podAffinityTerm.labelSelector.matchExpressions

Description
matchExpressions is a list of label selector requirements. The requirements are ANDed.

Type
`array`

## .spec.install.spec.deployments\[\].spec.template.spec.affinity.podAntiAffinity.preferredDuringSchedulingIgnoredDuringExecution\[\].podAffinityTerm.labelSelector.matchExpressions\[\]

Description
A label selector requirement is a selector that contains values, a key, and an operator that relates the key and values.

Type
`object`

Required
- `key`

- `operator`

| Property | Type | Description |
|----|----|----|
| `key` | `string` | key is the label key that the selector applies to. |
| `operator` | `string` | operator represents a key’s relationship to a set of values. Valid operators are In, NotIn, Exists and DoesNotExist. |
| `values` | `array (string)` | values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch. |

## .spec.install.spec.deployments\[\].spec.template.spec.affinity.podAntiAffinity.preferredDuringSchedulingIgnoredDuringExecution\[\].podAffinityTerm.namespaceSelector

Description
A label query over the set of namespaces that the term applies to. The term is applied to the union of the namespaces selected by this field and the ones listed in the namespaces field. null selector and null or empty namespaces list means "this pod’s namespace". An empty selector ({}) matches all namespaces.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `matchExpressions` | `array` | matchExpressions is a list of label selector requirements. The requirements are ANDed. |
| `matchExpressions[]` | `object` | A label selector requirement is a selector that contains values, a key, and an operator that relates the key and values. |
| `matchLabels` | `object (string)` | matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed. |

## .spec.install.spec.deployments\[\].spec.template.spec.affinity.podAntiAffinity.preferredDuringSchedulingIgnoredDuringExecution\[\].podAffinityTerm.namespaceSelector.matchExpressions

Description
matchExpressions is a list of label selector requirements. The requirements are ANDed.

Type
`array`

## .spec.install.spec.deployments\[\].spec.template.spec.affinity.podAntiAffinity.preferredDuringSchedulingIgnoredDuringExecution\[\].podAffinityTerm.namespaceSelector.matchExpressions\[\]

Description
A label selector requirement is a selector that contains values, a key, and an operator that relates the key and values.

Type
`object`

Required
- `key`

- `operator`

| Property | Type | Description |
|----|----|----|
| `key` | `string` | key is the label key that the selector applies to. |
| `operator` | `string` | operator represents a key’s relationship to a set of values. Valid operators are In, NotIn, Exists and DoesNotExist. |
| `values` | `array (string)` | values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch. |

## .spec.install.spec.deployments\[\].spec.template.spec.affinity.podAntiAffinity.requiredDuringSchedulingIgnoredDuringExecution

Description
If the anti-affinity requirements specified by this field are not met at scheduling time, the pod will not be scheduled onto the node. If the anti-affinity requirements specified by this field cease to be met at some point during pod execution (e.g. due to a pod label update), the system may or may not try to eventually evict the pod from its node. When there are multiple elements, the lists of nodes corresponding to each podAffinityTerm are intersected, i.e. all terms must be satisfied.

Type
`array`

## .spec.install.spec.deployments\[\].spec.template.spec.affinity.podAntiAffinity.requiredDuringSchedulingIgnoredDuringExecution\[\]

Description
Defines a set of pods (namely those matching the labelSelector relative to the given namespace(s)) that this pod should be co-located (affinity) or not co-located (anti-affinity) with, where co-located is defined as running on a node whose value of the label with key \<topologyKey\> matches that of any node on which a pod of the set of pods is running

Type
`object`

Required
- `topologyKey`

| Property | Type | Description |
|----|----|----|
| `labelSelector` | `object` | A label query over a set of resources, in this case pods. If it’s null, this PodAffinityTerm matches with no Pods. |
| `matchLabelKeys` | `array (string)` | MatchLabelKeys is a set of pod label keys to select which pods will be taken into consideration. The keys are used to lookup values from the incoming pod labels, those key-value labels are merged with `labelSelector` as `key in (value)` to select the group of existing pods which pods will be taken into consideration for the incoming pod’s pod (anti) affinity. Keys that don’t exist in the incoming pod labels will be ignored. The default value is empty. The same key is forbidden to exist in both matchLabelKeys and labelSelector. Also, matchLabelKeys cannot be set when labelSelector isn’t set. |
| `mismatchLabelKeys` | `array (string)` | MismatchLabelKeys is a set of pod label keys to select which pods will be taken into consideration. The keys are used to lookup values from the incoming pod labels, those key-value labels are merged with `labelSelector` as `key notin (value)` to select the group of existing pods which pods will be taken into consideration for the incoming pod’s pod (anti) affinity. Keys that don’t exist in the incoming pod labels will be ignored. The default value is empty. The same key is forbidden to exist in both mismatchLabelKeys and labelSelector. Also, mismatchLabelKeys cannot be set when labelSelector isn’t set. |
| `namespaceSelector` | `object` | A label query over the set of namespaces that the term applies to. The term is applied to the union of the namespaces selected by this field and the ones listed in the namespaces field. null selector and null or empty namespaces list means "this pod’s namespace". An empty selector ({}) matches all namespaces. |
| `namespaces` | `array (string)` | namespaces specifies a static list of namespace names that the term applies to. The term is applied to the union of the namespaces listed in this field and the ones selected by namespaceSelector. null or empty namespaces list and null namespaceSelector means "this pod’s namespace". |
| `topologyKey` | `string` | This pod should be co-located (affinity) or not co-located (anti-affinity) with the pods matching the labelSelector in the specified namespaces, where co-located is defined as running on a node whose value of the label with key topologyKey matches that of any node on which any of the selected pods is running. Empty topologyKey is not allowed. |

## .spec.install.spec.deployments\[\].spec.template.spec.affinity.podAntiAffinity.requiredDuringSchedulingIgnoredDuringExecution\[\].labelSelector

Description
A label query over a set of resources, in this case pods. If it’s null, this PodAffinityTerm matches with no Pods.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `matchExpressions` | `array` | matchExpressions is a list of label selector requirements. The requirements are ANDed. |
| `matchExpressions[]` | `object` | A label selector requirement is a selector that contains values, a key, and an operator that relates the key and values. |
| `matchLabels` | `object (string)` | matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed. |

## .spec.install.spec.deployments\[\].spec.template.spec.affinity.podAntiAffinity.requiredDuringSchedulingIgnoredDuringExecution\[\].labelSelector.matchExpressions

Description
matchExpressions is a list of label selector requirements. The requirements are ANDed.

Type
`array`

## .spec.install.spec.deployments\[\].spec.template.spec.affinity.podAntiAffinity.requiredDuringSchedulingIgnoredDuringExecution\[\].labelSelector.matchExpressions\[\]

Description
A label selector requirement is a selector that contains values, a key, and an operator that relates the key and values.

Type
`object`

Required
- `key`

- `operator`

| Property | Type | Description |
|----|----|----|
| `key` | `string` | key is the label key that the selector applies to. |
| `operator` | `string` | operator represents a key’s relationship to a set of values. Valid operators are In, NotIn, Exists and DoesNotExist. |
| `values` | `array (string)` | values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch. |

## .spec.install.spec.deployments\[\].spec.template.spec.affinity.podAntiAffinity.requiredDuringSchedulingIgnoredDuringExecution\[\].namespaceSelector

Description
A label query over the set of namespaces that the term applies to. The term is applied to the union of the namespaces selected by this field and the ones listed in the namespaces field. null selector and null or empty namespaces list means "this pod’s namespace". An empty selector ({}) matches all namespaces.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `matchExpressions` | `array` | matchExpressions is a list of label selector requirements. The requirements are ANDed. |
| `matchExpressions[]` | `object` | A label selector requirement is a selector that contains values, a key, and an operator that relates the key and values. |
| `matchLabels` | `object (string)` | matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed. |

## .spec.install.spec.deployments\[\].spec.template.spec.affinity.podAntiAffinity.requiredDuringSchedulingIgnoredDuringExecution\[\].namespaceSelector.matchExpressions

Description
matchExpressions is a list of label selector requirements. The requirements are ANDed.

Type
`array`

## .spec.install.spec.deployments\[\].spec.template.spec.affinity.podAntiAffinity.requiredDuringSchedulingIgnoredDuringExecution\[\].namespaceSelector.matchExpressions\[\]

Description
A label selector requirement is a selector that contains values, a key, and an operator that relates the key and values.

Type
`object`

Required
- `key`

- `operator`

| Property | Type | Description |
|----|----|----|
| `key` | `string` | key is the label key that the selector applies to. |
| `operator` | `string` | operator represents a key’s relationship to a set of values. Valid operators are In, NotIn, Exists and DoesNotExist. |
| `values` | `array (string)` | values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch. |

## .spec.install.spec.deployments\[\].spec.template.spec.containers

Description
List of containers belonging to the pod. Containers cannot currently be added or removed. There must be at least one container in a Pod. Cannot be updated.

Type
`array`

## .spec.install.spec.deployments\[\].spec.template.spec.containers\[\]

Description
A single application container that you want to run within a pod.

Type
`object`

Required
- `name`

| Property | Type | Description |
|----|----|----|
| `args` | `array (string)` | Arguments to the entrypoint. The container image’s CMD is used if this is not provided. Variable references \$(VAR_NAME) are expanded using the container’s environment. If a variable cannot be resolved, the reference in the input string will be unchanged. Double are reduced to a single \$, which allows for escaping the \$(VAR_NAME) syntax: i.e. "(VAR_NAME)" will produce the string literal "\$(VAR_NAME)". Escaped references will never be expanded, regardless of whether the variable exists or not. Cannot be updated. More info: <https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#running-a-command-in-a-shell> |
| `command` | `array (string)` | Entrypoint array. Not executed within a shell. The container image’s ENTRYPOINT is used if this is not provided. Variable references \$(VAR_NAME) are expanded using the container’s environment. If a variable cannot be resolved, the reference in the input string will be unchanged. Double are reduced to a single \$, which allows for escaping the \$(VAR_NAME) syntax: i.e. "(VAR_NAME)" will produce the string literal "\$(VAR_NAME)". Escaped references will never be expanded, regardless of whether the variable exists or not. Cannot be updated. More info: <https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#running-a-command-in-a-shell> |
| `env` | `array` | List of environment variables to set in the container. Cannot be updated. |
| `env[]` | `object` | EnvVar represents an environment variable present in a Container. |
| `envFrom` | `array` | List of sources to populate environment variables in the container. The keys defined within a source must be a C_IDENTIFIER. All invalid keys will be reported as an event when the container is starting. When a key exists in multiple sources, the value associated with the last source will take precedence. Values defined by an Env with a duplicate key will take precedence. Cannot be updated. |
| `envFrom[]` | `object` | EnvFromSource represents the source of a set of ConfigMaps or Secrets |
| `image` | `string` | Container image name. More info: <https://kubernetes.io/docs/concepts/containers/images> This field is optional to allow higher level config management to default or override container images in workload controllers like Deployments and StatefulSets. |
| `imagePullPolicy` | `string` | Image pull policy. One of Always, Never, IfNotPresent. Defaults to Always if :latest tag is specified, or IfNotPresent otherwise. Cannot be updated. More info: <https://kubernetes.io/docs/concepts/containers/images#updating-images> |
| `lifecycle` | `object` | Actions that the management system should take in response to container lifecycle events. Cannot be updated. |
| `livenessProbe` | `object` | Periodic probe of container liveness. Container will be restarted if the probe fails. Cannot be updated. More info: <https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes> |
| `name` | `string` | Name of the container specified as a DNS_LABEL. Each container in a pod must have a unique name (DNS_LABEL). Cannot be updated. |
| `ports` | `array` | List of ports to expose from the container. Not specifying a port here DOES NOT prevent that port from being exposed. Any port which is listening on the default "0.0.0.0" address inside a container will be accessible from the network. Modifying this array with strategic merge patch may corrupt the data. For more information See <https://github.com/kubernetes/kubernetes/issues/108255>. Cannot be updated. |
| `ports[]` | `object` | ContainerPort represents a network port in a single container. |
| `readinessProbe` | `object` | Periodic probe of container service readiness. Container will be removed from service endpoints if the probe fails. Cannot be updated. More info: <https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes> |
| `resizePolicy` | `array` | Resources resize policy for the container. |
| `resizePolicy[]` | `object` | ContainerResizePolicy represents resource resize policy for the container. |
| `resources` | `object` | Compute Resources required by this container. Cannot be updated. More info: <https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/> |
| `restartPolicy` | `string` | RestartPolicy defines the restart behavior of individual containers in a pod. This field may only be set for init containers, and the only allowed value is "Always". For non-init containers or when this field is not specified, the restart behavior is defined by the Pod’s restart policy and the container type. Setting the RestartPolicy as "Always" for the init container will have the following effect: this init container will be continually restarted on exit until all regular containers have terminated. Once all regular containers have completed, all init containers with restartPolicy "Always" will be shut down. This lifecycle differs from normal init containers and is often referred to as a "sidecar" container. Although this init container still starts in the init container sequence, it does not wait for the container to complete before proceeding to the next init container. Instead, the next init container starts immediately after this init container is started, or after any startupProbe has successfully completed. |
| `securityContext` | `object` | SecurityContext defines the security options the container should be run with. If set, the fields of SecurityContext override the equivalent fields of PodSecurityContext. More info: <https://kubernetes.io/docs/tasks/configure-pod-container/security-context/> |
| `startupProbe` | `object` | StartupProbe indicates that the Pod has successfully initialized. If specified, no other probes are executed until this completes successfully. If this probe fails, the Pod will be restarted, just as if the livenessProbe failed. This can be used to provide different probe parameters at the beginning of a Pod’s lifecycle, when it might take a long time to load data or warm a cache, than during steady-state operation. This cannot be updated. More info: <https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes> |
| `stdin` | `boolean` | Whether this container should allocate a buffer for stdin in the container runtime. If this is not set, reads from stdin in the container will always result in EOF. Default is false. |
| `stdinOnce` | `boolean` | Whether the container runtime should close the stdin channel after it has been opened by a single attach. When stdin is true the stdin stream will remain open across multiple attach sessions. If stdinOnce is set to true, stdin is opened on container start, is empty until the first client attaches to stdin, and then remains open and accepts data until the client disconnects, at which time stdin is closed and remains closed until the container is restarted. If this flag is false, a container processes that reads from stdin will never receive an EOF. Default is false |
| `terminationMessagePath` | `string` | Optional: Path at which the file to which the container’s termination message will be written is mounted into the container’s filesystem. Message written is intended to be brief final status, such as an assertion failure message. Will be truncated by the node if greater than 4096 bytes. The total message length across all containers will be limited to 12kb. Defaults to /dev/termination-log. Cannot be updated. |
| `terminationMessagePolicy` | `string` | Indicate how the termination message should be populated. File will use the contents of terminationMessagePath to populate the container status message on both success and failure. FallbackToLogsOnError will use the last chunk of container log output if the termination message file is empty and the container exited with an error. The log output is limited to 2048 bytes or 80 lines, whichever is smaller. Defaults to File. Cannot be updated. |
| `tty` | `boolean` | Whether this container should allocate a TTY for itself, also requires 'stdin' to be true. Default is false. |
| `volumeDevices` | `array` | volumeDevices is the list of block devices to be used by the container. |
| `volumeDevices[]` | `object` | volumeDevice describes a mapping of a raw block device within a container. |
| `volumeMounts` | `array` | Pod volumes to mount into the container’s filesystem. Cannot be updated. |
| `volumeMounts[]` | `object` | VolumeMount describes a mounting of a Volume within a container. |
| `workingDir` | `string` | Container’s working directory. If not specified, the container runtime’s default will be used, which might be configured in the container image. Cannot be updated. |

## .spec.install.spec.deployments\[\].spec.template.spec.containers\[\].env

Description
List of environment variables to set in the container. Cannot be updated.

Type
`array`

## .spec.install.spec.deployments\[\].spec.template.spec.containers\[\].env\[\]

Description
EnvVar represents an environment variable present in a Container.

Type
`object`

Required
- `name`

| Property | Type | Description |
|----|----|----|
| `name` | `string` | Name of the environment variable. Must be a C_IDENTIFIER. |
| `value` | `string` | Variable references \$(VAR_NAME) are expanded using the previously defined environment variables in the container and any service environment variables. If a variable cannot be resolved, the reference in the input string will be unchanged. Double are reduced to a single \$, which allows for escaping the \$(VAR_NAME) syntax: i.e. "(VAR_NAME)" will produce the string literal "\$(VAR_NAME)". Escaped references will never be expanded, regardless of whether the variable exists or not. Defaults to "". |
| `valueFrom` | `object` | Source for the environment variable’s value. Cannot be used if value is not empty. |

## .spec.install.spec.deployments\[\].spec.template.spec.containers\[\].env\[\].valueFrom

Description
Source for the environment variable’s value. Cannot be used if value is not empty.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `configMapKeyRef` | `object` | Selects a key of a ConfigMap. |
| `fieldRef` | `object` | Selects a field of the pod: supports metadata.name, metadata.namespace, `metadata.labels['<KEY>']`, `metadata.annotations['<KEY>']`, spec.nodeName, spec.serviceAccountName, status.hostIP, status.podIP, status.podIPs. |
| `resourceFieldRef` | `object` | Selects a resource of the container: only resources limits and requests (limits.cpu, limits.memory, limits.ephemeral-storage, requests.cpu, requests.memory and requests.ephemeral-storage) are currently supported. |
| `secretKeyRef` | `object` | Selects a key of a secret in the pod’s namespace |

## .spec.install.spec.deployments\[\].spec.template.spec.containers\[\].env\[\].valueFrom.configMapKeyRef

Description
Selects a key of a ConfigMap.

Type
`object`

Required
- `key`

| Property | Type | Description |
|----|----|----|
| `key` | `string` | The key to select. |
| `name` | `string` | Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names> |
| `optional` | `boolean` | Specify whether the ConfigMap or its key must be defined |

## .spec.install.spec.deployments\[\].spec.template.spec.containers\[\].env\[\].valueFrom.fieldRef

Description
Selects a field of the pod: supports metadata.name, metadata.namespace, `metadata.labels['<KEY>']`, `metadata.annotations['<KEY>']`, spec.nodeName, spec.serviceAccountName, status.hostIP, status.podIP, status.podIPs.

Type
`object`

Required
- `fieldPath`

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | Version of the schema the FieldPath is written in terms of, defaults to "v1". |
| `fieldPath` | `string` | Path of the field to select in the specified API version. |

## .spec.install.spec.deployments\[\].spec.template.spec.containers\[\].env\[\].valueFrom.resourceFieldRef

Description
Selects a resource of the container: only resources limits and requests (limits.cpu, limits.memory, limits.ephemeral-storage, requests.cpu, requests.memory and requests.ephemeral-storage) are currently supported.

Type
`object`

Required
- `resource`

| Property | Type | Description |
|----|----|----|
| `containerName` | `string` | Container name: required for volumes, optional for env vars |
| `divisor` | `integer-or-string` | Specifies the output format of the exposed resources, defaults to "1" |
| `resource` | `string` | Required: resource to select |

## .spec.install.spec.deployments\[\].spec.template.spec.containers\[\].env\[\].valueFrom.secretKeyRef

Description
Selects a key of a secret in the pod’s namespace

Type
`object`

Required
- `key`

| Property | Type | Description |
|----|----|----|
| `key` | `string` | The key of the secret to select from. Must be a valid secret key. |
| `name` | `string` | Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names> |
| `optional` | `boolean` | Specify whether the Secret or its key must be defined |

## .spec.install.spec.deployments\[\].spec.template.spec.containers\[\].envFrom

Description
List of sources to populate environment variables in the container. The keys defined within a source must be a C_IDENTIFIER. All invalid keys will be reported as an event when the container is starting. When a key exists in multiple sources, the value associated with the last source will take precedence. Values defined by an Env with a duplicate key will take precedence. Cannot be updated.

Type
`array`

## .spec.install.spec.deployments\[\].spec.template.spec.containers\[\].envFrom\[\]

Description
EnvFromSource represents the source of a set of ConfigMaps or Secrets

Type
`object`

| Property | Type | Description |
|----|----|----|
| `configMapRef` | `object` | The ConfigMap to select from |
| `prefix` | `string` | Optional text to prepend to the name of each environment variable. Must be a C_IDENTIFIER. |
| `secretRef` | `object` | The Secret to select from |

## .spec.install.spec.deployments\[\].spec.template.spec.containers\[\].envFrom\[\].configMapRef

Description
The ConfigMap to select from

Type
`object`

| Property | Type | Description |
|----|----|----|
| `name` | `string` | Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names> |
| `optional` | `boolean` | Specify whether the ConfigMap must be defined |

## .spec.install.spec.deployments\[\].spec.template.spec.containers\[\].envFrom\[\].secretRef

Description
The Secret to select from

Type
`object`

| Property | Type | Description |
|----|----|----|
| `name` | `string` | Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names> |
| `optional` | `boolean` | Specify whether the Secret must be defined |

## .spec.install.spec.deployments\[\].spec.template.spec.containers\[\].lifecycle

Description
Actions that the management system should take in response to container lifecycle events. Cannot be updated.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `postStart` | `object` | PostStart is called immediately after a container is created. If the handler fails, the container is terminated and restarted according to its restart policy. Other management of the container blocks until the hook completes. More info: <https://kubernetes.io/docs/concepts/containers/container-lifecycle-hooks/#container-hooks> |
| `preStop` | `object` | PreStop is called immediately before a container is terminated due to an API request or management event such as liveness/startup probe failure, preemption, resource contention, etc. The handler is not called if the container crashes or exits. The Pod’s termination grace period countdown begins before the PreStop hook is executed. Regardless of the outcome of the handler, the container will eventually terminate within the Pod’s termination grace period (unless delayed by finalizers). Other management of the container blocks until the hook completes or until the termination grace period is reached. More info: <https://kubernetes.io/docs/concepts/containers/container-lifecycle-hooks/#container-hooks> |
| `stopSignal` | `string` | StopSignal defines which signal will be sent to a container when it is being stopped. If not specified, the default is defined by the container runtime in use. StopSignal can only be set for Pods with a non-empty .spec.os.name |

## .spec.install.spec.deployments\[\].spec.template.spec.containers\[\].lifecycle.postStart

Description
PostStart is called immediately after a container is created. If the handler fails, the container is terminated and restarted according to its restart policy. Other management of the container blocks until the hook completes. More info: <https://kubernetes.io/docs/concepts/containers/container-lifecycle-hooks/#container-hooks>

Type
`object`

| Property | Type | Description |
|----|----|----|
| `exec` | `object` | Exec specifies a command to execute in the container. |
| `httpGet` | `object` | HTTPGet specifies an HTTP GET request to perform. |
| `sleep` | `object` | Sleep represents a duration that the container should sleep. |
| `tcpSocket` | `object` | Deprecated. TCPSocket is NOT supported as a LifecycleHandler and kept for backward compatibility. There is no validation of this field and lifecycle hooks will fail at runtime when it is specified. |

## .spec.install.spec.deployments\[\].spec.template.spec.containers\[\].lifecycle.postStart.exec

Description
Exec specifies a command to execute in the container.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `command` | `array (string)` | Command is the command line to execute inside the container, the working directory for the command is root ('/') in the container’s filesystem. The command is simply exec’d, it is not run inside a shell, so traditional shell instructions ('\|', etc) won’t work. To use a shell, you need to explicitly call out to that shell. Exit status of 0 is treated as live/healthy and non-zero is unhealthy. |

## .spec.install.spec.deployments\[\].spec.template.spec.containers\[\].lifecycle.postStart.httpGet

Description
HTTPGet specifies an HTTP GET request to perform.

Type
`object`

Required
- `port`

| Property | Type | Description |
|----|----|----|
| `host` | `string` | Host name to connect to, defaults to the pod IP. You probably want to set "Host" in httpHeaders instead. |
| `httpHeaders` | `array` | Custom headers to set in the request. HTTP allows repeated headers. |
| `httpHeaders[]` | `object` | HTTPHeader describes a custom header to be used in HTTP probes |
| `path` | `string` | Path to access on the HTTP server. |
| `port` | `integer-or-string` | Name or number of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME. |
| `scheme` | `string` | Scheme to use for connecting to the host. Defaults to HTTP. |

## .spec.install.spec.deployments\[\].spec.template.spec.containers\[\].lifecycle.postStart.httpGet.httpHeaders

Description
Custom headers to set in the request. HTTP allows repeated headers.

Type
`array`

## .spec.install.spec.deployments\[\].spec.template.spec.containers\[\].lifecycle.postStart.httpGet.httpHeaders\[\]

Description
HTTPHeader describes a custom header to be used in HTTP probes

Type
`object`

Required
- `name`

- `value`

| Property | Type | Description |
|----|----|----|
| `name` | `string` | The header field name. This will be canonicalized upon output, so case-variant names will be understood as the same header. |
| `value` | `string` | The header field value |

## .spec.install.spec.deployments\[\].spec.template.spec.containers\[\].lifecycle.postStart.sleep

Description
Sleep represents a duration that the container should sleep.

Type
`object`

Required
- `seconds`

| Property  | Type      | Description                                |
|-----------|-----------|--------------------------------------------|
| `seconds` | `integer` | Seconds is the number of seconds to sleep. |

## .spec.install.spec.deployments\[\].spec.template.spec.containers\[\].lifecycle.postStart.tcpSocket

Description
Deprecated. TCPSocket is NOT supported as a LifecycleHandler and kept for backward compatibility. There is no validation of this field and lifecycle hooks will fail at runtime when it is specified.

Type
`object`

Required
- `port`

| Property | Type | Description |
|----|----|----|
| `host` | `string` | Optional: Host name to connect to, defaults to the pod IP. |
| `port` | `integer-or-string` | Number or name of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME. |

## .spec.install.spec.deployments\[\].spec.template.spec.containers\[\].lifecycle.preStop

Description
PreStop is called immediately before a container is terminated due to an API request or management event such as liveness/startup probe failure, preemption, resource contention, etc. The handler is not called if the container crashes or exits. The Pod’s termination grace period countdown begins before the PreStop hook is executed. Regardless of the outcome of the handler, the container will eventually terminate within the Pod’s termination grace period (unless delayed by finalizers). Other management of the container blocks until the hook completes or until the termination grace period is reached. More info: <https://kubernetes.io/docs/concepts/containers/container-lifecycle-hooks/#container-hooks>

Type
`object`

| Property | Type | Description |
|----|----|----|
| `exec` | `object` | Exec specifies a command to execute in the container. |
| `httpGet` | `object` | HTTPGet specifies an HTTP GET request to perform. |
| `sleep` | `object` | Sleep represents a duration that the container should sleep. |
| `tcpSocket` | `object` | Deprecated. TCPSocket is NOT supported as a LifecycleHandler and kept for backward compatibility. There is no validation of this field and lifecycle hooks will fail at runtime when it is specified. |

## .spec.install.spec.deployments\[\].spec.template.spec.containers\[\].lifecycle.preStop.exec

Description
Exec specifies a command to execute in the container.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `command` | `array (string)` | Command is the command line to execute inside the container, the working directory for the command is root ('/') in the container’s filesystem. The command is simply exec’d, it is not run inside a shell, so traditional shell instructions ('\|', etc) won’t work. To use a shell, you need to explicitly call out to that shell. Exit status of 0 is treated as live/healthy and non-zero is unhealthy. |

## .spec.install.spec.deployments\[\].spec.template.spec.containers\[\].lifecycle.preStop.httpGet

Description
HTTPGet specifies an HTTP GET request to perform.

Type
`object`

Required
- `port`

| Property | Type | Description |
|----|----|----|
| `host` | `string` | Host name to connect to, defaults to the pod IP. You probably want to set "Host" in httpHeaders instead. |
| `httpHeaders` | `array` | Custom headers to set in the request. HTTP allows repeated headers. |
| `httpHeaders[]` | `object` | HTTPHeader describes a custom header to be used in HTTP probes |
| `path` | `string` | Path to access on the HTTP server. |
| `port` | `integer-or-string` | Name or number of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME. |
| `scheme` | `string` | Scheme to use for connecting to the host. Defaults to HTTP. |

## .spec.install.spec.deployments\[\].spec.template.spec.containers\[\].lifecycle.preStop.httpGet.httpHeaders

Description
Custom headers to set in the request. HTTP allows repeated headers.

Type
`array`

## .spec.install.spec.deployments\[\].spec.template.spec.containers\[\].lifecycle.preStop.httpGet.httpHeaders\[\]

Description
HTTPHeader describes a custom header to be used in HTTP probes

Type
`object`

Required
- `name`

- `value`

| Property | Type | Description |
|----|----|----|
| `name` | `string` | The header field name. This will be canonicalized upon output, so case-variant names will be understood as the same header. |
| `value` | `string` | The header field value |

## .spec.install.spec.deployments\[\].spec.template.spec.containers\[\].lifecycle.preStop.sleep

Description
Sleep represents a duration that the container should sleep.

Type
`object`

Required
- `seconds`

| Property  | Type      | Description                                |
|-----------|-----------|--------------------------------------------|
| `seconds` | `integer` | Seconds is the number of seconds to sleep. |

## .spec.install.spec.deployments\[\].spec.template.spec.containers\[\].lifecycle.preStop.tcpSocket

Description
Deprecated. TCPSocket is NOT supported as a LifecycleHandler and kept for backward compatibility. There is no validation of this field and lifecycle hooks will fail at runtime when it is specified.

Type
`object`

Required
- `port`

| Property | Type | Description |
|----|----|----|
| `host` | `string` | Optional: Host name to connect to, defaults to the pod IP. |
| `port` | `integer-or-string` | Number or name of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME. |

## .spec.install.spec.deployments\[\].spec.template.spec.containers\[\].livenessProbe

Description
Periodic probe of container liveness. Container will be restarted if the probe fails. Cannot be updated. More info: <https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes>

Type
`object`

| Property | Type | Description |
|----|----|----|
| `exec` | `object` | Exec specifies a command to execute in the container. |
| `failureThreshold` | `integer` | Minimum consecutive failures for the probe to be considered failed after having succeeded. Defaults to 3. Minimum value is 1. |
| `grpc` | `object` | GRPC specifies a GRPC HealthCheckRequest. |
| `httpGet` | `object` | HTTPGet specifies an HTTP GET request to perform. |
| `initialDelaySeconds` | `integer` | Number of seconds after the container has started before liveness probes are initiated. More info: <https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes> |
| `periodSeconds` | `integer` | How often (in seconds) to perform the probe. Default to 10 seconds. Minimum value is 1. |
| `successThreshold` | `integer` | Minimum consecutive successes for the probe to be considered successful after having failed. Defaults to 1. Must be 1 for liveness and startup. Minimum value is 1. |
| `tcpSocket` | `object` | TCPSocket specifies a connection to a TCP port. |
| `terminationGracePeriodSeconds` | `integer` | Optional duration in seconds the pod needs to terminate gracefully upon probe failure. The grace period is the duration in seconds after the processes running in the pod are sent a termination signal and the time when the processes are forcibly halted with a kill signal. Set this value longer than the expected cleanup time for your process. If this value is nil, the pod’s terminationGracePeriodSeconds will be used. Otherwise, this value overrides the value provided by the pod spec. Value must be non-negative integer. The value zero indicates stop immediately via the kill signal (no opportunity to shut down). This is a beta field and requires enabling ProbeTerminationGracePeriod feature gate. Minimum value is 1. spec.terminationGracePeriodSeconds is used if unset. |
| `timeoutSeconds` | `integer` | Number of seconds after which the probe times out. Defaults to 1 second. Minimum value is 1. More info: <https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes> |

## .spec.install.spec.deployments\[\].spec.template.spec.containers\[\].livenessProbe.exec

Description
Exec specifies a command to execute in the container.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `command` | `array (string)` | Command is the command line to execute inside the container, the working directory for the command is root ('/') in the container’s filesystem. The command is simply exec’d, it is not run inside a shell, so traditional shell instructions ('\|', etc) won’t work. To use a shell, you need to explicitly call out to that shell. Exit status of 0 is treated as live/healthy and non-zero is unhealthy. |

## .spec.install.spec.deployments\[\].spec.template.spec.containers\[\].livenessProbe.grpc

Description
GRPC specifies a GRPC HealthCheckRequest.

Type
`object`

Required
- `port`

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
<td style="text-align: left;"><p><code>port</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p>Port number of the gRPC service. Number must be in the range 1 to 65535.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>service</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Service is the name of the service to place in the gRPC HealthCheckRequest (see <a href="https://github.com/grpc/grpc/blob/master/doc/health-checking.md">https://github.com/grpc/grpc/blob/master/doc/health-checking.md</a>).</p>
<p>If this is not specified, the default behavior is defined by gRPC.</p></td>
</tr>
</tbody>
</table>

## .spec.install.spec.deployments\[\].spec.template.spec.containers\[\].livenessProbe.httpGet

Description
HTTPGet specifies an HTTP GET request to perform.

Type
`object`

Required
- `port`

| Property | Type | Description |
|----|----|----|
| `host` | `string` | Host name to connect to, defaults to the pod IP. You probably want to set "Host" in httpHeaders instead. |
| `httpHeaders` | `array` | Custom headers to set in the request. HTTP allows repeated headers. |
| `httpHeaders[]` | `object` | HTTPHeader describes a custom header to be used in HTTP probes |
| `path` | `string` | Path to access on the HTTP server. |
| `port` | `integer-or-string` | Name or number of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME. |
| `scheme` | `string` | Scheme to use for connecting to the host. Defaults to HTTP. |

## .spec.install.spec.deployments\[\].spec.template.spec.containers\[\].livenessProbe.httpGet.httpHeaders

Description
Custom headers to set in the request. HTTP allows repeated headers.

Type
`array`

## .spec.install.spec.deployments\[\].spec.template.spec.containers\[\].livenessProbe.httpGet.httpHeaders\[\]

Description
HTTPHeader describes a custom header to be used in HTTP probes

Type
`object`

Required
- `name`

- `value`

| Property | Type | Description |
|----|----|----|
| `name` | `string` | The header field name. This will be canonicalized upon output, so case-variant names will be understood as the same header. |
| `value` | `string` | The header field value |

## .spec.install.spec.deployments\[\].spec.template.spec.containers\[\].livenessProbe.tcpSocket

Description
TCPSocket specifies a connection to a TCP port.

Type
`object`

Required
- `port`

| Property | Type | Description |
|----|----|----|
| `host` | `string` | Optional: Host name to connect to, defaults to the pod IP. |
| `port` | `integer-or-string` | Number or name of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME. |

## .spec.install.spec.deployments\[\].spec.template.spec.containers\[\].ports

Description
List of ports to expose from the container. Not specifying a port here DOES NOT prevent that port from being exposed. Any port which is listening on the default "0.0.0.0" address inside a container will be accessible from the network. Modifying this array with strategic merge patch may corrupt the data. For more information See <https://github.com/kubernetes/kubernetes/issues/108255>. Cannot be updated.

Type
`array`

## .spec.install.spec.deployments\[\].spec.template.spec.containers\[\].ports\[\]

Description
ContainerPort represents a network port in a single container.

Type
`object`

Required
- `containerPort`

| Property | Type | Description |
|----|----|----|
| `containerPort` | `integer` | Number of port to expose on the pod’s IP address. This must be a valid port number, 0 \< x \< 65536. |
| `hostIP` | `string` | What host IP to bind the external port to. |
| `hostPort` | `integer` | Number of port to expose on the host. If specified, this must be a valid port number, 0 \< x \< 65536. If HostNetwork is specified, this must match ContainerPort. Most containers do not need this. |
| `name` | `string` | If specified, this must be an IANA_SVC_NAME and unique within the pod. Each named port in a pod must have a unique name. Name for the port that can be referred to by services. |
| `protocol` | `string` | Protocol for port. Must be UDP, TCP, or SCTP. Defaults to "TCP". |

## .spec.install.spec.deployments\[\].spec.template.spec.containers\[\].readinessProbe

Description
Periodic probe of container service readiness. Container will be removed from service endpoints if the probe fails. Cannot be updated. More info: <https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes>

Type
`object`

| Property | Type | Description |
|----|----|----|
| `exec` | `object` | Exec specifies a command to execute in the container. |
| `failureThreshold` | `integer` | Minimum consecutive failures for the probe to be considered failed after having succeeded. Defaults to 3. Minimum value is 1. |
| `grpc` | `object` | GRPC specifies a GRPC HealthCheckRequest. |
| `httpGet` | `object` | HTTPGet specifies an HTTP GET request to perform. |
| `initialDelaySeconds` | `integer` | Number of seconds after the container has started before liveness probes are initiated. More info: <https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes> |
| `periodSeconds` | `integer` | How often (in seconds) to perform the probe. Default to 10 seconds. Minimum value is 1. |
| `successThreshold` | `integer` | Minimum consecutive successes for the probe to be considered successful after having failed. Defaults to 1. Must be 1 for liveness and startup. Minimum value is 1. |
| `tcpSocket` | `object` | TCPSocket specifies a connection to a TCP port. |
| `terminationGracePeriodSeconds` | `integer` | Optional duration in seconds the pod needs to terminate gracefully upon probe failure. The grace period is the duration in seconds after the processes running in the pod are sent a termination signal and the time when the processes are forcibly halted with a kill signal. Set this value longer than the expected cleanup time for your process. If this value is nil, the pod’s terminationGracePeriodSeconds will be used. Otherwise, this value overrides the value provided by the pod spec. Value must be non-negative integer. The value zero indicates stop immediately via the kill signal (no opportunity to shut down). This is a beta field and requires enabling ProbeTerminationGracePeriod feature gate. Minimum value is 1. spec.terminationGracePeriodSeconds is used if unset. |
| `timeoutSeconds` | `integer` | Number of seconds after which the probe times out. Defaults to 1 second. Minimum value is 1. More info: <https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes> |

## .spec.install.spec.deployments\[\].spec.template.spec.containers\[\].readinessProbe.exec

Description
Exec specifies a command to execute in the container.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `command` | `array (string)` | Command is the command line to execute inside the container, the working directory for the command is root ('/') in the container’s filesystem. The command is simply exec’d, it is not run inside a shell, so traditional shell instructions ('\|', etc) won’t work. To use a shell, you need to explicitly call out to that shell. Exit status of 0 is treated as live/healthy and non-zero is unhealthy. |

## .spec.install.spec.deployments\[\].spec.template.spec.containers\[\].readinessProbe.grpc

Description
GRPC specifies a GRPC HealthCheckRequest.

Type
`object`

Required
- `port`

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
<td style="text-align: left;"><p><code>port</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p>Port number of the gRPC service. Number must be in the range 1 to 65535.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>service</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Service is the name of the service to place in the gRPC HealthCheckRequest (see <a href="https://github.com/grpc/grpc/blob/master/doc/health-checking.md">https://github.com/grpc/grpc/blob/master/doc/health-checking.md</a>).</p>
<p>If this is not specified, the default behavior is defined by gRPC.</p></td>
</tr>
</tbody>
</table>

## .spec.install.spec.deployments\[\].spec.template.spec.containers\[\].readinessProbe.httpGet

Description
HTTPGet specifies an HTTP GET request to perform.

Type
`object`

Required
- `port`

| Property | Type | Description |
|----|----|----|
| `host` | `string` | Host name to connect to, defaults to the pod IP. You probably want to set "Host" in httpHeaders instead. |
| `httpHeaders` | `array` | Custom headers to set in the request. HTTP allows repeated headers. |
| `httpHeaders[]` | `object` | HTTPHeader describes a custom header to be used in HTTP probes |
| `path` | `string` | Path to access on the HTTP server. |
| `port` | `integer-or-string` | Name or number of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME. |
| `scheme` | `string` | Scheme to use for connecting to the host. Defaults to HTTP. |

## .spec.install.spec.deployments\[\].spec.template.spec.containers\[\].readinessProbe.httpGet.httpHeaders

Description
Custom headers to set in the request. HTTP allows repeated headers.

Type
`array`

## .spec.install.spec.deployments\[\].spec.template.spec.containers\[\].readinessProbe.httpGet.httpHeaders\[\]

Description
HTTPHeader describes a custom header to be used in HTTP probes

Type
`object`

Required
- `name`

- `value`

| Property | Type | Description |
|----|----|----|
| `name` | `string` | The header field name. This will be canonicalized upon output, so case-variant names will be understood as the same header. |
| `value` | `string` | The header field value |

## .spec.install.spec.deployments\[\].spec.template.spec.containers\[\].readinessProbe.tcpSocket

Description
TCPSocket specifies a connection to a TCP port.

Type
`object`

Required
- `port`

| Property | Type | Description |
|----|----|----|
| `host` | `string` | Optional: Host name to connect to, defaults to the pod IP. |
| `port` | `integer-or-string` | Number or name of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME. |

## .spec.install.spec.deployments\[\].spec.template.spec.containers\[\].resizePolicy

Description
Resources resize policy for the container.

Type
`array`

## .spec.install.spec.deployments\[\].spec.template.spec.containers\[\].resizePolicy\[\]

Description
ContainerResizePolicy represents resource resize policy for the container.

Type
`object`

Required
- `resourceName`

- `restartPolicy`

| Property | Type | Description |
|----|----|----|
| `resourceName` | `string` | Name of the resource to which this resource resize policy applies. Supported values: cpu, memory. |
| `restartPolicy` | `string` | Restart policy to apply when specified resource is resized. If not specified, it defaults to NotRequired. |

## .spec.install.spec.deployments\[\].spec.template.spec.containers\[\].resources

Description
Compute Resources required by this container. Cannot be updated. More info: <https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/>

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
<td style="text-align: left;"><p><code>claims</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>Claims lists the names of resources, defined in spec.resourceClaims, that are used by this container.</p>
<p>This is an alpha field and requires enabling the DynamicResourceAllocation feature gate.</p>
<p>This field is immutable. It can only be set for containers.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>claims[]</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>ResourceClaim references one entry in PodSpec.ResourceClaims.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>limits</code></p></td>
<td style="text-align: left;"><p><code>integer-or-string</code></p></td>
<td style="text-align: left;"><p>Limits describes the maximum amount of compute resources allowed. More info: <a href="https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/">https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>requests</code></p></td>
<td style="text-align: left;"><p><code>integer-or-string</code></p></td>
<td style="text-align: left;"><p>Requests describes the minimum amount of compute resources required. If Requests is omitted for a container, it defaults to Limits if that is explicitly specified, otherwise to an implementation-defined value. Requests cannot exceed Limits. More info: <a href="https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/">https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/</a></p></td>
</tr>
</tbody>
</table>

## .spec.install.spec.deployments\[\].spec.template.spec.containers\[\].resources.claims

Description
Claims lists the names of resources, defined in spec.resourceClaims, that are used by this container.

This is an alpha field and requires enabling the DynamicResourceAllocation feature gate.

This field is immutable. It can only be set for containers.

Type
`array`

## .spec.install.spec.deployments\[\].spec.template.spec.containers\[\].resources.claims\[\]

Description
ResourceClaim references one entry in PodSpec.ResourceClaims.

Type
`object`

Required
- `name`

| Property | Type | Description |
|----|----|----|
| `name` | `string` | Name must match the name of one entry in pod.spec.resourceClaims of the Pod where this field is used. It makes that resource available inside a container. |
| `request` | `string` | Request is the name chosen for a request in the referenced claim. If empty, everything from the claim is made available, otherwise only the result of this request. |

## .spec.install.spec.deployments\[\].spec.template.spec.containers\[\].securityContext

Description
SecurityContext defines the security options the container should be run with. If set, the fields of SecurityContext override the equivalent fields of PodSecurityContext. More info: <https://kubernetes.io/docs/tasks/configure-pod-container/security-context/>

Type
`object`

| Property | Type | Description |
|----|----|----|
| `allowPrivilegeEscalation` | `boolean` | AllowPrivilegeEscalation controls whether a process can gain more privileges than its parent process. This bool directly controls if the no_new_privs flag will be set on the container process. AllowPrivilegeEscalation is true always when the container is: 1) run as Privileged 2) has CAP_SYS_ADMIN Note that this field cannot be set when spec.os.name is windows. |
| `appArmorProfile` | `object` | appArmorProfile is the AppArmor options to use by this container. If set, this profile overrides the pod’s appArmorProfile. Note that this field cannot be set when spec.os.name is windows. |
| `capabilities` | `object` | The capabilities to add/drop when running containers. Defaults to the default set of capabilities granted by the container runtime. Note that this field cannot be set when spec.os.name is windows. |
| `privileged` | `boolean` | Run container in privileged mode. Processes in privileged containers are essentially equivalent to root on the host. Defaults to false. Note that this field cannot be set when spec.os.name is windows. |
| `procMount` | `string` | procMount denotes the type of proc mount to use for the containers. The default value is Default which uses the container runtime defaults for readonly paths and masked paths. This requires the ProcMountType feature flag to be enabled. Note that this field cannot be set when spec.os.name is windows. |
| `readOnlyRootFilesystem` | `boolean` | Whether this container has a read-only root filesystem. Default is false. Note that this field cannot be set when spec.os.name is windows. |
| `runAsGroup` | `integer` | The GID to run the entrypoint of the container process. Uses runtime default if unset. May also be set in PodSecurityContext. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence. Note that this field cannot be set when spec.os.name is windows. |
| `runAsNonRoot` | `boolean` | Indicates that the container must run as a non-root user. If true, the Kubelet will validate the image at runtime to ensure that it does not run as UID 0 (root) and fail to start the container if it does. If unset or false, no such validation will be performed. May also be set in PodSecurityContext. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence. |
| `runAsUser` | `integer` | The UID to run the entrypoint of the container process. Defaults to user specified in image metadata if unspecified. May also be set in PodSecurityContext. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence. Note that this field cannot be set when spec.os.name is windows. |
| `seLinuxOptions` | `object` | The SELinux context to be applied to the container. If unspecified, the container runtime will allocate a random SELinux context for each container. May also be set in PodSecurityContext. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence. Note that this field cannot be set when spec.os.name is windows. |
| `seccompProfile` | `object` | The seccomp options to use by this container. If seccomp options are provided at both the pod & container level, the container options override the pod options. Note that this field cannot be set when spec.os.name is windows. |
| `windowsOptions` | `object` | The Windows specific settings applied to all containers. If unspecified, the options from the PodSecurityContext will be used. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence. Note that this field cannot be set when spec.os.name is linux. |

## .spec.install.spec.deployments\[\].spec.template.spec.containers\[\].securityContext.appArmorProfile

Description
appArmorProfile is the AppArmor options to use by this container. If set, this profile overrides the pod’s appArmorProfile. Note that this field cannot be set when spec.os.name is windows.

Type
`object`

Required
- `type`

| Property | Type | Description |
|----|----|----|
| `localhostProfile` | `string` | localhostProfile indicates a profile loaded on the node that should be used. The profile must be preconfigured on the node to work. Must match the loaded name of the profile. Must be set if and only if type is "Localhost". |
| `type` | `string` | type indicates which kind of AppArmor profile will be applied. Valid options are: Localhost - a profile pre-loaded on the node. RuntimeDefault - the container runtime’s default profile. Unconfined - no AppArmor enforcement. |

## .spec.install.spec.deployments\[\].spec.template.spec.containers\[\].securityContext.capabilities

Description
The capabilities to add/drop when running containers. Defaults to the default set of capabilities granted by the container runtime. Note that this field cannot be set when spec.os.name is windows.

Type
`object`

| Property | Type             | Description          |
|----------|------------------|----------------------|
| `add`    | `array (string)` | Added capabilities   |
| `drop`   | `array (string)` | Removed capabilities |

## .spec.install.spec.deployments\[\].spec.template.spec.containers\[\].securityContext.seLinuxOptions

Description
The SELinux context to be applied to the container. If unspecified, the container runtime will allocate a random SELinux context for each container. May also be set in PodSecurityContext. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence. Note that this field cannot be set when spec.os.name is windows.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `level` | `string` | Level is SELinux level label that applies to the container. |
| `role` | `string` | Role is a SELinux role label that applies to the container. |
| `type` | `string` | Type is a SELinux type label that applies to the container. |
| `user` | `string` | User is a SELinux user label that applies to the container. |

## .spec.install.spec.deployments\[\].spec.template.spec.containers\[\].securityContext.seccompProfile

Description
The seccomp options to use by this container. If seccomp options are provided at both the pod & container level, the container options override the pod options. Note that this field cannot be set when spec.os.name is windows.

Type
`object`

Required
- `type`

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
<td style="text-align: left;"><p><code>localhostProfile</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>localhostProfile indicates a profile defined in a file on the node should be used. The profile must be preconfigured on the node to work. Must be a descending path, relative to the kubelet’s configured seccomp profile location. Must be set if type is "Localhost". Must NOT be set for any other type.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>type</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>type indicates which kind of seccomp profile will be applied. Valid options are:</p>
<p>Localhost - a profile defined in a file on the node should be used. RuntimeDefault - the container runtime default profile should be used. Unconfined - no profile should be applied.</p></td>
</tr>
</tbody>
</table>

## .spec.install.spec.deployments\[\].spec.template.spec.containers\[\].securityContext.windowsOptions

Description
The Windows specific settings applied to all containers. If unspecified, the options from the PodSecurityContext will be used. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence. Note that this field cannot be set when spec.os.name is linux.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `gmsaCredentialSpec` | `string` | GMSACredentialSpec is where the GMSA admission webhook (<https://github.com/kubernetes-sigs/windows-gmsa>) inlines the contents of the GMSA credential spec named by the GMSACredentialSpecName field. |
| `gmsaCredentialSpecName` | `string` | GMSACredentialSpecName is the name of the GMSA credential spec to use. |
| `hostProcess` | `boolean` | HostProcess determines if a container should be run as a 'Host Process' container. All of a Pod’s containers must have the same effective HostProcess value (it is not allowed to have a mix of HostProcess containers and non-HostProcess containers). In addition, if HostProcess is true then HostNetwork must also be set to true. |
| `runAsUserName` | `string` | The UserName in Windows to run the entrypoint of the container process. Defaults to the user specified in image metadata if unspecified. May also be set in PodSecurityContext. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence. |

## .spec.install.spec.deployments\[\].spec.template.spec.containers\[\].startupProbe

Description
StartupProbe indicates that the Pod has successfully initialized. If specified, no other probes are executed until this completes successfully. If this probe fails, the Pod will be restarted, just as if the livenessProbe failed. This can be used to provide different probe parameters at the beginning of a Pod’s lifecycle, when it might take a long time to load data or warm a cache, than during steady-state operation. This cannot be updated. More info: <https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes>

Type
`object`

| Property | Type | Description |
|----|----|----|
| `exec` | `object` | Exec specifies a command to execute in the container. |
| `failureThreshold` | `integer` | Minimum consecutive failures for the probe to be considered failed after having succeeded. Defaults to 3. Minimum value is 1. |
| `grpc` | `object` | GRPC specifies a GRPC HealthCheckRequest. |
| `httpGet` | `object` | HTTPGet specifies an HTTP GET request to perform. |
| `initialDelaySeconds` | `integer` | Number of seconds after the container has started before liveness probes are initiated. More info: <https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes> |
| `periodSeconds` | `integer` | How often (in seconds) to perform the probe. Default to 10 seconds. Minimum value is 1. |
| `successThreshold` | `integer` | Minimum consecutive successes for the probe to be considered successful after having failed. Defaults to 1. Must be 1 for liveness and startup. Minimum value is 1. |
| `tcpSocket` | `object` | TCPSocket specifies a connection to a TCP port. |
| `terminationGracePeriodSeconds` | `integer` | Optional duration in seconds the pod needs to terminate gracefully upon probe failure. The grace period is the duration in seconds after the processes running in the pod are sent a termination signal and the time when the processes are forcibly halted with a kill signal. Set this value longer than the expected cleanup time for your process. If this value is nil, the pod’s terminationGracePeriodSeconds will be used. Otherwise, this value overrides the value provided by the pod spec. Value must be non-negative integer. The value zero indicates stop immediately via the kill signal (no opportunity to shut down). This is a beta field and requires enabling ProbeTerminationGracePeriod feature gate. Minimum value is 1. spec.terminationGracePeriodSeconds is used if unset. |
| `timeoutSeconds` | `integer` | Number of seconds after which the probe times out. Defaults to 1 second. Minimum value is 1. More info: <https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes> |

## .spec.install.spec.deployments\[\].spec.template.spec.containers\[\].startupProbe.exec

Description
Exec specifies a command to execute in the container.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `command` | `array (string)` | Command is the command line to execute inside the container, the working directory for the command is root ('/') in the container’s filesystem. The command is simply exec’d, it is not run inside a shell, so traditional shell instructions ('\|', etc) won’t work. To use a shell, you need to explicitly call out to that shell. Exit status of 0 is treated as live/healthy and non-zero is unhealthy. |

## .spec.install.spec.deployments\[\].spec.template.spec.containers\[\].startupProbe.grpc

Description
GRPC specifies a GRPC HealthCheckRequest.

Type
`object`

Required
- `port`

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
<td style="text-align: left;"><p><code>port</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p>Port number of the gRPC service. Number must be in the range 1 to 65535.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>service</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Service is the name of the service to place in the gRPC HealthCheckRequest (see <a href="https://github.com/grpc/grpc/blob/master/doc/health-checking.md">https://github.com/grpc/grpc/blob/master/doc/health-checking.md</a>).</p>
<p>If this is not specified, the default behavior is defined by gRPC.</p></td>
</tr>
</tbody>
</table>

## .spec.install.spec.deployments\[\].spec.template.spec.containers\[\].startupProbe.httpGet

Description
HTTPGet specifies an HTTP GET request to perform.

Type
`object`

Required
- `port`

| Property | Type | Description |
|----|----|----|
| `host` | `string` | Host name to connect to, defaults to the pod IP. You probably want to set "Host" in httpHeaders instead. |
| `httpHeaders` | `array` | Custom headers to set in the request. HTTP allows repeated headers. |
| `httpHeaders[]` | `object` | HTTPHeader describes a custom header to be used in HTTP probes |
| `path` | `string` | Path to access on the HTTP server. |
| `port` | `integer-or-string` | Name or number of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME. |
| `scheme` | `string` | Scheme to use for connecting to the host. Defaults to HTTP. |

## .spec.install.spec.deployments\[\].spec.template.spec.containers\[\].startupProbe.httpGet.httpHeaders

Description
Custom headers to set in the request. HTTP allows repeated headers.

Type
`array`

## .spec.install.spec.deployments\[\].spec.template.spec.containers\[\].startupProbe.httpGet.httpHeaders\[\]

Description
HTTPHeader describes a custom header to be used in HTTP probes

Type
`object`

Required
- `name`

- `value`

| Property | Type | Description |
|----|----|----|
| `name` | `string` | The header field name. This will be canonicalized upon output, so case-variant names will be understood as the same header. |
| `value` | `string` | The header field value |

## .spec.install.spec.deployments\[\].spec.template.spec.containers\[\].startupProbe.tcpSocket

Description
TCPSocket specifies a connection to a TCP port.

Type
`object`

Required
- `port`

| Property | Type | Description |
|----|----|----|
| `host` | `string` | Optional: Host name to connect to, defaults to the pod IP. |
| `port` | `integer-or-string` | Number or name of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME. |

## .spec.install.spec.deployments\[\].spec.template.spec.containers\[\].volumeDevices

Description
volumeDevices is the list of block devices to be used by the container.

Type
`array`

## .spec.install.spec.deployments\[\].spec.template.spec.containers\[\].volumeDevices\[\]

Description
volumeDevice describes a mapping of a raw block device within a container.

Type
`object`

Required
- `devicePath`

- `name`

| Property | Type | Description |
|----|----|----|
| `devicePath` | `string` | devicePath is the path inside of the container that the device will be mapped to. |
| `name` | `string` | name must match the name of a persistentVolumeClaim in the pod |

## .spec.install.spec.deployments\[\].spec.template.spec.containers\[\].volumeMounts

Description
Pod volumes to mount into the container’s filesystem. Cannot be updated.

Type
`array`

## .spec.install.spec.deployments\[\].spec.template.spec.containers\[\].volumeMounts\[\]

Description
VolumeMount describes a mounting of a Volume within a container.

Type
`object`

Required
- `mountPath`

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
<td style="text-align: left;"><p><code>mountPath</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Path within the container at which the volume should be mounted. Must not contain ':'.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>mountPropagation</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>mountPropagation determines how mounts are propagated from the host to container and the other way around. When not set, MountPropagationNone is used. This field is beta in 1.10. When RecursiveReadOnly is set to IfPossible or to Enabled, MountPropagation must be None or unspecified (which defaults to None).</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>name</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>This must match the Name of a Volume.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>readOnly</code></p></td>
<td style="text-align: left;"><p><code>boolean</code></p></td>
<td style="text-align: left;"><p>Mounted read-only if true, read-write otherwise (false or unspecified). Defaults to false.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>recursiveReadOnly</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>RecursiveReadOnly specifies whether read-only mounts should be handled recursively.</p>
<p>If ReadOnly is false, this field has no meaning and must be unspecified.</p>
<p>If ReadOnly is true, and this field is set to Disabled, the mount is not made recursively read-only. If this field is set to IfPossible, the mount is made recursively read-only, if it is supported by the container runtime. If this field is set to Enabled, the mount is made recursively read-only if it is supported by the container runtime, otherwise the pod will not be started and an error will be generated to indicate the reason.</p>
<p>If this field is set to IfPossible or Enabled, MountPropagation must be set to None (or be unspecified, which defaults to None).</p>
<p>If this field is not specified, it is treated as an equivalent of Disabled.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>subPath</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Path within the volume from which the container’s volume should be mounted. Defaults to "" (volume’s root).</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>subPathExpr</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Expanded path within the volume from which the container’s volume should be mounted. Behaves similarly to SubPath but environment variable references $(VAR_NAME) are expanded using the container’s environment. Defaults to "" (volume’s root). SubPathExpr and SubPath are mutually exclusive.</p></td>
</tr>
</tbody>
</table>

## .spec.install.spec.deployments\[\].spec.template.spec.dnsConfig

Description
Specifies the DNS parameters of a pod. Parameters specified here will be merged to the generated DNS configuration based on DNSPolicy.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `nameservers` | `array (string)` | A list of DNS name server IP addresses. This will be appended to the base nameservers generated from DNSPolicy. Duplicated nameservers will be removed. |
| `options` | `array` | A list of DNS resolver options. This will be merged with the base options generated from DNSPolicy. Duplicated entries will be removed. Resolution options given in Options will override those that appear in the base DNSPolicy. |
| `options[]` | `object` | PodDNSConfigOption defines DNS resolver options of a pod. |
| `searches` | `array (string)` | A list of DNS search domains for host-name lookup. This will be appended to the base search paths generated from DNSPolicy. Duplicated search paths will be removed. |

## .spec.install.spec.deployments\[\].spec.template.spec.dnsConfig.options

Description
A list of DNS resolver options. This will be merged with the base options generated from DNSPolicy. Duplicated entries will be removed. Resolution options given in Options will override those that appear in the base DNSPolicy.

Type
`array`

## .spec.install.spec.deployments\[\].spec.template.spec.dnsConfig.options\[\]

Description
PodDNSConfigOption defines DNS resolver options of a pod.

Type
`object`

| Property | Type     | Description                                        |
|----------|----------|----------------------------------------------------|
| `name`   | `string` | Name is this DNS resolver option’s name. Required. |
| `value`  | `string` | Value is this DNS resolver option’s value.         |

## .spec.install.spec.deployments\[\].spec.template.spec.ephemeralContainers

Description
List of ephemeral containers run in this pod. Ephemeral containers may be run in an existing pod to perform user-initiated actions such as debugging. This list cannot be specified when creating a pod, and it cannot be modified by updating the pod spec. In order to add an ephemeral container to an existing pod, use the pod’s ephemeralcontainers subresource.

Type
`array`

## .spec.install.spec.deployments\[\].spec.template.spec.ephemeralContainers\[\]

Description
An EphemeralContainer is a temporary container that you may add to an existing Pod for user-initiated activities such as debugging. Ephemeral containers have no resource or scheduling guarantees, and they will not be restarted when they exit or when a Pod is removed or restarted. The kubelet may evict a Pod if an ephemeral container causes the Pod to exceed its resource allocation.

To add an ephemeral container, use the ephemeralcontainers subresource of an existing Pod. Ephemeral containers may not be removed or restarted.

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
<td style="text-align: left;"><p><code>args</code></p></td>
<td style="text-align: left;"><p><code>array (string)</code></p></td>
<td style="text-align: left;"><p>Arguments to the entrypoint. The image’s CMD is used if this is not provided. Variable references $(VAR_NAME) are expanded using the container’s environment. If a variable cannot be resolved, the reference in the input string will be unchanged. Double are reduced to a single $, which allows for escaping the $(VAR_NAME) syntax: i.e. "(VAR_NAME)" will produce the string literal "$(VAR_NAME)". Escaped references will never be expanded, regardless of whether the variable exists or not. Cannot be updated. More info: <a href="https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#running-a-command-in-a-shell">https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#running-a-command-in-a-shell</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>command</code></p></td>
<td style="text-align: left;"><p><code>array (string)</code></p></td>
<td style="text-align: left;"><p>Entrypoint array. Not executed within a shell. The image’s ENTRYPOINT is used if this is not provided. Variable references $(VAR_NAME) are expanded using the container’s environment. If a variable cannot be resolved, the reference in the input string will be unchanged. Double are reduced to a single $, which allows for escaping the $(VAR_NAME) syntax: i.e. "(VAR_NAME)" will produce the string literal "$(VAR_NAME)". Escaped references will never be expanded, regardless of whether the variable exists or not. Cannot be updated. More info: <a href="https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#running-a-command-in-a-shell">https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#running-a-command-in-a-shell</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>env</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>List of environment variables to set in the container. Cannot be updated.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>env[]</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>EnvVar represents an environment variable present in a Container.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>envFrom</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>List of sources to populate environment variables in the container. The keys defined within a source must be a C_IDENTIFIER. All invalid keys will be reported as an event when the container is starting. When a key exists in multiple sources, the value associated with the last source will take precedence. Values defined by an Env with a duplicate key will take precedence. Cannot be updated.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>envFrom[]</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>EnvFromSource represents the source of a set of ConfigMaps or Secrets</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>image</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Container image name. More info: <a href="https://kubernetes.io/docs/concepts/containers/images">https://kubernetes.io/docs/concepts/containers/images</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>imagePullPolicy</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Image pull policy. One of Always, Never, IfNotPresent. Defaults to Always if :latest tag is specified, or IfNotPresent otherwise. Cannot be updated. More info: <a href="https://kubernetes.io/docs/concepts/containers/images#updating-images">https://kubernetes.io/docs/concepts/containers/images#updating-images</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>lifecycle</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>Lifecycle is not allowed for ephemeral containers.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>livenessProbe</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>Probes are not allowed for ephemeral containers.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>name</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Name of the ephemeral container specified as a DNS_LABEL. This name must be unique among all containers, init containers and ephemeral containers.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>ports</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>Ports are not allowed for ephemeral containers.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>ports[]</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>ContainerPort represents a network port in a single container.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>readinessProbe</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>Probes are not allowed for ephemeral containers.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>resizePolicy</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>Resources resize policy for the container.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>resizePolicy[]</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>ContainerResizePolicy represents resource resize policy for the container.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>resources</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>Resources are not allowed for ephemeral containers. Ephemeral containers use spare resources already allocated to the pod.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>restartPolicy</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Restart policy for the container to manage the restart behavior of each container within a pod. This may only be set for init containers. You cannot set this field on ephemeral containers.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>securityContext</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>Optional: SecurityContext defines the security options the ephemeral container should be run with. If set, the fields of SecurityContext override the equivalent fields of PodSecurityContext.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>startupProbe</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>Probes are not allowed for ephemeral containers.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>stdin</code></p></td>
<td style="text-align: left;"><p><code>boolean</code></p></td>
<td style="text-align: left;"><p>Whether this container should allocate a buffer for stdin in the container runtime. If this is not set, reads from stdin in the container will always result in EOF. Default is false.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>stdinOnce</code></p></td>
<td style="text-align: left;"><p><code>boolean</code></p></td>
<td style="text-align: left;"><p>Whether the container runtime should close the stdin channel after it has been opened by a single attach. When stdin is true the stdin stream will remain open across multiple attach sessions. If stdinOnce is set to true, stdin is opened on container start, is empty until the first client attaches to stdin, and then remains open and accepts data until the client disconnects, at which time stdin is closed and remains closed until the container is restarted. If this flag is false, a container processes that reads from stdin will never receive an EOF. Default is false</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>targetContainerName</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>If set, the name of the container from PodSpec that this ephemeral container targets. The ephemeral container will be run in the namespaces (IPC, PID, etc) of this container. If not set then the ephemeral container uses the namespaces configured in the Pod spec.</p>
<p>The container runtime must implement support for this feature. If the runtime does not support namespace targeting then the result of setting this field is undefined.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>terminationMessagePath</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Optional: Path at which the file to which the container’s termination message will be written is mounted into the container’s filesystem. Message written is intended to be brief final status, such as an assertion failure message. Will be truncated by the node if greater than 4096 bytes. The total message length across all containers will be limited to 12kb. Defaults to /dev/termination-log. Cannot be updated.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>terminationMessagePolicy</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Indicate how the termination message should be populated. File will use the contents of terminationMessagePath to populate the container status message on both success and failure. FallbackToLogsOnError will use the last chunk of container log output if the termination message file is empty and the container exited with an error. The log output is limited to 2048 bytes or 80 lines, whichever is smaller. Defaults to File. Cannot be updated.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>tty</code></p></td>
<td style="text-align: left;"><p><code>boolean</code></p></td>
<td style="text-align: left;"><p>Whether this container should allocate a TTY for itself, also requires 'stdin' to be true. Default is false.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>volumeDevices</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>volumeDevices is the list of block devices to be used by the container.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>volumeDevices[]</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>volumeDevice describes a mapping of a raw block device within a container.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>volumeMounts</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>Pod volumes to mount into the container’s filesystem. Subpath mounts are not allowed for ephemeral containers. Cannot be updated.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>volumeMounts[]</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>VolumeMount describes a mounting of a Volume within a container.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>workingDir</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Container’s working directory. If not specified, the container runtime’s default will be used, which might be configured in the container image. Cannot be updated.</p></td>
</tr>
</tbody>
</table>

## .spec.install.spec.deployments\[\].spec.template.spec.ephemeralContainers\[\].env

Description
List of environment variables to set in the container. Cannot be updated.

Type
`array`

## .spec.install.spec.deployments\[\].spec.template.spec.ephemeralContainers\[\].env\[\]

Description
EnvVar represents an environment variable present in a Container.

Type
`object`

Required
- `name`

| Property | Type | Description |
|----|----|----|
| `name` | `string` | Name of the environment variable. Must be a C_IDENTIFIER. |
| `value` | `string` | Variable references \$(VAR_NAME) are expanded using the previously defined environment variables in the container and any service environment variables. If a variable cannot be resolved, the reference in the input string will be unchanged. Double are reduced to a single \$, which allows for escaping the \$(VAR_NAME) syntax: i.e. "(VAR_NAME)" will produce the string literal "\$(VAR_NAME)". Escaped references will never be expanded, regardless of whether the variable exists or not. Defaults to "". |
| `valueFrom` | `object` | Source for the environment variable’s value. Cannot be used if value is not empty. |

## .spec.install.spec.deployments\[\].spec.template.spec.ephemeralContainers\[\].env\[\].valueFrom

Description
Source for the environment variable’s value. Cannot be used if value is not empty.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `configMapKeyRef` | `object` | Selects a key of a ConfigMap. |
| `fieldRef` | `object` | Selects a field of the pod: supports metadata.name, metadata.namespace, `metadata.labels['<KEY>']`, `metadata.annotations['<KEY>']`, spec.nodeName, spec.serviceAccountName, status.hostIP, status.podIP, status.podIPs. |
| `resourceFieldRef` | `object` | Selects a resource of the container: only resources limits and requests (limits.cpu, limits.memory, limits.ephemeral-storage, requests.cpu, requests.memory and requests.ephemeral-storage) are currently supported. |
| `secretKeyRef` | `object` | Selects a key of a secret in the pod’s namespace |

## .spec.install.spec.deployments\[\].spec.template.spec.ephemeralContainers\[\].env\[\].valueFrom.configMapKeyRef

Description
Selects a key of a ConfigMap.

Type
`object`

Required
- `key`

| Property | Type | Description |
|----|----|----|
| `key` | `string` | The key to select. |
| `name` | `string` | Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names> |
| `optional` | `boolean` | Specify whether the ConfigMap or its key must be defined |

## .spec.install.spec.deployments\[\].spec.template.spec.ephemeralContainers\[\].env\[\].valueFrom.fieldRef

Description
Selects a field of the pod: supports metadata.name, metadata.namespace, `metadata.labels['<KEY>']`, `metadata.annotations['<KEY>']`, spec.nodeName, spec.serviceAccountName, status.hostIP, status.podIP, status.podIPs.

Type
`object`

Required
- `fieldPath`

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | Version of the schema the FieldPath is written in terms of, defaults to "v1". |
| `fieldPath` | `string` | Path of the field to select in the specified API version. |

## .spec.install.spec.deployments\[\].spec.template.spec.ephemeralContainers\[\].env\[\].valueFrom.resourceFieldRef

Description
Selects a resource of the container: only resources limits and requests (limits.cpu, limits.memory, limits.ephemeral-storage, requests.cpu, requests.memory and requests.ephemeral-storage) are currently supported.

Type
`object`

Required
- `resource`

| Property | Type | Description |
|----|----|----|
| `containerName` | `string` | Container name: required for volumes, optional for env vars |
| `divisor` | `integer-or-string` | Specifies the output format of the exposed resources, defaults to "1" |
| `resource` | `string` | Required: resource to select |

## .spec.install.spec.deployments\[\].spec.template.spec.ephemeralContainers\[\].env\[\].valueFrom.secretKeyRef

Description
Selects a key of a secret in the pod’s namespace

Type
`object`

Required
- `key`

| Property | Type | Description |
|----|----|----|
| `key` | `string` | The key of the secret to select from. Must be a valid secret key. |
| `name` | `string` | Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names> |
| `optional` | `boolean` | Specify whether the Secret or its key must be defined |

## .spec.install.spec.deployments\[\].spec.template.spec.ephemeralContainers\[\].envFrom

Description
List of sources to populate environment variables in the container. The keys defined within a source must be a C_IDENTIFIER. All invalid keys will be reported as an event when the container is starting. When a key exists in multiple sources, the value associated with the last source will take precedence. Values defined by an Env with a duplicate key will take precedence. Cannot be updated.

Type
`array`

## .spec.install.spec.deployments\[\].spec.template.spec.ephemeralContainers\[\].envFrom\[\]

Description
EnvFromSource represents the source of a set of ConfigMaps or Secrets

Type
`object`

| Property | Type | Description |
|----|----|----|
| `configMapRef` | `object` | The ConfigMap to select from |
| `prefix` | `string` | Optional text to prepend to the name of each environment variable. Must be a C_IDENTIFIER. |
| `secretRef` | `object` | The Secret to select from |

## .spec.install.spec.deployments\[\].spec.template.spec.ephemeralContainers\[\].envFrom\[\].configMapRef

Description
The ConfigMap to select from

Type
`object`

| Property | Type | Description |
|----|----|----|
| `name` | `string` | Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names> |
| `optional` | `boolean` | Specify whether the ConfigMap must be defined |

## .spec.install.spec.deployments\[\].spec.template.spec.ephemeralContainers\[\].envFrom\[\].secretRef

Description
The Secret to select from

Type
`object`

| Property | Type | Description |
|----|----|----|
| `name` | `string` | Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names> |
| `optional` | `boolean` | Specify whether the Secret must be defined |

## .spec.install.spec.deployments\[\].spec.template.spec.ephemeralContainers\[\].lifecycle

Description
Lifecycle is not allowed for ephemeral containers.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `postStart` | `object` | PostStart is called immediately after a container is created. If the handler fails, the container is terminated and restarted according to its restart policy. Other management of the container blocks until the hook completes. More info: <https://kubernetes.io/docs/concepts/containers/container-lifecycle-hooks/#container-hooks> |
| `preStop` | `object` | PreStop is called immediately before a container is terminated due to an API request or management event such as liveness/startup probe failure, preemption, resource contention, etc. The handler is not called if the container crashes or exits. The Pod’s termination grace period countdown begins before the PreStop hook is executed. Regardless of the outcome of the handler, the container will eventually terminate within the Pod’s termination grace period (unless delayed by finalizers). Other management of the container blocks until the hook completes or until the termination grace period is reached. More info: <https://kubernetes.io/docs/concepts/containers/container-lifecycle-hooks/#container-hooks> |
| `stopSignal` | `string` | StopSignal defines which signal will be sent to a container when it is being stopped. If not specified, the default is defined by the container runtime in use. StopSignal can only be set for Pods with a non-empty .spec.os.name |

## .spec.install.spec.deployments\[\].spec.template.spec.ephemeralContainers\[\].lifecycle.postStart

Description
PostStart is called immediately after a container is created. If the handler fails, the container is terminated and restarted according to its restart policy. Other management of the container blocks until the hook completes. More info: <https://kubernetes.io/docs/concepts/containers/container-lifecycle-hooks/#container-hooks>

Type
`object`

| Property | Type | Description |
|----|----|----|
| `exec` | `object` | Exec specifies a command to execute in the container. |
| `httpGet` | `object` | HTTPGet specifies an HTTP GET request to perform. |
| `sleep` | `object` | Sleep represents a duration that the container should sleep. |
| `tcpSocket` | `object` | Deprecated. TCPSocket is NOT supported as a LifecycleHandler and kept for backward compatibility. There is no validation of this field and lifecycle hooks will fail at runtime when it is specified. |

## .spec.install.spec.deployments\[\].spec.template.spec.ephemeralContainers\[\].lifecycle.postStart.exec

Description
Exec specifies a command to execute in the container.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `command` | `array (string)` | Command is the command line to execute inside the container, the working directory for the command is root ('/') in the container’s filesystem. The command is simply exec’d, it is not run inside a shell, so traditional shell instructions ('\|', etc) won’t work. To use a shell, you need to explicitly call out to that shell. Exit status of 0 is treated as live/healthy and non-zero is unhealthy. |

## .spec.install.spec.deployments\[\].spec.template.spec.ephemeralContainers\[\].lifecycle.postStart.httpGet

Description
HTTPGet specifies an HTTP GET request to perform.

Type
`object`

Required
- `port`

| Property | Type | Description |
|----|----|----|
| `host` | `string` | Host name to connect to, defaults to the pod IP. You probably want to set "Host" in httpHeaders instead. |
| `httpHeaders` | `array` | Custom headers to set in the request. HTTP allows repeated headers. |
| `httpHeaders[]` | `object` | HTTPHeader describes a custom header to be used in HTTP probes |
| `path` | `string` | Path to access on the HTTP server. |
| `port` | `integer-or-string` | Name or number of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME. |
| `scheme` | `string` | Scheme to use for connecting to the host. Defaults to HTTP. |

## .spec.install.spec.deployments\[\].spec.template.spec.ephemeralContainers\[\].lifecycle.postStart.httpGet.httpHeaders

Description
Custom headers to set in the request. HTTP allows repeated headers.

Type
`array`

## .spec.install.spec.deployments\[\].spec.template.spec.ephemeralContainers\[\].lifecycle.postStart.httpGet.httpHeaders\[\]

Description
HTTPHeader describes a custom header to be used in HTTP probes

Type
`object`

Required
- `name`

- `value`

| Property | Type | Description |
|----|----|----|
| `name` | `string` | The header field name. This will be canonicalized upon output, so case-variant names will be understood as the same header. |
| `value` | `string` | The header field value |

## .spec.install.spec.deployments\[\].spec.template.spec.ephemeralContainers\[\].lifecycle.postStart.sleep

Description
Sleep represents a duration that the container should sleep.

Type
`object`

Required
- `seconds`

| Property  | Type      | Description                                |
|-----------|-----------|--------------------------------------------|
| `seconds` | `integer` | Seconds is the number of seconds to sleep. |

## .spec.install.spec.deployments\[\].spec.template.spec.ephemeralContainers\[\].lifecycle.postStart.tcpSocket

Description
Deprecated. TCPSocket is NOT supported as a LifecycleHandler and kept for backward compatibility. There is no validation of this field and lifecycle hooks will fail at runtime when it is specified.

Type
`object`

Required
- `port`

| Property | Type | Description |
|----|----|----|
| `host` | `string` | Optional: Host name to connect to, defaults to the pod IP. |
| `port` | `integer-or-string` | Number or name of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME. |

## .spec.install.spec.deployments\[\].spec.template.spec.ephemeralContainers\[\].lifecycle.preStop

Description
PreStop is called immediately before a container is terminated due to an API request or management event such as liveness/startup probe failure, preemption, resource contention, etc. The handler is not called if the container crashes or exits. The Pod’s termination grace period countdown begins before the PreStop hook is executed. Regardless of the outcome of the handler, the container will eventually terminate within the Pod’s termination grace period (unless delayed by finalizers). Other management of the container blocks until the hook completes or until the termination grace period is reached. More info: <https://kubernetes.io/docs/concepts/containers/container-lifecycle-hooks/#container-hooks>

Type
`object`

| Property | Type | Description |
|----|----|----|
| `exec` | `object` | Exec specifies a command to execute in the container. |
| `httpGet` | `object` | HTTPGet specifies an HTTP GET request to perform. |
| `sleep` | `object` | Sleep represents a duration that the container should sleep. |
| `tcpSocket` | `object` | Deprecated. TCPSocket is NOT supported as a LifecycleHandler and kept for backward compatibility. There is no validation of this field and lifecycle hooks will fail at runtime when it is specified. |

## .spec.install.spec.deployments\[\].spec.template.spec.ephemeralContainers\[\].lifecycle.preStop.exec

Description
Exec specifies a command to execute in the container.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `command` | `array (string)` | Command is the command line to execute inside the container, the working directory for the command is root ('/') in the container’s filesystem. The command is simply exec’d, it is not run inside a shell, so traditional shell instructions ('\|', etc) won’t work. To use a shell, you need to explicitly call out to that shell. Exit status of 0 is treated as live/healthy and non-zero is unhealthy. |

## .spec.install.spec.deployments\[\].spec.template.spec.ephemeralContainers\[\].lifecycle.preStop.httpGet

Description
HTTPGet specifies an HTTP GET request to perform.

Type
`object`

Required
- `port`

| Property | Type | Description |
|----|----|----|
| `host` | `string` | Host name to connect to, defaults to the pod IP. You probably want to set "Host" in httpHeaders instead. |
| `httpHeaders` | `array` | Custom headers to set in the request. HTTP allows repeated headers. |
| `httpHeaders[]` | `object` | HTTPHeader describes a custom header to be used in HTTP probes |
| `path` | `string` | Path to access on the HTTP server. |
| `port` | `integer-or-string` | Name or number of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME. |
| `scheme` | `string` | Scheme to use for connecting to the host. Defaults to HTTP. |

## .spec.install.spec.deployments\[\].spec.template.spec.ephemeralContainers\[\].lifecycle.preStop.httpGet.httpHeaders

Description
Custom headers to set in the request. HTTP allows repeated headers.

Type
`array`

## .spec.install.spec.deployments\[\].spec.template.spec.ephemeralContainers\[\].lifecycle.preStop.httpGet.httpHeaders\[\]

Description
HTTPHeader describes a custom header to be used in HTTP probes

Type
`object`

Required
- `name`

- `value`

| Property | Type | Description |
|----|----|----|
| `name` | `string` | The header field name. This will be canonicalized upon output, so case-variant names will be understood as the same header. |
| `value` | `string` | The header field value |

## .spec.install.spec.deployments\[\].spec.template.spec.ephemeralContainers\[\].lifecycle.preStop.sleep

Description
Sleep represents a duration that the container should sleep.

Type
`object`

Required
- `seconds`

| Property  | Type      | Description                                |
|-----------|-----------|--------------------------------------------|
| `seconds` | `integer` | Seconds is the number of seconds to sleep. |

## .spec.install.spec.deployments\[\].spec.template.spec.ephemeralContainers\[\].lifecycle.preStop.tcpSocket

Description
Deprecated. TCPSocket is NOT supported as a LifecycleHandler and kept for backward compatibility. There is no validation of this field and lifecycle hooks will fail at runtime when it is specified.

Type
`object`

Required
- `port`

| Property | Type | Description |
|----|----|----|
| `host` | `string` | Optional: Host name to connect to, defaults to the pod IP. |
| `port` | `integer-or-string` | Number or name of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME. |

## .spec.install.spec.deployments\[\].spec.template.spec.ephemeralContainers\[\].livenessProbe

Description
Probes are not allowed for ephemeral containers.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `exec` | `object` | Exec specifies a command to execute in the container. |
| `failureThreshold` | `integer` | Minimum consecutive failures for the probe to be considered failed after having succeeded. Defaults to 3. Minimum value is 1. |
| `grpc` | `object` | GRPC specifies a GRPC HealthCheckRequest. |
| `httpGet` | `object` | HTTPGet specifies an HTTP GET request to perform. |
| `initialDelaySeconds` | `integer` | Number of seconds after the container has started before liveness probes are initiated. More info: <https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes> |
| `periodSeconds` | `integer` | How often (in seconds) to perform the probe. Default to 10 seconds. Minimum value is 1. |
| `successThreshold` | `integer` | Minimum consecutive successes for the probe to be considered successful after having failed. Defaults to 1. Must be 1 for liveness and startup. Minimum value is 1. |
| `tcpSocket` | `object` | TCPSocket specifies a connection to a TCP port. |
| `terminationGracePeriodSeconds` | `integer` | Optional duration in seconds the pod needs to terminate gracefully upon probe failure. The grace period is the duration in seconds after the processes running in the pod are sent a termination signal and the time when the processes are forcibly halted with a kill signal. Set this value longer than the expected cleanup time for your process. If this value is nil, the pod’s terminationGracePeriodSeconds will be used. Otherwise, this value overrides the value provided by the pod spec. Value must be non-negative integer. The value zero indicates stop immediately via the kill signal (no opportunity to shut down). This is a beta field and requires enabling ProbeTerminationGracePeriod feature gate. Minimum value is 1. spec.terminationGracePeriodSeconds is used if unset. |
| `timeoutSeconds` | `integer` | Number of seconds after which the probe times out. Defaults to 1 second. Minimum value is 1. More info: <https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes> |

## .spec.install.spec.deployments\[\].spec.template.spec.ephemeralContainers\[\].livenessProbe.exec

Description
Exec specifies a command to execute in the container.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `command` | `array (string)` | Command is the command line to execute inside the container, the working directory for the command is root ('/') in the container’s filesystem. The command is simply exec’d, it is not run inside a shell, so traditional shell instructions ('\|', etc) won’t work. To use a shell, you need to explicitly call out to that shell. Exit status of 0 is treated as live/healthy and non-zero is unhealthy. |

## .spec.install.spec.deployments\[\].spec.template.spec.ephemeralContainers\[\].livenessProbe.grpc

Description
GRPC specifies a GRPC HealthCheckRequest.

Type
`object`

Required
- `port`

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
<td style="text-align: left;"><p><code>port</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p>Port number of the gRPC service. Number must be in the range 1 to 65535.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>service</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Service is the name of the service to place in the gRPC HealthCheckRequest (see <a href="https://github.com/grpc/grpc/blob/master/doc/health-checking.md">https://github.com/grpc/grpc/blob/master/doc/health-checking.md</a>).</p>
<p>If this is not specified, the default behavior is defined by gRPC.</p></td>
</tr>
</tbody>
</table>

## .spec.install.spec.deployments\[\].spec.template.spec.ephemeralContainers\[\].livenessProbe.httpGet

Description
HTTPGet specifies an HTTP GET request to perform.

Type
`object`

Required
- `port`

| Property | Type | Description |
|----|----|----|
| `host` | `string` | Host name to connect to, defaults to the pod IP. You probably want to set "Host" in httpHeaders instead. |
| `httpHeaders` | `array` | Custom headers to set in the request. HTTP allows repeated headers. |
| `httpHeaders[]` | `object` | HTTPHeader describes a custom header to be used in HTTP probes |
| `path` | `string` | Path to access on the HTTP server. |
| `port` | `integer-or-string` | Name or number of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME. |
| `scheme` | `string` | Scheme to use for connecting to the host. Defaults to HTTP. |

## .spec.install.spec.deployments\[\].spec.template.spec.ephemeralContainers\[\].livenessProbe.httpGet.httpHeaders

Description
Custom headers to set in the request. HTTP allows repeated headers.

Type
`array`

## .spec.install.spec.deployments\[\].spec.template.spec.ephemeralContainers\[\].livenessProbe.httpGet.httpHeaders\[\]

Description
HTTPHeader describes a custom header to be used in HTTP probes

Type
`object`

Required
- `name`

- `value`

| Property | Type | Description |
|----|----|----|
| `name` | `string` | The header field name. This will be canonicalized upon output, so case-variant names will be understood as the same header. |
| `value` | `string` | The header field value |

## .spec.install.spec.deployments\[\].spec.template.spec.ephemeralContainers\[\].livenessProbe.tcpSocket

Description
TCPSocket specifies a connection to a TCP port.

Type
`object`

Required
- `port`

| Property | Type | Description |
|----|----|----|
| `host` | `string` | Optional: Host name to connect to, defaults to the pod IP. |
| `port` | `integer-or-string` | Number or name of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME. |

## .spec.install.spec.deployments\[\].spec.template.spec.ephemeralContainers\[\].ports

Description
Ports are not allowed for ephemeral containers.

Type
`array`

## .spec.install.spec.deployments\[\].spec.template.spec.ephemeralContainers\[\].ports\[\]

Description
ContainerPort represents a network port in a single container.

Type
`object`

Required
- `containerPort`

| Property | Type | Description |
|----|----|----|
| `containerPort` | `integer` | Number of port to expose on the pod’s IP address. This must be a valid port number, 0 \< x \< 65536. |
| `hostIP` | `string` | What host IP to bind the external port to. |
| `hostPort` | `integer` | Number of port to expose on the host. If specified, this must be a valid port number, 0 \< x \< 65536. If HostNetwork is specified, this must match ContainerPort. Most containers do not need this. |
| `name` | `string` | If specified, this must be an IANA_SVC_NAME and unique within the pod. Each named port in a pod must have a unique name. Name for the port that can be referred to by services. |
| `protocol` | `string` | Protocol for port. Must be UDP, TCP, or SCTP. Defaults to "TCP". |

## .spec.install.spec.deployments\[\].spec.template.spec.ephemeralContainers\[\].readinessProbe

Description
Probes are not allowed for ephemeral containers.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `exec` | `object` | Exec specifies a command to execute in the container. |
| `failureThreshold` | `integer` | Minimum consecutive failures for the probe to be considered failed after having succeeded. Defaults to 3. Minimum value is 1. |
| `grpc` | `object` | GRPC specifies a GRPC HealthCheckRequest. |
| `httpGet` | `object` | HTTPGet specifies an HTTP GET request to perform. |
| `initialDelaySeconds` | `integer` | Number of seconds after the container has started before liveness probes are initiated. More info: <https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes> |
| `periodSeconds` | `integer` | How often (in seconds) to perform the probe. Default to 10 seconds. Minimum value is 1. |
| `successThreshold` | `integer` | Minimum consecutive successes for the probe to be considered successful after having failed. Defaults to 1. Must be 1 for liveness and startup. Minimum value is 1. |
| `tcpSocket` | `object` | TCPSocket specifies a connection to a TCP port. |
| `terminationGracePeriodSeconds` | `integer` | Optional duration in seconds the pod needs to terminate gracefully upon probe failure. The grace period is the duration in seconds after the processes running in the pod are sent a termination signal and the time when the processes are forcibly halted with a kill signal. Set this value longer than the expected cleanup time for your process. If this value is nil, the pod’s terminationGracePeriodSeconds will be used. Otherwise, this value overrides the value provided by the pod spec. Value must be non-negative integer. The value zero indicates stop immediately via the kill signal (no opportunity to shut down). This is a beta field and requires enabling ProbeTerminationGracePeriod feature gate. Minimum value is 1. spec.terminationGracePeriodSeconds is used if unset. |
| `timeoutSeconds` | `integer` | Number of seconds after which the probe times out. Defaults to 1 second. Minimum value is 1. More info: <https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes> |

## .spec.install.spec.deployments\[\].spec.template.spec.ephemeralContainers\[\].readinessProbe.exec

Description
Exec specifies a command to execute in the container.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `command` | `array (string)` | Command is the command line to execute inside the container, the working directory for the command is root ('/') in the container’s filesystem. The command is simply exec’d, it is not run inside a shell, so traditional shell instructions ('\|', etc) won’t work. To use a shell, you need to explicitly call out to that shell. Exit status of 0 is treated as live/healthy and non-zero is unhealthy. |

## .spec.install.spec.deployments\[\].spec.template.spec.ephemeralContainers\[\].readinessProbe.grpc

Description
GRPC specifies a GRPC HealthCheckRequest.

Type
`object`

Required
- `port`

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
<td style="text-align: left;"><p><code>port</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p>Port number of the gRPC service. Number must be in the range 1 to 65535.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>service</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Service is the name of the service to place in the gRPC HealthCheckRequest (see <a href="https://github.com/grpc/grpc/blob/master/doc/health-checking.md">https://github.com/grpc/grpc/blob/master/doc/health-checking.md</a>).</p>
<p>If this is not specified, the default behavior is defined by gRPC.</p></td>
</tr>
</tbody>
</table>

## .spec.install.spec.deployments\[\].spec.template.spec.ephemeralContainers\[\].readinessProbe.httpGet

Description
HTTPGet specifies an HTTP GET request to perform.

Type
`object`

Required
- `port`

| Property | Type | Description |
|----|----|----|
| `host` | `string` | Host name to connect to, defaults to the pod IP. You probably want to set "Host" in httpHeaders instead. |
| `httpHeaders` | `array` | Custom headers to set in the request. HTTP allows repeated headers. |
| `httpHeaders[]` | `object` | HTTPHeader describes a custom header to be used in HTTP probes |
| `path` | `string` | Path to access on the HTTP server. |
| `port` | `integer-or-string` | Name or number of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME. |
| `scheme` | `string` | Scheme to use for connecting to the host. Defaults to HTTP. |

## .spec.install.spec.deployments\[\].spec.template.spec.ephemeralContainers\[\].readinessProbe.httpGet.httpHeaders

Description
Custom headers to set in the request. HTTP allows repeated headers.

Type
`array`

## .spec.install.spec.deployments\[\].spec.template.spec.ephemeralContainers\[\].readinessProbe.httpGet.httpHeaders\[\]

Description
HTTPHeader describes a custom header to be used in HTTP probes

Type
`object`

Required
- `name`

- `value`

| Property | Type | Description |
|----|----|----|
| `name` | `string` | The header field name. This will be canonicalized upon output, so case-variant names will be understood as the same header. |
| `value` | `string` | The header field value |

## .spec.install.spec.deployments\[\].spec.template.spec.ephemeralContainers\[\].readinessProbe.tcpSocket

Description
TCPSocket specifies a connection to a TCP port.

Type
`object`

Required
- `port`

| Property | Type | Description |
|----|----|----|
| `host` | `string` | Optional: Host name to connect to, defaults to the pod IP. |
| `port` | `integer-or-string` | Number or name of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME. |

## .spec.install.spec.deployments\[\].spec.template.spec.ephemeralContainers\[\].resizePolicy

Description
Resources resize policy for the container.

Type
`array`

## .spec.install.spec.deployments\[\].spec.template.spec.ephemeralContainers\[\].resizePolicy\[\]

Description
ContainerResizePolicy represents resource resize policy for the container.

Type
`object`

Required
- `resourceName`

- `restartPolicy`

| Property | Type | Description |
|----|----|----|
| `resourceName` | `string` | Name of the resource to which this resource resize policy applies. Supported values: cpu, memory. |
| `restartPolicy` | `string` | Restart policy to apply when specified resource is resized. If not specified, it defaults to NotRequired. |

## .spec.install.spec.deployments\[\].spec.template.spec.ephemeralContainers\[\].resources

Description
Resources are not allowed for ephemeral containers. Ephemeral containers use spare resources already allocated to the pod.

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
<td style="text-align: left;"><p><code>claims</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>Claims lists the names of resources, defined in spec.resourceClaims, that are used by this container.</p>
<p>This is an alpha field and requires enabling the DynamicResourceAllocation feature gate.</p>
<p>This field is immutable. It can only be set for containers.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>claims[]</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>ResourceClaim references one entry in PodSpec.ResourceClaims.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>limits</code></p></td>
<td style="text-align: left;"><p><code>integer-or-string</code></p></td>
<td style="text-align: left;"><p>Limits describes the maximum amount of compute resources allowed. More info: <a href="https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/">https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>requests</code></p></td>
<td style="text-align: left;"><p><code>integer-or-string</code></p></td>
<td style="text-align: left;"><p>Requests describes the minimum amount of compute resources required. If Requests is omitted for a container, it defaults to Limits if that is explicitly specified, otherwise to an implementation-defined value. Requests cannot exceed Limits. More info: <a href="https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/">https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/</a></p></td>
</tr>
</tbody>
</table>

## .spec.install.spec.deployments\[\].spec.template.spec.ephemeralContainers\[\].resources.claims

Description
Claims lists the names of resources, defined in spec.resourceClaims, that are used by this container.

This is an alpha field and requires enabling the DynamicResourceAllocation feature gate.

This field is immutable. It can only be set for containers.

Type
`array`

## .spec.install.spec.deployments\[\].spec.template.spec.ephemeralContainers\[\].resources.claims\[\]

Description
ResourceClaim references one entry in PodSpec.ResourceClaims.

Type
`object`

Required
- `name`

| Property | Type | Description |
|----|----|----|
| `name` | `string` | Name must match the name of one entry in pod.spec.resourceClaims of the Pod where this field is used. It makes that resource available inside a container. |
| `request` | `string` | Request is the name chosen for a request in the referenced claim. If empty, everything from the claim is made available, otherwise only the result of this request. |

## .spec.install.spec.deployments\[\].spec.template.spec.ephemeralContainers\[\].securityContext

Description
Optional: SecurityContext defines the security options the ephemeral container should be run with. If set, the fields of SecurityContext override the equivalent fields of PodSecurityContext.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `allowPrivilegeEscalation` | `boolean` | AllowPrivilegeEscalation controls whether a process can gain more privileges than its parent process. This bool directly controls if the no_new_privs flag will be set on the container process. AllowPrivilegeEscalation is true always when the container is: 1) run as Privileged 2) has CAP_SYS_ADMIN Note that this field cannot be set when spec.os.name is windows. |
| `appArmorProfile` | `object` | appArmorProfile is the AppArmor options to use by this container. If set, this profile overrides the pod’s appArmorProfile. Note that this field cannot be set when spec.os.name is windows. |
| `capabilities` | `object` | The capabilities to add/drop when running containers. Defaults to the default set of capabilities granted by the container runtime. Note that this field cannot be set when spec.os.name is windows. |
| `privileged` | `boolean` | Run container in privileged mode. Processes in privileged containers are essentially equivalent to root on the host. Defaults to false. Note that this field cannot be set when spec.os.name is windows. |
| `procMount` | `string` | procMount denotes the type of proc mount to use for the containers. The default value is Default which uses the container runtime defaults for readonly paths and masked paths. This requires the ProcMountType feature flag to be enabled. Note that this field cannot be set when spec.os.name is windows. |
| `readOnlyRootFilesystem` | `boolean` | Whether this container has a read-only root filesystem. Default is false. Note that this field cannot be set when spec.os.name is windows. |
| `runAsGroup` | `integer` | The GID to run the entrypoint of the container process. Uses runtime default if unset. May also be set in PodSecurityContext. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence. Note that this field cannot be set when spec.os.name is windows. |
| `runAsNonRoot` | `boolean` | Indicates that the container must run as a non-root user. If true, the Kubelet will validate the image at runtime to ensure that it does not run as UID 0 (root) and fail to start the container if it does. If unset or false, no such validation will be performed. May also be set in PodSecurityContext. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence. |
| `runAsUser` | `integer` | The UID to run the entrypoint of the container process. Defaults to user specified in image metadata if unspecified. May also be set in PodSecurityContext. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence. Note that this field cannot be set when spec.os.name is windows. |
| `seLinuxOptions` | `object` | The SELinux context to be applied to the container. If unspecified, the container runtime will allocate a random SELinux context for each container. May also be set in PodSecurityContext. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence. Note that this field cannot be set when spec.os.name is windows. |
| `seccompProfile` | `object` | The seccomp options to use by this container. If seccomp options are provided at both the pod & container level, the container options override the pod options. Note that this field cannot be set when spec.os.name is windows. |
| `windowsOptions` | `object` | The Windows specific settings applied to all containers. If unspecified, the options from the PodSecurityContext will be used. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence. Note that this field cannot be set when spec.os.name is linux. |

## .spec.install.spec.deployments\[\].spec.template.spec.ephemeralContainers\[\].securityContext.appArmorProfile

Description
appArmorProfile is the AppArmor options to use by this container. If set, this profile overrides the pod’s appArmorProfile. Note that this field cannot be set when spec.os.name is windows.

Type
`object`

Required
- `type`

| Property | Type | Description |
|----|----|----|
| `localhostProfile` | `string` | localhostProfile indicates a profile loaded on the node that should be used. The profile must be preconfigured on the node to work. Must match the loaded name of the profile. Must be set if and only if type is "Localhost". |
| `type` | `string` | type indicates which kind of AppArmor profile will be applied. Valid options are: Localhost - a profile pre-loaded on the node. RuntimeDefault - the container runtime’s default profile. Unconfined - no AppArmor enforcement. |

## .spec.install.spec.deployments\[\].spec.template.spec.ephemeralContainers\[\].securityContext.capabilities

Description
The capabilities to add/drop when running containers. Defaults to the default set of capabilities granted by the container runtime. Note that this field cannot be set when spec.os.name is windows.

Type
`object`

| Property | Type             | Description          |
|----------|------------------|----------------------|
| `add`    | `array (string)` | Added capabilities   |
| `drop`   | `array (string)` | Removed capabilities |

## .spec.install.spec.deployments\[\].spec.template.spec.ephemeralContainers\[\].securityContext.seLinuxOptions

Description
The SELinux context to be applied to the container. If unspecified, the container runtime will allocate a random SELinux context for each container. May also be set in PodSecurityContext. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence. Note that this field cannot be set when spec.os.name is windows.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `level` | `string` | Level is SELinux level label that applies to the container. |
| `role` | `string` | Role is a SELinux role label that applies to the container. |
| `type` | `string` | Type is a SELinux type label that applies to the container. |
| `user` | `string` | User is a SELinux user label that applies to the container. |

## .spec.install.spec.deployments\[\].spec.template.spec.ephemeralContainers\[\].securityContext.seccompProfile

Description
The seccomp options to use by this container. If seccomp options are provided at both the pod & container level, the container options override the pod options. Note that this field cannot be set when spec.os.name is windows.

Type
`object`

Required
- `type`

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
<td style="text-align: left;"><p><code>localhostProfile</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>localhostProfile indicates a profile defined in a file on the node should be used. The profile must be preconfigured on the node to work. Must be a descending path, relative to the kubelet’s configured seccomp profile location. Must be set if type is "Localhost". Must NOT be set for any other type.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>type</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>type indicates which kind of seccomp profile will be applied. Valid options are:</p>
<p>Localhost - a profile defined in a file on the node should be used. RuntimeDefault - the container runtime default profile should be used. Unconfined - no profile should be applied.</p></td>
</tr>
</tbody>
</table>

## .spec.install.spec.deployments\[\].spec.template.spec.ephemeralContainers\[\].securityContext.windowsOptions

Description
The Windows specific settings applied to all containers. If unspecified, the options from the PodSecurityContext will be used. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence. Note that this field cannot be set when spec.os.name is linux.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `gmsaCredentialSpec` | `string` | GMSACredentialSpec is where the GMSA admission webhook (<https://github.com/kubernetes-sigs/windows-gmsa>) inlines the contents of the GMSA credential spec named by the GMSACredentialSpecName field. |
| `gmsaCredentialSpecName` | `string` | GMSACredentialSpecName is the name of the GMSA credential spec to use. |
| `hostProcess` | `boolean` | HostProcess determines if a container should be run as a 'Host Process' container. All of a Pod’s containers must have the same effective HostProcess value (it is not allowed to have a mix of HostProcess containers and non-HostProcess containers). In addition, if HostProcess is true then HostNetwork must also be set to true. |
| `runAsUserName` | `string` | The UserName in Windows to run the entrypoint of the container process. Defaults to the user specified in image metadata if unspecified. May also be set in PodSecurityContext. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence. |

## .spec.install.spec.deployments\[\].spec.template.spec.ephemeralContainers\[\].startupProbe

Description
Probes are not allowed for ephemeral containers.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `exec` | `object` | Exec specifies a command to execute in the container. |
| `failureThreshold` | `integer` | Minimum consecutive failures for the probe to be considered failed after having succeeded. Defaults to 3. Minimum value is 1. |
| `grpc` | `object` | GRPC specifies a GRPC HealthCheckRequest. |
| `httpGet` | `object` | HTTPGet specifies an HTTP GET request to perform. |
| `initialDelaySeconds` | `integer` | Number of seconds after the container has started before liveness probes are initiated. More info: <https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes> |
| `periodSeconds` | `integer` | How often (in seconds) to perform the probe. Default to 10 seconds. Minimum value is 1. |
| `successThreshold` | `integer` | Minimum consecutive successes for the probe to be considered successful after having failed. Defaults to 1. Must be 1 for liveness and startup. Minimum value is 1. |
| `tcpSocket` | `object` | TCPSocket specifies a connection to a TCP port. |
| `terminationGracePeriodSeconds` | `integer` | Optional duration in seconds the pod needs to terminate gracefully upon probe failure. The grace period is the duration in seconds after the processes running in the pod are sent a termination signal and the time when the processes are forcibly halted with a kill signal. Set this value longer than the expected cleanup time for your process. If this value is nil, the pod’s terminationGracePeriodSeconds will be used. Otherwise, this value overrides the value provided by the pod spec. Value must be non-negative integer. The value zero indicates stop immediately via the kill signal (no opportunity to shut down). This is a beta field and requires enabling ProbeTerminationGracePeriod feature gate. Minimum value is 1. spec.terminationGracePeriodSeconds is used if unset. |
| `timeoutSeconds` | `integer` | Number of seconds after which the probe times out. Defaults to 1 second. Minimum value is 1. More info: <https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes> |

## .spec.install.spec.deployments\[\].spec.template.spec.ephemeralContainers\[\].startupProbe.exec

Description
Exec specifies a command to execute in the container.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `command` | `array (string)` | Command is the command line to execute inside the container, the working directory for the command is root ('/') in the container’s filesystem. The command is simply exec’d, it is not run inside a shell, so traditional shell instructions ('\|', etc) won’t work. To use a shell, you need to explicitly call out to that shell. Exit status of 0 is treated as live/healthy and non-zero is unhealthy. |

## .spec.install.spec.deployments\[\].spec.template.spec.ephemeralContainers\[\].startupProbe.grpc

Description
GRPC specifies a GRPC HealthCheckRequest.

Type
`object`

Required
- `port`

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
<td style="text-align: left;"><p><code>port</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p>Port number of the gRPC service. Number must be in the range 1 to 65535.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>service</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Service is the name of the service to place in the gRPC HealthCheckRequest (see <a href="https://github.com/grpc/grpc/blob/master/doc/health-checking.md">https://github.com/grpc/grpc/blob/master/doc/health-checking.md</a>).</p>
<p>If this is not specified, the default behavior is defined by gRPC.</p></td>
</tr>
</tbody>
</table>

## .spec.install.spec.deployments\[\].spec.template.spec.ephemeralContainers\[\].startupProbe.httpGet

Description
HTTPGet specifies an HTTP GET request to perform.

Type
`object`

Required
- `port`

| Property | Type | Description |
|----|----|----|
| `host` | `string` | Host name to connect to, defaults to the pod IP. You probably want to set "Host" in httpHeaders instead. |
| `httpHeaders` | `array` | Custom headers to set in the request. HTTP allows repeated headers. |
| `httpHeaders[]` | `object` | HTTPHeader describes a custom header to be used in HTTP probes |
| `path` | `string` | Path to access on the HTTP server. |
| `port` | `integer-or-string` | Name or number of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME. |
| `scheme` | `string` | Scheme to use for connecting to the host. Defaults to HTTP. |

## .spec.install.spec.deployments\[\].spec.template.spec.ephemeralContainers\[\].startupProbe.httpGet.httpHeaders

Description
Custom headers to set in the request. HTTP allows repeated headers.

Type
`array`

## .spec.install.spec.deployments\[\].spec.template.spec.ephemeralContainers\[\].startupProbe.httpGet.httpHeaders\[\]

Description
HTTPHeader describes a custom header to be used in HTTP probes

Type
`object`

Required
- `name`

- `value`

| Property | Type | Description |
|----|----|----|
| `name` | `string` | The header field name. This will be canonicalized upon output, so case-variant names will be understood as the same header. |
| `value` | `string` | The header field value |

## .spec.install.spec.deployments\[\].spec.template.spec.ephemeralContainers\[\].startupProbe.tcpSocket

Description
TCPSocket specifies a connection to a TCP port.

Type
`object`

Required
- `port`

| Property | Type | Description |
|----|----|----|
| `host` | `string` | Optional: Host name to connect to, defaults to the pod IP. |
| `port` | `integer-or-string` | Number or name of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME. |

## .spec.install.spec.deployments\[\].spec.template.spec.ephemeralContainers\[\].volumeDevices

Description
volumeDevices is the list of block devices to be used by the container.

Type
`array`

## .spec.install.spec.deployments\[\].spec.template.spec.ephemeralContainers\[\].volumeDevices\[\]

Description
volumeDevice describes a mapping of a raw block device within a container.

Type
`object`

Required
- `devicePath`

- `name`

| Property | Type | Description |
|----|----|----|
| `devicePath` | `string` | devicePath is the path inside of the container that the device will be mapped to. |
| `name` | `string` | name must match the name of a persistentVolumeClaim in the pod |

## .spec.install.spec.deployments\[\].spec.template.spec.ephemeralContainers\[\].volumeMounts

Description
Pod volumes to mount into the container’s filesystem. Subpath mounts are not allowed for ephemeral containers. Cannot be updated.

Type
`array`

## .spec.install.spec.deployments\[\].spec.template.spec.ephemeralContainers\[\].volumeMounts\[\]

Description
VolumeMount describes a mounting of a Volume within a container.

Type
`object`

Required
- `mountPath`

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
<td style="text-align: left;"><p><code>mountPath</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Path within the container at which the volume should be mounted. Must not contain ':'.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>mountPropagation</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>mountPropagation determines how mounts are propagated from the host to container and the other way around. When not set, MountPropagationNone is used. This field is beta in 1.10. When RecursiveReadOnly is set to IfPossible or to Enabled, MountPropagation must be None or unspecified (which defaults to None).</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>name</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>This must match the Name of a Volume.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>readOnly</code></p></td>
<td style="text-align: left;"><p><code>boolean</code></p></td>
<td style="text-align: left;"><p>Mounted read-only if true, read-write otherwise (false or unspecified). Defaults to false.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>recursiveReadOnly</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>RecursiveReadOnly specifies whether read-only mounts should be handled recursively.</p>
<p>If ReadOnly is false, this field has no meaning and must be unspecified.</p>
<p>If ReadOnly is true, and this field is set to Disabled, the mount is not made recursively read-only. If this field is set to IfPossible, the mount is made recursively read-only, if it is supported by the container runtime. If this field is set to Enabled, the mount is made recursively read-only if it is supported by the container runtime, otherwise the pod will not be started and an error will be generated to indicate the reason.</p>
<p>If this field is set to IfPossible or Enabled, MountPropagation must be set to None (or be unspecified, which defaults to None).</p>
<p>If this field is not specified, it is treated as an equivalent of Disabled.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>subPath</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Path within the volume from which the container’s volume should be mounted. Defaults to "" (volume’s root).</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>subPathExpr</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Expanded path within the volume from which the container’s volume should be mounted. Behaves similarly to SubPath but environment variable references $(VAR_NAME) are expanded using the container’s environment. Defaults to "" (volume’s root). SubPathExpr and SubPath are mutually exclusive.</p></td>
</tr>
</tbody>
</table>

## .spec.install.spec.deployments\[\].spec.template.spec.hostAliases

Description
HostAliases is an optional list of hosts and IPs that will be injected into the pod’s hosts file if specified.

Type
`array`

## .spec.install.spec.deployments\[\].spec.template.spec.hostAliases\[\]

Description
HostAlias holds the mapping between IP and hostnames that will be injected as an entry in the pod’s hosts file.

Type
`object`

Required
- `ip`

| Property    | Type             | Description                         |
|-------------|------------------|-------------------------------------|
| `hostnames` | `array (string)` | Hostnames for the above IP address. |
| `ip`        | `string`         | IP address of the host file entry.  |

## .spec.install.spec.deployments\[\].spec.template.spec.imagePullSecrets

Description
ImagePullSecrets is an optional list of references to secrets in the same namespace to use for pulling any of the images used by this PodSpec. If specified, these secrets will be passed to individual puller implementations for them to use. More info: <https://kubernetes.io/docs/concepts/containers/images#specifying-imagepullsecrets-on-a-pod>

Type
`array`

## .spec.install.spec.deployments\[\].spec.template.spec.imagePullSecrets\[\]

Description
LocalObjectReference contains enough information to let you locate the referenced object inside the same namespace.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `name` | `string` | Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names> |

## .spec.install.spec.deployments\[\].spec.template.spec.initContainers

Description
List of initialization containers belonging to the pod. Init containers are executed in order prior to containers being started. If any init container fails, the pod is considered to have failed and is handled according to its restartPolicy. The name for an init container or normal container must be unique among all containers. Init containers may not have Lifecycle actions, Readiness probes, Liveness probes, or Startup probes. The resourceRequirements of an init container are taken into account during scheduling by finding the highest request/limit for each resource type, and then using the max of that value or the sum of the normal containers. Limits are applied to init containers in a similar fashion. Init containers cannot currently be added or removed. Cannot be updated. More info: <https://kubernetes.io/docs/concepts/workloads/pods/init-containers/>

Type
`array`

## .spec.install.spec.deployments\[\].spec.template.spec.initContainers\[\]

Description
A single application container that you want to run within a pod.

Type
`object`

Required
- `name`

| Property | Type | Description |
|----|----|----|
| `args` | `array (string)` | Arguments to the entrypoint. The container image’s CMD is used if this is not provided. Variable references \$(VAR_NAME) are expanded using the container’s environment. If a variable cannot be resolved, the reference in the input string will be unchanged. Double are reduced to a single \$, which allows for escaping the \$(VAR_NAME) syntax: i.e. "(VAR_NAME)" will produce the string literal "\$(VAR_NAME)". Escaped references will never be expanded, regardless of whether the variable exists or not. Cannot be updated. More info: <https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#running-a-command-in-a-shell> |
| `command` | `array (string)` | Entrypoint array. Not executed within a shell. The container image’s ENTRYPOINT is used if this is not provided. Variable references \$(VAR_NAME) are expanded using the container’s environment. If a variable cannot be resolved, the reference in the input string will be unchanged. Double are reduced to a single \$, which allows for escaping the \$(VAR_NAME) syntax: i.e. "(VAR_NAME)" will produce the string literal "\$(VAR_NAME)". Escaped references will never be expanded, regardless of whether the variable exists or not. Cannot be updated. More info: <https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#running-a-command-in-a-shell> |
| `env` | `array` | List of environment variables to set in the container. Cannot be updated. |
| `env[]` | `object` | EnvVar represents an environment variable present in a Container. |
| `envFrom` | `array` | List of sources to populate environment variables in the container. The keys defined within a source must be a C_IDENTIFIER. All invalid keys will be reported as an event when the container is starting. When a key exists in multiple sources, the value associated with the last source will take precedence. Values defined by an Env with a duplicate key will take precedence. Cannot be updated. |
| `envFrom[]` | `object` | EnvFromSource represents the source of a set of ConfigMaps or Secrets |
| `image` | `string` | Container image name. More info: <https://kubernetes.io/docs/concepts/containers/images> This field is optional to allow higher level config management to default or override container images in workload controllers like Deployments and StatefulSets. |
| `imagePullPolicy` | `string` | Image pull policy. One of Always, Never, IfNotPresent. Defaults to Always if :latest tag is specified, or IfNotPresent otherwise. Cannot be updated. More info: <https://kubernetes.io/docs/concepts/containers/images#updating-images> |
| `lifecycle` | `object` | Actions that the management system should take in response to container lifecycle events. Cannot be updated. |
| `livenessProbe` | `object` | Periodic probe of container liveness. Container will be restarted if the probe fails. Cannot be updated. More info: <https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes> |
| `name` | `string` | Name of the container specified as a DNS_LABEL. Each container in a pod must have a unique name (DNS_LABEL). Cannot be updated. |
| `ports` | `array` | List of ports to expose from the container. Not specifying a port here DOES NOT prevent that port from being exposed. Any port which is listening on the default "0.0.0.0" address inside a container will be accessible from the network. Modifying this array with strategic merge patch may corrupt the data. For more information See <https://github.com/kubernetes/kubernetes/issues/108255>. Cannot be updated. |
| `ports[]` | `object` | ContainerPort represents a network port in a single container. |
| `readinessProbe` | `object` | Periodic probe of container service readiness. Container will be removed from service endpoints if the probe fails. Cannot be updated. More info: <https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes> |
| `resizePolicy` | `array` | Resources resize policy for the container. |
| `resizePolicy[]` | `object` | ContainerResizePolicy represents resource resize policy for the container. |
| `resources` | `object` | Compute Resources required by this container. Cannot be updated. More info: <https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/> |
| `restartPolicy` | `string` | RestartPolicy defines the restart behavior of individual containers in a pod. This field may only be set for init containers, and the only allowed value is "Always". For non-init containers or when this field is not specified, the restart behavior is defined by the Pod’s restart policy and the container type. Setting the RestartPolicy as "Always" for the init container will have the following effect: this init container will be continually restarted on exit until all regular containers have terminated. Once all regular containers have completed, all init containers with restartPolicy "Always" will be shut down. This lifecycle differs from normal init containers and is often referred to as a "sidecar" container. Although this init container still starts in the init container sequence, it does not wait for the container to complete before proceeding to the next init container. Instead, the next init container starts immediately after this init container is started, or after any startupProbe has successfully completed. |
| `securityContext` | `object` | SecurityContext defines the security options the container should be run with. If set, the fields of SecurityContext override the equivalent fields of PodSecurityContext. More info: <https://kubernetes.io/docs/tasks/configure-pod-container/security-context/> |
| `startupProbe` | `object` | StartupProbe indicates that the Pod has successfully initialized. If specified, no other probes are executed until this completes successfully. If this probe fails, the Pod will be restarted, just as if the livenessProbe failed. This can be used to provide different probe parameters at the beginning of a Pod’s lifecycle, when it might take a long time to load data or warm a cache, than during steady-state operation. This cannot be updated. More info: <https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes> |
| `stdin` | `boolean` | Whether this container should allocate a buffer for stdin in the container runtime. If this is not set, reads from stdin in the container will always result in EOF. Default is false. |
| `stdinOnce` | `boolean` | Whether the container runtime should close the stdin channel after it has been opened by a single attach. When stdin is true the stdin stream will remain open across multiple attach sessions. If stdinOnce is set to true, stdin is opened on container start, is empty until the first client attaches to stdin, and then remains open and accepts data until the client disconnects, at which time stdin is closed and remains closed until the container is restarted. If this flag is false, a container processes that reads from stdin will never receive an EOF. Default is false |
| `terminationMessagePath` | `string` | Optional: Path at which the file to which the container’s termination message will be written is mounted into the container’s filesystem. Message written is intended to be brief final status, such as an assertion failure message. Will be truncated by the node if greater than 4096 bytes. The total message length across all containers will be limited to 12kb. Defaults to /dev/termination-log. Cannot be updated. |
| `terminationMessagePolicy` | `string` | Indicate how the termination message should be populated. File will use the contents of terminationMessagePath to populate the container status message on both success and failure. FallbackToLogsOnError will use the last chunk of container log output if the termination message file is empty and the container exited with an error. The log output is limited to 2048 bytes or 80 lines, whichever is smaller. Defaults to File. Cannot be updated. |
| `tty` | `boolean` | Whether this container should allocate a TTY for itself, also requires 'stdin' to be true. Default is false. |
| `volumeDevices` | `array` | volumeDevices is the list of block devices to be used by the container. |
| `volumeDevices[]` | `object` | volumeDevice describes a mapping of a raw block device within a container. |
| `volumeMounts` | `array` | Pod volumes to mount into the container’s filesystem. Cannot be updated. |
| `volumeMounts[]` | `object` | VolumeMount describes a mounting of a Volume within a container. |
| `workingDir` | `string` | Container’s working directory. If not specified, the container runtime’s default will be used, which might be configured in the container image. Cannot be updated. |

## .spec.install.spec.deployments\[\].spec.template.spec.initContainers\[\].env

Description
List of environment variables to set in the container. Cannot be updated.

Type
`array`

## .spec.install.spec.deployments\[\].spec.template.spec.initContainers\[\].env\[\]

Description
EnvVar represents an environment variable present in a Container.

Type
`object`

Required
- `name`

| Property | Type | Description |
|----|----|----|
| `name` | `string` | Name of the environment variable. Must be a C_IDENTIFIER. |
| `value` | `string` | Variable references \$(VAR_NAME) are expanded using the previously defined environment variables in the container and any service environment variables. If a variable cannot be resolved, the reference in the input string will be unchanged. Double are reduced to a single \$, which allows for escaping the \$(VAR_NAME) syntax: i.e. "(VAR_NAME)" will produce the string literal "\$(VAR_NAME)". Escaped references will never be expanded, regardless of whether the variable exists or not. Defaults to "". |
| `valueFrom` | `object` | Source for the environment variable’s value. Cannot be used if value is not empty. |

## .spec.install.spec.deployments\[\].spec.template.spec.initContainers\[\].env\[\].valueFrom

Description
Source for the environment variable’s value. Cannot be used if value is not empty.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `configMapKeyRef` | `object` | Selects a key of a ConfigMap. |
| `fieldRef` | `object` | Selects a field of the pod: supports metadata.name, metadata.namespace, `metadata.labels['<KEY>']`, `metadata.annotations['<KEY>']`, spec.nodeName, spec.serviceAccountName, status.hostIP, status.podIP, status.podIPs. |
| `resourceFieldRef` | `object` | Selects a resource of the container: only resources limits and requests (limits.cpu, limits.memory, limits.ephemeral-storage, requests.cpu, requests.memory and requests.ephemeral-storage) are currently supported. |
| `secretKeyRef` | `object` | Selects a key of a secret in the pod’s namespace |

## .spec.install.spec.deployments\[\].spec.template.spec.initContainers\[\].env\[\].valueFrom.configMapKeyRef

Description
Selects a key of a ConfigMap.

Type
`object`

Required
- `key`

| Property | Type | Description |
|----|----|----|
| `key` | `string` | The key to select. |
| `name` | `string` | Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names> |
| `optional` | `boolean` | Specify whether the ConfigMap or its key must be defined |

## .spec.install.spec.deployments\[\].spec.template.spec.initContainers\[\].env\[\].valueFrom.fieldRef

Description
Selects a field of the pod: supports metadata.name, metadata.namespace, `metadata.labels['<KEY>']`, `metadata.annotations['<KEY>']`, spec.nodeName, spec.serviceAccountName, status.hostIP, status.podIP, status.podIPs.

Type
`object`

Required
- `fieldPath`

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | Version of the schema the FieldPath is written in terms of, defaults to "v1". |
| `fieldPath` | `string` | Path of the field to select in the specified API version. |

## .spec.install.spec.deployments\[\].spec.template.spec.initContainers\[\].env\[\].valueFrom.resourceFieldRef

Description
Selects a resource of the container: only resources limits and requests (limits.cpu, limits.memory, limits.ephemeral-storage, requests.cpu, requests.memory and requests.ephemeral-storage) are currently supported.

Type
`object`

Required
- `resource`

| Property | Type | Description |
|----|----|----|
| `containerName` | `string` | Container name: required for volumes, optional for env vars |
| `divisor` | `integer-or-string` | Specifies the output format of the exposed resources, defaults to "1" |
| `resource` | `string` | Required: resource to select |

## .spec.install.spec.deployments\[\].spec.template.spec.initContainers\[\].env\[\].valueFrom.secretKeyRef

Description
Selects a key of a secret in the pod’s namespace

Type
`object`

Required
- `key`

| Property | Type | Description |
|----|----|----|
| `key` | `string` | The key of the secret to select from. Must be a valid secret key. |
| `name` | `string` | Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names> |
| `optional` | `boolean` | Specify whether the Secret or its key must be defined |

## .spec.install.spec.deployments\[\].spec.template.spec.initContainers\[\].envFrom

Description
List of sources to populate environment variables in the container. The keys defined within a source must be a C_IDENTIFIER. All invalid keys will be reported as an event when the container is starting. When a key exists in multiple sources, the value associated with the last source will take precedence. Values defined by an Env with a duplicate key will take precedence. Cannot be updated.

Type
`array`

## .spec.install.spec.deployments\[\].spec.template.spec.initContainers\[\].envFrom\[\]

Description
EnvFromSource represents the source of a set of ConfigMaps or Secrets

Type
`object`

| Property | Type | Description |
|----|----|----|
| `configMapRef` | `object` | The ConfigMap to select from |
| `prefix` | `string` | Optional text to prepend to the name of each environment variable. Must be a C_IDENTIFIER. |
| `secretRef` | `object` | The Secret to select from |

## .spec.install.spec.deployments\[\].spec.template.spec.initContainers\[\].envFrom\[\].configMapRef

Description
The ConfigMap to select from

Type
`object`

| Property | Type | Description |
|----|----|----|
| `name` | `string` | Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names> |
| `optional` | `boolean` | Specify whether the ConfigMap must be defined |

## .spec.install.spec.deployments\[\].spec.template.spec.initContainers\[\].envFrom\[\].secretRef

Description
The Secret to select from

Type
`object`

| Property | Type | Description |
|----|----|----|
| `name` | `string` | Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names> |
| `optional` | `boolean` | Specify whether the Secret must be defined |

## .spec.install.spec.deployments\[\].spec.template.spec.initContainers\[\].lifecycle

Description
Actions that the management system should take in response to container lifecycle events. Cannot be updated.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `postStart` | `object` | PostStart is called immediately after a container is created. If the handler fails, the container is terminated and restarted according to its restart policy. Other management of the container blocks until the hook completes. More info: <https://kubernetes.io/docs/concepts/containers/container-lifecycle-hooks/#container-hooks> |
| `preStop` | `object` | PreStop is called immediately before a container is terminated due to an API request or management event such as liveness/startup probe failure, preemption, resource contention, etc. The handler is not called if the container crashes or exits. The Pod’s termination grace period countdown begins before the PreStop hook is executed. Regardless of the outcome of the handler, the container will eventually terminate within the Pod’s termination grace period (unless delayed by finalizers). Other management of the container blocks until the hook completes or until the termination grace period is reached. More info: <https://kubernetes.io/docs/concepts/containers/container-lifecycle-hooks/#container-hooks> |
| `stopSignal` | `string` | StopSignal defines which signal will be sent to a container when it is being stopped. If not specified, the default is defined by the container runtime in use. StopSignal can only be set for Pods with a non-empty .spec.os.name |

## .spec.install.spec.deployments\[\].spec.template.spec.initContainers\[\].lifecycle.postStart

Description
PostStart is called immediately after a container is created. If the handler fails, the container is terminated and restarted according to its restart policy. Other management of the container blocks until the hook completes. More info: <https://kubernetes.io/docs/concepts/containers/container-lifecycle-hooks/#container-hooks>

Type
`object`

| Property | Type | Description |
|----|----|----|
| `exec` | `object` | Exec specifies a command to execute in the container. |
| `httpGet` | `object` | HTTPGet specifies an HTTP GET request to perform. |
| `sleep` | `object` | Sleep represents a duration that the container should sleep. |
| `tcpSocket` | `object` | Deprecated. TCPSocket is NOT supported as a LifecycleHandler and kept for backward compatibility. There is no validation of this field and lifecycle hooks will fail at runtime when it is specified. |

## .spec.install.spec.deployments\[\].spec.template.spec.initContainers\[\].lifecycle.postStart.exec

Description
Exec specifies a command to execute in the container.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `command` | `array (string)` | Command is the command line to execute inside the container, the working directory for the command is root ('/') in the container’s filesystem. The command is simply exec’d, it is not run inside a shell, so traditional shell instructions ('\|', etc) won’t work. To use a shell, you need to explicitly call out to that shell. Exit status of 0 is treated as live/healthy and non-zero is unhealthy. |

## .spec.install.spec.deployments\[\].spec.template.spec.initContainers\[\].lifecycle.postStart.httpGet

Description
HTTPGet specifies an HTTP GET request to perform.

Type
`object`

Required
- `port`

| Property | Type | Description |
|----|----|----|
| `host` | `string` | Host name to connect to, defaults to the pod IP. You probably want to set "Host" in httpHeaders instead. |
| `httpHeaders` | `array` | Custom headers to set in the request. HTTP allows repeated headers. |
| `httpHeaders[]` | `object` | HTTPHeader describes a custom header to be used in HTTP probes |
| `path` | `string` | Path to access on the HTTP server. |
| `port` | `integer-or-string` | Name or number of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME. |
| `scheme` | `string` | Scheme to use for connecting to the host. Defaults to HTTP. |

## .spec.install.spec.deployments\[\].spec.template.spec.initContainers\[\].lifecycle.postStart.httpGet.httpHeaders

Description
Custom headers to set in the request. HTTP allows repeated headers.

Type
`array`

## .spec.install.spec.deployments\[\].spec.template.spec.initContainers\[\].lifecycle.postStart.httpGet.httpHeaders\[\]

Description
HTTPHeader describes a custom header to be used in HTTP probes

Type
`object`

Required
- `name`

- `value`

| Property | Type | Description |
|----|----|----|
| `name` | `string` | The header field name. This will be canonicalized upon output, so case-variant names will be understood as the same header. |
| `value` | `string` | The header field value |

## .spec.install.spec.deployments\[\].spec.template.spec.initContainers\[\].lifecycle.postStart.sleep

Description
Sleep represents a duration that the container should sleep.

Type
`object`

Required
- `seconds`

| Property  | Type      | Description                                |
|-----------|-----------|--------------------------------------------|
| `seconds` | `integer` | Seconds is the number of seconds to sleep. |

## .spec.install.spec.deployments\[\].spec.template.spec.initContainers\[\].lifecycle.postStart.tcpSocket

Description
Deprecated. TCPSocket is NOT supported as a LifecycleHandler and kept for backward compatibility. There is no validation of this field and lifecycle hooks will fail at runtime when it is specified.

Type
`object`

Required
- `port`

| Property | Type | Description |
|----|----|----|
| `host` | `string` | Optional: Host name to connect to, defaults to the pod IP. |
| `port` | `integer-or-string` | Number or name of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME. |

## .spec.install.spec.deployments\[\].spec.template.spec.initContainers\[\].lifecycle.preStop

Description
PreStop is called immediately before a container is terminated due to an API request or management event such as liveness/startup probe failure, preemption, resource contention, etc. The handler is not called if the container crashes or exits. The Pod’s termination grace period countdown begins before the PreStop hook is executed. Regardless of the outcome of the handler, the container will eventually terminate within the Pod’s termination grace period (unless delayed by finalizers). Other management of the container blocks until the hook completes or until the termination grace period is reached. More info: <https://kubernetes.io/docs/concepts/containers/container-lifecycle-hooks/#container-hooks>

Type
`object`

| Property | Type | Description |
|----|----|----|
| `exec` | `object` | Exec specifies a command to execute in the container. |
| `httpGet` | `object` | HTTPGet specifies an HTTP GET request to perform. |
| `sleep` | `object` | Sleep represents a duration that the container should sleep. |
| `tcpSocket` | `object` | Deprecated. TCPSocket is NOT supported as a LifecycleHandler and kept for backward compatibility. There is no validation of this field and lifecycle hooks will fail at runtime when it is specified. |

## .spec.install.spec.deployments\[\].spec.template.spec.initContainers\[\].lifecycle.preStop.exec

Description
Exec specifies a command to execute in the container.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `command` | `array (string)` | Command is the command line to execute inside the container, the working directory for the command is root ('/') in the container’s filesystem. The command is simply exec’d, it is not run inside a shell, so traditional shell instructions ('\|', etc) won’t work. To use a shell, you need to explicitly call out to that shell. Exit status of 0 is treated as live/healthy and non-zero is unhealthy. |

## .spec.install.spec.deployments\[\].spec.template.spec.initContainers\[\].lifecycle.preStop.httpGet

Description
HTTPGet specifies an HTTP GET request to perform.

Type
`object`

Required
- `port`

| Property | Type | Description |
|----|----|----|
| `host` | `string` | Host name to connect to, defaults to the pod IP. You probably want to set "Host" in httpHeaders instead. |
| `httpHeaders` | `array` | Custom headers to set in the request. HTTP allows repeated headers. |
| `httpHeaders[]` | `object` | HTTPHeader describes a custom header to be used in HTTP probes |
| `path` | `string` | Path to access on the HTTP server. |
| `port` | `integer-or-string` | Name or number of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME. |
| `scheme` | `string` | Scheme to use for connecting to the host. Defaults to HTTP. |

## .spec.install.spec.deployments\[\].spec.template.spec.initContainers\[\].lifecycle.preStop.httpGet.httpHeaders

Description
Custom headers to set in the request. HTTP allows repeated headers.

Type
`array`

## .spec.install.spec.deployments\[\].spec.template.spec.initContainers\[\].lifecycle.preStop.httpGet.httpHeaders\[\]

Description
HTTPHeader describes a custom header to be used in HTTP probes

Type
`object`

Required
- `name`

- `value`

| Property | Type | Description |
|----|----|----|
| `name` | `string` | The header field name. This will be canonicalized upon output, so case-variant names will be understood as the same header. |
| `value` | `string` | The header field value |

## .spec.install.spec.deployments\[\].spec.template.spec.initContainers\[\].lifecycle.preStop.sleep

Description
Sleep represents a duration that the container should sleep.

Type
`object`

Required
- `seconds`

| Property  | Type      | Description                                |
|-----------|-----------|--------------------------------------------|
| `seconds` | `integer` | Seconds is the number of seconds to sleep. |

## .spec.install.spec.deployments\[\].spec.template.spec.initContainers\[\].lifecycle.preStop.tcpSocket

Description
Deprecated. TCPSocket is NOT supported as a LifecycleHandler and kept for backward compatibility. There is no validation of this field and lifecycle hooks will fail at runtime when it is specified.

Type
`object`

Required
- `port`

| Property | Type | Description |
|----|----|----|
| `host` | `string` | Optional: Host name to connect to, defaults to the pod IP. |
| `port` | `integer-or-string` | Number or name of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME. |

## .spec.install.spec.deployments\[\].spec.template.spec.initContainers\[\].livenessProbe

Description
Periodic probe of container liveness. Container will be restarted if the probe fails. Cannot be updated. More info: <https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes>

Type
`object`

| Property | Type | Description |
|----|----|----|
| `exec` | `object` | Exec specifies a command to execute in the container. |
| `failureThreshold` | `integer` | Minimum consecutive failures for the probe to be considered failed after having succeeded. Defaults to 3. Minimum value is 1. |
| `grpc` | `object` | GRPC specifies a GRPC HealthCheckRequest. |
| `httpGet` | `object` | HTTPGet specifies an HTTP GET request to perform. |
| `initialDelaySeconds` | `integer` | Number of seconds after the container has started before liveness probes are initiated. More info: <https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes> |
| `periodSeconds` | `integer` | How often (in seconds) to perform the probe. Default to 10 seconds. Minimum value is 1. |
| `successThreshold` | `integer` | Minimum consecutive successes for the probe to be considered successful after having failed. Defaults to 1. Must be 1 for liveness and startup. Minimum value is 1. |
| `tcpSocket` | `object` | TCPSocket specifies a connection to a TCP port. |
| `terminationGracePeriodSeconds` | `integer` | Optional duration in seconds the pod needs to terminate gracefully upon probe failure. The grace period is the duration in seconds after the processes running in the pod are sent a termination signal and the time when the processes are forcibly halted with a kill signal. Set this value longer than the expected cleanup time for your process. If this value is nil, the pod’s terminationGracePeriodSeconds will be used. Otherwise, this value overrides the value provided by the pod spec. Value must be non-negative integer. The value zero indicates stop immediately via the kill signal (no opportunity to shut down). This is a beta field and requires enabling ProbeTerminationGracePeriod feature gate. Minimum value is 1. spec.terminationGracePeriodSeconds is used if unset. |
| `timeoutSeconds` | `integer` | Number of seconds after which the probe times out. Defaults to 1 second. Minimum value is 1. More info: <https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes> |

## .spec.install.spec.deployments\[\].spec.template.spec.initContainers\[\].livenessProbe.exec

Description
Exec specifies a command to execute in the container.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `command` | `array (string)` | Command is the command line to execute inside the container, the working directory for the command is root ('/') in the container’s filesystem. The command is simply exec’d, it is not run inside a shell, so traditional shell instructions ('\|', etc) won’t work. To use a shell, you need to explicitly call out to that shell. Exit status of 0 is treated as live/healthy and non-zero is unhealthy. |

## .spec.install.spec.deployments\[\].spec.template.spec.initContainers\[\].livenessProbe.grpc

Description
GRPC specifies a GRPC HealthCheckRequest.

Type
`object`

Required
- `port`

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
<td style="text-align: left;"><p><code>port</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p>Port number of the gRPC service. Number must be in the range 1 to 65535.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>service</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Service is the name of the service to place in the gRPC HealthCheckRequest (see <a href="https://github.com/grpc/grpc/blob/master/doc/health-checking.md">https://github.com/grpc/grpc/blob/master/doc/health-checking.md</a>).</p>
<p>If this is not specified, the default behavior is defined by gRPC.</p></td>
</tr>
</tbody>
</table>

## .spec.install.spec.deployments\[\].spec.template.spec.initContainers\[\].livenessProbe.httpGet

Description
HTTPGet specifies an HTTP GET request to perform.

Type
`object`

Required
- `port`

| Property | Type | Description |
|----|----|----|
| `host` | `string` | Host name to connect to, defaults to the pod IP. You probably want to set "Host" in httpHeaders instead. |
| `httpHeaders` | `array` | Custom headers to set in the request. HTTP allows repeated headers. |
| `httpHeaders[]` | `object` | HTTPHeader describes a custom header to be used in HTTP probes |
| `path` | `string` | Path to access on the HTTP server. |
| `port` | `integer-or-string` | Name or number of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME. |
| `scheme` | `string` | Scheme to use for connecting to the host. Defaults to HTTP. |

## .spec.install.spec.deployments\[\].spec.template.spec.initContainers\[\].livenessProbe.httpGet.httpHeaders

Description
Custom headers to set in the request. HTTP allows repeated headers.

Type
`array`

## .spec.install.spec.deployments\[\].spec.template.spec.initContainers\[\].livenessProbe.httpGet.httpHeaders\[\]

Description
HTTPHeader describes a custom header to be used in HTTP probes

Type
`object`

Required
- `name`

- `value`

| Property | Type | Description |
|----|----|----|
| `name` | `string` | The header field name. This will be canonicalized upon output, so case-variant names will be understood as the same header. |
| `value` | `string` | The header field value |

## .spec.install.spec.deployments\[\].spec.template.spec.initContainers\[\].livenessProbe.tcpSocket

Description
TCPSocket specifies a connection to a TCP port.

Type
`object`

Required
- `port`

| Property | Type | Description |
|----|----|----|
| `host` | `string` | Optional: Host name to connect to, defaults to the pod IP. |
| `port` | `integer-or-string` | Number or name of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME. |

## .spec.install.spec.deployments\[\].spec.template.spec.initContainers\[\].ports

Description
List of ports to expose from the container. Not specifying a port here DOES NOT prevent that port from being exposed. Any port which is listening on the default "0.0.0.0" address inside a container will be accessible from the network. Modifying this array with strategic merge patch may corrupt the data. For more information See <https://github.com/kubernetes/kubernetes/issues/108255>. Cannot be updated.

Type
`array`

## .spec.install.spec.deployments\[\].spec.template.spec.initContainers\[\].ports\[\]

Description
ContainerPort represents a network port in a single container.

Type
`object`

Required
- `containerPort`

| Property | Type | Description |
|----|----|----|
| `containerPort` | `integer` | Number of port to expose on the pod’s IP address. This must be a valid port number, 0 \< x \< 65536. |
| `hostIP` | `string` | What host IP to bind the external port to. |
| `hostPort` | `integer` | Number of port to expose on the host. If specified, this must be a valid port number, 0 \< x \< 65536. If HostNetwork is specified, this must match ContainerPort. Most containers do not need this. |
| `name` | `string` | If specified, this must be an IANA_SVC_NAME and unique within the pod. Each named port in a pod must have a unique name. Name for the port that can be referred to by services. |
| `protocol` | `string` | Protocol for port. Must be UDP, TCP, or SCTP. Defaults to "TCP". |

## .spec.install.spec.deployments\[\].spec.template.spec.initContainers\[\].readinessProbe

Description
Periodic probe of container service readiness. Container will be removed from service endpoints if the probe fails. Cannot be updated. More info: <https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes>

Type
`object`

| Property | Type | Description |
|----|----|----|
| `exec` | `object` | Exec specifies a command to execute in the container. |
| `failureThreshold` | `integer` | Minimum consecutive failures for the probe to be considered failed after having succeeded. Defaults to 3. Minimum value is 1. |
| `grpc` | `object` | GRPC specifies a GRPC HealthCheckRequest. |
| `httpGet` | `object` | HTTPGet specifies an HTTP GET request to perform. |
| `initialDelaySeconds` | `integer` | Number of seconds after the container has started before liveness probes are initiated. More info: <https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes> |
| `periodSeconds` | `integer` | How often (in seconds) to perform the probe. Default to 10 seconds. Minimum value is 1. |
| `successThreshold` | `integer` | Minimum consecutive successes for the probe to be considered successful after having failed. Defaults to 1. Must be 1 for liveness and startup. Minimum value is 1. |
| `tcpSocket` | `object` | TCPSocket specifies a connection to a TCP port. |
| `terminationGracePeriodSeconds` | `integer` | Optional duration in seconds the pod needs to terminate gracefully upon probe failure. The grace period is the duration in seconds after the processes running in the pod are sent a termination signal and the time when the processes are forcibly halted with a kill signal. Set this value longer than the expected cleanup time for your process. If this value is nil, the pod’s terminationGracePeriodSeconds will be used. Otherwise, this value overrides the value provided by the pod spec. Value must be non-negative integer. The value zero indicates stop immediately via the kill signal (no opportunity to shut down). This is a beta field and requires enabling ProbeTerminationGracePeriod feature gate. Minimum value is 1. spec.terminationGracePeriodSeconds is used if unset. |
| `timeoutSeconds` | `integer` | Number of seconds after which the probe times out. Defaults to 1 second. Minimum value is 1. More info: <https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes> |

## .spec.install.spec.deployments\[\].spec.template.spec.initContainers\[\].readinessProbe.exec

Description
Exec specifies a command to execute in the container.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `command` | `array (string)` | Command is the command line to execute inside the container, the working directory for the command is root ('/') in the container’s filesystem. The command is simply exec’d, it is not run inside a shell, so traditional shell instructions ('\|', etc) won’t work. To use a shell, you need to explicitly call out to that shell. Exit status of 0 is treated as live/healthy and non-zero is unhealthy. |

## .spec.install.spec.deployments\[\].spec.template.spec.initContainers\[\].readinessProbe.grpc

Description
GRPC specifies a GRPC HealthCheckRequest.

Type
`object`

Required
- `port`

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
<td style="text-align: left;"><p><code>port</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p>Port number of the gRPC service. Number must be in the range 1 to 65535.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>service</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Service is the name of the service to place in the gRPC HealthCheckRequest (see <a href="https://github.com/grpc/grpc/blob/master/doc/health-checking.md">https://github.com/grpc/grpc/blob/master/doc/health-checking.md</a>).</p>
<p>If this is not specified, the default behavior is defined by gRPC.</p></td>
</tr>
</tbody>
</table>

## .spec.install.spec.deployments\[\].spec.template.spec.initContainers\[\].readinessProbe.httpGet

Description
HTTPGet specifies an HTTP GET request to perform.

Type
`object`

Required
- `port`

| Property | Type | Description |
|----|----|----|
| `host` | `string` | Host name to connect to, defaults to the pod IP. You probably want to set "Host" in httpHeaders instead. |
| `httpHeaders` | `array` | Custom headers to set in the request. HTTP allows repeated headers. |
| `httpHeaders[]` | `object` | HTTPHeader describes a custom header to be used in HTTP probes |
| `path` | `string` | Path to access on the HTTP server. |
| `port` | `integer-or-string` | Name or number of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME. |
| `scheme` | `string` | Scheme to use for connecting to the host. Defaults to HTTP. |

## .spec.install.spec.deployments\[\].spec.template.spec.initContainers\[\].readinessProbe.httpGet.httpHeaders

Description
Custom headers to set in the request. HTTP allows repeated headers.

Type
`array`

## .spec.install.spec.deployments\[\].spec.template.spec.initContainers\[\].readinessProbe.httpGet.httpHeaders\[\]

Description
HTTPHeader describes a custom header to be used in HTTP probes

Type
`object`

Required
- `name`

- `value`

| Property | Type | Description |
|----|----|----|
| `name` | `string` | The header field name. This will be canonicalized upon output, so case-variant names will be understood as the same header. |
| `value` | `string` | The header field value |

## .spec.install.spec.deployments\[\].spec.template.spec.initContainers\[\].readinessProbe.tcpSocket

Description
TCPSocket specifies a connection to a TCP port.

Type
`object`

Required
- `port`

| Property | Type | Description |
|----|----|----|
| `host` | `string` | Optional: Host name to connect to, defaults to the pod IP. |
| `port` | `integer-or-string` | Number or name of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME. |

## .spec.install.spec.deployments\[\].spec.template.spec.initContainers\[\].resizePolicy

Description
Resources resize policy for the container.

Type
`array`

## .spec.install.spec.deployments\[\].spec.template.spec.initContainers\[\].resizePolicy\[\]

Description
ContainerResizePolicy represents resource resize policy for the container.

Type
`object`

Required
- `resourceName`

- `restartPolicy`

| Property | Type | Description |
|----|----|----|
| `resourceName` | `string` | Name of the resource to which this resource resize policy applies. Supported values: cpu, memory. |
| `restartPolicy` | `string` | Restart policy to apply when specified resource is resized. If not specified, it defaults to NotRequired. |

## .spec.install.spec.deployments\[\].spec.template.spec.initContainers\[\].resources

Description
Compute Resources required by this container. Cannot be updated. More info: <https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/>

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
<td style="text-align: left;"><p><code>claims</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>Claims lists the names of resources, defined in spec.resourceClaims, that are used by this container.</p>
<p>This is an alpha field and requires enabling the DynamicResourceAllocation feature gate.</p>
<p>This field is immutable. It can only be set for containers.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>claims[]</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>ResourceClaim references one entry in PodSpec.ResourceClaims.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>limits</code></p></td>
<td style="text-align: left;"><p><code>integer-or-string</code></p></td>
<td style="text-align: left;"><p>Limits describes the maximum amount of compute resources allowed. More info: <a href="https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/">https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>requests</code></p></td>
<td style="text-align: left;"><p><code>integer-or-string</code></p></td>
<td style="text-align: left;"><p>Requests describes the minimum amount of compute resources required. If Requests is omitted for a container, it defaults to Limits if that is explicitly specified, otherwise to an implementation-defined value. Requests cannot exceed Limits. More info: <a href="https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/">https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/</a></p></td>
</tr>
</tbody>
</table>

## .spec.install.spec.deployments\[\].spec.template.spec.initContainers\[\].resources.claims

Description
Claims lists the names of resources, defined in spec.resourceClaims, that are used by this container.

This is an alpha field and requires enabling the DynamicResourceAllocation feature gate.

This field is immutable. It can only be set for containers.

Type
`array`

## .spec.install.spec.deployments\[\].spec.template.spec.initContainers\[\].resources.claims\[\]

Description
ResourceClaim references one entry in PodSpec.ResourceClaims.

Type
`object`

Required
- `name`

| Property | Type | Description |
|----|----|----|
| `name` | `string` | Name must match the name of one entry in pod.spec.resourceClaims of the Pod where this field is used. It makes that resource available inside a container. |
| `request` | `string` | Request is the name chosen for a request in the referenced claim. If empty, everything from the claim is made available, otherwise only the result of this request. |

## .spec.install.spec.deployments\[\].spec.template.spec.initContainers\[\].securityContext

Description
SecurityContext defines the security options the container should be run with. If set, the fields of SecurityContext override the equivalent fields of PodSecurityContext. More info: <https://kubernetes.io/docs/tasks/configure-pod-container/security-context/>

Type
`object`

| Property | Type | Description |
|----|----|----|
| `allowPrivilegeEscalation` | `boolean` | AllowPrivilegeEscalation controls whether a process can gain more privileges than its parent process. This bool directly controls if the no_new_privs flag will be set on the container process. AllowPrivilegeEscalation is true always when the container is: 1) run as Privileged 2) has CAP_SYS_ADMIN Note that this field cannot be set when spec.os.name is windows. |
| `appArmorProfile` | `object` | appArmorProfile is the AppArmor options to use by this container. If set, this profile overrides the pod’s appArmorProfile. Note that this field cannot be set when spec.os.name is windows. |
| `capabilities` | `object` | The capabilities to add/drop when running containers. Defaults to the default set of capabilities granted by the container runtime. Note that this field cannot be set when spec.os.name is windows. |
| `privileged` | `boolean` | Run container in privileged mode. Processes in privileged containers are essentially equivalent to root on the host. Defaults to false. Note that this field cannot be set when spec.os.name is windows. |
| `procMount` | `string` | procMount denotes the type of proc mount to use for the containers. The default value is Default which uses the container runtime defaults for readonly paths and masked paths. This requires the ProcMountType feature flag to be enabled. Note that this field cannot be set when spec.os.name is windows. |
| `readOnlyRootFilesystem` | `boolean` | Whether this container has a read-only root filesystem. Default is false. Note that this field cannot be set when spec.os.name is windows. |
| `runAsGroup` | `integer` | The GID to run the entrypoint of the container process. Uses runtime default if unset. May also be set in PodSecurityContext. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence. Note that this field cannot be set when spec.os.name is windows. |
| `runAsNonRoot` | `boolean` | Indicates that the container must run as a non-root user. If true, the Kubelet will validate the image at runtime to ensure that it does not run as UID 0 (root) and fail to start the container if it does. If unset or false, no such validation will be performed. May also be set in PodSecurityContext. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence. |
| `runAsUser` | `integer` | The UID to run the entrypoint of the container process. Defaults to user specified in image metadata if unspecified. May also be set in PodSecurityContext. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence. Note that this field cannot be set when spec.os.name is windows. |
| `seLinuxOptions` | `object` | The SELinux context to be applied to the container. If unspecified, the container runtime will allocate a random SELinux context for each container. May also be set in PodSecurityContext. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence. Note that this field cannot be set when spec.os.name is windows. |
| `seccompProfile` | `object` | The seccomp options to use by this container. If seccomp options are provided at both the pod & container level, the container options override the pod options. Note that this field cannot be set when spec.os.name is windows. |
| `windowsOptions` | `object` | The Windows specific settings applied to all containers. If unspecified, the options from the PodSecurityContext will be used. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence. Note that this field cannot be set when spec.os.name is linux. |

## .spec.install.spec.deployments\[\].spec.template.spec.initContainers\[\].securityContext.appArmorProfile

Description
appArmorProfile is the AppArmor options to use by this container. If set, this profile overrides the pod’s appArmorProfile. Note that this field cannot be set when spec.os.name is windows.

Type
`object`

Required
- `type`

| Property | Type | Description |
|----|----|----|
| `localhostProfile` | `string` | localhostProfile indicates a profile loaded on the node that should be used. The profile must be preconfigured on the node to work. Must match the loaded name of the profile. Must be set if and only if type is "Localhost". |
| `type` | `string` | type indicates which kind of AppArmor profile will be applied. Valid options are: Localhost - a profile pre-loaded on the node. RuntimeDefault - the container runtime’s default profile. Unconfined - no AppArmor enforcement. |

## .spec.install.spec.deployments\[\].spec.template.spec.initContainers\[\].securityContext.capabilities

Description
The capabilities to add/drop when running containers. Defaults to the default set of capabilities granted by the container runtime. Note that this field cannot be set when spec.os.name is windows.

Type
`object`

| Property | Type             | Description          |
|----------|------------------|----------------------|
| `add`    | `array (string)` | Added capabilities   |
| `drop`   | `array (string)` | Removed capabilities |

## .spec.install.spec.deployments\[\].spec.template.spec.initContainers\[\].securityContext.seLinuxOptions

Description
The SELinux context to be applied to the container. If unspecified, the container runtime will allocate a random SELinux context for each container. May also be set in PodSecurityContext. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence. Note that this field cannot be set when spec.os.name is windows.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `level` | `string` | Level is SELinux level label that applies to the container. |
| `role` | `string` | Role is a SELinux role label that applies to the container. |
| `type` | `string` | Type is a SELinux type label that applies to the container. |
| `user` | `string` | User is a SELinux user label that applies to the container. |

## .spec.install.spec.deployments\[\].spec.template.spec.initContainers\[\].securityContext.seccompProfile

Description
The seccomp options to use by this container. If seccomp options are provided at both the pod & container level, the container options override the pod options. Note that this field cannot be set when spec.os.name is windows.

Type
`object`

Required
- `type`

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
<td style="text-align: left;"><p><code>localhostProfile</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>localhostProfile indicates a profile defined in a file on the node should be used. The profile must be preconfigured on the node to work. Must be a descending path, relative to the kubelet’s configured seccomp profile location. Must be set if type is "Localhost". Must NOT be set for any other type.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>type</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>type indicates which kind of seccomp profile will be applied. Valid options are:</p>
<p>Localhost - a profile defined in a file on the node should be used. RuntimeDefault - the container runtime default profile should be used. Unconfined - no profile should be applied.</p></td>
</tr>
</tbody>
</table>

## .spec.install.spec.deployments\[\].spec.template.spec.initContainers\[\].securityContext.windowsOptions

Description
The Windows specific settings applied to all containers. If unspecified, the options from the PodSecurityContext will be used. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence. Note that this field cannot be set when spec.os.name is linux.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `gmsaCredentialSpec` | `string` | GMSACredentialSpec is where the GMSA admission webhook (<https://github.com/kubernetes-sigs/windows-gmsa>) inlines the contents of the GMSA credential spec named by the GMSACredentialSpecName field. |
| `gmsaCredentialSpecName` | `string` | GMSACredentialSpecName is the name of the GMSA credential spec to use. |
| `hostProcess` | `boolean` | HostProcess determines if a container should be run as a 'Host Process' container. All of a Pod’s containers must have the same effective HostProcess value (it is not allowed to have a mix of HostProcess containers and non-HostProcess containers). In addition, if HostProcess is true then HostNetwork must also be set to true. |
| `runAsUserName` | `string` | The UserName in Windows to run the entrypoint of the container process. Defaults to the user specified in image metadata if unspecified. May also be set in PodSecurityContext. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence. |

## .spec.install.spec.deployments\[\].spec.template.spec.initContainers\[\].startupProbe

Description
StartupProbe indicates that the Pod has successfully initialized. If specified, no other probes are executed until this completes successfully. If this probe fails, the Pod will be restarted, just as if the livenessProbe failed. This can be used to provide different probe parameters at the beginning of a Pod’s lifecycle, when it might take a long time to load data or warm a cache, than during steady-state operation. This cannot be updated. More info: <https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes>

Type
`object`

| Property | Type | Description |
|----|----|----|
| `exec` | `object` | Exec specifies a command to execute in the container. |
| `failureThreshold` | `integer` | Minimum consecutive failures for the probe to be considered failed after having succeeded. Defaults to 3. Minimum value is 1. |
| `grpc` | `object` | GRPC specifies a GRPC HealthCheckRequest. |
| `httpGet` | `object` | HTTPGet specifies an HTTP GET request to perform. |
| `initialDelaySeconds` | `integer` | Number of seconds after the container has started before liveness probes are initiated. More info: <https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes> |
| `periodSeconds` | `integer` | How often (in seconds) to perform the probe. Default to 10 seconds. Minimum value is 1. |
| `successThreshold` | `integer` | Minimum consecutive successes for the probe to be considered successful after having failed. Defaults to 1. Must be 1 for liveness and startup. Minimum value is 1. |
| `tcpSocket` | `object` | TCPSocket specifies a connection to a TCP port. |
| `terminationGracePeriodSeconds` | `integer` | Optional duration in seconds the pod needs to terminate gracefully upon probe failure. The grace period is the duration in seconds after the processes running in the pod are sent a termination signal and the time when the processes are forcibly halted with a kill signal. Set this value longer than the expected cleanup time for your process. If this value is nil, the pod’s terminationGracePeriodSeconds will be used. Otherwise, this value overrides the value provided by the pod spec. Value must be non-negative integer. The value zero indicates stop immediately via the kill signal (no opportunity to shut down). This is a beta field and requires enabling ProbeTerminationGracePeriod feature gate. Minimum value is 1. spec.terminationGracePeriodSeconds is used if unset. |
| `timeoutSeconds` | `integer` | Number of seconds after which the probe times out. Defaults to 1 second. Minimum value is 1. More info: <https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes> |

## .spec.install.spec.deployments\[\].spec.template.spec.initContainers\[\].startupProbe.exec

Description
Exec specifies a command to execute in the container.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `command` | `array (string)` | Command is the command line to execute inside the container, the working directory for the command is root ('/') in the container’s filesystem. The command is simply exec’d, it is not run inside a shell, so traditional shell instructions ('\|', etc) won’t work. To use a shell, you need to explicitly call out to that shell. Exit status of 0 is treated as live/healthy and non-zero is unhealthy. |

## .spec.install.spec.deployments\[\].spec.template.spec.initContainers\[\].startupProbe.grpc

Description
GRPC specifies a GRPC HealthCheckRequest.

Type
`object`

Required
- `port`

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
<td style="text-align: left;"><p><code>port</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p>Port number of the gRPC service. Number must be in the range 1 to 65535.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>service</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Service is the name of the service to place in the gRPC HealthCheckRequest (see <a href="https://github.com/grpc/grpc/blob/master/doc/health-checking.md">https://github.com/grpc/grpc/blob/master/doc/health-checking.md</a>).</p>
<p>If this is not specified, the default behavior is defined by gRPC.</p></td>
</tr>
</tbody>
</table>

## .spec.install.spec.deployments\[\].spec.template.spec.initContainers\[\].startupProbe.httpGet

Description
HTTPGet specifies an HTTP GET request to perform.

Type
`object`

Required
- `port`

| Property | Type | Description |
|----|----|----|
| `host` | `string` | Host name to connect to, defaults to the pod IP. You probably want to set "Host" in httpHeaders instead. |
| `httpHeaders` | `array` | Custom headers to set in the request. HTTP allows repeated headers. |
| `httpHeaders[]` | `object` | HTTPHeader describes a custom header to be used in HTTP probes |
| `path` | `string` | Path to access on the HTTP server. |
| `port` | `integer-or-string` | Name or number of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME. |
| `scheme` | `string` | Scheme to use for connecting to the host. Defaults to HTTP. |

## .spec.install.spec.deployments\[\].spec.template.spec.initContainers\[\].startupProbe.httpGet.httpHeaders

Description
Custom headers to set in the request. HTTP allows repeated headers.

Type
`array`

## .spec.install.spec.deployments\[\].spec.template.spec.initContainers\[\].startupProbe.httpGet.httpHeaders\[\]

Description
HTTPHeader describes a custom header to be used in HTTP probes

Type
`object`

Required
- `name`

- `value`

| Property | Type | Description |
|----|----|----|
| `name` | `string` | The header field name. This will be canonicalized upon output, so case-variant names will be understood as the same header. |
| `value` | `string` | The header field value |

## .spec.install.spec.deployments\[\].spec.template.spec.initContainers\[\].startupProbe.tcpSocket

Description
TCPSocket specifies a connection to a TCP port.

Type
`object`

Required
- `port`

| Property | Type | Description |
|----|----|----|
| `host` | `string` | Optional: Host name to connect to, defaults to the pod IP. |
| `port` | `integer-or-string` | Number or name of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME. |

## .spec.install.spec.deployments\[\].spec.template.spec.initContainers\[\].volumeDevices

Description
volumeDevices is the list of block devices to be used by the container.

Type
`array`

## .spec.install.spec.deployments\[\].spec.template.spec.initContainers\[\].volumeDevices\[\]

Description
volumeDevice describes a mapping of a raw block device within a container.

Type
`object`

Required
- `devicePath`

- `name`

| Property | Type | Description |
|----|----|----|
| `devicePath` | `string` | devicePath is the path inside of the container that the device will be mapped to. |
| `name` | `string` | name must match the name of a persistentVolumeClaim in the pod |

## .spec.install.spec.deployments\[\].spec.template.spec.initContainers\[\].volumeMounts

Description
Pod volumes to mount into the container’s filesystem. Cannot be updated.

Type
`array`

## .spec.install.spec.deployments\[\].spec.template.spec.initContainers\[\].volumeMounts\[\]

Description
VolumeMount describes a mounting of a Volume within a container.

Type
`object`

Required
- `mountPath`

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
<td style="text-align: left;"><p><code>mountPath</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Path within the container at which the volume should be mounted. Must not contain ':'.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>mountPropagation</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>mountPropagation determines how mounts are propagated from the host to container and the other way around. When not set, MountPropagationNone is used. This field is beta in 1.10. When RecursiveReadOnly is set to IfPossible or to Enabled, MountPropagation must be None or unspecified (which defaults to None).</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>name</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>This must match the Name of a Volume.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>readOnly</code></p></td>
<td style="text-align: left;"><p><code>boolean</code></p></td>
<td style="text-align: left;"><p>Mounted read-only if true, read-write otherwise (false or unspecified). Defaults to false.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>recursiveReadOnly</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>RecursiveReadOnly specifies whether read-only mounts should be handled recursively.</p>
<p>If ReadOnly is false, this field has no meaning and must be unspecified.</p>
<p>If ReadOnly is true, and this field is set to Disabled, the mount is not made recursively read-only. If this field is set to IfPossible, the mount is made recursively read-only, if it is supported by the container runtime. If this field is set to Enabled, the mount is made recursively read-only if it is supported by the container runtime, otherwise the pod will not be started and an error will be generated to indicate the reason.</p>
<p>If this field is set to IfPossible or Enabled, MountPropagation must be set to None (or be unspecified, which defaults to None).</p>
<p>If this field is not specified, it is treated as an equivalent of Disabled.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>subPath</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Path within the volume from which the container’s volume should be mounted. Defaults to "" (volume’s root).</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>subPathExpr</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Expanded path within the volume from which the container’s volume should be mounted. Behaves similarly to SubPath but environment variable references $(VAR_NAME) are expanded using the container’s environment. Defaults to "" (volume’s root). SubPathExpr and SubPath are mutually exclusive.</p></td>
</tr>
</tbody>
</table>

## .spec.install.spec.deployments\[\].spec.template.spec.os

Description
Specifies the OS of the containers in the pod. Some pod and container fields are restricted if this is set.

If the OS field is set to linux, the following fields must be unset: -securityContext.windowsOptions

If the OS field is set to windows, following fields must be unset: - spec.hostPID - spec.hostIPC - spec.hostUsers - spec.securityContext.appArmorProfile - spec.securityContext.seLinuxOptions - spec.securityContext.seccompProfile - spec.securityContext.fsGroup - spec.securityContext.fsGroupChangePolicy - spec.securityContext.sysctls - spec.shareProcessNamespace - spec.securityContext.runAsUser - spec.securityContext.runAsGroup - spec.securityContext.supplementalGroups - spec.securityContext.supplementalGroupsPolicy - spec.containers\[**\].securityContext.appArmorProfile - spec.containers\[**\].securityContext.seLinuxOptions - spec.containers\[**\].securityContext.seccompProfile - spec.containers\[**\].securityContext.capabilities - spec.containers\[**\].securityContext.readOnlyRootFilesystem - spec.containers\[**\].securityContext.privileged - spec.containers\[**\].securityContext.allowPrivilegeEscalation - spec.containers\[**\].securityContext.procMount - spec.containers\[**\].securityContext.runAsUser - spec.containers\[**\].securityContext.runAsGroup

Type
`object`

Required
- `name`

| Property | Type | Description |
|----|----|----|
| `name` | `string` | Name is the name of the operating system. The currently supported values are linux and windows. Additional value may be defined in future and can be one of: <https://github.com/opencontainers/runtime-spec/blob/master/config.md#platform-specific-configuration> Clients should expect to handle additional values and treat unrecognized values in this field as os: null |

## .spec.install.spec.deployments\[\].spec.template.spec.readinessGates

Description
If specified, all readiness gates will be evaluated for pod readiness. A pod is ready when all its containers are ready AND all conditions specified in the readiness gates have status equal to "True" More info: <https://git.k8s.io/enhancements/keps/sig-network/580-pod-readiness-gates>

Type
`array`

## .spec.install.spec.deployments\[\].spec.template.spec.readinessGates\[\]

Description
PodReadinessGate contains the reference to a pod condition

Type
`object`

Required
- `conditionType`

| Property | Type | Description |
|----|----|----|
| `conditionType` | `string` | ConditionType refers to a condition in the pod’s condition list with matching type. |

## .spec.install.spec.deployments\[\].spec.template.spec.resourceClaims

Description
ResourceClaims defines which ResourceClaims must be allocated and reserved before the Pod is allowed to start. The resources will be made available to those containers which consume them by name.

This is an alpha field and requires enabling the DynamicResourceAllocation feature gate.

This field is immutable.

Type
`array`

## .spec.install.spec.deployments\[\].spec.template.spec.resourceClaims\[\]

Description
PodResourceClaim references exactly one ResourceClaim, either directly or by naming a ResourceClaimTemplate which is then turned into a ResourceClaim for the pod.

It adds a name to it that uniquely identifies the ResourceClaim inside the Pod. Containers that need access to the ResourceClaim reference it with this name.

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
<td style="text-align: left;"><p><code>name</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Name uniquely identifies this resource claim inside the pod. This must be a DNS_LABEL.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>resourceClaimName</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>ResourceClaimName is the name of a ResourceClaim object in the same namespace as this pod.</p>
<p>Exactly one of ResourceClaimName and ResourceClaimTemplateName must be set.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>resourceClaimTemplateName</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>ResourceClaimTemplateName is the name of a ResourceClaimTemplate object in the same namespace as this pod.</p>
<p>The template will be used to create a new ResourceClaim, which will be bound to this pod. When this pod is deleted, the ResourceClaim will also be deleted. The pod name and resource name, along with a generated component, will be used to form a unique name for the ResourceClaim, which will be recorded in pod.status.resourceClaimStatuses.</p>
<p>This field is immutable and no changes will be made to the corresponding ResourceClaim by the control plane after creating the ResourceClaim.</p>
<p>Exactly one of ResourceClaimName and ResourceClaimTemplateName must be set.</p></td>
</tr>
</tbody>
</table>

## .spec.install.spec.deployments\[\].spec.template.spec.resources

Description
Resources is the total amount of CPU and Memory resources required by all containers in the pod. It supports specifying Requests and Limits for "cpu" and "memory" resource names only. ResourceClaims are not supported.

This field enables fine-grained control over resource allocation for the entire pod, allowing resource sharing among containers in a pod.

This is an alpha field and requires enabling the PodLevelResources feature gate.

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
<td style="text-align: left;"><p><code>claims</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>Claims lists the names of resources, defined in spec.resourceClaims, that are used by this container.</p>
<p>This is an alpha field and requires enabling the DynamicResourceAllocation feature gate.</p>
<p>This field is immutable. It can only be set for containers.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>claims[]</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>ResourceClaim references one entry in PodSpec.ResourceClaims.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>limits</code></p></td>
<td style="text-align: left;"><p><code>integer-or-string</code></p></td>
<td style="text-align: left;"><p>Limits describes the maximum amount of compute resources allowed. More info: <a href="https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/">https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>requests</code></p></td>
<td style="text-align: left;"><p><code>integer-or-string</code></p></td>
<td style="text-align: left;"><p>Requests describes the minimum amount of compute resources required. If Requests is omitted for a container, it defaults to Limits if that is explicitly specified, otherwise to an implementation-defined value. Requests cannot exceed Limits. More info: <a href="https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/">https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/</a></p></td>
</tr>
</tbody>
</table>

## .spec.install.spec.deployments\[\].spec.template.spec.resources.claims

Description
Claims lists the names of resources, defined in spec.resourceClaims, that are used by this container.

This is an alpha field and requires enabling the DynamicResourceAllocation feature gate.

This field is immutable. It can only be set for containers.

Type
`array`

## .spec.install.spec.deployments\[\].spec.template.spec.resources.claims\[\]

Description
ResourceClaim references one entry in PodSpec.ResourceClaims.

Type
`object`

Required
- `name`

| Property | Type | Description |
|----|----|----|
| `name` | `string` | Name must match the name of one entry in pod.spec.resourceClaims of the Pod where this field is used. It makes that resource available inside a container. |
| `request` | `string` | Request is the name chosen for a request in the referenced claim. If empty, everything from the claim is made available, otherwise only the result of this request. |

## .spec.install.spec.deployments\[\].spec.template.spec.schedulingGates

Description
SchedulingGates is an opaque list of values that if specified will block scheduling the pod. If schedulingGates is not empty, the pod will stay in the SchedulingGated state and the scheduler will not attempt to schedule the pod.

SchedulingGates can only be set at pod creation time, and be removed only afterwards.

Type
`array`

## .spec.install.spec.deployments\[\].spec.template.spec.schedulingGates\[\]

Description
PodSchedulingGate is associated to a Pod to guard its scheduling.

Type
`object`

Required
- `name`

| Property | Type | Description |
|----|----|----|
| `name` | `string` | Name of the scheduling gate. Each scheduling gate must have a unique name field. |

## .spec.install.spec.deployments\[\].spec.template.spec.securityContext

Description
SecurityContext holds pod-level security attributes and common container settings. Optional: Defaults to empty. See type description for default values of each field.

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
<td style="text-align: left;"><p><code>appArmorProfile</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>appArmorProfile is the AppArmor options to use by the containers in this pod. Note that this field cannot be set when spec.os.name is windows.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>fsGroup</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p>A special supplemental group that applies to all containers in a pod. Some volume types allow the Kubelet to change the ownership of that volume to be owned by the pod:</p>
<p>1. The owning GID will be the FSGroup 2. The setgid bit is set (new files created in the volume will be owned by FSGroup) 3. The permission bits are OR’d with rw-rw----</p>
<p>If unset, the Kubelet will not modify the ownership and permissions of any volume. Note that this field cannot be set when spec.os.name is windows.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>fsGroupChangePolicy</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>fsGroupChangePolicy defines behavior of changing ownership and permission of the volume before being exposed inside Pod. This field will only apply to volume types which support fsGroup based ownership(and permissions). It will have no effect on ephemeral volume types such as: secret, configmaps and emptydir. Valid values are "OnRootMismatch" and "Always". If not specified, "Always" is used. Note that this field cannot be set when spec.os.name is windows.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>runAsGroup</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p>The GID to run the entrypoint of the container process. Uses runtime default if unset. May also be set in SecurityContext. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence for that container. Note that this field cannot be set when spec.os.name is windows.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>runAsNonRoot</code></p></td>
<td style="text-align: left;"><p><code>boolean</code></p></td>
<td style="text-align: left;"><p>Indicates that the container must run as a non-root user. If true, the Kubelet will validate the image at runtime to ensure that it does not run as UID 0 (root) and fail to start the container if it does. If unset or false, no such validation will be performed. May also be set in SecurityContext. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>runAsUser</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p>The UID to run the entrypoint of the container process. Defaults to user specified in image metadata if unspecified. May also be set in SecurityContext. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence for that container. Note that this field cannot be set when spec.os.name is windows.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>seLinuxChangePolicy</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>seLinuxChangePolicy defines how the container’s SELinux label is applied to all volumes used by the Pod. It has no effect on nodes that do not support SELinux or to volumes does not support SELinux. Valid values are "MountOption" and "Recursive".</p>
<p>"Recursive" means relabeling of all files on all Pod volumes by the container runtime. This may be slow for large volumes, but allows mixing privileged and unprivileged Pods sharing the same volume on the same node.</p>
<p>"MountOption" mounts all eligible Pod volumes with <code>-o context</code> mount option. This requires all Pods that share the same volume to use the same SELinux label. It is not possible to share the same volume among privileged and unprivileged Pods. Eligible volumes are in-tree FibreChannel and iSCSI volumes, and all CSI volumes whose CSI driver announces SELinux support by setting spec.seLinuxMount: true in their CSIDriver instance. Other volumes are always re-labelled recursively. "MountOption" value is allowed only when SELinuxMount feature gate is enabled.</p>
<p>If not specified and SELinuxMount feature gate is enabled, "MountOption" is used. If not specified and SELinuxMount feature gate is disabled, "MountOption" is used for ReadWriteOncePod volumes and "Recursive" for all other volumes.</p>
<p>This field affects only Pods that have SELinux label set, either in PodSecurityContext or in SecurityContext of all containers.</p>
<p>All Pods that use the same volume should use the same seLinuxChangePolicy, otherwise some pods can get stuck in ContainerCreating state. Note that this field cannot be set when spec.os.name is windows.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>seLinuxOptions</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>The SELinux context to be applied to all containers. If unspecified, the container runtime will allocate a random SELinux context for each container. May also be set in SecurityContext. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence for that container. Note that this field cannot be set when spec.os.name is windows.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>seccompProfile</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>The seccomp options to use by the containers in this pod. Note that this field cannot be set when spec.os.name is windows.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>supplementalGroups</code></p></td>
<td style="text-align: left;"><p><code>array (integer)</code></p></td>
<td style="text-align: left;"><p>A list of groups applied to the first process run in each container, in addition to the container’s primary GID and fsGroup (if specified). If the SupplementalGroupsPolicy feature is enabled, the supplementalGroupsPolicy field determines whether these are in addition to or instead of any group memberships defined in the container image. If unspecified, no additional groups are added, though group memberships defined in the container image may still be used, depending on the supplementalGroupsPolicy field. Note that this field cannot be set when spec.os.name is windows.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>supplementalGroupsPolicy</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Defines how supplemental groups of the first container processes are calculated. Valid values are "Merge" and "Strict". If not specified, "Merge" is used. (Alpha) Using the field requires the SupplementalGroupsPolicy feature gate to be enabled and the container runtime must implement support for this feature. Note that this field cannot be set when spec.os.name is windows.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>sysctls</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>Sysctls hold a list of namespaced sysctls used for the pod. Pods with unsupported sysctls (by the container runtime) might fail to launch. Note that this field cannot be set when spec.os.name is windows.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>sysctls[]</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>Sysctl defines a kernel parameter to be set</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>windowsOptions</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>The Windows specific settings applied to all containers. If unspecified, the options within a container’s SecurityContext will be used. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence. Note that this field cannot be set when spec.os.name is linux.</p></td>
</tr>
</tbody>
</table>

## .spec.install.spec.deployments\[\].spec.template.spec.securityContext.appArmorProfile

Description
appArmorProfile is the AppArmor options to use by the containers in this pod. Note that this field cannot be set when spec.os.name is windows.

Type
`object`

Required
- `type`

| Property | Type | Description |
|----|----|----|
| `localhostProfile` | `string` | localhostProfile indicates a profile loaded on the node that should be used. The profile must be preconfigured on the node to work. Must match the loaded name of the profile. Must be set if and only if type is "Localhost". |
| `type` | `string` | type indicates which kind of AppArmor profile will be applied. Valid options are: Localhost - a profile pre-loaded on the node. RuntimeDefault - the container runtime’s default profile. Unconfined - no AppArmor enforcement. |

## .spec.install.spec.deployments\[\].spec.template.spec.securityContext.seLinuxOptions

Description
The SELinux context to be applied to all containers. If unspecified, the container runtime will allocate a random SELinux context for each container. May also be set in SecurityContext. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence for that container. Note that this field cannot be set when spec.os.name is windows.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `level` | `string` | Level is SELinux level label that applies to the container. |
| `role` | `string` | Role is a SELinux role label that applies to the container. |
| `type` | `string` | Type is a SELinux type label that applies to the container. |
| `user` | `string` | User is a SELinux user label that applies to the container. |

## .spec.install.spec.deployments\[\].spec.template.spec.securityContext.seccompProfile

Description
The seccomp options to use by the containers in this pod. Note that this field cannot be set when spec.os.name is windows.

Type
`object`

Required
- `type`

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
<td style="text-align: left;"><p><code>localhostProfile</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>localhostProfile indicates a profile defined in a file on the node should be used. The profile must be preconfigured on the node to work. Must be a descending path, relative to the kubelet’s configured seccomp profile location. Must be set if type is "Localhost". Must NOT be set for any other type.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>type</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>type indicates which kind of seccomp profile will be applied. Valid options are:</p>
<p>Localhost - a profile defined in a file on the node should be used. RuntimeDefault - the container runtime default profile should be used. Unconfined - no profile should be applied.</p></td>
</tr>
</tbody>
</table>

## .spec.install.spec.deployments\[\].spec.template.spec.securityContext.sysctls

Description
Sysctls hold a list of namespaced sysctls used for the pod. Pods with unsupported sysctls (by the container runtime) might fail to launch. Note that this field cannot be set when spec.os.name is windows.

Type
`array`

## .spec.install.spec.deployments\[\].spec.template.spec.securityContext.sysctls\[\]

Description
Sysctl defines a kernel parameter to be set

Type
`object`

Required
- `name`

- `value`

| Property | Type     | Description                |
|----------|----------|----------------------------|
| `name`   | `string` | Name of a property to set  |
| `value`  | `string` | Value of a property to set |

## .spec.install.spec.deployments\[\].spec.template.spec.securityContext.windowsOptions

Description
The Windows specific settings applied to all containers. If unspecified, the options within a container’s SecurityContext will be used. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence. Note that this field cannot be set when spec.os.name is linux.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `gmsaCredentialSpec` | `string` | GMSACredentialSpec is where the GMSA admission webhook (<https://github.com/kubernetes-sigs/windows-gmsa>) inlines the contents of the GMSA credential spec named by the GMSACredentialSpecName field. |
| `gmsaCredentialSpecName` | `string` | GMSACredentialSpecName is the name of the GMSA credential spec to use. |
| `hostProcess` | `boolean` | HostProcess determines if a container should be run as a 'Host Process' container. All of a Pod’s containers must have the same effective HostProcess value (it is not allowed to have a mix of HostProcess containers and non-HostProcess containers). In addition, if HostProcess is true then HostNetwork must also be set to true. |
| `runAsUserName` | `string` | The UserName in Windows to run the entrypoint of the container process. Defaults to the user specified in image metadata if unspecified. May also be set in PodSecurityContext. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence. |

## .spec.install.spec.deployments\[\].spec.template.spec.tolerations

Description
If specified, the pod’s tolerations.

Type
`array`

## .spec.install.spec.deployments\[\].spec.template.spec.tolerations\[\]

Description
The pod this Toleration is attached to tolerates any taint that matches the triple \<key,value,effect\> using the matching operator \<operator\>.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `effect` | `string` | Effect indicates the taint effect to match. Empty means match all taint effects. When specified, allowed values are NoSchedule, PreferNoSchedule and NoExecute. |
| `key` | `string` | Key is the taint key that the toleration applies to. Empty means match all taint keys. If the key is empty, operator must be Exists; this combination means to match all values and all keys. |
| `operator` | `string` | Operator represents a key’s relationship to the value. Valid operators are Exists and Equal. Defaults to Equal. Exists is equivalent to wildcard for value, so that a pod can tolerate all taints of a particular category. |
| `tolerationSeconds` | `integer` | TolerationSeconds represents the period of time the toleration (which must be of effect NoExecute, otherwise this field is ignored) tolerates the taint. By default, it is not set, which means tolerate the taint forever (do not evict). Zero and negative values will be treated as 0 (evict immediately) by the system. |
| `value` | `string` | Value is the taint value the toleration matches to. If the operator is Exists, the value should be empty, otherwise just a regular string. |

## .spec.install.spec.deployments\[\].spec.template.spec.topologySpreadConstraints

Description
TopologySpreadConstraints describes how a group of pods ought to spread across topology domains. Scheduler will schedule pods in a way which abides by the constraints. All topologySpreadConstraints are ANDed.

Type
`array`

## .spec.install.spec.deployments\[\].spec.template.spec.topologySpreadConstraints\[\]

Description
TopologySpreadConstraint specifies how to spread matching pods among the given topology.

Type
`object`

Required
- `maxSkew`

- `topologyKey`

- `whenUnsatisfiable`

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
<td style="text-align: left;"><p><code>labelSelector</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>LabelSelector is used to find matching pods. Pods that match this label selector are counted to determine the number of pods in their corresponding topology domain.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>matchLabelKeys</code></p></td>
<td style="text-align: left;"><p><code>array (string)</code></p></td>
<td style="text-align: left;"><p>MatchLabelKeys is a set of pod label keys to select the pods over which spreading will be calculated. The keys are used to lookup values from the incoming pod labels, those key-value labels are ANDed with labelSelector to select the group of existing pods over which spreading will be calculated for the incoming pod. The same key is forbidden to exist in both MatchLabelKeys and LabelSelector. MatchLabelKeys cannot be set when LabelSelector isn’t set. Keys that don’t exist in the incoming pod labels will be ignored. A null or empty list means only match against labelSelector.</p>
<p>This is a beta field and requires the MatchLabelKeysInPodTopologySpread feature gate to be enabled (enabled by default).</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>maxSkew</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p>MaxSkew describes the degree to which pods may be unevenly distributed. When <code>whenUnsatisfiable=DoNotSchedule</code>, it is the maximum permitted difference between the number of matching pods in the target topology and the global minimum. The global minimum is the minimum number of matching pods in an eligible domain or zero if the number of eligible domains is less than MinDomains. For example, in a 3-zone cluster, MaxSkew is set to 1, and pods with the same labelSelector spread as 2/2/1: In this case, the global minimum is 1. | zone1 | zone2 | zone3 | | P P | P P | P | - if MaxSkew is 1, incoming pod can only be scheduled to zone3 to become 2/2/2; scheduling it onto zone1(zone2) would make the ActualSkew(3-1) on zone1(zone2) violate MaxSkew(1). - if MaxSkew is 2, incoming pod can be scheduled onto any zone. When <code>whenUnsatisfiable=ScheduleAnyway</code>, it is used to give higher precedence to topologies that satisfy it. It’s a required field. Default value is 1 and 0 is not allowed.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>minDomains</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p>MinDomains indicates a minimum number of eligible domains. When the number of eligible domains with matching topology keys is less than minDomains, Pod Topology Spread treats "global minimum" as 0, and then the calculation of Skew is performed. And when the number of eligible domains with matching topology keys equals or greater than minDomains, this value has no effect on scheduling. As a result, when the number of eligible domains is less than minDomains, scheduler won’t schedule more than maxSkew Pods to those domains. If value is nil, the constraint behaves as if MinDomains is equal to 1. Valid values are integers greater than 0. When value is not nil, WhenUnsatisfiable must be DoNotSchedule.</p>
<p>For example, in a 3-zone cluster, MaxSkew is set to 2, MinDomains is set to 5 and pods with the same labelSelector spread as 2/2/2: | zone1 | zone2 | zone3 | | P P | P P | P P | The number of domains is less than 5(MinDomains), so "global minimum" is treated as 0. In this situation, new pod with the same labelSelector cannot be scheduled, because computed skew will be 3(3 - 0) if new Pod is scheduled to any of the three zones, it will violate MaxSkew.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>nodeAffinityPolicy</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>NodeAffinityPolicy indicates how we will treat Pod’s nodeAffinity/nodeSelector when calculating pod topology spread skew. Options are: - Honor: only nodes matching nodeAffinity/nodeSelector are included in the calculations. - Ignore: nodeAffinity/nodeSelector are ignored. All nodes are included in the calculations.</p>
<p>If this value is nil, the behavior is equivalent to the Honor policy.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>nodeTaintsPolicy</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>NodeTaintsPolicy indicates how we will treat node taints when calculating pod topology spread skew. Options are: - Honor: nodes without taints, along with tainted nodes for which the incoming pod has a toleration, are included. - Ignore: node taints are ignored. All nodes are included.</p>
<p>If this value is nil, the behavior is equivalent to the Ignore policy.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>topologyKey</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>TopologyKey is the key of node labels. Nodes that have a label with this key and identical values are considered to be in the same topology. We consider each &lt;key, value&gt; as a "bucket", and try to put balanced number of pods into each bucket. We define a domain as a particular instance of a topology. Also, we define an eligible domain as a domain whose nodes meet the requirements of nodeAffinityPolicy and nodeTaintsPolicy. e.g. If TopologyKey is "kubernetes.io/hostname", each Node is a domain of that topology. And, if TopologyKey is "topology.kubernetes.io/zone", each zone is a domain of that topology. It’s a required field.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>whenUnsatisfiable</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>WhenUnsatisfiable indicates how to deal with a pod if it doesn’t satisfy the spread constraint. - DoNotSchedule (default) tells the scheduler not to schedule it. - ScheduleAnyway tells the scheduler to schedule the pod in any location, but giving higher precedence to topologies that would help reduce the skew. A constraint is considered "Unsatisfiable" for an incoming pod if and only if every possible node assignment for that pod would violate "MaxSkew" on some topology. For example, in a 3-zone cluster, MaxSkew is set to 1, and pods with the same labelSelector spread as 3/1/1: | zone1 | zone2 | zone3 | | P P P | P | P | If WhenUnsatisfiable is set to DoNotSchedule, incoming pod can only be scheduled to zone2(zone3) to become 3/2/1(3/1/2) as ActualSkew(2-1) on zone2(zone3) satisfies MaxSkew(1). In other words, the cluster can still be imbalanced, but scheduler won’t make it <strong>more</strong> imbalanced. It’s a required field.</p></td>
</tr>
</tbody>
</table>

## .spec.install.spec.deployments\[\].spec.template.spec.topologySpreadConstraints\[\].labelSelector

Description
LabelSelector is used to find matching pods. Pods that match this label selector are counted to determine the number of pods in their corresponding topology domain.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `matchExpressions` | `array` | matchExpressions is a list of label selector requirements. The requirements are ANDed. |
| `matchExpressions[]` | `object` | A label selector requirement is a selector that contains values, a key, and an operator that relates the key and values. |
| `matchLabels` | `object (string)` | matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed. |

## .spec.install.spec.deployments\[\].spec.template.spec.topologySpreadConstraints\[\].labelSelector.matchExpressions

Description
matchExpressions is a list of label selector requirements. The requirements are ANDed.

Type
`array`

## .spec.install.spec.deployments\[\].spec.template.spec.topologySpreadConstraints\[\].labelSelector.matchExpressions\[\]

Description
A label selector requirement is a selector that contains values, a key, and an operator that relates the key and values.

Type
`object`

Required
- `key`

- `operator`

| Property | Type | Description |
|----|----|----|
| `key` | `string` | key is the label key that the selector applies to. |
| `operator` | `string` | operator represents a key’s relationship to a set of values. Valid operators are In, NotIn, Exists and DoesNotExist. |
| `values` | `array (string)` | values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch. |

## .spec.install.spec.deployments\[\].spec.template.spec.volumes

Description
List of volumes that can be mounted by containers belonging to the pod. More info: <https://kubernetes.io/docs/concepts/storage/volumes>

Type
`array`

## .spec.install.spec.deployments\[\].spec.template.spec.volumes\[\]

Description
Volume represents a named volume in a pod that may be accessed by any container in the pod.

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
<td style="text-align: left;"><p><code>awsElasticBlockStore</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>awsElasticBlockStore represents an AWS Disk resource that is attached to a kubelet’s host machine and then exposed to the pod. Deprecated: AWSElasticBlockStore is deprecated. All operations for the in-tree awsElasticBlockStore type are redirected to the ebs.csi.aws.com CSI driver. More info: <a href="https://kubernetes.io/docs/concepts/storage/volumes#awselasticblockstore">https://kubernetes.io/docs/concepts/storage/volumes#awselasticblockstore</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>azureDisk</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>azureDisk represents an Azure Data Disk mount on the host and bind mount to the pod. Deprecated: AzureDisk is deprecated. All operations for the in-tree azureDisk type are redirected to the disk.csi.azure.com CSI driver.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>azureFile</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>azureFile represents an Azure File Service mount on the host and bind mount to the pod. Deprecated: AzureFile is deprecated. All operations for the in-tree azureFile type are redirected to the file.csi.azure.com CSI driver.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>cephfs</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>cephFS represents a Ceph FS mount on the host that shares a pod’s lifetime. Deprecated: CephFS is deprecated and the in-tree cephfs type is no longer supported.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>cinder</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>cinder represents a cinder volume attached and mounted on kubelets host machine. Deprecated: Cinder is deprecated. All operations for the in-tree cinder type are redirected to the cinder.csi.openstack.org CSI driver. More info: <a href="https://examples.k8s.io/mysql-cinder-pd/README.md">https://examples.k8s.io/mysql-cinder-pd/README.md</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>configMap</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>configMap represents a configMap that should populate this volume</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>csi</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>csi (Container Storage Interface) represents ephemeral storage that is handled by certain external CSI drivers.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>downwardAPI</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>downwardAPI represents downward API about the pod that should populate this volume</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>emptyDir</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>emptyDir represents a temporary directory that shares a pod’s lifetime. More info: <a href="https://kubernetes.io/docs/concepts/storage/volumes#emptydir">https://kubernetes.io/docs/concepts/storage/volumes#emptydir</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>ephemeral</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>ephemeral represents a volume that is handled by a cluster storage driver. The volume’s lifecycle is tied to the pod that defines it - it will be created before the pod starts, and deleted when the pod is removed.</p>
<p>Use this if: a) the volume is only needed while the pod runs, b) features of normal volumes like restoring from snapshot or capacity tracking are needed, c) the storage driver is specified through a storage class, and d) the storage driver supports dynamic volume provisioning through a PersistentVolumeClaim (see EphemeralVolumeSource for more information on the connection between this volume type and PersistentVolumeClaim).</p>
<p>Use PersistentVolumeClaim or one of the vendor-specific APIs for volumes that persist for longer than the lifecycle of an individual pod.</p>
<p>Use CSI for light-weight local ephemeral volumes if the CSI driver is meant to be used that way - see the documentation of the driver for more information.</p>
<p>A pod can use both types of ephemeral volumes and persistent volumes at the same time.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>fc</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>fc represents a Fibre Channel resource that is attached to a kubelet’s host machine and then exposed to the pod.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>flexVolume</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>flexVolume represents a generic volume resource that is provisioned/attached using an exec based plugin. Deprecated: FlexVolume is deprecated. Consider using a CSIDriver instead.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>flocker</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>flocker represents a Flocker volume attached to a kubelet’s host machine. This depends on the Flocker control service being running. Deprecated: Flocker is deprecated and the in-tree flocker type is no longer supported.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>gcePersistentDisk</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>gcePersistentDisk represents a GCE Disk resource that is attached to a kubelet’s host machine and then exposed to the pod. Deprecated: GCEPersistentDisk is deprecated. All operations for the in-tree gcePersistentDisk type are redirected to the pd.csi.storage.gke.io CSI driver. More info: <a href="https://kubernetes.io/docs/concepts/storage/volumes#gcepersistentdisk">https://kubernetes.io/docs/concepts/storage/volumes#gcepersistentdisk</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>gitRepo</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>gitRepo represents a git repository at a particular revision. Deprecated: GitRepo is deprecated. To provision a container with a git repo, mount an EmptyDir into an InitContainer that clones the repo using git, then mount the EmptyDir into the Pod’s container.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>glusterfs</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>glusterfs represents a Glusterfs mount on the host that shares a pod’s lifetime. Deprecated: Glusterfs is deprecated and the in-tree glusterfs type is no longer supported. More info: <a href="https://examples.k8s.io/volumes/glusterfs/README.md">https://examples.k8s.io/volumes/glusterfs/README.md</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>hostPath</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>hostPath represents a pre-existing file or directory on the host machine that is directly exposed to the container. This is generally used for system agents or other privileged things that are allowed to see the host machine. Most containers will NOT need this. More info: <a href="https://kubernetes.io/docs/concepts/storage/volumes#hostpath">https://kubernetes.io/docs/concepts/storage/volumes#hostpath</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>image</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>image represents an OCI object (a container image or artifact) pulled and mounted on the kubelet’s host machine. The volume is resolved at pod startup depending on which PullPolicy value is provided:</p>
<p>- Always: the kubelet always attempts to pull the reference. Container creation will fail If the pull fails. - Never: the kubelet never pulls the reference and only uses a local image or artifact. Container creation will fail if the reference isn’t present. - IfNotPresent: the kubelet pulls if the reference isn’t already present on disk. Container creation will fail if the reference isn’t present and the pull fails.</p>
<p>The volume gets re-resolved if the pod gets deleted and recreated, which means that new remote content will become available on pod recreation. A failure to resolve or pull the image during pod startup will block containers from starting and may add significant latency. Failures will be retried using normal volume backoff and will be reported on the pod reason and message. The types of objects that may be mounted by this volume are defined by the container runtime implementation on a host machine and at minimum must include all valid types supported by the container image field. The OCI object gets mounted in a single directory (spec.containers[<strong>].volumeMounts.mountPath) by merging the manifest layers in the same way as for container images. The volume will be mounted read-only (ro) and non-executable files (noexec). Sub path mounts for containers are not supported (spec.containers[</strong>].volumeMounts.subpath) before 1.33. The field spec.securityContext.fsGroupChangePolicy has no effect on this volume type.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>iscsi</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>iscsi represents an ISCSI Disk resource that is attached to a kubelet’s host machine and then exposed to the pod. More info: <a href="https://examples.k8s.io/volumes/iscsi/README.md">https://examples.k8s.io/volumes/iscsi/README.md</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>name</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>name of the volume. Must be a DNS_LABEL and unique within the pod. More info: <a href="https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names">https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>nfs</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>nfs represents an NFS mount on the host that shares a pod’s lifetime More info: <a href="https://kubernetes.io/docs/concepts/storage/volumes#nfs">https://kubernetes.io/docs/concepts/storage/volumes#nfs</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>persistentVolumeClaim</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>persistentVolumeClaimVolumeSource represents a reference to a PersistentVolumeClaim in the same namespace. More info: <a href="https://kubernetes.io/docs/concepts/storage/persistent-volumes#persistentvolumeclaims">https://kubernetes.io/docs/concepts/storage/persistent-volumes#persistentvolumeclaims</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>photonPersistentDisk</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>photonPersistentDisk represents a PhotonController persistent disk attached and mounted on kubelets host machine. Deprecated: PhotonPersistentDisk is deprecated and the in-tree photonPersistentDisk type is no longer supported.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>portworxVolume</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>portworxVolume represents a portworx volume attached and mounted on kubelets host machine. Deprecated: PortworxVolume is deprecated. All operations for the in-tree portworxVolume type are redirected to the pxd.portworx.com CSI driver when the CSIMigrationPortworx feature-gate is on.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>projected</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>projected items for all in one resources secrets, configmaps, and downward API</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>quobyte</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>quobyte represents a Quobyte mount on the host that shares a pod’s lifetime. Deprecated: Quobyte is deprecated and the in-tree quobyte type is no longer supported.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>rbd</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>rbd represents a Rados Block Device mount on the host that shares a pod’s lifetime. Deprecated: RBD is deprecated and the in-tree rbd type is no longer supported. More info: <a href="https://examples.k8s.io/volumes/rbd/README.md">https://examples.k8s.io/volumes/rbd/README.md</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>scaleIO</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>scaleIO represents a ScaleIO persistent volume attached and mounted on Kubernetes nodes. Deprecated: ScaleIO is deprecated and the in-tree scaleIO type is no longer supported.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>secret</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>secret represents a secret that should populate this volume. More info: <a href="https://kubernetes.io/docs/concepts/storage/volumes#secret">https://kubernetes.io/docs/concepts/storage/volumes#secret</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>storageos</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>storageOS represents a StorageOS volume attached and mounted on Kubernetes nodes. Deprecated: StorageOS is deprecated and the in-tree storageos type is no longer supported.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>vsphereVolume</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>vsphereVolume represents a vSphere volume attached and mounted on kubelets host machine. Deprecated: VsphereVolume is deprecated. All operations for the in-tree vsphereVolume type are redirected to the csi.vsphere.vmware.com CSI driver.</p></td>
</tr>
</tbody>
</table>

## .spec.install.spec.deployments\[\].spec.template.spec.volumes\[\].awsElasticBlockStore

Description
awsElasticBlockStore represents an AWS Disk resource that is attached to a kubelet’s host machine and then exposed to the pod. Deprecated: AWSElasticBlockStore is deprecated. All operations for the in-tree awsElasticBlockStore type are redirected to the ebs.csi.aws.com CSI driver. More info: <https://kubernetes.io/docs/concepts/storage/volumes#awselasticblockstore>

Type
`object`

Required
- `volumeID`

| Property | Type | Description |
|----|----|----|
| `fsType` | `string` | fsType is the filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: <https://kubernetes.io/docs/concepts/storage/volumes#awselasticblockstore> |
| `partition` | `integer` | partition is the partition in the volume that you want to mount. If omitted, the default is to mount by volume name. Examples: For volume /dev/sda1, you specify the partition as "1". Similarly, the volume partition for /dev/sda is "0" (or you can leave the property empty). |
| `readOnly` | `boolean` | readOnly value true will force the readOnly setting in VolumeMounts. More info: <https://kubernetes.io/docs/concepts/storage/volumes#awselasticblockstore> |
| `volumeID` | `string` | volumeID is unique ID of the persistent disk resource in AWS (Amazon EBS volume). More info: <https://kubernetes.io/docs/concepts/storage/volumes#awselasticblockstore> |

## .spec.install.spec.deployments\[\].spec.template.spec.volumes\[\].azureDisk

Description
azureDisk represents an Azure Data Disk mount on the host and bind mount to the pod. Deprecated: AzureDisk is deprecated. All operations for the in-tree azureDisk type are redirected to the disk.csi.azure.com CSI driver.

Type
`object`

Required
- `diskName`

- `diskURI`

| Property | Type | Description |
|----|----|----|
| `cachingMode` | `string` | cachingMode is the Host Caching mode: None, Read Only, Read Write. |
| `diskName` | `string` | diskName is the Name of the data disk in the blob storage |
| `diskURI` | `string` | diskURI is the URI of data disk in the blob storage |
| `fsType` | `string` | fsType is Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. |
| `kind` | `string` | kind expected values are Shared: multiple blob disks per storage account Dedicated: single blob disk per storage account Managed: azure managed data disk (only in managed availability set). defaults to shared |
| `readOnly` | `boolean` | readOnly Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts. |

## .spec.install.spec.deployments\[\].spec.template.spec.volumes\[\].azureFile

Description
azureFile represents an Azure File Service mount on the host and bind mount to the pod. Deprecated: AzureFile is deprecated. All operations for the in-tree azureFile type are redirected to the file.csi.azure.com CSI driver.

Type
`object`

Required
- `secretName`

- `shareName`

| Property | Type | Description |
|----|----|----|
| `readOnly` | `boolean` | readOnly defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts. |
| `secretName` | `string` | secretName is the name of secret that contains Azure Storage Account Name and Key |
| `shareName` | `string` | shareName is the azure share Name |

## .spec.install.spec.deployments\[\].spec.template.spec.volumes\[\].cephfs

Description
cephFS represents a Ceph FS mount on the host that shares a pod’s lifetime. Deprecated: CephFS is deprecated and the in-tree cephfs type is no longer supported.

Type
`object`

Required
- `monitors`

| Property | Type | Description |
|----|----|----|
| `monitors` | `array (string)` | monitors is Required: Monitors is a collection of Ceph monitors More info: <https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it> |
| `path` | `string` | path is Optional: Used as the mounted root, rather than the full Ceph tree, default is / |
| `readOnly` | `boolean` | readOnly is Optional: Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts. More info: <https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it> |
| `secretFile` | `string` | secretFile is Optional: SecretFile is the path to key ring for User, default is /etc/ceph/user.secret More info: <https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it> |
| `secretRef` | `object` | secretRef is Optional: SecretRef is reference to the authentication secret for User, default is empty. More info: <https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it> |
| `user` | `string` | user is optional: User is the rados user name, default is admin More info: <https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it> |

## .spec.install.spec.deployments\[\].spec.template.spec.volumes\[\].cephfs.secretRef

Description
secretRef is Optional: SecretRef is reference to the authentication secret for User, default is empty. More info: <https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it>

Type
`object`

| Property | Type | Description |
|----|----|----|
| `name` | `string` | Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names> |

## .spec.install.spec.deployments\[\].spec.template.spec.volumes\[\].cinder

Description
cinder represents a cinder volume attached and mounted on kubelets host machine. Deprecated: Cinder is deprecated. All operations for the in-tree cinder type are redirected to the cinder.csi.openstack.org CSI driver. More info: <https://examples.k8s.io/mysql-cinder-pd/README.md>

Type
`object`

Required
- `volumeID`

| Property | Type | Description |
|----|----|----|
| `fsType` | `string` | fsType is the filesystem type to mount. Must be a filesystem type supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: <https://examples.k8s.io/mysql-cinder-pd/README.md> |
| `readOnly` | `boolean` | readOnly defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts. More info: <https://examples.k8s.io/mysql-cinder-pd/README.md> |
| `secretRef` | `object` | secretRef is optional: points to a secret object containing parameters used to connect to OpenStack. |
| `volumeID` | `string` | volumeID used to identify the volume in cinder. More info: <https://examples.k8s.io/mysql-cinder-pd/README.md> |

## .spec.install.spec.deployments\[\].spec.template.spec.volumes\[\].cinder.secretRef

Description
secretRef is optional: points to a secret object containing parameters used to connect to OpenStack.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `name` | `string` | Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names> |

## .spec.install.spec.deployments\[\].spec.template.spec.volumes\[\].configMap

Description
configMap represents a configMap that should populate this volume

Type
`object`

| Property | Type | Description |
|----|----|----|
| `defaultMode` | `integer` | defaultMode is optional: mode bits used to set permissions on created files by default. Must be an octal value between 0000 and 0777 or a decimal value between 0 and 511. YAML accepts both octal and decimal values, JSON requires decimal values for mode bits. Defaults to 0644. Directories within the path are not affected by this setting. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set. |
| `items` | `array` | items if unspecified, each key-value pair in the Data field of the referenced ConfigMap will be projected into the volume as a file whose name is the key and content is the value. If specified, the listed keys will be projected into the specified paths, and unlisted keys will not be present. If a key is specified which is not present in the ConfigMap, the volume setup will error unless it is marked optional. Paths must be relative and may not contain the '..' path or start with '..'. |
| `items[]` | `object` | Maps a string key to a path within a volume. |
| `name` | `string` | Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names> |
| `optional` | `boolean` | optional specify whether the ConfigMap or its keys must be defined |

## .spec.install.spec.deployments\[\].spec.template.spec.volumes\[\].configMap.items

Description
items if unspecified, each key-value pair in the Data field of the referenced ConfigMap will be projected into the volume as a file whose name is the key and content is the value. If specified, the listed keys will be projected into the specified paths, and unlisted keys will not be present. If a key is specified which is not present in the ConfigMap, the volume setup will error unless it is marked optional. Paths must be relative and may not contain the '..' path or start with '..'.

Type
`array`

## .spec.install.spec.deployments\[\].spec.template.spec.volumes\[\].configMap.items\[\]

Description
Maps a string key to a path within a volume.

Type
`object`

Required
- `key`

- `path`

| Property | Type | Description |
|----|----|----|
| `key` | `string` | key is the key to project. |
| `mode` | `integer` | mode is Optional: mode bits used to set permissions on this file. Must be an octal value between 0000 and 0777 or a decimal value between 0 and 511. YAML accepts both octal and decimal values, JSON requires decimal values for mode bits. If not specified, the volume defaultMode will be used. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set. |
| `path` | `string` | path is the relative path of the file to map the key to. May not be an absolute path. May not contain the path element '..'. May not start with the string '..'. |

## .spec.install.spec.deployments\[\].spec.template.spec.volumes\[\].csi

Description
csi (Container Storage Interface) represents ephemeral storage that is handled by certain external CSI drivers.

Type
`object`

Required
- `driver`

| Property | Type | Description |
|----|----|----|
| `driver` | `string` | driver is the name of the CSI driver that handles this volume. Consult with your admin for the correct name as registered in the cluster. |
| `fsType` | `string` | fsType to mount. Ex. "ext4", "xfs", "ntfs". If not provided, the empty value is passed to the associated CSI driver which will determine the default filesystem to apply. |
| `nodePublishSecretRef` | `object` | nodePublishSecretRef is a reference to the secret object containing sensitive information to pass to the CSI driver to complete the CSI NodePublishVolume and NodeUnpublishVolume calls. This field is optional, and may be empty if no secret is required. If the secret object contains more than one secret, all secret references are passed. |
| `readOnly` | `boolean` | readOnly specifies a read-only configuration for the volume. Defaults to false (read/write). |
| `volumeAttributes` | `object (string)` | volumeAttributes stores driver-specific properties that are passed to the CSI driver. Consult your driver’s documentation for supported values. |

## .spec.install.spec.deployments\[\].spec.template.spec.volumes\[\].csi.nodePublishSecretRef

Description
nodePublishSecretRef is a reference to the secret object containing sensitive information to pass to the CSI driver to complete the CSI NodePublishVolume and NodeUnpublishVolume calls. This field is optional, and may be empty if no secret is required. If the secret object contains more than one secret, all secret references are passed.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `name` | `string` | Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names> |

## .spec.install.spec.deployments\[\].spec.template.spec.volumes\[\].downwardAPI

Description
downwardAPI represents downward API about the pod that should populate this volume

Type
`object`

| Property | Type | Description |
|----|----|----|
| `defaultMode` | `integer` | Optional: mode bits to use on created files by default. Must be a Optional: mode bits used to set permissions on created files by default. Must be an octal value between 0000 and 0777 or a decimal value between 0 and 511. YAML accepts both octal and decimal values, JSON requires decimal values for mode bits. Defaults to 0644. Directories within the path are not affected by this setting. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set. |
| `items` | `array` | Items is a list of downward API volume file |
| `items[]` | `object` | DownwardAPIVolumeFile represents information to create the file containing the pod field |

## .spec.install.spec.deployments\[\].spec.template.spec.volumes\[\].downwardAPI.items

Description
Items is a list of downward API volume file

Type
`array`

## .spec.install.spec.deployments\[\].spec.template.spec.volumes\[\].downwardAPI.items\[\]

Description
DownwardAPIVolumeFile represents information to create the file containing the pod field

Type
`object`

Required
- `path`

| Property | Type | Description |
|----|----|----|
| `fieldRef` | `object` | Required: Selects a field of the pod: only annotations, labels, name, namespace and uid are supported. |
| `mode` | `integer` | Optional: mode bits used to set permissions on this file, must be an octal value between 0000 and 0777 or a decimal value between 0 and 511. YAML accepts both octal and decimal values, JSON requires decimal values for mode bits. If not specified, the volume defaultMode will be used. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set. |
| `path` | `string` | Required: Path is the relative path name of the file to be created. Must not be absolute or contain the '..' path. Must be utf-8 encoded. The first item of the relative path must not start with '..' |
| `resourceFieldRef` | `object` | Selects a resource of the container: only resources limits and requests (limits.cpu, limits.memory, requests.cpu and requests.memory) are currently supported. |

## .spec.install.spec.deployments\[\].spec.template.spec.volumes\[\].downwardAPI.items\[\].fieldRef

Description
Required: Selects a field of the pod: only annotations, labels, name, namespace and uid are supported.

Type
`object`

Required
- `fieldPath`

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | Version of the schema the FieldPath is written in terms of, defaults to "v1". |
| `fieldPath` | `string` | Path of the field to select in the specified API version. |

## .spec.install.spec.deployments\[\].spec.template.spec.volumes\[\].downwardAPI.items\[\].resourceFieldRef

Description
Selects a resource of the container: only resources limits and requests (limits.cpu, limits.memory, requests.cpu and requests.memory) are currently supported.

Type
`object`

Required
- `resource`

| Property | Type | Description |
|----|----|----|
| `containerName` | `string` | Container name: required for volumes, optional for env vars |
| `divisor` | `integer-or-string` | Specifies the output format of the exposed resources, defaults to "1" |
| `resource` | `string` | Required: resource to select |

## .spec.install.spec.deployments\[\].spec.template.spec.volumes\[\].emptyDir

Description
emptyDir represents a temporary directory that shares a pod’s lifetime. More info: <https://kubernetes.io/docs/concepts/storage/volumes#emptydir>

Type
`object`

| Property | Type | Description |
|----|----|----|
| `medium` | `string` | medium represents what type of storage medium should back this directory. The default is "" which means to use the node’s default medium. Must be an empty string (default) or Memory. More info: <https://kubernetes.io/docs/concepts/storage/volumes#emptydir> |
| `sizeLimit` | `integer-or-string` | sizeLimit is the total amount of local storage required for this EmptyDir volume. The size limit is also applicable for memory medium. The maximum usage on memory medium EmptyDir would be the minimum value between the SizeLimit specified here and the sum of memory limits of all containers in a pod. The default is nil which means that the limit is undefined. More info: <https://kubernetes.io/docs/concepts/storage/volumes#emptydir> |

## .spec.install.spec.deployments\[\].spec.template.spec.volumes\[\].ephemeral

Description
ephemeral represents a volume that is handled by a cluster storage driver. The volume’s lifecycle is tied to the pod that defines it - it will be created before the pod starts, and deleted when the pod is removed.

Use this if: a) the volume is only needed while the pod runs, b) features of normal volumes like restoring from snapshot or capacity tracking are needed, c) the storage driver is specified through a storage class, and d) the storage driver supports dynamic volume provisioning through a PersistentVolumeClaim (see EphemeralVolumeSource for more information on the connection between this volume type and PersistentVolumeClaim).

Use PersistentVolumeClaim or one of the vendor-specific APIs for volumes that persist for longer than the lifecycle of an individual pod.

Use CSI for light-weight local ephemeral volumes if the CSI driver is meant to be used that way - see the documentation of the driver for more information.

A pod can use both types of ephemeral volumes and persistent volumes at the same time.

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
<td style="text-align: left;"><p><code>volumeClaimTemplate</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>Will be used to create a stand-alone PVC to provision the volume. The pod in which this EphemeralVolumeSource is embedded will be the owner of the PVC, i.e. the PVC will be deleted together with the pod. The name of the PVC will be <code>&lt;pod name&gt;-&lt;volume name&gt;</code> where <code>&lt;volume name&gt;</code> is the name from the <code>PodSpec.Volumes</code> array entry. Pod validation will reject the pod if the concatenated name is not valid for a PVC (for example, too long).</p>
<p>An existing PVC with that name that is not owned by the pod will <strong>not</strong> be used for the pod to avoid using an unrelated volume by mistake. Starting the pod is then blocked until the unrelated PVC is removed. If such a pre-created PVC is meant to be used by the pod, the PVC has to updated with an owner reference to the pod once the pod exists. Normally this should not be necessary, but it may be useful when manually reconstructing a broken cluster.</p>
<p>This field is read-only and no changes will be made by Kubernetes to the PVC after it has been created.</p>
<p>Required, must not be nil.</p></td>
</tr>
</tbody>
</table>

## .spec.install.spec.deployments\[\].spec.template.spec.volumes\[\].ephemeral.volumeClaimTemplate

Description
Will be used to create a stand-alone PVC to provision the volume. The pod in which this EphemeralVolumeSource is embedded will be the owner of the PVC, i.e. the PVC will be deleted together with the pod. The name of the PVC will be `<pod name>-<volume name>` where `<volume name>` is the name from the `PodSpec.Volumes` array entry. Pod validation will reject the pod if the concatenated name is not valid for a PVC (for example, too long).

An existing PVC with that name that is not owned by the pod will **not** be used for the pod to avoid using an unrelated volume by mistake. Starting the pod is then blocked until the unrelated PVC is removed. If such a pre-created PVC is meant to be used by the pod, the PVC has to updated with an owner reference to the pod once the pod exists. Normally this should not be necessary, but it may be useful when manually reconstructing a broken cluster.

This field is read-only and no changes will be made by Kubernetes to the PVC after it has been created.

Required, must not be nil.

Type
`object`

Required
- `spec`

| Property | Type | Description |
|----|----|----|
| `metadata` | `object` | May contain labels and annotations that will be copied into the PVC when creating it. No other fields are allowed and will be rejected during validation. |
| `spec` | `object` | The specification for the PersistentVolumeClaim. The entire content is copied unchanged into the PVC that gets created from this template. The same fields as in a PersistentVolumeClaim are also valid here. |

## .spec.install.spec.deployments\[\].spec.template.spec.volumes\[\].ephemeral.volumeClaimTemplate.metadata

Description
May contain labels and annotations that will be copied into the PVC when creating it. No other fields are allowed and will be rejected during validation.

Type
`object`

## .spec.install.spec.deployments\[\].spec.template.spec.volumes\[\].ephemeral.volumeClaimTemplate.spec

Description
The specification for the PersistentVolumeClaim. The entire content is copied unchanged into the PVC that gets created from this template. The same fields as in a PersistentVolumeClaim are also valid here.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `accessModes` | `array (string)` | accessModes contains the desired access modes the volume should have. More info: <https://kubernetes.io/docs/concepts/storage/persistent-volumes#access-modes-1> |
| `dataSource` | `object` | dataSource field can be used to specify either: \* An existing VolumeSnapshot object (snapshot.storage.k8s.io/VolumeSnapshot) \* An existing PVC (PersistentVolumeClaim) If the provisioner or an external controller can support the specified data source, it will create a new volume based on the contents of the specified data source. When the AnyVolumeDataSource feature gate is enabled, dataSource contents will be copied to dataSourceRef, and dataSourceRef contents will be copied to dataSource when dataSourceRef.namespace is not specified. If the namespace is specified, then dataSourceRef will not be copied to dataSource. |
| `dataSourceRef` | `object` | dataSourceRef specifies the object from which to populate the volume with data, if a non-empty volume is desired. This may be any object from a non-empty API group (non core object) or a PersistentVolumeClaim object. When this field is specified, volume binding will only succeed if the type of the specified object matches some installed volume populator or dynamic provisioner. This field will replace the functionality of the dataSource field and as such if both fields are non-empty, they must have the same value. For backwards compatibility, when namespace isn’t specified in dataSourceRef, both fields (dataSource and dataSourceRef) will be set to the same value automatically if one of them is empty and the other is non-empty. When namespace is specified in dataSourceRef, dataSource isn’t set to the same value and must be empty. There are three important differences between dataSource and dataSourceRef: \* While dataSource only allows two specific types of objects, dataSourceRef allows any non-core object, as well as PersistentVolumeClaim objects. \* While dataSource ignores disallowed values (dropping them), dataSourceRef preserves all values, and generates an error if a disallowed value is specified. \* While dataSource only allows local objects, dataSourceRef allows objects in any namespaces. (Beta) Using this field requires the AnyVolumeDataSource feature gate to be enabled. (Alpha) Using the namespace field of dataSourceRef requires the CrossNamespaceVolumeDataSource feature gate to be enabled. |
| `resources` | `object` | resources represents the minimum resources the volume should have. If RecoverVolumeExpansionFailure feature is enabled users are allowed to specify resource requirements that are lower than previous value but must still be higher than capacity recorded in the status field of the claim. More info: <https://kubernetes.io/docs/concepts/storage/persistent-volumes#resources> |
| `selector` | `object` | selector is a label query over volumes to consider for binding. |
| `storageClassName` | `string` | storageClassName is the name of the StorageClass required by the claim. More info: <https://kubernetes.io/docs/concepts/storage/persistent-volumes#class-1> |
| `volumeAttributesClassName` | `string` | volumeAttributesClassName may be used to set the VolumeAttributesClass used by this claim. If specified, the CSI driver will create or update the volume with the attributes defined in the corresponding VolumeAttributesClass. This has a different purpose than storageClassName, it can be changed after the claim is created. An empty string value means that no VolumeAttributesClass will be applied to the claim but it’s not allowed to reset this field to empty string once it is set. If unspecified and the PersistentVolumeClaim is unbound, the default VolumeAttributesClass will be set by the persistentvolume controller if it exists. If the resource referred to by volumeAttributesClass does not exist, this PersistentVolumeClaim will be set to a Pending state, as reflected by the modifyVolumeStatus field, until such as a resource exists. More info: <https://kubernetes.io/docs/concepts/storage/volume-attributes-classes/> (Beta) Using this field requires the VolumeAttributesClass feature gate to be enabled (off by default). |
| `volumeMode` | `string` | volumeMode defines what type of volume is required by the claim. Value of Filesystem is implied when not included in claim spec. |
| `volumeName` | `string` | volumeName is the binding reference to the PersistentVolume backing this claim. |

## .spec.install.spec.deployments\[\].spec.template.spec.volumes\[\].ephemeral.volumeClaimTemplate.spec.dataSource

Description
dataSource field can be used to specify either: \* An existing VolumeSnapshot object (snapshot.storage.k8s.io/VolumeSnapshot) \* An existing PVC (PersistentVolumeClaim) If the provisioner or an external controller can support the specified data source, it will create a new volume based on the contents of the specified data source. When the AnyVolumeDataSource feature gate is enabled, dataSource contents will be copied to dataSourceRef, and dataSourceRef contents will be copied to dataSource when dataSourceRef.namespace is not specified. If the namespace is specified, then dataSourceRef will not be copied to dataSource.

Type
`object`

Required
- `kind`

- `name`

| Property | Type | Description |
|----|----|----|
| `apiGroup` | `string` | APIGroup is the group for the resource being referenced. If APIGroup is not specified, the specified Kind must be in the core API group. For any other third-party types, APIGroup is required. |
| `kind` | `string` | Kind is the type of resource being referenced |
| `name` | `string` | Name is the name of resource being referenced |

## .spec.install.spec.deployments\[\].spec.template.spec.volumes\[\].ephemeral.volumeClaimTemplate.spec.dataSourceRef

Description
dataSourceRef specifies the object from which to populate the volume with data, if a non-empty volume is desired. This may be any object from a non-empty API group (non core object) or a PersistentVolumeClaim object. When this field is specified, volume binding will only succeed if the type of the specified object matches some installed volume populator or dynamic provisioner. This field will replace the functionality of the dataSource field and as such if both fields are non-empty, they must have the same value. For backwards compatibility, when namespace isn’t specified in dataSourceRef, both fields (dataSource and dataSourceRef) will be set to the same value automatically if one of them is empty and the other is non-empty. When namespace is specified in dataSourceRef, dataSource isn’t set to the same value and must be empty. There are three important differences between dataSource and dataSourceRef: \* While dataSource only allows two specific types of objects, dataSourceRef allows any non-core object, as well as PersistentVolumeClaim objects. \* While dataSource ignores disallowed values (dropping them), dataSourceRef preserves all values, and generates an error if a disallowed value is specified. \* While dataSource only allows local objects, dataSourceRef allows objects in any namespaces. (Beta) Using this field requires the AnyVolumeDataSource feature gate to be enabled. (Alpha) Using the namespace field of dataSourceRef requires the CrossNamespaceVolumeDataSource feature gate to be enabled.

Type
`object`

Required
- `kind`

- `name`

| Property | Type | Description |
|----|----|----|
| `apiGroup` | `string` | APIGroup is the group for the resource being referenced. If APIGroup is not specified, the specified Kind must be in the core API group. For any other third-party types, APIGroup is required. |
| `kind` | `string` | Kind is the type of resource being referenced |
| `name` | `string` | Name is the name of resource being referenced |
| `namespace` | `string` | Namespace is the namespace of resource being referenced Note that when a namespace is specified, a gateway.networking.k8s.io/ReferenceGrant object is required in the referent namespace to allow that namespace’s owner to accept the reference. See the ReferenceGrant documentation for details. (Alpha) This field requires the CrossNamespaceVolumeDataSource feature gate to be enabled. |

## .spec.install.spec.deployments\[\].spec.template.spec.volumes\[\].ephemeral.volumeClaimTemplate.spec.resources

Description
resources represents the minimum resources the volume should have. If RecoverVolumeExpansionFailure feature is enabled users are allowed to specify resource requirements that are lower than previous value but must still be higher than capacity recorded in the status field of the claim. More info: <https://kubernetes.io/docs/concepts/storage/persistent-volumes#resources>

Type
`object`

| Property | Type | Description |
|----|----|----|
| `limits` | `integer-or-string` | Limits describes the maximum amount of compute resources allowed. More info: <https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/> |
| `requests` | `integer-or-string` | Requests describes the minimum amount of compute resources required. If Requests is omitted for a container, it defaults to Limits if that is explicitly specified, otherwise to an implementation-defined value. Requests cannot exceed Limits. More info: <https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/> |

## .spec.install.spec.deployments\[\].spec.template.spec.volumes\[\].ephemeral.volumeClaimTemplate.spec.selector

Description
selector is a label query over volumes to consider for binding.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `matchExpressions` | `array` | matchExpressions is a list of label selector requirements. The requirements are ANDed. |
| `matchExpressions[]` | `object` | A label selector requirement is a selector that contains values, a key, and an operator that relates the key and values. |
| `matchLabels` | `object (string)` | matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed. |

## .spec.install.spec.deployments\[\].spec.template.spec.volumes\[\].ephemeral.volumeClaimTemplate.spec.selector.matchExpressions

Description
matchExpressions is a list of label selector requirements. The requirements are ANDed.

Type
`array`

## .spec.install.spec.deployments\[\].spec.template.spec.volumes\[\].ephemeral.volumeClaimTemplate.spec.selector.matchExpressions\[\]

Description
A label selector requirement is a selector that contains values, a key, and an operator that relates the key and values.

Type
`object`

Required
- `key`

- `operator`

| Property | Type | Description |
|----|----|----|
| `key` | `string` | key is the label key that the selector applies to. |
| `operator` | `string` | operator represents a key’s relationship to a set of values. Valid operators are In, NotIn, Exists and DoesNotExist. |
| `values` | `array (string)` | values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch. |

## .spec.install.spec.deployments\[\].spec.template.spec.volumes\[\].fc

Description
fc represents a Fibre Channel resource that is attached to a kubelet’s host machine and then exposed to the pod.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `fsType` | `string` | fsType is the filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. |
| `lun` | `integer` | lun is Optional: FC target lun number |
| `readOnly` | `boolean` | readOnly is Optional: Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts. |
| `targetWWNs` | `array (string)` | targetWWNs is Optional: FC target worldwide names (WWNs) |
| `wwids` | `array (string)` | wwids Optional: FC volume world wide identifiers (wwids) Either wwids or combination of targetWWNs and lun must be set, but not both simultaneously. |

## .spec.install.spec.deployments\[\].spec.template.spec.volumes\[\].flexVolume

Description
flexVolume represents a generic volume resource that is provisioned/attached using an exec based plugin. Deprecated: FlexVolume is deprecated. Consider using a CSIDriver instead.

Type
`object`

Required
- `driver`

| Property | Type | Description |
|----|----|----|
| `driver` | `string` | driver is the name of the driver to use for this volume. |
| `fsType` | `string` | fsType is the filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". The default filesystem depends on FlexVolume script. |
| `options` | `object (string)` | options is Optional: this field holds extra command options if any. |
| `readOnly` | `boolean` | readOnly is Optional: defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts. |
| `secretRef` | `object` | secretRef is Optional: secretRef is reference to the secret object containing sensitive information to pass to the plugin scripts. This may be empty if no secret object is specified. If the secret object contains more than one secret, all secrets are passed to the plugin scripts. |

## .spec.install.spec.deployments\[\].spec.template.spec.volumes\[\].flexVolume.secretRef

Description
secretRef is Optional: secretRef is reference to the secret object containing sensitive information to pass to the plugin scripts. This may be empty if no secret object is specified. If the secret object contains more than one secret, all secrets are passed to the plugin scripts.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `name` | `string` | Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names> |

## .spec.install.spec.deployments\[\].spec.template.spec.volumes\[\].flocker

Description
flocker represents a Flocker volume attached to a kubelet’s host machine. This depends on the Flocker control service being running. Deprecated: Flocker is deprecated and the in-tree flocker type is no longer supported.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `datasetName` | `string` | datasetName is Name of the dataset stored as metadata → name on the dataset for Flocker should be considered as deprecated |
| `datasetUUID` | `string` | datasetUUID is the UUID of the dataset. This is unique identifier of a Flocker dataset |

## .spec.install.spec.deployments\[\].spec.template.spec.volumes\[\].gcePersistentDisk

Description
gcePersistentDisk represents a GCE Disk resource that is attached to a kubelet’s host machine and then exposed to the pod. Deprecated: GCEPersistentDisk is deprecated. All operations for the in-tree gcePersistentDisk type are redirected to the pd.csi.storage.gke.io CSI driver. More info: <https://kubernetes.io/docs/concepts/storage/volumes#gcepersistentdisk>

Type
`object`

Required
- `pdName`

| Property | Type | Description |
|----|----|----|
| `fsType` | `string` | fsType is filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: <https://kubernetes.io/docs/concepts/storage/volumes#gcepersistentdisk> |
| `partition` | `integer` | partition is the partition in the volume that you want to mount. If omitted, the default is to mount by volume name. Examples: For volume /dev/sda1, you specify the partition as "1". Similarly, the volume partition for /dev/sda is "0" (or you can leave the property empty). More info: <https://kubernetes.io/docs/concepts/storage/volumes#gcepersistentdisk> |
| `pdName` | `string` | pdName is unique name of the PD resource in GCE. Used to identify the disk in GCE. More info: <https://kubernetes.io/docs/concepts/storage/volumes#gcepersistentdisk> |
| `readOnly` | `boolean` | readOnly here will force the ReadOnly setting in VolumeMounts. Defaults to false. More info: <https://kubernetes.io/docs/concepts/storage/volumes#gcepersistentdisk> |

## .spec.install.spec.deployments\[\].spec.template.spec.volumes\[\].gitRepo

Description
gitRepo represents a git repository at a particular revision. Deprecated: GitRepo is deprecated. To provision a container with a git repo, mount an EmptyDir into an InitContainer that clones the repo using git, then mount the EmptyDir into the Pod’s container.

Type
`object`

Required
- `repository`

| Property | Type | Description |
|----|----|----|
| `directory` | `string` | directory is the target directory name. Must not contain or start with '..'. If '.' is supplied, the volume directory will be the git repository. Otherwise, if specified, the volume will contain the git repository in the subdirectory with the given name. |
| `repository` | `string` | repository is the URL |
| `revision` | `string` | revision is the commit hash for the specified revision. |

## .spec.install.spec.deployments\[\].spec.template.spec.volumes\[\].glusterfs

Description
glusterfs represents a Glusterfs mount on the host that shares a pod’s lifetime. Deprecated: Glusterfs is deprecated and the in-tree glusterfs type is no longer supported. More info: <https://examples.k8s.io/volumes/glusterfs/README.md>

Type
`object`

Required
- `endpoints`

- `path`

| Property | Type | Description |
|----|----|----|
| `endpoints` | `string` | endpoints is the endpoint name that details Glusterfs topology. More info: <https://examples.k8s.io/volumes/glusterfs/README.md#create-a-pod> |
| `path` | `string` | path is the Glusterfs volume path. More info: <https://examples.k8s.io/volumes/glusterfs/README.md#create-a-pod> |
| `readOnly` | `boolean` | readOnly here will force the Glusterfs volume to be mounted with read-only permissions. Defaults to false. More info: <https://examples.k8s.io/volumes/glusterfs/README.md#create-a-pod> |

## .spec.install.spec.deployments\[\].spec.template.spec.volumes\[\].hostPath

Description
hostPath represents a pre-existing file or directory on the host machine that is directly exposed to the container. This is generally used for system agents or other privileged things that are allowed to see the host machine. Most containers will NOT need this. More info: <https://kubernetes.io/docs/concepts/storage/volumes#hostpath>

Type
`object`

Required
- `path`

| Property | Type | Description |
|----|----|----|
| `path` | `string` | path of the directory on the host. If the path is a symlink, it will follow the link to the real path. More info: <https://kubernetes.io/docs/concepts/storage/volumes#hostpath> |
| `type` | `string` | type for HostPath Volume Defaults to "" More info: <https://kubernetes.io/docs/concepts/storage/volumes#hostpath> |

## .spec.install.spec.deployments\[\].spec.template.spec.volumes\[\].image

Description
image represents an OCI object (a container image or artifact) pulled and mounted on the kubelet’s host machine. The volume is resolved at pod startup depending on which PullPolicy value is provided:

- Always: the kubelet always attempts to pull the reference. Container creation will fail If the pull fails.

- Never: the kubelet never pulls the reference and only uses a local image or artifact. Container creation will fail if the reference isn’t present.

- IfNotPresent: the kubelet pulls if the reference isn’t already present on disk. Container creation will fail if the reference isn’t present and the pull fails.

The volume gets re-resolved if the pod gets deleted and recreated, which means that new remote content will become available on pod recreation. A failure to resolve or pull the image during pod startup will block containers from starting and may add significant latency. Failures will be retried using normal volume backoff and will be reported on the pod reason and message. The types of objects that may be mounted by this volume are defined by the container runtime implementation on a host machine and at minimum must include all valid types supported by the container image field. The OCI object gets mounted in a single directory (spec.containers\[**\].volumeMounts.mountPath) by merging the manifest layers in the same way as for container images. The volume will be mounted read-only (ro) and non-executable files (noexec). Sub path mounts for containers are not supported (spec.containers\[**\].volumeMounts.subpath) before 1.33. The field spec.securityContext.fsGroupChangePolicy has no effect on this volume type.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `pullPolicy` | `string` | Policy for pulling OCI objects. Possible values are: Always: the kubelet always attempts to pull the reference. Container creation will fail If the pull fails. Never: the kubelet never pulls the reference and only uses a local image or artifact. Container creation will fail if the reference isn’t present. IfNotPresent: the kubelet pulls if the reference isn’t already present on disk. Container creation will fail if the reference isn’t present and the pull fails. Defaults to Always if :latest tag is specified, or IfNotPresent otherwise. |
| `reference` | `string` | Required: Image or artifact reference to be used. Behaves in the same way as pod.spec.containers\[\*\].image. Pull secrets will be assembled in the same way as for the container image by looking up node credentials, SA image pull secrets, and pod spec image pull secrets. More info: <https://kubernetes.io/docs/concepts/containers/images> This field is optional to allow higher level config management to default or override container images in workload controllers like Deployments and StatefulSets. |

## .spec.install.spec.deployments\[\].spec.template.spec.volumes\[\].iscsi

Description
iscsi represents an ISCSI Disk resource that is attached to a kubelet’s host machine and then exposed to the pod. More info: <https://examples.k8s.io/volumes/iscsi/README.md>

Type
`object`

Required
- `iqn`

- `lun`

- `targetPortal`

| Property | Type | Description |
|----|----|----|
| `chapAuthDiscovery` | `boolean` | chapAuthDiscovery defines whether support iSCSI Discovery CHAP authentication |
| `chapAuthSession` | `boolean` | chapAuthSession defines whether support iSCSI Session CHAP authentication |
| `fsType` | `string` | fsType is the filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: <https://kubernetes.io/docs/concepts/storage/volumes#iscsi> |
| `initiatorName` | `string` | initiatorName is the custom iSCSI Initiator Name. If initiatorName is specified with iscsiInterface simultaneously, new iSCSI interface \<target portal\>:\<volume name\> will be created for the connection. |
| `iqn` | `string` | iqn is the target iSCSI Qualified Name. |
| `iscsiInterface` | `string` | iscsiInterface is the interface Name that uses an iSCSI transport. Defaults to 'default' (tcp). |
| `lun` | `integer` | lun represents iSCSI Target Lun number. |
| `portals` | `array (string)` | portals is the iSCSI Target Portal List. The portal is either an IP or ip_addr:port if the port is other than default (typically TCP ports 860 and 3260). |
| `readOnly` | `boolean` | readOnly here will force the ReadOnly setting in VolumeMounts. Defaults to false. |
| `secretRef` | `object` | secretRef is the CHAP Secret for iSCSI target and initiator authentication |
| `targetPortal` | `string` | targetPortal is iSCSI Target Portal. The Portal is either an IP or ip_addr:port if the port is other than default (typically TCP ports 860 and 3260). |

## .spec.install.spec.deployments\[\].spec.template.spec.volumes\[\].iscsi.secretRef

Description
secretRef is the CHAP Secret for iSCSI target and initiator authentication

Type
`object`

| Property | Type | Description |
|----|----|----|
| `name` | `string` | Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names> |

## .spec.install.spec.deployments\[\].spec.template.spec.volumes\[\].nfs

Description
nfs represents an NFS mount on the host that shares a pod’s lifetime More info: <https://kubernetes.io/docs/concepts/storage/volumes#nfs>

Type
`object`

Required
- `path`

- `server`

| Property | Type | Description |
|----|----|----|
| `path` | `string` | path that is exported by the NFS server. More info: <https://kubernetes.io/docs/concepts/storage/volumes#nfs> |
| `readOnly` | `boolean` | readOnly here will force the NFS export to be mounted with read-only permissions. Defaults to false. More info: <https://kubernetes.io/docs/concepts/storage/volumes#nfs> |
| `server` | `string` | server is the hostname or IP address of the NFS server. More info: <https://kubernetes.io/docs/concepts/storage/volumes#nfs> |

## .spec.install.spec.deployments\[\].spec.template.spec.volumes\[\].persistentVolumeClaim

Description
persistentVolumeClaimVolumeSource represents a reference to a PersistentVolumeClaim in the same namespace. More info: <https://kubernetes.io/docs/concepts/storage/persistent-volumes#persistentvolumeclaims>

Type
`object`

Required
- `claimName`

| Property | Type | Description |
|----|----|----|
| `claimName` | `string` | claimName is the name of a PersistentVolumeClaim in the same namespace as the pod using this volume. More info: <https://kubernetes.io/docs/concepts/storage/persistent-volumes#persistentvolumeclaims> |
| `readOnly` | `boolean` | readOnly Will force the ReadOnly setting in VolumeMounts. Default false. |

## .spec.install.spec.deployments\[\].spec.template.spec.volumes\[\].photonPersistentDisk

Description
photonPersistentDisk represents a PhotonController persistent disk attached and mounted on kubelets host machine. Deprecated: PhotonPersistentDisk is deprecated and the in-tree photonPersistentDisk type is no longer supported.

Type
`object`

Required
- `pdID`

| Property | Type | Description |
|----|----|----|
| `fsType` | `string` | fsType is the filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. |
| `pdID` | `string` | pdID is the ID that identifies Photon Controller persistent disk |

## .spec.install.spec.deployments\[\].spec.template.spec.volumes\[\].portworxVolume

Description
portworxVolume represents a portworx volume attached and mounted on kubelets host machine. Deprecated: PortworxVolume is deprecated. All operations for the in-tree portworxVolume type are redirected to the pxd.portworx.com CSI driver when the CSIMigrationPortworx feature-gate is on.

Type
`object`

Required
- `volumeID`

| Property | Type | Description |
|----|----|----|
| `fsType` | `string` | fSType represents the filesystem type to mount Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs". Implicitly inferred to be "ext4" if unspecified. |
| `readOnly` | `boolean` | readOnly defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts. |
| `volumeID` | `string` | volumeID uniquely identifies a Portworx volume |

## .spec.install.spec.deployments\[\].spec.template.spec.volumes\[\].projected

Description
projected items for all in one resources secrets, configmaps, and downward API

Type
`object`

| Property | Type | Description |
|----|----|----|
| `defaultMode` | `integer` | defaultMode are the mode bits used to set permissions on created files by default. Must be an octal value between 0000 and 0777 or a decimal value between 0 and 511. YAML accepts both octal and decimal values, JSON requires decimal values for mode bits. Directories within the path are not affected by this setting. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set. |
| `sources` | `array` | sources is the list of volume projections. Each entry in this list handles one source. |
| `sources[]` | `object` | Projection that may be projected along with other supported volume types. Exactly one of these fields must be set. |

## .spec.install.spec.deployments\[\].spec.template.spec.volumes\[\].projected.sources

Description
sources is the list of volume projections. Each entry in this list handles one source.

Type
`array`

## .spec.install.spec.deployments\[\].spec.template.spec.volumes\[\].projected.sources\[\]

Description
Projection that may be projected along with other supported volume types. Exactly one of these fields must be set.

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
<td style="text-align: left;"><p><code>clusterTrustBundle</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>ClusterTrustBundle allows a pod to access the <code>.spec.trustBundle</code> field of ClusterTrustBundle objects in an auto-updating file.</p>
<p>Alpha, gated by the ClusterTrustBundleProjection feature gate.</p>
<p>ClusterTrustBundle objects can either be selected by name, or by the combination of signer name and a label selector.</p>
<p>Kubelet performs aggressive normalization of the PEM contents written into the pod filesystem. Esoteric PEM features such as inter-block comments and block headers are stripped. Certificates are deduplicated. The ordering of certificates within the file is arbitrary, and Kubelet may change the order over time.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>configMap</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>configMap information about the configMap data to project</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>downwardAPI</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>downwardAPI information about the downwardAPI data to project</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>secret</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>secret information about the secret data to project</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>serviceAccountToken</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>serviceAccountToken is information about the serviceAccountToken data to project</p></td>
</tr>
</tbody>
</table>

## .spec.install.spec.deployments\[\].spec.template.spec.volumes\[\].projected.sources\[\].clusterTrustBundle

Description
ClusterTrustBundle allows a pod to access the `.spec.trustBundle` field of ClusterTrustBundle objects in an auto-updating file.

Alpha, gated by the ClusterTrustBundleProjection feature gate.

ClusterTrustBundle objects can either be selected by name, or by the combination of signer name and a label selector.

Kubelet performs aggressive normalization of the PEM contents written into the pod filesystem. Esoteric PEM features such as inter-block comments and block headers are stripped. Certificates are deduplicated. The ordering of certificates within the file is arbitrary, and Kubelet may change the order over time.

Type
`object`

Required
- `path`

| Property | Type | Description |
|----|----|----|
| `labelSelector` | `object` | Select all ClusterTrustBundles that match this label selector. Only has effect if signerName is set. Mutually-exclusive with name. If unset, interpreted as "match nothing". If set but empty, interpreted as "match everything". |
| `name` | `string` | Select a single ClusterTrustBundle by object name. Mutually-exclusive with signerName and labelSelector. |
| `optional` | `boolean` | If true, don’t block pod startup if the referenced ClusterTrustBundle(s) aren’t available. If using name, then the named ClusterTrustBundle is allowed not to exist. If using signerName, then the combination of signerName and labelSelector is allowed to match zero ClusterTrustBundles. |
| `path` | `string` | Relative path from the volume root to write the bundle. |
| `signerName` | `string` | Select all ClusterTrustBundles that match this signer name. Mutually-exclusive with name. The contents of all selected ClusterTrustBundles will be unified and deduplicated. |

## .spec.install.spec.deployments\[\].spec.template.spec.volumes\[\].projected.sources\[\].clusterTrustBundle.labelSelector

Description
Select all ClusterTrustBundles that match this label selector. Only has effect if signerName is set. Mutually-exclusive with name. If unset, interpreted as "match nothing". If set but empty, interpreted as "match everything".

Type
`object`

| Property | Type | Description |
|----|----|----|
| `matchExpressions` | `array` | matchExpressions is a list of label selector requirements. The requirements are ANDed. |
| `matchExpressions[]` | `object` | A label selector requirement is a selector that contains values, a key, and an operator that relates the key and values. |
| `matchLabels` | `object (string)` | matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed. |

## .spec.install.spec.deployments\[\].spec.template.spec.volumes\[\].projected.sources\[\].clusterTrustBundle.labelSelector.matchExpressions

Description
matchExpressions is a list of label selector requirements. The requirements are ANDed.

Type
`array`

## .spec.install.spec.deployments\[\].spec.template.spec.volumes\[\].projected.sources\[\].clusterTrustBundle.labelSelector.matchExpressions\[\]

Description
A label selector requirement is a selector that contains values, a key, and an operator that relates the key and values.

Type
`object`

Required
- `key`

- `operator`

| Property | Type | Description |
|----|----|----|
| `key` | `string` | key is the label key that the selector applies to. |
| `operator` | `string` | operator represents a key’s relationship to a set of values. Valid operators are In, NotIn, Exists and DoesNotExist. |
| `values` | `array (string)` | values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch. |

## .spec.install.spec.deployments\[\].spec.template.spec.volumes\[\].projected.sources\[\].configMap

Description
configMap information about the configMap data to project

Type
`object`

| Property | Type | Description |
|----|----|----|
| `items` | `array` | items if unspecified, each key-value pair in the Data field of the referenced ConfigMap will be projected into the volume as a file whose name is the key and content is the value. If specified, the listed keys will be projected into the specified paths, and unlisted keys will not be present. If a key is specified which is not present in the ConfigMap, the volume setup will error unless it is marked optional. Paths must be relative and may not contain the '..' path or start with '..'. |
| `items[]` | `object` | Maps a string key to a path within a volume. |
| `name` | `string` | Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names> |
| `optional` | `boolean` | optional specify whether the ConfigMap or its keys must be defined |

## .spec.install.spec.deployments\[\].spec.template.spec.volumes\[\].projected.sources\[\].configMap.items

Description
items if unspecified, each key-value pair in the Data field of the referenced ConfigMap will be projected into the volume as a file whose name is the key and content is the value. If specified, the listed keys will be projected into the specified paths, and unlisted keys will not be present. If a key is specified which is not present in the ConfigMap, the volume setup will error unless it is marked optional. Paths must be relative and may not contain the '..' path or start with '..'.

Type
`array`

## .spec.install.spec.deployments\[\].spec.template.spec.volumes\[\].projected.sources\[\].configMap.items\[\]

Description
Maps a string key to a path within a volume.

Type
`object`

Required
- `key`

- `path`

| Property | Type | Description |
|----|----|----|
| `key` | `string` | key is the key to project. |
| `mode` | `integer` | mode is Optional: mode bits used to set permissions on this file. Must be an octal value between 0000 and 0777 or a decimal value between 0 and 511. YAML accepts both octal and decimal values, JSON requires decimal values for mode bits. If not specified, the volume defaultMode will be used. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set. |
| `path` | `string` | path is the relative path of the file to map the key to. May not be an absolute path. May not contain the path element '..'. May not start with the string '..'. |

## .spec.install.spec.deployments\[\].spec.template.spec.volumes\[\].projected.sources\[\].downwardAPI

Description
downwardAPI information about the downwardAPI data to project

Type
`object`

| Property | Type | Description |
|----|----|----|
| `items` | `array` | Items is a list of DownwardAPIVolume file |
| `items[]` | `object` | DownwardAPIVolumeFile represents information to create the file containing the pod field |

## .spec.install.spec.deployments\[\].spec.template.spec.volumes\[\].projected.sources\[\].downwardAPI.items

Description
Items is a list of DownwardAPIVolume file

Type
`array`

## .spec.install.spec.deployments\[\].spec.template.spec.volumes\[\].projected.sources\[\].downwardAPI.items\[\]

Description
DownwardAPIVolumeFile represents information to create the file containing the pod field

Type
`object`

Required
- `path`

| Property | Type | Description |
|----|----|----|
| `fieldRef` | `object` | Required: Selects a field of the pod: only annotations, labels, name, namespace and uid are supported. |
| `mode` | `integer` | Optional: mode bits used to set permissions on this file, must be an octal value between 0000 and 0777 or a decimal value between 0 and 511. YAML accepts both octal and decimal values, JSON requires decimal values for mode bits. If not specified, the volume defaultMode will be used. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set. |
| `path` | `string` | Required: Path is the relative path name of the file to be created. Must not be absolute or contain the '..' path. Must be utf-8 encoded. The first item of the relative path must not start with '..' |
| `resourceFieldRef` | `object` | Selects a resource of the container: only resources limits and requests (limits.cpu, limits.memory, requests.cpu and requests.memory) are currently supported. |

## .spec.install.spec.deployments\[\].spec.template.spec.volumes\[\].projected.sources\[\].downwardAPI.items\[\].fieldRef

Description
Required: Selects a field of the pod: only annotations, labels, name, namespace and uid are supported.

Type
`object`

Required
- `fieldPath`

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | Version of the schema the FieldPath is written in terms of, defaults to "v1". |
| `fieldPath` | `string` | Path of the field to select in the specified API version. |

## .spec.install.spec.deployments\[\].spec.template.spec.volumes\[\].projected.sources\[\].downwardAPI.items\[\].resourceFieldRef

Description
Selects a resource of the container: only resources limits and requests (limits.cpu, limits.memory, requests.cpu and requests.memory) are currently supported.

Type
`object`

Required
- `resource`

| Property | Type | Description |
|----|----|----|
| `containerName` | `string` | Container name: required for volumes, optional for env vars |
| `divisor` | `integer-or-string` | Specifies the output format of the exposed resources, defaults to "1" |
| `resource` | `string` | Required: resource to select |

## .spec.install.spec.deployments\[\].spec.template.spec.volumes\[\].projected.sources\[\].secret

Description
secret information about the secret data to project

Type
`object`

| Property | Type | Description |
|----|----|----|
| `items` | `array` | items if unspecified, each key-value pair in the Data field of the referenced Secret will be projected into the volume as a file whose name is the key and content is the value. If specified, the listed keys will be projected into the specified paths, and unlisted keys will not be present. If a key is specified which is not present in the Secret, the volume setup will error unless it is marked optional. Paths must be relative and may not contain the '..' path or start with '..'. |
| `items[]` | `object` | Maps a string key to a path within a volume. |
| `name` | `string` | Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names> |
| `optional` | `boolean` | optional field specify whether the Secret or its key must be defined |

## .spec.install.spec.deployments\[\].spec.template.spec.volumes\[\].projected.sources\[\].secret.items

Description
items if unspecified, each key-value pair in the Data field of the referenced Secret will be projected into the volume as a file whose name is the key and content is the value. If specified, the listed keys will be projected into the specified paths, and unlisted keys will not be present. If a key is specified which is not present in the Secret, the volume setup will error unless it is marked optional. Paths must be relative and may not contain the '..' path or start with '..'.

Type
`array`

## .spec.install.spec.deployments\[\].spec.template.spec.volumes\[\].projected.sources\[\].secret.items\[\]

Description
Maps a string key to a path within a volume.

Type
`object`

Required
- `key`

- `path`

| Property | Type | Description |
|----|----|----|
| `key` | `string` | key is the key to project. |
| `mode` | `integer` | mode is Optional: mode bits used to set permissions on this file. Must be an octal value between 0000 and 0777 or a decimal value between 0 and 511. YAML accepts both octal and decimal values, JSON requires decimal values for mode bits. If not specified, the volume defaultMode will be used. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set. |
| `path` | `string` | path is the relative path of the file to map the key to. May not be an absolute path. May not contain the path element '..'. May not start with the string '..'. |

## .spec.install.spec.deployments\[\].spec.template.spec.volumes\[\].projected.sources\[\].serviceAccountToken

Description
serviceAccountToken is information about the serviceAccountToken data to project

Type
`object`

Required
- `path`

| Property | Type | Description |
|----|----|----|
| `audience` | `string` | audience is the intended audience of the token. A recipient of a token must identify itself with an identifier specified in the audience of the token, and otherwise should reject the token. The audience defaults to the identifier of the apiserver. |
| `expirationSeconds` | `integer` | expirationSeconds is the requested duration of validity of the service account token. As the token approaches expiration, the kubelet volume plugin will proactively rotate the service account token. The kubelet will start trying to rotate the token if the token is older than 80 percent of its time to live or if the token is older than 24 hours.Defaults to 1 hour and must be at least 10 minutes. |
| `path` | `string` | path is the path relative to the mount point of the file to project the token into. |

## .spec.install.spec.deployments\[\].spec.template.spec.volumes\[\].quobyte

Description
quobyte represents a Quobyte mount on the host that shares a pod’s lifetime. Deprecated: Quobyte is deprecated and the in-tree quobyte type is no longer supported.

Type
`object`

Required
- `registry`

- `volume`

| Property | Type | Description |
|----|----|----|
| `group` | `string` | group to map volume access to Default is no group |
| `readOnly` | `boolean` | readOnly here will force the Quobyte volume to be mounted with read-only permissions. Defaults to false. |
| `registry` | `string` | registry represents a single or multiple Quobyte Registry services specified as a string as host:port pair (multiple entries are separated with commas) which acts as the central registry for volumes |
| `tenant` | `string` | tenant owning the given Quobyte volume in the Backend Used with dynamically provisioned Quobyte volumes, value is set by the plugin |
| `user` | `string` | user to map volume access to Defaults to serivceaccount user |
| `volume` | `string` | volume is a string that references an already created Quobyte volume by name. |

## .spec.install.spec.deployments\[\].spec.template.spec.volumes\[\].rbd

Description
rbd represents a Rados Block Device mount on the host that shares a pod’s lifetime. Deprecated: RBD is deprecated and the in-tree rbd type is no longer supported. More info: <https://examples.k8s.io/volumes/rbd/README.md>

Type
`object`

Required
- `image`

- `monitors`

| Property | Type | Description |
|----|----|----|
| `fsType` | `string` | fsType is the filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: <https://kubernetes.io/docs/concepts/storage/volumes#rbd> |
| `image` | `string` | image is the rados image name. More info: <https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it> |
| `keyring` | `string` | keyring is the path to key ring for RBDUser. Default is /etc/ceph/keyring. More info: <https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it> |
| `monitors` | `array (string)` | monitors is a collection of Ceph monitors. More info: <https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it> |
| `pool` | `string` | pool is the rados pool name. Default is rbd. More info: <https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it> |
| `readOnly` | `boolean` | readOnly here will force the ReadOnly setting in VolumeMounts. Defaults to false. More info: <https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it> |
| `secretRef` | `object` | secretRef is name of the authentication secret for RBDUser. If provided overrides keyring. Default is nil. More info: <https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it> |
| `user` | `string` | user is the rados user name. Default is admin. More info: <https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it> |

## .spec.install.spec.deployments\[\].spec.template.spec.volumes\[\].rbd.secretRef

Description
secretRef is name of the authentication secret for RBDUser. If provided overrides keyring. Default is nil. More info: <https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it>

Type
`object`

| Property | Type | Description |
|----|----|----|
| `name` | `string` | Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names> |

## .spec.install.spec.deployments\[\].spec.template.spec.volumes\[\].scaleIO

Description
scaleIO represents a ScaleIO persistent volume attached and mounted on Kubernetes nodes. Deprecated: ScaleIO is deprecated and the in-tree scaleIO type is no longer supported.

Type
`object`

Required
- `gateway`

- `secretRef`

- `system`

| Property | Type | Description |
|----|----|----|
| `fsType` | `string` | fsType is the filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Default is "xfs". |
| `gateway` | `string` | gateway is the host address of the ScaleIO API Gateway. |
| `protectionDomain` | `string` | protectionDomain is the name of the ScaleIO Protection Domain for the configured storage. |
| `readOnly` | `boolean` | readOnly Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts. |
| `secretRef` | `object` | secretRef references to the secret for ScaleIO user and other sensitive information. If this is not provided, Login operation will fail. |
| `sslEnabled` | `boolean` | sslEnabled Flag enable/disable SSL communication with Gateway, default false |
| `storageMode` | `string` | storageMode indicates whether the storage for a volume should be ThickProvisioned or ThinProvisioned. Default is ThinProvisioned. |
| `storagePool` | `string` | storagePool is the ScaleIO Storage Pool associated with the protection domain. |
| `system` | `string` | system is the name of the storage system as configured in ScaleIO. |
| `volumeName` | `string` | volumeName is the name of a volume already created in the ScaleIO system that is associated with this volume source. |

## .spec.install.spec.deployments\[\].spec.template.spec.volumes\[\].scaleIO.secretRef

Description
secretRef references to the secret for ScaleIO user and other sensitive information. If this is not provided, Login operation will fail.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `name` | `string` | Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names> |

## .spec.install.spec.deployments\[\].spec.template.spec.volumes\[\].secret

Description
secret represents a secret that should populate this volume. More info: <https://kubernetes.io/docs/concepts/storage/volumes#secret>

Type
`object`

| Property | Type | Description |
|----|----|----|
| `defaultMode` | `integer` | defaultMode is Optional: mode bits used to set permissions on created files by default. Must be an octal value between 0000 and 0777 or a decimal value between 0 and 511. YAML accepts both octal and decimal values, JSON requires decimal values for mode bits. Defaults to 0644. Directories within the path are not affected by this setting. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set. |
| `items` | `array` | items If unspecified, each key-value pair in the Data field of the referenced Secret will be projected into the volume as a file whose name is the key and content is the value. If specified, the listed keys will be projected into the specified paths, and unlisted keys will not be present. If a key is specified which is not present in the Secret, the volume setup will error unless it is marked optional. Paths must be relative and may not contain the '..' path or start with '..'. |
| `items[]` | `object` | Maps a string key to a path within a volume. |
| `optional` | `boolean` | optional field specify whether the Secret or its keys must be defined |
| `secretName` | `string` | secretName is the name of the secret in the pod’s namespace to use. More info: <https://kubernetes.io/docs/concepts/storage/volumes#secret> |

## .spec.install.spec.deployments\[\].spec.template.spec.volumes\[\].secret.items

Description
items If unspecified, each key-value pair in the Data field of the referenced Secret will be projected into the volume as a file whose name is the key and content is the value. If specified, the listed keys will be projected into the specified paths, and unlisted keys will not be present. If a key is specified which is not present in the Secret, the volume setup will error unless it is marked optional. Paths must be relative and may not contain the '..' path or start with '..'.

Type
`array`

## .spec.install.spec.deployments\[\].spec.template.spec.volumes\[\].secret.items\[\]

Description
Maps a string key to a path within a volume.

Type
`object`

Required
- `key`

- `path`

| Property | Type | Description |
|----|----|----|
| `key` | `string` | key is the key to project. |
| `mode` | `integer` | mode is Optional: mode bits used to set permissions on this file. Must be an octal value between 0000 and 0777 or a decimal value between 0 and 511. YAML accepts both octal and decimal values, JSON requires decimal values for mode bits. If not specified, the volume defaultMode will be used. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set. |
| `path` | `string` | path is the relative path of the file to map the key to. May not be an absolute path. May not contain the path element '..'. May not start with the string '..'. |

## .spec.install.spec.deployments\[\].spec.template.spec.volumes\[\].storageos

Description
storageOS represents a StorageOS volume attached and mounted on Kubernetes nodes. Deprecated: StorageOS is deprecated and the in-tree storageos type is no longer supported.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `fsType` | `string` | fsType is the filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. |
| `readOnly` | `boolean` | readOnly defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts. |
| `secretRef` | `object` | secretRef specifies the secret to use for obtaining the StorageOS API credentials. If not specified, default values will be attempted. |
| `volumeName` | `string` | volumeName is the human-readable name of the StorageOS volume. Volume names are only unique within a namespace. |
| `volumeNamespace` | `string` | volumeNamespace specifies the scope of the volume within StorageOS. If no namespace is specified then the Pod’s namespace will be used. This allows the Kubernetes name scoping to be mirrored within StorageOS for tighter integration. Set VolumeName to any name to override the default behaviour. Set to "default" if you are not using namespaces within StorageOS. Namespaces that do not pre-exist within StorageOS will be created. |

## .spec.install.spec.deployments\[\].spec.template.spec.volumes\[\].storageos.secretRef

Description
secretRef specifies the secret to use for obtaining the StorageOS API credentials. If not specified, default values will be attempted.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `name` | `string` | Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names> |

## .spec.install.spec.deployments\[\].spec.template.spec.volumes\[\].vsphereVolume

Description
vsphereVolume represents a vSphere volume attached and mounted on kubelets host machine. Deprecated: VsphereVolume is deprecated. All operations for the in-tree vsphereVolume type are redirected to the csi.vsphere.vmware.com CSI driver.

Type
`object`

Required
- `volumePath`

| Property | Type | Description |
|----|----|----|
| `fsType` | `string` | fsType is filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. |
| `storagePolicyID` | `string` | storagePolicyID is the storage Policy Based Management (SPBM) profile ID associated with the StoragePolicyName. |
| `storagePolicyName` | `string` | storagePolicyName is the storage Policy Based Management (SPBM) profile name. |
| `volumePath` | `string` | volumePath is the path that identifies vSphere volume vmdk |

## .spec.install.spec.permissions

Description

Type
`array`

## .spec.install.spec.permissions\[\]

Description
StrategyDeploymentPermissions describe the rbac rules and service account needed by the install strategy

Type
`object`

Required
- `rules`

- `serviceAccountName`

| Property | Type | Description |
|----|----|----|
| `rules` | `array` |  |
| `rules[]` | `object` | PolicyRule holds information that describes a policy rule, but does not contain information about who the rule applies to or which namespace the rule applies to. |
| `serviceAccountName` | `string` |  |

## .spec.install.spec.permissions\[\].rules

Description

Type
`array`

## .spec.install.spec.permissions\[\].rules\[\]

Description
PolicyRule holds information that describes a policy rule, but does not contain information about who the rule applies to or which namespace the rule applies to.

Type
`object`

Required
- `verbs`

| Property | Type | Description |
|----|----|----|
| `apiGroups` | `array (string)` | APIGroups is the name of the APIGroup that contains the resources. If multiple API groups are specified, any action requested against one of the enumerated resources in any API group will be allowed. "" represents the core API group and "\*" represents all API groups. |
| `nonResourceURLs` | `array (string)` | NonResourceURLs is a set of partial urls that a user should have access to. \*s are allowed, but only as the full, final step in the path Since non-resource URLs are not namespaced, this field is only applicable for ClusterRoles referenced from a ClusterRoleBinding. Rules can either apply to API resources (such as "pods" or "secrets") or non-resource URL paths (such as "/api"), but not both. |
| `resourceNames` | `array (string)` | ResourceNames is an optional white list of names that the rule applies to. An empty set means that everything is allowed. |
| `resources` | `array (string)` | Resources is a list of resources this rule applies to. '\*' represents all resources. |
| `verbs` | `array (string)` | Verbs is a list of Verbs that apply to ALL the ResourceKinds contained in this rule. '\*' represents all verbs. |

## .spec.installModes

Description
InstallModes specify supported installation types

Type
`array`

## .spec.installModes\[\]

Description
InstallMode associates an InstallModeType with a flag representing if the CSV supports it

Type
`object`

Required
- `supported`

- `type`

| Property | Type | Description |
|----|----|----|
| `supported` | `boolean` |  |
| `type` | `string` | InstallModeType is a supported type of install mode for CSV installation |

## .spec.links

Description
A list of links related to the operator.

Type
`array`

## .spec.links\[\]

Description

Type
`object`

| Property | Type     | Description |
|----------|----------|-------------|
| `name`   | `string` |             |
| `url`    | `string` |             |

## .spec.maintainers

Description
A list of organizational entities maintaining the operator.

Type
`array`

## .spec.maintainers\[\]

Description

Type
`object`

| Property | Type     | Description |
|----------|----------|-------------|
| `email`  | `string` |             |
| `name`   | `string` |             |

## .spec.nativeAPIs

Description

Type
`array`

## .spec.nativeAPIs\[\]

Description
GroupVersionKind unambiguously identifies a kind. It doesn’t anonymously include GroupVersion to avoid automatic coercion. It doesn’t use a GroupVersion to avoid custom marshalling

Type
`object`

Required
- `group`

- `kind`

- `version`

| Property  | Type     | Description |
|-----------|----------|-------------|
| `group`   | `string` |             |
| `kind`    | `string` |             |
| `version` | `string` |             |

## .spec.provider

Description
The publishing entity behind the operator.

Type
`object`

| Property | Type     | Description |
|----------|----------|-------------|
| `name`   | `string` |             |
| `url`    | `string` |             |

## .spec.relatedImages

Description
List any related images, or other container images that your Operator might require to perform their functions. This list should also include operand images as well. All image references should be specified by digest (SHA) and not by tag. This field is only used during catalog creation and plays no part in cluster runtime.

Type
`array`

## .spec.relatedImages\[\]

Description

Type
`object`

Required
- `image`

- `name`

| Property | Type     | Description |
|----------|----------|-------------|
| `image`  | `string` |             |
| `name`   | `string` |             |

## .spec.selector

Description
Label selector for related resources.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `matchExpressions` | `array` | matchExpressions is a list of label selector requirements. The requirements are ANDed. |
| `matchExpressions[]` | `object` | A label selector requirement is a selector that contains values, a key, and an operator that relates the key and values. |
| `matchLabels` | `object (string)` | matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed. |

## .spec.selector.matchExpressions

Description
matchExpressions is a list of label selector requirements. The requirements are ANDed.

Type
`array`

## .spec.selector.matchExpressions\[\]

Description
A label selector requirement is a selector that contains values, a key, and an operator that relates the key and values.

Type
`object`

Required
- `key`

- `operator`

| Property | Type | Description |
|----|----|----|
| `key` | `string` | key is the label key that the selector applies to. |
| `operator` | `string` | operator represents a key’s relationship to a set of values. Valid operators are In, NotIn, Exists and DoesNotExist. |
| `values` | `array (string)` | values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch. |

## .spec.webhookdefinitions

Description

Type
`array`

## .spec.webhookdefinitions\[\]

Description
WebhookDescription provides details to OLM about required webhooks

Type
`object`

Required
- `admissionReviewVersions`

- `generateName`

- `sideEffects`

- `type`

| Property | Type | Description |
|----|----|----|
| `admissionReviewVersions` | `array (string)` |  |
| `containerPort` | `integer` |  |
| `conversionCRDs` | `array (string)` |  |
| `deploymentName` | `string` |  |
| `failurePolicy` | `string` | FailurePolicyType specifies a failure policy that defines how unrecognized errors from the admission endpoint are handled. |
| `generateName` | `string` |  |
| `matchPolicy` | `string` | MatchPolicyType specifies the type of match policy. |
| `objectSelector` | `object` | A label selector is a label query over a set of resources. The result of matchLabels and matchExpressions are ANDed. An empty label selector matches all objects. A null label selector matches no objects. |
| `reinvocationPolicy` | `string` | ReinvocationPolicyType specifies what type of policy the admission hook uses. |
| `rules` | `array` |  |
| `rules[]` | `object` | RuleWithOperations is a tuple of Operations and Resources. It is recommended to make sure that all the tuple expansions are valid. |
| `sideEffects` | `string` | SideEffectClass specifies the types of side effects a webhook may have. |
| `targetPort` | `integer-or-string` |  |
| `timeoutSeconds` | `integer` |  |
| `type` | `string` | WebhookAdmissionType is the type of admission webhooks supported by OLM |
| `webhookPath` | `string` |  |

## .spec.webhookdefinitions\[\].objectSelector

Description
A label selector is a label query over a set of resources. The result of matchLabels and matchExpressions are ANDed. An empty label selector matches all objects. A null label selector matches no objects.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `matchExpressions` | `array` | matchExpressions is a list of label selector requirements. The requirements are ANDed. |
| `matchExpressions[]` | `object` | A label selector requirement is a selector that contains values, a key, and an operator that relates the key and values. |
| `matchLabels` | `object (string)` | matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed. |

## .spec.webhookdefinitions\[\].objectSelector.matchExpressions

Description
matchExpressions is a list of label selector requirements. The requirements are ANDed.

Type
`array`

## .spec.webhookdefinitions\[\].objectSelector.matchExpressions\[\]

Description
A label selector requirement is a selector that contains values, a key, and an operator that relates the key and values.

Type
`object`

Required
- `key`

- `operator`

| Property | Type | Description |
|----|----|----|
| `key` | `string` | key is the label key that the selector applies to. |
| `operator` | `string` | operator represents a key’s relationship to a set of values. Valid operators are In, NotIn, Exists and DoesNotExist. |
| `values` | `array (string)` | values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch. |

## .spec.webhookdefinitions\[\].rules

Description

Type
`array`

## .spec.webhookdefinitions\[\].rules\[\]

Description
RuleWithOperations is a tuple of Operations and Resources. It is recommended to make sure that all the tuple expansions are valid.

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
<td style="text-align: left;"><p><code>apiGroups</code></p></td>
<td style="text-align: left;"><p><code>array (string)</code></p></td>
<td style="text-align: left;"><p>APIGroups is the API groups the resources belong to. '<strong>' is all groups. If '</strong>' is present, the length of the slice must be one. Required.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>apiVersions</code></p></td>
<td style="text-align: left;"><p><code>array (string)</code></p></td>
<td style="text-align: left;"><p>APIVersions is the API versions the resources belong to. '<strong>' is all versions. If '</strong>' is present, the length of the slice must be one. Required.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>operations</code></p></td>
<td style="text-align: left;"><p><code>array (string)</code></p></td>
<td style="text-align: left;"><p>Operations is the operations the admission hook cares about - CREATE, UPDATE, DELETE, CONNECT or * for all of those operations and any future admission operations that are added. If '*' is present, the length of the slice must be one. Required.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>resources</code></p></td>
<td style="text-align: left;"><p><code>array (string)</code></p></td>
<td style="text-align: left;"><p>Resources is a list of resources this rule applies to.</p>
<p>For example: 'pods' means pods. 'pods/log' means the log subresource of pods. '<strong>' means all resources, but not subresources. 'pods/</strong>' means all subresources of pods. '<strong>/scale' means all scale subresources. '</strong>/*' means all resources and their subresources.</p>
<p>If wildcard is present, the validation rule will ensure resources do not overlap with each other.</p>
<p>Depending on the enclosing object, subresources might not be allowed. Required.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>scope</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>scope specifies the scope of this rule. Valid values are "Cluster", "Namespaced", and "<strong>" "Cluster" means that only cluster-scoped resources will match this rule. Namespace API objects are cluster-scoped. "Namespaced" means that only namespaced resources will match this rule. "</strong>" means that there are no scope restrictions. Subresources match the scope of their parent resource. Default is "*".</p></td>
</tr>
</tbody>
</table>

## .status

Description
ClusterServiceVersionStatus represents information about the status of a CSV. Status may trail the actual state of a system.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `certsLastUpdated` | `string` | Last time the owned APIService certs were updated |
| `certsRotateAt` | `string` | Time the owned APIService certs will rotate next |
| `cleanup` | `object` | CleanupStatus represents information about the status of cleanup while a CSV is pending deletion |
| `conditions` | `array` | List of conditions, a history of state transitions |
| `conditions[]` | `object` | Conditions appear in the status as a record of state transitions on the ClusterServiceVersion |
| `lastTransitionTime` | `string` | Last time the status transitioned from one status to another. |
| `lastUpdateTime` | `string` | Last time we updated the status |
| `message` | `string` | A human readable message indicating details about why the ClusterServiceVersion is in this condition. |
| `phase` | `string` | Current condition of the ClusterServiceVersion |
| `reason` | `string` | A brief CamelCase message indicating details about why the ClusterServiceVersion is in this state. e.g. 'RequirementsNotMet' |
| `requirementStatus` | `array` | The status of each requirement for this CSV |
| `requirementStatus[]` | `object` |  |

## .status.cleanup

Description
CleanupStatus represents information about the status of cleanup while a CSV is pending deletion

Type
`object`

| Property | Type | Description |
|----|----|----|
| `pendingDeletion` | `array` | PendingDeletion is the list of custom resource objects that are pending deletion and blocked on finalizers. This indicates the progress of cleanup that is blocking CSV deletion or operator uninstall. |
| `pendingDeletion[]` | `object` | ResourceList represents a list of resources which are of the same Group/Kind |

## .status.cleanup.pendingDeletion

Description
PendingDeletion is the list of custom resource objects that are pending deletion and blocked on finalizers. This indicates the progress of cleanup that is blocking CSV deletion or operator uninstall.

Type
`array`

## .status.cleanup.pendingDeletion\[\]

Description
ResourceList represents a list of resources which are of the same Group/Kind

Type
`object`

Required
- `group`

- `instances`

- `kind`

| Property      | Type     | Description |
|---------------|----------|-------------|
| `group`       | `string` |             |
| `instances`   | `array`  |             |
| `instances[]` | `object` |             |
| `kind`        | `string` |             |

## .status.cleanup.pendingDeletion\[\].instances

Description

Type
`array`

## .status.cleanup.pendingDeletion\[\].instances\[\]

Description

Type
`object`

Required
- `name`

| Property    | Type     | Description                                         |
|-------------|----------|-----------------------------------------------------|
| `name`      | `string` |                                                     |
| `namespace` | `string` | Namespace can be empty for cluster-scoped resources |

## .status.conditions

Description
List of conditions, a history of state transitions

Type
`array`

## .status.conditions\[\]

Description
Conditions appear in the status as a record of state transitions on the ClusterServiceVersion

Type
`object`

| Property | Type | Description |
|----|----|----|
| `lastTransitionTime` | `string` | Last time the status transitioned from one status to another. |
| `lastUpdateTime` | `string` | Last time we updated the status |
| `message` | `string` | A human readable message indicating details about why the ClusterServiceVersion is in this condition. |
| `phase` | `string` | Condition of the ClusterServiceVersion |
| `reason` | `string` | A brief CamelCase message indicating details about why the ClusterServiceVersion is in this state. e.g. 'RequirementsNotMet' |

## .status.requirementStatus

Description
The status of each requirement for this CSV

Type
`array`

## .status.requirementStatus\[\]

Description

Type
`object`

Required
- `group`

- `kind`

- `message`

- `name`

- `status`

- `version`

| Property | Type | Description |
|----|----|----|
| `dependents` | `array` |  |
| `dependents[]` | `object` | DependentStatus is the status for a dependent requirement (to prevent infinite nesting) |
| `group` | `string` |  |
| `kind` | `string` |  |
| `message` | `string` |  |
| `name` | `string` |  |
| `status` | `string` | StatusReason is a camelcased reason for the status of a RequirementStatus or DependentStatus |
| `uuid` | `string` |  |
| `version` | `string` |  |

## .status.requirementStatus\[\].dependents

Description

Type
`array`

## .status.requirementStatus\[\].dependents\[\]

Description
DependentStatus is the status for a dependent requirement (to prevent infinite nesting)

Type
`object`

Required
- `group`

- `kind`

- `status`

- `version`

| Property | Type | Description |
|----|----|----|
| `group` | `string` |  |
| `kind` | `string` |  |
| `message` | `string` |  |
| `status` | `string` | StatusReason is a camelcased reason for the status of a RequirementStatus or DependentStatus |
| `uuid` | `string` |  |
| `version` | `string` |  |

# API endpoints

The following API endpoints are available:

- `/apis/operators.coreos.com/v1alpha1/clusterserviceversions`

  - `GET`: list objects of kind ClusterServiceVersion

- `/apis/operators.coreos.com/v1alpha1/namespaces/{namespace}/clusterserviceversions`

  - `DELETE`: delete collection of ClusterServiceVersion

  - `GET`: list objects of kind ClusterServiceVersion

  - `POST`: create a ClusterServiceVersion

- `/apis/operators.coreos.com/v1alpha1/namespaces/{namespace}/clusterserviceversions/{name}`

  - `DELETE`: delete a ClusterServiceVersion

  - `GET`: read the specified ClusterServiceVersion

  - `PATCH`: partially update the specified ClusterServiceVersion

  - `PUT`: replace the specified ClusterServiceVersion

- `/apis/operators.coreos.com/v1alpha1/namespaces/{namespace}/clusterserviceversions/{name}/status`

  - `GET`: read status of the specified ClusterServiceVersion

  - `PATCH`: partially update status of the specified ClusterServiceVersion

  - `PUT`: replace status of the specified ClusterServiceVersion

## /apis/operators.coreos.com/v1alpha1/clusterserviceversions

HTTP method
`GET`

Description
list objects of kind ClusterServiceVersion

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ClusterServiceVersionList`](../objects/index.md#com-coreos-operators-v1alpha1-ClusterServiceVersionList) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/operators.coreos.com/v1alpha1/namespaces/{namespace}/clusterserviceversions

HTTP method
`DELETE`

Description
delete collection of ClusterServiceVersion

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Status`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`GET`

Description
list objects of kind ClusterServiceVersion

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ClusterServiceVersionList`](../objects/index.md#com-coreos-operators-v1alpha1-ClusterServiceVersionList) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`POST`

Description
create a ClusterServiceVersion

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`ClusterServiceVersion`](clusterserviceversion-operators-coreos-com-v1alpha1.md#clusterserviceversion-operators-coreos-com-v1alpha1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ClusterServiceVersion`](clusterserviceversion-operators-coreos-com-v1alpha1.md#clusterserviceversion-operators-coreos-com-v1alpha1) schema |
| 201 - Created | [`ClusterServiceVersion`](clusterserviceversion-operators-coreos-com-v1alpha1.md#clusterserviceversion-operators-coreos-com-v1alpha1) schema |
| 202 - Accepted | [`ClusterServiceVersion`](clusterserviceversion-operators-coreos-com-v1alpha1.md#clusterserviceversion-operators-coreos-com-v1alpha1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/operators.coreos.com/v1alpha1/namespaces/{namespace}/clusterserviceversions/{name}

| Parameter | Type     | Description                       |
|-----------|----------|-----------------------------------|
| `name`    | `string` | name of the ClusterServiceVersion |

Global path parameters

HTTP method
`DELETE`

Description
delete a ClusterServiceVersion

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
read the specified ClusterServiceVersion

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ClusterServiceVersion`](clusterserviceversion-operators-coreos-com-v1alpha1.md#clusterserviceversion-operators-coreos-com-v1alpha1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PATCH`

Description
partially update the specified ClusterServiceVersion

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ClusterServiceVersion`](clusterserviceversion-operators-coreos-com-v1alpha1.md#clusterserviceversion-operators-coreos-com-v1alpha1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PUT`

Description
replace the specified ClusterServiceVersion

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`ClusterServiceVersion`](clusterserviceversion-operators-coreos-com-v1alpha1.md#clusterserviceversion-operators-coreos-com-v1alpha1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ClusterServiceVersion`](clusterserviceversion-operators-coreos-com-v1alpha1.md#clusterserviceversion-operators-coreos-com-v1alpha1) schema |
| 201 - Created | [`ClusterServiceVersion`](clusterserviceversion-operators-coreos-com-v1alpha1.md#clusterserviceversion-operators-coreos-com-v1alpha1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/operators.coreos.com/v1alpha1/namespaces/{namespace}/clusterserviceversions/{name}/status

| Parameter | Type     | Description                       |
|-----------|----------|-----------------------------------|
| `name`    | `string` | name of the ClusterServiceVersion |

Global path parameters

HTTP method
`GET`

Description
read status of the specified ClusterServiceVersion

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ClusterServiceVersion`](clusterserviceversion-operators-coreos-com-v1alpha1.md#clusterserviceversion-operators-coreos-com-v1alpha1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PATCH`

Description
partially update status of the specified ClusterServiceVersion

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ClusterServiceVersion`](clusterserviceversion-operators-coreos-com-v1alpha1.md#clusterserviceversion-operators-coreos-com-v1alpha1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PUT`

Description
replace status of the specified ClusterServiceVersion

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`ClusterServiceVersion`](clusterserviceversion-operators-coreos-com-v1alpha1.md#clusterserviceversion-operators-coreos-com-v1alpha1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ClusterServiceVersion`](clusterserviceversion-operators-coreos-com-v1alpha1.md#clusterserviceversion-operators-coreos-com-v1alpha1) schema |
| 201 - Created | [`ClusterServiceVersion`](clusterserviceversion-operators-coreos-com-v1alpha1.md#clusterserviceversion-operators-coreos-com-v1alpha1) schema |
| 401 - Unauthorized | Empty |

HTTP responses
