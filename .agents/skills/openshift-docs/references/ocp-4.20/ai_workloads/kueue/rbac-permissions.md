<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

The following procedures provide information about how you can configure role-based access control (RBAC) for your Red Hat build of Kueue deployment. These RBAC permissions determine which types of users can create which types of Red Hat build of Kueue objects.

# Cluster roles

The Red Hat build of Kueue Operator deploys `kueue-batch-admin-role` and `kueue-batch-user-role` cluster roles by default.

kueue-batch-admin-role
This cluster role includes the permissions to manage cluster queues, local queues, workloads, and resource flavors.

kueue-batch-user-role
This cluster role includes the permissions to manage jobs and to view local queues and workloads.

# Configuring permissions for batch administrators

You can configure permissions for batch administrators by binding the `kueue-batch-admin-role` cluster role to a user or group of users.

<div>

<div class="title">

Prerequisites

</div>

- The Red Hat build of Kueue Operator is installed on your cluster.

- You have cluster administrator permissions.

- You have installed the OpenShift CLI (`oc`).

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create a `ClusterRoleBinding` object as a YAML file:

    <div class="formalpara">

    <div class="title">

    Example `ClusterRoleBinding` object

    </div>

    ``` yaml
    apiVersion: rbac.authorization.k8s.io/v1
    kind: ClusterRoleBinding
    metadata:
      name: kueue-admins
    subjects:
    - kind: User
      name: admin@example.com
      apiGroup: rbac.authorization.k8s.io
    roleRef:
      kind: ClusterRole
      name: kueue-batch-admin-role
      apiGroup: rbac.authorization.k8s.io
    ```

    </div>

    - Provide a name for the `ClusterRoleBinding` object.

    - Add details about which user or group of users you want to provide user permissions for.

    - Add details about the `kueue-batch-admin-role` cluster role.

2.  Apply the `ClusterRoleBinding` object:

    ``` terminal
    $ oc apply -f <filename>.yaml
    ```

</div>

<div>

<div class="title">

Verification

</div>

- You can verify that the `ClusterRoleBinding` object was applied correctly by running the following command and verifying that the output contains the correct information for the `kueue-batch-admin-role` cluster role:

  ``` yaml
  $ oc describe clusterrolebinding.rbac
  ```

  <div class="formalpara">

  <div class="title">

  Example output

  </div>

  ``` terminal
  ...
  Name:         kueue-batch-admin-role
  Labels:       app.kubernetes.io/name=kueue
  Annotations:  <none>
  Role:
    Kind:  ClusterRole
    Name:  kueue-batch-admin-role
  Subjects:
    Kind            Name                      Namespace
    ----            ----                      ---------
    User            admin@example.com         admin-namespace
  ...
  ```

  </div>

</div>

# Configuring permissions for users

You can configure permissions for Red Hat build of Kueue users by binding the `kueue-batch-user-role` cluster role to a user or group of users.

<div>

<div class="title">

Prerequisites

</div>

- The Red Hat build of Kueue Operator is installed on your cluster.

- You have cluster administrator permissions.

- You have installed the OpenShift CLI (`oc`).

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create a `RoleBinding` object as a YAML file:

    <div class="formalpara">

    <div class="title">

    Example `ClusterRoleBinding` object

    </div>

    ``` yaml
    apiVersion: rbac.authorization.k8s.io/v1
    kind: RoleBinding
    metadata:
      name: kueue-users
      namespace: user-namespace
    subjects:
    - kind: Group
      name: team-a@example.com
      apiGroup: rbac.authorization.k8s.io
    roleRef:
      kind: ClusterRole
      name: kueue-batch-user-role
      apiGroup: rbac.authorization.k8s.io
    ```

    </div>

    - Provide a name for the `RoleBinding` object.

    - Add details about which namespace the `RoleBinding` object applies to.

    - Add details about which user or group of users you want to provide user permissions for.

    - Add details about the `kueue-batch-user-role` cluster role.

2.  Apply the `RoleBinding` object:

    ``` terminal
    $ oc apply -f <filename>.yaml
    ```

</div>

<div>

<div class="title">

Verification

</div>

- You can verify that the `RoleBinding` object was applied correctly by running the following command and verifying that the output contains the correct information for the `kueue-batch-user-role` cluster role:

  ``` yaml
  $ oc describe rolebinding.rbac
  ```

  <div class="formalpara">

  <div class="title">

  Example output

  </div>

  ``` terminal
  ...
  Name:         kueue-users
  Labels:       app.kubernetes.io/name=kueue
  Annotations:  <none>
  Role:
    Kind:  ClusterRole
    Name:  kueue-batch-user-role
  Subjects:
    Kind            Name                      Namespace
    ----            ----                      ---------
    Group           team-a@example.com        user-namespace
  ...
  ```

  </div>

</div>

# Additional resources

- [Using RBAC to define and apply permissions](../../authentication/using-rbac.md#using-rbac)

- [Glossary of common terms for OpenShift Container Platform authentication and authorization](../../authentication/index.md#openshift-auth-common-terms_overview-of-authentication-authorization)
