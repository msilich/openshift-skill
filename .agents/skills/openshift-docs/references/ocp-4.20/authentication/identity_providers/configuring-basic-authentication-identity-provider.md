<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Configure the `basic-authentication` identity provider. Users can log in to OpenShift Container Platform with credentials validated against a remote authentication service, without maintaining a separate user store in the cluster.

# Identity providers in OpenShift Container Platform

You can configure identity providers by creating a custom resource (CR) that describes the provider and adding it to the cluster. Identity providers enable user authentication in OpenShift Container Platform beyond the default `kubeadmin` user.

> [!NOTE]
> OpenShift Container Platform usernames containing `/`, `:`, and `%` are not supported.

# About basic authentication

Configure basic authentication to validate user credentials against a remote service over HTTP. Use this integration when you need a flexible back-end for username and password login in OpenShift Container Platform.

Basic authentication is a generic back-end integration mechanism that allows users to log in to OpenShift Container Platform with credentials validated against a remote identity provider.

Because basic authentication is generic, you can use this identity provider for advanced authentication configurations.

> [!IMPORTANT]
> Basic authentication must use an HTTPS connection to the remote server to prevent potential snooping of the user ID and password and man-in-the-middle attacks.

With basic authentication configured, users send their username and password to OpenShift Container Platform during login. OpenShift Container Platform validates those credentials against a remote server. OpenShift Container Platform makes a server-to-server request, passing the credentials as a basic authentication header.

> [!NOTE]
> This only works for username and password login mechanisms, and OpenShift Container Platform must be able to make network requests to the remote authentication server.

Usernames and passwords are validated against a remote URL that is protected by basic authentication and returns JSON.

A `401` response indicates failed authentication.

A non-`200` status, or the presence of a non-empty "error" key, indicates an error:

``` terminal
{"error":"Error message"}
```

A `200` status with a `sub` (subject) key indicates success:

``` terminal
{"sub":"userid"}
```

where:

`userid`
Specifies a value that is unique to the authenticated user and must not be modified.

A successful response can optionally provide additional data, such as:

- A display name using the `name` key. For example:

  ``` terminal
  {"sub":"userid", "name": "User Name", ...}
  ```

- An email address using the `email` key. For example:

  ``` terminal
  {"sub":"userid", "email":"user@example.com", ...}
  ```

- A preferred username using the `preferred_username` key. This is useful when the unique, unchangeable subject is a database key or UID, and a more human-readable name exists. This is used as a hint when provisioning the OpenShift Container Platform user for the authenticated identity. For example:

  ``` terminal
  {"sub":"014fbff9a07c", "preferred_username":"bob", ...}
  ```

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

# Sample basic authentication custom resource

You can configure basic authentication for your cluster by applying an `OAuth` custom resource (CR) with a `BasicAuth` identity provider. Use this sample to review provider parameters and acceptable values before you connect to your remote authentication server.

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

where:

`spec.identityProviders.name`
Specifies that the provider name is prefixed to the returned user ID to form an identity name.

`spec.identityProviders.mappingMethod`
Specifies how mappings are established between the identities of this provider and `User` objects.

`spec.identityProviders.basicAuth.url`
Specifies the URL that accepts credentials in Basic authentication headers.

`spec.identityProviders.basicAuth.ca`
Optional: Specifies a reference to an OpenShift Container Platform `ConfigMap` object containing the Privacy-Enhanced Mail (PEM)-encoded certificate authority bundle to use in validating server certificates for the configured URL.

`spec.identityProviders.basicAuth.tlsClientCert`
Optional: Specifies a reference to an OpenShift Container Platform `Secret` object containing the client certificate to present when making requests to the configured URL.

`spec.identityProviders.basicAuth.tlsClientKey`
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

# Example Apache HTTPD configuration for basic identity providers

You can use CGI scripting in Apache HTTPD to configure a remote authentication server that returns JSON responses for basic identity providers in OpenShift Container Platform.

The following is an example of an Apache `VirtualHost` configuration file.

``` conf
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
```

The following is an example of a `login.cgi` CGI script file.

``` bash
#!/bin/bash
echo "Content-Type: application/json"
echo ""
echo '{"sub":"userid", "name":"'$REMOTE_USER'"}'
exit 0
```

The following is an example of a `fail.cgi` CGI script file.

``` bash
#!/bin/bash
echo "Content-Type: application/json"
echo ""
echo '{"error": "Login failure"}'
exit 0
```

## File requirements

These are the requirements for the files you create on an Apache HTTPD web server:

- The `login.cgi` and `fail.cgi` CGI script files must be executable. Use the `chmod +x` command on both files.

- If SELinux is enabled, the `login.cgi` and `fail.cgi` CGI script files must have proper SELinux security contexts. Run the `restorecon -RFv /var/www/cgi-bin` command, or ensure that the context is the `httpd_sys_script_exec_t` SELinux type by using the `ls -laZ` command.

- The `login.cgi` CGI script file runs only when the user successfully logs in according to the `Require` and `Auth` Apache configuration directives.

- The `fail.cgi` CGI script file runs when the user fails to log in and returns an `HTTP 401` HTTP status code.

# Troubleshooting basic authentication

Troubleshoot basic authentication by testing backend connectivity and verifying JSON login responses when users cannot authenticate in OpenShift Container Platform.

The most common issue relates to network connectivity to the backend server. To debug connectivity, run `curl` commands on a control plane node.

<div>

<div class="title">

Procedure

</div>

1.  To test successful and unsuccessful logins, replace the `<user>` and `<password>` in the following example command with valid or invalid credentials:

    ``` terminal
    $ curl --cacert /path/to/ca.crt --cert /path/to/client.crt --key /path/to/client.key -u <user>:<password> -v https://www.example.com/remote-idp
    ```

2.  Review successful login responses.

    A `200` status with a `sub` (subject) key indicates success:

    ``` terminal
    {"sub":"userid"}
    ```

    The subject must be unique to the authenticated user and must not be modified.

    A successful response can optionally provide additional data, such as:

    - A display name using the `name` key:

      ``` terminal
      {"sub":"userid", "name": "User Name", ...}
      ```

    - An email address using the `email` key:

      ``` terminal
      {"sub":"userid", "email":"user@example.com", ...}
      ```

    - A preferred username using the `preferred_username` key:

      ``` terminal
      {"sub":"014fbff9a07c", "preferred_username":"bob", ...}
      ```

    The `preferred_username` key is useful when the unique, unchangeable subject is a database key or UID, and a more human-readable name exists. This is used as a hint when provisioning the OpenShift Container Platform user for the authenticated identity.

3.  Review failed login responses.

    - A `401` response indicates failed authentication.

    - A non-`200` status or the presence of a non-empty "error" key indicates an error: `{"error":"Error message"}`

</div>
