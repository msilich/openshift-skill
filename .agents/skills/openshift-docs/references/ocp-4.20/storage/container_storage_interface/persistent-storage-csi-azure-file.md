<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

You can provision and manage Azure File storage in OpenShift Container Platform by using the Azure File Container Storage Interface (CSI) Driver Operator and driver, which provide dynamic volume provisioning and eliminate the need to pre-provision storage.

# Overview

OpenShift Container Platform is capable of provisioning persistent volumes (PVs) by using the Container Storage Interface (CSI) driver for Microsoft Azure File Storage.

Familiarity with persistent storage and configuring CSI volumes is recommended when working with a CSI Operator and driver. For more information, see "Understanding persistent storage" and "Configuring CSI volumes".

To create CSI-provisioned PVs that mount to Azure File storage assets, OpenShift Container Platform installs the Azure File CSI Driver Operator and the Azure File CSI driver by default in the `openshift-cluster-csi-drivers` namespace.

Azure File CSI Driver Operator
The Azure File CSI Driver Operator provides a storage class that is named `azurefile-csi` that you can use to create persistent volume claims (PVCs). You can disable this default storage class if desired (see "Managing the default storage").

Azure File CSI driver
The Azure File CSI driver enables you to create and mount Azure File PVs. The Azure File CSI driver supports dynamic volume provisioning by allowing storage volumes to be created on-demand, eliminating the need for cluster administrators to pre-provision storage.

Azure File CSI Driver Operator does not support the following:

- Virtual hard disks (VHD)

- Running on nodes with Federal Information Processing Standard (FIPS) mode enabled for Server Message Block (SMB) file share. However, Network File System (NFS) does support FIPS mode.

For more information about supported features, see "Supported CSI drivers and features".

<div>

<div class="title">

Additional resources

</div>

- [Understanding persistent storage](../understanding-persistent-storage.md#understanding-persistent-storage)

- [Configuring CSI volumes](persistent-storage-csi.md#persistent-storage-csi)

- [Managing the default storage class](persistent-storage-csi-sc-manage.md#persistent-storage-csi-sc-manage)

- [Supported CSI drivers and features](persistent-storage-csi.md#persistent-storage-csi-drivers-supported_persistent-storage-csi)

</div>

# About CSI

The Container Storage Interface (CSI) enables storage vendors to deliver plugins through a standard interface without modifying Kubernetes core code, replacing traditional embedded storage drivers.

CSI Operators give OpenShift Container Platform users storage options, such as volume snapshots, that are not possible with in-tree volume plugins.

# NFS support

OpenShift Container Platform supports the Azure File Container Storage Interface (CSI) Driver Operator with Network File System (NFS).

The following restrictions apply:

- If you create a volume smaller than 100GiB, the CSI driver rounds it up to 100GiB.

- Creating pods with Azure File NFS volumes that are scheduled to the control plane node causes the mount to be denied.

  To work around this issue: If your control plane nodes are schedulable, and the pods can run on worker nodes, use `nodeSelector` or Affinity to schedule the pod in worker nodes.

- FS Group policy behavior:

  > [!IMPORTANT]
  > Azure File CSI with NFS does not honor the fsGroupChangePolicy requested by pods. Azure File CSI with NFS applies a default OnRootMismatch FS Group policy regardless of the policy requested by the pod.

- The Azure File CSI Operator does not automatically create a storage class for NFS. You must create it manually. Use a file similar to the following:

  <div class="formalpara">

  <div class="title">

  Example Azure File storage class YAML file

  </div>

  ``` yaml
  apiVersion: storage.k8s.io/v1
  kind: StorageClass
  metadata:
    name: <storage-class-name>
  provisioner: file.csi.azure.com
  parameters:
    protocol: nfs
    skuName: Premium_LRS  # available values: Premium_LRS, Premium_ZRS
  mountOptions:
    - nconnect=4
  ```

  </div>

- `metadata.name`: Specifies the storage class name.

- `provisioner`: Specifies the Azure File CSI provider.

- `parameters.protocol`: Specifies NFS as the storage backend protocol.

# Azure File cross-subscription support

Cross-subscription support allows you to have an OpenShift Container Platform cluster in one Azure subscription and mount your Azure file share in another Azure subscription by using the Azure File Container Storage Interface (CSI) driver.

> [!IMPORTANT]
> Both the OpenShift Container Platform cluster and the Azure File share (pre-provisioning or to be provisioned) should be inside the same tenant.

## Dynamic provisioning across subscriptions for Azure File

Enable Azure File dynamic provisioning across Azure subscriptions by granting the cluster’s Azure identity access to a storage account in a different subscription, then creating a storage class that references the target subscription.

<div>

<div class="title">

Prerequisites

</div>

- Installed OpenShift Container Platform cluster on Azure with the service principal or managed identity as an Azure identity in one subscription (call it Subscription A)

- Access to another subscription (call it Subscription B) with the storage that is in the same tenant as the cluster

- Logged in to the Azure CLI

</div>

<div>

<div class="title">

Procedure

</div>

1.  Record the Azure identity (service principal or managed identity) by running the following applicable commands. The Azure identity is needed in a later step:

    - If using the *service principal* as the Azure identity when installing the cluster:

      ``` terminal
      $ sp_id=$(oc -n openshift-cluster-csi-drivers get secret azure-file-credentials -o jsonpath='{.data.azure_client_id}' | base64 --decode)
      ```

      ``` terminal
      $ az ad sp show --id ${sp_id} --query displayName --output tsv
      ```

    - If using the *managed identity* as the Azure identity when installing the cluster:

      ``` terminal
      $ mi_id=$(oc -n openshift-cluster-csi-drivers get secret azure-file-credentials -o jsonpath='{.data.azure_client_id}' | base64 --decode)
      ```

      ``` terminal
      $ az identity list --query "[?clientId=='${mi_id}'].{Name:name}" --output tsv
      ```

2.  Grant the Azure identity (service principal or managed identity) permission to access the resource group in another Subscription B where you want to provision the Azure File share by doing one of the following:

    - Run the following Azure CLI command:

      ``` terminal
      az role assignment create \
        --assignee <object-id-or-app-id> \
        --role <role-name> \
        --scope /subscriptions/<subscription-id>/resourceGroups/<resource-group>/providers/Microsoft.Storage/storageAccounts/<storage-account-name>
      ```

      - `<object-id-or-app-id>`: Specifies the service principal or managed identity that you obtained from the previous step, such as `sp_id` or `mi_id`.

      - `<role-name>`: Specifies the role name. Contributor or your own role with required permissions.

      - `<subscription-id>`: Subscription B ID.

      - `<resource-group-name>`: Subscription B resource group name.

        Or

    - Log in to the Azure portal and on the left menu, click **Resource groups**:

      1.  Choose the resource group in Subscription B to which you want to assign a role by clicking **resource group** → **Access control (IAM)** → **Role assignments** tab to view current assignments, and then click **Add** \> **Add role assignment**.

      2.  On the **Role** tab, choose the contributor role to assign, and then click **Next**. You can also create and choose your own role with required permission.

      3.  On the **Members** tab:

          1.  Choose an assignee by selecting the type of assignee: user, group, or service principal (or managed identity).

          2.  Click **Select members**.

          3.  Search for, and then select the desired service principal or managed identity recorded in the previous step.

          4.  Click **Select** to confirm.

      4.  On the **Review + assign** tab, review the settings.

      5.  To finish the role assignment, click **Review + assign**.

          > [!NOTE]
          > If you only want to use a specific storage account to provision the Azure File share, you can also obtain the Azure identity (service principal or managed identity) permission to access the storage account by using similar steps.

3.  Create an Azure File storage class by using a similar configuration to the following:

    <div class="formalpara">

    <div class="title">

    Example Azure File storage class YAML file

    </div>

    ``` yaml
    allowVolumeExpansion: true
    apiVersion: storage.k8s.io/v1
    kind: StorageClass
    metadata:
      name: <sc-name>
    mount options:
      - mfsymlinks
      - cache=strict
      - nosharesock
      - actimeo=30
    parameters:
      subscriptionID: <xxxx-xxxx-xxxx-xxxx-xxxx>
      resourceGroup: <resource group name>
      storageAccount: <storage account>
      skuName: <skuName>
    provisioner: file.csi.azure.com
    reclaimPolicy: Delete
    volumeBindingMode: Immediate
    ```

    </div>

    - `metadata.name`: Specifies the name of the storage class.

    - `parameters.subscriptionID`: Specifies the subscription B ID.

    - `parameters.resourceGroup`: Specifies the Subscription B resource group name.

    - `parameters.storageAccount`: Specifies the storage account name, if you want to specify your own.

    - `parameters.skuName`: Specifies the name of the SKU type.

4.  Create a persistent volume claim (PVC) that specifies the Azure File storage class that you created in the previous step by using a similar configuration to the following:

    <div class="formalpara">

    <div class="title">

    Example PVC YAML file

    </div>

    ``` yaml
    apiVersion: v1
    kind: PersistentVolumeClaim
    metadata:
      name: <pvc-name>
    spec:
      storageClassName: <sc-name-cross-sub>
      accessModes:
        - ReadWriteMany
      resources:
        requests:
          storage: 5Gi
    ```

    </div>

    - `metadata.name`: Specifies the name of the PVC.

    - `spec.storageClassName`: Specifies the name of the storage class that you created in the previous step.

</div>

## Static provisioning across subscriptions for Azure File by creating a PV and PVC:

Provision Azure File storage across subscriptions using static provisioning by creating a secret with storage credentials, then creating a persistent volume (PV) and persistent volume claim (PVC) referencing an Azure File share in a different subscription.

Recommendation to use a storage class
In the following example of static provisioning across subscriptions, the storage class referenced in the PV and PVC is not strictly necessary, as storage classes are not required to accomplish static provisioning. However, it is advisable to use a storage class to avoid cases where a manually created PVC accidentally does not match a manually created PV, and thus potentially triggers dynamic provisioning of a new PV. Other ways to avoid this issue would be to create a storage class with `provisioner: kubernetes.io/no-provisioner` or reference a non-existing storage class, which in both cases ensures that dynamic provisioning does not occur. When using either of these strategies, if a mis-matched PV and PVC occurs, the PVC stays in a pending state, and you can correct the error.

<div>

<div class="title">

Prerequisites

</div>

- Installed OpenShift Container Platform cluster on Azure with the service principal or managed identity as an Azure identity in one subscription (call it Subscription A)

- Access to another subscription (call it Subscription B) with the storage that is in the same tenant as the cluster

- Logged in to the Azure CLI

</div>

<div>

<div class="title">

Procedure

</div>

1.  For your Azure File share, record the resource group, storage account, storage account key, and Azure File name. These values are used for the next steps.

2.  Create a secret for the persistent volume parameter `spec.csi.nodeStageSecretRef.name` by running the following command:

    ``` terminal
    $ oc create secret generic azure-storage-account-<storageaccount-name>-secret --from-literal=azurestorageaccountname="<azure-storage-account-name>" --from-literal azurestorageaccountkey="<azure-storage-account-key>" --type=Opaque
    ```

    `<azure-storage-account-name>` and `<azure-storage-account-key>` are the Azure storage account name and key respectively that you recorded in Step 1.

3.  Create a persistent volume (PV) by using a similar configuration to the following example file:

    <div class="formalpara">

    <div class="title">

    Example PV YAML file

    </div>

    ``` terminal
    apiVersion: v1
    kind: PersistentVolume
    metadata:
      annotations:
        pv.kubernetes.io/provisioned-by: file.csi.azure.com
      name: <pv-name>
    spec:
      capacity:
        storage: 10Gi
      accessModes:
        - ReadWriteMany
      persistentVolumeReclaimPolicy: Retain
      storageClassName: <sc-name>
      mountOptions:
        - cache=strict
        - nosharesock
        - actimeo=30
        - nobrl
      csi:
        driver: file.csi.azure.com
        volumeHandle: "{resource-group-name}#{storage-account-name}#{file-share-name}"
        volumeAttributes:
          shareName: <existing-file-share-name>
        nodeStageSecretRef:
          name: <secret-name>
          namespace: <secret-namespace>
    ```

    </div>

    - `metadata.name`: Specifies the name of the PV.

    - `spec.capacity.storage`: Specifies the size of the PV.

    - `spec.storageClassName`: Specifies the storage class name.

    - `spec.csi.volumeHandle`: Specifies the `volumeHandle` parameter. Ensure that `volumeHandle` is unique for every identical share in the cluster.

    - `spec.csi.volumeAttributes.shareName`: For `` <existing-file-share-name>` ``, use only the file share name and not the full path.

    - `spec.csi.nodeStageSecretRef.name`: Specifies the secret name created in the previous step.

    - `spec.csi.nodeStageSecretRef.namespace`: Specifies the namespace where the secret resides.

4.  Create a persistent value claim (PVC) specifying the existing Azure File share referenced in Step 1 using a similar configuration to the following:

    <div class="formalpara">

    <div class="title">

    Example PVC YAML file

    </div>

    ``` yaml
    apiVersion: v1
    kind: PersistentVolumeClaim
    metadata:
      name: <pvc-name>
    spec:
      storageClassName: <sc-name>
      accessModes:
        - ReadWriteMany
      resources:
        requests:
          storage: 5Gi
    ```

    </div>

    - `metadata.name`: Specifies the name of the PVC.

    - `spec.storageClassName`: Specifies the name of the storage class that you specified for the PV in the previous step.

</div>

# Static provisioning for Azure File

Use static provisioning to manually create persistent volumes (PVs) for existing Azure File shares. Create a secret with storage credentials, define a PV that references the share, and create a persistent volume claim (PVC) to consume the storage.

<div>

<div class="title">

Prerequisites

</div>

- Access to an OpenShift Container Platform cluster with administrator rights

</div>

<div>

<div class="title">

Procedure

</div>

1.  If you have not yet created a secret for the Azure storage account, create it now:

    This secret must contain the Azure Storage Account name and key with the following very specific format with two key-value pairs:

    - `azurestorageaccountname`: \<storage_account_name\>

    - `azurestorageaccountkey`: \<account_key\>

      To create a secret named `azure-secret`, run the following command:

      ``` terminal
      oc create secret generic azure-secret  -n <namespace_name> --type=Opaque --from-literal=azurestorageaccountname="<storage_account_name>" --from-literal=azurestorageaccountkey="<account_key>"
      ```

      - Set `<namespace_name>` to the namespace where the PV is consumed.

      - Provide your values for `<storage_account_name>` and `<account_key>`.

2.  Create a PV by using the following example YAML file:

    <div class="formalpara">

    <div class="title">

    Example PV YAML file

    </div>

    ``` yaml
    apiVersion: v1
    kind: PersistentVolume
    metadata:
      annotations:
        pv.kubernetes.io/provisioned-by: file.csi.azure.com
      name: pv-azurefile
    spec:
      capacity:
        storage: 5Gi
      accessModes:
        - ReadWriteMany
      persistentVolumeReclaimPolicy: Retain
      storageClassName: <sc-name>
      mountOptions:
        - dir_mode=0777
        - file_mode=0777
        - uid=0
        - gid=0
        - cache=strict
        - nosharesock
        - actimeo=30
        - nobrl
      csi:
        driver: file.csi.azure.com
        volumeHandle: "{resource-group-name}#{account-name}#{file-share-name}"
        volumeAttributes:
          shareName: EXISTING_FILE_SHARE_NAME
        nodeStageSecretRef:
          name: azure-secret
          namespace: <my-namespace>
    ```

    </div>

    - `spec.capacity.storage`: Specifies the Volume size.

    - `spec.accessModes`: Defines the read/write and mount permissions. For more information, see "Access modes".

    - `spec.persistentVolumeReclaimPolicy`: Specifies the Reclaim policy, which tells the cluster what to do with the volume after it is released. Accepted values are `Retain`, `Recycle`, or `Delete`.

    - `spec.storageClassName`: Specifies the storage class name. This name is used by the PVC to bind to this specific PV. For static provisioning, a `StorageClass` object does not need to exist, but the name in the PV and PVC must match.

    - `spec.mountOPtions.dir_mode=0777`: Modify this permission if you want to enhance the security.

    - `spec.mountOPtions.cache`: Specifies the cache mode. Accepted values are `none`, `strict`, and `loose`. The default is `strict`.

    - `spec.mountOPtions..nosharesock`: Use to reduce the probability of a reconnect race.

    - `spec.mountOPtions.actimeo`: Specifies the time (in seconds) that the CIFS client caches attributes of a file or directory before it requests attribute information from a server.

    - `spec.mountOPtions.nobrl`: Disables sending byte range lock requests to the server, and for applications which have challenges with POSIX locks.

    - `csi.volumeHandle`: Specifies the `volumeHandle`. Ensure that `volumeHandle` is unique across the cluster. The `resource-group-name` is the Azure resource group where the storage account resides.

    - `csi.volumeAttributes.shareName`: Specifies the file share name. Use only the file share name; do not use full path.

    - `csi.nodeStageSecretRef.name`: Provide the name of the secret created in step 1 of this procedure. In this example, it is `azure-secret`.

    - `csi.nodeStageSecretRef.namespace`: Specifies the namespace that the secret was created in. This must be the namespace where the PV is consumed.

3.  Create a PVC that references the PV using the following example file:

    <div class="formalpara">

    <div class="title">

    Example PVC YAML file

    </div>

    ``` yaml
    apiVersion: v1
    kind: PersistentVolumeClaim
    metadata:
      name: <pvc-name>
      namespace: <my-namespace>
    spec:
      volumeName: pv-azurefile
      storageClassName: <sc-name>
      accessModes:
        - ReadWriteMany
      resources:
        requests:
          storage: 5Gi
    ```

    </div>

    - `metadata.name`: Specifies the PVC name.

    - `metadata.namespace`: Specifies the namespace for the PVC.

    - `spec.volumeName`: Specifies the name of the PV that you created in the previous step.

    - `spec.storageClassName`: Specifies the storage class name. This name is used by the PVC to bind to this specific PV. For static provisioning, a `StorageClass` object does not need to exist, but the name in the PV and PVC must match.

    - `spec.accessModes`: Specifies the access mode. Defines the requested read/write access for the PVC. Claims use the same conventions as volumes when requesting storage with specific access modes. For more information, see "Access modes".

    - `spec.resources.requests.storage`: Specifies the PVC size.

4.  Ensure that the PVC is created and in `Bound` status after a while by running the following command:

    ``` terminal
    $ oc get pvc <pvc-name>
    ```

    Where `<pvc-name>` is the name of your PVC.

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    NAME       STATUS    VOLUME         CAPACITY   ACCESS MODES   STORAGECLASS   AGE
    pvc-name   Bound     pv-azurefile   5Gi        ReadWriteMany  my-sc          7m2s
    ```

    </div>

</div>

<div>

<div class="title">

Additional resources

</div>

- [Persistent storage using Azure File](../persistent_storage/persistent-storage-azure-file.md#persistent-storage-using-azure-file)

- [Access modes](../understanding-persistent-storage.md#pv-access-modes_understanding-persistent-storage)

</div>
