<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Red Hat Advanced Cluster Security for Kubernetes (RHACS) comes with role-based access control (RBAC) that you can use to configure roles and grant various levels of access to Red Hat Advanced Cluster Security for Kubernetes for different users.

Beginning with version 3.63, RHACS includes a scoped access control feature that enables you to configure fine-grained and specific sets of permissions that define how a given RHACS user or a group of users can interact with RHACS, which resources they can access, and which actions they can perform.

- *Roles* are a collection of permission sets and access scopes. You can assign roles to users and groups by specifying rules. You can configure these rules when you configure an authentication provider. There are two types of roles in Red Hat Advanced Cluster Security for Kubernetes:

  - System roles that are created by Red Hat and cannot be changed.

  - Custom roles, which Red Hat Advanced Cluster Security for Kubernetes administrators can create and change at any time.

    <div class="note">

    <div class="title">

    </div>

    - If you assign multiple roles for a user, they get access to the combined permissions of the assigned roles.

    - If you have users assigned to a custom role, and you delete that role, all associated users transfer to the minimum access role that you have configured.

    </div>

- *Permission sets* are a set of permissions that define what actions a role can perform on a given resource. *Resources* are the functionalities of Red Hat Advanced Cluster Security for Kubernetes for which you can set view (`read`) and modify (`write`) permissions. There are two types of permission sets in Red Hat Advanced Cluster Security for Kubernetes:

  - System permission sets, which are created by Red Hat and cannot be changed.

  - Custom permission sets, which Red Hat Advanced Cluster Security for Kubernetes administrators can create and change at any time.

- *Access scopes* are a set of Kubernetes and OpenShift Container Platform resources that users can access. For example, you can define an access scope that only allows users to access information about pods in a given project. There are two types of access scopes in Red Hat Advanced Cluster Security for Kubernetes:

  - System access scopes, which are created by Red Hat and cannot be changed.

  - Custom access scopes, which Red Hat Advanced Cluster Security for Kubernetes administrators can create and change at any time.

<a id="rbac-system-roles-3630_manage-role-based-access-control"></a>

# System roles

Red Hat Advanced Cluster Security for Kubernetes (RHACS) includes some default system roles that you can apply to users when you create rules. You can also create custom roles as required.

| System role | Description |
|----|----|
| **Admin** | This role is targeted for administrators. Use it to provide read and write access to all resources. |
| **Analyst** | This role is targeted for a user who cannot make any changes, but can view everything. Use it to provide read-only access for all resources. |
| **Continuous Integration** | This role is targeted for CI (continuous integration) systems and includes the permission set required to enforce deployment policies. |
| **Network Graph Viewer** | This role is targeted for users who need to view the network graph. |
| **None** | This role has no read and write access to any resource. You can set this role as the minimum access role for all users. |
| **Sensor Creator** | RHACS uses this role to automate new cluster setups. It includes the permission set to create Sensors in secured clusters. |
| **Vulnerability Management Approver** | This role allows you to provide access to approve vulnerability deferrals or false positive requests. |
| **Vulnerability Management Requester** | This role allows you to provide access to request vulnerability deferrals or false positives. |
| **Vulnerability Report Creator** | This role allows you to create and manage vulnerability reporting configurations for scheduled vulnerability reports. |

<a id="view-system-roles-permission-scope_manage-role-based-access-control"></a>

## Viewing the permission set and access scope for a system role

You can view the permission set and access scope for the default system roles.

<div>

<div class="title">

Procedure

</div>

1.  In the RHACS portal, go to **Platform Configuration** → **Access control**.

2.  Select **Roles**.

3.  Click on one of the roles to view its details. The details page shows the permission set and access scope for the slected role.

</div>

> [!NOTE]
> You cannot modify permission set and access scope for the default system roles.

<a id="create-a-custom-role-3630_manage-role-based-access-control"></a>

## Creating a custom role

You can create new roles from the **Access Control** view.

<div>

<div class="title">

Prerequisites

</div>

- You must have the **Admin** role, or read and write permissions for the `Access` resource to create, modify, and delete custom roles.

- You must create a permissions set and an access scope for the custom role before creating the role.

</div>

<div>

<div class="title">

Procedure

</div>

1.  In the RHACS portal, go to **Platform Configuration** → **Access Control**.

2.  Select **Roles**.

3.  Click **Create role**.

4.  Enter a **Name** and **Description** for the new role.

5.  Select a **Permission set** for the role.

6.  Select an **Access scope** for the role.

7.  Click **Save**.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Creating a custom permission set](manage-role-based-access-control-3630.md#create-a-custom-permission-set_manage-role-based-access-control)

- [Creating a custom access scope](manage-role-based-access-control-3630.md#create-a-custom-access-scope_manage-role-based-access-control)

</div>

<a id="assign-role-to-user-or-group_manage-role-based-access-control"></a>

## Assigning a role to a user or a group

You can use the RHACS portal to assign roles to a user or a group.

<div>

<div class="title">

Procedure

</div>

1.  In the RHACS portal, go to **Platform Configuration** → **Access Control**.

2.  From the list of authentication providers, select the authentication provider.

3.  Click **Edit minimum role and rules**.

4.  Under the **Rules** section, click **Add new rule**.

5.  For **Key**, select one of the values from `userid`, `name`, `email`, or `groups`. The available choices depend on the authentication provider.

6.  For **Value**, enter the value of the user ID, name, email address, or group based on the key you selected. For example, to assign the `Analyst` role to a user by email, after selecting `email` for the **Key** field, enter the email address of the user.

7.  Click the **Role** drop-down menu and select the role you want to assign. For example, to assign the `Analyst` role to a user whose email you have entered, select `Analyst`.

8.  Click **Save**.

</div>

You can repeat these instructions for each user or group and assign different roles. For role aggregation, you can use the same key/value pair with multiple roles. For example, you can create a rule that assigns the `Analyst` role to the user `jsmith@example.com`, and then add another rule to assign the `Vulnerability Report Creator` role to the same user. For more information about roles, see "System roles".

<a id="rbac-permission-sets_manage-role-based-access-control"></a>

# System permission sets

Red Hat Advanced Cluster Security for Kubernetes includes some default system permission sets that you can apply to roles. You can also create custom permission sets as required.

| Permission set | Description |
|----|----|
| **Admin** | Provides read and write access to all resources. |
| **Analyst** | Provides read-only access for all resources. |
| **Continuous Integration** | This permission set is targeted for CI (continuous integration) systems and includes the permissions required to enforce deployment policies. |
| **Network Graph Viewer** | Provides the minimum permissions to view network graphs. |
| **None** | No read and write permissions are allowed for any resource. |
| **Sensor Creator** | Provides permissions for resources that are required to create Sensors in secured clusters. |

<a id="view-system-permission-set_manage-role-based-access-control"></a>

## Viewing the permissions for a system permission set

You can view the permissions for a system permission set in the RHACS portal.

<div>

<div class="title">

Procedure

</div>

1.  In the RHACS portal, go to **Platform Configuration** → **Access control**.

2.  Select **Permission sets**.

3.  Click on one of the permission sets to view its details. The details page shows a list of resources and their permissions for the selected permission set.

</div>

> [!NOTE]
> You cannot modify permissions for a system permission set.

<a id="create-a-custom-permission-set_manage-role-based-access-control"></a>

## Creating a custom permission set

You can create new permission sets from the **Access Control** view.

<div>

<div class="title">

Prerequisites

</div>

- You must have the **Admin** role, or read and write permissions for the `Access` resource to create, modify, and delete permission sets.

</div>

<div>

<div class="title">

Procedure

</div>

1.  In the RHACS portal, go to **Platform Configuration** → **Access Control**.

2.  Select **Permission sets**.

3.  Click **Create permission set**.

4.  Enter a **Name** and **Description** for the new permission set.

5.  For each resource, under the **Access level** column, select one of the permissions from `No access`, `Read access`, or `Read and Write access`.

    <div class="warning">

    <div class="title">

    </div>

    - If you are configuring a permission set for users, you must grant read-only permissions for the following resources:

      - `Alert`

      - `Cluster`

      - `Deployment`

      - `Image`

      - `NetworkPolicy`

      - `NetworkGraph`

      - `WorkflowAdministration`

      - `Secret`

    - These permissions are preselected when you create a new permission set.

    - If you do not grant these permissions, users will experience issues with viewing pages in the RHACS portal.

    </div>

6.  Click **Save**.

</div>

<a id="rbac-access-scopes_manage-role-based-access-control"></a>

# System access scopes

Red Hat Advanced Cluster Security for Kubernetes includes some default system access scopes that you can apply on roles. You can also create custom access scopes as required.

| Access scope | Description |
|----|----|
| **Unrestricted** | Provides access to all clusters and namespaces that Red Hat Advanced Cluster Security for Kubernetes monitors. |
| **Deny All** | Provides no access to any Kubernetes and OpenShift Container Platform resources. |

<a id="view-system-access-scopes_manage-role-based-access-control"></a>

## Viewing the details for a system access scope

You can view the Kubernetes and OpenShift Container Platform resources that are allowed and not allowed for an access scope in the RHACS portal.

<div>

<div class="title">

Procedure

</div>

1.  In the RHACS portal, go to **Platform Configuration** → **Access control**.

2.  Select **Access scopes**.

3.  Click on one of the access scopes to view its details. The details page shows a list of clusters and namespaces, and which ones are allowed for the selected access scope.

</div>

> [!NOTE]
> You cannot modify allowed resources for a system access scope.

<a id="create-a-custom-access-scope_manage-role-based-access-control"></a>

## Creating a custom access scope

You can create new access scopes from the **Access Control** view.

<div>

<div class="title">

Prerequisites

</div>

- You must have the **Admin** role, or a role with the permission set with read and write permissions for the `Access` resource to create, modify, and delete permission sets.

</div>

<div>

<div class="title">

Procedure

</div>

1.  In the RHACS portal, go to **Platform Configuration** → **Access control**.

2.  Select **Access scopes**.

3.  Click **Create access scope**.

4.  Enter a **Name** and **Description** for the new access scope.

5.  Under the **Allowed resources** section:

    - Use the **Cluster filter** and **Namespace filter** fields to filter the list of clusters and namespaces visible in the list.

    - Expand the **Cluster name** to see the list of namespaces in that cluster.

    - To allow access to all namespaces in a cluster, toggle the switch in the **Manual selection** column.

      > [!NOTE]
      > Access to a specific cluster provides users with access to the following resources within the scope of the cluster:
      >
      > - OpenShift Container Platform or Kubernetes cluster metadata and security information
      >
      > - Compliance information for authorized clusters
      >
      > - Node metadata and security information
      >
      > - Access to all namespaces in that cluster and their associated security information

    - To allow access to a namespace, toggle the switch in the **Manual selection** column for a namespace.

      > [!NOTE]
      > Access to a specific namespace gives access to the following information within the scope of the namespace:
      >
      > - Alerts and violations for deployments
      >
      > - Vulnerability data for images
      >
      > - Deployment metadata and security information
      >
      > - Role and user information
      >
      > - Network graph, policy, and baseline information for deployments
      >
      > - Process information and process baseline configuration
      >
      > - Prioritized risk information for each deployment

6.  If you want to allow access to clusters and namespaces based on labels, click **Add label selector** under the **Label selection rules** section. Then click **Add rule** to specify **Key** and **Value** pairs for the label selector. You can specify labels for clusters and namespaces.

7.  Click **Save**.

</div>

<a id="scale-considerations_manage-role-based-access-control"></a>

### Scale considerations

In large environments, for example, with thousands of namespaces, the application of user scopes that cover large numbers of namespaces can cause some pages to render slowly or time out. For example, you might experience timeouts when opening the main **Dashboard** page.

Performance was tested in a single-cluster context on an environment with 20,000 deployments across 5,000 namespaces and 80,000 alerts in one test cluster. In that testing, the load time of the main **Dashboard** page for scopes including up to 2,000 namespaces on that cluster was under a few seconds.

Performance was tested in a multi-cluster context on an environment with 200,000 deployments across 50,000 namespaces and 800,000 alerts across 10 test clusters. In that testing, the load time of the main **Dashboard** page was under a few seconds for scopes including up to 500 namespaces across the 10 clusters, as well as for scopes including up to 2,000 namespaces on a single cluster.

The load time of RHACS portal pages for user scopes with more namespaces than the numbers tested cannot be guaranteed to stay under the timeout limit.

<a id="resource-definitions_manage-role-based-access-control"></a>

# Resource definitions

Red Hat Advanced Cluster Security for Kubernetes includes many resources. The following table lists the Red Hat Advanced Cluster Security for Kubernetes resources and describes the actions that users can perform with the `read` or `write` permission.

<div class="note">

<div class="title">

</div>

- To prevent privilege escalation, when you create a new token, your role’s permissions limit the permission you can assign to that token. For example, if you only have `read` permission for the Integration resource, you cannot create a token with `write` permission.

- If you want a custom role to create tokens for other users to use, you must assign the required permissions to that custom role.

- Use short-lived tokens for machine-to-machine communication, such as CI/CD pipelines, scripts, and other automation. Also, use the `roxctl central login` command for human-to-machine communication, such as `roxctl` CLI or API access.

- The majority of cloud service providers support OIDC identity tokens, for example, Microsoft Entra ID, Google Cloud Identity Platform, and AWS Cognito. You can use OIDC identity tokens issued by these services for RHACS short-lived access.

- You can also use third-party OIDC identity tokens directly to access the API endpoint, without an exchange, if a machine-to-machine configuration exists for the token issuer.

</div>

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 40%" />
<col style="width: 40%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Resource</th>
<th style="text-align: left;">Read permission</th>
<th style="text-align: left;">Write permission</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>Access</p></td>
<td style="text-align: left;"><p>View configurations for single sign-on (SSO) and role-based access control (RBAC) rules that match user metadata to Red Hat Advanced Cluster Security for Kubernetes roles and users that have accessed your Red Hat Advanced Cluster Security for Kubernetes instance, including the metadata that the authentication providers give about them.</p></td>
<td style="text-align: left;"><p>Create, modify, or delete SSO configurations and configured RBAC rules.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Administration</p></td>
<td style="text-align: left;"><p>View the following items:</p>
<ul>
<li><p>Options for data retention, security notices and other related configurations</p></li>
<li><p>The current logging verbosity level in Red Hat Advanced Cluster Security for Kubernetes components</p></li>
<li><p>Manifest content for the uploaded probe files</p></li>
<li><p>Existing image scanner integrations</p></li>
<li><p>The status of automatic upgrades</p></li>
<li><p>Metadata about Red Hat Advanced Cluster Security for Kubernetes service-to-service authentication</p></li>
<li><p>The content of the scanner bundle (download)</p></li>
</ul></td>
<td style="text-align: left;"><p>Edit the following items:</p>
<ul>
<li><p>Data retention, security notices, and related configurations</p></li>
<li><p>The logging level</p></li>
<li><p>Support packages in Central (upload)</p></li>
<li><p>Image scanner integrations (create/modify/delete)</p></li>
<li><p>Automatic upgrades for secured clusters (enable/disable)</p></li>
<li><p>Service-to-service authentication credentials (revoke/re-issue)</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: left;"><p>Alert</p></td>
<td style="text-align: left;"><p>View existing policy violations.</p></td>
<td style="text-align: left;"><p>Resolve or edit policy violations.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>CVE</p></td>
<td style="text-align: left;"><p><em>Internal use only</em></p></td>
<td style="text-align: left;"><p><em>Internal use only</em></p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Cluster</p></td>
<td style="text-align: left;"><p>View existing secured clusters.</p></td>
<td style="text-align: left;"><p>Add new secured clusters and modify or delete existing clusters.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Compliance</p></td>
<td style="text-align: left;"><p>View compliance standards and results, recent compliance runs, and the associated completion status.</p></td>
<td style="text-align: left;"><p>Trigger compliance runs.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Deployment</p></td>
<td style="text-align: left;"><p>View deployments (workloads) in secured clusters.</p></td>
<td style="text-align: left;"><p>N/A</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>DeploymentExtension</p></td>
<td style="text-align: left;"><p>View the following items:</p>
<ul>
<li><p>Process baselines</p></li>
<li><p>Process activity in deployments</p></li>
<li><p>Risk results</p></li>
</ul></td>
<td style="text-align: left;"><p>Modify the following items:</p>
<ul>
<li><p>Process baselines (add or remove processes)</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: left;"><p>Detection</p></td>
<td style="text-align: left;"><p>Check build-time policies against images or deployment YAML.</p></td>
<td style="text-align: left;"><p>N/A</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Image</p></td>
<td style="text-align: left;"><p>View images, their components, and their vulnerabilities.</p></td>
<td style="text-align: left;"><p>N/A</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Integration</p></td>
<td style="text-align: left;"><p>View integrations and their configuration, including backup, registry, image signature, notification systems, and API tokens.</p></td>
<td style="text-align: left;"><p>Add, modify, and delete integrations and their configurations, and API tokens.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>K8sRole</p></td>
<td style="text-align: left;"><p>View roles for Kubernetes RBAC in secured clusters.</p></td>
<td style="text-align: left;"><p>N/A</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>K8sRoleBinding</p></td>
<td style="text-align: left;"><p>View role bindings for Kubernetes RBAC in secured clusters.</p></td>
<td style="text-align: left;"><p>N/A</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>K8sSubject</p></td>
<td style="text-align: left;"><p>View users and groups for Kubernetes RBAC in secured clusters.</p></td>
<td style="text-align: left;"><p>N/A</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Namespace</p></td>
<td style="text-align: left;"><p>View existing Kubernetes namespaces in secured clusters.</p></td>
<td style="text-align: left;"><p>N/A</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>NetworkGraph</p></td>
<td style="text-align: left;"><p>View active and allowed network connections in secured clusters.</p></td>
<td style="text-align: left;"><p>N/A</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>NetworkPolicy</p></td>
<td style="text-align: left;"><p>View existing network policies in secured clusters and simulate changes.</p></td>
<td style="text-align: left;"><p>Apply network policy changes in secured clusters.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Node</p></td>
<td style="text-align: left;"><p>View existing Kubernetes nodes in secured clusters.</p></td>
<td style="text-align: left;"><p>N/A</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>WorkflowAdministration</p></td>
<td style="text-align: left;"><p>View all resource collections.</p></td>
<td style="text-align: left;"><p>Add, modify, or delete resource collections.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Role</p></td>
<td style="text-align: left;"><p>View existing Red Hat Advanced Cluster Security for Kubernetes RBAC roles and their permissions.</p></td>
<td style="text-align: left;"><p>Add, modify, or delete roles and their permissions.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Secret</p></td>
<td style="text-align: left;"><p>View metadata about secrets in secured clusters.</p></td>
<td style="text-align: left;"><p>N/A</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>ServiceAccount</p></td>
<td style="text-align: left;"><p>List Kubernetes service accounts in secured clusters.</p></td>
<td style="text-align: left;"><p>N/A</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>VulnerabilityManagementApprovals</p></td>
<td style="text-align: left;"><p>View all pending deferral or false positive requests for vulnerabilities.</p></td>
<td style="text-align: left;"><p>Approve or deny any pending deferral or false positive requests and move any previously approved requests back to observed.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>VulnerabilityManagementRequests</p></td>
<td style="text-align: left;"><p>View all pending deferral or false positive requests for vulnerabilities.</p></td>
<td style="text-align: left;"><p>Request a deferral on a vulnerability, mark it as a false positive, or move a pending or previously approved request made by the same user back to observed.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>WatchedImage</p></td>
<td style="text-align: left;"><p>View undeployed and monitored watched images.</p></td>
<td style="text-align: left;"><p>Configure watched images.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>WorkflowAdministration</p></td>
<td style="text-align: left;"><p>View all resource collections.</p></td>
<td style="text-align: left;"><p>Create, modify, or delete resource collections.</p></td>
</tr>
</tbody>
</table>

<a id="declarative-configuration-auth-resources_manage-role-based-access-control"></a>

# Declarative configuration for authentication and authorization resources

You can use declarative configuration for authentication and authorization resources such as authentication providers, roles, permission sets, and access scopes. For instructions on how to use declarative configuration, see "Using declarative configuration" in the "Additional resources" section.

<div>

<div class="title">

Additional resources

</div>

- [Using declarative configuration](../../configuration/declarative-configuration-using.md)

</div>
