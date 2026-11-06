> Source: [Red Hat Advanced Cluster Management for Kubernetes 2.17](https://docs.redhat.com/en/documentation/red_hat_advanced_cluster_management_for_kubernetes/2.17/html/release_notes/index). Copyright Red Hat.
> Adapted from AsciiDoc to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md), [CC BY-SA 3.0](LICENSE.md) and SOURCE.json for source revisions and gaps.

<a id="acm-release-notes"></a>

# Release notes for Red Hat Advanced Cluster Management

Learn about Red Hat Advanced Cluster Management 2.17 new features and enhancements, support, deprecations, removals, and fixed issues for errata releases.

**Important:** Cluster lifecycle components and features are within the multicluster engine operator, which is a software operator that enhances cluster fleet management. Release notes for multicluster engine operator-specific features are found in at [Release notes for the multicluster engine operator](mce_release_notes.md#mce-release-notes-intro).

Access the [Red Hat Advanced Cluster Management Support Matrix](https://access.redhat.com/articles/7142376) to learn about hub cluster and managed cluster requirements and support for each component. For lifecycle information, see [Red Hat OpenShift Container Platform Life Cycle policy](https://access.redhat.com/support/policy/updates/openshift).

- [New features and enhancements for Red Hat Advanced Cluster Management](release_notes.md#new-features-acm)

- [Fixed issues for Red Hat Advanced Cluster Management](release_notes.md#errata-acm)

- [Known issues Red Hat Advanced Cluster Management](release_notes.md#known-issues-acm)

- [Deprecations and removals for Red Hat Advanced Cluster Management](release_notes.md#deprecations-removals-acm)

- [Red Hat Advanced Cluster Management for Kubernetes considerations for GDPR readiness](release_notes.md#acm-gdpr)

- [FIPS readiness](release_notes.md#fips-readiness)

**Important:** OpenShift Container Platform release notes are not documented in this product documentation. For your OpenShift Container Platform cluster, see [OpenShift Container Platform release notes](https://docs.redhat.com/en/documentation/openshift_container_platform/4.20).

**Deprecated:** Red Hat Advanced Cluster Management 2.9 and earlier versions are no longer supported. The documentation might remain available, but without any errata releases for fixed issues or other updates.

**Best practice:** Update to the most recent version.

- The documentation references the earliest supported Red Hat OpenShift Container Platform versions, unless the component in the documentation is created and tested with only a specific version of OpenShift Container Platform.

- If you experience issues with one of the currently supported releases, or the product documentation, go to [Red Hat Support](https://www.redhat.com/en/services/support) where you can troubleshoot, view Knowledgebase articles, connect with the Support Team, or open a case. You must log in with your credentials.

- You can also learn more about the Customer Portal documentation at [Red Hat Customer Portal FAQ](https://access.redhat.com/articles/33844).

<a id="new-features-acm"></a>

## New features and enhancements for Red Hat Advanced Cluster Management

Red Hat Advanced Cluster Management for Kubernetes 2.17 provides visibility of your entire Kubernetes domain with built-in governance, cluster lifecycle management, and application lifecycle management with GitOps, along with observability.

Red Hat Advanced Cluster Management version 2.17 is released with the multicluster engine operator version 2.12 for Cluster lifecycle management. To learn about cluster management this release, see the [Release notes for the multicluster engine operator](mce_release_notes.md#mce-release-notes-intro).

Access the [Red Hat Advanced Cluster Management Support Matrix](https://access.redhat.com/articles/7142376) to learn about hub cluster and managed cluster requirements and support for each component. For lifecycle information, see [Red Hat OpenShift Container Platform Life Cycle policy](https://access.redhat.com/support/policy/updates/openshift).

**Important:**

- Red Hat Advanced Cluster Management supports all providers that are certified through the Cloud Native Computing Foundation (CNCF) Kubernetes Conformance Program. Choose a vendor that is recognized by CNCF for your hybrid cloud multicluster management. See the following information about using CNCF providers:

- Learn how CNCF providers are certified at [Certified Kubernetes Conformance](https://www.cncf.io/training/certification/software-conformance/).

- For Red Hat support information about CNCF third-party providers, see [Red Hat support with third party components](https://access.redhat.com/articles/third-party-software-support), or [Contact Red Hat support](https://access.redhat.com/support/contact/).

- If you bring your own CNCF conformance certified cluster, you need to change the OpenShift Container Platform CLI `oc` command to the Kubernetes CLI command, `kubectl`.

<a id="_general_announcements_for_this_release"></a>

### General announcements for this release

Red Hat Advanced Cluster Management is available on the [AWS Marketplace](https://aws.amazon.com/marketplace/pp/prodview-s2nb6rqz2i3ru) with either on-demand or annual pricing and a simplified billing option for running Red Hat Advanced Cluster Management on Red Hat OpenShift Service on AWS (classic) clusters. Red Hat Advanced Cluster Management on the AWS Marketplace offers billing consistency, flexible resource consumption, and cost efficiency.

- Purchase from the AWS Marketplace, then you can install `MultiClusterHub` resources and manage your clusters. To view the overall consumption, go to [console.redhat.com](https://console.redhat.com/subscriptions/usage/openshift). Click **Subscriptions Usage** \> **OpenShift**. Select **Variant: Red Hat Advanced Cluster Management** from the drop-down menu.

- Use the *Attach* feature with Red Hat OpenShift Lightspeed, a generative AI-powered virtual assistant for Red Hat OpenShift Container Platform, to add managed cluster resource details as context for questions. See the [Red Hat OpenShift Lightspeed](https://docs.redhat.com/en/documentation/red_hat_openshift_lightspeed/1.0/html/install/index) installation documentation to learn how to install Lightspeed. After installing, click **Infrastructure** \> **Clusters** \> **Cluster details** on any managed cluster page to access the assistant. The *Attach* feature automatically adds the relevant cluster YAML file details from the `ManagedCluster` and `ManagedClusterInfo` resource to the agent conversation.

<a id="_new_features_and_enhancements_for_each_component"></a>

### New features and enhancements for each component

Learn specific details about new features for components within Red Hat Advanced Cluster Management:

Some features and components are identified and released as [Technology Preview](https://access.redhat.com/support/offerings/techpreview).

Learn about Red Hat Advanced Cluster Management advanced configuration options at [MultiClusterHub advanced configuration](get_started.md#advanced-config-hub) in the documentation.

<a id="console-new-features"></a>

### Console

Learn about what is new in the Red Hat Advanced Cluster Management integrated console, which includes search capability.

- You can install the MCP server for Red Hat Advanced Cluster Management to query search data and Kubernetes resources across managed clusters from artifical intelligence (AI) assistants such as Red Hat OpenShift Lightspeed and Claude Code. See [MCP server overview (Technology Preview)](mcp.md#acm-mcp-intro).

See [Web console](console.md#web-console) for more information about the Console.

<a id="_clusters"></a>

### Clusters

For new features that are related to multicluster engine operator, see [New features and enhancements for the multicluster engine operator](mce_release_notes.md#new-features-mce) in the multicluster engine operator documentation.

- You can propagate user-defined labels to `ManagedCluster` resources for discovered hosted clusters across Red Hat Advanced Cluster Management and multicluster engine operator hub clusters. Labels added to a `HostedCluster` custom resource on an multicluster engine operator cluster are automatically applied to the corresponding `ManagedCluster` resources. Labels added to a `ManagedCluster` on the Red Hat Advanced Cluster Management hub cluster are synced to the corresponding `ManagedCluster` on the multicluster engine operator cluster. See [Label propagation for hosted clusters between Red Hat Advanced Cluster Management and multicluster engine operator hub clusters](mce_acm_integration.md#propagate-hosted-labels).

View other cluster management tasks and support information at [Cluster lifecycle with multicluster engine operator overview](clusters.md#cluster_mce_overview).

<a id="_applications_and_gitops"></a>

### Applications and GitOps

Learn about new features for application management and GitOps.

- **Technology Preview:** The Argo CD agent integration now has a `argocd-agent` mode that uses destination-based mapping for `ApplicationSet` deployment to reduce the need for prerequisite configurations. See [Argo CD with the Argo CD Agent-based pull model overview](gitops.md#gitops-pull-agent) for more information.

For other Application and GitOps topics, see [Manage applications](applications.md#managing-applications).

<a id="_observability"></a>

### Observability

Learn about new features for observability.

- **Technology Preview:** You can view hub cluster and managed cluster metrics in Perses dashboards from the OpenShift Container Platform console when you enable the multicluster observability add-on `ui` parameter in the `MultiClusterObservability` custom resource. Perses dashboards are rendered through the Cluster Observability Operator console plugin and complement existing Grafana dashboards. See [Enable Perses dashboards with the multicluster observability add-on (Technology Preview)](observability.md#enable-mcoa-perses) and [View Perses dashboards in the console](observability.md#view-perses-dashboards).

See [Observability service](observability.md#observing-environments-intro) to learn more.

<a id="_governance"></a>

### Governance

Learn about new features for Governance.

- The `spec.complianceConfig` operator policy can now detect if a minor version update is available for the operator on different channels. See [Operator policy controller](governance.md#operator-policy-ctrl) for more information.

See [Governance](governance.md#governance) to learn more about the dashboard and the policy framework.

<a id="virt-new-features"></a>

### Virtualization

Learn about new features for virtualization.

- You can now create custom `ClusterRole` resources to define environment-specific permissions for virtualization workloads. Distribute custom roles to managed clusters by using governance policies and assign them to users through `MulticlusterRoleAssignment` resources. This enables access control scenarios, such as granting console-only access to virtual machines without lifecycle control. See [Managing custom roles with *MulticlusterRoleAssignment*](secure_clusters.md#fine-grain-mca-custom) for more information.

See [Virtualization](virtualization.md#acm-virt) for more information.

<a id="_learn_more_about_this_release"></a>

### Learn more about this release

See more information about the release, as well as support information for the product.

- See more release notes, such as *Known Issues and Limitations*, in [Release notes for Red Hat Advanced Cluster Management](release_notes.md#acm-release-notes).

- Get an overview of Red Hat Advanced Cluster Management from the [Welcome to Red Hat Advanced Cluster Management for Kubernetes](about.md#welcome-to-red-hat-advanced-cluster-management-for-kubernetes) topic.

- See the [Multicluster architecture](about.md#multicluster-architecture) topic to learn more about major components of the product.

- See support information and more in the Red Hat Advanced Cluster Management [Troubleshooting](troubleshooting.md#troubleshooting).

- Access the open source *Open Cluster Management* community for interaction, growth, and contributions from the open community. To get involved, see [open-cluster-management.io](https://open-cluster-management.io/).

<a id="errata-acm"></a>

## Fixed issues for Red Hat Advanced Cluster Management

By default, fixed issues for *errata* releases are automatically applied when released. The details are published here when the release is available. If no release notes are listed, the product does not have an errata release at this time.

**Important:** For reference, Jira links and Jira numbers might be added to the content and used internally. Links that require access might not be available for the user. Learn about the types of [errata releases](https://access.redhat.com/security/updates/advisory) from Red Hat.

See [Updating your hub cluster](get_started.md#updating-hub) for more information about updates.

**Important:** Cluster lifecycle components and features are within the multicluster engine operator, which is a software operator that enhances cluster fleet management. Release notes for multicluster engine operator-specific features are found in at [Release notes for the multicluster engine operator](mce_release_notes.md#mce-release-notes-intro).

<a id="known-issues-acm"></a>

## Known issues Red Hat Advanced Cluster Management

Review the known issues for application management. The following list contains known issues for this release, or known issues that continued from the previous release.

**Important:** Cluster lifecycle components and features are within the multicluster engine operator, which is a software operator that enhances cluster fleet management. Release notes for multicluster engine operator-specific features are found in at [Release notes for the multicluster engine operator](mce_release_notes.md#mce-release-notes-intro).

- [Installation known issues](release_notes.md#known-issues-install)

- [Business continuity known issues](release_notes.md#known-issues-continuity)

- [Console known issues](release_notes.md#known-issues-console)

- [Cluster management known issues](release_notes.md#known-issues-cluster)

- [Virtualization known issues](release_notes.md#known-issues-virt)

- [Application known issues](release_notes.md#known-issues-apps)

- [Observability known issues](release_notes.md#known-issues-observability)

- [Governance known issues](release_notes.md#known-issues-governance)

- [Networking known issues](release_notes.md#known-issues_submariner)

- [Global Hub known issues](release_notes.md#known-issues-global-hub)

**Important:** OpenShift Container Platform release notes are not documented in this product documentation. For your OpenShift Container Platform cluster, see [OpenShift Container Platform release notes](https://docs.redhat.com/en/documentation/openshift_container_platform/4.20).

For more about deprecations and removals, see [Deprecations and removals for Red Hat Advanced Cluster Management](release_notes.md#deprecations-removals-acm).

<a id="known-issues-install"></a>

### Installation known issues

Review the known issues for installing and updating. The following list contains known issues for this release, or known issues that continued from the previous release.

For your Red Hat OpenShift Container Platform cluster, see [OpenShift Container Platform known issues](https://docs.redhat.com/en/documentation/openshift_container_platform/4.20/html/release_notes/#ocp-4-15-known-issues).

For more about deprecations and removals, see [Deprecations and removals for Red Hat Advanced Cluster Management](release_notes.md#deprecations-removals-acm).

- [Uninstalling and reinstalling earlier versions with an update can fail](release_notes.md#uninstall-manual-remove-cr)

- [The *kubevirt-hyperconverged* add-on is stuck in `in progress` during update](release_notes.md#add-on-stuck-update)

<a id="uninstall-manual-remove-cr"></a>

#### Uninstalling and reinstalling earlier versions with an update can fail

Uninstalling Red Hat Advanced Cluster Management from OpenShift Container Platform can cause issues if you later want to install earlier versions and then update. For instance, when you uninstall Red Hat Advanced Cluster Management, then install an earlier version of Red Hat Advanced Cluster Management and update that version, the update might fail. The update fails if the custom resources were not removed.

<div>

<div class="title">

Procedure

</div>

- Follow the [Cleaning up artifacts before reinstalling](get_started.md#cleanup-reinstall) procedure to prevent this problem.

</div>

<div>

<div class="title">

Additional resources

</div>

- [ACM-14343](https://issues.redhat.com/browse/ACM-14343)

</div>

<a id="add-on-stuck-update"></a>

#### The *kubevirt-hyperconverged* add-on is stuck in `in progress` during update

During an update from Red Hat Advanced Cluster Management 2.16 to 2.17, the `kubevirt-hyperconverged-operator` resource is not cleaned up and you receive the following error in the `ManifestWork` resource:

``` bash
Failed to apply manifest: operatorpolicies.policy.open-cluster-management.io
"kubevirt-hyperconverged-operator" is forbidden: User
"system:serviceaccount:open-cluster-management-agent:klusterlet-work-sa"
cannot get resource "operatorpolicies" in API group
"policy.open-cluster-management.io" in the namespace "open-cluster-management-policies"
```

To resolve the issue, complete the following steps:

<div>

<div class="title">

Procedure

</div>

1.  Remove existing resources. Run the following commands:

    ``` bash
    oc delete clustermanagementaddon kubevirt-hyperconverged-operator --ignore-not-found

    oc delete addontemplate kubevirt-hyperconverged-operator --ignore-not-found
    ```

2.  Get the namespace that is specified in the `installer.namespace` label of the `kubevirt-hyperconverged` `ClusterManagementAddOn` resource. Run the following command and record the output to use in step 4:

    ``` bash
    oc get clustermanagementaddon kubevirt-hyperconverged -o jsonpath='{.metadata.labels.installer\.namespace}'
    ```

3.  Delete the previous `ClusterManagementAddOn` resource, which is version `v1alpha1`. Run the following command:

    ``` bash
    oc delete clustermanagementaddon kubevirt-hyperconverged
    ```

4.  Create the `ClusterManagementAddOn` resource. See the following example and replace `<installer_namespace>` with the value that you retrieved in the previous step:

    ``` yaml
    apiVersion: addon.open-cluster-management.io/v1beta1
    kind: ClusterManagementAddOn
    metadata:
      name: kubevirt-hyperconverged
      annotations:
        addon.open-cluster-management.io/lifecycle: "addon-manager"
    spec:
      addOnMeta:
        description: Kubevirt Hyperconverged
        displayName: Kubevirt Hyperconverged
      defaultConfigs:
        - group: addon.open-cluster-management.io
          resource: addontemplates
          name: kubevirt-hyperconverged
      installStrategy:
        type: Placements
        placements:
        - name: openshift-cnv
          namespace: <installer_namespace>
    ```

5.  Run the following command to apply your resource:

    ``` bash
    oc apply -f <filename.yaml>
    ```

</div>

<div>

<div class="title">

Additional resources

</div>

- [ACM-31036](https://issues.redhat.com/browse/ACM-31036)

</div>

<a id="known-issues-continuity"></a>

### Business continuity known issues

Review the known issues for Red Hat Advanced Cluster Management for Kubernetes. The following list contains known issues for this release, or known issues that continued from the previous release.

For your Red Hat OpenShift Container Platform cluster, see [OpenShift Container Platform known issues](https://docs.redhat.com/en/documentation/openshift_container_platform/4.20/html/release_notes/#ocp-4-15-known-issues).

For more about deprecations and removals, see [Deprecations and removals for Red Hat Advanced Cluster Management](release_notes.md#deprecations-removals-acm).

- [Passive sync restore does not recover after transient *BackupStorageLocation* failures](release_notes.md#passive-sync-restore-failed)

- [Velero restore limitations](release_notes.md#restore-limitations)

- [Passive configurations do not display managed clusters](release_notes.md#imported-clusters-not-displayed)

- [Managed cluster resource not restored](release_notes.md#managed-cluster-resources-not-restored)

- [Restored Hive managed clusters not connecting with the new hub cluster](release_notes.md#restored-hive-managed-clusters-unable-new-hub)

- [Imported managed clusters show a *Pending Import* status](release_notes.md#imported-managed-clusters-pending-import)

- [The *appliedmanifestwork* is not removed after restoring the hub cluster](release_notes.md#appliedmanifestwork-not-removed)

- [Managed clusters with custom CA certificates fail to reconnect after hub restore](release_notes.md#ca-certificate-hub-restore)

<a id="passive-sync-restore-failed"></a>

#### Passive sync restore does not recover after transient *BackupStorageLocation* failures

When you configure a `Restore` resource in passive sync mode by setting `syncRestoreWithNewBackups` to `true`, and the `BackupStorageLocation` becomes temporarily unavailable, the Velero restore operation fails with a `FailedValidation` status.

After you restore the `BackupStorageLocation` and create successsful backups, the Red Hat Advanced Cluster Management `Restore` resource remains in the `Error` phase. This happens because failed Velero restore objects persist in the cluster, which prevents the controller from attempting new restores.

The issue causes the following conditions:

- The secondary hub cluster appears unhealthy.

- Automated disaster recovery scripts or tools identify the cluster as not ready for switchover.

- The `Restore` operation does not automatically resume sync operations after you resolve the `BackupStorageLocation` issue.

<div>

<div class="title">

Procedure

</div>

- Delete the failed Velero restore objects. Run the following command. Replace `<failed_restore_name>` with the name of the failed Velero restore object:

  ``` bash
  oc -n open-cluster-management-backup delete restore.velero.io <failed_restore_name>
  ```

  After the failed objects are deleted, the `Restore` controller performs the following actions:

  - Detects that the Velero restore objects are missing.

  - Creates new Velero restore objects based on the latest backups.

  - Updates the `Restore` resource phase to `Enabled`.

</div>

<a id="restore-limitations"></a>

#### Velero restore limitations

A new hub cluster can have a different configuration than the active hub cluster if the new hub cluster, where the data is restored, has user-created resources. For example, this can include an existing policy that was created on the new hub cluster before the backup data is restored on the new hub cluster.

Velero skips existing resources if they are not part of the restored backup, so the policy on the new hub cluster remains unchanged, resulting in a different configuration between the new hub cluster and active hub cluster.

To address this limitation, the cluster backup and restore operator runs a post restore operation to clean up the resources created by the user or a different restore operation when a `restore.cluster.open-cluster-management.io` resource is created. For more information, see the [Cleaning the hub cluster after restore](business_continuity.md#clean-hub-restore) topic.

<div>

<div class="title">

Additional resources

</div>

- [GH-21861](https://github.com/stolostron/backlog/issues/21861)

</div>

<a id="imported-clusters-not-displayed"></a>

#### Passive configurations do not display managed clusters

Managed clusters are only displayed when the activation data is restored on the passive hub cluster.

<div>

<div class="title">

Additional resources

</div>

- [GH-22098](https://github.com/stolostron/backlog/issues/22098)

</div>

<a id="managed-cluster-resources-not-restored"></a>

#### Managed cluster resource not restored

When you restore the settings for the `local-cluster` managed cluster resource and overwrite the `local-cluster` data on a new hub cluster, the settings are misconfigured. Content from the previous hub cluster `local-cluster` is not backed up because the resource contains `local-cluster` specific information, such as the cluster URL details.

<div>

<div class="title">

Procedure

</div>

- Apply any configuration changes that are related to the `local-cluster` resource on the restored cluster. See *Prepare the new hub cluster* in the [Install the backup and restore operator](business_continuity.md#dr4hub-install-backup-and-restore) topic.

</div>

<div>

<div class="title">

Additional resources

</div>

- [GH-21054](https://github.com/stolostron/backlog/issues/21054)

</div>

<a id="restored-hive-managed-clusters-unable-new-hub"></a>

#### Restored Hive managed clusters not connecting with the new hub cluster

When you restore the backup of the changed or rotated certificate of authority (CA) for the Hive managed cluster, on a new hub cluster, the managed cluster fails to connect to the new hub cluster. The connection fails because the `admin` `kubeconfig` secret for this managed cluster, available with the backup, is no longer valid.

<div>

<div class="title">

Procedure

</div>

- Update the restored `admin` `kubeconfig` secret of the managed cluster on the new hub cluster.

</div>

<div>

<div class="title">

Additional resources

</div>

- [GH-25461](https://github.com/stolostron/backlog/issues/25461)

</div>

<a id="imported-managed-clusters-pending-import"></a>

#### Imported managed clusters show a *Pending Import* status

Managed clusters that are manually imported on the primary hub cluster show a `Pending Import` status when the activation data is restored on the passive hub cluster. For more information, see [Connecting clusters by using a Managed Service Account](business_continuity.md#auto-connect-clusters-msa).

<div>

<div class="title">

Additional resources

</div>

- [ACM-1890](https://issues.redhat.com/browse/ACM-1890)

</div>

<a id="appliedmanifestwork-not-removed"></a>

#### The *appliedmanifestwork* is not removed after restoring the hub cluster

When the hub cluster data is restored on the new hub cluster, the `appliedmanifestwork` is not removed from managed clusters that have a placement rule for an application subscription that is not a fixed cluster set.

See the following example of a placement rule for an application subscription that is not a fixed cluster set:

``` yaml
spec:
  clusterReplicas: 1
  clusterSelector:
    matchLabels:
      environment: dev
```

As a result, the application is orphaned when the managed cluster is detached from the restored hub cluster.

<div>

<div class="title">

Procedure

</div>

1.  Specify a fixed cluster set in the placement rule. See the following example:

    ``` yaml
    spec:
      clusterSelector:
        matchLabels:
          environment: dev
    ```

2.  Delete the remaining `appliedmanifestwork` manually by running the following command:

    ``` bash
    oc delete appliedmanifestwork <the-left-appliedmanifestwork-name>
    ```

</div>

<div>

<div class="title">

Additional resources

</div>

- [GH-27129](https://github.com/stolostron/backlog/issues/27129)

</div>

<a id="ca-certificate-hub-restore"></a>

#### Managed clusters with custom CA certificates fail to reconnect after hub restore

After you restore the backup of a hub cluster that manages a cluster with custom CA certificates, the connection between the managed cluster and the hub cluster might fail. This is because the CA certificate was not backed up on the restored hub cluster.

<div>

<div class="title">

Procedure

</div>

- Copy the custom CA certificate information that is in the namespace of your managed cluster to the `<managed_cluster>-admin-kubeconfig` secret on the restored hub cluster.

  **Note:** If you copy this CA certificate to the hub cluster before creating the backup copy, the backup copy includes the secret information. When you use the backup copy to restore in the future, the connection between the hub cluster and managed cluster automatically completes.

</div>

<div>

<div class="title">

Additional resources

</div>

- [GH-19481](https://github.com/stolostron/backlog/issues/19481)

</div>

<a id="known-issues-console"></a>

### Console known issues

Review the known issues for the console. The following list contains known issues for this release, or known issues that continued from the previous release.

For your Red Hat OpenShift Container Platform cluster, see [OpenShift Container Platform known issues](https://docs.redhat.com/en/documentation/openshift_container_platform/4.20/html/release_notes#ocp-4-15-known-issues).

For more about deprecations and removals, see [Deprecations and removals for Red Hat Advanced Cluster Management](release_notes.md#deprecations-removals-acm).

- [*klusterlet-addon-search* pod fails](release_notes.md#klusterlet-addon-search-crashing)

- [Search does not display node information from the managed cluster](release_notes.md#search-display-node-managed)

- [Cannot update OpenShift Dedicated in console](release_notes.md#cannot-update-osd-ui)

- [Search PostgreSQL pod is in CrashLoopBackoff state](release_notes.md#search-postgres-crashloopbackoff)

- [Cannot edit namespace bindings for cluster set](release_notes.md#clusterset-ns-bindings)

- [Horizontal scrolling fails after provisioning hosted control plane cluster](release_notes.md#scrolling-hosted)

- [Issues with entering the *cluster-ID* in the OpenShift Cloud Manager console](release_notes.md#cluster-id-ocm-console)

<a id="klusterlet-addon-search-crashing"></a>

#### *klusterlet-addon-search* pod fails

The `klusterlet-addon-search` pod fails because the memory limit is reached.

<div>

<div class="title">

Procedure

</div>

- Update the memory request and limit by customizing the `klusterlet-addon-search` deployment on your managed cluster. Edit the `ManagedclusterAddon` custom resource named `search-collector`, on your hub cluster. Add the following annotations to the `search-collector` and update the memory, `addon.open-cluster-management.io/search_memory_request=512Mi` and `addon.open-cluster-management.io/search_memory_limit=1024Mi`.

  For example, if you have a managed cluster named `foobar`, run the following command to change the memory request to `512Mi` and the memory limit to `1024Mi`:

  ``` bash
  oc annotate managedclusteraddon search-collector -n foobar \
  addon.open-cluster-management.io/search_memory_request=512Mi \
  addon.open-cluster-management.io/search_memory_limit=1024Mi
  ```

</div>

<div>

<div class="title">

Additional resources

</div>

- [GH-27173](https://github.com/stolostron/backlog/issues/27173)

</div>

<a id="search-display-node-managed"></a>

#### Search does not display node information from the managed cluster

Search maps RBAC for resources in the hub cluster. Depending on user RBAC settings, users might not see node data from the managed cluster. Results from search might be different from what is displayed on the *Nodes* page for a cluster.

<div>

<div class="title">

Additional resources

</div>

- [GH-4598](https://github.com/stolostron/backlog/issues/4598)

</div>

<a id="cannot-update-osd-ui"></a>

#### Cannot update OpenShift Dedicated in console

From the console you can request an update for OpenShift Dedicated clusters, but the update fails with the `Cannot upgrade non openshift cluster` error message. Currently there is no workaround.

<div>

<div class="title">

Additional resources

</div>

- [ACM-10143](https://issues.redhat.com/browse/ACM-10143)

</div>

<a id="search-postgres-crashloopbackoff"></a>

#### Search PostgreSQL pod is in CrashLoopBackoff state

The `search-postgres` pod is in `CrashLoopBackoff` state. If Red Hat Advanced Cluster Management is deployed in a cluster with nodes that have the `hugepages` parameter enabled and the `search-postgres` pod gets scheduled in these nodes, then the pod does not start.

Complete the following steps to increase the memory of the `search-postgres` pod:

<div>

<div class="title">

Procedure

</div>

1.  Pause the `search-operator` pod with the following command:

    ``` bash
    oc annotate search search-v2-operator search-pause=true
    ```

2.  Update the `search-postgres` deployment with a limit for the `hugepages` parameter. Run the following command to set the `hugepages` parameter to `512Mi`:

    ``` bash
    oc patch deployment search-postgres --type json -p '[{"op": "add", "path": "/spec/template/spec/containers/0/resources/limits/hugepages-2Mi", "value":"512Mi"}]'
    ```

3.  Before you verify the memory usage for the pod, make sure your `search-postgres` pod is in the `Running` state. Run the following command:

    ``` bash
    oc get pod <your-postgres-pod-name>  -o jsonpath="Status: {.status.phase}"
    ```

4.  Run the following command to verify the memory usage of the `search-postgres` pod:

    ``` bash
    oc get pod <your-postgres-pod-name> -o jsonpath='{.spec.containers[0].resources.limits.hugepages-2Mi}'
    ```

    The following value appears: `512Mi`.

</div>

<div>

<div class="title">

Additional resources

</div>

- [ACM-7467](https://issues.redhat.com/browse/ACM-7467)

</div>

<a id="clusterset-ns-bindings"></a>

#### Cannot edit namespace bindings for cluster set

When you edit namespace bindings for a cluster set with the `admin` role or `bind` role, you might encounter an error that resembles the following message:

`ResourceError: managedclustersetbindings.cluster.open-cluster-management.io "<cluster-set>" is forbidden: User "<user>" cannot create/delete resource "managedclustersetbindings" in API group "cluster.open-cluster-management.io" in the namespace "<namespace>".`

<div>

<div class="title">

Procedure

</div>

- Make sure you also have permission to create or delete a `ManagedClusterSetBinding` resource in the namespace you want to bind. The role bindings only allow you to bind the cluster set to the namespace.

</div>

<div>

<div class="title">

Additional resources

</div>

- [GH-25389](https://github.com/stolostron/backlog/issues/25389)

</div>

<a id="scrolling-hosted"></a>

#### Horizontal scrolling fails after provisioning hosted control plane cluster

After provisioning a hosted control plane cluster, you might not be able to scroll horizontally in the cluster overview of the Red Hat Advanced Cluster Management console if the `ClusterVersionUpgradeable` parameter is too long. You cannot view the hidden data as a result.

<div>

<div class="title">

Procedure

</div>

- Zoom out by using your browser zoom controls, increase your Red Hat Advanced Cluster Management console window size, or copy and paste the text to a different location.

</div>

<div>

<div class="title">

Additional resources

</div>

- [GH-27107](https://github.com/stolostron/backlog/issues/27107)

</div>

<a id="cluster-id-ocm-console"></a>

#### Issues with entering the *cluster-ID* in the OpenShift Cloud Manager console

If you did not access the `cluster-ID` in the OpenShift Cloud Manager console, you can still get a description of your Red Hat OpenShift Service on AWS (classic) `cluster-ID` from the terminal. You need the Red Hat OpenShift Service on AWS (classic) command line interface. See [Getting started with the Red Hat OpenShift Service on AWS (classic) CLI](https://docs.redhat.com/en/documentation/red_hat_openshift_service_on_aws/4/html/rosa_cli/rosa-get-started-cli#rosa-get-started-cli) documentation.

<div>

<div class="title">

Procedure

</div>

- Run the following command from the Red Hat OpenShift Service on AWS (classic) command line interface:

  ``` bash
  rosa describe cluster --cluster=<cluster-name> | grep -o '^ID:.*'
  ```

</div>

<div>

<div class="title">

Additional resources

</div>

- [ACM-10651](https://issues.redhat.com/browse/ACM-10651)

</div>

<a id="known-issues-cluster"></a>

### Cluster management known issues

Review the known issues for *Cluster management* with Red Hat Advanced Cluster Management. The following list contains Known issues this release, or known issues that continued from the previous release.

For Cluster management with the stand-alone multicluster engine operator known issues and limitations, see [Cluster lifecycle known issues and limitations](mce_release_notes.md#known-issues-mce) in the multicluster engine operator documentation.

- [Hub cluster communication limitations](release_notes.md#hub-cluster-one-way-limits)

- [The local-cluster might not be automatically recreated](release_notes.md#local-cluster-auto)

- [Local-cluster status offline after reimporting with a different name](release_notes.md#cluster-local-offline-reimport)

- [Hub cluster and managed clusters clock not synced](release_notes.md#hub-managed-clusters-clock)

<a id="hub-cluster-one-way-limits"></a>

#### Hub cluster communication limitations

The following limitations occur if the hub cluster is not able to reach or communicate with the managed cluster:

<div>

<div class="title">

Procedure

</div>

1.  Import a managed cluster manually by using the command line interface or by using the **Run import commands manually** option in the console. You cannot create a new managed cluster by using the console.

2.  Use AppSub or the ArgoCD pull model if you deploy an Application or ApplicationSet by using the console, or if you import a managed cluster into ArgoCD. The hub cluster ArgoCD controller calls the managed cluster API server.

</div>

<div>

<div class="title">

Additional resources

</div>

- [ACM-6292](https://issues.redhat.com/browse/ACM-6292)

</div>

<a id="local-cluster-auto"></a>

#### The local-cluster might not be automatically recreated

If the local-cluster is deleted while `disableHubSelfManagement` is set to `false`, the local-cluster is recreated by the `MulticlusterHub` operator. After you detach a local-cluster, the local-cluster might not be automatically recreated.

<div>

<div class="title">

Procedure

</div>

1.  Modify a resource that is watched by the `MulticlusterHub` operator. See the following example:

    ``` bash
    oc delete deployment multiclusterhub-repo -n <namespace>
    ```

2.  Set the `disableHubSelfManagement` to true in the `MultiClusterHub` to properly detach the local-cluster.

</div>

<div>

<div class="title">

Additional resources

</div>

- [GH-17790](https://github.com/stolostron/backlog/issues/17790)

</div>

<a id="cluster-local-offline-reimport"></a>

#### Local-cluster status offline after reimporting with a different name

When you accidentally try to reimport the cluster named `local-cluster` as a cluster with a different name, the status for `local-cluster` and for the reimported cluster display `offline`. To recover from this case, complete the following steps:

<div>

<div class="title">

Procedure

</div>

1.  Run the following command on the hub cluster to edit the setting for self-management of the hub cluster temporarily:

    ``` bash
    oc edit mch -n open-cluster-management multiclusterhub
    ```

2.  Add the setting `spec.disableSelfManagement=true`.

3.  Run the following command on the hub cluster to delete and redeploy the local-cluster:

    ``` bash
    oc delete managedcluster local-cluster
    ```

4.  Enter the following command to remove the `local-cluster` management setting:

    ``` bash
    oc edit mch -n open-cluster-management multiclusterhub
    ```

5.  Remove `spec.disableSelfManagement=true` that you previously added.

</div>

<div>

<div class="title">

Additional resources

</div>

- [GH-16977](https://github.com/stolostron/backlog/issues/16977)

</div>

<a id="hub-managed-clusters-clock"></a>

#### Hub cluster and managed clusters clock not synced

Hub cluster and manage cluster time might become out-of-sync, displaying in the console `unknown` and eventually `available` within a few minutes.

<div>

<div class="title">

Procedure

</div>

- Configure the OpenShift Container Platform hub cluster time correctly. See [Customizing nodes](https://docs.redhat.com/en/documentation/openshift_container_platform/4.20/html/installation_configuration/installing-customizing).

</div>

<div>

<div class="title">

Additional resources

</div>

- [GH-5636](https://github.com/stolostron/backlog/issues/5636)

</div>

<a id="known-issues-virt"></a>

### Virtualization known issues

Review the known issues for Red Hat Advanced Cluster Management Virtualization capability. The following list contains known issues for this release, or known issues that continued from the previous release.

For your Red Hat OpenShift Container Platform cluster, see [OpenShift Container Platform known issues](https://docs.redhat.com/en/documentation/openshift_container_platform/4.20/html/release_notes/ocp-4-20-release-notes#ocp-release-known-issues_release-notes).

For more about deprecations and removals, see [Deprecations and removals for Red Hat Advanced Cluster Management](release_notes.md#deprecations-removals-acm).

See the following known issues and limitations that might occur while using Red Hat OpenShift Virtualization with Red Hat Advanced Cluster Management:

- [Red Hat Advanced Cluster Management Virtualization requires Red Hat OpenShift Virtualization 4.20.1 or later](release_notes.md#virt-requires-4-20-1-or-later)

- [Search results for virtual machine only are displayed](release_notes.md#search-vm-resources)

<a id="virt-requires-4-20-1-or-later"></a>

#### Red Hat Advanced Cluster Management Virtualization requires Red Hat OpenShift Virtualization 4.20.1 or later

Red Hat Advanced Cluster Management 2.15 Virtualization with Red Hat OpenShift Virtualization 4.20 is not supported. You need to use Red Hat OpenShift Virtualization 4.20.1 or later with Red Hat Advanced Cluster Management 2.15.

<a id="search-vm-resources"></a>

#### Search results for virtual machine only are displayed

After you enable fine-grained RBAC and attempt to search resources, only virtual machine resources in the `kubevirt.io` `ClusterRoles` are displayed and not other resources. To workaround this issue, disable the `fine-grained-rbac` feature.

<div>

<div class="title">

Procedure

</div>

1.  Edit your `MultiClusterHub` resource by running the following command:

    ``` bash
    oc edit mch -n open-cluster-management multiclusterhub
    ```

2.  Edit to change the `configOverrides` specification from `enabled: true` to `enabled: false`. See the following example with the feature disabled:

    ``` yaml
        - configOverrides: {}
          enabled: false
          name: fine-grained-rbac
    ```

</div>

<div>

<div class="title">

Additional resources

</div>

- [ACM-26537](https://issues.redhat.com/browse/ACM-26537)

</div>

<a id="known-issues-apps"></a>

### Application known issues and limitations

Review the known issues for application management. The following list contains known issues for this release, or known issues that continued from the previous release.

For your Red Hat OpenShift Container Platform cluster, see [OpenShift Container Platform known issues](https://docs.redhat.com/en/documentation/openshift_container_platform/4.20/html/release_notes/#ocp-4-15-known-issues).

For more about deprecations and removals, see [Deprecations and removals for Red Hat Advanced Cluster Management](release_notes.md#deprecations-removals-acm).

See the following known issues for the Application lifecycle component.

- [Subscription users without administrator rights cannot deploy cluster-scoped resources](release_notes.md#admin-rights-required)

- [*ManifestWork*-based Pull model applications are rejected in non-default `ApplicationSet` namespaces](release_notes.md#argo-pull-model-appset-non-default-namespace)

- [Cluster administrator subscriptions delay initial resource deployment](release_notes.md#admin-sub-delay)

- [Updating to Red Hat OpenShift GitOps 1.17 causes permission errors](release_notes.md#updating-permission-errors)

- [Subscription application displays incorrect warning message](release_notes.md#sub-app-incorrect-warning)

- [The console menu of the Application table can be difficult to click](release_notes.md#app-table-menu)

- [Application topology displays invalid expression](release_notes.md#topology-displays-invalid-expression)

- [Editing *PlacementRule* subscriptions does not display YAML in editor](release_notes.md#edit-sub-placement-rule)

- [Helm Chart with secret dependencies cannot be deployed by subscription](release_notes.md#helm-secret-dependencies)

- [Topology does not display correctly for Argo CD pull model `ApplicationSet`](release_notes.md#argo-pull-topology)

- [Local cluster is excluded as a managed cluster for pull model](release_notes.md#argo-pull-local-excluded)

- [Argo CD and propagation controllers might reconcile simultaneously](release_notes.md#argo-pull-model-controller)

- [Resource fails to deploy](release_notes.md#argo-pull-model-resource)

- [Resource allocation might take several minutes](release_notes.md#argo-pull-model-large)

- [Application ObjectBucket channel type cannot use allow and deny lists](release_notes.md#object-bucket-sub-admin)

- [Changes to the multicluster_operators_subscription image do not take effect automatically](release_notes.md#changes-not-automatic)

- [Policy resource not deployed unless by subscription administrator](release_notes.md#policy-needs-sub-admin)

- [Application Ansible hook stand-alone mode](release_notes.md#app-ansible-standalone)

- [Application not deployed after an updated placement rule](release_notes.md#app-placement-not-deployed)

- [Subscription operator does not create an SCC](release_notes.md#sub-operator-does-not-create-an-scc)

- [Application channels require unique namespaces](release_notes.md#app-channel-namespaces)

- [Ansible Automation Platform job fail](release_notes.md#ansible-automation-platform-fail)

- [Ansible Automation Platform operator access Ansible Automation Platform outside of a proxy](release_notes.md#ansible-automation-operator-access)

- [Application name requirements](release_notes.md#app-name)

- [Application console table limitations](release_notes.md#app-tables)

- [No Application console topology filtering](release_notes.md#app-topology)

- [*ClusterPermission* resource fails when creating many role bindings](release_notes.md#cluster-permission-fails)

<a id="admin-rights-required"></a>

#### Subscription users without administrator rights cannot deploy cluster-scoped resources

If you don’t have the `open-cluster-management:subscription-admin` `ClusterRoleBinding`, and create or update a `Subscription` resource, the subscription cannot deploy cluster-scoped resources through a Git, Helm repository, or object storage channel subscription. Examples of some cluster-scoped resources include `ClusterRoleBinding`, `ClusterRole`, `Namespace`, and `CustomResourceDefinition`.

As a result, the subscription deploys only namespace-scoped resources.

<div>

<div class="title">

Procedure

</div>

- Bind the user who creates or updates the `Subscription` resource to the `open-cluster-management:subscription-admin` `ClusterRoleBinding` on the hub cluster.

</div>

<div>

<div class="title">

Additional resources

</div>

- [ACM-39827](https://issues.redhat.com/browse/ACM-39827)

</div>

<a id="argo-pull-model-appset-non-default-namespace"></a>

#### *ManifestWork*-based Pull model applications are rejected in non-default `ApplicationSet` namespaces

When an `ApplicationSet` runs outside the `openshift-gitops` namespace by using the *ApplicationSet in any namespace* feature, the controller creates generated pull-model `Application` objects in that custom namespace.

The tenant-isolation check requires a `PlacementDecision` in the `Application` namespace that selects the target cluster before the controller creates a `ManifestWork`. Without that `PlacementDecision`, the controller silently rejects the applications, and the applications never propagate to managed clusters.

The check prevents a namespace with only the permission to create `Application` resources from targeting any managed cluster.

<div>

<div class="title">

Procedure

</div>

- Create a `ManagedClusterSetBinding` and a `Placement` that selects the target cluster or clusters in the `ApplicationSet` namespace. See the following example:

  ``` yaml
  apiVersion: cluster.open-cluster-management.io/v1beta2
  kind: ManagedClusterSetBinding
  metadata:
    name: global
    namespace: <applicationset-namespace>
  spec:
    clusterSet: global
  ---
  apiVersion: cluster.open-cluster-management.io/v1beta1
  kind: Placement
  metadata:
    name: my-managed-cluster-1
    namespace: <applicationset-namespace>
  spec:
    tolerations:
    - key: cluster.open-cluster-management.io/unreachable
      operator: Exists
    - key: cluster.open-cluster-management.io/unavailable
      operator: Exists
    predicates:
    - requiredClusterSelector:
        labelSelector:
          matchExpressions:
          - key: name
            operator: In
            values:
            - <target-managed-cluster-name>
  ```

</div>

<div>

<div class="title">

Additional resources

</div>

- [ACM-39827](https://issues.redhat.com/browse/ACM-39827)

</div>

<a id="admin-sub-delay"></a>

#### Cluster administrator subscriptions delay initial resource deployment

Subscriptions that use `cluster-admin` privilege elevation on a managed cluster experience a delay in initial resource deployment. The subscription controller confirms cluster administrator eligibility by checking whether the subscription appears in the `status.appliedResources` field of the `AppliedManifestWork`. The work agent populates the field at different times after you create the subscription.

If the first local subscription reconcile runs before the work agent updates that status, the controller treats the `cluster-admin` status as unresolved and does not deploy resources during that reconcile cycle. As a result, the deployment is delayed.

If the work agent status is up to date when the first reconcile runs, no delay occurs. Otherwise, resource deployment begins after one to three subscription reconcile loops complete. The default reconcile interval in appsub mode is 3 minutes for each loop, so deployment can begin up to 9 minutes after you create the subscription.

<div>

<div class="title">

Additional resources

</div>

- [ACM-39827](https://issues.redhat.com/browse/ACM-39827)

</div>

<a id="updating-permission-errors"></a>

#### Updating to Red Hat OpenShift GitOps 1.17 causes permission errors

When you update your OpenShift GitOps operator to version 1.17, you get permission errors in your `ApplicationSet` resource status. To workaround this issue, complete the following steps:

<div>

<div class="title">

Procedure

</div>

1.  Go to the `openshift-gitops` namespace and delete the `RoleBinding` resource named `openshift-gitops-applicationset-controller-placement`.

2.  Restart the `multicluster-operators-application-\*\` pod in the `open-cluster-management` namespace.

</div>

<div>

<div class="title">

Additional resources

</div>

- [ACM-23907](https://issues.redhat.com/browse/ACM-23907)

</div>

<a id="sub-app-incorrect-warning"></a>

#### Subscription application displays incorrect warning message

When you deploy the Subscription application (Deprecated), it displays a warning message for the Subscription node in the *Application Topology* page. If you check the Subscription node details, it incorrectly shows the `local-cluster` is offline.

<div>

<div class="title">

Procedure

</div>

- Check the real status of the `local-cluster` by clicking **Infrastructure** \> **Clusters** from the Console navigation.

</div>

<div>

<div class="title">

Additional resources

</div>

- [ACM-18544](https://issues.redhat.com/browse/ACM-18544)

</div>

<a id="app-table-menu"></a>

#### The console menu of the Application table can be difficult to click

When Application resources get updated in the hub cluster, the Application page table also gets updated. If you have the menu of the Application table opened, then it gets closed with every update to the Application page table. Because the menu can close often, it can be difficult for you to click the menu.

<div>

<div class="title">

Procedure

</div>

- Click the Application name to go to the Application details page where you can click the same action menu without it closing with every update.

</div>

<div>

<div class="title">

Additional resources

</div>

- [ACM-18543](https://issues.redhat.com/browse/ACM-18543)

</div>

<a id="topology-displays-invalid-expression"></a>

#### Application topology displays invalid expression

When you use the `Exist` or `DoesNotExist` operators in the `Placement` resource, the application topology node details display the expressions as `\#invalidExpr`. This display is wrong, and the expression is still valid and works in the `Placement` resource.

<div>

<div class="title">

Procedure

</div>

- Edit the expression inside the `Placement` resource YAML.

</div>

<div>

<div class="title">

Additional resources

</div>

- [ACM-15077](https://issues.redhat.com/browse/ACM-15077)

</div>

<a id="edit-sub-placement-rule"></a>

#### Editing *PlacementRule* subscriptions does not display YAML in editor

After you create a subscription application that references a `PlacementRule` resource, the subscription YAML does not display in the YAML editor in the console.

<div>

<div class="title">

Procedure

</div>

- Edit your subscription YAML file in your terminal.

</div>

<div>

<div class="title">

Additional resources

</div>

- [ACM-8889](https://issues.redhat.com/browse/ACM-8889)

</div>

<a id="helm-secret-dependencies"></a>

#### Helm Chart with secret dependencies cannot be deployed by subscription

Using Helm Chart, you can define privacy data in a Kubernetes secret and refer to this secret within the `value.yaml` file of the Helm Chart.

The username and password are given by the referred Kubernetes secret resource `dbsecret`. For example, see the following sample `value.yaml` file:

``` yaml
credentials:
  secretName: dbsecret
  usernameSecretKey: username
  passwordSecretKey: password
```

The Helm Chart with secret dependencies is only supported in the Helm binary CLI. It is not supported in the operator SDK Helm library. The Red Hat Advanced Cluster Management subscription controller applies the operator SDK Helm library to install and upgrade the Helm Chart. Therefore, the Red Hat Advanced Cluster Management subscription cannot deploy the Helm Chart with secret dependencies.

<div>

<div class="title">

Additional resources

</div>

- [ACM-8727](https://issues.redhat.com/browse/ACM-8727)

</div>

<a id="argo-pull-topology"></a>

#### Topology does not display correctly for Argo CD pull model `ApplicationSet`

When you use the Argo CD pull model to deploy `ApplicationSet` applications and the application resource names are customized, the resource names might appear different for each cluster. When this happens, the topology does not display your application correctly.

<div>

<div class="title">

Additional resources

</div>

- [ACM-6954](https://issues.redhat.com/browse/ACM-6954)

</div>

<a id="argo-pull-local-excluded"></a>

#### Local cluster is excluded as a managed cluster for pull model

The hub cluster application set deploys to target managed clusters, but the local cluster, which is a managed hub cluster, is excluded as a target managed cluster.

As a result, if the Argo CD application is propagated to the local cluster by the Argo CD pull model, the local cluster Argo CD application is not cleaned up, even though the local cluster is removed from the placement decision of the Argo CD `ApplicationSet` resource.

Additionally, if you manually refresh the pull model Argo CD application in the **Applications** section of the Argo CD console, the refresh is not processed and the **REFRESH** button in the Argo CD console is disabled.

<div>

<div class="title">

Procedure

</div>

1.  Remove the `skip-reconcile` annotation from the local cluster Argo CD application. See the following annotation:

    ``` yaml
    annotations:
        argocd.argoproj.io/skip-reconcile: "true"
    ```

2.  Remove the `refresh` annotation from the Argo CD application. See the following annotation:

    ``` yaml
    annotations:
        argocd.argoproj.io/refresh: normal
    ```

</div>

<div>

<div class="title">

Additional resources

</div>

- [ACM-7843](https://issues.redhat.com/browse/ACM-7843)

</div>

<a id="argo-pull-model-controller"></a>

#### Argo CD and propagation controllers might reconcile simultaneously

Both the Argo CD controller and the propagation controller might reconcile on the same application resource and cause the duplicate instances of application deployment on the managed clusters, but from the different deployment models.

For deploying applications by using the pull model, the Argo CD controllers ignore these application resources when the Argo CD `argocd.argoproj.io/skip-reconcile` annotation is added to the template section of the `ApplicationSet`.

The `argocd.argoproj.io/skip-reconcile` annotation is only available in the GitOps operator version 1.9.0, or later.

<div>

<div class="title">

Procedure

</div>

- Wait until the hub cluster and all the managed clusters are updated to GitOps operator version 1.9.0 before implementing the pull model.

</div>

<a id="argo-pull-model-resource"></a>

#### Resource fails to deploy

All the resources listed in the `MulticlusterApplicationSetReport` are actually deployed on the managed clusters. If a resource fails to deploy, the resource is not included in the resource list, but the cause is listed in the error message.

<a id="argo-pull-model-large"></a>

#### Resource allocation might take several minutes

For large environments with over 1000 managed clusters and Argo CD application sets that are deployed to hundreds of managed clusters, Argo CD application creation on the hub cluster might take several minutes.

<div>

<div class="title">

Procedure

</div>

- Set the `requeueAfterSeconds` to `zero` in the `clusterDecisionResource` generator of the application set, as it is displayed in the following example file:

  ``` yaml
  apiVersion: argoproj.io/v1alpha1
  kind: ApplicationSet
  metadata:
    name: cm-allclusters-app-set
    namespace: openshift-gitops
  spec:
    generators:
    - clusterDecisionResource:
        configMapRef: ocm-placement-generator
        labelSelector:
          matchLabels:
            cluster.open-cluster-management.io/placement: app-placement
        requeueAfterSeconds: 0
  ```

</div>

<a id="object-bucket-sub-admin"></a>

#### Application ObjectBucket channel type cannot use allow and deny lists

You cannot specify allow and deny lists with ObjectBucket channel type in the `subscription-admin` role. In other channel types, the allow and deny lists in the subscription indicates which Kubernetes resources can be deployed, and which Kubernetes resources should not be deployed.

<div>

<div class="title">

Additional resources

</div>

- [GH-22763](https://github.com/stolostron/backlog/issues/22763)

</div>

<a id="changes-not-automatic"></a>

#### Changes to the multicluster_operators_subscription image do not take effect automatically

The `application-manager` add-on that is running on the managed clusters is now handled by the subscription operator, when it was previously handled by the klusterlet operator. The subscription operator is not managed the `multicluster-hub`, so changes to the `multicluster_operators_subscription` image in the `multicluster-hub` image manifest config map do not take effect automatically.

If the image that is used by the subscription operator is overrided by changing the `multicluster_operators_subscription` image in the `multicluster-hub` image manifest config map, the `application-manager` add-on on the managed clusters does not use the new image until the subscription operator pod is restarted.

<a id="policy-needs-sub-admin"></a>

#### Policy resource not deployed unless by subscription administrator

The `policy.open-cluster-management.io/v1` resources are no longer deployed by an application subscription by default for Red Hat Advanced Cluster Management version 2.4. `policy.open-cluster-management.io/v1` resources that were deployed by existing application subscriptions in previous Red Hat Advanced Cluster Management versions remain, but are no longer reconciled with the source repository unless the application subscriptions are deployed by a subscription administrator.

<div>

<div class="title">

Procedure

</div>

- Deploy the application subscription as a subscription administrator. See [Create an allow and deny list as subscription administrator](applications.md#creating-allow-deny-list) for information.

</div>

<div>

<div class="title">

Additional resources

</div>

- [ACM-893](https://issues.redhat.com/browse/ACM-893)

</div>

<a id="app-ansible-standalone"></a>

#### Application Ansible hook stand-alone mode

Ansible hook stand-alone mode is not supported. To deploy Ansible hook on the hub cluster with a subscription, you might use the following subscription YAML:

``` yaml
apiVersion: apps.open-cluster-management.io/v1
kind: Subscription
metadata:
  name: sub-rhacm-gitops-demo
  namespace: hello-openshift
  annotations:
    apps.open-cluster-management.io/github-path: myapp
    apps.open-cluster-management.io/github-branch: master
spec:
  hooksecretref:
      name: toweraccess
  channel: rhacm-gitops-demo/ch-rhacm-gitops-demo
  placement:
     local: true
```

However, this configuration might never create the Ansible instance, since the `spec.placement.local:true` has the subscription running on `standalone` mode. You need to create the subscription in hub mode.

<div>

<div class="title">

Procedure

</div>

1.  Create a placement rule that deploys to `local-cluster`. See the following sample where `local-cluster: "true"` refers to your hub cluster:

    ``` yaml
    apiVersion: apps.open-cluster-management.io/v1
    kind: PlacementRule
    metadata:
      name: <towhichcluster>
      namespace: hello-openshift
    spec:
      clusterSelector:
        matchLabels:
          local-cluster: "true"
    ```

2.  Reference that placement rule in your subscription. See the following sample:

    ``` yaml
    apiVersion: apps.open-cluster-management.io/v1
    kind: Subscription
    metadata:
      name: sub-rhacm-gitops-demo
      namespace: hello-openshift
      annotations:
        apps.open-cluster-management.io/github-path: myapp
        apps.open-cluster-management.io/github-branch: master
    spec:
      hooksecretref:
          name: toweraccess
      channel: rhacm-gitops-demo/ch-rhacm-gitops-demo
      placement:
         placementRef:
            name: <towhichcluster>
            kind: PlacementRule
    ```

    After applying both, you should see the Ansible instance created in your hub cluster.

</div>

<div>

<div class="title">

Additional resources

</div>

- [GH-8036](https://github.com/stolostron/backlog/issues/8036)

</div>

<a id="app-placement-not-deployed"></a>

#### Application not deployed after an updated placement rule

If applications are not deploying after an update to a placement rule, verify that the `application-manager` pod is running. The `application-manager` is the subscription container that needs to run on managed clusters.

<div>

<div class="title">

Procedure

</div>

1.  Run the following command to verify that the `application-manager` is running:

    ``` bash
    oc get pods -n open-cluster-management-agent-addon |grep application-manager
    ```

2.  Search for `kind:pod cluster:yourcluster` in the console and see if the `application-manager` is running.

3.  If you cannot verify, attempt to import the cluster again and verify again.

</div>

<a id="sub-operator-does-not-create-an-scc"></a>

#### Subscription operator does not create an SCC

Learn about Red Hat OpenShift Container Platform SCC at [Managing security context constraints](https://docs.redhat.com/en/documentation/openshift_container_platform/4.20/html-single/authentication_and_authorization/index#managing-pod-security-policies), which is an additional configuration required on the managed cluster.

Different deployments have different security context and different service accounts. The subscription operator cannot create an SCC CR automatically.. Administrators control permissions for pods. A Security Context Constraints (SCC) CR is required to enable appropriate permissions for the relative service accounts to create pods in the non-default namespace. To manually create an SCC CR in your namespace, complete the following steps:

<div>

<div class="title">

Procedure

</div>

1.  Find the service account that is defined in the deployments. For example, see the following `nginx` deployments:

        nginx-ingress-52edb
        nginx-ingress-52edb-backend

2.  Create an SCC CR in your namespace to assign the required permissions to the service account or accounts. See the following example, where `kind: SecurityContextConstraints` is added:

    ``` yaml
    apiVersion: security.openshift.io/v1
     defaultAddCapabilities:
     kind: SecurityContextConstraints
     metadata:
       name: ingress-nginx
       namespace: ns-sub-1
     priority: null
     readOnlyRootFilesystem: false
     requiredDropCapabilities:
     fsGroup:
       type: RunAsAny
     runAsUser:
       type: RunAsAny
     seLinuxContext:
       type: RunAsAny
     users:
     - system:serviceaccount:my-operator:nginx-ingress-52edb
     - system:serviceaccount:my-operator:nginx-ingress-52edb-backend
    ```

</div>

<div>

<div class="title">

Additional resources

</div>

- [GH-24248](https://github.com/stolostron/backlog/issues/24248)

</div>

<a id="app-channel-namespaces"></a>

#### Application channels require unique namespaces

Creating more than one channel in the same namespace can cause errors with the hub cluster.

For instance, namespace `charts-v1` is used by the installer as a Helm type channel, so do not create any additional channels in `charts-v1`.

<div>

<div class="title">

Procedure

</div>

- Create your channel in a unique namespace. All channels need an individual namespace, except GitHub channels, which can share a namespace with another GitHub channel.

</div>

<a id="ansible-automation-platform-fail"></a>

#### Ansible Automation Platform job fail

Ansible jobs fail to run when you select an incompatible option. Ansible Automation Platform only works when the `-cluster-scoped` channel options are chosen. This affects all components that need to perform Ansible jobs.

<div>

<div class="title">

Additional resources

</div>

- [GH-14469](https://github.com/stolostron/backlog/issues/14469)

</div>

<a id="ansible-automation-operator-access"></a>

#### Ansible Automation Platform operator access Ansible Automation Platform outside of a proxy

The Red Hat Ansible Automation Platform operator cannot access Ansible Automation Platform outside of a proxy-enabled OpenShift Container Platform cluster.

<div>

<div class="title">

Procedure

</div>

- Install the Ansible Automation Platform within the proxy. See install steps that are provided by Ansible Automation Platform.

</div>

<div>

<div class="title">

Additional resources

</div>

- [GH-16821](https://github.com/stolostron/backlog/issues/16821)

</div>

<a id="app-name"></a>

#### Application name requirements

An application name cannot exceed 37 characters. The application deployment displays the following error if the characters exceed this amount.

``` yaml
status:
  phase: PropagationFailed
  reason: 'Deployable.apps.open-cluster-management.io "_long_lengthy_name_" is invalid: metadata.labels: Invalid value: "_long_lengthy_name_": must be no more than 63 characters/n'
```

<div>

<div class="title">

Additional resources

</div>

- [GH-14310](https://github.com/stolostron/backlog/issues/14310)

</div>

<a id="app-tables"></a>

#### Application console table limitations

See the following limitations to various *Application* tables in the console:

- From the *Applications* table on the *Overview* page and the *Subscriptions* table on the *Advanced configuration* page, the *Clusters* column displays a count of clusters where application resources are deployed. Since applications are defined by resources on the local cluster, the local cluster is included in the search results, whether actual application resources are deployed on the local cluster or not.

- From the *Advanced configuration* table for *Subscriptions*, the *Applications* column displays the total number of applications that use that subscription, but if the subscription deploys child applications, those are included in the search result, as well.

- From the *Advanced configuration* table for *Channels*, the *Subscriptions* column displays the total number of subscriptions on the local cluster that use that channel, but this does not include subscriptions that are deployed by other subscriptions, which are included in the search result.

<div>

<div class="title">

Additional resources

</div>

- [GH-12410](https://github.com/stolostron/backlog/issues/12410)

</div>

<a id="app-topology"></a>

#### No Application console topology filtering

The *Console* and *Topology* for *Application* changes for the 2.17. There is no filtering capability from the console Topology page.

<div>

<div class="title">

Additional resources

</div>

- [GH-20831](https://github.com/stolostron/backlog/issues/20831)

</div>

<a id="cluster-permission-fails"></a>

#### *ClusterPermission* resource fails when creating many role bindings

If you create a `ClusterPermission` resource that contains many role bindings within the same namespace and do not set the optional `name` field, it fails. This error occurs because the same name is used for the role bindings in the namespace.

<div>

<div class="title">

Procedure

</div>

- Set the optional `name` field for each role binding with a unique name.

</div>

<div>

<div class="title">

Additional resources

</div>

- [ACM-21342](https://issues.redhat.com/browse/ACM-21342)

</div>

<a id="known-issues-observability"></a>

### Observability known issues

Review the known issues for Red Hat Advanced Cluster Management for Kubernetes. The following list contains known issues for this release, or known issues that continued from the previous release.

For your Red Hat OpenShift Container Platform cluster, see [OpenShift Container Platform known issues](https://docs.redhat.com/en/documentation/openshift_container_platform/4.20/html/release_notes#ocp-4-15-known-issues).

For more about deprecations and removals, see [Deprecations and removals for Red Hat Advanced Cluster Management](release_notes.md#deprecations-removals-acm).

- [Manually configured alert forwarding fails](release_notes.md#alert-forward-fails)

- [Retention change causes data loss](release_notes.md#retention-change)

- [Observatorium API gateway pods have stale tenant data after hub restore](release_notes.md#obs-stale-tenant)

- [No permission to add *PrometheusRules* and *ServiceMonitors* in *openshift-monitoring* namespace](release_notes.md#permission-to-add-denied)

- [Lack of support for proxy settings](release_notes.md#lack-of-support-for-proxy-settings)

- [Grafana downsampled data mismatch](release_notes.md#grafana-downsampled-mismatch)

- [Limitations for custom managed cluster Observatorium API or Alertmanager URLs](release_notes.md#limits-custom-obs-urls)

<a id="alert-forward-fails"></a>

#### Manually configured alert forwarding fails

When you update to Red Hat Advanced Cluster Management 2.16 and later, alert forwarding fails if you disabled automatic configuration by setting `mco-disable-alerting: true` in the `MultiClusterObservability` custom resource, and if you manually configured alert forwarding.

Alert forwarding fails after you update because the name of the `observability-alertmanager-accessor` and `hub-alertmanager-router-ca` secrets were changed to include a postfix of the hub cluster ID.

The hub cluster ID is obtained from the `uuid` field in the metadata of the `ClusterVersion` custom resource on the hub cluster. The ID, with dashes removed and trimmed to the first 19 characters, is appended to the `alertmanager` secrets.

<div>

<div class="title">

Procedure

</div>

1.  Update your alert forwarding configuration that you manually configured to use the new names of the secrets.

2.  Update the secret name in the `cluster-monitoring-config` config map in the `openshift-monitoring` namespace for platform alerts. Update the secret name in the `user-workload-monitoring-config` config map in the `openshift-user-workload-monitoring` namespace for user workload alerts. Find the new secret names in the `openshift-monitoring` and `openshift-user-workload-monitoring` namespaces.

</div>

<div>

<div class="title">

Additional resources

</div>

- [ACM-26604](https://issues.redhat.com/browse/ACM-26604)

</div>

<a id="retention-change"></a>

#### Retention change causes data loss

The default retention for all resolution levels, such as `retentionResolutionRaw`, `retentionResolution5m`, or `retentionResolution1h`, is 365 days (`365d`). This `365d` default retention means that the default retention for a 1 hour resolution has decreased from indefinite, `0d` to `365d`. This retention change might cause you to lose data. If you did not set an explicit value for the resolution retention in your `MultiClusterObservability` `spec.advanced.retentionConfig` parameter, you might lose data. For more information, see [Observability advanced configuration](observability.md#adv-config-obs).

<div>

<div class="title">

Additional resources

</div>

- [ACM-11048](https://issues.redhat.com/browse/ACM-11048)

</div>

<a id="obs-stale-tenant"></a>

#### Observatorium API gateway pods have stale tenant data after hub restore

The Observatorium API gateway pods in a restored hub cluster might contain stale tenant data after a backup and restore procedure because of a Kubernetes limitation. See [Mounted config maps are updated automatically](https://kubernetes.io/docs/tasks/configure-pod-container/configure-pod-configmap/#mounted-configmaps-are-updated-automatically) for more about the limitation.

As a result, the Observatorium API and Thanos gateway rejects metrics from collectors, and the Red Hat Advanced Cluster Management Grafana dashboards do not display data.

See the following errors from the Observatorium API gateway pod logs:

``` bash
level=error name=observatorium caller=logchannel.go:129 msg="failed to forward metrics" returncode="500 Internal Server Error" response="no matching hashring to handle tenant\n"
```

Thanos receives pods logs with the following errors:

``` bash
caller=handler.go:551 level=error component=receive component=receive-handler tenant=xxxx err="no matching hashring to handle tenant" msg="internal server error"
```

See the following procedure to restart all Observatorium API gateway pods with the correct tenant information, and the data from collectors start displaying in Grafana in between 5-10 minutes:

<div>

<div class="title">

Procedure

</div>

1.  Scale down the `observability-observatorium-api` deployment instances from `N` to `0`.

2.  Scale up the `observability-observatorium-api` deployment instances from `0` to `N`.

    **Note:** `N` = `2` by default, but might be greater than `2` in some custom configuration environments.

</div>

<div>

<div class="title">

Additional resources

</div>

- [ACM-9681](https://issues.redhat.com/browse/ACM-9681)

</div>

<a id="permission-to-add-denied"></a>

#### No permission to add *PrometheusRules* and *ServiceMonitors* in *openshift-monitoring* namespace

When Red Hat Advanced Cluster Management is deployed or an installation is updated, the Red Hat Advanced Cluster Management observability `ServiceMonitors` and `PrometheusRule` resources are no longer present in the `openshift-monitoring` namespace.

<div>

<div class="title">

Procedure

</div>

- Use a label in your defined Red Hat Advanced Cluster Management hub cluster namespace. The label, `openshift.io/cluster-monitoring: "true"` causes the Cluster Monitoring Operator to scrape the namespace for metrics.

</div>

<div>

<div class="title">

Additional resources

</div>

- [ACM-8499](https://issues.redhat.com/browse/ACM-8499)

</div>

<a id="lack-of-support-for-proxy-settings"></a>

#### Lack of support for proxy settings

The Prometheus `AdditionalAlertManagerConfig` resource of the observability add-on does not support proxy settings. You must disable the observability alert forwarding feature. Complete the following steps to disable alert forwarding:

<div>

<div class="title">

Procedure

</div>

1.  Go to the `MultiClusterObservability` resource.

2.  Update the `mco-disabling-alerting` parameter value to `true`

    The HTTPS proxy with a self-signed CA certificate is not supported.

</div>

<div>

<div class="title">

Additional resources

</div>

- [ACM-7118](https://issues.redhat.com/browse/ACM-7118)

</div>

<a id="grafana-downsampled-mismatch"></a>

#### Grafana downsampled data mismatch

When you attempt to query historical data and there is a discrepancy between the calculated step value and downsampled data, the result is empty. For example, if the calculated step value is `5m` and the downsampled data is in a one-hour interval, data does not appear from Grafana.

This discrepancy occurs because a URL query parameter must be passed through the Thanos Query front-end data source. Afterwards, the URL query can perform additional queries for other downsampling levels when data is missing. You must manually update the Thanos Query front-end data source configuration.

<div>

<div class="title">

Procedure

</div>

1.  Go to the Query front-end data source.

2.  To update your query parameters, click the *Misc* section.

3.  From the *Custom query parameters* field, select **`max_source_resolution=auto`**.

4.  To verify that the data is displayed, refresh your Grafana page.

    Your query data appears from the Grafana dashboard.

</div>

<div>

<div class="title">

Additional resources

</div>

- [ACM-3748](https://issues.redhat.com/browse/ACM-3748)

</div>

<a id="limits-custom-obs-urls"></a>

#### Limitations for custom managed cluster Observatorium API or Alertmanager URLs

Custom Observatorium API and Alertmanager URLs only support intermediate components with TLS passthrough.

<div>

<div class="title">

Procedure

</div>

- Use separate sub-domains if both custom URLs are pointing to the same intermediate component because OpenShift Container Platform routers do not support two separate route objects with the same host.

</div>

<div>

<div class="title">

Additional resources

</div>

- [ACM-11407](https://issues.redhat.com/browse/ACM-11407)

</div>

<a id="known-issues-governance"></a>

### Governance known issues

Review the known issues for Governance. The following list contains known issues for this release, or known issues that continued from the previous release.

For your Red Hat OpenShift Container Platform cluster, see [OpenShift Container Platform known issues](https://docs.redhat.com/en/documentation/openshift_container_platform/4.20/html/release_notes/#ocp-4-15-known-issues).

For more about deprecations and removals, see [Deprecations and removals for Red Hat Advanced Cluster Management](release_notes.md#deprecations-removals-acm).

- [Configuration policy listed compliant when namespace is stuck in *Terminating* state](release_notes.md#config-policy-stuck)

- [*ConfigurationPolicy* stuck in terminating](release_notes.md#configurationpolicy-crd-terminating)

- [Policy status shows repeated updates when enforced](release_notes.md#policy-status-repeated-updates)

- [Kyverno policies no longer report a status for the latest version](release_notes.md#kyverno-no-status)

<a id="config-policy-stuck"></a>

#### Configuration policy listed compliant when namespace is stuck in *Terminating* state

When you have a configuration policy that is configured with `mustnothave` for the `complianceType` parameter and `enforce` for the `remediationAction` parameter, the policy is listed as compliant when a deletion request is made to the Kubernetes API. Therefore, the Kubernetes object can be stuck in a `Terminating` state while the policy is listed as compliant.

<div>

<div class="title">

Additional resources

</div>

- [GH-20715](https://github.com/stolostron/backlog/issues/20715)

</div>

<a id="configurationpolicy-crd-terminating"></a>

#### *ConfigurationPolicy* stuck in terminating

When you remove the `config-policy-controller` add-on from a managed cluster by disabling the policy controller in the `KlusterletAddonConfig` or by detaching the cluster, the `ConfigurationPolicy` custom resource definition might get stuck in a terminating state. If the `ConfigurationPolicy` custom resource definition is stuck in a terminating state, new policies might not be added to the cluster if the add-on is reinstalled later. You can also receive the following error:

    template-error; Failed to create policy template: create not allowed while custom resource definition is terminating

<div>

<div class="title">

Procedure

</div>

1.  Use the following command to check if the custom resource definition is stuck:

    ``` bash
    oc get crd configurationpolicies.policy.open-cluster-management.io -o=jsonpath='{.metadata.deletionTimestamp}'
    ```

2.  If a deletion timestamp is on the resource, the custom resource definition is stuck. To resolve the issue, remove all finalizers from configuration policies that remain on the cluster. Use the following command on the managed cluster and replace `<cluster-namespace>` with the managed cluster namespace:

    ``` bash
    oc get configurationpolicy -n <cluster-namespace> -o name | xargs oc patch -n <cluster-namespace> --type=merge -p '{"metadata":{"finalizers": []}}'
    ```

    The configuration policy resources are automatically removed from the cluster and the custom resource definition exits its terminating state. If the add-on has already been reinstalled, the custom resource definition is recreated automatically without a deletion timestamp.

</div>

<div>

<div class="title">

Additional resources

</div>

- [GH-25139](https://github.com/stolostron/backlog/issues/25139)

</div>

<a id="policy-status-repeated-updates"></a>

#### Policy status shows repeated updates when enforced

If a policy is set to `remediationAction: enforce` and is repeatedly updated, the Red Hat Advanced Cluster Management console shows repeated violations with successful updates. Repeated updates produce multiple policy events, which can cause the `governance-policy-framework-addon` pod to run out of memory and crash.

<div>

<div class="title">

Procedure

</div>

1.  Disable the policy and compare the differences between `objectDefinition` in the policy and the object on the managed cluster if another controller or process is also updating the object with different values.

    If the values are different, another controller or process might be updating them. Check the `metadata` of the object to help identify why the values are different.

2.  Disable the policy and compare the differences between `objectDefinition` in the policy and the object on the managed cluster if the `objectDefinition` in the `ConfigurationPolicy` does not match because of Kubernetes processing the object when the policy is applied.

    If the keys are different or missing, Kubernetes might have processed the keys before applying them to the object, such as removing keys containing default or empty values.

</div>

<div>

<div class="title">

Additional resources

</div>

- [ACM-3109](https://issues.redhat.com/browse/ACM-3109)

</div>

<a id="kyverno-no-status"></a>

#### Kyverno policies no longer report a status for the latest version

Kyverno policies generated by the Policy Generator report the following message in your Red Hat Advanced Cluster Management cluster:

    violation - couldn't find mapping resource with kind ClusterPolicyReport, please check if you have CRD deployed;
    violation - couldn't find mapping resource with kind PolicyReport, please check if you have CRD deployed

The cause is that the `PolicyReport` API version is incorrect in the generator and does not match what Kyverno has deployed.

<div>

<div class="title">

Additional resources

</div>

- [ACM-12743](https://issues.redhat.com/browse/ACM-12743)

</div>

<a id="known-issues_submariner"></a>

### Networking known issues

Review the known issues for Submariner. The following list contains known issues for this release, or known issues that continued from the previous release.

For your Red Hat OpenShift Container Platform cluster, see [OpenShift Container Platform known issues](https://docs.redhat.com/en/documentation/openshift_container_platform/4.20/html/release_notes/#ocp-4-15-known-issues).

For more about deprecations and removals, see [Deprecations and removals for Red Hat Advanced Cluster Management](release_notes.md#deprecations-removals-acm).

- [Submariner installation on IBM Power Systems fails](release_notes.md#ocp-acm-submariner-fails)

- [Source IP not retained for applications on OpenShift Container Platform with OVN-Kubernetes](release_notes.md#source-ip-ocp-ovnk)

- [Without *ClusterManagementAddon* submariner add-on fails](release_notes.md#cluster-management-addon-needed)

- [Submariner add-on resources not cleaned up properly when managed clusters are imported](release_notes.md#submariner-addon-resources)

- [Submariner install plan limitation](release_notes.md#subm-install-plan)

- [Limited headless services support](release_notes.md#headless-services-globalnet)

- [Deployments that use VXLAN when NAT is enabled are not supported](release_notes.md#submariner-vxlan)

- [Self-signed certificates might prevent connection to broker](release_notes.md#certificates-prevent-connection-broker)

- [Submariner only supports OpenShift SDN or OVN Kubernetes](release_notes.md#submariner-sdn-cni)

- [Command limitation on Microsoft Azure clusters](release_notes.md#submariner-diagnose-azure)

- [Automatic update not working with custom *CatalogSource* or *Subscription*](release_notes.md#submariner-update-limit)

- [Uninstall Submariner before removing *ManagedCluster* from a *ManageClusterSet*](release_notes.md#submariner-uninstall-before-move)

<a id="ocp-acm-submariner-fails"></a>

#### Submariner installation on IBM Power Systems fails

If you are using Red Hat Advanced Cluster Management 2.15, you cannot install Submariner on IBM systems, as it is currently not supported for these versions.

<div>

<div class="title">

Additional resources

</div>

- [ACM-27270](https://issues.redhat.com/browse/ACM-27270)

</div>

<a id="source-ip-ocp-ovnk"></a>

#### Source IP not retained for applications on OpenShift Container Platform with OVN-Kubernetes

If you are using OpenShift Container Platform versions between 4.18 and versions earlier than 4.19.5 with OVN-Kubernetes for Submariner, the source IP is not retained when packets reach the destination pod. As a result, applications that rely on the source IP, such as `NetworkPolicy`, might not work correctly.

<div>

<div class="title">

Additional resources

</div>

- [ACM-18680](https://issues.redhat.com/browse/ACM-18680)

</div>

<a id="cluster-management-addon-needed"></a>

#### Without *ClusterManagementAddon* submariner add-on fails

For versions 2.8 and earlier, when you install Red Hat Advanced Cluster Management, you also deploy the `submariner-addon` component with the Operator Lifecycle Manager. If you did not create a `MultiClusterHub` custom resource, the `submariner-addon` pod sends an error and prevents the operator from installing.

The following notification occurs because the `ClusterManagementAddon` custom resource definition is missing:

    graceful termination failed, controllers failed with error: the server could not find the requested resource (post clustermanagementaddons.addon.open-cluster-management.io)

The `ClusterManagementAddon` resource is created by the `cluster-manager` deployment, however, this deployment becomes available when the `MultiClusterEngine` components are installed on the cluster.

If there is not a `MultiClusterEngine` resource that is already available on the cluster when the `MultiClusterHub` custom resource is created, the `MultiClusterHub` operator deploys the `MultiClusterEngine` instance and the operator that is required, which resolves the previous error.

<div>

<div class="title">

Additional resources

</div>

- [GH-24159](https://github.com/stolostron/backlog/issues/24159)

</div>

<a id="submariner-addon-resources"></a>

#### Submariner add-on resources not cleaned up properly when managed clusters are imported

If the `submariner-addon` component is set to `false` within `MultiClusterHub` (MCH) operator, then the `submariner-addon` finalizers are not cleaned up properly for the managed cluster resources. Since the finalizers are not cleaned up properly, this prevents the `submariner-addon` component from being disabled within the hub cluster.

<div>

<div class="title">

Additional resources

</div>

- [ACM-8549](https://issues.redhat.com/browse/ACM-8549)

</div>

<a id="subm-install-plan"></a>

#### Submariner install plan limitation

The Submariner install plan does not follow the overall install plan settings. Therefore, the operator management screen cannot control the Submariner install plan. By default, Submariner install plans are applied automatically, and the Submariner add-on is always updated to the latest available version corresponding to the installed Red Hat Advanced Cluster Management version.

<div>

<div class="title">

Procedure

</div>

- Use a customized Submariner subscription.

</div>

<div>

<div class="title">

Additional resources

</div>

- [ACM-8260](https://issues.redhat.com/browse/ACM-8260)

</div>

<a id="headless-services-globalnet"></a>

#### Limited headless services support

Service discovery is not supported for headless services without selectors when using Globalnet.

<div>

<div class="title">

Additional resources

</div>

- [GH-24159](https://github.com/stolostron/backlog/issues/24159)

</div>

<a id="submariner-vxlan"></a>

#### Deployments that use VXLAN when NAT is enabled are not supported

Only non-NAT deployments support Submariner deployments with the VXLAN cable driver.

<div>

<div class="title">

Additional resources

</div>

- [GH-24258](https://github.com/stolostron/backlog/issues/24258)

</div>

<a id="certificates-prevent-connection-broker"></a>

#### Self-signed certificates might prevent connection to broker

Self-signed certificates on the broker might prevent joined clusters from connecting to the broker. The connection fails with certificate validation errors.

<div>

<div class="title">

Procedure

</div>

- Disable broker certificate validation by setting `InsecureBrokerConnection` to `true` in the relevant `SubmarinerConfig` object. See the following example:

  ``` yaml
  apiVersion: submarineraddon.open-cluster-management.io/v1alpha1
  kind: SubmarinerConfig
  metadata:
     name: submariner
     namespace: <managed-cluster-namespace>
  spec:
     insecureBrokerConnection: true
  ```

</div>

<div>

<div class="title">

Additional resources

</div>

- [GH-27008](https://github.com/stolostron/backlog/issues/27008)

</div>

<a id="submariner-sdn-cni"></a>

#### Submariner only supports OpenShift SDN or OVN Kubernetes

Submariner only supports Red Hat OpenShift Container Platform clusters that use the OpenShift SDN or the OVN-Kubernetes Container Network Interface (CNI) network provider.

<div>

<div class="title">

Additional resources

</div>

- [ACM-5306](https://issues.redhat.com/browse/ACM-5306)

</div>

<a id="submariner-diagnose-azure"></a>

#### Command limitation on Microsoft Azure clusters

The `subctl diagnose firewall inter-cluster` command does not work on Microsoft Azure clusters.

<div>

<div class="title">

Additional resources

</div>

- [ACM-5327](https://issues.redhat.com/browse/ACM-5327)

</div>

<a id="submariner-update-limit"></a>

#### Automatic update not working with custom *CatalogSource* or *Subscription*

Submariner is automatically updated when Red Hat Advanced Cluster Management for Kubernetes is updated. The automatic update might fail if you are using a custom `CatalogSource` or `Subscription`.

<div>

<div class="title">

Procedure

</div>

- Set the `spec.subscriptionConfig.channel` field to `stable-0.15` in the `SubmarinerConfig` custom resource for each managed cluster.

</div>

<div>

<div class="title">

Additional resources

</div>

- [ACM-6068](https://issues.redhat.com/browse/ACM-6068)

</div>

<a id="submariner-uninstall-before-move"></a>

#### Uninstall Submariner before removing *ManagedCluster* from a *ManageClusterSet*

If you remove a cluster from a `ClusterSet`, or move a cluster to a different `ClusterSet`, the Submariner installation is no longer valid.

<div>

<div class="title">

Procedure

</div>

- Uninstall Submariner before moving or removing a `ManagedCluster` from a `ManageClusterSet`. If you don’t uninstall Submariner, you cannot uninstall or reinstall Submariner anymore and Submariner stops working on your `ManagedCluster`.

</div>

<div>

<div class="title">

Additional resources

</div>

- [ACM-8847](https://issues.redhat.com/browse/ACM-8847)

</div>

<a id="known-issues-global-hub"></a>

### Multicluster global hub Operator known issues

Review the known issues for the multicluster global hub Operator. The following list contains known issues for this release, or known issues that continued from the previous release. For your OpenShift Container Platform cluster, see [OpenShift Container Platform known issues](https://docs.redhat.com/en/documentation/openshift_container_platform/4.20/html/release_notes/ocp-4-20-release-notes#rn-ocp-release-notes-known-issues_release-notes).

- [The *ManagedClusterMigration* resources error](release_notes.md#migration-resources-error)

- [Detached managed hub cluster deletes and recreates namespace and resources](release_notes.md#detached-managed-hub-cluster)

- [Kafka operator keeps restarting](release_notes.md#kafka-operator-keeps-restarting)

- [The standard group filter cannot pass to the new page](release_notes.md#no-new-page-group-filter)

<a id="migration-resources-error"></a>

#### The *ManagedClusterMigration* resources error

When you upgrade multicluster global hub and there are some `ManagedClusterMigration` resources in the multicluster global hub cluster, you might get the following error:

``` bash
error validating existing CRs against new CRD''s schema for "managedclustermigrations.global-hub.open-cluster-management.io":
      error validating global-hub.open-cluster-management.io/v1alpha1, Kind=ManagedClusterMigration
      "multicluster-global-hub/xxx": updated validation is
      too restrictive: [].spec.from: Required value'
```

<div>

<div class="title">

Procedure

</div>

- Delete all the `ManagedClusterMigration` resources before you upgrade multicluster global hub. Run the following command:

  ``` bash
  oc delete mcm --all
  ```

</div>

<div>

<div class="title">

Additional resources

</div>

- [ACM-25679](https://issues.redhat.com/browse/ACM-25679)

</div>

<a id="detached-managed-hub-cluster"></a>

#### Detached managed hub cluster deletes and recreates namespace and resources

If you import a managed hub cluster in the hosted mode and detach this managed hub cluster, then it deletes and recreates the `open-cluster-management-agent-addon` namespace. The detached managed hub cluster also deletes and recreates all the related `addon` resources within this namespace.

There is currently no workaround for this issue.

<div>

<div class="title">

Additional resources

</div>

- [ACM-15014](https://issues.redhat.com/browse/ACM-15014)

</div>

<a id="kafka-operator-keeps-restarting"></a>

#### Kafka operator keeps restarting

In the Federal Information Processing Standard (FIPS) environment, the Kafka operator keeps restarting because of the out-of-memory (OOM) state.

<div>

<div class="title">

Procedure

</div>

- Set the resource limit to at least `512M`. For detailed steps on how to set this limit, see [Deploying and Managing AMQ Streams on OpenShift](https://docs.redhat.com/en/documentation/red_hat_streams_for_apache_kafka/2.6/html/deploying_and_managing_amq_streams_on_openshift/index).

</div>

<div>

<div class="title">

Additional resources

</div>

- [ACM-12592](https://issues.redhat.com/browse/ACM-12592)

</div>

<a id="no-new-page-group-filter"></a>

#### The standard group filter cannot pass to the new page

In the *Global Hub Policy Group Compliancy Overview* hub dashboards, you can check one data point by clicking **View Offending Policies for standard group**, but after you click this link to go to the offending page, the standard group filter cannot pass to the new page.

This is also an issue for the **Cluster Group Compliancy Overview**.

<div>

<div class="title">

Additional resources

</div>

- [ACM-7461](https://issues.redhat.com/browse/ACM-7461)

</div>

<a id="deprecations-removals-acm"></a>

## Deprecations and removals for Red Hat Advanced Cluster Management

Learn when parts of the product are deprecated or removed from Red Hat Advanced Cluster Management for Kubernetes. Consider the alternative actions in the *Recommended action* and details, which display in the tables for the current release and for two prior releases. **Best practice:** Update to the most recent version.

**Deprecated:** Red Hat Advanced Cluster Management 2.10 and earlier versions are no longer supported. The documentation might remain available, but without any errata releases for fixed issues or other updates.

**Important:** Cluster lifecycle components and features are within the multicluster engine operator, which is a software operator that enhances cluster fleet management. Release notes for multicluster engine operator-specific features are found in at [Release notes for the multicluster engine operator](mce_release_notes.md#mce-release-notes-intro).

Deprecated items  
Components, features, or services are supported, but no longer recommended for use and might become obsolete in future releases. Consider the alternative actions in the *Recommended action* and details that are provided in the table.

Removed items  
Function that was deprecated in previous releases and is no longer available in the product. You must use alternatives for the removed function. Consider the alternative actions in the *Recommended action* and details that are provided in the following table:

| Product or category | Affected item | Version | Recommended action | More details and links |
|----|----|----|----|----|
| Application management | Subscription | 2.13 | Use Red Hat Advanced Cluster Management with OpenShift GitOps instead. | The deprecation is extended for five releases before removal. See [GitOps overview](gitops.md#gitops-overview) for updated function. |
| Applications and Governance | `PlacementRule` | 2.8 | Use `Placement` anywhere that you might use `PlacementRule`. | While `PlacementRule` is still available, it is not supported and the console displays `Placement` by default. |
| multicluster global hub | PostgreSQL manual update process | Red Hat Advanced Cluster Management 2.14 | None | Automatic database updates are supported for multicluster global hub version 1.5 and later. |

Table list of *deprecated* items for Red Hat Advanced Cluster Management

| Product or category | Affected item | Version | Recommended action | More details and links |
|----|----|----|----|----|
| {rhem} with Red Hat Advanced Cluster Management | `edge-manager-preview` component in the `MultiClusterHub` resource and integrated documentation | 2.15 | See [Red Hat Edge Manager 1.0](https://docs.redhat.com/en/documentation/red_hat_edge_manager) | See [Red Hat Edge Manager 1.0](https://docs.redhat.com/en/documentation/red_hat_edge_manager) |
| Backup and restore | The `backup-restore-auto-import` policy | 2.16 | Use the `backup-restore-enabled` policy instead. | The `backup-restore-auto-import` policy templates are merged into the existing `backup-restore-enabled` policy. The `hub-backup-policy-set.yaml` file is updated to reference only the `backup-restore-enabled` policy. |
| Console | **Infrastructure** \> **Virtual machines** console page | 2.15 | On Red Hat OpenShift Container Platform version 4.20, install Red Hat OpenShift Virtualization 4.20 to work with virtual machines across your fleet from the Fleet Virtualization perspective. Alternatively, use Search to find and take actions on virtual machines. | None |
| multicluster global hub | You are not required to migrate the resources, config maps and `Secrets` when you migrate managed clusters. | 2.15 | Migrate the managed clusters. | See [Migrating managed clusters with multicluster global hub](global_hub.md#global-hub-migrate). |
| Search service | Enabling virtual machine actions (Technology Preview) | 2.14 | Use fine-grained role-base access control instead. | See [Role-based access control](secure_clusters.md#rbac-rhacm). |
| Red Hat Advanced Cluster Management for Kubernetes console | Importing OpenShift Container Platform 3.11 clusters from the console | 2.14 | Update to a supported version of OpenShift Container Platform. See the [OpenShift Container Platform documentation](https://docs.redhat.com/en/documentation/openshift_container_platform/4.17). | The support for the deprecated custom resource definition `v1beta1` APIs is removed. The `v1beta1` APIs were only needed for OpenShift Container Platform 3.11. |

Table list of *removed* items for Red Hat Advanced Cluster Management

<a id="acm-gdpr"></a>

## Red Hat Advanced Cluster Management platform considerations for GDPR readiness

This document is intended to help you in your preparations for General Data Protection Regulation (GDPR) readiness. It provides information about features of the Red Hat Advanced Cluster Management for Kubernetes platform that you can configure, and aspects of the product’s use, that you should consider to help your organization with GDPR readiness.

- Notice

  - This information is not an exhaustive list, due to the many ways that clients can choose and configure features, and the large variety of ways that the product can be used in itself and with third-party clusters and systems.

  - Clients are responsible for ensuring their own compliance with various laws and regulations, including the European Union General Data Protection Regulation.

  - Clients are solely responsible for obtaining advice of competent legal counsel as to the identification and interpretation of any relevant laws and regulations that may affect the clients' business and any actions the clients may need to take to comply with such laws and regulations.

  - The products, services, and other capabilities described herein are not suitable for all client situations and may have restricted availability. Red Hat does not provide legal, accounting, or auditing advice or represent or warrant that its services or products will ensure that clients are in compliance with any law or regulation.\*

    GDPR  
    General Data Protection Regulation (GDPR) has been adopted by the European Union (EU) and applies from May 25, 2018. Why is GDPR important? GDPR establishes a stronger data protection regulatory framework for processing personal data of individuals. GDPR brings the following changes to data protection:

- New and enhanced rights for individuals

- Widened definition of personal data

- New obligations for processors

- Potential for significant financial penalties for non-compliance

- Compulsory data breach notification

- [Complete guide to GDPR compliance](https://gdpr.eu/)

- [Red Hat GDPR website](https://www.redhat.com/en/gdpr)

- Data Life Cycle

  The following sections describe aspects of data management within the Red Hat Advanced Cluster Management for Kubernetes platform and provide information on capabilities to help clients with GDPR requirements.

  - Red Hat Advanced Cluster Management for Kubernetes is an application platform for developing and managing on-premises, containerized applications. It is an integrated environment for managing containers that includes the container orchestrator Kubernetes, cluster lifecycle, application lifecycle, and security frameworks (governance, risk, and compliance).

  - As such, the Red Hat Advanced Cluster Management for Kubernetes platform deals primarily with technical data that is related to the configuration and management of the platform, some of which might be subject to GDPR. The Red Hat Advanced Cluster Management for Kubernetes platform also deals with information about users who manage the platform. This data will be described throughout this document for the awareness of clients responsible for meeting GDPR requirements.

  - This data is persisted on the platform on local or remote file systems as configuration files or in databases. Applications that are developed to run on the Red Hat Advanced Cluster Management for Kubernetes platform might deal with other forms of personal data subject to GDPR. The mechanisms that are used to protect and manage platform data are also available to applications that run on the platform. Additional mechanisms might be required to manage and protect personal data that is collected by applications run on the Red Hat Advanced Cluster Management for Kubernetes platform.

  - To best understand the Red Hat Advanced Cluster Management for Kubernetes platform and its data flows, you must understand how Kubernetes, Docker, and the Operator work. These open source components are fundamental to the Red Hat Advanced Cluster Management for Kubernetes platform. You use Kubernetes deployments to place instances of applications, which are built into Operators that reference Docker images. The Operator contain the details about your application, and the Docker images contain all the software packages that your applications need to run.

    What types of data flow through Red Hat Advanced Cluster Management for Kubernetes platform?

    As a platform, Red Hat Advanced Cluster Management for Kubernetes deals with several categories of technical data that could be considered as personal data, such as an administrator user ID and password, service user IDs and passwords, IP addresses, and Kubernetes node names. The Red Hat Advanced Cluster Management for Kubernetes platform also deals with information about users who manage the platform. Applications that run on the platform might introduce other categories of personal data unknown to the platform.

    Information on how this technical data is collected/created, stored, accessed, secured, logged, and deleted is described in later sections of this document.

- Personal data used for online contact

  Customers can submit online comments, feedback, and requests for information about in a variety of ways, primarily:

  - The public Slack community if there is a Slack channel

  - The public comments or tickets on the product documentation

  - The public conversations in a technical community

    Typically, only the client name and email address are used, to enable personal replies for the subject of the contact, and the use of personal data conforms to the [Red Hat Online Privacy Statement](https://www.redhat.com/en/about/privacy-policy).

- Data Collection

  The Red Hat Advanced Cluster Management for Kubernetes platform does not collect sensitive personal data. It does create and manage technical data, such as an administrator user ID and password, service user IDs and passwords, IP addresses, and Kubernetes node names, which might be considered personal data. The Red Hat Advanced Cluster Management for Kubernetes platform also deals with information about users who manage the platform. All such information is only accessible by the system administrator through a management console with role-based access control or by the system administrator though login to a Red Hat Advanced Cluster Management for Kubernetes platform node.

  Applications that run on the Red Hat Advanced Cluster Management for Kubernetes platform might collect personal data.

  When you assess the use of the Red Hat Advanced Cluster Management for Kubernetes platform running containerized applications and your need to meet the requirements of GDPR, you must consider the types of personal data that are collected by the application and aspects of how that data is managed, such as:

- How is the data protected as it flows to and from the application? Is the data encrypted in transit?

- How is the data stored by the application? Is the data encrypted at rest?

- How are credentials that are used to access the application collected and stored?

- How are credentials that are used by the application to access data sources collected and stored?

- How is data collected by the application removed as needed?

  This is not a definitive list of the types of data that are collected by the Red Hat Advanced Cluster Management for Kubernetes platform. It is provided as an example for consideration. If you have any questions about the types of data, contact Red Hat.

- Data storage

  The Red Hat Advanced Cluster Management for Kubernetes platform persists technical data that is related to configuration and management of the platform in stateful stores on local or remote file systems as configuration files or in databases. Consideration must be given to securing all data at rest. The Red Hat Advanced Cluster Management for Kubernetes platform supports encryption of data at rest in stateful stores that use `dm-crypt`.

  The following items highlight the areas where data is stored, which you might want to consider for GDPR.

  Platform Configuration Data  
  The Red Hat Advanced Cluster Management for Kubernetes platform configuration can be customized by updating a configuration YAML file with properties for general settings, Kubernetes, logs, network, Docker, and other settings. This data is used as input to the Red Hat Advanced Cluster Management for Kubernetes platform installer for deploying one or more nodes. The properties also include an administrator user ID and password that are used for bootstrap.

  Kubernetes Configuration Data  
  Kubernetes cluster state data is stored in a distributed key-value store, `etcd`.

  User Authentication Data, including User IDs and passwords  
  User ID and password management are handled through a client enterprise LDAP directory. Users and groups that are defined in LDAP can be added to Red Hat Advanced Cluster Management for Kubernetes platform teams and assigned access roles. Red Hat Advanced Cluster Management for Kubernetes platform stores the email address and user ID from LDAP, but does not store the password. Red Hat Advanced Cluster Management for Kubernetes platform stores the group name and upon login, caches the available groups to which a user belongs. Group membership is not persisted in any long-term way. Securing user and group data at rest in the enterprise LDAP must be considered. Red Hat Advanced Cluster Management for Kubernetes platform also includes an authentication service, Open ID Connect (OIDC) that interacts with the enterprise directory and maintains access tokens. This service uses ETCD as a backing store.

  Service authentication data, including user IDs and passwords  
  Credentials that are used by Red Hat Advanced Cluster Management for Kubernetes platform components for inter-component access are defined as Kubernetes Secrets. All Kubernetes resource definitions are persisted in the `etcd` key-value data store. Initial credentials values are defined in the platform configuration data as Kubernetes Secret configuration YAML files. For more information, see [Secrets](https://kubernetes.io/docs/concepts/configuration/secret/) in the Kubernetes documentation.

- Data access

  Red Hat Advanced Cluster Management for Kubernetes platform data can be accessed through the following defined set of product interfaces.

  - Web user interface (the console)

  - Kubernetes `kubectl` CLI

  - Red Hat Advanced Cluster Management for Kubernetes CLI

  - oc CLI

  These interfaces are designed to allow you to make administrative changes to your Red Hat Advanced Cluster Management for Kubernetes cluster. Administration access to Red Hat Advanced Cluster Management for Kubernetes can be secured and involves three logical, ordered stages when a request is made: authentication, role-mapping, and authorization.

- Authentication

  The Red Hat Advanced Cluster Management for Kubernetes platform authentication manager accepts user credentials from the console and forwards the credentials to the backend OIDC provider, which validates the user credentials against the enterprise directory. The OIDC provider then returns an authentication cookie (`auth-cookie`) with the content of a JSON Web Token (`JWT`) to the authentication manager. The JWT token persists information such as the user ID and email address, in addition to group membership at the time of the authentication request. This authentication cookie is then sent back to the console. The cookie is refreshed during the session. It is valid for 12 hours after you sign out of the console or close your web browser.

  For all subsequent authentication requests made from the console, the front-end NGINX server decodes the available authentication cookie in the request and validates the request by calling the authentication manager.

  The Red Hat Advanced Cluster Management for Kubernetes platform CLI requires the user to provide credentials to log in.

  The `kubectl` and `oc` CLI also requires credentials to access the cluster. These credentials can be obtained from the management console and expire after 12 hours. Access through service accounts is supported.

- Role Mapping

  Red Hat Advanced Cluster Management for Kubernetes platform supports role-based access control (RBAC). In the role mapping stage, the user name that is provided in the authentication stage is mapped to a user or group role. The roles are used when authorizing which administrative activities can be carried out by the authenticated user.

- Authorization

  Red Hat Advanced Cluster Management for Kubernetes platform roles control access to cluster configuration actions, to catalog and Helm resources, and to Kubernetes resources. Several IAM (Identity and Access Management) roles are provided, including Cluster Administrator, Administrator, Operator, Editor, Viewer. A role is assigned to users or user groups when you add them to a team. Team access to resources can be controlled by namespace.

- Pod Security

  Pod security policies are used to set up cluster-level control over what a pod can do or what it can access.

- Data Processing

  Users of Red Hat Advanced Cluster Management for Kubernetes can control the way that technical data that is related to configuration and management is processed and secured through system configuration.

  **Role-based access control** (RBAC) controls what data and functions can be accessed by users.

  **Data-in-transit** is protected by using `TLS`. `HTTPS` (`TLS` underlying) is used for secure data transfer between user client and back end services. Users can specify the root certificate to use during installation.

  **Data-at-rest** protection is supported by using `dm-crypt` to encrypt data.

  These same platform mechanisms that are used to manage and secure Red Hat Advanced Cluster Management for Kubernetes platform technical data can be used to manage and secure personal data for user-developed or user-provided applications. Clients can develop their own capabilities to implement further controls.

- Data Deletion

  Red Hat Advanced Cluster Management for Kubernetes platform provides commands, application programming interfaces (APIs), and user interface actions to delete data that is created or collected by the product. These functions enable users to delete technical data, such as service user IDs and passwords, IP addresses, Kubernetes node names, or any other platform configuration data, as well as information about users who manage the platform.

  Areas of Red Hat Advanced Cluster Management for Kubernetes platform to consider for support of data deletion:

  - All technical data that is related to platform configuration can be deleted through the management console or the Kubernetes `kubectl` API.

    Areas of Red Hat Advanced Cluster Management for Kubernetes platform to consider for support of account data deletion:

  - All technical data that is related to platform configuration can be deleted through the Red Hat Advanced Cluster Management for Kubernetes or the Kubernetes `kubectl` API.

    Function to remove user ID and password data that is managed through an enterprise LDAP directory would be provided by the LDAP product used with Red Hat Advanced Cluster Management for Kubernetes platform.

  - Capability for Restricting Use of Personal Data

    Using the facilities summarized in this document, Red Hat Advanced Cluster Management for Kubernetes platform enables an end user to restrict usage of any technical data within the platform that is considered personal data.

    Under GDPR, users have rights to access, modify, and restrict processing. Refer to other sections of this document to control the following:

- Right to access

  - Red Hat Advanced Cluster Management for Kubernetes platform administrators can use Red Hat Advanced Cluster Management for Kubernetes platform features to provide individuals access to their data.

  - Red Hat Advanced Cluster Management for Kubernetes platform administrators can use Red Hat Advanced Cluster Management for Kubernetes platform features to provide individuals information about what data Red Hat Advanced Cluster Management for Kubernetes platform holds about the individual.

- Right to modify

  - Red Hat Advanced Cluster Management for Kubernetes platform administrators can use Red Hat Advanced Cluster Management for Kubernetes platform features to allow an individual to modify or correct their data.

  - Red Hat Advanced Cluster Management for Kubernetes platform administrators can use Red Hat Advanced Cluster Management for Kubernetes platform features to correct an individual’s data for them.

- Right to restrict processing

  - Red Hat Advanced Cluster Management for Kubernetes platform administrators can use Red Hat Advanced Cluster Management for Kubernetes platform features to stop processing an individual’s data.

- Appendix

  As a platform, Red Hat Advanced Cluster Management for Kubernetes deals with several categories of technical data that could be considered as personal data, such as an administrator user ID and password, service user IDs and passwords, IP addresses, and Kubernetes node names. Red Hat Advanced Cluster Management for Kubernetes platform also deals with information about users who manage the platform. Applications that run on the platform might introduce other categories of personal data that are unknown to the platform.

  This appendix includes details on data that is logged by the platform services.

<a id="fips-readiness"></a>

## FIPS readiness

Red Hat Advanced Cluster Management for Kubernetes is designed for Federal Information Processing Standards (FIPS). When running on Red Hat OpenShift Container Platform in FIPS mode, OpenShift Container Platform uses the Red Hat Enterprise Linux cryptographic libraries submitted to NIST for FIPS Validation on only the architectures that are supported by OpenShift Container Platform.

For more information about the NIST validation program, see [Cryptographic Module Validation Program](https://csrc.nist.gov/Projects/cryptographic-module-validation-program/validated-modules).

For the latest NIST status for the individual versions of the RHEL cryptographic libraries submitted for validation, see [FIPS - Federal Information Processing Standards](https://access.redhat.com/compliance/fips).

If you plan to manage clusters with FIPS enabled, you must install Red Hat Advanced Cluster Management on an OpenShift Container Platform cluster that is configured to operate in FIPS mode. The hub cluster must be in FIPS mode because cryptography that is created on the hub cluster is used on managed clusters.

To enable FIPS mode on your managed clusters, set `fips: true` when you provision your OpenShift Container Platform managed cluster. You cannot enable FIPS after you provision your cluster.

For more information, see [Do you need extra security for your cluster?](https://docs.redhat.com/en/documentation/openshift_container_platform/4.20/html/installation_overview/installing-preparing#installing-preparing-security) in the OpenShift Container Platform documentation.

Persistent Volume Claim (PVC) and S3 storage that is used by the search and observability components must be encrypted when you configure the provided storage. Red Hat Advanced Cluster Management does not provide storage encryption, see the OpenShift Container Platform documentation, [Configuring persistent storage](https://docs.redhat.com/en/documentation/openshift_container_platform/4.20/html-single/storage/index#configuring-persistent-storage).

When you provision managed clusters using the Red Hat Advanced Cluster Management console, select the following checkbox in the *Cluster details* section of the managed cluster creation to enable the FIPS standards:

    FIPS with information text: Use the Federal Information Processing Standards (FIPS) modules provided with Red Hat Enterprise Linux CoreOS instead of the default Kubernetes cryptography suite file before you deploy the new managed cluster.
