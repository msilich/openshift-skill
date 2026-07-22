<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

# The OpenStack Cloud Controller Manager

Beginning with OpenShift Container Platform 4.12, clusters that run on Red Hat OpenStack Platform (RHOSP) were switched from the legacy OpenStack cloud provider to the external OpenStack Cloud Controller Manager (CCM). This change follows the move in Kubernetes from in-tree, legacy cloud providers to external cloud providers that are implemented by using the [Cloud Controller Manager](https://kubernetes.io/docs/concepts/architecture/cloud-controller/).

To preserve user-defined configurations for the legacy cloud provider, existing configurations are mapped to new ones as part of the migration process. It searches for a configuration called `cloud-provider-config` in the `openshift-config` namespace.

> [!NOTE]
> The config map name `cloud-provider-config` is not statically configured. It is derived from the `spec.cloudConfig.name` value in the `infrastructure/cluster` CRD.

Found configurations are synchronized to the `cloud-conf` config map in the `openshift-cloud-controller-manager` namespace.

As part of this synchronization, the OpenStack CCM Operator alters the new config map such that its properties are compatible with the external cloud provider. The file is changed in the following ways:

- The `[Global] secret-name`, `[Global] secret-namespace`, and `[Global] kubeconfig-path` options are removed. They do not apply to the external cloud provider.

- The `[Global] use-clouds`, `[Global] clouds-file`, and `[Global] cloud` options are added.

- The entire `[BlockStorage]` section is removed. External cloud providers no longer perform storage operations. Block storage configuration is managed by the Cinder CSI driver.

Additionally, the CCM Operator enforces a number of default options. Values for these options are always overriden as follows:

``` txt
[Global]
use-clouds = true
clouds-file = /etc/openstack/secret/clouds.yaml
cloud = openstack
...

[LoadBalancer]
enabled = true
```

The `clouds-value` value, `/etc/openstack/secret/clouds.yaml`, is mapped to the `openstack-cloud-credentials` config in the `openshift-cloud-controller-manager` namespace. You can modify the RHOSP cloud in this file as you do any other `clouds.yaml` file.

# The OpenStack Cloud Controller Manager (CCM) config map

An OpenStack CCM config map defines how your cluster interacts with your RHOSP cloud. By default, this configuration is stored under the `cloud.conf` key in the `cloud-conf` config map in the `openshift-cloud-controller-manager` namespace.

> [!IMPORTANT]
> The `cloud-conf` config map is generated from the `cloud-provider-config` config map in the `openshift-config` namespace.
>
> To change the settings that are described by the `cloud-conf` config map, modify the `cloud-provider-config` config map.
>
> As part of this synchronization, the CCM Operator overrides some options. For more information, see "The RHOSP Cloud Controller Manager".

For example:

<div class="formalpara">

<div class="title">

An example `cloud-conf` config map

</div>

``` yaml
apiVersion: v1
data:
  cloud.conf: |
    [Global]
    secret-name = openstack-credentials
    secret-namespace = kube-system
    region = regionOne
    [LoadBalancer]
    enabled = True
kind: ConfigMap
metadata:
  creationTimestamp: "2022-12-20T17:01:08Z"
  name: cloud-conf
  namespace: openshift-cloud-controller-manager
  resourceVersion: "2519"
  uid: cbbeedaf-41ed-41c2-9f37-4885732d3677
```

</div>

- Set global options by using a `clouds.yaml` file rather than modifying the config map.

The following options are present in the config map. Except when indicated otherwise, they are mandatory for clusters that run on RHOSP.

## Load balancer options

CCM supports several load balancer options for deployments that use Octavia.

> [!NOTE]
> Neutron-LBaaS support is deprecated.

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Option</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>enabled</code></p></td>
<td style="text-align: left;"><p>Whether or not to enable the <code>LoadBalancer</code> type of services integration. The default value is <code>true</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>floating-network-id</code></p></td>
<td style="text-align: left;"><p>Optional. The external network used to create floating IP addresses for load balancer virtual IP addresses (VIPs). If there are multiple external networks in the cloud, this option must be set or the user must specify <code>loadbalancer.openstack.org/floating-network-id</code> in the service annotation.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>floating-subnet-id</code></p></td>
<td style="text-align: left;"><p>Optional. The external network subnet used to create floating IP addresses for the load balancer VIP. Can be overridden by the service annotation <code>loadbalancer.openstack.org/floating-subnet-id</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>floating-subnet</code></p></td>
<td style="text-align: left;"><p>Optional. A name pattern (glob or regular expression if starting with <code>~</code>) for the external network subnet used to create floating IP addresses for the load balancer VIP. Can be overridden by the service annotation <code>loadbalancer.openstack.org/floating-subnet</code>. If multiple subnets match the pattern, the first one with available IP addresses is used.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>floating-subnet-tags</code></p></td>
<td style="text-align: left;"><p>Optional. Tags for the external network subnet used to create floating IP addresses for the load balancer VIP. Can be overridden by the service annotation <code>loadbalancer.openstack.org/floating-subnet-tags</code>. If multiple subnets match these tags, the first one with available IP addresses is used.</p>
<p>If the RHOSP network is configured with sharing disabled, for example, with the <code>--no-share</code> flag used during creation, this option is unsupported. Set the network to share to use this option.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>lb-method</code></p></td>
<td style="text-align: left;"><p>The load balancing algorithm used to create the load balancer pool. For the Amphora provider the value can be <code>ROUND_ROBIN</code>, <code>LEAST_CONNECTIONS</code>, or <code>SOURCE_IP</code>. The default value is <code>ROUND_ROBIN</code>.</p>
<p>For the OVN provider, only the <code>SOURCE_IP_PORT</code> algorithm is supported.</p>
<p>For the Amphora provider, if using the <code>LEAST_CONNECTIONS</code> or <code>SOURCE_IP</code> methods, configure the <code>create-monitor</code> option as <code>true</code> in the <code>cloud-provider-config</code> config map on the <code>openshift-config</code> namespace and <code>ETP:Local</code> on the load-balancer type service to allow balancing algorithm enforcement in the client to service endpoint connections.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>lb-provider</code></p></td>
<td style="text-align: left;"><p>Optional. Used to specify the provider of the load balancer, for example, <code>amphora</code> or <code>octavia</code>. Only the Amphora and Octavia providers are supported.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>lb-version</code></p></td>
<td style="text-align: left;"><p>Optional. The load balancer API version. Only <code>"v2"</code> is supported.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>subnet-id</code></p></td>
<td style="text-align: left;"><p>The ID of the Networking service subnet on which load balancer VIPs are created. For dual stack deployments, leave this option unset. The OpenStack cloud provider automatically selects which subnet to use for a load balancer.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>network-id</code></p></td>
<td style="text-align: left;"><p>The ID of the Networking service network on which load balancer VIPs are created. Unnecessary if <code>subnet-id</code> is set. If this property is not set, the network is automatically selected based on the network that cluster nodes use.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>create-monitor</code></p></td>
<td style="text-align: left;"><p>Whether or not to create a health monitor for the service load balancer. A health monitor is required for services that declare <code>externalTrafficPolicy: Local</code>. The default value is <code>false</code>.</p>
<p>This option is unsupported if you use RHOSP earlier than version 17 with the <code>ovn</code> provider.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>monitor-delay</code></p></td>
<td style="text-align: left;"><p>The interval in seconds by which probes are sent to members of the load balancer. The default value is <code>5</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>monitor-max-retries</code></p></td>
<td style="text-align: left;"><p>The number of successful checks that are required to change the operating status of a load balancer member to <code>ONLINE</code>. The valid range is <code>1</code> to <code>10</code>, and the default value is <code>1</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>monitor-timeout</code></p></td>
<td style="text-align: left;"><p>The time in seconds that a monitor waits to connect to the back end before it times out. The default value is <code>3</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>internal-lb</code></p></td>
<td style="text-align: left;"><p>Whether or not to create an internal load balancer without floating IP addresses. The default value is <code>false</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>LoadBalancerClass "ClassName"</code></p></td>
<td style="text-align: left;"><p>This is a config section that comprises a set of options:</p>
<ul>
<li><p><code>floating-network-id</code></p></li>
<li><p><code>floating-subnet-id</code></p></li>
<li><p><code>floating-subnet</code></p></li>
<li><p><code>floating-subnet-tags</code></p></li>
<li><p><code>network-id</code></p></li>
<li><p><code>subnet-id</code></p></li>
</ul>
<p>The behavior of these options is the same as that of the identically named options in the load balancer section of the CCM config file.</p>
<p>You can set the <code>ClassName</code> value by specifying the service annotation <code>loadbalancer.openstack.org/class</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>max-shared-lb</code></p></td>
<td style="text-align: left;"><p>The maximum number of services that can share a load balancer. The default value is <code>2</code>.</p></td>
</tr>
</tbody>
</table>

## Options that the Operator overrides

The CCM Operator overrides the following options, which you might recognize from configuring RHOSP. Do not configure them yourself. They are included in this document for informational purposes only.

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Option</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>auth-url</code></p></td>
<td style="text-align: left;"><p>The RHOSP Identity service URL. For example, <code>http://128.110.154.166/identity</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>os-endpoint-type</code></p></td>
<td style="text-align: left;"><p>The type of endpoint to use from the service catalog.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>username</code></p></td>
<td style="text-align: left;"><p>The Identity service user name.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>password</code></p></td>
<td style="text-align: left;"><p>The Identity service user password.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>domain-id</code></p></td>
<td style="text-align: left;"><p>The Identity service user domain ID.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>domain-name</code></p></td>
<td style="text-align: left;"><p>The Identity service user domain name.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>tenant-id</code></p></td>
<td style="text-align: left;"><p>The Identity service project ID. Leave this option unset if you are using Identity service application credentials.</p>
<p>In version 3 of the Identity API, which changed the identifier <code>tenant</code> to <code>project</code>, the value of <code>tenant-id</code> is automatically mapped to the project construct in the API.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>tenant-name</code></p></td>
<td style="text-align: left;"><p>The Identity service project name.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>tenant-domain-id</code></p></td>
<td style="text-align: left;"><p>The Identity service project domain ID.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>tenant-domain-name</code></p></td>
<td style="text-align: left;"><p>The Identity service project domain name.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>user-domain-id</code></p></td>
<td style="text-align: left;"><p>The Identity service user domain ID.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>user-domain-name</code></p></td>
<td style="text-align: left;"><p>The Identity service user domain name.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>use-clouds</code></p></td>
<td style="text-align: left;"><p>Whether or not to fetch authorization credentials from a <code>clouds.yaml</code> file. Options set in this section are prioritized over values read from the <code>clouds.yaml</code> file.</p>
<p>CCM searches for the file in the following places:</p>
<ol type="1">
<li><p>The value of the <code>clouds-file</code> option.</p></li>
<li><p>A file path stored in the environment variable <code>OS_CLIENT_CONFIG_FILE</code>.</p></li>
<li><p>The directory <code>pkg/openstack</code>.</p></li>
<li><p>The directory <code>~/.config/openstack</code>.</p></li>
<li><p>The directory <code>/etc/openstack</code>.</p></li>
</ol></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>clouds-file</code></p></td>
<td style="text-align: left;"><p>The file path of a <code>clouds.yaml</code> file. It is used if the <code>use-clouds</code> option is set to <code>true</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>cloud</code></p></td>
<td style="text-align: left;"><p>The named cloud in the <code>clouds.yaml</code> file that you want to use. It is used if the <code>use-clouds</code> option is set to <code>true</code>.</p></td>
</tr>
</tbody>
</table>
