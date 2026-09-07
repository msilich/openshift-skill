> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/integrate-proc_applying_oauth_consumer_secret_for_the_bitbucket_cloud). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Connect OpenShift Dev Spaces to your Bitbucket Cloud OAuth consumer

Connect OpenShift Dev Spaces to your Bitbucket Cloud OAuth consumer so that developers can access Bitbucket Cloud repositories from workspaces without re-entering credentials. .Prerequisites

## About this task

- You have configured the OAuth consumer in the Bitbucket Cloud.
- You have the following values, which were generated when configuring the Bitbucket OAuth consumer:
  - Bitbucket OAuth consumer Key
  - Bitbucket OAuth consumer Secret

<!-- -->

- You have an active `oc` session with administrative permissions to the OpenShift cluster. See [Getting started with the CLI](https://docs.openshift.com/container-platform/4.22/cli_reference/openshift_cli/getting-started-cli.html).

## Procedure

1.  Prepare the Secret:

    ``` yaml
    kind: Secret
    apiVersion: v1
    metadata:
      name: bitbucket-oauth-config
      namespace: openshift-devspaces
      labels:
        app.kubernetes.io/part-of: che.eclipse.org
        app.kubernetes.io/component: oauth-scm-configuration
      annotations:
        che.eclipse.org/oauth-scm-server: bitbucket
    type: Opaque
    stringData:
      id: <Bitbucket_Oauth_Consumer_Key>
      secret: <Bitbucket_Oauth_Consumer_Secret>
    ```

    where:

    namespace  
    The OpenShift Dev Spaces namespace. The default is `openshift-devspaces`.

    id  
    The **Bitbucket OAuth consumer Key**.

    secret  
    The **Bitbucket OAuth consumer Secret**.

2.  Apply the Secret:

    ``` bash
    $ oc apply -f - <<EOF
    <Secret_prepared_in_the_previous_step>
    EOF
    ```

## Results

- Verify that the output displays `secret/bitbucket-oauth-config created`.

**Related tasks**  

- [Create a Bitbucket Cloud OAuth consumer for OpenShift Dev Spaces](integrate-proc_setting_up_oauth_consumer_in_the_bitbucket_cloud.md "Create an OAuth consumer on Bitbucket Cloud so that OpenShift Dev Spaces can authenticate your developers and provide credential-free access to Bitbucket Cloud repositories. .Prerequisites")
- [Create a GitHub OAuth application for OpenShift Dev Spaces](integrate-proc_setting_up_the_github_oauth_app.md "Create an OAuth 2.0 application on GitHub so that OpenShift Dev Spaces can authenticate your developers and provide credential-free access to GitHub repositories. .Prerequisites")
- [Create a GitLab OAuth application for OpenShift Dev Spaces](integrate-proc_setting_up_the_gitlab_authorized_application.md "Create an OAuth 2.0 authorized application on your GitLab instance so that OpenShift Dev Spaces can authenticate your developers and provide credential-free access to GitLab repositories. .Prerequisites")
