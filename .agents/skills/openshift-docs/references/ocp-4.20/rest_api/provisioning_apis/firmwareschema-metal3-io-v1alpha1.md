<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Description
FirmwareSchema is the Schema for the firmwareschemas API.

Type
`object`

# Specification

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ObjectMeta`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) | Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |
| `spec` | `object` | FirmwareSchemaSpec defines the desired state of FirmwareSchema. |

## .spec

Description
FirmwareSchemaSpec defines the desired state of FirmwareSchema.

Type
`object`

Required
- `schema`

| Property         | Type     | Description                                      |
|------------------|----------|--------------------------------------------------|
| `hardwareModel`  | `string` | The hardware model associated with this schema   |
| `hardwareVendor` | `string` | The hardware vendor associated with this schema  |
| `schema`         | `object` | Map of firmware name to schema                   |
| `schema{}`       | `object` | Additional data describing the firmware setting. |

## .spec.schema

Description
Map of firmware name to schema

Type
`object`

## .spec.schema{}

Description
Additional data describing the firmware setting.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `allowable_values` | `array (string)` | The allowable value for an Enumeration type setting. |
| `attribute_type` | `string` | The type of setting. |
| `lower_bound` | `integer` | The lowest value for an Integer type setting. |
| `max_length` | `integer` | Maximum length for a String type setting. |
| `min_length` | `integer` | Minimum length for a String type setting. |
| `read_only` | `boolean` | Whether or not this setting is read only. |
| `unique` | `boolean` | Whether or not this setting’s value is unique to this node, e.g. a serial number. |
| `upper_bound` | `integer` | The highest value for an Integer type setting. |

# API endpoints

The following API endpoints are available:

- `/apis/metal3.io/v1alpha1/firmwareschemas`

  - `GET`: list objects of kind FirmwareSchema

- `/apis/metal3.io/v1alpha1/namespaces/{namespace}/firmwareschemas`

  - `DELETE`: delete collection of FirmwareSchema

  - `GET`: list objects of kind FirmwareSchema

  - `POST`: create a FirmwareSchema

- `/apis/metal3.io/v1alpha1/namespaces/{namespace}/firmwareschemas/{name}`

  - `DELETE`: delete a FirmwareSchema

  - `GET`: read the specified FirmwareSchema

  - `PATCH`: partially update the specified FirmwareSchema

  - `PUT`: replace the specified FirmwareSchema

## /apis/metal3.io/v1alpha1/firmwareschemas

HTTP method
`GET`

Description
list objects of kind FirmwareSchema

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`FirmwareSchemaList`](../objects/index.md#io-metal3-v1alpha1-FirmwareSchemaList) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/metal3.io/v1alpha1/namespaces/{namespace}/firmwareschemas

HTTP method
`DELETE`

Description
delete collection of FirmwareSchema

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Status`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`GET`

Description
list objects of kind FirmwareSchema

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`FirmwareSchemaList`](../objects/index.md#io-metal3-v1alpha1-FirmwareSchemaList) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`POST`

Description
create a FirmwareSchema

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`FirmwareSchema`](firmwareschema-metal3-io-v1alpha1.md#firmwareschema-metal3-io-v1alpha1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`FirmwareSchema`](firmwareschema-metal3-io-v1alpha1.md#firmwareschema-metal3-io-v1alpha1) schema |
| 201 - Created | [`FirmwareSchema`](firmwareschema-metal3-io-v1alpha1.md#firmwareschema-metal3-io-v1alpha1) schema |
| 202 - Accepted | [`FirmwareSchema`](firmwareschema-metal3-io-v1alpha1.md#firmwareschema-metal3-io-v1alpha1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/metal3.io/v1alpha1/namespaces/{namespace}/firmwareschemas/{name}

| Parameter | Type     | Description                |
|-----------|----------|----------------------------|
| `name`    | `string` | name of the FirmwareSchema |

Global path parameters

HTTP method
`DELETE`

Description
delete a FirmwareSchema

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
read the specified FirmwareSchema

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`FirmwareSchema`](firmwareschema-metal3-io-v1alpha1.md#firmwareschema-metal3-io-v1alpha1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PATCH`

Description
partially update the specified FirmwareSchema

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`FirmwareSchema`](firmwareschema-metal3-io-v1alpha1.md#firmwareschema-metal3-io-v1alpha1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PUT`

Description
replace the specified FirmwareSchema

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`FirmwareSchema`](firmwareschema-metal3-io-v1alpha1.md#firmwareschema-metal3-io-v1alpha1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`FirmwareSchema`](firmwareschema-metal3-io-v1alpha1.md#firmwareschema-metal3-io-v1alpha1) schema |
| 201 - Created | [`FirmwareSchema`](firmwareschema-metal3-io-v1alpha1.md#firmwareschema-metal3-io-v1alpha1) schema |
| 401 - Unauthorized | Empty |

HTTP responses
