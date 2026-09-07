> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/integrate-proc_setting_up_application_link_on_the_bitbucket_server). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Create a Bitbucket Server OAuth 1.0 application for OpenShift Dev Spaces

Create an OAuth 1.0 application link on your Bitbucket Server so that OpenShift Dev Spaces can authenticate your developers and provide access to Bitbucket Server repositories. .Prerequisites

## About this task

- You are logged in to the Bitbucket Server.
- [`openssl`](https://www.openssl.org/) is installed in the operating system you are using.

## Procedure

1.  On a command line, run the commands to create the necessary files for the next steps and for use when applying the application link Secret:

    ``` bash
    $ openssl genrsa -out private.pem 2048 && \
    openssl pkcs8 -topk8 -inform pem -outform pem -nocrypt -in private.pem -out privatepkcs8.pem && \
    cat privatepkcs8.pem | sed 's/-----BEGIN PRIVATE KEY-----//g' | sed 's/-----END PRIVATE KEY-----//g' | tr -d '\n' > privatepkcs8-stripped.pem && \
    openssl rsa -in private.pem -pubout > public.pub && \
    cat public.pub | sed 's/-----BEGIN PUBLIC KEY-----//g' | sed 's/-----END PUBLIC KEY-----//g' | tr -d '\n' > public-stripped.pub && \
    openssl rand -base64 24 > bitbucket-consumer-key && \
    openssl rand -base64 24 > bitbucket-shared-secret
    ```

2.  Go to Administration<span class="abbr" title="and then"> \> </span>Application Links, enter `https://`*`<openshift_dev_spaces_fqdn>`*`/` into the URL field, and click **Create new link**.

3.  Under **The supplied Application URL has redirected once**, check the **Use this URL** checkbox and click **Continue**.

4.  Configure the application link with the following values:
    1.  Enter **OpenShift Dev Spaces** as the **Application Name**.
    2.  Select **Generic Application** as the **Application Type**.
    3.  Enter **OpenShift Dev Spaces** as the **Service Provider Name**.
    4.  Paste the content of the `bitbucket-consumer-key` file as the **Consumer key**.
    5.  Paste the content of the `bitbucket-shared-secret` file as the **Shared secret**.
    6.  Enter *`<bitbucket_server_url>`*`/plugins/servlet/oauth/request-token` as the **Request Token URL**.
    7.  Enter *`<bitbucket_server_url>`*`/plugins/servlet/oauth/access-token` as the **Access token URL**.
    8.  Enter *`<bitbucket_server_url>`*`/plugins/servlet/oauth/authorize` as the **Authorize URL**.
    9.  Check the **Create incoming link** checkbox and click **Continue**.

5.  Configure the incoming link with the following values:
    1.  Paste the content of the `bitbucket-consumer-key` file as the **Consumer Key**.
    2.  Enter **OpenShift Dev Spaces** as the **Consumer name**.
    3.  Paste the content of the `public-stripped.pub` file as the **Public Key** and click **Continue**.

**Related information**  

- [Atlassian Documentation: Link to other applications](https://confluence.atlassian.com/bitbucketserver/link-to-other-applications-1018764620.html)
