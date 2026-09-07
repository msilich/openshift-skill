> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/whats_new-ref_technology_preview). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Technology Preview

Technology Preview features in Red Hat OpenShift Dev Spaces provide early access to experiment with new capabilities, provide feedback, and prepare your teams. Evaluate how new features fit into your development platform strategy and plan implementations ahead of general availability.

Using Technology Preview features helps you to:

- **Test new capabilities early:** Experiment with upcoming features in non-production environments to understand their potential value and fit for your use case.
- **Provide feedback:** Share your experience with Red Hat to help shape the final implementation of features before they reach general availability.
- **Plan ahead:** Identify integration points, training needs, and process changes before features become production-ready.

Important

Technology Preview features are not fully supported under Red Hat Subscription Level Agreements, may not be functionally complete, and are not intended for production use. As Red Hat considers making future iterations of Technology Preview features generally available, we will attempt to resolve any issues that customers experience when using these features. See: [Technology Preview support scope](https://access.redhat.com/support/offerings/techpreview/).

## Connecting to workspaces from a local IDE with the Dev Spaces Connector extension

To enable a seamless local-to-remote development experience, you can now connect to OpenShift Dev Spaces workspaces directly from a local Kiro IDE or VS Code instance by using the Dev Spaces Connector extension. The extension provides one-click OAuth2 authentication, workspace management from the sidebar, and automatic reconnection without requiring SSH or CLI tools. The extension is available on the [OpenVSX Registry](https://open-vsx.org/extension/redhat/devspaces-remote-connector).

**Additional resources**

- [CRW-10968](https://redhat.atlassian.net/browse/CRW-10968)

## Integrate AI coding assistants into the development workflow

To enable AI-assisted development in cloud workspaces, administrators can configure AI coding tool providers in a labeled ConfigMap and make them available to developers through the OpenShift Dev Spaces Dashboard. Developers can select an AI provider when creating a workspace, manage API keys in User Preferences, and view or change the active AI tool on existing workspaces.

**AI provider and tool configuration:** Administrators define AI providers and tools in a ConfigMap with the labels `app.kubernetes.io/component: ai-tool-registry` and `app.kubernetes.io/part-of: che.eclipse.org`. The Dashboard discovers the ConfigMap by these labels, so the ConfigMap name can be any valid value.

**AI provider selector on workspace creation:** The Get Started page includes a selector for AI providers. The selected provider ID is passed as a factory URL parameter (`ai-provider=`) and the tool is injected into the DevWorkspace at creation time.

**API key management in User Preferences:** An AI Providers Keys tab in User Preferences allows developers to list, add, update, and delete API keys. Keys are stored as Kubernetes Secrets with auto-mount labels so the DevWorkspace Controller injects them as environment variables.

**AI tool info on Workspace Details:** The Workspace Details Overview tab shows the currently injected AI tool. Developers can view available tools and switch to a different one when the workspace is stopped.

Important

Integrating AI coding assistants into the development workflow is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.

**Additional resources**

- [CRW-11424](https://redhat.atlassian.net/browse/CRW-11424)
