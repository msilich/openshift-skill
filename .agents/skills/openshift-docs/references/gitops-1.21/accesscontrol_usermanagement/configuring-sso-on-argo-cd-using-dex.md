<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

After the Red Hat OpenShift GitOps Operator is installed, Argo CD automatically creates a user with `admin` permissions. To manage multiple users, cluster administrators can use Argo CD to configure Single Sign-On (SSO).

> [!NOTE]
> The `spec.dex` parameter in the ArgoCD CR is no longer supported from Red Hat OpenShift GitOps v1.10.0 onwards. Consider using the `.spec.sso` parameter instead.

# Configuration to enable the Dex OpenShift OAuth Connector

Dex is installed by default for all the Argo CD instances created by the Operator. You can configure Red Hat OpenShift GitOps to use Dex as the SSO authentication provider by setting the `.spec.sso` parameter.

Dex uses the users and groups defined within OpenShift Container Platform by checking the OAuth server provided by the platform.

<div>

<div class="title">

Procedure

</div>

- To enable Dex, set the `.spec.sso.provider` parameter to `dex` in the YAML resource of the Operator:

  ``` yaml
  # ...
  spec:
    sso:
      provider: dex
      dex:
        openShiftOAuth: true
  # ...
  ```

  where:

  `spec.sso.dex.openShiftOAuth`
  Specifies the `openShiftOAuth` property that triggers the Operator to automatically configure the built-in OpenShift Container Platform `OAuth` server when the value is set to `true`.

  <div class="important">

  <div class="title">

  </div>

  - When external authentication is enabled at the cluster level, the `spec.sso` configuration (including `spec.sso.provider: dex` and `spec.sso.keycloak`) might not function as expected for the Argo CD instance.

  - In such cases, you must configure OIDC directly using `spec.oidcConfig` and either set `spec.sso` to `null` or remove it from the Argo CD custom resource.

  - You cannot use `spec.sso` and `spec.oidcConfig` simultaneously. Including both configurations in the Argo CD instance will result in a validation error.

  </div>

</div>

## Mapping users to specific roles

Argo CD cannot map users to specific roles if they have a direct `ClusterRoleBinding` role. You can manually change the role as `role:admin` on SSO through OpenShift.

<div>

<div class="title">

Procedure

</div>

1.  Create a group named `cluster-admins`.

    ``` terminal
    $ oc adm groups new cluster-admins
    ```

2.  Add the user to the group.

    ``` terminal
    $ oc adm groups add-users cluster-admins USER
    ```

3.  Apply the `cluster-admin` `ClusterRole` to the group:

    ``` terminal
    $ oc adm policy add-cluster-role-to-group cluster-admin cluster-admins
    ```

</div>

# Additional resources

- [`jq` command-line JSON processor documentation](https://jqlang.github.io/jq/)

- [Argo CD upstream documentation, RBAC Configuration section](https://argoproj.github.io/argo-cd/operator-manual/rbac/)
