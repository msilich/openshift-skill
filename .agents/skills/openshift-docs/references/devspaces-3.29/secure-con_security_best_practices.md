> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/secure-con_security_best_practices). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Protect your deployment

Protect your Red Hat OpenShift Dev Spaces deployment by applying these security practices to safeguard developer credentials, isolate workspaces, and reduce the cluster attack surface.

Red Hat OpenShift Dev Spaces runs on top of OpenShift, which provides the platform, and the foundation for the products functioning on top of it. OpenShift documentation is the entry point for security hardening.

<span id="con_security-best-practices_devspaces___what_is_secure_by_default"></span>

## [What is secure by default](secure-con_security_best_practices.md#con_security-best-practices_devspaces___what_is_secure_by_default)

OpenShift Dev Spaces applies these protections automatically when you install it. No configuration is required:

- **Project isolation.** Each developer gets a dedicated `<username>-devspaces` project. Users cannot access other users' resources.
- **Role-based access control (RBAC).** The Operator creates ClusterRoles that grant developers permissions only within their own project.
- **Authentication.** Only authenticated OpenShift users can access OpenShift Dev Spaces. The gateway enforces RBAC on every request.
- **Container security context.** Workspace pods run as non-root with dropped capabilities. The `container-build` SecurityContextConstraint adds only `SETGID` and `SETUID` for container builds.

<span id="con_security-best-practices_devspaces___what_you_must_configure"></span>

## [What you must configure](secure-con_security_best_practices.md#con_security-best-practices_devspaces___what_you_must_configure)

These security tasks require administrator action:

- **OAuth for Git providers.** Without OAuth, developers must manually create personal access token secrets. Set up OAuth for your Git providers to give developers credential-free repository access.
- **Access restrictions.** By default, all authenticated OpenShift users can access OpenShift Dev Spaces. Use the `advancedAuthorization` CheCluster property to restrict access to specific users and groups.

For Git OAuth setup and for restricting platform access, see Additional resources.

<span id="con_security-best-practices_devspaces___what_you_can_optionally_harden"></span>

## [What you can optionally harden](secure-con_security_best_practices.md#con_security-best-practices_devspaces___what_you_can_optionally_harden)

These additional measures strengthen your security posture but are not required:

- **Network policies.** Control ingress and egress traffic between workspace pods to limit the attack surface.
- **Resource quotas and limit ranges.** Prevent resource abuse by setting per-project consumption constraints.
- **Extension management.** Restrict IDE extensions to trusted sources, especially in air-gapped environments.
- **Self-signed certificates.** Import custom TLS certificates if your Git server or artifact repositories use internal certificate authorities.

<span id="con_security-best-practices_devspaces___project_isolation_for_developer_workspaces"></span>

## [Project isolation for developer workspaces](secure-con_security_best_practices.md#con_security-best-practices_devspaces___project_isolation_for_developer_workspaces)

In OpenShift, project isolation is similar to namespace isolation in Kubernetes but is achieved through the concept of projects. A project in OpenShift is a top-level organizational unit that provides isolation and collaboration between different applications, teams, or workloads within a cluster.

By default, OpenShift Dev Spaces provisions a unique `<username>-devspaces` project for each user. Alternatively, the cluster administrator can disable project self-provisioning on the OpenShift level, and turn off automatic namespace provisioning in the CheCluster custom resource:

``` yaml
devEnvironments:
  defaultNamespace:
    autoProvision: false
```

With this setup, you achieve curated access to OpenShift Dev Spaces. Cluster administrators control provisioning for each user and can explicitly configure various settings including resource limits and quotas. For more information about provisioning projects in advance, see Additional resources.

<span id="con_security-best-practices_devspaces___default_rbac_permissions_for_workspace_users"></span>

## [Default RBAC permissions for workspace users](secure-con_security_best_practices.md#con_security-best-practices_devspaces___default_rbac_permissions_for_workspace_users)

By default, the OpenShift Dev Spaces operator creates the following ClusterRoles:

- `<namespace>-cheworkspaces-clusterrole`
- `<namespace>-cheworkspaces-devworkspace-clusterrole`

The `<namespace>` prefix corresponds to the project name where the Red Hat OpenShift Dev Spaces CheCluster CR is located. The first time a user accesses Red Hat OpenShift Dev Spaces, the corresponding RoleBinding is created in the `<username>-devspaces` project.

The following table lists the resources and actions that you can grant users permission to use in their namespace.

<span id="con_security-best-practices_devspaces___default_rbac_permissions_for_workspace_users__entry__1"></span><span id="con_security-best-practices_devspaces___default_rbac_permissions_for_workspace_users__entry__2"></span>

| Resources | Actions |
|----|----|
| pods | "get", "list", "watch", "create", "delete", "update", "patch" |
| pods/exec | "get", "create" |
| pods/log | "get", "list", "watch" |
| pods/portforward | "get", "list", "create" |
| configmaps | "get", "list", "create", "update", "patch", "delete" |
| events | "list", "watch" |
| secrets | "get", "list", "create", "update", "patch", "delete" |
| services | "get", "list", "create", "delete", "update", "patch" |
| routes | "get", "list", "create", "delete" |
| persistentvolumeclaims | "get", "list", "watch", "create", "delete", "update", "patch" |
| apps/deployments | "get", "list", "watch", "create", "patch", "delete" |
| apps/replicasets | "get", "list", "patch", "delete" |
| namespaces | "get", "list" |
| projects | "get" |
| devworkspace | "get", "create", "delete", "list", "update", "patch", "watch" |
| devworkspacetemplates | "get", "create", "delete", "list", "update", "patch", "watch" |

Table 1. Overview of resources and actions available in a user’s namespace

Important

Each user is granted permissions only to their namespace and cannot access other users' resources. Cluster administrators can add extra permissions to users. They should not remove permissions granted by default.

For more details about configuring cluster roles for Red Hat OpenShift Dev Spaces users and role-based access control, see the Additional resources section.

<span id="con_security-best-practices_devspaces___what_runs_in_each_developer_namespace"></span>

## [What runs in each developer namespace](secure-con_security_best_practices.md#con_security-best-practices_devspaces___what_runs_in_each_developer_namespace)

Isolation of the development environments is implemented using OpenShift projects. Every developer has a project in which the following objects are created and managed:

- Cloud Development Environment (CDE) Pods, including the Integrated Development Environment (IDE) server.
- Secrets containing developer credentials, such as a Git token, SSH keys, and a Kubernetes token.
- ConfigMaps with developer-specific configuration, such as the Git name and email.
- Volumes that persist data such as the source code, even when the CDE Pod is stopped.

Important

Access to the resources in a namespace must be limited to the developer owning it. Granting read access to another developer is equivalent to sharing the developer credentials and should be avoided.

<span id="con_security-best-practices_devspaces___restrict_platform_access_with_allow_and_deny_lists"></span>

## [Restrict platform access with allow and deny lists](secure-con_security_best_practices.md#con_security-best-practices_devspaces___restrict_platform_access_with_allow_and_deny_lists)

By default, every authenticated OpenShift user can access OpenShift Dev Spaces. To limit the platform to specific users and groups, configure the `advancedAuthorization` properties in the CheCluster Custom Resource:

- `allowUsers`
- `allowGroups`
- `denyUsers`
- `denyGroups`

Users on a deny list cannot use OpenShift Dev Spaces and see a warning when they try to open the User Dashboard. If a user appears on both allow and deny lists, access is denied. For the procedure to configure allow and deny lists, see Additional resources.

<span id="con_security-best-practices_devspaces___how_gateway_authentication_controls_access"></span>

## [How gateway authentication controls access](secure-con_security_best_practices.md#con_security-best-practices_devspaces___how_gateway_authentication_controls_access)

Only authenticated OpenShift users can access Red Hat OpenShift Dev Spaces. The Gateway Pod uses a role-based access control (RBAC) subsystem to determine whether a developer is authorized to access a Cloud Development Environment (CDE) or not.

The CDE Gateway container checks the developer’s Kubernetes roles. If their roles allow access to the CDE Pod, the connection to the development environment is allowed. By default, only the owner of the namespace has access to the CDE Pod.

<span id="con_security-best-practices_devspaces___security_context_for_container_builds"></span>

## [Security context for container builds](secure-con_security_best_practices.md#con_security-best-practices_devspaces___security_context_for_container_builds)

Red Hat OpenShift Dev Spaces adds `SETGID` and `SETUID` capabilities to the specification of the CDE Pod container security context:

``` plaintext
"spec": {
  "containers": [
    "securityContext": {
            "allowPrivilegeEscalation": true,
            "capabilities": {
               "add": ["SETGID", "SETUID"],
               "drop": ["ALL","KILL","MKNOD"]
            },
            "readOnlyRootFilesystem": false,
            "runAsNonRoot": true,
            "runAsUser": 1001110000
   }
  ]
 }
```

This provides the ability for users to build container images from within a CDE.

By default, Red Hat OpenShift Dev Spaces assigns users a specific `SecurityContextConstraint` (SCC) that allows them to start a Pod with such capabilities. This SCC grants more capabilities to the users compared to the default `restricted` SCC but less capability compared to the `anyuid` SCC. This default SCC is pre-created in the OpenShift Dev Spaces namespace and named `container-build`.

Setting the following property in the CheCluster Custom Resource prevents assigning extra capabilities and SCC to users:

``` yaml
spec:
  devEnvironments:
    disableContainerBuildCapabilities: true
```

<span id="con_security-best-practices_devspaces___resource_quotas_and_limit_ranges"></span>

## [Resource quotas and limit ranges](secure-con_security_best_practices.md#con_security-best-practices_devspaces___resource_quotas_and_limit_ranges)

Resource Quotas and Limit Ranges are Kubernetes features you can use to help prevent bad actors and resource abuse within a cluster. Specifically, they allow you to set resource consumption constraints for pods and containers. By combining Resource Quotas and Limit Ranges, you can enforce project-specific policies to prevent bad actors from consuming excessive resources.

These mechanisms contribute to better resource management, stability, and fairness within an OpenShift cluster. For more information about resource quotas and limit ranges, see Additional resources.

<span id="con_security-best-practices_devspaces___network_policies_for_workspace_pods"></span>

## [Network policies for workspace pods](secure-con_security_best_practices.md#con_security-best-practices_devspaces___network_policies_for_workspace_pods)

Network policies provide an additional layer of security by controlling network traffic between pods in a Kubernetes cluster. By default, every pod can communicate with every other pod and service on the cluster.

Implementing network policies allows you to:

- Control ingress and egress traffic to and from workspace pods
- Limit the attack surface by denying unauthorized network access

When configuring network policies for Red Hat OpenShift Dev Spaces, ensure that pods in the OpenShift Dev Spaces namespace can still communicate with pods in user namespaces. This communication is required for proper functionality. For detailed instructions on configuring network policies, see Additional resources.

<span id="con_security-best-practices_devspaces___security_in_disconnected_and_air_gapped_deployments"></span>

## [Security in disconnected and air-gapped deployments](secure-con_security_best_practices.md#con_security-best-practices_devspaces___security_in_disconnected_and_air_gapped_deployments)

In a disconnected or air-gapped OpenShift cluster, nodes cannot reach public registries or the internet. That isolation reduces exposure to external threats, but you must supply container images, IDE extensions, and dependencies from internal registries that you control.

OpenShift Dev Spaces supports restricted-network installation. For installation steps, see Additional resources. Restrict IDE extensions to trusted internal sources as described in Secure IDE extensions in workspaces.

<span id="con_security-best-practices_devspaces___secure_ide_extensions_in_workspaces"></span>

## [Secure IDE extensions in workspaces](secure-con_security_best_practices.md#con_security-best-practices_devspaces___secure_ide_extensions_in_workspaces)

By default, Red Hat OpenShift Dev Spaces includes the embedded Open VSX registry which contains a limited set of extensions for the Microsoft Visual Studio Code - Open Source editor. Alternatively, cluster administrators can specify a different plugin registry in the Custom Resource, for example the open-vsx.org registry that contains thousands of extensions. They can also build a custom Open VSX registry.

Important

Installing extra extensions increases potential risks. To minimize these risks, ensure that you only install extensions from reliable sources and regularly update them.

For more information about managing IDE extensions, see Additional resources.

<span id="con_security-best-practices_devspaces___protect_developer_credentials_and_secrets"></span>

## [Protect developer credentials and secrets](secure-con_security_best_practices.md#con_security-best-practices_devspaces___protect_developer_credentials_and_secrets)

Developer credentials such as personal access tokens (PATs), SSH keys, and Kubernetes tokens are stored as Secrets in each user’s project. Treat those Secrets as confidential. Granting another user read access to a developer namespace is equivalent to sharing that developer’s credentials.

Prefer organization-wide Git OAuth so developers do not create and store long-lived personal tokens in every Cloud Development Environment. For Git OAuth setup and for mounting secrets into workspaces, see Additional resources.

<span id="con_security-best-practices_devspaces___trusted_git_repositories_and_dependencies"></span>

## [Trusted Git repositories and dependencies](secure-con_security_best_practices.md#con_security-best-practices_devspaces___trusted_git_repositories_and_dependencies)

Operate only on Git repositories that your organization trusts. Before adding new dependencies, confirm that maintainers publish security updates for known vulnerabilities. Untrusted repositories and outdated dependencies increase supply-chain risk for every Cloud Development Environment that clones them.

For credential-free Git access that reduces token sprawl, see Additional resources.

**Related tasks**  

- [Grant additional permissions to users](secure-proc_configuring_cluster_roles_for_users.md "Grant your developers additional OpenShift permissions by adding cluster roles so they can access resources beyond the default workspace operations.")
- [Restrict access to specific users and groups](secure-proc_configuring_advanced_authorization.md "Restrict OpenShift Dev Spaces access to specific users and groups so that you can control which users are allowed or denied access to the platform.")

**Related information**  

- [Provision projects in advance](configure-proc_provisioning_projects_in_advance.md)
- [Connect Git providers with OAuth](integrate-assembly_connecting_git_providers_with_oauth.md)
- [Use credentials and configurations in workspaces](develop-con_using_credentials_and_configurations_in_workspaces.md)
- [OpenShift role-based access control](https://docs.openshift.com/container-platform/4.22/authentication/using-rbac.html)
- [Resource quotas per project](https://docs.openshift.com/container-platform/4.22/applications/quotas/quotas-setting-per-project.html)
- [Limit ranges](https://docs.openshift.com/container-platform/4.22/nodes/clusters/nodes-cluster-limit-ranges.html)
- [OpenShift networking overview](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/networking_overview/index#about-openshift-sdn)
- [Configure network policies](configure-proc_configuring_network_policies.md)
- [Install OpenShift Dev Spaces in a restricted environment](install-proc_installing_dev_spaces_in_a_restricted_environment_on_openshift.md)
- [Add or remove IDE extensions](extend-assembly_managing_extensions.md)
