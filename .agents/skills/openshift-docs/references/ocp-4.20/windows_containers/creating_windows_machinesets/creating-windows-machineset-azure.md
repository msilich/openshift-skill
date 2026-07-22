<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

You can use a `MachineSet` custom resource (CR) to add a Windows compute node to your Microsoft Azure cluster, where you can run Windows container workloads.

For example, you might create infrastructure Windows machine sets and related machines so that you can move supporting Windows workloads to the new Windows machines. For more information about machine sets, see "Overview of machine management" in the *Additional resources* section.

# Prerequisites

- You installed the Windows Machine Config Operator (WMCO) using Operator Lifecycle Manager (OLM).

- You are using a supported Windows Server as the operating system image.

# Sample YAML for a Windows MachineSet object on Azure

You can add Windows nodes to an Microsoft Azure cluster by defining a Windows `MachineSet` object that the Windows Machine Config Operator (WMCO) can react upon.

The following example is a YAML file for creating a `MachineSet` object for Azure.

``` yaml
apiVersion: machine.openshift.io/v1beta1
kind: MachineSet
metadata:
  labels:
    machine.openshift.io/cluster-api-cluster: <infrastructure_id>
  name: <windows_machine_set_name>
  namespace: openshift-machine-api
spec:
  replicas: 1
  selector:
    matchLabels:
      machine.openshift.io/cluster-api-cluster: <infrastructure_id>
      machine.openshift.io/cluster-api-machineset: <windows_machine_set_name>
  template:
    metadata:
      labels:
        machine.openshift.io/cluster-api-cluster: <infrastructure_id>
        machine.openshift.io/cluster-api-machine-role: worker
        machine.openshift.io/cluster-api-machine-type: worker
        machine.openshift.io/cluster-api-machineset: <windows_machine_set_name>
        machine.openshift.io/os-id: Windows
    spec:
      metadata:
        labels:
          node-role.kubernetes.io/worker: ""
      providerSpec:
        value:
          apiVersion: azureproviderconfig.openshift.io/v1beta1
          credentialsSecret:
            name: azure-cloud-credentials
            namespace: openshift-machine-api
          image:
            offer: WindowsServer
            publisher: MicrosoftWindowsServer
            resourceID: ""
            sku: 2022-datacenter
            version: latest
          kind: AzureMachineProviderSpec
          location: <location>
          networkResourceGroup: <infrastructure_id>-rg
          osDisk:
            diskSizeGB: 128
            managedDisk:
              storageAccountType: Premium_LRS
            osType: Windows
          publicIP: false
          resourceGroup: <infrastructure_id>-rg
          subnet: <infrastructure_id>-worker-subnet
          userDataSecret:
            name: windows-user-data
            namespace: openshift-machine-api
          vmSize: Standard_D2s_v3
          vnet: <infrastructure_id>-vnet
          zone: "<zone>"
```

where:

`metadata.labels`
For the `machine.openshift.io/cluster-api-cluster` label, replace `<infrastructure_id>` with the infrastructure ID that is based on the cluster ID that you set when you provisioned the cluster. You can obtain the infrastructure ID by running the following command:

``` terminal
$ oc get -o jsonpath='{.status.infrastructureName}{"\n"}' infrastructure cluster
```

`metadata.name`
Replace `<windows_machine_set_name>` with the Windows compute machine set name. Windows machine names on Azure cannot be more than 15 characters long. Therefore, the compute machine set name cannot be more than 9 characters long, due to the way machine names are generated from it.

`spec.selector.matchLabels`
Replace the parameters for the following labels:

- `machine.openshift.io/cluster-api-cluster`. Replace the infrastructure ID.

- `machine.openshift.io/cluster-api-machineset`. Replace the Windows compute machine set name.

`spec.template.metadata.labels`
Replace the parameters for the following labels:

- `machine.openshift.io/cluster-api-cluster`. Replace the infrastructure ID.

- `machine.openshift.io/cluster-api-machineset`. Replace the Windows compute machine set name.

- `machine.openshift.io/os-id: Windows`. When set to `Windows`, configures the compute machine set as a Windows machine.

`spec.template.spec.metadata.labels`
When set to `node-role.kubernetes.io/worker`, configures the node as a compute machine.

`spec.template.spec.providerSpec`
Specify the following parameters:

- `value.image`. Specifies a `WindowsServer` image offering that defines the `2022-datacenter` SKU.

- `value.location`. Specifies the Azure region, such as `centralus`.

- `value.networkResourceGroup`. Replace the infrastructure ID.

- `value.resourceGroup`. Replace the infrastructure ID.

- `value.userDataSecret.name`. Specifies the name of the secret in the user data YAML file that is in the `openshift-machine-api` namespace. Use the value that installation program populates in the default compute machine set.

- `value.zone`. Specifies the zone within your region to place machines on. Be sure that your region supports the zone that you specify.

# Creating a compute machine set

To dynamically manage machine compute resources, you can create your own compute machine sets in addition to the compute machine sets created by the installation program. Use the OpenShift Container Platform CLI to automate node provisioning.

<div>

<div class="title">

Prerequisites

</div>

- Deploy an OpenShift Container Platform cluster.

- Install the OpenShift CLI (`oc`).

- Log in to `oc` as a user with `cluster-admin` permission.

- In disconnected environments, the image specified in the `MachineSet` custom resource (CR) must have the [OpenSSH server v0.0.1.0 installed](https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse?tabs=powershell#install-openssh-for-windows).

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
  NAME                                       DESIRED   CURRENT   READY   AVAILABLE   AGE
  agl030519-vplxk-windows-worker-us-east-1a  1         1         1       1           11m
  agl030519-vplxk-worker-us-east-1a          1         1         1       1           55m
  agl030519-vplxk-worker-us-east-1b          1         1         1       1           55m
  agl030519-vplxk-worker-us-east-1c          1         1         1       1           55m
  agl030519-vplxk-worker-us-east-1d          0         0                             55m
  agl030519-vplxk-worker-us-east-1e          0         0                             55m
  agl030519-vplxk-worker-us-east-1f          0         0                             55m
  ```

  When the new compute machine set is available, the `DESIRED` and `CURRENT` values match. If the compute machine set is not available, wait a few minutes and run the command again.

</div>

# Additional resources

- [Overview of machine management](../../machine_management/index.md#overview-of-machine-management)
