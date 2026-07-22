<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Description
HostFirmwareSettings is the Schema for the hostfirmwaresettings API.

Type
`object`

# Specification

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ObjectMeta`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) | Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |
| `spec` | `object` | HostFirmwareSettingsSpec defines the desired state of HostFirmwareSettings. |
| `status` | `object` | HostFirmwareSettingsStatus defines the observed state of HostFirmwareSettings. |

## .spec

Description
HostFirmwareSettingsSpec defines the desired state of HostFirmwareSettings.

Type
`object`

Required
- `settings`

| Property | Type | Description |
|----|----|----|
| `settings` | `integer-or-string` | Settings are the desired firmware settings stored as name/value pairs. |

## .status

Description
HostFirmwareSettingsStatus defines the observed state of HostFirmwareSettings.

Type
`object`

Required
- `settings`

| Property | Type | Description |
|----|----|----|
| `conditions` | `array` | Track whether settings stored in the spec are valid based on the schema |
| `conditions[]` | `object` | Condition contains details for one aspect of the current state of this API Resource. |
| `lastUpdated` | `string` | Time that the status was last updated |
| `schema` | `object` | FirmwareSchema is a reference to the Schema used to describe each FirmwareSetting. By default, this will be a Schema in the same Namespace as the settings but it can be overwritten in the Spec |
| `settings` | `object (string)` | Settings are the firmware settings stored as name/value pairs |

## .status.conditions

Description
Track whether settings stored in the spec are valid based on the schema

Type
`array`

## .status.conditions\[\]

Description
Condition contains details for one aspect of the current state of this API Resource.

Type
`object`

Required
- `lastTransitionTime`

- `message`

- `reason`

- `status`

- `type`

| Property | Type | Description |
|----|----|----|
| `lastTransitionTime` | `string` | lastTransitionTime is the last time the condition transitioned from one status to another. This should be when the underlying condition changed. If that is not known, then using the time when the API field changed is acceptable. |
| `message` | `string` | message is a human readable message indicating details about the transition. This may be an empty string. |
| `observedGeneration` | `integer` | observedGeneration represents the .metadata.generation that the condition was set based upon. For instance, if .metadata.generation is currently 12, but the .status.conditions\[x\].observedGeneration is 9, the condition is out of date with respect to the current state of the instance. |
| `reason` | `string` | reason contains a programmatic identifier indicating the reason for the condition’s last transition. Producers of specific condition types may define expected values and meanings for this field, and whether the values are considered a guaranteed API. The value should be a CamelCase string. This field may not be empty. |
| `status` | `string` | status of the condition, one of True, False, Unknown. |
| `type` | `string` | type of condition in CamelCase or in foo.example.com/CamelCase. |

## .status.schema

Description
FirmwareSchema is a reference to the Schema used to describe each FirmwareSetting. By default, this will be a Schema in the same Namespace as the settings but it can be overwritten in the Spec

Type
`object`

Required
- `name`

- `namespace`

| Property | Type | Description |
|----|----|----|
| `name` | `string` | `name` is the reference to the schema. |
| `namespace` | `string` | `namespace` is the namespace of the where the schema is stored. |

# API endpoints

The following API endpoints are available:

- `/apis/metal3.io/v1alpha1/hostfirmwaresettings`

  - `GET`: list objects of kind HostFirmwareSettings

- `/apis/metal3.io/v1alpha1/namespaces/{namespace}/hostfirmwaresettings`

  - `DELETE`: delete collection of HostFirmwareSettings

  - `GET`: list objects of kind HostFirmwareSettings

  - `POST`: create HostFirmwareSettings

- `/apis/metal3.io/v1alpha1/namespaces/{namespace}/hostfirmwaresettings/{name}`

  - `DELETE`: delete HostFirmwareSettings

  - `GET`: read the specified HostFirmwareSettings

  - `PATCH`: partially update the specified HostFirmwareSettings

  - `PUT`: replace the specified HostFirmwareSettings

- `/apis/metal3.io/v1alpha1/namespaces/{namespace}/hostfirmwaresettings/{name}/status`

  - `GET`: read status of the specified HostFirmwareSettings

  - `PATCH`: partially update status of the specified HostFirmwareSettings

  - `PUT`: replace status of the specified HostFirmwareSettings

## /apis/metal3.io/v1alpha1/hostfirmwaresettings

HTTP method
`GET`

Description
list objects of kind HostFirmwareSettings

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`HostFirmwareSettingsList`](../objects/index.md#io-metal3-v1alpha1-HostFirmwareSettingsList) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/metal3.io/v1alpha1/namespaces/{namespace}/hostfirmwaresettings

HTTP method
`DELETE`

Description
delete collection of HostFirmwareSettings

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Status`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`GET`

Description
list objects of kind HostFirmwareSettings

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`HostFirmwareSettingsList`](../objects/index.md#io-metal3-v1alpha1-HostFirmwareSettingsList) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`POST`

Description
create HostFirmwareSettings

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`HostFirmwareSettings`](hostfirmwaresettings-metal3-io-v1alpha1.md#hostfirmwaresettings-metal3-io-v1alpha1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`HostFirmwareSettings`](hostfirmwaresettings-metal3-io-v1alpha1.md#hostfirmwaresettings-metal3-io-v1alpha1) schema |
| 201 - Created | [`HostFirmwareSettings`](hostfirmwaresettings-metal3-io-v1alpha1.md#hostfirmwaresettings-metal3-io-v1alpha1) schema |
| 202 - Accepted | [`HostFirmwareSettings`](hostfirmwaresettings-metal3-io-v1alpha1.md#hostfirmwaresettings-metal3-io-v1alpha1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/metal3.io/v1alpha1/namespaces/{namespace}/hostfirmwaresettings/{name}

| Parameter | Type     | Description                      |
|-----------|----------|----------------------------------|
| `name`    | `string` | name of the HostFirmwareSettings |

Global path parameters

HTTP method
`DELETE`

Description
delete HostFirmwareSettings

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
read the specified HostFirmwareSettings

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`HostFirmwareSettings`](hostfirmwaresettings-metal3-io-v1alpha1.md#hostfirmwaresettings-metal3-io-v1alpha1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PATCH`

Description
partially update the specified HostFirmwareSettings

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`HostFirmwareSettings`](hostfirmwaresettings-metal3-io-v1alpha1.md#hostfirmwaresettings-metal3-io-v1alpha1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PUT`

Description
replace the specified HostFirmwareSettings

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`HostFirmwareSettings`](hostfirmwaresettings-metal3-io-v1alpha1.md#hostfirmwaresettings-metal3-io-v1alpha1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`HostFirmwareSettings`](hostfirmwaresettings-metal3-io-v1alpha1.md#hostfirmwaresettings-metal3-io-v1alpha1) schema |
| 201 - Created | [`HostFirmwareSettings`](hostfirmwaresettings-metal3-io-v1alpha1.md#hostfirmwaresettings-metal3-io-v1alpha1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/metal3.io/v1alpha1/namespaces/{namespace}/hostfirmwaresettings/{name}/status

| Parameter | Type     | Description                      |
|-----------|----------|----------------------------------|
| `name`    | `string` | name of the HostFirmwareSettings |

Global path parameters

HTTP method
`GET`

Description
read status of the specified HostFirmwareSettings

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`HostFirmwareSettings`](hostfirmwaresettings-metal3-io-v1alpha1.md#hostfirmwaresettings-metal3-io-v1alpha1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PATCH`

Description
partially update status of the specified HostFirmwareSettings

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`HostFirmwareSettings`](hostfirmwaresettings-metal3-io-v1alpha1.md#hostfirmwaresettings-metal3-io-v1alpha1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PUT`

Description
replace status of the specified HostFirmwareSettings

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`HostFirmwareSettings`](hostfirmwaresettings-metal3-io-v1alpha1.md#hostfirmwaresettings-metal3-io-v1alpha1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`HostFirmwareSettings`](hostfirmwaresettings-metal3-io-v1alpha1.md#hostfirmwaresettings-metal3-io-v1alpha1) schema |
| 201 - Created | [`HostFirmwareSettings`](hostfirmwaresettings-metal3-io-v1alpha1.md#hostfirmwaresettings-metal3-io-v1alpha1) schema |
| 401 - Unauthorized | Empty |

HTTP responses
