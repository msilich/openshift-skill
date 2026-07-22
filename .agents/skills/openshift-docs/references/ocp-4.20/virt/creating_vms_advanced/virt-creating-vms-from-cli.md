<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

You can create virtual machines (VMs) from the command line by editing or creating a `VirtualMachine` manifest. You can simplify VM configuration by using an instance type in your VM manifest.

> [!NOTE]
> You can also create VMs from instance types by using the OpenShift Container Platform web console.

# Creating a VM from a VirtualMachine manifest

You can create a virtual machine (VM) from a `VirtualMachine` manifest. To simplify the creation of these manifests, you can use the `virtctl` command-line tool.

<div>

<div class="title">

Prerequisites

</div>

- You have installed the `virtctl` CLI.

- You have installed the OpenShift CLI (`oc`).

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create a `VirtualMachine` manifest for your VM and save it as a YAML file. For example, to create a minimal Red Hat Enterprise Linux (RHEL) VM, run the following command:

    ``` terminal
    $ virtctl create vm --name rhel-9-minimal --volume-import type:ds,src:openshift-virtualization-os-images/rhel9
    ```

2.  Review the `VirtualMachine` manifest for your VM:

    > [!NOTE]
    > This example manifest does not configure VM authentication.

    <div class="formalpara">

    <div class="title">

    Example manifest for a RHEL VM

    </div>

    ``` yaml
    apiVersion: kubevirt.io/v1
    kind: VirtualMachine
    metadata:
      name: rhel-9-minimal
    spec:
      dataVolumeTemplates:
      - metadata:
          name: imported-volume-mk4lj
        spec:
          sourceRef:
            kind: DataSource
            name: rhel9
            namespace: openshift-virtualization-os-images
          storage:
            resources: {}
      instancetype:
        inferFromVolume: imported-volume-mk4lj
        inferFromVolumeFailurePolicy: Ignore
      preference:
        inferFromVolume: imported-volume-mk4lj
        inferFromVolumeFailurePolicy: Ignore
      runStrategy: Always
      template:
        spec:
          domain:
            devices: {}
            memory:
              guest: 512Mi
            resources: {}
          terminationGracePeriodSeconds: 180
          volumes:
          - dataVolume:
              name: imported-volume-mk4lj
            name: imported-volume-mk4lj
    ```

    </div>

    - The VM name.

    - The boot source for the guest operating system.

    - The namespace for the boot source. Golden images are stored in the `openshift-virtualization-os-images` namespace.

    - The instance type is inferred from the selected `DataSource` object.

    - The preference is inferred from the selected `DataSource` object.

3.  Create a virtual machine by using the manifest file:

    ``` terminal
    $ oc create -f <vm_manifest_file>.yaml
    ```

4.  Optional: Start the virtual machine:

    ``` terminal
    $ virtctl start <vm_name>
    ```

</div>

# Uploading a virtual machine image by using the CLI

You can upload an operating system image by using the `virtctl` command-line tool. You can use an existing data volume or create a new data volume for the image.

<div>

<div class="title">

Prerequisites

</div>

- You must have an `ISO`, `IMG`, or `QCOW2` operating system image file.

- For best performance, compress the image file by using the [virt-sparsify](https://libguestfs.org/virt-sparsify.1.html) tool or the `xz` or `gzip` utilities.

- The client machine must be configured to trust the OpenShift Container Platform router’s certificate.

- You have installed the `virtctl` CLI.

- You have installed the OpenShift CLI (`oc`).

</div>

<div>

<div class="title">

Procedure

</div>

1.  Upload the image by running the `virtctl image-upload` command:

    ``` terminal
    $ virtctl image-upload dv <datavolume_name> \
      --size=<datavolume_size> \
      --image-path=</path/to/image>
    ```

    `<datavolume_name>`
    The name of the data volume.

    `<datavolume_size>`
    The size of the data volume. For example: `--size=500Mi`, `--size=1G`

    `</path/to/image>`
    The file path of the image.

    <div class="note">

    <div class="title">

    </div>

    - If you do not want to create a new data volume, omit the `--size` parameter and include the `--no-create` flag.

    - When uploading a disk image to a PVC, the PVC size must be larger than the size of the uncompressed virtual disk.

    - To allow insecure server connections when using HTTPS, use the `--insecure` parameter. When you use the `--insecure` flag, the authenticity of the upload endpoint is **not** verified.

    </div>

2.  Optional. To verify that a data volume was created, view all data volumes by running the following command:

    ``` terminal
    $ oc get dvs
    ```

</div>

# Additional resources

- [SSH access for virtual machines](../managing_vms/ssh/virt-accessing-vm-ssh.md#virt-accessing-vm-ssh)

- [Creating virtual machines from instance types](../creating_vm/virt-creating-vms-from-instance-types.md#virt-creating-vms-from-instance-types)
