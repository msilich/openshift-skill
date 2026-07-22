<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Configure the `basic-authentication` identity provider for users to log in to OpenShift Container Platform with credentials validated against a remote identity provider. Basic authentication is a generic back-end integration mechanism.

# About identity providers in OpenShift Container Platform

You can configure identity providers by creating a custom resource (CR) that describes the provider and adding it to the cluster. Identity providers enable user authentication in OpenShift Container Platform beyond the default `kubeadmin` user.

> [!NOTE]
> OpenShift Container Platform user names containing `/`, `:`, and `%` are not supported.

# About basic authentication

Basic authentication is a generic back-end integration mechanism that allows users to log in to OpenShift Container Platform with credentials validated against a remote identity provider.

Because basic authentication is generic, you can use this identity provider for advanced authentication configurations.

> [!IMPORTANT]
> Basic authentication must use an HTTPS connection to the remote server to prevent potential snooping of the user ID and password and man-in-the-middle attacks.

With basic authentication configured, users send their user name and password to OpenShift Container Platform, which then validates those credentials against a remote server by making a server-to-server request, passing the credentials as a basic authentication header. This requires users to send their credentials to OpenShift Container Platform during login.

> [!NOTE]
> This only works for user name/password login mechanisms, and OpenShift Container Platform must be able to make network requests to the remote authentication server.

User names and passwords are validated against a remote URL that is protected by basic authentication and returns JSON.

A `401` response indicates failed authentication.

A non-`200` status, or the presence of a non-empty "error" key, indicates an error:

``` terminal
{"error":"Error message"}
```

A `200` status with a `sub` (subject) key indicates success:

``` terminal
{"sub":"userid"}
```

- The subject must be unique to the authenticated user and must not be able to be modified.

A successful response can optionally provide additional data, such as:

- A display name using the `name` key. For example:

  ``` terminal
  {"sub":"userid", "name": "User Name", ...}
  ```

- An email address using the `email` key. For example:

  ``` terminal
  {"sub":"userid", "email":"user@example.com", ...}
  ```

- A preferred user name using the `preferred_username` key. This is useful when the unique, unchangeable subject is a database key or UID, and a more human-readable name exists. This is used as a hint when provisioning the OpenShift Container Platform user for the authenticated identity. For example:

  ``` terminal
  {"sub":"014fbff9a07c", "preferred_username":"bob", ...}
  ```

# Creating the secret

Identity providers use OpenShift Container Platform `Secret` objects in the `openshift-config` namespace to contain the client secret, client certificates, and keys.

<div>

<div class="title">

Procedure

</div>

- Create a `Secret` object that contains the key and certificate by using the following command:

  ``` terminal
  $ oc create secret tls <secret_name> --key=key.pem --cert=cert.pem -n openshift-config
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
  > type: kubernetes.io/tls
  > data:
  >   tls.crt: <base64_encoded_cert>
  >   tls.key: <base64_encoded_key>
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

# Sample basic authentication CR

The following custom resource (CR) shows the parameters and acceptable values for a basic authentication identity provider.

<div class="formalpara">

<div class="title">

Basic authentication CR

</div>

``` yaml
apiVersion: config.openshift.io/v1
kind: OAuth
metadata:
  name: cluster
spec:
  identityProviders:
  - name: basicidp
    mappingMethod: claim
    type: BasicAuth
    basicAuth:
      url: https://www.example.com/remote-idp
      ca:
        name: ca-config-map
      tlsClientCert:
        name: client-cert-secret
      tlsClientKey:
        name: client-key-secret
```

</div>

- This provider name is prefixed to the returned user ID to form an identity name.

- Controls how mappings are established between this provider’s identities and `User` objects.

- URL accepting credentials in Basic authentication headers.

- Optional: Reference to an OpenShift Container Platform `ConfigMap` object containing the PEM-encoded certificate authority bundle to use in validating server certificates for the configured URL.

- Optional: Reference to an OpenShift Container Platform `Secret` object containing the client certificate to present when making requests to the configured URL.

- Reference to an OpenShift Container Platform `Secret` object containing the key for the client certificate. Required if `tlsClientCert` is specified.

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

# Example Apache HTTPD configuration for basic identity providers

The basic identify provider (IDP) configuration in OpenShift Container Platform 4 requires that the IDP server respond with JSON for success and failures. You can use CGI scripting in Apache HTTPD to accomplish this. This section provides examples.

<div class="formalpara">

<div class="title">

Example `/etc/httpd/conf.d/login.conf`

</div>

    <VirtualHost *:443>
      # CGI Scripts in here
      DocumentRoot /var/www/cgi-bin

      # SSL Directives
      SSLEngine on
      SSLCipherSuite PROFILE=SYSTEM
      SSLProxyCipherSuite PROFILE=SYSTEM
      SSLCertificateFile /etc/pki/tls/certs/localhost.crt
      SSLCertificateKeyFile /etc/pki/tls/private/localhost.key

      # Configure HTTPD to execute scripts
      ScriptAlias /basic /var/www/cgi-bin

      # Handles a failed login attempt
      ErrorDocument 401 /basic/fail.cgi

      # Handles authentication
      <Location /basic/login.cgi>
        AuthType Basic
        AuthName "Please Log In"
        AuthBasicProvider file
        AuthUserFile /etc/httpd/conf/passwords
        Require valid-user
      </Location>
    </VirtualHost>

</div>

<div class="formalpara">

<div class="title">

Example `/var/www/cgi-bin/login.cgi`

</div>

    #!/bin/bash
    echo "Content-Type: application/json"
    echo ""
    echo '{"sub":"userid", "name":"'$REMOTE_USER'"}'
    exit 0

</div>

<div class="formalpara">

<div class="title">

Example `/var/www/cgi-bin/fail.cgi`

</div>

    #!/bin/bash
    echo "Content-Type: application/json"
    echo ""
    echo '{"error": "Login failure"}'
    exit 0

</div>

## File requirements

These are the requirements for the files you create on an Apache HTTPD web server:

- `login.cgi` and `fail.cgi` must be executable (`chmod +x`).

- `login.cgi` and `fail.cgi` must have proper SELinux contexts if SELinux is enabled: `restorecon -RFv /var/www/cgi-bin`, or ensure that the context is `httpd_sys_script_exec_t` using `ls -laZ`.

- `login.cgi` is only executed if your user successfully logs in per `Require and Auth` directives.

- `fail.cgi` is executed if the user fails to log in, resulting in an `HTTP 401` response.

# Basic authentication troubleshooting

The most common issue relates to network connectivity to the backend server. For simple debugging, run `curl` commands on the master. To test for a successful login, replace the `<user>` and `<password>` in the following example command with valid credentials. To test an invalid login, replace them with false credentials.

``` terminal
$ curl --cacert /path/to/ca.crt --cert /path/to/client.crt --key /path/to/client.key -u <user>:<password> -v https://www.example.com/remote-idp
```

**Successful responses**

A `200` status with a `sub` (subject) key indicates success:

``` terminal
{"sub":"userid"}
```

The subject must be unique to the authenticated user, and must not be able to be modified.

A successful response can optionally provide additional data, such as:

- A display name using the `name` key:

  ``` terminal
  {"sub":"userid", "name": "User Name", ...}
  ```

- An email address using the `email` key:

  ``` terminal
  {"sub":"userid", "email":"user@example.com", ...}
  ```

- A preferred user name using the `preferred_username` key:

  ``` terminal
  {"sub":"014fbff9a07c", "preferred_username":"bob", ...}
  ```

  The `preferred_username` key is useful when the unique, unchangeable subject is a database key or UID, and a more human-readable name exists. This is used as a hint when provisioning the OpenShift Container Platform user for the authenticated identity.

**Failed responses**

- A `401` response indicates failed authentication.

- A non-`200` status or the presence of a non-empty "error" key indicates an error: `{"error":"Error message"}`
