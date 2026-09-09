<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Learn how to use the **Configuration Management** view and understand the correlation between various entities in your cluster to manage your cluster configuration efficiently.

Every OpenShift Container Platform cluster includes many different entities distributed throughout the cluster, which makes it more challenging to understand and act on the available information.

Red Hat Advanced Cluster Security for Kubernetes (RHACS) provides efficient configuration management that combines all these distributed entities on a single page. It brings together information about all your clusters, namespaces, nodes, deployments, images, secrets, users, groups, service accounts, and roles in a single **Configuration Management** view, helping you visualize different entities and the connections between them.

<a id="using-the-configuration-management-view_review-cluster-configuration"></a>

# Using the Configuration Management view

To open the **Configuration Management** view, select **Configuration Management** from the navigation menu. Similar to the **Dashboard**, it displays some useful widgets.

These widgets are interactive and show the following information:

- Security policy violations by severity

- The state of CIS (Center for Information Security) for Kubernetes benchmark controls

- Users with administrator rights in the most clusters

- Secrets used most widely in your clusters

The header in the **Configuration Management** view shows you the number of policies and CIS controls in your cluster.

> [!NOTE]
> Only policies in the Deploy lifecycle phase are included in the policy count and policy list view.

The header includes drop-down menus that allow you to switch between entities. For example, you can:

- Click **Policies** to view all policies and their severity, or select **CIS Controls** to view detailed information about all controls.

- Click **Application and Infrastructure** and select clusters, namespaces, nodes, deployments, images, and secrets to view detailed information.

- Click **RBAC Visibility and Configuration** and select users and groups, service accounts, and roles to view detailed information.

<a id="misconfigurations-kubernetes-rbac"></a>

# Identifying misconfigurations in Kubernetes roles

You can use the **Configuration Management** view to identify potential misconfigurations, such as users, groups, or service accounts granted the `cluster-admin` role, or roles that are not granted to anyone.

<a id="kubernetes-role-assignment_review-cluster-configuration"></a>

## Finding Kubernetes roles and their assignment

Use the **Configuration Management** view to get information about the Kubernetes roles that are assigned to specific users and groups.

<div>

<div class="title">

Procedure

</div>

1.  Go to the RHACS portal and click **Configuration Management**.

2.  Select **Role-Based Access Control** → **Users and Groups** from the header in the **Configuration Management** view. The **Users and Groups** view displays a list of Kubernetes users and groups, their assigned roles, and whether the `cluster-admin` role is enabled for each of them.

3.  Select a user or group to view more details about the associated cluster and namespace permissions.

</div>

<a id="service-accounts-permissions_review-cluster-configuration"></a>

## Finding service accounts and their permissions

Use the **Configuration Management** view to find out where service accounts are in use and their permissions.

<div>

<div class="title">

Procedure

</div>

1.  In the RHACS portal, go to **Configuration Management**.

2.  Select **RBAC Visibility and Configuration** → **Service Accounts** from the header in the **Configuration Management** view. The **Service Accounts** view displays a list of Kubernetes service accounts across your clusters, their assigned roles, whether the `cluster-admin` role is enabled, and which deployments use them.

3.  Select a row or an underlined link to view more details, including which cluster and namespace permissions are granted to the selected service account.

</div>

<a id="unused-kubernetes-roles_review-cluster-configuration"></a>

## Finding unused Kubernetes roles

Use the **Configuration Management** view to get more information about your Kubernetes roles and find unused roles.

<div>

<div class="title">

Procedure

</div>

1.  In the RHACS portal, go to **Configuration Management**.

2.  Select **RBAC Visibility and Configuration** → **Roles** from the header in the **Configuration Management** view. The **Roles** view displays a list of Kubernetes roles across your clusters, the permissions they grant, and where they are used.

3.  Select a row or an underlined link to view more details about the role.

4.  To find roles not granted to any users, groups, or service accounts, select the **Users & Groups** column header. Then select the **Service Account** column header while holding the Shift key. The list shows the roles that are not granted to any users, groups, or service accounts.

</div>

<a id="view-kubernetes-secrets_review-cluster-configuration"></a>

# Viewing Kubernetes secrets

View Kubernetes secrets in use in your environment and identify deployments using those secrets.

<div>

<div class="title">

Procedure

</div>

1.  In the RHACS portal, go to **Configuration Management**.

2.  On the **Secrets Most Used Across Deployments** widget, select **View All**. The **Secrets** view displays a list of Kubernetes secrets.

3.  Select a row to view more details.

</div>

Use the available information to identify if the secrets are in use in deployments where they are not needed.

<a id="find-policy-violations_review-cluster-configuration"></a>

# Finding policy violations

The **Policy Violations by Severity** widget in the **Configuration Management** view displays policy violations in a sunburst chart. Each level of the chart is represented by one ring or circle.

- The innermost circle represents the total number of violations.

- The next ring represents the **Low**, **Medium**, **High**, and **Critical** policy categories.

- The outermost ring represents individual policies in a particular category.

The **Configuration Management** view only shows the information about policies that have the **Lifecycle Stage** set to **Deploy**. It does not include policies that address runtime behavior or those configured for assessment in the **Build** stage.

<div>

<div class="title">

Procedure

</div>

1.  In the RHACS portal, go to **Configuration Management**.

2.  On the **Policy Violations by Severity** widget, move your mouse over the sunburst chart to view details about policy violations.

3.  Select ***n* rated as high**, where *n* is a number, to view detailed information about high-priority policy violations. The **Policies** view displays a list of policy violations filtered on the selected category.

4.  Select a row to view more details, including policy description, remediation, deployments with violations, and more. The details are visible in a panel.

5.  The **Policy Findings** section in the information panel lists deployments where these violations occurred.

6.  Select a deployment under the **Policy Findings** section to view related details including Kubernetes labels, annotations, and service account.

</div>

You can use the detailed information to plan a remediation for violations.

<a id="find-failing-cis-controls_review-cluster-configuration"></a>

# Finding failing CIS controls

Similar to the **Policy Violations** sunburst chart in the **Configuration Management** view, the **CIS Kubernetes v1.5** widget provides information about failing Center for Information Security (CIS) controls.

Each level of the chart is represented by one ring or circle.

- The innermost circle represents the percentage of failing controls.

- The next ring represents the control categories.

- The outermost ring represents individual controls in a particular category.

<div>

<div class="title">

Procedure

</div>

1.  To view details about failing controls, hover over the sunburst chart.

2.  To view detailed information about failing controls, select ***n* Controls Failing**, where *n* is a number. The **Controls** view displays a list of failing controls filtered based on the compliance state.

3.  Select a row to view more details, including control descriptions and nodes where the controls are failing.

4.  The **Control Findings** section in the information panel lists nodes where the controls are failing. Select a row to view more details, including Kubernetes labels, annotations, and other metadata.

</div>

You can use the detailed information to focus on a subset of nodes, industry standards, or failing controls. You can also assess, check, and report on the compliance status of your containerized infrastructure.
