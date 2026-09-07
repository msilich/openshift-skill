<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

The Argo CD Operator supports local users and automatically generates and renews API tokens. Administrators can define local users in the Argo CD custom resource (CR), and the Red Hat OpenShift GitOps Operator manages their API tokens.

# About local user management in Argo CD

Local users are intended for automation scenarios that require API tokens or for small teams where configuring single sign-on (SSO) is not necessary.

The Argo CD Operator manages local users by performing the following actions:

- Creating and managing user accounts defined in the Argo CD CR

- Generating JSON Web Token (JWT) API tokens

- Configuring token lifetimes and automatic renewal

- Storing tokens securely in Kubernetes secrets

- Cleaning up users and tokens when they are removed from the configuration

# Local user configuration in Argo CD

Local users are defined in the `.spec.localUsers` field of the Argo CD custom resource (CR). Each user definition includes required and optional configuration fields.

The following table describes configuration fields for local users.

| Field | Type | Default value | Description | Optional |
|----|----|----|----|----|
| `name` | String | None | Unique username for the local user. | No |
| `enabled` | Boolean | `true` | Enables or disables the user. Disabled users cannot login or use an API token to access the Argo CD instance, but their configuration and tokens are preserved. | Yes |
| `apiKey` | Boolean | `true` | Enables API token generation for the user. | Yes |
| `login` | Boolean | `false` | Enables login through the Argo CD web UI. If enabled, you must set a password manually by using the Argo CD CLI. | Yes |
| `tokenLifetime` | String | `0h` | Duration that the token remains valid, for example `24h` or `168h`. Uses the Go duration format. The default `0h` value creates a non-expiring token. | Yes |
| `autoRenewToken` | Boolean | `true` | Enables automatic renewal before expiration. Applies only when `tokenLifetime` is greater than `0h`. | Yes |

The following configuration creates two local users in an Argo CD CR, each with different API key settings.

``` yaml
apiVersion: argoproj.io/v1beta1
kind: ArgoCD
metadata:
  name: example-argocd
  namespace: argocd
spec:
  localUsers:
    - name: api-user
      apiKey: true
      tokenLifetime: "24h"
      autoRenewToken: true
    - name: service-account
      apiKey: true
      tokenLifetime: "168h"
      autoRenewToken: false
```

# Example local user configuration in Argo CD

You can configure local users for Argo CD in several ways based on your needs, such as long-lived API tokens, renewable tokens, or UI login access. The following examples show common patterns for local users.

| User type | Login enabled | API key | Token lifetime | Auto-renew |
|----|----|----|----|----|
| Basic local user | No | Yes | Non-expiring | No |
| Expiring token user | No | Yes | 30 days | Yes |
| Long-lived token user | No | Yes | 1 year | No |
| User with login capability | Yes | Yes | 24 hours | Yes |
| Disabled user | No | Yes | Retains configuration | No |
| API-only user | No | Yes | 7 days | Yes |

Summary of local user configuration

The following configuration creates a local user named `developer` with API key enabled and a non-expiring token.

``` yaml
apiVersion: argoproj.io/v1beta1
kind: ArgoCD
metadata:
  name: example-argocd
spec:
  localUsers:
    - name: developer
```

The following configuration creates a user with a 30-day token lifetime and automatic renewal.

``` yaml
apiVersion: argoproj.io/v1beta1
kind: ArgoCD
metadata:
  name: example-argocd
spec:
  localUsers:
    - name: ci-system
      apiKey: true
      tokenLifetime: "720h"
      autoRenewToken: true
```

The following configuration creates a user with a one-year token lifetime without automatic renewal.

``` yaml
apiVersion: argoproj.io/v1beta1
kind: ArgoCD
metadata:
  name: example-argocd
spec:
  localUsers:
    - name: monitoring
      apiKey: true
      tokenLifetime: "8760h"  # 1 year
      autoRenewToken: false
```

The following configuration creates a user who can log in to the Argo CD web UI and also use an API token.

``` yaml
apiVersion: argoproj.io/v1beta1
kind: ArgoCD
metadata:
  name: example-argocd
spec:
  localUsers:
    - name: developer
      enabled: true
      login: true
      apiKey: true
      tokenLifetime: "24h"
      autoRenewToken: true
```

> [!IMPORTANT]
> When `login: true` is enabled, you must set a password manually by using the Argo CD CLI. You cannot log in to the Argo CD web UI without a password.

The following configuration defines a user account that is disabled but retains its configuration and token data.

``` yaml
apiVersion: argoproj.io/v1beta1
kind: ArgoCD
metadata:
  name: example-argocd
spec:
  localUsers:
    - name: temp-user
      enabled: false
      apiKey: true
```

The following configuration creates a user for programmatic access with API key enabled, UI login disabled, and a renewable 7-day token.

``` yaml
apiVersion: argoproj.io/v1beta1
kind: ArgoCD
metadata:
  name: example-argocd
spec:
  localUsers:
    - name: automation
      enabled: true
      login: false
      apiKey: true
      tokenLifetime: "168h"
      autoRenewToken: true
```

# Token storage and access

For each local user, the Argo CD Operator creates a Kubernetes secret in the same namespace as the Argo CD instance. The secret name follows the format `{username}-local-user`.

The following example shows the Kubernetes `Secret` that stores a local user’s API token and configuration details.

``` yaml
apiVersion: v1
kind: Secret
metadata:
  name: api-user-local-user
  namespace: argocd
  labels:
    app.kubernetes.io/component: local-users
    app.kubernetes.io/managed-by: argocd-operator
type: Opaque
data:
  apiToken: base64-encoded-jwt-token
  user: base64-encoded-username
  expAt: base64-encoded-expiration-timestamp
  tokenLifetime: base64-encoded-lifetime-setting
  autoRenew: base64-encoded-auto-renew-setting
```

> [!IMPORTANT]
> The values in the secret are base64-encoded. You must decode them before using.

Retrieve tokens
You can retrieve a user’s API token from the Kubernetes secret, as shown in the following example:

``` terminal
$ oc get secret api-user-local-user -n argocd -o jsonpath='{.data.apiToken}' | base64 -d
```

Use tokens
You can use the retrieved token with the Argo CD CLI to list applications, as shown in the following example. The token can also be used with other Argo CD CLI commands in a similar way.

``` terminal
$ argocd --server <argocd_server> --auth-token <token> app list
```

# Token lifecycle management

The Argo CD Operator manages the lifecycle of local user tokens. Depending on the configuration, tokens can be renewed automatically or rotated manually.

**Automatic renewal**

You can configure the Operator to automatically renew tokens before they expire. This ensures that automation and integrations that depend on the token continue to work without interruption.

**Manual token rotation**

If you need to replace a token immediately, you can manually rotate it by deleting the user secret, as shown in the following example:

``` terminal
$ oc delete secret api-user-local-user -n argocd
```

The Argo CD Operator then generates a new token and updates the configuration.

**Disable API keys**

You can disable API key generation for a local user to remove their access through tokens. Disabling API keys also cleans up the associated secrets and stops renewal timers. To disable API key generation, you can set `apikey` field to `false`.

# User lifecycle management

The Argo CD Operator also manages the lifecycle of local user accounts. You can temporarily disable users without removing them from the configuration, or permanently remove them when they are no longer required.

Disable users
You can disable a user by setting the `enabled` field to `false`. When a user is disabled, the following behaviors apply:

- The user account remains in the Argo CD configuration, but it is set to disabled.

- The user secret and tokens are preserved.

- The user cannot authenticate by using the UI or by the API tokens.

- Token renewal timers continue to run, if configured.

- Re-enabling the user (`enabled: true`) immediately restores access.

User removal
You can remove a user completely by deleting the entry from the `localUsers` list in the Argo CD CR. When a user is removed, the following behaviors apply:

- The user secret is deleted.

- The token is removed from the Argo CD configuration.

- Any scheduled token renewal timers are canceled.

- The user account is removed from Argo CD.

# Integration with legacy configuration

The Argo CD Operator recognizes users defined in the `extraConfig` section of the Argo CD custom resource (CR). Tokens defined for these users are not managed by the Operator. This behavior supports gradual migration from manually managed users to Operator-managed users.

``` yaml
# ...
spec:
  extraConfig:
    accounts.legacy-user: apiKey
  localUsers:
    - name: new-user
      apiKey: true
# ...
```

> [!IMPORTANT]
> A user must be defined in only one section, either `extraConfig` or `localUsers`. If a user appears in both sections, the definition in `extraConfig` takes precedence and the definition in `localUsers` is ignored.

# Creating local users in Argo CD

You can configure local users with API keys for access to Argo CD. The Argo CD Operator manages these users and securely generates API tokens for service accounts or automation scripts.

<div>

<div class="title">

Prerequisites

</div>

- You are logged in to the OpenShift Container Platform cluster as an administrator.

- You installed the Red Hat OpenShift GitOps Operator on your OpenShift Container Platform cluster.

- You can access the default Argo CD instance in the `openshift-gitops` namespace.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Edit the Argo CD custom resource (CR) for your instance by running the following command:

    ``` terminal
    $ oc edit argocd <argocd_instance_name> -n <namespace>
    ```

2.  In the `spec` section of the Argo CD CR, add a `localUsers` configuration. For example:

    ``` yaml
    spec:
      localUsers:
      - name: "alice"
        enabled: true
        apiKey: true
        login: false
        tokenLifetime: "24h"
        autoRenewToken: true
      - name: "service-account"
        enabled: true
        apiKey: true
        login: false
        tokenLifetime: "0h"  # Infinite lifetime
        autoRenewToken: false
    ```

3.  Save and close the file.

    The Operator reconciles the changes and creates the required secrets and API tokens automatically.

</div>

# Additional resources

- [Argo CD user management documentation](https://argo-cd.readthedocs.io/en/stable/operator-manual/user-management/)

- [Installing the Red Hat OpenShift GitOps Operator](../installing_gitops/installing-openshift-gitops.md#installing-openshift-gitops)
