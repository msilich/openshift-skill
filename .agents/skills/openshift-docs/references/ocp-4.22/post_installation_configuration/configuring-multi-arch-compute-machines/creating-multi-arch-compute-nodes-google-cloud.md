<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

To deploy a cluster on Google Cloud with multi-architecture compute machines, you must first create a single-architecture installer-provisioned cluster that uses the multi-architecture installer binary.

You can also migrate your current cluster with single-architecture compute machines to a cluster with multi-architecture compute machines. After creating a multi-architecture cluster, you can add nodes with different architectures to the cluster.

# Adding a multi-architecture compute machine set to your Google Cloud cluster

After creating a multi-architecture cluster, you can add nodes with different architectures.

You can add multi-architecture compute machines to a multi-architecture cluster in the following ways:

- Adding 64-bit x86 compute machines to a cluster that uses 64-bit ARM control plane machines and already includes 64-bit ARM compute machines. In this case, 64-bit x86 is considered the secondary architecture.

- Adding 64-bit ARM compute machines to a cluster that uses 64-bit x86 control plane machines and already includes 64-bit x86 compute machines. In this case, 64-bit ARM is considered the secondary architecture.

> [!NOTE]
> Before adding a secondary architecture node to your cluster, it is recommended to install the Multiarch Tuning Operator, and deploy a `ClusterPodPlacementConfig` custom resource. For more information, see "Managing workloads on multi-architecture clusters by using the Multiarch Tuning Operator".

<div>

<div class="title">

Prerequisites

</div>

- You installed the OpenShift CLI (`oc`).

- You used the installation program to create a 64-bit ARM or 64-bit x86 single-architecture cluster with the multi-architecture installer binary.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Log in to the OpenShift CLI (`oc`).

2.  Create a YAML file and add the configuration to create a compute machine set to control the 64-bit ARM or 64-bit x86 compute nodes in your cluster.

    <div class="formalpara">

    <div class="title">

    Example `MachineSet` object for a Google Cloud 64-bit ARM or 64-bit x86 compute node

    </div>

    ``` yaml
    apiVersion: machine.openshift.io/v1beta1
    kind: MachineSet
    metadata:
      labels:
        machine.openshift.io/cluster-api-cluster: <infrastructure_id>
      name: <infrastructure_id>-w-a
      namespace: openshift-machine-api
    spec:
      replicas: 1
      selector:
        matchLabels:
          machine.openshift.io/cluster-api-cluster: <infrastructure_id>
          machine.openshift.io/cluster-api-machineset: <infrastructure_id>-w-a
      template:
        metadata:
          creationTimestamp: null
          labels:
            machine.openshift.io/cluster-api-cluster: <infrastructure_id>
            machine.openshift.io/cluster-api-machine-role: <role>
            machine.openshift.io/cluster-api-machine-type: <role>
            machine.openshift.io/cluster-api-machineset: <infrastructure_id>-w-a
        spec:
          metadata:
            labels:
              node-role.kubernetes.io/<role>: ""
          providerSpec:
            value:
              apiVersion: gcpprovider.openshift.io/v1beta1
              canIPForward: false
              credentialsSecret:
                name: gcp-cloud-credentials
              deletionProtection: false
              disks:
              - autoDelete: true
                boot: true
                image: <path_to_image>
                labels: null
                sizeGb: 128
                type: pd-ssd
              gcpMetadata:
              - key: <custom_metadata_key>
                value: <custom_metadata_value>
              kind: GCPMachineProviderSpec
              machineType: n1-standard-4
              metadata:
                creationTimestamp: null
              networkInterfaces:
              - network: <infrastructure_id>-network
                subnetwork: <infrastructure_id>-worker-subnet
              projectID: <project_name>
              region: us-central1
              serviceAccounts:
              - email: <infrastructure_id>-w@<project_name>.iam.gserviceaccount.com
                scopes:
                - https://www.googleapis.com/auth/cloud-platform
              tags:
                - <infrastructure_id>-worker
              userDataSecret:
                name: worker-user-data
              zone: us-central1-a
    ```

    </div>

    where:

    `<infrastructure_id>`
    Specifies the infrastructure ID that is based on the cluster ID that you set when you provisioned the cluster. You can obtain the infrastructure ID by running the following command:

    ``` terminal
    $ oc get -o jsonpath='{.status.infrastructureName}{"\n"}' infrastructure cluster
    ```

    `<role>`
    Specifies the role node label to add.

    `<path_to_image>`
    Specifies the path to the image that is used in current compute machine sets. You need the project and image name for your path to image.

    To access the project and image name, run the following command:

    ``` terminal
    $ oc get configmap/coreos-bootimages \
      -n openshift-machine-config-operator \
      -o jsonpath='{.data.stream}' | jq \
      -r '.architectures.aarch64.images.gcp'
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
      "gcp": {
        "release": "415.92.202309142014-0",
        "project": "rhcos-cloud",
        "name": "rhcos-415-92-202309142014-0-gcp-aarch64"
      }
    ```

    </div>

    Use the `project` and `name` parameters from the output to create the path to image field in your machine set. The path to the image should follow the following format:

    ``` terminal
    $ projects/<project>/global/images/<image_name>
    ```

    `gcpMetadata`
    Optional parameter. Specifies custom metadata in the form of a `key:value` pair. For example use cases, see "Setting custom metadata".

    `machineType`
    Specifies a machine type that aligns with the CPU architecture of the chosen OS image. For more information, see "Tested instance types for Google Cloud on 64-bit ARM infrastructures".

    `projectID`
    Specifies the name of the Google Cloud project that you use for your cluster.

    `region`
    Specifies the region. For example, `us-central1`. Ensure that the zone you select has machines with the required architecture.

3.  Create the compute machine set by running the following command:

    ``` terminal
    $ oc create -f <file_name>
    ```

    - Replace `<file_name>` with the name of the YAML file with compute machine set configuration. For example: `gcp-arm64-machine-set-0.yaml`, or `gcp-amd64-machine-set-0.yaml`.

</div>

<div>

<div class="title">

Verification

</div>

1.  Verify that the new machines are running by running the following command:

    ``` terminal
    $ oc get machineset -n openshift-machine-api
    ```

    The output must include the machine set that you created.

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    NAME                                                DESIRED  CURRENT  READY  AVAILABLE  AGE
    <infrastructure_id>-gcp-machine-set-0                   2        2      2          2  10m
    ```

    </div>

2.  You can check if the nodes are ready and schedulable by running the following command:

    ``` terminal
    $ oc get nodes
    ```

</div>

# Additional resources

- [Migrating to a cluster with multi-architecture compute machines](../../updating/updating_a_cluster/migrating-to-multi-payload.md#migrating-to-multi-payload)

- [Managing workloads on multi-architecture clusters by using the Multiarch Tuning Operator](multiarch-tuning-operator.md#multiarch-tuning-operator)

- [Tested instance types for Google Cloud on 64-bit ARM infrastructures](../../installing/installing_gcp/installing-gcp-customizations.md#installation-gcp-tested-machine-types-arm_installing-gcp-customizations)

- [Setting custom metadata](https://cloud.google.com/compute/docs/metadata/setting-custom-metadata)
