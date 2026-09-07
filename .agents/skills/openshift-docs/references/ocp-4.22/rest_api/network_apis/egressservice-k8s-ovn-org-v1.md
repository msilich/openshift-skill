<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Description
EgressService is a CRD that allows the user to request that the source IP of egress packets originating from all of the pods that are endpoints of the corresponding LoadBalancer Service would be its ingress IP. In addition, it allows the user to request that egress packets originating from all of the pods that are endpoints of the LoadBalancer service would use a different network than the main one.

Type
`object`

# Specification

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ObjectMeta`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) | Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |
| `spec` | `object` | EgressServiceSpec defines the desired state of EgressService |
| `status` | `object` | EgressServiceStatus defines the observed state of EgressService |

## .spec

Description
EgressServiceSpec defines the desired state of EgressService

Type
`object`

| Property | Type | Description |
|----|----|----|
| `network` | `string` | The network which this service should send egress and corresponding ingress replies to. This is typically implemented as VRF mapping, representing a numeric id or string name of a routing table which by omission uses the default host routing. |
| `nodeSelector` | `object` | Allows limiting the nodes that can be selected to handle the service’s traffic when sourceIPBy=LoadBalancerIP. When present only a node whose labels match the specified selectors can be selected for handling the service’s traffic. When it is not specified any node in the cluster can be chosen to manage the service’s traffic. |
| `sourceIPBy` | `string` | Determines the source IP of egress traffic originating from the pods backing the LoadBalancer Service. When `LoadBalancerIP` the source IP is set to its LoadBalancer ingress IP. When `Network` the source IP is set according to the interface of the Network, leveraging the masquerade rules that are already in place. Typically these rules specify SNAT to the IP of the outgoing interface, which means the packet will typically leave with the IP of the node. |

## .spec.nodeSelector

Description
Allows limiting the nodes that can be selected to handle the service’s traffic when sourceIPBy=LoadBalancerIP. When present only a node whose labels match the specified selectors can be selected for handling the service’s traffic. When it is not specified any node in the cluster can be chosen to manage the service’s traffic.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `matchExpressions` | `array` | matchExpressions is a list of label selector requirements. The requirements are ANDed. |
| `matchExpressions[]` | `object` | A label selector requirement is a selector that contains values, a key, and an operator that relates the key and values. |
| `matchLabels` | `object (string)` | matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed. |

## .spec.nodeSelector.matchExpressions

Description
matchExpressions is a list of label selector requirements. The requirements are ANDed.

Type
`array`

## .spec.nodeSelector.matchExpressions\[\]

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
EgressServiceStatus defines the observed state of EgressService

Type
`object`

Required
- `host`

| Property | Type | Description |
|----|----|----|
| `host` | `string` | The name of the node selected to handle the service’s traffic. In case sourceIPBy=Network the field will be set to "ALL". |

# API endpoints

The following API endpoints are available:

- `/apis/k8s.ovn.org/v1/egressservices`

  - `GET`: list objects of kind EgressService

- `/apis/k8s.ovn.org/v1/namespaces/{namespace}/egressservices`

  - `DELETE`: delete collection of EgressService

  - `GET`: list objects of kind EgressService

  - `POST`: create an EgressService

- `/apis/k8s.ovn.org/v1/namespaces/{namespace}/egressservices/{name}`

  - `DELETE`: delete an EgressService

  - `GET`: read the specified EgressService

  - `PATCH`: partially update the specified EgressService

  - `PUT`: replace the specified EgressService

- `/apis/k8s.ovn.org/v1/namespaces/{namespace}/egressservices/{name}/status`

  - `GET`: read status of the specified EgressService

  - `PATCH`: partially update status of the specified EgressService

  - `PUT`: replace status of the specified EgressService

## /apis/k8s.ovn.org/v1/egressservices

HTTP method
`GET`

Description
list objects of kind EgressService

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`EgressServiceList`](../objects/index.md#org-ovn-k8s-v1-EgressServiceList) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/k8s.ovn.org/v1/namespaces/{namespace}/egressservices

HTTP method
`DELETE`

Description
delete collection of EgressService

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Status`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`GET`

Description
list objects of kind EgressService

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`EgressServiceList`](../objects/index.md#org-ovn-k8s-v1-EgressServiceList) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`POST`

Description
create an EgressService

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`EgressService`](egressservice-k8s-ovn-org-v1.md#egressservice-k8s-ovn-org-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`EgressService`](egressservice-k8s-ovn-org-v1.md#egressservice-k8s-ovn-org-v1) schema |
| 201 - Created | [`EgressService`](egressservice-k8s-ovn-org-v1.md#egressservice-k8s-ovn-org-v1) schema |
| 202 - Accepted | [`EgressService`](egressservice-k8s-ovn-org-v1.md#egressservice-k8s-ovn-org-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/k8s.ovn.org/v1/namespaces/{namespace}/egressservices/{name}

| Parameter | Type     | Description               |
|-----------|----------|---------------------------|
| `name`    | `string` | name of the EgressService |

Global path parameters

HTTP method
`DELETE`

Description
delete an EgressService

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
read the specified EgressService

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`EgressService`](egressservice-k8s-ovn-org-v1.md#egressservice-k8s-ovn-org-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PATCH`

Description
partially update the specified EgressService

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`EgressService`](egressservice-k8s-ovn-org-v1.md#egressservice-k8s-ovn-org-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PUT`

Description
replace the specified EgressService

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`EgressService`](egressservice-k8s-ovn-org-v1.md#egressservice-k8s-ovn-org-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`EgressService`](egressservice-k8s-ovn-org-v1.md#egressservice-k8s-ovn-org-v1) schema |
| 201 - Created | [`EgressService`](egressservice-k8s-ovn-org-v1.md#egressservice-k8s-ovn-org-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/k8s.ovn.org/v1/namespaces/{namespace}/egressservices/{name}/status

| Parameter | Type     | Description               |
|-----------|----------|---------------------------|
| `name`    | `string` | name of the EgressService |

Global path parameters

HTTP method
`GET`

Description
read status of the specified EgressService

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`EgressService`](egressservice-k8s-ovn-org-v1.md#egressservice-k8s-ovn-org-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PATCH`

Description
partially update status of the specified EgressService

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`EgressService`](egressservice-k8s-ovn-org-v1.md#egressservice-k8s-ovn-org-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PUT`

Description
replace status of the specified EgressService

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`EgressService`](egressservice-k8s-ovn-org-v1.md#egressservice-k8s-ovn-org-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`EgressService`](egressservice-k8s-ovn-org-v1.md#egressservice-k8s-ovn-org-v1) schema |
| 201 - Created | [`EgressService`](egressservice-k8s-ovn-org-v1.md#egressservice-k8s-ovn-org-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses
