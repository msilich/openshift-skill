<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Monitor the consumption of cluster infrastructure resources using the metrics provided by OpenShift Virtualization. These metrics are also used to query live migration status.

<div class="note">

<div class="title">

</div>

- To use the vCPU metric, apply the `schedstats=enable` kernel argument to the `MachineConfig` object. This kernel argument enables scheduler statistics used for debugging and performance tuning and adds a minor additional load to the scheduler.

- For guest memory swapping queries to return data, memory swapping must be enabled on the virtual guests.

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

As a developer, you must specify a project name when querying metrics. You must have the required privileges to view metrics for the selected project.

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

`kubevirt_vmsnapshot_disks_restored_from_source`
Returns the total number of virtual machine disks restored from the source virtual machine. Type: Gauge.

`kubevirt_vmsnapshot_disks_restored_from_source_bytes`
Returns the amount of space in bytes restored from the source virtual machine. Type: Gauge.

Examples of storage snapshot data queries:

- The following query returns the total number of virtual machine disks restored from the source virtual machine:

  ``` promql
  kubevirt_vmsnapshot_disks_restored_from_source{vm_name="simple-vm", vm_namespace="default"}
  ```

- The following query returns the amount of space in bytes restored from the source virtual machine:

  ``` promql
  kubevirt_vmsnapshot_disks_restored_from_source_bytes{vm_name="simple-vm", vm_namespace="default"}
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
+
```

> [!NOTE]
> Memory swapping indicates that the virtual machine is under memory pressure. Increasing the memory allocation of the virtual machine can mitigate this issue.

## Monitoring AAQ operator metrics

The following metrics are exposed by the Application Aware Quota (AAQ) controller for monitoring resource quotas:

`kube_application_aware_resourcequota`
Returns the current quota usage and the CPU and memory limits enforced by the AAQ Operator resources. Type: Gauge.

`kube_application_aware_resourcequota_creation_timestamp`
Returns the time, in UNIX timestamp format, when the AAQ Operator resource is created. Type: Gauge.

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

# Additional resources

- [KubeVirt components metrics](https://github.com/kubevirt/monitoring/blob/main/docs/metrics.md)

- [Adding kernel arguments to nodes](../../machine_configuration/machine-configs-configure.md#nodes-nodes-kernel-arguments_machine-configs-configure)

- [About OpenShift Container Platform monitoring](https://docs.redhat.com/en/documentation/monitoring_stack_for_red_hat_openshift/4.20/html/about_monitoring/about-ocp-monitoring)

- [Querying Prometheus](https://prometheus.io/docs/prometheus/latest/querying/basics/)

- [Prometheus query examples](https://prometheus.io/docs/prometheus/latest/querying/examples/)
