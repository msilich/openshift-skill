<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Red Hat Advanced Cluster Security for Kubernetes provides ways to implement multi-tenancy within a Central instance.

You can implement multi-tenancy by using role-based access control (RBAC) and access scopes within RHACS.

<a id="understanding-resource-scoping"></a>

# Understanding resource scoping

RHACS includes resources which are used within RBAC. In addition to associating permissions for a resource, each resource is also scoped.

In RHACS, resources are scoped as the following types:

- Global scope, where a resource is not assigned to any cluster or namespace

- Cluster scope, where a resource is assigned to particular clusters

- Namespace scope, where a resource is assigned to particular namespaces

The scope of resources is important when creating custom access scopes. Custom access scopes are used to create multi-tenancy within RHACS.

Only resources which are cluster or namespace scoped are applicable for scoping in access scopes. Globally scoped resources are not scoped by access scopes. Therefore, multi-tenancy within RHACS can only be achieved for resources that are scoped either by cluster or namespace.

<a id="multi-tenancy-per-namespace-config-example"></a>

# Multi-tenancy per namespace configuration example

A common example for multi-tenancy within RHACS is associating users with a specific namespace and only allowing them access to their specific namespace.

The following example combines a custom permission set, access scope, and role. The user or group assigned with this role can only see CVE information, violations, and information about deployments in the particular namespace or cluster scoped to them.

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

13. Select the previously created **Permission Set** and **Access scope** for the role and click **Save**.

14. Assign the role to your required user or group. See [Assigning a role to a user or a group](manage-role-based-access-control-3630.md#assign-role-to-user-or-group_manage-role-based-access-control).

</div>

> [!NOTE]
> The RHACS dashboard options for users with the sample role are minimal compared to options available to an administrator. Only relevant pages are visible for the user.

<a id="mutli-tenancy-limitations"></a>

# Limitations

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

These resources are shared across all users within a RHACS Central instance and cannot be scoped.

<div>

<div class="title">

Additional resources

</div>

- [Creating a custom permission set](manage-role-based-access-control-3630.md#create-a-custom-permission-set_manage-role-based-access-control)

- [Create a custom access scope](manage-role-based-access-control-3630.md#create-a-custom-access-scope_manage-role-based-access-control)

- [Create a custom role](manage-role-based-access-control-3630.md#create-a-custom-role-3630_manage-role-based-access-control)

</div>
