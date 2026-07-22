<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Before you deploy an OpenShift Container Platform cluster using the Agent-based Installer, you provide parameters to customize your cluster and the platform that hosts it.

When you create the `install-config.yaml` and `agent-config.yaml` files, you must provide values for the required parameters, and you can use the optional parameters to customize your cluster further.

# Available installation configuration parameters

To customize your cluster installation, configuration parameters are available to use in the `install-config.yaml` file.

The following tables specify the required and optional installation configuration parameters that you can set as part of the Agent-based installation process.

These values are specified in the `install-config.yaml` file.

> [!IMPORTANT]
> These settings are used for installation only, and cannot be changed after installation.

## Required configuration parameters

Required installation configuration parameters are described in the following table:

<table>
<caption>Required parameters</caption>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Parameter</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><pre><code>apiVersion:</code></pre></td>
<td style="text-align: left;"><p>The API version for the <code>install-config.yaml</code> content. The current version is <code>v1</code>. The installation program might also support older API versions.</p>
<p><strong>Value:</strong> String</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>baseDomain:</code></pre></td>
<td style="text-align: left;"><p>The base domain of your cloud provider. The base domain is used to create routes to your OpenShift Container Platform cluster components. The full DNS name for your cluster is a combination of the <code>baseDomain</code> and <code>metadata.name</code> parameter values that uses the <code>&lt;metadata.name&gt;.&lt;baseDomain&gt;</code> format.</p>
<p><strong>Value:</strong> A fully-qualified domain or subdomain name, such as <code>example.com</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>metadata:</code></pre></td>
<td style="text-align: left;"><p>Kubernetes resource <code>ObjectMeta</code>, from which only the <code>name</code> parameter is consumed.</p>
<p><strong>Value:</strong> Object</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>metadata:
  name:</code></pre></td>
<td style="text-align: left;"><p>The name of the cluster. DNS records for the cluster are all subdomains of <code>{{.metadata.name}}.{}</code>. The cluster name is set to <code>agent-cluster</code> when you do not provide the <code>metadata.name</code> parameter through either the <code>install-config.yaml</code> or <code>agent-config.yaml</code> files. For example, installations that only use ZTP manifests do not provide the <code>metadata.name</code> parameter.</p>
<p><strong>Value:</strong> String of lowercase letters, hyphens (<code>-</code>), and periods (<code>.</code>), such as <code>dev</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>platform:</code></pre></td>
<td style="text-align: left;"><p>The configuration for the specific platform upon which to perform the installation: <code>baremetal</code>, <code>external</code>, <code>none</code>, <code>vsphere</code>, or <code>nutanix</code>.</p>
<p><strong>Value:</strong> Object</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>pullSecret:</code></pre></td>
<td style="text-align: left;"><p>Get a <a href="https://console.redhat.com/openshift/install/pull-secret">pull secret from Red Hat OpenShift Cluster Manager</a> to authenticate downloading container images for OpenShift Container Platform components from services such as Quay.io.</p>
<p><strong>Value:</strong></p>
<div class="sourceCode" id="cb7"><pre class="sourceCode json"><code class="sourceCode json"><span id="cb7-1"><a href="#cb7-1" aria-hidden="true" tabindex="-1"></a><span class="fu">{</span></span>
<span id="cb7-2"><a href="#cb7-2" aria-hidden="true" tabindex="-1"></a>   <span class="dt">&quot;auths&quot;</span><span class="fu">:{</span></span>
<span id="cb7-3"><a href="#cb7-3" aria-hidden="true" tabindex="-1"></a>      <span class="dt">&quot;cloud.openshift.com&quot;</span><span class="fu">:{</span></span>
<span id="cb7-4"><a href="#cb7-4" aria-hidden="true" tabindex="-1"></a>         <span class="dt">&quot;auth&quot;</span><span class="fu">:</span><span class="st">&quot;b3Blb=&quot;</span><span class="fu">,</span></span>
<span id="cb7-5"><a href="#cb7-5" aria-hidden="true" tabindex="-1"></a>         <span class="dt">&quot;email&quot;</span><span class="fu">:</span><span class="st">&quot;you@example.com&quot;</span></span>
<span id="cb7-6"><a href="#cb7-6" aria-hidden="true" tabindex="-1"></a>      <span class="fu">},</span></span>
<span id="cb7-7"><a href="#cb7-7" aria-hidden="true" tabindex="-1"></a>      <span class="dt">&quot;quay.io&quot;</span><span class="fu">:{</span></span>
<span id="cb7-8"><a href="#cb7-8" aria-hidden="true" tabindex="-1"></a>         <span class="dt">&quot;auth&quot;</span><span class="fu">:</span><span class="st">&quot;b3Blb=&quot;</span><span class="fu">,</span></span>
<span id="cb7-9"><a href="#cb7-9" aria-hidden="true" tabindex="-1"></a>         <span class="dt">&quot;email&quot;</span><span class="fu">:</span><span class="st">&quot;you@example.com&quot;</span></span>
<span id="cb7-10"><a href="#cb7-10" aria-hidden="true" tabindex="-1"></a>      <span class="fu">}</span></span>
<span id="cb7-11"><a href="#cb7-11" aria-hidden="true" tabindex="-1"></a>   <span class="fu">}</span></span>
<span id="cb7-12"><a href="#cb7-12" aria-hidden="true" tabindex="-1"></a><span class="fu">}</span></span></code></pre></div></td>
</tr>
</tbody>
</table>

## Network configuration parameters

You can customize your installation configuration based on the requirements of your existing network infrastructure. For example, you can expand the IP address block for the cluster network or configure different IP address blocks than the defaults.

Consider the following information before you configure network parameters for your cluster:

- If you use the Red Hat OpenShift Networking OVN-Kubernetes network plugin, both IPv4 and IPv6 address families are supported.

- If you deployed nodes in an OpenShift Container Platform cluster with a network that supports both IPv4 and non-link-local IPv6 addresses, configure your cluster to use a dual-stack network.

  - For clusters configured for dual-stack networking, both IPv4 and IPv6 traffic must use the same network interface as the default gateway. This ensures that in a multiple network interface controller (NIC) environment, a cluster can detect what NIC to use based on the available network interface. For more information, see "OVN-Kubernetes IPv6 and dual-stack limitations" in *About the OVN-Kubernetes network plugin*.

  - To prevent network connectivity issues, do not install a single-stack IPv4 cluster on a host that supports dual-stack networking.

If you configure your cluster to use both IP address families, review the following requirements:

- Both IP families must use the same network interface for the default gateway.

- Both IP families must have the default gateway.

- You must specify IPv4 and IPv6 addresses in the same order for all network configuration parameters. For example, in the following configuration, IPv4 addresses are listed before IPv6 addresses:

  ``` yaml
  networking:
    clusterNetwork:
    - cidr: 10.128.0.0/14
      hostPrefix: 23
    - cidr: fd00:10:128::/56
      hostPrefix: 64
    serviceNetwork:
    - 172.30.0.0/16
    - fd00:172:16::/112
  ```

<table>
<caption>Network parameters</caption>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Parameter</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><pre><code>networking:</code></pre></td>
<td style="text-align: left;"><p>The configuration for the cluster network.</p>
<p><strong>Value:</strong> Object</p>
<div class="note">
<div class="title">
&#10;</div>
<p>You cannot change parameters specified by the <code>networking</code> object after installation.</p>
</div></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>networking:
  networkType:</code></pre></td>
<td style="text-align: left;"><p>The Red Hat OpenShift Networking network plugin to install.</p>
<p><strong>Value:</strong> <code>OVNKubernetes</code>. <code>OVNKubernetes</code> is a Container Network Interface (CNI) plugin for Linux networks and hybrid networks that contain both Linux and Windows servers. The default value is <code>OVNKubernetes</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>networking:
  clusterNetwork:</code></pre></td>
<td style="text-align: left;"><p>The IP address blocks for pods.</p>
<p>The default value is <code>10.128.0.0/14</code> with a host prefix of <code>/23</code>.</p>
<p>If you specify multiple IP address blocks, the blocks must not overlap.</p>
<p><strong>Value:</strong> An array of objects. For example:</p>
<div class="sourceCode" id="cb4"><pre class="sourceCode yaml"><code class="sourceCode yaml"><span id="cb4-1"><a href="#cb4-1" aria-hidden="true" tabindex="-1"></a><span class="fu">networking</span><span class="kw">:</span></span>
<span id="cb4-2"><a href="#cb4-2" aria-hidden="true" tabindex="-1"></a><span class="at">  </span><span class="fu">clusterNetwork</span><span class="kw">:</span></span>
<span id="cb4-3"><a href="#cb4-3" aria-hidden="true" tabindex="-1"></a><span class="at">  </span><span class="kw">-</span><span class="at"> </span><span class="fu">cidr</span><span class="kw">:</span><span class="at"> 10.128.0.0/14</span></span>
<span id="cb4-4"><a href="#cb4-4" aria-hidden="true" tabindex="-1"></a><span class="at">    </span><span class="fu">hostPrefix</span><span class="kw">:</span><span class="at"> </span><span class="dv">23</span></span>
<span id="cb4-5"><a href="#cb4-5" aria-hidden="true" tabindex="-1"></a><span class="at">  </span><span class="kw">-</span><span class="at"> </span><span class="fu">cidr</span><span class="kw">:</span><span class="at"> fd01::/48</span></span>
<span id="cb4-6"><a href="#cb4-6" aria-hidden="true" tabindex="-1"></a><span class="at">    </span><span class="fu">hostPrefix</span><span class="kw">:</span><span class="at"> </span><span class="dv">64</span></span></code></pre></div></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>networking:
  clusterNetwork:
    cidr:</code></pre></td>
<td style="text-align: left;"><p>Required if you use <code>networking.clusterNetwork</code>. An IP address block.</p>
<p>If you use the OVN-Kubernetes network plugin, you can specify IPv4 and IPv6 networks.</p>
<p><strong>Value:</strong> An IP address block in Classless Inter-Domain Routing (CIDR) notation. The prefix length for an IPv4 block is between <code>0</code> and <code>32</code>. The prefix length for an IPv6 block is between <code>0</code> and <code>128</code>. For example, <code>10.128.0.0/14</code> or <code>fd01::/48</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>networking:
  clusterNetwork:
    hostPrefix:</code></pre></td>
<td style="text-align: left;"><p>The subnet prefix length to assign to each individual node. For example, if <code>hostPrefix</code> is set to <code>23</code> then each node is assigned a <code>/23</code> subnet out of the given <code>cidr</code>. A <code>hostPrefix</code> value of <code>23</code> provides 510 (2^(32 - 23) - 2) pod IP addresses.</p>
<p><strong>Value:</strong> A subnet prefix.</p>
<p>For an IPv4 network the default value is <code>23</code>. For an IPv6 network the default value is <code>64</code>. The default value is also the minimum value for IPv6.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>networking:
  serviceNetwork:</code></pre></td>
<td style="text-align: left;"><p>The IP address block for services. The default value is <code>172.30.0.0/16</code>.</p>
<p>The OVN-Kubernetes network plugins supports only a single IP address block for the service network.</p>
<p>If you use the OVN-Kubernetes network plugin, you can specify an IP address block for both of the IPv4 and IPv6 address families.</p>
<p><strong>Value:</strong> An array with an IP address block in CIDR format. For example:</p>
<div class="sourceCode" id="cb8"><pre class="sourceCode yaml"><code class="sourceCode yaml"><span id="cb8-1"><a href="#cb8-1" aria-hidden="true" tabindex="-1"></a><span class="fu">networking</span><span class="kw">:</span></span>
<span id="cb8-2"><a href="#cb8-2" aria-hidden="true" tabindex="-1"></a><span class="at">  </span><span class="fu">serviceNetwork</span><span class="kw">:</span></span>
<span id="cb8-3"><a href="#cb8-3" aria-hidden="true" tabindex="-1"></a><span class="at">   </span><span class="kw">-</span><span class="at"> 172.30.0.0/16</span></span>
<span id="cb8-4"><a href="#cb8-4" aria-hidden="true" tabindex="-1"></a><span class="at">   </span><span class="kw">-</span><span class="at"> fd02::/112</span></span></code></pre></div></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>networking:
  machineNetwork:</code></pre></td>
<td style="text-align: left;"><p>The IP address blocks for machines.</p>
<p>If you specify multiple IP address blocks, the blocks must not overlap.</p>
<p><strong>Value:</strong> An array of objects. For example:</p>
<div class="sourceCode" id="cb10"><pre class="sourceCode yaml"><code class="sourceCode yaml"><span id="cb10-1"><a href="#cb10-1" aria-hidden="true" tabindex="-1"></a><span class="fu">networking</span><span class="kw">:</span></span>
<span id="cb10-2"><a href="#cb10-2" aria-hidden="true" tabindex="-1"></a><span class="at">  </span><span class="fu">machineNetwork</span><span class="kw">:</span></span>
<span id="cb10-3"><a href="#cb10-3" aria-hidden="true" tabindex="-1"></a><span class="at">  </span><span class="kw">-</span><span class="at"> </span><span class="fu">cidr</span><span class="kw">:</span><span class="at"> 10.0.0.0/16</span></span></code></pre></div></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>networking:
  machineNetwork:
    cidr:</code></pre></td>
<td style="text-align: left;"><p>Required if you use <code>networking.machineNetwork</code>. An IP address block. The default value is <code>10.0.0.0/16</code> for all platforms other than libvirt and IBM Power® Virtual Server. For libvirt, the default value is <code>192.168.126.0/24</code>. For IBM Power® Virtual Server, the default value is <code>192.168.0.0/24</code>.</p>
<p><strong>Value:</strong> An IP network block in CIDR notation.</p>
<p>For example, <code>10.0.0.0/16</code> or <code>fd00::/48</code>.</p>
<div class="note">
<div class="title">
&#10;</div>
<p>Set the <code>networking.machineNetwork</code> to match the CIDR that the preferred NIC resides in.</p>
</div></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>networking:
  ovnKubernetesConfig:
    ipv4:
      internalJoinSubnet:</code></pre></td>
<td style="text-align: left;"><p>Configures the IPv4 join subnet that is used internally by <code>ovn-kubernetes</code>. This subnet must not overlap with any other subnet that OpenShift Container Platform is using, including the node network. The size of the subnet must be larger than the number of nodes. You cannot change the value after installation.</p>
<p><strong>Value:</strong> An IP network block in CIDR notation. The default value is <code>100.64.0.0/16</code>.</p></td>
</tr>
</tbody>
</table>

## Optional configuration parameters

Optional installation configuration parameters are described in the following table:

<table>
<caption>Optional parameters</caption>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Parameter</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><pre><code>additionalTrustBundle:</code></pre></td>
<td style="text-align: left;"><p>A PEM-encoded X.509 certificate bundle that is added to the nodes' trusted certificate store. This trust bundle might also be used when a proxy has been configured.</p>
<p><strong>Value:</strong> String</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>capabilities:</code></pre></td>
<td style="text-align: left;"><p>Controls the installation of optional core cluster components. You can reduce the footprint of your OpenShift Container Platform cluster by disabling optional components. For more information, see the "Cluster capabilities" page in <em>Installing</em>.</p>
<p><strong>Value:</strong> String array</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>capabilities:
  baselineCapabilitySet:</code></pre></td>
<td style="text-align: left;"><p>Selects an initial set of optional capabilities to enable. Valid values are <code>None</code>, <code>v4.11</code>, <code>v4.12</code> and <code>vCurrent</code>. The default value is <code>vCurrent</code>.</p>
<p><strong>Value:</strong> String</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>capabilities:
  additionalEnabledCapabilities:</code></pre></td>
<td style="text-align: left;"><p>Extends the set of optional capabilities beyond what you specify in <code>baselineCapabilitySet</code>. You can specify multiple capabilities in this parameter.</p>
<p><strong>Value:</strong> String array</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>cpuPartitioningMode:</code></pre></td>
<td style="text-align: left;"><p>Enables workload partitioning, which isolates OpenShift Container Platform services, cluster management workloads, and infrastructure pods to run on a reserved set of CPUs. You can only enable workload partitioning during installation. You cannot disable it after installation. While this field enables workload partitioning, it does not configure workloads to use specific CPUs. For more information, see the <em>Workload partitioning</em> page in the <em>Scalability and Performance</em> section.</p>
<p><strong>Value:</strong> <code>None</code> or <code>AllNodes</code>. <code>None</code> is the default value.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>compute:</code></pre></td>
<td style="text-align: left;"><p>The configuration for the machines that comprise the compute nodes.</p>
<p><strong>Value:</strong> Array of <code>MachinePool</code> objects.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>compute:
  architecture:</code></pre></td>
<td style="text-align: left;"><p>Determines the instruction set architecture of the machines in the pool. Currently, clusters with varied architectures are not supported. All pools must specify the same architecture. Valid values are <code>amd64</code>, <code>arm64</code>, <code>ppc64le</code>, and <code>s390x</code>.</p>
<p><strong>Value:</strong> String</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>compute:
  hyperthreading:</code></pre></td>
<td style="text-align: left;"><p>Whether to enable or disable simultaneous multithreading, or <code>hyperthreading</code>, on compute machines. By default, simultaneous multithreading is enabled to increase the performance of your machines' cores.</p>
<div class="important">
<div class="title">
&#10;</div>
<p>If you disable simultaneous multithreading, ensure that your capacity planning accounts for the dramatically decreased machine performance.</p>
</div>
<p><strong>Value:</strong> <code>Enabled</code> or <code>Disabled</code></p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>compute:
  name:</code></pre></td>
<td style="text-align: left;"><p>Required if you use <code>compute</code>. The name of the machine pool.</p>
<p><strong>Value:</strong> <code>worker</code></p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>compute:
  platform:</code></pre></td>
<td style="text-align: left;"><p>Required if you use <code>compute</code>. Use this parameter to specify the cloud provider to host the worker machines. This parameter value must match the <code>controlPlane.platform</code> parameter value.</p>
<p><strong>Value:</strong> <code>baremetal</code>, <code>vsphere</code>, or <code>{}</code></p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>compute:
  replicas:</code></pre></td>
<td style="text-align: left;"><p>The number of compute machines, which are also known as worker machines, to provision.</p>
<p><strong>Value:</strong> A positive integer greater than or equal to <code>2</code>. The default value is <code>3</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>featureSet:</code></pre></td>
<td style="text-align: left;"><p>Enables the cluster for a feature set. A feature set is a collection of OpenShift Container Platform features that are not enabled by default. For more information about enabling a feature set during installation, see "Enabling features using feature gates".</p>
<p><strong>Value:</strong> String. The name of the feature set to enable, such as <code>TechPreviewNoUpgrade</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>controlPlane:</code></pre></td>
<td style="text-align: left;"><p>The configuration for the machines that form the control plane.</p>
<p><strong>Value:</strong> Array of <code>MachinePool</code> objects.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>controlPlane:
  architecture:</code></pre></td>
<td style="text-align: left;"><p>Determines the instruction set architecture of the machines in the pool. Currently, clusters with varied architectures are not supported. All pools must specify the same architecture. Valid values are <code>amd64</code>, <code>arm64</code>, <code>ppc64le</code>, and <code>s390x</code>.</p>
<p><strong>Value:</strong> String</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>controlPlane:
  hyperthreading:</code></pre></td>
<td style="text-align: left;"><p>Whether to enable or disable simultaneous multithreading, or <code>hyperthreading</code>, on control plane machines. By default, simultaneous multithreading is enabled to increase the performance of your machines' cores.</p>
<div class="important">
<div class="title">
&#10;</div>
<p>If you disable simultaneous multithreading, ensure that your capacity planning accounts for the dramatically decreased machine performance.</p>
</div>
<p><strong>Value:</strong> <code>Enabled</code> or <code>Disabled</code></p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>controlPlane:
  name:</code></pre></td>
<td style="text-align: left;"><p>Required if you use <code>controlPlane</code>. The name of the machine pool.</p>
<p><strong>Value:</strong> <code>master</code></p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>controlPlane:
  platform:</code></pre></td>
<td style="text-align: left;"><p>Required if you use <code>controlPlane</code>. Use this parameter to specify the cloud provider that hosts the control plane machines. This parameter value must match the <code>compute.platform</code> parameter value.</p>
<p><strong>Value:</strong> <code>baremetal</code>, <code>vsphere</code>, or <code>{}</code></p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>controlPlane:
  replicas:</code></pre></td>
<td style="text-align: left;"><p>The number of control plane machines to provision.</p>
<p><strong>Value:</strong> Supported values are <code>3</code>, <code>4</code>, <code>5</code>, or <code>1</code> when deploying single-node OpenShift.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>arbiter:
    name:</code></pre></td>
<td style="text-align: left;"><p>The OpenShift Container Platform cluster requires a name for arbiter nodes. For example, <code>arbiter</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>arbiter:
    replicas:</code></pre></td>
<td style="text-align: left;"><p>The <code>replicas</code> parameter sets the number of arbiter nodes for the OpenShift Container Platform cluster. You cannot set this field to a value that is greater than 1.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>credentialsMode:</code></pre></td>
<td style="text-align: left;"><p>The Cloud Credential Operator (CCO) mode. If no mode is specified, the CCO dynamically tries to determine the capabilities of the provided credentials, with a preference for mint mode on the platforms where multiple modes are supported.</p>
<div class="note">
<div class="title">
&#10;</div>
<p>Not all CCO modes are supported for all cloud providers. For more information about CCO modes, see the "Managing cloud provider credentials" entry in the <em>Authentication and authorization</em> content.</p>
</div>
<p><strong>Value:</strong> <code>Mint</code>, <code>Passthrough</code>, <code>Manual</code> or an empty string (<code>""</code>).</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>fips:</code></pre></td>
<td style="text-align: left;"><p>Enable or disable FIPS mode. The default is <code>false</code> (disabled). If you enable FIPS mode, the Red Hat Enterprise Linux CoreOS (RHCOS) machines that OpenShift Container Platform runs on bypass the default Kubernetes cryptography suite and use the cryptography modules that RHCOS provides instead.</p>
<div class="important">
<div class="title">
&#10;</div>
<p>To enable FIPS mode for your cluster, you must run the installation program from a Red Hat Enterprise Linux (RHEL) computer configured to operate in FIPS mode. For more information about configuring FIPS mode on RHEL, see <a href="https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/security_hardening/switching-rhel-to-fips-mode_security-hardening">Switching RHEL to FIPS mode</a>.</p>
<p>When running Red Hat Enterprise Linux (RHEL) or Red Hat Enterprise Linux CoreOS (RHCOS) booted in FIPS mode, OpenShift Container Platform core components use the RHEL cryptographic libraries that have been submitted to NIST for FIPS 140-2/140-3 Validation on only the x86_64, ppc64le, and s390x architectures.</p>
</div>
<div class="important">
<div class="title">
&#10;</div>
<p>If you are using Azure File storage, you cannot enable FIPS mode.</p>
</div>
<p><strong>Value:</strong> <code>false</code> or <code>true</code></p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>imageContentSources:</code></pre></td>
<td style="text-align: left;"><p>Sources and repositories for the release-image content.</p>
<p><strong>Value:</strong> Array of objects. Includes a <code>source</code> and, optionally, <code>mirrors</code>, as described in the following rows of this table.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>imageContentSources:
  source:</code></pre></td>
<td style="text-align: left;"><p>Required if you use <code>imageContentSources</code>. Specify the repository that users refer to, for example, in image pull specifications.</p>
<p><strong>Value:</strong> String</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>imageContentSources:
  mirrors:</code></pre></td>
<td style="text-align: left;"><p>Specify one or more repositories that might also contain the same images.</p>
<p><strong>Value:</strong> Array of strings</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>publish:</code></pre></td>
<td style="text-align: left;"><p>How to publish or expose the user-facing endpoints of your cluster, such as the Kubernetes API, OpenShift routes.</p>
<p><strong>Value:</strong> <code>Internal</code> or <code>External</code>. The default value is <code>External</code>.</p>
<p>Setting this field to <code>Internal</code> is not supported on non-cloud platforms.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>sshKey:</code></pre></td>
<td style="text-align: left;"><p>The SSH key to authenticate access to your cluster machines.</p>
<div class="note">
<div class="title">
&#10;</div>
<p>For production OpenShift Container Platform clusters on which you want to perform installation debugging or disaster recovery, specify an SSH key that your <code>ssh-agent</code> process uses.</p>
</div>
<p><strong>Value:</strong> For example, <code>sshKey: ssh-ed25519 AAAA..</code>.</p></td>
</tr>
</tbody>
</table>

## Additional bare metal configuration parameters for the Agent-based Installer

Additional bare metal installation configuration parameters for the Agent-based Installer are described in the following table:

> [!NOTE]
> These fields are not used during the initial provisioning of the cluster, but they are available to use once the cluster has been installed. Configuring these fields at install time eliminates the need to set them as a Day 2 operation.

<table>
<caption>Additional bare metal parameters</caption>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Parameter</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><pre><code>platform:
  baremetal:
    clusterProvisioningIP:</code></pre></td>
<td style="text-align: left;"><p>The IP address within the cluster where the provisioning services run. Defaults to the third IP address of the provisioning subnet. For example, <code>172.22.0.3</code> or <code>2620:52:0:1307::3</code>.</p>
<p><strong>Value:</strong> IPv4 or IPv6 address.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>platform:
  baremetal:
    provisioningNetwork:</code></pre></td>
<td style="text-align: left;"><p>The <code>provisioningNetwork</code> configuration setting determines whether the cluster uses the provisioning network. If it does, the configuration setting also determines if the cluster manages the network.</p>
<p><code>Managed</code>: Default. Set this parameter to <code>Managed</code> to fully manage the provisioning network, including DHCP, TFTP, and so on.</p>
<p><code>Disabled</code>: Set this parameter to <code>Disabled</code> to disable the requirement for a provisioning network. When set to <code>Disabled</code>, you can use only virtual media based provisioning on Day 2. If <code>Disabled</code> and using power management, BMCs must be accessible from the bare-metal network. If Disabled, you must provide two IP addresses on the bare-metal network that are used for the provisioning services.</p>
<p><strong>Value:</strong> <code>Managed</code> or <code>Disabled</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>platform:
  baremetal:
    provisioningMACAddress:</code></pre></td>
<td style="text-align: left;"><p>The MAC address within the cluster where provisioning services run.</p>
<p><strong>Value:</strong> MAC address.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>platform:
  baremetal:
    provisioningNetworkCIDR:</code></pre></td>
<td style="text-align: left;"><p>The CIDR for the network to use for provisioning. This option is required when not using the default address range on the provisioning network.</p>
<p><strong>Value:</strong> Valid CIDR, for example <code>10.0.0.0/16</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>platform:
  baremetal:
    provisioningNetworkInterface:</code></pre></td>
<td style="text-align: left;"><p>The name of the network interface on nodes connected to the provisioning network. Use the <code>bootMACAddress</code> configuration setting to enable Ironic to identify the IP address of the NIC instead of using the <code>provisioningNetworkInterface</code> configuration setting to identify the name of the NIC.</p>
<p><strong>Value:</strong> String.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>platform:
  baremetal:
    provisioningDHCPRange:</code></pre></td>
<td style="text-align: left;"><p>Defines the IP range for nodes on the provisioning network, for example <code>172.22.0.10,172.22.0.254</code>.</p>
<p><strong>Value:</strong> IP address range.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>platform:
  baremetal:
    hosts:</code></pre></td>
<td style="text-align: left;"><p>Configuration for bare metal hosts.</p>
<p><strong>Value:</strong> Array of host configuration objects.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>platform:
  baremetal:
    hosts:
      name:</code></pre></td>
<td style="text-align: left;"><p>The name of the host.</p>
<p><strong>Value:</strong> String.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>platform:
  baremetal:
    hosts:
      bootMACAddress:</code></pre></td>
<td style="text-align: left;"><p>The MAC address of the NIC used for provisioning the host.</p>
<p><strong>Value:</strong> MAC address.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>platform:
  baremetal:
    hosts:
      bmc:</code></pre></td>
<td style="text-align: left;"><p>Configuration for the host to connect to the baseboard management controller (BMC).</p>
<p><strong>Value:</strong> Dictionary of BMC configuration objects.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>platform:
  baremetal:
    hosts:
      bmc:
        username:</code></pre></td>
<td style="text-align: left;"><p>The username for the BMC.</p>
<p><strong>Value:</strong> String.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>platform:
  baremetal:
    hosts:
      bmc:
        password:</code></pre></td>
<td style="text-align: left;"><p>Password for the BMC.</p>
<p><strong>Value:</strong> String.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>platform:
  baremetal:
    hosts:
      bmc:
        address:</code></pre></td>
<td style="text-align: left;"><p>The URL for communicating with the host’s BMC controller. The address configuration setting specifies the protocol. For example, <code>redfish+http://10.10.10.1:8000/redfish/v1/Systems/1234</code> enables Redfish. For more information, see "BMC addressing" in the "Deploying installer-provisioned clusters on bare metal" section.</p>
<p><strong>Value:</strong> URL.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>platform:
  baremetal:
    hosts:
      bmc:
        disableCertificateVerification:</code></pre></td>
<td style="text-align: left;"><p><code>redfish</code> and <code>redfish-virtualmedia</code> need this parameter to manage BMC addresses. The value should be <code>True</code> when using a self-signed certificate for BMC addresses.</p>
<p><strong>Value:</strong> Boolean.</p></td>
</tr>
</tbody>
</table>

## Additional VMware vSphere configuration parameters

Additional VMware vSphere configuration parameters are described in the following table:

<table>
<caption>Additional VMware vSphere cluster parameters</caption>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Parameter</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><pre><code>platform:
  vsphere:</code></pre></td>
<td style="text-align: left;"><p>Describes your account on the cloud platform that hosts your cluster. You can use the parameter to customize the platform. If you provide additional configuration settings for compute and control plane machines in the machine pool, the parameter is not required.</p>
<p><strong>Value:</strong> A dictionary of vSphere configuration objects</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>platform:
  vsphere:
    failureDomains:</code></pre></td>
<td style="text-align: left;"><p>Establishes the relationships between a region and zone. You define a failure domain by using vCenter objects, such as a <code>datastore</code> object. A failure domain defines the vCenter location for OpenShift Container Platform cluster nodes.</p>
<p><strong>Value:</strong> An array of failure domain configuration objects.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>platform:
  vsphere:
    failureDomains:
      name:</code></pre></td>
<td style="text-align: left;"><p>The name of the failure domain.</p>
<p><strong>Value:</strong> String</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>platform:
  vsphere:
    failureDomains:
      region:</code></pre></td>
<td style="text-align: left;"><p>If you define multiple failure domains for your cluster, you must attach the tag to each vCenter data center. To define a region, use a tag from the <code>openshift-region</code> tag category. For a single vSphere data center environment, you do not need to attach a tag, but you must enter an alphanumeric value, such as <code>datacenter</code>, for the parameter. If you want to base your failure domains on host groups, attach these tags to your vSphere clusters instead of your data centers.</p>
<div class="important">
<div class="title">
&#10;</div>
<p>OpenShift zones support for vSphere host groups is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.</p>
<p>For more information about the support scope of Red Hat Technology Preview features, see <a href="https://access.redhat.com/support/offerings/techpreview/">Technology Preview Features Support Scope</a>.</p>
</div>
<p><strong>Value:</strong> String</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>platform:
  vsphere:
    failureDomains:
      regionType:</code></pre></td>
<td style="text-align: left;"><p>Specifies the <code>ComputeCluster</code> region type to enable host groups.</p>
<div class="important">
<div class="title">
&#10;</div>
<p>OpenShift zones support for vSphere host groups is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.</p>
<p>For more information about the support scope of Red Hat Technology Preview features, see <a href="https://access.redhat.com/support/offerings/techpreview/">Technology Preview Features Support Scope</a>.</p>
</div>
<p><strong>Value:</strong> String</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>platform:
  vsphere:
    failureDomains:
      server:</code></pre></td>
<td style="text-align: left;"><p>Specifies the fully-qualified hostname or IP address of the VMware vCenter server, so that a client can access failure domain resources. You must apply the <code>server</code> role to the vSphere vCenter server location.</p>
<p><strong>Value:</strong> String</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>platform:
  vsphere:
    failureDomains:
      zone:</code></pre></td>
<td style="text-align: left;"><p>If you define multiple failure domains for your cluster, you must attach a tag to each vCenter cluster. To define a zone, use a tag from the <code>openshift-zone</code> tag category. For a single vSphere data center environment, you do not need to attach a tag, but you must enter an alphanumeric value, such as <code>cluster</code>, for the parameter. If you want to base your failure domains on host groups, define zones that correspond to your host groups instead of your clusters. Use these tags to associate each ESXi host with its host group.</p>
<div class="important">
<div class="title">
&#10;</div>
<p>OpenShift zones support for vSphere host groups is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.</p>
<p>For more information about the support scope of Red Hat Technology Preview features, see <a href="https://access.redhat.com/support/offerings/techpreview/">Technology Preview Features Support Scope</a>.</p>
</div>
<p><strong>Value:</strong> String</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>platform:
  vsphere:
    failureDomains:
      zoneType:</code></pre></td>
<td style="text-align: left;"><p>Specifies the <code>HostGroup</code> zone type to enable host groups.</p>
<div class="important">
<div class="title">
&#10;</div>
<p>OpenShift zones support for vSphere host groups is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.</p>
<p>For more information about the support scope of Red Hat Technology Preview features, see <a href="https://access.redhat.com/support/offerings/techpreview/">Technology Preview Features Support Scope</a>.</p>
</div>
<p><strong>Value:</strong> String</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>platform:
  vsphere:
    failureDomains:
      topology:
        computeCluster:</code></pre></td>
<td style="text-align: left;"><p>The path to the vSphere compute cluster.</p>
<p><strong>Value:</strong> String</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>platform:
  vsphere:
    failureDomains:
      topology:
        datacenter:</code></pre></td>
<td style="text-align: left;"><p>Lists and defines the data centers where OpenShift Container Platform virtual machines (VMs) operate. The list of data centers must match the list of data centers specified in the <code>vcenters</code> field.</p>
<p><strong>Value:</strong> String</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>platform:
  vsphere:
    failureDomains:
      topology:
        datastore:</code></pre></td>
<td style="text-align: left;"><p>The path to the vSphere datastore that holds virtual machine files, templates, and ISO images.</p>
<div class="important">
<div class="title">
&#10;</div>
<p>You can specify the path of any datastore that exists in a datastore cluster. By default, Storage vMotion is automatically enabled for a datastore cluster. Red Hat does not support Storage vMotion, so you must disable Storage vMotion to avoid data loss issues for your OpenShift Container Platform cluster.</p>
<p>If you must specify VMs across multiple datastores, use a <code>datastore</code> object to specify a failure domain in your cluster’s <code>install-config.yaml</code> configuration file. For more information, see "VMware vSphere region and zone enablement".</p>
</div>
<p><strong>Value:</strong> String</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>platform:
  vsphere:
    failureDomains:
      topology:
        folder:</code></pre></td>
<td style="text-align: left;"><p>Optional: The absolute path of an existing folder where the user creates the virtual machines, for example, <code>/&lt;data_center_name&gt;/vm/&lt;folder_name&gt;/&lt;subfolder_name&gt;</code>.</p>
<p><strong>Value:</strong> String</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>platform:
  vsphere:
    failureDomains:
      topology:
        hostGroup:</code></pre></td>
<td style="text-align: left;"><p>Specifies the vSphere host group to associate with the failure domain.</p>
<div class="important">
<div class="title">
&#10;</div>
<p>OpenShift zones support for vSphere host groups is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.</p>
<p>For more information about the support scope of Red Hat Technology Preview features, see <a href="https://access.redhat.com/support/offerings/techpreview/">Technology Preview Features Support Scope</a>.</p>
</div>
<p><strong>Value:</strong> String</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>platform:
  vsphere:
    failureDomains:
      topology:
        networks:</code></pre></td>
<td style="text-align: left;"><p>Lists any network in the vCenter instance that contains the virtual IP addresses and DNS records that you configured.</p>
<p><strong>Value:</strong> String</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>platform:
  vsphere:
    failureDomains:
      topology:
        resourcePool:</code></pre></td>
<td style="text-align: left;"><p>Optional: The absolute path of an existing resource pool where the installation program creates the virtual machines, for example, <code>/&lt;data_center_name&gt;/host/&lt;cluster_name&gt;/Resources/&lt;resource_pool_name&gt;/&lt;optional_nested_resource_pool_name&gt;</code>.</p>
<p><strong>Value:</strong> String</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>platform:
  vsphere:
    failureDomains:
      topology:
        tagIDs:</code></pre></td>
<td style="text-align: left;"><p>Optional: Specifies the ID of the tag to be associated by the installation program. Each VM created by OpenShift Container Platform is assigned a unique tag that is specific to the cluster. The assigned tag enables the installation program to identify and remove the associated VMs when a cluster is decommissioned. You can list up to ten additional tag IDs to be attached to the VMs provisioned by the installation program. For more information about determining the tag ID, see the <a href="https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.vcenterhost.doc/GUID-E8E854DD-AA97-4E0C-8419-CE84F93C4058.html">vSphere Tags and Attributes documentation</a>.</p>
<p><strong>Value:</strong> String, for example <code>urn:vmomi:InventoryServiceTag:208e713c-cae3-4b7f-918e-4051ca7d1f97:GLOBAL</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>platform:
  vsphere:
    failureDomains:
      topology:
        template:</code></pre></td>
<td style="text-align: left;"><p>Specifies the absolute path to a pre-existing Red Hat Enterprise Linux CoreOS (RHCOS) image template or virtual machine. The installation program can use the image template or virtual machine to quickly install RHCOS on vSphere hosts. Consider using this parameter as an alternative to uploading an RHCOS image on vSphere hosts. This parameter is available for use only on installer-provisioned infrastructure.</p>
<p><strong>Value:</strong> String</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>platform:
  vsphere:
    vcenters:</code></pre></td>
<td style="text-align: left;"><p>Configures the connection details so that services can communicate with a vCenter server.</p>
<p><strong>Value:</strong> An array of vCenter configuration objects.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>platform:
  vsphere:
    vcenters:
      datacenters:</code></pre></td>
<td style="text-align: left;"><p>Lists and defines the data centers where OpenShift Container Platform virtual machines (VMs) operate. The list of data centers must match the list of data centers specified in the <code>failureDomains</code> field.</p>
<p><strong>Value:</strong> String</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>platform:
  vsphere:
    vcenters:
      password:</code></pre></td>
<td style="text-align: left;"><p>The password associated with the vSphere user.</p>
<p><strong>Value:</strong> String</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>platform:
  vsphere:
    vcenters:
      port:</code></pre></td>
<td style="text-align: left;"><p>The port number used to communicate with the vCenter server.</p>
<p><strong>Value:</strong> Integer</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>platform:
  vsphere:
    vcenters:
      server:</code></pre></td>
<td style="text-align: left;"><p>The fully qualified host name (FQHN) or IP address of the vCenter server.</p>
<p><strong>Value:</strong> String</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>platform:
  vsphere:
    vcenters:
      user:</code></pre></td>
<td style="text-align: left;"><p>The username associated with the vSphere user.</p>
<p><strong>Value:</strong> String</p></td>
</tr>
</tbody>
</table>

## Deprecated VMware vSphere configuration parameters

In OpenShift Container Platform 4.13, the following vSphere configuration parameters are deprecated. You can continue to use these parameters, but the installation program does not automatically specify these parameters in the `install-config.yaml` file.

The following table lists each deprecated vSphere configuration parameter:

<table>
<caption>Deprecated VMware vSphere cluster parameters</caption>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Parameter</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><pre><code>platform:
  vsphere:
    cluster:</code></pre></td>
<td style="text-align: left;"><p>The vCenter cluster to install the OpenShift Container Platform cluster in.</p>
<p><strong>Value:</strong> String</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>platform:
  vsphere:
    datacenter:</code></pre></td>
<td style="text-align: left;"><p>Defines the data center where OpenShift Container Platform virtual machines (VMs) operate.</p>
<p><strong>Value:</strong> String</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>platform:
  vsphere:
    defaultDatastore:</code></pre></td>
<td style="text-align: left;"><p>The name of the default datastore to use for provisioning volumes.</p>
<p><strong>Value:</strong> String</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>platform:
  vsphere:
    folder:</code></pre></td>
<td style="text-align: left;"><p>Optional: The absolute path of an existing folder where the installation program creates the virtual machines. If you do not provide this value, the installation program creates a folder that is named with the infrastructure ID in the data center virtual machine folder.</p>
<p><strong>Value:</strong> String, for example, <code>/&lt;data_center_name&gt;/vm/&lt;folder_name&gt;/&lt;subfolder_name&gt;</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>platform:
  vsphere:
    password:</code></pre></td>
<td style="text-align: left;"><p>The password for the vCenter user name.</p>
<p><strong>Value:</strong> String</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>platform:
  vsphere:
    resourcePool:</code></pre></td>
<td style="text-align: left;"><p>Optional: The absolute path of an existing resource pool where the installation program creates the virtual machines. If you do not specify a value, the installation program installs the resources in the root of the cluster under <code>/&lt;data_center_name&gt;/host/&lt;cluster_name&gt;/Resources</code>.</p>
<p><strong>Value:</strong> String, for example, <code>/&lt;data_center_name&gt;/host/&lt;cluster_name&gt;/Resources/&lt;resource_pool_name&gt;/&lt;optional_nested_resource_pool_name&gt;</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>platform:
  vsphere:
    username:</code></pre></td>
<td style="text-align: left;"><p>The user name to use to connect to the vCenter instance with. This user must have at least the roles and privileges that are required for <a href="https://github.com/vmware-archive/vsphere-storage-for-kubernetes/blob/master/documentation/vcp-roles.md">static or dynamic persistent volume provisioning</a> in vSphere.</p>
<p><strong>Value:</strong> String</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>platform:
  vsphere:
    vCenter:</code></pre></td>
<td style="text-align: left;"><p>The fully-qualified hostname or IP address of a vCenter server.</p>
<p><strong>Value:</strong> String</p></td>
</tr>
</tbody>
</table>

<div>

<div class="title">

Additional resources

</div>

- [BMC addressing](../installing_bare_metal/ipi/ipi-install-installation-workflow.md#bmc-addressing_ipi-install-installation-workflow)

- [Configuring regions and zones for a VMware vCenter](../installing_vsphere/ipi/installing-vsphere-installer-provisioned-customizations.md#configuring-vsphere-regions-zones_installing-vsphere-installer-provisioned-customizations)

- [Required vCenter account privileges](../installing_vsphere/ipi/ipi-vsphere-installation-reqs.md#installation-vsphere-installer-infra-requirements-account_ipi-vsphere-installation-reqs)

</div>

# Available Agent configuration parameters

To customize your cluster installation, configuration parameters are available to use in the `agent-config.yaml` file.

The following tables specify the required and optional Agent configuration parameters that you can set as part of the Agent-based installation process.

> [!NOTE]
> These settings are used for installation only, and cannot be modified after installation.

## Required configuration parameters

Required Agent configuration parameters are described in the following table:

<table>
<caption>Required parameters</caption>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Parameter</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><pre><code>apiVersion:</code></pre></td>
<td style="text-align: left;"><p>The API version for the <code>agent-config.yaml</code> content. The current version is <code>v1beta1</code>. The installation program might also support older API versions.</p>
<p><strong>Value:</strong> String</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>metadata:</code></pre></td>
<td style="text-align: left;"><p>Kubernetes resource <code>ObjectMeta</code>, from which only the <code>name</code> parameter is consumed.</p>
<p><strong>Value:</strong> Object</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>metadata:
  name:</code></pre></td>
<td style="text-align: left;"><p>The name of the cluster. DNS records for the cluster are all subdomains of <code>{{.metadata.name}}.{}</code>. The value entered in the <code>agent-config.yaml</code> file is ignored, and instead the value specified in the <code>install-config.yaml</code> file is used. When you do not provide <code>metadata.name</code> through either the <code>install-config.yaml</code> or <code>agent-config.yaml</code> files, for example when you use only ZTP manifests, the cluster name is set to <code>agent-cluster</code>.</p>
<p><strong>Value:</strong> String of lowercase letters and hyphens (<code>-</code>), such as <code>dev</code>.</p></td>
</tr>
</tbody>
</table>

## Optional configuration parameters

Optional Agent configuration parameters are described in the following table:

<table>
<caption>Optional parameters</caption>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Parameter</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><pre><code>rendezvousIP:</code></pre></td>
<td style="text-align: left;"><p>The IP address of the node that performs the bootstrapping process as well as running the <code>assisted-service</code> component. You must provide the rendezvous IP address when you do not specify at least one host’s IP address in the <code>networkConfig</code> parameter. If this address is not provided, one IP address is selected from the provided hosts' <code>networkConfig</code>.</p>
<p><strong>Value:</strong> IPv4 or IPv6 address.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>bootArtifactsBaseURL:</code></pre></td>
<td style="text-align: left;"><p>When you use the Agent-based Installer to generate a minimal ISO image, this parameter specifies a URL where the rootfs image file can be retrieved from during cluster installation. This parameter is optional for booting minimal ISO images in connected environments.</p>
<p>When you use the Agent-based Installer to generate an iPXE script, this parameter specifies the URL of the server to upload Preboot Execution Environment (PXE) assets to. For more information, see "Preparing PXE assets for OpenShift Container Platform".</p>
<p><strong>Value:</strong> String.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>additionalNTPSources:</code></pre></td>
<td style="text-align: left;"><p>A list of Network Time Protocol (NTP) sources to be added to all cluster hosts, which are added to any NTP sources that are configured through other means.</p>
<p><strong>Value:</strong> List of hostnames or IP addresses.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>hosts:</code></pre></td>
<td style="text-align: left;"><p>Host configuration. An optional list of hosts. The number of hosts defined must not exceed the total number of hosts defined in the <code>install-config.yaml</code> file, which is the sum of the values of the <code>compute.replicas</code> and <code>controlPlane.replicas</code> parameters.</p>
<p><strong>Value:</strong> An array of host configuration objects.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>hosts:
  hostname:</code></pre></td>
<td style="text-align: left;"><p>Hostname. Overrides the hostname obtained from either the Dynamic Host Configuration Protocol (DHCP) or a reverse DNS lookup. Each host must have a unique hostname supplied by one of these methods, although configuring a hostname through this parameter is optional.</p>
<p><strong>Value:</strong> String.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>hosts:
  interfaces:</code></pre></td>
<td style="text-align: left;"><p>Provides a table of the name and MAC address mappings for the interfaces on the host. If a <code>NetworkConfig</code> section is provided in the <code>agent-config.yaml</code> file, this table must be included and the values must match the mappings provided in the <code>NetworkConfig</code> section.</p>
<p><strong>Value:</strong> An array of host configuration objects.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>hosts:
  interfaces:
    name:</code></pre></td>
<td style="text-align: left;"><p>The name of an interface on the host.</p>
<div class="note">
<div class="title">
&#10;</div>
<p>This value does not need to match the device name.</p>
</div>
<p><strong>Value:</strong> String.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>hosts:
  interfaces:
    macAddress:</code></pre></td>
<td style="text-align: left;"><p>The MAC address of an interface on the host.</p>
<p><strong>Value:</strong> A MAC address such as the following example: <code>00-B0-D0-63-C2-26</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>hosts:
  role:</code></pre></td>
<td style="text-align: left;"><p>Defines whether the host is a <code>master</code> or <code>worker</code> node. If no role is defined in the <code>agent-config.yaml</code> file, roles will be assigned at random during cluster installation.</p>
<p><strong>Value:</strong> <code>master</code> or <code>worker</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>hosts:
  rootDeviceHints:</code></pre></td>
<td style="text-align: left;"><p>Enables provisioning of the Red Hat Enterprise Linux CoreOS (RHCOS) image to a particular device. The installation program examines the devices in the order it discovers them, and compares the discovered values with the hint values. It uses the first discovered device that matches the hint value. This is the device that the operating system is written on during installation.</p>
<p><strong>Value:</strong> A dictionary of key-value pairs. For more information, see "Root device hints" in the "Setting up the environment for an OpenShift installation" page.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>hosts:
  rootDeviceHints:
    deviceName:</code></pre></td>
<td style="text-align: left;"><p>The name of the device the RHCOS image is provisioned to.</p>
<p><strong>Value:</strong> String.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>hosts:
  networkConfig:</code></pre></td>
<td style="text-align: left;"><p>The host network definition. The configuration must match the Host Network Management API defined in the "Declarative Network API (nmstate documentation)".</p>
<p><strong>Value:</strong> A dictionary of host network configuration objects.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>minimalISO:</code></pre></td>
<td style="text-align: left;"><p>Defines whether the Agent-based Installer generates a full ISO or a minimal ISO image. When this parameter is set to <code>True</code>, the Agent-based Installer generates an ISO without a rootfs image file, and instead contains details about where to pull the rootfs file from.</p>
<p>When you generate a minimal ISO, if you do not specify a rootfs URL through the <code>bootArtifactsBaseURL</code> parameter, the Agent-based Installer embeds a default URL that is accessible in environments with an internet connection.</p>
<p>The default value is <code>False</code>.</p>
<p><strong>Value:</strong> Boolean.</p></td>
</tr>
</tbody>
</table>

<div>

<div class="title">

Additional resources

</div>

- [Preparing PXE assets for OpenShift Container Platform](prepare-pxe-assets-agent.md#prepare-pxe-assets-agent)

- [Declarative Network API (nmstate documentation)](https://nmstate.io/)

- [Root device hints](../installing_bare_metal/ipi/ipi-install-installation-workflow.md#root-device-hints_ipi-install-installation-workflow)

</div>
