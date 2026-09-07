<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

To integrate OpenShift Container Platform with an external OpenID Connect (OIDC) identity provider, configure the `oidc` identity provider by using the Authorization Code Flow. Use this integration when your organization already uses OIDC for single sign-on.

# Identity providers in OpenShift Container Platform

You can configure identity providers by creating a custom resource (CR) that describes the provider and adding it to the cluster. Identity providers enable user authentication in OpenShift Container Platform beyond the default `kubeadmin` user.

> [!NOTE]
> OpenShift Container Platform usernames containing `/`, `:`, and `%` are not supported.

# About OpenID Connect authentication

Review OpenID Connect (OIDC) discovery, scopes, and claim mapping before you configure the `oidc` identity provider. OIDC support and correctly mapped claims are required for the Authentication Operator to authenticate users in OpenShift Container Platform.

The Authentication Operator in OpenShift Container Platform requires that the configured OIDC identity provider implements the OIDC discovery specification. For more information, see "OpenID Connect Discovery".

> [!NOTE]
> `ID Token` and `UserInfo` decryptions are not supported.

By default, the `openid` scope is requested. If required, extra scopes can be specified in the `extraScopes` field.

Claims are read from the JWT `id_token` returned from the OpenID identity provider and, if specified, from the JSON returned by the `UserInfo` URL.

At least one claim must be configured to use as the identity of the user. The standard identity claim is `sub`.

You can also indicate which claims to use as the preferred username, display name, and email address of the user. If multiple claims are specified, the first one with a non-empty value is used. The following table lists the standard claims:

| Claim | Description |
|----|----|
| `sub` | Short for "subject identifier." The remote identity for the user at the issuer. |
| `preferred_username` | The preferred username when provisioning a user. A shorthand name that the user wants to be referred to, such as `janedoe`. Typically a value that corresponds to the login or username of the user in the authentication system, such as username or email. |
| `email` | Email address. |
| `name` | Display name. |

For more information, see "OpenID claims documentation".

> [!NOTE]
> Unless your OpenID Connect identity provider supports the resource owner password credentials (ROPC) grant flow, users must get a token from `<namespace_route>/oauth/token/request` to use with command-line tools.

<div>

<div class="title">

Additional resources

</div>

- [OpenID Connect Discovery (OpenID documentation)](https://openid.net/specs/openid-connect-discovery-1_0.html)

- [OpenID claims documentation](https://openid.net/specs/openid-connect-core-1_0.html#StandardClaims)

</div>

# Supported OpenID Connect providers

Review the OpenID Connect (OIDC) providers that Red Hat tests and supports with OpenShift Container Platform. Choose a provider from this list if you need a Red Hat-tested OIDC integration with OpenShift Container Platform.

The following OIDC providers are tested and supported with OpenShift Container Platform. Using an OIDC provider that is not on the following list might work with OpenShift Container Platform, but the provider was not tested by Red Hat and therefore is not supported by Red Hat.

- Active Directory Federation Services for Windows Server

  > [!NOTE]
  > Currently, it is not supported to use Active Directory Federation Services for Windows Server with OpenShift Container Platform when custom claims are used.

- GitLab

- Google

- Keycloak

- Microsoft Entra ID

  > [!NOTE]
  > Currently, it is not supported to use Microsoft Entra ID when group names are required to be synced.

- Okta

- Ping Identity

- Red Hat Single Sign-On

# Creating the secret

Create a `Secret` object in the `openshift-config` namespace to store the client secret for your identity provider. The identity provider custom resource (CR) references this secret during configuration.

<div>

<div class="title">

Procedure

</div>

1.  Create a `Secret` object containing the client secret by running the following command:

    ``` terminal
    $ oc create secret generic <secret_name> --from-literal=clientSecret=<secret> -n openshift-config
    ```

2.  Optional: Apply the following YAML to create the secret:

    ``` yaml
    apiVersion: v1
    kind: Secret
    metadata:
      name: <secret_name>
      namespace: openshift-config
    type: Opaque
    data:
      clientSecret: <base64_encoded_client_secret>
    ```

3.  Create a `Secret` object from a file by running the following command:

    ``` terminal
    $ oc create secret generic <secret_name> --from-file=<path_to_file> -n openshift-config
    ```

</div>

# Creating a ConfigMap

Create a `ConfigMap` object in the `openshift-config` namespace that contains the certificate authority bundle for the identity provider. OpenShift Container Platform uses this bundle to validate Transport Layer Security (TLS) connections to the identity provider.

<div>

<div class="title">

Procedure

</div>

1.  Define an OpenShift Container Platform `ConfigMap` object containing the CA by running the following command:

    ``` terminal
    $ oc create configmap ca-config-map --from-file=ca.crt=/path/to/ca -n openshift-config
    ```

2.  Optional: Apply the following YAML to create the config map:

    ``` yaml
    apiVersion: v1
    kind: ConfigMap
    metadata:
      name: ca-config-map
      namespace: openshift-config
    data:
      ca.crt: |
        <CA_certificate_PEM>
    ```

    The CA must be stored in the `ca.crt` key of the `ConfigMap` object.

</div>

# Sample OpenID Connect CRs

Review the sample OpenID Connect (OIDC) custom resources (CRs) before you configure the `oidc` identity provider. These examples show required parameters, acceptable values, and optional fields such as custom certificate bundles and extra scopes.

If you must specify a custom certificate bundle, extra scopes, extra authorization request parameters, or a `userInfo` URL, use the full OIDC CR.

## Standard OIDC CR

The following is an example of a standard OIDC CR.

``` yaml
apiVersion: config.openshift.io/v1
kind: OAuth
metadata:
  name: cluster
spec:
  identityProviders:
  - name: oidcidp
    mappingMethod: claim
    type: OpenID
    openID:
      clientID: ...
      clientSecret:
        name: idp-secret
      claims:
        preferredUsername:
        - preferred_username
        name:
        - name
        email:
        - email
        groups:
        - groups
      issuer: https://www.idp-issuer.com
```

where:

`spec.identityProviders.name`
Specifies that this provider name is prefixed to the value of the identity claim to form an identity name. It is also used to build the redirect URL.

`spec.identityProviders.mappingMethod`
Specifies how mappings are established between identities from this provider and `User` objects.

`spec.identityProviders.openID.clientID`
Specifies the client ID of a client registered with the OpenID provider. The client must be allowed to redirect to `https://oauth-openshift.apps.<cluster_name>.<cluster_domain>/oauth2callback/<idp_provider_name>`.

`spec.identityProviders.openID.clientSecret`
Specifies a reference to an OpenShift Container Platform `Secret` object containing the client secret.

`spec.identityProviders.openID.claims`
Specifies the list of claims to use as the identity. The first non-empty claim is used.

`spec.identityProviders.openID.issuer`
Specifies the Issuer Identifier described in the OpenID spec. Must use `https` without query or fragment component. For more information, see "Issuer Identifier".

## Full OpenID CR

The following is an example of a full OpenID Connect CR.

``` yaml
apiVersion: config.openshift.io/v1
kind: OAuth
metadata:
  name: cluster
spec:
  identityProviders:
  - name: oidcidp
    mappingMethod: claim
    type: OpenID
    openID:
      clientID: ...
      clientSecret:
        name: idp-secret
      ca:
        name: ca-config-map
      extraScopes:
      - email
      - profile
      extraAuthorizeParameters:
        include_granted_scopes: "true"
      claims:
        preferredUsername:
        - preferred_username
        - email
        name:
        - nickname
        - given_name
        - name
        email:
        - custom_email_claim
        - email
        groups:
        - groups
      issuer: https://www.idp-issuer.com
```

where:

`spec.identityProviders.openID.ca`
Specifies a reference to an OpenShift Container Platform config map containing the PEM-encoded certificate authority bundle to use in validating server certificates for the configured URL. This value is optional.

`spec.identityProviders.openID.extraScopes`
Specifies the list of scopes to request, in addition to the `openid` scope, during the authorization token request. This value is optional.

`spec.identityProviders.openID.extraAuthorizeParameters`
Specifies a map of extra parameters to add to the authorization token request. This value is optional.

`spec.identityProviders.openID.claims.preferredUsername`
Specifies the list of claims to use as the preferred username when provisioning a user for this identity. The first non-empty claim is used.

`spec.identityProviders.openID.claims.name`
Specifies the list of claims to use as the display name. The first non-empty claim is used.

`spec.identityProviders.openID.claims.email`
Specifies the list of claims to use as the email address. The first non-empty claim is used.

`spec.identityProviders.openID.claims.groups`
Specifies the list of claims to use to synchronize groups from the OpenID Connect provider to OpenShift Container Platform upon user login. The first non-empty claim is used.

<div>

<div class="title">

Additional resources

</div>

- [Identity provider parameters](../understanding-identity-provider.md#identity-provider-parameters_understanding-identity-provider)

</div>

# Adding an identity provider to your cluster

Apply the identity provider custom resource (CR) to your cluster after you define it. With this configuration, you can authenticate with the configured identity provider.

<div>

<div class="title">

Prerequisites

</div>

- You have access to a OpenShift Container Platform cluster.

- You have created the CR for your identity providers.

- You are logged in as an administrator.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Apply the defined CR by running the following command:

    ``` terminal
    $ oc apply -f </path/to/CR>
    ```

    > [!NOTE]
    > If a CR does not exist, `oc apply` creates a new CR and might trigger the following warning: `Warning: oc apply should be used on resources created by either oc create --save-config or oc apply`. In this case you can safely ignore this warning.

2.  Obtain a token from the OAuth server.

    As long as the `kubeadmin` user has been removed, the `oc login` command provides instructions on how to access a web page where you can retrieve the token.

    You can also access this page from the web console by navigating to **(?) Help** → **Command Line Tools** → **Copy Login Command**.

3.  Log in to the cluster by running the following command, passing in the token to authenticate:

    ``` terminal
    $ oc login --token=<token>
    ```

    > [!NOTE]
    > If your OpenID Connect identity provider supports the resource owner password credentials (ROPC) grant flow, you can log in with a username and password. You might need to take steps to enable the ROPC grant flow for your identity provider.

4.  After the OIDC identity provider is configured in OpenShift Container Platform, log in by running the following command. The command prompts you for your username and password:

    ``` terminal
    $ oc login -u <identity_provider_username> --server=<api_server_url_and_port>
    ```

    If your OpenID Connect identity provider supports the resource owner password credentials (ROPC) grant flow, you might need to take steps to enable the ROPC grant flow for your identity provider.

5.  Confirm that the user logged in successfully and that the username displays by running the following command:

    ``` terminal
    $ oc whoami
    ```

</div>

# Configuring identity providers using the web console

You can configure identity providers on your OpenShift Container Platform cluster through the web console by updating the **OAuth** settings in the **Cluster Settings**.

<div>

<div class="title">

Prerequisites

</div>

- You are logged in to the web console as a cluster administrator.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Navigate to **Administration** → **Cluster Settings**.

2.  Under the **Configuration** tab, click **OAuth**.

3.  Under the **Identity Providers** section, select your identity provider from the **Add** drop-down list.

    > [!NOTE]
    > You can specify multiple identity providers through the web console without overwriting existing identity providers.

</div>

# Additional resources

- [Authorization Code Flow](https://openid.net/specs/openid-connect-core-1_0.html#CodeFlowAuth)

- [Issuer Identifier](https://openid.net/specs/openid-connect-core-1_0.html#IssuerIdentifier)
