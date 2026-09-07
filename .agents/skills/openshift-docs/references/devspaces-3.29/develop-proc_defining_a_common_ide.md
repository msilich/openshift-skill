> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/develop-proc_defining_a_common_ide). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Define a common IDE

Define a common IDE for all workspaces in a Git repository by using a `che-editor.yaml` file so that all team members and new contributors use the most suitable IDE for the project. You can also use this file to override the OpenShift Dev Spaces instance default IDE for a particular Git repository.

## Before you begin

- You have a project source code repository hosted on a Git provider.

## About this task

To use an IDE other than the default Microsoft Visual Studio Code - Open Source for most or all workspaces in your organization, an administrator can set `.spec.devEnvironments.defaultEditor` in the `CheCluster` Custom Resource to apply the change at the instance level.

## Procedure

In the remote Git repository of your project source code, create a `/.che/che-editor.yaml` file with lines that specify the relevant parameter. For example:

``` yaml
id: che-incubator/che-code/latest
```

## Results

1.  [Start a new workspace with a clone of the Git repository](get_started-proc_starting_a_workspace_from_a_git_repository_url.md).
2.  Verify that the specified IDE loads in the browser tab of the started workspace.

**Related concepts**  

- [Share preconfigured workspace links with your team](develop-assembly_optional_parameters_for_urls.md "Share preconfigured workspace links with your team by appending optional parameters to the URL that starts a new workspace so you can control the IDE, storage, resource limits, and devfile configuration without editing files.")

**Related reference**  

- [Parameters for che-editor.yaml](develop-ref_parameters_for_che_editor_yaml.md "Configure the che-editor.yaml file to select and customize the IDE for your workspace, including the editor type, version, and container image.")
