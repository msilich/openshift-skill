<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

The default cluster role for the Argo CD Application Controller has a specific set of hard-coded permissions. The Red Hat OpenShift GitOps Operator manages this cluster role, so you cannot modify it. As a cluster administrator, you can customize the permissions by using any one of the following methods:

- [Creating user-defined cluster roles](customizing-permissions-by-creating-user-defined-cluster-roles-for-cluster-scoped-instances.md#customizing-permissions-by-creating-user-defined-cluster-roles-for-cluster-scoped-instances)

- [Creating aggregated cluster roles](customizing-permissions-by-creating-aggregated-cluster-roles.md#gitops-creating-aggregated-cluster-roles_customizing-permissions-by-creating-aggregated-cluster-roles)

# Aggregated cluster roles

By using aggregated cluster roles, you do not have to define permissions by creating new cluster roles from scratch. Instead, you can combine several cluster roles into a single one.

With Red Hat OpenShift GitOps 1.14 and later, as a cluster administrator, you can use aggregated cluster roles so that users can easily add user-defined permissions for Argo CD Application Controller.

<div class="important">

<div class="title">

</div>

- The aggregated cluster roles functionality is optional and disabled by default. You can create aggregated cluster roles only for the Argo CD Application Controller component of a cluster-scoped Argo CD instance.

- Deleting the `aggregatedClusterRoles` field from the Argo CD custom resource (CR) does not delete the user-defined cluster role. You must manually delete the user-defined cluster role using the CLI or UI.

</div>

# Prerequisites

- You understand [aggregated cluster roles](https://kubernetes.io/docs/reference/access-authn-authz/rbac/#aggregated-clusterroles).

- You have installed Red Hat OpenShift GitOps on your OpenShift Container Platform cluster.

- You have installed the OpenShift CLI (`oc`).

- You have installed the Red Hat OpenShift GitOps `argocd` CLI.

- You have installed a [cluster-scoped Argo CD instance](configuring-an-openshift-cluster-by-deploying-an-application-with-cluster-configurations.md#using-argo-cd-instance-to-manage-cluster-scoped-resources_configuring-an-openshift-cluster-by-deploying-an-application-with-cluster-configurations) in your defined namespace.

- You have validated that the user-defined cluster-scoped instance is configured with the cluster roles and cluster role bindings for the following components:

  - Argo CD Application Controller

  - Argo CD server

  - Argo CD `ApplicationSet` Controller, if `ApplicationSet` Controller is created

- You have [disabled the creation of the default cluster roles](customizing-permissions-by-creating-user-defined-cluster-roles-for-cluster-scoped-instances.md#gitops-disabling-the-creation-of-the-default-cluster-roles-for-the-cluster-scoped-instance_customizing-permissions-by-creating-user-defined-cluster-roles-for-cluster-scoped-instances) for the cluster-scoped instance.

# Creating aggregated cluster roles

The process of creating aggregated cluster roles consists of the following procedures:

1.  Enabling the creation of aggregated cluster roles

2.  Creating user-defined cluster roles and configuring user-defined permissions for Application Controller

## Enable the creation of aggregated cluster roles

You can enable the creation of aggregated cluster roles by setting the value of the `.spec.aggregatedClusterRoles` field to `true` in the Argo CD custom resource (CR). When you enable the creation of aggregated cluster roles, the Red Hat OpenShift GitOps Operator takes the following actions:

- Creates an `<argocd_name>-<argocd_namespace>-argocd-application-controller` aggregated cluster role with a predefined `aggregationRule` field by default.

- Creates a corresponding cluster role binding and manages it.

- Creates and manages `view` and `admin` cluster roles for Application Controller to add user-defined permissions into the aggregated cluster role.

## Create user-defined cluster roles and configure user-defined permissions

To configure user-defined permissions into the `<argocd_name>-<argocd_namespace>-argocd-application-controller-admin` cluster role and aggregated cluster role, you must create one or more user-defined cluster roles with the `argocd/aggregate-to-admin: 'true'` label and then configure the user-defined permissions for Application Controller.

<div class="note">

<div class="title">

</div>

- The aggregated cluster role inherits permissions from the `<argocd_name>-<argocd_namespace>-argocd-application-controller-admin` and `<argocd_name>-<argocd_namespace>-argocd-application-controller-view` cluster roles.

- The `<argocd_name>-<argocd_namespace>-argocd-application-controller-admin` cluster role inherits permissions from the user-defined cluster role.

</div>

# Enabling the creation of aggregated cluster roles

To enable the creation of aggregated cluster roles for the Argo CD Application Controller component of a cluster-scoped Argo CD instance, you must configure the corresponding field by editing the YAML file of the Argo CD custom resource (CR).

<div>

<div class="title">

Procedure

</div>

1.  In the Argo CD CR, set the value of the `.spec.aggregatedClusterRoles` field to `true`:

    **Example Argo CD CR:**

    ``` yaml
    apiVersion: argoproj.io/v1beta1
    kind: ArgoCD
    metadata:
      name: example
      namespace: spring-petclinic
    # ...
    spec:
      aggregatedClusterRoles: true
    # ...
    ```

    where:

    `metadata.name`
    Specifies the name of the cluster-scoped instance.

    `metadata.namespace`
    Specifies the namespace where Argo CD is installed.

    `spec.aggregatedClusterRoles`
    Specifies the value of the cluster roles to enable the creation of aggregated cluster roles. If you do not want to enable the creation of aggregated cluster roles, either do not include this line or set the value to `false`.

    **Example output:**

    ``` terminal
    argocd.argoproj.io/example configured
    ```

2.  Verify that the `Status` field of the cluster-scoped Argo CD instance shows as `Phase: Available` by running the following command:

    ``` terminal
    $ oc describe argocd.argoproj.io/example -n spring-petclinic
    ```

    **Example output:**

    ``` terminal
    Name:         example
    Namespace:    spring-petclinic
    Labels:       <none>
    Annotations:  <none>
    API Version:  argoproj.io/v1beta1
    Kind:         ArgoCD
    Metadata:
      Creation Timestamp:  2024-08-14T08:20:53Z
      Finalizers:
        argoproj.io/finalizer
      Generation:        3
      Resource Version:  60437
      UID:               57940e54-d60b-4c1a-bc4a-85c81c63ab69
    Spec:
      Aggregated Cluster Roles:  true
    ...
    Status:
      Application Controller:      Running
      Application Set Controller:  Unknown
      Phase:                       Available
      Redis:                       Running
      Repo:                        Running
      Server:                      Running
      Sso:                         Unknown
    Events:                        <none>
    ```

    The `Available` status indicates that the cluster-scoped Argo CD instance is healthy and available.

    > [!NOTE]
    > The Red Hat OpenShift GitOps Operator creates the following default cluster roles and manages them:
    >
    > - `<argocd_name>-<argocd_namespace>-argocd-application-controller` aggregated cluster role
    >
    > - `<argocd_name>-<argocd_namespace>-argocd-application-controller-view`
    >
    > - `<argocd_name>-<argocd_namespace>-argocd-application-controller-admin`

3.  Verify that the Operator has created the default cluster roles and cluster role bindings for the Argo CD Application Controller and Argo CD server components by running the following commands:

    ``` terminal
    $ oc get ClusterRoles -l app.kubernetes.io/part-of=argocd
    ```

    **Example output:**

    ``` terminal
    NAME                                                           CREATED AT
    example-spring-petclinic-argocd-application-controller         2024-08-14T08:20:58Z
    example-spring-petclinic-argocd-application-controller-admin   2024-08-14T09:08:38Z
    example-spring-petclinic-argocd-application-controller-view    2024-08-14T09:08:38Z
    example-spring-petclinic-argocd-server                         2024-08-14T08:20:59Z
    ```

    ``` terminal
    $ oc get ClusterRoleBindings -l app.kubernetes.io/part-of=argocd
    ```

    **Example output:**

    ``` terminal
    NAME                                                     ROLE                                                                 AGE
    example-spring-petclinic-argocd-application-controller   ClusterRole/example-spring-petclinic-argocd-application-controller   54m
    example-spring-petclinic-argocd-server                   ClusterRole/example-spring-petclinic-argocd-server                   54m
    ```

    The cluster role bindings for the `view` and `admin` cluster roles are not created. This is because the `view` and `admin` cluster roles only add permissions to the aggregated cluster role and do not directly configure permissions to the Argo CD Application Controller.

    > [!TIP]
    > Alternatively, you can use the OpenShift Container Platform web console to verify from the **Administrator** perspective. You can go to **User Management** → **Roles** and **User Management** → **RoleBindings**, respectively. You can search for the cluster roles and cluster role bindings that have the `app.kubernetes.io/part-of:argocd` label.

4.  Verify that the aggregated cluster role is created by running the following command to check the role permissions:

    ``` terminal
    $ oc get ClusterRole/<cluster_role_name> -o yaml
    ```

    where:

    `<cluster_role_name>`
    Specifies the name of the role created.

    **Example output of the aggregated cluster role:**

    ``` terminal
    apiVersion: rbac.authorization.k8s.io/v1
    kind: ClusterRole
    metadata:
      annotations:
        argocds.argoproj.io/name: example
        argocds.argoproj.io/namespace: spring-petclinic
        kubectl.kubernetes.io/last-applied-configuration: |
          {"apiVersion":"argoproj.io/v1beta1","kind":"ArgoCD","metadata":{"annotations":{},"name":"example","namespace":"spring-petclinic"},"spec":{"aggregatedClusterRoles":true}}
        rbac.authorization.kubernetes.io/autoupdate: "true"
      creationTimestamp: "2024-08-14T08:20:58Z"
      labels:
        app.kubernetes.io/managed-by: spring-petclinic
        app.kubernetes.io/name: example
        app.kubernetes.io/part-of: argocd
      name: example-spring-petclinic-argocd-application-controller
      resourceVersion: "78640"
      uid: aeeb2ef5-b531-4fe3-a61a-b5ad8dd8ca6e
    aggregationRule:
      clusterRoleSelectors:
      - matchLabels:
          app.kubernetes.io/managed-by: spring-petclinic
          argocd/aggregate-to-controller: "true"
    rules: []
    ```

    where:

    `metadata.name`
    Specifies the name of the aggregated cluster role.

    `aggregationRule.clusterRoleSelectors`
    Specifies the predefined list of labels. This indicates that the aggregated cluster role can inherit permissions from the other user-defined cluster roles.

    `rules`
    Specifies the predefined permissions. However, when the Operator immediately creates a `<argocd_name>-<argocd_namespace>-argocd-application-controller-view` cluster role, the corresponding predefined `view` permissions are added into the aggregated cluster role.

    **Example output of the `view` cluster role:**

    ``` terminal
    apiVersion: rbac.authorization.k8s.io/v1
    kind: ClusterRole
    metadata:
      annotations:
        argocds.argoproj.io/name: example
        argocds.argoproj.io/namespace: spring-petclinic
        kubectl.kubernetes.io/last-applied-configuration: |
          {"apiVersion":"argoproj.io/v1beta1","kind":"ArgoCD","metadata":{"annotations":{},"name":"example","namespace":"spring-petclinic"},"spec":{"aggregatedClusterRoles":true}}
      creationTimestamp: "2024-08-14T09:59:14Z"
      labels:
        app.kubernetes.io/managed-by: spring-petclinic
        app.kubernetes.io/name: example
        app.kubernetes.io/part-of: argocd
        argocd/aggregate-to-controller: "true"
      name: example-spring-petclinic-argocd-application-controller-view
      resourceVersion: "78639"
      uid: 068b8867-7a0c-4af3-a17a-0560a00eba41
    rules:
    - apiGroups:
      - '*'
      resources:
      - '*'
      verbs:
      - get
      - list
      - watch
    - nonResourceURLs:
      - '*'
      verbs:
      - get
      - list
    ```

    where:

    `metadata.labels`
    Defines the labels to match the predefined list of an existing aggregated cluster role.

    `metadata.name`
    Specifies the name of the `view` cluster role.

    `rules`
    Specifies the predefined `view` permissions. These permissions are added into the existing aggregated cluster role.

    **Example output of the `admin` cluster role:**

    ``` terminal
    apiVersion: rbac.authorization.k8s.io/v1
    kind: ClusterRole
    metadata:
      annotations:
        argocds.argoproj.io/name: example
        argocds.argoproj.io/namespace: spring-petclinic
        kubectl.kubernetes.io/last-applied-configuration: |
          {"apiVersion":"argoproj.io/v1beta1","kind":"ArgoCD","metadata":{"annotations":{},"name":"example","namespace":"spring-petclinic"},"spec":{"aggregatedClusterRoles":true}}
        rbac.authorization.kubernetes.io/autoupdate: "true"
      creationTimestamp: "2024-08-14T09:59:15Z"
      labels:
        app.kubernetes.io/managed-by: spring-petclinic
        app.kubernetes.io/name: example
        app.kubernetes.io/part-of: argocd
        argocd/aggregate-to-controller: "true"
      name: example-spring-petclinic-argocd-application-controller-admin
      resourceVersion: "78642"
      uid: e2d35b6f-0832-4993-8b24-915a725454f9
    aggregationRule:
      clusterRoleSelectors:
      - matchLabels:
          app.kubernetes.io/managed-by: spring-petclinic
          argocd/aggregate-to-admin: "true"
    rules: null
    ```

    where:

    `metadata.labels`
    Specifies the labels to match the predefined list of an existing aggregated cluster role.

    `metadata.name`
    Specifies the name of the `admin` cluster role.

    `aggregationRule.clusterRoleSelectors`
    Specifies the predefined list of labels. This indicates that the existing `<argocd_name>-<argocd_namespace>-argocd-application-controller-admin` cluster role can inherit permissions from the other user-defined cluster roles.

    `rules`
    Specifies that no permissions are defined yet in one or more user-defined cluster roles.

    > [!TIP]
    > Alternatively, you can use the OpenShift Container Platform web console to verify from the **Administrator** perspective. You can go to **User Management** → **Roles**, use the **Filter** option, select **Cluster-wide Roles**, and search for the aggregated cluster role, `view`, and `admin` cluster roles. You must open the cluster role to check the details and configurations.

    As a cluster administrator, you can now create one or more user-defined cluster roles and configure user-defined permissions for Argo CD Application Controller.

</div>

# Additional resources

- [Installing a user-defined Argo CD instance](../argocd_instance/setting-up-argocd-instance.md#setting-up-argocd-instance)

# Creating user-defined cluster roles and configuring user-defined permissions for Application Controller

As a cluster administrator, to add user-defined permissions to your aggregated cluster role, you must create one or more user-defined cluster roles and then configure the user-defined permissions for the Argo CD Application Controller component of a cluster-scoped Argo CD instance.

<div>

<div class="title">

Prerequisites

</div>

- You have enabled the creation of aggregated cluster roles for the Argo CD Application Controller component of a cluster-scoped Argo CD instance.

- You have the following default cluster roles that are created and managed by the Red Hat OpenShift GitOps Operator:

  - `<argocd_name>-<argocd_namespace>-argocd-application-controller` aggregated cluster role with a predefined `aggregationRule` field

  - `<argocd_name>-<argocd_namespace>-argocd-application-controller-view` with predefined `view` permissions

  - `<argocd_name>-<argocd_namespace>-argocd-application-controller-admin` with no predefined permissions

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create a new cluster role with the required labels and permissions by using the following command:

    ``` terminal
    $ oc apply -n <namespace> -f <cluster_role_name>.yaml
    ```

    where:

    `<namespace>`
    Specifies the name of your defined namespace.

    `<cluster_role_name>`
    Specifies the name of your defined cluster role YAML file.

    **Example user-defined cluster role YAML:**

    ``` yaml
    apiVersion: rbac.authorization.k8s.io/v1
    kind: ClusterRole
    metadata:
      name: user-application-controller
      labels:
        app.kubernetes.io/managed-by: spring-petclinic
        app.kubernetes.io/name: example
        app.kubernetes.io/part-of: argocd
        argocd/aggregate-to-admin: 'true'
    rules:
      - verbs:
          - '*'
        apiGroups:
          - ''
        resources:
          - namespaces
          - persistentvolumeclaims
          - persistentvolumes
          - configmaps
      - verbs:
          - '*'
        apiGroups:
          - compliance.openshift.io
        resources:
          - scansettingbindings
    ```

    where:

    `metadata.name`
    Specifies the name of the user-defined cluster role.

    `metadata.labels.argocd/aggregate-to-admin`
    Specifies that the cluster role is aggregated into the Argo CD Application Controller admin cluster role, allowing the permissions defined in this role to be included automatically.

    `rules`
    Specifies the list of permissions granted by the cluster role, including allowed API groups, resources, and verbs.

    > [!TIP]
    > Alternatively, you can use the web console to create a user-defined cluster role from the **Administrator** perspective. You can go to **User Management** → **Roles** → **Create Role**, use the preceding YAML template to add permissions, and click **Create**.

    **Example output:**

    ``` terminal
    clusterrole.rbac.authorization.k8s.io/user-application-controller created
    ```

    A user-defined cluster role is created.

2.  Verify that the `<argocd_name>-<argocd_namespace>-argocd-application-controller-admin` cluster role inherits permissions from the user-defined cluster role by running the following command:

    ``` terminal
    $ oc get ClusterRole/<argocd_name>-<argocd_namespace>-argocd-application-controller-admin -o yaml
    ```

    where:

    `<argocd_name>`
    Specifies the name of your user-defined cluster-scoped Argo CD instance.

    `<argocd_namespace>`
    Specifies the namespace where Argo CD is installed.

    **Example output:**

    ``` terminal
    aggregationRule:
      clusterRoleSelectors:
      - matchLabels:
          app.kubernetes.io/managed-by: spring-petclinic
          argocd/aggregate-to-admin: "true"
    apiVersion: rbac.authorization.k8s.io/v1
    kind: ClusterRole
    metadata:
      annotations:
        argocds.argoproj.io/name: example
        argocds.argoproj.io/namespace: spring-petclinic
        kubectl.kubernetes.io/last-applied-configuration: |
          {"apiVersion":"argoproj.io/v1beta1","kind":"ArgoCD","metadata":{"annotations":{},"name":"example","namespace":"spring-petclinic"},"spec":{"aggregatedClusterRoles":true}}
      creationTimestamp: "2024-08-14T09:59:15Z"
      labels:
        app.kubernetes.io/managed-by: spring-petclinic
        app.kubernetes.io/name: example
        app.kubernetes.io/part-of: argocd
        argocd/aggregate-to-controller: "true"
      name: example-spring-petclinic-argocd-application-controller-admin
      resourceVersion: "79202"
      uid: e2d35b6f-0832-4993-8b24-915a725454f9
    rules:
    - apiGroups:
      - ""
      resources:
      - namespaces
      - persistentvolumeclaims
      - persistentvolumes
      - configmaps
      verbs:
      - '*'
    - apiGroups:
      - compliance.openshift.io
      resources:
      - scansettingbindings
      verbs:
      - '*'
    ```

    > [!TIP]
    > Alternatively, you can use the OpenShift Container Platform web console to verify from the **Administrator** perspective. You can go to **User Management** → **Roles**, use the **Filter** option, select **Cluster-wide Roles**, and search for the `<argocd_name>-<argocd_namespace>-argocd-application-controller-admin` cluster role. You must open the cluster role to check the details and configurations.

3.  Verify that the `<argocd_name>-<argocd_namespace>-argocd-application-controller` aggregated cluster role inherits permissions from the `<argocd_name>-<argocd_namespace>-argocd-application-controller-admin` and `<argocd_name>-<argocd_namespace>-argocd-application-controller-view` cluster roles by running the following command:

    ``` terminal
    $ oc get ClusterRole/<argocd_name>-<argocd_namespace>-argocd-application-controller -o yaml
    ```

    where:

    `<argocd_name>`
    Specifies the name of your user-defined cluster-scoped Argo CD instance.

    `<argocd_namespace>`
    Specifies the namespace where Argo CD is installed.

    **Example output of the aggregated cluster role:**

    ``` terminal
    aggregationRule:
      clusterRoleSelectors:
      - matchLabels:
          app.kubernetes.io/managed-by: spring-petclinic
          argocd/aggregate-to-controller: "true"
    apiVersion: rbac.authorization.k8s.io/v1
    kind: ClusterRole
    metadata:
      annotations:
        argocds.argoproj.io/name: example
        argocds.argoproj.io/namespace: spring-petclinic
        kubectl.kubernetes.io/last-applied-configuration: |
          {"apiVersion":"argoproj.io/v1beta1","kind":"ArgoCD","metadata":{"annotations":{},"name":"example","namespace":"spring-petclinic"},"spec":{"aggregatedClusterRoles":true}}
        rbac.authorization.kubernetes.io/autoupdate: "true"
      creationTimestamp: "2024-08-14T08:20:58Z"
      labels:
        app.kubernetes.io/managed-by: spring-petclinic
        app.kubernetes.io/name: example
        app.kubernetes.io/part-of: argocd
      name: example-spring-petclinic-argocd-application-controller
      resourceVersion: "79203"
      uid: aeeb2ef5-b531-4fe3-a61a-b5ad8dd8ca6e
    rules:
    - apiGroups:
      - ""
      resources:
      - namespaces
      - persistentvolumeclaims
      - persistentvolumes
      - configmaps
      verbs:
      - '*'
    - apiGroups:
      - compliance.openshift.io
      resources:
      - scansettingbindings
      verbs:
      - '*'
    - apiGroups:
      - '*'
      resources:
      - '*'
      verbs:
      - get
      - list
      - watch
    - nonResourceURLs:
      - '*'
      verbs:
      - get
      - list
    ```

    > [!TIP]
    > Alternatively, you can use the OpenShift Container Platform web console to verify from the **Administrator** perspective. You can go to **User Management** → **Roles**, use the **Filter** option, select **Cluster-wide Roles**, and search for the aggregated cluster role. You must open the cluster role to check the details and configurations.

</div>

# Additional resources

- [Installing a user-defined Argo CD instance](../argocd_instance/setting-up-argocd-instance.md#setting-up-argocd-instance)

- [Adding permissions for cluster configuration](configuring-an-openshift-cluster-by-deploying-an-application-with-cluster-configurations.md#gitops-additional-permissions-for-cluster-config_configuring-an-openshift-cluster-by-deploying-an-application-with-cluster-configurations)

- [Customizing permissions by creating user-defined cluster roles for cluster-scoped instances](customizing-permissions-by-creating-user-defined-cluster-roles-for-cluster-scoped-instances.md#customizing-permissions-by-creating-user-defined-cluster-roles-for-cluster-scoped-instances)
