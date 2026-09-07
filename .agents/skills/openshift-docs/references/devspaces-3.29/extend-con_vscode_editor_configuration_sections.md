> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/extend-con_vscode_editor_configuration_sections). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# IDE configuration options you can customize

The Visual Studio Code - Open Source ("Code - OSS") editor supports several configuration sections in a ConfigMap. Each section maps to a specific editor config file and controls a different aspect of editor behavior.

The following sections are currently supported:

`settings.json`  
Contains various settings with which you can customize different parts of the Code - OSS editor.

`extensions.json`  
Contains recommended extensions that are installed when a workspace is started.

`product.json`  
Contains properties that you need to add to the editor’s **product.json** file. If the property already exists, its value is updated.

`configurations.json`  
Contains properties for Code - OSS editor configuration. For example, you can use the `extensions.install-from-vsix-enabled` property to disable the `Install from VSIX` menu item in the Extensions panel.

Note

The `extensions.install-from-vsix-enabled` property disables only the UI action. Extensions can still be installed by using the `workbench.extensions.command.installFromVSIX` API command or the CLI. To block these paths as well, manage extension installation policies.

`policy.json`  
Controls Code - OSS extension installation by using the `AllowedExtensions` policy and the ability to fully block extension installation.

For procedures to apply these configurations and manage extension installation policies, see Additional resources.

**Related tasks**  

- [Control which extensions users can install](extend-proc_managing_extension_installation.md "Control Code - OSS extension installation by using a ConfigMap. Enforce a fine-grained allow or deny list by using the AllowedExtensions policy.")
- [Apply IDE settings to all workspaces](extend-proc_applying_editor_configurations.md "Apply a OpenShift ConfigMap to standardize the Code - OSS editor across all workspaces, giving every developer the same settings, recommended extensions, and product properties at startup.")
