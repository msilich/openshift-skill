> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/develop-proc_automating_installation_of_vscode_extensions). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Automate installation of VS Code extensions at workspace startup

Automate installation of VS Code extensions by adding an `extensions.json` file to your project’s remote Git repository so that the Microsoft Visual Studio Code - Open Source IDE automatically installs chosen extensions at workspace startup.

## Before you begin

- You have the public OpenVSX registry at [open-vsx.org](https://open-vsx.org) selected and accessible over the internet. In a restricted environment, configure a private Open VSX registry, define a common IDE, or install extensions from VSX files instead.

## Procedure

1.  Get the publisher and extension names of each chosen extension:
    1.  Find the extension on the [Open VSX registry website](https://www.open-vsx.org/) and copy the URL of the extension’s listing page.

    2.  Extract the *\<publisher\>* and *\<extension\>* names from the copied URL:

        ``` plaintext
        https://www.open-vsx.org/extension/<publisher>/<extension>
        ```

2.  Create a `.vscode/extensions.json` file in the remote Git repository.

3.  Add the *\<publisher\>* and *\<extension\>* names to the `extensions.json` file as follows:

    ``` plaintext
      {
        "recommendations": [
          "<publisher_A>.<extension_B>",
          "<publisher_C>.<extension_D>",
          "<publisher_E>.<extension_F>"
        ]
      }
    ```

## Results

1.  [Start a new workspace by using the URL of the remote Git repository](get_started-proc_starting_a_workspace_from_a_git_repository_url.md) that contains the created `extensions.json` file.
2.  In the IDE of the workspace, press Ctrl+Shift+X or go to **Extensions** to find each of the extensions listed in the file.
3.  The extension has the label **This extension is enabled globally**.

**Related tasks**  

- [Define a common IDE](develop-proc_defining_a_common_ide.md "Define a common IDE for all workspaces in a Git repository by using a che-editor.yaml file so that all team members and new contributors use the most suitable IDE for the project. You can also use this file to override the OpenShift Dev Spaces instance default IDE for a particular Git repository.")

**Related information**  

- [How IDE extensions work in workspaces](extend-con_extensions_for_vscode.md)
- [Use an alternative extension registry](extend-proc_configuring_open_vsx_registry_url.md)
- [Installing extensions from VSX files](https://code.visualstudio.com/docs/editor/extension-marketplace#_install-from-a-vsix)
- [Open VSX registry - Extensions for Microsoft Visual Studio Code compatible editors](https://www.open-vsx.org/)
- [Microsoft Visual Studio Code - Workspace recommended extensions](https://code.visualstudio.com/docs/editor/extension-marketplace#_workspace-recommended-extensions)
