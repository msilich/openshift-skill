> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/extend-proc_adding_or_removing_extensions_in_a_workspace). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Add or remove extensions in a workspace

Add or remove extensions in the embedded Open VSX registry instance directly within a workspace to create a custom extension catalog for your organization.

## Before you begin

- You are logged in to the OpenShift cluster from the workspace terminal with cluster administrator permissions:

  ``` bash
  oc login --token=<token> --server=<api_server_url>
  ```

- You have started a workspace using the [plugin registry repository](https://github.com/redhat-developer/che-plugin-registry).

- You have created a [Red Hat Registry Service Account](https://access.redhat.com/RegistryAuthentication) and have the username and token available.

- You have the custom plugin registry built locally on the corresponding hardware for IBM Power (`ppc64le`) and IBM Z (`s390x`) architectures.

- You have a container image based on the latest tag or SHA to include the latest security fixes.

## About this task

Important

The embedded plugin registry is deprecated; the Open VSX Registry is its successor. Setting up an internal, on-premises Open VSX Registry provides full control over the extension lifecycle, enables offline use, and improves compliance. See [Deploy from a prebuilt image](extend-proc_deploy_open_vsx_with_prebuilt_image.md "Deploy a standalone Open VSX extension registry by using an existing container image. Use a private, on-premises registry to control which extensions are available in your OpenShift Dev Spaces workspaces without building from source.") or [Build a custom extension registry from source](extend-proc_deploy_open_vsx_from_source.md "Build custom Open VSX server and CLI images from source and deploy them to your cluster. A source build gives you full control over the Open VSX version and allows custom modifications to the registry.") for detailed setup instructions.

## Procedure

1.  Identify the publisher and extension name for each extension you want to add:
    1.  Find the extension on the [Open VSX registry website](https://open-vsx.org/).

    2.  Copy the URL of the extension’s listing page.

    3.  Extract the *\<publisher\>* and *\<name\>* from the URL:

        ``` plaintext
        https://open-vsx.org/extension/<publisher>/<name>
        ```

        Tip

        If the extension is only available from [Microsoft Visual Studio Marketplace](https://marketplace.visualstudio.com/VSCode) and not [Open VSX](https://open-vsx.org), ask the extension publisher to publish it on [open-vsx.org](https://open-vsx.org). See the [publishing instructions](https://github.com/eclipse-openvsx/openvsx/wiki/Publishing-Extensions#how-to-publish-an-extension) and the [GitHub action](https://github.com/marketplace/actions/publish-vs-code-extension).

        If the publisher is unavailable or unwilling, and no Open VSX equivalent exists, consider [reporting an issue](https://github.com/open-vsx/publish-extensions/issues) to the Open VSX team.

2.  Open the [`openvsx-sync.json`](https://github.com/redhat-developer/che-plugin-registry/blob/main/openvsx-sync.json) file in the workspace.

3.  Add or remove extensions using the following JSON syntax:

    ``` plaintext
        {
            "id": "<publisher>.<name>",
            "version": "<extension_version>"
        }
    ```

    Tip

    If you have a closed-source or internal-only extension, you can add it directly from a `.vsix` file. Use a URL accessible to your custom plugin registry container:

    ``` plaintext
        {
            "id": "<publisher>.<name>",
            "download": "<url_to_download_vsix_file>",
            "version": "<extension_version>"
        }
    ```

    Read the [Terms of Use](https://aka.ms/vsmarketplace-ToU) for the [Microsoft Visual Studio Marketplace](https://marketplace.visualstudio.com/VSCode) before using its resources.

4.  Log in to the Red Hat registry:
    1.  Navigate to **Terminal** **Run Task…​** **devfile**.
    2.  Run the **1. Login to registry.redhat.io** task.
    3.  Enter your Red Hat Registry Service Account credentials when prompted.

5.  Build and publish the custom plugin registry:
    1.  Navigate to **Terminal** **Run Task…​** **devfile**.

    2.  Run the **2. Build and Publish a Custom Plugin Registry** task. Note

        Verify that the `CHE_CODE_VERSION` in the [`build-config.json`](https://github.com/redhat-developer/che-plugin-registry/blob/main/build-config.json) file matches the version of the editor currently used with OpenShift Dev Spaces. Update it if necessary.

6.  Configure OpenShift Dev Spaces to use the custom plugin registry:
    1.  Navigate to **Terminal** **Run Task…​** **devfile**.
    2.  Run the **3. Configure Che to use the Custom Plugin Registry** task.

## Results

1.  Check that the `plugin-registry` pod has restarted and is running.
2.  Restart your workspace.
3.  Open the **Extensions** view in the IDE and verify that your added extensions are available.

**Related tasks**  

- [Deploy from a prebuilt image](extend-proc_deploy_open_vsx_with_prebuilt_image.md "Deploy a standalone Open VSX extension registry by using an existing container image. Use a private, on-premises registry to control which extensions are available in your OpenShift Dev Spaces workspaces without building from source.")
- [Build a custom extension registry from source](extend-proc_deploy_open_vsx_from_source.md "Build custom Open VSX server and CLI images from source and deploy them to your cluster. A source build gives you full control over the Open VSX version and allows custom modifications to the registry.")

**Related information**  

- [Plugin registry repository](https://github.com/redhat-developer/che-plugin-registry)
