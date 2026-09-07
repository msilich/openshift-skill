> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/integrate-proc_setting_up_oauth_2_application_link_on_the_bitbucket_server). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Create a Bitbucket Server OAuth 2.0 application for OpenShift Dev Spaces

Create an OAuth 2.0 application link on your Bitbucket Server so that OpenShift Dev Spaces can authenticate your developers and provide credential-free access to Bitbucket Server repositories. .Prerequisites

## About this task

- You are logged in to the Bitbucket Server.

## Procedure

1.  Go to **Administration \> Applications \> Application links**.
2.  Select **Create link**.
3.  Select **External application** and **Incoming**.
4.  Enter `https://`*`<openshift_dev_spaces_fqdn>`*`/api/oauth/callback` to the **Redirect URL** field.
5.  Select the **Admin - Write** checkbox in **Application permissions**.
6.  Click **Save**.
7.  Copy and save the **Client ID** for use when applying the Bitbucket application link Secret.
8.  Copy and save the **Client secret** for use when applying the Bitbucket application link Secret.

**Related information**  

- [Atlassian Documentation: Configure an incoming link](https://confluence.atlassian.com/bitbucketserver0720/configure-an-incoming-link-1116282013.html)
