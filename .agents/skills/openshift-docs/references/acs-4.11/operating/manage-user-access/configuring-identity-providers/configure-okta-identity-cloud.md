<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

You can use Okta as a single sign-on (SSO) provider for Red Hat Advanced Cluster Security for Kubernetes (RHACS).

<a id="create-an-okta-app_configure-okta-identity-cloud"></a>

# Creating an Okta app

Before you can use Okta as a SAML 2.0 identity provider for Red Hat Advanced Cluster Security for Kubernetes, you must create an Okta app.

> [!WARNING]
> Okta’s **Developer Console** does not support the creation of custom SAML 2.0 applications. If you are using the **Developer Console**, you must first switch to the **Admin Console** (**Classic UI**). To switch, click **Developer Console** in the top left of the page and select **Classic UI**.

<div>

<div class="title">

Prerequisites

</div>

- You must have an account with administrative privileges for the Okta portal.

</div>

<div>

<div class="title">

Procedure

</div>

1.  On the Okta portal, select **Applications** from the menu bar.

2.  Click **Add Application** and then select **Create New App**.

3.  In the **Create a New Application Integration** dialog box, leave **Web** as the platform and select **SAML 2.0** as the protocol that you want to sign in users.

4.  Click **Create**.

5.  On the **General Settings** page, enter a name for the app in the **App name** field.

6.  Click **Next**.

7.  On the **SAML Settings** page, set values for the following fields:

    1.  **Single sign on URL**

        - Specify it as `https://<RHACS_portal_hostname>/sso/providers/saml/acs`.

        - Leave the **Use this for Recipient URL and Destination URL** option checked.

        - If your RHACS portal is accessible at different URLs, you can add them here by checking the **Allow this app to request other SSO URLs** option and add the alternative URLs using the specified format.

    2.  **Audience URI (SP Entity ID)**

        - Set the value to **RHACS** or another value of your choice.

        - Remember the value you choose; you will need this value when you configure Red Hat Advanced Cluster Security for Kubernetes.

    3.  **Attribute Statements**

        - You must add at least one attribute statement.

        - Red Hat recommends using the email attribute:

          - **Name:** email

          - **Format:** Unspecified

          - **Value:** user.email

8.  Verify that you have configured at least one **Attribute Statement** before continuing.

9.  Click **Next**.

10. On the **Feedback** page, select an option that applies to you.

11. Select an appropriate **App type**.

12. Click **Finish**.

</div>

After the configuration is complete, you are redirected to the **Sign On** settings page for the new app. A yellow box contains links to the information that you need to configure Red Hat Advanced Cluster Security for Kubernetes.

After you have created the app, assign Okta users to this application. Go to the **Assignments** tab, and assign the set of individual users or groups that can access Red Hat Advanced Cluster Security for Kubernetes. For example, assign the group **Everyone** to allow all users in the organization to access Red Hat Advanced Cluster Security for Kubernetes.

<a id="configure-saml-identity-provider_configure-okta-identity-cloud"></a>

# Configuring a SAML 2.0 identity provider

Use the instructions in this section to integrate a Security Assertion Markup Language (SAML) 2.0 identity provider with Red Hat Advanced Cluster Security for Kubernetes (RHACS).

<div>

<div class="title">

Prerequisites

</div>

- You must have permissions to configure identity providers in RHACS.

- For Okta identity providers, you must have an Okta app configured for RHACS.

</div>

<div>

<div class="title">

Procedure

</div>

1.  In the RHACS portal, go to **Platform Configuration** → **Access Control**.

2.  Click **Create auth provider** and select **SAML 2.0** from the drop-down list.

3.  In the **Name** field, enter a name to identify this authentication provider; for example, **Okta** or **Google**. The integration name is shown on the login page to help users select the correct sign-in option.

4.  In the **ServiceProvider issuer** field, enter the value that you are using as the `Audience URI` or `SP Entity ID` in Okta, or a similar value in other providers.

5.  Select the type of **Configuration**:

    - **Option 1: Dynamic Configuration**: If you select this option, enter the **IdP Metadata URL**, or the URL of **Identity Provider metadata** available from your identity provider console. The configuration values are acquired from the URL.

    - **Option 2: Static Configuration**: Copy the required static fields from the **View Setup Instructions** link in the Okta console, or a similar location for other providers:

      - **IdP Issuer**

      - **IdP SSO URL**

      - **Name/ID Format**

      - **IdP Certificate(s) (PEM)**

6.  Assign a **Minimum access role** for users who access RHACS using SAML.

    > [!TIP]
    > Set the **Minimum access role** to **Admin** while you complete setup. Later, you can return to the **Access Control** page to set up more tailored access rules based on user metadata from your identity provider.

7.  Click **Save**.

</div>

> [!IMPORTANT]
> If your SAML identity provider’s authentication response meets the following criteria:
>
> - Includes a `NotValidAfter` assertion: The user session remains valid until the time specified in the `NotValidAfter` field has elapsed. After the user session expires, users must reauthenticate.
>
> - Does not include a `NotValidAfter` assertion: The user session remains valid for 30 days, and then users must reauthenticate.

<div>

<div class="title">

Verification

</div>

1.  In the RHACS portal, go to **Platform Configuration** → **Access Control**.

2.  Select the **Auth Providers** tab.

3.  Click the authentication provider for which you want to verify the configuration.

4.  Select **Test login** from the **Auth Provider** section header. The **Test login** page opens in a new browser tab.

5.  Sign in with your credentials.

    - If you logged in successfully, RHACS shows the `User ID` and `User Attributes` that the identity provider sent for the credentials that you used to log in to the system.

    - If your login attempt failed, RHACS shows a message describing why the identity provider’s response could not be processed.

6.  Close the **Test login** browser tab.

    > [!NOTE]
    > Even if the response indicates successful authentication, you might need to create additional access rules based on the user metadata from your identity provider.

</div>
