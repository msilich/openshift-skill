<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Use the `roxctl` CLI to interact with RHACS for authentication, configuration, and administrative tasks.

<a id="setting-up-environment-variables_using-roxctl-cli"></a>

# Prerequisites

Configure the `ROX_ENDPOINT` environment variable to specify the host and port information for Central.

<div>

<div class="title">

Procedure

</div>

- To configure the `ROX_ENDPOINT` environment variable, run the following command:

  ``` terminal
  $ export ROX_ENDPOINT=<host:port>
  ```

  where:

  `<host:port>`  
  Specifies the host and port information that you want to store in the `ROX_ENDPOINT` environment variable.

</div>

<a id="getting-authentication-information_using-roxctl-cli"></a>

# Getting authentication information

Use the `roxctl central whoami` command to retrieve information about your authentication status and user profile in Central. The example output illustrates the data you can expect to see, including user roles, access permissions, and various administrative functions.

<div>

<div class="title">

Procedure

</div>

- Run the following command to get information about your current authentication status and user information in Central:

  ``` terminal
  $ roxctl central whoami
  ```

  The following is an example output:

  ``` terminal
  UserID:
          <redacted>
  User name:
          <redacted>
  Roles:
   APIToken creator, Admin, Analyst, Continuous Integration, Network Graph Viewer, None, Sensor Creator, Vulnerability Management Approver, Vulnerability Management Requester, Vulnerability Manager, Vulnerability Report Creator
  Access:
    rw Access
    rw Administration
    rw Alert
    rw CVE
    rw Cluster
    rw Compliance
    rw Deployment
    rw DeploymentExtension
    rw Detection
    rw Image
    rw Integration
    rw K8sRole
    rw K8sRoleBinding
    rw K8sSubject
    rw Namespace
    rw NetworkGraph
    rw NetworkPolicy
    rw Node
    rw Secret
    rw ServiceAccount
    rw VulnerabilityManagementApprovals
    rw VulnerabilityManagementRequests
    rw WatchedImage
    rw WorkflowAdministration
  ```

  Review the output to ensure that the authentication and user details are as expected.

</div>

<a id="authenticating-by-using-the-roxctl-cli_using-roxctl-cli"></a>

# Authenticating by using the roxctl CLI

For authentication, you can use an API token, your administrator password, or the `roxctl central login` command.

Follow these guidelines for the effective use of API tokens:

- Use an API token in a production environment with continuous integration (CI). Each token receives specific access permissions, providing control over the actions it can perform. In addition, API tokens do not require interactive processes, such as browser-based logins, making them ideal for automated processes. These tokens have a time-to-live (TTL) value of 1 year, providing a longer validity period for seamless integration and operational efficiency.

- Use your administrator password only for testing purposes. Do not use it in the production environment.

- Use the `roxctl central login` command only for interactive, local uses.

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

- [Configuring API tokens](../configuration/configure-api-token.md)

- [Configuring short-lived access](../operating/manage-user-access/configure-short-lived-access.md)

</div>

<a id="create-api-token_using-roxctl-cli"></a>

## Creating an API token

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

<a id="cli-authentication_using-roxctl-cli"></a>

## Exporting and saving the API token

Export the generated API token as an environment variable or save it to a file for use with roxctl commands.

<div>

<div class="title">

Procedure

</div>

1.  After you have generated the authentication token, export it as the `ROX_API_TOKEN` variable by entering the following command:

    ``` terminal
    $ export ROX_API_TOKEN=<api_token>
    ```

2.  (Optional): You can also save the token in a file and use it with the `--token-file` option by entering the following command:

    ``` terminal
    $ roxctl central debug dump --token-file <token_file>
    ```

    Note the following guidelines:

    - You cannot use both the `-password` (`-p`) and the `--token-file` options simultaneously.

    - If you have already set the `ROX_API_TOKEN` variable, and specify the `--token-file` option, the `roxctl` CLI uses the specified token file for authentication.

    - If you have already set the `ROX_API_TOKEN` variable, and specify the `--password` option, the `roxctl` CLI uses the specified password for authentication.

</div>

<a id="using-an-authentication-provider-to-authenticate-with-roxctl_using-roxctl-cli"></a>

## Using an authentication provider to authenticate with roxctl

You can configure an authentication provider in Central and initiate the login process with the `roxctl` CLI. Set the `ROX_ENDPOINT` variable, initiate the login process with the `roxctl central login` command, select the authentication provider in a browser window, and retrieve the token information from the `roxctl` CLI as described in the following procedure.

<div>

<div class="title">

Prerequisite

</div>

- You selected an authentication provider of your choice, such as OpenID Connect (OIDC) with fragment or query mode.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Run the following command to set the `ROX_ENDPOINT` variable to Central hostname and port:

    ``` terminal
    export ROX_ENDPOINT=<central_hostname:port>
    ```

2.  Run the following command to initiate the login process to Central:

    ``` terminal
    $ roxctl central login
    ```

3.  Within the `roxctl` CLI, a URL is printed as output and you are redirected to a browser window where you can select the authentication provider you want to use.

4.  Log in with your authentication provider.

    After you have successfully logged in, the browser window indicates that authentication was successful and you can close the browser window.

5.  The `roxctl` CLI displays your token information including details such as the access token, the expiration time of the access token, the refresh token if one has been issued, and notification that the system stores these values locally.

    The following is an example output:

    ``` terminal
    Please complete the authorization flow in the browser with an auth provider of your choice.
    If no browser window opens, please click on the following URL:
            http://127.0.0.1:xxxxx/login
    INFO:   Received the following after the authorization flow from Central:
    INFO:   Access token: <redacted>
    INFO:   Access token expiration: 2023-04-19 13:58:43 +0000 UTC
    INFO:   Refresh token: <redacted>
    INFO:   Storing these values under $HOME/.roxctl/login…
    ```

    - `Access token: <redacted>` is the access token.

    - `Access token expiration: 2023-04-19 13:58:43 +0000 UTC` is the expiration time of the access token.

    - `Refresh token: <redacted>` is the refresh token.

    - `$HOME/.roxctl/login…` is the directory where the system stores values of the access token, the access token expiration time, and the refresh token locally.

      > [!IMPORTANT]
      > Ensure that you set the environment to determine the directory where the system stores the configuration. By default, the system stores the configuration in the `$HOME/.roxctl/roxctl-config` directory.
      >
      > - If you set the `$ROX_CONFIG_DIR` environment variable, the system stores the configuration in the `$ROX_CONFIG_DIR/roxctl-config` directory. This option has the highest priority.
      >
      > - If you set the `$XDG_RUNTIME_DIR` environment variable and the `$ROX_CONFIG_DIR` variable is not set, the system stores the configuration in the `$XDG_RUNTIME_DIR /roxctl-config` directory.
      >
      > - If you do not set the `$ROX_CONFIG_DIR` or `$XDG_RUNTIME_DIR` environment variable, the system stores the configuration in the `$HOME/.roxctl/roxctl-config` directory.

</div>

<a id="configuring-and-using-the-roxctl-cli-in-rhacs-cloud-service_using-roxctl-cli"></a>

# Configuring and using the roxctl CLI in RHACS Cloud Service

Configure the `roxctl` CLI for use with RHACS Cloud Service by setting the API token and endpoint environment variables.

<div>

<div class="title">

Procedure

</div>

- Export the `ROX_API_TOKEN` by running the following command:

  ``` terminal
  $ export ROX_API_TOKEN=<api_token>
  ```

- Export the `ROX_ENDPOINT` by running the following command:

  ``` terminal
  $ export ROX_ENDPOINT=<address>:<port_number>
  ```

- You can use the `--help` option to get more information about the commands.

- In Red Hat Advanced Cluster Security Cloud Service (RHACS Cloud Service), when using `roxctl` commands that require the Central address, use the **Central instance address** as displayed in the **Instance Details** section of the Red Hat Hybrid Cloud Console. For example, use `acs-ABCD12345.acs.rhcloud.com` instead of `acs-data-ABCD12345.acs.rhcloud.com`.

</div>
