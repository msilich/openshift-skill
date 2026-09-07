<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Configure a Keystone identity provider to connect OpenShift Container Platform to an OpenStack Keystone v3 server so that users can sign in with Keystone credentials.

# Identity providers in OpenShift Container Platform

You can configure identity providers by creating a custom resource (CR) that describes the provider and adding it to the cluster. Identity providers enable user authentication in OpenShift Container Platform beyond the default `kubeadmin` user.

> [!NOTE]
> OpenShift Container Platform usernames containing `/`, `:`, and `%` are not supported.

# About Keystone authentication

Configure Keystone authentication in OpenShift Container Platform to share sign-in with your OpenStack Keystone server. Mapping users by Keystone ID reduces access risk when usernames are reused.

Map OpenShift Container Platform users to Keystone usernames or unique Keystone IDs. Users log in with their Keystone username and password.

Basing users on the Keystone ID is gives each user a unique identity. If you delete a Keystone user, then create a new user with the same username but a different Keystone ID, the new user does not have access to resources of the deleted user.

# Creating the secret

You can create a TLS `Secret` object in the `openshift-config` namespace by using the `oc` CLI or by applying a YAML file to store client certificates and keys that identity providers require for secure communication.

<div>

<div class="title">

Procedure

</div>

1.  Create a `Secret` object that contains the key and certificate by running the following command:

    ``` terminal
    $ oc create secret tls <secret_name> --key=key.pem --cert=cert.pem -n openshift-config
    ```

2.  Optional: Apply the following YAML to create the secret:

    ``` yaml
    apiVersion: v1
    kind: Secret
    metadata:
      name: <secret_name>
      namespace: openshift-config
    type: kubernetes.io/tls
    data:
      tls.crt: <base64_encoded_cert>
      tls.key: <base64_encoded_key>
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

# Sample Keystone custom resource

You can configure a Keystone identity provider for your cluster by applying an `OAuth` custom resource (CR) with a `Keystone` identity provider. Review domain name, server URL, certificate authority, and TLS client certificate parameters in this sample before you connect to your Keystone server.

``` yaml
apiVersion: config.openshift.io/v1
kind: OAuth
metadata:
  name: cluster
spec:
  identityProviders:
  - name: keystoneidp
    mappingMethod: claim
    type: Keystone
    keystone:
      domainName: default
      url: https://keystone.example.com:5000
      ca:
        name: ca-config-map
      tlsClientCert:
        name: client-cert-secret
      tlsClientKey:
        name: client-key-secret
```

where:

`spec.identityProviders.name`
Specifies the provider name, which is prefixed to provider usernames to form an identity name.

`spec.identityProviders.mappingMethod`
Specifies how mappings are established between identities from this provider and `User` objects.

`spec.identityProviders.keystone.domainName`
Specifies the Keystone domain name. In Keystone, usernames are domain-specific. Only a single domain is supported.

`spec.identityProviders.keystone.url`
Specifies the URL to use to connect to the Keystone server (required). This must use `https`.

`spec.identityProviders.keystone.ca`
Specifies an optional reference to an OpenShift Container Platform `ConfigMap` object containing the PEM-encoded certificate authority bundle to use in validating server certificates for the configured URL.

`spec.identityProviders.keystone.tlsClientCert`
Specifies an optional reference to an OpenShift Container Platform `Secret` object containing the client certificate to present when making requests to the configured URL.

`spec.identityProviders.keystone.tlsClientKey`
Specifies a reference to an OpenShift Container Platform `Secret` object containing the key for the client certificate. Required if `tlsClientCert` is specified.

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

# Additional resources

- [Keystone](http://docs.openstack.org/developer/keystone/)
