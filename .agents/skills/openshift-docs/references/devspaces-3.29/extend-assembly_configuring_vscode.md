> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/extend-assembly_configuring_vscode). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Customize the default IDE

Customize Visual Studio Code - Open Source for OpenShift Dev Spaces workspaces, including multi-root project layout, trusted and default extensions, and editor settings so that developers get a consistent IDE experience.

- **[Work with multiple projects in one workspace](extend-proc_configuring_single_and_multiroot_workspaces.md)**  
  Work with multiple project folders in the same workspace by using the multi-root workspace feature. This is useful when you are working on several related projects at once, such as product documentation and product code repositories.
- **[Grant extensions access to OAuth tokens](extend-proc_configuring_trusted_extensions.md)**  
  Grant specific extensions access to OAuth authentication tokens in Microsoft Visual Studio Code by configuring the `trustedExtensionAuthAccess` field. Extensions that access services such as GitHub or Microsoft can then authenticate without manual intervention.
- **[Pre-install extensions in every workspace](extend-proc_configuring_default_extensions.md)**  
  Pre-install VS Code extensions in OpenShift Dev Spaces workspaces by configuring the `DEFAULT_EXTENSIONS` environment variable to provide a consistent set of editor extensions on workspace startup.
- **[IDE configuration options you can customize](extend-con_vscode_editor_configuration_sections.md)**  
  The Visual Studio Code - Open Source ("Code - OSS") editor supports several configuration sections in a ConfigMap. Each section maps to a specific editor config file and controls a different aspect of editor behavior.
- **[Apply IDE settings to all workspaces](extend-proc_applying_editor_configurations.md)**  
  Apply a OpenShift ConfigMap to standardize the Code - OSS editor across all workspaces, giving every developer the same settings, recommended extensions, and product properties at startup.
- **[Control which extensions users can install](extend-proc_managing_extension_installation.md)**  
  Control Code - OSS extension installation by using a ConfigMap. Enforce a fine-grained allow or deny list by using the `AllowedExtensions` policy.

**Related concepts**  

- [Add or remove IDE extensions](extend-assembly_managing_extensions.md "Add or remove VS Code extensions in OpenShift Dev Spaces workspaces by changing the Open VSX registry URL, editing workspace devfiles, or using the command line.")
