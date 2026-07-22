<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Description
AdminPolicyBasedExternalRoute is a CRD allowing the cluster administrators to configure policies for external gateway IPs to be applied to all the pods contained in selected namespaces. Egress traffic from the pods that belong to the selected namespaces to outside the cluster is routed through these external gateway IPs.

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
| `spec` | `object` | AdminPolicyBasedExternalRouteSpec defines the desired state of AdminPolicyBasedExternalRoute |
| `status` | `object` | AdminPolicyBasedRouteStatus contains the observed status of the AdminPolicyBased route types. |

## .spec

Description
AdminPolicyBasedExternalRouteSpec defines the desired state of AdminPolicyBasedExternalRoute

Type
`object`

Required
- `from`

- `nextHops`

| Property | Type | Description |
|----|----|----|
| `from` | `object` | From defines the selectors that will determine the target namespaces to this CR. |
| `nextHops` | `object` | NextHops defines two types of hops: Static and Dynamic. Each hop defines at least one external gateway IP. |

## .spec.from

Description
From defines the selectors that will determine the target namespaces to this CR.

Type
`object`

Required
- `namespaceSelector`

| Property | Type | Description |
|----|----|----|
| `namespaceSelector` | `object` | NamespaceSelector defines a selector to be used to determine which namespaces will be targeted by this CR |

## .spec.from.namespaceSelector

Description
NamespaceSelector defines a selector to be used to determine which namespaces will be targeted by this CR

Type
`object`

| Property | Type | Description |
|----|----|----|
| `matchExpressions` | `array` | matchExpressions is a list of label selector requirements. The requirements are ANDed. |
| `matchExpressions[]` | `object` | A label selector requirement is a selector that contains values, a key, and an operator that relates the key and values. |
| `matchLabels` | `object (string)` | matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed. |

## .spec.from.namespaceSelector.matchExpressions

Description
matchExpressions is a list of label selector requirements. The requirements are ANDed.

Type
`array`

## .spec.from.namespaceSelector.matchExpressions\[\]

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

## .spec.nextHops

Description
NextHops defines two types of hops: Static and Dynamic. Each hop defines at least one external gateway IP.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `dynamic` | `array` | DynamicHops defines a slices of DynamicHop. This field is optional. |
| `dynamic[]` | `object` | DynamicHop defines the configuration for a dynamic external gateway interface. These interfaces are wrapped around a pod object that resides inside the cluster. The field NetworkAttachmentName captures the name of the multus network name to use when retrieving the gateway IP to use. The PodSelector and the NamespaceSelector are mandatory fields. |
| `static` | `array` | StaticHops defines a slice of StaticHop. This field is optional. |
| `static[]` | `object` | StaticHop defines the configuration of a static IP that acts as an external Gateway Interface. IP field is mandatory. |

## .spec.nextHops.dynamic

Description
DynamicHops defines a slices of DynamicHop. This field is optional.

Type
`array`

## .spec.nextHops.dynamic\[\]

Description
DynamicHop defines the configuration for a dynamic external gateway interface. These interfaces are wrapped around a pod object that resides inside the cluster. The field NetworkAttachmentName captures the name of the multus network name to use when retrieving the gateway IP to use. The PodSelector and the NamespaceSelector are mandatory fields.

Type
`object`

Required
- `namespaceSelector`

- `podSelector`

| Property | Type | Description |
|----|----|----|
| `bfdEnabled` | `boolean` | BFDEnabled determines if the interface implements the Bidirectional Forward Detection protocol. Defaults to false. |
| `namespaceSelector` | `object` | NamespaceSelector defines a selector to filter the namespaces where the pod gateways are located. |
| `networkAttachmentName` | `string` | NetworkAttachmentName determines the multus network name to use when retrieving the pod IPs that will be used as the gateway IP. When this field is empty, the logic assumes that the pod is configured with HostNetwork and is using the node’s IP as gateway. |
| `podSelector` | `object` | PodSelector defines the selector to filter the pods that are external gateways. |

## .spec.nextHops.dynamic\[\].namespaceSelector

Description
NamespaceSelector defines a selector to filter the namespaces where the pod gateways are located.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `matchExpressions` | `array` | matchExpressions is a list of label selector requirements. The requirements are ANDed. |
| `matchExpressions[]` | `object` | A label selector requirement is a selector that contains values, a key, and an operator that relates the key and values. |
| `matchLabels` | `object (string)` | matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed. |

## .spec.nextHops.dynamic\[\].namespaceSelector.matchExpressions

Description
matchExpressions is a list of label selector requirements. The requirements are ANDed.

Type
`array`

## .spec.nextHops.dynamic\[\].namespaceSelector.matchExpressions\[\]

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

## .spec.nextHops.dynamic\[\].podSelector

Description
PodSelector defines the selector to filter the pods that are external gateways.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `matchExpressions` | `array` | matchExpressions is a list of label selector requirements. The requirements are ANDed. |
| `matchExpressions[]` | `object` | A label selector requirement is a selector that contains values, a key, and an operator that relates the key and values. |
| `matchLabels` | `object (string)` | matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed. |

## .spec.nextHops.dynamic\[\].podSelector.matchExpressions

Description
matchExpressions is a list of label selector requirements. The requirements are ANDed.

Type
`array`

## .spec.nextHops.dynamic\[\].podSelector.matchExpressions\[\]

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

## .spec.nextHops.static

Description
StaticHops defines a slice of StaticHop. This field is optional.

Type
`array`

## .spec.nextHops.static\[\]

Description
StaticHop defines the configuration of a static IP that acts as an external Gateway Interface. IP field is mandatory.

Type
`object`

Required
- `ip`

| Property | Type | Description |
|----|----|----|
| `bfdEnabled` | `boolean` | BFDEnabled determines if the interface implements the Bidirectional Forward Detection protocol. Defaults to false. |
| `ip` | `string` | IP defines the static IP to be used for egress traffic. The IP can be either IPv4 or IPv6. |

## .status

Description
AdminPolicyBasedRouteStatus contains the observed status of the AdminPolicyBased route types.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `lastTransitionTime` | `string` | Captures the time when the last change was applied. |
| `messages` | `array (string)` | An array of Human-readable messages indicating details about the status of the object. |
| `status` | `string` | A concise indication of whether the AdminPolicyBasedRoute resource is applied with success |

# API endpoints

The following API endpoints are available:

- `/apis/k8s.ovn.org/v1/adminpolicybasedexternalroutes`

  - `DELETE`: delete collection of AdminPolicyBasedExternalRoute

  - `GET`: list objects of kind AdminPolicyBasedExternalRoute

  - `POST`: create an AdminPolicyBasedExternalRoute

- `/apis/k8s.ovn.org/v1/adminpolicybasedexternalroutes/{name}`

  - `DELETE`: delete an AdminPolicyBasedExternalRoute

  - `GET`: read the specified AdminPolicyBasedExternalRoute

  - `PATCH`: partially update the specified AdminPolicyBasedExternalRoute

  - `PUT`: replace the specified AdminPolicyBasedExternalRoute

- `/apis/k8s.ovn.org/v1/adminpolicybasedexternalroutes/{name}/status`

  - `GET`: read status of the specified AdminPolicyBasedExternalRoute

  - `PATCH`: partially update status of the specified AdminPolicyBasedExternalRoute

  - `PUT`: replace status of the specified AdminPolicyBasedExternalRoute

## /apis/k8s.ovn.org/v1/adminpolicybasedexternalroutes

HTTP method
`DELETE`

Description
delete collection of AdminPolicyBasedExternalRoute

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Status`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`GET`

Description
list objects of kind AdminPolicyBasedExternalRoute

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`AdminPolicyBasedExternalRouteList`](../objects/index.md#org-ovn-k8s-v1-AdminPolicyBasedExternalRouteList) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`POST`

Description
create an AdminPolicyBasedExternalRoute

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`AdminPolicyBasedExternalRoute`](adminpolicybasedexternalroute-k8s-ovn-org-v1.md#adminpolicybasedexternalroute-k8s-ovn-org-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`AdminPolicyBasedExternalRoute`](adminpolicybasedexternalroute-k8s-ovn-org-v1.md#adminpolicybasedexternalroute-k8s-ovn-org-v1) schema |
| 201 - Created | [`AdminPolicyBasedExternalRoute`](adminpolicybasedexternalroute-k8s-ovn-org-v1.md#adminpolicybasedexternalroute-k8s-ovn-org-v1) schema |
| 202 - Accepted | [`AdminPolicyBasedExternalRoute`](adminpolicybasedexternalroute-k8s-ovn-org-v1.md#adminpolicybasedexternalroute-k8s-ovn-org-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/k8s.ovn.org/v1/adminpolicybasedexternalroutes/{name}

| Parameter | Type     | Description                               |
|-----------|----------|-------------------------------------------|
| `name`    | `string` | name of the AdminPolicyBasedExternalRoute |

Global path parameters

HTTP method
`DELETE`

Description
delete an AdminPolicyBasedExternalRoute

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
read the specified AdminPolicyBasedExternalRoute

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`AdminPolicyBasedExternalRoute`](adminpolicybasedexternalroute-k8s-ovn-org-v1.md#adminpolicybasedexternalroute-k8s-ovn-org-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PATCH`

Description
partially update the specified AdminPolicyBasedExternalRoute

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`AdminPolicyBasedExternalRoute`](adminpolicybasedexternalroute-k8s-ovn-org-v1.md#adminpolicybasedexternalroute-k8s-ovn-org-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PUT`

Description
replace the specified AdminPolicyBasedExternalRoute

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`AdminPolicyBasedExternalRoute`](adminpolicybasedexternalroute-k8s-ovn-org-v1.md#adminpolicybasedexternalroute-k8s-ovn-org-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`AdminPolicyBasedExternalRoute`](adminpolicybasedexternalroute-k8s-ovn-org-v1.md#adminpolicybasedexternalroute-k8s-ovn-org-v1) schema |
| 201 - Created | [`AdminPolicyBasedExternalRoute`](adminpolicybasedexternalroute-k8s-ovn-org-v1.md#adminpolicybasedexternalroute-k8s-ovn-org-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/k8s.ovn.org/v1/adminpolicybasedexternalroutes/{name}/status

| Parameter | Type     | Description                               |
|-----------|----------|-------------------------------------------|
| `name`    | `string` | name of the AdminPolicyBasedExternalRoute |

Global path parameters

HTTP method
`GET`

Description
read status of the specified AdminPolicyBasedExternalRoute

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`AdminPolicyBasedExternalRoute`](adminpolicybasedexternalroute-k8s-ovn-org-v1.md#adminpolicybasedexternalroute-k8s-ovn-org-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PATCH`

Description
partially update status of the specified AdminPolicyBasedExternalRoute

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`AdminPolicyBasedExternalRoute`](adminpolicybasedexternalroute-k8s-ovn-org-v1.md#adminpolicybasedexternalroute-k8s-ovn-org-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PUT`

Description
replace status of the specified AdminPolicyBasedExternalRoute

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`AdminPolicyBasedExternalRoute`](adminpolicybasedexternalroute-k8s-ovn-org-v1.md#adminpolicybasedexternalroute-k8s-ovn-org-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`AdminPolicyBasedExternalRoute`](adminpolicybasedexternalroute-k8s-ovn-org-v1.md#adminpolicybasedexternalroute-k8s-ovn-org-v1) schema |
| 201 - Created | [`AdminPolicyBasedExternalRoute`](adminpolicybasedexternalroute-k8s-ovn-org-v1.md#adminpolicybasedexternalroute-k8s-ovn-org-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses
