<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

To deploy a cluster on Amazon Web Services (AWS) with multi-architecture compute machines, you must first create a single-architecture installer-provisioned cluster that uses the multi-architecture installer binary.

You can also migrate your current cluster with single-architecture compute machines to a cluster with multi-architecture compute machines. After creating a multi-architecture cluster, you can add nodes with different architectures to the cluster.

# Adding a multi-architecture compute machine set to your AWS cluster

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

    Example `MachineSet` object for an AWS 64-bit ARM or x86 compute node

    </div>

    ``` yaml
    apiVersion: machine.openshift.io/v1beta1
    kind: MachineSet
    metadata:
      labels:
        machine.openshift.io/cluster-api-cluster: <infrastructure_id>
      name: <infrastructure_id>-aws-machine-set-0
      namespace: openshift-machine-api
    spec:
      replicas: 1
      selector:
        matchLabels:
          machine.openshift.io/cluster-api-cluster: <infrastructure_id>
          machine.openshift.io/cluster-api-machineset: <infrastructure_id>-<role>-<zone>
      template:
        metadata:
          labels:
            machine.openshift.io/cluster-api-cluster: <infrastructure_id>
            machine.openshift.io/cluster-api-machine-role: <role>
            machine.openshift.io/cluster-api-machine-type: <role>
            machine.openshift.io/cluster-api-machineset: <infrastructure_id>-<role>-<zone>
        spec:
          metadata:
            labels:
              node-role.kubernetes.io/<role>: ""
          providerSpec:
            value:
              ami:
                id: ami-02a574449d4f4d280
              apiVersion: awsproviderconfig.openshift.io/v1beta1
              blockDevices:
                - ebs:
                    iops: 0
                    volumeSize: 120
                    volumeType: gp2
              credentialsSecret:
                name: aws-cloud-credentials
              deviceIndex: 0
              iamInstanceProfile:
                id: <infrastructure_id>-worker-profile
              instanceType: m6g.xlarge
              kind: AWSMachineProviderConfig
              placement:
                availabilityZone: us-east-1a
                region: <region>
              securityGroups:
                - filters:
                    - name: tag:Name
                      values:
                        - <infrastructure_id>-node
              subnet:
                filters:
                  - name: tag:Name
                    values:
                      - <infrastructure_id>-subnet-private-<zone>
              tags:
                - name: kubernetes.io/cluster/<infrastructure_id>
                  value: owned
                - name: <custom_tag_name>
                  value: <custom_tag_value>
              userDataSecret:
                name: worker-user-data
    ```

    </div>

    where:

    `<infrastructure_id>`
    Specifies the infrastructure ID that is based on the cluster ID that you set when you provisioned the cluster. If you have the OpenShift CLI (`oc`) installed, you can obtain the infrastructure ID by running the following command:

    ``` terminal
    $ oc get -o jsonpath="{.status.infrastructureName}{'\n'}" infrastructure cluster
    ```

    `<role>-<zone>`
    Specifies the infrastructure ID, role node label, and zone.

    `<role>`
    Specifies the role node label to add.

    `ami.id`
    Specifies a Red Hat Enterprise Linux CoreOS (RHCOS) Amazon Machine Image (AMI) for your AWS region for the nodes. The RHCOS AMI must be compatible with the machine architecture.

    ``` terminal
    $ oc get configmap/coreos-bootimages \
          -n openshift-machine-config-operator \
          -o jsonpath='{.data.stream}' | jq \
          -r '.architectures.<arch>.images.aws.regions."<region>".image'
    ```

    `instanceType`
    Specifies a machine type that aligns with the CPU architecture of the chosen AMI. For more information, see "Tested instance types for AWS 64-bit ARM".

    `availabilityZone`
    Specifies the zone. For example, `us-east-1a`. Ensure that the zone you select has machines with the required architecture.

    `region`
    Specifies the region. For example, `us-east-1`. Ensure that the zone you select has machines with the required architecture.

3.  Create the compute machine set by running the following command:

    ``` terminal
    $ oc create -f <file_name>
    ```

    - Replace `<file_name>` with the name of the YAML file with compute machine set configuration. For example: `aws-arm64-machine-set-0.yaml`, or `aws-amd64-machine-set-0.yaml`.

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
    <infrastructure_id>-aws-machine-set-0                   2        2      2          2  10m
    ```

    </div>

2.  You can check if the nodes are ready and schedulable by running the following command:

    ``` terminal
    $ oc get nodes
    ```

</div>

# Additional resources

- [Installing a cluster on AWS with customizations](../../installing/installing_aws/ipi/installing-aws-customizations.md#installing-aws-customizations)

- [Migrating to a cluster with multi-architecture compute machines](../../updating/updating_a_cluster/migrating-to-multi-payload.md#migrating-to-multi-payload)

- [Tested instance types for AWS 64-bit ARM](../../installing/installing_aws/ipi/installing-aws-customizations.md#installation-aws-arm-tested-machine-types_installing-aws-customizations)

- [Managing workloads on multi-architecture clusters by using the Multiarch Tuning Operator](multiarch-tuning-operator.md#multiarch-tuning-operator)
