<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

If you use an enterprise certificate authority (CA) for authentication, you can configure Red Hat Advanced Cluster Security for Kubernetes (RHACS) to authenticate users by using their personal certificates.

After you configure PKI authentication, users and API clients can log in using their personal certificates. Users without certificates can still use other authentication options, including API tokens, the local administrator password, or other authentication providers. PKI authentication is available on the same port number as the Web UI, gRPC, and REST APIs.

When you configure PKI authentication, by default, Red Hat Advanced Cluster Security for Kubernetes uses the same port for PKI, web UI, gRPC, other single sign-on (SSO) providers, and REST APIs. You can also configure a separate port for PKI authentication by using a YAML configuration file to configure and expose endpoints.

<a id="configure-pki-authentication-portal_enable-pki-authentication"></a>

# Configuring PKI authentication by using the RHACS portal

You can configure Public Key Infrastructure (PKI) authentication by using the RHACS portal.

<div>

<div class="title">

Procedure

</div>

1.  In the RHACS portal, go to **Platform Configuration** → **Access Control**.

2.  Click **Create Auth Provider** and select **User Certificates** from the drop-down list.

3.  In the **Name** field, specify a name for this authentication provider.

4.  In the **CA certificate(s) (PEM)** field, paste your root CA certificate in PEM format.

5.  Assign a **Minimum access role** for users who access RHACS using PKI authentication. A user must have the permissions granted to this role or a role with higher permissions to log in to RHACS.

    > [!TIP]
    > For security, Red Hat recommends first setting the **Minimum access role** to **None** while you complete setup. Later, you can return to the **Access Control** page to set up more tailored access rules based on user metadata from your identity provider.

6.  To add access rules for users and groups accessing RHACS, click **Add new rule** in the **Rules** section. For example, to give the **Admin** role to a user called `administrator`, you can use the following key-value pairs to create access rules:

    |         |               |
    |---------|---------------|
    | **Key** | **Value**     |
    | Name    | administrator |
    | Role    | Admin         |

7.  Click **Save**.

</div>

<a id="configure-pki-authentication-roxctl_enable-pki-authentication"></a>

# Configuring PKI authentication by using the `roxctl` CLI

You can configure PKI authentication by using the `roxctl` CLI.

<div>

<div class="title">

Procedure

</div>

- Run the following command:

  ``` terminal
  $ roxctl -e <hostname>:<port_number> central userpki create -c <ca_certificate_file> -r <default_role_name> <provider_name>
  ```

</div>

<a id="update-authentication-keys-and-certificates_enable-pki-authentication"></a>

# Updating authentication keys and certificates

You can update your authentication keys and certificates by using the RHACS portal.

<div>

<div class="title">

Procedure

</div>

1.  Create a new authentication provider.

2.  Copy the role mappings from your old authentication provider to the new authentication provider.

3.  Rename or delete the old authentication provider with the old root CA key.

</div>

<a id="log-in-using-client-certificate_enable-pki-authentication"></a>

# Logging in by using a client certificate

After you configure PKI authentication, users see a certificate prompt in the RHACS portal login page. The prompt only shows up if a client certificate trusted by the configured root CA is installed on the user’s system.

Use the procedure described in this section to log in by using a client certificate.

<div>

<div class="title">

Procedure

</div>

1.  Open the RHACS portal.

2.  Select a certificate in the browser prompt.

3.  On the login page, select the authentication provider name option to log in with a certificate. If you do not want to log in by using the certificate, you can also log in by using the administrator password or another login method.

</div>

> [!NOTE]
> Once you use a client certificate to log into the RHACS portal, you cannot log in with a different certificate unless you restart your browser.
