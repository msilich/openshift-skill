<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Monitor the consumption of cluster infrastructure resources by using the metrics provided by OpenShift Virtualization. These metrics are also used to query live migration status.

<div class="note">

<div class="title">

</div>

- To use the vCPU metric, apply the `schedstats=enable` kernel argument to the `MachineConfig` object. This kernel argument enables scheduler statistics used for debugging and performance tuning and adds a minor additional load to the scheduler.

- For guest memory swapping queries to return data, enable memory swapping on the virtual guests.

</div>

# Querying metrics for all projects with the OpenShift Container Platform web console

Monitor the state of a cluster and any user-defined workloads by using the OpenShift Container Platform metrics query browser. The query browser uses Prometheus Query Language (PromQL) queries to examine metrics visualized on a plot.

As a cluster administrator or as a user with view permissions for all projects, you can access metrics for all default OpenShift Container Platform and user-defined projects in the Metrics UI.

<div>

<div class="title">

Prerequisites

</div>

- You have access to the cluster as a user with the `cluster-admin` cluster role or with view permissions for all projects.

- You have installed the OpenShift CLI (`oc`).

</div>

<div>

<div class="title">

Procedure

</div>

1.  In the OpenShift Container Platform web console, click **Observe** → **Metrics**.

2.  To add one or more queries, perform any of the following actions:

    <table>
    <colgroup>
    <col style="width: 50%" />
    <col style="width: 50%" />
    </colgroup>
    <thead>
    <tr>
    <th style="text-align: left;">Option</th>
    <th style="text-align: left;">Description</th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td style="text-align: left;"><p>Select an existing query.</p></td>
    <td style="text-align: left;"><p>From the <strong>Select query</strong> drop-down list, select an existing query.</p></td>
    </tr>
    <tr>
    <td style="text-align: left;"><p>Create a custom query.</p></td>
    <td style="text-align: left;"><p>Add your Prometheus Query Language (PromQL) query to the <strong>Expression</strong> field.</p>
    <p>As you type a PromQL expression, autocomplete suggestions appear in a drop-down list. These suggestions include functions, metrics, labels, and time tokens. Use the keyboard arrows to select one of these suggested items and then press Enter to add the item to your expression. Move your mouse pointer over a suggested item to view a brief description of that item.</p></td>
    </tr>
    <tr>
    <td style="text-align: left;"><p>Add multiple queries.</p></td>
    <td style="text-align: left;"><p>Click <strong>Add query</strong>.</p></td>
    </tr>
    <tr>
    <td style="text-align: left;"><p>Duplicate an existing query.</p></td>
    <td style="text-align: left;"><p>Click the options menu <img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABsAAAAjCAIAAADqn+bCAAAACXBIWXMAAA7EAAAOxAGVKw4bAAAA+0lEQVRIie2WMQqEMBBFJ47gUXRBLyBYqbUXULCx9CR2XsAb6AlUEM9kpckW7obdZhwWYWHXX/3i8TPJZEKEUgpOlXFu3JX4V4kmB2qaZhgGKSUiZlkWxzEBC84N9zxv27bdO47Tti0Bs3at4wBgXVca/lJnfN/XPggCGmadIwAsywIAiGhZFk1ydy2EYJKgGCqK4vZUVVU0zKpxnmftp2mi4S/1GhG1N82DMWNNYVmW4zgqpRAxTVMa5t4evlg11nXd9/1eY57nSZIQMKtG13WllLu3bbvrOgJmdUbHwfur8Xniqw6Hh5UYRdGDNowwDA+WvP4UV+JPJ94B1gKUWcTOCT0AAAAASUVORK5CYII=" alt="kebab" /> next to the query, then choose <strong>Duplicate query</strong>.</p></td>
    </tr>
    <tr>
    <td style="text-align: left;"><p>Disable a query from being run.</p></td>
    <td style="text-align: left;"><p>Click the options menu <img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABsAAAAjCAIAAADqn+bCAAAACXBIWXMAAA7EAAAOxAGVKw4bAAAA+0lEQVRIie2WMQqEMBBFJ47gUXRBLyBYqbUXULCx9CR2XsAb6AlUEM9kpckW7obdZhwWYWHXX/3i8TPJZEKEUgpOlXFu3JX4V4kmB2qaZhgGKSUiZlkWxzEBC84N9zxv27bdO47Tti0Bs3at4wBgXVca/lJnfN/XPggCGmadIwAsywIAiGhZFk1ydy2EYJKgGCqK4vZUVVU0zKpxnmftp2mi4S/1GhG1N82DMWNNYVmW4zgqpRAxTVMa5t4evlg11nXd9/1eY57nSZIQMKtG13WllLu3bbvrOgJmdUbHwfur8Xniqw6Hh5UYRdGDNowwDA+WvP4UV+JPJ94B1gKUWcTOCT0AAAAASUVORK5CYII=" alt="kebab" /> next to the query and choose <strong>Disable query</strong>.</p></td>
    </tr>
    </tbody>
    </table>

3.  To run queries that you created, click **Run queries**. The metrics from the queries are visualized on the plot. If a query is invalid, the UI shows an error message.

    <div class="note">

    <div class="title">

    </div>

    - When drawing time series graphs, queries that operate on large amounts of data might time out or overload the browser. To avoid this, click **Hide graph** and calibrate your query by using only the metrics table. Then, after finding a feasible query, enable the plot to draw the graphs.

    - By default, the query table shows an expanded view that lists every metric and its current value. Click the **˅** down arrowhead to minimize the expanded view for a query.

    </div>

4.  Optional: Save the page URL to use this set of queries again in the future.

5.  Explore the visualized metrics. Initially, all metrics from all enabled queries are shown on the plot. Select which metrics are shown by performing any of the following actions:

    <table>
    <colgroup>
    <col style="width: 50%" />
    <col style="width: 50%" />
    </colgroup>
    <thead>
    <tr>
    <th style="text-align: left;">Option</th>
    <th style="text-align: left;">Description</th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td style="text-align: left;"><p>Hide all metrics from a query.</p></td>
    <td style="text-align: left;"><p>Click the options menu <img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABsAAAAjCAIAAADqn+bCAAAACXBIWXMAAA7EAAAOxAGVKw4bAAAA+0lEQVRIie2WMQqEMBBFJ47gUXRBLyBYqbUXULCx9CR2XsAb6AlUEM9kpckW7obdZhwWYWHXX/3i8TPJZEKEUgpOlXFu3JX4V4kmB2qaZhgGKSUiZlkWxzEBC84N9zxv27bdO47Tti0Bs3at4wBgXVca/lJnfN/XPggCGmadIwAsywIAiGhZFk1ydy2EYJKgGCqK4vZUVVU0zKpxnmftp2mi4S/1GhG1N82DMWNNYVmW4zgqpRAxTVMa5t4evlg11nXd9/1eY57nSZIQMKtG13WllLu3bbvrOgJmdUbHwfur8Xniqw6Hh5UYRdGDNowwDA+WvP4UV+JPJ94B1gKUWcTOCT0AAAAASUVORK5CYII=" alt="kebab" /> for the query and click <strong>Hide all series</strong>.</p></td>
    </tr>
    <tr>
    <td style="text-align: left;"><p>Hide a specific metric.</p></td>
    <td style="text-align: left;"><p>Go to the query table and click the colored square near the metric name.</p></td>
    </tr>
    <tr>
    <td style="text-align: left;"><p>Zoom into the plot and change the time range.</p></td>
    <td style="text-align: left;"><p>Perform one of the following actions:</p>
    <ul>
    <li><p>Visually select the time range by clicking and dragging on the plot horizontally.</p></li>
    <li><p>Use the menu to select the time range.</p></li>
    </ul></td>
    </tr>
    <tr>
    <td style="text-align: left;"><p>Reset the time range.</p></td>
    <td style="text-align: left;"><p>Click <strong>Reset zoom</strong>.</p></td>
    </tr>
    <tr>
    <td style="text-align: left;"><p>Display outputs for all queries at a specific point in time.</p></td>
    <td style="text-align: left;"><p>Hover over the plot at the point you are interested in. The query outputs appear in a pop-up box.</p></td>
    </tr>
    <tr>
    <td style="text-align: left;"><p>Hide the plot.</p></td>
    <td style="text-align: left;"><p>Click <strong>Hide graph</strong>.</p></td>
    </tr>
    </tbody>
    </table>

</div>

# Querying metrics for user-defined projects with the OpenShift Container Platform web console

Monitor user-defined workloads by using the OpenShift Container Platform metrics query browser. The query browser uses Prometheus Query Language (PromQL) queries to examine metrics visualized on a plot.

To query metrics in the **Developer** perspective, you must specify a project name that represents the namespace. You must have the required privileges to view metrics for the selected project.

<div>

<div class="title">

Prerequisites

</div>

- You have access to the cluster as a developer or as a user with view permissions for the project that you are viewing metrics for.

- You have enabled monitoring for user-defined projects.

- You have deployed a service in a user-defined project.

- You have created a `ServiceMonitor` custom resource definition (CRD) for the service to define how the service is monitored.

</div>

<div>

<div class="title">

Procedure

</div>

1.  In the OpenShift Container Platform web console, click **Observe** → **Metrics**.

2.  To add one or more queries, perform any of the following actions:

    <table>
    <colgroup>
    <col style="width: 50%" />
    <col style="width: 50%" />
    </colgroup>
    <thead>
    <tr>
    <th style="text-align: left;">Option</th>
    <th style="text-align: left;">Description</th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td style="text-align: left;"><p>Select an existing query.</p></td>
    <td style="text-align: left;"><p>From the <strong>Select query</strong> drop-down list, select an existing query.</p></td>
    </tr>
    <tr>
    <td style="text-align: left;"><p>Create a custom query.</p></td>
    <td style="text-align: left;"><p>Add your Prometheus Query Language (PromQL) query to the <strong>Expression</strong> field.</p>
    <p>As you type a PromQL expression, autocomplete suggestions appear in a drop-down list. These suggestions include functions, metrics, labels, and time tokens. Use the keyboard arrows to select one of these suggested items and then press Enter to add the item to your expression. Move your mouse pointer over a suggested item to view a brief description of that item.</p></td>
    </tr>
    <tr>
    <td style="text-align: left;"><p>Add multiple queries.</p></td>
    <td style="text-align: left;"><p>Click <strong>Add query</strong>.</p></td>
    </tr>
    <tr>
    <td style="text-align: left;"><p>Duplicate an existing query.</p></td>
    <td style="text-align: left;"><p>Click the options menu <img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABsAAAAjCAIAAADqn+bCAAAACXBIWXMAAA7EAAAOxAGVKw4bAAAA+0lEQVRIie2WMQqEMBBFJ47gUXRBLyBYqbUXULCx9CR2XsAb6AlUEM9kpckW7obdZhwWYWHXX/3i8TPJZEKEUgpOlXFu3JX4V4kmB2qaZhgGKSUiZlkWxzEBC84N9zxv27bdO47Tti0Bs3at4wBgXVca/lJnfN/XPggCGmadIwAsywIAiGhZFk1ydy2EYJKgGCqK4vZUVVU0zKpxnmftp2mi4S/1GhG1N82DMWNNYVmW4zgqpRAxTVMa5t4evlg11nXd9/1eY57nSZIQMKtG13WllLu3bbvrOgJmdUbHwfur8Xniqw6Hh5UYRdGDNowwDA+WvP4UV+JPJ94B1gKUWcTOCT0AAAAASUVORK5CYII=" alt="kebab" /> next to the query, then choose <strong>Duplicate query</strong>.</p></td>
    </tr>
    <tr>
    <td style="text-align: left;"><p>Disable a query from being run.</p></td>
    <td style="text-align: left;"><p>Click the options menu <img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABsAAAAjCAIAAADqn+bCAAAACXBIWXMAAA7EAAAOxAGVKw4bAAAA+0lEQVRIie2WMQqEMBBFJ47gUXRBLyBYqbUXULCx9CR2XsAb6AlUEM9kpckW7obdZhwWYWHXX/3i8TPJZEKEUgpOlXFu3JX4V4kmB2qaZhgGKSUiZlkWxzEBC84N9zxv27bdO47Tti0Bs3at4wBgXVca/lJnfN/XPggCGmadIwAsywIAiGhZFk1ydy2EYJKgGCqK4vZUVVU0zKpxnmftp2mi4S/1GhG1N82DMWNNYVmW4zgqpRAxTVMa5t4evlg11nXd9/1eY57nSZIQMKtG13WllLu3bbvrOgJmdUbHwfur8Xniqw6Hh5UYRdGDNowwDA+WvP4UV+JPJ94B1gKUWcTOCT0AAAAASUVORK5CYII=" alt="kebab" /> next to the query and choose <strong>Disable query</strong>.</p></td>
    </tr>
    </tbody>
    </table>

3.  To run queries that you created, click **Run queries**. The metrics from the queries are visualized on the plot. If a query is invalid, the UI shows an error message.

    <div class="note">

    <div class="title">

    </div>

    - When drawing time series graphs, queries that operate on large amounts of data might time out or overload the browser. To avoid this, click **Hide graph** and calibrate your query by using only the metrics table. Then, after finding a feasible query, enable the plot to draw the graphs.

    - By default, the query table shows an expanded view that lists every metric and its current value. Click the **˅** down arrowhead to minimize the expanded view for a query.

    </div>

4.  Optional: Save the page URL to use this set of queries again in the future.

5.  Explore the visualized metrics. Initially, all metrics from all enabled queries are shown on the plot. Select which metrics are shown by performing any of the following actions:

    <table>
    <colgroup>
    <col style="width: 50%" />
    <col style="width: 50%" />
    </colgroup>
    <thead>
    <tr>
    <th style="text-align: left;">Option</th>
    <th style="text-align: left;">Description</th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td style="text-align: left;"><p>Hide all metrics from a query.</p></td>
    <td style="text-align: left;"><p>Click the options menu <img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABsAAAAjCAIAAADqn+bCAAAACXBIWXMAAA7EAAAOxAGVKw4bAAAA+0lEQVRIie2WMQqEMBBFJ47gUXRBLyBYqbUXULCx9CR2XsAb6AlUEM9kpckW7obdZhwWYWHXX/3i8TPJZEKEUgpOlXFu3JX4V4kmB2qaZhgGKSUiZlkWxzEBC84N9zxv27bdO47Tti0Bs3at4wBgXVca/lJnfN/XPggCGmadIwAsywIAiGhZFk1ydy2EYJKgGCqK4vZUVVU0zKpxnmftp2mi4S/1GhG1N82DMWNNYVmW4zgqpRAxTVMa5t4evlg11nXd9/1eY57nSZIQMKtG13WllLu3bbvrOgJmdUbHwfur8Xniqw6Hh5UYRdGDNowwDA+WvP4UV+JPJ94B1gKUWcTOCT0AAAAASUVORK5CYII=" alt="kebab" /> for the query and click <strong>Hide all series</strong>.</p></td>
    </tr>
    <tr>
    <td style="text-align: left;"><p>Hide a specific metric.</p></td>
    <td style="text-align: left;"><p>Go to the query table and click the colored square near the metric name.</p></td>
    </tr>
    <tr>
    <td style="text-align: left;"><p>Zoom into the plot and change the time range.</p></td>
    <td style="text-align: left;"><p>Perform one of the following actions:</p>
    <ul>
    <li><p>Visually select the time range by clicking and dragging on the plot horizontally.</p></li>
    <li><p>Use the menu to select the time range.</p></li>
    </ul></td>
    </tr>
    <tr>
    <td style="text-align: left;"><p>Reset the time range.</p></td>
    <td style="text-align: left;"><p>Click <strong>Reset zoom</strong>.</p></td>
    </tr>
    <tr>
    <td style="text-align: left;"><p>Display outputs for all queries at a specific point in time.</p></td>
    <td style="text-align: left;"><p>Hover over the plot at the point you are interested in. The query outputs appear in a pop-up box.</p></td>
    </tr>
    <tr>
    <td style="text-align: left;"><p>Hide the plot.</p></td>
    <td style="text-align: left;"><p>Click <strong>Hide graph</strong>.</p></td>
    </tr>
    </tbody>
    </table>

</div>

# Virtualization metrics

Metric descriptions including example Prometheus Query Language (PromQL) queries. These metrics are not an API and might change between versions.

> [!NOTE]
> The following examples use `topk` queries that specify a time period. If virtual machines (VMs) are deleted during that time period, they can still appear in the query output.

## vCPU metrics

The following query can identify virtual machines that are waiting for Input/Output (I/O):

`kubevirt_vmi_vcpu_wait_seconds_total`
Returns the wait time (in seconds) on I/O for vCPUs of a virtual machine. Type: Counter.

A value above '0' means that the vCPU wants to run, but the host scheduler cannot run it yet. This inability to run indicates that there is an issue with I/O.

> [!NOTE]
> To query the vCPU metric, the `schedstats=enable` kernel argument must first be applied to the `MachineConfig` object. This kernel argument enables scheduler statistics used for debugging and performance tuning and adds a minor additional load to the scheduler.

`kubevirt_vmi_vcpu_delay_seconds_total`
Returns the cumulative time, in seconds, that a vCPU was enqueued by the host scheduler but could not run immediately. This delay appears to the virtual machine as *steal time*, which is CPU time lost when the host runs other workloads. Steal time can impact performance and often indicates CPU overcommitment or contention on the host. Type: Counter.

Example vCPU delay query:

The following query returns the average per-second delay over a 5-minute period. A high value may indicate CPU overcommitment or contention on the node:

``` promql
irate(kubevirt_vmi_vcpu_delay_seconds_total[5m]) > 0.05
```

Example vCPU wait time query:

The following query returns the top 3 VMs waiting for I/O at every given moment over a six-minute time period:

``` promql
topk(3, sum by (name, namespace) (rate(kubevirt_vmi_vcpu_wait_seconds_total[6m]))) > 0
```

## Network metrics

The following queries can identify virtual machines that are saturating the network:

`kubevirt_vmi_network_receive_bytes_total`
Returns the total amount of traffic received (in bytes) on the virtual machine’s network. Type: Counter.

`kubevirt_vmi_network_transmit_bytes_total`
Returns the total amount of traffic transmitted (in bytes) on the virtual machine’s network. Type: Counter.

Example network traffic query:

The following query returns the top 3 VMs transmitting the most network traffic at every given moment over a six-minute time period:

``` promql
topk(3, sum by (name, namespace) (rate(kubevirt_vmi_network_receive_bytes_total[6m])) + sum by (name, namespace) (rate(kubevirt_vmi_network_transmit_bytes_total[6m]))) > 0
```

## Storage metrics

You can monitor virtual machine storage traffic and identify high-traffic VMs by using Prometheus queries.

The following queries can identify VMs that are writing large amounts of data:

`kubevirt_vmi_storage_read_traffic_bytes_total`
Returns the total amount (in bytes) of the virtual machine’s storage-related traffic. Type: Counter.

`kubevirt_vmi_storage_write_traffic_bytes_total`
Returns the total amount of storage writes (in bytes) of the virtual machine’s storage-related traffic. Type: Counter.

Example storage-related traffic queries:

- The following query returns the top 3 VMs performing the most storage traffic at every given moment over a six-minute time period:

  ``` promql
  topk(3, sum by (name, namespace) (rate(kubevirt_vmi_storage_read_traffic_bytes_total[6m])) + sum by (name, namespace) (rate(kubevirt_vmi_storage_write_traffic_bytes_total[6m]))) > 0
  ```

- The following query returns the top 3 VMs with the highest average read latency at every given moment over a six-minute time period:

  ``` promql
  topk(3, sum by (name, namespace) (rate(kubevirt_vmi_storage_read_times_seconds_total{name='${name}',namespace='${namespace}'${clusterFilter}}[6m]) / rate(kubevirt_vmi_storage_iops_read_total{name='${name}',namespace='${namespace}'${clusterFilter}}[6m]) > 0)) > 0
  ```

The following queries can track data restored from storage snapshots:

`vm:kubevirt_vmsnapshot_disks_restored:sum`
Returns the total number of virtual machine disks restored from the source virtual machine. Type: Gauge.

`vm:kubevirt_vmsnapshot_restored_bytes:sum`
Returns the amount of space in bytes restored from the source virtual machine. Type: Gauge.

Examples of storage snapshot data queries:

- The following query returns the total number of virtual machine disks restored from the source virtual machine:

  ``` promql
  vm:kubevirt_vmsnapshot_disks_restored:sum{vm_name="simple-vm", vm_namespace="default"}
  ```

- The following query returns the amount of space in bytes restored from the source virtual machine:

  ``` promql
  vm:kubevirt_vmsnapshot_restored_bytes:sum{vm_name="simple-vm", vm_namespace="default"}
  ```

The following queries can determine the I/O performance of storage devices:

`kubevirt_vmi_storage_iops_read_total`
Returns the amount of read I/O operations the virtual machine is performing per second. Type: Counter.

`kubevirt_vmi_storage_iops_write_total`
Returns the amount of write I/O operations the virtual machine is performing per second. Type: Counter.

Example I/O performance query:

The following query returns the top 3 VMs performing the most I/O operations per second at every given moment over a six-minute time period:

``` promql
topk(3, sum by (name, namespace) (rate(kubevirt_vmi_storage_iops_read_total[6m])) + sum by (name, namespace) (rate(kubevirt_vmi_storage_iops_write_total[6m]))) > 0
```

## Guest memory swapping metrics

The following queries can identify which swap-enabled guests are performing the most memory swapping:

`kubevirt_vmi_memory_swap_in_traffic_bytes`
Returns the total amount (in bytes) of memory the virtual guest is swapping in. Type: Gauge.

`kubevirt_vmi_memory_swap_out_traffic_bytes`
Returns the total amount (in bytes) of memory the virtual guest is swapping out. Type: Gauge.

Example memory swapping query:

The following query returns the top 3 VMs where the guest is performing the most memory swapping at every given moment over a six-minute time period:

``` promql
topk(3, sum by (name, namespace) (rate(kubevirt_vmi_memory_swap_in_traffic_bytes[6m])) + sum by (name, namespace) (rate(kubevirt_vmi_memory_swap_out_traffic_bytes[6m]))) > 0
```

> [!NOTE]
> Memory swapping indicates that the virtual machine is under memory pressure. Increasing the memory allocation of the virtual machine can mitigate this issue.

## Monitoring AAQ operator metrics

The following metrics are exposed by the Application Aware Quota (AAQ) controller for monitoring resource quotas:

`kube_application_aware_resourcequota`
Returns the current quota usage and the CPU and memory limits enforced by the AAQ Operator resources. Type: Gauge.

`kube_application_aware_resourcequota_creation_timestamp`
Returns the time, in UNIX timestamp format, when the AAQ Operator resource is created. Type: Gauge.

## VM label metrics

`kubevirt_vm_labels`
Returns virtual machine labels as Prometheus labels. Type: Gauge.

You can expose and ignore specific labels by editing the `kubevirt-vm-labels-config` config map. After you apply the config map to your cluster, the configuration is loaded dynamically.

Example config map:

``` yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: kubevirt-vm-labels-config
  namespace: openshift-cnv
data:
  allowlist: "*"
  ignorelist: ""
```

- `data.allowlist` specifies labels to expose.

  - If `data.allowlist` has a value of `"*"`, all labels are included.

  - If `data.allowlist` has a value of `""`, the metric does not return any labels.

  - If `data.allowlist` contains a list of label keys, only the explicitly named labels are exposed. For example: `allowlist: "example.io/name,example.io/version"`.

- `data.ignorelist` specifies labels to ignore. The ignore list overrides the allow list.

  - The `data.ignorelist` field does not support wildcard patterns. It can be empty or include a list of specific labels to ignore.

  - If `data.ignorelist` has a value of `""`, no labels are ignored.

## Live migration metrics

You can query metrics to show live migration status.

`kubevirt_vmi_migration_data_processed_bytes`
The amount of guest operating system data that has migrated to the new virtual machine (VM). Type: Gauge.

`kubevirt_vmi_migration_data_remaining_bytes`
The amount of guest operating system data that remains to be migrated. Type: Gauge.

`kubevirt_vmi_migration_memory_transfer_rate_bytes`
The rate at which memory is becoming dirty in the guest operating system. Dirty memory is data that has been changed but not yet written to disk. Type: Gauge.

`kubevirt_vmi_migrations_in_pending_phase`
The number of pending migrations. Type: Gauge.

`kubevirt_vmi_migrations_in_scheduling_phase`
The number of scheduling migrations. Type: Gauge.

`kubevirt_vmi_migrations_in_running_phase`
The number of running migrations. Type: Gauge.

`kubevirt_vmi_migration_succeeded`
The number of successfully completed migrations. Type: Gauge.

`kubevirt_vmi_migration_failed`
The number of failed migrations. Type: Gauge.

# Node Memory Overcommit dashboard

The Node Memory Overcommit dashboard displays physical and virtual memory utilization across the cluster, focusing on how virtual machines (VMs) affect node memory.

Use this dashboard to monitor memory capacity, detect memory pressure, identify overcommitment risks, and validate that system processes do not exceed their reserved memory.

You can access this dashboard from the web console in **Observe** → **Dashboards (Perses)**.

## Dashboard filters

The dashboard provides two filter variables in the top toolbar:

| Filter | Description | Default |
|----|----|----|
| **Node** | Filters all panels to display information about one or more nodes in the cluster. | **All** |
| **role** | Filters all panels to display information about nodes with a specific Kubernetes role, populated from `kube_node_role`. | **worker** |

You can also change the time range displayed in the different panels in the top toolbar of the dashboard.

## Summary section

The **Summary** section provides a high-level overview of cluster memory health. The panels in this section provide general memory utilization data for the cluster and the nodes. Most of the panels in this section appear in other sections of the dashboard as well. However, the following panels are unique to the **Summary** section:

| Panel | Type | Description |
|----|----|----|
| **Node Utilization - max** | Gauge | Displays the highest node utilization in the cluster. Use this panel together with the **Node Utilization - min** panel to assess scheduling balance. A large gap between minimum and maximum node utilization indicates an imbalanced workload distribution. |
| **Cluster Utilization** | Time series | Displays the trend over time of several memory metrics. Use this panel to compare actual utilization and virtual memory plans against total capacity. |

## Cluster section

The **Cluster** section provides a more detailed view of cluster-wide memory behavior over a range of time. This section includes the following panels:

| Panel | Type | Description |
|----|----|----|
| **Physical Memory Utilization & Requests** | Time series | Displays the total node memory capacity alongside actual memory utilization split into virtualization and non-virtualization workloads. This panel also shows the memory request plan (system-reserved requests and pod requests) so that you can compare actual usage to the scheduler expectations. |
| **Cluster Utilization** | Gauge | Displays the aggregated memory utilization of the nodes in the cluster. This panel also appears in the **Summary** section. |
| **Virtual Memory Assignment** | Time series | This panel displays the worst-case scenario if all virtual memory is used at present. It shows total node capacity, utilization without virtualization, and non-virtualization utilization combined with the total assigned VM memory. If the **VM assigned virtual memory** line nears or exceeds **Node capacity**, the cluster risks out-of-memory conditions under full VM memory pressure. |
| **Cluster Virtual Committed** | Gauge | Displays the percentage of committed virtual memory out of all of the allocatable physical memory. This panel also appears in the **Summary** section. |
| **Cluster - Memory Pressure** | Time series | Shows cluster-level memory PSI rates for `Waiting` (processes delayed by memory) and `Stalled` (processes completely blocked). |
| **Cluster - Aggregated Swap** | Time series | Shows total swap capacity and usage across all the nodes that you select. Rising swap usage indicates memory pressure that has not yet caused PSI stalls. |

## Nodes section

The **Nodes** section breaks down memory information per node to help identify imbalances. This section includes the following panels:

| Panel | Type | Description |
|----|----|----|
| **Utilization - Actual Overcommit Level** | Time series | Displays the per-node allocatable memory utilization minus the system-reserved memory. |
| **Node Utilization - min** | Gauge | Displays the lowest node utilization in the cluster. This panel also appears in the **Summary** section. |
| **Plan - Pod Requests per Node** | Time series | Shows the memory request fill level per node: the sum of all pod memory requests on a node divided by the node’s allocatable memory. |
| **Node Requests - min/max** | Stat | Displays the minimum and maximum pod request ratios per node. Use this panel to quickly assess the cluster’s remaining capacity to host new workloads. |
| **Plan - Virtual Memory Commit Level** | Time series | Displays the virtual memory commit ratio per node. The panel compares total active and assigned VM memory against the node’s available memory. |
| **Node Virtual - min/max** | Stat | Displays the minimum and maximum virtual commit levels per node. |
| **Node - Pressure** | Time series | Displays the memory PSI waiting rate per node. Each line represents one node to help you identify which nodes experience memory contention. |
| **Node PSI - max** | Gauge | Displays the highest PSI value across all nodes. PSI shows the amount of time applications are stalled or delayed waiting for memory resources. This panel also appears in the **Summary** section. |

## System Reserved section

The **System Reserved** section monitors whether the system (hypervisor) processes stay within their reserved memory budget. This section includes the following panels:

| Panel | Type | Description |
|----|----|----|
| **Utilization - Reserved System Memory** | Time series | Displays the top 5 nodes by system-reserved memory utilization. This metric compares active system process memory against the reserved memory budget. |
| **Utilization - min/max** | Time series | Displays the minimum and maximum system-reserved memory utilization across all nodes over time. |
| **System Exceeding Reservation** | Stat | Displays the percentage or number of nodes out of all monitored nodes that are currently triggering the `SystemMemoryExceedsReservation` alert. This panel also appears in the **Summary** section. |

## Workloads section

The **Workloads** section, which is collapsed by default, focuses on individual VM memory behavior.

| Panel | Type | Description |
|----|----|----|
| **VM Overcommit Ratio** | Time series | Displays the ratio of assigned virtual memory to pod memory requests for each VM. |
| **VM Virtual Committed** | Gauge | Displays the average VM overcommit ratio, which includes launcher overhead. This panel also appears in the **Summary** section. |
| **VM Virtual Memory Utilization vs Host VM Utilization** | Time series | Displays the 10 VMs with the highest ratio between guest-reported memory usage and host-side container memory usage. Use this panel to identify VMs where guest-reported usage differs significantly from host-side accounting. This difference indicates balloon driver effectiveness or memory accounting discrepancies. |
| **Number of Running VMs** | Time series | Displays the total number of running virtual machine instances (VMIs) on the cluster to provide context for the other workload panels. |

## Interpreting the dashboard

Monitor the dashboard indicators in the **Summary** section to identify early warning signs of memory pressure and prevent critical out-of-memory events.

Healthy state
The **Cluster Utilization** panel gauge is green (below 70%), the **Cluster Virtual Committed** panel gauge is below 120%, the **Node PSI - max** values are near zero, and no nodes exceed their system reservation.

Warning signs
Utilization gauges turn amber (80% to 90%), the virtual commit approaches 150%, or individual nodes diverge significantly from the cluster average, which suggests imbalanced scheduling.

Critical state
Utilization gauges turn red (above 90%), PSI values exceed 0.5, system reservation is exceeded on any node, or virtual commit ratios per node exceed 200%. These conditions indicate that the cluster is at risk of out-of-memory events and VM eviction.

# Additional resources

- [KubeVirt components metrics](https://github.com/kubevirt/monitoring/blob/main/docs/metrics.md)

- [Adding kernel arguments to nodes](../../machine_configuration/machine-configs-configure.md#nodes-nodes-kernel-arguments_machine-configs-configure)

- [About OpenShift Container Platform monitoring](https://docs.redhat.com/en/documentation/monitoring_stack_for_red_hat_openshift/latest/html/about_monitoring/about-ocp-monitoring)

- [Querying Prometheus](https://prometheus.io/docs/prometheus/latest/querying/basics/)

- [Prometheus query examples](https://prometheus.io/docs/prometheus/latest/querying/examples/)
