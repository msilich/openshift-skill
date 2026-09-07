> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/extend-proc_configuring_default_extensions). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Pre-install extensions in every workspace

Pre-install VS Code extensions in OpenShift Dev Spaces workspaces by configuring the `DEFAULT_EXTENSIONS` environment variable to provide a consistent set of editor extensions on workspace startup.

## Before you begin

- You have an active `oc` session with administrative permissions to the OpenShift cluster. See [Getting started with the CLI](https://docs.openshift.com/container-platform/4.22/cli_reference/openshift_cli/getting-started-cli.html).

## About this task

After startup, the editor checks for the `DEFAULT_EXTENSIONS` environment variable and installs the specified extensions in the background. To specify multiple extensions, separate the paths with a semicolon.

There are three ways to embed default `.vsix` extensions into your workspace:

- Add the extension binary to the source repository.
- Use the devfile `postStart` event to fetch extension binaries from the network.
- Include the extensions' `.vsix` binaries in the `che-code` image.

## Procedure

1.  Add the extension binary to the source repository.

    Adding the extension binary to the Git repository and defining the environment variable in the devfile is the easiest way to add default extensions to your workspace. If the `extension.vsix` file exists in the repository root, set the `DEFAULT_EXTENSIONS` environment variable for the tooling container in your `.devfile.yaml`:

    ``` yaml
    schemaVersion: 2.3.0
    metadata:
      generateName: example-project
    components:
      - name: tools
        container:
          image: quay.io/devfile/universal-developer-image:ubi8-latest
          env:
            - name: 'DEFAULT_EXTENSIONS'
              value: '/projects/example-project/extension.vsix'
    ```

2.  Use the devfile `postStart` event to fetch extension binaries from the network.

    Use cURL or GNU Wget to download extensions to your workspace. Specify a devfile command to download extensions and add a `postStart` event to run the command on workspace startup. Define the `DEFAULT_EXTENSIONS` environment variable in the devfile:

    ``` yaml
    schemaVersion: 2.3.0
    metadata:
      generateName: example-project
    components:
      - name: tools
        container:
          image: quay.io/devfile/universal-developer-image:ubi8-latest
          env:
            - name: DEFAULT_EXTENSIONS
              value: '/tmp/extension-1.vsix;/tmp/extension-2.vsix'

    commands:
      - id: add-default-extensions
        exec:
          # name of the tooling container
          component: tools
          # download several extensions using curl
          commandLine: |
            curl https://.../extension-1.vsix --location -o /tmp/extension-1.vsix
            curl https://.../extension-2.vsix --location -o /tmp/extension-2.vsix

    events:
      postStart:
        - add-default-extensions
    ```

    Warning

    In some cases curl may download a `.gzip` compressed file. This might make installing the extension impossible. To fix that, save the file as a **.vsix.gz** file and then decompress it with **gunzip**. This replaces the **.vsix.gz** file with an unpacked **.vsix** file: `curl `[`https://some-extension-url`](https://some-extension-url)` --location -o /tmp/extension.vsix.gz && gunzip /tmp/extension.vsix.gz`

3.  Include the extensions `.vsix` binaries in the `che-code` image.

    Bundling extensions in the editor image and defining the `DEFAULT_EXTENSIONS` environment variable in a ConfigMap applies default extensions without changing the devfile.

    1.  Create a directory and place your selected `.vsix` extensions in this directory.

    2.  Create a Dockerfile with the following content:

        ``` plaintext
        # inherit che-incubator/che-code:latest
        FROM quay.io/che-incubator/che-code:latest
        USER 0

        # copy all .vsix files to /default-extensions directory
        RUN mkdir --mode=775 /default-extensions
        COPY --chmod=755 *.vsix /default-extensions/

        # add instruction to the script to copy default extensions to the working container
        RUN echo "cp -r /default-extensions /checode/" >> /entrypoint-init-container.sh
        ```

    3.  Build the image and then push it to a registry:

        ``` bash
        $ docker build -t yourname/che-code:next .
        $ docker push yourname/che-code:next
        ```

    4.  Add the new ConfigMap to the user’s project, define the `DEFAULT_EXTENSIONS` environment variable, and specify the absolute paths to the extensions. This ConfigMap sets the environment variable to all workspaces in the user’s project.

        ``` yaml
        kind: ConfigMap
        apiVersion: v1
        metadata:
          name: vscode-default-extensions
          labels:
            controller.devfile.io/mount-to-devworkspace: 'true'
            controller.devfile.io/watch-configmap: 'true'
          annotations:
            controller.devfile.io/mount-as: env
        data:
          DEFAULT_EXTENSIONS: '/checode/default-extensions/extension1.vsix;/checode/default-extensions/extension2.vsix'
        ```

    5.  Open the OpenShift Dev Spaces Dashboard and navigate to the **Create Workspace** tab on the left side.

    6.  In the **Editor Selector** section, expand the **Use an Editor Definition** dropdown and set the editor URI to `yourname/che-code:next`.

    7.  Create a workspace by selecting a sample or entering a Git repository URL.

## Results

- Verify that the extensions are installed in the workspace by checking the **Extensions** panel in the editor.

**Related tasks**  

- [Work with multiple projects in one workspace](extend-proc_configuring_single_and_multiroot_workspaces.md "Work with multiple project folders in the same workspace by using the multi-root workspace feature. This is useful when you are working on several related projects at once, such as product documentation and product code repositories.")
- [Grant extensions access to OAuth tokens](extend-proc_configuring_trusted_extensions.md "Grant specific extensions access to OAuth authentication tokens in Microsoft Visual Studio Code by configuring the trustedExtensionAuthAccess field. Extensions that access services such as GitHub or Microsoft can then authenticate without manual intervention.")
- [Apply IDE settings to all workspaces](extend-proc_applying_editor_configurations.md "Apply a OpenShift ConfigMap to standardize the Code - OSS editor across all workspaces, giving every developer the same settings, recommended extensions, and product properties at startup.")
