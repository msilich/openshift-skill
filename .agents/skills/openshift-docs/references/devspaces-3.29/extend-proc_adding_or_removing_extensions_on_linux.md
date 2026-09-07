> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/extend-proc_adding_or_removing_extensions_on_linux). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Add or remove extensions from the Linux command line

Add or remove extensions in a custom plugin registry from the Linux command line to create a tailored Open VSX registry with the specific extensions your organization needs.

## Before you begin

- You have an active `oc` session with administrative permissions to the OpenShift cluster. See [Getting started with the CLI](https://docs.openshift.com/container-platform/4.22/cli_reference/openshift_cli/getting-started-cli.html).
- You have podman installed.
- You have Node.js version 18.20.3 or higher installed.
- You have created a [Red Hat Registry Service Account](https://access.redhat.com/RegistryAuthentication) and have the username and token available.
- You have a container image based on the latest tag or SHA to include the latest security fixes.

## Procedure

1.  Clone the plugin registry repository:

    ``` shell-session
    $ git clone https://github.com/redhat-developer/che-plugin-registry.git
    ```

2.  Change to the plugin registry directory:

    ``` shell-session
    $ cd che-plugin-registry/
    ```

3.  Log in to the Red Hat registry:

    ``` shell-session
    $ podman login registry.redhat.io
    ```

4.  Identify the publisher and extension name for each extension you want to add:
    1.  Find the extension on the [Open VSX registry website](https://open-vsx.org/).

    2.  Copy the URL of the extension’s listing page.

    3.  Extract the *\<publisher\>* and *\<name\>* from the URL:

        ``` plaintext
        https://open-vsx.org/extension/<publisher>/<name>
        ```

        Tip

        If the extension is only available from [Microsoft Visual Studio Marketplace](https://marketplace.visualstudio.com/VSCode) and not [Open VSX](https://open-vsx.org), ask the extension publisher to publish it on [open-vsx.org](https://open-vsx.org). See the [publishing instructions](https://github.com/eclipse-openvsx/openvsx/wiki/Publishing-Extensions#how-to-publish-an-extension) and the [GitHub action](https://github.com/marketplace/actions/publish-vs-code-extension).

        If the publisher is unavailable or unwilling, and no Open VSX equivalent exists, consider [reporting an issue](https://github.com/open-vsx/publish-extensions/issues) to the Open VSX team.

5.  Open the [`openvsx-sync.json`](https://github.com/redhat-developer/che-plugin-registry/blob/main/openvsx-sync.json) file.

6.  Add or remove extensions using the following JSON syntax:

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

7.  Build the plugin registry container image:

    ``` bash
    $ ./build.sh -o <username> -r quay.io -t custom
    ```

    Note

    Verify that the `CHE_CODE_VERSION` in the [`build-config.json`](https://github.com/redhat-developer/che-plugin-registry/blob/main/build-config.json) file matches the version of the editor currently used with OpenShift Dev Spaces. Update it if necessary.

8.  Push the image to a container registry such as [quay.io](https://quay.io/):

    ``` bash
    $ podman push quay.io/<username>/plugin_registry:custom
    ```

9.  Edit the `CheCluster` custom resource in your organization’s cluster to point to the image and save the changes:

    ``` yaml
    spec:
      components:
        pluginRegistry:
          deployment:
            containers:
              - image: quay.io/<username>/plugin_registry:custom
          openVSXURL: ''
    ```

## Results

1.  Check that the `plugin-registry` pod has restarted and is running.
2.  Restart your workspace.
3.  Open the **Extensions** view in the IDE and verify that your added extensions are available.

**Related tasks**  

- [Add or remove extensions in a workspace](extend-proc_adding_or_removing_extensions_in_a_workspace.md "Add or remove extensions in the embedded Open VSX registry instance directly within a workspace to create a custom extension catalog for your organization.")
- [Deploy from a prebuilt image](extend-proc_deploy_open_vsx_with_prebuilt_image.md "Deploy a standalone Open VSX extension registry by using an existing container image. Use a private, on-premises registry to control which extensions are available in your OpenShift Dev Spaces workspaces without building from source.")

**Related information**  

- [Plugin registry repository](https://github.com/redhat-developer/che-plugin-registry)
