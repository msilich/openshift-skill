> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/integrate-assembly_connecting_git_providers_with_oauth). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Connect Git providers with OAuth

Connect OpenShift Dev Spaces to your organization’s Git providers with OAuth so that developers can clone repositories and push code from workspaces without manually configuring credentials.

For each provider, you complete two steps: create an OAuth application on the provider’s website, then apply the credentials as a OpenShift Secret on your OpenShift Dev Spaces cluster. Configure only the providers your team uses:

- **GitHub**: OAuth App or GitHub App (finer-grained permissions)
- **GitLab**: Authorized application (OAuth 2.0)
- **Bitbucket Server**: Application link (OAuth 2.0 or OAuth 1.0)
- **Bitbucket Cloud**: OAuth consumer
- **Microsoft Azure DevOps**: Microsoft Entra ID application

Note

Microsoft Entra ID replaces the deprecated Azure DevOps OAuth 2.0 application, which no longer accepts new registrations. If you have an existing Azure DevOps OAuth app, migrate to Microsoft Entra ID.

- **[Create a GitHub OAuth application for OpenShift Dev Spaces](integrate-proc_setting_up_the_github_oauth_app.md)**  
  Create an OAuth 2.0 application on GitHub so that OpenShift Dev Spaces can authenticate your developers and provide credential-free access to GitHub repositories. .Prerequisites
- **[Create a GitHub App for OpenShift Dev Spaces](integrate-proc_setting_up_the_github_app.md)**  
  Create a GitHub App as an alternative to an OAuth App so that OpenShift Dev Spaces can authenticate your developers with finer-grained repository permissions. .Prerequisites
- **[Connect OpenShift Dev Spaces to your GitHub OAuth application](integrate-proc_applying_the_github_oauth_app_secret.md)**  
  Connect OpenShift Dev Spaces to your GitHub OAuth application so that developers can access GitHub repositories from workspaces without re-entering credentials. .Prerequisites
- **[Create a GitLab OAuth application for OpenShift Dev Spaces](integrate-proc_setting_up_the_gitlab_authorized_application.md)**  
  Create an OAuth 2.0 authorized application on your GitLab instance so that OpenShift Dev Spaces can authenticate your developers and provide credential-free access to GitLab repositories. .Prerequisites
- **[Connect OpenShift Dev Spaces to your GitLab OAuth application](integrate-proc_applying_the_gitlab_authorized_application_secret.md)**  
  Connect OpenShift Dev Spaces to your GitLab OAuth application so that developers can access GitLab repositories from workspaces without re-entering credentials. .Prerequisites
- **[Create a Bitbucket Server OAuth 2.0 application for OpenShift Dev Spaces](integrate-proc_setting_up_oauth_2_application_link_on_the_bitbucket_server.md)**  
  Create an OAuth 2.0 application link on your Bitbucket Server so that OpenShift Dev Spaces can authenticate your developers and provide credential-free access to Bitbucket Server repositories. .Prerequisites
- **[Connect OpenShift Dev Spaces to your Bitbucket Server OAuth 2.0 application](integrate-proc_applying_oauth_2_application_link_secret_for_the_bitbucket_server.md)**  
  Connect OpenShift Dev Spaces to your Bitbucket Server OAuth 2.0 application so that developers can access Bitbucket Server repositories from workspaces without re-entering credentials. .Prerequisites
- **[Create a Bitbucket Cloud OAuth consumer for OpenShift Dev Spaces](integrate-proc_setting_up_oauth_consumer_in_the_bitbucket_cloud.md)**  
  Create an OAuth consumer on Bitbucket Cloud so that OpenShift Dev Spaces can authenticate your developers and provide credential-free access to Bitbucket Cloud repositories. .Prerequisites
- **[Connect OpenShift Dev Spaces to your Bitbucket Cloud OAuth consumer](integrate-proc_applying_oauth_consumer_secret_for_the_bitbucket_cloud.md)**  
  Connect OpenShift Dev Spaces to your Bitbucket Cloud OAuth consumer so that developers can access Bitbucket Cloud repositories from workspaces without re-entering credentials. .Prerequisites
- **[Create a Bitbucket Server OAuth 1.0 application for OpenShift Dev Spaces](integrate-proc_setting_up_application_link_on_the_bitbucket_server.md)**  
  Create an OAuth 1.0 application link on your Bitbucket Server so that OpenShift Dev Spaces can authenticate your developers and provide access to Bitbucket Server repositories. .Prerequisites
- **[Connect OpenShift Dev Spaces to your Bitbucket Server OAuth 1.0 application](integrate-proc_applying_application_link_secret_for_the_bitbucket_server.md)**  
  Connect OpenShift Dev Spaces to your Bitbucket Server OAuth 1.0 application so that developers can access Bitbucket Server repositories from workspaces without re-entering credentials. .Prerequisites
- **[Create a Microsoft Entra ID application for OpenShift Dev Spaces](integrate-proc_setting_up_the_microsoft_azure_devops_services_oauth_app.md)**  
  Create a Microsoft Entra ID OAuth application so that OpenShift Dev Spaces can authenticate your developers and provide credential-free access to Azure DevOps repositories. .Prerequisites
- **[Connect OpenShift Dev Spaces to your Microsoft Entra ID application](integrate-proc_applying_the_microsoft_azure_devops_services_oauth_app_secret.md)**  
  Connect OpenShift Dev Spaces to your Microsoft Entra ID application so that developers can access Azure DevOps repositories from workspaces without re-entering credentials. .Prerequisites
- **[Refresh an expired access token automatically](integrate-proc_forcing_refresh_of_personal_access_token.md)**  
  Refresh expired access tokens automatically on workspace startup so that developers do not encounter authentication failures caused by stale personal access tokens.

**Related information**  

- [Troubleshoot OAuth configuration errors](troubleshoot-ref_troubleshooting_oauth_configuration.md)
