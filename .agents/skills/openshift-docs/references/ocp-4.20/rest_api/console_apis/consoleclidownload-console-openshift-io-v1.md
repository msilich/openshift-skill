<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Description
ConsoleCLIDownload is an extension for configuring openshift web console command line interface (CLI) downloads.

Compatibility level 2: Stable within a major release for a minimum of 9 months or 3 minor releases (whichever is longer).

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
| `spec` | `object` | ConsoleCLIDownloadSpec is the desired cli download configuration. |

## .spec

Description
ConsoleCLIDownloadSpec is the desired cli download configuration.

Type
`object`

Required
- `description`

- `displayName`

- `links`

| Property | Type | Description |
|----|----|----|
| `description` | `string` | description is the description of the CLI download (can include markdown). |
| `displayName` | `string` | displayName is the display name of the CLI download. |
| `links` | `array` | links is a list of objects that provide CLI download link details. |
| `links[]` | `object` |  |

## .spec.links

Description
links is a list of objects that provide CLI download link details.

Type
`array`

## .spec.links\[\]

Description

Type
`object`

Required
- `href`

| Property | Type | Description |
|----|----|----|
| `href` | `string` | href is the absolute secure URL for the link (must use https) |
| `text` | `string` | text is the display text for the link |

# API endpoints

The following API endpoints are available:

- `/apis/console.openshift.io/v1/consoleclidownloads`

  - `DELETE`: delete collection of ConsoleCLIDownload

  - `GET`: list objects of kind ConsoleCLIDownload

  - `POST`: create a ConsoleCLIDownload

- `/apis/console.openshift.io/v1/consoleclidownloads/{name}`

  - `DELETE`: delete a ConsoleCLIDownload

  - `GET`: read the specified ConsoleCLIDownload

  - `PATCH`: partially update the specified ConsoleCLIDownload

  - `PUT`: replace the specified ConsoleCLIDownload

- `/apis/console.openshift.io/v1/consoleclidownloads/{name}/status`

  - `GET`: read status of the specified ConsoleCLIDownload

  - `PATCH`: partially update status of the specified ConsoleCLIDownload

  - `PUT`: replace status of the specified ConsoleCLIDownload

## /apis/console.openshift.io/v1/consoleclidownloads

HTTP method
`DELETE`

Description
delete collection of ConsoleCLIDownload

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Status`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`GET`

Description
list objects of kind ConsoleCLIDownload

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ConsoleCLIDownloadList`](../objects/index.md#io-openshift-console-v1-ConsoleCLIDownloadList) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`POST`

Description
create a ConsoleCLIDownload

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`ConsoleCLIDownload`](consoleclidownload-console-openshift-io-v1.md#consoleclidownload-console-openshift-io-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ConsoleCLIDownload`](consoleclidownload-console-openshift-io-v1.md#consoleclidownload-console-openshift-io-v1) schema |
| 201 - Created | [`ConsoleCLIDownload`](consoleclidownload-console-openshift-io-v1.md#consoleclidownload-console-openshift-io-v1) schema |
| 202 - Accepted | [`ConsoleCLIDownload`](consoleclidownload-console-openshift-io-v1.md#consoleclidownload-console-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/console.openshift.io/v1/consoleclidownloads/{name}

| Parameter | Type     | Description                    |
|-----------|----------|--------------------------------|
| `name`    | `string` | name of the ConsoleCLIDownload |

Global path parameters

HTTP method
`DELETE`

Description
delete a ConsoleCLIDownload

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
read the specified ConsoleCLIDownload

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ConsoleCLIDownload`](consoleclidownload-console-openshift-io-v1.md#consoleclidownload-console-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PATCH`

Description
partially update the specified ConsoleCLIDownload

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ConsoleCLIDownload`](consoleclidownload-console-openshift-io-v1.md#consoleclidownload-console-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PUT`

Description
replace the specified ConsoleCLIDownload

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`ConsoleCLIDownload`](consoleclidownload-console-openshift-io-v1.md#consoleclidownload-console-openshift-io-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ConsoleCLIDownload`](consoleclidownload-console-openshift-io-v1.md#consoleclidownload-console-openshift-io-v1) schema |
| 201 - Created | [`ConsoleCLIDownload`](consoleclidownload-console-openshift-io-v1.md#consoleclidownload-console-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/console.openshift.io/v1/consoleclidownloads/{name}/status

| Parameter | Type     | Description                    |
|-----------|----------|--------------------------------|
| `name`    | `string` | name of the ConsoleCLIDownload |

Global path parameters

HTTP method
`GET`

Description
read status of the specified ConsoleCLIDownload

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ConsoleCLIDownload`](consoleclidownload-console-openshift-io-v1.md#consoleclidownload-console-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PATCH`

Description
partially update status of the specified ConsoleCLIDownload

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ConsoleCLIDownload`](consoleclidownload-console-openshift-io-v1.md#consoleclidownload-console-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PUT`

Description
replace status of the specified ConsoleCLIDownload

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`ConsoleCLIDownload`](consoleclidownload-console-openshift-io-v1.md#consoleclidownload-console-openshift-io-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ConsoleCLIDownload`](consoleclidownload-console-openshift-io-v1.md#consoleclidownload-console-openshift-io-v1) schema |
| 201 - Created | [`ConsoleCLIDownload`](consoleclidownload-console-openshift-io-v1.md#consoleclidownload-console-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses
