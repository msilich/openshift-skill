<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

For OpenShift Container Platform, Red Hat Enterprise Linux CoreOS (RHCOS) is the only supported operating system for control plane. For node hosts, OpenShift Container Platform supports both RHCOS and Red Hat Enterprise Linux (RHEL). With Red Hat Advanced Cluster Security for Kubernetes (RHACS), you can scan RHCOS nodes for vulnerabilities and detect potential security threats.

RHACS scans RHCOS RPMs installed on the node host, as part of the RHCOS installation, for any known vulnerabilities.

First, RHACS analyzes and detects RHCOS components. Then it matches vulnerabilities for identified components by using RHEL and the following data streams:

- OpenShift 4.X Open Vulnerability and Assessment Language (OVAL) v2 security data streams is used if StackRox Scanner is used for node scanning.

- Red Hat Common Security Advisory Framework (CSAF) Vulnerability Exploitability eXchange (VEX) is used if Scanner V4 is used for node scanning.

<div class="note">

<div class="title">

</div>

- If you installed RHACS by using the `roxctl` CLI, you must manually enable the RHCOS node scanning features. When you use Helm or Operator installation methods on OpenShift Container Platform, this feature is enabled by default.

</div>

<div>

<div class="title">

Additional resources

</div>

- [RHEL Versions Utilized by RHEL CoreOS and OCP](https://access.redhat.com/articles/6907891)

</div>

<a id="rhcos-enable-node-scan_scan-rhcos-node-host"></a>

# Enabling RHCOS node scanning with the StackRox Scanner

If you use OpenShift Container Platform, you can enable scanning of Red Hat Enterprise Linux CoreOS (RHCOS) nodes for vulnerabilities by using Red Hat Advanced Cluster Security for Kubernetes (RHACS).

> [!NOTE]
> Use Scanner V4 for full functionality when scanning nodes. For instructions on changing to Scanner V4 if you are using the StackRox scanner, see "Enabling Scanner V4".

<div>

<div class="title">

Prerequisites

</div>

- For scanning RHCOS node hosts of the secured cluster, you must have installed Secured Cluster services on OpenShift Container Platform 4.12 or later. For information about supported platforms and architecture, see the "Red Hat Advanced Cluster Security for Kubernetes Support Matrix". For life cycle support information for RHACS, see the "Red Hat Advanced Cluster Security for Kubernetes Support Policy".

- This procedure describes how to enable node scanning for the first time. If you are reconfiguring Red Hat Advanced Cluster Security for Kubernetes to use the StackRox Scanner instead of Scanner V4, follow the procedure in "Restoring RHCOS node scanning with the StackRox Scanner".

</div>

<div>

<div class="title">

Procedure

</div>

1.  Run one of the following commands to update the compliance container.

    - For a default compliance container with metrics disabled, run the following command:

      ``` terminal
      $ oc -n stackrox patch daemonset/collector -p '{"spec":{"template":{"spec":{"containers":[{"name":"compliance","env":[{"name":"ROX_METRICS_PORT","value":"disabled"},{"name":"ROX_NODE_SCANNING_ENDPOINT","value":"127.0.0.1:8444"},{"name":"ROX_NODE_SCANNING_INTERVAL","value":"4h"},{"name":"ROX_NODE_SCANNING_INTERVAL_DEVIATION","value":"24m"},{"name":"ROX_NODE_SCANNING_MAX_INITIAL_WAIT","value":"5m"},{"name":"ROX_RHCOS_NODE_SCANNING","value":"true"},{"name":"ROX_CALL_NODE_INVENTORY_ENABLED","value":"true"}]}]}}}}'
      ```

    - For a compliance container with Prometheus metrics enabled, run the following command:

      ``` terminal
      $ oc -n stackrox patch daemonset/collector -p '{"spec":{"template":{"spec":{"containers":[{"name":"compliance","env":[{"name":"ROX_METRICS_PORT","value":":9091"},{"name":"ROX_NODE_SCANNING_ENDPOINT","value":"127.0.0.1:8444"},{"name":"ROX_NODE_SCANNING_INTERVAL","value":"4h"},{"name":"ROX_NODE_SCANNING_INTERVAL_DEVIATION","value":"24m"},{"name":"ROX_NODE_SCANNING_MAX_INITIAL_WAIT","value":"5m"},{"name":"ROX_RHCOS_NODE_SCANNING","value":"true"},{"name":"ROX_CALL_NODE_INVENTORY_ENABLED","value":"true"}]}]}}}}'
      ```

2.  Update the Collector DaemonSet (DS) by taking the following steps:

    1.  Add new volume mounts to Collector DS by running the following command:

        ``` terminal
        $ oc -n stackrox patch daemonset/collector -p '{"spec":{"template":{"spec":{"volumes":[{"name":"tmp-volume","emptyDir":{}},{"name":"cache-volume","emptyDir":{"sizeLimit":"200Mi"}}]}}}}'
        ```

    2.  Add the new `NodeScanner` container by running the following command:

        ``` terminal
        $ oc -n stackrox patch daemonset/collector -p '{"spec":{"template":{"spec":{"containers":[{"command":["/scanner","--nodeinventory","--config=",""],"env":[{"name":"ROX_NODE_NAME","valueFrom":{"fieldRef":{"apiVersion":"v1","fieldPath":"spec.nodeName"}}},{"name":"ROX_CLAIR_V4_SCANNING","value":"true"},{"name":"ROX_COMPLIANCE_OPERATOR_INTEGRATION","value":"true"},{"name":"ROX_CSV_EXPORT","value":"false"},{"name":"ROX_DECLARATIVE_CONFIGURATION","value":"false"},{"name":"ROX_INTEGRATIONS_AS_CONFIG","value":"false"},{"name":"ROX_NETPOL_FIELDS","value":"true"},{"name":"ROX_NETWORK_DETECTION_BASELINE_SIMULATION","value":"true"},{"name":"ROX_NETWORK_GRAPH_PATTERNFLY","value":"true"},{"name":"ROX_NODE_SCANNING_CACHE_TIME","value":"3h36m"},{"name":"ROX_NODE_SCANNING_INITIAL_BACKOFF","value":"30s"},{"name":"ROX_NODE_SCANNING_MAX_BACKOFF","value":"5m"},{"name":"ROX_PROCESSES_LISTENING_ON_PORT","value":"false"},{"name":"ROX_QUAY_ROBOT_ACCOUNTS","value":"true"},{"name":"ROX_ROXCTL_NETPOL_GENERATE","value":"true"},{"name":"ROX_SOURCED_AUTOGENERATED_INTEGRATIONS","value":"false"},{"name":"ROX_SYSLOG_EXTRA_FIELDS","value":"true"},{"name":"ROX_SYSTEM_HEALTH_PF","value":"false"},{"name":"ROX_VULN_MGMT_WORKLOAD_CVES","value":"false"}],"image":"registry.redhat.io/advanced-cluster-security/rhacs-scanner-slim-rhel9:4.11.3","imagePullPolicy":"IfNotPresent","name":"node-inventory","ports":[{"containerPort":8444,"name":"grpc","protocol":"TCP"}],"volumeMounts":[{"mountPath":"/host","name":"host-root-ro","readOnly":true},{"mountPath":"/tmp/","name":"tmp-volume"},{"mountPath":"/cache","name":"cache-volume"}]}]}}}}'
        ```

</div>

<a id="rhcos-enable-node-scan-scannerv4_scan-rhcos-node-host"></a>

# Enabling RHCOS node scanning with Scanner V4

If you use OpenShift Container Platform, you can enable scanning of Red Hat Enterprise Linux CoreOS (RHCOS) nodes for vulnerabilities by using Red Hat Advanced Cluster Security for Kubernetes (RHACS).

> [!NOTE]
> For OpenShift Container Platform, use `oc` instead of `kubectl`.

<div>

<div class="title">

Prerequisites

</div>

- For scanning RHCOS node hosts of the secured cluster, you must have installed the following software:

  - Secured Cluster services on OpenShift Container Platform 4.12 or later

  - RHACS version 4.6 or later

    For information about supported platforms and architecture, see the [Red Hat Advanced Cluster Security for Kubernetes Support Matrix](https://access.redhat.com/articles/7045053). For life cycle support information for RHACS, see the [Red Hat Advanced Cluster Security for Kubernetes Support Policy](https://access.redhat.com/support/policy/updates/rhacs).

</div>

> [!NOTE]
> Node scanning with Scanner V4 is enabled by default in a new installation of release 4.8 and later. These steps are only required if you are updating from an earlier version of RHACS and Scanner V4 was not enabled. Although the StackRox Scanner is deprecated as of release 4.9, it still must be enabled on the cluster where Central is installed due to software dependencies.

1.  Ensure that Scanner V4 is deployed in the Central cluster:

    ``` terminal
    $ kubectl -n stackrox get deployment scanner-v4-indexer scanner-v4-matcher scanner-v4-db
    ```

2.  In the Central pod, on the `central` container, set the `ROX_NODE_INDEX_ENABLED` and the `ROX_SCANNER_V4` variables to `true` by running the following command on the Central cluster:

    ``` terminal
    $ kubectl -n stackrox set env deployment/central ROX_NODE_INDEX_ENABLED=true ROX_SCANNER_V4=true
    ```

3.  In the Sensor pod, on the `sensor` container, set the `ROX_NODE_INDEX_ENABLED` and the `ROX_SCANNER_V4` variables to `true` by running the following command on all secured clusters where you want to enable node scanning:

    ``` terminal
    $ kubectl -n stackrox set env deployment/sensor ROX_NODE_INDEX_ENABLED=true ROX_SCANNER_V4=true
    ```

4.  In the Collector Daemonset, in the `compliance` container, set the `ROX_NODE_INDEX_ENABLED` and the `ROX_SCANNER_V4` variables to `true` by running the following command on all secured clusters where you want to enable node scanning:

    ``` terminal
    $ kubectl -n stackrox set env daemonset/collector ROX_NODE_INDEX_ENABLED=true ROX_SCANNER_V4=true
    ```

5.  To verify that node scanning is working, examine the Central logs for the following message:

    ``` text
    Scanned index report and found <number> components for node <node_name>.
    ```

    where:

    `<number>`  
    Specifies the number of discovered components.

    `<node_name>`  
    Specifies the name of the node.

<a id="rhcos-analyse-detect_scan-rhcos-node-host"></a>

# Analysis and detection

When you use RHACS with OpenShift Container Platform, RHACS creates two coordinating containers for analysis and detection, the Compliance container and the Node-inventory container. The Compliance container was already a part of earlier RHACS versions. However, the Node-inventory container is new with RHACS 4.0 and works only with OpenShift Container Platform cluster nodes.

Upon start-up, the Compliance and Node-inventory containers begin the first inventory scan of Red Hat Enterprise Linux CoreOS (RHCOS) software components within five minutes. Next, the Node-inventory container scans the node’s file system to identify installed RPM packages and report on RHCOS software components. Afterward, inventory scanning occurs at periodic intervals, typically every four hours. You can customize the default interval by configuring the ROX_NODE_SCANNING_INTERVAL environment variable for the Compliance container.

<a id="rhcos-match-vulnerability_scan-rhcos-node-host"></a>

# Vulnerability matching on RHCOS nodes

Central services, which include Central and Scanner, perform vulnerability matching with the results from RHACS Scanner V4.

When scanning RHCOS nodes, RHACS releases after 4.0 no longer use the Kubernetes node metadata to find the kernel and container runtime versions. Instead, RHACS uses the installed RHCOS RPMs to assess that information.

<div>

<div class="title">

Additional resources

</div>

- [Enabling Scanner V4](../examine-images-for-vulnerabilities.md#scannerv4-enabling_examine-images-for-vulnerabilities)

- [Scanner V4 settings for installing RHACS for OpenShift Container Platform by using the Operator](../../installing/installing_ocp/install-central-config-options-ocp.md#scannerv4-settings_install-central-config-options-ocp)

- [Scanner V4 settings for installing RHACS for OpenShift Container Platform by using Helm](../../installing/installing_ocp/install-central-ocp.md#central-services-public-configuration-file-scannerv4_install-central-ocp)

- [Scanner V4 settings for installing RHACS for Kubernetes by using Helm](../../installing/installing_other/install-central-other.md#central-services-public-configuration-file-scannerv4_install-central-other)

</div>

<a id="rhcos-environment-variables_scan-rhcos-node-host"></a>

# Related environment variables

You can use the following environment variables to configure RHCOS node scanning on RHACS.

| Environment Variable | Description |
|----|----|
| `ROX_NODE_SCANNING_CACHE_TIME` | The time after which a cached inventory is considered outdated. Defaults to 90% of `ROX_NODE_SCANNING_INTERVAL` that is `3h36m`. |
| `ROX_NODE_SCANNING_INITIAL_BACKOFF` | The initial time in seconds a node scan will be delayed if a backoff file is found. The default value is `30s`. |
| `ROX_NODE_SCANNING_MAX_BACKOFF` | The upper limit of backoff. The default value is 5m, being 50% of Kubernetes restart policy stability timer. |

Node-inventory configuration

| Environment Variable | Description |
|----|----|
| `ROX_NODE_INDEX_ENABLED` | Controls whether node indexing is enabled for this cluster. The default value is `true`. |
| `ROX_NODE_SCANNING_INTERVAL` | The base value of the interval duration between node scans. The default value is `4h`. |
| `ROX_NODE_SCANNING_INTERVAL_DEVIATION` | The duration of node scans can differ from the base interval time. However, the maximum value is limited by the `ROX_NODE_SCANNING_INTERVAL`. |
| `ROX_NODE_SCANNING_MAX_INITIAL_WAIT` | The maximum wait time before the first node scan, which is randomly generated. You can set this value to `0` to disable the initial node scanning wait time. The default value is `5m`. |

Compliance configuration

<a id="identify-vulnerabilities-in-nodes_scan-rhcos-node-host"></a>

# Identifying vulnerabilities in nodes by using the dashboard

You can use the **Vulnerability Management** view to identify vulnerabilities in your nodes. The identified vulnerabilities include vulnerabilities in core Kubernetes components and container runtimes such as Docker, CRI-O, runC, and containerd. For more information on operating systems that RHACS can scan, see "Supported operating systems".

<div>

<div class="title">

Procedure

</div>

1.  In the RHACS portal, go to **Vulnerability Management** → **Dashboard**.

2.  Select **Nodes** on the header to view a list of all the CVEs affecting your nodes.

3.  Select a node from the list to view details of all CVEs affecting that node.

    1.  When you select a node, the **Node** details panel opens for the selected node. The **Node** view shows in-depth details of the node and includes information about CVEs by CVSS score and fixable CVEs for that node.

    2.  Select **View All** on the **CVEs by CVSS score** widget header to view a list of all the CVEs in the selected node. You can also filter the list of CVEs.

    3.  To export the fixable CVEs as a CSV file, select **Export as CSV** under the **Node Findings** section.

</div>

<a id="viewing-node-cves_scan-rhcos-node-host"></a>

# Viewing vulnerabilities in nodes

You can identify vulnerabilities in your nodes by using RHACS. The vulnerabilities that are identified include the following:

- Vulnerabilities in core Kubernetes components

- Vulnerabilities in container runtimes such as Docker, CRI-O, runC, and containerd

For more information about operating systems that RHACS can scan, see "Supported operating systems".

RHACS currently supports scanning nodes with the StackRox scanner and Scanner V4. Depending on which scanner is configured, different results might appear in the list of vulnerabilities. For more information, see "Understanding differences in scanning results between the StackRox Scanner and Scanner V4".

<div>

<div class="title">

Procedure

</div>

1.  In the RHACS portal, go to **Vulnerability Management** → **Results**.

2.  Select the **Nodes** tab.

3.  Optional: The page defaults to a list of observed CVEs. Click **Show snoozed CVEs** to view them.

4.  Optional: To filter CVEs according to entity, select the appropriate filters and attributes. To add more filtering criteria, follow these steps:

    1.  Select the entity or attribute from the list.

    2.  Depending on your choices, enter the appropriate information such as text, or select a date or object.

    3.  Click the right arrow icon.

    4.  Optional: Select additional entities and attributes, and then click the right arrow icon to add them. The filter entities and attributes are listed in the following table.

        <table>
        <caption>Filter options</caption>
        <colgroup>
        <col style="width: 50%" />
        <col style="width: 50%" />
        </colgroup>
        <thead>
        <tr>
        <th style="text-align: left;">Entity</th>
        <th style="text-align: left;">Attributes</th>
        </tr>
        </thead>
        <tbody>
        <tr>
        <td style="text-align: left;"><p>Node</p></td>
        <td style="text-align: left;"><ul>
        <li><p><strong>Name</strong>: The name of the node.</p></li>
        <li><p><strong>Operating system</strong>: The operating system of the node, for example, Red Hat Enterprise Linux (RHEL).</p></li>
        <li><p><strong>Label</strong>: The label of the node.</p></li>
        <li><p><strong>Annotation</strong>: The annotation for the node.</p></li>
        <li><p><strong>Scan time</strong>: The scan date of the node.</p></li>
        </ul></td>
        </tr>
        <tr>
        <td style="text-align: left;"><p>CVE</p></td>
        <td style="text-align: left;"><ul>
        <li><p><strong>Name</strong>: The name of the CVE.</p></li>
        <li><p><strong>Discovered time</strong>: The date when RHACS discovered the CVE.</p></li>
        <li><p><strong>CVSS</strong>: The severity level for the CVE.</p>
        <p>The following values are associated with the severity level for the CVE:</p>
        <ul>
        <li><p><strong>is greater than</strong></p></li>
        <li><p><strong>is greater than or equal to</strong></p></li>
        <li><p><strong>is equal to</strong></p></li>
        <li><p><strong>is less than or equal to</strong></p></li>
        <li><p><strong>is less than</strong></p></li>
        </ul></li>
        </ul></td>
        </tr>
        <tr>
        <td style="text-align: left;"><p>Node Component</p></td>
        <td style="text-align: left;"><ul>
        <li><p><strong>Name</strong>: The name of the component.</p></li>
        <li><p><strong>Version</strong>: The version of the component, for example, <code>4.15.0-2024</code>. You can use this to search for a specific version of a component, for example, in conjunction with a component name.</p></li>
        </ul></td>
        </tr>
        <tr>
        <td style="text-align: left;"><p>Cluster</p></td>
        <td style="text-align: left;"><ul>
        <li><p><strong>ID</strong>: The alphanumeric ID for the cluster. This is an internal identifier that RHACS assigns for tracking purposes.</p></li>
        <li><p><strong>Name</strong>: The name of the cluster.</p></li>
        <li><p><strong>Label</strong>: The label for the cluster.</p></li>
        <li><p><strong>Type</strong>: The type of cluster, for example, OCP.</p></li>
        <li><p><strong>Platform type</strong>: The type of platform, for example, OpenShift 4 cluster.</p></li>
        </ul></td>
        </tr>
        </tbody>
        </table>

5.  Optional: To refine the list of results, do any of the following tasks:

    - Click **CVE severity**, and then select one or more levels.

    - Click **CVE status**, and then select **Fixable** or **Not fixable**.

6.  To view the data, click one of the following tabs:

    - **\<number\> CVEs**: Displays a list of all the CVEs affecting all of your nodes.

    - **\<number\> Nodes**: Displays a list of nodes that contain CVEs.

7.  To view the details of the node and information about the CVEs according to the CVSS score and fixable CVEs for that node, click a node name in the list of nodes.

</div>

<a id="understanding-node-cves-scanner-v4_scan-rhcos-node-host"></a>

# Understanding differences in scanning results between the StackRox Scanner and Scanner V4

Scanning RHCOS node hosts with Scanner V4 reports significantly more CVEs for the same operating system version. For example, Scanner V4 reports about 390 CVEs, compared to about 50 CVEs that are reported by StackRox Scanner. A manual review of selected vulnerabilities revealed the following causes:

- The Vulnerability Exploitability eXchange (VEX) data used in Scanner V4 is more accurate.

- The VEX data includes granular statuses, such as "no fix planned" and "fix deferred".

- Some vulnerabilities reported by StackRox Scanner were false positives.

As a result, Scanner V4 provides a more accurate and realistic vulnerability assessment.

Users might find discrepancies in reported vulnerabilities surprising, especially if some secured clusters still use older RHACS versions with StackRox Scanner while others use Scanner V4. To help you understand this difference, the following example provides an explanation and guidance on how to manually verify reported vulnerabilities.

<a id="_example_of_discrepancies_in_reported_vulnerabilities"></a>

## Example of discrepancies in reported vulnerabilities

In this example, we analyzed the differences in reported CVEs for three arbitrarily selected RHCOS versions. This example presents findings for RHCOS version `417.94.202501071621-0`. For this version, RHACS provided the following scan results:

- StackRox Scanner reported 49 CVEs.

- Scanner V4 reported 389 CVEs.

The breakdown is as follows:

- 1 CVE is reported only by the StackRox Scanner.

- 48 CVEs are reported by both scanners.

- 341 CVEs are reported only by Scanner V4.

<a id="_cves_reported_only_by_the_stackrox_scanner"></a>

### CVEs reported only by the StackRox Scanner

The single CVE reported exclusively by StackRox Scanner was a false positive. CVE-2022-4122 was flagged for the `podman` package in version `5:5.2.2-1.rhaos4.17.el9.x86_64`. However, a manual review of VEX data from [RHSA-2024:9102](https://access.redhat.com/errata/RHSA-2024:9102) indicated that this vulnerability was fixed in version `5:5.2.2-1.el9`. Therefore, the package version scanned was the first to contain the fix and was no longer affected.

<a id="_cves_reported_only_by_scanner_v4"></a>

### CVEs reported only by Scanner V4

We randomly selected 10 CVEs from the 341 unique to Scanner V4 and conducted a detailed analysis using VEX data. The vulnerabilities fell into two categories:

- Affected packages with a fine-grained status indicating that no fix is planned

- Affected packages with no additional status details regarding a fix

For example, the following results were analyzed:

- The `git-core` package (version `2.43.5-1.el9_4`) was flagged for CVE-2024-50349 ([VEX data](https://access.redhat.com/security/cve/cve-2024-50349)) and marked as "Affected" with a fine-grained status of "Fix deferred." This means a fix is not guaranteed due to higher-priority development work. The package is affected by three CVEs in total.

- The `vim-minimal` package (version `2:8.2.2637-20.el9_1`) was flagged for 109 CVEs, 108 of which have low CVSS scores. Most are marked as "Affected" with a fine-grained status of "Will not fix."

- The `krb5-libs` package (version `1.21.1-2.el9_4.1`) was flagged for CVE-2025-24528 ([VEX data](https://access.redhat.com/security/cve/cve-2025-24528)), but no fine-grained status was available. Given that this CVE was recently discovered at the time of this analysis, its status might be updated soon.

<a id="_cves_reported_by_both_scanners"></a>

### CVEs reported by both scanners

We manually verified three randomly selected packages, finding that the OVAL v2 data used in the StackRox Scanner and the VEX data used in Scanner V4 provided consistent explanations for the detected CVEs. In some cases, CVSS scores differed slightly, which is expected due to variations in VEX publisher data.

<a id="_verifying_the_status_of_vulnerabilities"></a>

## Verifying the status of vulnerabilities

As a best practice, verify the fine-grained statuses of vulnerabilities in node host components that are critical to your environment using publicly available VEX data. VEX data is accessible in both human-readable and machine-readable formats. For more information about interpreting VEX data, visit [Recent improvements in Red Hat Enterprise Linux CoreOS security data](https://www.redhat.com/en/blog/recent-improvements-red-hat-enterprise-linux-coreos-security-data).
