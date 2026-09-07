> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/develop-con_ides_in_workspaces). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# IDEs in Cloud Development Environments

OpenShift Dev Spaces supports multiple Integrated Development Environments (IDEs) that can be used in workspaces. The default IDE is Microsoft Visual Studio Code - Open Source.

The `che-editors.yaml` file features the devfiles of all supported IDEs. For the file location, see Related information.

<span id="con_ides-in-workspaces_devspaces___supported_ides"></span>

## [Supported IDEs](develop-con_ides_in_workspaces.md#con_ides-in-workspaces_devspaces___supported_ides)

The default IDE in a new workspace is Microsoft Visual Studio Code - Open Source. Alternatively, you can choose another supported IDE:

<span id="con_ides-in-workspaces_devspaces___supported_ides__entry__1"></span><span id="con_ides-in-workspaces_devspaces___supported_ides__entry__2"></span><span id="con_ides-in-workspaces_devspaces___supported_ides__entry__3"></span><span id="con_ides-in-workspaces_devspaces___supported_ides__entry__4"></span>

<table>
<caption>Table 1. Supported IDEs</caption>
<thead>
<tr>
<th>IDE</th>
<th>Status</th>
<th><code>id</code></th>
<th>Note</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>Microsoft Visual Studio Code - Open Source</p></td>
<td><p>Available</p></td>
<td><ul>
<li><code>che-incubator/che-code/latest</code></li>
<li><code>che-incubator/che-code/insiders</code></li>
</ul></td>
<td><ul>
<li><code>latest</code> is the default IDE that loads in a new workspace when the URL parameter or <code>che-editor.yaml</code> is not used.</li>
<li><code>insiders</code> is the development version.</li>
</ul></td>
</tr>
<tr>
<td><p>JetBrains IntelliJ IDEA Ultimate Edition (over JetBrains Gateway)</p></td>
<td><p>Available</p></td>
<td><ul>
<li><code>che-incubator/che-idea-server/latest</code></li>
<li><code>che-incubator/che-idea-server/next</code></li>
</ul></td>
<td><ul>
<li><code>latest</code> is the stable version.</li>
<li><code>next</code> is the development version.</li>
</ul></td>
</tr>
<tr>
<td><p>JetBrains IDEs (over JetBrains Toolbox)</p></td>
<td><p>Available</p></td>
<td><ul>
<li><code>che-incubator/che-idea-server/toolbox</code></li>
</ul></td>
<td><ul>
<li>Connects a local JetBrains IDE to a workspace through the JetBrains Toolbox application.</li>
</ul></td>
</tr>
</tbody>
</table>

<span id="con_ides-in-workspaces_devspaces___which_ide_should_i_choose"></span>

## [Which IDE should I choose?](develop-con_ides_in_workspaces.md#con_ides-in-workspaces_devspaces___which_ide_should_i_choose)

Use Microsoft Visual Studio Code - Open Source if you want a browser-based experience with no local installation. Use JetBrains IntelliJ IDEA if your team already uses JetBrains IDEs and you prefer a desktop client connected to the remote workspace over SSH. Visual Studio Code - Open Source is the default and requires no additional setup. JetBrains requires installing JetBrains Gateway or JetBrains Toolbox on your local machine.

<span id="con_ides-in-workspaces_devspaces___repository_level_ide_configuration_in_openshift_dev_spaces"></span>

## [Repository-level IDE configuration in OpenShift Dev Spaces](develop-con_ides_in_workspaces.md#con_ides-in-workspaces_devspaces___repository_level_ide_configuration_in_openshift_dev_spaces)

You can store IDE configuration files directly in the remote Git repository that contains your project source code. This way, one common IDE configuration is applied to all new workspaces that feature a clone of that repository. Such IDE configuration files might include the following:

- The `/.che/che-editor.yaml` file that stores a definition of the chosen IDE.
- IDE-specific configuration files that one would typically store locally for a desktop IDE. For example, the `/.vscode/extensions.json` file.

<span id="con_ides-in-workspaces_devspaces___microsoft_visual_studio_code_open_source"></span>

## [Microsoft Visual Studio Code - Open Source](develop-con_ides_in_workspaces.md#con_ides-in-workspaces_devspaces___microsoft_visual_studio_code_open_source)

The OpenShift Dev Spaces build of Microsoft Visual Studio Code - Open Source is the default IDE of a new workspace.

You can automate installation of Microsoft Visual Studio Code extensions from the Open VSX registry at workspace startup. For instructions on automating extension installation and configuring che-editor.yaml, see Related information. To configure IDE preferences on a per-workspace basis, invoke the Command Palette and select **Preferences: Open Workspace Settings**.

You might see your organization's branding in this IDE if your organization customized it through a branded build.

Use Tasks to find and run the commands specified in `devfile.yaml`. The following **Dev Spaces** commands are available by clicking **Dev Spaces** in the Status Bar or through the Command Palette:

- **Dev Spaces: Open Dashboard**
- **Dev Spaces: Open OpenShift Console**
- **Dev Spaces: Stop Workspace**
- **Dev Spaces: Restart Workspace**
- **Dev Spaces: Restart Workspace from Local Devfile**
- **Dev Spaces: Open Documentation**

**Related concepts**  

- [Share preconfigured workspace links with your team](develop-assembly_optional_parameters_for_urls.md "Share preconfigured workspace links with your team by appending optional parameters to the URL that starts a new workspace so you can control the IDE, storage, resource limits, and devfile configuration without editing files.")

**Related tasks**  

- [Automate installation of VS Code extensions at workspace startup](develop-proc_automating_installation_of_vscode_extensions.md "Automate installation of VS Code extensions by adding an extensions.json file to your project’s remote Git repository so that the Microsoft Visual Studio Code - Open Source IDE automatically installs chosen extensions at workspace startup.")
- [Set up GitHub Copilot Chat](develop-proc_using_github_copilot_chat.md "Configure GitHub Copilot Chat in your OpenShift Dev Spaces workspace to receive AI-powered code suggestions, completions, and inline explanations directly in the editor.")
- [Define a common IDE](develop-proc_defining_a_common_ide.md "Define a common IDE for all workspaces in a Git repository by using a che-editor.yaml file so that all team members and new contributors use the most suitable IDE for the project. You can also use this file to override the OpenShift Dev Spaces instance default IDE for a particular Git repository.")

**Related reference**  

- [Parameters for che-editor.yaml](develop-ref_parameters_for_che_editor_yaml.md "Configure the che-editor.yaml file to select and customize the IDE for your workspace, including the editor type, version, and container image.")

**Related information**  

- [The che-editors.yaml file](https://github.com/redhat-developer/devspaces/blob/devspaces-3-rhel-8/dependencies/che-plugin-registry/che-editors.yaml)
- [Microsoft Visual Studio Code - Open Source (che-code) GitHub repository](https://github.com/che-incubator/che-code)
- [JetBrains Gateway plugin GitHub repository](https://github.com/redhat-developer/devspaces-gateway-plugin/)
- [JetBrains Toolbox plugin GitHub repository](https://github.com/redhat-developer/devspaces-toolbox-plugin)
- [Microsoft Visual Studio Code GitHub repository](https://github.com/microsoft/vscode)
- [Extensions for Microsoft Visual Studio Code - Open Source](extend-con_extensions_for_vscode.md)
- [Visual Studio Code: Tasks](https://code.visualstudio.com/Docs/editor/tasks)
- [Visual Studio Code: Status Bar](https://code.visualstudio.com/api/ux-guidelines/status-bar)
- [Visual Studio Code: Command Palette](https://code.visualstudio.com/api/ux-guidelines/command-palette)
