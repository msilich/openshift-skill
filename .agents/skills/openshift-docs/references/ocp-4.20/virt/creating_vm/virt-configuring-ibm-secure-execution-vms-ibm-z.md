<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

You can configure IBM® Secure Execution virtual machines (VMs) on IBM Z® and IBM® LinuxONE.

IBM® Secure Execution for Linux is a s390x security technology that is introduced with IBM® z15 and IBM® LinuxONE III. It protects data of workloads that run in a KVM guest from being inspected or modified by the server environment.

In particular, no hardware administrator, no KVM code, and no KVM administrator can access the data in a guest that was started as an IBM Secure Execution guest.

> [!IMPORTANT]
> OpenShift Virtualization with IBM Secure Execution enabled on IBM Z and IBM LinuxONE is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.
>
> For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

<div>

<div class="title">

Additional resources

</div>

- [What is IBM Secure Execution?](https://www.ibm.com/docs/en/linux-on-systems?topic=execution-introduction)

</div>

# Enabling VMs to run IBM Secure Execution on IBM Z and IBM LinuxONE

To enable IBM® Secure Execution virtual machines (VMs) on IBM Z® and IBM® LinuxONE on the compute nodes of your cluster, you must ensure that you meet the prerequisites and complete the following steps.

<div>

<div class="title">

Prerequisites

</div>

- Your cluster has logical partition (LPAR) nodes running on IBM® z15 or later, or IBM® LinuxONE III or later.

- You have IBM® Secure Execution workloads available to run on the cluster.

- You have installed the OpenShift CLI (`oc`).

</div>

<div>

<div class="title">

Procedure

</div>

1.  To run IBM® Secure Execution VMs, you must add the `prot_virt=1` kernel parameter for each compute node. To enable all compute nodes, create a file named `secure-execution.yaml` that contains the following machine config manifest:

    ``` yaml
    apiVersion: machineconfiguration.openshift.io/v1
    kind: MachineConfig
    metadata:
      name: secure-execution
      labels:
        machineconfiguration.openshift.io/role: worker
    spec:
      kernelArguments:
        - prot_virt=1
    ```

    where:

    `prot_virt=1`
    Specifies that the ultravisor can store memory security information.

2.  Apply the changes by running the following command:

    ``` terminal
    $ oc apply -f secure-execution.yaml
    ```

    The Machine Config Operator (MCO) applies the changes and reboots the nodes in a controlled rollout.

3.  Edit the `HyperConverged` custom resource (CR) by running the following command:

    ``` terminal
    $ oc edit -n openshift-cnv HyperConverged kubevirt-hyperconverged
    ```

4.  Enable the feature gate for IBM® Secure Execution by applying the following annotations:

    ``` yaml
    apiVersion: hco.kubevirt.io/v1beta1
    kind: HyperConverged
    metadata:
      annotations:
        kubevirt.kubevirt.io/jsonpatch: |-
         [
          {
           "op":"add",
           "path":"/spec/configuration/developerConfiguration/featureGates/-",
           "value":"SecureExecution"
          }
         ]
    ```

</div>

# Launching an IBM Secure Execution VM on IBM Z and IBM LinuxONE

Before launching an IBM® Secure Execution VM on IBM Z® and IBM® LinuxONE, you must add the `launchSecurity` parameter to the VM manifest. Otherwise, the VM does not boot correctly because it does not have access to the devices.

<div>

<div class="title">

Procedure

</div>

- Apply the following `VirtualMachine` manifest to the cluster:

  ``` yaml
  apiVersion: kubevirt.io/v1
  kind: VirtualMachine
  metadata:
    labels:
      kubevirt.io/vm: f41-se
    name: f41-se
  spec:
    runStrategy: Always
    template:
      metadata:
        labels:
          kubevirt.io/vm: f41-se
      spec:
        domain:
          launchSecurity: {}
          devices:
            disks:
            - disk:
                bus: virtio
              name: rootfs
          machine:
            type: ""
          resources:
            requests:
              memory: 4Gi
        terminationGracePeriodSeconds: 0
        volumes:
          - name: rootfs
            dataVolume:
              name: f41-se
  ```

  To launch IBM® Secure Execution VMs, you must include the following YAML in the manifest:

  ``` yaml
  spec:
     domain:
       launchSecurity: {}
  ```

  The rest of the VM manifest is variable depending on your setup.

  > [!NOTE]
  > Because the memory of the VM is protected, IBM® Secure Execution VMs are not live migratable. The VMs can only be migrated offline.

</div>
