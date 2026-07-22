<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

You can use a TLS (Transport Layer Security) security profile to define which TLS ciphers are required by the kubelet when it is acting as an HTTP server. The kubelet uses its HTTP/GRPC server to communicate with the Kubernetes API server, which sends commands to pods, gathers logs, and run exec commands on pods through the kubelet.

A TLS security profile defines the TLS ciphers that the Kubernetes API server must use when connecting with the kubelet to protect communication between the kubelet and the Kubernetes API server.

> [!NOTE]
> By default, when the kubelet acts as a client with the Kubernetes API server, it automatically negotiates the TLS parameters with the API server.

# Understanding TLS security profiles

You can use a TLS (Transport Layer Security) security profile, as described in this section, to define which TLS ciphers are required by various OpenShift Container Platform components.

The OpenShift Container Platform TLS security profiles are based on [Mozilla recommended configurations](https://wiki.mozilla.org/Security/Server_Side_TLS).

You can specify one of the following TLS security profiles for each component:

<table>
<caption>TLS security profiles</caption>
<colgroup>
<col style="width: 33%" />
<col style="width: 66%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Profile</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>Old</code></p></td>
<td style="text-align: left;"><p>This profile is intended for use with legacy clients or libraries. The profile is based on the <a href="https://wiki.mozilla.org/Security/Server_Side_TLS#Old_backward_compatibility">Old backward compatibility</a> recommended configuration.</p>
<p>The <code>Old</code> profile requires a minimum TLS version of 1.0.</p>
<div class="note">
<div class="title">
&#10;</div>
<p>For the Ingress Controller, the minimum TLS version is converted from 1.0 to 1.1.</p>
</div></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>Intermediate</code></p></td>
<td style="text-align: left;"><p>This profile is the default TLS security profile for the Ingress Controller, kubelet, and control plane. The profile is based on the <a href="https://wiki.mozilla.org/Security/Server_Side_TLS#Intermediate_compatibility_.28recommended.29">Intermediate compatibility</a> recommended configuration.</p>
<p>The <code>Intermediate</code> profile requires a minimum TLS version of 1.2.</p>
<div class="note">
<div class="title">
&#10;</div>
<p>This profile is the recommended configuration for the majority of clients.</p>
</div></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>Modern</code></p></td>
<td style="text-align: left;"><p>This profile is intended for use with modern clients that have no need for backwards compatibility. This profile is based on the <a href="https://wiki.mozilla.org/Security/Server_Side_TLS#Modern_compatibility">Modern compatibility</a> recommended configuration.</p>
<p>The <code>Modern</code> profile requires a minimum TLS version of 1.3.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>Custom</code></p></td>
<td style="text-align: left;"><p>This profile allows you to define the TLS version and ciphers to use.</p>
<div class="warning">
<div class="title">
&#10;</div>
<p>Use caution when using a <code>Custom</code> profile, because invalid configurations can cause problems.</p>
</div></td>
</tr>
</tbody>
</table>

> [!NOTE]
> When using one of the predefined profile types, the effective profile configuration is subject to change between releases. For example, given a specification to use the Intermediate profile deployed on release X.Y.Z, an upgrade to release X.Y.Z+1 might cause a new profile configuration to be applied, resulting in a rollout.

# Configuring the TLS security profile for the kubelet

You can configure a TLS security profile for the kubelet when it is acting as an HTTP server by creating a `KubeletConfig` custom resource (CR) to specify a predefined or custom TLS security profile for specific nodes.

If a TLS security profile is not configured, the default TLS security profile, `Intermediate`, is used.

<div class="formalpara">

<div class="title">

Sample `KubeletConfig` CR that configures the `Old` TLS security profile on worker nodes

</div>

``` yaml
apiVersion: machineconfiguration.openshift.io/v1
kind: KubeletConfig
# ...
spec:
  tlsSecurityProfile:
    old: {}
    type: Old
  machineConfigPoolSelector:
    matchLabels:
      pools.operator.machineconfiguration.openshift.io/worker: ""
# ...
```

</div>

You can see the ciphers and the minimum TLS version of the configured TLS security profile in the `kubelet.conf` file on a configured node.

<div>

<div class="title">

Prerequisites

</div>

- You are logged in to OpenShift Container Platform as a user with the `cluster-admin` role.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create a `KubeletConfig` CR to configure the TLS security profile:

    <div class="formalpara">

    <div class="title">

    Sample `KubeletConfig` CR for a `Custom` profile

    </div>

    ``` yaml
    apiVersion: machineconfiguration.openshift.io/v1
    kind: KubeletConfig
    metadata:
      name: set-kubelet-tls-security-profile
    spec:
      tlsSecurityProfile:
        type: Custom
        custom:
          ciphers:
          - ECDHE-ECDSA-CHACHA20-POLY1305
          - ECDHE-RSA-CHACHA20-POLY1305
          - ECDHE-RSA-AES128-GCM-SHA256
          - ECDHE-ECDSA-AES128-GCM-SHA256
          minTLSVersion: VersionTLS11
      machineConfigPoolSelector:
        matchLabels:
          pools.operator.machineconfiguration.openshift.io/worker: ""
    #...
    ```

    </div>

    where:

    `spec.tlsSecurityProfile.type`
    Specifies the TLS security profile type (`Old`, `Intermediate`, or `Custom`). The default is `Intermediate`.

    `spec.tlsSecurityProfile.type.custom`
    Specifies the appropriate field for the selected type:

    - `old: {}`

    - `intermediate: {}`

    - `modern: {}`

    - `custom:`

    `spec.tlsSecurityProfile.type.custom`
    For the `custom` type, specifies a list of TLS ciphers and the minimum accepted TLS version.

    `spec.machineConfigPoolSelector.matchLabels.custom`
    Specifies the machine config pool label for the nodes you want to apply the TLS security profile. This parameter is optional.

2.  Create the `KubeletConfig` object:

    ``` terminal
    $ oc create -f <filename>
    ```

    Depending on the number of worker nodes in the cluster, wait for the configured nodes to be rebooted one by one.

</div>

<div class="formalpara">

<div class="title">

Verification

</div>

To verify that the profile is set, perform the following steps after the nodes are in the `Ready` state:

</div>

1.  Start a debug session for a configured node:

    ``` terminal
    $ oc debug node/<node_name>
    ```

2.  Set `/host` as the root directory within the debug shell:

    ``` terminal
    sh-4.4# chroot /host
    ```

3.  View the `kubelet.conf` file:

    ``` terminal
    sh-4.4# cat /etc/kubernetes/kubelet.conf
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
      "kind": "KubeletConfiguration",
      "apiVersion": "kubelet.config.k8s.io/v1beta1",
    #...
      "tlsCipherSuites": [
        "TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256",
        "TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256",
        "TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384",
        "TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384",
        "TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256",
        "TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256"
      ],
      "tlsMinVersion": "VersionTLS12",
    #...
    ```

    </div>
