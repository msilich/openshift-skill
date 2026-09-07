> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/get_started-proc_starting_a_workspace_from_a_git_repository_url). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Open your project in a cloud development environment

Open your team’s Git repository in a cloud development environment so that you can start coding without installing tools, cloning repositories, or configuring your local environment. OpenShift Dev Spaces handles all of this automatically.

## Before you begin

- You have a running instance of OpenShift Dev Spaces.
- You know the Fully Qualified Domain Name (FQDN) URL of your organization’s OpenShift Dev Spaces instance: `https://`*`<openshift_dev_spaces_fqdn>`*.
- Optional: You have [authentication to the Git server](get_started-con_authenticating_to_a_git_server_from_a_workspace.md "When you clone a private repository or push code from a cloud development environment, OpenShift Dev Spaces needs credentials to access your Git provider. Authentication can be configured at the platform level by your administrator or individually with a personal access token.") configured.
- Optional: You have a `devfile.yaml` or `.devfile.yaml` file in the root directory of the Git repository. Without a devfile, the cloud development environment starts with the Universal Developer Image and the default IDE.
- For private repositories: you have configured a personal access token or accepted the SCM authentication page to access the repository content. See [Access private repositories with a personal access token](get_started-proc_using_a_git_provider_access_token.md "Set up a personal access token so that you can clone private repositories and push code from your cloud development environment when your administrator has not configured OAuth for your Git provider.").
- For Git+SSH URLs: you have configured an SSH key for Git operations. See [Configuring DevWorkspaces to use SSH keys for Git operations](https://github.com/devfile/devworkspace-operator/blob/main/docs/additional-configuration.adoc#configuring-devworkspaces-to-use-ssh-keys-for-git-operations).

## About this task

Tip You can also use the **Git Repository URL** field on the **Create Workspace** page of your OpenShift Dev Spaces dashboard to enter the URL of a Git repository to start a new cloud development environment.

## Procedure

1.  Optional: Open the OpenShift Dev Spaces dashboard to authenticate to your organization’s instance of OpenShift Dev Spaces.

2.  Enter the URL in your browser or in the **Git Repository URL** field on the **Create Workspace** page to start a new cloud development environment:

    ``` plaintext
    https://<openshift_dev_spaces_fqdn>#<git_repository_url>
    ```

    To append optional parameters, add `?`*`<optional_parameters>`* to the URL. See [Optional parameters for workspace URLs](develop-assembly_optional_parameters_for_urls.md) for supported parameters.

    For example:

    - `https://`*`<openshift_dev_spaces_fqdn>`*`#https://github.com/che-samples/cpp-hello-world`

    - `https://`*`<openshift_dev_spaces_fqdn>`*`#git@github.com:che-samples/cpp-hello-world.git`

      URL syntax per Git provider:

      <span id="proc_starting-a-workspace-from-a-git-repository-url_devspaces__entry__1"></span>

      | URL pattern |
      |----|
      | Default branch: `https://`*`<openshift_dev_spaces_fqdn>`*`#https://`*`<github_host>`*`/`*`<user_or_org>`*`/`*`<repository>`* |
      | Specified branch: `https://`*`<openshift_dev_spaces_fqdn>`*`#https://`*`<github_host>`*`/`*`<user_or_org>`*`/`*`<repository>`*`/tree/`*`<branch_name>`* |
      | Pull request branch: `https://`*`<openshift_dev_spaces_fqdn>`*`#https://`*`<github_host>`*`/`*`<user_or_org>`*`/`*`<repository>`*`/pull/`*`<pull_request_id>`* |
      | Git+SSH: `https://`*`<openshift_dev_spaces_fqdn>`*`#git@`*`<github_host>`*`:`*`<user_or_org>`*`/`*`<repository>`*`.git` |

      Table 1. GitHub

      For GitHub, you can also use a URL of a directory containing a devfile, or a direct URL to the devfile. The devfile name must be `devfile.yaml` or `.devfile.yaml`. Other Git providers do not support this feature.

      <span id="proc_starting-a-workspace-from-a-git-repository-url_devspaces__entry__6"></span>

      | URL pattern |
      |----|
      | Default branch: `https://`*`<openshift_dev_spaces_fqdn>`*`#https://`*`<gitlab_host>`*`/`*`<user_or_org>`*`/`*`<repository>`* |
      | Specified branch: `https://`*`<openshift_dev_spaces_fqdn>`*`#https://`*`<gitlab_host>`*`/`*`<user_or_org>`*`/`*`<repository>`*`/-/tree/`*`<branch_name>`* |
      | Git+SSH: `https://`*`<openshift_dev_spaces_fqdn>`*`#git@`*`<gitlab_host>`*`:`*`<user_or_org>`*`/`*`<repository>`*`.git` |

      Table 2. GitLab

      <span id="proc_starting-a-workspace-from-a-git-repository-url_devspaces__entry__10"></span>

      | URL pattern |
      |----|
      | Default branch: `https://`*`<openshift_dev_spaces_fqdn>`*`#https://`*`<bb_host>`*`/scm/`*`<project-key>`*`/`*`<repository>`*`.git` |
      | Default branch (user profile repository): `https://`*`<openshift_dev_spaces_fqdn>`*`#https://`*`<bb_host>`*`/users/`*`<user_slug>`*`/repos/`*`<repository>`*`/` |
      | Specified branch: `https://`*`<openshift_dev_spaces_fqdn>`*`#https://`*`<bb_host>`*`/users/`*`<user-slug>`*`/repos/`*`<repository>`*`/browse?at=refs%2Fheads%2F`*`<branch-name>`* |
      | Git+SSH: `https://`*`<openshift_dev_spaces_fqdn>`*`#git@`*`<bb_host>`*`:`*`<user_slug>`*`/`*`<repository>`*`.git` |

      Table 3. Bitbucket Server

      <span id="proc_starting-a-workspace-from-a-git-repository-url_devspaces__entry__15"></span>

      | URL pattern |
      |----|
      | Default branch: `https://`*`<openshift_dev_spaces_fqdn>`*`#https://`*`<organization>`*`@dev.azure.com/`*`<organization>`*`/`*`<project>`*`/_git/`*`<repository>`* |
      | Specified branch: `https://`*`<openshift_dev_spaces_fqdn>`*`#https://`*`<organization>`*`@dev.azure.com/`*`<organization>`*`/`*`<project>`*`/_git/`*`<repository>`*`?version=GB`*`<branch>`* |
      | Git+SSH: `https://`*`<openshift_dev_spaces_fqdn>`*`#git@ssh.dev.azure.com:v3/`*`<organization>`*`/`*`<project>`*`/`*`<repository>`* |

      Table 4. Microsoft Azure DevOps

## Results

- After you enter the URL to start a new cloud development environment in a browser tab, the starting page appears.
- When the new cloud development environment is ready, the IDE loads in the browser tab.
- A clone of the Git repository is present in the filesystem of the new cloud development environment.
- The cloud development environment has a unique URL: `https://`*`<openshift_dev_spaces_fqdn>`*`/`*`<user_name>`*`/`*`<unique_url>`*.

**Related tasks**  

- [Access private repositories with a personal access token](get_started-proc_using_a_git_provider_access_token.md "Set up a personal access token so that you can clone private repositories and push code from your cloud development environment when your administrator has not configured OAuth for your Git provider.")

**Related reference**  

- [Manage your cloud development environments](get_started-ref_basic_actions_on_a_workspace.md "Stop, restart, and delete cloud development environments from the OpenShift Dev Spaces dashboard to control resource usage and keep your environment organized. Access the Workspaces page at https://<openshift_dev_spaces_fqdn>/dashboard/#/workspaces.")

**Related information**  

- [Optional parameters for workspace URLs](develop-assembly_optional_parameters_for_urls.md)
- [Mount Git configuration](develop-proc_mounting_git_configuration.md)
- [Configuring DevWorkspaces to use SSH keys for Git operations](https://github.com/devfile/devworkspace-operator/blob/main/docs/additional-configuration.adoc#configuring-devworkspaces-to-use-ssh-keys-for-git-operations)
