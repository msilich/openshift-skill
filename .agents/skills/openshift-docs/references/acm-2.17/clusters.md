> Source: [Red Hat Advanced Cluster Management for Kubernetes 2.17](https://docs.redhat.com/en/documentation/red_hat_advanced_cluster_management_for_kubernetes/2.17/html/clusters/index). Copyright Red Hat.
> Adapted from AsciiDoc to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md), [CC BY-SA 3.0](LICENSE.md) and SOURCE.json for source revisions and gaps.

<a id="cluster_mce_overview"></a>

# Cluster lifecycle with multicluster engine operator overview

The multicluster engine operator is the cluster lifecycle operator that provides cluster management capabilities for OpenShift Container Platform and Red Hat Advanced Cluster Management hub clusters. From the hub cluster, you can create and manage clusters, as well as destroy any clusters that you created. You can also hibernate, resume, and detach clusters.

If you installed Red Hat Advanced Cluster Management, you do not need to install multicluster engine operator, as it is automatically installed.

Your cluster is created by using the OpenShift Container Platform cluster installer with the Hive resource. With your OpenShift Container Platform cluster, you can use multicluster engine operator as a standalone cluster manager for cluster lifecycle function, or you can use it as part of a Red Hat Advanced Cluster Management hub cluster. If you subscribe to Red Hat Advanced Cluster Management, you also receive the operator with installation and can create, manage, and monitor other Kubernetes clusters with the Red Hat Advanced Cluster Management hub cluster.

Release images are the version of OpenShift Container Platform that you use when you create a cluster. For clusters that are created using Red Hat Advanced Cluster Management, you can enable automatic upgrading of your release images.

With hosted control planes for OpenShift Container Platform, you can create control planes as pods on a hosting cluster without the need for dedicated physical machines for each control plane.

<div>

<div class="title">

Additional resources

</div>

- [Installing and configuring OpenShift Container Platform clusters](https://docs.redhat.com/en/documentation/openshift_container_platform/4.20/html/installation_overview/index)

- [About multicluster engine for Kubernetes operator](https://docs.redhat.com/en/documentation/openshift_container_platform/4.20/html/architecture/about-the-multicluster-engine-for-kubernetes-operator)

- [Hosted control planes overview](https://docs.redhat.com/en/documentation/openshift_container_platform/4.20/html/hosted_control_planes/hosted-control-planes-overview)

- [Cluster lifecycle architecture](clusters.md#cluster-lifecycle-arch)

- [Release notes for the multicluster engine operator](mce_release_notes.md#mce-release-notes-intro)

- [Get started with multicluster engine operator](clusters.md#get-started-mce)

- [Console overview](clusters.md#mce-console-overview)

- [multicluster engine for Kubernetes operator Role-based access control](clusters.md#mce-rbac)

- [Network configuration for multicluster engine operator](clusters.md#mce-network-configuration)

- [About hosted control planes with multicluster engine operator](clusters.md#mce-hcp-overview)

- [Managing credentials](clusters.md#credentials)

- [Cluster lifecycle introduction](clusters.md#cluster-intro)

- [Release images](clusters.md#release-images-intro)

- [Discovery service introduction](clusters.md#discovery-intro)

- [APIs](clusters.md#apis-mce)

- [Troubleshooting](mce_troubleshooting.md#troubleshooting-mce)

</div>

<a id="mce-console-overview"></a>

## Console overview

OpenShift Container Platform console plug-ins are available with the OpenShift Container Platform web console and can be integrated. To use this feature, the console plug-ins must remain enabled. The multicluster engine operator displays certain console features from **Infrastructure** and **Credentials** navigation items. If you install Red Hat Advanced Cluster Management, you see more console capability.

**Note:** With the plug-ins enabled, you can access Red Hat Advanced Cluster Management within the OpenShift Container Platform console by selecting **Fleet Management** from the perspective selector. For previous OpenShift Container Platform versions, select **All Clusters** from the cluster switcher.

See [Disabling the multicluster engine for Kubernetes operator console plug-in](clusters.md#mce-disable-console) for more information.

<a id="mce-disable-console"></a>

## Disabling the multicluster engine for Kubernetes operator console plug-in

Disable the multicluster engine operator console plug-in to hide the cluster lifecycle features from the OpenShift Container Platform console. This does not affect the API access to the cluster lifecycle features.

**Required access:** Cluster administrator

<div class="formalpara">

<div class="title">

Procedure

</div>

Complete the following steps to disable the multicluster engine for Kubernetes operator console plug-in:

</div>

1.  To disable the plug-in, be sure you are in the *Administrator* perspective in the OpenShift Container Platform console.

2.  Find **Administration** in the navigation and click **Cluster Settings**, then click *Configuration* tab.

3.  From the list of *Configuration resources*, click the **Console** resource with the `operator.openshift.io` API group, which contains cluster-wide configuration for the web console.

4.  Click the *Console plug-ins* tab. The `mce` plug-in is listed. **Note:** If Red Hat Advanced Cluster Management is installed, it is also listed as `acm`.

5.  Modify plug-in status from the table. In a few moments, you are prompted to refresh the console.

<a id="mce-rbac"></a>

## multicluster engine operator role-based access control

RBAC is validated at the console level and at the API level. Actions in the console can be enabled or disabled based on user access role permissions.

RBAC is validated at the console level and at the API level. Actions in the console are enabled or disabled based on user access role permissions.

Resource scope  
Some product resources are cluster-wide, and some are namespace-scoped. You must apply cluster role bindings and namespace role bindings to your users for consistent access controls.

**Important**: \* Any user can create projects from OpenShift Container Platform, which grants administrator role permissions for the namespace. \* If a user does not have role access to a cluster, the cluster name is not visible. The cluster name is displayed as `-`.

Credential access  
Access to credentials is controlled by Kubernetes. Credentials are stored and secured as Kubernetes secrets. View the following information about credential access for users:

- Users with access to create secrets in a namespace can create credentials.

- Users with access to read secrets in a namespace can also view credentials.

- Users with the Kubernetes cluster roles of `admin` and `edit` can create and edit secrets.

- Users with the Kubernetes cluster role of `view` cannot view secrets because reading the contents of secrets enables access to service account credentials.

<div>

<div class="title">

Additional resources

</div>

- [Overview of multicluster engine for Kubernetes operator roles](clusters.md#mce-role-definitions)

- [Managing cluster lifecycle RBAC for multicluster engine operator](clusters.md#mce-manage-rbac)

</div>

<a id="mce-role-definitions"></a>

## Overview of multicluster engine for Kubernetes operator roles

Some product resources are cluster-wide and some are namespace-scoped. You must apply cluster role bindings and namespace role bindings to your users for consistent access controls. View the following table list of supported role definitions:

| Role | Definition |
|----|----|
| `cluster-admin` | This is an OpenShift Container Platform default role. A user with cluster binding to the `cluster-admin` role is an OpenShift Container Platform super user, who has all access. |
| `open-cluster-management:cluster-manager-admin` | A user with cluster binding to the `open-cluster-management:cluster-manager-admin` role is a super user, who has all access. This role allows the user to create a `ManagedCluster` resource. |
| `open-cluster-management:admin:<managed_cluster_name>` | A user with cluster binding to the `open-cluster-management:admin:<managed_cluster_name>` role has administrator access to the `ManagedCluster` resource named, `<managed_cluster_name>`. When a user has a managed cluster, this role is automatically created. |
| `open-cluster-management:view:<managed_cluster_name>` | A user with cluster binding to the `open-cluster-management:view:<managed_cluster_name>` role has view access to the `ManagedCluster` resource named, `<managed_cluster_name>`. |
| `open-cluster-management:managedclusterset:admin:<managed_clusterset_name>` | A user with cluster binding to the `open-cluster-management:managedclusterset:admin:<managed_clusterset_name>` role has administrator access to `ManagedCluster` resource named `<managed_clusterset_name>`. The user also has administrator access to `managedcluster.cluster.open-cluster-management.io`, `clusterclaim.hive.openshift.io`, `clusterdeployment.hive.openshift.io`, and `clusterpool.hive.openshift.io` resources, which has the managed cluster set labels: `cluster.open-cluster-management.io` and `clusterset=<managed_clusterset_name>`. A role binding is automatically generated when you are using a cluster set. See [*ManagedClusterSet* overview](clusters.md#creating-a-managedclusterset) to learn how to manage the resource. |
| `open-cluster-management:managedclusterset:view:<managed_clusterset_name>` | A user with cluster binding to the `open-cluster-management:managedclusterset:view:<managed_clusterset_name>` role has view access to the `ManagedCluster` resource named, \<managed_clusterset_name\>\`. The user also has view access to `managedcluster.cluster.open-cluster-management.io`, `clusterclaim.hive.openshift.io`, `clusterdeployment.hive.openshift.io`, and `clusterpool.hive.openshift.io` resources, which has the managed cluster set labels: `cluster.open-cluster-management.io`, `clusterset=<managed_clusterset_name>`. For more details on how to manage managed cluster set resources, see [*ManagedClusterSet* overview](clusters.md#creating-a-managedclusterset). |
| `admin, edit, view` | Admin, edit, and view are OpenShift Container Platform default roles. A user with a namespace-scoped binding to these roles has access to `open-cluster-management` resources in a specific namespace, while cluster-wide binding to the same roles gives access to all of the `open-cluster-management` resources cluster-wide. |

Table of role definitions

**Important**:

- Any user can create projects from OpenShift Container Platform, which gives administrator role permissions for the namespace.

- If a user does not have role access to a cluster, the cluster name is not visible. The cluster name is displayed with the following symbol: `-`.

RBAC is validated at the console level and at the API level. Actions in the console can be enabled or disabled based on user access role permissions. View the following sections for more information on RBAC for specific lifecycles in the product.

View the following console and API RBAC tables for cluster lifecycle:

| Resource | Admin | Edit | View |
|----|----|----|----|
| Clusters | read, update, delete | \- | read |
| Cluster sets | get, update, bind, join | edit role not mentioned | get |
| Managed clusters | read, update, delete | no edit role mentioned | get |
| Provider connections | create, read, update, and delete | \- | read |

Console RBAC table for cluster lifecycle

<table>
<caption>API RBAC table for cluster lifecycle</caption>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">API</th>
<th style="text-align: left;">Admin</th>
<th style="text-align: left;">Edit</th>
<th style="text-align: left;">View</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>managedclusters.cluster.open-cluster-management.io</code></p>
<p><em>You can use <code>mcl</code> (singular) or <code>mcls</code> (plural) in commands for this API.</em></p></td>
<td style="text-align: left;"><p>create, read, update, delete</p></td>
<td style="text-align: left;"><p>read, update</p></td>
<td style="text-align: left;"><p>read</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>managedclusters.view.open-cluster-management.io</code></p>
<p><em>You can use <code>mcv</code> (singular) or <code>mcvs</code> (plural) in commands for this API.</em></p></td>
<td style="text-align: left;"><p>read</p></td>
<td style="text-align: left;"><p>read</p></td>
<td style="text-align: left;"><p>read</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>managedclusters.register.open-cluster-management.io/accept</code></p></td>
<td style="text-align: left;"><p>update</p></td>
<td style="text-align: left;"><p>update</p></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>managedclusterset.cluster.open-cluster-management.io</code></p>
<p><em>You can use <code>mclset</code> (singular) or <code>mclsets</code> (plural) in commands for this API.</em></p></td>
<td style="text-align: left;"><p>create, read, update, delete</p></td>
<td style="text-align: left;"><p>read, update</p></td>
<td style="text-align: left;"><p>read</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>managedclustersets.view.open-cluster-management.io</code></p></td>
<td style="text-align: left;"><p>read</p></td>
<td style="text-align: left;"><p>read</p></td>
<td style="text-align: left;"><p>read</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>managedclustersetbinding.cluster.open-cluster-management.io</code></p>
<p><em>You can use <code>mclsetbinding</code> (singular) or <code>mclsetbindings</code> (plural) in commands for this API.</em></p></td>
<td style="text-align: left;"><p>create, read, update, delete</p></td>
<td style="text-align: left;"><p>read, update</p></td>
<td style="text-align: left;"><p>read</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>klusterletaddonconfigs.agent.open-cluster-management.io</code></p></td>
<td style="text-align: left;"><p>create, read, update, delete</p></td>
<td style="text-align: left;"><p>read, update</p></td>
<td style="text-align: left;"><p>read</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>managedclusteractions.action.open-cluster-management.io</code></p></td>
<td style="text-align: left;"><p>create, read, update, delete</p></td>
<td style="text-align: left;"><p>read, update</p></td>
<td style="text-align: left;"><p>read</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>managedclusterviews.view.open-cluster-management.io</code></p></td>
<td style="text-align: left;"><p>create, read, update, delete</p></td>
<td style="text-align: left;"><p>read, update</p></td>
<td style="text-align: left;"><p>read</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>managedclusterinfos.internal.open-cluster-management.io</code></p></td>
<td style="text-align: left;"><p>create, read, update, delete</p></td>
<td style="text-align: left;"><p>read, update</p></td>
<td style="text-align: left;"><p>read</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>manifestworks.work.open-cluster-management.io</code></p></td>
<td style="text-align: left;"><p>create, read, update, delete</p></td>
<td style="text-align: left;"><p>read, update</p></td>
<td style="text-align: left;"><p>read</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>submarinerconfigs.submarineraddon.open-cluster-management.io</code></p></td>
<td style="text-align: left;"><p>create, read, update, delete</p></td>
<td style="text-align: left;"><p>read, update</p></td>
<td style="text-align: left;"><p>read</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>placements.cluster.open-cluster-management.io</code></p></td>
<td style="text-align: left;"><p>create, read, update, delete</p></td>
<td style="text-align: left;"><p>read, update</p></td>
<td style="text-align: left;"><p>read</p></td>
</tr>
</tbody>
</table>

<a id="mce-manage-rbac"></a>

## Managing cluster lifecycle RBAC for multicluster engine operator

Validate RBAC at the console level and at the API level. Enable or disable actions in the console based on user access role permissions.

<div class="formalpara">

<div class="title">

Procedure

</div>

View the following cluster lifecycle RBAC operations:

</div>

1.  Create and administer cluster role bindings for all managed clusters. For example, create a cluster role binding to the cluster role `open-cluster-management:cluster-manager-admin`.

    This role is a superuser, with access to all resources and actions. You can create cluster-scoped `managedcluster` resources, the namespace for the resources that manage the managed cluster, and the resources in the namespace with this role. You might need to add the `username` of the ID that requires the role association to avoid permission errors. Run the following command:

    ``` bash
    oc create clusterrolebinding <role-binding-name> --clusterrole=open-cluster-management:cluster-manager-admin --user=<username>
    ```

2.  Administer a cluster role binding for a managed cluster named `cluster-name`, a role with read and write access to the cluster-scoped `managedcluster` resource. The `managedcluster` is a cluster-scoped resource and not a namespace-scoped resource. Run the following command:

    ``` bash
    oc create clusterrolebinding (role-binding-name) --clusterrole=open-cluster-management:admin:<cluster-name> --user=<username>
    ```

3.  Create a namespace role binding to the cluster role `admin`, which has read and write access to the resources in the namespace of the managed cluster. Run the following command:

    ``` bash
    oc create rolebinding <role-binding-name> -n <cluster-name> --clusterrole=admin --user=<username>
    ```

4.  Create a cluster role binding for the `open-cluster-management:view:<cluster-name>` cluster role to view a managed cluster named `cluster-name`. This role has read access to the cluster-scoped `managedcluster` resource. The `managedcluster` is a cluster-scoped resource. Run the following command:

    ``` bash
    oc create clusterrolebinding <role-binding-name> --clusterrole=open-cluster-management:view:<cluster-name> --user=<username>
    ```

5.  Create a namespace role binding to the cluster role `view`. This role has read-only access to the resources in the namespace of the managed cluster. Run the following command:

    ``` bash
    oc create rolebinding <role-binding-name> -n <cluster-name> --clusterrole=view --user=<username>
    ```

6.  View a list of the managed clusters that you can access. Administrators and users without cluster administrator privileges use the following command:

    ``` bash
    oc get managedclusters.clusterview.open-cluster-management.io
    ```

7.  View a list of the managed cluster sets that you can access. Administrators and users without cluster administrator privileges use the following command:

    ``` bash
    oc get managedclustersets.clusterview.open-cluster-management.io
    ```

8.  As a cluster administrator, use cluster pool provision clusters by creating a managed cluster set and grant administrator permission to roles by adding the role to the group. View the following examples:

    - Grant `admin` permission to the `server-foundation-clusterset` managed cluster set with the following command:

      ``` bash
      oc adm policy add-cluster-role-to-group open-cluster-management:clusterset-admin:server-foundation-clusterset
      server-foundation-team-admin
      ```

    - Grant `view` permission to the `server-foundation-clusterset` managed cluster set with the following command:

    ``` bash
    oc adm policy add-cluster-role-to-group open-cluster-management:clusterset-view:server-foundation-clusterset server-foundation-team-user
    ```

9.  Create a namespace for the cluster pool, `server-foundation-clusterpool`. View the following examples to grant role permissions:

    - Grant `admin` permission to `server-foundation-clusterpool` for the `server-foundation-team-admin` by running the following commands:

    ``` bash
    oc adm new-project server-foundation-clusterpool

    oc adm policy add-role-to-group admin server-foundation-team-admin --namespace  server-foundation-clusterpool
    ```

10. As a team administrator, create a cluster pool named `ocp46-aws-clusterpool` with a cluster set label, `cluster.open-cluster-management.io/clusterset=server-foundation-clusterset` in the cluster pool namespace:

    - The `server-foundation-webhook` checks if the cluster pool has the cluster set label, and if the user has permission to create cluster pools in the cluster set.

    - The `server-foundation-controller` grants `view` permission to the `server-foundation-clusterpool` namespace for `server-foundation-team-user`.

11. When a cluster pool is created, the cluster pool creates a `clusterdeployment`. Continue reading for more details:

    - The `server-foundation-controller` grants `admin` permission to the `clusterdeployment` namespace for `server-foundation-team-admin`.

    - The `server-foundation-controller` grants `view` permission `clusterdeployment` namespace for `server-foundation-team-user`.

      **Note:** As a `team-admin` and `team-user`, you have `admin` permission to the `clusterpool`, `clusterdeployment`, and `clusterclaim`.

<div class="formalpara">

<div class="title">

Additional resources

</div>

To learn more about each role, see [Overview of multicluster engine for Kubernetes operator roles](clusters.md#mce-role-definitions).

</div>

<a id="mce-network-configuration"></a>

## Network configuration for multicluster engine operator

When you are installing bare metal managed clusters with the Infrastructure Operator, you must configure your network to allow certain connections between the hub cluster and the managed clusters.

Configure your network settings to allow the connections.

**Important:** The trusted CA bundle is available in the multicluster engine operator namespace, but that enhancement requires changes to your network. The trusted CA bundle ConfigMap uses the default name of `trusted-ca-bundle`. You can change this name by providing it to the operator in an environment variable named `TRUSTED_CA_BUNDLE`.

For the multicluster engine operator cluster networking requirements, see the following table:

| Direction | Source | Destination | Protocol | Port | Description |
|----|----|----|----|----|----|
| Outbound to the managed cluster | Hive and `import-controller` on the hub cluster | Kubernetes API server of the provisioned managed cluster | HTTPS | 6443 | The Kubernetes API server of the provisioned managed cluster |
| Outbound to the managed cluster | Ironic service on the hub cluster | Ironic Python Agent on the managed cluster | TCP | 9999 | Communication between the bare metal node where the Ironic Python Agent is running and the Ironic conductor service |
| Inbound from the managed cluster | Baseboard Management Controller (BMC) | HTTP server next to the Ironic service | TCP | 6180, 6183 | The Baseboard Management Controller (BMC) accesses port 6180 and 6183 for virtual media. The boot firmware accesses port 6180 |
| Inbound from the managed cluster | Ironic Python Agent on the managed cluster | Ironic service on the hub cluster | TCP | 6385 | Communication between the Ironic Python Agent and the Ironic service on the hub cluster |
| Inbound from the managed cluster | Ironic Python Agent on the managed cluster | Ironic service (metal3 pod) on the hub cluster | TCP | 6388 | Internal communication between the Ironic Python Agent and the metal3 pod on the hub cluster when the provisioning network is disabled, or when virtual media through external network is enabled. Required when the hub cluster runs on a cloud provider such as Amazon Web Services, Microsoft Azure, or GCP, and managed clusters are bare metal. |
| Inbound from the managed cluster | Cluster proxy add-on agent on the managed cluster | Cluster proxy ANP service | TCP | 443 | Communication between the cluster proxy add-on agent on the managed cluster and the Cluster Proxy add-on ANP service on the hub cluster |
| Inbound from the managed cluster | Klusterlet agent and add-on agents | Kubernetes API server on the hub cluster | HTTPS | 6443 | The Kubernetes API server of the multicluster engine operator cluster from the managed cluster |

Table list of networking requirements

**Note:** If the klusterlet agent on the managed cluster requires proxy settings to access the `apiserver` on the hub cluster instead of connecting directly, configure the proxy between the hub cluster and the managed cluster.

<div>

<div class="title">

Additional resources

</div>

- [Configuring the cluster-wide proxy](https://docs.redhat.com/en/documentation/openshift_container_platform/4.20/html/configuring_network_settings/enable-cluster-wide-proxy)

- [Configure the proxy between hub cluster and managed cluster](clusters.md#config-proxy-hub-managed)

</div>

<a id="mce-hcp-overview"></a>

## About hosted control planes with multicluster engine operator

Hosted control planes represent a deployment model for OpenShift Container Platform clusters that provides significant infrastructure efficiency. Instead of requiring dedicated virtual or physical machines for each cluster control plane, hosted control planes run as pods in a single namespace on a centralized management cluster.

Standalone  
OpenShift Container Platform clusters that use dedicated virtual or physical machines for the control plane components. Each cluster requires individual infrastructure for etcd, API servers, controller managers, and schedulers.

Hosted  
A more efficient model where control planes run as pods on a shared management cluster. The hosted model offers the following advantages:

- Reduces infrastructure management effort and costs

- Enables faster cluster provisioning

- Simplifies control plane management and updates

- Allows for better resource utilization

<div>

<div class="title">

Additional resources

</div>

- [Hosted control planes overview](https://docs.redhat.com/en/documentation/openshift_container_platform/4.20/html/hosted_control_planes/hosted-control-planes-overview)

- [Requirements for hosted control planes](https://docs.redhat.com/en/documentation/openshift_container_platform/4.20/html/hosted_control_planes/preparing-to-deploy-hosted-control-planes)

- [Sizing guidance for hosted control planes](https://docs.redhat.com/en/documentation/openshift_container_platform/4.20/html/hosted_control_planes/preparing-to-deploy-hosted-control-planes#sizing-guidance-for-hosted-control-planes)

- [Deploying hosted control planes](https://docs.redhat.com/en/documentation/openshift_container_platform/4.20/html/hosted_control_planes/deploying-hosted-control-planes)

- [Deploying hosted control planes on AWS](https://docs.redhat.com/en/documentation/openshift_container_platform/4.20/html/hosted_control_planes/deploying-hosted-control-planes#deploying-hosted-control-planes-on-aws)

- [Deploying hosted control planes on bare metal](https://docs.redhat.com/en/documentation/openshift_container_platform/4.20/html/hosted_control_planes/deploying-hosted-control-planes#deploying-hosted-control-planes-on-bare-metal)

- [Deploying hosted control planes on OpenShift Virtualization](https://docs.redhat.com/en/documentation/openshift_container_platform/4.20/html/hosted_control_planes/deploying-hosted-control-planes#deploying-hosted-control-planes-on-openshift-virtualization)

- [Manually importing a hosted cluster](https://docs.redhat.com/en/documentation/openshift_container_platform/4.20/html/hosted_control_planes/manually-importing-a-hosted-cluster)

- [Managing hosted control planes](https://docs.redhat.com/en/documentation/openshift_container_platform/4.20/html/hosted_control_planes/managing-hosted-control-planes)

- [Authentication and authorization for hosted control planes](https://docs.redhat.com/en/documentation/openshift_container_platform/4.20/html/hosted_control_planes/authentication-and-authorization-for-hosted-control-planes)

- [Updating hosted control planes](https://docs.redhat.com/en/documentation/openshift_container_platform/4.20/html/hosted_control_planes/updating-hosted-control-planes)

- [Destroying a hosted cluster](https://docs.redhat.com/en/documentation/openshift_container_platform/4.20/html/hosted_control_planes/destroying-a-hosted-cluster)

- [Hosted control planes release notes](https://docs.redhat.com/en/documentation/openshift_container_platform/4.20/html/hosted_control_planes/hosted-control-planes-release-notes-1)

- [Troubleshooting hosted control planes](https://docs.redhat.com/en/documentation/openshift_container_platform/4.20/html/hosted_control_planes/troubleshooting-hosted-control-planes)

- [Integrated hosted control plane fleet management architecture pattern](https://docs.redhat.com/en/documentation/red_hat_advanced_cluster_management_for_kubernetes/2.15/html/multicluster_engine_operator_with_red_hat_advanced_cluster_management/mce-acm-integration#hosted-pattern)

- [Discovering hosted control plane clusters with Red Hat Advanced Cluster Management](https://docs.redhat.com/en/documentation/red_hat_advanced_cluster_management_for_kubernetes/2.14/html/multicluster_engine_operator_with_red_hat_advanced_cluster_management/mce-acm-integration#discover-hosted-acm)

- [Backup and restore for hosted control planes and hosted clusters](https://docs.redhat.com/en/documentation/red_hat_advanced_cluster_management_for_kubernetes/2.14/html/business_continuity/business-cont-overview#config-hcp-backup)

</div>

<a id="get-started-mce"></a>

## Get started with multicluster engine operator

The multicluster engine operator is a software operator for managing clusters across clouds and data centers. It supports both OpenShift Container Platform and Kubernetes cluster lifecycle management.

Install multicluster engine operator through Operator Lifecycle Manager, which manages the installation, update, and removal of components. You can install while connected online or in a disconnected environment.

Access APIs for cluster lifecycle management with the multicluster engine operator. Discover APIs from the console by using the API Explorer or from the command line.

The release image identifies the version of the OpenShift Container Platform image that is used to create the cluster. When you create a cluster, you can select a release image from the list of available images.

For full support information, see the [multicluster engine operator Support Matrix](https://access.redhat.com/articles/7142379). For life cycle information, see [Red Hat OpenShift Container Platform Life Cycle policy](https://access.redhat.com/support/policy/updates/openshift).

**Important:** If you are using Red Hat Advanced Cluster Management, then multicluster engine operator is already installed on the cluster.

**Deprecated:** multicluster engine operator 2.4 and earlier versions are no longer supported. The documentation might remain available, but without any errata releases for fixed issues or other updates.

**Best practice:** Update to the most recent version.

See the following documentation:

- [Preparing to install multicluster engine operator](clusters.md#preparing-to-install-mce)

- [Installing while connected online](clusters.md#installing-while-connected-online-mce)

- [Configuring infrastructure nodes for multicluster engine operator](clusters.md#config-infra-node-mce)

- [Installing on disconnected networks](get_started.md#install-on-disconnected-networks)

- [MultiClusterEngine advanced configuration](clusters.md#advanced-config-engine)

- [multicluster engine operator with Red Hat Advanced Cluster Management integration](mce_acm_integration.md#mce-acm-integration)

- [Uninstalling](clusters.md#uninstalling-mce)

- [Network configuration](clusters.md#mce-network-configuration)

- [Updating multicluster engine operator](clusters.md#updating-mce)

- [Updating disconnected clusters by using policies](clusters.md#update-disconnect-cluster-policy)

- [APIs](clusters.md#apis-mce)

- [Discover APIs from the console](clusters.md#discover-apis-console-mce)

- [Discover APIs from the command line](clusters.md#discover-apis-command-line-mce)

- [Release images](clusters.md#release-images-intro)

<a id="preparing-to-install-mce"></a>

### Preparing to install multicluster engine operator

The multicluster engine operator is installed with Operator Lifecycle Manager, which manages the installation, upgrade, and removal of the components that encompass the multicluster engine operator. Learn how to prepare for installation.

**Required access:** Cluster administrator

**Important:**

- You cannot install multicluster engine operator on a cluster that has a `ManagedCluster` resource configured in an external cluster. You must remove the `ManagedCluster` resource from the external cluster before you can install multicluster engine operator.

- For OpenShift Container Platform Dedicated environment, the `dedicated-admin` role does not have the required permissions to create namespaces in the OpenShift Container Platform Dedicated environment. You need *Cluster administrator* permissions.

- By default, the multicluster engine operator components are installed on worker nodes of your OpenShift Container Platform cluster without any additional configuration. You can install multicluster engine operator onto worker nodes by using the Red Hat OpenShift Software Catalog console, or by using the OpenShift Container Platform command-line interface.

- If you configured your OpenShift Container Platform cluster with infrastructure nodes, you can install multicluster engine operator onto those infrastructure nodes by using the OpenShift Container Platform command-line interface with additional resource parameters. See the *Installing multicluster engine on infrastructure nodes* section for details.

- If you plan to import Kubernetes clusters that were not created by OpenShift Container Platform or multicluster engine operator, you need to configure an image pull secret. For information about how to configure an image pull secret and other advanced configurations, see options in the [Advanced configuration](clusters.md#advanced-config-engine) section of this documentation.

<div class="formalpara">

<div class="title">

Prerequisites

</div>

Before you install multicluster engine operator, see the following prerequisites:

</div>

- You need an OpenShift Container Platform cluster with access to the multicluster engine operator in the Red Hat OpenShift Software Catalog console.

- You need access to the [catalog.redhat.com](https://catalog.redhat.com/software/containers/search?p=1&application_categories_list=Container%20Platform%20%2F%20Management).

- Ensure your cluster does *not* have a `ManagedCluster` resource configured in an external cluster.

- Confirm that a supported version of OpenShift Container Platform is deployed in your environment, and you must be logged into with the OpenShift Container Platform command-line interface. See the following install documentation:

  - [OpenShift Container Platform Installing](https://docs.redhat.com/en/documentation/openshift_container_platform/4.20/html/installation_overview/index)

- Your OpenShift Container Platform command-line interface must be configured to run `oc` commands. See [Getting started with the CLI](https://docs.redhat.com/en/documentation/openshift_container_platform/4.20/html/cli_tools/openshift-cli-oc#cli-getting-started) for information about installing and configuring.

- Your OpenShift Container Platform permissions must allow you to create a namespace.

- You must have an Internet connection to access the dependencies for the operator.

- To install in a OpenShift Container Platform Dedicated environment, see the following:

  - You must have the OpenShift Container Platform Dedicated environment configured and running.

  - You must have `cluster-admin` authority to the OpenShift Container Platform Dedicated environment where you are installing the engine.

- If you plan to create managed clusters by using the Assisted Installer that is provided with Red Hat OpenShift Container Platform, see [Preparing to install with the Assisted Installer](https://docs.redhat.com/en/documentation/assisted_installer_for_openshift_container_platform/2025/html/installing_openshift_container_platform_with_the_assisted_installer/prerequisites) topic in the OpenShift Container Platform documentation for the requirements.

- If you plan to configure TLS, go to the OpenShift Container Platform [Configuring TLS security profiles](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security_and_compliance/tls-security-profiles) section of the documentation and review the requirements for TLS security profiles.

<div>

<div class="title">

Procedure

</div>

1.  Verify that multicluster engine operator is not already installed on your OpenShift Container Platform cluster. The multicluster engine operator allows only one single installation on each OpenShift Container Platform cluster.

2.  To ensure that the OpenShift Container Platform cluster is set up correctly, access the OpenShift Container Platform web console with the following command:

    ``` bash
    kubectl -n openshift-console get route console
    ```

    See the following example output:

    ``` bash
    console console-openshift-console.apps.new-coral.purple-chesterfield.com
    console   https   reencrypt/Redirect     None
    ```

3.  Open the URL from your output in your browser and check the result. If the console URL displays `console-openshift-console.router.default.svc.cluster.local`, set the value for `openshift_master_default_subdomain` when you install OpenShift Container Platform. See the following example of a URL: `https://console-openshift-console.apps.new-coral.purple-chesterfield.com`.

</div>

<div class="formalpara">

<div class="title">

Next steps

</div>

You can proceed to install multicluster engine operator. See [Installing while connected online](clusters.md#installing-while-connected-online-mce) for installation instructions.

</div>

<a id="installing-while-connected-online-mce"></a>

### Installing while connected online

The multicluster engine operator is installed with Operator Lifecycle Manager, which manages the installation, update, and removal of the components that encompass the multicluster engine operator. Learn how to prepare for installation and how to install the multicluster engine operator.

**Required access:** Cluster administrator

After you prepare, you can install from the Red Hat OpenShift Software Catalog console, or from the OpenShift Container Platform command-line interface.

<div class="formalpara">

<div class="title">

Prerequisites

</div>

Before you start the installation procedure, you must complete the preparation process. See [Preparing to install multicluster engine operator](clusters.md#preparing-to-install-mce).

</div>

<div>

<div class="title">

Procedure

</div>

- Installing from the Red Hat OpenShift Software Catalog console:

  1.  From the *Administrator* view in your OpenShift Container Platform navigation, install the Red Hat OpenShift Software Catalog console that is provided with OpenShift Container Platform.

  2.  Go to **Ecosystem** \> **Software Catalog**.

  3.  Choose the Operator that you want to install.

  4.  On the *Operator Installation* page, select the options for your installation:

      Namespace  
      The multicluster engine operator engine must be installed in its own namespace, or project.

      - By default, the Red Hat OpenShift Software Catalog console installation process creates a namespace titled `multicluster-engine`. \*Continue to use the `multicluster-engine` namespace if it is available.

      - If there is already a namespace named `multicluster-engine`, select a different namespace.

      Channel  
      The channel that you select corresponds to the release that you are installing. When you select the channel, it installs the identified release, and establishes that the future errata updates within that release are obtained.

      Approval strategy  
      The approval strategy identifies the human interaction that is required for applying updates to the channel or release to which you subscribed.

      - Select **Automatic**, which is selected by default, to ensure any updates within that release are automatically applied.

      - Select **Manual** to receive a notification when an update is available. If you have concerns about when the updates are applied, this might be best practice for you.

        **Note:** To update to the next minor release, you must return to the Red Hat OpenShift Software Catalog and select a new channel for the more current release.

  5.  Select **Install** to apply your changes and create the operator.

  6.  Create the *MultiClusterEngine* custom resource.

      1.  In the OpenShift Container Platform console navigation, select **Installed Operators** \> **multicluster engine for Kubernetes**.

      2.  Select the **MultiCluster Engine** tab.

      3.  Select **Create MultiClusterEngine**.

      4.  Update the default values in the YAML file. See options in the *MultiClusterEngine advanced configuration* section of the documentation.

          The following example shows the default template:

          ``` yaml
          apiVersion: multicluster.openshift.io/v1
          kind: MultiClusterEngine
          metadata:
            name: multiclusterengine
          spec: {}
          ```

      5.  Select **Create** to initialize the custom resource. It can take up to 10 minutes for the multicluster engine operator engine to build and start.

  After the `MultiClusterEngine` resource is created, the status for the resource is `Available` on the `MultiCluster Engine` tab.

- Installing from the OpenShift Container Platform command-line interface:

  1.  Create a multicluster engine operator namespace where the operator requirements are contained. Run the following command, where `<namespace>` is the name for your multicluster engine operator namespace. The value for `<namespace>` might be referred to as *Project* in the OpenShift Container Platform environment:

      ``` bash
      oc create namespace <namespace>
      ```

  2.  Switch your project namespace to the one that you created. Replace `namespace` with the name of the namespace that you created in step 1.

      ``` bash
      oc project <namespace>
      ```

  3.  Create a YAML file to configure an `OperatorGroup` resource. Each namespace can have only one operator group. Replace `default` with the name of your operator group. Replace `namespace` with the name of your project namespace. See the following example:

      ``` yaml
      apiVersion: operators.coreos.com/v1
      kind: OperatorGroup
      metadata:
        name: <default>
        namespace: <namespace>
      spec:
        targetNamespaces:
        - <namespace>
      ```

  4.  Run the following command to create the `OperatorGroup` resource. Replace `operator-group` with the name of the operator group YAML file that you created:

      ``` bash
      oc apply -f <path-to-file>/<operator-group>.yaml
      ```

  5.  Create a YAML file to configure an OpenShift Container Platform Subscription. Your file appears similar to the following example, with `<stable-2.x>` changed to represent the supported version you are using:

      ``` yaml
      apiVersion: operators.coreos.com/v1alpha1
      kind: Subscription
      metadata:
        name: multicluster-engine
      spec:
        sourceNamespace: openshift-marketplace
        source: redhat-operators
        channel: stable-2.x
        installPlanApproval: Automatic
        name: multicluster-engine
      ```

      **Note:** To configure infrastructure nodes, see [Configuring infrastructure nodes for multicluster engine operator](clusters.md#config-infra-node-mce).

  6.  Run the following command to create the OpenShift Container Platform Subscription. Replace `subscription` with the name of the subscription file that you created:

      ``` bash
      oc apply -f <path-to-file>/<subscription>.yaml
      ```

  7.  Create a YAML file to configure the `MultiClusterEngine` custom resource. Your default template should look similar to the following example:

      ``` yaml
      apiVersion: multicluster.openshift.io/v1
      kind: MultiClusterEngine
      metadata:
        name: multiclusterengine
      spec: {}
      ```

  8.  Run the following command to create the `MultiClusterEngine` custom resource. Replace `custom-resource` with the name of your custom resource file:

      ``` bash
      oc apply -f <path-to-file>/<custom-resource>.yaml
      ```

      If this step fails with the following error, the resources are still being created and applied. Run the command again in a few minutes when the resources are created:

      ``` bash
      error: unable to recognize "./mce.yaml": no matches for kind "MultiClusterEngine" in version "operator.multicluster-engine.io/v1"
      ```

  9.  Run the following command to get the custom resource. It can take up to 10 minutes for the `MultiClusterEngine` custom resource status to display as `Available` in the `status.phase` field after you run the following command:

      ``` bash
      oc get mce -o=jsonpath='{.items[0].status.phase}'
      ```

      **Important:** If you are reinstalling the multicluster engine operator and the pods do not start, you might need to clean up artifacts. Copy the following script into a file:

      ``` bash
      #!/bin/bash
      oc delete apiservice v1.admission.cluster.open-cluster-management.io v1.admission.work.open-cluster-management.io
      oc delete validatingwebhookconfiguration multiclusterengines.multicluster.openshift.io
      oc delete mce --all
      ```

  **Notes:**

  - A `ServiceAccount` with a `ClusterRoleBinding` automatically gives cluster administrator privileges to multicluster engine operator and to any user credentials with access to the namespace where you install multicluster engine operator.

  - You can now configure your OpenShift Container Platform cluster to contain infrastructure nodes to run approved management components. Running components on infrastructure nodes avoids allocating OpenShift Container Platform subscription quota for the nodes that are running those management components. See [Configuring infrastructure nodes for multicluster engine operator](clusters.md#config-infra-node-mce) for that procedure.

</div>

<a id="config-infra-node-mce"></a>

### Configuring infrastructure nodes for multicluster engine operator

Configure your OpenShift Container Platform cluster to contain infrastructure nodes to run approved multicluster engine operator management components. Running components on infrastructure nodes avoids allocating OpenShift Container Platform subscription quota for the nodes that are running multicluster engine operator management components.

After adding infrastructure nodes to your OpenShift Container Platform cluster, follow the *Installing from the OpenShift Container Platform command-line interface* [Installing from the OpenShift Container Platform command-line interface](clusters.md#installing-while-connected-online-mce) instructions and add the following configurations to the Operator Lifecycle Manager Subscription and `MultiClusterEngine` custom resource.

<div>

<div class="title">

Procedure

</div>

1.  Configure infrastructure nodes to the OpenShift Container Platform cluster.

    1.  Follow the procedures that are described in [Creating infrastructure machine sets](https://docs.redhat.com/en/documentation/openshift_container_platform/4.20/html/machine_management/creating-infrastructure-machinesets) in the OpenShift Container Platform documentation. Infrastructure nodes are configured with a Kubernetes `taints` and `labels` to keep non-management workloads from running on them.

    2.  For compatibility with the infrastructure node enablement, which is provided by multicluster engine operator, ensure your infrastructure nodes have the following `taints` and `labels` applied:

    ``` yaml
    metadata:
      labels:
        node-role.kubernetes.io/infra: ""
    spec:
      taints:
      - effect: NoSchedule
        key: node-role.kubernetes.io/infra
    ```

2.  Configure your Operator Lifecycle Manager subscription.

    1.  Add the following additional configuration before applying the Operator Lifecycle Manager Subscription:

        ``` yaml
        spec:
          config:
            nodeSelector:
              node-role.kubernetes.io/infra: ""
            tolerations:
            - key: node-role.kubernetes.io/infra
              effect: NoSchedule
              operator: Exists
        ```

    2.  Update any add-ons to include the following node selectors and tolerations. You need to use the instructions [Set up the *AddOnDeploymentConfig* to configure klusterlet add-ons](add-ons.md#setting-addondeploymentconfig-klusterlet-addons):

    ``` yaml
        nodeSelector:
          node-role.kubernetes.io/infra: ""
        tolerations:
        - key: node-role.kubernetes.io/infra
          effect: NoSchedule
          operator: Exists
    ```

3.  If you used Red Hat OpenShift Data Foundation as a storage provisioner, make sure *Container Storage Interface* pods can run on infrastructure nodes. Learn more at [Managing container storage interface (CSI) component placements](https://docs.redhat.com/it/documentation/red_hat_openshift_data_foundation/4.18/html/managing_and_allocating_storage_resources/managing-container-storage-interface-component-placements_rhodf#managing-container-storage-interface-component-placements_rhodf) in the Red Hat OpenShift Data Foundation documentation.

4.  Add the following additional configuration before applying the `MultiClusterEngine` custom resource:

    ``` yaml
    spec:
      nodeSelector:
        node-role.kubernetes.io/infra: ""
    ```

</div>

<a id="install-on-disconnected-networks"></a>

### Install on disconnected networks

You might need to install the multicluster engine operator on Red Hat OpenShift Container Platform clusters that are not connected to the Internet. The procedure to install on a disconnected engine requires some of the same steps as the connected installation.

You must download copies of the packages to access them during the installation, rather than accessing them directly from the network during the installation.

Confirm your OpenShift Container Platform installation and then install in a disconnected environment.

You must have a supported OpenShift Container Platform version, including the registry and storage services, installed and working in your cluster. For information about OpenShift Container Platform, see [OpenShift Container Platform documentation](https://docs.redhat.com/en/documentation/openshift_container_platform/4.20/).

<div class="formalpara">

<div class="title">

Prerequisites

</div>

You must meet the following requirements before you install the multicluster engine operator:

</div>

- A supported OpenShift Container Platform version must be deployed in your environment, and you must be logged in with the command-line interface. For managing bare metal clusters, you need a supported OpenShift Container Platform version. See [OpenShift Container Platform Installing](https://docs.redhat.com/en/documentation/openshift_container_platform/4.20/html/installation_overview/index).

- You need access to [catalog.redhat.com](https://catalog.redhat.com/software/containers/search?p=1&application_categories_list=Container%20Platform%20%2F%20Management).

- Your Red Hat OpenShift Container Platform permissions must allow you to create a namespace.

- You must have a workstation with Internet connection to download the dependencies for the operator.

<div>

<div class="title">

Procedure

</div>

1.  When and if you are connected, access the OpenShift Container Platform web console with the following command to verify:

    ``` bash
    oc -n openshift-console get route console
    ```

    See the following example output:

    ``` bash
    console console-openshift-console.apps.new-name.purple-name.com
    console   https   reencrypt/Redirect     None
    ```

2.  Open the `console` URL from the outputin your browser and check the result.

3.  If the console URL displays `console-openshift-console.router.default.svc.cluster.local`, set the value for `openshift_master_default_subdomain` when you install OpenShift Container Platform.

4.  Download the required images to a mirroring registry to install the operators in a disconnected environment. Without the download, you might receive `ImagePullBackOff` errors during your deployment.

5.  Create a mirror registry. If you do not already have a mirror registry, create one by completing the procedure in the [Mirroring in disconnected environments](https://docs.redhat.com/en/documentation/openshift_container_platform/4.20/html-single/disconnected_environments/mirroring-in-disconnected-environments) topic of the Red Hat OpenShift Container Platform documentation. If you already have a mirror registry, you can configure and use your existing one.

    For bare metal only, you need to provide the certificate information for the disconnected registry in your `install-config.yaml` file. To access the image in a protected disconnected registry, you must provide the certificate information so the multicluster engine operator can access the registry. See the following steps to add the certificate information to your `install-config.yaml` file:

    1.  Copy the certificate information from the registry.

    2.  Open the `install-config.yaml` file in an editor.

    3.  Find the entry for `additionalTrustBundle: |`.

    4.  Add the certificate information after the `additionalTrustBundle` line. The result is similar to the following example:

        ``` yaml
        additionalTrustBundle: |
          -----BEGIN CERTIFICATE-----
          certificate_content
          -----END CERTIFICATE-----
        sshKey: >-
        ```

6.  **Optional:** You can specify one or multiple SSH public keys, which allow you to access the hosts after installing. See the following example:

    ``` yaml
    sshKey: |
      ssh-rsa <public-key-1>
      ssh-rsa <public-key-2>
      ssh-rsa <public-key-3>
    ```

7.  If you plan to use Governance policies, add the following additional mirrors for disconnected image registries:

    - Container Security Operator policy: Locate the images in the `registry.redhat.io/quay` source.

    - Compliance Operator policy: Locate the images in the `registry.redhat.io/compliance` source.

    - Gatekeeper Operator policy: Locate the images in the `registry.redhat.io/gatekeeper` source.

      See the following example of mirrors lists for all three operators:

    ``` yaml
        - mirrors:
          - <your_registry>/rhacm2
          source: registry.redhat.io/rhacm2
        - mirrors:
          - <your_registry>/quay
          source: registry.redhat.io/quay
        - mirrors:
          - <your_registry>/compliance
          source: registry.redhat.io/compliance
    ```

8.  Save the `install-config.yaml` file.

9.  Create a YAML file that contains the `ImageContentSourcePolicy` with the name `mce-policy.yaml`. **Note:** If you modify this on a running cluster, it causes a rolling restart of all nodes.

    ``` yaml
    apiVersion: operator.openshift.io/v1alpha1
    kind: ImageContentSourcePolicy
    metadata:
      name: mce-repo
    spec:
      repositoryDigestMirrors:
      - mirrors:
        - mirror.registry.com:5000/multicluster-engine
        source: registry.redhat.io/multicluster-engine
    ```

10. Apply the `ImageContentSourcePolicy` file by running the following command:

    ``` bash
    oc apply -f mce-policy.yaml
    ```

11. Enable the disconnected Operator Lifecycle Manager Red Hat operators and community operators. multicluster engine operator is included in the Operator Lifecycle Manager operator catalog.

12. Configure the disconnected Operator Lifecycle Manager for the Red Hat Operator catalog. Follow the steps in the [Using Operator Lifecycle Manager on restricted networks](https://docs.redhat.com/en/documentation/openshift_container_platform/4.20/html/operators/administrator-tasks#olm-restricted-networks) documentation.

13. Continue to install multicluster engine operator. See [Installing while connected online](clusters.md#installing-while-connected-online-mce) for the required steps.

</div>

<a id="advanced-config-engine"></a>

## Advanced configuration

The multicluster engine operator is installed using an operator that deploys all of the required components. The multicluster engine operator can be further configured during or after installation. Learn more about the advanced configuration options.

<a id="deployed-components"></a>

### Deployed components

Add one or more of the following attributes to the `MultiClusterEngine` custom resource:

|  |  |  |
|----|----|----|
| Name | Description | Enabled |
| assisted-service | Installs OpenShift Container Platform with minimal infrastructure prerequisites and comprehensive pre-flight validations | True |
| cluster-api | Provides capabilities to handle the Cluster API lifecycle from within a managed cluster | False |
| cluster-api-provider-aws | Provides Kubernetes-style APIs for cluster creation, configuration, and management for AWS | False |
| cluster-api-provider-openshift-assisted | Provides Kubernetes-style APIs for cluster creation, configuration, and management with Assisted Installer | False |
| cluster-api-provider-metal3 | Provides Kubernetes-style APIs for cluster creation, configuration, and management on bare-metal infrastructure | False |
| cluster-lifecycle | Provides cluster management capabilities for OpenShift Container Platform and Kubernetes hub clusters | True |
| cluster-manager | Manages various cluster-related operations within the cluster environment | True |
| cluster-proxy-addon | Automates the installation of `apiserver-network-proxy` on both hub and managed clusters using a reverse proxy server | True |
| console-mce | Enables the multicluster engine operator console plug-in | True |
| discovery | Discovers and identifies new clusters within the OpenShift Cluster Manager | True |
| hive | Provisions and performs initial configuration of OpenShift Container Platform clusters | True |
| hypershift | Hosts OpenShift Container Platform control planes at scale with cost and time efficiency, and cross-cloud portability | True |
| hypershift-local-hosting | Enables local hosting capabilities for within the local cluster environment | True |
| image-based-install-operator | Provides site configuration to single-node OpenShift clusters to complete installation | False |
| local-cluster | Enables the import and self-management of the local hub cluster where the multicluster engine operator is deployed | True |
| managedserviceacccount | Synchronizes service accounts to managed clusters, and collects tokens as secret resources to give back to the hub cluster | True |
| server-foundation | Provides foundational services for server-side operations within the multicluster environment | True |

Table list of the deployed components

When you install multicluster engine operator on to the cluster, not all of the listed components are enabled by default. You can further configure multicluster engine operator during or after installation by adding one or more attributes to the `MultiClusterEngine` custom resource. Continue reading for information about the attributes that you can add.

<a id="_console_and_component_configuration"></a>

### Console and component configuration

The following example displays the `spec.overrides` default template that you can use to enable or disable the components. Replace `<name>` with the name of the component for each configuration:

``` yaml
apiVersion: operator.open-cluster-management.io/v1
kind: MultiClusterEngine
metadata:
  name: multiclusterengine
spec:
  overrides:
    components:
    - name: <name>
      enabled: true
```

Alternatively, you can run the following command. Replace `<namespace>` with the name of your project and `<name>` with the name of the component:

``` bash
oc patch MultiClusterEngine <multiclusterengine-name> --type=json -p='[{"op": "add", "path": "/spec/overrides/components/-","value":{"name":"<name>","enabled":true}}]'
```

Local-cluster enablement  
By default, the cluster that is running multicluster engine operator is the *local cluster*, which is a hub cluster that manages itself and is designated as the `local-cluster` in the list of clusters.

In the `MultiClusterEngine` resource, the local cluster name is set from the `spec.localClusterName` value. The `enabled` setting specifies whether the feature is enabled or disabled.

The `enabled: true` setting designates your cluster as a `local-cluster`, and the `enabled: false` setting does not. See the following sample where the `local-cluster` is enabled with the `enabled: true` value.

``` yaml
apiVersion: multicluster.openshift.io/v1
kind: MultiClusterEngine
metadata:
  name: multiclusterengine
spec:
  localClusterName: <your-local-cluster-name>
  overrides:
    components:
    - name: local-cluster
      enabled: true
```

You can change the `local-cluster` name if the `enabled` field is set to `false`. You must use 34 or fewer characters for the `<your-local-cluster-name>` value. The `local-cluster` cannot be renamed if it is set as `enabled: true`.

To install multicluster engine operator *without* designating it as a `local-cluster`, change the `spec.overrides.components` settings to `enabled: false`. See the following YAML sample:

``` yaml
apiVersion: multicluster.openshift.io/v1
kind: MultiClusterEngine
metadata:
  name: multiclusterengine
spec:
  localClusterName: <your-local-cluster-name>
  overrides:
    components:
    - name: local-cluster
      enabled: false
```

Custom image pull secret  
If you plan to import Kubernetes clusters that were not created by OpenShift Container Platform or the multicluster engine operator, generate a secret that contains your OpenShift Container Platform pull secret information to access the entitled content from the distribution registry.

The secret requirements for OpenShift Container Platform clusters are automatically resolved by OpenShift Container Platform and multicluster engine for Kubernetes operator, so you do not have to create the secret if you are not importing other types of Kubernetes clusters to be managed.

**Important:** These secrets are namespace-specific, so make sure that you are in the namespace that you use for your engine.

You need to download your OpenShift Container Platform pull secret file from [cloud.redhat.com/openshift/install/pull-secret](https://console.redhat.com/openshift/install/pull-secret) by selecting **Download pull secret**. Your OpenShift Container Platform pull secret is associated with your Red Hat Customer Portal ID, and is the same across all Kubernetes providers. See the following command:

``` bash
oc create secret generic <secret> -n <namespace> --from-file=.dockerconfigjson=<path-to-pull-secret> --type=kubernetes.io/dockerconfigjson
```

- The `secret` is the name of the secret that you want to create.

- The `namespace` is your project namespace, as the secrets are namespace-specific.

- The `path-to-pull-secret` is the path to your OpenShift Container Platform pull secret that you downloaded.

  The following example displays the `spec.imagePullSecret` template to use if you want to use a custom pull secret. Replace `secret` with the name of your pull secret:

``` yaml
apiVersion: multicluster.openshift.io/v1
kind: MultiClusterEngine
metadata:
  name: multiclusterengine
spec:
  imagePullSecret: <secret>
```

Target namespace  
The operands can be installed in a designated namespace by specifying a location in the `MultiClusterEngine` custom resource. This namespace is created upon application of the `MultiClusterEngine` custom resource.

**Important:** If no target namespace is specified, the operator will install to the `multicluster-engine` namespace and will set it in the `MultiClusterEngine` custom resource specification.

The following example displays the `spec.targetNamespace` template that you can use to specify a target namespace. Replace `target` with the name of your destination namespace. **Note:** The `target` namespace cannot be the `default` namespace:

``` yaml
apiVersion: multicluster.openshift.io/v1
kind: MultiClusterEngine
metadata:
  name: multiclusterengine
spec:
  targetNamespace: <target>
```

availabilityConfig  
The hub cluster has two availabilities: `High` and `Basic`. By default, the hub cluster has `High` availability, which gives hub cluster components a `replicaCount` of `2`. This provides better support in cases of failover, but consumes more resources than the `Basic` availability, which gives components a `replicaCount` of `1`.

**Important:** Set `spec.availabilityConfig` to `Basic` if you are using multicluster engine operator on a single-node OpenShift cluster.

The following examples shows the `spec.availabilityConfig` template with `Basic` availability:

``` yaml
apiVersion: multicluster.openshift.io/v1
kind: MultiClusterEngine
metadata:
  name: multiclusterengine
spec:
  availabilityConfig: "Basic"
```

nodeSelector  
You can define a set of node selectors in the `MultiClusterEngine` to install to specific nodes on your cluster. The following example shows `spec.nodeSelector` to assign pods to nodes with the label `node-role.kubernetes.io/infra`:

``` yaml
spec:
  nodeSelector:
    node-role.kubernetes.io/infra: ""
```

To define a set of node selectors for the Red Hat Advanced Cluster Management for Kubernetes hub cluster, see [nodeSelector](get_started.md) in the Red Hat Advanced Cluster Management documentation.

tolerations  
You can define a list of tolerations to allow the `MultiClusterEngine` to tolerate specific taints defined on the cluster. The following example shows a `spec.tolerations` that matches a `node-role.kubernetes.io/infra` taint:

``` yaml
spec:
  tolerations:
  - key: node-role.kubernetes.io/infra
    effect: NoSchedule
    operator: Exists
```

The previous infra-node toleration is set on pods by default without specifying any tolerations in the configuration. Customizing tolerations in the configuration will replace this default behavior.

To define a list of tolerations for the Red Hat Advanced Cluster Management for Kubernetes hub cluster,, see [tolerations](get_started.md) in the Red Hat Advanced Cluster Management documentation.

ManagedServiceAccount add-on  
The `ManagedServiceAccount` add-on allows you to create or delete a service account on a managed cluster. To install with this add-on enabled, include the following in the `MultiClusterEngine` specification in `spec.overrides`:

``` yaml
apiVersion: multicluster.openshift.io/v1
kind: MultiClusterEngine
metadata:
  name: multiclusterengine
spec:
  overrides:
    components:
    - name: managedserviceaccount
      enabled: true
```

The `ManagedServiceAccount` add-on can be enabled after creating `MultiClusterEngine` by editing the resource on the command line and setting the `managedserviceaccount` component to `enabled: true`. Alternatively, you can run the following command and replace \<multiclusterengine-name\> with the name of your `MultiClusterEngine` resource.

``` bash
oc patch MultiClusterEngine <multiclusterengine-name> --type=json -p='[{"op": "add", "path": "/spec/overrides/components/-","value":{"name":"managedserviceaccount","enabled":true}}]'
```

<a id="uninstalling-mce"></a>

## Uninstalling

When you uninstall multicluster engine for Kubernetes operator, you see two different levels of the process: A *custom resource removal* and a *complete operator uninstall*. It might take up to five minutes to complete the uninstall process.

- The custom resource removal is the most basic type of uninstall that removes the custom resource of the `MultiClusterEngine` instance but leaves other required operator resources. This level of uninstall is helpful if you plan to reinstall using the same settings and components.

- The second level is a more complete uninstall that removes most operator components, excluding components such as custom resource definitions. When you continue with this step, it removes all of the components and subscriptions that were not removed with the custom resource removal. After this uninstall, you must reinstall the operator before reinstalling the custom resource.

You can use the terminal or the console to remove multicluster engine operator.

<div class="formalpara">

<div class="title">

Prerequisites

</div>

Before you uninstall the multicluster engine operator, you must detach all of the clusters that are managed by that engine. To avoid errors, detach all clusters, then try to uninstall again.

</div>

- If you have managed clusters attached, you might see the following message.

  ``` bash
  Cannot delete MultiClusterEngine resource because ManagedCluster resource(s) exist
  ```

  For more information about detaching clusters, see the *Cluster removal overview* section by selecting the information for your provider in [Creating clusters](clusters.md#create-intro).

<div>

<div class="title">

Procedure

</div>

1.  Uninstall multicluster engine operator from the terminal.

    1.  Ensure that your OpenShift Container Platform command-line interface is configured to run `oc` commands. See [Getting started with the OpenShift CLI](https://docs.redhat.com/en/documentation/openshift_container_platform/4.20/html/cli_tools/openshift-cli-oc#cli-getting-started) in the OpenShift Container Platform documentation for more information about how to configure the `oc` commands.

    2.  Change to your project namespace by entering the following command. Replace *namespace* with the name of your project namespace:

        ``` bash
        oc project <namespace>
        ```

    3.  Run the following command to remove the `MultiClusterEngine` custom resource:

        ``` bash
        oc delete multiclusterengine --all
        ```

    4.  Run the following command to check the progress:

        ``` bash
        oc get multiclusterengine -o yaml
        ```

    5.  Run the commands to delete the `ClusterServiceVersion` resource in the namespace where it is installed. Replace `v2.x.0` with your version:

        ``` bash
        oc get csv
        NAME                               DISPLAY                              VERSION   REPLACES   PHASE
        multicluster-engine.v2.x.0         multicluster engine for Kubernetes   2.x.0                Succeeded

        oc delete clusterserviceversion    multicluster-engine.v2.x.0
        oc delete sub multicluster-engine
        ```

    The CSV version might be different.

2.  Uninstall multicluster engine operator from the console. When you use the console to uninstall, you remove the operator.

    1.  In the OpenShift Container Platform console navigation, select **Operators** \> **Installed Operators** \> **multicluster engine for Kubernetes**.

    2.  Select the tab for *Multiclusterengine*.

    3.  Select the *Options* menu for the `MultiClusterEngine` custom resource.

    4.  Select **Delete MultiClusterEngine**.

    5.  Run the clean-up script at the end of the procedure.

        **Note:** If you plan to reinstall the same multicluster engine operator version, you can skip the rest of the steps in this procedure and reinstall the custom resource.

    6.  Navigate to **Installed Operators**.

    7.  Remove multicluster engine operator by selecting the **Options** \> **Uninstall operator**.

3.  If the multicluster engine operator resource is not removed, you need to clean up any potential remaining artifacts. Copy the following script into a file:

    ``` bash
    #!/bin/bash
    oc delete apiservice v1.admission.cluster.open-cluster-management.io v1.admission.work.open-cluster-management.io
    oc delete validatingwebhookconfiguration multiclusterengines.multicluster.openshift.io
    oc delete mce --all
    ```

</div>

<div>

<div class="title">

Additional resources

</div>

- [Mirroring in disconnected environments](https://docs.redhat.com/en/documentation/openshift_container_platform/4.20/html-single/disconnected_environments/mirroring-in-disconnected-environments)

</div>

<a id="updating-mce"></a>

## Updating multicluster engine for Kubernetes operator

Learn how to update your multicluster engine operator. Control your multicluster engine operator updates by using the operator subscription settings in the OpenShift Container Platform console.

**Required access:** OpenShift Container Platform administrator

**Important:**

- Updates are always supported from the immediate previous version. You can update to the next available feature release.

- If you are on a version with an **Extended Update Support** (EUS) status, you can update to the next version, or you can skip to the next EUS version.

- You can perform skip-level updates from `<2.x>` to `<2.x+2>` on even number versions of multicluster engine operator, starting with Red Hat Advanced Cluster Management version 2.11. For instance, when you update multicluster engine operator 2.6, which is an EUS version, you can choose to update to version 2.8, which is also an EUS version.

- You can update your `MultiClusterEngine` resource from the console. Use the Operator Lifecycle Manager `operatorcondition` to control how versions are updated. When you initially deploy multicluster engine operator by using the operator, you make the following selections:

  Channel  
  Channel corresponds to the version of the product that you are installing. The initial channel setting is often the most current channel that was available at the time of installation.

  Approval  
  Approval specifies whether approval is required for updates within the channel, or if they are done automatically.

  - If set to `Automatic`, then minor release updates in the selected channel are deployed without administrator intervention.

  - If set to `Manual`, then each update to the minor release within the channel requires an administrator to approve the update.

You also use these settings when you update to the latest version of multicluster engine operator by using the operator. Complete the following steps to update your operator:

**Important:** Downgrading a version is not supported. You cannot revert back to an earlier version after updating to a later version in the channel selection. You must uninstall the operator and reinstall it with the earlier version to use a previous version.

<div>

<div class="title">

Procedure

</div>

1.  Log in to your OpenShift Container Platform *Software Catalog*.

2.  In the OpenShift Container Platform navigation, select **Operators** \> **Installed operators**.

3.  Select the **multicluster engine for Kubernetes operator** operator.

4.  Select the **Subscription** tab to edit the subscription settings.

5.  Ensure that the *Update Status* is labeled `Up to date`. This status indicates that the operator is at the latest level that is available in the selected channel. If the *Update Status* indicates that there is an update pending, complete the following steps to update it to the latest minor release that is available in the channel:

    1.  Click the **Manual** setting in the *Approval* field to edit the value.

    2.  Select **Automatic** to enable automatic updates.

    3.  Select **Save** to commit your change.

    4.  Wait for the automatic updates to be applied to the operator. The updates automatically add the required updates to the latest version in the selected channel. When all of the updated updates are complete, the *Update Status* field indicates an `Up to date` status.

    **Note:** It can take up to 10 minutes for the `MultiClusterEngine` custom resource to finish updating.

6.  Run the following command to verify the update process is started:

    ``` bash
    oc get mce
    ```

    While in the process of updating, the `Status` displays `Updating`. After the update is complete, the `Status` field changes to `Available` status.

7.  When the *Update Status* is `Up to date`, click the value in the *Channel* field to edit the channel.

8.  Select the channel for the next available feature release, but do not attempt to skip a channel.

    The Operator Lifecycle Manager `operatorcondition` resource checks for previous updates during the current update process and prevents skipping versions. You can check that same resource status to see if the upgradable status is `true` or `false`.

9.  Click **Save** to save your changes.

10. Wait for the automatic update to complete. After the update to the next feature release completes, the updates to the latest patch releases within the channel are deployed.

11. If you have to update to a later feature release, repeat steps 7-9 until your operator is at the latest level of the desired channel. Make sure that all of the patch releases are deployed for your final channel.

12. Optional: You can set your *Approval* setting to **Manual**, if you want your future updates within the channel to require manual approvals.

13. If you performed a skip-level update, see the following sub-steps to verify your update:

    1.  Verify that the `csv` version from the previous release, for instance, `2.6` (EUS), is replaced with the updated version, for instance, `2.8` (EUS).

    2.  Verify that the `MultiClusterEngine` instance `status.currentVersion` specification value is set at `2.8` and matches the `desiredVersion` status, which is also set at `2.8`.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Operators in the OpenShift Container Platform documentation](https://docs.redhat.com/documentation/en-us/openshift_container_platform/4.17/html/operators/index)

</div>

<a id="update-disconnect-cluster-policy"></a>

## Updating disconnected clusters by using policies

If you use the Red Hat Advanced Cluster Management hub cluster, which uses the `MultiClusterHub` operator to manage, update, and install hub cluster components, you can use the OpenShift Update Service and Red Hat Advanced Cluster Management policies to update multiple clusters in a disconnected environment.

OpenShift Update Service is a separate operator and operand that monitors available versions for managed clusters and makes them accessible for updating in restricted networks.

OpenShift Update Service performs the following actions:

- Monitors update availability for disconnected clusters.

- Identifies updates mirrored to your local site by using the graph data file.

- Notifies you of available updates via the console.

See the following procedures to prepare and update clusters in a disconnected environment:

- [Preparing the disconnected mirror registry to use with OpenShift Update Service](clusters.md#prepare-disconnected-registry)

- [Deploying the OpenShift Update Service operator](clusters.md#deploy-update-service-operator)

- [Building the graph data init container](clusters.md#build-graph-init)

- [Deploying the OpenShift Update Service instance](clusters.md#deploy-update-service-instance)

- [Optional: Deploying a policy to change the default image registry](clusters.md#deploy-policy-change-registry)

- [Optional: Deploying a *Catalogsource* policy to change default location](clusters.md#deploy-policy-change-location)

- [Optional: Deploying the *ClusterVersion* policy to change the update location](clusters.md#deploy-policy-change-update-location)

- [Updating clusters in a disconnected environment](clusters.md#update-clusters-disconnected)

<a id="prepare-disconnected-registry"></a>

### Preparing the disconnected mirror registry to use with OpenShift Update Service

If you use the Red Hat Advanced Cluster Management hub cluster to manage, update, and install components with the the `MultiClusterHub` operator, you can use the OpenShift Update Service and Red Hat Advanced Cluster Management policies to update multiple clusters in a disconnected environment.

OpenShift Update Service is a separate operator and operand that monitors available versions for managed clusters and makes them accessible for updating in restricted networks.

OpenShift Update Service performs the following actions: \* Monitors update availability for disconnected clusters \* Identifies updates mirrored to your local site by using the graph data file \* Notifies you of available updates via the console

To update in a disconnected environment, you must mirror the target version image and the current version image to your local registry. You must also provide graph data for OpenShift Update Service to identify update paths.

<div class="formalpara">

<div class="title">

Prerequisites

</div>

Before you use OpenShift Update Service to update disconnected clusters, ensure you have the following requirements:

</div>

- A supported version of Red Hat Advanced Cluster Management. See [Get started with Red Hat Advanced Cluster Management](get_started.md#get-started-acm).

- A supported OpenShift Container Platform version with restricted Operator Lifecycle Manager configured. Take note of the catalog source image.

- An OpenShift Container Platform cluster that is managed by the hub cluster.

- Access credentials to a local repository for mirroring images.

- An image for the current cluster version that remains available in the mirrored images. If an update fails, the cluster reverts to the version present when the update was initiated. See [Configuring additional trust stores for image registry access](https://docs.redhat.com/en/documentation/openshift_container_platform/4.20/html/registry/configuring-registry-operator#images-configuration-cas_configuring-registry-operator)

<div>

<div class="title">

Procedure

</div>

1.  Create a script file to mirror your images. Replace `<pull-secret>` with the path to your OpenShift Container Platform pull secret:

    ``` bash
    UPSTREAM_REGISTRY=quay.io
    PRODUCT_REPO=openshift-release-dev
    RELEASE_NAME=ocp-release
    OCP_RELEASE=4.17.2-x86_64
    LOCAL_REGISTRY=$(hostname):5000
    LOCAL_SECRET_JSON=<pull-secret>

    oc adm -a ${LOCAL_SECRET_JSON} release mirror \
    --from=${UPSTREAM_REGISTRY}/${PRODUCT_REPO}/${RELEASE_NAME}:${OCP_RELEASE} \
    --to=${LOCAL_REGISTRY}/ocp4 \
    --to-release-image=${LOCAL_REGISTRY}/ocp4/release:${OCP_RELEASE}
    ```

2.  Run the script to mirror the images and separate the release images from the release content.

</div>

<div class="formalpara">

<div class="title">

Next steps

</div>

When your registry is prepared, you can deploy the OpenShift Update Service operator. See [Deploying the OpenShift Update Service operator](clusters.md#deploy-update-service-operator) for instructions.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Updating disconnected clusters by using policies](clusters.md#update-disconnect-cluster-policy)

</div>

<a id="deploy-update-service-operator"></a>

### Deploying the OpenShift Update Service operator

Deploy the OpenShift Update Service operator on your hub cluster to manage updates for disconnected clusters.

<div>

<div class="title">

Procedure

</div>

1.  In the hub cluster, access the Red Hat OpenShift Software Catalog

2.  Select the **OpenShift Update Service Operator**. Update the default values if needed. The deployment of the operator creates a new project named `openshift-update-service`.

3.  Deploy the operator. This creates the `openshift-update-service` project.

4.  Verify that the operator pods are in the `running` state: `oc get pods -n openshift-update-service`.

</div>

<div class="formalpara">

<div class="title">

Next steps

</div>

When the OpenShift Update Service is running, proceed to [Building the graph data init container](clusters.md#build-graph-init), which pulls the graph data information.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Updating disconnected clusters by using policies](clusters.md#update-disconnect-cluster-policy)

</div>

<a id="build-graph-init"></a>

### Building the graph data init container

OpenShift Update Service uses graph data information to find the available updates. In a connected environment, OpenShift Update Service pulls the graph data information for available updates directly from the [update-service graph data GitHub repository](https://github.com/openshift/cincinnati-graph-data). In a disconnected environment, you must make the graph data available in a local repository by using an `init` container.

<div>

<div class="title">

Procedure

</div>

1.  Clone the *graph data* Git repository by running the following command:

    ``` bash
    git clone https://github.com/openshift/cincinnati-graph-data
    ```

2.  Create a file that has the information for your graph data `init`. You can find a sample [Dockerfile](https://github.com/openshift/cincinnati-operator/blob/master/dev/Dockerfile) in the `cincinnati-operator` GitHub repository.

    - The `FROM` value is the external registry where OpenShift Update Service finds the images.

    - The `RUN` commands create the directory and package the files.

    - The `CMD` command copies the package file to the local repository and extracts the files for an update.

3.  Run the following command to build the `graph data init container`:

    ``` bash
    podman build -f <docker-path> -t <graph-path>:latest
    ```

    - Replace `<docker-path>` with the path to the file that you created in the previous step.

    - Replace `<graph-path>` with the path to your local graph data init container.

4.  Run the following command to push the `graph data init container`:

    ``` bash
    podman push <graph-path>:latest --authfile=<pull-secret>.json
    ```

    - Replace `<graph-path>` with the path to your local graph data init container.

    - Replace `<pull-secret>` with the path to your pull secret file.

5.  **Optional:** If you do not have `podman` installed, replace `podman` with `docker` in step three and four.

6.  Configure registry certificates. If you are using a secure external registry, OpenShift Update Service requires the CA certificate.

    1.  Find the OpenShift Container Platform external registry API, which is located in `image.config.openshift.io`. This is where the external registry CA certificate is stored. See *Configuring additional trust stores for image registry access* in the additional resources section to learn more.

    2.  Create a `ConfigMap` resource in the `openshift-config` namespace. See the following sample:

        ``` yaml
        apiVersion: v1
        kind: ConfigMap
        metadata:
          name: trusted-ca
        data:
          updateservice-registry: |
            -----BEGIN CERTIFICATE-----
            ...
            -----END CERTIFICATE-----
        ```

    3.  Edit the `cluster` resource in the `image.config.openshift.io` API to set the `additionalTrustedCA` field to the name of the `ConfigMap` that you created. Run the following command, replacing the name of the `trusted-ca` with the name in your `ConfigMap` if it changed:

    ``` bash
    oc patch image.config.openshift.io cluster -p '{"spec":{"additionalTrustedCA":{"name":"trusted-ca"}}}' --type merge
    ```

</div>

<div class="formalpara">

<div class="title">

Next steps

</div>

Follow the steps to [Deploying the OpenShift Update Service instance](clusters.md#deploy-update-service-instance).

</div>

<div>

<div class="title">

Additional resources

</div>

- [Updating disconnected clusters by using policies](clusters.md#update-disconnect-cluster-policy)

</div>

<a id="deploy-update-service-instance"></a>

### Deploying the OpenShift Update Service instance

When you finish deploying the OpenShift Update Service instance on your hub cluster, the instance is located where the images for the cluster updates are mirrored and made available to the disconnected managed cluster.

<div>

<div class="title">

Procedure

</div>

1.  If you do not want to use the default namespace of the operator, navigate to **Administration** \> **Namespaces** in the console to change the namespace.

2.  In the *Installed Operators* section of the OpenShift Container Platform console, select **OpenShift Update Service Operator**.

3.  Select **Create Instance** in the menu.

4.  Paste the contents from your OpenShift Update Service instance. Your YAML instance might resemble the following manifest:

    ``` yaml
    apiVersion: update-service.openshift.io/v1beta2
    kind: update-service
    metadata:
      name: openshift-cincinnati-instance
      namespace: openshift-update-service
    spec:
      registry: <registry-host-name>:<port>
      replicas: 1
      repository: ${LOCAL_REGISTRY}/ocp4/release
      graphDataImage: '<host-name>:<port>/cincinnati-graph-data-container'
    ```

    - Replace with the path to your local disconnected registry for your images.

    - Replace with the path to your graph data init container. This is the same value that you used when you ran the `podman push` command to push your graph data init container.

5.  Select **Create** to create the instance.

6.  From the hub cluster command-line interface, enter the `oc get pods` command to view the status of the instance creation. It might take a few minutes. The process is complete when the result of the command shows that the instance and the operator are running.

</div>

<div class="formalpara">

<div class="title">

Next steps

</div>

If you mirrored your releases into your mirrored registry, continue to [Optional: Deploying a policy to change the default image registry](clusters.md#deploy-policy-change-registry).

</div>

You can also proceed to [Updating clusters in a disconnected environment](clusters.md#update-clusters-disconnected).

<div>

<div class="title">

Additional resources

</div>

- [Updating disconnected clusters by using policies](clusters.md#update-disconnect-cluster-policy)

</div>

<a id="deploy-policy-change-registry"></a>

### Optional: Deploying a policy to change the default image registry

OpenShift Container Platform has a default image registry value that specifies where it finds the update packages. In a disconnected environment, you can create a policy to replace that value with the path to your local image registry where you mirrored your release images.

The following steps only apply if you have mirrored your releases into your mirrored registry:

**Deprecated:** `PlacementRule`

<div>

<div class="title">

Procedure

</div>

1.  Log in to the OpenShift Container Platform environment of your hub cluster.

2.  From the console, select **Governance** \> **Create policy**.

3.  Set the **YAML** switch to *On* to view the YAML version of the policy.

4.  Delete all of the content in the YAML code.

5.  Paste the following YAML content into the window to create a custom `Policy` resource with a `ConfigurationPolicy` template and a `PlacementBinding` resource:

    ``` yaml
    apiVersion: policy.open-cluster-management.io/v1
    kind: Policy
    metadata:
      name: policy-mirror
      namespace: default
    spec:
      disabled: false
      remediationAction: enforce
      policy-templates:
        - objectDefinition:
            apiVersion: policy.open-cluster-management.io/v1
            kind: ConfigurationPolicy
            metadata:
              name: policy-image-content-source-policy
            spec:
              object-templates:
                - complianceType: musthave
                  objectDefinition:
                    apiVersion: operator.openshift.io/v1alpha1
                    kind: ImageContentSourcePolicy
                    metadata:
                      name: <your-local-mirror-name>
                    spec:
                      repositoryDigestMirrors:
                        - mirrors:
                            - <your-registry>
                          source: registry.redhat.io
    ---
    apiVersion: policy.open-cluster-management.io/v1
    kind: PlacementBinding
    metadata:
      name: binding-policy-mirror
      namespace: default
    placementRef:
      name: placement-policy-mirror
      kind: PlacementRule
      apiGroup: apps.open-cluster-management.io
    subjects:
    - name: policy-mirror
      kind: Policy
      apiGroup: policy.open-cluster-management.io
    ---
    apiVersion: apps.open-cluster-management.io/v1
    kind: PlacementRule
    metadata:
      name: placement-policy-mirror
      namespace: default
    spec:
      clusterSelector:
        matchExpressions:
          []
    ```

    - Replace `<your-local-mirror-name>` with your local mirror name.

    - Replace `<your-registry>` with the path to your local mirror repository. You can find the path to your local mirror by running the `oc adm release mirror` command.

    - `matchExpressions` selects all clusters if you do not specify any expressions.

6.  Select **Enforce if supported**.

7.  Select **Create** to create the policy.

</div>

<div class="formalpara">

<div class="title">

Next steps

</div>

You can continue to [Optional: Deploying a *Catalogsource* policy to change default location](clusters.md#deploy-policy-change-location), or go to [Updating clusters in a disconnected environment](clusters.md#update-clusters-disconnected).

</div>

<div>

<div class="title">

Additional resources

</div>

- [Updating disconnected clusters by using policies](clusters.md#update-disconnect-cluster-policy)

</div>

<a id="deploy-policy-change-location"></a>

### Optional: Deploying a *CatalogSource* policy to change default location

You can push the `Catalogsource` policy to the managed cluster to change the default location from a connected location to your disconnected local registry.

<div>

<div class="title">

Procedure

</div>

1.  In the console menu, select **Governance** \> **Create policy**.

2.  Set the `YAML` switch to *On* to view the YAML version of the policy.

3.  Delete all of the content in the `YAML` code.

4.  Paste the following `YAML` content into the window to create a custom `Policy` resource and its associated `PlacementBinding` and `PlacementRule` resources:

    ``` yaml
    apiVersion: policy.open-cluster-management.io/v1
    kind: Policy
    metadata:
      name: policy-catalog
      namespace: default
    spec:
      disabled: false
      remediationAction: enforce
      policy-templates:
        - objectDefinition:
            apiVersion: policy.open-cluster-management.io/v1
            kind: ConfigurationPolicy
            metadata:
              name: policy-catalog
            spec:
              object-templates:
                - complianceType: musthave
                  objectDefinition:
                    apiVersion: config.openshift.io/v1
                    kind: OperatorHub
                    metadata:
                      name: cluster
                    spec:
                      disableAllDefaultSources: true
                - complianceType: musthave
                  objectDefinition:
                    apiVersion: operators.coreos.com/v1alpha1
                    kind: CatalogSource
                    metadata:
                      name: my-operator-catalog
                      namespace: openshift-marketplace
                    spec:
                      sourceType: grpc
                      image: '<registry_host_name>:<port>/olm/redhat-operators:v1'
                      displayName: My Operator Catalog
                      publisher: grpc
    ---
    apiVersion: policy.open-cluster-management.io/v1
    kind: PlacementBinding
    metadata:
      name: binding-policy-catalog
      namespace: default
    placementRef:
      name: placement-policy-catalog
      kind: PlacementRule
      apiGroup: apps.open-cluster-management.io
    subjects:
    - name: policy-catalog
      kind: Policy
      apiGroup: policy.open-cluster-management.io
    ---
    apiVersion: apps.open-cluster-management.io/v1
    kind: PlacementRule
    metadata:
      name: placement-policy-catalog
      namespace: default
    spec:
      clusterSelector:
        matchExpressions:
          []
    ```

    - Replace `'<registry_host_name>:<port>/olm/redhat-operators:v1'` with the path to your local restricted catalog source image.

    - `matchExpressions` selects all clusters if you do not specify any expressions.

5.  Select **Enforce if supported**.

6.  Select **Create** to create the policy.

</div>

<div class="formalpara">

<div class="title">

Next steps

</div>

Go to [Optional: Deploying the *ClusterVersion* policy to change the update location](clusters.md#deploy-policy-change-update-location) to deploy a policy to override the default registry with the OpenShift Update Service operand, or go to [Updating clusters in a disconnected environment](clusters.md#update-clusters-disconnected).

</div>

<div>

<div class="title">

Additional resources

</div>

- [Updating disconnected clusters by using policies](clusters.md#update-disconnect-cluster-policy)

</div>

<a id="deploy-policy-change-update-location"></a>

### Optional: Deploying the *ClusterVersion* policy to change the update location

You can push the `ClusterVersion` policy to the managed cluster to change the default location where it retrieves updates.

<div>

<div class="title">

Procedure

</div>

1.  From the managed cluster, confirm that the *ClusterVersion* upstream parameter is currently the default public OpenShift Update Service operand by running the following command:

    ``` bash
    oc get clusterversion -o yaml
    ```

2.  From the hub cluster, identify the route URL to the OpenShift Update Service operand by running the following command and plan to use the results from the output later in the procedure:

    ``` bash
    oc get routes
    ```

3.  In the hub cluster console menu, select **Governance** \> **Create a policy**.

4.  Set the `YAML` switch to *On* to view the YAML version of the policy.

5.  Delete all of the content in the `YAML` code and paste the following `YAML` content with the `Policy` and `PlacementBinding` resources:

    ``` yaml
    apiVersion: policy.open-cluster-management.io/v1
    kind: Policy
    metadata:
      name: policy-cluster-version
      namespace: default
      annotations:
        policy.open-cluster-management.io/standards: null
        policy.open-cluster-management.io/categories: null
        policy.open-cluster-management.io/controls: null
    spec:
      disabled: false
      remediationAction: enforce
      policy-templates:
        - objectDefinition:
            apiVersion: policy.open-cluster-management.io/v1
            kind: ConfigurationPolicy
            metadata:
              name: policy-cluster-version
            spec:
              object-templates:
                - complianceType: musthave
                  objectDefinition:
                    apiVersion: config.openshift.io/v1
                    kind: ClusterVersion
                    metadata:
                      name: version
                    spec:
                      channel: stable-4.4
                      upstream: >-
                        https://example-cincinnati-policy-engine-uri/api/upgrades_info/v1/graph 

    ---
    apiVersion: policy.open-cluster-management.io/v1
    kind: PlacementBinding
    metadata:
      name: binding-policy-cluster-version
      namespace: default
    placementRef:
      name: placement-policy-cluster-version
      kind: PlacementRule
      apiGroup: apps.open-cluster-management.io
    subjects:
    - name: policy-cluster-version
      kind: Policy
      apiGroup: policy.open-cluster-management.io
    ---
    apiVersion: apps.open-cluster-management.io/v1
    kind: PlacementRule
    metadata:
      name: placement-policy-cluster-version
      namespace: default
    spec:
      clusterSelector:
        matchExpressions:
          []
    ```

    - Replace the `https://example-cincinnati-policy-engine-uri/api/upgrades_info/v1/graph` values with the path to your hub cluster OpenShift Update Service operand.

    - `matchExpressions` selects all clusters if you do not specify any expressions.

6.  Run the `oc get get routes -A` command on the hub cluster to determine the path to the operand.

7.  Find the route to `update-service`. The path to the operand is the value in the `HOST/PORT` field.

8.  Select **Enforce if supported**.

9.  Select **Create** to create the policy.

10. In the managed cluster command-line interface, confirm that the upstream parameter in the `ClusterVersion` is updated with the local hub cluster OpenShift Update Service URL by running the following command:

    ``` bash
    oc get clusterversion -o yaml
    ```

11. Ensure that the the results resemble the following content:

    ``` yaml
    apiVersion: v1
    items:
    - apiVersion: config.openshift.io/v1
      kind: ClusterVersion
    [..]
      spec:
        channel: stable-4.4
        upstream: https://<hub-cincinnati-uri>/api/upgrades_info/v1/graph
    ```

</div>

<div>

<div class="title">

Additional resources

</div>

- [Updating disconnected clusters by using policies](clusters.md#update-disconnect-cluster-policy)

</div>

<a id="update-clusters-disconnected"></a>

### Updating clusters in a disconnected environment

You can view a list of available updates for your managed cluster. You can use the Red Hat Advanced Cluster Management console to select a channel for your cluster updates on OpenShift Container Platform. Those versions must be available on the mirror registry. After configuring the disconnected registry, Red Hat Advanced Cluster Management and OpenShift Update Service use the disconnected registry to find if updates are available.

After configuring the disconnected registry, Red Hat Advanced Cluster Management and OpenShift Update Service use the disconnected registry to find if updates are available. See [Configuring additional trust stores for image registry access](https://docs.redhat.com/en/documentation/openshift_container_platform/4.20/html/registry/configuring-registry-operator#images-configuration-cas_configuring-registry-operator) in the OpenShift Container Platform documentation to learn more about the external registry CA certificate.

If no available updates are displayed, make sure that you have the release image of the current level of the cluster and at least one later level mirrored in the local repository.

If the release image for the current version of the cluster is not available, no updates are available.

<div>

<div class="title">

Procedure

</div>

1.  From the console, select **Infrastructure** \> **Clusters**.

2.  Select a cluster that is in the *Ready* state.

3.  From the **Actions** menu, select **Update cluster**.

4.  Verify that the optional update paths are available. **Note:** No available update versions are shown if the current version is not mirrored into the local image repository.

5.  Select a *channel* for your cluster updates on OpenShift Container Platform. Those versions must be available on the mirror registry.

6.  In the console, select **Infrastructure** \> **Clusters**.

7.  Find the cluster that you want to update. If there is an update available, the **Distribution version** column for the cluster displays an update available.

8.  Select the *Options* menu for that cluster, and select **Update cluster**.

9.  Select the target version for the update, and select **Update**.

</div>

If your cluster update fails, the Operator generally retries the update a few times, stops, and reports the status of the failing component. In some cases, the update process continues to cycle through attempts to complete the process. Rolling your cluster back to a previous version after a failed update is not supported. Contact Red Hat support for assistance if your cluster update fails.

<div>

<div class="title">

Additional resources

</div>

- [Updating disconnected clusters by using policies](clusters.md#update-disconnect-cluster-policy)

</div>

<a id="apis-mce"></a>

## APIs

Use the *API Explorer* in the console, or run an `oc` or `kubectl` command, to view current and supported APIs.

You can access APIs for cluster lifecycle management with the multicluster engine operator. **User required access:** You can only perform actions that your role is assigned.

**Notes:**

- You can also access all APIs from the integrated console. Select the **Administrator** perspective, then navigate to **Home** \> **API Explorer** to explore API groups.

- For Red Hat OpenShift Container Platform versions earlier than version 4.20, select **local-cluster** from the cluster switcher. Then select **Home** \> **API Explorer** to explore API groups.

For more information, review the following API documentation:

- [Discover APIs from the console](clusters.md#discover-apis-console-mce)

- [Discover APIs from the command line](clusters.md#discover-apis-command-line-mce)

<a id="discover-apis-console-mce"></a>

### Discover APIs from the console

You can view multicluster engine operator custom resources definitions from the integrated console. List available APIs and view details on your managed clusters.

**Required access:** Cluster administrator, or a role with permission to list and get custom resources definitions

<div>

<div class="title">

Prerequisites

</div>

- You installed a supported version of OpenShift Container Platform on your hub cluster. See [Installing OpenShift Container Platform](https://docs.redhat.com/en/documentation/openshift_container_platform/4.19/html/installation_overview/index).

- multicluster engine operator is installed on the hub cluster. If you installed Red Hat Advanced Cluster Management, multicluster engine operator is installed automatically. See [Preparing to install multicluster engine operator](clusters.md#preparing-to-install-mce).

- You are logged in to the hub cluster with credentials that can access API resources.

</div>

<div>

<div class="title">

Procedure

</div>

1.  In the OpenShift Container Platform console, choose the **Core platform** view.

2.  Click **Home** \> **API Explorer** in the navigation menu.

3.  From the **API Explorer** page, sort by groups, versions, scope, and kind to view the available APIs and *Resource details* for your hub cluster and managed clusters. You can also change the amount of information that is displayed by selecting the number `per page` from the drop-down menu.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Advanced Cluster Management API documentation](https://github.com/stolostron/api-documentation)

</div>

<a id="discover-apis-command-line-mce"></a>

### Discover APIs from the command line

You can view multicluster engine operator custom resources definitions from the command line by using the Kubernetes CLI (`kubectl`). List available APIs and inspect CRD details on your managed clusters.

**Required access:** Cluster administrator, or a role with permission to list and get custom resources definitions

<div>

<div class="title">

Prerequisites

</div>

- You installed a supported version of OpenShift Container Platform on your hub cluster. See [Installing OpenShift Container Platform](https://docs.redhat.com/en/documentation/openshift_container_platform/4.20/html/installation_overview/index).

- multicluster engine operator is installed on the hub cluster. If you installed Red Hat Advanced Cluster Management, multicluster engine operator is installed automatically. See [Preparing to install multicluster engine operator](clusters.md#preparing-to-install-mce).

- You configured the OpenShift Container Platform CLI (`oc`) or the Kubernetes CLI (`kubectl`) on your workstation and can run commands against the hub cluster. See [Getting started with the OpenShift CLI](https://docs.redhat.com/en/documentation/openshift_container_platform/4.20/html/cli_tools/openshift-cli-oc#cli-getting-started).

- You are logged in to the hub cluster with credentials that can access API resources.

</div>

<div>

<div class="title">

Procedure

</div>

1.  List the APIs that are available on the cluster:

    ``` bash
    kubectl get crds
    ```

2.  To view details for a specific API, run the following command. Replace `<name>` with the CRD name from the previous step:

    ``` bash
    kubectl describe crd <name>
    ```

</div>

<div>

<div class="title">

Additional resources

</div>

- [Advanced Cluster Management API documentation](https://github.com/stolostron/api-documentation)

</div>

<a id="credentials"></a>

## Managing credentials

A *credential* is required to create and manage a Red Hat OpenShift Container Platform cluster on a cloud service provider with multicluster engine operator. The credential stores the access information for a cloud provider. Each provider account requires its own credential, as does each domain on a single provider.

You can create and manage your cluster credentials. Credentials are stored as Kubernetes secrets. Secrets are copied to the namespace of a managed cluster so that the controllers for the managed cluster can access the secrets. When a credential is updated, the copies of the secret are automatically updated in the managed cluster namespaces.

**Note:** Changes to the pull secret, SSH keys, or base domain of the cloud provider credentials are not reflected for existing managed clusters, as they have already been provisioned using the original credentials.

**Required access:** Edit

- [Creating a credential for Ansible Automation Platform](clusters.md#creating-a-credential-for-ansible)

- [Creating a credential for Amazon Web Services in the console](clusters.md#creating-credential-aws-ui)

- [Creating a credential for Amazon Web Services with the API](clusters.md#creating-credential-aws-api)

- [Creating a credential for Microsoft Azure in the console](clusters.md#creating-credential-azure-ui)

- [Creating a credential for Microsoft Azure with the API](clusters.md#creating-credential-azure-api)

- [Creating a credential for Google Cloud Platform in the console](clusters.md#creating-gcp-credential-ui)

- [Creating a credential for Google Cloud Platform with the API](clusters.md#creating-gcp-credential-api)

- [Creating a credential for VMware vSphere in the console](clusters.md#creating-a-credential-for-vmware-vsphere-ui)

- [Creating a credential for VMware vSphere with the API](clusters.md#creating-a-credential-for-vmware-vsphere-api)

- [Creating a credential for Red Hat OpenStack Platform in the console](clusters.md#creating-a-credential-for-openstack-ui)

- [Creating a credential for Red Hat OpenStack Platform with the API](clusters.md#creating-a-credential-for-openstack-api)

- [Creating a credential for Red Hat OpenShift Cluster Manager](clusters.md#creating-a-credential-for-openshift-cluster-manager)

- [Creating a credential for Ansible Automation Platform](clusters.md#creating-a-credential-for-ansible)

- [Creating a credential for a hosted environment](clusters.md#creating-a-credential-hosted)

<a id="creating-credential-aws-ui"></a>

### Creating a credential for Amazon Web Services in the console

You need a credential to use multicluster engine operator console to deploy and manage an Red Hat OpenShift Container Platform cluster on Amazon Web Services (AWS). This procedure must be done before you can create a cluster with multicluster engine operator. You can also create a credential for AWS with the API. See [Creating a credential for Amazon Web Services with the API](clusters.md#creating-credential-aws-api) for those steps.

**Required access:** Edit

<div>

<div class="title">

Prerequisites

</div>

- A deployed multicluster engine operator hub cluster

- Internet access for your multicluster engine operator hub cluster so it can create the Kubernetes cluster on Amazon Web Services (AWS)

- AWS login credentials, which include access key ID and secret access key. See *Understanding and getting your security credentials*.

- Account permissions that allow installing clusters on AWS. See *Configuring an AWS account* for instructions on how to configure an AWS account.

</div>

<div>

<div class="title">

Procedure

</div>

1.  In the console, click **Credentials** to choose from existing credential options.

2.  Create a name and namespace specifically to host your credentials, both for convenience and added security.

3.  **Optional:** Add a *Base DNS domain* for your credential. If you add the base DNS domain to the credential, it is automatically populated in the correct field when you create a cluster with this credential.

4.  Add your *AWS access key ID* for your AWS account. See *Log in to AWS* to find your ID.

5.  Provide the contents for your new *AWS Secret Access Key*.

6.  Click **Proxy** to enter proxy information in the fields that are provided.

7.  Enter your OpenShift Container Platform pull secret. See *Download your Red Hat OpenShift pull secret* to download your pull secret.

8.  Add your *SSH private key* and *SSH public key*, which allows you to connect to the cluster. You can use an existing key pair, or create a new one with key generation program.

9.  Create a cluster that uses this credential by completing the steps in *Create a cluster on Amazon Web Services* or *Create a cluster on Amazon Web Services GovCloud by using the console*.

10. Edit your credential in the console. If the cluster was created by using this provider connection, then the `<cluster-name>-aws-creds>` secret from `<cluster-namespace>` is updated with the new credentials.

    **Note:** Updating credentials does not work for cluster pool claimed clusters.

11. You can also create an Amazon Simple Storage Service (S3) secret, complete the following substeps from the console:

    1.  Click **Add credential** \> **AWS** \> **S3 Bucket**. If you click **For Hosted Control Plane**, the name and namespace are provided.

    2.  Enter information for the following fields that are provided:

        - `bucket name`: Add the name of the S3 bucket.

        - `aws_access_key_id`: Add your AWS access key ID for your AWS account. Log in to AWS to find your ID.

        - `aws_secret_access_key`: Provide the contents for your new AWS Secret Access Key.

        - `Region`: Enter your AWS region.

12. Delete the credential when you are no longer managing that cluster to protect the information in the credential. Select **Actions** to delete in bulk, or select the options menu beside the credential that you want to delete.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Understanding and getting your security credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/security-creds.html)

- [Installing on AWS](https://docs.redhat.com/en/documentation/openshift_container_platform/4.20/html/installing_on_aws/index)

- [Log in to AWS](https://console.aws.amazon.com/iam/home#/security_credentials)

- [Download your Red Hat OpenShift pull secret](https://console.redhat.com/openshift/install/pull-secret)

- [Installation configuration parameters for AWS](https://docs.redhat.com/en/documentation/openshift_container_platform/4.20/html-single/installing_on_aws/index#installation-config-parameters-aws)

- [Create a cluster on Amazon Web Services](clusters.md#create-a-cluster-on-amazon-web-services)

- [Amazon Web Services console settings](clusters.md#aws-console-settings)

- [Create a cluster on Amazon Web Services GovCloud](clusters.md#create-a-cluster-on-amazon-web-services-govcloud)

- [Create a cluster on Amazon Web Services GovCloud by using the console](clusters.md#create-a-cluster-on-amazon-web-services-govcloud-console)

</div>

<a id="creating-credential-aws-api"></a>

### Creating a credential for Amazon Web Services with the API

You need a credential to use multicluster engine operator console to deploy and manage an Red Hat OpenShift Container Platform cluster on Amazon Web Services (AWS). The credential is a prerequisite for creating a cluster with multicluster engine operator. You can also create a credential for AWS with the console. See [Creating a credential for Amazon Web Services in the console](clusters.md#creating-credential-aws-ui) for those steps.

**Required access:** Edit

<div>

<div class="title">

Prerequisites

</div>

- A deployed multicluster engine operator hub cluster.

- Internet access for your multicluster engine operator hub cluster so it can create the Kubernetes cluster on Amazon Web Services (AWS).

- AWS login credentials, which include access key ID and secret access key. See *Understanding and getting your security credentials*.

- Account permissions that allow installing clusters on AWS. See *Configuring an AWS account* for instructions on how to configure an AWS account.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create an opaque secret by using the API. Apply YAML content in the YAML preview window that is similar to the following example:

    ``` yaml
    kind: Secret
    metadata:
        name: <managed-cluster-name>-aws-creds
        namespace: <managed-cluster-namespace>
    type: Opaque
    data:
        aws_access_key_id: $(echo -n "${AWS_KEY}" | base64 -w0)
        aws_secret_access_key: $(echo -n "${AWS_SECRET}" | base64 -w0)
    ```

    **Notes:**

    - Opaque secrets are not visible in the console.

    - Opaque secrets are created in the managed cluster namespace you chose. Hive uses the opaque secret to provision the cluster. When provisioning the cluster by using the Red Hat Advanced Cluster Management console, the credentials you previoulsy created are copied to the managed cluster namespace as the opaque secret.

2.  Add labels to your credentials to view your secret in the console. For example, the following AWS S3 Bucket `oc label secret` is appended with `type=awss3` and `credentials --from-file=…​.`:

    ``` bash
    oc label secret hypershift-operator-oidc-provider-s3-credentials -n <your-local-cluster-name> "cluster.open-cluster-management.io/type=awss3"
    oc label secret hypershift-operator-oidc-provider-s3-credentials -n <your-local-cluster-name> "cluster.open-cluster-management.io/credentials=credentials="
    ```

</div>

<div>

<div class="title">

Additional resources

</div>

- [Understanding and getting your security credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/security-creds.html)

- [Installing on AWS](https://docs.redhat.com/en/documentation/openshift_container_platform/4.20/html/installing_on_aws/index)

- [Log in to AWS](https://console.aws.amazon.com/iam/home#/security_credentials)

- [Download your Red Hat OpenShift pull secret](https://console.redhat.com/openshift/install/pull-secret)

- [Installation configuration parameters for AWS](https://docs.redhat.com/en/documentation/openshift_container_platform/4.20/html-single/installing_on_aws/index#installation-config-parameters-aws)

- [Create a cluster on Amazon Web Services](clusters.md#create-a-cluster-on-amazon-web-services)

- [Amazon Web Services console settings](clusters.md#aws-console-settings)

- [Create a cluster on Amazon Web Services GovCloud](clusters.md#create-a-cluster-on-amazon-web-services-govcloud)

- [Create a cluster on Amazon Web Services GovCloud by using the console](clusters.md#create-a-cluster-on-amazon-web-services-govcloud-console)

</div>

<a id="creating-credential-azure-ui"></a>

### Creating a credential for Microsoft Azure in the console

You need a credential to use multicluster engine operator console to create and manage a Red Hat OpenShift Container Platform cluster on Microsoft Azure or on Microsoft Azure Government. You can also create a credential for Microsoft Azure with the API. See [Creating a credential for Microsoft Azure with the API](clusters.md#creating-credential-azure-api) for those steps. This procedure is a prerequisite for creating a cluster with multicluster engine operator.

**Required access:** Edit

<div>

<div class="title">

Prerequisites

</div>

- A deployed multicluster engine operator hub cluster.

- Internet access for your multicluster engine operator hub cluster so that it can create the Kubernetes cluster on Azure.

- Azure login credentials, which include your Base Domain Resource Group and Azure Service Principal JSON.See *Microsoft Azure portal* to get your login credentials.

- Account permissions that allow installing clusters on Azure. See *How to configure Cloud Services* and *Configuring an Azure account* for more information.

</div>

<div>

<div class="title">

Procedure

</div>

1.  In the console, click **Credentials** to choose from existing credential options.

2.  Create a name and namespace specifically to host your credentials, both for convenience and added security.

3.  **Optional:** Add a *Base DNS domain* for your credential. If you add the base DNS domain to the credential, it is automatically populated in the correct field when you create a cluster with this credential.

4.  Select whether the environment for your cluster is `AzurePublicCloud` or `AzureUSGovernmentCloud`. The settings are different for the Azure Government environment, so ensure that this is set correctly.

5.  Add your *Base domain resource group name* for your Azure account. This entry is the resource name that you created with your Microsoft Azure account. You can find your Base Domain Resource Group Name by selecting **Home** \> **DNS Zones** in the Azure interface. See *Create an Azure service principal with the Azure CLI* to find your base domain resource group name.

6.  Provide the contents for your *Client ID*. This value is generated as the `appId` property when you create a service principal with the following command. Replace `<service_principal>` with the name of your service principal:

    ``` bash
    az ad sp create-for-rbac --role Contributor --name <service_principal> --scopes <subscription_path>
    ```

7.  Add your *Client Secret*. This value is generated as the `password` property when you create a service principal. Run the following command and replace `<service_principal>` with the name of your service principal:

    ``` bash
    az ad sp create-for-rbac --role Contributor --name <service_principal> --scopes <subscription_path>
    ```

8.  Add your *Subscription ID*. This value is the `id` property in the output of the following command:

    ``` bash
    az account show
    ```

9.  Add your *Tenant ID*. This value is the `tenantId` property in the output of the following command:

    ``` bash
    az account show
    ```

10. If you want to enable a proxy, enter the proxy information.

11. Enter your *Red Hat OpenShift pull secret*. See *Download your Red Hat OpenShift pull secret* to download your pull secret.

12. Add your *SSH private key* and *SSH public key* to use to connect to the cluster. You can use an existing key pair, or create a new pair using a key generation program.

13. Create a cluster that uses this credential by completing the steps in *Create a cluster on Microsoft Azure*.

14. Edit your credential in the console as needed.

15. Delete the credential when you are no longer managing that cluster to protect the information in the credential. Select **Actions** to delete in bulk, or select the options menu beside the credential that you want to delete.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Microsoft Azure portal](https://azure.microsoft.com/en-ca/features/azure-portal)

- [How to configure Cloud Services](https://docs.microsoft.com/en-us/azure/cloud-services/cloud-services-how-to-configure-portal)

- [Configuring an Azure account](https://docs.redhat.com/en/documentation/openshift_container_platform/4.20/html/installing_on_azure/installing-azure-account)

- [Create an Azure service principal with the Azure CLI](https://docs.microsoft.com/en-us/cli/azure/create-an-azure-service-principal-azure-cli)

- [Download your Red Hat OpenShift pull secret](https://console.redhat.com/openshift/install/pull-secret)

- [Generating a key pair for cluster node SSH access](https://docs.redhat.com/en/documentation/openshift_container_platform/4.20/html-single/installing_on_azure/index#ssh-agent-using_installing-azure-preparing-ipi)

- [Create a cluster on Microsoft Azure](clusters.md#create-a-cluster-on-microsoft-azure)

</div>

<a id="creating-credential-azure-api"></a>

### Creating a credential for Microsoft Azure with the API

You need a credential to use multicluster engine operator console to create and manage a Red Hat OpenShift Container Platform cluster on Microsoft Azure or on Microsoft Azure Government. The credential is a prerequisite for creating a cluster with multicluster engine operator. You can also create a credential for Microsoft Azure with the console. See [Creating a credential for Microsoft Azure in the console](clusters.md#creating-credential-azure-ui) for those steps.

**Required access:** Edit

<div>

<div class="title">

Prerequisites

</div>

- A deployed multicluster engine operator hub cluster.

- Internet access for your multicluster engine operator hub cluster so that it can create the Kubernetes cluster on Azure.

- Azure login credentials, which include your Base Domain Resource Group and Azure Service Principal JSON. See *Microsoft Azure portal* to get your login credentials.

- Account permissions that allow installing clusters on Azure. See *How to configure Cloud Services* and *Configuring an Azure account* for more information.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create an opaque secret by using the API for Microsoft Azure. Apply YAML content in the YAML preview window that is similar to the following example:

    ``` yaml
    kind: Secret
    metadata:
        name: <managed-cluster-name>-azure-creds
        namespace: <managed-cluster-namespace>
    type: Opaque
    data:
        baseDomainResourceGroupName: $(echo -n "${azure_resource_group_name}" | base64 -w0)
        osServicePrincipal.json: $(base64 -w0 "${AZURE_CRED_JSON}")
    ```

    **Notes:** \* Opaque secrets are not visible in the console. \* Opaque secrets are created in the managed cluster namespace you chose. Hive uses the opaque secret to provision the cluster. When provisioning the cluster by using the Red Hat Advanced Cluster Management console, the credentials you previously created are copied to the managed cluster namespace as the opaque secret.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Microsoft Azure portal](https://azure.microsoft.com/en-ca/features/azure-portal)

- [How to configure Cloud Services](https://docs.microsoft.com/en-us/azure/cloud-services/cloud-services-how-to-configure-portal)

- [Configuring an Azure account](https://docs.redhat.com/en/documentation/openshift_container_platform/4.20/html/installing_on_azure/installing-azure-account)

- [Create an Azure service principal with the Azure CLI](https://docs.microsoft.com/en-us/cli/azure/create-an-azure-service-principal-azure-cli)

- [Download your Red Hat OpenShift pull secret](https://console.redhat.com/openshift/install/pull-secret)

- [Generating a key pair for cluster node SSH access](https://docs.redhat.com/en/documentation/openshift_container_platform/4.20/html-single/installing_on_azure/index#ssh-agent-using_installing-azure-preparing-ipi)

- [Create a cluster on Microsoft Azure](clusters.md#create-a-cluster-on-microsoft-azure)

</div>

<a id="creating-gcp-credential-ui"></a>

### Creating a credential for Google Cloud Platform in the console

You need a credential to use multicluster engine operator console to create and manage a Red Hat OpenShift Container Platform cluster on Google Cloud Platform (GCP). You also need a credential to create a cluster with multicluster engine operator. Create your credential from the console with the following steps. You can also create an opaque secret with the API by following the steps in [Creating a credential for Google Cloud Platform with the API](clusters.md#creating-gcp-credential-api).

**Required access:** Edit

<div>

<div class="title">

Prerequisites

</div>

- A deployed multicluster engine operator hub cluster

- Internet access for your multicluster engine operator hub cluster so it can create the Kubernetes cluster on GCP

- GCP login credentials, which include user Google Cloud Platform Project ID and Google Cloud Platform service account JSON key. See *Creating and managing projects*.

- Account permissions that allow installing clusters on GCP. See *Configuring a GCP project* for instructions on how to configure an account.

</div>

<div>

<div class="title">

Procedure

</div>

1.  From the multicluster engine operator console, click **Credentials** \> **Credential type** to choose from existing credential options.

2.  Create a name and namespace specifically to host your credentials, for both convenience and security.

3.  **Optional:** Add a *Base DNS domain* for your credential. If you add the base DNS domain to the credential, it is automatically populated in the correct field when you create a cluster with this credential.

4.  Add your *Google Cloud Platform project ID* for your GCP account. See *Log in to GCP* to retrieve your settings.

5.  Add your *Google Cloud Platform service account JSON key*. See the *Create service accounts* documentation to create your service account JSON key. Follow the steps for the GCP console.

6.  Click **Proxy** to enter proxy information in the fields that are provided.

7.  Enter your Red Hat OpenShift pull secret. See *Download your Red Hat OpenShift pull secret* to download your pull secret.

8.  Add your *SSH private key* and *SSH public key* so you can access the cluster. You can use an existing key pair, or create a new pair using a key generation program.

9.  Delete the credential when you are no longer managing that cluster to protect the information in the credential. Select **Actions** to delete in bulk, or select the options menu beside the credential that you want to delete.

</div>

<div>

<div class="title">

Next steps

</div>

- You can use this connection when you create a cluster by completing the steps in *Creating a cluster on Google Cloud Platform*. You can also edit your credential in the console.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Creating and managing projects](https://cloud.google.com/resource-manager/docs/creating-managing-projects)

- [Configuring a GCP project](https://docs.redhat.com/en/documentation/openshift_container_platform/4.20/html/installing_on_gcp/installing-gcp-account)

- [Log in to GCP](https://console.cloud.google.com/apis/credentials/serviceaccountkey)

- [Create service accounts](https://cloud.google.com/iam/docs/service-accounts-create)

- [Download your Red Hat OpenShift pull secret](https://console.redhat.com/openshift/install/pull-secret)

- [Generating a key pair for cluster node SSH access](https://docs.redhat.com/en/documentation/openshift_container_platform/4.20/html-single/installing_on_azure/index#ssh-agent-using_installing-azure-preparing-ipi)

- [Create a cluster on Google Cloud Platform by using the console](clusters.md#create-a-cluster-on-google-cloud-platform-console)

</div>

<a id="creating-gcp-credential-api"></a>

### Creating a credential for Google Cloud Platform with the API

You need a credential to use multicluster engine operator console to create and manage a Red Hat OpenShift Container Platform cluster on Google Cloud Platform (GCP). You need a credential to use multicluster engine operator console to create and manage a Red Hat OpenShift Container Platform cluster on Google Cloud Platform (GCP). You also need a credential to create a cluster with multicluster engine operator. You create an opaque secret with the API. To create a credential from the console, follow the steps in [Creating a credential for Google Cloud Platform in the console](clusters.md#creating-gcp-credential-ui).

**Required access:** Edit

<div>

<div class="title">

Prerequisites

</div>

- A deployed multicluster engine operator hub cluster.

- Internet access for your multicluster engine operator hub cluster so it can create the Kubernetes cluster on GCP.

- GCP login credentials, which include user Google Cloud Platform Project ID and Google Cloud Platform service account JSON key. See *Creating and managing projects*.

- Account permissions that allow installing clusters on GCP. See *Configuring a GCP project* for instructions on how to configure an account.

</div>

<div>

<div class="title">

Procedure

</div>

- Create an opaque secret for by using the API. Apply YAML content that is similar to the following example:

  ``` yaml
  kind: Secret
  metadata:
      name: <managed-cluster-name>-gcp-creds
      namespace: <managed-cluster-namespace>
  type: Opaque
  data:
      osServiceAccount.json: $(base64 -w0 "${GCP_CRED_JSON}")
  ```

  **Notes:**

- Opaque secrets are not visible in the console.

- Opaque secrets are created in the managed cluster namespace you chose. Hive uses the opaque secret to provision the cluster. When provisioning the cluster by using the Red Hat Advanced Cluster Management console, the credentials you previously created are copied to the managed cluster namespace as the opaque secret.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Creating and managing projects](https://cloud.google.com/resource-manager/docs/creating-managing-projects)

- [Configuring a GCP project](https://docs.redhat.com/en/documentation/openshift_container_platform/4.20/html/installing_on_gcp/installing-gcp-account)

- [Log in to GCP](https://console.cloud.google.com/apis/credentials/serviceaccountkey)

- [Create service accounts](https://cloud.google.com/iam/docs/service-accounts-create)

- [Download your Red Hat OpenShift pull secret](https://console.redhat.com/openshift/install/pull-secret)

- [Generating a key pair for cluster node SSH access](https://docs.redhat.com/en/documentation/openshift_container_platform/4.20/html-single/installing_on_azure/index#ssh-agent-using_installing-azure-preparing-ipi)

- [Create a cluster on Google Cloud Platform by using the console](clusters.md#create-a-cluster-on-google-cloud-platform-console)

</div>

<a id="creating-a-credential-for-vmware-vsphere-ui"></a>

### Creating a credential for VMware vSphere in the console

You need a credential to use multicluster engine operator console to deploy and manage a Red Hat OpenShift Container Platform cluster on VMware vSphere. Create your credential from the console with the following steps. You can also create an opaque secret with the API by following the steps in [Creating a credential for VMware vSphere with the API](clusters.md#creating-a-credential-for-vmware-vsphere-api).

**Required access:** Edit

<div>

<div class="title">

Prerequisites

</div>

- You must create a credential for VMware vSphere before you can create a cluster with multicluster engine operator.

- A deployed hub cluster on a supported OpenShift Container Platform version.

- Internet access for your hub cluster so it can create the Kubernetes cluster on VMware vSphere.

- VMware vSphere login credentials and vCenter requirements configured for OpenShift Container Platform when using installer-provisioned infrastructure. See *Installing a cluster on vSphere with customizations*. These credentials include the following information:

  - vCenter account privileges.

  - Cluster resources.

  - DHCP available.

  - ESXi hosts have time synchronized (for example, NTP).

</div>

<div>

<div class="title">

Procedure

</div>

1.  In the console, click **Credentials** to choose from existing credential options.

2.  Create a name and namespace specifically to host your credentials, both for convenience and added security.

3.  Add your *VMware vCenter server fully-qualified host name or IP address*. The value must be defined in the vCenter server root CA certificate. If possible, use the fully-qualified host name.

4.  Add your *VMware vCenter username*.

5.  Add your *VMware vCenter password*.

6.  Add your *VMware vCenter root CA certificate*.

    1.  You can download your certificate in the `download.zip` package with the certificate from your VMware vCenter server at: `https://<vCenter_address>/certs/download.zip`. Replace *vCenter_address* with the address to your vCenter server.

    2.  Unpackage the `download.zip`.

    3.  Use the certificates from the `certs/<platform>` directory that have a `.0` extension.

        **Tip:** You can use the `ls certs/<platform>` command to list all of the available certificates for your platform.

        Replace `<platform>` with the abbreviation for your platform: `lin`, `mac`, or `win`.

        For example: `certs/lin/3a343545.0`

        **Best practice:** Link together multiple certificates with a `.0` extension by running the `cat certs/lin/*.0 > ca.crt` command.

    4.  Add your *VMware vSphere cluster name*.

    5.  Add your *VMware vSphere datacenter*.

    6.  Add your *VMware vSphere default datastore*.

    7.  Add your *VMware vSphere disk type*.

    8.  Add your *VMware vSphere folder*.

    9.  Add your *VMware vSphere resource pool*.

7.  For disconnected installations only: Complete the fields in the **Configuration for disconnected installation** subsection with the required information:

    - *Cluster OS image*: This value contains the URL to the image to use for Red Hat OpenShift Container Platform cluster machines.

    - *Image content source*: This value contains the disconnected registry path. The path contains the hostname, port, and repository path to all of the installation images for disconnected installations. Example: `repository.com:5000/openshift/ocp-release`.

      The path creates an image content source policy mapping in the `install-config.yaml` to the Red Hat OpenShift Container Platform release images. As an example, `repository.com:5000` produces this `imageContentSource` content:

      ``` yaml
      - mirrors:
        - registry.example.com:5000/ocp4
        source: quay.io/openshift-release-dev/ocp-release-nightly
      - mirrors:
        - registry.example.com:5000/ocp4
        source: quay.io/openshift-release-dev/ocp-release
      - mirrors:
        - registry.example.com:5000/ocp4
        source: quay.io/openshift-release-dev/ocp-v4.0-art-dev
      ```

    - *Additional trust bundle*: This value provides the contents of the certificate file that is required to access the mirror registry.

      **Note:** If you are deploying managed clusters from a hub that is in a disconnected environment, and want them to be automatically imported post install, add an Image Content Source Policy to the `install-config.yaml` file by using the `YAML` editor. A sample entry is shown in the following example:

    ``` yaml
    - mirrors:
      - registry.example.com:5000/rhacm2
      source: registry.redhat.io/rhacm2
    ```

8.  If you want to enable a proxy, enter the proxy information.

9.  Enter your Red Hat OpenShift pull secret. See *Download your Red Hat OpenShift pull secret* to download your pull secret.

10. Add your *SSH private key* and *SSH public key*, which allows you to connect to the cluster. You can use an existing key pair, or create a new one with key generation program.

11. Click **Create**.

12. Review the new credential information, then click **Add**. When you add the credential, it is added to the list of credentials.

13. Create a cluster that uses this uses this credential by completing the steps in *Create a cluster on VMware vSphere*.

14. Edit your credential in the console.

15. Delete the credential when you are no longer managing that cluster to protect the information in the credential. Select **Actions** to delete in bulk, or select the options menu beside the credential that you want to delete

</div>

<div>

<div class="title">

Additional resources

</div>

- [Installing a cluster on vSphere with customizations](https://docs.redhat.com/en/documentation/openshift_container_platform/4.19/html/installing_on_vmware_vsphere/installer-provisioned-infrastructure#installing-vsphere-installer-provisioned-customizations)

- [Download your Red Hat OpenShift pull secret](https://console.redhat.com/openshift/install/pull-secret)

- [Generating a key pair for cluster node SSH access](https://docs.redhat.com/en/documentation/openshift_container_platform/4.19/html-single/installing_on_vmware_vsphere/index#ssh-agent-using_ipi-vsphere-preparing-to-install)

- [Create a cluster on VMware vSphere](clusters.md#create-a-cluster-on-vmware-vsphere)

- [VMware vSphere console settings](clusters.md#vsphere-console-settings)

</div>

<a id="creating-a-credential-for-vmware-vsphere-api"></a>

### Creating a credential for VMware vSphere with the API

Create an opaque secret with the API. You need a credential to use multicluster engine operator console to deploy and manage a Red Hat OpenShift Container Platform cluster on VMware vSphere. You can also create a credential from the console by following the steps in [Creating a credential for VMware vSphere in the console](clusters.md#creating-a-credential-for-vmware-vsphere-ui).

**Required access:** Edit

<div>

<div class="title">

Prerequisites

</div>

- You must create a credential for VMware vSphere before you can create a cluster with multicluster engine operator.

- A deployed hub cluster on a supported OpenShift Container Platform version.

- Internet access for your hub cluster so that it can create the Kubernetes cluster on VMware vSphere.

- VMware vSphere login credentials and vCenter requirements configured for OpenShift Container Platform when using installer-provisioned infrastructure. See *Installing a cluster on vSphere with customizations*. These credentials include the following information:

  - vCenter account privileges.

  - Cluster resources.

  - DHCP available.

  - ESXi hosts have time synchronized (for example, NTP).

</div>

<div>

<div class="title">

Procedure

</div>

- Create an opaque secret for by using the API. Apply YAML content that is similar to the following example:

</div>

``` yaml
kind: Secret
metadata:
    name: <managed-cluster-name>-vsphere-creds
    namespace: <managed-cluster-namespace>
type: Opaque
data:
    username: $(echo -n "${VMW_USERNAME}" | base64 -w0)
    password.json: $(base64 -w0 "${VMW_PASSWORD}")
```

\+ **Notes:** - Opaque secrets are not visible in the console. - Opaque secrets are created in the managed cluster namespace you chose. Hive uses the opaque secret to provision the cluster. When provisioning the cluster by using the Red Hat Advanced Cluster Management console, the credentials you previoulsy created are copied to the managed cluster namespace as the opaque secret.

<div>

<div class="title">

Additional resources

</div>

- [Installing a cluster on vSphere with customizations](https://docs.redhat.com/en/documentation/openshift_container_platform/4.19/html/installing_on_vmware_vsphere/installer-provisioned-infrastructure#installing-vsphere-installer-provisioned-customizations)

- [Download your Red Hat OpenShift pull secret](https://console.redhat.com/openshift/install/pull-secret)

- [Generating a key pair for cluster node SSH access](https://docs.redhat.com/en/documentation/openshift_container_platform/4.19/html-single/installing_on_vmware_vsphere/index#ssh-agent-using_ipi-vsphere-preparing-to-install)

- [Create a cluster on VMware vSphere](clusters.md#create-a-cluster-on-vmware-vsphere)

- [VMware vSphere console settings](clusters.md#vsphere-console-settings)

</div>

<a id="creating-a-credential-for-openstack-ui"></a>

### Creating a credential for Red Hat OpenStack in the console

You need a credential to use multicluster engine operator console to deploy and manage a supported Red Hat OpenShift Container Platform cluster on Red Hat OpenStack Platform. You must create a credential for Red Hat OpenStack Platform before you can create a cluster with multicluster engine operator. You can also create a credential by using the API. See [Creating a credential for Red Hat OpenStack Platform with the API](clusters.md#creating-a-credential-for-openstack-api) for those steps.

<div>

<div class="title">

Prerequisites

</div>

- A deployed hub cluster on a supported OpenShift Container Platform version.

- Internet access for your hub cluster so that it can create the Kubernetes cluster on Red Hat OpenStack Platform.

- Red Hat OpenStack Platform login credentials and Red Hat OpenStack Platform requirements configured for OpenShift Container Platform when using installer-provisioned infrastructure. See *Installing a cluster on OpenStack with customizations*.

- Download or create a `clouds.yaml` file for accessing the CloudStack API. Within the `clouds.yaml` file:

  - Determine the `cloud auth` section name to use.

  - Add a line for the **password**, immediately following the **username** line.

</div>

<div>

<div class="title">

Procedure

</div>

1.  In the console, click **Credentials** to choose from existing credential options.

2.  Create a name and namespace specifically to host your credentials, both for convenience and added security.

3.  **Optional:** Add a *Base DNS domain* for your credential. If you add the base DNS domain to the credential, it is automatically populated in the correct field when you create a cluster with this credential.

4.  Add your Red Hat OpenStack Platform `clouds.yaml` file contents. The contents of the `clouds.yaml` file, including the password, provide the required information for connecting to the Red Hat OpenStack Platform server. The file contents must include the password, which you add to a new line immediately after the `username`.

5.  Add your Red Hat OpenStack Platform cloud name. This entry is the name that is specified in the cloud section of the `clouds.yaml` to use for establishing communication to the Red Hat OpenStack Platform server.

6.  **Optional**: For configurations that use an internal certificate authority, enter your certificate in the **Internal CA certificate** field to automatically update your `clouds.yaml` with the certificate information.

7.  **For disconnected installations only:** Complete the fields in the **Configuration for disconnected installation** subsection with the required information:

    - *Cluster OS image*: This value contains the URL to the image to use for Red Hat OpenShift Container Platform cluster machines.

    - *Image content sources*: This value contains the disconnected registry path. The path contains the hostname, port, and repository path to all of the installation images for disconnected installations. Example: `repository.com:5000/openshift/ocp-release`. The path creates an image content source policy mapping in the `install-config.yaml` to the Red Hat OpenShift Container Platform release images. As an example, `repository.com:5000` produces this `imageContentSource` content:

      ``` yaml
      - mirrors:
        - registry.example.com:5000/ocp4
        source: quay.io/openshift-release-dev/ocp-release-nightly
      - mirrors:
        - registry.example.com:5000/ocp4
        source: quay.io/openshift-release-dev/ocp-release
      - mirrors:
        - registry.example.com:5000/ocp4
        source: quay.io/openshift-release-dev/ocp-v4.0-art-dev
      ```

    - *Additional trust bundle*: This value provides the contents of the certificate file that is required to access the mirror registry.

      **Note:** If you are deploying managed clusters from a hub that is in a disconnected environment, and want them to be automatically imported post install, add an Image Content Source Policy to the `install-config.yaml` file by using the `YAML` editor. A sample entry is shown in the following example:

    ``` yaml
    - mirrors:
      - registry.example.com:5000/rhacm2
      source: registry.redhat.io/rhacm2
    ```

8.  If you want to enable a proxy, enter the proxy information.

9.  Enter your Red Hat OpenShift pull secret. See *Download your Red Hat OpenShift pull secret* to download your pull secret.

10. Add your SSH Private Key and SSH Public Key, which allows you to connect to the cluster. You can use an existing key pair, or create a new one with key generation program.

11. Click **Create**.

12. Review the new credential information, then click **Add**. When you add the credential, it is added to the list of credentials.

13. Create a cluster that uses this credential by completing the steps in *Create a cluster on Red Hat OpenStack Platform*. You can edit your credential in the console.

14. Delete the credential when you are no longer managing that cluster to protect the information in the credential. Select **Actions** to delete in bulk, or select the options menu beside the credential that you want to delete.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Installing a cluster on OpenStack with customizations](https://docs.redhat.com/en/documentation/openshift_container_platform/4.19/html/installing_on_openstack/installing-openstack-installer-custom)

- [Download your Red Hat OpenShift pull secret](https://console.redhat.com/openshift/install/pull-secret)

- [Generating a key pair for cluster node SSH access](https://docs.redhat.com/en/documentation/openshift_container_platform/4.19/html/installing_on_openstack/installing-openstack-installer-custom#ssh-agent-using_installing-openstack-installer-custom)

- [Create a cluster on Red Hat OpenStack Platform](clusters.md#create-a-cluster-on-openstack)

- [Red Hat OpenStack Platform console settings](clusters.md#openstack-console-settings)

</div>

<a id="creating-a-credential-for-openstack-api"></a>

### Creating a credential for Red Hat OpenStack with the API

You need a credential to use multicluster engine operator console to deploy and manage a supported Red Hat OpenShift Container Platform cluster on Red Hat OpenStack Platform. You must create a credential for Red Hat OpenStack Platform before you can create a cluster with multicluster engine operator. You can also create a credential by using the console. See [Creating a credential for Red Hat OpenStack Platform in the console](clusters.md#creating-a-credential-for-openstack-ui) for those steps.

<div>

<div class="title">

Prerequisites

</div>

- A deployed hub cluster on a supported OpenShift Container Platform version.

- Internet access for your hub cluster so that it can create the Kubernetes cluster on Red Hat OpenStack Platform.

- Red Hat OpenStack Platform login credentials and Red Hat OpenStack Platform requirements configured for OpenShift Container Platform when using installer-provisioned infrastructure. See *Installing a cluster on OpenStack with customizations*.

- Download or create a `clouds.yaml` file for accessing the CloudStack API. Within the `clouds.yaml` file:

  - Determine the `cloud auth` section name to use.

  - Add a line for the **password**, immediately following the **username** line.

</div>

<div>

<div class="title">

Procedure

</div>

- Create an opaque secret for by using the API. Apply YAML content that is similar to the following example:

  ``` yaml
  kind: Secret
  metadata:
      name: <managed-cluster-name>-osp-creds
      namespace: <managed-cluster-namespace>
  type: Opaque
  data:
      clouds.yaml: $(base64 -w0 "${OSP_CRED_YAML}") cloud: $(echo -n "openstack" | base64 -w0)
  ```

  **Notes:**

- Opaque secrets are not visible in the console.

- Opaque secrets are created in the managed cluster namespace you chose. Hive uses the opaque secret to provision the cluster. When provisioning the cluster by using the Red Hat Advanced Cluster Management console, the credentials you previously created are copied to the managed cluster namespace as the opaque secret.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Installing a cluster on OpenStack with customizations](https://docs.redhat.com/en/documentation/openshift_container_platform/4.19/html/installing_on_openstack/installing-openstack-installer-custom)

- [Download your Red Hat OpenShift pull secret](https://console.redhat.com/openshift/install/pull-secret)

- [Generating a key pair for cluster node SSH access](https://docs.redhat.com/en/documentation/openshift_container_platform/4.19/html/installing_on_openstack/installing-openstack-installer-custom#ssh-agent-using_installing-openstack-installer-custom)

- [Create a cluster on Red Hat OpenStack Platform](clusters.md#create-a-cluster-on-openstack)

- [Red Hat OpenStack Platform console settings](clusters.md#openstack-console-settings)

</div>

<a id="creating-a-credential-for-openshift-cluster-manager"></a>

### Creating a credential for Red Hat OpenShift Cluster Manager

Add an OpenShift Cluster Manager credential so that you can discover clusters. You need to add your credential to discover clusters. To create a credential from the multicluster engine operator console, complete the steps in the console:

**Required access:** Administrator

<div>

<div class="title">

Prerequisites

</div>

- You need an API token for the OpenShift Cluster Manager account, or you can use a separate Service Account.

- To obtain an API token, see [Downloading the OpenShift Cluster Manager API token](https://docs.redhat.com/en/documentation/openshift_cluster_manager/1-latest/html/managing_clusters/assembly-managing-clusters#downloading-ocm-api-token_downloading-and-updating-pull-secrets).

- To use a Service Account, you must obtain the client ID and client secret when you are creating the Service Account. Enter the credentials to create the OpenShift Cluster Manager credential on your multicluster engine for Kubernetes operator. See [Creating and managing a service account](https://docs.redhat.com/en/documentation/red_hat_hybrid_cloud_console/1-latest/html/creating_and_managing_service_accounts/proc-ciam-svc-acct-overview-creating-service-acct).

</div>

<div>

<div class="title">

Procedure

</div>

1.  From the multicluster engine operator console, click **Credentials** to choose from existing credential options.

2.  Select the Red Hat OpenShift Cluster Manager option.

3.  Create a name and namespace specifically to host your credentials, for both convenience and security.

4.  Click **OpenShift Cluster Manager** to choose your Authentication method and enter your API credential information in the fields that are provided.

5.  Delete the credential when you are no longer managing that cluster to protect the information in the credential. Select **Actions** to delete in bulk, or select the options menu beside the credential that you want to delete. If your credential is removed, or your OpenShift Cluster Manager API token expires or is revoked, then the associated discovered clusters are removed.

</div>

<a id="creating-a-credential-for-ansible"></a>

### Creating a credential for Ansible Automation Platform

You need a credential to use multicluster engine operator console to deploy and manage an Red Hat OpenShift Container Platform cluster that is using Red Hat Ansible Automation Platform. This procedure must be done before you can create an Automation template to enable automation on a cluster.

**Required access:** Edit

<div>

<div class="title">

Prerequisites

</div>

- A deployed multicluster engine operator hub cluster.

- Ansible login credentials, which includes Ansible Automation Platform hostname and OAuth token; see [Credentials for Ansible Automation Platform](https://docs.ansible.com/ansible-tower/latest/html/userguide/credentials.html).

- Account permissions that allow you to install hub clusters and work with Ansible. Learn more about [Ansible users](https://docs.ansible.com/ansible-tower/latest/html/userguide/users.html).

</div>

<div>

<div class="title">

Procedure

</div>

1.  In the console, click **Credentials** to choose from existing credential options.

2.  Create a namespace specifically to host your credentials, both for convenience and added security.

    **Important:** The Ansible Token and host URL that you provide when you create your Ansible credential are automatically updated for the automation that use that credential when you edit the credential. The updates are copied to any automations that use that Ansible credential, including those related to cluster lifecycle, governance, and application management automations. This ensures that the automations continue to run after the credential is updated.

3.  Edit your credential in the console. Ansible credentials are automatically updated in your automation that use that credential when you update them in the credential.

4.  Create an Ansible Job that uses this credential by completing the steps in [Ansible Automation Platform for cluster management](clusters.md#ansible-intro).

5.  Delete the credential when you are no longer managing that cluster to protect the information in the credential. Select **Actions** to delete in bulk, or select the options menu beside the credential that you want to delete.

</div>

<a id="creating-a-credential-hosted"></a>

### Creating a credential for a hosted environment

You need a credential to use the console to deploy and manage a Red Hat OpenShift Container Platform cluster in an on-premises environment. The credential specifies the connections that are used for the cluster.

**Required access:** Edit

<div>

<div class="title">

Prerequisites

</div>

- A hub cluster that is deployed.

- Internet access for your hub cluster so it can create the Kubernetes cluster on your infrastructure environment.

- For a disconnected environment, you must have a configured mirror registry where you can copy the release images for your cluster creation. See [Mirroring in disconnected environments](https://docs.redhat.com/en/documentation/openshift_container_platform/4.20/html-single/disconnected_environments/mirroring-in-disconnected-environments) in the OpenShift Container Platform documentation for more information.

- Account permissions that support installing clusters on the on-premises environment.

</div>

<div>

<div class="title">

Procedure

</div>

1.  In the console, click **Credentials** to choose from existing credential options.

2.  Create a namespace specifically to host your credentials, both for convenience and added security.

3.  Select **Host inventory** for your credential type.

4.  **Optional:** Add a *Base DNS domain* for your credential. If you add the base DNS domain to the credential, it is automatically populated in the correct field when you create a cluster with this credential.

5.  Enter your *Red Hat OpenShift pull secret*. This pull secret is automatically entered when you create a cluster and specify this credential. You can download your pull secret from [Pull secret](https://console.redhat.com/openshift/install/pull-secret). See [Using image pull secrets](https://docs.redhat.com/en/documentation/openshift_container_platform/4.20/html/images/managing-images#using-image-pull-secrets) for more information about pull secrets.

6.  Enter your `SSH public key`. This `SSH public key` is also automatically entered when you create a cluster and specify this credential.

7.  Select **Add** to create your credential.

8.  Delete the credential when you are no longer managing that cluster to protect the information in the credential. Select **Actions** to delete in bulk, or select the options menu beside the credential that you want to delete.

</div>

<div class="formalpara">

<div class="title">

Next steps

</div>

You can create a cluster that uses this credential by completing the steps in [Create a cluster in an on-premises environment by using the CLI](clusters.md#create-a-cluster-on-premises-cli) or [Create a cluster in an on-premises environment by using the console](clusters.md#create-a-cluster-on-premises-console).

</div>

<a id="cluster-intro"></a>

## Cluster lifecycle introduction

The multicluster engine operator is the cluster lifecycle operator that provides cluster management capabilities for OpenShift Container Platform and Red Hat Advanced Cluster Management hub clusters. The multicluster engine operator is a software operator that enhances cluster fleet management and supports OpenShift Container Platform cluster lifecycle management across clouds and data centers. You can use multicluster engine operator with or without Red Hat Advanced Cluster Management. Red Hat Advanced Cluster Management also installs multicluster engine operator automatically and offers further multicluster capabilities.

See the following documentation:

- [Cluster lifecycle architecture](clusters.md#cluster-lifecycle-arch)

- [Managing credentials overview](clusters.md#credentials)

- [Release images](clusters.md#release-images-intro)

- [Creating clusters](clusters.md#create-intro)

- [Cluster import](clusters.md#import-intro)

- [Accessing your cluster](clusters.md#accessing-your-cluster)

- [Scaling managed clusters](clusters.md#scaling-managed-intro)

- [Hibernating a created cluster](clusters.md#hibernating-a-created-cluster)

- [Updating your cluster](clusters.md#updating-your-cluster)

- [Cluster proxy](clusters.md#proxy-intro)

- [Ansible Automation Platform for cluster management](clusters.md#ansible-intro)

- [ClusterClaims](clusters.md#clusterclaims)

- [*ManagedClusterSets*](clusters.md#managedclustersets-intro)

- [Placement](clusters.md#placement-intro)

- [Cluster pools (Technology Preview)](clusters.md#managing-cluster-pools)

- [Enabling ManagedServiceAccount](clusters.md#managed-serviceaccount-addon)

- [Configure the klusterlet to run on specific nodes](clusters.md#config-klusterlet-nodes)

- [Cluster removal overview](clusters.md#remove-managed-cluster)

<a id="cluster-lifecycle-arch"></a>

### Cluster lifecycle architecture

Cluster lifecycle requires two types of clusters: *hub clusters* and *managed clusters*.

The hub cluster is the OpenShift Container Platform (or Red Hat Advanced Cluster Management) main cluster with the multicluster engine operator automatically installed. You can create, manage, and monitor other Kubernetes clusters with the hub cluster. You can create clusters by using the hub cluster, while you can also import existing clusters to be managed by the hub cluster.

When you create a managed cluster, the cluster is created using the Red Hat OpenShift Container Platform cluster installer with the Hive resource. See more information about the process of installing clusters with the OpenShift Container Platform installer by reading [Installing and configuring OpenShift Container Platform clusters](https://docs.redhat.com/en/documentation/openshift_container_platform/4.20/html/installation_overview/index) in the OpenShift Container Platform documentation.

The following diagram shows the components that are installed with the multicluster engine for Kubernetes operator for cluster management:

![Cluster lifecycle architecture diagram](assets/712890b895996d63d86a.png)

The components of the cluster lifecycle management architecture include the following items:

<a id="components-hub-mce"></a>

#### Hub cluster

- The *managed cluster import controller* deploys the klusterlet operator to the managed clusters.

- The *Hive controller* provisions the clusters that you create by using the multicluster engine for Kubernetes operator. The Hive Controller also destroys managed clusters that were created by the multicluster engine for Kubernetes operator.

- The *cluster curator controller* creates the Ansible jobs as the pre-hook or post-hook to configure the cluster infrastructure environment when creating or upgrading managed clusters.

- When a managed cluster add-on is enabled on the hub cluster, its *add-on hub controller* is deployed on the hub cluster. The *add-on hub controller* deploys the *add-on agent* to the managed clusters.

<a id="components-managed-mce"></a>

#### Managed cluster

- The *klusterlet operator* deploys the klusterlet agent on the managed cluster.

- The *klusterlet agent* handles both cluster registration and work management functions. It registers the managed cluster and the managed cluster add-ons with the hub cluster, maintains the status of the managed cluster and the managed cluster add-ons, and applies add-on agents to the managed cluster. The following permissions are automatically created within the Clusterrole to allow the managed cluster to access the hub cluster:

  - Allows the agent to get or update its owned cluster that the hub cluster manages

  - Allows the agent to update the status of its owned cluster that the hub cluster manages

  - Allows the agent to rotate its certificate

  - Allows the agent to `get` or `update` the `coordination.k8s.io` lease

  - Allows the agent to `get` its managed cluster add-ons

  - Allows the agent to update the status of its managed cluster add-ons

  - Allows the agent to send events to the hub cluster

To continue adding and managing clusters, see the [Cluster lifecycle introduction](clusters.md#cluster-intro).

<a id="release-images-intro"></a>

## Release images

The release image identifies the version of the Red Hat OpenShift Container Platform image that is used to create the cluster. When you build your cluster, use the version that the release image specifies. By default, OpenShift Container Platform uses the `clusterImageSets` resources to get the list of supported release images.

<div>

<div class="title">

Additional resources

</div>

- [Specify release images](clusters.md#release-images-specify)

- [Locate *ClusterImageSets*](clusters.md#cluster-image-set)

- [Configure *ClusterImageSets*](clusters.md#config-cluster-image-set)

- [Create a release image to deploy a cluster on a different architecture](clusters.md#manual-release-image-cross-arch)

- [Maintain a custom list of release images while connected](clusters.md#release-images-connected)

- [Maintain a custom list of release images while disconnected](clusters.md#release-images-disconnected)

- [Synchronize available release images](clusters.md#sync-release-images)

- [Refresh the release images list](clusters.md#refresh-release-images)

</div>

<a id="release-images-specify"></a>

### Specify release images

When you create a cluster on a provider by using multicluster engine for Kubernetes operator, you need to specify a release image to use for your new cluster.

<div>

<div class="title">

Prerequisites

</div>

- You need access to the GitHub repository for the YAML files that reference the release images. See link:https://github.com/stolostron/acm-hive-openshift-releases \[acm-hive-openshift-releases\].

</div>

<div>

<div class="title">

Procedure

</div>

1.  Locate the release image that you want to use for your cluster. See [Locate *ClusterImageSets*](clusters.md#cluster-image-set) for information about how to locate the release image you want to use.

2.  Configure a *ClusterImageSet* resource to use the release image that you want. See [Configure *ClusterImageSets*](clusters.md#config-cluster-image-set) for information about how to configure a *ClusterImageSet* resource.

3.  Create a cluster on an architecture that is different from the architecture of the hub cluster. See [Create a release image to deploy a cluster on a different architecture](clusters.md#manual-release-image-cross-arch).

</div>

<a id="cluster-image-set"></a>

### Locate *ClusterImageSets*

The YAML files referencing the release images are maintained in the *acm-hive-openshift-releases* GitHub repository. The files are used to create the list of the available release images in the console. This includes the latest fast channel images from OpenShift Container Platform.

The console only displays the latest release images for the three latest versions of OpenShift Container Platform. For example, you might see the following release image displayed in the console options, with \<4.x\> changed to the proper release version that you are using:

`quay.io/openshift-release-dev/ocp-release:<4.x>.1-x86_64`

The console displays the latest versions to help you create a cluster with the latest release images. If you need to create a cluster that is a specific version, older release image versions are also available.

**Note:** You can only select images with the `visible: 'true'` label when creating clusters in the console. An example of this label in a `ClusterImageSet` resource is provided in the following content. Replace `4.x.1` with the current version of the product:

``` yaml
apiVersion: hive.openshift.io/v1
kind: ClusterImageSet
metadata:
  labels:
    channel: fast
    visible: 'true'
  name: img4.x.1-x86-64-appsub
spec:
  releaseImage: quay.io/openshift-release-dev/ocp-release:4.x.1-x86_64
```

Additional release images are stored, but are not visible in the console. To view all of the available release images, run the following command:

``` bash
oc get clusterimageset
```

The repository has the `clusterImageSets` directory, which is the directory that you use when working with the release images. The `clusterImageSets` directory has the following directories:

- Fast: Contains files that reference the latest versions of the release images for each supported OpenShift Container Platform version. The release images in this folder are tested, verified, and supported.

- Releases: Contains files that reference all of the release images for each OpenShift Container Platform version (stable, fast, and candidate channels)

  **Note:** These releases have not all been tested and determined to be stable.

- Stable: Contains files that reference the latest two stable versions of the release images for each supported OpenShift Container Platform version.

  **Note:** By default, the current list of release images updates one time every hour. After upgrading the product, it might take up to one hour for the list to reflect the recommended release image versions for the new version of the product.

<a id="config-cluster-image-set"></a>

### Configure *ClusterImageSets*

You can configure your `ClusterImageSets` with 3 options.

<div>

<div class="title">

Procedure

</div>

- Option 1: To create a cluster in the console, specify the image reference for the specific `ClusterImageSet` that you want to use. Each new entry you specify persists and is available for all future cluster provisions. See the following example entry:

  ``` bash
  quay.io/openshift-release-dev/ocp-release:4.6.8-x86_64
  ```

- Option 2: Manually create and apply a `ClusterImageSets` YAML file from the `acm-hive-openshift-releases` GitHub repository.

- Option 3: To enable automatic updates of `ClusterImageSets` from a forked GitHub repository, follow the `README.md` in the *cluster-image-set-controller* GitHub repository.

</div>

<div>

<div class="title">

Additional resources

</div>

- [cluster-image-set-controller README](https://github.com/stolostron/cluster-image-set-controller/blob/main/README.md)

</div>

<a id="manual-release-image-cross-arch"></a>

### Create a release image to deploy a cluster on a different architecture

You can create a cluster on an architecture that is different from the architecture of the hub cluster by manually creating a release image that has the files for both architectures.

For example, you might need to create an `x86_64` cluster from a hub cluster that is running on the `ppc64le`, `aarch64`, or `s390x` architecture. If you create the release image with both sets of files, the cluster creation succeeds because the new release image enables the OpenShift Container Platform release registry to provide a multi-architecture image manifest.

OpenShift Container Platform supports multiple architectures by default.

<div>

<div class="title">

Procedure

</div>

1.  Use the following `clusterImageSet` to provision a cluster. Replace `4.x.0` with the current supported version:

</div>

``` yaml
apiVersion: hive.openshift.io/v1
kind: ClusterImageSet
metadata:
  labels:
    channel: fast
    visible: 'true'
  name: img4.x.0-multi-appsub
spec:
  releaseImage: quay.io/openshift-release-dev/ocp-release:4.x.0-multi
```

1.  To create the release image for OpenShift Container Platform images that do not support multiple architectures, complete steps similar to the following example for your architecture type:

    1.  From the [OpenShift Container Platform release registry](clusters.md), create a [manifest list](clusters.md) that includes `x86_64`, `s390x`, `aarch64`, and `ppc64le` release images.

    2.  Pull the manifest lists for both architectures in your environment from the [Quay repository](clusters.md) by running the following example commands. Replace `4.x.1` with the current version of the product:

        ``` bash
        podman pull quay.io/openshift-release-dev/ocp-release:4.x.1-x86_64
        podman pull quay.io/openshift-release-dev/ocp-release:4.x.1-ppc64le
        podman pull quay.io/openshift-release-dev/ocp-release:4.x.1-s390x
        podman pull quay.io/openshift-release-dev/ocp-release:4.x.1-aarch64
        ```

    3.  Log in to your private repository where you maintain your images by running the following command. Replace `<private-repo>` with the path to your repository:

        ``` bash
        podman login <private-repo>
        ```

    4.  Add the release image manifest to your private repository by running the following commands that apply to your environment. Replace `4.x.1` with the current version of the product. Replace `<private-repo>` with the path to your repository:

        ``` bash
        podman push quay.io/openshift-release-dev/ocp-release:4.x.1-x86_64 <private-repo>/ocp-release:4.x.1-x86_64
        podman push quay.io/openshift-release-dev/ocp-release:4.x.1-ppc64le <private-repo>/ocp-release:4.x.1-ppc64le
        podman push quay.io/openshift-release-dev/ocp-release:4.x.1-s390x <private-repo>/ocp-release:4.x.1-s390x
        podman push quay.io/openshift-release-dev/ocp-release:4.x.1-aarch64 <private-repo>/ocp-release:4.x.1-aarch64
        ```

    5.  Create a manifest for the new information by running the following command:

        ``` bash
        podman manifest create mymanifest
        ```

    6.  Add references to both release images to the manifest list by running the following commands. Replace `4.x.1` with the current version of the product. Replace `<private-repo>` with the path to your repository:

        ``` bash
        podman manifest add mymanifest <private-repo>/ocp-release:4.x.1-x86_64
        podman manifest add mymanifest <private-repo>/ocp-release:4.x.1-ppc64le
        podman manifest add mymanifest <private-repo>/ocp-release:4.x.1-s390x
        podman manifest add mymanifest <private-repo>/ocp-release:4.x.1-aarch64
        ```

    7.  Merge the list in your manifest list with the existing manifest by running the following command. Replace `<private-repo>` with the path to your repository. Replace `4.x.1` with the current version:

    ``` bash
    podman manifest push mymanifest docker://<private-repo>/ocp-release:4.x.1
    ```

2.  On the hub cluster, create a release image that references the manifest in your repository.

    1.  Create a YAML file that contains information that is similar to the following example. Replace `<private-repo>` with the path to your repository. Replace `4.x.1` with the current version:

        ``` yaml
        apiVersion: hive.openshift.io/v1
        kind: ClusterImageSet
        metadata:
          labels:
            channel: fast
            visible: "true"
          name: img4.x.1-appsub
        spec:
          releaseImage: <private-repo>/ocp-release:4.x.1
        ```

    2.  Run the following command on your hub cluster to apply the changes. Replace `<file-name>` with the name of the YAML file that you created in the previous step:

    ``` bash
    oc apply -f <file-name>.yaml
    ```

3.  Select the new release image when you create your OpenShift Container Platform cluster.

4.  If you deploy the managed cluster by using the Red Hat Advanced Cluster Management console, specify the architecture for the managed cluster in the *Architecture* field during the cluster creation process.

    **Note:** The creation process uses the merged release images to create the cluster.

<a id="release-images-connected"></a>

### Maintain a custom list of release images when connected

You might want to use the same release image for all of your clusters. To simplify, create your own custom list of release images that are available when creating a cluster. Complete the following steps to manage your available release images:

<div>

<div class="title">

Procedure

</div>

1.  Fork the [acm-hive-openshift-releases GitHub](https://github.com/stolostron/acm-hive-openshift-releases/tree/backplane-2.10).

2.  Add the YAML files for the images that you want available when you create a cluster. Add the images to the `./clusterImageSets/stable/` or `./clusterImageSets/fast/` directory by using the Git console or the terminal.

3.  Create a `ConfigMap` file in the `multicluster-engine` namespace that is named `cluster-image-set-git-repo`. See the following example, but replace `mce-version` with you current version of multicluster engine operator, for example, `2.11`:

    ``` yaml
    apiVersion: v1
    kind: ConfigMap
    metadata:
      name: cluster-image-set-git-repo
      namespace: multicluster-engine
    data:
      gitRepoUrl:
      gitRepoBranch: backplane-<mce-version>
      gitRepoPath: clusterImageSets
      channel:
      insecureSkipVerify:
      caCerts:
    ```

    - For `gitRepoUrl`, use the URL that you received when you forked the `acm-hive-openshift-releases` repository.

    - For `channel`, choose to use either of the supported values, `fast` or `stable`.

    - For `insecureSkipVerify`, set the `insecureSkipVerify` specification to `true` to build the insecure connection. The supported values are `true` or `false`.

    - For `caCerts`, list the certified authority (CA) certificates to build a secure HTTPS connection.

4.  Retrieve the available YAML files from the main repository by merging changes into your forked repository with the following procedure:

    1.  Commit and merge your changes to your forked repository.

    2.  Synchronize your list of fast release images after you clone the `acm-hive-openshift-releases` repository by updating the value of channel field in the `cluster-image-set-git-repo` `ConfigMap` to `fast`.

    3.  Synchronize and display the stable release images by updating the value of channel field in the `cluster-image-set-git-repo` `ConfigMap` to `stable`.

        After updating the `ConfigMap`, the list of available stable release images updates with the currently available images in about one minute.

5.  Run the following commands to list what is available and remove the defaults. Replace `<clusterImageSet_NAME>` with the name of the cluster image set that you want to remove:

    ``` bash
    oc get clusterImageSets
    oc delete clusterImageSet <clusterImageSet_NAME>
    ```

</div>

<div>

<div class="title">

Verification

</div>

- View the list of currently available release images in the console when you are creating a cluster.

</div>

<a id="release-images-disconnected"></a>

### Maintain a custom list of release images while disconnected

In some cases, you need to maintain a custom list of release images when the hub cluster has no Internet connection. You can create your own custom list of release images that are available when creating a cluster. Complete the following steps to manage your available release images while disconnected:

<div>

<div class="title">

Procedure

</div>

1.  When you are on a connected system, go to the [acm-hive-openshift-releases GitHub repository](https://github.com/stolostron/acm-hive-openshift-releases/tree/backplane-2.10) to access the available cluster image sets.

2.  Copy the `clusterImageSets` directory to a system that can access the disconnected multicluster engine operator cluster.

3.  Add the mapping between the managed cluster and the disconnected repository with your cluster image sets by completing the following steps that fits your managed cluster:

    - For an OpenShift Container Platform managed cluster, see [Configuring image registry repository mirroring](https://docs.redhat.com/en/documentation/openshift_container_platform/4.20/html-single/images/index#images-configuration-registry-mirror-configuring_image-configuration) for information about using your `ImageContentSourcePolicy` object to complete the mapping.

    - For a managed cluster that is not an OpenShift Container Platform cluster, use the `ManageClusterImageRegistry` custom resource definition to override the location of the image sets. See [Specifying registry images on managed clusters for import](clusters.md#specify-registry-img-on-managed-clusters-for-import) for information about how to override the cluster for the mapping.

4.  Add the YAML files for the images that you want to be available when you create a cluster by using the console or CLI to manually add the `clusterImageSet` YAML content.

5.  Modify the `clusterImageSet` YAML files for the remaining OpenShift Container Platform release images to reference the correct offline repository where you store the images. Your updates resemble the following example where `spec.releaseImage` uses your offline image registry of the release image, and the release image is referenced by digest:

    ``` yaml
    apiVersion: hive.openshift.io/v1
    kind: ClusterImageSet
    metadata:
      labels:
        channel: fast
      name: img<4.x.x>-x86-64-appsub
    spec:
      releaseImage: IMAGE_REGISTRY_IPADDRESS_or__DNSNAME/REPO_PATH/ocp-release@sha256:073a4e46289be25e2a05f5264c8f1d697410db66b960c9ceeddebd1c61e58717
    ```

6.  Ensure that the images are loaded in the offline image registry that is referenced in the YAML file.

7.  Obtain the image digest by running the following command:

    ``` bash
    oc adm release info <tagged_openshift_release_image> | grep "Pull From"
    ```

    Replace `<tagged_openshift_release_image>` with the tagged image for the supported OpenShift Container Platform version. See the following example output:

    ``` bash
    Pull From: quay.io/openshift-release-dev/ocp-release@sha256:69d1292f64a2b67227c5592c1a7d499c7d00376e498634ff8e1946bc9ccdddfe
    ```

    To learn more about the image tag and digest, see [Referencing images in imagestreams](https://docs.redhat.com/en/documentation/openshift_container_platform/4.20/html/images/managing-images#images-referencing-images-imagestreams_tagging-images).

8.  Create each of the `clusterImageSets` by entering the following command for each YAML file. Replace `clusterImageSet_FILE` with the name of the cluster image set file:

    ``` bash
    oc create -f <clusterImageSet_FILE>
    ```

9.  Alternately, you can paste the image URL directly in the create cluster console. Adding the image URL creates new `clusterImageSets` if they do not exist.

</div>

<div>

<div class="title">

Verification

</div>

- View the list of currently available release images in the console when you are creating a cluster.

</div>

<a id="sync-release-images"></a>

### Synchronize available release images

If you have a Red Hat Advanced Cluster Management hub cluster, which uses the `MultiClusterHub` operator to manage, upgrade, and install hub cluster components, you can synchronize the list of release images to ensure that you can select the latest available versions.

Release images are available in the [acm-hive-openshift-releases](https://github.com/stolostron/acm-hive-openshift-releases/tree/backplane-2.10) repository and are updated frequently.

There are three levels of stability of the release images. See the following table:

| Category | Description |
|----|----|
| candidate | The most current images, which are not tested and might have some bugs. |
| fast | Images that are partially tested, but likely less stable than a stable version. |
| stable | These fully-tested images are confirmed to install and build clusters correctly. |

Table of release images stability levels

<div>

<div class="title">

Additional resources

</div>

- [Refresh the release images list](clusters.md#refresh-release-images)

</div>

<a id="refresh-release-images"></a>

### Refresh the release images list

Refresh and synchronize the list of release images to ensure that the console reflects the latest stable or fast-channel release images needed to build or provision new clusters.

<div>

<div class="title">

Prerequisites

</div>

- You are running a Linux or Mac operating system.

</div>

<div>

<div class="title">

Procedure

</div>

1.  If the installer-managed `acm-hive-openshift-releases` subscription is enabled, disable the subscription by setting the value of `disableUpdateClusterImageSets` to `true` in the `MultiClusterHub` resource.

2.  Clone the [acm-hive-openshift-releases](https://github.com/stolostron/acm-hive-openshift-releases/tree/backplane-2.10) GitHub repository.

3.  Remove the subscription by running the following command:

    ``` bash
    oc delete -f subscribe/subscription-fast
    ```

4.  Synchronize and display the `candidate` release images. Run the following command:

    ``` bash
    make subscribe-candidate
    ```

    **Note:** After about one minute, the latest list of `candidate` release images is available.

5.  Synchronize and display the `fast` release images. Run the following command:

    ``` bash
    make subscribe-fast
    ```

    **Note:** After about one minute, the latest list of `fast` release images is available.

6.  Connect to the `stable` release images and synchronize your Red Hat Advanced Cluster Management hub cluster. Run the following command:

    ``` bash
    make subscribe-stable
    ```

    **Note:** After about one minute, the list of available `candidate`, `fast`, and `stable` release images updates with the currently available images.

7.  **Optional:** Unsubscribe from any of these channels to stop viewing the updates by running the following command:

    ``` bash
    oc delete -f subscribe/subscription-fast
    ```

</div>

<div>

<div class="title">

Verification

</div>

1.  View the list of currently available release images in the Red Hat Advanced Cluster Management console when you are creating a cluster.

</div>

<a id="create-intro"></a>

## Creating clusters

Learn how to create Red Hat OpenShift Container Platform clusters across cloud providers with multicluster engine operator.

multicluster engine operator uses the Hive operator that is provided with OpenShift Container Platform to provision clusters for all providers except the on-premises clusters and hosted control planes. When provisioning the on-premises clusters, multicluster engine operator uses the central infrastructure management and Assisted Installer function that are provided with OpenShift Container Platform. The hosted clusters for hosted control planes are provisioned by using the HyperShift operator.

- [Prepare to create a cluster with the CLI](clusters.md#prepare-to-create-a-cluster-with-the-cli)

- [Create a cluster with the CLI](clusters.md#create-a-cluster-with-the-cli)

- [Configuring additional manifests during cluster creation](clusters.md#config-manifest-create)

- [Create a cluster on Amazon Web Services](clusters.md#create-a-cluster-on-amazon-web-services)

- [Amazon Web Services console settings](clusters.md#aws-console-settings)

- [Create a cluster on Amazon Web Services GovCloud](clusters.md#create-a-cluster-on-amazon-web-services-govcloud)

- [Create a cluster on Amazon Web Services GovCloud by using the console](clusters.md#create-a-cluster-on-amazon-web-services-govcloud-console)

- [Amazon Web Services GovCloud console settings](clusters.md#aws-govcloud-console-settings)

- [Create a cluster on Microsoft Azure](clusters.md#create-a-cluster-on-microsoft-azure)

- [Microsoft Azure console settings](clusters.md#azure-console-settings)

- [Create a cluster on Google Cloud Platform by using the console](clusters.md#create-a-cluster-on-google-cloud-platform-console)

- [Create a cluster on VMware vSphere](clusters.md#create-a-cluster-on-vmware-vsphere)

- [VMware vSphere console settings](clusters.md#vsphere-console-settings)

- [Create a cluster on Red Hat OpenStack Platform](clusters.md#create-a-cluster-on-openstack)

- [Red Hat OpenStack Platform console settings](clusters.md#openstack-console-settings)

- [Create a cluster in an on-premises environment by using the CLI](clusters.md#create-a-cluster-on-premises-cli)

- [Create a cluster in an on-premises environment by using the console](clusters.md#create-a-cluster-on-premises-console)

- [On-premises console settings](clusters.md#on-prem-console-settings)

- [Create a cluster in a proxy environment](clusters.md#create-a-cluster-in-a-proxy-environment)

- [Configure *AgentClusterInstall* proxy](clusters.md#config-agent-proxy)

<a id="prepare-to-create-a-cluster-with-the-cli"></a>

### Prepare to create a cluster with the CLI

Before you create a cluster with the CLI, complete the following preparation steps.

<div>

<div class="title">

Procedure

</div>

1.  Make sure the ClusterImageSet resources are available on the hub cluster by running the following command:

    ``` bash
    oc get clusterimageset -A
    ```

    The output might resemble the following example:

    ``` bash
    img4.18.4-multi-appsub     quay.io/openshift-release-dev/ocp-release:4.18.4-multi
    img4.18.4-x86-64-appsub    quay.io/openshift-release-dev/ocp-release:4.18.4-x86_64
    ```

    **Note:** Each ClusterImageSet references an OpenShift Container Platform release image. The ClusterImageSet resources are populated by the `cluster-image-set-controller` in multicluster engine for Kubernetes operator.

2.  If you use the Nutanix platform, use the `x86_64` architecture for the `releaseImage` in the `ClusterImageSet` resource and set the `visible` label value to `'true'`. See the following example:

    ``` yaml
    apiVersion: hive.openshift.io/v1
    kind: ClusterImageSet
    metadata:
      labels:
        channel: stable
        visible: 'true'
      name: img4.x.47-x86-64-appsub
    spec:
      releaseImage: quay.io/openshift-release-dev/ocp-release:4.x.47-x86_64
    ```

3.  Review the hub cluster `KubeAPIServer` certificate verification strategy and update the strategy if needed. To learn what strategy to use for your setup, see [Configuring the hub cluster `KubeAPIServer` verification strategy](clusters.md#set-hub-kube-api-server).

</div>

<a id="create-a-cluster-with-the-cli"></a>

### Create a cluster with the CLI

The multicluster engine for Kubernetes operator uses internal Hive components to create Red Hat OpenShift Container Platform clusters. See the following information to learn how to create clusters.

<div>

<div class="title">

Prerequisites

</div>

- Before you create a cluster with the CLI, complete the steps in [Prepare to create a cluster with the CLI](clusters.md#prepare-to-create-a-cluster-with-the-cli).

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create a `ClusterDeployment` resource, which is a Hive resource that is used to control the lifecycle of a cluster. Go to the [Using Hive](https://github.com/openshift/hive/blob/master/docs/using-hive.md#using-hive) documentation to create the `ClusterDeployment` custom resource and create an individual cluster.

2.  Create a `` ClusterPool` `` resource, which is also a Hive resource that is used to create multiple clusters. Go to the [Cluster Pools](https://github.com/openshift/hive/blob/master/docs/clusterpools.md) documentation to create a cluster with the Hive `ClusterPool` API.

</div>

<a id="config-manifest-create"></a>

### Configuring additional manifests during cluster creation

You can configure additional Kubernetes resource manifests during the installation process of creating your cluster. This can help if you need to configure additional manifests for scenarios such as configuring networking or setting up a load balancer.

<a id="config-manifest-create-prereq"></a>

#### Prerequisites

Add a reference to the `ClusterDeployment` resource that specifies a config map resource that contains the additional resource manifests.

**Note:** The `ClusterDeployment` resource and the config map must be in the same namespace.

<a id="config-manifest-create-steps"></a>

#### Configuring additional manifests during cluster creation by using examples

If you want to configure additional manifests by using a config map with resource manifests, complete the following steps:

1.  Create a YAML file and add the following example content:

    ``` yaml
    kind: ConfigMap
    apiVersion: v1
    metadata:
      name: <my-baremetal-cluster-install-manifests>
      namespace: <mynamespace>
    data:
      99_metal3-config.yaml: |
        kind: ConfigMap
        apiVersion: v1
        metadata:
          name: metal3-config
          namespace: openshift-machine-api
        data:
          http_port: "6180"
          provisioning_interface: "enp1s0"
          provisioning_ip: "172.00.0.3/24"
          dhcp_range: "172.00.0.10,172.00.0.100"
          deploy_kernel_url: "http://172.00.0.3:6180/images/ironic-python-agent.kernel"
          deploy_ramdisk_url: "http://172.00.0.3:6180/images/ironic-python-agent.initramfs"
          ironic_endpoint: "http://172.00.0.3:6385/v1/"
          ironic_inspector_endpoint: "http://172.00.0.3:5150/v1/"
          cache_url: "http://192.168.111.1/images"
          rhcos_image_url: "https://releases-art-rhcos.svc.ci.openshift.org/art/storage/releases/rhcos-4.3/43.81.201911192044.0/x86_64/rhcos-43.81.201911192044.0-openstack.x86_64.qcow2.gz"
    ```

    **Note:** The example `ConfigMap` contains a manifest with another `ConfigMap` resource. The resource manifest `ConfigMap` can contain multiple keys with resource configurations added in the following pattern, `data.<resource_name>\.yaml`.

2.  Apply the file by running the following command:

    ``` bash
    oc apply -f <filename>.yaml
    ```

    If you want to configure additional manifests by using a `ClusterDeployment` by referencing a resource manifest `ConfigMap`, complete the following steps:

3.  Create a YAML file and add the following example content. The resource manifest `ConfigMap` is referenced in `spec.provisioning.manifestsConfigMapRef`:

    ``` yaml
    apiVersion: hive.openshift.io/v1
    kind: ClusterDeployment
    metadata:
      name: <my-baremetal-cluster>
      namespace: <mynamespace>
      annotations:
        hive.openshift.io/try-install-once: "true"
    spec:
      baseDomain: test.example.com
      clusterName: <my-baremetal-cluster>
      controlPlaneConfig:
        servingCertificates: {}
      platform:
        baremetal:
          libvirtSSHPrivateKeySecretRef:
            name: provisioning-host-ssh-private-key
      provisioning:
        installConfigSecretRef:
          name: <my-baremetal-cluster-install-config>
        sshPrivateKeySecretRef:
          name: <my-baremetal-hosts-ssh-private-key>
        manifestsConfigMapRef:
          name: <my-baremetal-cluster-install-manifests>
        imageSetRef:
          name: <my-clusterimageset>
        sshKnownHosts:
        - "10.1.8.90 ecdsa-sha2-nistp256 AAAAE2VjZHNhLXvVVVKUYVkuyvkuygkuyTCYTytfkufTYAAAAIbmlzdHAyNTYAAABBBKWjJRzeUVuZs4yxSy4eu45xiANFIIbwE3e1aPzGD58x/NX7Yf+S8eFKq4RrsfSaK2hVJyJjvVIhUsU9z2sBJP8="
      pullSecretRef:
        name: <my-baremetal-cluster-pull-secret>
    ```

4.  Apply the file by running the following command:

    ``` bash
    oc apply -f <filename>.yaml
    ```

<a id="create-a-cluster-on-amazon-web-services"></a>

### Create a cluster on Amazon Web Services

You can use the multicluster engine operator console to create a Red Hat OpenShift Container Platform cluster on Amazon Web Services (AWS).

When you create a cluster, the creation process uses the OpenShift Container Platform installer with the Hive resource. For more information about cluster creation after completing this procedure, see [Installing on AWS](https://docs.redhat.com/en/documentation/openshift_container_platform/4.20/html/installing_on_aws) in the OpenShift Container Platform documentation. If you have an existing cluster that you want to *import* instead, see [Cluster import](clusters.md#import-intro).

<div>

<div class="title">

Prerequisites

</div>

- You must have a deployed hub cluster.

- You need an AWS credential. See [Creating a credential for Amazon Web Services in the console](clusters.md#creating-credential-aws-ui) for more information.

- You need a configured domain in AWS. See [Installing on AWS](https://docs.redhat.com/en/documentation/openshift_container_platform/4.20/html/installing_on_aws/index) for instructions on how to configure a domain.

- You must have Amazon Web Services (AWS) login credentials, which include user name, password, access key ID, and secret access key. See [Understanding and Getting Your Security Credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/security-creds.html).

- You must have an OpenShift Container Platform image pull secret. See [Using image pull secrets](https://docs.redhat.com/en/documentation/openshift_container_platform/4.20/html/images/managing-images#using-image-pull-secrets).

  **Note:** If you change your cloud provider access key on the cloud provider, you also need to manually update the corresponding credential for the cloud provider on the console. This is required when your credentials expire on the cloud provider where the managed cluster is hosted and you try to delete the managed cluster.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Navigate to **Infrastructure** \> **Clusters**.

2.  On the *Clusters* page. Click **Cluster** \> **Create cluster** and complete the steps in the console. See [Amazon Web Services console settings](clusters.md#aws-console-settings) for more information about the settings.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Amazon Web Services console settings](clusters.md#aws-console-settings)

- [Create a cluster on Amazon Web Services GovCloud](clusters.md#create-a-cluster-on-amazon-web-services-govcloud) and [Create a cluster on Amazon Web Services GovCloud by using the console](clusters.md#create-a-cluster-on-amazon-web-services-govcloud-console)

- [Installing on AWS](https://docs.redhat.com/en/documentation/openshift_container_platform/4.20/html/installing_on_aws/index)

- [Release images](clusters.md#release-images-intro)

- [AWS General purpose instances](https://aws.amazon.com/ec2/instance-types/)

</div>

<a id="aws-console-settings"></a>

### Amazon Web Services console settings

The name of the cluster is used in the hostname of the cluster.

If you are using Red Hat Advanced Cluster Management for Kubernetes and want to configure your managed cluster klusterlet to run on specific nodes, see [Configure the klusterlet to run on specific nodes](clusters.md#config-klusterlet-nodes) for the required steps.

- When you review your information and optionally customize it before creating the cluster, you can select **YAML: On** to view the `install-config.yaml` file content in the panel. You can edit the YAML file with your custom settings, if you have any updates.

- When you create a cluster, the controller creates a namespace for the cluster and the resources. Ensure that you include only resources for that cluster instance in that namespace.

- *Destroying* the cluster deletes the namespace and all of the resources in it.

- If you want to add your cluster to an existing cluster set, you must have the correct permissions on the cluster set to add it. If you do not have `cluster-admin` privileges when you are creating the cluster, you must select a cluster set on which you have `clusterset-admin` permissions.

- If you do not have the correct permissions on the specified cluster set, the cluster creation fails. Contact your cluster administrator to provide you with `clusterset-admin` permissions to a cluster set if you do not have any cluster set options to select.

- Every managed cluster must be associated with a managed cluster set. If you do not assign the managed cluster to a `ManagedClusterSet`, it is automatically added to the `default` managed cluster set.

- If there is already a base DNS domain that is associated with the selected credential that you configured with your AWS account, that value is populated in the field. You can change the value by overwriting it. This name is used in the hostname of the cluster.

- The release image identifies the version of the OpenShift Container Platform image that is used to create the cluster. Select the image from the list of images that are available. If the image that you want to use is not available, you can enter the URL to the image that you want to use.

- The node pools include the control plane pool and the worker pools. The control plane nodes share the management of the cluster activity. The information includes the following fields:

  - Region: Specify the region where you want the node pool.

  - CPU architecture: If the architecture type of the managed cluster is not the same as the architecture of your hub cluster, enter a value for the instruction set architecture of the machines in the pool. Valid values are *amd64*, *ppc64le*, *s390x*, and *arm64*.

  - Zones: Specify where you want to run your control plane pools. You can select multiple zones within the region for a more distributed group of control plane nodes. A closer zone might provide faster performance, but a more distant zone might be more distributed.

  - Instance type: Specify the instance type for your control plane node. You can change the type and size of your instance after it is created.

  - Root storage: Specify the amount of root storage to allocate for the cluster.

- You can create zero or more worker nodes in a worker pool to run the container workloads for the cluster. This can be in a single worker pool, or distributed across multiple worker pools. If zero worker nodes are specified, the control plane nodes also function as worker nodes. The optional information includes the following fields:

  - Zones: Specify where you want to run your worker pools. You can select multiple zones within the region for a more distributed group of nodes. A closer zone might provide faster performance, but a more distant zone might be more distributed.

  - Instance type: Specify the instance type of your worker pools. You can change the type and size of your instance after it is created.

  - Node count: Specify the node count of your worker pool. This setting is required when you define a worker pool.

  - Root storage: Specify the amount of root storage allocated for your worker pool. This setting is required when you define a worker pool.

- Networking details are required for your cluster, and multiple networks are required for using IPv6. You can add an additional network by clicking **Add network**.

- Proxy information that is provided in the credential is automatically added to the proxy fields. You can use the information as it is, overwrite it, or add the information if you want to enable a proxy. The following list contains the required information for creating a proxy:

  - HTTP proxy: Specify the URL that should be used as a proxy for `HTTP` traffic.

  - HTTPS proxy: Specify the secure proxy URL that should be used for `HTTPS` traffic. If no value is provided, the same value as the `HTTP Proxy URL` is used for both `HTTP` and `HTTPS`.

  - No proxy sites: A comma-separated list of sites that should bypass the proxy. Begin a domain name with a period `.` to include all of the subdomains that are in that domain. Add an asterisk `*` to bypass the proxy for all destinations.

  - Additional trust bundle: One or more additional CA certificates that are required for proxying HTTPS connections.

**Note:** You do not have to run the `oc` command that is provided with the cluster details to import the cluster. When you create the cluster, it is automatically configured under the management of multicluster engine operator.

<a id="create-a-cluster-on-amazon-web-services-govcloud"></a>

### Create a cluster on Amazon Web Services GovCloud

You can use the console to create a Red Hat OpenShift Container Platform cluster on Amazon Web Services (AWS) or on AWS GovCloud. This procedure explains how to prepare your environment for a cluster on AWS GovCloud. See [Create a cluster on Amazon Web Services](clusters.md#create-a-cluster-on-amazon-web-services) for the instructions for creating a cluster on AWS. After you complete the Hive configuration, see [Create a cluster on Amazon Web Services GovCloud by using the console](clusters.md#create-a-cluster-on-amazon-web-services-govcloud-console).

AWS GovCloud provides cloud services that meet additional requirements that are necessary to store government documents on the cloud. When you create a cluster on AWS GovCloud, you must complete additional steps to prepare your environment.

When you create a cluster, the creation process uses the OpenShift Container Platform installer with the Hive resource. If you have questions about cluster creation after completing this procedure, see [Installing a cluster on AWS into a government region](https://docs.redhat.com/en/documentation/openshift_container_platform/4.20/html/installing_on_aws/installer-provisioned-infrastructure#installing-aws-government-region) in the OpenShift Container Platform documentation for more information about the process. The following sections provide the steps for preparing a cluster on AWS GovCloud:

<div>

<div class="title">

Prerequisites

</div>

- You must have AWS login credentials, which include user name, password, access key ID, and secret access key. See [Understanding and Getting Your Security Credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/security-creds.html).

- You need an AWS credential. See [Creating a credential for Amazon Web Services in the console](clusters.md#creating-credential-aws-ui) for more information.

- You need a configured domain in AWS. See [Installing on AWS](https://docs.redhat.com/en/documentation/openshift_container_platform/4.20/html/installing_on_aws/index) for instructions on how to configure a domain.

- You must have an OpenShift Container Platform image pull secret. See [Using image pull secrets](https://docs.redhat.com/en/documentation/openshift_container_platform/4.20/html/images/managing-images#using-image-pull-secrets).

- You must have an Amazon Virtual Private Cloud (VPC) with an existing Red Hat OpenShift Container Platform cluster for the hub cluster. This VPC must be different from the VPCs that are used for the managed cluster resources or the managed cluster service endpoints.

- You need a VPC where the managed cluster resources are deployed. This cannot be the same as the VPCs that are used for the hub cluster or the managed cluster service endpoints.

- You need one or more VPCs that provide the managed cluster service endpoints. This cannot be the same as the VPCs that are used for the hub cluster or the managed cluster resources.

- Ensure that the IP addresses of the VPCs that are specified by Classless Inter-Domain Routing (CIDR) do not overlap.

- You need a `HiveConfig` custom resource that references a credential within the Hive namespace. This custom resource must have access to create resources on the VPC that you created for the managed cluster service endpoints.

  **Note:** If you change your cloud provider access key on the cloud provider, you also need to manually update the corresponding credential for the cloud provider on the multicluster engine operator console. This is required when your credentials expire on the cloud provider where the managed cluster is hosted and you try to delete the managed cluster.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create the VPCs for resources and endpoints in addition to the VPC that contains the hub cluster. See [Create a VPC](https://docs.aws.amazon.com/vpc/latest/userguide/working-with-vpcs.html#Create-VPC) in the Amazon Web Services documentation for specific steps for creating a VPC.

2.  Create a VPC for the managed cluster with private subnets.

3.  Create one or more VPCs for the managed cluster service endpoints with private subnets. Each VPC in a region has a limit of 255 VPC endpoints, so you need multiple VPCs to support more than 255 clusters in that region.

4.  For each VPC, create subnets in all of the supported availability zones of the region. Each subnet must have at least 255 usable IP addresses because of the controller requirements.

    The following example shows how you might structure subnets for VPCs that have 6 availability zones in the `us-gov-east-1` region:

        vpc-1 (us-gov-east-1) : 10.0.0.0/20
          subnet-11 (us-gov-east-1a): 10.0.0.0/23
          subnet-12 (us-gov-east-1b): 10.0.2.0/23
          subnet-13 (us-gov-east-1c): 10.0.4.0/23
          subnet-12 (us-gov-east-1d): 10.0.8.0/23
          subnet-12 (us-gov-east-1e): 10.0.10.0/23
          subnet-12 (us-gov-east-1f): 10.0.12.0/2

    <!-- Separate adjacent source examples. -->

        vpc-2 (us-gov-east-1) : 10.0.16.0/20
          subnet-21 (us-gov-east-1a): 10.0.16.0/23
          subnet-22 (us-gov-east-1b): 10.0.18.0/23
          subnet-23 (us-gov-east-1c): 10.0.20.0/23
          subnet-24 (us-gov-east-1d): 10.0.22.0/23
          subnet-25 (us-gov-east-1e): 10.0.24.0/23
          subnet-26 (us-gov-east-1f): 10.0.28.0/23

5.  Ensure that all of the hub environments (hub cluster VPCs) have network connectivity to the VPCs that you created for VPC endpoints that use peering, transit gateways, and that all DNS settings are enabled.

6.  Collect a list of VPCs that are needed to resolve the DNS setup for the AWS PrivateLink, which is required for the AWS GovCloud connectivity. This includes at least the VPC of the multicluster engine operator instance that you are configuring, and can include the list of all of the VPCs where various Hive controllers exist.

    **Note:** Each VPC endpoint in AWS has a security group attached to control access to the endpoint. When Hive creates a VPC endpoint, it does not specify a security group. The default security group of the VPC is attached to the VPC endpoint. The default security group of the VPC must have rules to allow traffic where VPC endpoints are created from the Hive installer pods. See [Control access to VPC endpoints using endpoint policies](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-access.html) in the AWS documentation for details. For example, if Hive is running in `hive-vpc(10.1.0.0/16)`, there must be a rule in the default security group of the VPC where the VPC endpoint is created that allows ingress from `10.1.0.0/16`.

7.  Set permissions for AWS PrivateLink by using multiple credentials. The required permissions for these credentials depend on the type of credential. See the following list for the required permissions:

    - The credentials for ClusterDeployment require the following permissions:

          ec2:CreateVpcEndpointServiceConfiguration
          ec2:DescribeVpcEndpointServiceConfigurations
          ec2:ModifyVpcEndpointServiceConfiguration
          ec2:DescribeVpcEndpointServicePermissions
          ec2:ModifyVpcEndpointServicePermissions
          ec2:DeleteVpcEndpointServiceConfigurations

    - The credentials for HiveConfig for endpoint VPCs account `.spec.awsPrivateLink.credentialsSecretRef` require the following permissions:

          ec2:DescribeVpcEndpointServices
          ec2:DescribeVpcEndpoints
          ec2:CreateVpcEndpoint
          ec2:CreateTags
          ec2:DescribeNetworkInterfaces
          ec2:DescribeVPCs

          ec2:DeleteVpcEndpoints

          route53:CreateHostedZone
          route53:GetHostedZone
          route53:ListHostedZonesByVPC
          route53:AssociateVPCWithHostedZone
          route53:DisassociateVPCFromHostedZone
          route53:CreateVPCAssociationAuthorization
          route53:DeleteVPCAssociationAuthorization
          route53:ListResourceRecordSets
          route53:ChangeResourceRecordSets

          route53:DeleteHostedZone

    - The credentials specified in the `HiveConfig` custom resource for associating VPCs to the private hosted zone (`.spec.awsPrivateLink.associatedVPCs[$idx].credentialsSecretRef`). The account where the VPC is located requires the following permissions:

          route53:AssociateVPCWithHostedZone
          route53:DisassociateVPCFromHostedZone
          ec2:DescribeVPCs

8.  Ensure that there is a credential secret within the Hive namespace on the hub cluster.

    **Notes:**

    - The `HiveConfig` custom resource needs to reference a credential within the Hive namespace that has permissions to create resources in a specific provided VPC. If the credential that you are using to provision an AWS cluster in AWS GovCloud is already in the Hive namespace, then you do not need to create another one. If the credential that you are using to provision an AWS cluster in AWS GovCloud is not already in the Hive namespace, you can either replace your current credential or create an additional credential in the Hive namespace. The `HiveConfig` custom resource needs to include the following content:

      - An AWS GovCloud credential that has the required permissions to provision resources for the given VPC.

      - The addresses of the VPCs for the OpenShift Container Platform cluster installation, as well as the service endpoints for the managed cluster.

    - Use different VPCs for the OpenShift Container Platform cluster installation and the service endpoints.

      The following example shows the credential content:

      ``` yaml
      spec:
        awsPrivateLink:
          ## The list of inventory of VPCs that can be used to create VPC
          ## endpoints by the controller.
          endpointVPCInventory:
          - region: us-east-1
            vpcID: vpc-1
            subnets:
            - availabilityZone: us-east-1a
              subnetID: subnet-11
            - availabilityZone: us-east-1b
              subnetID: subnet-12
            - availabilityZone: us-east-1c
              subnetID: subnet-13
            - availabilityZone: us-east-1d
              subnetID: subnet-14
            - availabilityZone: us-east-1e
              subnetID: subnet-15
            - availabilityZone: us-east-1f
              subnetID: subnet-16
          - region: us-east-1
            vpcID: vpc-2
            subnets:
            - availabilityZone: us-east-1a
              subnetID: subnet-21
            - availabilityZone: us-east-1b
              subnetID: subnet-22
            - availabilityZone: us-east-1c
              subnetID: subnet-23
            - availabilityZone: us-east-1d
              subnetID: subnet-24
            - availabilityZone: us-east-1e
              subnetID: subnet-25
            - availabilityZone: us-east-1f
              subnetID: subnet-26
          ## The credentialsSecretRef references a secret with permissions to create.
          ## The resources in the account where the inventory of VPCs exist.
          credentialsSecretRef:
            name: <hub-account-credentials-secret-name>

          ## A list of VPC where various mce clusters exists.
          associatedVPCs:
          - region: region-mce1
            vpcID: vpc-mce1
            credentialsSecretRef:
              name: <credentials-that-have-access-to-account-where-MCE1-VPC-exists>
          - region: region-mce2
            vpcID: vpc-mce2
            credentialsSecretRef:
              name: <credentials-that-have-access-to-account-where-MCE2-VPC-exists>
      ```

      You can include a VPC from all the regions where AWS PrivateLink is supported in the `endpointVPCInventory` list. The controller selects a VPC that meets the requirements for the ClusterDeployment. For more information, refer to the [Hive documentation](https://github.com/openshift/hive/blob/master/docs/awsprivatelink.md#configuring-hive-to-enable-aws-private-link).

</div>

<a id="create-a-cluster-on-amazon-web-services-govcloud-console"></a>

### Create a cluster on Amazon Web Services GovCloud by using the console

You can use the console to create a Red Hat OpenShift Container Platform cluster on Amazon Web Services (AWS) GovCloud. See [Create a cluster on Amazon Web Services](clusters.md#create-a-cluster-on-amazon-web-services) for the instructions for creating a cluster on standard AWS.

Before you create a cluster on AWS GovCloud, you must prepare your environment and configure Hive for AWS PrivateLink. See [Create a cluster on Amazon Web Services GovCloud](clusters.md#create-a-cluster-on-amazon-web-services-govcloud).

When you create a cluster, the creation process uses the OpenShift Container Platform installer with the Hive resource. If you have questions about cluster creation after completing this procedure, see [Installing a cluster on AWS into a government region](https://docs.redhat.com/en/documentation/openshift_container_platform/4.20/html/installing_on_aws/installer-provisioned-infrastructure#installing-aws-government-region) in the OpenShift Container Platform documentation for more information about the process.

<div>

<div class="title">

Prerequisites

</div>

- You must have AWS login credentials, which include user name, password, access key ID, and secret access key. See [Understanding and Getting Your Security Credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/security-creds.html).

- You need an AWS credential. See [Creating a credential for Amazon Web Services in the console](clusters.md#creating-credential-aws-ui) for more information.

- You need a configured domain in AWS. See [Installing on AWS](https://docs.redhat.com/en/documentation/openshift_container_platform/4.20/html/installing_on_aws/index) for instructions on how to configure a domain.

- You must have an OpenShift Container Platform image pull secret. See [Using image pull secrets](https://docs.redhat.com/en/documentation/openshift_container_platform/4.20/html/images/managing-images#using-image-pull-secrets).

- You must have an Amazon Virtual Private Cloud (VPC) with an existing Red Hat OpenShift Container Platform cluster for the hub cluster. This VPC must be different from the VPCs that are used for the managed cluster resources or the managed cluster service endpoints.

- You need a VPC where the managed cluster resources are deployed. This cannot be the same as the VPCs that are used for the hub cluster or the managed cluster service endpoints.

- You need one or more VPCs that provide the managed cluster service endpoints. This cannot be the same as the VPCs that are used for the hub cluster or the managed cluster resources.

- Ensure that the IP addresses of the VPCs that are specified by Classless Inter-Domain Routing (CIDR) do not overlap.

- You need a `HiveConfig` custom resource that references a credential within the Hive namespace. This custom resource must have access to create resources on the VPC that you created for the managed cluster service endpoints.

  **Note:** If you change your cloud provider access key on the cloud provider, you also need to manually update the corresponding credential for the cloud provider on the multicluster engine operator console. This is required when your credentials expire on the cloud provider where the managed cluster is hosted and you try to delete the managed cluster.

</div>

<div>

<div class="title">

Procedure

</div>

- To create a cluster from the console, navigate to **Infrastructure** \> **Clusters** \> **Create cluster** **AWS** \> **Standalone** and complete the steps in the console.

  **Note:** This procedure is for creating a cluster. If you have an existing cluster that you want to import, see [Cluster import](clusters.md#import-intro) for those steps.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Amazon Web Services GovCloud console settings](clusters.md#aws-govcloud-console-settings)

</div>

<a id="aws-govcloud-console-settings"></a>

### Amazon Web Services GovCloud console settings

The credential that you select must have access to the resources in an AWS GovCloud region, if you create an AWS GovCloud cluster. You can use an AWS GovCloud secret that is already in the Hive namespace if it has the required permissions to deploy a cluster. Existing credentials are displayed in the console.

The name of the cluster is used in the hostname of the cluster.

**Important:** When you create a cluster, the controller creates a namespace for the cluster and its resources. Ensure that you include only resources for that cluster instance in that namespace. Destroying the cluster deletes the namespace and all of the resources in it.

If you want to add your cluster to an existing cluster set, you must have the correct permissions on the cluster set to add it. If you do not have `cluster-admin` privileges when you are creating the cluster, you must select a cluster set on which you have `clusterset-admin` permissions. If you do not have the correct permissions on the specified cluster set, the cluster creation fails. Contact your cluster administrator to provide you with `clusterset-admin` permissions to a cluster set if you do not have any cluster set options to select.

Every managed cluster must be associated with a managed cluster set. If you do not assign the managed cluster to a `ManagedClusterSet`, it is automatically added to the `default` managed cluster set.

If there is already a base DNS domain that is associated with the selected credential that you configured with your AWS or AWS GovCloud account, that value is populated in the field. You can change the value by overwriting it. This name is used in the hostname of the cluster. See [Installing on AWS](https://docs.redhat.com/en/documentation/openshift_container_platform/4.20/html/installing_on_aws/index) for more information.

The release image identifies the version of the OpenShift Container Platform image that is used to create the cluster. If the version that you want to use is available, you can select the image from the list of images. If the image that you want to use is not a standard image, you can enter the URL to the image that you want to use. See [Release images](clusters.md#release-images-intro) for more information about release images.

The node pools include the control plane pool and the worker pools. The control plane nodes share the management of the cluster activity. The information includes the following fields:

- Region: The region where you create your cluster resources. If you are creating a cluster on an AWS GovCloud provider, you must include an AWS GovCloud region for your node pools. For example, `us-gov-west-1`.

- CPU architecture: If the architecture type of the managed cluster is not the same as the architecture of your hub cluster, enter a value for the instruction set architecture of the machines in the pool. Valid values are *amd64*, *ppc64le*, *s390x*, and *arm64*.

- Zones: Specify where you want to run your control plane pools. You can select multiple zones within the region for a more distributed group of control plane nodes. A closer zone might provide faster performance, but a more distant zone might be more distributed.

- Instance type: Specify the instance type for your control plane node, which must be the same as the *CPU architecture* that you previously indicated. You can change the type and size of your instance after it is created.

- Root storage: Specify the amount of root storage to allocate for the cluster.

You can create zero or more worker nodes in a worker pool to run the container workloads for the cluster. They can be in a single worker pool, or distributed across multiple worker pools. If zero worker nodes are specified, the control plane nodes also function as worker nodes. The optional information includes the following fields:

- Pool name: Provide a unique name for your pool.

- Zones: Specify where you want to run your worker pools. You can select multiple zones within the region for a more distributed group of nodes. A closer zone might provide faster performance, but a more distant zone might be more distributed.

- Instance type: Specify the instance type of your worker pools. You can change the type and size of your instance after it is created.

- Node count: Specify the node count of your worker pool. This setting is required when you define a worker pool.

- Root storage: Specify the amount of root storage allocated for your worker pool. This setting is required when you define a worker pool.

Networking details are required for your cluster, and multiple networks are required for using IPv6. For an AWS GovCloud cluster, enter the values of the block of addresses of the Hive VPC in the *Machine CIDR* field. You can add an additional network by clicking **Add network**.

Proxy information that is provided in the credential is automatically added to the proxy fields. You can use the information as it is, overwrite it, or add the information if you want to enable a proxy. The following list contains the required information for creating a proxy:

- HTTP proxy URL: Specify the URL that should be used as a proxy for `HTTP` traffic.

- HTTPS proxy URL: Specify the secure proxy URL that should be used for `HTTPS` traffic. If no value is provided, the same value as the `HTTP Proxy URL` is used for both `HTTP` and `HTTPS`.

- No proxy domains: A comma-separated list of domains that should bypass the proxy. Begin a domain name with a period `.` to include all of the subdomains that are in that domain. Add an asterisk `*` to bypass the proxy for all destinations.

- Additional trust bundle: One or more additional CA certificates that are required for proxying HTTPS connections.

When creating an AWS GovCloud cluster or using a private environment, complete the fields on the *AWS private configuration* page with the AMI ID and the subnet values. Ensure that the value of `spec:platform:aws:privateLink:enabled` is set to `true` in the `ClusterDeployment.yaml` file, which is automatically set when you select **Use private configuration**.

When you review your information and optionally customize it before creating the cluster, you can select **YAML: On** to view the `install-config.yaml` file content in the panel. You can edit the YAML file with your custom settings, if you have any updates.

**Note:** You do not have to run the `oc` command that is provided with the cluster details to import the cluster. When you create the cluster, it is automatically configured under the management of multicluster engine for Kubernetes operator.

If you are using Red Hat Advanced Cluster Management for Kubernetes and want to configure your managed cluster klusterlet to run on specific nodes, see [Configure the klusterlet to run on specific nodes](clusters.md#config-klusterlet-nodes) for the required steps.

<a id="create-a-cluster-on-microsoft-azure"></a>

### Create a cluster on Microsoft Azure

You can use the multicluster engine operator console to deploy a Red Hat OpenShift Container Platform cluster on Microsoft Azure or on Microsoft Azure Government.

When you create a cluster, the creation process uses the OpenShift Container Platform installer with the Hive resource. If you have questions about cluster creation after completing this procedure, see [Installing on Azure](https://docs.redhat.com/en/documentation/openshift_container_platform/4.20/html/installing_on_azure) in the OpenShift Container Platform documentation for more information about the process.

<div>

<div class="title">

Prerequisites

</div>

- You must have a deployed hub cluster.

- You need an Azure credential. See [Creating a credential for Microsoft Azure in the console](clusters.md#creating-credential-azure-ui) for more information.

- You need a configured domain in Azure or Azure Government. See [Configuring a custom domain name for an Azure cloud service](https://docs.microsoft.com/en-us/azure/cloud-services/cloud-services-custom-domain-name-portal) for instructions on how to configure a domain.

- You need Azure login credentials, which include user name and password. See the [Microsoft Azure Portal](https://azure.microsoft.com/en-ca/features/azure-portal).

- You need Azure service principals, which include `clientId`, `clientSecret`, and `tenantId`. See [azure.microsoft.com](https://docs.microsoft.com/en-us/cli/azure/create-an-azure-service-principal-azure-cli?view=azure-cli-latest#password-based-authentication).

- You need an OpenShift Container Platform image pull secret. See [Using image pull secrets](https://docs.redhat.com/en/documentation/openshift_container_platform/4.20/html/images/managing-images#using-image-pull-secrets).

  **Note:** If you change your cloud provider access key on the cloud provider, you also need to manually update the corresponding credential for the cloud provider on the console of multicluster engine operator. This is required when your credentials expire on the cloud provider where the managed cluster is hosted and you try to delete the managed cluster.

</div>

<div>

<div class="title">

Procedure

</div>

- To create a cluster from the multicluster engine operator console, navigate to **Infrastructure** \> **Clusters**. On the *Clusters* page, click **Create cluster** and complete the steps in the console. See [Microsoft Azure console settings](clusters.md#azure-console-settings) for more information about the settings.

  **Note:** This procedure is for creating a cluster. If you have an existing cluster that you want to import, see [Cluster import](clusters.md#import-intro) for those steps.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Microsoft Azure console settings](clusters.md#azure-console-settings)

</div>

<a id="azure-console-settings"></a>

### Microsoft Azure console settings

The name of the cluster is used in the hostname of the cluster.

**Important:** When you create a cluster, the controller creates a namespace for the cluster and its resources. Ensure that you include only resources for that cluster instance in that namespace. Destroying the cluster deletes the namespace and all of the resources in it.

If you want to add your cluster to an existing cluster set, you must have the correct permissions on the cluster set to add it. If you do not have `cluster-admin` privileges when you are creating the cluster, you must select a cluster set on which you have `clusterset-admin` permissions. If you do not have the correct permissions on the specified cluster set, the cluster creation fails. Contact your cluster administrator to provide you with `clusterset-admin` permissions to a cluster set if you do not have any cluster set options to select.

Every managed cluster must be associated with a managed cluster set. If you do not assign the managed cluster to a `ManagedClusterSet`, it is automatically added to the `default` managed cluster set.

If there is already a base DNS domain that is associated with the selected credential that you configured for your Azure account, that value is populated in that field. You can change the value by overwriting it. See [Configuring a custom domain name for an Azure cloud service](https://docs.microsoft.com/en-us/azure/cloud-services/cloud-services-custom-domain-name-portal) for more information. This name is used in the hostname of the cluster.

The release image identifies the version of the OpenShift Container Platform image that is used to create the cluster. If the version that you want to use is available, you can select the image from the list of images. If the image that you want to use is not a standard image, you can enter the URL to the image that you want to use. See [Release images](clusters.md#release-images-intro) for more information about release images.

The Node pools include the control plane pool and the worker pools. The control plane nodes share the management of the cluster activity. The information includes the following optional fields:

- Region: Specify a region where you want to run your node pools. You can select multiple zones within the region for a more distributed group of control plane nodes. A closer zone might provide faster performance, but a more distant zone might be more distributed.

- CPU architecture: If the architecture type of the managed cluster is not the same as the architecture of your hub cluster, enter a value for the instruction set architecture of the machines in the pool. Valid values are *amd64*, *ppc64le*, *s390x*, and *arm64*.

You can change the type and size of the Instance type and Root storage allocation (required) of your control plane pool after your cluster is created.

You can create one or more worker nodes in a worker pool to run the container workloads for the cluster. They can be in a single worker pool, or distributed across multiple worker pools. If zero worker nodes are specified, the control plane nodes also function as worker nodes. The information includes the following fields:

- Zones: Specifies here you want to run your worker pools. You can select multiple zones within the region for a more distributed group of nodes. A closer zone might provide faster performance, but a more distant zone might be more distributed.

- Instance type: You can change the type and size of your instance after it is created.

You can add an additional network by clicking **Add network**. You must have more than one network if you are using IPv6 addresses.

Proxy information that is provided in the credential is automatically added to the proxy fields. You can use the information as it is, overwrite it, or add the information if you want to enable a proxy. The following list contains the required information for creating a proxy:

- HTTP proxy: The URL that should be used as a proxy for `HTTP` traffic.

- HTTPS proxy: The secure proxy URL that should be used for `HTTPS` traffic. If no value is provided, the same value as the `HTTP Proxy URL` is used for both `HTTP` and `HTTPS`.

- No proxy: A comma-separated list of domains that should bypass the proxy. Begin a domain name with a period `.` to include all of the subdomains that are in that domain. Add an asterisk `*` to bypass the proxy for all destinations.

- Additional trust bundle: One or more additional CA certificates that are required for proxying HTTPS connections.

When you review your information and optionally customize it before creating the cluster, you can click the **YAML** switch **On** to view the `install-config.yaml` file content in the panel. You can edit the YAML file with your custom settings, if you have any updates.

If you are using Red Hat Advanced Cluster Management for Kubernetes and want to configure your managed cluster klusterlet to run on specific nodes, see [Configure the klusterlet to run on specific nodes](clusters.md#config-klusterlet-nodes) for the required steps.

**Note:** You do not have to run the `oc` command that is provided with the cluster details to import the cluster. When you create the cluster, it is automatically configured under the management of multicluster engine operator.

<a id="create-a-cluster-on-google-cloud-platform-console"></a>

### Create a cluster on Google Cloud Platform by using the console

Follow the procedure to create a Red Hat OpenShift Container Platform cluster on Google Cloud Platform (GCP). For more information about GCP, see [Google Cloud Platform](https://cloud.google.com/docs/overview).

When you create a cluster, the creation process uses the OpenShift Container Platform installer with the Hive resource. If you have questions about cluster creation after completing this procedure, see [Installing on GCP](https://docs.redhat.com/en/documentation/openshift_container_platform/4.20/html/installing_on_gcp) in the OpenShift Container Platform documentation for more information about the process.

<div>

<div class="title">

Prerequisites

</div>

- You must have a deployed hub cluster.

- You must have a GCP credential. See [Creating a credential for Google Cloud Platform in the console](clusters.md#creating-gcp-credential-ui) for more information.

- You must have a configured domain in GCP. See [Setting up a custom domain](https://cloud.google.com/endpoints/docs/openapi/dev-portal-setup-custom-domain) for instructions on how to configure a domain.

- You need your GCP login credentials, which include user name and password.

- You must have an OpenShift Container Platform image pull secret. See [Using image pull secrets](https://docs.redhat.com/en/documentation/openshift_container_platform/4.20/html/images/managing-images#using-image-pull-secrets).

</div>

**Note:** If you change your cloud provider access key on the cloud provider, you also need to manually update the corresponding credential for the cloud provider on the console of multicluster engine operator. This is required when your credentials expire on the cloud provider where the managed cluster is hosted and you try to delete the managed cluster.

<div>

<div class="title">

Procedure

</div>

- To create clusters from the multicluster engine operator console, navigate to **Infrastructure** \> **Clusters**. On the *Clusters* page, click **Create cluster** and complete the steps in the console. See [Google Cloud Platform console settings](clusters.md#google-console-settings) for more information about the settings.

  **Note:** This procedure is for creating a cluster. If you have an existing cluster that you want to import, see [Cluster import](clusters.md#import-intro) for those steps.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Google Cloud Platform console settings](clusters.md#google-console-settings)

</div>

<a id="google-console-settings"></a>

### Google Cloud Platform console settings

The name of your cluster is used in the hostname of the cluster. There are some restrictions that apply to naming your GCP cluster. These restrictions include not beginning the name with `goog` or containing a group of letters and numbers that resemble `google` anywhere in the name. See [Bucket naming guidelines](https://cloud.google.com/storage/docs/naming-buckets#requirements) for the complete list of restrictions.

**Important:** When you create a cluster, the controller creates a namespace for the cluster and its resources. Ensure that you include only resources for that cluster instance in that namespace. Destroying the cluster deletes the namespace and all of the resources in it.

If you want to add your cluster to an existing cluster set, you must have the correct permissions on the cluster set to add it. If you do not have `cluster-admin` privileges when you are creating the cluster, you must select a cluster set on which you have `clusterset-admin` permissions. If you do not have the correct permissions on the specified cluster set, the cluster creation fails. Contact your cluster administrator to provide you with `clusterset-admin` permissions to a cluster set if you do not have any cluster set options to select.

Every managed cluster must be associated with a managed cluster set. If you do not assign the managed cluster to a `ManagedClusterSet`, it is automatically added to the `default` managed cluster set.

If there is already a base DNS domain that is associated with the selected credential for your GCP account, that value is populated in the field. You can change the value by overwriting it. See [Setting up a custom domain](https://cloud.google.com/endpoints/docs/openapi/dev-portal-setup-custom-domain) for more information. This name is used in the hostname of the cluster.

The release image identifies the version of the OpenShift Container Platform image that is used to create the cluster. If the version that you want to use is available, you can select the image from the list of images. If the image that you want to use is not a standard image, you can enter the URL to the image that you want to use. See [Release images](clusters.md#release-images-intro) for more information about release images.

The Node pools include the control plane pool and the worker pools. The control plane nodes share the management of the cluster activity. The information includes the following fields:

- Region: Specify a region where you want to run your control plane pools. A closer region might provide faster performance, but a more distant region might be more distributed.

- CPU architecture: If the architecture type of the managed cluster is not the same as the architecture of your hub cluster, enter a value for the instruction set architecture of the machines in the pool. Valid values are *amd64*, *ppc64le*, *s390x*, and *arm64*.

You can specify the instance type of your control plane pool. You can change the type and size of your instance after it is created.

You can create one or more worker nodes in a worker pool to run the container workloads for the cluster. They can be in a single worker pool, or distributed across multiple worker pools. If zero worker nodes are specified, the control plane nodes also function as worker nodes. The information includes the following fields:

- Instance type: You can change the type and size of your instance after it is created.

- Node count: This setting is required when you define a worker pool.

The networking details are required, and multiple networks are required for using IPv6 addresses. You can add an additional network by clicking **Add network**.

Proxy information that is provided in the credential is automatically added to the proxy fields. You can use the information as it is, overwrite it, or add the information if you want to enable a proxy. The following list contains the required information for creating a proxy:

- HTTP proxy: The URL that should be used as a proxy for `HTTP` traffic.

- HTTPS proxy: The secure proxy URL that should be used for `HTTPS` traffic. If no value is provided, the same value as the `HTTP Proxy URL` is used for both `HTTP` and `HTTPS`.

- No proxy sites: A comma-separated list of sites that should bypass the proxy. Begin a domain name with a period `.` to include all of the subdomains that are in that domain. Add an asterisk `*` to bypass the proxy for all destinations.

- Additional trust bundle: One or more additional CA certificates that are required for proxying HTTPS connections.

When you review your information and optionally customize it before creating the cluster, you can select **YAML: On** to view the `install-config.yaml` file content in the panel. You can edit the YAML file with your custom settings, if you have any updates.

If you are using Red Hat Advanced Cluster Management for Kubernetes and want to configure your managed cluster klusterlet to run on specific nodes, see [Configure the klusterlet to run on specific nodes](clusters.md#config-klusterlet-nodes) for the required steps.

**Note:** You do not have to run the `oc` command that is provided with the cluster details to import the cluster. When you create the cluster, it is automatically configured under the management of multicluster engine operator.

<a id="create-a-cluster-on-vmware-vsphere"></a>

### Create a cluster on VMware vSphere

You can use the multicluster engine operator console to deploy a Red Hat OpenShift Container Platform cluster on VMware vSphere.

When you create a cluster, the creation process uses the OpenShift Container Platform installer with the Hive resource. To learn more about cluster creation after completing this procedure, see [Installing on VMware vSphere](https://docs.redhat.com/en/documentation/openshift_container_platform/4.20/html/installing_on_vmware_vsphere/preparing-to-install-on-vsphere) in the OpenShift Container Platform documentation.

<div>

<div class="title">

Prerequisites

</div>

- You must have a hub cluster that is deployed on a supported OpenShift Container Platform version.

- You need a vSphere credential. See [Creating a credential for VMware vSphere in the console](clusters.md#creating-a-credential-for-vmware-vsphere-ui) for more information.

- You need an OpenShift Container Platform image pull secret. See [Using image pull secrets](https://docs.redhat.com/en/documentation/openshift_container_platform/4.20/html/images/managing-images#using-image-pull-secrets).

- You must have the following information for the VMware instance where you are deploying:

  - Required static IP addresses for API and Ingress instances

  - DNS records for:

    - The following API base domain must point to the static API VIP:

      ``` bash
      api.<cluster_name>.<base_domain>
      ```

- The following application base domain must point to the static IP address for Ingress VIP: `*.apps.<cluster_name>.<base_domain>`

</div>

<div>

<div class="title">

Procedure

</div>

- To create a cluster from the multicluster engine operator console, navigate to **Infrastructure** \> **Clusters**. On the *Clusters* page, click **Create cluster** and complete the steps in the console. See [VMware vSphere console settings](clusters.md#vsphere-console-settings) for more information about the settings.

  **Note:** This procedure is for creating a cluster. If you have an existing cluster that you want to import, see [Cluster import](clusters.md#import-intro) for those steps.

</div>

<div>

<div class="title">

Additional resources

</div>

- [VMware vSphere console settings](clusters.md#vsphere-console-settings)

</div>

<a id="vsphere-console-settings"></a>

### VMware vSphere console settings

When you create a cluster on VMware vSphere by using the console, complete the following fields and review the following information.

The name of your cluster is used in the hostname of the cluster.

**Important:** When you create a cluster, the controller creates a namespace for the cluster and its resources. Ensure that you include only resources for that cluster instance in that namespace. Destroying the cluster deletes the namespace and all of the resources in it.

**Tip:** Select **YAML: On** to view content updates as you enter the information in the console.

If you want to add your cluster to an existing cluster set, you must have the correct permissions on the cluster set to add it. If you do not have `cluster-admin` privileges when you are creating the cluster, you must select a cluster set on which you have `clusterset-admin` permissions. If you do not have the correct permissions on the specified cluster set, the cluster creation fails. Contact your cluster administrator to provide you with `clusterset-admin` permissions to a cluster set if you do not have any cluster set options to select.

Every managed cluster must be associated with a managed cluster set. If you do not assign the managed cluster to a `ManagedClusterSet`, it is automatically added to the `default` managed cluster set.

If there is already a base domain associated with the selected credential that you configured for your vSphere account, that value is populated in the field. You can change the value by overwriting it. See [Installing a cluster on vSphere with customizations](https://docs.redhat.com/en/documentation/openshift_container_platform/4.20/html/installing_on_vmware_vsphere/installer-provisioned-infrastructure#installing-vsphere-installer-provisioned-customizations) for more information. This value must match the name that you used to create the DNS records listed in the prerequisites section. This name is used in the hostname of the cluster.

The release image identifies the version of the OpenShift Container Platform image that is used to create the cluster. If the version that you want to use is available, you can select the image from the list of images. If the image that you want to use is not a standard image, you can enter the URL to the image that you want to use. See [Release images](clusters.md#release-images-intro) for more information about release images.

**Note:** Choose release images for supported OpenShift Container Platform versions.

The node pools include the control plane pool and the worker pools. The control plane nodes share the management of the cluster activity. The information includes the *CPU architecture* field. View the following field description:

- CPU architecture: If the architecture type of the managed cluster is not the same as the architecture of your hub cluster, enter a value for the instruction set architecture of the machines in the pool. Valid values are *amd64*, *ppc64le*, *s390x*, and *arm64*.

You can create one or more worker nodes in a worker pool to run the container workloads for the cluster. They can be in a single worker pool, or distributed across multiple worker pools. If zero worker nodes are specified, the control plane nodes also function as worker nodes. The information includes *Cores per socket*, *CPUs*, *Memory_min MiB, \_Disk size* in GiB, and *Node count*.

Networking information is required. Multiple networks are required for using IPv6. Some of the required networking information is included the following fields:

- vSphere network name: Specify the VMware vSphere network name.

- API VIP: Specify the IP address to use for internal API communication.

  **Note:** This value must match the name that you used to create the DNS records listed in the prerequisites section. If not provided, the DNS must be pre-configured so that `api.` resolves correctly.

- Ingress VIP: Specify the IP address to use for ingress traffic.

  **Note:** This value must match the name that you used to create the DNS records listed in the prerequisites section. If not provided, the DNS must be pre-configured so that `test.apps.` resolves correctly.

You can add an additional network by clicking **Add network**. You must have more than one network if you are using IPv6 addresses.

Proxy information that is provided in the credential is automatically added to the proxy fields. You can use the information as it is, overwrite it, or add the information if you want to enable a proxy. The following list contains the required information for creating a proxy:

- HTTP proxy: Specify the URL that should be used as a proxy for `HTTP` traffic.

- HTTPS proxy: Specify the secure proxy URL that should be used for `HTTPS` traffic. If no value is provided, the same value as the `HTTP Proxy URL` is used for both `HTTP` and `HTTPS`.

- No proxy sites: Provide a comma-separated list of sites that should bypass the proxy. Begin a domain name with a period `.` to include all of the subdomains that are in that domain. Add an asterisk `*` to bypass the proxy for all destinations.

- Additional trust bundle: One or more additional CA certificates that are required for proxying HTTPS connections.

Click **Disconnected installation** to define the disconnected installation. When creating a cluster by using VMware vSphere provider and disconnected installation, if a certificate is required to access the mirror registry, you must enter it in the *Additional trust bundle* field in the *Configuration for disconnected installation* section when configuring your credential, or the *Disconnected installation* section when creating a cluster.

You can click **Add automation template** to create a template.

When you review your information and optionally customize it before creating the cluster, you can click the **YAML** switch **On** to view the `install-config.yaml` file content in the panel. You can edit the YAML file with your custom settings, if you have any updates.

If you are using Red Hat Advanced Cluster Management for Kubernetes and want to configure your managed cluster klusterlet to run on specific nodes, see [Configure the klusterlet to run on specific nodes](clusters.md#config-klusterlet-nodes) for the required steps.

**Note:** You do not have to run the `oc` command that is provided with the cluster details to import the cluster. When you create the cluster, it is automatically configured under the management of multicluster engine operator.

Continue with [Accessing your cluster](clusters.md#accessing-your-cluster) for instructions for accessing your cluster.

<a id="create-a-cluster-on-openstack"></a>

### Create a cluster on Red Hat OpenStack Platform

You can use the multicluster engine operator console to deploy a Red Hat OpenShift Container Platform cluster on Red Hat OpenStack Platform.

When you create a cluster, the creation process uses the OpenShift Container Platform installer with the Hive resource. If you have questions about cluster creation after completing this procedure, see [Installing on OpenStack](https://docs.redhat.com/en/documentation/openshift_container_platform/4.20/html/installing_on_openstack) in the OpenShift Container Platform documentation for more information about the process.

<div>

<div class="title">

Prerequisites

</div>

- You must have a hub cluster that is deployed on OpenShift Container Platform version 4.6 or later.

- You must have a Red Hat OpenStack Platform credential. See [Creating a credential for Red Hat OpenStack Platform in the console](clusters.md#creating-a-credential-for-openstack-ui) for more information.

- You need an OpenShift Container Platform image pull secret. See [Using image pull secrets](https://docs.redhat.com/en/documentation/openshift_container_platform/4.20/html/images/managing-images#using-image-pull-secrets).

- You need a flavor name for the control plane and worker instances; for example, `m1.xlarge`, for the Red Hat OpenStack Platform instance where you are deploying

- You also need a network name for the external network to provide the floating IP addresses.

- You must have a floating IP addresses for API and ingress instances.

- You need DNS records for the following domains:

  - The following API base domain must point to the floating IP address for the API: `api.<cluster_name>.<base_domain>`

  - The following application base domain must point to the floating IP address for ingress:app-name: `*.apps.<cluster_name>.<base_domain>`

</div>

<div>

<div class="title">

Procedure

</div>

1.  To create a cluster from the multicluster engine operator console, navigate to **Infrastructure** \> **Clusters**. On the *Clusters* page, click **Create cluster** and complete the steps in the console.

2.  When creating a cluster that uses an internal certificate authority (CA), you need to customize the YAML file. Insert a `Secret` object at the top of the list with the CA certificate bundle. If the Red Hat OpenStack Platform environment provides services using certificates signed by multiple authorities, the bundle must include the certificates to validate all of the required endpoints. The addition for a cluster named `ocp3` resembles the following example:

    ``` yaml
    apiVersion: v1
    kind: Secret
    type: Opaque
    metadata:
      name: ocp3-openstack-trust
      namespace: ocp3
    stringData:
      ca.crt: |
        -----BEGIN CERTIFICATE-----
        <Base64 certificate contents here>
        -----END CERTIFICATE-----
        -----BEGIN CERTIFICATE-----
        <Base64 certificate contents here>
        -----END CERTIFICATE----
    ```

3.  Modify the Hive `ClusterDeployment` object to specify the value of `certificatesSecretRef` in `spec.platform.openstack`, similar to the following example:

    ``` yaml
    platform:
      openstack:
        certificatesSecretRef:
          name: ocp3-openstack-trust
        credentialsSecretRef:
          name: ocp3-openstack-creds
        cloud: openstack
    ```

    **Note:** The example assumes that the cloud name in the `clouds.yaml` file is `openstack`.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Red Hat OpenStack Platform console settings](clusters.md#openstack-console-settings)

</div>

<a id="openstack-console-settings"></a>

### Red Hat OpenStack Platform console settings

The name of the cluster is used in the hostname of the cluster. The name must contain fewer than 15 characters. This value must match the name that you used to create the DNS records listed in the credential prerequisites section.

**Important:** When you create a cluster, the controller creates a namespace for the cluster and its resources. Ensure that you include only resources for that cluster instance in that namespace. Destroying the cluster deletes the namespace and all of the resources in it.

**Tip:** Select **YAML: On** to view content updates as you enter the information in the console.

If you want to add your cluster to an existing cluster set, you must have the correct permissions on the cluster set to add it. If you do not have `cluster-admin` privileges when you are creating the cluster, you must select a cluster set on which you have `clusterset-admin` permissions. If you do not have the correct permissions on the specified cluster set, the cluster creation fails. Contact your cluster administrator to provide you with `clusterset-admin` permissions to a cluster set if you do not have any cluster set options to select.

Every managed cluster must be associated with a managed cluster set. If you do not assign the managed cluster to a `ManagedClusterSet`, it is automatically added to the `default` managed cluster set.

If there is already a base DNS domain that is associated with the selected credential that you configured for your Red Hat OpenStack Platform account, that value is populated in the field. You can change the value by overwriting it. See [Managing domains](https://docs.redhat.com/en/documentation/red_hat_openstack_platform/16.1/html/users_and_identity_management_guide/domains) in the Red Hat OpenStack Platform documentation for more information. This name is used in the hostname of the cluster.

The release image identifies the version of the OpenShift Container Platform image that is used to create the cluster. If the version that you want to use is available, you can select the image from the list of images. If the image that you want to use is not a standard image, you can enter the URL to the image that you want to use. See [Release images](clusters.md#release-images-intro) for more information about release images. Only release images for OpenShift Container Platform versions 4.6.x and higher are supported.

The node pools include the control plane pool and the worker pools. The control plane nodes share the management of the cluster activity. If the architecture type of the managed cluster is not the same as the architecture of your hub cluster, enter a value for the instruction set architecture of the machines in the pool. Valid values are *amd64*, *ppc64le*, *s390x*, and *arm64*.

You must add an instance type for your control plane pool, but you can change the type and size of your instance after it is created.

You can create one or more worker nodes in a worker pool to run the container workloads for the cluster. They can be in a single worker pool, or distributed across multiple worker pools. If zero worker nodes are specified, the control plane nodes also function as worker nodes. The information includes the following fields:

- Instance type: You can change the type and size of your instance after it is created.

- Node count: Specify the node count for your worker pool. This setting is required when you define a worker pool.

Networking details are required for your cluster. You must provide the values for one or more networks for an IPv4 network. For an IPv6 network, you must define more than one network.

You can add an additional network by clicking **Add network**. You must have more than one network if you are using IPv6 addresses.

Proxy information that is provided in the credential is automatically added to the proxy fields. You can use the information as it is, overwrite it, or add the information if you want to enable a proxy. The following list contains the required information for creating a proxy:

- HTTP proxy: Specify the URL that should be used as a proxy for `HTTP` traffic.

- HTTPS proxy: The secure proxy URL that should be used for `HTTPS` traffic. If no value is provided, the same value as the `HTTP Proxy` is used for both `HTTP` and `HTTPS`.

- No proxy: Define a comma-separated list of sites that should bypass the proxy. Begin a domain name with a period `.` to include all of the subdomains that are in that domain. Add an asterisk `*` to bypass the proxy for all destinations.

- Additional trust bundle: One or more additional CA certificates that are required for proxying HTTPS connections.

You can define the disconnected installation image by clicking **Disconnected installation**. When creating a cluster by using Red Hat OpenStack Platform provider and disconnected installation, if a certificate is required to access the mirror registry, you must enter it in the *Additional trust bundle* field in the *Configuration for disconnected installation* section when configuring your credential or the *Disconnected installation* section when creating a cluster.

When you review your information and optionally customize it before creating the cluster, you can click the **YAML** switch **On** to view the `install-config.yaml` file content in the panel. You can edit the YAML file with your custom settings, if you have any updates.

If you are using Red Hat Advanced Cluster Management for Kubernetes and want to configure your managed cluster klusterlet to run on specific nodes, see [Configure the klusterlet to run on specific nodes](clusters.md#config-klusterlet-nodes) for the required steps.

**Note:** You do not have to run the `oc` command that is provided with the cluster details to import the cluster. When you create the cluster, it is automatically configured under the management of multicluster engine operator.

Continue with [Accessing your cluster](clusters.md#accessing-your-cluster) for instructions for accessing your cluster.

<a id="create-a-cluster-on-premises-cli"></a>

### Create a cluster in an on-premises environment by using the CLI

You can create on-premises Red Hat OpenShift Container Platform clusters by using the CLI. You can create single-node OpenShift clusters, multi-node clusters, and compact three-node clusters. You can create these clusters on VMware vSphere, Red Hat OpenStack, Nutanix, External, or in a bare metal environment.

Since the platform value is set to `platform=none`, there is no platform integration with the platform where you install the cluster. A single-node OpenShift cluster has only a single node, which hosts the control plane services and the user workloads. Use this configuration when you want to minimize the resource footprint of the cluster.

You can also provision multiple single-node OpenShift clusters on edge resources by using the zero touch provisioning feature, which is a feature that is available with Red Hat OpenShift Container Platform. For more information about zero touch provisioning, see *Clusters at the network far edge* in the additional resources section.

You can also create a cluster on premises without the console by using the Assisted Installer feature within the central infrastructure management component. After you complete this procedure, you can boot the host from the discovery image that is generated. The order of the procedures is generally not important.

When creating an on-premises cluster, you need a namespace for your resources. Keep all of the resources in a shared namespace.

<div>

<div class="title">

Prerequisites

</div>

- You must have a deployed hub cluster on a supported OpenShift Container Platform version.

- You need a configured infrastructure environment with a host inventory of configured hosts.

- You must have internet access for your hub cluster (connected), or a connection to an internal or mirror registry that has a connection to the internet (disconnected) to retrieve the required images for creating the cluster.

- You need a configured on-premises credential.

- You need an OpenShift Container Platform image pull secret. See [Using image pull secrets](https://docs.redhat.com/en/documentation/openshift_container_platform/4.20/html/images/managing-images#using-image-pull-secrets).

- You need the following DNS records:

  - The following API base domain must point to the static API VIP:

    `api.<cluster_name>.<base_domain>`

  - The following application base domain must point to the static IP address for Ingress VIP:

    `*.apps.<cluster_name>.<base_domain>`

- Review the hub cluster `KubeAPIServer` certificate verification strategy and update the strategy if needed. To learn what strategy to use for your setup, see [Configuring the hub cluster `KubeAPIServer` verification strategy](clusters.md#set-hub-kube-api-server).

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create and name your namespace. You can use any name except `assisted-installer`. Apply the following file which uses `sample-namespace` as an example for the namespace:

    ``` yaml
    apiVersion: v1
    kind: Namespace
    metadata:
      name: sample-namespace
    ```

2.  Add a pull secret to the namespace. Add your [pull secret](https://console.redhat.com/openshift/install/pull-secret) to your namespace by creating and applying the following custom resource:

    ``` yaml
    apiVersion: v1
    kind: Secret
    type: kubernetes.io/dockerconfigjson
    metadata:
      name: <pull-secret>
      namespace: sample-namespace
    stringData:
      .dockerconfigjson: 'your-pull-secret-json'
    ```

3.  Add the content of your pull secret in `stringData`. For example, this can include a `cloud.openshift.com`, `quay.io`, or `registry.redhat.io` authentication.

4.  Generate a `CustomImageSet` to specify the version of OpenShift Container Platform for your cluster by creating and applying the following custom resource. Replace `<4.x.0>` with the supported version that you are using for `ClusterImageSet` for both the `name` and the `releaseImage`:

    ``` yaml
    apiVersion: hive.openshift.io/v1
    kind: ClusterImageSet
    metadata:
      name: openshift-v<4.x.0>
    spec:
      releaseImage: quay.io/openshift-release-dev/ocp-release:<4.x.0>-rc.0-x86_64
    ```

    **Note:** You need to create a multi-architecture `ClusterImageSet` if you install a managed cluster that has a different architecture than the hub cluster. To learn more, see [Create a release image to deploy a cluster on a different architecture](clusters.md#manual-release-image-cross-arch).

5.  Create the `ClusterDeployment` custom resource. The `ClusterDeployment` custom resource definition is an API that controls the lifecycle of the cluster and references the `AgentClusterInstall` custom resource in the `spec.ClusterInstallRef` setting, which defines the cluster parameters. Apply the following custom resource:

    ``` yaml
    apiVersion: hive.openshift.io/v1
    kind: ClusterDeployment
    metadata:
      name: single-node
      namespace: demo-worker4
    spec:
      baseDomain: hive.example.com
      clusterInstallRef:
        group: extensions.hive.openshift.io
        kind: AgentClusterInstall
        name: <test-agent-cluster-install>
        version: v1beta1
      clusterName: test-cluster
      controlPlaneConfig:
        servingCertificates: {}
      platform:
        agentBareMetal:
          agentSelector:
            matchLabels:
              location: internal
      pullSecretRef:
        name: <pull-secret>
    ```

    - Add the name of your `AgentClusterInstall` resource to the `clusterInstallRef` name.

    - Add the pull secret that you previously created in the `pullSecretRef` field.

6.  Create the AgentClusterInstall custom resource. In the `AgentClusterInstall` custom resource, you can specify many of the requirements for the clusters. For example, you can specify the cluster network settings, platform, number of control planes, and worker nodes. Create and add the a custom resource that resembles the following example:

    ``` yaml
    apiVersion: extensions.hive.openshift.io/v1beta1
    kind: AgentClusterInstall
    metadata:
      name: test-agent-cluster-install
      namespace: demo-worker4
    spec:
      platformType: BareMetal
      clusterDeploymentRef:
        name: <single-node>
      imageSetRef:
        name: <openshift-<v4.x.0>>
      networking:
        clusterNetwork:
        - cidr: 10.128.0.0/14
          hostPrefix: 23
        machineNetwork:
        - cidr: 192.168.111.0/24
        serviceNetwork:
        - 172.30.0.0/16
      provisionRequirements:
        controlPlaneAgents: 1
      sshPublicKey: |
        ssh-rsa <public-key-1>
        ssh-rsa <public-key-2>
        ssh-rsa <public-key-3>
    ```

    - Replace `<4.x.0>` with the version of OpenShift Container Platform that you are using.

    - Specify the platform type of the environment where the cluster is created in `spec.platformType`. Possible values are: `BareMetal`, `None`, `VSphere`, `Nutanix`, or `External`.

    - For the `imgageSetRef` name, use the same name that you used for your `ClusterDeployment` resource.

    - Use the `ClusterImageSet` that you previously created.

    - Possible `ontrolPlaneAgents` values are `1` and `3`. If you are using OpenShift Container Platform version 4.18 or newer, the `platformType` field is set to `BareMetal` or `None`, and your CPU architecture is `x86_64`, you can also use `4` and `5`. Control plane nodes manage workloads, maintain cluster state, and ensure stability. You can increase fault tolerance and availability, and reduce downtime during failures, if you use more than three nodes.

    - You can specify one or multiple SSH public keys in the `sshPublicKey` field, which allow you to access the host after installing.

7.  If you set `platformType:` to `External`, you must add the `external` spec. See the following example:

    ``` yaml
    apiVersion: extensions.hive.openshift.io/v1beta1
    kind: AgentClusterInstall
    metadata:
      name: test-agent-cluster-install
      namespace: demo-worker4
    spec:
      platformType: External
      external:
        platformName: "myplatform"
        cloudControllerManager: External
    ```

    - Add your platform name to `platformName`.

    - If you set the `platformType` field to empty, `{}`, the Cloud Controller Manager is disabled during installation. If you set the field to `External`, you must add custom manifests to enable the Cloud Controller Manager.

8.  **Optional:** Create the `NMStateConfig` custom resource. The `NMStateConfig` custom resource is only required if you have a host-level network configuration, such as static IP addresses. If you create the `NMStateConfig` custom resource, you must complete this step before you create an `InfraEnv` custom resource. The values for `spec.nmStateConfigLabelSelector` in the `InfraEnv` custom resource refer to the `NMStateConfig` custom resource. The resource resembles the following example:

    ``` yaml
    apiVersion: agent-install.openshift.io/v1beta1
    kind: NMStateConfig
    metadata:
      name: <mynmstateconfig>
      namespace: <demo-worker4>
      labels:
        demo-nmstate-label: <value>
    spec:
      config:
        interfaces:
          - name: eth0
            type: ethernet
            state: up
            mac-address: 02:00:00:80:12:14
            ipv4:
              enabled: true
              address:
                - ip: 192.168.111.30
                  prefix-length: 24
              dhcp: false
          - name: eth1
            type: ethernet
            state: up
            mac-address: 02:00:00:80:12:15
            ipv4:
              enabled: true
              address:
                - ip: 192.168.140.30
                  prefix-length: 24
              dhcp: false
        dns-resolver:
          config:
            server:
              - 192.168.126.1
        routes:
          config:
            - destination: 0.0.0.0/0
              next-hop-address: 192.168.111.1
              next-hop-interface: eth1
              table-id: 254
            - destination: 0.0.0.0/0
              next-hop-address: 192.168.140.1
              next-hop-interface: eth1
              table-id: 254
      interfaces:
        - name: "eth0"
          macAddress: "02:00:00:80:12:14"
        - name: "eth1"
          macAddress: "02:00:00:80:12:15"
    ```

    - Replace `<mynmstateconfig>` with the name of your `NMStateConfig` resource.

    - Replace `<demo-worker4>` with the namespace of your `NMStateConfig` resource.

    - Replace `<value>` with the label value of your `NMStateConfig` resource.

    - Include the `demo-nmstate-label` label name and value in the `spec.nmStateConfigLabelSelector.matchLabels` field in the `InfraEnv` custom resource.

    - Add a MAC address when using the DHCP or static network protocol.

    **Note:** To see additional examples for `NMState` that you can add to the `spec.config` field, see [Additional NMState configuration examples](https://docs.redhat.com/en/documentation/assisted_installer_for_openshift_container_platform/2025/html/installing_openshift_container_platform_with_the_assisted_installer/assembly_network-configuration#additional_nmstate_configuration_examples) in the Assisted Installer for OpenShift Container Platform documentation.

9.  Create the `InfraEnv` custom resource, which provides the configuration to create the discovery ISO. Within this custom resource, you identify values for proxy settings, ignition overrides, and specify `NMState` labels. The value of `spec.nmStateConfigLabelSelector` in this custom resource references the `NMStateConfig` custom resource:

    **Note:** If you plan to include the optional `NMStateConfig` custom resource, you must reference it in the `InfraEnv` custom resource. If you create the `InfraEnv` custom resource before you create the `NMStateConfig` custom resource edit the `InfraEnv` custom resource to reference the `NMStateConfig` custom resource and download the ISO after the reference is added.

    ``` yaml
    apiVersion: agent-install.openshift.io/v1beta1
    kind: InfraEnv
    metadata:
      name: myinfraenv
      namespace: demo-worker4
    spec:
      clusterRef:
        name: single-node  
        namespace: demo-worker4 
      pullSecretRef:
        name: pull-secret
      sshAuthorizedKey: <your_public_key_here>
      nmStateConfigLabelSelector:
        matchLabels:
          demo-nmstate-label: value
      proxy:
        httpProxy: http://USERNAME:PASSWORD@proxy.example.com:PORT
        httpsProxy: https://USERNAME:PASSWORD@proxy.example.com:PORT
        noProxy: .example.com,172.22.0.0/24,10.10.0.0/24
    ```

    - Add the name of the `clusterDeployment` resource to the `clusterRef` field.

    - Add the namespace of the `clusterDeployment` resource to the `clusterRef` field.

      See the following table for the fields that you can add to the `InfraEnv` custom resource:

      |  |  |  |
      |----|----|----|
      | Field | Optional or required | Description |
      | `sshAuthorizedKey` | Optional | You can specify your SSH public key, which enables you to access the host when it is booted from the discovery ISO image. |
      | `nmStateConfigLabelSelector` | Optional | Consolidates advanced network configuration such as static IPs, bridges, and bonds for the hosts. The host network configuration is specified in one or more `NMStateConfig` resources with labels you choose. The `nmStateConfigLabelSelector` property is a Kubernetes label selector that matches your chosen labels. The network configuration for all `NMStateConfig` labels that match this label selector is included in the Discovery Image. When you boot, each host compares each configuration to its network interfaces and applies the appropriate configuration. |
      | `proxy` | Optional | You can specify proxy settings required by the host during discovery in the proxy section. |

      *InfraEnv* field table

    **Note:** When provisioning with IPv6, you cannot define a CIDR address block in the `noProxy` settings. You must define each address separately.

10. Apply the `InfraEnv` custom resource by running the following command:

    ``` bash
    oc apply -f infraenv.yaml
    ```

11. Boot the host from the discovery ISO image that results from the previous procedures. Download the discovery image from the namespace by running the following command:

    ``` bash
    curl --insecure -o image.iso $(kubectl -n sample-namespace get infraenvs.agent-install.openshift.io myinfraenv -o=jsonpath="{.status.isoDownloadURL}")
    ```

12. Move the discovery image to virtual media, a USB drive, or another storage location and boot the host from the discovery image that you downloaded.

13. The `Agent` resource is created automatically. It is registered to the cluster and represents a host that booted from a discovery image. Approve the `Agent` custom resource and start the installation by running the following command. Replace the agent name and UUID with your values:

    ``` bash
    oc -n sample-namespace patch agents.agent-install.openshift.io 07e80ea9-200c-4f82-aff4-4932acb773d4 -p '{"spec":{"approved":true}}' --type merge
    ```

</div>

<div>

<div class="title">

Verification

</div>

- You can confirm that it was approved when the output of the previous command includes an entry for the target cluster that includes a value of `true` for the `APPROVED` parameter.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Create a cluster in an on-premises environment by using the console](clusters.md#create-a-cluster-on-premises-console)

- [Adding hosts on Nutanix with the API](https://docs.redhat.com/en/documentation/assisted_installer_for_openshift_container_platform/2025/html/installing_openshift_container_platform_with_the_assisted_installer/assembly_installing-on-nutanix#adding-hosts-on-nutanix-with-the-api_installing-on-nutanix)

- [Nutanix post-installation configuration](https://docs.redhat.com/en/documentation/assisted_installer_for_openshift_container_platform/2025/html/installing_openshift_container_platform_with_the_assisted_installer/assembly_installing-on-nutanix#nutanix-post-installation-configuration_installing-on-nutanix)

- [Clusters at the network far edge](https://docs.redhat.com/en/documentation/openshift_container_platform/4.20/html/edge_computing/ztp-deploying-far-edge-clusters-at-scale)

- [Creating a credential for a hosted environment](clusters.md#creating-a-credential-hosted)

- [Release images](clusters.md#release-images-intro)

- [Adding hosts to the host inventory by using the console](clusters.md#add-host-host-inventory-console)

- [Configuring third-party CNI plugins for on-premises cluster installation (Technology Preview)](clusters.md#config-third-party-cni-on-prem)

</div>

<a id="create-a-cluster-on-premises-console"></a>

### Create a cluster in an on-premises environment by using the console

You can create on-premises Red Hat OpenShift Container Platform clusters by using the CLI. You can create single-node OpenShift clusters, multi-node clusters, and compact three-node clusters. You can create these clusters on VMware vSphere, Red Hat OpenStack, Nutanix, External, or in a bare metal environment.

Since the platform value is set to `platform=none`, there is no platform integration with the platform where you install the cluster. A single-node OpenShift cluster has only a single node, which hosts the control plane services and the user workloads. Use this configuration when you want to minimize the resource footprint of the cluster.

You can also provision multiple single-node OpenShift clusters on edge resources by using the zero touch provisioning feature, which is a feature that is available with Red Hat OpenShift Container Platform. For more information about zero touch provisioning, see *Clusters at the network far edge* in the additional resources section.

When creating an on-premises cluster, you need a namespace for your resources. Keep all of the resources in a shared namespace.

If you need to create a credential, see *Creating a credential for an on-premises environment* for more information.

<div>

<div class="title">

Prerequisites

</div>

- You must have a deployed hub cluster on a supported OpenShift Container Platform version.

- You need a configured infrastructure environment with a host inventory of configured hosts.

- You must have internet access for your hub cluster (connected), or a connection to an internal or mirror registry that has a connection to the internet (disconnected) to retrieve the required images for creating the cluster.

- You need a configured on-premises credential.

- You need an OpenShift Container Platform image pull secret. See [Using image pull secrets](https://docs.redhat.com/en/documentation/openshift_container_platform/4.20/html/images/managing-images#using-image-pull-secrets).

- You need the following DNS records:

  - The following API base domain must point to the static API VIP:

    `api.<cluster_name>.<base_domain>`

  - The following application base domain must point to the static IP address for Ingress VIP:

    `*.apps.<cluster_name>.<base_domain>`

- Review the hub cluster `KubeAPIServer` certificate verification strategy and update the strategy if needed. To learn what strategy to use for your setup, see [Configuring the hub cluster `KubeAPIServer` verification strategy](clusters.md#set-hub-kube-api-server).

</div>

<div>

<div class="title">

Procedure

</div>

1.  Navigate to **Infrastructure** \> **Clusters**.

2.  On the *Clusters* page, click **Create cluster** and complete the steps in the console. See [On-premises console settings](clusters.md#on-prem-console-settings) for more information about the settings.

3.  Select **Host inventory** as the type of cluster.

    The following options are available for your assisted installation:

    - **Use existing discovered hosts**: Select your hosts from a list of hosts that are in an existing host inventory.

    - **Discover new hosts**: Discover hosts that are not already in an existing infrastructure environment. Discover your own hosts, rather than using one that is already in an infrastructure environment.

</div>

<div>

<div class="title">

Additional resources

</div>

- [On-premises console settings](clusters.md#on-prem-console-settings)

- [Create a cluster in an on-premises environment by using the CLI](clusters.md#create-a-cluster-on-premises-cli)

- [Creating a credential for a hosted environment](clusters.md#creating-a-credential-hosted)

</div>

<a id="on-prem-console-settings"></a>

### On-premises console settings

The name for your cluster is used in the hostname of the cluster.

**Important:** When you create a cluster, the controller creates a namespace for the cluster and its resources. Ensure that you include only resources for that cluster instance in that namespace. Destroying the cluster deletes the namespace and all of the resources in it.

**Note:** Select **YAML: On** to view content updates as you enter the information in the console.

If you want to add your cluster to an existing cluster set, you must have the correct permissions on the cluster set to add it. If you do not have `cluster-admin` privileges when you are creating the cluster, you must select a cluster set on which you have `clusterset-admin` permissions. If you do not have the correct permissions on the specified cluster set, the cluster creation fails. Contact your cluster administrator to provide you with `clusterset-admin` permissions to a cluster set if you do not have any cluster set options to select.

Every managed cluster must be associated with a managed cluster set. If you do not assign the managed cluster to a `ManagedClusterSet`, it is automatically added to the `default` managed cluster set.

If there is already a base DNS domain that is associated with the selected credential that you configured for your provider account, that value is populated in that field. You can change the value by overwriting it, but this setting cannot be changed after the cluster is created. The base domain of your provider is used to create routes to your Red Hat OpenShift Container Platform cluster components. It is configured in the DNS of your cluster provider as a Start of Authority (SOA) record.

The **OpenShift version** identifies the version of the OpenShift Container Platform image that is used to create the cluster. If the version that you want to use is available, you can select the image from the list of images. If the image that you want to use is not a standard image, you can enter the URL to the image that you want to use. See *Release images* to learn more.

When you select a supported OpenShift Container Platform version, an option to select **Install single-node OpenShift** is displayed. A single-node OpenShift cluster contains a single node which hosts the control plane services and the user workloads. See *Scaling hosts to an infrastructure environment* to learn more about adding nodes to a single-node OpenShift cluster after it is created.

If you want your cluster to be a single-node OpenShift cluster, select the **single-node OpenShift** option. You can add additional workers to single-node OpenShift clusters by completing the following steps:

1.  From the console, navigate to **Infrastructure** \> **Clusters** and select the name of the cluster that you created or want to access.

2.  Select **Actions** \> **Add hosts** to add additional workers.

**Note:** The single-node OpenShift control plane requires 8 CPU cores, while a control plane node for a multinode control plane cluster only requires 4 CPU cores.

After you review and save the cluster, your cluster is saved as a draft cluster. You can close the creation process and finish the process later by selecting the cluster name on the *Clusters* page.

If you are using existing hosts, select whether you want to select the hosts yourself, or if you want them to be selected automatically. The number of hosts is based on the number of nodes that you selected. For example, a single-node OpenShift cluster only requires one host, while a standard three-node cluster requires three hosts.

The locations of the available hosts that meet the requirements for this cluster are displayed in the list of *Host locations*. For distribution of the hosts and a more high-availability configuration, select multiple locations.

If you are discovering new hosts with no existing infrastructure environment, complete the steps in *Adding hosts to the host inventory by using the Discovery Image*.

After the hosts are bound, and the validations pass, complete the networking information for your cluster by adding the following IP addresses:

- API VIP: Specifies the IP address to use for internal API communication.

  **Note:** This value must match the name that you used to create the DNS records listed in the prerequisites section. If not provided, the DNS must be pre-configured so that `api.` resolves correctly.

- Ingress VIP: Specifies the IP address to use for ingress traffic.

  **Note:** This value must match the name that you used to create the DNS records listed in the prerequisites section. If not provided, the DNS must be pre-configured so that `test.apps.` resolves correctly.

If you are using Red Hat Advanced Cluster Management for Kubernetes and want to configure your managed cluster klusterlet to run on specific nodes, see [Configure the klusterlet to run on specific nodes](clusters.md#config-klusterlet-nodes) for the required steps.

You can view the status of the installation on the *Clusters* navigation page.

Continue with [Accessing your cluster](clusters.md#accessing-your-cluster) for instructions for accessing your cluster.

<a id="config-agent-proxy"></a>

#### Configure *AgentClusterInstall* proxy

The *AgentClusterInstall* proxy fields determine the proxy settings during installation, and are used to create the cluster-wide proxy resource in the created cluster.

<div>

<div class="title">

Procedure

</div>

- To configure the `AgentClusterInstall` proxy, add the `proxy` settings to the `AgentClusterInstall` resource. See the following YAML sample with `httpProxy`, `httpsProxy`, and `noProxy`:

  ``` yaml
  apiVersion: extensions.hive.openshift.io/v1beta1
  kind: AgentClusterInstall
  spec:
    proxy:
      httpProxy: http://<username>:<password>@<proxy.example.com>:<port>
      httpsProxy: https://<username>:<password>@<proxy.example.com>:<port>
      noProxy: <wildcard-of-domain>,<provisioning-network/CIDR>,<BMC-address-range/CIDR>
  ```

- `httpProxy` is the URL of the proxy for HTTP requests. Replace the username and password values with your credentials for your proxy server. Replace `proxy.example.com` with the path of your proxy server.

- `httpsProxy` is the URL of the proxy for HTTPS requests. Replace the values with your credentials. Replace `port` with the communication port with the proxy server.

- `noProxy` is a comma-separated list of domains and CIDRs for which the proxy should not be used. Replace `wildcard-of-domain` with an entry for domains that should bypass the proxy. Replace `provisioning-network/CIDR` with the IP address of the provisioning network and the number of assigned IP addresses, in CIDR notation. Replace `BMC-address-range/CIDR` with the BMC address and the number of addresses, in CIDR notation.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Enabling the central infrastructure management service](clusters.md#enable-cim)

</div>

<a id="import-intro"></a>

## Cluster import overview

You can import clusters from different Kubernetes cloud providers. After you import, the target cluster becomes a managed cluster for the multicluster engine operator hub cluster. You can generally complete the import tasks anywhere that you can access the hub cluster and the target managed cluster, unless otherwise specified.

- A hub cluster cannot manage *any* other hub cluster, but can manage itself. The hub cluster is configured to automatically be imported and self-managed. You do not need to manually import the hub cluster.

- If you remove a hub cluster and try to import it again, you must add the `local-cluster:true` label to the `ManagedCluster` resource.

**Important:** Cluster lifecycle now supports all providers that are certified through the Cloud Native Computing Foundation (CNCF) Kubernetes Conformance Program. Choose a vendor that is recognized by CNCF for your hybrid cloud multicluster management.

See the following information about using CNCF providers:

- Learn how CNCF providers are certified at [Certified Kubernetes Conformance](https://www.cncf.io/training/certification/software-conformance/).

- For Red Hat support information about CNCF third-party providers, see [Red Hat support with third party components](https://access.redhat.com/articles/third-party-software-support), or [Contact Red Hat support](https://access.redhat.com/support/contact/).

- If you bring your own CNCF conformance certified cluster, you need to change the OpenShift Container Platform CLI `oc` command to the Kubernetes CLI command, `kubectl`.

Read the following topics to learn more about importing a cluster so that you can manage it:

- [Create a new pull secret](clusters.md#creating-new-pull-secret)

- [Import a cluster](clusters.md#importing-cluster)

- [Configure the cluster API address](clusters.md#import-configuring-cluster-api)

- [Configure the klusterlet to run on specific nodes](clusters.md#import-configuring-nodeselector-tolerations)

- [Remove an imported cluster](clusters.md#removing-an-imported-cluster)

- [Detached cluster considerations](clusters.md#detached-cluster-considerations)

- [Prepare for cluster import](clusters.md#preparing-cluster-import)

- [Import a cluster by using the auto import secret](clusters.md#importing-clusters-auto-import-secret)

- [Import a cluster manually](clusters.md#importing-cluster-manual)

- [Import the klusterlet add-on](clusters.md#importing-the-klusterlet)

- [Remove an imported cluster by using the command line interface](clusters.md#removing-imported-cluster-cli)

- [Import a managed cluster by using agent registration](clusters.md#importing-managed-agent)

- [Import an on-premises OpenShift Container Platform cluster manually by using central infrastructure management](clusters.md#import-ocp-cluster)

<a id="creating-new-pull-secret"></a>

### Create a new pull secret

If you need to create a new pull secret, complete the following steps:

**Required access:** Cluster administrator

<div>

<div class="title">

Prerequisites

</div>

- A deployed hub cluster. If you are importing bare metal clusters, the hub cluster must be installed on a supported Red Hat OpenShift Container Platform version.

- A cluster you want to manage.

- The `base64` command line tool.

- A defined `multiclusterhub.spec.imagePullSecret` if you are importing a cluster that was not created by OpenShift Container Platform. This secret might have been created when multicluster engine for Kubernetes operator was installed. See *Custom image pull secret* for more information about how to define this secret.

- Review the hub cluster `KubeAPIServer` certificate verification strategy and update the strategy if needed. To learn what strategy to use for your setup, see [Configuring the hub cluster `KubeAPIServer` verification strategy](clusters.md#set-hub-kube-api-server).

- Ensure that a previously installed agent is deleted from the cluster that you want to import. You must remove the `open-cluster-management-agent` and `open-cluster-management-agent-addon` namespaces to avoid errors.

- For importing in a Red Hat OpenShift Dedicated environment, you need the following:

  - You must have the hub cluster deployed in a Red Hat OpenShift Dedicated environment.

  - The default permission in Red Hat OpenShift Dedicated is dedicated-admin, but that does not contain all of the permissions to create a namespace. You must have `cluster-admin` permissions to import and manage a cluster with multicluster engine operator.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Download your Kubernetes pull secret from [cloud.redhat.com](https://cloud.redhat.com/).

2.  Add the pull secret to the namespace of your hub cluster.

3.  Run the following command to create a new secret in the `open-cluster-management` namespace:

    ``` bash
    oc create secret generic pull-secret -n <open-cluster-management> --from-file=.dockerconfigjson=<path-to-pull-secret> --type=kubernetes.io/dockerconfigjson
    ```

    Replace `open-cluster-management` with the name of the namespace of your hub cluster. The default namespace of the hub cluster is `open-cluster-management`.

    Replace `path-to-pull-secret` with the path to the pull secret that you downloaded.

    The secret is automatically copied to the managed cluster when it is imported.

</div>

<a id="importing-cluster"></a>

### Import a cluster

You can import existing clusters from the console for each of the available cloud providers.

**Important:** When you create a cluster, the controller creates a namespace for the cluster and its resources. Ensure that you include only resources for that cluster instance in that namespace. Destroying the cluster deletes the namespace and all of the resources in it.

Every managed cluster must be associated with a managed cluster set. If you do not assign the managed cluster to a `ManagedClusterSet`, the cluster is automatically added to the `default` managed cluster set.

If you want to add the cluster to a different cluster set, you must have `clusterset-admin` privileges to the cluster set. If you do not have `cluster-admin` privileges when you are importing the cluster, you must select a cluster set on which you have `clusterset-admin` permissions. If you do not have the correct permissions on the specified cluster set, the cluster importing fails. Contact your cluster administrator to provide you with `clusterset-admin` permissions to a cluster set if you do not have cluster set options to select.

If you import a OpenShift Container Platform Dedicated cluster and do not specify a vendor by adding a label for `vendor=OpenShiftDedicated`, or if you add a label for `vendor=auto-detect`, a `managed-by=platform` label is automatically added to the cluster. You can use this added label to identify the cluster as a OpenShift Container Platform Dedicated cluster and retrieve the OpenShift Container Platform Dedicated clusters as a group.

The following table provides the available options for *import mode*, which specifies the method for importing the cluster:

|  |  |
|----|----|
| Run import commands manually | After completing and submitting the information in the console, including any Red Hat Ansible Automation Platform templates, run the provided command on the target cluster to import the cluster. |
| Enter your server URL and API token for the existing cluster | Provide the server URL and API token of the cluster that you are importing. You can specify a Red Hat Ansible Automation Platform template to run when the cluster is upgraded. |
| Provide the `kubeconfig` file | Copy and paste the contents of the `kubeconfig` file of the cluster that you are importing. You can specify a Red Hat Ansible Automation Platform template to run when the cluster is upgraded. |

Options for *import mode*

**Notes:**

- You must have the Red Hat Ansible Automation Platform Resource Operator installed from the Red Hat OpenShift Software Catalog to create and run an Ansible Automation Platform job.

- A hub cluster cannot manage a different hub cluster. A hub cluster is set up to automatically import and manage itself as a `local-cluster`. You do not have to manually import a hub cluster to manage.

- The namespace for the imported cluster must match the name of the cluster. To configure a cluster API address, see [Optional: Configure the cluster API address](clusters.md#import-configuring-cluster-api).

To configure your managed cluster klusterlet to run on specific nodes, see [Optional: Configure the klusterlet to run on specific nodes](clusters.md#import-configuring-nodeselector-tolerations).

<a id="import-configuring-cluster-api"></a>

### Configure the cluster API address

**Optional:** Complete the following steps to configure the **Cluster API address** that is on the cluster details page by configuring the URL that is displayed in the table when you run the `oc get managedcluster` command.

**Required access:** Cluster administrator

<div>

<div class="title">

Prerequisites

</div>

- A deployed hub cluster. If you are importing bare metal clusters, the hub cluster must be installed on a supported Red Hat OpenShift Container Platform version.

- A cluster you want to manage.

- The `base64` command line tool.

- A defined `multiclusterhub.spec.imagePullSecret` if you are importing a cluster that was not created by OpenShift Container Platform. This secret might have been created when multicluster engine for Kubernetes operator was installed. See *Custom image pull secret* for more information about how to define this secret.

- Review the hub cluster `KubeAPIServer` certificate verification strategy and update the strategy if needed. To learn what strategy to use for your setup, see [Configuring the hub cluster `KubeAPIServer` verification strategy](clusters.md#set-hub-kube-api-server).

</div>

<div>

<div class="title">

Procedure

</div>

1.  Log in to your hub cluster with an ID that has `cluster-admin` permissions.

2.  Configure a `kubeconfig` file for your targeted managed cluster.

3.  Edit the managed cluster entry for the cluster that you are importing by running the following command, replacing `cluster-name` with the name of the managed cluster:

    ``` bash
    oc edit managedcluster <cluster-name>
    ```

4.  Add the `ManagedClusterClientConfigs` section to the `ManagedCluster` spec in the YAML file, as shown in the following example. Replace the value of the URL with the URL that provides external access to the managed cluster that you are importing:

    ``` yaml
    spec:
      hubAcceptsClient: true
      managedClusterClientConfigs:
      - url: <https://api.new-managed.dev.redhat.com>
    ```

</div>

<a id="import-configuring-nodeselector-tolerations"></a>

### Configure the klusterlet to run on specific nodes

**Optional:** You can specify which nodes you want the managed cluster klusterlet to run on by configuring the `nodeSelector` and `tolerations` annotation for the managed cluster.

**Required access:** Cluster administrator

<div>

<div class="title">

Prerequisites

</div>

- A deployed hub cluster. If you are importing bare metal clusters, the hub cluster must be installed on a supported Red Hat OpenShift Container Platform version.

- A cluster you want to manage.

- The `base64` command line tool.

- A defined `multiclusterhub.spec.imagePullSecret` if you are importing a cluster that was not created by OpenShift Container Platform. This secret might have been created when multicluster engine for Kubernetes operator was installed. See *Custom image pull secret* for more information about how to define this secret.

- Review the hub cluster `KubeAPIServer` certificate verification strategy and update the strategy if needed. To learn what strategy to use for your setup, see [Configuring the hub cluster `KubeAPIServer` verification strategy](clusters.md#set-hub-kube-api-server).

</div>

<div>

<div class="title">

Procedure

</div>

1.  Select the managed cluster that you want to update from the clusters page in the console.

2.  Set the YAML switch to `On` to view the YAML content.

    **Note:** The YAML editor is only available when importing or creating a cluster. To edit the managed cluster YAML definition after importing or creating, you must use the OpenShift Container Platform command-line interface or the Red Hat Advanced Cluster Management search feature.

3.  Add the `nodeSelector` annotation to the managed cluster YAML definition. The key for this annotation is: `open-cluster-management/nodeSelector`. The value of this annotation is a string map with JSON formatting.

4.  Add the `tolerations` entry to the managed cluster YAML definition. The key of this annotation is: `open-cluster-management/tolerations`. The value of this annotation represents a [toleration](https://github.com/kubernetes/api/blob/release-1.24/core/v1/types.go#L3007) list with JSON formatting. The resulting YAML might resemble the following example:

    ``` yaml
    apiVersion: cluster.open-cluster-management.io/v1
    kind: ManagedCluster
    metadata:
      annotations:
        open-cluster-management/nodeSelector: '{"dedicated":"acm"}'
        open-cluster-management/tolerations: '[{"key":"dedicated","operator":"equal","value":"acm","effect":"NoSchedule"}]'
    ```

    **Note:** If you use a `KlusterletConfig`, the managed cluster uses the configuration in the `KlusterletConfig` settings instead of the settings in the managed cluster annotation.

5.  Alternatively, you can also use a `KlusterletConfig` to configure the `nodeSelector` and `tolerations` for the managed cluster. Apply the following sample YAML content. Replace `<klusterletconfigName>` with the name of your `KlusterletConfig`:

    ``` yaml
    apiVersion: config.open-cluster-management.io/v1alpha1
    kind: KlusterletConfig
    metadata:
      name: <klusterletconfigName>
    spec:
      nodePlacement:
        nodeSelector:
          dedicated: acm
        tolerations:
          - key: dedicated
            operator: Equal
            value: acm
            effect: NoSchedule
    ```

6.  Add the `` agent.open-cluster-management.io/klusterlet-config: `<klusterletconfigName> `` annotation to the managed cluster, replacing `<klusterletconfigName>` with the name of your `KlusterletConfig`.

</div>

<a id="removing-an-imported-cluster"></a>

### Remove an imported cluster

Complete the following procedure to remove an imported cluster and the `open-cluster-management-agent-addon` that was created on the managed cluster.

**Required access:** Cluster administrator

<div>

<div class="title">

Prerequisites

</div>

- A deployed hub cluster. If you are importing bare metal clusters, the hub cluster must be installed on a supported Red Hat OpenShift Container Platform version.

- A cluster you want to manage.

- The `base64` command line tool.

- A defined `multiclusterhub.spec.imagePullSecret` if you are importing a cluster that was not created by OpenShift Container Platform. This secret might have been created when multicluster engine for Kubernetes operator was installed. See *Custom image pull secret* for more information about how to define this secret.

- Review the hub cluster `KubeAPIServer` certificate verification strategy and update the strategy if needed. To learn what strategy to use for your setup, see [Configuring the hub cluster `KubeAPIServer` verification strategy](clusters.md#set-hub-kube-api-server).

</div>

<div>

<div class="title">

Procedure

</div>

- On the *Clusters* page, click **Actions** \> **Detach cluster** to remove your cluster from management.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Detached cluster considerations](clusters.md#detached-cluster-considerations)

</div>

<a id="detached-cluster-considerations"></a>

### Detached cluster considerations

If you attempt to detach the hub cluster, which is named `<your-local-cluster-name>`, be aware that the default setting of `disableHubSelfManagement` is `false` and the hub cluster is the `local-cluster`, which manages itself. This setting causes the hub cluster to reimport itself and manage itself when it is detached and it reconciles the `MultiClusterHub` controller

It might take hours for the hub cluster to complete the detachment process and reimport. If you want to reimport the hub cluster without waiting for the processes to finish, you can run the following command to restart the `multiclusterhub-operator` pod and reimport faster:

``` bash
oc -n open-cluster-management delete -l name=multiclusterhub-operator pods
```

You can change the value of the hub cluster to not import automatically by changing the `disableHubSelfManagement` value to `true`. For more information, see the [disableHubSelfManagement](get_started.md) topic.

By default, the cluster namespace is deleted after you detach a managed cluster.

To prevent multicluster engine operator from deleting the namespace after detaching a managed cluster, add the `open-cluster-management.io/retain-namespace` annotation to the managed cluster namespace.

If you remove the `open-cluster-management.io/retain-namespace` annotation after detaching a managed cluster, multicluster engine operator deletes the cluster namespace.

The `cluster.open-cluster-management.io/managedCluster` and `open-cluster-management.io/cluster-name` labels identify the annotation as a cluster namespace. If you remove the annotation and labels at the same time, multicluster engine operator does not manage the cluster namespace anymore.

<a id="preparing-cluster-import"></a>

### Prepare for cluster import

Before importing a managed cluster by using the CLI, you must complete the following steps.

<div>

<div class="title">

Prerequisites

</div>

- A deployed hub cluster. If you are importing bare metal clusters, the hub cluster must be installed on a supported OpenShift Container Platform version.

- A separate cluster you want to manage.

- The OpenShift Container Platform CLI. See [Getting started with the OpenShift CLI](https://docs.redhat.com/en/documentation/openshift_container_platform/4.20/html/cli_tools/openshift-cli-oc#cli-getting-started) for information about installing and configuring the OpenShift Container Platform CLI.

- A defined `multiclusterhub.spec.imagePullSecret` if you are importing a cluster that was not created by OpenShift Container Platform. This secret might have been created when multicluster engine for Kubernetes operator was installed. See [*MultiClusterHub* advanced configuration](get_started.md#advanced-config-hub) for more information about how to define this secret.

- Review the hub cluster `KubeAPIServer` certificate verification strategy and update the strategy if needed. To learn what strategy to use for your setup, see [Configuring the hub cluster `KubeAPIServer` verification strategy](clusters.md#set-hub-kube-api-server).

- You need one of the following architectures: Linux (x86_64, s390x, ppc64le) or macOS

</div>

<div>

<div class="title">

Procedure

</div>

1.  Log in to your hub cluster by running the following command:

    ``` bash
    oc login
    ```

2.  Run the following command on the hub cluster to create the project and namespace. The cluster name that is defined in `<cluster_name>` is also used as the cluster namespace in the YAML file and commands:

    ``` bash
    oc new-project <cluster_name>
    ```

    **Important:** The `cluster.open-cluster-management.io/managedCluster` label is automatically added to and removed from a managed cluster namespace. Do not manually add it to or remove it from a managed cluster namespace.

3.  Create a file named `managed-cluster.yaml` with the following example content:

    ``` yaml
    apiVersion: cluster.open-cluster-management.io/v1
    kind: ManagedCluster
    metadata:
      name: <cluster_name>
      labels:
        cloud: auto-detect
        vendor: auto-detect
    spec:
      hubAcceptsClient: true
    ```

    **Note:** When the values for `cloud` and `vendor` are set to `auto-detect`, Red Hat Advanced Cluster Management detects the cloud and vendor types automatically from the cluster that you are importing. You can optionally replace the values for `auto-detect` with with the cloud and vendor values for your cluster. See the following example:

    ``` yaml
    cloud: Amazon
    vendor: OpenShift
    ```

4.  Apply the YAML file to the `ManagedCluster` resource by running the following command:

    ``` bash
    oc apply -f managed-cluster.yaml
    ```

</div>

<div class="formalpara">

<div class="title">

Next steps

</div>

You can now continue with either [Import a cluster by using the auto import secret](clusters.md#importing-clusters-auto-import-secret) or [Import a cluster manually](clusters.md#importing-cluster-manual).

</div>

<a id="importing-clusters-auto-import-secret"></a>

### Import a cluster by using the auto import secret

To import a managed cluster by using the auto import secret, you must create a secret that contains either a reference to the `kubeconfig` file of the cluster, or the kube API server and token pair of the cluster.

<div>

<div class="title">

Procedure

</div>

1.  Retrieve the `kubeconfig` file, or the kube API server and token, of the managed cluster that you want to import. See the documentation for your Kubernetes cluster to learn where to locate your `kubeconfig` file or your kube API server and token.

2.  Create a YAML file named `auto-import-secret.yaml` by using content that is similar to the following template:

    ``` yaml
    apiVersion: v1
    kind: Secret
    metadata:
      name: auto-import-secret
      namespace: <cluster_name>
    stringData:
      kubeconfig: |- <kubeconfig_file>
      token: <token_cluster>
      server: <cluster_api_url>
    type: Opaque
    ```

    - Replace `namespace: <cluster_name>` with the name of your cluster.

    - If you are using the `kubeconfig` file, replace `<kubeconfig_file>` with the value for the `kubeconfig` file that has context set to the cluster that you want to import.

    - If you are using the token and server pair, replace `token: <token_cluster>` and `server: <cluster_api_url>` with the cluster access token and cluster API URL instead of the `kubeconfig` file.

3.  Apply the YAML file in the \<cluster_name\> namespace by running the following command:

    ``` bash
    oc apply -f auto-import-secret.yaml
    ```

    **Note:** By default, the auto import secret is used one time and deleted when the import process completes. If you want to keep the auto import secret, add `managedcluster-import-controller.open-cluster-management.io/keeping-auto-import-secret` to the secret. You can add it by running the following command:

    ``` bash
    oc -n <cluster_name> annotate secrets auto-import-secret managedcluster-import-controller.open-cluster-management.io/keeping-auto-import-secret=""
    ```

4.  Validate the `JOINED` and `AVAILABLE` status for your imported cluster. Run the following command from the hub cluster:

    ``` bash
    oc get managedcluster <cluster_name>
    ```

5.  Log in to the managed cluster by running the following command on the cluster:

    ``` bash
    oc login
    ```

6.  You can validate the pod status on the cluster that you are importing by running the following command:

    ``` bash
    oc get pod -n open-cluster-management-agent
    ```

</div>

<div class="formalpara">

<div class="title">

Next steps

</div>

You can now continue with [Import the klusterlet add-on](clusters.md#importing-the-klusterlet).

</div>

<a id="importing-cluster-manual"></a>

### Import a cluster manually

The import command contains pull secret information that is copied to each of the imported managed clusters. Anyone who can access the imported clusters can also view the pull secret information.

<div>

<div class="title">

Procedure

</div>

1.  Obtain the `klusterlet-crd.yaml` file that was generated by the import controller on your hub cluster by running the following command:

    ``` bash
    oc get secret <cluster_name>-import -n <cluster_name> -o jsonpath={.data.crds\\.yaml} | base64 --decode > klusterlet-crd.yaml
    ```

2.  Obtain the `import.yaml` file that was generated by the import controller on your hub cluster by running the following command:

    ``` bash
    oc get secret <cluster_name>-import -n <cluster_name> -o jsonpath={.data.import\\.yaml} | base64 --decode > import.yaml
    ```

3.  Log in to the managed cluster that you are importing by entering the following command:

    ``` bash
    oc login
    ```

4.  Apply the `klusterlet-crd.yaml` that you generated in step 1 by running the following command:

    ``` bash
    oc apply -f klusterlet-crd.yaml
    ```

5.  Apply the `import.yaml` file that you previously generated by running the following command:

    ``` bash
    oc apply -f import.yaml
    ```

6.  You can validate the `JOINED` and `AVAILABLE` status for the managed cluster that you are importing by running the following command from the hub cluster:

    ``` bash
    oc get managedcluster <cluster_name>
    ```

</div>

<div class="formalpara">

<div class="title">

Next steps

</div>

You can now continue with [Import the klusterlet add-on](clusters.md#importing-the-klusterlet).

</div>

<a id="importing-the-klusterlet"></a>

### Import the klusterlet add-on

Implement the `KlusterletAddonConfig` klusterlet add-on configuration to enable other add-ons on your managed clusters. Create and apply the configuration file by completing the following steps:

<div>

<div class="title">

Procedure

</div>

1.  Create a YAML file that is similar to the following example:

    ``` yaml
    apiVersion: agent.open-cluster-management.io/v1
    kind: KlusterletAddonConfig
    metadata:
      name: <cluster_name>
      namespace: <cluster_name>
    spec:
      applicationManager:
        enabled: true
      certPolicyController:
        enabled: true
      policyController:
        enabled: true
      searchCollector:
        enabled: true
    ```

2.  Save the file as `klusterlet-addon-config.yaml`.

3.  Apply the YAML by running the following command:

    ``` bash
    oc apply -f klusterlet-addon-config.yaml
    ```

    **Note:** Add-ons are installed after the managed cluster status that you are importing is `AVAILABLE`.

4.  You can validate the pod status of add-ons on the cluster that you are importing by running the following command:

    ``` bash
    oc get pod -n open-cluster-management-agent-addon
    ```

</div>

<a id="removing-imported-cluster-cli"></a>

### Remove an imported cluster by using the command line interface

To remove a managed cluster by using the command line interface, complete the following step;

<div>

<div class="title">

Procedure

</div>

- Run the following command. Replace `<cluster_name>` with the name of the cluster:

  ``` bash
  oc delete managedcluster <cluster_name>
  ```

</div>

<a id="importing-managed-agent"></a>

### Import a managed cluster by using agent registration

After you install multicluster engine for Kubernetes operator, you are ready to import a cluster and manage it by using the agent registration endpoint.

<div>

<div class="title">

Prerequisites

</div>

- A deployed hub cluster. If you are importing bare metal clusters, the hub cluster must be installed on a supported OpenShift Container Platform version.

- A cluster you want to manage.

- The `base64` command line tool.

- A defined `multiclusterhub.spec.imagePullSecret` if you are importing a cluster that was not created by OpenShift Container Platform. This secret might have been created when multicluster engine for Kubernetes operator was installed. See [*MultiClusterHub* advanced configuration](get_started.md#advanced-config-hub) for more information about how to define this secret.

  If you need to create a new secret, see [Create a new pull secret](clusters.md#creating-new-pull-secret).

- You need one of the following architectures: Linux (x86_64, s390x, ppc64le) or macOS

</div>

<div>

<div class="title">

Procedure

</div>

1.  Get the agent registration server URL by running the following command on the hub cluster:

    ``` bash
    export agent_registration_host=$(oc get route -n multicluster-engine agent-registration -o=jsonpath="{.spec.host}")
    ```

    **Note:** If your hub cluster is using a cluster-wide-proxy, make sure that you are using the URL that managed cluster can access.

2.  Get the cacert by running the following command:

    ``` bash
    oc get configmap -n kube-system kube-root-ca.crt -o=jsonpath="{.data['ca\.crt']}" > ca.crt_
    ```

    **Note:** If you are not using the `kube-root-ca` issued endpoint, use the public `agent-registration` API endpoint CA instead of the `kube-root-ca` CA.

3.  Get the token for the agent registration sever to authorize by applying the following YAML content:

    ``` yaml
    apiVersion: v1
    kind: ServiceAccount
    metadata:
      name: managed-cluster-import-agent-registration-sa
      namespace: multicluster-engine
    ---
    apiVersion: v1
    kind: Secret
    type: kubernetes.io/service-account-token
    metadata:
      name: managed-cluster-import-agent-registration-sa-token
      namespace: multicluster-engine
      annotations:
        kubernetes.io/service-account.name: "managed-cluster-import-agent-registration-sa"
    ---
    apiVersion: rbac.authorization.k8s.io/v1
    kind: ClusterRole
    metadata:
      name: managedcluster-import-controller-agent-registration-client
    rules:
    - nonResourceURLs: ["/agent-registration/*"]
      verbs: ["get"]
    ---
    kind: ClusterRoleBinding
    apiVersion: rbac.authorization.k8s.io/v1
    metadata:
      name: managed-cluster-import-agent-registration
    roleRef:
      apiGroup: rbac.authorization.k8s.io
      kind: ClusterRole
      name: managedcluster-import-controller-agent-registration-client
    subjects:
      - kind: ServiceAccount
        name: managed-cluster-import-agent-registration-sa
        namespace: multicluster-engine
    ```

4.  Run the following command to export the token:

    ``` bash
    export token=$(oc get secret -n multicluster-engine managed-cluster-import-agent-registration-sa-token -o=jsonpath='{.data.token}' | base64 -d)
    ```

5.  Enable the automatic approval and patch the content to `cluster-manager` by running the following command:

    ``` bash
    oc patch clustermanager cluster-manager --type=merge -p '{"spec":{"registrationConfiguration":{"featureGates":[
    {"feature": "ManagedClusterAutoApproval", "mode": "Enable"}], "autoApproveUsers":["system:serviceaccount:multicluster-engine:agent-registration-bootstrap"]}}}'
    ```

    **Note:** You can also disable automatic approval and manually approve certificate signing requests from managed clusters.

6.  Switch to your managed cluster and get the cacert by running the following command:

    ``` bash
    curl --cacert ca.crt -H "Authorization: Bearer $token" https://$agent_registration_host/agent-registration/crds/v1 | oc apply -f -
    ```

7.  Run the following command to import the managed cluster to the hub cluster. Replace `<clusterName>` with the name of you cluster. Replace `<duration>` with a time value. For example, `4h`:

    **Optional:** Replace `<klusterletconfigName>` with the name of your KlusterletConfig.

    ``` bash
    curl --cacert ca.crt -H "Authorization: Bearer $token" https://$agent_registration_host/agent-registration/manifests/<clusterName>?klusterletconfig=<klusterletconfigName>&duration=<duration> | oc apply -f -
    ```

    **Note:** The `kubeconfig` bootstrap in the klusterlet manifest does not expire if you do not set a duration.

</div>

<a id="import-ocp-cluster"></a>

### Import an on-premises OpenShift Container Platform cluster manually by using central infrastructure management

After you install multicluster engine for Kubernetes operator, you are ready to import a managed cluster. You can import an existing OpenShift Container Platform cluster so that you can add additional nodes. Continue reading the following topics to learn more:

- [Import an OpenShift Container Platform cluster](clusters.md#import-ocp-cluster-steps)

- [OpenShift Container Platform cluster resources](clusters.md#import-ocp-cluster-resources)

- [Save and apply managed OpenShift Container Platform cluster resources](clusters.md#save-apply-cluster-resources)

- [Remove the managed OpenShift Container Platform cluster from the source hub cluster](clusters.md#removing-managed-cluster-source-hub)

<a id="import-ocp-cluster-steps"></a>

### Import an OpenShift Container Platform cluster

Complete the following steps to import an OpenShift Container Platform cluster manually, without a static network or a bare metal host, and prepare it for adding nodes:

**Prerequisites:**

- Enable the central infrastructure management feature.

<div>

<div class="title">

Procedure

</div>

1.  Create a namespace for the OpenShift Container Platform cluster that you want to import by applying the following YAML content:

    ``` yaml
    apiVersion: v1
    kind: Namespace
    metadata:
      name: managed-cluster
    ```

2.  Make sure that a `ClusterImageSet` matching the OpenShift Container Platform cluster you are importing exists by applying the following YAML content. Replace `<4.x.0>` with the version of OpenShift Container Platform that you are using:

    ``` yaml
    apiVersion: hive.openshift.io/v1
    kind: ClusterImageSet
    metadata:
      name: openshift-v4.x
    spec:
      releaseImage: quay.io/openshift-release-dev/ocp-release@sha256:22e149142517dfccb47be828f012659b1ccf71d26620e6f62468c264a7ce7863
    ```

3.  Add your pull secret to access the image by applying the following YAML content. Replace \<pull-secret-json\> with your pull secret JSON:

    ``` yaml
    apiVersion: v1
    kind: Secret
    type: kubernetes.io/dockerconfigjson
    metadata:
      name: pull-secret
      namespace: managed-cluster
    stringData:
      .dockerconfigjson: <pull-secret-json>
    ```

4.  Copy the `kubeconfig` from your OpenShift Container Platform cluster to the hub cluster. Get the `kubeconfig` from your OpenShift Container Platform cluster by running the following command. Make sure that `kubeconfig` is set as the cluster being imported:

    ``` bash
    oc get secret -n openshift-kube-apiserver node-kubeconfigs -ojson | jq '.data["lb-ext.kubeconfig"]' --raw-output | base64 -d > /tmp/kubeconfig.some-other-cluster
    ```

5.  If your cluster API is accessed through a custom domain, you must first edit this `kubeconfig` by adding your custom certificates in the `certificate-authority-data` field and by changing the `server` field to match your custom domain. Copy the `kubeconfig` to the hub cluster by running the following command. Make sure that `kubeconfig` is set as your hub cluster:

    ``` bash
    oc -n managed-cluster create secret generic some-other-cluster-admin-kubeconfig --from-file=kubeconfig=/tmp/kubeconfig.some-other-cluster
    ```

6.  Create an `AgentClusterInstall` custom resource by applying the following YAML content:

    ``` yaml
    apiVersion: extensions.hive.openshift.io/v1beta1
    kind: AgentClusterInstall
    metadata:
      name: <your-cluster-name>
      namespace: <managed-cluster>
    spec:
      networking:
        userManagedNetworking: true
      clusterDeploymentRef:
        name: <your-cluster>
      imageSetRef:
        name: openshift-v4.x.z
      provisionRequirements:
        controlPlaneAgents: <control_plane_agents>
      sshPublicKey: <ssh_public_key>
    ```

    - Replace `<your-cluster-name>` with the name of your cluster.

    - Replace `<control_plane_agents>` with `1` if you are using a single-node OpenShift cluster, or with `3` if you are using a multinode cluster.

    - Optional: Replace `<ssh_public_key>` with your SSH public key to log in to nodes for troubleshooting.

7.  Create a `ClusterDeployment` by applying the following YAML content. Replace values where needed:

    ``` yaml
    apiVersion: hive.openshift.io/v1
    kind: ClusterDeployment
    metadata:
      name: <your-cluster-name>
      namespace: managed-cluster
    spec:
      baseDomain: <redhat.com>
      installed: <true>
      clusterMetadata:
          adminKubeconfigSecretRef:
            name: <your-cluster-name-admin-kubeconfig>
          clusterID: <"">
          infraID: <"">
      clusterInstallRef:
        group: extensions.hive.openshift.io
        kind: AgentClusterInstall
        name: your-cluster-name-install
        version: v1beta1
      clusterName: your-cluster-name
      platform:
        agentBareMetal:
      pullSecretRef:
        name: pull-secret
    ```

    - Replace `name: <your-cluster-name>` with the name of your cluster.

    - Replace `baseDomain: <redhat.com>` with the domain that you are using for your OpenShift Container Platform cluster.

    - Replace `installed: <true>` with `true` to automatically import your OpenShift Container Platform cluster as a production environment cluster.

    - Replace `name: <your-cluster-name-admin-kubeconfig>` with a reference to the `kubeconfig` that you created in step 4.

    - Leave `clusterID: <"">` and `infraID: <"">` empty in production environments.

8.  Add an `InfraEnv` custom resource to discover new hosts to add to your cluster by applying the following YAML content. The following example might require additional configuration if you are not using a static IP address:

    ``` yaml
    apiVersion: agent-install.openshift.io/v1beta1
    kind: InfraEnv
    metadata:
      name: your-infraenv
      namespace: managed-cluster
    spec:
      clusterRef:
        name: your-cluster-name
        namespace: managed-cluster
      pullSecretRef:
        name: pull-secret
      sshAuthorizedKey: ""
    ```

    **Notes:** \* The `clusterRef` field is optional if you are using late binding. If you are not using late binding, you must add the `clusterRef`. \* Add the optional `sshAuthorizedKey` field to log in to nodes for troubleshooting.

9.  If the import is successful, a URL to download an ISO file appears. Download the ISO file by running the following command, replacing `<url>` with the URL that appears:

    ``` bash
    oc get infraenv -n managed-cluster some-other-infraenv -ojson | jq ".status.<url>" --raw-output | xargs curl -k -o /storage0/isos/some-other.iso
    ```

    **Note:** You can automate host discovery by using bare metal host.

10. **Optional:** If you want to use Red Hat Advanced Cluster Management features, such as policies, on your OpenShift Container Platform cluster, create a `ManagedCluster` resource. Make sure that the name of your `ManagedCluster` resource matches the name of your `ClusterDeplpoyment` resource. If you are missing the `ManagedCluster` resource, your cluster status is `detached` in the console.

</div>

<a id="import-ocp-cluster-resources"></a>

### OpenShift Container Platform cluster resources

If your OpenShift Container Platform managed cluster was installed by the Assisted Installer, you can move the managed cluster and its resources from one hub cluster to another hub cluster.

You can manage a cluster from a new hub cluster by saving a copy of the original resources, applying them to the new hub cluster, and deleting the original resources. You can then scale down or scale up your managed cluster from the new hub cluster.

**Important:** You can only scale down imported OpenShift Container Platform managed clusters if they were installed by the Assisted Installer.

You can import the following resources and continue to manage your cluster with them:

|  |  |  |
|----|----|----|
| Resource | Optional or required | Description |
| `Agent` | Required |  |
| `AgentClassification` | Optional | Required if you want to classify Agents with a filter query. |
| `AgentClusterInstall` | Required |  |
| `BareMetalHost` | Optional | Required if you are using the `baremetal` platform. |
| `ClusterDeployment` | Required |  |
| `InfraEnv` | Required |  |
| `NMStateConfig` | Optional | Required if you want to apply your network configuration on the hosts. |
| `ManagedCluster` | Required |  |
| `Secret` | Required | The `admin-kubeconfig` secret is required. The `bmc-secret` secret is only required if you are using `BareMetalHosts`. |

Managed cluster resource table

<a id="save-apply-cluster-resources"></a>

### Save and apply managed OpenShift Container Platform cluster resources

To save a copy of your managed cluster resources and apply them to a new hub cluster, complete the following steps:

<div>

<div class="title">

Procedure

</div>

1.  Get your resources from your source hub cluster by running the following command:

    ``` bash
    oc –kubeconfig <source_hub_kubeconfig> -n <managed_cluster_name> get <resource_name> <cluster_provisioning_namespace> -oyaml > <resource_name>.yaml
    ```

    - Replace `<source_hub_kubeconfig>` with the path to the `kubeconfig` file of the source hub cluster.

    - Replace `<managed_cluster_name>` with the name of the managed OpenShift Container Platform cluster.

    - Replace `<resource_name>` with the name of the resource you want to import.

    - Replace `<cluster_provisioning_namespace>` with the namespace of the OpenShift Container Platform cluster.

2.  Repeat the command for every resource you want to import by replacing `<resource_name>` with the name of the resource.

3.  Remove the `ownerReferences` property from the `AgentClusterInstall` resource by running the following command:

    ``` bash
    yq --in-place -y 'del(.metadata.ownerReferences)' AgentClusterInstall.yaml
    ```

4.  Remove the `ownerReferences` property from the `Secret` (`admin-kubeconfig`) resource by running the following command:

    ``` bash
    yq --in-place -y 'del(.metadata.ownerReferences)' AdminKubeconfigSecret.yaml
    ```

5.  Detach the managed cluster from the source hub cluster by running the following command:

    ``` bash
    oc –kubeconfig <target_hub_kubeconfig> delete ManagedCluster <cluster_name>
    ```

    - Replace `<target_hub_kubeconfig>` with the path to the `kubeconfig` file of the target hub cluster.

    - Replace `<cluster_name>` with the name of the managed OpenShift Container Platform cluster.

6.  Create a namespace on the target hub cluster for the managed cluster. Use a similar name as the source hub cluster.

7.  Apply your stored resources on the target hub cluster individually by running the following command:

    ``` bash
    oc –kubeconfig <target_hub_kubeconfig> apply -f <resource_name>.yaml
    ```

    - Replace `<target_hub_kubeconfig>` with the path to the `kubeconfig` file of the target hub cluster.

    - Replace `<resource_name>.yaml` with the name of the resource you want to apply.

    - Replace `<resource_name>.yaml` with `.` if you want to apply all the resources as a group instead of individually.

</div>

<a id="removing-managed-cluster-source-hub"></a>

### Remove a managed OpenShift Container Platform cluster from the source hub cluster

After importing your cluster resources, remove your managed cluster from the source hub cluster by completing the following steps:

<div>

<div class="title">

Procedure

</div>

1.  Set the `spec.preserveOnDelete` parameter to `true` in the `ClusterDeployment` custom resource to prevent destroying the managed cluster.

2.  Complete the steps in [Cluster removal overview](clusters.md#remove-managed-cluster).

</div>

<a id="custom-auto-import-strat"></a>

### Custom automatic import strategies

The following two automatic import strategies exist:

`ImportOnly`  
If a managed cluster is missing the `ManagedClusterImportSucceeded` condition, or the condition is set to `False`, the hub cluster controller applies the klusterlet manifests to the managed cluster to initiate the import.

After the managed cluster joins the hub cluster and the `ManagedClusterImportSucceeded` condition is set to `True`, the hub cluster controller stops applying klusterlet manifests and skips automatic import operations for the cluster. From this point, only the klusterlet agent on the managed cluster synchronizes the hub cluster configuration.

If the klusterlet agent fails, the manifests can become outdated, and might cause the managed cluster to appear in an `Unknown` state on the hub cluster. You must then [import the cluster manually](clusters.md#importing-cluster-manual).

Use the `ImportOnly` strategy for a hub cluster disaster recovery scenario where you want to prevent the initial hub cluster from recovering the managed clusters, if the initial hub cluster restarts unexpectedly after the managed clusters were moved to a different hub cluster.

`ImportAndSync`  
The hub cluster controller applies the klusterlet manifests until the managed cluster joins. After joining, both the hub cluster controller and the klusterlet agent continuously synchronize the klusterlet manifests with the hub cluster configuration, ensuring consistency even if one component stops working.

<a id="change-auto-import-strat"></a>

### Change the automatic import strategy

Set the automatic import behavior of a managed cluster to be either a one-time process or a continuous process.

If you are using multicluster engine for Kubernetes operator 2.9 or later, the default automatic import strategy is `ImportOnly`. If you upgraded your hub cluster from an earlier release, the automatic import strategy is set to `ImportAndSync` to preserve the existing automatic import behavior.

To change the import strategy, use a `ConfigMap` object, named `import-controller-config`, in the multicluster engine operator install namespace. Complete the following steps:

<div>

<div class="title">

Procedure

</div>

1.  Set a custom strategy. Run the following command. Replace `<mce_install_namespace>` with the default namespace where multicluster engine operator is installed, `multicluster-engine`:

    ``` bash
    oc -n <mce_install_namespace> create configmap import-controller-config \
      --from-literal=autoImportStrategy=<ImportOnly|ImportAndSync>
    ```

2.  If you want to include the updated strategy in the cluster backup, add the `backup=true` label to the `ConfigMap` by running the following command:

    ``` bash
    oc -n <mce_install_namespace> label configmap import-controller-config \

      cluster.open-cluster-management.io/backup=true
    ```

</div>

<a id="import-custom-bundle-ca"></a>

### Customize the hub cluster API server URL and CA bundle during import

You might not be able to register a managed cluster on your multicluster engine operator hub cluster if intermediate components exist between the managed cluster and the hub cluster. Example intermediate components include a Virtual IP, load balancer, reverse proxy, or API gateway. If you have an intermediate component, you must use a custom server URL and CA bundle for the hub cluster API server when importing a managed cluster.

**Required access:** Cluster administrator

<div>

<div class="title">

Prerequisites

</div>

- You must configure the intermediate component so that the hub cluster API server is accessible for the managed cluster.

- If the intermediate component terminates the SSL connections between the managed cluster and hub cluster API server, you must bridge the SSL connections and pass the authentication information from the original requests to the back end of the hub cluster API server. You can use the User Impersonation feature of the Kubernetes API server to bridge the SSL connections.

- The intermediate component extracts the client certificate from the original requests, adds Common Name (CN) and Organization (O) of the certificate subject as impersonation headers, and then forwards the modified impersonation requests to the back end of the hub cluster API server.

  **Note:** If you bridge the SSL connections, the cluster proxy add-on does not work.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create a `KlusterConfig` resource with the custom hub cluster API server URL and CA bundle. See the following example:

    ``` yaml
    apiVersion: config.open-cluster-management.io/v1alpha1
    kind: KlusterletConfig
    metadata:
      name: <name>
    spec:
      hubKubeAPIServerConfig:
        url: "https://api.example.com:6443"
        serverVerificationStrategy: UseCustomCABundles
        trustedCABundles:
        - name: <custom-ca-bundle>
          caBundle:
            name: <custom-ca-bundle-configmap>
            namespace: <multicluster-engine>
    ```

    - Replace `<name>` with the name of your klusterlet config.

    - Replace `"https://api.example.com:6443"` with your custom server URL.

    - Replace `<custom-ca-bundle>` with your custom CA bundle name. You can use any value except `auto-detected`, which is reserved for internal use.

    - Replace `<custom-ca-bundle-configmap>` with the name of the CA bundle config map. You can create the config map by running the following command: `oc create -n <configmap-namespace> configmap <configmap-name> --from-file=ca.crt=/path/to/ca/file`

    - Replace `<multicluster-engine>` with the namespace of the CA bundle config map.

2.  Select the `KlusterletConfig` resource when creating a managed cluster by adding an annotation that refers to the resource. See the following example:

    ``` yaml
    apiVersion: cluster.open-cluster-management.io/v1
    kind: ManagedCluster
    metadata:
      annotations:
        agent.open-cluster-management.io/klusterlet-config: <klusterlet_config_name>
      name: <cluster_name>
    spec:
      hubAcceptsClient: true
      leaseDurationSeconds: 60
    ```

    - Replace `<klusterlet_config_name>` with the name of your klusterlet config.

    - Replace `<cluster_name>` with the name of your cluster.

    **Notes:**

    - If you use the console, you might need to enable the YAML view to add the annotation to the `ManagedCluster` resource.

    - You can use a global `KlusterletConfig` to enable the configuration on every managed cluster without using an annotation for binding. See [Global *KlusterletConfig* configuration](clusters.md#config-gloabl-klusterletconfig).

</div>

<a id="config-gloabl-klusterletconfig"></a>

### Global *KlusterletConfig* configuration

If you create a `KlusterletConfig` resource and set the name to `global`, the configurations in the global `KlusterletConfig` are automatically applied on every managed cluster.

In an environment that has a global `KlusterletConfig`, create a cluster-specific `KlusterletConfig` resource and bind it with a managed cluster by adding the `agent.open-cluster-management.io/klusterlet-config: <klusterletconfig-name>` annotation to the `ManagedCluster` resource. The value of the cluster-specific `KlusterletConfig` specification overrides the global `KlusterletConfig` value if you set different values for the same field.

See the following example where the `hubKubeAPIServerURL` field has different values set in your `KlusterletConfig` and the global `KlusterletConfig`. The `https://api.example.test.com:6443` value overrides the `https://api.example.global.com:6443` value:

**Deprecated:** The `hubKubeAPIServerURL` field is deprecated.

``` yaml
apiVersion: config.open-cluster-management.io/v1alpha1
kind: KlusterletConfig
metadata:
  name: test
spec:
  hubKubeAPIServerConfig:
    url: "https://api.example.test.com:6443"
---
apiVersion: config.open-cluster-management.io/v1alpha1
kind: KlusterletConfig
metadata:
  name: global
spec:
  hubKubeAPIServerConfig:
    url: "https://api.example.global.com:6443"
```

The value of the global `KlusterletConfig` is used if there is no cluster-specific `KlusterletConfig` bound to a managed cluster, or the same field is missing or does not have a value in the cluster-specific `KlusterletConfig`.

See the following example, where the `"example.global.com"` value in the `hubKubeAPIServerURL` field of the global `KlusterletConfig` overrides your `KlusterletConfig`:

``` yaml
apiVersion: config.open-cluster-management.io/v1alpha1
kind: KlusterletConfig
metadata:
  name: test
spec:
  hubKubeAPIServerURL: ""
—
apiVersion: config.open-cluster-management.io/v1alpha1
kind: KlusterletConfig
metadata:
  name: global
spec:
  hubKubeAPIServerURL: "example.global.com"
```

See the following example, where the `"example.global.com"` value in the `hubKubeAPIServerURL` field of the global `KlusterletConfig` also overrides your `KlusterletConfig`:

``` yaml
apiVersion: config.open-cluster-management.io/v1alpha1
kind: KlusterletConfig
metadata:
  name: test
---
apiVersion: config.open-cluster-management.io/v1alpha1
kind: KlusterletConfig
metadata:
  name: global
spec:
  hubKubeAPIServerURL: "example.global.com"
```

<a id="specify-registry-img-on-managed-clusters-for-import"></a>

#### Specifying image registry on managed clusters for import

You might need to override the image registry on the managed clusters that you are importing. You can do this by creating a `ManagedClusterImageRegistry` custom resource definition.

The `ManagedClusterImageRegistry` custom resource definition is a namespace-scoped resource.

The `ManagedClusterImageRegistry` custom resource definition specifies a set of managed clusters for a Placement to select, but needs different images from the custom image registry. After the managed clusters are updated with the new images, the following label is added to each managed cluster for identification: `open-cluster-management.io/image-registry=<namespace>.<managedClusterImageRegistryName>`.

The following example shows a `ManagedClusterImageRegistry` custom resource definition:

``` yaml
apiVersion: imageregistry.open-cluster-management.io/v1alpha1
kind: ManagedClusterImageRegistry
metadata:
  name: <imageRegistryName>
  namespace: <namespace>
spec:
  placementRef:
    group: cluster.open-cluster-management.io
    resource: placements
    name: <placementName> 
  pullSecret:
    name: <pullSecretName> 
  registries: 
  - mirror: <mirrored-image-registry-address>
    source: <image-registry-address>
  - mirror: <mirrored-image-registry-address>
    source: <image-registry-address>
```

- Replace with the name of a Placement in the same namespace that selects a set of managed clusters.

- Replace with the name of the pull secret that is used to pull images from the custom image registry.

- List the values for each of the `source` and `mirror` registries. Replace the `mirrored-image-registry-address` and `image-registry-address` with the value for each of the `mirror` and `source` values of the registries.

  - Example 1: To replace the source image registry named `registry.redhat.io/rhacm2` with `localhost:5000/rhacm2`, and `registry.redhat.io/multicluster-engine` with `localhost:5000/multicluster-engine`, use the following example:

``` yaml
registries:
- mirror: localhost:5000/rhacm2/
    source: registry.redhat.io/rhacm2
- mirror: localhost:5000/multicluster-engine
    source: registry.redhat.io/multicluster-engine
```

- Example 2: To replace the source image, `registry.redhat.io/rhacm2/registration-rhel8-operator` with `localhost:5000/rhacm2-registration-rhel8-operator`, use the following example:

  ``` yaml
  registries:
  - mirror: localhost:5000/rhacm2-registration-rhel8-operator
      source: registry.redhat.io/rhacm2/registration-rhel8-operator
  ```

**Important:** If you are importing a managed cluster by using agent registration, you must create a `KlusterletConfig` that contains image registries. See the following example. Replace values where needed:

``` yaml
apiVersion: config.open-cluster-management.io/v1alpha1
kind: KlusterletConfig
metadata:
  name: <klusterletconfigName>
spec:
  pullSecret:
    namespace: <pullSecretNamespace>
    name: <pullSecretName>
  registries:
    - mirror: <mirrored-image-registry-address>
      source: <image-registry-address>
    - mirror: <mirrored-image-registry-address>
      source: <image-registry-address>
```

See [Import a managed cluster by using agent registration](clusters.md#importing-managed-agent) to learn more.

<a id="import-cluster-managedclusterimageregistry"></a>

##### Importing a cluster that has a *ManagedClusterImageRegistry*

Complete the following steps to import a cluster that is customized with a ManagedClusterImageRegistry custom resource definition:

1.  Create a pull secret in the namespace where you want your cluster to be imported. For these steps, the namespace is `myNamespace`.

        $ kubectl create secret docker-registry myPullSecret \
          --docker-server=<your-registry-server> \
          --docker-username=<my-name> \
          --docker-password=<my-password>

2.  Create a Placement in the namespace that you created.

    ``` yaml
    apiVersion: cluster.open-cluster-management.io/v1beta1
    kind: Placement
    metadata:
      name: myPlacement
      namespace: myNamespace
    spec:
      clusterSets:
      - myClusterSet
      tolerations:
      - key: "cluster.open-cluster-management.io/unreachable"
        operator: Exists
    ```

    **Note:** The `unreachable` toleration is required for the Placement to be able to select the cluster.

3.  Create a `ManagedClusterSet` resource and bind it to your namespace.

    ``` yaml
    apiVersion: cluster.open-cluster-management.io/v1beta2
    kind: ManagedClusterSet
    metadata:
      name: myClusterSet

    ---
    apiVersion: cluster.open-cluster-management.io/v1beta2
    kind: ManagedClusterSetBinding
    metadata:
      name: myClusterSet
      namespace: myNamespace
    spec:
      clusterSet: myClusterSet
    ```

4.  Create the `ManagedClusterImageRegistry` custom resource definition in your namespace.

    ``` yaml
    apiVersion: imageregistry.open-cluster-management.io/v1alpha1
    kind: ManagedClusterImageRegistry
    metadata:
      name: myImageRegistry
      namespace: myNamespace
    spec:
      placementRef:
        group: cluster.open-cluster-management.io
        resource: placements
        name: myPlacement
      pullSecret:
        name: myPullSecret
      registry: myRegistryAddress
    ```

5.  Import a managed cluster from the console and add it to a managed cluster set.

6.  Copy and run the import commands on the managed cluster after the `open-cluster-management.io/image-registry=myNamespace.myImageRegistry` label is added to the managed cluster.

<a id="accessing-your-cluster"></a>

### Accessing your cluster

To access an Red Hat OpenShift Container Platform cluster that was created and is managed, complete the following steps:

1.  From the console, navigate to **Infrastructure** \> **Clusters** and select the name of the cluster that you created or want to access.

2.  Select **Reveal credentials** to view the user name and password for the cluster. Note these values to use when you log in to the cluster.

    **Note:** The **Reveal credentials** option is not available for imported clusters.

3.  Select **Console URL** to link to the cluster.

4.  Log in to the cluster by using the user ID and password that you found in step three.

<a id="scaling-managed-intro"></a>

### Scaling managed clusters

For clusters that you created, you can customize and resize your managed cluster specifications, such as virtual machine sizes and number of nodes. See the following option if you are using installer-provisioned infrastructure for cluster deployment:

- [Scaling with MachinePool](clusters.md#scaling-machinepool)

See the following options if you are using central infrastructure management for cluster deployment:

- [Adding worker nodes to OpenShift Container Platform clusters](clusters.md#add-nodes-cim-ocp)

- [Adding control plane nodes to managed clusters](clusters.md#adding-ctrl-nodes-managed)

<a id="scaling-machinepool"></a>

#### Scaling with MachinePool

For clusters that you provision with multicluster engine operator, a `MachinePool` resource is automatically created for you. You can further customize and resize your managed cluster specifications, such as virtual machine sizes and number of nodes, by using `MachinePool`.

- Using the `MachinePool` resource is not supported for bare metal clusters.

- A `MachinePool` resource is a Kubernetes resource on the hub cluster that groups the `MachineSet` resources together on the managed cluster.

- The `MachinePool` resource uniformly configures a set of machine resources, including zone configurations, instance type, and root storage.

- With `MachinePool`, you can manually configure the desired number of nodes or configure autoscaling of nodes on the managed cluster.

<a id="configure-autoscale"></a>

##### Configure autoscaling

Configuring autoscaling provides the flexibility of your cluster to scale as needed to lower your cost of resources by scaling down when traffic is low, and by scaling up to ensure that there are enough resources when there is a higher demand for resources.

- To enable autoscaling on your `MachinePool` resources using the console, complete the following steps:

  1.  In the navigation, select **Infrastructure** \> **Clusters**.

  2.  Click the name of your target cluster and select the *Machine pools* tab.

  3.  From the machine pools page, select **Enable autoscale** from the *Options* menu for the target machine pool.

  4.  Select the minimum and maximum number of machine set replicas. A machine set replica maps directly to a node on the cluster.

      The changes might take several minutes to reflect on the console after you click **Scale**. You can view the status of the scaling operation by clicking **View machines** in the notification of the *Machine pools* tab.

- To enable autoscaling on your `MachinePool` resources using the command line, complete the following steps:

  1.  Enter the following command to view your list of machine pools, replacing `managed-cluster-namespace` with the namespace of your target managed cluster.

          oc get machinepools -n <managed-cluster-namespace>

  2.  Enter the following command to edit the YAML file for the machine pool:

          oc edit machinepool <MachinePool-resource-name> -n <managed-cluster-namespace>

      - Replace `MachinePool-resource-name` with the name of your `MachinePool` resource.

      - Replace `managed-cluster-namespace` with the name of the namespace of your managed cluster.

  3.  Delete the `spec.replicas` field from the YAML file.

  4.  Add the `spec.autoscaling.minReplicas` setting and `spec.autoscaling.maxReplicas` fields to the resource YAML.

  5.  Add the minimum number of replicas to the `minReplicas` setting.

  6.  Add the maximum number of replicas into the `maxReplicas` setting.

  7.  Save the file to submit the changes.

<a id="machinepools-autoscale-disable"></a>

##### Disabling autoscaling

You can disable autoscaling by using the console or the command line.

- To disable autoscaling by using the console, complete the following steps:

  1.  In the navigation, select **Infrastructure** \> **Clusters**.

  2.  Click the name of your target cluster and select the *Machine pools* tab.

  3.  From the machine pools page, select **Disable autoscale** from the *Options* menu for the target machine pool.

  4.  Select the number of machine set replicas that you want. A machine set replica maps directly with a node on the cluster.

      It might take several minutes to display in the console after you click **Scale**. You can view the status of the scaling by clicking **View machines** in the notification on the *Machine pools* tab.

- To disable autoscaling by using the command line, complete the following steps:

  1.  Enter the following command to view your list of machine pools:

          oc get machinepools -n <managed-cluster-namespace>

      Replace `managed-cluster-namespace` with the namespace of your target managed cluster.

  2.  Enter the following command to edit the YAML file for the machine pool:

          oc edit machinepool <name-of-MachinePool-resource> -n <namespace-of-managed-cluster>

      Replace `name-of-MachinePool-resource` with the name of your `MachinePool` resource.

      Replace `namespace-of-managed-cluster` with the name of the namespace of your managed cluster.

  3.  Delete the `spec.autoscaling` field from the YAML file.

  4.  Add the `spec.replicas` field to the resource YAML.

  5.  Add the number of replicas to the `replicas` setting.

  6.  Save the file to submit the changes.

<a id="machinepools-manual-scale"></a>

##### Enabling manual scaling

You can scale manually from the console and from the command line.

<a id="manual-console"></a>

###### Enabling manual scaling with the console

To scale your `MachinePool` resources using the console, complete the following steps:

1.  Disable autoscaling for your `MachinePool` if it is enabled. See the previous steps.

2.  From the console, click **Infrastructure** \> **Clusters**.

3.  Click the name of your target cluster and select the *Machine pools* tab.

4.  From the machine pools page, select **Scale machine pool** from the *Options* menu for the targeted machine pool.

5.  Select the number of machine set replicas that you want. A machine set replica maps directly with a node on the cluster. Changes might take several minutes to reflect on the console after you click **Scale**. You can view the status of the scaling operation by clicking **View machines** from the notification of the Machine pools tab.

<a id="manual-cli"></a>

###### Enabling manual scaling with the command line

To scale your `MachinePool` resources by using the command line, complete the following steps:

1.  Enter the following command to view your list of machine pools, replacing `<managed-cluster-namespace>` with the namespace of your target managed cluster namespace:

        oc get machinepools.hive.openshift.io -n <managed-cluster-namespace>

2.  Enter the following command to edit the YAML file for the machine pool:

        oc edit machinepool.hive.openshift.io <MachinePool-resource-name> -n <managed-cluster-namespace>

    - Replace `MachinePool-resource-name` with the name of your `MachinePool` resource.

    - Replace `managed-cluster-namespace` with the name of the namespace of your managed cluster.

3.  Delete the `spec.autoscaling` field from the YAML file.

4.  Modify the `spec.replicas` field in the YAML file with the number of replicas you want.

5.  Save the file to submit the changes.

<a id="add-nodes-cim-ocp"></a>

#### Adding worker nodes to OpenShift Container Platform clusters

If you are using central infrastructure management, you can customize your OpenShift Container Platform clusters by adding additional production environment nodes.

**Required access:** Administrator

- [Prerequisites](clusters.md#add-nodes-cim-ocp-prereqs)

- [Creating a valid `kubeconfig`](clusters.md#add-nodes-cim-ocp-create-config)

- [Adding worker nodes](clusters.md#add-nodes-cim-ocp-procedure)

<a id="add-nodes-cim-ocp-prereqs"></a>

##### Prerequisites

You must have the new CA certificates required to trust the managed cluster API.

<a id="add-nodes-cim-ocp-create-config"></a>

##### Creating a valid `kubeconfig`

Before adding production environment worker nodes to OpenShift Container Platform clusters, you must check if you have a valid `kubeconfig`.

If the API certificates in your managed cluster changed, complete the following steps to update the `kubeconfig` with new CA certificates:

1.  Check if the `kubeconfig` for your `clusterDeployment` is valid by running the following commands. Replace `<kubeconfig_name>` with the name of your current `kubeconfig` and replace `<cluster_name>` with the name of your cluster:

    ``` bash
    export <kubeconfig_name>=$(oc get cd $<cluster_name> -o "jsonpath={.spec.clusterMetadata.adminKubeconfigSecretRef.name}")
    oc extract secret/$<kubeconfig_name> --keys=kubeconfig --to=- > original-kubeconfig
    oc --kubeconfig=original-kubeconfig get node
    ```

2.  If you receive the following error message, you must update your `kubeconfig` secret. If you receive no error message, continue to [Adding worker nodes](clusters.md#add-nodes-cim-ocp-procedure):

        Unable to connect to the server: tls: failed to verify certificate: x509: certificate signed by unknown authority

3.  Get the `base64` encoded certificate bundle from your `kubeconfig` `certificate-authority-data` field and decode it by running the following command:

    ``` bash
    echo <base64 encoded blob> | base64 --decode > decoded-existing-certs.pem
    ```

4.  Create an updated `kubeconfig` file by copying your original file. Run the following command and replace `<new_kubeconfig_name>` with the name of your new `kubeconfig` file:

    ``` bash
    cp original-kubeconfig <new_kubeconfig_name>
    ```

5.  Append new certificates to the decoded pem by running the following command:

    ``` bash
    cat decoded-existing-certs.pem new-ca-certificate.pem | openssl base64 -A
    ```

6.  Add the `base64` output from the previous command as the value of the `certificate-authority-data` key in your new `kubeconfig` file by using a text editor.

7.  Check if the new `kubeconfig` is valid by querying the API with the new `kubeconfig`. Run the following command. Replace `<new_kubeconfig_name>` with the name of your new `kubeconfig` file:

    ``` bash
    KUBECONFIG=<new_kubeconfig_name> oc get nodes
    ```

    If you receive a successful output, the `kubeconfig` is valid.

8.  Update the `kubeconfig` secret in the Red Hat Advanced Cluster Management hub cluster by running the following command. Replace `<new_kubeconfig_name>` with the name of your new `kubeconfig` file:

    ``` bash
    oc patch secret $original-kubeconfig --type='json' -p="[{'op': 'replace', 'path': '/data/kubeconfig', 'value': '$(openssl base64 -A -in <new_kubeconfig_name>)'},{'op': 'replace', 'path': '/data/raw-kubeconfig', 'value': '$(openssl base64 -A -in <new_kubeconfig_name>)'}]"
    ```

<a id="add-nodes-cim-ocp-procedure"></a>

##### Adding worker nodes

If you have a valid `kubeconfig`, complete the following steps to add production environment worker nodes to OpenShift Container Platform clusters:

1.  Boot the machine that you want to use as a worker node from the ISO you previously downloaded.

    **Note:** Make sure that the worker node meets the requirements for an OpenShift Container Platform worker node.

2.  Wait for an agent to register after running the following command:

    ``` bash
    watch -n 5 "oc get agent -n managed-cluster"
    ```

3.  If the agent registration is successful, an agent is listed. Approve the agent for installation. This can take a few minutes.

    **Note:** If the agent is not listed, exit the `watch` command by pressing Ctrl and C, then log in to the worker node to troubleshoot.

4.  If you are using late binding, run the following command to associate pending unbound agents with your OpenShift Container Platform cluster. Skip to step 5 if you are not using late binding:

    ``` bash
    oc get agent -n managed-cluster -ojson | jq -r '.items[] | select(.spec.approved==false) |select(.spec.clusterDeploymentName==null) | .metadata.name'| xargs oc -n managed-cluster patch -p '{"spec":{"clusterDeploymentName":{"name":"some-other-cluster","namespace":"managed-cluster"}}}' --type merge agent
    ```

5.  Approve any pending agents for installation by running the following command:

    ``` bash
    oc get agent -n managed-cluster -ojson | jq -r '.items[] | select(.spec.approved==false) | .metadata.name'| xargs oc -n managed-cluster patch -p '{"spec":{"approved":true}}' --type merge agent
    ```

Wait for the installation of the worker node. When the worker node installation is complete, the worker node contacts the managed cluster with a Certificate Signing Request (CSR) to start the joining process. The CSR is automatically signed.

<a id="adding-ctrl-nodes-managed"></a>

#### Adding control plane nodes to managed clusters

You can replace a failing control plane by adding control plane nodes to healthy or unhealthy managed clusters.

**Required access:** Administrator

<a id="adding-ctrl-nodes-managed-healthy"></a>

##### Adding control plane nodes to healthy managed clusters

Complete the following steps to add control plane nodes to healthy managed clusters:

1.  Complete the steps in [Adding worker nodes to OpenShift Container Platform clusters](clusters.md#add-nodes-cim-ocp) to add the new control plane node.

2.  If you are using the Discovery ISO to add a node, set the agent to `master` before you approve the agent. Run the following command:

    ``` bash
    oc patch agent <agent-name> -p '{"spec":{"role": "master"}}' --type=merge
    ```

    **Note:** Certificate Signing Requests (CSRs) are not automatically approved.

3.  If you are using a `BareMetalHost` to add a node, add the following line to your `BareMetalHost` annotations when creating the `BareMetalHost` resource:

    ``` yaml
        bmac.agent-install.openshift.io/role: master
    ```

4.  Follow the steps in [Replacing a control plane node in a healthy cluster](https://docs.redhat.com/en/documentation/assisted_installer_for_openshift_container_platform/2025/html-single/installing_openshift_container_platform_with_the_assisted_installer/index#installing-control-plane-node-healthy-cluster_expanding-the-cluster) in the Assisted Installer for OpenShift Container Platform documentation.

<a id="adding-ctrl-nodes-managed-healthy-api"></a>

##### Adding control plane nodes to healthy managed clusters by using the API

Complete the following steps to add control plane nodes to healthy managed clusters by using the API:

1.  Log in to the hub cluster by running the following command. Add the name of your cluster:

    ``` bash
    oc login --token=sha256~value--server=https://api.<cluster-name>.basedomain:6443
    ```

2.  Boot the machine that you want to use as a control plane node from your Discovery ISO.

    **Note:** Alternatively, apply the new host to your `InfraEnv` by applying the `BareMetalHost` YAML.

3.  Check the agent state to ensure that the agent is ready to bind to the cluster again. Run the following commands and replace variables where needed:

    1.  Run the following command to switch your inventory. Replace `<host-inventory-namespace>` with your namespace:

        ``` bash
        oc project <host-inventory-namespace>
        ```

    2.  Run the following command to get the state of your agent. Replace `<agent-name>` with the name of your agent:

        ``` bash
        oc get agent <agent-name> -oyaml | grep state
        ```

    3.  In the output, check the `stateInfo` line to make sure that the host is ready to bind to a cluster.

4.  Set the role of your host to `master`:

    1.  If you are using the Discovery ISO to add a node, approve the agent and set the role to `master`. Run the following command:

        ``` bash
        oc patch agent <agent-name> -p '{"spec":{"approved":true,"role":"master"}}' --type=merge
        ```

    2.  If you are using a `BareMetalHost` to add a node, add the following line to your `BareMetalHost` annotations when creating the `BareMetalHost` resource:

    ``` yaml
        bmac.agent-install.openshift.io/role: master
    ```

5.  Verify the patch by running the following command:

    ``` bash
    oc get agent
    ```

    In the output, ensure that each line in the `APPROVED` column says `true` and that the `ROLE` is `master`. See the following examples:

    ``` bash
    NAME                                   CLUSTER    APPROVED    ROLE    STAGE
    c6e00642-0e11-1689-a79d-0e131d2c6ecf              true        master
    ```

6.  Add the agent to the cluster by running the following command:

    ``` bash
    oc patch agent <agent name> -p '{"spec":{"clusterDeploymentName":{"name":"<managed-cluster-name>","namespace":"<managed-cluster-namespace>"}}}' --type=merge
    ```

7.  Confirm that the agent is bound to the cluster by running the following command:

    ``` bash
    oc get agent
    ```

    See the following example output:

    ``` bash
    NAME                                   CLUSTER    APPROVED    ROLE    STAGE
    c6e00642-0e11-1689-a79d-0e131d2c6ecf   hcpagent   true        master
    ```

8.  Verify the agent status by the running the following command. While the agent is installing and joining the cluster, you might need to wait a few minutes:

    ``` bash
    oc get agent -w
    ```

    **Note:** Certificate Signing Requests (CSRs) are not automatically approved.

9.  After the agent reaches the `Rebooting` stage, you must manually approve the CSRs. Complete the following steps:

    1.  Get the managed cluster `kubeconfig` file by running the following command:

        ``` bash
        kubeconfig_secret_name=$(oc -n ${cluster_name} get clusterdeployments ${cluster_name} -ojsonpath='{.spec.clusterMetadata.adminKubeconfigSecretRef.name}')
        oc -n ${cluster_name} get secret ${kubeconfig_secret_name} -ojsonpath={.data.kubeconfig} | base64 -d > managed-cluster.kubeconfig
        ```

    2.  Find any pending CSRs on the managed cluster by running the following command:

        ``` bash
        oc --kubeconfig managed-cluster.kubeconfig get csr | grep Pending
        ```

    3.  Approve any pending CSRs for the agent in the managed cluster. Run the following command and replace `<csr-name>` with your CSR name:

        ``` bash
        oc  --kubeconfig managed-cluster.kubeconfig  adm certificate approve <csr-name>
        ```

The host is installed when the `STAGE` shows `Done`. See the following output example:

``` bash
NAME                                   CLUSTER    APPROVED   ROLE     STAGE
c6e00642-0e11-1689-a79d-0e131d2c6ecf   hcpagent   true       master   Done
```

<a id="adding-ctrl-nodes-managed-unhealthy"></a>

##### Adding control plane nodes to unhealthy managed clusters

Complete the following steps to add control plane nodes to unhealthy managed clusters:

1.  Remove the agent for unhealthy control plane nodes.

2.  If you used the zero-touch provisioning flow for deployment, remove the bare metal host.

3.  Complete the steps in [Adding worker nodes to OpenShift Container Platform clusters](clusters.md#add-nodes-cim-ocp) for your the new control plane node.

4.  Set the agent to `master` before you approve the agent by running the following command:

    ``` bash
    oc patch agent <AGENT-NAME> -p '{"spec":{"role": "master"}}' --type=merge
    ```

    **Note:** CSRs are not automatically approved.

5.  Follow the steps in [Installing a primary control plane node on an unhealthy cluster](https://docs.redhat.com/en/documentation/assisted_installer_for_openshift_container_platform/2025/html/installing_openshift_container_platform_with_the_assisted_installer/expanding-the-cluster#installing-primary-control-plane-node-unhealthy-cluster_expanding-the-cluster) in the Assisted Installer for OpenShift Container Platform documentation.

<a id="hibernating-a-created-cluster"></a>

### Hibernating a created cluster

You can hibernate a cluster that was created using multicluster engine operator to conserve resources. A hibernating cluster requires significantly fewer resources than one that is running, so you can potentially lower your provider costs by moving clusters in and out of a hibernating state. This feature only applies to clusters that were created by multicluster engine operator in the following environments:

- Amazon Web Services

- Microsoft Azure

- Google Cloud Platform

<a id="hibernate-cluster-console"></a>

#### Hibernate a cluster by using the console

To use the console to hibernate a cluster that was created by multicluster engine operator, complete the following steps:

1.  From the navigation menu, select **Infrastructure** \> **Clusters**. Ensure that the *Manage clusters* tab is selected.

2.  Select **Hibernate cluster** from the *Options* menu for the cluster. **Note:** If the *Hibernate cluster* option is not available, you cannot hibernate the cluster. This can happen when the cluster is imported, and not created by multicluster engine operator.

The status for the cluster on the *Clusters* page is `Hibernating` when the process completes.

**Tip:** You can hibernate multiple clusters by selecting the clusters that you want to hibernate on the *Clusters* page, and selecting **Actions** \> **Hibernate clusters**.

Your selected cluster is hibernating.

<a id="hibernate-cluster-cli"></a>

#### Hibernate a cluster by using the CLI

To use the CLI to hibernate a cluster that was created by multicluster engine operator, complete the following steps:

1.  Enter the following command to edit the settings for the cluster that you want to hibernate:

        oc edit clusterdeployment <name-of-cluster> -n <namespace-of-cluster>

    Replace `name-of-cluster` with the name of the cluster that you want to hibernate.

    Replace `namespace-of-cluster` with the namespace of the cluster that you want to hibernate.

2.  Change the value for `spec.powerState` to `Hibernating`.

3.  Enter the following command to view the status of the cluster:

        oc get clusterdeployment <name-of-cluster> -n <namespace-of-cluster> -o yaml

    Replace `name-of-cluster` with the name of the cluster that you want to hibernate.

    Replace `namespace-of-cluster` with the namespace of the cluster that you want to hibernate.

    When the process of hibernating the cluster is complete, the value of the type for the cluster is `type=Hibernating`.

Your selected cluster is hibernating.

<a id="resuming-normal-operation-of-a-hibernating-cluster-console"></a>

#### Resuming normal operation of a hibernating cluster by using the console

To resume normal operation of a hibernating cluster by using the console, complete the following steps:

1.  From the navigation menu, select **Infrastructure** \> **Clusters**. Ensure that the *Manage clusters* tab is selected.

2.  Select **Resume cluster** from the *Options* menu for the cluster that you want to resume.

The status for the cluster on the *Clusters* page is `Ready` when the process completes.

**Tip:** You can resume multiple clusters by selecting the clusters that you want to resume on the *Clusters* page, and selecting **Actions** \> **Resume clusters**.

Your selected cluster is resuming normal operation.

<a id="resuming-normal-operation-of-a-hibernating-cluster-cli"></a>

#### Resuming normal operation of a hibernating cluster by using the CLI

To resume normal operation of a hibernating cluster by using the CLI, complete the following steps:

1.  Enter the following command to edit the settings for the cluster:

        oc edit clusterdeployment <name-of-cluster> -n <namespace-of-cluster>

    Replace `name-of-cluster` with the name of the cluster that you want to hibernate.

    Replace `namespace-of-cluster` with the namespace of the cluster that you want to hibernate.

2.  Change the value for `spec.powerState` to `Running`.

3.  Enter the following command to view the status of the cluster:

        oc get clusterdeployment <name-of-cluster> -n <namespace-of-cluster> -o yaml

    Replace `name-of-cluster` with the name of the cluster that you want to hibernate.

    Replace `namespace-of-cluster` with the namespace of the cluster that you want to hibernate.

    When the process of resuming the cluster is complete, the value of the type for the cluster is `type=Running`.

Your selected cluster is resuming normal operation.

<a id="updating-your-cluster"></a>

### Updating your cluster

After you create Red Hat OpenShift Container Platform clusters that you want to manage with multicluster engine operator, you can use the multicluster engine operator console to update those clusters to the latest minor version that is available in the version channel that the managed cluster uses.

In a connected environment, the updates are automatically identified with notifications provided for each cluster that requires an update in the console.

<a id="updating-your-cluster-prereq"></a>

#### Prerequisites

- Verify that you meet all of the prerequisites for updating to that version. You must update the version channel on the managed cluster before you can update the cluster with the console.

  **Note:** After you update the version channel on the managed cluster, the multicluster engine operator console displays the latest versions that are available for the update.

- Your OpenShift Container Platform managed clusters must be in a *Ready* state.

**Important:** You cannot update Red Hat OpenShift Kubernetes Service managed clusters or OpenShift Container Platform managed clusters on Red Hat OpenShift Dedicated by using the multicluster engine operator console.

<a id="updating-your-cluster-conn-steps"></a>

#### Updating your cluster in a connected environment

To update your cluster in a connected environment, complete the following steps:

1.  From the navigation menu, go to **Infrastructure** \> **Clusters**. If an update is available, it appears in the *Distribution version* column.

2.  Select the clusters in *Ready* state that you want to update. You can only update OpenShift Container Platform clusters in the console.

3.  Select **Update**.

4.  Select the new version of each cluster.

5.  Select **Update**.

If your cluster update fails, the Operator generally retries the update a few times, stops, and reports the status of the failing component. In some cases, the update process continues to cycle through attempts to complete the process. Rolling your cluster back to a previous version following a failed update is not supported. Contact Red Hat support for assistance if your cluster update fails.

<a id="selecting-a-channel"></a>

#### Selecting a channel

You can use the console to select a channel for your cluster updates on OpenShift Container Platform. After selecting a channel, you are automatically reminded of cluster updates that are available for both errata versions and release versions.

To select a channel for your cluster, complete the following steps:

1.  From the navigation, select **Infrastructure** \> **Clusters**.

2.  Select the name of the cluster that you want to change to view the *Cluster details* page. If a different channel is available for the cluster, an edit icon is displayed in the *Channel* field.

3.  Click the **Edit** icon to change the setting in the field.

4.  Select a channel in the *New channel* field.

You can find the reminders for the available channel updates in the *Cluster details* page of the cluster.

<a id="updating-disconnected-cluster"></a>

#### Updating a disconnected cluster

You can use OpenShift Update Service with multicluster engine operator to update clusters in a disconnected environment.

In some cases, security concerns prevent you from connecting clusters directly to the internet. Configuring OpenShift Update Service to know when updates are available, even when your managed cluster is not connected to the internet.

OpenShift Update Service is a separate operator that monitors the available versions of your managed clusters in a disconnected environment, and makes them available for updating your managed clusters. After you configure OpenShift Update Service, it can perform the following actions:

- Monitor when updates are available for your disconnected clusters.

- Identify which updates are mirrored to your local site for updating by using the graph data file.

- Notify you that an update is available for your cluster by using the console.

Follow the steps in [Updating a cluster using the CLI](https://docs.redhat.com/en/documentation/openshift_container_platform/4.20/html/updating_clusters/performing-a-cluster-update#updating-cluster-cli) in the Red Hat OpenShift Container Platform documentation on your managed cluster to update your cluster in a disconnected environment.

<a id="proxy-intro"></a>

## Cluster proxy

Configure proxy settings for multicluster engine operator so that you can create clusters, register managed clusters, and access managed cluster resources when a direct network path is not available.

You might need a proxy in the following situations:

- You create an Red Hat OpenShift Container Platform cluster when your hub cluster is connected through a proxy server. Configure the `cluster-wide-proxy` setting in your `install-config` YAML. See [Create a cluster in a proxy environment](clusters.md#create-a-cluster-in-a-proxy-environment).

- Your managed cluster cannot reach the multicluster engine operator hub cluster directly. For example, the hub cluster is in a public cloud and the managed cluster is in a private cloud behind a firewall. Configure an HTTP or HTTPS proxy so that the managed cluster can access the hub cluster. See [Configure the proxy between hub cluster and managed cluster](clusters.md#config-proxy-hub-managed).

- A managed cluster is behind a firewall and you cannot access it directly from the hub cluster. Enable and configure the cluster proxy add-on to access the managed cluster `kube-apiserver` with a more secure connection. The `cluster-proxy-addon` component automates the installation of `apiserver-network-proxy` on the hub and managed clusters by using a reverse proxy server.

**Note:** If the klusterlet agent on the managed cluster requires proxy settings to access the `apiserver` on the hub cluster instead of connecting directly, configure the proxy between the hub cluster and the managed cluster.

See the following documentation:

- [Create a cluster in a proxy environment](clusters.md#create-a-cluster-in-a-proxy-environment)

- [Configure cluster proxy add-ons for hub clusters and managed clusters](clusters.md#config-cluster-proxy-addon-hub-managed)

- [Configure proxy settings for cluster proxy add-ons](clusters.md#cluster-proxy-addon-settings)

- [Configure the proxy between hub cluster and managed cluster](clusters.md#config-proxy-hub-managed)

- [Disable the proxy between hub cluster and managed cluster](clusters.md#disable-proxy-hub-managed)

- [Managed cluster `kube-apiserver` access](clusters.md#access-managed-cluster-kube-apiserver)

- [Gather data with a managed cluster user token](clusters.md#gather-data-managed-token)

- [Gather data with a hub cluster user token](clusters.md#gather-data-hub-token)

- [Gather data with managed cluster services](clusters.md#gather-data-managed-cluster-services)

<a id="config-cluster-proxy-addon-hub-managed"></a>

### Configure cluster proxy add-ons for hub clusters and managed clusters

Configure a cluster proxy add-on for a hub cluster or managed cluster so that you can access the managed cluster `kube-apiserver`. Configure the `kubeconfig` file to access the managed cluster `kube-apiserver` by completing the following steps.

<div>

<div class="title">

Procedure

</div>

1.  Provide a valid access token for the managed cluster.

    **Note:** : You can use the corresponding token of the service account. You can also use the default service account that is in the default namespace.

    1.  Export the `kubeconfig` file of the managed cluster by running the following command:

        ``` bash
        export KUBECONFIG=<managed-cluster-kubeconfig>
        ```

    2.  Add a role to your service account that allows it to access pods by running the following commands:

        ``` bash
        oc create role -n default test-role --verb=list,get --resource=pods
        oc create rolebinding -n default test-rolebinding --serviceaccount=default:default --role=test-role
        ```

    3.  Run the following command to locate the secret of the service account token. Replace `default-token` with the name of your secret:

        ``` bash
        oc get secret -n default | grep <default-token>
        ```

    4.  Run the following command to copy the token. Replace `default-token` with the name of your secret:

    ``` bash
    export MANAGED_CLUSTER_TOKEN=$(kubectl -n default get secret <default-token> -o jsonpath={.data.token} | base64 -d)
    ```

2.  Configure the `kubeconfig` file on the Red Hat Advanced Cluster Management hub cluster.

    1.  Export the current `kubeconfig` file on the hub cluster by running the following command:

        ``` bash
        oc config view --minify --raw=true > cluster-proxy.kubeconfig
        ```

    2.  Modify the `server` file with your editor. This example uses commands when using `sed`. Run `alias sed=gsed`, if you are using OSX.

        ``` bash
        export TARGET_MANAGED_CLUSTER=<managed-cluster-name>

        export NEW_SERVER=https://$(oc get route -n multicluster-engine cluster-proxy-addon-user -o=jsonpath='{.spec.host}')/$TARGET_MANAGED_CLUSTER

        sed -i'' -e '/server:/c\    server: '"$NEW_SERVER"'' cluster-proxy.kubeconfig

        export CADATA=$(oc get configmap -n openshift-service-ca kube-root-ca.crt -o=go-template='{{index .data "ca.crt"}}' | base64)

        sed -i'' -e '/certificate-authority-data:/c\    certificate-authority-data: '"$CADATA"'' cluster-proxy.kubeconfig
        ```

    3.  Delete the original user credentials by entering the following commands:

        ``` bash
        sed -i'' -e '/client-certificate-data/d' cluster-proxy.kubeconfig
        sed -i'' -e '/client-key-data/d' cluster-proxy.kubeconfig
        sed -i'' -e '/token/d' cluster-proxy.kubeconfig
        ```

    4.  Add the token of the service account:

    ``` bash
    sed -i'' -e '$a\    token: '"$MANAGED_CLUSTER_TOKEN"'' cluster-proxy.kubeconfig
    ```

3.  List all of the pods on the target namespace of the target managed cluster by running the following command. Replace the `default` namespace with the namespace that you want to use:

    ``` bash
    oc get pods --kubeconfig=cluster-proxy.kubeconfig -n <default>
    ```

4.  Access other services on the managed cluster. This feature is available when the managed cluster is a Red Hat OpenShift Container Platform cluster. The service must use `service-serving-certificate` to generate server certificates:

    - From the managed cluster, use the following service account token:

      ``` bash
      export PROMETHEUS_TOKEN=$(kubectl get secret -n openshift-monitoring $(kubectl get serviceaccount -n openshift-monitoring prometheus-k8s -o=jsonpath='{.secrets[0].name}') -o=jsonpath='{.data.token}' | base64 -d)
      ```

    - From the hub cluster, convert the certificate authority to a file by running the following command:

    ``` bash
    oc get configmap kube-root-ca.crt -o=jsonpath='{.data.ca\.crt}' > hub-ca.crt
    ```

5.  Get Prometheus metrics of the managed cluster by using the following commands:

    ``` bash
    export SERVICE_NAMESPACE=openshift-monitoring
    export SERVICE_NAME=prometheus-k8s
    export SERVICE_PORT=9091
    export SERVICE_PATH="api/v1/query?query=machine_cpu_sockets"
    curl --cacert hub-ca.crt $NEW_SERVER/api/v1/namespaces/$SERVICE_NAMESPACE/services/$SERVICE_NAME:$SERVICE_PORT/proxy-service/$SERVICE_PATH -H "Authorization: Bearer $PROMETHEUS_TOKEN"
    ```

</div>

<div>

<div class="title">

Additional resources

</div>

- [Configure proxy settings for cluster proxy add-ons](clusters.md#cluster-proxy-addon-settings)

</div>

<a id="cluster-proxy-addon-settings"></a>

### Configure proxy settings for cluster proxy add-ons

In some environments, a managed cluster is behind a firewall and that you cannot access directly through the hub cluster. To gain access, you can set up a proxy add-on to access the `kube-apiserver` of the managed cluster with a more secure connection.

Configure the proxy settings for cluster proxy add-ons to allow a managed cluster to communicate with the hub cluster through a HTTP and HTTPS proxy server. You might need to configure the proxy settings if the cluster proxy add-on agent requires access to the hub cluster through the proxy server.

**Required access:** Editor

<div>

<div class="title">

Procedure

</div>

1.  Create an `AddOnDeploymentConfig` resource on your hub cluster and add the `spec.proxyConfig` parameter. See the following example:

    ``` yaml
    apiVersion: addon.open-cluster-management.io/v1alpha1
    kind: AddOnDeploymentConfig
    metadata:
      name: <name>
      namespace: <namespace>
    spec:
      agentInstallNamespace: open-cluster-management-agent-addon
      proxyConfig:
        httpsProxy: "http://<username>:<password>@<ip>:<port>"
        noProxy: ".cluster.local,.svc,172.30.0.1"
        caBundle: <value>
    ```

    - Replace `name` with your add-on deployment config name.

    - Replace `namespace` with your managed cluster name.

    - Specify either a HTTP proxy or a HTTPS proxy in the `httpsProxy` field.

    - Add the IP address of the `kube-apiserver` to `noProxy`. To get the IP address, run following command on your managed cluster: `oc -n default describe svc kubernetes | grep IP:`

    - If you specify a HTTPS proxy in the `httpsProxy` field, set the proxy server CA bundle in `caBundle`.

      **Note:** The `spec.installNamespace` field is deprecated. See [Product deprecations and removals](mce_release_notes.md#deprecations-removals-cluster-mce) to learn more.

2.  Update the `ManagedClusterAddOn` resource by referencing the `AddOnDeploymentConfig` resource that you created. See the following example:

    ``` yaml
    apiVersion: addon.open-cluster-management.io/v1alpha1
    kind: ManagedClusterAddOn
    metadata:
      name: cluster-proxy
      namespace: <namespace>
    spec:
    installNamespace: open-cluster-management-addon
    configs:
      group: addon.open-cluster-management.io
      resource: addondeploymentconfigs
      name: <name>
      namespace: <namespace>
    ```

    - Replace `namespace` with your managed cluster name.

    - Replace `name` with your add-on deployment config name.

      **Note:** The `spec.installNamespace` field is deprecated. See [Product deprecations and removals](mce_release_notes.md#deprecations-removals-cluster-mce) to learn more.

3.  Verify the proxy settings by checking if the cluster proxy agent pod in the `open-cluster-management-addon` namespace has `HTTPS_PROXY` or `NO_PROXY` environment variables on the managed cluster.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Configure cluster proxy add-ons for hub clusters and managed clusters](clusters.md#config-cluster-proxy-addon-hub-managed)

- [Configure the proxy between hub cluster and managed cluster](clusters.md#config-proxy-hub-managed)

</div>

<a id="create-a-cluster-in-a-proxy-environment"></a>

### Create a cluster in a proxy environment

You can create a Red Hat OpenShift Container Platform cluster when your hub cluster is connected through a proxy server.

<div>

<div class="title">

Prerequisites

</div>

- One of the following situations must be true:

  - multicluster engine operator has a private network connection with the managed cluster that you are creating, with managed cluster access to the Internet by using a proxy.

  - The managed cluster is on an infrastructure provider, but the firewall ports enable communication from the managed cluster to the hub cluster.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Configure the `cluster-wide-proxy` setting on the hub cluster by adding the following information to your `install-config` YAML that is stored in your Secret:

    ``` yaml
    apiVersion: v1
    kind: Proxy
    baseDomain: <domain>
    proxy:
      httpProxy: http://<username>:<password>@<proxy.example.com>:<port>
      httpsProxy: https://<username>:<password>@<proxy.example.com>:<port>
      noProxy: <wildcard-of-domain>,<provisioning-network/CIDR>,<BMC-address-range/CIDR>
    ```

    - Replace `username` with the username for your proxy server.

    - Replace `password` with the password to access your proxy server.

    - Replace `proxy.example.com` with the path of your proxy server.

    - Replace `port` with the communication port with the proxy server.

    - Replace `wildcard-of-domain` with an entry for domains that should bypass the proxy.

    - Replace `provisioning-network/CIDR` with the IP address of the provisioning network and the number of assigned IP addresses, in CIDR notation.

    - Replace `BMC-address-range/CIDR` with the BMC address and the number of addresses, in CIDR notation.

2.  Provision the cluster by completing the procedure for creating a cluster. See *Creating a cluster* to select your provider.

    **Note:** You can only use `install-config` YAML when deploying your cluster. After deploying your cluster, any new changes you make to `install-config` YAML do not apply. To update the configuration after deployment, you must use policies. See *Pod policy* for more information.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Creating clusters](clusters.md#create-intro)

- [Configure *AgentClusterInstall* proxy](clusters.md#config-agent-proxy)

- [Pod policy](governance.md#pod-policy)

</div>

<a id="custom-hub-api-certificates"></a>

### Customizing the hub cluster *KubeAPIServer* certificates

The managed clusters communicate with the hub cluster through a mutual connection with the Red Hat OpenShift Container Platform `KubeAPIServer` external load balancer. The default OpenShift Container Platform `KubeAPIServer` certificate is issued by an internal OpenShift Container Platform cluster certificate authority (CA) when OpenShift Container Platform is installed. If necessary, you can add or change certificates.

Changing the API server certificate might impact the communication between the managed cluster and the hub cluster. When you add the named certificate before installing the product, you can avoid an issue that might leave your managed clusters in an offline state.

The following list contains some examples of when you might need to update your certificates:

- You want to replace the default API server certificate for the external load balancer with your own certificate. By following the guidance in [Adding API server certificates](https://docs.redhat.com/documentation/en-us/openshift_container_platform/4.17/html/security_and_compliance/configuring-certificates#api-server-certificates) in the OpenShift Container Platform documentation, you can add a named certificate with host name `api.<cluster_name>.<base_domain>` to replace the default API server certificate for the external load balancer. Replacing the certificate might cause some of your managed clusters to move to an offline state. If your clusters are in an offline state after upgrading the certificates, follow the troubleshooting instructions for [Troubleshooting imported clusters offline after certificate change](mce_troubleshooting.md#troubleshooting-imported-clusters-offline-after-certificate-change-mce) to resolve it.

**Note:** Adding the named certificate before installing the product helps to avoid your clusters moving to an offline state.

- The named certificate for the external load balancer is expiring and you need to replace it. If both the old and the new certificate share the same root CA certificate, despite the number of intermediate certificates, you can follow the guidance in [Adding API server certificates](https://docs.redhat.com/documentation/en-us/openshift_container_platform/4.17/html/security_and_compliance/configuring-certificates#api-server-certificates) in the OpenShift Container Platform documentation to create a new secret for the new certificate. Then update the serving certificate reference for host name `api.<cluster_name>.<base_domain>` to the new secret in the `APIServer` custom resource. Otherwise, when the old and new certificates have different root CA certificates, complete the following steps to replace the certificate:

<div>

<div class="title">

Procedure

</div>

1.  Locate your `APIServer` custom resource, which resembles the following example:

    ``` yaml
    apiVersion: config.openshift.io/v1
    kind: APIServer
    metadata:
      name: cluster
    spec:
      audit:
        profile: Default
      servingCerts:
        namedCertificates:
        - names:
          - api.mycluster.example.com
          servingCertificate:
            name: old-cert-secret
    ```

2.  Create a new secret in the `openshift-config` namespace that contains the content of the existing and new certificates.

    1.  Copy the old certificate into a new certificate by running the following command:

        ``` bash
        cp old.crt combined.crt
        ```

    2.  Add the contents of the new certificate to the copy of the old certificate by running the following command:

        ``` bash
        cat new.crt >> combined.crt
        ```

    3.  Apply the combined certificates to create a secret by running the following command:

    ``` bash
    oc create secret tls combined-certs-secret --cert=combined.crt --key=old.key -n openshift-config
    ```

3.  Update your `APIServer` resource to reference the combined certificate as the `servingCertificate`. Your `APIServer` resource might resemble the following file:

    ``` yaml
    apiVersion: config.openshift.io/v1
    kind: APIServer
    metadata:
      name: cluster
    spec:
      audit:
        profile: Default
      servingCerts:
        namedCertificates:
        - names:
          - api.mycluster.example.com
          servingCertificate:
            name: combined-cert-secret
    ```

4.  After about 15 minutes, the CA bundle containing both new and old certificates is propagated to the managed clusters.

5.  Create another secret named `new-cert-secret` in the `openshift-config` namespace that contains only the new certificate information by entering the following command:

    ``` bash
    oc create secret tls new-cert-secret --cert=new.crt --key=new.key -n openshift-config {code}
    ```

6.  Update the `APIServer` resource by changing the name of `servingCertificate` to reference the `new-cert-secret`. Your resource might resemble the following example:

    ``` yaml
    apiVersion: config.openshift.io/v1
    kind: APIServer
    metadata:
      name: cluster
    spec:
      audit:
        profile: Default
      servingCerts:
        namedCertificates:
        - names:
          - api.mycluster.example.com
          servingCertificate:
            name: new-cert-secret
    ```

</div>

After about 15 minutes, the previous certificate is removed from the CA bundle, and the change is automatically propagated to the managed clusters.

**Note:** Managed clusters must use the host name `api.<cluster_name>.<base_domain>` to access the hub cluster. You cannot use named certificates that are configured with other host names.

<a id="config-proxy-hub-managed"></a>

### Configure the proxy between hub cluster and managed cluster

Configure the proxy settings to allow communications from the managed cluster to access the multicluster engine operator hub cluster through a HTTP or HTTPS proxy server when the managed cluster cannot reach the hub cluster directly.

To register a managed cluster to your multicluster engine for Kubernetes operator hub cluster, you need to transport the managed cluster to your multicluster engine operator hub cluster. Sometimes your managed cluster cannot directly reach your multicluster engine operator hub cluster.

For example, the multicluster engine operator hub cluster is in a public cloud, and the managed cluster is in a private cloud environment within a firewall-protected network. The communications out of the private cloud can only go through a HTTP or HTTPS proxy server.

<div>

<div class="title">

Prerequisites

</div>

- You have an active HTTP or HTTPS proxy server that supports HTTP tunnels. For example, HTTP connect method.

- You have a managed cluster that can reach the HTTP or HTTPS proxy server, and the proxy server can access the multicluster engine operator hub cluster.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create a `KlusterConfig` resource with either a HTTP or HTTPS proxy configuration.

    1.  Apply the following YAML sample to the resource to use a HTTP proxy configuration:

        ``` yaml
        apiVersion: config.open-cluster-management.io/v1alpha1
        kind: KlusterletConfig
        metadata:
          name: http-proxy
        spec:
          hubKubeAPIServerConfig:
            proxyURL: "http://<username>:<password>@<ip>:<port>"
        ```

    2.  A certificate authority (CA) bundle is required for HTTPS proxy. To create a `KlusterConfig` resource for HTTPS proxy where the required certificate authority bundle is defined, run the following command:

        ``` bash
        oc create -n <configmap-namespace> configmap <configmap-name> --from-file=ca.crt=/path/to/ca/file
        ```

        See the following configuration where the CA bundle refers to a config map that contains one or multiple CA certificates with HTTPS proxy:

    ``` yaml
    apiVersion: config.open-cluster-management.io/v1alpha1
    kind: KlusterletConfig
    metadata:
      name: https-proxy
    spec:
      hubKubeAPIServerConfig:
        proxyURL: "https://<username>:<password>@<ip>:<port>"
        trustedCABundles:
        - name: "proxy-ca-bundle"
          caBundle:
            name: <configmap-name>
            namespace: <configmap-namespace>
    ```

2.  When creating a managed cluster, choose the `KlusterletConfig` resource by adding an annotation that refers to the `KlusterletConfig` resource. See the following example:

    ``` yaml
    apiVersion: cluster.open-cluster-management.io/v1
    kind: ManagedCluster
    metadata:
      annotations:
        agent.open-cluster-management.io/klusterlet-config: <klusterlet-config-name>
      name:<managed-cluster-name>
    spec:
      hubAcceptsClient: true
      leaseDurationSeconds: 60
    ```

    **Notes:**

    - You might need to toggle the YAML view to add the annotation to the `ManagedCluster` resource when you operate on the multicluster engine operator console.

    - You can use a global `KlusterletConfig` to enable the configuration on every managed cluster without using an annotation for binding.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Disable the proxy between hub cluster and managed cluster](clusters.md#disable-proxy-hub-managed)

- [Configure proxy settings for cluster proxy add-ons](clusters.md#cluster-proxy-addon-settings)

</div>

<a id="disable-proxy-hub-managed"></a>

### Disable the proxy between hub cluster and managed cluster

Disable the HTTP or HTTPS proxy between the hub cluster and the managed cluster when you no longer need the proxy.

<div>

<div class="title">

Procedure

</div>

1.  Go to the `ManagedCluster` resource.

2.  Remove the `agent.open-cluster-management.io/klusterlet-config` annotation.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Configure the proxy between hub cluster and managed cluster](clusters.md#config-proxy-hub-managed)

</div>

<a id="access-managed-cluster-kube-apiserver"></a>

### Managed cluster `kube-apiserver` access

With cluster proxy add-ons, you can access the managed cluster `kube-apiserver` or managed cluster services from the hub cluster to gather resources, get logs, and view data in the console when a direct connection is not available.

You can authenticate and gather data by using one of the following methods:

- A managed cluster user token

- A hub cluster user token, when the hub cluster and managed cluster use the same external identity provider

- Managed cluster services, when the managed cluster is an Red Hat OpenShift Container Platform cluster and the service uses `services-serving-certificate` to generate server certificates

Before you use these methods, configure proxy settings for the cluster proxy add-on. See [Configure proxy settings for cluster proxy add-ons](clusters.md#cluster-proxy-addon-settings).

<div>

<div class="title">

Additional resources

</div>

- [Gather data with a managed cluster user token](clusters.md#gather-data-managed-token)

- [Gather data with a hub cluster user token](clusters.md#gather-data-hub-token)

- [Gather data with managed cluster services](clusters.md#gather-data-managed-cluster-services)

</div>

<a id="gather-data-managed-token"></a>

### Gather data with a managed cluster user token

Gather data with a managed cluster user token by listing pods in the default namespace of a managed cluster.

<div>

<div class="title">

Prerequisites

</div>

- You must [configure proxy settings for cluster proxy add-ons](clusters.md#cluster-proxy-addon-settings).

</div>

<div>

<div class="title">

Procedure

</div>

1.  Export your cluster proxy URL by running the following command. Replace values where needed:

    ``` bash
    export CLUSTER_PROXY_URL=https://$(oc get route -n multicluster-engine cluster-proxy-addon-user -o=jsonpath='{.spec.host}')/<managed-cluster-name>
    ```

2.  Get the `ConfigMap` by running the following command:

    ``` bash
    oc get configmap kube-root-ca.crt -o=jsonpath='{.data.ca\.crt}' > hub-ca.crt
    ```

3.  Transfer your certificate authority (CA) certificate by running the following command:

    ``` bash
    curl --cacert hub-ca.crt -H "Authorization: Bearer $TOKEN" https://$CLUSTER_PROXY_URL/api/v1/namespaces/default/pods
    ```

    **Note:** You need a user token that has permission to list pods in the default namespace of the managed cluster.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Managed cluster `kube-apiserver` access](clusters.md#access-managed-cluster-kube-apiserver)

- [Gather data with a hub cluster user token](clusters.md#gather-data-hub-token)

- [Gather data with managed cluster services](clusters.md#gather-data-managed-cluster-services)

</div>

<a id="gather-data-hub-token"></a>

### Gather data with a hub cluster user token

Gather data with a hub cluster user token when the target hub cluster and target managed cluster both use the same external identity provider so that both clusters can recognize the same user.

<div>

<div class="title">

Prerequisites

</div>

- You must [configure proxy settings for cluster proxy add-ons](clusters.md#cluster-proxy-addon-settings).

</div>

<div>

<div class="title">

Procedure

</div>

1.  To list pods in the default namespace by using the hub cluster `developer` user token, you must first create the correct `Role` and `RoleBinding` for the `developer` on the managed cluster.

    If you are using Red Hat Advanced Cluster Management for Kubernetes, you can use the `ClusterPermission` API to create `Role` and `RoleBinding` objects from the hub cluster.

2.  Create a `ClusterPermission` that binds the `get` and `list` permissions for pods to the user `developer`. See the following example:

    ``` yaml
    apiVersion: rbac.open-cluster-management.io/v1alpha1
    kind: ClusterPermission
    metadata:
      name: <name>
      namespace: <cluster-namespace>
    spec:
      roles:
      - namespace: default
        rules:
        - apiGroups: [""]
          resources: ["pods"]
          verbs: ["get","list"]
      roleBindings:
      - namespace: default
        roleRef:
          kind: Role
        subject:
          apiGroup: rbac.authorization.k8s.io
          kind: User
          name: developer
    ```

</div>

<div>

<div class="title">

Additional resources

</div>

- [Managed cluster `kube-apiserver` access](clusters.md#access-managed-cluster-kube-apiserver)

- [Gather data with a managed cluster user token](clusters.md#gather-data-managed-token)

- [Gather data with managed cluster services](clusters.md#gather-data-managed-cluster-services)

</div>

<a id="gather-data-managed-cluster-services"></a>

### Gather data with managed cluster services

Gather data by accessing managed cluster services when the managed cluster is an Red Hat OpenShift Container Platform cluster and the service uses the `services-serving-certificate` service to generate server certificates.

<div>

<div class="title">

Prerequisites

</div>

- You must [configure proxy settings for cluster proxy add-ons](clusters.md#cluster-proxy-addon-settings).

</div>

<div>

<div class="title">

Procedure

</div>

1.  Get the Prometheus service token from the managed cluster. Run the following command:

    ``` bash
    export PROMETHEUS_TOKEN=$(kubectl get secret -n openshift-monitoring $(kubectl get serviceaccount -n openshift-monitoring prometheus-k8s -o=jsonpath='{.secrets[0].name}') -o=jsonpath='{.data.token}' | base64 -d)
    ```

2.  Get the Prometheus managed cluster metrics from the hub cluster. Run the following commands:

    ``` bash
    export SERVICE_NAMESPACE=openshift-monitoring
    export SERVICE_NAME=prometheus-k8s
    export SERVICE_PORT=9091
    export SERVICE_PATH="api/v1/query?query=machine_cpu_sockets"
    curl --cacert hub-ca.crt $CLUSTER_PROXY_URL/api/v1/namespaces/$SERVICE_NAMESPACE/services/$SERVICE_NAME:$SERVICE_PORT/proxy-service/$SERVICE_PATH -H "Authorization: Bearer $PROMETHEUS_TOKEN"
    ```

</div>

<div>

<div class="title">

Additional resources

</div>

- [Managed cluster `kube-apiserver` access](clusters.md#access-managed-cluster-kube-apiserver)

- [Gather data with a managed cluster user token](clusters.md#gather-data-managed-token)

- [Gather data with a hub cluster user token](clusters.md#gather-data-hub-token)

</div>

<a id="ansible-intro"></a>

## Ansible Automation Platform for cluster management

multicluster engine operator is integrated with Red Hat Ansible Automation Platform so that you can create prehook and posthook Ansible job instances that run before or after you create or upgrade clusters. You can automate managed cluster and hosted cluster lifecycle actions with Automation templates and the `ClusterCurator` resource.

Configuring prehook and posthook jobs for cluster destroy and cluster scale actions on managed clusters is not supported.

**Required access:** Cluster administrator

<div>

<div class="title">

Additional resources

</div>

- [Configure an Automation template on a cluster by using the console](clusters.md#ansible-template-run-cluster-console)

- [Create an Automation template](clusters.md#ansible-template-create)

- [Link an Ansible credential to an Automation template](clusters.md#ansible-template-link-credential)

- [View the status of an Ansible job](clusters.md#ansible-status-job-cluster)

- [Run a failed Ansible job again](clusters.md#ansible-rerun-job-cluster)

- [Specify an Ansible inventory for all jobs](clusters.md#specify-ansible-inventory)

- [Push custom labels from *ClusterCurator* to automation job pod](clusters.md#push-cl-cr-job-pod)

- [Use *ClusterCurator* to automate EUS updates](clusters.md#eus-updates)

- [Update OpenShift Container Platform clusters to versions with known issues](clusters.md#update-ocp-cluster-curator)

- [Create an Ansible job for a managed cluster](clusters.md#create-ansible-job-managed-cluster)

- [Run an Ansible Automation Platform job to install a hosted cluster](clusters.md#ansible-hosted-cluster-install)

- [Run an Ansible Automation Platform job to update a hosted cluster](clusters.md#ansible-hosted-cluster-update)

- [Run an Ansible Automation Platform job to delete a hosted cluster](clusters.md#ansible-hosted-cluster-delete)

- [Creating a credential for Ansible Automation Platform](clusters.md#creating-a-credential-for-ansible)

- [Installing the hosted control planes command-line interface](https://docs.redhat.com/en/documentation/openshift_container_platform/4.20/html/hosted_control_planes/preparing-to-deploy-hosted-control-planes#installing-the-hosted-control-plane-command-line-interface)

- [Introduction to hosted control planes](https://docs.redhat.com/en/documentation/openshift_container_platform/4.20/html/hosted_control_planes/hosted-control-planes-overview#hosted-control-planes-overview_hcp-overview)

</div>

<a id="ansible-template-run-cluster-console"></a>

### Configure an Automation template on a cluster by using the console

You can specify the Automation template for a cluster when you create the cluster, when you import the cluster, or after you create the cluster.

**Required access:** Cluster administrator

<div>

<div class="title">

Prerequisites

</div>

- Install OpenShift Container Platform.

- Install the Ansible Automation Platform Resource Operator to connect Ansible jobs to the lifecycle of Git subscriptions. For best results when using the Automation template to launch Ansible Automation Platform jobs, the Ansible Automation Platform job template should be idempotent when it is run. You can find the Ansible Automation Platform Resource Operator in the Red Hat OpenShift Software Catalog.

- When installing the Ansible Automation Platform Resource Operator, you must select the `*-cluster-scoped` channel and select the *all namespaces* installation mode.

</div>

<div>

<div class="title">

Procedure

</div>

1.  To specify the template when you create or import a cluster, select the Ansible template that you want to apply to the cluster in the *Automation* step. If there are no Automation templates, click **Add automation template** to create one.

2.  To specify the template after you create a cluster, click **Update automation template** in the action menu of an existing cluster. You can also use the **Update automation template** option to update an existing automation template.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Create an Automation template](clusters.md#ansible-template-create)

</div>

<a id="ansible-template-create"></a>

### Create an Automation template

Create an Automation template to specify when Ansible jobs run before or after a cluster installs or upgrades.

**Required access:** Cluster administrator

<div>

<div class="title">

Prerequisites

</div>

- Install OpenShift Container Platform.

- Install the Ansible Automation Platform Resource Operator to connect Ansible jobs to the lifecycle of Git subscriptions. For best results when using the Automation template to launch Ansible Automation Platform jobs, the Ansible Automation Platform job template should be idempotent when it is run. You can find the Ansible Automation Platform Resource Operator in the Red Hat OpenShift Software Catalog.

- When installing the Ansible Automation Platform Resource Operator, you must select the `\*-cluster-scoped` channel and select the *all namespaces* installation mode.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Select **Infrastructure** \> **Automation** from the navigation.

2.  Select the applicable path for your situation:

    - If you want to create a new template, click **Create Ansible template** and continue with step 3.

    - If you want to modify an existing template, click **Edit template** from the *Options* menu of the template that you want to modify and continue with step 5.

3.  Enter a unique name for your template that contains lowercase alphanumeric characters or a hyphen (-).

4.  Select the credential that you want to use for the new template.

5.  After you select a credential, select an Ansible inventory to use for all the jobs.

6.  If you want to initiate any Ansible jobs before the cluster is installed, select **Add an Automation template** in the *Pre-install Automation templates* section.

7.  Select between a `Job template` or a `Workflow job template` in the modal that appears. You can also add `job_tags`, `skip_tags`, and workflow types.

    - Use the **Extra variables** field to pass data to the `AnsibleJob` resource in the form of `key=value` pairs.

    - Special keys `cluster_deployment` and `install_config` are passed automatically as extra variables. They contain general information about the cluster and details about the cluster installation configuration.

8.  Select the name of the prehook and posthook Ansible jobs to add to the installation or upgrade of the cluster.

9.  Drag the Ansible jobs to change the order, if necessary.

10. Repeat steps 6-8 for any Automation templates that you want to initiate after the cluster is installed in the *Post-install Automation templates* section, the *Pre-upgrade Automation templates* section, and the *Post-upgrade Automation templates* section.

11. Use the **Extra variables** field to pass data to the `AnsibleJob` resource when you upgrade a cluster. Enter the values in the form of `key=value` pairs.

    **Note:** In addition to the `cluster_deployment` and `install_config` special keys, the `cluster_info` special key is also passed automatically as an extra variable that contains data from the `ManagedClusterInfo` resource.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Link an Ansible credential to an Automation template](clusters.md#ansible-template-link-credential)

</div>

<a id="ansible-template-link-credential"></a>

### Link an Ansible credential to an Automation template

Link an Ansible credential to an Automation template that is not yet linked to a credential.

**Required access:** Cluster administrator

<div>

<div class="title">

Procedure

</div>

1.  From the navigation, select **Automation**. Any template in the list of templates that is not linked to a credential contains a **Link to credential** icon that you can use to link the template to an existing credential. Only the credentials in the same namespace as the template are displayed.

2.  If there are no credentials that you can select, or if you do not want to use an existing credential, select **Edit template** from the *Options* menu for the template that you want to link.

3.  Click **Add credential** and complete the procedure in [Creating a credential for Ansible Automation Platform](clusters.md#creating-a-credential-for-ansible) if you have to create your credential.

4.  After you create your credential in the same namespace as the template, select the credential in the *Ansible Automation Platform credential* field when you edit the template.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Create an Automation template](clusters.md#ansible-template-create)

- [Creating a credential for Ansible Automation Platform](clusters.md#creating-a-credential-for-ansible)

</div>

<a id="ansible-status-job-cluster"></a>

### View the status of an Ansible job

View the status of a running Ansible job to verify that it started and is running successfully.

**Required access:** Cluster administrator

<div>

<div class="title">

Procedure

</div>

1.  In the menu, select **Infrastructure** \> **Clusters** to access the *Clusters* page.

2.  Select the name of the cluster to view its details.

3.  View the status of the last run of the Ansible job on the cluster information. The entry shows one of the following statuses:

    - When an install prehook or posthook job fails, the cluster status shows `Failed`.

    - When an upgrade prehook or posthook job fails, a warning is displayed in the *Distribution* field that the upgrade failed.

</div>

<a id="ansible-rerun-job-cluster"></a>

### Run a failed Ansible job again

Retry a failed cluster upgrade from the *Clusters* page, or rerun only the failed Ansible posthooks that are part of cluster automation templates. After you add the content, a new job is created to run the Ansible posthook.

**Required access:** Cluster administrator

You can retry an upgrade from the *Clusters* page if the cluster prehook or posthook failed.

To save time, you can also run only the failed Ansible posthooks that are part of cluster automation templates. Complete the following steps to run only the posthooks again, without retrying the entire upgrade:

<div>

<div class="title">

Procedure

</div>

1.  Add the following content to the root of the `ClusterCurator` resource to run the install posthook again:

    ``` yaml
    operation:
      retryPosthook: installPosthook
    ```

2.  Add the following content to the root of the `ClusterCurator` resource to run the upgrade posthook again:

    ``` yaml
    operation:
      retryPosthook: upgradePosthook
    ```

</div>

<a id="specify-ansible-inventory"></a>

### Specify an Ansible inventory for all jobs

Use the `ClusterCurator` resource to specify an Ansible inventory for all jobs.

**Required access:** Cluster administrator

<div>

<div class="title">

Procedure

</div>

- Create or edit a `ClusterCurator` resource and set the `inventory` field. Replace `channel` and `desiredUpdate` with the correct values for your `ClusterCurator`. See the following example:

  ``` yaml
  apiVersion: cluster.open-cluster-management.io/v1beta1
  kind: ClusterCurator
  metadata:
    name: test-inno
    namespace: test-inno
  spec:
    desiredCuration: upgrade
    destroy: {}
    install: {}
    scale: {}
    upgrade:
      channel: stable-4.x
      desiredUpdate: 4.x.1
      monitorTimeout: 150
      posthook:
      - extra_vars: {}
        clusterName: test-inno
        type: post_check
        name: ACM Upgrade Checks
      prehook:
      - extra_vars: {}
        clusterName: test-inno
        type: pre_check
        name: ACM Upgrade Checks
      towerAuthSecret: awx
      inventory: Demo Inventory
  ```

  **Note:** To use the example resource, the inventory must already exist in Ansible.

  1.  Verify that the inventory is created by checking the list of available Ansible inventories from the console.

</div>

<a id="push-cl-cr-job-pod"></a>

### Push custom labels from *ClusterCurator* to automation job pod

Use the `ClusterCurator` resource to push custom labels to the automation job pod that the Cluster Curator creates. You can push the custom labels on all curation types.

**Required access:** Cluster administrator

<div>

<div class="title">

Procedure

</div>

1.  Create or edit a `ClusterCurator` resource and add the labels that you want to push. See the following example:

    ``` yaml
    apiVersion: cluster.open-cluster-management.io/v1beta1
    kind: ClusterCurator
    metadata:
      name: cluster1
      namespace: cluster1
      labels:
        test1: test1
        test2: test2
    spec:
      desiredCuration: install
      install:
        jobMonitorTimeout: 5
        posthook:
          - extra_vars: {}
            name: Demo Job Template
            type: Job
        prehook:
          - extra_vars: {}
            name: Demo Job Template
            type: Job
        towerAuthSecret: toweraccess
    ```

</div>

<a id="eus-updates"></a>

### Use *ClusterCurator* to automate EUS updates

Use the `ClusterCurator` resource to perform an automatic upgrade between Extended Update Support releases.

**Required access:** Cluster administrator

<div>

<div class="title">

Procedure

</div>

1.  Add `spec.upgrade.intermediateUpdate` to the `ClusterCurator` resource with the intermediate release value. See the following sample, where the intermediate release is `4.17.x`, and the `desiredUpdate` is `4.18.x`:

    ``` yaml
    spec:
      desiredCuration: upgrade
      upgrade:
        intermediateUpdate: 4.17.x
        desiredUpdate: 4.18.x
        monitorTimeout: 120
    ```

2.  **Optional:** You can pause the `machineconfigpools` to skip the intermediate release for a faster upgrade. Enter `Unpause machinepool` in the `posthook` job, and `Pause machinepool` in the `prehook` job. See the following example:

    ``` yaml
        posthook:
          - extra_vars: {}
            name: Unpause machinepool
            type: Job
        prehook:
          - extra_vars: {}
            name: Pause machinepool
            type: Job
    ```

    See the following full example of the `ClusterCurator` that is configured to upgrade EUS to EUS:

</div>

``` yaml
apiVersion: cluster.open-cluster-management.io/v1beta1
kind: ClusterCurator
metadata:
  annotations:
    cluster.open-cluster-management.io/upgrade-clusterversion-backoff-limit: "10"
  name: your-name
  namespace: your-namespace
spec:
  desiredCuration: upgrade
  upgrade:
    intermediateUpdate: 4.17.x
    desiredUpdate: 4.18.x
    monitorTimeout: 120
    posthook:
      - extra_vars: {}
        name: Unpause machinepool
        type: Job
    prehook:
      - extra_vars: {}
        name: Pause machinepool
        type: Job
```

<a id="update-ocp-cluster-curator"></a>

### Update OpenShift Container Platform clusters to versions with known issues

Update your OpenShift Container Platform cluster to a version with known issues when you need to test new features quickly. The `ClusterCurator` checks the `desiredUpdate` image digest version at startup in the conditional updates list. If the image digest is not found, the `ClusterCurator` uses the image tag instead.

**Required access:** Cluster administrator

**Important:** Upgrading to an OpenShift Container Platform cluster version with known issues can reduce performance and compatibility.

<div>

<div class="title">

Procedure

</div>

1.  Create a file named `clustercurator.yaml`.

2.  Add your cluster `name`, `namespace`, and OpenShift Container Platform cluster version with known issues that you want to upgrade to. View the following example file:

    ``` yaml
    apiVersion: cluster.open-cluster-management.io/v1beta1
    kind: ClusterCurator
    metadata:
      annotations:
        cluster.open-cluster-management.io/upgrade-allow-not-recommended-versions: 'true'
      name: <name>
      namespace: <namespace>
    spec:
      desiredCuration: upgrade
      upgrade:
        desiredUpdate: <4.x.x>
        monitorTimeout: 120
    ```

3.  Apply the file. Run the following command:

    ``` bash
    oc apply -f clustercurator.yaml
    ```

</div>

<a id="create-ansible-job-managed-cluster"></a>

### Create an Ansible job for a managed cluster

Create an `AnsibleJob` that is bound to a cluster when the cluster is created or imported to be managed. Complete the following procedure to create an Ansible job and configure it with a cluster that is not yet managed.

**Required access:** Cluster administrator

<div>

<div class="title">

Procedure

</div>

1.  Create the definition file for the Ansible job in one of the channels that are supported by the application function. Only Git channels are supported.

    Use `AnsibleJob` as the value of `kind` in the definition. Your definition file contents might resemble the following example:

    ``` yaml
    apiVersion: tower.ansible.com/v1alpha1
    kind: AnsibleJob
    metadata:
      name: hive-cluster-gitrepo
    spec:
      tower_auth_secret: my-toweraccess
      job_template_name: my-tower-template-name
      extra_vars:
        variable1: value1
        variable2: value2
    ```

    **Note:** By storing the file in the prehook or posthook directory, it creates a list of cluster names that match the placement rule. The list of cluster names can be passed as a value of `extra_vars` to the `AnsibleJob` `kind` resource. When this value is passed to the `AnsibleJob` resource, the Ansible job can determine the new cluster name and use it in the automation.

2.  Log on to your hub cluster.

3.  Create an application with a Git subscription that references the channel where you stored the definition file that you just created.

    **Notes:**

    - When you create the subscription, specify a label that you can add to the cluster that you create or import later to connect this subscription with the cluster. This can be an existing label, such as `vendor=OpenShift`, or a unique label that you create and define.

    - If you select any label that is already in use, the Ansible job automatically runs. Include a resource in your application that is not part of the prehooks or posthooks.

      The default placement rule runs the job when it detects the cluster with the label that matches the label of the `AnsibleJob`.

4.  Add the following content to the placement rule if you want the automation to run on all of your running clusters that are managed by the hub cluster:

    ``` yaml
    clusterConditions:
      - type: ManagedClusterConditionAvailable
        status: "True"
    ```

5.  Alternatively, select **Deploy to all online clusters and local cluster** on the *Application create* page of the console.

6.  Create or import your cluster. When you create or import the cluster, use the same label that you used when you created the subscription, and the `AnsibleJob` is automatically configured to run on the cluster.

    **Note:** The multicluster engine operator automatically injects the cluster name into the `AnsibleJob.extra_vars.target_clusters` path.

7.  Dynamically inject the cluster name into the definition. Complete the following procedure to create an Ansible job and configure it with a cluster that is already managed:

    1.  Create the definition file for the Ansible job in the prehook or posthook directory of your Git Channel.

        Use `AnsibleJob` as the value of `kind` in the definition. Your definition file contents might resemble the following example:

    ``` yaml
    apiVersion: tower.ansible.com/v1alpha1
    kind: AnsibleJob
    metadata:
      name: hive-cluster-gitrepo
    spec:
      tower_auth_secret: my-toweraccess
      job_template_name: my-tower-template-name
      extra_vars:
        variable1: value1
        variable2: value2
    ```

8.  Replace `my-toweraccess` with the authentication secret to access your Ansible Automation Platform.

9.  Replace `my-tower-template-name` with the template name from your Ansible Automation Platform.

    **Note:** Each time a cluster that is controlled by the Ansible job is removed or added, the Ansible job automatically runs and updates the `extra_vars.target_clusters` variable. This updating provides the ability to specify cluster names with a specific automation, or apply the automation to a group of clusters.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Manage application resources](applications.md#managing-application-resources)

- [Creating clusters](clusters.md#create-intro)

- [Cluster import](clusters.md#import-intro)

</div>

<a id="ansible-hosted-cluster-install"></a>

### Run an Ansible Automation Platform job to install a hosted cluster

Start an Ansible Automation Platform job that installs a hosted cluster by creating paused `HostedCluster` and `NodePool` resources and a matching `ClusterCurator` resource.

**Required access:** Cluster administrator

<div>

<div class="title">

Prerequisites

</div>

- A supported version of OpenShift Container Platform

- Install the Ansible Automation Platform Resource Operator to connect Ansible Automation Platform jobs to the lifecycle of Git subscriptions. When you use the Automation template to start Ansible Automation Platform jobs, ensure that the Ansible Automation Platform job template is idempotent when it is run. You can find the Ansible Automation Platform Resource Operator in the Red Hat OpenShift Software Catalog.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create the `HostedCluster` and `NodePool` resources, including the `pausedUntil: true` field. If you use the `hcp create cluster` command line interface command, you can specify the `--pausedUntil: true` flag. See the following examples:

    ``` yaml
    apiVersion: hypershift.openshift.io/v1beta1
    kind: HostedCluster
    metadata:
      name: my-cluster
      namespace: clusters
    spec:
      pausedUntil: 'true'
    ```

    <!-- Separate adjacent source examples. -->

    ``` yaml
    apiVersion: hypershift.openshift.io/v1beta1
    kind: NodePool
    metadata:
      name: my-cluster-us-east-2
      namespace: clusters
    spec:
      pausedUntil: 'true'
    ```

2.  Create a `ClusterCurator` resource with the same name as the `HostedCluster` resource and in the same namespace as the `HostedCluster` resource. See the following example:

    ``` yaml
    apiVersion: cluster.open-cluster-management.io/v1beta1
    kind: ClusterCurator
    metadata:
      name: my-cluster
      namespace: clusters
      labels:
        open-cluster-management: curator
    spec:
      desiredCuration: install
      install:
        jobMonitorTimeout: 5
        prehook:
          - name: Demo Job Template
            extra_vars:
              variable1: something-interesting
              variable2: 2
          - name: Demo Job Template
        posthook:
          - name: Demo Job Template
        towerAuthSecret: toweraccess
    ```

3.  If your Ansible Automation Platform Tower requires authentication, create a secret resource. See the following example:

    ``` yaml
    apiVersion: v1
    kind: Secret
    metadata:
      name: toweraccess
      namespace: clusters
    stringData:
      host: https://my-tower-domain.io
      token: ANSIBLE_TOKEN_FOR_admin
    ```

</div>

<a id="ansible-hosted-cluster-update"></a>

### Run an Ansible Automation Platform job to update a hosted cluster

Run an Ansible Automation Platform job that updates a hosted cluster by editing the `ClusterCurator` resource of the hosted cluster that you want to update.

**Required access:** Cluster administrator

<div>

<div class="title">

Procedure

</div>

1.  Edit the `ClusterCurator` resource of the hosted cluster that you want to update. See the following example:

    ``` yaml
    apiVersion: cluster.open-cluster-management.io/v1beta1
    kind: ClusterCurator
    metadata:
      name: my-cluster
      namespace: clusters
      labels:
        open-cluster-management: curator
    spec:
      desiredCuration: upgrade
      upgrade:
        desiredUpdate: 4.17.1
        monitorTimeout: 120
        prehook:
          - name: Demo Job Template
            extra_vars:
              variable1: something-interesting
              variable2: 2
          - name: Demo Job Template
        posthook:
          - name: Demo Job Template
        towerAuthSecret: toweraccess
    ```

</div>

<div>

<div class="title">

Additional resources

</div>

- [Run an Ansible Automation Platform job to update the control plane and specific node pools](clusters.md#ansible-hosted-update-control-plane-nodepools)

- [Run an Ansible Automation Platform job to update the control plane](clusters.md#ansible-hosted-update-control-plane)

- [Run an Ansible Automation Platform job to update the node pools](clusters.md#ansible-hosted-update-nodepools)

- [Run an Ansible Automation Platform job to update specific node pools](clusters.md#ansible-hosted-update-specific-nodepools)

- [Run an Ansible Automation Platform job to update the cluster channel](clusters.md#ansible-hosted-update-channel)

- [Run an Ansible Automation Platform job to update cluster version and channel](clusters.md#ansible-hosted-update-version-channel)

</div>

<a id="ansible-hosted-update-control-plane-nodepools"></a>

### Run an Ansible Automation Platform job to update the control plane and specific node pools

Update the control plane and specific node pools by editing the `nodePoolNames` field in your `ClusterCurator` resource.

**Required access:** Cluster administrator

<div>

<div class="title">

Procedure

</div>

- Edit the `ClusterCurator` resource of the hosted cluster that you want to update. See the following example:

  ``` yaml
  apiVersion: cluster.open-cluster-management.io/v1beta1
  kind: ClusterCurator
  metadata:
    name: my-hosted-cluster
    namespace: clusters
  spec:
    desiredCuration: upgrade
    upgrade:
      desiredUpdate: "4.17.1"
      nodePoolNames:
        - my-nodepool-1
        - my-nodepool-2
  ```

</div>

<a id="ansible-hosted-update-control-plane"></a>

### Run an Ansible Automation Platform job to update the control plane

Update the control plane by setting the `upgradeType` field to `ControlPlane` in your `ClusterCurator` resource.

**Required access:** Cluster administrator

<div>

<div class="title">

Procedure

</div>

- Edit the `ClusterCurator` resource of the hosted cluster that you want to update. See the following example:

  ``` yaml
  apiVersion: cluster.open-cluster-management.io/v1beta1
  kind: ClusterCurator
  metadata:
    name: my-hosted-cluster
    namespace: clusters
  spec:
    desiredCuration: upgrade
    upgrade:
      desiredUpdate: "4.17.1"
      upgradeType: ControlPlane
  ```

</div>

<a id="ansible-hosted-update-nodepools"></a>

### Run an Ansible Automation Platform job to update the node pools

Update all node pools associated with your hosted cluster by setting the `upgradeType` field to `NodePools` in your `ClusterCurator` resource.

**Required access:** Cluster administrator

<div>

<div class="title">

Procedure

</div>

- Edit the `ClusterCurator` resource of the hosted cluster that you want to update. See the following example:

  ``` yaml
  apiVersion: cluster.open-cluster-management.io/v1beta1
  kind: ClusterCurator
  metadata:
    name: my-hosted-cluster
    namespace: clusters
  spec:
    desiredCuration: upgrade
    upgrade:
      desiredUpdate: "4.17.1"
      upgradeType: NodePools
  ```

</div>

<a id="ansible-hosted-update-specific-nodepools"></a>

### Run an Ansible Automation Platform job to update specific node pools

Update only specific node pools by setting the `upgradeType` field to `NodePools` and listing the node pools in the `nodePoolNames` field.

**Required access:** Cluster administrator

<div>

<div class="title">

Procedure

</div>

- Edit the `ClusterCurator` resource of the hosted cluster that you want to update. See the following example:

  ``` yaml
  apiVersion: cluster.open-cluster-management.io/v1beta1
  kind: ClusterCurator
  metadata:
    name: my-hosted-cluster
    namespace: clusters
  spec:
    desiredCuration: upgrade
    upgrade:
      desiredUpdate: "4.17.1"
      upgradeType: NodePools
      nodePoolNames:
        - my-nodepool-1
        - my-nodepool-2
  ```

</div>

<a id="ansible-hosted-update-channel"></a>

### Run an Ansible Automation Platform job to update the cluster channel

Update the cluster channel without changing the version by adding the cluster channel to the `channel` field.

**Required access:** Cluster administrator

<div>

<div class="title">

Procedure

</div>

- Edit the `ClusterCurator` resource of the hosted cluster that you want to update. See the following example:

  ``` yaml
  apiVersion: cluster.open-cluster-management.io/v1beta1
  kind: ClusterCurator
  metadata:
    name: my-hosted-cluster
    namespace: clusters
  spec:
    desiredCuration: upgrade
    upgrade:
      channel: "fast-4.17"
  ```

</div>

<a id="ansible-hosted-update-version-channel"></a>

### Run an Ansible Automation Platform job to update cluster version and channel

Update the cluster version and channel by setting the `desiredUpdate` and `channel` fields in your `ClusterCurator` resource.

**Required access:** Cluster administrator

<div>

<div class="title">

Procedure

</div>

- Edit the `ClusterCurator` resource of the hosted cluster that you want to update. See the following example:

  ``` yaml
  apiVersion: cluster.open-cluster-management.io/v1beta1
  kind: ClusterCurator
  metadata:
    name: my-hosted-cluster
    namespace: clusters
  spec:
    desiredCuration: upgrade
    upgrade:
      desiredUpdate: "4.17.1"
      channel: "fast-4.17"
  ```

</div>

<a id="ansible-hosted-cluster-delete"></a>

### Run an Ansible Automation Platform job to delete a hosted cluster

Run an Ansible Automation Platform job that deletes a hosted cluster by editing the `ClusterCurator` resource of the hosted cluster that you want to delete.

**Required access:** Cluster administrator

<div>

<div class="title">

Procedure

</div>

- Edit the `ClusterCurator` resource of the hosted cluster that you want to delete. **Note:** Deleting a hosted cluster on AWS is not supported. See the following example:

  ``` yaml
  apiVersion: cluster.open-cluster-management.io/v1beta1
  kind: ClusterCurator
  metadata:
    name: my-cluster
    namespace: clusters
    labels:
      open-cluster-management: curator
  spec:
    desiredCuration: destroy
    destroy:
      jobMonitorTimeout: 5
      prehook:
        - name: Demo Job Template
          extra_vars:
            variable1: something-interesting
            variable2: 2
        - name: Demo Job Template
      posthook:
        - name: Demo Job Template
      towerAuthSecret: toweraccess
  ```

</div>

<a id="clusterclaims"></a>

## ClusterClaims

A `ClusterClaim` is a cluster-scoped custom resource definition (CRD) on a managed cluster. A `ClusterClaim` represents a piece of information that a managed cluster claims. You can use the `ClusterClaim` to determine the Placement of the resource on the target clusters.

The following example shows a `ClusterClaim` that is identified in the YAML file:

``` yaml
apiVersion: cluster.open-cluster-management.io/v1alpha1
kind: ClusterClaim
metadata:
  name: id.openshift.io
spec:
  value: 95f91f25-d7a2-4fc3-9237-2ef633d8451c
```

The following table shows the defined `ClusterClaim` list for a cluster that multicluster engine operator manages:

| Claim name | Reserved | Mutable | Description |
|----|----|----|----|
| `id.k8s.io` | true | false | ClusterID defined in upstream proposal |
| `kubeversion.open-cluster-management.io` | true | true | Kubernetes version |
| `platform.open-cluster-management.io` | true | false | Platform the managed cluster is running on, such as AWS, GCE, and Equinix Metal |
| `product.open-cluster-management.io` | true | false | Product name, such as OpenShift, Anthos, EKS and GKE |
| `id.openshift.io` | false | false | OpenShift Container Platform external ID, which is only available for an OpenShift Container Platform cluster |
| `consoleurl.openshift.io` | false | true | URL of the management console, which is only available for an OpenShift Container Platform cluster |
| `version.openshift.io` | false | true | OpenShift Container Platform version, which is only available for an OpenShift Container Platform cluster |

If any of the previous claims are deleted or updated on managed cluster, they are restored or rolled back to a previous version automatically.

After the managed cluster joins the hub cluster, the following two types of `ClusterClaim` resources that are created on the managed cluster are synchronized with the status of the `ManagedCluster` resource on the hub cluster. `ClusterClaim` resources with the `open-cluster-management.io/spoke-only` label are not synchronized.

`ClusterClaim` resources that multicluster engine operator manages  
Includes `id.k8s.io`, or labels with the `open-cluster-management.io` or `openshift.io` suffix. These `ClusterClaim` resources are synchronized to the `ManagedCluster` status on the hub cluster.

`ClusterClaim` resources that you manage  
Without the `open-cluster-management.io` or `openshift.io` suffix. By default, up to 20 `ClusterClaim` resources are synchronized to the `ManagedCluster` status on the hub cluster. Configure the `KlusterletConfig` API to change the number of `ClusterClaim` resources you manage that are synchronized. Complete the following steps:

If you are managing `ClusterClaim` resources, configure the `KlusterletConfig` API to change the number of `ClusterClaim` resources that are synchronized. Complete the following steps:

1.  Create a `KlusterletConfig` and set `clusterClaimConfiguration.maxCustomClusterClaims` to your desired value. The maxmimum value is `100`. See the following example:

    ``` yaml
    kind: KlusterletConfig
    apiVersion: config.open-cluster-management.io/v1alpha1
    metadata:
      name: klusterlet-cluster-claim-config
    spec:
      clusterClaimConfiguration:
        maxCustomClusterClaims: 30
    ```

2.  Add an annotation to refer to the `KlusterletConfig` in the `ManagedCluster` resource. Run the following command:

    ``` bash
    oc annotate managedcluster <cluster-name> agent.open-cluster-management.io/klusterlet-config="klusterlet-cluster-claim-config"
    ```

    After adding the annotation, yor `ManagedCluster` resource resembles the following example:

    ``` yaml
    apiVersion: cluster.open-cluster-management.io/v1
    kind: ManagedCluster
    metadata:
      annotations:
       agent.open-cluster-management.io/klusterlet-config: klusterlet-cluster-claim-config
      name: cluster1
    spec:
      hubAcceptsClient: true
      leaseDurationSeconds: 60
    ```

<a id="create-custom-clusterclaims"></a>

### Create custom ClusterClaims

You can create a `ClusterClaim` resource with a custom name on a managed cluster, which makes it easier to identify. The custom `ClusterClaim` resource is synchronized with the status of the `ManagedCluster` resource on the hub cluster. The following content shows an example of a definition for a customized `ClusterClaim` resource:

``` yaml
apiVersion: cluster.open-cluster-management.io/v1alpha1
kind: ClusterClaim
metadata:
  name: <custom_claim_name>
spec:
  value: <custom_claim_value>
```

The length of `spec.value` field must be 1024 or less. The `create` permission on resource `clusterclaims.cluster.open-cluster-management.io` is required to create a `ClusterClaim` resource.

<a id="list-clusterclaims"></a>

## List existing ClusterClaims

You can use the `kubectl` command to list the ClusterClaims that apply to your managed cluster so that you can compare your ClusterClaim to an error message.

**Note:** Make sure you have `list` permission on resource `clusterclaims.cluster.open-cluster-management.io`.

Run the following command to list all existing ClusterClaims that are on the managed cluster:

    kubectl get clusterclaims.cluster.open-cluster-management.io

<a id="managedclustersets-intro"></a>

## *ManagedClusterSets*

A `ManagedClusterSet` is a group of managed clusters. A managed cluster set, can help you manage access to all of your managed clusters. You can also create a `ManagedClusterSetBinding` resource to bind a `ManagedClusterSet` resource to a namespace.

Each cluster must be a member of a managed cluster set. When you install the hub cluster, a `ManagedClusterSet` resource is created called `default`. All clusters that are not assigned to a managed cluster set are automatically assigned to the `default` managed cluster set. You cannot delete or update the `default` managed cluster set.

Continue reading to learn more about how to create and manage managed cluster sets:

- [*ManagedClusterSet* overview](clusters.md#creating-a-managedclusterset)

- [Create a *ManagedClusterSet* by using the command line](clusters.md#creating-managedclusterset-cli)

- [Add clusters to a *ManagedClusterSet* by using the command line](clusters.md#adding-clusters-managedclusterset-cli)

- [Assign RBAC permissions to a *ManagedClusterSet*](clusters.md#assign-role-managedclusterset)

- [*ManagedClusterSet* API RBAC permission levels](clusters.md#managedclusterset-api-rbac-permission-levels)

- [*ManagedClusterSetBinding* resource overview](clusters.md#creating-managedclustersetbinding)

- [Create a *ManagedClusterSetBinding* by using the console](clusters.md#creating-managedclustersetbinding-console)

- [Create a *ManagedClusterSetBinding* by using the command line](clusters.md#creating-a-managedclustersetbinding-cli)

- [Remove a cluster from a *ManagedClusterSet* by using the console](clusters.md#removing-cluster-managedclusterset-console)

- [Remove a cluster from a *ManagedClusterSet* by using the command line](clusters.md#removing-cluster-managedclusterset-cli)

<a id="creating-a-managedclusterset"></a>

### *ManagedClusterSet* overview

A `ManagedClusterSet` is a cluster-scoped resource, so you must have cluster administration permissions for the cluster where you are creating the `ManagedClusterSet`. A managed cluster cannot be included in more than one `ManagedClusterSet`. You can create a managed cluster set from either the multicluster engine operator console or from the CLI.

**Note:** Cluster pools that are not added to a managed cluster set are not added to the default `ManagedClusterSet` resource. After a cluster is claimed from the cluster pool, the cluster is added to the default `ManagedClusterSet`.

After installing multicluster engine operator, the following resources are automatically created on the hub cluster to ease management:

- A `ManagedClusterSet` called `global`.

- The namespace called `open-cluster-management-global-set`.

- A `ManagedClusterSetBinding` called `global` to bind the `global` `ManagedClusterSet` to the `open-cluster-management-global-set` namespace.

Managed clusters that you create belong to the `global` `ManagedClusterSet` by default.

**Important:** You cannot delete the `global` managed cluster set, or update its `spec.clusterSelector`. The `global` managed cluster set includes all managed clusters. See the following example:

``` yaml
apiVersion: cluster.open-cluster-management.io/v1beta2
kind: ManagedClusterSetBinding
metadata:
  name: global
  namespace: open-cluster-management-global-set
spec:
  clusterSet: global
```

Continue reading to learn more about how to create a managed cluster set and add clusters to it:

- [Create a *ManagedClusterSet* by using the CLI](clusters.md#creating-managedclusterset-cli)

- [Add clusters to a *ManagedClusterSet* by using the CLI](clusters.md#adding-clusters-managedclusterset-cli)

<a id="creating-managedclusterset-cli"></a>

### Create a *ManagedClusterSet* by using the CLI

Create a managed cluster set by adding a `ManagedClusterSet` resource definition to your YAML file.

<div>

<div class="title">

Procedure

</div>

- Add the following definition of the managed cluster set to your YAML file to create a managed cluster set by using the CLI:

  ``` yaml
  apiVersion: cluster.open-cluster-management.io/v1beta2
  kind: ManagedClusterSet
  metadata:
    name: <cluster_set>
  ```

  Replace `<cluster_set>` with the name of your managed cluster set.

</div>

<a id="adding-clusters-managedclusterset-cli"></a>

### Add clusters to a *ManagedClusterSet* by using the command line

Complete the following steps to add a cluster to a managed cluster set by using the command line.

<div>

<div class="title">

Procedure

</div>

1.  Ensure that there is an RBAC `ClusterRole` entry that allows you to create on a virtual subresource of `managedclustersets/join`. Replace `<cluster_set>` with the name of your `ManagedClusterSet`:

    ``` yaml
    kind: ClusterRole
    apiVersion: rbac.authorization.k8s.io/v1
    metadata:
      name: clusterrole1
    rules:
      - apiGroups: ["cluster.open-cluster-management.io"]
        resources: ["managedclustersets/join"]
        resourceNames: ["<cluster_set>"]
        verbs: ["create"]
    ```

    **Notes:** \* Without this permission, you cannot assign a managed cluster to a `ManagedClusterSet`. If this entry does not exist, add it to your YAML file. \* If you are moving a managed cluster from one `ManagedClusterSet` to another, you must have that permission available on both managed cluster sets.

2.  Find the definition of the managed cluster in the YAML file. See the following example definition:

    ``` yaml
    apiVersion: cluster.open-cluster-management.io/v1
    kind: ManagedCluster
    metadata:
      name: <cluster_name>
    spec:
      hubAcceptsClient: true
    ```

3.  Add the `cluster.open-cluster-management.io/clusterset` paremeter and specify the name of the `ManagedClusterSet`. See the following example:

    ``` yaml
    apiVersion: cluster.open-cluster-management.io/v1
    kind: ManagedCluster
    metadata:
      name: <cluster_name>
      labels:
        cluster.open-cluster-management.io/clusterset: <cluster_set>
    spec:
      hubAcceptsClient: true
    ```

</div>

<a id="assign-role-managedclusterset"></a>

### Assign RBAC permissions to a *ManagedClusterSet*

You can assign users or groups to your cluster set that are provided by the configured identity providers on the hub cluster. Complete the following steps to assign users or groups to your managed cluster set from the console.

**Required access:** Cluster administrator

**Note:** You cannot apply the Cluster set `admin` permission for the global cluster set.

<div>

<div class="title">

Procedure

</div>

1.  From the OpenShift Container Platform console, navigate to **Infrastructure** \> **Clusters**.

2.  Select the *Cluster sets* tab.

3.  Select your target cluster set.

4.  Select the *Access management* tab.

5.  Select **Add user or group**.

6.  Search for, and select the user or group that you want to provide access.

7.  Select the **Cluster set admin** or **Cluster set view** role to give to the selected user or user group. See *Overview of roles* in [multicluster engine operator Role-based access control](clusters.md#mce-rbac) for more information.

8.  Select **Add** to submit the changes.

    **Note:** It might take a few seconds for the permission assignments for all of the managed cluster set resources to be propagated to your user or group.

</div>

<div class="formalpara">

<div class="title">

Additional resources

</div>

See [*ManagedCluster* selection filters](clusters.md#managedcluster-selection-filters) for placement information.

</div>

<a id="managedclusterset-api-rbac-permission-levels"></a>

### *ManagedClusterSet* API RBAC permission levels

Review the following `ManagedClusterSet` API RBAC permission levels table when you assign users or groups to a managed cluster set:

| Cluster set | Access permissions | Create permissions |
|----|----|----|
| `admin` | Full access permission to all of the cluster and cluster pool resources that are assigned to the managed cluster set. | Permission to create clusters, import clusters, and create cluster pools. The permissions must be assigned to the managed cluster set when it is created. |
| `bind` | Permission to bind the cluster set to a namespace by creating a `ManagedClusterSetBinding`. The user or group must also have permission to create the `ManagedClusterSetBinding` in the target namespace. Read only permissions to all of the cluster and cluster pool resources that are assigned to the managed cluster set. | No permission to create clusters, import clusters, or create cluster pools. |
| `view` | Read only permission to all of the cluster and cluster pool resources that are assigned to the managed cluster set. | No permission to create clusters, import clusters, or create cluster pools. |

Table of `ManagedClusterSet` API RBAC permission levels

<a id="creating-managedclustersetbinding"></a>

## *ManagedClusterSetBinding* resource overview

A `ManagedClusterSetBinding` resource binds a `ManagedClusterSet` resource to a namespace. Applications and policies that are created in the same namespace can only access clusters that are included in the bound managed cluster set resource.

Access permissions to the namespace automatically apply to a managed cluster set that is bound to that namespace. If you have access permissions to that namespace, you automatically have permissions to access any managed cluster set that is bound to that namespace.

If you only have permissions to access the managed cluster set, you do not automatically have permissions to access other managed cluster sets on the namespace.

You can create a managed cluster set binding by using the console or the command line. Continue reading to learn more:

- [Create a *ManagedClusterSetBinding* by using the console](clusters.md#creating-managedclustersetbinding-console)

- [Create a *ManagedClusterSetBinding* by using the CLI](clusters.md#creating-a-managedclustersetbinding-cli)

<a id="creating-managedclustersetbinding-console"></a>

### Create a *ManagedClusterSetBinding* by using the console

Complete the following steps to create a `ManagedClusterSetBinding` by using the console.

<div>

<div class="title">

Procedure

</div>

1.  From the OpenShift Container Platform console, navigate to **Infrastructure** \> **Clusters** and select the *Cluster sets* tab.

2.  Select the name of the cluster set that you want to create a binding for.

3.  Navigate to **Actions** \> **Edit namespace bindings**.

4.  On the *Edit namespace bindings* page, select the namespace to which you want to bind the cluster set from the drop-down menu.

</div>

<a id="creating-a-managedclustersetbinding-cli"></a>

### Create a *ManagedClusterSetBinding* by using the command line

Complete the following steps to create a `ManagedClusterSetBinding` by using the command line.

<div>

<div class="title">

Procedure

</div>

1.  Create the `ManagedClusterSetBinding` resource in your YAML file. See the following example:

    ``` yaml
    apiVersion: cluster.open-cluster-management.io/v1beta2
    kind: ManagedClusterSetBinding
    metadata:
      namespace: <namespace>
      name: <cluster_set>
    spec:
      clusterSet: <cluster_set>
    ```

    **Note:** When you create a managed cluster set binding, the name of the managed cluster set binding must match the name of the managed cluster set to bind.

2.  Ensure that you have the bind permission on the target managed cluster set. View the following example of a `ClusterRole` resource, which contains rules that allow the user to bind to `<cluster_set>`:

    ``` yaml
    apiVersion: rbac.authorization.k8s.io/v1
    kind: ClusterRole
    metadata:
      name: <clusterrole>
    rules:
      - apiGroups: ["cluster.open-cluster-management.io"]
        resources: ["managedclustersets/bind"]
        resourceNames: ["<cluster_set>"]
        verbs: ["create"]
    ```

</div>

<a id="set-hub-kube-api-server"></a>

#### Setting the hub cluster `KubeAPIServer` verification strategy

Managed clusters communicate with the hub cluster through a mutual connection with the OpenShift Container Platform `KubeAPIServer` external load balancer. An internal OpenShift Container Platform cluster certificate authority (CA) issues the default OpenShift Container Platform `KubeAPIServer` certificate when you install OpenShift Container Platform. The multicluster engine for Kubernetes operator automatically detects and adds the certificate to managed clusters in the `bootstrap-kubeconfig-secret` namespace.

If your automatically detected certificate does not work, you can manually configure a strategy configuration in the `KlusterletConfig` resource. Manually configuring the strategy allows you to control how you verify the hub cluster `KubeAPIServer` certificate.

**Required access:** Cluster administrator

See the examples in one of the following three strategies to learn how to manually configure a strategy:

<a id="set-hub-strategy-auto-detect-ca"></a>

##### Setting the strategy with *UseAutoDetectedCABundle*

The default configuration strategy is `UseAutoDetectedCABundle`. The multicluster engine operator automatically detects the certificate on the hub cluster and merges the certificate configured in the `trustedCABundles` list of config map references to the real CA bundles, if there are any.

The following example merges the automatically detected certificates from the hub cluster and the certificates that you configured in the `new-ocp-ca` config map, and adds both to the managed cluster:

``` yaml
apiVersion: config.open-cluster-management.io/v1alpha1
kind: KlusterletConfig
metadata:
 name: ca-strategy
spec:
 hubKubeAPIServerConfig:
   serverVerificationStrategy: UseAutoDetectedCABundle
   trustedCABundles:
   - name: new-ca
     caBundle:
       name: new-ocp-ca
       namespace: default
```

<a id="set-hub-strategy-system-truststore"></a>

##### Setting the strategy with *UseSystemTruststore*

When you define `UseSystemTruststore` as a value, multicluster engine operator does not detect any certificate and ignores the certificates configured in the `trustedCABundles` specification. This configuration does not pass any certificate to the managed clusters. Instead, the managed clusters use certificates from the system trusted store of the managed clusters to verify the hub cluster API server. This applies to situations where a public CA, such as `Let’s Encrypt`, issues the hub cluster certificate. See the following example that uses `UseSystemTruststore` as the parameter value:

``` yaml
apiVersion: config.open-cluster-management.io/v1alpha1
kind: KlusterletConfig
metadata:
 name: ca-strategy
spec:
 hubKubeAPIServerConfig:
   serverVerificationStrategy: UseSystemTruststore
```

<a id="config-hub-strategy-custom-ca"></a>

##### Setting the strategy with *UseCustomCABundles*

- You can use `UseCustomCABundles` if you know the CA of the hub cluster API server and do not want multicluster engine operator to automatically detect it. For this strategy, multicluster engine operator adds your configured certificates from the `trustedCABundles` parameter to the managed clusters. See the following examples to learn how to use `UseCustomCABundles`:

  ``` yaml
  apiVersion: config.open-cluster-management.io/v1alpha1
  kind: KlusterletConfig
  metadata:
   name: ca-strategy
  spec:
   hubKubeAPIServerConfig:
     serverVerificationStrategy: UseCustomCABundles
     trustedCABundles:
     - name: ca
       caBundle:
         name: ocp-ca
         namespace: default
  ```

- Typically, this policy is the same for each managed cluster. As the hub cluster administrator, you can configure a `KlusterletConfig` named `global` to activate the policy for each managed cluster when you install multicluster engine operator or the hub cluster certificate changes. See the following example:

  ``` yaml
  apiVersion: config.open-cluster-management.io/v1alpha1
  kind: KlusterletConfig
  metadata:
   name: global
  spec:
   hubKubeAPIServerConfig:
     serverVerificationStrategy: UseSystemTruststore
  ```

- When a managed cluster needs to use a different strategy, you can also create a different `KlusterletConfig` and use the `agent.open-cluster-management.io/klusterlet-config` annotation in the managed clusters to point to a specific strategy. See the following example:

  ``` yaml
  apiVersion: config.open-cluster-management.io/v1alpha1
  kind: KlusterletConfig
  metadata:
   name: test-ca
  spec:
   hubKubeAPIServerConfig:
     serverVerificationStrategy: UseCustomCABundles
     trustedCABundles:
     - name: ca
       caBundle:
         name: ocp-ca
         namespace: default
  --
  apiVersion: cluster.open-cluster-management.io/v1
  kind: ManagedCluster
  metadata:
    annotations:
      agent.open-cluster-management.io/klusterlet-config: test-ca
    name: cluster1
  spec:
    hubAcceptsClient: true
    leaseDurationSeconds: 60
  ```

<a id="set-managed-ns"></a>

#### Setting managed namespaces for *ManagedClusterSets*

You can define one or more managed namespaces in a `ManagedClusterSet` to manage and scale clusters efficiently, or to apply configurations consistently across your fleet. If you specify managed namespaces, they are automatically created on every managed cluster that belongs to the set.

**Important:** Namespaces that you create on managed clusters are not deleted, even in the followiwing situations:

- You remove the namespace from the `ManagedClusterSet` specification

- You move the managed cluster to a different `ManagedClusterSet`

- You detach the managed cluster from the hub cluster

Complete the following steps to create namespaces for your `ManagedClusterSet` resource:

1.  Add the name of your managed namespaces. See the following example of a `ManagedClusterSet` resource where the `my-cluster-ns1` and `my-cluster-ns2` managed namespaces are defined:

``` yaml
apiVersion: cluster.open-cluster-management.io/v1beta2
kind: ManagedClusterSet
metadata:
  name: my-clusterset
spec:
  clusterSelector:
    selectorType: ExclusiveClusterSetLabel
  managedNamespaces:
  - name: my-clusterset-ns1
  - name: my-clusterset-ns2
```

1.  Check the managed namespaces in the `status` of each `ManagedCluster` that is part of the set.

See the following `ManagedCluster` `status` with managed namespaces. The `conditions.type` shows if the namespace is available on the managed cluster:

``` yaml
apiVersion: cluster.open-cluster-management.io/v1
kind: ManagedCluster
metadata:
  labels:
    cluster.open-cluster-management.io/clusterset: my-clusterset
  name: cluster1
status:
  managedNamespaces:
  - clusterSet: my-clusterset
    conditions:
    - lastTransitionTime: "2025-09-26T03:15:52Z"
      message: Namespace successfully applied and managed
      reason: NamespaceApplied
      status: "True"
      type: NamespaceAvailable
    name: my-clusterset-ns1
  - clusterSet: my-clusterset
    conditions:
    - lastTransitionTime: "2025-09-26T03:15:52Z"
      message: Namespace successfully applied and managed
      reason: NamespaceApplied
      status: "True"
      type: NamespaceAvailable
    name: my-clusterset-ns2
```

<a id="removing-cluster-managedclusterset-console"></a>

### Remove a cluster from a *ManagedClusterSet* by using the console

Remove a managed cluster from a `ManagedClusterSet` to move it to a different `ManagedClusterSet`, or to stop applying the management settings of the set to the cluster.

**Note:** Every managed cluster must be assigned to a managed cluster set. If you remove a managed cluster from a `ManagedClusterSet` and do not assign it to a different `ManagedClusterSet`, the cluster is automatically added to the `default` managed cluster set.

<div>

<div class="title">

Prerequisites

</div>

- If the Submariner add-on is installed on your managed cluster, you must uninstall the add-on before removing your managed cluster from a `ManagedClusterSet`.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Click **Infrastructure** \> **Clusters** and ensure that the *Cluster sets* tab is selected.

2.  Select the name of the cluster set that you want to remove from the managed cluster set to view the cluster set details.

3.  Select **Actions** \> **Manage resource assignments**.

4.  On the *Manage resource assignments* page, remove the checkbox for the resources that you want to remove from the cluster set.

    This step removes a resource that is already a member of the cluster set. You can see if the resource is already a member of a cluster set by viewing the details of the managed cluster.

    **Note:** If you are moving a managed cluster from one managed cluster set to another, you must have the required RBAC permissions on both managed cluster sets.

</div>

<a id="removing-cluster-managedclusterset-cli"></a>

### Remove a cluster from a *ManagedClusterSet* by using the command line

Remove a managed cluster from a `ManagedClusterSet` to move it to a different `ManagedClusterSet`, or to stop applying the management settings of the set to the cluster.

**Note:** Every managed cluster must be assigned to a managed cluster set. If you remove a managed cluster from a `ManagedClusterSet` and do not assign it to a different `ManagedClusterSet`, the cluster is automatically added to the `default` managed cluster set.

<div>

<div class="title">

Prerequisites

</div>

- If the Submariner add-on is installed on your managed cluster, you must uninstall the add-on before removing your managed cluster from a `ManagedClusterSet`.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Run the following command to display a list of managed clusters in the managed cluster set:

    ``` bash
    oc get managedclusters -l cluster.open-cluster-management.io/clusterset=<cluster_set>
    ```

    Replace `cluster_set` with the name of the managed cluster set.

2.  Locate the entry for the cluster that you want to remove.

3.  Remove the label from the YAML entry for the cluster that you want to remove. See the following code for an example of the label:

    ``` yaml
    labels:
       cluster.open-cluster-management.io/clusterset: clusterset1
    ```

    **Note:** If you are moving a managed cluster from one cluster set to another, you must have the required RBAC permission on both managed cluster sets.

</div>

<a id="placement-intro"></a>

## Placement

A placement resource is a namespace-scoped resource that defines a rule to select a set of `ManagedClusters` from the `ManagedClusterSets`, which are bound to the placement namespace. Continue reading to learn more about how to use placements:

**Required access:** Cluster administrator, Cluster set administrator

- [Placement overview](clusters.md#placement-overview)

- [*ManagedCluster* selection filters](clusters.md#managedcluster-selection-filters)

- [Add-on status](clusters.md#add-on-status)

- [Prioritizer policy](clusters.md#prioritizer-policy)

- [Placement decisions](clusters.md#placement-decisions)

- [Taints and tolerations](clusters.md#taints-tolerations)

- [Managed cluster taints](clusters.md#managed-cluster-taints)

- [Built-in taints](clusters.md#built-in-taints)

- [Placement tolerations](clusters.md#placement-tolerations)

- [Temporary tolerations](clusters.md#temporary-tolerations)

<a id="placement-overview"></a>

### Placement overview

A placement selects managed clusters for workloads in a namespace. Clusters register with the hub cluster as `ManagedClusters` and are grouped into `ManagedClusterSets`, which you bind to that namespace. The placement filters those clusters, applies taints and tolerations, and uses prioritizer scores to choose how many clusters to select. Clusters that are scheduled for deletion are not selected. To learn more about the API and `Prioritizers`, use the *API Explorer* in the console, or an `oc` command. See the following information about how placement with managed clusters works:

- Kubernetes clusters are registered with the hub cluster as cluster-scoped `ManagedClusters`.

- The `ManagedClusters` are organized into cluster-scoped `ManagedClusterSets`.

- The `ManagedClusterSets` are bound to workload namespaces.

- The namespace-scoped placements specify a portion of `ManagedClusterSets` that select a working set of the potential `ManagedClusters`.

- Placements filter `ManagedClusters` from `ManagedClusterSets` by using `labelSelector` and `claimSelector`.

- The placement of `ManagedClusters` can be controlled by using taints and tolerations.

- Placements sort the clusters by `Prioritizers` scores and select the top `n` clusters from that group. You can define `n` in `numberOfClusters`.

- Placements do not select managed clusters that you are deleting.

- You must bind at least one `ManagedClusterSet` to a namespace by creating a `ManagedClusterSetBinding` in that namespace.

- You must have role-based access to `CREATE` on the virtual sub-resource of `managedclustersets/bind`.

<div>

<div class="title">

Additional resources

</div>

- [Taints and tolerations](clusters.md#taints-tolerations)

- [Troubleshooting no PlacementDecision after creating Placement](mce_troubleshooting.md#troubleshooting-no-placementdecision-mce)

- [Placement](clusters.md#placement-intro)

</div>

<a id="managedcluster-selection-filters"></a>

### *ManagedCluster* selection filters

The `labelSelector`, `claimSelector`, and `celSelector` fields filter which `ManagedCluster` objects a placement selects. The `numberOfClusters` parameter sets how many `ManagedClusters` the placement selects. See the following examples to learn more about the filters:

- In the following example, the `labelSelector` field only matches clusters with the `vendor: OpenShift` label:

  ``` yaml
  apiVersion: cluster.open-cluster-management.io/v1beta1
  kind: Placement
  metadata:
    name: placement
    namespace: ns1
  spec:
    predicates:
      - requiredClusterSelector:
          labelSelector:
            matchLabels:
              vendor: OpenShift
  ```

- In the following example, `claimSelector` only matches clusters with `region.open-cluster-management.io` with `us-west-1`:

  ``` yaml
  apiVersion: cluster.open-cluster-management.io/v1beta1
  kind: Placement
  metadata:
    name: placement
    namespace: ns1
  spec:
    predicates:
      - requiredClusterSelector:
          claimSelector:
            matchExpressions:
              - key: region.open-cluster-management.io
                operator: In
                values:
                  - us-west-1
  ```

- You can also filter `ManagedClusters` from particular cluster sets by using the `clusterSets` parameter. In the following example, `claimSelector` only matches the cluster sets `clusterset1` and `clusterset2`:

  ``` yaml
  apiVersion: cluster.open-cluster-management.io/v1beta1
  kind: Placement
  metadata:
    name: placement
    namespace: ns1
  spec:
    clusterSets:
      - clusterset1
      - clusterset2
    predicates:
      - requiredClusterSelector:
          claimSelector:
            matchExpressions:
              - key: region.open-cluster-management.io
                operator: In
                values:
                  - us-west-1
  ```

- The following example displays five different ways of how you can use the `celSelector` field with Common Expression Language. You can use one or several expressions to filter your `ManagedCluster` objects. See *Common Expression Language in Kubernetes* in the additional resources section to learn more:

  ``` yaml
  apiVersion: cluster.open-cluster-management.io/v1beta1
  kind: Placement
  metadata:
    name: placement1
    namespace: ns1
  spec:
    numberOfClusters: 3
    clusterSets:
      - clusterset1
    predicates:
    - requiredClusterSelector:
        celSelector:
          celExpressions:
            - managedCluster.status.version.kubernetes == "v1.31.0"
            - managedCluster.status.clusterClaims.exists(c, c.name == "kubeversion.open-cluster-management.io" && c.value == "v1.31.0")
            - managedCluster.metadata.labels["version"].matches('^1\\.(30|31).d+$')
            - semver(managedCluster.metadata.labels["version"]).isGreaterThan(semver("1.30.0"))
            - managedCluster.scores("resource-usage-score").filter(s, s.name == 'memNodeAvailable').all(e, e.value > 0)
  ```

- `managedCluster.status.version.kubernetes == "v1.31.0"` is the Kubernetes version in the `managedCluster.status.version.kubernetes` field.

- `clusterClaims.exists` is a value that is stored in the `clusterClaims` field.

- `labels["version"].matches` is a Common Expression Language macro or function that is applied to `managedCluster` fields.

- `semver` with `isGreaterThan` is a version comparison that uses the Kubernetes `semver` library functions `isLessThan` and `isGreaterThan`.

- `managedCluster.scores` is a customized score from the `AddonPlacementScore` field.

- See the following example of `numberOfClusters` with the number of `ManagedClusters` to select. This example selects `3` clusters:

  ``` yaml
  apiVersion: cluster.open-cluster-management.io/v1beta1
  kind: Placement
  metadata:
    name: placement
    namespace: ns1
  spec:
    numberOfClusters: 3
    predicates:
      - requiredClusterSelector:
          labelSelector:
            matchLabels:
              vendor: OpenShift
          claimSelector:
            matchExpressions:
              - key: region.open-cluster-management.io
                operator: In
                values:
                  - us-west-1
  ```

<div>

<div class="title">

Additional resources

</div>

- [Common Expression Language in Kubernetes](https://kubernetes.io/docs/reference/using-api/cel/)

- [Placement](clusters.md#placement-intro)

</div>

<a id="add-on-status"></a>

### Add-on status

Placements can select managed clusters based on the status of the add-ons that are deployed on them. For example, a placement can select a managed cluster only if a specific add-on is enabled on that cluster.

You can specify the label for the add-on, as well as its status, when you create the placement. A label is automatically created on a `ManagedCluster` resource if an add-on is enabled on the managed cluster. The label is automatically removed if the add-on is disabled.

Each add-on is represented by a label in the format of `feature.open-cluster-management.io/addon-<addon_name>=<status_of_addon>`.

In that format, `addon_name` is the name of the add-on on the managed cluster, and `status_of_addon` is the add-on status required for the cluster to be selected.

| Value | Description |
|----|----|
| `available` | The add-on is enabled and available. |
| `unhealthy` | The add-on is enabled, but the lease is not updated continuously. |
| `unreachable` | The add-on is enabled, but there is no lease found for it. This can also be caused when the managed cluster is offline. |

Add-on status values

For example, an available `application-manager` add-on is represented by a label on the managed cluster that reads the following:

    feature.open-cluster-management.io/addon-application-manager: available

See the following examples to learn how to create placements based on add-ons and their status:

- The following placement example includes all managed clusters that have `application-manager` enabled on them:

  ``` yaml
  apiVersion: cluster.open-cluster-management.io/v1beta1
  kind: Placement
  metadata:
    name: placement1
    namespace: ns1
  spec:
    predicates:
      - requiredClusterSelector:
          labelSelector:
            matchExpressions:
              - key: feature.open-cluster-management.io/addon-application-manager
                operator: Exists
  ```

- The following placement example includes all managed clusters that have `application-manager` enabled with an `available` status:

  ``` yaml
  apiVersion: cluster.open-cluster-management.io/v1beta1
  kind: Placement
  metadata:
    name: placement2
    namespace: ns1
  spec:
    predicates:
      - requiredClusterSelector:
          labelSelector:
            matchLabels:
              "feature.open-cluster-management.io/addon-application-manager": "available"
  ```

- The following placement example includes all managed clusters that have `application-manager` disabled:

  ``` yaml
  apiVersion: cluster.open-cluster-management.io/v1beta1
  kind: Placement
  metadata:
    name: placement3
    namespace: ns1
  spec:
    predicates:
      - requiredClusterSelector:
          labelSelector:
            matchExpressions:
              - key: feature.open-cluster-management.io/addon-application-manager
                operator: DoesNotExist
  ```

<div>

<div class="title">

Additional resources

</div>

- [Placement](clusters.md#placement-intro)

</div>

<a id="prioritizer-policy"></a>

### Prioritizer policy

The `prioritizerPolicy` parameter ranks `ManagedClusters` so a placement can select the highest scoring clusters. View the following examples to learn how to prioritize `ManagedClusters` by using the `prioritizerPolicy` parameter with placement.

- The following example selects a cluster with the largest allocatable memory. Similar to Kubernetes *Node Allocatable*, 'allocatable' is defined as the amount of compute resources that are available for pods on each cluster:

  ``` yaml
  apiVersion: cluster.open-cluster-management.io/v1beta1
  kind: Placement
  metadata:
    name: placement
    namespace: ns1
  spec:
    numberOfClusters: 1
    prioritizerPolicy:
      configurations:
        - scoreCoordinate:
            builtIn: ResourceAllocatableMemory
  ```

- The following example selects a cluster with the largest allocatable CPU and memory, and makes placement sensitive to resource changes:

  ``` yaml
  apiVersion: cluster.open-cluster-management.io/v1beta1
  kind: Placement
  metadata:
    name: placement
    namespace: ns1
  spec:
    numberOfClusters: 1
    prioritizerPolicy:
      configurations:
        - scoreCoordinate:
            builtIn: ResourceAllocatableCPU
          weight: 2
        - scoreCoordinate:
            builtIn: ResourceAllocatableMemory
          weight: 2
  ```

- The following example selects two clusters with the largest `addOn` score CPU ratio, and pins the placement decisions:

  ``` yaml
  apiVersion: cluster.open-cluster-management.io/v1beta1
  kind: Placement
  metadata:
    name: placement
    namespace: ns1
  spec:
    numberOfClusters: 2
    prioritizerPolicy:
      mode: Exact
      configurations:
        - scoreCoordinate:
            builtIn: Steady
          weight: 3
        - scoreCoordinate:
            type: AddOn
            addOn:
              resourceName: default
              scoreName: cpuratio
  ```

<div>

<div class="title">

Additional resources

</div>

- [Node Allocatable](https://kubernetes.io/docs/tasks/administer-cluster/reserve-compute-resources/#node-allocatable)

- [Placement](clusters.md#placement-intro)

</div>

<a id="placement-decisions"></a>

### Placement decisions

One or more `PlacementDecision` kinds with the label `cluster.open-cluster-management.io/placement={placement_name}` are created to represent `ManagedClusters` selected by a placement. To learn more about the API, use the *API Explorer* in the console, or an `oc` command. If you select a `ManagedCluster` and add it to a `PlacementDecision`, the components that consume this placement might apply the workload on this `ManagedCluster`.

When you do not select `ManagedCluster` and you remove it from the `PlacementDecision`, the workload that is applied on this `ManagedCluster` is removed. You can prevent the workload removal by defining tolerations. To learn more about tolerations, see [Taints and tolerations](clusters.md#taints-tolerations).

See the following `PlacementDecision` example:

``` yaml
apiVersion: cluster.open-cluster-management.io/v1beta1
kind: PlacementDecision
metadata:
  labels:
    cluster.open-cluster-management.io/placement: placement1
  name: placement1-kbc7q
  namespace: ns1
  ownerReferences:
    - apiVersion: cluster.open-cluster-management.io/v1beta1
      blockOwnerDeletion: true
      controller: true
      kind: Placement
      name: placement1
      uid: 05441cf6-2543-4ecc-8389-1079b42fe63e
status:
  decisions:
    - clusterName: cluster1
      reason: ''
    - clusterName: cluster2
      reason: ''
    - clusterName: cluster3
      reason: ''
```

<div>

<div class="title">

Additional resources

</div>

- [Troubleshooting no PlacementDecision after creating Placement](mce_troubleshooting.md#troubleshooting-no-placementdecision-mce)

- [Placement](clusters.md#placement-intro)

</div>

<a id="taints-tolerations"></a>

## Taints and tolerations

You can control which placements can select your managed clusters by using taints and tolerations. This mechanism is useful when you want to restrict certain clusters to specific workloads. *Taints* on a managed cluster prevent most placements from selecting that managed cluster. *Tolerations* on a placement allow the placement to select clusters with matching taints. By default, placements do not select managed clusters that have the `NoSelect` taint. If the `NoSelectIfNew` effect is specified, a cluster that was already selected stays selected.

**Important:** When a cluster has a taint, only placements with matching tolerations can select that cluster. This filtering happens automatically to protect workloads from being deployed to clusters that might not be suitable. For example, if a managed cluster becomes unreachable or unavailable, built-in taints are automatically applied to prevent new workloads from being placed on that cluster until it recovers. See the following information about built-in taints and how to use tolerations to allow placements to select clusters with built-in taints:

- [Managed cluster taints](clusters.md#managed-cluster-taints)

- [Built-in taints](clusters.md#built-in-taints)

- [Placement tolerations](clusters.md#placement-tolerations)

- [Temporary tolerations](clusters.md#temporary-tolerations)

<a id="managed-cluster-taints"></a>

### Managed cluster taints

Taints are specified in the properties of a managed cluster and prevent placements from selecting that cluster unless the placement has a matching toleration. When the `taints` section does not exist, the following command adds one:

``` bash
oc patch managedcluster <managed_cluster_name> -p '{"spec":{"taints":[{"key": "key", "value": "value", "effect": "NoSelect"}]}}' --type=merge
```

When taints already exist, the following command appends another taint:

``` bash
oc patch managedcluster <managed_cluster_name> --type='json' -p='[{"op": "add", "path": "/spec/taints/-", "value": {"key": "key", "value": "value", "effect": "NoSelect"}}]'
```

The specification of a taint includes the following fields:

- **Required** Key - The taint key that is applied to a cluster. This value must match the value in the toleration for the managed cluster to meet the criteria for being added to that placement. You can determine this value. For example, this value could be `bar` or `foo.example.com/bar`.

- **Optional** Value - The taint value for the taint key. This value must match the value in the toleration for the managed cluster to meet the criteria for being added to that placement. For example, this value could be `value`.

- **Required** Effect - The effect of the taint on placements that do not tolerate the taint, or what occurs when the taint and the toleration of the placement do not match. The value of the effects must be one of the following values:

  - `NoSelect` - Placements are not allowed to select a cluster unless they tolerate this taint. If the cluster was selected by the placement before the taint was set, the cluster is removed from the placement decision.

  - `NoSelectIfNew` - The scheduler cannot select the cluster if it is a new cluster. Placements can only select the cluster if they tolerate the taint and already have the cluster in their cluster decisions.

- **Required** `TimeAdded` - The time when the taint was added. This value is automatically set.

<div>

<div class="title">

Additional resources

</div>

- [Placement](clusters.md#placement-intro)

</div>

<a id="built-in-taints"></a>

### Built-in taints

Built-in taints are automatically added to managed clusters based on availability status. Learning about the built-in taints can help you understand why a placement does not select a managed cluster.

`cluster.open-cluster-management.io/unavailable`  
This taint is added to a managed cluster when the cluster has a condition of `ManagedClusterConditionAvailable` with status of `False`. The taint has the effect of `NoSelect` and an empty value to prevent an unavailable cluster from being selected by placements.

See the following example of a managed cluster with the `cluster.open-cluster-management.io/unavailable` taint:

``` yaml
apiVersion: cluster.open-cluster-management.io/v1
kind: ManagedCluster
metadata:
  name: cluster1
spec:
  hubAcceptsClient: true
  taints:
    - effect: NoSelect
      key: cluster.open-cluster-management.io/unavailable
      timeAdded: '2022-02-21T08:11:54Z'
```

`cluster.open-cluster-management.io/unreachable`  
This taint is added to a managed cluster when the status of the condition for `ManagedClusterConditionAvailable` is either `Unknown` or has no condition. The taint has the effect of `NoSelect` and an empty value to prevent an unreachable cluster from being selected by placements.

See the following example of a managed cluster with the `cluster.open-cluster-management.io/unreachable` taint:

``` yaml
apiVersion: cluster.open-cluster-management.io/v1
kind: ManagedCluster
metadata:
  name: cluster1
spec:
  hubAcceptsClient: true
  taints:
    - effect: NoSelect
      key: cluster.open-cluster-management.io/unreachable
      timeAdded: '2022-02-21T08:11:06Z'
```

<div>

<div class="title">

Additional resources

</div>

- [Placement](clusters.md#placement-intro)

</div>

<a id="placement-tolerations"></a>

### Placement tolerations

Tolerations are applied to placements, and allow the placements to select managed clusters that have matching taints.

The specification of a toleration includes the following fields:

- Key (optional):: The key matches the taint key to allow the placement.

- Value (optional):: The value in the toleration must match the value of the taint for the toleration to allow the placement.

- Operator (optional):: The operator represents the relationship between a key and a value. Valid operators are `Equal` and `Exists`. The default value is `Equal`. A toleration matches a taint when the keys are the same, the effects are the same, and the operator is one of the following values:

  - `Equal` - The operator is `Equal` and the values are the same in the taint and the toleration.

  - `Exists` - The wildcard for value, so a placement can tolerate all taints of a particular category.

- Effect (optional):: The taint effect to match. When left empty, it matches all taint effects. The allowed values when specified are `NoSelect` or `NoSelectIfNew`.

- `TolerationSeconds` (optional):: The length of time, in seconds, that the toleration tolerates the taint before the placement stops selecting that cluster. If the effect value is not `NoSelect` or `NoSelectIfNew`, this field is ignored. The default value is `nil`, which indicates that there is no time limit. The time counting starts from the `TimeAdded` value in the taint, not from when the cluster was selected or when the toleration was added.

The following example shows how to configure a toleration that tolerates clusters that have taints:

- Taint on the managed cluster for this example:

  ``` yaml
  apiVersion: cluster.open-cluster-management.io/v1
  kind: ManagedCluster
  metadata:
    name: cluster1
  spec:
    hubAcceptsClient: true
    taints:
      - effect: NoSelect
        key: gpu
        value: "true"
        timeAdded: '2022-02-21T08:11:06Z'
  ```

- Toleration on the placement that allows the taint to be tolerated:

  ``` yaml
  apiVersion: cluster.open-cluster-management.io/v1beta1
  kind: Placement
  metadata:
    name: placement1
    namespace: default
  spec:
    tolerations:
      - key: gpu
        value: "true"
        operator: Equal
  ```

  With the example tolerations defined, `cluster1` can be selected by the placement because the `key: gpu` and `value: "true"` match.

**Note:** A placement with a matching toleration is not guaranteed to select a specific managed cluster. Other selection criteria and prioritizers also affect which clusters are selected.

<div>

<div class="title">

Additional resources

</div>

- [Placement](clusters.md#placement-intro)

</div>

<a id="temporary-tolerations"></a>

### Temporary tolerations

The value of `TolerationSeconds` specifies the period of time that the toleration tolerates the taint. This temporary toleration can be helpful when a managed cluster is offline and you want workloads to move to another managed cluster after a grace period.

For example, the managed cluster with the following taint becomes unreachable:

``` yaml
apiVersion: cluster.open-cluster-management.io/v1
kind: ManagedCluster
metadata:
  name: cluster1
spec:
  hubAcceptsClient: true
  taints:
    - effect: NoSelect
      key: cluster.open-cluster-management.io/unreachable
      timeAdded: '2022-02-21T08:11:06Z'
```

If you define a placement with a value for `TolerationSeconds`, as in the following example, the placement stops selecting the unreachable cluster after 5 minutes, allowing workloads to be deployed to another available managed cluster.

``` yaml
apiVersion: cluster.open-cluster-management.io/v1beta1
kind: Placement
metadata:
  name: demo4
  namespace: demo1
spec:
  tolerations:
    - key: cluster.open-cluster-management.io/unreachable
      operator: Exists
      tolerationSeconds: 300
```

After the managed cluster is unreachable for 5 minutes, the placement removes it from the selection, triggering the workload management system to redeploy to another cluster.

You can also tolerate all built-in taints without a time limit. The following example shows a placement that continues to select clusters even when they are unreachable or unavailable:

``` yaml
apiVersion: cluster.open-cluster-management.io/v1beta1
kind: Placement
metadata:
  name: placement1
  namespace: ns1
spec:
  tolerations:
    - key: cluster.open-cluster-management.io/unreachable
      operator: Exists
    - key: cluster.open-cluster-management.io/unavailable
      operator: Exists
```

With these tolerations, the placement continues to select the managed clusters indefinitely, regardless of their availability status.

<div>

<div class="title">

Additional resources

</div>

- [Placement](clusters.md#placement-intro)

</div>

<a id="managing-cluster-pools"></a>

### Cluster pools (Technology Preview)

Cluster pools provide rapid and cost-effective access to configured Red Hat OpenShift Container Platform clusters on-demand and at scale.

Cluster pools provision a configurable and scalable number of OpenShift Container Platform clusters on Amazon Web Services, Google Cloud Platform, or Microsoft Azure that can be claimed when they are needed. They are especially useful when providing or replacing cluster environments for development, continuous integration, and production scenarios. You can specify several clusters to remain available to be claimed immediately, while the remainder of the clusters remain in a hibernating state so that they can be resumed and claimed within a few minutes.

`ClusterClaim` resources are used to check out clusters from cluster pools. When a cluster claim is created, the pool assigns a running cluster to it. If no running clusters are available, a hibernating cluster is resumed to provide the cluster or a new cluster is provisioned. The cluster pool automatically creates new clusters and resumes hibernating clusters to maintain the specified size and number of available running clusters in the pool.

The procedure for creating a cluster pool is similar to the procedure for creating a cluster. Clusters in a cluster pool are not created for immediate use.

<div>

<div class="title">

Additional resources

</div>

- [Create a cluster pool](clusters.md#creating-a-clusterpool)

- [Create a single-node OpenShift cluster pool](clusters.md#create-a-sno-cluster-pool)

- [Claim clusters from cluster pools](clusters.md#claiming-clusters-from-cluster-pools)

- [Update the cluster pool release image](clusters.md#updating-the-cluster-pool-release-image)

- [Scale cluster pools](clusters.md#scaling-cluster-pools)

- [Destroy a cluster pool](clusters.md#destroying-a-cluster-pool)

</div>

<a id="creating-a-clusterpool"></a>

#### Create a cluster pool

Create a cluster pool to provision a scalable number of OpenShift Container Platform clusters that you can claim when you need them. Clusters in a cluster pool are not created for immediate use.

**Required access**: Administrator

<div>

<div class="title">

Prerequisites

</div>

- You need to deploy a multicluster engine operator hub cluster.

- You need Internet access for your multicluster engine operator hub cluster so that it can create the Kubernetes cluster on the provider environment.

- You need an AWS, GCP, or Microsoft Azure provider credential. See [Managing credentials overview](clusters.md#credentials) for more information.

- You need a configured domain in your provider environment. See your provider documentation for instructions about how to configure a domain.

- You need provider login credentials.

- You need your OpenShift Container Platform image pull secret. See [Using image pull secrets](https://docs.redhat.com/en/documentation/openshift_container_platform/4.20/html/images/managing-images#using-image-pull-secrets).

  **Note:** Adding a cluster pool with this procedure configures it so it automatically imports the cluster for multicluster engine operator management when you claim a cluster from the pool. If you want to create a cluster pool that does not automatically import the claimed cluster for management with the cluster claim, add the following annotation to your `clusterClaim` resource:

  ``` yaml
  kind: ClusterClaim
  metadata:
    annotations:
      cluster.open-cluster-management.io/createmanagedcluster: "false"
  ```

- The word `"false"` must be surrounded by quotation marks to indicate that it is a string.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Select **Infrastructure** \> **Clusters** in the navigation menu. The *Cluster pools* tab lists the cluster pools that you can access.

2.  Select **Create cluster pool** and complete the steps in the console.

3.  If you do not have an infrastructure credential that you want to use for the cluster pool, select **Add credential** to create one.

4.  Select an existing namespace from the list, or type the name of a new one to create one. The cluster pool does not have to be in the same namespace as the clusters.

5.  **Optional:** Select a cluster set name if you want the RBAC roles for your cluster pool to share the role assignments of an existing cluster set. The cluster set for the clusters in the cluster pool can only be set when you create the cluster pool. You cannot change the cluster set association for the cluster pool or for the clusters in the cluster pool after you create the cluster pool. Any cluster that you claim from the cluster pool is automatically added to the same cluster set as the cluster pool.

    **Note:** If you do not have `cluster admin` permissions, you must select a cluster set. The request to create a cluster set is rejected with a forbidden error if you do not include the cluster set name in this situation. If no cluster sets are available for you to select, contact your cluster administrator to create a cluster set and give you `clusterset admin` permissions to it.

6.  Enter the `cluster pool size` to specify the number of clusters that you want provisioned in your cluster pool, and enter the cluster pool running count to specify the number of clusters that the pool keeps running and ready to claim for immediate use.

    **Note:** The procedure is very similar to the procedure for creating clusters.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Create a cluster on Amazon Web Services](clusters.md#create-a-cluster-on-amazon-web-services)

- [Create a cluster on Microsoft Azure](clusters.md#create-a-cluster-on-microsoft-azure)

</div>

<a id="create-a-sno-cluster-pool"></a>

#### Create a single-node OpenShift cluster pool (Technology Preview)

Create a single-node OpenShift cluster pool to provision hibernating single-node clusters that you can claim when you need them. Clusters in a single-node OpenShift cluster pool are not created for immediate use.

`ClusterClaim` resources are used to check out clusters from cluster pools. After a cluster is checked out from a cluster pool, the checked out cluster is resumed and brought to a ready state. The cluster pool automatically creates a hibernated cluster in the cluster pool, to replace the claimed one.

**Note:** When a cluster that was claimed from the cluster pool is no longer needed and is destroyed, the resources are deleted. The cluster does not return to the cluster pool.

The procedure for creating a single-node OpenShift cluster pool is similar to the procedure for creating a cluster.

**Required access**: Administrator

<div>

<div class="title">

Prerequisites

</div>

- A deployed multicluster engine operator hub cluster.

- Internet access for your hub cluster so it can create the Kubernetes cluster on the provider environment.

- An AWS, GCP, or Microsoft Azure provider credential. See [Managing credentials overview](clusters.md#credentials) for more information.

- A configured domain in your provider environment. See your provider documentation for instructions about how to configure a domain.

- Provider login credentials.

- A OpenShift Container Platform image pull secret. See [Using image pull secrets](https://docs.redhat.com/en/documentation/openshift_container_platform/4.20/html/images/managing-images#using-image-pull-secrets).

- Enable the single-node OpenShift feature. The single-node OpenShift feature is disabled by default when you install Red Hat Advanced Cluster Management. You must enable it by completing the following steps:

  - Log in to your Red Hat Advanced Cluster Management hub cluster with `administrator` permissions.

  - Enable the feature by entering the following command:

  ``` bash
  oc patch configmap console-config -n open-cluster-management --patch '{"data":{"singleNodeOpenshift":"enabled"}}'
  ```

</div>

<div>

<div class="title">

Procedure

</div>

1.  From the multicluster engine operator console navigation menu, click **Infrastructure** \> **Clusters**.

2.  Select the *Cluster pools* tab to view cluster pools that you can access.

3.  Select **Create cluster pool** and complete the steps in the console to create a cluster pool.

4.  Select the infrastructure credential that you want to use for the cluster pool. You can create one by selecting **Add credential**, if it is not available in the list.

5.  Add the cluster pool details. Enter the namespace where you want to create your cluster pool. You can select an existing namespace from the list, or type the name of a new one to create one. The cluster pool does not have to be in the same namespace as the clusters.

    **Note:** When you create a cluster pool in a cluster set, the `namespace admin` permission is applied to all of the users with `clusterset admin` permissions for the namespace where you add the cluster pool. Similarly, the `namespace view` permission is applied to the users with `clusterset view` permissions.

6.  **Optional:** Select a cluster set name if you want the RBAC roles for your cluster pool to share the role assignments of an existing cluster set.

    **Note:** If you do not have `cluster admin` permissions, you must select a cluster set. The request to create a cluster set is rejected with a forbidden error if you do not include the cluster set name in this situation. If no cluster sets are available for you to select, contact your cluster administrator to create a cluster set and give you `clusterset admin` permissions to it.

7.  Enter the number of clusters that you want available in your cluster pool by adding the number to the cluster pool size.

8.  Enter the required information in the remaining steps to complete to provision your cluster pool. The procedure from this point on is the same as the procedure for creating clusters.

9.  While you create your cluster pool, you must select a supported OpenShift Container Platform version in the *Release image* field. If you enabled the feature gate, an option to select **Single node OpenShift** is displayed.

    **Note:** If you select an OpenShift Container Platform version that is older than 4.9, the option to select *Single node OpenShift* is not displayed.

10. Select **Single node OpenShift**.

11. Add the `spec:skipMachinePools` parameter in the YAML content to `true` by completing the following steps:

    1.  If you cannot see the YAML content window, set the switch to **YAML:On** to view the content.

    2.  Find the `spec` section for your cluster and add the following flag to the `spec` section:

    <!-- -->

        skipMachinePools: true

12. After all of the information is entered, select **Create** to create the cluster pool.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Create a cluster on Amazon Web Services](clusters.md#create-a-cluster-on-amazon-web-services)

- [Create a cluster on Microsoft Azure](clusters.md#create-a-cluster-on-microsoft-azure)

</div>

<a id="claiming-clusters-from-cluster-pools"></a>

#### Claim clusters from cluster pools

Claim a cluster from a cluster pool by creating a `ClusterClaim` resource. The pool assigns a running cluster, resumes a hibernating cluster, or provisions a new cluster to fulfill the claim.

`ClusterClaim` resources are used to check out clusters from cluster pools. Claim a cluster when it is running and ready in the cluster pool. The cluster pool automatically creates new running and hibernated clusters in the cluster pool to maintain the requirements that are specified for the cluster pool.

When you create a cluster claim, you request a new cluster from the cluster pool. A cluster is checked out from the pool when a cluster is available. The claimed cluster is automatically imported as one of your managed clusters, unless you disabled automatic import.

If a cluster is available, it is claimed and immediately appears in the *Managed clusters* tab. If there are no available clusters, it might take several minutes to resume a hibernated cluster or provision a new cluster. During this time, the claim status is `pending`. Expand the cluster pool to view or delete pending claims against it.

The claimed cluster remains a member of the cluster set that it was associated with when it was in the cluster pool. You cannot change the cluster set of the claimed cluster when you claim it.

**Required access**: Administrator

<div>

<div class="title">

Prerequisites

</div>

- You must have a cluster pool with or without available clusters. If there are available clusters in the cluster pool, the available clusters are claimed. If there are no available clusters in the cluster pool, a cluster is created to fulfill the claim. See [Create a cluster pool](clusters.md#creating-a-clusterpool) for information about how to create a cluster pool.

</div>

<div>

<div class="title">

Procedure

</div>

1.  From the navigation menu, click **Infrastructure** \> **Clusters**, and select the *Cluster pools* tab.

2.  Find the name of the cluster pool you want to claim a cluster from and select **Claim cluster**.

    **Notes:**

    - Changes to the pull secret, SSH keys, or base domain of the cloud provider credentials are not reflected for existing clusters that are claimed from a cluster pool, as they have already been provisioned using the original credentials. You cannot edit cluster pool information by using the console, but you can update it by updating its information using the CLI interface. You can also create a new cluster pool with a credential that contains the updated information. The clusters that are created in the new pool use the settings provided in the new credential.

    - When a cluster that was claimed from the cluster pool is no longer needed and is destroyed, the resources are deleted. The cluster does not return to the cluster pool.

</div>

<a id="updating-the-cluster-pool-release-image"></a>

#### Update the cluster pool release image

Update the OpenShift Container Platform release image for clusters in a cluster pool when hibernating clusters become backlevel.

**Required access**: Edit

**Note:** This procedure does not update clusters from the cluster pool that are already claimed in the cluster pool. After you complete this procedure, the updates to the release images only apply to the following clusters that are related to the cluster pool:

- Clusters that are created by the cluster pool after updating the release image with this procedure.

- Clusters that are hibernating in the cluster pool. The existing hibernating clusters with the old release image are destroyed, and new clusters with the new release image replace them.

<div>

<div class="title">

Procedure

</div>

1.  From the navigation menu, click **Infrastructure** \> **Clusters**.

2.  Select the *Cluster pools* tab.

3.  Find the name of the cluster pool that you want to update in the *Cluster pools* table.

4.  Click the *Options* menu for the *Cluster pools* in the table, and select **Update release image**.

5.  Select a new release image to use for future cluster creations from this cluster pool.

6.  Update the release image for multiple cluster pools with one by selecting the box for each of the cluster pools. Use the *Actions* menu to update the release image for the selected cluster pools.

</div>

<a id="scaling-cluster-pools"></a>

#### Scale cluster pools (Technology Preview)

Scale a cluster pool by increasing or decreasing the cluster pool size and the number of running clusters.

**Required access**: Cluster administrator

<div>

<div class="title">

Procedure

</div>

1.  From the navigation menu, click **Infrastructure** \> **Clusters**.

2.  Select the *Cluster pools* tab.

3.  In the *Options* menu for the cluster pool that you want to change, select **Scale cluster pool**.

4.  Change the value of the pool size.

5.  **Optional:** Update the number of running clusters to increase or decrease the number of clusters that are immediately available when you claim them.

</div>

<a id="destroying-a-cluster-pool"></a>

#### Destroy a cluster pool

Destroy a cluster pool that you no longer need. You can only destroy cluster pools that do not have any cluster claims.

**Important:** You can only destroy cluster pools that do not have any cluster claims.

**Required access**: Cluster administrator

<div>

<div class="title">

Procedure

</div>

1.  From the navigation menu, click **Infrastructure** \> **Clusters**.

2.  Select the *Cluster pools* tab.

3.  In the *Options* menu for the cluster pool that you want to delete, type `confirm` in the confirmation box and select **Destroy**.

    **Notes:**

    - The **Destroy** button is disabled if the cluster pool has any cluster claims.

    - The namespace that contains the cluster pool is not deleted. Deleting the namespace destroys any clusters that have been claimed from the cluster pool, since the cluster claim resources for these clusters are created in the same namespace.

4.  Destroy multiple cluster pools by selecting the box for each of the cluster pools. Use the *Actions* menu to destroy the selected cluster pools.

</div>

<a id="managed-serviceaccount-addon"></a>

### Enabling ManagedServiceAccount add-ons

When you install a supported version of multicluster engine operator, the `ManagedServiceAccount` add-on is enabled by default.

The `ManagedServiceAccount` allows you to create or delete a service account on a managed cluster.

**Required access:** Editor

When a `ManagedServiceAccount` custom resource is created in the `<managed_cluster>` namespace on the hub cluster, a `ServiceAccount` is created on the managed cluster.

A `TokenRequest` is made with the `ServiceAccount` on the managed cluster to the Kubernetes API server on the managed cluster. The token is then stored in a `Secret` in the `<target_managed_cluster>` namespace on the hub cluster.

**Note:** The token can expire and be rotated. See [TokenRequest](https://kubernetes.io/docs/reference/kubernetes-api/authentication-resources/token-request-v1/) for more information about token requests.

<a id="serviceaccount_prereqs"></a>

#### Prerequisites

- You need a supported Red Hat OpenShift Container Platform environment.

- You need the multicluster engine operator installed.

<a id="serviceaccount_enable"></a>

#### Enabling ManagedServiceAccount

To enable a `ManagedServiceAccount` add-on for a hub cluster and a managed cluster, complete the following steps:

1.  Enable the `ManagedServiceAccount` add-on on hub cluster. See *ManagedServiceAccount add-on* in [Advanced configuration](clusters.md#advanced-config-engine) to learn more.

2.  Deploy the `ManagedServiceAccount` add-on and apply it to your target managed cluster. Create the following YAML file and replace `target_managed_cluster` with the name of the managed cluster where you are applying the `Managed-ServiceAccount` add-on:

    ``` yaml
    apiVersion: addon.open-cluster-management.io/v1alpha1
    kind: ManagedClusterAddOn
    metadata:
      name: managed-serviceaccount
      namespace: <target_managed_cluster>
    spec:
      installNamespace: open-cluster-management-agent-addon
    ```

    **Note:** The `spec.installNamespace` field is deprecated. See [Product deprecations and removals](mce_release_notes.md#deprecations-removals-cluster-mce) to learn more.

3.  Run the following command to apply the file:

        oc apply -f -

    You have now enabled the `ManagedServiceAccount` plug-in for your managed cluster. See the following steps to configure a `ManagedServiceAccount`.

4.  Create a `ManagedServiceAccount` custom resource with the following YAML source:

    ``` yaml
    apiVersion: authentication.open-cluster-management.io/v1alpha1
    kind: ManagedServiceAccount
    metadata:
      name: <managedserviceaccount_name>
      namespace: <target_managed_cluster>
    spec:
      rotation: {}
    ```

    - Replace `managed_serviceaccount_name` with the name of your `ManagedServiceAccount`.

    - Replace `target_managed_cluster` with the name of the managed cluster to which you are applying the `ManagedServiceAccount`.

5.  To verify, view the `tokenSecretRef` attribute in the `ManagedServiceAccount` object status to find the secret name and namespace. Run the following command with your account and cluster name:

    ``` bash
    oc get managedserviceaccount <managed_serviceaccount_name> -n <target_managed_cluster> -o yaml
    ```

6.  View the `Secret` containing the retrieved token that is connected to the created `ServiceAccount` on the managed cluster. Run the following command:

    ``` bash
    oc get secret <managed_serviceaccount_name> -n <target_managed_cluster> -o yaml
    ```

<a id="config-klusterlet-nodes"></a>

### Configure the klusterlet to run on specific nodes

When you create a cluster using Red Hat Advanced Cluster Management for Kubernetes, you can specify which nodes you want to run the managed cluster klusterlet by configuring the `nodeSelector` and `tolerations` annotation for the managed cluster.

This is an optional procedure. Complete the following steps to configure these settings.

<div>

<div class="title">

Procedure

</div>

1.  Select the managed cluster that you want to update from the Clusters page in the console.

2.  Set the **YAML** switch to **On** to view the YAML content.

    **Note:** The YAML editor is only available when importing or creating a cluster. To edit the managed cluster YAML definition after importing or creating, you must use the OpenShift Container Platform command-line interface or the Red Hat Advanced Cluster Management search feature.

3.  Add the `nodeSelector` annotation to the managed cluster YAML definition. The key for this annotation is: `open-cluster-management/nodeSelector`. The value of this annotation is a string map with JSON formatting.

4.  Add the `tolerations` entry to the managed cluster YAML definition. The key of this annotation is: `open-cluster-management/tolerations`. The value of this annotation represents a [toleration](https://github.com/kubernetes/api/blob/release-1.24/core/v1/types.go#L3007) list with JSON formatting. The resulting YAML might resemble the following example:

    ``` yaml
    apiVersion: cluster.open-cluster-management.io/v1
    kind: ManagedCluster
    metadata:
      annotations:
        open-cluster-management/nodeSelector: '{"dedicated":"acm"}'
        open-cluster-management/tolerations: '[{"key":"dedicated","operator":"equal","value":"acm","effect":"NoSchedule"}]'
    ```

5.  To make sure that you can deploy your content to the correct nodes, see [Set up the *AddOnDeploymentConfig* to configure klusterlet add-ons](add-ons.md#setting-addondeploymentconfig-klusterlet-addons).

</div>

<a id="remove-managed-cluster"></a>

## Cluster removal overview

When you remove an OpenShift Container Platform cluster from management that was created with multicluster engine operator, you can either *detach* it or *destroy* it. Detaching a cluster removes it from management, but does not completely delete it. You can import it again if you want to manage it. This is only an option when the cluster is in a *Ready* state.

The following procedures remove a cluster from management in either of the following situations:

- You already deleted the cluster and want to remove the deleted cluster from Red Hat Advanced Cluster Management.

- You want to remove the cluster from management, but have not deleted the cluster.

**Important:**

- Destroying a cluster removes it from management and deletes the components of the cluster.

- When you detach or destroy a managed cluster, the related namespace is automatically deleted. Do not place custom resources in this namespace.

Continue reading the following topics to learn how to remove a cluster from management:

- [Remove a cluster by using the console](clusters.md#remove-a-cluster-by-using-the-console)

- [Remove a cluster by using the command line](clusters.md#remove-a-cluster-by-using-the-cli)

- [Considerations for removing a cluster by using the command line](clusters.md#remove-cluster-cli-considerations)

- [Remove remaining resources after removing a cluster](clusters.md#removing-a-cluster-from-management-in-special-cases)

- [Defragment the etcd database after removing a cluster](clusters.md#defragmenting-the-hub-cluster-etcd-database)

<a id="remove-a-cluster-by-using-the-console"></a>

### Remove a cluster by using the console

Detach or destroy a managed cluster by using the console. Detaching managed clusters allows you to move the managed cluster to a different hub cluster, or re-import the managed cluster into a different cluster set.

<div>

<div class="title">

Procedure

</div>

- From the navigation menu, navigate to **Infrastructure** \> **Clusters** and select **Destroy cluster** or **Detach cluster** from the options menu beside the cluster that you want to remove from management.

  **Note:** You can detach or destroy multiple clusters by selecting the check boxes of the clusters that you want to detach or destroy and selecting **Detach** or **Destroy**.

</div>

<a id="remove-a-cluster-by-using-the-cli"></a>

### Remove a cluster by using the command line

Detach or destroy a managed cluster by using the command line. Detaching managed clusters allows you to move the managed cluster to a different hub cluster, or re-import the managed cluster into a different cluster set.

<div>

<div class="title">

Procedure

</div>

1.  To detach a managed cluster by using the command line of the hub cluster, run the following command:

    ``` bash
    oc delete managedcluster <cluster_name>
    ```

2.  To destroy the managed cluster after detaching, run the following command:

    ``` bash
    oc delete clusterdeployment <cluster_name> -n $CLUSTER_NAME
    ```

</div>

<div>

<div class="title">

Additional resources

</div>

- [Considerations for removing a cluster by using the command line](clusters.md#remove-cluster-cli-considerations)

</div>

<a id="remove-cluster-cli-considerations"></a>

### Considerations for removing a cluster by using the command line

To prevent destroying the managed cluster, set the `spec.preserveOnDelete` parameter to `true` in the `ClusterDeployment` custom resource.

The default setting of `disableHubSelfManagement` is `false`. The `false` setting causes the hub cluster, which is the `local-cluster`, to reimport and manage itself when it is detached and it reconciles the `MultiClusterHub` controller.

The detachment and reimport process might take hours for the hub cluster to complete. If you want to reimport the hub cluster without waiting for the processes to finish, you can enter the following command to restart the `multiclusterhub-operator` pod and reimport faster:

``` bash
oc -n open-cluster-management delete -l name=multiclusterhub-operator pods
```

You can change the value of the hub cluster to not import automatically by changing the `disableHubSelfManagement` value to `true`. See [Installing while connected online](clusters.md#installing-while-connected-online-mce).

If you attempt to detach the hub cluster, which is named `<your-local-cluster-name>`, be aware that the default setting of `disableHubSelfManagement` is `false` and the hub cluster is the `local-cluster`, which manages itself.

This setting causes the hub cluster to reimport itself and manage itself when it is detached, and it reconciles the `MultiClusterHub` controller. It might take hours for the hub cluster to complete the detachment process and reimport.

<a id="removing-a-cluster-from-management-in-special-cases"></a>

### Remove remaining resources after removing a cluster

Remove remaining resources from a managed cluster after you detach it if components were not cleaned up automatically. Situations when these extra steps are required include the following examples:

- The managed cluster was detached before it was completely created, and components like the `klusterlet` remain on the managed cluster.

- The hub that was managing the cluster was lost or destroyed before detaching the managed cluster, and there is no way to detach the managed cluster from the hub.

- The managed cluster was not in an online state when it was detached.

If one of these situations apply to your attempted detachment of a managed cluster, there are some resources that cannot be removed from managed cluster. Complete the following steps to detach the managed cluster:

<div>

<div class="title">

Prerequisites

</div>

- You have the `oc` command line interface configured.

- You have `KUBECONFIG` configured on your managed cluster.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Remove the `klusterlet` custom resource by using the following command:

    ``` bash
    oc get klusterlet | grep klusterlet | awk '{print $1}' | xargs oc patch klusterlet --type=merge -p '{"metadata":{"finalizers": []}}'
    ```

2.  Run the following command to remove the remaining resources:

    ``` bash
    oc delete namespaces open-cluster-management-agent open-cluster-management-agent-addon --wait=false
    oc get crds | grep open-cluster-management.io | awk '{print $1}' | xargs oc delete crds --wait=false
    oc get crds | grep open-cluster-management.io | awk '{print $1}' | xargs oc patch crds --type=merge -p '{"metadata":{"finalizers": []}}'
    ```

3.  Run the following command to ensure that both namespaces and all open cluster management `crds` are removed:

    ``` bash
    oc get crds | grep open-cluster-management.io | awk '{print $1}'
    oc get ns | grep open-cluster-management-agent
    ```

</div>

<a id="defragmenting-the-hub-cluster-etcd-database"></a>

### Defragment the etcd database after removing a cluster

Defragment the `etcd` database on the hub cluster after you remove a managed cluster to reclaim disk space.

Having many managed clusters can affect the size of the `etcd` database in the hub cluster. In OpenShift Container Platform 4.8, when you delete a managed cluster, the `etcd` database in the hub cluster is not automatically reduced in size.

In some scenarios, the `etcd` database can run out of space. An error `etcdserver: mvcc: database space exceeded` is displayed. To correct this error, reduce the size of the `etcd` database by compacting the database history and defragmenting the `etcd` database.

**Note:** For OpenShift Container Platform version 4.9 and later, the etcd Operator automatically defragments disks and compacts the `etcd` history. No manual intervention is needed. The following procedure is for OpenShift Container Platform version 4.8 and earlier.

<div>

<div class="title">

Prerequisites

</div>

- Install the OpenShift CLI (`oc`).

- Log in as a user with `cluster-admin` privileges.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Open a remote shell session to the `etcd` member. Run the following command:

    ``` bash
    oc rsh -n openshift-etcd etcd-control-plane-0.example.com etcdctl endpoint status --cluster -w table
    ```

2.  Run the following command to compact the `etcd` history:

    ``` bash
    sh-4.4#etcdctl compact $(etcdctl endpoint status --write-out="json" |  egrep -o '"revision":[0-9]*' | egrep -o '[0-9]*' -m1)
    ```

    The output might resemble the following example:

    ``` bash
    compacted revision 158774421
    ```

3.  Defragment the `etcd` database and clear any `NOSPACE` alarms as outlined in [Defragmenting `etcd` data](https://docs.redhat.com/en/documentation/openshift_container_platform/4.20/html/scalability_and_performance/recommended-performance-and-scalability-practices-2#etcd-defrag_recommended-etcd-practices).

</div>

<a id="discovery-intro"></a>

## Discovery service

You can discover OpenShift Container Platform clusters that are available from [OpenShift Cluster Manager](https://docs.redhat.com/en/documentation/openshift_cluster_manager/1-latest). After discovery, you can import your clusters to manage. The Discovery services uses the Discover Operator for back-end and console usage.

You must have an OpenShift Cluster Manager credential. See [Creating a credential for OpenShift Cluster Manager](clusters.md#creating-a-credential-for-openshift-cluster-manager) if you need to create a credential.

**Required access**: Administrator

- [Authenticating service accounts](clusters.md#discovery-auth)

- [List of the deployed components](clusters.md#discovery-auth-permissions)

- [Configure Discovery with the console](clusters.md#discovery-console)

- [Configure Discovery using the CLI](clusters.md#discovery-enable-cli)

- [Importing discovered Red Hat OpenShift Service on AWS (classic) and hosted control plane clusters by using the console](clusters.md#discovery-import-console)

- [Importing discovered Red Hat OpenShift Service on AWS (classic) and hosted control plane clusters by using the CLI](clusters.md#discovery-import-cli)

<a id="discovery-auth"></a>

### Authenticating service accounts

To discover OpenShift Container Platform clusters that are available from [OpenShift Cluster Manager](https://docs.redhat.com/en/documentation/openshift_cluster_manager/1-latest), you need to authenticate with a service account. Note that OpenShift Cluster Manager offline token is deprecated. See the following procedure to authenticate with a service account.

<div>

<div class="title">

Prerequisites

</div>

- You must have an OpenShift Cluster Manager credential. See [Creating a credential for OpenShift Cluster Manager](clusters.md#creating-a-credential-for-openshift-cluster-manager) if you need to create a credential.

- Learn about creating an OpenShift Cluster Manager service account at [Service accounts](https://docs.redhat.com/en/documentation/red_hat_hybrid_cloud_console/1-latest/html/creating_and_managing_service_accounts/con-ciam-svc-acct-intro-creating-service-acct).

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create a new credentials secret as a service-account `client-id` and `client-secret` pair in the multicluster engine operator console.

2.  Specify a service account `client-id` and `client-secret` pair so that the multicluster engine operator Discovery service can authenticate correctly and discover clusters.

3.  Set up the Red Hat OpenShift Service on AWS (classic) `DiscoveredCluster` resource for import as a managed cluster. The Red Hat OpenShift Service on AWS (classic) import flow that is initiated uses the service-account credentials authenticate and import the cluster.

</div>

<a id="discovery-auth-permissions"></a>

### Deployed components

When you authenticate with a service account, the Discovery service deploys components with the following access permissions.

| Role | Access permissions |
|----|----|
| OpenShift Cluster Manager cluster autoscaler editor | Perform update operations on the cluster autoscaler |
| OpenShift Cluster Manager cluster editor | Perform update operations on clusters |
| OpenShift Cluster Manager cluster provisioner | Perform provision operations on clusters |
| OpenShift Cluster Manager cluster viewer | Perform read operations on clusters |
| OpenShift Cluster Manager IdP editor | Perform update operations on IdPs |
| OpenShift Cluster Manager machine pool editor | Perform update operations on machine pools |
| OpenShift Cluster Manager organization administrator | Perform all available operations on the associated organization’s clusters |
| Subscriptions viewer | Perform read operations on any Subscriptions resource. |

List of the deployed components

<a id="discovery-console"></a>

### Configure Discovery with the console

Configure Discovery in the console to find clusters. When you configure the Discovery feature on your cluster, you must enable a `DiscoveryConfig` resource to connect to the OpenShift Cluster Manager to begin discovering clusters that are a part of your organization. You can create multiple `DiscoveryConfig` resources with separate credentials.

After you discover clusters, you can import clusters that appear in the *Discovered clusters* tab of the console. Use the product console to enable Discovery.

**Required access**: Access to the namespace where the credential was created.

<div>

<div class="title">

Prerequisites

</div>

- You need a credential. See [Creating a credential for OpenShift Cluster Manager](clusters.md#creating-a-credential-for-openshift-cluster-manager) to connect to OpenShift Cluster Manager.

- You need access to the namespaces that were used to configure Discovery.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Manually import discovered clusters from the console. To import other infrastructure provider discovered clusters, complete the following steps:

    1.  Go to the existing *Clusters* page and click the **Discovered clusters** tab.

    2.  From the *Discovered clusters* table, find the cluster that you want to import.

    3.  From the options menu, choose **Import cluster**.

    4.  For discovered clusters, you can import manually using the documentation, or you can choose Import clusters automatically.

    5.  To import automatically with your credentials or `kubeconfig` file, copy and paste the content.

    6.  Click **Import**.

2.  View and search discovered clusters in the console after you set up your credentials.

    1.  Click **Clusters** \> **Discovered clusters**.

    2.  View the populated table with the following information:

        - *Name* is the display name that is designated in OpenShift Cluster Manager. If the cluster does not have a display name, a generated name based on the cluster console URL is displayed. If the console URL is missing or was modified manually in OpenShift Cluster Manager, the cluster external ID is displayed.

        - *Namespace* is the namespace where you created the credential and discovered clusters.

        - *Type* is the discovered cluster OpenShift Container Platform platform type.

        - *Distribution version* is the discovered cluster Red Hat OpenShift version.

        - *Infrastructure provider* is the cloud provider of the discovered cluster.

        - *Last active* is the last time the discovered cluster was active.

        - *Created* when the discovered cluster was created.

        - *Discovered* when the discovered cluster was discovered.

3.  You can search for any information in the table, as well. For example, to show only *Discovered clusters* in a particular namespace, search for that namespace.

4.  You can now click **Import cluster** to create managed clusters.

</div>

<a id="discovery-enable-cli"></a>

### Enable Discovery using the CLI

Enable discovery using the CLI to find clusters that are available from OpenShift Cluster Manager.

**Required access**: Administrator

<div>

<div class="title">

Prerequisites

</div>

- Create a credential to connect to OpenShift Cluster Manager.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create a `DiscoveryConfig` resource that is named `discovery` in the same namespace as the selected `credential`. See the following `DiscoveryConfig` sample:

    ``` yaml
    apiVersion: discovery.open-cluster-management.io/v1
    kind: DiscoveryConfig
    metadata:
      name: discovery
      namespace: <NAMESPACE_NAME>
    spec:
      credential: <SECRET_NAME>
      filters:
        lastActive: 7
        openshiftVersions:
        - "4.x"
    ```

2.  Replace `SECRET_NAME` with the credential that you previously set up.

3.  Replace `NAMESPACE_NAME` with the namespace of `SECRET_NAME`.

4.  Enter the maximum time since last activity of your clusters (in days) to discover. For example, with `lastActive: 7`, clusters that active in the last 7 days are discovered.

5.  Enter the versions of OpenShift Container Platform clusters to discover as a list of strings. **Note:** Every entry in the `openshiftVersions` list specifies the major and minor version. For example, specifying `4.x` includes all errata releases, such as `4.x.1`, `4.x.2`.

6.  View discovered clusters by running `oc get discoveredclusters -n <namespace>` where `namespace` is the namespace where the discovery credential exists. You can use the same command to view the region if you have a region set. Objects are created by the Discovery controller. These `DiscoveredClusters` represent the clusters that are found in OpenShift Cluster Manager by using the filters and credentials that are specified in the `DiscoveryConfig` `discoveredclusters.discovery.open-cluster-management.io` API. The value for `name` is the cluster external ID:

    ``` yaml
    apiVersion: discovery.open-cluster-management.io/v1
    kind: DiscoveredCluster
    metadata:
      name: <cluster-external-id>
      namespace: <NAMESPACE_NAME>
    spec:
      activity_timestamp: "2022-04-19T21:06:14Z"
      cloudProvider: vsphere
      console: https://console-openshift-console.apps.qe1-vmware-pkt.dev02.red-chesterfield.com
      creation_timestamp: "2022-04-19T16:29:53Z"
      credential:
        apiVersion: v1
        kind: Secret
        name: <SECRET_NAME>
        namespace: <NAMESPACE_NAME>
      display_name: qe1-vmware-pkt.dev02.red-chesterfield.com
      name: <cluster-external-id>
      openshiftVersion: 4.x
      status: Stale
    ```

</div>

<a id="discovery-import-console"></a>

### Importing discovered Red Hat OpenShift Service on AWS (classic) and hosted control plane clusters by using the console

Automatically import supported clusters into your hub cluster with the `Discovery-Operator` for faster cluster management, without manually importing individual clusters. The following procedure is an example of how to import your discovered Red Hat OpenShift Service on AWS (classic) and hosted control planes clusters automatically by using the `Discovery-Operator` from the console. You must modify the resource and set the `importAsManagedCluster` field to `true` in the console.

**Required access:** Cluster administrator

<div>

<div class="title">

Prerequisites

</div>

- Discovery is enabled by default. If you changed default settings, you need to enable Discovery.

- You must set up the Red Hat OpenShift Service on AWS (classic) command-line interface. See [Getting started with the Red Hat OpenShift Service on AWS (classic) CLI](https://docs.redhat.com/en/documentation/red_hat_openshift_service_on_aws/4/html/rosa_cli/rosa-get-started-cli#rosa-get-started-cli) documentation.

</div>

**Important:** For other Kubernetes providers, you must import these infrastructure provider `DiscoveredCluster` resources manually. Directly apply Kubernetes configurations to the other types of `DiscoveredCluster` resources. If you enable the `importAsManagedCluster` field from the `DiscoveredCluster` resource, it is not imported due to the Discovery webhook.

<div>

<div class="title">

Procedure

</div>

1.  Log in to your hub cluster from the console.

2.  Select **Search** from the navigation menu.

3.  From the search bar, enter the following query: "DiscoveredCluster".

4.  The `DiscoveredCluster` resource results appear.

5.  Go to the `DiscoveredCluster` resource and set `importAsManagedCluster` to `true`. See the following example, where `importAsManagedCluster` is set to `true` and `<4.x.z>` is your supported OpenShift Container Platform version:

    ``` yaml
    apiVersion: discovery.open-cluster-management.io/v1
    kind: DiscoveredCluster
    metadata:
      name: 28c17977-fc73-4050-b5cc-a5aa2d1d6892
      namespace: discovery
    spec:
      openshiftVersion: <4.x.z>
      isManagedCluster: false
      cloudProvider: aws
      name: 28c17977-fc73-4050-b5cc-a5aa2d1d6892
      displayName: rosa-dc
      status: Active
      importAsManagedCluster: true
      type: <supported-type>
    ```

    - By setting the field to `true`, the `Discovery-Operator` imports the `DiscoveredCluster` resource, creates a `ManagedCluster` resource and if the Red Hat Advanced Cluster Management is installed, creates the `KlusterletAddOnConfig` resource. It also creates the `Secret` resources for your automatic import.

    - You must use `ROSA` or `MultiClusterEngineHCP` as the parameter value.

6.  To verify that the `DiscoveredCluster` resource is imported, go to the **Clusters** page. Check the import status of your cluster from the *Cluster list* tab.

7.  If you want to detach managed clusters for Discovery to prevent automatic reimport, select the **Detach cluster** option. The `Discovery-Operator` adds the following annotation, `discovery.open-cluster-management.io/previously-auto-imported: 'true'`.

    Your `DiscoveredCluster` resource might resemble the following YAML:

    ``` yaml
    apiVersion: discovery.open-cluster-management.io/v1
    kind: DiscoveredCluster
    metadata:
      annotations:
        discovery.open-cluster-management.io/previously-auto-imported: 'true'
    ```

8.  To verify that the `DiscoveredCluster` resource is not reimported automatically, check for the following message in the `Discovery-Operator` logs, where `"rosa-dc"` is this discovered cluster:

    ``` bash
    2024-06-12T14:11:43.366Z INFO reconcile  Skipped automatic import for DiscoveredCluster due to
    existing 'discovery.open-cluster-management.io/previously-auto-imported' annotation {"Name": "rosa-dc"}
    ```

    **Note:** If you want to reimport the `DiscoveredCluster` resource automatically, you must remove the previously mentioned annotation.

</div>

<a id="discovery-import-cli"></a>

### Importing discovered Red Hat OpenShift Service on AWS (classic) and hosted control plane clusters by using the CLI

Automatically import supported clusters into your hub cluster with the `Discovery-Operator` for faster cluster management, without manually importing individual clusters. The following procedure is an example of how to import your discovered Red Hat OpenShift Service on AWS (classic) and hosted control planes clusters automatically by using the `Discovery-Operator` from the command-line interface.

**Required access:** Cluster administrator

<div>

<div class="title">

Prerequisites

</div>

- Discovery is enabled by default. If you changed default settings, you need to enable Discovery.

- You must set up the Red Hat OpenShift Service on AWS (classic) command-line interface. See [Getting started with the Red Hat OpenShift Service on AWS (classic) CLI](https://docs.redhat.com/en/documentation/red_hat_openshift_service_on_aws/4/html/rosa_cli/rosa-get-started-cli#rosa-get-started-cli) documentation.

</div>

**Important:** For other Kubernetes providers, you must import these infrastructure provider `DiscoveredCluster` resources manually. Directly apply Kubernetes configurations to the other types of `DiscoveredCluster` resources. If you enable the `importAsManagedCluster` field from the `DiscoveredCluster` resource, it is not imported due to the Discovery webhook.

<div>

<div class="title">

Procedure

</div>

1.  To automatically import the `DiscoveredCluster` resource from the command-line interface. Set the `importAsManagedCluster` paramater to `true` by using the following command after you log in. Replace `<name>` and `<namespace>` with your name and namespace:

    ``` bash
    oc patch discoveredcluster <name> -n <namespace> --type='json' -p='[{"op": "replace", "path": "/spec/importAsManagedCluster", "value": true}]'
    ```

2.  Run the following command to verify that the cluster was imported as a managed cluster:

    ``` bash
    oc get managedcluster <name>
    ```

3.  To get a description of your Red Hat OpenShift Service on AWS (classic) cluster ID, run the following command from the Red Hat OpenShift Service on AWS (classic) command-line interface:

    ``` bash
    rosa describe cluster --cluster=<cluster-name> | grep -o ^ID:.*
    ```

</div>

<a id="cim-intro"></a>

## Host inventory introduction

The host inventory management and on-premises cluster installation are available using the multicluster engine operator central infrastructure management feature.

Continue reading to learn more about host inventories and central infrastructure management:

- [Host inventory overview](clusters.md#cim-overview)

- [Enabling the central infrastructure management service](clusters.md#enable-cim)

- [Enabling central infrastructure management on Amazon Web Services](clusters.md#enable-cim-aws)

- [Creating a host inventory by using the console](clusters.md#create-host-inventory-console)

- [Creating a host inventory by using the command line interface](clusters.md#create-host-inventory-cli)

- [Configuring advanced networking for an infrastructure environment](clusters.md#cim-network-config)

- [Adding hosts to the host inventory by using the console](clusters.md#add-host-host-inventory-console)

- [Adding bare metal hosts to the host inventory by using the console](clusters.md#add-hosts-console)

- [Managing your host inventory](clusters.md#manage-host-inv)

- [Enabling hub cluster management by using central infrastructure management](clusters.md#enable-hub-manage-cim)

- [Configuring mirror registries for each cluster](clusters.md#config-mirror-reg-cluster)

- [Configuring third-party CNI plugins for on-premises cluster installation (Technology Preview)](clusters.md#config-third-party-cni-on-prem)

- [Create a cluster in an on-premises environment by using the CLI](clusters.md#create-a-cluster-on-premises-cli)

- [Import an on-premises OpenShift Container Platform cluster manually by using central infrastructure management](clusters.md#import-ocp-cluster)

- [Installing a two nodes with fencing cluster with Assisted Installer (Technology Preview)](clusters.md#install-tnf-cluster-ai) to learn more.

<a id="cim-overview"></a>

### Host inventory overview

The central infrastructure management feature is an Red Hat OpenShift Container Platform install experience in multicluster engine operator that focuses on managing bare-metal hosts during their lifecycle.

The Assisted Installer is an install method for OpenShift Container Platform that uses agents to run pre-installation validations on the target hosts, and a central service to evaluate and track install progress.

The infrastructure operator for Red Hat OpenShift is a multicluster engine operator component that manages and installs the workloads that run the Assisted Installer service.

If you are using standalone multicluster engine operator, you can use central infrastructure management features, such as deploying managed clusters. If you need additional features, such as SiteConfig operator or policy-based governance, you need to [install Red Hat Advanced Cluster Management for Kubernetes](get_started.md#prepare-install-acm), which automatically installs the multicluster engine operator.

Use the console to create a host inventory, which is a pool of bare-metal or virtual machines that you can use to create on-premises OpenShift Container Platform clusters. These clusters can be standalone, with dedicated machines for the control plane, or hosted control planes, where the control plane runs as pods on a hub cluster. See *Hosted control planes overview* in the additional resources section for more details.

You can install standalone clusters by using the console, API, or GitOps by using Zero Touch Provisioning (ZTP). See *Installing GitOps ZTP in a disconnected environment* in the additional resources section for more information on ZTP.

A machine joins the host inventory after booting with a Discovery Image. The Discovery Image is a Red Hat CoreOS live image that contains the following:

- An agent that performs discovery, validation, and installation tasks.

- The necessary configuration for reaching the service on the hub cluster, including the endpoint, token, and static network configuration, if applicable.

You have one Discovery Image for each infrastructure environment, which is a set of hosts sharing a common set of properties. The `InfraEnv` custom resource definition represents this infrastructure environment and associated Discovery Image. You can specify the Red Hat Core OS version used for the Discovery Image by setting the `osImageVersion` field in the `InfraEnv` custom resource. If you do not specify a value, the latest Red Hat Core OS version is used.

After the host boots and the agent contacts the service, the service creates a new `Agent` custom resource on the hub cluster representing that host. The `Agent` resources make up the host inventory.

You can install hosts in the inventory as OpenShift nodes later. The agent writes the operating system to the disk, along with the necessary configuration, and reboots the host.

**Note:** Red Hat Advanced Cluster Management and central infrastructure management supports the Nutanix platform by using the `AgentClusterInstall` resource, which requires additional configuration by creating the Nutanix virtual machines. To learn more, see [Optional: Installing on Nutanix](https://docs.redhat.com/en/documentation/assisted_installer_for_openshift_container_platform/2025/html/installing_openshift_container_platform_with_the_assisted_installer/assembly_installing-on-nutanix) in the Assisted Installer documentation.

<div>

<div class="title">

Additional resources

</div>

- [Hosted control planes overview](https://docs.redhat.com/en/documentation/openshift_container_platform/4.20/html/hosted_control_planes/hosted-control-planes-overview)

- [Installing GitOps ZTP in a disconnected environment](https://docs.redhat.com/en/documentation/openshift_container_platform/4.20/html-single/scalability_and_performance/index#installing-disconnected-rhacm_ztp-preparing-the-hub-cluster)

</div>

<a id="enable-cim"></a>

### Enabling the central infrastructure management service

The central infrastructure management service is provided with the multicluster engine operator and deploys OpenShift Container Platform clusters. The central infrastructure management service is deployed automatically if you installed Red Hat Advanced Cluster Management and enabled the `MultiClusterHub` Operator on the hub cluster, but you have to enable the service manually in this case.

<div>

<div class="title">

Prerequisites

</div>

- You must have a deployed hub cluster on a supported OpenShift Container Platform version and a supported Red Hat Advanced Cluster Management for Kubernetes version.

- You need internet access for your hub cluster.

- If you are working in a disconnected environment, you need a connection to an internal or mirror registry that has a connection to the internet to retrieve the required images for creating the environment.

- You must open the required ports for bare metal provisioning. See [Ensuring required ports are open](https://docs.redhat.com/en/documentation/openshift_container_platform/4.20/html-single/installing_on_bare_metal/index#network-requirements-ensuring-required-ports-are-open_ipi-install-prerequisites) in the OpenShift Container Platform documentation.

- You need a bare metal host custom resource definition.

- You need an OpenShift Container Platform [pull secret](https://console.redhat.com/openshift/install/pull-secret). See *Using image pull secrets* for more information.

- You need a configured default storage class.

- For disconnected environments only, complete the procedure for [Clusters at the network far edge](https://docs.redhat.com/en/documentation/openshift_container_platform/4.20/html/edge_computing/ztp-deploying-far-edge-clusters-at-scale#ztp-acm-preparing-to-install-disconnected-acm_ztp-deploying-disconnected) in the OpenShift Container Platform documentation.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Check if you already have a bare metal host custom resource definition by running the following command:

    ``` bash
    oc get crd baremetalhosts.metal3.io
    ```

    - If you have a bare metal host custom resource definition, the output shows the date when the resource was created.

    - If you do not have the resource, you receive an error that resembles the following:

    ``` bash
    Error from server (NotFound): customresourcedefinitions.apiextensions.k8s.io "baremetalhosts.metal3.io" not found
    ```

2.  If you do not have a bare metal host custom resource definition, download the [metal3.io_baremetalhosts.yaml](https://raw.githubusercontent.com/openshift/baremetal-operator/master/config/base/crds/bases/metal3.io_baremetalhosts.yaml) file and apply the content by running the following command to create the resource:

    ``` bash
    oc apply -f metal3.io_baremetalhosts.yaml
    ```

3.  Check if you have the `Provisioning` resource by running the following command:

    ``` bash
    oc get provisioning
    ```

4.  If you already have a `Provisioning` resource, and if your hub cluster is installed on Bare metal, Red Hat OpenStack Platform, VMware vSphere, or User-provisioned infrastructure (UPI) and the platform is `None`, modify the `Provisioning` resource to allow the Bare Metal Operator to watch all namespaces. Run the following command:

    ``` bash
    oc patch provisioning provisioning-configuration --type merge -p '{"spec":{"watchAllNamespaces": true }}'
    ```

    **Note:** If your hub cluster is installed on a different platform, continue at [Enabling central infrastructure management in disconnected environments](https://docs.redhat.com/en/documentation/red_hat_advanced_cluster_management_for_kubernetes/2.17/html/clusters/index) or [Enabling central infrastructure management in connected environments](https://docs.redhat.com/en/documentation/red_hat_advanced_cluster_management_for_kubernetes/2.17/html/clusters/index).

5.  If you do not have a `Provisioning` resource, you receive a `No resources found` error. Create the following `Provisioning` resource YAML file. Skip this step if you previously modified your `Provisioning` resource:

    ``` yaml
    apiVersion: metal3.io/v1alpha1
    kind: Provisioning
    metadata:
      name: provisioning-configuration
    spec:
      provisioningNetwork: "Disabled"
      watchAllNamespaces: true
    ```

6.  Apply the content by running the following command. Skip this step if you previously modified your `Provisioning` resource:

    ``` bash
    oc apply -f provisioning-configuration.yaml
    ```

</div>

<div>

<div class="title">

Additional resources

</div>

- [Challenges of the network far edge](https://docs.redhat.com/en/documentation/openshift_container_platform/4.20/html/edge_computing/ztp-deploying-far-edge-clusters-at-scale#ztp-deploying-far-edge-clusters-at-scale)

- [Using image pull secrets](https://docs.redhat.com/en/documentation/openshift_container_platform/4.20/html/images/managing-images#using-image-pull-secrets)

</div>

<a id="enable-cim-aws"></a>

### Enabling central infrastructure management on Amazon Web Services

If you are running your hub cluster on Amazon Web Services and want to enable the central infrastructure management service, complete the following procedure.

<div>

<div class="title">

Prerequisites

</div>

- Complete the steps in [Enabling the central infrastructure management service](clusters.md#enable-cim).

</div>

<div>

<div class="title">

Procedure

</div>

1.  Make sure you are logged in at the hub cluster and find the unique domain configured on the `assisted-image-service` by running the following command:

    ``` bash
    oc get routes --all-namespaces | grep assisted-image-service
    ```

    Your domain might resemble the following example: `assisted-image-service-multicluster-engine.apps.<yourdomain>.com`

2.  Make sure you are logged in at the hub cluster and create a new `IngressController` with a unique domain using the `NLB` `type` parameter. Add `<yourdomain>` to the `domain` parameter in `IngressController` by replacing `<domain>` in `nlb-apps.<domain>.com` with `<yourdomain>`. See the following example:

    ``` yaml
    apiVersion: operator.openshift.io/v1
    kind: IngressController
    metadata:
      name: ingress-controller-with-nlb
      namespace: openshift-ingress-operator
    spec:
      domain: nlb-apps.<domain>.com
      routeSelector:
          matchLabels:
            router-type: nlb
      endpointPublishingStrategy:
        type: LoadBalancerService
        loadBalancer:
          scope: External
          providerParameters:
            type: AWS
            aws:
              type: NLB
    ```

3.  Apply the new `IngressController` by running the following command:

    ``` bash
    oc apply -f ingresscontroller.yaml
    ```

4.  Make sure that the value of the `spec.domain` parameter of the new `IngressController` is not in conflict with an existing `IngressController` by completing the following steps:

    1.  List all `IngressControllers` by running the following command:

        ``` bash
        oc get ingresscontroller -n openshift-ingress-operator
        ```

    2.  Run the following command on each of the `IngressControllers`, except the `ingress-controller-with-nlb` that you just created:

    ``` bash
    oc edit ingresscontroller <name> -n openshift-ingress-operator
    ```

    \+ **Notes:**

    \+

    - If the `spec.domain` report is missing, add a default domain that matches all of the routes that are exposed in the cluster except `nlb-apps.<domain>.com`.

    - If the `spec.domain` report is provided, make sure that the `nlb-apps.<domain>.com` route is excluded from the specified range.

5.  Edit the `assisted-image-service` route to use the `nlb-apps` location. The default namespace is where you installed the multicluster engine operator. Run the following command:

    ``` bash
    oc edit route assisted-image-service -n <namespace>
    ```

6.  Add the following lines to the `assisted-image-service` route:

    ``` yaml
    metadata:
      labels:
        router-type: nlb
      name: assisted-image-service
    ```

7.  In the `assisted-image-service` route, find the URL value of `spec.host`. The URL might resemble the following example:

        assisted-image-service-multicluster-engine.apps.<yourdomain>.com

8.  Replace `apps` in the URL with `nlb-apps` to match the domain configured in the new `IngressController`.

9.  To verify that the central infrastructure management service is enabled on Amazon Web Services, run the following command to verify that the pods are healthy:

    ``` bash
    oc get pods -n multicluster-engine | grep assist
    ```

10. Create a new host inventory and ensure that the download URL uses the new `nlb-apps` URL.

</div>

<a id="create-host-inventory-console"></a>

### Creating a host inventory by using the console

You can create a host inventory (infrastructure environment) to discover physical or virtual machines that you can install your OpenShift Container Platform clusters on.

<div>

<div class="title">

Prerequisites

</div>

- You must enable the central infrastructure management service. See [Enabling the central infrastructure management service](clusters.md#enable-cim) for more information.

</div>

<div>

<div class="title">

Procedure

</div>

1.  From the console, navigate to **Infrastructure** \> **Host inventory** and click **Create infrastructure environment**.

2.  Add the required information to your host inventory settings. See [Host inventory console settings](clusters.md#host-inventory-console-settings) for more information about the settings.

3.  **Optional:** If you want to enable proxy settings for your hosts, select the setting to enable it.

</div>

<div class="formalpara">

<div class="title">

Next steps

</div>

If you need advanced configuration options that are not available in the console, continue to [Creating a host inventory by using the command line interface](clusters.md#create-host-inventory-cli).

</div>

If you do not need advanced configuration options, you can continue by configuring static networking, if required, and begin adding hosts to your infrastructure environment.

<div>

<div class="title">

Additional resources

</div>

- [Creating a credential for a hosted environment](clusters.md#creating-a-credential-hosted)

- [Adding hosts to the host inventory by using the console](clusters.md#add-host-host-inventory-console)

- [Automatically adding bare metal hosts to the host inventory](clusters.md#add-hosts-console)

</div>

<a id="host-inventory-console-settings"></a>

### Host inventory console settings

When you create a host inventory (infrastructure environment), you can configure various settings in the console. See the following definition list to learn more:

- See the following list of host inventory console settings:

  Name  
  A unique name for your infrastructure environment. Creating an infrastructure environment by using the console also creates a new namespace for the `InfraEnv` resource with the name you chose. If you create `InfraEnv` resources by using the command line interface and want to monitor the resources in the console, use the same name for your namespace and the `InfraEnv`.

  Network type  
  Specifies if the hosts you add to your infrastructure environment use DHCP or static networking. Static networking configuration requires additional steps.

  Location  
  Specifies the geographic location of the hosts. The geographic location can be used to define which data center the hosts are located.

  Labels  
  Optional field where you can add labels to the hosts that are discovered with this infrastructure environment. The specified location is automatically added to the list of labels.

  Infrastructure provider credentials  
  Selecting an infrastructure provider credential automatically populates the pull secret and SSH public key fields with information in the credential. For more information, see *Creating a credential for an on-premises environment*.

  Pull secret  
  Your OpenShift Container Platform [pull secret](https://console.redhat.com/openshift/install/pull-secret) that enables you to access the OpenShift Container Platform resources. This field is automatically populated if you selected an infrastructure provider credential.

  SSH public key  
  The SSH key that enables the secure communication with the hosts. You can use it to connect to the host for troubleshooting. After installing a cluster, you can no longer connect to the host with the SSH key. The key is generally in your `id_rsa.pub` file. The default file path is `~/.ssh/id_rsa.pub`. This field is automatically populated if you selected an infrastructure provider credential that contains the value of a SSH public key.

  HTTP Proxy URL  
  The URL of the proxy for HTTP requests.

  HTTPS Proxy URL  
  The URL of the proxy for HTTP requests. The URL must start with HTTP. HTTPS is not supported. If you do not provide a value, your HTTP proxy URL is used by default for both HTTP and HTTPS connections.

  No Proxy domains  
  A list of domains separated by commas that you do not want to use the proxy with. Start a domain name with a period (`.`) to include all of the subdomains that are in that domain. Add an asterisk (`*`) to bypass the proxy for all destinations. Optionally add your own Network Time Protocol (NTP) sources by providing a comma-separated list of IP or domain names of the NTP pools or servers.

<div>

<div class="title">

Additional resources

</div>

- [Creating a credential for a hosted environment](clusters.md#creating-a-credential-hosted)

- [Adding hosts to the host inventory by using the console](clusters.md#add-host-host-inventory-console)

- [Automatically adding bare metal hosts to the host inventory](clusters.md#add-hosts-console)

</div>

<a id="create-host-inventory-cli"></a>

### Creating a host inventory by using the command line interface

You can create a host inventory (infrastructure environment) to discover physical or virtual machines that you can install your OpenShift Container Platform clusters on. Use the command line interface instead of the console for automated deployments, or for the following advanced configuration options:

- Automatically bind discovered hosts to an existing cluster definition

- Override the ignition configuration of the Discovery Image

- Control the iPXE behavior

- Modify kernel arguments for the Discovery Image

- Pass additional certificates that you want the host to trust during the discovery phase

- Select a Red Hat CoreOS version to boot for testing that is not the default option of the newest version

<div>

<div class="title">

Prerequisites

</div>

- You must enable the central infrastructure management service. See [Enabling the central infrastructure management service](clusters.md#enable-cim) for more information.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Log in to your hub cluster by running the following command:

    ``` bash
    oc login
    ```

2.  Create a namespace for your resource.

3.  Create a file named, `namespace.yaml`, and add the following content:

    ``` yaml
    apiVersion: v1
    kind: Namespace
    metadata:
      name: <your_namespace>
    ```

    - Use the same `name` for your namespace and your infrastructure environment to monitor your inventory in the console.

4.  Apply the YAML content by running the following command:

    ``` bash
    oc apply -f namespace.yaml
    ```

5.  Create a `Secret` custom resource containing your OpenShift Container Platform [pull secret](https://console.redhat.com/openshift/install/pull-secret).

6.  Create the `pull-secret.yaml` file. Add your namespace to the `name` field and add your pull secret to the `.dockerconfigjson:` field. View the following content:

    ``` yaml
    apiVersion: v1
    kind: Secret
    type: kubernetes.io/dockerconfigjson
    metadata:
      name: pull-secret
      namespace: <your_namespace>
    stringData:
      .dockerconfigjson: <your_pull_secret>
    ```

7.  Apply the YAML content by running the following command:

    ``` bash
    oc apply -f pull-secret.yaml
    ```

8.  Create the infrastructure environment by using the `infra-env.yaml` file and add the following content:

    ``` yaml
    apiVersion: agent-install.openshift.io/v1beta1
    kind: InfraEnv
    metadata:
      name: myinfraenv
      namespace: <your_namespace>
    spec:
      proxy:
        httpProxy: <http://user:password@ipaddr:port>
        httpsProxy: <http://user:password@ipaddr:port>
        noProxy:
      additionalNTPSources:
      sshAuthorizedKey:
      pullSecretRef:
        name: <name>
      agentLabels:
        <key>: <value>
      nmStateConfigLabelSelector:
        matchLabels:
          <key>: <value>
      clusterRef:
        name: <cluster_name>
        namespace: <project_name>
      ignitionConfigOverride: '{"ignition": {"version": "3.1.0"}, …}'
      cpuArchitecture: x86_64
      ipxeScriptType: DiscoveryImageAlways
      kernelArguments:
        - operation: append
          value: audit=0
      additionalTrustBundle: <bundle>
      osImageVersion: <version>
      ImageType: <type>
    ```

    - Replace `<namespace>` with the name of your namespace.

    - Replace the `proxy` values with your proxy information.

    - Replace `<name>` with the name of your pull secret.

    - Replace `<key>: <value>` with your key and value for your agent labels.

    - Replace `<cluster_name>` and `<project_name>` with the name and namespace of your `ClusterDeployment`

    - Replace `<bundle>` with your PEM-encoded X.509 certificate bundle.

    - Replace `<version>` with the Red Hat CoreOS image version.

    - Replace `<type>` with the ISO file type to download.

    **Note:** To learn more about the `infra-env.yaml` fields, see [*InfraEnv* custom resource field descriptions](clusters.md#infraenv-cr-field-desc).

9.  Apply the YAML content by running the following command:

    ``` bash
    oc apply -f infra-env.yaml
    ```

10. To verify that your host inventory is created, check the status with the following command:

    ``` bash
    oc describe infraenv myinfraenv -n <your_namespace>
    ```

    **Note:** If you modify the `InfraEnv` resource, make sure that the `InfraEnv` has created a new Discovery Image by looking at the `createdTime` property. If you already booted hosts, boot them again with the latest Discovery Image.

</div>

<div class="formalpara">

<div class="title">

Next steps

</div>

Continue by configuring static networking, if required, and begin adding hosts to your infrastructure environment.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Configuring advanced networking for an infrastructure environment](clusters.md#cim-network-config)

- [Enabling the central infrastructure management service](clusters.md#enable-cim)

</div>

<a id="infraenv-cr-field-desc"></a>

### *InfraEnv* custom resource field descriptions

When you create a host inventory (infrastructure environment) by using the command line interface, you create a `InfraEnv` custom resource. The `InfraEnv` resource defines the configuration for your host inventory, such as the pull secret, SSH public key, and proxy settings. See the following field descriptions in the `InfraEnv` table to learn more about the `infra-env.yaml` fields:

| Field | Optional or required | Description |
|----|----|----|
| `proxy` | Optional | Defines the proxy settings for agents and clusters that use the `InfraEnv` resource. If you do not set the `proxy` value, agents are not configured to use a proxy. |
| `httpProxy` | Optional | The URL of the proxy for HTTP requests. The URL must start with `http`. HTTPS is not supported.. |
| `httpsProxy` | Optional | The URL of the proxy for HTTP requests. The URL must start with `http`. HTTPS is not supported. |
| `noProxy` | Optional | A list of domains and CIDRs separated by commas that you do not want to use the proxy with. |
| `additionalNTPSources` | Optional | A list of Network Time Protocol (NTP) sources (hostname or IP) to add to all hosts. They are added to NTP sources that are configured by using other options, such as DHCP. |
| `sshAuthorizedKey` | Optional | SSH public keys that are added to all hosts for use in debugging during the discovery phase. The discovery phase is when the host boots the Discovery Image. |
| `name` | Required | The name of the Kubernetes secret containing your pull secret. |
| `agentLabels` | Optional | Labels that are automatically added to the `Agent` resources representing the hosts that are discovered with your `InfraEnv`. Make sure to add your key and value. |
| `nmStateConfigLabelSelector` | Optional | Consolidates advanced network configuration such as static IPs, bridges, and bonds for the hosts. The host network configuration is specified in one or more `NMStateConfig` resources with labels you choose. The `nmStateConfigLabelSelector` property is a Kubernetes label selector that matches your chosen labels. The network configuration for all `NMStateConfig` labels that match this label selector is included in the Discovery Image. When you boot, each host compares each configuration to its network interfaces and applies the appropriate configuration. To learn more about advanced network configuration, see *Configuring advanced networking for an infrastructure environment*. |
| `clusterRef` | Optional | References an existing `ClusterDeployment` resource that describes a standalone on-premises cluster. Not set by default. If `clusterRef` is not set, then the hosts can be bound to one or more clusters later. You can remove the host from one cluster and add it to another. If `clusterRef` is set, then all hosts discovered with your `InfraEnv` are automatically bound to the specified cluster. If the cluster is not installed yet, then all discovered hosts are part of its installation. If the cluster is already installed, then all discovered hosts are added. |
| `ignitionConfigOverride` | Optional | Modifies the ignition configuration of the Red Hat CoreOS live image, such as adding files. Make sure to only use `ignitionConfigOverride` if you need it. Must use ignition version 3.1.0, regardless of the cluster version. |
| `cpuArchitecture` | Optional | Choose one of the following supported CPU architectures: x86_64, aarch64, ppc64le, or s390x. The default value is x86_64. |
| `ipxeScriptType` | Optional | Causes the image service to always serve the iPXE script when set to the default value of `DiscoveryImageAlways` and when you are using iPXE to boot. As a result, the host boots from the network discovery image. Setting the value to `BootOrderControl` causes the image service to decide when to return the iPXE script, depending on the host state, which causes the host to boot from the disk when the host is provisioned and is part of a cluster. |
| `kernelArguments` | Optional | Allows modifying the kernel arguments for when the Discovery Image boots. Possible values for `operation` are `append`, `replace`, or `delete`. |
| `additionalTrustBundle` | Optional | A PEM-encoded X.509 certificate bundle, usually needed if the hosts are in a network with a re-encrypting man-in-the-middle (MITM) proxy, or if the hosts need to trust certificates for other purposes, such as container image registries. Hosts discovered by your `InfraEnv` trust the certificates in this bundle. Clusters created from the hosts discovered by your `InfraEnv` also trust the certificates in this bundle. |
| `osImageVersion` | Optional | The Red Hat CoreOS image version to use for your `InfraEnv`. Make sure the version refers to the OS image specified in either the `AgentServiceConfig.spec.osImages` or in the default OS images list. Each release has a specific set of Red Hat CoreOS image versions. The `OSImageVersion` must match an OpenShift Container Platform version in the OS images list. You cannot specify `OSImageVersion` and `ClusterRef` at the same time. If you want to use another version of the Red Hat CoreOS image that does not exist by default, then you must manually add the version by specifying it in the `AgentServiceConfig.spec.osImages`. To learn more about adding versions, see *Enabling the central infrastructure management service*. |
| `ImageType` | Optional | Selects the ISO file type to download. Possible options are `minimal-iso` or `full-iso`. If you do not specify an ISO type, the minimal ISO is used by default. The minimal ISO does not contain the root file system, `RootFS`. If you select a minimal ISO, the `RootFS` is downloaded later. |

*InfraEnv* field table

<div>

<div class="title">

Additional resources

</div>

- [Configuring advanced networking for an infrastructure environment](clusters.md#cim-network-config)

- [Enabling the central infrastructure management service](clusters.md#enable-cim)

</div>

<a id="cim-network-config"></a>

### Configuring advanced networking for an infrastructure environment

For hosts that require networking beyond DHCP on a single interface, you must configure advanced networking. The required configuration includes creating one or more instances of the `NMStateConfig` resource that describes the networking for one or more hosts.

Each `NMStateConfig` resource must contain a label that matches the `nmStateConfigLabelSelector` on your `InfraEnv` resource. See *Creating a host inventory by using the command line interface* to learn more about the `nmStateConfigLabelSelector`.

The Discovery Image contains the network configurations defined in all referenced `NMStateConfig` resources. After booting, each host compares each configuration to its network interfaces and applies the appropriate configuration.

<div>

<div class="title">

Prerequisites

</div>

- You must enable the central infrastructure management service. See [Enabling the central infrastructure management service](clusters.md#enable-cim) for more information.

- You must create a host inventory. See [Creating a host inventory by using the console](clusters.md#create-host-inventory-console) for more information.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create a file named `nmstateconfig.yaml` and add content that is similar to the following template. Add your `namespace` and `some-key` values:

    ``` yaml
    apiVersion: agent-install.openshift.io/v1beta1
    kind: NMStateConfig
    metadata:
      name: mynmstateconfig
      namespace: <your-infraenv-namespace>
      labels:
        some-key: <some-value>
    spec:
      config:
        interfaces:
          - name: eth0
            type: ethernet
            state: up
            mac-address: 02:00:00:80:12:14
            ipv4:
              enabled: true
              address:
                - ip: 192.168.111.30
                  prefix-length: 24
              dhcp: false
          - name: eth1
            type: ethernet
            state: up
            mac-address: 02:00:00:80:12:15
            ipv4:
              enabled: true
              address:
                - ip: 192.168.140.30
                  prefix-length: 24
              dhcp: false
        dns-resolver:
          config:
            server:
              - 192.168.126.1
        routes:
          config:
            - destination: 0.0.0.0/0
              next-hop-address: 192.168.111.1
              next-hop-interface: eth1
              table-id: 254
            - destination: 0.0.0.0/0
              next-hop-address: 192.168.140.1
              next-hop-interface: eth1
              table-id: 254
      interfaces:
        - name: "eth0"
          macAddress: "02:00:00:80:12:14"
        - name: "eth1"
          macAddress: "02:00:00:80:12:15"
    ```

    **Note:** The Image Service automatically creates a new image when you update any `InfraEnv` properties or change the `NMStateConfig` resources that match its label selector. If you add `NMStateConfig` resources after creating the `InfraEnv` resource, make sure that the `InfraEnv` creates a new Discovery Image by checking the `createdTime` property in your `InfraEnv`. If you already booted hosts, boot them again with the latest Discovery Image.

2.  Apply the YAML content by running the following command:

    ``` bash
    oc apply -f nmstateconfig.yaml
    ```

</div>

<div>

<div class="title">

Additional resources

</div>

- [Creating a host inventory by using the command line interface](clusters.md#create-host-inventory-cli)

- [Declarative Network API](https://nmstate.io/)

</div>

<a id="add-host-host-inventory-console"></a>

### Adding hosts to the host inventory by using the console

After you create your host inventory (infrastructure environment), you can discover your hosts and add them to your inventory using the console.

To add hosts to your inventory, choose a method to download an ISO file and attach it to each server. For example, you can download ISO files by using a virtual media, or by writing the ISO file to a USB drive.

**Important:** To prevent the installation from failing, keep the Discovery ISO media connected to the device during the installation process, and set each host to boot from the device one time.

<div>

<div class="title">

Prequisites

</div>

- You must enable the central infrastructure management service. See [Enabling the central infrastructure management service](clusters.md#enable-cim) for more information.

- You must create a host inventory. See [Creating a host inventory by using the console](clusters.md#create-host-inventory-console) for more information.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Select **Infrastructure** \> **Host inventory** in the console.

2.  Select your infrastructure environment from the list.

3.  Click **Add hosts** and select **With Discovery ISO**.

4.  Select **Minimal image file** or **Full image file**.

5.  Click **Generate Discovery ISO**.

    **Note:** Booted hosts appear in the host inventory table. Hosts might take a few minutes to appear.

6.  Approve each host so that you can use it. You can select hosts from the inventory table by clicking **Actions** and selecting **Approve**.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Creating a host inventory by using the command line interface](clusters.md#create-host-inventory-cli)

</div>

<a id="add-host-host-inventory-cli"></a>

### Adding hosts to the host inventory by using the command line interface

After you create your host inventory (infrastructure environment), you can discover your hosts and add them to your inventory using the CLI.

To add hosts to your inventory, choose a method to download an ISO file and attach it to each server. For example, you can download ISO files by using a virtual media, or by writing the ISO file to a USB drive.

The URL to download the ISO file in the `isoDownloadURL` property is in the status of your `InfraEnv` resource. See *Creating a host inventory by using the command line interface* for more information about the `InfraEnv` resource.

Each booted host creates an `Agent` resource in the same namespace.

**Important:** To prevent the installation from failing, keep the Discovery ISO media connected to the device during the installation process, and set each host to boot from the device one time.

<div>

<div class="title">

Prerequisites

</div>

- You must enable the central infrastructure management service. See [Enabling the central infrastructure management service](clusters.md#enable-cim) for more information.

- You must create a host inventory. See [Creating a host inventory by using the console](clusters.md#create-host-inventory-console) for more information.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Run the following command to view the download URL in the `InfraEnv` custom resource:

    ``` bash
    oc get infraenv -n <infra env namespace> <infra env name> -o jsonpath='{.status.isoDownloadURL}'
    ```

    See the following output:

        https://assisted-image-service-assisted-installer.apps.example-acm-hub.com/byapikey/eyJhbGciOiJFUzI1NiIsInC93XVCJ9.eyJpbmZyYV9lbnZfaWQcTA0Y38sWVjYi02MTA0LTQ4NDMtODasdkOGIxYTZkZGM5ZTUifQ.3ydTpHaXJmTasd7uDp2NvGUFRKin3Z9Qct3lvDky1N-5zj3KsRePhAM48aUccBqmucGt3g/4.17/x86_64/minimal.iso

    **Note:** By default, the minimal ISO is provided. You can specify the full ISO by setting `ImageType` to `full-iso` in your `InfraEnv` resource. See *Creating a host inventory by using the command line interface* in the additional resources section to learn more.

2.  Use the URL to download the ISO file and boot your hosts with the ISO file.

    Next, you need to approve each host. See the following procedure:

3.  Run the following command to list all of your `Agents`:

    ``` bash
    oc get agent -n <infra env namespace>
    ```

    You get an output that is similar to the following output:

        NAME                                   CLUSTER   APPROVED   ROLE          STAGE
        24a92a6f-ea35-4d6f-9579-8f04c0d3591e             false      auto-assign

4.  Approve any `Agent` from the list with a `false` approval status. Run the following command:

    ``` bash
    oc patch agent -n <infra env namespace> <agent name> -p '{"spec":{"approved":true}}' --type merge
    ```

5.  Run the following command to confirm approval status:

    ``` bash
    oc get agent -n <infra env namespace>
    ```

    You get an output that is similar to the following output with a `true` value:

        NAME                                   CLUSTER   APPROVED   ROLE          STAGE
        173e3a84-88e2-4fe1-967f-1a9242503bec             true       auto-assign

</div>

<div>

<div class="title">

Additional resources

</div>

- [Creating a host inventory by using the command line interface](clusters.md#create-host-inventory-cli)

</div>

<a id="hosting-ipxe-artifacts"></a>

### Hosting iPXE artifacts with HTTP or HTTPS

After you create your host inventory (infrastructure environment), you can discover your hosts and add them to your inventory. You can configure how to host iPXE artifacts.

To add hosts to your inventory, choose a method to download an ISO file and attach it to each server. For example, you can download ISO files by using a virtual media, or by writing the ISO file to a USB drive.

**Important:** To prevent the installation from failing, keep the Discovery ISO media connected to the device during the installation process, and set each host to boot from the device one time.

<div>

<div class="title">

Prerequisites

</div>

- You must enable the central infrastructure management service. See [Enabling the central infrastructure management service](clusters.md#enable-cim) for more information.

- You must create a host inventory. See [Creating a host inventory by using the console](clusters.md#create-host-inventory-console) for more information.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Edit the `spec.iPXEHTTPRoute` field in the `AgentServiceConfig` custom resource.

2.  Set the field to `enabled` to use HTTP for iPXE artifacts.

3.  Set the field to `disabled` to use HTTPS for iPXE artifacts.

4.  The default value is `disabled`. See the following example, where the `spec.iPXEHTTPRoute` field is set to `enabled`:

    ``` yaml
    apiVersion: agent-install.openshift.io/v1beta1
    kind: AgentServiceConfig
    metadata:
      name: agent
    spec:
      iPXEHTTPRoute: enabled
    ```

    If you set the value to `enabled`, the following endpoints are exposed through HTTP:

    - `api/assisted-installer/v2/infra-envs/<id>/downloads/files?file_name=ipxe-script` in `assisted-service`

    - `boot-artifacts/` and `images/<infra-env-id>/pxe-initrd` in `assisted-image-service`

</div>

<div>

<div class="title">

Additional resources

</div>

- [Creating a host inventory by using the command line interface](clusters.md#create-host-inventory-cli)

</div>

<a id="add-hosts-console"></a>

### Adding bare metal hosts to the host inventory by using the console

After creating your infrastructure environment, you can discover your hosts and add them to your host inventory. You can automate booting the Discovery Image of your infrastructure environment by making the bare metal operator communicate with the Baseboard Management Controller (BMC) of each bare metal host. Create a `BareMetalHost` resource and associated BMC secret for each host. The automation is set by a label on the `BareMetalHost` that references your infrastructure environment.

The automation performs the following actions:

- Boots each bare metal host with the Discovery Image represented by the infrastructure environment

- Reboots each host with the latest Discovery Image in case the infrastructure environment or any associated network configurations is updated

- Associates each `Agent` resource with its corresponding `BareMetalHost` resource upon discovery

- Updates `Agent` resource properties based on information from the `BareMetalHost`, such as hostname, role, and installation disk

- Approves the `Agent` for use as a cluster node

<div>

<div class="title">

Prerequisites

</div>

- You must enable the central infrastructure management service. See [Enabling the central infrastructure management service](clusters.md#enable-cim) for more information.

- You must create a host inventory. See [Creating a host inventory by using the console](clusters.md#create-host-inventory-console) for more information.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Select **Infrastructure** \> **Host inventory** in the console.

2.  Select your infrastructure environment from the list.

3.  Click **Add hosts** and select **With BMC Form**.

4.  Add the required information and click **Create**.

</div>

To learn more about BMC address formatting, see *BMC addressing* in the additional resources section.

<div>

<div class="title">

Additional resources

</div>

- [BMC addressing](https://docs.redhat.com/en/documentation/openshift_container_platform/4.20/html-single/installing_on_bare_metal/index)

- [Clusters at the network far edge](https://docs.redhat.com/en/documentation/openshift_container_platform/4.20/html/edge_computing/ztp-deploying-far-edge-clusters-at-scale)

- [Port access for the out-of-band management IP address](https://docs.redhat.com/en/documentation/openshift_container_platform/4.20/html-single/installing_on_bare_metal/index#network-requirements-out-of-band_ipi-install-prerequisites)

- [Postinstallation configuration overview](https://docs.redhat.com/en/documentation/openshift_container_platform/4.20/html/postinstallation_configuration/post-install-configuration-overview)

- [Manually scaling a compute machine set](https://docs.redhat.com/en/documentation/openshift_container_platform/4.20/html-single/machine_management/index#manually-scaling-machineset)

</div>

<a id="auto-add-hosts-cli"></a>

### Automatically adding bare metal hosts to the host inventory by using the command line interface

After creating your infrastructure environment, you can discover your hosts and add them to your host inventory. You can automate booting the Discovery Image of your infrastructure environment by making the bare metal operator communicate with the Baseboard Management Controller (BMC) of each bare metal host. Create a `BareMetalHost` resource and associated BMC secret for each host. The automation is set by a label on the `BareMetalHost` that references your infrastructure environment.

The automation performs the following actions:

- Boots each bare metal host with the Discovery Image represented by the infrastructure environment

- Reboots each host with the latest Discovery Image in case the infrastructure environment or any associated network configurations is updated

- Associates each `Agent` resource with its corresponding `BareMetalHost` resource upon discovery

- Updates `Agent` resource properties based on information from the `BareMetalHost`, such as hostname, role, and installation disk

- Approves the `Agent` for use as a cluster node

After turning on the host, the image starts downloading. This might take a few minutes. When the host is discovered, an `Agent` custom resource is created automatically.

<div>

<div class="title">

Prerequisites

</div>

- You must enable the central infrastructure management service. See [Enabling the central infrastructure management service](clusters.md#enable-cim) for more information.

- You must create a host inventory. See [Creating a host inventory by using the console](clusters.md#create-host-inventory-console) for more information.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create a BMC secret by applying the following YAML content. Replace the BMC secret `name`, `namespace`, `username`, values where needed. The namespace must be the same as the namespace of your `InfraEnv`:

    ``` YAML
    apiVersion: v1
    kind: Secret
    metadata:
      name: <bmc-secret-name>
      namespace: <your_infraenv_namespace>
    type: Opaque
    data:
      username: <username>
      password: <password>
    ```

2.  Create a bare metal host by applying the following YAML content and replacing values where needed.

    ``` yaml
    apiVersion: metal3.io/v1alpha1
    kind: BareMetalHost
    metadata:
      name: <bmh-name>
      namespace: <your-infraenv-namespace>
      annotations:
        inspect.metal3.io: disabled
        bmac.agent-install.openshift.io/hostname: <hostname>
        bmac.agent-install.openshift.io/role: <role>
      labels:
        infraenvs.agent-install.openshift.io: <your-infraenv>
    spec:
      online: true
      automatedCleaningMode: disabled
      bootMACAddress: <your-mac-address>
      bmc:
        address: <machine-address>
        credentialsName: <bmc-secret-name> 
      rootDeviceHints:
        deviceName: /dev/sda
    ```

    - The namespace must be the same as the namespace of your `InfraEnv`.

    - **Optional:** Replace \<hostname\> with the name of your host.

    - **Optional:** Possible \<role\> values are `master` or `worker`.

    - The \<your-infraenv\> name must match the name of your `InfrEnv` and exist in the same namespace.

    - If you do not set a `` automatedCleaningMode`value, the `metadata `` value is automatically used.

    - Make sure \<your-mac-address\> matches the MAC address of one of your host interfaces.

    - Use the \<machine-address\> of the BMC. To learn more, see *Port access for the out-of-band management IP address* and *BMC addressing* in the additional resources section.

    - Make sure that the `credentialsName` value matches the name of the BMC secret you created.

    - **Optional:** Select the installation disk in the `deviceName` field. See *The BareMetalHost spec* for the available root device hints. After the host is booted with the Discovery Image and the corresponding `Agent` resource is created, the installation disk is set according to this hint.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Port access for the out-of-band management IP address](https://docs.redhat.com/en/documentation/openshift_container_platform/4.20/html-single/installing_on_bare_metal/index#network-requirements-out-of-band_ipi-install-prerequisites)

- [Postinstallation configuration overview](https://docs.redhat.com/en/documentation/openshift_container_platform/4.20/html/postinstallation_configuration/post-install-configuration-overview)

- [BMC addressing](https://docs.redhat.com/en/documentation/openshift_container_platform/4.20/html-single/installing_on_bare_metal/index)

</div>

<a id="bind-unbind-hosts"></a>

### Binding and unbinding hosts

You can bind hosts to an Red Hat OpenShift Container Platform cluster by setting the `spec.clusterDeploymentName` field in the `Agent` custom resource, or by setting the `{}bmac.agent-install.openshift.io/cluster-reference` bare metal host annotation.

The `{}bmac.agent-install.openshift.io/cluster-reference` bare metal host annotation controls the connection to your OpenShift Container Platform cluster, and binds or unbinds hosts to a specific cluster.

You can use the `{}bmac.agent-install.openshift.io/cluster-reference` annotation in one of the following three ways:

- If you do not set the annotation in the bare metal host, no changes apply to the host.

- If you set the annotation with an empty string value, the host unbinds.

- If you set the annotation and use a string value that follows the `<cluster-namespace>/<cluster-name>` format, the host binds to the cluster that your `ClusterDeployment` custom resource represents.

**Note:** If the `InfraEnv` that the host belongs to already contains a `cluster-reference` annotation, the `{}bmac.agent-install.openshift.io/cluster-reference` annotation is ignored.

<a id="remove-nodes-bm"></a>

### Removing managed cluster nodes with a bare metal host

You can remove managed cluster nodes from a managed cluster. Make sure to not delete `NMStateConfig` resources when you delete the agent and bare metal host. If you have a bare metal host on your hub cluster and want remove managed cluster nodes from a managed cluster, complete the following procedure:

<div>

<div class="title">

Prerequisites

</div>

- You need a hub cluster that is running on a supported OpenShift Container Platform version

- Any static networking configuration required for the node to boot must be available.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Add the following annotation to the `BareMetalHost` resource of the node that you want to delete:

    ``` bash
    bmac.agent-install.openshift.io/remove-agent-and-node-on-delete: true
    ```

2.  Delete the `BareMetalHost` resource by running the following command. Replace `<bmh-name>` with the name of your `BareMetalHost`:

    ``` bash
    oc delete bmh <bmh-name>
    ```

</div>

<a id="remove-nodes-wo-bm"></a>

### Removing managed cluster nodes without a bare metal host

You can remove managed cluster nodes from a managed cluster. Make sure to not delete `NMStateConfig` resources when you delete the agent and bare metal host. If you do not have a bare metal host on your hub cluster and you want to remove managed cluster nodes from a managed cluster, complete the following procedure:

<div>

<div class="title">

Prerequisites

</div>

- You need a hub cluster that is running on a supported OpenShift Container Platform version

- Any static networking configuration required for the node to boot must be available.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Unbind the agent by removing the `clusterDeploymentName` field from the `Agent` specification, or delete the `Agent` custom resource that corresponds with the node that you are removing.

2.  If you want to delete an `Agent` resource from the hub cluster, but do not want the node removed from the managed cluster, set the annotation `agent.agent-install.openshift.io/skip-spoke-cleanup` to `true` on the `Agent` resource before you remove it.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Deleting nodes](https://docs.openshift.com/container-platform/4.18/nodes/nodes/nodes-nodes-working.html#deleting-nodes)

</div>

<a id="cancel-host-install"></a>

### Cancelling host installations

You can cancel host installations to prevent incorrect cluster binding, change host configurations, or fix installation problems.

For example, you can cancel the installation if a production environment host becomes stuck during installation with the `installing-pending-user-action` status.

<div>

<div class="title">

Prerequisites

</div>

- You are using the late binding feature on your managed cluster.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Check if your managed cluster is using central infrastructure management. Run the following command:

    ``` bash
    oc get agentclusterinstall -n <namespace>
    ```

    If your managed cluster is using central infrastructure management, the following output with the `adding-hosts` `STATE` appears:

    ``` bash
    NAME                    CLUSTER                 STATE
    assisted-cluster        assisted-cluster        adding-hosts
    ```

2.  Check if the host is installing. Run the following command:

    ``` bash
    oc get agent -n <namespace>
    ```

    If the host is installing, the output resembles the following example:

    ``` bash
    NAME                                   CLUSTER                 APPROVED   ROLE          STAGE
    127877e3-2098-4bf8-9b44-588a78ffcccd   assisted-cluster        true       worker        Rebooting
    ```

3.  If your output resembles the previous example, you can continue cancelling the host installation. Otherwise, do not continue with the next steps.

4.  Unbind the host from the managed cluster by removing the `clusterDeploymentName` field in the `Agent` resource of the host that you want to stop installing. Run the following command:

    ``` bash
    oc patch agent -n <namespace> <agent-name> --patch='[{"op":"remove","path":"/spec/clusterDeploymentName"}]' --type=json
    ```

    Confirm that the host is unbound by running the following command:

    ``` bash
    oc get agent -n <namespace>
    ```

    If the host is unbound, the output resembles the following example, where `CLUSTER` is empty and `STAGE` is either empty, or `unbinding-pending-user-action` or similar.

    ``` bash
    NAME                                   CLUSTER   APPROVED   ROLE          STAGE
    127877e3-2098-4bf8-9b44-588a78ffcccd             true       auto-assign
    ```

5.  Return the host to the discovery phase. If you are using the Discovery ISO to add a node, download the Discovery ISO again and reboot your host with the Discovery ISO. Run the following command:

    ``` bash
    oc get infraenv -n <namespace> <infraenv-name> -ojsonpath='{.status.isoDownloadURL}'
    ```

6.  If you are using the `BareMetalHost` resource to add a node, the host automatically returns to the discovery phase. Run the following command to confirm that the host is in the discovery phase:

    ``` bash
    oc get bmh -n <namespace>
    ```

    **Note:** If the host is in the discovery phase, the `BareMetalHost` resource status changes from `deprovisioning` to `provisioning`. It might take a few minutes for deprovisioning to complete. After the `BareMetalHost` reaches the `provisioning status`, the host is in discovery mode.

7.  Check to see if the `Agent` resource is discovered and validated. Run the following command:

    ``` bash
    oc get agent -n <namespace> <agent-name> -ojsonpath='{"NAME: "}{.metadata.name}{"\n"}{"VALIDATIONS PASSING: "}{.status.conditions[?(@.type == "Validated")].status}{"\n"}'
    ```

8.  Bind the `Agent` resource to the managed cluster to reinstall the host. Run the following command:

    ``` bash
    oc patch agent -n <namespace> <agent-name> --patch='[{"op":"add","path":"/spec/clusterDeploymentName","value":{"name":"<cluster name>","namespace":"<cluster namespace>"}}]' --type=json
    ```

9.  Confirm that the `Agent` resource is bound to the managed cluster. Run the following command:

    ``` bash
    oc get agent -n <namespace>
    ```

    If the `Agent` resource is bound to the managed cluster, the output resembles the following example:

    ``` bash
    NAME                                   CLUSTER               APPROVED   ROLE          STAGE
    127877e3-2098-4bf8-9b44-588a78ffcccd   cluster name          true       auto-assign
    ```

</div>

<a id="manage-host-inv"></a>

### Managing your host inventory

You can manage your host inventory and edit existing hosts by using the console, or by using the command line interface and editing the `Agent` resource.

Each host that you successfully boot with the Discovery ISO appears as a row in your host inventory. Use the console to edit and manage your hosts. If you booted the host manually and are not using the bare metal operator automation, you must approve the host in the console before you can use it. Hosts that are ready to be installed as OpenShift nodes have the `Available` status.

If you manage your host inventory by using the command line interface, an `Agent` resource represents each host. See the following defintion list to learn about the properties in an `Agent` resource:

- See the following list of `Agent` resource properties:

  `clusterDeploymentName`  
  Set this property to the namespace and name of the `ClusterDeployment` you want to use if you want to install the host as a node in a cluster.

  `role`  
  Optional property that sets the role for the host in the cluster. Possible values are `master`, `worker`, and `auto-assign`. The default value is `auto-assign`.

  `hostname`  
  Sets the host name for the host. Optional if the host is automatically assigned a valid host name, for example by using DHCP.

  `approved`  
  Indicates if the host can be installed as an OpenShift node. This property is a boolean with a default value of `False`. If you booted the host manually and are not using the bare metal operator automation, you must set this property to `True` before installing the host.

  `installation_disk_id`  
  The ID of the installation disk you chose that is visible in the inventory of the host.

  `installerArgs`  
  A JSON-formatted string containing overrides for the *coreos-installer* arguments of the host. You can use this property to modify kernel arguments. See the following example syntax:

  <!-- -->

      ["--append-karg", "ip=192.0.2.2::192.0.2.254:255.255.255.0:core0.example.com:enp1s0:none", "--save-partindex", "4"]

  `ignitionConfigOverrides`  
  A JSON-formatted string containing overrides for the ignition configuration of the host. You can use this property to add files to the host by using ignition. See the following example syntax:

      {"ignition": "version": "3.1.0"}, "storage": {"files": [{"path": "/tmp/example", "contents": {"source": "data:text/plain;base64,aGVscGltdHJhcHBlZGluYXN3YWdnZXJzcGVj"}}]}}

  `nodeLabels`  
  A list of labels that are applied to the node after the host is installed.

The `status` of an `Agent` resource has the following properties:

`role`  
Sets the role for the host in the cluster. If you previously set a `role` in the `Agent` resource, the value appears in the `status`.

`inventory`  
Contains host properties that the agent running on the host discovers.

`progress`  
The host installation progress.

`ntpSources`  
The configured Network Time Protocol (NTP) sources of the host.

`conditions`  
Contains the following standard Kubernetes conditions with a `True` or `False` value:

- SpecSynced: `True` if all specified properties are successfully applied. `False` if some error was encountered.

- Connected: `True` if the agent connection to the installation service is not obstructed. `False` if the agent has not contacted the installation service in some time.

- RequirementsMet: `True` if the host is ready to begin the installation.

- Validated: `True` if all host validations pass.

- Installed: `True` if the host is installed as an OpenShift node.

- Bound: `True` if the host is bound to a cluster.

- Cleanup: `False` if the request to delete the `Agent` resouce fails.

`debugInfo`  
Contains URLs for downloading installation logs and events.

`validationsInfo`  
Contains information about validations that the agent runs after the host is discovered to ensure that the installation is successful. Troubleshoot if the value is `False`.

`installation_disk_id`  
The ID of the installation disk you chose that is visible in the inventory of the host.

<div>

<div class="title">

Additional resources

</div>

- [coreos-installer install](https://coreos.github.io/coreos-installer/cmd/install/)

</div>

<a id="enable-hub-manage-cim"></a>

### Enabling hub cluster management by using central infrastructure management

Importing and managing a hub cluster by using central infrastructure management can simplify your cluster management by providing a single point of control.

By default, central infrastructure management does not automatically manage your hub cluster. Enable the feature to add and manage additional hosts on your hub cluster by using central infrastructure management.

<div>

<div class="title">

Prerequisites

</div>

- You must enable the central infrastructure management service. See [Enabling the central infrastructure management service](clusters.md#enable-cim) for more information.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Annotate the `AgentServiceConfig` custom resource to enable `local-cluster` import. Run the following command:

    ``` bash
    oc annotate agentserviceconfig agent agent-install.openshift.io/enable-local-cluster-import=true
    ```

2.  Verify that the feature is enabled by checking if an `InfraEnv` custom resource is created for the `local-cluster`. Run the following command:

    ``` bash
    oc get infraenv -n multicluster-engine
    ```

</div>

<div>

<div class="title">

Additional resources

</div>

- [Adding hosts to the host inventory by using the console](clusters.md#add-host-host-inventory-console)

- [Automatically adding bare metal hosts to the host inventory](clusters.md#add-hosts-console)

</div>

<a id="config-mirror-reg-cluster"></a>

### Configuring mirror registries for each cluster

Use the mirror registry feature to configure and manage custom registries for each cluster by referencing a dedicated mirror registry configuration object from each `AgentClusterInstall` and `InfraEnv` resource.

You might configure mirror registries for each cluster in multicluster environments where you need isolated registry configurations.

<div>

<div class="title">

Prerequisites

</div>

- You must enable the central infrastructure management service. See [Enabling the central infrastructure management service](clusters.md#enable-cim) for more information.

- You must set up your mirror registry.

- The `assisted-service` must run in `KubeAPI` mode.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Ensure that the required images are mirrored to the registry.

    1.  Mirror the Red Hat OpenShift Container Platform release images by running the following command. Ensure that the OpenShift Container Platform version in the mirror registry matches the version in the image set configuration:

        ``` bash
        oc adm release mirror \
          -a pull_secret.json \
          --from=quay.io/openshift-release-dev/ocp-release:$OCP_TAG \
          --to=$REGISTRY_IP:$REGISTRY_PORT/openshift-release-dev/ocp-release \
          --to-release-image=$REGISTRY_IP:$REGISTRY_PORT/openshift-release-dev/ocp-release:$OCP_TAG
        ```

    2.  Mirror the Assisted Installer images by running the following commands:

    ``` bash
    oc image mirror \
      -a pull_secret.json \
      quay.io/edge-infrastructure/assisted-installer:latest \
      $REGISTRY_IP:$REGISTRY_PORT/edge-infrastructure/assisted-installer:latest

    oc image mirror \
      -a pull_secret.json \
      quay.io/edge-infrastructure/assisted-installer-controller:latest \
      $REGISTRY_IP:$REGISTRY_PORT/edge-infrastructure/assisted-installer-controller:latest

    oc image mirror \
      -a pull_secret.json \
      quay.io/edge-infrastructure/assisted-installer-agent:latest \
      $REGISTRY_IP:$REGISTRY_PORT/edge-infrastructure/assisted-installer-agent:latest
    ```

2.  Apply the required custom resource definitions to configure your cluster to use the mirrored images.

    1.  Create a `ConfigMap` file named `mirror_registry.yaml` with the following content. Replace values for `<your-namespace>`, `$REGISTRY_IP`, and `$REGISTRY_PORT` with your specific values:

        ``` yaml
        apiVersion: v1
        kind: ConfigMap
        metadata:
          name: mirror-registry-config
          namespace: <your-namespace>
        data:
          registries.conf: |
            [[registry]]
              prefix = ""
              location = "quay.io/openshift-release-dev/ocp-release"
              [[registry.mirror]]
                location = "$REGISTRY_IP:$REGISTRY_PORT/openshift-release-dev/ocp-release"
                pull-from-mirror = "digest-only"

            [[registry]]
              prefix = ""
              location = "quay.io/edge-infrastructure"
              [[registry.mirror]]
                location = "$REGISTRY_IP:$REGISTRY_PORT/edge-infrastructure"
          ca-bundle.crt: |
            -----BEGIN CERTIFICATE-----
            ...
            -----END CERTIFICATE-----
        ```

    2.  Apply the config map by running the following command:

        ``` bash
        oc apply -f mirror_registry.yaml
        ```

    3.  Ensure that your `AgentClusterInstall` and `InfraEnv` custom resource definitions reference the mirror registry configuration. See the following example for both `aci.yaml` and `infraenv.yaml`:

        ``` yaml
        ...
        spec:
          mirrorRegistryRef:
            name: mirror-registry-config
            namespace: <your-namespace>
            ...
        ```

    4.  Update and apply the `aci.yaml` file by running the following command:

        ``` bash
        oc apply -f aci.yaml
        ```

    5.  Update and apply the `infraenv.yaml` file by running the following command:

    ``` bash
    oc apply -f infraenv.yaml
    ```

</div>

<div>

<div class="title">

Additional resources

</div>

- [Mirroring images for a disconnected installation](https://docs.openshift.com/container-platform/4.18/installing/disconnected_install/installing-mirroring-installation-images.html)

</div>

<a id="config-third-party-cni-on-prem"></a>

### Configuring third-party CNI plugins for on-premises cluster installation (Technology Preview)

When you install on-premises OpenShift Container Platform clusters by using the central infrastructure management feature, you can select a third-party Container Network Interface (CNI) plugin instead of the built-in OVN-Kubernetes option. Using a third-party CNI plugin helps you maintain operational consistency or use special network functions.

<div>

<div class="title">

Prerequisites

</div>

- You must enable the central infrastructure management service. See [Enabling the central infrastructure management service](clusters.md#enable-cim) for more information.

- You need version-compatible CNI manifests from your CNI vendor. The installer does not ship or generate manifests for third-party CNIs.

- You need to upload CNI manifests before installation if you choose `CiscoACI`, `Cilium`, `Calico`, or `None`. See [Supported network types for third-party CNI plugins (Technology Preview)](clusters.md#support-net-types-third-party-cni) for more information.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create a `ConfigMap` that contains your CNI manifests. Each key in the `ConfigMap` is a manifest filename, and the value is its content. See the following example for Cilium:

    ``` yaml
    apiVersion: v1
    kind: ConfigMap
    metadata:
      name: <cilium-cni-manifests>
      namespace: <cluster-namespace>
    data:
      cilium-olm.yaml: |
        apiVersion: operators.coreos.com/v1alpha1
        kind: Subscription
        metadata:
          name: cilium
          namespace: cilium
        spec:
          channel: "1.17"
          name: cilium-olm
          source: certified-operators
          sourceNamespace: openshift-marketplace
      cilium-config.yaml: |
        <cilium-config-manifest>
    ```

    - Replace `<cilium-cni-manifests>` with the name of your `ConfigMap` resource.

    - Replace `<cluster-namespace>` with the namespace of your cluster.

    - Replace `<cilium-config-manifest>` with the content of your Cilium configuration manifest.

2.  Set `spec.networking.networkType` and reference the `ConfigMap` in your `AgentClusterInstall` resource. See the following example:

    ``` yaml
    apiVersion: extensions.hive.openshift.io/v1beta1
    kind: AgentClusterInstall
    metadata:
      name: <cluster-name>
      namespace: <cluster-namespace>
    spec:
      clusterDeploymentRef:
        name: <cluster-name>
      imageSetRef:
        name: openshift-v<image-version>
      networking:
        networkType: Cilium
        clusterNetwork:
        - cidr: 10.128.0.0/14
          hostPrefix: 23
        serviceNetwork:
        - 172.30.0.0/16
      provisionRequirements:
        controlPlaneAgents: 3
        workerAgents: 2
      manifestsConfigMapRefs:
      - name: <cilium-cni-manifests>
    ```

    - Replace `<cluster-name>` with the name of your cluster.

    - Replace `<cluster-namespace>` with the namespace of your cluster.

    - Replace `<image-version>` with the version of OpenShift Container Platform that you are using.

    - Replace `<cilium-cni-manifests>` with the name of your `ConfigMap` resource.

    **Notes:**

    - You can reference multiple `ConfigMap` resources. Manifest names must be unique across all referenced `ConfigMap` resources.

    - If you leave `networkType` empty, OVN-Kubernetes is selected for OpenShift Container Platform version 4.12 and later, IPv6, or single-node OpenShift clusters.

</div>

<div>

<div class="title">

Verification

</div>

- Verify that the cluster passes validation before installation. Run the following command:

  ``` bash
  oc get agentclusterinstall <cluster-name> -n <cluster-namespace> \
    -o jsonpath='{range .status.conditions[*]}{.type}{"\t"}{.message}{"\n"}{end}'
  ```

  - Replace `<cluster-name>` with the name of your cluster.

  - Replace `<cluster-namespace>` with the namespace of your cluster.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Certified OpenShift CNI Plug-ins](https://access.redhat.com/articles/5436171)

- [Create a cluster in an on-premises environment by using the CLI](clusters.md#create-a-cluster-on-premises-cli)

</div>

<a id="support-net-types-third-party-cni"></a>

### Supported network types for third-party CNI plugins (Technology Preview)

When you install on-premises OpenShift Container Platform clusters by using the central infrastructure management feature, you can select a third-party Container Network Interface (CNI) plugin instead of the built-in OVN-Kubernetes option.

To use a third-party CNI, set `spec.networking.networkType` on the `AgentClusterInstall` resource and provide CNI manifests by using the `spec.manifestsConfigMapRefs` field. See *Configuring third-party CNI plugins for on-premises cluster installation (Technology Preview)* in the additional resources section for more information.

All third-party CNI options (`CiscoACI`, `Cilium`, `Calico`, and `None`) require you to upload CNI manifests before installation.

The following table displays supported values for the `spec.networking.networkType` field in the `AgentClusterInstall` resource, and for `spec.networkType` in the `ClusterInstance` resource:

| Value | Description | Custom manifests required |
|----|----|----|
| `OVNKubernetes` | Default CNI for OpenShift Container Platform | No |
| `CiscoACI` | Cisco ACI CNI | Yes |
| `Cilium` | Isovalent Cilium CNI | Yes |
| `Calico` | Tigera Calico CNI | Yes |
| `None` | No CNI. You provide all networking manifests. | Yes |

Table of supported network types

<div>

<div class="title">

Additional resources

</div>

- [Configuring third-party CNI plugins for on-premises cluster installation (Technology Preview)](clusters.md#config-third-party-cni-on-prem)

</div>

<a id="install-tnf-cluster-ai"></a>

### Installing a TNF cluster with Assisted Installer (Technology Preview)

**Technology Preview**: A two-node with fencing (TNF) cluster is an Red Hat OpenShift Container Platform cluster that has two control plane nodes. Use TNF clusters to ensure redundancy at the edge and limit hardware costs.

<div>

<div class="title">

Prerequisites

</div>

- You are using the `baremetal` or `none` platform.

- You have access to the baseboard management controller (BMC) of the platform nodes.

- Your OpenShift Container Platform managed cluster version is 4.20.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Enable the TNF cluster installation feature with Assisted Installer by setting an environment variable on the `assisted-service` pod.

2.  Create the following `ConfigMap` resource:

    ``` yaml
    apiVersion: v1
    data:
      TNF_CLUSTERS_SUPPORT: "true"
    kind: ConfigMap
    metadata:
      name: assisted-service-custom
      namespace: multicluster-engine
    ```

3.  Reference the `ConfigMap` resource in an annotation on the `AgentServiceConfig` resource. Run the following command:

    ``` bash
    oc annotate agentserviceconfig agent unsupported.agent-install.openshift.io/assisted-service-configmap=assisted-service-custom
    ```

4.  Configure the TNF cluster object on the hub cluster by creating the required resources.

    1.  Create a namespace. Use the following YAML sample:

        ``` yaml
        apiVersion: v1
        kind: Namespace
        metadata:
          name: tnf-cluster
        ```

    2.  Create a pull secret. Use the following YAML sample. Replace `<your-base64-pull-secret>` with the name of your pull secret:

        ``` yaml
        apiVersion: v1
        kind: Secret
        type: kubernetes.io/dockerconfigjson
        metadata:
          name: pull-secret
          namespace: tnf-cluster
        data:
          .dockerconfigjson: <your-base64-pull-secret>
        ```

    3.  Create a `AgentClusterInstall` resource. Use the following YAML sample. Replace `<your-public-ssh-key>` with your public SSH key:

        ``` yaml
        apiVersion: extensions.hive.openshift.io/v1beta1
        kind: AgentClusterInstall
        metadata:
          name: tnf-cluster
          namespace: tnf-cluster
        spec:
          platformType: BareMetal
          apiVIPs: [192.168.122.10]
          ingressVIPs: [192.168.122.20]
          clusterDeploymentRef:
            name: tnf-cluster
          imageSetRef:
            name: img4.20.0-rc.3-x86-64-appsub
          networking:
            clusterNetwork:
            - cidr: 10.128.0.0/14
              hostPrefix: 23
            machineNetwork:
            - cidr: 192.168.122.0/24
            serviceNetwork:
            - 172.30.0.0/16
          provisionRequirements:
            controlPlaneAgents: 2
          sshPublicKey: <your-public-ssh-key>
        ```

    4.  Create a `ClusterDeployment` resource. Use the following YAML sample. Replace `<yourdomain.com>` with your domain address:

        ``` yaml
        apiVersion: hive.openshift.io/v1
        kind: ClusterDeployment
        metadata:
          name: tnf-cluster
          namespace: tnf-cluster
        spec:
          baseDomain: <yourdomain.com>
          clusterInstallRef:
            group: extensions.hive.openshift.io
            kind: AgentClusterInstall
            name: tnf-cluster
            version: v1beta1
          clusterName: tnf-cluster
          controlPlaneConfig:
            servingCertificates: {}
          platform:
            agentBareMetal:
              agentSelector:
                cluster: tnf
          pullSecretRef:
            name: pull-secret
        ```

    5.  Create an `InfraEnv` resource. Use the following YAML sample. Replace `<your-public-ssh-key>` with your public SSH key:

    ``` yaml
    apiVersion: agent-install.openshift.io/v1beta1
    kind: InfraEnv
    metadata:
      name: tnf-cluster
      namespace: tnf-cluster
    spec:
      clusterRef:
        name: tnf-cluster
        namespace: tnf-cluster
      pullSecretRef:
        name: pull-secret
      sshAuthorizedKey: <your-public-ssh-key>
    ```

5.  **Optional:** Create a fencing credentials secret for each node. Use the following YAML sample. Replace `<username>` and `<password>` with your username and password. The `certificateVerification` field default value is `Enabled`:

    ``` yaml
    apiVersion: v1
    stringData:
      address: https://bmc.example.com
      certificateVerification: Disabled
      username: <username>
      password: <password>
    kind: Secret
    metadata:
      name: node-0-fencing-credentials
      namespace: tnf-cluster
    type: Opaque
    ```

    **Note:** Fencing credentials for an Agent are stored as a Kubernetes secret in the Agent namespace that the Agent references in the `agent.spec.fencingCredentialsSecretRef` field.

6.  Use one of the following methods to set Agent fencing credentials. The methods are listed in descending order of priority:

    - Manually create the secret and add an annotation on the `BareMetalHost` resource that references the secret. Use the following annotation key:

      ``` bash
      bmac.agent-install.openshift.io/fencing-credentials-secret-name
      ```

      **Note:** The Assisted Installer sets the Agent `fencingCredentialsSecretRef` field to the value of the annotation.

    - Set an annotation on the Agent `BareMetalHost` resource to create the secret from the `BareMetalHost` BMC configuration. Use the following annotation key:

      ``` bash
      bmac.agent-install.openshift.io/create-fencing-credentials-secret
      ```

    **Note:** You can use any value.

    - Manually create the secret. Then, manually set the Agent `fencingCredentialsSecretRef` field to the secret name.

</div>

<a id="capi-intro"></a>

## Cluster API

Cluster API offers declarative APIs that simplify the provisioning, upgrading, and management of Kubernetes clusters. multicluster engine operator installs the core Cluster API components along with multiple infrastructure and bootstrap providers to support different use-cases and platforms. Learn how to use Cluster API with either standalone multicluster engine operator or Red Hat Advanced Cluster Management. See the following processes:

- [Installing a managed cluster with Cluster API](clusters.md#capi-managed-assisted)

- [Preparing your hub cluster for Cluster API clusters (Technology Preview)](clusters.md#prep-auto-import-capi)

- [Enabling automatic import for Cluster API clusters (Technology Preview)](clusters.md#auto-import-capi)

- [Switching from AWS credentials to IAM roles on your Cluster API managed cluster (Technology Preview)](clusters.md#switch-iam-roles-capi)

- [Preparing to create a Red Hat OpenShift Service on AWS with hosted control planes cluster with Cluster API](clusters.md#prep-create-rosa-hcp-capi-cluster)

- [Creating a Red Hat OpenShift Service on AWS with hosted control planes cluster with Cluster API](clusters.md#create-rosa-hcp-capi-cluster)

- [Deleting a Red Hat OpenShift Service on AWS with hosted control planes cluster with using Cluster API](clusters.md#delete-rosa-hcp-capi-cluster)

<a id="capi-managed-assisted"></a>

### Installing a managed cluster with Cluster API

You can install an OpenShift Container Platform managed cluster with the Cluster API by using the `metal3` infrastructure provider and the OpenShift Container Platform assisted bootstrap and control plane providers.

- A `ControlPlane` resource defines the control plane properties.

- The `ClusterInfrastructure` defines the cluster-level infrastructure details.

<div>

<div class="title">

Prerequisites

</div>

- You need the `MultiClusterEngine` resource either from the Red Hat Advanced Cluster Management installation, or the multicluster engine operator standalone installation.

- The following API base domain must point to the static API VIP: `api.<cluster_name>.<base_domain>`.

- The following application base domain must point to the static IP address for Ingress VIP:

      *.apps.<cluster_name>.<base_domain>

- You need the internal API endpoint for the cluster: `api-int.<baseDomain>`.

- The Cluster API Provider OpenShift Assisted requires the following components:

  - Cluster API: The core components provide the required custom resource definitions and controllers within the management cluster.

  - Assisted service: The infrastructure operator for Red Hat OpenShift in multicluster engine for Kubernetes operator provisions this service. Ensure the service is reachable and active.

  - Infrastructure provider: A provider, such as the `cluster-api-provider-metal3`, manages the physical or virtual resources.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Enable the services that you need to provision a workload. By default, `assisted-service` is enabled. By default, `cluster-api-provider-metal3` and `cluster-api-provider-openshift-assisted` are disabled. Ensure all three services are `enabled: true`. Run the following command to edit the resource:

    ``` bash
    oc edit multiclusterengines.multicluster.openshift.io -n multicluster-engine
    ```

2.  Set `enabled: true` in `.spec.overrides` for the `assisted-service` component, the `cluster-api-provider-metal3` component, and the `cluster-api-provider-openshift-assisted` component. See the following `configOverrides` values:

    ``` yaml
        - configOverrides: {}
          enabled: true
          name: assisted-service
        - configOverrides: {}
          enabled: true
          name: cluster-api
    ...
        - configOverrides: {}
          enabled: true
          name: cluster-api-provider-metal3
        - configOverrides: {}
          enabled: true
          name: cluster-api-provider-openshift-assisted
    ```

3.  Enable the central infrastructure management service. See [Enabling the central infrastructure management service](clusters.md#enable-cim) for the procedure.

4.  Configure a `Cluster` resource with `clusterNetwork` specifications, `controlPlaneRef` specifications, and `infrastructureRef` specifications. See the following `Cluster` resource:

    ``` yaml
    apiVersion: cluster.x-k8s.io/v1beta1
    kind: Cluster
    metadata:
      name: <cluster-name>
      namespace: <cluster-namespace>
    spec:
      clusterNetwork:
        pods:
          cidrBlocks:
            - 172.18.0.0/20
        services:
          cidrBlocks:
            - 10.96.0.0/12
      controlPlaneRef:
        apiVersion: controlplane.cluster.x-k8s.io/v1alpha2
        kind: OpenshiftAssistedControlPlane
        name:  <cluster-name>
        namespace:  <cluster-namespace>
      infrastructureRef:
        apiVersion: infrastructure.cluster.x-k8s.io/v1beta1
        kind: Metal3Cluster
        name: <cluster-name>
        namespace: <cluster-namespace>
    ```

    - In `controlPlaneRef.kind`, `OpenshiftAssistedControlPlane` is the control plane.

    - In `infrastructureRef.kind`, `Metal3Cluster` is the infrastructure.

5.  Apply the YAML content by running the following command:

    ``` bash
    oc apply -f <filename>.yaml
    ```

6.  Configure the `OpenshiftAssistedControlPlane` resource that includes the `distributionVersion`, `apiVIPs`, and SSH keys. Specify your OpenShift Container Platform version in the `distributionVersion` field.

    **Note:** The value for the `distributionVersion` matches the image from the [OpenShift Container Platform Releases](https://mirror.openshift.com/pub/openshift-v4/x86_64/clients/ocp/latest/). See the following YAML resource:

    ``` yaml
    apiVersion: controlplane.cluster.x-k8s.io/v1alpha2
    kind: OpenshiftAssistedControlPlane
    metadata:
      name: <cluster-name>
      namespace: <cluster-namespace>
      annotations: {}
    spec:
      openshiftAssistedConfigSpec:
        sshAuthorizedKey: "{{ ssh_authorized_key }}"
        nodeRegistration:
          kubeletExtraLabels:
          - 'metal3.io/uuid="${METADATA_UUID}"'
      distributionVersion: <4.x.0>
      config:
        apiVIPs:
        - 192.168.222.40
        ingressVIPs:
        - 192.168.222.41
        baseDomain: lab.home
        pullSecretRef:
          name: "pull-secret"
        sshAuthorizedKey: "{{ ssh_authorized_key }}"
      machineTemplate:
        infrastructureRef:
          apiVersion: infrastructure.cluster.x-k8s.io/v1beta1
          kind: Metal3MachineTemplate
          name: <cluster-name-control-plane>
          namespace: <cluster-namespace>
      replicas: 3
    ```

    - The `.spec.openshiftAssistedConfigSpec.sshAuthorizedKey` is used to access nodes in the *boot* phase, also known as *discovery* phase.

    - The `.spec.config.sshAuthorizedKey` is used to access the provisioned OpenShift Container Platform nodes.

7.  Apply the YAML file. Run the following command:

    ``` bash
    oc apply -f <filename>.yaml
    ```

8.  If you do not have a pull secret, you need to create a pull secret to enable your clusters to pull images from container registries. Complete the following steps to create a pull secret:

9.  Create a YAML file to pull images. See the following example of a file that is named `pull-secret.yaml`:

    ``` yaml
    apiVersion: v1
    kind: Secret
    metadata:
      name: pull-secret
      namespace: <cluster-namespace>
    data:
      .dockerconfigjson: <encoded_docker_configuration>
    type: kubernetes.io/dockerconfigjson
    ```

    - Ensure that the `<cluster-namespace>` value matches the target namespace.

    - Specify the base64-encoded configuration file as the value for `<encoded_docker_configuration>`.

10. Run the following command to apply the file:

    ``` bash
    oc apply -f pull-secret.yaml
    ```

11. Configure the `Metal3Cluster` infrastructure resource, which contains information that is related to the deployment of the cluster on baremetal.

    ``` yaml
    apiVersion: infrastructure.cluster.x-k8s.io/v1beta1
    kind: Metal3Cluster
    metadata:
      name: <cluster-name>
      namespace: <cluster-namespace>
    spec:
      controlPlaneEndpoint:
        host: <cluster-name>.lab.home
        port: 6443
      noCloudProvider: true
    ```

    - The `host` is the `<clusterName>.<baseDomain>*` value with the `clusterName` from the `Cluster` resource, and the `baseDomain` is defined in the `OpenshiftAssistedControlPlane` resource.

12. Apply the file. Run the following command:

    ``` bash
    oc apply -f <filename>.yaml
    ```

13. Configure the `Metal3MachineTemplate` resource for the control plane nodes that are referenced from the `OpenshiftAssistedControlPlane` resource. See the following YAML sample:

    ``` yaml
    apiVersion: infrastructure.cluster.x-k8s.io/v1beta1
    kind: Metal3MachineTemplate
    metadata:
      name: <cluster-name>
      namespace: <cluster-namespace>
    spec:
      nodeReuse: false
      template:
        spec:
          automatedCleaningMode: disabled
          dataTemplate:
            name: <cluster-name-template>
          image:
            checksum: https://mirror.openshift.com/pub/openshift-v4/x86_64/dependencies/rhcos/4.19/4.19.0/sha256sum.txt
            checksumType: sha256
            url: https://mirror.openshift.com/pub/openshift-v4/x86_64/dependencies/rhcos/4.19/4.19.0/rhcos-4.19.0-x86_64-nutanix.x86_64.qcow2
            format: qcow2
    ---
    apiVersion: infrastructure.cluster.x-k8s.io/v1beta1
    kind: Metal3DataTemplate
    metadata:
       name: <cluster-name-template>
       namespace: <cluster-namespace>
    spec:
       clusterName: <cluster-name>
    ```

    - The `spec.template.spec.image` matches the `distributionVersion` value and the version from [OpenShift Container Platform Releases](https://mirror.openshift.com/pub/openshift-v4/x86_64/clients/ocp/latest/).

    - Set the `<cluster-name>` to the same value that it is in the `Cluster` resource

14. Apply the file. Run the following command:

    ``` bash
    oc apply -f <filename>.yaml
    ```

15. Configure worker nodes with the `MachineDeployment` resource, which refers to a `Metal3MachineTemplate`. See the following YAML example:

    ``` yaml
    apiVersion: cluster.x-k8s.io/v1beta1
    kind: MachineDeployment
    metadata:
      name: <cluster-name-worker>
      namespace: <cluster-namespace>
      labels:
        cluster.x-k8s.io/cluster-name: <cluster-name>
    spec:
      clusterName: <cluster-name>
      replicas: 2
      selector:
        matchLabels:
          cluster.x-k8s.io/cluster-name: <cluster-name>
      template:
        metadata:
          labels:
            cluster.x-k8s.io/cluster-name: <cluster-name>
        spec:
          clusterName: <cluster-name>
          bootstrap:
            configRef:
              name: <cluster-name-worker>
              apiVersion: bootstrap.cluster.x-k8s.io/v1alpha1
              kind: OpenshiftAssistedConfigTemplate
          infrastructureRef:
            name: <cluster-name-workers-2>
            apiVersion: infrastructure.cluster.x-k8s.io/v1alpha3
            kind: Metal3MachineTemplate
    ```

    - The `spec.bootstrap` configuration is also referenced in the next resource for installation.

    - The `infrastructureRef` reference points to the resource to provision.

16. Apply the file. Run the following command:

    ``` bash
    oc apply -f <filename>.yaml
    ```

17. Create the `OpenshiftAssistedConfigTemplate` resource that is referenced in the `MachineDeployment`. The following YAML defines the bootstrap configuration for worker nodes and is used to register the nodes with the Assisted Installer:

    ``` yaml
    apiVersion: bootstrap.cluster.x-k8s.io/v1alpha1
    kind: OpenshiftAssistedConfigTemplate
    metadata:
      name: <cluster-name-worker>
      namespace: <cluster-namespace>
      labels:
        cluster.x-k8s.io/cluster-name: cluster-name
    spec:
      template:
        spec:
          nodeRegistration:
            kubeletExtraLabels:
              - 'metal3.io/uuid="${METADATA_UUID}"'
          sshAuthorizedKey: "{{ ssh_authorized_key }}"
    ```

    - The `kubeletExtraLabels` cannot change from this value.

    - Enter your key in the `sshAuthorizedKey` field.

18. Create the `Metal3MachineTemplate` that is referenced in the `MachineDeployment` resource. See the following example:

    ``` yaml
    apiVersion: infrastructure.cluster.x-k8s.io/v1beta1
    kind: Metal3MachineTemplate
    metadata:
       name: <cluster-name-workers-2>
       namespace: <cluster-namespace>
    spec:
       nodeReuse: false
       template:
          spec:
             automatedCleaningMode: metadata
             dataTemplate:
                name: <cluster-name-workers-template>
          image:
            checksum: https://mirror.openshift.com/pub/openshift-v4/x86_64/dependencies/rhcos/4.19/4.19.0/sha256sum.txt
            checksumType: sha256
            url: https://mirror.openshift.com/pub/openshift-v4/x86_64/dependencies/rhcos/4.19/4.19.0/rhcos-4.19.0-x86_64-nutanix.x86_64.qcow2
            format: qcow2
    ---
    apiVersion: infrastructure.cluster.x-k8s.io/v1beta1
    kind: Metal3DataTemplate
    metadata:
       name: <cluster-name-workers-template>
       namespace: <cluster-namespace>
    spec:
       clusterName: <cluster-name>
    ```

19. Run the following command to save the YAML file and provision a cluster:

    ``` bash
    oc apply -f <filename>.yaml
    ```

</div>

<div>

<div class="title">

Verification

</div>

1.  Run `oc get cluster --namespace <cluster-namespace> <cluster-name> -o yaml` to check your `Cluster` resource status.

    See the following output and status:

    ``` yaml
    status:
      conditions:
      - lastTransitionTime: "2025-06-25T11:23:38Z"
        status: "True"
        type: Ready
      - lastTransitionTime: "2025-06-25T11:23:38Z"
        status: "True"
        type: ControlPlaneReady
      - lastTransitionTime: "2025-06-25T10:37:03Z"
        status: "True"
        type: InfrastructureReady
    ```

2.  Run the `oc get metal3cluster --namespace <cluster-namespace> <cluster-name> -o yaml` command to check your cluster infrastructure status.

    See the following output and status:

    ``` yaml
    status:
      conditions:
      - lastTransitionTime: "2025-06-25T10:37:03Z"
        status: "True"
        type: Ready
      - lastTransitionTime: "2025-06-25T10:37:03Z"
        status: "True"
        type: BaremetalInfrastructureReady
    ```

3.  Run the `oc get openshiftassistedcontrolplane --namespace <cluster-namespace> <cluster-name> -o yaml` command to check your control plane status.

    See the following output and status:

    ``` yaml
    status:
      conditions:
      - lastTransitionTime: "2025-06-25T11:23:38Z"
        status: "True"
        type: Ready
      - lastTransitionTime: "2025-06-25T11:23:38Z"
        status: "True"
        type: ControlPlaneReady
      - lastTransitionTime: "2025-06-25T10:45:48Z"
        status: "True"
        type: KubeconfigAvailable
      - lastTransitionTime: "2025-06-25T10:38:25Z"
        status: "True"
        type: MachinesCreated
      - lastTransitionTime: "2025-06-25T11:10:54Z"
        status: "True"
        type: MachinesReady
      - lastTransitionTime: "2025-06-25T11:23:38Z"
        status: "True"
        type: UpgradeCompleted
    ```

4.  Run the `oc get machinedeployment --namespace <cluster-namespace> <cluster-name> -o yaml` command to check your machine deployments status.

    See the following output and status:

    ``` yaml
    status:
      conditions:
      - lastTransitionTime: "2025-06-25T11:10:29Z"
        status: "True"
        type: Ready
      - lastTransitionTime: "2025-06-25T11:10:29Z"
        status: "True"
        type: Available
      - lastTransitionTime: "2025-06-25T11:10:29Z"
        status: "True"
        type: MachineSetReady
    ```

5.  Run the `kubectl get machine -l cluster.x-k8s.io/cluster-name=cluster-name -n test-capi -o yaml` command to check your machines.

    See the following output and status:

    ``` yaml
     status:
        conditions:
        - lastTransitionTime: "2025-06-25T11:09:57Z"
        status: "True"
        type: Ready
        - lastTransitionTime: "2025-06-25T10:38:20Z"
        status: "True"
        type: BootstrapReady
        - lastTransitionTime: "2025-06-25T11:09:57Z"
        status: "True"
        type: InfrastructureReady
        - lastTransitionTime: "2025-06-25T11:10:29Z"
        status: "True"
        type: NodeHealthy
    ```

6.  Access the cluster.

    1.  Run the following command to get the `kubeconfig` file:

        ``` bash
        oc get secret -n test-capi  cluster-name-admin-kubeconfig -o json | jq -r .data.kubeconfig | base64 --decode > kubeconfig
        ```

    2.  Run the following command to use the `kubeconfig` file to access the cluster:

    ``` bash
    export KUBECONFIG=$(realpath kubeconfig)
    oc get nodes
    ```

</div>

<a id="prep-auto-import-capi"></a>

### Preparing your hub cluster for Cluster API clusters (Technology Preview)

Before you can automatically import provisioned clusters with the Cluster API, you must complete the following procedure.

**Required access:** Cluster administrator

<div>

<div class="title">

Prerequisites

</div>

- You need the `MultiClusterEngine` resource either from the Red Hat Advanced Cluster Management installation, or the multicluster engine operator standalone installation.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Enable the `ClusterImporter` feature gate in the `ClusterManager` resource by adding the following YAML file sample:

    ``` yaml
    apiVersion: operator.open-cluster-management.io/v1
    kind: ClusterManager
    metadata:
      name: cluster-manager
    spec:
      registrationConfiguration:
        featureGates:
        - feature: ClusterImporter
          mode: Enable
    ```

2.  Configure the import controller to create cluster import configuration secrets by setting `clusterImportConfig` to `true`. Your `ConfigMap` resource might resemble the following YAML file sample:

    ``` yaml
    apiVersion: v1
    kind: ConfigMap
    metadata:
      name: import-controller-config
      namespace: multicluster-engine
    data:
      clusterImportConfig: "true"
    ```

    1.  If you do not have a `ConfigMap` resource yet, run the following command to apply the changes. Replace `<filename>` with your file name:

        ``` bash
        oc apply -f <filename>.yaml
        ```

    2.  If you already have a `ConfigMap` resource, run the following command to apply the changes:

    ``` bash
    oc patch configmap import-controller-config -n multicluster-engine --type merge -p '{"data":{"clusterImportConfig":"true"}}'
    ```

3.  Bind the Cluster API manager permissions to the import controller service account. Add the following YAML file sample:

    ``` yaml
    apiVersion: rbac.authorization.k8s.io/v1
    kind: ClusterRoleBinding
    metadata:
      name: cluster-manager-registration-capi
    roleRef:
      apiGroup: rbac.authorization.k8s.io
      kind: ClusterRole
      name: capi-manager-role
    subjects:
    - kind: ServiceAccount
      name: registration-controller-sa
      namespace: open-cluster-management-hub
    ```

4.  Run the following command to apply the changes. Replace `<filename>` with your file name:

    ``` bash
    oc apply -f <filename>.yaml
    ```

</div>

<a id="auto-import-capi"></a>

### Enabling automatic import for Cluster API clusters (Technology Preview)

You can save time by automatically importing clusters that you provision by using the Cluster API.

**Required access:** Cluster administrator

<div>

<div class="title">

Prerequisites

</div>

- You must prepare for automatic import by following the steps in [Preparing your hub cluster for Cluster API clusters (Technology Preview)](clusters.md#prep-auto-import-capi).

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create a `ManagedCluster` resource by adding the following YAML sample. Add the name of your Cluster API cluster to the `name` parameter:

    ``` yaml
    apiVersion: cluster.open-cluster-management.io/v1
    kind: ManagedCluster
    metadata:
      name: <clusterapi_cluster_name>
    spec:
      hubAcceptsClient: true
    ```

2.  Run the following command to apply the changes. Replace `<filename>` with your file name:

    ``` bash
    oc apply -f <filename>.yaml
    ```

</div>

<a id="switch-iam-roles-capi"></a>

### Switching from AWS credentials to IAM roles on your managed cluster (Technology Preview)

You can switch to using Identity and Access Management (IAM) roles when deploying a managed cluster with Cluster API. If you created a managed cluster with Amazon Web Services (AWS) credentials, you can switch from AWS credentials to IAM roles to use `cluster-api-provider-aws` to create Red Hat OpenShift Service on AWS with hosted control planes clusters without storing AWS credentials on your managed cluster.

**Required access:** Cluster administrator

<div>

<div class="title">

Prerequisites

</div>

- You need a Red Hat OpenShift Container Platform or Red Hat OpenShift Service on AWS with hosted control planes bootstrap cluster that you created with AWS credentials. You can use temporary credentials. See [Request temporary security credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_request.html) in the AWS documentation to learn more.

- You need Red Hat Advanced Cluster Management for Kubernetes installed on the bootstrap cluster.

- You need to disable HyperShift components before enabling Cluster API and Cluster API Provider AWS.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Edit the `MultiClusterEngine` resource. Run the following command:

    ``` bash
    oc edit multiclusterengine engine
    ```

2.  Disable the `hypershift` and `hypershift-local-hosting` components, and enable the `cluster-api` and `cluster-api-provider-aws` components. See the following example:

    ``` yaml
    - configOverrides: {}
      enabled: false
      name: hypershift
    - configOverrides: {}
      enabled: false
      name: hypershift-local-hosting
    - configOverrides: {}
      enabled: true
      name: cluster-api
    - configOverrides: {}
      enabled: true
      name: cluster-api-provider-aws
    ```

3.  Verify that the Cluster API and Cluster API Provider AWS deployments are running. Run the following command:

    ``` bash
    oc get deploy -n multicluster-engine
    ```

    The output might resemble the following example:

        NAME                                  READY   UP-TO-DATE   AVAILABLE   AGE
        capa-controller-manager               1/1     1            1           12d
        capi-controller-manager               1/1     1            1           12d

4.  Pause the `MultiClusterEngine` custom resource so that the Cluster API Provider AWS controller service account can update. Run the following command:

    ``` bash
    oc annotate mce multiclusterengine installer.multicluster.openshift.io/pause=true
    ```

5.  Retrieve the OpenID Connect (OIDC) provider details. Run the following command:

    ``` bash
    export OIDC_PROVIDER=$(oc get authentication.config.openshift.io cluster -ojson | jq -r .spec.serviceAccountIssuer | sed 's/https:\/\///')
    ```

6.  Set your AWS account ID. Run the following command. Change the account ID value:

    ``` bash
    export AWS_ACCOUNT_ID={YOUR_AWS_ACCOUNT_ID}
    ```

7.  Create the trust policy file for the `capa-controller-manager` IAM role. Run the following command:

    ``` bash
    cat ./trust.json
    ```

8.  Define who is allowed to assume an associated IAM role by adding the following content to the file:

    ``` bash
    {
      "Version": "2012-10-17",
      "Statement": [
        {
          "Effect": "Allow",
          "Principal": {
            "Federated": "arn:aws:iam::${AWS_ACCOUNT_ID}:oidc-provider/${OIDC_PROVIDER}"
          },
          "Action": "sts:AssumeRoleWithWebIdentity",
          "Condition": {
            "StringEquals": {
              "${OIDC_PROVIDER}:sub": "system:serviceaccount:multicluster-engine:capa-controller-manager"
            }
          }
        }
      ]
    }
    ```

9.  Create the IAM role and attach the required AWS policies. Run the following commands:

    ``` bash
    aws iam create-role --role-name "capa-manager-role" --assume-role-policy-document file://trust.json --description "IAM role for CAPA to assume"

    aws iam attach-role-policy --role-name capa-manager-role --policy-arn arn:aws:iam::aws:policy/AWSCloudFormationFullAccess

    aws iam attach-role-policy --role-name capa-manager-role --policy-arn arn:aws:iam::aws:policy/AmazonVPCFullAccess
    ```

10. Retrieve the IAM role Amazon Resource Name (ARN). Run the following commands:

    ``` bash
    export APP_IAM_ROLE_ARN=$(aws iam get-role --role-name=capa-manager-role --query Role.Arn --output text)

    export IRSA_ROLE_ARN=eks.amazonaws.com/role-arn=$APP_IAM_ROLE_ARN
    ```

11. Annotate the service account with the IAM role ARN. Run the following command:

    ``` bash
    oc annotate serviceaccount -n multicluster-engine capa-controller-manager $IRSA_ROLE_ARN
    ```

12. Restart the Cluster API Provider AWS deployment. Run the following command:

    ``` bash
    oc rollout restart deployment capa-controller-manager -n multicluster-engine
    ```

</div>

<a id="prep-create-rosa-hcp-capi-cluster"></a>

### Preparing for creating a Red Hat OpenShift Service on AWS with hosted control planes cluster with Cluster API

You need a service account, AWS credentials, and OpenShift Cluster Manager credentials before you can provision a Red Hat OpenShift Service on AWS with hosted control planes cluster.

**Required access:** Cluster administrator

<div>

<div class="title">

Prerequisites

</div>

- You need an AWS access key. See [Manage access keys for IAM users](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html) in the AWS documentation to learn more.

- The AWS Red Hat OpenShift Service on AWS (classic) managed policies are attached to your AWS user permissions. See [AWS managed policies for ROSA](https://docs.aws.amazon.com/rosa/latest/userguide/security-iam-awsmanpol.html) in the AWS documentation to learn more.

- You need the OpenShift CLI (`oc`). See [OpenShift CLI (oc)](https://docs.redhat.com/en/documentation/openshift_container_platform/4.20/html/cli_tools/openshift-cli-oc) in the OpenShift Container Platform documentation to learn more.

- You need the ROSA CLI (`rosa`). See [ROSA CLI](https://docs.redhat.com/en/documentation/red_hat_openshift_service_on_aws/4/html/cli_tools/rosa-cli) in the Red Hat OpenShift Service on AWS (classic) documentation to learn more.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create a service account by navigating to **Identity & Access Management** \> **Service Accounts** in the console. Skip to to step 4 if you already have a service account.

2.  Click the **Create service account** button.

3.  For every new service account you create, activate the account by using the ROSA CLI.

    1.  Log in to your new service account. Run the following command. Replace values where needed:

        ``` bash
        rosa login --client-id <your-client-id> --client-secret <your-client-secret>
        ```

    2.  Activate your service account. Run the following command:

    ``` bash
    rosa whoami
    ```

4.  If you are not using multi-factor authentication with AWS, set your AWS credentials by using the AWS access key you created. Run the following command. Replace values where needed:

    ``` bash
    echo '[default]
    aws_access_key_id = <your-access-key>
    aws_secret_access_key = <your-secret-access-key>
    region = us-east-1
    ' | base64 -w 0
    ```

5.  If you are using multi-factor authentication with AWS, run the following command. Replace values where needed:

    ``` bash
    echo '[default]
    aws_access_key_id = <your-access-key>
    aws_secret_access_key = <your-secret-access-key>
    aws_session_token= <your-aws-session-token>
    region = us-east-1
    ' | base64 -w 0
    ```

6.  Update the `capa-manager-bootstrap-credentials` secret.

    1.  Copy the output of the previous command and add the output to the `capa-manager-bootstrap-credentials` secret. Run the following command to edit the secret:

        ``` bash
        oc edit secret -n multicluster-engine capa-manager-bootstrap-credentials
        ```

    2.  Add your output to the `credentials` field. See the following example:

        ``` bash
        apiVersion: v1
        data:
          credentials: <your-aws-credentials>
        kind: Secret
        metadata:
            name: capa-manager-bootstrap-credentials
            namespace: multicluster-engine
        ```

        **Optional:** If you want to use AWS IAM roles with your service account to authenticate the `capa-controller-manager`, see the Additional resources section and complete the steps in *Switching from AWS credentials to IAM roles on your Cluster API managed cluster (Technology Preview)*.

7.  Restart the `capa-controller-manager` deployment. Run the following command:

    ``` bash
    oc rollout restart deployment capa-controller-manager -n multicluster-engine
    ```

8.  Create a Kubernetes secret in the target namespace with the service account credentials you created. The `ROSAControlPlane` resource references this secret during provisioning.

    1.  Create the namespace. Run the following command. Replace `<your-rosa-hcp-namespace>` with your target namespace:

        ``` bash
        oc create namespace <your-rosa-hcp-namespace>
        ```

    2.  Create the secret. Run the following command. Replace `<your-rosa-hcp-namespace>` with your target namespace:

        ``` bash
        oc -n <your-rosa-hcp-namespace> create secret generic rosa-creds-secret \
          --from-literal=ocmClientID='....' \
          --from-literal=ocmClientSecret='eyJhbGciOiJIUzI1NiIsI....' \
          --from-literal=ocmApiUrl='https://api.openshift.com'
        ```

9.  **Optional:** You can consume the secret without referencing it from your `ROSAControlPlane` resource by calling the secret `rosa-creds-secret` and creating it in the `multicluster-engine` namespace. Run the following command:

    ``` bash
    oc -n multicluster-engine create secret generic rosa-creds-secret \
      --from-literal=ocmClientID='....' \
      --from-literal=ocmClientSecret='eyJhbGciOiJIUzI1NiIsI....' \
      --from-literal=ocmApiUrl='https://api.openshift.com'
    ```

</div>

<a id="create-rosa-hcp-capi-cluster"></a>

### Creating a Red Hat OpenShift Service on AWS with hosted control planes cluster with Cluster API

A Red Hat OpenShift Service on AWS with hosted control planes cluster is a deployment model for Red Hat OpenShift Service on AWS (classic) where the cluster control plane is hosted and managed in a Red Hat Amazon Web Services (AWS) account. Complete the steps in the following topics to create a Red Hat OpenShift Service on AWS with hosted control planes cluster by using Cluster API.

**Required access:** Cluster administrator

<div>

<div class="title">

Prerequisites

</div>

- You must prepare before creating a Red Hat OpenShift Service on AWS with hosted control planes cluster. Complete the steps in [Preparing for creating a Red Hat OpenShift Service on AWS with hosted control planes cluster with Cluster API](clusters.md#prep-create-rosa-hcp-capi-cluster).

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create the `AWSClusterControllerIdentity` resource. See the following YAML file sample:

    ``` yaml
    apiVersion: infrastructure.cluster.x-k8s.io/v1beta2
    kind: AWSClusterControllerIdentity
    metadata:
      name: "default"
    spec:
      allowedNamespaces: {}
    ```

2.  Create the `ROSARoleConfig` resource . See the following YAML file sample:

    ``` yaml
    apiVersion: infrastructure.cluster.x-k8s.io/v1beta2
    kind: ROSARoleConfig
    metadata:
      name: "role-config"
      namespace: "ns-rosa-hcp"
    spec:
      accountRoleConfig:
        prefix: "rosa"
        version: "4.20.0"
      operatorRoleConfig:
        prefix: "rosa"
      credentialsSecretRef:
        name: rosa-creds-secret
      oidcProviderType: Managed
    ```

3.  Create the `ROSANetwork` resource. See the following YAML file sample:

    ``` yaml
    apiVersion: infrastructure.cluster.x-k8s.io/v1beta2
    kind: ROSANetwork
    metadata:
      name: "rosa-vpc"
      namespace: "ns-rosa-hcp"
      spec:
        region: "us-west-2"
        stackName: "rosa-hcp-net"
        availabilityZones:
        - "us-west-2a"
        - "us-west-2b"
        - "us-west-2c"
        cidrBlock: 10.0.0.0/16
        identityRef:
          kind: AWSClusterControllerIdentity
          name: default
    ```

4.  Verify that the `ROSARoleConfig` resource is created. Check that the `ROSARoleConfig` status contains the `accountRolesRef`, `oidcID`, `oidcProviderARN`, and `operatorRolesRef`. Run the following command:

    ``` bash
    oc get rosaroleconfig  -n ns-rosa-hcp role-config -o yaml
    ```

5.  Verify that the `ROSANetwork` resource is created. The `ROSANetwork` status contains the created subnets. Run the following command:

    ``` bash
    oc get rosanetwork -n ns-rosa-hcp rosa-vpc -o yaml
    ```

6.  Create the required custom resources for the `ROSAControlPlane` resource.

    1.  Create the `ManagedCluster` resource with the following YAML file content:

        ``` yaml
        apiVersion: cluster.open-cluster-management.io/v1
        kind: ManagedCluster
        metadata:
          name: rosa-hcp-1
          spec:
            hubAcceptsClient: true
        ```

    2.  Create the `Cluster` resource with the following YAML file content:

        ``` yaml
        apiVersion: cluster.x-k8s.io/v1beta1
        kind: Cluster
        metadata:
          name: "rosa-hcp-1"
          namespace: "ns-rosa-hcp"
          spec:
            clusterNetwork:
              pods:
                cidrBlocks: ["192.168.0.0/16"]
            infrastructureRef:
              apiVersion: infrastructure.cluster.x-k8s.io/v1beta2
              kind: ROSACluster
              name: "rosa-hcp-1"
              namespace: "ns-rosa-hcp"
            controlPlaneRef:
              apiVersion: controlplane.cluster.x-k8s.io/v1beta2
              kind: ROSAControlPlane
              name: "rosa-cp-1"
              namespace: "ns-rosa-hcp"
        ```

7.  Create the `ROSACluster` resource with the following YAML file content:

    ``` yaml
    apiVersion: infrastructure.cluster.x-k8s.io/v1beta2
    kind: ROSACluster
    metadata:
      name: "rosa-hcp-1"
      namespace: "ns-rosa-hcp"
      spec: {}
    ```

8.  Create the `ROSAControlPlane` resource with the following YAML file content. Make sure the `region` matches the AWS region you used to create the `ROSANetwork` resource:

    ``` yaml
    apiVersion: controlplane.cluster.x-k8s.io/v1beta2
    kind: ROSAControlPlane
    metadata:
      name: "rosa-cp-1"
      namespace: "ns-rosa-hcp"
      spec:
        credentialsSecretRef:
          name: rosa-creds-secret
        rosaClusterName: rosa-hcp-1
        domainPrefix: rosa-hcp
        rosaRoleConfigRef:
          name: role-config
        version: "4.20.0"
        region: "us-west-2"
        rosaNetworkRef:
          name: "rosa-vpc"
        network:
          machineCIDR: "10.0.0.0/16"
          podCIDR: "10.128.0.0/14"
          serviceCIDR: "172.30.0.0/16"
        defaultMachinePoolSpec:
          instanceType: "m5.xlarge"
          autoscaling:
            maxReplicas: 6
            minReplicas: 3
        additionalTags:
          env: "demo"
          profile: "hcp"
    ```

9.  Check the `ROSAControlPlane` status. Run the following command. Make sure the `READY` column says `true`:

    ``` bash
    oc get ROSAControlPlane rosa-cp-1 -n ns-rosa-hcp
    ```

    **Note:** The Red Hat OpenShift Service on AWS with hosted control planes cluster might need up to 40 minutes to fully provision.

10. After the `ROSAControlPlane` resource provisioning is completed, verify the `ROSAMachinePool` is created. Run the following command:

    ``` bash
    oc get ROSAMachinePool -n ns-rosa-hcp
    ```

    The following output might be displayed:

        NAMESPACE     NAME        READY   REPLICAS
        ns-rosa-hcp   workers-0   true    1
        ns-rosa-hcp   workers-1   true    1
        ns-rosa-hcp   workers-2   true    1

    **Note:** The default available `ROSAMachinePools` count is based on the assigned availability zones.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Switching from AWS credentials to IAM roles on your Cluster API managed cluster (Technology Preview)](clusters.md#switch-iam-roles-capi)

</div>

<a id="delete-rosa-hcp-capi-cluster"></a>

### Deleting a Red Hat OpenShift Service on AWS with hosted control planes cluster with Cluster API

Deleting the `ROSAControlPlane` deprovisions the Red Hat OpenShift Service on AWS with hosted control planes cluster. The process takes 30 to 50 minutes to complete. The associated `ROSAMachinePool` resources are automatically deleted.

**Required access:** Cluster administrator

<div>

<div class="title">

Prequisites

</div>

- You have a Red Hat OpenShift Service on AWS with hosted control planes cluster with Cluster API.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Delete the `ROSAControlPlane` custom resource and the matching cluster custom resource. Run the following command. Replace values where needed:

    ``` bash
    oc delete -n ns-rosa-hcp cluster/rosa-hcp-1 rosacontrolplane/rosa-cp-1
    ```

2.  After the `ROSAControlPlane` deletion completes, delete the `ROSARoleConfig` and `ROSANetwork` resources.

</div>
