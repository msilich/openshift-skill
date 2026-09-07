> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/develop-assembly_optional_parameters_for_urls). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Share preconfigured workspace links with your team

Share preconfigured workspace links with your team by appending optional parameters to the URL that starts a new workspace so you can control the IDE, storage, resource limits, and devfile configuration without editing files.

When you open a Git repository URL in OpenShift Dev Spaces, you can add query parameters to control the IDE, workspace storage, resource limits, devfile path, and other workspace settings.

- **[URL parameter concatenation](develop-ref_url_parameter_concatenation.md)**  
  Combine multiple URL parameters when starting an OpenShift Dev Spaces workspace by concatenating them with `&`. This enables you to customize the editor, storage type, devfile, and other workspace settings in a single URL.
- **[URL parameter for the IDE](develop-ref_url_parameter_for_the_ide.md)**  
  The `che-editor=` URL parameter specifies a supported IDE when starting a workspace, allowing you to override the default editor or the `che-editor.yaml` file without modifying the Git repository.
- **[URL parameter for the IDE image](develop-ref_url_parameter_for_the_ide_image.md)**  
  The `editor-image` URL parameter sets a custom IDE image for the workspace, allowing you to test prerelease IDE builds or use a customized IDE container.
- **[URL parameter for starting duplicate workspaces](develop-ref_url_parameter_for_starting_duplicate_workspaces.md)**  
  Use the `new` URL parameter to create multiple workspaces from the same devfile and Git repository, which is useful when you need parallel environments for testing or comparing changes.
- **[URL parameter for the existing workspace name](develop-ref_url_parameter_for_the_existing_workspace_name.md)**  
  Use the `existing` URL parameter to reopen an existing workspace instead of creating a new one, which avoids duplicate workspaces when revisiting a workspace URL.
- **[URL parameter for the devfile file name](develop-ref_url_parameter_for_the_devfile_file_name.md)**  
  Use the `df` URL parameter to specify a custom devfile file name when the repository uses a name other than the default `.devfile.yaml` or `devfile.yaml`.
- **[URL parameter for the devfile file path](develop-ref_url_parameter_for_the_devfile_file_path.md)**  
  Use the `devfilePath` URL parameter to specify a custom path to the devfile when it is not in the root directory of the linked Git repository.
- **[URL parameter for the workspace storage](develop-ref_url_parameter_for_the_workspace_storage.md)**  
  Use the `storageType` URL parameter to override the default storage strategy for a new workspace, choosing between persistent and ephemeral storage based on your data retention needs.
- **[URL parameter for additional remotes](develop-ref_url_parameter_for_additional_remotes.md)**  
  Configure additional Git remotes when starting a workspace by specifying extra repository URLs as parameters, enabling work with multiple upstream sources in a single workspace.
- **[URL parameter for a container image](develop-ref_url_parameter_for_a_container_image.md)**  
  The `image` URL parameter specifies a custom container image for the workspace, allowing you to use a different base image than the one defined in the devfile or the default Universal Developer Image.
- **[URL parameter for a memory limit](develop-ref_url_parameter_for_a_memory_limit.md)**  
  The `memoryLimit` URL parameter specifies or overrides the container memory limit when starting a new workspace from a devfile URL. Use this parameter to allocate enough memory for resource-intensive development tasks.
- **[URL parameter for a CPU limit](develop-ref_url_parameter_for_a_cpu_limit.md)**  
  The `cpuLimit` URL parameter specifies or overrides the container CPU limit when starting a new workspace from a devfile URL. Use this parameter to allocate enough CPU for resource-intensive development tasks.
- **[URL parameter for the AI provider](develop-ref_url_parameter_for_the_ai_provider.md)**  
  Use the `ai-provider=` URL parameter to specify one or more AI providers in a workspace start URL. The workspace launches with the selected AI tool binaries injected and ready to use, without requiring manual selection on the dashboard.
- **[Start a cloud development environment from a raw devfile URL](develop-proc_starting_a_workspace_from_a_raw_devfile_url.md)**  
  Start a cloud development environment from a devfile hosted outside your Git repository so that you can share a standard development environment across teams or test devfile changes before committing them.
- **[Prevent workspace idling for long-running commands](develop-proc_preventing_workspace_idling_for_long_running_commands.md)**  
  Prevent a workspace from stopping while long-running CLI tools such as `helm`, `odo`, or `sleep` are active, so that unattended tasks can complete without interruption.
