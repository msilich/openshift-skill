<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

You can configure webhook secrets for Git providers declaratively by using the `Argo CD` custom resource (CR). This allows you to manage webhook credentials alongside your GitOps configuration instead of manually updating the `argocd-secret` secret.

# Declarative webhook secrets for Git providers

Argo CD uses webhook secrets to validate incoming webhook requests from Git providers. You can configure webhook secrets declaratively by using the `spec.webhookSecrets` field in the `Argo CD` custom resource (CR).

Using declarative webhook secrets provides the following benefits:

- Manage webhook secrets together with Argo CD configuration

- Integrate with Kubernetes secret management tools, such as Sealed Secrets or External Secrets Operator

- Simplify operations by allowing the Red Hat OpenShift GitOps Operator to synchronize referenced secret values to the `argocd-secret` secret

- Configure webhook secrets for multiple Git providers in a single `ArgoCD` CR

When you configure `spec.webhookSecrets`, the Red Hat OpenShift GitOps Operator automatically populates the required keys in the `argocd-secret` secret that Argo CD uses internally.

> [!IMPORTANT]
> The referenced `Secret` resource must exist in the same namespace as the `Argo CD` CR. Cross-namespace secret references are not supported.

The following Git providers are supported for declarative webhook secret configuration:

| Provider | Field in `spec.webhookSecrets` | Required secret reference |
|----|----|----|
| GitHub | `github` | `webhookSecretRef` |
| GitLab | `gitlab` | `webhookSecretRef` |
| Bitbucket Cloud | `bitbucket` | `webhookUUIDSecretRef` |
| Bitbucket Server | `bitbucketServer` | `webhookSecretRef` |
| Gogs | `gogs` | `webhookSecretRef` |
| Azure DevOps | `azureDevOps` | `usernameSecretRef` and `passwordSecretRef` |

> [!NOTE]
> When `spec.webhookSecrets` is configured, the Red Hat OpenShift GitOps Operator synchronizes webhook secret values only for the declared providers. Webhook keys for providers that are not declared in `spec.webhookSecrets` might be removed from the `argocd-secret` secret.

> [!IMPORTANT]
> Do not store plain-text secrets in Git repositories. Use secret management solutions, such as sealed secrets or external secrets Operator, to manage sensitive data securely.

# Create webhook secrets using the Argo CD CR

You can configure webhook secrets for Git providers by creating a Kubernetes `Secret` resource and referencing it in the `Argo CD` custom resource (CR).

<div>

<div class="title">

Prerequisites

</div>

- You have installed the Red Hat OpenShift GitOps Operator.

- You have created an `ArgoCD` instance.

- You have configured a webhook in your Git provider.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create a `Secret` resource in the same namespace as the `ArgoCD` CR and configure the `spec.webhookSecrets` field in the `ArgoCD` CR.

    The following example configures a webhook secret for GitHub:

    ``` yaml
    apiVersion: v1
    kind: Secret
    metadata:
      name: github-webhook-credentials
      namespace: argocd
      labels:
        app.kubernetes.io/part-of: argocd
        app.kubernetes.io/component: webhook
    type: Opaque
    stringData:
      token: "your-github-webhook-secret"
    ---
    apiVersion: argoproj.io/v1beta1
    kind: ArgoCD
    metadata:
      name: example-argocd
      namespace: argocd
    spec:
      webhookSecrets:
        github:
          webhookSecretRef:
            name: github-webhook-credentials
            key: token
    ```

2.  Apply the configuration:

    ``` terminal
    $ oc apply -f webhook-secret.yaml
    ```

</div>

# Verify declarative webhook secret configuration

After configuring declarative webhook secrets, verify that the Red Hat OpenShift GitOps Operator synchronized the webhook secret values to the `argocd-secret` secret.

<div>

<div class="title">

Procedure

</div>

1.  Run the following command to verify the configured GitHub webhook secret:

    ``` terminal
    $ oc get secret argocd-secret -n <namespace> -o jsonpath='{.data.webhook\.github\.secret}' | base64 -d
    ```

    where:

    `<namespace>`
    Specifies the namespace where your Argo CD instance is installed, such as `openshift-gitops` for the default instance.

2.  Verify that the command output matches the value stored in the Secret referenced by `spec.webhookSecrets.github.webhookSecretRef`.

    > [!NOTE]
    > After updating webhook secrets, the Argo CD server might need to restart to pick up the updated values.
    >
    > Run the following command to restart the Argo CD server deployment:
    >
    > ``` terminal
    > $ oc rollout restart deployment/<argocd_cr_name>-server -n <namespace>
    > ```
    >
    > where:
    >
    > `<argocd_cr_name>`
    > Specifies the name of your Argo CD custom resource.
    >
    > `<namespace>`
    > Specifies the namespace where your Argo CD instance is installed.

</div>

# Additional resources

- [Setting up a new Argo CD instance](setting-up-argocd-instance.md#setting-up-argocd-instance)

- [Argo CD custom resource and component properties](argo-cd-cr-component-properties.md#argo-cd-cr-component-properties)

- [Argo CD Webhook Secrets](https://argocd-operator.readthedocs.io/en/latest/usage/webhook-secrets/)
