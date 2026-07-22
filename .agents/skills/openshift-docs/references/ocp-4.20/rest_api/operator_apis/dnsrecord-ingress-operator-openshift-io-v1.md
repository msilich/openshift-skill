<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Description
DNSRecord is a DNS record managed in the zones defined by dns.config.openshift.io/cluster .spec.publicZone and .spec.privateZone.

Cluster admin manipulation of this resource is not supported. This resource is only for internal communication of OpenShift operators.

If DNSManagementPolicy is "Unmanaged", the operator will not be responsible for managing the DNS records on the cloud provider.

Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).

Type
`object`

# Specification

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ObjectMeta`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) | Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |
| `spec` | `object` | spec is the specification of the desired behavior of the dnsRecord. |
| `status` | `object` | status is the most recently observed status of the dnsRecord. |

## .spec

Description
spec is the specification of the desired behavior of the dnsRecord.

Type
`object`

Required
- `dnsManagementPolicy`

- `dnsName`

- `recordTTL`

- `recordType`

- `targets`

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
<td style="text-align: left;"><p><code>dnsManagementPolicy</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>dnsManagementPolicy denotes the current policy applied on the DNS record. Records that have policy set as "Unmanaged" are ignored by the ingress operator. This means that the DNS record on the cloud provider is not managed by the operator, and the "Published" status condition will be updated to "Unknown" status, since it is externally managed. Any existing record on the cloud provider can be deleted at the discretion of the cluster admin.</p>
<p>This field defaults to Managed. Valid values are "Managed" and "Unmanaged".</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>dnsName</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>dnsName is the hostname of the DNS record</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>recordTTL</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p>recordTTL is the record TTL in seconds. If zero, the default is 30. RecordTTL will not be used in AWS regions Alias targets, but will be used in CNAME targets, per AWS API contract.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>recordType</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>recordType is the DNS record type. For example, "A" or "CNAME".</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>targets</code></p></td>
<td style="text-align: left;"><p><code>array (string)</code></p></td>
<td style="text-align: left;"><p>targets are record targets.</p></td>
</tr>
</tbody>
</table>

## .status

Description
status is the most recently observed status of the dnsRecord.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `observedGeneration` | `integer` | observedGeneration is the most recently observed generation of the DNSRecord. When the DNSRecord is updated, the controller updates the corresponding record in each managed zone. If an update for a particular zone fails, that failure is recorded in the status condition for the zone so that the controller can determine that it needs to retry the update for that specific zone. |
| `zones` | `array` | zones are the status of the record in each zone. |
| `zones[]` | `object` | DNSZoneStatus is the status of a record within a specific zone. |

## .status.zones

Description
zones are the status of the record in each zone.

Type
`array`

## .status.zones\[\]

Description
DNSZoneStatus is the status of a record within a specific zone.

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
<td style="text-align: left;"><p>conditions are any conditions associated with the record in the zone.</p>
<p>If publishing the record succeeds, the "Published" condition will be set with status "True" and upon failure it will be set to "False" along with the reason and message describing the cause of the failure.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>conditions[]</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>DNSZoneCondition is just the standard condition fields.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>dnsZone</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>dnsZone is the zone where the record is published.</p></td>
</tr>
</tbody>
</table>

## .status.zones\[\].conditions

Description
conditions are any conditions associated with the record in the zone.

If publishing the record succeeds, the "Published" condition will be set with status "True" and upon failure it will be set to "False" along with the reason and message describing the cause of the failure.

Type
`array`

## .status.zones\[\].conditions\[\]

Description
DNSZoneCondition is just the standard condition fields.

Type
`object`

Required
- `status`

- `type`

| Property             | Type     | Description |
|----------------------|----------|-------------|
| `lastTransitionTime` | `string` |             |
| `message`            | `string` |             |
| `reason`             | `string` |             |
| `status`             | `string` |             |
| `type`               | `string` |             |

## .status.zones\[\].dnsZone

Description
dnsZone is the zone where the record is published.

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
<td style="text-align: left;"><p><code>id</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>id is the identifier that can be used to find the DNS hosted zone.</p>
<p>on AWS zone can be fetched using <code>ID</code> as id in [1] on Azure zone can be fetched using <code>ID</code> as a pre-determined name in [2], on GCP zone can be fetched using <code>ID</code> as a pre-determined name in [3].</p>
<p>[1]: <a href="https://docs.aws.amazon.com/cli/latest/reference/route53/get-hosted-zone.html#options">https://docs.aws.amazon.com/cli/latest/reference/route53/get-hosted-zone.html#options</a> [2]: <a href="https://docs.microsoft.com/en-us/cli/azure/network/dns/zone?view=azure-cli-latest#az-network-dns-zone-show">https://docs.microsoft.com/en-us/cli/azure/network/dns/zone?view=azure-cli-latest#az-network-dns-zone-show</a> [3]: <a href="https://cloud.google.com/dns/docs/reference/v1/managedZones/get">https://cloud.google.com/dns/docs/reference/v1/managedZones/get</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>tags</code></p></td>
<td style="text-align: left;"><p><code>object (string)</code></p></td>
<td style="text-align: left;"><p>tags can be used to query the DNS hosted zone.</p>
<p>on AWS, resourcegroupstaggingapi [1] can be used to fetch a zone using <code>Tags</code> as tag-filters,</p>
<p>[1]: <a href="https://docs.aws.amazon.com/cli/latest/reference/resourcegroupstaggingapi/get-resources.html#options">https://docs.aws.amazon.com/cli/latest/reference/resourcegroupstaggingapi/get-resources.html#options</a></p></td>
</tr>
</tbody>
</table>

# API endpoints

The following API endpoints are available:

- `/apis/ingress.operator.openshift.io/v1/dnsrecords`

  - `GET`: list objects of kind DNSRecord

- `/apis/ingress.operator.openshift.io/v1/namespaces/{namespace}/dnsrecords`

  - `DELETE`: delete collection of DNSRecord

  - `GET`: list objects of kind DNSRecord

  - `POST`: create a DNSRecord

- `/apis/ingress.operator.openshift.io/v1/namespaces/{namespace}/dnsrecords/{name}`

  - `DELETE`: delete a DNSRecord

  - `GET`: read the specified DNSRecord

  - `PATCH`: partially update the specified DNSRecord

  - `PUT`: replace the specified DNSRecord

- `/apis/ingress.operator.openshift.io/v1/namespaces/{namespace}/dnsrecords/{name}/status`

  - `GET`: read status of the specified DNSRecord

  - `PATCH`: partially update status of the specified DNSRecord

  - `PUT`: replace status of the specified DNSRecord

## /apis/ingress.operator.openshift.io/v1/dnsrecords

HTTP method
`GET`

Description
list objects of kind DNSRecord

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`DNSRecordList`](../objects/index.md#io-openshift-operator-ingress-v1-DNSRecordList) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/ingress.operator.openshift.io/v1/namespaces/{namespace}/dnsrecords

HTTP method
`DELETE`

Description
delete collection of DNSRecord

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Status`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`GET`

Description
list objects of kind DNSRecord

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`DNSRecordList`](../objects/index.md#io-openshift-operator-ingress-v1-DNSRecordList) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`POST`

Description
create a DNSRecord

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`DNSRecord`](dnsrecord-ingress-operator-openshift-io-v1.md#dnsrecord-ingress-operator-openshift-io-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`DNSRecord`](dnsrecord-ingress-operator-openshift-io-v1.md#dnsrecord-ingress-operator-openshift-io-v1) schema |
| 201 - Created | [`DNSRecord`](dnsrecord-ingress-operator-openshift-io-v1.md#dnsrecord-ingress-operator-openshift-io-v1) schema |
| 202 - Accepted | [`DNSRecord`](dnsrecord-ingress-operator-openshift-io-v1.md#dnsrecord-ingress-operator-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/ingress.operator.openshift.io/v1/namespaces/{namespace}/dnsrecords/{name}

| Parameter | Type     | Description           |
|-----------|----------|-----------------------|
| `name`    | `string` | name of the DNSRecord |

Global path parameters

HTTP method
`DELETE`

Description
delete a DNSRecord

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
read the specified DNSRecord

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`DNSRecord`](dnsrecord-ingress-operator-openshift-io-v1.md#dnsrecord-ingress-operator-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PATCH`

Description
partially update the specified DNSRecord

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`DNSRecord`](dnsrecord-ingress-operator-openshift-io-v1.md#dnsrecord-ingress-operator-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PUT`

Description
replace the specified DNSRecord

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`DNSRecord`](dnsrecord-ingress-operator-openshift-io-v1.md#dnsrecord-ingress-operator-openshift-io-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`DNSRecord`](dnsrecord-ingress-operator-openshift-io-v1.md#dnsrecord-ingress-operator-openshift-io-v1) schema |
| 201 - Created | [`DNSRecord`](dnsrecord-ingress-operator-openshift-io-v1.md#dnsrecord-ingress-operator-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/ingress.operator.openshift.io/v1/namespaces/{namespace}/dnsrecords/{name}/status

| Parameter | Type     | Description           |
|-----------|----------|-----------------------|
| `name`    | `string` | name of the DNSRecord |

Global path parameters

HTTP method
`GET`

Description
read status of the specified DNSRecord

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`DNSRecord`](dnsrecord-ingress-operator-openshift-io-v1.md#dnsrecord-ingress-operator-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PATCH`

Description
partially update status of the specified DNSRecord

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`DNSRecord`](dnsrecord-ingress-operator-openshift-io-v1.md#dnsrecord-ingress-operator-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PUT`

Description
replace status of the specified DNSRecord

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`DNSRecord`](dnsrecord-ingress-operator-openshift-io-v1.md#dnsrecord-ingress-operator-openshift-io-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`DNSRecord`](dnsrecord-ingress-operator-openshift-io-v1.md#dnsrecord-ingress-operator-openshift-io-v1) schema |
| 201 - Created | [`DNSRecord`](dnsrecord-ingress-operator-openshift-io-v1.md#dnsrecord-ingress-operator-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses
