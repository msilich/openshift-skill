<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Description
OperatorPKI is a simple certificate authority. It is not intended for external use - rather, it is internal to the network operator. The CNO creates a CA and a certificate signed by that CA. The certificate has both ClientAuth and ServerAuth extended usages enabled.

    More specifically, given an OperatorPKI with <name>, the CNO will manage:

- A Secret called \<name\>-ca with two data keys:

- tls.key - the private key

- tls.crt - the CA certificate

- A ConfigMap called \<name\>-ca with a single data key:

- cabundle.crt - the CA certificate(s)

- A Secret called \<name\>-cert with two data keys:

- tls.key - the private key

- tls.crt - the certificate, signed by the CA

The CA certificate will have a validity of 10 years, rotated after 9. The target certificate will have a validity of 6 months, rotated after 3

The CA certificate will have a CommonName of "\<namespace\>\_\<name\>-ca@\<timestamp\>", where \<timestamp\> is the last rotation time.

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
| `spec` | `object` | OperatorPKISpec is the PKI configuration. |
| `status` | `object` | OperatorPKIStatus is not implemented. |

## .spec

Description
OperatorPKISpec is the PKI configuration.

Type
`object`

Required
- `targetCert`

| Property | Type | Description |
|----|----|----|
| `targetCert` | `object` | targetCert configures the certificate signed by the CA. It will have both ClientAuth and ServerAuth enabled |

## .spec.targetCert

Description
targetCert configures the certificate signed by the CA. It will have both ClientAuth and ServerAuth enabled

Type
`object`

Required
- `commonName`

| Property     | Type     | Description                                     |
|--------------|----------|-------------------------------------------------|
| `commonName` | `string` | commonName is the value in the certificate’s CN |

## .status

Description
OperatorPKIStatus is not implemented.

Type
`object`

# API endpoints

The following API endpoints are available:

- `/apis/network.operator.openshift.io/v1/operatorpkis`

  - `GET`: list objects of kind OperatorPKI

- `/apis/network.operator.openshift.io/v1/namespaces/{namespace}/operatorpkis`

  - `DELETE`: delete collection of OperatorPKI

  - `GET`: list objects of kind OperatorPKI

  - `POST`: create an OperatorPKI

- `/apis/network.operator.openshift.io/v1/namespaces/{namespace}/operatorpkis/{name}`

  - `DELETE`: delete an OperatorPKI

  - `GET`: read the specified OperatorPKI

  - `PATCH`: partially update the specified OperatorPKI

  - `PUT`: replace the specified OperatorPKI

## /apis/network.operator.openshift.io/v1/operatorpkis

HTTP method
`GET`

Description
list objects of kind OperatorPKI

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`OperatorPKIList`](../objects/index.md#io-openshift-operator-network-v1-OperatorPKIList) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/network.operator.openshift.io/v1/namespaces/{namespace}/operatorpkis

HTTP method
`DELETE`

Description
delete collection of OperatorPKI

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Status`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`GET`

Description
list objects of kind OperatorPKI

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`OperatorPKIList`](../objects/index.md#io-openshift-operator-network-v1-OperatorPKIList) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`POST`

Description
create an OperatorPKI

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`OperatorPKI`](operatorpki-network-operator-openshift-io-v1.md#operatorpki-network-operator-openshift-io-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`OperatorPKI`](operatorpki-network-operator-openshift-io-v1.md#operatorpki-network-operator-openshift-io-v1) schema |
| 201 - Created | [`OperatorPKI`](operatorpki-network-operator-openshift-io-v1.md#operatorpki-network-operator-openshift-io-v1) schema |
| 202 - Accepted | [`OperatorPKI`](operatorpki-network-operator-openshift-io-v1.md#operatorpki-network-operator-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/network.operator.openshift.io/v1/namespaces/{namespace}/operatorpkis/{name}

| Parameter | Type     | Description             |
|-----------|----------|-------------------------|
| `name`    | `string` | name of the OperatorPKI |

Global path parameters

HTTP method
`DELETE`

Description
delete an OperatorPKI

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
read the specified OperatorPKI

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`OperatorPKI`](operatorpki-network-operator-openshift-io-v1.md#operatorpki-network-operator-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PATCH`

Description
partially update the specified OperatorPKI

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`OperatorPKI`](operatorpki-network-operator-openshift-io-v1.md#operatorpki-network-operator-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PUT`

Description
replace the specified OperatorPKI

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`OperatorPKI`](operatorpki-network-operator-openshift-io-v1.md#operatorpki-network-operator-openshift-io-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`OperatorPKI`](operatorpki-network-operator-openshift-io-v1.md#operatorpki-network-operator-openshift-io-v1) schema |
| 201 - Created | [`OperatorPKI`](operatorpki-network-operator-openshift-io-v1.md#operatorpki-network-operator-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses
