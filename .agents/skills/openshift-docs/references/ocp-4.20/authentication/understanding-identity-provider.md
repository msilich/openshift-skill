<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

As an administrator, you can configure OAuth to specify an identity provider after you install your cluster. Developers and administrators obtain OAuth access tokens to authenticate themselves to the API.

The OpenShift Container Platform master includes a built-in OAuth server.

# About identity providers in OpenShift Container Platform

You can configure identity providers by creating a custom resource (CR) that describes the provider and adding it to the cluster. Identity providers enable user authentication in OpenShift Container Platform beyond the default `kubeadmin` user.

> [!NOTE]
> OpenShift Container Platform user names containing `/`, `:`, and `%` are not supported.

# Supported identity providers

You can configure the following types of identity providers:

| Identity provider | Description |
|----|----|
| [htpasswd](identity_providers/configuring-htpasswd-identity-provider.md#configuring-htpasswd-identity-provider) | Configure the `htpasswd` identity provider to validate user names and passwords against a flat file generated using [`htpasswd`](http://httpd.apache.org/docs/2.4/programs/htpasswd.html). |
| [Keystone](identity_providers/configuring-keystone-identity-provider.md#configuring-keystone-identity-provider) | Configure the `keystone` identity provider to integrate your OpenShift Container Platform cluster with Keystone to enable shared authentication with an OpenStack Keystone v3 server configured to store users in an internal database. |
| [LDAP](identity_providers/configuring-ldap-identity-provider.md#configuring-ldap-identity-provider) | Configure the `ldap` identity provider to validate user names and passwords against an LDAPv3 server, using simple bind authentication. |
| [Basic authentication](identity_providers/configuring-basic-authentication-identity-provider.md#configuring-basic-authentication-identity-provider) | Configure a `basic-authentication` identity provider for users to log in to OpenShift Container Platform with credentials validated against a remote identity provider. Basic authentication is a generic backend integration mechanism. |
| [Request header](identity_providers/configuring-request-header-identity-provider.md#configuring-request-header-identity-provider) | Configure a `request-header` identity provider to identify users from request header values, such as `X-Remote-User`. It is typically used in combination with an authenticating proxy, which sets the request header value. |
| [GitHub or GitHub Enterprise](identity_providers/configuring-github-identity-provider.md#configuring-github-identity-provider) | Configure a `github` identity provider to validate user names and passwords against GitHub or GitHub Enterprise’s OAuth authentication server. |
| [GitLab](identity_providers/configuring-gitlab-identity-provider.md#configuring-gitlab-identity-provider) | Configure a `gitlab` identity provider to use [GitLab.com](https://gitlab.com/) or any other GitLab instance as an identity provider. |
| [Google](identity_providers/configuring-google-identity-provider.md#configuring-google-identity-provider) | Configure a `google` identity provider using [Google’s OpenID Connect integration](https://developers.google.com/identity/protocols/OpenIDConnect). |
| [OpenID Connect](identity_providers/configuring-oidc-identity-provider.md#configuring-oidc-identity-provider) | Configure an `oidc` identity provider to integrate with an OpenID Connect identity provider using an [Authorization Code Flow](http://openid.net/specs/openid-connect-core-1_0.html#CodeFlowAuth). |

Once an identity provider has been defined, you can [use RBAC to define and apply permissions](using-rbac.md#authorization-overview_using-rbac).

# Removing the kubeadmin user

After you define an identity provider and create a new `cluster-admin` user, you can remove the `kubeadmin` to improve cluster security.

> [!WARNING]
> If you follow this procedure before another user is a `cluster-admin`, then OpenShift Container Platform must be reinstalled. It is not possible to undo this command.

<div>

<div class="title">

Prerequisites

</div>

- You must have configured at least one identity provider.

- You must have added the `cluster-admin` role to a user.

- You must be logged in as an administrator.

</div>

<div>

<div class="title">

Procedure

</div>

- Remove the `kubeadmin` secrets:

  ``` terminal
  $ oc delete secrets kubeadmin -n kube-system
  ```

</div>

# Identity provider parameters

The following parameters are common to all identity providers:

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 80%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Parameter</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>name</code></p></td>
<td style="text-align: left;"><p>The provider name is prefixed to provider user names to form an identity name.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>mappingMethod</code></p></td>
<td style="text-align: left;"><p>Defines how new identities are mapped to users when they log in. Enter one of the following values:</p>
<dl>
<dt>claim</dt>
<dd>
<p>The default value. Provisions a user with the identity’s preferred user name. Fails if a user with that user name is already mapped to another identity.</p>
</dd>
<dt>lookup</dt>
<dd>
<p>Looks up an existing identity, user identity mapping, and user, but does not automatically provision users or identities. This allows cluster administrators to set up identities and users manually, or using an external process. Using this method requires you to manually provision users.</p>
</dd>
<dt>add</dt>
<dd>
<p>Provisions a user with the identity’s preferred user name. If a user with that user name already exists, the identity is mapped to the existing user, adding to any existing identity mappings for the user. Required when multiple identity providers are configured that identify the same set of users and map to the same user names.</p>
</dd>
</dl></td>
</tr>
</tbody>
</table>

> [!NOTE]
> When adding or changing identity providers, you can map identities from the new provider to existing users by setting the `mappingMethod` parameter to `add`.

# Sample identity provider CR

You can use a custom resource (CR) to see the parameters and default values that you use to configure an identity provider.

The following example uses the htpasswd identity provider.

<div class="formalpara">

<div class="title">

Sample identity provider CR

</div>

``` yaml
apiVersion: config.openshift.io/v1
kind: OAuth
metadata:
  name: cluster
spec:
  identityProviders:
  - name: my_identity_provider
    mappingMethod: claim
    type: HTPasswd
    htpasswd:
      fileData:
        name: htpass-secret
```

</div>

where:

`spec.identityProviders.name`
Specifies the provider name, which is prefixed to provider user names to form an identity name.

`spec.identityProviders.mappingMethod`
Specifies how mappings are established between this provider’s identities and `User` objects.

`spec.identityProviders.htpasswd.fileData.name`
Specifies an existing secret containing a file generated using [`htpasswd`](http://httpd.apache.org/docs/2.4/programs/htpasswd.html).

# Manually provisioning a user when using the lookup mapping method

You can manually provision users when the `lookup` mapping method is enabled. The `lookup` method disables automatic identity-to-user mapping during login, requiring manual provisioning of each user after configuring the identity provider.

<div>

<div class="title">

Prerequisites

</div>

- You have installed the OpenShift CLI (`oc`).

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create an OpenShift Container Platform user:

    ``` terminal
    $ oc create user <username>
    ```

2.  Create an OpenShift Container Platform identity:

    ``` terminal
    $ oc create identity <identity_provider>:<identity_provider_user_id>
    ```

    Where `<identity_provider_user_id>` is a name that uniquely represents the user in the identity provider.

3.  Create a user identity mapping for the created user and identity:

    ``` terminal
    $ oc create useridentitymapping <identity_provider>:<identity_provider_user_id> <username>
    ```

</div>

<div>

<div class="title">

Additional resources

</div>

- [How to create user, identity and map user and identity in LDAP authentication for `mappingMethod` as `lookup` inside the OAuth manifest](https://access.redhat.com/solutions/6006921)

- [How to create user, identity and map user and identity in OIDC authentication for `mappingMethod` as `lookup`](https://access.redhat.com/solutions/7072510)

</div>
