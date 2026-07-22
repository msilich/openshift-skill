<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

TLS security profiles provide a way for servers to regulate which ciphers a client can use when connecting to the server. This ensures that OpenShift Container Platform components use cryptographic libraries that do not allow known insecure protocols, ciphers, or algorithms.

Cluster administrators can choose which TLS security profile to use for each of the following components:

- the Ingress Controller

- the control plane

  This includes the Kubernetes API server, Kubernetes controller manager, Kubernetes scheduler, OpenShift API server, OpenShift OAuth API server, OpenShift OAuth server, etcd, the Machine Config Operator, and the Machine Config Server.

- the kubelet, when it acts as an HTTP server for the Kubernetes API server

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

# Viewing TLS security profile details

You can view the minimum TLS version and ciphers for the predefined TLS security profiles for each of the following components: Ingress Controller, control plane, and kubelet.

> [!IMPORTANT]
> The effective configuration of minimum TLS version and list of ciphers for a profile might differ between components.

<div>

<div class="title">

Procedure

</div>

- View details for a specific TLS security profile:

  ``` terminal
  $ oc explain <component>.spec.tlsSecurityProfile.<profile>
  ```

  - For `<component>`, specify `ingresscontroller`, `apiserver`, or `kubeletconfig`. For `<profile>`, specify `old`, `intermediate`, or `custom`.

    For example, to check the ciphers included for the `intermediate` profile for the control plane:

    ``` terminal
    $ oc explain apiserver.spec.tlsSecurityProfile.intermediate
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    KIND:     APIServer
    VERSION:  config.openshift.io/v1

    DESCRIPTION:
        intermediate is a TLS security profile based on:
        https://wiki.mozilla.org/Security/Server_Side_TLS#Intermediate_compatibility_.28recommended.29
        and looks like this (yaml):
        ciphers: - TLS_AES_128_GCM_SHA256 - TLS_AES_256_GCM_SHA384 -
        TLS_CHACHA20_POLY1305_SHA256 - ECDHE-ECDSA-AES128-GCM-SHA256 -
        ECDHE-RSA-AES128-GCM-SHA256 - ECDHE-ECDSA-AES256-GCM-SHA384 -
        ECDHE-RSA-AES256-GCM-SHA384 - ECDHE-ECDSA-CHACHA20-POLY1305 -
        ECDHE-RSA-CHACHA20-POLY1305 - DHE-RSA-AES128-GCM-SHA256 -
        DHE-RSA-AES256-GCM-SHA384 minTLSVersion: TLSv1.2
    ```

    </div>

- View all details for the `tlsSecurityProfile` field of a component:

  ``` terminal
  $ oc explain <component>.spec.tlsSecurityProfile
  ```

  - For `<component>`, specify `ingresscontroller`, `apiserver`, or `kubeletconfig`.

    For example, to check all details for the `tlsSecurityProfile` field for the Ingress Controller:

    ``` terminal
    $ oc explain ingresscontroller.spec.tlsSecurityProfile
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    KIND:     IngressController
    VERSION:  operator.openshift.io/v1

    RESOURCE: tlsSecurityProfile <Object>

    DESCRIPTION:
         ...

    FIELDS:
       custom   <>
         custom is a user-defined TLS security profile. Be extremely careful using a
         custom profile as invalid configurations can be catastrophic. An example
         custom profile looks like this:
         ciphers: - ECDHE-ECDSA-CHACHA20-POLY1305 - ECDHE-RSA-CHACHA20-POLY1305 -
         ECDHE-RSA-AES128-GCM-SHA256 - ECDHE-ECDSA-AES128-GCM-SHA256 minTLSVersion:
         TLSv1.1

       intermediate <>
         intermediate is a TLS security profile based on:
         https://wiki.mozilla.org/Security/Server_Side_TLS#Intermediate_compatibility_.28recommended.29
         and looks like this (yaml):
         ...

       modern   <>
         modern is a TLS security profile based on:
         https://wiki.mozilla.org/Security/Server_Side_TLS#Modern_compatibility and
         looks like this (yaml):
         ...
         NOTE: Currently unsupported.

       old  <>
         old is a TLS security profile based on:
         https://wiki.mozilla.org/Security/Server_Side_TLS#Old_backward_compatibility
         and looks like this (yaml):
         ...

       type <string>
         ...
    ```

    </div>

  - Lists ciphers and minimum version for the `intermediate` profile here.

  - Lists ciphers and minimum version for the `modern` profile here.

  - Lists ciphers and minimum version for the `old` profile here.

</div>

# Configuring the TLS security profile for the Ingress Controller

To configure a TLS security profile for an Ingress Controller, edit the `IngressController` custom resource (CR) to specify a predefined or custom TLS security profile. If a TLS security profile is not configured, the default value is based on the TLS security profile set for the API server.

<div class="formalpara">

<div class="title">

Sample `IngressController` CR that configures the `Old` TLS security profile

</div>

``` yaml
apiVersion: operator.openshift.io/v1
kind: IngressController
 ...
spec:
  tlsSecurityProfile:
    old: {}
    type: Old
 ...
```

</div>

The TLS security profile defines the minimum TLS version and the TLS ciphers for TLS connections for Ingress Controllers.

You can see the ciphers and the minimum TLS version of the configured TLS security profile in the `IngressController` custom resource (CR) under `Status.Tls Profile` and the configured TLS security profile under `Spec.Tls Security Profile`. For the `Custom` TLS security profile, the specific ciphers and minimum TLS version are listed under both parameters.

> [!NOTE]
> The HAProxy Ingress Controller image supports TLS `1.3` and the `Modern` profile.
>
> The Ingress Operator also converts the TLS `1.0` of an `Old` or `Custom` profile to `1.1`.

<div>

<div class="title">

Prerequisites

</div>

- You have access to the cluster as a user with the `cluster-admin` role.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Edit the `IngressController` CR in the `openshift-ingress-operator` project to configure the TLS security profile:

    ``` terminal
    $ oc edit IngressController default -n openshift-ingress-operator
    ```

2.  Add the `spec.tlsSecurityProfile` field:

    <div class="formalpara">

    <div class="title">

    Sample `IngressController` CR for a `Custom` profile

    </div>

    ``` yaml
    apiVersion: operator.openshift.io/v1
    kind: IngressController
     ...
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
     ...
    ```

    </div>

    - Specify the TLS security profile type (`Old`, `Intermediate`, or `Custom`). The default is `Intermediate`.

    - Specify the appropriate field for the selected type:

      - `old: {}`

      - `intermediate: {}`

      - `modern: {}`

      - `custom:`

    - For the `custom` type, specify a list of TLS ciphers and minimum accepted TLS version.

3.  Save the file to apply the changes.

</div>

<div>

<div class="title">

Verification

</div>

- Verify that the profile is set in the `IngressController` CR:

  ``` terminal
  $ oc describe IngressController default -n openshift-ingress-operator
  ```

  <div class="formalpara">

  <div class="title">

  Example output

  </div>

  ``` terminal
  Name:         default
  Namespace:    openshift-ingress-operator
  Labels:       <none>
  Annotations:  <none>
  API Version:  operator.openshift.io/v1
  Kind:         IngressController
   ...
  Spec:
   ...
    Tls Security Profile:
      Custom:
        Ciphers:
          ECDHE-ECDSA-CHACHA20-POLY1305
          ECDHE-RSA-CHACHA20-POLY1305
          ECDHE-RSA-AES128-GCM-SHA256
          ECDHE-ECDSA-AES128-GCM-SHA256
        Min TLS Version:  VersionTLS11
      Type:               Custom
   ...
  ```

  </div>

</div>

# Configuring the TLS security profile for the control plane

To configure a TLS security profile for the control plane, edit the `APIServer` custom resource (CR) to specify a predefined or custom TLS security profile. Setting the TLS security profile in the `APIServer` CR propagates the setting to the following control plane components:

- Kubernetes API server

- Kubernetes controller manager

- Kubernetes scheduler

- OpenShift API server

- OpenShift OAuth API server

- OpenShift OAuth server

- etcd

- Machine Config Operator

- Machine Config Server

If a TLS security profile is not configured, the default TLS security profile is `Intermediate`.

> [!NOTE]
> The default TLS security profile for the Ingress Controller is based on the TLS security profile set for the API server.

<div class="formalpara">

<div class="title">

Sample `APIServer` CR that configures the `Old` TLS security profile

</div>

``` yaml
apiVersion: config.openshift.io/v1
kind: APIServer
 ...
spec:
  tlsSecurityProfile:
    old: {}
    type: Old
 ...
```

</div>

The TLS security profile defines the minimum TLS version and the TLS ciphers required to communicate with the control plane components.

You can see the configured TLS security profile in the `APIServer` custom resource (CR) under `Spec.Tls Security Profile`. For the `Custom` TLS security profile, the specific ciphers and minimum TLS version are listed.

<div>

<div class="title">

Prerequisites

</div>

- You have access to the cluster as a user with the `cluster-admin` role.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Edit the default `APIServer` CR to configure the TLS security profile:

    ``` terminal
    $ oc edit APIServer cluster
    ```

2.  Add the `spec.tlsSecurityProfile` field:

    <div class="formalpara">

    <div class="title">

    Sample `APIServer` CR for a `Custom` profile

    </div>

    ``` yaml
    apiVersion: config.openshift.io/v1
    kind: APIServer
    metadata:
      name: cluster
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
    ```

    </div>

    - Specify the TLS security profile type (`Old`, `Intermediate`, or `Custom`). The default is `Intermediate`.

    - Specify the appropriate field for the selected type:

      - `old: {}`

      - `intermediate: {}`

      - `modern: {}`

      - `custom:`

    - For the `custom` type, specify a list of TLS ciphers and minimum accepted TLS version.

3.  Save the file to apply the changes.

</div>

<div>

<div class="title">

Verification

</div>

- Verify that the TLS security profile is set in the `APIServer` CR:

  ``` terminal
  $ oc describe apiserver cluster
  ```

  <div class="formalpara">

  <div class="title">

  Example output

  </div>

  ``` terminal
  Name:         cluster
  Namespace:
   ...
  API Version:  config.openshift.io/v1
  Kind:         APIServer
   ...
  Spec:
    Audit:
      Profile:  Default
    Tls Security Profile:
      Custom:
        Ciphers:
          ECDHE-ECDSA-CHACHA20-POLY1305
          ECDHE-RSA-CHACHA20-POLY1305
          ECDHE-RSA-AES128-GCM-SHA256
          ECDHE-ECDSA-AES128-GCM-SHA256
        Min TLS Version:  VersionTLS11
      Type:               Custom
   ...
  ```

  </div>

- Verify that the TLS security profile is set in the `etcd` CR:

  ``` terminal
  $ oc describe etcd cluster
  ```

  <div class="formalpara">

  <div class="title">

  Example output

  </div>

  ``` terminal
  Name:         cluster
  Namespace:
   ...
  API Version:  operator.openshift.io/v1
  Kind:         Etcd
   ...
  Spec:
    Log Level:         Normal
    Management State:  Managed
    Observed Config:
      Serving Info:
        Cipher Suites:
          TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256
          TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256
          TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384
          TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384
          TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256
          TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256
        Min TLS Version:           VersionTLS12
   ...
  ```

  </div>

- Verify that the TLS security profile is set in the Machine Config Server pod:

  ``` terminal
  $ oc logs machine-config-server-5msdv -n openshift-machine-config-operator
  ```

  <div class="formalpara">

  <div class="title">

  Example output

  </div>

  ``` terminal
  # ...
  I0905 13:48:36.968688       1 start.go:51] Launching server with tls min version: VersionTLS12 & cipher suites [TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256 TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256 TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384 TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384 TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256 TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256]
  # ...
  ```

  </div>

</div>

# Configuring the TLS security profile for the kubelet

You can configure a TLS security profile for the kubelet when it is acting as an HTTP server by creating a `KubeletConfig` custom resource (CR) to specify a predefined or custom TLS security profile for specific nodes.

If a TLS security profile is not configured, the default TLS security profile, `Intermediate`, is used.

The kubelet uses its HTTP/GRPC server to communicate with the Kubernetes API server, which sends commands to pods, gathers logs, and run exec commands on pods through the kubelet.

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
