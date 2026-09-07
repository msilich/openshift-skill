<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Red Hat OpenShift GitOps uses Argo CD to manage specific cluster-scoped resources, including cluster Operators, optional Operator Lifecycle Manager (OLM) Operators, and user management.

# Prerequisites

- You have access to the OpenShift Container Platform web console.

- You are logged in to the OpenShift Container Platform cluster as an administrator.

- Your cluster has the Marketplace capability enabled or the Red Hat Operator catalog source configured manually.

> [!WARNING]
> If you have already installed the Community version of the Argo CD Operator, remove the Argo CD Community Operator before you install the Red Hat OpenShift GitOps Operator.

This guide explains how to install the Red Hat OpenShift GitOps Operator to an OpenShift Container Platform cluster and log in to the Argo CD instance.

> [!IMPORTANT]
> The `latest` channel enables installation of the most recent stable version of the Red Hat OpenShift GitOps Operator. Currently, it is the default channel for installing the Red Hat OpenShift GitOps Operator.
>
> To install a specific version of the Red Hat OpenShift GitOps Operator, cluster administrators can use the corresponding `gitops-<version>` channel. For example, to install the Red Hat OpenShift GitOps Operator version 1.19.x, you can use the `gitops-1.19` channel.

# Installing Red Hat OpenShift GitOps Operator in web console

You can install Red Hat OpenShift GitOps Operator from the OperatorHub by using the web console.

<div>

<div class="title">

Procedure

</div>

1.  In the OpenShift Container Platform web console:

    1.  Click **Operators** → **OperatorHub**, if your version of OpenShift Container Platform is 4.19 or earlier.

    2.  Click **Ecosystem** → **Software Catalog**, if your version of OpenShift Container Platform is 4.20 or later.

    3.  Type `openshift-gitops` in the **Filter by keyword** box.

2.  Search for `OpenShift GitOps`, click the **Red Hat OpenShift GitOps** tile, and then click **Install**.

3.  On the **Install Operator** page:

    1.  Select an **Update channel**.

    2.  Select a GitOps **Version** to install.

    3.  Choose an **Installed Namespace**. The default installation namespace is `openshift-gitops-operator`.

        > [!NOTE]
        > For the GitOps version 1.10 and later, the default namespace changed from `openshift-operators` to `openshift-gitops operator`.

    4.  Select the **Enable Operator recommended cluster monitoring on this Namespace** checkbox to enable cluster monitoring.

        > [!NOTE]
        > You can enable cluster monitoring on any namespace by applying the `openshift.io/cluster-monitoring=true` label:
        >
        > ``` terminal
        > $ oc label namespace <namespace> openshift.io/cluster-monitoring=true
        > ```
        >
        > **Example output:**
        >
        > ``` terminal
        > namespace/<namespace> labeled
        > ```

4.  Click **Install** to make the GitOps Operator available on the OpenShift Container Platform cluster.

    Red Hat OpenShift GitOps is installed in all namespaces of the cluster.

5.  Verify that the Red Hat OpenShift GitOps Operator is listed in **Operators** → **Installed Operators**. The **Status** should resolve to **Succeeded**.

    After the Red Hat OpenShift GitOps Operator is installed, it automatically sets up a ready-to-use Argo CD instance that is available in the `openshift-gitops` namespace, and an Argo CD icon is displayed in the console toolbar. You can create subsequent Argo CD instances for your applications under your projects.

</div>

# Installing Red Hat OpenShift GitOps Operator using CLI

You can install Red Hat OpenShift GitOps Operator from the OperatorHub by using the CLI.

> [!NOTE]
> For the GitOps version 1.10 and later, the default namespace changed from `openshift-operators` to `openshift-gitops operator`.

<div>

<div class="title">

Prerequisite

</div>

- You have login credentials to access the OpenShift Container Platform cluster with `cluster-admin` privileges.

- You have installed the [`oc` CLI](https://docs.redhat.com/en/documentation/openshift_container_platform/latest/html/cli_tools/openshift-cli-oc).

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create a `openshift-gitops-operator` namespace:

    ``` terminal
    $ oc create ns openshift-gitops-operator
    ```

    **Example output:**

    ``` terminal
    namespace/openshift-gitops-operator created
    ```

    > [!NOTE]
    > You can enable cluster monitoring on `openshift-gitops-operator`, or any namespace, by applying the `openshift.io/cluster-monitoring=true` label:

    ``` terminal
    $ oc label namespace <namespace> openshift.io/cluster-monitoring=true
    ```

    **Example output:**

    ``` terminal
    namespace/<namespace> labeled
    ```

2.  Create a `OperatorGroup` object YAML file, for example, `gitops-operator-group.yaml`:

    **Example OperatorGroup:**

    ``` yaml
    apiVersion: operators.coreos.com/v1
    kind: OperatorGroup
    metadata:
      name: openshift-gitops-operator
      namespace: openshift-gitops-operator
    spec:
      upgradeStrategy: Default
    ```

3.  Apply the `OperatorGroup` to the cluster:

    ``` terminal
    $ oc apply -f gitops-operator-group.yaml
    ```

    **Example output:**

    ``` terminal
    operatorgroup.operators.coreos.com/openshift-gitops-operator created
    ```

4.  Create a `Subscription` object YAML file to subscribe a namespace to the Red Hat OpenShift GitOps Operator, for example, `openshift-gitops-sub.yaml`:

    **Example Subscription:**

    ``` yaml
    apiVersion: operators.coreos.com/v1alpha1
    kind: Subscription
    metadata:
      name: openshift-gitops-operator
      namespace: openshift-gitops-operator
    spec:
      channel: latest
      installPlanApproval: Automatic
      name: openshift-gitops-operator
      source: redhat-operators
      sourceNamespace: openshift-marketplace
    ```

    where:

    `metadata.name`
    Specifies the specify the channel name from where you want to subscribe the Operator.

    `metadata.namespace`
    Specifies the specify the name of the Operator to subscribe to.

    `spec.channel`
    Specifies the specify the name of the CatalogSource that provides the Operator.

    `spec.source` (openshift-marketplace namespace)
    Specifies the namespace of the CatalogSource. Use `openshift-marketplace` for the default OperatorHub CatalogSources.

5.  Apply the `Subscription` to the cluster:

    ``` terminal
    $ oc apply -f openshift-gitops-sub.yaml
    ```

    **Example output:**

    ``` terminal
    subscription.operators.coreos.com/openshift-gitops-operator created
    ```

6.  After the installation is complete, verify that all the pods in the `openshift-gitops` namespace are running:

    ``` terminal
    $ oc get pods -n openshift-gitops
    ```

    **Example output:**

    ``` terminal
    NAME                                                           READY   STATUS    RESTARTS   AGE
    cluster-785cfc5f75-669wq                                      1/1     Running   0          76s
    gitops-plugin-6664c749dd-dx64s                                1/1     Running   0          76s
    openshift-gitops-application-controller-0                     1/1     Running   0          74s
    openshift-gitops-applicationset-controller-549d7f6686-wzckt   1/1     Running   0          74s
    openshift-gitops-dex-server-5d4ffdb9b9-lb7b7                  1/1     Running   0          74s
    openshift-gitops-redis-6d65c94d4b-k9l8k                       1/1     Running   0          75s
    openshift-gitops-repo-server-79db854c58-279jr                 1/1     Running   0          75s
    openshift-gitops-server-f488b848-xntbc                        1/1     Running   0          75s
    ```

7.  Verify that the pods in the `openshift-gitops-operator` namespace are running:

    ``` terminal
    $ oc get pods -n openshift-gitops-operator
    ```

    **Example output:**

    ``` terminal
    NAME                                                            READY   STATUS    RESTARTS   AGE
    openshift-gitops-operator-controller-manager-6fdc5cd9dc-jr9mn   2/2     Running   0          41s
    ```

</div>

# Additional resources

- [Setting up an Argo CD instance](../argocd_instance/setting-up-argocd-instance.md#setting-up-argocd-instance)

- [Marketplace capability](https://docs.openshift.com/container-platform/latest/installing/overview/cluster-capabilities.html#marketplace-operator_cluster-capabilities)
