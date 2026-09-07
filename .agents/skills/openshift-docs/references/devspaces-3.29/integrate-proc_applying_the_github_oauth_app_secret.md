> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/integrate-proc_applying_the_github_oauth_app_secret). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Connect OpenShift Dev Spaces to your GitHub OAuth application

Connect OpenShift Dev Spaces to your GitHub OAuth application so that developers can access GitHub repositories from workspaces without re-entering credentials. .Prerequisites

## About this task

- You have configured the GitHub OAuth App.
- You have the following values, which were generated when configuring the GitHub OAuth App:
  - **GitHub OAuth Client ID**
  - **GitHub OAuth Client Secret**

<!-- -->

- You have an active `oc` session with administrative permissions to the OpenShift cluster. See [Getting started with the CLI](https://docs.openshift.com/container-platform/4.22/cli_reference/openshift_cli/getting-started-cli.html).

## Procedure

1.  Prepare the Secret:

    ``` yaml
    kind: Secret
    apiVersion: v1
    metadata:
      name: github-oauth-config
      namespace: openshift-devspaces
      labels:
        app.kubernetes.io/part-of: che.eclipse.org
        app.kubernetes.io/component: oauth-scm-configuration
      annotations:
        che.eclipse.org/oauth-scm-server: github
        che.eclipse.org/scm-server-endpoint: <github_server_url>
        che.eclipse.org/scm-github-disable-subdomain-isolation: 'false'
    type: Opaque
    stringData:
      id: <GitHub_OAuth_Client_ID>
      secret: <GitHub_OAuth_Client_Secret>
    ```

    where:

    namespace  
    The OpenShift Dev Spaces namespace. The default is `openshift-devspaces`.

    che.eclipse.org/scm-server-endpoint  
    This depends on the GitHub product your organization is using. When hosting repositories on GitHub.com or GitHub Enterprise Cloud, omit this line or enter the default [`https://github.com`](https://github.com). When hosting repositories on GitHub Enterprise Server, enter the GitHub Enterprise Server URL.

    che.eclipse.org/scm-github-disable-subdomain-isolation  
    If you are using GitHub Enterprise Server with a disabled [subdomain isolation](https://docs.github.com/en/enterprise-server/admin/configuration/hardening-security-for-your-enterprise/enabling-subdomain-isolation#about-subdomain-isolation) option, you must set the annotation to `true`. Otherwise, you can either omit the annotation or set it to `false`.

    id  
    The **GitHub OAuth Client ID**.

    secret  
    The **GitHub OAuth Client Secret**.

2.  Apply the Secret:

    ``` bash
    $ oc apply -f - <<EOF
    <Secret_prepared_in_the_previous_step>
    EOF
    ```

3.  Optional: To configure OAuth 2.0 for another GitHub provider, repeat the previous steps and create a second GitHub OAuth Secret with a different name.

## Results

- Verify that the output displays `secret/github-oauth-config created`.

**Related tasks**  

- [Create a GitHub OAuth application for OpenShift Dev Spaces](integrate-proc_setting_up_the_github_oauth_app.md "Create an OAuth 2.0 application on GitHub so that OpenShift Dev Spaces can authenticate your developers and provide credential-free access to GitHub repositories. .Prerequisites")
- [Create a GitLab OAuth application for OpenShift Dev Spaces](integrate-proc_setting_up_the_gitlab_authorized_application.md "Create an OAuth 2.0 authorized application on your GitLab instance so that OpenShift Dev Spaces can authenticate your developers and provide credential-free access to GitLab repositories. .Prerequisites")
- [Connect OpenShift Dev Spaces to your GitLab OAuth application](integrate-proc_applying_the_gitlab_authorized_application_secret.md "Connect OpenShift Dev Spaces to your GitLab OAuth application so that developers can access GitLab repositories from workspaces without re-entering credentials. .Prerequisites")
