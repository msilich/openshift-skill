<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Description
ClusterExtension is the Schema for the clusterextensions API

Type
`object`

# Specification

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ObjectMeta`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) | Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |
| `spec` | `object` | spec is an optional field that defines the desired state of the ClusterExtension. |
| `status` | `object` | status is an optional field that defines the observed state of the ClusterExtension. |

## .spec

Description
spec is an optional field that defines the desired state of the ClusterExtension.

Type
`object`

Required
- `namespace`

- `serviceAccount`

- `source`

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
<td style="text-align: left;"><p><code>install</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>install is an optional field used to configure the installation options for the ClusterExtension such as the pre-flight check configuration.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>namespace</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>namespace is a reference to a Kubernetes namespace. This is the namespace in which the provided ServiceAccount must exist. It also designates the default namespace where namespace-scoped resources for the extension are applied to the cluster. Some extensions may contain namespace-scoped resources to be applied in other namespaces. This namespace must exist.</p>
<p>namespace is required, immutable, and follows the DNS label standard as defined in [RFC 1123]. It must contain only lowercase alphanumeric characters or hyphens (-), start and end with an alphanumeric character, and be no longer than 63 characters</p>
<p>[RFC 1123]: <a href="https://tools.ietf.org/html/rfc1123">https://tools.ietf.org/html/rfc1123</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>serviceAccount</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>serviceAccount is a reference to a ServiceAccount used to perform all interactions with the cluster that are required to manage the extension. The ServiceAccount must be configured with the necessary permissions to perform these interactions. The ServiceAccount must exist in the namespace referenced in the spec. serviceAccount is required.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>source</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>source is a required field which selects the installation source of content for this ClusterExtension. Selection is performed by setting the sourceType.</p>
<p>Catalog is currently the only implemented sourceType, and setting the sourcetype to "Catalog" requires the catalog field to also be defined.</p>
<p>Below is a minimal example of a source definition (in yaml):</p>
<p>source: sourceType: Catalog catalog: packageName: example-package</p></td>
</tr>
</tbody>
</table>

## .spec.install

Description
install is an optional field used to configure the installation options for the ClusterExtension such as the pre-flight check configuration.

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
<td style="text-align: left;"><p><code>preflight</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>preflight is an optional field that can be used to configure the checks that are run before installation or upgrade of the content for the package specified in the packageName field.</p>
<p>When specified, it replaces the default preflight configuration for install/upgrade actions. When not specified, the default configuration will be used.</p></td>
</tr>
</tbody>
</table>

## .spec.install.preflight

Description
preflight is an optional field that can be used to configure the checks that are run before installation or upgrade of the content for the package specified in the packageName field.

When specified, it replaces the default preflight configuration for install/upgrade actions. When not specified, the default configuration will be used.

Type
`object`

Required
- `crdUpgradeSafety`

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
<td style="text-align: left;"><p><code>crdUpgradeSafety</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>crdUpgradeSafety is used to configure the CRD Upgrade Safety pre-flight checks that run prior to upgrades of installed content.</p>
<p>The CRD Upgrade Safety pre-flight check safeguards from unintended consequences of upgrading a CRD, such as data loss.</p></td>
</tr>
</tbody>
</table>

## .spec.install.preflight.crdUpgradeSafety

Description
crdUpgradeSafety is used to configure the CRD Upgrade Safety pre-flight checks that run prior to upgrades of installed content.

The CRD Upgrade Safety pre-flight check safeguards from unintended consequences of upgrading a CRD, such as data loss.

Type
`object`

Required
- `enforcement`

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
<td style="text-align: left;"><p><code>enforcement</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>enforcement is a required field, used to configure the state of the CRD Upgrade Safety pre-flight check.</p>
<p>Allowed values are "None" or "Strict". The default value is "Strict".</p>
<p>When set to "None", the CRD Upgrade Safety pre-flight check will be skipped when performing an upgrade operation. This should be used with caution as unintended consequences such as data loss can occur.</p>
<p>When set to "Strict", the CRD Upgrade Safety pre-flight check will be run when performing an upgrade operation.</p></td>
</tr>
</tbody>
</table>

## .spec.serviceAccount

Description
serviceAccount is a reference to a ServiceAccount used to perform all interactions with the cluster that are required to manage the extension. The ServiceAccount must be configured with the necessary permissions to perform these interactions. The ServiceAccount must exist in the namespace referenced in the spec. serviceAccount is required.

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
<td style="text-align: left;"><p>name is a required, immutable reference to the name of the ServiceAccount to be used for installation and management of the content for the package specified in the packageName field.</p>
<p>This ServiceAccount must exist in the installNamespace.</p>
<p>name follows the DNS subdomain standard as defined in [RFC 1123]. It must contain only lowercase alphanumeric characters, hyphens (-) or periods (.), start and end with an alphanumeric character, and be no longer than 253 characters.</p>
<p>Some examples of valid values are: - some-serviceaccount - 123-serviceaccount - 1-serviceaccount-2 - someserviceaccount - some.serviceaccount</p>
<p>Some examples of invalid values are: - -some-serviceaccount - some-serviceaccount-</p>
<p>[RFC 1123]: <a href="https://tools.ietf.org/html/rfc1123">https://tools.ietf.org/html/rfc1123</a></p></td>
</tr>
</tbody>
</table>

## .spec.source

Description
source is a required field which selects the installation source of content for this ClusterExtension. Selection is performed by setting the sourceType.

Catalog is currently the only implemented sourceType, and setting the sourcetype to "Catalog" requires the catalog field to also be defined.

Below is a minimal example of a source definition (in yaml):

source: sourceType: Catalog catalog: packageName: example-package

Type
`object`

Required
- `sourceType`

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
<td style="text-align: left;"><p><code>catalog</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>catalog is used to configure how information is sourced from a catalog. This field is required when sourceType is "Catalog", and forbidden otherwise.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>sourceType</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>sourceType is a required reference to the type of install source.</p>
<p>Allowed values are "Catalog"</p>
<p>When this field is set to "Catalog", information for determining the appropriate bundle of content to install will be fetched from ClusterCatalog resources existing on the cluster. When using the Catalog sourceType, the catalog field must also be set.</p></td>
</tr>
</tbody>
</table>

## .spec.source.catalog

Description
catalog is used to configure how information is sourced from a catalog. This field is required when sourceType is "Catalog", and forbidden otherwise.

Type
`object`

Required
- `packageName`

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
<td style="text-align: left;"><p><code>channels</code></p></td>
<td style="text-align: left;"><p><code>array (string)</code></p></td>
<td style="text-align: left;"><p>channels is an optional reference to a set of channels belonging to the package specified in the packageName field.</p>
<p>A "channel" is a package-author-defined stream of updates for an extension.</p>
<p>Each channel in the list must follow the DNS subdomain standard as defined in [RFC 1123]. It must contain only lowercase alphanumeric characters, hyphens (-) or periods (.), start and end with an alphanumeric character, and be no longer than 253 characters. No more than 256 channels can be specified.</p>
<p>When specified, it is used to constrain the set of installable bundles and the automated upgrade path. This constraint is an AND operation with the version field. For example: - Given channel is set to "foo" - Given version is set to "&gt;=1.0.0, &lt;1.5.0" - Only bundles that exist in channel "foo" AND satisfy the version range comparison will be considered installable - Automatic upgrades will be constrained to upgrade edges defined by the selected channel</p>
<p>When unspecified, upgrade edges across all channels will be used to identify valid automatic upgrade paths.</p>
<p>Some examples of valid values are: - 1.1.x - alpha - stable - stable-v1 - v1-stable - dev-preview - preview - community</p>
<p>Some examples of invalid values are: - -some-channel - some-channel- - thisisareallylongchannelnamethatisgreaterthanthemaximumlength - original_40 - --default-channel</p>
<p>[RFC 1123]: <a href="https://tools.ietf.org/html/rfc1123">https://tools.ietf.org/html/rfc1123</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>packageName</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>packageName is a reference to the name of the package to be installed and is used to filter the content from catalogs.</p>
<p>packageName is required, immutable, and follows the DNS subdomain standard as defined in [RFC 1123]. It must contain only lowercase alphanumeric characters, hyphens (-) or periods (.), start and end with an alphanumeric character, and be no longer than 253 characters.</p>
<p>Some examples of valid values are: - some-package - 123-package - 1-package-2 - somepackage</p>
<p>Some examples of invalid values are: - -some-package - some-package- - thisisareallylongpackagenamethatisgreaterthanthemaximumlength - some.package</p>
<p>[RFC 1123]: <a href="https://tools.ietf.org/html/rfc1123">https://tools.ietf.org/html/rfc1123</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>selector</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>selector is an optional field that can be used to filter the set of ClusterCatalogs used in the bundle selection process.</p>
<p>When unspecified, all ClusterCatalogs will be used in the bundle selection process.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>upgradeConstraintPolicy</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>upgradeConstraintPolicy is an optional field that controls whether the upgrade path(s) defined in the catalog are enforced for the package referenced in the packageName field.</p>
<p>Allowed values are: "CatalogProvided" or "SelfCertified", or omitted.</p>
<p>When this field is set to "CatalogProvided", automatic upgrades will only occur when upgrade constraints specified by the package author are met.</p>
<p>When this field is set to "SelfCertified", the upgrade constraints specified by the package author are ignored. This allows for upgrades and downgrades to any version of the package. This is considered a dangerous operation as it can lead to unknown and potentially disastrous outcomes, such as data loss. It is assumed that users have independently verified changes when using this option.</p>
<p>When this field is omitted, the default value is "CatalogProvided".</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>version</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>version is an optional semver constraint (a specific version or range of versions). When unspecified, the latest version available will be installed.</p>
<p>Acceptable version ranges are no longer than 64 characters. Version ranges are composed of comma- or space-delimited values and one or more comparison operators, known as comparison strings. Additional comparison strings can be added using the OR operator (||).</p>
<p># Range Comparisons</p>
<p>To specify a version range, you can use a comparison string like "&gt;=3.0, &lt;3.6". When specifying a range, automatic updates will occur within that range. The example comparison string means "install any version greater than or equal to 3.0.0 but less than 3.6.0.". It also states intent that if any upgrades are available within the version range after initial installation, those upgrades should be automatically performed.</p>
<p># Pinned Versions</p>
<p>To specify an exact version to install you can use a version range that "pins" to a specific version. When pinning to a specific version, no automatic updates will occur. An example of a pinned version range is "0.6.0", which means "only install version 0.6.0 and never upgrade from this version".</p>
<p># Basic Comparison Operators</p>
<p>The basic comparison operators and their meanings are: - "=", equal (not aliased to an operator) - "!=", not equal - "&lt;", less than - "&gt;", greater than - "&gt;=", greater than OR equal to - "⇐", less than OR equal to</p>
<p># Wildcard Comparisons</p>
<p>You can use the "x", "X", and "<strong>" characters as wildcard characters in all comparison operations. Some examples of using the wildcard characters: - "1.2.x", "1.2.X", and "1.2.</strong>" is equivalent to "&gt;=1.2.0, &lt; 1.3.0" - "&gt;= 1.2.x", "&gt;= 1.2.X", and "&gt;= 1.2.<strong>" is equivalent to "&gt;= 1.2.0" - "⇐ 2.x", "⇐ 2.X", and "⇐ 2.</strong>" is equivalent to "&lt; 3" - "x", "X", and "*" is equivalent to "&gt;= 0.0.0"</p>
<p># Patch Release Comparisons</p>
<p>When you want to specify a minor version up to the next major version you can use the "~" character to perform patch comparisons. Some examples: - "~1.2.3" is equivalent to "&gt;=1.2.3, &lt;1.3.0" - "~1" and "~1.x" is equivalent to "&gt;=1, &lt;2" - "~2.3" is equivalent to "&gt;=2.3, &lt;2.4" - "~1.2.x" is equivalent to "&gt;=1.2.0, &lt;1.3.0"</p>
<p># Major Release Comparisons</p>
<p>You can use the "^" character to make major release comparisons after a stable 1.0.0 version is published. If there is no stable version published, // minor versions define the stability level. Some examples: - "^1.2.3" is equivalent to "&gt;=1.2.3, &lt;2.0.0" - "^1.2.x" is equivalent to "&gt;=1.2.0, &lt;2.0.0" - "^2.3" is equivalent to "&gt;=2.3, &lt;3" - "^2.x" is equivalent to "&gt;=2.0.0, &lt;3" - "^0.2.3" is equivalent to "&gt;=0.2.3, &lt;0.3.0" - "^0.2" is equivalent to "&gt;=0.2.0, &lt;0.3.0" - "^0.0.3" is equvalent to "&gt;=0.0.3, &lt;0.0.4" - "^0.0" is equivalent to "&gt;=0.0.0, &lt;0.1.0" - "^0" is equivalent to "&gt;=0.0.0, &lt;1.0.0"</p>
<p># OR Comparisons You can use the "||" character to represent an OR operation in the version range. Some examples: - "&gt;=1.2.3, &lt;2.0.0 || &gt;3.0.0" - "^0 || ^3 || ^5"</p>
<p>For more information on semver, please see <a href="https://semver.org/">https://semver.org/</a></p></td>
</tr>
</tbody>
</table>

## .spec.source.catalog.selector

Description
selector is an optional field that can be used to filter the set of ClusterCatalogs used in the bundle selection process.

When unspecified, all ClusterCatalogs will be used in the bundle selection process.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `matchExpressions` | `array` | matchExpressions is a list of label selector requirements. The requirements are ANDed. |
| `matchExpressions[]` | `object` | A label selector requirement is a selector that contains values, a key, and an operator that relates the key and values. |
| `matchLabels` | `object (string)` | matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed. |

## .spec.source.catalog.selector.matchExpressions

Description
matchExpressions is a list of label selector requirements. The requirements are ANDed.

Type
`array`

## .spec.source.catalog.selector.matchExpressions\[\]

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

## .status

Description
status is an optional field that defines the observed state of the ClusterExtension.

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
<td style="text-align: left;"><p><code>conditions</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>The set of condition types which apply to all spec.source variations are Installed and Progressing.</p>
<p>The Installed condition represents whether or not the bundle has been installed for this ClusterExtension. When Installed is True and the Reason is Succeeded, the bundle has been successfully installed. When Installed is False and the Reason is Failed, the bundle has failed to install.</p>
<p>The Progressing condition represents whether or not the ClusterExtension is advancing towards a new state. When Progressing is True and the Reason is Succeeded, the ClusterExtension is making progress towards a new state. When Progressing is True and the Reason is Retrying, the ClusterExtension has encountered an error that could be resolved on subsequent reconciliation attempts. When Progressing is False and the Reason is Blocked, the ClusterExtension has encountered an error that requires manual intervention for recovery.</p>
<p>When the ClusterExtension is sourced from a catalog, if may also communicate a deprecation condition. These are indications from a package owner to guide users away from a particular package, channel, or bundle. BundleDeprecated is set if the requested bundle version is marked deprecated in the catalog. ChannelDeprecated is set if the requested channel is marked deprecated in the catalog. PackageDeprecated is set if the requested package is marked deprecated in the catalog. Deprecated is a rollup condition that is present when any of the deprecated conditions are present.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>conditions[]</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>Condition contains details for one aspect of the current state of this API Resource.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>install</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>install is a representation of the current installation status for this ClusterExtension.</p></td>
</tr>
</tbody>
</table>

## .status.conditions

Description
The set of condition types which apply to all spec.source variations are Installed and Progressing.

The Installed condition represents whether or not the bundle has been installed for this ClusterExtension. When Installed is True and the Reason is Succeeded, the bundle has been successfully installed. When Installed is False and the Reason is Failed, the bundle has failed to install.

The Progressing condition represents whether or not the ClusterExtension is advancing towards a new state. When Progressing is True and the Reason is Succeeded, the ClusterExtension is making progress towards a new state. When Progressing is True and the Reason is Retrying, the ClusterExtension has encountered an error that could be resolved on subsequent reconciliation attempts. When Progressing is False and the Reason is Blocked, the ClusterExtension has encountered an error that requires manual intervention for recovery.

When the ClusterExtension is sourced from a catalog, if may also communicate a deprecation condition. These are indications from a package owner to guide users away from a particular package, channel, or bundle. BundleDeprecated is set if the requested bundle version is marked deprecated in the catalog. ChannelDeprecated is set if the requested channel is marked deprecated in the catalog. PackageDeprecated is set if the requested package is marked deprecated in the catalog. Deprecated is a rollup condition that is present when any of the deprecated conditions are present.

Type
`array`

## .status.conditions\[\]

Description
Condition contains details for one aspect of the current state of this API Resource.

Type
`object`

Required
- `lastTransitionTime`

- `message`

- `reason`

- `status`

- `type`

| Property | Type | Description |
|----|----|----|
| `lastTransitionTime` | `string` | lastTransitionTime is the last time the condition transitioned from one status to another. This should be when the underlying condition changed. If that is not known, then using the time when the API field changed is acceptable. |
| `message` | `string` | message is a human readable message indicating details about the transition. This may be an empty string. |
| `observedGeneration` | `integer` | observedGeneration represents the .metadata.generation that the condition was set based upon. For instance, if .metadata.generation is currently 12, but the .status.conditions\[x\].observedGeneration is 9, the condition is out of date with respect to the current state of the instance. |
| `reason` | `string` | reason contains a programmatic identifier indicating the reason for the condition’s last transition. Producers of specific condition types may define expected values and meanings for this field, and whether the values are considered a guaranteed API. The value should be a CamelCase string. This field may not be empty. |
| `status` | `string` | status of the condition, one of True, False, Unknown. |
| `type` | `string` | type of condition in CamelCase or in foo.example.com/CamelCase. |

## .status.install

Description
install is a representation of the current installation status for this ClusterExtension.

Type
`object`

Required
- `bundle`

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
<td style="text-align: left;"><p><code>bundle</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>bundle is a required field which represents the identifying attributes of a bundle.</p>
<p>A "bundle" is a versioned set of content that represents the resources that need to be applied to a cluster to install a package.</p></td>
</tr>
</tbody>
</table>

## .status.install.bundle

Description
bundle is a required field which represents the identifying attributes of a bundle.

A "bundle" is a versioned set of content that represents the resources that need to be applied to a cluster to install a package.

Type
`object`

Required
- `name`

- `version`

| Property | Type | Description |
|----|----|----|
| `name` | `string` | name is required and follows the DNS subdomain standard as defined in \[RFC 1123\]. It must contain only lowercase alphanumeric characters, hyphens (-) or periods (.), start and end with an alphanumeric character, and be no longer than 253 characters. |
| `version` | `string` | version is a required field and is a reference to the version that this bundle represents version follows the semantic versioning standard as defined in <https://semver.org/>. |

# API endpoints

The following API endpoints are available:

- `/apis/olm.operatorframework.io/v1/clusterextensions`

  - `DELETE`: delete collection of ClusterExtension

  - `GET`: list objects of kind ClusterExtension

  - `POST`: create a ClusterExtension

- `/apis/olm.operatorframework.io/v1/clusterextensions/{name}`

  - `DELETE`: delete a ClusterExtension

  - `GET`: read the specified ClusterExtension

  - `PATCH`: partially update the specified ClusterExtension

  - `PUT`: replace the specified ClusterExtension

- `/apis/olm.operatorframework.io/v1/clusterextensions/{name}/status`

  - `GET`: read status of the specified ClusterExtension

  - `PATCH`: partially update status of the specified ClusterExtension

  - `PUT`: replace status of the specified ClusterExtension

## /apis/olm.operatorframework.io/v1/clusterextensions

HTTP method
`DELETE`

Description
delete collection of ClusterExtension

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Status`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`GET`

Description
list objects of kind ClusterExtension

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ClusterExtensionList`](../objects/index.md#io-operatorframework-olm-v1-ClusterExtensionList) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`POST`

Description
create a ClusterExtension

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`ClusterExtension`](clusterextension-olm-operatorframework-io-v1.md#clusterextension-olm-operatorframework-io-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ClusterExtension`](clusterextension-olm-operatorframework-io-v1.md#clusterextension-olm-operatorframework-io-v1) schema |
| 201 - Created | [`ClusterExtension`](clusterextension-olm-operatorframework-io-v1.md#clusterextension-olm-operatorframework-io-v1) schema |
| 202 - Accepted | [`ClusterExtension`](clusterextension-olm-operatorframework-io-v1.md#clusterextension-olm-operatorframework-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/olm.operatorframework.io/v1/clusterextensions/{name}

| Parameter | Type     | Description                  |
|-----------|----------|------------------------------|
| `name`    | `string` | name of the ClusterExtension |

Global path parameters

HTTP method
`DELETE`

Description
delete a ClusterExtension

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
read the specified ClusterExtension

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ClusterExtension`](clusterextension-olm-operatorframework-io-v1.md#clusterextension-olm-operatorframework-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PATCH`

Description
partially update the specified ClusterExtension

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ClusterExtension`](clusterextension-olm-operatorframework-io-v1.md#clusterextension-olm-operatorframework-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PUT`

Description
replace the specified ClusterExtension

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`ClusterExtension`](clusterextension-olm-operatorframework-io-v1.md#clusterextension-olm-operatorframework-io-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ClusterExtension`](clusterextension-olm-operatorframework-io-v1.md#clusterextension-olm-operatorframework-io-v1) schema |
| 201 - Created | [`ClusterExtension`](clusterextension-olm-operatorframework-io-v1.md#clusterextension-olm-operatorframework-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/olm.operatorframework.io/v1/clusterextensions/{name}/status

| Parameter | Type     | Description                  |
|-----------|----------|------------------------------|
| `name`    | `string` | name of the ClusterExtension |

Global path parameters

HTTP method
`GET`

Description
read status of the specified ClusterExtension

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ClusterExtension`](clusterextension-olm-operatorframework-io-v1.md#clusterextension-olm-operatorframework-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PATCH`

Description
partially update status of the specified ClusterExtension

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ClusterExtension`](clusterextension-olm-operatorframework-io-v1.md#clusterextension-olm-operatorframework-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PUT`

Description
replace status of the specified ClusterExtension

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`ClusterExtension`](clusterextension-olm-operatorframework-io-v1.md#clusterextension-olm-operatorframework-io-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ClusterExtension`](clusterextension-olm-operatorframework-io-v1.md#clusterextension-olm-operatorframework-io-v1) schema |
| 201 - Created | [`ClusterExtension`](clusterextension-olm-operatorframework-io-v1.md#clusterextension-olm-operatorframework-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses
