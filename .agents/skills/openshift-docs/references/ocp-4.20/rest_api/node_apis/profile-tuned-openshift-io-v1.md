<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Description
Profile is a specification for a Profile resource.

Type
`object`

# Specification

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ObjectMeta`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) | Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |
| `spec` | `object` |  |
| `status` | `object` | ProfileStatus is the status for a Profile resource; the status is for internal use only and its fields may be changed/removed in the future. |

## .spec

Description

Type
`object`

Required
- `config`

| Property    | Type     | Description      |
|-------------|----------|------------------|
| `config`    | `object` |                  |
| `profile`   | `array`  | Tuned profiles.  |
| `profile[]` | `object` | A Tuned profile. |

## .spec.config

Description

Type
`object`

Required
- `tunedProfile`

| Property | Type | Description |
|----|----|----|
| `debug` | `boolean` | option to debug TuneD daemon execution |
| `providerName` | `string` | Name of the cloud provider as taken from the Node providerID: \<ProviderName\>://\<ProviderSpecificNodeID\> |
| `tunedConfig` | `object` | Global configuration for the TuneD daemon as defined in tuned-main.conf |
| `tunedProfile` | `string` | TuneD profile to apply |
| `verbosity` | `integer` | klog logging verbosity |

## .spec.config.tunedConfig

Description
Global configuration for the TuneD daemon as defined in tuned-main.conf

Type
`object`

| Property | Type | Description |
|----|----|----|
| `reapply_sysctl` | `boolean` | turn reapply_sysctl functionality on/off for the TuneD daemon: true/false |

## .spec.profile

Description
Tuned profiles.

Type
`array`

## .spec.profile\[\]

Description
A Tuned profile.

Type
`object`

Required
- `data`

- `name`

| Property | Type | Description |
|----|----|----|
| `data` | `string` | Specification of the Tuned profile to be consumed by the Tuned daemon. |
| `name` | `string` | Name of the Tuned profile to be used in the recommend section. |

## .status

Description
ProfileStatus is the status for a Profile resource; the status is for internal use only and its fields may be changed/removed in the future.

Type
`object`

Required
- `tunedProfile`

| Property | Type | Description |
|----|----|----|
| `conditions` | `array` | conditions represents the state of the per-node Profile application |
| `conditions[]` | `object` | StatusCondition represents a partial state of the per-node Profile application. |
| `observedGeneration` | `integer` | If set, this represents the .metadata.generation that the conditions were set based upon. |
| `tunedProfile` | `string` | the current profile in use by the Tuned daemon |

## .status.conditions

Description
conditions represents the state of the per-node Profile application

Type
`array`

## .status.conditions\[\]

Description
StatusCondition represents a partial state of the per-node Profile application.

Type
`object`

Required
- `lastTransitionTime`

- `status`

- `type`

| Property | Type | Description |
|----|----|----|
| `lastTransitionTime` | `string` | lastTransitionTime is the time of the last update to the current status property. |
| `message` | `string` | message provides additional information about the current condition. This is only to be consumed by humans. |
| `reason` | `string` | reason is the CamelCase reason for the condition’s current status. |
| `status` | `string` | status of the condition, one of True, False, Unknown. |
| `type` | `string` | type specifies the aspect reported by this condition. |

# API endpoints

The following API endpoints are available:

- `/apis/tuned.openshift.io/v1/profiles`

  - `GET`: list objects of kind Profile

- `/apis/tuned.openshift.io/v1/namespaces/{namespace}/profiles`

  - `DELETE`: delete collection of Profile

  - `GET`: list objects of kind Profile

  - `POST`: create a Profile

- `/apis/tuned.openshift.io/v1/namespaces/{namespace}/profiles/{name}`

  - `DELETE`: delete a Profile

  - `GET`: read the specified Profile

  - `PATCH`: partially update the specified Profile

  - `PUT`: replace the specified Profile

- `/apis/tuned.openshift.io/v1/namespaces/{namespace}/profiles/{name}/status`

  - `GET`: read status of the specified Profile

  - `PATCH`: partially update status of the specified Profile

  - `PUT`: replace status of the specified Profile

## /apis/tuned.openshift.io/v1/profiles

HTTP method
`GET`

Description
list objects of kind Profile

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ProfileList`](../objects/index.md#io-openshift-tuned-v1-ProfileList) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/tuned.openshift.io/v1/namespaces/{namespace}/profiles

HTTP method
`DELETE`

Description
delete collection of Profile

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Status`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`GET`

Description
list objects of kind Profile

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ProfileList`](../objects/index.md#io-openshift-tuned-v1-ProfileList) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`POST`

Description
create a Profile

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`Profile`](profile-tuned-openshift-io-v1.md#profile-tuned-openshift-io-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Profile`](profile-tuned-openshift-io-v1.md#profile-tuned-openshift-io-v1) schema |
| 201 - Created | [`Profile`](profile-tuned-openshift-io-v1.md#profile-tuned-openshift-io-v1) schema |
| 202 - Accepted | [`Profile`](profile-tuned-openshift-io-v1.md#profile-tuned-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/tuned.openshift.io/v1/namespaces/{namespace}/profiles/{name}

| Parameter | Type     | Description         |
|-----------|----------|---------------------|
| `name`    | `string` | name of the Profile |

Global path parameters

HTTP method
`DELETE`

Description
delete a Profile

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
read the specified Profile

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Profile`](profile-tuned-openshift-io-v1.md#profile-tuned-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PATCH`

Description
partially update the specified Profile

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Profile`](profile-tuned-openshift-io-v1.md#profile-tuned-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PUT`

Description
replace the specified Profile

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`Profile`](profile-tuned-openshift-io-v1.md#profile-tuned-openshift-io-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Profile`](profile-tuned-openshift-io-v1.md#profile-tuned-openshift-io-v1) schema |
| 201 - Created | [`Profile`](profile-tuned-openshift-io-v1.md#profile-tuned-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/tuned.openshift.io/v1/namespaces/{namespace}/profiles/{name}/status

| Parameter | Type     | Description         |
|-----------|----------|---------------------|
| `name`    | `string` | name of the Profile |

Global path parameters

HTTP method
`GET`

Description
read status of the specified Profile

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Profile`](profile-tuned-openshift-io-v1.md#profile-tuned-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PATCH`

Description
partially update status of the specified Profile

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Profile`](profile-tuned-openshift-io-v1.md#profile-tuned-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PUT`

Description
replace status of the specified Profile

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`Profile`](profile-tuned-openshift-io-v1.md#profile-tuned-openshift-io-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Profile`](profile-tuned-openshift-io-v1.md#profile-tuned-openshift-io-v1) schema |
| 201 - Created | [`Profile`](profile-tuned-openshift-io-v1.md#profile-tuned-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses
