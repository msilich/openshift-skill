<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Description
EgressFirewall describes the current egress firewall for a Namespace. Traffic from a pod to an IP address outside the cluster will be checked against each EgressFirewallRule in the pod’s namespace’s EgressFirewall, in order. If no rule matches (or no EgressFirewall is present) then the traffic will be allowed by default.

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
| `spec` | `object` | Specification of the desired behavior of EgressFirewall. |
| `status` | `object` | Observed status of EgressFirewall |

## .spec

Description
Specification of the desired behavior of EgressFirewall.

Type
`object`

Required
- `egress`

| Property | Type | Description |
|----|----|----|
| `egress` | `array` | a collection of egress firewall rule objects |
| `egress[]` | `object` | EgressFirewallRule is a single egressfirewall rule object |

## .spec.egress

Description
a collection of egress firewall rule objects

Type
`array`

## .spec.egress\[\]

Description
EgressFirewallRule is a single egressfirewall rule object

Type
`object`

Required
- `to`

- `type`

| Property | Type | Description |
|----|----|----|
| `ports` | `array` | ports specify what ports and protocols the rule applies to |
| `ports[]` | `object` | EgressFirewallPort specifies the port to allow or deny traffic to |
| `to` | `object` | to is the target that traffic is allowed/denied to |
| `type` | `string` | type marks this as an "Allow" or "Deny" rule |

## .spec.egress\[\].ports

Description
ports specify what ports and protocols the rule applies to

Type
`array`

## .spec.egress\[\].ports\[\]

Description
EgressFirewallPort specifies the port to allow or deny traffic to

Type
`object`

Required
- `port`

- `protocol`

| Property | Type | Description |
|----|----|----|
| `port` | `integer` | port that the traffic must match |
| `protocol` | `string` | protocol (tcp, udp, sctp) that the traffic must match. |

## .spec.egress\[\].to

Description
to is the target that traffic is allowed/denied to

Type
`object`

| Property | Type | Description |
|----|----|----|
| `cidrSelector` | `string` | cidrSelector is the CIDR range to allow/deny traffic to. If this is set, dnsName and nodeSelector must be unset. |
| `dnsName` | `string` | dnsName is the domain name to allow/deny traffic to. If this is set, cidrSelector and nodeSelector must be unset. For a wildcard DNS name, the '**' will match only one label. Additionally, only a single '**' can be used at the beginning of the wildcard DNS name. For example, '\*.example.com' will match 'sub1.example.com' but won’t match 'sub2.sub1.example.com'. |
| `nodeSelector` | `object` | nodeSelector will allow/deny traffic to the Kubernetes node IP of selected nodes. If this is set, cidrSelector and DNSName must be unset. |

## .spec.egress\[\].to.nodeSelector

Description
nodeSelector will allow/deny traffic to the Kubernetes node IP of selected nodes. If this is set, cidrSelector and DNSName must be unset.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `matchExpressions` | `array` | matchExpressions is a list of label selector requirements. The requirements are ANDed. |
| `matchExpressions[]` | `object` | A label selector requirement is a selector that contains values, a key, and an operator that relates the key and values. |
| `matchLabels` | `object (string)` | matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed. |

## .spec.egress\[\].to.nodeSelector.matchExpressions

Description
matchExpressions is a list of label selector requirements. The requirements are ANDed.

Type
`array`

## .spec.egress\[\].to.nodeSelector.matchExpressions\[\]

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
Observed status of EgressFirewall

Type
`object`

| Property   | Type             | Description |
|------------|------------------|-------------|
| `messages` | `array (string)` |             |
| `status`   | `string`         |             |

# API endpoints

The following API endpoints are available:

- `/apis/k8s.ovn.org/v1/egressfirewalls`

  - `GET`: list objects of kind EgressFirewall

- `/apis/k8s.ovn.org/v1/namespaces/{namespace}/egressfirewalls`

  - `DELETE`: delete collection of EgressFirewall

  - `GET`: list objects of kind EgressFirewall

  - `POST`: create an EgressFirewall

- `/apis/k8s.ovn.org/v1/namespaces/{namespace}/egressfirewalls/{name}`

  - `DELETE`: delete an EgressFirewall

  - `GET`: read the specified EgressFirewall

  - `PATCH`: partially update the specified EgressFirewall

  - `PUT`: replace the specified EgressFirewall

- `/apis/k8s.ovn.org/v1/namespaces/{namespace}/egressfirewalls/{name}/status`

  - `GET`: read status of the specified EgressFirewall

  - `PATCH`: partially update status of the specified EgressFirewall

  - `PUT`: replace status of the specified EgressFirewall

## /apis/k8s.ovn.org/v1/egressfirewalls

HTTP method
`GET`

Description
list objects of kind EgressFirewall

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`EgressFirewallList`](../objects/index.md#org-ovn-k8s-v1-EgressFirewallList) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/k8s.ovn.org/v1/namespaces/{namespace}/egressfirewalls

HTTP method
`DELETE`

Description
delete collection of EgressFirewall

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Status`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`GET`

Description
list objects of kind EgressFirewall

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`EgressFirewallList`](../objects/index.md#org-ovn-k8s-v1-EgressFirewallList) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`POST`

Description
create an EgressFirewall

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`EgressFirewall`](egressfirewall-k8s-ovn-org-v1.md#egressfirewall-k8s-ovn-org-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`EgressFirewall`](egressfirewall-k8s-ovn-org-v1.md#egressfirewall-k8s-ovn-org-v1) schema |
| 201 - Created | [`EgressFirewall`](egressfirewall-k8s-ovn-org-v1.md#egressfirewall-k8s-ovn-org-v1) schema |
| 202 - Accepted | [`EgressFirewall`](egressfirewall-k8s-ovn-org-v1.md#egressfirewall-k8s-ovn-org-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/k8s.ovn.org/v1/namespaces/{namespace}/egressfirewalls/{name}

| Parameter | Type     | Description                |
|-----------|----------|----------------------------|
| `name`    | `string` | name of the EgressFirewall |

Global path parameters

HTTP method
`DELETE`

Description
delete an EgressFirewall

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
read the specified EgressFirewall

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`EgressFirewall`](egressfirewall-k8s-ovn-org-v1.md#egressfirewall-k8s-ovn-org-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PATCH`

Description
partially update the specified EgressFirewall

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`EgressFirewall`](egressfirewall-k8s-ovn-org-v1.md#egressfirewall-k8s-ovn-org-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PUT`

Description
replace the specified EgressFirewall

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`EgressFirewall`](egressfirewall-k8s-ovn-org-v1.md#egressfirewall-k8s-ovn-org-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`EgressFirewall`](egressfirewall-k8s-ovn-org-v1.md#egressfirewall-k8s-ovn-org-v1) schema |
| 201 - Created | [`EgressFirewall`](egressfirewall-k8s-ovn-org-v1.md#egressfirewall-k8s-ovn-org-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/k8s.ovn.org/v1/namespaces/{namespace}/egressfirewalls/{name}/status

| Parameter | Type     | Description                |
|-----------|----------|----------------------------|
| `name`    | `string` | name of the EgressFirewall |

Global path parameters

HTTP method
`GET`

Description
read status of the specified EgressFirewall

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`EgressFirewall`](egressfirewall-k8s-ovn-org-v1.md#egressfirewall-k8s-ovn-org-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PATCH`

Description
partially update status of the specified EgressFirewall

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`EgressFirewall`](egressfirewall-k8s-ovn-org-v1.md#egressfirewall-k8s-ovn-org-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PUT`

Description
replace status of the specified EgressFirewall

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`EgressFirewall`](egressfirewall-k8s-ovn-org-v1.md#egressfirewall-k8s-ovn-org-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`EgressFirewall`](egressfirewall-k8s-ovn-org-v1.md#egressfirewall-k8s-ovn-org-v1) schema |
| 201 - Created | [`EgressFirewall`](egressfirewall-k8s-ovn-org-v1.md#egressfirewall-k8s-ovn-org-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses
