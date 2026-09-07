<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Description
MachineAutoscaler is the Schema for the machineautoscalers API

Type
`object`

# Specification

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ObjectMeta`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) | Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |
| `spec` | `object` | Specification of constraints of a scalable resource |
| `status` | `object` | Most recently observed status of a scalable resource |

## .spec

Description
Specification of constraints of a scalable resource

Type
`object`

Required
- `maxReplicas`

- `minReplicas`

- `scaleTargetRef`

| Property | Type | Description |
|----|----|----|
| `maxReplicas` | `integer` | MaxReplicas constrains the maximal number of replicas of a scalable resource |
| `minReplicas` | `integer` | MinReplicas constrains the minimal number of replicas of a scalable resource |
| `scaleTargetRef` | `object` | ScaleTargetRef holds reference to a scalable resource |

## .spec.scaleTargetRef

Description
ScaleTargetRef holds reference to a scalable resource

Type
`object`

Required
- `kind`

- `name`

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `name` | `string` | Name specifies a name of an object, e.g. worker-us-east-1a. Scalable resources are expected to exist under a single namespace. |

## .status

Description
Most recently observed status of a scalable resource

Type
`object`

| Property | Type | Description |
|----|----|----|
| `lastTargetRef` | `object` | LastTargetRef holds reference to the recently observed scalable resource |

## .status.lastTargetRef

Description
LastTargetRef holds reference to the recently observed scalable resource

Type
`object`

Required
- `kind`

- `name`

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `name` | `string` | Name specifies a name of an object, e.g. worker-us-east-1a. Scalable resources are expected to exist under a single namespace. |

# API endpoints

The following API endpoints are available:

- `/apis/autoscaling.openshift.io/v1beta1/machineautoscalers`

  - `GET`: list objects of kind MachineAutoscaler

- `/apis/autoscaling.openshift.io/v1beta1/namespaces/{namespace}/machineautoscalers`

  - `DELETE`: delete collection of MachineAutoscaler

  - `GET`: list objects of kind MachineAutoscaler

  - `POST`: create a MachineAutoscaler

- `/apis/autoscaling.openshift.io/v1beta1/namespaces/{namespace}/machineautoscalers/{name}`

  - `DELETE`: delete a MachineAutoscaler

  - `GET`: read the specified MachineAutoscaler

  - `PATCH`: partially update the specified MachineAutoscaler

  - `PUT`: replace the specified MachineAutoscaler

- `/apis/autoscaling.openshift.io/v1beta1/namespaces/{namespace}/machineautoscalers/{name}/status`

  - `GET`: read status of the specified MachineAutoscaler

  - `PATCH`: partially update status of the specified MachineAutoscaler

  - `PUT`: replace status of the specified MachineAutoscaler

## /apis/autoscaling.openshift.io/v1beta1/machineautoscalers

HTTP method
`GET`

Description
list objects of kind MachineAutoscaler

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`MachineAutoscalerList`](../objects/index.md#io-openshift-autoscaling-v1beta1-MachineAutoscalerList) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/autoscaling.openshift.io/v1beta1/namespaces/{namespace}/machineautoscalers

HTTP method
`DELETE`

Description
delete collection of MachineAutoscaler

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Status`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`GET`

Description
list objects of kind MachineAutoscaler

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`MachineAutoscalerList`](../objects/index.md#io-openshift-autoscaling-v1beta1-MachineAutoscalerList) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`POST`

Description
create a MachineAutoscaler

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`MachineAutoscaler`](machineautoscaler-autoscaling-openshift-io-v1beta1.md#machineautoscaler-autoscaling-openshift-io-v1beta1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`MachineAutoscaler`](machineautoscaler-autoscaling-openshift-io-v1beta1.md#machineautoscaler-autoscaling-openshift-io-v1beta1) schema |
| 201 - Created | [`MachineAutoscaler`](machineautoscaler-autoscaling-openshift-io-v1beta1.md#machineautoscaler-autoscaling-openshift-io-v1beta1) schema |
| 202 - Accepted | [`MachineAutoscaler`](machineautoscaler-autoscaling-openshift-io-v1beta1.md#machineautoscaler-autoscaling-openshift-io-v1beta1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/autoscaling.openshift.io/v1beta1/namespaces/{namespace}/machineautoscalers/{name}

| Parameter | Type     | Description                   |
|-----------|----------|-------------------------------|
| `name`    | `string` | name of the MachineAutoscaler |

Global path parameters

HTTP method
`DELETE`

Description
delete a MachineAutoscaler

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
read the specified MachineAutoscaler

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`MachineAutoscaler`](machineautoscaler-autoscaling-openshift-io-v1beta1.md#machineautoscaler-autoscaling-openshift-io-v1beta1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PATCH`

Description
partially update the specified MachineAutoscaler

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`MachineAutoscaler`](machineautoscaler-autoscaling-openshift-io-v1beta1.md#machineautoscaler-autoscaling-openshift-io-v1beta1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PUT`

Description
replace the specified MachineAutoscaler

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`MachineAutoscaler`](machineautoscaler-autoscaling-openshift-io-v1beta1.md#machineautoscaler-autoscaling-openshift-io-v1beta1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`MachineAutoscaler`](machineautoscaler-autoscaling-openshift-io-v1beta1.md#machineautoscaler-autoscaling-openshift-io-v1beta1) schema |
| 201 - Created | [`MachineAutoscaler`](machineautoscaler-autoscaling-openshift-io-v1beta1.md#machineautoscaler-autoscaling-openshift-io-v1beta1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/autoscaling.openshift.io/v1beta1/namespaces/{namespace}/machineautoscalers/{name}/status

| Parameter | Type     | Description                   |
|-----------|----------|-------------------------------|
| `name`    | `string` | name of the MachineAutoscaler |

Global path parameters

HTTP method
`GET`

Description
read status of the specified MachineAutoscaler

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`MachineAutoscaler`](machineautoscaler-autoscaling-openshift-io-v1beta1.md#machineautoscaler-autoscaling-openshift-io-v1beta1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PATCH`

Description
partially update status of the specified MachineAutoscaler

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`MachineAutoscaler`](machineautoscaler-autoscaling-openshift-io-v1beta1.md#machineautoscaler-autoscaling-openshift-io-v1beta1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PUT`

Description
replace status of the specified MachineAutoscaler

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`MachineAutoscaler`](machineautoscaler-autoscaling-openshift-io-v1beta1.md#machineautoscaler-autoscaling-openshift-io-v1beta1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`MachineAutoscaler`](machineautoscaler-autoscaling-openshift-io-v1beta1.md#machineautoscaler-autoscaling-openshift-io-v1beta1) schema |
| 201 - Created | [`MachineAutoscaler`](machineautoscaler-autoscaling-openshift-io-v1beta1.md#machineautoscaler-autoscaling-openshift-io-v1beta1) schema |
| 401 - Unauthorized | Empty |

HTTP responses
