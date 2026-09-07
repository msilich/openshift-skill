> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/get_started-proc_configure_github_oauth_for_your_team). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Configure GitHub OAuth for your team

Configure a GitHub OAuth application so that developers can clone repositories and push code from OpenShift Dev Spaces workspaces without manually entering credentials. This procedure covers GitHub.com and GitHub Enterprise Cloud. For other providers, see the Additional resources.

## Before you begin

- You have an active `oc` session with administrative permissions to the OpenShift cluster. See [Getting started with the CLI](https://docs.openshift.com/container-platform/4.22/cli_reference/openshift_cli/getting-started-cli.html).
- You are logged in to GitHub with an account that has permission to create OAuth applications for your organization.

## Procedure

1.  Go to the [GitHub OAuth application registration page](https://github.com/settings/applications/new).

2.  Enter the following values:
    1.  **Application name**: `OpenShift Dev Spaces`
    2.  **Homepage URL**: `https://`*`<openshift_dev_spaces_fqdn>`*`/`
    3.  **Authorization callback URL**: `https://`*`<openshift_dev_spaces_fqdn>`*`/api/oauth/callback`

3.  Click **Register application**.

4.  Click **Generate new client secret**.

5.  Copy the **Client ID** and the **Client Secret**. You need both values in the next step.

6.  Prepare and apply the OpenShift Secret:

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
    type: Opaque
    stringData:
      id: <GitHub_OAuth_Client_ID>
      secret: <GitHub_OAuth_Client_Secret>
    ```

7.  Apply the Secret:

    ``` bash
    $ oc apply -f - <<EOF
    <Secret_prepared_in_the_previous_step>
    EOF
    ```

## Results

- The output displays `secret/github-oauth-config created`.
- A developer creates a new workspace from a private GitHub repository and is not prompted for credentials.

**Related information**  

- [Connect Git providers with OAuth for GitHub, GitLab, Bitbucket, and Azure DevOps](integrate-assembly_connecting_git_providers_with_oauth.md)
- [GitHub Docs: Creating an OAuth App](https://docs.github.com/en/developers/apps/building-oauth-apps/creating-an-oauth-app)
