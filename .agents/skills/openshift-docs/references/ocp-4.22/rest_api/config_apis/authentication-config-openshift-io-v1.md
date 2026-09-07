<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Description
Authentication specifies cluster-wide settings for authentication (like OAuth and webhook token authenticators). The canonical name of an instance is `cluster`.

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
<td style="text-align: left;"><p><code>oauthMetadata</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>oauthMetadata contains the discovery endpoint data for OAuth 2.0 Authorization Server Metadata for an external OAuth server. This discovery document can be viewed from its served location: oc get --raw '/.well-known/oauth-authorization-server' For further details, see the IETF Draft: <a href="https://tools.ietf.org/html/draft-ietf-oauth-discovery-04#section-2">https://tools.ietf.org/html/draft-ietf-oauth-discovery-04#section-2</a> If oauthMetadata.name is non-empty, this value has precedence over any metadata reference stored in status. The key "oauthMetadata" is used to locate the data. If specified and the config map or expected key is not found, no metadata is served. If the specified metadata is not valid, no metadata is served. The namespace for this config map is openshift-config.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>oidcProviders</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>oidcProviders are OIDC identity providers that can issue tokens for this cluster Can only be set if "Type" is set to "OIDC".</p>
<p>At most one provider can be configured.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>oidcProviders[]</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>serviceAccountIssuer</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>serviceAccountIssuer is the identifier of the bound service account token issuer. The default is <a href="https://kubernetes.default.svc">https://kubernetes.default.svc</a> WARNING: Updating this field will not result in immediate invalidation of all bound tokens with the previous issuer value. Instead, the tokens issued by previous service account issuer will continue to be trusted for a time period chosen by the platform (currently set to 24h). This time period is subject to change over time. This allows internal components to transition to use new service account issuer without service distruption.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>type</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>type identifies the cluster managed, user facing authentication mode in use. Specifically, it manages the component that responds to login attempts. The default is IntegratedOAuth.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>webhookTokenAuthenticator</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>webhookTokenAuthenticator configures a remote token reviewer. These remote authentication webhooks can be used to verify bearer tokens via the tokenreviews.authentication.k8s.io REST API. This is required to honor bearer tokens that are provisioned by an external authentication service.</p>
<p>Can only be set if "Type" is set to "None".</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>webhookTokenAuthenticators</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>webhookTokenAuthenticators is DEPRECATED, setting it has no effect.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>webhookTokenAuthenticators[]</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>deprecatedWebhookTokenAuthenticator holds the necessary configuration options for a remote token authenticator. It’s the same as WebhookTokenAuthenticator but it’s missing the 'required' validation on KubeConfig field.</p></td>
</tr>
</tbody>
</table>

## .spec.oauthMetadata

Description
oauthMetadata contains the discovery endpoint data for OAuth 2.0 Authorization Server Metadata for an external OAuth server. This discovery document can be viewed from its served location: oc get --raw '/.well-known/oauth-authorization-server' For further details, see the IETF Draft: <https://tools.ietf.org/html/draft-ietf-oauth-discovery-04#section-2> If oauthMetadata.name is non-empty, this value has precedence over any metadata reference stored in status. The key "oauthMetadata" is used to locate the data. If specified and the config map or expected key is not found, no metadata is served. If the specified metadata is not valid, no metadata is served. The namespace for this config map is openshift-config.

Type
`object`

Required
- `name`

| Property | Type     | Description                                            |
|----------|----------|--------------------------------------------------------|
| `name`   | `string` | name is the metadata.name of the referenced config map |

## .spec.oidcProviders

Description
oidcProviders are OIDC identity providers that can issue tokens for this cluster Can only be set if "Type" is set to "OIDC".

At most one provider can be configured.

Type
`array`

## .spec.oidcProviders\[\]

Description

Type
`object`

Required
- `claimMappings`

- `issuer`

- `name`

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
<td style="text-align: left;"><p><code>claimMappings</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>claimMappings is a required field that configures the rules to be used by the Kubernetes API server for translating claims in a JWT token, issued by the identity provider, to a cluster identity.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>claimValidationRules</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>claimValidationRules is an optional field that configures the rules to be used by the Kubernetes API server for validating the claims in a JWT token issued by the identity provider.</p>
<p>Validation rules are joined via an AND operation.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>claimValidationRules[]</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>TokenClaimValidationRule represents a validation rule based on token claims. If type is RequiredClaim, requiredClaim must be set. If Type is CEL, CEL must be set and RequiredClaim must be omitted.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>issuer</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>issuer is a required field that configures how the platform interacts with the identity provider and how tokens issued from the identity provider are evaluated by the Kubernetes API server.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>name</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>name is a required field that configures the unique human-readable identifier associated with the identity provider. It is used to distinguish between multiple identity providers and has no impact on token validation or authentication mechanics.</p>
<p>name must not be an empty string ("").</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>oidcClients</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>oidcClients is an optional field that configures how on-cluster, platform clients should request tokens from the identity provider. oidcClients must not exceed 20 entries and entries must have unique namespace/name pairs.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>oidcClients[]</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>OIDCClientConfig configures how platform clients interact with identity providers as an authentication method.</p></td>
</tr>
</tbody>
</table>

## .spec.oidcProviders\[\].claimMappings

Description
claimMappings is a required field that configures the rules to be used by the Kubernetes API server for translating claims in a JWT token, issued by the identity provider, to a cluster identity.

Type
`object`

Required
- `username`

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
<td style="text-align: left;"><p><code>extra</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>extra is an optional field for configuring the mappings used to construct the extra attribute for the cluster identity. When omitted, no extra attributes will be present on the cluster identity.</p>
<p>key values for extra mappings must be unique. A maximum of 32 extra attribute mappings may be provided.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>extra[]</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>ExtraMapping allows specifying a key and CEL expression to evaluate the keys' value. It is used to create additional mappings and attributes added to a cluster identity from a provided authentication token.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>groups</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>groups is an optional field that configures how the groups of a cluster identity should be constructed from the claims in a JWT token issued by the identity provider.</p>
<p>When referencing a claim, if the claim is present in the JWT token, its value must be a list of groups separated by a comma (',').</p>
<p>For example - '"example"' and '"exampleOne", "exampleTwo", "exampleThree"' are valid claim values.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>uid</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>uid is an optional field for configuring the claim mapping used to construct the uid for the cluster identity.</p>
<p>When using uid.claim to specify the claim it must be a single string value. When using uid.expression the expression must result in a single string value.</p>
<p>When omitted, this means the user has no opinion and the platform is left to choose a default, which is subject to change over time.</p>
<p>The current default is to use the 'sub' claim.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>username</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>username is a required field that configures how the username of a cluster identity should be constructed from the claims in a JWT token issued by the identity provider.</p></td>
</tr>
</tbody>
</table>

## .spec.oidcProviders\[\].claimMappings.extra

Description
extra is an optional field for configuring the mappings used to construct the extra attribute for the cluster identity. When omitted, no extra attributes will be present on the cluster identity.

key values for extra mappings must be unique. A maximum of 32 extra attribute mappings may be provided.

Type
`array`

## .spec.oidcProviders\[\].claimMappings.extra\[\]

Description
ExtraMapping allows specifying a key and CEL expression to evaluate the keys' value. It is used to create additional mappings and attributes added to a cluster identity from a provided authentication token.

Type
`object`

Required
- `key`

- `valueExpression`

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
<td style="text-align: left;"><p><code>key</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>key is a required field that specifies the string to use as the extra attribute key.</p>
<p>key must be a domain-prefix path (e.g 'example.org/foo'). key must not exceed 510 characters in length. key must contain the '/' character, separating the domain and path characters. key must not be empty.</p>
<p>The domain portion of the key (string of characters prior to the '/') must be a valid RFC1123 subdomain. It must not exceed 253 characters in length. It must start and end with an alphanumeric character. It must only contain lower case alphanumeric characters and '-' or '.'. It must not use the reserved domains, or be subdomains of, "kubernetes.io", "k8s.io", and "openshift.io".</p>
<p>The path portion of the key (string of characters after the '/') must not be empty and must consist of at least one alphanumeric character, percent-encoded octets, '-', '.', '_', '~', '!', '$', '&amp;', ''', '(', ')', '*', '+', ',', ';', '=', and ':'. It must not exceed 256 characters in length.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>valueExpression</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>valueExpression is a required field to specify the CEL expression to extract the extra attribute value from a JWT token’s claims. valueExpression must produce a string or string array value. "", [], and null are treated as the extra mapping not being present. Empty string values within an array are filtered out.</p>
<p>CEL expressions have access to the token claims through a CEL variable, 'claims'. 'claims' is a map of claim names to claim values. For example, the 'sub' claim value can be accessed as 'claims.sub'. Nested claims can be accessed using dot notation ('claims.foo.bar').</p>
<p>valueExpression must not exceed 1024 characters in length. valueExpression must not be empty.</p></td>
</tr>
</tbody>
</table>

## .spec.oidcProviders\[\].claimMappings.groups

Description
groups is an optional field that configures how the groups of a cluster identity should be constructed from the claims in a JWT token issued by the identity provider.

When referencing a claim, if the claim is present in the JWT token, its value must be a list of groups separated by a comma (',').

For example - '"example"' and '"exampleOne", "exampleTwo", "exampleThree"' are valid claim values.

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
<td style="text-align: left;"><p><code>claim</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>claim is an optional field for specifying the JWT token claim that is used in the mapping. The value of this claim will be assigned to the field in which this mapping is associated. claim must not exceed 256 characters in length. When set to the empty string <code>""</code>, this means that no named claim should be used for the group mapping. claim is required when the ExternalOIDCWithUpstreamParity feature gate is not enabled.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>prefix</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>prefix is an optional field that configures the prefix that will be applied to the cluster identity attribute during the process of mapping JWT claims to cluster identity attributes.</p>
<p>When omitted or set to an empty string (""), no prefix is applied to the cluster identity attribute. Must not be set to a non-empty value when expression is set.</p>
<p>Example: if <code>prefix</code> is set to "myoidc:" and the <code>claim</code> in JWT contains an array of strings "a", "b" and "c", the mapping will result in an array of string "myoidc:a", "myoidc:b" and "myoidc:c".</p></td>
</tr>
</tbody>
</table>

## .spec.oidcProviders\[\].claimMappings.uid

Description
uid is an optional field for configuring the claim mapping used to construct the uid for the cluster identity.

When using uid.claim to specify the claim it must be a single string value. When using uid.expression the expression must result in a single string value.

When omitted, this means the user has no opinion and the platform is left to choose a default, which is subject to change over time.

The current default is to use the 'sub' claim.

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
<td style="text-align: left;"><p><code>claim</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>claim is an optional field for specifying the JWT token claim that is used in the mapping. The value of this claim will be assigned to the field in which this mapping is associated.</p>
<p>Precisely one of claim or expression must be set. claim must not be specified when expression is set. When specified, claim must be at least 1 character in length and must not exceed 256 characters in length.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>expression</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>expression is an optional field for specifying a CEL expression that produces a string value from JWT token claims.</p>
<p>CEL expressions have access to the token claims through a CEL variable, 'claims'. 'claims' is a map of claim names to claim values. For example, the 'sub' claim value can be accessed as 'claims.sub'. Nested claims can be accessed using dot notation ('claims.foo.bar').</p>
<p>Precisely one of claim or expression must be set. expression must not be specified when claim is set. When specified, expression must be at least 1 character in length and must not exceed 1024 characters in length.</p></td>
</tr>
</tbody>
</table>

## .spec.oidcProviders\[\].claimMappings.username

Description
username is a required field that configures how the username of a cluster identity should be constructed from the claims in a JWT token issued by the identity provider.

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
<td style="text-align: left;"><p><code>claim</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>claim is an optional field that configures the JWT token claim whose value is assigned to the cluster identity field associated with this mapping. claim is required when the ExternalOIDCWithUpstreamParity feature gate is not enabled. When the ExternalOIDCWithUpstreamParity feature gate is enabled, claim must not be set when expression is set.</p>
<p>claim must not be an empty string ("") and must not exceed 256 characters.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>prefix</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>prefix configures the prefix that should be prepended to the value of the JWT claim.</p>
<p>prefix must be set when prefixPolicy is set to 'Prefix' and must be unset otherwise.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>prefixPolicy</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>prefixPolicy is an optional field that configures how a prefix should be applied to the value of the JWT claim specified in the 'claim' field.</p>
<p>Allowed values are 'Prefix', 'NoPrefix', and omitted (not provided or an empty string).</p>
<p>When set to 'Prefix', the value specified in the prefix field will be prepended to the value of the JWT claim. The prefix field must be set when prefixPolicy is 'Prefix'. Must not be set to 'Prefix' when expression is set. When set to 'NoPrefix', no prefix will be prepended to the value of the JWT claim. When omitted, this means no opinion and the platform is left to choose any prefixes that are applied which is subject to change over time. Currently, the platform prepends <code>{issuerURL}#</code> to the value of the JWT claim when the claim is not 'email'.</p>
<p>As an example, consider the following scenario:</p>
<p><code>prefix</code> is unset, <code>issuerURL</code> is set to <code>https://myoidc.tld</code>, the JWT claims include "username":"userA" and "email":"<a href="mailto:userA@myoidc.tld">userA@myoidc.tld</a>", and <code>claim</code> is set to: - "username": the mapped value will be "https://myoidc.tld#userA" - "email": the mapped value will be "<a href="mailto:userA@myoidc.tld">userA@myoidc.tld</a>"</p></td>
</tr>
</tbody>
</table>

## .spec.oidcProviders\[\].claimMappings.username.prefix

Description
prefix configures the prefix that should be prepended to the value of the JWT claim.

prefix must be set when prefixPolicy is set to 'Prefix' and must be unset otherwise.

Type
`object`

Required
- `prefixString`

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
<td style="text-align: left;"><p><code>prefixString</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>prefixString is a required field that configures the prefix that will be applied to cluster identity username attribute during the process of mapping JWT claims to cluster identity attributes.</p>
<p>prefixString must not be an empty string ("").</p></td>
</tr>
</tbody>
</table>

## .spec.oidcProviders\[\].claimValidationRules

Description
claimValidationRules is an optional field that configures the rules to be used by the Kubernetes API server for validating the claims in a JWT token issued by the identity provider.

Validation rules are joined via an AND operation.

Type
`array`

## .spec.oidcProviders\[\].claimValidationRules\[\]

Description
TokenClaimValidationRule represents a validation rule based on token claims. If type is RequiredClaim, requiredClaim must be set. If Type is CEL, CEL must be set and RequiredClaim must be omitted.

Type
`object`

Required
- `type`

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
<td style="text-align: left;"><p><code>requiredClaim</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>requiredClaim allows configuring a required claim name and its expected value. This field is required when <code>type</code> is set to RequiredClaim, and must be omitted when <code>type</code> is set to any other value. The Kubernetes API server uses this field to validate if an incoming JWT is valid for this identity provider.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>type</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>type is an optional field that configures the type of the validation rule.</p>
<p>Allowed values are "RequiredClaim" and "CEL".</p>
<p>When set to 'RequiredClaim', the Kubernetes API server will be configured to validate that the incoming JWT contains the required claim and that its value matches the required value.</p>
<p>When set to 'CEL', the Kubernetes API server will be configured to validate the incoming JWT against the configured CEL expression.</p></td>
</tr>
</tbody>
</table>

## .spec.oidcProviders\[\].claimValidationRules\[\].requiredClaim

Description
requiredClaim allows configuring a required claim name and its expected value. This field is required when `type` is set to RequiredClaim, and must be omitted when `type` is set to any other value. The Kubernetes API server uses this field to validate if an incoming JWT is valid for this identity provider.

Type
`object`

Required
- `claim`

- `requiredValue`

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
<td style="text-align: left;"><p><code>claim</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>claim is a required field that configures the name of the required claim. When taken from the JWT claims, claim must be a string value.</p>
<p>claim must not be an empty string ("").</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>requiredValue</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>requiredValue is a required field that configures the value that 'claim' must have when taken from the incoming JWT claims. If the value in the JWT claims does not match, the token will be rejected for authentication.</p>
<p>requiredValue must not be an empty string ("").</p></td>
</tr>
</tbody>
</table>

## .spec.oidcProviders\[\].issuer

Description
issuer is a required field that configures how the platform interacts with the identity provider and how tokens issued from the identity provider are evaluated by the Kubernetes API server.

Type
`object`

Required
- `audiences`

- `issuerURL`

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
<td style="text-align: left;"><p><code>audiences</code></p></td>
<td style="text-align: left;"><p><code>array (string)</code></p></td>
<td style="text-align: left;"><p>audiences is a required field that configures the acceptable audiences the JWT token, issued by the identity provider, must be issued to. At least one of the entries must match the 'aud' claim in the JWT token.</p>
<p>audiences must contain at least one entry and must not exceed ten entries.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>issuerCertificateAuthority</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>issuerCertificateAuthority is an optional field that configures the certificate authority, used by the Kubernetes API server, to validate the connection to the identity provider when fetching discovery information.</p>
<p>When not specified, the system trust is used.</p>
<p>When specified, it must reference a ConfigMap in the openshift-config namespace containing the PEM-encoded CA certificates under the 'ca-bundle.crt' key in the data field of the ConfigMap.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>issuerURL</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>issuerURL is a required field that configures the URL used to issue tokens by the identity provider. The Kubernetes API server determines how authentication tokens should be handled by matching the 'iss' claim in the JWT to the issuerURL of configured identity providers.</p>
<p>Must be at least 1 character and must not exceed 512 characters in length. Must be a valid URL that uses the 'https' scheme and does not contain a query, fragment or user.</p></td>
</tr>
</tbody>
</table>

## .spec.oidcProviders\[\].issuer.issuerCertificateAuthority

Description
issuerCertificateAuthority is an optional field that configures the certificate authority, used by the Kubernetes API server, to validate the connection to the identity provider when fetching discovery information.

When not specified, the system trust is used.

When specified, it must reference a ConfigMap in the openshift-config namespace containing the PEM-encoded CA certificates under the 'ca-bundle.crt' key in the data field of the ConfigMap.

Type
`object`

Required
- `name`

| Property | Type     | Description                                            |
|----------|----------|--------------------------------------------------------|
| `name`   | `string` | name is the metadata.name of the referenced config map |

## .spec.oidcProviders\[\].oidcClients

Description
oidcClients is an optional field that configures how on-cluster, platform clients should request tokens from the identity provider. oidcClients must not exceed 20 entries and entries must have unique namespace/name pairs.

Type
`array`

## .spec.oidcProviders\[\].oidcClients\[\]

Description
OIDCClientConfig configures how platform clients interact with identity providers as an authentication method.

Type
`object`

Required
- `clientID`

- `componentName`

- `componentNamespace`

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
<td style="text-align: left;"><p><code>clientID</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>clientID is a required field that configures the client identifier, from the identity provider, that the platform component uses for authentication requests made to the identity provider. The identity provider must accept this identifier for platform components to be able to use the identity provider as an authentication mode.</p>
<p>clientID must not be an empty string ("").</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>clientSecret</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>clientSecret is an optional field that configures the client secret used by the platform component when making authentication requests to the identity provider.</p>
<p>When not specified, no client secret will be used when making authentication requests to the identity provider.</p>
<p>When specified, clientSecret references a Secret in the 'openshift-config' namespace that contains the client secret in the 'clientSecret' key of the '.data' field.</p>
<p>The client secret will be used when making authentication requests to the identity provider.</p>
<p>Public clients do not require a client secret but private clients do require a client secret to work with the identity provider.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>componentName</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>componentName is a required field that specifies the name of the platform component being configured to use the identity provider as an authentication mode.</p>
<p>It is used in combination with componentNamespace as a unique identifier.</p>
<p>componentName must not be an empty string ("") and must not exceed 256 characters in length.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>componentNamespace</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>componentNamespace is a required field that specifies the namespace in which the platform component being configured to use the identity provider as an authentication mode is running.</p>
<p>It is used in combination with componentName as a unique identifier.</p>
<p>componentNamespace must not be an empty string ("") and must not exceed 63 characters in length.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>extraScopes</code></p></td>
<td style="text-align: left;"><p><code>array (string)</code></p></td>
<td style="text-align: left;"><p>extraScopes is an optional field that configures the extra scopes that should be requested by the platform component when making authentication requests to the identity provider. This is useful if you have configured claim mappings that requires specific scopes to be requested beyond the standard OIDC scopes.</p>
<p>When omitted, no additional scopes are requested.</p></td>
</tr>
</tbody>
</table>

## .spec.oidcProviders\[\].oidcClients\[\].clientSecret

Description
clientSecret is an optional field that configures the client secret used by the platform component when making authentication requests to the identity provider.

When not specified, no client secret will be used when making authentication requests to the identity provider.

When specified, clientSecret references a Secret in the 'openshift-config' namespace that contains the client secret in the 'clientSecret' key of the '.data' field.

The client secret will be used when making authentication requests to the identity provider.

Public clients do not require a client secret but private clients do require a client secret to work with the identity provider.

Type
`object`

Required
- `name`

| Property | Type     | Description                                        |
|----------|----------|----------------------------------------------------|
| `name`   | `string` | name is the metadata.name of the referenced secret |

## .spec.webhookTokenAuthenticator

Description
webhookTokenAuthenticator configures a remote token reviewer. These remote authentication webhooks can be used to verify bearer tokens via the tokenreviews.authentication.k8s.io REST API. This is required to honor bearer tokens that are provisioned by an external authentication service.

Can only be set if "Type" is set to "None".

Type
`object`

Required
- `kubeConfig`

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
<td style="text-align: left;"><p><code>kubeConfig</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>kubeConfig references a secret that contains kube config file data which describes how to access the remote webhook service. The namespace for the referenced secret is openshift-config.</p>
<p>For further details, see:</p>
<p><a href="https://kubernetes.io/docs/reference/access-authn-authz/authentication/#webhook-token-authentication">https://kubernetes.io/docs/reference/access-authn-authz/authentication/#webhook-token-authentication</a></p>
<p>The key "kubeConfig" is used to locate the data. If the secret or expected key is not found, the webhook is not honored. If the specified kube config data is not valid, the webhook is not honored.</p></td>
</tr>
</tbody>
</table>

## .spec.webhookTokenAuthenticator.kubeConfig

Description
kubeConfig references a secret that contains kube config file data which describes how to access the remote webhook service. The namespace for the referenced secret is openshift-config.

For further details, see:

<https://kubernetes.io/docs/reference/access-authn-authz/authentication/#webhook-token-authentication>

The key "kubeConfig" is used to locate the data. If the secret or expected key is not found, the webhook is not honored. If the specified kube config data is not valid, the webhook is not honored.

Type
`object`

Required
- `name`

| Property | Type     | Description                                        |
|----------|----------|----------------------------------------------------|
| `name`   | `string` | name is the metadata.name of the referenced secret |

## .spec.webhookTokenAuthenticators

Description
webhookTokenAuthenticators is DEPRECATED, setting it has no effect.

Type
`array`

## .spec.webhookTokenAuthenticators\[\]

Description
deprecatedWebhookTokenAuthenticator holds the necessary configuration options for a remote token authenticator. It’s the same as WebhookTokenAuthenticator but it’s missing the 'required' validation on KubeConfig field.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `kubeConfig` | `object` | kubeConfig contains kube config file data which describes how to access the remote webhook service. For further details, see: <https://kubernetes.io/docs/reference/access-authn-authz/authentication/#webhook-token-authentication> The key "kubeConfig" is used to locate the data. If the secret or expected key is not found, the webhook is not honored. If the specified kube config data is not valid, the webhook is not honored. The namespace for this secret is determined by the point of use. |

## .spec.webhookTokenAuthenticators\[\].kubeConfig

Description
kubeConfig contains kube config file data which describes how to access the remote webhook service. For further details, see: <https://kubernetes.io/docs/reference/access-authn-authz/authentication/#webhook-token-authentication> The key "kubeConfig" is used to locate the data. If the secret or expected key is not found, the webhook is not honored. If the specified kube config data is not valid, the webhook is not honored. The namespace for this secret is determined by the point of use.

Type
`object`

Required
- `name`

| Property | Type     | Description                                        |
|----------|----------|----------------------------------------------------|
| `name`   | `string` | name is the metadata.name of the referenced secret |

## .status

Description
status holds observed values from the cluster. They may not be overridden.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `integratedOAuthMetadata` | `object` | integratedOAuthMetadata contains the discovery endpoint data for OAuth 2.0 Authorization Server Metadata for the in-cluster integrated OAuth server. This discovery document can be viewed from its served location: oc get --raw '/.well-known/oauth-authorization-server' For further details, see the IETF Draft: <https://tools.ietf.org/html/draft-ietf-oauth-discovery-04#section-2> This contains the observed value based on cluster state. An explicitly set value in spec.oauthMetadata has precedence over this field. This field has no meaning if authentication spec.type is not set to IntegratedOAuth. The key "oauthMetadata" is used to locate the data. If the config map or expected key is not found, no metadata is served. If the specified metadata is not valid, no metadata is served. The namespace for this config map is openshift-config-managed. |
| `oidcClients` | `array` | oidcClients is where participating operators place the current OIDC client status for OIDC clients that can be customized by the cluster-admin. |
| `oidcClients[]` | `object` | OIDCClientStatus represents the current state of platform components and how they interact with the configured identity providers. |

## .status.integratedOAuthMetadata

Description
integratedOAuthMetadata contains the discovery endpoint data for OAuth 2.0 Authorization Server Metadata for the in-cluster integrated OAuth server. This discovery document can be viewed from its served location: oc get --raw '/.well-known/oauth-authorization-server' For further details, see the IETF Draft: <https://tools.ietf.org/html/draft-ietf-oauth-discovery-04#section-2> This contains the observed value based on cluster state. An explicitly set value in spec.oauthMetadata has precedence over this field. This field has no meaning if authentication spec.type is not set to IntegratedOAuth. The key "oauthMetadata" is used to locate the data. If the config map or expected key is not found, no metadata is served. If the specified metadata is not valid, no metadata is served. The namespace for this config map is openshift-config-managed.

Type
`object`

Required
- `name`

| Property | Type     | Description                                            |
|----------|----------|--------------------------------------------------------|
| `name`   | `string` | name is the metadata.name of the referenced config map |

## .status.oidcClients

Description
oidcClients is where participating operators place the current OIDC client status for OIDC clients that can be customized by the cluster-admin.

Type
`array`

## .status.oidcClients\[\]

Description
OIDCClientStatus represents the current state of platform components and how they interact with the configured identity providers.

Type
`object`

Required
- `componentName`

- `componentNamespace`

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
<td style="text-align: left;"><p><code>componentName</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>componentName is a required field that specifies the name of the platform component using the identity provider as an authentication mode. It is used in combination with componentNamespace as a unique identifier.</p>
<p>componentName must not be an empty string ("") and must not exceed 256 characters in length.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>componentNamespace</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>componentNamespace is a required field that specifies the namespace in which the platform component using the identity provider as an authentication mode is running.</p>
<p>It is used in combination with componentName as a unique identifier.</p>
<p>componentNamespace must not be an empty string ("") and must not exceed 63 characters in length.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>conditions</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>conditions are used to communicate the state of the <code>oidcClients</code> entry.</p>
<p>Supported conditions include Available, Degraded and Progressing.</p>
<p>If Available is true, the component is successfully using the configured client. If Degraded is true, that means something has gone wrong trying to handle the client configuration. If Progressing is true, that means the component is taking some action related to the <code>oidcClients</code> entry.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>conditions[]</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>Condition contains details for one aspect of the current state of this API Resource.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>consumingUsers</code></p></td>
<td style="text-align: left;"><p><code>array (string)</code></p></td>
<td style="text-align: left;"><p>consumingUsers is an optional list of ServiceAccounts requiring read permissions on the <code>clientSecret</code> secret.</p>
<p>consumingUsers must not exceed 5 entries.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>currentOIDCClients</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>currentOIDCClients is an optional list of clients that the component is currently using.</p>
<p>Entries must have unique issuerURL/clientID pairs.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>currentOIDCClients[]</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>OIDCClientReference is a reference to a platform component client configuration.</p></td>
</tr>
</tbody>
</table>

## .status.oidcClients\[\].conditions

Description
conditions are used to communicate the state of the `oidcClients` entry.

Supported conditions include Available, Degraded and Progressing.

If Available is true, the component is successfully using the configured client. If Degraded is true, that means something has gone wrong trying to handle the client configuration. If Progressing is true, that means the component is taking some action related to the `oidcClients` entry.

Type
`array`

## .status.oidcClients\[\].conditions\[\]

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

## .status.oidcClients\[\].currentOIDCClients

Description
currentOIDCClients is an optional list of clients that the component is currently using.

Entries must have unique issuerURL/clientID pairs.

Type
`array`

## .status.oidcClients\[\].currentOIDCClients\[\]

Description
OIDCClientReference is a reference to a platform component client configuration.

Type
`object`

Required
- `clientID`

- `issuerURL`

- `oidcProviderName`

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
<td style="text-align: left;"><p><code>clientID</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>clientID is a required field that specifies the client identifier, from the identity provider, that the platform component is using for authentication requests made to the identity provider.</p>
<p>clientID must not be empty.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>issuerURL</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>issuerURL is a required field that specifies the URL of the identity provider that this client is configured to make requests against.</p>
<p>issuerURL must use the 'https' scheme.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>oidcProviderName</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>oidcProviderName is a required reference to the 'name' of the identity provider configured in 'oidcProviders' that this client is associated with.</p>
<p>oidcProviderName must not be an empty string ("").</p></td>
</tr>
</tbody>
</table>

# API endpoints

The following API endpoints are available:

- `/apis/config.openshift.io/v1/authentications`

  - `DELETE`: delete collection of Authentication

  - `GET`: list objects of kind Authentication

  - `POST`: create an Authentication

- `/apis/config.openshift.io/v1/authentications/{name}`

  - `DELETE`: delete an Authentication

  - `GET`: read the specified Authentication

  - `PATCH`: partially update the specified Authentication

  - `PUT`: replace the specified Authentication

- `/apis/config.openshift.io/v1/authentications/{name}/status`

  - `GET`: read status of the specified Authentication

  - `PATCH`: partially update status of the specified Authentication

  - `PUT`: replace status of the specified Authentication

## /apis/config.openshift.io/v1/authentications

HTTP method
`DELETE`

Description
delete collection of Authentication

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Status`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`GET`

Description
list objects of kind Authentication

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`AuthenticationList`](../objects/index.md#io-openshift-config-v1-AuthenticationList) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`POST`

Description
create an Authentication

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`Authentication`](authentication-config-openshift-io-v1.md#authentication-config-openshift-io-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Authentication`](authentication-config-openshift-io-v1.md#authentication-config-openshift-io-v1) schema |
| 201 - Created | [`Authentication`](authentication-config-openshift-io-v1.md#authentication-config-openshift-io-v1) schema |
| 202 - Accepted | [`Authentication`](authentication-config-openshift-io-v1.md#authentication-config-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/config.openshift.io/v1/authentications/{name}

| Parameter | Type     | Description                |
|-----------|----------|----------------------------|
| `name`    | `string` | name of the Authentication |

Global path parameters

HTTP method
`DELETE`

Description
delete an Authentication

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
read the specified Authentication

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Authentication`](authentication-config-openshift-io-v1.md#authentication-config-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PATCH`

Description
partially update the specified Authentication

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Authentication`](authentication-config-openshift-io-v1.md#authentication-config-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PUT`

Description
replace the specified Authentication

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`Authentication`](authentication-config-openshift-io-v1.md#authentication-config-openshift-io-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Authentication`](authentication-config-openshift-io-v1.md#authentication-config-openshift-io-v1) schema |
| 201 - Created | [`Authentication`](authentication-config-openshift-io-v1.md#authentication-config-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/config.openshift.io/v1/authentications/{name}/status

| Parameter | Type     | Description                |
|-----------|----------|----------------------------|
| `name`    | `string` | name of the Authentication |

Global path parameters

HTTP method
`GET`

Description
read status of the specified Authentication

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Authentication`](authentication-config-openshift-io-v1.md#authentication-config-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PATCH`

Description
partially update status of the specified Authentication

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Authentication`](authentication-config-openshift-io-v1.md#authentication-config-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PUT`

Description
replace status of the specified Authentication

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`Authentication`](authentication-config-openshift-io-v1.md#authentication-config-openshift-io-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Authentication`](authentication-config-openshift-io-v1.md#authentication-config-openshift-io-v1) schema |
| 201 - Created | [`Authentication`](authentication-config-openshift-io-v1.md#authentication-config-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses
