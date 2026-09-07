> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/integrate-proc_setting_up_oauth_consumer_in_the_bitbucket_cloud). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Create a Bitbucket Cloud OAuth consumer for OpenShift Dev Spaces

Create an OAuth consumer on Bitbucket Cloud so that OpenShift Dev Spaces can authenticate your developers and provide credential-free access to Bitbucket Cloud repositories. .Prerequisites

## About this task

- You are logged in to the Bitbucket Cloud.

## Procedure

1.  Click your avatar and go to the **All workspaces** page.
2.  Select a workspace and click it.
3.  Go to Settings<span class="abbr" title="and then"> \> </span>OAuth consumers<span class="abbr" title="and then"> \> </span>Add consumer.
4.  Enter **OpenShift Dev Spaces** as the **Name**.
5.  Enter `https://`*`<openshift_dev_spaces_fqdn>`*`/api/oauth/callback` as the **Callback URL**.
6.  Under **Permissions**, check all of the **Account** and **Repositories** checkboxes, and click **Save**.
7.  Expand the added consumer and then copy and save the **Key** value for use when applying the Bitbucket OAuth consumer Secret.
8.  Copy and save the **Secret** value for use when applying the Bitbucket OAuth consumer Secret.

**Related information**  

- [Bitbucket Docs: Use OAuth on Bitbucket Cloud](https://support.atlassian.com/bitbucket-cloud/docs/use-oauth-on-bitbucket-cloud)
