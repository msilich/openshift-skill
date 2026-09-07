> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/integrate-proc_setting_up_the_github_oauth_app). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Create a GitHub OAuth application for OpenShift Dev Spaces

Create an OAuth 2.0 application on GitHub so that OpenShift Dev Spaces can authenticate your developers and provide credential-free access to GitHub repositories. .Prerequisites

## About this task

- You are logged in to GitHub.

## Procedure

1.  Go to [the GitHub OAuth application registration page](https://github.com/settings/applications/new).
2.  Enter the following values:
    1.  **Application name**: `<`*`application name`*`>`
    2.  **Homepage URL**: `https://`*`<openshift_dev_spaces_fqdn>`*`/`
    3.  **Authorization callback URL**: `https://`*`<openshift_dev_spaces_fqdn>`*`/api/oauth/callback`
3.  Click **Register application**.
4.  Click **Generate new client secret**.
5.  Copy and save the **GitHub OAuth Client ID** for use when applying the GitHub OAuth App Secret.
6.  Copy and save the **GitHub OAuth Client Secret** for use when applying the GitHub OAuth App Secret.

**Related information**  

- [GitHub Docs: Creating an OAuth App](https://docs.github.com/en/developers/apps/building-oauth-apps/creating-an-oauth-app)
