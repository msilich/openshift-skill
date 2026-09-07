<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

OpenShift Container Platform supports OpenStack Cinder volumes. You can provision your OpenShift Container Platform cluster with persistent storage using OpenStack Cinder. Some familiarity with Kubernetes and OpenStack is assumed.

Persistent volumes are not bound to a single project or namespace; they can be shared across the OpenShift Container Platform cluster. Persistent volume claims are specific to a project or namespace and can be requested by users.

> [!IMPORTANT]
> OpenShift Container Platform 4.11 and later provides automatic migration for the Cinder in-tree volume plugin to its equivalent CSI driver.
>
> CSI automatic migration should be seamless. Migration does not change how you use all existing API objects, such as persistent volumes, persistent volume claims, and storage classes. For more information about migration, see "CSI automatic migration".

<div>

<div class="title">

Additional resources

</div>

- [CSI automatic migration](../container_storage_interface/persistent-storage-csi-migration.md#persistent-storage-csi-migration)

- [OpenStack Cinder](https://access.redhat.com/documentation/en-us/red_hat_openstack_platform/8/html-single/architecture_guide/index#comp-cinder)

</div>

# Manual provisioning with Cinder

Storage must exist in the underlying infrastructure before it can be mounted as a volume in OpenShift Container Platform.

Manual provisioning requires that OpenShift Container Platform is configured for Red Hat OpenStack Platform (RHOSP) and that you have the Cinder volume ID.

## Creating the persistent volume

You can create a persistent volume (PV) that provisions storage from an Red Hat OpenStack Platform (RHOSP) Cinder volume for use with OpenShift Container Platform.

<div>

<div class="title">

Prerequisites

</div>

- You have defined your PV in an object definition before creating it in OpenShift Container Platform.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Save your object definition to a file.

    <div class="formalpara">

    <div class="title">

    cinder-persistentvolume.yaml

    </div>

    ``` yaml
    apiVersion: "v1"
    kind: "PersistentVolume"
    metadata:
      name: "pv0001"
    spec:
      capacity:
        storage: "5Gi"
      accessModes:
        - "ReadWriteOnce"
      cinder:
        fsType: "ext3"
        volumeID: "f37a03aa-6212-4c62-a805-9ce139fab180"
    ```

    </div>

    where:

    `metadata.name`
    Specifies the name of the volume that is used by persistent volume claims or pods.

    `spec.capacity.storage`
    Specifies the amount of storage allocated to this volume.

    `spec.cinder`
    Indicates `cinder` for Red Hat OpenStack Platform (RHOSP) Cinder volumes.

    `spec.cinder.fsType`
    Specifies the file system that is created when the volume is mounted for the first time.

    `spec.cinder.volumeID`
    Specifies the Cinder volume to use.

    > [!IMPORTANT]
    > Do not change the `fstype` parameter value after the volume is formatted and provisioned. Changing this value can result in data loss and pod failure.

2.  Create the object definition file you saved in the previous step.

    ``` terminal
    $ oc create -f cinder-persistentvolume.yaml
    ```

</div>

## Persistent volume formatting

You can use unformatted Cinder volumes as PVs because OpenShift Container Platform formats them before the first use.

Before OpenShift Container Platform mounts the volume and passes it to a container, the system checks that it contains a file system as specified by the `fsType` parameter in the PV definition. If the device is not formatted with the file system, all data from the device is erased and the device is automatically formatted with the given file system.

## Configuring Cinder volume security

If you use Cinder PVs in your application, configure security for their deployment resources.

<div>

<div class="title">

Prerequisites

</div>

- An SCC must be created that uses the appropriate `fsGroup` strategy.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create a service account and add it to the SCC:

    ``` terminal
    $ oc create serviceaccount <service_account>
    ```

    ``` terminal
    $ oc adm policy add-scc-to-user <new_scc> -z <service_account> -n <project>
    ```

2.  In your application’s deployment resource, provide the service account name and `securityContext`:

    ``` yaml
    apiVersion: v1
    kind: ReplicationController
    metadata:
      name: frontend-1
    spec:
      replicas: 1
      selector:
        name: frontend
      template:
        metadata:
          labels:
            name: frontend
        spec:
          containers:
          - image: openshift/hello-openshift
            name: helloworld
            ports:
            - containerPort: 8080
              protocol: TCP
          restartPolicy: Always
          serviceAccountName: <service_account>
          securityContext:
            fsGroup: 7777
    ```

    where:

    `spec.replicas`
    Specifies the number of copies of the pod to run.

    `spec.selector`
    Specifies the label selector of the pod to run.

    `spec.template`
    Specifies a template for the pod that the controller creates.

    `spec.template.metadata.labels`
    Specifies the labels on the pod. They must include labels from the label selector.

    `spec.template.metadata.labels.name`
    Specifies the maximum name length after expanding any parameters is 63 characters.

    `spec.template.spec.serviceAccountName`
    Specifies the service account you created.

    `spec.template.spec.securityContext.fsGroup`
    Specifies an `fsGroup` for the pods.

</div>
