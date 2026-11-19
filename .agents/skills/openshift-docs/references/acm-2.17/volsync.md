> Source: [Red Hat Advanced Cluster Management for Kubernetes 2.17](https://docs.redhat.com/en/documentation/red_hat_advanced_cluster_management_for_kubernetes/2.17/html/volsync/index). Copyright Red Hat.
> Adapted from AsciiDoc to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md), [CC BY-SA 3.0](LICENSE.md) and SOURCE.json for source revisions and gaps.

<a id="volsync"></a>

# VolSync persistent volume replication service

VolSync is a Kubernetes operator that asynchronously replicates persistent volumes within a cluster, or across clusters with storage types that are not otherwise compatible for replication. It uses the Container Storage Interface (CSI) to overcome the compatibility limitation.

**Important:** VolSync only supports replicating persistent volume claims with the `volumeMode` of `Filesystem`. If you do not select the `volumeMode`, it defaults to `Filesystem`.

<div>

<div class="title">

Additional resources

</div>

- [VolSync installation on managed clusters](volsync.md#volsync-install-clusters)

- [Configure an Rsync-TLS replication](volsync.md#rsync-tls-replication-volsync)

- [Configure an Rsync replication](volsync.md#rsync-replication-volsync)

- [Configure a Restic backup](volsync.md#restic-backup-volsync)

- [Configure an Rclone replication](volsync.md#rclone-replication-volsync)

- [Convert a replicated image to a persistent volume claim](volsync.md#volsync-convert-backup-pvc)

- [VolSync replication schedule](volsync.md#volsync-schedule)

- [VolSync copy and storage parameters](volsync.md#volsync-copy-params)

</div>

<a id="volsync-install-clusters"></a>

## VolSync installation on managed clusters

VolSync installation on managed clusters places the VolSync operator in the `volsync-system` namespace. That deployment supports managed clusters that are not OpenShift Container Platform, and is required on both the source and destination clusters for persistent volume claim replication.

If you installed VolSync as an Operator Lifecycle Manager operator on an OpenShift Container Platform managed cluster in an earlier Red Hat Advanced Cluster Management version, the VolSync Operator Lifecycle Manager operator is removed and replaced with the VolSync deployment in the `volsync-system` namespace.

VolSync can be installed with a managed cluster label or with a `ManagedClusterAddOn` resource on the hub cluster.

<div>

<div class="title">

Additional resources

</div>

- [Install VolSync by adding a label in the console](volsync.md#volsync-install-label)

- [Install VolSync by adding a label from the command line](volsync.md#volsync-install-label-cli)

- [Install VolSync by creating a ManagedClusterAddOn](volsync.md#volsync-install-mcaddon)

</div>

<a id="volsync-install-label"></a>

## Install VolSync by adding a label in the console

Install VolSync on a managed cluster by adding the VolSync add-on label from the Red Hat Advanced Cluster Management console.

<div>

<div class="title">

Prerequisites

</div>

- A configured Red Hat OpenShift Container Platform environment on a supported Red Hat Advanced Cluster Management hub cluster

- The storage driver for the source persistent volume is CSI-compatible and supports snapshots

</div>

<div>

<div class="title">

Procedure

</div>

1.  Select a managed cluster from the **Clusters** page in the hub cluster console to view its details.

2.  In the **Labels** field, add the following label:

        addons.open-cluster-management.io/volsync=true

    The VolSync service pod is installed on the managed cluster.

3.  Add the same label to the other managed cluster.

4.  Run the following command on the hub cluster to confirm that the VolSync operator is installed:

    ``` bash
    oc -n <managed-cluster-name> get ManagedClusterAddOn volsync
    ```

    Replace `managed-cluster-name` with the name of the managed cluster.

5.  Verify that the command output shows that the `ManagedClusterAddOn` has a `Ready` status.

6.  Run the following command on the managed cluster to confirm that the VolSync operator is installed:

    ``` bash
    kubectl -n volsync-system get deployment volsync
    ```

</div>

<div>

<div class="title">

Additional resources

</div>

- [Install VolSync by adding a label from the command line](volsync.md#volsync-install-label-cli)

- [Install VolSync by creating a ManagedClusterAddOn](volsync.md#volsync-install-mcaddon)

</div>

<a id="volsync-install-label-cli"></a>

## Install VolSync by adding a label from the command line

Install VolSync on a managed cluster by adding the VolSync add-on label to the `ManagedCluster` resource from the command line.

<div>

<div class="title">

Prerequisites

</div>

- A configured Red Hat OpenShift Container Platform environment on a supported Red Hat Advanced Cluster Management hub cluster

- The storage driver for the source persistent volume is CSI-compatible and supports snapshots

</div>

<div>

<div class="title">

Procedure

</div>

1.  Start a command-line session on the hub cluster.

2.  Enter the following command to add the label to the first managed cluster:

    ``` bash
    oc label managedcluster <managed-cluster-1> "addons.open-cluster-management.io/volsync"="true"
    ```

    Replace `managed-cluster-1` with the name of one of your managed clusters.

3.  Add the label to the second managed cluster. Run the following command:

    ``` bash
    oc label managedcluster <managed-cluster-2> "addons.open-cluster-management.io/volsync"="true"
    ```

    Replace `managed-cluster-2` with the name of your other managed cluster.

    A `ManagedClusterAddOn` resource is created automatically on the hub cluster in the namespace of each corresponding managed cluster.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Install VolSync by adding a label in the console](volsync.md#volsync-install-label)

- [Install VolSync by creating a ManagedClusterAddOn](volsync.md#volsync-install-mcaddon)

</div>

<a id="volsync-install-mcaddon"></a>

## Install VolSync by creating a *ManagedClusterAddOn* resource

Install VolSync on a managed cluster by creating and applying a `ManagedClusterAddOn` resource on the hub cluster.

<div>

<div class="title">

Prerequisites

</div>

- A configured Red Hat OpenShift Container Platform environment on a supported Red Hat Advanced Cluster Management hub cluster

- The storage driver for the source persistent volume is CSI-compatible and supports snapshots

</div>

<div>

<div class="title">

Procedure

</div>

1.  On the hub cluster, create a YAML file called `volsync-mcao.yaml` that contains content that is similar to the following example:

    ``` yaml
    apiVersion: addon.open-cluster-management.io/v1alpha1
    kind: ManagedClusterAddOn
    metadata:
      name: volsync
      namespace: <managed-cluster-1-namespace>
    spec: {}
    ```

    Replace `managed-cluster-1-namespace` with the namespace of one of your managed clusters. This namespace is the same as the name of the managed cluster.

    **Note:** The name of the `ManagedClusterAddOn` must be `volsync`.

2.  Apply the file by entering a command similar to the following example:

    ``` bash
    oc apply -f volsync-mcao.yaml
    ```

3.  Repeat the procedure for the other managed cluster.

</div>

<div>

<div class="title">

Additional resources

</div>

- [VolSync installation on managed clusters](volsync.md#volsync-install-clusters)

</div>

<a id="rsync-tls-replication-volsync"></a>

## Rsync-TLS persistent volume replication

Rsync-TLS-based replication creates a 1:1 asynchronous replication of a persistent volume claim across managed clusters. VolSync synchronizes data by using Rsync across a TLS-protected tunnel that is provided by stunnel.

You can use Rsync-TLS-based replication for disaster recovery or for sending data to a remote site. For more information about stunnel, see the *stunnel documentation*. For more information about Rsync-TLS, see *Usage* in the VolSync documentation.

**Note:** You must copy the values for `address` and `keySecret` from the destination to the source, so configure the destination before you configure the source.

Before you configure Rsync-TLS replication, ensure that the following requirements are met:

- VolSync is installed on the source and destination managed clusters. See *VolSync installation on managed clusters*.

- At least two managed clusters for the same Red Hat Advanced Cluster Management hub cluster

- Network connectivity between the clusters that you configure with VolSync. If the clusters are not on the same network, you can configure the *Submariner multicluster networking and service discovery* and use the `ClusterIP` value for `ServiceType`, or use a load balancer with the `LoadBalancer` value for `ServiceType`.

- The source persistent volume claim is on a CSI storage class

<div>

<div class="title">

Additional resources

</div>

- [VolSync installation on managed clusters](volsync.md#volsync-install-clusters)

- [Submariner multicluster networking and service discovery](networking.md#submariner)

- [Configure an Rsync-TLS replication destination](volsync.md#volsync-rsync-tls-destination)

- [Copy the Rsync-TLS key secret to the source cluster](volsync.md#volsync-rsync-tls-copy-secret)

- [Configure an Rsync-TLS replication source](volsync.md#volsync-rsync-tls-source)

- [Verify an Rsync-TLS replication](volsync.md#volsync-rsync-tls-verify)

- [Rsync-TLS key secret](volsync.md#volsync-rsync-create-tls-secret)

- [Convert a replicated image to a persistent volume claim](volsync.md#volsync-convert-backup-pvc)

- [Usage](https://volsync.readthedocs.io/en/latest/usage/index.html)

- [VolSync copy and storage parameters](volsync.md#volsync-copy-params)

- [VolSync replication schedule](volsync.md#volsync-schedule)

- [stunnel documentation](https://www.stunnel.org/docs.html)

</div>

<a id="volsync-rsync-tls-destination"></a>

## Configure an Rsync-TLS replication destination

Configure a `ReplicationDestination` on the destination cluster and capture the `.status.rsyncTLS.address` and `.status.rsyncTLS.keySecret` values to use on the source cluster.

<div>

<div class="title">

Prerequisites

</div>

- VolSync is installed on the source and destination managed clusters. See [VolSync installation on managed clusters](volsync.md#volsync-install-clusters).

- At least two managed clusters for the same Red Hat Advanced Cluster Management hub cluster

- Network connectivity between the clusters that you configure with VolSync. If the clusters are not on the same network, you can configure the [Submariner multicluster networking and service discovery](networking.md#submariner) and use the `ClusterIP` value for `ServiceType`, or use a load balancer with the `LoadBalancer` value for `ServiceType`.

- The source persistent volume claim is on a CSI storage class

</div>

<div>

<div class="title">

Procedure

</div>

1.  Run the following command on the destination cluster to create the namespace:

    ``` bash
    oc create ns <destination-ns>
    ```

    Replace `destination-ns` with the namespace where your replication destination is located.

2.  Create a file named `replication_destination.yaml`. Your resource might resemble the following content:

    ``` yaml
    apiVersion: volsync.backube/v1alpha1
    kind: ReplicationDestination
    metadata:
      name: <destination>
      namespace: <destination-ns>
    spec:
      rsyncTLS:
        serviceType: LoadBalancer
        copyMethod: Snapshot
        capacity: 2Gi
        accessModes: [ReadWriteOnce]
        storageClassName: gp2-csi
        volumeSnapshotClassName: csi-aws-vsc
    ```

    - For this example, the `serviceType` value of `LoadBalancer` is used. The load balancer service enables your source managed cluster to transfer information to a different destination managed cluster. You can use `ClusterIP` as the service type if your source and destinations are on the same cluster, or if you have Submariner network service configured. Note the address and the name of the secret to refer to when you configure the source cluster.

    - Make sure that the `capacity` value matches the capacity of the persistent volume claim that is being replicated.

    - Replace `destination` with the name of your replication destination custom resource.

    - Replace `destination-ns` with the name of the namespace where your destination is located.

3.  Run the following command on the destination cluster to create the `ReplicationDestination` resource:

    ``` bash
    oc create -n <destination-ns> -f replication_destination.yaml
    ```

    Replace `destination-ns` with the name of the namespace where your destination is located.

    After the `ReplicationDestination` resource is created, the `.status.rsyncTLS.address` field provides the destination address for source-to-destination communication, and the `.status.rsyncTLS.keySecret` field provides the name of the TLS key secret that authenticates the connection with the source cluster.

4.  Run the following command to copy the value of `.status.rsyncTLS.address` to use on the source cluster:

    ``` bash
    ADDRESS=`oc get replicationdestination <destination> -n <destination-ns> --template={{.status.rsyncTLS.address}}`
    echo $ADDRESS
    ```

    - Replace `destination` with the name of your replication destination custom resource.

    - Replace `destination-ns` with the name of the namespace where your destination is located.

      The output appears similar to the following example, which is for an Amazon Web Services environment:

    <!-- -->

        a831264645yhrjrjyer6f9e4a02eb2-5592c0b3d94dd376.elb.us-east-1.amazonaws.com

5.  Run the following command to copy the name of the secret:

    ``` bash
    KEYSECRET=`oc get replicationdestination <destination> -n <destination-ns> --template={{.status.rsyncTLS.keySecret}}`
    echo $KEYSECRET
    ```

    - Replace `destination` with the name of your replication destination custom resource.

    - Replace `destination-ns` with the name of the namespace where your destination is located.

      Use the TLS key secret name from the output when you configure the source cluster. The output might resemble the following name:

    <!-- -->

        volsync-rsync-tls-destination-name

</div>

<div class="formalpara">

<div class="title">

Next steps

</div>

To copy the TLS key secret to the source cluster, see [Copy the Rsync-TLS key secret to the source cluster](volsync.md#volsync-rsync-tls-copy-secret).

</div>

<a id="volsync-rsync-tls-copy-secret"></a>

## Copy the Rsync-TLS key secret to the source cluster

Copy the Rsync-TLS key secret from the destination cluster to the source cluster so that the `ReplicationSource` can authenticate to the destination.

<div>

<div class="title">

Prerequisites

</div>

- You configured a `ReplicationDestination` and captured the `.status.rsyncTLS.keySecret` value. See [Configure an Rsync-TLS replication destination](volsync.md#volsync-rsync-tls-destination).

</div>

<div>

<div class="title">

Procedure

</div>

1.  Copy the key secret from the destination cluster by entering the following command:

    ``` bash
    oc get secret -n <destination-ns> $KEYSECRET -o yaml > /tmp/secret.yaml
    ```

    Replace `destination-ns` with the namespace where your replication destination is located.

2.  Open the secret file by entering the following command:

    ``` bash
    vi /tmp/secret.yaml
    ```

3.  Change the namespace to the namespace of your source cluster. For this example, it is `source-ns`.

4.  Remove the owner references (`.metadata.ownerReferences`).

5.  On the source cluster, create the secret by entering the following command:

    ``` bash
    oc create -f /tmp/secret.yaml
    ```

</div>

<div class="formalpara">

<div class="title">

Next steps

</div>

To configure the `ReplicationSource`, see [Configure an Rsync-TLS replication source](volsync.md#volsync-rsync-tls-source).

</div>

<a id="volsync-rsync-tls-source"></a>

## Configure an Rsync-TLS replication source

Configure a `ReplicationSource` on the source cluster by using the address and TLS key secret values that you copied from the `ReplicationDestination`.

<div>

<div class="title">

Prerequisites

</div>

- You configured a `ReplicationDestination` and captured the `.status.rsyncTLS.address` and `.status.rsyncTLS.keySecret` values. See [Configure an Rsync-TLS replication destination](volsync.md#volsync-rsync-tls-destination).

- You copied the Rsync-TLS key secret to the source cluster. See [Copy the Rsync-TLS key secret to the source cluster](volsync.md#volsync-rsync-tls-copy-secret).

- The source persistent volume claim is on a CSI storage class

</div>

<div>

<div class="title">

Procedure

</div>

1.  Identify the source persistent volume claim that you want to replicate.

2.  Create the `ReplicationSource` resource on the source cluster. Your resource might resemble the following content:

    ``` yaml
    apiVersion: volsync.backube/v1alpha1
    kind: ReplicationSource
    metadata:
      name: <source>
      namespace: <source-ns>
    spec:
      sourcePVC: <persistent_volume_claim>
      trigger:
        schedule: "*/3 * * * *"
      rsyncTLS:
        keySecret: <mykeysecret>
        address: <my.host.com>
        copyMethod: Snapshot
        storageClassName: gp2-csi
        volumeSnapshotClassName: csi-aws-vsc
    ```

    - Replace `source` with the name for your replication source custom resource.

    - Replace `source-ns` with the namespace of the persistent volume claim where your source is located.

    - Replace `persistent_volume_claim` with the name of your source persistent volume claim.

    - Replace `mykeysecret` with the name of the secret that you copied from the destination cluster to the source cluster (the value of `$KEYSECRET`).

    - Replace `my.host.com` with the host address that you copied from the `.status.rsyncTLS.address` field of the `ReplicationDestination`.

3.  On the source cluster, replace the `address` and `keySecret` values with the values that you noted from the destination cluster, then create the resource:

    ``` bash
    sed -i "s/<my.host.com>/$ADDRESS/g" replication_source.yaml
    sed -i "s/<mykeysecret>/$KEYSECRET/g" replication_source.yaml
    oc create -n <source-ns> -f replication_source.yaml
    ```

    Replace `source-ns` with the namespace of the persistent volume claim where your source is located.

    **Note:** You must create the file in the same namespace as the persistent volume claim that you want to replicate.

</div>

<div class="formalpara">

<div class="title">

Next steps

</div>

To verify that the replication completed, see [Verify an Rsync-TLS replication](volsync.md#volsync-rsync-tls-verify).

</div>

<a id="volsync-rsync-tls-verify"></a>

## Verify an Rsync-TLS replication

Verify that the Rsync-TLS replication completed by checking the status of the `ReplicationSource` object on the source cluster.

<div>

<div class="title">

Prerequisites

</div>

- You created a `ReplicationSource` on the source cluster. See [Configure an Rsync-TLS replication source](volsync.md#volsync-rsync-tls-source).

</div>

<div>

<div class="title">

Procedure

</div>

1.  Verify that the replication completed by running the following command on the `ReplicationSource` object:

    ``` bash
    oc describe ReplicationSource -n <source-ns> <source>
    ```

    - Replace `source-ns` with the namespace of the persistent volume claim where your source is located.

    - Replace `source` with the name of your replication source custom resource.

      If the replication is successful, the output should be similar to the following example:

    <!-- -->

        Status:
          Conditions:
            Last Transition Time:  2021-10-14T20:48:00Z
            Message:               Synchronization in-progress
            Reason:                SyncInProgress
            Status:                True
            Type:                  Synchronizing
            Last Transition Time:  2021-10-14T20:41:41Z
            Message:               Reconcile complete
            Reason:                ReconcileComplete
            Status:                True
            Type:                  Reconciled
          Last Sync Duration:      5m20.764642395s
          Last Sync Time:          2021-10-14T20:47:01Z
          Next Sync Time:          2021-10-14T20:48:00Z

    If the `Last Sync Time` has no time listed, then the replication is not complete.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Rsync-TLS key secret](volsync.md#volsync-rsync-create-tls-secret)

- [Convert a replicated image to a persistent volume claim](volsync.md#volsync-convert-backup-pvc)

- [Usage](https://volsync.readthedocs.io/en/latest/usage/index.html)

- [VolSync copy and storage parameters](volsync.md#volsync-copy-params)

- [VolSync replication schedule](volsync.md#volsync-schedule)

</div>

<a id="rsync-replication-volsync"></a>

## Rsync persistent volume replication

Rsync-based replication creates a 1:1 asynchronous replication of a persistent volume claim across managed clusters. You can use Rsync-based replication for disaster recovery or for sending data to a remote site.

**Important:** Use Rsync-TLS instead of Rsync for enhanced security. By using Rsync-TLS, you can avoid using elevated user permissions that are not required for replicating persistent volumes.

For Rsync-based replication, configure custom resources on the source and destination clusters. The custom resources use the `address` value to connect the source to the destination, and the `sshKeys` to ensure that the transferred data is secure.

**Note:** You must copy the values for `address` and `sshKeys` from the destination to the source, so configure the destination before you configure the source.

Before you configure Rsync replication, ensure that the following requirements are met:

- VolSync is installed on the source and destination managed clusters. See [VolSync installation on managed clusters](volsync.md#volsync-install-clusters).

- At least two managed clusters for the same Red Hat Advanced Cluster Management hub cluster

- Network connectivity between the clusters that you configure with VolSync. If the clusters are not on the same network, you can configure the [Submariner multicluster networking and service discovery](networking.md#submariner) and use the `ClusterIP` value for `ServiceType`, or use a load balancer with the `LoadBalancer` value for `ServiceType`.

- The source persistent volume claim is on a CSI storage class

<div>

<div class="title">

Additional resources

</div>

- [Configure an Rsync replication destination](volsync.md#volsync-rsync-destination)

- [Copy the Rsync SSH secret to the source cluster](volsync.md#volsync-rsync-copy-secret)

- [Configure an Rsync replication source](volsync.md#volsync-rsync-source)

- [Verify an Rsync replication](volsync.md#volsync-rsync-verify)

- [Configure an Rsync-TLS replication](volsync.md#rsync-tls-replication-volsync)

- [Convert a replicated image to a persistent volume claim](volsync.md#volsync-convert-backup-pvc)

- [Usage](https://volsync.readthedocs.io/en/latest/usage/index.html)

- [VolSync copy and storage parameters](volsync.md#volsync-copy-params)

- [VolSync replication schedule](volsync.md#volsync-schedule)

</div>

<a id="volsync-rsync-destination"></a>

## Configure an Rsync replication destination

Configure a `ReplicationDestination` on the destination cluster and capture the `.status.rsync.address` and `.status.rsync.sshKeys` values to use on the source cluster.

<div>

<div class="title">

Prerequisites

</div>

- VolSync is installed on the source and destination managed clusters. See [VolSync installation on managed clusters](volsync.md#volsync-install-clusters).

- At least two managed clusters for the same Red Hat Advanced Cluster Management hub cluster

- Network connectivity between the clusters that you configure with VolSync. If the clusters are not on the same network, you can configure the [Submariner multicluster networking and service discovery](networking.md#submariner) and use the `ClusterIP` value for `ServiceType`, or use a load balancer with the `LoadBalancer` value for `ServiceType`.

- The source persistent volume claim is on a CSI storage class

</div>

<div>

<div class="title">

Procedure

</div>

1.  Run the following command on the destination cluster to create the namespace:

    ``` bash
    oc create ns <destination-ns>
    ```

    Replace `destination-ns` with a name for the namespace that will contain your destination persistent volume claim.

2.  Create a file named `replication_destination.yaml`. Your resource might resemble the following content:

    ``` yaml
    apiVersion: volsync.backube/v1alpha1
    kind: ReplicationDestination
    metadata:
      name: <destination>
      namespace: <destination-ns>
    spec:
      rsync:
        serviceType: LoadBalancer
        copyMethod: Snapshot
        capacity: 2Gi
        accessModes: [ReadWriteOnce]
        storageClassName: gp2-csi
        volumeSnapshotClassName: csi-aws-vsc
    ```

    - For this example, the `serviceType` value of `LoadBalancer` is used. The load balancer service enables your source managed cluster to transfer information to a different destination managed cluster. You can use `ClusterIP` as the service type if your source and destinations are on the same cluster, or if you have Submariner network service configured. Note the address and the name of the secret to refer to when you configure the source cluster.

    - Make sure that the `capacity` value matches the capacity of the persistent volume claim that is being replicated.

    - Replace `destination` with the name of your replication destination custom resource.

    - Replace `destination-ns` with the name of the namespace where your destination is located.

3.  Run the following command on the destination cluster to create the `ReplicationDestination` resource:

    ``` bash
    oc create -n <destination-ns> -f replication_destination.yaml
    ```

    Replace `destination-ns` with the name of the namespace where your destination is located.

    After the `ReplicationDestination` resource is created, the `.status.rsync.address` field provides the destination address for source-to-destination communication, and the `.status.rsync.sshKeys` field provides the name of the SSH key secret for secure data transfer.

4.  Run the following command to copy the value of `.status.rsync.address` to use on the source cluster:

    ``` bash
    ADDRESS=`oc get replicationdestination <destination> -n <destination-ns> --template={{.status.rsync.address}}`
    echo $ADDRESS
    ```

    - Replace `destination` with the name of your replication destination custom resource.

    - Replace `destination-ns` with the name of the namespace where your destination is located.

      The output should appear similar to the following example for an Amazon Web Services environment:

    <!-- -->

        a831264645yhrjrjyer6f9e4a02eb2-5592c0b3d94dd376.elb.us-east-1.amazonaws.com

5.  Run the following command to copy the name of the secret:

    ``` bash
    SSHKEYS=`oc get replicationdestination <destination> -n <destination-ns> --template={{.status.rsync.sshKeys}}`
    echo $SSHKEYS
    ```

    - Replace `destination` with the name of your replication destination custom resource.

    - Replace `destination-ns` with the name of the namespace where your destination is located.

      Use the SSH keys secret name from the output when you configure the source cluster. The output might resemble the following name:

    <!-- -->

        volsync-rsync-dst-src-destination-name

</div>

<div class="formalpara">

<div class="title">

Next steps

</div>

To copy the SSH secret to the source cluster, see [Copy the Rsync SSH secret to the source cluster](volsync.md#volsync-rsync-copy-secret).

</div>

<a id="volsync-rsync-copy-secret"></a>

## Copy the Rsync SSH secret to the source cluster

Copy the Rsync SSH secret from the destination cluster to the source cluster so that the `ReplicationSource` can authenticate to the destination.

<div>

<div class="title">

Prerequisites

</div>

- You configured a `ReplicationDestination` and captured the `.status.rsync.sshKeys` value. See [Configure an Rsync replication destination](volsync.md#volsync-rsync-destination).

</div>

<div>

<div class="title">

Procedure

</div>

1.  Copy the SSH secret from the destination cluster by entering the following command:

    ``` bash
    oc get secret -n <destination-ns> $SSHKEYS -o yaml > /tmp/secret.yaml
    ```

2.  Replace `destination-ns` with the namespace of the persistent volume claim where your destination is located.

3.  Open the secret file by entering the following command:

    ``` bash
    vi /tmp/secret.yaml
    ```

4.  Change the namespace to the namespace of your source cluster. For this example, it is `source-ns`.

5.  Remove the owner references (`.metadata.ownerReferences`).

6.  On the source cluster, create the secret by entering the following command:

    ``` bash
    oc create -f /tmp/secret.yaml
    ```

</div>

<div class="formalpara">

<div class="title">

Next steps

</div>

To configure the `ReplicationSource`, see [Configure an Rsync replication source](volsync.md#volsync-rsync-source).

</div>

<a id="volsync-rsync-source"></a>

## Configure an Rsync replication source

Configure a `ReplicationSource` on the source cluster by using the address and SSH keys values that you copied from the `ReplicationDestination`.

<div>

<div class="title">

Prerequisites

</div>

- You configured a `ReplicationDestination` and captured the `.status.rsync.address` and `.status.rsync.sshKeys` values. See [Configure an Rsync replication destination](volsync.md#volsync-rsync-destination).

- You copied the Rsync SSH secret to the source cluster. See [Copy the Rsync SSH secret to the source cluster](volsync.md#volsync-rsync-copy-secret).

- The source persistent volume claim is on a CSI storage class

</div>

<div>

<div class="title">

Procedure

</div>

1.  Identify the source persistent volume claim that you want to replicate.

2.  Create the `ReplicationSource` resource on the source cluster. Your resource might resemble the following content:

    ``` yaml
    apiVersion: volsync.backube/v1alpha1
    kind: ReplicationSource
    metadata:
      name: <source>
      namespace: <source-ns>
    spec:
      sourcePVC: <persistent_volume_claim>
      trigger:
        schedule: "*/3 * * * *"
      rsync:
        sshKeys: <mysshkeys>
        address: <my.host.com>
        copyMethod: Snapshot
        storageClassName: gp2-csi
        volumeSnapshotClassName: csi-aws-vsc
    ```

    - Replace `source` with the name for your replication source custom resource.

    - Replace `source-ns` with the namespace of the persistent volume claim where your source is located.

    - Replace `persistent_volume_claim` with the name of your source persistent volume claim.

    - Replace `mysshkeys` with the keys that you copied from the `.status.rsync.sshKeys` field of the `ReplicationDestination` when you configured it.

    - Replace `my.host.com` with the host address that you copied from the `.status.rsync.address` field of the `ReplicationDestination` when you configured it.

3.  On the source cluster, replace the `address` and `sshKeys` values with the values that you noted from the destination cluster, then create the resource:

    ``` bash
    sed -i "s/<my.host.com>/$ADDRESS/g" replication_source.yaml
    sed -i "s/<mysshkeys>/$SSHKEYS/g" replication_source.yaml
    oc create -n <source-ns> -f replication_source.yaml
    ```

4.  Replace `source-ns` with the namespace of the persistent volume claim where your source is located.

    **Note:** You must create the file in the same namespace as the persistent volume claim that you want to replicate.

</div>

<div class="formalpara">

<div class="title">

Next steps

</div>

To verify that the replication completed, see [Verify an Rsync replication](volsync.md#volsync-rsync-verify).

</div>

<a id="volsync-rsync-verify"></a>

## Verify an Rsync replication

Verify that the Rsync replication completed by checking the status of the `ReplicationSource` object on the source cluster.

<div>

<div class="title">

Prerequisites

</div>

- You created a `ReplicationSource` on the source cluster. See [Configure an Rsync replication source](volsync.md#volsync-rsync-source).

</div>

<div>

<div class="title">

Procedure

</div>

1.  Verify that the replication completed by running the following command on the `ReplicationSource` object:

    ``` bash
    oc describe ReplicationSource -n <source-ns> <source>
    ```

    - Replace `source-ns` with the namespace of the persistent volume claim where your source is located.

    - Replace `source` with the name of your replication source custom resource.

      If the replication was successful, the output should be similar to the following example:

    <!-- -->

        Status:
          Conditions:
            Last Transition Time:  2021-10-14T20:48:00Z
            Message:               Synchronization in-progress
            Reason:                SyncInProgress
            Status:                True
            Type:                  Synchronizing
            Last Transition Time:  2021-10-14T20:41:41Z
            Message:               Reconcile complete
            Reason:                ReconcileComplete
            Status:                True
            Type:                  Reconciled
          Last Sync Duration:      5m20.764642395s
          Last Sync Time:          2021-10-14T20:47:01Z
          Next Sync Time:          2021-10-14T20:48:00Z

    If the `Last Sync Time` has no time listed, then the replication is not complete.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Configure an Rsync-TLS replication](volsync.md#rsync-tls-replication-volsync)

- [Convert a replicated image to a persistent volume claim](volsync.md#volsync-convert-backup-pvc)

- [Usage](https://volsync.readthedocs.io/en/latest/usage/index.html)

- [VolSync copy and storage parameters](volsync.md#volsync-copy-params)

- [VolSync replication schedule](volsync.md#volsync-schedule)

</div>

<a id="restic-backup-volsync"></a>

## Configure a Restic backup

Configure a Restic backup of a persistent volume by creating a repository secret and a `ReplicationSource`. A Restic backup does not synchronize data between clusters. It copies backup data to the location that you specify in your `restic-config` secret.

<div>

<div class="title">

Prerequisites

</div>

- VolSync is installed on the managed cluster. See [VolSync installation on managed clusters](volsync.md#volsync-install-clusters).

- The storage driver for the source persistent volume is CSI-compatible and supports snapshots

</div>

<div>

<div class="title">

Procedure

</div>

1.  Specify a repository where your backup images are stored by creating a secret. Your resource might resemble the following example:

    ``` yaml
    apiVersion: v1
    kind: Secret
    metadata:
      name: restic-config
    type: Opaque
    stringData:
      RESTIC_REPOSITORY: <my-restic-repository>
      RESTIC_PASSWORD: <my-restic-password>
      AWS_ACCESS_KEY_ID: access
      AWS_SECRET_ACCESS_KEY: password
    ```

    - Replace `my-restic-repository` with the location of the S3 bucket repository where you want to store your backup files.

    - Replace `my-restic-password` with the encryption key that is required to access the repository.

    - Replace `access` and `password` with the credentials for your provider, if required.

      If you need to prepare a new repository, see [Preparing a new repository](https://restic.readthedocs.io/en/stable/030_preparing_a_new_repo.html) for the procedure. If you use that procedure, skip the step that requires you to run the `restic init` command. VolSync automatically initializes the repository during the first backup.

      **Important:** When you back up multiple persistent volume claims to the same S3 bucket, the path to the bucket must be unique for each persistent volume claim. Each persistent volume claim is backed up with a separate `ReplicationSource`, and each requires a separate restic-config secret. By sharing the same S3 bucket, each `ReplicationSource` has write access to the entire S3 bucket.

2.  Create the `ReplicationSource` resource to configure your backup policy. Your resource might resemble the following example:

    ``` yaml
    apiVersion: volsync.backube/v1alpha1
    kind: ReplicationSource
    metadata:
      name: mydata-backup
    spec:
      sourcePVC: <source>
      trigger:
        schedule: "*/30 * * * *"
      restic:
        pruneIntervalDays: 14
        repository: <restic-config>
        retain:
          hourly: 6
          daily: 5
          weekly: 4
          monthly: 2
          yearly: 1
        copyMethod: Clone
    ```

    - Replace `source` with the persistent volume claim that you are backing up.

    - Replace the value for `schedule` with how often to run the backup. This example runs every 30 minutes.

    - Replace the value of `pruneIntervalDays` with the number of days that elapse between instances of repacking the data to save space. The prune operation can generate significant I/O traffic while it is running.

    - Replace `restic-config` with the name of the secret that you created in the previous step.

    - Set the values for `retain` to your retention policy for the backed up images.

      **Note:** Use `Clone` for the value of `copyMethod` to ensure that a point-in-time image is saved.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Restore a Restic backup](volsync.md#restore-restic-backup)

- [Run VolSync movers as root](volsync.md#volsync-privileged-movers)

- [VolSync copy and storage parameters](volsync.md#volsync-copy-params)

- [VolSync replication schedule](volsync.md#volsync-schedule)

- [Backup options](https://volsync.readthedocs.io/en/latest/usage/restic/index.html#backup-options)

</div>

<a id="restore-restic-backup"></a>

## Restore a Restic backup

Restore copied data from a Restic backup into a new persistent volume claim by creating the claim and a `ReplicationDestination` that points to that claim. The restore process needs to be completed only once. This example restores the most recent backup.

<div>

<div class="title">

Procedure

</div>

1.  Create a new persistent volume claim to contain the restored data. Your resource might resemble the following example:

    ``` yaml
    kind: PersistentVolumeClaim
    apiVersion: v1
    metadata:
      name: <pvc-name>
    spec:
      accessModes:
        - ReadWriteOnce
      resources:
        requests:
          storage: 3Gi
    ```

    - Replace `pvc-name` with the name of the new persistent volume claim.

      **Note:** Restore only one backup into a new persistent volume claim.

2.  Create a `ReplicationDestination` custom resource to specify where to restore the data. Your resource might resemble the following example:

    ``` yaml
    apiVersion: volsync.backube/v1alpha1
    kind: ReplicationDestination
    metadata:
      name: <destination>
    spec:
      trigger:
        manual: restore-once
      restic:
        repository: <restic-repo>
        destinationPVC: <pvc-name>
        copyMethod: Direct
    ```

    - Replace `destination` with the name of your replication destination custom resource.

    - Replace `restic-repo` with the path to your repository where the source is stored.

    - Replace `pvc-name` with the name of the persistent volume claim where you want to restore the data. Use an existing persistent volume claim for this value, rather than provisioning a new one.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Configure a Restic backup](volsync.md#restic-backup-volsync)

- [Restore options](https://volsync.readthedocs.io/en/latest/usage/restic/index.html#restore-options)

</div>

<a id="rclone-replication-volsync"></a>

## Configure an Rclone replication

Configure an Rclone replication to copy a single persistent volume to multiple locations by creating a `ReplicationSource` and a `ReplicationDestination` that use Rclone through an intermediate object storage location, such as AWS S3.

<div>

<div class="title">

Prerequisites

</div>

- VolSync is installed on the managed clusters that participate in the replication. See [VolSync installation on managed clusters](volsync.md#volsync-install-clusters).

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create the `ReplicationSource` resource on the source cluster. Your resource might resemble the following example:

    ``` yaml
    apiVersion: volsync.backube/v1alpha1
    kind: ReplicationSource
    metadata:
      name: <source>
      namespace: <source-ns>
    spec:
      sourcePVC: <source-pvc>
      trigger:
        schedule: "*/6 * * * *"
      rclone:
        rcloneConfigSection: <intermediate-s3-bucket>
        rcloneDestPath: <destination-bucket>
        rcloneConfig: <rclone-secret>
        copyMethod: Snapshot
        storageClassName: <my-sc-name>
        volumeSnapshotClassName: <my-vsc>
    ```

    - Replace `source` with the name for your replication source custom resource.

    - Replace `source-ns` with the namespace of the persistent volume claim where your source is located.

    - Replace `source-pvc` with the persistent volume claim that you are replicating.

    - Replace the value of `schedule` with how often to run the replication. This example runs every 6 minutes. The value must be within quotation marks.

    - Replace `intermediate-s3-bucket` with the path to the configuration section of the Rclone configuration file.

    - Replace `destination-bucket` with the path to the object bucket where you want your replicated files copied.

    - Replace `rclone-secret` with the name of the secret that contains your Rclone configuration information.

2.  Create the `ReplicationDestination` resource. Your resource might resemble the following example:

    ``` yaml
    apiVersion: volsync.backube/v1alpha1
    kind: ReplicationDestination
    metadata:
      name: database-destination
      namespace: dest
    spec:
      trigger:
        schedule: "3,9,15,21,27,33,39,45,51,57 * * * *"
      rclone:
        rcloneConfigSection: <intermediate-s3-bucket>
        rcloneDestPath: <destination-bucket>
        rcloneConfig: <rclone-secret>
        copyMethod: Snapshot
        accessModes: [ReadWriteOnce]
        capacity: 10Gi
        storageClassName: <my-sc>
        volumeSnapshotClassName: <my-vsc>
    ```

    - Replace the value for `schedule` with how often to move the replication to the destination. The schedules for the source and destination must be offset so that the data can finish replicating before it is pulled from the destination. This example runs every 6 minutes, offset by 3 minutes. The value must be within quotation marks.

    - Replace `intermediate-s3-bucket` with the path to the configuration section of the Rclone configuration file.

    - Replace `destination-bucket` with the path to the object bucket where you want your replicated files copied.

    - Replace `rclone-secret` with the name of the secret that contains your Rclone configuration information.

    - The value for `accessModes` specifies the access modes for the persistent volume claim. Valid values are `ReadWriteOnce` or `ReadWriteMany`.

    - The `capacity` value specifies the size of the destination volume, which must be large enough to contain the incoming data.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Run VolSync movers as root](volsync.md#volsync-privileged-movers)

- [Convert a replicated image to a persistent volume claim](volsync.md#volsync-convert-backup-pvc)

- [VolSync copy and storage parameters](volsync.md#volsync-copy-params)

- [VolSync replication schedule](volsync.md#volsync-schedule)

</div>

<a id="volsync-privileged-movers"></a>

## Run VolSync movers as root

Run Restic or Rclone movers as root by annotating the namespace with the elevated permissions annotation. Restic and Rclone movers run without root permissions by default.

<div>

<div class="title">

Procedure

</div>

1.  Run the following command to add the elevated permissions annotation to your namespace:

    ``` bash
    oc annotate namespace <namespace> volsync.backube/privileged-movers=true
    ```

2.  Replace `namespace` with the name of your namespace.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Configure a Restic backup](volsync.md#restic-backup-volsync)

- [Configure an Rclone replication](volsync.md#rclone-replication-volsync)

</div>

<a id="volsync-convert-backup-pvc"></a>

## Convert a replicated image to a persistent volume claim

Convert the copy of the image to a usable persistent volume claim to recover data from a replicated image. When you replicate or restore a persistent volume claim from a `ReplicationDestination` by using a `VolumeSnapshot`, a `VolumeSnapshot` is created. The `VolumeSnapshot` contains the `latestImage` from the last successful synchronization. The VolSync `ReplicationDestination` volume populator converts that image to a usable persistent volume claim.

<div>

<div class="title">

Procedure

</div>

1.  Create a persistent volume claim with a `dataSourceRef` that references the `ReplicationDestination` where you want to restore a persistent volume claim. This persistent volume claim is populated with the contents of the `VolumeSnapshot` that is specified in the `status.latestImage` setting of the `ReplicationDestination` custom resource definition. The following YAML content shows a sample persistent volume claim that might be used:

    ``` yaml
    apiVersion: v1
    kind: PersistentVolumeClaim
    metadata:
      name: <pvc-name>
      namespace: <destination-ns>
    spec:
      accessModes:
        - ReadWriteOnce
      dataSourceRef:
        kind: ReplicationDestination
        apiGroup: volsync.backube
        name: <replicationdestination_to_replace>
      resources:
        requests:
          storage: 2Gi
    ```

    - Replace `pvc-name` with a name for your new persistent volume claim.

    - Replace `destination-ns` with the namespace where the persistent volume claim and `ReplicationDestination` are located.

    - Replace `replicationdestination_to_replace` with the `ReplicationDestination` name.

      **Note:** You can update `resources.requests.storage` with a different value when the value is at least the same size as the initial source persistent volume claim.

2.  Validate that your persistent volume claim is running in the environment. Replace `destination-ns` with the namespace where the persistent volume claim is located. Run the following command:

    ``` bash
    kubectl get pvc -n <destination-ns>
    ```

    **Notes:**

    - If no `latestImage` exists, the persistent volume claim remains in a pending state until the `ReplicationDestination` completes and a snapshot is available. You can create a `ReplicationDestination` and a persistent volume claim that use the `ReplicationDestination` at the same time. The persistent volume claim starts the volume population process only after the `ReplicationDestination` completes a replication and a snapshot is available. You can find the snapshot in `.status.latestImage`.

    - If the storage class that is used has a `volumeBindingMode` value of `WaitForFirstConsumer`, the volume populator waits until there is a consumer of the persistent volume claim before the volume is populated. When a consumer requires access, such as a pod that wants to mount the persistent volume claim, then the volume is populated. The VolSync volume populator controller uses the `latestImage` from the `ReplicationDestination`. The `latestImage` is updated each time a replication completes after the persistent volume claim was created.

</div>

<div>

<div class="title">

Additional resources

</div>

- [VolSync persistent volume replication service](volsync.md#volsync)

</div>

<a id="volsync-schedule"></a>

## VolSync replication schedule

A VolSync replication can start continuously, on a schedule, or manually. The replication starts when the scheduled time occurs.

See the following order of the schedule values:

    "minute (0-59) hour (0-23) day-of-month (1-31) month (1-12) day-of-week (0-6)"

Your setting for this replication option might resemble the following content:

``` yaml
spec:
  trigger:
    schedule: "*/6 * * * *"
```

<div>

<div class="title">

Additional resources

</div>

- [VolSync](https://volsync.readthedocs.io/en/latest/index.html)

- [Configure an Rsync-TLS replication](volsync.md#rsync-tls-replication-volsync)

- [Configure an Rclone replication](volsync.md#rclone-replication-volsync)

</div>

<a id="volsync-copy-params"></a>

## VolSync copy and storage parameters

The `copyMethod`, `storageClassName`, and `volumeSnapshotClassName` fields control how VolSync creates a point-in-time copy of a persistent volume claim.

`copyMethod`  
Specifies whether a point-in-time copy is generated, and which method is used. Valid values include `Clone`, `Direct`, and `Snapshot`. If your storage driver supports cloning, `Clone` can be a more streamlined process for replication. For Restic backups, use `Clone` when you want to ensure that a point-in-time image is saved.

`storageClassName`  
Name of the storage class to use for the point-in-time copy. Specify this value when you use a storage class that is different from the default for your environment. If you omit the value on a `ReplicationSource`, the storage class of the source volume is used. If you omit the value on a `ReplicationDestination`, the system storage class is used.

`volumeSnapshotClassName`  
Name of the `VolumeSnapshotClass` to use when `copyMethod` is `Snapshot`. This value is not required for other `copyMethod` values. If you omit the value, the system default `VolumeSnapshotClass` is used.

<div>

<div class="title">

Additional resources

</div>

- [Configure an Rsync-TLS replication](volsync.md#rsync-tls-replication-volsync)

- [Configure an Rsync replication](volsync.md#rsync-replication-volsync)

- [Configure a Restic backup](volsync.md#restic-backup-volsync)

- [Configure an Rclone replication](volsync.md#rclone-replication-volsync)

</div>

<a id="volsync-rsync-create-tls-secret"></a>

## Rsync-TLS key secret

The source and destination clusters must have access to the shared key for the TLS connection. You can find the key location in the `keySecret` field. If you do not provide a secret name in `.spec.rsyncTLS.keySecret`, the secret name is automatically generated and added to `.status.rsyncTLS.keySecret`.

See the following format for the secret:

    <id>:<at_least_32_hex_digits>

See the following example: `1:23b7395fafc3e842bd8ac0fe142e6ad1`

The corresponding secret might resemble the following example:

``` yaml
apiVersion: v1
data:
  # echo -n 1:23b7395fafc3e842bd8ac0fe142e6ad1 | base64
  psk.txt: MToyM2I3Mzk1ZmFmYzNlODQyYmQ4YWMwZmUxNDJlNmFkMQ==
kind: Secret
metadata:
  name: tls-key-secret
type: Opaque
```

<div>

<div class="title">

Additional resources

</div>

- [Configure an Rsync-TLS replication](volsync.md#rsync-tls-replication-volsync)

</div>
