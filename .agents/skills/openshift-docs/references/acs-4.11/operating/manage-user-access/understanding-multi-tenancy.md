<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Red Hat Advanced Cluster Security for Kubernetes provides ways to implement multi-tenancy within a Central instance by using role-based access control (RBAC) and access scopes.

<a id="understanding-resource-scoping_understanding-multi-tenancy"></a>

# Understanding resource scoping

RHACS resources use global, cluster, or namespace scoping levels, which determines how you can use them in custom access scopes for multi-tenancy.

RHACS includes resources that RBAC uses. In addition to associating permissions for a resource, RHACS also scopes each resource.

In RHACS, resources use the following scope types:

- Global scope, where the resource does not assign to any cluster or namespace

- Cluster scope, where you assign the resource to particular clusters

- Namespace scope, where you assign the resource to particular namespaces

The scope of resources is important when creating custom access scopes. Custom access scopes create multi-tenancy within RHACS.

Only resources that use cluster or namespace scoping are applicable for scoping in access scopes. Access scopes do not scope globally scoped resources. Therefore, you can only achieve multi-tenancy within RHACS for resources that use either cluster or namespace scoping.

<a id="multi-tenancy-per-namespace-config-example_understanding-multi-tenancy"></a>

# Multi-tenancy per namespace configuration example

A common multi-tenancy pattern associates users with specific namespaces, allowing them access only to their designated namespace through a combination of custom permission sets, access scopes, and roles.

A common example for multi-tenancy within RHACS is associating users with a specific namespace and only allowing them access to their specific namespace.

The following example combines a custom permission set, access scope, and role. The user or group assigned with this role can only see CVE information, violations, and information about deployments in the particular namespace or cluster scoped to them.

<a id="multi-tenancy-per-namespace-config-example-procedure_understanding-multi-tenancy"></a>

## Configuring multi-tenancy per namespace

You can configure multi-tenancy by creating a custom permission set, access scope, and role that restricts user access to a specific namespace.

<div>

<div class="title">

Procedure

</div>

1.  In the RHACS portal, select **Platform Configuration** → **Access Control**.

2.  Select **Permission Sets**.

3.  Click **Create permission set**.

4.  Enter a **Name** and **Description** for the permission set.

5.  Select the following resources and access level and click **Save**:

    - `READ` Alert

    - `READ` Deployment

    - `READ` DeploymentExtension

    - `READ` Image

    - `READ` K8sRole

    - `READ` K8sRoleBinding

    - `READ` K8sSubject

    - `READ` NetworkGraph

    - `READ` NetworkPolicy

    - `READ` Secret

    - `READ` ServiceAccount

6.  Select **Access Scopes**.

7.  Click **Create access scope**.

8.  Enter a **Name** and **Description** for the access scope.

9.  In the **Allowed resources** section, select the namespace you want to use for scoping and click **Save**.

10. Select **Roles**.

11. Click **Create role**.

12. Enter a **Name** and **Description** for the role.

13. Select the **Permission Set** and **Access scope** that you created before for the role and click **Save**.

14. Assign the role to your required user or group.

    > [!NOTE]
    > The RHACS dashboard options for users with the sample role are minimal compared to options available to an administrator. Only relevant pages are visible for the user.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Assigning a role to a user or a group](manage-role-based-access-control-3630.md#assign-role-to-user-or-group_manage-role-based-access-control)

</div>

<a id="mutli-tenancy-limitations_understanding-multi-tenancy"></a>

# Limitations

Multi-tenancy within RHACS is not possible for resources with a global scope, which all users within a Central instance share.

Achieving multi-tenancy within RHACS is not possible for resources with a **global scope**.

The following resources have a global scope:

- Access

- Administration

- Detection

- Integration

- VulnerabilityManagementApprovals

- VulnerabilityManagementRequests

- WatchedImage

- WorkflowAdministration

All users within a RHACS Central instance share these resources and you cannot scope them.

<div>

<div class="title">

Additional resources

</div>

- [Creating a custom permission set](manage-role-based-access-control-3630.md#create-a-custom-permission-set_manage-role-based-access-control)

- [Create a custom access scope](manage-role-based-access-control-3630.md#create-a-custom-access-scope_manage-role-based-access-control)

- [Create a custom role](manage-role-based-access-control-3630.md#create-a-custom-role-3630_manage-role-based-access-control)

</div>
