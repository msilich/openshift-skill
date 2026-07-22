<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

You can manually generate a configuration ISO by using the `openshift-install` program. Attach the configuration ISO to your preinstalled target host to complete the deployment.

# Deploying a single-node OpenShift cluster using the openshift-install program

You can use the `openshift-install` program to configure and deploy a host that you preinstalled with an image-based installation. To configure the target host with site-specific details, you must create the following resources:

- The `install-config.yaml` installation manifest

- The `image-based-config.yaml` manifest

The `openshift-install` program uses these resources to generate a configuration ISO that you attach to the preinstalled target host to complete the deployment.

> [!NOTE]
> For more information about the specifications for the `image-based-config.yaml` manifest, see "Reference specifications for the image-based-config.yaml manifest".

<div>

<div class="title">

Prerequisites

</div>

- You preinstalled a host with single-node OpenShift using an image-based installation.

- You downloaded the latest version of the `openshift-install` program.

- You created a pull secret to authenticate pull requests. For more information, see "Using image pull secrets".

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create a working directory by running the following:

    ``` terminal
    $ mkdir <working_directory>
    ```

    where `<working_directory>` is the name of your working directory, for example `ibi-config-iso-workdir`.

2.  Create the installation manifest:

    1.  Create a YAML file that defines the `install-config` manifest, as in the following example:

        ``` yaml
        apiVersion: v1
        metadata:
          name: sno-cluster-name
        baseDomain: host.example.com
        compute:
          - architecture: amd64
            hyperthreading: Enabled
            name: worker
            replicas: 0
        controlPlane:
          architecture: amd64
          hyperthreading: Enabled
          name: master
          replicas: 1
        networking:
          machineNetwork:
          - cidr: 192.168.200.0/24
          #- cidr: fd01::/64
        platform:
          none: {}
        fips: false
        cpuPartitioningMode: "AllNodes"
        pullSecret: '{"auths":{"<your_pull_secret>"}}}'
        sshKey: 'ssh-rsa <your_ssh_pub_key>'
        ```

        \+ For dual-stack networking, you can specify both IPv4 and IPv6 CIDRs using a list format in the `machineNetwork` field. The first CIDR in the list is the primary address family and must match the primary address family of the seed cluster.

        > [!IMPORTANT]
        > If your cluster deployment requires a proxy configuration, you must do the following:
        >
        > - Create a seed image from a seed cluster featuring a proxy configuration. The proxy configurations do not have to match.
        >
        > - Configure the `machineNetwork` field in your installation manifest.

    2.  Save the file in your working directory.

3.  Optional. Create a configuration template in your working directory by running the following command:

    ``` terminal
    $ openshift-install image-based create config-template --dir ibi-config-iso-workdir/
    ```

    Example output:

    ``` terminal
    INFO Config-Template created in: ibi-config-iso-workdir
    ```

    The command creates the `image-based-config.yaml` configuration template in your working directory:

    ``` yaml
    #
    # Note: This is a sample ImageBasedConfig file showing
    # which fields are available to aid you in creating your
    # own image-based-config.yaml file.
    #
    apiVersion: v1beta1
    kind: ImageBasedConfig
    metadata:
      name: example-image-based-config
    additionalNTPSources:
      - 0.rhel.pool.ntp.org
      - 1.rhel.pool.ntp.org
    hostname: change-to-hostname
    releaseRegistry: quay.io
    # networkConfig contains the network configuration for the host in NMState format.
    # See https://nmstate.io/examples.html for examples.
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
    ```

4.  Edit your configuration file:

    Example `image-based-config.yaml` file:

    ``` yaml
    #
    # Note: This is a sample ImageBasedConfig file showing
    # which fields are available to aid you in creating your
    # own image-based-config.yaml file.
    #
    apiVersion: v1beta1
    kind: ImageBasedConfig
    metadata:
      name: sno-cluster-name
    additionalNTPSources:
      - 0.rhel.pool.ntp.org
      - 1.rhel.pool.ntp.org
    hostname: host.example.com
    releaseRegistry: quay.io
    # networkConfig contains the network configuration for the host in NMState format.
    # See https://nmstate.io/examples.html for examples.
    networkConfig:
        interfaces:
          - name: ens1f0
            type: ethernet
            state: up
            ipv4:
              enabled: true
              dhcp: false
              auto-dns: false
              address:
                - ip: 192.168.200.25
                  prefix-length: 24
            ipv6:
              enabled: false
        dns-resolver:
          config:
            server:
              - 192.168.15.47
              - 192.168.15.48
        routes:
          config:
          - destination: 0.0.0.0/0
            metric: 150
            next-hop-address: 192.168.200.254
            next-hop-interface: ens1f0
    ```

5.  Create the configuration ISO in your working directory by running the following command:

    ``` terminal
    $ openshift-install image-based create config-image --dir ibi-config-iso-workdir/
    ```

    Example output:

    ``` terminal
    INFO Adding NMConnection file <ens1f0.nmconnection>
    INFO Consuming Install Config from target directory
    INFO Consuming Image-based Config ISO configuration from target directory
    INFO Config-Image created in: ibi-config-iso-workdir/auth
    ```

    View the output in the working directory:

    Example output:

    ``` terminal
    ibi-config-iso-workdir/
    ├── auth
    │   ├── kubeadmin-password
    │   └── kubeconfig
    └── imagebasedconfig.iso
    ```

6.  Attach the `imagebasedconfig.iso` to the preinstalled host using your preferred method and restart the host to complete the configuration process and deploy the cluster.

</div>

<div class="formalpara">

<div class="title">

Verification

</div>

When the configuration process completes on the host, access the cluster to verify its status.

</div>

1.  Export the `kubeconfig` environment variable to your kubeconfig file by running the following command:

    ``` terminal
    $ export KUBECONFIG=ibi-config-iso-workdir/auth/kubeconfig
    ```

2.  Verify that the cluster is responding by running the following command:

    ``` terminal
    $ oc get nodes
    ```

    Example output:

    ``` terminal
    NAME                                         STATUS   ROLES                  AGE     VERSION
    node/sno-cluster-name.host.example.com       Ready    control-plane,master   5h15m   v1.33.4
    ```

<div>

<div class="title">

Additional resources

</div>

- [Using image pull secrets](../../../openshift_images/managing_images/using-image-pull-secrets.md)

- [Reference specifications for the `image-based-installation-config.yaml` manifest](ibi-edge-image-based-install-standalone.md#ibi-installer-configuration-config_ibi-edge-image-based-install)

</div>

## Reference specifications for the image-based-config.yaml manifest

The following content describes the specifications for the `image-based-config.yaml` manifest.

The `openshift-install` program uses the `image-based-config.yaml` manifest to create a site-specific configuration ISO for image-based deployments of single-node OpenShift.

| Specification | Type | Description |
|----|----|----|
| `hostname` | `string` | Define the name of the node for the single-node OpenShift cluster. |

Required specifications

<table>
<caption>Optional specifications</caption>
<colgroup>
<col style="width: 28%" />
<col style="width: 14%" />
<col style="width: 57%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Specification</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>networkConfig</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Specifies networking configurations for the host, for example:</p>
<div class="sourceCode" id="cb1"><pre class="sourceCode yaml"><code class="sourceCode yaml"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a><span class="fu">networkConfig</span><span class="kw">:</span></span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a><span class="at">    </span><span class="fu">interfaces</span><span class="kw">:</span></span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a><span class="at">      </span><span class="kw">-</span><span class="at"> </span><span class="fu">name</span><span class="kw">:</span><span class="at"> ens1f0</span></span>
<span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a><span class="at">        </span><span class="fu">type</span><span class="kw">:</span><span class="at"> ethernet</span></span>
<span id="cb1-5"><a href="#cb1-5" aria-hidden="true" tabindex="-1"></a><span class="at">        </span><span class="fu">state</span><span class="kw">:</span><span class="at"> up</span></span>
<span id="cb1-6"><a href="#cb1-6" aria-hidden="true" tabindex="-1"></a><span class="at">        ...</span></span></code></pre></div>
<p>If you require static networking, you must install the <code>nmstatectl</code> library on the host that creates the live installation ISO. For further information about defining network configurations by using <code>nmstate</code>, see <a href="https://nmstate.io/">nmstate.io</a>.</p>
<div class="important">
<div class="title">
&#10;</div>
<p>The name of the interface must match the actual NIC name as shown in the operating system.</p>
</div></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>additionalNTPSources</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Specifies a list of NTP sources for all cluster hosts. These NTP sources are added to any existing NTP sources in the cluster. You can use the hostname or IP address for the NTP source.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>releaseRegistry</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Specifies the container image registry that you used for the release image of the seed cluster.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>nodeLabels</code></p></td>
<td style="text-align: left;"><p><code>map[string]string</code></p></td>
<td style="text-align: left;"><p>Specifies custom node labels for the single-node OpenShift node, for example:</p>
<div class="sourceCode" id="cb2"><pre class="sourceCode yaml"><code class="sourceCode yaml"><span id="cb2-1"><a href="#cb2-1" aria-hidden="true" tabindex="-1"></a><span class="fu">nodeLabels</span><span class="kw">:</span></span>
<span id="cb2-2"><a href="#cb2-2" aria-hidden="true" tabindex="-1"></a><span class="at">  </span><span class="fu">node-role.kubernetes.io/edge</span><span class="kw">:</span><span class="at"> </span><span class="ch">true</span></span>
<span id="cb2-3"><a href="#cb2-3" aria-hidden="true" tabindex="-1"></a><span class="at">  </span><span class="fu">environment</span><span class="kw">:</span><span class="at"> production</span></span></code></pre></div></td>
</tr>
</tbody>
</table>

# Configuring resources for extra manifests

You can optionally define additional resources in an image-based deployment for single-node OpenShift clusters.

Create the additional resources in an `extra-manifests` folder in the same working directory that has the `install-config.yaml` and `image-based-config.yaml` manifests.

> [!NOTE]
> Filenames for additional resources in the `extra-manifests` directory must not exceed 30 characters. Longer filenames might cause deployment failures.

The following example shows how to create a resource in the `extra-manifests` folder of your working directory to add an single-root I/O virtualization (SR-IOV) network to the deployment.

> [!NOTE]
> If you add more than one extra manifest, and the manifests must be applied in a specific order, you must prefix the filenames of the manifests with numbers that represent the required order. For example, `00-namespace.yaml`, `01-sriov-extra-manifest.yaml`, and so on.

<div>

<div class="title">

Prerequisites

</div>

- You created a working directory with the `install-config.yaml` and `image-based-config.yaml` manifests

</div>

<div>

<div class="title">

Procedure

</div>

1.  Go to your working directory and create the `extra-manifests` folder by running the following command:

    ``` terminal
    $ mkdir extra-manifests
    ```

2.  Create the `SriovNetworkNodePolicy` and `SriovNetwork` resources in the `extra-manifests` folder:

    1.  Create a YAML file that defines the resources, as shown in the following example:

        > [!NOTE]
        > If the cluster nodes include Intel vRAN Boost (VRB1 or VRB2) hardware, you can include a `SriovVrbClusterConfig` resource in the extra manifests to configure the hardware.

        ``` yaml
        apiVersion: sriovnetwork.openshift.io/v1
        kind: SriovNetworkNodePolicy
        metadata:
          name: "example-sriov-node-policy"
          namespace: openshift-sriov-network-operator
        spec:
          deviceType: vfio-pci
          isRdma: false
          nicSelector:
            pfNames: [ens1f0]
          nodeSelector:
            node-role.kubernetes.io/master: ""
          mtu: 1500
          numVfs: 8
          priority: 99
          resourceName: example-sriov-node-policy
        ---
        apiVersion: sriovnetwork.openshift.io/v1
        kind: SriovNetwork
        metadata:
          name: "example-sriov-network"
          namespace: openshift-sriov-network-operator
        spec:
          ipam: |-
            {
            }
          linkState: auto
          networkNamespace: sriov-namespace
          resourceName: example-sriov-node-policy
          spoofChk: "on"
          trust: "off"
        ---
        apiVersion: sriovvrb.intel.com/v1
        kind: SriovVrbClusterConfig
        metadata:
          name: config
          namespace: vran-acceleration-operators
        spec:
          priority: 1
          nodeSelector:
            kubernetes.io/hostname: worker-node
          acceleratorSelector:
            pciAddress: 0000:07:00.0
          drainSkip: true
          physicalFunction:
            pfDriver: vfio-pci
            vfDriver: vfio-pci
            vfAmount: 2
            bbDevConfig:
              vrb2:
                pfMode: false
                numVfBundles: 2
                maxQueueSize: 1024
                downlink4G:
                  aqDepthLog2: 4
                  numAqsPerGroups: 16
                  numQueueGroups: 0
                uplink4G:
                  aqDepthLog2: 4
                  numAqsPerGroups: 16
                  numQueueGroups: 0
                downlink5G:
                  aqDepthLog2: 4
                  numAqsPerGroups: 16
                  numQueueGroups: 4
                uplink5G:
                  aqDepthLog2: 4
                  numAqsPerGroups: 16
                  numQueueGroups: 4
                qfft:
                  aqDepthLog2: 4
                  numAqsPerGroups: 16
                  numQueueGroups: 4
                qmld:
                  aqDepthLog2: 4
                  numAqsPerGroups: 64
                  numQueueGroups: 4
        ```

</div>

<div>

<div class="title">

Verification

</div>

- When you create the configuration ISO, you can view the reference to the extra manifests in the `.openshift_install_state.json` file in your working directory:

  ``` json
   "*configimage.ExtraManifests": {
          "FileList": [
              {
                  "Filename": "extra-manifests/sriov-extra-manifest.yaml",
                  "Data": "YXBFDFFD..."
              }
          ]
      }
  ```

</div>
