> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/integrate-proc_setting_up_the_github_app). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Create a GitHub App for OpenShift Dev Spaces

Create a GitHub App as an alternative to an OAuth App so that OpenShift Dev Spaces can authenticate your developers with finer-grained repository permissions. .Prerequisites

## About this task

- You are logged in to GitHub.

## Procedure

1.  Register a GitHub App. See [Registering a GitHub App](https://docs.github.com/en/apps/creating-github-apps/registering-a-github-app/registering-a-github-app#registering-a-github-app).
2.  Enter the following values:
    1.  **GitHub App name**: *`<application_name>`*
    2.  **Homepage URL**: `https://`*`<openshift_dev_spaces_fqdn>`*`/`
    3.  **Callback URL**: `https://`*`<openshift_dev_spaces_fqdn>`*`/api/oauth/callback`
    4.  Deselect the **Active** check box in the **Webhook** section.
    5.  Under **Permissions & events**, set the **Contents** repository permission to **Read and Write**.
3.  Click **Create GitHub App**.
4.  Click **Generate a new client secret**.
5.  Copy and save the **GitHub App Client Secret** for use when applying the GitHub App Secret.
6.  Copy and save the **GitHub App Client ID** for use when applying the GitHub App Secret.
7.  Install the GitHub App. See [Installing your own GitHub App](https://docs.github.com/en/apps/using-github-apps/installing-your-own-github-app#installing-your-own-github-app).

## Results

- Verify that the GitHub App appears in your GitHub account under **Settings** **Developer settings** **GitHub Apps**.

**Related tasks**  

- [Connect OpenShift Dev Spaces to your GitHub OAuth application](integrate-proc_applying_the_github_oauth_app_secret.md "Connect OpenShift Dev Spaces to your GitHub OAuth application so that developers can access GitHub repositories from workspaces without re-entering credentials. .Prerequisites")

**Related information**  

- [GitHub Docs: Registering a GitHub App](https://docs.github.com/en/apps/creating-github-apps/registering-a-github-app/registering-a-github-app)
