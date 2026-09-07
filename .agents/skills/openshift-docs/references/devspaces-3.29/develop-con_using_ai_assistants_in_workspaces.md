> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/develop-con_using_ai_assistants_in_workspaces). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# AI assistants in Cloud Development Environments

OpenShift Dev Spaces supports AI coding assistants that are injected into workspaces and available from the terminal. You can select one or more AI providers when creating a workspace, and your administrator controls which providers are available.

Important

AI assistants in workspaces is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.

For more information about the support scope of Red Hat Technology Preview features, see Related information.

When your administrator configures AI providers, an **AI Provider** section is displayed on the **Create Workspace** page. Selecting a provider injects the tool binary into the workspace editor container and adds it to `PATH`.

If no AI providers are configured, the **AI Provider** section is hidden. To configure your API key and manage AI tools on existing workspaces, see Related information.

<span id="using-ai-assistants-in-workspaces_devspaces___default_ai_provider"></span>

## [Default AI provider](develop-con_using_ai_assistants_in_workspaces.md#using-ai-assistants-in-workspaces_devspaces___default_ai_provider)

If your administrator has set a default AI provider, the **Create Workspace** page displays it automatically. To override, expand **Choose an AI Provider** and select a different provider.

<span id="using-ai-assistants-in-workspaces_devspaces___ai_provider_column_in_the_workspaces_page"></span>

## [AI Provider column in the Workspaces page](develop-con_using_ai_assistants_in_workspaces.md#using-ai-assistants-in-workspaces_devspaces___ai_provider_column_in_the_workspaces_page)

The **Workspaces** page displays an **AI Provider(s)** column showing the injected AI tool for each workspace.

**Related tasks**  

- [Configure an AI provider API key](develop-proc_configuring_an_ai_provider_api_key.md "Configure an AI provider API key so that it is automatically injected as an environment variable into all your workspaces.")
- [Change the AI tool on a workspace](develop-proc_changing_the_ai_tool_on_a_workspace.md "Change the AI coding assistant on a stopped workspace without recreating it.")
- [Mount Secrets](develop-proc_mounting_secrets.md "Mount Kubernetes Secrets into workspace containers to provide sensitive configuration data such as credentials, API keys, and certificates.")

**Related reference**  

- [URL parameter for the AI provider](develop-ref_url_parameter_for_the_ai_provider.md "Use the ai-provider= URL parameter to specify one or more AI providers in a workspace start URL. The workspace launches with the selected AI tool binaries injected and ready to use, without requiring manual selection on the dashboard.")

**Related information**  

- [Technology Preview features support scope](https://access.redhat.com/support/offerings/techpreview/)
