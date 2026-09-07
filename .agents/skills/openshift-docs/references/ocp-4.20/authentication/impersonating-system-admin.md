<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

You can configure API requests to impersonate users or groups to test permissions and troubleshoot access issues in OpenShift Container Platform.

# API impersonation

You can configure API requests in OpenShift Container Platform to act as another user. Impersonation allows you to perform actions on behalf of another account without switching credentials.

# Impersonating the system:admin user

You can grant a user permission to impersonate `system:admin`, which grants them cluster administrator permissions.

<div>

<div class="title">

Procedure

</div>

- To grant a user permission to impersonate `system:admin`, run the following command:

  ``` terminal
  $ oc create clusterrolebinding <any_valid_name> --clusterrole=sudoer --user=<username>
  ```

  > [!TIP]
  > You can alternatively apply the following YAML to grant permission to impersonate `system:admin`:
  >
  > ``` yaml
  > apiVersion: rbac.authorization.k8s.io/v1
  > kind: ClusterRoleBinding
  > metadata:
  >   name: <any_valid_name>
  > roleRef:
  >   apiGroup: rbac.authorization.k8s.io
  >   kind: ClusterRole
  >   name: sudoer
  > subjects:
  > - apiGroup: rbac.authorization.k8s.io
  >   kind: User
  >   name: <username>
  > ```

</div>

# Impersonating the system:admin group

To impersonate a user who has cluster administration privileges through group membership, you must specify both the user and the associated groups in the impersonation command.

<div>

<div class="title">

Procedure

</div>

- To grant a user permission to impersonate a `system:admin` by impersonating the associated cluster administration groups, run the following command:

  ``` terminal
  $ oc create clusterrolebinding <any_valid_name> --clusterrole=sudoer --as=<user> \
  --as-group=<group1> --as-group=<group2>
  ```

</div>

# Adding unauthenticated groups to cluster roles

Grant unauthenticated users access to specific cluster roles to enable features that require cluster access without authentication, such as external webhooks or automated token management.

You can add unauthenticated users to the following cluster roles:

- `system:scope-impersonation`

- `system:webhook`

- `system:oauth-token-deleter`

- `self-access-reviewer`

> [!IMPORTANT]
> Always verify compliance with your organization’s security standards when modifying unauthenticated access.

<div>

<div class="title">

Prerequisites

</div>

- You have access to the cluster as a user with the `cluster-admin` role.

- You have installed the OpenShift CLI (`oc`).

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create a YAML file named `add-<cluster_role>-unauth.yaml` and add the following content:

    ``` yaml
    apiVersion: rbac.authorization.k8s.io/v1
    kind: ClusterRoleBinding
    metadata:
     annotations:
       rbac.authorization.kubernetes.io/autoupdate: "true"
     name: <cluster_role>access-unauthenticated
    roleRef:
     apiGroup: rbac.authorization.k8s.io
     kind: ClusterRole
     name: <cluster_role>
    subjects:
     - apiGroup: rbac.authorization.k8s.io
       kind: Group
       name: system:unauthenticated
    ```

2.  Apply the configuration by running the following command:

    ``` terminal
    $ oc apply -f add-<cluster_role>.yaml
    ```

</div>

# Additional resources

- [User impersonation (Kubernetes documentation)](https://kubernetes.io/docs/reference/access-authn-authz/authentication/#user-impersonation)
