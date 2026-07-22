<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

You can use a `MachineSet` custom resource (CR) to add a Windows compute node to your Nutanix cluster, where you can run Windows container workloads.

For example, you might create infrastructure Windows machine sets and related machines so that you can move supporting Windows workloads to the new Windows machines. For more information about machine sets, see "Overview of machine management" in the *Additional resources* section.

# Prerequisites

- You installed the Windows Machine Config Operator (WMCO) using Operator Lifecycle Manager (OLM).

- You are using a supported Windows Server as the operating system image.

- You added a new DNS entry for the internal API server URL, `api-int.<cluster_name>.<base_domain>`, that points to the external API server URL, `api.<cluster_name>.<base_domain>`. This can be a CNAME or an additional A record.

# Sample YAML for a Windows MachineSet object on Nutanix

You can define a Windows `MachineSet` object running on Nutanix by creating a YAML file similar to the following example that the Windows Machine Config Operator (WMCO) can react upon.

``` yaml
apiVersion: machine.openshift.io/v1beta1
kind: MachineSet
metadata:
  labels:
    machine.openshift.io/cluster-api-cluster: <infrastructure_id>
  name: <infrastructure_id>-windows-worker-<zone>
  namespace: openshift-machine-api
spec:
  replicas: 1
  selector:
    matchLabels:
      machine.openshift.io/cluster-api-cluster: <infrastructure_id>
      machine.openshift.io/cluster-api-machineset: <infrastructure_id>-windows-worker-<zone>
  template:
    metadata:
      labels:
        machine.openshift.io/cluster-api-cluster: <infrastructure_id>
        machine.openshift.io/cluster-api-machine-role: worker
        machine.openshift.io/cluster-api-machine-type: worker
        machine.openshift.io/cluster-api-machineset: <infrastructure_id>-windows-worker-<zone>
        machine.openshift.io/os-id: Windows
    spec:
      metadata:
        labels:
          node-role.kubernetes.io/worker: ""
      providerSpec:
        value:
          apiVersion: machine.openshift.io/v1
          bootType: ""
          categories: null
          cluster:
            type: uuid
            uuid: <cluster_uuid>
          credentialsSecret:
            name: nutanix-credentials
          image:
            name: <image_id>
            type: name
          kind: NutanixMachineProviderConfig
          memorySize: 16Gi
          project:
            type: ""
          subnets:
          - type: uuid
            uuid: <subnet_uuid>
          systemDiskSize: 120Gi
          userDataSecret:
            name: windows-user-data
          vcpuSockets: 4
          vcpusPerSocket: 1
```

where:

`metadata.labels.machine.openshift.io/cluster-api-cluster`
Replace `<infrastructure_id>` with the infrastructure ID. You can obtain the infrastructure ID by running the following command:

``` terminal
$ oc get -o jsonpath='{.status.infrastructureName}{"\n"}' infrastructure cluster
```

`metadata.name`
Replace the infrastructure ID, worker label, and zone.

`spec.selector.matchLabels`
Replace the parameters for the following labels:

- `machine.openshift.io/cluster-api-cluster`. Replace the infrastructure ID.

- `machine.openshift.io/cluster-api-machineset`. Replace the infrastructure ID, worker label, and zone.

`spec.template.metadata.labels`
Replace the parameters for the following labels:

- `machine.openshift.io/cluster-api-cluster`. Replace the infrastructure ID.

- `machine.openshift.io/cluster-api-machineset`. Replace the infrastructure ID, worker label, and zone.

- `machine.openshift.io/os-id: Windows`. When set to `Windows`, configures the compute machine set as a Windows machine.

`spec.template.spec.metadata.labels`
When set to `node-role.kubernetes.io/worker`, configures the node as a compute machine.

`spec.template.spec.providerSpec`
Specify the following parameters:

- `value.bootType`. Specifies the boot type that the compute machines use. Valid values are `Legacy`, `SecureBoot`, or `UEFI`. The default is `Legacy`. For more information about boot types, see "Understanding UEFI, Secure Boot, and TPM in the Virtualized Environment (Nutanix documentaiton)" in the *Additional resources* section.

  > [!NOTE]
  > You must use the `Legacy` boot type in OpenShift Container Platform 4.17.

- `value.cluster`. Specifies a Nutanix Prism Element cluster configuration. In this example, the cluster type is `uuid`, so there is a `uuid` stanza. Replace `<cluster_uuid>` with the cluster UUID.

- `value.credentialsSecret.name`. Specifies the secret name for the cluster. Do not change this value.

- `value.image`. Specifies the image to use. Replace `<image_id>` with an image from an existing default compute machine set for the cluster.

- `value.kind`. Specifies the cloud provider platform type. Do not change this value.

- `value.memorySize`. Specifies the amount of memory for the cluster in Gi.

- `value.subnets`. Specifies a subnet configuration. In this example, the subnet type is `uuid`, so there is a `uuid` stanza. Replace `<subnet_uuid>` with the subnet UUID.

- `value.systemDiskSize`. Specifies the size of the system disk in Gi.

- `value.userDataSecret.name`. Specifies the name of the secret in the user data YAML file that is in the `openshift-machine-api` namespace. Use the value that installation program populates in the default compute machine set.

- `value.vcpuSockets`. Specifies the number of vCPU sockets.

- `value.vcpusPerSocket`. Specifies the number of vCPUs per socket.

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

# Additional resources

- [Overview of machine management](../../machine_management/index.md#overview-of-machine-management)

- [Understanding UEFI, Secure Boot, and TPM in the Virtualized Environment (Nutanix documenation)](https://portal.nutanix.com/page/documents/kbs/details?targetId=kA07V000000H3K9SAK)
