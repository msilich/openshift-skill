<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

By default, any type of user, except the `kube:admin` user, logged into the default Argo CD instance does not have access to any services. However, a user logged into a custom Argo CD instance is a read-only user by default.

> [!NOTE]
> In Red Hat OpenShift GitOps v1.9.0 or earlier versions, any type of user, except the `kube:admin` user, logged into Argo CD using Red Hat SSO (RH SSO) is a read-only user by default.

# Configuring user level access

To manage and change the user level access, configure the role-based access control (RBAC) section in the Argo CD custom resource (CR).

<div>

<div class="title">

Procedure

</div>

1.  Edit the `argocd` CR:

    ``` terminal
    $ oc edit argocd <argocd-instance-name> -n <namespace>
    ```

    Example Output:

    ``` yaml
    metadata
    ...
    ...
      rbac:
        policy: 'g, rbacsystem:cluster-admins, role:admin'
        scopes: '[groups]'
    ```

2.  Add the `policy` configuration to the `rbac` section and add the `name` and the required `role` to be applied to the user:

    ``` yaml
    metadata
    ...
    ...
    rbac:
        policy: g, <name>, role:<role>
        scopes: '[groups]'
    ```

    > [!NOTE]
    > Currently, Red Hat SSO (RH SSO) cannot read the group information of the Red Hat OpenShift GitOps users. Therefore, configure the RBAC at the user level.

</div>
