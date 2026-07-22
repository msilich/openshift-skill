<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Configure the `ldap` identity provider to validate user names and passwords against an LDAPv3 server, using simple bind authentication.

# About identity providers in OpenShift Container Platform

You can configure identity providers by creating a custom resource (CR) that describes the provider and adding it to the cluster. Identity providers enable user authentication in OpenShift Container Platform beyond the default `kubeadmin` user.

> [!NOTE]
> OpenShift Container Platform user names containing `/`, `:`, and `%` are not supported.

# About LDAP authentication

During authentication, the LDAP directory is searched for an entry that matches the provided user name. If a single unique match is found, a simple bind is attempted using the distinguished name (DN) of the entry plus the provided password.

These are the steps taken:

1.  Generate a search filter by combining the attribute and filter in the configured `url` with the user-provided user name.

2.  Search the directory using the generated filter. If the search does not return exactly one entry, deny access.

3.  Attempt to bind to the LDAP server using the DN of the entry retrieved from the search, and the user-provided password.

4.  If the bind is unsuccessful, deny access.

5.  If the bind is successful, build an identity using the configured attributes as the identity, email address, display name, and preferred user name.

The configured `url` is an RFC 2255 URL, which specifies the LDAP host and search parameters to use. The syntax of the URL is:

    ldap://host:port/basedn?attribute?scope?filter

For this URL:

| URL component | Description |
|----|----|
| `ldap` | For regular LDAP, use the string `ldap`. For secure LDAP (LDAPS), use `ldaps` instead. |
| `host:port` | The name and port of the LDAP server. Defaults to `localhost:389` for ldap and `localhost:636` for LDAPS. |
| `basedn` | The DN of the branch of the directory where all searches should start from. At the very least, this must be the top of your directory tree, but it could also specify a subtree in the directory. |
| `attribute` | The attribute to search for. Although RFC 2255 allows a comma-separated list of attributes, only the first attribute will be used, no matter how many are provided. If no attributes are provided, the default is to use `uid`. It is recommended to choose an attribute that will be unique across all entries in the subtree you will be using. |
| `scope` | The scope of the search. Can be either `one` or `sub`. If the scope is not provided, the default is to use a scope of `sub`. |
| `filter` | A valid LDAP search filter. If not provided, defaults to `(objectClass=*)` |

When doing searches, the attribute, filter, and provided user name are combined to create a search filter that looks like:

    (&(<filter>)(<attribute>=<username>))

For example, consider a URL of:

    ldap://ldap.example.com/o=Acme?cn?sub?(enabled=true)

When a client attempts to connect using a user name of `bob`, the resulting search filter will be `(&(enabled=true)(cn=bob))`.

If the LDAP directory requires authentication to search, specify a `bindDN` and `bindPassword` to use to perform the entry search.

# Creating the LDAP secret

To use the identity provider, you must define an OpenShift Container Platform `Secret` object that contains the `bindPassword` field.

<div>

<div class="title">

Procedure

</div>

- Create a `Secret` object that contains the `bindPassword` field:

  ``` terminal
  $ oc create secret generic ldap-secret --from-literal=bindPassword=<secret> -n openshift-config
  ```

  - The secret key containing the bindPassword for the `--from-literal` argument must be called `bindPassword`.

    > [!TIP]
    > You can alternatively apply the following YAML to create the secret:
    >
    > ``` yaml
    > apiVersion: v1
    > kind: Secret
    > metadata:
    >   name: ldap-secret
    >   namespace: openshift-config
    > type: Opaque
    > data:
    >   bindPassword: <base64_encoded_bind_password>
    > ```

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

# Sample LDAP CR

The following custom resource (CR) shows the parameters and acceptable values for an LDAP identity provider.

<div class="formalpara">

<div class="title">

LDAP CR

</div>

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

</div>

- This provider name is prefixed to the returned user ID to form an identity name.

- Controls how mappings are established between this provider’s identities and `User` objects.

- List of attributes to use as the identity. First non-empty attribute is used. At least one attribute is required. If none of the listed attribute have a value, authentication fails. Defined attributes are retrieved as raw, allowing for binary values to be used.

- List of attributes to use as the email address. First non-empty attribute is used.

- List of attributes to use as the display name. First non-empty attribute is used.

- List of attributes to use as the preferred user name when provisioning a user for this identity. First non-empty attribute is used.

- Optional DN to use to bind during the search phase. Must be set if `bindPassword` is defined.

- Optional reference to an OpenShift Container Platform `Secret` object containing the bind password. Must be set if `bindDN` is defined.

- Optional: Reference to an OpenShift Container Platform `ConfigMap` object containing the PEM-encoded certificate authority bundle to use in validating server certificates for the configured URL. Only used when `insecure` is `false`.

- When `true`, no TLS connection is made to the server. When `false`, `ldaps://` URLs connect using TLS, and `ldap://` URLs are upgraded to TLS. This must be set to `false` when `ldaps://` URLs are in use, as these URLs always attempt to connect using TLS.

- An RFC 2255 URL which specifies the LDAP host and search parameters to use.

> [!NOTE]
> To whitelist users for an LDAP integration, use the `lookup` mapping method. Before a login from LDAP would be allowed, a cluster administrator must create an `Identity` object and a `User` object for each LDAP user.

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

2.  Log in to the cluster as a user from your identity provider, entering the password when prompted.

    ``` terminal
    $ oc login -u <username>
    ```

3.  Confirm that the user logged in successfully, and display the user name.

    ``` terminal
    $ oc whoami
    ```

</div>
