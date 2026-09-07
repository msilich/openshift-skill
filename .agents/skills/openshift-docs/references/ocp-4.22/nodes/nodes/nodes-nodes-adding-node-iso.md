<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

You can add worker nodes to on-premise clusters by using the OpenShift CLI (`oc`) to generate an ISO image, which can then be used to boot one or more nodes in your target cluster. This process can be used regardless of how you installed your cluster.

You can add one or more nodes at a time while customizing each node with more complex configurations, such as static network configuration, or you can specify only the MAC address of each node. Any required configurations that are not specified during ISO generation are retrieved from the target cluster and applied to the new nodes.

> [!NOTE]
> `Machine` or `BareMetalHost` resources are not automatically created after a node has been successfully added to the cluster.

Preflight validation checks are also performed when booting the ISO image to inform you of failure-causing issues before you attempt to boot each node.

Supported platforms
The following platforms are supported for this method of adding nodes:

- `baremetal`

- `vsphere`

- `nutanix`

- `none`

Supported architectures
The following architecture combinations have been validated to work when adding worker nodes using this process:

- `amd64` worker nodes on `amd64` or `arm64` clusters

- `arm64` worker nodes on `amd64` or `arm64` clusters

- `s390x` worker nodes on `s390x` clusters

- `ppc64le` worker nodes on `ppc64le` clusters

Adding nodes to your cluster
You can add nodes with this method in the following two ways:

- Adding one or more nodes using a configuration file.

  You can specify configurations for one or more nodes in the `nodes-config.yaml` file before running the `oc adm node-image create` command. This is useful if you want to add more than one node at a time, or if you are specifying complex configurations.

- Adding a single node using only command flags.

  You can add a node by running the `oc adm node-image create` command with flags to specify your configurations. This is useful if you want to add only a single node at a time, and have only simple configurations to specify for that node.

# Adding one or more nodes using a configuration file

You can add one or more nodes to your cluster by using the `nodes-config.yaml` file to specify configurations for the new nodes.

<div>

<div class="title">

Prerequisites

</div>

- You have installed the OpenShift CLI (`oc`)

- You have installed the Rsync utility

- You have an active connection to your target cluster

- You have a kubeconfig file available

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create a new YAML file that contains configurations for the nodes you are adding and is named `nodes-config.yaml`. You must provide a MAC address for each new node.

    In the following example file, two new workers are described with an initial static network configuration:

    <div class="formalpara">

    <div class="title">

    Example `nodes-config.yaml` file

    </div>

    ``` yaml
    hosts:
    - hostname: extra-worker-1
      rootDeviceHints:
       deviceName: /dev/sda
      interfaces:
       - macAddress: 00:00:00:00:00:00
         name: eth0
      networkConfig:
       interfaces:
         - name: eth0
           type: ethernet
           state: up
           mac-address: 00:00:00:00:00:00
           ipv4:
             enabled: true
             address:
               - ip: 192.168.122.2
                 prefix-length: 23
             dhcp: false
    - hostname: extra-worker-2
      rootDeviceHints:
       deviceName: /dev/sda
      interfaces:
       - macAddress: 00:00:00:00:00:02
         name: eth0
      networkConfig:
       interfaces:
         - name: eth0
           type: ethernet
           state: up
           mac-address: 00:00:00:00:00:02
           ipv4:
             enabled: true
             address:
               - ip: 192.168.122.3
                 prefix-length: 23
             dhcp: false
    ```

    </div>

2.  Generate the ISO image by running the following command:

    ``` terminal
    $ oc adm node-image create
    ```

    > [!IMPORTANT]
    > In order for the `create` command to fetch a release image that matches the target cluster version, you must specify a valid pull secret. You can specify the pull secret either by using the `--registry-config` flag or by setting the `REGISTRY_AUTH_FILE` environment variable beforehand.

    > [!NOTE]
    > If the directory of the `nodes-config.yaml` file is not specified by using the `--dir` flag, the tool looks for the file in the current directory.

3.  Verify that a new `node.<arch>.iso` file is present in the asset directory. The asset directory is your current directory, unless you specified a different one when creating the ISO image.

4.  Boot the selected node with the generated ISO image.

5.  Track progress of the node creation by running the following command:

    ``` terminal
    $ oc adm node-image monitor --ip-addresses <ip_addresses>
    ```

    where:

    `<ip_addresses>`
    Specifies a list of the IP addresses of the nodes that are being added.

    > [!NOTE]
    > If reverse DNS entries are not available for your node, the `oc adm node-image monitor` command skips checks for pending certificate signing requests (CSRs). If these checks are skipped, you must manually check for CSRs by running the `oc get csr` command.

6.  Approve the CSRs by running the following command for each CSR:

    ``` terminal
    $ oc adm certificate approve <csr_name>
    ```

</div>

# Adding a node with command flags

You can add a single node to your cluster by using command flags to specify configurations for the new node.

<div>

<div class="title">

Prerequisites

</div>

- You have installed the OpenShift CLI (`oc`)

- You have installed the Rsync utility

- You have an active connection to your target cluster

- You have a kubeconfig file available

</div>

<div>

<div class="title">

Procedure

</div>

1.  Generate the ISO image by running the following command. The MAC address must be specified using a command flag. See the "Cluster configuration reference" section for more flags that you can use with this command.

    ``` terminal
    $ oc adm node-image create --mac-address=<mac_address>
    ```

    where:

    `<mac_address>`
    Specifies the MAC address of the node that is being added.

    > [!IMPORTANT]
    > In order for the `create` command to fetch a release image that matches the target cluster version, you must specify a valid pull secret. You can specify the pull secret either by using the `--registry-config` flag or by setting the `REGISTRY_AUTH_FILE` environment variable beforehand.

    > [!TIP]
    > To see additional flags that can be used to configure your node, run the following `oc adm node-image create --help` command.

2.  Verify that a new `node.<arch>.iso` file is present in the asset directory. The asset directory is your current directory, unless you specified a different one when creating the ISO image.

3.  Boot the node with the generated ISO image.

4.  Track progress of the node creation by running the following command:

    ``` terminal
    $ oc adm node-image monitor --ip-addresses <ip_address>
    ```

    where:

    `<ip_address>`
    Specifies a list of the IP addresses of the nodes that are being added.

    > [!NOTE]
    > If reverse DNS entries are not available for your node, the `oc adm node-image monitor` command skips checks for pending certificate signing requests (CSRs). If these checks are skipped, you must manually check for CSRs by running the `oc get csr` command.

5.  Approve the pending CSRs by running the following command for each CSR:

    ``` terminal
    $ oc adm certificate approve <csr_name>
    ```

</div>

# Cluster configuration reference

When creating the ISO image, configurations are retrieved from the target cluster and are applied to the new nodes. You can override these configurations by specifying new values in either the `nodes-config.yaml` file or any flags you add to the `oc adm node-image create` command before you create the ISO image.

YAML file parameters
Configuration parameters that can be specified in the `nodes-config.yaml` file are described in the following table:

<table style="width:100%;">
<caption><code>nodes-config.yaml</code> parameters</caption>
<colgroup>
<col style="width: 44%" />
<col style="width: 33%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Parameter</th>
<th style="text-align: left;">Description</th>
<th style="text-align: left;">Values</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><pre><code>hosts:</code></pre></td>
<td style="text-align: left;"><p>Host configuration.</p></td>
<td style="text-align: left;"><p>An array of host configuration objects.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>hosts:
  hostname:</code></pre></td>
<td style="text-align: left;"><p>Hostname. Overrides the hostname obtained from either the Dynamic Host Configuration Protocol (DHCP) or a reverse DNS lookup. Each host must have a unique hostname supplied by one of these methods, although configuring a hostname through this parameter is optional.</p></td>
<td style="text-align: left;"><p>String.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>hosts:
  interfaces:</code></pre></td>
<td style="text-align: left;"><p>Provides a table of the name and MAC address mappings for the interfaces on the host. If a <code>NetworkConfig</code> section is provided in the <code>nodes-config.yaml</code> file, this table must be included and the values must match the mappings provided in the <code>NetworkConfig</code> section.</p></td>
<td style="text-align: left;"><p>An array of host configuration objects.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>hosts:
  interfaces:
    name:</code></pre></td>
<td style="text-align: left;"><p>The name of an interface on the host.</p></td>
<td style="text-align: left;"><p>String.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>hosts:
  interfaces:
    macAddress:</code></pre></td>
<td style="text-align: left;"><p>The MAC address of an interface on the host.</p></td>
<td style="text-align: left;"><p>A MAC address such as the following example: <code>00-B0-D0-63-C2-26</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>hosts:
  rootDeviceHints:</code></pre></td>
<td style="text-align: left;"><p>Enables provisioning of the Red Hat Enterprise Linux CoreOS (RHCOS) image to a particular device. The node-adding tool examines the devices in the order it discovers them, and compares the discovered values with the hint values. It uses the first discovered device that matches the hint value.</p></td>
<td style="text-align: left;"><p>A dictionary of key-value pairs. For more information, see "Root device hints" in the "Setting up the environment for an OpenShift installation" page.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>hosts:
  rootDeviceHints:
    deviceName:</code></pre></td>
<td style="text-align: left;"><p>The name of the device the RHCOS image is provisioned to.</p></td>
<td style="text-align: left;"><p>String.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>hosts:
  networkConfig:</code></pre></td>
<td style="text-align: left;"><p>The host network definition. The configuration must match the Host Network Management API defined in the <a href="https://nmstate.io/">nmstate documentation</a>.</p></td>
<td style="text-align: left;"><p>A dictionary of host network configuration objects.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>cpuArchitecture:</code></pre></td>
<td style="text-align: left;"><p>Optional. Specifies the architecture of the nodes you are adding. This parameter allows you to override the default value from the cluster when required.</p></td>
<td style="text-align: left;"><p>String.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>sshKey:</code></pre></td>
<td style="text-align: left;"><p>Optional. The file containing the SSH key to authenticate access to your cluster machines.</p></td>
<td style="text-align: left;"><p>String.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>bootArtifactsBaseURL:</code></pre></td>
<td style="text-align: left;"><p>Optional. Specifies the URL of the server to upload Preboot Execution Environment (PXE) assets to when you are generating an iPXE script. You must also set the <code>--pxe</code> flag to generate PXE assets instead of an ISO image.</p></td>
<td style="text-align: left;"><p>String.</p></td>
</tr>
</tbody>
</table>

Command flag options
You can use command flags with the `oc adm node-image create` command to configure the nodes you are creating.

The following table describes command flags that are not limited to the single-node use case:

<table style="width:100%;">
<caption>General command flags</caption>
<colgroup>
<col style="width: 44%" />
<col style="width: 33%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Flag</th>
<th style="text-align: left;">Description</th>
<th style="text-align: left;">Values</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>--certificate-authority</code></p></td>
<td style="text-align: left;"><p>The path to a certificate authority bundle to use when communicating with the managed container image registries. If the <code>--insecure</code> flag is used, this flag is ignored.</p></td>
<td style="text-align: left;"><p>String</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>--dir</code></p></td>
<td style="text-align: left;"><p>The path containing the configuration file, if provided. This path is also used to store the generated artifacts.</p></td>
<td style="text-align: left;"><p>String</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>--insecure</code></p></td>
<td style="text-align: left;"><p>Allows push and pull operations to registries to be made over HTTP.</p></td>
<td style="text-align: left;"><p>Boolean</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>-o</code>, <code>--output-name</code></p></td>
<td style="text-align: left;"><p>The name of the generated output image.</p></td>
<td style="text-align: left;"><p>String</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>p</code>, <code>--pxe</code></p></td>
<td style="text-align: left;"><p>Generates Preboot Execution Environment (PXE) assets instead of a bootable ISO file.</p>
<p>When this flag is set, you can also use the <code>bootArtifactsBaseURL</code> parameter in the <code>nodes-config.yaml</code> file to specify URL of the server you will upload PXE assets to.</p></td>
<td style="text-align: left;"><p>Boolean</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>-a</code>, <code>--registry-config</code></p></td>
<td style="text-align: left;"><p>The path to your registry credentials. Alternatively, you can specify the <code>REGISTRY_AUTH_FILE</code> environment variable. The default paths are <code>${XDG_RUNTIME_DIR}/containers/auth.json</code>, <code>/run/containers/${UID}/auth.json</code>, <code>${XDG_CONFIG_HOME}/containers/auth.json</code>, <code>${DOCKER_CONFIG}</code>, <code>~/.docker/config.json</code>, <code>~/.dockercfg.</code> The order can be changed through the deprecated <code>REGISTRY_AUTH_PREFERENCE</code> environment variable to a "docker" value, in order to prioritize Docker credentials over Podman.</p></td>
<td style="text-align: left;"><p>String</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>-r</code>, <code>--report</code></p></td>
<td style="text-align: left;"><p>Generates a report of the node creation process regardless of whether the process is successful or not. If you do not specify this flag, reports are generated only in cases of failure.</p></td>
<td style="text-align: left;"><p>Boolean</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>--skip-verification</code></p></td>
<td style="text-align: left;"><p>An option to skip verifying the integrity of the retrieved content. This is not recommended, but might be necessary when importing images from older image registries. Bypass verification only if the registry is known to be trustworthy.</p></td>
<td style="text-align: left;"><p>Boolean</p></td>
</tr>
</tbody>
</table>

The following table describes command flags that can be used only when creating a single node:

| Flag | Description | Values |
|----|----|----|
| `-c`, `--cpu-architecture` | The CPU architecture to be used to install the node. This flag can be used to create only a single node, and the `--mac-address` flag must be defined. | String |
| `--hostname` | The hostname to be set for the node. This flag can be used to create only a single node, and the `--mac-address` flag must be defined. | String |
| `-m`, `--mac-address` | The MAC address used to identify the host to apply configurations to. This flag can be used to create only a single node, and the `--mac-address` flag must be defined. | String |
| `--network-config-path` | The path to a YAML file containing NMState configurations to be applied to the node. This flag can be used to create only a single node, and the `--mac-address` flag must be defined. | String |
| `--root-device-hint` | A hint for specifying the storage location for the image root filesystem. The accepted format is `<hint_name>:<value>`. This flag can be used to create only a single node, and the `--mac-address` flag must be defined. | String |
| `-k`, `--ssh-key-path` | The path to the SSH key used to access the node. This flag can be used to create only a single node, and the `--mac-address` flag must be defined. | String |

Single-node only command flags

# Additional resources

- [Root device hints](../../installing/installing_bare_metal/ipi/ipi-install-installation-workflow.md#root-device-hints_ipi-install-installation-workflow)
