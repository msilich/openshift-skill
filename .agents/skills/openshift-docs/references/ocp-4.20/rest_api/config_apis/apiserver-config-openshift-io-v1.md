<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Description
APIServer holds configuration (like serving certificates, client CA and CORS domains) shared by all API servers in the system, among them especially kube-apiserver and openshift-apiserver. The canonical name of an instance is 'cluster'.

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
| `spec` | `object` | spec holds user settable values for configuration |
| `status` | `object` | status holds observed values from the cluster. They may not be overridden. |

## .spec

Description
spec holds user settable values for configuration

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
<td style="text-align: left;"><p><code>additionalCORSAllowedOrigins</code></p></td>
<td style="text-align: left;"><p><code>array (string)</code></p></td>
<td style="text-align: left;"><p>additionalCORSAllowedOrigins lists additional, user-defined regular expressions describing hosts for which the API server allows access using the CORS headers. This may be needed to access the API and the integrated OAuth server from JavaScript applications. The values are regular expressions that correspond to the Golang regular expression language.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>audit</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>audit specifies the settings for audit configuration to be applied to all OpenShift-provided API servers in the cluster.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>clientCA</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>clientCA references a ConfigMap containing a certificate bundle for the signers that will be recognized for incoming client certificates in addition to the operator managed signers. If this is empty, then only operator managed signers are valid. You usually only have to set this if you have your own PKI you wish to honor client certificates from. The ConfigMap must exist in the openshift-config namespace and contain the following required fields: - ConfigMap.Data["ca-bundle.crt"] - CA bundle.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>encryption</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>encryption allows the configuration of encryption of resources at the datastore layer.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>servingCerts</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>servingCert is the TLS cert info for serving secure traffic. If not specified, operator managed certificates will be used for serving secure traffic.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>tlsSecurityProfile</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>tlsSecurityProfile specifies settings for TLS connections for externally exposed servers.</p>
<p>If unset, a default (which may change between releases) is chosen. Note that only Old, Intermediate and Custom profiles are currently supported, and the maximum available minTLSVersion is VersionTLS12.</p></td>
</tr>
</tbody>
</table>

## .spec.audit

Description
audit specifies the settings for audit configuration to be applied to all OpenShift-provided API servers in the cluster.

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
<td style="text-align: left;"><p><code>customRules</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>customRules specify profiles per group. These profile take precedence over the top-level profile field if they apply. They are evaluation from top to bottom and the first one that matches, applies.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>customRules[]</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>AuditCustomRule describes a custom rule for an audit profile that takes precedence over the top-level profile.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>profile</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>profile specifies the name of the desired top-level audit profile to be applied to all requests sent to any of the OpenShift-provided API servers in the cluster (kube-apiserver, openshift-apiserver and oauth-apiserver), with the exception of those requests that match one or more of the customRules.</p>
<p>The following profiles are provided: - Default: default policy which means MetaData level logging with the exception of events (not logged at all), oauthaccesstokens and oauthauthorizetokens (both logged at RequestBody level). - WriteRequestBodies: like 'Default', but logs request and response HTTP payloads for write requests (create, update, patch). - AllRequestBodies: like 'WriteRequestBodies', but also logs request and response HTTP payloads for read requests (get, list). - None: no requests are logged at all, not even oauthaccesstokens and oauthauthorizetokens.</p>
<p>Warning: It is not recommended to disable audit logging by using the <code>None</code> profile unless you are fully aware of the risks of not logging data that can be beneficial when troubleshooting issues. If you disable audit logging and a support situation arises, you might need to enable audit logging and reproduce the issue in order to troubleshoot properly.</p>
<p>If unset, the 'Default' profile is used as the default.</p></td>
</tr>
</tbody>
</table>

## .spec.audit.customRules

Description
customRules specify profiles per group. These profile take precedence over the top-level profile field if they apply. They are evaluation from top to bottom and the first one that matches, applies.

Type
`array`

## .spec.audit.customRules\[\]

Description
AuditCustomRule describes a custom rule for an audit profile that takes precedence over the top-level profile.

Type
`object`

Required
- `group`

- `profile`

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
<td style="text-align: left;"><p><code>group</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>group is a name of group a request user must be member of in order to this profile to apply.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>profile</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>profile specifies the name of the desired audit policy configuration to be deployed to all OpenShift-provided API servers in the cluster.</p>
<p>The following profiles are provided: - Default: the existing default policy. - WriteRequestBodies: like 'Default', but logs request and response HTTP payloads for write requests (create, update, patch). - AllRequestBodies: like 'WriteRequestBodies', but also logs request and response HTTP payloads for read requests (get, list). - None: no requests are logged at all, not even oauthaccesstokens and oauthauthorizetokens.</p>
<p>If unset, the 'Default' profile is used as the default.</p></td>
</tr>
</tbody>
</table>

## .spec.clientCA

Description
clientCA references a ConfigMap containing a certificate bundle for the signers that will be recognized for incoming client certificates in addition to the operator managed signers. If this is empty, then only operator managed signers are valid. You usually only have to set this if you have your own PKI you wish to honor client certificates from. The ConfigMap must exist in the openshift-config namespace and contain the following required fields: - ConfigMap.Data\["ca-bundle.crt"\] - CA bundle.

Type
`object`

Required
- `name`

| Property | Type     | Description                                            |
|----------|----------|--------------------------------------------------------|
| `name`   | `string` | name is the metadata.name of the referenced config map |

## .spec.encryption

Description
encryption allows the configuration of encryption of resources at the datastore layer.

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
<td style="text-align: left;"><p><code>type</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>type defines what encryption type should be used to encrypt resources at the datastore layer. When this field is unset (i.e. when it is set to the empty string), identity is implied. The behavior of unset can and will change over time. Even if encryption is enabled by default, the meaning of unset may change to a different encryption type based on changes in best practices.</p>
<p>When encryption is enabled, all sensitive resources shipped with the platform are encrypted. This list of sensitive resources can and will change over time. The current authoritative list is:</p>
<p>1. secrets 2. configmaps 3. routes.route.openshift.io 4. oauthaccesstokens.oauth.openshift.io 5. oauthauthorizetokens.oauth.openshift.io</p></td>
</tr>
</tbody>
</table>

## .spec.servingCerts

Description
servingCert is the TLS cert info for serving secure traffic. If not specified, operator managed certificates will be used for serving secure traffic.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `namedCertificates` | `array` | namedCertificates references secrets containing the TLS cert info for serving secure traffic to specific hostnames. If no named certificates are provided, or no named certificates match the server name as understood by a client, the defaultServingCertificate will be used. |
| `namedCertificates[]` | `object` | APIServerNamedServingCert maps a server DNS name, as understood by a client, to a certificate. |

## .spec.servingCerts.namedCertificates

Description
namedCertificates references secrets containing the TLS cert info for serving secure traffic to specific hostnames. If no named certificates are provided, or no named certificates match the server name as understood by a client, the defaultServingCertificate will be used.

Type
`array`

## .spec.servingCerts.namedCertificates\[\]

Description
APIServerNamedServingCert maps a server DNS name, as understood by a client, to a certificate.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `names` | `array (string)` | names is a optional list of explicit DNS names (leading wildcards allowed) that should use this certificate to serve secure traffic. If no names are provided, the implicit names will be extracted from the certificates. Exact names trump over wildcard names. Explicit names defined here trump over extracted implicit names. |
| `servingCertificate` | `object` | servingCertificate references a kubernetes.io/tls type secret containing the TLS cert info for serving secure traffic. The secret must exist in the openshift-config namespace and contain the following required fields: - Secret.Data\["tls.key"\] - TLS private key. - Secret.Data\["tls.crt"\] - TLS certificate. |

## .spec.servingCerts.namedCertificates\[\].servingCertificate

Description
servingCertificate references a kubernetes.io/tls type secret containing the TLS cert info for serving secure traffic. The secret must exist in the openshift-config namespace and contain the following required fields: - Secret.Data\["tls.key"\] - TLS private key. - Secret.Data\["tls.crt"\] - TLS certificate.

Type
`object`

Required
- `name`

| Property | Type     | Description                                        |
|----------|----------|----------------------------------------------------|
| `name`   | `string` | name is the metadata.name of the referenced secret |

## .spec.tlsSecurityProfile

Description
tlsSecurityProfile specifies settings for TLS connections for externally exposed servers.

If unset, a default (which may change between releases) is chosen. Note that only Old, Intermediate and Custom profiles are currently supported, and the maximum available minTLSVersion is VersionTLS12.

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
status holds observed values from the cluster. They may not be overridden.

Type
`object`

# API endpoints

The following API endpoints are available:

- `/apis/config.openshift.io/v1/apiservers`

  - `DELETE`: delete collection of APIServer

  - `GET`: list objects of kind APIServer

  - `POST`: create an APIServer

- `/apis/config.openshift.io/v1/apiservers/{name}`

  - `DELETE`: delete an APIServer

  - `GET`: read the specified APIServer

  - `PATCH`: partially update the specified APIServer

  - `PUT`: replace the specified APIServer

- `/apis/config.openshift.io/v1/apiservers/{name}/status`

  - `GET`: read status of the specified APIServer

  - `PATCH`: partially update status of the specified APIServer

  - `PUT`: replace status of the specified APIServer

## /apis/config.openshift.io/v1/apiservers

HTTP method
`DELETE`

Description
delete collection of APIServer

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Status`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`GET`

Description
list objects of kind APIServer

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`APIServerList`](../objects/index.md#io-openshift-config-v1-APIServerList) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`POST`

Description
create an APIServer

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`APIServer`](apiserver-config-openshift-io-v1.md#apiserver-config-openshift-io-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`APIServer`](apiserver-config-openshift-io-v1.md#apiserver-config-openshift-io-v1) schema |
| 201 - Created | [`APIServer`](apiserver-config-openshift-io-v1.md#apiserver-config-openshift-io-v1) schema |
| 202 - Accepted | [`APIServer`](apiserver-config-openshift-io-v1.md#apiserver-config-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/config.openshift.io/v1/apiservers/{name}

| Parameter | Type     | Description           |
|-----------|----------|-----------------------|
| `name`    | `string` | name of the APIServer |

Global path parameters

HTTP method
`DELETE`

Description
delete an APIServer

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
read the specified APIServer

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`APIServer`](apiserver-config-openshift-io-v1.md#apiserver-config-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PATCH`

Description
partially update the specified APIServer

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`APIServer`](apiserver-config-openshift-io-v1.md#apiserver-config-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PUT`

Description
replace the specified APIServer

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`APIServer`](apiserver-config-openshift-io-v1.md#apiserver-config-openshift-io-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`APIServer`](apiserver-config-openshift-io-v1.md#apiserver-config-openshift-io-v1) schema |
| 201 - Created | [`APIServer`](apiserver-config-openshift-io-v1.md#apiserver-config-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/config.openshift.io/v1/apiservers/{name}/status

| Parameter | Type     | Description           |
|-----------|----------|-----------------------|
| `name`    | `string` | name of the APIServer |

Global path parameters

HTTP method
`GET`

Description
read status of the specified APIServer

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`APIServer`](apiserver-config-openshift-io-v1.md#apiserver-config-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PATCH`

Description
partially update status of the specified APIServer

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`APIServer`](apiserver-config-openshift-io-v1.md#apiserver-config-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PUT`

Description
replace status of the specified APIServer

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`APIServer`](apiserver-config-openshift-io-v1.md#apiserver-config-openshift-io-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`APIServer`](apiserver-config-openshift-io-v1.md#apiserver-config-openshift-io-v1) schema |
| 201 - Created | [`APIServer`](apiserver-config-openshift-io-v1.md#apiserver-config-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses
