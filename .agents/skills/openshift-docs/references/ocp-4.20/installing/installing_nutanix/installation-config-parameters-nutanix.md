<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Before you deploy an OpenShift Container Platform cluster on Nutanix, you provide parameters to customize your cluster and the platform that hosts it. When you create the `install-config.yaml` file, you provide values for the required parameters through the command line. You can then modify the `install-config.yaml` file to customize your cluster further.

# Available installation configuration parameters for Nutanix

To customize your cluster installation, configuration parameters are available to use in the `install-config.yaml` file.

The following tables specify the required, optional, and Nutanix-specific installation configuration parameters that you can set as part of the installation process.

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

## Additional Nutanix configuration parameters

Additional Nutanix configuration parameters are described in the following table:

<table>
<caption>Additional Nutanix cluster parameters</caption>
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
    nutanix:
      categories:
        key:</code></pre></td>
<td style="text-align: left;"><p>The name of a prism category key to apply to compute VMs. This parameter must be accompanied by the <code>value</code> parameter, and both <code>key</code> and <code>value</code> parameters must exist in Prism Central. For more information on categories, see <a href="https://portal.nutanix.com/page/documents/details?targetId=Prism-Central-Guide-vpc_2022_6:ssp-ssp-categories-manage-pc-c.html">Category management</a>.</p>
<p><strong>Value:</strong> String</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>compute:
  platform:
    nutanix:
      categories:
        value:</code></pre></td>
<td style="text-align: left;"><p>The value of a prism category key-value pair to apply to compute VMs. This parameter must be accompanied by the <code>key</code> parameter, and both <code>key</code> and <code>value</code> parameters must exist in Prism Central.</p>
<p><strong>Value:</strong> String</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>compute:
  platform:
    nutanix:
     failureDomains:</code></pre></td>
<td style="text-align: left;"><p>The failure domains that apply to only compute machines.</p>
<p>Failure domains are specified in <code>platform.nutanix.failureDomains</code>.</p>
<p><strong>Value:</strong> List.</p>
<p>The name of one or more failures domains.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>compute:
  platform:
    nutanix:
      gpus:
        type:</code></pre></td>
<td style="text-align: left;"><p>The type of identifier used to attach a GPU to a compute machine. Valid values are "Name" or "DeviceID".</p>
<p><strong>Value:</strong> String</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>compute:
  platform:
    nutanix:
      gpus:
        name:</code></pre></td>
<td style="text-align: left;"><p>The name of the GPU device to attach to a compute machine. This parameter is required if the GPU <code>type</code> is "Name".</p>
<p><strong>Value:</strong> String</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>compute:
  platform:
    nutanix:
      gpus:
        deviceID:</code></pre></td>
<td style="text-align: left;"><p>The device identifier of the GPU device to attach to a compute machine. This information is available in Prism Central. This parameter is required if the GPU <code>type</code> is "DeviceID".</p>
<p><strong>Value:</strong> Integer</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>compute:
  platform:
    nutanix:
      project:
        type:</code></pre></td>
<td style="text-align: left;"><p>The type of identifier you use to select a project for compute VMs. Projects define logical groups of user roles for managing permissions, networks, and other parameters. For more information on projects, see <a href="https://portal.nutanix.com/page/documents/details?targetId=Prism-Central-Guide-vpc_2022_9:ssp-app-mgmt-project-env-c.html">Projects Overview</a>.</p>
<p><strong>Value:</strong> <code>name</code> or <code>uuid</code></p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>compute:
  platform:
    nutanix:
      project:
        name: or uuid:</code></pre></td>
<td style="text-align: left;"><p>The name or UUID of a project with which compute VMs are associated. This parameter must be accompanied by the <code>type</code> parameter.</p>
<p><strong>Value:</strong> String</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>compute:
  platform:
    nutanix:
      bootType:</code></pre></td>
<td style="text-align: left;"><p>The boot type that the compute machines use. You must use the <code>Legacy</code> boot type in OpenShift Container Platform 4.17. For more information on boot types, see <a href="https://portal.nutanix.com/page/documents/kbs/details?targetId=kA07V000000H3K9SAK">Understanding UEFI, Secure Boot, and TPM in the Virtualized Environment</a>.</p>
<p><strong>Value:</strong> <code>Legacy</code>, <code>SecureBoot</code> or <code>UEFI</code>. The default is <code>Legacy</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>compute:
  platform:
    nutanix:
      dataDisks:
        dataSourceImage:
          name:</code></pre></td>
<td style="text-align: left;"><p>Optional. The name of the data source image for the virtual machine disk in Prism Central.</p>
<p><strong>Value:</strong> String</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>compute:
  platform:
    nutanix:
      dataDisks:
        dataSourceImage:
          referenceName:</code></pre></td>
<td style="text-align: left;"><p>Optional. The reference name of the data source image in the failure domain. If you use this parameter, you must configure a matching <code>dataSourceImage</code> with the same <code>referenceName</code> in each failure domain that the compute nodes occupy. For more information about configuring failure domains, see <em>Configuring failure domains</em> in the <em>Installing a cluster on Nutanix</em> page.</p>
<p><strong>Value:</strong> String</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>compute:
  platform:
    nutanix:
      dataDisks:
        dataSourceImage:
          uuid:</code></pre></td>
<td style="text-align: left;"><p>The UUID of the data source image in Prism Central. This value is required.</p>
<p><strong>Value:</strong> String</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>compute:
  platform:
    nutanix:
      dataDisks:
        deviceProperties:
          adapterType:</code></pre></td>
<td style="text-align: left;"><p>The adapter type of the disk address. If the disk type is "Disk", valid values are "SCSI", "IDE", "PCI", "SATA" or "SPAPR". If the disk type is "CDRom", valid values are "IDE" or "SATA".</p>
<p><strong>Value:</strong> String</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>compute:
  platform:
    nutanix:
      dataDisks:
        deviceProperties:
          deviceIndex:</code></pre></td>
<td style="text-align: left;"><p>The index of the disk address. Valid values are non-negative integers including <code>0</code>. The device index for disks that share the same adapter type should start at 0 and increase consecutively. The default value is <code>0</code>. For each virtual machine, the <code>Disk.SCSI.0</code> and <code>CDRom.IDE.0</code> indices are reserved. If you use the <code>Disk.SCSI</code> or <code>CDRom.IDE</code> disk and adapter types, the <code>deviceIndex</code> should start at <code>1</code>.</p>
<p><strong>Value:</strong> Non-negative integer, including <code>0</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>compute:
  platform:
    nutanix:
      dataDisks:
        deviceProperties:
          deviceType:</code></pre></td>
<td style="text-align: left;"><p>The disk device type. Valid values are "Disk" and "CDRom".</p>
<p><strong>Value:</strong> String</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>compute:
  platform:
    nutanix:
      dataDisks:
        diskSize:</code></pre></td>
<td style="text-align: left;"><p>The size of the disk to attach to the virtual machine. The minimum size is 1Gb.</p>
<p><strong>Value:</strong> Quantity format, such as 100G or 100Gi. For more information on this format, see link:https://pkg.go.dev/k8s.io/apimachinery/pkg/api/resource#Format.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>compute:
  platform:
    nutanix:
      dataDisks:
        storageConfig:
          diskMode:</code></pre></td>
<td style="text-align: left;"><p>The disk mode. Valid values are <code>Standard</code> or <code>Flash</code>, and the default is <code>Standard</code>.</p>
<p><strong>Value:</strong> String</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>compute:
  platform:
    nutanix:
      dataDisks:
        storageConfig:
          storageContainer:
            name:</code></pre></td>
<td style="text-align: left;"><p>Optional. The name of the storage container object used by the virtual machine disk in Prism Central.</p>
<p><strong>Value:</strong> String</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>compute:
  platform:
    nutanix:
      dataDisks:
        storageConfig:
          storageContainer:
            referenceName:</code></pre></td>
<td style="text-align: left;"><p>Optional. The reference name of the storage container in the failure domain. If you use this, you must configure a matching <code>storageContainer</code> with the same <code>referenceName</code> in each failure domain the compute nodes occupy. For more information about configuring failure domains, see <em>Configuring failure domains</em> in the <em>Installing a cluster on Nutanix</em> page.</p>
<p><strong>Value:</strong> String</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>compute:
  platform:
    nutanix:
      dataDisks:
        storageConfig:
          storageContainer:
            uuid:</code></pre></td>
<td style="text-align: left;"><p>The UUID of the storage container in Prism Central.</p>
<p><strong>Value:</strong> String</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>controlPlane:
  platform:
    nutanix:
      categories:
        key:</code></pre></td>
<td style="text-align: left;"><p>The name of a prism category key to apply to control plane VMs. This parameter must be accompanied by the <code>value</code> parameter, and both <code>key</code> and <code>value</code> parameters must exist in Prism Central. For more information on categories, see <a href="https://portal.nutanix.com/page/documents/details?targetId=Prism-Central-Guide-vpc_2022_6:ssp-ssp-categories-manage-pc-c.html">Category management</a>.</p>
<p><strong>Value:</strong> String</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>controlPlane:
  platform:
    nutanix:
      categories:
        value:</code></pre></td>
<td style="text-align: left;"><p>The value of a prism category key-value pair to apply to control plane VMs. This parameter must be accompanied by the <code>key</code> parameter, and both <code>key</code> and <code>value</code> parameters must exist in Prism Central.</p>
<p><strong>Value:</strong> String</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>controlPlane:
  platform:
    nutanix:
     failureDomains:</code></pre></td>
<td style="text-align: left;"><p>The failure domains that apply to only control plane machines.</p>
<p>Failure domains are specified in <code>platform.nutanix.failureDomains</code>.</p>
<p><strong>Value:</strong> List.</p>
<p>The name of one or more failures domains.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>controlPlane:
  platform:
    nutanix:
      project:
        type:</code></pre></td>
<td style="text-align: left;"><p>The type of identifier you use to select a project for control plane VMs. Projects define logical groups of user roles for managing permissions, networks, and other parameters. For more information on projects, see <a href="https://portal.nutanix.com/page/documents/details?targetId=Prism-Central-Guide-vpc_2022_9:ssp-app-mgmt-project-env-c.html">Projects Overview</a>.</p>
<p><strong>Value:</strong> <code>name</code> or <code>uuid</code></p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>controlPlane:
  platform:
    nutanix:
      project:
        name: or uuid:</code></pre></td>
<td style="text-align: left;"><p>The name or UUID of a project with which control plane VMs are associated. This parameter must be accompanied by the <code>type</code> parameter.</p>
<p><strong>Value:</strong> String</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>platform:
  nutanix:
    defaultMachinePlatform:
      categories:
        key:</code></pre></td>
<td style="text-align: left;"><p>The name of a prism category key to apply to all VMs. This parameter must be accompanied by the <code>value</code> parameter, and both <code>key</code> and <code>value</code> parameters must exist in Prism Central. For more information on categories, see <a href="https://portal.nutanix.com/page/documents/details?targetId=Prism-Central-Guide-vpc_2022_6:ssp-ssp-categories-manage-pc-c.html">Category management</a>.</p>
<p><strong>Value:</strong> String</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>platform:
  nutanix:
    defaultMachinePlatform:
      categories:
        value:</code></pre></td>
<td style="text-align: left;"><p>The value of a prism category key-value pair to apply to all VMs. This parameter must be accompanied by the <code>key</code> parameter, and both <code>key</code> and <code>value</code> parameters must exist in Prism Central.</p>
<p><strong>Value:</strong> String</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>platform:
  nutanix:
    defaultMachinePlatform:
      failureDomains:</code></pre></td>
<td style="text-align: left;"><p>The failure domains that apply to both control plane and compute machines.</p>
<p>Failure domains are specified in <code>platform.nutanix.failureDomains</code>.</p>
<p><strong>Value:</strong> List.</p>
<p>The name of one or more failures domains.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>platform:
  nutanix:
    defaultMachinePlatform:
      project:
        type:</code></pre></td>
<td style="text-align: left;"><p>The type of identifier you use to select a project for all VMs. Projects define logical groups of user roles for managing permissions, networks, and other parameters. For more information on projects, see <a href="https://portal.nutanix.com/page/documents/details?targetId=Prism-Central-Guide-vpc_2022_9:ssp-app-mgmt-project-env-c.html">Projects Overview</a>.</p>
<p><strong>Value:</strong> <code>name</code> or <code>uuid</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>platform:
  nutanix:
    defaultMachinePlatform:
      project:
        name: or uuid:</code></pre></td>
<td style="text-align: left;"><p>The name or UUID of a project with which all VMs are associated. This parameter must be accompanied by the <code>type</code> parameter.</p>
<p><strong>Value:</strong> String</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>platform:
  nutanix:
    defaultMachinePlatform:
      bootType:</code></pre></td>
<td style="text-align: left;"><p>The boot type for all machines. You must use the <code>Legacy</code> boot type in OpenShift Container Platform 4.17. For more information on boot types, see <a href="https://portal.nutanix.com/page/documents/kbs/details?targetId=kA07V000000H3K9SAK">Understanding UEFI, Secure Boot, and TPM in the Virtualized Environment</a>.</p>
<p><strong>Value:</strong> <code>Legacy</code>, <code>SecureBoot</code> or <code>UEFI</code>. The default is <code>Legacy</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>platform:
  nutanix:
    apiVIP:</code></pre></td>
<td style="text-align: left;"><p>The virtual IP (VIP) address that you configured for control plane API access.</p>
<p><strong>Value:</strong> IP address</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>platform:
  nutanix:
    failureDomains:
    - name:
      prismElement:
        name:
        uuid:
      subnetUUIDs:
      -</code></pre></td>
<td style="text-align: left;"><p>By default, the installation program installs cluster machines to a single Prism Element instance. A maximum of 32 subnets for each failure domain (Prism Element) in an OpenShift Container Platform cluster is supported. All <code>subnetUUID</code> values must be unique. You can specify additional Prism Element instances for fault tolerance, and then apply them to:</p>
<ul>
<li><p>The cluster’s default machine configuration</p></li>
<li><p>Only control plane or compute machine pools</p></li>
</ul>
<p><strong>Value:</strong> A list of configured failure domains.</p>
<p>For more information on usage, see "Configuring a failure domain" in "Installing a cluster on Nutanix".</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>platform:
  nutanix:
    ingressVIP:</code></pre></td>
<td style="text-align: left;"><p>The virtual IP (VIP) address that you configured for cluster ingress.</p>
<p><strong>Value:</strong> IP address</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>platform:
  nutanix:
    prismCentral:
      endpoint:
        address:</code></pre></td>
<td style="text-align: left;"><p>The Prism Central domain name or IP address.</p>
<p><strong>Value:</strong> String</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>platform:
  nutanix:
    prismCentral:
      endpoint:
        port:</code></pre></td>
<td style="text-align: left;"><p>The port that is used to log into Prism Central.</p>
<p><strong>Value:</strong> String</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>platform:
  nutanix:
    prismCentral:
      password:</code></pre></td>
<td style="text-align: left;"><p>The password for the Prism Central user name.</p>
<p><strong>Value:</strong> String</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>platform:
  nutanix:
    preloadedOSImageName:</code></pre></td>
<td style="text-align: left;"><p>Instead of creating and uploading a RHCOS image object for each OpenShift Container Platform cluster, this parameter uses the named, preloaded RHCOS image object from the Prism Elements to which the OpenShift Container Platform cluster is deployed.</p>
<p><strong>Value:</strong> String</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>platform:
  nutanix:
    prismCentral:
      username:</code></pre></td>
<td style="text-align: left;"><p>The user name that is used to log into Prism Central.</p>
<p><strong>Value:</strong> String</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>platform:
  nutanix:
    prismElements:
      endpoint:
        address:</code></pre></td>
<td style="text-align: left;"><p>The Prism Element domain name or IP address. [<sup>1</sup>]</p>
<p><strong>Value:</strong> String</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>platform:
  nutanix:
    prismElements:
      endpoint:
        port:</code></pre></td>
<td style="text-align: left;"><p>The port that is used to log into Prism Element.</p>
<p><strong>Value:</strong> String</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>platform:
  nutanix:
    prismElements:
      uuid:</code></pre></td>
<td style="text-align: left;"><p>The universally unique identifier (UUID) for Prism Element.</p>
<p><strong>Value:</strong> String</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>platform:
  nutanix:
    subnetUUIDs:</code></pre></td>
<td style="text-align: left;"><p>The UUID of the Prism Element network that contains the virtual IP addresses and DNS records that you configured. [<sup>2</sup>]</p>
<p><strong>Value:</strong> String</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>platform:
  nutanix:
    clusterOSImage:</code></pre></td>
<td style="text-align: left;"><p>Optional: By default, the installation program downloads and installs the Red Hat Enterprise Linux CoreOS (RHCOS) image. If Prism Central does not have internet access, you can override the default behavior by hosting the RHCOS image on any HTTP server and pointing the installation program to the image.</p>
<p><strong>Value:</strong> An HTTP or HTTPS URL, optionally with a SHA-256 checksum. For example, http://example.com/images/rhcos-47.83.202103221318-0-nutanix.x86_64.qcow2</p></td>
</tr>
</tbody>
</table>

1.  The `prismElements` section holds a list of Prism Elements (clusters). A Prism Element encompasses all of the Nutanix resources, for example virtual machines and subnets, that are used to host the OpenShift Container Platform cluster.

2.  A maximum of 32 subnets for each Prism Element in an OpenShift Container Platform cluster is supported. All `subnetUUID` values must be unique.
