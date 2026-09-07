> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/integrate-proc_setting_up_the_gitlab_authorized_application). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Create a GitLab OAuth application for OpenShift Dev Spaces

Create an OAuth 2.0 authorized application on your GitLab instance so that OpenShift Dev Spaces can authenticate your developers and provide credential-free access to GitLab repositories. .Prerequisites

## About this task

- You are logged in to GitLab.

## Procedure

1.  Click your avatar and go to Edit profile<span class="abbr" title="and then"> \> </span>Applications.
2.  Enter **OpenShift Dev Spaces** as the **Name**.
3.  Enter `https://`*`<openshift_dev_spaces_fqdn>`*`/api/oauth/callback` as the **Redirect URI**.
4.  Check the **Confidential** and **Expire access tokens** checkboxes.
5.  Under **Scopes**, check the `api`, `write_repository`, and `openid` checkboxes.
6.  Click **Save application**.
7.  Copy and save the **GitLab Application ID** for use when applying the GitLab-authorized application Secret.
8.  Copy and save the **GitLab Client Secret** for use when applying the GitLab-authorized application Secret.

**Related information**  

- [GitLab Docs: Authorized applications](https://docs.gitlab.com/ee/integration/oauth_provider.html#authorized-applications)
