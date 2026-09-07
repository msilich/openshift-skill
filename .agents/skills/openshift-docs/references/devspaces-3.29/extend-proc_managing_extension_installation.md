> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/extend-proc_managing_extension_installation). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Control which extensions users can install

Control Code - OSS extension installation by using a ConfigMap. Enforce a fine-grained allow or deny list by using the `AllowedExtensions` policy.

## Before you begin

- You have an active `oc` session with administrative permissions to the OpenShift cluster. See [Getting started with the CLI](https://docs.openshift.com/container-platform/4.22/cli_reference/openshift_cli/getting-started-cli.html).

## About this task

You can also block installs through the CLI, default extensions, and the `workbench.extensions.command.installFromVSIX` API command. The following properties are supported:

- `BlockCliExtensionsInstallation` — when enabled, blocks installation of extensions through the CLI.
- `BlockDefaultExtensionsInstallation` — when enabled, blocks installation of default extensions. See [Pre-install extensions in every workspace](extend-proc_configuring_default_extensions.md "Pre-install VS Code extensions in OpenShift Dev Spaces workspaces by configuring the DEFAULT_EXTENSIONS environment variable to provide a consistent set of editor extensions on workspace startup.").
- `BlockInstallFromVSIXCommandExtensionsInstallation` — when enabled, blocks installation of extensions through the `workbench.extensions.command.installFromVSIX` API command.
- `AllowedExtensions` — provides fine-grained control over Code - OSS extension installation. When this policy is applied, already installed extensions that are not allowed are disabled and display a warning. For conceptual background, see [Configure allowed extensions](https://code.visualstudio.com/docs/setup/enterprise#_configure-allowed-extensions).

## Procedure

1.  Add a new ConfigMap to the `openshift-devspaces` namespace and specify the properties you want to add:

    ``` yaml
    kind: ConfigMap
    apiVersion: v1
    metadata:
      name: vscode-editor-configurations
      namespace: openshift-devspaces
      labels:
        app.kubernetes.io/component: workspaces-config
        app.kubernetes.io/part-of: che.eclipse.org
      annotations:
        controller.devfile.io/mount-as: subpath
        controller.devfile.io/mount-path: /checode-config
        controller.devfile.io/read-only: 'true'
    data:
      policy.json: |
        {
          "BlockCliExtensionsInstallation": true,
          "BlockDefaultExtensionsInstallation": true,
          "BlockInstallFromVSIXCommandExtensionsInstallation": true,
          "AllowedExtensions": {
              "*": true,
              "dbaeumer.vscode-eslint": false,
              "ms-python.python": false,
              "redhat": false
           }
        }
    ```

    Note

    Ensure that the ConfigMap contains data in a valid JSON format.

2.  Optional: To completely disable extension installation instead of using fine-grained control, set all extensions to disallowed:

    ``` yaml
    kind: ConfigMap
    apiVersion: v1
    metadata:
      name: vscode-editor-configurations
      namespace: openshift-devspaces
      labels:
        app.kubernetes.io/component: workspaces-config
        app.kubernetes.io/part-of: che.eclipse.org
      annotations:
        controller.devfile.io/mount-as: subpath
        controller.devfile.io/mount-path: /checode-config
        controller.devfile.io/read-only: 'true'
    data:
      policy.json: |
        {
          "AllowedExtensions": {
            "*": false
          }
        }
    ```

3.  Start or restart your workspace.

4.  Optional: Add the ConfigMap in the user’s project:

    ``` yaml
    kind: ConfigMap
    apiVersion: v1
    metadata:
      name: vscode-editor-configurations
      labels:
        controller.devfile.io/mount-to-devworkspace: 'true'
        controller.devfile.io/watch-configmap: 'true'
      annotations:
        controller.devfile.io/mount-as: subpath
        controller.devfile.io/mount-path: /checode-config
        controller.devfile.io/read-only: 'true'
    data:
      policy.json: |
        {
          "AllowedExtensions": {
              "*": false
           }
        }
    ```

    Note

    When the ConfigMap is stored in the user’s project, the user can edit its values.

## Results

1.  Verify that the `BlockCliExtensionsInstallation` property is applied:
    - Press F1, select **Preferences: Open Settings (UI)**, and enter `BlockCliExtensionsInstallation` in search.
    - Provide a `.vsix` file and try CLI install. The installation fails with "Installation of extensions via CLI has been blocked by an administrator".
2.  Verify that the `BlockDefaultExtensionsInstallation` property is applied:
    - Check Settings for the property.
    - Configure default extensions and verify they are not installed on workspace start or restart.
3.  Verify that the `BlockInstallFromVSIXCommandExtensionsInstallation` property is applied:
    - Check Settings for the property.
    - The `workbench.extensions.command.installFromVSIX` API command is blocked.
4.  Verify that rules defined in the `AllowedExtensions` section are applied:
    - Check **Settings** `extensions.allowed`.
    - Disallowed extensions display a "This extension cannot be installed because it is not in the allowed list" warning.

**Related tasks**  

- [Apply IDE settings to all workspaces](extend-proc_applying_editor_configurations.md "Apply a OpenShift ConfigMap to standardize the Code - OSS editor across all workspaces, giving every developer the same settings, recommended extensions, and product properties at startup.")
- [Pre-install extensions in every workspace](extend-proc_configuring_default_extensions.md "Pre-install VS Code extensions in OpenShift Dev Spaces workspaces by configuring the DEFAULT_EXTENSIONS environment variable to provide a consistent set of editor extensions on workspace startup.")

**Related information**  

- [Configure allowed extensions](https://code.visualstudio.com/docs/setup/enterprise#_configure-allowed-extensions)
