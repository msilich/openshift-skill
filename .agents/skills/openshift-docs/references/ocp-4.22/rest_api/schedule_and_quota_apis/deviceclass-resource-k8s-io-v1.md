<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Description
DeviceClass is a vendor- or admin-provided resource that contains device configuration and selectors. It can be referenced in the device requests of a claim to apply these presets. Cluster scoped.

This is an alpha type and requires enabling the DynamicResourceAllocation feature gate.

Type
`object`

Required
- `spec`

# Specification

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ObjectMeta`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) | Standard object metadata |
| `spec` | `object` | DeviceClassSpec is used in a \[DeviceClass\] to define what can be allocated and how to configure it. |

## .spec

Description
DeviceClassSpec is used in a \[DeviceClass\] to define what can be allocated and how to configure it.

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
<td style="text-align: left;"><p><code>config</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>Config defines configuration parameters that apply to each device that is claimed via this class. Some classses may potentially be satisfied by multiple drivers, so each instance of a vendor configuration applies to exactly one driver.</p>
<p>They are passed to the driver, but are not considered while allocating the claim.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>config[]</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>DeviceClassConfiguration is used in DeviceClass.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>extendedResourceName</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>ExtendedResourceName is the extended resource name for the devices of this class. The devices of this class can be used to satisfy a pod’s extended resource requests. It has the same format as the name of a pod’s extended resource. It should be unique among all the device classes in a cluster. If two device classes have the same name, then the class created later is picked to satisfy a pod’s extended resource requests. If two classes are created at the same time, then the name of the class lexicographically sorted first is picked.</p>
<p>This is an alpha field.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>selectors</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>Each selector must be satisfied by a device which is claimed via this class.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>selectors[]</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>DeviceSelector must have exactly one field set.</p></td>
</tr>
</tbody>
</table>

## .spec.config

Description
Config defines configuration parameters that apply to each device that is claimed via this class. Some classses may potentially be satisfied by multiple drivers, so each instance of a vendor configuration applies to exactly one driver.

They are passed to the driver, but are not considered while allocating the claim.

Type
`array`

## .spec.config\[\]

Description
DeviceClassConfiguration is used in DeviceClass.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `opaque` | `object` | OpaqueDeviceConfiguration contains configuration parameters for a driver in a format defined by the driver vendor. |

## .spec.config\[\].opaque

Description
OpaqueDeviceConfiguration contains configuration parameters for a driver in a format defined by the driver vendor.

Type
`object`

Required
- `driver`

- `parameters`

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
<td style="text-align: left;"><p><code>driver</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Driver is used to determine which kubelet plugin needs to be passed these configuration parameters.</p>
<p>An admission policy provided by the driver developer could use this to decide whether it needs to validate them.</p>
<p>Must be a DNS subdomain and should end with a DNS domain owned by the vendor of the driver. It should use only lower case characters.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>parameters</code></p></td>
<td style="text-align: left;"><p><a href="../objects/index.xml#io-k8s-apimachinery-pkg-runtime-RawExtension"><code>RawExtension</code></a></p></td>
<td style="text-align: left;"><p>Parameters can contain arbitrary data. It is the responsibility of the driver developer to handle validation and versioning. Typically this includes self-identification and a version ("kind" + "apiVersion" for Kubernetes types), with conversion between different versions.</p>
<p>The length of the raw data must be smaller or equal to 10 Ki.</p></td>
</tr>
</tbody>
</table>

## .spec.selectors

Description
Each selector must be satisfied by a device which is claimed via this class.

Type
`array`

## .spec.selectors\[\]

Description
DeviceSelector must have exactly one field set.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `cel` | `object` | CELDeviceSelector contains a CEL expression for selecting a device. |

## .spec.selectors\[\].cel

Description
CELDeviceSelector contains a CEL expression for selecting a device.

Type
`object`

Required
- `expression`

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
<td style="text-align: left;"><p><code>expression</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Expression is a CEL expression which evaluates a single device. It must evaluate to true when the device under consideration satisfies the desired criteria, and false when it does not. Any other result is an error and causes allocation of devices to abort.</p>
<p>The expression’s input is an object named "device", which carries the following properties: - driver (string): the name of the driver which defines this device. - attributes (map[string]object): the device’s attributes, grouped by prefix (e.g. device.attributes["dra.example.com"] evaluates to an object with all of the attributes which were prefixed by "dra.example.com". - capacity (map[string]object): the device’s capacities, grouped by prefix. - allowMultipleAllocations (bool): the allowMultipleAllocations property of the device (v1.34+ with the DRAConsumableCapacity feature enabled).</p>
<p>Example: Consider a device with driver="dra.example.com", which exposes two attributes named "model" and "ext.example.com/family" and which exposes one capacity named "modules". This input to this expression would have the following fields:</p>
<p>device.driver device.attributes["dra.example.com"].model device.attributes["ext.example.com"].family device.capacity["dra.example.com"].modules</p>
<p>The device.driver field can be used to check for a specific driver, either as a high-level precondition (i.e. you only want to consider devices from this driver) or as part of a multi-clause expression that is meant to consider devices from different drivers.</p>
<p>The value type of each attribute is defined by the device definition, and users who write these expressions must consult the documentation for their specific drivers. The value type of each capacity is Quantity.</p>
<p>If an unknown prefix is used as a lookup in either device.attributes or device.capacity, an empty map will be returned. Any reference to an unknown field will cause an evaluation error and allocation to abort.</p>
<p>A robust expression should check for the existence of attributes before referencing them.</p>
<p>For ease of use, the cel.bind() function is enabled, and can be used to simplify expressions that access multiple attributes with the same domain. For example:</p>
<p>cel.bind(dra, device.attributes["dra.example.com"], dra.someBool &amp;&amp; dra.anotherBool)</p>
<p>The length of the expression must be smaller or equal to 10 Ki. The cost of evaluating it is also limited based on the estimated number of logical steps.</p></td>
</tr>
</tbody>
</table>

# API endpoints

The following API endpoints are available:

- `/apis/resource.k8s.io/v1/deviceclasses`

  - `DELETE`: delete collection of DeviceClass

  - `GET`: list or watch objects of kind DeviceClass

  - `POST`: create a DeviceClass

- `/apis/resource.k8s.io/v1/watch/deviceclasses`

  - `GET`: watch individual changes to a list of DeviceClass. deprecated: use the 'watch' parameter with a list operation instead.

- `/apis/resource.k8s.io/v1/deviceclasses/{name}`

  - `DELETE`: delete a DeviceClass

  - `GET`: read the specified DeviceClass

  - `PATCH`: partially update the specified DeviceClass

  - `PUT`: replace the specified DeviceClass

- `/apis/resource.k8s.io/v1/watch/deviceclasses/{name}`

  - `GET`: watch changes to an object of kind DeviceClass. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.

## /apis/resource.k8s.io/v1/deviceclasses

HTTP method
`DELETE`

Description
delete collection of DeviceClass

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |

Query parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Status`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`GET`

Description
list or watch objects of kind DeviceClass

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`DeviceClassList`](../objects/index.md#io-k8s-api-resource-v1-DeviceClassList) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`POST`

Description
create a DeviceClass

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`DeviceClass`](deviceclass-resource-k8s-io-v1.md#deviceclass-resource-k8s-io-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`DeviceClass`](deviceclass-resource-k8s-io-v1.md#deviceclass-resource-k8s-io-v1) schema |
| 201 - Created | [`DeviceClass`](deviceclass-resource-k8s-io-v1.md#deviceclass-resource-k8s-io-v1) schema |
| 202 - Accepted | [`DeviceClass`](deviceclass-resource-k8s-io-v1.md#deviceclass-resource-k8s-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/resource.k8s.io/v1/watch/deviceclasses

HTTP method
`GET`

Description
watch individual changes to a list of DeviceClass. deprecated: use the 'watch' parameter with a list operation instead.

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`WatchEvent`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/resource.k8s.io/v1/deviceclasses/{name}

| Parameter | Type     | Description             |
|-----------|----------|-------------------------|
| `name`    | `string` | name of the DeviceClass |

Global path parameters

HTTP method
`DELETE`

Description
delete a DeviceClass

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |

Query parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`DeviceClass`](deviceclass-resource-k8s-io-v1.md#deviceclass-resource-k8s-io-v1) schema |
| 202 - Accepted | [`DeviceClass`](deviceclass-resource-k8s-io-v1.md#deviceclass-resource-k8s-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`GET`

Description
read the specified DeviceClass

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`DeviceClass`](deviceclass-resource-k8s-io-v1.md#deviceclass-resource-k8s-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PATCH`

Description
partially update the specified DeviceClass

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`DeviceClass`](deviceclass-resource-k8s-io-v1.md#deviceclass-resource-k8s-io-v1) schema |
| 201 - Created | [`DeviceClass`](deviceclass-resource-k8s-io-v1.md#deviceclass-resource-k8s-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PUT`

Description
replace the specified DeviceClass

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`DeviceClass`](deviceclass-resource-k8s-io-v1.md#deviceclass-resource-k8s-io-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`DeviceClass`](deviceclass-resource-k8s-io-v1.md#deviceclass-resource-k8s-io-v1) schema |
| 201 - Created | [`DeviceClass`](deviceclass-resource-k8s-io-v1.md#deviceclass-resource-k8s-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/resource.k8s.io/v1/watch/deviceclasses/{name}

| Parameter | Type     | Description             |
|-----------|----------|-------------------------|
| `name`    | `string` | name of the DeviceClass |

Global path parameters

HTTP method
`GET`

Description
watch changes to an object of kind DeviceClass. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`WatchEvent`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema |
| 401 - Unauthorized | Empty |

HTTP responses
