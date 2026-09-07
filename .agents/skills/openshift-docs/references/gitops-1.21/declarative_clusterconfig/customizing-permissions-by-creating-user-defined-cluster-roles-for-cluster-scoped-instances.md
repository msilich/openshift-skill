<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

For the default cluster-scoped instance, the Red Hat OpenShift GitOps Operator grants additional permissions for managing certain cluster-scoped resources. Consequently, as a cluster administrator, when you deploy Argo CD as a cluster-scoped instance, the Operator creates additional cluster roles and cluster role bindings for the GitOps control plane components. These cluster roles and cluster role bindings provide the additional permissions that Argo CD requires to operate at the cluster level.

If you do not want the cluster-scoped instance to have all of the Operator-given permissions and choose to add or remove permissions to cluster-wide resources, you must first disable the creation of the default cluster roles for the cluster-scoped instance. Then, you can customize permissions for the following cluster-scoped instances:

- Default Argo CD instance (default cluster-scoped instance)

- User-defined cluster-scoped Argo CD instance

This guide provides instructions with examples to help you create a user-defined cluster-scoped Argo CD instance and deploy an Argo CD application in your defined namespace that contains custom configurations for your cluster. Disable the creation of the default cluster roles for the cluster-scoped instance and customize permissions for user-defined cluster-scoped instances by creating new cluster roles and cluster role bindings for the GitOps control plane components.

> [!NOTE]
> As a developer, if you are creating an Argo CD application and deploying cluster-wide resources, ensure that your cluster administrator grants the necessary permissions.

Otherwise, after the Argo CD reconciliation, you will see an authentication error message in the application’s `Status` field similar to the following example:

**Example authentication error message:**

``` terminal
persistentvolumes is forbidden: User "system:serviceaccount:gitops-demo:argocd-argocd-application-controller" cannot create resource "persistentvolumes" in API group "" at the cluster scope.
```

# Prerequisites

- You have installed Red Hat OpenShift GitOps 1.13.0 or a later version on your OpenShift Container Platform cluster.

- You have installed the OpenShift CLI (`oc`).

- You have installed the Red Hat OpenShift GitOps `argocd` CLI.

- You have installed a [cluster-scoped Argo CD instance](configuring-an-openshift-cluster-by-deploying-an-application-with-cluster-configurations.md#using-argo-cd-instance-to-manage-cluster-scoped-resources_configuring-an-openshift-cluster-by-deploying-an-application-with-cluster-configurations) in your defined namespace, for example, the `spring-petclinic` namespace.

- You have validated that the user-defined cluster-scoped instance is configured with the cluster roles and cluster role bindings for the following components:

  - Argo CD Application Controller

  - Argo CD server

  - Argo CD `ApplicationSet` Controller (provided the `ApplicationSet` Controller is created)

- You have deployed a `cluster-configs` [Argo CD application](configuring-an-openshift-cluster-by-deploying-an-application-with-cluster-configurations.md#creating-an-application-by-using-the-argo-cd-dashboard_configuring-an-openshift-cluster-by-deploying-an-application-with-cluster-configurations) with the `customclusterrole` [path](https://github.com/redhat-developer/openshift-gitops-getting-started/tree/main/customclusterrole) in the `spring-petclinic` namespace and created the `test-gitops-ns` namespace and `test-gitops-pv` persistent volume resources.

  > [!NOTE]
  > The `cluster-configs` Argo CD application must be managed by a user-defined cluster-scoped instance with the following parameters set:
  >
  > - The `selfHeal` field value set to `true`
  >
  > - The `syncPolicy` field value set to `automated`
  >
  > - The **Label** field set to the `app.kubernetes.io/part-of=argocd` value
  >
  > - The **Label** field set to the `argocd.argoproj.io/managed-by=<user_defined_namespace>` value so that the Argo CD instance in your defined namespace can manage your namespace
  >
  > - The **Label** field set to the `app.kubernetes.io/name=<user_defined_argocd_instance>` value

# Disabling the creation of the default cluster roles for the cluster-scoped instance

To add or remove permissions to cluster-wide resources, as needed, you must disable the creation of the default cluster roles for the cluster-scoped instance by editing the YAML file of the Argo CD custom resource (CR).

<div>

<div class="title">

Procedure

</div>

1.  In the Argo CD CR, set the value of the `.spec.defaultClusterScopedRoleDisabled` field to `true`:

    **Example Argo CD CR:**

    ``` yaml
    apiVersion: argoproj.io/v1beta1
    kind: ArgoCD
    metadata:
      name: example
      namespace: spring-petclinic
    # ...
    spec:
      defaultClusterScopedRoleDisabled: true
    # ...
    ```

    where:

    `metadata.name`
    Specifies the name of the cluster-scoped instance.

    `metadata.namespace`
    Specifies the namespace where you want to run the cluster-scoped instance.

    `spec.defaultClusterScopedRoleDisabled`
    Specifies the flag value that disables the creation of the default cluster roles for the cluster-scoped instance. If you want the Operator to recreate the default cluster roles and cluster role bindings for the cluster-scoped instance, set the field value to `false`.

    **Sample output:**

    ``` terminal
    argocd.argoproj.io/example configured
    ```

2.  Verify that the Red Hat OpenShift GitOps Operator has deleted the default cluster roles and cluster role bindings for the GitOps control plane components by running the following commands:

    ``` terminal
    $ oc get ClusterRoles/<argocd_name>-<argocd_namespace>-<control_plane_component>
    ```

    ``` terminal
    $ oc get ClusterRoleBindings/<argocd_name>-<argocd_namespace>-<control_plane_component>
    ```

    **Sample output:**

    ``` terminal
    No resources found
    ```

    The default cluster roles and cluster role bindings for the cluster-scoped instance are deleted. As a cluster administrator, you can now create and customize permissions for cluster-scoped instances by creating new cluster roles and cluster role bindings for the GitOps control plane components.

</div>

# Additional resources

- [Installing a user-defined Argo CD instance](../argocd_instance/setting-up-argocd-instance.md#setting-up-argocd-instance)

# Customizing permissions for cluster-scoped instances

As a cluster administrator, to customize permissions for cluster-scoped instances, you must create new cluster roles and cluster role bindings for the GitOps control plane components.

For example purposes, the following instructions focus only on user-defined cluster-scoped instances.

<div>

<div class="title">

Procedure

</div>

1.  Open the **Administrator** perspective of the web console and go to **User Management** → **Roles** → **Create Role**.

2.  Use the following `ClusterRole` YAML template to add rules to specify the additional permissions.

    **Example cluster role YAML template:**

    ``` yaml
    apiVersion: rbac.authorization.k8s.io/v1
    kind: ClusterRole
    metadata:
      name: example-spring-petclinic-argocd-application-controller
    rules:
      - verbs:
          - get
          - list
          - watch
        apiGroups:
          - '*'
        resources:
          - '*'
      - verbs:
          - '*'
        apiGroups:
          - ''
        resources:
          - namespaces
          - persistentvolumes
    ```

    where:

    `metadata.name`
    Specifies the name of the cluster role according to the \<argocd_name\>-\<argocd_namespace\>-\<control_plane_component\> naming convention.

    `rules`
    Specifies the resources to which you want to grant permissions at the cluster level.

3.  Click **Create** to add the cluster role.

4.  Find the service account used by the control plane component you are customizing permissions for by performing the following steps:

    1.  Go to **Workloads** → **Pods**.

    2.  From the **Project** list, select the project where the user-defined cluster-scoped instance is installed.

    3.  Click the pod of the control plane component and go to the **YAML** tab.

    4.  Find the value of the `spec.ServiceAccountName` field.

5.  Go to **User Management** → **RoleBindings** → **Create binding**.

6.  Click **Create binding**.

7.  Select **Binding type** as **Cluster-wide role binding (ClusterRoleBinding)**.

8.  Enter a unique value for **RoleBinding name** by following the \<argocd_name\>-\<argocd_namespace\>-\<control_plane_component\> naming convention.

9.  Select the newly created cluster role from the drop-down list for **Role name**.

10. Select the **Subject** as **ServiceAccount** and then provide the **Subject namespace** and **name**.

    1.  **Subject namespace**: `spring-petclinic`

    2.  **Subject name**: `example-argocd-application-controller`

        > [!NOTE]
        > For **Subject name**, ensure that the value you configure is the same as the value of the `spec.ServiceAccount` field of the control plane component you are customizing permissions for.

11. Click **Create**.

    You have created the required permissions for the control plane component’s service account in the specified namespace.. The YAML file for the `ClusterRoleBinding` object looks similar to the following example:

    **Example YAML file for a cluster role binding:**

    ``` yaml
    kind: ClusterRoleBinding
    apiVersion: rbac.authorization.k8s.io/v1
    metadata:
      name: example-spring-petclinic-argocd-application-controller
    subjects:
      - kind: ServiceAccount
        name: example-argocd-application-controller
        namespace: spring-petclinic
    roleRef:
      apiGroup: rbac.authorization.k8s.io
      kind: ClusterRole
      name: example-spring-petclinic-argocd-application-controller
    ```

</div>

# Additional resources

- [Adding permissions for cluster configuration](configuring-an-openshift-cluster-by-deploying-an-application-with-cluster-configurations.md#gitops-additional-permissions-for-cluster-config_configuring-an-openshift-cluster-by-deploying-an-application-with-cluster-configurations)

- [Configuring common cluster roles by specifying user-defined cluster roles for namespace-scoped instances](../argocd_instance/setting-up-argocd-instance.md#gitops-configuring-common-cluster-roles-by-specifying-user-defined-cluster-roles-for-namespace-scoped-instances_setting-up-argocd-instance)

- [Customizing permissions by creating aggregated cluster roles](customizing-permissions-by-creating-aggregated-cluster-roles.md#customizing-permissions-by-creating-aggregated-cluster-roles)
