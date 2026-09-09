<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Red Hat Advanced Cluster Security for Kubernetes (RHACS) provides the ability to configure short-lived access to the user interface and API calls.

You can configure this by exchanging OpenID Connect (OIDC) identity tokens for a RHACS-issued token. This is sometimes called machine to machine authentication.

We recommend this especially for Continuous Integration (CI) usage, where short-lived access is preferable over long-lived API tokens.

The following steps outline the high-level workflow on how to configure short-lived access to the user interface and API calls:

1.  Configuring RHACS to trust OIDC identity token issuers for exchanging short-lived RHACS-issued tokens.

2.  Exchanging an OIDC identity token for a short-lived RHACS-issued token by calling the API.

<div class="note">

<div class="title">

</div>

- To prevent privilege escalation, when you create a new token, your role’s permissions limit the permission you can assign to that token. For example, if you only have `read` permission for the Integration resource, you cannot create a token with `write` permission.

- If you want a custom role to create tokens for other users to use, you must assign the required permissions to that custom role.

- Use short-lived tokens for machine-to-machine communication, such as CI/CD pipelines, scripts, and other automation. Also, use the `roxctl central login` command for human-to-machine communication, such as `roxctl` CLI or API access.

- The majority of cloud service providers support OIDC identity tokens, for example, Microsoft Entra ID, Google Cloud Identity Platform, and AWS Cognito. You can use OIDC identity tokens issued by these services for RHACS short-lived access.

- You can also use third-party OIDC identity tokens directly to access the API endpoint, without an exchange, if a machine-to-machine configuration exists for the token issuer.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Using Azure Entra ID service principals for machine to machine auth with RHACS](https://github.com/stackrox/contributions/blob/main/guides/cloud-provider-integrations/azure-service-principal-m2m-auth.md)

- [Using an authentication provider to authenticate with roxctl](../../cli/using-the-roxctl-cli.md#using-an-authentication-provider-to-authenticate-with-roxctl_using-roxctl-cli)

- [Configuring API tokens](../../configuration/configure-api-token.md)

</div>

<a id="configure-short-lived-access_configure-short-lived-access"></a>

# Configure short-lived access for an OIDC identity token issuer

Start configuring short-lived access for an OpenID Connect (OIDC) identity token issuer.

<div>

<div class="title">

Procedure

</div>

1.  In the RHACS portal, go to **Platform Configuration** → **Integrations**.

2.  Scroll to the **Authentication Tokens** category, and then click **Machine access configuration**.

3.  Click **Create configuration**.

4.  Select the **configuration type**, choosing one of the following:

    - **Generic** if you use an arbitrary OIDC identity token issuer.

    - **GitHub Actions** if you plan to access RHACS from GitHub Actions.

5.  Enter the OIDC identity token issuer.

6.  Enter the **token lifetime** for tokens issued by the configuration.

    > [!NOTE]
    > The format for the **token lifetime** is **XhYmZs** and you cannot set it for longer than 24 hours.

7.  Add rules to the configuration:

    - The **Key** is the OIDC token’s claim to use.

    - The **Value** is the expected OIDC token claim value.

    - The **Role** is the role to assign to the token if the OIDC token claim and value exist.

      > [!NOTE]
      > Rules are similar to Authentication Provider rules to assign roles based on claim values.
      >
      > As a general rule, Red Hat recommends to use unique, immutable claims within Rules. The general recommendation is to use the **sub** claim within the OIDC identity token. For more information about OIDC token claims, see [the list of standard OIDC claims](https://openid.net/specs/openid-connect-core-1_0.html#Claims).

8.  Click **Save**.

</div>

<a id="exchanging-identity-token_configure-short-lived-access"></a>

# Exchanging an identity token

<div>

<div class="title">

Prerequisites

</div>

- You have a valid OpenID Connect (OIDC) token.

- You added a **Machine access configuration** for the RHACS instance you want to access.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Prepare the POST request’s JSON data:

    ``` json
    {
        "idToken": "<id_token>"
    }
    ```

2.  Send a POST request to the API **/v1/auth/m2m/exchange**.

3.  Wait for the API response:

    ``` json
    {
        "accessToken": "<access_token>"
    }
    ```

4.  Use the returned access token to access the RHACS instance.

</div>

> [!NOTE]
> If you are using **GitHub Actions**, you can use the [stackrox/central-login GitHub Action](https://github.com/marketplace/actions/central-login).
