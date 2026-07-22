<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Create compute machine sets in your OpenShift Container Platform cluster on IBM Power® Virtual Server to perform specific tasks. For example, you might create infrastructure machine sets and related machines so that you can move supporting workloads to the new machines. Moving supporting workloads to dedicated machines helps ensure that your cluster resources are allocated efficiently.

> [!IMPORTANT]
> You can use the advanced machine management and scaling capabilities only in clusters where the Machine API is operational. Clusters with user-provisioned infrastructure require additional validation and configuration to use the Machine API.
>
> Clusters with the infrastructure platform type `none` cannot use the Machine API. This limitation applies even if the compute machines that are attached to the cluster are installed on a platform that supports the feature. This parameter cannot be changed after installation.
>
> To view the platform type for your cluster, run the following command:
>
> ``` terminal
> $ oc get infrastructure cluster -o jsonpath='{.status.platform}'
> ```

# Sample YAML for a compute machine set custom resource on IBM Power Virtual Server

You can use the sample YAML file to help automate provisioning and to ensure scaling and scheduling work, as required. The sample YAML file defines a compute machine set that runs in a specified IBM Power® Virtual Server zone in a region and creates nodes that are labeled with `node-role.kubernetes.io/<role>: ""`.

In the sample, `<infrastructure_id>` is the infrastructure ID label that is based on the cluster ID that you set when you provisioned the cluster, and `<role>` is the node label to add.

``` yaml
apiVersion: machine.openshift.io/v1beta1
kind: MachineSet
metadata:
  labels:
    machine.openshift.io/cluster-api-cluster: <infrastructure_id>
    machine.openshift.io/cluster-api-machine-role: <role>
    machine.openshift.io/cluster-api-machine-type: <role>
  name: <infrastructure_id>-<role>-<region>
  namespace: openshift-machine-api
spec:
  replicas: 1
  selector:
    matchLabels:
      machine.openshift.io/cluster-api-cluster: <infrastructure_id>
      machine.openshift.io/cluster-api-machineset: <infrastructure_id>-<role>-<region>
  template:
    metadata:
      labels:
        machine.openshift.io/cluster-api-cluster: <infrastructure_id>
        machine.openshift.io/cluster-api-machine-role: <role>
        machine.openshift.io/cluster-api-machine-type: <role>
        machine.openshift.io/cluster-api-machineset: <infrastructure_id>-<role>-<region>
    spec:
      metadata:
        labels:
          node-role.kubernetes.io/<role>: ""
      providerSpec:
        value:
          apiVersion: machine.openshift.io/v1
          credentialsSecret:
            name: powervs-credentials
          image:
            name: rhcos-<infrastructure_id>
            type: Name
          keyPairName: <infrastructure_id>-key
          kind: PowerVSMachineProviderConfig
          memoryGiB: 32
          network:
            regex: ^DHCPSERVER[0-9a-z]{32}_Private$
            type: RegEx
          processorType: Shared
          processors: "0.5"
          serviceInstance:
            id: <ibm_power_vs_service_instance_id>
            type: ID
          systemType: s922
          userDataSecret:
            name: <role>-user-data
```

where:

`<infrastructure_id>`
Specifies the infrastructure ID that is based on the cluster ID that you set when you provisioned the cluster. If you have the OpenShift CLI installed, you can obtain the infrastructure ID by running the following command:

``` terminal
$ oc get -o jsonpath='{.status.infrastructureName}{"\n"}' infrastructure cluster
```

`<role>`
Specifies the node label to add.

`<infrastructure_id>-<role>-<region>`
Specifies the infrastructure ID, node label, and region.

`rhcos-<infrastructure_id>`
Specifies the custom Red Hat Enterprise Linux CoreOS (RHCOS) image that was used for cluster installation.

`<ibm_power_vs_service_instance_id>`
Specifies the infrastructure ID within your region to place machines on.

# Creating a compute machine set

To dynamically manage machine compute resources, you can create your own compute machine sets in addition to the compute machine sets created by the installation program. Use the OpenShift Container Platform CLI to automate node provisioning.

<div>

<div class="title">

Prerequisites

</div>

- Deploy an OpenShift Container Platform cluster.

- Install the OpenShift CLI (`oc`).

- Log in to `oc` as a user with `cluster-admin` permission.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create a new YAML file that contains the compute machine set custom resource (CR) sample and is named `<file_name>.yaml`.

    Ensure that you set the `<clusterID>` and `<role>` parameter values.

2.  Optional: If you are not sure which value to set for a specific field, you can check an existing compute machine set from your cluster.

    1.  To list the compute machine sets in your cluster, run the following command:

        ``` terminal
        $ oc get machinesets -n openshift-machine-api
        ```

        The following is example output:

        ``` terminal
        NAME                                DESIRED   CURRENT   READY   AVAILABLE   AGE
        agl030519-vplxk-worker-us-east-1a   1         1         1       1           55m
        agl030519-vplxk-worker-us-east-1b   1         1         1       1           55m
        agl030519-vplxk-worker-us-east-1c   1         1         1       1           55m
        agl030519-vplxk-worker-us-east-1d   0         0                             55m
        agl030519-vplxk-worker-us-east-1e   0         0                             55m
        agl030519-vplxk-worker-us-east-1f   0         0                             55m
        ```

    2.  To view values of a specific compute machine set custom resource (CR), run the following command:

        ``` terminal
        $ oc get machineset <machineset_name> \
          -n openshift-machine-api -o yaml
        ```

        The following is example output:

        ``` yaml
        apiVersion: machine.openshift.io/v1beta1
        kind: MachineSet
        metadata:
          labels:
            machine.openshift.io/cluster-api-cluster: <infrastructure_id>
          name: <infrastructure_id>-<role>
          namespace: openshift-machine-api
        spec:
          replicas: 1
          selector:
            matchLabels:
              machine.openshift.io/cluster-api-cluster: <infrastructure_id>
              machine.openshift.io/cluster-api-machineset: <infrastructure_id>-<role>
          template:
            metadata:
              labels:
                machine.openshift.io/cluster-api-cluster: <infrastructure_id>
                machine.openshift.io/cluster-api-machine-role: <role>
                machine.openshift.io/cluster-api-machine-type: <role>
                machine.openshift.io/cluster-api-machineset: <infrastructure_id>-<role>
            spec:
              providerSpec:
                ...
        ```

        where:

        `metadata.labels.machine.openshift.io/cluster-api-cluster`
        Specifies the cluster infrastructure ID.

        `metadata.labels.name`
        Specifies a default node label.

        > [!NOTE]
        > For clusters that have user-provisioned infrastructure, a compute machine set can only create `worker` and `infra` type machines.

        `spec.template.metadata.spec.providerSpec`
        Specifies the values of the compute machine set CR. The values are platform-specific. For more information about `<providerSpec>` parameters in the CR, see the sample compute machine set CR configuration for your provider.

3.  Create a `MachineSet` CR by running the following command:

    ``` terminal
    $ oc create -f <file_name>.yaml
    ```

</div>

<div>

<div class="title">

Verification

</div>

- View the list of compute machine sets by running the following command:

  ``` terminal
  $ oc get machineset -n openshift-machine-api
  ```

  The following is example output:

  ``` terminal
  NAME                                DESIRED   CURRENT   READY   AVAILABLE   AGE
  agl030519-vplxk-infra-us-east-1a    1         1         1       1           11m
  agl030519-vplxk-worker-us-east-1a   1         1         1       1           55m
  agl030519-vplxk-worker-us-east-1b   1         1         1       1           55m
  agl030519-vplxk-worker-us-east-1c   1         1         1       1           55m
  agl030519-vplxk-worker-us-east-1d   0         0                             55m
  agl030519-vplxk-worker-us-east-1e   0         0                             55m
  agl030519-vplxk-worker-us-east-1f   0         0                             55m
  ```

  When the new compute machine set is available, the `DESIRED` and `CURRENT` values match. If the compute machine set is not available, wait a few minutes and run the command again.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Cluster autoscaler resource definition](../applying-autoscaling.md#cluster-autoscaler-cr_applying-autoscaling)

</div>
