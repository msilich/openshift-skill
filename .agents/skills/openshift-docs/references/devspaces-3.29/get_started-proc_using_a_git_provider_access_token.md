> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/get_started-proc_using_a_git_provider_access_token). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Access private repositories with a personal access token

Set up a personal access token so that you can clone private repositories and push code from your cloud development environment when your administrator has not configured OAuth for your Git provider.

## Before you begin

- You have a personal access token from your Git provider:
  - [GitHub Personal Access Token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token)

  - [GitLab Personal Access Token](https://docs.gitlab.com/ee/user/profile/personal_access_tokens.html)

  - [Bitbucket App Password](https://support.atlassian.com/bitbucket-cloud/docs/app-passwords/)

  - [Azure DevOps Personal Access Token](https://docs.microsoft.com/en-us/azure/devops/organizations/accounts/use-personal-access-tokens-to-authenticate) Important

    Personal access tokens are sensitive information. Treat them like passwords. If you are having trouble with authentication, verify the token locally before applying it as a Secret:

    ``` bash
    $ git clone https://<PAT>@github.com/username/repo.git
    ```

    Replace `<PAT>` with your personal access token, and `username/repo` with the appropriate repository path. If cloning succeeds, the token is valid and has the necessary permissions.

    For GitHub Enterprise Cloud, verify that the token is [authorized for use within your organization with SAML single sign-on](https://docs.github.com/en/enterprise-cloud@latest/authentication/authenticating-with-saml-single-sign-on/authorizing-a-personal-access-token-for-use-with-saml-single-sign-on).
- You have an active `oc` session with your project. See [Getting started with the CLI](https://docs.openshift.com/container-platform/4.22/cli_reference/openshift_cli/getting-started-cli.html).

## About this task

Mounting your access token as a Secret enables the OpenShift Dev Spaces Server to access the remote repository that is cloned during cloud development environment creation, including access to the repository’s `/.che` and `/.vscode` folders.

You can create and apply multiple access-token Secrets per Git provider. You must apply each Secret in your user project.

## Procedure

1.  Open `https://`*`<openshift_dev_spaces_fqdn>`*`/api/user/id` in a browser to get your OpenShift Dev Spaces user ID.

2.  Create a Kubernetes Secret with your access token:

    ``` yaml
    kind: Secret
    apiVersion: v1
    metadata:
      name: personal-access-token-<git_provider>
      labels:
        app.kubernetes.io/component: scm-personal-access-token
        app.kubernetes.io/part-of: che.eclipse.org
      annotations:
        che.eclipse.org/che-userid: <devspaces_user_id>
        che.eclipse.org/scm-personal-access-token-name: <git_provider_name>
        che.eclipse.org/scm-url: <git_provider_endpoint>
        che.eclipse.org/scm-organization: <git_provider_organization>
    type: Opaque
    stringData:
      token: <your_personal_access_token>
    ```

    where:

    che.eclipse.org/che-userid  
    Your OpenShift Dev Spaces user ID.

    che.eclipse.org/scm-personal-access-token-name  
    The Git provider name (`github`, `gitlab`, `bitbucket-server`, or `azure-devops`).

    che.eclipse.org/scm-url  
    The Git provider URL endpoint, for example [`https://github.com`](https://github.com) or [`https://gitlab.com`](https://gitlab.com).

    che.eclipse.org/scm-organization  
    Required only for Azure DevOps: your Git provider user organization, or collection if Azure DevOps Server is used.

    token  
    Your personal access token.

    Example for GitHub:

    ``` yaml
    kind: Secret
    apiVersion: v1
    metadata:
      name: personal-access-token-github
      labels:
        app.kubernetes.io/component: scm-personal-access-token
        app.kubernetes.io/part-of: che.eclipse.org
      annotations:
        che.eclipse.org/che-userid: 1a2b3c4d-5e6f-7g8h-9i0j-1k2l3m4n5o6p
        che.eclipse.org/scm-personal-access-token-name: github
        che.eclipse.org/scm-url: https://github.com
    type: Opaque
    stringData:
      token: ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
    ```

3.  Open `https://`*`<openshift_dev_spaces_fqdn>`*`/api/kubernetes/namespace` to get your OpenShift Dev Spaces user namespace as `name`.

4.  Apply the Secret to your OpenShift Dev Spaces user project:

    ``` bash
    $ oc apply -f personal-access-token.yaml -n <your_user_namespace>
    ```

    Important

    If you are using Azure DevOps Server, you must also modify the [cloud development environment gitconfig](develop-proc_mounting_git_configuration.md) with the following section:

    ``` plaintext
    extraheader = "Authorization: Basic <base64-encoded(:personal-access-token)>"
    ```

    To generate the key-value pair, use the following command:

    ``` bash
    echo -n "extraheader = \"Authorization: Basic "$(printf ":%s" <personal access token> | base64)\"
    ```

    The `extraheader` configuration is needed for remote git operations to Azure DevOps Server, for example `git clone`. This authorization method has a higher priority over the git credentials store, and as a result, remote operations to other Git providers will fail.

5.  Start or restart your cloud development environment.

## Results

1.  Open a terminal in your cloud development environment.

2.  Clone a private repository or push to a repository to verify authentication:

    ``` bash
    $ git clone https://github.com/<org>/<private-repo>.git
    ```

**Related concepts**  

- [How Git authentication works in cloud development environments](get_started-con_authenticating_to_a_git_server_from_a_workspace.md "When you clone a private repository or push code from a cloud development environment, OpenShift Dev Spaces needs credentials to access your Git provider. Authentication can be configured at the platform level by your administrator or individually with a personal access token.")

**Related information**  

- [Authorizing a personal access token for use with SAML single sign-on](https://docs.github.com/en/enterprise-cloud@latest/authentication/authenticating-with-saml-single-sign-on/authorizing-a-personal-access-token-for-use-with-saml-single-sign-on)
