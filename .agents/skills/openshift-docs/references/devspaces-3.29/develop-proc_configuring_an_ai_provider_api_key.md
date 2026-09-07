> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/develop-proc_configuring_an_ai_provider_api_key). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Configure an AI provider API key

Configure an AI provider API key so that it is automatically injected as an environment variable into all your workspaces.

## Before you begin

- Your administrator has enabled at least one AI provider.
- You have a valid API key from your AI provider.

## About this task

Important

AI assistants in workspaces is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.

For more information about the support scope of Red Hat Technology Preview features, see <https://access.redhat.com/support/offerings/techpreview/>.

## Procedure

Configure the API key using one of the following methods:

- **From the Create Workspace page:**
  1.  Navigate to **Create Workspace**.

  2.  In the **AI Provider** section, expand **Choose an AI Provider**.

  3.  Click the provider card.

  4.  Enter your API key and click **Save key**.

      A **Key configured** badge is displayed on the provider card.
- **From User Preferences:**
  1.  Navigate to **User Preferences \> AI Providers Keys**.

  2.  Click **Add API Key**.

  3.  Select the AI provider and enter the API key.

  4.  Click **Save**.

      To update or delete a key, use the edit or delete icons in the table row.

## Results

1.  Start a workspace with the configured AI provider.

2.  Open a terminal and verify that the tool binary is in `PATH` and the API key variable is set:

    ``` plaintext
    $ which opencode
    $ test -n "$OPENAI_API_KEY" && echo "API key is configured"
    ```

Note

The API key is available in all workspaces in your project, including already running ones.

**Related concepts**  

- [AI assistants in Cloud Development Environments](develop-con_using_ai_assistants_in_workspaces.md "OpenShift Dev Spaces supports AI coding assistants that are injected into workspaces and available from the terminal. You can select one or more AI providers when creating a workspace, and your administrator controls which providers are available.")

**Related tasks**  

- [Mount Secrets](develop-proc_mounting_secrets.md "Mount Kubernetes Secrets into workspace containers to provide sensitive configuration data such as credentials, API keys, and certificates.")
