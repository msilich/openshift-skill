<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Description
ConsoleNotification is the extension for configuring openshift web console notifications.

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
| `spec` | `object` | ConsoleNotificationSpec is the desired console notification configuration. |

## .spec

Description
ConsoleNotificationSpec is the desired console notification configuration.

Type
`object`

Required
- `text`

| Property | Type | Description |
|----|----|----|
| `backgroundColor` | `string` | backgroundColor is the color of the background for the notification as CSS data type color. |
| `color` | `string` | color is the color of the text for the notification as CSS data type color. |
| `link` | `object` | link is an object that holds notification link details. |
| `location` | `string` | location is the location of the notification in the console. Valid values are: "BannerTop", "BannerBottom", "BannerTopBottom". |
| `text` | `string` | text is the visible text of the notification. |

## .spec.link

Description
link is an object that holds notification link details.

Type
`object`

Required
- `href`

- `text`

| Property | Type | Description |
|----|----|----|
| `href` | `string` | href is the absolute secure URL for the link (must use https) |
| `text` | `string` | text is the display text for the link |

# API endpoints

The following API endpoints are available:

- `/apis/console.openshift.io/v1/consolenotifications`

  - `DELETE`: delete collection of ConsoleNotification

  - `GET`: list objects of kind ConsoleNotification

  - `POST`: create a ConsoleNotification

- `/apis/console.openshift.io/v1/consolenotifications/{name}`

  - `DELETE`: delete a ConsoleNotification

  - `GET`: read the specified ConsoleNotification

  - `PATCH`: partially update the specified ConsoleNotification

  - `PUT`: replace the specified ConsoleNotification

- `/apis/console.openshift.io/v1/consolenotifications/{name}/status`

  - `GET`: read status of the specified ConsoleNotification

  - `PATCH`: partially update status of the specified ConsoleNotification

  - `PUT`: replace status of the specified ConsoleNotification

## /apis/console.openshift.io/v1/consolenotifications

HTTP method
`DELETE`

Description
delete collection of ConsoleNotification

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Status`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`GET`

Description
list objects of kind ConsoleNotification

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ConsoleNotificationList`](../objects/index.md#io-openshift-console-v1-ConsoleNotificationList) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`POST`

Description
create a ConsoleNotification

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`ConsoleNotification`](consolenotification-console-openshift-io-v1.md#consolenotification-console-openshift-io-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ConsoleNotification`](consolenotification-console-openshift-io-v1.md#consolenotification-console-openshift-io-v1) schema |
| 201 - Created | [`ConsoleNotification`](consolenotification-console-openshift-io-v1.md#consolenotification-console-openshift-io-v1) schema |
| 202 - Accepted | [`ConsoleNotification`](consolenotification-console-openshift-io-v1.md#consolenotification-console-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/console.openshift.io/v1/consolenotifications/{name}

| Parameter | Type     | Description                     |
|-----------|----------|---------------------------------|
| `name`    | `string` | name of the ConsoleNotification |

Global path parameters

HTTP method
`DELETE`

Description
delete a ConsoleNotification

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
read the specified ConsoleNotification

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ConsoleNotification`](consolenotification-console-openshift-io-v1.md#consolenotification-console-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PATCH`

Description
partially update the specified ConsoleNotification

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ConsoleNotification`](consolenotification-console-openshift-io-v1.md#consolenotification-console-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PUT`

Description
replace the specified ConsoleNotification

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`ConsoleNotification`](consolenotification-console-openshift-io-v1.md#consolenotification-console-openshift-io-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ConsoleNotification`](consolenotification-console-openshift-io-v1.md#consolenotification-console-openshift-io-v1) schema |
| 201 - Created | [`ConsoleNotification`](consolenotification-console-openshift-io-v1.md#consolenotification-console-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/console.openshift.io/v1/consolenotifications/{name}/status

| Parameter | Type     | Description                     |
|-----------|----------|---------------------------------|
| `name`    | `string` | name of the ConsoleNotification |

Global path parameters

HTTP method
`GET`

Description
read status of the specified ConsoleNotification

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ConsoleNotification`](consolenotification-console-openshift-io-v1.md#consolenotification-console-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PATCH`

Description
partially update status of the specified ConsoleNotification

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ConsoleNotification`](consolenotification-console-openshift-io-v1.md#consolenotification-console-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PUT`

Description
replace status of the specified ConsoleNotification

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`ConsoleNotification`](consolenotification-console-openshift-io-v1.md#consolenotification-console-openshift-io-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`ConsoleNotification`](consolenotification-console-openshift-io-v1.md#consolenotification-console-openshift-io-v1) schema |
| 201 - Created | [`ConsoleNotification`](consolenotification-console-openshift-io-v1.md#consolenotification-console-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses
