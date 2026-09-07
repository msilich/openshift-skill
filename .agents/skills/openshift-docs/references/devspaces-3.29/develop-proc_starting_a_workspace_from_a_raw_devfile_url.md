> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/develop-proc_starting_a_workspace_from_a_raw_devfile_url). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Start a cloud development environment from a raw devfile URL

Start a cloud development environment from a devfile hosted outside your Git repository so that you can share a standard development environment across teams or test devfile changes before committing them.

## Before you begin

- You have a running instance of OpenShift Dev Spaces.
- You know the Fully Qualified Domain Name (FQDN) URL of your organization’s OpenShift Dev Spaces instance: `https://`*`<openshift_dev_spaces_fqdn>`*.
- You have a devfile that includes project information to clone the Git repository. See <https://devfile.io/docs/2.2.0/adding-projects>.

## About this task

Tip

You can also use the **Git Repo URL** field on the **Create Workspace** page of your OpenShift Dev Spaces dashboard to enter the URL of a devfile to start a new cloud development environment.

## Procedure

1.  Optional: Open the OpenShift Dev Spaces dashboard to authenticate to your organization’s instance of OpenShift Dev Spaces.

2.  Enter the devfile URL in your browser to start a new cloud development environment.

    For a public repository:

    ``` plaintext
    https://<openshift_dev_spaces_fqdn>#<devfile_url>
    ```

    For a private repository, include your personal access token in the URL:

    ``` plaintext
    https://<openshift_dev_spaces_fqdn>#https://<token>@<host>/<path_to_devfile>
    ```

    where:

    ` `*`<token>`*` `  
    Your personal access token that you generated on the Git provider’s website. This method works for GitHub, GitLab, Bitbucket, Microsoft Azure, and other providers that support Personal Access Token.

    Important

    Automated Git credential injection does not work with token-embedded URLs. To configure Git credentials separately, see [Access private repositories with a personal access token](get_started-proc_using_a_git_provider_access_token.md).

    To append optional parameters, add `?`*`<optional_parameters>`* to the URL. See [Optional parameters for workspace URLs](develop-assembly_optional_parameters_for_urls.md "Share preconfigured workspace links with your team by appending optional parameters to the URL that starts a new workspace so you can control the IDE, storage, resource limits, and devfile configuration without editing files.") for supported parameters.

    For example:

    - Public repository: `https://`*`<openshift_dev_spaces_fqdn>`*`#https://raw.githubusercontent.com/che-samples/cpp-hello-world/main/devfile.yaml`
    - Private repository: `https://`*`<openshift_dev_spaces_fqdn>`*`#https://`*`<token>`*`@raw.githubusercontent.com/che-samples/cpp-hello-world/main/devfile.yaml`

## Results

- After you enter the URL, the starting page appears in the browser tab.
- When the cloud development environment is ready, the IDE loads automatically.
- The cloud development environment has a unique URL: `https://`*`<openshift_dev_spaces_fqdn>`*`/`*`<user_name>`*`/`*`<unique_url>`*.

**Related concepts**  

- [Optional parameters for workspace URLs](develop-assembly_optional_parameters_for_urls.md "Share preconfigured workspace links with your team by appending optional parameters to the URL that starts a new workspace so you can control the IDE, storage, resource limits, and devfile configuration without editing files.")

**Related tasks**  

- [Mount Git configuration](develop-proc_mounting_git_configuration.md "Mount your Git configuration into workspaces to set your Git identity and preferences.")

**Related information**  

- [Manage your Cloud Development Environments](get_started-ref_basic_actions_on_a_workspace.md)
- [Access private repositories with a personal access token](get_started-proc_using_a_git_provider_access_token.md)
- [Configuring DevWorkspaces to use SSH keys for Git operations](https://github.com/devfile/devworkspace-operator/blob/main/docs/additional-configuration.adoc#configuring-devworkspaces-to-use-ssh-keys-for-git-operations)
