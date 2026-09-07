<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Description
Metal3Remediation is the Schema for the metal3remediations API.

Type
`object`

# Specification

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ObjectMeta`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) | Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |
| `spec` | `object` | Metal3RemediationSpec defines the desired state of Metal3Remediation. |
| `status` | `object` | Metal3RemediationStatus defines the observed state of Metal3Remediation. |

## .spec

Description
Metal3RemediationSpec defines the desired state of Metal3Remediation.

Type
`object`

| Property   | Type     | Description                                  |
|------------|----------|----------------------------------------------|
| `strategy` | `object` | Strategy field defines remediation strategy. |

## .spec.strategy

Description
Strategy field defines remediation strategy.

Type
`object`

| Property     | Type      | Description                                   |
|--------------|-----------|-----------------------------------------------|
| `retryLimit` | `integer` | Sets maximum number of remediation retries.   |
| `timeout`    | `string`  | Sets the timeout between remediation retries. |
| `type`       | `string`  | Type of remediation.                          |

## .status

Description
Metal3RemediationStatus defines the observed state of Metal3Remediation.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `lastRemediated` | `string` | LastRemediated identifies when the host was last remediated |
| `phase` | `string` | Phase represents the current phase of machine remediation. E.g. Pending, Running, Done etc. |
| `retryCount` | `integer` | RetryCount can be used as a counter during the remediation. Field can hold number of reboots etc. |

# API endpoints

The following API endpoints are available:

- `/apis/infrastructure.cluster.x-k8s.io/v1beta1/metal3remediations`

  - `GET`: list objects of kind Metal3Remediation

- `/apis/infrastructure.cluster.x-k8s.io/v1beta1/namespaces/{namespace}/metal3remediations`

  - `DELETE`: delete collection of Metal3Remediation

  - `GET`: list objects of kind Metal3Remediation

  - `POST`: create a Metal3Remediation

- `/apis/infrastructure.cluster.x-k8s.io/v1beta1/namespaces/{namespace}/metal3remediations/{name}`

  - `DELETE`: delete a Metal3Remediation

  - `GET`: read the specified Metal3Remediation

  - `PATCH`: partially update the specified Metal3Remediation

  - `PUT`: replace the specified Metal3Remediation

- `/apis/infrastructure.cluster.x-k8s.io/v1beta1/namespaces/{namespace}/metal3remediations/{name}/status`

  - `GET`: read status of the specified Metal3Remediation

  - `PATCH`: partially update status of the specified Metal3Remediation

  - `PUT`: replace status of the specified Metal3Remediation

## /apis/infrastructure.cluster.x-k8s.io/v1beta1/metal3remediations

HTTP method
`GET`

Description
list objects of kind Metal3Remediation

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Metal3RemediationList`](../objects/index.md#io-x-k8s-cluster-infrastructure-v1beta1-Metal3RemediationList) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/infrastructure.cluster.x-k8s.io/v1beta1/namespaces/{namespace}/metal3remediations

HTTP method
`DELETE`

Description
delete collection of Metal3Remediation

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Status`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`GET`

Description
list objects of kind Metal3Remediation

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Metal3RemediationList`](../objects/index.md#io-x-k8s-cluster-infrastructure-v1beta1-Metal3RemediationList) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`POST`

Description
create a Metal3Remediation

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`Metal3Remediation`](metal3remediation-infrastructure-cluster-x-k8s-io-v1beta1.md#metal3remediation-infrastructure-cluster-x-k8s-io-v1beta1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Metal3Remediation`](metal3remediation-infrastructure-cluster-x-k8s-io-v1beta1.md#metal3remediation-infrastructure-cluster-x-k8s-io-v1beta1) schema |
| 201 - Created | [`Metal3Remediation`](metal3remediation-infrastructure-cluster-x-k8s-io-v1beta1.md#metal3remediation-infrastructure-cluster-x-k8s-io-v1beta1) schema |
| 202 - Accepted | [`Metal3Remediation`](metal3remediation-infrastructure-cluster-x-k8s-io-v1beta1.md#metal3remediation-infrastructure-cluster-x-k8s-io-v1beta1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/infrastructure.cluster.x-k8s.io/v1beta1/namespaces/{namespace}/metal3remediations/{name}

| Parameter | Type     | Description                   |
|-----------|----------|-------------------------------|
| `name`    | `string` | name of the Metal3Remediation |

Global path parameters

HTTP method
`DELETE`

Description
delete a Metal3Remediation

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
read the specified Metal3Remediation

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Metal3Remediation`](metal3remediation-infrastructure-cluster-x-k8s-io-v1beta1.md#metal3remediation-infrastructure-cluster-x-k8s-io-v1beta1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PATCH`

Description
partially update the specified Metal3Remediation

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Metal3Remediation`](metal3remediation-infrastructure-cluster-x-k8s-io-v1beta1.md#metal3remediation-infrastructure-cluster-x-k8s-io-v1beta1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PUT`

Description
replace the specified Metal3Remediation

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`Metal3Remediation`](metal3remediation-infrastructure-cluster-x-k8s-io-v1beta1.md#metal3remediation-infrastructure-cluster-x-k8s-io-v1beta1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Metal3Remediation`](metal3remediation-infrastructure-cluster-x-k8s-io-v1beta1.md#metal3remediation-infrastructure-cluster-x-k8s-io-v1beta1) schema |
| 201 - Created | [`Metal3Remediation`](metal3remediation-infrastructure-cluster-x-k8s-io-v1beta1.md#metal3remediation-infrastructure-cluster-x-k8s-io-v1beta1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/infrastructure.cluster.x-k8s.io/v1beta1/namespaces/{namespace}/metal3remediations/{name}/status

| Parameter | Type     | Description                   |
|-----------|----------|-------------------------------|
| `name`    | `string` | name of the Metal3Remediation |

Global path parameters

HTTP method
`GET`

Description
read status of the specified Metal3Remediation

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Metal3Remediation`](metal3remediation-infrastructure-cluster-x-k8s-io-v1beta1.md#metal3remediation-infrastructure-cluster-x-k8s-io-v1beta1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PATCH`

Description
partially update status of the specified Metal3Remediation

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Metal3Remediation`](metal3remediation-infrastructure-cluster-x-k8s-io-v1beta1.md#metal3remediation-infrastructure-cluster-x-k8s-io-v1beta1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PUT`

Description
replace status of the specified Metal3Remediation

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`Metal3Remediation`](metal3remediation-infrastructure-cluster-x-k8s-io-v1beta1.md#metal3remediation-infrastructure-cluster-x-k8s-io-v1beta1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Metal3Remediation`](metal3remediation-infrastructure-cluster-x-k8s-io-v1beta1.md#metal3remediation-infrastructure-cluster-x-k8s-io-v1beta1) schema |
| 201 - Created | [`Metal3Remediation`](metal3remediation-infrastructure-cluster-x-k8s-io-v1beta1.md#metal3remediation-infrastructure-cluster-x-k8s-io-v1beta1) schema |
| 401 - Unauthorized | Empty |

HTTP responses
