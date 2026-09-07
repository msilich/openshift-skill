<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

OpenShift Container Platform supports Amazon Elastic Block Store (EBS) volumes. You can provision your OpenShift Container Platform cluster with persistent storage by using Amazon EC2.

The Kubernetes persistent volume framework allows administrators to provision a cluster with persistent storage and gives users a way to request those resources without having any knowledge of the underlying infrastructure. You can dynamically provision Amazon EBS volumes. Persistent volumes are not bound to a single project or namespace; they can be shared across the OpenShift Container Platform cluster. Persistent volume claims are specific to a project or namespace and can be requested by users. You can define a KMS key to encrypt container-persistent volumes on AWS. By default, newly created clusters by using OpenShift Container Platform version 4.10 and later use gp3 storage and the AWS EBS CSI driver.

> [!IMPORTANT]
> High-availability of storage in the infrastructure is left to the underlying storage provider.

> [!IMPORTANT]
> OpenShift Container Platform 4.12 and later provides automatic migration for the AWS Block in-tree volume plugin to its equivalent CSI driver.
>
> CSI automatic migration should be seamless. Migration does not change how you use all existing API objects, such as persistent volumes, persistent volume claims, and storage classes. For more information about migration, see CSI automatic migration.

# About the EBS storage class

To enable dynamic provisioning of persistent volumes, create a storage class that defines storage characteristics and allows users to automatically provision volumes on-demand.

# Creating the persistent volume claim

You can create a persistent volume claim to dynamically provision and bind storage from a pre-configured storage class, so that your applications can consume persistent storage in OpenShift Container Platform.

<div>

<div class="title">

Prerequisites

</div>

- Storage must exist in the underlying infrastructure before it can be mounted as a volume in OpenShift Container Platform.

</div>

<div>

<div class="title">

Procedure

</div>

1.  In the OpenShift Container Platform web console, click **Storage** → **Persistent Volume Claims**.

2.  In the persistent volume claims overview, click **Create Persistent Volume Claim**.

3.  Define the required options on the page that is displayed.

    1.  Select the previously-created storage class from the drop-down menu.

    2.  Enter a unique name for the storage claim.

    3.  Select the access mode. This selection determines the read and write access for the storage claim.

    4.  Define the size of the storage claim.

4.  Click **Create** to create the persistent volume claim and generate a persistent volume.

</div>

# Volume format

You can use unformatted AWS volumes as persistent volumes, because OpenShift Container Platform automatically formats the device before mounting it to a container.

Before OpenShift Container Platform mounts the volume and passes it to a container, it checks that the volume contains a file system as specified by the `fsType` parameter in the persistent volume definition. If the device is not formatted with the file system, all data from the device is erased and the device is automatically formatted with the given file system.

# Maximum number of EBS volumes on a node

By default, you can attach a maximum of 39 EBS volumes attached to one node. This limit is consistent with the AWS volume limits. The volume limit depends on the instance type.

> [!IMPORTANT]
> As a cluster administrator, you must use either in-tree or Container Storage Interface (CSI) volumes and their respective storage classes, but never both volume types at the same time. The maximum attached EBS volume number is counted separately for in-tree and CSI volumes, which means you could have up to 39 EBS volumes of each type.

# Encrypting container persistent volumes on AWS with a KMS key

You can define a KMS key to encrypt container-persistent volumes on AWS if you have explicit compliance and security guidelines when deploying to AWS.

<div>

<div class="title">

Prerequisites

</div>

- Underlying infrastructure must contain storage.

- You must create a customer KMS key on AWS.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create a storage class:

    ``` yaml
    $ cat << EOF | oc create -f -
    apiVersion: storage.k8s.io/v1
    kind: StorageClass
    metadata:
      name: <storage-class-name>
    parameters:
      fsType: ext4
      encrypted: "true"
      kmsKeyId: keyvalue
    provisioner: ebs.csi.aws.com
    reclaimPolicy: Delete
    volumeBindingMode: WaitForFirstConsumer
    EOF
    ```

    where:

    `metadata.name`
    Specifies the name of the storage class.

    `parameters.fsType`
    Specifies the file system that is created on provisioned volumes.

    `parameters.kmsKeyId`
    Specifies the full Amazon Resource Name (ARN) of the key to use when encrypting the container-persistent volume. If you do not provide any key, but the `encrypted` field is set to `true`, then the default KMS key is used.

2.  Create a persistent volume claim (PVC) with the storage class specifying the KMS key:

    ``` yaml
    $ cat << EOF | oc create -f -
    apiVersion: v1
    kind: PersistentVolumeClaim
    metadata:
      name: mypvc
    spec:
      accessModes:
        - ReadWriteOnce
      volumeMode: Filesystem
      storageClassName: <storage-class-name>
      resources:
        requests:
          storage: 1Gi
    EOF
    ```

3.  Create workload containers to consume the PVC:

    ``` yaml
    $ cat << EOF | oc create -f -
    kind: Pod
    metadata:
      name: mypod
    spec:
      containers:
        - name: httpd
          image: quay.io/centos7/httpd-24-centos7
          ports:
            - containerPort: 80
          volumeMounts:
            - mountPath: /mnt/storage
              name: data
      volumes:
        - name: data
          persistentVolumeClaim:
            claimName: mypvc
    EOF
    ```

</div>

# Additional resources

- [Amazon EC2 documentation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html)

- [AWS EBS CSI driver](https://github.com/openshift/aws-ebs-csi-driver)

- [CSI automatic migration](../container_storage_interface/persistent-storage-csi-migration.md#persistent-storage-csi-migration)

- [AWS Elastic Block Store CSI Driver Operator](../container_storage_interface/persistent-storage-csi-ebs.md#persistent-storage-csi-ebs)
