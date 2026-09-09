<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Red Hat Advanced Cluster Security for Kubernetes (RHACS) requires API tokens for some system integrations, authentication processes, and system functions. You can configure tokens by using the RHACS web interface.

<div class="note">

<div class="title">

</div>

- To prevent privilege escalation, when you create a new token, your role’s permissions limit the permission you can assign to that token. For example, if you only have `read` permission for the Integration resource, you cannot create a token with `write` permission.

- If you want a custom role to create tokens for other users to use, you must assign the required permissions to that custom role.

- Use short-lived tokens for machine-to-machine communication, such as CI/CD pipelines, scripts, and other automation. Also, use the `roxctl central login` command for human-to-machine communication, such as `roxctl` CLI or API access.

- The majority of cloud service providers support OIDC identity tokens, for example, Microsoft Entra ID, Google Cloud Identity Platform, and AWS Cognito. You can use OIDC identity tokens issued by these services for RHACS short-lived access.

- You can also use third-party OIDC identity tokens directly to access the API endpoint, without an exchange, if a machine-to-machine configuration exists for the token issuer.

</div>

<a id="create-api-token_configure-api-token"></a>

# Creating an API token

Create an API token in the RHACS portal with the required access level for authentication.

<div>

<div class="title">

Procedure

</div>

1.  In the RHACS portal, go to **Platform Configuration** → **Integrations**.

2.  Scroll to the **Authentication Tokens** category, and then click **API Token**.

3.  Click **Generate Token**.

4.  Enter a name for the token and select a role that provides the required level of access (for example, **Continuous Integration** or **Sensor Creator**).

5.  Click **Generate**.

    > [!IMPORTANT]
    > Copy the generated token and securely store it. You will not be able to view it again.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Using an authentication provider to authenticate with roxctl](../cli/using-the-roxctl-cli.md#using-an-authentication-provider-to-authenticate-with-roxctl_using-roxctl-cli)

- [Configuring short-lived access](../operating/manage-user-access/configure-short-lived-access.md)

- [Using Azure Entra ID service principals for machine to machine auth with RHACS](https://github.com/stackrox/contributions/blob/main/guides/cloud-provider-integrations/azure-service-principal-m2m-auth.md)

</div>

<a id="about-api-token-expiration_configure-api-token"></a>

# About API token expiration

You use API tokens in Red Hat Advanced Cluster Security for Kubernetes (RHACS) for several authentication and access functions, such as API access, CLI access, and authentication. API tokens expire one year from the creation date, and RHACS alerts you when a token expires soon.

RHACS provides notifications in the web interface and by sending log messages to Central when a token will expire in less than one week. The log message process runs every hour. The process lists the tokens that are expiring and creates a log message for each one every day. RHACS issues log messages daily and they appear in Central logs.

Logs have the format as shown in the following example:

``` text
Warn: API Token [token name] (ID [token ID]) will expire in less than X days.
```

<a id="api-token-expiration-environment-variables_configure-api-token"></a>

## Configuring API token expiration notification settings

You can customize the API token expiration notification behavior by configuring environment variables that control the notification frequency and detection window.

You can change the default settings for the log message process by configuring the environment variables shown in the following table:

|  |  |  |
|----|----|----|
| Environment variable | Default value | Description |
| ROX_TOKEN_EXPIRATION_NOTIFIER_INTERVAL | 1h (1 hour) | The frequency at which the log message background loop that lists tokens and creates the logs will run. |
| ROX_TOKEN_EXPIRATION_NOTIFIER_BACKOFF_INTERVAL | 24h (1 day) | The frequency at which the loop lists tokens and issues notifications. |
| ROX_TOKEN_EXPIRATION_DETECTION_WINDOW | 168h (1 week) | The time period before expiration of the token that triggers the notification. |
