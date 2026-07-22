<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

You can configure MetalLB so that the IP address is advertised with layer 2 protocols, the BGP protocol, or both.

With layer 2, MetalLB provides a fault-tolerant external IP address. With BGP, MetalLB provides fault-tolerance for the external IP address and load balancing.

MetalLB supports advertising by using Layer 2 and BGP for the same set of IP addresses.

MetalLB provides the flexibility to assign address pools to specific BGP peers, effectively limiting advertising to a subset of nodes on the network. This allows for more complex configurations, such as facilitating the isolation of nodes or the segmentation of the network.

# About the BGPAdvertisement custom resource

To configure how the cluster announces IP addresses to external peers, define the properties of the `BGPAdvertisement` custom resource (CR). Specifying these parameters ensures that MetalLB correctly manages routing advertisements for your application services within the network.

The following table describes the parameters for the `BGPAdvertisements` CR:

<table>
<caption>BGPAdvertisements configuration</caption>
<colgroup>
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 60%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Parameter</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>metadata.name</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Specifies the name for the BGP advertisement.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>metadata.namespace</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Specifies the namespace for the BGP advertisement. Specify the same namespace that the MetalLB Operator uses.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>spec.aggregationLength</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p>Optional: Specifies the number of bits to include in a 32-bit CIDR mask. To aggregate the routes that the speaker advertises to BGP peers, the mask is applied to the routes for several service IP addresses and the speaker advertises the aggregated route. For example, with an aggregation length of <code>24</code>, the speaker can aggregate several <code>10.0.1.x/32</code> service IP addresses and advertise a single <code>10.0.1.0/24</code> route.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>spec.aggregationLengthV6</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p>Optional: Specifies the number of bits to include in a 128-bit CIDR mask. For example, with an aggregation length of <code>124</code>, the speaker can aggregate several <code>fc00:f853:0ccd:e799::x/128</code> service IP addresses and advertise a single <code>fc00:f853:0ccd:e799::0/124</code> route.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>spec.communities</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Optional: Specifies one or more BGP communities. Each community is specified as two 16-bit values separated by the colon character. Well-known communities must be specified as 16-bit values:</p>
<ul>
<li><p><code>NO_EXPORT</code>: <code>65535:65281</code></p></li>
<li><p><code>NO_ADVERTISE</code>: <code>65535:65282</code></p></li>
<li><p><code>NO_EXPORT_SUBCONFED</code>: <code>65535:65283</code></p>
<div class="note">
<div class="title">
&#10;</div>
<p>You can also use community objects that are created along with the strings.</p>
</div></li>
</ul></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>spec.localPref</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p>Optional: Specifies the local preference for this advertisement. This BGP attribute applies to BGP sessions within the Autonomous System.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>spec.ipAddressPools</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Optional: The list of <code>IPAddressPools</code> to advertise with this advertisement, selected by name.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>spec.ipAddressPoolSelectors</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Optional: A selector for the <code>IPAddressPools</code> that gets advertised with this advertisement. This is for associating the <code>IPAddressPool</code> to the advertisement based on the label assigned to the <code>IPAddressPool</code> instead of the name itself. If no <code>IPAddressPool</code> is selected by this or by the list, the advertisement is applied to all the <code>IPAddressPools</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>spec.nodeSelectors</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Optional: By setting the <code>NodeSelectors</code> parameter, you can limit the nodes to announce as next hops for the load balancer IP. When empty, all the nodes are announced as next hops.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>spec.peers</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Optional: Use a list to specify the <code>metadata.name</code> values for each <code>BGPPeer</code> resource that receives advertisements for the MetalLB service IP address. The MetalLB service IP address is assigned from the IP address pool. By default, the MetalLB service IP address is advertised to all configured <code>BGPPeer</code> resources. Set this parameter to limit the advertisement to specific <code>BGPpeer</code> resources.</p></td>
</tr>
</tbody>
</table>

# Configure MetalLB with a BGP advertisement and a basic use case

Configure MetalLB so that the peer BGP routers receive one `203.0.113.200/32` route and one `fc00:f853:ccd:e799::1/128` route for each load-balancer IP address that MetalLB assigns to a service.

Because the `localPref` and `communities` fields are not specified, the routes are advertised with `localPref` set to zero and no BGP communities.

Ensure that you can configure MetalLB so that the peer BGP routers receive one `203.0.113.200/32` route and one `fc00:f853:ccd:e799::1/128` route for each load-balancer IP address that MetalLB assigns to a service. If you do not specify the `localPref` and `communities` parameters, MetalLB advertises the routes with `localPref` set to \`0 and no BGP communities.

## Advertising a basic address pool configuration with BGP

Configure MetalLB to advertise the `IPAddressPool` by using Border Gateway Protocol (BGP).

<div>

<div class="title">

Prerequisites

</div>

- Install the OpenShift CLI (`oc`).

- Log in as a user with `cluster-admin` privileges.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create an IP address pool.

    1.  Create a file, such as `ipaddresspool.yaml`, with content like the following example:

        ``` yaml
        apiVersion: metallb.io/v1beta1
        kind: IPAddressPool
        metadata:
          namespace: metallb-system
          name: doc-example-bgp-basic
        spec:
          addresses:
            - 203.0.113.200/30
            - fc00:f853:ccd:e799::/124
        # ...
        ```

    2.  Apply the configuration for the IP address pool:

        ``` terminal
        $ oc apply -f ipaddresspool.yaml
        ```

2.  Create a BGP advertisement.

    1.  Create a file, such as `bgpadvertisement.yaml`, with content like the following example:

        ``` yaml
        apiVersion: metallb.io/v1beta1
        kind: BGPAdvertisement
        metadata:
          name: bgpadvertisement-basic
          namespace: metallb-system
        spec:
          ipAddressPools:
          - doc-example-bgp-basic
        # ...
        ```

    2.  Apply the configuration:

        ``` terminal
        $ oc apply -f bgpadvertisement.yaml
        ```

</div>

# Configuring MetalLB with a BGP advertisement and an advanced use case

Configure MetalLB so that MetalLB assigns IP addresses to load-balancer services in the ranges between `203.0.113.200` and `203.0.113.203` and between `fc00:f853:ccd:e799::0` and `fc00:f853:ccd:e799::f`.

To explain the two BGP advertisements, consider an instance when MetalLB assigns the IP address of `203.0.113.200` to a service. With that IP address as an example, the speaker advertises the following two routes to BGP peers:

- `203.0.113.200/32`, with `localPref` set to `100` and the community set to the numeric value of the `NO_ADVERTISE` community. This specification indicates to the peer routers that they can use this route but they should not propagate information about this route to BGP peers.

- `203.0.113.200/30`, aggregates the load-balancer IP addresses assigned by MetalLB into a single route. MetalLB advertises the aggregated route to BGP peers with the community attribute set to `8000:800`. BGP peers propagate the `203.0.113.200/30` route to other BGP peers. When traffic is routed to a node with a speaker, the `203.0.113.200/32` route is used to forward the traffic into the cluster and to a pod that is associated with the service.

As you add more services and MetalLB assigns more load-balancer IP addresses from the pool, peer routers receive one local route, `203.0.113.20x/32`, for each service, and the `203.0.113.200/30` aggregate route. Each service that you add generates the `/30` route, but MetalLB deduplicates the routes to one BGP advertisement before communicating with peer routers.

## Advertising an advanced address pool configuration with BGP

Configure MetalLB to advertise an advanced address pool by using the BGP.

<div>

<div class="title">

Prerequisites

</div>

- Install the OpenShift CLI (`oc`).

- Log in as a user with `cluster-admin` privileges.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create an IP address pool.

    1.  Create a file, such as `ipaddresspool.yaml`, with content like the following example:

        ``` yaml
        apiVersion: metallb.io/v1beta1
        kind: IPAddressPool
        metadata:
          namespace: metallb-system
          name: doc-example-bgp-adv
          labels:
            zone: east
        spec:
          addresses:
            - 203.0.113.200/30
            - fc00:f853:ccd:e799::/124
          autoAssign: false
        # ...
        ```

    2.  Apply the configuration for the IP address pool:

        ``` terminal
        $ oc apply -f ipaddresspool.yaml
        ```

2.  Create a BGP advertisement.

    1.  Create a file, such as `bgpadvertisement1.yaml`, with content like the following example:

        ``` yaml
        apiVersion: metallb.io/v1beta1
        kind: BGPAdvertisement
        metadata:
          name: bgpadvertisement-adv-1
          namespace: metallb-system
        spec:
          ipAddressPools:
            - doc-example-bgp-adv
          communities:
            - 65535:65282
          aggregationLength: 32
          localPref: 100
        # ...
        ```

    2.  Apply the configuration:

        ``` terminal
        $ oc apply -f bgpadvertisement1.yaml
        ```

    3.  Create a file, such as `bgpadvertisement2.yaml`, with content like the following example:

        ``` yaml
        apiVersion: metallb.io/v1beta1
        kind: BGPAdvertisement
        metadata:
          name: bgpadvertisement-adv-2
          namespace: metallb-system
        spec:
          ipAddressPools:
            - doc-example-bgp-adv
          communities:
            - 8000:800
          aggregationLength: 30
          aggregationLengthV6: 124
        # ...
        ```

    4.  Apply the configuration:

        ``` terminal
        $ oc apply -f bgpadvertisement2.yaml
        ```

</div>

# Advertising an IP address pool from a subset of nodes

To advertise an IP address from an IP addresses pool, from a specific set of nodes only, use the `.spec.nodeSelector` specification in the `BGPAdvertisement` custom resource (CR). This specification associates a pool of IP addresses with a set of nodes in the cluster. This is useful when you have nodes on different subnets in a cluster and you want to advertise an IP addresses from an address pool from a specific subnet, for example a public-facing subnet only.

<div>

<div class="title">

Prerequisites

</div>

- Install the OpenShift CLI (`oc`).

- Log in as a user with `cluster-admin` privileges.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create an IP address pool by using a CR:

    ``` yaml
    apiVersion: metallb.io/v1beta1
    kind: IPAddressPool
    metadata:
      namespace: metallb-system
      name: pool1
    spec:
      addresses:
        - 4.4.4.100-4.4.4.200
        - 2001:100:4::200-2001:100:4::400
    # ...
    ```

2.  Control which cluster nodes advertise the IP address from `pool1` by setting the `.spec.nodeSelector` value in the `BGPAdvertisement` CR. The following example advertises the IP address from `pool1` only from `NodeA` and `NodeB`.

    ``` yaml
    apiVersion: metallb.io/v1beta1
    kind: BGPAdvertisement
    metadata:
      name: example
    spec:
      ipAddressPools:
      - pool1
      nodeSelector:
      - matchLabels:
          kubernetes.io/hostname: NodeA
      - matchLabels:
          kubernetes.io/hostname: NodeB
    # ...
    ```

</div>

# About the L2Advertisement custom resource

To configure how application services are announced over a Layer 2 network, define the properties in the `L2Advertisement` custom resource (CR). Establishing these parameters ensures that MetalLB correctly manages routing for your load-balancer IP addresses within the local network infrastructure

The following table details parameters for the `l2Advertisements` CR:

<table>
<caption>L2 advertisements configuration</caption>
<colgroup>
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 60%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Parameter</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>metadata.name</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Specifies the name for the L2 advertisement.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>metadata.namespace</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Specifies the namespace for the L2 advertisement. Specify the same namespace that the MetalLB Operator uses.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>spec.ipAddressPools</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Optional: The list of <code>IPAddressPools</code> to advertise with this advertisement, selected by name.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>spec.ipAddressPoolSelectors</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Optional: A selector for the <code>IPAddressPools</code> to advertise with this advertisement. This is for associating the <code>IPAddressPool</code> to the advertisement based on the label assigned to the <code>IPAddressPool</code> instead of the name itself. If no <code>IPAddressPool</code> is selected by this or by the list, the advertisement is applied to all the <code>IPAddressPools</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>spec.nodeSelectors</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Optional: <code>NodeSelectors</code> limits the nodes to announce as next hops for the load balancer IP. If empty, MetalLB announces all nodes as next hops.</p>
<div class="important">
<div class="title">
&#10;</div>
<p>Limiting the nodes to announce as next hops is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.</p>
<p>For more information about the support scope of Red Hat Technology Preview features, see <a href="https://access.redhat.com/support/offerings/techpreview/">Technology Preview Features Support Scope</a>.</p>
</div></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>spec.interfaces</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Optional: The list of <code>interfaces</code> to announce the load balancer IP address.</p></td>
</tr>
</tbody>
</table>

# Configuring MetalLB with an L2 advertisement

You can configure MetalLB so that the `IPAddressPool` is advertised with the L2 protocol.

<div>

<div class="title">

Prerequisites

</div>

- Install the OpenShift CLI (`oc`).

- Log in as a user with `cluster-admin` privileges.

- Install the MetalLB Operator and start MetalLB.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create an IP address pool.

    1.  Create a file, such as `ipaddresspool.yaml`, with content like the following example:

        ``` yaml
        apiVersion: metallb.io/v1beta1
        kind: IPAddressPool
        metadata:
          namespace: metallb-system
          name: doc-example-l2
        spec:
          addresses:
            - <ip_address_range>
          autoAssign: false
        ```

        - `<ip_address_range>` specifies a range of IP addresses that are routable on your network, for example `4.4.4.0/24`.

    2.  Apply the configuration for the IP address pool:

        ``` terminal
        $ oc apply -f ipaddresspool.yaml
        ```

2.  Create an L2 advertisement.

    1.  Create a file, such as `l2advertisement.yaml`, with content like the following example:

        ``` yaml
        apiVersion: metallb.io/v1beta1
        kind: L2Advertisement
        metadata:
          name: l2advertisement
          namespace: metallb-system
        spec:
          ipAddressPools:
           - doc-example-l2
        ```

    2.  Apply the configuration:

        ``` terminal
        $ oc apply -f l2advertisement.yaml
        ```

</div>

<div>

<div class="title">

Verification

</div>

1.  Verify that the IP address pool is created:

    ``` terminal
    $ oc get ipaddresspool -n metallb-system
    ```

    The following is example output:

    ``` terminal
    NAME             AUTO ASSIGN   AVOID BUGGY IPS   ADDRESSES
    doc-example-l2   false         false             ["4.4.4.0/24"]
    ```

2.  Verify that the L2 advertisement is created:

    ``` terminal
    $ oc get l2advertisement -n metallb-system
    ```

    The following is example output:

    ``` terminal
    NAME              IPADDRESSPOOLS     IPADDRESSPOOL SELECTORS   INTERFACES
    l2advertisement   ["doc-example-l2"]
    ```

</div>

# Configuring MetalLB with an L2 advertisement and labels

You can use the `ipAddressPoolSelectors` field in the `BGPAdvertisement` and `L2Advertisement` custom resource definitions to associate the `IPAddressPool` to the advertisement. This association is based on the label assigned to the `IPAddressPool` instead of the name itself.

The example in the procedure shows how to configure MetalLB so that the `IPAddressPool` is advertised with the L2 protocol by configuring the `ipAddressPoolSelectors` field.

<div>

<div class="title">

Prerequisites

</div>

- Install the OpenShift CLI (`oc`).

- Log in as a user with `cluster-admin` privileges.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create an IP address pool.

    1.  Create a file, such as `ipaddresspool.yaml`, with content like the following example:

        ``` yaml
        apiVersion: metallb.io/v1beta1
        kind: IPAddressPool
        metadata:
          namespace: metallb-system
          name: doc-example-l2-label
          labels:
            zone: east
        spec:
          addresses:
            - 172.31.249.87/32
        # ...
        ```

    2.  Apply the configuration for the IP address pool:

        ``` terminal
        $ oc apply -f ipaddresspool.yaml
        ```

2.  Create an L2 advertisement that advertises the IP address by using `ipAddressPoolSelectors`.

    1.  Create a file, such as `l2advertisement.yaml`, with content like the following example:

        ``` yaml
        apiVersion: metallb.io/v1beta1
        kind: L2Advertisement
        metadata:
          name: l2advertisement-label
          namespace: metallb-system
        spec:
          ipAddressPoolSelectors:
            - matchExpressions:
                - key: zone
                  operator: In
                  values:
                    - east
        # ...
        ```

    2.  Apply the configuration:

        ``` terminal
        $ oc apply -f l2advertisement.yaml
        ```

</div>

# Configuring MetalLB with an L2 advertisement for selected interfaces

By default, the IP addresses from IP address pool that has been assigned to the service, is advertised from all the network interfaces. You can use the `interfaces` field in the `L2Advertisement` custom resource definition to restrict those network interfaces that advertise the IP address pool.

The example in the procedure shows how to configure MetalLB so that the IP address pool is advertised only from the network interfaces listed in the `interfaces` parameter of all nodes.

<div>

<div class="title">

Prerequisites

</div>

- You have installed the OpenShift CLI (`oc`).

- You are logged in as a user with `cluster-admin` privileges.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create an IP address pool.

    1.  Create a file, such as `ipaddresspool.yaml`, and enter the configuration details as shown in the following example:

        ``` yaml
        apiVersion: metallb.io/v1beta1
        kind: IPAddressPool
        metadata:
          namespace: metallb-system
          name: doc-example-l2
        spec:
          addresses:
            - 4.4.4.0/24
          autoAssign: false
        # ...
        ```

    2.  Apply the configuration for the IP address pool as shown in the following example:

        ``` terminal
        $ oc apply -f ipaddresspool.yaml
        ```

2.  Create an L2 advertisement with the `interfaces` selector to advertise the IP address.

    1.  Create a YAML file, such as `l2advertisement.yaml`, and enter the configuration details as shown the following example:

        ``` yaml
        apiVersion: metallb.io/v1beta1
        kind: L2Advertisement
        metadata:
          name: l2advertisement
          namespace: metallb-system
        spec:
          ipAddressPools:
           - doc-example-l2
           interfaces:
           - interfaceA
           - interfaceB
        # ...
        ```

    2.  Apply the configuration for the advertisement as shown in the following example:

        ``` terminal
        $ oc apply -f l2advertisement.yaml
        ```

        > [!IMPORTANT]
        > The interface selector does not affect how MetalLB chooses the node to announce a given IP by using L2. The chosen node does not announce the service if the node does not have the selected interface.

</div>

# Configuring MetalLB with secondary networks

From OpenShift Container Platform 4.14 the default network behavior is to not allow forwarding of IP packets between network interfaces. Therefore, when MetalLB is configured on a secondary interface, you need to add a machine configuration to enable IP forwarding for only the required interfaces.

> [!NOTE]
> OpenShift Container Platform clusters upgraded from 4.13 are not affected because a global parameter is set during upgrade to enable global IP forwarding.

To enable IP forwarding for the secondary interface, you have two options:

- Enable IP forwarding for a specific interface.

- Enable IP forwarding for all interfaces.

> [!NOTE]
> Enabling IP forwarding for a specific interface provides more granular control, while enabling it for all interfaces applies a global setting.

<div>

<div class="title">

Procedure

</div>

1.  Patch the Cluster Network Operator, setting the parameter `routingViaHost` to `true` by running the following command:

    ``` terminal
    $ oc patch network.operator cluster -p '{"spec":{"defaultNetwork":{"ovnKubernetesConfig":{"gatewayConfig": {"routingViaHost": true} }}}}' --type=merge
    ```

2.  Enable forwarding for a specific secondary interface, such as `bridge-net`, by creating and applying a `MachineConfig` CR:

    1.  Base64-encode the string that is used to configure network kernel parameters by running the following command on your local machine:

        ``` terminal
        $ echo -e "net.ipv4.conf.bridge-net.forwarding = 1" | base64 -w0
        ```

        <div class="formalpara">

        <div class="title">

        Example output

        </div>

        ``` terminal
        bmV0LmlwdjQuY29uZi5icmlkZ2UtbmV0LmZvcndhcmRpbmcgPSAxCg==
        ```

        </div>

    2.  Create the `MachineConfig` CR to enable IP forwarding for the specified secondary interface named `bridge-net`.

    3.  Save the following YAML in the `enable-ip-forward.yaml` file:

        ``` yaml
        apiVersion: machineconfiguration.openshift.io/v1
        kind: MachineConfig
        metadata:
          labels:
            machineconfiguration.openshift.io/role: <node_role>
          name: 81-enable-global-forwarding
        spec:
          config:
            ignition:
              version: 3.2.0
            storage:
              files:
              - contents:
                  source: data:text/plain;charset=utf-8;base64,bmV0LmlwdjQuY29uZi5icmlkZ2UtbmV0LmZvcndhcmRpbmcgPSAxCg==
                  verification: {}
                filesystem: root
                mode: 420
                path: /etc/sysctl.d/enable-global-forwarding.conf
          osImageURL: ""
        # ...
        ```

        where:

        `<node_role>`
        Node role where you want to enable IP forwarding, for example, `worker`.

        `contents.source`
        Populate with the generated Base64 string.

    4.  Apply the configuration by running the following command:

        ``` terminal
        $ oc apply -f enable-ip-forward.yaml
        ```

3.  Optional: Enable IP forwarding globally by running the following command:

    ``` terminal
    $ oc patch network.operator cluster -p '{"spec":{"defaultNetwork":{"ovnKubernetesConfig":{"gatewayConfig":{"ipForwarding": "Global"}}}}}' --type=merge
    ```

    > [!NOTE]
    > Setting `ipForwarding` to `Global` sets `net.ipv4.conf.default.forwarding = 1`. All interfaces on the node inherit this, resulting in settings like `net.ipv4.conf.tun0.forwarding = 1`. This configuration also skips installing the default drop firewall rules, allowing the node to act as a router that forwards traffic between interfaces.

</div>

<div>

<div class="title">

Verification

</div>

1.  After you apply the machine config, verify the changes by completing the following steps:

    1.  Enter into a debug session on the target node by running the following command. This command instantiates a debug pod called `<node-name>-debug`.

        ``` terminal
        $ oc debug node/<node-name>
        ```

    2.  Set `/host` as the root directory within the debug shell by running the following command. The debug pod mounts root file system of the host in `/host` within the pod. By changing the root directory to `/host`, you can run binaries contained in the executable paths of the host.

        ``` terminal
        $ chroot /host
        ```

    3.  Verify that IP forwarding is enabled by running the following command:

        ``` terminal
        $ cat /etc/sysctl.d/enable-global-forwarding.conf
        ```

        <div class="formalpara">

        <div class="title">

        Example output

        </div>

        ``` terminal
        net.ipv4.conf.bridge-net.forwarding = 1
        ```

        </div>

        The output indicates that IPv4 forwarding is enabled on the `bridge-net` interface.

</div>

# Additional resources

- [Configuring a community alias](metallb-configure-community-alias.md#metallb-configure-community-alias)
