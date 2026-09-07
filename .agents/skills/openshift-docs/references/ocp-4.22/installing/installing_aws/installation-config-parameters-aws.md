<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Before you deploy an OpenShift Container Platform cluster on Amazon Web Services (AWS), you create the `install-config.yaml` file and provide parameters to customize your cluster and the platform that hosts it. You can then modify the `install-config.yaml` file to customize your cluster further.

# Available installation configuration parameters for AWS

To customize your cluster installation, you can use configuration parameters in the `install-config.yaml` file.

The following tables specify the required, optional, and AWS-specific installation configuration parameters that you can set as part of the installation process.

> [!IMPORTANT]
> After installation, you cannot change these parameters in the `install-config.yaml` file.

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
<td style="text-align: left;"><p>The name of the cluster. DNS records for the cluster are all subdomains of <code>{{.metadata.name}}.{}</code>.</p>
<p><strong>Value:</strong> String of lowercase letters, hyphens (<code>-</code>), and periods (<code>.</code>), such as <code>dev</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>platform:</code></pre></td>
<td style="text-align: left;"><p>The configuration for the specific platform upon which to perform the installation: <code>aws</code>, <code>baremetal</code>, <code>azure</code>, <code>gcp</code>, <code>ibmcloud</code>, <code>nutanix</code>, <code>openstack</code>, <code>powervs</code>, <code>vsphere</code>, or <code>{}</code>. For additional information about <code>platform.&lt;platform&gt;</code> parameters, consult the table for your specific platform that follows.</p>
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

  If you are installing your cluster on AWS, the order of address families must match the `platform.aws.ipFamily` parameter. For example, if you specified the `DualStackIPv6Primary` parameter, you must list the IPv6 address first.

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
<p>An IPv4 network.</p>
<p>If you use the OVN-Kubernetes network plugin, you can specify IPv4 and IPv6 networks.</p>
<p><strong>Value:</strong> An IP address block in Classless Inter-Domain Routing (CIDR) notation. The prefix length for an IPv4 block is between <code>0</code> and <code>32</code>. The prefix length for an IPv6 block is between <code>0</code> and <code>128</code>. For example, <code>10.128.0.0/14</code> or <code>fd01::/48</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>networking:
  clusterNetwork:
    hostPrefix:</code></pre></td>
<td style="text-align: left;"><p>The subnet prefix length to assign to each individual node. For example, if <code>hostPrefix</code> is set to <code>23</code> then each node is assigned a <code>/23</code> subnet out of the given <code>cidr</code>. A <code>hostPrefix</code> value of <code>23</code> provides 510 (2^(32 - 23) - 2) pod IP addresses.</p>
<p><strong>Value:</strong> A subnet prefix.</p>
<p>The default value is <code>23</code>.</p>
<p>For an IPv4 network the default value is <code>23</code>. For an IPv6 network <code>hostPrefix</code> must be set to <code>64</code>, which is the default value.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>networking:
  serviceNetwork:</code></pre></td>
<td style="text-align: left;"><p>The IP address block for services. The default value is <code>172.30.0.0/16</code>.</p>
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
<p>For example, <code>10.0.0.0/16</code>.</p>
<div class="note">
<div class="title">
&#10;</div>
<p>Set the <code>networking.machineNetwork</code> to match the CIDR of the preferred NIC.</p>
<p>If you are installing a cluster on AWS with dual-stack networking, consider the following distinction:</p>
<ul>
<li><p>If the installation program creates the VPC, do not specify an IPv6 entry in <code>networking.machineNetwork</code>. The installation program will assign an IPv6 address to the VPC.</p></li>
<li><p>If you provide existing dual-stack subnets using the <code>platform.aws.vpc.subnets</code> parameter, you must specify IPv6 entries corresponding to either the VPC CIDR or the CIDR of the subnets.</p></li>
<li><p>In both cases, you must provide an IPv4 CIDR entry.</p></li>
</ul>
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
<td style="text-align: left;"><p>Determines the instruction set architecture of the machines in the pool. Currently, clusters with varied architectures are not supported. All pools must specify the same architecture. Valid values are <code>amd64</code> and <code>arm64</code>.</p>
<p>Not all installation options support the 64-bit ARM architecture. To verify if your installation option is supported on your platform, see <em>Supported installation methods for different platforms</em> in <em>Selecting a cluster installation method and preparing it for users</em>.</p>
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
<p><strong>Value:</strong> <code>aws</code>, <code>azure</code>, <code>gcp</code>, <code>ibmcloud</code>, <code>nutanix</code>, <code>openstack</code>, <code>powervs</code>, <code>vsphere</code>, or <code>{}</code></p></td>
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
<td style="text-align: left;"><p>Determines the instruction set architecture of the machines in the pool. Currently, clusters with varied architectures are not supported. All pools must specify the same architecture. Valid values are <code>amd64</code> and <code>arm64</code>.</p>
<p>Not all installation options support the 64-bit ARM architecture. To verify if your installation option is supported on your platform, see <em>Supported installation methods for different platforms</em> in <em>Selecting a cluster installation method and preparing it for users</em>.</p>
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
<p><strong>Value:</strong> <code>aws</code>, <code>azure</code>, <code>gcp</code>, <code>ibmcloud</code>, <code>nutanix</code>, <code>openstack</code>, <code>powervs</code>, <code>vsphere</code>, or <code>{}</code></p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>controlPlane:
  replicas:</code></pre></td>
<td style="text-align: left;"><p>The number of control plane machines to provision.</p>
<p><strong>Value:</strong> Supported values are <code>3</code>, or <code>1</code> when deploying single-node OpenShift.</p></td>
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
<td style="text-align: left;"><pre><code>endpoint:
  name: &lt;endpoint_name&gt;
  clusterUseOnly: `true` or `false`</code></pre></td>
<td style="text-align: left;"><p>The <code>name</code> parameter contains the name of the Private Service Connect (PSC) endpoints.</p>
<div class="important">
<div class="title">
&#10;</div>
<p>When <code>clusterUseOnly</code> is <code>false</code>, its default setting, you must run the installation program from a bastion host that is within the same VPC where you want to deploy the cluster.</p>
</div>
<p>When you want the installation program to use the public API endpoints and cluster Operators to use the API endpoint overrides, set <code>clusterUseOnly</code> to <code>true</code>. When you want both the installation program and the cluster Operators to use the API endpoint overrides, for example if you are running the installation program from a bastion host that is within the same VPC where you want to deploy the cluster, set <code>clusterUseOnly</code> to <code>false</code> . The parameter is optional and defaults to <code>false</code>.</p>
<p><strong>Value:</strong> String or boolean</p></td>
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
<td style="text-align: left;"><pre><code>osImageStream:</code></pre></td>
<td style="text-align: left;"><p>Specifies the image stream that will be used for all machines in the cluster. <code>osImageStream</code> is a Technology Preview feature. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.</p>
<p><strong>Value:</strong> String. Valid values are <code>rhel-9</code> or <code>rhel-10</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>platform:
  aws:
    lbType:</code></pre></td>
<td style="text-align: left;"><p>Required to set the NLB load balancer type in AWS. Valid values are <code>Classic</code> or <code>NLB</code>. If no value is specified, the installation program defaults to <code>Classic</code>. The installation program sets the value provided here in the ingress cluster configuration object. If you do not specify a load balancer type for other Ingress Controllers, they use the type set in this parameter.</p>
<p>If you installed your cluster using the <code>DualStackIPv4Primary</code> or <code>DualStackIPv6Primary</code> values for the <code>platform.aws.ipFamily</code> parameter, any services that have IPv6 addresses must use the NLB load balancer type. The classic load balancer (CLB) does not support IPv6.</p>
<p><strong>Value:</strong> <code>Classic</code> or <code>NLB</code>. If you do not set the <code>platform.aws.ipFamily</code> parameter or set it to <code>IPv4</code>, the default value is <code>Classic</code>. If you set the <code>platform.aws.ipFamily</code> parameter to <code>DualStackIPv4Primary</code> or <code>DualStackIPv6Primary</code>, the default value is <code>NLB</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>publish:</code></pre></td>
<td style="text-align: left;"><p>How to publish or expose the user-facing endpoints of your cluster, such as the Kubernetes API, OpenShift routes.</p>
<p><strong>Value:</strong> <code>Internal</code> or <code>External</code>. To deploy a private cluster that cannot be accessed from the internet, set the <code>publish</code> parameter to <code>Internal</code>. The default value is <code>External</code>.</p></td>
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

> [!NOTE]
> If your AWS account has service control policies (SCP) enabled, you must configure the `credentialsMode` parameter to `Mint`, `Passthrough`, or `Manual`.

> [!IMPORTANT]
> Setting this parameter to `Manual` enables alternatives to storing administrator-level secrets in the `kube-system` project, which require additional configuration steps. For more information, see "Alternatives to storing administrator-level secrets in the kube-system project".

## Optional AWS configuration parameters

Optional AWS configuration parameters are described in the following table:

<table>
<caption>Optional AWS parameters</caption>
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
<td style="text-align: left;"><pre><code>compute:
  platform:
    aws:
      amiID:</code></pre></td>
<td style="text-align: left;"><p>The AWS AMI used to boot compute machines for the cluster. This is required for regions that require a custom RHCOS AMI.</p>
<p><strong>Value:</strong> Any published or custom RHCOS AMI that belongs to the set AWS region. See <em>RHCOS AMIs for AWS infrastructure</em> for available AMI IDs.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>compute:
  platform:
    aws:
      iamProfile:</code></pre></td>
<td style="text-align: left;"><p>The name of the IAM instance profile that you use for the machine. If you want the installation program to create the IAM instance profile for you, do not use the <code>iamProfile</code> parameter. You can specify either the <code>iamProfile</code> or <code>iamRole</code> parameter, but you cannot specify both.</p>
<p><strong>Value:</strong> String</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>compute:
  platform:
    aws:
      iamRole:</code></pre></td>
<td style="text-align: left;"><p>The name of the IAM instance role that you use for the machine. When you specify an IAM role, the installation program creates an instance profile. If you want the installation program to create the IAM instance role for you, do not select the <code>iamRole</code> parameter. You can specify either the <code>iamRole</code> or <code>iamProfile</code> parameter, but you cannot specify both.</p>
<p><strong>Value:</strong> String</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>compute:
  platform:
    aws:
      rootVolume:
        iops:</code></pre></td>
<td style="text-align: left;"><p>The Input/Output Operations Per Second (IOPS) that is reserved for the root volume.</p>
<p><strong>Value:</strong> Integer, for example <code>4000</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>compute:
  platform:
    aws:
      rootVolume:
        size:</code></pre></td>
<td style="text-align: left;"><p>The size in GiB of the root volume.</p>
<p><strong>Value:</strong> Integer, for example <code>500</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>compute:
  platform:
    aws:
      rootVolume:
        type:</code></pre></td>
<td style="text-align: left;"><p>The type of the root volume.</p>
<p><strong>Value:</strong> Valid <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSVolumeTypes.html">AWS EBS volume type</a>, such as <code>io1</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>compute:
  platform:
    aws:
      rootVolume:
        throughput:</code></pre></td>
<td style="text-align: left;"><p>The maximum throughput of the root volume. This throughput can be customized only for the gp3 volume type. The minimum value is 125 MiB/s and the maximum value is 2000 MiB/s.</p>
<p><strong>Value:</strong> Integer, for example <code>1000</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>compute:
  platform:
    aws:
      rootVolume:
        kmsKeyARN:</code></pre></td>
<td style="text-align: left;"><p>The Amazon Resource Name (key ARN) of a KMS key. This is required to encrypt operating system volumes of worker nodes with a specific KMS key.</p>
<p><strong>Value:</strong> Valid <a href="https://docs.aws.amazon.com/kms/latest/developerguide/find-cmk-id-arn.html">key ID or the key ARN</a>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>compute:
  platform:
    aws:
      type:</code></pre></td>
<td style="text-align: left;"><p>The EC2 instance type for the compute machines.</p>
<p><strong>Value:</strong> Valid AWS instance type, such as <code>m4.2xlarge</code>. See the "Tested instance types for AWS" table on the "Installing a cluster on AWS with customizations" page.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>compute:
  platform:
    aws:
      zones:</code></pre></td>
<td style="text-align: left;"><p>The availability zones where the installation program creates machines for the compute machine pool. If you provide your own VPC, you must provide a subnet in that availability zone.</p>
<p><strong>Value:</strong> A list of valid AWS availability zones, such as <code>us-east-1c</code>, in a <a href="https://yaml.org/spec/1.2/spec.html#sequence//">YAML sequence</a>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>compute:
  platform:
    aws:
      hostPlacement:
        affinity:</code></pre></td>
<td style="text-align: left;"><p>Specifies the affinity setting for placing compute machines on AWS Dedicated Hosts. When set to <code>DedicatedHost</code>, machines are pinned to the specific Dedicated Hosts listed in the <code>dedicatedHost</code> field. If a machine is stopped and restarted, the machine returns to the same physical host. When set to <code>AnyAvailable</code>, machines are not pinned to specific Dedicated Hosts. If a machine is stopped and restarted, AWS can place the machine on any available Dedicated Host that matches the instance type and availability zone.</p>
<div class="important">
<div class="title">
&#10;</div>
<p>AWS Dedicated Host support is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.</p>
<p>For more information about the support scope of Red Hat Technology Preview features, see <a href="https://access.redhat.com/support/offerings/techpreview/">Technology Preview Features Support Scope</a>.</p>
</div>
<p><strong>Value:</strong> <code>DedicatedHost</code> or <code>AnyAvailable</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>compute:
  platform:
    aws:
      hostPlacement:
        dedicatedHost:</code></pre></td>
<td style="text-align: left;"><p>A list of AWS Dedicated Host entries for compute machines. Required when <code>hostPlacement.affinity</code> is set to <code>DedicatedHost</code>. Must be omitted when <code>hostPlacement.affinity</code> is set to <code>AnyAvailable</code>.</p>
<div class="important">
<div class="title">
&#10;</div>
<p>AWS Dedicated Host support is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.</p>
<p>For more information about the support scope of Red Hat Technology Preview features, see <a href="https://access.redhat.com/support/offerings/techpreview/">Technology Preview Features Support Scope</a>.</p>
</div>
<p><strong>Value:</strong> A list of objects.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>compute:
  platform:
    aws:
      hostPlacement:
        dedicatedHost:
        - id:</code></pre></td>
<td style="text-align: left;"><p>The ID of the AWS Dedicated Host. The value must start with <code>h-</code> followed by 17 lowercase hexadecimal characters.</p>
<div class="important">
<div class="title">
&#10;</div>
<p>AWS Dedicated Host support is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.</p>
<p>For more information about the support scope of Red Hat Technology Preview features, see <a href="https://access.redhat.com/support/offerings/techpreview/">Technology Preview Features Support Scope</a>.</p>
</div>
<p><strong>Value:</strong> String, for example <code>h-015c6d3ffa1d43d38</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>controlPlane:
  platform:
    aws:
      amiID:</code></pre></td>
<td style="text-align: left;"><p>The AWS AMI used to boot control plane machines for the cluster. This is required for regions that require a custom RHCOS AMI.</p>
<p><strong>Value:</strong> Any published or custom RHCOS AMI that belongs to the set AWS region. See <em>RHCOS AMIs for AWS infrastructure</em> for available AMI IDs.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>controlPlane:
  platform:
    aws:
      iamProfile:</code></pre></td>
<td style="text-align: left;"><p>The name of the IAM instance profile that you use for the machine. If you want the installation program to create the IAM instance profile for you, do not use the <code>iamProfile</code> parameter. You can specify either the <code>iamProfile</code> or <code>iamRole</code> parameter, but you cannot specify both.</p>
<p><strong>Value:</strong> String</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>controlPlane:
  platform:
    aws:
      iamRole:</code></pre></td>
<td style="text-align: left;"><p>The name of the IAM instance role that you use for the machine. When you specify an IAM role, the installation program creates an instance profile. If you want the installation program to create the IAM instance role for you, do not use the <code>iamRole</code> parameter. You can specify either the <code>iamRole</code> or <code>iamProfile</code> parameter, but you cannot specify both.</p>
<p><strong>Value:</strong> String</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>controlPlane:
  platform:
    aws:
      rootVolume:
        iops:</code></pre></td>
<td style="text-align: left;"><p>The Input/Output Operations Per Second (IOPS) that is reserved for the root volume on control plane machines.</p>
<p><strong>Value:</strong> Integer, for example <code>4000</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>controlPlane:
  platform:
    aws:
      rootVolume:
        size:</code></pre></td>
<td style="text-align: left;"><p>The size in GiB of the root volume for control plane machines.</p>
<p><strong>Value:</strong> Integer, for example <code>500</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>controlPlane:
  platform:
    aws:
      rootVolume:
        type:</code></pre></td>
<td style="text-align: left;"><p>The type of the root volume for control plane machines.</p>
<p><strong>Value:</strong> Valid <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSVolumeTypes.html">AWS EBS volume type</a>, such as <code>io1</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>controlPlane:
  platform:
    aws:
      rootVolume:
        throughput:</code></pre></td>
<td style="text-align: left;"><p>The maximum throughput of the root volume. This throughput can be customized only for the gp3 volume type. The minimum value is 125 MiB/s and the maximum value is 2000 MiB/s.</p>
<p><strong>Value:</strong> Integer, for example <code>1000</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>controlPlane:
  platform:
    aws:
      rootVolume:
        kmsKeyARN:</code></pre></td>
<td style="text-align: left;"><p>The Amazon Resource Name (key ARN) of a KMS key. This is required to encrypt operating system volumes of control plane nodes with a specific KMS key.</p>
<p><strong>Value:</strong> Valid <a href="https://docs.aws.amazon.com/kms/latest/developerguide/find-cmk-id-arn.html">key ID and the key ARN</a>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>controlPlane:
  platform:
    aws:
      type:</code></pre></td>
<td style="text-align: left;"><p>The EC2 instance type for the control plane machines.</p>
<p><strong>Value:</strong> Valid AWS instance type, such as <code>m6i.xlarge</code>. See the "Tested instance types for AWS" table on the "Installing a cluster on AWS with customizations" page.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>controlPlane:
  platform:
    aws:
      zones:</code></pre></td>
<td style="text-align: left;"><p>The availability zones where the installation program creates machines for the control plane machine pool.</p>
<p><strong>Value:</strong> A list of valid AWS availability zones, such as <code>us-east-1c</code>, in a <a href="https://yaml.org/spec/1.2/spec.html#sequence//">YAML sequence</a>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>platform:
  aws:
    amiID:</code></pre></td>
<td style="text-align: left;"><p>The AWS AMI used to boot all machines for the cluster. If set, the AMI must belong to the same region as the cluster. This is required for regions that require a custom RHCOS AMI.</p>
<p><strong>Value:</strong> Any published or custom RHCOS AMI that belongs to the set AWS region. See <em>RHCOS AMIs for AWS infrastructure</em> for available AMI IDs.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>platform:
  aws:
    hostedZone:</code></pre></td>
<td style="text-align: left;"><p>An existing Route 53 private hosted zone for the cluster. You can only use a pre-existing hosted zone when also supplying your own VPC. The hosted zone must already be associated with the user-provided VPC before installation. Also, the domain of the hosted zone must be the cluster domain or a parent of the cluster domain. If undefined, the installation program creates a new hosted zone.</p>
<p><strong>Value:</strong> String, for example <code>Z3URY6TWQ91KVV</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>platform:
  aws:
    hostedZoneRole:</code></pre></td>
<td style="text-align: left;"><p>An Amazon Resource Name (ARN) for an existing IAM role in the account containing the specified hosted zone. The installation program and cluster operators assume this role when performing operations on the hosted zone. Use this parameter only when you are installing a cluster into a shared VPC.</p>
<p><strong>Value:</strong> String, for example <code>arn:aws:iam::1234567890:role/shared-vpc-role</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>platform:
  aws:
    userProvisionedDNS:</code></pre></td>
<td style="text-align: left;"><p>Enables user-provisioned DNS instead of the default cluster-provisioned DNS solution. If you use this feature, you must provide your own DNS solution that includes records for <code>api.&lt;cluster_name&gt;.&lt;base_domain&gt;.</code> and <code>*.apps.&lt;cluster_name&gt;.&lt;base_domain&gt;.</code>. <code>userProvisionedDNS</code> is a Technology Preview feature.</p>
<p><strong>Value:</strong> <code>Enabled</code> or <code>Disabled</code>. The default value is <code>Disabled</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>platform:
  aws:
    region:</code></pre></td>
<td style="text-align: left;"><p>The AWS region that the installation program creates all cluster resources in.</p>
<p><strong>Value:</strong> Any valid <a href="https://docs.aws.amazon.com/general/latest/gr/rande.html">AWS region</a>, such as <code>us-east-1</code>. You can use the AWS CLI to access the regions available based on your selected instance type by running the following command:</p>
<pre class="terminal"><code>$ aws ec2 describe-instance-type-offerings --filters Name=instance-type,Values=c7g.xlarge</code></pre>
<div class="important">
<div class="title">
&#10;</div>
<p>When running on ARM based AWS instances, ensure that you enter a region where AWS Graviton processors are available. See <a href="https://aws.amazon.com/ec2/graviton/#Global_availability">Global availability</a> map in the AWS documentation. Currently, AWS Graviton3 processors are only available in some regions.</p>
</div></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>platform:
  aws:
    serviceEndpoints:
      - name:
        url:</code></pre></td>
<td style="text-align: left;"><p>The AWS service endpoint name and URL. Custom endpoints are only required for cases where alternative AWS endpoints, such as FIPS, must be used. Custom API endpoints can be specified for EC2, S3, IAM, Elastic Load Balancing, Tagging, Route 53, and STS AWS services.</p>
<p><strong>Value:</strong> Valid <a href="https://docs.aws.amazon.com/general/latest/gr/rande.html">AWS service endpoint</a> name and valid <a href="https://docs.aws.amazon.com/general/latest/gr/rande.html">AWS service endpoint</a> URL.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>platform:
  aws:
    userTags:</code></pre></td>
<td style="text-align: left;"><p>A map of keys and values that the installation program adds as tags to all resources that it creates.</p>
<p><strong>Value:</strong> Any valid YAML map, such as key value pairs in the <code>&lt;key&gt;: &lt;value&gt;</code> format. For more information about AWS tags, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html">Tagging Your Amazon EC2 Resources</a> in the AWS documentation.</p>
<div class="note">
<div class="title">
&#10;</div>
<p>You can add up to 25 user-defined tags during installation. The remaining 25 tags are reserved for OpenShift Container Platform.</p>
</div></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>platform:
  aws:
    propagateUserTags:</code></pre></td>
<td style="text-align: left;"><p>A flag that directs in-cluster Operators to include the specified user tags in the tags of the AWS resources that the Operators create.</p>
<p><strong>Value:</strong> Boolean values, for example <code>true</code> or <code>false</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>platform:
  aws:
    publicIpv4Pool:</code></pre></td>
<td style="text-align: left;"><p>The public IPv4 pool ID that is used to allocate Elastic IPs (EIPs) when <code>publish</code> is set to <code>External</code>. You must provision and advertise the pool in the same AWS account and region of the cluster. You must ensure that you have 2n + 1 IPv4 addresses available in the pool where <em>n</em> is the total number of AWS zones used to deploy the Network Load Balancer (NLB) for API, NAT gateways, and bootstrap node. For more information about bring your own IP addresses (BYOIP) in AWS, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-byoip.html#byoip-onboard">Onboard your BYOIP</a>.</p>
<p><strong>Value:</strong> A valid <a href="https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-public-ipv4-pools.html">public IPv4 pool id</a></p>
<div class="note">
<div class="title">
&#10;</div>
<p>You can enable BYOIP only for customized installations that do not have any network restrictions.</p>
</div></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>platform:
  aws:
    bestEffortDeleteIgnition:</code></pre></td>
<td style="text-align: left;"><p>An optional flag that determines whether to ignore errors when deleting Ignition objects from the S3 bucket. By default, the installation program fails if it cannot delete the Ignition objects.</p>
<p><strong>Value:</strong> <code>true</code> or <code>false</code>. The default value is <code>false</code>, which causes the installation program to fail on S3 Ignition deletion errors.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>platform:
  aws:
    ipFamily:</code></pre></td>
<td style="text-align: left;"><p>The IP address family for networks used by the cluster. Specify <code>IPv4</code> for IPv4-only networking, <code>DualStackIPv4Primary</code> for dual-stack networking with IPv4 as the primary address family, or <code>DualStackIPv6Primary</code> for dual-stack networking with IPv6 as the primary address family. When using dual-stack, the VPC and subnets must be configured with both IPv4 and IPv6 CIDR blocks.</p>
<p>Consider the following requirements if you use dual-stack networking:</p>
<ul>
<li><p>All API and Ingress load balancers must be Network Load Balancers (NLB). Classic Load Balancers (CLB) do not support IPv6 addressing.</p></li>
<li><p>All machines in a dual-stack cluster must be Nitro-based and support IPv6 addressing.</p></li>
<li><p>If you are installing a cluster using existing subnets, all provided subnets must be configured with dual-stack address pools.</p></li>
<li><p>If you are installing a cluster using Local Zones, you must provide dual-stack subnets. The installation program cannot automatically provision dual-stack subnets in Local Zones.</p></li>
<li><p>Installing a cluster using dual-stack networking is not supported in Wavelength Zones.</p></li>
</ul>
<div class="important">
<div class="title">
&#10;</div>
<p>Dual-stack networking on AWS is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process. For more information about the support scope of Red Hat Technology Preview features, see <a href="https://access.redhat.com/support/offerings/techpreview/">Technology Preview Features Support Scope</a>.</p>
</div>
<p><strong>Value:</strong> "IPv4", "DualStackIPv4Primary", or "DualStackIPv6Primary". The default value is "IPv4".</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>platform:
  aws:
    vpc:
      subnets:</code></pre></td>
<td style="text-align: left;"><p>A list of subnets in an existing VPC to be used in place of automatically created subnets. You specify a subnet by providing the subnet ID and an optional list of roles that apply to that subnet. If you specify subnet IDs but do not specify roles for any subnet, the subnets' roles are decided automatically. If you do not specify any roles, you must ensure that any other subnets in your VPC have the <code>kubernetes.io/cluster/.: .</code> or <code>kubernetes.io/cluster/unmanaged: true</code> tags.</p>
<p>The subnets must be part of the same <code>networking.machineNetwork[].cidr</code> ranges that you specify. If you provide dual-stack subnets using this parameter, you must specify IPv6 entries in the <code>networking.machineNetwork[].cidr</code> parameter.</p>
<p>For a public cluster, specify a public and a private subnet for each availability zone.</p>
<p>For a private cluster, specify a private subnet for each availability zone.</p>
<p>For clusters that use AWS Local Zones, you must add AWS Local Zone subnets to this list to ensure edge machine pool creation.</p>
<p><strong>Value:</strong> List of pairs of <code>id</code> and <code>roles</code> parameters.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>platform:
  aws:
    vpc:
      subnets:
      - id:</code></pre></td>
<td style="text-align: left;"><p>The ID of an existing subnet to be used in place of a subnet created by the installation program.</p>
<p><strong>Value:</strong> String. The subnet ID must be a unique ID containing only alphanumeric characters, beginning with "subnet-". The ID must be exactly 24 characters long.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>platform:
  aws:
    vpc:
      subnets:
      - id:
        roles:
        - type:</code></pre></td>
<td style="text-align: left;"><p>One or more roles that apply to the subnet specified by <code>platform.aws.vpc.subnets.id</code>. If you specify a role for any subnet, each subnet must have at least one assigned role, and the <code>ClusterNode</code>, <code>IngressControllerLB</code>, <code>ControlPlaneExternalLB</code>, <code>BootstrapNode</code>, and <code>ControlPlaneInternalLB</code> roles must be assigned to at least one subnet. However, if the cluster scope is internal, then the <code>ControlPlaneExternalLB</code> role is not required.</p>
<p>You can only assign the <code>EdgeNode</code> role to subnets in AWS Local Zones.</p>
<p><strong>Value:</strong> List of one or more role types. Valid values include <code>ClusterNode</code>, <code>EdgeNode</code>, <code>BootstrapNode</code>, <code>IngressControllerLB</code>, <code>ControlPlaneExternalLB</code>, and <code>ControlPlaneInternalLB</code>.</p></td>
</tr>
</tbody>
</table>
