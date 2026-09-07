> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/extend-proc_running_open_vsx_using_workspace). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Build the extension registry inside a workspace

Build an on-premises Open VSX extension registry by using predefined devfile tasks in a OpenShift Dev Spaces workspace. The workspace environment includes all necessary tools and commands defined in the `.devfile.yaml` file of the Open VSX repository.

## Before you begin

- You have cluster administrator permissions on the OpenShift cluster.
- You have a running OpenShift Dev Spaces instance.

## Procedure

1.  Start a workspace by using the [Eclipse Open VSX repository](https://github.com/eclipse-openvsx/openvsx).

2.  Log in to the cluster from the workspace terminal:

    ``` bash
    oc login --token=<token> --server=<api_server_url>
    ```

    Warning

    The [.devfile.yaml](https://github.com/eclipse-openvsx/openvsx/blob/master/.devfile.yaml) includes an `elasticsearch` component that does not support IBM Power (ppc64le) or IBM Z (s390x) architectures. To start the workspace on these architectures, remove the `elasticsearch` component from the devfile. Alternatively, use the [Deploy from a prebuilt image](extend-proc_deploy_open_vsx_with_prebuilt_image.md "Deploy a standalone Open VSX extension registry by using an existing container image. Use a private, on-premises registry to control which extensions are available in your OpenShift Dev Spaces workspaces without building from source.") procedure to deploy Open VSX without starting a workspace.

    Tip

    The environment, including all necessary commands, is defined in the `.devfile.yaml` file. The numbered task names (such as `2.1.`, `2.4.1.`) are labels defined in the devfile. Use these exact names to locate each task in the `Terminal` \> `Run Task…​` menu.

3.  Create a new project for Open VSX.

    Select `Terminal` \> `Run Task…​` \> `devfile` and run the `2.1. Create Namespace for OpenVSX` task. A new project named `openvsx` is created on the cluster.

4.  Deploy Open VSX with the OpenShift Dev Spaces pre-built image.

    Select `Terminal` \> `Run Task…​` \> `devfile` and run the `2.4.1. Deploy Custom OpenVSX` task. When the task prompts for the Open VSX server image, enter `registry.redhat.io/devspaces/openvsx-rhel9:3.29`.

    After the deployment completes, the `openvsx` project has two components: PostgreSQL database and Open VSX server. The Open VSX UI is accessible through an exposed route in the OpenShift cluster.

    Tip

    All deployment parameters are described in the `deploy/openshift/openvsx-deployment-no-es.yml` file. The template includes default values such as `OVSX_PAT_BASE64`.

5.  Add an Open VSX user with a PAT to the database.

    Select `Terminal` \> `Run Task…​` \> `devfile` and run the `2.5. Add OpenVSX user with PAT to the DB` task. The task prompts you for the Open VSX username and user PAT. Press Enter to use the default values.

    Important

    The user PAT must match the decoded value of `OVSX_PAT_BASE64` specified in the deployment file. If you update `OVSX_PAT_BASE64`, use the new decoded value as the user PAT.

6.  Configure OpenShift Dev Spaces to use the internal Open VSX registry.

    Select `Terminal` \> `Run Task…​` \> `devfile` and run the `2.6. Configure Che to use the internal OpenVSX registry` task. This task patches the `CheCluster` custom resource to use the deployed Open VSX registry URL.

7.  Publish a Visual Studio Code extension from a `.vsix` file.

    Select `Terminal` \> `Run Task…​` \> `devfile` and run the `2.8. Publish a VS Code Extension from a VSIX file` task. The task prompts you to provide the extension publisher name and the path to the `.vsix` file.

8.  Optional: Publish a predefined list of extensions.

    Update the `deploy/openshift/extensions.txt` file with the download URLs of each `.vsix` file, then select `Terminal` \> `Run Task…​` \> `devfile` and run the `2.9. Publish list of VS Code Extensions` task.

## Results

- Start any workspace and verify the published extensions are available in the Extensions view of the workspace IDE.
- Open the `internal` route in the `openvsx` project to verify the registry UI displays the published extensions.

**Related tasks**  

- [Restrict the extension registry to internal traffic](extend-proc_configure_internal_open_vsx_access.md "Restrict your Open VSX registry to internal cluster traffic by removing the public route and configuring OpenShift Dev Spaces to use the internal service URL. Internal routing keeps extension registry traffic within the cluster and avoids public exposure.")
- [Remove an extension through the registry API](extend-proc_deleting_extension_using_openvsx_admin_api.md "Remove an extension from your private Open VSX registry by calling the administrator API with an administrator user and a Personal Access Token (PAT).")
- [Deploy from a prebuilt image](extend-proc_deploy_open_vsx_with_prebuilt_image.md "Deploy a standalone Open VSX extension registry by using an existing container image. Use a private, on-premises registry to control which extensions are available in your OpenShift Dev Spaces workspaces without building from source.")
- [Build a custom extension registry from source](extend-proc_deploy_open_vsx_from_source.md "Build custom Open VSX server and CLI images from source and deploy them to your cluster. A source build gives you full control over the Open VSX version and allows custom modifications to the registry.")

**Related information**  

- [Eclipse Open VSX sources](https://github.com/eclipse-openvsx/openvsx/)
- [Open VSX devfile](https://github.com/eclipse-openvsx/openvsx/blob/master/.devfile.yaml)
