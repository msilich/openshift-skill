<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Description
ConsoleYAMLSample is an extension for customizing OpenShift web console YAML samples.

Compatibility level 2: Stable within a major release for a minimum of 9 months or 3 minor releases (whichever is longer).

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
| `spec` | `object` | ConsoleYAMLSampleSpec is the desired YAML sample configuration. Samples will appear with their descriptions in a samples sidebar when creating a resources in the web console. |

## .spec

Description
ConsoleYAMLSampleSpec is the desired YAML sample configuration. Samples will appear with their descriptions in a samples sidebar when creating a resources in the web console.

Type
`object`

Required
- `description`

- `targetResource`

- `title`

- `yaml`

| Property | Type | Description |
|----|----|----|
| `description` | `string` | description of the YAML sample. |
| `snippet` | `boolean` | snippet indicates that the YAML sample is not the full YAML resource definition, but a fragment that can be inserted into the existing YAML document at the user’s cursor. |
| `targetResource` | `object` | targetResource contains apiVersion and kind of the resource YAML sample is representating. |
| `title` | `string` | title of the YAML sample. |
| `yaml` | `string` | yaml is the YAML sample to display. |

## .spec.targetResource

Description
targetResource contains apiVersion and kind of the resource YAML sample is representating.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

# API endpoints

The following API endpoints are available:

- `/apis/console.openshift.io/v1/consoleyamlsamples`

  - `DELETE`: delete collection of ConsoleYAMLSample

  - `GET`: list objects of kind ConsoleYAMLSample

  - `POST`: create a ConsoleYAMLSample

- `/apis/console.openshift.io/v1/consoleyamlsamples/{name}`

  - `DELETE`: delete a ConsoleYAMLSample

  - `GET`: read the specified ConsoleYAMLSample

  - `PATCH`: partially update the specified ConsoleYAMLSample

  - `PUT`: replace the specified ConsoleYAMLSample

## /apis/console.openshift.io/v1/consoleyamlsamples

HTTP method
`DELETE`

Description
delete collection of ConsoleYAMLSample

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Status`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`GET`

Description
list objects of kind ConsoleYAMLSample

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ConsoleYAMLSampleList`](../objects/index.md#io-openshift-console-v1-ConsoleYAMLSampleList) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`POST`

Description
create a ConsoleYAMLSample

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`ConsoleYAMLSample`](consoleyamlsample-console-openshift-io-v1.md#consoleyamlsample-console-openshift-io-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ConsoleYAMLSample`](consoleyamlsample-console-openshift-io-v1.md#consoleyamlsample-console-openshift-io-v1) schema |
| 201 - Created | [`ConsoleYAMLSample`](consoleyamlsample-console-openshift-io-v1.md#consoleyamlsample-console-openshift-io-v1) schema |
| 202 - Accepted | [`ConsoleYAMLSample`](consoleyamlsample-console-openshift-io-v1.md#consoleyamlsample-console-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/console.openshift.io/v1/consoleyamlsamples/{name}

| Parameter | Type     | Description                   |
|-----------|----------|-------------------------------|
| `name`    | `string` | name of the ConsoleYAMLSample |

Global path parameters

HTTP method
`DELETE`

Description
delete a ConsoleYAMLSample

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
read the specified ConsoleYAMLSample

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ConsoleYAMLSample`](consoleyamlsample-console-openshift-io-v1.md#consoleyamlsample-console-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PATCH`

Description
partially update the specified ConsoleYAMLSample

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ConsoleYAMLSample`](consoleyamlsample-console-openshift-io-v1.md#consoleyamlsample-console-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PUT`

Description
replace the specified ConsoleYAMLSample

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`ConsoleYAMLSample`](consoleyamlsample-console-openshift-io-v1.md#consoleyamlsample-console-openshift-io-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ConsoleYAMLSample`](consoleyamlsample-console-openshift-io-v1.md#consoleyamlsample-console-openshift-io-v1) schema |
| 201 - Created | [`ConsoleYAMLSample`](consoleyamlsample-console-openshift-io-v1.md#consoleyamlsample-console-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses
