<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Before you deploy an OpenShift Container Platform cluster on Microsoft Azure, you create the `install-config.yaml` file and provide parameters to customize your cluster and the platform that hosts it. You can then modify the `install-config.yaml` file to customize your cluster further.

# Available installation configuration parameters for Azure

To customize your cluster installation, configuration parameters are available to use in the `install-config.yaml` file.

The following tables specify the required, optional, and Azure-specific installation configuration parameters that you can set as part of the installation process.

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

Only IPv4 addresses are supported.

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
<span id="cb4-4"><a href="#cb4-4" aria-hidden="true" tabindex="-1"></a><span class="at">    </span><span class="fu">hostPrefix</span><span class="kw">:</span><span class="at"> </span><span class="dv">23</span></span></code></pre></div></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>networking:
  clusterNetwork:
    cidr:</code></pre></td>
<td style="text-align: left;"><p>Required if you use <code>networking.clusterNetwork</code>. An IP address block.</p>
<p>An IPv4 network.</p>
<p><strong>Value:</strong> An IP address block in Classless Inter-Domain Routing (CIDR) notation. The prefix length for an IPv4 block is between <code>0</code> and <code>32</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>networking:
  clusterNetwork:
    hostPrefix:</code></pre></td>
<td style="text-align: left;"><p>The subnet prefix length to assign to each individual node. For example, if <code>hostPrefix</code> is set to <code>23</code> then each node is assigned a <code>/23</code> subnet out of the given <code>cidr</code>. A <code>hostPrefix</code> value of <code>23</code> provides 510 (2^(32 - 23) - 2) pod IP addresses.</p>
<p><strong>Value:</strong> A subnet prefix.</p>
<p>The default value is <code>23</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>networking:
  serviceNetwork:</code></pre></td>
<td style="text-align: left;"><p>The IP address block for services. The default value is <code>172.30.0.0/16</code>.</p>
<p>The OVN-Kubernetes network plugins supports only a single IP address block for the service network.</p>
<p><strong>Value:</strong> An array with an IP address block in CIDR format. For example:</p>
<div class="sourceCode" id="cb8"><pre class="sourceCode yaml"><code class="sourceCode yaml"><span id="cb8-1"><a href="#cb8-1" aria-hidden="true" tabindex="-1"></a><span class="fu">networking</span><span class="kw">:</span></span>
<span id="cb8-2"><a href="#cb8-2" aria-hidden="true" tabindex="-1"></a><span class="at">  </span><span class="fu">serviceNetwork</span><span class="kw">:</span></span>
<span id="cb8-3"><a href="#cb8-3" aria-hidden="true" tabindex="-1"></a><span class="at">   </span><span class="kw">-</span><span class="at"> 172.30.0.0/16</span></span></code></pre></div></td>
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
<p><strong>Value:</strong> <code>Internal</code>, <code>External</code>, or <code>Mixed</code>. To deploy a private cluster that cannot be accessed from the internet, set the <code>publish</code> parameter to <code>Internal</code>. The default value is <code>External</code>. To deploy a cluster where the API and the ingress server have different publishing strategies, set <code>publish</code> to <code>Mixed</code> and use the <code>operatorPublishingStrategy</code> parameter.</p></td>
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

> [!IMPORTANT]
> Setting this parameter to `Manual` enables alternatives to storing administrator-level secrets in the `kube-system` project, which require additional configuration steps. For more information, see "Alternatives to storing administrator-level secrets in the kube-system project".

## Additional Azure configuration parameters

Additional Azure configuration parameters are described in the following table.

> [!NOTE]
> By default, if you specify availability zones in the `install-config.yaml` file, the installation program distributes the control plane machines and the compute machines across [these availability zones](https://azure.microsoft.com/en-us/global-infrastructure/availability-zones/) within [a region](https://azure.microsoft.com/en-us/global-infrastructure/regions). To ensure high availability for your cluster, select a region with at least three availability zones. If your region contains fewer than three availability zones, the installation program places more than one control plane machine in the available zones.

<table>
<caption>Additional Azure parameters</caption>
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
    azure:
      bootDiagnostics:
        type:</code></pre></td>
<td style="text-align: left;"><p>Enables boot diagnostics collection for compute machines. The <code>type</code> field specifies the Azure boot diagnostics type for the created compute machines.</p>
<p>The following values are associated with the boot diagnostics type:</p>
<dl>
<dt><code>UserManaged</code></dt>
<dd>
<p>When you set <code>type</code> to <code>UserManaged</code>, you must provide values for <code>resourceGroup</code> and <code>storageAccountName</code>. For <code>storageAccountName</code> and OpenShift Container Platform cluster nodes, use the same region and subscription.</p>
</dd>
<dt><code>Managed</code></dt>
<dd>
<p>When you set <code>type</code> to <code>Managed</code>, Azure stores the boot diagnostics data blobs in a managed storage account.</p>
</dd>
<dt><code>Disabled</code></dt>
<dd>
<p>When you set <code>type</code> to <code>Disabled</code>, you turn off the parameter.</p>
</dd>
</dl>
<p><strong>Value:</strong> String, for example <code>Enabled</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>compute:
  platform:
    azure:
      bootDiagnostics:
        resourceGroup:</code></pre></td>
<td style="text-align: left;"><p>Specifies the name of the Azure resource group that contains the diagnostic storage account for compute machines. Use <code>resourceGroup</code> only when you set <code>type</code> to <code>UserManaged</code>.</p>
<p><strong>Value:</strong> String.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>compute:
  platform:
    azure:
      bootDiagnostics:
        storageAccountName:</code></pre></td>
<td style="text-align: left;"><p>Specifies the Azure storage account to store the diagnostic logs for compute machines. Use <code>storageAccountName</code> only when you set`type` to <code>UserManaged</code>.</p>
<p><strong>Value:</strong> String.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>compute:
  platform:
    azure:
      encryptionAtHost:</code></pre></td>
<td style="text-align: left;"><p>Enables host-level encryption for compute machines. You can enable this encryption alongside user-managed server-side encryption. This feature encrypts temporary, ephemeral, cached and un-managed disks on the VM host. This is not a prerequisite for user-managed server-side encryption.</p>
<p><strong>Value:</strong> <code>true</code> or <code>false</code>. The default is <code>false</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>compute:
  platform:
    azure:
      osDisk:
        diskSizeGB:</code></pre></td>
<td style="text-align: left;"><p>The Azure disk size for the VM.</p>
<p><strong>Value:</strong> Integer that represents the size of the disk in GB. The default is <code>128</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>compute:
  platform:
    azure:
      osDisk:
        diskType:</code></pre></td>
<td style="text-align: left;"><p>Defines the type of disk.</p>
<p><strong>Value:</strong> <code>standard_LRS</code>, <code>premium_LRS</code>, or <code>standardSSD_LRS</code>. The default is <code>premium_LRS</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>compute:
  platform:
    azure:
      ultraSSDCapability:</code></pre></td>
<td style="text-align: left;"><p>Enables the use of Azure ultra disks for persistent storage on compute nodes. This requires that your Azure region and zone have ultra disks available.</p>
<p><strong>Value:</strong> <code>Enabled</code>, <code>Disabled</code>. The default is <code>Disabled</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>compute:
  platform:
    azure:
      osDisk:
        diskEncryptionSet:
          resourceGroup:</code></pre></td>
<td style="text-align: left;"><p>The name of the Azure resource group that contains the disk encryption set from the installation prerequisites. This resource group should be different from the resource group where you install the cluster to avoid deleting your Azure encryption key when the cluster is destroyed. This value is only necessary if you intend to install the cluster with user-managed disk encryption.</p>
<p><strong>Value:</strong> String, for example <code>production_encryption_resource_group</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>compute:
  platform:
    azure:
      osDisk:
        diskEncryptionSet:
          name:</code></pre></td>
<td style="text-align: left;"><p>The name of the disk encryption set that contains the encryption key from the installation prerequisites.</p>
<p><strong>Value:</strong> String, for example <code>production_disk_encryption_set</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>compute:
  platform:
    azure:
      osDisk:
        diskEncryptionSet:
          subscriptionId:</code></pre></td>
<td style="text-align: left;"><p>Defines the Azure subscription of the disk encryption set where the disk encryption set resides. This secondary disk encryption set is used to encrypt compute machines.</p>
<p><strong>Value:</strong> String, in the format <code>00000000-0000-0000-0000-000000000000</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>compute:
  platform:
    azure:
      osImage:
        publisher:</code></pre></td>
<td style="text-align: left;"><p>Optional. By default, the installation program downloads and installs the Red Hat Enterprise Linux CoreOS (RHCOS) image that is used to boot compute machines. You can override the default behavior by using a custom RHCOS image that is available from the Azure Marketplace. The installation program uses this image for compute machines only.</p>
<p><strong>Value:</strong> String. The name of the image publisher.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>compute:
  platform:
    azure:
      osImage:
        offer:</code></pre></td>
<td style="text-align: left;"><p>The name of Azure Marketplace offer that is associated with the custom RHCOS image. If you use <code>compute.platform.azure.osImage.publisher</code>, this field is required.</p>
<p><strong>Value:</strong> String. The name of the image offer.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>compute:
  platform:
    azure:
      osImage:
        sku:</code></pre></td>
<td style="text-align: left;"><p>An instance of the Azure Marketplace offer. If you use <code>compute.platform.azure.osImage.publisher</code>, this field is required.</p>
<p><strong>Value:</strong> String. The SKU of the image offer.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>compute:
  platform:
    azure:
      osImage:
        version:</code></pre></td>
<td style="text-align: left;"><p>The version number of the image SKU. If you use <code>compute.platform.azure.osImage.publisher</code>, this field is required.</p>
<p><strong>Value:</strong> String. The version of the image to use.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>compute:
  platform:
    azure:
      identity:
        type:</code></pre></td>
<td style="text-align: left;"><p>The type of identity used for compute virtual machines. The <code>UserAssigned</code> identity is a standalone Azure resource provided by the user and assigned to compute virtual machines. If you specify <code>identity.type</code> as <code>UserAssigned</code>, but do not provide a user-assigned identity, the installation program creates the identity. If you provide a user-assigned identity, the Azure account that you use to create the identity must have either the "User Access Administrator" or "RBAC Access Admin" roles.</p>
<p><strong>Value:</strong> <code>UserAssigned</code> or <code>None</code>. If you do not specify a value, the installation program generates a user-assigned identity.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>compute:
  platform:
    azure:
      identity:
        userAssignedIdentities:
        - name:
          resourceGroup:
          subscription:</code></pre></td>
<td style="text-align: left;"><p>A group of parameters that specify the name of the user-assigned identity, and the resource group and subscription that contain the identity. All three values must be provided to specify a user-assigned identity. Only one user-assigned identity can be supplied. Supplying more than one user-assigned identity is an experimental feature, which may be enabled with the <code>MachineAPIMigration</code> feature gate.</p>
<p><strong>Value:</strong> Array of strings.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>compute:
  platform:
    azure:
      vmNetworkingType:</code></pre></td>
<td style="text-align: left;"><p>Enables accelerated networking. Accelerated networking enables single root I/O virtualization (SR-IOV) to a VM, improving its networking performance. If instance type of compute machines support <code>Accelerated</code> networking, by default, the installation program enables <code>Accelerated</code> networking, otherwise the default networking type is <code>Basic</code>.</p>
<p><strong>Value:</strong> <code>Accelerated</code> or <code>Basic</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>compute:
  platform:
    azure:
      type:</code></pre></td>
<td style="text-align: left;"><p>Defines the Azure instance type for compute machines.</p>
<p><strong>Value:</strong> String</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>compute:
  platform:
    azure:
      zones:</code></pre></td>
<td style="text-align: left;"><p>The availability zones where the installation program creates compute machines.</p>
<p><strong>Value:</strong> String list</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>compute:
  platform:
    azure:
      settings:
        securityType:</code></pre></td>
<td style="text-align: left;"><p>Enables confidential VMs or trusted launch for compute nodes. This option is not enabled by default.</p>
<p><strong>Value:</strong> <code>ConfidentialVM</code> or <code>TrustedLaunch</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>compute:
  platform:
    azure:
      settings:
        confidentialVM:
          uefiSettings:
            secureBoot:</code></pre></td>
<td style="text-align: left;"><p>Enables secure boot on compute nodes if you are using confidential VMs.</p>
<p><strong>Value:</strong> <code>Enabled</code> or <code>Disabled</code>. The default is <code>Disabled</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>compute:
  platform:
    azure:
      settings:
        confidentialVM:
          uefiSettings:
            virtualizedTrustedPlatformModule:</code></pre></td>
<td style="text-align: left;"><p>Enables the virtualized Trusted Platform Module (vTPM) feature on compute nodes if you are using confidential VMs.</p>
<p><strong>Value:</strong> <code>Enabled</code> or <code>Disabled</code>. The default is <code>Disabled</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>compute:
  platform:
    azure:
      settings:
        trustedLaunch:
          uefiSettings:
            secureBoot:</code></pre></td>
<td style="text-align: left;"><p>Enables secure boot on compute nodes if you are using trusted launch.</p>
<p><strong>Value:</strong> <code>Enabled</code> or <code>Disabled</code>. The default is <code>Disabled</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>compute:
  platform:
    azure:
      settings:
        trustedLaunch:
          uefiSettings:
            virtualizedTrustedPlatformModule:</code></pre></td>
<td style="text-align: left;"><p>Enables the vTPM feature on compute nodes if you are using trusted launch.</p>
<p><strong>Value:</strong> <code>Enabled</code> or <code>Disabled</code>. The default is <code>Disabled</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>compute:
  platform:
    azure:
      osDisk:
        securityProfile:
          securityEncryptionType:</code></pre></td>
<td style="text-align: left;"><p>Enables the encryption of the virtual machine guest state for compute nodes. This parameter can only be used if you use Confidential VMs.</p>
<p><strong>Value:</strong> <code>VMGuestStateOnly</code> is the only supported value.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>controlPlane:
  diskSetup:</code></pre></td>
<td style="text-align: left;"><p>Specifies node component information for dedicated disk configuration.</p>
<p><strong>Value:</strong> Array of objects. Each object includes the <code>type</code> and <code>etcd</code> parameters as described in the following rows of the table.</p>
<div class="important">
<div class="title">
&#10;</div>
<p>Dedicated disk for <code>etcd</code> on Microsoft Azure is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process. For more information about the support scope of Red Hat Technology Preview features, see <a href="https://access.redhat.com/support/offerings/techpreview/">Technology Preview Features Support Scope</a>.</p>
</div></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>controlPlane:
  diskSetup:
  - type:</code></pre></td>
<td style="text-align: left;"><p>Specifies which node component type to assign a dedicated disk.</p>
<p><strong>Value:</strong> <code>etcd</code> is the only supported value.</p>
<div class="important">
<div class="title">
&#10;</div>
<p>Dedicated disk for <code>etcd</code> on Microsoft Azure is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process. For more information about the support scope of Red Hat Technology Preview features, see <a href="https://access.redhat.com/support/offerings/techpreview/">Technology Preview Features Support Scope</a>.</p>
</div></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>controlPlane:
  diskSetup:
  - etcd:</code></pre></td>
<td style="text-align: left;"><p>Specifies parameters for an <code>etcd</code> dedicated disk.</p>
<p><strong>Value</strong>: The <code>platformDiskID</code> object is the only supported value.</p>
<div class="important">
<div class="title">
&#10;</div>
<p>Dedicated disk for <code>etcd</code> on Microsoft Azure is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process. For more information about the support scope of Red Hat Technology Preview features, see <a href="https://access.redhat.com/support/offerings/techpreview/">Technology Preview Features Support Scope</a>.</p>
</div></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>controlPlane:
  diskSetup:
  - etcd:
      platformDiskID:</code></pre></td>
<td style="text-align: left;"><p>Specifies a name to identify the dedicated disk.</p>
<p><strong>Value:</strong> String. Must not exceed 12 characters.</p>
<div class="important">
<div class="title">
&#10;</div>
<p>Dedicated disk for <code>etcd</code> on Microsoft Azure is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process. For more information about the support scope of Red Hat Technology Preview features, see <a href="https://access.redhat.com/support/offerings/techpreview/">Technology Preview Features Support Scope</a>.</p>
</div></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>controlPlane:
  platform:
    azure:
      identity:
        type:</code></pre></td>
<td style="text-align: left;"><p>The type of identity used for control plane virtual machines. The <code>UserAssigned</code> identity is a standalone Azure resource provided by the user and assigned to control plane virtual machines. If you specify <code>identity.type</code> as <code>UserAssigned</code>, but do not provide a user-assigned identity, the installation program creates the identity. If you provide a user-assigned identity, the Azure account that you use to create the identity must have either the "User Access Administrator" or "RBAC Access Admin" roles.</p>
<p><strong>Value:</strong> <code>UserAssigned</code> or <code>None</code>. If you do not specify a value, the installation program generates a user-assigned identity.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>controlPlane:
  platform:
    azure:
      bootDiagnostics:
        type:</code></pre></td>
<td style="text-align: left;"><p>Enables boot diagnostics collection for control plane machines. The <code>type</code> field specifies the Azure boot diagnostics type for the created control plane machines.</p>
<p>The following values are associated with the boot diagnostics type:</p>
<dl>
<dt><code>UserManaged</code></dt>
<dd>
<p>When you set <code>type</code> to <code>UserManaged</code>, you must provide the values for <code>resourceGroup</code> and <code>storageAccountName</code>. For <code>storageAccountName</code> and OpenShift Container Platform cluster nodes, ensure that you use the same region and subscription.</p>
</dd>
<dt><code>Managed</code></dt>
<dd>
<p>When you set <code>type</code> to <code>Managed</code>, Azure stores the boot diagnostics data blobs in a managed storage account.</p>
</dd>
<dt><code>Disabled</code></dt>
<dd>
<p>When you set <code>type</code> to <code>Disabled</code>, you turn off the parameter.</p>
</dd>
</dl>
<p><strong>Value:</strong> String. For control plane machines, the default value is <code>Managed</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>controlPlane:
  platform:
    azure:
      identity:
        userAssignedIdentities:
        - name:
          resourceGroup:
          subscription:</code></pre></td>
<td style="text-align: left;"><p>A group of parameters that specify the name of the user-assigned identity, and the resource group and subscription that contain the identity. All three values must be provided to specify a user-assigned identity. Only one user-assigned identity can be supplied. Supplying more than one user-assigned identity is an experimental feature, which may be enabled with the <code>MachineAPIMigration</code> feature gate.</p>
<p><strong>Value:</strong> Array of strings.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>controlPlane:
  platform:
    azure:
      bootDiagnostics:
        resourceGroup:</code></pre></td>
<td style="text-align: left;"><p>Specifies the name of the Azure resource group that contains the diagnostic storage account for control plane machines. Use <code>resourceGroup</code> only when you set <code>type</code> to <code>UserManaged</code>.</p>
<p><strong>Value:</strong> String.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>controlPlane:
  platform:
    azure:
      bootDiagnostics:
        storageAccountName:</code></pre></td>
<td style="text-align: left;"><p>Specifies the Azure storage account to store the diagnostic logs for control plane machines. Use <code>storageAccountName</code> only when you set <code>type</code> to <code>UserManaged</code>.</p>
<p><strong>Value:</strong> String.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>controlPlane:
  platform:
    azure:
      dataDisks:</code></pre></td>
<td style="text-align: left;"><p>Specifies dedicated disk parameters.</p>
<p><strong>Value:</strong> Array of objects. Each object includes <code>nameSuffix</code>, <code>cachingType</code>, <code>diskSizeGB</code>, and <code>lun</code> as described in the following rows of the table.</p>
<div class="important">
<div class="title">
&#10;</div>
<p>Dedicated disk for <code>etcd</code> on Microsoft Azure is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process. For more information about the support scope of Red Hat Technology Preview features, see <a href="https://access.redhat.com/support/offerings/techpreview/">Technology Preview Features Support Scope</a>.</p>
</div></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>controlPlane:
  platform:
    azure:
      dataDisks:
      - nameSuffix:</code></pre></td>
<td style="text-align: left;"><p>Specifies the same value you defined for <code>platformDiskID</code>.</p>
<p><strong>Value:</strong> String.</p>
<div class="important">
<div class="title">
&#10;</div>
<p>Dedicated disk for <code>etcd</code> on Microsoft Azure is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process. For more information about the support scope of Red Hat Technology Preview features, see <a href="https://access.redhat.com/support/offerings/techpreview/">Technology Preview Features Support Scope</a>.</p>
</div></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>controlPlane:
  platform:
    azure:
      dataDisks:
      - cachingType:</code></pre></td>
<td style="text-align: left;"><p>Specifies the caching requirements for the disk.</p>
<p><strong>Value:</strong> <code>None</code> is the only value currently supported.</p>
<div class="important">
<div class="title">
&#10;</div>
<p>Dedicated disk for <code>etcd</code> on Microsoft Azure is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process. For more information about the support scope of Red Hat Technology Preview features, see <a href="https://access.redhat.com/support/offerings/techpreview/">Technology Preview Features Support Scope</a>.</p>
</div></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>controlPlane:
  platform:
    azure:
      dataDisks:
      - diskSizeGB:</code></pre></td>
<td style="text-align: left;"><p>Specifies a dedicated disk size in GB.</p>
<p><strong>Value:</strong> Integer greater than <code>0</code>.</p>
<div class="important">
<div class="title">
&#10;</div>
<p>Dedicated disk for <code>etcd</code> on Microsoft Azure is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process. For more information about the support scope of Red Hat Technology Preview features, see <a href="https://access.redhat.com/support/offerings/techpreview/">Technology Preview Features Support Scope</a>.</p>
</div></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>controlPlane:
  platform:
    azure:
      dataDisks:
      - lun:</code></pre></td>
<td style="text-align: left;"><p>Specifies a logical unit number (LUN) for the dedicated disk.</p>
<p><strong>Value:</strong> Integer from <code>0</code> through <code>63</code> that is not used by another disk.</p>
<div class="important">
<div class="title">
&#10;</div>
<p>Dedicated disk for <code>etcd</code> on Microsoft Azure is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process. For more information about the support scope of Red Hat Technology Preview features, see <a href="https://access.redhat.com/support/offerings/techpreview/">Technology Preview Features Support Scope</a>.</p>
</div></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>controlPlane:
  platform:
    azure:
      settings:
        securityType:</code></pre></td>
<td style="text-align: left;"><p>Enables confidential VMs or trusted launch for control plane nodes. This option is not enabled by default.</p>
<p><strong>Value:</strong> <code>ConfidentialVM</code> or <code>TrustedLaunch</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>controlPlane:
  platform:
    azure:
      settings:
        confidentialVM:
          uefiSettings:
            secureBoot:</code></pre></td>
<td style="text-align: left;"><p>Enables secure boot on control plane nodes if you are using confidential VMs.</p>
<p><strong>Value:</strong> <code>Enabled</code> or <code>Disabled</code>. The default is <code>Disabled</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>controlPlane:
  platform:
    azure:
      settings:
        confidentialVM:
          uefiSettings:
            virtualizedTrustedPlatformModule:</code></pre></td>
<td style="text-align: left;"><p>Enables the vTPM feature on control plane nodes if you are using confidential VMs.</p>
<p><strong>Value:</strong> <code>Enabled</code> or <code>Disabled</code>. The default is <code>Disabled</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>controlPlane:
  platform:
    azure:
      settings:
        trustedLaunch:
          uefiSettings:
            secureBoot:</code></pre></td>
<td style="text-align: left;"><p>Enables secure boot on control plane nodes if you are using trusted launch.</p>
<p><strong>Value:</strong> <code>Enabled</code> or <code>Disabled</code>. The default is <code>Disabled</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>controlPlane:
  platform:
    azure:
      settings:
        trustedLaunch:
          uefiSettings:
            virtualizedTrustedPlatformModule:</code></pre></td>
<td style="text-align: left;"><p>Enables the vTPM feature on control plane nodes if you are using trusted launch.</p>
<p><strong>Value:</strong> <code>Enabled</code> or <code>Disabled</code>. The default is <code>Disabled</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>controlPlane:
  platform:
    azure:
      osDisk:
        securityProfile:
          securityEncryptionType:</code></pre></td>
<td style="text-align: left;"><p>Enables the encryption of the virtual machine guest state for control plane nodes. This parameter can only be used if you use Confidential VMs.</p>
<p><strong>Value:</strong> <code>VMGuestStateOnly</code> is the only supported value.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>controlPlane:
  platform:
    azure:
      type:</code></pre></td>
<td style="text-align: left;"><p>Defines the Azure instance type for control plane machines.</p>
<p><strong>Value:</strong> String</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>controlPlane:
  platform:
    azure:
      zones:</code></pre></td>
<td style="text-align: left;"><p>The availability zones where the installation program creates control plane machines.</p>
<p><strong>Value:</strong> String list</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>platform:
  azure:
    defaultMachinePlatform:
       bootDiagnostics:
        type:</code></pre></td>
<td style="text-align: left;"><p>Enables boot diagnostics collection for all machines. The <code>type</code> field specifies the Azure boot diagnostics type for all the created machines.</p>
<p>The following values are associated with the boot diagnostics type:</p>
<dl>
<dt><code>UserManaged</code></dt>
<dd>
<p>When you set <code>type</code> to <code>UserManaged</code>, you must provide the values for <code>resourceGroup</code> and <code>storageAccountName</code>. For <code>storageAccountName</code> and OpenShift Container Platform cluster nodes, ensure that you use the same region and subscription.</p>
</dd>
<dt><code>Managed</code></dt>
<dd>
<p>When you set <code>type</code> to <code>Managed</code>, Azure stores the boot diagnostics data blobs in a managed storage account.</p>
</dd>
<dt><code>Disabled</code></dt>
<dd>
<p>When you set <code>type</code> to <code>Disabled</code>, you turn off the parameter.</p>
</dd>
</dl>
<p><strong>Value:</strong> String, for example <code>Enabled</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>platform:
  azure:
    defaultMachinePlatform:
       bootDiagnostics:
        resourceGroup:</code></pre></td>
<td style="text-align: left;"><p>Specifies the name of the Azure resource group that contains the diagnostic storage account for all machines. Use <code>resourceGroup</code> only when you set <code>type</code> to <code>UserManaged</code>.</p>
<p><strong>Value:</strong> String.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>platform:
  azure:
    defaultMachinePlatform:
       bootDiagnostics:
        storageAccountName:</code></pre></td>
<td style="text-align: left;"><p>Specifies the Azure storage account to store the diagnostic logs for all machines. Use <code>storageAccountName</code> only when you set <code>type</code> to <code>UserManaged</code>.</p>
<p><strong>Value:</strong> String.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>platform:
  azure:
    defaultMachinePlatform:
      settings:
        securityType:</code></pre></td>
<td style="text-align: left;"><p>Enables confidential VMs or trusted launch for all nodes. This option is not enabled by default.</p>
<p><strong>Value:</strong> <code>ConfidentialVM</code> or <code>TrustedLaunch</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>platform:
  azure:
    defaultMachinePlatform:
      settings:
        confidentialVM:
          uefiSettings:
            secureBoot:</code></pre></td>
<td style="text-align: left;"><p>Enables secure boot on all nodes if you are using confidential VMs.</p>
<p><strong>Value:</strong> <code>Enabled</code> or <code>Disabled</code>. The default is <code>Disabled</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>platform:
  azure:
    defaultMachinePlatform:
      settings:
        confidentialVM:
          uefiSettings:
            virtualizedTrustedPlatformModule:</code></pre></td>
<td style="text-align: left;"><p>Enables the virtualized Trusted Platform Module (vTPM) feature on all nodes if you are using confidential VMs.</p>
<p><strong>Value:</strong> <code>Enabled</code> or <code>Disabled</code>. The default is <code>Disabled</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>platform:
  azure:
    defaultMachinePlatform:
      settings:
        trustedLaunch:
          uefiSettings:
            secureBoot:</code></pre></td>
<td style="text-align: left;"><p>Enables secure boot on all nodes if you are using trusted launch.</p>
<p><strong>Value:</strong> <code>Enabled</code> or <code>Disabled</code>. The default is <code>Disabled</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>platform:
  azure:
    defaultMachinePlatform:
      settings:
        trustedLaunch:
          uefiSettings:
            virtualizedTrustedPlatformModule:</code></pre></td>
<td style="text-align: left;"><p>Enables the vTPM feature on all nodes if you are using trusted launch.</p>
<p><strong>Value:</strong> <code>Enabled</code> or <code>Disabled</code>. The default is <code>Disabled</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>platform:
  azure:
    defaultMachinePlatform:
      identity:
        type:</code></pre></td>
<td style="text-align: left;"><p>The type of identity used for all virtual machines. The <code>UserAssigned</code> identity is a standalone Azure resource provided by the user and assigned to all virtual machines. If you specify <code>identity.type</code> as <code>UserAssigned</code>, but do not provide a user-assigned identity, the installation program creates the identity. If you provide a user-assigned identity, the Azure account that you use to create the identity must have either the "User Access Administrator" or "RBAC Access Admin" roles.</p>
<p><strong>Value:</strong> <code>UserAssigned</code> or <code>None</code>. If you do not specify a value, the installation program generates a user-assigned identity.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>platform:
  azure:
    defaultMachinePlatform:
      identity:
        userAssignedIdentities:
        - name:
          resourceGroup:
          subscription:</code></pre></td>
<td style="text-align: left;"><p>A group of parameters that specify the name of the user-assigned identity, and the resource group and subscription that contain the identity. All three values must be provided to specify a user-assigned identity. Only one user-assigned identity can be supplied. Supplying more than one user-assigned identity is an experimental feature, which may be enabled with the <code>MachineAPIMigration</code> feature gate.</p>
<p><strong>Value:</strong> Array of strings.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>platform:
  azure:
    defaultMachinePlatform:
      osDisk:
        securityProfile:
          securityEncryptionType:</code></pre></td>
<td style="text-align: left;"><p>Enables the encryption of the virtual machine guest state for all nodes. This parameter can only be used if you use Confidential VMs.</p>
<p><strong>Value:</strong> <code>VMGuestStateOnly</code> is the only supported value.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>platform:
  azure:
    defaultMachinePlatform:
      encryptionAtHost:</code></pre></td>
<td style="text-align: left;"><p>Enables host-level encryption for compute machines. You can enable this encryption alongside user-managed server-side encryption. This feature encrypts temporary, ephemeral, cached, and un-managed disks on the VM host. This parameter is not a prerequisite for user-managed server-side encryption.</p>
<p><strong>Value:</strong> <code>true</code> or <code>false</code>. The default is <code>false</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>platform:
  azure:
    defaultMachinePlatform:
      osDisk:
        diskEncryptionSet:
          name:</code></pre></td>
<td style="text-align: left;"><p>The name of the disk encryption set that contains the encryption key from the installation prerequisites.</p>
<p><strong>Value:</strong> String, for example, <code>production_disk_encryption_set</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>platform:
  azure:
    defaultMachinePlatform:
      osDisk:
        diskEncryptionSet:
          resourceGroup:</code></pre></td>
<td style="text-align: left;"><p>The name of the Azure resource group that contains the disk encryption set from the installation prerequisites. To avoid deleting your Azure encryption key when the cluster is destroyed, this resource group must be different from the resource group where you install the cluster. This value is necessary only if you intend to install the cluster with user-managed disk encryption.</p>
<p><strong>Value:</strong> String, for example, <code>production_encryption_resource_group</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>platform:
  azure:
    defaultMachinePlatform:
      osDisk:
        diskEncryptionSet:
          subscriptionId:</code></pre></td>
<td style="text-align: left;"><p>Defines the Azure subscription of the disk encryption set where the disk encryption set resides. This secondary disk encryption set is used to encrypt compute machines.</p>
<p><strong>Value:</strong> String, in the format <code>00000000-0000-0000-0000-000000000000</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>platform:
  azure:
    defaultMachinePlatform:
      osDisk:
        diskSizeGB:</code></pre></td>
<td style="text-align: left;"><p>The Azure disk size for the VM.</p>
<p><strong>Value:</strong> Integer that represents the size of the disk in GB. The default is <code>128</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>platform:
  azure:
    defaultMachinePlatform:
      osDisk:
        diskType:</code></pre></td>
<td style="text-align: left;"><p>Defines the type of disk.</p>
<p><strong>Value:</strong> <code>premium_LRS</code> or <code>standardSSD_LRS</code>. The default is <code>premium_LRS</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>platform:
  azure:
    defaultMachinePlatform:
      osImage:
        publisher:</code></pre></td>
<td style="text-align: left;"><p>Optional. By default, the installation program downloads and installs the Red Hat Enterprise Linux CoreOS (RHCOS) image that is used to boot control plane and compute machines. You can override the default behavior by using a custom RHCOS image that is available from the Azure Marketplace. The installation program uses this image for both types of machines. Control plane machines do not contribute to licensing costs when using the default image. But, if you apply an Azure Marketplace image for a control plane machine, usage costs do apply.</p>
<p><strong>Value:</strong> String. The name of the image publisher.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>platform:
  azure:
    defaultMachinePlatform:
      osImage:
        offer:</code></pre></td>
<td style="text-align: left;"><p>The name of Azure Marketplace offer that is associated with the custom RHCOS image. If you use <code>platform.azure.defaultMachinePlatform.osImage.publisher</code>, this field is required.</p>
<p><strong>Value:</strong> String. The name of the image offer.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>platform:
  azure:
    defaultMachinePlatform:
      osImage:
        sku:</code></pre></td>
<td style="text-align: left;"><p>An instance of the Azure Marketplace offer. If you use <code>platform.azure.defaultMachinePlatform.osImage.publisher</code>, this field is required.</p>
<p><strong>Value:</strong> String. The SKU of the image offer.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>platform:
  azure:
    defaultMachinePlatform:
      osImage:
        version:</code></pre></td>
<td style="text-align: left;"><p>The version number of the image SKU. If you use <code>platform.azure.defaultMachinePlatform.osImage.publisher</code>, this field is required.</p>
<p><strong>Value:</strong> String. The version of the image to use.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>platform:
  azure:
    defaultMachinePlatform:
      type:</code></pre></td>
<td style="text-align: left;"><p>The Azure instance type for control plane and compute machines.</p>
<p><strong>Value:</strong> The Azure instance type.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>platform:
  azure:
    defaultMachinePlatform:
      zones:</code></pre></td>
<td style="text-align: left;"><p>The availability zones where the installation program creates compute and control plane machines.</p>
<p><strong>Value:</strong> String list.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>controlPlane:
  platform:
    azure:
      encryptionAtHost:</code></pre></td>
<td style="text-align: left;"><p>Enables host-level encryption for control plane machines. You can enable this encryption alongside user-managed server-side encryption. This feature encrypts temporary, ephemeral, cached and un-managed disks on the VM host. This is not a prerequisite for user-managed server-side encryption.</p>
<p><strong>Value:</strong> <code>true</code> or <code>false</code>. The default is <code>false</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>controlPlane:
  platform:
    azure:
      osDisk:
        diskEncryptionSet:
          resourceGroup:</code></pre></td>
<td style="text-align: left;"><p>The name of the Azure resource group that contains the disk encryption set from the installation prerequisites. This resource group should be different from the resource group where you install the cluster to avoid deleting your Azure encryption key when the cluster is destroyed. This value is only necessary if you intend to install the cluster with user-managed disk encryption.</p>
<p><strong>Value:</strong> String, for example <code>production_encryption_resource_group</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>controlPlane:
  platform:
    azure:
      osDisk:
        diskEncryptionSet:
          name:</code></pre></td>
<td style="text-align: left;"><p>The name of the disk encryption set that contains the encryption key from the installation prerequisites.</p>
<p><strong>Value:</strong> String, for example <code>production_disk_encryption_set</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>controlPlane:
  platform:
    azure:
      osDisk:
        diskEncryptionSet:
          subscriptionId:</code></pre></td>
<td style="text-align: left;"><p>Defines the Azure subscription of the disk encryption set where the disk encryption set resides. This secondary disk encryption set is used to encrypt control plane machines.</p>
<p><strong>Value:</strong> String, in the format <code>00000000-0000-0000-0000-000000000000</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>controlPlane:
  platform:
    azure:
      osDisk:
        diskSizeGB:</code></pre></td>
<td style="text-align: left;"><p>The Azure disk size for the VM.</p>
<p><strong>Value:</strong> Integer that represents the size of the disk in GB. The default is <code>1024</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>controlPlane:
  platform:
    azure:
      osDisk:
        diskType:</code></pre></td>
<td style="text-align: left;"><p>Defines the type of disk.</p>
<p><strong>Value:</strong> <code>premium_LRS</code> or <code>standardSSD_LRS</code>. The default is <code>premium_LRS</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>controlPlane:
  platform:
    azure:
      osImage:
        publisher:</code></pre></td>
<td style="text-align: left;"><p>Optional. By default, the installation program downloads and installs the Red Hat Enterprise Linux CoreOS (RHCOS) image that is used to boot control plane machines. You can override the default behavior by using a custom RHCOS image that is available from the Azure Marketplace. The installation program uses this image for control plane machines only. Control plane machines do not contribute to licensing costs when using the default image. But, if you apply an Azure Marketplace image for a control plane machine, usage costs do apply.</p>
<p><strong>Value:</strong> String. The name of the image publisher.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>controlPlane:
  platform:
    azure:
      osImage:
        offer:</code></pre></td>
<td style="text-align: left;"><p>The name of Azure Marketplace offer that is associated with the custom RHCOS image. If you use <code>controlPlane.platform.azure.osImage.publisher</code>, this field is required.</p>
<p><strong>Value:</strong> String. The name of the image offer.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>controlPlane:
  platform:
    azure:
      osImage:
        sku:</code></pre></td>
<td style="text-align: left;"><p>An instance of the Azure Marketplace offer. If you use <code>controlPlane.platform.azure.osImage.publisher</code>, this field is required.</p>
<p><strong>Value:</strong> String. The SKU of the image offer.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>controlPlane:
  platform:
    azure:
      osImage:
        version:</code></pre></td>
<td style="text-align: left;"><p>The version number of the image SKU. If you use <code>controlPlane.platform.azure.osImage.publisher</code>, this field is required.</p>
<p><strong>Value:</strong> String. The version of the image to use.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>controlPlane:
  platform:
    azure:
      ultraSSDCapability:</code></pre></td>
<td style="text-align: left;"><p>Enables the use of Azure ultra disks for persistent storage on control plane machines. This requires that your Azure region and zone have ultra disks available.</p>
<p><strong>Value:</strong> <code>Enabled</code>, <code>Disabled</code>. The default is <code>Disabled</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>controlPlane:
  platform:
    azure:
      vmNetworkingType:</code></pre></td>
<td style="text-align: left;"><p>Enables accelerated networking. Accelerated networking enables single root I/O virtualization (SR-IOV) to a VM, improving its networking performance. If instance type of control plane machines support <code>Accelerated</code> networking, by default, the installation program enables <code>Accelerated</code> networking, otherwise the default networking type is <code>Basic</code>.</p>
<p><strong>Value:</strong> <code>Accelerated</code> or <code>Basic</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>platform:
  azure:
    baseDomainResourceGroupName:</code></pre></td>
<td style="text-align: left;"><p>The name of the resource group that contains the DNS zone for your base domain.</p>
<p><strong>Value:</strong> String, for example <code>production_cluster</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>platform:
  azure:
    resourceGroupName:</code></pre></td>
<td style="text-align: left;"><p>The name of an already existing resource group to install your cluster to. This resource group must be empty and only used for this specific cluster; the cluster components assume ownership of all resources in the resource group. If you limit the service principal scope of the installation program to this resource group, you must ensure all other resources used by the installation program in your environment have the necessary permissions, such as the public DNS zone and virtual network. Destroying the cluster by using the installation program deletes this resource group.</p>
<p><strong>Value:</strong> String, for example <code>existing_resource_group</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>platform:
  azure:
    outboundType:</code></pre></td>
<td style="text-align: left;"><p>The outbound routing strategy used to connect your cluster to the internet. If you are using user-defined routing, you must have pre-existing networking available. The outbound routing must be configured before installing a cluster. The installation program does not configure user-defined routing. If you specify the <code>NatGateway</code> routing strategy, the installation program only creates one NAT gateway. If you specify the <code>NatGateway</code> routing strategy, your account must have the <code>Microsoft.Network/natGateways/read</code> and <code>Microsoft.Network/natGateways/write</code> permissions.</p>
<div class="important">
<div class="title">
&#10;</div>
<p><code>NatGateway</code> is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.</p>
<p>For more information about the support scope of Red Hat Technology Preview features, see <a href="https://access.redhat.com/support/offerings/techpreview/">Technology Preview Features Support Scope</a>.</p>
</div>
<p><strong>Value:</strong> <code>LoadBalancer</code>, <code>UserDefinedRouting</code>, or <code>NatGateway</code>. The default is <code>LoadBalancer</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>platform:
  azure:
    region:</code></pre></td>
<td style="text-align: left;"><p>The name of the Azure region that hosts your cluster.</p>
<p><strong>Value:</strong> Any valid region name, such as <code>centralus</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>platform:
  azure:
    zone:</code></pre></td>
<td style="text-align: left;"><p>List of availability zones to place machines in. For high availability, specify at least two zones.</p>
<p><strong>Value:</strong> List of zones, for example <code>["1", "2", "3"]</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>platform:
  azure:
    customerManagedKey:
      keyVault:
        name:</code></pre></td>
<td style="text-align: left;"><p>Specifies the name of the key vault that contains the encryption key that is used to encrypt Azure storage.</p>
<p><strong>Value:</strong> String.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>platform:
  azure:
    customerManagedKey:
      keyVault:
        keyName:</code></pre></td>
<td style="text-align: left;"><p>Specifies the name of the user-managed encryption key that is used to encrypt Azure storage.</p>
<p><strong>Value:</strong> String.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>platform:
  azure:
    customerManagedKey:
      keyVault:
        resourceGroup:</code></pre></td>
<td style="text-align: left;"><p>Specifies the name of the resource group that contains the key vault and managed identity.</p>
<p><strong>Value:</strong> String.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>platform:
  azure:
    customerManagedKey:
      userAssignedIdentityKey:</code></pre></td>
<td style="text-align: left;"><p>Specifies the name of the user-assigned managed identity that resides in the resource group with the key vault and has access to the user-managed key.</p>
<p><strong>Value:</strong> String.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>platform:
  azure:
    defaultMachinePlatform:
      ultraSSDCapability:</code></pre></td>
<td style="text-align: left;"><p>Enables the use of Azure ultra disks for persistent storage on control plane and compute machines. This requires that your Azure region and zone have ultra disks available.</p>
<p><strong>Value:</strong> <code>Enabled</code>, <code>Disabled</code>. The default is <code>Disabled</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>platform:
  azure:
    networkResourceGroupName:</code></pre></td>
<td style="text-align: left;"><p>The name of the resource group that contains the existing VNet that you want to deploy your cluster to. This name cannot be the same as the <code>platform.azure.baseDomainResourceGroupName</code>.</p>
<p><strong>Value:</strong> String.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>platform:
  azure:
    virtualNetwork:</code></pre></td>
<td style="text-align: left;"><p>The name of the existing VNet that you want to deploy your cluster to.</p>
<p><strong>Value:</strong> String.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>platform:
  azure:
    controlPlaneSubnet:</code></pre></td>
<td style="text-align: left;"><p>The name of the existing subnet in your VNet that you want to deploy your control plane machines to.</p>
<p><strong>Value:</strong> Valid CIDR, for example <code>10.0.0.0/16</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>platform:
  azure:
    computeSubnet:</code></pre></td>
<td style="text-align: left;"><p>The name of the existing subnet in your VNet that you want to deploy your compute machines to.</p>
<p><strong>Value:</strong> Valid CIDR, for example <code>10.0.0.0/16</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>platform:
  azure:
    cloudName:</code></pre></td>
<td style="text-align: left;"><p>The name of the Azure cloud environment that is used to configure the Azure SDK with the appropriate Azure API endpoints. If empty, the default value <code>AzurePublicCloud</code> is used.</p>
<p><strong>Value:</strong> Any valid cloud environment, such as <code>AzurePublicCloud</code> or <code>AzureUSGovernmentCloud</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>platform:
  azure:
    defaultMachinePlatform:
      vmNetworkingType:</code></pre></td>
<td style="text-align: left;"><p>Enables accelerated networking. Accelerated networking enables single root I/O virtualization (SR-IOV) to a VM, improving its networking performance.</p>
<p><strong>Value:</strong> <code>Accelerated</code> or <code>Basic</code>. If instance type of control plane and compute machines support <code>Accelerated</code> networking, by default, the installation program enables <code>Accelerated</code> networking, otherwise the default networking type is <code>Basic</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>operatorPublishingStrategy:
  apiserver:</code></pre></td>
<td style="text-align: left;"><p>Determines whether the load balancers that service the API are public or private. Set this parameter to <code>Internal</code> to prevent the API server from being accessible outside of your VNet. Set this parameter to <code>External</code> to make the API server accessible outside of your VNet. If you set this parameter, you must set the <code>publish</code> parameter to <code>Mixed</code>.</p>
<p><strong>Value:</strong> <code>External</code> or <code>Internal</code>. The default value is <code>External</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>operatorPublishingStrategy:
  ingress:</code></pre></td>
<td style="text-align: left;"><p>Determines whether the DNS resources that the cluster creates for ingress traffic are publicly visible. Set this parameter to <code>Internal</code> to prevent the ingress VIP from being publicly accessible. Set this parameter to <code>External</code> to make the ingress VIP publicly accessible. If you set this parameter, you must set the <code>publish</code> parameter to <code>Mixed</code>.</p>
<p><strong>Value:</strong> <code>External</code> or <code>Internal</code>. The default value is <code>External</code>.</p></td>
</tr>
</tbody>
</table>

> [!NOTE]
> You cannot customize [Azure Availability Zones](https://azure.microsoft.com/en-us/global-infrastructure/availability-zones/) or [Use tags to organize your Azure resources](https://docs.microsoft.com/en-us/azure/azure-resource-manager/resource-group-using-tags) with an Azure cluster.
