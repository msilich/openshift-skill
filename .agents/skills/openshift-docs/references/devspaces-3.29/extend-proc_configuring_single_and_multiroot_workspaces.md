> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/extend-proc_configuring_single_and_multiroot_workspaces). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Work with multiple projects in one workspace

Work with multiple project folders in the same workspace by using the multi-root workspace feature. This is useful when you are working on several related projects at once, such as product documentation and product code repositories.

## Before you begin

- You have an active `oc` session with administrative permissions to the OpenShift cluster. See [Getting started with the CLI](https://docs.openshift.com/container-platform/4.22/cli_reference/openshift_cli/getting-started-cli.html).

## About this task

By default, workspaces open in multi-root mode. After a workspace starts, the `/projects/.code-workspace` workspace file is generated. The workspace file contains all the projects described in the devfile.

``` plaintext
{
	"folders": [
		{
			"name": "project-1",
			"path": "/projects/project-1"
		},
		{
			"name": "project-2",
			"path": "/projects/project-2"
		}
	]
}
```

If the workspace file already exists, it is updated and all missing projects are taken from the devfile. If you remove a project from the devfile, it remains in the workspace file.

You can change the default behavior and provide your own workspace file or switch to a single-root workspace.

## Procedure

1.  Add a workspace file with the name `.code-workspace` to the root of your repository. After workspace creation, the Visual Studio Code - Open Source ("Code - OSS") uses the workspace file as it is.

    ``` plaintext
    {
    	"folders": [
    		{
    			"name": "project-name",
    			"path": "."
    		}
    	]
    }
    ```

    Important

    Be careful when creating a workspace file. In case of errors, an empty Visual Studio Code - Open Source ("Code - OSS") opens instead. If you have several projects, the workspace file is taken from the first project. If the workspace file does not exist in the first project, a new one is created and placed in the `/projects` directory.

2.  Define the `VSCODE_DEFAULT_WORKSPACE` environment variable in your devfile with the path to an alternative workspace file.

    ``` yaml
       env:
         - name: VSCODE_DEFAULT_WORKSPACE
           value: "/projects/project-name/workspace-file"
    ```

3.  Define the `VSCODE_DEFAULT_WORKSPACE` environment variable and set it to `/` to open a workspace in single-root mode.

    ``` yaml
       env:
         - name: VSCODE_DEFAULT_WORKSPACE
           value: "/"
    ```

## Results

- Start or restart the workspace and verify that Code - OSS opens with the expected workspace mode (single-root or multi-root).

**Related tasks**  

- [Grant extensions access to OAuth tokens](extend-proc_configuring_trusted_extensions.md "Grant specific extensions access to OAuth authentication tokens in Microsoft Visual Studio Code by configuring the trustedExtensionAuthAccess field. Extensions that access services such as GitHub or Microsoft can then authenticate without manual intervention.")
- [Pre-install extensions in every workspace](extend-proc_configuring_default_extensions.md "Pre-install VS Code extensions in OpenShift Dev Spaces workspaces by configuring the DEFAULT_EXTENSIONS environment variable to provide a consistent set of editor extensions on workspace startup.")
- [Apply IDE settings to all workspaces](extend-proc_applying_editor_configurations.md "Apply a OpenShift ConfigMap to standardize the Code - OSS editor across all workspaces, giving every developer the same settings, recommended extensions, and product properties at startup.")

**Related information**  

- [What is a VS Code workspace](https://code.visualstudio.com/docs/editing/workspaces/workspaces)
