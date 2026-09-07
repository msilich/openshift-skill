> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/extend-assembly_managing_editors). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Choose which editors are available

Choose which IDE options developers see when creating workspaces. Add custom editor definitions, set the default IDE, hide or restore editors, and host editor binaries internally for air-gapped clusters.

- **[Add custom editors to the dashboard](extend-proc_configuring_editors_definitions.md)**  
  Add custom editor definitions to OpenShift Dev Spaces by creating a devfile with the editor configuration and storing it in a ConfigMap to offer additional IDE options to your users.
- **[Set the default IDE for new workspaces](extend-proc_configuring_default_editor.md)**  
  Set the default editor that OpenShift Dev Spaces uses when creating new workspaces to ensure a consistent development experience. The default editor is specified by its plugin ID in the `publisher/name/version` format.
- **[Hide editors from the dashboard](extend-proc_concealing_editors.md)**  
  Hide selected OpenShift Dev Spaces editors from the Dashboard UI, for example IntelliJ IDEA Ultimate, and have only Visual Studio Code - Open Source visible.
- **[Restore access to deprecated editors](extend-proc_show_deprecated_editors.md)**  
  Restore access to deprecated OpenShift Dev Spaces editors on the Dashboard to support users who need them during migration to a supported editor. By default, the Dashboard UI hides them.
- **[Host editor binaries internally for air-gapped clusters](extend-proc_configuring_editors_download_urls.md)**  
  Host editor binaries internally by configuring custom download URLs for editors in air-gapped OpenShift Dev Spaces environments where editors cannot be retrieved from the public internet. This option applies only to JetBrains editors.

**Related concepts**  

- [Customize the default IDE](extend-assembly_configuring_vscode.md "Customize Visual Studio Code - Open Source for OpenShift Dev Spaces workspaces, including multi-root project layout, trusted and default extensions, and editor settings so that developers get a consistent IDE experience.")
