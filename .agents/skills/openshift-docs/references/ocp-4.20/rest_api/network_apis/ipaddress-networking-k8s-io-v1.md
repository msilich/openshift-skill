<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Description
IPAddress represents a single IP of a single IP Family. The object is designed to be used by APIs that operate on IP addresses. The object is used by the Service core API for allocation of IP addresses. An IP address can be represented in different formats, to guarantee the uniqueness of the IP, the name of the object is the IP address in canonical format, four decimal digits separated by dots suppressing leading zeros for IPv4 and the representation defined by RFC 5952 for IPv6. Valid: 192.168.1.5 or 2001:db8::1 or 2001:db8:aaaa:bbbb:cccc:dddd:eeee:1 Invalid: 10.01.2.3 or 2001:db8:0:0:0::1

Type
`object`

# Specification

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ObjectMeta`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) | Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |
| `spec` | `object` | IPAddressSpec describe the attributes in an IP Address. |

## .spec

Description
IPAddressSpec describe the attributes in an IP Address.

Type
`object`

Required
- `parentRef`

| Property | Type | Description |
|----|----|----|
| `parentRef` | `object` | ParentReference describes a reference to a parent object. |

## .spec.parentRef

Description
ParentReference describes a reference to a parent object.

Type
`object`

Required
- `resource`

- `name`

| Property | Type | Description |
|----|----|----|
| `group` | `string` | Group is the group of the object being referenced. |
| `name` | `string` | Name is the name of the object being referenced. |
| `namespace` | `string` | Namespace is the namespace of the object being referenced. |
| `resource` | `string` | Resource is the resource of the object being referenced. |

# API endpoints

The following API endpoints are available:

- `/apis/networking.k8s.io/v1/ipaddresses`

  - `DELETE`: delete collection of IPAddress

  - `GET`: list or watch objects of kind IPAddress

  - `POST`: create an IPAddress

- `/apis/networking.k8s.io/v1/watch/ipaddresses`

  - `GET`: watch individual changes to a list of IPAddress. deprecated: use the 'watch' parameter with a list operation instead.

- `/apis/networking.k8s.io/v1/ipaddresses/{name}`

  - `DELETE`: delete an IPAddress

  - `GET`: read the specified IPAddress

  - `PATCH`: partially update the specified IPAddress

  - `PUT`: replace the specified IPAddress

- `/apis/networking.k8s.io/v1/watch/ipaddresses/{name}`

  - `GET`: watch changes to an object of kind IPAddress. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.

## /apis/networking.k8s.io/v1/ipaddresses

HTTP method
`DELETE`

Description
delete collection of IPAddress

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
list or watch objects of kind IPAddress

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`IPAddressList`](../objects/index.md#io-k8s-api-networking-v1-IPAddressList) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`POST`

Description
create an IPAddress

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`IPAddress`](ipaddress-networking-k8s-io-v1.md#ipaddress-networking-k8s-io-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`IPAddress`](ipaddress-networking-k8s-io-v1.md#ipaddress-networking-k8s-io-v1) schema |
| 201 - Created | [`IPAddress`](ipaddress-networking-k8s-io-v1.md#ipaddress-networking-k8s-io-v1) schema |
| 202 - Accepted | [`IPAddress`](ipaddress-networking-k8s-io-v1.md#ipaddress-networking-k8s-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/networking.k8s.io/v1/watch/ipaddresses

HTTP method
`GET`

Description
watch individual changes to a list of IPAddress. deprecated: use the 'watch' parameter with a list operation instead.

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`WatchEvent`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/networking.k8s.io/v1/ipaddresses/{name}

| Parameter | Type     | Description           |
|-----------|----------|-----------------------|
| `name`    | `string` | name of the IPAddress |

Global path parameters

HTTP method
`DELETE`

Description
delete an IPAddress

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
read the specified IPAddress

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`IPAddress`](ipaddress-networking-k8s-io-v1.md#ipaddress-networking-k8s-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PATCH`

Description
partially update the specified IPAddress

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`IPAddress`](ipaddress-networking-k8s-io-v1.md#ipaddress-networking-k8s-io-v1) schema |
| 201 - Created | [`IPAddress`](ipaddress-networking-k8s-io-v1.md#ipaddress-networking-k8s-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PUT`

Description
replace the specified IPAddress

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`IPAddress`](ipaddress-networking-k8s-io-v1.md#ipaddress-networking-k8s-io-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`IPAddress`](ipaddress-networking-k8s-io-v1.md#ipaddress-networking-k8s-io-v1) schema |
| 201 - Created | [`IPAddress`](ipaddress-networking-k8s-io-v1.md#ipaddress-networking-k8s-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/networking.k8s.io/v1/watch/ipaddresses/{name}

| Parameter | Type     | Description           |
|-----------|----------|-----------------------|
| `name`    | `string` | name of the IPAddress |

Global path parameters

HTTP method
`GET`

Description
watch changes to an object of kind IPAddress. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`WatchEvent`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema |
| 401 - Unauthorized | Empty |

HTTP responses
