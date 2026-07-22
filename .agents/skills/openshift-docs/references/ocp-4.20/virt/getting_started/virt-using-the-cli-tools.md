<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

You can manage OpenShift Virtualization resources by using the `virtctl` command-line tool. Virtual machine (VM) commands can also be used to manage virtual machine instances (VMIs) unless otherwise specified.

> [!NOTE]
> You can access and change VM disk images by using the `libguestfs` command-line tool. You deploy `libguestfs` by using the `virtctl libguestfs` command.

# Installing the virtctl binary on RHEL 9 or later, Linux, Windows, or macOS

You can download the `virtctl` binary by using the OpenShift Container Platform web console and then install it on Red Hat Enterprise Linux (RHEL) 9 or later, Linux, Windows, or macOS.

<div>

<div class="title">

Procedure

</div>

1.  Navigate to the **Virtualization → Overview** page in the web console.

2.  Click the **Download virtctl** link to download the `virtctl` binary for your operating system.

3.  Install `virtctl`:

    - For RHEL and other Linux operating systems:

      1.  Decompress the archive file:

          ``` terminal
          $ tar -xvf <virtctl-version-distribution.arch>.tar.gz
          ```

      2.  Run the following command to make the `virtctl` binary executable:

          ``` terminal
          $ chmod +x <path/virtctl-file-name>
          ```

      3.  Move the `virtctl` binary to a directory in your `PATH` environment variable.

          You can check your path by running the following command:

          ``` terminal
          $ echo $PATH
          ```

      4.  Set the `KUBECONFIG` environment variable:

          ``` terminal
          $ export KUBECONFIG=/home/<user>/clusters/current/auth/kubeconfig
          ```

    - For Windows:

      1.  Decompress the archive file.

      2.  Navigate the extracted folder hierarchy and double-click the `virtctl` executable file to install the client.

      3.  Move the `virtctl` binary to a directory in your `PATH` environment variable.

          You can check your path by running the following command:

          ``` terminal
          C:\> path
          ```

    - For macOS:

      1.  Decompress the archive file.

      2.  Move the `virtctl` binary to a directory in your `PATH` environment variable.

          You can check your path by running the following command:

          ``` terminal
          echo $PATH
          ```

</div>

# Installing the virtctl RPM package on RHEL 8

You can install the `virtctl` RPM package on Red Hat Enterprise Linux (RHEL) 8 by enabling the OpenShift Virtualization repository and then installing the `kubevirt-virtctl` RPM package.

<div>

<div class="title">

Prerequisites

</div>

- Each host in your cluster must be registered with Red Hat Subscription Manager (RHSM) and have an active OpenShift Container Platform subscription.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Enable the OpenShift Virtualization repository by using the `subscription-manager` CLI tool to run the following command:

    ``` terminal
    # subscription-manager repos --enable cnv-4.20-for-rhel-8-x86_64-rpms
    ```

2.  Install the `kubevirt-virtctl` RPM package by running the following command:

    ``` terminal
    # yum install kubevirt-virtctl
    ```

</div>

# virtctl information commands

You can use the following `virtctl` information commands to view information about the `virtctl` client.

| Command | Description |
|----|----|
| `virtctl version` | View the `virtctl` client and server versions. |
| `virtctl help` | View a list of `virtctl` commands. |
| `virtctl <command> -h|--help` | View a list of options for a specific command. |
| `virtctl options` | View a list of global command options for any `virtctl` command. |

Information commands

# VM information commands

You can use `virtctl` to view information about virtual machines (VMs) and virtual machine instances (VMIs).

| Command | Description |
|----|----|
| `virtctl fslist <vm_name>` | View the file systems available on a guest machine. |
| `virtctl guestosinfo <vm_name>` | View information about the operating systems on a guest machine. |
| `virtctl userlist <vm_name>` | View the logged-in users on a guest machine. |

VM information commands

# VM manifest creation commands

You can use the following `virtctl create` commands to create manifests for virtual machines, instance types, and preferences.

| Command | Description |
|----|----|
| `virtctl create vm` | Create a `VirtualMachine` (VM) manifest. |
| `virtctl create vm --name <vm_name>` | Create a VM manifest, specifying a name for the VM. |
| `virtctl create vm --user <user_name> --ssh-key|password-file=<value>` | Create a VM manifest with a cloud-init configuration to create the selected user and either add an SSH public key from the supplied string, or a password from a file. |
| `virtctl create vm --access-cred type:password,src:<secret>` | Create a VM manifest with a user and password combination injected from the selected secret. |
| `virtctl create vm --access-cred type:ssh,src:<secret>,user:<user_name>` | Create a VM manifest with an SSH public key injected from the selected secret. |
| `virtctl create vm --volume-sysprep src:<config_map>` | Create a VM manifest, specifying a config map to use as the sysprep volume. The config map must contain a valid answer file named `unattend.xml` or `autounattend.xml`. |
| `virtctl create vm --instancetype <instancetype_name>` | Create a VM manifest that uses an existing cluster-wide instance type. |
| `virtctl create vm --instancetype=virtualmachineinstancetype/<instancetype_name>` | Create a VM manifest that uses an existing namespaced instance type. |
| `virtctl create instancetype --cpu <cpu_value> --memory <memory_value> --name <instancetype_name>` | Create a manifest for a cluster-wide instance type. |
| `virtctl create instancetype --cpu <cpu_value> --memory <memory_value> --name <instancetype_name> --namespace <namespace_value>` | Create a manifest for a namespaced instance type. |
| `virtctl create preference --name <preference_name>` | Create a manifest for a cluster-wide VM preference, specifying a name for the preference. |
| `virtctl create preference --namespace <namespace_value>` | Create a manifest for a namespaced VM preference. |

VM manifest creation commands

# VM management commands

You can use the following `virtctl` commands to manage and migrate virtual machines (VMs) and VM instances (VMIs).

| Command | Description |
|----|----|
| `virtctl start <vm_name>` | Start a VM. |
| `virtctl start --paused <vm_name>` | Start a VM in a paused state. This option enables you to interrupt the boot process from the VNC console. |
| `virtctl stop <vm_name>` | Stop a VM. |
| `virtctl stop <vm_name> --grace-period 0 --force` | Force stop a VM. This option might cause data inconsistency or data loss. |
| `virtctl pause vm <vm_name>` | Pause a VM. The machine state is kept in memory. |
| `virtctl unpause vm <vm_name>` | Unpause a VM. |
| `virtctl migrate <vm_name>` | Migrate a VM. |
| `virtctl migrate-cancel <vm_name>` | Cancel a VM migration. |
| `virtctl restart <vm_name>` | Restart a VM. |

VM management commands

# VM connection commands

You use can use the following `virtctl` commands to expose ports and connect to virtual machines (VMs) and VM instances (VMIs).

<table>
<caption>VM connection commands</caption>
<colgroup>
<col style="width: 33%" />
<col style="width: 66%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Command</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>virtctl console &lt;vm_name&gt;</code></p></td>
<td style="text-align: left;"><p>Connect to the serial console of a VM.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>virtctl expose vm &lt;vm_name&gt; --name &lt;service_name&gt; --type &lt;ClusterIP|NodePort|LoadBalancer&gt; --port &lt;port&gt;</code></p></td>
<td style="text-align: left;"><p>Create a service that forwards a designated port of a VM and expose the service on the specified port of the node.</p>
<p>Example: <code>virtctl expose vm rhel9_vm --name rhel9-ssh --type NodePort --port 22</code></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>virtctl scp -i &lt;ssh_key&gt; &lt;file_name&gt; &lt;user_name&gt;@vm/&lt;vm_name&gt;</code></p></td>
<td style="text-align: left;"><p>Copy a file from your machine to a VM. This command uses the private key of an SSH key pair. The VM must be configured with the public key.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>virtctl scp -i &lt;ssh_key&gt; &lt;user_name@vm/&lt;vm_name&gt;:&lt;file_name&gt; .</code></p></td>
<td style="text-align: left;"><p>Copy a file from a VM to your machine. This command uses the private key of an SSH key pair. The VM must be configured with the public key.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>virtctl ssh -i &lt;ssh_key&gt; &lt;user_name&gt;@vm/&lt;vm_name&gt;</code></p></td>
<td style="text-align: left;"><p>Open an SSH connection with a VM. This command uses the private key of an SSH key pair. The VM must be configured with the public key.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>virtctl vnc &lt;vm_name&gt;</code></p></td>
<td style="text-align: left;"><p>Connect to the VNC console of a VM.</p>
<p>You must have <code>virt-viewer</code> installed.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>virtctl vnc --proxy-only=true &lt;vm_name&gt;</code></p></td>
<td style="text-align: left;"><p>Display the port number and connect manually to a VM by using any viewer through the VNC connection.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>virtctl vnc --port=&lt;port-number&gt; &lt;vm_name&gt;</code></p></td>
<td style="text-align: left;"><p>Specify a port number to run the proxy on the specified port, if that port is available.</p>
<p>If a port number is not specified, the proxy runs on a random port.</p></td>
</tr>
</tbody>
</table>

# VM export commands

Use `virtctl vmexport` commands to create, download, or delete a volume exported from a VM, VM snapshot, or persistent volume claim (PVC). Certain manifests also contain a header secret, which grants access to the endpoint to import a disk image in a format that OpenShift Virtualization can use.

<table>
<caption>VM export commands</caption>
<colgroup>
<col style="width: 33%" />
<col style="width: 66%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Command</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>virtctl vmexport create &lt;vmexport_name&gt; --vm|snapshot|pvc=&lt;object_name&gt;</code></p></td>
<td style="text-align: left;"><p>Create a <code>VirtualMachineExport</code> custom resource (CR) to export a volume from a VM, VM snapshot, or PVC.</p>
<ul>
<li><p><code>--vm</code>: Exports the PVCs of a VM.</p></li>
<li><p><code>--snapshot</code>: Exports the PVCs contained in a <code>VirtualMachineSnapshot</code> CR.</p></li>
<li><p><code>--pvc</code>: Exports a PVC.</p></li>
<li><p>Optional: <code>--ttl=1h</code> specifies the time to live. The default duration is 2 hours.</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>virtctl vmexport delete &lt;vmexport_name&gt;</code></p></td>
<td style="text-align: left;"><p>Delete a <code>VirtualMachineExport</code> CR manually.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>virtctl vmexport download &lt;vmexport_name&gt; --output=&lt;output_file&gt; --volume=&lt;volume_name&gt;</code></p></td>
<td style="text-align: left;"><p>Download the volume defined in a <code>VirtualMachineExport</code> CR.</p>
<ul>
<li><p><code>--output</code> specifies the file format. Example: <code>disk.img.gz</code>.</p></li>
<li><p><code>--volume</code> specifies the volume to download. This flag is optional if only one volume is available.</p></li>
</ul>
<p>Optional:</p>
<ul>
<li><p><code>--keep-vme</code> retains the <code>VirtualMachineExport</code> CR after download. The default behavior is to delete the <code>VirtualMachineExport</code> CR after download.</p></li>
<li><p><code>--insecure</code> enables an insecure HTTP connection.</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>virtctl vmexport download &lt;vmexport_name&gt; --vm|snapshot|pvc=&lt;object_name&gt; --output=&lt;output_file&gt; --volume=&lt;volume_name&gt;</code></p></td>
<td style="text-align: left;"><p>Create a <code>VirtualMachineExport</code> CR and then download the volume defined in the CR.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>virtctl vmexport download export --manifest</code></p></td>
<td style="text-align: left;"><p>Retrieve the manifest for an existing export. The manifest does not include the header secret.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>virtctl vmexport download export --manifest --vm=example</code></p></td>
<td style="text-align: left;"><p>Create a VM export for a VM example, and retrieve the manifest. The manifest does not include the header secret.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>virtctl vmexport download export --manifest --snap=example</code></p></td>
<td style="text-align: left;"><p>Create a VM export for a VM snapshot example, and retrieve the manifest. The manifest does not include the header secret.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>virtctl vmexport download export --manifest --include-secret</code></p></td>
<td style="text-align: left;"><p>Retrieve the manifest for an existing export. The manifest includes the header secret.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>virtctl vmexport download export --manifest --manifest-output-format=json</code></p></td>
<td style="text-align: left;"><p>Retrieve the manifest for an existing export in json format. The manifest does not include the header secret.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>virtctl vmexport download export --manifest --include-secret --output=manifest.yaml</code></p></td>
<td style="text-align: left;"><p>Retrieve the manifest for an existing export. The manifest includes the header secret and writes it to the file specified.</p></td>
</tr>
</tbody>
</table>

# Hot plug and hot unplug commands

You can use the following `virtctl` commands to add or remove resources from running virtual machines (VMs) and VM instances (VMIs).

<table>
<caption>Hot plug and hot unplug commands</caption>
<colgroup>
<col style="width: 33%" />
<col style="width: 66%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Command</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>virtctl addvolume &lt;vm_name&gt; --volume-name=&lt;datavolume_or_PVC&gt; [--persist] [--serial=&lt;label&gt;]</code></p></td>
<td style="text-align: left;"><p>Hot plug a data volume or persistent volume claim (PVC).</p>
<p>Optional:</p>
<ul>
<li><p><code>--persist</code> mounts the virtual disk permanently on a VM. <strong>This flag does not apply to VMIs.</strong></p></li>
<li><p><code>--serial=&lt;label&gt;</code> adds a label to the VM. If you do not specify a label, the default label is the data volume or PVC name.</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>virtctl removevolume &lt;vm_name&gt; --volume-name=&lt;virtual_disk&gt;</code></p></td>
<td style="text-align: left;"><p>Hot unplug a virtual disk.</p></td>
</tr>
</tbody>
</table>

# Image upload commands

You can use the following `virtctl image-upload` commands to upload a VM image to a data volume.

| Command | Description |
|----|----|
| `virtctl image-upload dv <datavolume_name> --image-path=</path/to/image> --no-create` | Upload a VM image to a data volume that already exists. |
| `virtctl image-upload dv <datavolume_name> --size=<datavolume_size> --image-path=</path/to/image>` | Upload a VM image to a new data volume of a specified requested size. |
| `virtctl image-upload dv <datavolume_name> --datasource --size=<datavolume_size> --image-path=</path/to/image>` | Upload a VM image to a new data volume and create an associated `DataSource` object for it. |

Image upload commands

# Deploying libguestfs by using virtctl

You can use the `virtctl guestfs` command to deploy an interactive container with `libguestfs-tools` and a persistent volume claim (PVC) attached to it.

<div>

<div class="title">

Procedure

</div>

- To deploy a container with `libguestfs-tools`, mount the PVC, and attach a shell to it, run the following command:

  ``` terminal
  $ virtctl guestfs -n <namespace> <pvc_name>
  ```

  > [!IMPORTANT]
  > The `<pvc_name>` argument is required. If you do not include it, an error message appears.

</div>

# Libguestfs and virtctl guestfs commands

`Libguestfs` tools help you access and modify virtual machine (VM) disk images. You can use `libguestfs` tools to view and edit files in a guest, clone and build virtual machines, and format and resize disks.

You can also use the `virtctl guestfs` command and its sub-commands to modify, inspect, and debug VM disks on a PVC. To see a complete list of possible sub-commands, enter `virt-` on the command line and press the Tab key. For example:

| Command | Description |
|----|----|
| `virt-edit -a /dev/vda /etc/motd` | Edit a file interactively in your terminal. |
| `virt-customize -a /dev/vda --ssh-inject root:string:<public key example>` | Inject an ssh key into the guest and create a login. |
| `virt-df -a /dev/vda -h` | See how much disk space is used by a VM. |
| `virt-customize -a /dev/vda --run-command 'rpm -qa > /rpm-list'` | See the full list of all RPMs installed on a guest by creating an output file containing the full list. |
| `virt-cat -a /dev/vda /rpm-list` | Display the output file list of all RPMs created using the `virt-customize -a /dev/vda --run-command 'rpm -qa > /rpm-list'` command in your terminal. |
| `virt-sysprep -a /dev/vda` | Seal a virtual machine disk image to be used as a template. |

By default, `virtctl guestfs` creates a session with everything needed to manage a VM disk. However, the command also supports several flag options if you want to customize the behavior:

<table>
<colgroup>
<col style="width: 42%" />
<col style="width: 57%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Flag Option</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>--h</code> or <code>--help</code></p></td>
<td style="text-align: left;"><p>Provides help for <code>guestfs</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>-n &lt;namespace&gt;</code> option with a <code>&lt;pvc_name&gt;</code> argument</p></td>
<td style="text-align: left;"><p>To use a PVC from a specific namespace.</p>
<p>If you do not use the <code>-n &lt;namespace&gt;</code> option, your current project is used. To change projects, use <code>oc project &lt;namespace&gt;</code>.</p>
<p>If you do not include a <code>&lt;pvc_name&gt;</code> argument, an error message appears.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>--image string</code></p></td>
<td style="text-align: left;"><p>Lists the <code>libguestfs-tools</code> container image.</p>
<p>You can configure the container to use a custom image by using the <code>--image</code> option.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>--kvm</code></p></td>
<td style="text-align: left;"><p>Indicates that <code>kvm</code> is used by the <code>libguestfs-tools</code> container.</p>
<p>By default, <code>virtctl guestfs</code> sets up <code>kvm</code> for the interactive container, which greatly speeds up the <code>libguest-tools</code> execution because it uses QEMU.</p>
<p>If a cluster does not have any <code>kvm</code> supporting nodes, you must disable <code>kvm</code> by setting the option <code>--kvm=false</code>.</p>
<p>If not set, the <code>libguestfs-tools</code> pod remains pending because it cannot be scheduled on any node.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>--pull-policy string</code></p></td>
<td style="text-align: left;"><p>Shows the pull policy for the <code>libguestfs</code> image.</p>
<p>You can also overwrite the image’s pull policy by setting the <code>pull-policy</code> option.</p></td>
</tr>
</tbody>
</table>

The command also checks if a PVC is in use by another pod, in which case an error message appears. However, once the `libguestfs-tools` process starts, the setup cannot avoid a new pod using the same PVC. You must verify that there are no active `virtctl guestfs` pods before starting the VM that accesses the same PVC.

> [!NOTE]
> The `virtctl guestfs` command accepts only a single PVC attached to the interactive pod.

# Additional resources

- [Red Hat Ansible Automation Hub](https://console.redhat.com/ansible/automation-hub)

- [`libguestfs`](https://libguestfs.org)
