<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

With Argo CD, you can create your applications on an OpenShift Container Platform cluster by using the GitOps `argocd` CLI.

# Creating an application in the default mode by using the GitOps CLI

You can create applications in the default mode by using the GitOps `argocd` CLI.

<div>

<div class="title">

Prerequisites

</div>

- You have installed the Red Hat OpenShift GitOps Operator on your OpenShift Container Platform cluster.

- You have installed the OpenShift CLI (`oc`).

- You have installed the Red Hat OpenShift GitOps `argocd` CLI.

- You have logged in to an Argo CD instance.

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

3.  Log in to the Argo CD server by using the `admin` account password:

    > [!IMPORTANT]
    > Enclosing the password in single quotes ensures that special characters, such as `$`, are not misinterpreted by the shell. Always use single quotes to enclose the literal value of the password.

    ``` terminal
    $ argocd login --username admin --password ${ADMIN_PASSWD} ${SERVER_URL}
    ```

    **Example:**

    ``` terminal
    $ argocd login --username admin --password '<password>' openshift-gitops.openshift-gitops.apps-crc.testing
    ```

4.  Verify that you are able to run `argocd` commands in the default mode by listing all applications:

    ``` terminal
    $ argocd app list
    ```

    If the configuration is correct, then existing applications will be listed with the following header:

    **Sample output:**

    ``` terminal
    NAME CLUSTER NAMESPACE  PROJECT  STATUS  HEALTH   SYNCPOLICY  CONDITIONS  REPO PATH TARGET
    ```

5.  Create an application in the default mode:

    ``` terminal
    $ argocd app create app-spring-petclinic \
        --repo https://github.com/redhat-developer/openshift-gitops-getting-started.git \
        --path app \
        --revision main \
        --dest-server  https://kubernetes.default.svc \
        --dest-namespace spring-petclinic \
        --directory-recurse \
        --sync-policy automated \
        --self-heal \
        --sync-option Prune=true \
        --sync-option CreateNamespace=true
    ```

6.  Label the `spring-petclinic` destination namespace to be managed by the `openshift-gitops` Argo CD instance:

    ``` terminal
    $ oc label ns spring-petclinic "argocd.argoproj.io/managed-by=openshift-gitops"
    ```

7.  List the available applications to confirm that the application is created successfully and repeat the command until the application has the `Healthy` and `Synced` statuses:

    ``` terminal
    $ argocd app list
    ```

</div>

# Creating an application in core mode by using the GitOps CLI

You can create applications in `core` mode by using the GitOps `argocd` CLI.

<div>

<div class="title">

Prerequisites

</div>

- You have installed the Red Hat OpenShift GitOps Operator on your OpenShift Container Platform cluster.

- You have installed the OpenShift CLI (`oc`).

- You have installed the Red Hat OpenShift GitOps `argocd` CLI.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Log in to the OpenShift Container Platform cluster by using the `oc` CLI tool:

    ``` terminal
    $ oc login -u <username> -p <password> <server_url>
    ```

    **Example:**

    ``` terminal
    $ oc login -u kubeadmin -p '<password>' https://api.crc.testing:6443
    ```

2.  Check whether the context is set correctly in the `kubeconfig` file:

    ``` terminal
    $ oc config current-context
    ```

3.  Set the default namespace of the current context to `openshift-gitops`:

    ``` terminal
    $ oc config set-context --current --namespace openshift-gitops
    ```

4.  Set the following environment variable to override the Argo CD component names:

    ``` terminal
    $ export ARGOCD_REPO_SERVER_NAME=openshift-gitops-repo-server
    ```

5.  Verify that you are able to run `argocd` commands in `core` mode by listing all applications:

    ``` terminal
    $ argocd app list --core
    ```

    If the configuration is correct, then existing applications will be listed with the following header:

    **Sample output:**

    ``` terminal
    NAME CLUSTER NAMESPACE  PROJECT  STATUS  HEALTH   SYNCPOLICY  CONDITIONS  REPO PATH TARGET
    ```

6.  Create an application in `core` mode:

    ``` terminal
    $ argocd app create app-spring-petclinic --core \
        --repo https://github.com/redhat-developer/openshift-gitops-getting-started.git \
        --path app \
        --revision main \
        --dest-server  https://kubernetes.default.svc \
        --dest-namespace spring-petclinic \
        --directory-recurse \
        --sync-policy automated \
        --self-heal \
        --sync-option Prune=true \
        --sync-option CreateNamespace=true
    ```

7.  Label the `spring-petclinic` destination namespace to be managed by the `openshift-gitops` Argo CD instance:

    ``` terminal
    $ oc label ns spring-petclinic "argocd.argoproj.io/managed-by=openshift-gitops"
    ```

8.  List the available applications to confirm that the application is created successfully and repeat the command until the application has the `Healthy` and `Synced` statuses:

    ``` terminal
    $ argocd app list --core
    ```

</div>

# Additional resources

- [Installing the GitOps CLI](../installing_gitops/installing-argocd-gitops-cli.md#installing-argocd-gitops-cli)

- [Basic GitOps argocd commands](../gitops_cli_argocd/argocd-gitops-cli-reference.md#argocd-gitops-cli-reference)
