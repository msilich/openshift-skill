<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

You can simplify virtual machine (VM) creation by using instance types, which define a reusable set of resources, such as CPU and memory. You can create instance types or change the VMs that use them.

# About instance types

An instance type is a reusable object where you can define resources and characteristics to apply to new VMs. You can define custom instance types or use the variety that are included when you install OpenShift Virtualization.

To create a new instance type, you must first create a manifest, either manually or by using the `virtctl` CLI tool. You then create the instance type object by applying the manifest to your cluster.

OpenShift Virtualization provides two CRDs for configuring instance types:

- A namespaced object: `VirtualMachineInstancetype`

- A cluster-wide object: `VirtualMachineClusterInstancetype`

These objects use the same `VirtualMachineInstancetypeSpec`.

## Required attributes

When you configure an instance type, you must define the `cpu` and `memory` attributes. Other attributes are optional.

> [!NOTE]
> When you create a VM from an instance type, you cannot override any parameters defined in the instance type.
>
> Because instance types require defined CPU and memory attributes, OpenShift Virtualization always rejects additional requests for these resources when creating a VM from an instance type.

You can manually create an instance type manifest. For example:

``` yaml
apiVersion: instancetype.kubevirt.io/v1beta1
kind: VirtualMachineInstancetype
metadata:
  name: example-instancetype
spec:
  cpu:
    guest: 1
  memory:
    guest: 128Mi
```

- `spec.cpu.guest` is a required field that specifies the number of vCPUs to allocate to the guest.

- `spec.memory.guest` is a required field that specifies an amount of memory to allocate to the guest.

You can create an instance type manifest by using the `virtctl` CLI utility. For example:

``` terminal
$ virtctl create instancetype --cpu 2 --memory 256Mi
```

where:

`--cpu <value>`
Specifies the number of vCPUs to allocate to the guest. Required.

`--memory <value>`
Specifies an amount of memory to allocate to the guest. Required.

> [!TIP]
> You can immediately create the object from the new manifest by running the following command:
>
> ``` terminal
> $ virtctl create instancetype --cpu 2 --memory 256Mi | oc apply -f -
> ```

## Optional attributes

In addition to the required `cpu` and `memory` attributes, you can include the following optional attributes in the `VirtualMachineInstancetypeSpec`:

`annotations`
List annotations to apply to the VM.

`gpus`
List vGPUs for passthrough.

`hostDevices`
List host devices for passthrough.

`ioThreadsPolicy`
Define an IO threads policy for managing dedicated disk access.

`launchSecurity`
Configure Secure Encrypted Virtualization (SEV).

`nodeSelector`
Specify node selectors to control the nodes where this VM is scheduled.

`schedulerName`
Define a custom scheduler to use for this VM instead of the default scheduler.

## Controller revisions

When you create a VM by using an instance type, a `ControllerRevision` object retains an immutable snapshot of the instance type object. This snapshot locks in resource-related characteristics defined in the instance type object, such as the required guest CPU and memory. The VM status also contains a reference to the `ControllerRevision` object.

This snapshot is essential for versioning, and ensures that the VM instance created when starting a VM does not change if the underlying instance type object is updated while the VM is running.

# Using flags to specify instance types and preferences

You can specify instance types and preferences by using flags.

<div>

<div class="title">

Prerequisites

</div>

- You must have an instance type, preference, or both on the cluster.

</div>

<div>

<div class="title">

Procedure

</div>

1.  To specify an instance type when creating a VM, use the `--instancetype` flag. To specify a preference, use the `--preference` flag. The following example includes both flags:

    ``` terminal
    $ virtctl create vm --instancetype <my_instancetype> --preference <my_preference>
    ```

2.  Optional: To specify a namespaced instance type or preference, include the `kind` in the value passed to the `--instancetype` or `--preference` flag command. The namespaced instance type or preference must be in the same namespace you are creating the VM in. The following example includes flags for a namespaced instance type and a namespaced preference:

    ``` terminal
    $ virtctl create vm --instancetype virtualmachineinstancetype/<my_instancetype> --preference virtualmachinepreference/<my_preference>
    ```

</div>

# Inferring an instance type or preference

Inferring instance types, preferences, or both is enabled by default, and the `inferFromVolumeFailure` policy of the `inferFromVolume` attribute is set to `Ignore`. When inferring from the boot volume, errors are ignored, and the VM is created with the instance type and preference left unset.

However, when flags are applied, the `inferFromVolumeFailure` policy defaults to `Reject`. When inferring from the boot volume, errors result in the rejection of the creation of that VM.

You can use the `--infer-instancetype` and `--infer-preference` flags to infer which instance type, preference, or both to use to define the workload sizing and runtime characteristics of a VM.

<div>

<div class="title">

Prerequisites

</div>

- You have installed the `virtctl` tool.

</div>

<div>

<div class="title">

Procedure

</div>

- To explicitly infer instance types from the volume used to boot the VM, use the `--infer-instancetype` flag. To explicitly infer preferences, use the `--infer-preference` flag. The following command includes both flags:

  ``` terminal
  $ virtctl create vm --volume-import type:pvc,src:my-ns/my-pvc --infer-instancetype --infer-preference
  ```

- To infer an instance type or preference from a volume other than the volume used to boot the VM, use the `--infer-instancetype-from` and `--infer-preference-from` flags to specify any of the virtual machine’s volumes. In the example below, the virtual machine boots from `volume-a` but infers the instancetype and preference from `volume-b`.

  ``` terminal
  $ virtctl create vm \
    --volume-import=type:pvc,src:my-ns/my-pvc-a,name:volume-a \
    --volume-import=type:pvc,src:my-ns/my-pvc-b,name:volume-b \
    --infer-instancetype-from volume-b \
    --infer-preference-from volume-b
  ```

</div>

# Setting the inferFromVolume labels

Use the following labels on your PVC, data source, or data volume to instruct the inference mechanism which instance type, preference, or both to use when trying to boot from a volume.

- A cluster-wide instance type: `instancetype.kubevirt.io/default-instancetype` label.

- A namespaced instance type: `instancetype.kubevirt.io/default-instancetype-kind` label. Defaults to the `VirtualMachineClusterInstancetype` label if left empty.

- A cluster-wide preference: `instancetype.kubevirt.io/default-preference` label.

- A namespaced preference: `instancetype.kubevirt.io/default-preference-kind` label. Defaults to `VirtualMachineClusterPreference` label, if left empty.

<div>

<div class="title">

Prerequisites

</div>

- You must have an instance type, preference, or both on the cluster.

- You have installed the OpenShift CLI (`oc`).

</div>

<div>

<div class="title">

Procedure

</div>

- To apply a label to a data source, use `oc label`. The following command applies a label that points to a cluster-wide instance type:

  ``` terminal
  $ oc label DataSource foo instancetype.kubevirt.io/default-instancetype=<my_instancetype>
  ```

</div>

# Change the instance type for a VM

Cluster administrators and VM owners can change the instance type for existing virtual machines to adjust resources or optimize performance for specific workloads.

Changing the instance type for a VM allows you to adapt to evolving workload requirements without recreating the virtual machine. When a VM’s workload increases over time, you can switch to an instance type with more CPU, additional memory, or specific hardware resources to prevent performance bottlenecks and ensure the VM continues to meet demand.

Different instance types are optimized for specific use cases, so switching to a specialized instance type can improve performance for particular workloads. For example, you might transition to a compute-optimized instance type for CPU-intensive applications or to a memory-optimized type for workloads that require larger memory allocations.

You can change the instance type for an existing VM using either the OpenShift Container Platform web console or the OpenShift CLI (`oc`).

## Changing the instance type of a VM by using the web console

You can change the instance type associated with a running virtual machine (VM) by using the web console. The change takes effect immediately.

<div>

<div class="title">

Prerequisites

</div>

- You created the VM by using an instance type.

</div>

<div>

<div class="title">

Procedure

</div>

1.  In the OpenShift Container Platform web console, click **Virtualization** → **VirtualMachines**.

2.  Select a VM to open the **VirtualMachine details** page.

3.  Click the **Configuration** tab.

4.  On the **Details** tab, click the instance type text to open the **Edit Instancetype** dialog. For example, click **1 CPU \| 2 GiB Memory**.

5.  Edit the instance type by using the **Series** and **Size** lists.

    1.  Select an item from the **Series** list to show the relevant sizes for that series. For example, select **General Purpose**.

    2.  Select the new instance type for the VM from the **Size** list. For example, select **medium: 1 CPUs, 4Gi Memory**, which is available in the **General Purpose** series.

6.  Click **Save**.

</div>

<div>

<div class="title">

Verification

</div>

1.  Click the **YAML** tab.

2.  Click **Reload**.

3.  Review the VM YAML to confirm that the instance type changed.

</div>

## Changing the instance type of a VM by using the CLI

To change the instance type of a VM, change the `name` field in the VM spec. This triggers the update logic, which ensures that a new, immutable controller revision snapshot is taken of the new resource configuration.

<div>

<div class="title">

Prerequisites

</div>

- You have installed the OpenShift CLI (`oc`).

- You created the VM by using an instance type, or have administrator privileges for the VM that you want to modify.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Stop the VM.

2.  Run the following command, and replace `<vm_name>` with the name of your VM, and `<new_instancetype>` with the name of the instance type you want to change to:

    ``` terminal
    $ oc patch vm/<vm_name> --type merge -p '{"spec":{"instancetype":{"name": "<new_instancetype>"}}}'
    ```

</div>

<div>

<div class="title">

Verification

</div>

- Check the controller revision reference in the updated VM `status` field. Run the following command and verify that the revision name is updated in the output:

  ``` terminal
  $ oc get vms/<vm_name> -o json | jq .status.instancetypeRef
  ```

  Example output:

  ``` terminal
  {
    "controllerRevisionRef": {
      "name": "vm-cirros-csmall-csmall-3e86e367-9cd7-4426-9507-b14c27a08671-2"
    },
    "kind": "VirtualMachineInstancetype",
    "name": "csmall"
  }
  ```

- Optional: Check that the VM instance is running the new configuration defined in the latest controller revision. For example, if you updated the instance type to use 2 vCPUs instead of 1, run the following command and check the output:

  ``` terminal
  $ oc get vmi/<vm_name> -o json | jq .spec.domain.cpu
  ```

  Example output that verifies that the revision uses 2 vCPUs:

  ``` terminal
  {
    "cores": 1,
    "model": "host-model",
    "sockets": 2,
    "threads": 1
  }
  ```

</div>

# Additional resources

- [Configuring a downward metrics device](../monitoring/virt-exposing-downward-metrics.md#virt-configuring-downward-metrics_virt-exposing-downward-metrics)
