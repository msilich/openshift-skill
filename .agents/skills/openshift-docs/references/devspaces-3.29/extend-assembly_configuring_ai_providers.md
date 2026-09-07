> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/extend-assembly_configuring_ai_providers). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Register AI coding assistants for developers

Register AI coding assistants for developers so that they can select an AI provider when creating workspaces. Specify the API key and endpoint for each provider in a Kubernetes Secret. For information about how developers use AI assistants in workspaces, see Additional resources.

- **[Register an AI provider](extend-proc_configuring_ai_providers.md)**  
  Register one or more AI providers in OpenShift Dev Spaces so that developers can select and use AI coding assistants when creating workspaces.
- **[AI provider API key secret reference](extend-ref_ai_provider_api_key_secret_reference.md)**  
  Each user’s AI provider API key is stored as a OpenShift `Opaque` Secret in the user’s personal project. The Dev Workspace Controller automatically mounts matching Secrets as environment variables into all workspace containers.
- **[Disable AI coding assistants](extend-proc_disabling_ai_providers.md)**  
  Disable AI coding assistants by deleting the `ai-tool-registry` ConfigMap. The AI Provider section on the **Create Workspace** page is hidden when the ConfigMap is absent.

**Related information**  

- [Use AI assistants in workspaces](https://access.redhat.com/documentation/en-us/red_hat_openshift_dev_spaces/3.29/html-single/develop_tools/index#using-ai-assistants-in-workspaces_develop_tools)
