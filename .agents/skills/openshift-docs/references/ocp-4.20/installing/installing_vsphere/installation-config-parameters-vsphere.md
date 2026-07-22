<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Before you deploy an OpenShift Container Platform cluster on vSphere, you can configure parameters to customize your cluster and the platform that hosts it. The installation program uses the information in the `install-config.yaml` file to provision required infrastructure and deploy cluster components. When you create the `install-config.yaml` file, you can configure the values for your required parameters through the command line. Edit the `install-config.yaml` file to customize your cluster further before installation begins.

# Available installation configuration parameters for vSphere

To customize your cluster installation, configuration parameters are available to use in the `install-config.yaml` file.

The following tables specify the required, optional, and vSphere-specific installation configuration parameters that you can set as part of the installation process.

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
<p><strong>Value:</strong> String of lowercase letters and hyphens (<code>-</code>), such as <code>dev</code>.</p></td>
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

> [!NOTE]
> On VMware vSphere, dual-stack networking can specify either IPv4 or IPv6 as the primary address family.

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
    apiVIPs:</code></pre></td>
<td style="text-align: left;"><p>Virtual IP (VIP) addresses that you configured for control plane API access.</p>
<div class="note">
<div class="title">
&#10;</div>
<p>This parameter applies only to installer-provisioned infrastructure without an external load balancer configured. You must not specify this parameter in user-provisioned infrastructure.</p>
<p>The <code>apiVIP</code> and <code>ingressVIP</code> parameters must come from the same network segment as the <code>networking.machineNetwork</code> parameter. If the <code>networking.machineNetwork</code> parameter is set to <code>10.0.0.0/16</code> then the API and Ingress VIPs must be in one of the <code>10.0.0.0/16</code> machine networks.</p>
</div>
<p><strong>Value:</strong> Multiple IP addresses</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>platform:
  vsphere:
    diskType:</code></pre></td>
<td style="text-align: left;"><p>Optional: The disk provisioning method. This value defaults to the vSphere default storage policy if not set.</p>
<p><strong>Value:</strong> Valid values are <code>thin</code>, <code>thick</code>, or <code>eagerZeroedThick</code>.</p></td>
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
<td style="text-align: left;"><p>Specifies the path to a vSphere datastore that stores virtual machines files for a failure domain. You must apply the <code>datastore</code> role to the vSphere vCenter datastore location.</p>
<div class="important">
<div class="title">
&#10;</div>
<p>You can specify the path of any datastore that exists in a datastore cluster. By default, Storage vMotion is automatically enabled for a datastore cluster. Red Hat does not support Storage vMotion, so you must disable Storage vMotion to avoid data loss issues for your OpenShift Container Platform cluster.</p>
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
<td style="text-align: left;"><p>Optional: The absolute path of an existing folder where the user creates the virtual machines, for example, <code>/&lt;data_center_name&gt;/vm/&lt;folder_name&gt;/&lt;subfolder_name&gt;</code>. If you do not provide this value, the installation program creates a top-level folder in the data center virtual machine folder that is named with the infrastructure ID. If you are providing the infrastructure for the cluster and you do not want to use the default <code>StorageClass</code> object, named <code>thin</code>, you can omit the <code>folder</code> parameter from the <code>install-config.yaml</code> file.</p>
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
<td style="text-align: left;"><p>Optional: The absolute path of an existing resource pool where the installation program creates the virtual machines, for example, <code>/&lt;data_center_name&gt;/host/&lt;cluster_name&gt;/Resources/&lt;resource_pool_name&gt;/&lt;optional_nested_resource_pool_name&gt;</code>. If you do not specify a value, the installation program installs the resources in the root of the cluster under <code>/&lt;data_center_name&gt;/host/&lt;cluster_name&gt;/Resources</code>.</p>
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
    ingressVIPs:</code></pre></td>
<td style="text-align: left;"><p>Virtual IP (VIP) addresses that you configured for cluster Ingress.</p>
<div class="note">
<div class="title">
&#10;</div>
<p>This parameter applies only to installer-provisioned infrastructure without an external load balancer configured. You must not specify this parameter in user-provisioned infrastructure.</p>
<p>The <code>apiVIP</code> and <code>ingressVIP</code> parameters must come from the same network segment as the <code>networking.machineNetwork</code> parameter. If the <code>networking.machineNetwork</code> parameter is set to <code>10.0.0.0/16</code> then the API and Ingress VIPs must be in one of the <code>10.0.0.0/16</code> machine networks.</p>
</div>
<p><strong>Value:</strong> Multiple IP addresses</p></td>
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
    apiVIP:</code></pre></td>
<td style="text-align: left;"><p>The virtual IP (VIP) address that you configured for control plane API access.</p>
<div class="note">
<div class="title">
&#10;</div>
<p>In OpenShift Container Platform 4.12 and later, the <code>apiVIP</code> configuration setting is deprecated. Instead, use a <code>List</code> format to enter a value in the <code>apiVIPs</code> configuration setting.</p>
</div>
<p><strong>Value:</strong> An IP address, for example <code>128.0.0.1</code>.</p></td>
</tr>
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
    ingressVIP:</code></pre></td>
<td style="text-align: left;"><p>Virtual IP (VIP) addresses that you configured for cluster Ingress.</p>
<div class="note">
<div class="title">
&#10;</div>
<p>In OpenShift Container Platform 4.12 and later, the <code>ingressVIP</code> configuration setting is deprecated. Instead, use a <code>List</code> format to enter a value in the <code>ingressVIPs</code> configuration setting.</p>
</div>
<p><strong>Value:</strong> An IP address, for example <code>128.0.0.1</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>platform:
  vsphere:
    network:</code></pre></td>
<td style="text-align: left;"><p>The network in the vCenter instance that contains the virtual IP addresses and DNS records that you configured.</p>
<p><strong>Value:</strong> String</p></td>
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

## Optional VMware vSphere machine pool configuration parameters

Optional VMware vSphere machine pool configuration parameters are described in the following table:

<table>
<caption>Optional VMware vSphere machine pool parameters</caption>
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
    clusterOSImage:</code></pre></td>
<td style="text-align: left;"><p>The location from which the installation program downloads the Red Hat Enterprise Linux CoreOS (RHCOS) image. Before setting a path value for this parameter, ensure that the default RHCOS boot image in the OpenShift Container Platform release matches the RHCOS image template or virtual machine version; otherwise, cluster installation might fail. As an alternative to this configuration, you can use the <code>topology.template</code> parameter to point to the path in your vCenter environment that includes an RHCOS image in Open Virtual Appliance (OVA) format.</p>
<p><strong>Value:</strong> An HTTP or HTTPS URL, optionally with a SHA-256 checksum. For example, <code>https://mirror.openshift.com/images/rhcos-&lt;version&gt;-vmware.&lt;architecture&gt;.ova</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>platform:
  vsphere:
    osDisk:
      diskSizeGB:</code></pre></td>
<td style="text-align: left;"><p>The size of the disk in gigabytes.</p>
<p><strong>Value:</strong> Integer</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>platform:
  vsphere:
    cpus:</code></pre></td>
<td style="text-align: left;"><p>The total number of virtual processor cores to assign a virtual machine. The value of <code>platform.vsphere.cpus</code> must be a multiple of <code>platform.vsphere.coresPerSocket</code> value.</p>
<p><strong>Value:</strong> Integer</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>platform:
  vsphere:
    coresPerSocket:</code></pre></td>
<td style="text-align: left;"><p>The number of cores per socket in a virtual machine, where <code>platform.vsphere.cpus</code> divided by <code>platform.vsphere.coresPerSocket</code> determines the number of virtual sockets on a virtual machine. Control plane nodes and compute nodes default to <code>4</code> virtual sockets on a virtual machine.</p>
<p><strong>Value:</strong> Integer</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>platform:
  vsphere:
    memoryMB:</code></pre></td>
<td style="text-align: left;"><p>The size of a virtual machine’s memory in megabytes.</p>
<p><strong>Value:</strong> Integer</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>platform:
  vsphere:
    dataDisks:
      name:</code></pre></td>
<td style="text-align: left;"><p>The name of the data disk to add to the virtual machines. The maximum name length is 80 characters.</p>
<div class="important">
<div class="title">
&#10;</div>
<p>Installing OpenShift Container Platform on VMware vSphere using multiple data disks is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.</p>
<p>For more information about the support scope of Red Hat Technology Preview features, see <a href="https://access.redhat.com/support/offerings/techpreview/">Technology Preview Features Support Scope</a>.</p>
</div>
<p><strong>Value:</strong> String</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>platform:
  vsphere:
    dataDisks:
      sizeGiB:</code></pre></td>
<td style="text-align: left;"><p>The size of the data disk to add to the virtual machines. The maximum size is 16384 GiB.</p>
<p><strong>Value:</strong> Integer</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>platform:
  vsphere:
    dataDisks:
      provisioningMode:</code></pre></td>
<td style="text-align: left;"><p>Optional: The data disk provisioning method. This value defaults to the vSphere default storage policy, if not set.</p>
<p><strong>Value:</strong> Valid values are <code>Thin</code>, <code>Thick</code>, or <code>EagerlyZeroed</code>.</p></td>
</tr>
</tbody>
</table>
