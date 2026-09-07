<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Description
SecurityContextConstraints governs the ability to make requests that affect the SecurityContext that will be applied to a container. For historical reasons SCC was exposed under the core Kubernetes API group. That exposure is deprecated and will be removed in a future release - users should instead use the security.openshift.io group to manage SecurityContextConstraints.

Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).

Type
`object`

Required
- `allowHostDirVolumePlugin`

- `allowHostIPC`

- `allowHostNetwork`

- `allowHostPID`

- `allowHostPorts`

- `allowPrivilegedContainer`

- `readOnlyRootFilesystem`

# Specification

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
<td style="text-align: left;"><p><code>allowHostDirVolumePlugin</code></p></td>
<td style="text-align: left;"><p><code>boolean</code></p></td>
<td style="text-align: left;"><p>allowHostDirVolumePlugin determines if the policy allow containers to use the HostDir volume plugin</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>allowHostIPC</code></p></td>
<td style="text-align: left;"><p><code>boolean</code></p></td>
<td style="text-align: left;"><p>allowHostIPC determines if the policy allows host ipc in the containers.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>allowHostNetwork</code></p></td>
<td style="text-align: left;"><p><code>boolean</code></p></td>
<td style="text-align: left;"><p>allowHostNetwork determines if the policy allows the use of HostNetwork in the pod spec.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>allowHostPID</code></p></td>
<td style="text-align: left;"><p><code>boolean</code></p></td>
<td style="text-align: left;"><p>allowHostPID determines if the policy allows host pid in the containers.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>allowHostPorts</code></p></td>
<td style="text-align: left;"><p><code>boolean</code></p></td>
<td style="text-align: left;"><p>allowHostPorts determines if the policy allows host ports in the containers.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>allowPrivilegeEscalation</code></p></td>
<td style="text-align: left;"><p>``</p></td>
<td style="text-align: left;"><p>allowPrivilegeEscalation determines if a pod can request to allow privilege escalation. If unspecified, defaults to true.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>allowPrivilegedContainer</code></p></td>
<td style="text-align: left;"><p><code>boolean</code></p></td>
<td style="text-align: left;"><p>allowPrivilegedContainer determines if a container can request to be run as privileged.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>allowedCapabilities</code></p></td>
<td style="text-align: left;"><p>``</p></td>
<td style="text-align: left;"><p>allowedCapabilities is a list of capabilities that can be requested to add to the container. Capabilities in this field maybe added at the pod author’s discretion. You must not list a capability in both AllowedCapabilities and RequiredDropCapabilities. To allow all capabilities you may use '*'.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>allowedFlexVolumes</code></p></td>
<td style="text-align: left;"><p>``</p></td>
<td style="text-align: left;"><p>allowedFlexVolumes is a whitelist of allowed Flexvolumes. Empty or nil indicates that all Flexvolumes may be used. This parameter is effective only when the usage of the Flexvolumes is allowed in the "Volumes" field.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>allowedUnsafeSysctls</code></p></td>
<td style="text-align: left;"><p>``</p></td>
<td style="text-align: left;"><p>allowedUnsafeSysctls is a list of explicitly allowed unsafe sysctls, defaults to none. Each entry is either a plain sysctl name or ends in "*" in which case it is considered as a prefix of allowed sysctls. Single \* means all unsafe sysctls are allowed. Kubelet has to whitelist all allowed unsafe sysctls explicitly to avoid rejection.</p>
<p>Examples: e.g. "foo/*" allows "foo/bar", "foo/baz", etc. e.g. "foo.\*" allows "foo.bar", "foo.baz", etc.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>apiVersion</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <a href="https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources">https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>defaultAddCapabilities</code></p></td>
<td style="text-align: left;"><p>``</p></td>
<td style="text-align: left;"><p>defaultAddCapabilities is the default set of capabilities that will be added to the container unless the pod spec specifically drops the capability. You may not list a capabiility in both DefaultAddCapabilities and RequiredDropCapabilities.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>defaultAllowPrivilegeEscalation</code></p></td>
<td style="text-align: left;"><p>``</p></td>
<td style="text-align: left;"><p>defaultAllowPrivilegeEscalation controls the default setting for whether a process can gain more privileges than its parent process.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>forbiddenSysctls</code></p></td>
<td style="text-align: left;"><p>``</p></td>
<td style="text-align: left;"><p>forbiddenSysctls is a list of explicitly forbidden sysctls, defaults to none. Each entry is either a plain sysctl name or ends in "*" in which case it is considered as a prefix of forbidden sysctls. Single \* means all sysctls are forbidden.</p>
<p>Examples: e.g. "foo/<strong>" forbids "foo/bar", "foo/baz", etc. e.g. "foo.</strong>" forbids "foo.bar", "foo.baz", etc.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>fsGroup</code></p></td>
<td style="text-align: left;"><p>``</p></td>
<td style="text-align: left;"><p>fsGroup is the strategy that will dictate what fs group is used by the SecurityContext.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>groups</code></p></td>
<td style="text-align: left;"><p>``</p></td>
<td style="text-align: left;"><p>The groups that have permission to use this security context constraints</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>kind</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <a href="https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds">https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>metadata</code></p></td>
<td style="text-align: left;"><p><a href="../objects/index.xml#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta"><code>ObjectMeta</code></a></p></td>
<td style="text-align: left;"><p>Standard object’s metadata. More info: <a href="https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata">https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>priority</code></p></td>
<td style="text-align: left;"><p>``</p></td>
<td style="text-align: left;"><p>priority influences the sort order of SCCs when evaluating which SCCs to try first for a given pod request based on access in the Users and Groups fields. The higher the int, the higher priority. An unset value is considered a 0 priority. If scores for multiple SCCs are equal they will be sorted from most restrictive to least restrictive. If both priorities and restrictions are equal the SCCs will be sorted by name.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>readOnlyRootFilesystem</code></p></td>
<td style="text-align: left;"><p><code>boolean</code></p></td>
<td style="text-align: left;"><p>readOnlyRootFilesystem when set to true will force containers to run with a read only root file system. If the container specifically requests to run with a non-read only root file system the SCC should deny the pod. If set to false the container may run with a read only root file system if it wishes but it will not be forced to.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>requiredDropCapabilities</code></p></td>
<td style="text-align: left;"><p>``</p></td>
<td style="text-align: left;"><p>requiredDropCapabilities are the capabilities that will be dropped from the container. These are required to be dropped and cannot be added.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>runAsUser</code></p></td>
<td style="text-align: left;"><p>``</p></td>
<td style="text-align: left;"><p>runAsUser is the strategy that will dictate what RunAsUser is used in the SecurityContext.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>seLinuxContext</code></p></td>
<td style="text-align: left;"><p>``</p></td>
<td style="text-align: left;"><p>seLinuxContext is the strategy that will dictate what labels will be set in the SecurityContext.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>seccompProfiles</code></p></td>
<td style="text-align: left;"><p>``</p></td>
<td style="text-align: left;"><p>seccompProfiles lists the allowed profiles that may be set for the pod or container’s seccomp annotations. An unset (nil) or empty value means that no profiles may be specifid by the pod or container. The wildcard '*' may be used to allow all profiles. When used to generate a value for a pod the first non-wildcard profile will be used as the default.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>supplementalGroups</code></p></td>
<td style="text-align: left;"><p>``</p></td>
<td style="text-align: left;"><p>supplementalGroups is the strategy that will dictate what supplemental groups are used by the SecurityContext.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>userNamespaceLevel</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>userNamespaceLevel determines if the policy allows host users in containers. Valid values are "AllowHostLevel", "RequirePodLevel", and omitted. When "AllowHostLevel" is set, a pod author may set <code>hostUsers</code> to either <code>true</code> or <code>false</code>. When "RequirePodLevel" is set, a pod author must set <code>hostUsers</code> to <code>false</code>. When omitted, the default value is "AllowHostLevel".</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>users</code></p></td>
<td style="text-align: left;"><p>``</p></td>
<td style="text-align: left;"><p>The users who have permissions to use this security context constraints</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>volumes</code></p></td>
<td style="text-align: left;"><p>``</p></td>
<td style="text-align: left;"><p>volumes is a white list of allowed volume plugins. FSType corresponds directly with the field names of a VolumeSource (azureFile, configMap, emptyDir). To allow all volumes you may use "*". To allow no volumes, set to ["none"].</p></td>
</tr>
</tbody>
</table>

# API endpoints

The following API endpoints are available:

- `/apis/security.openshift.io/v1/securitycontextconstraints`

  - `DELETE`: delete collection of SecurityContextConstraints

  - `GET`: list objects of kind SecurityContextConstraints

  - `POST`: create SecurityContextConstraints

- `/apis/security.openshift.io/v1/watch/securitycontextconstraints`

  - `GET`: watch individual changes to a list of SecurityContextConstraints. deprecated: use the 'watch' parameter with a list operation instead.

- `/apis/security.openshift.io/v1/securitycontextconstraints/{name}`

  - `DELETE`: delete SecurityContextConstraints

  - `GET`: read the specified SecurityContextConstraints

  - `PATCH`: partially update the specified SecurityContextConstraints

  - `PUT`: replace the specified SecurityContextConstraints

- `/apis/security.openshift.io/v1/watch/securitycontextconstraints/{name}`

  - `GET`: watch changes to an object of kind SecurityContextConstraints. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.

## /apis/security.openshift.io/v1/securitycontextconstraints

HTTP method
`DELETE`

Description
delete collection of SecurityContextConstraints

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Status`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`GET`

Description
list objects of kind SecurityContextConstraints

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`SecurityContextConstraintsList`](../objects/index.md#io-openshift-security-v1-SecurityContextConstraintsList) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`POST`

Description
create SecurityContextConstraints

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`SecurityContextConstraints`](securitycontextconstraints-security-openshift-io-v1.md#securitycontextconstraints-security-openshift-io-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`SecurityContextConstraints`](securitycontextconstraints-security-openshift-io-v1.md#securitycontextconstraints-security-openshift-io-v1) schema |
| 201 - Created | [`SecurityContextConstraints`](securitycontextconstraints-security-openshift-io-v1.md#securitycontextconstraints-security-openshift-io-v1) schema |
| 202 - Accepted | [`SecurityContextConstraints`](securitycontextconstraints-security-openshift-io-v1.md#securitycontextconstraints-security-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/security.openshift.io/v1/watch/securitycontextconstraints

HTTP method
`GET`

Description
watch individual changes to a list of SecurityContextConstraints. deprecated: use the 'watch' parameter with a list operation instead.

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`WatchEvent`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/security.openshift.io/v1/securitycontextconstraints/{name}

| Parameter | Type     | Description                            |
|-----------|----------|----------------------------------------|
| `name`    | `string` | name of the SecurityContextConstraints |

Global path parameters

HTTP method
`DELETE`

Description
delete SecurityContextConstraints

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
read the specified SecurityContextConstraints

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`SecurityContextConstraints`](securitycontextconstraints-security-openshift-io-v1.md#securitycontextconstraints-security-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PATCH`

Description
partially update the specified SecurityContextConstraints

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`SecurityContextConstraints`](securitycontextconstraints-security-openshift-io-v1.md#securitycontextconstraints-security-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PUT`

Description
replace the specified SecurityContextConstraints

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`SecurityContextConstraints`](securitycontextconstraints-security-openshift-io-v1.md#securitycontextconstraints-security-openshift-io-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`SecurityContextConstraints`](securitycontextconstraints-security-openshift-io-v1.md#securitycontextconstraints-security-openshift-io-v1) schema |
| 201 - Created | [`SecurityContextConstraints`](securitycontextconstraints-security-openshift-io-v1.md#securitycontextconstraints-security-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/security.openshift.io/v1/watch/securitycontextconstraints/{name}

| Parameter | Type     | Description                            |
|-----------|----------|----------------------------------------|
| `name`    | `string` | name of the SecurityContextConstraints |

Global path parameters

HTTP method
`GET`

Description
watch changes to an object of kind SecurityContextConstraints. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`WatchEvent`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema |
| 401 - Unauthorized | Empty |

HTTP responses
