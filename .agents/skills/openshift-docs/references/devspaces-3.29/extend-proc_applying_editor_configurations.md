> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/extend-proc_applying_editor_configurations). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Apply IDE settings to all workspaces

Apply a OpenShift ConfigMap to standardize the Code - OSS editor across all workspaces, giving every developer the same settings, recommended extensions, and product properties at startup.

## Before you begin

- You have an active OpenShift Dev Spaces workspace or you are ready to start one.
- You have an active `oc` session with permissions to create ConfigMaps in user projects.

## About this task

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

The `extensions.install-from-vsix-enabled` property disables only the UI action. Extensions can still be installed by using the `workbench.extensions.command.installFromVSIX` API command or the CLI. To block these paths as well, see [Control which extensions users can install](extend-proc_managing_extension_installation.md "Control Code - OSS extension installation by using a ConfigMap. Enforce a fine-grained allow or deny list by using the AllowedExtensions policy.").

`policy.json`  
Controls Code - OSS extension installation by using the `AllowedExtensions` policy and the ability to fully block extension installation. See [Control which extensions users can install](extend-proc_managing_extension_installation.md "Control Code - OSS extension installation by using a ConfigMap. Enforce a fine-grained allow or deny list by using the AllowedExtensions policy.").

## Procedure

1.  Add a new ConfigMap in valid JSON format to the user’s project, define the supported sections, and specify the properties you want to add.

    ``` yaml
    apiVersion: v1
    kind: ConfigMap
    metadata:
      name: vscode-editor-configurations
      labels:
         app.kubernetes.io/part-of: che.eclipse.org
         app.kubernetes.io/component: workspaces-config
    data:
      extensions.json: |
        {
          "recommendations": [
              "dbaeumer.vscode-eslint",
              "github.vscode-pull-request-github"
          ]
        }
      settings.json: |
        {
          "window.header": "A HEADER MESSAGE",
          "window.commandCenter": false,
          "workbench.colorCustomizations": {
            "titleBar.activeBackground": "#CCA700",
            "titleBar.activeForeground": "#ffffff"
          }
        }
      product.json: |
        {
          "extensionEnabledApiProposals": {
            "ms-python.python": [
              "contribEditorContentMenu",
              "quickPickSortByLabel"
            ]
          },
          "trustedExtensionAuthAccess": [
            "<publisher1>.<extension1>",
            "<publisher2>.<extension2>"
          ]
        }
      configurations.json: |
        {
          "extensions.install-from-vsix-enabled": false
        }
    ```

    where:

    *`<publisher1>`*`.`*`<extension1>`*, *`<publisher2>`*`.`*`<extension2>`*  
    The publisher and extension name pairs for extensions that are granted trusted authentication access. Use the format `publisher.extensionName`.

2.  Optional: To replicate the ConfigMap across all user projects while preventing user modifications, add the ConfigMap to the `openshift-devspaces` namespace instead of individual user projects.

3.  Start or restart your workspace.

## Results

1.  Verify that settings defined in the ConfigMap are applied using one of the following methods:
    - Use `F1 Preferences: Open Remote Settings` to check if the defined settings are applied.
    - Ensure that the settings from the ConfigMap are present in the `/checode/remote/data/Machine/settings.json` file by using the `F1 File: Open File…​` command to inspect the file’s content.
2.  Verify that extensions defined in the ConfigMap are applied:
    - Go to the `Extensions` view (`F1 View: Show Extensions`) and check that the extensions are installed
    - Ensure that the extensions from the ConfigMap are present in the `.code-workspace` file by using the `F1 File: Open File…​` command. By default, the workspace file is placed at `/projects/.code-workspace`.
3.  Verify that product properties defined in the ConfigMap are being added to the Visual Studio Code **product.json**:
    - Open a terminal, run the command `cat /checode/entrypoint-logs.txt | grep -a "Node.js dir"` and copy the Visual Studio Code path.
    - Press `Ctrl + O`, paste the copied path and open **product.json** file.
    - Ensure that **product.json** file contains all the properties defined in the ConfigMap.
4.  Verify that `extensions.install-from-vsix-enabled` property defined in the ConfigMap is applied to the Code - OSS editor:
    - Open the Command Palette (use `F1`) to check that `Install from VSIX` command is not present in the list of commands.
    - Use `F1 Open View Extensions` to open the `Extensions` panel, then click `…​` on the view (`Views and More Actions` tooltip) to check that `Install from VSIX` action is absent in the list of actions.
    - Go to the Explorer, find a file with the `vsix` extension (redhat.vscode-yaml-1.17.0.vsix, for example), open menu for that file. `Install from VSIX` action should be absent in the menu.

**Related tasks**  

- [Work with multiple projects in one workspace](extend-proc_configuring_single_and_multiroot_workspaces.md "Work with multiple project folders in the same workspace by using the multi-root workspace feature. This is useful when you are working on several related projects at once, such as product documentation and product code repositories.")
- [Grant extensions access to OAuth tokens](extend-proc_configuring_trusted_extensions.md "Grant specific extensions access to OAuth authentication tokens in Microsoft Visual Studio Code by configuring the trustedExtensionAuthAccess field. Extensions that access services such as GitHub or Microsoft can then authenticate without manual intervention.")
- [Pre-install extensions in every workspace](extend-proc_configuring_default_extensions.md "Pre-install VS Code extensions in OpenShift Dev Spaces workspaces by configuring the DEFAULT_EXTENSIONS environment variable to provide a consistent set of editor extensions on workspace startup.")

**Related information**  

- [Synchronize resources across user namespaces](configure-proc_configuring_a_user_namespace.md)
