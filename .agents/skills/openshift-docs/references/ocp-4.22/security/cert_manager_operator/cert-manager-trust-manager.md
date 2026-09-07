<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

The trust-manager operand simplifies the distribution of certificate authority (CA) certificates across OpenShift Container Platform clusters. As an administrator, you can configure the operand according to the cluster requirements and manage trust bundles efficiently.

> [!IMPORTANT]
> Distributing certificates by using trust manager is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.
>
> For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

The trust-manager operand provides the following benefits:

- Distribution of CA certificates across your cluster as a Day 2 operation.

- Consolidation of certificates from multiple sources, such as ConfigMaps, Secrets, inline data, and default CAs, into a single trust bundle.

- Automatic updates to target objects whenever the underlying source certificates change.

- Creation of trust bundles as secret objects for applications that explicitly require secrets instead of ConfigMap objects.

- Automatic integration with the default trusted CA bundle of the cluster, requiring no manual configuration.

# Installing the trust-manager operand

You can install the trust-manager operand to enable the automated distribution of trust bundles across your cluster namespaces. The trust-manager operand is not installed by default.

> [!IMPORTANT]
> Distributing certificates by using trust manager is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.
>
> For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

<div>

<div class="title">

Prerequisites

</div>

- You have access to the cluster with `cluster-admin` privileges.

- You have installed cert-manager Operator for Red Hat OpenShift.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Enable the trust manager add-on feature in the Operator subscription by running the following command:

    ``` terminal
    oc -n cert-manager-operator patch subscription cert-manager-operator \
      --type='merge' \
      -p '{"spec":{"config":{"env":[{"name":"UNSUPPORTED_ADDON_FEATURES","value":"TrustManager=true"}]}}}'
    ```

2.  Create a YAML file, for example, `trust-manager.yaml`, that defines the `TrustManager` custom resource (CR) as shown in the following example:

    <div class="formalpara">

    <div class="title">

    Example trust-manager.yaml

    </div>

    ``` yaml
    apiVersion: operator.openshift.io/v1alpha1
    kind: TrustManager
    metadata:
      name: cluster
    spec:
      trustManagerConfig:
        logLevel: 2
        logFormat: "text"
        trustNamespace: "cert-manager"
        filterExpiredCertificates: "Enabled"
        secretTargets:
          policy: "Custom"
          authorizedSecrets:
            - "my-trust-bundle"
            - "app-ca-bundle"
        defaultCAPackage:
          policy: "Enabled"
        resources: {}
        affinity: {}
        tolerations: []
        nodeSelector: {}
      controllerConfig:
        labels:
          environment: "production"
          team: "platform"
        annotations:
          example.com/managed-by: "cert-manager-operator"
    ```

    </div>

    > [!NOTE]
    > Because you can create only one instance of `TrustManager` CR per cluster, the `metadata.name` field must be set to `cluster`.

3.  Create the `TrustManager` CR by running the following command:

    ``` terminal
    $ oc create -f trust-manager.yaml
    ```

</div>

<div>

<div class="title">

Verification

</div>

- Verify that the `trust-manager` operand is running successfully by running the following command:

  ``` terminal
  $ oc get TrustManager cluster -o jsonpath='{.status.conditions}' | jq
  ```

  <div class="formalpara">

  <div class="title">

  Example output

  </div>

  ``` terminal
  [
    {
      "lastTransitionTime": "2026-03-27T11:54:50Z",
      "message": "",
      "reason": "Ready",
      "status": "False",
      "type": "Degraded"
    },
    {
      "lastTransitionTime": "2026-03-27T11:54:50Z",
      "message": "reconciliation successful",
      "reason": "Ready",
      "status": "True",
      "type": "Ready"
    }
  ]
  ```

  </div>

  The `message` field in the output must have the value `reconciliation successful`.

- Verify that the `trust-manager` deployment is running successfully in the `cert-manager` namespace:

  ``` terminal
  $ oc get Deployments -l "app.kubernetes.io/name=cert-manager-trust-manager" -n cert-manager
  ```

  <div class="formalpara">

  <div class="title">

  Example output

  </div>

  ``` terminal
  NAME            READY   UP-TO-DATE   AVAILABLE   AGE
  trust-manager   1/1     1            1           109s
  ```

  </div>

- Verify that the status of the pod is `Running` by running the following command:

  ``` terminal
  $ oc get pods -l "app.kubernetes.io/name=cert-manager-trust-manager" -n cert-manager
  ```

  <div class="formalpara">

  <div class="title">

  Example output

  </div>

  ``` terminal
  NAME                             READY   STATUS    RESTARTS   AGE
  trust-manager-547bb59b4b-hd6mv    1/1     Running   0          24s
  ```

  </div>

</div>

<div>

<div class="title">

Next Step

</div>

- Configuring trust bundle

</div>

# Configuring trust bundle

After installing the trust-manager operand, you must use the Bundle custom resource (CR) to distribute certificate authority (CA) certificates across your cluster. A trust bundle combines certificate sources and maintains target `ConfigMap` and `Secret` objects across selected namespaces.

If you configure your trust bundle to use the default CAs, you do not need to manually provision the source certificates. The controller reads them from the `cert-manager-operator-trusted-ca-bundle` ConfigMap, which is injected by the Cluster Network Operator (CNO) during the Operator installation.

> [!IMPORTANT]
> Distributing certificates by using trust manager is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.
>
> For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

<div>

<div class="title">

Prerequisites

</div>

- You have access to the cluster with `cluster-admin` privileges.

- You have installed `trust-manager` operand.

</div>

<div>

<div class="title">

Procedure

</div>

1.  To inject the trust bundle into a specific namespace, apply the required label by running the following command:

    ``` terminal
    $ oc patch namespace <namespace> --type=merge '{"metadata":{"labels":{"trust.cert-manager.io/inject":"true"}}}'
    ```

    The trust-manager operand creates the target bundle in all namespaces that match the label selector defined in your `Bundle` CR.

2.  Create a YAML file, for example, `bundle.yaml`, that defines the `Bundle` object as shown in the following example:

    ``` yaml
    apiVersion: trust.cert-manager.io/v1alpha1
    kind: Bundle
    metadata:
      name: example-bundle
    spec:
      sources:
        - useDefaultCAs: true
      target:
        configMap:
          key: ca-certificates.crt
        secret:
          key: ca-certificates.crt
        namespaceSelector:
          matchLabels:
            trust.cert-manager.io/inject: "true"
    ```

    For more information on bundle configurations, see [trust-manager usage](https://cert-manager.io/docs/trust/trust-manager/#usage).

    > [!NOTE]
    > If your Bundle CR targets a `Secret` object, you must set the `spec.trustManagerConfig.secretTargets.policy` field in your TrustManager CR to `Custom` and add the name of target secret to the `spec.trustManagerConfig.secretTargets.authorizedSecrets` list. If the `spec.trustManagerConfig.secretTargets.policy` field is set to `Disabled`, the Bundle CR fails to create the target secret.

3.  Create the `Bundle` custom resource by running the following command:

    ``` terminal
    $ oc create -f bundle.yaml
    ```

</div>

<div>

<div class="title">

Verification

</div>

- Verify the status of Bundle CR by running the following command:

  ``` terminal
  $ oc get Bundle example-bundle -o jsonpath='{.status.conditions}' | jq
  ```

  In the output, the `reason` must be set to `Synced` and `status` must be set to `True`, as shown in the following example:

  ``` terminal
  [
    {
      "lastTransitionTime": "2026-03-27T12:03:42Z",
      "message": "Successfully synced Bundle to namespaces that match this label selector: trust.cert-manager.io/inject=true",
      "observedGeneration": 1,
      "reason": "Synced",
      "status": "True",
      "type": "Synced"
    }
  ]
  ```

- Verify the target secret by running the following command:

  ``` terminal
  $ oc describe secret example-bundle -n trust-bundle-target
  ```

  <div class="formalpara">

  <div class="title">

  Example output

  </div>

  ``` terminal
  Name:         example-bundle
  Namespace:    trust-bundle-target
  Labels:       trust.cert-manager.io/bundle=example-bundle
  Annotations:  trust.cert-manager.io/hash: 55c00f8109c4c6b1ee4710aa53ad280355973f25444d6bb13a93851af0d8f5d8

  Type:  Opaque

  Data
  ====
  ca-certificates.crt:  219257 bytes
  ```

  </div>

- Verify the target ConfigMap by running the following command:

  ``` terminal
  $ oc get cm example-bundle -n trust-bundle-target
  ```

  <div class="formalpara">

  <div class="title">

  Example output

  </div>

  ``` terminal
  NAME             DATA   AGE
  example-bundle   1      4m25s
  ```

  </div>

</div>

# Uninstalling the trust-manager operand

You can uninstall the trust-manager operand by deleting the TrustManager custom resource (CR). Deleting the TrustManager CR stops the operator from reconciling trust-manager resources, but does not automatically remove the trust-manager deployment or its associated resources. You must manually delete these resources after deleting the CR if you need a complete cleanup.

<div>

<div class="title">

Prerequisites

</div>

- You have access to the cluster with `cluster-admin` privileges.

- You have enabled the trust manager feature.

- You have created the `TrustManager` custom resource.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Delete any Bundle CRs that you created. Deleting a Bundle CR causes trust-manager to remove the corresponding target ConfigMap and Secret objects from the target namespaces.

    1.  Fetch the list of bundles created by running the following command:

        ``` terminal
        $ oc get Bundle
        ```

    2.  Delete each Bundle in the list by running the following command:

        ``` terminal
        $ oc delete Bundle <bundle_name>
        ```

2.  Delete the `TrustManager` custom resource by running the following command:

    ``` terminal
    $ oc delete TrustManager cluster
    ```

3.  Delete all the labeled resources to complete the cleanup:

    1.  Delete the namespace-scoped resources in the `cert-manager` namespace:

        ``` terminal
        $ oc delete deployments,services,serviceaccounts,configmaps,certificates,issuers -l "app.kubernetes.io/name=cert-manager-trust-manager" -n cert-manager
        ```

    2.  Delete the cluster-scoped resources:

        ``` terminal
        $ oc delete clusterroles,clusterrolebindings,validatingwebhookconfigurations -l "app.kubernetes.io/name=cert-manager-trust-manager"
        ```

    3.  If you configured a custom trust namespace, delete the role and role binding resources in that namespace:

        ``` terminal
        $ oc delete roles,rolebindings -l "app.kubernetes.io/name=cert-manager-trust-manager" -n <trust_namespace>
        ```

</div>

# Trust manager custom resource fields

You can configure the behavior of the trust-manager operand by modifying the `TrustManager` custom resource (CR).

> [!IMPORTANT]
> Distributing certificates by using trust manager is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.
>
> For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

The following table lists the parameters for configuring trust-manager settings.

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 11%" />
<col style="width: 55%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Field</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>spec.controllerConfig.labels</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>Optional. Specifies a list of key-value pairs to apply as labels to all resources created for the trust manager deployment.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>spec.controllerConfig.annotations</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>Optional. Specifies a list of key-value pairs to apply as annotations to all resources created for the trust manager deployment.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>spec.trustManagerConfig.affinity</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>Optional. Specifies the scheduling constraints for the trust manager pod. For more information, see <a href="https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/">Assigning Pods to Nodes</a>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>spec.trustManagerConfig.defaultCAPackage</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>Optional. Configures the default CA package for trust manager. When enabled, the Operator uses the OpenShift Container Platform trusted CA bundle injection mechanism.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>spec.trustManagerConfig.defaultCAPackage.policy</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Optional. Specifies whether the default CA package feature is enabled. When set to <code>Enabled</code>, the Operator configures the trusted CA bundle to trust manager. When set to <code>Disabled</code>, no default CA package is configured. The default value is <code>Disabled</code>.</p>
<div class="note">
<div class="title">
&#10;</div>
<p>To enable the <code>useDefaultCAs: true</code> setting in your Bundle CR, you must set the value to <code>Enabled</code>.</p>
</div></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>spec.trustManagerConfig.filterExpiredCertificates</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Optional. Specifies whether trust manager filters out expired certificates from trust bundles before distributing them. When set to <code>Enabled</code>, the expired certificates are removed from bundles. When set to <code>Disabled</code>, the expired certificates are included in bundles. The default value is <code>Disabled</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>spec.trustManagerConfig.logLevel</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p>Optional. Specifies the verbosity of trust manager logging. The minimum value is <code>1</code> and the maximum value is <code>5</code>. The default value is <code>1</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>spec.trustManagerConfig.logFormat</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Optional. Specifies the output format for trust manager logging. The supported formats are <code>text</code> and <code>json</code>. The default value is <code>text</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>spec.trustManagerConfig.nodeSelector</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>Optional. Specifies the key-value pairs that limit which nodes can host the trust manager pod. You can specify a maximum of 50 node selectors. For more information, see <a href="https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/">Assigning Pods to Nodes</a>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>spec.trustManagerConfig.resources</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>Optional. Defines the compute resource requirements for the trust manager pod.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>spec.trustManagerConfig.secretTargets</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>Optional. Defines the configuration for writing trust bundles to <code>Secrets</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>spec.trustManagerConfig.secretTargets.authorizedSecrets</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>Optional. A list of specific secret names that trust manager is authorized to create and update.</p>
<div class="note">
<div class="title">
&#10;</div>
<p>If <code>spec.trustManagerConfig.secretTargets.policy</code> is set to <code>Custom</code>, you must specify a value. If <code>spec.trustManagerConfig.secretTargets.policy</code> is set to <code>Disabled</code>, you must not specify a value.</p>
</div></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>spec.trustManagerConfig.secretTargets.policy</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Optional. Specifies whether trust manager can write trust bundles to <code>Secrets</code>. When set to <code>Disabled</code>, trust manager cannot write trust bundles to <code>Secrets</code>. When set to <code>Custom</code>, trust manager is granted permission to create and update only the secrets listed in the <code>authorizedSecrets</code> parameter. The default value is <code>Disabled</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>spec.trustManagerConfig.tolerations</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>Optional. Allows the trust manager pod to be scheduled on nodes with specific taints. You can specify a maximum of 50 tolerations.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>spec.trustManagerConfig.trustNamespace</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Optional. Specifies the namespace where trust manager locates CA certificate sources, such as ConfigMaps and Secrets. This namespace must exist before you create the TrustManager custom resource. The default value is <code>cert-manager</code>.</p>
<div class="note">
<div class="title">
&#10;</div>
<p>You cannot change the value once set.</p>
</div></td>
</tr>
</tbody>
</table>
