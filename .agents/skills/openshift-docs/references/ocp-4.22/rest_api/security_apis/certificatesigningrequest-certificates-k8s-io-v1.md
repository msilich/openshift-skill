<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Description
CertificateSigningRequest objects provide a mechanism to obtain x509 certificates by submitting a certificate signing request, and having it asynchronously approved and issued.

Kubelets use this API to obtain: 1. client certificates to authenticate to kube-apiserver (with the "kubernetes.io/kube-apiserver-client-kubelet" signerName). 2. serving certificates for TLS endpoints kube-apiserver can connect to securely (with the "kubernetes.io/kubelet-serving" signerName).

This API can be used to request client certificates to authenticate to kube-apiserver (with the "kubernetes.io/kube-apiserver-client" signerName), or to obtain certificates from custom non-Kubernetes signers.

Type
`object`

Required
- `spec`

# Specification

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ObjectMeta`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) |  |
| `spec` | `object` | CertificateSigningRequestSpec contains the certificate request. |
| `status` | `object` | CertificateSigningRequestStatus contains conditions used to indicate approved/denied/failed status of the request, and the issued certificate. |

## .spec

Description
CertificateSigningRequestSpec contains the certificate request.

Type
`object`

Required
- `request`

- `signerName`

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
<td style="text-align: left;"><p><code>expirationSeconds</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p>expirationSeconds is the requested duration of validity of the issued certificate. The certificate signer may issue a certificate with a different validity duration so a client must check the delta between the notBefore and and notAfter fields in the issued certificate to determine the actual duration.</p>
<p>The v1.22+ in-tree implementations of the well-known Kubernetes signers will honor this field as long as the requested duration is not greater than the maximum duration they will honor per the --cluster-signing-duration CLI flag to the Kubernetes controller manager.</p>
<p>Certificate signers may not honor this field for various reasons:</p>
<p>1. Old signer that is unaware of the field (such as the in-tree implementations prior to v1.22) 2. Signer whose configured maximum is shorter than the requested duration 3. Signer whose configured minimum is longer than the requested duration</p>
<p>The minimum valid value for expirationSeconds is 600, i.e. 10 minutes.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>extra</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>extra contains extra attributes of the user that created the CertificateSigningRequest. Populated by the API server on creation and immutable.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>extra{}</code></p></td>
<td style="text-align: left;"><p><code>array (string)</code></p></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>groups</code></p></td>
<td style="text-align: left;"><p><code>array (string)</code></p></td>
<td style="text-align: left;"><p>groups contains group membership of the user that created the CertificateSigningRequest. Populated by the API server on creation and immutable.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>request</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>request contains an x509 certificate signing request encoded in a "CERTIFICATE REQUEST" PEM block. When serialized as JSON or YAML, the data is additionally base64-encoded.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>signerName</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>signerName indicates the requested signer, and is a qualified name.</p>
<p>List/watch requests for CertificateSigningRequests can filter on this field using a "spec.signerName=NAME" fieldSelector.</p>
<p>Well-known Kubernetes signers are: 1. "kubernetes.io/kube-apiserver-client": issues client certificates that can be used to authenticate to kube-apiserver. Requests for this signer are never auto-approved by kube-controller-manager, can be issued by the "csrsigning" controller in kube-controller-manager. 2. "kubernetes.io/kube-apiserver-client-kubelet": issues client certificates that kubelets use to authenticate to kube-apiserver. Requests for this signer can be auto-approved by the "csrapproving" controller in kube-controller-manager, and can be issued by the "csrsigning" controller in kube-controller-manager. 3. "kubernetes.io/kubelet-serving" issues serving certificates that kubelets use to serve TLS endpoints, which kube-apiserver can connect to securely. Requests for this signer are never auto-approved by kube-controller-manager, and can be issued by the "csrsigning" controller in kube-controller-manager.</p>
<p>More details are available at <a href="https://k8s.io/docs/reference/access-authn-authz/certificate-signing-requests/#kubernetes-signers">https://k8s.io/docs/reference/access-authn-authz/certificate-signing-requests/#kubernetes-signers</a></p>
<p>Custom signerNames can also be specified. The signer defines: 1. Trust distribution: how trust (CA bundles) are distributed. 2. Permitted subjects: and behavior when a disallowed subject is requested. 3. Required, permitted, or forbidden x509 extensions in the request (including whether subjectAltNames are allowed, which types, restrictions on allowed values) and behavior when a disallowed extension is requested. 4. Required, permitted, or forbidden key usages / extended key usages. 5. Expiration/certificate lifetime: whether it is fixed by the signer, configurable by the admin. 6. Whether or not requests for CA certificates are allowed.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>uid</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>uid contains the uid of the user that created the CertificateSigningRequest. Populated by the API server on creation and immutable.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>usages</code></p></td>
<td style="text-align: left;"><p><code>array (string)</code></p></td>
<td style="text-align: left;"><p>usages specifies a set of key usages requested in the issued certificate.</p>
<p>Requests for TLS client certificates typically request: "digital signature", "key encipherment", "client auth".</p>
<p>Requests for TLS serving certificates typically request: "key encipherment", "digital signature", "server auth".</p>
<p>Valid values are: "signing", "digital signature", "content commitment", "key encipherment", "key agreement", "data encipherment", "cert sign", "crl sign", "encipher only", "decipher only", "any", "server auth", "client auth", "code signing", "email protection", "s/mime", "ipsec end system", "ipsec tunnel", "ipsec user", "timestamping", "ocsp signing", "microsoft sgc", "netscape sgc"</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>username</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>username contains the name of the user that created the CertificateSigningRequest. Populated by the API server on creation and immutable.</p></td>
</tr>
</tbody>
</table>

## .spec.extra

Description
extra contains extra attributes of the user that created the CertificateSigningRequest. Populated by the API server on creation and immutable.

Type
`object`

## .status

Description
CertificateSigningRequestStatus contains conditions used to indicate approved/denied/failed status of the request, and the issued certificate.

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
<td style="text-align: left;"><p><code>certificate</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>certificate is populated with an issued certificate by the signer after an Approved condition is present. This field is set via the /status subresource. Once populated, this field is immutable.</p>
<p>If the certificate signing request is denied, a condition of type "Denied" is added and this field remains empty. If the signer cannot issue the certificate, a condition of type "Failed" is added and this field remains empty.</p>
<p>Validation requirements: 1. certificate must contain one or more PEM blocks. 2. All PEM blocks must have the "CERTIFICATE" label, contain no headers, and the encoded data must be a BER-encoded ASN.1 Certificate structure as described in section 4 of RFC5280. 3. Non-PEM content may appear before or after the "CERTIFICATE" PEM blocks and is unvalidated, to allow for explanatory text as described in section 5.2 of RFC7468.</p>
<p>If more than one PEM block is present, and the definition of the requested spec.signerName does not indicate otherwise, the first block is the issued certificate, and subsequent blocks should be treated as intermediate certificates and presented in TLS handshakes.</p>
<p>The certificate is encoded in PEM format.</p>
<p>When serialized as JSON or YAML, the data is additionally base64-encoded, so it consists of:</p>
<p>base64( -----BEGIN CERTIFICATE----- …​ -----END CERTIFICATE----- )</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>conditions</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>conditions applied to the request. Known conditions are "Approved", "Denied", and "Failed".</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>conditions[]</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>CertificateSigningRequestCondition describes a condition of a CertificateSigningRequest object</p></td>
</tr>
</tbody>
</table>

## .status.conditions

Description
conditions applied to the request. Known conditions are "Approved", "Denied", and "Failed".

Type
`array`

## .status.conditions\[\]

Description
CertificateSigningRequestCondition describes a condition of a CertificateSigningRequest object

Type
`object`

Required
- `type`

- `status`

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
<td style="text-align: left;"><p><code>lastTransitionTime</code></p></td>
<td style="text-align: left;"><p><a href="../objects/index.xml#io-k8s-apimachinery-pkg-apis-meta-v1-Time"><code>Time</code></a></p></td>
<td style="text-align: left;"><p>lastTransitionTime is the time the condition last transitioned from one status to another. If unset, when a new condition type is added or an existing condition’s status is changed, the server defaults this to the current time.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>lastUpdateTime</code></p></td>
<td style="text-align: left;"><p><a href="../objects/index.xml#io-k8s-apimachinery-pkg-apis-meta-v1-Time"><code>Time</code></a></p></td>
<td style="text-align: left;"><p>lastUpdateTime is the time of the last update to this condition</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>message</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>message contains a human readable message with details about the request state</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>reason</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>reason indicates a brief reason for the request state</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>status</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>status of the condition, one of True, False, Unknown. Approved, Denied, and Failed conditions may not be "False" or "Unknown".</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>type</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>type of the condition. Known conditions are "Approved", "Denied", and "Failed".</p>
<p>An "Approved" condition is added via the /approval subresource, indicating the request was approved and should be issued by the signer.</p>
<p>A "Denied" condition is added via the /approval subresource, indicating the request was denied and should not be issued by the signer.</p>
<p>A "Failed" condition is added via the /status subresource, indicating the signer failed to issue the certificate.</p>
<p>Approved and Denied conditions are mutually exclusive. Approved, Denied, and Failed conditions cannot be removed once added.</p>
<p>Only one condition of a given type is allowed.</p></td>
</tr>
</tbody>
</table>

# API endpoints

The following API endpoints are available:

- `/apis/certificates.k8s.io/v1/certificatesigningrequests`

  - `DELETE`: delete collection of CertificateSigningRequest

  - `GET`: list or watch objects of kind CertificateSigningRequest

  - `POST`: create a CertificateSigningRequest

- `/apis/certificates.k8s.io/v1/watch/certificatesigningrequests`

  - `GET`: watch individual changes to a list of CertificateSigningRequest. deprecated: use the 'watch' parameter with a list operation instead.

- `/apis/certificates.k8s.io/v1/certificatesigningrequests/{name}`

  - `DELETE`: delete a CertificateSigningRequest

  - `GET`: read the specified CertificateSigningRequest

  - `PATCH`: partially update the specified CertificateSigningRequest

  - `PUT`: replace the specified CertificateSigningRequest

- `/apis/certificates.k8s.io/v1/watch/certificatesigningrequests/{name}`

  - `GET`: watch changes to an object of kind CertificateSigningRequest. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.

- `/apis/certificates.k8s.io/v1/certificatesigningrequests/{name}/status`

  - `GET`: read status of the specified CertificateSigningRequest

  - `PATCH`: partially update status of the specified CertificateSigningRequest

  - `PUT`: replace status of the specified CertificateSigningRequest

- `/apis/certificates.k8s.io/v1/certificatesigningrequests/{name}/approval`

  - `GET`: read approval of the specified CertificateSigningRequest

  - `PATCH`: partially update approval of the specified CertificateSigningRequest

  - `PUT`: replace approval of the specified CertificateSigningRequest

## /apis/certificates.k8s.io/v1/certificatesigningrequests

HTTP method
`DELETE`

Description
delete collection of CertificateSigningRequest

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |

Query parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Status`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`GET`

Description
list or watch objects of kind CertificateSigningRequest

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`CertificateSigningRequestList`](../objects/index.md#io-k8s-api-certificates-v1-CertificateSigningRequestList) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`POST`

Description
create a CertificateSigningRequest

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`CertificateSigningRequest`](certificatesigningrequest-certificates-k8s-io-v1.md#certificatesigningrequest-certificates-k8s-io-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`CertificateSigningRequest`](certificatesigningrequest-certificates-k8s-io-v1.md#certificatesigningrequest-certificates-k8s-io-v1) schema |
| 201 - Created | [`CertificateSigningRequest`](certificatesigningrequest-certificates-k8s-io-v1.md#certificatesigningrequest-certificates-k8s-io-v1) schema |
| 202 - Accepted | [`CertificateSigningRequest`](certificatesigningrequest-certificates-k8s-io-v1.md#certificatesigningrequest-certificates-k8s-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/certificates.k8s.io/v1/watch/certificatesigningrequests

HTTP method
`GET`

Description
watch individual changes to a list of CertificateSigningRequest. deprecated: use the 'watch' parameter with a list operation instead.

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`WatchEvent`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/certificates.k8s.io/v1/certificatesigningrequests/{name}

| Parameter | Type     | Description                           |
|-----------|----------|---------------------------------------|
| `name`    | `string` | name of the CertificateSigningRequest |

Global path parameters

HTTP method
`DELETE`

Description
delete a CertificateSigningRequest

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
read the specified CertificateSigningRequest

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`CertificateSigningRequest`](certificatesigningrequest-certificates-k8s-io-v1.md#certificatesigningrequest-certificates-k8s-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PATCH`

Description
partially update the specified CertificateSigningRequest

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`CertificateSigningRequest`](certificatesigningrequest-certificates-k8s-io-v1.md#certificatesigningrequest-certificates-k8s-io-v1) schema |
| 201 - Created | [`CertificateSigningRequest`](certificatesigningrequest-certificates-k8s-io-v1.md#certificatesigningrequest-certificates-k8s-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PUT`

Description
replace the specified CertificateSigningRequest

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`CertificateSigningRequest`](certificatesigningrequest-certificates-k8s-io-v1.md#certificatesigningrequest-certificates-k8s-io-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`CertificateSigningRequest`](certificatesigningrequest-certificates-k8s-io-v1.md#certificatesigningrequest-certificates-k8s-io-v1) schema |
| 201 - Created | [`CertificateSigningRequest`](certificatesigningrequest-certificates-k8s-io-v1.md#certificatesigningrequest-certificates-k8s-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/certificates.k8s.io/v1/watch/certificatesigningrequests/{name}

| Parameter | Type     | Description                           |
|-----------|----------|---------------------------------------|
| `name`    | `string` | name of the CertificateSigningRequest |

Global path parameters

HTTP method
`GET`

Description
watch changes to an object of kind CertificateSigningRequest. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`WatchEvent`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/certificates.k8s.io/v1/certificatesigningrequests/{name}/status

| Parameter | Type     | Description                           |
|-----------|----------|---------------------------------------|
| `name`    | `string` | name of the CertificateSigningRequest |

Global path parameters

HTTP method
`GET`

Description
read status of the specified CertificateSigningRequest

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`CertificateSigningRequest`](certificatesigningrequest-certificates-k8s-io-v1.md#certificatesigningrequest-certificates-k8s-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PATCH`

Description
partially update status of the specified CertificateSigningRequest

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`CertificateSigningRequest`](certificatesigningrequest-certificates-k8s-io-v1.md#certificatesigningrequest-certificates-k8s-io-v1) schema |
| 201 - Created | [`CertificateSigningRequest`](certificatesigningrequest-certificates-k8s-io-v1.md#certificatesigningrequest-certificates-k8s-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PUT`

Description
replace status of the specified CertificateSigningRequest

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`CertificateSigningRequest`](certificatesigningrequest-certificates-k8s-io-v1.md#certificatesigningrequest-certificates-k8s-io-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`CertificateSigningRequest`](certificatesigningrequest-certificates-k8s-io-v1.md#certificatesigningrequest-certificates-k8s-io-v1) schema |
| 201 - Created | [`CertificateSigningRequest`](certificatesigningrequest-certificates-k8s-io-v1.md#certificatesigningrequest-certificates-k8s-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/certificates.k8s.io/v1/certificatesigningrequests/{name}/approval

| Parameter | Type     | Description                           |
|-----------|----------|---------------------------------------|
| `name`    | `string` | name of the CertificateSigningRequest |

Global path parameters

HTTP method
`GET`

Description
read approval of the specified CertificateSigningRequest

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`CertificateSigningRequest`](certificatesigningrequest-certificates-k8s-io-v1.md#certificatesigningrequest-certificates-k8s-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PATCH`

Description
partially update approval of the specified CertificateSigningRequest

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`CertificateSigningRequest`](certificatesigningrequest-certificates-k8s-io-v1.md#certificatesigningrequest-certificates-k8s-io-v1) schema |
| 201 - Created | [`CertificateSigningRequest`](certificatesigningrequest-certificates-k8s-io-v1.md#certificatesigningrequest-certificates-k8s-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PUT`

Description
replace approval of the specified CertificateSigningRequest

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`CertificateSigningRequest`](certificatesigningrequest-certificates-k8s-io-v1.md#certificatesigningrequest-certificates-k8s-io-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`CertificateSigningRequest`](certificatesigningrequest-certificates-k8s-io-v1.md#certificatesigningrequest-certificates-k8s-io-v1) schema |
| 201 - Created | [`CertificateSigningRequest`](certificatesigningrequest-certificates-k8s-io-v1.md#certificatesigningrequest-certificates-k8s-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses
