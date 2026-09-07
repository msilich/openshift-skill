> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/integrate-proc_applying_the_gitlab_authorized_application_secret). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Connect OpenShift Dev Spaces to your GitLab OAuth application

Connect OpenShift Dev Spaces to your GitLab OAuth application so that developers can access GitLab repositories from workspaces without re-entering credentials. .Prerequisites

## About this task

- You have configured the GitLab authorized application.
- You have the following values, which were generated when configuring the GitLab authorized application:
  - **GitLab Application ID**
  - **GitLab Client Secret**

<!-- -->

- You have an active `oc` session with administrative permissions to the OpenShift cluster. See [Getting started with the CLI](https://docs.openshift.com/container-platform/4.22/cli_reference/openshift_cli/getting-started-cli.html).

## Procedure

1.  Prepare the Secret:

    ``` yaml
    kind: Secret
    apiVersion: v1
    metadata:
      name: gitlab-oauth-config
      namespace: openshift-devspaces
      labels:
        app.kubernetes.io/part-of: che.eclipse.org
        app.kubernetes.io/component: oauth-scm-configuration
      annotations:
        che.eclipse.org/oauth-scm-server: gitlab
        che.eclipse.org/scm-server-endpoint: <gitlab_server_url>
    type: Opaque
    stringData:
      id: <GitLab_Application_ID>
      secret: <GitLab_Client_Secret>
    ```

    where:

    namespace  
    The OpenShift Dev Spaces namespace. The default is `openshift-devspaces`.

    che.eclipse.org/scm-server-endpoint  
    The **GitLab server URL**. Use [`https://gitlab.com`](https://gitlab.com) for the `SAAS` version.

    id  
    The **GitLab Application ID**.

    secret  
    The **GitLab Client Secret**.

2.  Apply the Secret:

    ``` bash
    $ oc apply -f - <<EOF
    <Secret_prepared_in_the_previous_step>
    EOF
    ```

3.  Optional: To configure OAuth 2.0 for another GitLab provider, repeat the previous steps and create a second GitLab OAuth Secret with a different name.

## Results

- Verify that the output displays `secret/gitlab-oauth-config created`.

**Related tasks**  

- [Create a GitLab OAuth application for OpenShift Dev Spaces](integrate-proc_setting_up_the_gitlab_authorized_application.md "Create an OAuth 2.0 authorized application on your GitLab instance so that OpenShift Dev Spaces can authenticate your developers and provide credential-free access to GitLab repositories. .Prerequisites")
- [Create a GitHub OAuth application for OpenShift Dev Spaces](integrate-proc_setting_up_the_github_oauth_app.md "Create an OAuth 2.0 application on GitHub so that OpenShift Dev Spaces can authenticate your developers and provide credential-free access to GitHub repositories. .Prerequisites")
- [Connect OpenShift Dev Spaces to your GitHub OAuth application](integrate-proc_applying_the_github_oauth_app_secret.md "Connect OpenShift Dev Spaces to your GitHub OAuth application so that developers can access GitHub repositories from workspaces without re-entering credentials. .Prerequisites")
