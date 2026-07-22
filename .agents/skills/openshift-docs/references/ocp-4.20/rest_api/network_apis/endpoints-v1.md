<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Description
Endpoints is a collection of endpoints that implement the actual service. Example:

     Name: "mysvc",
     Subsets: [
       {
         Addresses: [{"ip": "10.10.1.1"}, {"ip": "10.10.2.2"}],
         Ports: [{"name": "a", "port": 8675}, {"name": "b", "port": 309}]
       },
       {
         Addresses: [{"ip": "10.10.3.3"}],
         Ports: [{"name": "a", "port": 93}, {"name": "b", "port": 76}]
       },
    ]

Endpoints is a legacy API and does not contain information about all Service features. Use discoveryv1.EndpointSlice for complete information about Service endpoints.

Deprecated: This API is deprecated in v1.33+. Use discoveryv1.EndpointSlice.

Type
`object`

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
<td style="text-align: left;"><p><code>kind</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <a href="https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds">https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>metadata</code></p></td>
<td style="text-align: left;"><p><a href="../objects/index.xml#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta"><code>ObjectMeta</code></a></p></td>
<td style="text-align: left;"><p>Standard object’s metadata. More info: <a href="https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata">https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>subsets</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>The set of all endpoints is the union of all subsets. Addresses are placed into subsets according to the IPs they share. A single address with multiple ports, some of which are ready and some of which are not (because they come from different containers) will result in the address being displayed in different subsets for the different ports. No address will appear in both Addresses and NotReadyAddresses in the same subset. Sets of addresses and ports that comprise a service.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>subsets[]</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>EndpointSubset is a group of addresses with a common set of ports. The expanded set of endpoints is the Cartesian product of Addresses x Ports. For example, given:</p>
<p>{ Addresses: [{"ip": "10.10.1.1"}, {"ip": "10.10.2.2"}], Ports: [{"name": "a", "port": 8675}, {"name": "b", "port": 309}] }</p>
<p>The resulting set of endpoints can be viewed as:</p>
<p>a: [ 10.10.1.1:8675, 10.10.2.2:8675 ], b: [ 10.10.1.1:309, 10.10.2.2:309 ]</p>
<p>Deprecated: This API is deprecated in v1.33+.</p></td>
</tr>
</tbody>
</table>

## .subsets

Description
The set of all endpoints is the union of all subsets. Addresses are placed into subsets according to the IPs they share. A single address with multiple ports, some of which are ready and some of which are not (because they come from different containers) will result in the address being displayed in different subsets for the different ports. No address will appear in both Addresses and NotReadyAddresses in the same subset. Sets of addresses and ports that comprise a service.

Type
`array`

## .subsets\[\]

Description
EndpointSubset is a group of addresses with a common set of ports. The expanded set of endpoints is the Cartesian product of Addresses x Ports. For example, given:

    {
      Addresses: [{"ip": "10.10.1.1"}, {"ip": "10.10.2.2"}],
      Ports:     [{"name": "a", "port": 8675}, {"name": "b", "port": 309}]
    }

The resulting set of endpoints can be viewed as:

    a: [ 10.10.1.1:8675, 10.10.2.2:8675 ],
    b: [ 10.10.1.1:309, 10.10.2.2:309 ]

Deprecated: This API is deprecated in v1.33+.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `addresses` | `array` | IP addresses which offer the related ports that are marked as ready. These endpoints should be considered safe for load balancers and clients to utilize. |
| `addresses[]` | `object` | EndpointAddress is a tuple that describes single IP address. Deprecated: This API is deprecated in v1.33+. |
| `notReadyAddresses` | `array` | IP addresses which offer the related ports but are not currently marked as ready because they have not yet finished starting, have recently failed a readiness check, or have recently failed a liveness check. |
| `notReadyAddresses[]` | `object` | EndpointAddress is a tuple that describes single IP address. Deprecated: This API is deprecated in v1.33+. |
| `ports` | `array` | Port numbers available on the related IP addresses. |
| `ports[]` | `object` | EndpointPort is a tuple that describes a single port. Deprecated: This API is deprecated in v1.33+. |

## .subsets\[\].addresses

Description
IP addresses which offer the related ports that are marked as ready. These endpoints should be considered safe for load balancers and clients to utilize.

Type
`array`

## .subsets\[\].addresses\[\]

Description
EndpointAddress is a tuple that describes single IP address. Deprecated: This API is deprecated in v1.33+.

Type
`object`

Required
- `ip`

| Property | Type | Description |
|----|----|----|
| `hostname` | `string` | The Hostname of this endpoint |
| `ip` | `string` | The IP of this endpoint. May not be loopback (127.0.0.0/8 or ::1), link-local (169.254.0.0/16 or fe80::/10), or link-local multicast (224.0.0.0/24 or ff02::/16). |
| `nodeName` | `string` | Optional: Node hosting this endpoint. This can be used to determine endpoints local to a node. |
| `targetRef` | `object` | ObjectReference contains enough information to let you inspect or modify the referred object. |

## .subsets\[\].addresses\[\].targetRef

Description
ObjectReference contains enough information to let you inspect or modify the referred object.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | API version of the referent. |
| `fieldPath` | `string` | If referring to a piece of an object instead of an entire object, this string should contain a valid JSON/Go field access statement, such as desiredState.manifest.containers\[2\]. For example, if the object reference is to a container within a pod, this would take on a value like: "spec.containers{name}" (where "name" refers to the name of the container that triggered the event) or if no container name is specified "spec.containers\[2\]" (container with index 2 in this pod). This syntax is chosen only to have some well-defined way of referencing a part of an object. |
| `kind` | `string` | Kind of the referent. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `name` | `string` | Name of the referent. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names> |
| `namespace` | `string` | Namespace of the referent. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/> |
| `resourceVersion` | `string` | Specific resourceVersion to which this reference is made, if any. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#concurrency-control-and-consistency> |
| `uid` | `string` | UID of the referent. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#uids> |

## .subsets\[\].notReadyAddresses

Description
IP addresses which offer the related ports but are not currently marked as ready because they have not yet finished starting, have recently failed a readiness check, or have recently failed a liveness check.

Type
`array`

## .subsets\[\].notReadyAddresses\[\]

Description
EndpointAddress is a tuple that describes single IP address. Deprecated: This API is deprecated in v1.33+.

Type
`object`

Required
- `ip`

| Property | Type | Description |
|----|----|----|
| `hostname` | `string` | The Hostname of this endpoint |
| `ip` | `string` | The IP of this endpoint. May not be loopback (127.0.0.0/8 or ::1), link-local (169.254.0.0/16 or fe80::/10), or link-local multicast (224.0.0.0/24 or ff02::/16). |
| `nodeName` | `string` | Optional: Node hosting this endpoint. This can be used to determine endpoints local to a node. |
| `targetRef` | `object` | ObjectReference contains enough information to let you inspect or modify the referred object. |

## .subsets\[\].notReadyAddresses\[\].targetRef

Description
ObjectReference contains enough information to let you inspect or modify the referred object.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | API version of the referent. |
| `fieldPath` | `string` | If referring to a piece of an object instead of an entire object, this string should contain a valid JSON/Go field access statement, such as desiredState.manifest.containers\[2\]. For example, if the object reference is to a container within a pod, this would take on a value like: "spec.containers{name}" (where "name" refers to the name of the container that triggered the event) or if no container name is specified "spec.containers\[2\]" (container with index 2 in this pod). This syntax is chosen only to have some well-defined way of referencing a part of an object. |
| `kind` | `string` | Kind of the referent. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `name` | `string` | Name of the referent. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names> |
| `namespace` | `string` | Namespace of the referent. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/> |
| `resourceVersion` | `string` | Specific resourceVersion to which this reference is made, if any. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#concurrency-control-and-consistency> |
| `uid` | `string` | UID of the referent. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#uids> |

## .subsets\[\].ports

Description
Port numbers available on the related IP addresses.

Type
`array`

## .subsets\[\].ports\[\]

Description
EndpointPort is a tuple that describes a single port. Deprecated: This API is deprecated in v1.33+.

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
<td style="text-align: left;"><p><code>appProtocol</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>The application protocol for this port. This is used as a hint for implementations to offer richer behavior for protocols that they understand. This field follows standard Kubernetes label syntax. Valid values are either:</p>
<p>* Un-prefixed protocol names - reserved for IANA standard service names (as per RFC-6335 and <a href="https://www.iana.org/assignments/service-names">https://www.iana.org/assignments/service-names</a>).</p>
<p>* Kubernetes-defined prefixed names: * 'kubernetes.io/h2c' - HTTP/2 prior knowledge over cleartext as described in <a href="https://www.rfc-editor.org/rfc/rfc9113.html#name-starting-http-2-with-prior-">https://www.rfc-editor.org/rfc/rfc9113.html#name-starting-http-2-with-prior-</a> * 'kubernetes.io/ws' - WebSocket over cleartext as described in <a href="https://www.rfc-editor.org/rfc/rfc6455">https://www.rfc-editor.org/rfc/rfc6455</a> * 'kubernetes.io/wss' - WebSocket over TLS as described in <a href="https://www.rfc-editor.org/rfc/rfc6455">https://www.rfc-editor.org/rfc/rfc6455</a></p>
<p>* Other protocols should use implementation-defined prefixed names such as mycompany.com/my-custom-protocol.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>name</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>The name of this port. This must match the 'name' field in the corresponding ServicePort. Must be a DNS_LABEL. Optional only if one port is defined.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>port</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p>The port number of the endpoint.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>protocol</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>The IP protocol for this port. Must be UDP, TCP, or SCTP. Default is TCP.</p>
<p>Possible enum values: - <code>"SCTP"</code> is the SCTP protocol. - <code>"TCP"</code> is the TCP protocol. - <code>"UDP"</code> is the UDP protocol.</p></td>
</tr>
</tbody>
</table>

# API endpoints

The following API endpoints are available:

- `/api/v1/endpoints`

  - `GET`: list or watch objects of kind Endpoints

- `/api/v1/watch/endpoints`

  - `GET`: watch individual changes to a list of Endpoints. deprecated: use the 'watch' parameter with a list operation instead.

- `/api/v1/namespaces/{namespace}/endpoints`

  - `DELETE`: delete collection of Endpoints

  - `GET`: list or watch objects of kind Endpoints

  - `POST`: create Endpoints

- `/api/v1/watch/namespaces/{namespace}/endpoints`

  - `GET`: watch individual changes to a list of Endpoints. deprecated: use the 'watch' parameter with a list operation instead.

- `/api/v1/namespaces/{namespace}/endpoints/{name}`

  - `DELETE`: delete Endpoints

  - `GET`: read the specified Endpoints

  - `PATCH`: partially update the specified Endpoints

  - `PUT`: replace the specified Endpoints

- `/api/v1/watch/namespaces/{namespace}/endpoints/{name}`

  - `GET`: watch changes to an object of kind Endpoints. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.

## /api/v1/endpoints

HTTP method
`GET`

Description
list or watch objects of kind Endpoints

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`EndpointsList`](../objects/index.md#io-k8s-api-core-v1-EndpointsList) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /api/v1/watch/endpoints

HTTP method
`GET`

Description
watch individual changes to a list of Endpoints. deprecated: use the 'watch' parameter with a list operation instead.

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`WatchEvent`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /api/v1/namespaces/{namespace}/endpoints

HTTP method
`DELETE`

Description
delete collection of Endpoints

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
list or watch objects of kind Endpoints

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`EndpointsList`](../objects/index.md#io-k8s-api-core-v1-EndpointsList) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`POST`

Description
create Endpoints

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`Endpoints`](endpoints-v1.md#endpoints-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Endpoints`](endpoints-v1.md#endpoints-v1) schema |
| 201 - Created | [`Endpoints`](endpoints-v1.md#endpoints-v1) schema |
| 202 - Accepted | [`Endpoints`](endpoints-v1.md#endpoints-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /api/v1/watch/namespaces/{namespace}/endpoints

HTTP method
`GET`

Description
watch individual changes to a list of Endpoints. deprecated: use the 'watch' parameter with a list operation instead.

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`WatchEvent`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /api/v1/namespaces/{namespace}/endpoints/{name}

| Parameter | Type     | Description           |
|-----------|----------|-----------------------|
| `name`    | `string` | name of the Endpoints |

Global path parameters

HTTP method
`DELETE`

Description
delete Endpoints

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
read the specified Endpoints

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Endpoints`](endpoints-v1.md#endpoints-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PATCH`

Description
partially update the specified Endpoints

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Endpoints`](endpoints-v1.md#endpoints-v1) schema |
| 201 - Created | [`Endpoints`](endpoints-v1.md#endpoints-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PUT`

Description
replace the specified Endpoints

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`Endpoints`](endpoints-v1.md#endpoints-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Endpoints`](endpoints-v1.md#endpoints-v1) schema |
| 201 - Created | [`Endpoints`](endpoints-v1.md#endpoints-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /api/v1/watch/namespaces/{namespace}/endpoints/{name}

| Parameter | Type     | Description           |
|-----------|----------|-----------------------|
| `name`    | `string` | name of the Endpoints |

Global path parameters

HTTP method
`GET`

Description
watch changes to an object of kind Endpoints. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`WatchEvent`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema |
| 401 - Unauthorized | Empty |

HTTP responses
