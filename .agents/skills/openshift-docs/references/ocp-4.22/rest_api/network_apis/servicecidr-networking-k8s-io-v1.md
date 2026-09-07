<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Description
ServiceCIDR defines a range of IP addresses using CIDR format (e.g. 192.168.0.0/24 or 2001:db2::/64). This range is used to allocate ClusterIPs to Service objects.

Type
`object`

# Specification

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ObjectMeta`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) | Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |
| `spec` | `object` | ServiceCIDRSpec define the CIDRs the user wants to use for allocating ClusterIPs for Services. |
| `status` | `object` | ServiceCIDRStatus describes the current state of the ServiceCIDR. |

## .spec

Description
ServiceCIDRSpec define the CIDRs the user wants to use for allocating ClusterIPs for Services.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `cidrs` | `array (string)` | CIDRs defines the IP blocks in CIDR notation (e.g. "192.168.0.0/24" or "2001:db8::/64") from which to assign service cluster IPs. Max of two CIDRs is allowed, one of each IP family. This field is immutable. |

## .status

Description
ServiceCIDRStatus describes the current state of the ServiceCIDR.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `conditions` | [`array (Condition)`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-Condition) | conditions holds an array of metav1.Condition that describe the state of the ServiceCIDR. Current service state |

# API endpoints

The following API endpoints are available:

- `/apis/networking.k8s.io/v1/servicecidrs`

  - `DELETE`: delete collection of ServiceCIDR

  - `GET`: list or watch objects of kind ServiceCIDR

  - `POST`: create a ServiceCIDR

- `/apis/networking.k8s.io/v1/watch/servicecidrs`

  - `GET`: watch individual changes to a list of ServiceCIDR. deprecated: use the 'watch' parameter with a list operation instead.

- `/apis/networking.k8s.io/v1/servicecidrs/{name}`

  - `DELETE`: delete a ServiceCIDR

  - `GET`: read the specified ServiceCIDR

  - `PATCH`: partially update the specified ServiceCIDR

  - `PUT`: replace the specified ServiceCIDR

- `/apis/networking.k8s.io/v1/watch/servicecidrs/{name}`

  - `GET`: watch changes to an object of kind ServiceCIDR. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.

- `/apis/networking.k8s.io/v1/servicecidrs/{name}/status`

  - `GET`: read status of the specified ServiceCIDR

  - `PATCH`: partially update status of the specified ServiceCIDR

  - `PUT`: replace status of the specified ServiceCIDR

## /apis/networking.k8s.io/v1/servicecidrs

HTTP method
`DELETE`

Description
delete collection of ServiceCIDR

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
list or watch objects of kind ServiceCIDR

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ServiceCIDRList`](../objects/index.md#io-k8s-api-networking-v1-ServiceCIDRList) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`POST`

Description
create a ServiceCIDR

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`ServiceCIDR`](servicecidr-networking-k8s-io-v1.md#servicecidr-networking-k8s-io-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ServiceCIDR`](servicecidr-networking-k8s-io-v1.md#servicecidr-networking-k8s-io-v1) schema |
| 201 - Created | [`ServiceCIDR`](servicecidr-networking-k8s-io-v1.md#servicecidr-networking-k8s-io-v1) schema |
| 202 - Accepted | [`ServiceCIDR`](servicecidr-networking-k8s-io-v1.md#servicecidr-networking-k8s-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/networking.k8s.io/v1/watch/servicecidrs

HTTP method
`GET`

Description
watch individual changes to a list of ServiceCIDR. deprecated: use the 'watch' parameter with a list operation instead.

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`WatchEvent`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/networking.k8s.io/v1/servicecidrs/{name}

| Parameter | Type     | Description             |
|-----------|----------|-------------------------|
| `name`    | `string` | name of the ServiceCIDR |

Global path parameters

HTTP method
`DELETE`

Description
delete a ServiceCIDR

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
read the specified ServiceCIDR

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ServiceCIDR`](servicecidr-networking-k8s-io-v1.md#servicecidr-networking-k8s-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PATCH`

Description
partially update the specified ServiceCIDR

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ServiceCIDR`](servicecidr-networking-k8s-io-v1.md#servicecidr-networking-k8s-io-v1) schema |
| 201 - Created | [`ServiceCIDR`](servicecidr-networking-k8s-io-v1.md#servicecidr-networking-k8s-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PUT`

Description
replace the specified ServiceCIDR

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`ServiceCIDR`](servicecidr-networking-k8s-io-v1.md#servicecidr-networking-k8s-io-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ServiceCIDR`](servicecidr-networking-k8s-io-v1.md#servicecidr-networking-k8s-io-v1) schema |
| 201 - Created | [`ServiceCIDR`](servicecidr-networking-k8s-io-v1.md#servicecidr-networking-k8s-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/networking.k8s.io/v1/watch/servicecidrs/{name}

| Parameter | Type     | Description             |
|-----------|----------|-------------------------|
| `name`    | `string` | name of the ServiceCIDR |

Global path parameters

HTTP method
`GET`

Description
watch changes to an object of kind ServiceCIDR. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`WatchEvent`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/networking.k8s.io/v1/servicecidrs/{name}/status

| Parameter | Type     | Description             |
|-----------|----------|-------------------------|
| `name`    | `string` | name of the ServiceCIDR |

Global path parameters

HTTP method
`GET`

Description
read status of the specified ServiceCIDR

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ServiceCIDR`](servicecidr-networking-k8s-io-v1.md#servicecidr-networking-k8s-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PATCH`

Description
partially update status of the specified ServiceCIDR

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ServiceCIDR`](servicecidr-networking-k8s-io-v1.md#servicecidr-networking-k8s-io-v1) schema |
| 201 - Created | [`ServiceCIDR`](servicecidr-networking-k8s-io-v1.md#servicecidr-networking-k8s-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PUT`

Description
replace status of the specified ServiceCIDR

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`ServiceCIDR`](servicecidr-networking-k8s-io-v1.md#servicecidr-networking-k8s-io-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ServiceCIDR`](servicecidr-networking-k8s-io-v1.md#servicecidr-networking-k8s-io-v1) schema |
| 201 - Created | [`ServiceCIDR`](servicecidr-networking-k8s-io-v1.md#servicecidr-networking-k8s-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses
