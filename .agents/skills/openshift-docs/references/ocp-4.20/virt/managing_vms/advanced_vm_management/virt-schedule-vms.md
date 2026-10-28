<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

You can schedule a virtual machine (VM) on a node by ensuring that the VM’s CPU model and policy attribute are matched for compatibility with the CPU models and policy attributes supported by the node.

# CPU feature policy attributes

A policy attribute controls how strictly the scheduler enforces a CPU feature that you set on a virtual machine (VM). Use a policy attribute to require a feature, treat it as optional, or forbid it.

| Policy attribute | Description |
|----|----|
| force | The VM is forced to be scheduled on a node. This is true even if the host CPU does not support the VM’s CPU. |
| require | Default policy that applies to a VM if the VM is not configured with a specific CPU model and feature specification. If a node is not configured to support CPU node discovery with this default policy attribute or any one of the other policy attributes, VMs are not scheduled on that node. Either the host CPU must support the VM’s CPU or the hypervisor must be able to emulate the supported CPU model. |
| optional | The VM is added to a node if that VM is supported by the host’s physical machine CPU. |
| disable | The VM cannot be scheduled with CPU node discovery. |
| forbid | The VM is not scheduled even if the feature is supported by the host CPU and CPU node discovery is enabled. |

# Set a policy attribute and CPU feature

Set a CPU feature and a policy attribute on a virtual machine (VM) so that the VM runs only where the feature is available. The feature must be supported by the host CPU or emulated by the hypervisor.

<div>

<div class="title">

Procedure

</div>

- Edit the `domain` spec of your VM configuration file. The following example sets the CPU feature and the `require` policy for a virtual machine (VM):

  ``` yaml
  apiVersion: kubevirt.io/v1
  kind: VirtualMachine
  metadata:
    name: myvm
  spec:
    template:
      spec:
        domain:
          cpu:
            features:
              - name: apic
                policy: require
  ```

  - `spec.template.spec.domain.cpu.features.name` defines the name of the CPU feature for the VM.

  - `spec.template.spec.domain.cpu.features.policy` defines the policy attribute for the VM.

</div>

# Set a VM to run only on nodes with a named CPU model

Set a named CPU model on a virtual machine (VM) so that the scheduler places the VM only on nodes that support that model.

<div>

<div class="title">

Procedure

</div>

- Edit the `domain` spec of your virtual machine configuration file. The following example shows a specific CPU model defined for a VM:

  ``` yaml
  apiVersion: kubevirt.io/v1
  kind: VirtualMachine
  metadata:
    name: myvm
  spec:
    template:
      spec:
        domain:
          cpu:
            model: Conroe
  # ...
  ```

  - `spec.template.spec.domain.cpu.model` defines the CPU model for the VM.

</div>

# Set a VM to inherit the node CPU model

Set the CPU model of a virtual machine (VM) to `host-model` so that the VM inherits the CPU model of the node where it is scheduled, and can use the CPU features that the node provides.

<div>

<div class="title">

Procedure

</div>

- Edit the `domain` spec of your VM configuration file. The following example shows `host-model` being specified for the virtual machine:

  ``` yaml
  apiVersion: kubevirt/v1alpha3
  kind: VirtualMachine
  metadata:
    name: myvm
  spec:
    template:
      spec:
        domain:
          cpu:
            model: host-model
  ```

  - `spec.template.spec.domain.cpu.model` defines the VM that inherits the CPU model of the node where it is scheduled.

</div>

# Schedule VMs with a custom scheduler

You can run a virtual machine (VM) under a custom scheduler instead of the default scheduler, so that your own scheduling logic decides which node runs the VM.

<div>

<div class="title">

Prerequisites

</div>

- A secondary scheduler is configured for your cluster.

- You have installed the OpenShift CLI (`oc`).

</div>

<div>

<div class="title">

Procedure

</div>

- Add the custom scheduler to the VM configuration by editing the `VirtualMachine` manifest. For example:

  ``` yaml
  apiVersion: kubevirt.io/v1
  kind: VirtualMachine
  metadata:
    name: vm-fedora
  spec:
    runStrategy: Always
    template:
      spec:
        schedulerName: my-scheduler
        domain:
          devices:
            disks:
              - name: containerdisk
                disk:
                  bus: virtio
  # ...
  ```

  `schedulerName`
  The name of the custom scheduler. If the `schedulerName` value does not match an existing scheduler, the `virt-launcher` pod stays in a `Pending` state until the specified scheduler is found.

</div>

<div>

<div class="title">

Verification

</div>

- Verify that the VM is using the custom scheduler specified in the `VirtualMachine` manifest by checking the `virt-launcher` pod events:

  1.  View the list of pods in your cluster by entering the following command:

      ``` terminal
      $ oc get pods
      ```

      Example output:

      ``` terminal
      NAME                             READY   STATUS    RESTARTS   AGE
      virt-launcher-vm-fedora-dpc87    2/2     Running   0          24m
      ```

  2.  Run the following command to display the pod events:

      ``` terminal
      $ oc describe pod virt-launcher-vm-fedora-dpc87
      ```

      The value of the `From` field in the output verifies that the scheduler name matches the custom scheduler specified in the `VirtualMachine` manifest:

      Example output:

      ``` terminal
      [...]
      Events:
        Type    Reason     Age   From              Message
        ----    ------     ----  ----              -------
        Normal  Scheduled  21m   my-scheduler  Successfully assigned default/virt-launcher-vm-fedora-dpc87 to node01
      [...]
      ```

</div>

<div>

<div class="title">

Additional resources

</div>

- [Deploying a secondary scheduler](../../../nodes/scheduling/secondary_scheduler/nodes-secondary-scheduler-configuring.md#nodes-secondary-scheduler-configuring-console_secondary-scheduler-configuring)

</div>
