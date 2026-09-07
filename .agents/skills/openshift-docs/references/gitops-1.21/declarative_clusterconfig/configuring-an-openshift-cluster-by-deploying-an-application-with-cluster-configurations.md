<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

With Red Hat OpenShift GitOps, you can configure Argo CD to recursively sync the content of a Git directory with an application that contains custom configurations for your cluster.

# Prerequisites

- You have logged in to the OpenShift Container Platform cluster as an administrator.

- You have installed the Red Hat OpenShift GitOps Operator on your OpenShift Container Platform cluster.

# Using an Argo CD instance to manage cluster-scoped resources

> [!WARNING]
> Do not elevate the permissions of Argo CD instances to be cluster-scoped unless you have a distinct use case that requires it. Only users with `cluster-admin` privileges should manage the instances you elevate. Anyone with access to the namespace of a cluster-scoped instance can elevate their privileges on the cluster to become a cluster administrator themselves.

To manage cluster-scoped resources, update the existing `Subscription` object for the Red Hat OpenShift GitOps Operator and add the namespace of the Argo CD instance to the `ARGOCD_CLUSTER_CONFIG_NAMESPACES` environment variable in the `spec` section.

<div>

<div class="title">

Procedure

</div>

1.  In the **Administrator** perspective of the web console, navigate to **Operators** → **Installed Operators** → **Red Hat OpenShift GitOps** → **Subscription**.

2.  Click the **Actions** list and then click **Edit Subscription**.

3.  On the **openshift-gitops-operator** Subscription details page, under the **YAML** tab, edit the `Subscription` YAML file by adding the namespace of the Argo CD instance to the `ARGOCD_CLUSTER_CONFIG_NAMESPACES` environment variable in the `spec` section:

    ``` yaml
    apiVersion: operators.coreos.com/v1alpha1
    kind: Subscription
    metadata:
      name: openshift-gitops-operator
      namespace: openshift-gitops-operator
    # ...
    spec:
      config:
        env:
        - name: ARGOCD_CLUSTER_CONFIG_NAMESPACES
          value: openshift-gitops, <list of namespaces of cluster-scoped Argo CD instances>
    # ...
    ```

4.  Click **Save** and **Reload**.

5.  To verify that the Argo CD instance is configured with a cluster role to manage cluster-scoped resources, perform the following steps:

    1.  Navigate to **User Management** → **Roles** and from the **Filter** list select **Cluster-wide Roles**.

    2.  Search for the `argocd-application-controller` by using the **Search by name** field.

        The **Roles** page displays the created cluster role.

        > [!TIP]
        > Alternatively, in the OpenShift CLI, run the following command:
        >
        > ``` terminal
        > oc auth can-i create oauth -n openshift-gitops --as system:serviceaccount:openshift-gitops:openshift-gitops-argocd-application-controller
        > ```
        >
        > The output `yes` verifies that the Argo instance is configured with a cluster role to manage cluster-scoped resources. Else, check your configurations and take necessary steps as required.

</div>

# Default permissions of an Argo CD instance

By default Argo CD instance has the following permissions:

- Argo CD instance has the `admin` privileges to manage resources only in the namespace where it is deployed. For instance, an Argo CD instance deployed in the **foo** namespace has the `admin` privileges to manage resources only for that namespace.

- Argo CD has the following cluster-scoped permissions because Argo CD requires cluster-wide `read` privileges on resources to function appropriately:

  ``` yaml
  - verbs:
      - get
      - list
      - watch
     apiGroups:
      - '*'
     resources:
      - '*'
   - verbs:
      - get
      - list
     nonResourceURLs:
      - '*'
  ```

<div class="note">

<div class="title">

</div>

- You can edit the cluster roles used by the `argocd-server` and `argocd-application-controller` components where Argo CD is running such that the `write` privileges are limited to only the namespaces and resources that you wish Argo CD to manage.

  ``` terminal
  $ oc edit clusterrole argocd-server
  $ oc edit clusterrole argocd-application-controller
  ```

</div>

# Running the Argo CD instance at the cluster-level

The default Argo CD instance and the accompanying controllers, installed by the Red Hat OpenShift GitOps Operator, can now run on the infrastructure nodes of the cluster by setting a simple configuration toggle.

<div>

<div class="title">

Procedure

</div>

1.  Label the existing nodes:

    ``` terminal
    $ oc label node <node-name> node-role.kubernetes.io/infra=""
    ```

2.  Optional: If required, you can also apply taints and isolate the workloads on infrastructure nodes and prevent other workloads from scheduling on these nodes:

    ``` terminal
    $ oc adm taint nodes -l node-role.kubernetes.io/infra \
    infra=reserved:NoSchedule infra=reserved:NoExecute
    ```

3.  Add the `runOnInfra` toggle in the `GitOpsService` custom resource:

    ``` yaml
    apiVersion: pipelines.openshift.io/v1alpha1
    kind: GitopsService
    metadata:
      name: cluster
    spec:
      runOnInfra: true
    ```

4.  Optional: If taints have been added to the nodes, then add `tolerations` to the `GitOpsService` custom resource.

    **Example:**

    ``` yaml
    apiVersion: pipelines.openshift.io/v1alpha1
    kind: GitopsService
    metadata:
      name: cluster
      spec:
        runOnInfra: true
        tolerations:
        - effect: NoSchedule
          key: infra
          value: reserved
        - effect: NoExecute
          key: infra
          value: reserved
    ```

5.  Verify that the workloads in the `openshift-gitops` namespace are now scheduled on the infrastructure nodes by viewing **Pods** → **Pod details** for any pod in the console UI.

</div>

> [!NOTE]
> Any `nodeSelectors` and `tolerations` manually added to the default Argo CD custom resource are overwritten by the toggle and `tolerations` in the `GitOpsService` custom resource.

# Additional resources

- For more information on taints and tolerations, see [Controlling pod placement using node taints](https://docs.openshift.com/container-platform/latest/nodes/scheduling/nodes-scheduler-taints-tolerations.html#nodes-scheduler-taints-tolerations).

- For more information on infrastructure machine sets, see [Creating infrastructure machine sets](https://docs.openshift.com/container-platform/latest/machine_management/creating-infrastructure-machinesets.html#creating-infrastructure-machinesets).

# Creating an application by using the Argo CD dashboard

Argo CD provides a dashboard which allows you to create applications.

This sample workflow walks you through the process of configuring Argo CD to recursively sync the content of the `cluster` directory to the `cluster-configs` application. The directory defines the OpenShift Container Platform web console cluster configurations that add a link to the **Red Hat Developer Blog - Kubernetes** under the ![red hat applications menu icon](data:image/jpg;base64,/9j/4QCLRXhpZgAATU0AKgAAAAgABgEPAAIAAAAIAAAAVgESAAMAAAABAAEAAAEaAAUAAAABAAAAXgEbAAUAAAABAAAAZgEoAAMAAAABAAIAAAExAAIAAAAVAAAAbgAAAABCZUZ1bmt5AAAAASwAAAABAAABLAAAAAFCZUZ1bmt5IFBob3RvIEVkaXRvcgD/4AAQSkZJRgABAQEBLAEsAAD/2wBDAAEBAQEBAQEBAQEBAQEBAQIBAQEBAQIBAQECAgICAgICAgIDAwQDAwMDAwICAwQDAwQEBAQEAgMFBQQEBQQEBAT/2wBDAQEBAQEBAQIBAQIEAwIDBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAT/wAARCAAgACADAREAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwD+KegAoAKACgAoA/uU+J37BH/BDLTPjd+xX4f8J/sXftm6d4P+IXiXxTF8TtE1b9nP9rG01Hxxptl4D1fUdPW1trjTxqN7cQalHpl0w8Mq4jhS4kucWo3UAL8MP2CP+CGWqfG79tPw/wCLP2Lv2zdR8IfD3xN4Wi+GOh6T+zn+1jd6j4H0298B6RqOoLdW1vp51GyuJ9Sk1O6UeJlQSQvbyW2bUhqAP4aqACgD/UT+OXhb/goEP2lv+Cc9vrX7V/7GWrazq3xB8by+GrvSf2NfFdjpy3kfws8TSXF/dWLfE6SXVbc2rXkSmzudLWGa+t5nE6AW1AB8DPC3/BQJv2lv+Ci9vov7V/7GWk6zpPxB8ES+JbvVv2NfFd/pzXknws8MyW9/a2A+J0culW4tVs4m+2XOqLNNY3EyCBCbagD/AC7KACgAoAKAD9KAP//Z) menu in the web console, and defines a namespace `spring-petclinic` on the cluster.

<div>

<div class="title">

Prerequisites

</div>

- You have logged in to the OpenShift Container Platform cluster as an administrator.

- You have installed the Red Hat OpenShift GitOps Operator on your OpenShift Container Platform cluster.

- You have logged in to an Argo CD instance.

</div>

<div>

<div class="title">

Procedure

</div>

1.  In the Argo CD dashboard, click **NEW APP** to add a new Argo CD application.

2.  For this workflow, create a **cluster-configs** application with the following configurations:

    Application Name
    `cluster-configs`

    Project
    `default`

    Sync Policy
    `Manual`

    Repository URL
    `https://github.com/redhat-developer/openshift-gitops-getting-started`

    Revision
    `HEAD`

    Path
    `cluster`

    Destination
    `https://kubernetes.default.svc`

    Namespace
    `spring-petclinic`

    Directory Recurse
    `checked`

3.  Click **CREATE** to create your application.

4.  Open the **Administrator** perspective of the web console and expand **Administration** → **Namespaces**.

5.  Search for and select the `spring-petclinic` namespace, then enter `argocd.argoproj.io/managed-by=openshift-gitops` in the **Label** field so that the Argo CD instance in the `openshift-gitops` namespace can manage your namespace.

</div>

# Creating an application by using the `oc` tool

You can create Argo CD applications in your terminal by using the `oc` tool.

<div>

<div class="title">

Prerequisites

</div>

- You have installed the Red Hat OpenShift GitOps Operator on your OpenShift Container Platform cluster.

- You have logged in to an Argo CD instance.

- You have access to the `oc` CLI tool.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Download [the sample application](https://github.com/redhat-developer/openshift-gitops-getting-started):

    ``` terminal
    $ git clone git@github.com:redhat-developer/openshift-gitops-getting-started.git
    ```

2.  Create the application:

    ``` terminal
    $ oc create -f openshift-gitops-getting-started/argo/cluster.yaml
    ```

3.  Run the `oc get` command to review the created application:

    ``` terminal
    $ oc get application -n openshift-gitops
    ```

4.  Add a label to the namespace your application is deployed in so that the Argo CD instance in the `openshift-gitops` namespace can manage it:

    ``` terminal
    $ oc label namespace spring-petclinic argocd.argoproj.io/managed-by=openshift-gitops
    ```

</div>

# Creating an application in the default mode by using the GitOps CLI

You can create applications in the default mode by using the GitOps `argocd` CLI.

This sample workflow walks you through the process of configuring Argo CD to recursively sync the content of the `cluster` directory to the `cluster-configs` application. The directory defines the OpenShift Container Platform cluster configurations and the `spring-petclinic` namespace on the cluster.

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
    $ argocd app create app-cluster-configs \
        --repo https://github.com/redhat-developer/openshift-gitops-getting-started.git \
        --path cluster \
        --revision main \
        --dest-server  https://kubernetes.default.svc \
        --dest-namespace spring-petclinic \
        --directory-recurse \
        --sync-policy none \
        --sync-option Prune=true \
        --sync-option CreateNamespace=true
    ```

6.  Label the `spring-petclinic` destination namespace to be managed by the `openshift-gitops` Argo CD instance:

    ``` terminal
    $ oc label ns spring-petclinic "argocd.argoproj.io/managed-by=openshift-gitops"
    ```

7.  List the available applications to confirm that the application is created successfully:

    ``` terminal
    $ argocd app list
    ```

    Even though the `cluster-configs` Argo CD application has the `Healthy` status, it is not automatically synced due to its `none` sync policy, causing it to remain in the `OutOfSync` status.

</div>

# Creating an application in core mode by using the GitOps CLI

You can create applications in `core` mode by using the GitOps `argocd` CLI.

This sample workflow walks you through the process of configuring Argo CD to recursively sync the content of the `cluster` directory to the `cluster-configs` application. The directory defines the OpenShift Container Platform cluster configurations and the `spring-petclinic` namespace on the cluster.

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
    $ argocd app create app-cluster-configs --core \
        --repo https://github.com/redhat-developer/openshift-gitops-getting-started.git \
        --path cluster \
        --revision main \
        --dest-server  https://kubernetes.default.svc \
        --dest-namespace spring-petclinic \
        --directory-recurse \
        --sync-policy none \
        --sync-option Prune=true \
        --sync-option CreateNamespace=true
    ```

7.  Label the `spring-petclinic` destination namespace to be managed by the `openshift-gitops` Argo CD instance:

    ``` terminal
    $ oc label ns spring-petclinic "argocd.argoproj.io/managed-by=openshift-gitops"
    ```

8.  List the available applications to confirm that the application is created successfully:

    ``` terminal
    $ argocd app list --core
    ```

    Even though the `cluster-configs` Argo CD application has the `Healthy` status, it is not automatically synced due to its `none` sync policy, causing it to remain in the `OutOfSync` status.

</div>

# Synchronizing your application with your Git repository

You can synchronize your application with your Git repository by modifying the synchronization policy for Argo CD. The policy modification automatically applies the changes in your cluster configurations from your Git repository to the cluster.

<div>

<div class="title">

Procedure

</div>

1.  In the Argo CD dashboard, notice that the **cluster-configs** Argo CD application has the statuses **Missing** and **OutOfSync**. Because the application was configured with a manual sync policy, Argo CD does not sync it automatically.

2.  Click **SYNC** on the **cluster-configs** tile, review the changes, and then click **SYNCHRONIZE**. Argo CD will detect any changes in the Git repository automatically. If the configurations are changed, Argo CD will change the status of the **cluster-configs** to **OutOfSync**. You can modify the synchronization policy for Argo CD to automatically apply changes from your Git repository to the cluster.

3.  Notice that the **cluster-configs** Argo CD application now has the statuses **Healthy** and **Synced**. Click the **cluster-configs** tile to check the details of the synchronized resources and their status on the cluster.

4.  Navigate to the OpenShift Container Platform web console and click ![red hat applications menu icon](data:image/jpg;base64,/9j/4QCLRXhpZgAATU0AKgAAAAgABgEPAAIAAAAIAAAAVgESAAMAAAABAAEAAAEaAAUAAAABAAAAXgEbAAUAAAABAAAAZgEoAAMAAAABAAIAAAExAAIAAAAVAAAAbgAAAABCZUZ1bmt5AAAAASwAAAABAAABLAAAAAFCZUZ1bmt5IFBob3RvIEVkaXRvcgD/4AAQSkZJRgABAQEBLAEsAAD/2wBDAAEBAQEBAQEBAQEBAQEBAQIBAQEBAQIBAQECAgICAgICAgIDAwQDAwMDAwICAwQDAwQEBAQEAgMFBQQEBQQEBAT/2wBDAQEBAQEBAQIBAQIEAwIDBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAT/wAARCAAgACADAREAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwD+KegAoAKACgAoA/uU+J37BH/BDLTPjd+xX4f8J/sXftm6d4P+IXiXxTF8TtE1b9nP9rG01Hxxptl4D1fUdPW1trjTxqN7cQalHpl0w8Mq4jhS4kucWo3UAL8MP2CP+CGWqfG79tPw/wCLP2Lv2zdR8IfD3xN4Wi+GOh6T+zn+1jd6j4H0298B6RqOoLdW1vp51GyuJ9Sk1O6UeJlQSQvbyW2bUhqAP4aqACgD/UT+OXhb/goEP2lv+Cc9vrX7V/7GWrazq3xB8by+GrvSf2NfFdjpy3kfws8TSXF/dWLfE6SXVbc2rXkSmzudLWGa+t5nE6AW1AB8DPC3/BQJv2lv+Ci9vov7V/7GWk6zpPxB8ES+JbvVv2NfFd/pzXknws8MyW9/a2A+J0culW4tVs4m+2XOqLNNY3EyCBCbagD/AC7KACgAoAKAD9KAP//Z) to verify that a link to the **Red Hat Developer Blog - Kubernetes** is now present there.

5.  Navigate to the **Project** page and search for the `spring-petclinic` namespace to verify that it has been added to the cluster.

    Your cluster configurations have been successfully synchronized to the cluster.

</div>

# Synchronizing an application in the default mode by using the GitOps CLI

You can synchronize applications in the default mode by using the GitOps `argocd` CLI.

This sample workflow walks you through the process of configuring Argo CD to recursively sync the content of the `cluster` directory to the `cluster-configs` application. The directory defines the OpenShift Container Platform cluster configurations and the `spring-petclinic` namespace on the cluster.

<div>

<div class="title">

Prerequisites

</div>

- You have installed the Red Hat OpenShift GitOps Operator on your OpenShift Container Platform cluster.

- You have logged in to an Argo CD instance.

- You have installed the OpenShift CLI (`oc`).

- You have installed the Red Hat OpenShift GitOps `argocd` CLI.

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

4.  Because the application is configured with the `none` sync policy, you must manually trigger the sync operation:

    ``` terminal
    $ argocd app sync openshift-gitops/app-cluster-configs
    ```

5.  List the application to confirm that the application has the `Healthy` and `Synced` statuses:

    ``` terminal
    $ argocd app list
    ```

</div>

# Synchronizing an application in core mode by using the GitOps CLI

You can synchronize applications in `core` mode by using the GitOps `argocd` CLI.

This sample workflow walks you through the process of configuring Argo CD to recursively sync the content of the `cluster` directory to the `cluster-configs` application. The directory defines the OpenShift Container Platform cluster configurations and the `spring-petclinic` namespace on the cluster.

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

5.  Because the application is configured with the `none` sync policy, you must manually trigger the sync operation:

    ``` terminal
    $ argocd app sync --core openshift-gitops/app-cluster-configs
    ```

6.  List the application to confirm that the application has the `Healthy` and `Synced` statuses:

    ``` terminal
    $ argocd app list --core
    ```

</div>

# In-built permissions for cluster configuration

By default, the Argo CD instance has permissions to manage specific cluster-scoped resources such as cluster Operators, optional OLM Operators and user management.

<div class="note">

<div class="title">

</div>

- Argo CD does not have `cluster-admin` permissions.

- You can extend the permissions bound to any Argo CD instances managed by the GitOps Operator. However, you must not modify the permission resources, such as roles or cluster roles created by the GitOps Operator, because the Operator might reconcile them back to their initial state. Instead, create dedicated role and cluster role objects and bind them to the appropriate service account that the application controller uses.

</div>

Permissions for the Argo CD instance:

| Resources | Descriptions |
|----|----|
| Resource Groups | Configure the user or administrator |
| `operators.coreos.com` | Optional Operators managed by OLM |
| `user.openshift.io` , `rbac.authorization.k8s.io` | Groups, Users and their permissions |
| `config.openshift.io` | Control plane Operators managed by CVO used to configure cluster-wide build configuration, registry configuration and scheduler policies |
| `storage.k8s.io` | Storage |
| `console.openshift.io` | Console customization |

# Adding permissions for cluster configuration

You can grant permissions for an Argo CD instance to manage cluster configuration. Create a cluster role with additional permissions and then create a new cluster role binding to associate the cluster role with a service account.

<div>

<div class="title">

Prerequisites

</div>

- You have access to an OpenShift Container Platform cluster with `cluster-admin` privileges and are logged in to the web console.

- You have installed the Red Hat OpenShift GitOps Operator on your OpenShift Container Platform cluster.

</div>

<div>

<div class="title">

Procedure

</div>

1.  In the web console, select **User Management** → **Roles** → **Create Role**. Use the following `ClusterRole` YAML template to add rules to specify the additional permissions.

    ``` yaml
    apiVersion: rbac.authorization.k8s.io/v1
    kind: ClusterRole
    metadata:
      name: secrets-cluster-role
    rules:
    - apiGroups: [""]
      resources: ["secrets"]
      verbs: ["*"]
    ```

2.  Click **Create** to add the cluster role.

3.  To create the cluster role binding, select **User Management** → **Role Bindings** → **Create Binding**.

4.  Select **All Projects** from the **Project** list.

5.  Click **Create binding**.

6.  Select **Binding type** as **Cluster-wide role binding (ClusterRoleBinding)**.

7.  Enter a unique value for the **RoleBinding name**.

8.  Select the newly created cluster role or an existing cluster role from the drop-down list.

9.  Select the **Subject** as **ServiceAccount** and then provide the **Subject namespace** and **name**.

    1.  **Subject namespace**: `openshift-gitops`

    2.  **Subject name**: `openshift-gitops-argocd-application-controller`

        > [!NOTE]
        > The value of **Subject name** depends on the GitOps control plane components for which you create the cluster roles and cluster role bindings.

10. Click **Create**. The YAML file for the `ClusterRoleBinding` object is as follows:

    ``` yaml
    kind: ClusterRoleBinding
    apiVersion: rbac.authorization.k8s.io/v1
    metadata:
      name: cluster-role-binding
    subjects:
      - kind: ServiceAccount
        name: openshift-gitops-argocd-application-controller
        namespace: openshift-gitops
    roleRef:
      apiGroup: rbac.authorization.k8s.io
      kind: ClusterRole
      name: secrets-cluster-role
    ```

</div>

# Additional resources

- [Customizing permissions by creating user-defined cluster roles for cluster-scoped instances](customizing-permissions-by-creating-user-defined-cluster-roles-for-cluster-scoped-instances.md#customizing-permissions-by-creating-user-defined-cluster-roles-for-cluster-scoped-instances)

- [Customizing permissions by creating aggregated cluster roles](customizing-permissions-by-creating-aggregated-cluster-roles.md#customizing-permissions-by-creating-aggregated-cluster-roles)

# Installing OLM Operators using Red Hat OpenShift GitOps

Red Hat OpenShift GitOps with cluster configurations manages specific cluster-scoped resources and takes care of installing cluster Operators or any namespace-scoped OLM Operators.

Consider a case where as a cluster administrator, you have to install an OLM Operator such as Tekton. You use the OpenShift Container Platform web console to manually install a Tekton Operator or the OpenShift CLI to manually install a Tekton subscription and Tekton Operator group on your cluster.

Red Hat OpenShift GitOps places your Kubernetes resources in your Git repository. As a cluster administrator, use Red Hat OpenShift GitOps to manage and automate the installation of other OLM Operators without any manual procedures. For example, after you place the Tekton subscription in your Git repository by using Red Hat OpenShift GitOps, the Red Hat OpenShift GitOps automatically takes this Tekton subscription from your Git repository and installs the Tekton Operator on your cluster.

## Installing cluster-scoped Operators

Operator Lifecycle Manager (OLM) uses a default `global-operators` Operator group in the `openshift-operators` namespace for cluster-scoped Operators. Hence you do not have to manage the `OperatorGroup` resource in your GitOps repository. However, for namespace-scoped Operators, you must manage the `OperatorGroup` resource in that namespace.

To install cluster-scoped Operators, create and place the `Subscription` resource of the required Operator in your Git repository.

**Example: Grafana Operator subscription:**

``` yaml
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  name: grafana
spec:
  channel: v4
  installPlanApproval: Automatic
  name: grafana-operator
  source: redhat-operators
  sourceNamespace: openshift-marketplace
```

## Installing namespace-scoped Operators

To install namespace-scoped Operators, create and place the `Subscription` and `OperatorGroup` resources of the required Operator in your Git repository.

**Example: Ansible Automation Platform Resource Operator:**

``` yaml
# ...
apiVersion: v1
kind: Namespace
metadata:
  labels:
    openshift.io/cluster-monitoring: "true"
  name: ansible-automation-platform
# ...
apiVersion: operators.coreos.com/v1
kind: OperatorGroup
metadata:
  name: ansible-automation-platform-operator
  namespace: ansible-automation-platform
spec:
  targetNamespaces:
    - ansible-automation-platform
# ...
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  name: ansible-automation-platform
  namespace: ansible-automation-platform
spec:
  channel: patch-me
  installPlanApproval: Automatic
  name: ansible-automation-platform-operator
  source: redhat-operators
  sourceNamespace: openshift-marketplace
# ...
```

> [!IMPORTANT]
> When deploying multiple Operators using Red Hat OpenShift GitOps, you must create only a single Operator group in the corresponding namespace. If more than one Operator group exists in a single namespace, any CSV created in that namespace transition to a `failure` state with the `TooManyOperatorGroups` reason. After the number of Operator groups in their corresponding namespaces reaches one, all the previous `failure` state CSVs transition to `pending` state. You must manually approve the pending install plan to complete the Operator installation.

# About the respectRBAC feature

The `respectRBAC` feature in Argo CD controls how Argo CD watches resources on a cluster. By default, Argo CD attempts to watch all Kubernetes resources (CRDs) on a cluster at the cluster scope. With the `respectRBAC` feature, you can restrict the Argo CD controller from discovering or syncing specific resources using only controller RBAC, without manually configuring resource exclusions.

To enable this feature, set the `.spec.controller.respectRBAC` key in the Argo CD resource. After you set this key, the controller automatically stops watching resources it cannot list or access. For example, this prevents a situation where the Argo CD cluster role restricts Argo CD from watching OpenShift Routes, which would otherwise result in an error during synchronization, stating that it cannot watch the resource.

The `respectRBAC` feature supports the following modes:

`normal`
Provides a balance between accuracy and speed. Resource listing is a lightweight operation. Use this mode as the default when enabling `respectRBAC`.

`strict`
Increases the number of API calls to the server and is more accurate compared to `normal`. Argo CD performs additional validations of RBAC resources to determine permissions. Use this mode if Argo CD reports errors indicating that it cannot access resources when you set the value as `normal`.

## Configuring respectRBAC using the CLI

You can configure the `respectRBAC` feature by using the CLI.

<div>

<div class="title">

Prerequisites

</div>

- You have created and updated a namespace in the `Subscription` resource, so `Subscription` can host a cluster-scoped Argo CD instance. For more information, see "Using an Argo CD instance to manage cluster-scoped resources".

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create a YAML object file, for example, `argo-cd-resource.yaml`, to configure the `respectRBAC` feature:

    **Example `ArgoCD` YAML to create `respectRBAC`:**

    ``` yaml
    apiVersion: argoproj.io/v1beta1
    kind: ArgoCD
    metadata:
      name: example-argocd
    spec:
      controller:
        respectRBAC: strict
    ```

    where:

    `metadata.name`
    Specifies the specify the name of the Argo CD instance.

    `spec.controller.respectRBAC`
    Defines the value of the `spec.controller.respectRBAC` key in the `ArgoCD` resource as `normal` or `strict`. Consider setting a value as `normal` to balance accuracy and speed as resource listing is a lightweight operation. Set the value as `strict` if Argo CD reports errors indicating that it cannot access resources when you set the value as `normal`. Setting `strict` increases the number of API calls to the server and it is more accurate compared to `normal` as Argo CD performs additional validations of RBAC resources to determine permissions.

2.  Apply the changes to the YAML file by running the following command.

    ``` terminal
    $ oc apply -f argocd-resource.yaml -n argo-cd-instance
    ```

    Specify the name of the YAML file that includes the `ArgoCD` resource and the namespace that hosts `ArgoCD`.

3.  Verify that the status of the `.status.phase` field is `Available` by running the following command:

    ``` terminal
    $ oc get argocd <argocd_instance_name> -n <argocd_namespace> -o jsonpath='{.status.phase}'
    ```

    Replace `<argocd_instance_name>` with the name of your Argo CD instance for example, `example-argocd`.

4.  Verify that the `resource.respectRBAC` parameter in the `ConfigMap` resource is updated successfully:

    1.  To retrieve the contents of the `argocd-cm` config map, run the following command:

        ``` terminal
        $ oc get cm argocd-cm -n <argocd_namespace> -o yaml
        ```

    2.  Verify that the `argocd-cm` `ConfigMap` contains the `resource.respectRBAC` parameter and ensure its value is set to either `strict` or `normal`.

</div>

## Configuring respectRBAC by using the web console

You can configure `respectRBAC` in the web console.

<div>

<div class="title">

Prerequisites

</div>

- You have created and updated a namespace in the `Subscription` resource, so `Subscription` can host a cluster-scoped Argo CD instance. For more information, see "Using an Argo CD instance to manage cluster-scoped resources".

</div>

<div>

<div class="title">

Procedure

</div>

1.  Log in to the OpenShift Container Platform web console.

2.  In the **Administrator** perspective of the web console, click **Operators** → **Installed Operators**.

3.  Create or select the project where you want to install the user-defined Argo CD instance from the **Project** list.

4.  Select **Red Hat OpenShift GitOps** from the installed Operators list and click the **Argo CD** tab.

5.  Configure the `respectRBAC` parameter in the **Argo CD** tab.

    ``` yaml
    spec:
      controller:
        respectRBAC: strict
    ```

6.  Click **Create**.

    After successful installation, verify that the Argo CD instance is listed under the **Argo CD** tab and the **Status** is **Available**.

7.  After the Argo CD instance is created, verify that the `resource.respectRBAC` parameter in the `ConfigMap` resource is updated successfully by completing the following steps.

    1.  In the **Administrator** perspective, go to **Workload** → **ConfigMaps**.

    2.  In the **Project** option, select the **Argo CD** namespace.

    3.  Select the `argocd-cm` config map.

    4.  Select the **YAML** tab to view the `resource.respectRBAC` parameter.

</div>

# Additional resources

- [Installing the GitOps CLI](../installing_gitops/installing-argocd-gitops-cli.md#installing-argocd-gitops-cli)

- [Basic GitOps argocd commands](../gitops_cli_argocd/argocd-gitops-cli-reference.md#argocd-gitops-cli-reference)

- [Using an Argo CD instance to manage cluster-scoped resources](configuring-an-openshift-cluster-by-deploying-an-application-with-cluster-configurations.md#using-argo-cd-instance-to-manage-cluster-scoped-resources_configuring-an-openshift-cluster-by-deploying-an-application-with-cluster-configurations)

- [Auto respect RBAC for controller](https://argo-cd.readthedocs.io/en/stable/operator-manual/declarative-setup/#auto-respect-rbac-for-controller)
