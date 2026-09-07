<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

As a cluster administrator, you can configure an external gateway on the default network.

This feature offers the following benefits:

- Granular control over egress traffic on a per-namespace basis

- Flexible configuration of static and dynamic external gateway IP addresses

- Support for both IPv4 and IPv6 address families

# Prerequisites

- Your cluster uses the OVN-Kubernetes network plugin.

- Your infrastructure is configured to route traffic from the secondary external gateway.

# How OpenShift Container Platform determines the external gateway IP address

You configure a secondary external gateway with the `AdminPolicyBasedExternalRoute` custom resource (CR) from the `k8s.ovn.org` API group. The CR supports static and dynamic approaches for specifying an IP address for an external gateway.

Each namespace that an `AdminPolicyBasedExternalRoute` CR targets cannot be selected by any other `AdminPolicyBasedExternalRoute` CR. A namespace cannot have concurrent secondary external gateways.

Changes to policies are isolated in the controller. If a policy fails to apply, changes to other policies do not trigger a retry of other policies. Policies are re-evaluated when updates occur to the policy or to related objects such as target namespaces, pod gateways, or the namespaces that host them from dynamic hops. When re-evaluated, the policy applies any differences from the changes.

Static assignment
You specify an IP address directly.

Dynamic assignment
You specify an IP address indirectly, with namespace and pod selectors, and an optional network attachment definition.

> [!IMPORTANT]
> If the name of a network attachment definition is provided, the external gateway IP address of the network attachment is used.
>
> If the name of a network attachment definition is not provided, the external gateway IP address for the pod itself is used. However, this approach works only if the pod is configured with `hostNetwork` set to `true`.

# AdminPolicyBasedExternalRoute object configuration

You can define an `AdminPolicyBasedExternalRoute` object, which is cluster scoped, with specific properties.

A namespace can be selected by only one `AdminPolicyBasedExternalRoute` CR at a time.

The following tables detail supported fields for objects.

<table>
<caption><code>AdminPolicyBasedExternalRoute</code> object</caption>
<colgroup>
<col style="width: 30%" />
<col style="width: 20%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Field</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>metadata.name</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Specifies the name of the <code>AdminPolicyBasedExternalRoute</code> object.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>spec.from</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Specifies a namespace selector that the routing policies apply to. Only <code>namespaceSelector</code> is supported for external traffic. For example:</p>
<div class="sourceCode" id="cb1"><pre class="sourceCode yaml"><code class="sourceCode yaml"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a><span class="fu">from</span><span class="kw">:</span></span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a><span class="at">  </span><span class="fu">namespaceSelector</span><span class="kw">:</span></span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a><span class="at">    </span><span class="fu">matchLabels</span><span class="kw">:</span></span>
<span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a><span class="at">      </span><span class="fu">kubernetes.io/metadata.name</span><span class="kw">:</span><span class="at"> novxlan-externalgw-ecmp-4059</span></span></code></pre></div>
<p>A namespace can only be targeted by one <code>AdminPolicyBasedExternalRoute</code> CR. If a namespace is selected by more than one <code>AdminPolicyBasedExternalRoute</code> CR, a <code>failed</code> error status occurs on the second and subsequent CRs that target the same namespace. To apply updates, you must change the policy itself or related objects such as target namespaces, pod gateways, or namespaces hosting them from dynamic hops. The policy is then re-evaluated and your changes are applied.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>spec.nextHops</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>Specifies the destinations where the packets are forwarded to. Must be either or both of <code>static</code> and <code>dynamic</code>. You must have at least one next hop defined.</p></td>
</tr>
</tbody>
</table>

| Field | Type | Description |
|----|----|----|
| `static` | `array` | Specifies an array of static IP addresses. |
| `dynamic` | `array` | Specifies an array of pod selectors corresponding to pods configured with a network attachment definition to use as the external gateway target. |

`nextHops` object

| Field | Type | Description |
|----|----|----|
| `ip` | `string` | Specifies either an IPv4 or IPv6 address of the next destination hop. |
| `bfdEnabled` | `boolean` | Optional field. Specifies whether Bi-Directional Forwarding Detection (BFD) is supported by the network. The default value is `false`. |

`nextHops.static` object

| Field | Type | Description |
|----|----|----|
| `podSelector` | `string` | Specifies a set-based label selector to filter the pods in the namespace that match this network configuration. For more information, see "Set-based requirement" in the *Additional resources* section. |
| `namespaceSelector` | `string` | Specifies a `set-based` selector to filter the namespaces that the `podSelector` applies to. You must specify a value for this field. |
| `bfdEnabled` | `boolean` | Optional field. Specifies whether Bi-Directional Forwarding Detection (BFD) is supported by the network. The default value is `false`. |
| `networkAttachmentName` | `string` | Optional field. Specifies the name of a network attachment definition. The name must match the list of logical networks associated with the pod. If this field is not specified, the host network of the pod is used. However, the pod must be configured as a host network pod to use the host network. |

`nextHops.dynamic` object

# Additional resources

- [Set-based requirement (Kubernetes)](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#set-based-requirement)

# Example secondary external gateway configurations

Reference the `AdminPolicyBasedExternalRoute` objects to better understand secondary external gateway configurations.

In the following example, the `AdminPolicyBasedExternalRoute` object configures two static IP addresses as external gateways for pods in namespaces with the `kubernetes.io/metadata.name: novxlan-externalgw-ecmp-4059` label:

``` yaml
apiVersion: k8s.ovn.org/v1
kind: AdminPolicyBasedExternalRoute
metadata:
  name: default-route-policy
spec:
  from:
    namespaceSelector:
      matchLabels:
        kubernetes.io/metadata.name: novxlan-externalgw-ecmp-4059
  nextHops:
    static:
    - ip: "172.18.0.8"
    - ip: "172.18.0.9"
# ...
```

In the following example, the `AdminPolicyBasedExternalRoute` object configures a dynamic external gateway. The IP addresses used for the external gateway are derived from the additional network attachments associated with each of the selected pods.

``` yaml
apiVersion: k8s.ovn.org/v1
kind: AdminPolicyBasedExternalRoute
metadata:
  name: shadow-traffic-policy
spec:
  from:
    namespaceSelector:
      matchLabels:
        externalTraffic: ""
  nextHops:
    dynamic:
    - podSelector:
        matchLabels:
          gatewayPod: ""
      namespaceSelector:
        matchLabels:
          shadowTraffic: ""
      networkAttachmentName: shadow-gateway
    - podSelector:
        matchLabels:
          gigabyteGW: ""
      namespaceSelector:
        matchLabels:
          gatewayNamespace: ""
      networkAttachmentName: gateway
# ...
```

In the following example, the `AdminPolicyBasedExternalRoute` object configures both static and dynamic external gateways:

``` yaml
apiVersion: k8s.ovn.org/v1
kind: AdminPolicyBasedExternalRoute
metadata:
  name: multi-hop-policy
spec:
  from:
    namespaceSelector:
      matchLabels:
        trafficType: "egress"
  nextHops:
    static:
    - ip: "172.18.0.8"
    - ip: "172.18.0.9"
    dynamic:
    - podSelector:
        matchLabels:
          gatewayPod: ""
      namespaceSelector:
        matchLabels:
          egressTraffic: ""
      networkAttachmentName: gigabyte
# ...
```

# Configure a secondary external gateway

You can configure an external gateway on the default network for a namespace in your cluster.

<div>

<div class="title">

Prerequisites

</div>

- You installed the OpenShift CLI (`oc`).

- You are logged in to the cluster with a user with `cluster-admin` privileges.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create a YAML file that contains an `AdminPolicyBasedExternalRoute` object. For more information, see "AdminPolicyBasedExternalRoute object configuration".

2.  To create an admin policy based external route, enter the following command:

    ``` terminal
    $ oc create -f <file>.yaml
    ```

    - `<file>`: Specifies the name of the YAML file that you created in a previous step.

      <div class="formalpara">

      <div class="title">

      Example output

      </div>

      ``` text
      adminpolicybasedexternalroute.k8s.ovn.org/default-route-policy created
      ```

      </div>

3.  To confirm that the admin policy based external route was created, enter the following command:

    ``` terminal
    $ oc describe apbexternalroute <name> | tail -n 6
    ```

    - `<name>`: Specifies the name of the `AdminPolicyBasedExternalRoute` object.

      <div class="formalpara">

      <div class="title">

      Example output

      </div>

      ``` text
      Status:
        Last Transition Time:  2023-04-24T15:09:01Z
        Messages:
        Configured external gateway IPs: 172.18.0.8
        Status:  Success
      Events:  <none>
      ```

      </div>

</div>

# Additional resources

- [Understanding multiple networks](../multiple_networks/understanding-multiple-networks.md#understanding-multiple-networks)
