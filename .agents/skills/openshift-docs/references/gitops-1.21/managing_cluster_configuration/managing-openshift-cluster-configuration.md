<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

As an administrator, maintaining the stability and consistency of an OpenShift Container Platform environment requires a move away from traditionally manual configurations toward automated, declarative management. Red Hat OpenShift GitOps enables you to use Git repositories as the foundation for your infrastructure and application definitions. With Red Hat OpenShift GitOps, you can manage your OpenShift Container Platform cluster configuration for the following benefits:

- Version control and auditability: Configuration changes committed to Git provide a complete history of modifications. This helps auditing, compliance, and accountability.

- Single source of truth: Git serves as the definitive source for the desired state of your OpenShift Container Platform cluster.

- Optimized performance and disaster recovery: GitOps points the Argo CD application to the previous commit or tag with a known-good state in Git, which in turn reduces downtime and helps with disaster recovery.

- Collaboration and Review: Git’s collaborative features enable team members to review and approve infrastructure and application configuration changes before they are applied to your OpenShift Container Platform cluster.

- Efficiency and Scalability: GitOps streamlines the deployment and operations workflows, enabling efficient management of complex and multi-cluster environments with reduced manual intervention and human error.

Perform the following tasks to manage your OpenShift Container Platform cluster configuration:

1.  Installing the Red Hat OpenShift GitOps Operator using CLI

2.  Analyzing the default Argo CD instance

3.  Accessing the default Argo CD instance

4.  Configuring the default Argo CD instance

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

# Analyzing the default Argo CD instance details

By default, the Operator creates an Argo CD instance in the `openshift-gitops` namespace. After installation, you can use the OpenShift Container Platform web console to view the **Operator details** page and analyze the default instance configuration. This analysis helps you to customize the behavior of this instance later. The instance is intended for the cluster configuration use case and has elevated privileges.

> [!NOTE]
> You can create additional Argo CD instances in other namespaces to support your application use cases.

<div>

<div class="title">

Prerequisite

</div>

- You have your login credentials to access the OpenShift Container Platform cluster with `cluster-admin` privileges.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Perform one of the following steps to open the **Operator details** page:

    - Click the **View Operator** button that is available after the Operator installation completes.

    - Click **Installed Operators** under the **Operators** menu, and select the **Red Hat OpenShift GitOps** Operator.

2.  Select the **Argo CD** tab.

3.  Click the name of the default instance, `openshift-gitops`, to view its details on a new page.

4.  Select the **YAML** tab to analyze how it is configured.

</div>

# Access the default Argo CD instance

After analyzing the default Argo CD instance details, you can access it through the Argo CD UI to check whether it is available for use.

<div>

<div class="title">

Prerequisite

</div>

- You have your login credentials to access the OpenShift Container Platform cluster with `cluster-admin` privileges.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Click the **Application Launcher** menu in the top right corner of the OpenShift Container Platform web console.

2.  Select **Cluster Argo CD** from the dropdown list. The Argo CD login page opens.

3.  Click the **LOG IN VIA OPENSHIFT** button. The OpenShift Container Platform login page opens.

4.  Enter your OpenShift Container Platform credentials. The **Authorize Access** page opens.

5.  Click **Allow selected permissions** to provide requested permission. The Argo CD UI page opens.

</div>

At this point, the UI is empty as you have not created any Argo CD applications. You can check the **User Info** page to view the user details.

# Configuring the default Argo CD instance

Though the Operator creates a default Argo CD instance in the `openshift-gitops` namespace, you must configure it to make it useful for deploying applications and setting cluster configuration:

- Configure Role Based Access Control (RBAC): Argo CD uses its own RBAC configuration. The default permissions configured by the Operator might not be sufficient, depending on the OpenShift Container Platform cluster groups your user has been assigned to.

- Configure permissions: The Operator configures the default instance with a default set of Kubernetes permissions. However, these permissions are insufficient when deploying applications in the real-time environment. Therefore, ensure to provide additional permissions to this default instance.

## Configuring RBAC

You must configure RBAC to provide the sufficient access to the users to work with the default instance.

The `defaultPolicy` of the instance is an empty string, which means no role is assigned automatically. Though users can log into the instance, they have no permissions to view anything or perform any tasks in the Argo CD UI or CLI.

The instance includes the following two groups:

- `system:cluster-admins`: The group only applies to the temporary `kube-admin` credentials and can be ignored.

- `cluster-admins`: You can add your user to this group to enable them to perform tasks, such as deploying an application, in the Argo CD web console.

> [!NOTE]
> *Restrict default permissions:*
>
> Ensure that you always use either an empty string or a deny-all type of role for the `defaultPolicy` parameter because permissions granted in it cannot be revoked. Hence, it is not recommended to set the `defaultPolicy` parameter in a way that grants permissions.

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

1.  View the Operator-configured RBAC for the default instance:

    ``` terminal
    $ oc get argocd openshift-gitops -n openshift-gitops -o=jsonpath='{.spec.rbac}'
    ```

    **Example Output:**

    ``` json
    {"defaultPolicy":"","policy":"g, system:cluster-admins, role:admin\ng, cluster-admins, role:admin\n","scopes":"[groups]"}
    ```

2.  Check if the `cluster-admins` group exists:

    ``` terminal
    $ oc get groups
    ```

3.  Perform one of the following steps:

    - If the group does not exist, create it and add your user to it:

      ``` terminal
      $ oc adm groups new cluster-admins <user>
      ```

      where:

      \<user\>
      Denotes the user that you want to add to the group.

      **Example Output:**

      ``` terminal
      group.user.openshift.io/cluster-admins created
      ```

    - If the group exists, check if your user is part of it in the output of the previously run `oc get groups` command. If your user is not in the group, add your user to the group:

      ``` terminal
      $ oc adm groups add-users cluster-admins <user>
      ```

      where:

      \<user\>
      Denotes the user that you want to add to the group.

      ``` terminal
      $ oc adm groups add-users cluster-admins jane.doe
      ```

      <div class="formalpara">

      <div class="title">

      Example output

      </div>

      ``` terminal
      group.user.openshift.io/cluster-admins added: "jane.doe"
      ```

      </div>

</div>

<div>

<div class="title">

Verification

</div>

- Validate that the group `cluster-admins` exists and that your user is part of it:

  ``` terminal
  $ oc get groups cluster-admins
  ```

  The output shows the `cluster-admins` group with your user assigned to it.

  > [!IMPORTANT]
  > After creating or editing the `cluster-admins` group, ensure you log out of the Argo CD web console and then log back in again so that the group becomes associated with your user. Check the **User Info** page to validate that your user is part of the `cluster-admins` group within Argo CD.

</div>

## Configuring permissions

Though the default Argo CD instance is automatically configured with a default set of Kubernetes permissions, you need to provide it with additional permissions to deploy all the resources required for cluster configuration. Conversely, if you need to set more restrictive permissions for the default instance to deploy only specific resources, you can do so through additional configurations.

> [!NOTE]
> For more information about the default set of Kubernetes permissions, see "Additional resources".

When using the default instance for cluster configuration, provide the `cluster-admin` permissions to the Argo CD application controller service account. To do this, you can create a `ClusterRoleBinding` object for the `openshift-gitops-argocd-application-controller` service account as the default instance uses this account for interacting with the Kubernetes API to deploy resources.

<div>

<div class="title">

Prerequisite

</div>

- You have your login credentials to access the OpenShift Container Platform cluster with `cluster-admin` privileges.

- You have installed the [`oc` CLI](https://docs.redhat.com/en/documentation/openshift_container_platform/latest/html/cli_tools/openshift-cli-oc).

</div>

<div>

<div class="title">

Procedure

</div>

- Run the following command:

  ``` terminal
  $ oc adm policy add-cluster-role-to-user --rolebinding-name="openshift-gitops-cluster-admin" cluster-admin -z openshift-gitops-argocd-application-controller -n openshift-gitops
  ```

  **Example output:**

  ``` terminal
  clusterrole.rbac.authorization.k8s.io/cluster-admin added: "openshift-gitops-argocd-application-controller"
  ```

</div>

<div>

<div class="title">

Verification

</div>

- View the created `ClusterRoleBinding` object:

  ``` terminal
  $ oc get clusterrolebinding openshift-gitops-cluster-admin -o yaml
  ```

  **Example output:**

  ``` yaml
  apiVersion: rbac.authorization.k8s.io/v1
  kind: ClusterRoleBinding
  metadata:
    name: openshift-gitops-cluster-admin
  roleRef:
    apiGroup: rbac.authorization.k8s.io
    kind: ClusterRole
    name: cluster-admin
  subjects:
    - kind: ServiceAccount
      name: openshift-gitops-argocd-application-controller
      namespace: openshift-gitops
  ```

</div>

# Additional resources

- [Installing a user-defined Argo CD instance](../argocd_instance/setting-up-argocd-instance.md#gitops-argo-cd-installation_setting-up-argocd-instance)

- [Installing GitOps in web console](../installing_gitops/installing-openshift-gitops.md#installing-gitops-operator-in-web-console_installing-openshift-gitops)

- [Default set of Kubernetes permissions](../declarative_clusterconfig/configuring-an-openshift-cluster-by-deploying-an-application-with-cluster-configurations.md#gitops-inbuilt-permissions-for-cluster-config_configuring-an-openshift-cluster-by-deploying-an-application-with-cluster-configurations)

- [Config Management Plugins](https://argo-cd.readthedocs.io/en/stable/operator-manual/config-management-plugins/#config-management-plugins)
