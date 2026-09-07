<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Monitor TLS traffic to identify insecure protocols, detect security risks, and maintain compliance without decrypting traffic.

# Transport Layer Security traffic monitoring

Transport Layer Security (TLS) traffic monitoring identifies security risks and maintains compliance by analyzing encrypted traffic metadata without decryption.

As a network administrator or security practitioner, you must verify that encrypted traffic uses secure protocols and cipher suites. Monitoring TLS usage identifies security risks, such as workloads that use deprecated TLS versions, and helps maintain compliance with cluster security policies.

## Security improvements through metadata analysis

The Network Observability Operator captures TLS metadata from handshake messages without decrypting traffic, providing visibility into encryption protocols while maintaining data privacy. This approach enables the following improvements:

Security risk detection
Identifies workloads using deprecated TLS versions (1.0, 1.1) or weak cipher suites by capturing TLS version, cipher suite, and group information. You can configure Prometheus alerts to automatically report deprecated TLS configurations.

Compliance auditing
Audits TLS configurations to meet regulatory requirements through metric aggregation in dashboard charts and overview panels. You can filter flows by TLS fields to isolate specific protocol versions or cipher suites for compliance reporting.

Security posture assessment
Visualizes encrypted network traffic with lock icons in the topology view and identifies unencrypted communications across your cluster. You can analyze TLS usage patterns to evaluate your overall security posture.

Remediation prioritization
Targets workloads using deprecated protocols for updates by filtering and analyzing TLS fields to isolate problematic connections requiring immediate attention.

## TLS traffic monitoring workflow phases

To monitor TLS traffic effectively, complete the following phases:

- Enable the TLS tracking feature in the eBPF agent configuration.

- Analyze TLS traffic details in the **Network Traffic** view.

- Visualize secure connections in the **Topology** view.

# Enable Transport Layer Security tracking

Enable Transport Layer Security (TLS) tracking to monitor encryption protocols and identify security risks in the cluster.

> [!NOTE]
> TLS fields only appear in flows for connections that perform a TLS handshake after the feature is enabled.

<div>

<div class="title">

Prerequisites

</div>

- The Network Observability Operator is installed.

- The `FlowCollector` custom resource (CR) is configured with `spec.agent.type: eBPF`.

- Access to the cluster with `cluster-admin` privileges.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Edit the `FlowCollector` CR by running the following command:

    ``` terminal
    $ oc edit flowcollector cluster
    ```

2.  Add `TLSTracking` to the `spec.agent.ebpf.features` list:

    ``` yaml
    apiVersion: flows.netobserv.io/v1beta2
    kind: FlowCollector
    metadata:
      name: cluster
    spec:
      agent:
        type: eBPF
        ebpf:
          features:
          - TLSTracking
    # ...
    ```

    where:

    `spec.agent.ebpf.features`
    Specifies the list of eBPF agent features to enable. Add `TLSTracking` to this array to enable TLS metadata capture from handshake messages.

3.  Save and exit your editor.

</div>

<div>

<div class="title">

Verification

</div>

1.  Confirm that the eBPF agent pods have restarted by running the following command:

    ``` terminal
    $ oc get pods -n netobserv-privileged
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    NAME                                    READY   STATUS    RESTARTS   AGE
    netobserv-ebpf-agent-abc12              1/1     Running   0          2m
    ```

    </div>

2.  Verify the TLS tracking feature is active by running the following command:

    ``` terminal
    $ oc logs -n netobserv-privileged ds/netobserv-ebpf-agent | grep "EnableTLSTracking"
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    EnableTLSTracking:true
    ```

    </div>

    The output confirms that the TLS tracking feature has been initialized in the eBPF agent.

</div>

# Analyze Transport Layer Security traffic data

View and filter Transport Layer Security (TLS) metadata to identify deprecated configurations and verify encryption compliance in the cluster.

<div>

<div class="title">

Prerequisites

</div>

- The Network Observability Operator is installed.

- TLS tracking is enabled in the `FlowCollector` custom resource (CR).

- Access to the OpenShift Container Platform web console.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Navigate to **Observe** → **Network Traffic** in the OpenShift Container Platform web console and click the **Traffic flows** tab.

    > [!NOTE]
    > The **TLS Version** column is enabled by default. If the default TLS version column is not visible after enabling TLS tracking, click **Restore default columns** in **Manage columns** to refresh the table.

2.  Add TLS-specific columns to the traffic table:

    1.  Click **Manage columns**.

    2.  Select the **TLS Cipher Suite**, **TLS Group**, and **TLS Types** checkboxes.

    3.  Click **Save**.

3.  Filter traffic by message type to view complete TLS metadata:

    1.  In the filter bar, select **TLS Types** and choose **ServerHello** from the dropdown menu.

        `ServerHello` messages contain negotiated TLS metadata such as cipher suite and cryptographic group information.

4.  Filter traffic by TLS version to identify deprecated configurations:

    1.  In the filter bar, select **TLS Version**.

    2.  Select the versions you want to review:

        - **1.0**: Deprecated

        - **1.1**: Deprecated

        - **1.2**: Legacy

        - **1.3**: Current standard

          To identify all deprecated connections, filter for TLS versions 1.0 and 1.1.

5.  Analyze TLS metrics in the overview panel:

    1.  Click the **Overview** tab.

    2.  Review the default TLS panels, which include **TLS usage (network flows per second)** and **TLS per version (network flows per second)**.

    3.  Optional: To view additional TLS metrics, click **Manage panels** to select and display additional panels, such as **TLS per group (network flows per second)** or **TLS per cipher suite (network flows per second)**.

6.  Identify secure connections in the **Topology** view:

    1.  Click the **Topology** tab.

        Connections secured with TLS are marked with a lock icon. The color of the lock icon indicates the security level:

        - **Red**: Deprecated TLS versions (1.0 or 1.1)

        - **Yellow**: Legacy configurations (TLS 1.2)

        - **Green**: Secure connections (TLS 1.3)

        - **Blue**: Post-Quantum Cryptography (PQC) compliant

          Select a connection node to view its specific TLS version and cipher suite details.

7.  View TLS metrics in the Network Observability dashboard:

    1.  Navigate to **Observe** → **Dashboards**.

    2.  Search for **NetObserv** and review the available metrics:

        - **TLS Traffic**: Displays overall TLS traffic metrics.

        - **Flows rate per TLS version**: Displays traffic trends by TLS version over time.

        - **Flows rate per TLS group**: Displays traffic by TLS group over time.

</div>

# Transport Layer Security tracking fields reference

Transport Layer Security (TLS) metadata fields track and define encryption protocols, protocol versions, and cipher suite data to help you analyze secure network flows.

<table>
<caption>TLS tracking fields</caption>
<colgroup>
<col style="width: 14%" />
<col style="width: 28%" />
<col style="width: 28%" />
<col style="width: 28%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Field</th>
<th style="text-align: left;">Description</th>
<th style="text-align: left;">Possible values</th>
<th style="text-align: left;">Availability</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><strong>TLS Version</strong></p></td>
<td style="text-align: left;"><p>Negotiated TLS protocol version.</p></td>
<td style="text-align: left;"><ul>
<li><p><code>1.0</code>: Deprecated</p></li>
<li><p><code>1.1</code>: Deprecated</p></li>
<li><p><code>1.2</code>: Secure</p></li>
<li><p><code>1.3</code>: Current standard</p></li>
</ul></td>
<td style="text-align: left;"><p><code>ClientHello</code>, <code>ServerHello</code></p>
<p><code>ClientHello</code> displays the version requested by the client. <code>ServerHello</code> displays the negotiated version selected by the server.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><strong>TLS Cipher Suite</strong></p></td>
<td style="text-align: left;"><p>Cryptographic algorithm suite negotiated between the client and server.</p></td>
<td style="text-align: left;"><p>Examples:</p>
<ul>
<li><p><code>TLS_AES_256_GCM_SHA384</code></p></li>
<li><p><code>TLS_CHACHA20_POLY1305_SHA256</code></p></li>
</ul></td>
<td style="text-align: left;"><p><code>ServerHello</code> only</p>
<p>Displays as <code>n/a</code> in <code>ClientHello</code> messages.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><strong>TLS Group</strong></p></td>
<td style="text-align: left;"><p>Elliptic curve used for key exchange.</p></td>
<td style="text-align: left;"><p>Examples:</p>
<ul>
<li><p><code>X25519</code>: Recommended for TLS 1.3</p></li>
<li><p><code>secp256r1</code> (P-256)</p></li>
</ul></td>
<td style="text-align: left;"><p><code>ServerHello</code> (TLS 1.3 only)</p>
<p>Displays as <code>n/a</code> in <code>ClientHello</code> messages and TLS 1.2 connections.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><strong>TLS Types</strong></p></td>
<td style="text-align: left;"><p>Type of TLS handshake message captured.</p></td>
<td style="text-align: left;"><ul>
<li><p><code>ClientHello</code>: Initial client request</p></li>
<li><p><code>ServerHello</code>: Server response</p></li>
</ul></td>
<td style="text-align: left;"><p>All TLS flows</p></td>
</tr>
</tbody>
</table>
