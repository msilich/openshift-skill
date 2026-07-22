<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

# API impersonation

You can configure a request to the OpenShift Container Platform API to act as though it originated from another user. For more information, see [User impersonation](https://kubernetes.io/docs/reference/access-authn-authz/authentication/#user-impersonation) in the Kubernetes documentation.

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

When a `system:admin` user is granted cluster administration permissions through a group, you must include the `--as=<user> --as-group=<group1> --as-group=<group2>` parameters in the command to impersonate the associated groups.

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

As a cluster administrator, you can grant unauthenticated users access to specific cluster roles to enable features, such as external webhooks or automated token management, that require cluster access without authentication. Only grant this access when required and after verifying compliance with your organization’s security standards.

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
