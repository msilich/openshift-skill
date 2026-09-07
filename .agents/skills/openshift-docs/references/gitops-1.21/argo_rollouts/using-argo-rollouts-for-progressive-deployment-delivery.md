<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

To use Argo Rollouts and manage progressive delivery, after you install the Red Hat OpenShift GitOps Operator on the cluster, you can create and configure a `RolloutManager` custom resource (CR) instance in the namespace of your choice. You can scope the `RolloutManager` CR for single or multiple namespaces.

# Prerequisites

- You have access to the cluster with `cluster-admin` privileges.

- You have access to the OpenShift Container Platform web console.

- Red Hat OpenShift GitOps 1.9.0 or a newer version is installed on your cluster.

# Creating a RolloutManager custom resource

To manage progressive delivery of deployments by using Argo Rollouts in Red Hat OpenShift GitOps, you must create and configure a `RolloutManager` custom resource (CR) in the namespace of your choice. By default, any new `argo-rollouts` instance has permission to manage resources only in the namespace where it is deployed, but you can use Argo Rollouts in multiple namespaces as required.

<div>

<div class="title">

Prerequisites

</div>

- Red Hat OpenShift GitOps 1.9.0 or a newer version is installed on your cluster.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Log in to the OpenShift Container Platform web console as a cluster administrator.

2.  In the **Administrator** perspective, click **Operators** → **Installed Operators**.

3.  Create or select the project where you want to create and configure a `RolloutManager` custom resource (CR) from the **Project** drop-down menu.

4.  Select **Red Hat OpenShift GitOps** from the installed operators.

5.  In the **Details** tab, under the **Provided APIs** section, click **Create instance** in the **RolloutManager** pane.

6.  On the **Create RolloutManager** page, select the **YAML view** and use the default YAML or edit it according to your requirements:

    **Example: `RolloutManager` CR:**

    ``` yaml
    apiVersion: argoproj.io/v1alpha1
    kind: RolloutManager
    metadata:
      name: argo-rollout
      namespace: openshift-gitops
    spec: {}
    ```

7.  Click **Create**.

8.  In the **RolloutManager** tab, under the **RolloutManagers** section, verify that the **Status** field of the RolloutManager instance shows as **Phase: Available**.

9.  In the left navigation pane, verify the creation of the namespace-scoped supporting resources:

    - Click **Workloads** → **Deployments** to verify that the `argo-rollouts` deployment is available with the **Status** showing as `1 of 1 pods` running.

    - Click **Workloads** → **Secrets** to verify that the `argo-rollouts-notification-secret` secret is available.

    - Click **Networking** → **Services** to verify that the `argo-rollouts-metrics` service is available.

    - Click **User Management** → **Roles** to verify that the `argo-rollouts` role and `argo-rollouts-aggregate-to-admin`, `argo-rollouts-aggregate-to-edit`, and `argo-rollouts-aggregate-to-view` cluster roles are available.

    - Click **User Management** → **RoleBindings** to verify that the `argo-rollouts` role binding is available.

</div>

# Deleting a RolloutManager custom resource

Uninstalling the Red Hat OpenShift GitOps Operator does not remove the resources that were created during installation. You must manually delete the `RolloutManager` custom resource (CR) before you uninstall the Red Hat OpenShift GitOps Operator.

<div>

<div class="title">

Prerequisites

</div>

- Red Hat OpenShift GitOps 1.9.0 or a newer version is installed on your cluster.

- A `RolloutManager` CR exists in your namespace.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Log in to the OpenShift Container Platform web console as a cluster administrator.

2.  In the **Administrator** perspective, click **Operators** → **Installed Operators**.

3.  Click the **Project** drop-down menu and select the project that contains the `RolloutManager` CR.

4.  Select **Red Hat OpenShift GitOps** from the installed operators.

5.  Click the **RolloutManager** tab to find RolloutManager instances under the **RolloutManagers** section.

6.  Click the instance.

7.  Click **Actions** → **Delete RolloutManager** from the drop-down menu, and click **Delete** to confirm in the dialog box.

8.  In the **RolloutManager** tab, under the **RolloutManagers** section, verify that the RolloutManager instance is not available anymore.

9.  In the left navigation pane, verify the deletion of the namespace-scoped supporting resources:

    - Click **Workloads** → **Deployments** to verify that the `argo-rollouts` deployment is deleted.

    - Click **Workloads** → **Secrets** to verify that the `argo-rollouts-notification-secret` secret is deleted.

    - Click **Networking** → **Services** to verify that the `argo-rollouts-metrics` service is deleted.

    - Click **User Management** → **Roles** to verify that the `argo-rollouts` role and `argo-rollouts-aggregate-to-admin`, `argo-rollouts-aggregate-to-edit`, and `argo-rollouts-aggregate-to-view` cluster roles are deleted.

    - Click **User Management** → **RoleBindings** to verify that the `argo-rollouts` role binding is deleted.

</div>

# Installing Argo Rollouts CLI on Linux

You can install the Argo Rollouts CLI on Linux.

<div>

<div class="title">

Prerequisites

</div>

- You have installed the OpenShift Container Platform CLI (`oc`).

</div>

<div>

<div class="title">

Procedure

</div>

1.  Download the latest version of the Argo Rollouts CLI binary, `kubectl-argo-rollouts`, by running the following command:

    ``` terminal
    $ curl -LO https://github.com/argoproj/argo-rollouts/releases/latest/download/kubectl-argo-rollouts-linux-amd64
    ```

2.  Ensure that the `kubectl-argo-rollouts` binary is executable by running the following command:

    ``` terminal
    $ chmod +x ./kubectl-argo-rollouts-linux-amd64
    ```

3.  Move the `kubectl-argo-rollouts` binary to the system path by running the following command:

    ``` terminal
    # mv ./kubectl-argo-rollouts-linux-amd64 /usr/local/bin/kubectl-argo-rollouts
    ```

    > [!IMPORTANT]
    > Ensure that you have superuser privileges to run this command.

4.  Verify that the plugin is installed correctly by running the following command and receiving similar output:

    ``` terminal
    $ oc argo rollouts version
    ```

    **Example output:**

    ``` terminal
    kubectl-argo-rollouts: v1.6.6+737ca89
      BuildDate: 2024-02-13T15:39:31Z
      GitCommit: 737ca89b42e4791e96e05b438c2b8540737a2a1a
      GitTreeState: clean
      GoVersion: go1.20.14
      Compiler: gc
      Platform: linux/amd64
    ```

    where:

    `kubectl-argo-rollouts`
    Specifies the version information of the Argo Rollouts binary.

    `BuildDate`
    Specifies the build date of the Argo Rollouts binary.

    `GitCommit`
    Specifies the Git commit hash that built the Argo Rollouts binary.

    `GoVersion`
    Specifies the version of the Go language that built the Argo Rollouts binary.

    `Platform`
    Specifies the platform (operating system and architecture) that runs the binary.

</div>

# Installing Argo Rollouts CLI on macOS

If you are a macOS user, you can install the Argo Rollouts CLI by using the [Homebrew](https://brew.sh) package manager.

<div>

<div class="title">

Prerequisites

</div>

- You have installed the Homebrew (`brew`) package manager.

</div>

<div>

<div class="title">

Procedure

</div>

- Run the following command to install the Argo Rollouts CLI:

  ``` terminal
  $ brew install argoproj/tap/kubectl-argo-rollouts
  ```

</div>

# Enabling Argo Rollouts UI on an Argo CD instance

To enable Argo Rollouts UI on an Argo CD instance, complete the following steps.

<div>

<div class="title">

Prerequisites

</div>

- You have access to the cluster with `cluster-admin` privileges.

- You have installed the Red Hat OpenShift GitOps Operator on your OpenShift Container Platform cluster.

- You have configured the **RolloutManager** custom resource (CR).

</div>

<div>

<div class="title">

Procedure

</div>

1.  Log in to the OpenShift Container Platform web console.

2.  In the **Administrator** perspective of the web console, click **Operators** → **Installed Operators**.

3.  Select **Red Hat OpenShift GitOps** from the installed Operators list and click the **Argo CD** tab.

4.  Select the Argo CD instance in the **Argo CD** tab under the `openshift-gitops` namespace.

5.  Click **YAML** and add the following configuration to configure the Argo Rollouts UI:

    **Example enabling Argo Rollouts UI in the Argo CD CR:**

    ``` yaml
    apiVersion: argoproj.io/v1beta1
    kind: ArgoCD
    metadata:
      name: argocd
    spec:
      server:
        enableRolloutsUI: true
    ```

    where:

    `spec.server.enableRolloutsUI`
    Specifies the value of `enableRolloutsUI` field to configure the Rollouts UI.

6.  Click **Save**.

7.  In the **Administrator** perspective of the web console, navigate to the ![red hat applications menu icon](data:image/jpg;base64,/9j/4QCLRXhpZgAATU0AKgAAAAgABgEPAAIAAAAIAAAAVgESAAMAAAABAAEAAAEaAAUAAAABAAAAXgEbAAUAAAABAAAAZgEoAAMAAAABAAIAAAExAAIAAAAVAAAAbgAAAABCZUZ1bmt5AAAAASwAAAABAAABLAAAAAFCZUZ1bmt5IFBob3RvIEVkaXRvcgD/4AAQSkZJRgABAQEBLAEsAAD/2wBDAAEBAQEBAQEBAQEBAQEBAQIBAQEBAQIBAQECAgICAgICAgIDAwQDAwMDAwICAwQDAwQEBAQEAgMFBQQEBQQEBAT/2wBDAQEBAQEBAQIBAQIEAwIDBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAT/wAARCAAgACADAREAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwD+KegAoAKACgAoA/uU+J37BH/BDLTPjd+xX4f8J/sXftm6d4P+IXiXxTF8TtE1b9nP9rG01Hxxptl4D1fUdPW1trjTxqN7cQalHpl0w8Mq4jhS4kucWo3UAL8MP2CP+CGWqfG79tPw/wCLP2Lv2zdR8IfD3xN4Wi+GOh6T+zn+1jd6j4H0298B6RqOoLdW1vp51GyuJ9Sk1O6UeJlQSQvbyW2bUhqAP4aqACgD/UT+OXhb/goEP2lv+Cc9vrX7V/7GWrazq3xB8by+GrvSf2NfFdjpy3kfws8TSXF/dWLfE6SXVbc2rXkSmzudLWGa+t5nE6AW1AB8DPC3/BQJv2lv+Ci9vov7V/7GWk6zpPxB8ES+JbvVv2NfFd/pzXknws8MyW9/a2A+J0culW4tVs4m+2XOqLNNY3EyCBCbagD/AC7KACgAoAKAD9KAP//Z) menu → **OpenShift GitOps** → **Cluster Argo CD**. The login page of the Argo CD Web UI is displayed in a new window.

8.  To access the Argo Rollouts UI in the Argo CD Web UI, configure a sample application that includes the Argo Rollouts resources.

    > [!NOTE]
    > The `enableRolloutsUI` field restarts the Argo CD server deployment pod, so it takes a few seconds for the Argo Rollouts extension to enable in the Argo CD Web UI.

</div>

# Additional resources

- [RolloutManager custom resource (CR)](using-argo-rollouts-for-progressive-deployment-delivery.md#gitops-creating-rolloutmanager-custom-resource_using-argo-rollouts-for-progressive-deployment-delivery)

- [Getting started with Argo Rollouts](getting-started-with-argo-rollouts.md#getting-started-with-argo-rollouts)

- [Installing Red Hat OpenShift GitOps](../installing_gitops/installing-openshift-gitops.md#installing-openshift-gitops)

- [Uninstalling Red Hat OpenShift GitOps](../removing_gitops/uninstalling-openshift-gitops.md#uninstalling-openshift-gitops)

- [`RolloutManager` Custom Resource specification](https://argo-rollouts-manager.readthedocs.io/en/latest/crd_reference/)
