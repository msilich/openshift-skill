> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/extend-assembly_managing_extensions). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Add or remove IDE extensions

Add or remove VS Code extensions in OpenShift Dev Spaces workspaces by changing the Open VSX registry URL, editing workspace devfiles, or using the command line.

- **[How IDE extensions work in workspaces](extend-con_extensions_for_vscode.md)**  
  IDE extensions in in OpenShift Dev Spaces workspaces use an Open VSX registry instance that controls which extensions are available, trusted, and pre-installed. Extension management supports air-gapped environments, security policies, and consistent tooling.
- **[Use an alternative extension registry](extend-proc_configuring_open_vsx_registry_url.md)**  
  Use an alternative Open VSX registry instance instead of the default embedded registry. Switch to the public open-vsx.org registry for internet-connected environments, or to a standalone on-premises instance for full control over available extensions.
- **[Add or remove extensions in a workspace](extend-proc_adding_or_removing_extensions_in_a_workspace.md)**  
  Add or remove extensions in the embedded Open VSX registry instance directly within a workspace to create a custom extension catalog for your organization.
- **[Add or remove extensions from the Linux command line](extend-proc_adding_or_removing_extensions_on_linux.md)**  
  Add or remove extensions in a custom plugin registry from the Linux command line to create a tailored Open VSX registry with the specific extensions your organization needs.

**Related concepts**  

- [Deploy a private extension registry](extend-assembly_deploying_private_registry.md "Deploy an on-premises Open VSX registry for air-gapped OpenShift Dev Spaces environments where workspaces cannot reach the public internet. Build the registry from a prebuilt image or from source, restrict it to internal traffic, and manage its extension catalog.")
