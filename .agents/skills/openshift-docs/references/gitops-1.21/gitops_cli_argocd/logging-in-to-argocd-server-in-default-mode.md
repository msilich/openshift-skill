<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

You can log in to the Argo CD server in the default mode using the GitOps `argocd` CLI and your Argo CD credentials to execute commands.

# Logging in to the Argo CD server

After you install and configure the GitOps `argocd` CLI, you must log in to the Argo CD server to execute commands in the default mode.

<div>

<div class="title">

Prerequisites

</div>

- You must have the GitOps `argocd` CLI tool installed and configured.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Get the `admin` account password for the Argo CD server:

    ``` terminal
    $ ADMIN_PASSWD=$(oc get secret openshift-gitops-cluster -n openshift-gitops -o jsonpath='{.data.admin\.password}' | base64 -d)
    ```

2.  Get the Argo CD server URL:

    ``` terminal
    $ SERVER_URL=$(oc get routes openshift-gitops-server -n openshift-gitops -o jsonpath='{.status.ingress[0].host}')
    ```

3.  Log in to the Argo CD server by using the `admin` account password and enclosing it in single quotes:

    > [!IMPORTANT]
    > Enclosing the password in single quotes ensures that special characters, such as `$`, are not misinterpreted by the shell. Always use single quotes to enclose the literal value of the password.

    ``` terminal
    $ argocd login --username admin --password ${ADMIN_PASSWD} ${SERVER_URL}
    ```

    **Example:**

    ``` terminal
    $ argocd login --username admin --password '<password>' openshift-gitops.openshift-gitops.apps-crc.testing
    ```

    After a successful login, the session context will be displayed as follows:

    **Example output:**

    ``` terminal
    'admin:login' logged in successfully
    Context '<server_url>' updated
    ```

    > [!IMPORTANT]
    > If the login session times out, you can use the `relogin` command to log in again. When done using the `argocd` commands, you can log out using the `logout` command.

</div>

# Additional resources

- [Installing the GitOps CLI](../installing_gitops/installing-argocd-gitops-cli.md#installing-argocd-gitops-cli)

- [Configuring the GitOps CLI](configuring-argocd-gitops-cli.md#configuring-argocd-gitops-cli)

- [Basic GitOps argocd commands](argocd-gitops-cli-reference.md#argocd-gitops-cli-reference)
