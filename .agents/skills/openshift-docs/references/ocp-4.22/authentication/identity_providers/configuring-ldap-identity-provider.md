<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Configure an LDAP identity provider so users can log in to OpenShift Container Platform with usernames and passwords validated against your LDAPv3 directory.

# Identity providers in OpenShift Container Platform

You can configure identity providers by creating a custom resource (CR) that describes the provider and adding it to the cluster. Identity providers enable user authentication in OpenShift Container Platform beyond the default `kubeadmin` user.

> [!NOTE]
> OpenShift Container Platform usernames containing `/`, `:`, and `%` are not supported.

# About LDAP authentication

Review how usernames and passwords are validated against the LDAP directory so you can configure the LDAP identity provider correctly.

During authentication, the LDAP directory is searched for an entry that matches the provided username. If a single unique match is found, a simple bind is attempted using the distinguished name (DN) of the entry plus the provided password.

LDAP authentication uses the following process:

1.  Generates a search filter by combining the attribute and filter in the configured `url` with the user-provided username.

2.  Searches the directory using the generated filter. Denies access if the search does not return exactly one entry.

3.  Attempts to bind to the LDAP server using the DN of the entry retrieved from the search, and the user-provided password.

4.  Denies access if the bind is unsuccessful.

5.  Builds an identity using the configured attributes as the identity, email address, display name, and preferred username if the bind is successful.

The configured `url` is an RFC 2255 URL, which specifies the LDAP host and search parameters to use. The syntax of the URL is:

    ldap://host:port/basedn?attribute?scope?filter

For this URL:

| URL component | Description |
|----|----|
| `ldap` | For regular LDAP, use the string `ldap`. For secure LDAP (LDAPS), use `ldaps` instead. |
| `host:port` | The name and port of the LDAP server. Defaults to `localhost:389` for LDAP and `localhost:636` for LDAPS. |
| `basedn` | The DN of the branch of the directory where all searches should start from. At the very least, this must be the top of your directory tree, but it could also specify a subtree in the directory. |
| `attribute` | The attribute to search for. Although RFC 2255 allows a comma-separated list of attributes, only the first attribute is used, no matter how many are provided. If no attributes are provided, the default is to use `uid`. It is recommended to choose an attribute that is unique across all entries in the subtree you are using. |
| `scope` | The scope of the search. Can be either `one` or `sub`. If the scope is not provided, the default is to use a scope of `sub`. |
| `filter` | A valid LDAP search filter. If not provided, defaults to `(objectClass=*)` |

During a search, the attribute and filter from the configured `url` are combined with the user-provided username to create a search filter in the following format:

    (&(<filter>)(<attribute>=<username>))

For example, consider a URL of:

    ldap://ldap.example.com/o=Acme?cn?sub?(enabled=true)

When a client attempts to connect using username `bob`, the resulting search filter is `(&(enabled=true)(cn=bob))`.

If the LDAP directory requires authentication to search, specify a `bindDN` and `bindPassword` to use to perform the entry search.

# Creating the LDAP secret

Create a secret that contains the LDAP bind password in the `openshift-config` namespace so the identity provider can authenticate to the directory.

<div>

<div class="title">

Procedure

</div>

- Create a `Secret` object that contains the `bindPassword` field by running the following command:

  ``` terminal
  $ oc create secret generic ldap-secret --from-literal=bindPassword=<secret> -n openshift-config
  ```

  where:

  `<secret>`
  Specifies the LDAP bind password value for the `--from-literal` argument. The key name must be `bindPassword`.

- Alternatively, apply the following YAML to create the secret:

  ``` yaml
  apiVersion: v1
  kind: Secret
  metadata:
    name: ldap-secret
    namespace: openshift-config
  type: Opaque
  data:
    bindPassword: <base64_encoded_bind_password>
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

# Sample LDAP custom resource

Review the sample LDAP custom resource (CR) and acceptable parameter values so you can configure attribute mappings, bind credentials, and connection settings for the LDAP identity provider.

``` yaml
apiVersion: config.openshift.io/v1
kind: OAuth
metadata:
  name: cluster
spec:
  identityProviders:
  - name: ldapidp
    mappingMethod: claim
    type: LDAP
    ldap:
      attributes:
        id:
        - dn
        email:
        - mail
        name:
        - cn
        preferredUsername:
        - uid
      bindDN: ""
      bindPassword:
        name: ldap-secret
      ca:
        name: ca-config-map
      insecure: false
      url: "ldaps://ldaps.example.com/ou=users,dc=acme,dc=com?uid"
```

where:

`spec.identityProviders.name`
Specifies the provider name. The provider name is prefixed to the returned user ID to form an identity

`spec.identityProviders.mappingMethod`
Specifies how mappings are established between the identities of this provider and `User` objects.

`spec.identityProviders.ldap.attributes.id`
Specifies the list of attributes to use as the identity. The first non-empty attribute is used. At least one attribute is required. If none of the listed attributes have a value, authentication fails. Defined attributes are retrieved as raw, allowing binary values to be used.

`spec.identityProviders.ldap.attributes.email`
Specifies the list of attributes to use as the email address. The first non-empty attribute is used.

`spec.identityProviders.ldap.attributes.name`
Specifies the list of attributes to use as the display name. The first non-empty attribute is used.

`spec.identityProviders.ldap.attributes.preferredUsername`
Specifies the list of attributes to use as the preferred username when provisioning a user for this identity. The first non-empty attribute is used.

`spec.identityProviders.ldap.bindDN`
Specifies the optional DN to use to bind during the search phase. Must be set if `bindPassword` is defined.

`spec.identityProviders.ldap.bindPassword`
Specifies an optional reference to an OpenShift Container Platform `Secret` object containing the bind password. Must be set if `bindDN` is defined.

`spec.identityProviders.ldap.ca`
Specifies an optional reference to an OpenShift Container Platform `ConfigMap` object containing the Privacy-Enhanced Mail (PEM)-encoded certificate authority bundle to use in validating server certificates for the configured URL. Only used when `insecure` is `false`.

`spec.identityProviders.ldap.insecure`
Specifies whether a TLS connection is made to the server. When `true`, no TLS connection is made to the server. When `false`, `ldaps://` URLs connect using TLS, and `ldap://` URLs are upgraded to TLS. This must be set to `false` when `ldaps://` URLs are in use, as these URLs always attempt to connect using TLS.

`spec.identityProviders.ldap.url`
Specifies an RFC 2255 URL for the LDAP host and search parameters to use.

> [!NOTE]
> To allowlist users for an LDAP integration, use the `lookup` mapping method. Before a login from LDAP is allowed, a cluster administrator must create an `Identity` object and a `User` object for each LDAP user.

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

2.  Log in to the cluster as a user from your identity provider, entering the password when prompted.

    ``` terminal
    $ oc login -u <username>
    ```

3.  Confirm that the user logged in successfully and that the username displays by running the following command:

    ``` terminal
    $ oc whoami
    ```

</div>
