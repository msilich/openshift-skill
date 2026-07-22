<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

You can customize the behavior of the External Secrets Operator for Red Hat OpenShift operand components by configuring custom annotations, deployment lifecycle settings, and environment variables through the `ExternalSecretsConfig` custom resource (CR).

These configurations provide administrators with fine-grained control over the external-secrets deployment.

You can customize the External Secrets Operator for Red Hat OpenShift operand by using the `ExternalSecretsConfig` custom resource (CR). The CR supports a set of deployment and runtime options, such as custom annotations, revision history limits, environment variables, resource limits, tolerations, and proxy settings—so you can control how the operand is deployed and run without editing the operand resources directly.

All supported options are defined in the `ExternalSecretsConfig` CR (for example under the `spec.controllerConfig` for controller-related settings). The Operator reconciles the operand from this CR. Changes made directly to operand resources are overwritten. Use the `ExternalSecretsConfig` CR as the only supported way to customize the operand.

For the complete list of fields and allowed values, see the `ExternalSecretsConfig` API reference in the External Secrets Operator for Red Hat OpenShift documentation.

<div>

<div class="title">

Additional resources

</div>

- [External Secrets Operator for Red Hat OpenShift APIs](external-secrets-operator-api.md#external-secrets-operator-api)

</div>

# Setting a log level for the External Secrets Operator for Red Hat OpenShift

You can configure the log verbosity for the lifecycle manager. You must adjust this setting to troubleshoot issues related to the installation, upgrade, or configuration of the operator itself, rather than secret synchronization.

<div>

<div class="title">

Prerequisites

</div>

- You have access to the cluster with `cluster-admin` privileges.

- You have created the `ExternalSecretsConfig` custom resource.

</div>

<div>

<div class="title">

Procedure

</div>

- Update the subscription object for the External Secrets Operator for Red Hat OpenShift to provide the verbosity level for the operator logs by running the following command:

  ``` terminal
  $ oc -n <external_secrets_operator_namespace> patch subscription openshift-external-secrets-operator --type='merge' -p '{"spec":{"config":{"env":[{"name":"OPERATOR_LOG_LEVEL","value":"<log_level>"}]}}}'
  ```

  where:

  external_secrets_operator_namespace
  Specifies the namespace where the Operator is installed.

  log_level
  Specifies the level of log detail. Values range from 1-5. The default is 2.

</div>

<div>

<div class="title">

Verification

</div>

1.  The External Secrets Operator pod is redeployed. Verify that the log level of the External Secrets Operator for Red Hat OpenShift is updated by running the following command:

    ``` terminal
    $ oc set env deploy/external-secrets-operator-controller-manager -n external-secrets-operator --list | grep -e OPERATOR_LOG_LEVEL -e container
    ```

    The following example verifies that the log level of the External Secrets Operator for Red Hat OpenShift is updated.

    ``` terminal
    # deployments/external-secrets-operator-controller-manager, container manager
    OPERATOR_LOG_LEVEL=2
    ```

2.  Verify that the log level of the External Secrets Operator for Red Hat OpenShift is updated by running the `oc logs` command:

    ``` terminal
    $ oc logs -n external-secrets-operator -f deployments/external-secrets-operator-controller-manager -c manager
    ```

</div>

# Setting a log level for the External Secrets Operator for Red Hat OpenShift operand

You can troubleshoot common issues, such as secret synchronization failures, provider authentication errors, or data formatting problems, by configuring the log verbosity for the core controller.

<div>

<div class="title">

Prerequisites

</div>

- You have access to the cluster with `cluster-admin` privileges.

- You have created the `ExternalSecretsConfig` custom resource.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Edit the `ExternalSecretsConfig` CR by running the following command:

    ``` terminal
    $ oc edit externalsecretsconfigs.operator.openshift.io cluster
    ```

2.  Set the log level value by editing the `spec.appConfig.logLevel` section:

    ``` yaml
    apiVersion: operator.openshift.io/v1alpha1
    kind: ExternalSecretsConfig
    ...
    spec:
      appConfig:
        logLevel: <log_level>
    ```

    where:

    log_level
    Supports the value range of 1-5. The log level gets mapped to the following operand support levels:

    - 1 - warnings

    - 2 - error logs

    - 3 - info logs

    - 4 and 5 - debug logs

3.  Save your changes and exit the editor.

</div>

# Configuring cert-manager for the external-secrets certificate requirements

You can optionally configure cert-manager to manage certificates for the External Secrets Operator for Red Hat OpenShift webhook and plugins. If you do not use cert-manager, the Operator automatically generates webhook certificates, but you must manually configure certificates for any plugins.

<div>

<div class="title">

Prerequisites

</div>

- You have access to the cluster with `cluster-admin` privileges.

- You have created the `ExternalSecretsConfig` custom resource.

- You have installed the cert-manager Operator for Red Hat OpenShift. For more information, see "Installing the cert-manager Operator for Red Hat OpenShift"

</div>

<div>

<div class="title">

Procedure

</div>

1.  Edit the `ExternalSecretsConfig` custom resource by running the following command:

    ``` terminal
    $  oc edit externalsecretsconfigs.operator.openshift.io cluster
    ```

2.  Configure `cert-manager` by editing the `spec.controllerConfig.certProvider.certManager` section as follows:

    ``` yaml
    apiVersion: operator.openshift.io/v1alpha1
    kind: ExternalSecretsConfig
    ...
    spec:
      controllerConfig:
        certProvider:
          certManager:
            injectAnnotations: "true"
            issuerRef:
              name: <issuer_name>
              kind: <issuer_kind>
              group: <issuer_group>
            mode: Enabled
    ```

    where:

    injectAnnotation
    Must be set to `true` when enabled.

    name
    Specifies the name of the issuer object referenced in `ExternalSecretsConfig`.

    kind
    Specifies the API issuer. Can be set to either `Issuer` or `ClusterIssuer`.

    group
    Specifies the API issuer group. The group name must be `cert-manager.io`.

    mode
    Must be set to `Enabled`. This is an immutable field and cannot be modified once it is configured.

3.  Save your changes.

4.  After you update the `cert-manager` configurations in the `externalsecretsconfig.operator.openshift.io` object, you must manually delete `external-secrets-cert-controller` deployment by running the following command. This prevents performance degradation of the `external-secrets` application.

    ``` terminal
    $ oc delete deployments.apps external-secrets-cert-controller -n external-secrets
    ```

5.  Optionally, you can delete other resources created for the `cert-controller` by running the following commands:

    ``` terminal
    $ oc delete clusterrolebindings.rbac.authorization.k8s.io external-secrets-cert-controller
    ```

    ``` terminal
    $ oc delete clusterroles.rbac.authorization.k8s.io external-secrets-cert-controller
    ```

    ``` terminal
    $ oc delete serviceaccounts external-secrets-cert-controller -n external-secrets
    ```

    ``` terminal
    $ oc delete secrets external-secrets-webhook -n external-secrets
    ```

</div>

<div id="external-secrets-log-levels_additional-resources">

<div class="title">

Additional resources

</div>

- [External Secrets Operator for Red Hat OpenShift APIs](external-secrets-operator-api.md#external-secrets-operator-api)

- [cert-manager Operator for Red Hat Openshift](../cert_manager_operator/index.md#cert-manager-operator-about)

- [Installing the cert-manager-Operator for Red Hat Openshift](../cert_manager_operator/cert-manager-operator-install.md#cert-manager-operator-install)

</div>

# Configuring the bitwardenSecretManagerProvider plugin

You must configure the `bitwardenSecretManagerProvider` plugin to enable communication with the Bitwarden API. This configuration enables the Operator to authenticate and fetch secrets for synchronization.

<div>

<div class="title">

Prerequisites

</div>

- You have access to the cluster with `cluster-admin` privileges.

- You have created the `ExternalSecretsConfig` custom resource.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Edit the `ExternalSecretsConfig` custom resource by running the following command:

    ``` terminal
    $  oc edit externalsecretsconfigs.operator.openshift.io cluster
    ```

2.  Edit the `spec.plugins.bitwardenSecretManagerProvider` section as follows to enable the Bitwarden Secrets Manager:

    ``` yaml
    apiVersion: operator.openshift.io/v1alpha1
    kind: ExternalSecretsConfig
    ...
    spec:
      plugins:
        bitwardenSecretManagerProvider:
          mode: Enabled
          secretRef:
            name: <secret_object_name>
    ```

    where:

    name
    The name of the secret containing the certificate key pair for the plugin. The key name in the secret for the certificate must be `tls.crt`. The key name for the private key must be `tls.key`. The key name for the Certificate Authority (CA) certificate key name must be `ca.crt`. Configuring the secret is optional when the cert-manager certificate provider is configured.

3.  Save your changes and exit the editor.

4.  If you disable the plugin the following resources must be deleted manually by running the following commands:

    ``` terminal
    $ oc delete deployments.apps bitwarden-sdk-server -n external-secrets
    ```

    ``` terminal
    $ oc delete certificates.cert-manager.io bitwarden-tls-certs -n external-secrets
    ```

    ``` terminal
    $ oc delete service bitwarden-sdk-server -n external-secrets
    ```

    ``` terminal
    $ oc delete serviceaccounts bitwarden-sdk-server -n external-secrets
    ```

</div>

# Adding custom annotations to external-secrets resources

To customize your resources, you can define up to 20 custom annotations in the custom resource (CR). The Operator merges the annotations with the defaults, prioritizes them, and safely preserves annotations set by external systems.

When an annotation is removed from the CR, the Operator automatically removes it from all managed resources during the next reconciliation. Annotations set by external sources, such as Kubernetes system annotations or annotations added by other controllers, are preserved and are not affected by the Operator.

Annotation keys containing the following reserved domain prefixes are not allowed and are rejected by validation if applied:

- `kubernetes.io/` (including subdomains such as `*.kubernetes.io/`)

- `k8s.io/` (including subdomains such as `*.k8s.io/`)

- `openshift.io/` (including subdomains such as `*.openshift.io/`)

- `cert-manager.io/`

<div>

<div class="title">

Prerequisites

</div>

- You have access to the cluster with `cluster-admin` privileges.

- You have created the `ExternalSecretsConfig` custom resource.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Edit the `ExternalSecretsConfig` CR by running the following command:

    ``` terminal
    $ oc edit externalsecretsconfigs.operator.openshift.io cluster
    ```

2.  Add the `annotations` field under `spec.controllerConfig` as follows:

    ``` yaml
    apiVersion: operator.openshift.io/v1alpha1
    kind: ExternalSecretsConfig
    metadata:
      name: cluster
    spec:
      controllerConfig:
        annotations:
          prometheus.io/scrape: "true"
          example.com/environment: "production"
    ```

</div>

<div>

<div class="title">

Verification

</div>

1.  Verify that annotations are applied to the external-secrets deployment by running the following command:

    ``` terminal
    $ oc get deployment external-secrets -n external-secrets -o jsonpath='{.metadata.annotations}' | jq .
    ```

    The output should include the custom annotations you specified.

2.  Verify that annotations are applied to the pod template by running the following command:

    ``` terminal
    $ oc get deployment external-secrets -n external-secrets -o jsonpath='{.spec.template.metadata.annotations}' | jq .
    ```

    The output should include the custom annotations you specified.

3.  Verify that annotations are applied to other managed resources such as Services by running the following command:

    ``` terminal
    $ oc get service external-secrets-webhook -n external-secrets -o jsonpath='{.metadata.annotations}' | jq .
    ```

    The output should include the custom annotations you specified.

</div>

# Configuring the revisionHistoryLimit for external-secrets components

Configure the number of old `ReplicaSet` objects retained for rollback by setting the `revisionHistoryLimit` parameter for `external-secrets` components.

The following components can be configured:

| Component name | Description |
|----|----|
| `ExternalSecretsCoreController` | The main `external-secrets` controller. |
| `Webhook` | The `external-secrets` webhook server. |
| `CertController` | The certificate controller for webhook TLS. |
| `BitwardenSDKServer` | The Bitwarden SDK server plugin. |

Each component can only have one configuration entry. A maximum of 4 component configuration entries are allowed, one per component.

<div>

<div class="title">

Prerequisites

</div>

- You have access to the cluster with `cluster-admin` privileges.

- You have created the `ExternalSecretsConfig` custom resource.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Edit the `ExternalSecretsConfig` CR by running the following command:

    ``` terminal
    $ oc edit externalsecretsconfigs.operator.openshift.io cluster
    ```

2.  Add the `componentConfigs` field under `spec.controllerConfig` as follows:

    ``` yaml
    apiVersion: operator.openshift.io/v1alpha1
    kind: ExternalSecretsConfig
    metadata:
      name: cluster
    spec:
      controllerConfig:
        componentConfigs:
          - componentName: ExternalSecretsCoreController
            deploymentConfigs:
              revisionHistoryLimit: 5
          - componentName: Webhook
            deploymentConfigs:
              revisionHistoryLimit: 3
    ```

    where

    `spec.controllerConfig.componentConfigs.componentName.deploymentConfigs.revisionHistoryLimit`
    Specifies the number of old `ReplicaSet` objects to retain for rollback. The value must be at least 1 to ensure rollback capability. The maximum value is 50. If not specified, the default is 10.

</div>

<div>

<div class="title">

Verification

</div>

- Verify that the `revisionHistoryLimit` parameter is applied to the deployment by running the following command:

  ``` terminal
  $ oc get deployment external-secrets -n external-secrets -o jsonpath='{.spec.revisionHistoryLimit}'
  ```

  The output should display the value you configured.

</div>

# Setting custom environment variables for external-secrets components

To configure component behavior at runtime or integrate with external services, set custom environment variables for individual `external-secrets` components.

Custom environment variables are merged with the default environment variables set by the Operator. User-specified variables take precedence in case of conflicts with the Operator defaults. A maximum of 50 custom environment variables can be specified per component.

The environment variable names starting with the following prefixes are reserved:

- `HOSTNAME`

- `KUBERNETES_`

- `EXTERNAL_SECRETS_`

<div>

<div class="title">

Prerequisites

</div>

- You have access to the cluster with `cluster-admin` privileges.

- You have created the `ExternalSecretsConfig` custom resource.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Edit the `ExternalSecretsConfig` CR by running the following command:

    ``` terminal
    $ oc edit externalsecretsconfigs.operator.openshift.io cluster
    ```

2.  Add the `overrideEnv` field under the desired component in the `spec.controllerConfig.componentConfigs` stanza as follows:

    ``` yaml
    apiVersion: operator.openshift.io/v1alpha1
    kind: ExternalSecretsConfig
    metadata:
      name: cluster
    spec:
      controllerConfig:
        componentConfigs:
          - componentName: ExternalSecretsCoreController
            overrideEnv:
              - name: Example
                value: "4"
    ```

    where

    `spec.controllerConfig.componentConfigs.overrideEnv.name`
    Specifies the name of the environment variable. Environment variable names starting with `HOSTNAME`, `KUBERNETES_`, or `EXTERNAL_SECRETS_` are reserved and are not allowed.

    `spec.controllerConfig.componentConfigs.overrideEnv.value`
    Specifies the value of the environment variable.

</div>

<div>

<div class="title">

Verification

</div>

- Verify that the environment variable is set on the deployment by running the following command:

  ``` terminal
  $ oc set env deployment/external-secrets -n external-secrets --list
  ```

  The output should include the custom environment variable you specified.

</div>

# Enabling optional features for External Secrets Operator for Red Hat OpenShift

The External Secrets Operator for Red Hat OpenShift supports optional capabilities that can be enabled cluster-wide through the `ExternalSecretsManager` custom resource (CR). Features are disabled by default and must be explicitly enabled.

You can enable or disable a feature at any time. The Operator reconciles the core controller deployment when the feature state changes, without requiring a restart or reinstallation.

> [!WARNING]
> `UnsafeAllowGenericTargets` is a pre-release feature. It is not recommended for production use. Enabling this feature allows `ExternalSecret` resources to write secret data to arbitrary Kubernetes resource types beyond Secret objects. This might cause data managed by other controllers to be overwritten and can expose sensitive values through non-secret resources. This feature provides no additional access control beyond standard Kubernetes role-based access control (RBAC).

When enabled, `ExternalSecret` resources can target arbitrary Kubernetes resource types as their sync destination, instead of being limited to `Secret` objects.

The Operator passes the `--unsafe-allow-generic-targets=true` flag to the core `external-secrets` controller. The webhook and cert-controller are not affected.

<div>

<div class="title">

Prerequisites

</div>

- You have access to the cluster with `cluster-admin` privileges.

- You have installed the External Secrets Operator for Red Hat OpenShift and created the `ExternalSecretsConfig` CR.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Edit the `ExternalSecretsManager` CR by running the following command:

    ``` terminal
    $ oc edit externalsecretsmanagers.operator.openshift.io cluster
    ```

2.  Add the `features` field under `spec` and set the desired feature mode:

    ``` yaml
    apiVersion: operator.openshift.io/v1alpha1
    kind: ExternalSecretsManager
    metadata:
      name: cluster
    spec:
      features:
        - name: UnsafeAllowGenericTargets
          mode: Enabled
    ```

    To disable the feature, set `mode: Disabled` or remove the entry from the features list.

</div>

<div>

<div class="title">

Verification

</div>

1.  Verify that the feature flag is passed to the core controller by running the following command:

    ``` terminal
    $ oc get deployment external-secrets \
      -n external-secrets \
      -o jsonpath='{.spec.template.spec.containers[0].args}' | jq .
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` json
    [
      "--concurrent=1",
      "--metrics-addr=:8080",
      "--loglevel=warn",
      "--zap-time-encoding=epoch",
      "--enable-leader-election=true",
      "--enable-push-secret-reconciler=true",
      "--enable-cluster-store-reconciler=true",
      "--enable-cluster-external-secret-reconciler=true",
      "--unsafe-allow-generic-targets=true"
    ]
    ```

    </div>

    When the feature is enabled, the output includes `--unsafe-allow-generic-targets=true`. When disabled or not configured, the flag is absent.

2.  Verify that the `ExternalSecretsManager` CR reflects the configured feature by running the following command:

    ``` terminal
    $ oc get externalsecretsmanagers.operator.openshift.io cluster -o jsonpath='{.spec.features}' | jq .
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` json
    [
      {
        "mode": "Enabled",
        "name": "UnsafeAllowGenericTargets"
      }
    ]
    ```

    </div>

</div>

# Mounting a custom trusted certificate authority bundle for external-secrets

You can configure the External Secrets Operator for Red Hat OpenShift to trust a custom certificate authority (CA) bundle when the `external-secrets` core controller communicates with external secret backends over transport layer socket (TLS). This is required when your organization uses a private CA or a self-signed certificate that is not included in the default system truststore.

To enable mounting a custom trusted CA, you reference a `ConfigMap` that contains the Privacy Enhanced Mail (PEM)-encoded CA certificates in the `spec.controllerConfig.trustedCABundle` field of the `ExternalSecretsConfig` custom resource (CR). The Operator mounts the bundle into the core controller pod and configures the TLS library to use it alongside the default system trust stores.

The External Secrets Operator for Red Hat OpenShift applies the following rules to the CA bundle `ConfigMap`:

- The `ConfigMap` must reside in the `external-secrets` namespace and must contain only PEM-encoded X.509 CA certificates. Leaf certificates and private key PEM blocks are rejected.

- If the `ConfigMap` key contains an invalid bundle, the `ExternalSecretsConfig` CR enters a `Degraded` state. The Operator automatically recovers and mounts the bundle when the `ConfigMap` is corrected, without requiring manual intervention.

- If the referenced `ConfigMap` does not exist, the Operator removes any previously mounted CA bundle from the core controller deployment and sets the `ExternalSecretsConfig` CR to a `Degraded` state until the `ConfigMap` is created.

- The CA bundle is mounted only on the core `external-secrets` controller container. The webhook and cert-controller containers are not affected.

- If the `ConfigMap` has the `config.openshift.io/inject-trusted-cabundle: "true"` label and a cluster proxy is configured, the Operator skips the user-defined mount. The cluster-wide CA bundle injected by the Cluster Network Operator (CNO) is already available to the controller through the proxy CA bundle mechanism.

<div>

<div class="title">

Prerequisites

</div>

- You have access to the cluster with `cluster-admin` privileges.

- You have installed the External Secrets Operator for Red Hat OpenShift and created the `ExternalSecretsConfig` CR.

- A `ConfigMap` containing PEM-encoded X.509 CA certificates exists in the `external-secrets` namespace.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create the `ConfigMap` containing your CA bundle by running the following command:

    ``` terminal
    $ oc create configmap user-ca-bundle \
      --from-file=ca-bundle.crt=/path/to/ca.pem \
      -n external-secrets
    ```

2.  Edit the `ExternalSecretsConfig` CR by running the following command:

    ``` terminal
    $ oc edit externalsecretsconfigs.operator.openshift.io cluster
    ```

3.  Add the `trustedCABundle` field under `spec.controllerConfig`:

    ``` yaml
    apiVersion: operator.openshift.io/v1alpha1
    kind: ExternalSecretsConfig
    metadata:
      name: cluster
    spec:
      controllerConfig:
        trustedCABundle:
          name: user-ca-bundle
          key: ca-bundle.crt
    ```

    where:

    `spec.controllerConfig.trustedCABundle.name`
    Specifies the name of the `ConfigMap` in the `external-secrets` namespace that contains the CA certificate bundle.

    `spec.controllerConfig.trustedCABundle.key`
    Optional. Specifies the key within the `ConfigMap` that holds the PEM-encoded CA bundle. The default is `ca-bundle.crt`.

</div>

<div>

<div class="title">

Verification

</div>

1.  Verify that the CA bundle volume is mounted on the core controller deployment by running the following command:

    ``` terminal
    $ oc get deployment external-secrets \
      -n external-secrets \
      -o jsonpath='{.spec.template.spec.volumes}' | jq '.[] | select(.name=="user-ca-bundle")'
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` json
    {
      "configMap": {
        "defaultMode": 420,
        "items": [
          {
            "key": "ca-bundle.crt",
            "path": "ca-bundle.crt"
          }
        ],
        "name": "trusted-ca-bundle-for-es"
      },
      "name": "user-ca-bundle"
    }
    ```

    </div>

2.  Verify that the `SSL_CERT_DIR` is set on the core controller container by running the following command:

    ``` terminal
    $ oc set env deployment/external-secrets \
      -n external-secrets \
      --list | grep SSL_CERT_DIR
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    SSL_CERT_DIR=/etc/pki/tls/user-certs:/etc/pki/tls/certs:/etc/ssl/certs
    ```

    </div>

3.  Verify that the `ExternalSecretsConfig` CR is not in a `Degraded` state by running the following command:

    ``` terminal
    $ oc get externalsecretsconfigs.operator.openshift.io cluster \
      -o jsonpath='{.status.conditions[?(@.type=="Degraded")]}' | jq .
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` json
    {
      "lastTransitionTime": "2026-06-22T10:29:11Z",
      "message": "",
      "observedGeneration": 5,
      "reason": "Ready",
      "status": "False",
      "type": "Degraded"
    }
    ```

    </div>

    The `Degraded` condition should show `"status": "False"`. If the condition is `True,` review the message field for the specific validation error and correct the referenced `ConfigMap`.

</div>
