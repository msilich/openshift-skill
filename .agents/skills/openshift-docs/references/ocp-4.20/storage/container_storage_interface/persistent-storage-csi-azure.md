<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

You can provision and manage Azure Disk storage in OpenShift Container Platform by using the Azure Disk Container Storage Interface (CSI) Driver Operator and driver, which provide dynamic volume provisioning and eliminate the need to pre-provision storage.

# Overview of Azure Disk CSI Driver Operator

OpenShift Container Platform is capable of provisioning persistent volumes (PVs) using the Container Storage Interface (CSI) driver for Microsoft Azure Disk Storage.

Familiarity with persistent storage and configuring CSI volumes is recommended when working with a CSI Operator and driver. For more information about these topics, see "Understanding persistent storage" and "Configuring CSI volumes".

To create CSI-provisioned PVs that mount to Azure Disk storage assets, OpenShift Container Platform installs the Azure Disk CSI Driver Operator and the Azure Disk CSI driver by default in the `openshift-cluster-csi-drivers` namespace.

Azure Disk CSI Driver Operator
The Azure Disk CSI Driver Operator provides a storage class named `managed-csi` that you can use to create persistent volume claims (PVCs). The Azure Disk CSI Driver Operator supports dynamic volume provisioning by allowing storage volumes to be created on-demand, eliminating the need for cluster administrators to pre-provision storage. You can disable this default storage class if desired (see "Managing the default storage class").

Azure Disk CSI driver
The Azure Disk CSI driver enables you to create and mount Azure Disk PVs.

> [!NOTE]
> OpenShift Container Platform provides automatic migration for the Azure Disk in-tree volume plugin to its equivalent CSI driver. For more information, see "CSI automatic migration".

<div>

<div class="title">

Additional resources

</div>

- [Understanding persistent storage](../understanding-persistent-storage.md#understanding-persistent-storage)

- [Configuring CSI volumes](persistent-storage-csi.md#persistent-storage-csi)

- [Managing the default storage class](persistent-storage-csi-sc-manage.md#persistent-storage-csi-sc-manage)

- [CSI automatic migration](persistent-storage-csi-migration.md#persistent-storage-csi-migration)

</div>

# About CSI

The Container Storage Interface (CSI) enables storage vendors to deliver plugins through a standard interface without modifying Kubernetes core code, replacing traditional embedded storage drivers.

CSI Operators give OpenShift Container Platform users storage options, such as volume snapshots, that are not possible with in-tree volume plugins.

# Creating a storage class with storage account type

To provision persistent volumes with specific performance and redundancy characteristics, create a storage class that designates an Azure storage account type corresponding to your SKU tier.

Storage classes are used to differentiate and delineate storage levels and usages. By defining a storage class, you can obtain dynamically provisioned persistent volumes.

When creating a storage class, you can designate the storage account type. This corresponds to your Azure storage account SKU tier. Valid options are `Standard_LRS`, `Premium_LRS`, `StandardSSD_LRS`, `UltraSSD_LRS`, `Premium_ZRS`, and `StandardSSD_ZRS`. For information about finding your Azure SKU tier, see "SKU Types".

Both zone-redundant storage (ZRS) and PremiumV2_LRS have some region limitations. For information about these limitations, see "ZRS limitations" and "Premium_LRS limitations".

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

1.  Create a storage class designating the storage account type using a YAML file similar to the following:

    ``` terminal
    $ oc create -f - << EOF
    apiVersion: storage.k8s.io/v1
    kind: StorageClass
    metadata:
      name: <storage-class>
    provisioner: disk.csi.azure.com
    parameters:
      skuName: <storage-class-account-type>
    reclaimPolicy: Delete
    volumeBindingMode: WaitForFirstConsumer
    allowVolumeExpansion: true
    EOF
    ```

    - `metadata.name`: Specifies the storage class name.

    - `parameters.skuName`: The storage account type. This corresponds to your Azure storage account SKU tier:\`Standard_LRS\`, `Premium_LRS`, `StandardSSD_LRS`, `UltraSSD_LRS`, `Premium_ZRS`, `StandardSSD_ZRS`, `PremiumV2_LRS`.

      > [!NOTE]
      > For PremiumV2_LRS, specify `cachingMode: None` in `storageclass.parameters`.

2.  Ensure that the storage class was created by listing the storage classes:

    ``` terminal
    $ oc get storageclass
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    NAME                    PROVISIONER          RECLAIMPOLICY   VOLUMEBINDINGMODE      ALLOWVOLUMEEXPANSION   AGE
    azurefile-csi           file.csi.azure.com   Delete          Immediate              true                   68m
    managed-csi (default)   disk.csi.azure.com   Delete          WaitForFirstConsumer   true                   68m
    sc-prem-zrs             disk.csi.azure.com   Delete          WaitForFirstConsumer   true                   4m25s
    ```

    </div>

    In this example, `sc-prem-zrs` is the new storage class with storage account type.

</div>

<div>

<div class="title">

Additional resources

</div>

- [SKU Types](https://learn.microsoft.com/en-us/rest/api/storagerp/srp_sku_types)

- [ZRS limitations](https://learn.microsoft.com/en-us/azure/virtual-machines/disks-deploy-zrs?tabs=portal#limitations)

- [Premium_LRS limitations](https://learn.microsoft.com/en-us/azure/virtual-machines/disks-deploy-premium-v2?tabs=azure-cli#limitations)

</div>

# Performance plus for Azure Disk

You can enhance Azure disk performance by enabling performance plus to increase IOPS and throughput limits for certain Azure disk types 513 GiB, and larger.

## Overview of performance plus

Performance plus increases Input/Output Operations Per Second (IOPS) and throughput limits for certain Azure disk types 513 GiB, and larger.

The following Azure disk types support performance plus:

- Azure Premium solid-state drives (SSD)

- Standard SSDs

- Standard hard disk drives (HDD)

To see what the increased limits are for IOPS and throughput, consult the columns that begin with **Expanded** in the tables in "Scalability and performance targets for VM disks".

<div>

<div class="title">

Additional resources

</div>

- [Scalability and performance targets for VM disks](https://learn.microsoft.com/en-us/azure/virtual-machines/disks-scalability-targets)

</div>

## Limitations for performance plus

To successfully enable performance plus, verify that your disk configuration meets the required type, size, and provisioning criteria before attempting to use this feature.

Performance plus for Azure Disk has the following limitations:

- Can be enabled only on Standard HDD, Standard SSD, and Premium SSD managed disks that are 513 GiB or larger.

  > [!IMPORTANT]
  > If you request a smaller value, the disk size is rounded up to 513GiB.

- Can be enabled only on new disks. For a workaround, see "Enabling performance plus by snapshot or cloning".

<div>

<div class="title">

Additional resources

</div>

- [Enabling performance plus by snapshot or cloning](persistent-storage-csi-azure.md#persistent-storage-csi-azure-disk-perf-plus-create-new-disk-by-snapshot-clone_persistent-storage-csi-azure)

</div>

## Creating a storage class to use performance plus enhanced disks

To provision Azure disks with enhanced IOPS and throughput, create a storage class with performance plus enabled that automatically applies to persistent volume claims.

<div>

<div class="title">

Prerequisites

</div>

- Access to a Microsoft Azure cluster with cluster-admin privileges.

- Access to an Azure disk with performance plus enabled.

  For information about enabling performance plus on disks, see the "Microsoft Azure storage documentation".

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create a storage class using the following example YAML file:

    <div class="formalpara">

    <div class="title">

    Example storage class YAML file

    </div>

        apiVersion: storage.k8s.io/v1
        kind: StorageClass
        metadata:
          name: <azure-disk-performance-plus-sc>
        provisioner: disk.csi.azure.com
        parameters:
          skuName: Premium_LRS
          cachingMode: ReadOnly
          enablePerformancePlus: "true"
        reclaimPolicy: Delete
        volumeBindingMode: WaitForFirstConsumer
        allowVolumeExpansion: true

    </div>

    - `metadata.name`: Specifies the name of the storage class.

    - `provisioner`: Specifies the Azure Disk Container Storage Interface (CSI) driver provisioner.

    - `parameters.skuName`: Specifies the Azure disk type SKU. In this example, `Premium_LRS` for Premium SSD Locally Redundant Storage.

    - `parameters.enablePerformancePlus`: Enables Azure Disk performance plus.

2.  Create a persistent volume claim (PVC) that uses this storage class by using the following example YAML file:

    <div class="formalpara">

    <div class="title">

    Example PVC YAML file

    </div>

    ``` yaml
    apiVersion: v1
    kind: PersistentVolumeClaim
    metadata:
      name: <my-azure-pvc>
    spec:
      accessModes:
        - ReadWriteOnce
      storageClassName: <azure-disk-performance-plus-sc>
      resources:
        requests:
          storage: 513Gi
    ```

    </div>

    - `metadata.name`: Specifies the PVC name.

    - `spec.storageClassName`: References the performance plus storage class.

    - `spec.resources.requests.storage`: Any disk size smaller than 513GiB is automatically rounded up.

</div>

## Enabling performance plus by snapshot or cloning

To work around the limitation that performance plus applies only to new disks, snapshot or clone an existing volume to provision a new disk with performance plus enabled.

Normally, performance plus can be enabled only on new disks. For a workaround, you can use this procedure.

<div>

<div class="title">

Prerequisites

</div>

- Access to a Microsoft Azure cluster with cluster-admin privileges.

- Access to an Azure disk with performance plus enabled.

- Have created a storage class to use performance plus enhanced Azure disks.

  For more information about creating the storage class, see "Creating a storage class to use performance plus enhanced disks".

</div>

<div>

<div class="title">

Procedure

</div>

1.  Do one of the following to enable performance plus:

    - Create a snapshot of the existing volume that does not have performance plus enabled on it, and then provision a new disk from that snapshot using a storage class with `enablePerformancePlus` set to "true".

    - Clone the persistent volume claim (PVC) using a storage class with `enablePerformancePlus` set to "true" to create a new disk clone.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Creating a storage class to use performance plus enhanced disks](persistent-storage-csi-azure.md#persistent-storage-csi-azure-disk-perf-plus-sc_persistent-storage-csi-azure)

</div>

# User-managed encryption

The user-managed encryption feature allows you to provide keys during installation that encrypt OpenShift Container Platform node root volumes, and enables all managed storage classes to use these keys to encrypt provisioned storage volumes.

You must specify the custom key in the `platform.<cloud_type>.defaultMachinePlatform` field in the install-config YAML file.

This features supports the following storage types:

- Amazon Web Services (AWS) Elastic Block storage (EBS)

  > [!NOTE]
  > If there is no encrypted key defined in the storage class, only set `encrypted: "true"` in the storage class. The AWS EBS CSI driver uses the AWS managed alias/aws/ebs, which is created by Amazon EBS automatically in each region by default to encrypt provisioned storage volumes. In addition, the managed storage classes all have the `encrypted: "true"` setting.

  For information about installing AWS EBS with user-managed encryption, see "Optional AWS configuration parameters".

- Microsoft Azure Disk storage

  > [!NOTE]
  > If the OS (root) disk is encrypted, and there is no encrypted key defined in the storage class, Azure Disk CSI driver uses the OS disk encryption key by default to encrypt provisioned storage volumes.

  For information about installing Azure Disk with user-managed encryption, see "Preparing an Azure Disk Encryption Set".

- Google Cloud Platform (GCP) persistent disk (PD) storage

  For information about installing GCP PD with user-managed encryption, see "Additional Google Cloud configuration parameters".

- IBM Cloud® Virtual Private Cloud (VPC) Block storage

  For information about installing with IBM Cloud with user-managed encryption, see "User-managed encryption for IBM Cloud" and "Installing on IBM Cloud".

<div>

<div class="title">

Additional resources

</div>

- [Preparing an Azure Disk Encryption Set](../../installing/installing_azure/ipi/installing-azure-preparing-ipi.md#preparing-disk-encryption-sets_installing-azure-preparing-ipi)

</div>

# Machine sets that deploy machines with ultra disks using PVCs

You can create a machine set running on Microsoft Azure that deploys machines with ultra disks. Ultra disks are high-performance storage that are intended for use with the most demanding data workloads.

Both the in-tree plugin and CSI driver support using PVCs to enable ultra disks. You can also deploy machines with ultra disks as data disks without creating a PVC.

<div>

<div class="title">

Additional resources

</div>

- [Microsoft Azure ultra disks documentation](https://docs.microsoft.com/en-us/azure/virtual-machines/disks-types#ultra-disks)

- [Machine sets that deploy machines on ultra disks using in-tree PVCs](../persistent_storage/persistent-storage-azure.md#machineset-azure-ultra-disk_persistent-storage-azure)

- [Machine sets that deploy machines on ultra disks as data disks](../../machine_management/creating_machinesets/creating-machineset-azure.md#machineset-azure-ultra-disk_creating-machineset-azure)

</div>

## Creating machines with ultra disks by using machine sets

You can deploy machines with ultra disks on Microsoft Azure by editing your machine set YAML file.

<div>

<div class="title">

Prerequisites

</div>

- Have an existing Microsoft Azure cluster.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Copy an existing Azure `MachineSet` custom resource (CR) and edit it by running the following command:

    ``` terminal
    $ oc edit machineset <machine_set_name>
    ```

    where:

    `<machine_set_name>`
    Indicates the machine set that you want to provision machines with ultra disks.

2.  Add the following lines in the positions indicated:

    ``` yaml
    apiVersion: machine.openshift.io/v1beta1
    kind: MachineSet
    spec:
      template:
        spec:
          metadata:
            labels:
              disk: ultrassd
          providerSpec:
            value:
              ultraSSDCapability: Enabled
    ```

    where:

    `spec.template.spec.metadata.labels.disk`
    Specifies a label to use to select a node that is created by this machine set. The example uses `disk.ultrassd` for this value.

    `spec.template.spec.providerSpec.value.ultraSSDCapability`
    Enables the use of ultra disks.

3.  Create a machine set by using the updated configuration by running the following command:

    ``` terminal
    $ oc create -f <machine_set_name>.yaml
    ```

4.  Create a storage class that contains the following YAML definition:

    ``` yaml
    apiVersion: storage.k8s.io/v1
    kind: StorageClass
    metadata:
      name: ultra-disk-sc
    parameters:
      cachingMode: None
      diskIopsReadWrite: "2000"
      diskMbpsReadWrite: "320"
      kind: managed
      skuname: UltraSSD_LRS
    provisioner: disk.csi.azure.com
    reclaimPolicy: Delete
    volumeBindingMode: WaitForFirstConsumer
    ```

    where:

    `metadata.name`
    Specifies the name of the storage class. The example uses `ultra-disk-sc` for this value.

    `parameters.diskIopsReadWrite`
    Specifies the number of Input/Output Operations Per Second (IOPS) for the storage class.

    `parameters.diskMbpsReadWrite`
    Specifies the throughput in MBps for the storage class.

    `provisioner`
    For Microsoft Azure Kubernetes Service (AKS) version 1.21 or later, use `disk.csi.azure.com`. For earlier versions of AKS, use `kubernetes.io/azure-disk`.

    `volumeBindingMode`
    Optional parameter. Specifies this parameter to wait for the creation of the pod that will use the disk.

5.  Create a persistent volume claim (PVC) to reference the `ultra-disk-sc` storage class that contains the following YAML definition:

    ``` yaml
    apiVersion: v1
    kind: PersistentVolumeClaim
    metadata:
      name: ultra-disk
    spec:
      accessModes:
      - ReadWriteOnce
      storageClassName: ultra-disk-sc
      resources:
        requests:
          storage: 4Gi
    ```

    where:

    `metadata.name`
    Specifies the name of the PVC. The example uses `ultra-disk` for this value.

    `spec.storageClassName`
    Specifies the name of the storage class to use. The example uses `ultra-disk-sc` storage class.

    `spec.resources.requests.storage`
    Specifies the size for the storage class. The minimum value is `4Gi`.

6.  Create a pod that contains the following YAML definition:

    ``` yaml
    apiVersion: v1
    kind: Pod
    metadata:
      name: nginx-ultra
    spec:
      nodeSelector:
        disk: ultrassd
      containers:
      - name: nginx-ultra
        image: alpine:latest
        command:
          - "sleep"
          - "infinity"
        volumeMounts:
        - mountPath: "/mnt/azure"
          name: volume
      volumes:
        - name: volume
          persistentVolumeClaim:
            claimName: ultra-disk
    ```

    where:

    `spec.nodeSelector.disk`
    Specifies the label of the machine set that enables the use of ultra disks. The example uses `disk.ultrassd` for this value.

    `spec.volumes.persistentVolumeClaim.claimName`
    Specifies the name of the PVC to attach. This pod references the `ultra-disk` PVC.

</div>

<div>

<div class="title">

Verification

</div>

1.  Validate that the machines are created by running the following command:

    ``` terminal
    $ oc get machines
    ```

    The machines should be in the `Running` state.

2.  For a machine that is running and has a node attached, validate the partition by running the following command:

    ``` terminal
    $ oc debug node/<node_name> -- chroot /host lsblk
    ```

    In this command, `oc debug node/<node_name>` starts a debugging shell on the node `<node_name>` and passes a command with `--`. The passed command `chroot /host` provides access to the underlying host OS binaries, and `lsblk` shows the block devices that are attached to the host OS machine.

</div>

<div>

<div class="title">

Next steps

</div>

- To use an ultra disk from within a pod, create a workload that uses the mount point. Create a YAML file similar to the following example:

  ``` yaml
  apiVersion: v1
  kind: Pod
  metadata:
    name: ssd-benchmark1
  spec:
    containers:
    - name: ssd-benchmark1
      image: nginx
      ports:
        - containerPort: 80
          name: "http-server"
      volumeMounts:
      - name: lun0p1
        mountPath: "/tmp"
    volumes:
      - name: lun0p1
        hostPath:
          path: /var/lib/lun0p1
          type: DirectoryOrCreate
    nodeSelector:
      disktype: ultrassd
  ```

</div>

## Troubleshooting resources for machine sets that enable ultra disks

You can recover from issues that you might encounter when you enable ultra disks for machine sets. Review fields, such as disk settings, and ensure that the parameters are correctly configured.

### Unable to mount a persistent volume claim backed by an ultra disk

If there is an issue mounting a persistent volume claim backed by an ultra disk, the pod becomes stuck in the `ContainerCreating` state and an alert is triggered.

For example, if the `additionalCapabilities.ultraSSDEnabled` parameter is not set on the machine that backs the node that hosts the pod, the following error message appears:

``` terminal
StorageAccountType UltraSSD_LRS can be used only when additionalCapabilities.ultraSSDEnabled is set.
```

- To resolve this issue, describe the pod by running the following command:

  ``` terminal
  $ oc -n <stuck_pod_namespace> describe pod <stuck_pod_name>
  ```

# Additional resources

- [Persistent storage using Azure Disk](../persistent_storage/persistent-storage-azure.md#persistent-storage-using-azure)

- [Configuring CSI volumes](persistent-storage-csi.md#persistent-storage-csi)

- [Microsoft Azure storage documentation](https://learn.microsoft.com/en-us/azure/?product=storage)
