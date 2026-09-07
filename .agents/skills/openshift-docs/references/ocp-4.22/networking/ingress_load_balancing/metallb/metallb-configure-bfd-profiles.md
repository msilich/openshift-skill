<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

As a cluster administrator, you can add, modify, and delete Bidirectional Forwarding Detection (BFD) profiles. The MetalLB Operator uses the BFD profile custom resources to identify which BGP sessions use BFD to provide faster path failure detection than BGP alone provides.

# About the BFD profile custom resource

As a cluster administrator, you can specify parameters in the BFD profile CR. The MetalLB Operator uses the BFD profile custom resources to identify which BGP sessions use BFD to provide faster path failure detection than BGP alone provides.

The following table describes parameters for the BFD profile CR:

<table>
<caption>BFD profile custom resource</caption>
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
<td style="text-align: left;"><p>Specifies the name for the BFD profile custom resource.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>metadata.namespace</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Specifies the namespace for the BFD profile custom resource.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>spec.detectMultiplier</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p>Specifies the detection multiplier to determine packet loss. The remote transmission interval is multiplied by this value to determine the connection loss detection timer.</p>
<p>For example, when the local system has the detect multiplier set to <code>3</code> and the remote system has the transmission interval set to <code>300</code>, the local system detects failures only after <code>900</code> ms without receiving packets. The range is <code>2</code> to <code>255</code>. The default value is <code>3</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>spec.echoMode</code></p></td>
<td style="text-align: left;"><p><code>boolean</code></p></td>
<td style="text-align: left;"><p>Specifies the echo transmission mode. If you are not using distributed BFD, echo transmission mode works only when the peer is also FRR. The default value is <code>false</code> and echo transmission mode is disabled.</p>
<p>When echo transmission mode is enabled, consider increasing the transmission interval of control packets to reduce bandwidth usage. For example, consider increasing the transmit interval to <code>2000</code> ms.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>spec.echoInterval</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p>Specifies the minimum transmission interval, less jitter, that this system uses to send and receive echo packets. The range is <code>10</code> to <code>60000</code>. The default value is <code>50</code> ms.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>spec.minimumTtl</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p>Specifies the minimum expected TTL for an incoming control packet. This field applies to multi-hop sessions only.</p>
<p>The purpose of setting a minimum TTL is to make the packet validation requirements more stringent and avoid receiving control packets from other sessions. The default value is <code>254</code> and indicates that the system expects only one hop between this system and the peer.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>spec.passiveMode</code></p></td>
<td style="text-align: left;"><p><code>boolean</code></p></td>
<td style="text-align: left;"><p>Specifies whether a session is marked as active or passive. A passive session does not attempt to start the connection. Instead, a passive session waits for control packets from a peer before it begins to reply.</p>
<p>Marking a session as passive is useful when you have a router that acts as the central node of a star network and you want to avoid sending control packets that you do not need the system to send. The default value is <code>false</code> and marks the session as active.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>spec.receiveInterval</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p>Specifies the minimum interval that this system is capable of receiving control packets. The range is <code>10</code> to <code>60000</code>. The default value is <code>300</code> ms.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>spec.transmitInterval</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p>Specifies the minimum transmission interval, less jitter, that this system uses to send control packets. The range is <code>10</code> to <code>60000</code>. The default value is <code>300</code> ms.</p></td>
</tr>
</tbody>
</table>

# Configuring a BFD profile

To achieve faster path failure detection for BGP sessions, configure a MetalLB BFD profile and associate it with a BGP peer. Establishing these profiles ensures that your network routing remains highly available and responsive by identifying connectivity issues more rapidly than standard protocols.

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

1.  Create a file, such as `bfdprofile.yaml`, with content like the following example:

    ``` yaml
    apiVersion: metallb.io/v1beta1
    kind: BFDProfile
    metadata:
      name: doc-example-bfd-profile-full
      namespace: metallb-system
    spec:
      receiveInterval: 300
      transmitInterval: 300
      detectMultiplier: 3
      echoMode: false
      passiveMode: true
      minimumTtl: 254
    # ...
    ```

2.  Apply the configuration for the BFD profile:

    ``` terminal
    $ oc apply -f bfdprofile.yaml
    ```

</div>

# Additional resources

- [Configuring MetalLB BGP peers](metallb-configure-bgp-peers.md#metallb-configure-bgp-peers)
