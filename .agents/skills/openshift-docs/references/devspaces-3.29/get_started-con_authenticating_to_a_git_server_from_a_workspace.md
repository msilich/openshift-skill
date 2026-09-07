> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/get_started-con_authenticating_to_a_git_server_from_a_workspace). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# How Git authentication works in cloud development environments

When you clone a private repository or push code from a cloud development environment, OpenShift Dev Spaces needs credentials to access your Git provider. Authentication can be configured at the platform level by your administrator or individually with a personal access token.

User authentication to a Git server from a cloud development environment is configured by the administrator or, in some cases, by the individual user:

- Your administrator configures an OAuth application on GitHub, GitLab, Bitbucket, or Microsoft Azure Repos for your Red Hat OpenShift Dev Spaces instance.
- Alternatively, individual users create their own Kubernetes Secrets for personal Git-provider access tokens or configure SSH keys.

**Related tasks**  

- [Using a Git-provider access token](get_started-proc_using_a_git_provider_access_token.md "Set up a personal access token so that you can clone private repositories and push code from your cloud development environment when your administrator has not configured OAuth for your Git provider.")

**Related information**  

- [Configuring DevWorkspaces to use SSH keys for Git operations](https://github.com/devfile/devworkspace-operator/blob/main/docs/additional-configuration.adoc#configuring-devworkspaces-to-use-ssh-keys-for-git-operations)
- [Connect Git providers with OAuth](integrate-assembly_connecting_git_providers_with_oauth.md)
