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
<td style="text-align: left;"><p>Optional: Specifies the number of bits to include in a 32-bit CIDR mask. To aggregate the routes that the speaker advertises to BGP peers, the mask is applied to the routes for several service IP addresses and the speaker advertises the aggregated route. For example, with an aggregation length of <code>24</code>, the speaker can aggregate several <code>10.0.1.x/32</code> service IP addresses and advertise a single <code>10.0.1.0/24</code> route. If this <code>BGPAdvertisement</code> resource uses <code>spec.serviceSelectors</code> to limit the advertisement to labeled services, you must omit <code>aggregationLength</code> or set it to <code>32</code>; you cannot set another aggregation length on this same resource together with labeled service selection.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>spec.aggregationLengthV6</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p>Optional: Specifies the number of bits to include in a 128-bit CIDR mask. For example, with an aggregation length of <code>124</code>, the speaker can aggregate several <code>fc00:f853:0ccd:e799::x/128</code> service IP addresses and advertise a single <code>fc00:f853:0ccd:e799::0/124</code> route. If this <code>BGPAdvertisement</code> resource uses <code>spec.serviceSelectors</code> to limit the advertisement to labeled services, you must omit <code>aggregationLengthV6</code> or set it to <code>128</code>; you cannot set another aggregation length on this same resource together with labeled service selection.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>spec.communities</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Optional: Specifies one or more BGP communities. Each community is specified as two 16-bit values separated by the colon character. Well-known communities must be specified as 16-bit values:</p>
<ul>
<li><p><code>NO_EXPORT</code>: <code>65535:65281</code></p></li>
<li><p><code>NO_ADVERTISE</code>: <code>65535:65282</code></p></li>
<li><p><code>NO_EXPORT_SUBCONFED</code>: <code>65535:65283</code></p></li>
</ul>
<p>You can also use community objects that are created along with the strings.</p></td>
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
<td style="text-align: left;"><p><code>spec.serviceSelectors</code></p></td>
<td style="text-align: left;"><p><code>array (LabelSelector)</code></p></td>
<td style="text-align: left;"><p>Optional: Kubernetes label selectors that determine which <code>LoadBalancer</code> services receive this advertisement’s BGP policy for routes from the selected pools. If you omit <code>spec.serviceSelectors</code> or specify an empty list, MetalLB applies this advertisement to every <code>LoadBalancer</code> service that draws an IP address from the pools listed in <code>spec.ipAddressPools</code> or matched by <code>spec.ipAddressPoolSelectors</code>. You can use selectors to limit the advertisement to labeled services. On this <code>BGPAdvertisement</code> resource, if you use <code>spec.serviceSelectors</code> to limit the advertisement to labeled services, labeled service selection and custom BGP route aggregation are mutually exclusive: omit <code>spec.aggregationLength</code> and <code>spec.aggregationLengthV6</code> or set them to <code>32</code> (IPv4) and <code>128</code> (IPv6). You cannot set other aggregation lengths on this same resource together with labeled service selection.</p></td>
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

Configure MetalLB to advertise an advanced address pool by using BGP attributes such as BGP communities, route aggregation, and local preference.

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

## Apply different BGP advertisement policies on a shared IP address pool

Use this procedure when many `BGPAdvertisement` resources reference the same `IPAddressPool` and each advertisement must apply different BGP settings to a different group of `LoadBalancer` services. You match services with `spec.serviceSelectors` so each advertisement applies only where its selectors match.

<div>

<div class="title">

Prerequisites

</div>

- You created the `IPAddressPool` that your advertisements reference (for example, `doc-example-bgp-adv`).

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create two `BGPAdvertisement` resources that reference the same `IPAddressPool` but use different `serviceSelectors` and `localPref` values.

    The following example uses two `LoadBalancer` services that share one pool and use the labels `app: web` and `app: api`. It does not include a catch-all `BGPAdvertisement` with no `serviceSelectors`; for that behavior, see the description of `spec.serviceSelectors` in "About the BGPAdvertisement custom resource".

    > [!NOTE]
    > The label keys and values you set under `spec.serviceSelectors` must match the labels on each `LoadBalancer` service that should use this advertisement, and you must use the same keys and values consistently across both advertisement manifests in this procedure (for example, `app: web` and `app: api`). This procedure shows those selectors in the manifests first; add matching labels on your services in the next step. For how `spec.serviceSelectors` interacts with `spec.aggregationLength` on a `BGPAdvertisement` resource, see "About the BGPAdvertisement custom resource".

    1.  Create a file, such as `bgpadvertisement-web.yaml`, with content similar to the following example:

        ``` yaml
        apiVersion: metallb.io/v1beta1
        kind: BGPAdvertisement
        metadata:
          name: bgpadvertisement-web
          namespace: metallb-system
        spec:
          ipAddressPools:
          - doc-example-bgp-adv
          localPref: 200
          serviceSelectors:
          - matchLabels:
              app: web
        ```

        where:

        `doc-example-bgp-adv`
        Specifies the name of the `IPAddressPool` that both advertisements share.

        `localPref`
        Specifies the BGP local preference for routes that this advertisement controls for matching services.

        `serviceSelectors`
        Specifies label selectors so MetalLB applies this advertisement only to `LoadBalancer` services whose labels include `app: web`.

    2.  Apply the configuration by running the following command:

        ``` terminal
        $ oc apply -f bgpadvertisement-web.yaml
        ```

    3.  Create a file, such as `bgpadvertisement-api.yaml`, with content similar to the following example:

        ``` yaml
        apiVersion: metallb.io/v1beta1
        kind: BGPAdvertisement
        metadata:
          name: bgpadvertisement-api
          namespace: metallb-system
        spec:
          ipAddressPools:
          - doc-example-bgp-adv
          localPref: 300
          serviceSelectors:
          - matchLabels:
              app: api
        ```

        where:

        `doc-example-bgp-adv`
        Specifies the same shared `IPAddressPool` name as the first advertisement.

        `localPref`
        Specifies the BGP local preference for routes that this advertisement controls for matching services.

        `serviceSelectors`
        Specifies label selectors so MetalLB applies this advertisement only to `LoadBalancer` services whose labels include `app: api`.

    4.  Apply the configuration by running the following command:

        ``` terminal
        $ oc apply -f bgpadvertisement-api.yaml
        ```

        A `LoadBalancer` service whose labels include `app: web` receives the BGP policy from `bgpadvertisement-web`, including `localPref` `200`. A service whose labels include `app: api` receives the BGP policy from `bgpadvertisement-api`, including `localPref` `300`. Each advertisement applies only to services that satisfy its `serviceSelectors`.

        For the same pattern for Layer 2 advertisements on a shared pool, see **Apply different Layer 2 advertisement policies on a shared IP address pool**.

2.  Add labels to each `LoadBalancer` service that must match the advertisements.

    1.  Label the service that should match `app: web` by running the following command:

        ``` terminal
        $ oc label service <service_web_name> app=web -n <project>
        ```

        where:

        `<service_web_name>`
        Specifies the name of the `LoadBalancer` service.

        `<project>`
        Specifies the namespace that contains the service.

    2.  Label the service that should match `app: api` by running the following command:

        ``` terminal
        $ oc label service <service_api_name> app=api -n <project>
        ```

        where:

        `<service_api_name>`
        Specifies the name of the `LoadBalancer` service.

        `<project>`
        Specifies the namespace that contains the service.

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

To configure how application services are announced over a Layer 2 network, define the properties in the `L2Advertisement` custom resource (CR). Establishing these parameters ensures that MetalLB correctly manages routing for your load-balancer IP addresses within the local network infrastructure.

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
<td style="text-align: left;"><p><code>spec.serviceSelectors</code></p></td>
<td style="text-align: left;"><p><code>array (LabelSelector)</code></p></td>
<td style="text-align: left;"><p>Optional: Kubernetes label selectors that determine which <code>LoadBalancer</code> services receive this advertisement’s Layer 2 settings for addresses from the selected pools. If you omit <code>spec.serviceSelectors</code> or specify an empty list, MetalLB applies this advertisement to every <code>LoadBalancer</code> service that draws an IP address from the pools listed in <code>spec.ipAddressPools</code> or matched by <code>spec.ipAddressPoolSelectors</code>. You can use selectors to limit the advertisement to labeled services. On this <code>L2Advertisement</code> resource, if you use <code>spec.serviceSelectors</code> to limit the advertisement to labeled services, <code>LoadBalancer</code> services that use the <code>metallb.io/allow-shared-ip</code> annotation are not announced on Layer 2 when this advertisement matches those services. Do not combine that annotation with <code>serviceSelectors</code> for Layer 2.</p></td>
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

You can use the `ipAddressPoolSelectors` field in the `L2Advertisement` custom resource definition to associate the `IPAddressPool` with the advertisement based on the label assigned to the pool instead of the pool name. The example configures MetalLB to advertise the pool over Layer 2 by using `ipAddressPoolSelectors`.

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

# Apply different Layer 2 advertisement policies on a shared IP address pool

Use this procedure when many `L2Advertisement` resources reference the same `IPAddressPool` and each advertisement must apply different Layer 2 settings to a different group of `LoadBalancer` services. You match services with `spec.serviceSelectors` so each advertisement applies only where its selectors match.

<div>

<div class="title">

Prerequisites

</div>

- You created the `IPAddressPool` that your advertisements reference (for example, `doc-example-l2-label`).

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create two `L2Advertisement` resources that reference the same `IPAddressPool` but use different `serviceSelectors` so that each advertisement applies Layer 2 settings to a different group of services.

    The following example uses two `LoadBalancer` services that share one pool and use the labels `app: web` and `app: api`. It does not include a catch-all `L2Advertisement` with no `serviceSelectors`; for that behavior, see the description of `spec.serviceSelectors` in "About the L2Advertisement custom resource". Each manifest lists `ipAddressPools` and `serviceSelectors`; add other fields such as `interfaces` or `nodeSelectors` when your deployment requires them.

    > [!NOTE]
    > The label keys and values you set under `spec.serviceSelectors` must match the labels on each `LoadBalancer` service that should use this advertisement, and you must use the same keys and values consistently across both advertisement manifests in this procedure (for example, `app: web` and `app: api`). This procedure shows those selectors in the manifests first; add matching labels on your services in the next step. For how `spec.serviceSelectors` interacts with the `metallb.io/allow-shared-ip` annotation, see "About the L2Advertisement custom resource".

    1.  Create a file, such as `l2advertisement-web.yaml`, with content similar to the following example:

        ``` yaml
        apiVersion: metallb.io/v1beta1
        kind: L2Advertisement
        metadata:
          name: l2advertisement-web
          namespace: metallb-system
        spec:
          ipAddressPools:
          - doc-example-l2-label
          serviceSelectors:
          - matchLabels:
              app: web
        ```

        where:

        `doc-example-l2-label`
        Specifies the name of the `IPAddressPool` that both Layer 2 advertisements share.

        `serviceSelectors`
        Specifies label selectors so MetalLB applies this advertisement only to `LoadBalancer` services whose labels include `app: web`.

    2.  Apply the configuration by running the following command:

        ``` terminal
        $ oc apply -f l2advertisement-web.yaml
        ```

    3.  Create a file, such as `l2advertisement-api.yaml`, with content similar to the following example:

        ``` yaml
        apiVersion: metallb.io/v1beta1
        kind: L2Advertisement
        metadata:
          name: l2advertisement-api
          namespace: metallb-system
        spec:
          ipAddressPools:
          - doc-example-l2-label
          serviceSelectors:
          - matchLabels:
              app: api
        ```

        where:

        `doc-example-l2-label`
        Specifies the same shared `IPAddressPool` name as the first Layer 2 advertisement.

        `serviceSelectors`
        Specifies label selectors so MetalLB applies this advertisement only to `LoadBalancer` services whose labels include `app: api`.

    4.  Apply the configuration by running the following command:

        ``` terminal
        $ oc apply -f l2advertisement-api.yaml
        ```

        A `LoadBalancer` service whose labels include `app: web` receives the Layer 2 settings from `l2advertisement-web`. A service whose labels include `app: api` receives the Layer 2 settings from `l2advertisement-api`. Each advertisement applies only to services that satisfy its `serviceSelectors`.

        For the same pattern for BGP on a shared pool, see **Apply different BGP advertisement policies on a shared IP address pool**.

2.  Add labels to each `LoadBalancer` service that must match the advertisements.

    1.  Label the service that should match `app: web` by running the following command:

        ``` terminal
        $ oc label service <service_web_name> app=web -n <project>
        ```

        where:

        `<service_web_name>`
        Specifies the name of the `LoadBalancer` service.

        `<project>`
        Specifies the namespace that contains the service.

    2.  Label the service that should match `app: api` by running the following command:

        ``` terminal
        $ oc label service <service_api_name> app=api -n <project>
        ```

        where:

        `<service_api_name>`
        Specifies the name of the `LoadBalancer` service.

        `<project>`
        Specifies the namespace that contains the service.

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

# Configure MetalLB with secondary networks

In environments with multiple network interfaces, you might need MetalLB to advertise load-balancer IP addresses on a secondary interface for network traffic segmentation. To route traffic using a secondary interface, you must do the following:

- Enable IP forwarding on the secondary interface so that the interface can forward packets to the pods.

- Enable local gateway mode at the cluster level so that traffic uses the host networking stack.

> [!NOTE]
> From OpenShift Container Platform 4.14, IP forwarding is disabled by default on cluster nodes for improved security. Clusters upgraded from 4.13 might already have IP forwarding enabled because existing node settings are preserved during upgrade.

<div>

<div class="title">

Prerequisites

</div>

- You installed and configured MetalLB.

- You identified the secondary network interface on each node.

- You installed the Kubernetes NMState Operator.

- You have access to the cluster as a user with the `cluster-admin` role.

- You have installed the OpenShift CLI (`oc`).

</div>

<div>

<div class="title">

Procedure

</div>

1.  Enable local gateway mode by patching the Cluster Network Operator to set `routingViaHost` to `true`:

    ``` terminal
    $ oc patch network.operator cluster -p '{"spec":{"defaultNetwork":{"ovnKubernetesConfig":{"gatewayConfig": {"routingViaHost": true} }}}}' --type=merge
    ```

    This setting routes traffic through the host networking stack, which is required for MetalLB to use secondary interfaces.

2.  Create a `NodeNetworkConfigurationPolicy` manifest to enable IP forwarding on the secondary interface, such as `eth1`:

    ``` yaml
    apiVersion: nmstate.io/v1
    kind: NodeNetworkConfigurationPolicy
    metadata:
      name: enable-forwarding-eth1
    spec:
      nodeSelector:
        node-role.kubernetes.io/worker: ""
      desiredState:
        interfaces:
        - name: eth1
          type: ethernet
          state: up
          ipv4:
            enabled: true
            forwarding: true
    ```

    - `interfaces.name` defines the name of the secondary interface on which to enable IP forwarding.

    - `ipv4.forwarding` enables IPv4 forwarding on the interface.

3.  Apply the policy by running the following command:

    ``` terminal
    $ oc apply -f enable-forwarding-eth1.yaml
    ```

</div>

<div>

<div class="title">

Verification

</div>

1.  Verify that the policy was applied by running the following command:

    ``` terminal
    $ oc get nncp
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    NAME                      STATUS      REASON
    enable-forwarding-eth1    Available   SuccessfullyConfigured
    ```

    </div>

2.  Verify that IP forwarding is enabled on a node by running the following command, replacing `<node_name>` with the name of the node:

    ``` terminal
    $ oc debug node/<node_name> -- chroot /host sysctl net.ipv4.conf.eth1.forwarding
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    net.ipv4.conf.eth1.forwarding = 1
    ```

    </div>

</div>

# Additional resources

- [Configuring a community alias](metallb-configure-community-alias.md#metallb-configure-community-alias)

- [Enable IP forwarding on specific interfaces](../../k8s_nmstate/k8s-nmstate-updating-node-network-config.md#nw-nmstate-enable-per-interface-ip-forwarding_k8s-nmstate-updating-node-network-config)
