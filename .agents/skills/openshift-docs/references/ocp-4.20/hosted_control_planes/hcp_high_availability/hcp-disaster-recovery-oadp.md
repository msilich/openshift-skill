<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

By using the OpenShift API for Data Protection (OADP) Operator for disaster recovery, you can restore hosted cluster namespaces from object storage instead of manually rebuilding every cluster. In addition, you back up etcd as part of the control plane backup, and you can back up hosted clusters independently.

You can use the OADP Operator to perform disaster recovery for hosted control planes on Amazon Web Services (AWS) and bare metal.

The disaster recovery process with OpenShift API for Data Protection (OADP) involves the following steps:

1.  Preparing your platform, such as Amazon Web Services or bare metal, to use OADP

2.  Backing up the data plane workload

3.  Backing up the control plane workload

4.  Restoring a hosted cluster by using OADP

# Preparing AWS to use OADP for disaster recovery

Before you can perform disaster recovery for hosted control planes on Amazon Web Services (AWS), you need to meet a few prerequisites and configure OpenShift API for Data Protection (OADP) on AWS S3 compatible storage.

<div>

<div class="title">

Prerequisites

</div>

- You installed the OADP Operator on the management cluster. For more information, see "About installing OADP".

- You created a storage class for the management cluster.

- You have access to the management cluster with `cluster-admin` privileges.

- You have access to the OADP subscription through a catalog source.

- You have access to a cloud storage provider that is compatible with OADP, such as S3, Microsoft Azure, Google Cloud, or MinIO.

- In a disconnected environment, you have access to a self-hosted storage provider that is compatible with OADP, such as [Red Hat OpenShift Data Foundation](https://docs.redhat.com/en/documentation/red_hat_openshift_data_foundation/) or [MinIO](https://min.io/).

- Your hosted control planes pods are up and running.

- You are using a supported version of OADP for your management cluster. For example, if your management cluster is on OpenShift Container Platform 4.20, you must use OADP version 1.5. For more information, see "Support for OpenShift API for Data Protection (OADP)".

</div>

<div>

<div class="title">

Procedure

</div>

- To prepare AWS to use OADP, follow the steps in "Configuring the OpenShift API for Data Protection with AWS S3 compatible storage".

  After you create the `DataProtectionApplication` object, new `velero` deployment and `node-agent` pods are created in the `openshift-adp` namespace.

</div>

<div>

<div class="title">

Next steps

</div>

- Back up the data plane workload and the control plane workload.

</div>

<div>

<div class="title">

Additional resources

</div>

- [About installing OADP](../../backup_and_restore/application_backup_and_restore/installing/about-installing-oadp.md#about-installing-oadp)

- [Support for OpenShift API for Data Protection (OADP)](../../backup_and_restore/application_backup_and_restore/oadp-intro.md#oadp-operator-supported_oadp-api)

- [Configuring the OpenShift API for Data Protection with AWS S3 compatible storage](../../backup_and_restore/application_backup_and_restore/installing/installing-oadp-mcg.md#installing-oadp-mcg)

</div>

# Preparing bare metal to use OADP for disaster recovery

Before you can perform disaster recovery for hosted control planes on bare metal, you need to meet a few prerequisites and configure the OpenShift API for Data Protection (OADP) with Multicloud Object Gateway.

<div>

<div class="title">

Prerequisites

</div>

- You installed the OADP Operator on the management cluster. For more information, see "About installing OADP".

- You created a storage class for the management cluster.

- You have access to the management cluster with `cluster-admin` privileges.

- You have access to the OADP subscription through a catalog source.

- You have access to a cloud storage provider that is compatible with OADP, such as S3, Microsoft Azure, Google Cloud, or MinIO.

- In a disconnected environment, you have access to a self-hosted storage provider that is compatible with OADP, such as [Red Hat OpenShift Data Foundation](https://docs.redhat.com/en/documentation/red_hat_openshift_data_foundation/) or [MinIO](https://min.io/).

- Your hosted control planes pods are up and running.

- You are using a supported version of OADP for your management cluster. For example, if your management cluster is on OpenShift Container Platform 4.20, you must use OADP version 1.5. For more information, see "Support for OpenShift API for Data Protection (OADP)".

</div>

<div>

<div class="title">

Procedure

</div>

- To prepare bare metal to use OADP, complete the steps in "Configuring the OpenShift API for Data Protection with Multicloud Object Gateway".

  After you create the `DataProtectionApplication` object, new `velero` deployment and `node-agent` pods are created in the `openshift-adp` namespace.

</div>

<div>

<div class="title">

Next steps

</div>

- Back up the data plane workload and the control plane workload.

</div>

<div>

<div class="title">

Additional resources

</div>

- [About installing OADP](../../backup_and_restore/application_backup_and_restore/installing/about-installing-oadp.md#about-installing-oadp)

- [Support for OpenShift API for Data Protection (OADP)](../../backup_and_restore/application_backup_and_restore/oadp-intro.md#oadp-operator-supported_oadp-api)

- [Configuring the OpenShift API for Data Protection with Multicloud Object Gateway](../../backup_and_restore/application_backup_and_restore/installing/installing-oadp-aws.md#installing-oadp-aws)

</div>

# Data plane workload backup

As part of the process to back up and restore by using the OADP Operator, you can back up the data plane workload.

If the data plane workload is not important, you can skip this procedure.

To back up the data plane workload by using the OADP Operator, see "Backing up applications". After you complete those steps, you can restore your hosted cluster by using OADP.

<div>

<div class="title">

Additional resources

</div>

- [Backing up applications](../../backup_and_restore/application_backup_and_restore/backing_up_and_restoring/backing-up-applications.md#backing-up-applications)

</div>

# Control plane workload backup

You can back up the control plane workload by creating the `Backup` custom resource (CR).

The steps vary depending on whether your platform is AWS or bare metal.

## Backing up the control plane workload on AWS

You can back up the control plane workload by creating the `Backup` custom resource (CR).

For information about monitoring the backup process, see "Observing the backup and restore process".

<div>

<div class="title">

Procedure

</div>

1.  Pause the reconciliation of the `HostedCluster` resource by running the following command:

    ``` terminal
    $ oc --kubeconfig <management_cluster_kubeconfig_file> \
      patch hostedcluster -n <hosted_cluster_namespace> <hosted_cluster_name> \
      --type json -p '[{"op": "add", "path": "/spec/pausedUntil", "value": "true"}]'
    ```

2.  Get the infrastructure ID of your hosted cluster by running the following command:

    ``` terminal
    $ oc get hostedcluster -n local-cluster <hosted_cluster_name> -o=jsonpath="{.spec.infraID}"
    ```

    Note the infrastructure ID to use in the next step.

3.  Pause the reconciliation of the `cluster.cluster.x-k8s.io` resource by running the following command:

    ``` terminal
    $ oc --kubeconfig <management_cluster_kubeconfig_file> \
      patch cluster.cluster.x-k8s.io \
      -n local-cluster-<hosted_cluster_name> <hosted_cluster_infra_id> \
      --type json -p '[{"op": "add", "path": "/spec/paused", "value": true}]'
    ```

4.  Pause the reconciliation of the `NodePool` resource by running the following command:

    ``` terminal
    $ oc --kubeconfig <management_cluster_kubeconfig_file> \
      patch nodepool -n <hosted_cluster_namespace> <node_pool_name> \
      --type json -p '[{"op": "add", "path": "/spec/pausedUntil", "value": "true"}]'
    ```

5.  Pause the reconciliation of the `AgentCluster` resource by running the following command:

    ``` terminal
    $ oc --kubeconfig <management_cluster_kubeconfig_file> \
      annotate agentcluster -n <hosted_control_plane_namespace>  \
      cluster.x-k8s.io/paused=true --all'
    ```

6.  Pause the reconciliation of the `AgentMachine` resource by running the following command:

    ``` terminal
    $ oc --kubeconfig <management_cluster_kubeconfig_file> \
      annotate agentmachine -n <hosted_control_plane_namespace>  \
      cluster.x-k8s.io/paused=true --all'
    ```

7.  Annotate the `HostedCluster` resource to prevent the deletion of the hosted control plane namespace by running the following command:

    ``` terminal
    $ oc --kubeconfig <management_cluster_kubeconfig_file> \
      annotate hostedcluster -n <hosted_cluster_namespace> <hosted_cluster_name> \
      hypershift.openshift.io/skip-delete-hosted-controlplane-namespace=true
    ```

8.  Create a YAML file that defines the `Backup` CR:

    <div class="formalpara">

    <div class="title">

    Example `backup-control-plane.yaml` file

    </div>

    ``` yaml
    apiVersion: velero.io/v1
    kind: Backup
    metadata:
      name: <backup_resource_name>
      namespace: openshift-adp
      labels:
        velero.io/storage-location: default
    spec:
      hooks: {}
      includedNamespaces:
      - <hosted_cluster_namespace>
      - <hosted_control_plane_namespace>
      includedResources:
      - sa
      - role
      - rolebinding
      - pod
      - pvc
      - pv
      - bmh
      - configmap
      - infraenv
      - priorityclasses
      - pdb
      - agents
      - hostedcluster
      - nodepool
      - secrets
      - hostedcontrolplane
      - cluster
      - agentcluster
      - agentmachinetemplate
      - agentmachine
      - machinedeployment
      - machineset
      - machine
      excludedResources: []
      storageLocation: default
      ttl: 2h0m0s
      snapshotMoveData: true
      datamover: "velero"
      defaultVolumesToFsBackup: true
    ```

    </div>

    - `metadata.name` specifies the name of your `Backup` resource.

    - `spec.includedNamespaces` includes specific namespaces to back up objects from them. You must replace `<hosted_cluster_namespace>` with the name of the hosted cluster namespace and replace `<hosted_control_plane_namespace>` with the name of the hosted control plane namespace.

    - `spec.includedResources` includes the `infraenv` resource. You must create the `infraenv` resource in a separate namespace. Do not delete the `infraenv` resource during the backup process.

    - `spec.snapshotMoveData` and `spec.datamover` enable the CSI volume snapshots and upload the control plane workload automatically to the cloud storage.

    - `spec.defaultVolumesToFsBackup` sets the `fs-backup` backing up method for persistent volumes (PVs) as default. This setting is useful when you use a combination of Container Storage Interface (CSI) volume snapshots and the `fs-backup` method.

      > [!NOTE]
      > If you want to use CSI volume snapshots, you must add the `backup.velero.io/backup-volumes-excludes=<pv_name>` annotation to your PVs.

9.  Apply the `Backup` CR by running the following command:

    ``` terminal
    $ oc apply -f backup-control-plane.yaml
    ```

</div>

<div>

<div class="title">

Verification

</div>

- Verify if the value of the `status.phase` is `Completed` by running the following command:

  ``` terminal
  $ oc get backups.velero.io <backup_resource_name> -n openshift-adp \
    -o jsonpath='{.status.phase}'
  ```

</div>

<div>

<div class="title">

Next steps

</div>

- Restoring a hosted cluster by using OADP

</div>

## Backing up the control plane workload on a bare metal

You can back up the control plane workload by creating the `Backup` custom resource (CR).

For more information about monitoring the backup process, see "Observing the backup and restore process".

<div>

<div class="title">

Procedure

</div>

1.  Pause the reconciliation of the `HostedCluster` resource by running the following command:

    ``` terminal
    $ oc --kubeconfig <management_cluster_kubeconfig_file> \
      patch hostedcluster -n <hosted_cluster_namespace> <hosted_cluster_name> \
      --type json -p '[{"op": "add", "path": "/spec/pausedUntil", "value": "true"}]'
    ```

2.  Get the infrastructure ID of your hosted cluster by running the following command:

    ``` terminal
    $ oc --kubeconfig <management_cluster_kubeconfig_file> \
      get hostedcluster -n <hosted_cluster_namespace> \
      <hosted_cluster_name> -o=jsonpath="{.spec.infraID}"
    ```

3.  Note the infrastructure ID to use in the next step.

4.  Pause the reconciliation of the `cluster.cluster.x-k8s.io` resource by running the following command:

    ``` terminal
    $ oc --kubeconfig <management_cluster_kubeconfig_file> \
      annotate cluster -n <hosted_control_plane_namespace> \
      <hosted_cluster_infra_id> cluster.x-k8s.io/paused=true
    ```

5.  Pause the reconciliation of the `NodePool` resource by running the following command:

    ``` terminal
    $ oc --kubeconfig <management_cluster_kubeconfig_file> \
      patch nodepool -n <hosted_cluster_namespace> <node_pool_name> \
      --type json -p '[{"op": "add", "path": "/spec/pausedUntil", "value": "true"}]'
    ```

6.  Pause the reconciliation of the `AgentCluster` resource by running the following command:

    ``` terminal
    $ oc --kubeconfig <management_cluster_kubeconfig_file> \
      annotate agentcluster -n <hosted_control_plane_namespace>  \
      cluster.x-k8s.io/paused=true --all
    ```

7.  Pause the reconciliation of the `AgentMachine` resource by running the following command:

    ``` terminal
    $ oc --kubeconfig <management_cluster_kubeconfig_file> \
      annotate agentmachine -n <hosted_control_plane_namespace>  \
      cluster.x-k8s.io/paused=true --all
    ```

8.  If you are backing up and restoring to the same management cluster, annotate the `HostedCluster` resource to prevent the deletion of the hosted control plane namespace by running the following command:

    ``` terminal
    $ oc --kubeconfig <management_cluster_kubeconfig_file> \
      annotate hostedcluster -n <hosted_cluster_namespace> <hosted_cluster_name> \
      hypershift.openshift.io/skip-delete-hosted-controlplane-namespace=true
    ```

9.  Create a YAML file that defines the `Backup` CR:

    <div class="formalpara">

    <div class="title">

    Example `backup-control-plane.yaml` file

    </div>

    ``` yaml
    apiVersion: velero.io/v1
    kind: Backup
    metadata:
      name: <backup_resource_name>
      namespace: openshift-adp
      labels:
        velero.io/storage-location: default
    spec:
      hooks: {}
      includedNamespaces:
      - <hosted_cluster_namespace>
      - <hosted_control_plane_namespace>
      - <agent_namespace>
      includedResources:
      - sa
      - role
      - rolebinding
      - pod
      - pvc
      - pv
      - bmh
      - configmap
      - infraenv
      - priorityclasses
      - pdb
      - agents
      - hostedcluster
      - nodepool
      - secrets
      - services
      - deployments
      - hostedcontrolplane
      - cluster
      - agentcluster
      - agentmachinetemplate
      - agentmachine
      - machinedeployment
      - machineset
      - machine
      excludedResources: []
      storageLocation: default
      ttl: 2h0m0s
      snapshotMoveData: true
      datamover: "velero"
      defaultVolumesToFsBackup: true
    ```

    </div>

    - `metadata.name` specifies the name of your `Backup` resource.

    - `spec.includedNamespaces` specifies namespaces to back up objects from them. Replace `<hosted_cluster_namespace>` with the name of the hosted cluster namespace, replace `<hosted_control_plane_namespace>` with the name of the hosted control plane namespace, and replace `<agent_namespace>` with the namespace where your `Agent`, `BMH`, and `InfraEnv` CRs are located.

    - `spec.snapshotMoveData` enable the CSI volume snapshots and upload the control plane workload automatically to the cloud storage.

    - `spec.defaultVolumesToFsBackup` sets the `fs-backup` backing up method for persistent volumes (PVs) as default. This setting is useful when you use a combination of Container Storage Interface (CSI) volume snapshots and the `fs-backup` method.

      > [!NOTE]
      > If you want to use CSI volume snapshots, you must add the `backup.velero.io/backup-volumes-excludes=<pv_name>` annotation to your PVs.

10. Apply the `Backup` CR by running the following command:

    ``` terminal
    $ oc apply -f backup-control-plane.yaml
    ```

</div>

<div>

<div class="title">

Verification

</div>

- Verify if the value of the `status.phase` is `Completed` by running the following command:

  ``` terminal
  $ oc get backups.velero.io <backup_resource_name> -n openshift-adp \
    -o jsonpath='{.status.phase}'
  ```

</div>

<div>

<div class="title">

Next steps

</div>

- Restore a hosted cluster by using OADP.

</div>

# Hosted cluster restoration by using OADP

You can restore a hosted cluster into the same management cluster or into a new management cluster.

## Restoring a hosted cluster into the same management cluster by using OADP

You can restore the hosted cluster by creating the `Restore` custom resource (CR).

- If you are using an *in-place* update, the `InfraEnv` resource does not need spare nodes. You need to re-provision the worker nodes from the new management cluster.

- If you are using a *replace* update, you need some spare nodes for the `InfraEnv` resource to deploy the worker nodes.

> [!IMPORTANT]
> After you back up your hosted cluster, you must delete it to start the restoring process. To start node provisioning, you must back up workloads in the data plane before deleting the hosted cluster.

<div>

<div class="title">

Prerequisites

</div>

- You completed the steps in [Removing a cluster by using the console](https://docs.redhat.com/en/documentation/red_hat_advanced_cluster_management_for_kubernetes/2.15/html/clusters/cluster_mce_overview#remove-a-cluster-by-using-the-console) to delete your hosted cluster.

- You completed the steps in [Removing remaining resources after removing a cluster](https://docs.redhat.com/en/documentation/red_hat_advanced_cluster_management_for_kubernetes/2.15/html/clusters/cluster_mce_overview#removing-a-cluster-from-management-in-special-cases).

</div>

To monitor and observe the backup process, see "Observing the backup and restore process".

<div>

<div class="title">

Procedure

</div>

1.  Verify that no pods and persistent volume claims (PVCs) are present in the hosted control plane namespace by running the following command:

    ``` terminal
    $ oc get pod pvc -n <hosted_control_plane_namespace>
    ```

    <div class="formalpara">

    <div class="title">

    Expected output

    </div>

    ``` terminal
    No resources found
    ```

    </div>

2.  Create a YAML file that defines the `Restore` CR:

    <div class="formalpara">

    <div class="title">

    Example `restore-hosted-cluster.yaml` file

    </div>

    ``` yaml
    apiVersion: velero.io/v1
    kind: Restore
    metadata:
      name: <restore_resource_name>
      namespace: openshift-adp
    spec:
      backupName: <backup_resource_name>
      restorePVs: true
      existingResourcePolicy: update
      excludedResources:
      - nodes
      - events
      - events.events.k8s.io
      - backups.velero.io
      - restores.velero.io
      - resticrepositories.velero.io
    ```

    </div>

    - `metadata.name` specifies the name of your `Restore` resource.

    - `spec.backupName` specifies the name of your `Backup` resource.

    - `spec.restorePVs: true` starts the recovery of persistent volumes (PVs) and its pods.

    - `spec.existingResourcePolicy: update` ensures that the existing objects are overwritten with the backed up content.

      > [!IMPORTANT]
      > You must create the `infraenv` resource in a separate namespace. Do not delete the `infraenv` resource during the restore process. The `infraenv` resource is mandatory for the new nodes to be reprovisioned.

3.  Apply the `Restore` CR by running the following command:

    ``` terminal
    $ oc apply -f restore-hosted-cluster.yaml
    ```

4.  Verify if the value of the `status.phase` is `Completed` by running the following command:

    ``` terminal
    $ oc get hostedcluster <hosted_cluster_name> -n <hosted_cluster_namespace> \
      -o jsonpath='{.status.phase}'
    ```

5.  After the restore process is complete, start the reconciliation of the `HostedCluster` and `NodePool` resources that you paused during backing up of the control plane workload:

    1.  Start the reconciliation of the `HostedCluster` resource by running the following command:

        ``` terminal
        $ oc --kubeconfig <management_cluster_kubeconfig_file> \
          patch hostedcluster -n <hosted_cluster_namespace> <hosted_cluster_name> \
          --type json \
          -p '[{"op": "add", "path": "/spec/pausedUntil", "value": "false"}]'
        ```

    2.  Start the reconciliation of the `NodePool` resource by running the following command:

        ``` terminal
        $ oc --kubeconfig <management_cluster_kubeconfig_file> \
          patch nodepool -n <hosted_cluster_namespace> <node_pool_name> \
          --type json \
          -p '[{"op": "add", "path": "/spec/pausedUntil", "value": "false"}]'
        ```

6.  Start the reconciliation of the Agent provider resources that you paused during backing up of the control plane workload:

    1.  Start the reconciliation of the `AgentCluster` resource by running the following command:

        ``` terminal
        $ oc --kubeconfig <management_cluster_kubeconfig_file> \
          annotate agentcluster -n <hosted_control_plane_namespace>  \
          cluster.x-k8s.io/paused- --overwrite=true --all
        ```

    2.  Start the reconciliation of the `AgentMachine` resource by running the following command:

        ``` terminal
        $ oc --kubeconfig <management_cluster_kubeconfig_file> \
          annotate agentmachine -n <hosted_control_plane_namespace>  \
          cluster.x-k8s.io/paused- --overwrite=true --all
        ```

7.  Remove the `hypershift.openshift.io/skip-delete-hosted-controlplane-namespace-` annotation in the `HostedCluster` resource to avoid manually deleting the hosted control plane namespace by running the following command:

    ``` terminal
    $ oc --kubeconfig <management_cluster_kubeconfig_file> \
      annotate hostedcluster -n <hosted_cluster_namespace> <hosted_cluster_name> \
      hypershift.openshift.io/skip-delete-hosted-controlplane-namespace- \
      --overwrite=true --all
    ```

</div>

## Restoring a hosted cluster into a new management cluster by using OADP

You can restore the hosted cluster into a new management cluster by creating the `Restore` custom resource (CR).

- If you are using an in-place update, the `InfraEnv` resource does not need spare nodes. Instead, you need to re-provision the worker nodes from the new management cluster.

- If you are using a replace update, you need some spare nodes for the `InfraEnv` resource to deploy the worker nodes.

<div>

<div class="title">

Prerequisites

</div>

- You configured the new management cluster to use OpenShift API for Data Protection (OADP). The new management cluster must have the same Data Protection Application (DPA) as the management cluster that you backed up from so that the `Restore` CR can access the backup storage.

- You configured the networking settings of the new management cluster to resolve the DNS of the hosted cluster.

  - The DNS of the host must resolve to the IP of both the new management cluster and the hosted cluster.

  - The hosted cluster must resolve to the IP of the new management cluster.

</div>

To monitor and observe the backup process, see "Observing the backup and restore process".

> [!IMPORTANT]
> Complete the following steps on the new management cluster that you are restoring the hosted cluster to, not on the management cluster that you created the backup from.

<div>

<div class="title">

Procedure

</div>

1.  Create a YAML file that defines the `Restore` CR:

    <div class="formalpara">

    <div class="title">

    Example `restore-hosted-cluster.yaml` file

    </div>

    ``` yaml
    apiVersion: velero.io/v1
    kind: Restore
    metadata:
      name: <restore_resource_name>
      namespace: openshift-adp
    spec:
      includedNamespaces:
      - <hosted_cluster_namespace>
      - <hosted_control_plane_namespace>
      - <agent_namespace>
      backupName: <backup_resource_name>
      cleanupBeforeRestore: CleanupRestored
      veleroManagedClustersBackupName: <managed_cluster_name>
      veleroCredentialsBackupName: <credentials_backup_name>
      veleroResourcesBackupName: <resources_backup_name>
      restorePVs: true
      preserveNodePorts: true
      existingResourcePolicy: update
      excludedResources:
      - pod
      - nodes
      - events
      - events.events.k8s.io
      - backups.velero.io
      - restores.velero.io
      - resticrepositories.velero.io
      - pv
      - pvc
    ```

    </div>

    - `metadata.name` specifies the name of your `Restore` resource.

    - `spec.includedNamespaces` specifies namespaces to back up objects from them. Replace `<hosted_cluster_namespace>` with the name of the hosted cluster namespace, replace `<hosted_control_plane_namespace>` with the name of the hosted control plane namespace, and replace `<agent_namespace>` with the namespace where your `Agent`, `BMH`, and `InfraEnv` CRs are located.

    - `spec.backupName` specifies the name of your `Backup` resource.

    - `spec.veleroManagedClustersBackupName` can be omitted if you are not using Red Hat Advanced Cluster Management.

    - `spec.restorePVs: true` starts the recovery of persistent volumes (PVs) and its pods.

    - `spec.existingResourcePolicy: update` ensures that the existing objects are overwritten with the backed up content.

2.  Apply the `Restore` CR by running the following command:

    ``` terminal
    $ oc --kubeconfig <restore_management_kubeconfig> apply -f restore-hosted-cluster.yaml
    ```

3.  Verify that the value of the `status.phase` is `Completed` by running the following command:

    ``` terminal
    $ oc --kubeconfig <restore_management_kubeconfig> \
      get restore.velero.io <restore_resource_name> \
      -n openshift-adp -o jsonpath='{.status.phase}'
    ```

4.  Verify that all CRs are restored by running the following commands:

    ``` terminal
    $ oc --kubeconfig <restore_management_kubeconfig> get infraenv -n <agent_namespace>
    ```

    ``` terminal
    $ oc --kubeconfig <restore_management_kubeconfig> get agent -n <agent_namespace>
    ```

    ``` terminal
    $  oc --kubeconfig <restore_management_kubeconfig> get bmh -n <agent_namespace>
    ```

    ``` terminal
    $ oc --kubeconfig <restore_management_kubeconfig> get hostedcluster -n <hosted_cluster_namespace>
    ```

    ``` terminal
    $ oc --kubeconfig <restore_management_kubeconfig> get nodepool -n <hosted_cluster_namespace>
    ```

    ``` terminal
    $ oc --kubeconfig <restore_management_kubeconfig> get agentmachine -n <hosted_controlplane_namespace>
    ```

    ``` terminal
    $ oc --kubeconfig <restore_management_kubeconfig> get agentcluster -n <hosted_controlplane_namespace>
    ```

5.  If you plan to use the new management cluster as your main management cluster going forward, complete the following steps. Otherwise, if you plan to use the management cluster that you backed up from as your main management cluster, complete steps 5 - 8 in "Restoring a hosted cluster into the same management cluster by using OADP".

    1.  Remove the Cluster API deployment from the management cluster that you backed up from by running the following command:

        ``` terminal
        $ oc --kubeconfig <backup_management_kubeconfig> delete deploy cluster-api \
          -n <hosted_control_plane_namespace>
        ```

        Because only one Cluster API can access a cluster at a time, this step ensures that the Cluster API for the new management cluster functions correctly.

    2.  After the restore process is complete, start the reconciliation of the `HostedCluster` and `NodePool` resources that you paused during backing up of the control plane workload:

        1.  Start the reconciliation of the `HostedCluster` resource by running the following command:

            ``` terminal
            $ oc --kubeconfig <restore_management_kubeconfig> \
              patch hostedcluster -n <hosted_cluster_namespace> <hosted_cluster_name> \
              --type json \
              -p '[{"op": "replace", "path": "/spec/pausedUntil", "value": "false"}]'
            ```

        2.  Start the reconciliation of the `NodePool` resource by running the following command:

            ``` terminal
            $ oc --kubeconfig <restore_management_kubeconfig> \
              patch nodepool -n <hosted_cluster_namespace> <node_pool_name> \
              --type json \
              -p '[{"op": "replace", "path": "/spec/pausedUntil", "value": "false"}]'
            ```

        3.  Verify that the hosted cluster is reporting that the hosted control plane is available by running the following command:

            ``` terminal
            $ oc --kubeconfig <restore_management_kubeconfig> get hostedcluster
            ```

        4.  Verify that the hosted cluster is reporting that the cluster operators are available by running the following command:

            ``` terminal
            $ oc get co --kubeconfig <hosted_cluster_kubeconfig>
            ```

    3.  Start the reconciliation of the Agent provider resources that you paused during backing up of the control plane workload:

        1.  Start the reconciliation of the `AgentCluster` resource by running the following command:

            ``` terminal
            $ oc --kubeconfig <restore_management_kubeconfig> \
              annotate agentcluster -n <hosted_control_plane_namespace>  \
              cluster.x-k8s.io/paused- --overwrite=true --all
            ```

        2.  Start the reconciliation of the `AgentMachine` resource by running the following command:

            ``` terminal
            $ oc --kubeconfig <restore_management_kubeconfig> \
              annotate agentmachine -n <hosted_control_plane_namespace>  \
              cluster.x-k8s.io/paused- --overwrite=true --all
            ```

        3.  Start the reconciliation of the `Cluster` resource by running the following command:

            ``` terminal
            $ oc --kubeconfig <restore_management_kubeconfig> \
              annotate cluster -n <hosted_control_plane_namespace> \
              cluster.x-k8s.io/paused- --overwrite=true --all
            ```

    4.  Verify that the node pool is working as expected by running the following command:

        ``` terminal
        $ oc --kubeconfig <restore_management_kubeconfig> \
          get nodepool -n <hosted_cluster_namespace>
        ```

        <div class="formalpara">

        <div class="title">

        Example output

        </div>

        ``` terminal
        NAME       CLUSTER    DESIRED NODES   CURRENT NODES   AUTOSCALING   AUTOREPAIR   VERSION   UPDATINGVERSION   UPDATINGCONFIG   MESSAGE
        hosted-0   hosted-0   3               3               False         False        4.17.11   False             False
        ```

        </div>

    5.  Optional: To ensure that no conflicts exist and that the new management cluster has continued functionality, remove the `HostedCluster` resources from the backup management cluster by completing the following steps:

        1.  In the management cluster that you backed up from, in the `ClusterDeployment` resource, set the `spec.preserveOnDelete` parameter to `true` by running the following command:

            ``` terminal
            $ oc --kubeconfig <backup_management_kubeconfig> patch \
              -n <hosted_control_plane_namespace> \
              ClusterDeployment/<hosted_cluster_name> -p \
              '{"spec":{"preserveOnDelete":'true'}}' \
              --type=merge
            ```

            This step ensures that the hosts are not deprovisioned.

        2.  Delete the machines by running the following commands:

            ``` terminal
            $ oc --kubeconfig <backup_management_kubeconfig> patch \
              <machine_name> -n <hosted_control_plane_namespace> -p \
              '[{"op":"remove","path":"/metadata/finalizers"}]' \
              --type=merge
            ```

            ``` terminal
            $ oc --kubeconfig <backup_management_kubeconfig> \
              delete machine <machine_name> \
              -n <hosted_control_plane_namespace>
            ```

        3.  Delete the `AgentCluster` and `Cluster` resources by running the following commands:

            ``` terminal
            $ oc --kubeconfig <backup_management_kubeconfig> \
              delete agentcluster <hosted_cluster_name> \
              -n <hosted_control_plane_namespace>
            ```

            ``` terminal
            $ oc --kubeconfig <backup_management_kubeconfig> \
              patch cluster <cluster_name> \
              -n <hosted_control_plane_namespace> \
              -p '[{"op":"remove","path":"/metadata/finalizers"}]' \
              --type=json
            ```

            ``` terminal
            $ oc --kubeconfig <backup_management_kubeconfig> \
              delete cluster <cluster_name> \
              -n <hosted_control_plane_namespace>
            ```

        4.  If you use Red Hat Advanced Cluster Management, delete the managed cluster by running the following commands:

            ``` terminal
            $ oc --kubeconfig <backup_management_kubeconfig> \
              patch managedcluster <hosted_cluster_name> \
              -n <hosted_cluster_namespace> \
              -p '[{"op":"remove","path":"/metadata/finalizers"}]' \
              --type=json
            ```

            ``` terminal
            $ oc --kubeconfig <backup_management_kubeconfig> \
              delete managedcluster <hosted_cluster_name> \
              -n <hosted_cluster_namespace>
            ```

        5.  Delete the `HostedCluster` resource by running the following command:

            ``` terminal
            $ oc --kubeconfig <backup_management_kubeconfig> \
              delete hostedcluster \
              -n <hosted_cluster_namespace> <hosted_cluster_name>
            ```

</div>

<div>

<div class="title">

Additional resources

</div>

- [Removing a cluster by using the console](https://docs.redhat.com/en/documentation/red_hat_advanced_cluster_management_for_kubernetes/2.13/html/clusters/cluster_mce_overview#remove-a-cluster-by-using-the-console)

- [Removing remaining resources after removing a cluster](https://docs.redhat.com/en/documentation/red_hat_advanced_cluster_management_for_kubernetes/2.13/html/clusters/cluster_mce_overview#removing-a-cluster-from-management-in-special-cases)

</div>

# Observing the backup and restore process

When you use OpenShift API for Data Protection (OADP) to back up and restore a hosted cluster, you can monitor and observe the process.

<div>

<div class="title">

Procedure

</div>

1.  Observe the backup process by running the following command:

    ``` terminal
    $ watch "oc get backups.velero.io -n openshift-adp <backup_resource_name> -o jsonpath=''"
    ```

2.  Observe the restore process by running the following command:

    ``` terminal
    $ watch "oc get restores.velero.io -n openshift-adp <backup_resource_name> -o jsonpath=''"
    ```

3.  Observe the Velero logs by running the following command:

    ``` terminal
    $ oc logs -n openshift-adp -ldeploy=velero -f
    ```

4.  Observe the progress of all of the OADP objects by running the following command:

    ``` terminal
    $ watch "echo BackupRepositories:;echo;oc get backuprepositories.velero.io -A;echo; echo BackupStorageLocations: ;echo; oc get backupstoragelocations.velero.io -A;echo;echo DataUploads: ;echo;oc get datauploads.velero.io -A;echo;echo DataDownloads: ;echo;oc get datadownloads.velero.io -n openshift-adp; echo;echo VolumeSnapshotLocations: ;echo;oc get volumesnapshotlocations.velero.io -A;echo;echo Backups:;echo;oc get backup -A; echo;echo Restores:;echo;oc get restore -A"
    ```

</div>

# Using the Velero CLI to describe the Backup and Restore resources

When you use OpenShift API for Data Protection, you can get more details of the `Backup` and `Restore` resources by using the `velero` command-line interface (CLI).

<div>

<div class="title">

Procedure

</div>

1.  Create an alias to use the `velero` CLI from a container by running the following command:

    ``` terminal
    $ alias velero='oc -n openshift-adp exec deployment/velero -c velero -it -- ./velero'
    ```

2.  Get details of your `Restore` custom resource (CR) by running the following command:

    ``` terminal
    $ velero restore describe <restore_resource_name> --details
    ```

    Replace `<restore_resource_name>` with the name of your `Restore` resource.

3.  Get details of your `Backup` CR by running the following command:

    ``` terminal
    $ velero restore describe <backup_resource_name> --details
    ```

    Replace `<backup_resource_name>` with the name of your `Backup` resource.

</div>
