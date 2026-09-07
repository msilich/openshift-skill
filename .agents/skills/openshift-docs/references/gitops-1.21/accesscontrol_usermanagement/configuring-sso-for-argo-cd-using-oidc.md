<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

After the Red Hat OpenShift GitOps Operator is installed, Argo CD automatically creates a user with `admin` permissions. To manage multiple users, cluster administrators can use Argo CD to configure Single Sign-On (SSO) with external OpenID Connect (OIDC) providers.

# Understanding OIDC integration approaches for Argo CD

Argo CD supports Single Sign-On (SSO) using OpenID Connect (OIDC) providers. You can integrate Argo CD with identity providers using the following two primary approaches:

`Dex-based SSO (spec.sso)`
Argo CD uses Dex as an intermediary identity broker. Dex connects to various identity providers and presents a unified authentication interface to Argo CD.

`Direct OIDC integration (spec.oidcConfig)`
Argo CD connects directly to an external OIDC-compliant provider without using Dex as an intermediary.

Direct OIDC integration (`spec.oidcConfig`) is provider-agnostic and works with any OIDC-compliant identity provider.

This approach requires that you configure the identity provider according to its official documentation before updating the Argo CD instance configuration. For more information, see the *Additional resources* section.

# Prerequisites

- The Red Hat OpenShift GitOps Operator is installed on your OpenShift Container Platform cluster.

- You have access to the cluster with `cluster-admin` privileges.

- You have configured an OIDC-compliant identity provider according to the provider’s official documentation.

- You have obtained the following information from your OIDC provider:

  - Issuer URL

  - Client ID

  - Client secret

# Configuring direct OIDC integration for Argo CD

You can configure Argo CD to authenticate users directly with an external OIDC provider by using the `spec.oidcConfig` parameter in the Argo CD custom resource. This method bypasses Dex and connects Argo CD directly to your identity provider.

<div>

<div class="title">

Procedure

</div>

1.  Edit the ArgoCD custom resource for your instance:

    ``` terminal
    $ oc edit argocd <argocd_instance_name> -n <argocd_instance_namespace>
    ```

    Replace `<argocd_instance_name>` with the name of your Argo CD instance, for example, `openshift-gitops`, and `<argocd_instance_namespace>` with the namespace where the instance is deployed, for example, `openshift-gitops`.

2.  Add or update the `spec.oidcConfig` parameter with your OIDC provider details:

    ``` yaml
    apiVersion: argoproj.io/v1beta1
    kind: ArgoCD
    metadata:
      name: <argocd_instance_name>
      namespace: <argocd_instance_namespace>
    spec:
      oidcConfig: |
        name: <provider_name>
        issuer: https://<issuer-url>
        clientID: <client_id>
        clientSecret: <client_secret>
        requestedScopes:
          - openid
          - profile
          - email
          - groups
        requestedIDTokenClaims:
          groups:
            essential: true
        logoutURL: https://<optional-logout-url>
    ```

    where:

    `metadata.name`
    Specifies the name of your Argo CD instance.

    `metadata.namespace`
    Specifies the namespace where your Argo CD instance is deployed.

    `spec.oidcConfig.issuer`
    Specifies the OIDC issuer URL provided by your identity provider.

    `spec.oidcConfig.clientid`
    Specifies the client ID obtained from your OIDC provider.

    `spec.oidcConfig.clientSecret`
    Specifies the client secret obtained from your OIDC provider.

    `spec.oidcConfig.requestedScopes`
    Specifies the OIDC scopes to request during authentication. Common scopes include `openid`, `profile`, `email`, and `groups`. Adjust based on your provider’s supported scopes.

    `spec.oidcConfig.requestedIDTokenClaims`
    Specifies the claims to request in the ID token. This parameter is optional.

    `spec.oidcConfig.logoutURL`
    Specifies the logout URL provided by your identity provider. This parameter is optional.

    `<provider_name>`
    Specifies a a unique identifier for the OIDC provider configuration.

3.  Save the changes into a YAML file, for example, `argocd-oidc.yaml`.

4.  Apply the configuration by running the following command.

    ``` terminal
    $ oc apply -f argocd-oidc.yaml
    ```

5.  Restart the Argo CD server to apply the OIDC configuration:

    ``` terminal
    $ oc rollout restart deployment/<argocd_instance_name>-server -n <argocd_instance_namespace>
    ```

6.  Run the following command to verify that the rollout completed successfully:

    ``` terminal
    $ oc rollout status deployment/<argocd_instance_name>-server -n <argocd_instance_namespace>
    ```

    `Example output:`

    ``` terminal
    deployment "openshift-gitops-server" successfully rolled out
    ```

</div>

# Verifying OIDC login for Argo CD

After configuring direct OIDC integration, you can verify that the authentication is working correctly by accessing the Argo CD web UI and logging in with your identity provider credentials.

<div>

<div class="title">

Procedure

</div>

1.  Open the Argo CD route URL in a web browser.

2.  On the Argo CD login page, verify that a login option appears with the name you configured in the `spec.oidcConfig.name` parameter. For example, `LOG IN VIA <provider_name>`.

3.  Authenticate using your identity provider credentials.

4.  After successful authentication, verify the access and role-based permissions.

</div>

# Additional resources

- [Argo CD upstream documentation, SSO Configuration section](https://argo-cd.readthedocs.io/en/stable/operator-manual/user-management/#sso)

- [Argo CD upstream documentation, User Management section](https://argo-cd.readthedocs.io/en/stable/operator-manual/user-management/)
