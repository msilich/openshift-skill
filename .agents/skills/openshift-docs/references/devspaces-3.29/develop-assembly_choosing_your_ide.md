> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/develop-assembly_choosing_your_ide). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Choose and configure your IDE

Choose and configure the IDE for your OpenShift Dev Spaces Cloud Development Environments. Connect Visual Studio Code or JetBrains IntelliJ IDEA, define a common IDE for your team, and automate extension installation.

- **[IDEs in Cloud Development Environments](develop-con_ides_in_workspaces.md)**  
  OpenShift Dev Spaces supports multiple Integrated Development Environments (IDEs) that can be used in workspaces. The default IDE is Microsoft Visual Studio Code - Open Source.
- **[Connect JetBrains IntelliJ IDEA Ultimate Edition to a new Dev Spaces workspace](develop-proc_connecting_jetbrains_intellij_to_devspaces.md)**  
  Connect your local IntelliJ IDEA Ultimate Edition IDE to a new OpenShift Dev Spaces workspace over JetBrains Gateway.
- **[Connect JetBrains IntelliJ IDEA Ultimate Edition to an existing Dev Spaces workspace](develop-proc_connecting_jetbrains_intellij_to_existing_workspace.md)**  
  Connect your local IntelliJ IDEA Ultimate Edition IDE to an existing OpenShift Dev Spaces workspace by using the JetBrains Gateway application, without accessing the OpenShift Dev Spaces Dashboard.
- **[Connect JetBrains Toolbox to an OpenShift Dev Spaces workspace](develop-proc_connecting_jetbrains_toolbox_to_devspaces.md)**  
  Connect your local JetBrains IDE to a running OpenShift Dev Spaces workspace by using the JetBrains Toolbox application.
- **[JetBrains Gateway plugin compatibility matrix](develop-ref_gateway_plugin_compatibility.md)**  
  The JetBrains Gateway provider plugin for OpenShift Dev Spaces requires specific versions of the JetBrains Gateway application to function correctly. Only plugin versions 0.0.14 and later are compatible with OpenShift Dev Spaces 3.24 through 3.29.
- **[Automate installation of VS Code extensions at workspace startup](develop-proc_automating_installation_of_vscode_extensions.md)**  
  Automate installation of VS Code extensions by adding an `extensions.json` file to your project’s remote Git repository so that the Microsoft Visual Studio Code - Open Source IDE automatically installs chosen extensions at workspace startup.
- **[Define a common IDE](develop-proc_defining_a_common_ide.md)**  
  Define a common IDE for all workspaces in a Git repository by using a `che-editor.yaml` file so that all team members and new contributors use the most suitable IDE for the project. You can also use this file to override the OpenShift Dev Spaces instance default IDE for a particular Git repository.
- **[Parameters for che-editor.yaml](develop-ref_parameters_for_che_editor_yaml.md)**  
  Configure the `che-editor.yaml` file to select and customize the IDE for your workspace, including the editor type, version, and container image.

**Related concepts**  

- [Use AI coding assistants](develop-assembly_using_ai_assistants.md "Use AI coding assistants in your OpenShift Dev Spaces Cloud Development Environments. Select a provider, configure your API key, set up GitHub Copilot Chat, and switch between tools.")
