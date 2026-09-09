<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

You can use [Google Workspace](https://workspace.google.com/) as a single sign-on (SSO) provider for Red Hat Advanced Cluster Security for Kubernetes.

<a id="set-up-oauth-20-credentials-for-your-gcp-project_configure-google-workspace-identity"></a>

# Setting up OAuth 2.0 credentials for your GCP project

To configure Google Workspace as an identity provider for Red Hat Advanced Cluster Security for Kubernetes, you must first configure OAuth 2.0 credentials for your GCP project.

<div>

<div class="title">

Prerequisites

</div>

- You must have administrator-level access to your organization’s Google Workspace account to create a new project, or permissions to create and configure OAuth 2.0 credentials for an existing project. Red Hat recommends that you create a new project for managing access to Red Hat Advanced Cluster Security for Kubernetes.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create a new Google Cloud project, see the Google documentation topic [creating and managing projects](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

2.  After you have created the project, open the [**Credentials**](https://console.developers.google.com/apis/credentials) page in the Google API Console.

3.  Verify the project name listed in the upper left corner near the logo to make sure that you are using the correct project.

4.  To create new credentials, go to **Create Credentials** → **OAuth client ID**.

5.  Choose **Web application** as the **Application type**.

6.  In the **Name** box, enter a name for the application, for example, **RHACS**.

7.  In the **Authorized redirect URIs** box, enter `https://<stackrox_hostname>:<port_number>/sso/providers/oidc/callback`.

    - replace `<stackrox_hostname>` with the hostname on which you expose your Central instance.

    - replace `<port_number>` with the port number on which you expose Central. If you are using the standard HTTPS port `443`, you can omit the port number.

8.  Click **Create**. This creates an application and credentials and redirects you back to the credentials page.

9.  An information box opens, showing details about the newly created application. Close the information box.

10. Copy and save the **Client ID** that ends with `.apps.googleusercontent.com`. You can check this client ID by using the Google API Console.

11. Select **OAuth consent screen** from the navigation menu on the left.

    > [!NOTE]
    > The OAuth consent screen configuration is valid for the entire GCP project, and not only to the application you created in the previous steps. If you already have an OAuth consent screen configured in this project and want to apply different settings for Red Hat Advanced Cluster Security for Kubernetes login, create a new GCP project.

12. On the OAuth consent screen page:

    1.  Choose the **Application type** as **Internal**. If you select **Public**, anyone with a Google account can sign in.

    2.  Enter a descriptive **Application name**. This name is shown to users on the consent screen when they sign in. For example, use **RHACS** or **\<organization_name\> SSO for Red Hat Advanced Cluster Security for Kubernetes**.

    3.  Verify that the **Scopes for Google APIs** only lists **email**, **profile**, and **openid** scopes. Only these scopes are required for single sign-on. If you grant additional scopes it increases the risk of exposing sensitive data.

</div>

<a id="specify-a-client-secret_configure-google-workspace-identity"></a>

# Specifying a client secret

Red Hat Advanced Cluster Security for Kubernetes version 3.0.39 and newer supports the [OAuth 2.0 Authorization Code Grant](https://oauth.net/2/grant-types/authorization-code/) authentication flow when you specify a client secret. When you use this authentication flow, Red Hat Advanced Cluster Security for Kubernetes uses a refresh token to keep users logged in beyond the token expiration time configured in your OIDC identity provider.

When users log out, Red Hat Advanced Cluster Security for Kubernetes deletes the refresh token from the client-side. Additionally, if your identity provider API supports refresh token revocation, Red Hat Advanced Cluster Security for Kubernetes also sends a request to your identity provider to revoke the refresh token.

You can specify a client secret when you configure Red Hat Advanced Cluster Security for Kubernetes to integrate with an OIDC identity provider.

<div class="note">

<div class="title">

</div>

- You cannot use a **Client Secret** with the *Fragment* **Callback mode**.

- You cannot edit configurations for existing authentication providers.

- You must create a new OIDC integration in Red Hat Advanced Cluster Security for Kubernetes if you want to use a **Client Secret**.

</div>

Red Hat recommends using a client secret when connecting Red Hat Advanced Cluster Security for Kubernetes with an OIDC identity provider. If you do not want to use a **Client Secret**, you must select the **Do not use Client Secret (not recommended)** option.

<a id="configure-oidc-identity-provider_configure-google-workspace-identity"></a>

# Configuring an OIDC identity provider

You can configure Red Hat Advanced Cluster Security for Kubernetes (RHACS) to use your OpenID Connect (OIDC) identity provider.

<div>

<div class="title">

Prerequisites

</div>

- You must have already configured an application in your identity provider, such as Google Workspace.

- You must have permissions to configure identity providers in RHACS.

</div>

<div>

<div class="title">

Procedure

</div>

1.  In the RHACS portal, go to **Platform Configuration** → **Access Control**.

2.  Click **Create auth provider** and select **OpenID Connect** from the drop-down list.

3.  Enter information in the following fields:

    - **Name**: A name to identify your authentication provider; for example, **Google Workspace**. The integration name is shown on the login page to help users select the correct sign-in option.

    - **Callback mode**: Select **Auto-select (recommended)**, which is the default value, unless the identity provider requires another mode.

      > [!NOTE]
      > `Fragment` mode is designed around the limitations of Single Page Applications (SPAs). Red Hat only supports the `Fragment` mode for early integrations and does not recommended using it for later integrations.

    - **Issuer**: The root URL of your identity provider; for example, `https://accounts.google.com` for Google Workspace. See your identity provider documentation for more information.

      > [!NOTE]
      > If you are using RHACS version 3.0.49 and later, for **Issuer** you can perform these actions:
      >
      > - Prefix your root URL with `https+insecure://` to skip TLS validation. This configuration is insecure and Red Hat does not recommended it. Only use it for testing purposes.
      >
      > - Specify query strings; for example, `?key1=value1&key2=value2` along with the root URL. RHACS appends the value of **Issuer** as you entered it to the authorization endpoint. You can use it to customize your provider’s login screen. For example, you can optimize the Google Workspace login screen to a specific hosted domain by using the [`hd` parameter](https://developers.google.com/identity/protocols/oauth2/openid-connect#hd-param), or preselect an authentication method in `PingFederate` by using the [`pfidpadapterid` parameter](https://docs.pingidentity.com/bundle/pingfederate-93/page/nfr1564003024683.html).

    - **Client ID**: The OIDC Client ID for your configured project.

    - **Client Secret**: Enter the client secret provided by your identity provider (IdP). If you are not using a client secret, which is not recommended, select **Do not use Client Secret**.

4.  Assign a **Minimum access role** for users who access RHACS using the selected identity provider.

    > [!TIP]
    > Set the **Minimum access role** to **Admin** while you complete setup. Later, you can return to the **Access Control** page to set up more tailored access rules based on user metadata from your identity provider.

5.  To add access rules for users and groups accessing RHACS, click **Add new rule** in the **Rules** section. For example, to give the **Admin** role to a user called `administrator`, you can use the following key-value pairs to create access rules:

    |         |               |
    |---------|---------------|
    | **Key** | **Value**     |
    | Name    | administrator |
    | Role    | Admin         |

6.  Click **Save**.

</div>

<div>

<div class="title">

Verification

</div>

1.  In the RHACS portal, go to **Platform Configuration** → **Access Control**.

2.  Select the **Auth providers** tab.

3.  Select the authentication provider for which you want to verify the configuration.

4.  Select **Test login** from the **Auth Provider** section header. The **Test login** page opens in a new browser tab.

5.  Log in with your credentials.

    - If you logged in successfully, RHACS shows the `User ID` and `User Attributes` that the identity provider sent for the credentials that you used to log in to the system.

    - If your login attempt failed, RHACS shows a message describing why the identity provider’s response could not be processed.

6.  Close the **Test Login** browser tab.

</div>
