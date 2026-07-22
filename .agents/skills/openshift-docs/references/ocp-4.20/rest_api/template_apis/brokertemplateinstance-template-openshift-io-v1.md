<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Description
BrokerTemplateInstance holds the service broker-related state associated with a TemplateInstance. BrokerTemplateInstance is part of an experimental API.

Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).

Type
`object`

Required
- `spec`

# Specification

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ObjectMeta_v2`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta_v2) | metadata is the standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |
| `spec` | `object` | BrokerTemplateInstanceSpec describes the state of a BrokerTemplateInstance. |

## .spec

Description
BrokerTemplateInstanceSpec describes the state of a BrokerTemplateInstance.

Type
`object`

Required
- `templateInstance`

- `secret`

| Property | Type | Description |
|----|----|----|
| `bindingIDs` | `array (string)` | bindingids is a list of 'binding_id’s provided during successive bind calls to the template service broker. |
| `secret` | [`ObjectReference`](../objects/index.md#io-k8s-api-core-v1-ObjectReference) | secret is a reference to a Secret object residing in a namespace, containing the necessary template parameters. |
| `templateInstance` | [`ObjectReference`](../objects/index.md#io-k8s-api-core-v1-ObjectReference) | templateinstance is a reference to a TemplateInstance object residing in a namespace. |

# API endpoints

The following API endpoints are available:

- `/apis/template.openshift.io/v1/brokertemplateinstances`

  - `DELETE`: delete collection of BrokerTemplateInstance

  - `GET`: list or watch objects of kind BrokerTemplateInstance

  - `POST`: create a BrokerTemplateInstance

- `/apis/template.openshift.io/v1/watch/brokertemplateinstances`

  - `GET`: watch individual changes to a list of BrokerTemplateInstance. deprecated: use the 'watch' parameter with a list operation instead.

- `/apis/template.openshift.io/v1/brokertemplateinstances/{name}`

  - `DELETE`: delete a BrokerTemplateInstance

  - `GET`: read the specified BrokerTemplateInstance

  - `PATCH`: partially update the specified BrokerTemplateInstance

  - `PUT`: replace the specified BrokerTemplateInstance

- `/apis/template.openshift.io/v1/watch/brokertemplateinstances/{name}`

  - `GET`: watch changes to an object of kind BrokerTemplateInstance. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.

## /apis/template.openshift.io/v1/brokertemplateinstances

HTTP method
`DELETE`

Description
delete collection of BrokerTemplateInstance

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |

Query parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Status_v9`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-Status_v9) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`GET`

Description
list or watch objects of kind BrokerTemplateInstance

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`BrokerTemplateInstanceList`](../objects/index.md#com-github-openshift-api-template-v1-BrokerTemplateInstanceList) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`POST`

Description
create a BrokerTemplateInstance

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`BrokerTemplateInstance`](brokertemplateinstance-template-openshift-io-v1.md#brokertemplateinstance-template-openshift-io-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`BrokerTemplateInstance`](brokertemplateinstance-template-openshift-io-v1.md#brokertemplateinstance-template-openshift-io-v1) schema |
| 201 - Created | [`BrokerTemplateInstance`](brokertemplateinstance-template-openshift-io-v1.md#brokertemplateinstance-template-openshift-io-v1) schema |
| 202 - Accepted | [`BrokerTemplateInstance`](brokertemplateinstance-template-openshift-io-v1.md#brokertemplateinstance-template-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/template.openshift.io/v1/watch/brokertemplateinstances

HTTP method
`GET`

Description
watch individual changes to a list of BrokerTemplateInstance. deprecated: use the 'watch' parameter with a list operation instead.

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`WatchEvent`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/template.openshift.io/v1/brokertemplateinstances/{name}

| Parameter | Type     | Description                        |
|-----------|----------|------------------------------------|
| `name`    | `string` | name of the BrokerTemplateInstance |

Global path parameters

HTTP method
`DELETE`

Description
delete a BrokerTemplateInstance

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |

Query parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Status_v9`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-Status_v9) schema |
| 202 - Accepted | [`Status_v9`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-Status_v9) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`GET`

Description
read the specified BrokerTemplateInstance

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`BrokerTemplateInstance`](brokertemplateinstance-template-openshift-io-v1.md#brokertemplateinstance-template-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PATCH`

Description
partially update the specified BrokerTemplateInstance

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`BrokerTemplateInstance`](brokertemplateinstance-template-openshift-io-v1.md#brokertemplateinstance-template-openshift-io-v1) schema |
| 201 - Created | [`BrokerTemplateInstance`](brokertemplateinstance-template-openshift-io-v1.md#brokertemplateinstance-template-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PUT`

Description
replace the specified BrokerTemplateInstance

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`BrokerTemplateInstance`](brokertemplateinstance-template-openshift-io-v1.md#brokertemplateinstance-template-openshift-io-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`BrokerTemplateInstance`](brokertemplateinstance-template-openshift-io-v1.md#brokertemplateinstance-template-openshift-io-v1) schema |
| 201 - Created | [`BrokerTemplateInstance`](brokertemplateinstance-template-openshift-io-v1.md#brokertemplateinstance-template-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/template.openshift.io/v1/watch/brokertemplateinstances/{name}

| Parameter | Type     | Description                        |
|-----------|----------|------------------------------------|
| `name`    | `string` | name of the BrokerTemplateInstance |

Global path parameters

HTTP method
`GET`

Description
watch changes to an object of kind BrokerTemplateInstance. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`WatchEvent`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema |
| 401 - Unauthorized | Empty |

HTTP responses
