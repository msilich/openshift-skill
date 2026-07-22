<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Before you deploy an OpenShift Container Platform cluster on Red Hat OpenStack Platform (RHOSP), you provide parameters to customize your cluster and the platform that hosts it. When you create the `install-config.yaml` file, you provide values for the required parameters through the command line. You can then modify the `install-config.yaml` file to customize your cluster further.

# Available installation configuration parameters for OpenStack

To customize your cluster installation, configuration parameters are available to use in the `install-config.yaml` file.

The following tables specify the required, optional, and OpenStack-specific installation configuration parameters that you can set as part of the installation process.

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
<p><strong>Value:</strong> String of lowercase letters, hyphens (<code>-</code>), and periods (<code>.</code>), such as <code>dev</code>. The string must be 14 characters or fewer long.</p></td>
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

> [!NOTE]
> Globalnet is not supported with Red Hat OpenShift Data Foundation disaster recovery solutions. For regional disaster recovery scenarios, ensure that you use a non-overlapping range of private IP addresses for the cluster and service networks in each cluster.

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
<td style="text-align: left;"><p>Determines the instruction set architecture of the machines in the pool. Currently, clusters with varied architectures are not supported. All pools must specify the same architecture. Valid values are <code>amd64</code> (the default).</p>
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
<td style="text-align: left;"><p>Determines the instruction set architecture of the machines in the pool. Currently, clusters with varied architectures are not supported. All pools must specify the same architecture. Valid values are <code>amd64</code> (the default).</p>
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

## Additional Red Hat OpenStack Platform (RHOSP) configuration parameters

Additional RHOSP configuration parameters are described in the following table:

<table>
<caption>Additional RHOSP parameters</caption>
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
    openstack:
      rootVolume:
        size:</code></pre></td>
<td style="text-align: left;"><p>For compute machines, the size in gigabytes of the root volume. If you do not set this value, machines use ephemeral storage.</p>
<p><strong>Value:</strong> Integer, for example <code>30</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>compute:
  platform:
    openstack:
      rootVolume:
        types:</code></pre></td>
<td style="text-align: left;"><p>For compute machines, the root volume types.</p>
<p><strong>Value:</strong> A list of strings, for example, {<code>performance-host1</code>, <code>performance-host2</code>, <code>performance-host3</code>}. <sup>[1]</sup></p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>compute:
  platform:
    openstack:
      rootVolume:
        type:</code></pre></td>
<td style="text-align: left;"><p>For compute machines, the root volume’s type. This property is deprecated and is replaced by <code>compute.platform.openstack.rootVolume.types</code>.</p>
<p><strong>Value:</strong> String, for example, <code>performance</code>. <sup>[2]</sup></p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>compute:
  platform:
    openstack:
      rootVolume:
        zones:</code></pre></td>
<td style="text-align: left;"><p>For compute machines, the Cinder availability zone to install root volumes on. If you do not set a value for this parameter, the installation program selects the default availability zone. This parameter is mandatory when <code>compute.platform.openstack.zones</code> is defined.</p>
<p><strong>Value:</strong> A list of strings, for example <code>["zone-1", "zone-2"]</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>controlPlane:
  platform:
    openstack:
      rootVolume:
        size:</code></pre></td>
<td style="text-align: left;"><p>For control plane machines, the size in gigabytes of the root volume. If you do not set this value, machines use ephemeral storage.</p>
<p><strong>Value:</strong> Integer, for example <code>30</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>controlPlane:
  platform:
    openstack:
      rootVolume:
        types:</code></pre></td>
<td style="text-align: left;"><p>For control plane machines, the root volume types.</p>
<p><strong>Value:</strong> A list of strings, for example, {<code>performance-host1</code>, <code>performance-host2</code>, <code>performance-host3</code>}. <sup>[1]</sup></p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>controlPlane:
  platform:
    openstack:
      rootVolume:
        type:</code></pre></td>
<td style="text-align: left;"><p>For control plane machines, the root volume’s type. This property is deprecated and is replaced by <code>compute.platform.openstack.rootVolume.types</code>.</p>
<p><strong>Value:</strong> String, for example, <code>performance</code>. <sup>[2]</sup></p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>controlPlane:
  platform:
    openstack:
      rootVolume:
        zones:</code></pre></td>
<td style="text-align: left;"><p>For control plane machines, the Cinder availability zone to install root volumes on. If you do not set this value, the installation program selects the default availability zone. This parameter is mandatory when <code>controlPlane.platform.openstack.zones</code> is defined.</p>
<p><strong>Value:</strong> A list of strings, for example <code>["zone-1", "zone-2"]</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>platform:
  openstack:
    cloud:</code></pre></td>
<td style="text-align: left;"><p>The name of the RHOSP cloud to use from the list of clouds in the <code>clouds.yaml</code> file.</p>
<p>In the cloud configuration in the <code>clouds.yaml</code> file, if possible, use application credentials rather than a user name and password combination. Using application credentials avoids disruptions from secret propogation that follow user name and password rotation.</p>
<p><strong>Value:</strong> String, for example <code>MyCloud</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>platform:
  openstack:
    externalNetwork:</code></pre></td>
<td style="text-align: left;"><p>The RHOSP external network name to be used for installation.</p>
<p><strong>Value:</strong> String, for example <code>external</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>platform:
  openstack:
    computeFlavor:</code></pre></td>
<td style="text-align: left;"><p>The RHOSP flavor to use for control plane and compute machines.</p>
<p>This property is deprecated. To use a flavor as the default for all machine pools, add it as the value of the <code>type</code> key in the <code>platform.openstack.defaultMachinePlatform</code> property. You can also set a flavor value for each machine pool individually.</p>
<p><strong>Value:</strong> String, for example <code>m1.xlarge</code>.</p></td>
</tr>
</tbody>
</table>

1.  If the machine pool defines `zones`, the count of types can either be a single item or match the number of items in `zones`. For example, the count of types cannot be 2 if there are 3 items in `zones`.

2.  If you have any existing reference to this property, the installation program populates the corresponding value in the `controlPlane.platform.openstack.rootVolume.types` field.

## Optional RHOSP configuration parameters

Optional RHOSP configuration parameters are described in the following table:

<table>
<caption>Optional RHOSP parameters</caption>
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
    openstack:
      additionalNetworkIDs:</code></pre></td>
<td style="text-align: left;"><p>Additional networks that are associated with compute machines. Allowed address pairs are not created for additional networks.</p>
<p><strong>Value:</strong> A list of one or more UUIDs as strings. For example, <code>fa806b2f-ac49-4bce-b9db-124bc64209bf</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>compute:
  platform:
    openstack:
      additionalSecurityGroupIDs:</code></pre></td>
<td style="text-align: left;"><p>Additional security groups that are associated with compute machines.</p>
<p><strong>Value:</strong> A list of one or more UUIDs as strings. For example, <code>7ee219f3-d2e9-48a1-96c2-e7429f1b0da7</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>compute:
  platform:
    openstack:
      zones:</code></pre></td>
<td style="text-align: left;"><p>RHOSP Compute (Nova) availability zones (AZs) to install machines on. If this parameter is not set, the installation program relies on the default settings for Nova that the RHOSP administrator configured.</p>
<p><strong>Value:</strong> A list of strings. For example, <code>["zone-1", "zone-2"]</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>compute:
  platform:
    openstack:
      serverGroupPolicy:</code></pre></td>
<td style="text-align: left;"><p>The server group policy to apply to the group that contains the compute machines in the pool. You cannot change server group policies or affiliations after creation. Supported options include <code>anti-affinity</code>, <code>soft-affinity</code>, and <code>soft-anti-affinity</code>. The default value is <code>soft-anti-affinity</code>.</p>
<p>An <code>affinity</code> policy prevents migrations and therefore affects RHOSP upgrades. The <code>affinity</code> policy is not supported.</p>
<p>If you use a strict <code>anti-affinity</code> policy, an additional RHOSP host is required during instance migration.</p>
<p><strong>Value:</strong> A server group policy to apply to the machine pool. For example, <code>soft-affinity</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>controlPlane:
  platform:
    openstack:
      additionalNetworkIDs:</code></pre></td>
<td style="text-align: left;"><p>Additional networks that are associated with control plane machines. Allowed address pairs are not created for additional networks.</p>
<p>Additional networks that are attached to a control plane machine are also attached to the bootstrap node.</p>
<p><strong>Value:</strong> A list of one or more UUIDs as strings. For example, <code>fa806b2f-ac49-4bce-b9db-124bc64209bf</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>controlPlane:
  platform:
    openstack:
      additionalSecurityGroupIDs:</code></pre></td>
<td style="text-align: left;"><p>Additional security groups that are associated with control plane machines.</p>
<p><strong>Value:</strong> A list of one or more UUIDs as strings. For example, <code>7ee219f3-d2e9-48a1-96c2-e7429f1b0da7</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>controlPlane:
  platform:
    openstack:
      zones:</code></pre></td>
<td style="text-align: left;"><p>RHOSP Compute (Nova) availability zones (AZs) to install machines on. If this parameter is not set, the installation program relies on the default settings for Nova that the RHOSP administrator configured.</p>
<p><strong>Value:</strong> A list of strings. For example, <code>["zone-1", "zone-2"]</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>controlPlane:
  platform:
    openstack:
      serverGroupPolicy:</code></pre></td>
<td style="text-align: left;"><p>Server group policy to apply to the group that contains the control plane machines in the pool. You cannot change server group policies or affiliations after creation. Supported options include <code>anti-affinity</code>, <code>soft-affinity</code>, and <code>soft-anti-affinity</code>. The default value is <code>soft-anti-affinity</code>.</p>
<p>An <code>affinity</code> policy prevents migrations, and therefore affects RHOSP upgrades. The <code>affinity</code> policy is not supported.</p>
<p>If you use a strict <code>anti-affinity</code> policy, an additional RHOSP host is required during instance migration.</p>
<p><strong>Value:</strong> A server group policy to apply to the machine pool. For example, <code>soft-affinity</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>platform:
  openstack:
    apiVIPs:</code></pre></td>
<td style="text-align: left;"><p>IP address on the machine network to assign to the API VIP. If multiple addresses are present, they must consist of exactly one IPv4 and one IPv6 address.</p>
<p><strong>Value:</strong> An array of strings. For example, <code>[ "192.168.1.10", "2001:db8::10" ]</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>platform:
  openstack:
    clusterOSImage:</code></pre></td>
<td style="text-align: left;"><p>The location from which the installation program downloads the RHCOS image.</p>
<p>You must set this parameter to perform an installation in a restricted network.</p>
<p><strong>Value:</strong> An HTTP or HTTPS URL, optionally with an SHA-256 checksum.</p>
<p>For example, <code>http://mirror.example.com/images/rhcos-43.81.201912131630.0-openstack.x86_64.qcow2.gz?sha256=ffebbd68e8a1f2a245ca19522c16c86f67f9ac8e4e0c1f0a812b068b16f7265d</code>. The value can also be the name of an existing Glance image, for example <code>my-rhcos</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>platform:
  openstack:
    clusterOSImageProperties:</code></pre></td>
<td style="text-align: left;"><p>Properties to add to the installation program-uploaded ClusterOSImage in Glance. This property is ignored if <code>platform.openstack.clusterOSImage</code> is set to an existing Glance image.</p>
<p>You can use this property to exceed the default persistent volume (PV) limit for RHOSP of 26 PVs per node. To exceed the limit, set the <code>hw_scsi_model</code> property value to <code>virtio-scsi</code> and the <code>hw_disk_bus</code> value to <code>scsi</code>.</p>
<p>You can also use this property to enable the QEMU guest agent by including the <code>hw_qemu_guest_agent</code> property with a value of <code>yes</code>.</p>
<p><strong>Value:</strong> A set of string properties. For example:</p>
<div class="sourceCode" id="cb12"><pre class="sourceCode yaml"><code class="sourceCode yaml"><span id="cb12-1"><a href="#cb12-1" aria-hidden="true" tabindex="-1"></a><span class="fu">clusterOSImageProperties</span><span class="kw">:</span></span>
<span id="cb12-2"><a href="#cb12-2" aria-hidden="true" tabindex="-1"></a><span class="at">    </span><span class="fu">hw_scsi_model</span><span class="kw">:</span><span class="at"> </span><span class="st">&quot;virtio-scsi&quot;</span></span>
<span id="cb12-3"><a href="#cb12-3" aria-hidden="true" tabindex="-1"></a><span class="at">    </span><span class="fu">hw_disk_bus</span><span class="kw">:</span><span class="at"> </span><span class="st">&quot;scsi&quot;</span></span>
<span id="cb12-4"><a href="#cb12-4" aria-hidden="true" tabindex="-1"></a><span class="at">    </span><span class="fu">hw_qemu_guest_agent</span><span class="kw">:</span><span class="at"> </span><span class="st">&quot;yes&quot;</span></span></code></pre></div></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>platform:
  openstack:
    controlPlanePort:
      fixedIPs:</code></pre></td>
<td style="text-align: left;"><p>Subnets for the machines to use.</p>
<p><strong>Value:</strong> A list of subnet names or UUIDs to use in cluster installation.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>platform:
  openstack:
    controlPlanePort:
      network:</code></pre></td>
<td style="text-align: left;"><p>A network for the machines to use.</p>
<p><strong>Value:</strong> The UUID or name of an RHOSP network to use in cluster installation.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>platform:
  openstack:
    defaultMachinePlatform:</code></pre></td>
<td style="text-align: left;"><p>The default machine pool platform configuration.</p>
<p><strong>Value:</strong></p>
<div class="sourceCode" id="cb16"><pre class="sourceCode json"><code class="sourceCode json"><span id="cb16-1"><a href="#cb16-1" aria-hidden="true" tabindex="-1"></a><span class="fu">{</span></span>
<span id="cb16-2"><a href="#cb16-2" aria-hidden="true" tabindex="-1"></a>   <span class="dt">&quot;type&quot;</span><span class="fu">:</span> <span class="st">&quot;ml.large&quot;</span><span class="fu">,</span></span>
<span id="cb16-3"><a href="#cb16-3" aria-hidden="true" tabindex="-1"></a>   <span class="dt">&quot;rootVolume&quot;</span><span class="fu">:</span> <span class="fu">{</span></span>
<span id="cb16-4"><a href="#cb16-4" aria-hidden="true" tabindex="-1"></a>      <span class="dt">&quot;size&quot;</span><span class="fu">:</span> <span class="dv">30</span><span class="fu">,</span></span>
<span id="cb16-5"><a href="#cb16-5" aria-hidden="true" tabindex="-1"></a>      <span class="dt">&quot;type&quot;</span><span class="fu">:</span> <span class="st">&quot;performance&quot;</span></span>
<span id="cb16-6"><a href="#cb16-6" aria-hidden="true" tabindex="-1"></a>   <span class="fu">}</span></span>
<span id="cb16-7"><a href="#cb16-7" aria-hidden="true" tabindex="-1"></a><span class="fu">}</span></span></code></pre></div></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>platform:
  openstack:
    ingressFloatingIP:</code></pre></td>
<td style="text-align: left;"><p>An existing floating IP address to associate with the Ingress port. To use this property, you must also define the <code>platform.openstack.externalNetwork</code> property.</p>
<p><strong>Value:</strong> An IP address, for example <code>128.0.0.1</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>platform:
  openstack:
    ingressVIPs:</code></pre></td>
<td style="text-align: left;"><p>An IP address or addresses on the machine network to assign to the ingress VIP. If multiple addresses are provided, they must consist of exactly one IPv4 and one IPv6 address.</p>
<p><strong>Value:</strong> An array of strings. For example, <code>[ "192.168.1.11", "2001:db8::11" ]</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>platform:
  openstack:
    apiFloatingIP:</code></pre></td>
<td style="text-align: left;"><p>An existing floating IP address to associate with the API load balancer. To use this property, you must also define the <code>platform.openstack.externalNetwork</code> property.</p>
<p><strong>Value:</strong> An IP address, for example <code>128.0.0.1</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>platform:
  openstack:
    externalDNS:</code></pre></td>
<td style="text-align: left;"><p>IP addresses for external DNS servers that cluster instances use for DNS resolution.</p>
<p><strong>Value:</strong> A list of IP addresses as strings. For example, <code>["8.8.8.8", "192.168.1.12"]</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>platform:
  openstack:
    loadbalancer:</code></pre></td>
<td style="text-align: left;"><p>Whether or not to use the default, internal load balancer. If the value is set to <code>UserManaged</code>, this default load balancer is disabled so that you can deploy a cluster that uses an external, user-managed load balancer. If the parameter is not set, or if the value is <code>OpenShiftManagedDefault</code>, the cluster uses the default load balancer.</p>
<p><strong>Value:</strong> <code>UserManaged</code> or <code>OpenShiftManagedDefault</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>platform:
  openstack:
    machinesSubnet:</code></pre></td>
<td style="text-align: left;"><p>The UUID of a RHOSP subnet that the cluster’s nodes use. Nodes and virtual IP (VIP) ports are created on this subnet.</p>
<p>The first item in <code>networking.machineNetwork</code> must match the value of <code>machinesSubnet</code>.</p>
<p>If you deploy to a custom subnet, you cannot specify an external DNS server to the OpenShift Container Platform installer. Instead, <a href="https://access.redhat.com/documentation/en-us/red_hat_openstack_platform/16.0/html/command_line_interface_reference/subnet">add DNS to the subnet in RHOSP</a>.</p>
<p><strong>Value:</strong> A UUID as a string. For example, <code>fa806b2f-ac49-4bce-b9db-124bc64209bf</code>.</p></td>
</tr>
</tbody>
</table>
