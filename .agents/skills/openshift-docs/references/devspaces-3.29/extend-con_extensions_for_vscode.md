> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/extend-con_extensions_for_vscode). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# How IDE extensions work in workspaces

IDE extensions in in OpenShift Dev Spaces workspaces use an Open VSX registry instance that controls which extensions are available, trusted, and pre-installed. Extension management supports air-gapped environments, security policies, and consistent tooling.

To manage extensions, this IDE uses one of the Open VSX registry instances:

- The embedded instance of the Open VSX registry that runs in the `plugin-registry` pod of OpenShift Dev Spaces to support air-gapped, offline, and proxy-restricted environments. The embedded Open VSX registry contains only a subset of the extensions published on the public open-vsx.org registry. This subset is customizable.
- The public open-vsx.org registry that is accessed over the internet.
- A standalone Open VSX registry instance that is deployed on a network accessible from OpenShift Dev Spaces workspace pods.

The default is the embedded instance of the Open VSX registry. For more information about the Open VSX registry and managing extensions in your workspaces, see Additional resources.

**Related tasks**  

- [Add or remove extensions in a workspace](extend-proc_adding_or_removing_extensions_in_a_workspace.md "Add or remove extensions in the embedded Open VSX registry instance directly within a workspace to create a custom extension catalog for your organization.")
- [Add or remove extensions from the Linux command line](extend-proc_adding_or_removing_extensions_on_linux.md "Add or remove extensions in a custom plugin registry from the Linux command line to create a tailored Open VSX registry with the specific extensions your organization needs.")

**Related information**  

- [Microsoft Visual Studio Code - Open Source source code repository](https://github.com/microsoft/vscode)
- [Open VSX registry](https://open-vsx.org/about)
- [open-vsx.org](https://open-vsx.org)
