<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

> [!IMPORTANT]
> Argo CD application sets in non-control plane namespaces is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.
>
> For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

By using application sets, you can automate and manage the deployments of multiple Argo CD applications declaratively from a single mono-repository to many clusters at once with greater flexibility.

With Red Hat OpenShift GitOps 1.12 and later, as a cluster administrator, you can create and manage `ApplicationSet` resources in non-control plane namespaces other than `openshift-gitops`. To do this, enable and configure the `ArgoCD` and `ApplicationSet` custom resources (CRs). This is useful in multitenancy environments where isolated teams manage their own Argo CD application deployments. In the Argo CD open source project, this is called the *ApplicationSet in any namespace* feature.

> [!NOTE]
> The generated Argo CD applications can create resources in any non-control plane namespace. However, the application itself will be in the same namespace as the application set resources.

# Prerequisites

- You have a user-defined [cluster-scoped Argo CD instance](../declarative_clusterconfig/configuring-an-openshift-cluster-by-deploying-an-application-with-cluster-configurations.md#using-argo-cd-instance-to-manage-cluster-scoped-resources_configuring-an-openshift-cluster-by-deploying-an-application-with-cluster-configurations) in your defined namespace. For example, `spring-petclinic` namespace.

- You have [explicitly enabled and configured](../argocd_applications/managing-apps-in-non-control-plane-namespaces.md#managing-apps-in-non-control-plane-namespaces) the target namespaces in the `ArgoCD` CR to manage application resources in non-control plane namespaces.

# Enabling the application set resources in non-control plane namespaces

As a cluster administrator, you can define a certain set of non-control plane namespaces wherein users can create, update, and reconcile `ApplicationSet` resources. You must explicitly enable and configure the `ArgoCD` and `ApplicationSet` custom resources (CRs) as per your requirements.

<div>

<div class="title">

Prerequisites

</div>

- You have installed the Red Hat OpenShift GitOps Operator on your OpenShift Container Platform cluster.

- You are logged in to the OpenShift Container Platform cluster as an administrator.

- Ensure that a cluster-scoped Argo CD instance exists in your defined namespace.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Set the `sourceNamespaces` parameter for the `applicationSet` spec to include the non-control plane namespaces:

    **Example Argo CD custom resource:**

    ``` yaml
    apiVersion: argoproj.io/v1beta1
    kind: ArgoCD
    metadata:
      name: example
      namespace: spring-petclinic
    spec:
      applicationSet:
        sourceNamespaces:
          - dev
    ```

    where:

    `spec.applicationSet.sourceNamespaces`
    Specifies the list of non-control plane namespaces for creating and managing `ApplicationSet` resources.

    > [!NOTE]
    > At the moment, the use of wildcards (`*`) is not supported in the `.spec.applicationSet.sourceNamespaces` field.

2.  Verify that the following role-based access control (RBAC) resources are either created or modified by the GitOps Operator:

    | Name | Kind | Purpose |
    |----|----|----|
    | `<argocd_name>-<argocd_namespace>-argocd-applicationset-controller` | `ClusterRole` and `ClusterRoleBinding` | For the Argo CD ApplicationSet Controller to watch and list `ApplicationSet` resources at cluster-level |
    | `<argocd_name>-<argocd_namespace>-applicationset` | `Role` and `RoleBinding` | For the Argo CD ApplicationSet Controller to manage `ApplicationSet` resources in target namespace |
    | `<argocd_name>-<target_namespace>` | `Role` and `RoleBinding` | For the Argo CD server to manage `ApplicationSet` resources in target namespace through UI, API, or CLI |

    > [!NOTE]
    > In addition to creating RBAC resources, the Red Hat OpenShift GitOps Operator also adds a label to target namespaces. The GitOps Operator adds the `argocd.argoproj.io/applicationset-managed-by-cluster-argocd` label to the target namespace.

</div>

# About configuring ApplicationSet namespaces using names and patterns

Red Hat OpenShift GitOps controls which namespaces an Argo CD instance can use to create and manage `ApplicationSet` resources.

You enable this behavior by specifying allowed namespaces in the Argo CD custom resource (CR) using the `spec.applicationSet.sourceNamespaces` field. The Red Hat OpenShift GitOps Operator uses this configuration to determine which namespaces are permitted to host `ApplicationSet` resources and automatically provisions the required role-based access control (RBAC) resources.

The `spec.applicationSet.sourceNamespaces` field supports the following namespace selectors:

- Explicit namespace names

- Glob-style wildcard patterns

- Regular expression patterns

The Red Hat OpenShift GitOps Operator evaluates these selectors at reconcile time and applies permissions to all matching namespaces. Permissions are also automatically applied to newly created namespaces that match the configured selectors.

## Enable ApplicationSet in a specific namespace

To enable an Argo CD instance to manage `ApplicationSet` resources in a specific namespace, add the namespace name to the `spec.applicationSet.sourceNamespaces` field in the Argo CD custom resource.

<div>

<div class="title">

Procedure

</div>

1.  Add the namespace name to the `spec.applicationSet.sourceNamespaces` field in the Argo CD custom resource:

    ``` yaml
    apiVersion: argoproj.io/v1beta1
    kind: ArgoCD
    metadata:
      name: example
    spec:
      sourceNamespaces:
        - foo
      applicationSet:
        sourceNamespaces:
          - foo
    ```

    In this example, the Argo CD instance named `example` can create and manage `ApplicationSet` resources in the `foo` namespace.

</div>

## Define glob-style in wildcard patterns

To grant permissions across multiple namespaces that share a common naming convention, use glob-style wildcard patterns.

<div>

<div class="title">

Procedure

</div>

1.  Use glob-style wildcard patterns in the `spec.applicationSet.sourceNamespaces` field to grant permissions across multiple namespaces:

    ``` yaml
    apiVersion: argoproj.io/v1beta1
    kind: ArgoCD
    metadata:
      name: example
    spec:
      sourceNamespaces:
        - team-*
      applicationSet:
        sourceNamespaces:
          - team-*
    ```

    This configuration allows the Argo CD instance to manage `ApplicationSet` resources in namespaces, such as `team-1` and `team-2`.

</div>

## Define regular expressions in patterns

To precisely control which namespaces receive permissions, use regular expressions. Regular expression patterns must be wrapped in forward slashes (/pattern/).

<div>

<div class="title">

Procedure

</div>

1.  Use regular expression patterns wrapped in forward slashes in the `spec.applicationSet.sourceNamespaces` field:

    ``` yaml
    apiVersion: argoproj.io/v1beta1
    kind: ArgoCD
    metadata:
      name: example
    spec:
      sourceNamespaces:
        - team-*
      applicationSet:
        sourceNamespaces:
          - /^team-(frontend|backend)$/
          - /^team-[0-9]+$/
    ```

    In this example, permissions are granted only to namespaces that match the specified regular expressions.

    > [!NOTE]
    > Patterns wrapped in forward slashes (`/pattern/\`) are treated as regular expressions. Patterns without slashes are treated as glob-style wildcard patterns.

    > [!IMPORTANT]
    > To create applications in non-control-plane namespaces, *Apps in Any Namespace* must be enabled. Ensure that the target namespace names are included in the `spec.sourceNamespaces` field of the Argo CD custom resource.

    > [!WARNING]
    > Avoid using broad patterns. These patterns can match a large number of namespaces, including system or sensitive namespaces, and might grant unintended access. Use the most specific pattern that meets your requirements and regularly review which namespaces match your configuration.

</div>

# Allowing Source Code Manager Providers

> [!IMPORTANT]
> Ensure that you read this section carefully. Misconfiguration could lead to potential security issues.

Allowing ApplicationSet resources in non-control plane namespaces can expose secrets through malicious API endpoints in Source Code Manager (SCM) Provider or Pull Request (PR) generators. To help prevent unauthorized access to sensitive information, the Operator disables these generators by default.

<div>

<div class="title">

Prerequisites

</div>

- You have installed the Red Hat OpenShift GitOps Operator on your OpenShift Container Platform cluster.

- You are logged in to the OpenShift Container Platform cluster as an administrator.

- You have a cluster-scoped Argo CD instance configured with `spec.applicationSet.sourceNamespaces`.

</div>

<div>

<div class="title">

Procedure

</div>

1.  To use the SCM Provider and PR generators, explicitly define a list of allowed SCM Providers:

    **Example Argo CD custom resource:**

    ``` yaml
    apiVersion: argoproj.io/v1beta1
    kind: ArgoCD
    metadata:
      name: example-argocd
    spec:
      applicationSet:
        sourceNamespaces:
          - dev
        scmProviders:
          - https://git.mydomain.com/
          - https://gitlab.mydomain.com/
    ```

    where:

    `spec.applicationSet.scmProviders`
    Specifies the allowlist of SCM Provider URLs that `ApplicationSets` can access. Only SCM Providers from this list are permitted for use with SCM Provider and Pull Request generators.

    > [!NOTE]
    > If you use a URL that is not in the list of allowed SCM Providers, the Argo CD ApplicationSet Controller will reject it.

</div>

# ApplicationSet tokenRef strict mode

When you configure ApplicationSets to run in non-control plane namespaces using `spec.applicationSet.sourceNamespaces`, GitOps automatically enables `tokenRef` strict mode by default to enhance security.

The `tokenRef` field allows an ApplicationSet generator to reference a secret that contains authentication credentials, such as a Git access token, for Source Code Manager (SCM) Provider or Pull Request generators. This enables ApplicationSets to authenticate with external Git providers when generating applications.

In `tokenRef` strict mode, secrets referenced by ApplicationSet SCM Provider or Pull Request generators through `tokenRef` must be labeled with the following label:

``` terminal
argocd.argoproj.io/secret-type: scm-creds
```

This security feature provides the following benefits:

- Ensures only secrets explicitly designated for SCM/PR generator use (via the scm-creds label) can be referenced through `tokenRef`.

- Establishes clear security boundaries for secret references

- Helps identify which secrets are intended for ApplicationSet use

- Reduces the risk of accidental or unauthorized access to sensitive credentials

The following table shows when `tokenRef` strict mode is enabled:

| Situation | Strict mode status |
|----|----|
| `spec.applicationSet.sourceNamespaces` is not configured or matches no namespace | Disabled (`false`) |
| `spec.applicationSet.sourceNamespaces` is configured and matches one or more namespaces | Enabled (`true`) |

<div class="important">

<div class="title">

</div>

- Ensure that tokenRef strict mode is enabled for enhanced security.

- If required during migration, you can temporarily disable strict mode by setting `applicationsetcontroller.enable.tokenref.strict.mode` to `"false"` in `spec.cmdParams` of the `ArgoCD` custom resource (CR).

- `tokenRef` strict mode applies only to SCM Provider generators and Pull Request generators. Other generator types are not affected by this security feature.

</div>

## Configuring ApplicationSet tokenRef strict mode

When you enable ApplicationSets in non-control plane namespaces, `tokenRef` strict mode is enabled by default. To use SCM Provider or Pull Request generators with `tokenRef`, you must label the referenced secrets appropriately.

> [!WARNING]
> When strict mode is enabled on an existing deployment, ApplicationSets that use `tokenRef` without the `scm-creds` label stop reconciling until you label the referenced secrets. After you label the secrets, the ApplicationSets resume reconciliation without requiring changes to existing `ApplicationSet` resources.

<div>

<div class="title">

Prerequisites

</div>

- You have installed the Red Hat OpenShift GitOps Operator on your OpenShift Container Platform cluster.

- You are logged in to the OpenShift Container Platform cluster as an administrator.

- You use SCM Provider or Pull Request generators with `tokenRef` and you have configured `spec.applicationSet.scmProviders`.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Enable ApplicationSet resources in non-control plane namespaces by configuring the `Argo CD` custom resource:

    ``` yaml
    apiVersion: argoproj.io/v1beta1
    kind: ArgoCD
    metadata:
      name: example
      namespace: argocd-foo
    spec:
      sourceNamespaces:
        - foo
      applicationSet:
        sourceNamespaces:
          - foo
    ```

    When you configure `spec.applicationSet.sourceNamespaces`, tokenRef strict mode is automatically enabled.

2.  Identify secrets used by your ApplicationSet SCM Provider or Pull Request generators.

    For example, if your ApplicationSet uses a `tokenRef` like this:

    ``` yaml
    apiVersion: argoproj.io/v1alpha1
    kind: ApplicationSet
    metadata:
      name: github-appset
      namespace: foo
    spec:
      generators:
        - scmProvider:
            github:
              organization: myorg
              tokenRef:
                secretName: github-token
                key: token
    ```

    `secretName`
    Specifies the `github-token` secret in the `foo` namespace. When `spec.applicationSet.sourceNamespaces` is configured in the `ArgoCD` CR, this secret must include the `argocd.argoproj.io/secret-type: scm-creds` label.

3.  Label each secret referenced by `tokenRef` with the required label by running the following command:

    ``` terminal
    $ oc label secret -n <namespace> <secret-name> \
      argocd.argoproj.io/secret-type=scm-creds
    ```

    **Example command:**

    ``` terminal
    $ oc label secret -n foo github-token \
      argocd.argoproj.io/secret-type=scm-creds
    ```

4.  Verify that the label is applied correctly by running the following command:

    ``` terminal
    $ oc get secret -n <namespace> <secret-name> --show-labels
    ```

    **Example output:**

    ``` terminal
    NAME           TYPE     DATA   AGE   LABELS
    github-token   Opaque   1      5m    argocd.argoproj.io/secret-type=scm-creds
    ```

</div>

<div>

<div class="title">

Verification

</div>

- Verify that the ApplicationSet reconciles successfully without tokenRef-related errors:

  ``` terminal
  $ oc get applicationset -n <namespace> <applicationset-name>
  ```

  Check the status section for any reconciliation errors.

- Optional: View the ApplicationSet controller logs to confirm successful reconciliation:

  ``` terminal
  $ oc logs -n <argocd-namespace> deployment/<argocd-name>-applicationset-controller
  ```

</div>

# Additional resources

- [The `ApplicationSet` resource](https://argo-cd.readthedocs.io/en/stable/operator-manual/applicationset/#the-applicationset-resource)

- [ApplicationSet in any namespace](https://argo-cd.readthedocs.io/en/stable/operator-manual/applicationset/Appset-Any-Namespace/)

- [Argo CD custom resource and component properties](../argocd_instance/argo-cd-cr-component-properties.md#argo-cd-cr-component-properties)

- [SCM Provider Generator](https://argo-cd.readthedocs.io/en/stable/operator-manual/applicationset/Generators-SCM-Provider/)

- [Pull Request Generator](https://argo-cd.readthedocs.io/en/stable/operator-manual/applicationset/Generators-Pull-Request/)

- [Argo CD — tokenRef restrictions, upstream documentation](https://argo-cd.readthedocs.io/en/stable/operator-manual/applicationset/Appset-Any-Namespace/#tokenref-restrictions)
