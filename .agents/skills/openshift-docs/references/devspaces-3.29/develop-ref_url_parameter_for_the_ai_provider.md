> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/develop-ref_url_parameter_for_the_ai_provider). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# URL parameter for the AI provider

Use the `ai-provider=` URL parameter to specify one or more AI providers in a workspace start URL. The workspace launches with the selected AI tool binaries injected and ready to use, without requiring manual selection on the dashboard.

Important

AI assistants in workspaces is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.

For more information about the support scope of Red Hat Technology Preview features, see <https://access.redhat.com/support/offerings/techpreview/>.

The URL parameter accepts a comma-separated list of provider IDs:

``` plaintext
https://<openshift_dev_spaces_fqdn>#<git_repository_url>?ai-provider=<provider_id>
```

For example, with a single provider:

`https://`*`<openshift_dev_spaces_fqdn>`*`#`*`<git_repository_url>`*`?ai-provider=opencodeai/opencode`

Note

The `ai-provider=` parameter requires that the AI tool registry ConfigMap is configured by the administrator. Provider IDs not found in the registry are ignored.
