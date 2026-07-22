<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Description
Config contains the configuration and detailed condition status for the Samples Operator. Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).

Type
`object`

Required
- `metadata`

- `spec`

# Specification

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ObjectMeta`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) | Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |
| `spec` | `object` | ConfigSpec contains the desired configuration and state for the Samples Operator, controlling various behavior around the imagestreams and templates it creates/updates in the openshift namespace. |
| `status` | `object` | ConfigStatus contains the actual configuration in effect, as well as various details that describe the state of the Samples Operator. |

## .spec

Description
ConfigSpec contains the desired configuration and state for the Samples Operator, controlling various behavior around the imagestreams and templates it creates/updates in the openshift namespace.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `architectures` | `array (string)` | architectures determine which hardware architecture(s) to install, where x86_64, ppc64le, and s390x are the only supported choices currently. |
| `managementState` | `string` | managementState is top level on/off type of switch for all operators. When "Managed", this operator processes config and manipulates the samples accordingly. When "Unmanaged", this operator ignores any updates to the resources it watches. When "Removed", it reacts that same wasy as it does if the Config object is deleted, meaning any ImageStreams or Templates it manages (i.e. it honors the skipped lists) and the registry secret are deleted, along with the ConfigMap in the operator’s namespace that represents the last config used to manipulate the samples, |
| `samplesRegistry` | `string` | samplesRegistry allows for the specification of which registry is accessed by the ImageStreams for their image content. Defaults on the content in <https://github.com/openshift/library> that are pulled into this github repository, but based on our pulling only ocp content it typically defaults to registry.redhat.io. |
| `skippedImagestreams` | `array (string)` | skippedImagestreams specifies names of image streams that should NOT be created/updated. Admins can use this to allow them to delete content they don’t want. They will still have to manually delete the content but the operator will not recreate(or update) anything listed here. |
| `skippedTemplates` | `array (string)` | skippedTemplates specifies names of templates that should NOT be created/updated. Admins can use this to allow them to delete content they don’t want. They will still have to manually delete the content but the operator will not recreate(or update) anything listed here. |

## .status

Description
ConfigStatus contains the actual configuration in effect, as well as various details that describe the state of the Samples Operator.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `architectures` | `array (string)` | architectures determine which hardware architecture(s) to install, where x86_64 and ppc64le are the supported choices. |
| `conditions` | `array` | conditions represents the available maintenance status of the sample imagestreams and templates. |
| `conditions[]` | `object` | ConfigCondition captures various conditions of the Config as entries are processed. |
| `managementState` | `string` | managementState reflects the current operational status of the on/off switch for the operator. This operator compares the ManagementState as part of determining that we are turning the operator back on (i.e. "Managed") when it was previously "Unmanaged". |
| `samplesRegistry` | `string` | samplesRegistry allows for the specification of which registry is accessed by the ImageStreams for their image content. Defaults on the content in <https://github.com/openshift/library> that are pulled into this github repository, but based on our pulling only ocp content it typically defaults to registry.redhat.io. |
| `skippedImagestreams` | `array (string)` | skippedImagestreams specifies names of image streams that should NOT be created/updated. Admins can use this to allow them to delete content they don’t want. They will still have to manually delete the content but the operator will not recreate(or update) anything listed here. |
| `skippedTemplates` | `array (string)` | skippedTemplates specifies names of templates that should NOT be created/updated. Admins can use this to allow them to delete content they don’t want. They will still have to manually delete the content but the operator will not recreate(or update) anything listed here. |
| `version` | `string` | version is the value of the operator’s payload based version indicator when it was last successfully processed |

## .status.conditions

Description
conditions represents the available maintenance status of the sample imagestreams and templates.

Type
`array`

## .status.conditions\[\]

Description
ConfigCondition captures various conditions of the Config as entries are processed.

Type
`object`

Required
- `status`

- `type`

| Property | Type | Description |
|----|----|----|
| `lastTransitionTime` | `string` | lastTransitionTime is the last time the condition transitioned from one status to another. |
| `lastUpdateTime` | `string` | lastUpdateTime is the last time this condition was updated. |
| `message` | `string` | message is a human readable message indicating details about the transition. |
| `reason` | `string` | reason is what caused the condition’s last transition. |
| `status` | `string` | status of the condition, one of True, False, Unknown. |
| `type` | `string` | type of condition. |

# API endpoints

The following API endpoints are available:

- `/apis/samples.operator.openshift.io/v1/configs`

  - `DELETE`: delete collection of Config

  - `GET`: list objects of kind Config

  - `POST`: create a Config

- `/apis/samples.operator.openshift.io/v1/configs/{name}`

  - `DELETE`: delete a Config

  - `GET`: read the specified Config

  - `PATCH`: partially update the specified Config

  - `PUT`: replace the specified Config

- `/apis/samples.operator.openshift.io/v1/configs/{name}/status`

  - `GET`: read status of the specified Config

  - `PATCH`: partially update status of the specified Config

  - `PUT`: replace status of the specified Config

## /apis/samples.operator.openshift.io/v1/configs

HTTP method
`DELETE`

Description
delete collection of Config

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Status`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`GET`

Description
list objects of kind Config

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ConfigList`](../objects/index.md#io-openshift-operator-samples-v1-ConfigList) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`POST`

Description
create a Config

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`Config`](config-samples-operator-openshift-io-v1.md#config-samples-operator-openshift-io-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Config`](config-samples-operator-openshift-io-v1.md#config-samples-operator-openshift-io-v1) schema |
| 201 - Created | [`Config`](config-samples-operator-openshift-io-v1.md#config-samples-operator-openshift-io-v1) schema |
| 202 - Accepted | [`Config`](config-samples-operator-openshift-io-v1.md#config-samples-operator-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/samples.operator.openshift.io/v1/configs/{name}

| Parameter | Type     | Description        |
|-----------|----------|--------------------|
| `name`    | `string` | name of the Config |

Global path parameters

HTTP method
`DELETE`

Description
delete a Config

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
read the specified Config

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Config`](config-samples-operator-openshift-io-v1.md#config-samples-operator-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PATCH`

Description
partially update the specified Config

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Config`](config-samples-operator-openshift-io-v1.md#config-samples-operator-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PUT`

Description
replace the specified Config

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`Config`](config-samples-operator-openshift-io-v1.md#config-samples-operator-openshift-io-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Config`](config-samples-operator-openshift-io-v1.md#config-samples-operator-openshift-io-v1) schema |
| 201 - Created | [`Config`](config-samples-operator-openshift-io-v1.md#config-samples-operator-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/samples.operator.openshift.io/v1/configs/{name}/status

| Parameter | Type     | Description        |
|-----------|----------|--------------------|
| `name`    | `string` | name of the Config |

Global path parameters

HTTP method
`GET`

Description
read status of the specified Config

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Config`](config-samples-operator-openshift-io-v1.md#config-samples-operator-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PATCH`

Description
partially update status of the specified Config

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Config`](config-samples-operator-openshift-io-v1.md#config-samples-operator-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PUT`

Description
replace status of the specified Config

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`Config`](config-samples-operator-openshift-io-v1.md#config-samples-operator-openshift-io-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Config`](config-samples-operator-openshift-io-v1.md#config-samples-operator-openshift-io-v1) schema |
| 201 - Created | [`Config`](config-samples-operator-openshift-io-v1.md#config-samples-operator-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses
