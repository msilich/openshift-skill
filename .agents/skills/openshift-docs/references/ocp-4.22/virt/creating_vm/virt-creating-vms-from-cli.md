<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

You can create virtual machines (VMs) from the command line by editing or creating a `VirtualMachine` manifest. You can also create a VM from an operating system image that you import, upload, build into a container disk, or clone from an existing persistent volume claim (PVC).

> [!NOTE]
> You can also create VMs from instance types by using the OpenShift Container Platform web console.

> [!IMPORTANT]
> You must install the QEMU guest agent on VMs created from operating system images that are not provided by Red Hat.

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
            devices:
              video:
                type: virtio
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

    - `name: rhel-9-minimal` specifies the name of the VM.

    - `name: rhel9` specifies the boot source for the guest operating system in the `sourceRef` section.

    - `namespace: openshift-virtualization-os-images` specifies the namespace for the boot source. Golden images are stored in the `openshift-virtualization-os-images` namespace.

    - `instancetype: inferFromVolume: imported-volume-mk4lj` specifies the instance type inferred from the selected `DataSource` object.

    - `preference: inferFromVolume: imported-volume-mk4lj` specifies that the preference is inferred from the selected `DataSource` object.

    - `type: virtio` specifies the use of a custom video device (a VirtIO device in this example) to enable hardware graphics acceleration. Enabling a custom video device is in Technology Preview for OpenShift Virtualization 4.22.

3.  Create a virtual machine by using the manifest file:

    ``` terminal
    $ oc create -f <vm_manifest_file>.yaml
    ```

4.  Optional: Start the virtual machine:

    ``` terminal
    $ virtctl start <vm_name>
    ```

</div>

# Creating a VM from an image on a web page by using the CLI

You can create a virtual machine (VM) from an image on a web page by using the command line.

When the VM is created, the data volume with the image is imported into persistent storage.

<div>

<div class="title">

Prerequisites

</div>

- You must have access credentials for the web page that contains the image.

- You have installed the `virtctl` CLI.

- You have installed the OpenShift CLI (`oc`).

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create a `VirtualMachine` manifest for your VM and save it as a YAML file. For example, to create a minimal Red Hat Enterprise Linux (RHEL) VM from an image on a web page, run the following command:

    ``` terminal
    $ virtctl create vm --name vm-rhel-9 --instancetype u1.small --preference rhel.9 --volume-import type:http,url:https://example.com/rhel9.qcow2,size:10Gi
    ```

2.  Review the `VirtualMachine` manifest for your VM:

    ``` yaml
    apiVersion: kubevirt.io/v1
    kind: VirtualMachine
    metadata:
      name: vm-rhel-9
    spec:
      dataVolumeTemplates:
      - metadata:
          name: imported-volume-6dcpf
        spec:
          source:
            http:
              url: https://example.com/rhel9.qcow2
          storage:
            resources:
              requests:
                storage: 10Gi
      instancetype:
        name: u1.small
      preference:
        name: rhel.9
      runStrategy: Always
      template:
        spec:
          domain:
            devices: {}
            resources: {}
          terminationGracePeriodSeconds: 180
          volumes:
          - dataVolume:
              name: imported-volume-6dcpf
            name: imported-volume-6dcpf
    ```

    - `metadata.name` defines the VM name.

    - `spec.dataVolumeTemplates.metadata.name` defines the data volume name.

    - `spec.dataVolumeTemplates.spec.source.http.url` defines the URL of the image.

    - `spec.dataVolumeTemplates.spec.storage.resources.requests.storage` defines the size of the storage requested for the data volume.

    - `spec.instancetype.name` defines the instance type to use to control resource sizing of the VM.

    - `spec.preference.name` defines the preference to use.

3.  Create the VM by running the following command:

    ``` terminal
    $ oc create -f <vm_manifest_file>.yaml
    ```

    The `oc create` command creates the data volume and the VM. The CDI controller creates an underlying PVC with the correct annotation and the import process begins. When the import is complete, the data volume status changes to `Succeeded`. You can start the VM.

    Data volume provisioning happens in the background, so there is no need to monitor the process.

</div>

<div>

<div class="title">

Verification

</div>

1.  The importer pod downloads the image from the specified URL and stores it on the provisioned persistent volume. View the status of the importer pod:

    ``` terminal
    $ oc get pods
    ```

2.  Monitor the status of the data volume:

    ``` terminal
    $ oc get dv <data_volume_name>
    ```

    If the provisioning is successful, the data volume phase is `Succeeded`.

    Example output:

    ``` terminal
    NAME                    PHASE       PROGRESS   RESTARTS   AGE
    imported-volume-6dcpf   Succeeded   100.0%                18s
    ```

3.  Verify that provisioning is complete and that the VM has started by accessing its serial console:

    ``` terminal
    $ virtctl console <vm_name>
    ```

    If the VM is running and the serial console is accessible, the output looks as follows:

    ``` terminal
    Successfully connected to vm-rhel-9 console. The escape sequence is ^]
    ```

</div>

# Generalizing a VM image

You can generalize a Red Hat Enterprise Linux (RHEL) image to remove all system-specific configuration data before you use the image to create a boot source image, a preconfigured snapshot of a virtual machine (VM). You can use a boot source image to deploy new VMs.

You can generalize a RHEL VM by using the `virtctl`, `guestfs`, and `virt-sysprep` tools.

<div>

<div class="title">

Prerequisites

</div>

- You have a RHEL virtual machine (VM) to use as a base VM.

- You have installed the OpenShift CLI (`oc`).

- You have installed the `virtctl` tool.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Stop the RHEL VM if it is running, by entering the following command:

    ``` terminal
    $ virtctl stop <my_vm_name>
    ```

2.  Optional: Clone the virtual machine to avoid losing the data from your original VM. You can then generalize the cloned VM.

3.  Retrieve the `dataVolume` that stores the root filesystem for the VM by running the following command:

    ``` terminal
    $ oc get vm <my_vm_name> -o jsonpath="{.spec.template.spec.volumes}{'\n'}"
    ```

    Example output:

    ``` terminal
    [{"dataVolume":{"name":"<my_vm_volume>"},"name":"rootdisk"},{"cloudInitNoCloud":{...}]
    ```

4.  Retrieve the persistent volume claim (PVC) that matches the listed `dataVolume` by running the followimg command:

    ``` terminal
    $ oc get pvc
    ```

    Example output:

    ``` terminal
    NAME            STATUS   VOLUME  CAPACITY   ACCESS MODES  STORAGECLASS     AGE
    <my_vm_volume> Bound  …
    ```

    > [!NOTE]
    > If your cluster configuration does not enable you to clone a VM, to avoid losing the data from your original VM, you can clone the VM PVC to a data volume instead. You can then use the cloned PVC to create a boot source image.
    >
    > If you are creating a boot source image by cloning a PVC, continue with the next steps, using the cloned PVC.

5.  Deploy a new interactive container with `libguestfs-tools` and attach the PVC to it by running the following command:

    ``` terminal
    $ virtctl guestfs <my-vm-volume> --uid 107
    ```

    This command opens a shell for you to run the next command.

6.  Remove all configurations specific to your system by running the following command:

    ``` terminal
    $ virt-sysprep -a disk.img
    ```

7.  In the OpenShift Container Platform console, click **Virtualization** → **Catalog**.

8.  Click **Add volume**.

9.  In the **Add volume** window:

    1.  From the **Source type** list, select **Use existing Volume**.

    2.  From the **Volume project** list, select your project.

    3.  From the **Volume name** list, select the correct PVC.

    4.  In the **Volume name** field, enter a name for the new boot source image.

    5.  From the **Preference** list, select the RHEL version you are using.

    6.  From the **Default Instance Type** list, select the instance type with the correct CPU and memory requirements for the version of RHEL you selected previously.

    7.  Heterogeneous clusters only: From the **Architecture** list, select the architecture that corresponds with the selected volume.

    8.  Click **Save**.

</div>

<div class="formalpara">

<div class="title">

Result

</div>

The new volume appears in the **Select volume to boot from** list. This is your new boot source image. You can use this volume to create new VMs.

</div>

# Creating a Windows VM

You can create a Windows virtual machine (VM) by uploading a Windows image to a persistent volume claim (PVC) and then cloning the PVC when you create a VM by using the OpenShift Container Platform web console.

> [!IMPORTANT]
> You must install VirtIO drivers on Windows VMs. Download VirtIO drivers only from official Red Hat sources.

<div>

<div class="title">

Prerequisites

</div>

- You created a Windows installation DVD or USB with the Windows Media Creation Tool. See [Create Windows 10 installation media](https://www.microsoft.com/en-us/software-download/windows10) in the Microsoft documentation.

- You created an `autounattend.xml` answer file. See [Answer files (unattend.xml)](https://docs.microsoft.com/en-us/windows-hardware/manufacture/desktop/update-windows-settings-and-scripts-create-your-own-answer-file-sxs) in the Microsoft documentation.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Upload the Windows image as a new PVC:

    1.  Navigate to **Storage** → **PersistentVolumeClaims** in the web console.

    2.  Click **Create PersistentVolumeClaim** → **With Data upload form**.

    3.  Browse to the Windows image and select it.

    4.  Enter the PVC name, select the storage class and size and then click **Upload**.

        The Windows image is uploaded to a PVC.

2.  Configure a new VM by cloning the uploaded PVC:

    1.  Navigate to **Virtualization** → **Catalog**.

    2.  Select a Windows template tile and click **Customize VirtualMachine**.

    3.  Select **Clone (clone PVC)** from the **Disk source** list.

    4.  Select the PVC project, the Windows image PVC, and the disk size.

3.  Apply the answer file to the VM:

    1.  Click **Customize VirtualMachine parameters**.

    2.  On the **Sysprep** section of the **Scripts** tab, click **Edit**.

    3.  Browse to the `autounattend.xml` answer file and click **Save**.

4.  Set the run strategy of the VM:

    1.  Clear **Start this VirtualMachine after creation** so that the VM does not start immediately.

    2.  Click **Create VirtualMachine**.

    3.  On the **YAML** tab, replace `running:false` with `runStrategy: RerunOnFailure` and click **Save**.

5.  Click the Options menu ![kebab](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABsAAAAjCAIAAADqn+bCAAAACXBIWXMAAA7EAAAOxAGVKw4bAAAA+0lEQVRIie2WMQqEMBBFJ47gUXRBLyBYqbUXULCx9CR2XsAb6AlUEM9kpckW7obdZhwWYWHXX/3i8TPJZEKEUgpOlXFu3JX4V4kmB2qaZhgGKSUiZlkWxzEBC84N9zxv27bdO47Tti0Bs3at4wBgXVca/lJnfN/XPggCGmadIwAsywIAiGhZFk1ydy2EYJKgGCqK4vZUVVU0zKpxnmftp2mi4S/1GhG1N82DMWNNYVmW4zgqpRAxTVMa5t4evlg11nXd9/1eY57nSZIQMKtG13WllLu3bbvrOgJmdUbHwfur8Xniqw6Hh5UYRdGDNowwDA+WvP4UV+JPJ94B1gKUWcTOCT0AAAAASUVORK5CYII=) and select **Control** → **Start**.

    The VM boots from the `sysprep` disk containing the `autounattend.xml` answer file.

</div>

## Generalizing a Windows VM image

You can generalize a Windows operating system image to remove all system-specific configuration data before you use the image to create a new virtual machine (VM).

Before generalizing the VM, you must ensure the `sysprep` tool cannot detect an answer file after the unattended Windows installation.

<div>

<div class="title">

Prerequisites

</div>

- A running Windows VM with the QEMU guest agent installed.

</div>

<div>

<div class="title">

Procedure

</div>

1.  In the OpenShift Container Platform console, click **Virtualization** → **VirtualMachines**.

2.  Select a Windows VM to open the **VirtualMachine details** page.

3.  Click **Configuration** → **Disks**.

4.  Click the Options menu ![kebab](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABsAAAAjCAIAAADqn+bCAAAACXBIWXMAAA7EAAAOxAGVKw4bAAAA+0lEQVRIie2WMQqEMBBFJ47gUXRBLyBYqbUXULCx9CR2XsAb6AlUEM9kpckW7obdZhwWYWHXX/3i8TPJZEKEUgpOlXFu3JX4V4kmB2qaZhgGKSUiZlkWxzEBC84N9zxv27bdO47Tti0Bs3at4wBgXVca/lJnfN/XPggCGmadIwAsywIAiGhZFk1ydy2EYJKgGCqK4vZUVVU0zKpxnmftp2mi4S/1GhG1N82DMWNNYVmW4zgqpRAxTVMa5t4evlg11nXd9/1eY57nSZIQMKtG13WllLu3bbvrOgJmdUbHwfur8Xniqw6Hh5UYRdGDNowwDA+WvP4UV+JPJ94B1gKUWcTOCT0AAAAASUVORK5CYII=) beside the `sysprep` disk and select **Detach**.

5.  Click **Detach**.

6.  Rename `C:\Windows\Panther\unattend.xml` to avoid detection by the `sysprep` tool.

7.  Start the `sysprep` program by running the following command:

    ``` terminal
    %WINDIR%\System32\Sysprep\sysprep.exe /generalize /shutdown /oobe /mode:vm
    ```

8.  After the `sysprep` tool completes, the Windows VM shuts down. The disk image of the VM is now available to use as an installation image for Windows VMs.

</div>

<div class="formalpara">

<div class="title">

Result

</div>

You can now specialize the VM.

</div>

## Specializing a Windows VM image

Specializing a Windows virtual machine (VM) configures the computer-specific information from a generalized Windows image onto the VM.

<div>

<div class="title">

Prerequisites

</div>

- You must have a generalized Windows disk image.

- You must create an `unattend.xml` answer file. See the [Microsoft documentation](https://docs.microsoft.com/en-us/windows-hardware/manufacture/desktop/update-windows-settings-and-scripts-create-your-own-answer-file-sxs?view=windows-11) for details.

</div>

<div>

<div class="title">

Procedure

</div>

1.  In the OpenShift Container Platform console, click **Virtualization** → **Catalog**.

2.  Select a Windows template and click **Customize VirtualMachine**.

3.  Select **PVC (clone PVC)** from the **Disk source** list.

4.  Select the PVC project and PVC name of the generalized Windows image.

5.  Click **Customize VirtualMachine parameters**.

6.  Click the **Scripts** tab.

7.  In the **Sysprep** section, click **Edit**, browse to the `unattend.xml` answer file, and click **Save**.

8.  Click **Create VirtualMachine**.

</div>

<div class="formalpara">

<div class="title">

Result

</div>

During the initial boot, Windows uses the `unattend.xml` answer file to specialize the VM. The VM is now ready to use.

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

# Building and uploading a container disk

You can build a virtual machine (VM) image into a container disk and upload it to a registry.

The size of a container disk is limited by the maximum layer size of the registry where the container disk is hosted.

You create a VM from a container disk by performing the following steps:

1.  Build an operating system image into a container disk and upload it to your container registry.

2.  If your container registry does not have TLS, configure your environment to disable TLS for your registry.

3.  Create a VM with the container disk as the disk source by using the OpenShift Container Platform web console or the command line.

> [!IMPORTANT]
> If the container disks are large, the I/O traffic might increase and cause worker nodes to be unavailable. You can perform the following tasks to reclaim resources:
>
> - Prune `DeploymentConfig` objects.
>
> - Configure garbage collection.

> [!NOTE]
> For [Red Hat Quay](https://access.redhat.com/documentation/en-us/red_hat_quay/), you can change the maximum layer size by editing the YAML configuration file that is created when Red Hat Quay is first deployed.

<div>

<div class="title">

Prerequisites

</div>

- You must have `podman` installed.

- You must have a QCOW2 or RAW image file.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create a Dockerfile to build the VM image into a container image. The VM image must be owned by QEMU, which has a UID of `107`, and placed in the `/disk/` directory inside the container. Permissions for the `/disk/` directory must then be set to `0440`.

    The following example uses the Red Hat Universal Base Image (UBI) to handle these configuration changes in the first stage, and uses the minimal `scratch` image in the second stage to store the result:

    ``` terminal
    $ cat > Dockerfile << EOF
    FROM registry.access.redhat.com/ubi8/ubi:latest AS builder
    ADD --chown=107:107 <vm_image>.qcow2 /disk/ //
    RUN chmod 0440 /disk/*

    FROM scratch
    COPY --from=builder /disk/* /disk/
    EOF
    ```

    where:

    `<vm_image>`
    Specifies the image in either QCOW2 or RAW format. If you use a remote image, replace `<vm_image>.qcow2` with the complete URL.

2.  Build and tag the container:

    ``` terminal
    $ podman build -t <registry>/<container_disk_name>:latest .
    ```

3.  Push the container image to the registry:

    ``` terminal
    $ podman push <registry>/<container_disk_name>:latest
    ```

</div>

# Disabling TLS for a container registry

You can disable TLS (transport layer security) for one or more container registries by editing the `insecureRegistries` field of the `HyperConverged` custom resource.

<div>

<div class="title">

Prerequisites

</div>

- You have installed the OpenShift CLI (`oc`).

</div>

<div>

<div class="title">

Procedure

</div>

1.  Open the `HyperConverged` CR in your default editor by running the following command:

    ``` terminal
    $ oc edit hyperconvergeds.v1beta1.hco.kubevirt.io kubevirt-hyperconverged -n openshift-cnv
    ```

2.  Add a list of insecure registries to the `spec.storageImport.insecureRegistries` field.

    Example `HyperConverged` custom resource:

    ``` yaml
    apiVersion: hco.kubevirt.io/v1beta1
    kind: HyperConverged
    metadata:
      name: kubevirt-hyperconverged
      namespace: openshift-cnv
    spec:
      storageImport:
        insecureRegistries:
          - "private-registry-example-1:5000"
          - "private-registry-example-2:5000"
    ```

    Replace the examples in the `insecureRegistries` list with valid registry hostnames.

</div>

# Creating a VM from a container disk by using the CLI

You can create a virtual machine (VM) from a container disk by using the command line.

<div>

<div class="title">

Prerequisites

</div>

- You must have access credentials for the container registry that contains the container disk.

- You have installed the `virtctl` CLI.

- You have installed the OpenShift CLI (`oc`).

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create a `VirtualMachine` manifest for your VM and save it as a YAML file. For example, to create a minimal Red Hat Enterprise Linux (RHEL) VM from a container disk, run the following command:

    ``` terminal
    $ virtctl create vm --name vm-rhel-9 --instancetype u1.small --preference rhel.9 --volume-containerdisk src:registry.redhat.io/rhel9/rhel-guest-image:9.5
    ```

2.  Review the `VirtualMachine` manifest for your VM:

    ``` yaml
    apiVersion: kubevirt.io/v1
    kind: VirtualMachine
    metadata:
      name: vm-rhel-9
    spec:
      instancetype:
        name: u1.small
      preference:
        name: rhel.9
      runStrategy: Always
      template:
        metadata:
          creationTimestamp: null
        spec:
          domain:
            devices: {}
            resources: {}
          terminationGracePeriodSeconds: 180
          volumes:
          - containerDisk:
              image: registry.redhat.io/rhel9/rhel-guest-image:9.5
            name: vm-rhel-9-containerdisk-0
    ```

    - `metadata.name` defines the VM name.

    - `spec.instancetype.name` defines the instance type to use to control resource sizing of the VM.

    - `spec.preference.name` defines the preference to use.

    - `spec.template.spec.volumes.containerDisk.image` defines the URL of the container disk.

3.  Create the VM by running the following command:

    ``` terminal
    $ oc create -f <vm_manifest_file>.yaml
    ```

</div>

<div>

<div class="title">

Verification

</div>

1.  Monitor the status of the VM:

    ``` terminal
    $ oc get vm <vm_name>
    ```

    If the provisioning is successful, the VM status is `Running`. Example output:

    ``` terminal
    NAME        AGE   STATUS    READY
    vm-rhel-9   18s   Running   True
    ```

2.  Verify that provisioning is complete and that the VM has started by accessing its serial console:

    ``` terminal
    $ virtctl console <vm_name>
    ```

    If the VM is running and the serial console is accessible, the output looks as follows:

    ``` terminal
    Successfully connected to vm-rhel-9 console. The escape sequence is ^]
    ```

</div>

# About cloning

When cloning a data volume, the Containerized Data Importer (CDI) chooses one of the Container Storage Interface (CSI) clone methods: CSI volume cloning or smart cloning. Both methods are efficient but have certain requirements. If the requirements are not met, the CDI uses host-assisted cloning.

Host-assisted cloning is the slowest and least efficient method of cloning, but it has fewer requirements than either of the other two cloning methods.

## CSI volume cloning

Container Storage Interface (CSI) cloning uses CSI driver features to more efficiently clone a source data volume.

CSI volume cloning has the following requirements:

- The CSI driver that backs the storage class of the persistent volume claim (PVC) must support volume cloning.

- For provisioners not recognized by the CDI, the corresponding storage profile must have the `cloneStrategy` set to CSI Volume Cloning.

- The source and target PVCs must have the same storage class and volume mode.

- If you create the data volume, you must have permission to create the `datavolumes/source` resource in the source namespace.

- The source volume must not be in use.

## Smart cloning

When a Container Storage Interface (CSI) plugin with snapshot capabilities is available, the Containerized Data Importer (CDI) creates a persistent volume claim (PVC) from a snapshot, which then allows efficient cloning of additional PVCs.

Smart cloning has the following requirements:

- A snapshot class associated with the storage class must exist.

- The source and target PVCs must have the same storage class and volume mode.

- If you create the data volume, you must have permission to create the `datavolumes/source` resource in the source namespace.

- The source volume must not be in use.

## Host-assisted cloning

When the requirements for neither Container Storage Interface (CSI) volume cloning nor smart cloning have been met, host-assisted cloning is used as a fallback method. Host-assisted cloning is less efficient than either of the two other cloning methods.

Host-assisted cloning uses a source pod and a target pod to copy data from the source volume to the target volume. The target persistent volume claim (PVC) is annotated with the fallback reason that explains why host-assisted cloning has been used, and an event is created.

Example PVC target annotation:

``` yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  annotations:
    cdi.kubevirt.io/cloneFallbackReason: The volume modes of source and target are incompatible
    cdi.kubevirt.io/clonePhase: Succeeded
    cdi.kubevirt.io/cloneType: copy
```

Example event:

``` terminal
NAMESPACE   LAST SEEN   TYPE      REASON                    OBJECT                              MESSAGE
test-ns     0s          Warning   IncompatibleVolumeModes   persistentvolumeclaim/test-target   The volume modes of source and target are incompatible
```

# Creating a VM from a PVC by using the CLI

You can create a virtual machine (VM) by cloning the persistent volume claim (PVC) of an existing VM by using the command line.

You can clone a PVC by using one of the following options:

- Cloning a PVC to a new data volume.

  This method creates a data volume whose lifecycle is independent of the original VM. Deleting the original VM does not affect the new data volume or its associated PVC.

- Cloning a PVC by creating a `VirtualMachine` manifest with a `dataVolumeTemplates` stanza.

  This method creates a data volume whose lifecycle is dependent on the original VM. Deleting the original VM deletes the cloned data volume and its associated PVC.

## Optimizing clone Performance at scale in OpenShift Data Foundation

When you use OpenShift Data Foundation, the storage profile configures the default cloning strategy as `csi-clone`. However, this method has limitations, as shown in the following link.

After a certain number of clones are created from a persistent volume claim (PVC), a background flattening process begins, which can significantly reduce clone creation performance at scale.

To improve performance when creating hundreds of clones from a single source PVC, use the `VolumeSnapshot` cloning method instead of the default `csi-clone` strategy.

<div>

<div class="title">

Procedure

</div>

1.  Create a `VolumeSnapshot` custom resource (CR) of the source image by using the following content:

    ``` yaml
    apiVersion: snapshot.storage.k8s.io/v1
    kind: VolumeSnapshot
    metadata:
      name: golden-volumesnapshot
      namespace: golden-ns
    spec:
      volumeSnapshotClassName: ocs-storagecluster-rbdplugin-snapclass
      source:
        persistentVolumeClaimName: golden-snap-source
    ```

2.  Add the `spec.source.snapshot` stanza to reference the `VolumeSnapshot` as the source for the `DataVolume clone`:

    ``` yaml
    spec:
      source:
        snapshot:
          namespace: golden-ns
          name: golden-volumesnapshot
    ```

</div>

## Cloning a PVC to a data volume

You can clone the persistent volume claim (PVC) of an existing virtual machine (VM) disk to a data volume by using the command line.

You create a data volume that references the original source PVC. The lifecycle of the new data volume is independent of the original VM. Deleting the original VM does not affect the new data volume or its associated PVC.

Cloning between different volume modes is supported for host-assisted cloning, such as cloning from a block persistent volume (PV) to a file system PV, as long as the source and target PVs belong to the `kubevirt` content type.

> [!NOTE]
> Smart-cloning is faster and more efficient than host-assisted cloning because it uses snapshots to clone PVCs. Smart-cloning is supported by storage providers that support snapshots, such as Red Hat OpenShift Data Foundation.
>
> Cloning between different volume modes is not supported for smart-cloning.

<div>

<div class="title">

Prerequisites

</div>

- You have installed the OpenShift CLI (`oc`).

- The VM with the source PVC must be powered down.

- If you clone a PVC to a different namespace, you must have permissions to create resources in the target namespace.

- Additional prerequisites for smart-cloning:

  - Your storage provider must support snapshots.

  - The source and target PVCs must have the same storage provider and volume mode.

  - The value of the `driver` key of the `VolumeSnapshotClass` object must match the value of the `provisioner` key of the `StorageClass` object as shown in the following example:

    Example `VolumeSnapshotClass` object:

    ``` yaml
    kind: VolumeSnapshotClass
    apiVersion: snapshot.storage.k8s.io/v1
    driver: openshift-storage.rbd.csi.ceph.com
    # ...
    ```

    Example `StorageClass` object:

    ``` yaml
    kind: StorageClass
    apiVersion: storage.k8s.io/v1
    # ...
    provisioner: openshift-storage.rbd.csi.ceph.com
    ```

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create a `DataVolume` manifest as shown in the following example:

    ``` yaml
    apiVersion: cdi.kubevirt.io/v1beta1
    kind: DataVolume
    metadata:
      name: <datavolume>
    spec:
      source:
        pvc:
          namespace: "<source_namespace>"
          name: "<my_vm_disk>"
      storage: {}
    ```

    where:

    `<datavolume>`
    Specifies the name of the new data volume.

    `<source_namespace>`
    Specifies the namespace of the source PVC.

    `<my_vm_disk>`
    Specifies the name of the source PVC.

2.  Create the data volume by running the following command:

    ``` terminal
    $ oc create -f <datavolume>.yaml
    ```

    > [!NOTE]
    > Data volumes prevent a VM from starting before the PVC is prepared. You can create a VM that references the new data volume while the PVC is being cloned.

</div>

## Creating a VM from a cloned PVC by using a data volume template

You can create a virtual machine (VM) that clones the persistent volume claim (PVC) of an existing VM by using a data volume template. This method creates a data volume whose lifecycle is independent on the original VM.

<div>

<div class="title">

Prerequisites

</div>

- The VM with the source PVC must be powered down.

- You have installed the `virtctl` CLI.

- You have installed the OpenShift CLI (`oc`).

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create a `VirtualMachine` manifest for your VM and save it as a YAML file, for example:

    ``` terminal
    $ virtctl create vm --name rhel-9-clone --volume-import type:pvc,src:my-project/imported-volume-q5pr9
    ```

2.  Review the `VirtualMachine` manifest for your VM:

    ``` yaml
    apiVersion: kubevirt.io/v1
    kind: VirtualMachine
    metadata:
      name: rhel-9-clone
    spec:
      dataVolumeTemplates:
      - metadata:
          name: imported-volume-h4qn8
        spec:
          source:
            pvc:
              name: imported-volume-q5pr9
              namespace: my-project
          storage:
            resources: {}
      instancetype:
        inferFromVolume: imported-volume-h4qn8
        inferFromVolumeFailurePolicy: Ignore
      preference:
        inferFromVolume: imported-volume-h4qn8
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
              name: imported-volume-h4qn8
            name: imported-volume-h4qn8
    ```

    - `metadata.name` defines the VM name.

    - `spec.dataVolumeTemplates.spec.source.pvc.name` defines the name of the source PVC.

    - `spec.dataVolumeTemplates.spec.source.pvc.namespace` defines the namespace of the source PVC.

    - `spec.instancetype.inferFromVolume` defines that if the PVC source has appropriate labels, the instance type is inferred from the selected `DataSource` object.

    - `spec.preference.inferFromVolume` defines that if the PVC source has appropriate labels, the preference is inferred from the selected `DataSource` object.

3.  Create the virtual machine with the PVC-cloned data volume:

    ``` terminal
    $ oc create -f <vm_manifest_file>.yaml
    ```

</div>

# Supported custom video device types

When creating a virtual machine (VM), you can configure a custom video device type to override the default video configuration.

Configuring a custom video device allows you to specify different video devices, based on your guest operating system requirements and performance needs.

> [!IMPORTANT]
> Custom video device support is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.
>
> For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

Using a custom video device provides several advantages:

Performance
Certain video devices provide better performance than the default configuration. For example, VirtIO is a more efficient video device on AMD/x86_64 architecture than legacy VGA.

Resolution flexibility
With some video device types, you can set custom display resolutions.

Memory efficiency
Some video types are more memory efficient for headless or console-only operations.

You can configure the following video device types:

- VirtIO: provides improved performance, and hardware-accelerated video decoding and encoding by offloading tasks to the host. Recommended for modern guest operating systems with available `VirtIO` drivers.

- VGA: the standard for analog video display (default on AMD/x86_64 with BIOS).

- Bochs: an emulated graphics adapter that provides a simple interface for guest operating systems to manage display settings (default on AMD/x86_64 with EFI).

- Cirrus: a legacy video device that provides stable video output.

- ramfb: a simple, unaccelerated virtual display device primarily used in the QEMU emulator, and useful for ARM architecture.

| Architecture | Boot mode | Default type | Supported types |
|----|----|----|----|
| AMD/x86_64 | BIOS | `vga` | `virtio`, `vga`, `bochs`, `cirrus`, `ramfb` |
| AMD/x86_64 | EFI | `bochs` | `virtio`, `vga`, `bochs`, `cirrus`, `ramfb` |
| ARM64 | BIOS/EFI | `virtio` | `virtio`, `ramfb` |
| s390x | BIOS/EFI | `virtio` | `virtio` |

Video device support by architecture

# Additional resources

- [SSH access for virtual machines](../managing_vms/ssh/virt-accessing-vm-ssh.md#virt-accessing-vm-ssh)

- [Instance types](virt-creating-vms-from-instance-types.md#virt-creating-vms-from-instance-types)

- [Installing the QEMU guest agent](../managing_vms/virt-installing-qemu-guest-agent.md#virt-installing-qemu-guest-agent)

- [Installing VirtIO drivers on Windows VMs](../managing_vms/virt-install-virtio-drivers-on-windows-vms.md#virt-install-virtio-drivers-on-windows-vms)

- [Red Hat VirtIO drivers download page](https://access.redhat.com/downloads/content/479/virtio-win/noarch/package-latest)

- [How to check virtio-win drivers version on Windows guest](https://access.redhat.com/solutions/764103)

- [Installing and updating VirtIO drivers for Windows virtual machines](https://access.redhat.com/solutions/6957701)

- [Sysprep (Generalize) a Windows installation](https://docs.microsoft.com/en-us/windows-hardware/manufacture/desktop/sysprep--generalize--a-windows-installation)

- [Configuration pass of Windows Setup (generalize)](https://docs.microsoft.com/en-us/windows-hardware/manufacture/desktop/generalize)

- [Configuration pass of Windows Setup (specialize)](https://docs.microsoft.com/en-us/windows-hardware/manufacture/desktop/specialize)

- [Cloning a VM by using the web console](virt-creating-vms-web.md#virt-cloning-vm-wizard-web_virt-creating-vms-web)

- [Managing automatic boot source updates](../storage/virt-automatic-bootsource-updates.md#virt-automatic-bootsource-updates)

- [Setting a default cloning strategy using a storage profile](../storage/virt-configuring-storage-profile.md#virt-customizing-storage-profile-default-cloning-strategy_virt-configuring-storage-profile)

- [Volume cloning](https://docs.redhat.com/en/documentation/red_hat_openshift_data_foundation/latest/html/managing_and_allocating_storage_resources/volume-cloning_rhodf#volume-cloning_rhodf)

- [Pruning objects to reclaim resources](../../applications/pruning-objects.md#pruning-deployments_pruning-objects)

- [Configuring garbage collection for containers and images](../../nodes/nodes/nodes-nodes-garbage-collection.md#nodes-nodes-garbage-collection-configuring_nodes-nodes-configuring)

- [CSI volume snapshots](../../storage/container_storage_interface/persistent-storage-csi-snapshots.md#persistent-storage-csi-snapshots)
