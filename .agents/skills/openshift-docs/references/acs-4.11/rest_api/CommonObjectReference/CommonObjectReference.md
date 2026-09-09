<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

<a id="models_CommonObjectReference"></a>

# Common object reference

<a id="_models"></a>

# Models

<a id="AdministrationEventResource_CommonObjectReference"></a>

## AdministrationEventResource

Resource holds all information about the resource associated with the event.

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| type |  |  | String | Resource type associated with the event. An event may refer to an underlying resource such as a particular image. In that case, the resource type will be filled here. |  |
| id |  |  | String | Resource ID associated with the event. If an event refers to an underlying resource, the resource ID identifies the underlying resource. The resource ID is not guaranteed to be set, depending on the context of the administration event. |  |
| name |  |  | String | Resource name associated with the event. If an event refers to an underlying resource, the resource name identifies the underlying resource. The resource name is not guaranteed to be set, depending on the context of the administration event. |  |

<a id="AlertDeploymentContainer_CommonObjectReference"></a>

## AlertDeploymentContainer

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| image |  |  | [StorageContainerImage](#StorageContainerImage_CommonObjectReference) |  |  |
| name |  |  | String |  |  |

<a id="AlertEnforcement_CommonObjectReference"></a>

## AlertEnforcement

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| action |  |  | [StorageEnforcementAction](#StorageEnforcementAction_CommonObjectReference) |  | UNSET_ENFORCEMENT, SCALE_TO_ZERO_ENFORCEMENT, UNSATISFIABLE_NODE_CONSTRAINT_ENFORCEMENT, KILL_POD_ENFORCEMENT, FAIL_BUILD_ENFORCEMENT, FAIL_KUBE_REQUEST_ENFORCEMENT, FAIL_DEPLOYMENT_CREATE_ENFORCEMENT, FAIL_DEPLOYMENT_UPDATE_ENFORCEMENT, |
| message |  |  | String |  |  |

<a id="AlertEntityType_CommonObjectReference"></a>

## AlertEntityType

| Enum Values     |
|-----------------|
| UNSET           |
| DEPLOYMENT      |
| CONTAINER_IMAGE |
| RESOURCE        |
| NODE            |

<a id="AlertGroupAlertCounts_CommonObjectReference"></a>

## AlertGroupAlertCounts

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| severity |  |  | [StorageSeverity](#StorageSeverity_CommonObjectReference) |  | UNSET_SEVERITY, LOW_SEVERITY, MEDIUM_SEVERITY, HIGH_SEVERITY, CRITICAL_SEVERITY, |
| count |  |  | String |  | int64 |

<a id="AlertNode_CommonObjectReference"></a>

## AlertNode

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| id |  |  | String |  |  |
| name |  |  | String |  |  |
| clusterId |  |  | String | This field has to be duplicated in Alert for scope management and search. |  |
| clusterName |  |  | String | This field has to be duplicated in Alert for scope management and search. |  |

<a id="AlertProcessViolation_CommonObjectReference"></a>

## AlertProcessViolation

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| message |  |  | String |  |  |
| processes |  |  | List of [StorageProcessIndicator](#StorageProcessIndicator_CommonObjectReference) |  |  |

<a id="AlertResourceResourceType_CommonObjectReference"></a>

## AlertResourceResourceType

| Enum Values                  |
|------------------------------|
| UNKNOWN                      |
| SECRETS                      |
| CONFIGMAPS                   |
| CLUSTER_ROLES                |
| CLUSTER_ROLE_BINDINGS        |
| NETWORK_POLICIES             |
| SECURITY_CONTEXT_CONSTRAINTS |
| EGRESS_FIREWALLS             |

<a id="AlertServiceResolveAlertBody_CommonObjectReference"></a>

## AlertServiceResolveAlertBody

| Field Name    | Required | Nullable | Type    | Description | Format |
|---------------|----------|----------|---------|-------------|--------|
| whitelist     |          |          | Boolean |             |        |
| addToBaseline |          |          | Boolean |             |        |

<a id="AlertViolation_CommonObjectReference"></a>

## AlertViolation

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| message |  |  | String |  |  |
| keyValueAttrs |  |  | [ViolationKeyValueAttrs](#ViolationKeyValueAttrs_CommonObjectReference) |  |  |
| networkFlowInfo |  |  | [ViolationNetworkFlowInfo](#ViolationNetworkFlowInfo_CommonObjectReference) |  |  |
| fileAccess |  |  | [StorageFileAccess](#StorageFileAccess_CommonObjectReference) |  |  |
| type |  |  | [AlertViolationType](#AlertViolationType_CommonObjectReference) |  | GENERIC, K8S_EVENT, NETWORK_FLOW, NETWORK_POLICY, FILE_ACCESS, |
| time |  |  | Date | Indicates violation time. This field differs from top-level field 'time' which represents last time the alert occurred in case of multiple occurrences of the policy alert. As of 55.0, this field is set only for kubernetes event violations, but may not be limited to it in future. | date-time |

<a id="AlertViolationType_CommonObjectReference"></a>

## AlertViolationType

| Enum Values    |
|----------------|
| GENERIC        |
| K8S_EVENT      |
| NETWORK_FLOW   |
| NETWORK_POLICY |
| FILE_ACCESS    |

<a id="AuthMachineToMachineConfigMapping_CommonObjectReference"></a>

## AuthMachineToMachineConfigMapping

Mappings map an identity token’s claim values to a specific role within Central.

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| key |  |  | String | A key within the identity token’s claim value to use. |  |
| valueExpression |  |  | String | A regular expression that will be evaluated against values of the identity token claim identified by the specified key. This regular expressions is in RE2 format, see more here: <https://github.com/google/re2/wiki/Syntax>. |  |
| role |  |  | String | The role which should be issued when the key and value match for a particular identity token. |  |

<a id="AuthProviderRequiredAttribute_CommonObjectReference"></a>

## AuthProviderRequiredAttribute

RequiredAttribute allows to specify a set of attributes which ALL are required to be returned by the auth provider. If any attribute is missing within the external claims of the token issued by Central, the authentication request to this IdP is considered failed.

| Field Name     | Required | Nullable | Type   | Description | Format |
|----------------|----------|----------|--------|-------------|--------|
| attributeKey   |          |          | String |             |        |
| attributeValue |          |          | String |             |        |

<a id="AuthProviderServicePutAuthProviderBody_CommonObjectReference"></a>

## AuthProviderServicePutAuthProviderBody

Next Tag: 15.

<table id="Fields-AuthProviderServicePutAuthProviderBody_CommonObjectReference">
<colgroup>
<col style="width: 18%" />
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 18%" />
<col style="width: 36%" />
<col style="width: 9%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Field Name</th>
<th style="text-align: left;">Required</th>
<th style="text-align: left;">Nullable</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Description</th>
<th style="text-align: left;">Format</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>name</p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><p>String</p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><p>type</p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><p>String</p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><p>uiEndpoint</p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><p>String</p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><p>enabled</p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><p>Boolean</p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><p>config</p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><p>Map of <code>string</code></p></td>
<td style="text-align: left;"><p>Config holds auth provider specific configuration. Each configuration options are different based on the given auth provider type.</p>
<p>OIDC:</p>
<ul>
<li><p>"issuer": the OIDC issuer according to <a href="https://openid.net/specs/openid-connect-core-1_0.html#IssuerIdentifier">https://openid.net/specs/openid-connect-core-1_0.html#IssuerIdentifier</a>.</p></li>
<li><p>"client_id": the client ID according to <a href="https://www.rfc-editor.org/rfc/rfc6749.html#section-2.2">https://www.rfc-editor.org/rfc/rfc6749.html#section-2.2</a>.</p></li>
<li><p>"client_secret": the client secret according to <a href="https://www.rfc-editor.org/rfc/rfc6749.html#section-2.3.1">https://www.rfc-editor.org/rfc/rfc6749.html#section-2.3.1</a>.</p></li>
<li><p>"do_not_use_client_secret": set to "true" if you want to create a configuration with only a client ID and no client secret.</p></li>
<li><p>"mode": the OIDC callback mode, choosing from "fragment", "post", or "query".</p></li>
<li><p>"disable_offline_access_scope": set to "true" if no offline tokens shall be issued.</p></li>
<li><p>"extra_scopes": a space-delimited string of additional scopes to request in addition to "openid profile email" according to <a href="https://www.rfc-editor.org/rfc/rfc6749.html#section-3.3">https://www.rfc-editor.org/rfc/rfc6749.html#section-3.3</a>.</p></li>
</ul>
<p>OpenShift Auth: supports no extra configuration options.</p>
<p>User PKI:</p>
<ul>
<li><p>"keys": the trusted certificates PEM encoded.</p></li>
</ul>
<p>SAML:</p>
<ul>
<li><p>"sp_issuer": the service provider issuer according to <a href="https://datatracker.ietf.org/doc/html/rfc7522#section-3">https://datatracker.ietf.org/doc/html/rfc7522#section-3</a>.</p></li>
<li><p>"idp_metadata_url": the metadata URL according to <a href="https://docs.oasis-open.org/security/saml/v2.0/saml-metadata-2.0-os.pdf">https://docs.oasis-open.org/security/saml/v2.0/saml-metadata-2.0-os.pdf</a>.</p></li>
<li><p>"idp_issuer": the IdP issuer.</p></li>
<li><p>"idp_cert_pem": the cert PEM encoded for the IdP endpoint.</p></li>
<li><p>"idp_sso_url": the IdP SSO URL.</p></li>
<li><p>"idp_nameid_format": the IdP name ID format.</p></li>
</ul>
<p>IAP:</p>
<ul>
<li><p>"audience": the audience to use.</p></li>
</ul></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><p>loginUrl</p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><p>String</p></td>
<td style="text-align: left;"><p>The login URL will be provided by the backend, and may not be specified in a request.</p></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><p>validated</p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><p>Boolean</p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><p>extraUiEndpoints</p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><p>List of <code>string</code></p></td>
<td style="text-align: left;"><p>UI endpoints which to allow in addition to <code>ui_endpoint</code>. I.e., if a login request is coming from any of these, the auth request will use these for the callback URL, not ui_endpoint.</p></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><p>active</p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><p>Boolean</p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><p>requiredAttributes</p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><p>List of <a href="#AuthProviderRequiredAttribute_CommonObjectReference">AuthProviderRequiredAttribute</a></p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><p>traits</p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><p><a href="#StorageTraits_CommonObjectReference">StorageTraits</a></p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><p>claimMappings</p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><p>Map of <code>string</code></p></td>
<td style="text-align: left;"><p>Specifies claims from IdP token that will be copied to Rox token attributes. Each key in this map contains a path in IdP token we want to map. Path is separated by "." symbol.</p>
<p>For example, if IdP token payload looks like:</p>
<div class="sourceCode" id="cb1"><pre class="sourceCode json"><code class="sourceCode json"><span id="cb1-1"><a data-unavailable-reference="true" aria-hidden="true" tabindex="-1"></a><span class="fu">{</span></span>
<span id="cb1-2"><a data-unavailable-reference="true" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;a&quot;</span><span class="fu">:</span> <span class="fu">{</span></span>
<span id="cb1-3"><a data-unavailable-reference="true" aria-hidden="true" tabindex="-1"></a>        <span class="dt">&quot;b&quot;</span> <span class="fu">:</span> <span class="st">&quot;c&quot;</span><span class="fu">,</span></span>
<span id="cb1-4"><a data-unavailable-reference="true" aria-hidden="true" tabindex="-1"></a>        <span class="dt">&quot;d&quot;</span><span class="fu">:</span> <span class="kw">true</span><span class="fu">,</span></span>
<span id="cb1-5"><a data-unavailable-reference="true" aria-hidden="true" tabindex="-1"></a>        <span class="dt">&quot;e&quot;</span><span class="fu">:</span> <span class="ot">[</span> <span class="st">&quot;val1&quot;</span><span class="ot">,</span> <span class="st">&quot;val2&quot;</span><span class="ot">,</span> <span class="st">&quot;val3&quot;</span> <span class="ot">]</span><span class="fu">,</span></span>
<span id="cb1-6"><a data-unavailable-reference="true" aria-hidden="true" tabindex="-1"></a>        <span class="dt">&quot;f&quot;</span><span class="fu">:</span> <span class="ot">[</span> <span class="kw">true</span><span class="ot">,</span> <span class="kw">false</span><span class="ot">,</span> <span class="kw">false</span> <span class="ot">]</span><span class="fu">,</span></span>
<span id="cb1-7"><a data-unavailable-reference="true" aria-hidden="true" tabindex="-1"></a>        <span class="dt">&quot;g&quot;</span><span class="fu">:</span> <span class="fl">123.0</span><span class="fu">,</span></span>
<span id="cb1-8"><a data-unavailable-reference="true" aria-hidden="true" tabindex="-1"></a>        <span class="dt">&quot;h&quot;</span><span class="fu">:</span> <span class="ot">[</span> <span class="dv">1</span><span class="ot">,</span> <span class="dv">2</span><span class="ot">,</span> <span class="dv">3</span><span class="ot">]</span></span>
<span id="cb1-9"><a data-unavailable-reference="true" aria-hidden="true" tabindex="-1"></a>    <span class="fu">}</span></span>
<span id="cb1-10"><a data-unavailable-reference="true" aria-hidden="true" tabindex="-1"></a><span class="fu">}</span></span></code></pre></div>
<p>then "a.b" would be a valid key and "a.z" is not.</p>
<p>We support the following types of claims:</p>
<ul>
<li><p>string(path "a.b")</p></li>
<li><p>bool(path "a.d")</p></li>
<li><p>string array(path "a.e")</p></li>
<li><p>bool array (path "a.f.")</p></li>
</ul>
<p>We do NOT support the following types of claims:</p>
<ul>
<li><p>complex claims(path "a")</p></li>
<li><p>float/integer claims(path "a.g")</p></li>
<li><p>float/integer array claims(path "a.h")</p></li>
</ul>
<p>Each value in this map contains a Rox token attribute name we want to add claim to. If, for example, value is "groups", claim would be found in "external_user.Attributes.groups" in token.</p>
<p>Note: we only support this feature for OIDC auth provider.</p></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><p>lastUpdated</p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><p>Date</p></td>
<td style="text-align: left;"><p>Last updated indicates the last time the auth provider has been updated. In case there have been tokens issued by an auth provider <em>before</em> this timestamp, they will be considered invalid. Subsequently, all clients will have to re-issue their tokens (either by refreshing or by an additional login attempt).</p></td>
<td style="text-align: left;"><p>date-time</p></td>
</tr>
</tbody>
</table>

<a id="AuthProviderServiceUpdateAuthProviderBody_CommonObjectReference"></a>

## AuthProviderServiceUpdateAuthProviderBody

| Field Name | Required | Nullable | Type    | Description | Format |
|------------|----------|----------|---------|-------------|--------|
| name       |          |          | String  |             |        |
| enabled    |          |          | Boolean |             |        |

<a id="AuthServiceUpdateAuthMachineToMachineConfigBody_CommonObjectReference"></a>

## AuthServiceUpdateAuthMachineToMachineConfigBody

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| config |  |  | [AuthServiceUpdateAuthMachineToMachineConfigBody](#AuthServiceUpdateAuthMachineToMachineConfigBody_CommonObjectReference) |  |  |

<a id="AuthServiceUpdateAuthMachineToMachineConfigBodyConfig_CommonObjectReference"></a>

## AuthServiceUpdateAuthMachineToMachineConfigBodyConfig

AuthMachineToMachineConfig determines rules for exchanging an identity token from a third party with a Central access token. The M2M stands for machine to machine, as this is the intended use-case for the config.

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| type |  |  | [V1AuthMachineToMachineConfigType](#V1AuthMachineToMachineConfigType_CommonObjectReference) |  | GENERIC, GITHUB_ACTIONS, KUBE_SERVICE_ACCOUNT, |
| tokenExpirationDuration |  |  | String | Sets the expiration of the token returned from the ExchangeAuthMachineToMachineToken API call. Possible valid time units are: s, m, h. The maximum allowed expiration duration is 24h. As an example: 2h45m. For additional information on the validation of the duration, see: <https://pkg.go.dev/time#ParseDuration>. |  |
| mappings |  |  | List of [AuthMachineToMachineConfigMapping](#AuthMachineToMachineConfigMapping_CommonObjectReference) | At least one mapping is required to resolve to a valid role for the access token to be successfully generated. |  |
| issuer |  |  | String | The issuer of the related OIDC provider issuing the ID tokens to exchange. Must be non-empty string containing URL when type is GENERIC. In case of GitHub actions, this must be empty or set to <https://token.actions.githubusercontent.com>. Issuer is a unique key, therefore there may be at most one GITHUB_ACTIONS config, and each GENERIC config must have a distinct issuer. |  |
| traits |  |  | [V1Traits](#V1Traits_CommonObjectReference) |  |  |

<a id="AuthorizationTraceResponseResponseStatus_CommonObjectReference"></a>

## AuthorizationTraceResponseResponseStatus

| Enum Values    |
|----------------|
| UNKNOWN_STATUS |
| SUCCESS        |
| FAILURE        |

<a id="AuthorizationTraceResponseTrace_CommonObjectReference"></a>

## AuthorizationTraceResponseTrace

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| scopeCheckerType |  |  | String |  |  |
| builtIn |  |  | [TraceBuiltInAuthorizer](#TraceBuiltInAuthorizer_CommonObjectReference) |  |  |

<a id="AuthorizationTraceResponseUser_CommonObjectReference"></a>

## AuthorizationTraceResponseUser

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| username |  |  | String |  |  |
| friendlyName |  |  | String |  |  |
| aggregatedPermissions |  |  | Map of [StorageAccess](#StorageAccess_CommonObjectReference) |  |  |
| roles |  |  | List of [UserRole](#UserRole_CommonObjectReference) |  |  |

<a id="AvailableProviderTypesResponseAuthProviderType_CommonObjectReference"></a>

## AvailableProviderTypesResponseAuthProviderType

| Field Name          | Required | Nullable | Type             | Description | Format |
|---------------------|----------|----------|------------------|-------------|--------|
| type                |          |          | String           |             |        |
| suggestedAttributes |          |          | List of `string` |             |        |

<a id="BannerConfigSize_CommonObjectReference"></a>

## BannerConfigSize

| Enum Values |
|-------------|
| UNSET       |
| SMALL       |
| MEDIUM      |
| LARGE       |

<a id="BaseImageServiceV2UpdateBaseImageTagPatternBody_CommonObjectReference"></a>

## BaseImageServiceV2UpdateBaseImageTagPatternBody

| Field Name          | Required | Nullable | Type   | Description | Format |
|---------------------|----------|----------|--------|-------------|--------|
| baseImageTagPattern |          |          | String |             |        |

<a id="CRSRevokeResponseCRSRevocationError_CommonObjectReference"></a>

## CRSRevokeResponseCRSRevocationError

| Field Name | Required | Nullable | Type   | Description | Format |
|------------|----------|----------|--------|-------------|--------|
| id         |          |          | String |             |        |
| error      |          |          | String |             |        |

<a id="CVEInfoReference_CommonObjectReference"></a>

## CVEInfoReference

| Field Name | Required | Nullable | Type             | Description | Format |
|------------|----------|----------|------------------|-------------|--------|
| URI        |          |          | String           |             |        |
| tags       |          |          | List of `string` |             |        |

<a id="CVSSV2AccessComplexity_CommonObjectReference"></a>

## CVSSV2AccessComplexity

| Enum Values   |
|---------------|
| ACCESS_HIGH   |
| ACCESS_MEDIUM |
| ACCESS_LOW    |

<a id="CVSSV2Authentication_CommonObjectReference"></a>

## CVSSV2Authentication

| Enum Values   |
|---------------|
| AUTH_MULTIPLE |
| AUTH_SINGLE   |
| AUTH_NONE     |

<a id="CVSSV3AttackVector_CommonObjectReference"></a>

## CVSSV3AttackVector

| Enum Values     |
|-----------------|
| ATTACK_LOCAL    |
| ATTACK_ADJACENT |
| ATTACK_NETWORK  |
| ATTACK_PHYSICAL |

<a id="CVSSV3Complexity_CommonObjectReference"></a>

## CVSSV3Complexity

| Enum Values     |
|-----------------|
| COMPLEXITY_LOW  |
| COMPLEXITY_HIGH |

<a id="CVSSV3Impact_CommonObjectReference"></a>

## CVSSV3Impact

| Enum Values |
|-------------|
| IMPACT_NONE |
| IMPACT_LOW  |
| IMPACT_HIGH |

<a id="CVSSV3Privileges_CommonObjectReference"></a>

## CVSSV3Privileges

| Enum Values    |
|----------------|
| PRIVILEGE_NONE |
| PRIVILEGE_LOW  |
| PRIVILEGE_HIGH |

<a id="CVSSV3Severity_CommonObjectReference"></a>

## CVSSV3Severity

| Enum Values |
|-------------|
| UNKNOWN     |
| NONE        |
| LOW         |
| MEDIUM      |
| HIGH        |
| CRITICAL    |

<a id="CVSSV3UserInteraction_CommonObjectReference"></a>

## CVSSV3UserInteraction

| Enum Values |
|-------------|
| UI_NONE     |
| UI_REQUIRED |

<a id="CentralServicesCapabilitiesCapabilityStatus_CommonObjectReference"></a>

## CentralServicesCapabilitiesCapabilityStatus

- CapabilityAvailable: CapabilityAvailable means that UI and APIs should be available for users to use. This does not automatically mean that the functionality is 100% available and any calls to APIs will result in successful execution. Rather it means that users should be allowed to leverage the functionality as opposed to CapabilityDisabled when functionality should be blocked.

- CapabilityDisabled: CapabilityDisabled means the corresponding UI should be disabled and attempts to use related APIs should lead to errors.

| Enum Values         |
|---------------------|
| CapabilityAvailable |
| CapabilityDisabled  |

<a id="CentralTelemetryConfig_CommonObjectReference"></a>

## CentralTelemetryConfig

| Field Name   | Required | Nullable | Type   | Description | Format |
|--------------|----------|----------|--------|-------------|--------|
| userId       |          |          | String |             |        |
| endpoint     |          |          | String |             |        |
| storageKeyV1 |          |          | String |             |        |

<a id="CloudSourceCredentials_CommonObjectReference"></a>

## CloudSourceCredentials

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| secret |  |  | String | Used for single-valued authentication via long-lived tokens. |  |
| clientId |  |  | String | Used for client authentication in combination with client_secret. |  |
| clientSecret |  |  | String | Used for client authentication in combination with client_id. |  |

<a id="CloudSourcesServiceUpdateCloudSourceBody_CommonObjectReference"></a>

## CloudSourcesServiceUpdateCloudSourceBody

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| cloudSource |  |  | [CloudSourcesServiceUpdateCloudSourceBody](#CloudSourcesServiceUpdateCloudSourceBody_CommonObjectReference) |  |  |
| updateCredentials |  |  | Boolean | If true, cloud_source must include valid credentials. If false, the resource must already exist and credentials in cloud_source are ignored. |  |

<a id="CloudSourcesServiceUpdateCloudSourceBodyCloudSource_CommonObjectReference"></a>

## CloudSourcesServiceUpdateCloudSourceBodyCloudSource

CloudSource is an integration which provides a source for discovered clusters.

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| name |  |  | String |  |  |
| type |  |  | [V1CloudSourceType](#V1CloudSourceType_CommonObjectReference) |  | TYPE_UNSPECIFIED, TYPE_PALADIN_CLOUD, TYPE_OCM, |
| credentials |  |  | [CloudSourceCredentials](#CloudSourceCredentials_CommonObjectReference) |  |  |
| skipTestIntegration |  |  | Boolean |  |  |
| paladinCloud |  |  | [V1PaladinCloudConfig](#V1PaladinCloudConfig_CommonObjectReference) |  |  |
| ocm |  |  | [V1OCMConfig](#V1OCMConfig_CommonObjectReference) |  |  |

<a id="ClusterAlertsAlertEvents_CommonObjectReference"></a>

## ClusterAlertsAlertEvents

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| severity |  |  | [StorageSeverity](#StorageSeverity_CommonObjectReference) |  | UNSET_SEVERITY, LOW_SEVERITY, MEDIUM_SEVERITY, HIGH_SEVERITY, CRITICAL_SEVERITY, |
| events |  |  | List of [V1AlertEvent](#V1AlertEvent_CommonObjectReference) |  |  |

<a id="ClusterHealthStatusHealthStatusLabel_CommonObjectReference"></a>

## ClusterHealthStatusHealthStatusLabel

- UNAVAILABLE: Only collector can have unavailable status

| Enum Values   |
|---------------|
| UNINITIALIZED |
| UNAVAILABLE   |
| UNHEALTHY     |
| DEGRADED      |
| HEALTHY       |

<a id="ClusterScanStatusSuiteStatus_CommonObjectReference"></a>

## ClusterScanStatusSuiteStatus

Additional scan status gathered from ComplianceSuite

| Field Name         | Required | Nullable | Type   | Description | Format    |
|--------------------|----------|----------|--------|-------------|-----------|
| phase              |          |          | String |             |           |
| result             |          |          | String |             |           |
| errorMessage       |          |          | String |             |           |
| lastTransitionTime |          |          | Date   |             | date-time |

<a id="ClusterUpgradeStatusUpgradability_CommonObjectReference"></a>

## ClusterUpgradeStatusUpgradability

- SENSOR_VERSION_HIGHER: SENSOR_VERSION_HIGHER occurs when we detect that the sensor is running a newer version than this Central. This is unexpected, but can occur depending on the patches a customer does. In this case, we will NOT automatically "upgrade" the sensor, since that would be a downgrade, even if the autoupgrade setting is on. The user will be allowed to manually trigger the upgrade, but they are strongly discouraged from doing so without upgrading Central first, since this is an unsupported configuration.

| Enum Values             |
|-------------------------|
| UNSET                   |
| UP_TO_DATE              |
| MANUAL_UPGRADE_REQUIRED |
| AUTO_UPGRADE_POSSIBLE   |
| SENSOR_VERSION_HIGHER   |

<a id="ClusterUpgradeStatusUpgradeProcessStatus_CommonObjectReference"></a>

## ClusterUpgradeStatusUpgradeProcessStatus

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| active |  |  | Boolean |  |  |
| id |  |  | String |  |  |
| targetVersion |  |  | String |  |  |
| upgraderImage |  |  | String |  |  |
| initiatedAt |  |  | Date |  | date-time |
| progress |  |  | [StorageUpgradeProgress](#StorageUpgradeProgress_CommonObjectReference) |  |  |
| type |  |  | [UpgradeProcessStatusUpgradeProcessType](#UpgradeProcessStatusUpgradeProcessType_CommonObjectReference) |  | UPGRADE, CERT_ROTATION, |

<a id="ClustersServicePutClusterBody_CommonObjectReference"></a>

## ClustersServicePutClusterBody

Next tag: 33

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| name |  |  | String |  |  |
| type |  |  | [StorageClusterType](#StorageClusterType_CommonObjectReference) |  | GENERIC_CLUSTER, KUBERNETES_CLUSTER, OPENSHIFT_CLUSTER, OPENSHIFT4_CLUSTER, |
| labels |  |  | Map of `string` |  |  |
| mainImage |  |  | String |  |  |
| collectorImage |  |  | String |  |  |
| centralApiEndpoint |  |  | String |  |  |
| runtimeSupport |  |  | Boolean |  |  |
| collectionMethod |  |  | [StorageCollectionMethod](#StorageCollectionMethod_CommonObjectReference) |  | UNSET_COLLECTION, NO_COLLECTION, KERNEL_MODULE, EBPF, CORE_BPF, |
| admissionController |  |  | Boolean |  |  |
| admissionControllerUpdates |  |  | Boolean |  |  |
| admissionControllerEvents |  |  | Boolean |  |  |
| status |  |  | [StorageClusterStatus](#StorageClusterStatus_CommonObjectReference) |  |  |
| dynamicConfig |  |  | [StorageDynamicClusterConfig](#StorageDynamicClusterConfig_CommonObjectReference) |  |  |
| tolerationsConfig |  |  | [StorageTolerationsConfig](#StorageTolerationsConfig_CommonObjectReference) |  |  |
| priority |  |  | String |  | int64 |
| healthStatus |  |  | [StorageClusterHealthStatus](#StorageClusterHealthStatus_CommonObjectReference) |  |  |
| slimCollector |  |  | Boolean |  |  |
| helmConfig |  |  | [StorageCompleteClusterConfig](#StorageCompleteClusterConfig_CommonObjectReference) |  |  |
| mostRecentSensorId |  |  | [StorageSensorDeploymentIdentification](#StorageSensorDeploymentIdentification_CommonObjectReference) |  |  |
| auditLogState |  |  | Map of [StorageAuditLogFileState](#StorageAuditLogFileState_CommonObjectReference) | For internal use only. |  |
| initBundleId |  |  | String |  |  |
| managedBy |  |  | [StorageManagerType](#StorageManagerType_CommonObjectReference) |  | MANAGER_TYPE_UNKNOWN, MANAGER_TYPE_MANUAL, MANAGER_TYPE_HELM_CHART, MANAGER_TYPE_KUBERNETES_OPERATOR, |
| sensorCapabilities |  |  | List of `string` |  |  |
| admissionControllerFailOnError |  |  | Boolean |  |  |

<a id="CollectionServiceUpdateCollectionBody_CommonObjectReference"></a>

## CollectionServiceUpdateCollectionBody

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| name |  |  | String |  |  |
| description |  |  | String |  |  |
| resourceSelectors |  |  | List of [StorageResourceSelector](#StorageResourceSelector_CommonObjectReference) |  |  |
| embeddedCollectionIds |  |  | List of `string` |  |  |

<a id="ComplianceAggregationAggregationKey_CommonObjectReference"></a>

## ComplianceAggregationAggregationKey

Next available tag: 3

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| scope |  |  | [StorageComplianceAggregationScope](#StorageComplianceAggregationScope_CommonObjectReference) |  | UNKNOWN, STANDARD, CLUSTER, CATEGORY, CONTROL, NAMESPACE, NODE, DEPLOYMENT, CHECK, |
| id |  |  | String |  |  |

<a id="ComplianceAggregationResult_CommonObjectReference"></a>

## ComplianceAggregationResult

Next available tag: 5

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| aggregationKeys |  |  | List of [ComplianceAggregationAggregationKey](#ComplianceAggregationAggregationKey_CommonObjectReference) |  |  |
| unit |  |  | [StorageComplianceAggregationScope](#StorageComplianceAggregationScope_CommonObjectReference) |  | UNKNOWN, STANDARD, CLUSTER, CATEGORY, CONTROL, NAMESPACE, NODE, DEPLOYMENT, CHECK, |
| numPassing |  |  | Integer |  | int32 |
| numFailing |  |  | Integer |  | int32 |
| numSkipped |  |  | Integer |  | int32 |

<a id="ComplianceDomainCluster_CommonObjectReference"></a>

## ComplianceDomainCluster

These must mirror the tags *exactly* in cluster.proto for backwards compatibility

| Field Name | Required | Nullable | Type   | Description | Format |
|------------|----------|----------|--------|-------------|--------|
| id         |          |          | String |             |        |
| name       |          |          | String |             |        |

<a id="ComplianceDomainDeployment_CommonObjectReference"></a>

## ComplianceDomainDeployment

This must mirror the tags *exactly* in deployment.proto for backwards compatibility

| Field Name  | Required | Nullable | Type   | Description | Format |
|-------------|----------|----------|--------|-------------|--------|
| id          |          |          | String |             |        |
| name        |          |          | String |             |        |
| type        |          |          | String |             |        |
| namespace   |          |          | String |             |        |
| namespaceId |          |          | String |             |        |
| clusterId   |          |          | String |             |        |
| clusterName |          |          | String |             |        |

<a id="ComplianceDomainNode_CommonObjectReference"></a>

## ComplianceDomainNode

These must mirror the tags *exactly* in node.proto for backwards compatibility

| Field Name  | Required | Nullable | Type   | Description | Format |
|-------------|----------|----------|--------|-------------|--------|
| id          |          |          | String |             |        |
| name        |          |          | String |             |        |
| clusterId   |          |          | String |             |        |
| clusterName |          |          | String |             |        |

<a id="ComplianceResultValueEvidence_CommonObjectReference"></a>

## ComplianceResultValueEvidence

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| state |  |  | [StorageComplianceState](#StorageComplianceState_CommonObjectReference) |  | COMPLIANCE_STATE_UNKNOWN, COMPLIANCE_STATE_SKIP, COMPLIANCE_STATE_NOTE, COMPLIANCE_STATE_SUCCESS, COMPLIANCE_STATE_FAILURE, COMPLIANCE_STATE_ERROR, |
| message |  |  | String |  |  |
| messageId |  |  | Integer |  | int32 |

<a id="ComplianceRuleFix_CommonObjectReference"></a>

## ComplianceRuleFix

| Field Name | Required | Nullable | Type   | Description | Format |
|------------|----------|----------|--------|-------------|--------|
| platform   |          |          | String |             |        |
| disruption |          |          | String |             |        |

<a id="ComplianceRunResultsEntityResults_CommonObjectReference"></a>

## ComplianceRunResultsEntityResults

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| controlResults |  |  | Map of [StorageComplianceResultValue](#StorageComplianceResultValue_CommonObjectReference) |  |  |

<a id="ComplianceScanConfigurationServiceUpdateComplianceScanConfigurationBody_CommonObjectReference"></a>

## ComplianceScanConfigurationServiceUpdateComplianceScanConfigurationBody

Next available tag: 5

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| scanName |  |  | String |  |  |
| scanConfig |  |  | [V2BaseComplianceScanConfigurationSettings](#V2BaseComplianceScanConfigurationSettings_CommonObjectReference) |  |  |
| clusters |  |  | List of `string` |  |  |

<a id="ComplianceServiceUpdateComplianceStandardConfigBody_CommonObjectReference"></a>

## ComplianceServiceUpdateComplianceStandardConfigBody

| Field Name      | Required | Nullable | Type    | Description | Format |
|-----------------|----------|----------|---------|-------------|--------|
| hideScanResults |          |          | Boolean |             |        |

<a id="ComputeEffectiveAccessScopeRequestDetail_CommonObjectReference"></a>

## ComputeEffectiveAccessScopeRequestDetail

| Enum Values |
|-------------|
| STANDARD    |
| MINIMAL     |
| HIGH        |

<a id="ComputeEffectiveAccessScopeRequestPayload_CommonObjectReference"></a>

## ComputeEffectiveAccessScopeRequestPayload

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| simpleRules |  |  | [SimpleAccessScopeRules](#SimpleAccessScopeRules_CommonObjectReference) |  |  |

<a id="ContainerConfigEnvironmentConfig_CommonObjectReference"></a>

## ContainerConfigEnvironmentConfig

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| key |  |  | String |  |  |
| value |  |  | String |  |  |
| envVarSource |  |  | [EnvironmentConfigEnvVarSource](#EnvironmentConfigEnvVarSource_CommonObjectReference) |  | UNSET, RAW, SECRET_KEY, CONFIG_MAP_KEY, FIELD, RESOURCE_FIELD, UNKNOWN, |

<a id="ContainerNameAndBaselineStatusBaselineStatus_CommonObjectReference"></a>

## ContainerNameAndBaselineStatusBaselineStatus

- NOT_GENERATED: In current implementation, this is a temporary condition.

| Enum Values   |
|---------------|
| INVALID       |
| NOT_GENERATED |
| UNLOCKED      |
| LOCKED        |

<a id="CosignPublicKeyVerificationPublicKey_CommonObjectReference"></a>

## CosignPublicKeyVerificationPublicKey

| Field Name      | Required | Nullable | Type   | Description | Format |
|-----------------|----------|----------|--------|-------------|--------|
| name            |          |          | String |             |        |
| publicKeyPemEnc |          |          | String |             |        |

<a id="DBExportManifestEncodingType_CommonObjectReference"></a>

## DBExportManifestEncodingType

The encoding of the file data in the restore body, usually for compression purposes.

| Enum Values   |
|---------------|
| UNKNOWN       |
| UNCOMPREESSED |
| DEFLATED      |

<a id="DBRestoreProcessStatusResumeInfo_CommonObjectReference"></a>

## DBRestoreProcessStatusResumeInfo

| Field Name | Required | Nullable | Type   | Description | Format |
|------------|----------|----------|--------|-------------|--------|
| pos        |          |          | String |             | int64  |

<a id="DBRestoreRequestHeaderLocalFileInfo_CommonObjectReference"></a>

## DBRestoreRequestHeaderLocalFileInfo

LocalFileInfo provides information about the file on the local machine of the user initiating the restore process, in order to provide information to other users about ongoing restore processes.

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| path |  |  | String | The full path of the file. |  |
| bytesSize |  |  | String | The size of the file, in bytes. 0 if unknown. | int64 |

<a id="DatabaseStatusDatabaseType_CommonObjectReference"></a>

## DatabaseStatusDatabaseType

| Enum Values |
|-------------|
| Hidden      |
| RocksDB     |
| PostgresDB  |

<a id="DeclarativeConfigHealthResourceType_CommonObjectReference"></a>

## DeclarativeConfigHealthResourceType

| Enum Values                    |
|--------------------------------|
| CONFIG_MAP                     |
| ACCESS_SCOPE                   |
| PERMISSION_SET                 |
| ROLE                           |
| AUTH_PROVIDER                  |
| GROUP                          |
| NOTIFIER                       |
| AUTH_MACHINE_TO_MACHINE_CONFIG |

<a id="DelegatedRegistryConfigDelegatedRegistry_CommonObjectReference"></a>

## DelegatedRegistryConfigDelegatedRegistry

| Field Name | Required | Nullable | Type   | Description | Format |
|------------|----------|----------|--------|-------------|--------|
| path       |          |          | String |             |        |
| clusterId  |          |          | String |             |        |

<a id="DelegatedRegistryConfigEnabledFor_CommonObjectReference"></a>

## DelegatedRegistryConfigEnabledFor

- NONE: Scan all images via central services except for images from the OCP integrated registry - ALL: Scan all images via the secured clusters - SPECIFIC: Scan images that match `registries` or are from the OCP integrated registry via the secured clusters otherwise scan via central services

| Enum Values |
|-------------|
| NONE        |
| ALL         |
| SPECIFIC    |

<a id="DeployDetectionResponseRun_CommonObjectReference"></a>

## DeployDetectionResponseRun

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| name |  |  | String |  |  |
| type |  |  | String |  |  |
| alerts |  |  | List of [StorageAlert](#StorageAlert_CommonObjectReference) |  |  |

<a id="DeploymentContainer_CommonObjectReference"></a>

## DeploymentContainer

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| image |  |  | [StorageContainerImage](#StorageContainerImage_CommonObjectReference) |  |  |
| name |  |  | String |  |  |

<a id="DeploymentLabelsResponseLabelValues_CommonObjectReference"></a>

## DeploymentLabelsResponseLabelValues

| Field Name | Required | Nullable | Type             | Description | Format |
|------------|----------|----------|------------------|-------------|--------|
| values     |          |          | List of `string` |             |        |

<a id="DeploymentListenPort_CommonObjectReference"></a>

## DeploymentListenPort

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| port |  |  | Long |  | int64 |
| l4protocol |  |  | [StorageL4Protocol](#StorageL4Protocol_CommonObjectReference) |  | L4_PROTOCOL_UNKNOWN, L4_PROTOCOL_TCP, L4_PROTOCOL_UDP, L4_PROTOCOL_ICMP, L4_PROTOCOL_RAW, L4_PROTOCOL_SCTP, L4_PROTOCOL_ANY, |

<a id="DiscoveredClusterMetadataType_CommonObjectReference"></a>

## DiscoveredClusterMetadataType

| Enum Values |
|-------------|
| UNSPECIFIED |
| AKS         |
| ARO         |
| EKS         |
| GKE         |
| OCP         |
| OSD         |
| ROSA        |

<a id="DryRunResponseAlert_CommonObjectReference"></a>

## DryRunResponseAlert

| Field Name | Required | Nullable | Type             | Description | Format |
|------------|----------|----------|------------------|-------------|--------|
| deployment |          |          | String           |             |        |
| violations |          |          | List of `string` |             |        |

<a id="DynamicClusterConfigProcessIndicatorsConfig_CommonObjectReference"></a>

## DynamicClusterConfigProcessIndicatorsConfig

Configure per-namespace persistence for ProcessIndicators

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| noPersistence |  |  | Boolean | Specifies whether to persist process indicators independently from other configuratons. If true, the filters above are ignored, and no process indicators are persisted. If false (the protobuf default for booleans), process indicators are persisted according to namespace_filter and exclude_openshift_ns. |  |
| excludeNamespaceFilter |  |  | String | A regex specifying to not persist process indicators from specified namespaces. E.g. namespace_filter: "test-.\*" will instruct Central to not persist any process indicator coming from the "test-filtering" namespace. |  |
| excludeOpenshiftNs |  |  | Boolean | A short-cut to not persist process indicators from openshift namespaces. Equivalent to namespace_filter: "openshift-.\*". |  |

<a id="ECRConfigAuthorizationData_CommonObjectReference"></a>

## ECRConfigAuthorizationData

An authorization data represents the IAM authentication credentials and can be used to access any Amazon ECR registry that the IAM principal has access to.

| Field Name | Required | Nullable | Type   | Description | Format    |
|------------|----------|----------|--------|-------------|-----------|
| username   |          |          | String |             |           |
| password   |          |          | String |             |           |
| expiresAt  |          |          | Date   |             | date-time |

<a id="EffectiveAccessScopeCluster_CommonObjectReference"></a>

## EffectiveAccessScopeCluster

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| id |  |  | String |  |  |
| name |  |  | String |  |  |
| state |  |  | [StorageEffectiveAccessScopeState](#StorageEffectiveAccessScopeState_CommonObjectReference) |  | UNKNOWN, INCLUDED, EXCLUDED, PARTIAL, |
| labels |  |  | Map of `string` |  |  |
| namespaces |  |  | List of [StorageEffectiveAccessScopeNamespace](#StorageEffectiveAccessScopeNamespace_CommonObjectReference) |  |  |

<a id="EmailAuthMethod_CommonObjectReference"></a>

## EmailAuthMethod

| Enum Values |
|-------------|
| DISABLED    |
| PLAIN       |
| LOGIN       |

<a id="EmbeddedImageScanComponentExecutable_CommonObjectReference"></a>

## EmbeddedImageScanComponentExecutable

| Field Name   | Required | Nullable | Type             | Description | Format |
|--------------|----------|----------|------------------|-------------|--------|
| path         |          |          | String           |             |        |
| dependencies |          |          | List of `string` |             |        |

<a id="EmbeddedVulnerabilityScoreVersion_CommonObjectReference"></a>

## EmbeddedVulnerabilityScoreVersion

ScoreVersion can be deprecated ROX-26066

- V2: No unset for automatic backwards compatibility

| Enum Values |
|-------------|
| V2          |
| V3          |

<a id="EmbeddedVulnerabilityVulnerabilityType_CommonObjectReference"></a>

## EmbeddedVulnerabilityVulnerabilityType

| Enum Values             |
|-------------------------|
| UNKNOWN_VULNERABILITY   |
| IMAGE_VULNERABILITY     |
| K8S_VULNERABILITY       |
| ISTIO_VULNERABILITY     |
| NODE_VULNERABILITY      |
| OPENSHIFT_VULNERABILITY |

<a id="EnvironmentConfigEnvVarSource_CommonObjectReference"></a>

## EnvironmentConfigEnvVarSource

For any update to EnvVarSource, please also update 'ui/src/messages/common.js'

| Enum Values    |
|----------------|
| UNSET          |
| RAW            |
| SECRET_KEY     |
| CONFIG_MAP_KEY |
| FIELD          |
| RESOURCE_FIELD |
| UNKNOWN        |

<a id="ExceptionExpiryExpiryType_CommonObjectReference"></a>

## ExceptionExpiryExpiryType

| Enum Values     |
|-----------------|
| TIME            |
| ALL_CVE_FIXABLE |
| ANY_CVE_FIXABLE |

<a id="ExclusionDeployment_CommonObjectReference"></a>

## ExclusionDeployment

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| name |  |  | String |  |  |
| scope |  |  | [StorageScope](#StorageScope_CommonObjectReference) |  |  |

<a id="ExclusionImage_CommonObjectReference"></a>

## ExclusionImage

| Field Name | Required | Nullable | Type   | Description | Format |
|------------|----------|----------|--------|-------------|--------|
| name       |          |          | String |             |        |

<a id="ExternalBackupServicePutExternalBackupBody_CommonObjectReference"></a>

## ExternalBackupServicePutExternalBackupBody

Next available tag: 10

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| name |  |  | String |  |  |
| type |  |  | String |  |  |
| schedule |  |  | [StorageSchedule](#StorageSchedule_CommonObjectReference) |  |  |
| backupsToKeep |  |  | Integer |  | int32 |
| s3 |  |  | [StorageS3Config](#StorageS3Config_CommonObjectReference) |  |  |
| gcs |  |  | [StorageGCSConfig](#StorageGCSConfig_CommonObjectReference) |  |  |
| s3compatible |  |  | [StorageS3Compatible](#StorageS3Compatible_CommonObjectReference) |  |  |
| includeCertificates |  |  | Boolean |  |  |

<a id="ExternalBackupServiceUpdateExternalBackupBody_CommonObjectReference"></a>

## ExternalBackupServiceUpdateExternalBackupBody

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| externalBackup |  |  | [NextAvailableTag10](#NextAvailableTag10_CommonObjectReference) |  |  |
| updatePassword |  |  | Boolean | When false, use the stored credentials of an existing external backup configuration given its ID. |  |

<a id="FileAccessFileMetadata_CommonObjectReference"></a>

## FileAccessFileMetadata

| Field Name | Required | Nullable | Type   | Description | Format |
|------------|----------|----------|--------|-------------|--------|
| uid        |          |          | Long   |             | int64  |
| gid        |          |          | Long   |             | int64  |
| mode       |          |          | Long   |             | int64  |
| username   |          |          | String |             |        |
| group      |          |          | String |             |        |

<a id="FileAccessOperation_CommonObjectReference"></a>

## FileAccessOperation

| Enum Values       |
|-------------------|
| CREATE            |
| UNLINK            |
| RENAME            |
| PERMISSION_CHANGE |
| OWNERSHIP_CHANGE  |
| OPEN              |

<a id="GenerateNetworkPoliciesRequestDeleteExistingPoliciesMode_CommonObjectReference"></a>

## GenerateNetworkPoliciesRequestDeleteExistingPoliciesMode

- NONE: Do not delete any existing network policies.

- GENERATED_ONLY: Delete any existing **auto-generated** network policies.

- ALL: Delete all existing network policies in the respective namespace.

| Enum Values    |
|----------------|
| UNKNOWN        |
| NONE           |
| GENERATED_ONLY |
| ALL            |

<a id="GetAlertTimeseriesResponseClusterAlerts_CommonObjectReference"></a>

## GetAlertTimeseriesResponseClusterAlerts

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| cluster |  |  | String |  |  |
| severities |  |  | List of [ClusterAlertsAlertEvents](#ClusterAlertsAlertEvents_CommonObjectReference) |  |  |

<a id="GetAlertsCountsRequestRequestGroup_CommonObjectReference"></a>

## GetAlertsCountsRequestRequestGroup

| Enum Values |
|-------------|
| UNSET       |
| CATEGORY    |
| CLUSTER     |

<a id="GetAlertsCountsResponseAlertGroup_CommonObjectReference"></a>

## GetAlertsCountsResponseAlertGroup

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| group |  |  | String |  |  |
| counts |  |  | List of [AlertGroupAlertCounts](#AlertGroupAlertCounts_CommonObjectReference) |  |  |

<a id="GetLoginAuthProvidersResponseLoginAuthProvider_CommonObjectReference"></a>

## GetLoginAuthProvidersResponseLoginAuthProvider

| Field Name | Required | Nullable | Type   | Description | Format |
|------------|----------|----------|--------|-------------|--------|
| id         |          |          | String |             |        |
| name       |          |          | String |             |        |
| type       |          |          | String |             |        |
| loginUrl   |          |          | String |             |        |

<a id="GetSensorUpgradeConfigResponseSensorAutoUpgradeFeatureStatus_CommonObjectReference"></a>

## GetSensorUpgradeConfigResponseSensorAutoUpgradeFeatureStatus

| Enum Values   |
|---------------|
| NOT_SUPPORTED |
| SUPPORTED     |

<a id="GetSensorUpgradeConfigResponseUpgradeConfig_CommonObjectReference"></a>

## GetSensorUpgradeConfigResponseUpgradeConfig

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| enableAutoUpgrade |  |  | Boolean |  |  |
| autoUpgradeFeature |  |  | [GetSensorUpgradeConfigResponseSensorAutoUpgradeFeatureStatus](#GetSensorUpgradeConfigResponseSensorAutoUpgradeFeatureStatus_CommonObjectReference) |  | NOT_SUPPORTED, SUPPORTED, |

<a id="GoogleRpcStatus_CommonObjectReference"></a>

## GoogleRpcStatus

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| code |  |  | Integer |  | int32 |
| message |  |  | String |  |  |
| details |  |  | List of [ProtobufAny](#ProtobufAny_CommonObjectReference) |  |  |

<a id="GooglerpcStatus_CommonObjectReference"></a>

## GooglerpcStatus

| Field Name | Required | Nullable | Type    | Description | Format |
|------------|----------|----------|---------|-------------|--------|
| code       |          |          | Integer |             | int32  |
| message    |          |          | String  |             |        |

<a id="GroupLabels_CommonObjectReference"></a>

## GroupLabels

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| labels |  |  | List of `string` | A list of labels to aggregate on. The complete list of labels for the given metric group can be found in the documentation, or in the API error message, returned when an invalid label is attempted to be added. |  |
| includeFilters |  |  | Map of `string` | A map of label name to a filter regular expression for this label value. See the RE2 syntax reference: <https://github.com/google/re2/wiki/Syntax>. If include_filters are specified, a metric record is only counted if all label values match the according label expression. Patterns are full-match only (automatically wrapped with ^ and \$). |  |
| excludeFilters |  |  | Map of `string` | A map of label name to a filter regular expression for this label value. See the RE2 syntax reference: <https://github.com/google/re2/wiki/Syntax>. If exclude_filters are specified, a metric record is dropped if any label value matches the according label expression. Patterns are full-match only (automatically wrapped with ^ and \$). Exclude filters are applied after include filters. |  |

<a id="ImageIntegrationServicePutImageIntegrationBody_CommonObjectReference"></a>

## ImageIntegrationServicePutImageIntegrationBody

Next Tag: 25

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| name |  |  | String |  |  |
| type |  |  | String |  |  |
| categories |  |  | List of [StorageImageIntegrationCategory](#StorageImageIntegrationCategory_CommonObjectReference) |  |  |
| clairify |  |  | [StorageClairifyConfig](#StorageClairifyConfig_CommonObjectReference) |  |  |
| scannerV4 |  |  | [StorageScannerV4Config](#StorageScannerV4Config_CommonObjectReference) |  |  |
| docker |  |  | [StorageDockerConfig](#StorageDockerConfig_CommonObjectReference) |  |  |
| quay |  |  | [StorageQuayConfig](#StorageQuayConfig_CommonObjectReference) |  |  |
| ecr |  |  | [StorageECRConfig](#StorageECRConfig_CommonObjectReference) |  |  |
| google |  |  | [StorageGoogleConfig](#StorageGoogleConfig_CommonObjectReference) |  |  |
| clair |  |  | [StorageClairConfig](#StorageClairConfig_CommonObjectReference) |  |  |
| clairV4 |  |  | [StorageClairV4Config](#StorageClairV4Config_CommonObjectReference) |  |  |
| ibm |  |  | [StorageIBMRegistryConfig](#StorageIBMRegistryConfig_CommonObjectReference) |  |  |
| azure |  |  | [StorageAzureConfig](#StorageAzureConfig_CommonObjectReference) |  |  |
| autogenerated |  |  | Boolean |  |  |
| clusterId |  |  | String |  |  |
| skipTestIntegration |  |  | Boolean |  |  |
| source |  |  | [StorageImageIntegrationSource](#StorageImageIntegrationSource_CommonObjectReference) |  |  |

<a id="ImageIntegrationServiceUpdateImageIntegrationBody_CommonObjectReference"></a>

## ImageIntegrationServiceUpdateImageIntegrationBody

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| config |  |  | [NextTag25](#NextTag25_CommonObjectReference) |  |  |
| updatePassword |  |  | Boolean | When false, use the stored credentials of an existing image integration given its ID. |  |

<a id="ImagePullSecretRegistry_CommonObjectReference"></a>

## ImagePullSecretRegistry

| Field Name | Required | Nullable | Type   | Description | Format |
|------------|----------|----------|--------|-------------|--------|
| name       |          |          | String |             |        |
| username   |          |          | String |             |        |

<a id="ImageSBOMRequest_CommonObjectReference"></a>

## ImageSBOMRequest

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| cluster |  |  | String | Cluster to delegate scan to, may be the cluster’s name or ID. |  |
| namespace |  |  | String | Namespace on the secured cluster from which to read context information when delegating image scans, specifically pull secrets to access the image registry. |  |
| imageName | X |  | String | Image name and reference. (e.g. nginx:latest or nginx@sha256:…​) |  |
| force |  |  | Boolean | Bypass Central’s cache for the image and force a new pull from the Scanner |  |
| digest |  |  | String | Image digest if not already part of image name |  |

<a id="InitBundleMetaImpactedCluster_CommonObjectReference"></a>

## InitBundleMetaImpactedCluster

| Field Name | Required | Nullable | Type   | Description | Format |
|------------|----------|----------|--------|-------------|--------|
| name       |          |          | String |             |        |
| id         |          |          | String |             |        |

<a id="InitBundleRevokeResponseInitBundleRevocationError_CommonObjectReference"></a>

## InitBundleRevokeResponseInitBundleRevocationError

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| id |  |  | String |  |  |
| error |  |  | String |  |  |
| impactedClusters |  |  | List of [InitBundleMetaImpactedCluster](#InitBundleMetaImpactedCluster_CommonObjectReference) |  |  |

<a id="JiraPriorityMapping_CommonObjectReference"></a>

## JiraPriorityMapping

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| severity |  |  | [StorageSeverity](#StorageSeverity_CommonObjectReference) |  | UNSET_SEVERITY, LOW_SEVERITY, MEDIUM_SEVERITY, HIGH_SEVERITY, CRITICAL_SEVERITY, |
| priorityName |  |  | String |  |  |

<a id="KeyValueAttrsKeyValueAttr_CommonObjectReference"></a>

## KeyValueAttrsKeyValueAttr

| Field Name | Required | Nullable | Type   | Description | Format |
|------------|----------|----------|--------|-------------|--------|
| key        |          |          | String |             |        |
| value      |          |          | String |             |        |

<a id="LabelSelectorOperator_CommonObjectReference"></a>

## LabelSelectorOperator

| Enum Values |
|-------------|
| UNKNOWN     |
| IN          |
| NOT_IN      |
| EXISTS      |
| NOT_EXISTS  |

<a id="LabelSelectorRequirement_CommonObjectReference"></a>

## LabelSelectorRequirement

Next available tag: 4

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| key |  |  | String |  |  |
| op |  |  | [StorageLabelSelectorOperator](#StorageLabelSelectorOperator_CommonObjectReference) |  | UNKNOWN, IN, NOT_IN, EXISTS, NOT_EXISTS, |
| values |  |  | List of `string` |  |  |

<a id="ListAlertCommonEntityInfo_CommonObjectReference"></a>

## ListAlertCommonEntityInfo

Fields common to all entities that an alert might belong to.

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| clusterName |  |  | String |  |  |
| namespace |  |  | String |  |  |
| clusterId |  |  | String |  |  |
| namespaceId |  |  | String |  |  |
| resourceType |  |  | [StorageListAlertResourceType](#StorageListAlertResourceType_CommonObjectReference) |  | DEPLOYMENT, SECRETS, CONFIGMAPS, CLUSTER_ROLES, CLUSTER_ROLE_BINDINGS, NETWORK_POLICIES, SECURITY_CONTEXT_CONSTRAINTS, EGRESS_FIREWALLS, NODE, |

<a id="ListAlertNodeEntity_CommonObjectReference"></a>

## ListAlertNodeEntity

| Field Name | Required | Nullable | Type   | Description | Format |
|------------|----------|----------|--------|-------------|--------|
| name       |          |          | String |             |        |

<a id="ListAlertPolicyDevFields_CommonObjectReference"></a>

## ListAlertPolicyDevFields

| Field Name | Required | Nullable | Type   | Description | Format |
|------------|----------|----------|--------|-------------|--------|
| SORTName   |          |          | String |             |        |

<a id="ListAlertResourceEntity_CommonObjectReference"></a>

## ListAlertResourceEntity

| Field Name | Required | Nullable | Type   | Description | Format |
|------------|----------|----------|--------|-------------|--------|
| name       |          |          | String |             |        |

<a id="ListDeploymentsWithProcessInfoResponseDeploymentWithProcessInfo_CommonObjectReference"></a>

## ListDeploymentsWithProcessInfoResponseDeploymentWithProcessInfo

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| deployment |  |  | [StorageListDeployment](#StorageListDeployment_CommonObjectReference) |  |  |
| baselineStatuses |  |  | List of [StorageContainerNameAndBaselineStatus](#StorageContainerNameAndBaselineStatus_CommonObjectReference) |  |  |

<a id="MetadataLicenseStatus_CommonObjectReference"></a>

## MetadataLicenseStatus

| Enum Values |
|-------------|
| NONE        |
| INVALID     |
| EXPIRED     |
| RESTARTING  |
| VALID       |

<a id="MetadataProviderType_CommonObjectReference"></a>

## MetadataProviderType

| Enum Values               |
|---------------------------|
| PROVIDER_TYPE_UNSPECIFIED |
| PROVIDER_TYPE_AWS         |
| PROVIDER_TYPE_GCP         |
| PROVIDER_TYPE_AZURE       |

<a id="MicrosoftSentinelClientCertAuthConfig_CommonObjectReference"></a>

## MicrosoftSentinelClientCertAuthConfig

client certificate which is used for authentication

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| clientCert |  |  | String | PEM encoded ASN.1 DER format. |  |
| privateKey |  |  | String | PEM encoded PKCS \#8, ASN.1 DER format. |  |

<a id="MicrosoftSentinelDataCollectionRuleConfig_CommonObjectReference"></a>

## MicrosoftSentinelDataCollectionRuleConfig

DataCollectionRuleConfig contains information about the data collection rule which is a config per notifier type.

| Field Name           | Required | Nullable | Type    | Description | Format |
|----------------------|----------|----------|---------|-------------|--------|
| streamName           |          |          | String  |             |        |
| dataCollectionRuleId |          |          | String  |             |        |
| enabled              |          |          | Boolean |             |        |

<a id="NetworkBaselineServiceGetNetworkBaselineStatusForFlowsBody_CommonObjectReference"></a>

## NetworkBaselineServiceGetNetworkBaselineStatusForFlowsBody

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| peers |  |  | List of [V1NetworkBaselineStatusPeer](#V1NetworkBaselineStatusPeer_CommonObjectReference) |  |  |

<a id="NetworkBaselineServiceModifyBaselineStatusForPeersBody_CommonObjectReference"></a>

## NetworkBaselineServiceModifyBaselineStatusForPeersBody

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| peers |  |  | List of [V1NetworkBaselinePeerStatus](#V1NetworkBaselinePeerStatus_CommonObjectReference) |  |  |

<a id="NetworkEntityInfoDeployment_CommonObjectReference"></a>

## NetworkEntityInfoDeployment

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| name |  |  | String |  |  |
| namespace |  |  | String |  |  |
| cluster |  |  | String |  |  |
| listenPorts |  |  | List of [DeploymentListenPort](#DeploymentListenPort_CommonObjectReference) |  |  |

<a id="NetworkEntityInfoExternalSource_CommonObjectReference"></a>

## NetworkEntityInfoExternalSource

Update normalizeDupNameExtSrcs(…​) in `central/networkgraph/aggregator/aggregator.go` whenever this message is updated.

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| name |  |  | String |  |  |
| cidr |  |  | String |  |  |
| default |  |  | Boolean | `default` indicates whether the external source is user-generated or system-generated. |  |
| discovered |  |  | Boolean | `discovered` indicates whether the external source is harvested from monitored traffic. |  |

<a id="NetworkFlowInfoEntity_CommonObjectReference"></a>

## NetworkFlowInfoEntity

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| name |  |  | String |  |  |
| entityType |  |  | [StorageNetworkEntityInfoType](#StorageNetworkEntityInfoType_CommonObjectReference) |  | UNKNOWN_TYPE, DEPLOYMENT, INTERNET, LISTEN_ENDPOINT, EXTERNAL_SOURCE, INTERNAL_ENTITIES, |
| deploymentNamespace |  |  | String |  |  |
| deploymentType |  |  | String |  |  |
| port |  |  | Integer |  | int32 |

<a id="NetworkGraphServiceCreateExternalNetworkEntityBody_CommonObjectReference"></a>

## NetworkGraphServiceCreateExternalNetworkEntityBody

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| entity |  |  | [NetworkEntityInfoExternalSource](#NetworkEntityInfoExternalSource_CommonObjectReference) |  |  |

<a id="NetworkGraphServicePatchExternalNetworkEntityBody_CommonObjectReference"></a>

## NetworkGraphServicePatchExternalNetworkEntityBody

| Field Name | Required | Nullable | Type   | Description | Format |
|------------|----------|----------|--------|-------------|--------|
| name       |          |          | String |             |        |

<a id="NetworkPolicyServiceApplyNetworkPolicyYamlForDeploymentBody_CommonObjectReference"></a>

## NetworkPolicyServiceApplyNetworkPolicyYamlForDeploymentBody

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| modification |  |  | [StorageNetworkPolicyModification](#StorageNetworkPolicyModification_CommonObjectReference) |  |  |

<a id="NetworkPolicyServiceGetBaselineGeneratedNetworkPolicyForDeploymentBody_CommonObjectReference"></a>

## NetworkPolicyServiceGetBaselineGeneratedNetworkPolicyForDeploymentBody

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| deleteExisting |  |  | [GenerateNetworkPoliciesRequestDeleteExistingPoliciesMode](#GenerateNetworkPoliciesRequestDeleteExistingPoliciesMode_CommonObjectReference) |  | UNKNOWN, NONE, GENERATED_ONLY, ALL, |
| includePorts |  |  | Boolean |  |  |

<a id="NextAvailableTag10_CommonObjectReference"></a>

## NextAvailableTag10

Next available tag: 10

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| name |  |  | String |  |  |
| type |  |  | String |  |  |
| schedule |  |  | [StorageSchedule](#StorageSchedule_CommonObjectReference) |  |  |
| backupsToKeep |  |  | Integer |  | int32 |
| s3 |  |  | [StorageS3Config](#StorageS3Config_CommonObjectReference) |  |  |
| gcs |  |  | [StorageGCSConfig](#StorageGCSConfig_CommonObjectReference) |  |  |
| s3compatible |  |  | [StorageS3Compatible](#StorageS3Compatible_CommonObjectReference) |  |  |
| includeCertificates |  |  | Boolean |  |  |

<a id="NextTag21_CommonObjectReference"></a>

## NextTag21

Next Tag: 21

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| name |  |  | String |  |  |
| type |  |  | String |  |  |
| uiEndpoint |  |  | String |  |  |
| labelKey |  |  | String |  |  |
| labelDefault |  |  | String |  |  |
| jira |  |  | [StorageJira](#StorageJira_CommonObjectReference) |  |  |
| email |  |  | [StorageEmail](#StorageEmail_CommonObjectReference) |  |  |
| cscc |  |  | [StorageCSCC](#StorageCSCC_CommonObjectReference) |  |  |
| splunk |  |  | [StorageSplunk](#StorageSplunk_CommonObjectReference) |  |  |
| pagerduty |  |  | [StoragePagerDuty](#StoragePagerDuty_CommonObjectReference) |  |  |
| generic |  |  | [StorageGeneric](#StorageGeneric_CommonObjectReference) |  |  |
| sumologic |  |  | [StorageSumoLogic](#StorageSumoLogic_CommonObjectReference) |  |  |
| awsSecurityHub |  |  | [StorageAWSSecurityHub](#StorageAWSSecurityHub_CommonObjectReference) |  |  |
| syslog |  |  | [StorageSyslog](#StorageSyslog_CommonObjectReference) |  |  |
| microsoftSentinel |  |  | [StorageMicrosoftSentinel](#StorageMicrosoftSentinel_CommonObjectReference) |  |  |
| notifierSecret |  |  | String |  |  |
| traits |  |  | [StorageTraits](#StorageTraits_CommonObjectReference) |  |  |

<a id="NextTag25_CommonObjectReference"></a>

## NextTag25

Next Tag: 25

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| name |  |  | String |  |  |
| type |  |  | String |  |  |
| categories |  |  | List of [StorageImageIntegrationCategory](#StorageImageIntegrationCategory_CommonObjectReference) |  |  |
| clairify |  |  | [StorageClairifyConfig](#StorageClairifyConfig_CommonObjectReference) |  |  |
| scannerV4 |  |  | [StorageScannerV4Config](#StorageScannerV4Config_CommonObjectReference) |  |  |
| docker |  |  | [StorageDockerConfig](#StorageDockerConfig_CommonObjectReference) |  |  |
| quay |  |  | [StorageQuayConfig](#StorageQuayConfig_CommonObjectReference) |  |  |
| ecr |  |  | [StorageECRConfig](#StorageECRConfig_CommonObjectReference) |  |  |
| google |  |  | [StorageGoogleConfig](#StorageGoogleConfig_CommonObjectReference) |  |  |
| clair |  |  | [StorageClairConfig](#StorageClairConfig_CommonObjectReference) |  |  |
| clairV4 |  |  | [StorageClairV4Config](#StorageClairV4Config_CommonObjectReference) |  |  |
| ibm |  |  | [StorageIBMRegistryConfig](#StorageIBMRegistryConfig_CommonObjectReference) |  |  |
| azure |  |  | [StorageAzureConfig](#StorageAzureConfig_CommonObjectReference) |  |  |
| autogenerated |  |  | Boolean |  |  |
| clusterId |  |  | String |  |  |
| skipTestIntegration |  |  | Boolean |  |  |
| source |  |  | [StorageImageIntegrationSource](#StorageImageIntegrationSource_CommonObjectReference) |  |  |

<a id="NodeScanScanner_CommonObjectReference"></a>

## NodeScanScanner

| Enum Values |
|-------------|
| SCANNER     |
| SCANNER_V4  |

<a id="NotifierServicePutNotifierBody_CommonObjectReference"></a>

## NotifierServicePutNotifierBody

Next Tag: 21

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| name |  |  | String |  |  |
| type |  |  | String |  |  |
| uiEndpoint |  |  | String |  |  |
| labelKey |  |  | String |  |  |
| labelDefault |  |  | String |  |  |
| jira |  |  | [StorageJira](#StorageJira_CommonObjectReference) |  |  |
| email |  |  | [StorageEmail](#StorageEmail_CommonObjectReference) |  |  |
| cscc |  |  | [StorageCSCC](#StorageCSCC_CommonObjectReference) |  |  |
| splunk |  |  | [StorageSplunk](#StorageSplunk_CommonObjectReference) |  |  |
| pagerduty |  |  | [StoragePagerDuty](#StoragePagerDuty_CommonObjectReference) |  |  |
| generic |  |  | [StorageGeneric](#StorageGeneric_CommonObjectReference) |  |  |
| sumologic |  |  | [StorageSumoLogic](#StorageSumoLogic_CommonObjectReference) |  |  |
| awsSecurityHub |  |  | [StorageAWSSecurityHub](#StorageAWSSecurityHub_CommonObjectReference) |  |  |
| syslog |  |  | [StorageSyslog](#StorageSyslog_CommonObjectReference) |  |  |
| microsoftSentinel |  |  | [StorageMicrosoftSentinel](#StorageMicrosoftSentinel_CommonObjectReference) |  |  |
| notifierSecret |  |  | String |  |  |
| traits |  |  | [StorageTraits](#StorageTraits_CommonObjectReference) |  |  |

<a id="NotifierServiceUpdateNotifierBody_CommonObjectReference"></a>

## NotifierServiceUpdateNotifierBody

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| notifier |  |  | [NextTag21](#NextTag21_CommonObjectReference) |  |  |
| updatePassword |  |  | Boolean | When false, use the stored credentials of an existing notifier configuration given its ID. |  |

<a id="PlatformComponentConfigRule_CommonObjectReference"></a>

## PlatformComponentConfigRule

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| name |  |  | String |  |  |
| namespaceRule |  |  | [RuleNamespaceRule](#RuleNamespaceRule_CommonObjectReference) |  |  |

<a id="PodContainerInstanceList_CommonObjectReference"></a>

## PodContainerInstanceList

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| instances |  |  | List of [StorageContainerInstance](#StorageContainerInstance_CommonObjectReference) |  |  |

<a id="PolicyMitreAttackVectors_CommonObjectReference"></a>

## PolicyMitreAttackVectors

| Field Name | Required | Nullable | Type             | Description | Format |
|------------|----------|----------|------------------|-------------|--------|
| tactic     |          |          | String           |             |        |
| techniques |          |          | List of `string` |             |        |

<a id="PolicyServiceEnableDisablePolicyNotificationBody_CommonObjectReference"></a>

## PolicyServiceEnableDisablePolicyNotificationBody

| Field Name  | Required | Nullable | Type             | Description | Format |
|-------------|----------|----------|------------------|-------------|--------|
| notifierIds |          |          | List of `string` |             |        |
| disable     |          |          | Boolean          |             |        |

<a id="PolicyServicePatchPolicyBody_CommonObjectReference"></a>

## PolicyServicePatchPolicyBody

| Field Name | Required | Nullable | Type    | Description | Format |
|------------|----------|----------|---------|-------------|--------|
| disabled   |          |          | Boolean |             |        |

<a id="PolicyServicePutPolicyBody_CommonObjectReference"></a>

## PolicyServicePutPolicyBody

Next tag: 28

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| name |  |  | String | Name of the policy. Must be unique. |  |
| description |  |  | String | Free-form text description of this policy. |  |
| rationale |  |  | String |  |  |
| remediation |  |  | String | Describes how to remediate a violation of this policy. |  |
| disabled |  |  | Boolean | Toggles whether or not this policy will be executing and actively firing alerts. |  |
| categories |  |  | List of `string` | List of categories that this policy falls under. Category names must already exist in Central. |  |
| lifecycleStages |  |  | List of [StorageLifecycleStage](#StorageLifecycleStage_CommonObjectReference) | Describes which policy lifecylce stages this policy applies to. Choices are DEPLOY, BUILD, and RUNTIME. |  |
| eventSource |  |  | [StorageEventSource](#StorageEventSource_CommonObjectReference) |  | NOT_APPLICABLE, DEPLOYMENT_EVENT, AUDIT_LOG_EVENT, NODE_EVENT, |
| exclusions |  |  | List of [StorageExclusion](#StorageExclusion_CommonObjectReference) | Define deployments or images that should be excluded from this policy. |  |
| scope |  |  | List of [StorageScope](#StorageScope_CommonObjectReference) | Defines clusters, namespaces, and deployments that should be included in this policy. No scopes defined includes everything. |  |
| severity |  |  | [StorageSeverity](#StorageSeverity_CommonObjectReference) |  | UNSET_SEVERITY, LOW_SEVERITY, MEDIUM_SEVERITY, HIGH_SEVERITY, CRITICAL_SEVERITY, |
| enforcementActions |  |  | List of [StorageEnforcementAction](#StorageEnforcementAction_CommonObjectReference) | FAIL_DEPLOYMENT_CREATE_ENFORCEMENT takes effect only if admission control webhook is configured to enforce on object creates/updates. FAIL_KUBE_REQUEST_ENFORCEMENT takes effect only if admission control webhook is enabled to listen on exec and port-forward events. FAIL_DEPLOYMENT_UPDATE_ENFORCEMENT takes effect only if admission control webhook is configured to enforce on object updates. Lists the enforcement actions to take when a violation from this policy is identified. Possible value are UNSET_ENFORCEMENT, SCALE_TO_ZERO_ENFORCEMENT, UNSATISFIABLE_NODE_CONSTRAINT_ENFORCEMENT, KILL_POD_ENFORCEMENT, FAIL_BUILD_ENFORCEMENT, FAIL_KUBE_REQUEST_ENFORCEMENT, FAIL_DEPLOYMENT_CREATE_ENFORCEMENT, and. FAIL_DEPLOYMENT_UPDATE_ENFORCEMENT. |  |
| notifiers |  |  | List of `string` | List of IDs of the notifiers that should be triggered when a violation from this policy is identified. IDs should be in the form of a UUID and are found through the Central API. |  |
| lastUpdated |  |  | Date |  | date-time |
| SORTName |  |  | String | For internal use only. |  |
| SORTLifecycleStage |  |  | String | For internal use only. |  |
| SORTEnforcement |  |  | Boolean | For internal use only. |  |
| policyVersion |  |  | String |  |  |
| policySections |  |  | List of [StoragePolicySection](#StoragePolicySection_CommonObjectReference) | PolicySections define the violation criteria for this policy. |  |
| mitreAttackVectors |  |  | List of [PolicyMitreAttackVectors](#PolicyMitreAttackVectors_CommonObjectReference) |  |  |
| criteriaLocked |  |  | Boolean | Read-only field. If true, the policy’s criteria fields are rendered read-only. |  |
| mitreVectorsLocked |  |  | Boolean | Read-only field. If true, the policy’s MITRE ATT&CK fields are rendered read-only. |  |
| isDefault |  |  | Boolean | Read-only field. Indicates the policy is a default policy if true and a custom policy if false. |  |
| source |  |  | [StoragePolicySource](#StoragePolicySource_CommonObjectReference) |  | IMPERATIVE, DECLARATIVE, |

<a id="PortConfigExposureInfo_CommonObjectReference"></a>

## PortConfigExposureInfo

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| level |  |  | [PortConfigExposureLevel](#PortConfigExposureLevel_CommonObjectReference) |  | UNSET, EXTERNAL, NODE, INTERNAL, HOST, ROUTE, |
| serviceName |  |  | String |  |  |
| serviceId |  |  | String |  |  |
| serviceClusterIp |  |  | String |  |  |
| servicePort |  |  | Integer |  | int32 |
| nodePort |  |  | Integer |  | int32 |
| externalIps |  |  | List of `string` |  |  |
| externalHostnames |  |  | List of `string` |  |  |

<a id="PortConfigExposureLevel_CommonObjectReference"></a>

## PortConfigExposureLevel

| Enum Values |
|-------------|
| UNSET       |
| EXTERNAL    |
| NODE        |
| INTERNAL    |
| HOST        |
| ROUTE       |

<a id="ProcessListeningOnPortEndpoint_CommonObjectReference"></a>

## ProcessListeningOnPortEndpoint

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| port |  |  | Long |  | int64 |
| protocol |  |  | [StorageL4Protocol](#StorageL4Protocol_CommonObjectReference) |  | L4_PROTOCOL_UNKNOWN, L4_PROTOCOL_TCP, L4_PROTOCOL_UDP, L4_PROTOCOL_ICMP, L4_PROTOCOL_RAW, L4_PROTOCOL_SCTP, L4_PROTOCOL_ANY, |

<a id="ProcessSignalLineageInfo_CommonObjectReference"></a>

## ProcessSignalLineageInfo

| Field Name         | Required | Nullable | Type   | Description | Format |
|--------------------|----------|----------|--------|-------------|--------|
| parentUid          |          |          | Long   |             | int64  |
| parentExecFilePath |          |          | String |             |        |

<a id="PrometheusMetricsGroup_CommonObjectReference"></a>

## PrometheusMetricsGroup

A group is a collection of metrics that are computed by the same aggregator. Metrics in a group may use different subsets of a complete list of labels supported by the aggregator.

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| gatheringPeriodMinutes |  |  | Long | The gathering period for periodically gathered metrics. If set to zero, gathering is disabled. | int64 |
| descriptors |  |  | Map of [GroupLabels](#GroupLabels_CommonObjectReference) | Metric descriptors is a map of metric names to the list of allowed labels. |  |

<a id="ProtobufAny_CommonObjectReference"></a>

## ProtobufAny

| Field Name | Required | Nullable | Type   | Description | Format |
|------------|----------|----------|--------|-------------|--------|
| @type      |          |          | String |             |        |

<a id="QuayConfigRobotAccount_CommonObjectReference"></a>

## QuayConfigRobotAccount

Robot account is Quay’s named tokens that can be granted permissions on multiple repositories under an organization. It’s Quay’s recommended authentication model when possible (i.e. registry integration)

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| username |  |  | String |  |  |
| password |  |  | String | The server will mask the value of this password in responses and logs. |  |

<a id="ReportConfigurationReportType_CommonObjectReference"></a>

## ReportConfigurationReportType

| Enum Values   |
|---------------|
| VULNERABILITY |

<a id="ReportConfigurationServiceUpdateReportConfigurationBody_CommonObjectReference"></a>

## ReportConfigurationServiceUpdateReportConfigurationBody

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| reportConfig |  |  | [StorageReportConfiguration](#StorageReportConfiguration_CommonObjectReference) |  |  |

<a id="ReportLastRunStatusRunStatus_CommonObjectReference"></a>

## ReportLastRunStatusRunStatus

| Enum Values |
|-------------|
| SUCCESS     |
| FAILURE     |

<a id="ReportServiceUpdateReportConfigurationBody_CommonObjectReference"></a>

## ReportServiceUpdateReportConfigurationBody

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| name |  |  | String |  |  |
| description |  |  | String |  |  |
| type |  |  | [V2ReportConfigurationReportType](#V2ReportConfigurationReportType_CommonObjectReference) |  | VULNERABILITY, |
| vulnReportFilters |  |  | [V2VulnerabilityReportFilters](#V2VulnerabilityReportFilters_CommonObjectReference) |  |  |
| schedule |  |  | [V2ReportSchedule](#V2ReportSchedule_CommonObjectReference) |  |  |
| resourceScope |  |  | [V2ResourceScope](#V2ResourceScope_CommonObjectReference) |  |  |
| notifiers |  |  | List of [V2NotifierConfiguration](#V2NotifierConfiguration_CommonObjectReference) |  |  |

<a id="ResourceCollectionEmbeddedResourceCollection_CommonObjectReference"></a>

## ResourceCollectionEmbeddedResourceCollection

| Field Name | Required | Nullable | Type   | Description | Format |
|------------|----------|----------|--------|-------------|--------|
| id         |          |          | String |             |        |

<a id="ResourceResourceType_CommonObjectReference"></a>

## ResourceResourceType

| Enum Values                  |
|------------------------------|
| UNKNOWN                      |
| SECRETS                      |
| CONFIGMAPS                   |
| CLUSTER_ROLES                |
| CLUSTER_ROLE_BINDINGS        |
| NETWORK_POLICIES             |
| SECURITY_CONTEXT_CONSTRAINTS |
| EGRESS_FIREWALLS             |

<a id="ResultFactor_CommonObjectReference"></a>

## ResultFactor

| Field Name | Required | Nullable | Type   | Description | Format |
|------------|----------|----------|--------|-------------|--------|
| message    |          |          | String |             |        |
| url        |          |          | String |             |        |

<a id="RiskResult_CommonObjectReference"></a>

## RiskResult

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| name |  |  | String |  |  |
| factors |  |  | List of [ResultFactor](#ResultFactor_CommonObjectReference) |  |  |
| score |  |  | Float |  | float |

<a id="RoleServicePutPermissionSetBody_CommonObjectReference"></a>

## RoleServicePutPermissionSetBody

This encodes a set of permissions for StackRox resources.

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| name |  |  | String | `name` and `description` are provided by the user and can be changed. |  |
| description |  |  | String |  |  |
| resourceToAccess |  |  | Map of [StorageAccess](#StorageAccess_CommonObjectReference) |  |  |
| traits |  |  | [StorageTraits](#StorageTraits_CommonObjectReference) |  |  |

<a id="RoleServicePutSimpleAccessScopeBody_CommonObjectReference"></a>

## RoleServicePutSimpleAccessScopeBody

Simple access scope is a (simple) selection criteria for scoped resources. It does **not** allow multi-component AND-rules nor set operations on names.

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| name |  |  | String | `name` and `description` are provided by the user and can be changed. |  |
| description |  |  | String |  |  |
| rules |  |  | [SimpleAccessScopeRules](#SimpleAccessScopeRules_CommonObjectReference) |  |  |
| traits |  |  | [StorageTraits](#StorageTraits_CommonObjectReference) |  |  |

<a id="RoleServiceUpdateRoleBody_CommonObjectReference"></a>

## RoleServiceUpdateRoleBody

A role specifies which actions are allowed for which subset of cluster objects. Permissions be can either specified directly via setting resource_to_access together with global_access or by referencing a permission set by its id in permission_set_name.

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| description |  |  | String |  |  |
| permissionSetId |  |  | String | The associated PermissionSet and AccessScope for this Role. |  |
| accessScopeId |  |  | String |  |  |
| globalAccess |  |  | [StorageAccess](#StorageAccess_CommonObjectReference) |  | NO_ACCESS, READ_ACCESS, READ_WRITE_ACCESS, |
| resourceToAccess |  |  | Map of [StorageAccess](#StorageAccess_CommonObjectReference) | Deprecated 2021-04-20 in favor of `permission_set_id`. |  |
| traits |  |  | [StorageTraits](#StorageTraits_CommonObjectReference) |  |  |

<a id="RpcStatus_CommonObjectReference"></a>

## RpcStatus

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| code |  |  | Integer |  | int32 |
| message |  |  | String |  |  |
| details |  |  | List of [ProtobufAny](#ProtobufAny_CommonObjectReference) |  |  |

<a id="RuleNamespaceRule_CommonObjectReference"></a>

## RuleNamespaceRule

| Field Name | Required | Nullable | Type   | Description | Format |
|------------|----------|----------|--------|-------------|--------|
| regex      |          |          | String |             |        |

<a id="SBOMSPDX23Document_CommonObjectReference"></a>

## SBOMSPDX23Document

SPDX 2.3 document, refer to <https://spdx.github.io/spdx-spec/v2.3/> for more details.

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| spdxVersion |  |  | String |  |  |
| dataLicense |  |  | String |  |  |
| SPDXID |  |  | String |  |  |
| name |  |  | String |  |  |
| documentNamespace |  |  | String |  |  |
| creationInfo |  |  | [SBOMSPDX23DocumentCreationInfo](#SBOMSPDX23DocumentCreationInfo_CommonObjectReference) |  |  |
| packages |  |  | List of [SBOMSPDX23DocumentPackagesInner](#SBOMSPDX23DocumentPackagesInner_CommonObjectReference) |  |  |
| relationships |  |  | List of [SBOMSPDX23DocumentRelationshipsInner](#SBOMSPDX23DocumentRelationshipsInner_CommonObjectReference) |  |  |

<a id="SBOMSPDX23DocumentCreationInfo_CommonObjectReference"></a>

## SBOMSPDX23DocumentCreationInfo

| Field Name | Required | Nullable | Type             | Description | Format |
|------------|----------|----------|------------------|-------------|--------|
| created    |          |          | String           |             |        |
| creators   |          |          | List of `string` |             |        |

<a id="SBOMSPDX23DocumentPackagesInner_CommonObjectReference"></a>

## SBOMSPDX23DocumentPackagesInner

| Field Name            | Required | Nullable | Type    | Description | Format |
|-----------------------|----------|----------|---------|-------------|--------|
| SPDXID                |          |          | Object  |             |        |
| name                  |          |          | String  |             |        |
| versionInfo           |          |          | String  |             |        |
| packageFileName       |          |          | String  |             |        |
| downloadLocation      |          |          | String  |             |        |
| filesAnalyzed         |          |          | Boolean |             |        |
| primaryPackagePurpose |          |          | String  |             |        |

<a id="SBOMSPDX23DocumentRelationshipsInner_CommonObjectReference"></a>

## SBOMSPDX23DocumentRelationshipsInner

| Field Name         | Required | Nullable | Type   | Description | Format |
|--------------------|----------|----------|--------|-------------|--------|
| spdxElementId      |          |          | String |             |        |
| relatedSpdxElement |          |          | String |             |        |
| relationshipType   |          |          | String |             |        |

<a id="ScheduleDaysOfMonth_CommonObjectReference"></a>

## ScheduleDaysOfMonth

1 for 1st, 2 for 2nd …​. 31 for 31st

| Field Name | Required | Nullable | Type              | Description | Format |
|------------|----------|----------|-------------------|-------------|--------|
| days       |          |          | List of `integer` |             | int32  |

<a id="ScheduleDaysOfWeek_CommonObjectReference"></a>

## ScheduleDaysOfWeek

Sunday = 0, Monday = 1, …​. Saturday = 6

| Field Name | Required | Nullable | Type              | Description | Format |
|------------|----------|----------|-------------------|-------------|--------|
| days       |          |          | List of `integer` |             | int32  |

<a id="ScheduleIntervalType_CommonObjectReference"></a>

## ScheduleIntervalType

| Enum Values |
|-------------|
| UNSET       |
| DAILY       |
| WEEKLY      |
| MONTHLY     |

<a id="ScheduleWeeklyInterval_CommonObjectReference"></a>

## ScheduleWeeklyInterval

| Field Name | Required | Nullable | Type    | Description | Format |
|------------|----------|----------|---------|-------------|--------|
| day        |          |          | Integer |             | int32  |

<a id="ScopeImage_CommonObjectReference"></a>

## ScopeImage

| Field Name | Required | Nullable | Type   | Description | Format |
|------------|----------|----------|--------|-------------|--------|
| registry   |          |          | String |             |        |
| remote     |          |          | String |             |        |
| tag        |          |          | String |             |        |

<a id="SearchResponseCount_CommonObjectReference"></a>

## SearchResponseCount

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| category |  |  | [V1SearchCategory](#V1SearchCategory_CommonObjectReference) |  | SEARCH_UNSET, ALERTS, IMAGES, IMAGE_COMPONENTS, IMAGE_VULN_EDGE, IMAGE_COMPONENT_EDGE, POLICIES, DEPLOYMENTS, PODS, SECRETS, PROCESS_INDICATORS, COMPLIANCE, CLUSTERS, NAMESPACES, NODES, NODE_COMPONENTS, NODE_VULN_EDGE, NODE_COMPONENT_EDGE, NODE_COMPONENT_CVE_EDGE, COMPLIANCE_STANDARD, COMPLIANCE_CONTROL_GROUP, COMPLIANCE_CONTROL, SERVICE_ACCOUNTS, ROLES, ROLEBINDINGS, REPORT_CONFIGURATIONS, PROCESS_BASELINES, SUBJECTS, RISKS, VULNERABILITIES, CLUSTER_VULNERABILITIES, IMAGE_VULNERABILITIES, NODE_VULNERABILITIES, COMPONENT_VULN_EDGE, CLUSTER_VULN_EDGE, NETWORK_ENTITY, VULN_REQUEST, NETWORK_BASELINE, NETWORK_POLICIES, PROCESS_BASELINE_RESULTS, COMPLIANCE_METADATA, COMPLIANCE_RESULTS, COMPLIANCE_DOMAIN, CLUSTER_HEALTH, POLICY_CATEGORIES, IMAGE_INTEGRATIONS, COLLECTIONS, POLICY_CATEGORY_EDGE, PROCESS_LISTENING_ON_PORT, API_TOKEN, REPORT_METADATA, REPORT_SNAPSHOT, COMPLIANCE_INTEGRATIONS, COMPLIANCE_SCAN_CONFIG, COMPLIANCE_SCAN, COMPLIANCE_CHECK_RESULTS, BLOB, ADMINISTRATION_EVENTS, COMPLIANCE_SCAN_CONFIG_STATUS, ADMINISTRATION_USAGE, COMPLIANCE_PROFILES, COMPLIANCE_RULES, COMPLIANCE_SCAN_SETTING_BINDINGS, COMPLIANCE_SUITES, CLOUD_SOURCES, DISCOVERED_CLUSTERS, COMPLIANCE_REMEDIATIONS, COMPLIANCE_BENCHMARKS, AUTH_PROVIDERS, COMPLIANCE_REPORT_SNAPSHOT, IMAGE_COMPONENTS_V2, IMAGE_VULNERABILITIES_V2, IMAGES_V2, VIRTUAL_MACHINES, BASE_IMAGES, BASE_IMAGE_LAYERS, VIRTUAL_MACHINES_V2, VIRTUAL_MACHINE_SCANS_V2, VIRTUAL_MACHINE_COMPONENTS_V2, VIRTUAL_MACHINE_VULNERABILITIES_V2, IMAGE_CVE_INFOS, |
| count |  |  | String |  | int64 |

<a id="SearchResultMatches_CommonObjectReference"></a>

## SearchResultMatches

| Field Name | Required | Nullable | Type             | Description | Format |
|------------|----------|----------|------------------|-------------|--------|
| values     |          |          | List of `string` |             |        |

<a id="SeccompProfileProfileType_CommonObjectReference"></a>

## SeccompProfileProfileType

| Enum Values     |
|-----------------|
| UNCONFINED      |
| RUNTIME_DEFAULT |
| LOCALHOST       |

<a id="SecurityContextSELinux_CommonObjectReference"></a>

## SecurityContextSELinux

| Field Name | Required | Nullable | Type   | Description | Format |
|------------|----------|----------|--------|-------------|--------|
| user       |          |          | String |             |        |
| role       |          |          | String |             |        |
| type       |          |          | String |             |        |
| level      |          |          | String |             |        |

<a id="SecurityContextSeccompProfile_CommonObjectReference"></a>

## SecurityContextSeccompProfile

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| type |  |  | [SeccompProfileProfileType](#SeccompProfileProfileType_CommonObjectReference) |  | UNCONFINED, RUNTIME_DEFAULT, LOCALHOST, |
| localhostProfile |  |  | String |  |  |

<a id="SetBasedLabelSelectorOperator_CommonObjectReference"></a>

## SetBasedLabelSelectorOperator

| Enum Values |
|-------------|
| UNKNOWN     |
| IN          |
| NOT_IN      |
| EXISTS      |
| NOT_EXISTS  |

<a id="SetBasedLabelSelectorRequirement_CommonObjectReference"></a>

## SetBasedLabelSelectorRequirement

Next available tag: 4

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| key |  |  | String |  |  |
| op |  |  | [SetBasedLabelSelectorOperator](#SetBasedLabelSelectorOperator_CommonObjectReference) |  | UNKNOWN, IN, NOT_IN, EXISTS, NOT_EXISTS, |
| values |  |  | List of `string` |  |  |

<a id="SignatureIntegrationServicePutSignatureIntegrationBody_CommonObjectReference"></a>

## SignatureIntegrationServicePutSignatureIntegrationBody

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| name |  |  | String |  |  |
| cosign |  |  | [StorageCosignPublicKeyVerification](#StorageCosignPublicKeyVerification_CommonObjectReference) |  |  |
| cosignCertificates |  |  | List of [StorageCosignCertificateVerification](#StorageCosignCertificateVerification_CommonObjectReference) |  |  |
| transparencyLog |  |  | [StorageTransparencyLogVerification](#StorageTransparencyLogVerification_CommonObjectReference) |  |  |
| traits |  |  | [StorageTraits](#StorageTraits_CommonObjectReference) |  |  |

<a id="SimpleAccessScopeRules_CommonObjectReference"></a>

## SimpleAccessScopeRules

Each element of any repeated field is an individual rule. Rules are joined by logical OR: if there exists a rule allowing resource `x`, `x` is in the access scope.

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| includedClusterIds |  |  | List of `string` | included_cluster_ids contains a list of clusters to which full access is granted, identified by their IDs. |  |
| includedClusters |  |  | List of `string` | included_clusters contains a list of clusters to which full access is granted, identified by their names. |  |
| includedNamespaces |  |  | List of [SimpleAccessScopeRulesNamespace](#SimpleAccessScopeRulesNamespace_CommonObjectReference) |  |  |
| clusterLabelSelectors |  |  | List of [StorageSetBasedLabelSelector](#StorageSetBasedLabelSelector_CommonObjectReference) |  |  |
| namespaceLabelSelectors |  |  | List of [StorageSetBasedLabelSelector](#StorageSetBasedLabelSelector_CommonObjectReference) |  |  |

<a id="SimpleAccessScopeRulesNamespace_CommonObjectReference"></a>

## SimpleAccessScopeRulesNamespace

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| clusterId |  |  | String | The namespace field and at least one cluster field must be set. The cluster ID takes precedence over the cluster name when a cluster with that ID exists. |  |
| clusterName |  |  | String |  |  |
| namespaceName |  |  | String |  |  |

<a id="StorageAWSProviderMetadata_CommonObjectReference"></a>

## StorageAWSProviderMetadata

| Field Name | Required | Nullable | Type   | Description | Format |
|------------|----------|----------|--------|-------------|--------|
| accountId  |          |          | String |             |        |

<a id="StorageAWSSecurityHub_CommonObjectReference"></a>

## StorageAWSSecurityHub

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| region |  |  | String |  |  |
| credentials |  |  | [StorageAWSSecurityHubCredentials](#StorageAWSSecurityHubCredentials_CommonObjectReference) |  |  |
| accountId |  |  | String |  |  |

<a id="StorageAWSSecurityHubCredentials_CommonObjectReference"></a>

## StorageAWSSecurityHubCredentials

| Field Name      | Required | Nullable | Type    | Description | Format |
|-----------------|----------|----------|---------|-------------|--------|
| accessKeyId     |          |          | String  |             |        |
| secretAccessKey |          |          | String  |             |        |
| stsEnabled      |          |          | Boolean |             |        |

<a id="StorageAccess_CommonObjectReference"></a>

## StorageAccess

| Enum Values       |
|-------------------|
| NO_ACCESS         |
| READ_ACCESS       |
| READ_WRITE_ACCESS |

<a id="StorageAdministrationEventsConfig_CommonObjectReference"></a>

## StorageAdministrationEventsConfig

| Field Name            | Required | Nullable | Type | Description | Format |
|-----------------------|----------|----------|------|-------------|--------|
| retentionDurationDays |          |          | Long |             | int64  |

<a id="StorageAdmissionControlHealthInfo_CommonObjectReference"></a>

## StorageAdmissionControlHealthInfo

AdmissionControlHealthInfo carries data about admission control deployment but does not include admission control health status derived from this data. Aggregated admission control health status is not included because it is derived in central and not in the component that first reports AdmissionControlHealthInfo (sensor).

The following fields are made optional/nullable because there can be errors when trying to obtain them and the default value of 0 might be confusing with the actual value 0. In case an error happens when trying to obtain a certain field, it will be absent (instead of having the default value).

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| totalDesiredPods |  |  | Integer |  | int32 |
| totalReadyPods |  |  | Integer |  | int32 |
| statusErrors |  |  | List of `string` | Collection of errors that occurred while trying to obtain admission control health info. |  |

<a id="StorageAdmissionControllerConfig_CommonObjectReference"></a>

## StorageAdmissionControllerConfig

| Field Name       | Required | Nullable | Type    | Description | Format |
|------------------|----------|----------|---------|-------------|--------|
| enabled          |          |          | Boolean |             |        |
| timeoutSeconds   |          |          | Integer |             | int32  |
| scanInline       |          |          | Boolean |             |        |
| disableBypass    |          |          | Boolean |             |        |
| enforceOnUpdates |          |          | Boolean |             |        |

<a id="StorageAdvisory_CommonObjectReference"></a>

## StorageAdvisory

| Field Name | Required | Nullable | Type   | Description | Format |
|------------|----------|----------|--------|-------------|--------|
| name       |          |          | String |             |        |
| link       |          |          | String |             |        |

<a id="StorageAlert_CommonObjectReference"></a>

## StorageAlert

Next available tag: 26

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| id |  |  | String |  |  |
| policy |  |  | [StoragePolicy](#StoragePolicy_CommonObjectReference) |  |  |
| lifecycleStage |  |  | [StorageLifecycleStage](#StorageLifecycleStage_CommonObjectReference) |  | DEPLOY, BUILD, RUNTIME, |
| clusterId |  |  | String |  |  |
| clusterName |  |  | String |  |  |
| namespace |  |  | String |  |  |
| namespaceId |  |  | String |  |  |
| deployment |  |  | [StorageAlertDeployment](#StorageAlertDeployment_CommonObjectReference) |  |  |
| image |  |  | [StorageContainerImage](#StorageContainerImage_CommonObjectReference) |  |  |
| resource |  |  | [StorageAlertResource](#StorageAlertResource_CommonObjectReference) |  |  |
| node |  |  | [AlertNode](#AlertNode_CommonObjectReference) |  |  |
| violations |  |  | List of [AlertViolation](#AlertViolation_CommonObjectReference) | For run-time phase alert, a maximum of 40 violations are retained. |  |
| processViolation |  |  | [AlertProcessViolation](#AlertProcessViolation_CommonObjectReference) |  |  |
| enforcement |  |  | [AlertEnforcement](#AlertEnforcement_CommonObjectReference) |  |  |
| time |  |  | Date |  | date-time |
| firstOccurred |  |  | Date |  | date-time |
| resolvedAt |  |  | Date | The time at which the alert was resolved. Only set if ViolationState is RESOLVED. | date-time |
| state |  |  | [StorageViolationState](#StorageViolationState_CommonObjectReference) |  | ACTIVE, RESOLVED, ATTEMPTED, |
| platformComponent |  |  | Boolean |  |  |
| entityType |  |  | [AlertEntityType](#AlertEntityType_CommonObjectReference) |  | UNSET, DEPLOYMENT, CONTAINER_IMAGE, RESOURCE, NODE, |
| enforcementCount |  |  | Integer | Cached enforcement count, computed on upsert. For RUNTIME+KILL_POD alerts this is the number of unique pods killed. For DEPLOY alerts with enforcement this is 1. Avoids deserializing the full alert blob for ListAlert queries. | int32 |

<a id="StorageAlertDeployment_CommonObjectReference"></a>

## StorageAlertDeployment

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| id |  |  | String |  |  |
| name |  |  | String |  |  |
| type |  |  | String |  |  |
| namespace |  |  | String | This field has to be duplicated in Alert for scope management and search. |  |
| namespaceId |  |  | String | This field has to be duplicated in Alert for scope management and search. |  |
| labels |  |  | Map of `string` |  |  |
| clusterId |  |  | String | This field has to be duplicated in Alert for scope management and search. |  |
| clusterName |  |  | String | This field has to be duplicated in Alert for scope management and search. |  |
| containers |  |  | List of [AlertDeploymentContainer](#AlertDeploymentContainer_CommonObjectReference) |  |  |
| annotations |  |  | Map of `string` |  |  |
| inactive |  |  | Boolean |  |  |

<a id="StorageAlertResource_CommonObjectReference"></a>

## StorageAlertResource

Represents an alert on a kubernetes resource other than a deployment (configmaps, secrets, etc.)

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| resourceType |  |  | [ResourceResourceType](#ResourceResourceType_CommonObjectReference) |  | UNKNOWN, SECRETS, CONFIGMAPS, CLUSTER_ROLES, CLUSTER_ROLE_BINDINGS, NETWORK_POLICIES, SECURITY_CONTEXT_CONSTRAINTS, EGRESS_FIREWALLS, |
| name |  |  | String |  |  |
| clusterId |  |  | String | This field has to be duplicated in Alert for scope management and search. |  |
| clusterName |  |  | String | This field has to be duplicated in Alert for scope management and search. |  |
| namespace |  |  | String | This field has to be duplicated in Alert for scope management and search. |  |
| namespaceId |  |  | String | This field has to be duplicated in Alert for scope management and search. |  |

<a id="StorageAlertRetentionConfig_CommonObjectReference"></a>

## StorageAlertRetentionConfig

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| resolvedDeployRetentionDurationDays |  |  | Integer |  | int32 |
| deletedRuntimeRetentionDurationDays |  |  | Integer | This runtime alert retention configuration takes precedence after `allRuntimeRetentionDurationDays`. | int32 |
| allRuntimeRetentionDurationDays |  |  | Integer | This runtime alert retention configuration has highest precedence. All runtime alerts, including attempted alerts and deleted deployment alerts, are deleted even if respective retention is longer. | int32 |
| attemptedDeployRetentionDurationDays |  |  | Integer |  | int32 |
| attemptedRuntimeRetentionDurationDays |  |  | Integer | This runtime alert retention configuration has lowest precedence. | int32 |

<a id="StorageAuditLogFileState_CommonObjectReference"></a>

## StorageAuditLogFileState

AuditLogFileState tracks the last audit log event timestamp and ID that was collected by Compliance For internal use only

| Field Name       | Required | Nullable | Type   | Description | Format    |
|------------------|----------|----------|--------|-------------|-----------|
| collectLogsSince |          |          | Date   |             | date-time |
| lastAuditId      |          |          | String |             |           |

<a id="StorageAuthProvider_CommonObjectReference"></a>

## StorageAuthProvider

Next Tag: 15.

<table id="Fields-StorageAuthProvider_CommonObjectReference">
<colgroup>
<col style="width: 18%" />
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 18%" />
<col style="width: 36%" />
<col style="width: 9%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Field Name</th>
<th style="text-align: left;">Required</th>
<th style="text-align: left;">Nullable</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Description</th>
<th style="text-align: left;">Format</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>id</p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><p>String</p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><p>name</p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><p>String</p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><p>type</p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><p>String</p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><p>uiEndpoint</p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><p>String</p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><p>enabled</p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><p>Boolean</p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><p>config</p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><p>Map of <code>string</code></p></td>
<td style="text-align: left;"><p>Config holds auth provider specific configuration. Each configuration options are different based on the given auth provider type.</p>
<p>OIDC:</p>
<ul>
<li><p>"issuer": the OIDC issuer according to <a href="https://openid.net/specs/openid-connect-core-1_0.html#IssuerIdentifier">https://openid.net/specs/openid-connect-core-1_0.html#IssuerIdentifier</a>.</p></li>
<li><p>"client_id": the client ID according to <a href="https://www.rfc-editor.org/rfc/rfc6749.html#section-2.2">https://www.rfc-editor.org/rfc/rfc6749.html#section-2.2</a>.</p></li>
<li><p>"client_secret": the client secret according to <a href="https://www.rfc-editor.org/rfc/rfc6749.html#section-2.3.1">https://www.rfc-editor.org/rfc/rfc6749.html#section-2.3.1</a>.</p></li>
<li><p>"do_not_use_client_secret": set to "true" if you want to create a configuration with only a client ID and no client secret.</p></li>
<li><p>"mode": the OIDC callback mode, choosing from "fragment", "post", or "query".</p></li>
<li><p>"disable_offline_access_scope": set to "true" if no offline tokens shall be issued.</p></li>
<li><p>"extra_scopes": a space-delimited string of additional scopes to request in addition to "openid profile email" according to <a href="https://www.rfc-editor.org/rfc/rfc6749.html#section-3.3">https://www.rfc-editor.org/rfc/rfc6749.html#section-3.3</a>.</p></li>
</ul>
<p>OpenShift Auth: supports no extra configuration options.</p>
<p>User PKI:</p>
<ul>
<li><p>"keys": the trusted certificates PEM encoded.</p></li>
</ul>
<p>SAML:</p>
<ul>
<li><p>"sp_issuer": the service provider issuer according to <a href="https://datatracker.ietf.org/doc/html/rfc7522#section-3">https://datatracker.ietf.org/doc/html/rfc7522#section-3</a>.</p></li>
<li><p>"idp_metadata_url": the metadata URL according to <a href="https://docs.oasis-open.org/security/saml/v2.0/saml-metadata-2.0-os.pdf">https://docs.oasis-open.org/security/saml/v2.0/saml-metadata-2.0-os.pdf</a>.</p></li>
<li><p>"idp_issuer": the IdP issuer.</p></li>
<li><p>"idp_cert_pem": the cert PEM encoded for the IdP endpoint.</p></li>
<li><p>"idp_sso_url": the IdP SSO URL.</p></li>
<li><p>"idp_nameid_format": the IdP name ID format.</p></li>
</ul>
<p>IAP:</p>
<ul>
<li><p>"audience": the audience to use.</p></li>
</ul></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><p>loginUrl</p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><p>String</p></td>
<td style="text-align: left;"><p>The login URL will be provided by the backend, and may not be specified in a request.</p></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><p>validated</p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><p>Boolean</p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><p>extraUiEndpoints</p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><p>List of <code>string</code></p></td>
<td style="text-align: left;"><p>UI endpoints which to allow in addition to <code>ui_endpoint</code>. I.e., if a login request is coming from any of these, the auth request will use these for the callback URL, not ui_endpoint.</p></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><p>active</p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><p>Boolean</p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><p>requiredAttributes</p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><p>List of <a href="#AuthProviderRequiredAttribute_CommonObjectReference">AuthProviderRequiredAttribute</a></p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><p>traits</p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><p><a href="#StorageTraits_CommonObjectReference">StorageTraits</a></p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><p>claimMappings</p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><p>Map of <code>string</code></p></td>
<td style="text-align: left;"><p>Specifies claims from IdP token that will be copied to Rox token attributes. Each key in this map contains a path in IdP token we want to map. Path is separated by "." symbol.</p>
<p>For example, if IdP token payload looks like:</p>
<div class="sourceCode" id="cb1"><pre class="sourceCode json"><code class="sourceCode json"><span id="cb1-1"><a data-unavailable-reference="true" aria-hidden="true" tabindex="-1"></a><span class="fu">{</span></span>
<span id="cb1-2"><a data-unavailable-reference="true" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;a&quot;</span><span class="fu">:</span> <span class="fu">{</span></span>
<span id="cb1-3"><a data-unavailable-reference="true" aria-hidden="true" tabindex="-1"></a>        <span class="dt">&quot;b&quot;</span> <span class="fu">:</span> <span class="st">&quot;c&quot;</span><span class="fu">,</span></span>
<span id="cb1-4"><a data-unavailable-reference="true" aria-hidden="true" tabindex="-1"></a>        <span class="dt">&quot;d&quot;</span><span class="fu">:</span> <span class="kw">true</span><span class="fu">,</span></span>
<span id="cb1-5"><a data-unavailable-reference="true" aria-hidden="true" tabindex="-1"></a>        <span class="dt">&quot;e&quot;</span><span class="fu">:</span> <span class="ot">[</span> <span class="st">&quot;val1&quot;</span><span class="ot">,</span> <span class="st">&quot;val2&quot;</span><span class="ot">,</span> <span class="st">&quot;val3&quot;</span> <span class="ot">]</span><span class="fu">,</span></span>
<span id="cb1-6"><a data-unavailable-reference="true" aria-hidden="true" tabindex="-1"></a>        <span class="dt">&quot;f&quot;</span><span class="fu">:</span> <span class="ot">[</span> <span class="kw">true</span><span class="ot">,</span> <span class="kw">false</span><span class="ot">,</span> <span class="kw">false</span> <span class="ot">]</span><span class="fu">,</span></span>
<span id="cb1-7"><a data-unavailable-reference="true" aria-hidden="true" tabindex="-1"></a>        <span class="dt">&quot;g&quot;</span><span class="fu">:</span> <span class="fl">123.0</span><span class="fu">,</span></span>
<span id="cb1-8"><a data-unavailable-reference="true" aria-hidden="true" tabindex="-1"></a>        <span class="dt">&quot;h&quot;</span><span class="fu">:</span> <span class="ot">[</span> <span class="dv">1</span><span class="ot">,</span> <span class="dv">2</span><span class="ot">,</span> <span class="dv">3</span><span class="ot">]</span></span>
<span id="cb1-9"><a data-unavailable-reference="true" aria-hidden="true" tabindex="-1"></a>    <span class="fu">}</span></span>
<span id="cb1-10"><a data-unavailable-reference="true" aria-hidden="true" tabindex="-1"></a><span class="fu">}</span></span></code></pre></div>
<p>then "a.b" would be a valid key and "a.z" is not.</p>
<p>We support the following types of claims:</p>
<ul>
<li><p>string(path "a.b")</p></li>
<li><p>bool(path "a.d")</p></li>
<li><p>string array(path "a.e")</p></li>
<li><p>bool array (path "a.f.")</p></li>
</ul>
<p>We do NOT support the following types of claims:</p>
<ul>
<li><p>complex claims(path "a")</p></li>
<li><p>float/integer claims(path "a.g")</p></li>
<li><p>float/integer array claims(path "a.h")</p></li>
</ul>
<p>Each value in this map contains a Rox token attribute name we want to add claim to. If, for example, value is "groups", claim would be found in "external_user.Attributes.groups" in token.</p>
<p>Note: we only support this feature for OIDC auth provider.</p></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><p>lastUpdated</p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><p>Date</p></td>
<td style="text-align: left;"><p>Last updated indicates the last time the auth provider has been updated. In case there have been tokens issued by an auth provider <em>before</em> this timestamp, they will be considered invalid. Subsequently, all clients will have to re-issue their tokens (either by refreshing or by an additional login attempt).</p></td>
<td style="text-align: left;"><p>date-time</p></td>
</tr>
</tbody>
</table>

<a id="StorageAutoLockProcessBaselinesConfig_CommonObjectReference"></a>

## StorageAutoLockProcessBaselinesConfig

| Field Name | Required | Nullable | Type    | Description | Format |
|------------|----------|----------|---------|-------------|--------|
| enabled    |          |          | Boolean |             |        |

<a id="StorageAzureConfig_CommonObjectReference"></a>

## StorageAzureConfig

Azure container registry configuration. Used by integrations of type "azure".

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| endpoint |  |  | String |  |  |
| username |  |  | String |  |  |
| password |  |  | String | The password for the integration. The server will mask the value of this credential in responses and logs. |  |
| wifEnabled |  |  | Boolean | Enables authentication with short-lived tokens using Azure managed identities or Azure workload identities. |  |

<a id="StorageAzureProviderMetadata_CommonObjectReference"></a>

## StorageAzureProviderMetadata

| Field Name     | Required | Nullable | Type   | Description | Format |
|----------------|----------|----------|--------|-------------|--------|
| subscriptionId |          |          | String |             |        |

<a id="StorageBackupInfo_CommonObjectReference"></a>

## StorageBackupInfo

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| backupLastRunAt |  |  | Date |  | date-time |
| status |  |  | [StorageOperationStatus](#StorageOperationStatus_CommonObjectReference) |  | FAIL, PASS, |
| requestor |  |  | [StorageSlimUser](#StorageSlimUser_CommonObjectReference) |  |  |

<a id="StorageBannerConfig_CommonObjectReference"></a>

## StorageBannerConfig

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| enabled |  |  | Boolean |  |  |
| text |  |  | String |  |  |
| size |  |  | [BannerConfigSize](#BannerConfigSize_CommonObjectReference) |  | UNSET, SMALL, MEDIUM, LARGE, |
| color |  |  | String |  |  |
| backgroundColor |  |  | String |  |  |

<a id="StorageBaseImageInfo_CommonObjectReference"></a>

## StorageBaseImageInfo

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| baseImageId |  |  | String |  |  |
| baseImageFullName |  |  | String |  |  |
| baseImageDigest |  |  | String |  |  |
| created |  |  | Date |  | date-time |
| maxLayerIndex |  |  | Integer | Index of the last base image layer, taking into account "empty layers" (aka. metadata history without SHA). | int32 |

<a id="StorageBaselineElement_CommonObjectReference"></a>

## StorageBaselineElement

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| element |  |  | [StorageBaselineItem](#StorageBaselineItem_CommonObjectReference) |  |  |
| auto |  |  | Boolean |  |  |

<a id="StorageBaselineItem_CommonObjectReference"></a>

## StorageBaselineItem

| Field Name  | Required | Nullable | Type   | Description | Format |
|-------------|----------|----------|--------|-------------|--------|
| processName |          |          | String |             |        |

<a id="StorageBooleanOperator_CommonObjectReference"></a>

## StorageBooleanOperator

| Enum Values |
|-------------|
| OR          |
| AND         |

<a id="StorageCSCC_CommonObjectReference"></a>

## StorageCSCC

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| serviceAccount |  |  | String | The service account for the integration. The server will mask the value of this credential in responses and logs. |  |
| sourceId |  |  | String |  |  |
| wifEnabled |  |  | Boolean |  |  |

<a id="StorageCVEInfo_CommonObjectReference"></a>

## StorageCVEInfo

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| cve |  |  | String |  |  |
| summary |  |  | String |  |  |
| link |  |  | String |  |  |
| publishedOn |  |  | Date | This indicates the timestamp when the cve was first published in the cve feeds. | date-time |
| createdAt |  |  | Date | Time when the CVE was first seen in the system. | date-time |
| lastModified |  |  | Date |  | date-time |
| scoreVersion |  |  | [StorageCVEInfoScoreVersion](#StorageCVEInfoScoreVersion_CommonObjectReference) |  | V2, V3, UNKNOWN, |
| cvssV2 |  |  | [StorageCVSSV2](#StorageCVSSV2_CommonObjectReference) |  |  |
| cvssV3 |  |  | [StorageCVSSV3](#StorageCVSSV3_CommonObjectReference) |  |  |
| references |  |  | List of [CVEInfoReference](#CVEInfoReference_CommonObjectReference) |  |  |
| cvssMetrics |  |  | List of [StorageCVSSScore](#StorageCVSSScore_CommonObjectReference) |  |  |
| epss |  |  | [StorageEPSS](#StorageEPSS_CommonObjectReference) |  |  |

<a id="StorageCVEInfoScoreVersion_CommonObjectReference"></a>

## StorageCVEInfoScoreVersion

ScoreVersion can be deprecated ROX-26066

- V2: No unset for automatic backwards compatibility

| Enum Values |
|-------------|
| V2          |
| V3          |
| UNKNOWN     |

<a id="StorageCVSSScore_CommonObjectReference"></a>

## StorageCVSSScore

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| source |  |  | [StorageSource](#StorageSource_CommonObjectReference) |  | SOURCE_UNKNOWN, SOURCE_RED_HAT, SOURCE_OSV, SOURCE_NVD, |
| url |  |  | String |  |  |
| cvssv2 |  |  | [StorageCVSSV2](#StorageCVSSV2_CommonObjectReference) |  |  |
| cvssv3 |  |  | [StorageCVSSV3](#StorageCVSSV3_CommonObjectReference) |  |  |

<a id="StorageCVSSV2_CommonObjectReference"></a>

## StorageCVSSV2

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| vector |  |  | String |  |  |
| attackVector |  |  | [StorageCVSSV2AttackVector](#StorageCVSSV2AttackVector_CommonObjectReference) |  | ATTACK_LOCAL, ATTACK_ADJACENT, ATTACK_NETWORK, |
| accessComplexity |  |  | [CVSSV2AccessComplexity](#CVSSV2AccessComplexity_CommonObjectReference) |  | ACCESS_HIGH, ACCESS_MEDIUM, ACCESS_LOW, |
| authentication |  |  | [CVSSV2Authentication](#CVSSV2Authentication_CommonObjectReference) |  | AUTH_MULTIPLE, AUTH_SINGLE, AUTH_NONE, |
| confidentiality |  |  | [StorageCVSSV2Impact](#StorageCVSSV2Impact_CommonObjectReference) |  | IMPACT_NONE, IMPACT_PARTIAL, IMPACT_COMPLETE, |
| integrity |  |  | [StorageCVSSV2Impact](#StorageCVSSV2Impact_CommonObjectReference) |  | IMPACT_NONE, IMPACT_PARTIAL, IMPACT_COMPLETE, |
| availability |  |  | [StorageCVSSV2Impact](#StorageCVSSV2Impact_CommonObjectReference) |  | IMPACT_NONE, IMPACT_PARTIAL, IMPACT_COMPLETE, |
| exploitabilityScore |  |  | Float |  | float |
| impactScore |  |  | Float |  | float |
| score |  |  | Float |  | float |
| severity |  |  | [StorageCVSSV2Severity](#StorageCVSSV2Severity_CommonObjectReference) |  | UNKNOWN, LOW, MEDIUM, HIGH, |

<a id="StorageCVSSV2AttackVector_CommonObjectReference"></a>

## StorageCVSSV2AttackVector

| Enum Values     |
|-----------------|
| ATTACK_LOCAL    |
| ATTACK_ADJACENT |
| ATTACK_NETWORK  |

<a id="StorageCVSSV2Impact_CommonObjectReference"></a>

## StorageCVSSV2Impact

| Enum Values     |
|-----------------|
| IMPACT_NONE     |
| IMPACT_PARTIAL  |
| IMPACT_COMPLETE |

<a id="StorageCVSSV2Severity_CommonObjectReference"></a>

## StorageCVSSV2Severity

| Enum Values |
|-------------|
| UNKNOWN     |
| LOW         |
| MEDIUM      |
| HIGH        |

<a id="StorageCVSSV3_CommonObjectReference"></a>

## StorageCVSSV3

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| vector |  |  | String |  |  |
| exploitabilityScore |  |  | Float |  | float |
| impactScore |  |  | Float |  | float |
| attackVector |  |  | [StorageCVSSV3AttackVector](#StorageCVSSV3AttackVector_CommonObjectReference) |  | ATTACK_LOCAL, ATTACK_ADJACENT, ATTACK_NETWORK, ATTACK_PHYSICAL, |
| attackComplexity |  |  | [CVSSV3Complexity](#CVSSV3Complexity_CommonObjectReference) |  | COMPLEXITY_LOW, COMPLEXITY_HIGH, |
| privilegesRequired |  |  | [CVSSV3Privileges](#CVSSV3Privileges_CommonObjectReference) |  | PRIVILEGE_NONE, PRIVILEGE_LOW, PRIVILEGE_HIGH, |
| userInteraction |  |  | [CVSSV3UserInteraction](#CVSSV3UserInteraction_CommonObjectReference) |  | UI_NONE, UI_REQUIRED, |
| scope |  |  | [StorageCVSSV3Scope](#StorageCVSSV3Scope_CommonObjectReference) |  | UNCHANGED, CHANGED, |
| confidentiality |  |  | [StorageCVSSV3Impact](#StorageCVSSV3Impact_CommonObjectReference) |  | IMPACT_NONE, IMPACT_LOW, IMPACT_HIGH, |
| integrity |  |  | [StorageCVSSV3Impact](#StorageCVSSV3Impact_CommonObjectReference) |  | IMPACT_NONE, IMPACT_LOW, IMPACT_HIGH, |
| availability |  |  | [StorageCVSSV3Impact](#StorageCVSSV3Impact_CommonObjectReference) |  | IMPACT_NONE, IMPACT_LOW, IMPACT_HIGH, |
| score |  |  | Float |  | float |
| severity |  |  | [StorageCVSSV3Severity](#StorageCVSSV3Severity_CommonObjectReference) |  | UNKNOWN, NONE, LOW, MEDIUM, HIGH, CRITICAL, |

<a id="StorageCVSSV3AttackVector_CommonObjectReference"></a>

## StorageCVSSV3AttackVector

| Enum Values     |
|-----------------|
| ATTACK_LOCAL    |
| ATTACK_ADJACENT |
| ATTACK_NETWORK  |
| ATTACK_PHYSICAL |

<a id="StorageCVSSV3Impact_CommonObjectReference"></a>

## StorageCVSSV3Impact

| Enum Values |
|-------------|
| IMPACT_NONE |
| IMPACT_LOW  |
| IMPACT_HIGH |

<a id="StorageCVSSV3Scope_CommonObjectReference"></a>

## StorageCVSSV3Scope

| Enum Values |
|-------------|
| UNCHANGED   |
| CHANGED     |

<a id="StorageCVSSV3Severity_CommonObjectReference"></a>

## StorageCVSSV3Severity

| Enum Values |
|-------------|
| UNKNOWN     |
| NONE        |
| LOW         |
| MEDIUM      |
| HIGH        |
| CRITICAL    |

<a id="StorageCert_CommonObjectReference"></a>

## StorageCert

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| subject |  |  | [StorageCertName](#StorageCertName_CommonObjectReference) |  |  |
| issuer |  |  | [StorageCertName](#StorageCertName_CommonObjectReference) |  |  |
| sans |  |  | List of `string` |  |  |
| startDate |  |  | Date |  | date-time |
| endDate |  |  | Date |  | date-time |
| algorithm |  |  | String |  |  |

<a id="StorageCertName_CommonObjectReference"></a>

## StorageCertName

| Field Name       | Required | Nullable | Type             | Description | Format |
|------------------|----------|----------|------------------|-------------|--------|
| commonName       |          |          | String           |             |        |
| country          |          |          | String           |             |        |
| organization     |          |          | String           |             |        |
| organizationUnit |          |          | String           |             |        |
| locality         |          |          | String           |             |        |
| province         |          |          | String           |             |        |
| streetAddress    |          |          | String           |             |        |
| postalCode       |          |          | String           |             |        |
| names            |          |          | List of `string` |             |        |

<a id="StorageCertificateTransparencyLogVerification_CommonObjectReference"></a>

## StorageCertificateTransparencyLogVerification

Validate that the signature certificate contains a signed certificate timestamp as proof of inclusion into the certificate transparency log.

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| enabled |  |  | Boolean | Validate the inclusion of certificates into a certificate transparency log. Disables validation if not enabled. |  |
| publicKeyPemEnc |  |  | String | PEM encoded public key used to validate the proof of inclusion into the certificate transparency log. Defaults to the key of the public Sigstore instance if left empty. |  |

<a id="StorageClairConfig_CommonObjectReference"></a>

## StorageClairConfig

| Field Name | Required | Nullable | Type    | Description | Format |
|------------|----------|----------|---------|-------------|--------|
| endpoint   |          |          | String  |             |        |
| insecure   |          |          | Boolean |             |        |

<a id="StorageClairV4Config_CommonObjectReference"></a>

## StorageClairV4Config

| Field Name | Required | Nullable | Type    | Description | Format |
|------------|----------|----------|---------|-------------|--------|
| endpoint   |          |          | String  |             |        |
| insecure   |          |          | Boolean |             |        |

<a id="StorageClairifyConfig_CommonObjectReference"></a>

## StorageClairifyConfig

| Field Name         | Required | Nullable | Type    | Description | Format |
|--------------------|----------|----------|---------|-------------|--------|
| endpoint           |          |          | String  |             |        |
| grpcEndpoint       |          |          | String  |             |        |
| numConcurrentScans |          |          | Integer |             | int32  |

<a id="StorageCluster_CommonObjectReference"></a>

## StorageCluster

Next tag: 33

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| id |  |  | String |  |  |
| name |  |  | String |  |  |
| type |  |  | [StorageClusterType](#StorageClusterType_CommonObjectReference) |  | GENERIC_CLUSTER, KUBERNETES_CLUSTER, OPENSHIFT_CLUSTER, OPENSHIFT4_CLUSTER, |
| labels |  |  | Map of `string` |  |  |
| mainImage |  |  | String |  |  |
| collectorImage |  |  | String |  |  |
| centralApiEndpoint |  |  | String |  |  |
| runtimeSupport |  |  | Boolean |  |  |
| collectionMethod |  |  | [StorageCollectionMethod](#StorageCollectionMethod_CommonObjectReference) |  | UNSET_COLLECTION, NO_COLLECTION, KERNEL_MODULE, EBPF, CORE_BPF, |
| admissionController |  |  | Boolean |  |  |
| admissionControllerUpdates |  |  | Boolean |  |  |
| admissionControllerEvents |  |  | Boolean |  |  |
| status |  |  | [StorageClusterStatus](#StorageClusterStatus_CommonObjectReference) |  |  |
| dynamicConfig |  |  | [StorageDynamicClusterConfig](#StorageDynamicClusterConfig_CommonObjectReference) |  |  |
| tolerationsConfig |  |  | [StorageTolerationsConfig](#StorageTolerationsConfig_CommonObjectReference) |  |  |
| priority |  |  | String |  | int64 |
| healthStatus |  |  | [StorageClusterHealthStatus](#StorageClusterHealthStatus_CommonObjectReference) |  |  |
| slimCollector |  |  | Boolean |  |  |
| helmConfig |  |  | [StorageCompleteClusterConfig](#StorageCompleteClusterConfig_CommonObjectReference) |  |  |
| mostRecentSensorId |  |  | [StorageSensorDeploymentIdentification](#StorageSensorDeploymentIdentification_CommonObjectReference) |  |  |
| auditLogState |  |  | Map of [StorageAuditLogFileState](#StorageAuditLogFileState_CommonObjectReference) | For internal use only. |  |
| initBundleId |  |  | String |  |  |
| managedBy |  |  | [StorageManagerType](#StorageManagerType_CommonObjectReference) |  | MANAGER_TYPE_UNKNOWN, MANAGER_TYPE_MANUAL, MANAGER_TYPE_HELM_CHART, MANAGER_TYPE_KUBERNETES_OPERATOR, |
| sensorCapabilities |  |  | List of `string` |  |  |
| admissionControllerFailOnError |  |  | Boolean |  |  |

<a id="StorageClusterCertExpiryStatus_CommonObjectReference"></a>

## StorageClusterCertExpiryStatus

| Field Name          | Required | Nullable | Type | Description | Format    |
|---------------------|----------|----------|------|-------------|-----------|
| sensorCertExpiry    |          |          | Date |             | date-time |
| sensorCertNotBefore |          |          | Date |             | date-time |

<a id="StorageClusterHealthStatus_CommonObjectReference"></a>

## StorageClusterHealthStatus

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| id |  |  | String |  |  |
| collectorHealthInfo |  |  | [StorageCollectorHealthInfo](#StorageCollectorHealthInfo_CommonObjectReference) |  |  |
| admissionControlHealthInfo |  |  | [StorageAdmissionControlHealthInfo](#StorageAdmissionControlHealthInfo_CommonObjectReference) |  |  |
| scannerHealthInfo |  |  | [StorageScannerHealthInfo](#StorageScannerHealthInfo_CommonObjectReference) |  |  |
| sensorHealthStatus |  |  | [ClusterHealthStatusHealthStatusLabel](#ClusterHealthStatusHealthStatusLabel_CommonObjectReference) |  | UNINITIALIZED, UNAVAILABLE, UNHEALTHY, DEGRADED, HEALTHY, |
| collectorHealthStatus |  |  | [ClusterHealthStatusHealthStatusLabel](#ClusterHealthStatusHealthStatusLabel_CommonObjectReference) |  | UNINITIALIZED, UNAVAILABLE, UNHEALTHY, DEGRADED, HEALTHY, |
| overallHealthStatus |  |  | [ClusterHealthStatusHealthStatusLabel](#ClusterHealthStatusHealthStatusLabel_CommonObjectReference) |  | UNINITIALIZED, UNAVAILABLE, UNHEALTHY, DEGRADED, HEALTHY, |
| admissionControlHealthStatus |  |  | [ClusterHealthStatusHealthStatusLabel](#ClusterHealthStatusHealthStatusLabel_CommonObjectReference) |  | UNINITIALIZED, UNAVAILABLE, UNHEALTHY, DEGRADED, HEALTHY, |
| scannerHealthStatus |  |  | [ClusterHealthStatusHealthStatusLabel](#ClusterHealthStatusHealthStatusLabel_CommonObjectReference) |  | UNINITIALIZED, UNAVAILABLE, UNHEALTHY, DEGRADED, HEALTHY, |
| lastContact |  |  | Date | For sensors not having health capability, this will be filled with gRPC connection poll. Otherwise, this timestamp will be updated by central pipeline when message is processed. Note: we use this setting to guard against a specific attack vector during CRS-based cluster registration. Assuming that a CRS was used to register a cluster A and the CRS is leaked, an attacker shall not be able to re-run the CRS-flow which would then equip the attacker with a certificate & key issued to the cluster A. As countermeasure we only allow re-running the CRS-flow only as long as the last_contact field is empty, indicating that the legit cluster A’s sensor has not yet connected with the CRS-issued service certificates. | date-time |
| healthInfoComplete |  |  | Boolean |  |  |

<a id="StorageClusterMetadata_CommonObjectReference"></a>

## StorageClusterMetadata

ClusterMetadata contains metadata information about the cluster infrastructure.

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| type |  |  | [StorageClusterMetadataType](#StorageClusterMetadataType_CommonObjectReference) |  | UNSPECIFIED, AKS, ARO, EKS, GKE, OCP, OSD, ROSA, |
| name |  |  | String | Name represents the name under which the cluster is registered with the cloud provider. In case of self managed OpenShift it is the name chosen by the OpenShift installer. |  |
| id |  |  | String | Id represents a unique ID under which the cluster is registered with the cloud provider. Not all cluster types have an id. For all OpenShift clusters, this is the Red Hat `cluster_id` registered with OCM. |  |

<a id="StorageClusterMetadataType_CommonObjectReference"></a>

## StorageClusterMetadataType

| Enum Values |
|-------------|
| UNSPECIFIED |
| AKS         |
| ARO         |
| EKS         |
| GKE         |
| OCP         |
| OSD         |
| ROSA        |

<a id="StorageClusterStatus_CommonObjectReference"></a>

## StorageClusterStatus

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| sensorVersion |  |  | String |  |  |
| DEPRECATEDLastContact |  |  | Date | This field has been deprecated starting release 49.0. Use healthStatus.lastContact instead. | date-time |
| providerMetadata |  |  | [StorageProviderMetadata](#StorageProviderMetadata_CommonObjectReference) |  |  |
| orchestratorMetadata |  |  | [StorageOrchestratorMetadata](#StorageOrchestratorMetadata_CommonObjectReference) |  |  |
| upgradeStatus |  |  | [StorageClusterUpgradeStatus](#StorageClusterUpgradeStatus_CommonObjectReference) |  |  |
| certExpiryStatus |  |  | [StorageClusterCertExpiryStatus](#StorageClusterCertExpiryStatus_CommonObjectReference) |  |  |

<a id="StorageClusterType_CommonObjectReference"></a>

## StorageClusterType

| Enum Values        |
|--------------------|
| GENERIC_CLUSTER    |
| KUBERNETES_CLUSTER |
| OPENSHIFT_CLUSTER  |
| OPENSHIFT4_CLUSTER |

<a id="StorageClusterUpgradeStatus_CommonObjectReference"></a>

## StorageClusterUpgradeStatus

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| upgradability |  |  | [ClusterUpgradeStatusUpgradability](#ClusterUpgradeStatusUpgradability_CommonObjectReference) |  | UNSET, UP_TO_DATE, MANUAL_UPGRADE_REQUIRED, AUTO_UPGRADE_POSSIBLE, SENSOR_VERSION_HIGHER, |
| upgradabilityStatusReason |  |  | String |  |  |
| mostRecentProcess |  |  | [ClusterUpgradeStatusUpgradeProcessStatus](#ClusterUpgradeStatusUpgradeProcessStatus_CommonObjectReference) |  |  |

<a id="StorageCollectionMethod_CommonObjectReference"></a>

## StorageCollectionMethod

| Enum Values      |
|------------------|
| UNSET_COLLECTION |
| NO_COLLECTION    |
| KERNEL_MODULE    |
| EBPF             |
| CORE_BPF         |

<a id="StorageCollectorHealthInfo_CommonObjectReference"></a>

## StorageCollectorHealthInfo

CollectorHealthInfo carries data about collector deployment but does not include collector health status derived from this data. Aggregated collector health status is not included because it is derived in central and not in the component that first reports CollectorHealthInfo (sensor).

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| version |  |  | String |  |  |
| totalDesiredPods |  |  | Integer |  | int32 |
| totalReadyPods |  |  | Integer |  | int32 |
| totalRegisteredNodes |  |  | Integer |  | int32 |
| statusErrors |  |  | List of `string` | Collection of errors that occurred while trying to obtain collector health info. |  |

<a id="StorageCompleteClusterConfig_CommonObjectReference"></a>

## StorageCompleteClusterConfig

Encodes a complete cluster configuration minus ID/Name identifiers including static and dynamic settings.

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| dynamicConfig |  |  | [StorageDynamicClusterConfig](#StorageDynamicClusterConfig_CommonObjectReference) |  |  |
| staticConfig |  |  | [StorageStaticClusterConfig](#StorageStaticClusterConfig_CommonObjectReference) |  |  |
| configFingerprint |  |  | String |  |  |
| clusterLabels |  |  | Map of `string` |  |  |

<a id="StorageComplianceAggregationResponse_CommonObjectReference"></a>

## StorageComplianceAggregationResponse

Next available tag: 3

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| results |  |  | List of [ComplianceAggregationResult](#ComplianceAggregationResult_CommonObjectReference) |  |  |
| sources |  |  | List of [StorageComplianceAggregationSource](#StorageComplianceAggregationSource_CommonObjectReference) |  |  |
| errorMessage |  |  | String |  |  |

<a id="StorageComplianceAggregationScope_CommonObjectReference"></a>

## StorageComplianceAggregationScope

| Enum Values |
|-------------|
| UNKNOWN     |
| STANDARD    |
| CLUSTER     |
| CATEGORY    |
| CONTROL     |
| NAMESPACE   |
| NODE        |
| DEPLOYMENT  |
| CHECK       |

<a id="StorageComplianceAggregationSource_CommonObjectReference"></a>

## StorageComplianceAggregationSource

Next available tag: 5

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| clusterId |  |  | String |  |  |
| standardId |  |  | String |  |  |
| successfulRun |  |  | [StorageComplianceRunMetadata](#StorageComplianceRunMetadata_CommonObjectReference) |  |  |
| failedRuns |  |  | List of [StorageComplianceRunMetadata](#StorageComplianceRunMetadata_CommonObjectReference) |  |  |

<a id="StorageComplianceDomain_CommonObjectReference"></a>

## StorageComplianceDomain

Next available tag: 5

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| id |  |  | String |  |  |
| cluster |  |  | [ComplianceDomainCluster](#ComplianceDomainCluster_CommonObjectReference) |  |  |
| nodes |  |  | Map of [ComplianceDomainNode](#ComplianceDomainNode_CommonObjectReference) |  |  |
| deployments |  |  | Map of [ComplianceDomainDeployment](#ComplianceDomainDeployment_CommonObjectReference) |  |  |

<a id="StorageComplianceResultValue_CommonObjectReference"></a>

## StorageComplianceResultValue

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| evidence |  |  | List of [ComplianceResultValueEvidence](#ComplianceResultValueEvidence_CommonObjectReference) |  |  |
| overallState |  |  | [StorageComplianceState](#StorageComplianceState_CommonObjectReference) |  | COMPLIANCE_STATE_UNKNOWN, COMPLIANCE_STATE_SKIP, COMPLIANCE_STATE_NOTE, COMPLIANCE_STATE_SUCCESS, COMPLIANCE_STATE_FAILURE, COMPLIANCE_STATE_ERROR, |

<a id="StorageComplianceRunMetadata_CommonObjectReference"></a>

## StorageComplianceRunMetadata

Next available tag: 5

| Field Name      | Required | Nullable | Type    | Description | Format    |
|-----------------|----------|----------|---------|-------------|-----------|
| runId           |          |          | String  |             |           |
| standardId      |          |          | String  |             |           |
| clusterId       |          |          | String  |             |           |
| startTimestamp  |          |          | Date    |             | date-time |
| finishTimestamp |          |          | Date    |             | date-time |
| success         |          |          | Boolean |             |           |
| errorMessage    |          |          | String  |             |           |
| domainId        |          |          | String  |             |           |

<a id="StorageComplianceRunResults_CommonObjectReference"></a>

## StorageComplianceRunResults

Next available tag: 6

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| domain |  |  | [StorageComplianceDomain](#StorageComplianceDomain_CommonObjectReference) |  |  |
| runMetadata |  |  | [StorageComplianceRunMetadata](#StorageComplianceRunMetadata_CommonObjectReference) |  |  |
| clusterResults |  |  | [ComplianceRunResultsEntityResults](#ComplianceRunResultsEntityResults_CommonObjectReference) |  |  |
| nodeResults |  |  | Map of [ComplianceRunResultsEntityResults](#ComplianceRunResultsEntityResults_CommonObjectReference) |  |  |
| deploymentResults |  |  | Map of [ComplianceRunResultsEntityResults](#ComplianceRunResultsEntityResults_CommonObjectReference) |  |  |
| machineConfigResults |  |  | Map of [ComplianceRunResultsEntityResults](#ComplianceRunResultsEntityResults_CommonObjectReference) |  |  |

<a id="StorageComplianceState_CommonObjectReference"></a>

## StorageComplianceState

| Enum Values              |
|--------------------------|
| COMPLIANCE_STATE_UNKNOWN |
| COMPLIANCE_STATE_SKIP    |
| COMPLIANCE_STATE_NOTE    |
| COMPLIANCE_STATE_SUCCESS |
| COMPLIANCE_STATE_FAILURE |
| COMPLIANCE_STATE_ERROR   |

<a id="StorageConfig_CommonObjectReference"></a>

## StorageConfig

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| publicConfig |  |  | [StoragePublicConfig](#StoragePublicConfig_CommonObjectReference) |  |  |
| privateConfig |  |  | [StoragePrivateConfig](#StoragePrivateConfig_CommonObjectReference) |  |  |
| platformComponentConfig |  |  | [StoragePlatformComponentConfig](#StoragePlatformComponentConfig_CommonObjectReference) |  |  |

<a id="StorageContainer_CommonObjectReference"></a>

## StorageContainer

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| id |  |  | String |  |  |
| config |  |  | [StorageContainerConfig](#StorageContainerConfig_CommonObjectReference) |  |  |
| image |  |  | [StorageContainerImage](#StorageContainerImage_CommonObjectReference) |  |  |
| securityContext |  |  | [StorageSecurityContext](#StorageSecurityContext_CommonObjectReference) |  |  |
| volumes |  |  | List of [StorageVolume](#StorageVolume_CommonObjectReference) |  |  |
| ports |  |  | List of [StoragePortConfig](#StoragePortConfig_CommonObjectReference) |  |  |
| secrets |  |  | List of [StorageEmbeddedSecret](#StorageEmbeddedSecret_CommonObjectReference) |  |  |
| resources |  |  | [StorageResources](#StorageResources_CommonObjectReference) |  |  |
| name |  |  | String |  |  |
| livenessProbe |  |  | [StorageLivenessProbe](#StorageLivenessProbe_CommonObjectReference) |  |  |
| readinessProbe |  |  | [StorageReadinessProbe](#StorageReadinessProbe_CommonObjectReference) |  |  |
| type |  |  | [StorageContainerType](#StorageContainerType_CommonObjectReference) |  | REGULAR, INIT, |

<a id="StorageContainerConfig_CommonObjectReference"></a>

## StorageContainerConfig

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| env |  |  | List of [ContainerConfigEnvironmentConfig](#ContainerConfigEnvironmentConfig_CommonObjectReference) |  |  |
| command |  |  | List of `string` |  |  |
| args |  |  | List of `string` |  |  |
| directory |  |  | String |  |  |
| user |  |  | String |  |  |
| uid |  |  | String |  | int64 |
| appArmorProfile |  |  | String |  |  |

<a id="StorageContainerImage_CommonObjectReference"></a>

## StorageContainerImage

Next tag: 13

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| id |  |  | String |  |  |
| name |  |  | [StorageImageName](#StorageImageName_CommonObjectReference) |  |  |
| notPullable |  |  | Boolean |  |  |
| isClusterLocal |  |  | Boolean |  |  |
| idV2 |  |  | String |  |  |

<a id="StorageContainerInstance_CommonObjectReference"></a>

## StorageContainerInstance

ContainerInstanceID allows to uniquely identify a container within a cluster.

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| instanceId |  |  | [StorageContainerInstanceID](#StorageContainerInstanceID_CommonObjectReference) |  |  |
| containingPodId |  |  | String | The pod containing this container instance (kubernetes only). |  |
| containerName |  |  | String | Container name. |  |
| containerIps |  |  | List of `string` | The IP addresses of this container. |  |
| started |  |  | Date |  | date-time |
| imageDigest |  |  | String |  |  |
| finished |  |  | Date | The finish time of the container, if it finished. | date-time |
| exitCode |  |  | Integer | The exit code of the container. Only valid when finished is populated. | int32 |
| terminationReason |  |  | String | The reason for the container’s termination, if it finished. |  |

<a id="StorageContainerInstanceID_CommonObjectReference"></a>

## StorageContainerInstanceID

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| containerRuntime |  |  | [StorageContainerRuntime](#StorageContainerRuntime_CommonObjectReference) |  | UNKNOWN_CONTAINER_RUNTIME, DOCKER_CONTAINER_RUNTIME, CRIO_CONTAINER_RUNTIME, |
| id |  |  | String | The ID of the container, specific to the given runtime. |  |
| node |  |  | String | The node on which this container runs. |  |

<a id="StorageContainerNameAndBaselineStatus_CommonObjectReference"></a>

## StorageContainerNameAndBaselineStatus

`ContainerNameAndBaselineStatus` represents a cached result of process evaluation on a specific container name.

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| containerName |  |  | String |  |  |
| baselineStatus |  |  | [ContainerNameAndBaselineStatusBaselineStatus](#ContainerNameAndBaselineStatusBaselineStatus_CommonObjectReference) |  | INVALID, NOT_GENERATED, UNLOCKED, LOCKED, |
| anomalousProcessesExecuted |  |  | Boolean |  |  |

<a id="StorageContainerRuntime_CommonObjectReference"></a>

## StorageContainerRuntime

| Enum Values               |
|---------------------------|
| UNKNOWN_CONTAINER_RUNTIME |
| DOCKER_CONTAINER_RUNTIME  |
| CRIO_CONTAINER_RUNTIME    |

<a id="StorageContainerRuntimeInfo_CommonObjectReference"></a>

## StorageContainerRuntimeInfo

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| type |  |  | [StorageContainerRuntime](#StorageContainerRuntime_CommonObjectReference) |  | UNKNOWN_CONTAINER_RUNTIME, DOCKER_CONTAINER_RUNTIME, CRIO_CONTAINER_RUNTIME, |
| version |  |  | String |  |  |

<a id="StorageContainerType_CommonObjectReference"></a>

## StorageContainerType

| Enum Values |
|-------------|
| REGULAR     |
| INIT        |

<a id="StorageCosignCertificateVerification_CommonObjectReference"></a>

## StorageCosignCertificateVerification

Holds all verification data for verifying certificates attached to cosign signatures. If only the certificate is given, the Fulcio trusted root chain will be assumed and verified against. If only the chain is given, this will be used over the Fulcio trusted root chain for verification. If no certificate or chain is given, the Fulcio trusted root chain will be assumed and verified against.

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| certificatePemEnc |  |  | String | PEM encoded certificate to use for verification. Leave empty when using short-lived certificates as issued by Fulcio. |  |
| certificateChainPemEnc |  |  | String | PEM encoded certificate chain to use for verification. Defaults to the root certificate authority of the public Sigstore instance if left empty. |  |
| certificateOidcIssuer |  |  | String | Certificate OIDC issuer to verify against. This supports regular expressions following the RE2 syntax: <https://github.com/google/re2/wiki/Syntax>. In case the certificate does not specify an OIDC issuer, you may use '.\*' as the OIDC issuer. However, it is recommended to use Fulcio compatible certificates according to the specification: <https://github.com/sigstore/fulcio/blob/main/docs/certificate-specification.md>. |  |
| certificateIdentity |  |  | String | Certificate identity to verify against. This supports regular expressions following the RE2 syntax: <https://github.com/google/re2/wiki/Syntax>. In case the certificate does not specify an identity, you may use '.\*' as the identity. However, it is recommended to use Fulcio compatible certificates according to the specification: <https://github.com/sigstore/fulcio/blob/main/docs/certificate-specification.md>. |  |
| certificateTransparencyLog |  |  | [StorageCertificateTransparencyLogVerification](#StorageCertificateTransparencyLogVerification_CommonObjectReference) |  |  |

<a id="StorageCosignPublicKeyVerification_CommonObjectReference"></a>

## StorageCosignPublicKeyVerification

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| publicKeys |  |  | List of [CosignPublicKeyVerificationPublicKey](#CosignPublicKeyVerificationPublicKey_CommonObjectReference) |  |  |

<a id="StorageCosignSignature_CommonObjectReference"></a>

## StorageCosignSignature

| Field Name       | Required | Nullable | Type     | Description | Format |
|------------------|----------|----------|----------|-------------|--------|
| rawSignature     |          |          | byte\[\] |             | byte   |
| signaturePayload |          |          | byte\[\] |             | byte   |
| certPem          |          |          | byte\[\] |             | byte   |
| certChainPem     |          |          | byte\[\] |             | byte   |
| rekorBundle      |          |          | byte\[\] |             | byte   |

<a id="StorageDataSource_CommonObjectReference"></a>

## StorageDataSource

| Field Name | Required | Nullable | Type   | Description | Format |
|------------|----------|----------|--------|-------------|--------|
| id         |          |          | String |             |        |
| name       |          |          | String |             |        |
| mirror     |          |          | String |             |        |

<a id="StorageDayOption_CommonObjectReference"></a>

## StorageDayOption

| Field Name | Required | Nullable | Type    | Description | Format |
|------------|----------|----------|---------|-------------|--------|
| numDays    |          |          | Long    |             | int64  |
| enabled    |          |          | Boolean |             |        |

<a id="StorageDeclarativeConfigHealth_CommonObjectReference"></a>

## StorageDeclarativeConfigHealth

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| id |  |  | String |  |  |
| name |  |  | String |  |  |
| status |  |  | [StorageDeclarativeConfigHealthStatus](#StorageDeclarativeConfigHealthStatus_CommonObjectReference) |  | UNHEALTHY, HEALTHY, |
| errorMessage |  |  | String |  |  |
| resourceName |  |  | String |  |  |
| resourceType |  |  | [DeclarativeConfigHealthResourceType](#DeclarativeConfigHealthResourceType_CommonObjectReference) |  | CONFIG_MAP, ACCESS_SCOPE, PERMISSION_SET, ROLE, AUTH_PROVIDER, GROUP, NOTIFIER, AUTH_MACHINE_TO_MACHINE_CONFIG, |
| lastTimestamp |  |  | Date | Timestamp when the current status was set. | date-time |

<a id="StorageDeclarativeConfigHealthStatus_CommonObjectReference"></a>

## StorageDeclarativeConfigHealthStatus

| Enum Values |
|-------------|
| UNHEALTHY   |
| HEALTHY     |

<a id="StorageDecommissionedClusterRetentionConfig_CommonObjectReference"></a>

## StorageDecommissionedClusterRetentionConfig

next available tag: 5

| Field Name            | Required | Nullable | Type            | Description | Format    |
|-----------------------|----------|----------|-----------------|-------------|-----------|
| retentionDurationDays |          |          | Integer         |             | int32     |
| ignoreClusterLabels   |          |          | Map of `string` |             |           |
| lastUpdated           |          |          | Date            |             | date-time |
| createdAt             |          |          | Date            |             | date-time |

<a id="StorageDeployment_CommonObjectReference"></a>

## StorageDeployment

Next available tag: 36

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| id |  |  | String |  |  |
| name |  |  | String |  |  |
| hash |  |  | String |  | uint64 |
| type |  |  | String |  |  |
| namespace |  |  | String |  |  |
| namespaceId |  |  | String |  |  |
| orchestratorComponent |  |  | Boolean |  |  |
| replicas |  |  | String |  | int64 |
| labels |  |  | Map of `string` |  |  |
| podLabels |  |  | Map of `string` |  |  |
| labelSelector |  |  | [StorageLabelSelector](#StorageLabelSelector_CommonObjectReference) |  |  |
| created |  |  | Date |  | date-time |
| clusterId |  |  | String |  |  |
| clusterName |  |  | String |  |  |
| containers |  |  | List of [StorageContainer](#StorageContainer_CommonObjectReference) |  |  |
| annotations |  |  | Map of `string` |  |  |
| priority |  |  | String |  | int64 |
| inactive |  |  | Boolean |  |  |
| imagePullSecrets |  |  | List of `string` |  |  |
| serviceAccount |  |  | String |  |  |
| serviceAccountPermissionLevel |  |  | [StoragePermissionLevel](#StoragePermissionLevel_CommonObjectReference) |  | UNSET, NONE, DEFAULT, ELEVATED_IN_NAMESPACE, ELEVATED_CLUSTER_WIDE, CLUSTER_ADMIN, |
| automountServiceAccountToken |  |  | Boolean |  |  |
| hostNetwork |  |  | Boolean |  |  |
| hostPid |  |  | Boolean |  |  |
| hostIpc |  |  | Boolean |  |  |
| runtimeClass |  |  | String |  |  |
| tolerations |  |  | List of [StorageToleration](#StorageToleration_CommonObjectReference) |  |  |
| ports |  |  | List of [StoragePortConfig](#StoragePortConfig_CommonObjectReference) |  |  |
| stateTimestamp |  |  | String |  | int64 |
| riskScore |  |  | Float |  | float |
| platformComponent |  |  | Boolean |  |  |

<a id="StorageDockerConfig_CommonObjectReference"></a>

## StorageDockerConfig

Docker registry configuration. Used by integrations of type "docker" and other docker compliant registries without dedicated configuration type.

Use of type "azure" with `DockerConfig` has been deprecated in 4.7. Use `AzureConfig` instead.

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| endpoint |  |  | String |  |  |
| username |  |  | String |  |  |
| password |  |  | String | The password for the integration. The server will mask the value of this credential in responses and logs. |  |
| insecure |  |  | Boolean |  |  |

<a id="StorageDynamicClusterConfig_CommonObjectReference"></a>

## StorageDynamicClusterConfig

The difference between Static and Dynamic cluster config is that Dynamic values are sent over the Central to Sensor gRPC connection. This has the benefit of allowing for "hot reloading" of values without restarting Secured cluster components.

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| admissionControllerConfig |  |  | [StorageAdmissionControllerConfig](#StorageAdmissionControllerConfig_CommonObjectReference) |  |  |
| registryOverride |  |  | String |  |  |
| disableAuditLogs |  |  | Boolean |  |  |
| autoLockProcessBaselinesConfig |  |  | [StorageAutoLockProcessBaselinesConfig](#StorageAutoLockProcessBaselinesConfig_CommonObjectReference) |  |  |
| processIndicators |  |  | [DynamicClusterConfigProcessIndicatorsConfig](#DynamicClusterConfigProcessIndicatorsConfig_CommonObjectReference) |  |  |

<a id="StorageECRConfig_CommonObjectReference"></a>

## StorageECRConfig

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| registryId |  |  | String |  |  |
| accessKeyId |  |  | String | The access key ID for the integration. The server will mask the value of this credential in responses and logs. |  |
| secretAccessKey |  |  | String | The secret access key for the integration. The server will mask the value of this credential in responses and logs. |  |
| region |  |  | String |  |  |
| useIam |  |  | Boolean |  |  |
| endpoint |  |  | String |  |  |
| useAssumeRole |  |  | Boolean |  |  |
| assumeRoleId |  |  | String |  |  |
| assumeRoleExternalId |  |  | String |  |  |
| authorizationData |  |  | [ECRConfigAuthorizationData](#ECRConfigAuthorizationData_CommonObjectReference) |  |  |

<a id="StorageEPSS_CommonObjectReference"></a>

## StorageEPSS

EPSS Score stores two epss metrics returned by scanner - epss probability and epss percentile

| Field Name      | Required | Nullable | Type  | Description | Format |
|-----------------|----------|----------|-------|-------------|--------|
| epssProbability |          |          | Float |             | float  |
| epssPercentile  |          |          | Float |             | float  |

<a id="StorageEffectiveAccessScope_CommonObjectReference"></a>

## StorageEffectiveAccessScope

EffectiveAccessScope describes which clusters and namespaces are "in scope" given current state. Basically, if AccessScope is applied to the currently known clusters and namespaces, the result is EffectiveAccessScope.

EffectiveAccessScope represents a tree with nodes marked as included and excluded. If a node is included, all its child nodes are included.

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| clusters |  |  | List of [EffectiveAccessScopeCluster](#EffectiveAccessScopeCluster_CommonObjectReference) |  |  |

<a id="StorageEffectiveAccessScopeNamespace_CommonObjectReference"></a>

## StorageEffectiveAccessScopeNamespace

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| id |  |  | String |  |  |
| name |  |  | String |  |  |
| state |  |  | [StorageEffectiveAccessScopeState](#StorageEffectiveAccessScopeState_CommonObjectReference) |  | UNKNOWN, INCLUDED, EXCLUDED, PARTIAL, |
| labels |  |  | Map of `string` |  |  |

<a id="StorageEffectiveAccessScopeState_CommonObjectReference"></a>

## StorageEffectiveAccessScopeState

| Enum Values |
|-------------|
| UNKNOWN     |
| INCLUDED    |
| EXCLUDED    |
| PARTIAL     |

<a id="StorageEmail_CommonObjectReference"></a>

## StorageEmail

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| server |  |  | String |  |  |
| sender |  |  | String |  |  |
| username |  |  | String |  |  |
| password |  |  | String | The password for the integration. The server will mask the value of this credential in responses and logs. |  |
| disableTLS |  |  | Boolean |  |  |
| DEPRECATEDUseStartTLS |  |  | Boolean |  |  |
| from |  |  | String |  |  |
| startTLSAuthMethod |  |  | [EmailAuthMethod](#EmailAuthMethod_CommonObjectReference) |  | DISABLED, PLAIN, LOGIN, |
| allowUnauthenticatedSmtp |  |  | Boolean |  |  |
| skipTLSVerify |  |  | Boolean |  |  |
| hostnameHeloEhlo |  |  | String |  |  |

<a id="StorageEmailNotifierConfiguration_CommonObjectReference"></a>

## StorageEmailNotifierConfiguration

| Field Name    | Required | Nullable | Type             | Description | Format |
|---------------|----------|----------|------------------|-------------|--------|
| notifierId    |          |          | String           |             |        |
| mailingLists  |          |          | List of `string` |             |        |
| customSubject |          |          | String           |             |        |
| customBody    |          |          | String           |             |        |

<a id="StorageEmbeddedImageScanComponent_CommonObjectReference"></a>

## StorageEmbeddedImageScanComponent

Next Tag: 14

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| name |  |  | String |  |  |
| version |  |  | String |  |  |
| license |  |  | [StorageLicense](#StorageLicense_CommonObjectReference) |  |  |
| vulns |  |  | List of [StorageEmbeddedVulnerability](#StorageEmbeddedVulnerability_CommonObjectReference) |  |  |
| layerIndex |  |  | Integer |  | int32 |
| priority |  |  | String |  | int64 |
| source |  |  | [StorageSourceType](#StorageSourceType_CommonObjectReference) |  | OS, PYTHON, JAVA, RUBY, NODEJS, GO, DOTNETCORERUNTIME, INFRASTRUCTURE, |
| location |  |  | String |  |  |
| topCvss |  |  | Float |  | float |
| riskScore |  |  | Float |  | float |
| fixedBy |  |  | String | Component version that fixes all the fixable vulnerabilities in this component. |  |
| executables |  |  | List of [EmbeddedImageScanComponentExecutable](#EmbeddedImageScanComponentExecutable_CommonObjectReference) |  |  |
| architecture |  |  | String |  |  |

<a id="StorageEmbeddedImageScanComponentExecutable_CommonObjectReference"></a>

## StorageEmbeddedImageScanComponentExecutable

| Field Name   | Required | Nullable | Type             | Description | Format |
|--------------|----------|----------|------------------|-------------|--------|
| path         |          |          | String           |             |        |
| dependencies |          |          | List of `string` |             |        |

<a id="StorageEmbeddedNodeScanComponent_CommonObjectReference"></a>

## StorageEmbeddedNodeScanComponent

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| name |  |  | String |  |  |
| version |  |  | String |  |  |
| vulns |  |  | List of [StorageEmbeddedVulnerability](#StorageEmbeddedVulnerability_CommonObjectReference) |  |  |
| vulnerabilities |  |  | List of [StorageNodeVulnerability](#StorageNodeVulnerability_CommonObjectReference) |  |  |
| priority |  |  | String |  | int64 |
| topCvss |  |  | Float |  | float |
| riskScore |  |  | Float |  | float |

<a id="StorageEmbeddedSecret_CommonObjectReference"></a>

## StorageEmbeddedSecret

| Field Name | Required | Nullable | Type   | Description | Format |
|------------|----------|----------|--------|-------------|--------|
| name       |          |          | String |             |        |
| path       |          |          | String |             |        |

<a id="StorageEmbeddedVulnerability_CommonObjectReference"></a>

## StorageEmbeddedVulnerability

Next Tag: 27

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| cve |  |  | String |  |  |
| advisory |  |  | [StorageAdvisory](#StorageAdvisory_CommonObjectReference) |  |  |
| cvss |  |  | Float |  | float |
| summary |  |  | String |  |  |
| link |  |  | String |  |  |
| fixedBy |  |  | String |  |  |
| scoreVersion |  |  | [EmbeddedVulnerabilityScoreVersion](#EmbeddedVulnerabilityScoreVersion_CommonObjectReference) |  | V2, V3, |
| cvssV2 |  |  | [StorageCVSSV2](#StorageCVSSV2_CommonObjectReference) |  |  |
| cvssV3 |  |  | [StorageCVSSV3](#StorageCVSSV3_CommonObjectReference) |  |  |
| publishedOn |  |  | Date |  | date-time |
| lastModified |  |  | Date |  | date-time |
| vulnerabilityType |  |  | [EmbeddedVulnerabilityVulnerabilityType](#EmbeddedVulnerabilityVulnerabilityType_CommonObjectReference) |  | UNKNOWN_VULNERABILITY, IMAGE_VULNERABILITY, K8S_VULNERABILITY, ISTIO_VULNERABILITY, NODE_VULNERABILITY, OPENSHIFT_VULNERABILITY, |
| vulnerabilityTypes |  |  | List of [EmbeddedVulnerabilityVulnerabilityType](#EmbeddedVulnerabilityVulnerabilityType_CommonObjectReference) |  |  |
| suppressed |  |  | Boolean |  |  |
| suppressActivation |  |  | Date |  | date-time |
| suppressExpiry |  |  | Date |  | date-time |
| firstSystemOccurrence |  |  | Date | Time when the CVE was first seen, for this specific distro, in the system. | date-time |
| firstImageOccurrence |  |  | Date | Time when the CVE was first seen in this image. | date-time |
| fixAvailableTimestamp |  |  | Date | Timestamp when the fix for this CVE was made available according to the sources or the timestamp of the first scan after this field was introduced which discovered this CVE as fixable, if it is. | date-time |
| severity |  |  | [StorageVulnerabilitySeverity](#StorageVulnerabilitySeverity_CommonObjectReference) |  | UNKNOWN_VULNERABILITY_SEVERITY, LOW_VULNERABILITY_SEVERITY, MODERATE_VULNERABILITY_SEVERITY, IMPORTANT_VULNERABILITY_SEVERITY, CRITICAL_VULNERABILITY_SEVERITY, |
| state |  |  | [StorageVulnerabilityState](#StorageVulnerabilityState_CommonObjectReference) |  | OBSERVED, DEFERRED, FALSE_POSITIVE, |
| cvssMetrics |  |  | List of [StorageCVSSScore](#StorageCVSSScore_CommonObjectReference) |  |  |
| nvdCvss |  |  | Float |  | float |
| epss |  |  | [StorageEPSS](#StorageEPSS_CommonObjectReference) |  |  |
| datasource |  |  | String |  |  |

<a id="StorageEmbeddedVulnerabilityScoreVersion_CommonObjectReference"></a>

## StorageEmbeddedVulnerabilityScoreVersion

ScoreVersion can be deprecated ROX-26066

- V2: No unset for automatic backwards compatibility

| Enum Values |
|-------------|
| V2          |
| V3          |

<a id="StorageEnforcementAction_CommonObjectReference"></a>

## StorageEnforcementAction

- FAIL_KUBE_REQUEST_ENFORCEMENT: FAIL_KUBE_REQUEST_ENFORCEMENT takes effect only if admission control webhook is enabled to listen on exec and port-forward events.

- FAIL_DEPLOYMENT_CREATE_ENFORCEMENT: FAIL_DEPLOYMENT_CREATE_ENFORCEMENT takes effect only if admission control webhook is configured to enforce on object creates.

- FAIL_DEPLOYMENT_UPDATE_ENFORCEMENT: FAIL_DEPLOYMENT_UPDATE_ENFORCEMENT takes effect only if admission control webhook is configured to enforce on object updates.

| Enum Values                               |
|-------------------------------------------|
| UNSET_ENFORCEMENT                         |
| SCALE_TO_ZERO_ENFORCEMENT                 |
| UNSATISFIABLE_NODE_CONSTRAINT_ENFORCEMENT |
| KILL_POD_ENFORCEMENT                      |
| FAIL_BUILD_ENFORCEMENT                    |
| FAIL_KUBE_REQUEST_ENFORCEMENT             |
| FAIL_DEPLOYMENT_CREATE_ENFORCEMENT        |
| FAIL_DEPLOYMENT_UPDATE_ENFORCEMENT        |

<a id="StorageEntityField_CommonObjectReference"></a>

## StorageEntityField

| Enum Values      |
|------------------|
| FIELD_UNSET      |
| FIELD_ID         |
| FIELD_NAME       |
| FIELD_LABEL      |
| FIELD_ANNOTATION |

<a id="StorageEntityScope_CommonObjectReference"></a>

## StorageEntityScope

EntityScope is a new scoping method using ns,deployments,clusters filters introduced in 4.11

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| rules |  |  | List of [StorageEntityScopeRule](#StorageEntityScopeRule_CommonObjectReference) |  |  |

<a id="StorageEntityScopeRule_CommonObjectReference"></a>

## StorageEntityScopeRule

EntityScopeRule stores the filter as an entity field pair along with a list of values

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| entity |  |  | [StorageEntityType](#StorageEntityType_CommonObjectReference) |  | ENTITY_TYPE_UNSET, ENTITY_TYPE_DEPLOYMENT, ENTITY_TYPE_NAMESPACE, ENTITY_TYPE_CLUSTER, |
| field |  |  | [StorageEntityField](#StorageEntityField_CommonObjectReference) |  | FIELD_UNSET, FIELD_ID, FIELD_NAME, FIELD_LABEL, FIELD_ANNOTATION, |
| values |  |  | List of [StorageRuleValue](#StorageRuleValue_CommonObjectReference) |  |  |

<a id="StorageEntityType_CommonObjectReference"></a>

## StorageEntityType

| Enum Values            |
|------------------------|
| ENTITY_TYPE_UNSET      |
| ENTITY_TYPE_DEPLOYMENT |
| ENTITY_TYPE_NAMESPACE  |
| ENTITY_TYPE_CLUSTER    |

<a id="StorageEventSource_CommonObjectReference"></a>

## StorageEventSource

| Enum Values      |
|------------------|
| NOT_APPLICABLE   |
| DEPLOYMENT_EVENT |
| AUDIT_LOG_EVENT  |
| NODE_EVENT       |

<a id="StorageExclusion_CommonObjectReference"></a>

## StorageExclusion

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| name |  |  | String |  |  |
| deployment |  |  | [ExclusionDeployment](#ExclusionDeployment_CommonObjectReference) |  |  |
| image |  |  | [ExclusionImage](#ExclusionImage_CommonObjectReference) |  |  |
| expiration |  |  | Date |  | date-time |

<a id="StorageExclusionDeployment_CommonObjectReference"></a>

## StorageExclusionDeployment

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| name |  |  | String |  |  |
| scope |  |  | [StorageScope](#StorageScope_CommonObjectReference) |  |  |

<a id="StorageExportPoliciesResponse_CommonObjectReference"></a>

## StorageExportPoliciesResponse

ExportPoliciesResponse is used by the API but it is defined in storage because we expect customers to store them. We do backwards-compatibility checks on objects in the storge folder and those checks should be applied to this object

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| policies |  |  | List of [StoragePolicy](#StoragePolicy_CommonObjectReference) |  |  |

<a id="StorageExternalBackup_CommonObjectReference"></a>

## StorageExternalBackup

Next available tag: 10

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| id |  |  | String |  |  |
| name |  |  | String |  |  |
| type |  |  | String |  |  |
| schedule |  |  | [StorageSchedule](#StorageSchedule_CommonObjectReference) |  |  |
| backupsToKeep |  |  | Integer |  | int32 |
| s3 |  |  | [StorageS3Config](#StorageS3Config_CommonObjectReference) |  |  |
| gcs |  |  | [StorageGCSConfig](#StorageGCSConfig_CommonObjectReference) |  |  |
| s3compatible |  |  | [StorageS3Compatible](#StorageS3Compatible_CommonObjectReference) |  |  |
| includeCertificates |  |  | Boolean |  |  |

<a id="StorageFileAccess_CommonObjectReference"></a>

## StorageFileAccess

FileAccess contains fields related to arbitrary file accesses performed by a given process. This activity can come from k8s, or directly on a node.

It is currently intended to be used in Sensor and for detection, but will only be stored embedded in an Alert. As a result, it does not currently define a primary key.

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| file |  |  | [StorageFileAccessFile](#StorageFileAccessFile_CommonObjectReference) |  |  |
| operation |  |  | [FileAccessOperation](#FileAccessOperation_CommonObjectReference) |  | CREATE, UNLINK, RENAME, PERMISSION_CHANGE, OWNERSHIP_CHANGE, OPEN, |
| moved |  |  | [StorageFileAccessFile](#StorageFileAccessFile_CommonObjectReference) |  |  |
| timestamp |  |  | Date |  | date-time |
| process |  |  | [StorageProcessIndicator](#StorageProcessIndicator_CommonObjectReference) |  |  |
| hostname |  |  | String |  |  |

<a id="StorageFileAccessFile_CommonObjectReference"></a>

## StorageFileAccessFile

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| effectivePath |  |  | String |  |  |
| actualPath |  |  | String |  |  |
| meta |  |  | [FileAccessFileMetadata](#FileAccessFileMetadata_CommonObjectReference) |  |  |

<a id="StorageGCSConfig_CommonObjectReference"></a>

## StorageGCSConfig

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| bucket |  |  | String |  |  |
| serviceAccount |  |  | String | The service account for the storage integration. The server will mask the value of this credential in responses and logs. |  |
| objectPrefix |  |  | String |  |  |
| useWorkloadId |  |  | Boolean |  |  |

<a id="StorageGeneric_CommonObjectReference"></a>

## StorageGeneric

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| endpoint |  |  | String |  |  |
| skipTLSVerify |  |  | Boolean |  |  |
| caCert |  |  | String |  |  |
| username |  |  | String |  |  |
| password |  |  | String | The password for the integration. The server will mask the value of this credential in responses and logs. |  |
| headers |  |  | List of [StorageKeyValuePair](#StorageKeyValuePair_CommonObjectReference) |  |  |
| extraFields |  |  | List of [StorageKeyValuePair](#StorageKeyValuePair_CommonObjectReference) |  |  |
| auditLoggingEnabled |  |  | Boolean |  |  |

<a id="StorageGoogleConfig_CommonObjectReference"></a>

## StorageGoogleConfig

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| endpoint |  |  | String |  |  |
| serviceAccount |  |  | String | The service account for the integration. The server will mask the value of this credential in responses and logs. |  |
| project |  |  | String |  |  |
| wifEnabled |  |  | Boolean |  |  |

<a id="StorageGoogleProviderMetadata_CommonObjectReference"></a>

## StorageGoogleProviderMetadata

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| project |  |  | String |  |  |
| clusterName |  |  | String | Deprecated in favor of providerMetadata.cluster.name. |  |

<a id="StorageGroup_CommonObjectReference"></a>

## StorageGroup

Group is a GroupProperties : Role mapping.

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| props |  |  | [StorageGroupProperties](#StorageGroupProperties_CommonObjectReference) |  |  |
| roleName |  |  | String | This is the name of the role that will apply to users in this group. |  |

<a id="StorageGroupProperties_CommonObjectReference"></a>

## StorageGroupProperties

GroupProperties defines the properties of a group. Groups apply to users when their properties match. For instance: - If GroupProperties has only an auth_provider_id, then that group applies to all users logged in with that auth provider. - If GroupProperties in addition has a claim key, then it applies to all users with that auth provider and the claim key, etc. Note: Changes to GroupProperties may require changes to v1.DeleteGroupRequest.

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| id |  |  | String | Unique identifier for group properties and respectively the group. |  |
| traits |  |  | [StorageTraits](#StorageTraits_CommonObjectReference) |  |  |
| authProviderId |  |  | String |  |  |
| key |  |  | String |  |  |
| value |  |  | String |  |  |

<a id="StorageIBMRegistryConfig_CommonObjectReference"></a>

## StorageIBMRegistryConfig

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| endpoint |  |  | String |  |  |
| apiKey |  |  | String | The API key for the integration. The server will mask the value of this credential in responses and logs. |  |

<a id="StorageIPBlock_CommonObjectReference"></a>

## StorageIPBlock

| Field Name | Required | Nullable | Type             | Description | Format |
|------------|----------|----------|------------------|-------------|--------|
| cidr       |          |          | String           |             |        |
| except     |          |          | List of `string` |             |        |

<a id="StorageImage_CommonObjectReference"></a>

## StorageImage

This proto is deprecated and replaced by ImageV2. Next Tag: 19

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| id |  |  | String |  |  |
| name |  |  | [StorageImageName](#StorageImageName_CommonObjectReference) |  |  |
| names |  |  | List of [StorageImageName](#StorageImageName_CommonObjectReference) | This should deprecate the ImageName field long-term, allowing images with the same digest to be associated with different locations. TODO(dhaus): For now, this message will be without search tags due to duplicated search tags otherwise. |  |
| metadata |  |  | [StorageImageMetadata](#StorageImageMetadata_CommonObjectReference) |  |  |
| scan |  |  | [StorageImageScan](#StorageImageScan_CommonObjectReference) |  |  |
| signatureVerificationData |  |  | [StorageImageSignatureVerificationData](#StorageImageSignatureVerificationData_CommonObjectReference) |  |  |
| signature |  |  | [StorageImageSignature](#StorageImageSignature_CommonObjectReference) |  |  |
| components |  |  | Integer |  | int32 |
| cves |  |  | Integer |  | int32 |
| fixableCves |  |  | Integer |  | int32 |
| lastUpdated |  |  | Date |  | date-time |
| notPullable |  |  | Boolean |  |  |
| isClusterLocal |  |  | Boolean |  |  |
| priority |  |  | String |  | int64 |
| riskScore |  |  | Float |  | float |
| topCvss |  |  | Float |  | float |
| notes |  |  | List of [StorageImageNote](#StorageImageNote_CommonObjectReference) |  |  |
| baseImageInfo |  |  | List of [StorageBaseImageInfo](#StorageBaseImageInfo_CommonObjectReference) |  |  |

<a id="StorageImageIntegration_CommonObjectReference"></a>

## StorageImageIntegration

Next Tag: 25

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| id |  |  | String |  |  |
| name |  |  | String |  |  |
| type |  |  | String |  |  |
| categories |  |  | List of [StorageImageIntegrationCategory](#StorageImageIntegrationCategory_CommonObjectReference) |  |  |
| clairify |  |  | [StorageClairifyConfig](#StorageClairifyConfig_CommonObjectReference) |  |  |
| scannerV4 |  |  | [StorageScannerV4Config](#StorageScannerV4Config_CommonObjectReference) |  |  |
| docker |  |  | [StorageDockerConfig](#StorageDockerConfig_CommonObjectReference) |  |  |
| quay |  |  | [StorageQuayConfig](#StorageQuayConfig_CommonObjectReference) |  |  |
| ecr |  |  | [StorageECRConfig](#StorageECRConfig_CommonObjectReference) |  |  |
| google |  |  | [StorageGoogleConfig](#StorageGoogleConfig_CommonObjectReference) |  |  |
| clair |  |  | [StorageClairConfig](#StorageClairConfig_CommonObjectReference) |  |  |
| clairV4 |  |  | [StorageClairV4Config](#StorageClairV4Config_CommonObjectReference) |  |  |
| ibm |  |  | [StorageIBMRegistryConfig](#StorageIBMRegistryConfig_CommonObjectReference) |  |  |
| azure |  |  | [StorageAzureConfig](#StorageAzureConfig_CommonObjectReference) |  |  |
| autogenerated |  |  | Boolean |  |  |
| clusterId |  |  | String |  |  |
| skipTestIntegration |  |  | Boolean |  |  |
| source |  |  | [StorageImageIntegrationSource](#StorageImageIntegrationSource_CommonObjectReference) |  |  |

<a id="StorageImageIntegrationCategory_CommonObjectReference"></a>

## StorageImageIntegrationCategory

- NODE_SCANNER: Image and Node integrations are currently done on the same form in the UI so the image integration is also currently used for node integrations. This decision was made because we currently only support one node scanner (our scanner).

| Enum Values  |
|--------------|
| REGISTRY     |
| SCANNER      |
| NODE_SCANNER |

<a id="StorageImageIntegrationSource_CommonObjectReference"></a>

## StorageImageIntegrationSource

| Field Name          | Required | Nullable | Type   | Description | Format |
|---------------------|----------|----------|--------|-------------|--------|
| clusterId           |          |          | String |             |        |
| namespace           |          |          | String |             |        |
| imagePullSecretName |          |          | String |             |        |

<a id="StorageImageLayer_CommonObjectReference"></a>

## StorageImageLayer

| Field Name  | Required | Nullable | Type    | Description | Format    |
|-------------|----------|----------|---------|-------------|-----------|
| instruction |          |          | String  |             |           |
| value       |          |          | String  |             |           |
| created     |          |          | Date    |             | date-time |
| author      |          |          | String  |             |           |
| empty       |          |          | Boolean |             |           |

<a id="StorageImageMetadata_CommonObjectReference"></a>

## StorageImageMetadata

If any fields of ImageMetadata are modified including subfields, please check pkg/images/enricher/metadata.go to ensure that those changes will be automatically picked up Next Tag: 6

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| v1 |  |  | [StorageV1Metadata](#StorageV1Metadata_CommonObjectReference) |  |  |
| v2 |  |  | [StorageV2Metadata](#StorageV2Metadata_CommonObjectReference) |  |  |
| layerShas |  |  | List of `string` |  |  |
| dataSource |  |  | [StorageDataSource](#StorageDataSource_CommonObjectReference) |  |  |
| version |  |  | String |  | uint64 |

<a id="StorageImageName_CommonObjectReference"></a>

## StorageImageName

| Field Name | Required | Nullable | Type   | Description | Format |
|------------|----------|----------|--------|-------------|--------|
| registry   |          |          | String |             |        |
| remote     |          |          | String |             |        |
| tag        |          |          | String |             |        |
| fullName   |          |          | String |             |        |

<a id="StorageImageNote_CommonObjectReference"></a>

## StorageImageNote

| Enum Values                         |
|-------------------------------------|
| MISSING_METADATA                    |
| MISSING_SCAN_DATA                   |
| MISSING_SIGNATURE                   |
| MISSING_SIGNATURE_VERIFICATION_DATA |

<a id="StorageImagePullSecret_CommonObjectReference"></a>

## StorageImagePullSecret

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| registries |  |  | List of [ImagePullSecretRegistry](#ImagePullSecretRegistry_CommonObjectReference) |  |  |

<a id="StorageImageScan_CommonObjectReference"></a>

## StorageImageScan

Next tag: 8

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| scannerVersion |  |  | String |  |  |
| scanTime |  |  | Date |  | date-time |
| components |  |  | List of [StorageEmbeddedImageScanComponent](#StorageEmbeddedImageScanComponent_CommonObjectReference) |  |  |
| operatingSystem |  |  | String |  |  |
| dataSource |  |  | [StorageDataSource](#StorageDataSource_CommonObjectReference) |  |  |
| notes |  |  | List of [StorageImageScanNote](#StorageImageScanNote_CommonObjectReference) |  |  |
| hash |  |  | String |  | uint64 |

<a id="StorageImageScanNote_CommonObjectReference"></a>

## StorageImageScanNote

| Enum Values                     |
|---------------------------------|
| UNSET                           |
| OS_UNAVAILABLE                  |
| PARTIAL_SCAN_DATA               |
| OS_CVES_UNAVAILABLE             |
| OS_CVES_STALE                   |
| LANGUAGE_CVES_UNAVAILABLE       |
| CERTIFIED_RHEL_SCAN_UNAVAILABLE |

<a id="StorageImageSignature_CommonObjectReference"></a>

## StorageImageSignature

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| signatures |  |  | List of [StorageSignature](#StorageSignature_CommonObjectReference) |  |  |
| fetched |  |  | Date |  | date-time |

<a id="StorageImageSignatureVerificationData_CommonObjectReference"></a>

## StorageImageSignatureVerificationData

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| results |  |  | List of [StorageImageSignatureVerificationResult](#StorageImageSignatureVerificationResult_CommonObjectReference) |  |  |

<a id="StorageImageSignatureVerificationResult_CommonObjectReference"></a>

## StorageImageSignatureVerificationResult

Next Tag: 7

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| verificationTime |  |  | Date |  | date-time |
| verifierId |  |  | String | verifier_id correlates to the ID of the signature integration used to verify the signature. |  |
| status |  |  | [StorageImageSignatureVerificationResultStatus](#StorageImageSignatureVerificationResultStatus_CommonObjectReference) |  | UNSET, VERIFIED, FAILED_VERIFICATION, INVALID_SIGNATURE_ALGO, CORRUPTED_SIGNATURE, GENERIC_ERROR, |
| description |  |  | String | description is set in the case of an error with the specific error’s message. Otherwise, this will not be set. |  |
| verifiedImageReferences |  |  | List of `string` | The full image names that are verified by this specific signature integration ID. |  |
| verifierName |  |  | String | verifier_name is the name of the signature integration associated with `verifier_id`. |  |

<a id="StorageImageSignatureVerificationResultStatus_CommonObjectReference"></a>

## StorageImageSignatureVerificationResultStatus

Status represents the status of the result.

- VERIFIED: VERIFIED is set when the signature’s verification was successful.

- FAILED_VERIFICATION: FAILED_VERIFICATION is set when the signature’s verification failed.

- INVALID_SIGNATURE_ALGO: INVALID_SIGNATURE_ALGO is set when the signature’s algorithm is invalid and unsupported.

- CORRUPTED_SIGNATURE: CORRUPTED_SIGNATURE is set when the raw signature is corrupted, i.e. wrong base64 encoding.

- GENERIC_ERROR: GENERIC_ERROR is set when an error occurred during verification that cannot be associated with a specific status.

| Enum Values            |
|------------------------|
| UNSET                  |
| VERIFIED               |
| FAILED_VERIFICATION    |
| INVALID_SIGNATURE_ALGO |
| CORRUPTED_SIGNATURE    |
| GENERIC_ERROR          |

<a id="StorageIntegrationHealth_CommonObjectReference"></a>

## StorageIntegrationHealth

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| id |  |  | String |  |  |
| name |  |  | String |  |  |
| type |  |  | [StorageIntegrationHealthType](#StorageIntegrationHealthType_CommonObjectReference) |  | UNKNOWN, IMAGE_INTEGRATION, NOTIFIER, BACKUP, DECLARATIVE_CONFIG, |
| status |  |  | [StorageIntegrationHealthStatus](#StorageIntegrationHealthStatus_CommonObjectReference) |  | UNINITIALIZED, UNHEALTHY, HEALTHY, |
| errorMessage |  |  | String |  |  |
| lastTimestamp |  |  | Date |  | date-time |

<a id="StorageIntegrationHealthStatus_CommonObjectReference"></a>

## StorageIntegrationHealthStatus

| Enum Values   |
|---------------|
| UNINITIALIZED |
| UNHEALTHY     |
| HEALTHY       |

<a id="StorageIntegrationHealthType_CommonObjectReference"></a>

## StorageIntegrationHealthType

| Enum Values        |
|--------------------|
| UNKNOWN            |
| IMAGE_INTEGRATION  |
| NOTIFIER           |
| BACKUP             |
| DECLARATIVE_CONFIG |

<a id="StorageJira_CommonObjectReference"></a>

## StorageJira

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| url |  |  | String |  |  |
| username |  |  | String |  |  |
| password |  |  | String | The password for the integration. The server will mask the value of this credential in responses and logs. |  |
| issueType |  |  | String |  |  |
| priorityMappings |  |  | List of [JiraPriorityMapping](#JiraPriorityMapping_CommonObjectReference) |  |  |
| defaultFieldsJson |  |  | String |  |  |
| disablePriority |  |  | Boolean |  |  |

<a id="StorageK8sRole_CommonObjectReference"></a>

## StorageK8sRole

Properties of an individual k8s Role or ClusterRole. ////////////////////////////////////////

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| id |  |  | String |  |  |
| name |  |  | String |  |  |
| namespace |  |  | String |  |  |
| clusterId |  |  | String |  |  |
| clusterName |  |  | String |  |  |
| clusterRole |  |  | Boolean |  |  |
| labels |  |  | Map of `string` |  |  |
| annotations |  |  | Map of `string` |  |  |
| createdAt |  |  | Date |  | date-time |
| rules |  |  | List of [StoragePolicyRule](#StoragePolicyRule_CommonObjectReference) |  |  |

<a id="StorageK8sRoleBinding_CommonObjectReference"></a>

## StorageK8sRoleBinding

Properties of an individual k8s RoleBinding or ClusterRoleBinding. ////////////////////////////////////////

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| id |  |  | String |  |  |
| name |  |  | String |  |  |
| namespace |  |  | String |  |  |
| clusterId |  |  | String |  |  |
| clusterName |  |  | String |  |  |
| clusterRole |  |  | Boolean | ClusterRole specifies whether the binding binds a cluster role. However, it cannot be used to determine whether the binding is a cluster role binding. This can be done in conjunction with the namespace. If the namespace is empty and cluster role is true, the binding is a cluster role binding. |  |
| labels |  |  | Map of `string` |  |  |
| annotations |  |  | Map of `string` |  |  |
| createdAt |  |  | Date |  | date-time |
| subjects |  |  | List of [StorageSubject](#StorageSubject_CommonObjectReference) |  |  |
| roleId |  |  | String |  |  |

<a id="StorageKeyValuePair_CommonObjectReference"></a>

## StorageKeyValuePair

| Field Name | Required | Nullable | Type   | Description | Format |
|------------|----------|----------|--------|-------------|--------|
| key        |          |          | String |             |        |
| value      |          |          | String |             |        |

<a id="StorageL4Protocol_CommonObjectReference"></a>

## StorageL4Protocol

| Enum Values         |
|---------------------|
| L4_PROTOCOL_UNKNOWN |
| L4_PROTOCOL_TCP     |
| L4_PROTOCOL_UDP     |
| L4_PROTOCOL_ICMP    |
| L4_PROTOCOL_RAW     |
| L4_PROTOCOL_SCTP    |
| L4_PROTOCOL_ANY     |

<a id="StorageLabelSelector_CommonObjectReference"></a>

## StorageLabelSelector

Label selector components are joined with logical AND, see <https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/>

Next available tag: 3

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| matchLabels |  |  | Map of `string` | This is actually a oneof, but we can’t make it one due to backwards compatibility constraints. |  |
| requirements |  |  | List of [LabelSelectorRequirement](#LabelSelectorRequirement_CommonObjectReference) |  |  |

<a id="StorageLabelSelectorOperator_CommonObjectReference"></a>

## StorageLabelSelectorOperator

| Enum Values |
|-------------|
| UNKNOWN     |
| IN          |
| NOT_IN      |
| EXISTS      |
| NOT_EXISTS  |

<a id="StorageLicense_CommonObjectReference"></a>

## StorageLicense

| Field Name | Required | Nullable | Type   | Description | Format |
|------------|----------|----------|--------|-------------|--------|
| name       |          |          | String |             |        |
| type       |          |          | String |             |        |
| url        |          |          | String |             |        |

<a id="StorageLifecycleStage_CommonObjectReference"></a>

## StorageLifecycleStage

| Enum Values |
|-------------|
| DEPLOY      |
| BUILD       |
| RUNTIME     |

<a id="StorageListAlert_CommonObjectReference"></a>

## StorageListAlert

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| id |  |  | String |  |  |
| lifecycleStage |  |  | [StorageLifecycleStage](#StorageLifecycleStage_CommonObjectReference) |  | DEPLOY, BUILD, RUNTIME, |
| time |  |  | Date |  | date-time |
| policy |  |  | [StorageListAlertPolicy](#StorageListAlertPolicy_CommonObjectReference) |  |  |
| state |  |  | [StorageViolationState](#StorageViolationState_CommonObjectReference) |  | ACTIVE, RESOLVED, ATTEMPTED, |
| enforcementCount |  |  | Integer |  | int32 |
| enforcementAction |  |  | [StorageEnforcementAction](#StorageEnforcementAction_CommonObjectReference) |  | UNSET_ENFORCEMENT, SCALE_TO_ZERO_ENFORCEMENT, UNSATISFIABLE_NODE_CONSTRAINT_ENFORCEMENT, KILL_POD_ENFORCEMENT, FAIL_BUILD_ENFORCEMENT, FAIL_KUBE_REQUEST_ENFORCEMENT, FAIL_DEPLOYMENT_CREATE_ENFORCEMENT, FAIL_DEPLOYMENT_UPDATE_ENFORCEMENT, |
| commonEntityInfo |  |  | [ListAlertCommonEntityInfo](#ListAlertCommonEntityInfo_CommonObjectReference) |  |  |
| deployment |  |  | [StorageListAlertDeployment](#StorageListAlertDeployment_CommonObjectReference) |  |  |
| resource |  |  | [ListAlertResourceEntity](#ListAlertResourceEntity_CommonObjectReference) |  |  |
| node |  |  | [ListAlertNodeEntity](#ListAlertNodeEntity_CommonObjectReference) |  |  |

<a id="StorageListAlertDeployment_CommonObjectReference"></a>

## StorageListAlertDeployment

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| id |  |  | String |  |  |
| name |  |  | String |  |  |
| clusterName |  |  | String | This field is deprecated and can be found in CommonEntityInfo. It will be removed from here in a future release. This field has moved to CommonEntityInfo |  |
| namespace |  |  | String | This field is deprecated and can be found in CommonEntityInfo. It will be removed from here in a future release. This field has moved to CommonEntityInfo |  |
| clusterId |  |  | String | This field is deprecated and can be found in CommonEntityInfo. It will be removed from here in a future release. This field has moved to CommonEntityInfo |  |
| inactive |  |  | Boolean |  |  |
| namespaceId |  |  | String | This field is deprecated and can be found in CommonEntityInfo. It will be removed from here in a future release. This field has moved to CommonEntityInfo |  |
| deploymentType |  |  | String |  |  |

<a id="StorageListAlertPolicy_CommonObjectReference"></a>

## StorageListAlertPolicy

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| id |  |  | String |  |  |
| name |  |  | String |  |  |
| severity |  |  | [StorageSeverity](#StorageSeverity_CommonObjectReference) |  | UNSET_SEVERITY, LOW_SEVERITY, MEDIUM_SEVERITY, HIGH_SEVERITY, CRITICAL_SEVERITY, |
| description |  |  | String |  |  |
| categories |  |  | List of `string` |  |  |
| developerInternalFields |  |  | [ListAlertPolicyDevFields](#ListAlertPolicyDevFields_CommonObjectReference) |  |  |

<a id="StorageListAlertResourceType_CommonObjectReference"></a>

## StorageListAlertResourceType

A special ListAlert-only enumeration of all resource types. Unlike Alert.Resource.ResourceType this also includes deployment and node as types This must be kept in sync with Alert.Resource.ResourceType (excluding the deployment and node values)

| Enum Values                  |
|------------------------------|
| DEPLOYMENT                   |
| SECRETS                      |
| CONFIGMAPS                   |
| CLUSTER_ROLES                |
| CLUSTER_ROLE_BINDINGS        |
| NETWORK_POLICIES             |
| SECURITY_CONTEXT_CONSTRAINTS |
| EGRESS_FIREWALLS             |
| NODE                         |

<a id="StorageListDeployment_CommonObjectReference"></a>

## StorageListDeployment

Next available tag: 9

| Field Name | Required | Nullable | Type   | Description | Format    |
|------------|----------|----------|--------|-------------|-----------|
| id         |          |          | String |             |           |
| hash       |          |          | String |             | uint64    |
| name       |          |          | String |             |           |
| cluster    |          |          | String |             |           |
| clusterId  |          |          | String |             |           |
| namespace  |          |          | String |             |           |
| created    |          |          | Date   |             | date-time |
| priority   |          |          | String |             | int64     |

<a id="StorageListImage_CommonObjectReference"></a>

## StorageListImage

| Field Name  | Required | Nullable | Type    | Description | Format    |
|-------------|----------|----------|---------|-------------|-----------|
| id          |          |          | String  |             |           |
| name        |          |          | String  |             |           |
| components  |          |          | Integer |             | int32     |
| cves        |          |          | Integer |             | int32     |
| fixableCves |          |          | Integer |             | int32     |
| created     |          |          | Date    |             | date-time |
| lastUpdated |          |          | Date    |             | date-time |
| priority    |          |          | String  |             | int64     |

<a id="StorageListPolicy_CommonObjectReference"></a>

## StorageListPolicy

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| id |  |  | String |  |  |
| name |  |  | String |  |  |
| description |  |  | String |  |  |
| severity |  |  | [StorageSeverity](#StorageSeverity_CommonObjectReference) |  | UNSET_SEVERITY, LOW_SEVERITY, MEDIUM_SEVERITY, HIGH_SEVERITY, CRITICAL_SEVERITY, |
| disabled |  |  | Boolean |  |  |
| lifecycleStages |  |  | List of [StorageLifecycleStage](#StorageLifecycleStage_CommonObjectReference) |  |  |
| notifiers |  |  | List of `string` |  |  |
| lastUpdated |  |  | Date |  | date-time |
| eventSource |  |  | [StorageEventSource](#StorageEventSource_CommonObjectReference) |  | NOT_APPLICABLE, DEPLOYMENT_EVENT, AUDIT_LOG_EVENT, NODE_EVENT, |
| isDefault |  |  | Boolean |  |  |
| source |  |  | [StoragePolicySource](#StoragePolicySource_CommonObjectReference) |  | IMPERATIVE, DECLARATIVE, |

<a id="StorageListSecret_CommonObjectReference"></a>

## StorageListSecret

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| id |  |  | String |  |  |
| name |  |  | String |  |  |
| clusterId |  |  | String |  |  |
| clusterName |  |  | String |  |  |
| namespace |  |  | String |  |  |
| types |  |  | List of [StorageSecretType](#StorageSecretType_CommonObjectReference) |  |  |
| createdAt |  |  | Date |  | date-time |

<a id="StorageLivenessProbe_CommonObjectReference"></a>

## StorageLivenessProbe

| Field Name | Required | Nullable | Type    | Description | Format |
|------------|----------|----------|---------|-------------|--------|
| defined    |          |          | Boolean |             |        |

<a id="StorageLoginNotice_CommonObjectReference"></a>

## StorageLoginNotice

| Field Name | Required | Nullable | Type    | Description | Format |
|------------|----------|----------|---------|-------------|--------|
| enabled    |          |          | Boolean |             |        |
| text       |          |          | String  |             |        |

<a id="StorageManagerType_CommonObjectReference"></a>

## StorageManagerType

| Enum Values                      |
|----------------------------------|
| MANAGER_TYPE_UNKNOWN             |
| MANAGER_TYPE_MANUAL              |
| MANAGER_TYPE_HELM_CHART          |
| MANAGER_TYPE_KUBERNETES_OPERATOR |

<a id="StorageMatchType_CommonObjectReference"></a>

## StorageMatchType

| Enum Values |
|-------------|
| EXACT       |
| REGEX       |

<a id="StorageMicrosoftSentinel_CommonObjectReference"></a>

## StorageMicrosoftSentinel

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| logIngestionEndpoint |  |  | String | log_ingestion_endpoint is the log ingestion endpoint. |  |
| directoryTenantId |  |  | String | directory_tenant_id contains the ID of the Microsoft Directory ID of the selected tenant. |  |
| applicationClientId |  |  | String | application_client_id contains the ID of the application ID of the service principal. |  |
| secret |  |  | String | secret contains the client secret. |  |
| alertDcrConfig |  |  | [MicrosoftSentinelDataCollectionRuleConfig](#MicrosoftSentinelDataCollectionRuleConfig_CommonObjectReference) |  |  |
| auditLogDcrConfig |  |  | [MicrosoftSentinelDataCollectionRuleConfig](#MicrosoftSentinelDataCollectionRuleConfig_CommonObjectReference) |  |  |
| clientCertAuthConfig |  |  | [MicrosoftSentinelClientCertAuthConfig](#MicrosoftSentinelClientCertAuthConfig_CommonObjectReference) |  |  |
| wifEnabled |  |  | Boolean | Enables authentication with short-lived tokens using Azure managed identities or Azure workload identities. The toggle exists to make the use of Azure default credentials explicit rather than always using them as a fallback. The explicit behavior is more consistent with other integrations. |  |

<a id="StorageMitreAttackVector_CommonObjectReference"></a>

## StorageMitreAttackVector

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| tactic |  |  | [StorageMitreTactic](#StorageMitreTactic_CommonObjectReference) |  |  |
| techniques |  |  | List of [StorageMitreTechnique](#StorageMitreTechnique_CommonObjectReference) |  |  |

<a id="StorageMitreTactic_CommonObjectReference"></a>

## StorageMitreTactic

| Field Name  | Required | Nullable | Type   | Description | Format |
|-------------|----------|----------|--------|-------------|--------|
| id          |          |          | String |             |        |
| name        |          |          | String |             |        |
| description |          |          | String |             |        |

<a id="StorageMitreTechnique_CommonObjectReference"></a>

## StorageMitreTechnique

| Field Name  | Required | Nullable | Type   | Description | Format |
|-------------|----------|----------|--------|-------------|--------|
| id          |          |          | String |             |        |
| name        |          |          | String |             |        |
| description |          |          | String |             |        |

<a id="StorageNamespaceMetadata_CommonObjectReference"></a>

## StorageNamespaceMetadata

| Field Name   | Required | Nullable | Type            | Description | Format    |
|--------------|----------|----------|-----------------|-------------|-----------|
| id           |          |          | String          |             |           |
| name         |          |          | String          |             |           |
| clusterId    |          |          | String          |             |           |
| clusterName  |          |          | String          |             |           |
| labels       |          |          | Map of `string` |             |           |
| creationTime |          |          | Date            |             | date-time |
| priority     |          |          | String          |             | int64     |
| annotations  |          |          | Map of `string` |             |           |

<a id="StorageNetworkBaseline_CommonObjectReference"></a>

## StorageNetworkBaseline

NetworkBaseline represents a network baseline of a deployment. It contains all the baseline peers and their respective connections. next available tag: 8

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| deploymentId |  |  | String | This is the ID of the baseline. |  |
| clusterId |  |  | String |  |  |
| namespace |  |  | String |  |  |
| peers |  |  | List of [StorageNetworkBaselinePeer](#StorageNetworkBaselinePeer_CommonObjectReference) |  |  |
| forbiddenPeers |  |  | List of [StorageNetworkBaselinePeer](#StorageNetworkBaselinePeer_CommonObjectReference) | A list of peers that will never be added to the baseline. For now, this contains peers that the user has manually removed. This is used to ensure we don’t add it back in the event we see the flow again. |  |
| observationPeriodEnd |  |  | Date |  | date-time |
| locked |  |  | Boolean |  |  |
| deploymentName |  |  | String |  |  |

<a id="StorageNetworkBaselineConnectionProperties_CommonObjectReference"></a>

## StorageNetworkBaselineConnectionProperties

NetworkBaselineConnectionProperties represents information about a baseline connection next available tag: 4

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| ingress |  |  | Boolean |  |  |
| port |  |  | Long |  | int64 |
| protocol |  |  | [StorageL4Protocol](#StorageL4Protocol_CommonObjectReference) |  | L4_PROTOCOL_UNKNOWN, L4_PROTOCOL_TCP, L4_PROTOCOL_UDP, L4_PROTOCOL_ICMP, L4_PROTOCOL_RAW, L4_PROTOCOL_SCTP, L4_PROTOCOL_ANY, |

<a id="StorageNetworkBaselinePeer_CommonObjectReference"></a>

## StorageNetworkBaselinePeer

NetworkBaselinePeer represents a baseline peer. next available tag: 3

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| entity |  |  | [StorageNetworkEntity](#StorageNetworkEntity_CommonObjectReference) |  |  |
| properties |  |  | List of [StorageNetworkBaselineConnectionProperties](#StorageNetworkBaselineConnectionProperties_CommonObjectReference) |  |  |

<a id="StorageNetworkEntity_CommonObjectReference"></a>

## StorageNetworkEntity

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| info |  |  | [StorageNetworkEntityInfo](#StorageNetworkEntityInfo_CommonObjectReference) |  |  |
| scope |  |  | [StorageNetworkEntityScope](#StorageNetworkEntityScope_CommonObjectReference) |  |  |

<a id="StorageNetworkEntityInfo_CommonObjectReference"></a>

## StorageNetworkEntityInfo

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| type |  |  | [StorageNetworkEntityInfoType](#StorageNetworkEntityInfoType_CommonObjectReference) |  | UNKNOWN_TYPE, DEPLOYMENT, INTERNET, LISTEN_ENDPOINT, EXTERNAL_SOURCE, INTERNAL_ENTITIES, |
| id |  |  | String |  |  |
| deployment |  |  | [NetworkEntityInfoDeployment](#NetworkEntityInfoDeployment_CommonObjectReference) |  |  |
| externalSource |  |  | [NetworkEntityInfoExternalSource](#NetworkEntityInfoExternalSource_CommonObjectReference) |  |  |

<a id="StorageNetworkEntityInfoType_CommonObjectReference"></a>

## StorageNetworkEntityInfoType

- INTERNAL_ENTITIES: INTERNAL_ENTITIES is for grouping all internal entities under a single network graph node

| Enum Values       |
|-------------------|
| UNKNOWN_TYPE      |
| DEPLOYMENT        |
| INTERNET          |
| LISTEN_ENDPOINT   |
| EXTERNAL_SOURCE   |
| INTERNAL_ENTITIES |

<a id="StorageNetworkEntityScope_CommonObjectReference"></a>

## StorageNetworkEntityScope

| Field Name | Required | Nullable | Type   | Description | Format |
|------------|----------|----------|--------|-------------|--------|
| clusterId  |          |          | String |             |        |

<a id="StorageNetworkFlow_CommonObjectReference"></a>

## StorageNetworkFlow

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| props |  |  | [StorageNetworkFlowProperties](#StorageNetworkFlowProperties_CommonObjectReference) |  |  |
| lastSeenTimestamp |  |  | Date |  | date-time |
| clusterId |  |  | String |  |  |
| updatedAt |  |  | Date |  | date-time |

<a id="StorageNetworkFlowProperties_CommonObjectReference"></a>

## StorageNetworkFlowProperties

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| srcEntity |  |  | [StorageNetworkEntityInfo](#StorageNetworkEntityInfo_CommonObjectReference) |  |  |
| dstEntity |  |  | [StorageNetworkEntityInfo](#StorageNetworkEntityInfo_CommonObjectReference) |  |  |
| dstPort |  |  | Long | may be 0 if not applicable (e.g., icmp). | int64 |
| l4protocol |  |  | [StorageL4Protocol](#StorageL4Protocol_CommonObjectReference) |  | L4_PROTOCOL_UNKNOWN, L4_PROTOCOL_TCP, L4_PROTOCOL_UDP, L4_PROTOCOL_ICMP, L4_PROTOCOL_RAW, L4_PROTOCOL_SCTP, L4_PROTOCOL_ANY, |

<a id="StorageNetworkGraphConfig_CommonObjectReference"></a>

## StorageNetworkGraphConfig

| Field Name              | Required | Nullable | Type    | Description | Format |
|-------------------------|----------|----------|---------|-------------|--------|
| id                      |          |          | String  |             |        |
| hideDefaultExternalSrcs |          |          | Boolean |             |        |

<a id="StorageNetworkPolicy_CommonObjectReference"></a>

## StorageNetworkPolicy

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| id |  |  | String |  |  |
| name |  |  | String |  |  |
| clusterId |  |  | String |  |  |
| clusterName |  |  | String |  |  |
| namespace |  |  | String |  |  |
| labels |  |  | Map of `string` |  |  |
| annotations |  |  | Map of `string` |  |  |
| spec |  |  | [StorageNetworkPolicySpec](#StorageNetworkPolicySpec_CommonObjectReference) |  |  |
| yaml |  |  | String |  |  |
| apiVersion |  |  | String |  |  |
| created |  |  | Date |  | date-time |

<a id="StorageNetworkPolicyApplicationUndoRecord_CommonObjectReference"></a>

## StorageNetworkPolicyApplicationUndoRecord

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| clusterId |  |  | String |  |  |
| user |  |  | String |  |  |
| applyTimestamp |  |  | Date |  | date-time |
| originalModification |  |  | [StorageNetworkPolicyModification](#StorageNetworkPolicyModification_CommonObjectReference) |  |  |
| undoModification |  |  | [StorageNetworkPolicyModification](#StorageNetworkPolicyModification_CommonObjectReference) |  |  |

<a id="StorageNetworkPolicyEgressRule_CommonObjectReference"></a>

## StorageNetworkPolicyEgressRule

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| ports |  |  | List of [StorageNetworkPolicyPort](#StorageNetworkPolicyPort_CommonObjectReference) |  |  |
| to |  |  | List of [StorageNetworkPolicyPeer](#StorageNetworkPolicyPeer_CommonObjectReference) |  |  |

<a id="StorageNetworkPolicyIngressRule_CommonObjectReference"></a>

## StorageNetworkPolicyIngressRule

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| ports |  |  | List of [StorageNetworkPolicyPort](#StorageNetworkPolicyPort_CommonObjectReference) |  |  |
| from |  |  | List of [StorageNetworkPolicyPeer](#StorageNetworkPolicyPeer_CommonObjectReference) |  |  |

<a id="StorageNetworkPolicyModification_CommonObjectReference"></a>

## StorageNetworkPolicyModification

Next available tag: 3

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| applyYaml |  |  | String |  |  |
| toDelete |  |  | List of [StorageNetworkPolicyReference](#StorageNetworkPolicyReference_CommonObjectReference) |  |  |

<a id="StorageNetworkPolicyPeer_CommonObjectReference"></a>

## StorageNetworkPolicyPeer

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| podSelector |  |  | [StorageLabelSelector](#StorageLabelSelector_CommonObjectReference) |  |  |
| namespaceSelector |  |  | [StorageLabelSelector](#StorageLabelSelector_CommonObjectReference) |  |  |
| ipBlock |  |  | [StorageIPBlock](#StorageIPBlock_CommonObjectReference) |  |  |

<a id="StorageNetworkPolicyPort_CommonObjectReference"></a>

## StorageNetworkPolicyPort

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| protocol |  |  | [StorageProtocol](#StorageProtocol_CommonObjectReference) |  | UNSET_PROTOCOL, TCP_PROTOCOL, UDP_PROTOCOL, SCTP_PROTOCOL, |
| port |  |  | Integer |  | int32 |
| portName |  |  | String |  |  |

<a id="StorageNetworkPolicyReference_CommonObjectReference"></a>

## StorageNetworkPolicyReference

Next available tag: 3

| Field Name | Required | Nullable | Type   | Description | Format |
|------------|----------|----------|--------|-------------|--------|
| namespace  |          |          | String |             |        |
| name       |          |          | String |             |        |

<a id="StorageNetworkPolicySpec_CommonObjectReference"></a>

## StorageNetworkPolicySpec

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| podSelector |  |  | [StorageLabelSelector](#StorageLabelSelector_CommonObjectReference) |  |  |
| ingress |  |  | List of [StorageNetworkPolicyIngressRule](#StorageNetworkPolicyIngressRule_CommonObjectReference) |  |  |
| egress |  |  | List of [StorageNetworkPolicyEgressRule](#StorageNetworkPolicyEgressRule_CommonObjectReference) |  |  |
| policyTypes |  |  | List of [StorageNetworkPolicyType](#StorageNetworkPolicyType_CommonObjectReference) |  |  |

<a id="StorageNetworkPolicyType_CommonObjectReference"></a>

## StorageNetworkPolicyType

| Enum Values                 |
|-----------------------------|
| UNSET_NETWORK_POLICY_TYPE   |
| INGRESS_NETWORK_POLICY_TYPE |
| EGRESS_NETWORK_POLICY_TYPE  |

<a id="StorageNode_CommonObjectReference"></a>

## StorageNode

Node represents information about a node in the cluster. next available tag: 28

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| id |  |  | String | A unique ID identifying this node. |  |
| name |  |  | String | The (host)name of the node. Might or might not be the same as ID. |  |
| taints |  |  | List of [StorageTaint](#StorageTaint_CommonObjectReference) |  |  |
| clusterId |  |  | String |  |  |
| clusterName |  |  | String |  |  |
| labels |  |  | Map of `string` |  |  |
| annotations |  |  | Map of `string` |  |  |
| joinedAt |  |  | Date |  | date-time |
| internalIpAddresses |  |  | List of `string` |  |  |
| externalIpAddresses |  |  | List of `string` |  |  |
| containerRuntimeVersion |  |  | String | Use container_runtime.version |  |
| containerRuntime |  |  | [StorageContainerRuntimeInfo](#StorageContainerRuntimeInfo_CommonObjectReference) |  |  |
| kernelVersion |  |  | String |  |  |
| operatingSystem |  |  | String | From NodeInfo. Operating system reported by the node (ex: linux). |  |
| osImage |  |  | String | From NodeInfo. OS image reported by the node from /etc/os-release. |  |
| kubeletVersion |  |  | String |  |  |
| kubeProxyVersion |  |  | String |  |  |
| lastUpdated |  |  | Date |  | date-time |
| k8sUpdated |  |  | Date | Time we received an update from Kubernetes. | date-time |
| scan |  |  | [StorageNodeScan](#StorageNodeScan_CommonObjectReference) |  |  |
| components |  |  | Integer |  | int32 |
| cves |  |  | Integer |  | int32 |
| fixableCves |  |  | Integer |  | int32 |
| priority |  |  | String |  | int64 |
| riskScore |  |  | Float |  | float |
| topCvss |  |  | Float |  | float |
| notes |  |  | List of [StorageNodeNote](#StorageNodeNote_CommonObjectReference) |  |  |

<a id="StorageNodeNote_CommonObjectReference"></a>

## StorageNodeNote

| Enum Values       |
|-------------------|
| MISSING_SCAN_DATA |

<a id="StorageNodeScan_CommonObjectReference"></a>

## StorageNodeScan

Next tag: 5

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| scanTime |  |  | Date |  | date-time |
| operatingSystem |  |  | String |  |  |
| components |  |  | List of [StorageEmbeddedNodeScanComponent](#StorageEmbeddedNodeScanComponent_CommonObjectReference) |  |  |
| notes |  |  | List of [StorageNodeScanNote](#StorageNodeScanNote_CommonObjectReference) |  |  |
| scannerVersion |  |  | [NodeScanScanner](#NodeScanScanner_CommonObjectReference) |  | SCANNER, SCANNER_V4, |

<a id="StorageNodeScanNote_CommonObjectReference"></a>

## StorageNodeScanNote

| Enum Values                     |
|---------------------------------|
| UNSET                           |
| UNSUPPORTED                     |
| KERNEL_UNSUPPORTED              |
| CERTIFIED_RHEL_CVES_UNAVAILABLE |

<a id="StorageNodeVulnerability_CommonObjectReference"></a>

## StorageNodeVulnerability

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| cveBaseInfo |  |  | [StorageCVEInfo](#StorageCVEInfo_CommonObjectReference) |  |  |
| cvss |  |  | Float |  | float |
| severity |  |  | [StorageVulnerabilitySeverity](#StorageVulnerabilitySeverity_CommonObjectReference) |  | UNKNOWN_VULNERABILITY_SEVERITY, LOW_VULNERABILITY_SEVERITY, MODERATE_VULNERABILITY_SEVERITY, IMPORTANT_VULNERABILITY_SEVERITY, CRITICAL_VULNERABILITY_SEVERITY, |
| fixedBy |  |  | String |  |  |
| snoozed |  |  | Boolean |  |  |
| snoozeStart |  |  | Date |  | date-time |
| snoozeExpiry |  |  | Date |  | date-time |

<a id="StorageNotifier_CommonObjectReference"></a>

## StorageNotifier

Next Tag: 21

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| id |  |  | String |  |  |
| name |  |  | String |  |  |
| type |  |  | String |  |  |
| uiEndpoint |  |  | String |  |  |
| labelKey |  |  | String |  |  |
| labelDefault |  |  | String |  |  |
| jira |  |  | [StorageJira](#StorageJira_CommonObjectReference) |  |  |
| email |  |  | [StorageEmail](#StorageEmail_CommonObjectReference) |  |  |
| cscc |  |  | [StorageCSCC](#StorageCSCC_CommonObjectReference) |  |  |
| splunk |  |  | [StorageSplunk](#StorageSplunk_CommonObjectReference) |  |  |
| pagerduty |  |  | [StoragePagerDuty](#StoragePagerDuty_CommonObjectReference) |  |  |
| generic |  |  | [StorageGeneric](#StorageGeneric_CommonObjectReference) |  |  |
| sumologic |  |  | [StorageSumoLogic](#StorageSumoLogic_CommonObjectReference) |  |  |
| awsSecurityHub |  |  | [StorageAWSSecurityHub](#StorageAWSSecurityHub_CommonObjectReference) |  |  |
| syslog |  |  | [StorageSyslog](#StorageSyslog_CommonObjectReference) |  |  |
| microsoftSentinel |  |  | [StorageMicrosoftSentinel](#StorageMicrosoftSentinel_CommonObjectReference) |  |  |
| notifierSecret |  |  | String |  |  |
| traits |  |  | [StorageTraits](#StorageTraits_CommonObjectReference) |  |  |

<a id="StorageNotifierConfiguration_CommonObjectReference"></a>

## StorageNotifierConfiguration

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| emailConfig |  |  | [StorageEmailNotifierConfiguration](#StorageEmailNotifierConfiguration_CommonObjectReference) |  |  |
| id |  |  | String |  |  |

<a id="StorageOperationStatus_CommonObjectReference"></a>

## StorageOperationStatus

| Enum Values |
|-------------|
| FAIL        |
| PASS        |

<a id="StorageOrchestratorMetadata_CommonObjectReference"></a>

## StorageOrchestratorMetadata

| Field Name       | Required | Nullable | Type             | Description | Format    |
|------------------|----------|----------|------------------|-------------|-----------|
| version          |          |          | String           |             |           |
| openshiftVersion |          |          | String           |             |           |
| buildDate        |          |          | Date             |             | date-time |
| apiVersions      |          |          | List of `string` |             |           |

<a id="StoragePagerDuty_CommonObjectReference"></a>

## StoragePagerDuty

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| apiKey |  |  | String | The API key for the integration. The server will mask the value of this credential in responses and logs. |  |

<a id="StoragePermissionLevel_CommonObjectReference"></a>

## StoragePermissionLevel

For any update to PermissionLevel, also update: - pkg/searchbasedpolicies/builders/k8s_rbac.go - ui/src/messages/common.js

| Enum Values           |
|-----------------------|
| UNSET                 |
| NONE                  |
| DEFAULT               |
| ELEVATED_IN_NAMESPACE |
| ELEVATED_CLUSTER_WIDE |
| CLUSTER_ADMIN         |

<a id="StoragePermissionSet_CommonObjectReference"></a>

## StoragePermissionSet

This encodes a set of permissions for StackRox resources.

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| id |  |  | String | id is generated and cannot be changed. |  |
| name |  |  | String | `name` and `description` are provided by the user and can be changed. |  |
| description |  |  | String |  |  |
| resourceToAccess |  |  | Map of [StorageAccess](#StorageAccess_CommonObjectReference) |  |  |
| traits |  |  | [StorageTraits](#StorageTraits_CommonObjectReference) |  |  |

<a id="StoragePlatformComponentConfig_CommonObjectReference"></a>

## StoragePlatformComponentConfig

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| rules |  |  | List of [PlatformComponentConfigRule](#PlatformComponentConfigRule_CommonObjectReference) |  |  |
| needsReevaluation |  |  | Boolean |  |  |

<a id="StoragePod_CommonObjectReference"></a>

## StoragePod

Pod represents information for a currently running pod or deleted pod in an active deployment.

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| id |  |  | String |  |  |
| name |  |  | String |  |  |
| deploymentId |  |  | String |  |  |
| namespace |  |  | String |  |  |
| clusterId |  |  | String |  |  |
| liveInstances |  |  | List of [StorageContainerInstance](#StorageContainerInstance_CommonObjectReference) |  |  |
| terminatedInstances |  |  | List of [PodContainerInstanceList](#PodContainerInstanceList_CommonObjectReference) | Must be a list of lists, so we can perform search queries (does not work for maps that aren’t \<string, string\>) There is one bucket (list) per container name. |  |
| started |  |  | Date | Time Kubernetes reports the pod was created. | date-time |

<a id="StoragePolicy_CommonObjectReference"></a>

## StoragePolicy

Next tag: 28

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| id |  |  | String |  |  |
| name |  |  | String | Name of the policy. Must be unique. |  |
| description |  |  | String | Free-form text description of this policy. |  |
| rationale |  |  | String |  |  |
| remediation |  |  | String | Describes how to remediate a violation of this policy. |  |
| disabled |  |  | Boolean | Toggles whether or not this policy will be executing and actively firing alerts. |  |
| categories |  |  | List of `string` | List of categories that this policy falls under. Category names must already exist in Central. |  |
| lifecycleStages |  |  | List of [StorageLifecycleStage](#StorageLifecycleStage_CommonObjectReference) | Describes which policy lifecylce stages this policy applies to. Choices are DEPLOY, BUILD, and RUNTIME. |  |
| eventSource |  |  | [StorageEventSource](#StorageEventSource_CommonObjectReference) |  | NOT_APPLICABLE, DEPLOYMENT_EVENT, AUDIT_LOG_EVENT, NODE_EVENT, |
| exclusions |  |  | List of [StorageExclusion](#StorageExclusion_CommonObjectReference) | Define deployments or images that should be excluded from this policy. |  |
| scope |  |  | List of [StorageScope](#StorageScope_CommonObjectReference) | Defines clusters, namespaces, and deployments that should be included in this policy. No scopes defined includes everything. |  |
| severity |  |  | [StorageSeverity](#StorageSeverity_CommonObjectReference) |  | UNSET_SEVERITY, LOW_SEVERITY, MEDIUM_SEVERITY, HIGH_SEVERITY, CRITICAL_SEVERITY, |
| enforcementActions |  |  | List of [StorageEnforcementAction](#StorageEnforcementAction_CommonObjectReference) | FAIL_DEPLOYMENT_CREATE_ENFORCEMENT takes effect only if admission control webhook is configured to enforce on object creates/updates. FAIL_KUBE_REQUEST_ENFORCEMENT takes effect only if admission control webhook is enabled to listen on exec and port-forward events. FAIL_DEPLOYMENT_UPDATE_ENFORCEMENT takes effect only if admission control webhook is configured to enforce on object updates. Lists the enforcement actions to take when a violation from this policy is identified. Possible value are UNSET_ENFORCEMENT, SCALE_TO_ZERO_ENFORCEMENT, UNSATISFIABLE_NODE_CONSTRAINT_ENFORCEMENT, KILL_POD_ENFORCEMENT, FAIL_BUILD_ENFORCEMENT, FAIL_KUBE_REQUEST_ENFORCEMENT, FAIL_DEPLOYMENT_CREATE_ENFORCEMENT, and. FAIL_DEPLOYMENT_UPDATE_ENFORCEMENT. |  |
| notifiers |  |  | List of `string` | List of IDs of the notifiers that should be triggered when a violation from this policy is identified. IDs should be in the form of a UUID and are found through the Central API. |  |
| lastUpdated |  |  | Date |  | date-time |
| SORTName |  |  | String | For internal use only. |  |
| SORTLifecycleStage |  |  | String | For internal use only. |  |
| SORTEnforcement |  |  | Boolean | For internal use only. |  |
| policyVersion |  |  | String |  |  |
| policySections |  |  | List of [StoragePolicySection](#StoragePolicySection_CommonObjectReference) | PolicySections define the violation criteria for this policy. |  |
| mitreAttackVectors |  |  | List of [PolicyMitreAttackVectors](#PolicyMitreAttackVectors_CommonObjectReference) |  |  |
| criteriaLocked |  |  | Boolean | Read-only field. If true, the policy’s criteria fields are rendered read-only. |  |
| mitreVectorsLocked |  |  | Boolean | Read-only field. If true, the policy’s MITRE ATT&CK fields are rendered read-only. |  |
| isDefault |  |  | Boolean | Read-only field. Indicates the policy is a default policy if true and a custom policy if false. |  |
| source |  |  | [StoragePolicySource](#StoragePolicySource_CommonObjectReference) |  | IMPERATIVE, DECLARATIVE, |

<a id="StoragePolicyGroup_CommonObjectReference"></a>

## StoragePolicyGroup

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| fieldName |  |  | String | Defines which field on a deployment or image this PolicyGroup evaluates. See <https://docs.openshift.com/acs/operating/manage-security-policies.html#policy-criteria_manage-security-policies> for a complete list of possible values. |  |
| booleanOperator |  |  | [StorageBooleanOperator](#StorageBooleanOperator_CommonObjectReference) |  | OR, AND, |
| negate |  |  | Boolean | Determines if the evaluation of this PolicyGroup is negated. Default to false. |  |
| values |  |  | List of [StoragePolicyValue](#StoragePolicyValue_CommonObjectReference) |  |  |

<a id="StoragePolicyRule_CommonObjectReference"></a>

## StoragePolicyRule

Properties of an individual rules that grant permissions to resources. ////////////////////////////////////////

| Field Name      | Required | Nullable | Type             | Description | Format |
|-----------------|----------|----------|------------------|-------------|--------|
| verbs           |          |          | List of `string` |             |        |
| apiGroups       |          |          | List of `string` |             |        |
| resources       |          |          | List of `string` |             |        |
| nonResourceUrls |          |          | List of `string` |             |        |
| resourceNames   |          |          | List of `string` |             |        |

<a id="StoragePolicySection_CommonObjectReference"></a>

## StoragePolicySection

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| sectionName |  |  | String |  |  |
| policyGroups |  |  | List of [StoragePolicyGroup](#StoragePolicyGroup_CommonObjectReference) | The set of policies groups that make up this section. Each group can be considered an individual criterion. |  |

<a id="StoragePolicySource_CommonObjectReference"></a>

## StoragePolicySource

| Enum Values |
|-------------|
| IMPERATIVE  |
| DECLARATIVE |

<a id="StoragePolicyValue_CommonObjectReference"></a>

## StoragePolicyValue

| Field Name | Required | Nullable | Type   | Description | Format |
|------------|----------|----------|--------|-------------|--------|
| value      |          |          | String |             |        |

<a id="StoragePortConfig_CommonObjectReference"></a>

## StoragePortConfig

Next Available Tag: 6

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| name |  |  | String |  |  |
| containerPort |  |  | Integer |  | int32 |
| protocol |  |  | String |  |  |
| exposure |  |  | [PortConfigExposureLevel](#PortConfigExposureLevel_CommonObjectReference) |  | UNSET, EXTERNAL, NODE, INTERNAL, HOST, ROUTE, |
| exposedPort |  |  | Integer |  | int32 |
| exposureInfos |  |  | List of [PortConfigExposureInfo](#PortConfigExposureInfo_CommonObjectReference) |  |  |

<a id="StoragePrivateConfig_CommonObjectReference"></a>

## StoragePrivateConfig

next available tag: 10

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| DEPRECATEDAlertRetentionDurationDays |  |  | Integer |  | int32 |
| alertConfig |  |  | [StorageAlertRetentionConfig](#StorageAlertRetentionConfig_CommonObjectReference) |  |  |
| imageRetentionDurationDays |  |  | Integer |  | int32 |
| expiredVulnReqRetentionDurationDays |  |  | Integer |  | int32 |
| decommissionedClusterRetention |  |  | [StorageDecommissionedClusterRetentionConfig](#StorageDecommissionedClusterRetentionConfig_CommonObjectReference) |  |  |
| reportRetentionConfig |  |  | [StorageReportRetentionConfig](#StorageReportRetentionConfig_CommonObjectReference) |  |  |
| vulnerabilityExceptionConfig |  |  | [StorageVulnerabilityExceptionConfig](#StorageVulnerabilityExceptionConfig_CommonObjectReference) |  |  |
| administrationEventsConfig |  |  | [StorageAdministrationEventsConfig](#StorageAdministrationEventsConfig_CommonObjectReference) |  |  |
| metrics |  |  | [StoragePrometheusMetrics](#StoragePrometheusMetrics_CommonObjectReference) |  |  |

<a id="StorageProcessBaseline_CommonObjectReference"></a>

## StorageProcessBaseline

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| id |  |  | String |  |  |
| key |  |  | [StorageProcessBaselineKey](#StorageProcessBaselineKey_CommonObjectReference) |  |  |
| elements |  |  | List of [StorageBaselineElement](#StorageBaselineElement_CommonObjectReference) |  |  |
| elementGraveyard |  |  | List of [StorageBaselineElement](#StorageBaselineElement_CommonObjectReference) |  |  |
| created |  |  | Date |  | date-time |
| userLockedTimestamp |  |  | Date |  | date-time |
| stackRoxLockedTimestamp |  |  | Date |  | date-time |
| lastUpdate |  |  | Date |  | date-time |

<a id="StorageProcessBaselineKey_CommonObjectReference"></a>

## StorageProcessBaselineKey

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| deploymentId |  |  | String | The idea is for the keys to be flexible. Only certain combinations of these will be supported. |  |
| containerName |  |  | String |  |  |
| clusterId |  |  | String |  |  |
| namespace |  |  | String |  |  |

<a id="StorageProcessIndicator_CommonObjectReference"></a>

## StorageProcessIndicator

Next available tag: 13

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| id |  |  | String |  |  |
| deploymentId |  |  | String |  |  |
| containerName |  |  | String |  |  |
| podId |  |  | String |  |  |
| podUid |  |  | String |  |  |
| signal |  |  | [StorageProcessSignal](#StorageProcessSignal_CommonObjectReference) |  |  |
| clusterId |  |  | String |  |  |
| namespace |  |  | String |  |  |
| containerStartTime |  |  | Date |  | date-time |
| imageId |  |  | String |  |  |

<a id="StorageProcessListeningOnPort_CommonObjectReference"></a>

## StorageProcessListeningOnPort

The API returns an array of these

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| endpoint |  |  | [ProcessListeningOnPortEndpoint](#ProcessListeningOnPortEndpoint_CommonObjectReference) |  |  |
| deploymentId |  |  | String |  |  |
| containerName |  |  | String |  |  |
| podId |  |  | String |  |  |
| podUid |  |  | String |  |  |
| signal |  |  | [StorageProcessSignal](#StorageProcessSignal_CommonObjectReference) |  |  |
| clusterId |  |  | String |  |  |
| namespace |  |  | String |  |  |
| containerStartTime |  |  | Date |  | date-time |
| imageId |  |  | String |  |  |

<a id="StorageProcessSignal_CommonObjectReference"></a>

## StorageProcessSignal

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| id |  |  | String | A unique UUID for identifying the message We have this here instead of at the top level because we want to have each message to be self contained. |  |
| containerId |  |  | String |  |  |
| time |  |  | Date |  | date-time |
| name |  |  | String |  |  |
| args |  |  | String |  |  |
| execFilePath |  |  | String |  |  |
| pid |  |  | Long |  | int64 |
| uid |  |  | Long |  | int64 |
| gid |  |  | Long |  | int64 |
| lineage |  |  | List of `string` |  |  |
| scraped |  |  | Boolean |  |  |
| lineageInfo |  |  | List of [ProcessSignalLineageInfo](#ProcessSignalLineageInfo_CommonObjectReference) |  |  |

<a id="StoragePrometheusMetrics_CommonObjectReference"></a>

## StoragePrometheusMetrics

next available tag: 4

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| imageVulnerabilities |  |  | [PrometheusMetricsGroup](#PrometheusMetricsGroup_CommonObjectReference) |  |  |
| policyViolations |  |  | [PrometheusMetricsGroup](#PrometheusMetricsGroup_CommonObjectReference) |  |  |
| nodeVulnerabilities |  |  | [PrometheusMetricsGroup](#PrometheusMetricsGroup_CommonObjectReference) |  |  |

<a id="StorageProtocol_CommonObjectReference"></a>

## StorageProtocol

| Enum Values    |
|----------------|
| UNSET_PROTOCOL |
| TCP_PROTOCOL   |
| UDP_PROTOCOL   |
| SCTP_PROTOCOL  |

<a id="StorageProviderMetadata_CommonObjectReference"></a>

## StorageProviderMetadata

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| region |  |  | String |  |  |
| zone |  |  | String |  |  |
| google |  |  | [StorageGoogleProviderMetadata](#StorageGoogleProviderMetadata_CommonObjectReference) |  |  |
| aws |  |  | [StorageAWSProviderMetadata](#StorageAWSProviderMetadata_CommonObjectReference) |  |  |
| azure |  |  | [StorageAzureProviderMetadata](#StorageAzureProviderMetadata_CommonObjectReference) |  |  |
| verified |  |  | Boolean |  |  |
| cluster |  |  | [StorageClusterMetadata](#StorageClusterMetadata_CommonObjectReference) |  |  |

<a id="StoragePublicConfig_CommonObjectReference"></a>

## StoragePublicConfig

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| loginNotice |  |  | [StorageLoginNotice](#StorageLoginNotice_CommonObjectReference) |  |  |
| header |  |  | [StorageBannerConfig](#StorageBannerConfig_CommonObjectReference) |  |  |
| footer |  |  | [StorageBannerConfig](#StorageBannerConfig_CommonObjectReference) |  |  |
| telemetry |  |  | [StorageTelemetryConfiguration](#StorageTelemetryConfiguration_CommonObjectReference) |  |  |

<a id="StorageQuayConfig_CommonObjectReference"></a>

## StorageQuayConfig

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| endpoint |  |  | String |  |  |
| oauthToken |  |  | String | The OAuth token for the integration. Required if this is a scanner integration. The server will mask the value of this credential in responses and logs. |  |
| insecure |  |  | Boolean |  |  |
| registryRobotCredentials |  |  | [QuayConfigRobotAccount](#QuayConfigRobotAccount_CommonObjectReference) |  |  |

<a id="StorageReadinessProbe_CommonObjectReference"></a>

## StorageReadinessProbe

| Field Name | Required | Nullable | Type    | Description | Format |
|------------|----------|----------|---------|-------------|--------|
| defined    |          |          | Boolean |             |        |

<a id="StorageReportConfiguration_CommonObjectReference"></a>

## StorageReportConfiguration

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| id |  |  | String |  |  |
| name |  |  | String |  |  |
| description |  |  | String |  |  |
| type |  |  | [ReportConfigurationReportType](#ReportConfigurationReportType_CommonObjectReference) |  | VULNERABILITY, |
| vulnReportFilters |  |  | [StorageVulnerabilityReportFilters](#StorageVulnerabilityReportFilters_CommonObjectReference) |  |  |
| scopeId |  |  | String |  |  |
| emailConfig |  |  | [StorageEmailNotifierConfiguration](#StorageEmailNotifierConfiguration_CommonObjectReference) |  |  |
| schedule |  |  | [StorageSchedule](#StorageSchedule_CommonObjectReference) |  |  |
| lastRunStatus |  |  | [StorageReportLastRunStatus](#StorageReportLastRunStatus_CommonObjectReference) |  |  |
| lastSuccessfulRunTime |  |  | Date |  | date-time |
| resourceScope |  |  | [StorageResourceScope](#StorageResourceScope_CommonObjectReference) |  |  |
| notifiers |  |  | List of [StorageNotifierConfiguration](#StorageNotifierConfiguration_CommonObjectReference) |  |  |
| creator |  |  | [StorageSlimUser](#StorageSlimUser_CommonObjectReference) |  |  |
| version |  |  | Integer |  | int32 |

<a id="StorageReportLastRunStatus_CommonObjectReference"></a>

## StorageReportLastRunStatus

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| reportStatus |  |  | [ReportLastRunStatusRunStatus](#ReportLastRunStatusRunStatus_CommonObjectReference) |  | SUCCESS, FAILURE, |
| lastRunTime |  |  | Date |  | date-time |
| errorMsg |  |  | String |  |  |

<a id="StorageReportRetentionConfig_CommonObjectReference"></a>

## StorageReportRetentionConfig

next available tag: 4

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| historyRetentionDurationDays |  |  | Long |  | int64 |
| downloadableReportRetentionDays |  |  | Long |  | int64 |
| downloadableReportGlobalRetentionBytes |  |  | Long |  | int64 |

<a id="StorageResourceCollection_CommonObjectReference"></a>

## StorageResourceCollection

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| id |  |  | String |  |  |
| name |  |  | String |  |  |
| description |  |  | String |  |  |
| createdAt |  |  | Date |  | date-time |
| lastUpdated |  |  | Date |  | date-time |
| createdBy |  |  | [StorageSlimUser](#StorageSlimUser_CommonObjectReference) |  |  |
| updatedBy |  |  | [StorageSlimUser](#StorageSlimUser_CommonObjectReference) |  |  |
| resourceSelectors |  |  | List of [StorageResourceSelector](#StorageResourceSelector_CommonObjectReference) | `resource_selectors` resolve as disjunction (OR) with each-other and with selectors from `embedded_collections`. For MVP, the size of resource_selectors will at most be 1 from UX standpoint. |  |
| embeddedCollections |  |  | List of [ResourceCollectionEmbeddedResourceCollection](#ResourceCollectionEmbeddedResourceCollection_CommonObjectReference) |  |  |

<a id="StorageResourceScope_CommonObjectReference"></a>

## StorageResourceScope

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| collectionId |  |  | String |  |  |
| entityScope |  |  | [StorageEntityScope](#StorageEntityScope_CommonObjectReference) |  |  |

<a id="StorageResourceSelector_CommonObjectReference"></a>

## StorageResourceSelector

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| rules |  |  | List of [StorageSelectorRule](#StorageSelectorRule_CommonObjectReference) | `rules` resolve as a conjunction (AND). |  |

<a id="StorageResources_CommonObjectReference"></a>

## StorageResources

| Field Name      | Required | Nullable | Type  | Description | Format |
|-----------------|----------|----------|-------|-------------|--------|
| cpuCoresRequest |          |          | Float |             | float  |
| cpuCoresLimit   |          |          | Float |             | float  |
| memoryMbRequest |          |          | Float |             | float  |
| memoryMbLimit   |          |          | Float |             | float  |

<a id="StorageRisk_CommonObjectReference"></a>

## StorageRisk

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| id |  |  | String |  |  |
| subject |  |  | [StorageRiskSubject](#StorageRiskSubject_CommonObjectReference) |  |  |
| score |  |  | Float |  | float |
| results |  |  | List of [RiskResult](#RiskResult_CommonObjectReference) |  |  |

<a id="StorageRiskSubject_CommonObjectReference"></a>

## StorageRiskSubject

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| id |  |  | String |  |  |
| namespace |  |  | String |  |  |
| clusterId |  |  | String |  |  |
| type |  |  | [StorageRiskSubjectType](#StorageRiskSubjectType_CommonObjectReference) |  | UNKNOWN, DEPLOYMENT, NAMESPACE, CLUSTER, NODE, NODE_COMPONENT, IMAGE, IMAGE_COMPONENT, SERVICEACCOUNT, |

<a id="StorageRiskSubjectType_CommonObjectReference"></a>

## StorageRiskSubjectType

Next tag: 9

| Enum Values     |
|-----------------|
| UNKNOWN         |
| DEPLOYMENT      |
| NAMESPACE       |
| CLUSTER         |
| NODE            |
| NODE_COMPONENT  |
| IMAGE           |
| IMAGE_COMPONENT |
| SERVICEACCOUNT  |

<a id="StorageRole_CommonObjectReference"></a>

## StorageRole

A role specifies which actions are allowed for which subset of cluster objects. Permissions be can either specified directly via setting resource_to_access together with global_access or by referencing a permission set by its id in permission_set_name.

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| name |  |  | String | `name` and `description` are provided by the user and can be changed. |  |
| description |  |  | String |  |  |
| permissionSetId |  |  | String | The associated PermissionSet and AccessScope for this Role. |  |
| accessScopeId |  |  | String |  |  |
| globalAccess |  |  | [StorageAccess](#StorageAccess_CommonObjectReference) |  | NO_ACCESS, READ_ACCESS, READ_WRITE_ACCESS, |
| resourceToAccess |  |  | Map of [StorageAccess](#StorageAccess_CommonObjectReference) | Deprecated 2021-04-20 in favor of `permission_set_id`. |  |
| traits |  |  | [StorageTraits](#StorageTraits_CommonObjectReference) |  |  |

<a id="StorageRuleValue_CommonObjectReference"></a>

## StorageRuleValue

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| value |  |  | String |  |  |
| matchType |  |  | [StorageMatchType](#StorageMatchType_CommonObjectReference) |  | EXACT, REGEX, |

<a id="StorageS3Compatible_CommonObjectReference"></a>

## StorageS3Compatible

S3Compatible configures the backup integration with an S3 compatible storage provider. S3 compatible is intended for non-AWS providers. For AWS S3 use S3Config.

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| bucket |  |  | String |  |  |
| accessKeyId |  |  | String | The access key ID to use. The server will mask the value of this credential in responses and logs. |  |
| secretAccessKey |  |  | String | The secret access key to use. The server will mask the value of this credential in responses and logs. |  |
| region |  |  | String |  |  |
| objectPrefix |  |  | String |  |  |
| endpoint |  |  | String |  |  |
| urlStyle |  |  | [StorageS3URLStyle](#StorageS3URLStyle_CommonObjectReference) |  | S3_URL_STYLE_UNSPECIFIED, S3_URL_STYLE_VIRTUAL_HOSTED, S3_URL_STYLE_PATH, |

<a id="StorageS3Config_CommonObjectReference"></a>

## StorageS3Config

S3Config configures the backup integration with AWS S3.

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| bucket |  |  | String |  |  |
| useIam |  |  | Boolean |  |  |
| accessKeyId |  |  | String | The access key ID for the storage integration. The server will mask the value of this credential in responses and logs. |  |
| secretAccessKey |  |  | String | The secret access key for the storage integration. The server will mask the value of this credential in responses and logs. |  |
| region |  |  | String |  |  |
| objectPrefix |  |  | String |  |  |
| endpoint |  |  | String |  |  |

<a id="StorageS3URLStyle_CommonObjectReference"></a>

## StorageS3URLStyle

| Enum Values                 |
|-----------------------------|
| S3_URL_STYLE_UNSPECIFIED    |
| S3_URL_STYLE_VIRTUAL_HOSTED |
| S3_URL_STYLE_PATH           |

<a id="StorageScannerHealthInfo_CommonObjectReference"></a>

## StorageScannerHealthInfo

ScannerHealthInfo represents health info of a scanner instance that is deployed on a secured cluster (so called "local scanner"). When the scanner is deployed on a central cluster, the following message is NOT used. ScannerHealthInfo carries data about scanner deployment but does not include scanner health status derived from this data. Aggregated scanner health status is not included because it is derived in central and not in the component that first reports ScannerHealthInfo (sensor).

The following fields are made optional/nullable because there can be errors when trying to obtain them and the default value of 0 might be confusing with the actual value 0. In case an error happens when trying to obtain a certain field, it will be absent (instead of having the default value).

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| totalDesiredAnalyzerPods |  |  | Integer |  | int32 |
| totalReadyAnalyzerPods |  |  | Integer |  | int32 |
| totalDesiredDbPods |  |  | Integer |  | int32 |
| totalReadyDbPods |  |  | Integer |  | int32 |
| statusErrors |  |  | List of `string` | Collection of errors that occurred while trying to obtain scanner health info. |  |

<a id="StorageScannerV4Config_CommonObjectReference"></a>

## StorageScannerV4Config

| Field Name         | Required | Nullable | Type    | Description | Format |
|--------------------|----------|----------|---------|-------------|--------|
| numConcurrentScans |          |          | Integer |             | int32  |
| indexerEndpoint    |          |          | String  |             |        |
| matcherEndpoint    |          |          | String  |             |        |

<a id="StorageSchedule_CommonObjectReference"></a>

## StorageSchedule

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| intervalType |  |  | [ScheduleIntervalType](#ScheduleIntervalType_CommonObjectReference) |  | UNSET, DAILY, WEEKLY, MONTHLY, |
| hour |  |  | Integer |  | int32 |
| minute |  |  | Integer |  | int32 |
| weekly |  |  | [ScheduleWeeklyInterval](#ScheduleWeeklyInterval_CommonObjectReference) |  |  |
| daysOfWeek |  |  | [ScheduleDaysOfWeek](#ScheduleDaysOfWeek_CommonObjectReference) |  |  |
| daysOfMonth |  |  | [ScheduleDaysOfMonth](#ScheduleDaysOfMonth_CommonObjectReference) |  |  |

<a id="StorageScope_CommonObjectReference"></a>

## StorageScope

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| cluster |  |  | String |  |  |
| namespace |  |  | String |  |  |
| label |  |  | [StorageScopeLabel](#StorageScopeLabel_CommonObjectReference) |  |  |
| clusterLabel |  |  | [StorageScopeLabel](#StorageScopeLabel_CommonObjectReference) |  |  |
| namespaceLabel |  |  | [StorageScopeLabel](#StorageScopeLabel_CommonObjectReference) |  |  |

<a id="StorageScopeLabel_CommonObjectReference"></a>

## StorageScopeLabel

| Field Name | Required | Nullable | Type   | Description | Format |
|------------|----------|----------|--------|-------------|--------|
| key        |          |          | String |             |        |
| value      |          |          | String |             |        |

<a id="StorageSecret_CommonObjectReference"></a>

## StorageSecret

Flat secret object. Any properties of an individual secret. (regardless of time, scope, or context) ////////////////////////////////////////

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| id |  |  | String |  |  |
| name |  |  | String |  |  |
| clusterId |  |  | String |  |  |
| clusterName |  |  | String |  |  |
| namespace |  |  | String |  |  |
| type |  |  | String |  |  |
| labels |  |  | Map of `string` |  |  |
| annotations |  |  | Map of `string` |  |  |
| createdAt |  |  | Date |  | date-time |
| files |  |  | List of [StorageSecretDataFile](#StorageSecretDataFile_CommonObjectReference) | Metadata about the secrets. The secret need not be a file, but rather may be an arbitrary value. |  |
| relationship |  |  | [StorageSecretRelationship](#StorageSecretRelationship_CommonObjectReference) |  |  |

<a id="StorageSecretContainerRelationship_CommonObjectReference"></a>

## StorageSecretContainerRelationship

Secrets can be mounted in a path in a container. Next Tag: 3

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| id |  |  | String | Id of the container the secret is mounted in. |  |
| path |  |  | String | Path is a container specific mounting directory. |  |

<a id="StorageSecretDataFile_CommonObjectReference"></a>

## StorageSecretDataFile

Metadata about secret. Additional information is presented for a certificate file and imagePullSecret, but the "file" may also represent some arbitrary value.

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| name |  |  | String |  |  |
| type |  |  | [StorageSecretType](#StorageSecretType_CommonObjectReference) |  | UNDETERMINED, PUBLIC_CERTIFICATE, CERTIFICATE_REQUEST, PRIVACY_ENHANCED_MESSAGE, OPENSSH_PRIVATE_KEY, PGP_PRIVATE_KEY, EC_PRIVATE_KEY, RSA_PRIVATE_KEY, DSA_PRIVATE_KEY, CERT_PRIVATE_KEY, ENCRYPTED_PRIVATE_KEY, IMAGE_PULL_SECRET, |
| cert |  |  | [StorageCert](#StorageCert_CommonObjectReference) |  |  |
| imagePullSecret |  |  | [StorageImagePullSecret](#StorageImagePullSecret_CommonObjectReference) |  |  |

<a id="StorageSecretDeploymentRelationship_CommonObjectReference"></a>

## StorageSecretDeploymentRelationship

Secrets can be used by a deployment. Next Tag: 3

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| id |  |  | String | Id of the deployment using the secret within a container. |  |
| name |  |  | String | Name of the deployment. |  |

<a id="StorageSecretRelationship_CommonObjectReference"></a>

## StorageSecretRelationship

The combined relationships that belong to the secret. Next Tag: 6

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| id |  |  | String |  |  |
| containerRelationships |  |  | List of [StorageSecretContainerRelationship](#StorageSecretContainerRelationship_CommonObjectReference) |  |  |
| deploymentRelationships |  |  | List of [StorageSecretDeploymentRelationship](#StorageSecretDeploymentRelationship_CommonObjectReference) | Deployment id to relationship. |  |

<a id="StorageSecretType_CommonObjectReference"></a>

## StorageSecretType

| Enum Values              |
|--------------------------|
| UNDETERMINED             |
| PUBLIC_CERTIFICATE       |
| CERTIFICATE_REQUEST      |
| PRIVACY_ENHANCED_MESSAGE |
| OPENSSH_PRIVATE_KEY      |
| PGP_PRIVATE_KEY          |
| EC_PRIVATE_KEY           |
| RSA_PRIVATE_KEY          |
| DSA_PRIVATE_KEY          |
| CERT_PRIVATE_KEY         |
| ENCRYPTED_PRIVATE_KEY    |
| IMAGE_PULL_SECRET        |

<a id="StorageSecurityContext_CommonObjectReference"></a>

## StorageSecurityContext

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| privileged |  |  | Boolean |  |  |
| selinux |  |  | [SecurityContextSELinux](#SecurityContextSELinux_CommonObjectReference) |  |  |
| dropCapabilities |  |  | List of `string` |  |  |
| addCapabilities |  |  | List of `string` |  |  |
| readOnlyRootFilesystem |  |  | Boolean |  |  |
| seccompProfile |  |  | [SecurityContextSeccompProfile](#SecurityContextSeccompProfile_CommonObjectReference) |  |  |
| allowPrivilegeEscalation |  |  | Boolean |  |  |

<a id="StorageSelectorRule_CommonObjectReference"></a>

## StorageSelectorRule

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| fieldName |  |  | String |  |  |
| operator |  |  | [StorageBooleanOperator](#StorageBooleanOperator_CommonObjectReference) |  | OR, AND, |
| values |  |  | List of [StorageRuleValue](#StorageRuleValue_CommonObjectReference) | `values` resolve as a conjunction (AND) or disjunction (OR) depending on operator. For MVP, only OR is supported from UX standpoint. |  |

<a id="StorageSensorDeploymentIdentification_CommonObjectReference"></a>

## StorageSensorDeploymentIdentification

StackRoxDeploymentIdentification aims at uniquely identifying a StackRox Sensor deployment. It is used to determine whether a sensor connection comes from a sensor pod that has restarted or was recreated (possibly after a network partition), or from a deployment in a different namespace or cluster.

| Field Name          | Required | Nullable | Type   | Description | Format |
|---------------------|----------|----------|--------|-------------|--------|
| systemNamespaceId   |          |          | String |             |        |
| defaultNamespaceId  |          |          | String |             |        |
| appNamespace        |          |          | String |             |        |
| appNamespaceId      |          |          | String |             |        |
| appServiceaccountId |          |          | String |             |        |
| k8sNodeName         |          |          | String |             |        |

<a id="StorageSensorUpgradeConfig_CommonObjectReference"></a>

## StorageSensorUpgradeConfig

SensorUpgradeConfig encapsulates configuration relevant to sensor auto-upgrades.

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| enableAutoUpgrade |  |  | Boolean | Whether to automatically trigger upgrades for out-of-date sensors. |  |

<a id="StorageServiceAccount_CommonObjectReference"></a>

## StorageServiceAccount

Any properties of an individual service account. (regardless of time, scope, or context) ////////////////////////////////////////

| Field Name       | Required | Nullable | Type             | Description | Format    |
|------------------|----------|----------|------------------|-------------|-----------|
| id               |          |          | String           |             |           |
| name             |          |          | String           |             |           |
| namespace        |          |          | String           |             |           |
| clusterName      |          |          | String           |             |           |
| clusterId        |          |          | String           |             |           |
| labels           |          |          | Map of `string`  |             |           |
| annotations      |          |          | Map of `string`  |             |           |
| createdAt        |          |          | Date             |             | date-time |
| automountToken   |          |          | Boolean          |             |           |
| secrets          |          |          | List of `string` |             |           |
| imagePullSecrets |          |          | List of `string` |             |           |

<a id="StorageServiceIdentity_CommonObjectReference"></a>

## StorageServiceIdentity

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| serialStr |  |  | String |  |  |
| serial |  |  | String |  | int64 |
| id |  |  | String |  |  |
| type |  |  | [StorageServiceType](#StorageServiceType_CommonObjectReference) |  | UNKNOWN_SERVICE, SENSOR_SERVICE, CENTRAL_SERVICE, CENTRAL_DB_SERVICE, REMOTE_SERVICE, COLLECTOR_SERVICE, MONITORING_UI_SERVICE, MONITORING_DB_SERVICE, MONITORING_CLIENT_SERVICE, BENCHMARK_SERVICE, SCANNER_SERVICE, SCANNER_DB_SERVICE, ADMISSION_CONTROL_SERVICE, SCANNER_V4_INDEXER_SERVICE, SCANNER_V4_MATCHER_SERVICE, SCANNER_V4_DB_SERVICE, SCANNER_V4_SERVICE, REGISTRANT_SERVICE, |
| initBundleId |  |  | String |  |  |

<a id="StorageServiceType_CommonObjectReference"></a>

## StorageServiceType

Next available tag: 18

- SCANNER_V4_SERVICE: This is used when Scanner V4 is run in combo-mode.

| Enum Values                |
|----------------------------|
| UNKNOWN_SERVICE            |
| SENSOR_SERVICE             |
| CENTRAL_SERVICE            |
| CENTRAL_DB_SERVICE         |
| REMOTE_SERVICE             |
| COLLECTOR_SERVICE          |
| MONITORING_UI_SERVICE      |
| MONITORING_DB_SERVICE      |
| MONITORING_CLIENT_SERVICE  |
| BENCHMARK_SERVICE          |
| SCANNER_SERVICE            |
| SCANNER_DB_SERVICE         |
| ADMISSION_CONTROL_SERVICE  |
| SCANNER_V4_INDEXER_SERVICE |
| SCANNER_V4_MATCHER_SERVICE |
| SCANNER_V4_DB_SERVICE      |
| SCANNER_V4_SERVICE         |
| REGISTRANT_SERVICE         |

<a id="StorageSetBasedLabelSelector_CommonObjectReference"></a>

## StorageSetBasedLabelSelector

SetBasedLabelSelector only allows set-based label requirements.

Next available tag: 3

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| requirements |  |  | List of [SetBasedLabelSelectorRequirement](#SetBasedLabelSelectorRequirement_CommonObjectReference) |  |  |

<a id="StorageSeverity_CommonObjectReference"></a>

## StorageSeverity

| Enum Values       |
|-------------------|
| UNSET_SEVERITY    |
| LOW_SEVERITY      |
| MEDIUM_SEVERITY   |
| HIGH_SEVERITY     |
| CRITICAL_SEVERITY |

<a id="StorageSignature_CommonObjectReference"></a>

## StorageSignature

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| cosign |  |  | [StorageCosignSignature](#StorageCosignSignature_CommonObjectReference) |  |  |

<a id="StorageSignatureIntegration_CommonObjectReference"></a>

## StorageSignatureIntegration

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| id |  |  | String |  |  |
| name |  |  | String |  |  |
| cosign |  |  | [StorageCosignPublicKeyVerification](#StorageCosignPublicKeyVerification_CommonObjectReference) |  |  |
| cosignCertificates |  |  | List of [StorageCosignCertificateVerification](#StorageCosignCertificateVerification_CommonObjectReference) |  |  |
| transparencyLog |  |  | [StorageTransparencyLogVerification](#StorageTransparencyLogVerification_CommonObjectReference) |  |  |
| traits |  |  | [StorageTraits](#StorageTraits_CommonObjectReference) |  |  |

<a id="StorageSimpleAccessScope_CommonObjectReference"></a>

## StorageSimpleAccessScope

Simple access scope is a (simple) selection criteria for scoped resources. It does **not** allow multi-component AND-rules nor set operations on names.

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| id |  |  | String | `id` is generated and cannot be changed. |  |
| name |  |  | String | `name` and `description` are provided by the user and can be changed. |  |
| description |  |  | String |  |  |
| rules |  |  | [SimpleAccessScopeRules](#SimpleAccessScopeRules_CommonObjectReference) |  |  |
| traits |  |  | [StorageTraits](#StorageTraits_CommonObjectReference) |  |  |

<a id="StorageSlimUser_CommonObjectReference"></a>

## StorageSlimUser

| Field Name | Required | Nullable | Type   | Description | Format |
|------------|----------|----------|--------|-------------|--------|
| id         |          |          | String |             |        |
| name       |          |          | String |             |        |

<a id="StorageSource_CommonObjectReference"></a>

## StorageSource

| Enum Values    |
|----------------|
| SOURCE_UNKNOWN |
| SOURCE_RED_HAT |
| SOURCE_OSV     |
| SOURCE_NVD     |

<a id="StorageSourceType_CommonObjectReference"></a>

## StorageSourceType

| Enum Values       |
|-------------------|
| OS                |
| PYTHON            |
| JAVA              |
| RUBY              |
| NODEJS            |
| GO                |
| DOTNETCORERUNTIME |
| INFRASTRUCTURE    |

<a id="StorageSplunk_CommonObjectReference"></a>

## StorageSplunk

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| httpToken |  |  | String | The HTTP token for the integration. The server will mask the value of this credential in responses and logs. |  |
| httpEndpoint |  |  | String |  |  |
| insecure |  |  | Boolean |  |  |
| truncate |  |  | String |  | int64 |
| auditLoggingEnabled |  |  | Boolean |  |  |
| derivedSourceType |  |  | Boolean |  |  |
| sourceTypes |  |  | Map of `string` |  |  |

<a id="StorageStaticClusterConfig_CommonObjectReference"></a>

## StorageStaticClusterConfig

The difference between Static and Dynamic cluster config is that Static values are not sent over the Central to Sensor gRPC connection. They are used, for example, to generate manifests that can be used to set up the Secured Cluster’s k8s components. They are **not** dynamically reloaded.

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| type |  |  | [StorageClusterType](#StorageClusterType_CommonObjectReference) |  | GENERIC_CLUSTER, KUBERNETES_CLUSTER, OPENSHIFT_CLUSTER, OPENSHIFT4_CLUSTER, |
| mainImage |  |  | String |  |  |
| centralApiEndpoint |  |  | String |  |  |
| collectionMethod |  |  | [StorageCollectionMethod](#StorageCollectionMethod_CommonObjectReference) |  | UNSET_COLLECTION, NO_COLLECTION, KERNEL_MODULE, EBPF, CORE_BPF, |
| collectorImage |  |  | String |  |  |
| admissionController |  |  | Boolean |  |  |
| admissionControllerUpdates |  |  | Boolean |  |  |
| tolerationsConfig |  |  | [StorageTolerationsConfig](#StorageTolerationsConfig_CommonObjectReference) |  |  |
| slimCollector |  |  | Boolean |  |  |
| admissionControllerEvents |  |  | Boolean |  |  |
| admissionControllerFailOnError |  |  | Boolean |  |  |

<a id="StorageSubject_CommonObjectReference"></a>

## StorageSubject

Properties of an individual subjects who are granted roles via role bindings. ////////////////////////////////////////

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| id |  |  | String |  |  |
| kind |  |  | [StorageSubjectKind](#StorageSubjectKind_CommonObjectReference) |  | UNSET_KIND, SERVICE_ACCOUNT, USER, GROUP, |
| name |  |  | String |  |  |
| namespace |  |  | String |  |  |
| clusterId |  |  | String |  |  |
| clusterName |  |  | String |  |  |

<a id="StorageSubjectKind_CommonObjectReference"></a>

## StorageSubjectKind

| Enum Values     |
|-----------------|
| UNSET_KIND      |
| SERVICE_ACCOUNT |
| USER            |
| GROUP           |

<a id="StorageSumoLogic_CommonObjectReference"></a>

## StorageSumoLogic

| Field Name        | Required | Nullable | Type    | Description | Format |
|-------------------|----------|----------|---------|-------------|--------|
| httpSourceAddress |          |          | String  |             |        |
| skipTLSVerify     |          |          | Boolean |             |        |

<a id="StorageSyslog_CommonObjectReference"></a>

## StorageSyslog

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| localFacility |  |  | [SyslogLocalFacility](#SyslogLocalFacility_CommonObjectReference) |  | LOCAL0, LOCAL1, LOCAL2, LOCAL3, LOCAL4, LOCAL5, LOCAL6, LOCAL7, |
| tcpConfig |  |  | [SyslogTCPConfig](#SyslogTCPConfig_CommonObjectReference) |  |  |
| extraFields |  |  | List of [StorageKeyValuePair](#StorageKeyValuePair_CommonObjectReference) |  |  |
| messageFormat |  |  | [SyslogMessageFormat](#SyslogMessageFormat_CommonObjectReference) |  | LEGACY, CEF, |
| maxMessageSize |  |  | Integer |  | int32 |

<a id="StorageTaint_CommonObjectReference"></a>

## StorageTaint

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| key |  |  | String |  |  |
| value |  |  | String |  |  |
| taintEffect |  |  | [StorageTaintEffect](#StorageTaintEffect_CommonObjectReference) |  | UNKNOWN_TAINT_EFFECT, NO_SCHEDULE_TAINT_EFFECT, PREFER_NO_SCHEDULE_TAINT_EFFECT, NO_EXECUTE_TAINT_EFFECT, |

<a id="StorageTaintEffect_CommonObjectReference"></a>

## StorageTaintEffect

| Enum Values                     |
|---------------------------------|
| UNKNOWN_TAINT_EFFECT            |
| NO_SCHEDULE_TAINT_EFFECT        |
| PREFER_NO_SCHEDULE_TAINT_EFFECT |
| NO_EXECUTE_TAINT_EFFECT         |

<a id="StorageTelemetryConfiguration_CommonObjectReference"></a>

## StorageTelemetryConfiguration

| Field Name  | Required | Nullable | Type    | Description | Format    |
|-------------|----------|----------|---------|-------------|-----------|
| enabled     |          |          | Boolean |             |           |
| lastSetTime |          |          | Date    |             | date-time |

<a id="StorageTokenMetadata_CommonObjectReference"></a>

## StorageTokenMetadata

Next available tag: 8

| Field Name | Required | Nullable | Type             | Description | Format    |
|------------|----------|----------|------------------|-------------|-----------|
| id         |          |          | String           |             |           |
| name       |          |          | String           |             |           |
| roles      |          |          | List of `string` |             |           |
| issuedAt   |          |          | Date             |             | date-time |
| expiration |          |          | Date             |             | date-time |
| revoked    |          |          | Boolean          |             |           |
| role       |          |          | String           |             |           |

<a id="StorageToleration_CommonObjectReference"></a>

## StorageToleration

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| key |  |  | String |  |  |
| operator |  |  | [StorageTolerationOperator](#StorageTolerationOperator_CommonObjectReference) |  | TOLERATION_OPERATION_UNKNOWN, TOLERATION_OPERATOR_EXISTS, TOLERATION_OPERATOR_EQUAL, |
| value |  |  | String |  |  |
| taintEffect |  |  | [StorageTaintEffect](#StorageTaintEffect_CommonObjectReference) |  | UNKNOWN_TAINT_EFFECT, NO_SCHEDULE_TAINT_EFFECT, PREFER_NO_SCHEDULE_TAINT_EFFECT, NO_EXECUTE_TAINT_EFFECT, |

<a id="StorageTolerationOperator_CommonObjectReference"></a>

## StorageTolerationOperator

| Enum Values                  |
|------------------------------|
| TOLERATION_OPERATION_UNKNOWN |
| TOLERATION_OPERATOR_EXISTS   |
| TOLERATION_OPERATOR_EQUAL    |

<a id="StorageTolerationsConfig_CommonObjectReference"></a>

## StorageTolerationsConfig

| Field Name | Required | Nullable | Type    | Description | Format |
|------------|----------|----------|---------|-------------|--------|
| disabled   |          |          | Boolean |             |        |

<a id="StorageTraits_CommonObjectReference"></a>

## StorageTraits

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| mutabilityMode |  |  | [StorageTraitsMutabilityMode](#StorageTraitsMutabilityMode_CommonObjectReference) |  | ALLOW_MUTATE, ALLOW_MUTATE_FORCED, |
| visibility |  |  | [StorageTraitsVisibility](#StorageTraitsVisibility_CommonObjectReference) |  | VISIBLE, HIDDEN, |
| origin |  |  | [StorageTraitsOrigin](#StorageTraitsOrigin_CommonObjectReference) |  | IMPERATIVE, DEFAULT, DECLARATIVE, DECLARATIVE_ORPHANED, EPHEMERAL, |
| expiresAt |  |  | Date | expires_at specifies when this object should be considered expired and eligible for pruning. This field is optional. Objects without an expires_at value are never pruned based on expiry. Currently used for dynamically created RBAC objects (roles, permission sets, access scopes) that are generated by the internal token API for sensors. | date-time |

<a id="StorageTraitsMutabilityMode_CommonObjectReference"></a>

## StorageTraitsMutabilityMode

EXPERIMENTAL. NOTE: Please refer from using MutabilityMode for the time being. It will be replaced in the future (ROX-14276). MutabilityMode specifies whether and how an object can be modified. Default is ALLOW_MUTATE and means there are no modification restrictions; this is equivalent to the absence of MutabilityMode specification. ALLOW_MUTATE_FORCED forbids all modifying operations except object removal with force bit on.

Be careful when changing the state of this field. For example, modifying an object from ALLOW_MUTATE to ALLOW_MUTATE_FORCED is allowed but will prohibit any further changes to it, including modifying it back to ALLOW_MUTATE.

| Enum Values         |
|---------------------|
| ALLOW_MUTATE        |
| ALLOW_MUTATE_FORCED |

<a id="StorageTraitsOrigin_CommonObjectReference"></a>

## StorageTraitsOrigin

Origin specifies the origin of an object. Objects can have five different origins: - IMPERATIVE: the object was created via the API. This is assumed by default. - DEFAULT: the object is a default object, such as default roles, access scopes etc. - DECLARATIVE: the object is created via declarative configuration. - DECLARATIVE_ORPHANED: the object is created via declarative configuration and then unsuccessfully deleted(for example, because it is referenced by another object) - EPHEMERAL: the object is created via an internal API, generated on the fly and meant to be ephemeral. Based on the origin, different rules apply to the objects. Objects with the DECLARATIVE origin are not allowed to be modified via API, only via declarative configuration. Additionally, they may not reference objects with the IMPERATIVE or EPHEMERAL origin. Objects with the DEFAULT origin are not allowed to be modified via either API or declarative configuration. They may be referenced by all other objects. Objects with the IMPERATIVE origin are allowed to be modified via API, not via declarative configuration. They may reference all other objects. Objects with the EPHEMERAL origin are neither allowed to be modified via API, nor via declarative configuration. They may reference all other objects. Objects with the DECLARATIVE_ORPHANED origin are not allowed to be modified via either API or declarative configuration. DECLARATIVE_ORPHANED resource can become DECLARATIVE again if it is redefined in declarative configuration. Objects with this origin will be cleaned up from the system immediately after they are not referenced by other resources anymore. They may be referenced by all other objects.

| Enum Values          |
|----------------------|
| IMPERATIVE           |
| DEFAULT              |
| DECLARATIVE          |
| DECLARATIVE_ORPHANED |
| EPHEMERAL            |

<a id="StorageTraitsVisibility_CommonObjectReference"></a>

## StorageTraitsVisibility

EXPERIMENTAL. visibility allows to specify whether the object should be visible for certain APIs.

| Enum Values |
|-------------|
| VISIBLE     |
| HIDDEN      |

<a id="StorageTransparencyLogVerification_CommonObjectReference"></a>

## StorageTransparencyLogVerification

Validate the inclusion of signature signing events into a transparency log.

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| enabled |  |  | Boolean | Validate the inclusion of signatures into a transparency log. Disables validation if not enabled. |  |
| url |  |  | String | The URL of the transparency log. Required for online confirmation of inclusion into the transparency log. Defaults to the Sigstore instance `rekor.sigstore.dev`. |  |
| validateOffline |  |  | Boolean | Force offline validation of the signature proof of inclusion into the transparency log. Do not fall back to request confirmation from the transparency log over network. |  |
| publicKeyPemEnc |  |  | String | PEM encoded public key used to validate the proof of inclusion into the transparency log. Defaults to the key of the public Sigstore instance if left empty. |  |

<a id="StorageUpgradeProgress_CommonObjectReference"></a>

## StorageUpgradeProgress

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| upgradeState |  |  | [UpgradeProgressUpgradeState](#UpgradeProgressUpgradeState_CommonObjectReference) |  | UPGRADE_INITIALIZING, UPGRADER_LAUNCHING, UPGRADER_LAUNCHED, PRE_FLIGHT_CHECKS_COMPLETE, UPGRADE_OPERATIONS_DONE, UPGRADE_COMPLETE, UPGRADE_INITIALIZATION_ERROR, PRE_FLIGHT_CHECKS_FAILED, UPGRADE_ERROR_ROLLING_BACK, UPGRADE_ERROR_ROLLED_BACK, UPGRADE_ERROR_ROLLBACK_FAILED, UPGRADE_ERROR_UNKNOWN, UPGRADE_TIMED_OUT, |
| upgradeStatusDetail |  |  | String |  |  |
| since |  |  | Date |  | date-time |

<a id="StorageUser_CommonObjectReference"></a>

## StorageUser

User is an object that allows us to track the roles a user is tied to, and how they logged in.

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| id |  |  | String |  |  |
| authProviderId |  |  | String |  |  |
| attributes |  |  | List of [StorageUserAttribute](#StorageUserAttribute_CommonObjectReference) |  |  |
| idpToken |  |  | String |  |  |

<a id="StorageUserAttribute_CommonObjectReference"></a>

## StorageUserAttribute

| Field Name | Required | Nullable | Type   | Description | Format |
|------------|----------|----------|--------|-------------|--------|
| key        |          |          | String |             |        |
| value      |          |          | String |             |        |

<a id="StorageUserInfo_CommonObjectReference"></a>

## StorageUserInfo

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| username |  |  | String |  |  |
| friendlyName |  |  | String |  |  |
| permissions |  |  | [UserInfoResourceToAccess](#UserInfoResourceToAccess_CommonObjectReference) |  |  |
| roles |  |  | List of [StorageUserInfoRole](#StorageUserInfoRole_CommonObjectReference) |  |  |

<a id="StorageUserInfoRole_CommonObjectReference"></a>

## StorageUserInfoRole

Role is wire compatible with the old format of storage.Role and hence only includes role name and associated permissions.

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| name |  |  | String |  |  |
| resourceToAccess |  |  | Map of [StorageAccess](#StorageAccess_CommonObjectReference) |  |  |

<a id="StorageV1Metadata_CommonObjectReference"></a>

## StorageV1Metadata

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| digest |  |  | String |  |  |
| created |  |  | Date |  | date-time |
| author |  |  | String |  |  |
| layers |  |  | List of [StorageImageLayer](#StorageImageLayer_CommonObjectReference) |  |  |
| user |  |  | String |  |  |
| command |  |  | List of `string` |  |  |
| entrypoint |  |  | List of `string` |  |  |
| volumes |  |  | List of `string` |  |  |
| labels |  |  | Map of `string` |  |  |

<a id="StorageV2Metadata_CommonObjectReference"></a>

## StorageV2Metadata

| Field Name | Required | Nullable | Type   | Description | Format |
|------------|----------|----------|--------|-------------|--------|
| digest     |          |          | String |             |        |

<a id="StorageViolationState_CommonObjectReference"></a>

## StorageViolationState

| Enum Values |
|-------------|
| ACTIVE      |
| RESOLVED    |
| ATTEMPTED   |

<a id="StorageVolume_CommonObjectReference"></a>

## StorageVolume

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| name |  |  | String |  |  |
| source |  |  | String |  |  |
| destination |  |  | String |  |  |
| readOnly |  |  | Boolean |  |  |
| type |  |  | String |  |  |
| mountPropagation |  |  | [VolumeMountPropagation](#VolumeMountPropagation_CommonObjectReference) |  | NONE, HOST_TO_CONTAINER, BIDIRECTIONAL, |

<a id="StorageVulnerabilityExceptionConfig_CommonObjectReference"></a>

## StorageVulnerabilityExceptionConfig

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| expiryOptions |  |  | [StorageVulnerabilityExceptionConfigExpiryOptions](#StorageVulnerabilityExceptionConfigExpiryOptions_CommonObjectReference) |  |  |

<a id="StorageVulnerabilityExceptionConfigExpiryOptions_CommonObjectReference"></a>

## StorageVulnerabilityExceptionConfigExpiryOptions

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| dayOptions |  |  | List of [StorageDayOption](#StorageDayOption_CommonObjectReference) |  |  |
| fixableCveOptions |  |  | [StorageVulnerabilityExceptionConfigFixableCVEOptions](#StorageVulnerabilityExceptionConfigFixableCVEOptions_CommonObjectReference) |  |  |
| customDate |  |  | Boolean |  |  |
| indefinite |  |  | Boolean |  |  |

<a id="StorageVulnerabilityExceptionConfigFixableCVEOptions_CommonObjectReference"></a>

## StorageVulnerabilityExceptionConfigFixableCVEOptions

| Field Name | Required | Nullable | Type    | Description | Format |
|------------|----------|----------|---------|-------------|--------|
| allFixable |          |          | Boolean |             |        |
| anyFixable |          |          | Boolean |             |        |

<a id="StorageVulnerabilityReportFilters_CommonObjectReference"></a>

## StorageVulnerabilityReportFilters

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| fixability |  |  | [VulnerabilityReportFiltersFixability](#VulnerabilityReportFiltersFixability_CommonObjectReference) |  | BOTH, FIXABLE, NOT_FIXABLE, |
| sinceLastReport |  |  | Boolean |  |  |
| severities |  |  | List of [StorageVulnerabilitySeverity](#StorageVulnerabilitySeverity_CommonObjectReference) |  |  |
| imageTypes |  |  | List of [VulnerabilityReportFiltersImageType](#VulnerabilityReportFiltersImageType_CommonObjectReference) |  |  |
| allVuln |  |  | Boolean |  |  |
| sinceLastSentScheduledReport |  |  | Boolean |  |  |
| sinceStartDate |  |  | Date |  | date-time |
| accessScopeRules |  |  | List of [SimpleAccessScopeRules](#SimpleAccessScopeRules_CommonObjectReference) |  |  |
| includeNvdCvss |  |  | Boolean |  |  |
| includeEpssProbability |  |  | Boolean |  |  |
| includeAdvisory |  |  | Boolean |  |  |
| query |  |  | String |  |  |

<a id="StorageVulnerabilitySeverity_CommonObjectReference"></a>

## StorageVulnerabilitySeverity

| Enum Values                      |
|----------------------------------|
| UNKNOWN_VULNERABILITY_SEVERITY   |
| LOW_VULNERABILITY_SEVERITY       |
| MODERATE_VULNERABILITY_SEVERITY  |
| IMPORTANT_VULNERABILITY_SEVERITY |
| CRITICAL_VULNERABILITY_SEVERITY  |

<a id="StorageVulnerabilityState_CommonObjectReference"></a>

## StorageVulnerabilityState

VulnerabilityState indicates if vulnerability is being observed or deferred(/suppressed). By default, it vulnerabilities are observed.

- OBSERVED: \[Default state\]

| Enum Values    |
|----------------|
| OBSERVED       |
| DEFERRED       |
| FALSE_POSITIVE |

<a id="StorageWatchedImage_CommonObjectReference"></a>

## StorageWatchedImage

| Field Name | Required | Nullable | Type   | Description | Format |
|------------|----------|----------|--------|-------------|--------|
| name       |          |          | String |             |        |

<a id="SyslogLocalFacility_CommonObjectReference"></a>

## SyslogLocalFacility

| Enum Values |
|-------------|
| LOCAL0      |
| LOCAL1      |
| LOCAL2      |
| LOCAL3      |
| LOCAL4      |
| LOCAL5      |
| LOCAL6      |
| LOCAL7      |

<a id="SyslogMessageFormat_CommonObjectReference"></a>

## SyslogMessageFormat

| Enum Values |
|-------------|
| LEGACY      |
| CEF         |

<a id="SyslogTCPConfig_CommonObjectReference"></a>

## SyslogTCPConfig

| Field Name    | Required | Nullable | Type    | Description | Format |
|---------------|----------|----------|---------|-------------|--------|
| hostname      |          |          | String  |             |        |
| port          |          |          | Integer |             | int32  |
| skipTlsVerify |          |          | Boolean |             |        |
| useTls        |          |          | Boolean |             |        |

<a id="TraceBuiltInAuthorizer_CommonObjectReference"></a>

## TraceBuiltInAuthorizer

| Field Name            | Required | Nullable | Type             | Description | Format |
|-----------------------|----------|----------|------------------|-------------|--------|
| clustersTotalNum      |          |          | Integer          |             | int32  |
| namespacesTotalNum    |          |          | Integer          |             | int32  |
| deniedAuthzDecisions  |          |          | Map of `integer` |             | int32  |
| allowedAuthzDecisions |          |          | Map of `integer` |             | int32  |
| effectiveAccessScopes |          |          | Map of `string`  |             |        |

<a id="UpgradeProcessStatusUpgradeProcessType_CommonObjectReference"></a>

## UpgradeProcessStatusUpgradeProcessType

- UPGRADE: UPGRADE represents a sensor version upgrade.

- CERT_ROTATION: CERT_ROTATION represents an upgrade process that only rotates the TLS certs used by the cluster, without changing anything else.

| Enum Values   |
|---------------|
| UPGRADE       |
| CERT_ROTATION |

<a id="UpgradeProgressUpgradeState_CommonObjectReference"></a>

## UpgradeProgressUpgradeState

- UPGRADER_LAUNCHING: In-progress states.

- UPGRADE_COMPLETE: The success state. PLEASE NUMBER ALL IN-PROGRESS STATES ABOVE THIS AND ALL ERROR STATES BELOW THIS.

- UPGRADE_INITIALIZATION_ERROR: Error states.

| Enum Values                   |
|-------------------------------|
| UPGRADE_INITIALIZING          |
| UPGRADER_LAUNCHING            |
| UPGRADER_LAUNCHED             |
| PRE_FLIGHT_CHECKS_COMPLETE    |
| UPGRADE_OPERATIONS_DONE       |
| UPGRADE_COMPLETE              |
| UPGRADE_INITIALIZATION_ERROR  |
| PRE_FLIGHT_CHECKS_FAILED      |
| UPGRADE_ERROR_ROLLING_BACK    |
| UPGRADE_ERROR_ROLLED_BACK     |
| UPGRADE_ERROR_ROLLBACK_FAILED |
| UPGRADE_ERROR_UNKNOWN         |
| UPGRADE_TIMED_OUT             |

<a id="UserInfoResourceToAccess_CommonObjectReference"></a>

## UserInfoResourceToAccess

ResourceToAccess represents a collection of permissions. It is wire compatible with the old format of storage.Role and replaces it in places where only aggregated permissions are required.

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| resourceToAccess |  |  | Map of [StorageAccess](#StorageAccess_CommonObjectReference) |  |  |

<a id="UserRole_CommonObjectReference"></a>

## UserRole

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| name |  |  | String |  |  |
| permissions |  |  | Map of [StorageAccess](#StorageAccess_CommonObjectReference) |  |  |
| accessScopeName |  |  | String |  |  |
| accessScope |  |  | [SimpleAccessScopeRules](#SimpleAccessScopeRules_CommonObjectReference) |  |  |

<a id="V1AddAuthMachineToMachineConfigRequest_CommonObjectReference"></a>

## V1AddAuthMachineToMachineConfigRequest

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| config |  |  | [V1AuthMachineToMachineConfig](#V1AuthMachineToMachineConfig_CommonObjectReference) |  |  |

<a id="V1AddAuthMachineToMachineConfigResponse_CommonObjectReference"></a>

## V1AddAuthMachineToMachineConfigResponse

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| config |  |  | [V1AuthMachineToMachineConfig](#V1AuthMachineToMachineConfig_CommonObjectReference) |  |  |

<a id="V1AdministrationEvent_CommonObjectReference"></a>

## V1AdministrationEvent

AdministrationEvents are administrative events emitted by Central. They are used to create transparency for users for asynchronous, background tasks. Events are part of Central’s system health view.

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| id |  |  | String | UUID of the event. |  |
| type |  |  | [V1AdministrationEventType](#V1AdministrationEventType_CommonObjectReference) |  | ADMINISTRATION_EVENT_TYPE_UNKNOWN, ADMINISTRATION_EVENT_TYPE_GENERIC, ADMINISTRATION_EVENT_TYPE_LOG_MESSAGE, |
| level |  |  | [V1AdministrationEventLevel](#V1AdministrationEventLevel_CommonObjectReference) |  | ADMINISTRATION_EVENT_LEVEL_UNKNOWN, ADMINISTRATION_EVENT_LEVEL_INFO, ADMINISTRATION_EVENT_LEVEL_SUCCESS, ADMINISTRATION_EVENT_LEVEL_WARNING, ADMINISTRATION_EVENT_LEVEL_ERROR, |
| message |  |  | String | Message associated with the event. The message may include detailed information for this particular event. |  |
| hint |  |  | String | Hint associated with the event. The hint may include different information based on the type of event. It can include instructions to resolve an event, or informational hints. |  |
| domain |  |  | String | Domain associated with the event. An event’s domain outlines the feature domain where the event was created from. As an example, this might be "Image Scanning". In case of events that cannot be tied to a specific domain, this will be "General". |  |
| resource |  |  | [AdministrationEventResource](#AdministrationEventResource_CommonObjectReference) |  |  |
| numOccurrences |  |  | String | Occurrences associated with the event. When events may occur multiple times, the occurrences track the amount. | int64 |
| lastOccurredAt |  |  | Date | Specifies the time when the event has last occurred. | date-time |
| createdAt |  |  | Date | Specifies the time when the event has been created. | date-time |

<a id="V1AdministrationEventLevel_CommonObjectReference"></a>

## V1AdministrationEventLevel

AdministrationEventLevel exposes the different levels of events.

| Enum Values                        |
|------------------------------------|
| ADMINISTRATION_EVENT_LEVEL_UNKNOWN |
| ADMINISTRATION_EVENT_LEVEL_INFO    |
| ADMINISTRATION_EVENT_LEVEL_SUCCESS |
| ADMINISTRATION_EVENT_LEVEL_WARNING |
| ADMINISTRATION_EVENT_LEVEL_ERROR   |

<a id="V1AdministrationEventType_CommonObjectReference"></a>

## V1AdministrationEventType

AdministrationEventType exposes the different types of events.

| Enum Values                           |
|---------------------------------------|
| ADMINISTRATION_EVENT_TYPE_UNKNOWN     |
| ADMINISTRATION_EVENT_TYPE_GENERIC     |
| ADMINISTRATION_EVENT_TYPE_LOG_MESSAGE |

<a id="V1AdministrationEventsFilter_CommonObjectReference"></a>

## V1AdministrationEventsFilter

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| from |  |  | Date | Matches events with last_occurred_at after a specific timestamp, i.e. the lower boundary. | date-time |
| until |  |  | Date | Matches events with last_occurred_at before a specific timestamp, i.e. the upper boundary. | date-time |
| domain |  |  | List of `string` | Matches events from a specific domain. |  |
| resourceType |  |  | List of `string` | Matches events associated with a specific resource type. |  |
| type |  |  | List of [V1AdministrationEventType](#V1AdministrationEventType_CommonObjectReference) | Matches events based on their type. |  |
| level |  |  | List of [V1AdministrationEventLevel](#V1AdministrationEventLevel_CommonObjectReference) | Matches events based on their level. |  |

<a id="V1AggregateBy_CommonObjectReference"></a>

## V1AggregateBy

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| aggrFunc |  |  | [V1Aggregation](#V1Aggregation_CommonObjectReference) |  | UNSET, COUNT, MIN, MAX, |
| distinct |  |  | Boolean |  |  |

<a id="V1Aggregation_CommonObjectReference"></a>

## V1Aggregation

| Enum Values |
|-------------|
| UNSET       |
| COUNT       |
| MIN         |
| MAX         |

<a id="V1AlertEvent_CommonObjectReference"></a>

## V1AlertEvent

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| time |  |  | String |  | int64 |
| type |  |  | [V1Type](#V1Type_CommonObjectReference) |  | CREATED, REMOVED, |
| id |  |  | String |  |  |

<a id="V1AuthMachineToMachineConfig_CommonObjectReference"></a>

## V1AuthMachineToMachineConfig

AuthMachineToMachineConfig determines rules for exchanging an identity token from a third party with a Central access token. The M2M stands for machine to machine, as this is the intended use-case for the config.

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| id |  |  | String | UUID of the config. Note that when adding a machine to machine config, this field should not be set. |  |
| type |  |  | [V1AuthMachineToMachineConfigType](#V1AuthMachineToMachineConfigType_CommonObjectReference) |  | GENERIC, GITHUB_ACTIONS, KUBE_SERVICE_ACCOUNT, |
| tokenExpirationDuration |  |  | String | Sets the expiration of the token returned from the ExchangeAuthMachineToMachineToken API call. Possible valid time units are: s, m, h. The maximum allowed expiration duration is 24h. As an example: 2h45m. For additional information on the validation of the duration, see: <https://pkg.go.dev/time#ParseDuration>. |  |
| mappings |  |  | List of [AuthMachineToMachineConfigMapping](#AuthMachineToMachineConfigMapping_CommonObjectReference) | At least one mapping is required to resolve to a valid role for the access token to be successfully generated. |  |
| issuer |  |  | String | The issuer of the related OIDC provider issuing the ID tokens to exchange. Must be non-empty string containing URL when type is GENERIC. In case of GitHub actions, this must be empty or set to <https://token.actions.githubusercontent.com>. Issuer is a unique key, therefore there may be at most one GITHUB_ACTIONS config, and each GENERIC config must have a distinct issuer. |  |
| traits |  |  | [V1Traits](#V1Traits_CommonObjectReference) |  |  |

<a id="V1AuthMachineToMachineConfigType_CommonObjectReference"></a>

## V1AuthMachineToMachineConfigType

The type of the auth machine to machine config. Currently supports GitHub actions or any other generic OIDC provider to use for verifying and exchanging the token.

| Enum Values          |
|----------------------|
| GENERIC              |
| GITHUB_ACTIONS       |
| KUBE_SERVICE_ACCOUNT |

<a id="V1AuthStatus_CommonObjectReference"></a>

## V1AuthStatus

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| userId |  |  | String |  |  |
| serviceId |  |  | [StorageServiceIdentity](#StorageServiceIdentity_CommonObjectReference) |  |  |
| expires |  |  | Date |  | date-time |
| refreshUrl |  |  | String |  |  |
| authProvider |  |  | [StorageAuthProvider](#StorageAuthProvider_CommonObjectReference) |  |  |
| userInfo |  |  | [StorageUserInfo](#StorageUserInfo_CommonObjectReference) |  |  |
| userAttributes |  |  | List of [V1UserAttribute](#V1UserAttribute_CommonObjectReference) |  |  |
| idpToken |  |  | String | Token returned to ACS by the underlying identity provider. This field is set only in a few, specific contexts. Do not rely on this field being present in the response. |  |

<a id="V1Authorities_CommonObjectReference"></a>

## V1Authorities

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| authorities |  |  | List of [V1Authority](#V1Authority_CommonObjectReference) |  |  |

<a id="V1Authority_CommonObjectReference"></a>

## V1Authority

| Field Name     | Required | Nullable | Type     | Description | Format |
|----------------|----------|----------|----------|-------------|--------|
| certificatePem |          |          | byte\[\] |             | byte   |

<a id="V1AuthorizationTraceResponse_CommonObjectReference"></a>

## V1AuthorizationTraceResponse

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| arrivedAt |  |  | Date |  | date-time |
| processedAt |  |  | Date |  | date-time |
| request |  |  | [V1AuthorizationTraceResponseRequest](#V1AuthorizationTraceResponseRequest_CommonObjectReference) |  |  |
| response |  |  | [V1AuthorizationTraceResponseResponse](#V1AuthorizationTraceResponseResponse_CommonObjectReference) |  |  |
| user |  |  | [AuthorizationTraceResponseUser](#AuthorizationTraceResponseUser_CommonObjectReference) |  |  |
| trace |  |  | [AuthorizationTraceResponseTrace](#AuthorizationTraceResponseTrace_CommonObjectReference) |  |  |

<a id="V1AuthorizationTraceResponseRequest_CommonObjectReference"></a>

## V1AuthorizationTraceResponseRequest

| Field Name | Required | Nullable | Type   | Description | Format |
|------------|----------|----------|--------|-------------|--------|
| endpoint   |          |          | String |             |        |
| method     |          |          | String |             |        |

<a id="V1AuthorizationTraceResponseResponse_CommonObjectReference"></a>

## V1AuthorizationTraceResponseResponse

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| status |  |  | [AuthorizationTraceResponseResponseStatus](#AuthorizationTraceResponseResponseStatus_CommonObjectReference) |  | UNKNOWN_STATUS, SUCCESS, FAILURE, |
| error |  |  | String |  |  |

<a id="V1AutocompleteResponse_CommonObjectReference"></a>

## V1AutocompleteResponse

| Field Name | Required | Nullable | Type             | Description | Format |
|------------|----------|----------|------------------|-------------|--------|
| values     |          |          | List of `string` |             |        |

<a id="V1AvailableProviderTypesResponse_CommonObjectReference"></a>

## V1AvailableProviderTypesResponse

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| authProviderTypes |  |  | List of [AvailableProviderTypesResponseAuthProviderType](#AvailableProviderTypesResponseAuthProviderType_CommonObjectReference) |  |  |

<a id="V1BuildDetectionRequest_CommonObjectReference"></a>

## V1BuildDetectionRequest

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| image |  |  | [StorageContainerImage](#StorageContainerImage_CommonObjectReference) |  |  |
| imageName |  |  | String |  |  |
| noExternalMetadata |  |  | Boolean |  |  |
| sendNotifications |  |  | Boolean |  |  |
| force |  |  | Boolean |  |  |
| policyCategories |  |  | List of `string` |  |  |
| cluster |  |  | String | Cluster to delegate scan to, may be the cluster’s name or ID. |  |
| namespace |  |  | String | Namespace on the secured cluster from which to read context information when delegating image scans, specifically pull secrets to access the image registry. |  |

<a id="V1BuildDetectionResponse_CommonObjectReference"></a>

## V1BuildDetectionResponse

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| alerts |  |  | List of [StorageAlert](#StorageAlert_CommonObjectReference) |  |  |

<a id="V1BulkProcessBaselinesRequest_CommonObjectReference"></a>

## V1BulkProcessBaselinesRequest

| Field Name | Required | Nullable | Type             | Description | Format |
|------------|----------|----------|------------------|-------------|--------|
| clusterId  |          |          | String           |             |        |
| namespaces |          |          | List of `string` |             |        |

<a id="V1BulkUpdateProcessBaselinesResponse_CommonObjectReference"></a>

## V1BulkUpdateProcessBaselinesResponse

| Field Name | Required | Nullable | Type    | Description | Format |
|------------|----------|----------|---------|-------------|--------|
| success    |          |          | Boolean |             |        |

<a id="V1CRSGenRequest_CommonObjectReference"></a>

## V1CRSGenRequest

| Field Name | Required | Nullable | Type   | Description | Format |
|------------|----------|----------|--------|-------------|--------|
| name       |          |          | String |             |        |

<a id="V1CRSGenRequestExtended_CommonObjectReference"></a>

## V1CRSGenRequestExtended

| Field Name       | Required | Nullable | Type   | Description | Format    |
|------------------|----------|----------|--------|-------------|-----------|
| name             |          |          | String |             |           |
| validUntil       |          |          | Date   |             | date-time |
| validFor         |          |          | String |             |           |
| maxRegistrations |          |          | String |             | uint64    |

<a id="V1CRSGenResponse_CommonObjectReference"></a>

## V1CRSGenResponse

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| meta |  |  | [V1CRSMeta](#V1CRSMeta_CommonObjectReference) |  |  |
| crs |  |  | byte\[\] |  | byte |

<a id="V1CRSMeta_CommonObjectReference"></a>

## V1CRSMeta

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| id |  |  | String |  |  |
| name |  |  | String |  |  |
| createdAt |  |  | Date |  | date-time |
| createdBy |  |  | [StorageUser](#StorageUser_CommonObjectReference) |  |  |
| expiresAt |  |  | Date |  | date-time |
| maxRegistrations |  |  | String |  | uint64 |
| registrationsInitiated |  |  | List of `string` |  |  |
| registrationsCompleted |  |  | List of `string` |  |  |

<a id="V1CRSMetasResponse_CommonObjectReference"></a>

## V1CRSMetasResponse

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| items |  |  | List of [V1CRSMeta](#V1CRSMeta_CommonObjectReference) |  |  |

<a id="V1CRSRevokeRequest_CommonObjectReference"></a>

## V1CRSRevokeRequest

| Field Name | Required | Nullable | Type             | Description | Format |
|------------|----------|----------|------------------|-------------|--------|
| ids        |          |          | List of `string` |             |        |

<a id="V1CRSRevokeResponse_CommonObjectReference"></a>

## V1CRSRevokeResponse

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| crsRevocationErrors |  |  | List of [CRSRevokeResponseCRSRevocationError](#CRSRevokeResponseCRSRevocationError_CommonObjectReference) |  |  |
| revokedIds |  |  | List of `string` |  |  |

<a id="V1CentralServicesCapabilities_CommonObjectReference"></a>

## V1CentralServicesCapabilities

Provides availability of certain functionality of Central Services in the current configuration. The initial intended use is to disable certain functionality that does not make sense in the Cloud Service context.

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| centralScanningCanUseContainerIamRoleForEcr |  |  | [CentralServicesCapabilitiesCapabilityStatus](#CentralServicesCapabilitiesCapabilityStatus_CommonObjectReference) |  | CapabilityAvailable, CapabilityDisabled, |
| centralCanUseCloudBackupIntegrations |  |  | [CentralServicesCapabilitiesCapabilityStatus](#CentralServicesCapabilitiesCapabilityStatus_CommonObjectReference) |  | CapabilityAvailable, CapabilityDisabled, |
| centralCanDisplayDeclarativeConfigHealth |  |  | [CentralServicesCapabilitiesCapabilityStatus](#CentralServicesCapabilitiesCapabilityStatus_CommonObjectReference) |  | CapabilityAvailable, CapabilityDisabled, |
| centralCanUpdateCert |  |  | [CentralServicesCapabilitiesCapabilityStatus](#CentralServicesCapabilitiesCapabilityStatus_CommonObjectReference) |  | CapabilityAvailable, CapabilityDisabled, |
| centralCanUseAcscsEmailIntegration |  |  | [CentralServicesCapabilitiesCapabilityStatus](#CentralServicesCapabilitiesCapabilityStatus_CommonObjectReference) |  | CapabilityAvailable, CapabilityDisabled, |

<a id="V1CentralUpgradeStatus_CommonObjectReference"></a>

## V1CentralUpgradeStatus

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| version |  |  | String |  |  |
| forceRollbackTo |  |  | String | The version of previous clone in Central. This is the version we can force rollback to. |  |
| canRollbackAfterUpgrade |  |  | Boolean | If true, we can rollback to the current version if an upgrade failed. |  |
| spaceRequiredForRollbackAfterUpgrade |  |  | String |  | int64 |
| spaceAvailableForRollbackAfterUpgrade |  |  | String |  | int64 |

<a id="V1CloudSource_CommonObjectReference"></a>

## V1CloudSource

CloudSource is an integration which provides a source for discovered clusters.

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| id |  |  | String |  |  |
| name |  |  | String |  |  |
| type |  |  | [V1CloudSourceType](#V1CloudSourceType_CommonObjectReference) |  | TYPE_UNSPECIFIED, TYPE_PALADIN_CLOUD, TYPE_OCM, |
| credentials |  |  | [CloudSourceCredentials](#CloudSourceCredentials_CommonObjectReference) |  |  |
| skipTestIntegration |  |  | Boolean |  |  |
| paladinCloud |  |  | [V1PaladinCloudConfig](#V1PaladinCloudConfig_CommonObjectReference) |  |  |
| ocm |  |  | [V1OCMConfig](#V1OCMConfig_CommonObjectReference) |  |  |

<a id="V1CloudSourceType_CommonObjectReference"></a>

## V1CloudSourceType

| Enum Values        |
|--------------------|
| TYPE_UNSPECIFIED   |
| TYPE_PALADIN_CLOUD |
| TYPE_OCM           |

<a id="V1CloudSourcesFilter_CommonObjectReference"></a>

## V1CloudSourcesFilter

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| names |  |  | List of `string` | Matches cloud sources based on their name. |  |
| types |  |  | List of [V1CloudSourceType](#V1CloudSourceType_CommonObjectReference) | Matches cloud sources based on their type. |  |

<a id="V1ClusterDefaultsResponse_CommonObjectReference"></a>

## V1ClusterDefaultsResponse

| Field Name               | Required | Nullable | Type    | Description | Format |
|--------------------------|----------|----------|---------|-------------|--------|
| mainImageRepository      |          |          | String  |             |        |
| collectorImageRepository |          |          | String  |             |        |
| kernelSupportAvailable   |          |          | Boolean |             |        |

<a id="V1ClusterResponse_CommonObjectReference"></a>

## V1ClusterResponse

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| cluster |  |  | [StorageCluster](#StorageCluster_CommonObjectReference) |  |  |
| clusterRetentionInfo |  |  | [V1DecommissionedClusterRetentionInfo](#V1DecommissionedClusterRetentionInfo_CommonObjectReference) |  |  |

<a id="V1ClustersList_CommonObjectReference"></a>

## V1ClustersList

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| clusters |  |  | List of [StorageCluster](#StorageCluster_CommonObjectReference) |  |  |
| clusterIdToRetentionInfo |  |  | Map of [V1DecommissionedClusterRetentionInfo](#V1DecommissionedClusterRetentionInfo_CommonObjectReference) |  |  |

<a id="V1CollectionDeploymentMatchOptions_CommonObjectReference"></a>

## V1CollectionDeploymentMatchOptions

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| withMatches |  |  | Boolean |  |  |
| filterQuery |  |  | [V1RawQuery](#V1RawQuery_CommonObjectReference) |  |  |

<a id="V1ComplianceControl_CommonObjectReference"></a>

## V1ComplianceControl

| Field Name         | Required | Nullable | Type    | Description | Format |
|--------------------|----------|----------|---------|-------------|--------|
| id                 |          |          | String  |             |        |
| standardId         |          |          | String  |             |        |
| groupId            |          |          | String  |             |        |
| name               |          |          | String  |             |        |
| description        |          |          | String  |             |        |
| implemented        |          |          | Boolean |             |        |
| interpretationText |          |          | String  |             |        |

<a id="V1ComplianceControlGroup_CommonObjectReference"></a>

## V1ComplianceControlGroup

| Field Name           | Required | Nullable | Type    | Description | Format |
|----------------------|----------|----------|---------|-------------|--------|
| id                   |          |          | String  |             |        |
| standardId           |          |          | String  |             |        |
| name                 |          |          | String  |             |        |
| description          |          |          | String  |             |        |
| numImplementedChecks |          |          | Integer |             | int32  |

<a id="V1ComplianceRun_CommonObjectReference"></a>

## V1ComplianceRun

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| id |  |  | String |  |  |
| clusterId |  |  | String |  |  |
| standardId |  |  | String |  |  |
| startTime |  |  | Date |  | date-time |
| finishTime |  |  | Date |  | date-time |
| state |  |  | [V1ComplianceRunState](#V1ComplianceRunState_CommonObjectReference) |  | INVALID, READY, STARTED, WAIT_FOR_DATA, EVALUTING_CHECKS, FINISHED, |
| errorMessage |  |  | String |  |  |

<a id="V1ComplianceRunSelection_CommonObjectReference"></a>

## V1ComplianceRunSelection

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| clusterId |  |  | String | The ID of the cluster. "\*" means "all clusters". |  |
| standardId |  |  | String | The ID of the compliance standard. "\*" means "all standards". |  |

<a id="V1ComplianceRunState_CommonObjectReference"></a>

## V1ComplianceRunState

| Enum Values      |
|------------------|
| INVALID          |
| READY            |
| STARTED          |
| WAIT_FOR_DATA    |
| EVALUTING_CHECKS |
| FINISHED         |

<a id="V1ComplianceStandard_CommonObjectReference"></a>

## V1ComplianceStandard

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| metadata |  |  | [V1ComplianceStandardMetadata](#V1ComplianceStandardMetadata_CommonObjectReference) |  |  |
| groups |  |  | List of [V1ComplianceControlGroup](#V1ComplianceControlGroup_CommonObjectReference) |  |  |
| controls |  |  | List of [V1ComplianceControl](#V1ComplianceControl_CommonObjectReference) |  |  |

<a id="V1ComplianceStandardMetadata_CommonObjectReference"></a>

## V1ComplianceStandardMetadata

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| id |  |  | String |  |  |
| name |  |  | String |  |  |
| description |  |  | String |  |  |
| numImplementedChecks |  |  | Integer |  | int32 |
| scopes |  |  | List of [V1ComplianceStandardMetadataScope](#V1ComplianceStandardMetadataScope_CommonObjectReference) |  |  |
| dynamic |  |  | Boolean |  |  |
| hideScanResults |  |  | Boolean |  |  |

<a id="V1ComplianceStandardMetadataScope_CommonObjectReference"></a>

## V1ComplianceStandardMetadataScope

| Enum Values |
|-------------|
| UNSET       |
| CLUSTER     |
| NAMESPACE   |
| DEPLOYMENT  |
| NODE        |

<a id="V1ConfigureTelemetryRequest_CommonObjectReference"></a>

## V1ConfigureTelemetryRequest

| Field Name | Required | Nullable | Type    | Description | Format |
|------------|----------|----------|---------|-------------|--------|
| enabled    |          |          | Boolean |             |        |

<a id="V1CountAdministrationEventsResponse_CommonObjectReference"></a>

## V1CountAdministrationEventsResponse

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| count |  |  | Integer | The total number of events after filtering and deduplication. | int32 |

<a id="V1CountAlertsResponse_CommonObjectReference"></a>

## V1CountAlertsResponse

| Field Name | Required | Nullable | Type    | Description | Format |
|------------|----------|----------|---------|-------------|--------|
| count      |          |          | Integer |             | int32  |

<a id="V1CountCloudSourcesResponse_CommonObjectReference"></a>

## V1CountCloudSourcesResponse

| Field Name | Required | Nullable | Type    | Description | Format |
|------------|----------|----------|---------|-------------|--------|
| count      |          |          | Integer |             | int32  |

<a id="V1CountDeploymentsResponse_CommonObjectReference"></a>

## V1CountDeploymentsResponse

| Field Name | Required | Nullable | Type    | Description | Format |
|------------|----------|----------|---------|-------------|--------|
| count      |          |          | Integer |             | int32  |

<a id="V1CountDiscoveredClustersResponse_CommonObjectReference"></a>

## V1CountDiscoveredClustersResponse

| Field Name | Required | Nullable | Type    | Description | Format |
|------------|----------|----------|---------|-------------|--------|
| count      |          |          | Integer |             | int32  |

<a id="V1CountImagesResponse_CommonObjectReference"></a>

## V1CountImagesResponse

| Field Name | Required | Nullable | Type    | Description | Format |
|------------|----------|----------|---------|-------------|--------|
| count      |          |          | Integer |             | int32  |

<a id="V1CountProcessesResponse_CommonObjectReference"></a>

## V1CountProcessesResponse

| Field Name | Required | Nullable | Type    | Description | Format |
|------------|----------|----------|---------|-------------|--------|
| count      |          |          | Integer |             | int32  |

<a id="V1CountReportConfigurationsResponse_CommonObjectReference"></a>

## V1CountReportConfigurationsResponse

| Field Name | Required | Nullable | Type    | Description | Format |
|------------|----------|----------|---------|-------------|--------|
| count      |          |          | Integer |             | int32  |

<a id="V1CountSecretsResponse_CommonObjectReference"></a>

## V1CountSecretsResponse

| Field Name | Required | Nullable | Type    | Description | Format |
|------------|----------|----------|---------|-------------|--------|
| count      |          |          | Integer |             | int32  |

<a id="V1CreateCloudSourceRequest_CommonObjectReference"></a>

## V1CreateCloudSourceRequest

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| cloudSource |  |  | [V1CloudSource](#V1CloudSource_CommonObjectReference) |  |  |

<a id="V1CreateCloudSourceResponse_CommonObjectReference"></a>

## V1CreateCloudSourceResponse

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| cloudSource |  |  | [V1CloudSource](#V1CloudSource_CommonObjectReference) |  |  |

<a id="V1CreateCollectionRequest_CommonObjectReference"></a>

## V1CreateCollectionRequest

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| name |  |  | String |  |  |
| description |  |  | String |  |  |
| resourceSelectors |  |  | List of [StorageResourceSelector](#StorageResourceSelector_CommonObjectReference) |  |  |
| embeddedCollectionIds |  |  | List of `string` |  |  |

<a id="V1CreateCollectionResponse_CommonObjectReference"></a>

## V1CreateCollectionResponse

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| collection |  |  | [StorageResourceCollection](#StorageResourceCollection_CommonObjectReference) |  |  |

<a id="V1CreateServiceIdentityRequest_CommonObjectReference"></a>

## V1CreateServiceIdentityRequest

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| id |  |  | String |  |  |
| type |  |  | [StorageServiceType](#StorageServiceType_CommonObjectReference) |  | UNKNOWN_SERVICE, SENSOR_SERVICE, CENTRAL_SERVICE, CENTRAL_DB_SERVICE, REMOTE_SERVICE, COLLECTOR_SERVICE, MONITORING_UI_SERVICE, MONITORING_DB_SERVICE, MONITORING_CLIENT_SERVICE, BENCHMARK_SERVICE, SCANNER_SERVICE, SCANNER_DB_SERVICE, ADMISSION_CONTROL_SERVICE, SCANNER_V4_INDEXER_SERVICE, SCANNER_V4_MATCHER_SERVICE, SCANNER_V4_DB_SERVICE, SCANNER_V4_SERVICE, REGISTRANT_SERVICE, |

<a id="V1CreateServiceIdentityResponse_CommonObjectReference"></a>

## V1CreateServiceIdentityResponse

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| identity |  |  | [StorageServiceIdentity](#StorageServiceIdentity_CommonObjectReference) |  |  |
| certificatePem |  |  | byte\[\] |  | byte |
| privateKeyPem |  |  | byte\[\] |  | byte |

<a id="V1DBExportFormat_CommonObjectReference"></a>

## V1DBExportFormat

DBExportFormat describes a format (= a collection of files) for the database export.

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| formatName |  |  | String |  |  |
| files |  |  | List of [V1DBExportFormatFile](#V1DBExportFormatFile_CommonObjectReference) |  |  |

<a id="V1DBExportFormatFile_CommonObjectReference"></a>

## V1DBExportFormatFile

| Field Name | Required | Nullable | Type    | Description | Format |
|------------|----------|----------|---------|-------------|--------|
| name       |          |          | String  |             |        |
| optional   |          |          | Boolean |             |        |

<a id="V1DBExportManifest_CommonObjectReference"></a>

## V1DBExportManifest

A DB export manifest describes the file contents of a restore request. To prevent data loss, a manifest is always interpreted as binding, i.e., the server must ensure that it will read and make use of every file listed in the manifest, otherwise it must reject the request.

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| files |  |  | List of [V1DBExportManifestFile](#V1DBExportManifestFile_CommonObjectReference) |  |  |

<a id="V1DBExportManifestFile_CommonObjectReference"></a>

## V1DBExportManifestFile

A single file in the restore body.

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| name |  |  | String | The name of the file. This may or may not be a (relative) file path and up to the server to interpret. For databases exported as ZIP files, this is the path relative to the root of the archive. |  |
| encoding |  |  | [DBExportManifestEncodingType](#DBExportManifestEncodingType_CommonObjectReference) |  | UNKNOWN, UNCOMPREESSED, DEFLATED, |
| encodedSize |  |  | String |  | int64 |
| decodedSize |  |  | String |  | int64 |
| decodedCrc32 |  |  | Long | The CRC32 (IEEE) checksum of the decoded(!) data. | int64 |

<a id="V1DBRestoreProcessMetadata_CommonObjectReference"></a>

## V1DBRestoreProcessMetadata

The metadata of an ongoing or completed restore process. This is the **static** metadata, which will not change (i.e., it is not a status).

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| id |  |  | String | An ID identifying the restore process. Auto-assigned. |  |
| header |  |  | [V1DBRestoreRequestHeader](#V1DBRestoreRequestHeader_CommonObjectReference) |  |  |
| startTime |  |  | Date | The time at which the restore process was started. | date-time |
| initiatingUserName |  |  | String | The user who initiated the database restore process. |  |

<a id="V1DBRestoreProcessStatus_CommonObjectReference"></a>

## V1DBRestoreProcessStatus

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| metadata |  |  | [V1DBRestoreProcessMetadata](#V1DBRestoreProcessMetadata_CommonObjectReference) |  |  |
| attemptId |  |  | String |  |  |
| state |  |  | [V1DBRestoreProcessStatusState](#V1DBRestoreProcessStatusState_CommonObjectReference) |  | UNKNOWN, NOT_STARTED, IN_PROGRESS, PAUSED, COMPLETED, |
| resumeInfo |  |  | [DBRestoreProcessStatusResumeInfo](#DBRestoreProcessStatusResumeInfo_CommonObjectReference) |  |  |
| error |  |  | String |  |  |
| bytesRead |  |  | String |  | int64 |
| filesProcessed |  |  | String |  | int64 |

<a id="V1DBRestoreProcessStatusState_CommonObjectReference"></a>

## V1DBRestoreProcessStatusState

- COMPLETED: successful if error is empty, unsuccessful otherwise

| Enum Values |
|-------------|
| UNKNOWN     |
| NOT_STARTED |
| IN_PROGRESS |
| PAUSED      |
| COMPLETED   |

<a id="V1DBRestoreRequestHeader_CommonObjectReference"></a>

## V1DBRestoreRequestHeader

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| formatName |  |  | String | The name of the database export format. Mandatory. |  |
| manifest |  |  | [V1DBExportManifest](#V1DBExportManifest_CommonObjectReference) |  |  |
| localFile |  |  | [DBRestoreRequestHeaderLocalFileInfo](#DBRestoreRequestHeaderLocalFileInfo_CommonObjectReference) |  |  |

<a id="V1DatabaseBackupStatus_CommonObjectReference"></a>

## V1DatabaseBackupStatus

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| backupInfo |  |  | [StorageBackupInfo](#StorageBackupInfo_CommonObjectReference) |  |  |

<a id="V1DatabaseStatus_CommonObjectReference"></a>

## V1DatabaseStatus

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| databaseAvailable |  |  | Boolean |  |  |
| databaseType |  |  | [DatabaseStatusDatabaseType](#DatabaseStatusDatabaseType_CommonObjectReference) |  | Hidden, RocksDB, PostgresDB, |
| databaseVersion |  |  | String |  |  |
| databaseIsExternal |  |  | Boolean |  |  |

<a id="V1DayOption_CommonObjectReference"></a>

## V1DayOption

| Field Name | Required | Nullable | Type    | Description | Format |
|------------|----------|----------|---------|-------------|--------|
| numDays    |          |          | Long    |             | int64  |
| enabled    |          |          | Boolean |             |        |

<a id="V1DecommissionedClusterRetentionInfo_CommonObjectReference"></a>

## V1DecommissionedClusterRetentionInfo

next available tag: 3

| Field Name        | Required | Nullable | Type    | Description | Format |
|-------------------|----------|----------|---------|-------------|--------|
| isExcluded        |          |          | Boolean |             |        |
| daysUntilDeletion |          |          | Integer |             | int32  |

<a id="V1DelegatedRegistryCluster_CommonObjectReference"></a>

## V1DelegatedRegistryCluster

| Field Name | Required | Nullable | Type    | Description | Format |
|------------|----------|----------|---------|-------------|--------|
| id         |          |          | String  |             |        |
| name       |          |          | String  |             |        |
| isValid    |          |          | Boolean |             |        |

<a id="V1DelegatedRegistryClustersResponse_CommonObjectReference"></a>

## V1DelegatedRegistryClustersResponse

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| clusters |  |  | List of [V1DelegatedRegistryCluster](#V1DelegatedRegistryCluster_CommonObjectReference) |  |  |

<a id="V1DelegatedRegistryConfig_CommonObjectReference"></a>

## V1DelegatedRegistryConfig

DelegatedRegistryConfig determines if and where scan requests are delegated to, such as kept in central services or sent to particular secured clusters.

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| enabledFor |  |  | [DelegatedRegistryConfigEnabledFor](#DelegatedRegistryConfigEnabledFor_CommonObjectReference) |  | NONE, ALL, SPECIFIC, |
| defaultClusterId |  |  | String |  |  |
| registries |  |  | List of [DelegatedRegistryConfigDelegatedRegistry](#DelegatedRegistryConfigDelegatedRegistry_CommonObjectReference) | If `enabled for` is NONE registries has no effect. If `ALL` registries directs ad-hoc requests to the specified secured clusters if the path matches. If `SPECIFIC` registries directs ad-hoc requests to the specified secured clusters just like with `ALL`, but in addition images that match the specified paths will be scanned locally by the secured clusters (images from the OCP integrated registry are always scanned locally). Images that do not match a path will be scanned via central services |  |

<a id="V1DeleteAlertsResponse_CommonObjectReference"></a>

## V1DeleteAlertsResponse

| Field Name | Required | Nullable | Type    | Description | Format |
|------------|----------|----------|---------|-------------|--------|
| numDeleted |          |          | Long    |             | int64  |
| dryRun     |          |          | Boolean |             |        |

<a id="V1DeleteImagesResponse_CommonObjectReference"></a>

## V1DeleteImagesResponse

| Field Name | Required | Nullable | Type    | Description | Format |
|------------|----------|----------|---------|-------------|--------|
| numDeleted |          |          | Long    |             | int64  |
| dryRun     |          |          | Boolean |             |        |

<a id="V1DeleteProcessBaselinesResponse_CommonObjectReference"></a>

## V1DeleteProcessBaselinesResponse

| Field Name | Required | Nullable | Type    | Description | Format |
|------------|----------|----------|---------|-------------|--------|
| numDeleted |          |          | Integer |             | int32  |
| dryRun     |          |          | Boolean |             |        |

<a id="V1DeployDetectionRemark_CommonObjectReference"></a>

## V1DeployDetectionRemark

| Field Name             | Required | Nullable | Type             | Description | Format |
|------------------------|----------|----------|------------------|-------------|--------|
| name                   |          |          | String           |             |        |
| permissionLevel        |          |          | String           |             |        |
| appliedNetworkPolicies |          |          | List of `string` |             |        |

<a id="V1DeployDetectionRequest_CommonObjectReference"></a>

## V1DeployDetectionRequest

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| deployment |  |  | [StorageDeployment](#StorageDeployment_CommonObjectReference) |  |  |
| noExternalMetadata |  |  | Boolean |  |  |
| enforcementOnly |  |  | Boolean |  |  |
| clusterId |  |  | String |  |  |

<a id="V1DeployDetectionResponse_CommonObjectReference"></a>

## V1DeployDetectionResponse

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| runs |  |  | List of [DeployDetectionResponseRun](#DeployDetectionResponseRun_CommonObjectReference) |  |  |
| ignoredObjectRefs |  |  | List of `string` | The reference will be in the format: namespace/name\[\<group\>/\<version\>, Kind=\<kind\>\]. |  |
| remarks |  |  | List of [V1DeployDetectionRemark](#V1DeployDetectionRemark_CommonObjectReference) |  |  |

<a id="V1DeployYAMLDetectionRequest_CommonObjectReference"></a>

## V1DeployYAMLDetectionRequest

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| yaml |  |  | String |  |  |
| noExternalMetadata |  |  | Boolean |  |  |
| enforcementOnly |  |  | Boolean |  |  |
| force |  |  | Boolean |  |  |
| policyCategories |  |  | List of `string` |  |  |
| cluster |  |  | String | Cluster to delegate scan to, may be the cluster’s name or ID. |  |
| namespace |  |  | String |  |  |

<a id="V1DeploymentLabelsResponse_CommonObjectReference"></a>

## V1DeploymentLabelsResponse

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| labels |  |  | Map of [DeploymentLabelsResponseLabelValues](#DeploymentLabelsResponseLabelValues_CommonObjectReference) |  |  |
| values |  |  | List of `string` |  |  |

<a id="V1DiscoveredCluster_CommonObjectReference"></a>

## V1DiscoveredCluster

DiscoveredCluster represents a cluster discovered from a cloud source.

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| id |  |  | String | UUIDv5 generated deterministically from the tuple (metadata.id, metadata.type, source.id). |  |
| metadata |  |  | [V1DiscoveredClusterMetadata](#V1DiscoveredClusterMetadata_CommonObjectReference) |  |  |
| status |  |  | [V1DiscoveredClusterStatus](#V1DiscoveredClusterStatus_CommonObjectReference) |  | STATUS_UNSPECIFIED, STATUS_SECURED, STATUS_UNSECURED, |
| source |  |  | [V1DiscoveredClusterCloudSource](#V1DiscoveredClusterCloudSource_CommonObjectReference) |  |  |

<a id="V1DiscoveredClusterCloudSource_CommonObjectReference"></a>

## V1DiscoveredClusterCloudSource

| Field Name | Required | Nullable | Type   | Description | Format |
|------------|----------|----------|--------|-------------|--------|
| id         |          |          | String |             |        |

<a id="V1DiscoveredClusterMetadata_CommonObjectReference"></a>

## V1DiscoveredClusterMetadata

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| id |  |  | String | Represents a unique ID under which the cluster is registered with the cloud provider. Matches storage.ClusterMetadata.id for secured clusters. |  |
| name |  |  | String | Represents the name under which the cluster is registered with the cloud provider. Matches storage.ClusterMetadata.name for secured clusters. |  |
| type |  |  | [DiscoveredClusterMetadataType](#DiscoveredClusterMetadataType_CommonObjectReference) |  | UNSPECIFIED, AKS, ARO, EKS, GKE, OCP, OSD, ROSA, |
| providerType |  |  | [MetadataProviderType](#MetadataProviderType_CommonObjectReference) |  | PROVIDER_TYPE_UNSPECIFIED, PROVIDER_TYPE_AWS, PROVIDER_TYPE_GCP, PROVIDER_TYPE_AZURE, |
| region |  |  | String | The region as reported by the cloud provider. |  |
| firstDiscoveredAt |  |  | Date | Timestamp at which the cluster was first discovered by the cloud source. | date-time |

<a id="V1DiscoveredClusterStatus_CommonObjectReference"></a>

## V1DiscoveredClusterStatus

- STATUS_UNSPECIFIED: The status of the cluster is unknown. May occur if a secured cluster is missing the metadata for a possible match.

- STATUS_SECURED: The discovered cluster was matched with a secured cluster.

- STATUS_UNSECURED: The discovered cluster was not matched with a secured cluster.

| Enum Values        |
|--------------------|
| STATUS_UNSPECIFIED |
| STATUS_SECURED     |
| STATUS_UNSECURED   |

<a id="V1DiscoveredClustersFilter_CommonObjectReference"></a>

## V1DiscoveredClustersFilter

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| names |  |  | List of `string` | Matches discovered clusters of specific names. |  |
| types |  |  | List of [DiscoveredClusterMetadataType](#DiscoveredClusterMetadataType_CommonObjectReference) | Matches discovered clusters of specific types. |  |
| statuses |  |  | List of [V1DiscoveredClusterStatus](#V1DiscoveredClusterStatus_CommonObjectReference) | Matches discovered clusters of specific statuses. |  |
| sourceIds |  |  | List of `string` | Matches discovered clusters of specific cloud source IDs. |  |

<a id="V1DryRunCollectionRequest_CommonObjectReference"></a>

## V1DryRunCollectionRequest

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| name |  |  | String |  |  |
| id |  |  | String |  |  |
| description |  |  | String |  |  |
| resourceSelectors |  |  | List of [StorageResourceSelector](#StorageResourceSelector_CommonObjectReference) |  |  |
| embeddedCollectionIds |  |  | List of `string` |  |  |
| options |  |  | [V1CollectionDeploymentMatchOptions](#V1CollectionDeploymentMatchOptions_CommonObjectReference) |  |  |

<a id="V1DryRunCollectionResponse_CommonObjectReference"></a>

## V1DryRunCollectionResponse

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| deployments |  |  | List of [StorageListDeployment](#StorageListDeployment_CommonObjectReference) |  |  |

<a id="V1DryRunJobStatusResponse_CommonObjectReference"></a>

## V1DryRunJobStatusResponse

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| pending |  |  | Boolean |  |  |
| result |  |  | [V1DryRunResponse](#V1DryRunResponse_CommonObjectReference) |  |  |

<a id="V1DryRunResponse_CommonObjectReference"></a>

## V1DryRunResponse

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| alerts |  |  | List of [DryRunResponseAlert](#DryRunResponseAlert_CommonObjectReference) |  |  |

<a id="V1ExchangeAuthMachineToMachineTokenRequest_CommonObjectReference"></a>

## V1ExchangeAuthMachineToMachineTokenRequest

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| idToken |  |  | String | Identity token that is supposed to be exchanged. |  |

<a id="V1ExchangeAuthMachineToMachineTokenResponse_CommonObjectReference"></a>

## V1ExchangeAuthMachineToMachineTokenResponse

| Field Name  | Required | Nullable | Type   | Description                 | Format |
|-------------|----------|----------|--------|-----------------------------|--------|
| accessToken |          |          | String | The exchanged access token. |        |

<a id="V1ExchangeTokenRequest_CommonObjectReference"></a>

## V1ExchangeTokenRequest

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| externalToken |  |  | String | The external authentication token. The server will mask the value of this credential in responses and logs. |  |
| type |  |  | String |  |  |
| state |  |  | String |  |  |

<a id="V1ExchangeTokenResponse_CommonObjectReference"></a>

## V1ExchangeTokenResponse

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| token |  |  | String |  |  |
| clientState |  |  | String |  |  |
| test |  |  | Boolean |  |  |
| user |  |  | [V1AuthStatus](#V1AuthStatus_CommonObjectReference) |  |  |

<a id="V1ExportDeploymentResponse_CommonObjectReference"></a>

## V1ExportDeploymentResponse

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| deployment |  |  | [StorageDeployment](#StorageDeployment_CommonObjectReference) |  |  |

<a id="V1ExportImageResponse_CommonObjectReference"></a>

## V1ExportImageResponse

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| image |  |  | [StorageImage](#StorageImage_CommonObjectReference) |  |  |

<a id="V1ExportNodeResponse_CommonObjectReference"></a>

## V1ExportNodeResponse

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| node |  |  | [StorageNode](#StorageNode_CommonObjectReference) |  |  |

<a id="V1ExportPodResponse_CommonObjectReference"></a>

## V1ExportPodResponse

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| pod |  |  | [StoragePod](#StoragePod_CommonObjectReference) |  |  |

<a id="V1ExportPoliciesRequest_CommonObjectReference"></a>

## V1ExportPoliciesRequest

| Field Name | Required | Nullable | Type             | Description | Format |
|------------|----------|----------|------------------|-------------|--------|
| policyIds  |          |          | List of `string` |             |        |

<a id="V1ExternalNetworkFlowMetadata_CommonObjectReference"></a>

## V1ExternalNetworkFlowMetadata

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| entity |  |  | [StorageNetworkEntityInfo](#StorageNetworkEntityInfo_CommonObjectReference) |  |  |
| flowsCount |  |  | Integer |  | int32 |

<a id="V1FeatureFlag_CommonObjectReference"></a>

## V1FeatureFlag

| Field Name | Required | Nullable | Type    | Description | Format |
|------------|----------|----------|---------|-------------|--------|
| name       |          |          | String  |             |        |
| envVar     |          |          | String  |             |        |
| enabled    |          |          | Boolean |             |        |

<a id="V1GenerateNetworkPoliciesResponse_CommonObjectReference"></a>

## V1GenerateNetworkPoliciesResponse

Next available tag: 2

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| modification |  |  | [StorageNetworkPolicyModification](#StorageNetworkPolicyModification_CommonObjectReference) |  |  |

<a id="V1GenerateTokenRequest_CommonObjectReference"></a>

## V1GenerateTokenRequest

| Field Name | Required | Nullable | Type             | Description | Format    |
|------------|----------|----------|------------------|-------------|-----------|
| name       |          |          | String           |             |           |
| role       |          |          | String           |             |           |
| roles      |          |          | List of `string` |             |           |
| expiration |          |          | Date             |             | date-time |

<a id="V1GenerateTokenResponse_CommonObjectReference"></a>

## V1GenerateTokenResponse

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| token |  |  | String |  |  |
| metadata |  |  | [StorageTokenMetadata](#StorageTokenMetadata_CommonObjectReference) |  |  |

<a id="V1GetAPITokensResponse_CommonObjectReference"></a>

## V1GetAPITokensResponse

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| tokens |  |  | List of [StorageTokenMetadata](#StorageTokenMetadata_CommonObjectReference) |  |  |

<a id="V1GetActiveDBRestoreProcessResponse_CommonObjectReference"></a>

## V1GetActiveDBRestoreProcessResponse

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| activeStatus |  |  | [V1DBRestoreProcessStatus](#V1DBRestoreProcessStatus_CommonObjectReference) |  |  |

<a id="V1GetAdministrationEventResponse_CommonObjectReference"></a>

## V1GetAdministrationEventResponse

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| event |  |  | [V1AdministrationEvent](#V1AdministrationEvent_CommonObjectReference) |  |  |

<a id="V1GetAlertTimeseriesResponse_CommonObjectReference"></a>

## V1GetAlertTimeseriesResponse

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| clusters |  |  | List of [GetAlertTimeseriesResponseClusterAlerts](#GetAlertTimeseriesResponseClusterAlerts_CommonObjectReference) |  |  |

<a id="V1GetAlertsCountsResponse_CommonObjectReference"></a>

## V1GetAlertsCountsResponse

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| groups |  |  | List of [GetAlertsCountsResponseAlertGroup](#GetAlertsCountsResponseAlertGroup_CommonObjectReference) |  |  |

<a id="V1GetAlertsGroupResponse_CommonObjectReference"></a>

## V1GetAlertsGroupResponse

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| alertsByPolicies |  |  | List of [V1GetAlertsGroupResponsePolicyGroup](#V1GetAlertsGroupResponsePolicyGroup_CommonObjectReference) |  |  |

<a id="V1GetAlertsGroupResponsePolicyGroup_CommonObjectReference"></a>

## V1GetAlertsGroupResponsePolicyGroup

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| policy |  |  | [StorageListAlertPolicy](#StorageListAlertPolicy_CommonObjectReference) |  |  |
| numAlerts |  |  | String |  | int64 |

<a id="V1GetAllowedPeersFromCurrentPolicyForDeploymentResponse_CommonObjectReference"></a>

## V1GetAllowedPeersFromCurrentPolicyForDeploymentResponse

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| allowedPeers |  |  | List of [V1NetworkBaselineStatusPeer](#V1NetworkBaselineStatusPeer_CommonObjectReference) |  |  |

<a id="V1GetAuthMachineToMachineConfigResponse_CommonObjectReference"></a>

## V1GetAuthMachineToMachineConfigResponse

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| config |  |  | [V1AuthMachineToMachineConfig](#V1AuthMachineToMachineConfig_CommonObjectReference) |  |  |

<a id="V1GetAuthProvidersResponse_CommonObjectReference"></a>

## V1GetAuthProvidersResponse

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| authProviders |  |  | List of [StorageAuthProvider](#StorageAuthProvider_CommonObjectReference) |  |  |

<a id="V1GetBaselineGeneratedPolicyForDeploymentResponse_CommonObjectReference"></a>

## V1GetBaselineGeneratedPolicyForDeploymentResponse

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| modification |  |  | [StorageNetworkPolicyModification](#StorageNetworkPolicyModification_CommonObjectReference) |  |  |

<a id="V1GetCAConfigResponse_CommonObjectReference"></a>

## V1GetCAConfigResponse

| Field Name       | Required | Nullable | Type     | Description | Format |
|------------------|----------|----------|----------|-------------|--------|
| helmValuesBundle |          |          | byte\[\] |             | byte   |

<a id="V1GetCertExpiryComponent_CommonObjectReference"></a>

## V1GetCertExpiryComponent

| Enum Values |
|-------------|
| UNKNOWN     |
| CENTRAL     |
| SCANNER     |
| SCANNER_V4  |
| CENTRAL_DB  |

<a id="V1GetCertExpiryResponse_CommonObjectReference"></a>

## V1GetCertExpiryResponse

| Field Name | Required | Nullable | Type | Description | Format    |
|------------|----------|----------|------|-------------|-----------|
| expiry     |          |          | Date |             | date-time |

<a id="V1GetCloudSourceResponse_CommonObjectReference"></a>

## V1GetCloudSourceResponse

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| cloudSource |  |  | [V1CloudSource](#V1CloudSource_CommonObjectReference) |  |  |

<a id="V1GetClustersForPermissionsResponse_CommonObjectReference"></a>

## V1GetClustersForPermissionsResponse

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| clusters |  |  | List of [V1ScopeObject](#V1ScopeObject_CommonObjectReference) |  |  |

<a id="V1GetCollectionCountResponse_CommonObjectReference"></a>

## V1GetCollectionCountResponse

| Field Name | Required | Nullable | Type    | Description | Format |
|------------|----------|----------|---------|-------------|--------|
| count      |          |          | Integer |             | int32  |

<a id="V1GetCollectionResponse_CommonObjectReference"></a>

## V1GetCollectionResponse

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| collection |  |  | [StorageResourceCollection](#StorageResourceCollection_CommonObjectReference) |  |  |
| deployments |  |  | List of [StorageListDeployment](#StorageListDeployment_CommonObjectReference) |  |  |

<a id="V1GetComplianceRunResultsResponse_CommonObjectReference"></a>

## V1GetComplianceRunResultsResponse

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| results |  |  | [StorageComplianceRunResults](#StorageComplianceRunResults_CommonObjectReference) |  |  |
| failedRuns |  |  | List of [StorageComplianceRunMetadata](#StorageComplianceRunMetadata_CommonObjectReference) |  |  |

<a id="V1GetComplianceRunStatusesResponse_CommonObjectReference"></a>

## V1GetComplianceRunStatusesResponse

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| invalidRunIds |  |  | List of `string` |  |  |
| runs |  |  | List of [V1ComplianceRun](#V1ComplianceRun_CommonObjectReference) |  |  |

<a id="V1GetComplianceStandardResponse_CommonObjectReference"></a>

## V1GetComplianceStandardResponse

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| standard |  |  | [V1ComplianceStandard](#V1ComplianceStandard_CommonObjectReference) |  |  |

<a id="V1GetComplianceStandardsResponse_CommonObjectReference"></a>

## V1GetComplianceStandardsResponse

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| standards |  |  | List of [V1ComplianceStandardMetadata](#V1ComplianceStandardMetadata_CommonObjectReference) |  |  |

<a id="V1GetDBExportCapabilitiesResponse_CommonObjectReference"></a>

## V1GetDBExportCapabilitiesResponse

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| formats |  |  | List of [V1DBExportFormat](#V1DBExportFormat_CommonObjectReference) |  |  |
| supportedEncodings |  |  | List of [DBExportManifestEncodingType](#DBExportManifestEncodingType_CommonObjectReference) |  |  |

<a id="V1GetDeclarativeConfigHealthsResponse_CommonObjectReference"></a>

## V1GetDeclarativeConfigHealthsResponse

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| healths |  |  | List of [StorageDeclarativeConfigHealth](#StorageDeclarativeConfigHealth_CommonObjectReference) |  |  |

<a id="V1GetDefaultRedHatLayeredProductsRegexResponse_CommonObjectReference"></a>

## V1GetDefaultRedHatLayeredProductsRegexResponse

| Field Name | Required | Nullable | Type   | Description | Format |
|------------|----------|----------|--------|-------------|--------|
| regex      |          |          | String |             |        |

<a id="V1GetDeploymentWithRiskResponse_CommonObjectReference"></a>

## V1GetDeploymentWithRiskResponse

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| deployment |  |  | [StorageDeployment](#StorageDeployment_CommonObjectReference) |  |  |
| risk |  |  | [StorageRisk](#StorageRisk_CommonObjectReference) |  |  |

<a id="V1GetDiffFlowsGroupedFlow_CommonObjectReference"></a>

## V1GetDiffFlowsGroupedFlow

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| entity |  |  | [StorageNetworkEntityInfo](#StorageNetworkEntityInfo_CommonObjectReference) |  |  |
| properties |  |  | List of [StorageNetworkBaselineConnectionProperties](#StorageNetworkBaselineConnectionProperties_CommonObjectReference) |  |  |

<a id="V1GetDiffFlowsReconciledFlow_CommonObjectReference"></a>

## V1GetDiffFlowsReconciledFlow

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| entity |  |  | [StorageNetworkEntityInfo](#StorageNetworkEntityInfo_CommonObjectReference) |  |  |
| added |  |  | List of [StorageNetworkBaselineConnectionProperties](#StorageNetworkBaselineConnectionProperties_CommonObjectReference) |  |  |
| removed |  |  | List of [StorageNetworkBaselineConnectionProperties](#StorageNetworkBaselineConnectionProperties_CommonObjectReference) |  |  |
| unchanged |  |  | List of [StorageNetworkBaselineConnectionProperties](#StorageNetworkBaselineConnectionProperties_CommonObjectReference) |  |  |

<a id="V1GetDiffFlowsResponse_CommonObjectReference"></a>

## V1GetDiffFlowsResponse

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| added |  |  | List of [V1GetDiffFlowsGroupedFlow](#V1GetDiffFlowsGroupedFlow_CommonObjectReference) |  |  |
| removed |  |  | List of [V1GetDiffFlowsGroupedFlow](#V1GetDiffFlowsGroupedFlow_CommonObjectReference) |  |  |
| reconciled |  |  | List of [V1GetDiffFlowsReconciledFlow](#V1GetDiffFlowsReconciledFlow_CommonObjectReference) |  |  |

<a id="V1GetDiscoveredClusterResponse_CommonObjectReference"></a>

## V1GetDiscoveredClusterResponse

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| cluster |  |  | [V1DiscoveredCluster](#V1DiscoveredCluster_CommonObjectReference) |  |  |

<a id="V1GetExistingProbesResponse_CommonObjectReference"></a>

## V1GetExistingProbesResponse

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| existingFiles |  |  | List of [V1ProbeUploadManifestFile](#V1ProbeUploadManifestFile_CommonObjectReference) |  |  |

<a id="V1GetExternalBackupsResponse_CommonObjectReference"></a>

## V1GetExternalBackupsResponse

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| externalBackups |  |  | List of [StorageExternalBackup](#StorageExternalBackup_CommonObjectReference) |  |  |

<a id="V1GetExternalNetworkEntitiesResponse_CommonObjectReference"></a>

## V1GetExternalNetworkEntitiesResponse

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| entities |  |  | List of [StorageNetworkEntity](#StorageNetworkEntity_CommonObjectReference) |  |  |

<a id="V1GetExternalNetworkFlowsMetadataResponse_CommonObjectReference"></a>

## V1GetExternalNetworkFlowsMetadataResponse

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| entities |  |  | List of [V1ExternalNetworkFlowMetadata](#V1ExternalNetworkFlowMetadata_CommonObjectReference) |  |  |
| totalEntities |  |  | Integer |  | int32 |

<a id="V1GetExternalNetworkFlowsResponse_CommonObjectReference"></a>

## V1GetExternalNetworkFlowsResponse

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| entity |  |  | [StorageNetworkEntityInfo](#StorageNetworkEntityInfo_CommonObjectReference) |  |  |
| totalFlows |  |  | Integer |  | int32 |
| flows |  |  | List of [StorageNetworkFlow](#StorageNetworkFlow_CommonObjectReference) |  |  |

<a id="V1GetFeatureFlagsResponse_CommonObjectReference"></a>

## V1GetFeatureFlagsResponse

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| featureFlags |  |  | List of [V1FeatureFlag](#V1FeatureFlag_CommonObjectReference) |  |  |

<a id="V1GetGroupedProcessesResponse_CommonObjectReference"></a>

## V1GetGroupedProcessesResponse

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| groups |  |  | List of [V1ProcessNameGroup](#V1ProcessNameGroup_CommonObjectReference) |  |  |

<a id="V1GetGroupedProcessesWithContainerResponse_CommonObjectReference"></a>

## V1GetGroupedProcessesWithContainerResponse

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| groups |  |  | List of [V1ProcessNameAndContainerNameGroup](#V1ProcessNameAndContainerNameGroup_CommonObjectReference) |  |  |

<a id="V1GetGroupsResponse_CommonObjectReference"></a>

## V1GetGroupsResponse

API for updating Groups and getting users. Next Available Tag: 2

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| groups |  |  | List of [StorageGroup](#StorageGroup_CommonObjectReference) |  |  |

<a id="V1GetImageIntegrationsResponse_CommonObjectReference"></a>

## V1GetImageIntegrationsResponse

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| integrations |  |  | List of [StorageImageIntegration](#StorageImageIntegration_CommonObjectReference) |  |  |

<a id="V1GetIntegrationHealthResponse_CommonObjectReference"></a>

## V1GetIntegrationHealthResponse

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| integrationHealth |  |  | List of [StorageIntegrationHealth](#StorageIntegrationHealth_CommonObjectReference) |  |  |

<a id="V1GetLoginAuthProvidersResponse_CommonObjectReference"></a>

## V1GetLoginAuthProvidersResponse

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| authProviders |  |  | List of [GetLoginAuthProvidersResponseLoginAuthProvider](#GetLoginAuthProvidersResponseLoginAuthProvider_CommonObjectReference) |  |  |

<a id="V1GetMitreVectorResponse_CommonObjectReference"></a>

## V1GetMitreVectorResponse

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| mitreAttackVector |  |  | [StorageMitreAttackVector](#StorageMitreAttackVector_CommonObjectReference) |  |  |

<a id="V1GetNamespacesForClusterAndPermissionsResponse_CommonObjectReference"></a>

## V1GetNamespacesForClusterAndPermissionsResponse

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| namespaces |  |  | List of [V1ScopeObject](#V1ScopeObject_CommonObjectReference) |  |  |

<a id="V1GetNamespacesResponse_CommonObjectReference"></a>

## V1GetNamespacesResponse

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| namespaces |  |  | List of [V1Namespace](#V1Namespace_CommonObjectReference) |  |  |

<a id="V1GetNotifiersResponse_CommonObjectReference"></a>

## V1GetNotifiersResponse

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| notifiers |  |  | List of [StorageNotifier](#StorageNotifier_CommonObjectReference) |  |  |

<a id="V1GetPermissionsResponse_CommonObjectReference"></a>

## V1GetPermissionsResponse

GetPermissionsResponse is wire-compatible with the old format of the Role message and represents a collection of aggregated permissions.

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| resourceToAccess |  |  | Map of [StorageAccess](#StorageAccess_CommonObjectReference) |  |  |

<a id="V1GetPolicyCategoriesResponse_CommonObjectReference"></a>

## V1GetPolicyCategoriesResponse

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| categories |  |  | List of [V1PolicyCategory](#V1PolicyCategory_CommonObjectReference) |  |  |

<a id="V1GetPolicyMitreVectorsRequestOptions_CommonObjectReference"></a>

## V1GetPolicyMitreVectorsRequestOptions

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| excludePolicy |  |  | Boolean | If set to true, policy is excluded from the response. |  |

<a id="V1GetPolicyMitreVectorsResponse_CommonObjectReference"></a>

## V1GetPolicyMitreVectorsResponse

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| policy |  |  | [StoragePolicy](#StoragePolicy_CommonObjectReference) |  |  |
| vectors |  |  | List of [StorageMitreAttackVector](#StorageMitreAttackVector_CommonObjectReference) |  |  |

<a id="V1GetProcessesListeningOnPortsResponse_CommonObjectReference"></a>

## V1GetProcessesListeningOnPortsResponse

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| listeningEndpoints |  |  | List of [StorageProcessListeningOnPort](#StorageProcessListeningOnPort_CommonObjectReference) |  |  |
| totalListeningEndpoints |  |  | Integer |  | int32 |

<a id="V1GetProcessesResponse_CommonObjectReference"></a>

## V1GetProcessesResponse

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| processes |  |  | List of [StorageProcessIndicator](#StorageProcessIndicator_CommonObjectReference) |  |  |

<a id="V1GetRecentComplianceRunsResponse_CommonObjectReference"></a>

## V1GetRecentComplianceRunsResponse

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| complianceRuns |  |  | List of [V1ComplianceRun](#V1ComplianceRun_CommonObjectReference) |  |  |

<a id="V1GetReportConfigurationResponse_CommonObjectReference"></a>

## V1GetReportConfigurationResponse

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| reportConfig |  |  | [StorageReportConfiguration](#StorageReportConfiguration_CommonObjectReference) |  |  |

<a id="V1GetReportConfigurationsResponse_CommonObjectReference"></a>

## V1GetReportConfigurationsResponse

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| reportConfigs |  |  | List of [StorageReportConfiguration](#StorageReportConfiguration_CommonObjectReference) |  |  |

<a id="V1GetResourcesResponse_CommonObjectReference"></a>

## V1GetResourcesResponse

| Field Name | Required | Nullable | Type             | Description | Format |
|------------|----------|----------|------------------|-------------|--------|
| resources  |          |          | List of `string` |             |        |

<a id="V1GetRoleBindingResponse_CommonObjectReference"></a>

## V1GetRoleBindingResponse

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| binding |  |  | [StorageK8sRoleBinding](#StorageK8sRoleBinding_CommonObjectReference) |  |  |

<a id="V1GetRoleResponse_CommonObjectReference"></a>

## V1GetRoleResponse

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| role |  |  | [StorageK8sRole](#StorageK8sRole_CommonObjectReference) |  |  |

<a id="V1GetRolesResponse_CommonObjectReference"></a>

## V1GetRolesResponse

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| roles |  |  | List of [StorageRole](#StorageRole_CommonObjectReference) |  |  |

<a id="V1GetSensorUpgradeConfigResponse_CommonObjectReference"></a>

## V1GetSensorUpgradeConfigResponse

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| config |  |  | [GetSensorUpgradeConfigResponseUpgradeConfig](#GetSensorUpgradeConfigResponseUpgradeConfig_CommonObjectReference) |  |  |

<a id="V1GetServiceAccountResponse_CommonObjectReference"></a>

## V1GetServiceAccountResponse

One service account Next Tag: 2

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| saAndRole |  |  | [V1ServiceAccountAndRoles](#V1ServiceAccountAndRoles_CommonObjectReference) |  |  |

<a id="V1GetSubjectResponse_CommonObjectReference"></a>

## V1GetSubjectResponse

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| subject |  |  | [StorageSubject](#StorageSubject_CommonObjectReference) |  |  |
| clusterRoles |  |  | List of [StorageK8sRole](#StorageK8sRole_CommonObjectReference) |  |  |
| scopedRoles |  |  | List of [V1ScopedRoles](#V1ScopedRoles_CommonObjectReference) |  |  |

<a id="V1GetUndoModificationForDeploymentResponse_CommonObjectReference"></a>

## V1GetUndoModificationForDeploymentResponse

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| undoRecord |  |  | [StorageNetworkPolicyApplicationUndoRecord](#StorageNetworkPolicyApplicationUndoRecord_CommonObjectReference) |  |  |

<a id="V1GetUndoModificationResponse_CommonObjectReference"></a>

## V1GetUndoModificationResponse

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| undoRecord |  |  | [StorageNetworkPolicyApplicationUndoRecord](#StorageNetworkPolicyApplicationUndoRecord_CommonObjectReference) |  |  |

<a id="V1GetUpgradeStatusResponse_CommonObjectReference"></a>

## V1GetUpgradeStatusResponse

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| upgradeStatus |  |  | [V1CentralUpgradeStatus](#V1CentralUpgradeStatus_CommonObjectReference) |  |  |

<a id="V1GetUsersAttributesResponse_CommonObjectReference"></a>

## V1GetUsersAttributesResponse

Next Tag: 2

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| usersAttributes |  |  | List of [V1UserAttributeTuple](#V1UserAttributeTuple_CommonObjectReference) |  |  |

<a id="V1GetUsersResponse_CommonObjectReference"></a>

## V1GetUsersResponse

Next Tag: 2

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| users |  |  | List of [StorageUser](#StorageUser_CommonObjectReference) |  |  |

<a id="V1GetVulnerabilityExceptionConfigResponse_CommonObjectReference"></a>

## V1GetVulnerabilityExceptionConfigResponse

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| config |  |  | [V1VulnerabilityExceptionConfig](#V1VulnerabilityExceptionConfig_CommonObjectReference) |  |  |

<a id="V1GetWatchedImagesResponse_CommonObjectReference"></a>

## V1GetWatchedImagesResponse

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| watchedImages |  |  | List of [StorageWatchedImage](#StorageWatchedImage_CommonObjectReference) |  |  |

<a id="V1GroupBatchUpdateRequest_CommonObjectReference"></a>

## V1GroupBatchUpdateRequest

GroupBatchUpdateRequest is an in transaction batch update to the groups present. Next Available Tag: 3

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| previousGroups |  |  | List of [StorageGroup](#StorageGroup_CommonObjectReference) | Previous groups are the groups expected to be present in the store. Performs a diff on the GroupProperties present in previous_groups and required_groups: 1) if in previous_groups but not required_groups, it gets deleted. 2) if in previous_groups and required_groups, it gets updated. 3) if not in previous_groups but in required_groups, it gets added. |  |
| requiredGroups |  |  | List of [StorageGroup](#StorageGroup_CommonObjectReference) | Required groups are the groups we want to mutate the previous groups into. |  |
| force |  |  | Boolean |  |  |

<a id="V1ImportPoliciesMetadata_CommonObjectReference"></a>

## V1ImportPoliciesMetadata

| Field Name | Required | Nullable | Type    | Description | Format |
|------------|----------|----------|---------|-------------|--------|
| overwrite  |          |          | Boolean |             |        |

<a id="V1ImportPoliciesRequest_CommonObjectReference"></a>

## V1ImportPoliciesRequest

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| metadata |  |  | [V1ImportPoliciesMetadata](#V1ImportPoliciesMetadata_CommonObjectReference) |  |  |
| policies |  |  | List of [StoragePolicy](#StoragePolicy_CommonObjectReference) |  |  |

<a id="V1ImportPoliciesResponse_CommonObjectReference"></a>

## V1ImportPoliciesResponse

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| responses |  |  | List of [V1ImportPolicyResponse](#V1ImportPolicyResponse_CommonObjectReference) |  |  |
| allSucceeded |  |  | Boolean |  |  |

<a id="V1ImportPolicyError_CommonObjectReference"></a>

## V1ImportPolicyError

| Field Name      | Required | Nullable | Type   | Description | Format |
|-----------------|----------|----------|--------|-------------|--------|
| message         |          |          | String |             |        |
| type            |          |          | String |             |        |
| duplicateName   |          |          | String |             |        |
| validationError |          |          | String |             |        |

<a id="V1ImportPolicyResponse_CommonObjectReference"></a>

## V1ImportPolicyResponse

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| succeeded |  |  | Boolean |  |  |
| policy |  |  | [StoragePolicy](#StoragePolicy_CommonObjectReference) |  |  |
| errors |  |  | List of [V1ImportPolicyError](#V1ImportPolicyError_CommonObjectReference) |  |  |

<a id="V1InitBundleGenRequest_CommonObjectReference"></a>

## V1InitBundleGenRequest

| Field Name | Required | Nullable | Type   | Description | Format |
|------------|----------|----------|--------|-------------|--------|
| name       |          |          | String |             |        |

<a id="V1InitBundleGenResponse_CommonObjectReference"></a>

## V1InitBundleGenResponse

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| meta |  |  | [V1InitBundleMeta](#V1InitBundleMeta_CommonObjectReference) |  |  |
| helmValuesBundle |  |  | byte\[\] |  | byte |
| kubectlBundle |  |  | byte\[\] |  | byte |

<a id="V1InitBundleMeta_CommonObjectReference"></a>

## V1InitBundleMeta

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| id |  |  | String |  |  |
| name |  |  | String |  |  |
| impactedClusters |  |  | List of [InitBundleMetaImpactedCluster](#InitBundleMetaImpactedCluster_CommonObjectReference) |  |  |
| createdAt |  |  | Date |  | date-time |
| createdBy |  |  | [StorageUser](#StorageUser_CommonObjectReference) |  |  |
| expiresAt |  |  | Date |  | date-time |

<a id="V1InitBundleMetasResponse_CommonObjectReference"></a>

## V1InitBundleMetasResponse

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| items |  |  | List of [V1InitBundleMeta](#V1InitBundleMeta_CommonObjectReference) |  |  |

<a id="V1InitBundleRevokeRequest_CommonObjectReference"></a>

## V1InitBundleRevokeRequest

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| ids |  |  | List of `string` |  |  |
| confirmImpactedClustersIds |  |  | List of `string` |  |  |

<a id="V1InitBundleRevokeResponse_CommonObjectReference"></a>

## V1InitBundleRevokeResponse

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| initBundleRevocationErrors |  |  | List of [InitBundleRevokeResponseInitBundleRevocationError](#InitBundleRevokeResponseInitBundleRevocationError_CommonObjectReference) |  |  |
| initBundleRevokedIds |  |  | List of `string` |  |  |

<a id="V1InterruptDBRestoreProcessResponse_CommonObjectReference"></a>

## V1InterruptDBRestoreProcessResponse

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| resumeInfo |  |  | [DBRestoreProcessStatusResumeInfo](#DBRestoreProcessStatusResumeInfo_CommonObjectReference) |  |  |

<a id="V1JobId_CommonObjectReference"></a>

## V1JobId

| Field Name | Required | Nullable | Type   | Description | Format |
|------------|----------|----------|--------|-------------|--------|
| jobId      |          |          | String |             |        |

<a id="V1KernelSupportAvailableResponse_CommonObjectReference"></a>

## V1KernelSupportAvailableResponse

| Field Name             | Required | Nullable | Type    | Description | Format |
|------------------------|----------|----------|---------|-------------|--------|
| kernelSupportAvailable |          |          | Boolean |             |        |

<a id="V1ListAdministrationEventsResponse_CommonObjectReference"></a>

## V1ListAdministrationEventsResponse

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| events |  |  | List of [V1AdministrationEvent](#V1AdministrationEvent_CommonObjectReference) |  |  |

<a id="V1ListAlertsRequest_CommonObjectReference"></a>

## V1ListAlertsRequest

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| query |  |  | String |  |  |
| pagination |  |  | [V1Pagination](#V1Pagination_CommonObjectReference) |  |  |

<a id="V1ListAlertsResponse_CommonObjectReference"></a>

## V1ListAlertsResponse

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| alerts |  |  | List of [StorageListAlert](#StorageListAlert_CommonObjectReference) |  |  |

<a id="V1ListAllowedTokenRolesResponse_CommonObjectReference"></a>

## V1ListAllowedTokenRolesResponse

| Field Name | Required | Nullable | Type             | Description | Format |
|------------|----------|----------|------------------|-------------|--------|
| roleNames  |          |          | List of `string` |             |        |

<a id="V1ListAuthMachineToMachineConfigResponse_CommonObjectReference"></a>

## V1ListAuthMachineToMachineConfigResponse

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| configs |  |  | List of [V1AuthMachineToMachineConfig](#V1AuthMachineToMachineConfig_CommonObjectReference) |  |  |

<a id="V1ListCloudSourcesResponse_CommonObjectReference"></a>

## V1ListCloudSourcesResponse

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| cloudSources |  |  | List of [V1CloudSource](#V1CloudSource_CommonObjectReference) |  |  |

<a id="V1ListCollectionSelectorsResponse_CommonObjectReference"></a>

## V1ListCollectionSelectorsResponse

| Field Name | Required | Nullable | Type             | Description | Format |
|------------|----------|----------|------------------|-------------|--------|
| selectors  |          |          | List of `string` |             |        |

<a id="V1ListCollectionsResponse_CommonObjectReference"></a>

## V1ListCollectionsResponse

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| collections |  |  | List of [StorageResourceCollection](#StorageResourceCollection_CommonObjectReference) |  |  |

<a id="V1ListDeploymentsResponse_CommonObjectReference"></a>

## V1ListDeploymentsResponse

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| deployments |  |  | List of [StorageListDeployment](#StorageListDeployment_CommonObjectReference) |  |  |

<a id="V1ListDeploymentsWithProcessInfoResponse_CommonObjectReference"></a>

## V1ListDeploymentsWithProcessInfoResponse

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| deployments |  |  | List of [ListDeploymentsWithProcessInfoResponseDeploymentWithProcessInfo](#ListDeploymentsWithProcessInfoResponseDeploymentWithProcessInfo_CommonObjectReference) |  |  |

<a id="V1ListDiscoveredClustersResponse_CommonObjectReference"></a>

## V1ListDiscoveredClustersResponse

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| clusters |  |  | List of [V1DiscoveredCluster](#V1DiscoveredCluster_CommonObjectReference) |  |  |

<a id="V1ListImagesResponse_CommonObjectReference"></a>

## V1ListImagesResponse

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| images |  |  | List of [StorageListImage](#StorageListImage_CommonObjectReference) |  |  |

<a id="V1ListMitreAttackVectorsResponse_CommonObjectReference"></a>

## V1ListMitreAttackVectorsResponse

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| mitreAttackVectors |  |  | List of [StorageMitreAttackVector](#StorageMitreAttackVector_CommonObjectReference) |  |  |

<a id="V1ListNodesResponse_CommonObjectReference"></a>

## V1ListNodesResponse

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| nodes |  |  | List of [StorageNode](#StorageNode_CommonObjectReference) |  |  |

<a id="V1ListPermissionSetsResponse_CommonObjectReference"></a>

## V1ListPermissionSetsResponse

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| permissionSets |  |  | List of [StoragePermissionSet](#StoragePermissionSet_CommonObjectReference) |  |  |

<a id="V1ListPoliciesResponse_CommonObjectReference"></a>

## V1ListPoliciesResponse

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| policies |  |  | List of [StorageListPolicy](#StorageListPolicy_CommonObjectReference) |  |  |

<a id="V1ListRoleBindingsResponse_CommonObjectReference"></a>

## V1ListRoleBindingsResponse

A list of k8s role bindings (free of scoped information) Next Tag: 2

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| bindings |  |  | List of [StorageK8sRoleBinding](#StorageK8sRoleBinding_CommonObjectReference) |  |  |

<a id="V1ListRolesResponse_CommonObjectReference"></a>

## V1ListRolesResponse

A list of k8s roles (free of scoped information) Next Tag: 2

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| roles |  |  | List of [StorageK8sRole](#StorageK8sRole_CommonObjectReference) |  |  |

<a id="V1ListSecretsResponse_CommonObjectReference"></a>

## V1ListSecretsResponse

A list of secrets with their relationships. Next Tag: 2

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| secrets |  |  | List of [StorageListSecret](#StorageListSecret_CommonObjectReference) |  |  |

<a id="V1ListServiceAccountResponse_CommonObjectReference"></a>

## V1ListServiceAccountResponse

A list of service accounts (free of scoped information) Next Tag: 2

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| saAndRoles |  |  | List of [V1ServiceAccountAndRoles](#V1ServiceAccountAndRoles_CommonObjectReference) |  |  |

<a id="V1ListSignatureIntegrationsResponse_CommonObjectReference"></a>

## V1ListSignatureIntegrationsResponse

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| integrations |  |  | List of [StorageSignatureIntegration](#StorageSignatureIntegration_CommonObjectReference) |  |  |

<a id="V1ListSimpleAccessScopesResponse_CommonObjectReference"></a>

## V1ListSimpleAccessScopesResponse

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| accessScopes |  |  | List of [StorageSimpleAccessScope](#StorageSimpleAccessScope_CommonObjectReference) |  |  |

<a id="V1ListSubjectsResponse_CommonObjectReference"></a>

## V1ListSubjectsResponse

A list of k8s subjects (users and groups only, for service accounts, try the service account service) Next Tag: 2

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| subjectAndRoles |  |  | List of [V1SubjectAndRoles](#V1SubjectAndRoles_CommonObjectReference) |  |  |

<a id="V1LockProcessBaselinesRequest_CommonObjectReference"></a>

## V1LockProcessBaselinesRequest

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| keys |  |  | List of [StorageProcessBaselineKey](#StorageProcessBaselineKey_CommonObjectReference) |  |  |
| locked |  |  | Boolean |  |  |

<a id="V1LogLevelRequest_CommonObjectReference"></a>

## V1LogLevelRequest

| Field Name | Required | Nullable | Type             | Description | Format |
|------------|----------|----------|------------------|-------------|--------|
| level      |          |          | String           |             |        |
| modules    |          |          | List of `string` |             |        |

<a id="V1LogLevelResponse_CommonObjectReference"></a>

## V1LogLevelResponse

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| level |  |  | String |  |  |
| moduleLevels |  |  | List of [V1ModuleLevel](#V1ModuleLevel_CommonObjectReference) |  |  |

<a id="V1MaxSecuredUnitsUsageResponse_CommonObjectReference"></a>

## V1MaxSecuredUnitsUsageResponse

MaxSecuredUnitsUsageResponse holds the maximum values of the secured nodes and CPU Units (as reported by Kubernetes) with the time at which these values were aggregated, with the aggregation period accuracy (1h).

| Field Name    | Required | Nullable | Type   | Description | Format    |
|---------------|----------|----------|--------|-------------|-----------|
| maxNodesAt    |          |          | Date   |             | date-time |
| maxNodes      |          |          | String |             | int64     |
| maxCpuUnitsAt |          |          | Date   |             | date-time |
| maxCpuUnits   |          |          | String |             | int64     |

<a id="V1Metadata_CommonObjectReference"></a>

## V1Metadata

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| version |  |  | String |  |  |
| buildFlavor |  |  | String |  |  |
| releaseBuild |  |  | Boolean |  |  |
| licenseStatus |  |  | [MetadataLicenseStatus](#MetadataLicenseStatus_CommonObjectReference) |  | NONE, INVALID, EXPIRED, RESTARTING, VALID, |

<a id="V1ModuleLevel_CommonObjectReference"></a>

## V1ModuleLevel

| Field Name | Required | Nullable | Type   | Description | Format |
|------------|----------|----------|--------|-------------|--------|
| module     |          |          | String |             |        |
| level      |          |          | String |             |        |

<a id="V1Namespace_CommonObjectReference"></a>

## V1Namespace

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| metadata |  |  | [StorageNamespaceMetadata](#StorageNamespaceMetadata_CommonObjectReference) |  |  |
| numDeployments |  |  | Integer |  | int32 |
| numSecrets |  |  | Integer |  | int32 |
| numNetworkPolicies |  |  | Integer |  | int32 |

<a id="V1NetworkBaselineExternalStatusResponse_CommonObjectReference"></a>

## V1NetworkBaselineExternalStatusResponse

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| anomalous |  |  | List of [V1NetworkBaselinePeerStatus](#V1NetworkBaselinePeerStatus_CommonObjectReference) |  |  |
| totalAnomalous |  |  | Integer |  | int32 |
| baseline |  |  | List of [V1NetworkBaselinePeerStatus](#V1NetworkBaselinePeerStatus_CommonObjectReference) |  |  |
| totalBaseline |  |  | Integer |  | int32 |

<a id="V1NetworkBaselinePeerEntity_CommonObjectReference"></a>

## V1NetworkBaselinePeerEntity

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| id |  |  | String |  |  |
| type |  |  | [StorageNetworkEntityInfoType](#StorageNetworkEntityInfoType_CommonObjectReference) |  | UNKNOWN_TYPE, DEPLOYMENT, INTERNET, LISTEN_ENDPOINT, EXTERNAL_SOURCE, INTERNAL_ENTITIES, |
| name |  |  | String |  |  |
| discovered |  |  | Boolean |  |  |

<a id="V1NetworkBaselinePeerStatus_CommonObjectReference"></a>

## V1NetworkBaselinePeerStatus

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| peer |  |  | [V1NetworkBaselineStatusPeer](#V1NetworkBaselineStatusPeer_CommonObjectReference) |  |  |
| status |  |  | [V1NetworkBaselinePeerStatusStatus](#V1NetworkBaselinePeerStatusStatus_CommonObjectReference) |  | BASELINE, ANOMALOUS, |

<a id="V1NetworkBaselinePeerStatusStatus_CommonObjectReference"></a>

## V1NetworkBaselinePeerStatusStatus

Status of this peer connection. As of now we only have two statuses: - BASELINE: the connection is in the current deployment baseline - ANOMALOUS: the connection is not recognized by the current deployment baseline

| Enum Values |
|-------------|
| BASELINE    |
| ANOMALOUS   |

<a id="V1NetworkBaselineStatusPeer_CommonObjectReference"></a>

## V1NetworkBaselineStatusPeer

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| entity |  |  | [V1NetworkBaselinePeerEntity](#V1NetworkBaselinePeerEntity_CommonObjectReference) |  |  |
| port |  |  | Long | The port and protocol of the destination of the given connection. | int64 |
| protocol |  |  | [StorageL4Protocol](#StorageL4Protocol_CommonObjectReference) |  | L4_PROTOCOL_UNKNOWN, L4_PROTOCOL_TCP, L4_PROTOCOL_UDP, L4_PROTOCOL_ICMP, L4_PROTOCOL_RAW, L4_PROTOCOL_SCTP, L4_PROTOCOL_ANY, |
| ingress |  |  | Boolean | A boolean representing whether the query is for an ingress or egress connection. This is defined with respect to the current deployment. Thus: - If the connection in question is in the outEdges of the current deployment, this should be false. - If it is in the outEdges of the peer deployment, this should be true. |  |

<a id="V1NetworkBaselineStatusResponse_CommonObjectReference"></a>

## V1NetworkBaselineStatusResponse

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| statuses |  |  | List of [V1NetworkBaselinePeerStatus](#V1NetworkBaselinePeerStatus_CommonObjectReference) |  |  |

<a id="V1NetworkEdgeProperties_CommonObjectReference"></a>

## V1NetworkEdgeProperties

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| port |  |  | Long |  | int64 |
| protocol |  |  | [StorageL4Protocol](#StorageL4Protocol_CommonObjectReference) |  | L4_PROTOCOL_UNKNOWN, L4_PROTOCOL_TCP, L4_PROTOCOL_UDP, L4_PROTOCOL_ICMP, L4_PROTOCOL_RAW, L4_PROTOCOL_SCTP, L4_PROTOCOL_ANY, |
| lastActiveTimestamp |  |  | Date |  | date-time |

<a id="V1NetworkEdgePropertiesBundle_CommonObjectReference"></a>

## V1NetworkEdgePropertiesBundle

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| properties |  |  | List of [V1NetworkEdgeProperties](#V1NetworkEdgeProperties_CommonObjectReference) |  |  |

<a id="V1NetworkGraph_CommonObjectReference"></a>

## V1NetworkGraph

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| epoch |  |  | Long |  | int64 |
| nodes |  |  | List of [V1NetworkNode](#V1NetworkNode_CommonObjectReference) |  |  |

<a id="V1NetworkGraphDiff_CommonObjectReference"></a>

## V1NetworkGraphDiff

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| DEPRECATEDNodeDiffs |  |  | Map of [V1NetworkNodeDiff](#V1NetworkNodeDiff_CommonObjectReference) |  |  |
| nodeDiffs |  |  | Map of [V1NetworkNodeDiff](#V1NetworkNodeDiff_CommonObjectReference) |  |  |

<a id="V1NetworkGraphEpoch_CommonObjectReference"></a>

## V1NetworkGraphEpoch

| Field Name | Required | Nullable | Type | Description | Format |
|------------|----------|----------|------|-------------|--------|
| epoch      |          |          | Long |             | int64  |

<a id="V1NetworkGraphScope_CommonObjectReference"></a>

## V1NetworkGraphScope

| Field Name | Required | Nullable | Type   | Description | Format |
|------------|----------|----------|--------|-------------|--------|
| query      |          |          | String |             |        |

<a id="V1NetworkNode_CommonObjectReference"></a>

## V1NetworkNode

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| entity |  |  | [StorageNetworkEntityInfo](#StorageNetworkEntityInfo_CommonObjectReference) |  |  |
| internetAccess |  |  | Boolean |  |  |
| policyIds |  |  | List of `string` |  |  |
| nonIsolatedIngress |  |  | Boolean |  |  |
| nonIsolatedEgress |  |  | Boolean |  |  |
| queryMatch |  |  | Boolean |  |  |
| outEdges |  |  | Map of [V1NetworkEdgePropertiesBundle](#V1NetworkEdgePropertiesBundle_CommonObjectReference) |  |  |

<a id="V1NetworkNodeDiff_CommonObjectReference"></a>

## V1NetworkNodeDiff

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| policyIds |  |  | List of `string` |  |  |
| DEPRECATEDOutEdges |  |  | Map of [V1NetworkEdgePropertiesBundle](#V1NetworkEdgePropertiesBundle_CommonObjectReference) |  |  |
| outEdges |  |  | Map of [V1NetworkEdgePropertiesBundle](#V1NetworkEdgePropertiesBundle_CommonObjectReference) |  |  |
| nonIsolatedIngress |  |  | Boolean |  |  |
| nonIsolatedEgress |  |  | Boolean |  |  |

<a id="V1NetworkPoliciesResponse_CommonObjectReference"></a>

## V1NetworkPoliciesResponse

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| networkPolicies |  |  | List of [StorageNetworkPolicy](#StorageNetworkPolicy_CommonObjectReference) |  |  |

<a id="V1NetworkPolicyInSimulation_CommonObjectReference"></a>

## V1NetworkPolicyInSimulation

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| policy |  |  | [StorageNetworkPolicy](#StorageNetworkPolicy_CommonObjectReference) |  |  |
| status |  |  | [V1NetworkPolicyInSimulationStatus](#V1NetworkPolicyInSimulationStatus_CommonObjectReference) |  | INVALID, UNCHANGED, MODIFIED, ADDED, DELETED, |
| oldPolicy |  |  | [StorageNetworkPolicy](#StorageNetworkPolicy_CommonObjectReference) |  |  |

<a id="V1NetworkPolicyInSimulationStatus_CommonObjectReference"></a>

## V1NetworkPolicyInSimulationStatus

| Enum Values |
|-------------|
| INVALID     |
| UNCHANGED   |
| MODIFIED    |
| ADDED       |
| DELETED     |

<a id="V1OCMConfig_CommonObjectReference"></a>

## V1OCMConfig

OCMConfig provides information required to fetch discovered clusters from the OpenShift cluster manager.

| Field Name | Required | Nullable | Type   | Description | Format |
|------------|----------|----------|--------|-------------|--------|
| endpoint   |          |          | String |             |        |

<a id="V1Pagination_CommonObjectReference"></a>

## V1Pagination

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| limit |  |  | Integer |  | int32 |
| offset |  |  | Integer |  | int32 |
| sortOption |  |  | [V1SortOption](#V1SortOption_CommonObjectReference) |  |  |
| sortOptions |  |  | List of [V1SortOption](#V1SortOption_CommonObjectReference) | This field is under development. It is not supported on any REST APIs. |  |

<a id="V1PaladinCloudConfig_CommonObjectReference"></a>

## V1PaladinCloudConfig

PaladinCloudConfig provides information required to fetch discovered clusters from Paladin Cloud.

| Field Name | Required | Nullable | Type   | Description | Format |
|------------|----------|----------|--------|-------------|--------|
| endpoint   |          |          | String |             |        |

<a id="V1PodsResponse_CommonObjectReference"></a>

## V1PodsResponse

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| pods |  |  | List of [StoragePod](#StoragePod_CommonObjectReference) |  |  |

<a id="V1PolicyCategoriesResponse_CommonObjectReference"></a>

## V1PolicyCategoriesResponse

| Field Name | Required | Nullable | Type             | Description | Format |
|------------|----------|----------|------------------|-------------|--------|
| categories |          |          | List of `string` |             |        |

<a id="V1PolicyCategory_CommonObjectReference"></a>

## V1PolicyCategory

| Field Name | Required | Nullable | Type    | Description | Format |
|------------|----------|----------|---------|-------------|--------|
| id         |          |          | String  |             |        |
| name       |          |          | String  |             |        |
| isDefault  |          |          | Boolean |             |        |

<a id="V1PolicyFromSearchRequest_CommonObjectReference"></a>

## V1PolicyFromSearchRequest

| Field Name   | Required | Nullable | Type   | Description | Format |
|--------------|----------|----------|--------|-------------|--------|
| searchParams |          |          | String |             |        |

<a id="V1PolicyFromSearchResponse_CommonObjectReference"></a>

## V1PolicyFromSearchResponse

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| policy |  |  | [StoragePolicy](#StoragePolicy_CommonObjectReference) |  |  |
| alteredSearchTerms |  |  | List of `string` |  |  |
| hasNestedFields |  |  | Boolean |  |  |

<a id="V1PongMessage_CommonObjectReference"></a>

## V1PongMessage

| Field Name | Required | Nullable | Type   | Description | Format |
|------------|----------|----------|--------|-------------|--------|
| status     |          |          | String |             |        |

<a id="V1PostReportConfigurationRequest_CommonObjectReference"></a>

## V1PostReportConfigurationRequest

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| reportConfig |  |  | [StorageReportConfiguration](#StorageReportConfiguration_CommonObjectReference) |  |  |

<a id="V1PostReportConfigurationResponse_CommonObjectReference"></a>

## V1PostReportConfigurationResponse

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| reportConfig |  |  | [StorageReportConfiguration](#StorageReportConfiguration_CommonObjectReference) |  |  |

<a id="V1Preferences_CommonObjectReference"></a>

## V1Preferences

| Field Name              | Required | Nullable | Type   | Description | Format |
|-------------------------|----------|----------|--------|-------------|--------|
| maxGrpcReceiveSizeBytes |          |          | String |             | uint64 |

<a id="V1ProbeUploadManifestFile_CommonObjectReference"></a>

## V1ProbeUploadManifestFile

| Field Name | Required | Nullable | Type   | Description | Format |
|------------|----------|----------|--------|-------------|--------|
| name       |          |          | String |             |        |
| size       |          |          | String |             | int64  |
| crc32      |          |          | Long   |             | int64  |

<a id="V1ProcessBaselineUpdateError_CommonObjectReference"></a>

## V1ProcessBaselineUpdateError

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| error |  |  | String |  |  |
| key |  |  | [StorageProcessBaselineKey](#StorageProcessBaselineKey_CommonObjectReference) |  |  |

<a id="V1ProcessGroup_CommonObjectReference"></a>

## V1ProcessGroup

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| args |  |  | String |  |  |
| signals |  |  | List of [StorageProcessIndicator](#StorageProcessIndicator_CommonObjectReference) |  |  |

<a id="V1ProcessNameAndContainerNameGroup_CommonObjectReference"></a>

## V1ProcessNameAndContainerNameGroup

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| name |  |  | String |  |  |
| containerName |  |  | String |  |  |
| timesExecuted |  |  | Long |  | int64 |
| groups |  |  | List of [V1ProcessGroup](#V1ProcessGroup_CommonObjectReference) |  |  |
| suspicious |  |  | Boolean |  |  |

<a id="V1ProcessNameGroup_CommonObjectReference"></a>

## V1ProcessNameGroup

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| name |  |  | String |  |  |
| timesExecuted |  |  | Long |  | int64 |
| groups |  |  | List of [V1ProcessGroup](#V1ProcessGroup_CommonObjectReference) |  |  |

<a id="V1PutConfigRequest_CommonObjectReference"></a>

## V1PutConfigRequest

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| config |  |  | [StorageConfig](#StorageConfig_CommonObjectReference) |  |  |

<a id="V1PutNetworkGraphConfigRequest_CommonObjectReference"></a>

## V1PutNetworkGraphConfigRequest

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| config |  |  | [StorageNetworkGraphConfig](#StorageNetworkGraphConfig_CommonObjectReference) |  |  |

<a id="V1PutPlatformComponentConfigRequest_CommonObjectReference"></a>

## V1PutPlatformComponentConfigRequest

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| rules |  |  | List of [PlatformComponentConfigRule](#PlatformComponentConfigRule_CommonObjectReference) |  |  |

<a id="V1RawQuery_CommonObjectReference"></a>

## V1RawQuery

RawQuery represents the search query string. The format of the query string is "\<field name\>:\<value,value,…​\>\<field name\>:\<value, value,...\>…​" For example: To search for deployments named "central" and "sensor" in the namespace "stackrox", the query string would be "Deployment:central,sensor+Namespace:stackrox" RawQuery is used in ListAPIs to search for a particular object.

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| query |  |  | String |  |  |
| pagination |  |  | [V1Pagination](#V1Pagination_CommonObjectReference) |  |  |

<a id="V1RenamePolicyCategoryRequest_CommonObjectReference"></a>

## V1RenamePolicyCategoryRequest

| Field Name      | Required | Nullable | Type   | Description | Format |
|-----------------|----------|----------|--------|-------------|--------|
| id              |          |          | String |             |        |
| newCategoryName |          |          | String |             |        |

<a id="V1ResolveAlertsRequest_CommonObjectReference"></a>

## V1ResolveAlertsRequest

| Field Name | Required | Nullable | Type   | Description | Format |
|------------|----------|----------|--------|-------------|--------|
| query      |          |          | String |             |        |

<a id="V1SADeploymentRelationship_CommonObjectReference"></a>

## V1SADeploymentRelationship

Service accounts can be used by a deployment. Next Tag: 3

| Field Name | Required | Nullable | Type   | Description             | Format |
|------------|----------|----------|--------|-------------------------|--------|
| id         |          |          | String |                         |        |
| name       |          |          | String | Name of the deployment. |        |

<a id="V1ScanImageRequest_CommonObjectReference"></a>

## V1ScanImageRequest

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| imageName |  |  | String |  |  |
| force |  |  | Boolean |  |  |
| includeSnoozed |  |  | Boolean |  |  |
| cluster |  |  | String | Cluster to delegate scan to, may be the cluster’s name or ID. |  |
| namespace |  |  | String | Namespace on the secured cluster from which to read context information when delegating image scans, specifically pull secrets to access the image registry. |  |

<a id="V1ScopeObject_CommonObjectReference"></a>

## V1ScopeObject

ScopeObject represents an ID, name pair, which can apply to any entity that takes part in an access scope (so far Cluster and Namespace).

| Field Name | Required | Nullable | Type   | Description | Format |
|------------|----------|----------|--------|-------------|--------|
| id         |          |          | String |             |        |
| name       |          |          | String |             |        |

<a id="V1ScopedRoles_CommonObjectReference"></a>

## V1ScopedRoles

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| namespace |  |  | String |  |  |
| roles |  |  | List of [StorageK8sRole](#StorageK8sRole_CommonObjectReference) |  |  |

<a id="V1SearchCategory_CommonObjectReference"></a>

## V1SearchCategory

Next available tag: 85

| Enum Values                        |
|------------------------------------|
| SEARCH_UNSET                       |
| ALERTS                             |
| IMAGES                             |
| IMAGE_COMPONENTS                   |
| IMAGE_VULN_EDGE                    |
| IMAGE_COMPONENT_EDGE               |
| POLICIES                           |
| DEPLOYMENTS                        |
| PODS                               |
| SECRETS                            |
| PROCESS_INDICATORS                 |
| COMPLIANCE                         |
| CLUSTERS                           |
| NAMESPACES                         |
| NODES                              |
| NODE_COMPONENTS                    |
| NODE_VULN_EDGE                     |
| NODE_COMPONENT_EDGE                |
| NODE_COMPONENT_CVE_EDGE            |
| COMPLIANCE_STANDARD                |
| COMPLIANCE_CONTROL_GROUP           |
| COMPLIANCE_CONTROL                 |
| SERVICE_ACCOUNTS                   |
| ROLES                              |
| ROLEBINDINGS                       |
| REPORT_CONFIGURATIONS              |
| PROCESS_BASELINES                  |
| SUBJECTS                           |
| RISKS                              |
| VULNERABILITIES                    |
| CLUSTER_VULNERABILITIES            |
| IMAGE_VULNERABILITIES              |
| NODE_VULNERABILITIES               |
| COMPONENT_VULN_EDGE                |
| CLUSTER_VULN_EDGE                  |
| NETWORK_ENTITY                     |
| VULN_REQUEST                       |
| NETWORK_BASELINE                   |
| NETWORK_POLICIES                   |
| PROCESS_BASELINE_RESULTS           |
| COMPLIANCE_METADATA                |
| COMPLIANCE_RESULTS                 |
| COMPLIANCE_DOMAIN                  |
| CLUSTER_HEALTH                     |
| POLICY_CATEGORIES                  |
| IMAGE_INTEGRATIONS                 |
| COLLECTIONS                        |
| POLICY_CATEGORY_EDGE               |
| PROCESS_LISTENING_ON_PORT          |
| API_TOKEN                          |
| REPORT_METADATA                    |
| REPORT_SNAPSHOT                    |
| COMPLIANCE_INTEGRATIONS            |
| COMPLIANCE_SCAN_CONFIG             |
| COMPLIANCE_SCAN                    |
| COMPLIANCE_CHECK_RESULTS           |
| BLOB                               |
| ADMINISTRATION_EVENTS              |
| COMPLIANCE_SCAN_CONFIG_STATUS      |
| ADMINISTRATION_USAGE               |
| COMPLIANCE_PROFILES                |
| COMPLIANCE_RULES                   |
| COMPLIANCE_SCAN_SETTING_BINDINGS   |
| COMPLIANCE_SUITES                  |
| CLOUD_SOURCES                      |
| DISCOVERED_CLUSTERS                |
| COMPLIANCE_REMEDIATIONS            |
| COMPLIANCE_BENCHMARKS              |
| AUTH_PROVIDERS                     |
| COMPLIANCE_REPORT_SNAPSHOT         |
| IMAGE_COMPONENTS_V2                |
| IMAGE_VULNERABILITIES_V2           |
| IMAGES_V2                          |
| VIRTUAL_MACHINES                   |
| BASE_IMAGES                        |
| BASE_IMAGE_LAYERS                  |
| VIRTUAL_MACHINES_V2                |
| VIRTUAL_MACHINE_SCANS_V2           |
| VIRTUAL_MACHINE_COMPONENTS_V2      |
| VIRTUAL_MACHINE_VULNERABILITIES_V2 |
| IMAGE_CVE_INFOS                    |

<a id="V1SearchOptionsResponse_CommonObjectReference"></a>

## V1SearchOptionsResponse

| Field Name | Required | Nullable | Type             | Description | Format |
|------------|----------|----------|------------------|-------------|--------|
| options    |          |          | List of `string` |             |        |

<a id="V1SearchResponse_CommonObjectReference"></a>

## V1SearchResponse

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| results |  |  | List of [V1SearchResult](#V1SearchResult_CommonObjectReference) |  |  |
| counts |  |  | List of [SearchResponseCount](#SearchResponseCount_CommonObjectReference) |  |  |

<a id="V1SearchResult_CommonObjectReference"></a>

## V1SearchResult

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| id |  |  | String |  |  |
| name |  |  | String |  |  |
| category |  |  | [V1SearchCategory](#V1SearchCategory_CommonObjectReference) |  | SEARCH_UNSET, ALERTS, IMAGES, IMAGE_COMPONENTS, IMAGE_VULN_EDGE, IMAGE_COMPONENT_EDGE, POLICIES, DEPLOYMENTS, PODS, SECRETS, PROCESS_INDICATORS, COMPLIANCE, CLUSTERS, NAMESPACES, NODES, NODE_COMPONENTS, NODE_VULN_EDGE, NODE_COMPONENT_EDGE, NODE_COMPONENT_CVE_EDGE, COMPLIANCE_STANDARD, COMPLIANCE_CONTROL_GROUP, COMPLIANCE_CONTROL, SERVICE_ACCOUNTS, ROLES, ROLEBINDINGS, REPORT_CONFIGURATIONS, PROCESS_BASELINES, SUBJECTS, RISKS, VULNERABILITIES, CLUSTER_VULNERABILITIES, IMAGE_VULNERABILITIES, NODE_VULNERABILITIES, COMPONENT_VULN_EDGE, CLUSTER_VULN_EDGE, NETWORK_ENTITY, VULN_REQUEST, NETWORK_BASELINE, NETWORK_POLICIES, PROCESS_BASELINE_RESULTS, COMPLIANCE_METADATA, COMPLIANCE_RESULTS, COMPLIANCE_DOMAIN, CLUSTER_HEALTH, POLICY_CATEGORIES, IMAGE_INTEGRATIONS, COLLECTIONS, POLICY_CATEGORY_EDGE, PROCESS_LISTENING_ON_PORT, API_TOKEN, REPORT_METADATA, REPORT_SNAPSHOT, COMPLIANCE_INTEGRATIONS, COMPLIANCE_SCAN_CONFIG, COMPLIANCE_SCAN, COMPLIANCE_CHECK_RESULTS, BLOB, ADMINISTRATION_EVENTS, COMPLIANCE_SCAN_CONFIG_STATUS, ADMINISTRATION_USAGE, COMPLIANCE_PROFILES, COMPLIANCE_RULES, COMPLIANCE_SCAN_SETTING_BINDINGS, COMPLIANCE_SUITES, CLOUD_SOURCES, DISCOVERED_CLUSTERS, COMPLIANCE_REMEDIATIONS, COMPLIANCE_BENCHMARKS, AUTH_PROVIDERS, COMPLIANCE_REPORT_SNAPSHOT, IMAGE_COMPONENTS_V2, IMAGE_VULNERABILITIES_V2, IMAGES_V2, VIRTUAL_MACHINES, BASE_IMAGES, BASE_IMAGE_LAYERS, VIRTUAL_MACHINES_V2, VIRTUAL_MACHINE_SCANS_V2, VIRTUAL_MACHINE_COMPONENTS_V2, VIRTUAL_MACHINE_VULNERABILITIES_V2, IMAGE_CVE_INFOS, |
| fieldToMatches |  |  | Map of [SearchResultMatches](#SearchResultMatches_CommonObjectReference) |  |  |
| score |  |  | Double |  | double |
| location |  |  | String | Location is intended to be a unique, yet human readable, identifier for the result. For example, for a deployment, the location will be "\$cluster_name/\$namespace/\$deployment_name. It is displayed in the UI in the global search results, underneath the name for each result. |  |

<a id="V1SecuredUnitsUsageResponse_CommonObjectReference"></a>

## V1SecuredUnitsUsageResponse

SecuredUnitsUsageResponse holds the values of the currently observable administration usage metrics.

| Field Name  | Required | Nullable | Type   | Description | Format |
|-------------|----------|----------|--------|-------------|--------|
| numNodes    |          |          | String |             | int64  |
| numCpuUnits |          |          | String |             | int64  |

<a id="V1ServiceAccountAndRoles_CommonObjectReference"></a>

## V1ServiceAccountAndRoles

A service account and the roles that reference it Next Tag: 5

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| serviceAccount |  |  | [StorageServiceAccount](#StorageServiceAccount_CommonObjectReference) |  |  |
| clusterRoles |  |  | List of [StorageK8sRole](#StorageK8sRole_CommonObjectReference) |  |  |
| scopedRoles |  |  | List of [V1ScopedRoles](#V1ScopedRoles_CommonObjectReference) |  |  |
| deploymentRelationships |  |  | List of [V1SADeploymentRelationship](#V1SADeploymentRelationship_CommonObjectReference) |  |  |

<a id="V1ServiceIdentityResponse_CommonObjectReference"></a>

## V1ServiceIdentityResponse

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| identities |  |  | List of [StorageServiceIdentity](#StorageServiceIdentity_CommonObjectReference) |  |  |

<a id="V1SimulateNetworkGraphResponse_CommonObjectReference"></a>

## V1SimulateNetworkGraphResponse

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| simulatedGraph |  |  | [V1NetworkGraph](#V1NetworkGraph_CommonObjectReference) |  |  |
| policies |  |  | List of [V1NetworkPolicyInSimulation](#V1NetworkPolicyInSimulation_CommonObjectReference) |  |  |
| added |  |  | [V1NetworkGraphDiff](#V1NetworkGraphDiff_CommonObjectReference) |  |  |
| removed |  |  | [V1NetworkGraphDiff](#V1NetworkGraphDiff_CommonObjectReference) |  |  |

<a id="V1SortOption_CommonObjectReference"></a>

## V1SortOption

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| field |  |  | String |  |  |
| reversed |  |  | Boolean |  |  |
| aggregateBy |  |  | [V1AggregateBy](#V1AggregateBy_CommonObjectReference) |  |  |

<a id="V1SubjectAndRoles_CommonObjectReference"></a>

## V1SubjectAndRoles

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| subject |  |  | [StorageSubject](#StorageSubject_CommonObjectReference) |  |  |
| roles |  |  | List of [StorageK8sRole](#StorageK8sRole_CommonObjectReference) |  |  |

<a id="V1SuppressCVERequest_CommonObjectReference"></a>

## V1SuppressCVERequest

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| cves |  |  | List of `string` | These are (NVD) vulnerability identifiers, `cve` field of `storage.CVE`, and **not** the `id` field. For example, CVE-2021-44832. |  |
| duration |  |  | String | In JSON format, the Duration type is encoded as a string rather than an object, where the string ends in the suffix "s" (indicating seconds) and is preceded by the number of seconds, with nanoseconds expressed as fractional seconds. For example, 3 seconds with 0 nanoseconds should be encoded in JSON format as "3s", while 3 seconds and 1 nanosecond should be expressed in JSON format as "3.000000001s", and 3 seconds and 1 microsecond should be expressed in JSON format as "3.000001s". |  |

<a id="V1TLSChallengeResponse_CommonObjectReference"></a>

## V1TLSChallengeResponse

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| trustInfoSerialized |  |  | byte\[\] |  | byte |
| signature |  |  | byte\[\] |  | byte |
| signatureSecondaryCa |  |  | byte\[\] | optional signature by key from TrustInfo.secondary_cert_chain\[0\]. | byte |

<a id="V1TestCloudSourceRequest_CommonObjectReference"></a>

## V1TestCloudSourceRequest

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| cloudSource |  |  | [V1CloudSource](#V1CloudSource_CommonObjectReference) |  |  |
| updateCredentials |  |  | Boolean | If true, cloud_source must include valid credentials. If false, the resource must already exist and credentials in cloud_source are ignored. |  |

<a id="V1Traits_CommonObjectReference"></a>

## V1Traits

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| mutabilityMode |  |  | [V1TraitsMutabilityMode](#V1TraitsMutabilityMode_CommonObjectReference) |  | ALLOW_MUTATE, ALLOW_MUTATE_FORCED, |
| visibility |  |  | [V1TraitsVisibility](#V1TraitsVisibility_CommonObjectReference) |  | VISIBLE, HIDDEN, |
| origin |  |  | [V1TraitsOrigin](#V1TraitsOrigin_CommonObjectReference) |  | IMPERATIVE, DEFAULT, DECLARATIVE, DECLARATIVE_ORPHANED, |

<a id="V1TraitsMutabilityMode_CommonObjectReference"></a>

## V1TraitsMutabilityMode

EXPERIMENTAL. NOTE: Please refer from using MutabilityMode for the time being. It will be replaced in the future (ROX-14276). MutabilityMode specifies whether and how an object can be modified. Default is ALLOW_MUTATE and means there are no modification restrictions; this is equivalent to the absence of MutabilityMode specification. ALLOW_MUTATE_FORCED forbids all modifying operations except object removal with force bit on.

Be careful when changing the state of this field. For example, modifying an object from ALLOW_MUTATE to ALLOW_MUTATE_FORCED is allowed but will prohibit any further changes to it, including modifying it back to ALLOW_MUTATE.

| Enum Values         |
|---------------------|
| ALLOW_MUTATE        |
| ALLOW_MUTATE_FORCED |

<a id="V1TraitsOrigin_CommonObjectReference"></a>

## V1TraitsOrigin

Origin specifies the origin of an object. Objects can have four different origins: - IMPERATIVE: the object was created via the API. This is assumed by default. - DEFAULT: the object is a default object, such as default roles, access scopes etc. - DECLARATIVE: the object is created via declarative configuration. - DECLARATIVE_ORPHANED: the object is created via declarative configuration and then unsuccessfully deleted(for example, because it is referenced by another object) Based on the origin, different rules apply to the objects. Objects with the DECLARATIVE origin are not allowed to be modified via API, only via declarative configuration. Additionally, they may not reference objects with the IMPERATIVE origin. Objects with the DEFAULT origin are not allowed to be modified via either API or declarative configuration. They may be referenced by all other objects. Objects with the IMPERATIVE origin are allowed to be modified via API, not via declarative configuration. They may reference all other objects. Objects with the DECLARATIVE_ORPHANED origin are not allowed to be modified via either API or declarative configuration. DECLARATIVE_ORPHANED resource can become DECLARATIVE again if it is redefined in declarative configuration. Objects with this origin will be cleaned up from the system immediately after they are not referenced by other resources anymore. They may be referenced by all other objects.

| Enum Values          |
|----------------------|
| IMPERATIVE           |
| DEFAULT              |
| DECLARATIVE          |
| DECLARATIVE_ORPHANED |

<a id="V1TraitsVisibility_CommonObjectReference"></a>

## V1TraitsVisibility

EXPERIMENTAL. visibility allows to specify whether the object should be visible for certain APIs.

| Enum Values |
|-------------|
| VISIBLE     |
| HIDDEN      |

<a id="V1TriggerComplianceRunsRequest_CommonObjectReference"></a>

## V1TriggerComplianceRunsRequest

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| selection |  |  | [V1ComplianceRunSelection](#V1ComplianceRunSelection_CommonObjectReference) |  |  |

<a id="V1TriggerComplianceRunsResponse_CommonObjectReference"></a>

## V1TriggerComplianceRunsResponse

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| startedRuns |  |  | List of [V1ComplianceRun](#V1ComplianceRun_CommonObjectReference) |  |  |

<a id="V1Type_CommonObjectReference"></a>

## V1Type

| Enum Values |
|-------------|
| CREATED     |
| REMOVED     |

<a id="V1UnsuppressCVERequest_CommonObjectReference"></a>

## V1UnsuppressCVERequest

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| cves |  |  | List of `string` | These are (NVD) vulnerability identifiers, `cve` field of `storage.CVE`, and **not** the `id` field. For example, CVE-2021-44832. |  |

<a id="V1UpdateCollectionResponse_CommonObjectReference"></a>

## V1UpdateCollectionResponse

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| collection |  |  | [StorageResourceCollection](#StorageResourceCollection_CommonObjectReference) |  |  |

<a id="V1UpdateExternalBackupRequest_CommonObjectReference"></a>

## V1UpdateExternalBackupRequest

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| externalBackup |  |  | [StorageExternalBackup](#StorageExternalBackup_CommonObjectReference) |  |  |
| updatePassword |  |  | Boolean | When false, use the stored credentials of an existing external backup configuration given its ID. |  |

<a id="V1UpdateImageIntegrationRequest_CommonObjectReference"></a>

## V1UpdateImageIntegrationRequest

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| config |  |  | [StorageImageIntegration](#StorageImageIntegration_CommonObjectReference) |  |  |
| updatePassword |  |  | Boolean | When false, use the stored credentials of an existing image integration given its ID. |  |

<a id="V1UpdateNotifierRequest_CommonObjectReference"></a>

## V1UpdateNotifierRequest

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| notifier |  |  | [StorageNotifier](#StorageNotifier_CommonObjectReference) |  |  |
| updatePassword |  |  | Boolean | When false, use the stored credentials of an existing notifier configuration given its ID. |  |

<a id="V1UpdateProcessBaselinesRequest_CommonObjectReference"></a>

## V1UpdateProcessBaselinesRequest

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| keys |  |  | List of [StorageProcessBaselineKey](#StorageProcessBaselineKey_CommonObjectReference) |  |  |
| addElements |  |  | List of [StorageBaselineItem](#StorageBaselineItem_CommonObjectReference) |  |  |
| removeElements |  |  | List of [StorageBaselineItem](#StorageBaselineItem_CommonObjectReference) |  |  |

<a id="V1UpdateProcessBaselinesResponse_CommonObjectReference"></a>

## V1UpdateProcessBaselinesResponse

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| baselines |  |  | List of [StorageProcessBaseline](#StorageProcessBaseline_CommonObjectReference) |  |  |
| errors |  |  | List of [V1ProcessBaselineUpdateError](#V1ProcessBaselineUpdateError_CommonObjectReference) |  |  |

<a id="V1UpdateSensorUpgradeConfigRequest_CommonObjectReference"></a>

## V1UpdateSensorUpgradeConfigRequest

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| config |  |  | [StorageSensorUpgradeConfig](#StorageSensorUpgradeConfig_CommonObjectReference) |  |  |

<a id="V1UpdateVulnerabilityExceptionConfigRequest_CommonObjectReference"></a>

## V1UpdateVulnerabilityExceptionConfigRequest

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| config |  |  | [V1VulnerabilityExceptionConfig](#V1VulnerabilityExceptionConfig_CommonObjectReference) |  |  |

<a id="V1UpdateVulnerabilityExceptionConfigResponse_CommonObjectReference"></a>

## V1UpdateVulnerabilityExceptionConfigResponse

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| config |  |  | [V1VulnerabilityExceptionConfig](#V1VulnerabilityExceptionConfig_CommonObjectReference) |  |  |

<a id="V1UserAttribute_CommonObjectReference"></a>

## V1UserAttribute

| Field Name | Required | Nullable | Type             | Description | Format |
|------------|----------|----------|------------------|-------------|--------|
| key        |          |          | String           |             |        |
| values     |          |          | List of `string` |             |        |

<a id="V1UserAttributeTuple_CommonObjectReference"></a>

## V1UserAttributeTuple

UserAttributeTuple descript the auth:key:value tuple that decides group membership. Next Tag: 4

| Field Name     | Required | Nullable | Type   | Description | Format |
|----------------|----------|----------|--------|-------------|--------|
| authProviderId |          |          | String |             |        |
| key            |          |          | String |             |        |
| value          |          |          | String |             |        |

<a id="V1VulnDefinitionsInfo_CommonObjectReference"></a>

## V1VulnDefinitionsInfo

| Field Name           | Required | Nullable | Type | Description | Format    |
|----------------------|----------|----------|------|-------------|-----------|
| lastUpdatedTimestamp |          |          | Date |             | date-time |

<a id="V1VulnDefinitionsInfoRequestComponent_CommonObjectReference"></a>

## V1VulnDefinitionsInfoRequestComponent

| Enum Values |
|-------------|
| SCANNER     |
| SCANNER_V4  |

<a id="V1VulnMgmtExportWorkloadsResponse_CommonObjectReference"></a>

## V1VulnMgmtExportWorkloadsResponse

The workloads response contains the full image details including the vulnerability data.

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| deployment |  |  | [StorageDeployment](#StorageDeployment_CommonObjectReference) |  |  |
| images |  |  | List of [StorageImage](#StorageImage_CommonObjectReference) |  |  |
| livePods |  |  | Integer |  | int32 |

<a id="V1VulnerabilityExceptionConfig_CommonObjectReference"></a>

## V1VulnerabilityExceptionConfig

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| expiryOptions |  |  | [V1VulnerabilityExceptionConfigExpiryOptions](#V1VulnerabilityExceptionConfigExpiryOptions_CommonObjectReference) |  |  |

<a id="V1VulnerabilityExceptionConfigExpiryOptions_CommonObjectReference"></a>

## V1VulnerabilityExceptionConfigExpiryOptions

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| dayOptions |  |  | List of [V1DayOption](#V1DayOption_CommonObjectReference) | This allows users to set expiry interval based on number of days. |  |
| fixableCveOptions |  |  | [V1VulnerabilityExceptionConfigFixableCVEOptions](#V1VulnerabilityExceptionConfigFixableCVEOptions_CommonObjectReference) |  |  |
| customDate |  |  | Boolean | This option, if true, allows UI to show a custom date picker for setting expiry date. |  |
| indefinite |  |  | Boolean |  |  |

<a id="V1VulnerabilityExceptionConfigFixableCVEOptions_CommonObjectReference"></a>

## V1VulnerabilityExceptionConfigFixableCVEOptions

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| allFixable |  |  | Boolean | This options allows users to expire the vulnerability deferral request if and only if **all** vulnerabilities in the requests become fixable. |  |
| anyFixable |  |  | Boolean | This options allows users to expire the vulnerability deferral request if **any** vulnerability in the requests become fixable. |  |

<a id="V1WatchImageRequest_CommonObjectReference"></a>

## V1WatchImageRequest

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| name |  |  | String | The name of the image. This must be fully qualified, including a tag, but must NOT include a SHA. |  |

<a id="V1WatchImageResponse_CommonObjectReference"></a>

## V1WatchImageResponse

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| normalizedName |  |  | String |  |  |
| errorType |  |  | [WatchImageResponseErrorType](#WatchImageResponseErrorType_CommonObjectReference) |  | NO_ERROR, INVALID_IMAGE_NAME, NO_VALID_INTEGRATION, SCAN_FAILED, |
| errorMessage |  |  | String | Only set if error_type is NOT equal to "NO_ERROR". |  |

<a id="V2Advisory_CommonObjectReference"></a>

## V2Advisory

| Field Name | Required | Nullable | Type   | Description | Format |
|------------|----------|----------|--------|-------------|--------|
| name       |          |          | String |             |        |
| link       |          |          | String |             |        |

<a id="V2AgentStatus_CommonObjectReference"></a>

## V2AgentStatus

Agent status enriched from a separate data source (not on VirtualMachineV2 storage).

| Enum Values          |
|----------------------|
| AGENT_STATUS_UNKNOWN |
| AGENT_STATUS_ACTIVE  |

<a id="V2AggregateBy_CommonObjectReference"></a>

## V2AggregateBy

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| aggrFunc |  |  | [V2Aggregation](#V2Aggregation_CommonObjectReference) |  | UNSET, COUNT, MIN, MAX, |
| distinct |  |  | Boolean |  |  |

<a id="V2Aggregation_CommonObjectReference"></a>

## V2Aggregation

| Enum Values |
|-------------|
| UNSET       |
| COUNT       |
| MIN         |
| MAX         |

<a id="V2ApproveVulnerabilityExceptionResponse_CommonObjectReference"></a>

## V2ApproveVulnerabilityExceptionResponse

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| exception |  |  | [V2VulnerabilityException](#V2VulnerabilityException_CommonObjectReference) |  |  |

<a id="V2BaseComplianceScanConfigurationSettings_CommonObjectReference"></a>

## V2BaseComplianceScanConfigurationSettings

Next available tag: 5

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| oneTimeScan |  |  | Boolean |  |  |
| profiles |  |  | List of `string` |  |  |
| scanSchedule |  |  | [V2Schedule](#V2Schedule_CommonObjectReference) |  |  |
| description |  |  | String |  |  |
| notifiers |  |  | List of [V2NotifierConfiguration](#V2NotifierConfiguration_CommonObjectReference) |  |  |

<a id="V2BaseImageReference_CommonObjectReference"></a>

## V2BaseImageReference

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| id |  |  | String |  |  |
| baseImageRepoPath |  |  | String |  |  |
| baseImageTagPattern |  |  | String |  |  |
| user |  |  | [V2SlimUser](#V2SlimUser_CommonObjectReference) |  |  |

<a id="V2COStatus_CommonObjectReference"></a>

## V2COStatus

Represents the status of compliance operator

| Enum Values |
|-------------|
| HEALTHY     |
| UNHEALTHY   |

<a id="V2CVSSScore_CommonObjectReference"></a>

## V2CVSSScore

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| source |  |  | [V2Source](#V2Source_CommonObjectReference) |  | SOURCE_UNKNOWN, SOURCE_RED_HAT, SOURCE_OSV, SOURCE_NVD, |
| url |  |  | String |  |  |
| cvssv3 |  |  | [V2CVSSV3](#V2CVSSV3_CommonObjectReference) |  |  |

<a id="V2CVSSV3_CommonObjectReference"></a>

## V2CVSSV3

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| vector |  |  | String |  |  |
| exploitabilityScore |  |  | Float |  | float |
| impactScore |  |  | Float |  | float |
| attackVector |  |  | [CVSSV3AttackVector](#CVSSV3AttackVector_CommonObjectReference) |  | ATTACK_LOCAL, ATTACK_ADJACENT, ATTACK_NETWORK, ATTACK_PHYSICAL, |
| attackComplexity |  |  | [CVSSV3Complexity](#CVSSV3Complexity_CommonObjectReference) |  | COMPLEXITY_LOW, COMPLEXITY_HIGH, |
| privilegesRequired |  |  | [CVSSV3Privileges](#CVSSV3Privileges_CommonObjectReference) |  | PRIVILEGE_NONE, PRIVILEGE_LOW, PRIVILEGE_HIGH, |
| userInteraction |  |  | [CVSSV3UserInteraction](#CVSSV3UserInteraction_CommonObjectReference) |  | UI_NONE, UI_REQUIRED, |
| scope |  |  | [V2CVSSV3Scope](#V2CVSSV3Scope_CommonObjectReference) |  | UNCHANGED, CHANGED, |
| confidentiality |  |  | [CVSSV3Impact](#CVSSV3Impact_CommonObjectReference) |  | IMPACT_NONE, IMPACT_LOW, IMPACT_HIGH, |
| integrity |  |  | [CVSSV3Impact](#CVSSV3Impact_CommonObjectReference) |  | IMPACT_NONE, IMPACT_LOW, IMPACT_HIGH, |
| availability |  |  | [CVSSV3Impact](#CVSSV3Impact_CommonObjectReference) |  | IMPACT_NONE, IMPACT_LOW, IMPACT_HIGH, |
| score |  |  | Float |  | float |
| severity |  |  | [CVSSV3Severity](#CVSSV3Severity_CommonObjectReference) |  | UNKNOWN, NONE, LOW, MEDIUM, HIGH, CRITICAL, |

<a id="V2CVSSV3Scope_CommonObjectReference"></a>

## V2CVSSV3Scope

| Enum Values |
|-------------|
| UNCHANGED   |
| CHANGED     |

<a id="V2CancelVulnerabilityExceptionResponse_CommonObjectReference"></a>

## V2CancelVulnerabilityExceptionResponse

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| exception |  |  | [V2VulnerabilityException](#V2VulnerabilityException_CommonObjectReference) |  |  |

<a id="V2ClusterCheckStatus_CommonObjectReference"></a>

## V2ClusterCheckStatus

ClusterCheckStatus groups the result of the check by cluster

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| cluster |  |  | [V2ComplianceScanCluster](#V2ComplianceScanCluster_CommonObjectReference) |  |  |
| status |  |  | [V2ComplianceCheckStatus](#V2ComplianceCheckStatus_CommonObjectReference) |  | UNSET_CHECK_STATUS, PASS, FAIL, ERROR, INFO, MANUAL, NOT_APPLICABLE, INCONSISTENT, |
| createdTime |  |  | Date |  | date-time |
| checkUid |  |  | String |  |  |
| lastScanTime |  |  | Date |  | date-time |

<a id="V2ClusterPlatformType_CommonObjectReference"></a>

## V2ClusterPlatformType

| Enum Values        |
|--------------------|
| GENERIC_CLUSTER    |
| KUBERNETES_CLUSTER |
| OPENSHIFT_CLUSTER  |
| OPENSHIFT4_CLUSTER |

<a id="V2ClusterProviderType_CommonObjectReference"></a>

## V2ClusterProviderType

| Enum Values |
|-------------|
| UNSPECIFIED |
| AKS         |
| ARO         |
| EKS         |
| GKE         |
| OCP         |
| OSD         |
| ROSA        |

<a id="V2ClusterScanStatus_CommonObjectReference"></a>

## V2ClusterScanStatus

ClusterScanStatus holds status based on cluster in the event that a scan configuration was successfully applied to some clusters but not others. Next available tag: 5

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| clusterId |  |  | String |  |  |
| errors |  |  | List of `string` |  |  |
| clusterName |  |  | String |  |  |
| suiteStatus |  |  | [ClusterScanStatusSuiteStatus](#ClusterScanStatusSuiteStatus_CommonObjectReference) |  |  |

<a id="V2CollectionReference_CommonObjectReference"></a>

## V2CollectionReference

| Field Name     | Required | Nullable | Type   | Description | Format |
|----------------|----------|----------|--------|-------------|--------|
| collectionId   |          |          | String |             |        |
| collectionName |          |          | String |             |        |

<a id="V2CollectionSnapshot_CommonObjectReference"></a>

## V2CollectionSnapshot

| Field Name | Required | Nullable | Type   | Description | Format |
|------------|----------|----------|--------|-------------|--------|
| id         |          |          | String |             |        |
| name       |          |          | String |             |        |

<a id="V2Comment_CommonObjectReference"></a>

## V2Comment

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| id |  |  | String |  |  |
| message |  |  | String |  |  |
| user |  |  | [V2SlimUser](#V2SlimUser_CommonObjectReference) |  |  |
| createdAt |  |  | Date |  | date-time |

<a id="V2ComplianceBenchmark_CommonObjectReference"></a>

## V2ComplianceBenchmark

| Field Name  | Required | Nullable | Type   | Description | Format |
|-------------|----------|----------|--------|-------------|--------|
| name        |          |          | String |             |        |
| version     |          |          | String |             |        |
| description |          |          | String |             |        |
| provider    |          |          | String |             |        |
| shortName   |          |          | String |             |        |

<a id="V2ComplianceCheckData_CommonObjectReference"></a>

## V2ComplianceCheckData

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| clusterId |  |  | String |  |  |
| scanName |  |  | String |  |  |
| result |  |  | [V2ComplianceCheckResult](#V2ComplianceCheckResult_CommonObjectReference) |  |  |

<a id="V2ComplianceCheckResult_CommonObjectReference"></a>

## V2ComplianceCheckResult

ComplianceCheckResult details of an instance of a compliance check result

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| checkId |  |  | String |  |  |
| checkName |  |  | String |  |  |
| checkUid |  |  | String |  |  |
| description |  |  | String |  |  |
| instructions |  |  | String |  |  |
| rationale |  |  | String |  |  |
| valuesUsed |  |  | List of `string` |  |  |
| warnings |  |  | List of `string` |  |  |
| status |  |  | [V2ComplianceCheckStatus](#V2ComplianceCheckStatus_CommonObjectReference) |  | UNSET_CHECK_STATUS, PASS, FAIL, ERROR, INFO, MANUAL, NOT_APPLICABLE, INCONSISTENT, |
| ruleName |  |  | String |  |  |
| labels |  |  | Map of `string` |  |  |
| annotations |  |  | Map of `string` |  |  |
| controls |  |  | List of [V2ComplianceControl](#V2ComplianceControl_CommonObjectReference) |  |  |

<a id="V2ComplianceCheckResultStatusCount_CommonObjectReference"></a>

## V2ComplianceCheckResultStatusCount

Group the number of occurrences by status

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| checkName |  |  | String |  |  |
| rationale |  |  | String |  |  |
| ruleName |  |  | String |  |  |
| checkStats |  |  | List of [V2ComplianceCheckStatusCount](#V2ComplianceCheckStatusCount_CommonObjectReference) |  |  |
| controls |  |  | List of [V2ComplianceControl](#V2ComplianceControl_CommonObjectReference) |  |  |

<a id="V2ComplianceCheckStatus_CommonObjectReference"></a>

## V2ComplianceCheckStatus

| Enum Values        |
|--------------------|
| UNSET_CHECK_STATUS |
| PASS               |
| FAIL               |
| ERROR              |
| INFO               |
| MANUAL             |
| NOT_APPLICABLE     |
| INCONSISTENT       |

<a id="V2ComplianceCheckStatusCount_CommonObjectReference"></a>

## V2ComplianceCheckStatusCount

Group the number of occurrences by status

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| count |  |  | Integer |  | int32 |
| status |  |  | [V2ComplianceCheckStatus](#V2ComplianceCheckStatus_CommonObjectReference) |  | UNSET_CHECK_STATUS, PASS, FAIL, ERROR, INFO, MANUAL, NOT_APPLICABLE, INCONSISTENT, |

<a id="V2ComplianceClusterCheckStatus_CommonObjectReference"></a>

## V2ComplianceClusterCheckStatus

ComplianceClusterCheckStatus provides the status of a compliance check result across clusters

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| checkId |  |  | String |  |  |
| checkName |  |  | String |  |  |
| clusters |  |  | List of [V2ClusterCheckStatus](#V2ClusterCheckStatus_CommonObjectReference) |  |  |
| description |  |  | String |  |  |
| instructions |  |  | String |  |  |
| rationale |  |  | String |  |  |
| valuesUsed |  |  | List of `string` |  |  |
| warnings |  |  | List of `string` |  |  |
| labels |  |  | Map of `string` |  |  |
| annotations |  |  | Map of `string` |  |  |
| controls |  |  | List of [V2ComplianceControl](#V2ComplianceControl_CommonObjectReference) |  |  |

<a id="V2ComplianceClusterOverallStats_CommonObjectReference"></a>

## V2ComplianceClusterOverallStats

ComplianceClusterOverallStats provides overall stats for cluster

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| cluster |  |  | [V2ComplianceScanCluster](#V2ComplianceScanCluster_CommonObjectReference) |  |  |
| checkStats |  |  | List of [V2ComplianceCheckStatusCount](#V2ComplianceCheckStatusCount_CommonObjectReference) |  |  |
| clusterErrors |  |  | List of `string` |  |  |
| lastScanTime |  |  | Date |  | date-time |

<a id="V2ComplianceClusterScanStats_CommonObjectReference"></a>

## V2ComplianceClusterScanStats

ComplianceClusterScanStats provides scan stats overview based on cluster

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| scanStats |  |  | [V2ComplianceScanStatsShim](#V2ComplianceScanStatsShim_CommonObjectReference) |  |  |
| cluster |  |  | [V2ComplianceScanCluster](#V2ComplianceScanCluster_CommonObjectReference) |  |  |

<a id="V2ComplianceControl_CommonObjectReference"></a>

## V2ComplianceControl

| Field Name | Required | Nullable | Type   | Description | Format |
|------------|----------|----------|--------|-------------|--------|
| standard   |          |          | String |             |        |
| control    |          |          | String |             |        |

<a id="V2ComplianceIntegration_CommonObjectReference"></a>

## V2ComplianceIntegration

Next Tag: 11

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| id |  |  | String |  |  |
| version |  |  | String |  |  |
| clusterId |  |  | String |  |  |
| clusterName |  |  | String |  |  |
| namespace |  |  | String |  |  |
| statusErrors |  |  | List of `string` | Collection of errors that occurred while trying to obtain compliance operator health info. |  |
| operatorInstalled |  |  | Boolean |  |  |
| status |  |  | [V2COStatus](#V2COStatus_CommonObjectReference) |  | HEALTHY, UNHEALTHY, |
| clusterPlatformType |  |  | [V2ClusterPlatformType](#V2ClusterPlatformType_CommonObjectReference) |  | GENERIC_CLUSTER, KUBERNETES_CLUSTER, OPENSHIFT_CLUSTER, OPENSHIFT4_CLUSTER, |
| clusterProviderType |  |  | [V2ClusterProviderType](#V2ClusterProviderType_CommonObjectReference) |  | UNSPECIFIED, AKS, ARO, EKS, GKE, OCP, OSD, ROSA, |

<a id="V2ComplianceProfile_CommonObjectReference"></a>

## V2ComplianceProfile

Next Tag: 13

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| id |  |  | String |  |  |
| name |  |  | String |  |  |
| profileVersion |  |  | String |  |  |
| productType |  |  | String |  |  |
| description |  |  | String |  |  |
| rules |  |  | List of [V2ComplianceRule](#V2ComplianceRule_CommonObjectReference) |  |  |
| product |  |  | String |  |  |
| title |  |  | String |  |  |
| values |  |  | List of `string` |  |  |
| standards |  |  | List of [V2ComplianceBenchmark](#V2ComplianceBenchmark_CommonObjectReference) |  |  |
| operatorKind |  |  | [V2ComplianceProfileOperatorKind](#V2ComplianceProfileOperatorKind_CommonObjectReference) |  | OPERATOR_KIND_UNSPECIFIED, PROFILE, TAILORED_PROFILE, |

<a id="V2ComplianceProfileOperatorKind_CommonObjectReference"></a>

## V2ComplianceProfileOperatorKind

OperatorKind is the kind of the Compliance Operator resource that this `ComplianceProfile` was sourced from. ACS represents both Compliance Operator `Profiles` and `TailoredProfiles` as compliance profiles.

- OPERATOR_KIND_UNSPECIFIED: The kind is unspecified.

- PROFILE: The kind is `Profile`.

- TAILORED_PROFILE: The kind is `TailoredProfile`.

| Enum Values               |
|---------------------------|
| OPERATOR_KIND_UNSPECIFIED |
| PROFILE                   |
| TAILORED_PROFILE          |

<a id="V2ComplianceProfileScanStats_CommonObjectReference"></a>

## V2ComplianceProfileScanStats

ComplianceProfileScanStats provides scan stats overview based on profile

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| checkStats |  |  | List of [V2ComplianceCheckStatusCount](#V2ComplianceCheckStatusCount_CommonObjectReference) |  |  |
| profileName |  |  | String |  |  |
| title |  |  | String |  |  |
| version |  |  | String |  |  |
| benchmarks |  |  | List of [V2ComplianceBenchmark](#V2ComplianceBenchmark_CommonObjectReference) |  |  |

<a id="V2ComplianceProfileSummary_CommonObjectReference"></a>

## V2ComplianceProfileSummary

Next Tag: 9

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| name |  |  | String |  |  |
| productType |  |  | String |  |  |
| description |  |  | String |  |  |
| title |  |  | String |  |  |
| ruleCount |  |  | Integer |  | int32 |
| profileVersion |  |  | String |  |  |
| standards |  |  | List of [V2ComplianceBenchmark](#V2ComplianceBenchmark_CommonObjectReference) |  |  |
| operatorKind |  |  | [V2ComplianceProfileSummaryOperatorKind](#V2ComplianceProfileSummaryOperatorKind_CommonObjectReference) |  | OPERATOR_KIND_UNSPECIFIED, PROFILE, TAILORED_PROFILE, |

<a id="V2ComplianceProfileSummaryOperatorKind_CommonObjectReference"></a>

## V2ComplianceProfileSummaryOperatorKind

OperatorKind is the kind of the Compliance Operator resource that this `ComplianceProfileSummary` was sourced from. ACS represents both Compliance Operator `Profiles` and `TailoredProfiles` as compliance profiles.

- OPERATOR_KIND_UNSPECIFIED: The kind is unspecified.

- PROFILE: The kind is `Profile`.

- TAILORED_PROFILE: The kind is `TailoredProfile`.

| Enum Values               |
|---------------------------|
| OPERATOR_KIND_UNSPECIFIED |
| PROFILE                   |
| TAILORED_PROFILE          |

<a id="V2ComplianceReportHistoryResponse_CommonObjectReference"></a>

## V2ComplianceReportHistoryResponse

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| complianceReportSnapshots |  |  | List of [V2ComplianceReportSnapshot](#V2ComplianceReportSnapshot_CommonObjectReference) |  |  |

<a id="V2ComplianceReportSnapshot_CommonObjectReference"></a>

## V2ComplianceReportSnapshot

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| reportJobId |  |  | String |  |  |
| scanConfigId |  |  | String |  |  |
| name |  |  | String |  |  |
| description |  |  | String |  |  |
| reportStatus |  |  | [V2ComplianceReportStatus](#V2ComplianceReportStatus_CommonObjectReference) |  |  |
| reportData |  |  | [V2ComplianceScanConfigurationStatus](#V2ComplianceScanConfigurationStatus_CommonObjectReference) |  |  |
| user |  |  | [V2SlimUser](#V2SlimUser_CommonObjectReference) |  |  |
| isDownloadAvailable |  |  | Boolean |  |  |

<a id="V2ComplianceReportStatus_CommonObjectReference"></a>

## V2ComplianceReportStatus

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| runState |  |  | [V2ComplianceReportStatusRunState](#V2ComplianceReportStatusRunState_CommonObjectReference) |  | WAITING, PREPARING, GENERATED, DELIVERED, FAILURE, PARTIAL_ERROR, PARTIAL_SCAN_ERROR_DOWNLOAD, PARTIAL_SCAN_ERROR_EMAIL, |
| startedAt |  |  | Date |  | date-time |
| completedAt |  |  | Date |  | date-time |
| errorMsg |  |  | String |  |  |
| reportRequestType |  |  | [V2ComplianceReportStatusReportMethod](#V2ComplianceReportStatusReportMethod_CommonObjectReference) |  | ON_DEMAND, SCHEDULED, |
| reportNotificationMethod |  |  | [V2NotificationMethod](#V2NotificationMethod_CommonObjectReference) |  | EMAIL, DOWNLOAD, |
| failedClusters |  |  | List of [V2FailedCluster](#V2FailedCluster_CommonObjectReference) |  |  |

<a id="V2ComplianceReportStatusReportMethod_CommonObjectReference"></a>

## V2ComplianceReportStatusReportMethod

| Enum Values |
|-------------|
| ON_DEMAND   |
| SCHEDULED   |

<a id="V2ComplianceReportStatusRunState_CommonObjectReference"></a>

## V2ComplianceReportStatusRunState

| Enum Values                 |
|-----------------------------|
| WAITING                     |
| PREPARING                   |
| GENERATED                   |
| DELIVERED                   |
| FAILURE                     |
| PARTIAL_ERROR               |
| PARTIAL_SCAN_ERROR_DOWNLOAD |
| PARTIAL_SCAN_ERROR_EMAIL    |

<a id="V2ComplianceRule_CommonObjectReference"></a>

## V2ComplianceRule

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| name |  |  | String |  |  |
| ruleType |  |  | String |  |  |
| severity |  |  | String |  |  |
| standard |  |  | String |  |  |
| control |  |  | String |  |  |
| title |  |  | String |  |  |
| description |  |  | String |  |  |
| rationale |  |  | String |  |  |
| fixes |  |  | List of [ComplianceRuleFix](#ComplianceRuleFix_CommonObjectReference) |  |  |
| id |  |  | String |  |  |
| ruleId |  |  | String |  |  |
| parentRule |  |  | String |  |  |
| instructions |  |  | String |  |  |
| warning |  |  | String |  |  |
| operatorKind |  |  | [V2ComplianceRuleOperatorKind](#V2ComplianceRuleOperatorKind_CommonObjectReference) |  | OPERATOR_KIND_UNSPECIFIED, RULE, CUSTOM_RULE, |

<a id="V2ComplianceRuleOperatorKind_CommonObjectReference"></a>

## V2ComplianceRuleOperatorKind

OperatorKind is the kind of the Compliance Operator resource that this `ComplianceRule` was sourced from. ACS represents both Compliance Operator `Rules` and `CustomRules` as compliance rules.

- OPERATOR_KIND_UNSPECIFIED: The kind is unspecified.

- RULE: The kind is `Rule`.

- CUSTOM_RULE: The kind is `CustomRule`.

| Enum Values               |
|---------------------------|
| OPERATOR_KIND_UNSPECIFIED |
| RULE                      |
| CUSTOM_RULE               |

<a id="V2ComplianceRunReportRequest_CommonObjectReference"></a>

## V2ComplianceRunReportRequest

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| scanConfigId |  |  | String |  |  |
| reportNotificationMethod |  |  | [V2NotificationMethod](#V2NotificationMethod_CommonObjectReference) |  | EMAIL, DOWNLOAD, |

<a id="V2ComplianceRunReportResponse_CommonObjectReference"></a>

## V2ComplianceRunReportResponse

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| runState |  |  | [V2ComplianceRunReportResponseRunState](#V2ComplianceRunReportResponseRunState_CommonObjectReference) |  | SUBMITTED, ERROR, |
| submittedAt |  |  | Date |  | date-time |
| errorMsg |  |  | String |  |  |

<a id="V2ComplianceRunReportResponseRunState_CommonObjectReference"></a>

## V2ComplianceRunReportResponseRunState

| Enum Values |
|-------------|
| SUBMITTED   |
| ERROR       |

<a id="V2ComplianceScanCluster_CommonObjectReference"></a>

## V2ComplianceScanCluster

| Field Name  | Required | Nullable | Type   | Description | Format |
|-------------|----------|----------|--------|-------------|--------|
| clusterId   |          |          | String |             |        |
| clusterName |          |          | String |             |        |

<a id="V2ComplianceScanConfiguration_CommonObjectReference"></a>

## V2ComplianceScanConfiguration

Next available tag: 5

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| id |  |  | String |  |  |
| scanName |  |  | String |  |  |
| scanConfig |  |  | [V2BaseComplianceScanConfigurationSettings](#V2BaseComplianceScanConfigurationSettings_CommonObjectReference) |  |  |
| clusters |  |  | List of `string` |  |  |

<a id="V2ComplianceScanConfigurationStatus_CommonObjectReference"></a>

## V2ComplianceScanConfigurationStatus

Next available tag: 9

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| id |  |  | String |  |  |
| scanName |  |  | String |  |  |
| scanConfig |  |  | [V2BaseComplianceScanConfigurationSettings](#V2BaseComplianceScanConfigurationSettings_CommonObjectReference) |  |  |
| clusterStatus |  |  | List of [V2ClusterScanStatus](#V2ClusterScanStatus_CommonObjectReference) |  |  |
| createdTime |  |  | Date |  | date-time |
| lastUpdatedTime |  |  | Date |  | date-time |
| modifiedBy |  |  | [V2SlimUser](#V2SlimUser_CommonObjectReference) |  |  |
| lastExecutedTime |  |  | Date |  | date-time |

<a id="V2ComplianceScanStatsShim_CommonObjectReference"></a>

## V2ComplianceScanStatsShim

ComplianceScanStatsShim models statistics of checks for a given scan configuration

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| scanName |  |  | String |  |  |
| checkStats |  |  | List of [V2ComplianceCheckStatusCount](#V2ComplianceCheckStatusCount_CommonObjectReference) |  |  |
| lastScan |  |  | Date |  | date-time |
| scanConfigId |  |  | String |  |  |

<a id="V2ComponentScanCount_CommonObjectReference"></a>

## V2ComponentScanCount

Scanned vs total component counts (for "15/518 scanned packages" display).

| Field Name | Required | Nullable | Type    | Description | Format |
|------------|----------|----------|---------|-------------|--------|
| scanned    |          |          | Integer |             | int32  |
| total      |          |          | Integer |             | int32  |

<a id="V2CountReportConfigurationsResponse_CommonObjectReference"></a>

## V2CountReportConfigurationsResponse

| Field Name | Required | Nullable | Type    | Description | Format |
|------------|----------|----------|---------|-------------|--------|
| count      |          |          | Integer |             | int32  |

<a id="V2CreateBaseImageReferenceRequest_CommonObjectReference"></a>

## V2CreateBaseImageReferenceRequest

| Field Name          | Required | Nullable | Type   | Description | Format |
|---------------------|----------|----------|--------|-------------|--------|
| baseImageRepoPath   |          |          | String |             |        |
| baseImageTagPattern |          |          | String |             |        |

<a id="V2CreateBaseImageReferenceResponse_CommonObjectReference"></a>

## V2CreateBaseImageReferenceResponse

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| baseImageReference |  |  | [V2BaseImageReference](#V2BaseImageReference_CommonObjectReference) |  |  |

<a id="V2CreateDeferVulnerabilityExceptionRequest_CommonObjectReference"></a>

## V2CreateDeferVulnerabilityExceptionRequest

next available tag: 6

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| cves |  |  | List of `string` | REQUIRED. The CVEs to which the exception should be applied. |  |
| comment |  |  | String | REQUIRED. The rationale for creating the exception. |  |
| scope |  |  | [V2VulnerabilityExceptionScope](#V2VulnerabilityExceptionScope_CommonObjectReference) |  |  |
| exceptionExpiry |  |  | [V2ExceptionExpiry](#V2ExceptionExpiry_CommonObjectReference) |  |  |

<a id="V2CreateDeferVulnerabilityExceptionResponse_CommonObjectReference"></a>

## V2CreateDeferVulnerabilityExceptionResponse

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| exception |  |  | [V2VulnerabilityException](#V2VulnerabilityException_CommonObjectReference) |  |  |

<a id="V2CreateFalsePositiveVulnerabilityExceptionRequest_CommonObjectReference"></a>

## V2CreateFalsePositiveVulnerabilityExceptionRequest

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| cves |  |  | List of `string` | REQUIRED. The CVEs to which the exception should be applied. |  |
| scope |  |  | [V2VulnerabilityExceptionScope](#V2VulnerabilityExceptionScope_CommonObjectReference) |  |  |
| comment |  |  | String | REQUIRED. The rationale for creating the exception. |  |

<a id="V2CreateFalsePositiveVulnerabilityExceptionResponse_CommonObjectReference"></a>

## V2CreateFalsePositiveVulnerabilityExceptionResponse

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| exception |  |  | [V2VulnerabilityException](#V2VulnerabilityException_CommonObjectReference) |  |  |

<a id="V2DeferralRequest_CommonObjectReference"></a>

## V2DeferralRequest

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| expiry |  |  | [V2ExceptionExpiry](#V2ExceptionExpiry_CommonObjectReference) |  |  |

<a id="V2DeferralUpdate_CommonObjectReference"></a>

## V2DeferralUpdate

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| cves |  |  | List of `string` | Use this field to update the CVEs of a deferral exception. |  |
| expiry |  |  | [V2ExceptionExpiry](#V2ExceptionExpiry_CommonObjectReference) |  |  |

<a id="V2DenyVulnerabilityExceptionResponse_CommonObjectReference"></a>

## V2DenyVulnerabilityExceptionResponse

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| exception |  |  | [V2VulnerabilityException](#V2VulnerabilityException_CommonObjectReference) |  |  |

<a id="V2EPSS_CommonObjectReference"></a>

## V2EPSS

EPSS Score stores two epss metrics returned by scanner - epss probability and epss percentile

| Field Name      | Required | Nullable | Type  | Description | Format |
|-----------------|----------|----------|-------|-------------|--------|
| epssProbability |          |          | Float |             | float  |
| epssPercentile  |          |          | Float |             | float  |

<a id="V2EmailNotifierConfiguration_CommonObjectReference"></a>

## V2EmailNotifierConfiguration

| Field Name    | Required | Nullable | Type             | Description | Format |
|---------------|----------|----------|------------------|-------------|--------|
| notifierId    |          |          | String           |             |        |
| mailingLists  |          |          | List of `string` |             |        |
| customSubject |          |          | String           |             |        |
| customBody    |          |          | String           |             |        |

<a id="V2EmbeddedVulnerability_CommonObjectReference"></a>

## V2EmbeddedVulnerability

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| cve |  |  | String |  |  |
| summary |  |  | String |  |  |
| link |  |  | String |  |  |
| publishedOn |  |  | Date |  | date-time |
| lastModified |  |  | Date |  | date-time |
| firstSystemOccurrence |  |  | Date | Time when the CVE was first seen, for this specific distro, in the system. | date-time |
| cvssMetrics |  |  | List of [V2CVSSScore](#V2CVSSScore_CommonObjectReference) |  |  |
| epss |  |  | [V2EPSS](#V2EPSS_CommonObjectReference) |  |  |
| cvss |  |  | Float |  | float |
| fixedBy |  |  | String |  |  |
| severity |  |  | [V2VulnerabilitySeverity](#V2VulnerabilitySeverity_CommonObjectReference) |  | UNKNOWN_VULNERABILITY_SEVERITY, LOW_VULNERABILITY_SEVERITY, MODERATE_VULNERABILITY_SEVERITY, IMPORTANT_VULNERABILITY_SEVERITY, CRITICAL_VULNERABILITY_SEVERITY, |
| advisory |  |  | [V2Advisory](#V2Advisory_CommonObjectReference) |  |  |

<a id="V2EntityScope_CommonObjectReference"></a>

## V2EntityScope

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| rules |  |  | List of [V2EntityScopeRule](#V2EntityScopeRule_CommonObjectReference) |  |  |

<a id="V2EntityScopeRule_CommonObjectReference"></a>

## V2EntityScopeRule

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| entity |  |  | [V2ScopeEntity](#V2ScopeEntity_CommonObjectReference) |  | SCOPE_ENTITY_UNSET, SCOPE_ENTITY_DEPLOYMENT, SCOPE_ENTITY_NAMESPACE, SCOPE_ENTITY_CLUSTER, |
| field |  |  | [V2ScopeField](#V2ScopeField_CommonObjectReference) |  | FIELD_UNSET, FIELD_ID, FIELD_NAME, FIELD_LABEL, FIELD_ANNOTATION, |
| values |  |  | List of [V2RuleValue](#V2RuleValue_CommonObjectReference) |  |  |

<a id="V2ExceptionExpiry_CommonObjectReference"></a>

## V2ExceptionExpiry

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| expiryType |  |  | [ExceptionExpiryExpiryType](#ExceptionExpiryExpiryType_CommonObjectReference) |  | TIME, ALL_CVE_FIXABLE, ANY_CVE_FIXABLE, |
| expiresOn |  |  | Date | Indicates the timestamp when the exception expires. This field is REQUIRED only if the expiry type is set to TIME. | date-time |

<a id="V2ExceptionStatus_CommonObjectReference"></a>

## V2ExceptionStatus

Indicates the status of a request.

- PENDING: Default request state. It indicates that the request has not been fulfilled and that an action (approve/deny) is required.

- APPROVED: Indicates that the request has been approved by the approver.

- DENIED: Indicates that the request has been denied by the approver.

- APPROVED_PENDING_UPDATE: Indicates that the original request was approved, but an update is still pending an approval or denial.

| Enum Values             |
|-------------------------|
| PENDING                 |
| APPROVED                |
| DENIED                  |
| APPROVED_PENDING_UPDATE |

<a id="V2FailedCluster_CommonObjectReference"></a>

## V2FailedCluster

| Field Name      | Required | Nullable | Type   | Description | Format |
|-----------------|----------|----------|--------|-------------|--------|
| clusterId       |          |          | String |             |        |
| clusterName     |          |          | String |             |        |
| reason          |          |          | String |             |        |
| operatorVersion |          |          | String |             |        |

<a id="V2FalsePositiveUpdate_CommonObjectReference"></a>

## V2FalsePositiveUpdate

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| cves |  |  | List of `string` | Use this field to update the CVEs of a false-positive exception. |  |

<a id="V2GetBaseImageReferenceResponse_CommonObjectReference"></a>

## V2GetBaseImageReferenceResponse

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| baseImageReferences |  |  | List of [V2BaseImageReference](#V2BaseImageReference_CommonObjectReference) |  |  |

<a id="V2GetVMCVEComponentsResponse_CommonObjectReference"></a>

## V2GetVMCVEComponentsResponse

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| components |  |  | List of [V2VMCVEComponentRow](#V2VMCVEComponentRow_CommonObjectReference) |  |  |

<a id="V2GetVulnerabilityExceptionResponse_CommonObjectReference"></a>

## V2GetVulnerabilityExceptionResponse

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| exception |  |  | [V2VulnerabilityException](#V2VulnerabilityException_CommonObjectReference) |  |  |

<a id="V2ListComplianceCheckClusterResponse_CommonObjectReference"></a>

## V2ListComplianceCheckClusterResponse

ListComplianceCheckClusterResponse provides stats per cluster

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| checkResults |  |  | List of [V2ClusterCheckStatus](#V2ClusterCheckStatus_CommonObjectReference) |  |  |
| profileName |  |  | String |  |  |
| checkName |  |  | String |  |  |
| totalCount |  |  | Integer |  | int32 |
| controls |  |  | List of [V2ComplianceControl](#V2ComplianceControl_CommonObjectReference) |  |  |

<a id="V2ListComplianceCheckResultResponse_CommonObjectReference"></a>

## V2ListComplianceCheckResultResponse

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| checkResults |  |  | List of [V2ComplianceCheckResult](#V2ComplianceCheckResult_CommonObjectReference) |  |  |
| profileName |  |  | String |  |  |
| clusterId |  |  | String |  |  |
| totalCount |  |  | Integer |  | int32 |
| lastScanTime |  |  | Date |  | date-time |

<a id="V2ListComplianceClusterOverallStatsResponse_CommonObjectReference"></a>

## V2ListComplianceClusterOverallStatsResponse

ListComplianceCheckScanStatsResponse provides stats per cluster

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| scanStats |  |  | List of [V2ComplianceClusterOverallStats](#V2ComplianceClusterOverallStats_CommonObjectReference) |  |  |
| totalCount |  |  | Integer |  | int32 |

<a id="V2ListComplianceClusterProfileStatsResponse_CommonObjectReference"></a>

## V2ListComplianceClusterProfileStatsResponse

ListComplianceClusterProfileStatsResponse provides stats for the profiles within the scans

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| scanStats |  |  | List of [V2ComplianceProfileScanStats](#V2ComplianceProfileScanStats_CommonObjectReference) |  |  |
| clusterId |  |  | String |  |  |
| clusterName |  |  | String |  |  |
| totalCount |  |  | Integer |  | int32 |

<a id="V2ListComplianceClusterScanStatsResponse_CommonObjectReference"></a>

## V2ListComplianceClusterScanStatsResponse

ListComplianceClusterScanStatsResponse provides stats for the clusters within the scans

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| scanStats |  |  | List of [V2ComplianceClusterScanStats](#V2ComplianceClusterScanStats_CommonObjectReference) |  |  |
| totalCount |  |  | Integer |  | int32 |

<a id="V2ListComplianceIntegrationsResponse_CommonObjectReference"></a>

## V2ListComplianceIntegrationsResponse

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| integrations |  |  | List of [V2ComplianceIntegration](#V2ComplianceIntegration_CommonObjectReference) |  |  |
| totalCount |  |  | Integer |  | int32 |

<a id="V2ListComplianceProfileResults_CommonObjectReference"></a>

## V2ListComplianceProfileResults

ListComplianceProfileResults provides scan stats overview based on profile

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| profileResults |  |  | List of [V2ComplianceCheckResultStatusCount](#V2ComplianceCheckResultStatusCount_CommonObjectReference) |  |  |
| profileName |  |  | String |  |  |
| totalCount |  |  | Integer |  | int32 |

<a id="V2ListComplianceProfileScanStatsResponse_CommonObjectReference"></a>

## V2ListComplianceProfileScanStatsResponse

ListComplianceProfileScanStatsResponse provides stats for the profiles within the scans

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| scanStats |  |  | List of [V2ComplianceProfileScanStats](#V2ComplianceProfileScanStats_CommonObjectReference) |  |  |
| totalCount |  |  | Integer |  | int32 |

<a id="V2ListComplianceProfileSummaryResponse_CommonObjectReference"></a>

## V2ListComplianceProfileSummaryResponse

ListComplianceProfileSummaryResponse provides a list of profiles summaries

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| profiles |  |  | List of [V2ComplianceProfileSummary](#V2ComplianceProfileSummary_CommonObjectReference) |  |  |
| totalCount |  |  | Integer |  | int32 |

<a id="V2ListComplianceProfilesResponse_CommonObjectReference"></a>

## V2ListComplianceProfilesResponse

ListComplianceProfilesResponse provides a list of profiles

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| profiles |  |  | List of [V2ComplianceProfile](#V2ComplianceProfile_CommonObjectReference) |  |  |
| totalCount |  |  | Integer |  | int32 |

<a id="V2ListComplianceResultsResponse_CommonObjectReference"></a>

## V2ListComplianceResultsResponse

ListComplianceResultsResponse provides the complete scan results

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| scanResults |  |  | List of [V2ComplianceCheckData](#V2ComplianceCheckData_CommonObjectReference) |  |  |
| totalCount |  |  | Integer |  | int32 |

<a id="V2ListComplianceScanConfigsClusterProfileResponse_CommonObjectReference"></a>

## V2ListComplianceScanConfigsClusterProfileResponse

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| clusterId |  |  | String |  |  |
| clusterName |  |  | String |  |  |
| profiles |  |  | List of [V2ComplianceProfileSummary](#V2ComplianceProfileSummary_CommonObjectReference) |  |  |
| totalCount |  |  | Integer |  | int32 |

<a id="V2ListComplianceScanConfigsProfileResponse_CommonObjectReference"></a>

## V2ListComplianceScanConfigsProfileResponse

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| profiles |  |  | List of [V2ComplianceProfileSummary](#V2ComplianceProfileSummary_CommonObjectReference) |  |  |
| totalCount |  |  | Integer |  | int32 |

<a id="V2ListComplianceScanConfigurationsResponse_CommonObjectReference"></a>

## V2ListComplianceScanConfigurationsResponse

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| configurations |  |  | List of [V2ComplianceScanConfigurationStatus](#V2ComplianceScanConfigurationStatus_CommonObjectReference) |  |  |
| totalCount |  |  | Integer |  | int32 |

<a id="V2ListReportConfigurationsResponse_CommonObjectReference"></a>

## V2ListReportConfigurationsResponse

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| reportConfigs |  |  | List of [V2ReportConfiguration](#V2ReportConfiguration_CommonObjectReference) |  |  |

<a id="V2ListVMCVEAffectedVMsResponse_CommonObjectReference"></a>

## V2ListVMCVEAffectedVMsResponse

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| vms |  |  | List of [V2VMCVEAffectedVMRow](#V2VMCVEAffectedVMRow_CommonObjectReference) |  |  |
| totalCount |  |  | Integer |  | int32 |

<a id="V2ListVMCVEsByVMResponse_CommonObjectReference"></a>

## V2ListVMCVEsByVMResponse

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| cves |  |  | List of [V2VMCVERow](#V2VMCVERow_CommonObjectReference) |  |  |
| totalCount |  |  | Integer |  | int32 |

<a id="V2ListVMCVEsResponse_CommonObjectReference"></a>

## V2ListVMCVEsResponse

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| cves |  |  | List of [V2VMCVEListItem](#V2VMCVEListItem_CommonObjectReference) |  |  |
| totalCount |  |  | Integer |  | int32 |

<a id="V2ListVMComponentsResponse_CommonObjectReference"></a>

## V2ListVMComponentsResponse

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| components |  |  | List of [V2VMComponentRow](#V2VMComponentRow_CommonObjectReference) |  |  |
| totalCount |  |  | Integer |  | int32 |

<a id="V2ListVMsResponse_CommonObjectReference"></a>

## V2ListVMsResponse

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| vms |  |  | List of [V2VMListItem](#V2VMListItem_CommonObjectReference) |  |  |
| totalCount |  |  | Integer |  | int32 |

<a id="V2ListVirtualMachinesResponse_CommonObjectReference"></a>

## V2ListVirtualMachinesResponse

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| virtualMachines |  |  | List of [V2VirtualMachine](#V2VirtualMachine_CommonObjectReference) |  |  |
| totalCount |  |  | Integer |  | int32 |

<a id="V2ListVulnerabilityExceptionsResponse_CommonObjectReference"></a>

## V2ListVulnerabilityExceptionsResponse

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| exceptions |  |  | List of [V2VulnerabilityException](#V2VulnerabilityException_CommonObjectReference) |  |  |

<a id="V2MatchType_CommonObjectReference"></a>

## V2MatchType

| Enum Values |
|-------------|
| EXACT       |
| REGEX       |

<a id="V2NotificationMethod_CommonObjectReference"></a>

## V2NotificationMethod

| Enum Values |
|-------------|
| EMAIL       |
| DOWNLOAD    |

<a id="V2NotifierConfiguration_CommonObjectReference"></a>

## V2NotifierConfiguration

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| emailConfig |  |  | [V2EmailNotifierConfiguration](#V2EmailNotifierConfiguration_CommonObjectReference) |  |  |
| notifierName |  |  | String |  |  |

<a id="V2Pagination_CommonObjectReference"></a>

## V2Pagination

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| limit |  |  | Integer |  | int32 |
| offset |  |  | Integer |  | int32 |
| sortOption |  |  | [V2SortOption](#V2SortOption_CommonObjectReference) |  |  |
| sortOptions |  |  | List of [V2SortOption](#V2SortOption_CommonObjectReference) | This field is under development. It is not supported on any REST APIs. |  |

<a id="V2RawQuery_CommonObjectReference"></a>

## V2RawQuery

RawQuery represents the search query string. The format of the query string is "\<field name\>:\<value,value,…​\>\<field name\>:\<value, value,...\>…​" For example: To search for deployments named "central" and "sensor" in the namespace "stackrox", the query string would be "Deployment:central,sensor+Namespace:stackrox" RawQuery is used in ListAPIs to search for a particular object.

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| query |  |  | String |  |  |
| pagination |  |  | [V2Pagination](#V2Pagination_CommonObjectReference) |  |  |

<a id="V2ReportConfiguration_CommonObjectReference"></a>

## V2ReportConfiguration

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| id |  |  | String |  |  |
| name |  |  | String |  |  |
| description |  |  | String |  |  |
| type |  |  | [V2ReportConfigurationReportType](#V2ReportConfigurationReportType_CommonObjectReference) |  | VULNERABILITY, |
| vulnReportFilters |  |  | [V2VulnerabilityReportFilters](#V2VulnerabilityReportFilters_CommonObjectReference) |  |  |
| schedule |  |  | [V2ReportSchedule](#V2ReportSchedule_CommonObjectReference) |  |  |
| resourceScope |  |  | [V2ResourceScope](#V2ResourceScope_CommonObjectReference) |  |  |
| notifiers |  |  | List of [V2NotifierConfiguration](#V2NotifierConfiguration_CommonObjectReference) |  |  |

<a id="V2ReportConfigurationReportType_CommonObjectReference"></a>

## V2ReportConfigurationReportType

| Enum Values   |
|---------------|
| VULNERABILITY |

<a id="V2ReportHistoryResponse_CommonObjectReference"></a>

## V2ReportHistoryResponse

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| reportSnapshots |  |  | List of [V2ReportSnapshot](#V2ReportSnapshot_CommonObjectReference) |  |  |

<a id="V2ReportRequestViewBased_CommonObjectReference"></a>

## V2ReportRequestViewBased

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| type |  |  | [V2ReportRequestViewBasedReportType](#V2ReportRequestViewBasedReportType_CommonObjectReference) |  | VULNERABILITY, |
| viewBasedVulnReportFilters |  |  | [V2ViewBasedVulnerabilityReportFilters](#V2ViewBasedVulnerabilityReportFilters_CommonObjectReference) |  |  |
| areaOfConcern |  |  | String |  |  |

<a id="V2ReportRequestViewBasedReportType_CommonObjectReference"></a>

## V2ReportRequestViewBasedReportType

| Enum Values   |
|---------------|
| VULNERABILITY |

<a id="V2ReportSchedule_CommonObjectReference"></a>

## V2ReportSchedule

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| intervalType |  |  | [V2ReportScheduleIntervalType](#V2ReportScheduleIntervalType_CommonObjectReference) |  | UNSET, WEEKLY, MONTHLY, DAILY, |
| hour |  |  | Integer |  | int32 |
| minute |  |  | Integer |  | int32 |
| daysOfWeek |  |  | [V2ReportScheduleDaysOfWeek](#V2ReportScheduleDaysOfWeek_CommonObjectReference) |  |  |
| daysOfMonth |  |  | [V2ReportScheduleDaysOfMonth](#V2ReportScheduleDaysOfMonth_CommonObjectReference) |  |  |

<a id="V2ReportScheduleDaysOfMonth_CommonObjectReference"></a>

## V2ReportScheduleDaysOfMonth

1 for 1st, 2 for 2nd …​. 31 for 31st

| Field Name | Required | Nullable | Type              | Description | Format |
|------------|----------|----------|-------------------|-------------|--------|
| days       |          |          | List of `integer` |             | int32  |

<a id="V2ReportScheduleDaysOfWeek_CommonObjectReference"></a>

## V2ReportScheduleDaysOfWeek

Sunday = 0, Monday = 1, …​. Saturday = 6

| Field Name | Required | Nullable | Type              | Description | Format |
|------------|----------|----------|-------------------|-------------|--------|
| days       |          |          | List of `integer` |             | int32  |

<a id="V2ReportScheduleIntervalType_CommonObjectReference"></a>

## V2ReportScheduleIntervalType

| Enum Values |
|-------------|
| UNSET       |
| WEEKLY      |
| MONTHLY     |
| DAILY       |

<a id="V2ReportSnapshot_CommonObjectReference"></a>

## V2ReportSnapshot

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| reportConfigId |  |  | String |  |  |
| reportJobId |  |  | String |  |  |
| name |  |  | String |  |  |
| description |  |  | String |  |  |
| vulnReportFilters |  |  | [V2VulnerabilityReportFilters](#V2VulnerabilityReportFilters_CommonObjectReference) |  |  |
| viewBasedVulnReportFilters |  |  | [V2ViewBasedVulnerabilityReportFilters](#V2ViewBasedVulnerabilityReportFilters_CommonObjectReference) |  |  |
| collectionSnapshot |  |  | [V2CollectionSnapshot](#V2CollectionSnapshot_CommonObjectReference) |  |  |
| schedule |  |  | [V2ReportSchedule](#V2ReportSchedule_CommonObjectReference) |  |  |
| reportStatus |  |  | [V2ReportStatus](#V2ReportStatus_CommonObjectReference) |  |  |
| notifiers |  |  | List of [V2NotifierConfiguration](#V2NotifierConfiguration_CommonObjectReference) |  |  |
| user |  |  | [V2SlimUser](#V2SlimUser_CommonObjectReference) |  |  |
| isDownloadAvailable |  |  | Boolean |  |  |
| areaOfConcern |  |  | String |  |  |
| resourceScope |  |  | [V2ResourceScope](#V2ResourceScope_CommonObjectReference) |  |  |

<a id="V2ReportStatus_CommonObjectReference"></a>

## V2ReportStatus

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| runState |  |  | [V2ReportStatusRunState](#V2ReportStatusRunState_CommonObjectReference) |  | WAITING, PREPARING, GENERATED, DELIVERED, FAILURE, |
| completedAt |  |  | Date |  | date-time |
| errorMsg |  |  | String |  |  |
| reportRequestType |  |  | [V2ReportStatusReportMethod](#V2ReportStatusReportMethod_CommonObjectReference) |  | ON_DEMAND, SCHEDULED, |
| reportNotificationMethod |  |  | [V2NotificationMethod](#V2NotificationMethod_CommonObjectReference) |  | EMAIL, DOWNLOAD, |

<a id="V2ReportStatusReportMethod_CommonObjectReference"></a>

## V2ReportStatusReportMethod

| Enum Values |
|-------------|
| ON_DEMAND   |
| SCHEDULED   |

<a id="V2ReportStatusResponse_CommonObjectReference"></a>

## V2ReportStatusResponse

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| status |  |  | [V2ReportStatus](#V2ReportStatus_CommonObjectReference) |  |  |

<a id="V2ReportStatusRunState_CommonObjectReference"></a>

## V2ReportStatusRunState

| Enum Values |
|-------------|
| WAITING     |
| PREPARING   |
| GENERATED   |
| DELIVERED   |
| FAILURE     |

<a id="V2ResourceScope_CommonObjectReference"></a>

## V2ResourceScope

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| collectionScope |  |  | [V2CollectionReference](#V2CollectionReference_CommonObjectReference) |  |  |
| entityScope |  |  | [V2EntityScope](#V2EntityScope_CommonObjectReference) |  |  |

<a id="V2RuleValue_CommonObjectReference"></a>

## V2RuleValue

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| value |  |  | String |  |  |
| matchType |  |  | [V2MatchType](#V2MatchType_CommonObjectReference) |  | EXACT, REGEX, |

<a id="V2RunReportRequest_CommonObjectReference"></a>

## V2RunReportRequest

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| reportConfigId |  |  | String |  |  |
| reportNotificationMethod |  |  | [V2NotificationMethod](#V2NotificationMethod_CommonObjectReference) |  | EMAIL, DOWNLOAD, |

<a id="V2RunReportResponse_CommonObjectReference"></a>

## V2RunReportResponse

| Field Name     | Required | Nullable | Type   | Description | Format |
|----------------|----------|----------|--------|-------------|--------|
| reportConfigId |          |          | String |             |        |
| reportId       |          |          | String |             |        |

<a id="V2RunReportResponseViewBased_CommonObjectReference"></a>

## V2RunReportResponseViewBased

| Field Name  | Required | Nullable | Type   | Description | Format |
|-------------|----------|----------|--------|-------------|--------|
| reportID    |          |          | String |             |        |
| requestName |          |          | String |             |        |

<a id="V2ScanComponent_CommonObjectReference"></a>

## V2ScanComponent

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| name |  |  | String |  |  |
| version |  |  | String |  |  |
| topCvss |  |  | Float |  | float |
| riskScore |  |  | Float |  | float |
| architecture |  |  | String |  |  |
| vulns |  |  | List of [V2EmbeddedVulnerability](#V2EmbeddedVulnerability_CommonObjectReference) |  |  |
| source |  |  | [V2SourceType](#V2SourceType_CommonObjectReference) |  | OS, PYTHON, JAVA, RUBY, NODEJS, GO, DOTNETCORERUNTIME, INFRASTRUCTURE, |
| notes |  |  | List of [V2ScanComponentNote](#V2ScanComponentNote_CommonObjectReference) |  |  |

<a id="V2ScanComponentNote_CommonObjectReference"></a>

## V2ScanComponentNote

Note specifies a conditional status of the scan component.

- UNSCANNED: Scan components remain unscanned if the corresponding package is not associated with a valid Common Platform Enumeration (CPE).

| Enum Values |
|-------------|
| UNSPECIFIED |
| UNSCANNED   |

<a id="V2ScanStatus_CommonObjectReference"></a>

## V2ScanStatus

| Enum Values  |
|--------------|
| NOT_SCANNED  |
| SCAN_PENDING |
| CPE_MISSING  |
| REPO_UNKNOWN |
| SCANNED      |

<a id="V2Schedule_CommonObjectReference"></a>

## V2Schedule

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| intervalType |  |  | [V2ScheduleIntervalType](#V2ScheduleIntervalType_CommonObjectReference) |  | UNSET, WEEKLY, MONTHLY, DAILY, |
| hour |  |  | Integer |  | int32 |
| minute |  |  | Integer |  | int32 |
| daysOfWeek |  |  | [V2ScheduleDaysOfWeek](#V2ScheduleDaysOfWeek_CommonObjectReference) |  |  |
| daysOfMonth |  |  | [V2ScheduleDaysOfMonth](#V2ScheduleDaysOfMonth_CommonObjectReference) |  |  |

<a id="V2ScheduleDaysOfMonth_CommonObjectReference"></a>

## V2ScheduleDaysOfMonth

1 for 1st, 2 for 2nd …​. 31 for 31st

| Field Name | Required | Nullable | Type              | Description | Format |
|------------|----------|----------|-------------------|-------------|--------|
| days       |          |          | List of `integer` |             | int32  |

<a id="V2ScheduleDaysOfWeek_CommonObjectReference"></a>

## V2ScheduleDaysOfWeek

Sunday = 0, Monday = 1, …​. Saturday = 6

| Field Name | Required | Nullable | Type              | Description | Format |
|------------|----------|----------|-------------------|-------------|--------|
| days       |          |          | List of `integer` |             | int32  |

<a id="V2ScheduleIntervalType_CommonObjectReference"></a>

## V2ScheduleIntervalType

| Enum Values |
|-------------|
| UNSET       |
| WEEKLY      |
| MONTHLY     |
| DAILY       |

<a id="V2ScopeEntity_CommonObjectReference"></a>

## V2ScopeEntity

| Enum Values             |
|-------------------------|
| SCOPE_ENTITY_UNSET      |
| SCOPE_ENTITY_DEPLOYMENT |
| SCOPE_ENTITY_NAMESPACE  |
| SCOPE_ENTITY_CLUSTER    |

<a id="V2ScopeField_CommonObjectReference"></a>

## V2ScopeField

| Enum Values      |
|------------------|
| FIELD_UNSET      |
| FIELD_ID         |
| FIELD_NAME       |
| FIELD_LABEL      |
| FIELD_ANNOTATION |

<a id="V2SlimUser_CommonObjectReference"></a>

## V2SlimUser

| Field Name | Required | Nullable | Type   | Description | Format |
|------------|----------|----------|--------|-------------|--------|
| id         |          |          | String |             |        |
| name       |          |          | String |             |        |

<a id="V2SortOption_CommonObjectReference"></a>

## V2SortOption

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| field |  |  | String |  |  |
| reversed |  |  | Boolean |  |  |
| aggregateBy |  |  | [V2AggregateBy](#V2AggregateBy_CommonObjectReference) |  |  |

<a id="V2Source_CommonObjectReference"></a>

## V2Source

| Enum Values    |
|----------------|
| SOURCE_UNKNOWN |
| SOURCE_RED_HAT |
| SOURCE_OSV     |
| SOURCE_NVD     |

<a id="V2SourceType_CommonObjectReference"></a>

## V2SourceType

| Enum Values       |
|-------------------|
| OS                |
| PYTHON            |
| JAVA              |
| RUBY              |
| NODEJS            |
| GO                |
| DOTNETCORERUNTIME |
| INFRASTRUCTURE    |

<a id="V2UpdateVulnerabilityExceptionResponse_CommonObjectReference"></a>

## V2UpdateVulnerabilityExceptionResponse

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| exception |  |  | [V2VulnerabilityException](#V2VulnerabilityException_CommonObjectReference) |  |  |

<a id="V2VMCVEAffectedVMRow_CommonObjectReference"></a>

## V2VMCVEAffectedVMRow

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| vmId |  |  | String |  |  |
| vmName |  |  | String |  |  |
| severity |  |  | [V2VulnerabilitySeverity](#V2VulnerabilitySeverity_CommonObjectReference) |  | UNKNOWN_VULNERABILITY_SEVERITY, LOW_VULNERABILITY_SEVERITY, MODERATE_VULNERABILITY_SEVERITY, IMPORTANT_VULNERABILITY_SEVERITY, CRITICAL_VULNERABILITY_SEVERITY, |
| isFixable |  |  | Boolean |  |  |
| cvss |  |  | Float |  | float |
| guestOs |  |  | String |  |  |
| affectedComponentCount |  |  | Integer |  | int32 |

<a id="V2VMCVEComponentRow_CommonObjectReference"></a>

## V2VMCVEComponentRow

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| componentName |  |  | String |  |  |
| componentVersion |  |  | String |  |  |
| source |  |  | [V2SourceType](#V2SourceType_CommonObjectReference) |  | OS, PYTHON, JAVA, RUBY, NODEJS, GO, DOTNETCORERUNTIME, INFRASTRUCTURE, |
| fixedBy |  |  | String |  |  |
| advisory |  |  | [V2Advisory](#V2Advisory_CommonObjectReference) |  |  |

<a id="V2VMCVEDetail_CommonObjectReference"></a>

## V2VMCVEDetail

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| cve |  |  | String |  |  |
| summary |  |  | String |  |  |
| link |  |  | String |  |  |
| epssProbability |  |  | Float |  | float |
| publishedOn |  |  | Date |  | date-time |
| firstDiscovered |  |  | Date |  | date-time |
| affectedVmCount |  |  | Integer |  | int32 |
| totalVmCount |  |  | Integer |  | int32 |
| affectedGuestOsCount |  |  | Integer |  | int32 |
| vmSeverityCounts |  |  | [V2VulnCountBySeverity](#V2VulnCountBySeverity_CommonObjectReference) |  |  |
| topCvss |  |  | Float |  | float |

<a id="V2VMCVEListItem_CommonObjectReference"></a>

## V2VMCVEListItem

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| cve |  |  | String |  |  |
| vmSeverityCounts |  |  | [V2VulnCountBySeverity](#V2VulnCountBySeverity_CommonObjectReference) |  |  |
| topCvss |  |  | Float |  | float |
| cvssVersion |  |  | String |  |  |
| affectedVmCount |  |  | Integer |  | int32 |
| totalVmCount |  |  | Integer |  | int32 |
| epssProbability |  |  | Float |  | float |
| publishedOn |  |  | Date |  | date-time |

<a id="V2VMCVERow_CommonObjectReference"></a>

## V2VMCVERow

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| cve |  |  | String |  |  |
| severity |  |  | [V2VulnerabilitySeverity](#V2VulnerabilitySeverity_CommonObjectReference) |  | UNKNOWN_VULNERABILITY_SEVERITY, LOW_VULNERABILITY_SEVERITY, MODERATE_VULNERABILITY_SEVERITY, IMPORTANT_VULNERABILITY_SEVERITY, CRITICAL_VULNERABILITY_SEVERITY, |
| isFixable |  |  | Boolean |  |  |
| cvss |  |  | Float |  | float |
| nvdCvss |  |  | Float |  | float |
| epssProbability |  |  | Float |  | float |
| affectedComponentCount |  |  | Integer |  | int32 |
| publishedOn |  |  | Date |  | date-time |
| summary |  |  | String |  |  |
| link |  |  | String |  |  |
| advisory |  |  | [V2Advisory](#V2Advisory_CommonObjectReference) |  |  |

<a id="V2VMComponentRow_CommonObjectReference"></a>

## V2VMComponentRow

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| id |  |  | String |  |  |
| name |  |  | String |  |  |
| version |  |  | String |  |  |
| source |  |  | [V2SourceType](#V2SourceType_CommonObjectReference) |  | OS, PYTHON, JAVA, RUBY, NODEJS, GO, DOTNETCORERUNTIME, INFRASTRUCTURE, |
| scanStatus |  |  | [V2ScanStatus](#V2ScanStatus_CommonObjectReference) |  | NOT_SCANNED, SCAN_PENDING, CPE_MISSING, REPO_UNKNOWN, SCANNED, |
| lastScanned |  |  | Date |  | date-time |
| cveCount |  |  | Integer |  | int32 |

<a id="V2VMDashboardCountsResponse_CommonObjectReference"></a>

## V2VMDashboardCountsResponse

| Field Name | Required | Nullable | Type    | Description | Format |
|------------|----------|----------|---------|-------------|--------|
| vmCount    |          |          | Integer |             | int32  |
| cveCount   |          |          | Integer |             | int32  |

<a id="V2VMDetail_CommonObjectReference"></a>

## V2VMDetail

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| id |  |  | String |  |  |
| name |  |  | String |  |  |
| namespace |  |  | String |  |  |
| clusterId |  |  | String |  |  |
| clusterName |  |  | String |  |  |
| guestOs |  |  | String |  |  |
| state |  |  | [V2VirtualMachineV2State](#V2VirtualMachineV2State_CommonObjectReference) |  | VM_STATE_UNKNOWN, VM_STATE_STOPPED, VM_STATE_RUNNING, |
| lastUpdated |  |  | Date |  | date-time |
| facts |  |  | Map of `string` | Contains KubeVirt facts. Labels and annotations are added by the sensor pipeline. |  |
| annotations |  |  | Map of `string` |  |  |
| labels |  |  | Map of `string` |  |  |
| vsockCid |  |  | Integer |  | int32 |
| notes |  |  | List of [V2VMNote](#V2VMNote_CommonObjectReference) |  |  |
| latestScan |  |  | [V2VMScanInfo](#V2VMScanInfo_CommonObjectReference) |  |  |
| agentStatus |  |  | [V2AgentStatus](#V2AgentStatus_CommonObjectReference) |  | AGENT_STATUS_UNKNOWN, AGENT_STATUS_ACTIVE, |

<a id="V2VMListItem_CommonObjectReference"></a>

## V2VMListItem

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| id |  |  | String |  |  |
| name |  |  | String |  |  |
| namespace |  |  | String |  |  |
| clusterId |  |  | String |  |  |
| clusterName |  |  | String |  |  |
| guestOs |  |  | String |  |  |
| state |  |  | [V2VirtualMachineV2State](#V2VirtualMachineV2State_CommonObjectReference) |  | VM_STATE_UNKNOWN, VM_STATE_STOPPED, VM_STATE_RUNNING, |
| scanTime |  |  | Date |  | date-time |
| lastUpdated |  |  | Date |  | date-time |
| cveSeverityCounts |  |  | [V2VulnCountBySeverity](#V2VulnCountBySeverity_CommonObjectReference) |  |  |
| componentScanCount |  |  | [V2ComponentScanCount](#V2ComponentScanCount_CommonObjectReference) |  |  |

<a id="V2VMNote_CommonObjectReference"></a>

## V2VMNote

| Enum Values                                 |
|---------------------------------------------|
| VM_NOTE_MISSING_METADATA                    |
| VM_NOTE_MISSING_SCAN_DATA                   |
| VM_NOTE_MISSING_SIGNATURE                   |
| VM_NOTE_MISSING_SIGNATURE_VERIFICATION_DATA |
| VM_NOTE_MISSING_SCANNER                     |
| VM_NOTE_SCAN_FAILED                         |

<a id="V2VMScanInfo_CommonObjectReference"></a>

## V2VMScanInfo

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| scanId |  |  | String |  |  |
| scanOs |  |  | String |  |  |
| scanTime |  |  | Date |  | date-time |
| topCvss |  |  | Float |  | float |
| scanNotes |  |  | List of [V2VMScanNote](#V2VMScanNote_CommonObjectReference) |  |  |

<a id="V2VMScanNote_CommonObjectReference"></a>

## V2VMScanNote

| Enum Values                 |
|-----------------------------|
| VM_SCAN_NOTE_UNSET          |
| VM_SCAN_NOTE_OS_UNKNOWN     |
| VM_SCAN_NOTE_OS_UNSUPPORTED |

<a id="V2VMVulnSummary_CommonObjectReference"></a>

## V2VMVulnSummary

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| severityCounts |  |  | [V2VulnCountBySeverity](#V2VulnCountBySeverity_CommonObjectReference) |  |  |
| fixableCount |  |  | Integer |  | int32 |
| notFixableCount |  |  | Integer |  | int32 |

<a id="V2ViewBasedVulnerabilityReportFilters_CommonObjectReference"></a>

## V2ViewBasedVulnerabilityReportFilters

filter for ondemand view based reports

| Field Name | Required | Nullable | Type   | Description | Format |
|------------|----------|----------|--------|-------------|--------|
| query      |          |          | String |             |        |

<a id="V2VirtualMachine_CommonObjectReference"></a>

## V2VirtualMachine

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| id |  |  | String |  |  |
| namespace |  |  | String |  |  |
| name |  |  | String |  |  |
| clusterId |  |  | String |  |  |
| clusterName |  |  | String |  |  |
| facts |  |  | Map of `string` |  |  |
| lastUpdated |  |  | Date |  | date-time |
| vsockCid |  |  | Integer |  | int32 |
| state |  |  | [VirtualMachineState](#VirtualMachineState_CommonObjectReference) |  | UNKNOWN, STOPPED, RUNNING, |
| scan |  |  | [V2VirtualMachineScan](#V2VirtualMachineScan_CommonObjectReference) |  |  |

<a id="V2VirtualMachineScan_CommonObjectReference"></a>

## V2VirtualMachineScan

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| scanTime |  |  | Date |  | date-time |
| operatingSystem |  |  | String |  |  |
| notes |  |  | List of [V2VirtualMachineScanNote](#V2VirtualMachineScanNote_CommonObjectReference) |  |  |
| components |  |  | List of [V2ScanComponent](#V2ScanComponent_CommonObjectReference) |  |  |

<a id="V2VirtualMachineScanNote_CommonObjectReference"></a>

## V2VirtualMachineScanNote

| Enum Values    |
|----------------|
| UNSET          |
| OS_UNKNOWN     |
| OS_UNSUPPORTED |

<a id="V2VirtualMachineV2State_CommonObjectReference"></a>

## V2VirtualMachineV2State

| Enum Values      |
|------------------|
| VM_STATE_UNKNOWN |
| VM_STATE_STOPPED |
| VM_STATE_RUNNING |

<a id="V2VulnCountBySeverity_CommonObjectReference"></a>

## V2VulnCountBySeverity

Vulnerability counts by severity level. Used for summary cards and inline columns.

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| critical |  |  | [V2VulnFixableCount](#V2VulnFixableCount_CommonObjectReference) |  |  |
| important |  |  | [V2VulnFixableCount](#V2VulnFixableCount_CommonObjectReference) |  |  |
| moderate |  |  | [V2VulnFixableCount](#V2VulnFixableCount_CommonObjectReference) |  |  |
| low |  |  | [V2VulnFixableCount](#V2VulnFixableCount_CommonObjectReference) |  |  |
| unknown |  |  | [V2VulnFixableCount](#V2VulnFixableCount_CommonObjectReference) |  |  |

<a id="V2VulnFixableCount_CommonObjectReference"></a>

## V2VulnFixableCount

Counts for a single severity level, split by fixability.

| Field Name | Required | Nullable | Type    | Description | Format |
|------------|----------|----------|---------|-------------|--------|
| total      |          |          | Integer |             | int32  |
| fixable    |          |          | Integer |             | int32  |

<a id="V2VulnerabilityException_CommonObjectReference"></a>

## V2VulnerabilityException

Next available tag: 16 VulnerabilityException represents a vulnerability exception such as deferral and false-positive.

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| id |  |  | String |  |  |
| name |  |  | String | Auto-generated display name of the exception. |  |
| targetState |  |  | [V2VulnerabilityState](#V2VulnerabilityState_CommonObjectReference) |  | OBSERVED, DEFERRED, FALSE_POSITIVE, |
| status |  |  | [V2ExceptionStatus](#V2ExceptionStatus_CommonObjectReference) |  | PENDING, APPROVED, DENIED, APPROVED_PENDING_UPDATE, |
| expired |  |  | Boolean | If set to `true`, this field indicates that the exception is no longer enforced. |  |
| requester |  |  | [V2SlimUser](#V2SlimUser_CommonObjectReference) |  |  |
| approvers |  |  | List of [V2SlimUser](#V2SlimUser_CommonObjectReference) |  |  |
| createdAt |  |  | Date |  | date-time |
| lastUpdated |  |  | Date |  | date-time |
| comments |  |  | List of [V2Comment](#V2Comment_CommonObjectReference) |  |  |
| scope |  |  | [V2VulnerabilityExceptionScope](#V2VulnerabilityExceptionScope_CommonObjectReference) |  |  |
| deferralRequest |  |  | [V2DeferralRequest](#V2DeferralRequest_CommonObjectReference) |  |  |
| falsePositiveRequest |  |  | Object |  |  |
| cves |  |  | List of `string` | Indicates the CVEs to which the exception applies. |  |
| deferralUpdate |  |  | [V2DeferralUpdate](#V2DeferralUpdate_CommonObjectReference) |  |  |
| falsePositiveUpdate |  |  | [V2FalsePositiveUpdate](#V2FalsePositiveUpdate_CommonObjectReference) |  |  |

<a id="V2VulnerabilityExceptionScope_CommonObjectReference"></a>

## V2VulnerabilityExceptionScope

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| imageScope |  |  | [ScopeImage](#ScopeImage_CommonObjectReference) |  |  |

<a id="V2VulnerabilityReportFilters_CommonObjectReference"></a>

## V2VulnerabilityReportFilters

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| fixability |  |  | [VulnerabilityReportFiltersFixability](#VulnerabilityReportFiltersFixability_CommonObjectReference) |  | BOTH, FIXABLE, NOT_FIXABLE, |
| severities |  |  | List of [V2VulnerabilityReportFiltersVulnerabilitySeverity](#V2VulnerabilityReportFiltersVulnerabilitySeverity_CommonObjectReference) |  |  |
| imageTypes |  |  | List of [VulnerabilityReportFiltersImageType](#VulnerabilityReportFiltersImageType_CommonObjectReference) |  |  |
| allVuln |  |  | Boolean |  |  |
| sinceLastSentScheduledReport |  |  | Boolean |  |  |
| sinceStartDate |  |  | Date |  | date-time |
| includeNvdCvss |  |  | Boolean | Deprecated: These fields are no longer used. NVD CVSS, EPSS Probability and Advisory columns are always included in reports. |  |
| includeEpssProbability |  |  | Boolean |  |  |
| includeAdvisory |  |  | Boolean |  |  |
| query |  |  | String |  |  |

<a id="V2VulnerabilityReportFiltersVulnerabilitySeverity_CommonObjectReference"></a>

## V2VulnerabilityReportFiltersVulnerabilitySeverity

| Enum Values                      |
|----------------------------------|
| UNKNOWN_VULNERABILITY_SEVERITY   |
| LOW_VULNERABILITY_SEVERITY       |
| MODERATE_VULNERABILITY_SEVERITY  |
| IMPORTANT_VULNERABILITY_SEVERITY |
| CRITICAL_VULNERABILITY_SEVERITY  |

<a id="V2VulnerabilitySeverity_CommonObjectReference"></a>

## V2VulnerabilitySeverity

| Enum Values                      |
|----------------------------------|
| UNKNOWN_VULNERABILITY_SEVERITY   |
| LOW_VULNERABILITY_SEVERITY       |
| MODERATE_VULNERABILITY_SEVERITY  |
| IMPORTANT_VULNERABILITY_SEVERITY |
| CRITICAL_VULNERABILITY_SEVERITY  |

<a id="V2VulnerabilityState_CommonObjectReference"></a>

## V2VulnerabilityState

VulnerabilityState are the possible applicable to CVE. By default all vulnerabilities are in observed state.

- OBSERVED: This is the default state and indicates that the CVE is not excluded from policy evaluation and risk evaluation.

<!-- -->

- DEFERRED: Indicates that the vulnerability is deferred. A deferred CVE is excluded from policy evaluation and risk evaluation.

- FALSE_POSITIVE: Indicates that the vulnerability is a false-positive. A false-positive CVE is excluded from policy evaluation and risk evaluation.

| Enum Values    |
|----------------|
| OBSERVED       |
| DEFERRED       |
| FALSE_POSITIVE |

<a id="ViolationKeyValueAttrs_CommonObjectReference"></a>

## ViolationKeyValueAttrs

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| attrs |  |  | List of [KeyValueAttrsKeyValueAttr](#KeyValueAttrsKeyValueAttr_CommonObjectReference) |  |  |

<a id="ViolationNetworkFlowInfo_CommonObjectReference"></a>

## ViolationNetworkFlowInfo

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| protocol |  |  | [StorageL4Protocol](#StorageL4Protocol_CommonObjectReference) |  | L4_PROTOCOL_UNKNOWN, L4_PROTOCOL_TCP, L4_PROTOCOL_UDP, L4_PROTOCOL_ICMP, L4_PROTOCOL_RAW, L4_PROTOCOL_SCTP, L4_PROTOCOL_ANY, |
| source |  |  | [NetworkFlowInfoEntity](#NetworkFlowInfoEntity_CommonObjectReference) |  |  |
| destination |  |  | [NetworkFlowInfoEntity](#NetworkFlowInfoEntity_CommonObjectReference) |  |  |

<a id="VirtualMachineState_CommonObjectReference"></a>

## VirtualMachineState

| Enum Values |
|-------------|
| UNKNOWN     |
| STOPPED     |
| RUNNING     |

<a id="VolumeMountPropagation_CommonObjectReference"></a>

## VolumeMountPropagation

| Enum Values       |
|-------------------|
| NONE              |
| HOST_TO_CONTAINER |
| BIDIRECTIONAL     |

<a id="VulnerabilityExceptionServiceApproveVulnerabilityExceptionBody_CommonObjectReference"></a>

## VulnerabilityExceptionServiceApproveVulnerabilityExceptionBody

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| comment |  |  | String | REQUIRED. The rationale for approving the exception. |  |

<a id="VulnerabilityExceptionServiceDenyVulnerabilityExceptionBody_CommonObjectReference"></a>

## VulnerabilityExceptionServiceDenyVulnerabilityExceptionBody

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| comment |  |  | String | REQUIRED. The rationale for denying the exception. |  |

<a id="VulnerabilityExceptionServiceUpdateVulnerabilityExceptionBody_CommonObjectReference"></a>

## VulnerabilityExceptionServiceUpdateVulnerabilityExceptionBody

| Field Name | Required | Nullable | Type | Description | Format |
|----|----|----|----|----|----|
| comment |  |  | String | REQUIRED. The rationale for updating the exception. |  |
| deferralUpdate |  |  | [V2DeferralUpdate](#V2DeferralUpdate_CommonObjectReference) |  |  |
| falsePositiveUpdate |  |  | [V2FalsePositiveUpdate](#V2FalsePositiveUpdate_CommonObjectReference) |  |  |

<a id="VulnerabilityReportFiltersFixability_CommonObjectReference"></a>

## VulnerabilityReportFiltersFixability

| Enum Values |
|-------------|
| BOTH        |
| FIXABLE     |
| NOT_FIXABLE |

<a id="VulnerabilityReportFiltersImageType_CommonObjectReference"></a>

## VulnerabilityReportFiltersImageType

| Enum Values |
|-------------|
| DEPLOYED    |
| WATCHED     |

<a id="WatchImageResponseErrorType_CommonObjectReference"></a>

## WatchImageResponseErrorType

| Enum Values          |
|----------------------|
| NO_ERROR             |
| INVALID_IMAGE_NAME   |
| NO_VALID_INTEGRATION |
| SCAN_FAILED          |
