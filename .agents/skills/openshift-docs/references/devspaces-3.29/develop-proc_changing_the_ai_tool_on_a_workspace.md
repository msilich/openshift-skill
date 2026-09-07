> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/develop-proc_changing_the_ai_tool_on_a_workspace). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Change the AI tool on a workspace

Change the AI coding assistant on a stopped workspace without recreating it.

## Before you begin

- You have a stopped workspace.

## About this task

Important

AI assistants in workspaces is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.

For more information about the support scope of Red Hat Technology Preview features, see <https://access.redhat.com/support/offerings/techpreview/>.

## Procedure

1.  Navigate to **Workspaces** and click the workspace name.

2.  On the **Overview** tab, find the **AI Tool** section.

3.  Click the edit icon, select a different tool or **None**, and click **Save**. Note

    The AI tool can only be changed while the workspace is stopped.

**Related concepts**  

- [AI assistants in Cloud Development Environments](develop-con_using_ai_assistants_in_workspaces.md "OpenShift Dev Spaces supports AI coding assistants that are injected into workspaces and available from the terminal. You can select one or more AI providers when creating a workspace, and your administrator controls which providers are available.")

**Related tasks**  

- [Configure an AI provider API key](develop-proc_configuring_an_ai_provider_api_key.md "Configure an AI provider API key so that it is automatically injected as an environment variable into all your workspaces.")
