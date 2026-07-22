<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

The Ingress Node Firewall Operator provides a stateless, eBPF-based firewall for managing node-level ingress traffic in OpenShift Container Platform.

# Ingress Node Firewall Operator

The Ingress Node Firewall Operator provides ingress firewall rules at a node level that you can specify and manage in the firewall configurations.

To deploy the daemon set created by the Operator, you create an `IngressNodeFirewallConfig` custom resource (CR). The Operator applies the `IngressNodeFirewallConfig` CR to create ingress node firewall daemon set `daemon`, which run on all nodes that match the `nodeSelector`.

You configure `rules` of the `IngressNodeFirewall` CR and apply them to clusters using the `nodeSelector` and setting values to "true".

> [!IMPORTANT]
> The Ingress Node Firewall Operator supports only stateless firewall rules.
>
> Network interface controllers (NICs) that do not support native XDP drivers will run at a lower performance.
>
> For OpenShift Container Platform 4.14 or later, you must run Ingress Node Firewall Operator on RHEL 9.0 or later.

# Installing the Ingress Node Firewall Operator

As a cluster administrator, you can install the Ingress Node Firewall Operator to enable node-level ingress firewalling by using the OpenShift Container Platform CLI.

<div>

<div class="title">

Prerequisites

</div>

- You have installed the OpenShift CLI (`oc`).

- You have an account with administrator privileges.

</div>

<div>

<div class="title">

Procedure

</div>

1.  To create the `openshift-ingress-node-firewall` namespace, enter the following command:

    ``` terminal
    $ cat << EOF| oc create -f -
    apiVersion: v1
    kind: Namespace
    metadata:
      labels:
        pod-security.kubernetes.io/enforce: privileged
        pod-security.kubernetes.io/enforce-version: v1.24
      name: openshift-ingress-node-firewall
    EOF
    ```

2.  To create an `OperatorGroup` CR, enter the following command:

    ``` terminal
    $ cat << EOF| oc create -f -
    apiVersion: operators.coreos.com/v1
    kind: OperatorGroup
    metadata:
      name: ingress-node-firewall-operators
      namespace: openshift-ingress-node-firewall
    EOF
    ```

3.  Subscribe to the Ingress Node Firewall Operator.

    - To create a `Subscription` CR for the Ingress Node Firewall Operator, enter the following command:

      ``` terminal
      $ cat << EOF| oc create -f -
      apiVersion: operators.coreos.com/v1alpha1
      kind: Subscription
      metadata:
        name: ingress-node-firewall-sub
        namespace: openshift-ingress-node-firewall
      spec:
        name: ingress-node-firewall
        channel: stable
        source: redhat-operators
        sourceNamespace: openshift-marketplace
      EOF
      ```

4.  To verify that the Operator is installed, enter the following command:

    ``` terminal
    $ oc get ip -n openshift-ingress-node-firewall
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    NAME            CSV                                         APPROVAL    APPROVED
    install-5cvnz   ingress-node-firewall.4.17.0-202211122336   Automatic   true
    ```

    </div>

5.  To verify the version of the Operator, enter the following command:

    ``` terminal
    $ oc get csv -n openshift-ingress-node-firewall
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    NAME                                        DISPLAY                          VERSION               REPLACES                                    PHASE
    ingress-node-firewall.4.17.0-202211122336   Ingress Node Firewall Operator   4.17.0-202211122336   ingress-node-firewall.4.17.0-202211102047   Succeeded
    ```

    </div>

</div>

# Installing the Ingress Node Firewall Operator using the web console

As a cluster administrator, you can install the Ingress Node Firewall Operator to enable node-level ingress firewalling by using the web console.

<div>

<div class="title">

Prerequisites

</div>

- You have installed the OpenShift CLI (`oc`).

- You have an account with administrator privileges.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Install the Ingress Node Firewall Operator:

    1.  In the OpenShift Container Platform web console, click **Ecosystem** → **Software Catalog**.

    2.  Select **Ingress Node Firewall Operator** from the list of available Operators, and then click **Install**.

    3.  On the **Install Operator** page, under **Installed Namespace**, select **Operator recommended Namespace**.

    4.  Click **Install**.

2.  Verify that the Ingress Node Firewall Operator is installed successfully:

    1.  Navigate to the **Ecosystem** → **Installed Operators** page.

    2.  Ensure that **Ingress Node Firewall Operator** is listed in the **openshift-ingress-node-firewall** project with a **Status** of **InstallSucceeded**.

        > [!NOTE]
        > During installation an Operator might display a **Failed** status. If the installation later succeeds with an **InstallSucceeded** message, you can ignore the **Failed** message.

        If the Operator does not have a **Status** of **InstallSucceeded**, troubleshoot using the following steps:

        - Inspect the **Operator Subscriptions** and **Install Plans** tabs for any failures or errors under **Status**.

        - Navigate to the **Workloads** → **Pods** page and check the logs for pods in the `openshift-ingress-node-firewall` project.

        - Check the namespace of the YAML file. If the annotation is missing, you can add the annotation `workload.openshift.io/allowed=management` to the Operator namespace with the following command:

          ``` terminal
          $ oc annotate ns/openshift-ingress-node-firewall workload.openshift.io/allowed=management
          ```

          > [!NOTE]
          > For single-node OpenShift clusters, the `openshift-ingress-node-firewall` namespace requires the `workload.openshift.io/allowed=management` annotation.

</div>

# Deploying Ingress Node Firewall Operator

To deploy the Ingress Node Firewall Operator, create a `IngressNodeFirewallConfig` custom resource that will deploy the Operator’s daemon set. You can deploy one or multiple `IngressNodeFirewall` CRDs to nodes by applying firewall rules.

<div>

<div class="title">

Prerequisite

</div>

- The Ingress Node Firewall Operator is installed.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create the `IngressNodeFirewallConfig` inside the `openshift-ingress-node-firewall` namespace named `ingressnodefirewallconfig`.

2.  Run the following command to deploy Ingress Node Firewall Operator rules:

    ``` terminal
    $ oc apply -f rule.yaml
    ```

</div>

# Ingress Node Firewall configuration object

Review configuration fields so you can define how the Operator deploys the firewall.

The fields for the Ingress Node Firewall configuration object are described in the following table:

<table>
<caption>Ingress Node Firewall Configuration object</caption>
<colgroup>
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 60%" />
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
<td style="text-align: left;"><p>The name of the CR object. The name of the firewall rules object must be <code>ingressnodefirewallconfig</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>metadata.namespace</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Namespace for the Ingress Firewall Operator CR object. The <code>IngressNodeFirewallConfig</code> CR must be created inside the <code>openshift-ingress-node-firewall</code> namespace.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>spec.nodeSelector</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>A node selection constraint used to target nodes through specified node labels. For example:</p>
<div class="sourceCode" id="cb1"><pre class="sourceCode yaml"><code class="sourceCode yaml"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a><span class="fu">apiVersion</span><span class="kw">:</span><span class="at"> ingressnodefirewall.openshift.io/v1alpha1</span></span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a><span class="fu">kind</span><span class="kw">:</span><span class="at"> IngressNodeFirewallConfig</span></span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a><span class="fu">metadata</span><span class="kw">:</span></span>
<span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a><span class="at">  </span><span class="fu">name</span><span class="kw">:</span><span class="at"> ingressnodefirewallconfig</span></span>
<span id="cb1-5"><a href="#cb1-5" aria-hidden="true" tabindex="-1"></a><span class="at">  </span><span class="fu">namespace</span><span class="kw">:</span><span class="at"> openshift-ingress-node-firewall</span></span>
<span id="cb1-6"><a href="#cb1-6" aria-hidden="true" tabindex="-1"></a><span class="fu">spec</span><span class="kw">:</span></span>
<span id="cb1-7"><a href="#cb1-7" aria-hidden="true" tabindex="-1"></a><span class="at">  </span><span class="fu">nodeSelector</span><span class="kw">:</span></span>
<span id="cb1-8"><a href="#cb1-8" aria-hidden="true" tabindex="-1"></a><span class="at">    </span><span class="fu">node-role.kubernetes.io/worker</span><span class="kw">:</span><span class="at"> </span><span class="st">&quot;&quot;</span></span></code></pre></div>
<div class="note">
<div class="title">
&#10;</div>
<p>One label used in <code>nodeSelector</code> must match a label on the nodes in order for the daemon set to start. For example, if the node labels <code>node-role.kubernetes.io/worker</code> and <code>node-type.kubernetes.io/vm</code> are applied to a node, then at least one label must be set using <code>nodeSelector</code> for the daemon set to start.</p>
</div></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>spec.ebpfProgramManagerMode</code></p></td>
<td style="text-align: left;"><p><code>boolean</code></p></td>
<td style="text-align: left;"><p>Specifies if the Node Ingress Firewall Operator uses the eBPF Manager Operator or not to manage eBPF programs. This capability is a Technology Preview feature.</p>
<p>For more information about the support scope of Red Hat Technology Preview features, see <a href="https://access.redhat.com/support/offerings/techpreview/">Technology Preview Features Support Scope</a>.</p></td>
</tr>
</tbody>
</table>

> [!NOTE]
> The Operator consumes the CR and creates an ingress node firewall daemon set on all the nodes that match the `nodeSelector`.

## Ingress Node Firewall Operator example configuration

A complete Ingress Node Firewall Configuration is specified in the following example:

<div class="formalpara">

<div class="title">

Example of how to create an Ingress Node Firewall Configuration object

</div>

``` yaml
$ cat << EOF | oc create -f -
apiVersion: ingressnodefirewall.openshift.io/v1alpha1
kind: IngressNodeFirewallConfig
metadata:
  name: ingressnodefirewallconfig
  namespace: openshift-ingress-node-firewall
spec:
  nodeSelector:
    node-role.kubernetes.io/worker: ""
EOF
```

</div>

> [!NOTE]
> The Operator consumes the CR object and creates an ingress node firewall daemon set on all the nodes that match the `nodeSelector`.

## Ingress Node Firewall rules object

You can review rule fields and examples to define which ingress traffic is allowed or denied by using the Ingress Node Firewall rules object.

The fields for the Ingress Node Firewall rules object are described in the following table:

| Field | Type | Description |
|----|----|----|
| `metadata.name` | `string` | The name of the CR object. |
| `interfaces` | `array` | The fields for this object specify the interfaces to apply the firewall rules to. For example, `- en0` and `- en1`. |
| `nodeSelector` | `array` | You can use `nodeSelector` to select the nodes to apply the firewall rules to. Set the value of your named `nodeselector` labels to `true` to apply the rule. |
| `ingress` | `object` | `ingress` allows you to configure the rules that allow outside access to the services on your cluster. |

Ingress Node Firewall rules object

### Ingress object configuration

The values for the `ingress` object are defined in the following table:

<table>
<caption><code>ingress</code> object</caption>
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
<td style="text-align: left;"><p><code>sourceCIDRs</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>Allows you to set the CIDR block. You can configure multiple CIDRs from different address families.</p>
<div class="note">
<div class="title">
&#10;</div>
<p>Different CIDRs allow you to use the same order rule. In the case that there are multiple <code>IngressNodeFirewall</code> objects for the same nodes and interfaces with overlapping CIDRs, the <code>order</code> field will specify which rule is applied first. Rules are applied in ascending order.</p>
</div></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>rules</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>Ingress firewall <code>rules.order</code> objects are ordered starting at <code>1</code> for each <code>source.CIDR</code> with up to 100 rules per CIDR. Lower order rules are executed first.</p>
<p><code>rules.protocolConfig.protocol</code> supports the following protocols: TCP, UDP, SCTP, ICMP and ICMPv6. ICMP and ICMPv6 rules can match against ICMP and ICMPv6 types or codes. TCP, UDP, and SCTP rules can match against a single destination port or a range of ports using <code>&lt;start : end-1&gt;</code> format.</p>
<p>Set <code>rules.action</code> to <code>allow</code> to apply the rule or <code>deny</code> to disallow the rule.</p>
<div class="note">
<div class="title">
&#10;</div>
<p>Ingress firewall rules are verified using a verification webhook that blocks any invalid configuration. The verification webhook prevents you from blocking any critical cluster services such as the API server.</p>
</div></td>
</tr>
</tbody>
</table>

### Ingress Node Firewall rules object example

A complete Ingress Node Firewall configuration is specified in the following example:

<div class="formalpara">

<div class="title">

Example Ingress Node Firewall configuration

</div>

``` yaml
apiVersion: ingressnodefirewall.openshift.io/v1alpha1
kind: IngressNodeFirewall
metadata:
  name: ingressnodefirewall
spec:
  interfaces:
  - eth0
  nodeSelector:
    matchLabels:
      <label_name>: <label_value>
  ingress:
  - sourceCIDRs:
       - 172.16.0.0/12
    rules:
    - order: 10
      protocolConfig:
        protocol: ICMP
        icmp:
          icmpType: 8 #ICMP Echo request
      action: Deny
    - order: 20
      protocolConfig:
        protocol: TCP
        tcp:
          ports: "8000-9000"
      action: Deny
  - sourceCIDRs:
       - fc00:f853:ccd:e793::0/64
    rules:
    - order: 10
      protocolConfig:
        protocol: ICMPv6
        icmpv6:
          icmpType: 128 #ICMPV6 Echo request
      action: Deny
```

</div>

\+ A `<label_name>` and a `<label_value>` must exist on the node and must match the `nodeselector` label and value applied to the nodes you want the `ingressfirewallconfig` CR to run on. The `<label_value>` can be `true` or `false`. By using `nodeSelector` labels, you can target separate groups of nodes to apply different rules to using the `ingressfirewallconfig` CR.

### Zero trust Ingress Node Firewall rules object example

Zero trust Ingress Node Firewall rules can provide additional security to multi-interface clusters. For example, you can use zero trust Ingress Node Firewall rules to drop all traffic on a specific interface except for SSH.

A complete configuration of a zero trust Ingress Node Firewall rule for a network-interface cluster is specified in the following example:

> [!IMPORTANT]
> Users need to add all ports their application will use to their allowlist in the following case to ensure proper functionality.

<div class="formalpara">

<div class="title">

Example zero trust Ingress Node Firewall rules

</div>

``` yaml
apiVersion: ingressnodefirewall.openshift.io/v1alpha1
kind: IngressNodeFirewall
metadata:
 name: ingressnodefirewall-zero-trust
spec:
 interfaces:
 - eth1
 nodeSelector:
   matchLabels:
     <ingress_firewall_label_name>: <label_value>
 ingress:
 - sourceCIDRs:
      - 0.0.0.0/0
   rules:
   - order: 10
     protocolConfig:
       protocol: TCP
       tcp:
         ports: 22
     action: Allow
   - order: 20
     action: Deny
```

</div>

> [!IMPORTANT]
> eBPF Manager Operator integration is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.
>
> For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

# Ingress Node Firewall Operator integration

Learn when to use eBPF Manager to load and manage Ingress Node Firewall programs.

The Ingress Node Firewall uses [eBPF](https://www.kernel.org/doc/html/latest/bpf/index.html) programs to implement some of its key firewall functionality. By default these eBPF programs are loaded into the kernel using a mechanism specific to the Ingress Node Firewall. You can configure the Ingress Node Firewall Operator to use the eBPF Manager Operator for loading and managing these programs instead.

When this integration is enabled, the following limitations apply:

- The Ingress Node Firewall Operator uses TCX if XDP is not available and TCX is incompatible with bpfman.

- The Ingress Node Firewall Operator daemon set pods remain in the `ContainerCreating` state until the firewall rules are applied.

- The Ingress Node Firewall Operator daemon set pods run as privileged.

# Configuring Ingress Node Firewall Operator to use the eBPF Manager Operator

Configure the Ingress Node Firewall to use eBPF Manager for program lifecycle control.

The Ingress Node Firewall uses [eBPF](https://www.kernel.org/doc/html/latest/bpf/index.html) programs to implement some of its key firewall functionality. By default these eBPF programs are loaded into the kernel using a mechanism specific to the Ingress Node Firewall.

As a cluster administrator, you can configure the Ingress Node Firewall Operator to use the eBPF Manager Operator for loading and managing these programs instead, adding additional security and observability functionality.

<div>

<div class="title">

Prerequisites

</div>

- You have installed the OpenShift CLI (`oc`).

- You have an account with administrator privileges.

- You installed the Ingress Node Firewall Operator.

- You have installed the eBPF Manager Operator.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Apply the following labels to the `ingress-node-firewall-system` namespace:

    ``` terminal
    $ oc label namespace openshift-ingress-node-firewall \
        pod-security.kubernetes.io/enforce=privileged \
        pod-security.kubernetes.io/warn=privileged --overwrite
    ```

2.  Edit the `IngressNodeFirewallConfig` object named `ingressnodefirewallconfig` and set the `ebpfProgramManagerMode` field:

    <div class="formalpara">

    <div class="title">

    Ingress Node Firewall Operator configuration object

    </div>

    ``` yaml
    apiVersion: ingressnodefirewall.openshift.io/v1alpha1
    kind: IngressNodeFirewallConfig
    metadata:
      name: ingressnodefirewallconfig
      namespace: openshift-ingress-node-firewall
    spec:
      nodeSelector:
        node-role.kubernetes.io/worker: ""
      ebpfProgramManagerMode: <ebpf_mode>
    ```

    </div>

    where:

    `<ebpf_mode>`: Specifies whether or not the Ingress Node Firewall Operator uses the eBPF Manager Operator to manage eBPF programs. Must be either `true` or `false`. If unset, eBPF Manager is not used.

</div>

# Viewing Ingress Node Firewall Operator rules

Inspect existing rules and configs to confirm the firewall is applied as intended.

<div>

<div class="title">

Procedure

</div>

1.  Run the following command to view all current rules :

    ``` terminal
    $ oc get ingressnodefirewall
    ```

2.  Choose one of the returned `<resource>` names and run the following command to view the rules or configs:

    ``` terminal
    $ oc get <resource> <name> -o yaml
    ```

</div>

# Troubleshooting the Ingress Node Firewall Operator

You can verify the status and view the logs to diagnose ingress firewall deployment or rule issues.

<div>

<div class="title">

Procedure

</div>

- Run the following command to list installed Ingress Node Firewall custom resource definitions (CRD):

  ``` terminal
  $ oc get crds | grep ingressnodefirewall
  ```

  <div class="formalpara">

  <div class="title">

  Example output

  </div>

  ``` terminal
  NAME               READY   UP-TO-DATE   AVAILABLE   AGE
  ingressnodefirewallconfigs.ingressnodefirewall.openshift.io       2022-08-25T10:03:01Z
  ingressnodefirewallnodestates.ingressnodefirewall.openshift.io    2022-08-25T10:03:00Z
  ingressnodefirewalls.ingressnodefirewall.openshift.io             2022-08-25T10:03:00Z
  ```

  </div>

- Run the following command to view the state of the Ingress Node Firewall Operator:

  ``` terminal
  $ oc get pods -n openshift-ingress-node-firewall
  ```

  <div class="formalpara">

  <div class="title">

  Example output

  </div>

  ``` terminal
  NAME                                       READY  STATUS         RESTARTS  AGE
  ingress-node-firewall-controller-manager   2/2    Running        0         5d21h
  ingress-node-firewall-daemon-pqx56         3/3    Running        0         5d21h
  ```

  </div>

  The following fields provide information about the status of the Operator: `READY`, `STATUS`, `AGE`, and `RESTARTS`. The `STATUS` field is `Running` when the Ingress Node Firewall Operator is deploying a daemon set to the assigned nodes.

- Run the following command to collect all ingress firewall node pods' logs:

  ``` terminal
  $ oc adm must-gather – gather_ingress_node_firewall
  ```

  The logs are available in the sos node’s report containing eBPF `bpftool` outputs at `/sos_commands/ebpf`. These reports include lookup tables used or updated as the ingress firewall XDP handles packet processing, updates statistics, and emits events.

</div>

# Additional resources

- [About the eBPF Manager Operator](ebpf_manager/ebpf-manager-operator-about.md#bpfman-operator-about)
