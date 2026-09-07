<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

You can simplify virtual machine (VM) creation by using instance types, whether you use the OpenShift Container Platform web console or the CLI to create VMs.

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

# Pre-defined instance types

OpenShift Virtualization includes a set of pre-defined instance types called `common-instancetypes`. Some are specialized for specific workloads and others are workload-agnostic.

These instance type resources are named according to their series, version, and size. The size value follows the `.` delimiter and ranges from `nano` to `8xlarge`.

<table>
<caption><code>common-instancetypes</code> series comparison</caption>
<colgroup>
<col style="width: 25%" />
<col style="width: 12%" />
<col style="width: 25%" />
<col style="width: 12%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr>
<th style="text-align: center;">Use case</th>
<th style="text-align: center;">Series</th>
<th style="text-align: center;">Characteristics</th>
<th style="text-align: center;">vCPU to memory ratio</th>
<th style="text-align: center;">Example resource</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><p>Network</p></td>
<td style="text-align: center;"><p>N</p></td>
<td style="text-align: left;"><ul>
<li><p>Hugepages</p></li>
<li><p>Dedicated CPU</p></li>
<li><p>Isolated emulator threads</p></li>
<li><p>Requires nodes capable of running DPDK workloads</p></li>
</ul></td>
<td style="text-align: center;"><p>1:2</p></td>
<td style="text-align: left;"><dl>
<dt><code>n1.medium</code></dt>
<dd>
<ul>
<li><p>4 vCPUs</p></li>
<li><p>4GiB Memory</p></li>
</ul>
</dd>
</dl></td>
</tr>
<tr>
<td style="text-align: center;"><p>Overcommitted</p></td>
<td style="text-align: center;"><p>O</p></td>
<td style="text-align: left;"><ul>
<li><p>Overcommitted memory</p></li>
<li><p>Burstable CPU performance</p></li>
</ul></td>
<td style="text-align: center;"><p>1:4</p></td>
<td style="text-align: left;"><dl>
<dt><code>o1.small</code></dt>
<dd>
<ul>
<li><p>1 vCPU</p></li>
<li><p>2GiB Memory</p></li>
</ul>
</dd>
</dl></td>
</tr>
<tr>
<td style="text-align: center;"><p>Compute Exclusive</p></td>
<td style="text-align: center;"><p>CX</p></td>
<td style="text-align: left;"><ul>
<li><p>Hugepages</p></li>
<li><p>Dedicated CPU</p></li>
<li><p>Isolated emulator threads</p></li>
<li><p>vNUMA</p></li>
</ul></td>
<td style="text-align: center;"><p>1:2</p></td>
<td style="text-align: left;"><dl>
<dt><code>cx1.2xlarge</code></dt>
<dd>
<ul>
<li><p>8 vCPUs</p></li>
<li><p>16GiB Memory</p></li>
</ul>
</dd>
</dl></td>
</tr>
<tr>
<td style="text-align: center;"><p>General Purpose</p></td>
<td style="text-align: center;"><p>U</p></td>
<td style="text-align: left;"><ul>
<li><p>Burstable CPU performance</p></li>
</ul></td>
<td style="text-align: center;"><p>1:4</p></td>
<td style="text-align: left;"><dl>
<dt><code>u1.medium</code></dt>
<dd>
<ul>
<li><p>1 vCPU</p></li>
<li><p>4GiB Memory</p></li>
</ul>
</dd>
</dl></td>
</tr>
<tr>
<td style="text-align: center;"><p>Memory Intensive</p></td>
<td style="text-align: center;"><p>M</p></td>
<td style="text-align: left;"><ul>
<li><p>Hugepages</p></li>
<li><p>Burstable CPU performance</p></li>
</ul></td>
<td style="text-align: center;"><p>1:8</p></td>
<td style="text-align: left;"><dl>
<dt><code>m1.large</code></dt>
<dd>
<ul>
<li><p>2 vCPUs</p></li>
<li><p>16GiB Memory</p></li>
</ul>
</dd>
</dl></td>
</tr>
<tr>
<td style="text-align: center;"><p>Dedicated</p></td>
<td style="text-align: center;"><p>D</p></td>
<td style="text-align: left;"><ul>
<li><p>Dedicated CPU</p></li>
<li><p>Isolated emulator threads</p></li>
</ul></td>
<td style="text-align: center;"><p>1:4</p></td>
<td style="text-align: left;"><dl>
<dt><code>d1.medium</code></dt>
<dd>
<ul>
<li><p>1 vCPUs</p></li>
<li><p>4GiB Memory</p></li>
</ul>
</dd>
</dl></td>
</tr>
</tbody>
</table>

# Specifying an instance type or preference

You can specify an instance type, a preference, or both to define a set of workload sizing and runtime characteristics for reuse across multiple VMs.

## Using flags to specify instance types and preferences

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

## Inferring an instance type or preference

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

## Setting the inferFromVolume labels

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

# Creating a VM from an instance type by using the web console

You can create a virtual machine (VM) from an instance type by using the OpenShift Container Platform web console. You can also use the web console to create a VM by copying an existing snapshot or to clone a VM.

You can create a VM from a list of available bootable volumes. You can add Linux- or Windows-based volumes to the list.

<div>

<div class="title">

Procedure

</div>

1.  In the web console, navigate to **Virtualization** → **Catalog**.

    The **InstanceTypes** tab opens by default.

    > [!NOTE]
    > When configuring a downward-metrics device on an IBM Z® system that uses a VM preference, set the `spec.preference.name` value to `rhel.9.s390x` or another available preference with the format `*.s390x`.

2.  Heterogeneous clusters only: To filter the bootable volumes using the options provided, click **Architecture**.

3.  Select either of the following options:

    - Select a suitable bootable volume from the list. If the list is truncated, click the **Show all** button to display the entire list.

      > [!NOTE]
      > The bootable volume table lists only those volumes in the `openshift-virtualization-os-images` namespace that have the `instancetype.kubevirt.io/default-preference` label.

      - Optional: Click the star icon to designate a bootable volume as a favorite. Starred bootable volumes appear first in the volume list.

    - Click **Add volume** to upload a new volume or to use an existing persistent volume claim (PVC), a volume snapshot, or a `containerDisk` volume. Click **Save**.

      Logos of operating systems that are not available in the cluster are shown at the bottom of the list. You can add a volume for the required operating system by clicking the **Add volume** link.

      In addition, there is a link to the **Create a Windows bootable volume** quick start. The same link appears in a popover if you hover the pointer over the question mark icon next to the *Select volume to boot from* line.

      Immediately after you install the environment or when the environment is disconnected, the list of volumes to boot from is empty. In that case, three operating system logos are displayed: Windows, RHEL, and Linux. You can add a new volume that meets your requirements by clicking the **Add volume** button.

4.  Click an instance type tile and select the resource size appropriate for your workload. You can select huge pages for Red Hat-provided instance types of the **M** and **CX** series. Huge page options are identified by names that end with **1gi**.

5.  Optional: Choose the virtual machine details, including the VM’s name, that apply to the volume you are booting from:

    - For a Linux-based volume, follow these steps to configure SSH:

      1.  If you have not already added a public SSH key to your project, click the edit icon beside **Authorized SSH key** in the **VirtualMachine details** section.

      2.  Select one of the following options:

          - **Use existing**: Select a secret from the secrets list.

          - **Add new**: Follow these steps:

            1.  Browse to the public SSH key file or paste the file in the key field.

            2.  Enter the secret name.

            3.  Optional: Select **Automatically apply this key to any new VirtualMachine you create in this project**.

      3.  Click **Save**.

    - For a Windows volume, follow either of these set of steps to configure sysprep options:

      - If you have not already added sysprep options for the Windows volume, follow these steps:

        1.  Click the edit icon beside **Sysprep** in the **VirtualMachine details** section.

        2.  Add the **Autoattend.xml** answer file.

        3.  Add the **Unattend.xml** answer file.

        4.  Click **Save**.

      - If you want to use existing sysprep options for the Windows volume, follow these steps:

        1.  Click **Attach existing sysprep**.

        2.  Enter the name of the existing sysprep **Unattend.xml** answer file.

        3.  Click **Save**.

6.  Optional: If you are creating a Windows VM, you can mount a Windows driver disk:

    1.  Click the **Customize VirtualMachine** button.

    2.  On the **VirtualMachine details** page, click **Storage**.

    3.  Select the **Mount Windows drivers disk** checkbox.

7.  Optional: Click **View YAML & CLI** to view the YAML file. Click **CLI** to view the CLI commands. You can also download or copy either the YAML file contents or the CLI commands.

8.  Click **Create VirtualMachine**.

</div>

<div class="formalpara">

<div class="title">

Result

</div>

After the VM is created, you can monitor the status on the **VirtualMachine details** page.

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
