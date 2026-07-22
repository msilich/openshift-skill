<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Configure the `oidc` identity provider to integrate with an OpenID Connect identity provider using an [Authorization Code Flow](http://openid.net/specs/openid-connect-core-1_0.html#CodeFlowAuth).

# About identity providers in OpenShift Container Platform

You can configure identity providers by creating a custom resource (CR) that describes the provider and adding it to the cluster. Identity providers enable user authentication in OpenShift Container Platform beyond the default `kubeadmin` user.

> [!NOTE]
> OpenShift Container Platform user names containing `/`, `:`, and `%` are not supported.

# About OpenID Connect authentication

The Authentication Operator in OpenShift Container Platform requires that the configured OpenID Connect identity provider implements the [OpenID Connect Discovery](https://openid.net/specs/openid-connect-discovery-1_0.html) specification.

> [!NOTE]
> `ID Token` and `UserInfo` decryptions are not supported.

By default, the `openid` scope is requested. If required, extra scopes can be specified in the `extraScopes` field.

Claims are read from the JWT `id_token` returned from the OpenID identity provider and, if specified, from the JSON returned by the `UserInfo` URL.

At least one claim must be configured to use as the user’s identity. The standard identity claim is `sub`.

You can also indicate which claims to use as the user’s preferred user name, display name, and email address. If multiple claims are specified, the first one with a non-empty value is used. The following table lists the standard claims:

| Claim | Description |
|----|----|
| `sub` | Short for "subject identifier." The remote identity for the user at the issuer. |
| `preferred_username` | The preferred user name when provisioning a user. A shorthand name that the user wants to be referred to as, such as `janedoe`. Typically a value that corresponding to the user’s login or username in the authentication system, such as username or email. |
| `email` | Email address. |
| `name` | Display name. |

See the [OpenID claims documentation](http://openid.net/specs/openid-connect-core-1_0.html#StandardClaims) for more information.

> [!NOTE]
> Unless your OpenID Connect identity provider supports the resource owner password credentials (ROPC) grant flow, users must get a token from `<namespace_route>/oauth/token/request` to use with command-line tools.

# Supported OIDC providers

Red Hat tests and supports specific OpenID Connect (OIDC) providers with OpenShift Container Platform. The following OpenID Connect (OIDC) providers are tested and supported with OpenShift Container Platform. Using an OIDC provider that is not on the following list might work with OpenShift Container Platform, but the provider was not tested by Red Hat and therefore is not supported by Red Hat.

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

Identity providers use OpenShift Container Platform `Secret` objects in the `openshift-config` namespace to contain the client secret, client certificates, and keys.

<div>

<div class="title">

Procedure

</div>

- Create a `Secret` object containing a string by using the following command:

  ``` terminal
  $ oc create secret generic <secret_name> --from-literal=clientSecret=<secret> -n openshift-config
  ```

  > [!TIP]
  > You can alternatively apply the following YAML to create the secret:
  >
  > ``` yaml
  > apiVersion: v1
  > kind: Secret
  > metadata:
  >   name: <secret_name>
  >   namespace: openshift-config
  > type: Opaque
  > data:
  >   clientSecret: <base64_encoded_client_secret>
  > ```

- You can define a `Secret` object containing the contents of a file by using the following command:

  ``` terminal
  $ oc create secret generic <secret_name> --from-file=<path_to_file> -n openshift-config
  ```

</div>

# Creating a config map

Identity providers use OpenShift Container Platform `ConfigMap` objects in the `openshift-config` namespace to contain the certificate authority bundle. These are primarily used to contain certificate bundles needed by the identity provider.

<div>

<div class="title">

Procedure

</div>

- Define an OpenShift Container Platform `ConfigMap` object containing the certificate authority by using the following command. The certificate authority must be stored in the `ca.crt` key of the `ConfigMap` object.

  ``` terminal
  $ oc create configmap ca-config-map --from-file=ca.crt=/path/to/ca -n openshift-config
  ```

  > [!TIP]
  > You can alternatively apply the following YAML to create the config map:
  >
  > ``` yaml
  > apiVersion: v1
  > kind: ConfigMap
  > metadata:
  >   name: ca-config-map
  >   namespace: openshift-config
  > data:
  >   ca.crt: |
  >     <CA_certificate_PEM>
  > ```

</div>

# Sample OpenID Connect CRs

The following custom resources (CRs) show the parameters and acceptable values for an OpenID Connect identity provider.

If you must specify a custom certificate bundle, extra scopes, extra authorization request parameters, or a `userInfo` URL, use the full OpenID Connect CR.

<div class="formalpara">

<div class="title">

Standard OpenID Connect CR

</div>

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

</div>

- This provider name is prefixed to the value of the identity claim to form an identity name. It is also used to build the redirect URL.

- Controls how mappings are established between this provider’s identities and `User` objects.

- The client ID of a client registered with the OpenID provider. The client must be allowed to redirect to `https://oauth-openshift.apps.<cluster_name>.<cluster_domain>/oauth2callback/<idp_provider_name>`.

- A reference to an OpenShift Container Platform `Secret` object containing the client secret.

- The list of claims to use as the identity. The first non-empty claim is used.

- The [Issuer Identifier](https://openid.net/specs/openid-connect-core-1_0.html#IssuerIdentifier) described in the OpenID spec. Must use `https` without query or fragment component.

<div class="formalpara">

<div class="title">

Full OpenID Connect CR

</div>

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

</div>

- Optional: Reference to an OpenShift Container Platform config map containing the PEM-encoded certificate authority bundle to use in validating server certificates for the configured URL.

- Optional: The list of scopes to request, in addition to the `openid` scope, during the authorization token request.

- Optional: A map of extra parameters to add to the authorization token request.

- The list of claims to use as the preferred user name when provisioning a user for this identity. The first non-empty claim is used.

- The list of claims to use as the display name. The first non-empty claim is used.

- The list of claims to use as the email address. The first non-empty claim is used.

- The list of claims to use to synchronize groups from the OpenID Connect provider to OpenShift Container Platform upon user login. The first non-empty claim is used.

<div>

<div class="title">

Additional resources

</div>

- See [Identity provider parameters](../understanding-identity-provider.md#identity-provider-parameters_understanding-identity-provider) for information on parameters, such as `mappingMethod`, that are common to all identity providers.

</div>

# Adding an identity provider to your cluster

After you install your cluster, add an identity provider to it so your users can authenticate.

<div>

<div class="title">

Prerequisites

</div>

- Create an OpenShift Container Platform cluster.

- Create the custom resource (CR) for your identity providers.

- You must be logged in as an administrator.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Apply the defined CR:

    ``` terminal
    $ oc apply -f </path/to/CR>
    ```

    > [!NOTE]
    > If a CR does not exist, `oc apply` creates a new CR and might trigger the following warning: `Warning: oc apply should be used on resources created by either oc create --save-config or oc apply`. In this case you can safely ignore this warning.

2.  Obtain a token from the OAuth server.

    As long as the `kubeadmin` user has been removed, the `oc login` command provides instructions on how to access a web page where you can retrieve the token.

    You can also access this page from the web console by navigating to **(?) Help** → **Command Line Tools** → **Copy Login Command**.

3.  Log in to the cluster, passing in the token to authenticate.

    ``` terminal
    $ oc login --token=<token>
    ```

    > [!NOTE]
    > If your OpenID Connect identity provider supports the resource owner password credentials (ROPC) grant flow, you can log in with a user name and password. You might need to take steps to enable the ROPC grant flow for your identity provider.
    >
    > After the OIDC identity provider is configured in OpenShift Container Platform, you can log in by using the following command, which prompts for your user name and password:
    >
    > ``` terminal
    > $ oc login -u <identity_provider_username> --server=<api_server_url_and_port>
    > ```

4.  Confirm that the user logged in successfully, and display the user name.

    ``` terminal
    $ oc whoami
    ```

</div>

# Configuring identity providers using the web console

Configure your identity provider (IDP) through the web console instead of the CLI.

<div>

<div class="title">

Prerequisites

</div>

- You must be logged in to the web console as a cluster administrator.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Navigate to **Administration** → **Cluster Settings**.

2.  Under the **Configuration** tab, click **OAuth**.

3.  Under the **Identity Providers** section, select your identity provider from the **Add** drop-down menu.

</div>

> [!NOTE]
> You can specify multiple IDPs through the web console without overwriting existing IDPs.
