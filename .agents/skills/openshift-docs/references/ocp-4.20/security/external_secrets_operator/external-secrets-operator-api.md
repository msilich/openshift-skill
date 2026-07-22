<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

External Secrets Operator for Red Hat OpenShift uses the following two APIs to configure the `external-secrets` application deployment.

| Group                   | Version    | Kind                     |
|-------------------------|------------|--------------------------|
| `operator.openshift.io` | `v1alpha1` | `externalsecretsConfig`  |
| `operator.openshift.io` | `v1alpha1` | `externalsecretsmanager` |

The following list contains the External Secrets Operator for Red Hat OpenShift APIs:

- ExternalSecretsConfig

- ExternalSecretsManager

# applicationConfig

The `applicationConfig` object customizes the runtime behavior and deployment constraints of the operand. Use this section to control observability, define the operational scope, and configure webhook specifics. Additionally, you can tailor the deployment to your infrastructure requirements.

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Field</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Description</th>
<th style="text-align: left;">Default</th>
<th style="text-align: left;">Validation</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>logLevel</code></p></td>
<td style="text-align: left;"><p><em>integer</em></p></td>
<td style="text-align: left;"><p><code>logLevel</code> supports a range of values as defined in the <a href="https://github.com/kubernetes/community/blob/master/contributors/devel/sig-instrumentation/logging.md#what-method-to-use">kubernetes logging guidelines</a>.</p></td>
<td style="text-align: left;"><p>1</p></td>
<td style="text-align: left;"><p>The maximum range value is 5</p>
<p>The minimum range value is 1</p>
<p>Optional</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>operatingNamespace</code></p></td>
<td style="text-align: left;"><p><em>string</em></p></td>
<td style="text-align: left;"><p><code>operatingNamespace</code> restricts the <code>external-secrets</code> operand operations to the provided namespace. Enabling this field disables <code>ClusterSecretStore</code> and <code>ClusterExternalSecret</code>.</p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><p>The maximum length is 63</p>
<p>The minimum length is 1</p>
<p>Optional</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>webhookConfig</code></p></td>
<td style="text-align: left;"><p><em>object</em></p></td>
<td style="text-align: left;"><p><code>webhookConfig</code> configures webhook specifics of the <code>external-secrets</code> operand.</p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>resources</code></p></td>
<td style="text-align: left;"><p><a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.31/#resourcerequirements-v1-core"><em>ResourceRequirements</em></a></p></td>
<td style="text-align: left;"><p><code>resources</code> defines the resource requirements. You cannot change the value of this field after setting it initially. For more information, see <a href="https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/">https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/</a></p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><p>Optional</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>affinity</code></p></td>
<td style="text-align: left;"><p><a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.31/#affinity-v1-core"><em>Affinity</em></a></p></td>
<td style="text-align: left;"><p><code>affinity</code> sets the scheduling affinity rules. For more information, see <a href="https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/">https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/</a></p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><p>Optional</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>tolerations</code></p></td>
<td style="text-align: left;"><p><a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.31/#toleration-v1-core"><em>Toleration</em></a> <em>array</em></p></td>
<td style="text-align: left;"><p><code>tolerations</code> sets the pod tolerations. For more information, see <a href="https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/">https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/</a></p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><p>The maximum number of items is 50</p>
<p>The minimum number of items is 0</p>
<p>Optional</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>nodeSelector</code></p></td>
<td style="text-align: left;"><p><em>object (keys:string, values:string)</em></p></td>
<td style="text-align: left;"><p><code>nodeSelector</code> defines the scheduling criteria by using node labels. For more information, see <a href="https://kubernetes.io/docs/concepts/configuration/assign-pod-node/">https://kubernetes.io/docs/concepts/configuration/assign-pod-node/</a></p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><p>The maximum number of properties is 50</p>
<p>The minimum number of properties is 0</p>
<p>Optional</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>proxy</code></p></td>
<td style="text-align: left;"><p><em>object (keys:string, values:string)</em></p></td>
<td style="text-align: left;"><p><code>proxy</code> sets the proxy configurations available in operand containers managed by the Operator as environment variables.</p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><p>Optional</p></td>
</tr>
</tbody>
</table>

# bitwardenSecretManagerProvider

To enable the Bitwarden secrets manager provider and set up the additional service required to connect to the Bitwarden server, you can configure the `bitwardenSecretManagerProvider` field.

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Field</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Description</th>
<th style="text-align: left;">Default</th>
<th style="text-align: left;">Validation</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>mode</code></p></td>
<td style="text-align: left;"><p><em>string</em></p></td>
<td style="text-align: left;"><p><code>mode</code> field enables the <code>bitwardenSecretManagerProvider</code> provider state, which can be set to <code>Enabled</code> or <code>Disabled</code>. If set to <code>Enabled</code>, the Operator ensures the plugin is deployed and synchronized. If set to <code>Disabled</code>, the Bitwarden provider plugin reconciliation is disabled. The plugin and resources remain in their current state, and are not managed by the Operator.</p></td>
<td style="text-align: left;"><p><code>Disabled</code></p></td>
<td style="text-align: left;"><p>enum: [Enabled Disabled]</p>
<p>Optional</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>secretRef</code></p></td>
<td style="text-align: left;"><p><em>SecretReference</em></p></td>
<td style="text-align: left;"><p><code>SecretRef</code> specifies the Kubernetes secret that contains the TLS key pair for the Bitwarden server. If this reference is not provided and the <code>certManagerConfig</code> field is configured, the issuer defined in <code>certManagerConfig</code> generates the required certificate. The secret must use <code>tls.crt</code> for certificate, <code>tls.key</code> for the private key, and <code>ca.crt</code> for CA certificate.</p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><p>Optional</p></td>
</tr>
</tbody>
</table>

# certManagerConfig

You can integrate the External Secrets Operator for Red Hat OpenShift with cert-manager to secure internal webhooks. Use these settings to replace the default internal certificate management with cert-manager, specify custom issuers, and define certificate lifecycle and renewal policies.

| Field | Type | Description | Default | Validation |
|----|----|----|----|----|
| `mode` | *string* | `mode` specifies whether to use cert-manager for certificate management instead of the built-in `cert-controller` which can be indicated by setting either `Enabled` or `Disabled`. If set to `Enabled`, uses `cert-manager` for obtaining the certificates for the webhook server and other components. If set to `Disabled`, uses the `cert-controller` for obtaining the certificates for the webhook server. `Disabled` is the default behavior. |  | enum: \[Enabled Disabled\] |
| `injectAnnotations` | *string* | `injectAnnotations` adds the `cert-manager.io/inject-ca-from` annotation to the webhooks and custom resource definitions (CRDs) to automatically configure the webhook with the `cert-manager` Operator certificate authority (CA). This requires CA Injector to be enabled in `cert-manager` Operator. Set this field to `true` or `false`. When set, this field cannot be changed. | false | enum: \[true false\] |
| `issuerRef` | *ObjectReference* | `issuerRef` contains details of the referenced object used for obtaining certificates. The object must exist in the `external-secrets` namespace unless a cluster-scoped `cert-manager` Operator issuer is used. |  |  |
| `certificateDuration` | [*Duration*](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.31/#duration-v1-meta) | `certificateDuration` sets the validity period of the webhook certificate. | 8760h |  |
| `certificateRenewBefore` | [*Duration*](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.31/#duration-v1-meta) | `certificateRenewBefore` sets the ahead time to renew the webhook certificate before expiry. | 30m |  |

# certProvidersConfig

The `certProvidersConfig` defines the configuration for the certificate providers used to manage TLS certificates for webhook and plugins.

| Field | Type | Description | Default | Validation |
|----|----|----|----|----|
| `certManager` | *object* | `certManager` defines the configuration for `cert-manager` provider specifics. |  |  |

# commonConfigs

The `commonConfigs` specifies the common configurations available for all operands managed by the Operator.

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Field</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Description</th>
<th style="text-align: left;">Default</th>
<th style="text-align: left;">Validation</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>logLevel</code></p></td>
<td style="text-align: left;"><p><em>integer</em></p></td>
<td style="text-align: left;"><p><code>logLevel</code> supports the value range as defined in the <a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#time-v1-meta"><em>Time</em></a>.</p></td>
<td style="text-align: left;"><p>1</p></td>
<td style="text-align: left;"><p>The maximum number of log levels is 5.</p>
<p>The minimum number of log levels is 1.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>resources</code></p></td>
<td style="text-align: left;"><p><a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#resourcerequirements-v1-core"><em>ResourceRequirements</em></a>.</p></td>
<td style="text-align: left;"><p><code>resources</code> defines the resource requirements. This cannot be updated. See <a href="https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/">Resource Management for Pods and Containers</a>.</p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>affinity</code></p></td>
<td style="text-align: left;"><p><a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#affinity-v1-core"><em>affinity</em></a>.</p></td>
<td style="text-align: left;"><p><code>affinity</code> is used for setting scheduling affinity rules. See See <a href="https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/">Assigning Pods to Nodes</a>.</p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>tolerations</code></p></td>
<td style="text-align: left;"><p><a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#toleration-v1-core"><em>toleration array</em></a></p></td>
<td style="text-align: left;"><p><code>tolerations</code> sets the pod tolerations.</p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><p>The maximum number of items is 50.</p>
<p>The minimum number of items is 0.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>nodeSelector</code></p></td>
<td style="text-align: left;"><p><em>object (keys:string, values:string)</em></p></td>
<td style="text-align: left;"><p><code>nodeSelector</code> defines the scheduling criteria using node labels.</p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><p>The maximum number of properties is 50.</p>
<p>The minimum number of properties is 0.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>proxy</code></p></td>
<td style="text-align: left;"><p><em>proxyConfig</em></p></td>
<td style="text-align: left;"><p><code>proxy</code> sets the proxy configurations which are made avaiable in operand containers managed by the Operator as environment variables.</p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
</tbody>
</table>

# componentConfig

The `componentConfig` field defines configuration overrides for a specific `external-secrets` component.

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Field</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Description</th>
<th style="text-align: left;">Default</th>
<th style="text-align: left;">Validation</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>componentName</code></p></td>
<td style="text-align: left;"><p><em>string</em></p></td>
<td style="text-align: left;"><p><code>componentName</code> identifies which <code>external-secrets</code> component this configuration applies to. Valid values are <code>ExternalSecretsCoreController</code>, <code>Webhook</code>, <code>CertController</code>, and <code>BitwardenSDKServer</code>.</p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><p>Enum: [<code>ExternalSecretsCoreController</code>, <code>Webhook</code>, <code>CertController</code>, <code>BitwardenSDKServer</code>]</p>
<p>Required</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>deploymentConfigs</code></p></td>
<td style="text-align: left;"><p><em>object</em></p></td>
<td style="text-align: left;"><p><code>deploymentConfigs</code> specifies overrides for the Kubernetes Deployment resource of this component.</p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>overrideEnv</code></p></td>
<td style="text-align: left;"><p><strong>EnvVar</strong></p>
<p><em>array</em></p></td>
<td style="text-align: left;"><p><code>overrideEnv</code> specifies custom environment variables for this component’s container. These are merged with operator-managed environment variables, with user-defined values taking precedence. Environment variable names starting with <code>HOSTNAME</code>, <code>KUBERNETES_</code> or <code>EXTERNAL_SECRETS_</code> are reserved and are not allowed.</p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><p>The maximum number of items is 50.</p></td>
</tr>
</tbody>
</table>

# componentName

The `componentName` field represents the different external-secrets components that can have network policies applied.

| Field | Type | Description |
|----|----|----|
| `ExternalSecretsCoreController` | *object* | `ExternalSecretsCoreController` represents the `external-secret` component. |
| `BitwardenSDKServer` | *object* | `BitwardenSDKServer` represents the `bitwarden-sdk-server` component. |
| `Webhook` | *object* | `Webhook` represents the `external-secrets` webhook component. |
| `CertController` | *object* | `CertController` represents the `cert-controller` component. |

# condition

The `condition` object reports the current health and operational state of the External Secrets Operator for Red Hat OpenShift deployment. It provides a standardized status check by detailing the specific type of condition, its current status, and a message to verify deployment success or troubleshooting errors.

| Field | Type | Description |
|----|----|----|
| `type` | *string* | `type` contains the condition of the deployment. |
| `status` | [*ConditionStatus*](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#conditionstatus-v1-meta) | `status` contains the status of the condition of the deployment |
| `message` | *string* | `message` provides details on the state of the deployment |

# conditionalStatus

The `conditionalStatus` field holds information about the current state of the `external-secrets` deployment.

| Field | Type | Description |
|----|----|----|
| `conditions` | *array* | `conditions` contains information on the current state of the deployment. |

# configMapKeyReference

The `configMapKeyReference` specifies a specific key in a ConfigMap.

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Field</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Description</th>
<th style="text-align: left;">Default</th>
<th style="text-align: left;">Validation</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>name</code></p></td>
<td style="text-align: left;"><p><em>string</em></p></td>
<td style="text-align: left;"><p><code>name</code> specifies the name of the ConfigMap resource being referred to.</p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><p>The maximum length of the name is 253 characters.</p>
<p>The minimum length of the name is 1 character.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>key</code></p></td>
<td style="text-align: left;"><p><em>string</em></p></td>
<td style="text-align: left;"><p><code>key</code> specifies the specific key to be used in the ConfigMap. When ommitted, defaults to <code>ca-bundle.crt</code>.</p></td>
<td style="text-align: left;"><p><code>ca-bundle.crt</code></p></td>
<td style="text-align: left;"><p>The maximum length of the key is 253 characters.</p>
<p>The minimum length of the key is 1 character.</p>
<p>The pattern is: <code>^[-._a-zA-Z0-9]+$</code></p></td>
</tr>
</tbody>
</table>

# controllerConfig

The `controllerConfig` specifies the configurations used by the controller when installing the `external-secrets` operand and the plugins.

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Field</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Description</th>
<th style="text-align: left;">Default</th>
<th style="text-align: left;">Validation</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>certProvider</code></p></td>
<td style="text-align: left;"><p><em>string</em></p></td>
<td style="text-align: left;"><p><code>certProvider</code> defines the configuration for the certificate providers used to manage TLS certificates for webhook and plugins.</p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>labels</code></p></td>
<td style="text-align: left;"><p><em>object (keys:string, values:string)</em></p></td>
<td style="text-align: left;"><p><code>labels</code> field applies labels to all resources created for the <code>external-secrets</code> operand deployment.</p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><p>The maximum number of properties is 20.</p>
<p>The minimum number of properties is 0.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>annotations</code></p></td>
<td style="text-align: left;"><p><em>object (keys:string, values:string)</em></p></td>
<td style="text-align: left;"><p><code>annotations</code> add custom annotations to all the resources created for the <code>external-secrets</code> deployment. The annotations are merged with any default annotations set by the Operator. User-specified annotations take precedence over defaults in case of conflicts. Annotation keys containing the reserved domains <code>kubernetes.io/</code>, <code>openshift.io/</code>, <code>k8s.io/</code>, or <code>cert-manager.io/</code> (including subdomains like <code>*.kubernetes.io/</code>) are not allowed.</p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><p>The maximum number of annotations is 20.</p>
<p>The minimum number of annotations is 0.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>networkPolicies</code></p></td>
<td style="text-align: left;"><p><em>networkPolicy array</em></p></td>
<td style="text-align: left;"><p><code>networkPolicies</code> specifies the list of network policy configurations to be applied to the <code>external-secrets</code> pods. Each entry allows specifying a name for the generated <code>NetworkPolicy</code> object, along with its full Kubernetes <code>NetworkPolicy</code> definition. The Operator prepends <code>eso-user-</code> to the provided name when creating the Kubernetes object. If this field is not provided, <code>external-secrets</code> components are isolated with <code>deny-all</code> network policies, which prevents proper operation.</p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><p>The maximum number of items is 50.</p>
<p>The minimum number of items is 0.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>componentConfigs</code></p></td>
<td style="text-align: left;"><p><em>ComponentConfig array</em></p></td>
<td style="text-align: left;"><p><code>componentConfigs</code> allows specifying deployment-level configuration overrides for individual <code>external-secrets</code> components. This field enables fine-grained control over deployment settings for each component independently. Each component can have only one configuration entry.</p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><p>The maximum number of items is 4.</p>
<p>The minimum number of items is 0.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>trustedCABundle</code></p>
<p><strong>ConfigMapKeyReference</strong></p></td>
<td style="text-align: left;"><p><em>object</em></p></td>
<td style="text-align: left;"><p><code>trustedCABundle</code> references a ConfigMap containing PEM-encoded CA certificates for the <code>external-secrets</code> core controller to trust when making outbound TLS connections. If specified, this bundle is used for all outbound TLS traffic, including connections to external secret management systems and configured proxies.</p>
<p>The ConfigMap must exist in the <code>external-secrets</code> Operand namespace and must not carry the CNO inject-trusted-cabundle label when proxy is configured. When omitted, external providers use standard system certificates. When proxy is configured, proxy TLS connections use the operator-managed OpenShift Container Platform trusted CA bundle injected by the Cluster Network Operator.</p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
</tbody>
</table>

# controllerStatus

The `controllerStatus` field tracks the health and synchronization state of the individual controllers managed by the Operator. It identifies each controller by name, details its current operational conditions, and verifies that the controller is processing the latest configuration version.

| Field | Type | Description | Default | Validation |
|----|----|----|----|----|
| `name` | *string* | `name` specifies the name of the controller for which the observed condition is recorded. |  |  |
| `conditions` | *array* | `conditions` contains information about the current state of the External Secrets Operator controllers. |  |  |
| `observedGeneration` | *integer* | `observedGeneration` represents the `.metadata.generation` on the observed resource. |  | The minimum number of observed resources is 0. |

# deploymentConfig

The `deploymentConfig` field defines configuration overrides for a Kubernetes Deployment resource.

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Field</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Description</th>
<th style="text-align: left;">Default</th>
<th style="text-align: left;">Validation</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>revisionHistoryLimit</code></p></td>
<td style="text-align: left;"><p><em>integer</em></p></td>
<td style="text-align: left;"><p><code>revisionHistoryLimit</code> specifies the number of old <code>ReplicaSets</code> to retain for rollback purposes. This allows rolling back to previous deployment versions using the command <code>oc rollout undo</code>. Must be at least 1 to ensure rollback capability.</p></td>
<td style="text-align: left;"><p>10</p></td>
<td style="text-align: left;"><p>The maximum value is 50.</p>
<p>The minimum value is 1.</p></td>
</tr>
</tbody>
</table>

# externalSecretsConfig

The `externalSecretsConfig` object defines the configuration and information for the managed `external-secrets` operand deployment. Set the name to `cluster` as `externalSecretsConfig` object allows only one instance per cluster.

Creating an `externalSecretsConfig` object triggers the deployment of the `external-secrets` operand and maintains the desired state.

| Field | Type | Description |
|----|----|----|
| `apiVersion` | *string* | The `apiVersion` specifies the version of the schema in use, which is `operator.openshift.io/v1alpha1`. |
| `kind` | *string* | `kind` specifies the type of the object, which is `externalSecrets` for this object. |
| `metadata` | [*ObjectMeta*](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.31/#objectmeta-v1-meta) | Refer to Kubernetes API documentation for details about the `metadata` fields. |
| `spec` | *object* | `spec` contains the specifications of the desired behavior of the `externalSecrets` object. |
| `status` | *object* | `status` displays the most recently observed status of the `externalSecrets` object. |

# externalSecretsConfigList

The `externalSecretsConfigList` object fetches the list of `externalSecretsConfig` objects.

| Field | Type | Description |
|----|----|----|
| `apiVersion` | *string* | The `apiVersion` specifies the version of the schema in use, which is `operator.openshift.io/v1alpha1` |
| `kind` | *string* | `kind` specifies the type of the object, which is `externalSecretsList` for this API. |
| `metadata` | [*ListMeta*](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.31/#listmeta-v1-meta) | Refer to Kubernetes API documentation for details about the `metadata` fields. |
| `items` | *array* | `Items` contains a list of `externalSecrets` objects. |

# externalSecretsConfigSpec

The `externalSecretsConfigSpec` field defines the desired behavior of the `externalSecrets` object.

| Field | Type | Description |
|----|----|----|
| `appConfig` | *object* | `appConfig` configures the behavior of the `external-secrets` operand. |
| `plugins` | *object* | `plugins` configures the optional provider plugins. |
| `controllerConfig` | *object* | `controllerConfig` configures the controller to set up defaults that enable `external-secrets` operand. |

# externalSecretsConfigStatus

The `externalSecretsConfigStatus` field shows the most recently observed status of the `externalSecretsConfig` Object.

| Field | Type | Description |
|----|----|----|
| `conditions` | [*Condition*](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#condition-v1-meta) *array* | `conditions` contains information about the current state of deployment. |
| `externalSecretsImage` | *string* | `externalSecretsImage` specifies the image name and tag used for deploy `external-secrets` operand. |
| `bitwardenSDKServerImage` | *string* | `bitwardenSDKServerImage` specifies the name of the image and tag used for deploying the `bitwarden-sdk-server`. |

# externalSecretsManager

The `externalSecretsManager` object defines the configuration and information of deployments managed by the External Secrets Operator. Set the name to `cluster` as this allows only one instance of `externalSecretsManager` per cluster. You can configure global options by using `externalSecretsManager`. This serves as a centralized configuration for managing multiple controllers of the Operator. The Operator automatically creates the `externalSecretsManager` object during installation.

| Field | Type | Description |
|----|----|----|
| `apiVersion` | *string* | The `apiVersion` specifies the version of the schema in use, which is `operator.openshift.io/v1alpha1`. |
| `kind` | *string* | `kind` specifies the type of the object, which is `externalSecretsManager` for this Object. |
| `metadata` | [*ObjectMeta*](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.31/#objectmeta-v1-meta) | Refer to Kubernetes API documentation for details about the `metadata` fields. |
| `spec` | *object* | `spec` contains specifications of the desired behavior. |
| `status` | *object* | `status` displays the most recently observed state of the controllers in the External Secrets Operator. |

# externalSecretsManagerList

The `externalSecretsManagerList` object fetches the list of `externalSecretsManager` objects.

| Field | Type | Description | Default | Validation |
|----|----|----|----|----|
| `apiVersion` | *string* | The `apiVersion` specifies the version of the schema in use, which is `operator.openshift.io/v1alpha1`. |  |  |
| `kind` | *string* | `kind` specifies the type of the object, which is `externalSecretsManagerList` for this API. |  |  |
| `metadata` | [*ListMeta*](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.31/#listmeta-v1-meta) | Refer to Kubernetes API documentation for details about the `metadata` fields. |  |  |
| `items` | *array* |  |  |  |

# externalSecretsManagerSpec

The `externalSecretsManagerSpec` field defines the desired behavior of the `externalSecretsManager` object.

| Field | type | Description | Default | Validation |
|----|----|----|----|----|
| `globalConfig` | *object* | `globalConfig` configures the behavior of deployments that External Secrets Operator manages. |  | Optional |

# externalSecretsManagerStatus

The `externalSecretsManagerStatus` field shows the most recently observed status of the `externalSecretsManager` object.

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Field</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Description</th>
<th style="text-align: left;">Default</th>
<th style="text-align: left;">Validation</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>controllerStatuses</code></p></td>
<td style="text-align: left;"><p><em>array</em></p></td>
<td style="text-align: left;"><p><code>controllerStatuses</code> holds the observed conditions of the controllers used by the Operator.</p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>lastTransitionTime</code></p></td>
<td style="text-align: left;"><p><a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#time-v1-meta"><em>Time</em></a></p></td>
<td style="text-align: left;"><p><code>lastTransitionTime</code> records the most recent time the status of the condition changed.</p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><p>Format: date-time</p>
<p>Type: string</p></td>
</tr>
</tbody>
</table>

# Feature

The `Feature` field configures an optional capability that is applied by the `external-secrets-operator` across its managed deployments.

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Field</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Description</th>
<th style="text-align: left;">Default</th>
<th style="text-align: left;">Validation</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>name</code></p></td>
<td style="text-align: left;"><p><strong>FeatureName</strong></p>
<p><em>string</em></p></td>
<td style="text-align: left;"><p><code>name</code> identifies the optional feature to configure. Currently, the only supported value is <code>UnsafeAllowGenericTargets</code>.</p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><p>Enum: [<code>UnsafeAllowGenericTargets</code>]</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>mode</code></p></td>
<td style="text-align: left;"><p><strong>mode</strong></p>
<p><em>string</em></p></td>
<td style="text-align: left;"><p><code>mode</code> mode controls whether the feature is active. When set to <code>Enabled</code>, the Operator applies the configuration associated with the named feature to the relevant managed deployments. For <code>UnsafeAllowGenericTargets</code>, this passes the <code>--unsafe-allow-generic-targets</code> flag to the <code>external-secrets</code> core controller, allowing <code>ExternalSecret</code> resources to target Kubernetes resources other than <code>Secrets</code>. For example, ConfigMaps or custom resources.</p>
<div class="warning">
<div class="title">
&#10;</div>
<p>Generic targets require additional RBAC permissions on the affected operand; enabling this feature without the appropriate permissions will cause reconciliation failures.</p>
</div></td>
<td style="text-align: left;"><p>Disabled</p></td>
<td style="text-align: left;"><p>Enum:[<code>Enabled</code> <code>Disabled</code>]</p></td>
</tr>
</tbody>
</table>

# featureName

The `featureName` field identifies an optional feature that can be configured on the `ExternalSecretsManager` and applied by the `external-secrets-operator`.

| Field | Type | Description |
|----|----|----|
| `UnsafeAllowGenericTargets` | *object* | `UnsafeAllowGenericTargets` configures the `external-secrets` core controller to run with the `--unsafe-allow-generic-targets` startup flag, which allows `ExternalSecret` resources to sync data into Kubernetes resources other than `Secrets`. |

# globalConfig

The `globalConfig` field defines the baseline behavior and deployment parameters for the External Secrets Operator for Red Hat OpenShift. Use this section to apply labels to all managed resources and configure the logging verbosity. It also provides infrastructure-level controls to govern where and how the Operator is scheduled, alongside proxy settings for network compatibility.

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Field</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Description</th>
<th style="text-align: left;">Default</th>
<th style="text-align: left;">Validation</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>logLevel</code></p></td>
<td style="text-align: left;"><p><em>integer</em></p></td>
<td style="text-align: left;"><p><code>logLevel</code> supports a range of values as defined in the <a href="https://github.com/kubernetes/community/blob/master/contributors/devel/sig-instrumentation/logging.md#what-method-to-use">kubernetes logging guidelines</a>.</p></td>
<td style="text-align: left;"><p>1</p></td>
<td style="text-align: left;"><p>The maximum range value is 5</p>
<p>The minimum range value is 1</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>resources</code></p></td>
<td style="text-align: left;"><p><a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.31/#resourcerequirements-v1-core"><em>ResourceRequirements</em></a></p></td>
<td style="text-align: left;"><p><code>resources</code> defines the resource requirements. You cannot change the value of this field after setting it initially. For more information, see <a href="https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/">https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/</a></p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>affinity</code></p></td>
<td style="text-align: left;"><p><a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.31/#affinity-v1-core"><em>Affinity</em></a></p></td>
<td style="text-align: left;"><p><code>affinity</code> sets the scheduling affinity rules. For more information, see <a href="https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/">https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/</a></p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>tolerations</code></p></td>
<td style="text-align: left;"><p><a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.31/#toleration-v1-core"><em>Toleration</em></a> <em>array</em></p></td>
<td style="text-align: left;"><p><code>tolerations</code> sets the pod tolerations. For more information, see <a href="https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/">https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/</a></p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><p>The maximum number of items is 50</p>
<p>The minimum number of items is 0</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>nodeSelector</code></p></td>
<td style="text-align: left;"><p><em>object (keys:string, values:string)</em></p></td>
<td style="text-align: left;"><p><code>nodeSelector</code> defines the scheduling criteria by using the node labels. For more information, see <a href="https://kubernetes.io/docs/concepts/configuration/assign-pod-node/">https://kubernetes.io/docs/concepts/configuration/assign-pod-node/</a></p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><p>The maximum number of properties is 50</p>
<p>The minimum number of properties is 0</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>proxy</code></p></td>
<td style="text-align: left;"><p><em>object</em></p></td>
<td style="text-align: left;"><p><code>proxy</code> sets the proxy configurations available in the operand containers managed by the Operator as environment variables.</p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>labels</code></p></td>
<td style="text-align: left;"><p><em>object (keys:string, values:string)</em></p></td>
<td style="text-align: left;"><p><code>labels</code> applies to all resources created by the Operator. This field can have a maximum of 20 entries</p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><p>The maximum number of properties is 20</p>
<p>The minimum number of properties is 0</p></td>
</tr>
</tbody>
</table>

# managementState

The `managementState` field controls whether the Operator manages the resource lifecycle.

| Field | Type | Description |
|----|----|----|
| `Managed` | *string* | `ManagementStateManaged` indicates the Operator is responsible for the resource lifecycle. |
| `Unmanaged` | *string* | `ManagementStateUnmanaged` indicates the user is responsible for the resource lifecycle. |

# mode

The `mode` field indicates the operational state of the optional features.

| Field | Type | Description |
|----|----|----|
| `Enabled` | *string* | `Enabled` indicates the optional configuration is enabled. |
| `Disabled` | *string* | `Disabled` indicates the optional configuration is disabled. |

# networkPolicy

The `networkPolicy` field represents a custom network policy configuration for operator-managed components. The field includes a name for identification and the network policy rules to be enforced.

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Field</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Description</th>
<th style="text-align: left;">Default</th>
<th style="text-align: left;">Validation</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>name</code></p></td>
<td style="text-align: left;"><p><em>string</em></p></td>
<td style="text-align: left;"><p><code>name</code> is the logical identifier for this network policy entry. The Operator prepends <code>eso-user-</code> to this value when creating the Kubernetes <code>NetworkPolicy</code> object, for example <code>allow-egress</code> becomes <code>eso-user-allow-egress</code>. The maximum length is 243 to accommodate the prefix within the 253-character Kubernetes name limit.</p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><p>The maximum length is 243 characters.</p>
<p>The minimum length is 1. character.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>componentName</code></p></td>
<td style="text-align: left;"><p><em>string</em></p></td>
<td style="text-align: left;"><p><code>componentName</code> specifies which external-secrets component this network policy applies to.</p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><p>Enum:[<code>ExternalSecretsCoreController</code> <code>BitwardenSDIServer</code>]</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>egress</code> <strong>NetworkPolicyegressRule</strong></p></td>
<td style="text-align: left;"><p><em>array</em></p></td>
<td style="text-align: left;"><p><code>egress</code> is a list of egress rules to be applied to the selected pods. Outgoing traffic is allowed if there are no <code>NetworkPolicies</code> selecting the pod, and cluster policy otherwise allows the traffic, or if the traffic matches at least one egress rule across all the <code>NetworkPolicy</code> objects whose <code>podSelector</code> matches the pod. If this field is empty, then this <code>NetworkPolicy</code> limits all outgoing traffic and serves solely to ensure that the pods it selects are isolated by default. The Operator automatically handles ingress rules based on the current running ports.</p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
</tbody>
</table>

# objectReference

The `ObjectReference` object acts as a pointer to a specific Kubernetes resource. It uniquely identifies the target by requiring its name, and optionally, helps scope the reference to a specific resource type and API group.

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Field</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Description</th>
<th style="text-align: left;">Default</th>
<th style="text-align: left;">Validation</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>name</code></p></td>
<td style="text-align: left;"><p><em>string</em></p></td>
<td style="text-align: left;"><p><code>name</code> specifies the name of the resource being referred to.</p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><p>The maximum length is 253 characters.</p>
<p>The minimum length is 1 character.</p>
<p>Required</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>kind</code></p></td>
<td style="text-align: left;"><p><em>string</em></p></td>
<td style="text-align: left;"><p><code>kind</code> specifies the kind of the resource being referred to.</p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><p>The maximum length is 253 characters.</p>
<p>The minimum length is 1 character.</p>
<p>Optional</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>group</code></p></td>
<td style="text-align: left;"><p><em>string</em></p></td>
<td style="text-align: left;"><p><code>group</code> specifies the group of the resource being referred to.</p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><p>The maximum length is 253 characters.</p>
<p>The minimum length is 1 character.</p>
<p>Optional</p></td>
</tr>
</tbody>
</table>

# pluginsConfig

The `pluginsConfig` configures the optional plugins.

| Field | Type | Description | Default | Validation |
|----|----|----|----|----|
| `bitwardenSecretManagerProvider` | *object* | `bitwardenSecretManagerProvider` enables the `bitwarden-secrets-manager` provider plugin for connecting with the 'bitwarden-secrets-manager'. |  | Optional |

# proxyConfig

The `proxyConfig` object defines the network proxy settings that the Operator injects into managed containers as environment variables. Use this configuration to ensure proper connectivity in restricted network environments, or to bypass the proxy and connect directly.

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Field</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Description</th>
<th style="text-align: left;">Default</th>
<th style="text-align: left;">Validation</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>httpProxy</code></p></td>
<td style="text-align: left;"><p><em>string</em></p></td>
<td style="text-align: left;"><p>The <code>httpProxy</code> field contains the URL of the proxy for HTTP requests. This field can have a maximum of 2048 characters.</p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><p>The maximum length is 2048 characters.</p>
<p>The minimum length is 0 characters.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>httpsProxy</code></p></td>
<td style="text-align: left;"><p><em>string</em></p></td>
<td style="text-align: left;"><p>The <code>httpsProxy</code> field contains the URL of the proxy for HTTPS requests. This field can have a maximum of 2048 characters.</p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><p>The maximum length is 2048 characters.</p>
<p>The minimum length is 0 characters.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>noProxy</code></p></td>
<td style="text-align: left;"><p><em>string</em></p></td>
<td style="text-align: left;"><p>The <code>noProxy</code> field is a comma-separated list of hostnames, classless inter-domain routings (CIDRs), and IP addresses or a combination of the three for which the proxy should not be used. This field can have a maximum of 4096 characters.</p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><p>The maximum length is 4096 characters.</p>
<p>The minimum length is 0 characters.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>networkPolicyProvisioning</code></p>
<p><strong>ManagementState</strong></p></td>
<td style="text-align: left;"><p><em>string</em></p></td>
<td style="text-align: left;"><p>The <code>networkPolicyProvisioning</code> field defines the management strategy for the proxy egress rule. When set to <code>Managed</code>, the Operator automatically provisions and maintains a <code>NetworkPolicy</code> allowing traffic to the configured proxy. If no proxy is configured, a <code>NetworkPolicy</code> is not created regardless of this setting.</p></td>
<td style="text-align: left;"><p>Managed</p></td>
<td style="text-align: left;"><p>Enum:[<code>Managed</code> <code>Unmanaged</code>]</p></td>
</tr>
</tbody>
</table>

# secretReference

The `secretReference` field refers to a secret with the given name in the same namespace where it used.

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Field</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Description</th>
<th style="text-align: left;">Default</th>
<th style="text-align: left;">Validation</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>name</code></p></td>
<td style="text-align: left;"><p><em>string</em></p></td>
<td style="text-align: left;"><p><code>name</code> specifies the name of the secret resource being referred to.</p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><p>The maximum length is 253.</p>
<p>The minimum length is 1.</p></td>
</tr>
</tbody>
</table>

# webhookConfig

The `webhookConfig` field configures the specifics of the `external-secrets` application webhook.

| Field | Type | Description | Default | Validation |
|----|----|----|----|----|
| `certificateCheckInterval` | [*Duration*](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.31/#duration-v1-meta) | `certificateCheckInterval` configures the polling interval to check certificate validity. | 5m | Optional |
