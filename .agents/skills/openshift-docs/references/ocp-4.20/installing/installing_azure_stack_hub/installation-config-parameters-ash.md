<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Before you deploy an OpenShift Container Platform cluster on Azure Stack Hub, you provide a customized `install-config.yaml` installation configuration file that describes the details for your environment.

# Available installation configuration parameters for Azure Stack Hub

To customize your cluster installation, configuration parameters are available to use in the `install-config.yaml` file.

The following tables specify the required, optional, and Azure Stack Hub-specific installation configuration parameters that you can set as part of the installation process.

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

## Additional Azure Stack Hub configuration parameters

Additional Azure configuration parameters are described in the following table:

<table>
<caption>Additional Azure Stack Hub parameters</caption>
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
<p><strong>Value:</strong> <code>standard_LRS</code> or <code>premium_LRS</code>. The default is <code>premium_LRS</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>compute:
  platform:
    azure:
      type:</code></pre></td>
<td style="text-align: left;"><p>Defines the azure instance type for compute machines.</p>
<p><strong>Value:</strong> String</p></td>
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
<p><strong>Value:</strong> <code>premium_LRS</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>controlPlane:
  platform:
    azure:
      type:</code></pre></td>
<td style="text-align: left;"><p>Defines the azure instance type for control plane machines.</p>
<p><strong>Value:</strong> String</p></td>
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
<p><strong>Value:</strong> <code>standard_LRS</code> or <code>premium_LRS</code>. The default is <code>premium_LRS</code>.</p></td>
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
    armEndpoint:</code></pre></td>
<td style="text-align: left;"><p>The URL of the Azure Resource Manager endpoint that your Azure Stack Hub operator provides.</p>
<p><strong>Value:</strong> String</p></td>
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
    region:</code></pre></td>
<td style="text-align: left;"><p>The name of your Azure Stack Hub local region.</p>
<p><strong>Value:</strong> String</p></td>
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
<td style="text-align: left;"><p>The outbound routing strategy used to connect your cluster to the internet. If you are using user-defined routing, you must have pre-existing networking available. The outbound routing must be configured before installing a cluster. The installation program does not configure user-defined routing.</p>
<p><strong>Value:</strong> <code>LoadBalancer</code> or <code>UserDefinedRouting</code>. The default is <code>LoadBalancer</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>platform:
  azure:
    cloudName:</code></pre></td>
<td style="text-align: left;"><p>The name of the Azure cloud environment that is used to configure the Azure SDK with the appropriate Azure API endpoints.</p>
<p><strong>Value:</strong> <code>AzureStackCloud</code></p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>clusterOSImage:</code></pre></td>
<td style="text-align: left;"><p>The URL of a storage blob in the Azure Stack environment that contains an RHCOS VHD.</p>
<p><strong>Value:</strong> String, for example, https://vhdsa.blob.example.example.com/vhd/rhcos-410.84.202112040202-0-azurestack.x86_64.vhd</p></td>
</tr>
</tbody>
</table>
