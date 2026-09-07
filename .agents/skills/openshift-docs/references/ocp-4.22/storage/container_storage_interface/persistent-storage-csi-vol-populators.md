<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Volume populators enable the automatic pre-loading of data into a volume during dynamic provisioning, instead of provisioning an empty volume.

# Volume populators overview

With volume populators, using the `dataSourceRef` field, you can prepopulate volumes from a Custom Resource Definition (CRD) instead of only persistent volume claims (PVCs) and snapshots.

In OpenShift Container Platform versions 4.12 through 4.19, the `dataSource` field in a PVC spec provides volume populator capability. However, it is limited to using only PVCs and snapshots as the data source for populating volumes.

Starting with OpenShift Container Platform version 4.20, the `dataSourceRef` field is used instead. With the `dataSourceRef` field, you can use any appropriate custom resource (CR) as the data source to prepopulate a new volume.

> [!NOTE]
> Volume populator functionality using the `dataSource` field is likely to be deprecated in future versions. If you have created any volume populators using this field, consider re-creating your volume populators to use the `dataSourceRef` field to avoid future issues.

Volume population is enabled by default and OpenShift Container Platform includes the installed `volume-data-source-validator` controller. However, OpenShift Container Platform does not ship with any volume populators.

# Volume populators creation

To implement custom volume prepopulation behavior, create a volume populator by defining a custom resource definition (CRD) and then using it to create prepopulated volumes.

## Creating CRDs for volume populators

To enable custom volume prepopulation, create a Custom Resource Definition (CRD) that defines a data source that users can instantiate to populate persistent volume claims (PVCs).

The following procedure explains how to create an example "hello, world" CRD for a volume populator.

Users can then create instances of this CRD to populate PVCs.

<div>

<div class="title">

Prerequisites

</div>

- Access to the OpenShift Container Platform web console.

- Access to the cluster with cluster-admin privileges.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create a namespace for the logical grouping and operation of the populator, and related resources, using the following example YAML file:

    <div class="formalpara">

    <div class="title">

    Example namespace YAML file

    </div>

    ``` yaml
    apiVersion: v1
    kind: Namespace
    metadata:
      name: hello
    ```

    </div>

2.  Create a CRD for your data source using the following example YAML file:

    <div class="formalpara">

    <div class="title">

    Example CRD YAML file

    </div>

    ``` yaml
    apiVersion: apiextensions.k8s.io/v1
    kind: CustomResourceDefinition
    metadata:
      name: hellos.hello.example.com
    spec:
      group: hello.example.com
      names:
        kind: Hello
        listKind: HelloList
        plural: hellos
        singular: hello
      scope: Namespaced
      versions:
      - name: v1alpha1
        schema:
          openAPIV3Schema:
            description: Hello is a specification for a Hello resource
            properties:
              apiVersion:
                description: 'APIVersion defines the versioned schema of this representation
                  of an object. Servers should convert recognized schemas to the latest
                  internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources'
                type: string
              kind:
                description: 'Kind is a string value representing the REST resource this
                  object represents. Servers may infer this from the endpoint the client
                  submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds'
                type: string
              spec:
                description: HelloSpec is the spec for a Hello resource
                properties:
                  fileContents:
                    type: string
                  fileName:
                    type: string
                required:
                - fileContents
                - fileName
                type: object
            required:
            - spec
            type: object
        served: true
        storage: true
    ```

    </div>

3.  Deploy the controller by creating a `ServiceAccount`, `ClusterRole`, `ClusterRoleBindering`, and `Deployment` to run the logic that implements the population:

    1.  Create a service account for the populator using the following example YAML file:

        <div class="formalpara">

        <div class="title">

        Example service account YAML file

        </div>

        ``` yaml
        apiVersion: v1
        kind: ServiceAccount
        metadata:
          name: hello-account
          namespace: hello
        ```

        </div>

        Where `metadata.namespace` references the namespace that you created earlier.

    2.  Create a cluster role for the populator using the following example YAML file:

        <div class="formalpara">

        <div class="title">

        Example cluster role YAML file

        </div>

        ``` yaml
        kind: ClusterRole
        apiVersion: rbac.authorization.k8s.io/v1
        metadata:
          name: hello-role
        rules:
          - apiGroups: [hello.example.com]
            resources: [hellos]
            verbs: [get, list, watch]
        ```

        </div>

    3.  Create a cluster role binding using the following example YAML file:

        <div class="formalpara">

        <div class="title">

        Example cluster role binding YAML file

        </div>

        ``` yaml
        kind: ClusterRoleBinding
        apiVersion: rbac.authorization.k8s.io/v1
        metadata:
          name: hello-binding
        subjects:
          - kind: ServiceAccount
            name: hello-account
            namespace: hello
        roleRef:
          kind: ClusterRole
          name: hello-role
          apiGroup: rbac.authorization.k8s.io
        ```

        </div>

        - `metadata.name`: Specifies the role binding name.

        - `subjects.name`: References the name of the service account that you created earlier.

        - `subjects.namespace`: References the name of the namespace for the service account that you created earlier.

        - `roleRef.name`: References the cluster role you created earlier.

    4.  Create a Deployment for the populator using the following example YAML file:

        <div class="formalpara">

        <div class="title">

        Example deployment YAML file

        </div>

        ``` yaml
        kind: Deployment
        apiVersion: apps/v1
        metadata:
          name: hello-populator
          namespace: hello
        spec:
          selector:
            matchLabels:
              app: hello
          template:
            metadata:
              labels:
                app: hello
            spec:
              serviceAccount: hello-account
              containers:
                - name: hello
                  image: registry.k8s.io/sig-storage/hello-populator:v1.0.1
                  imagePullPolicy: IfNotPresent
                  args:
                    - --mode=controller
                    - --image-name=registry.k8s.io/sig-storage/hello-populator:v1.0.1
                    - --http-endpoint=:8080
                  ports:
                    - containerPort: 8080
                      name: http-endpoint
                      protocol: TCP
        ```

        </div>

        - `metadata.namespace`: References the namespace that you created earlier.

        - `spec.template.spec.serviceAccount`: References the service account that you created earlier.

4.  Create a volume populator to register the `kind:Hello` resource as a valid data source for the volume using the following example YAML file:

    <div class="formalpara">

    <div class="title">

    Example volume populator YAML file

    </div>

    ``` yaml
    kind: VolumePopulator
    apiVersion: populator.storage.k8s.io/v1beta1
    metadata:
      name: hello-populator
    sourceKind:
      group: hello.example.com
      kind: Hello
    ```

    </div>

    The `metadata.name` field specifies the Volume populator name.

    PVCs that use an unregistered populator generate an event: "The datasource for this PVC does not match any registered VolumePopulator", indicating that the PVC might not be provisioned because you are using an unknown (unregistered) populator.

</div>

<div>

<div class="title">

Next steps

</div>

- You can now create CR instances of this CRD to populate PVCs

  For more information, see "Creating prepopulated volumes using volume populators".

</div>

## Creating prepopulated volumes using volume populators

To create volumes that are automatically filled with data when provisioned, define a Custom Resource Definition (CRD) as a data source and reference it when creating the persistent volume claim (PVC).

The following procedure explains how to create a prepopulated PVC using the example `hellos.hello.example.com` CRD created previously.

In this example, rather than using an actual data source, you are creating a file called "example.txt" that contains the string "Hello, world!" in the root directory of the volume. For a real-world implementation, you need to create your own volume populator.

<div>

<div class="title">

Prerequisites

</div>

- You are logged in to a running OpenShift Container Platform cluster.

- There is an existing CRD for volume populators.

- OpenShift Container Platform does not ship with any volume populators. You **must** create your own volume populator.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create a Custom Resource (CR) instance of the `Hello` CRD with the text "Hello, World!" passed in as `fileContents` parameter by running the following command:

    ``` terminal
    $ oc apply -f  - <<EOF
    apiVersion: hello.example.com/v1alpha1
    kind: Hello
    metadata:
      name: example-hello
    spec:
      fileName: example.txt
      fileContents: Hello, world!
    EOF
    ```

2.  Create a PVC that references the Hello CR similar to the following example file:

    <div class="formalpara">

    <div class="title">

    Example PVC YAML file

    </div>

    ``` yaml
    apiVersion: v1
    kind: PersistentVolumeClaim
    metadata:
      name: example-pvc
    spec:
      accessModes:
      - ReadWriteOnce
      resources:
        requests:
          storage: 10Mi
      dataSourceRef:
        apiGroup: hello.example.com
        kind: Hello
        name: example-hello
      volumeMode: Filesystem
    ```

    </div>

    - `spec.dataSourceRef`: Specifies the data source for the PVC.

    - `spec.dataSourceRef.name`: Specifies the name of the CR that you are using as the data source. In this example, it is 'example-hello'.

</div>

<div>

<div class="title">

Verification

</div>

1.  After a few minutes, ensure that the PVC is created and in the `Bound` status by running the following command:

    ``` terminal
    $ oc get pvc example-pvc -n hello
    ```

    In this example, the name of the PVC is `example-pvc`.

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    NAME          STATUS    VOLUME        CAPACITY   ACCESS MODES   STORAGECLASS   VOLUMEATTRIBUTESCLASS   AGE
    example-pvc   Bound     my-pv         10Mi       ReadWriteOnce  gp3-csi        <unset>                 14s
    ```

    </div>

2.  Create a job that reads from the PVC to verify that the data source information was applied using the following example file:

    <div class="formalpara">

    <div class="title">

    Example job YAML file

    </div>

    ``` yaml
    apiVersion: batch/v1
    kind: Job
    metadata:
      name: example-job
    spec:
      template:
        spec:
          containers:
            - name: example-container
              image: busybox:latest
              command:
                - cat
                - /mnt/example.txt
              volumeMounts:
                - name: vol
                  mountPath: /mnt
          restartPolicy: Never
          volumes:
            - name: vol
              persistentVolumeClaim:
                claimName: example-pvc
    ```

    </div>

    - `spec.template.spec.containers.command`: Specifies the location and name of the file with the "Hello, world!" text. In this example, the location is "/mnt/example.txt".

    - `spec.template.spec.volumes.persistentVolumeClaim`: Specifies the name of the PVC you created in Step 2. In this example, it is `example-pvc`.

3.  Start the job by running the following command:

    ``` terminal
    $ oc run example-job --image=busybox --command -- sleep 30 --restart=OnFailure
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    pod/example-job created
    ```

    </div>

4.  Wait for the job, and all of its dependencies, to finish by running the following command:

    ``` terminal
    $ oc wait --for=condition=Complete pod/example-job
    ```

5.  Verify the contents collected by the job by running the following command:

    ``` terminal
    $ oc logs job/example-job
    ```

    <div class="formalpara">

    <div class="title">

    Example expected output

    </div>

    ``` terminal
    Hello, world!
    ```

    </div>

</div>

# Uninstalling volume populators

To remove custom volume prepopulation functionality, delete all volume populator resources in reverse order of creation.

<div>

<div class="title">

Prerequisites

</div>

- Access to the OpenShift Container Platform web console.

- Access to the cluster with cluster-admin privileges.

</div>

<div>

<div class="title">

Procedure

</div>

- To uninstall volume populators, delete in reverse order all objects installed in the following procedures:

  1.  "Creating prepopulated volumes using volume populators".

  2.  "Creating CRDs for volume populators".

      Be sure to remove the `VolumePopulator` instance.

</div>
