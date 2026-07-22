<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Description
KubeletConfig describes a customized Kubelet configuration.

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
| `metadata` | [`ObjectMeta`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) | Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |
| `spec` | `object` | spec contains the desired kubelet configuration. |
| `status` | `object` | status contains observed information about the kubelet configuration. |

## .spec

Description
spec contains the desired kubelet configuration.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `autoSizingReserved` | `boolean` |  |
| `kubeletConfig` | \`\` | kubeletConfig fields are defined in kubernetes upstream. Please refer to the types defined in the version/commit used by OpenShift of the upstream kubernetes. It’s important to note that, since the fields of the kubelet configuration are directly fetched from upstream the validation of those values is handled directly by the kubelet. Please refer to the upstream version of the relevant kubernetes for the valid values of these fields. Invalid values of the kubelet configuration fields may render cluster nodes unusable. |
| `logLevel` | `integer` |  |
| `machineConfigPoolSelector` | `object` | machineConfigPoolSelector selects which pools the KubeletConfig shoud apply to. A nil selector will result in no pools being selected. |
| `tlsSecurityProfile` | `object` | If unset, the default is based on the apiservers.config.openshift.io/cluster resource. Note that only Old and Intermediate profiles are currently supported, and the maximum available minTLSVersion is VersionTLS12. |

## .spec.machineConfigPoolSelector

Description
machineConfigPoolSelector selects which pools the KubeletConfig shoud apply to. A nil selector will result in no pools being selected.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `matchExpressions` | `array` | matchExpressions is a list of label selector requirements. The requirements are ANDed. |
| `matchExpressions[]` | `object` | A label selector requirement is a selector that contains values, a key, and an operator that relates the key and values. |
| `matchLabels` | `object (string)` | matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed. |

## .spec.machineConfigPoolSelector.matchExpressions

Description
matchExpressions is a list of label selector requirements. The requirements are ANDed.

Type
`array`

## .spec.machineConfigPoolSelector.matchExpressions\[\]

Description
A label selector requirement is a selector that contains values, a key, and an operator that relates the key and values.

Type
`object`

Required
- `key`

- `operator`

| Property | Type | Description |
|----|----|----|
| `key` | `string` | key is the label key that the selector applies to. |
| `operator` | `string` | operator represents a key’s relationship to a set of values. Valid operators are In, NotIn, Exists and DoesNotExist. |
| `values` | `array (string)` | values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch. |

## .spec.tlsSecurityProfile

Description
If unset, the default is based on the apiservers.config.openshift.io/cluster resource. Note that only Old and Intermediate profiles are currently supported, and the maximum available minTLSVersion is VersionTLS12.

Type
`object`

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Property</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>custom</code></p></td>
<td style="text-align: left;"><p>``</p></td>
<td style="text-align: left;"><p>custom is a user-defined TLS security profile. Be extremely careful using a custom profile as invalid configurations can be catastrophic. An example custom profile looks like this:</p>
<p>ciphers:</p>
<p>- ECDHE-ECDSA-CHACHA20-POLY1305</p>
<p>- ECDHE-RSA-CHACHA20-POLY1305</p>
<p>- ECDHE-RSA-AES128-GCM-SHA256</p>
<p>- ECDHE-ECDSA-AES128-GCM-SHA256</p>
<p>minTLSVersion: VersionTLS11</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>intermediate</code></p></td>
<td style="text-align: left;"><p>``</p></td>
<td style="text-align: left;"><p>intermediate is a TLS security profile based on:</p>
<p><a href="https://wiki.mozilla.org/Security/Server_Side_TLS#Intermediate_compatibility_.28recommended.29">https://wiki.mozilla.org/Security/Server_Side_TLS#Intermediate_compatibility_.28recommended.29</a></p>
<p>and looks like this (yaml):</p>
<p>ciphers:</p>
<p>- TLS_AES_128_GCM_SHA256</p>
<p>- TLS_AES_256_GCM_SHA384</p>
<p>- TLS_CHACHA20_POLY1305_SHA256</p>
<p>- ECDHE-ECDSA-AES128-GCM-SHA256</p>
<p>- ECDHE-RSA-AES128-GCM-SHA256</p>
<p>- ECDHE-ECDSA-AES256-GCM-SHA384</p>
<p>- ECDHE-RSA-AES256-GCM-SHA384</p>
<p>- ECDHE-ECDSA-CHACHA20-POLY1305</p>
<p>- ECDHE-RSA-CHACHA20-POLY1305</p>
<p>- DHE-RSA-AES128-GCM-SHA256</p>
<p>- DHE-RSA-AES256-GCM-SHA384</p>
<p>minTLSVersion: VersionTLS12</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>modern</code></p></td>
<td style="text-align: left;"><p>``</p></td>
<td style="text-align: left;"><p>modern is a TLS security profile based on:</p>
<p><a href="https://wiki.mozilla.org/Security/Server_Side_TLS#Modern_compatibility">https://wiki.mozilla.org/Security/Server_Side_TLS#Modern_compatibility</a></p>
<p>and looks like this (yaml):</p>
<p>ciphers:</p>
<p>- TLS_AES_128_GCM_SHA256</p>
<p>- TLS_AES_256_GCM_SHA384</p>
<p>- TLS_CHACHA20_POLY1305_SHA256</p>
<p>minTLSVersion: VersionTLS13</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>old</code></p></td>
<td style="text-align: left;"><p>``</p></td>
<td style="text-align: left;"><p>old is a TLS security profile based on:</p>
<p><a href="https://wiki.mozilla.org/Security/Server_Side_TLS#Old_backward_compatibility">https://wiki.mozilla.org/Security/Server_Side_TLS#Old_backward_compatibility</a></p>
<p>and looks like this (yaml):</p>
<p>ciphers:</p>
<p>- TLS_AES_128_GCM_SHA256</p>
<p>- TLS_AES_256_GCM_SHA384</p>
<p>- TLS_CHACHA20_POLY1305_SHA256</p>
<p>- ECDHE-ECDSA-AES128-GCM-SHA256</p>
<p>- ECDHE-RSA-AES128-GCM-SHA256</p>
<p>- ECDHE-ECDSA-AES256-GCM-SHA384</p>
<p>- ECDHE-RSA-AES256-GCM-SHA384</p>
<p>- ECDHE-ECDSA-CHACHA20-POLY1305</p>
<p>- ECDHE-RSA-CHACHA20-POLY1305</p>
<p>- DHE-RSA-AES128-GCM-SHA256</p>
<p>- DHE-RSA-AES256-GCM-SHA384</p>
<p>- DHE-RSA-CHACHA20-POLY1305</p>
<p>- ECDHE-ECDSA-AES128-SHA256</p>
<p>- ECDHE-RSA-AES128-SHA256</p>
<p>- ECDHE-ECDSA-AES128-SHA</p>
<p>- ECDHE-RSA-AES128-SHA</p>
<p>- ECDHE-ECDSA-AES256-SHA384</p>
<p>- ECDHE-RSA-AES256-SHA384</p>
<p>- ECDHE-ECDSA-AES256-SHA</p>
<p>- ECDHE-RSA-AES256-SHA</p>
<p>- DHE-RSA-AES128-SHA256</p>
<p>- DHE-RSA-AES256-SHA256</p>
<p>- AES128-GCM-SHA256</p>
<p>- AES256-GCM-SHA384</p>
<p>- AES128-SHA256</p>
<p>- AES256-SHA256</p>
<p>- AES128-SHA</p>
<p>- AES256-SHA</p>
<p>- DES-CBC3-SHA</p>
<p>minTLSVersion: VersionTLS10</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>type</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>type is one of Old, Intermediate, Modern or Custom. Custom provides the ability to specify individual TLS security profile parameters. Old, Intermediate and Modern are TLS security profiles based on:</p>
<p><a href="https://wiki.mozilla.org/Security/Server_Side_TLS#Recommended_configurations">https://wiki.mozilla.org/Security/Server_Side_TLS#Recommended_configurations</a></p>
<p>The profiles are intent based, so they may change over time as new ciphers are developed and existing ciphers are found to be insecure. Depending on precisely which ciphers are available to a process, the list may be reduced.</p>
<p>Note that the Modern profile is currently not supported because it is not yet well adopted by common software libraries.</p></td>
</tr>
</tbody>
</table>

## .status

Description
status contains observed information about the kubelet configuration.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `conditions` | `array` | conditions represents the latest available observations of current state. |
| `conditions[]` | `object` | KubeletConfigCondition defines the state of the KubeletConfig |
| `observedGeneration` | `integer` | observedGeneration represents the generation observed by the controller. |

## .status.conditions

Description
conditions represents the latest available observations of current state.

Type
`array`

## .status.conditions\[\]

Description
KubeletConfigCondition defines the state of the KubeletConfig

Type
`object`

| Property | Type | Description |
|----|----|----|
| `lastTransitionTime` | \`\` | lastTransitionTime is the time of the last update to the current status object. |
| `message` | `string` | message provides additional information about the current condition. This is only to be consumed by humans. |
| `reason` | `string` | reason is the reason for the condition’s last transition. Reasons are PascalCase |
| `status` | `string` | status of the condition, one of True, False, Unknown. |
| `type` | `string` | type specifies the state of the operator’s reconciliation functionality. |

# API endpoints

The following API endpoints are available:

- `/apis/machineconfiguration.openshift.io/v1/kubeletconfigs`

  - `DELETE`: delete collection of KubeletConfig

  - `GET`: list objects of kind KubeletConfig

  - `POST`: create a KubeletConfig

- `/apis/machineconfiguration.openshift.io/v1/kubeletconfigs/{name}`

  - `DELETE`: delete a KubeletConfig

  - `GET`: read the specified KubeletConfig

  - `PATCH`: partially update the specified KubeletConfig

  - `PUT`: replace the specified KubeletConfig

- `/apis/machineconfiguration.openshift.io/v1/kubeletconfigs/{name}/status`

  - `GET`: read status of the specified KubeletConfig

  - `PATCH`: partially update status of the specified KubeletConfig

  - `PUT`: replace status of the specified KubeletConfig

## /apis/machineconfiguration.openshift.io/v1/kubeletconfigs

HTTP method
`DELETE`

Description
delete collection of KubeletConfig

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Status`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`GET`

Description
list objects of kind KubeletConfig

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`KubeletConfigList`](../objects/index.md#io-openshift-machineconfiguration-v1-KubeletConfigList) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`POST`

Description
create a KubeletConfig

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`KubeletConfig`](kubeletconfig-machineconfiguration-openshift-io-v1.md#kubeletconfig-machineconfiguration-openshift-io-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`KubeletConfig`](kubeletconfig-machineconfiguration-openshift-io-v1.md#kubeletconfig-machineconfiguration-openshift-io-v1) schema |
| 201 - Created | [`KubeletConfig`](kubeletconfig-machineconfiguration-openshift-io-v1.md#kubeletconfig-machineconfiguration-openshift-io-v1) schema |
| 202 - Accepted | [`KubeletConfig`](kubeletconfig-machineconfiguration-openshift-io-v1.md#kubeletconfig-machineconfiguration-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/machineconfiguration.openshift.io/v1/kubeletconfigs/{name}

| Parameter | Type     | Description               |
|-----------|----------|---------------------------|
| `name`    | `string` | name of the KubeletConfig |

Global path parameters

HTTP method
`DELETE`

Description
delete a KubeletConfig

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
read the specified KubeletConfig

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`KubeletConfig`](kubeletconfig-machineconfiguration-openshift-io-v1.md#kubeletconfig-machineconfiguration-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PATCH`

Description
partially update the specified KubeletConfig

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`KubeletConfig`](kubeletconfig-machineconfiguration-openshift-io-v1.md#kubeletconfig-machineconfiguration-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PUT`

Description
replace the specified KubeletConfig

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`KubeletConfig`](kubeletconfig-machineconfiguration-openshift-io-v1.md#kubeletconfig-machineconfiguration-openshift-io-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`KubeletConfig`](kubeletconfig-machineconfiguration-openshift-io-v1.md#kubeletconfig-machineconfiguration-openshift-io-v1) schema |
| 201 - Created | [`KubeletConfig`](kubeletconfig-machineconfiguration-openshift-io-v1.md#kubeletconfig-machineconfiguration-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/machineconfiguration.openshift.io/v1/kubeletconfigs/{name}/status

| Parameter | Type     | Description               |
|-----------|----------|---------------------------|
| `name`    | `string` | name of the KubeletConfig |

Global path parameters

HTTP method
`GET`

Description
read status of the specified KubeletConfig

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`KubeletConfig`](kubeletconfig-machineconfiguration-openshift-io-v1.md#kubeletconfig-machineconfiguration-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PATCH`

Description
partially update status of the specified KubeletConfig

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`KubeletConfig`](kubeletconfig-machineconfiguration-openshift-io-v1.md#kubeletconfig-machineconfiguration-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PUT`

Description
replace status of the specified KubeletConfig

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`KubeletConfig`](kubeletconfig-machineconfiguration-openshift-io-v1.md#kubeletconfig-machineconfiguration-openshift-io-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`KubeletConfig`](kubeletconfig-machineconfiguration-openshift-io-v1.md#kubeletconfig-machineconfiguration-openshift-io-v1) schema |
| 201 - Created | [`KubeletConfig`](kubeletconfig-machineconfiguration-openshift-io-v1.md#kubeletconfig-machineconfiguration-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses
