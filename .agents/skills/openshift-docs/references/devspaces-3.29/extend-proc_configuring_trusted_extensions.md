> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/extend-proc_configuring_trusted_extensions). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Grant extensions access to OAuth tokens

Grant specific extensions access to OAuth authentication tokens in Microsoft Visual Studio Code by configuring the `trustedExtensionAuthAccess` field. Extensions that access services such as GitHub or Microsoft can then authenticate without manual intervention.

## Before you begin

- You have an active `oc` session with administrative permissions to the OpenShift cluster. See [Getting started with the CLI](https://docs.openshift.com/container-platform/4.22/cli_reference/openshift_cli/getting-started-cli.html).

## About this task

``` plaintext
	"trustedExtensionAuthAccess": [
		"<publisher1>.<extension1>",
		"<publisher2>.<extension2>"
	]
```

Define the variable in the devfile or in a ConfigMap.

Warning

Use the `trustedExtensionAuthAccess` field with caution as it could potentially lead to security risks if misused. Give access only to trusted extensions.

Important

Since the Microsoft Visual Studio Code editor is bundled within `che-code` image, you can only change the `product.json` file when the workspace is started up.

## Procedure

1.  Define the `VSCODE_TRUSTED_EXTENSIONS` environment variable in devfile.yaml:

    ``` yaml
       env:
         - name: VSCODE_TRUSTED_EXTENSIONS
           value: "<publisher1>.<extension1>,<publisher2>.<extension2>"
    ```

2.  Alternatively, mount a ConfigMap with the `VSCODE_TRUSTED_EXTENSIONS` environment variable. With a ConfigMap, the variable is propagated to all your workspaces and you do not need to add the variable to each devfile you are using.

    ``` yaml
    kind: ConfigMap
    apiVersion: v1
    metadata:
      name: trusted-extensions
      labels:
        controller.devfile.io/mount-to-devworkspace: 'true'
        controller.devfile.io/watch-configmap: 'true'
      annotations:
        controller.devfile.io/mount-as: env
    data:
      VSCODE_TRUSTED_EXTENSIONS: '<publisher1>.<extension1>,<publisher2>.<extension2>'
    ```

## Results

- Start or restart the workspace and verify that the `trustedExtensionAuthAccess` section is added to the `product.json` file.

**Related tasks**  

- [Work with multiple projects in one workspace](extend-proc_configuring_single_and_multiroot_workspaces.md "Work with multiple project folders in the same workspace by using the multi-root workspace feature. This is useful when you are working on several related projects at once, such as product documentation and product code repositories.")
- [Pre-install extensions in every workspace](extend-proc_configuring_default_extensions.md "Pre-install VS Code extensions in OpenShift Dev Spaces workspaces by configuring the DEFAULT_EXTENSIONS environment variable to provide a consistent set of editor extensions on workspace startup.")
- [Apply IDE settings to all workspaces](extend-proc_applying_editor_configurations.md "Apply a OpenShift ConfigMap to standardize the Code - OSS editor across all workspaces, giving every developer the same settings, recommended extensions, and product properties at startup.")
