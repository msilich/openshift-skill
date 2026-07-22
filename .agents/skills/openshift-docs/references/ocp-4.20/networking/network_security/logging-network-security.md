<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

The OVN-Kubernetes network plugin uses Open Virtual Network (OVN) access control lists (ACLs) to manage `AdminNetworkPolicy`, `BaselineAdminNetworkPolicy`, `NetworkPolicy`, and `EgressFirewall` objects. Audit logging exposes `Allow` and `Deny` ACL events for `NetworkPolicy`, `EgressFirewall` and `BaselineAdminNetworkPolicy` custom resources (CR). Logging also exposes `Allow`, `Deny`, and `Pass` ACL events for `AdminNetworkPolicy` (ANP) CR.

> [!NOTE]
> Audit logging is available for only the [OVN-Kubernetes network plugin](../ovn_kubernetes_network_provider/about-ovn-kubernetes.md#about-ovn-kubernetes).

# Audit configuration

Audit logging configuration in OpenShift Container Platform is defined in the `policyAuditConfig` section of the cluster `Network` custom resource for OVN-Kubernetes. You can review these default settings to plan log destinations, file size limits, and rate limits before you enable logging.

The following YAML illustrates the default values for the audit logging:

<div class="formalpara">

<div class="title">

Audit logging configuration

</div>

``` yaml
apiVersion: operator.openshift.io/v1
kind: Network
metadata:
  name: cluster
spec:
  defaultNetwork:
    ovnKubernetesConfig:
      policyAuditConfig:
        destination: "null"
        maxFileSize: 50
        rateLimit: 20
        syslogFacility: local0
```

</div>

The following table describes the configuration fields for audit logging.

<table>
<caption><code>policyAuditConfig</code> object</caption>
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
<td style="text-align: left;"><p><code>rateLimit</code></p></td>
<td style="text-align: left;"><p>integer</p></td>
<td style="text-align: left;"><p>The maximum number of messages to generate every second per node. The default value is <code>20</code> messages per second.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>maxFileSize</code></p></td>
<td style="text-align: left;"><p>integer</p></td>
<td style="text-align: left;"><p>The maximum size for the audit log in bytes. The default value is <code>50000000</code> or 50 MB.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>maxLogFiles</code></p></td>
<td style="text-align: left;"><p>integer</p></td>
<td style="text-align: left;"><p>The maximum number of log files that are retained.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>destination</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p>One of the following additional audit log targets:</p>
<dl>
<dt><code>libc</code></dt>
<dd>
<p>The libc <code>syslog()</code> function of the journald process on the host.</p>
</dd>
<dt><code>udp:&lt;host&gt;:&lt;port&gt;</code></dt>
<dd>
<p>A syslog server. Replace <code>&lt;host&gt;:&lt;port&gt;</code> with the host and port of the syslog server.</p>
</dd>
<dt><code>unix:&lt;file&gt;</code></dt>
<dd>
<p>A Unix Domain Socket file specified by <code>&lt;file&gt;</code>.</p>
</dd>
<dt><code>null</code></dt>
<dd>
<p>Do not send the audit logs to any additional target.</p>
</dd>
</dl></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>syslogFacility</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p>The syslog facility, such as <code>kern</code>, as defined by RFC5424. The default value is <code>local0</code>.</p></td>
</tr>
</tbody>
</table>

# Audit logging

You can enable network policy audit logging in OpenShift Container Platform by annotating namespaces with the `k8s.ovn.org/acl-logging` key and configuring log destinations for the OVN-Kubernetes plugin.

You can also configure the destination for audit logs, such as a syslog server or a UNIX domain socket. Regardless of any additional configuration, an audit log is always saved to `/var/log/ovn/acl-audit-log.log` on each OVN-Kubernetes pod in the cluster.

> [!NOTE]
> A network policy does not support setting the `Pass` action set as a rule.

The ACL-logging implementation logs access control list (ACL) events for a network. You can view these logs to analyze any potential security issues.

<div class="formalpara">

<div class="title">

Example namespace annotation

</div>

``` yaml
kind: Namespace
apiVersion: v1
metadata:
  name: example1
  annotations:
    k8s.ovn.org/acl-logging: |-
      {
        "deny": "info",
        "allow": "info"
      }
```

</div>

To view the default ACL logging configuration values, see the `policyAuditConfig` object in the `cluster-network-03-config.yml` file. If required, you can change the ACL logging configuration values for log file parameters in this file.

The logging message format is compatible with syslog as defined by RFC5424. The syslog facility is configurable and defaults to `local0`. The following example shows key parameters and their values outputted in a log message:

<div class="formalpara">

<div class="title">

Example logging message that outputs parameters and their values

</div>

``` terminal
<timestamp>|<message_serial>|acl_log(ovn_pinctrl0)|<severity>|name="<acl_name>", verdict="<verdict>", severity="<severity>", direction="<direction>": <flow>
```

</div>

Where:

- `<timestamp>` states the time and date for the creation of a log message.

- `<message_serial>` lists the serial number for a log message.

- `acl_log(ovn_pinctrl0)` is a literal string that prints the location of the log message in the OVN-Kubernetes plugin.

- `<severity>` sets the severity level for a log message. If you enable audit logging that supports `allow` and `deny` tasks then two severity levels show in the log message output.

- `<name>` states the name of the ACL-logging implementation in the OVN Network Bridging Database (`nbdb`) that was created by the network policy.

- `<verdict>` can be either `allow` or `drop`.

- `<direction>` can be either `to-lport` or `from-lport` to indicate that the policy was applied to traffic going to or away from a pod.

- `<flow>` shows packet information in a format equivalent to the `OpenFlow` protocol. This parameter comprises Open vSwitch (OVS) fields.

The following example shows OVS fields that the `flow` parameter uses to extract packet information from system memory:

<div class="formalpara">

<div class="title">

Example of OVS fields used by the `flow` parameter to extract packet information

</div>

``` terminal
<proto>,vlan_tci=0x0000,dl_src=<src_mac>,dl_dst=<source_mac>,nw_src=<source_ip>,nw_dst=<target_ip>,nw_tos=<tos_dscp>,nw_ecn=<tos_ecn>,nw_ttl=<ip_ttl>,nw_frag=<fragment>,tp_src=<tcp_src_port>,tp_dst=<tcp_dst_port>,tcp_flags=<tcp_flags>
```

</div>

Where:

- `<proto>` states the protocol. Valid values are `tcp` and `udp`.

- `vlan_tci=0x0000` states the VLAN header as `0` because a VLAN ID is not set for internal pod network traffic.

- `<src_mac>` specifies the source for the Media Access Control (MAC) address.

- `<source_mac>` specifies the destination for the MAC address.

- `<source_ip>` lists the source IP address

- `<target_ip>` lists the target IP address.

- `<tos_dscp>` states Differentiated Services Code Point (DSCP) values to classify and prioritize certain network traffic over other traffic.

- `<tos_ecn>` states Explicit Congestion Notification (ECN) values that indicate any congested traffic in your network.

- `<ip_ttl>` states the Time To Live (TTP) information for an packet.

- `<fragment>` specifies what type of IP fragments or IP non-fragments to match.

- `<tcp_src_port>` shows the source for the port for TCP and UDP protocols.

- `<tcp_dst_port>` lists the destination port for TCP and UDP protocols.

- `<tcp_flags>` supports numerous flags such as `SYN`, `ACK`, `PSH` and so on. If you need to set multiple values then each value is separated by a vertical bar (`|`). The UDP protocol does not support this parameter.

> [!NOTE]
> For more information about the previous field descriptions, go to the OVS manual page for `ovs-fields`.

<div class="formalpara">

<div class="title">

Example ACL deny log entry for a network policy

</div>

``` text
2023-11-02T16:28:54.139Z|00004|acl_log(ovn_pinctrl0)|INFO|name="NP:verify-audit-logging:Ingress", verdict=drop, severity=alert, direction=to-lport: tcp,vlan_tci=0x0000,dl_src=0a:58:0a:81:02:01,dl_dst=0a:58:0a:81:02:23,nw_src=10.131.0.39,nw_dst=10.129.2.35,nw_tos=0,nw_ecn=0,nw_ttl=62,nw_frag=no,tp_src=58496,tp_dst=8080,tcp_flags=syn
2023-11-02T16:28:55.187Z|00005|acl_log(ovn_pinctrl0)|INFO|name="NP:verify-audit-logging:Ingress", verdict=drop, severity=alert, direction=to-lport: tcp,vlan_tci=0x0000,dl_src=0a:58:0a:81:02:01,dl_dst=0a:58:0a:81:02:23,nw_src=10.131.0.39,nw_dst=10.129.2.35,nw_tos=0,nw_ecn=0,nw_ttl=62,nw_frag=no,tp_src=58496,tp_dst=8080,tcp_flags=syn
2023-11-02T16:28:57.235Z|00006|acl_log(ovn_pinctrl0)|INFO|name="NP:verify-audit-logging:Ingress", verdict=drop, severity=alert, direction=to-lport: tcp,vlan_tci=0x0000,dl_src=0a:58:0a:81:02:01,dl_dst=0a:58:0a:81:02:23,nw_src=10.131.0.39,nw_dst=10.129.2.35,nw_tos=0,nw_ecn=0,nw_ttl=62,nw_frag=no,tp_src=58496,tp_dst=8080,tcp_flags=syn
```

</div>

The following table describes namespace annotation values:

| Field | Description |
|----|----|
| `deny` | Blocks namespace access to any traffic that matches an ACL rule with the `deny` action. The field supports `alert`, `warning`, `notice`, `info`, or `debug` values. |
| `allow` | Permits namespace access to any traffic that matches an ACL rule with the `allow` action. The field supports `alert`, `warning`, `notice`, `info`, or `debug` values. |
| `pass` | A `pass` action applies to an admin network policy’s ACL rule. A `pass` action allows either the network policy in the namespace or the baseline admin network policy rule to evaluate all incoming and outgoing traffic. A network policy does not support a `pass` action. |

Audit logging namespace annotation for `k8s.ovn.org/acl-logging`

<div>

<div class="title">

Additional resources

</div>

- [Understanding network policy APIs](network-policy-apis.md#network-policy-apis)

</div>

# AdminNetworkPolicy audit logging

You can enable audit logging for individual `AdminNetworkPolicy` custom resources in OpenShift Container Platform by annotating each policy with the `k8s.ovn.org/acl-logging` key. Use the resulting logs to verify how `Allow`, `Deny`, and `Pass` rules affect traffic between namespaces.

<div class="example">

<div class="title">

Example of annotation for `AdminNetworkPolicy` CR

</div>

``` yaml
apiVersion: policy.networking.k8s.io/v1alpha1
kind: AdminNetworkPolicy
metadata:
  annotations:
    k8s.ovn.org/acl-logging: '{ "deny": "alert", "allow": "alert", "pass" : "warning" }'
  name: anp-tenant-log
spec:
  priority: 5
  subject:
    namespaces:
      matchLabels:
        tenant: backend-storage # Selects all pods owned by storage tenant.
  ingress:
    - name: "allow-all-ingress-product-development-and-customer" # Product development and customer tenant ingress to backend storage.
      action: "Allow"
      from:
      - pods:
          namespaceSelector:
            matchExpressions:
            - key: tenant
              operator: In
              values:
              - product-development
              - customer
          podSelector: {}
    - name: "pass-all-ingress-product-security"
      action: "Pass"
      from:
      - namespaces:
          matchLabels:
              tenant: product-security
    - name: "deny-all-ingress" # Ingress to backend from all other pods in the cluster.
      action: "Deny"
      from:
      - namespaces: {}
  egress:
    - name: "allow-all-egress-product-development"
      action: "Allow"
      to:
      - pods:
          namespaceSelector:
            matchLabels:
              tenant: product-development
          podSelector: {}
    - name: "pass-egress-product-security"
      action: "Pass"
      to:
      - namespaces:
           matchLabels:
             tenant: product-security
    - name: "deny-all-egress" # Egress from backend denied to all other pods.
      action: "Deny"
      to:
      - namespaces: {}
```

</div>

Logs are generated whenever a specific OVN ACL is hit and meets the action criteria set in your logging annotation. For example, an event in which any of the namespaces with the label `tenant: product-development` accesses the namespaces with the label `tenant: backend-storage`, a log is generated.

> [!NOTE]
> ACL logging is limited to 60 characters. If your ANP `name` field is long, the rest of the log will be truncated.

The following is a direction index for the examples log entries that follow:

<table>
<colgroup>
<col style="width: 40%" />
<col style="width: 60%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Direction</th>
<th style="text-align: left;">Rule</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>Ingress</p></td>
<td style="text-align: left;"><dl>
<dt>Rule0</dt>
<dd>
<p>Allow from tenant <code>product-development</code> and <code>customer</code> to tenant <code>backend-storage</code>; Ingress0: <code>Allow</code></p>
</dd>
<dt>Rule1</dt>
<dd>
<p>Pass from <code>product-security`to tenant `backend-storage</code>; Ingress1: <code>Pass</code></p>
</dd>
<dt>Rule2</dt>
<dd>
<p>Deny ingress from all pods; Ingress2: <code>Deny</code></p>
</dd>
</dl></td>
</tr>
<tr>
<td style="text-align: left;"><p>Egress</p></td>
<td style="text-align: left;"><dl>
<dt>Rule0</dt>
<dd>
<p>Allow to <code>product-development</code>; Egress0: <code>Allow</code></p>
</dd>
<dt>Rule1</dt>
<dd>
<p>Pass to <code>product-security</code>; Egress1: <code>Pass</code></p>
</dd>
<dt>Rule2</dt>
<dd>
<p>Deny egress to all other pods; Egress2: <code>Deny</code></p>
</dd>
</dl></td>
</tr>
</tbody>
</table>

<div class="example">

<div class="title">

Example ACL log entry for `Allow` action of the `AdminNetworkPolicy` named `anp-tenant-log` with `Ingress:0` and `Egress:0`

</div>

``` text
2024-06-10T16:27:45.194Z|00052|acl_log(ovn_pinctrl0)|INFO|name="ANP:anp-tenant-log:Ingress:0", verdict=allow, severity=alert, direction=to-lport: tcp,vlan_tci=0x0000,dl_src=0a:58:0a:80:02:1a,dl_dst=0a:58:0a:80:02:19,nw_src=10.128.2.26,nw_dst=10.128.2.25,nw_tos=0,nw_ecn=0,nw_ttl=64,nw_frag=no,tp_src=57814,tp_dst=8080,tcp_flags=syn
2024-06-10T16:28:23.130Z|00059|acl_log(ovn_pinctrl0)|INFO|name="ANP:anp-tenant-log:Ingress:0", verdict=allow, severity=alert, direction=to-lport: tcp,vlan_tci=0x0000,dl_src=0a:58:0a:80:02:18,dl_dst=0a:58:0a:80:02:19,nw_src=10.128.2.24,nw_dst=10.128.2.25,nw_tos=0,nw_ecn=0,nw_ttl=64,nw_frag=no,tp_src=38620,tp_dst=8080,tcp_flags=ack
2024-06-10T16:28:38.293Z|00069|acl_log(ovn_pinctrl0)|INFO|name="ANP:anp-tenant-log:Egress:0", verdict=allow, severity=alert, direction=from-lport: tcp,vlan_tci=0x0000,dl_src=0a:58:0a:80:02:19,dl_dst=0a:58:0a:80:02:1a,nw_src=10.128.2.25,nw_dst=10.128.2.26,nw_tos=0,nw_ecn=0,nw_ttl=64,nw_frag=no,tp_src=47566,tp_dst=8080,tcp_flags=fin|ack=0,nw_ecn=0,nw_ttl=64,nw_frag=no,tp_src=55704,tp_dst=8080,tcp_flags=ack
```

</div>

<div class="example">

<div class="title">

Example ACL log entry for `Pass` action of the `AdminNetworkPolicy` named `anp-tenant-log` with `Ingress:1` and `Egress:1`

</div>

``` text
2024-06-10T16:33:12.019Z|00075|acl_log(ovn_pinctrl0)|INFO|name="ANP:anp-tenant-log:Ingress:1", verdict=pass, severity=warning, direction=to-lport: tcp,vlan_tci=0x0000,dl_src=0a:58:0a:80:02:1b,dl_dst=0a:58:0a:80:02:19,nw_src=10.128.2.27,nw_dst=10.128.2.25,nw_tos=0,nw_ecn=0,nw_ttl=64,nw_frag=no,tp_src=37394,tp_dst=8080,tcp_flags=ack
2024-06-10T16:35:04.209Z|00081|acl_log(ovn_pinctrl0)|INFO|name="ANP:anp-tenant-log:Egress:1", verdict=pass, severity=warning, direction=from-lport: tcp,vlan_tci=0x0000,dl_src=0a:58:0a:80:02:19,dl_dst=0a:58:0a:80:02:1b,nw_src=10.128.2.25,nw_dst=10.128.2.27,nw_tos=0,nw_ecn=0,nw_ttl=64,nw_frag=no,tp_src=34018,tp_dst=8080,tcp_flags=ack
```

</div>

<div class="example">

<div class="title">

Example ACL log entry for `Deny` action of the `AdminNetworkPolicy` named `anp-tenant-log` with `Egress:2` and `Ingress2`

</div>

``` text
2024-06-10T16:43:05.287Z|00087|acl_log(ovn_pinctrl0)|INFO|name="ANP:anp-tenant-log:Egress:2", verdict=drop, severity=alert, direction=from-lport: tcp,vlan_tci=0x0000,dl_src=0a:58:0a:80:02:19,dl_dst=0a:58:0a:80:02:18,nw_src=10.128.2.25,nw_dst=10.128.2.24,nw_tos=0,nw_ecn=0,nw_ttl=64,nw_frag=no,tp_src=51598,tp_dst=8080,tcp_flags=syn
2024-06-10T16:44:43.591Z|00090|acl_log(ovn_pinctrl0)|INFO|name="ANP:anp-tenant-log:Ingress:2", verdict=drop, severity=alert, direction=to-lport: tcp,vlan_tci=0x0000,dl_src=0a:58:0a:80:02:1c,dl_dst=0a:58:0a:80:02:19,nw_src=10.128.2.28,nw_dst=10.128.2.25,nw_tos=0,nw_ecn=0,nw_ttl=64,nw_frag=no,tp_src=33774,tp_dst=8080,tcp_flags=syn
```

</div>

The following table describes ANP annotation:

<table>
<caption>Audit logging AdminNetworkPolicy annotation</caption>
<colgroup>
<col style="width: 40%" />
<col style="width: 60%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Annotation</th>
<th style="text-align: left;">Value</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>k8s.ovn.org/acl-logging</code></p></td>
<td style="text-align: left;"><p>You must specify at least one of <code>Allow</code>, <code>Deny</code>, or <code>Pass</code> to enable audit logging for a namespace.</p>
<dl>
<dt><code>Deny</code></dt>
<dd>
<p>Optional: Specify <code>alert</code>, <code>warning</code>, <code>notice</code>, <code>info</code>, or <code>debug</code>.</p>
</dd>
<dt><code>Allow</code></dt>
<dd>
<p>Optional: Specify <code>alert</code>, <code>warning</code>, <code>notice</code>, <code>info</code>, or <code>debug</code>.</p>
</dd>
<dt><code>Pass</code></dt>
<dd>
<p>Optional: Specify <code>alert</code>, <code>warning</code>, <code>notice</code>, <code>info</code>, or <code>debug</code>.</p>
</dd>
</dl></td>
</tr>
</tbody>
</table>

# BaselineAdminNetworkPolicy audit logging

You can enable audit logging for `BaselineAdminNetworkPolicy` custom resources in OpenShift Container Platform by annotating each policy with the `k8s.ovn.org/acl-logging` key.

<div class="example">

<div class="title">

Example of annotation for `BaselineAdminNetworkPolicy` CR

</div>

``` yaml
apiVersion: policy.networking.k8s.io/v1alpha1
kind: BaselineAdminNetworkPolicy
metadata:
  annotations:
    k8s.ovn.org/acl-logging: '{ "deny": "alert", "allow": "alert"}'
  name: default
spec:
  subject:
    namespaces:
      matchLabels:
          tenant: workloads # Selects all workload pods in the cluster.
  ingress:
  - name: "default-allow-dns" # This rule allows ingress from dns tenant to all workloads.
    action: "Allow"
    from:
    - namespaces:
          matchLabels:
            tenant: dns
  - name: "default-deny-dns" # This rule denies all ingress from all pods to workloads.
    action: "Deny"
    from:
    - namespaces: {} # Use the empty selector with caution because it also selects OpenShift namespaces as well.
  egress:
  - name: "default-deny-dns" # This rule denies all egress from workloads. It will be applied when no ANP or network policy matches.
    action: "Deny"
    to:
    - namespaces: {} # Use the empty selector with caution because it also selects OpenShift namespaces as well.
```

</div>

In the example, an event in which any of the namespaces with the label `tenant: dns` accesses the namespaces with the label `tenant: workloads`, a log is generated.

The following is a direction index for the examples log entries that follow:

<table>
<colgroup>
<col style="width: 40%" />
<col style="width: 60%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Direction</th>
<th style="text-align: left;">Rule</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>Ingress</p></td>
<td style="text-align: left;"><dl>
<dt>Rule0</dt>
<dd>
<p>Allow from tenant <code>dns</code> to tenant <code>workloads</code>; Ingress0: <code>Allow</code></p>
</dd>
<dt>Rule1</dt>
<dd>
<p>Deny to tenant <code>workloads</code> from all pods; Ingress1: <code>Deny</code></p>
</dd>
</dl></td>
</tr>
<tr>
<td style="text-align: left;"><p>Egress</p></td>
<td style="text-align: left;"><dl>
<dt>Rule0</dt>
<dd>
<p>Deny to all pods; Egress0: <code>Deny</code></p>
</dd>
</dl></td>
</tr>
</tbody>
</table>

<div class="example">

<div class="title">

Example ACL allow log entry for `Allow` action of `default` BANP with `Ingress:0`

</div>

``` text
2024-06-10T18:11:58.263Z|00022|acl_log(ovn_pinctrl0)|INFO|name="BANP:default:Ingress:0", verdict=allow, severity=alert, direction=to-lport: tcp,vlan_tci=0x0000,dl_src=0a:58:0a:82:02:57,dl_dst=0a:58:0a:82:02:56,nw_src=10.130.2.87,nw_dst=10.130.2.86,nw_tos=0,nw_ecn=0,nw_ttl=64,nw_frag=no,tp_src=60510,tp_dst=8080,tcp_flags=syn
2024-06-10T18:11:58.264Z|00023|acl_log(ovn_pinctrl0)|INFO|name="BANP:default:Ingress:0", verdict=allow, severity=alert, direction=to-lport: tcp,vlan_tci=0x0000,dl_src=0a:58:0a:82:02:57,dl_dst=0a:58:0a:82:02:56,nw_src=10.130.2.87,nw_dst=10.130.2.86,nw_tos=0,nw_ecn=0,nw_ttl=64,nw_frag=no,tp_src=60510,tp_dst=8080,tcp_flags=psh|ack
2024-06-10T18:11:58.264Z|00024|acl_log(ovn_pinctrl0)|INFO|name="BANP:default:Ingress:0", verdict=allow, severity=alert, direction=to-lport: tcp,vlan_tci=0x0000,dl_src=0a:58:0a:82:02:57,dl_dst=0a:58:0a:82:02:56,nw_src=10.130.2.87,nw_dst=10.130.2.86,nw_tos=0,nw_ecn=0,nw_ttl=64,nw_frag=no,tp_src=60510,tp_dst=8080,tcp_flags=ack
2024-06-10T18:11:58.264Z|00025|acl_log(ovn_pinctrl0)|INFO|name="BANP:default:Ingress:0", verdict=allow, severity=alert, direction=to-lport: tcp,vlan_tci=0x0000,dl_src=0a:58:0a:82:02:57,dl_dst=0a:58:0a:82:02:56,nw_src=10.130.2.87,nw_dst=10.130.2.86,nw_tos=0,nw_ecn=0,nw_ttl=64,nw_frag=no,tp_src=60510,tp_dst=8080,tcp_flags=ack
2024-06-10T18:11:58.264Z|00026|acl_log(ovn_pinctrl0)|INFO|name="BANP:default:Ingress:0", verdict=allow, severity=alert, direction=to-lport: tcp,vlan_tci=0x0000,dl_src=0a:58:0a:82:02:57,dl_dst=0a:58:0a:82:02:56,nw_src=10.130.2.87,nw_dst=10.130.2.86,nw_tos=0,nw_ecn=0,nw_ttl=64,nw_frag=no,tp_src=60510,tp_dst=8080,tcp_flags=fin|ack
2024-06-10T18:11:58.264Z|00027|acl_log(ovn_pinctrl0)|INFO|name="BANP:default:Ingress:0", verdict=allow, severity=alert, direction=to-lport: tcp,vlan_tci=0x0000,dl_src=0a:58:0a:82:02:57,dl_dst=0a:58:0a:82:02:56,nw_src=10.130.2.87,nw_dst=10.130.2.86,nw_tos=0,nw_ecn=0,nw_ttl=64,nw_frag=no,tp_src=60510,tp_dst=8080,tcp_flags=ack
```

</div>

<div class="example">

<div class="title">

Example ACL allow log entry for `Allow` action of `default` BANP with `Egress:0` and `Ingress:1`

</div>

``` text
2024-06-10T18:09:57.774Z|00016|acl_log(ovn_pinctrl0)|INFO|name="BANP:default:Egress:0", verdict=drop, severity=alert, direction=from-lport: tcp,vlan_tci=0x0000,dl_src=0a:58:0a:82:02:56,dl_dst=0a:58:0a:82:02:57,nw_src=10.130.2.86,nw_dst=10.130.2.87,nw_tos=0,nw_ecn=0,nw_ttl=64,nw_frag=no,tp_src=45614,tp_dst=8080,tcp_flags=syn
2024-06-10T18:09:58.809Z|00017|acl_log(ovn_pinctrl0)|INFO|name="BANP:default:Egress:0", verdict=drop, severity=alert, direction=from-lport: tcp,vlan_tci=0x0000,dl_src=0a:58:0a:82:02:56,dl_dst=0a:58:0a:82:02:57,nw_src=10.130.2.86,nw_dst=10.130.2.87,nw_tos=0,nw_ecn=0,nw_ttl=64,nw_frag=no,tp_src=45614,tp_dst=8080,tcp_flags=syn
2024-06-10T18:10:00.857Z|00018|acl_log(ovn_pinctrl0)|INFO|name="BANP:default:Egress:0", verdict=drop, severity=alert, direction=from-lport: tcp,vlan_tci=0x0000,dl_src=0a:58:0a:82:02:56,dl_dst=0a:58:0a:82:02:57,nw_src=10.130.2.86,nw_dst=10.130.2.87,nw_tos=0,nw_ecn=0,nw_ttl=64,nw_frag=no,tp_src=45614,tp_dst=8080,tcp_flags=syn
2024-06-10T18:10:25.414Z|00019|acl_log(ovn_pinctrl0)|INFO|name="BANP:default:Ingress:1", verdict=drop, severity=alert, direction=to-lport: tcp,vlan_tci=0x0000,dl_src=0a:58:0a:82:02:58,dl_dst=0a:58:0a:82:02:56,nw_src=10.130.2.88,nw_dst=10.130.2.86,nw_tos=0,nw_ecn=0,nw_ttl=64,nw_frag=no,tp_src=40630,tp_dst=8080,tcp_flags=syn
2024-06-10T18:10:26.457Z|00020|acl_log(ovn_pinctrl0)|INFO|name="BANP:default:Ingress:1", verdict=drop, severity=alert, direction=to-lport: tcp,vlan_tci=0x0000,dl_src=0a:58:0a:82:02:58,dl_dst=0a:58:0a:82:02:56,nw_src=10.130.2.88,nw_dst=10.130.2.86,nw_tos=0,nw_ecn=0,nw_ttl=64,nw_frag=no,tp_src=40630,tp_dst=8080,tcp_flags=syn
2024-06-10T18:10:28.505Z|00021|acl_log(ovn_pinctrl0)|INFO|name="BANP:default:Ingress:1", verdict=drop, severity=alert, direction=to-lport: tcp,vlan_tci=0x0000,dl_src=0a:58:0a:82:02:58,dl_dst=0a:58:0a:82:02:56,nw_src=10.130.2.88,nw_dst=10.130.2.86,nw_tos=0,nw_ecn=0,nw_ttl=64,nw_frag=no,tp_src=40630,tp_dst=8080,tcp_flags=syn
```

</div>

The following table describes BANP annotation:

<table>
<caption>Audit logging BaselineAdminNetworkPolicy annotation</caption>
<colgroup>
<col style="width: 40%" />
<col style="width: 60%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Annotation</th>
<th style="text-align: left;">Value</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>k8s.ovn.org/acl-logging</code></p></td>
<td style="text-align: left;"><p>You must specify at least one of <code>Allow</code> or <code>Deny</code> to enable audit logging for a namespace.</p>
<dl>
<dt><code>Deny</code></dt>
<dd>
<p>Optional: Specify <code>alert</code>, <code>warning</code>, <code>notice</code>, <code>info</code>, or <code>debug</code>.</p>
</dd>
<dt><code>Allow</code></dt>
<dd>
<p>Optional: Specify <code>alert</code>, <code>warning</code>, <code>notice</code>, <code>info</code>, or <code>debug</code>.</p>
</dd>
</dl></td>
</tr>
</tbody>
</table>

# Configuring egress firewall and network policy auditing for a cluster

To customize egress firewall and network policy audit logging in OpenShift Container Platform, you can configure the `policyAuditConfig` section in the cluster `Network` custom resource. Adjust log destination, file size, and rate limits to control how ACL events are recorded.

<div>

<div class="title">

Prerequisites

</div>

- Install the OpenShift CLI (`oc`).

- Log in to the cluster with a user with `cluster-admin` privileges.

</div>

<div>

<div class="title">

Procedure

</div>

- To customize the audit logging configuration, enter the following command:

  ``` terminal
  $ oc edit network.operator.openshift.io/cluster
  ```

  > [!TIP]
  > You can also customize and apply the following YAML to configure audit logging:
  >
  > ``` yaml
  > apiVersion: operator.openshift.io/v1
  > kind: Network
  > metadata:
  >   name: cluster
  > spec:
  >   defaultNetwork:
  >     ovnKubernetesConfig:
  >       policyAuditConfig:
  >         destination: "null"
  >         maxFileSize: 50
  >         rateLimit: 20
  >         syslogFacility: local0
  > ```

</div>

<div>

<div class="title">

Verification

</div>

1.  To create a namespace with network policies complete the following steps:

    1.  Create a namespace for verification:

        ``` terminal
        $ cat <<EOF| oc create -f -
        kind: Namespace
        apiVersion: v1
        metadata:
          name: verify-audit-logging
          annotations:
            k8s.ovn.org/acl-logging: '{ "deny": "alert", "allow": "alert" }'
        EOF
        ```

        Successful output lists the namespace with the network policy and the `created` status.

    2.  Create network policies for the namespace:

        ``` terminal
        $ cat <<EOF| oc create -n verify-audit-logging -f -
        apiVersion: networking.k8s.io/v1
        kind: NetworkPolicy
        metadata:
          name: deny-all
        spec:
          podSelector:
            matchLabels:
          policyTypes:
          - Ingress
          - Egress
        ---
        apiVersion: networking.k8s.io/v1
        kind: NetworkPolicy
        metadata:
          name: allow-from-same-namespace
          namespace: verify-audit-logging
        spec:
          podSelector: {}
          policyTypes:
           - Ingress
           - Egress
          ingress:
            - from:
                - podSelector: {}
          egress:
            - to:
               - namespaceSelector:
                  matchLabels:
                    kubernetes.io/metadata.name: verify-audit-logging
        EOF
        ```

        <div class="formalpara">

        <div class="title">

        Example output

        </div>

        ``` text
        networkpolicy.networking.k8s.io/deny-all created
        networkpolicy.networking.k8s.io/allow-from-same-namespace created
        ```

        </div>

2.  Create a pod for source traffic in the `default` namespace:

    ``` terminal
    $ cat <<EOF| oc create -n default -f -
    apiVersion: v1
    kind: Pod
    metadata:
      name: client
    spec:
      containers:
        - name: client
          image: registry.access.redhat.com/rhel7/rhel-tools
          command: ["/bin/sh", "-c"]
          args:
            ["sleep inf"]
    EOF
    ```

3.  Create two pods in the `verify-audit-logging` namespace:

    ``` terminal
    $ for name in client server; do
    cat <<EOF| oc create -n verify-audit-logging -f -
    apiVersion: v1
    kind: Pod
    metadata:
      name: ${name}
    spec:
      containers:
        - name: ${name}
          image: registry.access.redhat.com/rhel7/rhel-tools
          command: ["/bin/sh", "-c"]
          args:
            ["sleep inf"]
    EOF
    done
    ```

    Successful output lists the two pods, such as `pod/client` and `pod/server`, and the `created` status.

4.  To generate traffic and produce network policy audit log entries, complete the following steps:

    1.  Obtain the IP address for pod named `server` in the `verify-audit-logging` namespace:

        ``` terminal
        $ POD_IP=$(oc get pods server -n verify-audit-logging -o jsonpath='{.status.podIP}')
        ```

    2.  Ping the IP address from an earlier command from the pod named `client` in the `default` namespace and confirm the all packets are dropped:

        ``` terminal
        $ oc exec -it client -n default -- /bin/ping -c 2 $POD_IP
        ```

        <div class="formalpara">

        <div class="title">

        Example output

        </div>

        ``` text
        PING 10.128.2.55 (10.128.2.55) 56(84) bytes of data.

        --- 10.128.2.55 ping statistics ---
        2 packets transmitted, 0 received, 100% packet loss, time 2041ms
        ```

        </div>

    3.  From the client pod in the `verify-audit-logging` namespace, ping the IP address stored in the `POD_IP shell` environment variable and confirm the system allows all packets.

        ``` terminal
        $ oc exec -it client -n verify-audit-logging -- /bin/ping -c 2 $POD_IP
        ```

        <div class="formalpara">

        <div class="title">

        Example output

        </div>

        ``` text
        PING 10.128.0.86 (10.128.0.86) 56(84) bytes of data.
        64 bytes from 10.128.0.86: icmp_seq=1 ttl=64 time=2.21 ms
        64 bytes from 10.128.0.86: icmp_seq=2 ttl=64 time=0.440 ms

        --- 10.128.0.86 ping statistics ---
        2 packets transmitted, 2 received, 0% packet loss, time 1001ms
        rtt min/avg/max/mdev = 0.440/1.329/2.219/0.890 ms
        ```

        </div>

5.  Display the latest entries in the network policy audit log:

    ``` terminal
    $ for pod in $(oc get pods -n openshift-ovn-kubernetes -l app=ovnkube-node --no-headers=true | awk '{ print $1 }') ; do
        oc exec -it $pod -n openshift-ovn-kubernetes -- tail -4 /var/log/ovn/acl-audit-log.log
      done
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` text
    2023-11-02T16:28:54.139Z|00004|acl_log(ovn_pinctrl0)|INFO|name="NP:verify-audit-logging:Ingress", verdict=drop, severity=alert, direction=to-lport: tcp,vlan_tci=0x0000,dl_src=0a:58:0a:81:02:01,dl_dst=0a:58:0a:81:02:23,nw_src=10.131.0.39,nw_dst=10.129.2.35,nw_tos=0,nw_ecn=0,nw_ttl=62,nw_frag=no,tp_src=58496,tp_dst=8080,tcp_flags=syn
    2023-11-02T16:28:55.187Z|00005|acl_log(ovn_pinctrl0)|INFO|name="NP:verify-audit-logging:Ingress", verdict=drop, severity=alert, direction=to-lport: tcp,vlan_tci=0x0000,dl_src=0a:58:0a:81:02:01,dl_dst=0a:58:0a:81:02:23,nw_src=10.131.0.39,nw_dst=10.129.2.35,nw_tos=0,nw_ecn=0,nw_ttl=62,nw_frag=no,tp_src=58496,tp_dst=8080,tcp_flags=syn
    2023-11-02T16:28:57.235Z|00006|acl_log(ovn_pinctrl0)|INFO|name="NP:verify-audit-logging:Ingress", verdict=drop, severity=alert, direction=to-lport: tcp,vlan_tci=0x0000,dl_src=0a:58:0a:81:02:01,dl_dst=0a:58:0a:81:02:23,nw_src=10.131.0.39,nw_dst=10.129.2.35,nw_tos=0,nw_ecn=0,nw_ttl=62,nw_frag=no,tp_src=58496,tp_dst=8080,tcp_flags=syn
    2023-11-02T16:49:57.909Z|00028|acl_log(ovn_pinctrl0)|INFO|name="NP:verify-audit-logging:allow-from-same-namespace:Egress:0", verdict=allow, severity=alert, direction=from-lport: icmp,vlan_tci=0x0000,dl_src=0a:58:0a:81:02:22,dl_dst=0a:58:0a:81:02:23,nw_src=10.129.2.34,nw_dst=10.129.2.35,nw_tos=0,nw_ecn=0,nw_ttl=64,nw_frag=no,icmp_type=8,icmp_code=0
    2023-11-02T16:49:57.909Z|00029|acl_log(ovn_pinctrl0)|INFO|name="NP:verify-audit-logging:allow-from-same-namespace:Ingress:0", verdict=allow, severity=alert, direction=to-lport: icmp,vlan_tci=0x0000,dl_src=0a:58:0a:81:02:22,dl_dst=0a:58:0a:81:02:23,nw_src=10.129.2.34,nw_dst=10.129.2.35,nw_tos=0,nw_ecn=0,nw_ttl=64,nw_frag=no,icmp_type=8,icmp_code=0
    2023-11-02T16:49:58.932Z|00030|acl_log(ovn_pinctrl0)|INFO|name="NP:verify-audit-logging:allow-from-same-namespace:Egress:0", verdict=allow, severity=alert, direction=from-lport: icmp,vlan_tci=0x0000,dl_src=0a:58:0a:81:02:22,dl_dst=0a:58:0a:81:02:23,nw_src=10.129.2.34,nw_dst=10.129.2.35,nw_tos=0,nw_ecn=0,nw_ttl=64,nw_frag=no,icmp_type=8,icmp_code=0
    2023-11-02T16:49:58.932Z|00031|acl_log(ovn_pinctrl0)|INFO|name="NP:verify-audit-logging:allow-from-same-namespace:Ingress:0", verdict=allow, severity=alert, direction=to-lport: icmp,vlan_tci=0x0000,dl_src=0a:58:0a:81:02:22,dl_dst=0a:58:0a:81:02:23,nw_src=10.129.2.34,nw_dst=10.129.2.35,nw_tos=0,nw_ecn=0,nw_ttl=64,nw_frag=no,icmp_type=8,icmp_code=0
    ```

    </div>

</div>

# Enabling egress firewall and network policy audit logging for a namespace

To enable egress firewall and network policy audit logging for a namespace in OpenShift Container Platform, you can add the `k8s.ovn.org/acl-logging` annotation with the `oc annotate` command. You can also apply a namespace YAML file that sets `Allow` and `Deny` log severity levels.

<div>

<div class="title">

Prerequisites

</div>

- Install the OpenShift CLI (`oc`).

- Log in to the cluster with a user with `cluster-admin` privileges.

</div>

<div>

<div class="title">

Procedure

</div>

- To enable audit logging for a namespace, enter the following command:

  ``` terminal
  $ oc annotate namespace <namespace> \
    k8s.ovn.org/acl-logging='{ "deny": "alert", "allow": "notice" }'
  ```

  where:

  `<namespace>`
  Specifies the name of the namespace.

  > [!TIP]
  > You can also apply the following YAML to enable audit logging:
  >
  > ``` yaml
  > kind: Namespace
  > apiVersion: v1
  > metadata:
  >   name: <namespace>
  >   annotations:
  >     k8s.ovn.org/acl-logging: |-
  >       {
  >         "deny": "alert",
  >         "allow": "notice"
  >       }
  > ```

  Successful output lists the audit logging name and the `annotated` status.

</div>

<div>

<div class="title">

Verification

</div>

- Display the latest entries in the audit log:

  ``` terminal
  $ for pod in $(oc get pods -n openshift-ovn-kubernetes -l app=ovnkube-node --no-headers=true | awk '{ print $1 }') ; do
      oc exec -it $pod -n openshift-ovn-kubernetes -- tail -4 /var/log/ovn/acl-audit-log.log
    done
  ```

  <div class="formalpara">

  <div class="title">

  Example output

  </div>

  ``` text
  2023-11-02T16:49:57.909Z|00028|acl_log(ovn_pinctrl0)|INFO|name="NP:verify-audit-logging:allow-from-same-namespace:Egress:0", verdict=allow, severity=alert, direction=from-lport: icmp,vlan_tci=0x0000,dl_src=0a:58:0a:81:02:22,dl_dst=0a:58:0a:81:02:23,nw_src=10.129.2.34,nw_dst=10.129.2.35,nw_tos=0,nw_ecn=0,nw_ttl=64,nw_frag=no,icmp_type=8,icmp_code=0
  2023-11-02T16:49:57.909Z|00029|acl_log(ovn_pinctrl0)|INFO|name="NP:verify-audit-logging:allow-from-same-namespace:Ingress:0", verdict=allow, severity=alert, direction=to-lport: icmp,vlan_tci=0x0000,dl_src=0a:58:0a:81:02:22,dl_dst=0a:58:0a:81:02:23,nw_src=10.129.2.34,nw_dst=10.129.2.35,nw_tos=0,nw_ecn=0,nw_ttl=64,nw_frag=no,icmp_type=8,icmp_code=0
  2023-11-02T16:49:58.932Z|00030|acl_log(ovn_pinctrl0)|INFO|name="NP:verify-audit-logging:allow-from-same-namespace:Egress:0", verdict=allow, severity=alert, direction=from-lport: icmp,vlan_tci=0x0000,dl_src=0a:58:0a:81:02:22,dl_dst=0a:58:0a:81:02:23,nw_src=10.129.2.34,nw_dst=10.129.2.35,nw_tos=0,nw_ecn=0,nw_ttl=64,nw_frag=no,icmp_type=8,icmp_code=0
  2023-11-02T16:49:58.932Z|00031|acl_log(ovn_pinctrl0)|INFO|name="NP:verify-audit-logging:allow-from-same-namespace:Ingress:0", verdict=allow, severity=alert, direction=to-lport: icmp,vlan_tci=0x0000,dl_src=0a:58:0a:81:02:22,dl_dst=0a:58:0a:81:02:23,nw_src=10.129.2.34,nw_dst=10.129.2.35,nw_tos=0,nw_ecn=0,nw_ttl=64,nw_frag=no,icmp_type=8,icmp_code=0
  ```

  </div>

</div>

# Disabling egress firewall and network policy audit logging for a namespace

To disable egress firewall and network policy audit logging for a namespace in OpenShift Container Platform, you can remove the `k8s.ovn.org/acl-logging` annotation with the `oc annotate` command. You can also apply a namespace YAML file that sets the annotation to `null`.

<div>

<div class="title">

Prerequisites

</div>

- Install the OpenShift CLI (`oc`).

- Log in to the cluster with a user with `cluster-admin` privileges.

</div>

<div>

<div class="title">

Procedure

</div>

- To disable audit logging for a namespace, enter the following command:

  ``` terminal
  $ oc annotate --overwrite namespace <namespace> k8s.ovn.org/acl-logging-
  ```

  where:

  `<namespace>`
  Specifies the name of the namespace.

  > [!TIP]
  > You can also apply the following YAML to disable audit logging:
  >
  > ``` yaml
  > kind: Namespace
  > apiVersion: v1
  > metadata:
  >   name: <namespace>
  >   annotations:
  >     k8s.ovn.org/acl-logging: null
  > ```

  Successful output lists the audit logging name and the `annotated` status.

</div>

# Additional resources

- [About network policy](network_policy/about-network-policy.md#about-network-policy)

- [Configuring an egress firewall for a project](egress_firewall/configuring-egress-firewall-ovn.md#configuring-egress-firewall-ovn)
