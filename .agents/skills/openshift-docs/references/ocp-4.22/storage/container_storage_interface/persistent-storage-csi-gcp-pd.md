<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

You can provision and manage Google Cloud Platform (GCP) persistent disk (PD) storage in OpenShift Container Platform by using the GCP PD Container Storage Interface (CSI) Driver Operator and driver, which provide dynamic volume provisioning and eliminate the need to pre-provision storage.

# Overview of GCP PD CSI Driver Operator

You can provision and manage Google Cloud Platform (GCP) persistent disk (PD) storage in OpenShift Container Platform by using the GCP PD Container Storage Interface (CSI) Driver Operator and driver, which are installed by default.

Familiarity with persistent storage and configuring CSI volumes is recommended when working with a CSI Operator and driver. For more information, see "Understanding persistent storage" and "Configuring CSI volumes".

To create CSI-provisioned persistent volumes (PVs) that mount to GCP PD storage assets, OpenShift Container Platform installs the GCP PD CSI Driver Operator and the GCP PD CSI driver by default in the `openshift-cluster-csi-drivers` namespace.

GCP PD CSI Driver Operator
By default, the GCP PD CSI Driver Operator provides a storage class that you can use to create PVCs. You can disable this default storage class if desired (see "Managing the default storage class"). You also have the option to create the GCP PD storage class as described in "Persistent storage using GCE Persistent Disk".

GCP PD driver
The GCP PD driver enables you to create and mount GCP PD PVs.

GCP PD CSI driver supports the C3 instance type for bare metal and N4 machine series. The C3 instance type and N4 machine series support the hyperdisk-balanced disks and hyperdisk-balanced high-availability disks. For more information, see "C3 instance type for bare metal and N4 machine series".

> [!NOTE]
> OpenShift Container Platform provides automatic migration for the GCE Persistent Disk in-tree volume plugin to its equivalent CSI driver. For more information, see "CSI automatic migration".

<div>

<div class="title">

Additional resources

</div>

- [Understanding persistent storage](../understanding-persistent-storage.md#understanding-persistent-storage)

- [Configuring CSI volumes](persistent-storage-csi.md#persistent-storage-csi)

- [Managing the default storage class](persistent-storage-csi-sc-manage.md#persistent-storage-csi-sc-manage)

- [Persistent storage using GCE Persistent Disk](../persistent_storage/persistent-storage-gce.md#persistent-storage-using-gce)

- [C3 instance type for bare metal and N4 machine series](persistent-storage-csi-gcp-pd.md#persistent-storage-csi-gcp-hyperdisk-overview_persistent-storage-csi-gcp-pd)

- [CSI automatic migration](persistent-storage-csi-migration.md#persistent-storage-csi-migration)

</div>

# About CSI

The Container Storage Interface (CSI) enables storage vendors to deliver plugins through a standard interface without modifying Kubernetes core code, replacing traditional embedded storage drivers.

CSI Operators give OpenShift Container Platform users storage options, such as volume snapshots, that are not possible with in-tree volume plugins.

# Reducing permissions while using the GCP PD CSI Driver Operator

By default, the Google Cloud Platform (GCP) persistent disk (PD) Container Storage Interface (CSI) Driver can impersonate any service account in the Google Cloud project. You can reduce the scope of permissions to only the required node service accounts.

To reduce permissions, grant the `iam.serviceAccountUser` role to the control plane and compute node service accounts, and then remove the `iam.serviceAccountUser` role from the project-wide service account, thus reducing the scope of the permission.

> [!NOTE]
> Reducing permissions only applies to GCP clusters using Workload Identity Federation (WIF).

<div>

<div class="title">

Procedure

</div>

1.  Grant scoped `iam.serviceAccountUser` role for node service accounts by running the following Bash commands:

    ``` terminal
    gcloud iam service-accounts add-iam-policy-binding "${MASTER_NODE_SA}" --project="${GOOGLE_PROJECT_ID}" --member="serviceAccount:${SERVICE_ACCOUNT_EMAIL}" --role="roles/iam.serviceAccountUser" --condition=None
    gcloud iam service-accounts add-iam-policy-binding "${WORKER_NODE_SA}" --project="${GOOGLE_PROJECT_ID}" --member="serviceAccount:${SERVICE_ACCOUNT_EMAIL}" --role="roles/iam.serviceAccountUser" --condition=None
    ```

    - `GOOGLE_PROJECT_ID`: The unique ID of your Google Cloud project.

    - `SERVICE_ACCOUNT_EMAIL`: The email address of the "Member" (the person or service account) who is being granted the new permissions. To find the service account, on WIF clusters, there is a default service account on GCP for the CSI driver based on the cluster name, for example: `${CLUSTER_NAME}-openshift-gcp-pd-csi-*`.

    - `MASTER_NODE_SA`: The email address of the service account used by your cluster’s master node.

    - `WORKER_NODE_SA`: The email address of the service account used by your cluster’s worker nodes.

2.  Remove project-level `iam.serviceAccountUser` role from the binding created by the installation program by running the following Bash commands:

    ``` terminal
    gcloud projects remove-iam-policy-binding "${GOOGLE_PROJECT_ID}" --member="serviceAccount:${SERVICE_ACCOUNT_EMAIL}" --role="roles/iam.serviceAccountUser" --condition=None
    ```

    - `SERVICE_ACCOUNT_EMAIL`: The email address of the account losing the permission. For example, `my-app-sa@my-project.iam.gserviceaccount.com`. To find the service account, on WIF clusters, there is a default service account on GCP for the CSI driver based on the cluster name, for example: `${CLUSTER_NAME}-openshift-gcp-pd-csi-*`.

    - `GOOGLE_PROJECT_ID`: The unique ID of the Google Cloud project where this is occurring. For example, `prod-data-789`.

</div>

# GCP PD CSI driver storage class parameters

To configure persistent volume provisioning behavior for Google Cloud Platform (GCP) persistent disk (PD), use storage class parameters that control disk type, replication, and encryption settings.

The GCP PD Container Storage Interface (CSI) driver uses the CSI `external-provisioner` sidecar as a controller. This is a separate helper container that is deployed with the CSI driver. The sidecar manages persistent volumes (PVs) by triggering the `CreateVolume` operation.

The GCP PD CSI driver uses the `csi.storage.k8s.io/fstype` parameter key to support dynamic provisioning. The following table describes all the GCP PD CSI storage class parameters that are supported by OpenShift Container Platform.

<table>
<caption>CreateVolume Parameters</caption>
<colgroup>
<col style="width: 18%" />
<col style="width: 27%" />
<col style="width: 18%" />
<col style="width: 36%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Parameter</th>
<th style="text-align: left;">Values</th>
<th style="text-align: left;">Default</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>type</code></p></td>
<td style="text-align: left;"><p><code>pd-ssd</code>, <code>pd-standard</code>, <code>pd-balanced</code>, or <code>hyperdisk-balanced</code></p></td>
<td style="text-align: left;"><p><code>pd-standard</code></p></td>
<td style="text-align: left;"><p>Allows you to choose between standard PVs or solid-state-drive PVs.</p>
<p>The driver does not validate the value, thus all the possible values are accepted.</p>
<p>For <code>hyperdisk-balanced</code>, be sure to check the limitations under "C3 and N4 instance type limitations".</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>replication-type</code></p></td>
<td style="text-align: left;"><p><code>none</code> or <code>regional-pd</code></p></td>
<td style="text-align: left;"><p><code>none</code></p></td>
<td style="text-align: left;"><p>Allows you to choose between zonal or regional PVs.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>disk-encryption-kms-key</code></p></td>
<td style="text-align: left;"><p>Fully qualified resource identifier for the key to use to encrypt new disks.</p></td>
<td style="text-align: left;"><p>Empty string</p></td>
<td style="text-align: left;"><p>Uses customer-managed encryption keys (CMEK) to encrypt new disks.</p></td>
</tr>
</tbody>
</table>

<div>

<div class="title">

Additional resources

</div>

- [C3 and N4 instance type limitations](persistent-storage-csi-gcp-pd.md#persistent-storage-csi-gcp-hyperdisk-limitations_persistent-storage-csi-gcp-pd)

</div>

# C3 instance type for bare metal and N4 machines series

You can use hyperdisk-balanced storage on Google Cloud Platform (GCP) C3 bare metal and N4 machine series instances to achieve high performance.

## C3 and N4 instance type limitations

Before deploying hyperdisk-balanced disks on C3 bare metal or N4 machine series instances, review the volume size, cloning, resizing, and storage class requirements to ensure successful configuration.

The GCP PD CSI driver support for the C3 instance type for bare metal and N4 machine series have the following limitations:

- You must set the volume size to at least 4Gi when you create hyperdisk-balanced disks. OpenShift Container Platform does not round up to the minimum size, so you must specify the correct size yourself.

- Cloning volumes is not supported when using storage pools.

- For cloning or resizing, hyperdisk-balanced disks original volume size must be 6Gi or greater.

- The default storage class is standard-csi.

  > [!IMPORTANT]
  > You need to manually create a storage class.
  >
  > For information about creating the storage class, see Step 2 in "Setting up hyperdisk-balanced disks".

- Clusters with mixed virtual machines (VMs) that use different storage types, for example, N2 and N4, are not supported. This is due to hyperdisks-balanced disks not being usable on most legacy VMs. Similarly, regular persistent disks are not usable on N4/C3 VMs.

- A GCP cluster with c3-standard-2, c3-standard-4, n4-standard-2, and n4-standard-4 nodes can erroneously exceed the maximum attachable disk number, which should be 16. For more information, see "OCPBUGS-39258".

- For more limitations, see Google Cloud documentation "Limitations for Hyperdisk".

<div>

<div class="title">

Additional resources

</div>

- [Setting up hyperdisk-balanced disk](persistent-storage-csi-gcp-pd.md#persistent-storage-csi-gcp-hyperdisk-storage-pools-procedure_persistent-storage-csi-gcp-pd)

- [OCPBUGS-39258](https://issues.redhat.com/browse/OCPBUGS-39258)

- [Limitations for Hyperdisk](https://cloud.google.com/compute/docs/disks/hyperdisks#limitations)

</div>

## Hyperdisk-balanced high availability disks overview

You can improve application resilience against zone failures by using Hyperdisk Balanced High Availability volumes that synchronously replicate data across two zones in the same region.

Hyperdisk Balanced High Availability volumes are useful for:

- Protecting your applications from a zonal outage by synchronously replicating data across two zones in the same region

- When you require write access to the same volume in multiple zones

> [!NOTE]
> Volume Attributes Classes (VAC) does not work on Hyperdisk Balanced High Availability disks.

To set up Hyperdisk Balanced High Availability disks, see "Setting up hyperdisk-balanced disks".

<div>

<div class="title">

Additional resources

</div>

- [Setting up hyperdisk-balanced disk](persistent-storage-csi-gcp-pd.md#persistent-storage-csi-gcp-hyperdisk-storage-pools-procedure_persistent-storage-csi-gcp-pd)

</div>

## Storage pools for hyperdisk-balanced disks overview

You can simplify storage management and reduce costs by using hyperdisk storage pools to aggregate capacity, throughput, and IOPS into a single pool instead of managing individual disks.

Hyperdisk storage pools can be used with Compute Engine for large-scale storage. A hyperdisk storage pool is a purchased collection of capacity, throughput, and IOPS, which you can then provision for your applications as needed. You can use hyperdisk storage pools to create and manage disks in pools and use the disks across multiple workloads. By managing disks in aggregate, you can save costs while achieving expected capacity and performance growth. By using only the storage that you need in hyperdisk storage pools, you reduce the complexity of forecasting capacity and reduce management by going from managing hundreds of disks to managing a single storage pool.

## Setting up hyperdisk-balanced disks

To provision high-performance hyperdisk-balanced storage volumes, configure a storage class, create persistent volume claims, and deploy applications that use the hyperdisk storage.

<div>

<div class="title">

Prerequisites

</div>

- Access to the cluster with administrative privileges

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create a GCP cluster with attached disks provisioned with hyperdisk-balanced disks.

2.  Create a storage class specifying the hyperdisk-balanced disks during installation:

    1.  Follow the procedure in "Installing a cluster on GCP with customizations".

        For your install-config.yaml file, use the following example file:

        <div class="formalpara">

        <div class="title">

        Example install-config YAML file

        </div>

        ``` yaml
        apiVersion: v1
        metadata:
          name: ci-op-9976b7t2-8aa6b

        sshKey: |
          XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
        baseDomain: XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
        platform:
          gcp:
            projectID: XXXXXXXXXXXXXXXXXXXXXX
            region: us-central1
        controlPlane:
          architecture: amd64
          name: master
          platform:
            gcp:
              type: n4-standard-4
              osDisk:
                diskType: hyperdisk-balanced
                diskSizeGB: 200
          replicas: 3
        compute:
        - architecture: amd64
          name: worker
          replicas: 3
          platform:
            gcp:
              type: n4-standard-4
              osDisk:
                diskType: hyperdisk-balanced
        ```

        </div>

        - `controlPlane.platform.gcp.type` and `compute.platform.gcp.type`: Specifies the node type as n4-standard-4.

        - `controlPlane.platform.gcp.osDisk.diskType` and `compute.platform.osDisk.diskType`: Specifies the node has the root disk backed by hyperdisk-balanced disk type. All nodes in the cluster should use the same disk type, either hyperdisks-balanced or pd-\*.

          > [!NOTE]
          > All nodes in the cluster must support hyperdisk-balanced volumes. Clusters with mixed nodes are not supported, for example N2 and N3 using hyperdisk-balanced disks.

    2.  After step 3 in "Incorporating the Cloud Credential Operator utility manifests", copy the following manifests into the manifests directory created by the installation program:

        - cluster_csi_driver.yaml - specifies opting out of the default storage class creation

        - storageclass.yaml - creates a hyperdisk-specific storage class

          <div class="formalpara">

          <div class="title">

          Example cluster CSI driver YAML file

          </div>

          ``` yaml
          apiVersion: operator.openshift.io/v1
          kind: "ClusterCSIDriver"
          metadata:
            name: "pd.csi.storage.gke.io"
          spec:
            logLevel: Normal
            managementState: Managed
            operatorLogLevel: Normal
            storageClassState: Unmanaged
          ```

          </div>

          `spec.storageClassState` specifies disabling creation of the default OpenShift Container Platform storage classes.

          <div class="formalpara">

          <div class="title">

          Example storage class YAML file

          </div>

          ``` yaml
          apiVersion: storage.k8s.io/v1
          kind: StorageClass
          metadata:
            name: hyperdisk-sc
            annotations:
              storageclass.kubernetes.io/is-default-class: "true"
          provisioner: pd.csi.storage.gke.io
          volumeBindingMode: WaitForFirstConsumer
          allowVolumeExpansion: true
          reclaimPolicy: Delete
          parameters:
            type: hyperdisk-balanced
            replication-type: none
            provisioned-throughput-on-create: "140Mi"
            provisioned-iops-on-create: "3000"
            storage-pools: projects/my-project/zones/us-east4-c/storagePools/pool-us-east4-c
          allowedTopologies:
          - matchLabelExpressions:
            - key: topology.kubernetes.io/zone
              values:
              - us-east4-c
          ...
          ```

          </div>

        - `metadata`.name: Specifies the name for your storage class. In this example, it is `hyperdisk-sc`.

        - `provisioner`: `pd.csi.storage.gke.io` specifies GCP CSI provisioner.

        - `parameters.type`: Specifies using hyperdisk-balanced disks. To specify high availability hyperdisk-balanced disk, set the value to `hyperdisk-balanced-high-availability`.

        - `parameters.provisioned-throughput-on-create`: Specifies the throughput value in MiBps using the "Mi" qualifier. For example, if your required throughput is 250 MiBps, specify "250Mi". If you do not specify a value, the capacity is based upon the disk type default.

        - `parameters.provisioned-iops-on-create`: Specifies the IOPS value without any qualifiers. For example, if you require 7,000 IOPS, specify "7000". If you do not specify a value, the capacity is based upon the disk type default.

        - `parameters.storage-pools`: If using storage pools, specifies a list of specific storage pools that you want to use in the format: projects/PROJECT_ID/zones/ZONE/storagePools/STORAGE_POOL_NAME.

        - `parameters.allowedTopologies`: If using storage pools, set `allowedTopologies` to restrict the topology of provisioned volumes to where the storage pool exists. In this example, `us-east4-c`.

3.  Create a persistent volume claim (PVC) that uses the hyperdisk-specific storage class using the following example YAML file:

    <div class="formalpara">

    <div class="title">

    Example PVC YAML file

    </div>

    ``` yaml
    apiVersion: v1
    kind: PersistentVolumeClaim
    metadata:
      name: my-pvc
    spec:
      storageClassName: hyperdisk-sc
      accessModes:
      - ReadWriteOnce
      resources:
        requests:
          storage: 2048Gi
    ```

    </div>

    - `spec.storageClassName`: The PVC references the storage pool-specific storage class. In this example, `hyperdisk-sc`.

    - `spec.resources.requests.storage`: Target storage capacity of the hyperdisk-balanced volume. In this example, `2048Gi`.

4.  Create a deployment that uses the PVC that you just created. Using a deployment helps ensure that your application has access to the persistent storage even after the pod restarts and rescheduling:

    1.  Ensure a node pool with the specified machine series is up and running before creating the deployment. Otherwise, the pod fails to schedule.

    2.  Use the following example YAML file to create the deployment:

        <div class="formalpara">

        <div class="title">

        Example deployment YAML file

        </div>

        ``` yaml
        apiVersion: apps/v1
        kind: Deployment
        metadata:
          name: postgres
        spec:
          selector:
            matchLabels:
              app: postgres
          template:
            metadata:
              labels:
                app: postgres
            spec:
              nodeSelector:
                cloud.google.com/machine-family: n4
              containers:
              - name: postgres
                image: postgres:14-alpine
                args: [ "sleep", "3600" ]
                volumeMounts:
                - name: sdk-volume
                  mountPath: /usr/share/data/
              volumes:
              - name: sdk-volume
                persistentVolumeClaim:
                  claimName: my-pvc
        ```

        </div>

        - `spec.template.spec.nodeSelector`: Specifies the machine family. In this example, it is `n4`.

        - `spec.template.spec.volumes.persistentVolumeClaim.claimName`: Specifies the name of the PVC created in the preceding step. In this example, it is `my-pfc`.

    3.  Confirm that the deployment was successfully created by running the following command:

        ``` terminal
        $ oc get deployment
        ```

        <div class="formalpara">

        <div class="title">

        Example output

        </div>

        ``` terminal
        NAME       READY   UP-TO-DATE   AVAILABLE   AGE
        postgres   0/1     1            0           42s
        ```

        </div>

        It might take a few minutes for hyperdisk instances to complete provisioning and display a READY status.

    4.  Confirm that PVC `my-pvc` has been successfully bound to a persistent volume (PV) by running the following command:

        ``` terminal
        $ oc get pvc my-pvc
        ```

        <div class="formalpara">

        <div class="title">

        Example output

        </div>

        ``` terminal
        NAME          STATUS   VOLUME                                     CAPACITY   ACCESS MODES   STORAGECLASS       VOLUMEATTRIBUTESCLASS  AGE
        my-pvc        Bound    pvc-1ff52479-4c81-4481-aa1d-b21c8f8860c6   2Ti        RWO            hyperdisk-sc       <unset>                2m24s
        ```

        </div>

    5.  Confirm the expected configuration of your hyperdisk-balanced disk:

        ``` terminal
        $ gcloud compute disks list
        ```

        <div class="formalpara">

        <div class="title">

        Example output

        </div>

        ``` terminal
        NAME                                        LOCATION        LOCATION_SCOPE  SIZE_GB  TYPE                STATUS
        instance-20240914-173145-boot               us-central1-a   zone            150      pd-standard         READY
        instance-20240914-173145-data-workspace     us-central1-a   zone            100      pd-balanced         READY
        c4a-rhel-vm                                 us-central1-a   zone            50       hyperdisk-balanced  READY
        ```

        </div>

        Where `c4a-rhel.vm` is a hyperdisk-balanced disk.

    6.  If using storage pools, check that the volume is provisioned as specified in your storage class and PVC by running the following command:

        ``` terminal
        $ gcloud compute storage-pools list-disks pool-us-east4-c --zone=us-east4-c
        ```

        <div class="formalpara">

        <div class="title">

        Example output

        </div>

        ``` terminal
        NAME                                      STATUS  PROVISIONED_IOPS  PROVISIONED_THROUGHPUT  SIZE_GB
        pvc-1ff52479-4c81-4481-aa1d-b21c8f8860c6  READY   3000              140                     2048
        ```

        </div>

</div>

<div>

<div class="title">

Additional resources

</div>

- [Create a Hyperdisk Storage Pool](https://cloud.google.com/compute/docs/disks/create-storage-pools#create-pool)

- [Installing a cluster on GCP with customizations](../../installing/installing_gcp/installing-gcp-customizations.md#installing-gcp-customizations)

</div>

# Creating a custom-encrypted persistent volume

To enhance data security beyond default encryption, create persistent volumes with customer-managed encryption keys (CMEK) that use Google Cloud Key Management Service for encryption control.

When you create a `PersistentVolumeClaim` object, OpenShift Container Platform provisions a new persistent volume (PV) and creates a `PersistentVolume` object. You can add a custom encryption key in Google Cloud Platform (GCP) to protect a PV in your cluster by encrypting the newly created PV.

For encryption, the newly attached PV that you create uses customer-managed encryption keys (CMEK) on a cluster by using a new or existing Google Cloud Key Management Service (KMS) key.

<div>

<div class="title">

Prerequisites

</div>

- You are logged in to a running OpenShift Container Platform cluster.

- You have created a Cloud KMS key ring and key version.

</div>

For more information about CMEK and Cloud KMS resources, see Google Cloud documentation "Using customer-managed encryption keys (CMEK)".

<div>

<div class="title">

Procedure

</div>

1.  Create a storage class with the Cloud KMS key. The following example enables dynamic provisioning of encrypted volumes:

    <div class="formalpara">

    <div class="title">

    Example

    </div>

    ``` yaml
    apiVersion: storage.k8s.io/v1
    kind: StorageClass
    metadata:
      name: csi-gce-pd-cmek
    provisioner: pd.csi.storage.gke.io
    volumeBindingMode: "WaitForFirstConsumer"
    allowVolumeExpansion: true
    parameters:
      type: pd-standard
      disk-encryption-kms-key: projects/<key-project-id>/locations/<location>/keyRings/<key-ring>/cryptoKeys/<key>
    ```

    </div>

    The `parameters.disk-encryption-kms-key` field must be the resource identifier for the key that will be used to encrypt new disks. Values are case-sensitive. For more information about providing key ID values, see Google Cloud documentation "Retrieving a resource’s ID" and "Getting a Cloud KMS resource ID".

    > [!NOTE]
    > You cannot add the `disk-encryption-kms-key` parameter to an existing storage class. However, you can delete the storage class and re-create it with the same name and a different set of parameters. If you do this, the provisioner of the existing class must be `pd.csi.storage.gke.io`.

2.  Deploy the storage class on your OpenShift Container Platform cluster by using the `oc` command:

    ``` terminal
    $ oc describe storageclass csi-gce-pd-cmek
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    Name:                  csi-gce-pd-cmek
    IsDefaultClass:        No
    Annotations:           None
    Provisioner:           pd.csi.storage.gke.io
    Parameters:            disk-encryption-kms-key=projects/key-project-id/locations/location/keyRings/ring-name/cryptoKeys/key-name,type=pd-standard
    AllowVolumeExpansion:  true
    MountOptions:          none
    ReclaimPolicy:         Delete
    VolumeBindingMode:     WaitForFirstConsumer
    Events:                none
    ```

    </div>

3.  Create a file named `pvc.yaml` that matches the name of your storage class object that you created in the previous step:

    ``` yaml
    kind: PersistentVolumeClaim
    apiVersion: v1
    metadata:
      name: podpvc
    spec:
      accessModes:
        - ReadWriteOnce
      storageClassName: csi-gce-pd-cmek
      resources:
        requests:
          storage: 6Gi
    ```

    > [!NOTE]
    > If you marked the new storage class as default, you can omit the `storageClassName` field.

4.  Apply the PVC on your cluster:

    ``` terminal
    $ oc apply -f pvc.yaml
    ```

5.  Get the status of your PVC and verify that it is created and bound to a newly provisioned PV:

    ``` terminal
    $ oc get pvc
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    NAME      STATUS    VOLUME                                     CAPACITY   ACCESS MODES   STORAGECLASS     AGE
    podpvc    Bound     pvc-e36abf50-84f3-11e8-8538-42010a800002   10Gi       RWO            csi-gce-pd-cmek  9s
    ```

    </div>

    > [!NOTE]
    > If your storage class has the `volumeBindingMode` field set to `WaitForFirstConsumer`, you must create a pod to use the PVC before you can verify it.

    Your CMEK-protected PV is now ready to use with your OpenShift Container Platform cluster.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Using customer-managed encryption keys (CMEK)](https://cloud.google.com/kubernetes-engine/docs/how-to/using-cmek)

- [Retrieving a resource’s ID](https://cloud.google.com/kms/docs/resource-hierarchy#retrieve_resource_id)

- [Getting a Cloud KMS resource ID](https://cloud.google.com/kms/docs/getting-resource-ids)

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

- [Additional Google Cloud configuration parameters](../../installing/installing_gcp/installation-config-parameters-gcp.md#installation-configuration-parameters-additional-gcp_installation-config-parameters-gcp)

</div>

# Volume snapshot class csi-gce-pd-vsc-images

By default, you cannot restore more than six volumes per snapshot per hour. So in Kubevirt environments, you normally cannot create more than six VMs per hour from a "golden image" (templates saved as snapshots).

For Google Cloud Platform (GCP) persistent disk (PD) storage CSI, there is a non-default `VolumeSnapshotClass`, named `csi-gce-pd-vsc-images`, that uses the `snapshot-type`: `images` parameter. When using KubeVirt, it allows you overcome the six VMs per hour restriction, so that you can create VMs from "golden images".

> [!NOTE]
> Snapshots using the images snapshot class are strictly limited to ReadWriteOnce (RWO) sources, but you can restore them to ReadWriteMany (RWX) hyperdisk-balanced disks.

For more information, see, "Volume snapshots CRD: VolumeSnapshotClass".

<div>

<div class="title">

Additional resources

</div>

- [Volume snapshots CRD: VolumeSnapshotClass](persistent-storage-csi-snapshots.md#volume-snapshot-crds)

</div>

# Additional resources

- [Persistent storage using GCE Persistent Disk](../persistent_storage/persistent-storage-gce.md#persistent-storage-using-gce)
