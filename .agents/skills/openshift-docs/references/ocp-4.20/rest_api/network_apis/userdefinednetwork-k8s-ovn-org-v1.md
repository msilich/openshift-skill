<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Description
UserDefinedNetwork describe network request for a Namespace.

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
| `spec` | `object` | UserDefinedNetworkSpec defines the desired state of UserDefinedNetworkSpec. |
| `status` | `object` | UserDefinedNetworkStatus contains the observed status of the UserDefinedNetwork. |

## .spec

Description
UserDefinedNetworkSpec defines the desired state of UserDefinedNetworkSpec.

Type
`object`

Required
- `topology`

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
<td style="text-align: left;"><p><code>layer2</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>Layer2 is the Layer2 topology configuration.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>layer3</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>Layer3 is the Layer3 topology configuration.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>topology</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Topology describes network configuration.</p>
<p>Allowed values are "Layer3", "Layer2". Layer3 topology creates a layer 2 segment per node, each with a different subnet. Layer 3 routing is used to interconnect node subnets. Layer2 topology creates one logical switch shared by all nodes.</p></td>
</tr>
</tbody>
</table>

## .spec.layer2

Description
Layer2 is the Layer2 topology configuration.

Type
`object`

Required
- `role`

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
<td style="text-align: left;"><p><code>ipam</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>IPAM section contains IPAM-related configuration for the network.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>joinSubnets</code></p></td>
<td style="text-align: left;"><p><code>array (string)</code></p></td>
<td style="text-align: left;"><p>JoinSubnets are used inside the OVN network topology.</p>
<p>Dual-stack clusters may set 2 subnets (one for each IP family), otherwise only 1 subnet is allowed. This field is only allowed for "Primary" network. It is not recommended to set this field without explicit need and understanding of the OVN network topology. When omitted, the platform will choose a reasonable default which is subject to change over time.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>mtu</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p>MTU is the maximum transmission unit for a network. MTU is optional, if not provided, the globally configured value in OVN-Kubernetes (defaults to 1400) is used for the network.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>role</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Role describes the network role in the pod.</p>
<p>Allowed value is "Secondary". Secondary network is only assigned to pods that use <code>k8s.v1.cni.cncf.io/networks</code> annotation to select given network.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>subnets</code></p></td>
<td style="text-align: left;"><p><code>array (string)</code></p></td>
<td style="text-align: left;"><p>Subnets are used for the pod network across the cluster. Dual-stack clusters may set 2 subnets (one for each IP family), otherwise only 1 subnet is allowed.</p>
<p>The format should match standard CIDR notation (for example, "10.128.0.0/16"). This field must be omitted if <code>ipam.mode</code> is <code>Disabled</code>.</p></td>
</tr>
</tbody>
</table>

## .spec.layer2.ipam

Description
IPAM section contains IPAM-related configuration for the network.

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
<td style="text-align: left;"><p><code>lifecycle</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Lifecycle controls IP addresses management lifecycle.</p>
<p>The only allowed value is Persistent. When set, OVN Kubernetes assigned IP addresses will be persisted in an <code>ipamclaims.k8s.cni.cncf.io</code> object. These IP addresses will be reused by other pods if requested. Only supported when mode is <code>Enabled</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>mode</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Mode controls how much of the IP configuration will be managed by OVN. <code>Enabled</code> means OVN-Kubernetes will apply IP configuration to the SDN infrastructure and it will also assign IPs from the selected subnet to the individual pods. <code>Disabled</code> means OVN-Kubernetes will only assign MAC addresses and provide layer 2 communication, letting users configure IP addresses for the pods. <code>Disabled</code> is only available for Secondary networks. By disabling IPAM, any Kubernetes features that rely on selecting pods by IP will no longer function (such as network policy, services, etc). Additionally, IP port security will also be disabled for interfaces attached to this network. Defaults to <code>Enabled</code>.</p></td>
</tr>
</tbody>
</table>

## .spec.layer3

Description
Layer3 is the Layer3 topology configuration.

Type
`object`

Required
- `role`

- `subnets`

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
<td style="text-align: left;"><p><code>joinSubnets</code></p></td>
<td style="text-align: left;"><p><code>array (string)</code></p></td>
<td style="text-align: left;"><p>JoinSubnets are used inside the OVN network topology.</p>
<p>Dual-stack clusters may set 2 subnets (one for each IP family), otherwise only 1 subnet is allowed. This field is only allowed for "Primary" network. It is not recommended to set this field without explicit need and understanding of the OVN network topology. When omitted, the platform will choose a reasonable default which is subject to change over time.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>mtu</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p>MTU is the maximum transmission unit for a network.</p>
<p>MTU is optional, if not provided, the globally configured value in OVN-Kubernetes (defaults to 1400) is used for the network.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>role</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Role describes the network role in the pod.</p>
<p>Allowed values are "Primary" and "Secondary". Primary network is automatically assigned to every pod created in the same namespace. Secondary network is only assigned to pods that use <code>k8s.v1.cni.cncf.io/networks</code> annotation to select given network.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>subnets</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>Subnets are used for the pod network across the cluster.</p>
<p>Dual-stack clusters may set 2 subnets (one for each IP family), otherwise only 1 subnet is allowed. Given subnet is split into smaller subnets for every node.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>subnets[]</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"></td>
</tr>
</tbody>
</table>

## .spec.layer3.subnets

Description
Subnets are used for the pod network across the cluster.

Dual-stack clusters may set 2 subnets (one for each IP family), otherwise only 1 subnet is allowed. Given subnet is split into smaller subnets for every node.

Type
`array`

## .spec.layer3.subnets\[\]

Description

Type
`object`

Required
- `cidr`

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
<td style="text-align: left;"><p><code>cidr</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>CIDR specifies L3Subnet, which is split into smaller subnets for every node.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>hostSubnet</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p>HostSubnet specifies the subnet size for every node.</p>
<p>When not set, it will be assigned automatically.</p></td>
</tr>
</tbody>
</table>

## .status

Description
UserDefinedNetworkStatus contains the observed status of the UserDefinedNetwork.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `conditions` | `array` |  |
| `conditions[]` | `object` | Condition contains details for one aspect of the current state of this API Resource. |

## .status.conditions

Description

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

# API endpoints

The following API endpoints are available:

- `/apis/k8s.ovn.org/v1/userdefinednetworks`

  - `GET`: list objects of kind UserDefinedNetwork

- `/apis/k8s.ovn.org/v1/namespaces/{namespace}/userdefinednetworks`

  - `DELETE`: delete collection of UserDefinedNetwork

  - `GET`: list objects of kind UserDefinedNetwork

  - `POST`: create an UserDefinedNetwork

- `/apis/k8s.ovn.org/v1/namespaces/{namespace}/userdefinednetworks/{name}`

  - `DELETE`: delete an UserDefinedNetwork

  - `GET`: read the specified UserDefinedNetwork

  - `PATCH`: partially update the specified UserDefinedNetwork

  - `PUT`: replace the specified UserDefinedNetwork

- `/apis/k8s.ovn.org/v1/namespaces/{namespace}/userdefinednetworks/{name}/status`

  - `GET`: read status of the specified UserDefinedNetwork

  - `PATCH`: partially update status of the specified UserDefinedNetwork

  - `PUT`: replace status of the specified UserDefinedNetwork

## /apis/k8s.ovn.org/v1/userdefinednetworks

HTTP method
`GET`

Description
list objects of kind UserDefinedNetwork

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`UserDefinedNetworkList`](../objects/index.md#org-ovn-k8s-v1-UserDefinedNetworkList) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/k8s.ovn.org/v1/namespaces/{namespace}/userdefinednetworks

HTTP method
`DELETE`

Description
delete collection of UserDefinedNetwork

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Status`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`GET`

Description
list objects of kind UserDefinedNetwork

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`UserDefinedNetworkList`](../objects/index.md#org-ovn-k8s-v1-UserDefinedNetworkList) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`POST`

Description
create an UserDefinedNetwork

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`UserDefinedNetwork`](userdefinednetwork-k8s-ovn-org-v1.md#userdefinednetwork-k8s-ovn-org-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`UserDefinedNetwork`](userdefinednetwork-k8s-ovn-org-v1.md#userdefinednetwork-k8s-ovn-org-v1) schema |
| 201 - Created | [`UserDefinedNetwork`](userdefinednetwork-k8s-ovn-org-v1.md#userdefinednetwork-k8s-ovn-org-v1) schema |
| 202 - Accepted | [`UserDefinedNetwork`](userdefinednetwork-k8s-ovn-org-v1.md#userdefinednetwork-k8s-ovn-org-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/k8s.ovn.org/v1/namespaces/{namespace}/userdefinednetworks/{name}

| Parameter | Type     | Description                    |
|-----------|----------|--------------------------------|
| `name`    | `string` | name of the UserDefinedNetwork |

Global path parameters

HTTP method
`DELETE`

Description
delete an UserDefinedNetwork

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
read the specified UserDefinedNetwork

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`UserDefinedNetwork`](userdefinednetwork-k8s-ovn-org-v1.md#userdefinednetwork-k8s-ovn-org-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PATCH`

Description
partially update the specified UserDefinedNetwork

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`UserDefinedNetwork`](userdefinednetwork-k8s-ovn-org-v1.md#userdefinednetwork-k8s-ovn-org-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PUT`

Description
replace the specified UserDefinedNetwork

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`UserDefinedNetwork`](userdefinednetwork-k8s-ovn-org-v1.md#userdefinednetwork-k8s-ovn-org-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`UserDefinedNetwork`](userdefinednetwork-k8s-ovn-org-v1.md#userdefinednetwork-k8s-ovn-org-v1) schema |
| 201 - Created | [`UserDefinedNetwork`](userdefinednetwork-k8s-ovn-org-v1.md#userdefinednetwork-k8s-ovn-org-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/k8s.ovn.org/v1/namespaces/{namespace}/userdefinednetworks/{name}/status

| Parameter | Type     | Description                    |
|-----------|----------|--------------------------------|
| `name`    | `string` | name of the UserDefinedNetwork |

Global path parameters

HTTP method
`GET`

Description
read status of the specified UserDefinedNetwork

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`UserDefinedNetwork`](userdefinednetwork-k8s-ovn-org-v1.md#userdefinednetwork-k8s-ovn-org-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PATCH`

Description
partially update status of the specified UserDefinedNetwork

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`UserDefinedNetwork`](userdefinednetwork-k8s-ovn-org-v1.md#userdefinednetwork-k8s-ovn-org-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PUT`

Description
replace status of the specified UserDefinedNetwork

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`UserDefinedNetwork`](userdefinednetwork-k8s-ovn-org-v1.md#userdefinednetwork-k8s-ovn-org-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`UserDefinedNetwork`](userdefinednetwork-k8s-ovn-org-v1.md#userdefinednetwork-k8s-ovn-org-v1) schema |
| 201 - Created | [`UserDefinedNetwork`](userdefinednetwork-k8s-ovn-org-v1.md#userdefinednetwork-k8s-ovn-org-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses
